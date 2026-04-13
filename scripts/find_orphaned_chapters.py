#!/usr/bin/env python3
"""Find chapter files that are not reachable from main.tex.

The script follows non-commented \\input{...} and \\include{...} edges
transitively, then reports unreachable files in the standard chapter
directories used by the book.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


INCLUDE_RE = re.compile(r"^(?!\s*%).*\\(?:input|include)\{([^}]+)\}", re.M)


def resolve_child(repo_root: Path, token: str) -> Path | None:
    rel = Path(token if token.endswith(".tex") else f"{token}.tex")
    candidate = repo_root / rel
    return candidate if candidate.exists() else None


def walk_graph(repo_root: Path, root_tex: Path) -> set[Path]:
    seen: set[Path] = set()
    stack = [root_tex]

    while stack:
        current = stack.pop()
        if current in seen or not current.exists():
            continue
        seen.add(current)
        text = current.read_text(encoding="utf-8")
        for match in INCLUDE_RE.finditer(text):
            child = resolve_child(repo_root, match.group(1))
            if child is not None and child not in seen:
                stack.append(child)

    return seen


def iter_candidates(repo_root: Path) -> list[Path]:
    dirs = [
        repo_root / "chapters" / "theory",
        repo_root / "chapters" / "examples",
        repo_root / "chapters" / "connections",
    ]
    out: list[Path] = []
    for directory in dirs:
        out.extend(sorted(directory.glob("*.tex")))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="main.tex",
        help="TeX root file, relative to the repository root (default: main.tex)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    root_tex = repo_root / args.root
    if not root_tex.exists():
        print(f"missing root file: {root_tex}", file=sys.stderr)
        return 1

    reachable = walk_graph(repo_root, root_tex)
    for path in iter_candidates(repo_root):
        if path not in reachable:
            print(path.relative_to(repo_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
