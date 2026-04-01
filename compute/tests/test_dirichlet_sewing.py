#!/usr/bin/env python3
r"""
test_dirichlet_sewing.py -- Tests for Dirichlet-sewing lift, Miura defect, Li coefficients

T1-T8:   Dirichlet-sewing lift S_A(u) for standard families
T9-T16:  Euler product for Heisenberg
T17-T25: Miura defect D_N(q)
T26-T37: Li coefficients lambda_tilde_n(A)
T38-T44: DS kappa deficit and Miura connection
T45-T50: Cross-consistency and structural checks
T51-T55: Dirichlet coefficient verification
"""

import pytest
import math
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

try:
    from mpmath import mp, mpf, zeta, diff as mp_diff, log as mp_log, power, fac
    from mpmath import euler as euler_gamma, pi as mp_pi
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

skip_no_mpmath = pytest.mark.skipif(not HAS_MPMATH, reason="mpmath required")

from dirichlet_sewing import (
    # S_A(u)
    S_heisenberg, S_virasoro, S_affine_sl2, S_WN, S_generic,
    harmonic_zeta,
    # Euler product
    euler_product_heisenberg, euler_local_factor,
    euler_product_relative_error,
    # Virasoro defect
    virasoro_defect_ratio,
    # Miura defect
    miura_defect, miura_defect_exact, miura_defect_polynomial_degree,
    miura_defect_expanded, miura_defect_at_roots_of_unity,
    # Li coefficients
    Xi_heisenberg, Xi_virasoro, Xi_WN,
    li_coefficients, li_heisenberg, li_virasoro, li_WN,
    lambda1_heisenberg_analytic, lambda1_virasoro_analytic, lambda1_WN_analytic,
    # DS kappa deficit
    kappa_slN, kappa_WN, kappa_deficit, kappa_ghost_free,
    ds_kappa_deficit_vs_ghost,
    # Euler defect
    euler_defect_WN,
    # Dirichlet coefficients
    divisor_sigma_neg1, dirichlet_coefficients_heisenberg,
    dirichlet_coefficients_generic,
    # Verification
    verify_SH_equals_zeta_product, verify_W2_equals_virasoro,
    verify_ds_additivity, verify_dirichlet_series,
    verify_li_xi_consistency,
    # Tables
    sewing_lift_table, miura_defect_table,
)


# ============================================================================
# T1-T8: Dirichlet-sewing lift S_A(u) for standard families
# ============================================================================

class TestSewingLift:
    @skip_no_mpmath
    @pytest.mark.parametrize("u_val", [2, 3, 4, 5])
    def test_T1_heisenberg_equals_zeta_product(self, u_val):
        """T1: S_H(u) = zeta(u) * zeta(u+1)."""
        u = mpf(u_val)
        sh = S_heisenberg(u)
        exact = zeta(u) * zeta(u + 1)
        assert abs(float(sh - exact)) < 1e-20

    @skip_no_mpmath
    def test_T2_heisenberg_at_u2(self):
        """T2: S_H(2) = zeta(2)*zeta(3) = (pi^2/6)*zeta(3)."""
        u = mpf(2)
        val = float(S_heisenberg(u))
        expected = float(mp_pi**2 / 6 * zeta(3))
        assert abs(val - expected) / abs(expected) < 1e-15

    @skip_no_mpmath
    @pytest.mark.parametrize("u_val", [2, 3, 4, 5])
    def test_T3_virasoro_formula(self, u_val):
        """T3: S_Vir(u) = zeta(u+1)*(zeta(u) - 1)."""
        u = mpf(u_val)
        sv = S_virasoro(u)
        expected = zeta(u + 1) * (zeta(u) - 1)
        assert abs(float(sv - expected)) < 1e-20

    @skip_no_mpmath
    @pytest.mark.parametrize("u_val", [2, 3, 4, 5])
    def test_T4_affine_sl2_formula(self, u_val):
        """T4: S_{sl_2}(u) = zeta(u+1)*(2*zeta(u) - 1)."""
        u = mpf(u_val)
        s = S_affine_sl2(u)
        expected = zeta(u + 1) * (2 * zeta(u) - 1)
        assert abs(float(s - expected)) < 1e-20

    @skip_no_mpmath
    def test_T5_W2_equals_virasoro(self):
        """T5: S_{W_2}(u) = S_Vir(u) (Virasoro = W_2)."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            _, _, diff = verify_W2_equals_virasoro(u)
            assert float(diff) < 1e-20

    @skip_no_mpmath
    @pytest.mark.parametrize("N", [3, 4, 5])
    def test_T6_WN_formula(self, N):
        """T6: S_{W_N}(u) via explicit formula."""
        u = mpf(3)
        s = S_WN(N, u)
        harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
        expected = zeta(u + 1) * ((N - 1) * zeta(u) - harm_sum)
        assert abs(float(s - expected)) < 1e-15

    @skip_no_mpmath
    def test_T7_generic_weights(self):
        """T7: S_generic([1]) = S_H and S_generic([2]) = S_Vir."""
        u = mpf(3)
        assert abs(float(S_generic([1], u) - S_heisenberg(u))) < 1e-20
        assert abs(float(S_generic([2], u) - S_virasoro(u))) < 1e-20

    @skip_no_mpmath
    def test_T8_ds_additivity(self):
        """T8: S_{sl_2}(u) = S_H(u) + S_Vir(u) (weight additivity)."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            _, _, diff = verify_ds_additivity(u)
            assert float(diff) < 1e-15


# ============================================================================
# T9-T16: Euler product for Heisenberg
# ============================================================================

class TestEulerProduct:
    @skip_no_mpmath
    def test_T9_euler_product_u2(self):
        """T9: Euler product at u=2 converges to zeta(2)*zeta(3) = pi^2*zeta(3)/6."""
        u = mpf(2)
        ep = euler_product_heisenberg(u, n_primes=100)
        exact = zeta(2) * zeta(3)
        rel_err = abs(float((ep - exact) / exact))
        assert rel_err < 1e-3

    @skip_no_mpmath
    def test_T10_euler_product_u3(self):
        """T10: Euler product at u=3 converges well."""
        u = mpf(3)
        ep = euler_product_heisenberg(u, n_primes=50)
        exact = zeta(3) * zeta(4)
        rel_err = abs(float((ep - exact) / exact))
        assert rel_err < 1e-4

    @skip_no_mpmath
    @pytest.mark.parametrize("u_val", [4, 5, 10])
    def test_T11_euler_product_large_u(self, u_val):
        """T11: Euler product converges faster at larger u."""
        u = mpf(u_val)
        rel_err = float(euler_product_relative_error(u, n_primes=30))
        assert rel_err < 1e-5

    @skip_no_mpmath
    def test_T12_euler_local_factor_at_2(self):
        """T12: Local factor at p=2: (1-2^{-u})^{-1}(1-2^{-u-1})^{-1}."""
        u = mpf(3)
        lf = euler_local_factor(2, u)
        expected = 1 / ((1 - power(2, -u)) * (1 - power(2, -(u + 1))))
        assert abs(float(lf - expected)) < 1e-20

    @skip_no_mpmath
    def test_T13_euler_product_monotone_convergence(self):
        """T13: Adding more primes improves the Euler product."""
        u = mpf(3)
        err_20 = float(euler_product_relative_error(u, n_primes=20))
        err_50 = float(euler_product_relative_error(u, n_primes=50))
        assert err_50 < err_20

    @skip_no_mpmath
    def test_T14_euler_product_small_primes(self):
        """T14: Product over first 15 primes at u=3."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        u = mpf(3)
        ep = euler_product_heisenberg(u, primes=primes)
        exact = zeta(3) * zeta(4)
        rel_err = abs(float((ep - exact) / exact))
        assert rel_err < 1e-3

    @skip_no_mpmath
    def test_T15_local_factor_product_identity(self):
        """T15: Product of local factors = partial Euler product."""
        primes = [2, 3, 5, 7]
        u = mpf(4)
        product = mpf(1)
        for p in primes:
            product *= euler_local_factor(p, u)
        ep = euler_product_heisenberg(u, primes=primes)
        assert abs(float(product - ep)) < 1e-20

    @skip_no_mpmath
    def test_T16_euler_convergence_rate(self):
        """T16: Relative error decreases as u increases."""
        errs = []
        for u_val in [2, 3, 5, 10]:
            errs.append(float(euler_product_relative_error(mpf(u_val), n_primes=30)))
        for i in range(len(errs) - 1):
            assert errs[i] > errs[i + 1], "Error should decrease with u"


# ============================================================================
# T17-T25: Miura defect D_N(q)
# ============================================================================

class TestMiuraDefect:
    def test_T17_D2(self):
        """T17: D_2(q) = 1 - q."""
        assert miura_defect(2, Fraction(1, 2)) == Fraction(1, 2)
        assert miura_defect(2, 0) == 1
        assert miura_defect(2, 1) == 0

    def test_T18_D3_factored(self):
        """T18: D_3(q) = (1-q)(1-q^2) = (1-q)^2(1+q)."""
        q = Fraction(1, 2)
        d3 = miura_defect_exact(3, q)
        expected = (1 - q) * (1 - q**2)
        assert d3 == expected
        # Also check = (1-q)^2 (1+q)
        expected2 = (1 - q)**2 * (1 + q)
        assert d3 == expected2

    def test_T19_D3_values(self):
        """T19: D_3 at specific rational points."""
        assert miura_defect_exact(3, Fraction(1, 2)) == Fraction(3, 8)
        assert miura_defect_exact(3, Fraction(1, 3)) == Fraction(16, 27)

    def test_T20_DN_at_0(self):
        """T20: D_N(0) = 1 (normalization) for all N."""
        for N in range(2, 8):
            assert miura_defect(N, 0) == 1

    def test_T21_DN_at_1(self):
        """T21: D_N(1) = 0 for all N >= 2."""
        for N in range(2, 8):
            assert miura_defect(N, 1) == 0

    def test_T22_polynomial_degree(self):
        """T22: deg(D_N) = N*(N-1)/2."""
        assert miura_defect_polynomial_degree(2) == 1
        assert miura_defect_polynomial_degree(3) == 3
        assert miura_defect_polynomial_degree(4) == 6
        assert miura_defect_polynomial_degree(5) == 10

    def test_T23_expanded_D2(self):
        """T23: D_2(q) = 1 - q, coefficients [1, -1]."""
        coeffs = miura_defect_expanded(2)
        assert coeffs == [1, -1]

    def test_T24_expanded_D3(self):
        """T24: D_3(q) = 1 - q - q^2 + q^3, coefficients [1, -1, -1, 1]."""
        coeffs = miura_defect_expanded(3)
        assert coeffs == [1, -1, -1, 1]

    def test_T25_expanded_D4(self):
        """T25: D_4(q) = (1-q)(1-q^2)(1-q^3), degree 6."""
        coeffs = miura_defect_expanded(4)
        assert len(coeffs) == 7  # degree 6, so 7 coefficients
        assert coeffs[0] == 1  # leading coeff
        # Verify by evaluation at q = 1/2
        q = 0.5
        poly_val = sum(c * q**k for k, c in enumerate(coeffs))
        direct_val = miura_defect(4, q)
        assert abs(poly_val - direct_val) < 1e-12

    def test_T25b_D5_polynomial(self):
        """T25b: D_5(q) has degree 10."""
        coeffs = miura_defect_expanded(5)
        assert len(coeffs) == 11  # degree 10
        assert coeffs[0] == 1
        # Verify at q = 1/3
        q = Fraction(1, 3)
        poly_val = sum(Fraction(c) * q**k for k, c in enumerate(coeffs))
        direct_val = miura_defect_exact(5, q)
        assert poly_val == direct_val

    def test_T25c_DN_roots_of_unity(self):
        """T25c: D_N(1) = 0 via roots-of-unity evaluation."""
        for N in range(2, 6):
            val = miura_defect_at_roots_of_unity(N, 0)
            assert abs(val) < 1e-10, f"D_{N}(1) should be 0"


# ============================================================================
# T26-T37: Li coefficients
# ============================================================================

class TestLiCoefficients:
    @skip_no_mpmath
    def test_T26_heisenberg_lambda1_analytic(self):
        """T26: lambda_1(H) = gamma + zeta'(2)/zeta(2), analytic vs numerical."""
        mp.dps = 30
        lam_num = li_heisenberg(1)[0]
        lam_ana = lambda1_heisenberg_analytic()
        assert abs(float(lam_num - lam_ana)) < 1e-8

    @skip_no_mpmath
    def test_T27_virasoro_lambda1_analytic(self):
        """T27: lambda_1(Vir) = lambda_1(W_2), analytic vs numerical."""
        mp.dps = 30
        lam_num = li_virasoro(1)[0]
        lam_ana = lambda1_virasoro_analytic()
        assert abs(float(lam_num - lam_ana)) < 1e-8

    @skip_no_mpmath
    @pytest.mark.parametrize("N", [2, 3, 4, 5])
    def test_T28_WN_lambda1_analytic(self, N):
        """T28: lambda_1(W_N) analytic formula matches numerical."""
        mp.dps = 30
        lam_num = li_WN(N, 1)[0]
        lam_ana = lambda1_WN_analytic(N)
        assert abs(float(lam_num - lam_ana)) < 1e-8, f"W_{N} mismatch"

    @skip_no_mpmath
    def test_T29_heisenberg_positive_initial(self):
        """T29: Heisenberg Li coefficients are positive for n = 1,...,6."""
        mp.dps = 30
        lams = li_heisenberg(6)
        for n in range(6):
            assert float(lams[n]) > 0, f"lambda_{n+1}(H) should be positive"

    @skip_no_mpmath
    def test_T30_heisenberg_sign_change_at_7(self):
        """T30: lambda_7(H) < 0 (first sign change)."""
        mp.dps = 30
        lams = li_heisenberg(7)
        assert float(lams[5]) > 0, "lambda_6(H) should be positive"
        assert float(lams[6]) < 0, "lambda_7(H) should be negative"

    @skip_no_mpmath
    def test_T31_virasoro_all_negative(self):
        """T31: Virasoro Li coefficients are all negative for n = 1,...,8."""
        mp.dps = 30
        lams = li_virasoro(8)
        for n in range(8):
            assert float(lams[n]) < 0, f"lambda_{n+1}(Vir) should be negative"

    @skip_no_mpmath
    def test_T32_WN_increasingly_negative(self):
        """T32: At fixed n, lambda_n(W_N) decreases with N."""
        mp.dps = 30
        for n in [1, 3, 5]:
            prev = float(li_virasoro(n)[n - 1])  # W_2 = Virasoro
            for N in [3, 4, 5]:
                curr = float(li_WN(N, n)[n - 1])
                assert curr < prev, f"n={n}, W_{N}: not more negative"
                prev = curr

    @skip_no_mpmath
    def test_T33_li_xi_consistency_heisenberg(self):
        """T33: Li coefficients from two different computation paths agree."""
        mp.dps = 30
        for n in [1, 2, 3]:
            v1, v2 = verify_li_xi_consistency('heisenberg', n)
            assert abs(float(v1 - v2)) < 1e-8, f"n={n}: inconsistency"

    @skip_no_mpmath
    def test_T34_li_xi_consistency_virasoro(self):
        """T34: Li coefficients from two paths agree for Virasoro."""
        mp.dps = 30
        for n in [1, 2, 3]:
            v1, v2 = verify_li_xi_consistency('virasoro', n)
            assert abs(float(v1 - v2)) < 1e-8, f"n={n}: inconsistency"

    @skip_no_mpmath
    def test_T35_lambda1_asymptotics(self):
        """T35: lambda_1(W_N) + log(N) converges as N -> infinity."""
        mp.dps = 30
        vals = []
        for N in [10, 20, 50, 100]:
            l1 = lambda1_WN_analytic(N)
            vals.append(float(l1 + mp_log(N)))
        # Convergence: gaps shrink
        gaps = [abs(vals[i+1] - vals[i]) for i in range(len(vals) - 1)]
        for i in range(len(gaps) - 1):
            assert gaps[i + 1] < gaps[i], "Gap should shrink"

    @skip_no_mpmath
    def test_T36_asymptotic_constant(self):
        """T36: lim_{N->inf} (lambda_1(W_N) + log(N)) = zeta'(2)/zeta(2) + 1."""
        mp.dps = 30
        c_inf = float(mp_diff(zeta, mpf(2)) / zeta(2) + 1)
        # Should be approximately 0.43
        assert 0.4 < c_inf < 0.5
        # Check large N approaches from below
        for N in [50, 100]:
            val = float(lambda1_WN_analytic(N) + mp_log(N))
            assert val < c_inf

    @skip_no_mpmath
    def test_T37_lambda_n_growth(self):
        """T37: |lambda_n(H)| grows with n (broadly)."""
        mp.dps = 30
        lams = li_heisenberg(10)
        abs_vals = [abs(float(l)) for l in lams]
        # Not strictly monotone but trend is growth; check last > first
        assert abs_vals[-1] > abs_vals[0]


# ============================================================================
# T38-T44: DS kappa deficit and Miura connection
# ============================================================================

class TestKappaDeficit:
    def test_T38_kappa_sl2_formula(self):
        """T38: kappa(V_k(sl_2)) = 3(k+2)/4."""
        k = Fraction(1)
        assert kappa_slN(2, k) == Fraction(3 * (1 + 2), 4)

    def test_T39_kappa_sl3_formula(self):
        """T39: kappa(V_k(sl_3)) = 8(k+3)/6 = 4(k+3)/3."""
        k = Fraction(1)
        expected = Fraction(8 * (1 + 3), 6)
        assert kappa_slN(3, k) == expected

    def test_T40_kappa_deficit_sl2(self):
        """T40: DS kappa deficit for sl_2 at level k=1."""
        k = Fraction(1)
        deficit = kappa_deficit(2, k)
        ksl = kappa_slN(2, k)
        kw = kappa_WN(2, k)
        assert deficit == ksl - kw

    def test_T41_deficit_ne_ghost(self):
        """T41: DS kappa deficit != free-ghost kappa (AP1 check)."""
        for N in [3, 4, 5]:
            k = Fraction(1)
            result = ds_kappa_deficit_vs_ghost(N, k)
            # Difference should be nonzero in general
            # (they differ because BRST coupling breaks independent-sum)
            deficit = result['ds_deficit']
            ghost = result['free_ghost_kappa']
            # At generic level, these should differ for N >= 3
            if N >= 3:
                assert deficit != ghost, f"N={N}: deficit should differ from ghost kappa"

    def test_T42_ghost_kappa_values(self):
        """T42: Free-ghost kappa = N(N-1)/2."""
        assert kappa_ghost_free(2) == Fraction(1)
        assert kappa_ghost_free(3) == Fraction(3)
        assert kappa_ghost_free(4) == Fraction(6)
        assert kappa_ghost_free(5) == Fraction(10)

    def test_T43_critical_level_raises(self):
        """T43: kappa at critical level k = -N raises ValueError."""
        for N in [2, 3, 4]:
            with pytest.raises(ValueError):
                kappa_slN(N, Fraction(-N))

    def test_T44_deficit_k_dependent(self):
        """T44: DS deficit varies with level k."""
        for N in [2, 3, 4]:
            d1 = kappa_deficit(N, Fraction(1))
            d2 = kappa_deficit(N, Fraction(2))
            assert d1 != d2, f"N={N}: deficit should be k-dependent"


# ============================================================================
# T45-T50: Cross-consistency and structural checks
# ============================================================================

class TestCrossConsistency:
    @skip_no_mpmath
    def test_T45_virasoro_defect_identity(self):
        """T45: S_Vir(u)/S_H(u) = 1 - 1/zeta(u)."""
        mp.dps = 30
        for u_val in [2, 3, 4, 5, 8, 10]:
            u = mpf(u_val)
            ratio = S_virasoro(u) / S_heisenberg(u)
            expected = virasoro_defect_ratio(u)
            assert abs(float(ratio - expected)) < 1e-15

    @skip_no_mpmath
    def test_T46_euler_defect_decomposition(self):
        """T46: Euler-pure + defect = total for W_3."""
        u = mpf(3)
        pure, defect, total = euler_defect_WN(3, u)
        s_w3 = S_WN(3, u)
        assert abs(float(total - s_w3)) < 1e-15

    @skip_no_mpmath
    def test_T47_generic_equals_specialized(self):
        """T47: S_generic with W_3 weights matches S_WN(3, u)."""
        u = mpf(3)
        s_gen = S_generic([2, 3], u)
        s_w3 = S_WN(3, u)
        assert abs(float(s_gen - s_w3)) < 1e-15

    @skip_no_mpmath
    def test_T48_heisenberg_positive_real_axis(self):
        """T48: S_H(u) > 0 for all u > 1 on the real axis."""
        for u_val in [1.5, 2, 3, 5, 10, 20]:
            val = float(S_heisenberg(mpf(u_val)))
            assert val > 0, f"S_H({u_val}) should be positive"

    @skip_no_mpmath
    def test_T49_SH_limit(self):
        """T49: S_H(u) -> 1 as u -> infinity (since zeta(u) -> 1)."""
        val = float(S_heisenberg(mpf(30)))
        assert abs(val - 1.0) < 1e-5

    @skip_no_mpmath
    def test_T50_SVir_limit(self):
        """T50: S_Vir(u) -> 0 as u -> infinity."""
        val = float(S_virasoro(mpf(30)))
        assert abs(val) < 1e-5


# ============================================================================
# T51-T55: Dirichlet coefficient verification
# ============================================================================

class TestDirichletCoefficients:
    @skip_no_mpmath
    def test_T51_sigma_minus1_values(self):
        """T51: sigma_{-1}(N) at small N."""
        assert abs(float(divisor_sigma_neg1(1)) - 1.0) < 1e-15
        assert abs(float(divisor_sigma_neg1(2)) - 1.5) < 1e-15
        # sigma_{-1}(6) = 1 + 1/2 + 1/3 + 1/6 = 2
        assert abs(float(divisor_sigma_neg1(6)) - 2.0) < 1e-15
        # sigma_{-1}(12) = 1 + 1/2 + 1/3 + 1/4 + 1/6 + 1/12
        expected = 1 + 0.5 + 1/3 + 0.25 + 1/6 + 1/12
        assert abs(float(divisor_sigma_neg1(12)) - expected) < 1e-15

    @skip_no_mpmath
    def test_T52_sigma_minus1_multiplicative(self):
        """T52: sigma_{-1} is multiplicative for coprime arguments."""
        from math import gcd
        for m in range(1, 15):
            for n in range(1, 15):
                if gcd(m, n) == 1:
                    assert abs(float(
                        divisor_sigma_neg1(m * n) -
                        divisor_sigma_neg1(m) * divisor_sigma_neg1(n)
                    )) < 1e-15

    @skip_no_mpmath
    def test_T53_dirichlet_series_heisenberg(self):
        """T53: sum a_H(N) N^{-u} ~ zeta(u)*zeta(u+1) for u=3."""
        _, _, rel_err = verify_dirichlet_series([1], mpf(3), N_max=300)
        assert float(rel_err) < 1e-2

    @skip_no_mpmath
    def test_T54_generic_coefficients_weight2(self):
        """T54: Dirichlet coefficients for Virasoro (weight {2})."""
        coeffs = dirichlet_coefficients_generic([2], 6)
        # a_Vir(1) = 0 (no weight-1 contribution)
        assert abs(float(coeffs[0])) < 1e-15
        # a_Vir(2) = 1/1 = 1 (d=1, m=2, w=2<=2: count=1)
        assert abs(float(coeffs[1]) - 1.0) < 1e-15

    @skip_no_mpmath
    def test_T55_dirichlet_series_virasoro(self):
        """T55: sum a_Vir(N) N^{-u} ~ S_Vir(u) at u=3."""
        _, _, rel_err = verify_dirichlet_series([2], mpf(3), N_max=300)
        assert float(rel_err) < 5e-2


# ============================================================================
# Additional structural tests (T56-T60)
# ============================================================================

class TestStructural:
    def test_T56_miura_N_raises_for_1(self):
        """T56: miura_defect raises ValueError for N < 2."""
        with pytest.raises(ValueError):
            miura_defect(1, 0.5)

    def test_T57_WN_raises_for_N1(self):
        """T57: S_WN raises ValueError for N < 2."""
        if not HAS_MPMATH:
            pytest.skip("mpmath required")
        with pytest.raises(ValueError):
            S_WN(1, mpf(3))

    @skip_no_mpmath
    def test_T58_harmonic_zeta_limit(self):
        """T58: H_n(u) -> zeta(u) as n -> infinity."""
        u = mpf(3)
        H_1000 = harmonic_zeta(1000, u)
        z = zeta(u)
        assert abs(float(H_1000 - z)) / abs(float(z)) < 1e-3

    @skip_no_mpmath
    def test_T59_sewing_lift_table(self):
        """T59: Table generation produces correct structure."""
        table = sewing_lift_table([2, 3])
        assert 'Heisenberg' in table
        assert 'Virasoro' in table
        assert 2 in table['Heisenberg']
        assert 3 in table['Heisenberg']
        # Heisenberg at u=2 should be pi^2/6 * zeta(3)
        expected = float(mp_pi**2 / 6 * zeta(3))
        assert abs(table['Heisenberg'][2] - expected) / abs(expected) < 1e-10

    def test_T60_miura_defect_table(self):
        """T60: Miura defect table has correct structure."""
        table = miura_defect_table([0.0, 0.5, 1.0], [2, 3])
        assert table[2][0.0] == 1.0
        assert table[2][1.0] == 0.0
        assert table[3][0.0] == 1.0
        assert table[3][1.0] == 0.0
        assert abs(table[3][0.5] - 0.375) < 1e-10  # (1-0.5)(1-0.25) = 0.5*0.75


# ============================================================================
# Additional Miura defect tests (T61-T63)
# ============================================================================

class TestMiuraDefectAdvanced:
    def test_T61_D3_exact_factorization(self):
        """T61: D_3(q) = (1-q)^2(1+q) algebraically."""
        for q_val in [Fraction(1, 4), Fraction(1, 3), Fraction(2, 3)]:
            d3 = miura_defect_exact(3, q_val)
            factored = (1 - q_val)**2 * (1 + q_val)
            assert d3 == factored

    def test_T62_D4_at_half(self):
        """T62: D_4(1/2) = (1-1/2)(1-1/4)(1-1/8) = 1/2 * 3/4 * 7/8."""
        d4 = miura_defect_exact(4, Fraction(1, 2))
        expected = Fraction(1, 2) * Fraction(3, 4) * Fraction(7, 8)
        assert d4 == expected

    def test_T63_DN_near_1(self):
        """T63: D_N(q) ~ (1-q)^{N-1} * ... near q = 1."""
        # The leading behavior is (1-q)^{N-1} (since each factor vanishes at q=1)
        # But factors (1-q^j) vanish at q=1 only if j divides ... wait,
        # all factors (1-q^j) for j = 1,...,N-1 vanish at q=1.
        # So D_N(1-eps) ~ prod_{j=1}^{N-1} j*eps = (N-1)! * eps^{N-1} + O(eps^N).
        # Check: D_N(1-eps) / ((N-1)! * eps^{N-1}) -> 1 as eps -> 0.
        for N in [2, 3, 4, 5]:
            eps = 1e-6
            q = 1 - eps
            d_val = miura_defect(N, q)
            leading = math.factorial(N - 1) * eps**(N - 1)
            ratio = d_val / leading
            assert abs(ratio - 1.0) < 1e-2, f"N={N}: ratio={ratio}"
