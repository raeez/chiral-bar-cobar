r"""Tests for finite scalar and stationary shadow diagnostics."""

import math

import pytest
from sympy import I, Rational, simplify, pi

from compute.lib.shadow_hierarchy_engine import (
    LOCAL_SOURCES,
    OBJECT_FIREWALLS,
    STANDARD_KAPPAS,
    STANDARD_KERNELS,
    VIRASORO_SHADOW_COEFFICIENTS,
    _LAMBDA_FP_KNOWN,
    dispersionless_shadow_hierarchy,
    finite_scalar_tau_identity,
    hirota_bilinear_kappa_deformation,
    kappa_deformed_kdv_equation,
    kdv_obstruction_explicit,
    kdv_residual_from_power,
    lambda_fp,
    mc_as_pde_system,
    mc_is_hierarchy,
    shadow_free_energy_genus,
    shadow_hierarchy_landscape,
    shadow_hierarchy_main_theorem,
    shadow_instanton_action_numerical,
    shadow_instanton_structure,
    stationary_riccati_diagnostics,
    toda_from_multichannel_shadow,
    verify_kdv_failure_genus2,
    verify_virasoro_on_shadow_tau,
    virasoro_operator_kappa,
    wn_kappa_deformed_gelfand_dickey,
)


class TestLocalConstants:
    def test_sources_are_local(self):
        assert LOCAL_SOURCES["finite_scalar_tau"].endswith(":20304")
        assert LOCAL_SOURCES["stationary_hierarchy_shadow"].endswith(":20234")
        assert LOCAL_SOURCES["kernel_normalizations"].endswith(":165")

    def test_object_firewalls_are_explicit(self):
        assert OBJECT_FIREWALLS["B(A)"] != OBJECT_FIREWALLS["A^!"]
        assert "Hochschild" in OBJECT_FIREWALLS["Z_ch^der(A)"]
        assert "not Koszul duality" in OBJECT_FIREWALLS["Omega(B(A))"]

    def test_kernel_normalizations_are_not_conflated(self):
        assert STANDARD_KERNELS["Heisenberg_collision"] == "k/z"
        assert STANDARD_KERNELS["affine_collision_trace_form"] == "k*Omega_tr/z"
        assert STANDARD_KERNELS["affine_KZ"] == "Omega/((k+h^vee)*z)"
        assert STANDARD_KERNELS["Virasoro_collision"] == "(c/2)/z^3 + 2*T/z"
        assert STANDARD_KERNELS["affine_collision_trace_form"] != STANDARD_KERNELS["affine_KZ"]

    def test_standard_kappas_match_census_surface(self):
        assert STANDARD_KAPPAS["Heisenberg_rank_1_level_k"] == "k"
        assert STANDARD_KAPPAS["affine_V_k_g"] == "dim(g)*(k+h^vee)/(2*h^vee)"
        assert STANDARD_KAPPAS["Virasoro_c"] == "c/2"
        assert STANDARD_KAPPAS["W_N"] == "c*(H_N-1)"
        assert STANDARD_KAPPAS["beta_gamma_lambda"] == "6*lambda^2 - 6*lambda + 1"

    def test_virasoro_shadow_coefficients_match_census_surface(self):
        assert VIRASORO_SHADOW_COEFFICIENTS["S_2"] == "c/2"
        assert VIRASORO_SHADOW_COEFFICIENTS["S_3"] == "2"
        assert VIRASORO_SHADOW_COEFFICIENTS["S_4"] == "10/(c*(5*c+22))"
        assert VIRASORO_SHADOW_COEFFICIENTS["S_5"] == "-48/(c^2*(5*c+22))"
        assert VIRASORO_SHADOW_COEFFICIENTS["Delta"] == "40/(5*c+22)"


class TestFaberPandharipande:
    def test_known_values(self):
        for g, expected in _LAMBDA_FP_KNOWN.items():
            assert lambda_fp(g) == expected

    def test_invalid_genus_rejected(self):
        with pytest.raises(ValueError):
            lambda_fp(0)

    def test_all_positive(self):
        for g in range(1, 11):
            assert lambda_fp(g) > 0

    def test_ratio_converges_to_inverse_action(self):
        target = 1.0 / (2 * math.pi) ** 2
        for g in range(6, 14):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            assert abs(ratio - target) / target < 0.02


class TestFiniteScalarWindow:
    def test_shadow_free_energy_is_linear_scalar_projection(self):
        assert shadow_free_energy_genus(Rational(5, 2), 2) == Rational(5, 2) * Rational(7, 5760)

    def test_tau_identity_is_finite_window_only(self):
        result = finite_scalar_tau_identity(Rational(3), g_max=3)
        assert result["surface"] == "finite-window scalar coefficient identity"
        assert result["constructs_descendant_hierarchy"] is False
        assert result["coefficients"][2]["F_g_shadow_scalar"] == Rational(21, 5760)

    def test_multi_genus_coefficients_match_lambda_table(self):
        result = finite_scalar_tau_identity(Rational(7), g_max=5)
        for g in range(1, 6):
            assert result["coefficients"][g]["F_g_shadow_scalar"] == 7 * lambda_fp(g)


class TestScalarKdVObstruction:
    def test_obstruction_vanishes_at_scalar_trivial_and_kw_points(self):
        for k in [Rational(0), Rational(1)]:
            result = kdv_residual_from_power(k)
            assert result["obstruction_value"] == 0
            assert result["vanishes"] is True

    def test_obstruction_uses_manuscript_orientation(self):
        assert kdv_residual_from_power(Rational(1, 2))["obstruction_value"] == Rational(1, 4)
        assert kdv_residual_from_power(Rational(13))["obstruction_value"] == Rational(-156)

    def test_standard_kdv_residual_has_opposite_orientation(self):
        result = kdv_residual_from_power(Rational(3))
        assert result["obstruction_value"] == Rational(-6)
        assert result["standard_kdv_residual_factor"] == Rational(6)

    def test_obstruction_formula_for_sample_values(self):
        for k in [Rational(1, 3), Rational(3, 4), Rational(5), Rational(-1)]:
            assert kdv_residual_from_power(k)["obstruction_value"] == k * (1 - k)

    def test_genus2_scalar_mismatch(self):
        result = verify_kdv_failure_genus2(Rational(3))
        assert result["residual_is_zero"] is False
        assert result["quadratic_residual"] == Rational(-6, 576)
        assert result["standard_orientation_residual"] == Rational(6, 576)

    def test_genus2_scalar_mismatch_vanishes_at_kw_point(self):
        assert verify_kdv_failure_genus2(Rational(1))["residual_is_zero"] is True

    def test_explicit_obstruction_is_diagnostic_only(self):
        result = kdv_obstruction_explicit(Rational(2), max_genus=4)
        assert result["constructs_kdv_hierarchy"] is False
        assert result["details"][2]["scalar_window_mismatch"] == Rational(-1, 288)


class TestConditionalKdVAndHirota:
    def test_rescaled_kdv_requires_supplied_descendant_field(self):
        result = kappa_deformed_kdv_equation(Rational(2))
        assert result["constructs_kdv_hierarchy"] is False
        assert result["requires_descendant_cohft"] is True
        assert "u_t + (6/2)*u*u_x" in result["rescaled_equation_if_kdv_field_is_supplied"]

    def test_hirota_obstruction_factor(self):
        for k in [Rational(1, 2), Rational(3), Rational(-1)]:
            result = hirota_bilinear_kappa_deformation(k)
            assert result["hirota_D4_correction"] == k * (k - 1)
            assert result["constructs_hirota_hierarchy"] is False

    def test_hirota_obstruction_vanishes_at_zero_and_one(self):
        for k in [Rational(0), Rational(1)]:
            result = hirota_bilinear_kappa_deformation(k)
            assert result["hirota_D4_correction"] == 0
            assert result["vanishes_at_kappa_1"] is True


class TestMCAndVirasoroScope:
    def test_mc_surface_separates_scalar_stationary_and_descendant(self):
        result = mc_as_pde_system(Rational(1))
        assert "stationary_primary_line" in result["surfaces"]
        assert "finite_scalar_window" in result["surfaces"]
        assert "descendant_cohft" in result["surfaces"]
        assert result["kdv_flows"]["constructed_by_engine"] is False

    def test_virasoro_entries_require_descendant_cohft(self):
        result = mc_as_pde_system(Rational(1), max_arity=5)
        for entry in result["virasoro_constraints"].values():
            assert entry["requires_descendant_cohft"] is True
            assert entry["scalar_engine_constructs"] is False

    def test_string_equation_scope(self):
        result = virasoro_operator_kappa(-1, Rational(3))
        assert result["name"] == "string equation"
        assert result["requires_descendant_cohft"] is True
        assert result["constructed_from_scalar_tau_power"] is False
        assert "(3/2)*t_0^2" in result["kappa_deformed"]

    def test_dilaton_scalar_constant(self):
        result = virasoro_operator_kappa(0, Rational(5))
        assert result["name"] == "dilaton equation"
        assert "5/24" in result["kappa_deformed"]

    def test_higher_virasoro_scope(self):
        result = virasoro_operator_kappa(2, Rational(3))
        assert "not inferred" in result["kappa_deformed"]

    def test_scalar_a_hat_check_is_not_virasoro_construction(self):
        result = verify_virasoro_on_shadow_tau(Rational(13), max_genus=5)
        assert result["all_match"] is True
        assert result["dilaton_check"]["match"] is True
        assert result["constructs_virasoro_constraints"] is False

    def test_mc_summary_lists_negative_firewalls(self):
        result = mc_is_hierarchy()
        joined = " ".join(result["negative_results"])
        assert "scalar anomaly kappa*(1-kappa)" in joined
        assert "Gelfand-Dickey flows require descendant CohFT data" in joined
        assert "Toda lattice equations require coupled descendant data" in joined
        assert "Painleve descendants require a separate isomonodromic system" in joined


class TestStationaryDiagnostics:
    def test_riccati_metric_coefficients(self):
        result = stationary_riccati_diagnostics(Rational(2), Rational(3), Rational(5))
        q = result["Q_L"]
        assert q["constant"] == 16
        assert q["linear"] == 72
        assert q["Delta"] == 80
        assert q["quadratic"] == 9 * 9 + 2 * 80
        assert result["constructs_descendant_hierarchy"] is False

    def test_dispersionless_surface_is_scalar_scaling_only(self):
        result = dispersionless_shadow_hierarchy(Rational(10))
        for g in range(1, 6):
            assert result["genus_scaling"][g]["kappa_power_under_hbar2_equals_1_over_kappa"] == 1 - g
        assert result["dispersionless_equation"]["constructed_by_engine"] is False

    def test_wn_gelfand_dickey_is_stationary_shadow_only(self):
        result = wn_kappa_deformed_gelfand_dickey(3)
        assert result["rank"] == 2
        assert result["hierarchy"]["constructed_by_engine"] is False
        assert result["hierarchy"]["name"] == "stationary GD_3 shadow"
        assert "D^3" in result["lax_operator"]

    def test_wn_rejects_invalid_rank(self):
        with pytest.raises(ValueError):
            wn_kappa_deformed_gelfand_dickey(1)

    def test_toda_requires_separate_lax_input(self):
        result = toda_from_multichannel_shadow({"channels": ["T", "W", "V"]})
        assert result["N"] == 3
        assert result["toda_equations"]["constructed_by_engine"] is False
        assert len(result["toda_equations"]["template_if_lax_system_supplied"]) == 3
        assert result["hierarchy_type"]["constructed_by_engine"] is False


class TestLandscape:
    def test_every_family_has_depth_and_no_descendant_construction(self):
        landscape = shadow_hierarchy_landscape()
        for data in landscape.values():
            assert "depth_class" in data
            assert data["constructs_descendant_hierarchy"] is False

    def test_family_kappas_are_exact_strings(self):
        landscape = shadow_hierarchy_landscape()
        assert landscape["Heisenberg_k"]["kappa"] == "k"
        assert landscape["affine_sl2_k"]["kappa"] == "3*(k+2)/4"
        assert landscape["affine_slN_k"]["kappa"] == "(N^2-1)*(k+N)/(2*N)"
        assert landscape["Virasoro_c"]["kappa"] == "c/2"
        assert landscape["W3_c"]["kappa"] == "5*c/6"
        assert landscape["WN_c"]["kappa"] == "c*(H_N-1)"
        assert landscape["beta_gamma_lambda"]["kappa"] == "6*lambda^2 - 6*lambda + 1"

    def test_kernel_entries_are_carried_into_landscape(self):
        landscape = shadow_hierarchy_landscape()
        assert landscape["Heisenberg_k"]["kernel"] == "k/z"
        assert landscape["affine_sl2_k"]["kernel"] == "k*Omega_tr/z"
        assert landscape["affine_sl2_k"]["kz_kernel"] == "Omega/((k+h^vee)*z)"
        assert landscape["Virasoro_c"]["kernel"] == "(c/2)/z^3 + 2*T/z"

    def test_stationary_shadow_labels_do_not_claim_full_flows(self):
        landscape = shadow_hierarchy_landscape()
        assert "stationary" in landscape["Virasoro_c"]["stationary_shadow"]
        assert "descendant_hierarchy_if_supplied" in landscape["Virasoro_c"]


class TestResurgence:
    def test_scalar_instanton_action_and_stokes_multiplier(self):
        result = shadow_instanton_structure(Rational(3))
        assert simplify(result["instanton_action"]["A_symbolic"] - 4 * pi**2) == 0
        assert simplify(result["stokes_constant"]["S_1_symbolic"] + 12 * pi**2 * I) == 0
        assert "linear" in result["stokes_constant"]["kappa_scaling"]

    def test_painleve_firewall(self):
        result = shadow_instanton_structure(Rational(1))
        assert result["painleve"]["single_channel_constructed_from_scalar_tau"] is False
        assert "Painleve VI" in result["painleve"]["multi_channel_if_isomonodromic_system_supplied"]

    def test_trans_series_entries_are_scalar_large_order_only(self):
        result = shadow_instanton_structure(Rational(1), max_instanton=3)
        assert len(result["trans_series"]) == 3
        for entry in result["trans_series"].values():
            assert entry["scalar_large_order_only"] is True

    def test_instanton_action_numerical(self):
        result = shadow_instanton_action_numerical(1.0, max_g=15)
        A_exact = (2 * math.pi) ** 2
        last_g = max(result["A_estimates"].keys())
        A_est = result["A_estimates"][last_g]
        assert abs(A_est - A_exact) / A_exact < 0.005

    def test_instanton_action_kappa_independence(self):
        r1 = shadow_instanton_action_numerical(1.0, max_g=10)
        r2 = shadow_instanton_action_numerical(3.0, max_g=10)
        assert r1["A_exact"] == r2["A_exact"]


class TestMainSurface:
    def test_main_surface_has_three_way_split(self):
        result = shadow_hierarchy_main_theorem()
        statements = " ".join(result["statements"].values())
        assert "finite scalar tau identity" in statements
        assert "stationary primary-line Riccati" in statements
        assert "descendant CohFT hierarchy requires separate input" in statements

    def test_main_surface_key_formulas(self):
        result = shadow_hierarchy_main_theorem()
        formulas = result["key_formula"]
        assert formulas["obstruction"] == "kappa*(1-kappa)"
        assert formulas["instanton_action_scalar"] == "A=(2*pi)^2"
        assert "H(t)^2" in formulas["riccati"]

    def test_main_surface_preserves_firewalls(self):
        result = shadow_hierarchy_main_theorem()
        assert result["firewalls"]["objects"]["A^!"].startswith("Verdier")
        assert result["firewalls"]["kernels"]["affine_collision_trace_form"] == "k*Omega_tr/z"

    def test_classification_is_stationary(self):
        result = shadow_hierarchy_main_theorem()
        for cls in ["G", "L", "C", "M"]:
            assert "stationary" in result["classification"][cls]
