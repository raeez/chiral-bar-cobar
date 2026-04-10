% Hook Enhancements Wave 12 -- Proposals for catching repeat AP violations at the PreToolUse / PostToolUse boundary

## 0. Scope

This document proposes additions/enhancements to the hook scripts located at:

- /Users/raeez/chiral-bar-cobar/.claude/hooks/beilinson-gate.sh        (Vol I   -- PostToolUse Edit|Write)
- /Users/raeez/chiral-bar-cobar/.claude/hooks/convergence-gate.sh      (Vol I   -- Stop)
- /Users/raeez/chiral-bar-cobar-vol2/.claude/hooks/beilinson-gate.sh   (Vol II  -- PostToolUse Edit|Write)
- /Users/raeez/chiral-bar-cobar-vol2/.claude/hooks/convergence-gate.sh (Vol II  -- Stop)
- /Users/raeez/calabi-yau-quantum-groups/.claude/hooks/beilinson-gate.sh   (Vol III -- PostToolUse Edit|Write)
- /Users/raeez/calabi-yau-quantum-groups/.claude/hooks/convergence-gate.sh (Vol III -- Stop)

PreToolUse is wired only for `Bash(*git commit*)` via settings.json. There is currently NO PreToolUse Edit|Write gate in any volume.

All proposals below are drop-in snippets for `beilinson-gate.sh`. The existing pattern is:

```bash
if grep -Eq '<regex>' "$FILE_PATH" 2>/dev/null; then
  MATCHES=$(grep -En '<regex>' "$FILE_PATH" | head -3)
  if [ -n "$MATCHES" ]; then
    ISSUES="${ISSUES}APxxx: <message>. Lines: ${MATCHES}\n"   # or WARNINGS
  fi
fi
```

Proposals are split into three classes:

- **PreToolUse Edit** (needs a new hook file + settings.json wiring). Blocks the WRITE before it lands. Reserved for catastrophic pattern leaks (tool-markup, AI attribution).
- **PostToolUse BLOCK** (append to beilinson-gate.sh, push to ISSUES). Loud signal that forces an immediate fix before further work.
- **PostToolUse WARN** (append to beilinson-gate.sh, push to WARNINGS). Quiet signal that the agent should verify.

## 1. Current coverage inventory (what the hooks already catch)

beilinson-gate.sh today covers:

| AP | Status | Method |
|----|--------|--------|
| AP7/AP32 | WARN | "for all / universally" scope inflation |
| AP8 | BLOCK | self-dual Virasoro without c=13 |
| AP10 | WARN (.py) | hardcoded assertions without cross-checks |
| AP14 | WARN | "not Koszul / non-Koszul" |
| AP19 | WARN | r-matrix with OPE pole orders |
| AP24 | BLOCK | unqualified kappa+kappa'=0 |
| AP25/AP34 | BLOCK | bar-cobar produces bulk |
| AP27 | WARN | Hodge bundle E_h |
| AP33 | BLOCK | H_k^! = H_{-k} |
| AP40 | BLOCK | ClaimStatusConjectured inside theorem |
| AP44 | WARN | lambda-bracket c/2 vs c/12 |
| AP45 | WARN | desuspension sign |
| AP106/RS-5 | BLOCK | "this chapter constructs" openings |
| AP113 | BLOCK (Vol III only) | bare kappa without subscript |
| AP117 | WARN | d log vs dz in KZ |
| AP121 | BLOCK | Markdown backtick numerals |
| AP124 | WARN | duplicate labels |
| V2-AP26 | WARN | hardcoded Part~I numbers |
| PROSE | BLOCK | AI slop word list (~20 words) |
| PROSE | BLOCK | 11 signpost phrases |
| PROSE | BLOCK | Moreover/Additionally/Furthermore sentence openers |
| AAP1 | BLOCK | antml / </invoke> / <tool_call> leakage |
| AP-OC | BLOCK (Vol II) | bar = bulk |
| V2-AP1/AP43 | BLOCK (Vol II) | "VAs are not E_infty" |
| AP-CY6 | WARN (Vol III) | A_X for CY3 treated as existing |
| AP-CY7 | WARN (Vol III) | CoHA = E_1 chiral algebra |
| AP43 | WARN (Vol III) | G(X) without definition |
| AP49 | WARN (Vol III) | cross-volume convention reference |

Cross-volume propagation reminder fires on any edit touching kappa, Theta, lambda_g, F_g, E_1, E_infty, CY functor, etc.

The convergence gate (Stop hook) only covers skill-invoked rectification sessions. Untouched by the proposals below; it is working as designed.

## 2. Gaps identified (what is slipping through)

Wave audits found the following repeat violations that the current hook did NOT catch:

1. **Bare Omega/z r-matrix** (AP126 / AP141): 42+ instances across all three volumes. Most-violated AP in the manuscript. No existing check.
2. **Label/environment prefix mismatch** (AP125): `\begin{conjecture} ... \label{thm:...}`. Current hook only catches AP40 (ClaimStatusConjectured inside theorem), not the inverse prefix error.
3. **Bar augmentation ideal missing** (AP132): `T^c(s^{-1} A)` instead of `T^c(s^{-1} \bar A)`. No check.
4. **Summation boundary** (AP116): `\sum_{j=1}^{N-1}` when meaning `H_N`. No check.
5. **Harmonic-number shift confusion** (AP136): `H_{N-1}` vs `H_N - 1`. No check.
6. **Bosonic/fermionic partner sign** (AP137): `c_{\beta\gamma}` vs `c_{bc}`. No check.
7. **Reciprocal transcription** (AP129): `S_4 = -(5c+22)/(10c)` instead of `10/[c(5c+22)]`. Cannot be caught by regex alone; needs numerical probe.
8. **Fiber-base confusion** (AP130): `omega_g = d\tau` (form on fiber assigned to class on moduli). No check.
9. **Partition number family** (AP135): bicoloured partitions confused with triangular numbers. Test-time only.
10. **Em dashes** (AP121 extension): U+2014 in .tex. No check.
11. **`\newcommand` in chapter** (LaTeX preamble discipline): no check.
12. **`\cite{key}` / `\ref{label}` unresolved** in standalones. No check.
13. **AI attribution in commit messages and .tex** (AAP-git): no check.
14. **Stray `\end{environment>`** (typo introduced by tool-call leak residue): no check.
15. **Vol II standalone artifact leak** (V2-AP32): `\title{}`, `\begin{abstract}`, `\tableofcontents`, `\date{}`, `\author{}` inside chapter files `\input{}`'d into main.tex. No check.
16. **lambda-bracket convention drift** (V2-AP34): `c/2 \lambda^3` in Vol II (should be `c/12 \lambda^3`). No check.
17. **Bare `\kappa = S_2`** (AP39): forgetting Virasoro-only caveat. No check.
18. **`av(r(z)) = \kappa`** without Sugawara shift note (AP98). No check.
19. **`RECTIFICATION-FLAG`** debt (V2-AP33): left in file permanently. No check.
20. **Unresolved "therefore"** after correction (V2-AP35). No check.

## 3. Proposed hooks (organized by severity)

Each proposal gives: Trigger, drop-in bash/regex, fail message, severity, expected APs prevented, false-positive risk.

### 3.1 BLOCK (correctness-critical)

---

#### H1. AP126/AP141 -- Bare Omega/z r-matrix

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `\Omega/z` or `\Omega / z` NOT preceded by `k`, `k\,`, `k(k+h^\vee)`, `\hbar`, `(k+h^\vee)`, `\frac{k}`, or a numeric coefficient. Additionally require the context to mention "r-matrix" or `r(z)` within 3 lines (to avoid false hits on Riemann Omega in other contexts).

```bash
# AP126/AP141: Bare Omega/z r-matrix
if grep -En '\\Omega\s*/\s*z' "$FILE_PATH" 2>/dev/null | grep -v 'k\s*\\\?,?\s*\\Omega\|\\hbar\s*\\\?,?\s*\\Omega\|k(k+h\^\\vee)\s*\\Omega\|(k+h\^\\vee)\s*\\Omega\|\\frac{k}.*\\Omega\|[0-9]\s*\\Omega' > /tmp/ap126_hits 2>/dev/null; then
  if [ -s /tmp/ap126_hits ]; then
    CONTEXT_HITS=$(while IFS=: read -r LN _; do
      START=$((LN - 3)); [ $START -lt 1 ] && START=1
      END=$((LN + 3))
      if sed -n "${START},${END}p" "$FILE_PATH" | grep -qi 'r-matrix\|r(z)\|classical.*r\|KZ\|Knizhnik'; then
        sed -n "${LN}p" "$FILE_PATH" | head -c 200
        echo " [line $LN]"
      fi
    done < /tmp/ap126_hits | head -3)
    if [ -n "$CONTEXT_HITS" ]; then
      ISSUES="${ISSUES}AP126/AP141: Bare \\Omega/z in r-matrix context. Level prefix MISSING. Use k\\Omega/z (affine KM level k) or \\hbar\\Omega/z (quantum). Verify: at k=0 the r-matrix MUST vanish. Hits: ${CONTEXT_HITS}\n"
    fi
  fi
  rm -f /tmp/ap126_hits
fi
```

**Fail message:** `AP126/AP141: Bare \Omega/z in r-matrix context. Level prefix MISSING. Use k\Omega/z (affine KM level k) or \hbar\Omega/z (quantum). Verify: at k=0 the r-matrix MUST vanish.`

**Severity:** BLOCK

**Expected APs prevented:** AP126, AP141 (the single most-violated AP; 42+ historical instances).

**False-positive risk:** MEDIUM. `\Omega` is used for period matrices (Im Omega), for M-bar_{g,n} boundary forms (omega_g), and for volume forms. The `/z` + r-matrix-context guard filters these out. Still, any `\Omega/z_{ij}` in a KZ line without explicit level prefix will fire; that is usually a real violation (the level k is outside the sum but should be factored in).

---

#### H2. AP125 -- Label/environment prefix mismatch

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** For each `\begin{ENV}[...]\label{PREFIX:...}` block within 5 lines of each other, check that PREFIX matches ENV:

- `theorem` -> `thm:`
- `proposition` -> `prop:`
- `lemma` -> `lem:`
- `corollary` -> `cor:`
- `conjecture` -> `conj:`
- `definition` -> `def:`
- `remark` -> `rem:`
- `example` -> `ex:`

```bash
# AP125: Label prefix must match environment
for ENV in theorem proposition lemma corollary conjecture definition remark example; do
  case "$ENV" in
    theorem)     PREFIX="thm:"  ;;
    proposition) PREFIX="prop:" ;;
    lemma)       PREFIX="lem:"  ;;
    corollary)   PREFIX="cor:"  ;;
    conjecture)  PREFIX="conj:" ;;
    definition)  PREFIX="def:"  ;;
    remark)      PREFIX="rem:"  ;;
    example)     PREFIX="ex:"   ;;
  esac
  # Look for \begin{ENV} followed within 5 lines by a label with a DIFFERENT prefix
  awk -v env="$ENV" -v prefix="$PREFIX" '
    $0 ~ "\\\\begin\\{"env"\\}" { watch=NR+5; begin_line=NR }
    watch && NR<=watch && /\\label\{/ {
      if (match($0, /\\label\{[a-z]+:/)) {
        found=substr($0, RSTART+7, RLENGTH-8)
        if (found != prefix) {
          print begin_line": \\begin{"env"} but \\label{"found"...} (expected "prefix"...)"
        }
      }
      watch=0
    }
  ' "$FILE_PATH" > /tmp/ap125_hits 2>/dev/null
  if [ -s /tmp/ap125_hits ]; then
    HITS=$(head -3 /tmp/ap125_hits)
    ISSUES="${ISSUES}AP125: Label prefix mismatch. ${HITS}\n"
  fi
  rm -f /tmp/ap125_hits
done
```

**Fail message:** `AP125: Label prefix must match environment. When upgrading/downgrading, rename label AND update all \ref instances atomically.`

**Severity:** BLOCK

**Expected APs prevented:** AP125. Catches the "stale thm: prefix on a conjecture" pattern.

**False-positive risk:** LOW. The 5-line window is tight; if an agent intentionally labels a remark inside a theorem block, they are fighting the convention anyway.

---

#### H3. AP132 -- Augmentation ideal in bar complex

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `T^c(s^{-1} A)` where the `A` is NOT `\bar A`, `\overline A`, `\bar{A}`, `\overline{A}`, `A^+`, or an ideal-marked A.

```bash
# AP132: Bar complex must use augmentation ideal
if grep -En 'T\^c\s*\(\s*s\^\{-?1\}\s*A[^+\\-]' "$FILE_PATH" 2>/dev/null | grep -v '\\bar\s*A\|\\overline\s*{?A\|A\^+\|A\^{?+}\|\\bar{A}\|\\overline{A}' > /tmp/ap132_hits; then
  if [ -s /tmp/ap132_hits ]; then
    HITS=$(head -3 /tmp/ap132_hits)
    ISSUES="${ISSUES}AP132: Bar complex B(A)=T^c(s^{-1}\\bar A) uses the AUGMENTATION IDEAL \\bar A=ker(epsilon), NOT A. Hits: ${HITS}\n"
  fi
  rm -f /tmp/ap132_hits
fi
```

**Fail message:** `AP132: Bar complex B(A)=T^c(s^{-1}\bar A) uses the augmentation ideal \bar A=ker(epsilon), NOT A.`

**Severity:** BLOCK

**Expected APs prevented:** AP132.

**False-positive risk:** LOW-MEDIUM. A chapter defining `T^c` abstractly with a generic `A` might legitimately write `T^c(s^{-1} A)`. Add `\bar` or parenthetical "(with A augmented)" to pass.

---

#### H4. Em dash U+2014

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Search for the actual U+2014 character.

```bash
# Em dash U+2014 -- CLAUDE.md prose law
if grep -l $'\xe2\x80\x94' "$FILE_PATH" >/dev/null 2>&1; then
  MATCHES=$(grep -n $'\xe2\x80\x94' "$FILE_PATH" | head -3)
  ISSUES="${ISSUES}PROSE: Em dash (U+2014) detected. Use colon, semicolon, or separate sentences. Lines: ${MATCHES}\n"
fi
```

**Fail message:** `PROSE: Em dash (U+2014) detected. Use colon, semicolon, or separate sentences.`

**Severity:** BLOCK

**Expected APs prevented:** AP121 extension (prose law 3).

**False-positive risk:** ZERO. The manuscript has zero legitimate em dashes by decree.

---

#### H5. AI attribution in .tex or staged commit message

**Trigger:** PostToolUse Edit|Write on `*.tex`, `*.md`, `.git/COMMIT_EDITMSG`

**Rule:** Regex for co-authored-by, Anthropic, Claude, ChatGPT, LLM, AI-assisted, Generated-by (case-insensitive).

```bash
# Git attribution hard rule: no AI attribution anywhere
if grep -Eni 'co-authored-by:.*claude\|co-authored-by:.*anthropic\|co-authored-by:.*chatgpt\|co-authored-by:.*gpt\|generated by claude\|generated by gpt\|ai-assisted\|llm-assisted\|claude-code <\|🤖 Generated with' "$FILE_PATH" 2>/dev/null > /tmp/aiattr_hits; then
  if [ -s /tmp/aiattr_hits ]; then
    HITS=$(head -3 /tmp/aiattr_hits)
    ISSUES="${ISSUES}AAP-GIT: AI attribution detected. All commits by Raeez Lorgat. NEVER credit an LLM. Hits: ${HITS}\n"
  fi
  rm -f /tmp/aiattr_hits
fi
```

**Fail message:** `AAP-GIT: AI attribution detected. All commits and prose by Raeez Lorgat. NEVER credit an LLM.`

**Severity:** BLOCK

**Expected APs prevented:** MEMORY.md git attribution rule, feedback_commit_protocol.

**False-positive risk:** ZERO. No legitimate use in this manuscript.

---

#### H6. `\newcommand` in chapter files

**Trigger:** PostToolUse Edit|Write on `chapters/**/*.tex`, `appendices/**/*.tex`

**Rule:** Detect `\newcommand` in any file under chapters/ or appendices/ (main.tex allowed).

```bash
# LaTeX preamble discipline: no \newcommand in chapters
case "$FILE_PATH" in
  */chapters/*|*/appendices/*)
    if grep -En '^\s*\\newcommand' "$FILE_PATH" 2>/dev/null > /tmp/newcmd_hits; then
      if [ -s /tmp/newcmd_hits ]; then
        HITS=$(head -3 /tmp/newcmd_hits)
        ISSUES="${ISSUES}LATEX: \\newcommand in chapter file. Use \\providecommand or move to main.tex preamble. Hits: ${HITS}\n"
      fi
      rm -f /tmp/newcmd_hits
    fi
    ;;
esac
```

**Fail message:** `LATEX: \newcommand in chapter file. Use \providecommand or move to main.tex preamble.`

**Severity:** BLOCK

**Expected APs prevented:** CLAUDE.md LaTeX section rule; prevents multiply-defined macro builds.

**False-positive risk:** LOW. `\providecommand` is the escape hatch.

---

#### H7. V2-AP32 -- Standalone artifact leak in chapters

**Trigger:** PostToolUse Edit|Write on `chapters/**/*.tex`

**Rule:** Detect `\title{}`, `\author{}`, `\date{}`, `\begin{abstract}`, `\tableofcontents`, `\maketitle` in any chapter file.

```bash
# V2-AP32: standalone doc artifacts inside \input'd chapter
case "$FILE_PATH" in
  */chapters/*)
    if grep -En '^\s*(\\title\{|\\author\{|\\date\{|\\begin\{abstract\}|\\tableofcontents|\\maketitle|\\documentclass)' "$FILE_PATH" 2>/dev/null > /tmp/v2ap32_hits; then
      if [ -s /tmp/v2ap32_hits ]; then
        HITS=$(head -3 /tmp/v2ap32_hits)
        ISSUES="${ISSUES}V2-AP32: Standalone-document artifact leak in \\input'd chapter. Remove \\title/\\author/\\date/\\begin{abstract}/\\tableofcontents/\\maketitle/\\documentclass. Hits: ${HITS}\n"
      fi
      rm -f /tmp/v2ap32_hits
    fi
    ;;
esac
```

**Fail message:** `V2-AP32: Standalone-document artifact leak. Chapter files \input'd into main.tex MUST NOT contain \title{}/\author{}/\date{}/\begin{abstract}/\tableofcontents/\maketitle.`

**Severity:** BLOCK

**Expected APs prevented:** V2-AP32, silent rendering artifacts, double-title.

**False-positive risk:** NONE for chapters. Standalone papers live under `standalone/` or `papers/`, not `chapters/`.

---

#### H8. V2-AP34 -- lambda-bracket c/2 lambda^3 (Vol II)

**Trigger:** PostToolUse Edit|Write on `*.tex` (Vol II worktrees)

**Rule:** Detect `c/2\s*\\lambda^?\{?3` in a Vol II file. Should be `c/12`.

```bash
# V2-AP34: divided-power lambda-bracket. c/2 lambda^3 is wrong; correct is c/12.
case "$FILE_PATH" in
  *chiral-bar-cobar-vol2*)
    if grep -En '(\\frac\{c\}\{2\}|c/2)\s*\\lambda\^?\{?3' "$FILE_PATH" 2>/dev/null > /tmp/v2ap34_hits; then
      if [ -s /tmp/v2ap34_hits ]; then
        HITS=$(head -3 /tmp/v2ap34_hits)
        ISSUES="${ISSUES}V2-AP34: Vol II lambda-bracket uses divided powers. {T_lambda T}|_{lambda^3} = c/12, NOT c/2. Hits: ${HITS}\n"
      fi
      rm -f /tmp/v2ap34_hits
    fi
    ;;
esac
```

**Fail message:** `V2-AP34: Vol II lambda-bracket uses divided powers. {T_lambda T}|_{\lambda^3} = c/12, NOT c/2. OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12.`

**Severity:** BLOCK

**Expected APs prevented:** V2-AP34.

**False-positive risk:** LOW. A Vol II file with raw c/2 lambda^3 is almost always wrong.

---

### 3.2 WARN (hygiene, probable violation)

---

#### H9. AP116 -- Summation boundary

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Flag `\sum_{j=1}^{N-1}` for manual verification.

```bash
# AP116: Summation boundary requires verification
if grep -En '\\sum_\{[a-z]=[0-9]+\}\^\{[A-Za-z]-1\}' "$FILE_PATH" 2>/dev/null > /tmp/ap116_hits; then
  if [ -s /tmp/ap116_hits ]; then
    HITS=$(head -3 /tmp/ap116_hits)
    WARNINGS="${WARNINGS}AP116: Summation with shifted upper limit N-1. Verify boundary at smallest index. H_N = sum_{j=1}^{N}, NOT sum_{j=1}^{N-1}. Hits: ${HITS}\n"
  fi
  rm -f /tmp/ap116_hits
fi
```

**Severity:** WARN

**Expected APs prevented:** AP116, AP136.

**False-positive risk:** MEDIUM. Many legitimate sums end at N-1; the warning is a prompt to re-check.

---

#### H10. AP136 -- H_{N-1} vs H_N - 1

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `H_{N-1}` or `H_{k-1}` where H is a harmonic number.

```bash
# AP136: Harmonic number shift confusion
if grep -En 'H_\{[A-Za-z]-1\}' "$FILE_PATH" 2>/dev/null > /tmp/ap136_hits; then
  if [ -s /tmp/ap136_hits ]; then
    HITS=$(head -3 /tmp/ap136_hits)
    WARNINGS="${WARNINGS}AP136: H_{N-1} detected. H_{N-1} != H_N - 1. At N=2: H_1=1 but H_2-1=1/2. Verify at smallest N. kappa(W_N)=c*(H_N - 1), NOT c*H_{N-1}. Hits: ${HITS}\n"
  fi
  rm -f /tmp/ap136_hits
fi
```

**Severity:** WARN

**Expected APs prevented:** AP136.

**False-positive risk:** LOW. Any occurrence of H_{N-1} should be double-checked.

---

#### H11. AP137 -- Bosonic/fermionic partner sanity

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** When `c_{\beta\gamma}` OR `c_{bc}` is detected, remind agent to verify `c_{\beta\gamma} + c_{bc} = 0` at lambda=1.

```bash
# AP137: bosonic/fermionic partner sanity check
if grep -qE 'c_\{\\beta\\gamma\}\|c_\{bc\}' "$FILE_PATH" 2>/dev/null; then
  MATCHES=$(grep -nE 'c_\{\\beta\\gamma\}\|c_\{bc\}' "$FILE_PATH" | head -3)
  WARNINGS="${WARNINGS}AP137: ghost central-charge partners detected. VERIFY c_{beta gamma} + c_{bc} = 0. At lambda=1: c_{beta gamma}=2, c_{bc}=-2. c_{beta gamma}(lambda)=2(6 lambda^2 - 6 lambda + 1), c_{bc}(lambda)=1-3(2 lambda - 1)^2. Lines: ${MATCHES}\n"
fi
```

**Severity:** WARN

**Expected APs prevented:** AP137.

**False-positive risk:** LOW. Fires on every ghost central-charge discussion; content is a sanity checklist rather than a block.

---

#### H12. AP130 -- Fiber vs base confusion for omega_g

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `\omega_g\s*=\s*d\\tau` or `omega_g\s*=\s*[^c\[]` where RHS is a holomorphic form symbol (`d\tau`, `dz`, `dw`, `dbar z`).

```bash
# AP130: fiber vs base level confusion
if grep -En '\\omega_g\s*=\s*(d\\tau|dz|d\\bar|dw)' "$FILE_PATH" 2>/dev/null > /tmp/ap130_hits; then
  if [ -s /tmp/ap130_hits ]; then
    HITS=$(head -3 /tmp/ap130_hits)
    WARNINGS="${WARNINGS}AP130: omega_g is the Hodge CLASS c_1(Lambda) on M-bar_{g,n}, NOT a form on the fiber. d\\tau lives on Sigma_g, not on moduli. Hits: ${HITS}\n"
  fi
  rm -f /tmp/ap130_hits
fi
```

**Severity:** WARN

**Expected APs prevented:** AP130.

**False-positive risk:** LOW. omega_g is specific enough.

---

#### H13. AP39 -- kappa = S_2 without Virasoro qualifier

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `\kappa\s*=\s*S_2` or `S_2\s*=\s*\kappa` and WARN if Virasoro is not mentioned within 10 lines.

```bash
# AP39: kappa = S_2 only for Virasoro (rank-1)
if grep -qEn '\\kappa\s*=\s*S_\{?2\|S_\{?2\s*=\s*\\kappa' "$FILE_PATH" 2>/dev/null; then
  LNS=$(grep -nE '\\kappa\s*=\s*S_\{?2\|S_\{?2\s*=\s*\\kappa' "$FILE_PATH" | cut -d: -f1)
  for LN in $LNS; do
    START=$((LN - 10)); [ $START -lt 1 ] && START=1
    END=$((LN + 10))
    if ! sed -n "${START},${END}p" "$FILE_PATH" | grep -qi 'virasoro\|Vir[^a-z]\|rank.?1\|rank.one'; then
      WARNINGS="${WARNINGS}AP39: kappa = S_2 identity holds ONLY for Virasoro (rank-1). KM: kappa=dim(g)(k+h^v)/(2h^v). Line ${LN} has no Virasoro qualifier nearby.\n"
    fi
  done
fi
```

**Severity:** WARN

**Expected APs prevented:** AP39.

**False-positive risk:** MEDIUM. Content within a Virasoro-only chapter will fire spuriously; the 10-line context window is a compromise.

---

#### H14. AP98 -- av(r(z)) = kappa without Sugawara shift

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `av(r(z))\s*=\s*\kappa` and warn about Sugawara shift.

```bash
# AP98: av(r(z)) = kappa only for abelian/Virasoro
if grep -qEn 'av\(r\(z\)\)\s*=\s*\\kappa\|av.*r\(z\).*=.*kappa' "$FILE_PATH" 2>/dev/null; then
  MATCHES=$(grep -nE 'av\(r\(z\)\)\s*=\s*\\kappa' "$FILE_PATH" | head -3)
  WARNINGS="${WARNINGS}AP98: av(r(z))=kappa needs Sugawara shift for non-abelian KM. For KM: av involves (k+h^v) denominator. Lines: ${MATCHES}\n"
fi
```

**Severity:** WARN

**Expected APs prevented:** AP98.

**False-positive risk:** LOW. The exact phrasing is rare.

---

#### H15. V2-AP33 -- Unresolved RECTIFICATION-FLAG

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `RECTIFICATION-FLAG` or `TODO: rectify` in a file being written.

```bash
# V2-AP33: RECTIFICATION-FLAG must not become permanent debt
if grep -qn 'RECTIFICATION-FLAG\|TODO:\s*rectify\|FIXME:\s*rectify' "$FILE_PATH" 2>/dev/null; then
  COUNT=$(grep -c 'RECTIFICATION-FLAG\|TODO:\s*rectify' "$FILE_PATH")
  WARNINGS="${WARNINGS}V2-AP33: ${COUNT} unresolved RECTIFICATION-FLAG(s) in file. Resolve before session end; zero tolerance for permanent debt.\n"
fi
```

**Severity:** WARN

**Expected APs prevented:** V2-AP33.

**False-positive risk:** NONE (by design -- the flag is authored).

---

#### H16. Stray `\end{...>` typo from tool-call leak residue

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** Detect `\end{[a-z]+>` (closing angle bracket instead of brace).

```bash
# Stray \end{env> residue from tool markup leak
if grep -qEn '\\end\{[a-z]+>' "$FILE_PATH" 2>/dev/null; then
  MATCHES=$(grep -nE '\\end\{[a-z]+>' "$FILE_PATH" | head -3)
  ISSUES="${ISSUES}LATEX: Stray \\end{...>} typo (should be \\end{...}). Likely tool-call leak residue. Lines: ${MATCHES}\n"
fi
```

**Severity:** BLOCK (promote from WARN; this breaks the build).

**Expected APs prevented:** AAP1 subcase, build-breaker.

**False-positive risk:** ZERO. No legitimate LaTeX uses `\end{...>`.

---

#### H17. Unresolved `\cite{}` and `\ref{}` in standalone files

**Trigger:** PostToolUse Edit|Write on `standalone/**/*.tex` or `papers/**/*.tex`

**Rule:** For standalone files, grep all `\cite{KEY}` keys, then check each KEY exists as `\bibitem{KEY}` in the same file. Similarly `\ref{LABEL}` vs `\label{LABEL}`.

```bash
# Unresolved \cite and \ref in standalones
case "$FILE_PATH" in
  *standalone*|*papers/*|*standalones/*)
    # \cite keys
    CITES=$(grep -oE '\\cite\{[^}]+\}' "$FILE_PATH" 2>/dev/null | sed 's/\\cite{//;s/}//' | tr ',' '\n' | sort -u)
    BIBS=$(grep -oE '\\bibitem\{[^}]+\}' "$FILE_PATH" 2>/dev/null | sed 's/\\bibitem{//;s/}//' | sort -u)
    for KEY in $CITES; do
      if ! echo "$BIBS" | grep -qx "$KEY"; then
        WARNINGS="${WARNINGS}CITE: \\cite{${KEY}} has no \\bibitem in standalone file. Will compile as '[?]'.\n"
      fi
    done | head -5
    # \ref labels
    REFS=$(grep -oE '\\ref\{[^}]+\}' "$FILE_PATH" 2>/dev/null | sed 's/\\ref{//;s/}//' | sort -u)
    LABELS=$(grep -oE '\\label\{[^}]+\}' "$FILE_PATH" 2>/dev/null | sed 's/\\label{//;s/}//' | sort -u)
    for LBL in $REFS; do
      if ! echo "$LABELS" | grep -qx "$LBL"; then
        WARNINGS="${WARNINGS}REF: \\ref{${LBL}} has no \\label in standalone file. Will compile as '??'.\n"
      fi
    done | head -5
    ;;
esac
```

**Severity:** WARN

**Expected APs prevented:** AP127 (cross-ref to migrated chapter), general hygiene.

**False-positive risk:** LOW for pure standalones. Some standalones still `\input` shared chapters; add a bypass if so.

---

#### H18. V2-AP35 -- Unresolved "therefore/hence" after correction

**Trigger:** PostToolUse Edit|Write on `*.tex`

**Rule:** If the edit changes a displayed equation (regex: `\\[.*\\]` or `\begin{equation}`), warn that all "therefore"/"hence"/"it follows" within 5 lines must be re-audited.

```bash
# V2-AP35: audit logical connectives after formula edit
NEW_CONTENT=$(echo "$INPUT" | jq -r '(.tool_input.new_string // .tool_input.content) // empty' 2>/dev/null)
if echo "$NEW_CONTENT" | grep -qE '\\begin\{equation\}\|\\begin\{align\}\|\\\['; then
  # Find connectives near the edited region
  CONN=$(grep -nE 'therefore\|hence\|it follows\|consequently' "$FILE_PATH" 2>/dev/null | head -3)
  if [ -n "$CONN" ]; then
    WARNINGS="${WARNINGS}V2-AP35: Displayed equation edited. AUDIT nearby 'therefore/hence/it follows' for stale inference. Connectives in file: ${CONN}\n"
  fi
fi
```

**Severity:** WARN

**Expected APs prevented:** V2-AP35.

**False-positive risk:** HIGH (fires often). Consider raising threshold or restricting to edits that change RHS numerics.

---

### 3.3 Proposals deferred (high false-positive or require numerical probe)

- **AP129 reciprocal transcription**: needs numerical probe (substitute c=1). Cannot be done in a hook without a sympy subprocess; defer to a Python-based PreToolUse tool. SKIP at hook layer.
- **AP135 partition number family**: requires OEIS lookup; out of scope for regex. SKIP.
- **AP139 unbound variable in theorem**: requires parsing the theorem statement and extracting bound variables. Defer.

## 4. PreToolUse Edit|Write new hook (two cases only)

Two patterns are severe enough to BLOCK the write before it lands, not after. Propose a new hook file:

`/Users/raeez/chiral-bar-cobar/.claude/hooks/pretooluse-edit-gate.sh`

```bash
#!/bin/bash
# PreToolUse gate: block writes that introduce tool-markup leak or AI attribution.
INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
NEW_CONTENT=$(echo "$INPUT" | jq -r '(.tool_input.new_string // .tool_input.content) // empty')

case "$FILE_PATH" in
  *.tex|*.md|*.py|*.sh|*.json) ;;
  *) exit 0 ;;
esac

# BLOCK 1: tool markup leak
if echo "$NEW_CONTENT" | grep -qE 'antml\|</invoke>\|<function_calls>\|<tool_call>'; then
  jq -n '{"decision":"block","reason":"AAP1: Tool markup (antml/invoke/function_calls/tool_call) in write content. Remove before writing."}'
  exit 0
fi

# BLOCK 2: AI attribution
if echo "$NEW_CONTENT" | grep -qEi 'co-authored-by:.*claude\|co-authored-by:.*anthropic\|🤖 Generated with\|Generated by Claude\|Generated by GPT\|Claude-Code <noreply'; then
  jq -n '{"decision":"block","reason":"AAP-GIT: AI attribution in write content. All commits by Raeez Lorgat. NEVER credit an LLM."}'
  exit 0
fi

# BLOCK 3: Markdown backtick numeral in .tex
if [[ "$FILE_PATH" == *.tex ]] && echo "$NEW_CONTENT" | grep -qE '`[0-9]'; then
  jq -n '{"decision":"block","reason":"AP121: Markdown backtick numeral in .tex write. Use $...$ instead."}'
  exit 0
fi

exit 0
```

Wire in `settings.json`:

```json
"PreToolUse": [
  {
    "matcher": "Bash",
    "if": "Bash(*git commit*)",
    "hooks": [ { "type": "command", "command": "echo '...'", "timeout": 5 } ]
  },
  {
    "matcher": "Edit|Write",
    "hooks": [
      { "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/pretooluse-edit-gate.sh", "timeout": 10 }
    ]
  }
]
```

## 5. Summary ranking by ROI

| # | Hook | Target APs | Severity | Historical hits | FP risk | ROI |
|---|------|-----------|----------|-----------------|---------|-----|
| 1 | H1 AP126 bare Omega/z | AP126, AP141 | BLOCK | 42+ | MED | HIGHEST |
| 2 | H5 AI attribution | AAP-GIT | BLOCK | unknown | ZERO | HIGH |
| 3 | H4 Em dash | AP121 | BLOCK | frequent | ZERO | HIGH |
| 4 | H2 AP125 label prefix | AP125 | BLOCK | ~10 | LOW | HIGH |
| 5 | H3 AP132 bar ideal | AP132 | BLOCK | 2-3 | LOW-MED | HIGH |
| 6 | H7 V2-AP32 standalone leak | V2-AP32 | BLOCK | ~5 | NONE | MED |
| 7 | H16 stray \end{...> typo | AAP1 | BLOCK | build-breaker | ZERO | MED |
| 8 | H6 \newcommand in chapter | LaTeX | BLOCK | recurring | LOW | MED |
| 9 | H8 V2-AP34 lambda^3 c/2 | V2-AP34 | BLOCK | 2-5 | LOW | MED |
| 10 | H10 AP136 H_{N-1} | AP136 | WARN | 2-4 | LOW | MED |
| 11 | H9 AP116 sum boundary | AP116 | WARN | ~10 | MED | MED |
| 12 | H12 AP130 omega_g = d tau | AP130 | WARN | 2-4 | LOW | LOW-MED |
| 13 | H13 AP39 kappa = S_2 | AP39 | WARN | recurring | MED | LOW-MED |
| 14 | H11 AP137 ghost partners | AP137 | WARN | 2-3 | LOW | LOW |
| 15 | H17 unresolved cite/ref | AP127 | WARN | occasional | LOW | LOW |
| 16 | H14 av(r(z))=kappa | AP98 | WARN | 1-2 | LOW | LOW |
| 17 | H15 RECTIFICATION-FLAG | V2-AP33 | WARN | as-authored | NONE | LOW |
| 18 | H18 therefore after edit | V2-AP35 | WARN | rare | HIGH | LOW |

## 6. Test vectors

Each regex should match the first, NOT the second:

| H | Should match | Should NOT match |
|---|-------------|------------------|
| H1 | `r(z) = \Omega/z` | `r(z) = k\Omega/z`, `\hbar\Omega/z`, `\Omega/(z_1 - z_2)` preceded by k |
| H2 | `\begin{conjecture}...\label{thm:foo}` within 5 lines | `\begin{theorem}...\label{thm:foo}` |
| H3 | `T^c(s^{-1} A)` | `T^c(s^{-1} \bar A)`, `T^c(s^{-1} A^+)` |
| H4 | `This — that` | `This, that`, `This -- that`, `This -- that` (double hyphen) |
| H5 | `Co-Authored-By: Claude` | `Authored-by: Raeez Lorgat` |
| H6 | `\newcommand{\foo}{...}` | `\providecommand{\foo}{...}` |
| H7 | `\title{Chapter 5}` in chapters/ | `\chapter{Chapter 5}` |
| H8 | `\frac{c}{2} \lambda^3` in Vol II | `\frac{c}{12} \lambda^3` |
| H9 | `\sum_{j=1}^{N-1}` | `\sum_{j=1}^{N}` |
| H10 | `H_{N-1}` | `H_N - 1`, `H_{N}` |
| H11 | `c_{\beta\gamma}` | `c_\beta`, `c_{bc\_ghost}` |
| H12 | `\omega_g = d\tau` | `\omega_g = c_1(\Lambda)` |
| H16 | `\end{equation>` | `\end{equation}` |

## 7. Implementation notes

- All regex assume GNU grep/awk (`grep -En`). macOS ships BSD grep; `grep -E` is portable. Verify on Darwin before deploying.
- The existing hook uses `grep` (BSD-compatible); keep that style. Avoid `grep -P` (Perl regex) since macOS BSD grep does not support it.
- Use `/tmp/<hookname>_hits` files to avoid shell-variable escaping issues with multi-line grep output.
- Keep the individual timeouts inside the 15-second beilinson-gate.sh budget. The proposed additions add roughly 1-2 seconds total if all fire.
- Propagate each hook identically across Vol I, Vol II, Vol III beilinson-gate.sh (AAP2 atomic propagation). Vol III adds the kappa subscript guard.
- Test vector harness: create `compute/tests/hook_regex_tests.sh` that feeds sample inputs through each regex and checks expected match/no-match. Track false-positive rate in compute/audit/hook_fpr_log.md.

## 8. Caveats

- **Hooks cannot substitute for multi-path verification.** AP129 (reciprocal), AP135 (partition numbers), AP139 (unbound variable) require semantic analysis beyond regex. These belong in a separate verification pass, not the hook layer.
- **Hook saturation is a real risk.** The current beilinson-gate already fires ~25 distinct checks. Adding 15 more puts the fire rate near "every edit has at least one warning." Triage ISSUES (BLOCK) strictly from WARNINGS (hygiene) so BLOCK signals stay rare and attention-worthy.
- **Regex test discipline.** Each new regex should come with a test vector line in `compute/tests/hook_regex_tests.sh`. Without that, a future change to the regex can silently un-catch the pattern it was written for (AP128 variant at the hook layer).

END OF PROPOSAL.
