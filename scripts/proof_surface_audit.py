#!/usr/bin/env python3
"""Cross-volume proof-surface audit.

This script is intentionally syntactic.  It does not certify a proof.
It finds places where a proof cannot be certified without further
mathematics: missing statuses, missing proof bodies, unstable
dependencies, unresolved references, duplicate labels, and forbidden
object-collapses.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path


ROOTS = {
    "Vol I": Path("/Users/raeez/chiral-bar-cobar"),
    "Vol II": Path("/Users/raeez/chiral-bar-cobar-vol2"),
    "Vol III": Path("/Users/raeez/calabi-yau-quantum-groups"),
}

OUT = ROOTS["Vol I"] / "notes" / "proof_audit_20260705"

CLAIM_ENVS = {
    "theorem",
    "maintheorem",
    "lemma",
    "proposition",
    "corollary",
    "conjecture",
    "computation",
    "calculation",
    "verification",
    "definition",
    "construction",
    "convention",
    "remark",
}

PROOF_REQUIRED_STATUSES = {"ProvedHere"}
PROOF_ENV_REQUIRED = {
    "theorem",
    "maintheorem",
    "lemma",
    "proposition",
    "corollary",
    "computation",
    "calculation",
    "verification",
}
NON_PROVED_STATUSES = {
    "Conjectured",
    "Conditional",
    "Heuristic",
    "Open",
    "Retracted",
    "NeedsVerification",
    "Evidence",
    "NumericalEvidence",
    "Unknown",
    "Unmarked",
}

STATUS_RE = re.compile(r"\\ClaimStatus([A-Za-z]+)")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|autoref|Cref|cref|eqref|nameref|hyperref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite(?:[a-zA-Z]*|\[[^\]]*\])*(?:\[[^\]]*\])?\{([^}]+)\}")
INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")
BEGIN_RE = re.compile(r"\\begin\{([A-Za-z*]+)\}")
BEGIN_OPT_RE = re.compile(r"\\begin\{([A-Za-z*]+)\}\s*\[([^\]]*)\]", re.S)

FORBIDDEN_PATTERNS = {
    "bar_equals_bulk": re.compile(r"Bar\s*\([^)]*\)\s*(?:=|\\simeq|is)\s*(?:the\s*)?bulk", re.I),
    "A_primitive": re.compile(r"\bA\b\s+is\s+(?:the\s+)?primitive", re.I),
    "closed_algebra_modular": re.compile(r"closed\s+algebra\s+is\s+modular", re.I),
    "direct_phi": re.compile(r"\\Phi(?:_\{?d\}?|d)?\s*:\s*.*CY.*ChirAlg", re.I | re.S),
    "kappa_bkm_additive": re.compile(r"kappa_\{\\mathrm\{BKM\}\}\s*=\s*kappa_\{\\mathrm\{ch\}\}\s*\+\s*\\chi", re.I),
    "coha_equals_w": re.compile(r"CoHA.*(?:=|\\simeq).*W_\{?1\\?\\?\+?\\infty", re.I),
    "delta5_hilbert": re.compile(r"Delta_?5.*(?:constructs|is).*Hilbert", re.I),
    "path_integral_shadow": re.compile(r"Z_\{?\\mathrm\{BPS\}\}?.*(?:is|=).*path\s+integral", re.I),
    "unconditional_winfty": re.compile(r"W_\\infty.*E_\\infty(?![^.\n]{0,120}(conditional|hyp|Prochazka|CKL|PRS|Yamada))", re.I),
}


@dataclass
class Claim:
    volume: str
    root: str
    file: str
    line: int
    env: str
    label: str
    status: str
    title: str
    active: bool
    has_proof: bool
    proof_line: int | None
    refs: list[str] = field(default_factory=list)
    cites: list[str] = field(default_factory=list)
    labels_in_block: list[str] = field(default_factory=list)
    forbidden_hits: list[str] = field(default_factory=list)


@dataclass
class Finding:
    severity: str
    code: str
    volume: str
    file: str
    line: int
    label: str
    detail: str


def strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        buf = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            buf.append(line[i])
            i += 1
        out.append("".join(buf))
    return "\n".join(out)


def normalize_tex_path(root: Path, rel: str) -> Path:
    if not rel.endswith(".tex"):
        rel += ".tex"
    return root / rel


def active_files(root: Path) -> set[Path]:
    main = root / "main.tex"
    if not main.exists():
        return set()

    files: set[Path] = set()
    todo = [main.resolve()]
    while todo:
        current = todo.pop()
        if current in files or not current.exists():
            continue
        files.add(current)
        text = strip_comments(current.read_text(encoding="utf-8", errors="ignore"))
        for match in INCLUDE_RE.finditer(text):
            raw = match.group(1).strip()
            if raw.startswith("bibliography/"):
                continue
            path = normalize_tex_path(root, raw).resolve()
            if path.exists() and path not in files:
                todo.append(path)
    return files


def all_tex_files(root: Path) -> list[Path]:
    dirs = ["chapters", "appendices", "standalone", "frame", "bibliography"]
    files: set[Path] = set()
    for d in dirs:
        path = root / d
        if path.exists():
            files.update(p.resolve() for p in path.rglob("*.tex"))
    main = root / "main.tex"
    if main.exists():
        files.add(main.resolve())
    return sorted(files)


def find_env_end(lines: list[str], start: int, env: str) -> int:
    begin = f"\\begin{{{env}}}"
    end = f"\\end{{{env}}}"
    depth = 1
    for idx in range(start + 1, len(lines)):
        if begin in lines[idx]:
            depth += 1
        if end in lines[idx]:
            depth -= 1
            if depth == 0:
                return idx
    return len(lines) - 1


def next_proof(lines: list[str], after: int, label: str) -> tuple[bool, int | None]:
    """Find a proof body following a claim.

    The manuscripts often place a short remark or a subsection title
    between a statement and its proof.  Count a proof if it appears
    before the next theorem-like statement, or if its optional title
    explicitly names the label.
    """
    for j in range(after + 1, min(len(lines), after + 90)):
        stripped = lines[j].strip()
        if not stripped:
            continue
        if stripped.startswith(r"\begin{proof}"):
            return True, j + 1
        if label and f"\\ref{{{label}}}" in stripped and r"\begin{proof}" in stripped:
            return True, j + 1
        m = BEGIN_RE.search(stripped)
        if m and m.group(1) in CLAIM_ENVS and m.group(1) not in {"remark", "definition", "convention"}:
            return False, None
    return False, None


def refs_from(text: str) -> list[str]:
    refs: list[str] = []
    for match in REF_RE.finditer(text):
        for raw in match.group(1).split(","):
            key = raw.strip()
            if key:
                refs.append(key)
    return list(dict.fromkeys(refs))


def cites_from(text: str) -> list[str]:
    cites: list[str] = []
    for match in CITE_RE.finditer(text):
        for raw in match.group(1).split(","):
            key = raw.strip()
            if key:
                cites.append(key)
    return list(dict.fromkeys(cites))


def scan_claims(volume: str, root: Path, active: set[Path]) -> list[Claim]:
    claims: list[Claim] = []
    for path in all_tex_files(root):
        text = strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
        lines = text.splitlines()
        i = 0
        while i < len(lines):
            m = BEGIN_RE.search(lines[i])
            if not m or m.group(1) not in CLAIM_ENVS:
                i += 1
                continue
            env = m.group(1)
            end = find_env_end(lines, i, env)
            block = "\n".join(lines[i : end + 1])
            labels = LABEL_RE.findall(block)
            statuses = STATUS_RE.findall(block)
            if statuses:
                status = statuses[0]
            elif env == "conjecture":
                status = "Conjectured"
            else:
                status = "Unmarked"
            label = labels[0] if labels else f"__unlabeled_{path.relative_to(root).as_posix()}:{i + 1}"
            opt = BEGIN_OPT_RE.search(block[:600])
            title = ""
            if opt:
                title = STATUS_RE.sub("", opt.group(2)).strip("; \t\n")
            has_proof, proof_line = next_proof(lines, end, label)
            forbidden_hits = [name for name, pattern in FORBIDDEN_PATTERNS.items() if pattern.search(block)]
            claims.append(
                Claim(
                    volume=volume,
                    root=str(root),
                    file=path.relative_to(root).as_posix(),
                    line=i + 1,
                    env=env,
                    label=label,
                    status=status,
                    title=title,
                    active=path.resolve() in active,
                    has_proof=has_proof,
                    proof_line=proof_line,
                    refs=refs_from(block),
                    cites=cites_from(block),
                    labels_in_block=labels,
                    forbidden_hits=forbidden_hits,
                )
            )
            i = end + 1
    return claims


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_claims: list[Claim] = []
    for volume, root in ROOTS.items():
        act = active_files(root)
        all_claims.extend(scan_claims(volume, root, act))

    label_to_claims: dict[str, list[Claim]] = defaultdict(list)
    for claim in all_claims:
        for label in claim.labels_in_block or [claim.label]:
            if not label.startswith("__unlabeled_"):
                label_to_claims[label].append(claim)

    label_status: dict[str, set[str]] = defaultdict(set)
    for label, claims in label_to_claims.items():
        for claim in claims:
            label_status[label].add(claim.status)

    findings: list[Finding] = []
    for claim in all_claims:
        if claim.active and claim.status == "Unmarked" and claim.env in CLAIM_ENVS:
            if claim.env in PROOF_ENV_REQUIRED or claim.env in {"conjecture", "maintheorem"}:
                findings.append(Finding("CRITICAL", "UNMARKED_ACTIVE_PROOF_CLAIM", claim.volume, claim.file, claim.line, claim.label, "active proof-bearing environment has no ClaimStatus macro"))
            else:
                findings.append(Finding("MODERATE", "UNMARKED_ACTIVE_EXPOSITORY_CLAIM", claim.volume, claim.file, claim.line, claim.label, "active theorem-like expository environment has no ClaimStatus macro"))
        if (
            claim.active
            and claim.status in PROOF_REQUIRED_STATUSES
            and claim.env in PROOF_ENV_REQUIRED
            and not claim.has_proof
        ):
            findings.append(Finding("CRITICAL", "PROVED_WITHOUT_PROOF_ENV", claim.volume, claim.file, claim.line, claim.label, "ClaimStatusProvedHere has no adjacent proof environment"))
        if claim.active and claim.status == "ProvedHere":
            bad_refs = []
            missing_refs = []
            for ref in claim.refs:
                ref_claims = label_to_claims.get(ref)
                if not ref_claims:
                    missing_refs.append(ref)
                    continue
                statuses = {c.status for c in ref_claims}
                if statuses & NON_PROVED_STATUSES:
                    bad_refs.append(f"{ref}:{'/'.join(sorted(statuses))}")
            if bad_refs:
                findings.append(Finding("SERIOUS", "PROVED_DEPENDS_ON_NON_PROVED", claim.volume, claim.file, claim.line, claim.label, "; ".join(bad_refs[:20])))
            if missing_refs:
                findings.append(Finding("MODERATE", "PROVED_HAS_UNRESOLVED_REF", claim.volume, claim.file, claim.line, claim.label, "; ".join(missing_refs[:20])))
        if claim.active and claim.forbidden_hits:
            findings.append(Finding("SERIOUS", "FORBIDDEN_COLLAPSE_PATTERN", claim.volume, claim.file, claim.line, claim.label, "; ".join(claim.forbidden_hits)))

    for label, statuses in label_status.items():
        claims = label_to_claims[label]
        active_claims = [c for c in claims if c.active]
        active_statuses = {c.status for c in active_claims}
        if len(active_statuses) > 1:
            detail = "; ".join(f"{c.volume}:{c.file}:{c.line}:{c.status}" for c in active_claims[:8])
            worst = "SERIOUS" if "ProvedHere" in active_statuses and (active_statuses & NON_PROVED_STATUSES) else "MODERATE"
            first = active_claims[0]
            findings.append(Finding(worst, "ACTIVE_LABEL_STATUS_CONFLICT", first.volume, first.file, first.line, label, detail))
        elif len(statuses) > 1:
            detail = "; ".join(f"{c.volume}:{c.file}:{c.line}:{c.status}:{'active' if c.active else 'inactive'}" for c in claims[:8])
            first = claims[0]
            findings.append(Finding("MINOR", "ARCHIVAL_LABEL_STATUS_CONFLICT", first.volume, first.file, first.line, label, detail))

    rows = [asdict(c) for c in all_claims]
    for row in rows:
        for key in ("refs", "cites", "labels_in_block", "forbidden_hits"):
            row[key] = ";".join(row[key])
    write_csv(
        OUT / "claims.csv",
        rows,
        [
            "volume",
            "file",
            "line",
            "env",
            "label",
            "status",
            "active",
            "has_proof",
            "proof_line",
            "title",
            "refs",
            "cites",
            "labels_in_block",
            "forbidden_hits",
        ],
    )

    frows = [asdict(f) for f in findings]
    severity_rank = {"CRITICAL": 0, "SERIOUS": 1, "MODERATE": 2, "MINOR": 3}
    frows.sort(key=lambda r: (severity_rank.get(r["severity"], 9), r["code"], r["volume"], r["file"], r["line"]))
    write_csv(
        OUT / "findings.csv",
        frows,
        ["severity", "code", "volume", "file", "line", "label", "detail"],
    )

    summary = {
        "date": str(date.today()),
        "roots": {k: str(v) for k, v in ROOTS.items()},
        "claim_count": len(all_claims),
        "active_claim_count": sum(1 for c in all_claims if c.active),
        "by_volume": {},
        "findings_by_severity": Counter(f.severity for f in findings),
        "findings_by_code": Counter(f.code for f in findings),
    }
    for volume in ROOTS:
        cs = [c for c in all_claims if c.volume == volume]
        active_cs = [c for c in cs if c.active]
        summary["by_volume"][volume] = {
            "claims": len(cs),
            "active_claims": len(active_cs),
            "statuses": Counter(c.status for c in active_cs),
            "envs": Counter(c.env for c in active_cs),
        }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2, default=dict), encoding="utf-8")

    lines = [
        "# End-to-End Proof Surface Audit",
        "",
        f"Generated: {date.today()}",
        "",
        "This is a syntactic proof-surface audit. It does not certify a theorem; it identifies claims that cannot be certified without further mathematical audit.",
        "",
        "## Summary",
        "",
        f"- Total theorem-like environments scanned: {len(all_claims)}",
        f"- Active theorem-like environments scanned: {summary['active_claim_count']}",
        "",
        "## Findings By Severity",
        "",
    ]
    for sev, count in summary["findings_by_severity"].most_common():
        lines.append(f"- {sev}: {count}")
    lines.extend(["", "## Findings By Code", ""])
    for code, count in summary["findings_by_code"].most_common():
        lines.append(f"- {code}: {count}")
    lines.extend(["", "## Volume Status Counts", ""])
    for volume, data in summary["by_volume"].items():
        lines.append(f"### {volume}")
        for status, count in data["statuses"].most_common():
            lines.append(f"- {status}: {count}")
        lines.append("")
    lines.extend(["## First 100 Findings", ""])
    for f in frows[:100]:
        lines.append(f"- {f['severity']} {f['code']} {f['volume']} `{f['file']}:{f['line']}` `{f['label']}` -- {f['detail']}")
    (OUT / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2, default=dict))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
