"""Exact four-point kinematics and open W3 scalar-ODE checks."""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.theorem_w3_4pt_ode_engine import (
    DIFF_ORDER_W3,
    K_MAX_VIR,
    K_MAX_W3,
    LAMBDA_COUPLING_NUMERATOR,
    MAX_OPE_POLE_W3,
    channel_structure_4pt,
    diagnostic_scope_4pt,
    evaluate_hamiltonian_at_z,
    extract_scalar_ode_coefficients,
    fuchsian_structure_4pt,
    full_4pt_ode_summary,
    lambda_coupling_denominator,
    n_moduli,
    ode_order_analysis,
    require_regular_universal_normalization,
    sl2_fixed_positions,
    surviving_depths_on_primaries,
    t_sector_restriction_4pt,
    verify_depth_4_vanishing,
    virasoro_bpz_4pt_hamiltonian,
    w3_4pt_hamiltonian,
    w3_c2_specific_coefficients,
    w3_channel_kappa_matrix,
    w3_channel_norm_matrix,
    w3_exceeds_virasoro_order,
    w3_lambda_coupling,
    w3_minimal_model_c2,
    w3_universal_normalization_domain,
    w_sector_leading_term,
    zamolodchikov_lambda_norm,
)


def test_four_points_leave_one_cross_ratio():
    assert n_moduli(3) == 0
    assert n_moduli(4) == 1
    assert n_moduli(5) == 2
    positions = sl2_fixed_positions()
    assert positions["z1"] == 0
    assert positions["z3"] == 1
    assert positions["z4"] == sp.oo


def test_w3_normalization_domain_and_32_coupling():
    assert LAMBDA_COUPLING_NUMERATOR == 32
    assert lambda_coupling_denominator(Fraction(2)) == 32
    assert w3_lambda_coupling(Fraction(2)) == 1
    assert zamolodchikov_lambda_norm(Fraction(2)) == sp.Rational(32, 5)
    assert w3_universal_normalization_domain(2)["regular"]
    assert not w3_universal_normalization_domain(0)["regular"]
    assert not w3_universal_normalization_domain(Fraction(-22, 5))["regular"]
    require_regular_universal_normalization(2)
    with pytest.raises(ValueError):
        require_regular_universal_normalization(0)


def test_channel_matrix_is_typed_as_ope_norm_data():
    c = sp.Symbol("c")
    assert w3_channel_norm_matrix(c) == sp.diag(c / 2, c / 3)
    packet = w3_channel_kappa_matrix(c)
    assert packet["mathematical_type"] == "leading OPE norm matrix"
    assert packet["matrix"] == sp.diag(c / 2, c / 3)
    assert packet["modular_kappa_matrix"].status == "open"


def test_local_pole_order_remains_separate_from_collision_and_ode_order():
    assert MAX_OPE_POLE_W3 == 6
    assert K_MAX_W3.status == "open"
    assert K_MAX_VIR.status == "open"
    assert DIFF_ORDER_W3.status == "open"
    assert ode_order_analysis().status == "open"
    assert w3_exceeds_virasoro_order().status == "open"


def test_fifth_order_ope_pole_absence_has_open_collision_consequence():
    packet = verify_depth_4_vanishing([1, 2, 10])
    assert packet["all_zero"]
    assert packet["W_(4)W"] == ({}, {}, {})
    assert packet["collision_consequence"].status == "open"


def test_c2_packet_uses_correct_lambda_zero_mode():
    packet = w3_c2_specific_coefficients(sp.Rational(1, 2), 0)
    assert packet["WW_to_Lambda"] == 1
    assert packet["WW_to_dLambda"] == sp.Rational(1, 2)
    assert packet["Lambda_zero"] == sp.Rational(7, 20)
    assert packet["collision_projection"].status == "open"
    assert w3_minimal_model_c2()["minimal_model_identification"].status == "open"


def test_channel_structure_contains_exact_ope_orders_only():
    packet = channel_structure_4pt(2)
    assert packet["OPE_pole_orders"] == {"TT": 4, "TW": 2, "WT": 2, "WW": 6}
    assert packet["max_OPE_pole"] == 6
    assert packet["collision_channels"].status == "open"


@pytest.mark.parametrize(
    "packet",
    [
        virasoro_bpz_4pt_hamiltonian(2, 0, 0, 0, 0),
        w3_4pt_hamiltonian(2, 0, 0, 0, 0, 0, 0, 0, 0),
        extract_scalar_ode_coefficients(2, 0, 0, 0, 0),
        t_sector_restriction_4pt(2, 0, 0, 0, 0),
        w_sector_leading_term(2, 0, 0),
        surviving_depths_on_primaries(2, 0, 0),
        evaluate_hamiltonian_at_z(2, 0, 0, 0, 0, 0, 0, 0, 0, Fraction(1, 2)),
        fuchsian_structure_4pt(),
    ],
)
def test_hamiltonian_bpz_fuchsian_and_scalar_ode_outputs_are_open(packet):
    assert packet.status == "open"


def test_scope_and_full_summary():
    scope = diagnostic_scope_4pt()
    assert scope["cross_ratio_dimension"] == "exact"
    assert scope["finite_OPE"] == "exact"
    assert scope["scalar_ODE"].status == "open"
    summary = full_4pt_ode_summary(2, 0, 0, 0, 0)
    assert summary["moduli_dimension"] == 1
    assert summary["Hamiltonian"].status == "open"
    assert summary["scalar_ODE"].status == "open"
