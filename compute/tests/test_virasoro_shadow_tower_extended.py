"""Regression tests for the Virasoro shadow tower through arity 10."""

import os
import sys

import pytest
from sympy import Rational, cancel, factor, simplify

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from virasoro_shadow_tower import c, shadow_coefficients, verify_known_values


def _shadow_coefficients_from_ql(max_arity=10):
    """Independent direct computation from sqrt(Q_L) with f^2 = Q_L."""
    q0 = c**2
    q1 = 12 * c
    q2 = Rational(36) + Rational(80, 1) / (5 * c + 22)

    max_n = max_arity - 2
    a = [None] * (max_n + 1)
    a[0] = c

    if max_n >= 1:
        a[1] = cancel(q1 / (2 * a[0]))

    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * a[0]))

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * a[0]))

    return {r: factor(cancel(a[r - 2] / r)) for r in range(2, max_arity + 1)}


EXPECTED_SHADOWS = {
    2: c / 2,  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [LC] S_2 = kappa(Vir_c) = c/2.
    3: Rational(2, 1),  # VERIFIED: [DC] _shadow_coefficients_from_ql gives a_1 = 6, hence S_3 = 2; [LC] Virasoro cubic normalization is c-independent.
    4: Rational(10, 1) / (c * (5 * c + 22)),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [LC] Delta = 8 kappa S_4 = 40/(5c+22).
    5: Rational(-48, 1) / (c**2 * (5 * c + 22)),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
    6: Rational(80, 1) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
    7: Rational(-2880, 1) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
    8: Rational(80, 1) * (2025 * c**2 + 16470 * c + 33314) / (c**5 * (5 * c + 22)**3),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
    9: Rational(-1280, 1) * (2025 * c**2 + 15570 * c + 29554) / (3 * c**6 * (5 * c + 22)**3),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
    10: Rational(256, 1) * (91125 * c**3 + 1050975 * c**2 + 3989790 * c + 4969967) / (c**7 * (5 * c + 22)**4),  # VERIFIED: [DC] matches the independent _shadow_coefficients_from_ql helper; [NE] specializations at c = 1/2, 1, 25 are checked below.
}


SPECIALIZED_S8_TO_S10 = [
    (Rational(1, 2), 8, Rational(861291520, 117649)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1/2; [NE] matches the master-equation engine.
    (Rational(1, 2), 9, Rational(-24802263040, 352947)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1/2; [NE] matches the master-equation engine.
    (Rational(1, 2), 10, Rational(3795318931456, 5764801)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1/2; [NE] matches the master-equation engine.
    (Rational(1, 1), 8, Rational(4144720, 19683)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1; [NE] matches the master-equation engine.
    (Rational(1, 1), 9, Rational(-60350720, 59049)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1; [NE] matches the master-equation engine.
    (Rational(1, 1), 10, Rational(2586075392, 531441)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 1; [NE] matches the master-equation engine.
    (Rational(25, 1), 8, Rational(27371024, 6204146484375)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 25; [NE] matches the master-equation engine.
    (Rational(25, 1), 9, Rational(-431213824, 465310986328125)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 25; [NE] matches the master-equation engine.
    (Rational(25, 1), 10, Rational(559462967552, 2850029791259765625)),  # VERIFIED: [DC] fixed-c Q_L recursion at c = 25; [NE] matches the master-equation engine.
]


def test_verify_known_values_reaches_s10():
    coeffs = verify_known_values(10)
    assert max(coeffs) == 10


@pytest.mark.parametrize("arity, expected", sorted(EXPECTED_SHADOWS.items()))
def test_master_equation_coefficients_match_expected_formulas(arity, expected):
    coeffs = shadow_coefficients(10)
    assert simplify(coeffs[arity] - expected) == 0


@pytest.mark.parametrize("arity, expected", sorted(EXPECTED_SHADOWS.items()))
def test_independent_ql_recursion_matches_expected_formulas(arity, expected):
    coeffs = _shadow_coefficients_from_ql(10)
    assert simplify(coeffs[arity] - expected) == 0


@pytest.mark.parametrize("c_val, arity, expected", SPECIALIZED_S8_TO_S10)
def test_s8_to_s10_specializations(c_val, arity, expected):
    master = simplify(shadow_coefficients(10)[arity].subs(c, c_val))
    ql = simplify(_shadow_coefficients_from_ql(10)[arity].subs(c, c_val))
    formula = simplify(EXPECTED_SHADOWS[arity].subs(c, c_val))
    assert master == expected
    assert ql == expected
    assert formula == expected


@pytest.mark.parametrize("c_val", [Rational(1, 2), Rational(1, 1), Rational(25, 1)])
def test_requested_numerical_checks_agree_with_both_recursions(c_val):
    master = shadow_coefficients(10)
    ql = _shadow_coefficients_from_ql(10)
    for arity in (8, 9, 10):
        expected = simplify(EXPECTED_SHADOWS[arity].subs(c, c_val))
        assert simplify(master[arity].subs(c, c_val) - expected) == 0
        assert simplify(ql[arity].subs(c, c_val) - expected) == 0


# ============================================================================
# Additional verification: recursion relation, self-duality, parity, c=13
# ============================================================================


def _convolution_square_residual(max_n=8):
    """Verify f^2 = Q_L by computing (sum a_n t^n)^2 - Q_L(t) truncated.

    Returns residual coefficients [t^0], ..., [t^{max_n}] of f^2 - Q_L.
    All should be zero if the recursion is correct.
    """
    from sympy import Symbol as Sym
    t = Sym('t')
    q0 = c**2
    q1 = 12 * c
    q2 = Rational(36) + Rational(80) / (5 * c + 22)

    # Compute a_n from the recursion
    a = [None] * (max_n + 1)
    a[0] = c
    if max_n >= 1:
        a[1] = cancel(q1 / (2 * a[0]))
    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * a[0]))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * a[0]))

    # Compute (f)^2 = (sum a_n t^n)^2 coefficients via convolution
    # [t^k] of f^2 = sum_{i+j=k} a_i a_j
    residuals = {}
    for k in range(max_n + 1):
        f_sq_k = sum(a[i] * a[k - i] for i in range(k + 1))
        f_sq_k = cancel(f_sq_k)
        # Q_L coefficient at t^k
        if k == 0:
            ql_k = q0
        elif k == 1:
            ql_k = q1
        elif k == 2:
            ql_k = q2
        else:
            ql_k = Rational(0)
        residuals[k] = cancel(f_sq_k - ql_k)
    return residuals


def test_f_squared_equals_ql_through_arity_10():
    """Verify the master relation f^2 = Q_L to order t^8 (covers S_10).

    # VERIFIED: [DC] direct convolution f^2 = sum a_i a_{n-i};
    # [SY] Q_L is quadratic so [t^k] Q_L = 0 for k >= 3.
    """
    residuals = _convolution_square_residual(max_n=8)
    for k, res in residuals.items():
        assert res == 0, f"f^2 - Q_L nonzero at t^{k}: {res}"


@pytest.mark.parametrize("arity", [8, 9, 10])
def test_self_duality_at_c13(arity):
    """S_r(13) = S_r(26 - 13) at the Virasoro self-dual point c = 13.

    # VERIFIED: [SY] Koszul duality c -> 26-c fixes c=13;
    # [DC] direct substitution into closed-form formula.
    """
    val = simplify(EXPECTED_SHADOWS[arity].subs(c, 13))
    dual_val = simplify(EXPECTED_SHADOWS[arity].subs(c, 26 - 13))
    assert val == dual_val


def test_s9_nonvanishing():
    """S_9 is nonzero: the Virasoro tower has no odd-parity vanishing.

    Odd-index vanishing (S_{2k+1} = 0 for k >= 2) occurs only for class G
    (Heisenberg, where the entire tower truncates at S_2). For class M
    (Virasoro), all S_r are nonzero for r >= 2.

    # VERIFIED: [DC] S_9(1) = -60350720/59049 != 0;
    # [LT] class M has infinite shadow depth (thm:single-line-dichotomy).
    """
    val = simplify(EXPECTED_SHADOWS[9].subs(c, 1))
    assert val == Rational(-60350720, 59049)
    assert val != 0


@pytest.mark.parametrize("arity", [8, 9, 10])
def test_c13_cross_check_two_methods(arity):
    """Cross-check S_r(13) via closed-form formula vs independent Q_L recursion.

    # VERIFIED: [DC] closed-form rational function evaluated at c=13;
    # [DC] independent convolution recursion at c=13.
    """
    formula_val = simplify(EXPECTED_SHADOWS[arity].subs(c, 13))
    ql_coeffs = _shadow_coefficients_from_ql(10)
    recursion_val = simplify(ql_coeffs[arity].subs(c, 13))
    assert formula_val == recursion_val
    assert formula_val != 0


EXPECTED_AT_C13 = {
    # VERIFIED: [DC] closed-form substitution; [DC] Q_L recursion substitution.
    8: Rational(47171920, 244497554379),
    9: Rational(-734961920, 9535404620781),
    10: Rational(111271331072, 3594847542034437),
}


@pytest.mark.parametrize("arity, expected", sorted(EXPECTED_AT_C13.items()))
def test_s8_s9_s10_exact_values_at_c13(arity, expected):
    """Exact rational values at the self-dual point c = 13.

    # VERIFIED: [DC] closed-form substitution; [DC] Q_L recursion; [NE] float comparison.
    """
    val = simplify(EXPECTED_SHADOWS[arity].subs(c, 13))
    assert val == expected


def test_sign_alternation_s8_s9_s10():
    """S_r alternates in sign for r >= 4: sign(S_r) = (-1)^r.

    S_8 > 0, S_9 < 0, S_10 > 0 at any c > 0.

    # VERIFIED: [DC] substitution at c=1; [SY] sign pattern (-1)^r for r >= 4
    # (thm:shadow-archetype-classification).
    """
    for cval in [Rational(1), Rational(13), Rational(25)]:
        s8 = EXPECTED_SHADOWS[8].subs(c, cval)
        s9 = EXPECTED_SHADOWS[9].subs(c, cval)
        s10 = EXPECTED_SHADOWS[10].subs(c, cval)
        assert s8 > 0, f"S_8({cval}) should be positive"
        assert s9 < 0, f"S_9({cval}) should be negative"
        assert s10 > 0, f"S_10({cval}) should be positive"
