"""Guards for theorem-status census remarks in editorial_constitution.tex."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/connections/editorial_constitution.tex"
LEDGER = ROOT / "notes/audit_repairs_ledger_20260610.md"
MATRIX = ROOT / "notes/external_review_harvest_matrix_20260617.md"


def visible_text() -> str:
    return "\n".join(
        line
        for line in SOURCE.read_text().splitlines()
        if not line.lstrip().startswith("%")
    )


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def environment_window(text: str, label: str, lines: int) -> str:
    anchor = rf"\label{{{label}}}"
    assert anchor in text, label
    prefix, suffix = text.split(anchor, 1)
    begin = prefix.rfind(r"\begin{")
    assert begin != -1, label
    return "\n".join((prefix[begin:] + anchor + suffix).splitlines()[:lines])


class TestEditorialConstitutionStatusCensusScope:
    def test_conjecture_attack_strategies_is_conditional_census(self):
        text = visible_text()
        window = normalized(environment_window(text, "rem:conjecture-attack-strategies", 35))

        required = (
            "Obstruction stratification by conjecture; \\ClaimStatusConditional",
            "status census and search-strategy surface",
            "supported only by finite computation",
            "remain conjectural",
            "does not promote any listed conjecture to a theorem",
            "Conjecture~\\ref{conj:scalar-saturation-universality}",
        )
        for fragment in required:
            assert fragment in window

        assert "\\ClaimStatusProvedHere" not in window

    def test_constitution_status_updates_is_conditional_census(self):
        text = visible_text()
        window = normalized(environment_window(text, "rem:constitution-status-updates", 45))

        required = (
            "Consequences of the theorem-status hypotheses; \\ClaimStatusConditional",
            "conditional status-census surface",
            "not a new proof of any referenced conjectural or conditional input",
            "Remark~\\ref{rem:mc3-type-b-folding}",
            "prefundamental Clebsch--Gordan closure",
            "not an input to the completed/coderived DK package",
        )
        for fragment in required:
            assert fragment in window

        forbidden = (
            "\\ClaimStatusProvedHere",
            "Proposition~\\ref{rem:mc3-type-b-folding}",
            "provides an alternative route for types $B_n$ and $C_n$",
        )
        for fragment in forbidden:
            assert fragment not in window

    def test_harvest_matrix_and_ledger_record_status_census_pass(self):
        ledger = LEDGER.read_text()
        matrix = MATRIX.read_text()

        assert "Pass 530: Editorial status-census remarks scoped" in ledger
        assert "Pass 530" in matrix
        assert "status-census remarks" in matrix
