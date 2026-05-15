"""Focused tests for the W_3 Bouwknegt-Schoutens finite-OPE surface."""

import os
import sys
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

from theorem_w3_bouwknegt_schoutens_engine import (
    W3_BETA_SINGULAR_C,
    beta_w3,
    bpz_degenerate_weight,
    bpz_null_vector_ode,
    bs_w3_null_vector_level2,
    collision_depth_ode_w3,
    compare_at_c2,
    compare_at_generic_c,
    compare_bpz_equations,
    finite_ope_diagnostic_scope,
    full_comparison_summary,
    kappa_channels_w3,
    kappa_principal_w3,
    kappa_total_w3,
    lambda_zero_on_primary,
    lambda_zero_witness,
    uniform_weight_reduction_diagnostic,
    verify_depth_4_vanishing_bs,
    w3_harmonic_ratio,
    w3_kac_weight,
    w3_minimal_model_c,
    w3_rmatrix_collision_poles,
    w3_tline_shadow_data,
    w3_wline_shadow_data,
    w3_ww_ope_modes,
    w3_extra_depths_on_primaries,
)


class TestSingularSurfaces:
    def test_beta_regular_values(self):
        assert beta_w3(Fraction(2)) == Fraction(1, 2)
        assert beta_w3(Fraction(0)) == Fraction(8, 11)
        assert beta_w3(Fraction(4)) == Fraction(8, 21)

    def test_beta_rejects_bouwknegt_schoutens_pole(self):
        assert W3_BETA_SINGULAR_C == Fraction(-22, 5)
        with pytest.raises(ValueError, match="singular"):
            beta_w3(W3_BETA_SINGULAR_C)

    def test_minimal_model_can_land_on_singular_surface(self):
        assert w3_minimal_model_c(3, 5) == Fraction(-22, 5)
        with pytest.raises(ValueError, match="singular"):
            w3_ww_ope_modes(w3_minimal_model_c(3, 5))

    def test_shadow_data_rejects_c_zero_and_beta_pole(self):
        with pytest.raises(ValueError, match=r"c\(5c \+ 22\)"):
            w3_tline_shadow_data(Fraction(0))
        with pytest.raises(ValueError, match=r"c\(5c \+ 22\)"):
            w3_wline_shadow_data(Fraction(-22, 5))


class TestKappaAndUniformWeight:
    def test_w3_kappa_channels_are_separate(self):
        channels = kappa_channels_w3(Fraction(12))
        assert channels["T"] == 6
        assert channels["W"] == 4
        assert channels["principal_total"] == 10
        assert channels["weights"] == {"T": 2, "W": 3}
        assert not channels["uniform_weight"]

    def test_principal_kappa_is_harmonic_sum_not_uniform_weight(self):
        c = Fraction(6)
        assert w3_harmonic_ratio() == Fraction(5, 6)
        assert kappa_principal_w3(c) == 5
        assert kappa_total_w3(c) == 5

    def test_uniform_weight_promotion_is_rejected(self):
        diagnostic = uniform_weight_reduction_diagnostic(Fraction(6))
        assert not diagnostic["is_uniform_weight"]
        assert diagnostic["principal_scalar_trace"] == 5
        assert not diagnostic["uniform_weight_all_genus_formula_available"]
        assert not diagnostic["certifies_modular_koszul"]
        assert not diagnostic["certifies_derived_center"]
        assert not diagnostic["certifies_all_genus"]


class TestW3OPEConstants:
    def test_ww_ope_modes_at_c2(self):
        modes = w3_ww_ope_modes(Fraction(2))
        assert modes["mode_5"]["coefficient"] == Fraction(2, 3)
        assert modes["mode_4"]["coefficient"] == 0
        assert modes["mode_3"]["coefficient"] == 2
        assert modes["mode_2"]["coefficient"] == 1
        assert modes["mode_1"]["fields"]["d2T"] == Fraction(3, 10)
        assert modes["mode_1"]["fields"]["Lambda"] == Fraction(1, 2)

    def test_dlog_rmatrix_poles(self):
        poles = w3_rmatrix_collision_poles(Fraction(2))
        assert tuple(poles) == (5, 4, 3, 2, 1)
        assert poles[5]["r_pole_order"] == 5
        assert poles[4]["coefficient"] == 0
        assert poles[1]["fields"]["Lambda"] == Fraction(1, 2)

    def test_collision_depth_keeps_lambda_and_d2t_separate(self):
        data = collision_depth_ode_w3(Fraction(2), Fraction(1), 0, 0, 0)
        depth_1 = data["w_sector"]["depth_1"]
        assert depth_1["pole_0_lambda"] == Fraction(-2, 5)
        assert depth_1["pole_0_d2T"] == Fraction(9, 5)
        assert depth_1["pole_0_total_on_primary"] == Fraction(7, 5)
        assert data["w_sector"]["depth_3"]["pole_0_ww"] == 2
        assert data["w_sector"]["depth_4"]["vanishes"]
        assert data["w_sector"]["depth_5"]["pole_0"] == Fraction(2, 3)

    def test_extra_depths_use_same_finite_ope_data(self):
        result = w3_extra_depths_on_primaries(Fraction(2), Fraction(1))
        assert result["depth_1_lambda"] == Fraction(-2, 5)
        assert result["depth_1_d2T"] == Fraction(9, 5)
        assert result["depth_1_total_on_primary"] == Fraction(7, 5)
        assert result["scope"]["certifies_all_genus"] is False


class TestLambdaWitness:
    def test_lambda_zero_mode_formula_from_field_definition(self):
        witness = lambda_zero_witness(Fraction(1))
        assert witness["normal_ordered_TT_zero"] == 1
        assert witness["d2T_zero"] == 6
        assert witness["lambda_zero"] == Fraction(-4, 5)
        assert lambda_zero_on_primary(Fraction(2), Fraction(1)) == Fraction(-4, 5)

    def test_lambda_zeroes_are_h_0_and_h_9_over_5(self):
        assert lambda_zero_on_primary(Fraction(2), Fraction(0)) == 0
        assert lambda_zero_on_primary(Fraction(2), Fraction(9, 5)) == 0
        assert lambda_zero_on_primary(Fraction(2), Fraction(3, 5)) != 0


class TestMinimalAndBPZData:
    def test_minimal_model_central_charges(self):
        assert w3_minimal_model_c(3, 4) == 0
        assert w3_minimal_model_c(4, 5) == Fraction(4, 5)
        assert w3_minimal_model_c(3, 5) == Fraction(-22, 5)

    def test_kac_weight_vacuum(self):
        for p, pp in [(3, 4), (4, 5), (3, 5)]:
            assert w3_kac_weight(1, 1, p, pp) == 0

    def test_bpz_degenerate_weight_exact_square_case(self):
        weights = bpz_degenerate_weight(Fraction(1, 2))
        assert weights["exact_rational"]
        assert weights["sqrt_discriminant"] == Fraction(7, 2)
        assert weights["h_plus"] == Fraction(1, 2)
        assert weights["h_minus"] == Fraction(1, 16)

    def test_bpz_degenerate_weight_does_not_fake_sqrt(self):
        weights = bpz_degenerate_weight(Fraction(2))
        assert weights["discriminant"] == -23
        assert weights["sqrt_discriminant"] is None
        assert weights["h_plus"] is None
        assert not weights["exact_rational"]

    def test_bpz_ode_leading_coefficient(self):
        ode = bpz_null_vector_ode(Fraction(2), Fraction(1, 2), 0, 0, 0)
        assert ode["order"] == 2
        assert ode["leading_coefficient"] == Fraction(4, 3)

    def test_bpz_comparison_is_t_sector_only(self):
        result = compare_bpz_equations(
            Fraction(2), Fraction(1), Fraction(2), Fraction(3), Fraction(4)
        )
        assert result["structural_agreement"]
        assert result["sign_adjusted_cross_match"]
        assert result["t_sector_only"]
        assert not result["certifies_w3_bs_null_vector_ode"]


class TestShadowLineData:
    def test_tline_shadow_data_at_c2(self):
        data = w3_tline_shadow_data(Fraction(2))
        assert data["kappa"] == 1
        assert data["S3"] == 2
        assert data["S4"] == Fraction(5, 32)
        assert data["Delta"] == Fraction(5, 4)

    def test_wline_shadow_data_at_c2(self):
        data = w3_wline_shadow_data(Fraction(2))
        assert data["kappa"] == Fraction(2, 3)
        assert data["S3"] == 0
        assert data["S4"] == Fraction(5, 128)
        assert data["Delta"] == Fraction(5, 24)
        assert data["Q_constant"] == Fraction(16, 9)
        assert data["Q_t2_coefficient"] == Fraction(5, 12)
        assert data["odd_coefficients_vanish"]


class TestScopeAndSummary:
    def test_finite_ope_scope_has_no_theorem_promotion(self):
        scope = finite_ope_diagnostic_scope()
        assert scope["finite_ope_modes"]
        assert not scope["certifies_bs_null_vector_ode"]
        assert not scope["certifies_modular_koszul"]
        assert not scope["certifies_derived_center"]
        assert not scope["certifies_all_genus"]

    def test_generic_bs_level2_null_vector_is_not_certified(self):
        result = bs_w3_null_vector_level2(Fraction(2), Fraction(1), Fraction(1))
        assert not result["has_w_null_vector"]
        assert not result["certifies_full_bs_null_vector"]
        assert "Kac-Shapovalov" in result["required_missing_witness"]

    def test_depth_4_is_only_a_finite_ope_check(self):
        result = verify_depth_4_vanishing_bs()
        assert result["w4_w_vanishes"]
        assert result["ope_mode"] == "W_{(4)}W = 0"
        assert not result["certifies_full_bs_null_vector_ode"]

    def test_compare_helpers_return_non_certification_flags(self):
        c2 = compare_at_c2(h1=Fraction(1))
        assert c2["beta"] == Fraction(1, 2)
        assert c2["kappa_total"] == Fraction(5, 3)
        assert not c2["scope"]["certifies_all_genus"]

        generic = compare_at_generic_c(Fraction(4), Fraction(1), 0, 0, 0)
        assert generic["beta"] == Fraction(8, 21)
        assert generic["kappa_total"] == Fraction(10, 3)
        assert not generic["scope"]["certifies_modular_koszul"]

    def test_full_summary_is_finite_not_full_agreement(self):
        summary = full_comparison_summary(Fraction(2))
        assert summary["finite_ope_diagnostic_passes"]
        assert not summary["overall_agreement"]
        assert summary["kappa_total"] == Fraction(5, 3)
        assert summary["wline_shadow"]["S4"] == Fraction(5, 128)
        assert not summary["scope"]["certifies_derived_center"]
        assert "Kac-Shapovalov" in summary["remaining_obligation"]
