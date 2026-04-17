#!/usr/bin/env python3
"""
Audit ProvedHere coverage vs the independent-verification registry.

Scans chapters/, appendices/, notes/, working_notes.tex for
  \\ClaimStatusProvedHere
then pairs each with the nearest preceding \\label{...}. Imports every test
module in compute/tests/ so that @independent_verification decorators fire
and populate the registry. Reports:

  (a) How many ProvedHere claims have at least one independent test.
  (b) Which claims are uncovered (the gap to close).
  (c) Any registry entry that is tautological (source overlap) -- note:
      the decorator raises at import time, so a tautology prevents the
      test module from loading. We still report via a catch.
  (d) Orphan registry entries (decorated tests whose claim label is not
      actually ProvedHere anywhere).

Exit status
-----------
0   : no tautologies and no orphans (coverage gap is OK; gap reduction is a
      continuous project).
2   : at least one tautological decoration OR at least one orphan entry.

The CI gate uses the nonzero exit. Coverage percentage is reported but not
enforced -- enforcing a floor would incentivize tautological "fix" tests.
"""

from __future__ import annotations

import argparse
import importlib
import re
import sys
import traceback
from pathlib import Path

# Allow running this script directly via `python compute/scripts/...`.
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compute.lib.independent_verification import (  # noqa: E402
    IndependentVerificationError,
    build_coverage_report,
    registry,
)


LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
PROVED_HERE_RE = re.compile(r"\\ClaimStatusProvedHere")
# ProvedElsewhere: claim proved in cited literature; carries decoration-
# eligible labels (tests verify external proof's predictions).
PROVED_ELSEWHERE_RE = re.compile(r"\\ClaimStatusProvedElsewhere")
# Conjectured/Conditional: claim not yet proved; falsifiable predictions
# can carry @independent_verification decorations.
CONJECTURED_RE = re.compile(r"\\ClaimStatus(?:Conjectured|Conditional)")
BEGIN_ENV_RE = re.compile(
    r"\\begin\{(theorem|proposition|lemma|corollary|conjecture|remark|"
    r"definition|construction)[^}]*\}"
)


def _scrape_status_labels(tex_root: Path,
                          status_re: re.Pattern[str]) -> dict[str, list[Path]]:
    """Generic label scraper parametrised by status regex.

    Same hybrid heuristic as scrape_proved_here but for any status tag.

    The forward-only and backward-only heuristics each miss legitimate
    aliasing and aggressive-forward falsely captures equation/section
    labels inside the proof body. The hybrid "collect all labels in the
    owning environment" approach is both strictly more complete than the
    prior backward-first heuristic (picks up aliases) and strictly more
    precise than the forward-first heuristic (stops at the first real
    non-label line e.g. equation / proof text, bounded by `+6` window).

    Returns
    -------
    dict mapping label -> list of files it appears in (usually one).
    """
    search_dirs = [
        tex_root / "chapters",
        tex_root / "appendices",
    ]
    # Also look at working_notes.tex and any top-level .tex in notes/.
    aux_files = []
    wn = tex_root / "working_notes.tex"
    if wn.exists():
        aux_files.append(wn)
    notes_dir = tex_root / "notes"
    if notes_dir.exists():
        aux_files.extend(sorted(notes_dir.glob("*.tex")))

    tex_files: list[Path] = []
    for d in search_dirs:
        if d.exists():
            tex_files.extend(sorted(d.rglob("*.tex")))
    tex_files.extend(aux_files)

    found: dict[str, list[Path]] = {}
    for f in tex_files:
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for idx, line in enumerate(lines):
            if not status_re.search(line):
                continue
            # Find the \begin{...} that owns this status tag (walk
            # backward up to 40 lines).
            begin_idx = -1
            lo = max(0, idx - 40)
            for back in range(idx, lo - 1, -1):
                if BEGIN_ENV_RE.search(lines[back]):
                    begin_idx = back
                    break
            # Collect ALL labels within the owning environment's HEADER
            # region. The header extends from the `\begin{...}` through
            # the status marker plus a small look-ahead (labels are
            # typically either immediately before or immediately after
            # the status line; beyond +2 we risk capturing equation
            # labels deeper in the statement body).
            if begin_idx < 0:
                scan_lo = max(0, idx - 3)
            else:
                scan_lo = begin_idx
            scan_hi = min(len(lines), idx + 3)
            captured: list[str] = []
            for j in range(scan_lo, scan_hi):
                line_j = lines[j]
                # Stop capturing if we hit an equation environment start
                # (those labels belong to equations, not the theorem).
                if re.search(r"\\begin\{equation", line_j):
                    break
                # Ignore `\label{eq:...}` even within the header window:
                # equations numbered inline in multiline headers are rare
                # but should not be registered as theorem names. The
                # theorem-alias stack universally uses non-`eq:` prefix.
                for m in LABEL_RE.finditer(line_j):
                    lbl = m.group(1)
                    if lbl.startswith("eq:"):
                        continue
                    captured.append(lbl)
            for label in captured:
                found.setdefault(label, []).append(f)
    return found


def scrape_proved_here(tex_root: Path) -> dict[str, list[Path]]:
    """Find every ProvedHere claim and the labels it attaches to."""
    return _scrape_status_labels(tex_root, PROVED_HERE_RE)


def scrape_proved_elsewhere(tex_root: Path) -> dict[str, list[Path]]:
    """Find every ProvedElsewhere claim and the labels it attaches to.

    These are claims proved in cited literature; tests verify the external
    proof's predictions against disjoint sources.
    """
    return _scrape_status_labels(tex_root, PROVED_ELSEWHERE_RE)


def scrape_conjectured(tex_root: Path) -> dict[str, list[Path]]:
    """Find every Conjectured/Conditional claim and the labels it attaches to.

    Decorations on conjecture labels are valid: they verify falsifiable
    predictions of a conjecture, not its truth.
    """
    return _scrape_status_labels(tex_root, CONJECTURED_RE)


def scrape_remark_definition_construction(tex_root: Path) -> dict[str, list[Path]]:
    """Find every \\begin{remark|definition|construction} and its label.

    These environments hold definitional/notational/constructive content
    that tests can decorate via @independent_verification (the test verifies
    notational consistency or constructed-object properties via disjoint
    inputs).

    Heuristic: for each \\begin{remark|definition|construction} match, walk
    FORWARD up to 8 lines for the nearest \\label{...}.
    """
    pattern = re.compile(
        r"\\begin\{(?:remark|definition|construction)[^}]*\}"
    )
    search_dirs = [
        tex_root / "chapters",
        tex_root / "appendices",
    ]
    aux_files = []
    wn = tex_root / "working_notes.tex"
    if wn.exists():
        aux_files.append(wn)
    notes_dir = tex_root / "notes"
    if notes_dir.exists():
        aux_files.extend(sorted(notes_dir.glob("*.tex")))

    tex_files: list[Path] = []
    for d in search_dirs:
        if d.exists():
            tex_files.extend(sorted(d.rglob("*.tex")))
    tex_files.extend(aux_files)

    found: dict[str, list[Path]] = {}
    for f in tex_files:
        try:
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for idx, line in enumerate(lines):
            if not pattern.search(line):
                continue
            hi = min(len(lines), idx + 8)
            for fwd in range(idx, hi):
                m = LABEL_RE.search(lines[fwd])
                if m:
                    label = m.group(1)
                    if not label.startswith("eq:"):
                        found.setdefault(label, []).append(f)
                    break
    return found


def load_test_modules(tests_dir: Path) -> list[tuple[str, BaseException]]:
    """Import every test_*.py under tests_dir to populate the registry.

    Returns a list of (module_name, error) for modules that failed to
    import. An IndependentVerificationError during import means a
    tautological decoration was caught -- we surface those separately.
    """
    failures: list[tuple[str, BaseException]] = []
    if not tests_dir.exists():
        return failures
    for test_file in sorted(tests_dir.glob("test_*.py")):
        # Build an importable dotted path from the repo root.
        rel = test_file.resolve().relative_to(REPO_ROOT)
        module_name = ".".join(rel.with_suffix("").parts)
        try:
            importlib.import_module(module_name)
        except BaseException as exc:  # noqa: BLE001
            failures.append((module_name, exc))
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tex-root", type=Path, default=REPO_ROOT,
        help="Manuscript root (default: repo root)",
    )
    parser.add_argument(
        "--tests-dir", type=Path,
        default=REPO_ROOT / "compute" / "tests",
        help="Directory with test_*.py files",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print every uncovered claim (can be long)",
    )
    parser.add_argument(
        "--show-orphans", action="store_true",
        help="Print every orphan registry entry",
    )
    args = parser.parse_args(argv)

    print(f"[audit] scanning {args.tex_root} for ProvedHere claims...")
    proved_here = scrape_proved_here(args.tex_root)
    print(f"[audit] found {len(proved_here)} ProvedHere-tagged labels.")

    print(f"[audit] scanning {args.tex_root} for ProvedElsewhere claims...")
    proved_elsewhere = scrape_proved_elsewhere(args.tex_root)
    print(f"[audit] found {len(proved_elsewhere)} ProvedElsewhere-tagged labels.")

    print(f"[audit] scanning {args.tex_root} for Conjectured/Conditional claims...")
    conjectured = scrape_conjectured(args.tex_root)
    print(f"[audit] found {len(conjectured)} Conjectured/Conditional-tagged labels.")

    print(f"[audit] scanning {args.tex_root} for remark/definition/construction labels...")
    rdc = scrape_remark_definition_construction(args.tex_root)
    print(f"[audit] found {len(rdc)} remark/definition/construction labels.")

    print(f"[audit] importing test modules from {args.tests_dir}...")
    failures = load_test_modules(args.tests_dir)

    # Separate tautological-decoration import failures from real errors.
    tautology_failures: list[tuple[str, IndependentVerificationError]] = []
    other_failures: list[tuple[str, BaseException]] = []
    for name, exc in failures:
        cause = exc
        is_tautology = False
        while cause is not None:
            if isinstance(cause, IndependentVerificationError):
                is_tautology = True
                break
            cause = cause.__cause__ or cause.__context__
        if is_tautology:
            tautology_failures.append((name, cause))  # type: ignore[arg-type]
        else:
            other_failures.append((name, exc))

    if other_failures:
        print(f"[audit] WARNING: {len(other_failures)} test module(s) failed "
              "to import (non-tautology). These are not counted as coverage.")
        for name, exc in other_failures[:5]:
            print(f"         {name}: {type(exc).__name__}: {exc}")

    other_valid = (set(proved_elsewhere.keys())
                   | set(conjectured.keys())
                   | set(rdc.keys()))
    report = build_coverage_report(proved_here.keys(), other_valid)

    print()
    print("=" * 72)
    print("INDEPENDENT VERIFICATION COVERAGE")
    print("=" * 72)
    print(report.summary())
    print()

    if tautology_failures:
        print("TAUTOLOGICAL DECORATIONS (blocked at import time):")
        for name, exc in tautology_failures:
            print(f"  - {name}")
            for line in str(exc).splitlines():
                print(f"      {line}")
        print()

    if report.tautological:
        # Should be empty in practice because the decorator raises at import
        # time. Still report for completeness in case someone bypasses.
        print("TAUTOLOGICAL REGISTRY ENTRIES (check decorator path):")
        for e in report.tautological:
            print(f"  - {e.claim}  [{e.test_qualname}]")
        print()

    if report.orphan_entries:
        print(f"ORPHAN REGISTRY ENTRIES ({len(report.orphan_entries)}): "
              "test decorates a claim label not found in any .tex as ProvedHere")
        if args.show_orphans:
            for e in report.orphan_entries:
                print(f"  - {e.claim}  [{e.test_qualname}]")
        else:
            for e in report.orphan_entries[:5]:
                print(f"  - {e.claim}  [{e.test_qualname}]")
            if len(report.orphan_entries) > 5:
                print(f"  ... and {len(report.orphan_entries) - 5} more "
                      "(use --show-orphans to see all)")
        print()

    if args.verbose and report.uncovered_claims:
        print(f"UNCOVERED CLAIMS ({len(report.uncovered_claims)}):")
        for c in sorted(report.uncovered_claims):
            files = proved_here.get(c, [])
            loc = files[0].relative_to(args.tex_root) if files else "<?>"
            print(f"  - {c}    ({loc})")
        print()

    # Exit status: fail on tautology or orphan; coverage gap is a metric, not
    # a gate (enforcing a coverage floor would incentivize low-quality tests).
    fail = bool(tautology_failures) or bool(report.orphan_entries) \
        or bool(report.tautological)
    if fail:
        print("AUDIT RESULT: FAIL "
              "(tautological decoration or orphan entry present)")
        return 2
    print("AUDIT RESULT: PASS (no tautologies, no orphans)")
    print(f"           coverage gap: {len(report.uncovered_claims)} claims "
          "without independent verification -- address incrementally")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
