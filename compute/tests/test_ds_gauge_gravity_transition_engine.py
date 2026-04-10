"""Tests for the DS gauge/gravity transition engine."""

from fractions import Fraction

from sympy import Rational as SympyRational
from sympy import simplify

from compute.lib.ds_gauge_gravity_transition_engine import (
    CRITICAL_LEVEL,
    DEFAULT_LEVELS,
    affine_sl2_kappa,
    critical_level_transition,
    ds_sl2_virasoro_c,
    ds_transition_at_level,
    shadow_discriminant,
    transition_table,
    virasoro_kappa,
    virasoro_s4,
)
from compute.lib.lie_algebra import virasoro_ds_c
from compute.lib.theorem_genus2_planted_forest_gz26_engine import (
    affine_sl2_shadow,
    virasoro_shadow,
)
from compute.lib.virasoro_shadow_tower import c as vir_c_symbol
from compute.lib.virasoro_shadow_tower import shadow_coefficients


def _to_sympy_rational(value: Fraction) -> SympyRational:
    return SympyRational(value.numerator, value.denominator)


def test_requested_levels_are_covered():
    transitions = transition_table()
    assert [entry.level for entry in transitions] == list(DEFAULT_LEVELS)


def test_affine_sl2_spot_check_at_k1():
    transition = ds_transition_at_level(Fraction(1))
    pre = transition.pre_ds

    # VERIFIED: [DC] dim(sl_2)=3 and h^v=2 give kappa=3(1+2)/4=9/4; [CF] theorem_genus2_planted_forest_gz26_engine.affine_sl2_shadow uses the same sl_2 Sugawara/T-line formula.
    assert pre.kappa == Fraction(9, 4)
    assert pre.S_2 == Fraction(9, 4)
    # VERIFIED: [DC] S_3=4/(k+2) gives 4/3 at k=1; [CF] linf_bracket_engine and theorem_genus2_planted_forest_gz26_engine both record the same sl_2 cubic normalization.
    assert pre.S_3 == Fraction(4, 3)
    # VERIFIED: [DC] class L forces S_4=0 and hence Delta=8*kappa*S_4=0; [CF] ds_shadow_cascade_engine and theorem_genus2_planted_forest_gz26_engine both mark affine sl_2 as depth 3 with vanishing quartic.
    assert pre.S_4 == Fraction(0)
    assert pre.Delta == Fraction(0)
    # VERIFIED: [DC] Sugawara gives c_aff=3k/(k+2)=1 at k=1; [CF] lie_algebra.sugawara_c and the sl_2 compute surfaces in Vol I/II use the same value.
    assert pre.central_charge == Fraction(1)
    assert pre.shadow_class == "L"
    assert pre.finite_tower is True


def test_post_ds_spot_check_at_k1():
    transition = ds_transition_at_level(Fraction(1))
    post = transition.post_ds

    # VERIFIED: [DC] c_DS=1-6(k+1)^2/(k+2) gives -7 at k=1; [CF] lie_algebra.virasoro_ds_c and wn_central_charge_canonical agree on the same DS value.
    assert post.central_charge == Fraction(-7)
    # VERIFIED: [DC] kappa(Vir_c)=c/2 gives -7/2 at c=-7; [CF] theorem_genus2_planted_forest_gz26_engine.virasoro_shadow uses the same Virasoro kappa formula.
    assert post.kappa == Fraction(-7, 2)
    assert post.S_2 == Fraction(-7, 2)
    # VERIFIED: [DC] the Virasoro cubic is the universal value 2; [CF] virasoro_shadow_tower and theorem_genus2_planted_forest_gz26_engine both use S_3=2.
    assert post.S_3 == Fraction(2)
    # VERIFIED: [DC] S_4=10/[c(5c+22)] gives 10/[(-7)(-13)]=10/91; [CF] virasoro_shadow_tower and theorem_genus2_planted_forest_gz26_engine both encode the same quartic.
    assert post.S_4 == Fraction(10, 91)
    # VERIFIED: [DC] Delta=8*(c/2)*S_4 gives -40/13 at c=-7; [LC] Delta=40/(5c+22) gives the same value because 5(-7)+22=-13.
    assert post.Delta == Fraction(-40, 13)
    assert post.shadow_class == "M"
    assert post.finite_tower is False


def test_c_and_kappa_transform_correctly_under_ds():
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        direct_c = Fraction(1) - Fraction(6) * (level + 1) ** 2 / (level + 2)
        sympy_c = virasoro_ds_c(level)
        assert transition.pre_ds.central_charge == Fraction(3) * level / (level + 2)
        assert transition.pre_ds.kappa == Fraction(3) * (level + 2) / 4
        assert transition.post_ds.central_charge == direct_c
        assert transition.post_ds.central_charge == Fraction(int(sympy_c.p), int(sympy_c.q))
        assert transition.post_ds.kappa == direct_c / 2
        assert transition.post_ds.kappa == virasoro_kappa(direct_c)
        assert transition.pre_ds.kappa != transition.post_ds.kappa


def test_affine_cubic_normalization_matches_existing_sl2_engine():
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        expected = affine_sl2_shadow(level)["S_3"]
        assert transition.pre_ds.S_3 == expected


def test_virasoro_quartic_matches_existing_engines():
    vir_tower = shadow_coefficients(4)
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        c_val = transition.post_ds.central_charge
        expected_fraction = virasoro_shadow(c_val)["S_4"]
        expected_sympy = simplify(
            vir_tower[4].subs(vir_c_symbol, _to_sympy_rational(c_val))
        )
        assert transition.post_ds.S_4 == expected_fraction
        assert simplify(expected_sympy - _to_sympy_rational(transition.post_ds.S_4)) == 0


def test_delta_transition_is_visible_on_requested_levels():
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        assert transition.class_transition == ("L", "M")
        assert transition.quartic_created is True
        assert transition.pre_ds.Delta == 0
        assert transition.post_ds.Delta != 0
        assert transition.delta_jump == transition.post_ds.Delta


def test_delta_is_linear_in_kappa_before_and_after_ds():
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        assert transition.pre_ds.Delta == shadow_discriminant(
            transition.pre_ds.kappa,
            transition.pre_ds.S_4,
        )
        assert transition.post_ds.Delta == shadow_discriminant(
            transition.post_ds.kappa,
            transition.post_ds.S_4,
        )
        assert transition.post_ds.Delta == Fraction(40) / (
            5 * transition.post_ds.central_charge + 22
        )


def test_critical_level_degeneration_is_recorded():
    transition = critical_level_transition()
    pre = transition.pre_ds
    post = transition.post_ds

    # VERIFIED: [DC] kappa=3(k+2)/4 vanishes at k=-2; [LC] class-L S_4=0 forces Delta=0 even at the degenerate level.
    assert pre.kappa == Fraction(0)
    assert pre.S_2 == Fraction(0)
    assert pre.S_4 == Fraction(0)
    assert pre.Delta == Fraction(0)
    assert pre.S_3 is None
    assert pre.central_charge is None
    assert pre.singular_reason is not None

    assert post.central_charge is None
    assert post.kappa is None
    assert post.S_2 is None
    assert post.S_3 is None
    assert post.S_4 is None
    assert post.Delta is None
    assert post.shadow_class == "critical"
    assert post.singular_reason is not None
    assert transition.level == CRITICAL_LEVEL


def test_engine_helpers_match_formula_surface():
    for level in DEFAULT_LEVELS:
        transition = ds_transition_at_level(level)
        c_val = ds_sl2_virasoro_c(level)
        assert transition.pre_ds.kappa == affine_sl2_kappa(level)
        assert transition.post_ds.central_charge == c_val
        assert transition.post_ds.S_4 == virasoro_s4(c_val)
