"""Exact NS-mode and PBW checks for the N=2 superconformal algebra."""

from fractions import Fraction

import pytest
import sympy as sp

from compute.lib.bar_cohomology_n2sca_explicit_engine import (
    OpenN2BarComparisonError,
    SuperCEComplex,
    bracket,
    compute_master,
    enumerate_creating_modes,
    enumerate_n2_states,
    kappa_n2,
    mode_charge,
    mode_parity,
    mode_weight_half,
    n2_weight_space_table,
    spectral_flow_packet,
    state_charge,
    state_parity,
    state_weight_half,
    vacuum_character_coefficients,
    verify_bracket_relations,
    verify_d_squared_all,
    verify_super_jacobi,
)


def test_standard_negative_mode_brackets():
    assert all(verify_bracket_relations().values())
    assert bracket(("G+", Fraction(-3, 2)), ("G-", Fraction(-3, 2))) == {
        ("L", Fraction(-3)): 2
    }
    expected = {
        ("L", Fraction(-4)): 2,
        ("J", Fraction(-4)): 1,
    }
    assert bracket(("G+", Fraction(-3, 2)), ("G-", Fraction(-5, 2))) == expected
    assert bracket(("G-", Fraction(-5, 2)), ("G+", Fraction(-3, 2))) == expected


def test_super_skew_symmetry_on_mixed_and_even_pairs():
    a = ("L", Fraction(-2))
    b = ("G+", Fraction(-3, 2))
    forward = bracket(a, b)
    reverse = bracket(b, a)
    assert reverse == {mode: -coefficient for mode, coefficient in forward.items()}
    x = ("L", Fraction(-2))
    y = ("L", Fraction(-3))
    assert bracket(y, x) == {mode: -coefficient for mode, coefficient in bracket(x, y).items()}


@pytest.mark.parametrize("max_wh", [6, 8, 10])
def test_super_jacobi(max_wh):
    assert verify_super_jacobi(max_wh) == 0


def test_vacuum_creating_modes_and_types():
    modes = enumerate_creating_modes(6)
    assert len(modes) == 9
    assert mode_weight_half(("J", Fraction(-1))) == 2
    assert mode_weight_half(("G+", Fraction(-3, 2))) == 3
    assert mode_parity(("G-", Fraction(-3, 2))) == 1
    assert mode_charge(("G+", Fraction(-3, 2))) == 1


def test_pbw_states_have_correct_energy_and_fermionic_multiplicity():
    for weight_half in range(0, 13):
        for state in enumerate_n2_states(weight_half):
            assert state_weight_half(state) == weight_half
            odd_modes = [mode for mode in state if mode_parity(mode)]
            assert len(odd_modes) == len(set(odd_modes))


def test_pbw_enumeration_matches_independent_character_product():
    max_wh = 14
    product_coefficients = vacuum_character_coefficients(max_wh)
    enumerated = {weight: len(enumerate_n2_states(weight)) for weight in range(max_wh + 1)}
    assert enumerated == product_coefficients


def test_charge_conjugation_and_parity_refinement():
    table = n2_weight_space_table(12)
    for data in table.values():
        charges = data["charges"]
        for charge, multiplicity in charges.items():
            assert multiplicity == charges.get(-charge, 0)
        assert sum(data["parities"].values()) == data["total"]
    state = (("G+", Fraction(-3, 2)), ("J", Fraction(-1)))
    assert state_charge(state) == 1
    assert state_parity(state) == 1


def test_ce_chain_space_uses_shifted_parity():
    ce = SuperCEComplex(8)
    j_index = ce.modes.index(("J", Fraction(-1)))
    gp_index = ce.modes.index(("G+", Fraction(-3, 2)))
    degree_two_weight_two = ce.weight_basis(2, 4)
    assert (j_index, j_index) not in degree_two_weight_two
    degree_two_weight_three = ce.weight_basis(2, 6)
    assert (gp_index, gp_index) in degree_two_weight_three


@pytest.mark.parametrize(
    "operation",
    [
        lambda: SuperCEComplex(8).ce_differential(1, 6),
        lambda: SuperCEComplex(8).cohomology_dim(2, 6),
        lambda: verify_d_squared_all(8),
        lambda: kappa_n2(sp.Symbol("c")),
    ],
)
def test_ce_bar_and_modular_promotions_are_open(operation):
    with pytest.raises(OpenN2BarComparisonError):
        operation()


def test_spectral_flow_arithmetic():
    packet = spectral_flow_packet(sp.Rational(1, 2), 1, 2, 3)
    assert packet["h"] == sp.Rational(17, 8)
    assert packet["q"] == sp.Rational(5, 2)


def test_master_packet_separates_exact_inputs_from_open_claims():
    packet = compute_master(8)
    assert all(packet["bracket_checks"].values())
    assert packet["super_jacobi_violations"] == 0
    assert packet["pbw_weight_spaces"][0]["total"] == 1
    assert packet["ce_cohomology"].status == "open"
    assert packet["chiral_bar"].status == "open"
    assert packet["koszulness"].status == "open"
    assert packet["modular_kappa"].status == "open"
