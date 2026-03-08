#!/usr/bin/env python3
"""Corpus-level quality-control checks for the monograph sources."""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_ROOTS = ("main.tex", "chapters", "appendices", "bibliography")
CONTROL_DOCS = (
    "notes/GPT54_CODEX_OPERATING_SYSTEM.md",
    "notes/VISION.md",
    "notes/PROGRAMMES.md",
    "notes/NEW_MACHINERY.md",
    "notes/REWRITE_QUEUE.md",
    "metadata/frontier_and_gaps.md",
    "CLAUDE.md",
)
FRONTIER_PHRASE_DOCS = (
    "notes/GPT54_CODEX_OPERATING_SYSTEM.md",
    "notes/VISION.md",
    "notes/PROGRAMMES.md",
    "notes/NEW_MACHINERY.md",
    "metadata/frontier_and_gaps.md",
    "CLAUDE.md",
)
THEOREM_ENVS = ("theorem", "lemma", "proposition", "corollary")
STATUS_RE = re.compile(
    r"\\ClaimStatus(?:ProvedHere|ProvedElsewhere|Open|Conjectured|Heuristic)"
)
GOQ_RE = re.compile(r"governing question", re.IGNORECASE)
HMS_RE = re.compile(r"semantic levels; convention|conv:hms-levels", re.IGNORECASE)
PRIOR_VERSION_PATTERNS = (
    re.compile(r"previous version", re.IGNORECASE),
    re.compile(r"previous draft", re.IGNORECASE),
    re.compile(r"earlier draft", re.IGNORECASE),
    re.compile(r"legacy", re.IGNORECASE),
    re.compile(r"supersede[s]? earlier preview", re.IGNORECASE),
)
AI_TELL_PATTERNS = (
    re.compile(r"it is worth noting", re.IGNORECASE),
    re.compile(r"it is important to note", re.IGNORECASE),
    re.compile(r"this chapter is organized as follows", re.IGNORECASE),
    re.compile(r"in this chapter[, ]+we", re.IGNORECASE),
    re.compile(r"we now turn to", re.IGNORECASE),
    re.compile(r"needless to say", re.IGNORECASE),
)
AMBIGUOUS_STATUS_PATTERNS = (
    re.compile(r"\bis expected\b", re.IGNORECASE),
    re.compile(r"\bare expected\b", re.IGNORECASE),
    re.compile(r"\bsuggests?\b", re.IGNORECASE),
    re.compile(r"\bby analogy\b", re.IGNORECASE),
    re.compile(r"\bin precise analogy\b", re.IGNORECASE),
)
VIRASORO_DUAL_PATTERNS = (
    re.compile(r"Virasoro[^.\n]{0,140}\bhas a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\badmits? a Koszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\brequires completion[^.\n]{0,80}\bKoszul dual\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bKoszul dual is\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual algebra\b", re.IGNORECASE),
    re.compile(r"Virasoro[^.\n]{0,140}\bdual object\b", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_\\infty", re.IGNORECASE),
    re.compile(r"Virasoro[^\n]{0,160}W_infty", re.IGNORECASE),
)
VIRASORO_SAFE_PATTERNS = (
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
)
INFINITE_GENERATOR_DUAL_PATTERNS = (
    re.compile(r"W_\\infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,140}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"W_\\infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"W_infty[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"Yangian tower[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bis (?:the )?Koszul dual\b", re.IGNORECASE),
    re.compile(r"dg-shifted Yangian[^.\n]{0,160}\bdual object\b", re.IGNORECASE),
)
INFINITE_GENERATOR_SAFE_PATTERNS = (
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
)
DK_SCOPE_PATTERNS = (
    re.compile(r"The derived Drinfeld--Kohno theorem", re.IGNORECASE),
    re.compile(r"Towards a derived Drinfeld--Kohno theorem", re.IGNORECASE),
    re.compile(r"\[Derived Drinfeld--Kohno", re.IGNORECASE),
    re.compile(r"Derived Drinfeld--Kohno is proved", re.IGNORECASE),
)
DK_SCOPE_SAFE_PATTERNS = (
    re.compile(r"chain-level", re.IGNORECASE),
    re.compile(r"evaluation locus", re.IGNORECASE),
    re.compile(r"evaluation-locus", re.IGNORECASE),
    re.compile(r"full derived Drinfeld--Kohno", re.IGNORECASE),
    re.compile(r"full factorization", re.IGNORECASE),
    re.compile(r"conjectur", re.IGNORECASE),
)
PERIODICITY_PROFILE_PATTERNS = (
    re.compile(r"periodicity triple", re.IGNORECASE),
)
KL_SCOPE_PATTERNS = (
    re.compile(r"Kazhdan--Lusztig equivalence from bar-cobar", re.IGNORECASE),
    re.compile(r"full Kazhdan--Lusztig equivalence", re.IGNORECASE),
    re.compile(r"Rep\^\{\\mathrm\{fd\}\}\(U_q", re.IGNORECASE),
    re.compile(r"equivalence of abelian categories", re.IGNORECASE),
)
KL_SCOPE_SAFE_PATTERNS = (
    re.compile(r"semisimplified tilting quotient", re.IGNORECASE),
    re.compile(r"\\mathcal\{C\}\(U_q", re.IGNORECASE),
    re.compile(r"non-semisimple", re.IGNORECASE),
    re.compile(r"before semisimplification", re.IGNORECASE),
    re.compile(r"abelian lift", re.IGNORECASE),
    re.compile(r"BGG reciprocity", re.IGNORECASE),
    re.compile(r"chain-level adjunction", re.IGNORECASE),
    re.compile(r"recovery problem", re.IGNORECASE),
    re.compile(r"programme", re.IGNORECASE),
    re.compile(r"conjectur", re.IGNORECASE),
    re.compile(r"small quantum group", re.IGNORECASE),
)
PERIODICITY_OVERCLAIM_PATTERNS = (
    re.compile(r"proved for minimal models and WZW", re.IGNORECASE),
    re.compile(r"Proved for min\.\ models/WZW", re.IGNORECASE),
    re.compile(r"proved minimal model and WZW cases", re.IGNORECASE),
    re.compile(r"all three periodicity sources are controlled", re.IGNORECASE),
)
PACKAGE_SCOPE_PATTERNS = (
    re.compile(r"full scalar modular characteristic package", re.IGNORECASE),
    re.compile(r"modular characteristic package is trivial", re.IGNORECASE),
    re.compile(r"preserves the modular characteristic package", re.IGNORECASE),
    re.compile(r"consequences of the modular characteristic package", re.IGNORECASE),
    re.compile(r"\(\\Theta_\{\\cA\}, H_\{\\cA\}, \\Delta_\{\\cA\}\)"),
    re.compile(r"`\(\\Theta_A,\s*H_A,\s*\\Delta_A\)`"),
    re.compile(r"universal `Theta_A` package", re.IGNORECASE),
    re.compile(r"N-complex periodicity of Theta_A", re.IGNORECASE),
    re.compile(r"modular package is functorial", re.IGNORECASE),
    re.compile(r"characteristic package \$\(\\Delta_\{\\cA\}, \\Pi_\{\\cA\}, \\Theta_\{\\cA\}\)\$"),
    re.compile(r"characteristic package \$\(\\kappa\(\\cA\), \\Delta_\{\\cA\}\)\$"),
)
MC2_FRONTIER_PATTERNS = (
    re.compile(r"MC2 is the foundational next target", re.IGNORECASE),
    re.compile(r"Foundational next target[^.\n]{0,160}MC2", re.IGNORECASE),
    re.compile(r"immediate foundational target is now MC2", re.IGNORECASE),
    re.compile(r"Advance MC2 first", re.IGNORECASE),
    re.compile(r"build MC2 infrastructure for the cyclic deformation algebra", re.IGNORECASE),
    re.compile(r"MC2 \(cyclic deformation / universal `Theta_A`\) first", re.IGNORECASE),
)
MC2_FRONTIER_SAFE_PATTERNS = (
    re.compile(r"reduction principle", re.IGNORECASE),
    re.compile(r"three exact packages", re.IGNORECASE),
    re.compile(r"three-package frontier", re.IGNORECASE),
    re.compile(r"intrinsic cyclic", re.IGNORECASE),
    re.compile(r"completed tensor", re.IGNORECASE),
    re.compile(r"clutching", re.IGNORECASE),
    re.compile(r"one-channel", re.IGNORECASE),
    re.compile(r"genus-by-genus normalization", re.IGNORECASE),
)
FRONTIER_STALE_PHRASE_PATTERNS = (
    re.compile(r"four remaining master conjectures", re.IGNORECASE),
    re.compile(r"remaining master conjectures", re.IGNORECASE),
    re.compile(r"completed infinite-generator bar theory", re.IGNORECASE),
)


@dataclass(frozen=True)
class Finding:
    path: pathlib.Path
    line: int
    detail: str


@dataclass(frozen=True)
class Paragraph:
    path: pathlib.Path
    line: int
    text: str
    normalized: str


def iter_tex_files() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for entry in SCAN_ROOTS:
        path = ROOT / entry
        if path.is_file():
            files.append(path)
            continue
        files.extend(sorted(path.rglob("*.tex")))
    return [
        path
        for path in sorted(files)
        if "archive/legacy" not in str(path) and "_legacy_" not in path.name
    ]


def iter_drift_files() -> list[pathlib.Path]:
    files = iter_tex_files()
    for entry in CONTROL_DOCS:
        path = ROOT / entry
        if path.exists():
            files.append(path)
    return sorted(dict.fromkeys(files))


def active_include_graph() -> set[pathlib.Path]:
    main_path = ROOT / "main.tex"
    lines = clean_lines(main_path)
    text = "\n".join(lines)
    active = {pathlib.Path("main.tex")}
    for match in re.finditer(r"\\(?:include|input)\{([^}]+)\}", text):
        include = pathlib.Path(match.group(1))
        if include.suffix != ".tex":
            include = include.with_suffix(".tex")
        active.add(include)
    return active


def strip_comments(line: str) -> str:
    escaped = False
    chars: list[str] = []
    for ch in line:
        if ch == "%" and not escaped:
            break
        chars.append(ch)
        escaped = ch == "\\"
        if ch != "\\":
            escaped = False
    return "".join(chars)


def clean_lines(path: pathlib.Path) -> list[str]:
    return [strip_comments(line.rstrip("\n")) for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()]


def paragraph_iter(path: pathlib.Path, lines: list[str]) -> list[Paragraph]:
    paragraphs: list[Paragraph] = []
    start = 0
    while start < len(lines):
        while start < len(lines) and not lines[start].strip():
            start += 1
        if start >= len(lines):
            break
        end = start
        block: list[str] = []
        while end < len(lines) and lines[end].strip():
            block.append(lines[end].strip())
            end += 1
        text = " ".join(block)
        if len(text) >= 180 and not text.startswith("\\begin") and not text.startswith("\\end"):
            normalized = normalize_paragraph(text)
            paragraphs.append(Paragraph(path=path, line=start + 1, text=text, normalized=normalized))
        start = end
    return paragraphs


def normalize_paragraph(text: str) -> str:
    norm = re.sub(r"\\label\{[^}]+\}", "", text)
    norm = re.sub(r"\\index\{[^}]+\}", "", norm)
    norm = re.sub(r"\\cite\{[^}]+\}", "CITE", norm)
    norm = re.sub(r"\\(?:eq)?ref\{[^}]+\}", "REF", norm)
    norm = re.sub(r"\s+", " ", norm).strip()
    return norm


def is_chapter_like(path: pathlib.Path) -> bool:
    return path.parts[0] in {"chapters", "appendices"}


def scan() -> dict[str, object]:
    files = iter_tex_files()
    drift_files = iter_drift_files()
    active_files = active_include_graph()
    frontier_phrase_docs = {pathlib.Path(entry) for entry in FRONTIER_PHRASE_DOCS}
    total_lines = 0
    missing_goq: list[pathlib.Path] = []
    missing_hms: list[pathlib.Path] = []
    untagged: list[Finding] = []
    prior_version: list[Finding] = []
    ai_tells: list[Finding] = []
    ambiguous_status: list[Finding] = []
    virasoro_shadow_drift: list[Finding] = []
    infinite_generator_drift: list[Finding] = []
    dk_scope_drift: list[Finding] = []
    periodicity_profile_drift: list[Finding] = []
    kl_scope_drift: list[Finding] = []
    periodicity_overclaim_drift: list[Finding] = []
    package_scope_drift: list[Finding] = []
    mc2_frontier_drift: list[Finding] = []
    frontier_stale_phrase_drift: list[Finding] = []
    long_paragraphs: list[Paragraph] = []
    duplicate_map: dict[str, list[Paragraph]] = collections.defaultdict(list)

    head_re = re.compile(r"\\begin\{(" + "|".join(THEOREM_ENVS) + r")\}")

    for path in files:
        rel = path.relative_to(ROOT)
        lines = clean_lines(path)
        total_lines += len(lines)
        text = "\n".join(lines)

        is_active = rel in active_files

        if is_active and is_chapter_like(rel):
            if not GOQ_RE.search(text):
                missing_goq.append(rel)
            if not HMS_RE.search(text):
                missing_hms.append(rel)

        for idx, line in enumerate(lines, start=1):
            if is_active:
                for pattern in PRIOR_VERSION_PATTERNS:
                    if pattern.search(line):
                        prior_version.append(Finding(rel, idx, line.strip()))
                        break
                if is_chapter_like(rel):
                    lower = line.lower()
                    # Allow explicit conjectural/open framing.
                    if (
                        "conjectur" not in lower
                        and "\\claimstatusconjectured" not in lower
                        and "\\claimstatusheuristic" not in lower
                    ):
                        for pattern in AMBIGUOUS_STATUS_PATTERNS:
                            if pattern.search(line):
                                ambiguous_status.append(Finding(rel, idx, line.strip()))
                                break
            for pattern in AI_TELL_PATTERNS:
                if pattern.search(line):
                    ai_tells.append(Finding(rel, idx, line.strip()))
                    break
            if is_active and head_re.search(line):
                window = "\n".join(lines[idx - 1 : idx + 7])
                if not STATUS_RE.search(window):
                    untagged.append(Finding(rel, idx, line.strip()))

        if is_active:
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in VIRASORO_DUAL_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in VIRASORO_SAFE_PATTERNS):
                    virasoro_shadow_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in INFINITE_GENERATOR_DUAL_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in INFINITE_GENERATOR_SAFE_PATTERNS):
                    infinite_generator_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in DK_SCOPE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in DK_SCOPE_SAFE_PATTERNS):
                    dk_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PERIODICITY_PROFILE_PATTERNS):
                    continue
                periodicity_profile_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in KL_SCOPE_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                lower_window = window.lower()
                if "kazhdan--lusztig" not in lower_window and "u_q" not in lower_window:
                    continue
                if not any(pattern.search(window) for pattern in KL_SCOPE_SAFE_PATTERNS):
                    kl_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PERIODICITY_OVERCLAIM_PATTERNS):
                    continue
                periodicity_overclaim_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in PACKAGE_SCOPE_PATTERNS):
                    continue
                package_scope_drift.append(Finding(rel, idx, line.strip()))
            for idx, line in enumerate(lines, start=1):
                if not any(pattern.search(line) for pattern in MC2_FRONTIER_PATTERNS):
                    continue
                window = "\n".join(lines[max(0, idx - 3) : min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_FRONTIER_SAFE_PATTERNS):
                    mc2_frontier_drift.append(Finding(rel, idx, line.strip()))
            if rel in frontier_phrase_docs:
                for idx, line in enumerate(lines, start=1):
                    if any(pattern.search(line) for pattern in FRONTIER_STALE_PHRASE_PATTERNS):
                        frontier_stale_phrase_drift.append(Finding(rel, idx, line.strip()))

        for para in paragraph_iter(rel, lines):
            if len(para.text) > 1200:
                long_paragraphs.append(para)
            duplicate_map[para.normalized].append(para)

    for path in drift_files:
        rel = path.relative_to(ROOT)
        if rel in active_files:
            continue
        lines = clean_lines(path)
        for idx, line in enumerate(lines, start=1):
            if any(pattern.search(line) for pattern in DK_SCOPE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in DK_SCOPE_SAFE_PATTERNS):
                    dk_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PERIODICITY_PROFILE_PATTERNS):
                periodicity_profile_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in KL_SCOPE_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                lower_window = window.lower()
                if "kazhdan--lusztig" not in lower_window and "u_q" not in lower_window:
                    continue
                if not any(pattern.search(window) for pattern in KL_SCOPE_SAFE_PATTERNS):
                    kl_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PERIODICITY_OVERCLAIM_PATTERNS):
                periodicity_overclaim_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in PACKAGE_SCOPE_PATTERNS):
                package_scope_drift.append(Finding(rel, idx, line.strip()))
            if any(pattern.search(line) for pattern in MC2_FRONTIER_PATTERNS):
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 3)])
                if not any(pattern.search(window) for pattern in MC2_FRONTIER_SAFE_PATTERNS):
                    mc2_frontier_drift.append(Finding(rel, idx, line.strip()))
            if rel in frontier_phrase_docs and any(
                pattern.search(line) for pattern in FRONTIER_STALE_PHRASE_PATTERNS
            ):
                frontier_stale_phrase_drift.append(Finding(rel, idx, line.strip()))

    duplicates = []
    for norm, paras in duplicate_map.items():
        unique_paths = {para.path for para in paras}
        if len(paras) > 1 and len(unique_paths) > 1:
            duplicates.append((norm, paras))
    duplicates.sort(key=lambda item: (-len(item[1]), item[1][0].path.as_posix(), item[1][0].line))
    long_paragraphs.sort(key=lambda para: (-len(para.text), para.path.as_posix(), para.line))

    return {
        "files": files,
        "active_files": active_files,
        "total_lines": total_lines,
        "missing_goq": missing_goq,
        "missing_hms": missing_hms,
        "untagged": untagged,
        "prior_version": prior_version,
        "ai_tells": ai_tells,
        "ambiguous_status": ambiguous_status,
        "virasoro_shadow_drift": virasoro_shadow_drift,
        "infinite_generator_drift": infinite_generator_drift,
        "dk_scope_drift": dk_scope_drift,
        "periodicity_profile_drift": periodicity_profile_drift,
        "kl_scope_drift": kl_scope_drift,
        "periodicity_overclaim_drift": periodicity_overclaim_drift,
        "package_scope_drift": package_scope_drift,
        "mc2_frontier_drift": mc2_frontier_drift,
        "frontier_stale_phrase_drift": frontier_stale_phrase_drift,
        "long_paragraphs": long_paragraphs,
        "duplicates": duplicates,
    }


def print_section(title: str) -> None:
    print(f"## {title}")


def print_findings(findings: list[Finding], limit: int) -> None:
    for finding in findings[:limit]:
        print(f"- `{finding.path}:{finding.line}` {finding.detail}")
    if len(findings) > limit:
        print(f"- ... {len(findings) - limit} more")


def print_paragraphs(paragraphs: list[Paragraph], limit: int) -> None:
    for para in paragraphs[:limit]:
        snippet = para.text[:180].strip()
        print(f"- `{para.path}:{para.line}` {len(para.text)} chars: {snippet}")
    if len(paragraphs) > limit:
        print(f"- ... {len(paragraphs) - limit} more")


def report(data: dict[str, object], limit: int) -> None:
    files = data["files"]
    print("# Manuscript QC Report")
    print()
    print(f"- Files scanned: `{len(files)}`")
    print(f"- Active files: `{len(data['active_files'])}`")
    print(f"- Lines scanned: `{data['total_lines']}`")
    print(f"- Missing governing-question markers: `{len(data['missing_goq'])}`")
    print(f"- Missing H/M/S markers: `{len(data['missing_hms'])}`")
    print(f"- Untagged theorem heads: `{len(data['untagged'])}`")
    print(f"- Prior-version leaks: `{len(data['prior_version'])}`")
    print(f"- Ambiguous status language: `{len(data['ambiguous_status'])}`")
    print(f"- Virasoro shadow-doctrine drift: `{len(data['virasoro_shadow_drift'])}`")
    print(f"- Infinite-generator frontier drift: `{len(data['infinite_generator_drift'])}`")
    print(f"- DK scope drift: `{len(data['dk_scope_drift'])}`")
    print(f"- Periodicity-profile drift: `{len(data['periodicity_profile_drift'])}`")
    print(f"- KL scope drift: `{len(data['kl_scope_drift'])}`")
    print(f"- Periodicity overclaim drift: `{len(data['periodicity_overclaim_drift'])}`")
    print(f"- Package-scope drift: `{len(data['package_scope_drift'])}`")
    print(f"- MC2 frontier drift: `{len(data['mc2_frontier_drift'])}`")
    print(f"- Stale frontier-phrase drift: `{len(data['frontier_stale_phrase_drift'])}`")
    print(f"- AI-tell candidates: `{len(data['ai_tells'])}`")
    print(f"- Cross-file duplicate paragraphs: `{len(data['duplicates'])}`")
    print(f"- Long paragraphs (>1200 chars): `{len(data['long_paragraphs'])}`")
    print()

    print_section("Structural Findings")
    if data["missing_goq"]:
        for path in data["missing_goq"][:limit]:
            print(f"- missing governing question: `{path}`")
    if data["missing_hms"]:
        for path in data["missing_hms"][:limit]:
            print(f"- missing semantic-level marker: `{path}`")
    if data["untagged"]:
        print_findings(data["untagged"], limit)
    if not data["missing_goq"] and not data["missing_hms"] and not data["untagged"]:
        print("- none")
    print()

    print_section("Prior-Version Leaks")
    if data["prior_version"]:
        print_findings(data["prior_version"], limit)
    else:
        print("- none")
    print()

    print_section("Ambiguous Status Language")
    if data["ambiguous_status"]:
        print_findings(data["ambiguous_status"], limit)
    else:
        print("- none")
    print()

    print_section("Virasoro Shadow-Doctrine Drift")
    if data["virasoro_shadow_drift"]:
        print_findings(data["virasoro_shadow_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Infinite-Generator Frontier Drift")
    if data["infinite_generator_drift"]:
        print_findings(data["infinite_generator_drift"], limit)
    else:
        print("- none")
    print()

    print_section("DK Scope Drift")
    if data["dk_scope_drift"]:
        print_findings(data["dk_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Periodicity-Profile Drift")
    if data["periodicity_profile_drift"]:
        print_findings(data["periodicity_profile_drift"], limit)
    else:
        print("- none")
    print()

    print_section("KL Scope Drift")
    if data["kl_scope_drift"]:
        print_findings(data["kl_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Periodicity Overclaim Drift")
    if data["periodicity_overclaim_drift"]:
        print_findings(data["periodicity_overclaim_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Package-Scope Drift")
    if data["package_scope_drift"]:
        print_findings(data["package_scope_drift"], limit)
    else:
        print("- none")
    print()

    print_section("MC2 Frontier Drift")
    if data["mc2_frontier_drift"]:
        print_findings(data["mc2_frontier_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Stale Frontier-Phrase Drift")
    if data["frontier_stale_phrase_drift"]:
        print_findings(data["frontier_stale_phrase_drift"], limit)
    else:
        print("- none")
    print()

    print_section("Duplicate Paragraphs")
    if data["duplicates"]:
        for _, paras in data["duplicates"][:limit]:
            print(f"- duplicate x{len(paras)}")
            for para in paras[:4]:
                snippet = para.text[:140].strip()
                print(f"  - `{para.path}:{para.line}` {snippet}")
    else:
        print("- none")
    print()

    print_section("Long Paragraphs")
    if data["long_paragraphs"]:
        print_paragraphs(data["long_paragraphs"], limit)
    else:
        print("- none")
    print()

    print_section("AI-Tell Candidates")
    if data["ai_tells"]:
        print_findings(data["ai_tells"], limit)
    else:
        print("- none")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=12, help="Maximum findings per section.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero on structural failures or prior-version leakage.",
    )
    args = parser.parse_args()

    data = scan()
    report(data, args.limit)

    if args.strict and (
        data["missing_goq"]
        or data["missing_hms"]
        or data["untagged"]
        or data["prior_version"]
        or data["ambiguous_status"]
        or data["virasoro_shadow_drift"]
        or data["infinite_generator_drift"]
        or data["dk_scope_drift"]
        or data["periodicity_profile_drift"]
        or data["kl_scope_drift"]
        or data["periodicity_overclaim_drift"]
        or data["package_scope_drift"]
        or data["mc2_frontier_drift"]
        or data["frontier_stale_phrase_drift"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
