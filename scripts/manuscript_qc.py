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
    active_files = active_include_graph()
    total_lines = 0
    missing_goq: list[pathlib.Path] = []
    missing_hms: list[pathlib.Path] = []
    untagged: list[Finding] = []
    prior_version: list[Finding] = []
    ai_tells: list[Finding] = []
    ambiguous_status: list[Finding] = []
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

        for para in paragraph_iter(rel, lines):
            if len(para.text) > 1200:
                long_paragraphs.append(para)
            duplicate_map[para.normalized].append(para)

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
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
