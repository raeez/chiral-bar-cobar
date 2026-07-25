r"""Primary-source guards for the Bershadsky--Polyakov scalar lanes."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import re

import pytest

from compute.lib.bp_koszul_conductor_engine import (
    BP_CONVENTIONS,
    BP_GENERATORS,
    BP_KAPPA_STATUS,
    KAPPA_COMPLEMENTARITY_EXACT,
    K_BP_EXACT,
    K_BP_SHIFTED_EXACT,
    SHIFTED_BP_CONVENTION,
    STANDARD_BP_CONVENTION,
    UnverifiedBPInvariantError,
    VARRHO_BP,
    K_BP,
    K_BP_shifted,
    c_BP,
    c_BP_shifted,
    compute_varrho,
    dual_level,
    kappa_BP,
    kappa_complementarity,
    self_dual_level,
    summary,
    verify_all,
)
from compute.lib.independent_verification import independent_verification


ROOT = Path(__file__).resolve().parents[2]
CENSUS = ROOT / "chapters" / "examples" / "landscape_census.tex"
BP_CHAPTER = ROOT / "chapters" / "examples" / "bershadsky_polyakov.tex"


C_BP_TEST_DATA = (
    (0, Fraction(-1), Fraction(51)),
    (1, Fraction(-5), Fraction(55)),
    (-1, Fraction(1), Fraction(49)),
    (2, Fraction(-49, 5), Fraction(299, 5)),
    (-2, Fraction(-5), Fraction(55)),
    (5, Fraction(-26), Fraction(76)),
    (10, Fraction(-713, 13), Fraction(1363, 13)),
    (-4, Fraction(55), Fraction(-5)),
)


class TestPrimaryConvention:
    def test_record_cites_the_primary_equation(self) -> None:
        assert STANDARD_BP_CONVENTION.name == "standard_fkr_equal_weight_G"
        assert STANDARD_BP_CONVENTION.status == "proved-primary-source"
        assert "Definition 2.1 and Eq. (2.2)" in STANDARD_BP_CONVENTION.source
        assert STANDARD_BP_CONVENTION.conductor == Fraction(50)
        assert BP_CONVENTIONS["standard"] is STANDARD_BP_CONVENTION

    @pytest.mark.parametrize("level, expected, expected_dual", C_BP_TEST_DATA)
    def test_hand_computed_values(
        self, level: int, expected: Fraction, expected_dual: Fraction
    ) -> None:
        assert c_BP(level) == expected
        assert c_BP(dual_level(level)) == expected_dual
        assert expected + expected_dual == Fraction(50)

    def test_two_primary_normalization_checks(self) -> None:
        assert c_BP(Fraction(-3, 2)) == 0
        assert c_BP(-1) == 1

    def test_critical_pole(self) -> None:
        with pytest.raises(ZeroDivisionError):
            c_BP(-3)


class TestLevelInvolutionAndConductor:
    @pytest.mark.parametrize(
        "level, companion",
        (
            (0, -6),
            (1, -7),
            (-1, -5),
            (-3, -3),
            (Fraction(1, 2), Fraction(-13, 2)),
        ),
    )
    def test_involution(self, level: int | Fraction, companion: int | Fraction) -> None:
        assert dual_level(level) == Fraction(companion)
        assert dual_level(dual_level(level)) == Fraction(level)

    def test_fixed_point_is_the_pole(self) -> None:
        assert self_dual_level() == -3
        assert dual_level(self_dual_level()) == self_dual_level()

    @pytest.mark.parametrize("level, _expected, _dual", C_BP_TEST_DATA)
    def test_standard_conductor(self, level: int, _expected: Fraction, _dual: Fraction) -> None:
        assert K_BP(level) == K_BP_EXACT == Fraction(50)


class TestPrimaryParityAndOpenKappa:
    def test_all_bp_strong_generators_are_even(self) -> None:
        assert BP_GENERATORS == {
            "J": (Fraction(1), 0),
            "G+": (Fraction(3, 2), 0),
            "G-": (Fraction(3, 2), 0),
            "T": (Fraction(2), 0),
        }

    def test_corrected_reciprocal_weight_diagnostic(self) -> None:
        contributions = {
            name: (Fraction(-1) if parity else Fraction(1)) / weight
            for name, (weight, parity) in BP_GENERATORS.items()
        }
        assert contributions == {
            "J": Fraction(1),
            "G+": Fraction(2, 3),
            "G-": Fraction(2, 3),
            "T": Fraction(1, 2),
        }
        assert compute_varrho() == Fraction(17, 6)

    def test_kappa_constants_are_withheld_pending_genus_one_computation(self) -> None:
        assert VARRHO_BP is None
        assert KAPPA_COMPLEMENTARITY_EXACT is None
        assert BP_KAPPA_STATUS.status == "open-genus-one-computation"
        assert "full genus-one curvature" in BP_KAPPA_STATUS.resolution_obligation

    @pytest.mark.parametrize("function", (kappa_BP, kappa_complementarity))
    def test_numeric_kappa_api_fails_loud(self, function) -> None:
        with pytest.raises(UnverifiedBPInvariantError, match="genus-one curvature"):
            function(0)


class TestShiftedConvention:
    def test_secondary_record(self) -> None:
        assert SHIFTED_BP_CONVENTION.name == "explicit_shifted_formula"
        assert SHIFTED_BP_CONVENTION.status == "computed-secondary"
        assert SHIFTED_BP_CONVENTION.conductor == Fraction(196)
        assert BP_CONVENTIONS["shifted"] is SHIFTED_BP_CONVENTION

    @pytest.mark.parametrize(
        "level, expected",
        ((0, Fraction(-6)), (1, Fraction(-22)), (-1, Fraction(2)), (-4, Fraction(218))),
    )
    def test_shifted_values(self, level: int, expected: Fraction) -> None:
        assert c_BP_shifted(level) == expected

    @pytest.mark.parametrize("level", (0, 1, -1, 2, -2, 5, 10, -4))
    def test_shifted_conductor(self, level: int) -> None:
        assert K_BP_shifted(level) == K_BP_SHIFTED_EXACT == Fraction(196)


class TestBatchAndSummary:
    def test_batch_verifies_certified_lanes(self) -> None:
        assert verify_all((0, 1, -1, 2, -2, -3, Fraction(1, 2)))

    def test_summary_exposes_status_instead_of_fabricated_numbers(self) -> None:
        packet = summary(0)
        assert packet["K_BP"] == Fraction(50)
        assert packet["reciprocal_weight_diagnostic"] == Fraction(17, 6)
        assert packet["kappa_status"] == "open-genus-one-computation"
        assert packet["kappa_BP(k)"] is None
        assert packet["kappa_complementarity"] is None


@independent_verification(
    claim="thm:bp-koszul-conductor-polynomial",
    derived_from=[
        "Fehily--Kawasetsu--Ridout 2021 Eq. (2.2)",
        "hand substitution at k=-3/2, -1, and 0",
    ],
    verified_against=["SymPy normalization in Q(k)"],
    disjoint_rationale=(
        "Fraction samples fix point values while SymPy proves the global "
        "rational-function identity."
    ),
)
def test_symbolic_primary_identity() -> None:
    sp = pytest.importorskip("sympy")
    k = sp.Symbol("k", rational=True)
    companion = -k - 6
    standard = -(2 * k + 3) * (3 * k + 1) / (k + 3)
    standard_dual = -(
        (2 * companion + 3) * (3 * companion + 1) / (companion + 3)
    )
    assert sp.cancel(standard + standard_dual) == 50
    assert sp.cancel((standard - 25) + (standard_dual - 25)) == 0


def test_symbolic_convention_separation() -> None:
    sp = pytest.importorskip("sympy")
    k = sp.Symbol("k", rational=True)
    companion = -k - 6
    standard = -(2 * k + 3) * (3 * k + 1) / (k + 3)
    standard_dual = -(
        (2 * companion + 3) * (3 * companion + 1) / (companion + 3)
    )
    shifted = 2 - 24 * (k + 1) ** 2 / (k + 3)
    shifted_dual = 2 - 24 * (companion + 1) ** 2 / (companion + 3)
    assert sp.cancel(standard + standard_dual) == 50
    assert sp.cancel(shifted + shifted_dual) == 196


def test_active_bp_chapter_records_the_primary_parity_and_open_obligation() -> None:
    source = BP_CHAPTER.read_text(encoding="utf-8")
    assert r"\cite[Eq.~\textup{(}2.2\textup{)}]{FKR20}" in source
    assert "ordinary bosonic vertex algebra" in source
    assert r"G^+_{h=3/2}^{\mathrm{even}}" in source
    assert r"G^-_{h=3/2}^{\mathrm{even}}" in source
    assert r"\ClaimStatusOpen" in source
    assert "full genus-$1$ curvature computation" in source
    assert r"\kappa(\mathcal{B}^k) \;=\; \frac{c}{6}" not in source


def test_bp_chapter_corrects_the_reverse_ope_and_theorem_ab_types() -> None:
    source = BP_CHAPTER.read_text(encoding="utf-8")
    assert "ordinary vertex-algebra skew\nsymmetry" in source
    assert r"\label{eq:bp-ope-GmGp}" not in source
    assert "A (reconstruction)" in source
    assert r"\epsilon_{\mathcal B^k}" in source
    assert "B (quadratic recognition)" in source
    assert r"q_{\mathcal B^k}" in source
    assert r"H_{\mathrm{CL}}" in source


def test_bp_t_line_rational_functions_use_the_primary_central_charge() -> None:
    source = BP_CHAPTER.read_text(encoding="utf-8")
    assert r"c=c_{\mathrm{BP}}(k)=-(2k+3)(3k+1)/(k+3)" in source
    assert (
        r"\frac{10(k+3)^2}"
        "\n"
        r"{3(2k+3)(3k+1)(10k^2+11k-17)}"
    ) in source
    assert (
        r"\frac{16(k+3)^3}"
        "\n"
        r"{(2k+3)^2(3k+1)^2(10k^2+11k-17)}"
    ) in source

    sp = pytest.importorskip("sympy")
    k = sp.Symbol("k")
    c_value = -(2 * k + 3) * (3 * k + 1) / (k + 3)
    expected_s4 = 10 * (k + 3) ** 2 / (
        3 * (2 * k + 3) * (3 * k + 1) * (10 * k**2 + 11 * k - 17)
    )
    expected_s5 = 16 * (k + 3) ** 3 / (
        (2 * k + 3) ** 2 * (3 * k + 1) ** 2 * (10 * k**2 + 11 * k - 17)
    )
    assert sp.cancel(10 / (c_value * (5 * c_value + 22)) - expected_s4) == 0
    assert sp.cancel(-48 / (c_value**2 * (5 * c_value + 22)) - expected_s5) == 0


def test_bp_chapter_uses_positive_declarative_prose() -> None:
    source = BP_CHAPTER.read_text(encoding="utf-8")
    prohibited = re.compile(
        r"\b(?:not|does\s+not|do\s+not|cannot|without|never|no|fails?|failure|"
        r"undefined|outside|excluded?)\b",
        flags=re.IGNORECASE,
    )
    assert prohibited.search(source) is None


def test_census_marks_bp_kappa_as_open() -> None:
    source = re.sub(r"\s+", " ", CENSUS.read_text(encoding="utf-8"))
    assert "BP genus-$1$ curvature computation" in source
    assert "open-genus-one-computation" in source
    assert r"standard scalar data $(K^c,\varrho,K^\kappa)=(50,1/6,25/3)$" not in source


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
