"""Independent convention checks for the standard W3 lambda brackets."""

import sympy as sp

from compute.lib.w3_lambda_brackets import (
    TT_lambda_bracket,
    TW_lambda_bracket,
    WT_lambda_bracket,
    WW_lambda_bracket_from_OPE,
    c,
    composite_field_necessity_theorem,
    compute_T_lambda_TT,
    compute_T_lambda_d2T,
    lambda_norm,
    lambda_zero_eigenvalue,
    level_four_vacuum_gram_matrix,
    run_all_verifications,
    verify_Lambda_0_on_hw,
    verify_Lambda_quasi_primary,
    verify_WW_bracket_coefficients,
    verify_alpha_from_jacobi,
    verify_beta_from_quasi_primarity,
    verify_integral_term_symbolically,
    w3_lambda_coupling,
    w3_mode_lambda_coefficient,
    weight_4_linear_quasi_primaries,
)


def _field_map(terms):
    return {field: coefficient for coefficient, field in terms}


def test_tt_tw_wt_lambda_brackets():
    assert _field_map(TT_lambda_bracket()[3])["scalar"] == c / 12
    assert TW_lambda_bracket()[0] == [(1, "dW")]
    assert WT_lambda_bracket()[0] == [(2, "dW")]
    assert TW_lambda_bracket()[1] == WT_lambda_bracket()[1] == [(3, "W")]


def test_ww_lambda_bracket_has_32_16_coefficients():
    bracket = WW_lambda_bracket_from_OPE()
    alpha = 32 / (22 + 5 * c)
    assert sp.simplify(_field_map(bracket[1])["Lambda"] - alpha) == 0
    assert sp.simplify(_field_map(bracket[0])["dLambda"] - alpha / 2) == 0
    assert _field_map(bracket[5])["scalar"] == c / 360
    assert bracket[4] == []


def test_mode_conversion_supplies_the_independent_half_factor():
    m, n = sp.symbols("m n")
    expected = 16 * (m - n) / (22 + 5 * c)
    assert sp.simplify(w3_mode_lambda_coefficient(m, n) - expected) == 0


def test_noncommutative_wick_and_sesquilinearity_packets():
    tt = compute_T_lambda_TT()
    d2t = compute_T_lambda_d2T()
    assert _field_map(tt[2])["dT"] == sp.Rational(3, 2)
    assert _field_map(tt[3])["T"] == (c + 8) / 6
    assert _field_map(d2t[2])["dT"] == 5
    assert _field_map(d2t[3])["T"] == 2
    integral = verify_integral_term_symbolically()
    assert integral["lambda^5 scalar"] == c / 40


def test_lambda_quasi_primary_and_gram_norm():
    bracket = verify_Lambda_quasi_primary()
    assert bracket[2] == []
    assert _field_map(bracket[3])["T"] == (5 * c + 22) / 30
    expected_norm = c * (5 * c + 22) / 10
    assert sp.factor(lambda_norm() - expected_norm) == 0
    matrix = level_four_vacuum_gram_matrix()
    vector = sp.Matrix([1, sp.Rational(-3, 5)])
    assert sp.factor((vector.T * matrix * vector)[0] - expected_norm) == 0
    assert verify_beta_from_quasi_primarity() == sp.Rational(-3, 10)


def test_lambda_zero_mode_on_highest_weight_vector():
    h = sp.Symbol("h")
    expected = h**2 + h / 5
    assert sp.factor(lambda_zero_eigenvalue(h) - expected) == 0
    assert sp.factor(verify_Lambda_0_on_hw() - expected) == 0
    assert lambda_zero_eigenvalue(sp.Rational(-1, 5)) == 0


def test_composite_field_is_forced_on_the_generic_standard_ope():
    linear = weight_4_linear_quasi_primaries()
    assert linear["linear_quasi_primary_dimension"] == 0
    packet = composite_field_necessity_theorem()
    assert packet.status == "proved elsewhere"
    assert sp.simplify(packet.value - w3_lambda_coupling()) == 0
    assert sp.simplify(verify_alpha_from_jacobi() - 32 / (22 + 5 * c)) == 0


def test_full_verification_packet():
    assert all(verify_WW_bracket_coefficients().values())
    results = run_all_verifications()
    assert sp.factor(results["Lambda_norm"] - c * (5 * c + 22) / 10) == 0
    assert all(results["coefficient_checks"].values())
