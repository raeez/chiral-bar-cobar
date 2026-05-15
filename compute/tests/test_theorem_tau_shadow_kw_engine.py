"""Exact tests for the finite tau-shadow / KW scalar-window engine."""

from fractions import Fraction

import pytest

from compute.lib.theorem_tau_shadow_kw_engine import (
    HOLOGRAPHIC_PACKAGE_ENTRIES,
    MODULAR_KOSZUL_COMPUTE_PROJECTIONS,
    _bernoulli_number,
    ahat_log_coefficient,
    ahat_log_coefficients,
    complementarity_tau_functions,
    convergence_radius_shadow,
    formal_log_from_unit_series,
    formal_tau_power_window,
    fp_window,
    free_energy_virasoro_constraints,
    genus1_universality,
    kappa_one_recovers_kw,
    kappa_w3,
    kappa_zero_degenerate_case,
    kdv_compatibility_check,
    kdv_hirota_residual_certificate,
    kernel_constant_certificate,
    lambda_fp,
    multi_weight_failure_genus2_w3,
    scalar_lane_certificate,
    scalar_projection_firewall,
    scalar_shadow_window,
    shadow_free_energy,
    standard_family_verification_table,
    structural_firewall_summary,
    tau_kw_coefficients,
    tau_shadow_coefficients,
    typed_object_firewall,
    virasoro_constraint_scope,
    w3_cross_channel_witness,
    w3_cross_correction_decomposition_genus2,
    w3_delta_cross,
    w3_free_energy_window,
    w3_large_c_cross_to_scalar_ratio,
)


def _anchored_w3_cross(g: int, c: Fraction) -> Fraction:
    """Independent Horner oracle from genus_expansions.tex constants."""

    c = Fraction(c)
    if g == 1:
        return Fraction(0)
    constants = {
        2: ((1, 204), 16, 1),
        3: ((5, 3792, 1_149_120, 217_071_360), 138_240, 2),
        4: (
            (
                287,
                268_881,
                115_455_816,
                29_725_133_760,
                5_594_347_866_240,
            ),
            17_418_240,
            3,
        ),
    }
    coeffs, denominator, c_power = constants[g]
    numerator = Fraction(0)
    for coeff in coeffs:
        numerator = numerator * c + coeff
    return numerator / (denominator * c**c_power)


def test_package_firewalls_have_required_sizes_and_entries():
    assert HOLOGRAPHIC_PACKAGE_ENTRIES == (
        "A",
        "A^i",
        "A^!",
        "C",
        "r(z)",
        "Theta_A",
        "nabla^hol",
    )
    assert MODULAR_KOSZUL_COMPUTE_PROJECTIONS == (
        "Fact_X(L)",
        "barB_X(L)",
        "Theta_L",
        "L_L",
        "(V_br,T_br)",
        "R4_mod(L)",
    )
    summary = structural_firewall_summary()
    assert summary["packages_are_distinct"] is True


def test_object_firewall_keeps_inversion_dual_and_bulk_distinct():
    roles = typed_object_firewall()
    assert roles["Omega(B(A))"] == "bar-cobar inversion recovering A"
    assert "Verdier" in roles["A^!"]
    assert "ChirHoch" in roles["Z_ch^der(A)"]
    assert roles["B(A)"] != roles["A^i"]


def test_kernel_constants_are_exact_and_sourced():
    constants = kernel_constant_certificate(k=Fraction(3), h_vee=Fraction(2), c=26)
    assert constants["source"] == "chapters/examples/landscape_census.tex:173-186"
    assert constants["affine_raw_trace"]["formula"] == "k*Omega_tr/z"
    assert constants["affine_raw_trace"]["coefficient"] == 3
    assert constants["affine_kz"]["formula"] == "Omega/((k+h^vee)z)"
    assert constants["affine_kz"]["coefficient"] == Fraction(1, 5)
    assert constants["heisenberg"]["formula"] == "k/z"
    assert constants["heisenberg"]["coefficient"] == 3
    assert constants["virasoro"]["formula"] == "(c/2)/z^3 + 2T/z"
    assert constants["virasoro"]["central_coefficient"] == 13
    assert constants["virasoro"]["stress_coefficient"] == 2

    with pytest.raises(ValueError):
        kernel_constant_certificate(k=Fraction(-2), h_vee=Fraction(2))


def test_fp_constants_match_landscape_table_through_genus_6():
    assert lambda_fp(1) == Fraction(1, 24)
    assert lambda_fp(2) == Fraction(7, 5760)
    assert lambda_fp(3) == Fraction(31, 967680)
    assert lambda_fp(4) == Fraction(127, 154828800)
    assert lambda_fp(5) == Fraction(73, 3503554560)
    assert lambda_fp(6) == Fraction(1414477, 2678117105664000)


def test_fp_formula_uses_even_bernoulli_numbers_exactly():
    for g in range(1, 11):
        power = 2 ** (2 * g - 1)
        expected = (
            Fraction(power - 1, power)
            * abs(_bernoulli_number(2 * g))
            / Fraction(1, 1)
            / __import__("math").factorial(2 * g)
        )
        assert lambda_fp(g) == expected


def test_ahat_reciprocal_series_is_independent_fp_oracle():
    coeffs = ahat_log_coefficients(10)
    for g, coeff in enumerate(coeffs, start=1):
        assert coeff == lambda_fp(g)
        assert ahat_log_coefficient(g) == lambda_fp(g)


def test_invalid_genus_inputs_raise():
    with pytest.raises(ValueError):
        lambda_fp(0)
    with pytest.raises(ValueError):
        ahat_log_coefficients(0)
    with pytest.raises(ValueError):
        ahat_log_coefficient(0)


def test_scalar_shadow_window_is_finite_and_not_analytic_claim():
    cert = scalar_shadow_window(Fraction(13, 2), 5)
    assert cert.kappa == Fraction(13, 2)
    assert cert.g_max == 5
    assert cert.variable == "q = hbar^2"
    assert cert.ring == "Q[kappa][[q]]/(q^6)"
    assert cert.log_identity_modulus == "q^6"
    assert cert.all_coefficients_match is True
    assert cert.analytic_tau_identity_proved is False
    assert cert.kw_kdv_tau_membership_certified is False
    assert cert.full_descendant_hierarchy_certified is False
    assert cert.full_mc_element_certified is False
    assert cert.bar_cobar_theorem_certified is False
    assert cert.derived_center_data_certified is False
    assert cert.stable_graph_cross_channels_checked is False
    assert cert.multi_weight_theorem is False
    assert cert.rows[1].scalar_free_energy == Fraction(13, 2) * Fraction(7, 5760)


def test_scalar_projection_firewall_blocks_theorem_overreach():
    firewall = scalar_projection_firewall()
    assert firewall["certifies_fp_coefficients"] is True
    assert firewall["certifies_finite_log_window"] is True
    assert firewall["certifies_full_mc_element"] is False
    assert firewall["certifies_bar_cobar_equivalence"] is False
    assert firewall["certifies_derived_center_data"] is False
    assert firewall["certifies_all_class_theorem"] is False
    assert firewall["certifies_full_descendant_hierarchy"] is False
    assert "Mbar" in firewall["tautological_integral"]


def test_shadow_free_energy_is_only_diagonal_scalar_term():
    assert shadow_free_energy(Fraction(5), 2) == Fraction(5) * Fraction(7, 5760)
    assert shadow_free_energy(Fraction(-3, 2), 5) < 0


def test_tau_kw_coefficients_from_exponential_recurrence():
    coeffs = tau_kw_coefficients(3)
    assert coeffs[0] == 1
    assert coeffs[1] == Fraction(1, 24)
    assert coeffs[2] == Fraction(1, 480)
    expected_q3 = (
        lambda_fp(3)
        + lambda_fp(1) * lambda_fp(2)
        + lambda_fp(1) ** 3 / 6
    )
    assert coeffs[3] == expected_q3


def test_tau_shadow_coefficients_kappa_5_are_exact():
    coeffs = tau_shadow_coefficients(Fraction(5), 3)
    assert coeffs[0] == 1
    assert coeffs[1] == Fraction(5, 24)
    assert coeffs[2] == Fraction(1, 36)
    expected_q3 = (
        5 * lambda_fp(3)
        + 25 * lambda_fp(1) * lambda_fp(2)
        + 125 * lambda_fp(1) ** 3 / 6
    )
    assert coeffs[3] == expected_q3


def test_formal_log_recovery_inverts_exponential_window():
    kw_tau = tau_kw_coefficients(6)
    recovered = formal_log_from_unit_series(kw_tau)
    assert recovered[0] == 0
    for g in range(1, 7):
        assert recovered[g] == lambda_fp(g)


def test_formal_tau_power_window_is_formal_not_analytic():
    result = formal_tau_power_window(Fraction(7, 3), 6)
    assert result["finite_formal_match"] is True
    assert result["theorem_proves_log_coefficients_only"] is True
    assert result["derived_formal_exponential_check"] is True
    assert result["analytic_tau_identity_proved"] is False
    assert result["constructs_analytic_tau_function"] is False
    assert result["kw_kdv_tau_membership_certified"] is False
    assert result["full_descendant_hierarchy_certified"] is False
    assert result["firewall"]["certifies_full_mc_element"] is False
    assert result["modulus"] == "q^7"


def test_kappa_zero_and_one_special_windows():
    zero = kappa_zero_degenerate_case(5)
    assert zero["all_Fg_zero"] is True
    assert zero["tau_coefficients"] == (1, 0, 0, 0, 0, 0)

    one = kappa_one_recovers_kw(5)
    assert one["recovers_kw"] is True
    assert one["kw_finite_window_normalization_certified"] is True
    assert one["kw_tau_normalization_certified"] is False
    assert one["full_descendant_hierarchy_certified_by_this_engine"] is False
    assert one["tau_coefficients"] == tau_kw_coefficients(5)


def test_scalar_lane_certificate_separates_uniform_from_multi_weight():
    assert scalar_lane_certificate("Virasoro", (2,))["on_scalar_lane"] is True
    w3 = scalar_lane_certificate("W_3", (2, 3))
    assert w3["uniform_weight"] is False
    assert w3["cross_channel_correction_required"] is True
    assert w3["stable_graph_cross_channels_required"] is True
    assert w3["scalar_formula_exact"] is False
    assert w3["certifies_full_mc_element"] is False

    free_field = scalar_lane_certificate(
        "beta-gamma free field", (1, 2), free_field_exception=True
    )
    assert free_field["uniform_weight"] is False
    assert free_field["on_scalar_lane"] is False
    assert free_field["scalar_formula_exact"] is True
    assert free_field["cross_channel_correction_required"] is False
    assert free_field["stable_graph_cross_channels_required"] is False
    assert free_field["exception_source"].endswith(":196-240")


def test_standard_family_table_is_finite_window_only():
    table = standard_family_verification_table(g_max=4)
    assert table["Heisenberg_k=1"]["kappa"] == Fraction(1)
    assert table["Virasoro_c=26"]["kappa"] == Fraction(13)
    assert table["Affine_sl2_k=1"]["kappa"] == Fraction(9, 4)
    for data in table.values():
        assert data["on_scalar_lane"] is True
        assert data["log_coefficients_match"] is True
        assert data["finite_formal_tau_match"] is True
        assert data["analytic_tau_identity_proved"] is False
        assert data["kw_kdv_tau_membership_certified"] is False


def test_w3_kappa_is_diagonal_sum_not_full_free_energy():
    c = Fraction(50)
    assert kappa_w3(c) == Fraction(5, 6) * c
    assert kappa_w3(c) == c / 2 + c / 3


def test_w3_genus2_cross_decomposition_matches_manuscript_formula():
    c = Fraction(100)
    pieces = w3_cross_correction_decomposition_genus2(c)
    assert pieces["sunset"] == Fraction(3, 100)
    assert pieces["theta"] == Fraction(9, 200)
    assert pieces["bridge_loop"] == Fraction(1, 16)
    assert pieces["barbell"] == Fraction(21, 400)
    assert pieces["total"] == Fraction(304, 1600)
    assert pieces["total"] == w3_delta_cross(2, c)


def test_w3_genus2_sharp_negative_for_scalar_tau_power():
    result = multi_weight_failure_genus2_w3(Fraction(100))
    assert result["F2_scalar"] == Fraction(5 * 100, 6) * Fraction(7, 5760)
    assert result["delta_F2_cross"] == Fraction(304, 1600)
    assert result["F2_full"] != result["F2_scalar"]
    assert result["tau_power_fails_for_full_free_energy"] is True


def test_w3_cross_corrections_through_genus_4_are_exact():
    c = Fraction(10)
    assert w3_delta_cross(1, c) == 0
    assert w3_delta_cross(2, c) == Fraction(214, 160)
    assert w3_delta_cross(3, c) == Fraction(
        5 * c**3 + 3792 * c**2 + 1_149_120 * c + 217_071_360,
        138_240 * c**2,
    )
    assert w3_delta_cross(4, c) == Fraction(
        287 * c**4
        + 268_881 * c**3
        + 115_455_816 * c**2
        + 29_725_133_760 * c
        + 5_594_347_866_240,
        17_418_240 * c**3,
    )


def test_w3_cross_corrections_match_anchored_horner_oracle():
    for c in [Fraction(1), Fraction(10), Fraction(50), Fraction(100)]:
        assert w3_delta_cross(2, c) == _anchored_w3_cross(2, c)
        assert w3_delta_cross(3, c) == _anchored_w3_cross(3, c)
        assert w3_delta_cross(4, c) == _anchored_w3_cross(4, c)


def test_w3_cross_channel_witness_records_stable_graph_scope():
    g2 = w3_cross_channel_witness(2, Fraction(50))
    assert g2["delta_cross"] == Fraction(127, 400)
    assert g2["stable_graph_count"] == 7
    assert g2["tautological_ring_input_required"] is True
    assert g2["certifies_full_mc_element"] is False

    g3 = w3_cross_channel_witness(3, Fraction(50))
    assert g3["stable_graph_count"] == 42
    assert g3["delta_cross"] == _anchored_w3_cross(3, Fraction(50))

    g4 = w3_cross_channel_witness(4, Fraction(50))
    assert g4["stable_graph_count"] is None
    assert "overdetermined" in g4["witness"]
    assert g4["delta_cross"] == _anchored_w3_cross(4, Fraction(50))


def test_w3_cross_correction_has_non_unitary_zero_at_c_minus_204():
    assert w3_delta_cross(2, Fraction(-204)) == 0
    window = w3_free_energy_window(Fraction(-204), 2)
    assert window["rows"][2]["scalar_equals_full"] is True


def test_w3_positive_cross_corrections_for_positive_c():
    for c in [Fraction(1), Fraction(2), Fraction(10), Fraction(50), Fraction(100)]:
        window = w3_free_energy_window(c, 4)
        assert window["lane"]["cross_channel_correction_required"] is True
        assert window["full_mc_element_certified"] is False
        assert window["derived_center_data_certified"] is False
        assert window["rows"][1]["delta_cross"] == 0
        for g in (2, 3, 4):
            assert window["rows"][g]["delta_cross"] > 0
            assert window["cross_channel_witnesses"][g]["tautological_ring_input_required"] is True
            assert window["rows"][g]["full"] != window["rows"][g]["scalar_diagonal"]


def test_w3_large_c_ratios_are_recorded_exactly():
    assert w3_large_c_cross_to_scalar_ratio(2) == 0
    assert w3_large_c_cross_to_scalar_ratio(3) == Fraction(42, 31)
    assert w3_large_c_cross_to_scalar_ratio(4) == Fraction(9184, 381)


def test_w3_invalid_cross_window_raises():
    with pytest.raises(ValueError):
        w3_delta_cross(5, Fraction(10))
    with pytest.raises(ValueError):
        w3_delta_cross(2, Fraction(0))
    with pytest.raises(ValueError):
        w3_free_energy_window(Fraction(10), 5)


def test_genus1_universality_is_scalar_and_delta_free():
    for kappa in [Fraction(1), Fraction(5), Fraction(13, 2), Fraction(-3)]:
        result = genus1_universality(kappa)
        assert result["F_1"] == kappa / 24
        assert result["match"] is True
        assert result["cross_channel_delta"] == 0


def test_kdv_residual_blocks_kw_power_overreach():
    one = kdv_compatibility_check(Fraction(1))
    assert one["satisfies_kdv"] is True
    assert one["kw_reference_case"] is True
    assert one["kw_tau_normalization_certified"] is False
    assert one["kw_tau_normalization_certified_by_this_engine"] is False

    zero = kdv_compatibility_check(Fraction(0))
    assert zero["satisfies_kdv"] is True
    assert zero["trivial_solution"] is True
    assert zero["kw_tau_normalization_certified"] is False

    half = kdv_compatibility_check(Fraction(1, 2))
    assert half["satisfies_kdv"] is False
    assert half["discrepancy_coefficient"] == Fraction(1, 4)

    five = kdv_compatibility_check(Fraction(5))
    assert five["discrepancy_coefficient"] == Fraction(-20)


def test_kdv_hirota_residuals_are_separate_from_coefficient_identity():
    half = kdv_hirota_residual_certificate(Fraction(1, 2))
    assert half["kdv_residual_factor"] == Fraction(1, 4)
    assert half["hirota_residual_factor"] == Fraction(1, 4)
    assert half["standard_kdv_hierarchy"] is False
    assert half["standard_hirota_equations"] is False
    assert half["coefficient_identity_used"] is False

    kw = kdv_hirota_residual_certificate(Fraction(1))
    assert kw["kw_reference_case"] is True
    assert kw["full_kw_descendant_hierarchy"] is False
    assert kw["full_descendant_hierarchy_certified_by_this_engine"] is False
    assert kw["kw_tau_normalization_certified"] is False

    zero = kdv_hirota_residual_certificate(Fraction(0))
    assert zero["standard_kdv_hierarchy"] is True
    assert zero["standard_hirota_equations"] is True
    assert zero["full_kw_descendant_hierarchy"] is False
    assert zero["trivial_zero_solution_exception"] is True


def test_virasoro_scope_is_not_certified_by_zero_time_coefficients():
    scope = virasoro_constraint_scope(Fraction(5))
    assert scope["zero_time_coefficients_only"] is True
    assert scope["full_descendant_constraints_checked"] is False
    assert scope["analytic_tau_membership_certified_by_coefficients"] is False
    assert scope["kw_virasoro_normalization_preserved"] is False

    kw_scope = virasoro_constraint_scope(Fraction(1))
    assert kw_scope["kw_reference_case"] is True
    assert kw_scope["kw_virasoro_normalization_preserved"] is False
    assert kw_scope["full_descendant_hierarchy_certified"] is False
    assert kw_scope["full_descendant_hierarchy_certified_by_this_engine"] is False


def test_virasoro_scope_report_contains_window_values():
    report = free_energy_virasoro_constraints(Fraction(7), g_max=3)
    assert report["full_descendant_constraints_checked"] is False
    assert report["coefficient_identity_only"] is True
    assert report["coefficient_window"][1] == Fraction(7, 24)
    assert report["coefficient_window"][2] == Fraction(7) * Fraction(7, 5760)


def test_convergence_scope_separates_ahat_radius_from_tau_theorem():
    scope = convergence_radius_shadow(Fraction(5))
    assert scope["formal_coefficient_window_only"] is True
    assert scope["coefficient_identity_implies_radius"] is False
    assert scope["finite_window_has_radius"] is False
    assert scope["ahat_meromorphic_model_radius_hbar"] == "2*pi"
    assert scope["ahat_model_radius_independent_of_kappa"] is True
    assert scope["radius_theorem_for_tau_shadow"] is False
    assert scope["analytic_tau_identity_proved"] is False


def test_complementarity_is_finite_formal_product_only():
    vir = complementarity_tau_functions(Fraction(5), Fraction(8), g_max=4)
    assert vir["kappa_sum"] == 13
    for g in range(1, 5):
        assert vir["product_log_coefficients"][g] == 13 * lambda_fp(g)
    assert vir["analytic_tau_identity_proved"] is False
    assert vir["kw_kdv_tau_membership_certified"] is False
    assert "Verdier" in vir["object_firewall"]["A^!"]
    assert "bar-cobar inversion" in vir["object_firewall"]["Omega(B(A))"]

    km = complementarity_tau_functions(Fraction(9, 4), Fraction(-9, 4), g_max=4)
    assert km["kappa_sum"] == 0
    assert km["product_tau_coefficients"] == (1, 0, 0, 0, 0)


def test_fp_window_exposes_exact_mapping():
    assert fp_window(3) == {
        1: Fraction(1, 24),
        2: Fraction(7, 5760),
        3: Fraction(31, 967680),
    }
