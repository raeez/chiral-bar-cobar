#!/usr/bin/env python3
"""Regenerate PHASE0 theorem dependency index from active theory graph."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import re
from collections import Counter


ROOT = Path(__file__).resolve().parents[1]
MAIN_TEX = ROOT / "main.tex"
OUT_MD = ROOT / "PHASE0_THEOREM_DEPENDENCY_INDEX.md"

THEOREM_ENVS = ("theorem", "lemma", "proposition", "corollary")
STATUS_RE = re.compile(
    r"\\ClaimStatus(ProvedHere|ProvedElsewhere|Open|Conjectured)"
)
LABEL_RE = re.compile(r"\\label\{((?:thm|lem|prop|cor):[^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|autoref|Cref|cref|eqref)\{([^}]+)\}")
BEGIN_RE = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary)\}")
INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")


@dataclass
class Node:
    label: str
    kind: str
    status: str
    location: str
    deps: list[str]


def strip_comments(text: str) -> str:
    return "\n".join(line.split("%", 1)[0] for line in text.splitlines())


def active_theory_files() -> list[Path]:
    main = strip_comments(MAIN_TEX.read_text(encoding="utf-8", errors="ignore"))
    ordered: list[Path] = []
    seen: set[Path] = set()
    for match in INCLUDE_RE.finditer(main):
        rel = match.group(1)
        if not rel.endswith(".tex"):
            rel = f"{rel}.tex"
        path = ROOT / rel
        if not path.is_file():
            continue
        if "chapters/theory/" not in rel:
            continue
        if path in seen:
            continue
        seen.add(path)
        ordered.append(path)
    return ordered


def find_env_end(lines: list[str], start: int, kind: str) -> int:
    end_token = f"\\end{{{kind}}}"
    for i in range(start + 1, len(lines)):
        if end_token in lines[i]:
            return i
    return len(lines) - 1


def build_nodes(files: list[Path]) -> dict[str, Node]:
    nodes: dict[str, Node] = {}

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        i = 0
        while i < len(lines):
            line = lines[i]
            m = BEGIN_RE.search(line)
            if not m:
                i += 1
                continue

            kind = m.group(1)
            end = find_env_end(lines, i, kind)
            segment_lines = lines[i : end + 1]
            segment = "\n".join(segment_lines)

            status_match = STATUS_RE.search(segment)
            status = status_match.group(1) if status_match else "Unknown"

            deps: list[str] = []
            for ref_match in REF_RE.finditer(segment):
                for raw in ref_match.group(1).split(","):
                    key = raw.strip()
                    if re.match(r"^(thm|lem|prop|cor):", key):
                        deps.append(key)

            labels = LABEL_RE.findall(segment)
            if not labels:
                i = end + 1
                continue

            for label in labels:
                if label in nodes:
                    continue
                label_line = i + 1
                for local_idx, local_line in enumerate(segment_lines):
                    if f"\\label{{{label}}}" in local_line:
                        label_line = i + local_idx + 1
                        break
                nodes[label] = Node(
                    label=label,
                    kind=kind,
                    status=status,
                    location=f"{rel}:{label_line}",
                    deps=deps,
                )

            i = end + 1

    node_labels = set(nodes.keys())
    for node in nodes.values():
        uniq = []
        seen = set()
        for dep in node.deps:
            if dep not in node_labels:
                continue
            if dep in seen:
                continue
            seen.add(dep)
            uniq.append(dep)
        node.deps = uniq

    return nodes


def open_ref_counts(files: list[Path], nodes: dict[str, Node]) -> Counter[str]:
    open_labels = {
        label
        for label, node in nodes.items()
        if node.status in {"Open", "Conjectured"}
    }
    counts: Counter[str] = Counter()
    for path in files:
        text = strip_comments(path.read_text(encoding="utf-8", errors="ignore"))
        for ref_match in REF_RE.finditer(text):
            for raw in ref_match.group(1).split(","):
                key = raw.strip()
                if key in open_labels:
                    counts[key] += 1
    return counts


def render_index(nodes: dict[str, Node]) -> str:
    rows = sorted(nodes.values(), key=lambda n: n.label)
    out = []
    out.append("# Phase 0 Theorem Dependency Index (Active Theory Graph)")
    out.append("")
    out.append(f"Date: {date.today().isoformat()}")
    out.append("Scope: active `chapters/theory/*.tex` files included by `main.tex`.")
    out.append("")
    out.append(
        "Generation: deterministic extraction from theorem/lemma/proposition/corollary "
        "blocks with theorem-like labels (`thm:`, `lem:`, `prop:`, `cor:`); "
        "dependencies are in-block `\\ref`-family edges to theorem-like labels "
        "in the same active theory graph."
    )
    out.append("")
    out.append(f"Total indexed claim nodes: {len(rows)}")
    out.append("")
    out.append("| Label | Kind | Status tag | Location | Dependency labels |")
    out.append("|---|---|---|---|---|")
    for node in rows:
        deps = ", ".join(node.deps) if node.deps else "—"
        out.append(
            f"| `{node.label}` | `{node.kind}` | `{node.status}` | "
            f"`{node.location}` | {deps} |"
        )
    out.append("")
    return "\n".join(out)


def main() -> None:
    files = active_theory_files()
    nodes = build_nodes(files)
    OUT_MD.write_text(render_index(nodes), encoding="utf-8")

    counts = open_ref_counts(files, nodes)
    print(f"ACTIVE_THEORY_FILES={len(files)}")
    print(f"INDEXED_NODES={len(nodes)}")
    print(
        "OPEN_LABELS="
        + str(
            sum(
                1
                for n in nodes.values()
                if n.status in {"Open", "Conjectured"}
            )
        )
    )
    for label, count in counts.most_common(10):
        node = nodes.get(label)
        if not node:
            continue
        print(f"OPEN_REF_COUNT {count:3d} {label} {node.location}")


if __name__ == "__main__":
    main()
