#!/usr/bin/env python3
"""Build the Vol I chapter dependency DAG and report SCC/back-edge data.

The script scans `chapters/**/*.tex`, `standalone/**/*.tex`, and
`appendices/**/*.tex`, resolves cross-file `\\ref`-family links against local
`\\label`s, computes strongly connected components with Tarjan's algorithm, and
emits a raw report for the AP284 DAG audit.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import argparse
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MAIN_TEX = ROOT / "main.tex"
DEFAULT_REPORT = ROOT / "adversarial_swarm_20260418" / "ap284_dag_report.txt"
SEARCH_ROOTS = ("chapters", "standalone", "appendices")

INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|[cC]ref|eqref|[aA]utoref)\{([^}]*)\}")

NAMED_KOSZUL_SOURCES = {
    "chapters/theory/chiral_koszul_pairs.tex",
    "chapters/theory/koszulness_vii_multiweight_platonic.tex",
    "chapters/theory/chiral_hochschild_koszul.tex",
}
HIGHER_GENUS_TARGETS = {
    "chapters/theory/higher_genus_foundations.tex",
    "chapters/theory/higher_genus_complementarity.tex",
    "chapters/theory/higher_genus_modular_koszul.tex",
}
KOSZUL_BLOCK_START = "chapters/theory/chiral_koszul_pairs.tex"
KOSZUL_BLOCK_END = "chapters/theory/koszulness_vii_multiweight_platonic.tex"


@dataclass(frozen=True)
class LabelOccurrence:
    label: str
    file: str
    line: int


@dataclass(frozen=True)
class RefOccurrence:
    label: str
    command: str
    file: str
    line: int


@dataclass(frozen=True)
class ResolvedReference:
    ref: RefOccurrence
    owner: LabelOccurrence


def strip_comments_with_newlines(text: str) -> str:
    """Strip LaTeX comments while preserving line count."""
    stripped_lines: list[str] = []
    for raw_line in text.splitlines():
        out: list[str] = []
        escaped = False
        for char in raw_line:
            if char == "%" and not escaped:
                break
            out.append(char)
            escaped = (char == "\\") and not escaped
            if char != "\\":
                escaped = False
        stripped_lines.append("".join(out))
    return "\n".join(stripped_lines)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def tex_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for base in SEARCH_ROOTS:
        base_path = root / base
        if not base_path.exists():
            continue
        files.extend(sorted(base_path.rglob("*.tex")))
    return files


def canonical_main_order(root: Path, main_tex: Path) -> dict[str, int]:
    order: dict[str, int] = {}
    if not main_tex.is_file():
        return order

    main_text = strip_comments_with_newlines(
        main_tex.read_text(encoding="utf-8", errors="ignore")
    )
    next_index = 1
    for match in INCLUDE_RE.finditer(main_text):
        rel = match.group(1).strip()
        if not rel.endswith(".tex"):
            rel = f"{rel}.tex"
        candidate = root / rel
        if not candidate.is_file():
            continue
        rel_name = relpath(candidate, root)
        if rel_name in order:
            continue
        order[rel_name] = next_index
        next_index += 1
    return order


def parse_file(path: Path, root: Path) -> tuple[list[LabelOccurrence], list[RefOccurrence]]:
    rel = relpath(path, root)
    text = strip_comments_with_newlines(path.read_text(encoding="utf-8", errors="ignore"))

    labels = [
        LabelOccurrence(
            label=match.group(1).strip(),
            file=rel,
            line=line_number(text, match.start()),
        )
        for match in LABEL_RE.finditer(text)
    ]

    refs: list[RefOccurrence] = []
    for match in REF_RE.finditer(text):
        command_match = re.match(r"\\([A-Za-z]+)\{", match.group(0))
        command = command_match.group(1) if command_match else "ref"
        labels_raw = match.group(1)
        for piece in labels_raw.split(","):
            label = piece.strip()
            if not label:
                continue
            refs.append(
                RefOccurrence(
                    label=label,
                    command=command,
                    file=rel,
                    line=line_number(text, match.start()),
                )
            )
    return labels, refs


def tarjan_scc(nodes: Iterable[str], adjacency: dict[str, set[str]]) -> list[list[str]]:
    """Hand-rolled Tarjan SCC implementation."""
    node_list = list(nodes)
    index = 0
    indices: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    components: list[list[str]] = []

    sys.setrecursionlimit(max(2000, len(node_list) * 4 + 100))

    def strongconnect(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for neighbor in sorted(adjacency.get(node, set())):
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[node] = min(lowlink[node], indices[neighbor])

        if lowlink[node] != indices[node]:
            return

        component: list[str] = []
        while stack:
            popped = stack.pop()
            on_stack.remove(popped)
            component.append(popped)
            if popped == node:
                break
        components.append(component)

    for node in sorted(node_list):
        if node not in indices:
            strongconnect(node)

    return components


def order_value(order: dict[str, int], file_name: str) -> tuple[int, str]:
    return (order.get(file_name, 10**9), file_name)


def is_koszul_programme_source(file_name: str, order: dict[str, int]) -> bool:
    if file_name in NAMED_KOSZUL_SOURCES:
        return True
    idx = order.get(file_name)
    start_idx = order.get(KOSZUL_BLOCK_START)
    end_idx = order.get(KOSZUL_BLOCK_END)
    if start_idx is None or end_idx is None or idx is None:
        return False
    return (
        file_name.startswith("chapters/theory/")
        and start_idx <= idx <= end_idx
    )


def format_index(order: dict[str, int], file_name: str) -> str:
    idx = order.get(file_name)
    return str(idx) if idx is not None else "n/a"


def build_report(
    root: Path,
    order: dict[str, int],
    files: list[str],
    labels_by_name: dict[str, list[LabelOccurrence]],
    refs: list[RefOccurrence],
    pair_occurrences: dict[tuple[str, str], list[ResolvedReference]],
    ambiguous_refs: list[tuple[RefOccurrence, list[LabelOccurrence]]],
    unresolved_refs: list[RefOccurrence],
    sccs: list[list[str]],
) -> str:
    non_trivial = [sorted(component, key=lambda item: order_value(order, item))
                   for component in sccs if len(component) > 1]
    non_trivial.sort(key=lambda comp: (-len(comp), [order_value(order, name) for name in comp]))
    largest = non_trivial[0] if non_trivial else []

    back_edge_pairs: list[tuple[str, str, list[ResolvedReference]]] = []
    for (src, dst), occurrences in pair_occurrences.items():
        if not is_koszul_programme_source(src, order):
            continue
        if dst not in HIGHER_GENUS_TARGETS:
            continue
        src_idx = order.get(src)
        dst_idx = order.get(dst)
        if src_idx is None or dst_idx is None or src_idx >= dst_idx:
            continue
        back_edge_pairs.append((src, dst, occurrences))

    back_edge_pairs.sort(
        key=lambda item: (
            order_value(order, item[0]),
            order_value(order, item[1]),
            item[2][0].ref.line if item[2] else 10**9,
        )
    )

    lines: list[str] = []
    lines.append("AP284 Chapter Dependency DAG Report")
    lines.append(f"root: {root}")
    lines.append(f"main_tex: {root / 'main.tex'}")
    lines.append("")
    lines.append("Scan summary")
    lines.append(f"- scanned_tex_files: {len(files)}")
    lines.append(f"- labels_found: {sum(len(entries) for entries in labels_by_name.values())}")
    lines.append(f"- unique_label_names: {len(labels_by_name)}")
    lines.append(f"- duplicate_label_names: {sum(1 for entries in labels_by_name.values() if len(entries) > 1)}")
    lines.append(f"- ref_occurrences: {len(refs)}")
    lines.append(f"- unresolved_refs_no_owner: {len(unresolved_refs)}")
    lines.append(f"- unresolved_refs_ambiguous_owner: {len(ambiguous_refs)}")
    lines.append(f"- cross_file_ref_occurrences: {sum(len(items) for items in pair_occurrences.values())}")
    lines.append(f"- cross_file_edges_unique: {len(pair_occurrences)}")
    lines.append(f"- canonical_main_ordered_files: {len(order)}")
    lines.append("")
    lines.append("SCC summary")
    lines.append(f"- non_trivial_scc_count: {len(non_trivial)}")
    lines.append(
        "- non_trivial_scc_sizes: "
        + (", ".join(str(len(component)) for component in non_trivial) if non_trivial else "none")
    )
    lines.append(f"- largest_scc_size: {len(largest)}")
    lines.append("- largest_scc_membership:")
    if largest:
        for member in largest:
            lines.append(f"  - [{format_index(order, member)}] {member}")
    else:
        lines.append("  - none")

    lines.append("")
    lines.append("Koszul-programme -> higher-genus back-edges")
    lines.append(
        "- source_set: named {chiral_koszul_pairs, koszulness_vii_multiweight_platonic, "
        "chiral_hochschild_koszul} union chapters/theory block from "
        "chiral_koszul_pairs.tex through koszulness_vii_multiweight_platonic.tex"
    )
    lines.append(
        "- target_set: higher_genus_foundations.tex, higher_genus_complementarity.tex, "
        "higher_genus_modular_koszul.tex"
    )
    lines.append("- back_edge_rule: canonical_index(source) < canonical_index(target)")
    lines.append(f"- back_edge_pair_count: {len(back_edge_pairs)}")
    lines.append(f"- back_edge_ref_occurrences: {sum(len(items) for _, _, items in back_edge_pairs)}")
    if not back_edge_pairs:
        lines.append("  - none")
    else:
        for src, dst, occurrences in back_edge_pairs:
            lines.append(
                f"  - [{format_index(order, src)}] {src} -> "
                f"[{format_index(order, dst)}] {dst}: {len(occurrences)} occurrence(s)"
            )
            for occurrence in sorted(occurrences, key=lambda item: (item.ref.line, item.ref.label)):
                lines.append(
                    "      "
                    f"{occurrence.ref.file}:{occurrence.ref.line} "
                    f"\\{occurrence.ref.command}{{{occurrence.ref.label}}} -> "
                    f"{occurrence.owner.file}:{occurrence.owner.line} "
                    f"\\label{{{occurrence.owner.label}}}"
                )

    lines.append("")
    lines.append("Duplicate labels (ambiguous owners)")
    duplicates = [
        (label, owners)
        for label, owners in labels_by_name.items()
        if len(owners) > 1
    ]
    duplicates.sort(key=lambda item: item[0])
    if not duplicates:
        lines.append("  - none")
    else:
        for label, owners in duplicates[:100]:
            owner_text = ", ".join(f"{owner.file}:{owner.line}" for owner in owners)
            lines.append(f"  - {label}: {owner_text}")

    lines.append("")
    lines.append("Ambiguous resolved refs skipped from graph")
    if not ambiguous_refs:
        lines.append("  - none")
    else:
        for ref, owners in ambiguous_refs[:100]:
            owner_text = ", ".join(f"{owner.file}:{owner.line}" for owner in owners)
            lines.append(
                f"  - {ref.file}:{ref.line} \\{ref.command}{{{ref.label}}} -> ambiguous among {owner_text}"
            )

    lines.append("")
    lines.append("Unresolved refs without a local owner")
    if not unresolved_refs:
        lines.append("  - none")
    else:
        for ref in unresolved_refs[:100]:
            lines.append(f"  - {ref.file}:{ref.line} \\{ref.command}{{{ref.label}}}")

    return "\n".join(lines) + "\n"


def run(root: Path, report_path: Path) -> str:
    order = canonical_main_order(root, root / "main.tex")
    paths = tex_files(root)

    labels_by_name: dict[str, list[LabelOccurrence]] = defaultdict(list)
    refs: list[RefOccurrence] = []
    file_names = [relpath(path, root) for path in paths]

    for path in paths:
        labels, file_refs = parse_file(path, root)
        for occurrence in labels:
            labels_by_name[occurrence.label].append(occurrence)
        refs.extend(file_refs)

    pair_occurrences: dict[tuple[str, str], list[ResolvedReference]] = defaultdict(list)
    ambiguous_refs: list[tuple[RefOccurrence, list[LabelOccurrence]]] = []
    unresolved_refs: list[RefOccurrence] = []
    adjacency: dict[str, set[str]] = {name: set() for name in file_names}

    for ref in refs:
        owners = labels_by_name.get(ref.label, [])
        if not owners:
            unresolved_refs.append(ref)
            continue
        if len(owners) > 1:
            ambiguous_refs.append((ref, owners))
            continue
        owner = owners[0]
        if owner.file == ref.file:
            continue
        pair_occurrences[(ref.file, owner.file)].append(ResolvedReference(ref=ref, owner=owner))
        adjacency[ref.file].add(owner.file)

    components = tarjan_scc(file_names, adjacency)
    report = build_report(
        root=root,
        order=order,
        files=file_names,
        labels_by_name=labels_by_name,
        refs=refs,
        pair_occurrences=pair_occurrences,
        ambiguous_refs=ambiguous_refs,
        unresolved_refs=unresolved_refs,
        sccs=components,
    )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root to scan (default: this script's parent repo).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_REPORT,
        help="Path to the raw text report.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    report = run(root=root, report_path=output)
    print(report, end="")
    print(f"Wrote report to {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
