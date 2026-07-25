"""Completion guards for the external-review harvest surface."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"

LIVE_TEX_ROOTS = (
    ROOT / "chapters",
    ROOT / "appendices",
    ROOT / "standalone",
)


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def live_tex_files() -> list[Path]:
    files: list[Path] = []
    for root in LIVE_TEX_ROOTS:
        files.extend(path for path in root.rglob("*.tex") if ".bak" not in path.name)
    return sorted(files)


def live_tex_and_main_files() -> list[Path]:
    return [ROOT / "main.tex", *live_tex_files()]


def assert_no_live_fragment(fragment: str) -> None:
    for path in live_tex_files():
        text = visible(path)
        assert fragment not in text, f"{fragment!r} remains in {path.relative_to(ROOT)}"


def assert_no_live_regex(pattern: str) -> None:
    compiled = re.compile(pattern, re.IGNORECASE | re.DOTALL)
    for path in live_tex_files():
        text = visible(path)
        match = compiled.search(text)
        assert match is None, (
            f"{pattern!r} matched {match.group(0)!r} in {path.relative_to(ROOT)}"
        )


def test_external_harvest_matrix_has_no_unresolved_table_statuses():
    text = MATRIX.read_text()
    table_rows = [line for line in text.splitlines() if line.startswith("|")]
    unresolved = ("open", "audit", "partial", "ongoing")
    for row in table_rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        if len(cells) >= 3 and cells[0] not in {"Source item", "---", "Block"}:
            status = cells[2].lower()
            for word in unresolved:
                assert word not in status, row

    required = (
        "materials/raw/2026-06-05-chiral1-research-paper-strengthening.pdf",
        "materials/raw/2026-06-17-chiral-bar-cobar-manuscript-review-and-improvement.pdf",
        "materials/raw/2026-06-17-expanded-expert-repair-specification-main36.md",
        "references/source-provenance.md",
        "The harvestable local mathematical corrections from the three external",
        "Residual work is nonlocal",
        "There are no `open`, `audit`, `partial`, or `ongoing` table statuses",
        "Pass 540 hardens the harvest-control surface",
        "Pass 554 fences the BP scalar-conductor compute layer",
        "Pass 557 guards the fatal-navigation placeholder forms",
        "Pass 558 fences the Linshaw--Qi admissible",
        "Pass 559 removes the residual PBW-universality critical/admissible",
        "Pass 560 removes the corresponding detailed universal W-algebra",
        "Pass 561 syncs the standalone",
        "Pass 562 repairs the ordered chiral-homology symmetric descent",
        "Pass 563 sharpens the lossy-descent theorem",
        "Pass 564 gates Verlinde recovery",
        "Pass 565 gates the canonical pointed-bar/conformal-block bridge",
        "Pass 566 syncs the pointed-bar/conformal-block metadata",
        "Pass 567 fences the Theorem A ambient-transfer route",
        "Pass 568 proves the rank-one Heisenberg finite-window combinatorics",
        "Pass 569 proves the two-point Heisenberg residue-twisted Arnold summand",
        "Pass 570 proves the curved second-kind Heisenberg endpoint",
        "Pass 571 proves the two-point Heisenberg weight-one polynomial string",
        "Pass 572 proves the two-point Heisenberg single-oscillator arbitrary-mode string",
        "Pass 573 proves the two-point Heisenberg single-mode polynomial arbitrary-mode string",
        "Pass 574 proves the two-point Heisenberg mixed-mode residue formula",
    )
    for fragment in required:
        assert fragment in text


def test_external_review_raw_sources_are_repo_local_with_provenance():
    provenance = ROOT / "references/source-provenance.md"
    assert provenance.exists()

    source_hashes = {
        "materials/raw/2026-06-05-chiral1-research-paper-strengthening.pdf":
            "5df7478dcbbe23b1d9b9e62e84668b89c21e0292356b945c6b842a6d47c56f22",
        "materials/raw/2026-06-17-chiral-bar-cobar-manuscript-review-and-improvement.pdf":
            "23dfb1968c7ca31e49cf2bfd6dbb6b33e06de1002e0f9dee3e5495c275b035c9",
        "materials/raw/2026-06-17-expanded-expert-repair-specification-main36.md":
            "c7301d510cea84e837a498d542cfade84b2cea13345fd52a0ac1d4a192981f04",
    }

    matrix = MATRIX.read_text()
    provenance_text = provenance.read_text()
    for relative, digest in source_hashes.items():
        assert (ROOT / relative).exists()
        assert relative in matrix
        assert relative in provenance_text
        assert digest in provenance_text


def test_external_review_source_item_coverage_is_explicit():
    text = MATRIX.read_text()
    flat_text = " ".join(text.split())
    compact_spec_rows = (
        "A1 / review theorem-status firewall",
        "A2 / review Theorem A ambient",
        "A3 / review object firewall",
        "A4 / review local/global",
        "A5 / review",
        "A6 / review nilpotence",
        "A7 / review positive-genus curvature",
        "A8 / review ordered-to-symmetric averaging",
        "B1 / review",
        "B2 / review Kontsevich gate",
        "B3 / review Gelfand gate",
        "B4 / review Polyakov gate",
        "B5 / review Gaiotto gate",
        "B6 / review Costello gate",
        "B7 / review Witten gate",
        "C1 same-pair residue",
        "C2 beta-gamma residue",
        "C3 Feigin--Frenkel language",
        "C4 DDYBE",
        "C5 K3/BKM/Hall",
        "D1 typed Arnold--KZ skeleton",
        "D2 typed Theorem A skeleton",
        "D3 typed Theorem C skeleton",
        "D4 typed Theorem D skeleton",
        "D5 typed Theorem H skeleton",
        "E rewrite policy",
    )
    for fragment in compact_spec_rows:
        assert fragment in flat_text

    review_pdf_fragments = (
        "(1) fatal build/navigation guard",
        "(2) local/global collision form",
        "(3) KZ--Arnold chain/connection typing",
        "(4) Arnold+Borcherds",
        "(5) same-pair residue",
        "(6) positive-genus curvature",
        "(7) bar cohomology versus chiral Hochschild",
        "(8) Theorem A ambient",
        "(9) Feigin--Frenkel",
        "(10) principal W-algebra",
        "(11) beta-gamma binary residue",
        "(12) DDYBE",
        "(13) q/hbar conventions",
        "(14) K3/BKM/Hall/GRT",
        "(15) physical bridges",
        "(16) five-theorem spine",
        "(17) named-reader checklist",
        "(18) healed ambition",
    )
    for fragment in review_pdf_fragments:
        assert fragment in flat_text


def test_external_review_fatal_navigation_placeholders_are_absent():
    """Guard the PDF's fatal-navigation warning without running LaTeX."""

    for path in live_tex_and_main_files():
        text = visible(path)
        assert "??" not in text, f"literal ?? placeholder remains in {path.relative_to(ROOT)}"

    placeholder_fragments = (
        "Vol II Remark ??",
        "Vol~II Remark~??",
        "Theorem ??",
        "Theorem~??",
        "Proposition ??",
        "Proposition~??",
        "Chapter ??",
        "Chapter~??",
        "Table ??",
        "Table~??",
        "§??",
    )
    for fragment in placeholder_fragments:
        for path in live_tex_and_main_files():
            text = visible(path)
            assert fragment not in text, (
                f"{fragment!r} remains in {path.relative_to(ROOT)}"
            )


def test_exact_external_review_retired_slogans_are_absent_from_live_tex():
    retired_fragments = (
        "Bar(A) is the bulk",
        "A is the primitive open sector",
        "bar differential = pulled-back KZ--Arnold connection",
        "bar differential = pulled-back KZ-Arnold connection",
        "same diagonal vanishes for degree reasons",
        "same diagonal is zero for degree reasons",
        "Arnold alone",
        "Feigin--Frenkel = Koszul duality",
        "Feigin--Frenkel Koszul dual sends",
        "CoHA(\\mathbb{C}^3)=\\mathcal W_{1+\\infty}",
        "\\mathrm{CoHA}(\\mathbb{C}^3)=\\mathcal W_{1+\\infty}",
        "\\Delta_5 constructs the BPS Hilbert space",
        "Z_BPS is the gravitational path integral",
        "PVA Jacobi \\Rightarrow all-loop",
        "PVA Jacobi implies all-loop",
        "FM propagator form $\\dlog(z_i - z_j)$",
    )
    for fragment in retired_fragments:
        assert_no_live_fragment(fragment)


def test_external_review_symbolic_drift_patterns_are_absent_from_live_tex():
    retired_patterns = (
        r"\\dbar\s*=\s*\\KZ\^\*",
        r"d_\{\\mathrm\{bar\}\}\s*=\s*\\mathrm\{KZ\}\^\*",
        r"d_B\s*=\s*KZ\^\*",
        r"\\kappa_\{\\mathrm\{BKM\}\}\s*=\s*\\kappa_\{\\mathrm\{ch\}\}\s*\+\s*\\chi",
        r"\\CoHA\s*\(\s*\\mathbb\{C\}\^3\s*\)\s*=\s*\\mathcal\s*W_\{1\+\\infty\}",
        r"Z_\{\\mathrm\{BPS\}\}\s+is\s+the\s+gravitational\s+path\s+integral",
    )
    for pattern in retired_patterns:
        assert_no_live_regex(pattern)


def test_final_local_global_dlog_harvest_is_inscribed_and_logged():
    notation = visible(ROOT / "appendices/notation_index.tex")
    signs = visible(ROOT / "appendices/signs_and_shifts.tex")
    ledger = LEDGER.read_text()
    matrix = MATRIX.read_text()

    for fragment in (
        "FM logarithmic normal form along $D_{ij}$",
        "affine/formal collision screen",
        "coordinate-change cocycle",
        "KZB/prime-form replacement data",
    ):
        assert fragment in notation

    for fragment in (
        "local normal coordinate on an affine/formal",
        "local representative of the logarithmic normal form",
        "coordinate-change or KZB/prime-form",
    ):
        assert fragment in signs

    assert "Pass 538" in ledger
    assert "Pass 538" in matrix
