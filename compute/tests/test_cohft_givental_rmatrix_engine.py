from fractions import Fraction

from sympy import Rational

from compute.lib.cohft_givental_rmatrix_engine import (
    cohft_axiom_analysis,
    givental_Fg_from_wk,
    hodge_r_coefficients,
    string_defect,
    symplecticity_check,
)


def test_universal_hodge_r_coefficients_start_correctly():
    assert hodge_r_coefficients(3) == [
        Rational(1),
        Rational(1, 12),
        Rational(1, 288),
        Rational(-139, 51840),
    ]


def test_heisenberg_and_virasoro_string_defects_split_flat_unit_behavior():
    heisenberg = string_defect("heisenberg")
    virasoro = string_defect("virasoro", c=Fraction(26))

    assert heisenberg["has_flat_unit"] is True
    assert heisenberg["obstruction_order"] is None
    assert virasoro["has_flat_unit"] is False
    assert virasoro["obstruction_order"] == 1


def test_axiom_analysis_and_symplecticity():
    R = hodge_r_coefficients(5)
    analysis = cohft_axiom_analysis("heisenberg")

    assert analysis["axioms"]["CohFT-3 (flat identity)"]["holds"] is True
    assert symplecticity_check(R)["is_symplectic"] is True
    assert givental_Fg_from_wk(Rational(3), R, 2) == Rational(7, 1920)
