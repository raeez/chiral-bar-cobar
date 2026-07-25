"""Verification of exact extended-family OPE data and open boundaries."""

from __future__ import annotations

import sympy as sp
import pytest

from compute.lib.shadow_tower_extended_families import (
    OpenShadowProjectionError,
    bp_c_arakawa,
    bp_generator_packet,
    bp_j_level_feigin_semikhatov,
    bp_modular_status,
    bp_ope_packet,
    bp_reflected_central_sum,
    bp_shifted_reflected_sum,
    bp_t_inverse_norm,
    bp_t_inverse_norm_factored,
    bp_t_line_status,
    certified_denominator_factors,
    lambda_norm_from_gram,
    level_four_vacuum_gram_matrix,
    s4_bp_tline,
    s4_w3_tline,
    s4_w3_wline,
    sl11_shadow_S2_fermionic,
    super_yangian_line_status,
    virasoro_level_four_inverse_norm,
    w3_alpha_coefficient,
    w3_derivative_lambda_coefficient,
    w3_mode_lambda_coefficient,
    w3_ope_packet,
    w3_t_line_status,
    w3_w_line_status,
    w_infinity_alpha,
    w_infinity_endpoint_status,
    zamolodchikov_norm_Lambda,
    zamolodchikov_norm_T,
    zamolodchikov_norm_W,
)


def test_level_four_norm_by_two_independent_routes():
    c = sp.Symbol("c")
    expected = c * (5 * c + 22) / 10
    assert sp.factor(zamolodchikov_norm_Lambda(c) - expected) == 0
    assert sp.factor(lambda_norm_from_gram(c) - expected) == 0
    matrix = level_four_vacuum_gram_matrix(c)
    assert matrix == sp.Matrix([[c * (c + 8) / 2, 3 * c], [3 * c, 5 * c]])


def test_leading_w3_norms():
    c = sp.Symbol("c")
    assert zamolodchikov_norm_T(c) == c / 2
    assert zamolodchikov_norm_W(c) == c / 3


def test_w3_pole_two_and_pole_one_coefficients():
    c = sp.Symbol("c")
    assert w3_alpha_coefficient(c) == 32 / (22 + 5 * c)
    assert w3_derivative_lambda_coefficient(c) == 16 / (22 + 5 * c)
    packet = w3_ope_packet(c)["WW"]
    assert packet[1]["Lambda"] == 32 / (22 + 5 * c)
    assert packet[0]["dLambda"] == 16 / (22 + 5 * c)


def test_w3_mode_coefficient_checks_the_half_factor():
    m, n, c = sp.symbols("m n c")
    expected = 16 * (m - n) / (22 + 5 * c)
    assert sp.simplify(w3_mode_lambda_coefficient(m, n, c) - expected) == 0


def test_inverse_norm_is_exact_while_shadow_is_open():
    c = sp.Symbol("c")
    exact = 10 / (c * (5 * c + 22))
    assert sp.cancel(virasoro_level_four_inverse_norm(c) - exact) == 0
    t_line = w3_t_line_status(c)
    w_line = w3_w_line_status(c)
    assert sp.cancel(t_line["inverse_N_Lambda"] - exact) == 0
    assert t_line["scalar_shadow"].status == "open"
    assert w_line["scalar_quartic"].status == "open"


@pytest.mark.parametrize("function", [s4_w3_tline, s4_w3_wline])
def test_w3_shadow_compatibility_names_stop_at_projection_boundary(function):
    with pytest.raises(OpenShadowProjectionError, match="H_bar"):
        function(sp.Symbol("c"))


def test_bp_standard_central_charge_and_all_even_generators():
    k = sp.Symbol("k")
    expected = -((2 * k + 3) * (3 * k + 1)) / (k + 3)
    assert sp.factor(bp_c_arakawa(k) - expected) == 0
    generators = bp_generator_packet()
    assert {entry["parity"] for entry in generators.values()} == {"even"}
    assert generators["G+"]["weight"] == sp.Rational(3, 2)


def test_bp_fkr_ope_packet():
    k = sp.Symbol("k")
    packet = bp_ope_packet(k)
    assert packet["JJ"][1]["vac"] == (2 * k + 3) / 3
    assert packet["G+G-"][2]["vac"] == (k + 1) * (2 * k + 3)
    assert packet["G+G-"][1]["J"] == 3 * (k + 1)
    assert packet["G+G-"][0]["T"] == -(k + 3)
    assert bp_j_level_feigin_semikhatov(k) == (2 * k + 3) / 3


def test_bp_t_inverse_norm_by_substitution_and_factorization():
    k = sp.Symbol("k")
    assert sp.factor(bp_t_inverse_norm(k) - bp_t_inverse_norm_factored(k)) == 0
    expected = 10 * (k + 3) ** 2 / (
        3 * (2 * k + 3) * (3 * k + 1) * (10 * k**2 + 11 * k - 17)
    )
    assert sp.factor(bp_t_inverse_norm(k) - expected) == 0


def test_bp_reflection_ledgers_are_distinct():
    k = sp.Symbol("k")
    assert bp_reflected_central_sum(k) == 50
    assert bp_shifted_reflected_sum(k) == 196


def test_bp_projection_and_modular_quantities_are_open():
    k = sp.Symbol("k")
    assert bp_t_line_status(k)["scalar_quartic"].status == "open"
    assert {packet.status for packet in bp_modular_status().values()} == {"open"}
    with pytest.raises(OpenShadowProjectionError):
        s4_bp_tline(k)


def test_universal_w_and_super_yangian_lines_require_named_packages():
    w_packet = w_infinity_endpoint_status()
    y_packet = super_yangian_line_status()
    assert w_packet.status == "open"
    assert any("coordinate conversion" in item for item in w_packet.hypotheses)
    assert y_packet.status == "open"
    assert any("invariant form" in item for item in y_packet.hypotheses)
    with pytest.raises(OpenShadowProjectionError):
        w_infinity_alpha(sp.Symbol("c"), sp.Symbol("Psi"))
    with pytest.raises(OpenShadowProjectionError):
        sl11_shadow_S2_fermionic(sp.Symbol("k"))


def test_denominator_ledger_certifies_factors_and_opens_exponents():
    c, k = sp.symbols("c k")
    ledger = certified_denominator_factors(c, k)
    assert ledger["N_Lambda"] == c * (5 * c + 22) / 10
    assert ledger["W3_Lambda_coupling_denominator"] == 22 + 5 * c
    assert ledger["BP_central_numerator"] == (2 * k + 3) * (3 * k + 1)
    assert ledger["BP_level_four_factor"] == 10 * k**2 + 11 * k - 17
    assert ledger["shadow_denominator_exponents"].status == "open"
