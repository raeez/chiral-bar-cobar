"""Exact finite-W3 checks and comparison-boundary tests."""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.theorem_w3_bouwknegt_schoutens_engine import (
    OpenW3ComparisonError,
    W3_BETA_SINGULAR_C,
    beta_w3,
    bpz_degenerate_weight,
    bpz_null_vector_ode,
    bs_w3_null_vector_level2,
    collision_depth_ode_w3,
    compare_at_c2,
    finite_ope_diagnostic_scope,
    full_comparison_summary,
    kappa_channels_w3,
    lambda_zero_on_primary,
    lambda_zero_witness,
    leading_norm_channels_w3,
    level_one_null_status,
    reciprocal_weight_diagnostic_w3,
    uniform_weight_reduction_diagnostic,
    verify_depth_4_vanishing_bs,
    w3_harmonic_ratio,
    w3_kac_weight,
    w3_level_one_null_curve,
    w3_minimal_model_c,
    w3_mode_lambda_coefficient,
    w3_rmatrix_collision_poles,
    w3_tline_shadow_data,
    w3_ww_ope_modes,
    w3_wline_shadow_data,
)


def test_32_16_ope_and_mode_normalizations():
    c = sp.Symbol("c")
    modes = w3_ww_ope_modes(c)
    assert sp.simplify(modes["mode_1"]["fields"]["Lambda"] - 32 / (22 + 5 * c)) == 0
    assert sp.simplify(modes["mode_0"]["fields"]["dLambda"] - 16 / (22 + 5 * c)) == 0
    m, n = sp.symbols("m n")
    expected = 16 * (m - n) / (22 + 5 * c)
    assert sp.simplify(w3_mode_lambda_coefficient(m, n, c) - expected) == 0


def test_bouwknegt_schoutens_singular_surface():
    assert W3_BETA_SINGULAR_C == Fraction(-22, 5)
    assert beta_w3(Fraction(2)) == 1
    with pytest.raises(ValueError):
        beta_w3(W3_BETA_SINGULAR_C)


def test_leading_norms_and_reciprocal_weights_have_distinct_types():
    c = sp.Symbol("c")
    norms = leading_norm_channels_w3(c)
    assert norms["T"] == c / 2
    assert norms["W"] == c / 3
    assert norms["ratio"] == sp.Rational(2, 3)
    assert reciprocal_weight_diagnostic_w3() == sp.Rational(5, 6)
    assert w3_harmonic_ratio() == sp.Rational(5, 6)
    kappa = kappa_channels_w3(c)
    assert kappa["status"] == "conditional"
    assert kappa["T"].value == c / 2
    assert kappa["W"].value == c / 3
    assert kappa["total"].value == 5 * c / 6


def test_lambda_zero_mode_includes_normal_ordering_contribution():
    h = sp.Symbol("h")
    witness = lambda_zero_witness(h)
    assert witness["normal_ordered_TT_zero"] == h**2 + 2 * h
    assert witness["d2T_zero"] == 6 * h
    assert sp.factor(witness["lambda_zero"] - (h**2 + h / 5)) == 0
    assert sp.factor(lambda_zero_on_primary(sp.Symbol("c"), h) - (h**2 + h / 5)) == 0


def test_level_one_null_curve():
    c, h, w = sp.symbols("c h w")
    expected = 9 * w**2 * (22 + 5 * c) - 2 * h**2 * (32 * h + 2 - c)
    assert sp.expand(w3_level_one_null_curve(c, h, w) - expected) == 0
    point = level_one_null_status(2, 0, 0)
    assert point["is_on_curve"]


def test_minimal_model_and_t_sector_arithmetic():
    assert w3_minimal_model_c(4, 5) == sp.Rational(4, 5)
    assert w3_kac_weight(1, 1, 4, 5) == 0
    roots = bpz_degenerate_weight(Fraction(1))
    assert roots["h_plus"] == roots["h_minus"] == Fraction(1, 4)
    packet = bpz_null_vector_ode(1, Fraction(1, 4), 0, 0, 0)
    assert packet.status == "conditional"


@pytest.mark.parametrize(
    "packet",
    [
        w3_rmatrix_collision_poles(2),
        collision_depth_ode_w3(2, 0, 0, 0, 0),
        w3_tline_shadow_data(2),
        w3_wline_shadow_data(2),
        bs_w3_null_vector_level2(2, 0, 0),
    ],
)
def test_collision_shadow_and_null_vector_promotions_are_open(packet):
    assert packet.status == "open"


def test_uniform_weight_and_scope_packets():
    diagnostic = uniform_weight_reduction_diagnostic(2)
    assert diagnostic["weights"] == (2, 3)
    assert diagnostic["scalar_modular_reduction"].status == "conditional"
    assert diagnostic["scalar_modular_reduction"].value == sp.Rational(5, 3)
    assert diagnostic["all_genus_reduction"].status == "open"
    scope = finite_ope_diagnostic_scope()
    assert scope["finite_ope_modes"] == "exact"
    assert scope["ordered_bar"].status == "open"
    assert scope["scalar_shadow"].status == "open"


def test_fifth_order_pole_absence_has_only_typed_collision_consequence():
    packet = verify_depth_4_vanishing_bs()
    assert packet["W_(4)W"] == 0
    assert packet["collision_consequence"].status == "open"


def test_summary_and_comparison_helpers_preserve_scope():
    comparison = compare_at_c2()
    assert comparison["collision"].status == "open"
    assert comparison["bpz"].status == "open"
    assert comparison["shadow"].status == "open"
    summary = full_comparison_summary(Fraction(2))
    assert summary["status"] == "finite OPE and determinant arithmetic exact; comparison theorems open"
