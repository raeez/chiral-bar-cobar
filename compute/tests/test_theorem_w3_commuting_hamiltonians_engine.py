"""Exact W3 input checks and open Hamiltonian-boundary tests."""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.theorem_w3_commuting_hamiltonians_engine import (
    OpenW3HamiltonianError,
    W3_CENTRAL_CHARGE_CONDUCTOR,
    W3_KAPPA_CONDUCTOR,
    beta_composite,
    central_charge_from_level,
    collision_residue_on_primary,
    differential_operator_order,
    formal_reflected_central_sum_wN,
    full_evaluation,
    inverse_metric,
    k_max_family,
    kappa_T,
    koszul_conductor_wN,
    lambda_zero_mode_on_primary,
    leading_norm_packet,
    max_ope_pole,
    max_ope_pole_algebra,
    ode_order_prediction,
    ope_mode,
    principal_wN_central_charge,
    verify_commutativity_4pt_w3,
    verify_commutativity_5pt_w3,
    w3_exchange_ratios,
    w3_hamiltonian_on_primaries,
    w3_shadow_constants,
    w3_uniform_weight_reduction,
    w3_ward_identities,
    wN_structure,
    zamolodchikov_metric,
)


def test_exact_w3_ope_packet_uses_32_16():
    c = sp.Symbol("c")
    assert ope_mode("T", "T", 3)["vac"] == c / 2
    assert ope_mode("W", "W", 5)["vac"] == c / 3
    assert sp.simplify(ope_mode("W", "W", 1)["Lambda"] - 32 / (22 + 5 * c)) == 0
    assert sp.simplify(ope_mode("W", "W", 0)["dLambda"] - 16 / (22 + 5 * c)) == 0
    assert ope_mode("W", "W", 4) == {}


def test_ope_pole_orders_are_finite_local_data():
    assert max_ope_pole("T", "T") == 4
    assert max_ope_pole("T", "W") == 2
    assert max_ope_pole("W", "W") == 6
    assert max_ope_pole_algebra() == 6


def test_lambda_norm_inverse_and_exchange_normalizations():
    c = sp.Symbol("c")
    norm = c * (5 * c + 22) / 10
    assert sp.factor(zamolodchikov_metric(c) - norm) == 0
    assert sp.cancel(inverse_metric(c) - 1 / norm) == 0
    ratios = w3_exchange_ratios(c)
    assert sp.cancel(ratios["OPE_normalized"] - 10240 / (c * (5 * c + 22) ** 3)) == 0
    assert sp.cancel(ratios["mode_normalized"] - 2560 / (c * (5 * c + 22) ** 3)) == 0
    assert ratios["full_quartic_tensor"].status == "open"


def test_lambda_zero_mode_is_h_squared_plus_h_over_five():
    h = sp.Symbol("h")
    assert sp.factor(lambda_zero_mode_on_primary(sp.Symbol("c"), h) - (h**2 + h / 5)) == 0
    assert lambda_zero_mode_on_primary(2, sp.Rational(-1, 5)) == 0


def test_principal_central_and_reflection_arithmetic():
    k = sp.Symbol("k")
    assert sp.factor(central_charge_from_level(k) - (2 - 24 * (k + 2) ** 2 / (k + 3))) == 0
    assert formal_reflected_central_sum_wN(3, k) == 100
    assert W3_CENTRAL_CHARGE_CONDUCTOR == 100
    for N in range(2, 8):
        expected = 4 * N**3 - 2 * N - 2
        assert formal_reflected_central_sum_wN(N, k) == expected
        assert sp.simplify(
            principal_wN_central_charge(N, k)
            + principal_wN_central_charge(N, -k - 2 * N)
            - expected
        ) == 0


def test_leading_norms_are_separate_from_modular_kappa():
    c = sp.Symbol("c")
    norms = leading_norm_packet(c)
    assert norms["T"] == c / 2
    assert norms["W"] == c / 3
    assert norms["ratio"] == sp.Rational(2, 3)
    assert W3_KAPPA_CONDUCTOR.status == "conditional"
    assert W3_KAPPA_CONDUCTOR.value == sp.Rational(250, 3)
    assert kappa_T(c).status == "conditional"
    assert kappa_T(c).value == c / 2


def test_wn_structure_records_exact_generators_and_open_later_steps():
    packet = wN_structure(5)
    assert packet["generator_weights"] == (2, 3, 4, 5)
    assert packet["largest_diagonal_leading_OPE_pole"] == 10
    assert packet["formal_reflected_central_sum"] == 488
    assert packet["collision_depth"].status == "open"
    assert packet["scalar_ode_order"].status == "open"


@pytest.mark.parametrize(
    "operation",
    [
        lambda: k_max_family("w3"),
        lambda: differential_operator_order("w3"),
    ],
)
def test_pole_order_does_not_promote_to_collision_or_ode_order(operation):
    with pytest.raises(OpenW3HamiltonianError):
        operation()


@pytest.mark.parametrize(
    "packet",
    [
        collision_residue_on_primary(1, ("W", "W"), 2),
        w3_hamiltonian_on_primaries(2, 0),
        verify_commutativity_4pt_w3(2, (0, 0, 0, 0), (0, 0, 0, 0)),
        verify_commutativity_5pt_w3(2, (0, 0, 0, 0, 0)),
        w3_ward_identities(4, (0, 0, 0, 0), (0, 0, 0, 0), (0, 1, 2, 3)),
        ode_order_prediction("w3"),
        w3_shadow_constants(2),
    ],
)
def test_hamiltonian_flatness_ward_ode_and_shadow_claims_are_open(packet):
    assert packet.status == "open"


def test_full_evaluation_is_an_exact_input_open_output_packet():
    packet = full_evaluation(Fraction(2), Fraction(1, 2), 0)
    assert packet["leading_norms"]["T"] == 1
    assert packet["Lambda_norm"] == sp.Rational(32, 5)
    assert packet["Lambda_zero"] == sp.Rational(7, 20)
    assert packet["Hamiltonian"].status == "open"
    assert packet["scalar_ODE"].status == "open"


def test_uniform_weight_reduction_keeps_mixed_weights_visible():
    packet = w3_uniform_weight_reduction(2)
    assert packet["weights"] == (2, 3)
    assert packet["uniform_weight"] is False
    assert packet["scalar_modular_reduction"].status == "conditional"
    assert packet["scalar_modular_reduction"].value == sp.Rational(5, 3)


def test_principal_modular_conductor_is_conditional_on_named_packages():
    packet = koszul_conductor_wN(3)
    assert packet.status == "conditional"
    assert packet.value == sp.Rational(250, 3)
    assert any("H_diag" in hypothesis for hypothesis in packet.hypotheses)
    assert any("DS/bar" in hypothesis for hypothesis in packet.hypotheses)
