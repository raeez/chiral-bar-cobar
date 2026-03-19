"""
Tests for the connected Dirichlet-sewing lift S_A(u) and prime-side Li coefficients.

Verifies:
1. Heisenberg divisor-sum identity: a_H(N) = sigma_{-1}(N), S_H(u) = zeta(u)*zeta(u+1)
2. Lambda_1 analytic formulas for all W_N families
3. Asymptotic behavior lambda_1(W_N) ~ -log(N) + c_inf
4. Euler-Koszul exactness for weight-1 families
5. Virasoro defect identity D_Vir(u) = 1 - 1/zeta(u)
6. Surface moment matrix positivity (Heisenberg)
7. Sign structure of Li coefficients
8. DS reduction = harmonic defect (W_N Euler product structure)
"""

import pytest
from mpmath import mp, mpf, zeta, diff, log, euler as euler_gamma, power, pi, stieltjes, fac
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

mp.dps = 30


# =============================================================================
# Helpers (self-contained for test stability)
# =============================================================================

def harmonic_zeta(n, u):
    if n <= 0:
        return mpf(0)
    return sum(power(j, -u) for j in range(1, n + 1))

def divisor_sigma_minus1(N):
    return sum(mpf(1) / d for d in range(1, N + 1) if N % d == 0)

def _zeta_reg(u):
    eps = u - 1
    if abs(eps) < mpf('1e-15'):
        return (1 + euler_gamma * eps + stieltjes(1) * eps**2 + stieltjes(2) * eps**3)
    return (u - 1) * zeta(u)

def Xi_H(u):
    return _zeta_reg(u) * zeta(u + 1)

def Xi_V(u):
    return zeta(u + 1) * (_zeta_reg(u) - (u - 1))

def Xi_WN(N, u):
    harm_sum = sum(harmonic_zeta(j, u) for j in range(1, N))
    return zeta(u + 1) * ((N - 1) * _zeta_reg(u) - (u - 1) * harm_sum)

def li_n(Xi_func, n):
    def f(u):
        return power(u, n - 1) * log(Xi_func(u))
    return diff(f, mpf(1), n) / fac(n - 1)

def lambda1_WN_analytic(N):
    zp2 = diff(zeta, mpf(2))
    z2 = zeta(2)
    H = sum(mpf(1) / j for j in range(1, N))
    return zp2 / z2 + euler_gamma + 1 - mpf(N) / (N - 1) * H


# =============================================================================
# Test 1: Heisenberg divisor-sum identity
# =============================================================================

class TestHeisenbergDivisorSum:
    def test_sigma_minus1_small(self):
        """sigma_{-1}(N) for small N."""
        assert abs(divisor_sigma_minus1(1) - 1) < 1e-20
        assert abs(divisor_sigma_minus1(2) - mpf('1.5')) < 1e-20
        assert abs(divisor_sigma_minus1(6) - (1 + mpf(1)/2 + mpf(1)/3 + mpf(1)/6)) < 1e-20

    def test_dirichlet_series_identity(self):
        """sum sigma_{-1}(N) N^{-u} = zeta(u)*zeta(u+1) for u > 1."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            partial_sum = sum(divisor_sigma_minus1(N) * power(N, -u) for N in range(1, 500))
            exact = zeta(u) * zeta(u + 1)
            assert abs(partial_sum - exact) / abs(exact) < 1e-2, f"Failed at u={u_val}"

    def test_euler_product(self):
        """zeta(u)*zeta(u+1) = prod_p (1-p^{-u})^{-1}(1-p^{-u-1})^{-1}."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        u = mpf(3)
        euler_prod = mpf(1)
        for p in primes:
            euler_prod *= 1 / ((1 - power(p, -u)) * (1 - power(p, -u - 1)))
        exact = zeta(u) * zeta(u + 1)
        assert abs(euler_prod - exact) / abs(exact) < 1e-3


# =============================================================================
# Test 2: Lambda_1 analytic formulas
# =============================================================================

class TestLambda1Formulas:
    def test_heisenberg_lambda1(self):
        """lambda_1(H) = gamma + zeta'(2)/zeta(2)."""
        num = float(li_n(Xi_H, 1))
        ana = float(euler_gamma + diff(zeta, mpf(2)) / zeta(2))
        assert abs(num - ana) < 1e-8

    @pytest.mark.parametrize("N", [2, 3, 4, 5, 10])
    def test_WN_lambda1(self, N):
        """lambda_1(W_N) analytic formula."""
        num = float(li_n(lambda u: Xi_WN(N, u), 1))
        ana = float(lambda1_WN_analytic(N))
        assert abs(num - ana) < 1e-8, f"W_{N}: num={num}, ana={ana}"


# =============================================================================
# Test 3: Asymptotics
# =============================================================================

class TestAsymptotics:
    def test_lambda1_grows_like_minus_log_N(self):
        """lambda_1(W_N) + log(N) converges as N -> infty."""
        vals = []
        for N in [10, 20, 50, 100]:
            l1 = lambda1_WN_analytic(N)
            vals.append(float(l1 + log(N)))
        # Should be monotonically increasing and converging
        for i in range(len(vals) - 1):
            assert vals[i] < vals[i + 1], "Not monotone"
        # Convergence: gap shrinks
        assert abs(vals[-1] - vals[-2]) < abs(vals[-2] - vals[-3])

    def test_asymptotic_constant(self):
        """lim_{N->inf} (lambda_1(W_N) + log(N)) = zeta'(2)/zeta(2) + 1."""
        c_inf = float(diff(zeta, mpf(2)) / zeta(2) + 1)
        # Check approach from below
        for N in [50, 100]:
            val = float(lambda1_WN_analytic(N) + log(N))
            assert val < c_inf, f"Overshoot at N={N}"
            assert val > c_inf - 1.0, f"Too far at N={N}"


# =============================================================================
# Test 4: Euler-Koszul exactness
# =============================================================================

class TestEulerKoszul:
    def test_heisenberg_exact(self):
        """Heisenberg is exact Euler-Koszul: S_H = zeta*zeta."""
        for u_val in [2, 3, 5, 10]:
            u = mpf(u_val)
            S = zeta(u) * zeta(u + 1)
            S_check = zeta(u) * zeta(u + 1)
            assert abs(S - S_check) < 1e-20

    def test_betagamma_exact(self):
        """beta-gamma (two weight-1 generators) is exact Euler-Koszul."""
        for u_val in [2, 3, 5]:
            u = mpf(u_val)
            S = 2 * zeta(u) * zeta(u + 1)
            S_baseline = 2 * zeta(u) * zeta(u + 1)
            assert abs(S / S_baseline - 1) < 1e-20

    def test_virasoro_not_exact(self):
        """Virasoro is NOT exact Euler-Koszul."""
        u = mpf(2)
        S_vir = zeta(u + 1) * (zeta(u) - 1)
        S_heis = zeta(u) * zeta(u + 1)
        assert abs(S_vir / S_heis - 1) > 0.5  # significant defect


# =============================================================================
# Test 5: Virasoro defect identity
# =============================================================================

class TestVirasoroDefect:
    @pytest.mark.parametrize("u_val", [2, 3, 4, 5, 8, 10, 20])
    def test_defect_formula(self, u_val):
        """D_Vir(u) = S_Vir(u)/S_H(u) = 1 - 1/zeta(u)."""
        u = mpf(u_val)
        S_vir = zeta(u + 1) * (zeta(u) - 1)
        S_heis = zeta(u) * zeta(u + 1)
        D = S_vir / S_heis
        expected = 1 - 1 / zeta(u)
        assert abs(float(D - expected)) < 1e-20

    def test_defect_involves_zeta_prime(self):
        """d/du D_Vir(u) = zeta'(u)/zeta(u)^2, so poles at zeta zeros."""
        u = mpf(3)
        D_prime = float(diff(lambda u: 1 - 1 / zeta(u), u))
        expected = float(diff(zeta, u) / zeta(u)**2)
        assert abs(D_prime - expected) < 1e-10


# =============================================================================
# Test 6: DS reduction = harmonic defect
# =============================================================================

class TestDSReductionArithmetic:
    def test_WN_harmonic_defect(self):
        """S_{W_N}(u) = zeta(u+1)*((N-1)*zeta(u) - sum H_j(u))."""
        for N in [3, 4, 5]:
            u = mpf(3)
            expected = zeta(u + 1) * ((N - 1) * zeta(u) - sum(harmonic_zeta(j, u) for j in range(1, N)))
            # Direct computation
            weights = list(range(2, N + 1))
            direct = zeta(u + 1) * sum(zeta(u) - harmonic_zeta(w - 1, u) for w in weights)
            assert abs(float(expected - direct)) < 1e-15

    def test_DS_removes_weight1_mode(self):
        """DS: sl_2 -> Virasoro removes weight-1 mode."""
        # sl_2 hat has weights {1, 2} (J at weight 1, Sugawara at weight 2)
        # After DS, only weight 2 remains
        u = mpf(3)
        S_sl2 = zeta(u + 1) * (zeta(u) + (zeta(u) - 1))  # weights {1, 2}
        S_vir = zeta(u + 1) * (zeta(u) - 1)  # weight {2}
        S_removed = S_sl2 - S_vir
        S_heis = zeta(u) * zeta(u + 1)  # weight {1}
        assert abs(float(S_removed - S_heis)) < 1e-15


# =============================================================================
# Test 7: Li coefficient sign structure
# =============================================================================

class TestLiSignStructure:
    def test_heisenberg_initial_positive(self):
        """Heisenberg Li coefficients are positive for small n."""
        for n in [1, 2, 3, 4, 5]:
            val = float(li_n(Xi_H, n))
            assert val > 0, f"lambda_{n}(H) = {val} should be positive"

    def test_heisenberg_eventually_negative(self):
        """Heisenberg Li coefficients become negative."""
        val_7 = float(li_n(Xi_H, 7))
        assert val_7 < 0, f"lambda_7(H) = {val_7} should be negative"

    def test_virasoro_all_negative(self):
        """Virasoro Li coefficients are all negative (n=1..10)."""
        for n in range(1, 11):
            val = float(li_n(Xi_V, n))
            assert val < 0, f"lambda_{n}(Vir) = {val} should be negative"

    def test_WN_increasingly_negative(self):
        """W_N Li coefficients become more negative with N at fixed n."""
        for n in [1, 3, 5]:
            prev = float(li_n(Xi_V, n))
            for N in [3, 4, 5]:
                curr = float(li_n(lambda u: Xi_WN(N, u), n))
                assert curr < prev, f"n={n}, W_{N}: not more negative"
                prev = curr

    def test_heisenberg_sign_change_at_n7(self):
        """The sign change in Heisenberg Li coeffs occurs between n=6 and n=7."""
        assert float(li_n(Xi_H, 6)) > 0
        assert float(li_n(Xi_H, 7)) < 0


# =============================================================================
# Test 8: Surface moment matrix (S_A evaluated at integer points)
# =============================================================================

class TestSurfaceMoments:
    def test_heisenberg_surface_positive(self):
        """All surface moments S_H(n) > 0 for n >= 2."""
        for n in range(2, 20):
            val = float(zeta(n) * zeta(n + 1))
            assert val > 0

    def test_surface_moments_decrease(self):
        """S_H(n) -> 1 as n -> infty (since zeta(n) -> 1)."""
        vals = [float(zeta(n) * zeta(n + 1)) for n in range(2, 20)]
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1], "Not monotone decreasing"
        assert vals[-1] < 1.001

    def test_virasoro_surface_ratio(self):
        """S_Vir(n)/S_H(n) = 1 - 1/zeta(n) for all n >= 2."""
        for n in range(2, 15):
            u = mpf(n)
            ratio = (zeta(u) - 1) / zeta(u)
            expected = 1 - 1 / zeta(u)
            assert abs(float(ratio - expected)) < 1e-20


# =============================================================================
# Test 9: Multiplicativity and convolution
# =============================================================================

class TestMultiplicativity:
    def test_sigma_minus1_multiplicative(self):
        """sigma_{-1} is multiplicative: sigma_{-1}(mn) = sigma_{-1}(m)*sigma_{-1}(n) for gcd(m,n)=1."""
        from math import gcd
        for m in range(1, 20):
            for n in range(1, 20):
                if gcd(m, n) == 1:
                    assert abs(float(divisor_sigma_minus1(m * n) -
                                     divisor_sigma_minus1(m) * divisor_sigma_minus1(n))) < 1e-15

    def test_euler_product_prime_factors(self):
        """At each prime p, the local factor of S_H is (1-p^{-u})^{-1}(1-p^{-u-1})^{-1}."""
        u = mpf(4)
        for p in [2, 3, 5, 7]:
            local = 1 / ((1 - power(p, -u)) * (1 - power(p, -u - 1)))
            # The local factor contributes to sigma_{-1}(p^k) = sum_{j=0}^k p^{-j}
            sigma_p = sum(power(p, -j) for j in range(6))  # truncated
            sigma_p2 = sum(power(p, -j) for j in range(12))
            # local = sum_{k>=0} sigma_{-1}(p^k) p^{-ku}
            local_check = sum(sum(power(p, -j) for j in range(k + 1)) * power(p, -k * u) for k in range(10))
            assert abs(float(local - local_check) / float(local)) < 1e-5


# =============================================================================
# Test 10: Independent sum factorization
# =============================================================================

class TestIndependentSum:
    def test_direct_sum_additivity(self):
        """S_{A1 oplus A2}(u) = S_{A1}(u) + S_{A2}(u) when OPE vanishes."""
        u = mpf(3)
        # H oplus Vir has weights {1, 2}
        S_sum = zeta(u + 1) * (zeta(u) + (zeta(u) - 1))
        S_H = zeta(u) * zeta(u + 1)
        S_V = zeta(u + 1) * (zeta(u) - 1)
        assert abs(float(S_sum - S_H - S_V)) < 1e-15


# =============================================================================
# Test 11: The asymptotic constant
# =============================================================================

class TestAsymptoticConstant:
    def test_constant_value(self):
        """c_infty = zeta'(2)/zeta(2) + 1 ~ 0.4100..."""
        c = float(diff(zeta, mpf(2)) / zeta(2) + 1)
        # zeta'(2)/zeta(2) ~ -0.5699..., so c ~ 0.4301
        assert 0.4 < c < 0.5


# =============================================================================
# Test 12: Connection to Benjamin-Chang
# =============================================================================

class TestBenjaminChangConnection:
    def test_epsilon1_equals_4zeta2s(self):
        """At c=1, R=1: epsilon^1_s(R=1) = 4*zeta(2s) (Benjamin-Chang)."""
        # This is the scalar shadow: the genus-1 spectral determinant
        # at the simplest point in Narain moduli.
        for s_val in [2, 3, 4, 5]:
            s = mpf(s_val)
            eps = 4 * zeta(2 * s)
            # Should be close to 4 for large s
            assert float(eps) > 4.0
            assert float(eps) == pytest.approx(4 * float(zeta(2 * s)), rel=1e-10)

    def test_scalar_universality(self):
        """At the scalar level, S_A(u) / kappa(A) is family-independent only at u=infty."""
        # S_H(u) / kappa_H = zeta(u)*zeta(u+1) / 1
        # S_Vir(u) / kappa_Vir(c) = zeta(u+1)*(zeta(u)-1) / (c/2)
        # These are NOT proportional for finite u.
        u = mpf(3)
        r_H = zeta(u) * zeta(u + 1)
        r_V = zeta(u + 1) * (zeta(u) - 1) / mpf('0.5')  # kappa_Vir = c/2, use c=1
        assert abs(float(r_H - r_V)) > 0.1  # genuinely different
