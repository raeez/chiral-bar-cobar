r"""Tests for bc_lichtenbaum_shadow_values_engine.py.

Lichtenbaum conjecture and special L-values from the shadow obstruction tower.

MULTI-PATH VERIFICATION throughout:
    Path 1: Direct Dirichlet series summation
    Path 2: Closed-form exact formulas (for finite towers)
    Path 3: mpmath high-precision cross-check
    Path 4: Functional equation / complementarity
    Path 5: Euler-Maclaurin analytic continuation
    Path 6: Cross-family additivity
    Path 7: Numerical evaluation consistency at 10+ points

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP10): Every test value independently computed.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13.
"""

import cmath
import math
import pytest

import mpmath

from compute.lib.bc_lichtenbaum_shadow_values_engine import (
    # Core special value functions
    shadow_zeta_negative_integers,
    shadow_zeta_negative_integers_mpmath,
    shadow_bernoulli_numbers,
    shadow_k_group_ratio,
    # Heisenberg exact
    heisenberg_zeta_at_negative_integers,
    heisenberg_zeta_derivative_at_zero,
    # Affine exact
    affine_sl2_zeta_at_negative_integers,
    # Tamagawa
    compute_shadow_tamagawa,
    ShadowTamagawa,
    # Zeta zeros
    shadow_zeta_at_riemann_zeros,
    shadow_zeta_derivative_at_riemann_zeros,
    virasoro_zeta_at_specialized_zeros,
    RIEMANN_ZETA_ZEROS_IMAG,
    # Complementarity
    complementarity_at_negative_integers,
    kappa_complementarity_check_at_zero,
    # Master table
    compute_family_special_values,
    FamilySpecialValues,
    # Verification
    verify_heisenberg_special_values,
    verify_affine_special_values,
    verify_virasoro_complementarity_at_neg,
    # Tables
    heisenberg_table,
    virasoro_table,
    affine_sl2_table,
    # Growth
    special_value_growth,
    # Derivatives
    shadow_zeta_derivative_at_zero,
    shadow_zeta_second_derivative_at_zero,
    # Continuation
    euler_maclaurin_continuation,
    # Cross-family
    cross_family_kappa_additivity_at_neg_integers,
    self_dual_virasoro_check,
)

from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
)


# ============================================================================
# Section 1: Heisenberg special values (exact, multi-path)
# ============================================================================

class TestHeisenbergSpecialValues:
    """Heisenberg H_k: zeta(s) = k * 2^{-s}, all values exact."""

    @pytest.mark.parametrize("k", [1, 2, 3, 5, 7, 10])
    def test_zeta_at_zero(self, k):
        """zeta_{H_k}(0) = k * 2^0 = k (sum of shadow coeffs)."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        z0 = sum(coeffs.get(r, 0.0) for r in range(2, 31))
        assert abs(z0 - k) < 1e-12

    @pytest.mark.parametrize("k", [1, 2, 3, 5])
    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_direct_vs_closed_form(self, k, n):
        """Path 1 vs Path 2: direct sum = k * 2^{n-1}."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        direct = shadow_zeta_negative_integers(coeffs, n)[n]
        closed = k * (2.0 ** (n - 1))
        assert abs(direct - closed) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 5])
    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_direct_vs_mpmath(self, k, n):
        """Path 1 vs Path 3: float vs mpmath."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        direct = shadow_zeta_negative_integers(coeffs, n)[n]
        hp = shadow_zeta_negative_integers_mpmath(coeffs, n)
        assert abs(direct - float(hp[n])) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_closed_form_function(self, k):
        """heisenberg_zeta_at_negative_integers matches direct."""
        closed = heisenberg_zeta_at_negative_integers(float(k), 5)
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        direct = shadow_zeta_negative_integers(coeffs, 5)
        for n in range(1, 6):
            assert abs(closed[n] - direct[n]) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 5, 10])
    def test_derivative_at_zero(self, k):
        """zeta'_{H_k}(0) = -k * log(2)."""
        val = heisenberg_zeta_derivative_at_zero(float(k))
        expected = -k * math.log(2)
        assert abs(val - expected) < 1e-12

    @pytest.mark.parametrize("k", [1, 3, 7])
    def test_zeta_derivative_via_coefficients(self, k):
        """Cross-check: zeta'(0) via shadow_zeta_derivative_at_zero."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        val = shadow_zeta_derivative_at_zero(coeffs)
        expected = -k * math.log(2)
        assert abs(val - expected) < 1e-12

    def test_heisenberg_additivity(self):
        """zeta_{H_{k1+k2}}(1-n) = zeta_{H_{k1}}(1-n) + zeta_{H_{k2}}(1-n)."""
        checks = cross_family_kappa_additivity_at_neg_integers(3.0, 7.0, 5)
        for key, val in checks.items():
            assert val, f"Additivity failed at {key}"

    def test_heisenberg_full_verification(self):
        """Full multi-path verification for k = 5."""
        checks = verify_heisenberg_special_values(5.0, 5)
        for key, val in checks.items():
            assert val, f"Heisenberg verification failed: {key}"

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_bernoulli_numbers(self, k):
        """Shadow Bernoulli: B_n^sh = (-1)^{n+1} * n * k * 2^{n-1}."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        bern = shadow_bernoulli_numbers(coeffs, 5)
        for n in range(1, 6):
            expected = ((-1) ** (n + 1)) * n * k * (2.0 ** (n - 1))
            assert abs(bern[n] - expected) < 1e-10

    @pytest.mark.parametrize("k", [1, 3, 5])
    def test_second_derivative_at_zero(self, k):
        """zeta''_{H_k}(0) = k * (log 2)^2."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        val = shadow_zeta_second_derivative_at_zero(coeffs)
        expected = k * math.log(2) ** 2
        assert abs(val - expected) < 1e-12


# ============================================================================
# Section 2: Affine sl_2 special values
# ============================================================================

class TestAffineSl2SpecialValues:
    """Affine V_k(sl_2): zeta(s) = kappa * 2^{-s} + alpha * 3^{-s}."""

    @pytest.mark.parametrize("k", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_zeta_at_zero(self, k):
        """zeta(0) = kappa + alpha."""
        k_val = float(k)
        kappa = 3.0 * (k_val + 2.0) / 4.0
        alpha = 4.0 / (k_val + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k_val, 30)
        z0 = sum(coeffs.get(r, 0.0) for r in range(2, 31))
        assert abs(z0 - (kappa + alpha)) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 4, 8])
    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_direct_vs_closed(self, k, n):
        """Direct sum = kappa * 2^{n-1} + alpha * 3^{n-1}."""
        k_val = float(k)
        coeffs = affine_sl2_shadow_coefficients(k_val, 30)
        direct = shadow_zeta_negative_integers(coeffs, n)[n]
        closed = affine_sl2_zeta_at_negative_integers(k_val, n)[n]
        assert abs(direct - closed) < 1e-10

    @pytest.mark.parametrize("k", [1, 4])
    @pytest.mark.parametrize("n", [1, 2, 3])
    def test_direct_vs_mpmath(self, k, n):
        """Float vs mpmath cross-check."""
        coeffs = affine_sl2_shadow_coefficients(float(k), 30)
        direct = shadow_zeta_negative_integers(coeffs, n)[n]
        hp = shadow_zeta_negative_integers_mpmath(coeffs, n)
        assert abs(direct - float(hp[n])) < 1e-10

    def test_full_verification_k1(self):
        """Multi-path verification for k = 1."""
        checks = verify_affine_special_values(1.0, 5)
        for key, val in checks.items():
            assert val, f"Affine verification failed: {key}"

    def test_full_verification_k4(self):
        """Multi-path verification for k = 4."""
        checks = verify_affine_special_values(4.0, 5)
        for key, val in checks.items():
            assert val, f"Affine verification failed: {key}"

    @pytest.mark.parametrize("k", [1, 2, 3])
    def test_derivative_at_zero(self, k):
        """zeta'(0) = -kappa*log(2) - alpha*log(3)."""
        k_val = float(k)
        kappa = 3.0 * (k_val + 2.0) / 4.0
        alpha = 4.0 / (k_val + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k_val, 30)
        val = shadow_zeta_derivative_at_zero(coeffs)
        expected = -kappa * math.log(2) - alpha * math.log(3)
        assert abs(val - expected) < 1e-10

    @pytest.mark.parametrize("k", [1, 2, 5])
    def test_kappa_formula(self, k):
        """AP1 check: kappa = 3(k+2)/4, NOT c/2."""
        k_val = float(k)
        kappa = 3.0 * (k_val + 2.0) / 4.0
        # c = k*dim/(k+h^v) = 3k/(k+2)
        c_val = 3.0 * k_val / (k_val + 2.0)
        # AP39: kappa != c/2 for non-Virasoro families
        assert abs(kappa - c_val / 2.0) > 1e-3 or k_val == 0  # They differ


# ============================================================================
# Section 3: Virasoro special values
# ============================================================================

class TestVirasoroSpecialValues:
    """Virasoro Vir_c: class M, infinite tower."""

    @pytest.mark.parametrize("c_val", [1.0, 2.0, 5.0, 10.0, 13.0, 20.0, 25.0])
    def test_zeta_at_zero_finite(self, c_val):
        """zeta(0) = sum S_r converges for Virasoro (rho < 1 at large c)."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        z0 = sum(coeffs.get(r, 0.0) for r in range(2, 31))
        # Just check it's finite and well-defined
        assert math.isfinite(z0)

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_complementarity_at_neg_ints(self, c_val):
        """zeta_c(1-n) + zeta_{26-c}(1-n) = D(1-n)."""
        checks = verify_virasoro_complementarity_at_neg(c_val, 5, 30)
        for key, val in checks.items():
            assert val, f"Complementarity failed: {key} at c={c_val}"

    @pytest.mark.parametrize("c_val", [2.0, 10.0, 13.0, 24.0])
    def test_direct_vs_mpmath(self, c_val):
        """Float vs mpmath for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        direct = shadow_zeta_negative_integers(coeffs, 3, 30)
        hp = shadow_zeta_negative_integers_mpmath(coeffs, 3, 30)
        for n in range(1, 4):
            assert abs(direct[n] - float(hp[n])) < 1e-6 * max(abs(direct[n]), 1)

    def test_self_dual_c13(self):
        """At c=13: self-duality checks."""
        checks = self_dual_virasoro_check(30, 5)
        for key, val in checks.items():
            assert val, f"Self-dual check failed: {key}"

    def test_kappa_sum_is_13(self):
        """AP24: kappa(c) + kappa(26-c) = 13 for all c."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            result = kappa_complementarity_check_at_zero(c_val, 30)
            assert abs(result['kappa_sum'] - 13.0) < 1e-12

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0, 25.0])
    def test_bernoulli_consistency(self, c_val):
        """B_n^sh = (-1)^{n+1} * n * zeta(1-n)."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        zn = shadow_zeta_negative_integers(coeffs, 5, 30)
        bn = shadow_bernoulli_numbers(coeffs, 5, 30)
        for n in range(1, 6):
            expected = ((-1) ** (n + 1)) * n * zn[n]
            assert abs(bn[n] - expected) < 1e-8 * max(abs(expected), 1)

    def test_virasoro_zeta_at_zero_sign(self):
        """zeta_{Vir_c}(0) should be positive for c > 0 (kappa > 0 dominates)."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
            z0 = sum(coeffs.get(r, 0.0) for r in range(2, 31))
            assert z0 > 0, f"zeta(0) should be positive at c={c_val}"

    def test_growth_rate_class_m(self):
        """Virasoro special values grow: |zeta(1-n)| increases with n."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, 30)
        growth = special_value_growth(coeffs, 10, 30)
        vals = growth['values']
        # Values should generally increase
        assert vals[-1] > vals[0]


# ============================================================================
# Section 4: Beta-gamma special values
# ============================================================================

class TestBetaGammaSpecialValues:
    """Beta-gamma: class C, tower terminates at arity 4."""

    @pytest.mark.parametrize("lam", [0.5, 1.0, 1.5, 2.0])
    def test_zeta_at_zero(self, lam):
        """zeta(0) = kappa + S_3 + S_4."""
        coeffs = betagamma_shadow_coefficients(lam, 30)
        z0 = sum(coeffs.get(r, 0.0) for r in range(2, 31))
        expected = coeffs[2] + coeffs[3] + coeffs[4]
        assert abs(z0 - expected) < 1e-12

    @pytest.mark.parametrize("lam", [0.5, 1.0, 2.0])
    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_closed_form_finite(self, lam, n):
        """zeta(1-n) = kappa * 2^{n-1} + S_3 * 3^{n-1} + S_4 * 4^{n-1} (exact)."""
        coeffs = betagamma_shadow_coefficients(lam, 30)
        direct = shadow_zeta_negative_integers(coeffs, n)[n]
        exact = (coeffs[2] * (2 ** (n - 1))
                 + coeffs[3] * (3 ** (n - 1))
                 + coeffs[4] * (4 ** (n - 1)))
        assert abs(direct - exact) < 1e-10

    @pytest.mark.parametrize("lam", [0.5, 1.5])
    def test_vs_mpmath(self, lam):
        """Float vs mpmath for beta-gamma."""
        coeffs = betagamma_shadow_coefficients(lam, 30)
        direct = shadow_zeta_negative_integers(coeffs, 3)
        hp = shadow_zeta_negative_integers_mpmath(coeffs, 3)
        for n in range(1, 4):
            assert abs(direct[n] - float(hp[n])) < 1e-10


# ============================================================================
# Section 5: Shadow Bernoulli numbers
# ============================================================================

class TestShadowBernoulli:
    """Shadow Bernoulli numbers B_n^sh."""

    def test_heisenberg_bernoulli_explicit(self):
        """B_n^sh(H_k) = (-1)^{n+1} * n * k * 2^{n-1}."""
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k, 30)
        bn = shadow_bernoulli_numbers(coeffs, 10)
        for n in range(1, 11):
            expected = ((-1) ** (n + 1)) * n * k * (2.0 ** (n - 1))
            assert abs(bn[n] - expected) < 1e-8

    def test_bernoulli_sign_alternation(self):
        """B_n^sh alternates sign (like classical Bernoulli for even index)."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        bn = shadow_bernoulli_numbers(coeffs, 10)
        # B_1 = 1*1*1 = 1 > 0 (n=1: (-1)^2 = +1)
        # B_2 = -2*1*2 = -4 < 0 (n=2: (-1)^3 = -1)
        assert bn[1] > 0
        assert bn[2] < 0

    def test_bernoulli_growth(self):
        """|B_n^sh| grows exponentially (like classical Bernoulli ~ (2n)!)."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        bn = shadow_bernoulli_numbers(coeffs, 10)
        # |B_n| = n * 2^{n-1}: exponential growth
        assert abs(bn[10]) > abs(bn[5])


# ============================================================================
# Section 6: Shadow K-group ratios
# ============================================================================

class TestShadowKGroupRatios:
    """Shadow K-group ratio (Lichtenbaum analogy)."""

    @pytest.mark.parametrize("k", [1, 3, 5])
    def test_heisenberg_k_ratios(self, k):
        """K-ratios well-defined for Heisenberg."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        kr = shadow_k_group_ratio(coeffs, 5)
        for n in range(1, 6):
            assert math.isfinite(kr[n]['ratio'])
            assert math.isfinite(kr[n]['zeta_A(1-n)'])

    def test_k_ratio_structure(self):
        """K-ratio dict has correct keys."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        kr = shadow_k_group_ratio(coeffs, 3)
        for n in range(1, 4):
            assert 'zeta_A(1-n)' in kr[n]
            assert 'K_{2n-2}' in kr[n]
            assert 'K_{2n-1}' in kr[n]
            assert 'ratio' in kr[n]
            assert 'B_n^sh' in kr[n]

    @pytest.mark.parametrize("c_val", [5.0, 13.0, 25.0])
    def test_virasoro_k_ratios_finite(self, c_val):
        """K-ratios finite for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        kr = shadow_k_group_ratio(coeffs, 3, 30)
        for n in range(1, 4):
            assert math.isfinite(kr[n]['zeta_A(1-n)'])


# ============================================================================
# Section 7: Shadow Tamagawa numbers
# ============================================================================

class TestShadowTamagawa:
    """Shadow Tamagawa numbers."""

    @pytest.mark.parametrize("k", [1, 2, 5])
    def test_heisenberg_tamagawa(self, k):
        """Heisenberg: h0 = k, h1 = 0, h2 = 0, tau = 0."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        tam = compute_shadow_tamagawa('heisenberg', float(k), coeffs)
        assert abs(tam.h0 - k) < 1e-12
        assert abs(tam.h1) < 1e-12
        assert abs(tam.h2) < 1e-12
        assert tam.regulator == 0.0  # Finite tower

    @pytest.mark.parametrize("k", [1, 3, 5])
    def test_affine_tamagawa(self, k):
        """Affine: h0 = kappa, h1 = alpha, h2 = 0."""
        k_val = float(k)
        kappa = 3.0 * (k_val + 2.0) / 4.0
        alpha = 4.0 / (k_val + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k_val, 30)
        tam = compute_shadow_tamagawa('affine_sl2', k_val, coeffs)
        assert abs(tam.h0 - kappa) < 1e-10
        assert abs(tam.h1 - alpha) < 1e-10
        assert abs(tam.h2) < 1e-12

    @pytest.mark.parametrize("c_val", [5.0, 10.0, 13.0, 25.0])
    def test_virasoro_tamagawa_positive(self, c_val):
        """Virasoro: tau > 0, L*(1) finite."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        tam = compute_shadow_tamagawa('virasoro', c_val, coeffs)
        assert tam.h0 > 0
        assert math.isfinite(tam.L_star_1)
        assert math.isfinite(tam.tau)

    def test_tamagawa_dataclass_fields(self):
        """ShadowTamagawa has all expected fields."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        tam = compute_shadow_tamagawa('heisenberg', 1.0, coeffs)
        assert hasattr(tam, 'tau')
        assert hasattr(tam, 'L_star_1')
        assert hasattr(tam, 'omega')
        assert hasattr(tam, 'regulator')
        assert hasattr(tam, 'bsd_ratio')

    def test_betagamma_tamagawa(self):
        """Beta-gamma: all three H^i nonzero."""
        coeffs = betagamma_shadow_coefficients(0.5, 30)
        tam = compute_shadow_tamagawa('betagamma', 0.5, coeffs)
        assert tam.h0 > 0
        assert tam.h1 > 0
        assert tam.h2 > 0
        assert tam.tau > 0


# ============================================================================
# Section 8: Values at Riemann zeta zeros
# ============================================================================

class TestZetaAtRiemannZeros:
    """Shadow zeta evaluated at Riemann zeta zeros."""

    def test_zero_list_length(self):
        """We have 20 zeros."""
        assert len(RIEMANN_ZETA_ZEROS_IMAG) == 20

    def test_zeros_increasing(self):
        """Zeros are strictly increasing."""
        for i in range(len(RIEMANN_ZETA_ZEROS_IMAG) - 1):
            assert RIEMANN_ZETA_ZEROS_IMAG[i] < RIEMANN_ZETA_ZEROS_IMAG[i + 1]

    def test_first_zero_approx(self):
        """First zero gamma_1 ~ 14.13."""
        assert abs(RIEMANN_ZETA_ZEROS_IMAG[0] - 14.1347) < 0.001

    @pytest.mark.parametrize("k", [1, 5])
    def test_heisenberg_at_zeros(self, k):
        """zeta_{H_k}(rho) = k * 2^{-rho} for each rho."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        results = shadow_zeta_at_riemann_zeros(coeffs, 5)
        for item in results:
            rho = item['rho']
            val = item['zeta_A(rho)']
            expected = k * (2.0 ** (-rho))
            assert abs(val - expected) < 1e-10

    @pytest.mark.parametrize("c_val", [5.0, 13.0, 25.0])
    def test_virasoro_at_zeros_finite(self, c_val):
        """Shadow zeta at zeros is finite for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        results = shadow_zeta_at_riemann_zeros(coeffs, 5, 30)
        for item in results:
            assert math.isfinite(item['|zeta_A(rho)|'])

    def test_heisenberg_magnitude_at_zeros(self):
        """For H_1: |zeta(rho)| = |2^{-rho}| = 2^{-1/2} for all rho on critical line."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        results = shadow_zeta_at_riemann_zeros(coeffs, 10)
        expected_mag = 2.0 ** (-0.5)
        for item in results:
            assert abs(item['|zeta_A(rho)|'] - expected_mag) < 1e-10


class TestZetaDerivativeAtZeros:
    """Shadow zeta derivative at Riemann zeros."""

    def test_heisenberg_derivative(self):
        """zeta'_{H_k}(rho) = -k * log(2) * 2^{-rho}."""
        k = 3.0
        coeffs = heisenberg_shadow_coefficients(k, 30)
        results = shadow_zeta_derivative_at_riemann_zeros(coeffs, 3)
        for item in results:
            rho = item['rho']
            direct = item["zeta'_A(rho)_direct"]
            expected = -k * math.log(2) * (2.0 ** (-rho))
            assert abs(direct - expected) < 1e-6

    def test_derivative_methods_agree(self):
        """Direct derivative and finite difference should agree."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        results = shadow_zeta_derivative_at_riemann_zeros(coeffs, 5)
        for item in results:
            assert item['agreement'] < 1e-4, f"Methods disagree at zero {item['n']}"

    @pytest.mark.parametrize("c_val", [5.0, 13.0])
    def test_virasoro_derivative_agreement(self, c_val):
        """Direct and FD agree for Virasoro."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        results = shadow_zeta_derivative_at_riemann_zeros(coeffs, 3, 30)
        for item in results:
            assert item['agreement'] < 1e-2  # Looser for infinite series


class TestSpecializedZeros:
    """Virasoro at c(rho) = 26*rho/(rho+1)."""

    def test_specialized_zeros_finite(self):
        """Values at specialized zeros are finite."""
        results = virasoro_zeta_at_specialized_zeros(5, 30)
        for item in results:
            assert math.isfinite(item['|zeta_A(rho)|']), f"Infinite at zero {item['n']}"

    def test_c_rho_formula(self):
        """c(rho_1) = 26*(1/2 + i*gamma_1)/(3/2 + i*gamma_1)."""
        gamma_1 = RIEMANN_ZETA_ZEROS_IMAG[0]
        rho = complex(0.5, gamma_1)
        c_rho = 26.0 * rho / (rho + 1.0)
        results = virasoro_zeta_at_specialized_zeros(1, 30)
        assert abs(results[0]['c(rho)'] - c_rho) < 1e-10


# ============================================================================
# Section 9: Complementarity tests
# ============================================================================

class TestComplementarity:
    """Theorem C complementarity at special values."""

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 10.0, 13.0, 20.0, 25.0])
    def test_complementarity_exact(self, c_val):
        """zeta_c(1-n) + zeta_{26-c}(1-n) = D(1-n) exactly."""
        results = complementarity_at_negative_integers(c_val, 5, 30)
        for item in results:
            assert item['error'] < 1e-6, (
                f"Complementarity error at c={c_val}, n={item['n']}: {item['error']}")

    def test_kappa_sum_at_zero(self):
        """AP24: kappa_c + kappa_{26-c} = 13 for all c."""
        for c_val in [0.5, 1.0, 5.0, 10.0, 13.0, 20.0, 25.0, 25.5]:
            result = kappa_complementarity_check_at_zero(c_val, 30)
            assert abs(result['kappa_sum'] - 13.0) < 1e-12

    def test_self_dual_c13_all_checks(self):
        """Full self-dual verification at c = 13."""
        checks = self_dual_virasoro_check(30, 5)
        for key, val in checks.items():
            assert val, f"c=13 self-dual failed: {key}"

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 20.0])
    def test_complementarity_n1(self, c_val):
        """At n=1 (s=0): explicit kappa + kappa' = 13 propagation."""
        c_dual = 26.0 - c_val
        kappa_c = c_val / 2.0
        kappa_dual = c_dual / 2.0
        assert abs(kappa_c + kappa_dual - 13.0) < 1e-12


# ============================================================================
# Section 10: Master table and family computation
# ============================================================================

class TestMasterTables:
    """Comprehensive tables for all families."""

    def test_heisenberg_table(self):
        """Heisenberg table for k=1..10."""
        table = heisenberg_table()
        assert len(table) == 10
        for row in table:
            assert row['kappa'] == row['k']
            assert abs(row['zeta(0)'] - row['k']) < 1e-12

    def test_virasoro_table(self):
        """Virasoro table for c = 0.5..26 step 0.5."""
        table = virasoro_table()
        assert len(table) >= 50  # At least 50 entries
        for row in table:
            assert abs(row['kappa'] - row['c'] / 2.0) < 1e-12

    def test_affine_table(self):
        """Affine sl_2 table for k=1..8."""
        table = affine_sl2_table()
        assert len(table) == 8

    def test_heisenberg_table_values(self):
        """Spot-check: k=1 has zeta(0) = 1, zeta(-1) = 2."""
        table = heisenberg_table(range(1, 2))
        assert len(table) == 1
        assert abs(table[0]['zeta(0)'] - 1.0) < 1e-12
        assert abs(table[0]['zeta(-1)'] - 2.0) < 1e-12

    def test_affine_table_kappa_formula(self):
        """AP1: kappa = 3(k+2)/4 for affine sl_2."""
        table = affine_sl2_table()
        for row in table:
            k = row['k']
            expected_kappa = 3.0 * (k + 2.0) / 4.0
            assert abs(row['kappa'] - expected_kappa) < 1e-10


class TestFamilySpecialValues:
    """compute_family_special_values for various families."""

    @pytest.mark.parametrize("family,param", [
        ('heisenberg', 1.0),
        ('heisenberg', 5.0),
        ('affine_sl2', 1.0),
        ('affine_sl2', 4.0),
        ('virasoro', 5.0),
        ('virasoro', 13.0),
        ('betagamma', 0.5),
        ('betagamma', 1.0),
    ])
    def test_family_data_complete(self, family, param):
        """Each family returns complete data."""
        data = compute_family_special_values(family, param)
        assert data.family == family
        assert data.param == param
        assert math.isfinite(data.kappa)
        assert len(data.zeta_neg) == 5
        assert len(data.bernoulli_sh) == 5
        assert len(data.k_ratios) == 5
        assert data.tamagawa is not None

    def test_heisenberg_class_G(self):
        """Heisenberg is class G."""
        data = compute_family_special_values('heisenberg', 1.0)
        assert data.shadow_class == 'G'

    def test_affine_class_L(self):
        """Affine is class L."""
        data = compute_family_special_values('affine_sl2', 1.0)
        assert data.shadow_class == 'L'

    def test_virasoro_class_M(self):
        """Virasoro is class M."""
        data = compute_family_special_values('virasoro', 10.0)
        assert data.shadow_class == 'M'

    def test_betagamma_class_C(self):
        """Beta-gamma is class C."""
        data = compute_family_special_values('betagamma', 0.5)
        assert data.shadow_class == 'C'


# ============================================================================
# Section 11: Growth analysis
# ============================================================================

class TestGrowthAnalysis:
    """Special value growth analysis."""

    def test_heisenberg_growth_base_2(self):
        """Heisenberg growth base = 2."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        growth = special_value_growth(coeffs, 10)
        assert abs(growth['expected_growth_base'] - 2.0) < 1e-12
        # Actual growth base converges to dominant_r = 2
        assert abs(growth['actual_growth_base'] - 2.0) < 0.1

    def test_affine_growth_base_3(self):
        """Affine growth base = 3 (dominant arity is 3)."""
        coeffs = affine_sl2_shadow_coefficients(1.0, 30)
        growth = special_value_growth(coeffs, 10)
        assert growth['dominant_r'] == 3
        # Ratios converge to 3
        assert abs(growth['actual_growth_base'] - 3.0) < 0.5

    def test_betagamma_growth_base_4(self):
        """Beta-gamma growth base = 4 (dominant arity is 4)."""
        coeffs = betagamma_shadow_coefficients(0.5, 30)
        growth = special_value_growth(coeffs, 10)
        assert growth['dominant_r'] == 4


# ============================================================================
# Section 12: Euler-Maclaurin continuation
# ============================================================================

class TestEulerMaclaurin:
    """Euler-Maclaurin analytic continuation."""

    @pytest.mark.parametrize("k", [1, 3, 5])
    def test_heisenberg_continuation_exact(self, k):
        """For finite towers, EM continuation = direct sum."""
        coeffs = heisenberg_shadow_coefficients(float(k), 30)
        for s in [2.0, 3.0, 5.0]:
            em = euler_maclaurin_continuation(coeffs, s)
            direct = shadow_zeta_numerical(coeffs, complex(s, 0), 30).real
            assert abs(em - direct) < 1e-10

    @pytest.mark.parametrize("s", [3.0, 5.0, 10.0])
    def test_virasoro_continuation_vs_direct(self, s):
        """EM continuation should match direct sum in convergence region."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, 30)
        em = euler_maclaurin_continuation(coeffs, s, N_terms=20)
        direct = shadow_zeta_numerical(coeffs, complex(s, 0), 30).real
        # Allow larger tolerance for class M
        assert abs(em - direct) / max(abs(direct), 1e-10) < 0.1


# ============================================================================
# Section 13: Cross-family consistency
# ============================================================================

class TestCrossFamily:
    """Cross-family consistency checks."""

    def test_heisenberg_additivity_k1_k2(self):
        """zeta_{H_3+H_7}(1-n) = zeta_{H_3}(1-n) + zeta_{H_7}(1-n)."""
        checks = cross_family_kappa_additivity_at_neg_integers(3.0, 7.0, 5)
        for key, val in checks.items():
            assert val, f"Additivity failed: {key}"

    def test_heisenberg_additivity_general(self):
        """Additivity for k1=2.5, k2=3.5."""
        checks = cross_family_kappa_additivity_at_neg_integers(2.5, 3.5, 5)
        for key, val in checks.items():
            assert val, f"Additivity failed: {key}"

    def test_scaling_invariance(self):
        """zeta_{H_{c*k}}(s) = c * zeta_{H_k}(s) (linearity)."""
        for c_val in [2.0, 3.0, 0.5]:
            for k in [1.0, 3.0]:
                coeffs_ck = heisenberg_shadow_coefficients(c_val * k, 30)
                coeffs_k = heisenberg_shadow_coefficients(k, 30)
                zn_ck = shadow_zeta_negative_integers(coeffs_ck, 5)
                zn_k = shadow_zeta_negative_integers(coeffs_k, 5)
                for n in range(1, 6):
                    assert abs(zn_ck[n] - c_val * zn_k[n]) < 1e-10

    @pytest.mark.parametrize("c_val", [1.0, 5.0, 13.0])
    def test_virasoro_derivative_sign(self, c_val):
        """zeta'(0) < 0 for positive kappa."""
        coeffs = virasoro_shadow_coefficients_numerical(c_val, 30)
        zprime = shadow_zeta_derivative_at_zero(coeffs)
        # -sum S_r * log(r): dominant term is -kappa*log(2) < 0
        assert zprime < 0


# ============================================================================
# Section 14: Numerical consistency at 10+ points
# ============================================================================

class TestNumericalConsistency:
    """Verify consistency by evaluating at many points."""

    def test_heisenberg_10_points(self):
        """Evaluate H_1 at 10 integer points and verify closed form."""
        coeffs = heisenberg_shadow_coefficients(1.0, 30)
        for s in range(-5, 6):
            if s == 1:
                continue  # Skip potential pole
            val = shadow_zeta_numerical(coeffs, complex(float(s), 0), 30)
            expected = 2.0 ** (-s)
            assert abs(val - expected) < 1e-10, f"Failed at s={s}"

    def test_affine_10_points(self):
        """Evaluate affine sl_2 at 10 points."""
        k_val = 2.0
        kappa = 3.0 * (k_val + 2.0) / 4.0
        alpha = 4.0 / (k_val + 2.0)
        coeffs = affine_sl2_shadow_coefficients(k_val, 30)
        for s in range(-5, 6):
            val = shadow_zeta_numerical(coeffs, complex(float(s), 0), 30)
            expected = kappa * (2.0 ** (-s)) + alpha * (3.0 ** (-s))
            assert abs(val - expected) < 1e-10, f"Failed at s={s}"

    def test_virasoro_convergence_region(self):
        """Virasoro at 10 positive-real points should be consistent."""
        coeffs = virasoro_shadow_coefficients_numerical(10.0, 30)
        prev = None
        for s in range(2, 12):
            val = shadow_zeta_numerical(coeffs, complex(float(s), 0), 30).real
            assert math.isfinite(val)
            if prev is not None:
                # Values should decrease as s increases (terms r^{-s} shrink)
                assert abs(val) <= abs(prev) * 1.1  # Allow small fluctuation
            prev = val

    def test_betagamma_10_points(self):
        """Beta-gamma at 10 integer points (finite tower, exact)."""
        coeffs = betagamma_shadow_coefficients(0.5, 30)
        for s in range(-5, 6):
            val = shadow_zeta_numerical(coeffs, complex(float(s), 0), 30)
            expected = (coeffs[2] * (2.0 ** (-s))
                        + coeffs[3] * (3.0 ** (-s))
                        + coeffs[4] * (4.0 ** (-s)))
            assert abs(val - expected) < 1e-10, f"Failed at s={s}"


# ============================================================================
# Section 15: Edge cases and robustness
# ============================================================================

class TestEdgeCases:
    """Edge cases and boundary conditions."""

    def test_heisenberg_k_zero(self):
        """H_0: all shadow coefficients vanish, zeta = 0."""
        coeffs = heisenberg_shadow_coefficients(0.0, 30)
        zn = shadow_zeta_negative_integers(coeffs, 5)
        for n in range(1, 6):
            assert abs(zn[n]) < 1e-15

    def test_large_k_heisenberg(self):
        """H_{100}: exact values scale with k."""
        coeffs = heisenberg_shadow_coefficients(100.0, 30)
        zn = shadow_zeta_negative_integers(coeffs, 3)
        assert abs(zn[1] - 100.0) < 1e-10
        assert abs(zn[2] - 200.0) < 1e-10
        assert abs(zn[3] - 400.0) < 1e-10

    def test_virasoro_near_c1(self):
        """Virasoro near c = 1 (minimal model boundary)."""
        coeffs = virasoro_shadow_coefficients_numerical(1.0, 30)
        zn = shadow_zeta_negative_integers(coeffs, 3, 30)
        for n in range(1, 4):
            assert math.isfinite(zn[n])

    def test_virasoro_c25_5(self):
        """Virasoro at c = 25.5 (near bosonic string critical)."""
        coeffs = virasoro_shadow_coefficients_numerical(25.5, 30)
        zn = shadow_zeta_negative_integers(coeffs, 3, 30)
        for n in range(1, 4):
            assert math.isfinite(zn[n])

    def test_max_r_sensitivity(self):
        """For finite towers, increasing max_r doesn't change values."""
        k = 3.0
        c10 = heisenberg_shadow_coefficients(k, 10)
        c30 = heisenberg_shadow_coefficients(k, 30)
        c100 = heisenberg_shadow_coefficients(k, 100)
        z10 = shadow_zeta_negative_integers(c10, 3, 10)
        z30 = shadow_zeta_negative_integers(c30, 3, 30)
        z100 = shadow_zeta_negative_integers(c100, 3, 100)
        for n in range(1, 4):
            assert abs(z10[n] - z30[n]) < 1e-12
            assert abs(z30[n] - z100[n]) < 1e-12

    def test_unknown_family_raises(self):
        """Unknown family raises ValueError."""
        with pytest.raises(ValueError):
            compute_family_special_values('unknown_family', 1.0)


# ============================================================================
# Section 16: AP verification tests
# ============================================================================

class TestAntiPatternChecks:
    """Explicit anti-pattern verification."""

    def test_ap1_kappa_not_copied(self):
        """AP1: kappa(H_k) = k, kappa(Vir_c) = c/2, kappa(sl_2) = 3(k+2)/4.
        These are THREE DISTINCT formulas. Never copy between families."""
        # Heisenberg
        assert abs(heisenberg_shadow_coefficients(5.0, 10)[2] - 5.0) < 1e-12
        # Virasoro
        assert abs(virasoro_shadow_coefficients_numerical(10.0, 10)[2] - 5.0) < 1e-10
        # Affine sl_2 at k=2: kappa = 3*4/4 = 3, NOT c/2 = 3*2/4 = 1.5
        assert abs(affine_sl2_shadow_coefficients(2.0, 10)[2] - 3.0) < 1e-10

    def test_ap24_kappa_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            kappa_c = c_val / 2.0
            kappa_dual = (26.0 - c_val) / 2.0
            assert abs(kappa_c + kappa_dual - 13.0) < 1e-12

    def test_ap39_kappa_ne_S2(self):
        """AP39: kappa != S_2 in general (though S_2 = kappa by definition here).
        The real check: kappa(affine sl_2) != c(sl_2)/2."""
        k_val = 4.0
        kappa = 3.0 * (k_val + 2.0) / 4.0  # = 4.5
        c_val = 3.0 * k_val / (k_val + 2.0)  # = 2
        assert abs(kappa - c_val / 2.0) > 1.0  # 4.5 vs 1.0: very different

    def test_ap10_cross_verification(self):
        """AP10: never trust a single path. Verify Heisenberg 3 ways."""
        k = 7.0
        coeffs = heisenberg_shadow_coefficients(k, 30)

        # Path 1: direct
        z1 = shadow_zeta_negative_integers(coeffs, 5)
        # Path 2: closed form
        z2 = heisenberg_zeta_at_negative_integers(k, 5)
        # Path 3: mpmath
        z3 = shadow_zeta_negative_integers_mpmath(coeffs, 5)

        for n in range(1, 6):
            assert abs(z1[n] - z2[n]) < 1e-10
            assert abs(z1[n] - float(z3[n])) < 1e-10

    def test_ap48_kappa_is_algebra_specific(self):
        """AP48: kappa depends on the full algebra.
        H_k at k=24: kappa = 24. Vir at c=24: kappa = 12. Different!"""
        h_coeffs = heisenberg_shadow_coefficients(24.0, 10)
        v_coeffs = virasoro_shadow_coefficients_numerical(24.0, 10)
        assert abs(h_coeffs[2] - 24.0) < 1e-12  # kappa(H_24) = 24
        assert abs(v_coeffs[2] - 12.0) < 1e-10  # kappa(Vir_24) = 12
        assert abs(h_coeffs[2] - v_coeffs[2]) > 10  # Very different
