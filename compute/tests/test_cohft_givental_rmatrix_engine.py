from fractions import Fraction

from sympy import Rational, Symbol, bernoulli, exp, factorial, series, sin

from compute.lib.cohft_dr_hierarchy_engine import wk_intersection as wk_dr
from compute.lib.cohft_givental_rmatrix_engine import (
    cohft_axiom_analysis,
    givental_Fg_from_wk,
    hodge_r_coefficients,
    koszul_dual_rmatrix,
    r_matrix_comparison,
    scalar_genus_free_energy,
    string_defect,
    symplecticity_check,
    wk_intersection,
)
from compute.lib.shadow_cohft_tautological import wk_intersection as wk_shadow


def _to_rational(value):
    if isinstance(value, Fraction):
        return Rational(value.numerator, value.denominator)
    return Rational(value)


def _hodge_r_oracle(max_order):
    z = Symbol("z")
    exponent = sum(
        Rational(bernoulli(2 * j), 2 * j * (2 * j - 1)) * z ** (2 * j - 1)
        for j in range(1, max_order + 2)
        if 2 * j - 1 <= max_order
    )
    expanded = series(exp(exponent), z, 0, max_order + 1).removeO().expand()
    return [Rational(expanded.coeff(z, i)) for i in range(max_order + 1)]


def test_wk_dilaton_uses_remaining_markings_and_matches_local_oracles():
    cases = [
        (1, (1,), Rational(1, 24)),
        (1, (1, 1), Rational(1, 24)),
        (1, (1, 1, 1), Rational(1, 12)),
        (2, (4,), Rational(1, 1152)),
        (2, (4, 1), Rational(1, 384)),
        (2, (4, 1, 1), Rational(1, 96)),
        (2, (3, 2), Rational(29, 5760)),
        (2, (5, 0), Rational(1, 1152)),
    ]

    for g, insertions, expected in cases:
        assert wk_intersection(g, insertions) == expected
        assert _to_rational(wk_shadow(g, insertions)) == expected
        assert _to_rational(wk_dr(g, insertions)) == expected


def test_universal_hodge_r_coefficients_match_exponential_oracle():
    assert hodge_r_coefficients(5) == _hodge_r_oracle(5)
    assert hodge_r_coefficients(3) == [
        Rational(1),
        Rational(1, 12),
        Rational(1, 288),
        Rational(-139, 51840),
    ]


def test_hodge_lambda_constants_match_ahat_generating_function_lane():
    x = Symbol("x")
    ahat_ix = series((x / 2) / sin(x / 2) - 1, x, 0, 8).removeO().expand()
    for g, expected in [
        (1, Rational(1, 24)),
        (2, Rational(7, 5760)),
        (3, Rational(31, 967680)),
    ]:
        direct = (
            (2 ** (2 * g - 1) - 1)
            * abs(bernoulli(2 * g))
            / (2 ** (2 * g - 1) * factorial(2 * g))
        )
        assert Rational(direct) == expected
        assert Rational(ahat_ix.coeff(x, 2 * g)) == expected


def test_string_defect_separates_rank_one_defect_from_flat_unit():
    heisenberg = string_defect("heisenberg")
    heisenberg_with_vacuum = string_defect("heisenberg", vacuum_in_V=True)
    virasoro = string_defect("virasoro", c=Fraction(26))

    assert heisenberg["formal_rank_one_unit_fixed"] is True
    assert heisenberg["has_flat_unit"] is False
    assert heisenberg["vacuum_in_V"] is False
    assert heisenberg["obstruction_order"] is None

    assert heisenberg_with_vacuum["has_flat_unit"] is True
    assert virasoro["formal_rank_one_unit_fixed"] is False
    assert virasoro["has_flat_unit"] is False
    assert virasoro["obstruction_order"] == 1


def test_axiom_analysis_and_teleman_are_not_certified_by_r_defect_alone():
    analysis = cohft_axiom_analysis("heisenberg")
    analysis_with_vacuum = cohft_axiom_analysis("heisenberg", vacuum_in_V=True)

    assert analysis["axioms"]["CohFT-3 (flat identity)"]["holds"] is False
    assert analysis["teleman_applicable"] is False
    assert analysis["string_defect"]["formal_rank_one_unit_fixed"] is True
    assert analysis["axioms"]["CohFT-3' (modified string)"]["holds"] is None

    assert analysis_with_vacuum["axioms"]["CohFT-3 (flat identity)"]["holds"] is True
    assert analysis_with_vacuum["teleman_applicable"] is True


def test_symplecticity_reports_finite_window_and_catches_complementarity_failure():
    R = hodge_r_coefficients(8)
    check = symplecticity_check(R, 8)
    comparison = r_matrix_comparison("virasoro", 6, c=Rational(26))

    assert check["is_symplectic_to_order"] is True
    assert check["finite_window_only"] is True
    assert check["checked_order"] == 8

    assert comparison["comp_is_symplectic"] is False
    assert comparison["comp_symplecticity"]["first_defect_order"] == 2
    assert comparison["symp_is_symplectic"] is True
    assert comparison["symp_symplecticity"]["finite_window_only"] is True


def test_scalar_genus_lane_is_explicitly_not_full_graph_sum():
    R = hodge_r_coefficients(5)
    unrelated_R = [Rational(1), Rational(99), Rational(-7)]

    assert scalar_genus_free_energy(Rational(3), 2) == Rational(7, 1920)
    assert givental_Fg_from_wk(Rational(3), R, 2) == Rational(7, 1920)
    assert givental_Fg_from_wk(Rational(3), unrelated_R, 2) == Rational(7, 1920)


def test_virasoro_dual_branch_keeps_firewalls_and_fractional_c_dual_exact():
    self_dual = koszul_dual_rmatrix(13, 4)
    fractional = koszul_dual_rmatrix(Rational(3, 2), 2)

    assert self_dual["R_equal_at_self_dual"] is True
    assert fractional["c_dual"] == Rational(49, 2)
    assert fractional["not_bar_cobar_inversion"] is True
    assert fractional["not_hochschild_bulk_center"] is True
    assert "Verdier" in fractional["branch"]
