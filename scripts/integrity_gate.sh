#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

echo "==> Integrity gate: clean rebuild"
make veryclean
make -j1

# One extra pass stabilizes hyperref destination anchors after large cross-reference churn.
pdflatex -interaction=nonstopmode -file-line-error -synctex=1 main.tex >/tmp/integrity_stabilize.log 2>&1

log="main.log"
if [[ ! -f "$log" ]]; then
  echo "ERROR: $log not found after build."
  exit 1
fi

count_log() {
  local pattern="$1"
  grep -aE -c "$pattern" "$log" || true
}

fail=0

# Baseline-tolerated typography diagnostics (non-structural); tighten over time.
max_overfull="${MAX_OVERFULL:-5}"
max_underfull="${MAX_UNDERFULL:-300}"
max_float_too_large="${MAX_FLOAT_TOO_LARGE:-0}"
max_hyperref_warn="${MAX_HYPERREF_WARN:-220}"

echo "==> Structural metrics"
metrics=(
  "LATEX_ERRORS|^! LaTeX Error:"
  "UNDEF_CTRL|^! Undefined control sequence\\."
  "UNDEF_REF|LaTeX Warning: Reference \`[^\`]+\` on page [0-9]+ undefined"
  "UNDEF_CITE|LaTeX Warning: Citation \`[^\`]+\` on page [0-9]+ undefined"
  "MULTI_LABEL|LaTeX Warning: Label \`[^\`]+\` multiply defined"
  "OVERFULL|Overfull \\\\hbox"
  "UNDERFULL|Underfull \\\\hbox|Underfull \\\\vbox"
  "FLOAT_TOO_LARGE|Float too large for page"
  "HYPERREF_WARN|Package hyperref Warning"
  "BOOKMARK_INFO|bookmark level for unknown"
  "PDFTEX_DEST_MISSING|pdfTeX warning \\(dest\\): name\\{[^}]+\\} has been referenced but does not exist"
  "NTXEBGMIA_MISMATCH|ntxebgmia\\.vf.*checksum mismatch|ntxebgmia\\.vf.*design size mismatch|ntxebgmia\\.vf.*charht values differ"
)

for item in "${metrics[@]}"; do
  key="${item%%|*}"
  pat="${item#*|}"
  val="$(count_log "$pat")"
  echo "  $key=$val"
  case "$key" in
    OVERFULL)
      if (( val > max_overfull )); then fail=1; fi
      ;;
    UNDERFULL)
      if (( val > max_underfull )); then fail=1; fi
      ;;
    FLOAT_TOO_LARGE)
      if (( val > max_float_too_large )); then fail=1; fi
      ;;
    HYPERREF_WARN)
      if (( val > max_hyperref_warn )); then fail=1; fi
      ;;
    *)
      if [[ "$val" != "0" ]]; then fail=1; fi
      ;;
  esac
done
echo "  LIMIT_OVERFULL=$max_overfull"
echo "  LIMIT_UNDERFULL=$max_underfull"
echo "  LIMIT_FLOAT_TOO_LARGE=$max_float_too_large"
echo "  LIMIT_HYPERREF_WARN=$max_hyperref_warn"

echo "==> Repository-wide label uniqueness"
dup_keys="$(
  { rg --files -g '*.tex' \
    | xargs -I{} grep -a -oE '\\label\\{[^}]+\\}' '{}' 2>/dev/null || true; } \
    | sed -E 's/\\label\\{([^}]+)\\}/\\1/' \
    | sort \
    | uniq -d \
    | wc -l \
    | tr -d ' '
)"
echo "  REPO_DUP_LABEL_KEYS=$dup_keys"
if [[ "$dup_keys" != "0" ]]; then
  fail=1
fi

echo "==> Claim-status coverage (active include graph)"
read -r heads tagged untagged < <(
python3 - <<'PY'
import pathlib
import re

main = pathlib.Path("main.tex").read_text(encoding="utf-8", errors="ignore")
main = "\n".join([ln.split("%", 1)[0] for ln in main.splitlines()])

active = []
for m in re.finditer(r'\\(?:include|input)\{([^}]+)\}', main):
    p = m.group(1)
    if not (p.startswith("chapters/") or p.startswith("appendices/")):
        continue
    if not p.endswith(".tex"):
        p += ".tex"
    pp = pathlib.Path(p)
    if pp.is_file():
        active.append(pp)

seen = set()
uniq = []
for p in active:
    if p not in seen:
        seen.add(p)
        uniq.append(p)

head_re = re.compile(r'\\begin\{(theorem|lemma|proposition|corollary)\}')
status_re = re.compile(
    r'\\ClaimStatus(?:ProvedHere|ProvedElsewhere|Open|Conjectured|Conditional|Heuristic)'
)

heads = 0
tagged = 0
for path in uniq:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for i, line in enumerate(lines):
        if head_re.search(line):
            heads += 1
            window = "\n".join(lines[i:i+8])
            if status_re.search(window):
                tagged += 1

untagged = heads - tagged
print(f"{heads} {tagged} {untagged}")
PY
)

echo "  ACTIVE_CLAIM_HEADS=$heads"
echo "  ACTIVE_TAGGED=$tagged"
echo "  ACTIVE_UNTAGGED=$untagged"
if [[ "$untagged" != "0" ]]; then
  fail=1
fi

echo "==> Route-discipline coverage (active include graph)"
read -r active_files gq_missing hms_missing < <(
python3 - <<'PY'
import pathlib
import re

main = pathlib.Path("main.tex").read_text(encoding="utf-8", errors="ignore")
main = "\n".join([ln.split("%", 1)[0] for ln in main.splitlines()])

active = []
for m in re.finditer(r'\\(?:include|input)\{([^}]+)\}', main):
    p = m.group(1)
    if not (p.startswith("chapters/") or p.startswith("appendices/")):
        continue
    if not p.endswith(".tex"):
        p += ".tex"
    pp = pathlib.Path(p)
    if pp.is_file():
        active.append(pp)

seen = set()
uniq = []
for p in active:
    if p not in seen:
        seen.add(p)
        uniq.append(p)

gq_missing = 0
hms_missing = 0
hms_re = re.compile(r'conv:hms-levels|semantic levels', re.IGNORECASE)

for path in uniq:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "governing question" not in text.lower():
        gq_missing += 1
    if not hms_re.search(text):
        hms_missing += 1

print(f"{len(uniq)} {gq_missing} {hms_missing}")
PY
)

echo "  ACTIVE_FILES=$active_files"
echo "  ACTIVE_GQ_MISSING=$gq_missing"
echo "  ACTIVE_HMS_MISSING=$hms_missing"
if [[ "$gq_missing" != "0" || "$hms_missing" != "0" ]]; then
  fail=1
fi

echo "==> Virasoro shadow doctrine (active include graph)"
vir_shadow_drift="$(
python3 - <<'PY'
import pathlib
import re

main = pathlib.Path("main.tex").read_text(encoding="utf-8", errors="ignore")
main = "\n".join([ln.split("%", 1)[0] for ln in main.splitlines()])

active = []
for m in re.finditer(r'\\(?:include|input)\{([^}]+)\}', main):
    p = m.group(1)
    if not (p.startswith("chapters/") or p.startswith("appendices/")):
        continue
    if not p.endswith(".tex"):
        p += ".tex"
    pp = pathlib.Path(p)
    if pp.is_file():
        active.append(pp)

seen = set()
uniq = []
for p in active:
    if p not in seen:
        seen.add(p)
        uniq.append(p)

triggers = [
    re.compile(r"Virasoro[^.\n]{0,140}\bhas a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\badmits? a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\brequires completion[^.\n]{0,80}\bKoszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bKoszul dual is\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual algebra\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual object\b", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_\\infty", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_infty", re.IGNORECASE),
]
safe = [
    re.compile(r"same-family", re.IGNORECASE),
    re.compile(r"\bshadow\b", re.IGNORECASE),
    re.compile(r"self-dual", re.IGNORECASE),
    re.compile(r"m/s-level", re.IGNORECASE),
    re.compile(r"\bm-level\b", re.IGNORECASE),
    re.compile(r"\bs-level\b", re.IGNORECASE),
    re.compile(r"\bmc4\b", re.IGNORECASE),
    re.compile(r"completion frontier", re.IGNORECASE),
    re.compile(r"realization problem", re.IGNORECASE),
    re.compile(r"infinite-generator", re.IGNORECASE),
    re.compile(r"does not yet", re.IGNORECASE),
    re.compile(r"not yet", re.IGNORECASE),
]

count = 0
for path in uniq:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for i, line in enumerate(lines):
        if not any(p.search(line) for p in triggers):
            continue
        window = "\n".join(lines[max(0, i - 2):min(len(lines), i + 4)])
        if not any(p.search(window) for p in safe):
            count += 1

print(count)
PY
)"
echo "  VIRASORO_SHADOW_DRIFT=$vir_shadow_drift"
if [[ "$vir_shadow_drift" != "0" ]]; then
  fail=1
fi

echo "==> Infinite-generator frontier doctrine (active include graph)"
inf_gen_drift="$(
python3 - <<'PY'
import pathlib
import re

main = pathlib.Path("main.tex").read_text(encoding="utf-8", errors="ignore")
main = "\n".join([ln.split("%", 1)[0] for ln in main.splitlines()])

active = []
for m in re.finditer(r'\\(?:include|input)\{([^}]+)\}', main):
    p = m.group(1)
    if not (p.startswith("chapters/") or p.startswith("appendices/")):
        continue
    if not p.endswith(".tex"):
        p += ".tex"
    pp = pathlib.Path(p)
    if pp.is_file():
        active.append(pp)

seen = set()
uniq = []
for p in active:
    if p not in seen:
        seen.add(p)
        uniq.append(p)

triggers = [
    re.compile(r"W_\\infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_\\infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
]
safe = [
    re.compile(r"\bmc4\b", re.IGNORECASE),
    re.compile(r"theorem-ready", re.IGNORECASE),
    re.compile(r"frontier", re.IGNORECASE),
    re.compile(r"inverse-limit", re.IGNORECASE),
    re.compile(r"completed bar", re.IGNORECASE),
    re.compile(r"continuity", re.IGNORECASE),
    re.compile(r"stabilization", re.IGNORECASE),
    re.compile(r"surjectiv", re.IGNORECASE),
    re.compile(r"mittag", re.IGNORECASE),
    re.compile(r"not yet", re.IGNORECASE),
    re.compile(r"does not yet", re.IGNORECASE),
    re.compile(r"realization problem", re.IGNORECASE),
]

count = 0
for path in uniq:
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for i, line in enumerate(lines):
        if not any(p.search(line) for p in triggers):
            continue
        window = "\n".join(lines[max(0, i - 2):min(len(lines), i + 4)])
        if not any(p.search(window) for p in safe):
            count += 1

print(count)
PY
)"
echo "  INFINITE_GENERATOR_DRIFT=$inf_gen_drift"
if [[ "$inf_gen_drift" != "0" ]]; then
  fail=1
fi

echo "==> Manuscript QC (active structural checks)"
qc_log="$(mktemp)"
if ./scripts/manuscript_qc.py --strict >"$qc_log"; then
  sed -n '1,12p' "$qc_log"
else
  cat "$qc_log"
  fail=1
fi
rm -f "$qc_log"

if [[ "$fail" -ne 0 ]]; then
  echo "==> Integrity gate FAILED"
  exit 1
fi

echo "==> Integrity gate PASSED"
