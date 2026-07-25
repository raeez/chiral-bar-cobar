"""Scope guard for the universal W-algebra PBW/Koszul lane."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXISTENCE = ROOT / "chapters" / "theory" / "existence_criteria.tex"
LEDGER = ROOT / "notes" / "audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes" / "external_review_harvest_matrix_20260617.md"


def visible(path: Path) -> str:
    return "\n".join(
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("%")
    )


def test_universal_w_algebra_is_not_claimed_koszul_at_every_level():
    text = visible(EXISTENCE)

    retired_fragments = (
        r"is chirally Koszul at every level~$k$",
        "PBW bar-coalgebra comparison at every level",
    )
    for fragment in retired_fragments:
        assert fragment not in text


def test_universal_w_algebra_scope_names_boundary_surfaces():
    text = visible(EXISTENCE)

    required_fragments = (
        r"generic/non-critical principal $\mathcal W$ lane",
        "Feigin--Frenkel centre/Sugawara--KZ boundary",
        "centre/Sugawara--KZ degeneration is a separate boundary surface",
        "admissible or other simple-quotient levels",
        "null-vector obstruction calculation",
        "finite-type or completed",
        "Theorem~H amplitude",
        "strict post-Verdier algebra",
    )
    for fragment in required_fragments:
        assert fragment in text


def test_w_algebra_scope_repair_is_logged_in_harvest_records():
    ledger = LEDGER.read_text(encoding="utf-8")
    matrix = MATRIX.read_text(encoding="utf-8")

    for text in (ledger, matrix):
        assert "Pass 560" in text
        assert "universal W-algebra" in text
        assert "generic/non-critical principal" in text
        assert "Feigin--Frenkel centre/Sugawara--KZ boundary" in text
