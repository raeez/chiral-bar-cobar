#!/usr/bin/env python3
"""Export Vol I cross-reference labels into a flat .aux file for Vol II xr-hyper.

Recursively reads main.aux and all \\@input{...} referenced aux files,
extracts every \\newlabel{...}{...} and \\new@label@record{...}{...} entry,
and writes them into a single flat file vol1-xrefs.aux that xr-hyper can
read without hitting its \\read capacity limit.

Usage:
    python3 scripts/export_vol1_xrefs.py
"""

import os
import re
import sys

# ── Configuration ──────────────────────────────────────────────────────────
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN_AUX = os.path.join(ROOT_DIR, "main.aux")
OUTPUT = os.path.join(ROOT_DIR, "vol1-xrefs.aux")

# Patterns
INPUT_RE = re.compile(r"\\@input\{([^}]+)\}")
LABEL_RE = re.compile(r"^\\(?:newlabel|new@label@record)\{")


def collect_labels(aux_path: str, visited: set) -> list[str]:
    """Recursively collect label lines from an aux file and its children."""
    aux_path = os.path.normpath(aux_path)
    if aux_path in visited:
        return []
    visited.add(aux_path)

    if not os.path.isfile(aux_path):
        print(f"  WARNING: referenced aux file not found: {aux_path}",
              file=sys.stderr)
        return []

    labels = []
    parent_dir = os.path.dirname(aux_path)

    with open(aux_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue

            # Recurse into child aux files
            m = INPUT_RE.search(stripped)
            if m:
                child = os.path.join(
                    os.path.dirname(MAIN_AUX), m.group(1)
                )
                labels.extend(collect_labels(child, visited))
                continue

            # Keep label entries
            if LABEL_RE.match(stripped):
                labels.append(stripped)

    return labels


def main():
    if not os.path.isfile(MAIN_AUX):
        print(f"ERROR: main.aux not found at {MAIN_AUX}", file=sys.stderr)
        print("       Build Vol I first: make fast", file=sys.stderr)
        sys.exit(1)

    print(f"Reading label tree from {MAIN_AUX}")
    visited: set[str] = set()
    labels = collect_labels(MAIN_AUX, visited)

    # Deduplicate while preserving order (last wins for duplicate keys,
    # but xr-hyper is fine with duplicates; we keep all for safety)
    print(f"  Scanned {len(visited)} aux file(s)")

    # Write flat output
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\\relax\n")
        for label in labels:
            f.write(label + "\n")

    size_kb = os.path.getsize(OUTPUT) / 1024
    print(f"Wrote {OUTPUT}")
    print(f"  Labels exported: {len(labels)}")
    print(f"  File size:       {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
