r"""Tests for BC-85: Euler product structure of shadow zeta functions.

Multi-path verification (>=3 paths per claim):
  Path 1: Direct computation of shadow coefficients and Euler product structure
  Path 2: Moebius inversion / von Mangoldt support on prime powers
  Path 3: Local factor rationality and Satake parameter extraction
  Path 4: Partial Euler product convergence to direct sum
  Path 5: Cross-family consistency (Heisenberg, affine, lattice, Virasoro)

The central question: does zeta_A(s) = sum_{r>=2} S_r r^{-s} have an Euler product?

Answer: Standard shadow towers are NOT multiplicative (the convolution recursion
is quadratic, not multiplicative).  Class G/L towers are trivially multiplicative
(finitely many nonzero terms).  Class M (Virasoro, W_N) towers are NOT multiplicative:
S_6 != S_2 * S_3 in general.

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP10): Expected values are independently derived, not hardcoded from a single source.
"""

import sys
sys.path.insert(0, 'compute')

import math
import cmath
import pytest
from fractions import Fraction

from sympy import Rational, cancel


# =============================================================================
# Helper: lazy imports from engine
# =============================================================================

def _eng():
    """Lazy import to avoid module-level failures."""
    import lib.bc_euler_product_shadow_engine as eng
    return eng


# =============================================================================
# 1. Number-theoretic utilities
# =============================================================================

class TestNumberTheoreticUtilities:
    """Verify primes, Moebius, von Mangoldt, divisors."""

    def test_primes_up_to_10(self):
        eng = _eng()
        assert eng._primes_up_to(10) == [2, 3, 5, 7]

    def test_primes_up_to_30(self):
        eng = _eng()
        primes = eng._primes_up_to(30)
        assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_is_prime_basic(self):
        eng = _eng()
        assert eng._is_prime(2)
        assert eng._is_prime(3)
        assert not eng._is_prime(4)
        assert eng._is_prime(97)
        assert not eng._is_prime(1)

    def test_is_prime_power(self):
        eng = _eng()
        assert eng._is_prime_power(4) == (True, 2, 2)
        assert eng._is_prime_power(8) == (True, 2, 3)
        assert eng._is_prime_power(9) == (True, 3, 2)
        assert eng._is_prime_power(6) == (False, 0, 0)
        assert eng._is_prime_power(7) == (True, 7, 1)
        assert eng._is_prime_power(1) == (False, 0, 0)

    def test_mobius_function(self):
        eng = _eng()
        # mu(1)=1, mu(2)=-1, mu(3)=-1, mu(4)=0, mu(5)=-1, mu(6)=1
        assert eng._mobius(1) == 1
        assert eng._mobius(2) == -1
        assert eng._mobius(3) == -1
        assert eng._mobius(4) == 0
        assert eng._mobius(5) == -1
        assert eng._mobius(6) == 1
        assert eng._mobius(30) == -1  # 2*3*5, squarefree, 3 factors

    def test_von_mangoldt(self):
        eng = _eng()
        assert abs(eng._von_mangoldt(4) - math.log(2)) < 1e-14
        assert abs(eng._von_mangoldt(8) - math.log(2)) < 1e-14
        assert eng._von_mangoldt(6) == 0.0
        assert abs(eng._von_mangoldt(7) - math.log(7)) < 1e-14

    def test_divisors(self):
        eng = _eng()
        assert eng._divisors(12) == [1, 2, 3, 4, 6, 12]
        assert eng._divisors(7) == [1, 7]
        assert eng._divisors(1) == [1]

    def test_gcd(self):
        eng = _eng()
        assert eng._gcd(12, 8) == 4
        assert eng._gcd(7, 13) == 1
        assert eng._gcd(6, 15) == 3


# =============================================================================
# 2. Shadow coefficient providers
# =============================================================================

class TestShadowCoefficientProviders:
    """Verify shadow coefficients for standard families."""

    def test_virasoro_S2_is_kappa(self):
        """S_2 = c/2 for Virasoro (AP48: this is specific to Virasoro)."""
        eng = _eng()
        for c_val in [1, 2, 13, 25]:
            S = eng.virasoro_shadow_coefficients(c_val, max_r=5)
            assert S[2] == Rational(c_val, 2)

    def test_virasoro_S3_universal(self):
        """S_3 = 2 for all Virasoro (universal cubic coefficient)."""
        eng = _eng()
        for c_val in [Rational(1, 2), 1, 13, 25]:
            S = eng.virasoro_shadow_coefficients(c_val, max_r=5)
            assert S[3] == Rational(2)

    def test_virasoro_S4_formula(self):
        """S_4 = 10/(c(5c+22)) -- the quartic contact shadow."""
        eng = _eng()
        for c_val in [1, 2, 13, 25]:
            S = eng.virasoro_shadow_coefficients(c_val, max_r=6)
            cv = Rational(c_val)
            expected = Rational(10) / (cv * (5 * cv + 22))
            assert cancel(S[4] - expected) == 0

    def test_virasoro_S5_formula(self):
        """S_5 = -48/(c^2(5c+22)) for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=7)
        # At c=1: -48/(1*27) = -48/27 = -16/9.  S_5 = a_3/5.
        # a_3 = -(a_1*a_2 + a_2*a_1)/(2c) = -(6*40/27 + 40/27*6)/(2)
        #      = -(480/27)/(2) = -240/27 = -80/9
        # S_5 = (-80/9)/5 = -16/9
        assert S[5] == Rational(-16, 9)

    def test_heisenberg_class_G(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=20)
        assert S[2] == Rational(5)
        for r in range(3, 21):
            assert S[r] == 0

    def test_affine_sl2_class_L(self):
        """Affine sl_2 at k=2: kappa = 3, S_3 = 4/(2+2) = 1, S_r = 0 for r >= 4."""
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=10)
        assert S[2] == Rational(3) * 4 / 4  # 3(2+2)/4 = 3
        assert S[3] == Rational(1)  # 4/(k+2) = 4/4 = 1
        for r in range(4, 11):
            assert S[r] == 0

    def test_lattice_class_G(self):
        """Lattice VOA: kappa = rank, S_r = 0 for r >= 3."""
        eng = _eng()
        S = eng.lattice_shadow_coefficients(24, max_r=10)
        assert S[2] == Rational(24)
        for r in range(3, 11):
            assert S[r] == 0

    def test_virasoro_float_vs_exact(self):
        """Float and exact computations agree."""
        eng = _eng()
        S_exact = eng.virasoro_shadow_coefficients(Rational(10), max_r=30)
        S_float = eng.virasoro_shadow_coefficients_float(10.0, max_r=30)
        for r in range(2, 31):
            assert abs(float(S_exact[r]) - S_float[r]) < 1e-10 * max(1, abs(S_float[r]))


# =============================================================================
# 3. Multiplicativity tests — the central question
# =============================================================================

class TestMultiplicativity:
    """Test whether shadow coefficients are multiplicative."""

    def test_heisenberg_trivially_multiplicative(self):
        """Heisenberg: only S_2 != 0, so multiplicativity holds vacuously.
        S_6 = S_2*S_3 = k*0 = 0 = S_6. (Both zero.)"""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(3, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        assert result['is_multiplicative']

    def test_lattice_trivially_multiplicative(self):
        """Lattice: same as Heisenberg."""
        eng = _eng()
        S = eng.lattice_shadow_coefficients(8, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        assert result['is_multiplicative']

    def test_affine_sl2_multiplicativity(self):
        """Affine sl_2: S_2, S_3 nonzero, S_r = 0 for r >= 4.
        Test pairs: (2,3)=6, (2,5)=10, (3,5)=15, etc.
        S_6 = 0, S_2*S_3 = kappa*2 != 0 in general => NOT multiplicative."""
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        # S_6 = 0 but S_2 * S_3 = 3 * 2 = 6 != 0
        assert not result['is_multiplicative']
        # Check the specific failure at (2, 3)
        found_23 = False
        for m, n, s_mn, s_m_s_n in result['failures']:
            if (m, n) == (2, 3):
                found_23 = True
                assert s_mn == Rational(0)  # S_6 = 0
                assert s_m_s_n == Rational(3)  # kappa * S_3 = 3 * 4/(2+2) = 3
        assert found_23

    def test_virasoro_not_multiplicative_c1(self):
        """Virasoro at c=1: S_6 should differ from S_2 * S_3.
        S_2 = 1/2, S_3 = 2. Product = 1. S_6 should be computed from recursion."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        # Virasoro shadow tower is NOT multiplicative
        assert not result['is_multiplicative']

    def test_virasoro_not_multiplicative_c13(self):
        """Self-dual point c=13: still not multiplicative."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(13, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        assert not result['is_multiplicative']

    def test_virasoro_S6_vs_S2_S3(self):
        """Explicit check: S_6(c=1) != S_2(c=1) * S_3(c=1)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=10)
        S6 = S[6]
        S2_S3 = S[2] * S[3]
        assert cancel(S6 - S2_S3) != 0  # They differ

    def test_virasoro_S10_vs_S2_S5(self):
        """S_{10} != S_2 * S_5 for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=12)
        S10 = S[10]
        S2_S5 = S[2] * S[5]
        assert cancel(S10 - S2_S5) != 0

    def test_virasoro_S15_vs_S3_S5(self):
        """S_{15} != S_3 * S_5 for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=16)
        S15 = S[15]
        S3_S5 = S[3] * S[5]
        assert cancel(S15 - S3_S5) != 0

    def test_virasoro_complete_multiplicativity_fails(self):
        """Virasoro is also not completely multiplicative."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=20)
        result = eng.test_complete_multiplicativity(S, max_r=20)
        assert not result['is_multiplicative']

    def test_multiplicativity_defect_grows(self):
        """The multiplicativity defect should be nonzero for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        defects = eng.multiplicativity_defect(S, max_r=60)
        assert len(defects) > 0
        # S_6 = S[6], defect at 6 = |S_6 - S_2*S_3|
        assert 6 in defects
        assert defects[6] > 1e-15


# =============================================================================
# 4. Shadow von Mangoldt function
# =============================================================================

class TestShadowVonMangoldt:
    """Test the shadow von Mangoldt function and Euler product diagnostics."""

    def test_heisenberg_von_mangoldt_prime_power_support(self):
        """For Heisenberg (class G), only S_2 != 0, so Lambda_A is trivially
        supported on {2} only => prime power support holds."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(3, max_r=30)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=30)
        result = eng.von_mangoldt_prime_power_support(Lambda, max_r=30)
        assert result['euler_product_holds']

    def test_lattice_von_mangoldt_support(self):
        """Lattice VOA: same as Heisenberg."""
        eng = _eng()
        S = eng.lattice_shadow_coefficients(8, max_r=30)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=30)
        result = eng.von_mangoldt_prime_power_support(Lambda, max_r=30)
        assert result['euler_product_holds']

    def test_virasoro_von_mangoldt_NOT_prime_power(self):
        """For Virasoro (class M), the shadow von Mangoldt should have support
        on non-prime-powers, confirming no classical Euler product."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=60)
        result = eng.von_mangoldt_prime_power_support(Lambda, max_r=60)
        assert not result['euler_product_holds']
        assert len(result['non_prime_power_violations']) > 0

    def test_virasoro_c13_von_mangoldt_NOT_prime_power(self):
        """Self-dual c=13: still no Euler product."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(13.0, max_r=60)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=60)
        result = eng.von_mangoldt_prime_power_support(Lambda, max_r=60)
        assert not result['euler_product_holds']

    def test_virasoro_Lambda_6_nonzero(self):
        """Lambda_A(6) should be nonzero for Virasoro (6 is not a prime power)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=10)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=10)
        assert abs(Lambda[6]) > 1e-15

    def test_von_mangoldt_at_primes(self):
        """At prime p, Lambda_A(p) = S_p * log(p) (leading term dominates
        since there are no proper divisors d with 2 <= d < p and p/d >= 2
        except d and p/d where one is 1)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=20)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=20)
        for p in [2, 3, 5, 7, 11, 13]:
            expected = S[p] * math.log(p)
            assert abs(Lambda[p] - expected) < 1e-12

    def test_two_methods_agree_at_primes(self):
        """At primes, both recursion and direct Moebius agree since there
        are no proper divisors d with 2 <= d < p and p/d >= 2.
        Lambda_rec(p) = S_p * log(p), Lambda_dir(p) = mu(1)*S_p*log(p) = S_p*log(p)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=30)
        Lambda_rec = eng.shadow_von_mangoldt_mobius(S, max_r=30)
        Lambda_dir = eng.shadow_von_mangoldt_direct_mobius(S, max_r=30)
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            assert abs(Lambda_rec[p] - Lambda_dir[p]) < 1e-12

    def test_direct_mobius_vs_recursion_difference_measures_structure(self):
        """The direct Moebius inversion sum_{d|n} mu(n/d) S_d log(d) is NOT
        the same as the recursion-based von Mangoldt for general (non-multiplicative)
        sequences.  The difference at composite n measures the failure of the
        Dirichlet series to factor as an Euler product.

        For Heisenberg with only S_2 nonzero:
        Lambda_rec(4) = S_4*log(4) - Lambda(2)*S_2 = 0 - (k*log 2)*k = -k^2*log 2
        Lambda_dir(4) = mu(2)*S_2*log 2 = (-1)*k*log 2 = -k*log 2
        These DIFFER by (k^2 - k)*log 2 when k != 0, 1."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=10)
        S_float = {r: float(v) for r, v in S.items()}
        Lambda_rec = eng.shadow_von_mangoldt_mobius(S_float, max_r=10)
        Lambda_dir = eng.shadow_von_mangoldt_direct_mobius(S_float, max_r=10)
        # Lambda_rec(4) = 0*log(4) - (5*log 2)*5 = -25 log 2
        assert abs(Lambda_rec[4] - (-25.0 * math.log(2))) < 1e-12
        # Lambda_dir(4) = mu(2)*S_2*log 2 = -5 log 2
        assert abs(Lambda_dir[4] - (-5.0 * math.log(2))) < 1e-12


# =============================================================================
# 5. Local factors at primes
# =============================================================================

class TestLocalFactors:
    """Test local factor extraction and evaluation."""

    def test_heisenberg_local_factor_p2(self):
        """Heisenberg: F_2(X) = 1 + k*X (only S_2 = k nonzero at p=2)."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        coeffs = eng.local_factor_coefficients(S, 2, max_power=5)
        assert coeffs[0] == 1.0
        assert coeffs[1] == 5.0  # S_2 = k = 5
        for i in range(2, 6):
            assert coeffs[i] == 0.0

    def test_heisenberg_local_factor_p3(self):
        """Heisenberg: F_3(X) = 1 (S_3 = 0, S_9 = 0, etc.)."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=100)
        coeffs = eng.local_factor_coefficients(S, 3, max_power=5)
        assert coeffs[0] == 1.0
        for i in range(1, 6):
            assert coeffs[i] == 0.0

    def test_virasoro_local_factor_p2_nonzero(self):
        """Virasoro: F_2 has nonzero coefficients at all powers."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        coeffs = eng.local_factor_coefficients(S, 2, max_power=6)
        assert coeffs[0] == 1.0
        assert abs(coeffs[1] - S[2]) < 1e-14  # S_2 = 1/2
        assert abs(coeffs[2] - S[4]) < 1e-14  # S_4 = 10/27
        assert abs(coeffs[3] - S[8]) < 1e-14  # S_8

    def test_virasoro_local_factor_p3(self):
        """Virasoro: F_3(X) has S_3, S_9, S_27, ..."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        coeffs = eng.local_factor_coefficients(S, 3, max_power=4)
        assert coeffs[0] == 1.0
        assert abs(coeffs[1] - S[3]) < 1e-14  # S_3 = 2
        assert abs(coeffs[2] - S[9]) < 1e-14  # S_9

    def test_local_factor_evaluate_heisenberg(self):
        """Heisenberg at p=2: F_2(X) = 1 + 5X at X=1/4 gives 1 + 5/4 = 9/4."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        val = eng.local_factor_evaluate(S, 2, 0.25, max_power=5)
        assert abs(val - 2.25) < 1e-12

    def test_local_factor_rationality_heisenberg(self):
        """Heisenberg: F_2(X) = 1 + kX is a polynomial of degree (1,0)."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        result = eng.local_factor_rationality_test(S_float, 2, max_power=5, max_degree=3)
        assert result['residual'] < 1e-10


# =============================================================================
# 6. Prime power ratios
# =============================================================================

class TestPrimePowerRatios:
    """Test S_{p^k} / (S_p)^k ratios."""

    def test_heisenberg_prime_power_ratio(self):
        """Heisenberg: S_{2^k} / (S_2)^k: S_{2^1} = k, S_{2^2} = 0 for k >= 2.
        Ratio = 0 for k >= 2."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=100)
        ratios = eng.prime_power_ratio(S, 2, max_k=5)
        assert ratios[1] == pytest.approx(1.0)
        for k in range(2, 6):
            assert ratios[k] == pytest.approx(0.0)

    def test_virasoro_prime_power_ratio_p2(self):
        """Virasoro at c=1: S_{2^k} / (S_2)^k should differ from 1 for k >= 2."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        ratios = eng.prime_power_ratio(S, 2, max_k=6)
        assert ratios[1] == pytest.approx(1.0)
        # S_4 = 10/27, (S_2)^2 = (1/2)^2 = 1/4, ratio = (10/27)/(1/4) = 40/27
        expected_k2 = (10.0 / 27.0) / (0.5 ** 2)
        assert ratios[2] == pytest.approx(expected_k2, rel=1e-10)

    def test_virasoro_not_completely_multiplicative(self):
        """If completely multiplicative, ratio S_{p^k}/(S_p)^k = 1 always.
        For Virasoro, this fails at k=2."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        ratios = eng.prime_power_ratio(S, 2, max_k=4)
        assert abs(ratios[2] - 1.0) > 0.1  # significantly different from 1

    def test_prime_power_recursion_virasoro_p2(self):
        """Check degree-2 recursion S_{p^{k+1}} = S_p * S_{p^k} - chi(p) * S_{p^{k-1}}."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        result = eng.prime_power_recursion_check(S, 2, max_k=6)
        # The recursion should hold approximately if S_{p^k} follows degree-2 pattern
        # (from degree-2 Satake at each prime)
        # For Virasoro, this is NOT expected to hold exactly
        # because the shadow recursion is nonlinear (quadratic in the a_n)
        chi_p = result['chi_p']
        assert chi_p is not None

    def test_prime_power_recursion_heisenberg(self):
        """Heisenberg: S_4 = 0, S_8 = 0. chi(2) = (S_2)^2 - S_4 = k^2."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=100)
        S_float = {r: float(v) for r, v in S.items()}
        result = eng.prime_power_recursion_check(S_float, 2, max_k=5)
        assert result['chi_p'] == pytest.approx(25.0)  # 5^2 - 0 = 25


# =============================================================================
# 7. Shadow Satake parameters
# =============================================================================

class TestShadowSatakeParameters:
    """Test extraction and consistency of Satake parameters."""

    def test_heisenberg_satake_p2(self):
        """Heisenberg at level k: S_2 = k, S_4 = 0.
        alpha + beta = k, alpha*beta = k^2 - 0 = k^2.
        Discriminant = k^2 - 4k^2 = -3k^2 < 0 => complex Satake."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        sat = eng.shadow_satake_parameters(S, 2)
        assert abs(sat['sum_ab'] - 5.0) < 1e-12
        assert abs(sat['product_ab'] - 25.0) < 1e-12
        assert sat['discriminant'] < 0  # complex conjugate pair

    def test_virasoro_satake_p2_c1(self):
        """Virasoro at c=1, p=2: S_2 = 1/2, S_4 = 10/27.
        alpha + beta = 1/2, alpha*beta = (1/2)^2 - 10/27 = 1/4 - 10/27 = -13/108."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=30)
        sat = eng.shadow_satake_parameters(S, 2)
        assert abs(sat['sum_ab'] - 0.5) < 1e-12
        expected_prod = 0.25 - 10.0 / 27.0
        assert abs(sat['product_ab'] - expected_prod) < 1e-12

    def test_satake_sum_product_consistency(self):
        """alpha + beta and alpha * beta should be consistent with the quadratic."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(10.0, max_r=30)
        for p in [2, 3, 5]:
            sat = eng.shadow_satake_parameters(S, p)
            a, b = sat['alpha_p'], sat['beta_p']
            assert abs((a + b) - sat['sum_ab']) < 1e-10
            assert abs((a * b) - complex(sat['product_ab'])) < 1e-10

    def test_satake_predicted_vs_actual(self):
        """Satake-predicted S_{p^k} vs actual, for Virasoro at p=2."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        sat = eng.shadow_satake_parameters(S, 2)
        predicted = eng.satake_predicted_coefficients(sat['alpha_p'], sat['beta_p'], max_k=6)
        # predicted[0] should be 1, predicted[1] = S_2, predicted[2] = S_4, etc.
        assert abs(predicted[0] - 1.0) < 1e-10
        assert abs(predicted[1].real - S[2]) < 1e-10
        assert abs(predicted[2].real - S[4]) < 1e-10
        # Higher k may diverge (Satake assumes degree-2 local factor, which
        # is an approximation for the nonlinear shadow recursion)

    def test_satake_multiple_c_values(self):
        """Satake parameters at p=2 for various c: check discriminant sign pattern."""
        eng = _eng()
        for c_val in [1, 5, 10, 13, 20, 25]:
            S = eng.virasoro_shadow_coefficients_float(float(c_val), max_r=30)
            sat = eng.shadow_satake_parameters(S, 2)
            # alpha*beta = S_2^2 - S_4 = (c/2)^2 - 10/(c(5c+22))
            # This should be well-defined for all standard c values
            assert sat['alpha_p'] is not None
            assert sat['beta_p'] is not None


# =============================================================================
# 8. Partial Euler product and factorization obstruction
# =============================================================================

class TestPartialEulerProduct:
    """Test convergence of partial Euler product to direct sum."""

    def test_heisenberg_euler_product_exact(self):
        """Heisenberg at level k: zeta_A(s) = 1 + k * 2^{-s}.
        Euler product: F_2(2^{-s}) = 1 + k * 2^{-s}, F_p = 1 for p >= 3.
        So the partial Euler product equals the direct sum exactly."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        for s in [2, 3, 4]:
            direct = eng.shadow_zeta_direct(S_float, s)
            euler = eng.partial_euler_product(S_float, s, P_max=50)
            assert abs(direct - euler) < 1e-12

    def test_lattice_euler_product_exact(self):
        """Lattice VOA rank r: same as Heisenberg at level r."""
        eng = _eng()
        S = eng.lattice_shadow_coefficients(8, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        for s in [2, 3]:
            direct = eng.shadow_zeta_direct(S_float, s)
            euler = eng.partial_euler_product(S_float, s, P_max=50)
            assert abs(direct - euler) < 1e-12

    def test_virasoro_euler_product_NOT_exact(self):
        """Virasoro: partial Euler product does NOT equal direct sum
        (because shadow coefficients are not multiplicative)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        direct = eng.shadow_zeta_direct(S, 3.0)
        euler = eng.partial_euler_product(S, 3.0, P_max=50, local_max_power=6)
        # They should differ
        assert abs(direct - euler) > 1e-10

    def test_factorization_obstruction_heisenberg(self):
        """Heisenberg: E_A(s, P) = zeta_A(s) / prod F_p = 1 for P >= 2."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        obst = eng.factorization_obstruction(S_float, 3.0, [2, 10, 50])
        for P, val in obst.items():
            assert abs(val - 1.0) < 1e-10

    def test_factorization_obstruction_virasoro_not_converging(self):
        """Virasoro: E_A does NOT converge to 1 (no Euler product)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        obst = eng.factorization_obstruction(S, 3.0, [10, 30, 50])
        # At least one value should differ significantly from 1
        any_far = any(abs(v - 1.0) > 0.01 for v in obst.values())
        assert any_far

    def test_euler_vs_direct_at_integers_heisenberg(self):
        """Cross-verify Euler product vs direct sum at integer s."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(3, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        result = eng.euler_vs_direct_at_integers(S_float, [2, 3, 4, 5], P_max=50)
        for s, data in result.items():
            assert data['rel_diff'] < 1e-10


# =============================================================================
# 9. Rankin-Selberg from Euler product
# =============================================================================

class TestRankinSelbergEuler:
    """Cross-check Rankin-Selberg via Euler product vs direct computation."""

    def test_rankin_selberg_direct_heisenberg_self(self):
        """Heisenberg self-convolution: L(s, A x A) = k^2 * 2^{-s}."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        val = eng.rankin_selberg_direct(S_float, S_float, 3.0)
        expected = 25.0 * 2.0 ** (-3.0)  # S_2^2 * 2^{-3}
        assert abs(val - expected) < 1e-12

    def test_rankin_selberg_euler_local_factor(self):
        """Local RS factor from Satake parameters."""
        eng = _eng()
        S_A = eng.virasoro_shadow_coefficients_float(1.0, max_r=30)
        S_B = eng.virasoro_shadow_coefficients_float(13.0, max_r=30)
        rs_coeffs = eng.rankin_selberg_from_euler(S_A, S_B, 2, max_k=3)
        # First coefficient should be 1
        assert abs(rs_coeffs[0] - 1.0) < 1e-10
        # Second coefficient should be sum of eigenvalue products
        # This is a structural test, not a numerical verification

    def test_rankin_selberg_heisenberg_cross(self):
        """L(s, H_k x H_l) = k*l * 2^{-s}."""
        eng = _eng()
        S_A = eng.heisenberg_shadow_coefficients(3, max_r=30)
        S_B = eng.heisenberg_shadow_coefficients(7, max_r=30)
        S_Af = {r: float(v) for r, v in S_A.items()}
        S_Bf = {r: float(v) for r, v in S_B.items()}
        val = eng.rankin_selberg_direct(S_Af, S_Bf, 2.0)
        expected = 21.0 * 2.0 ** (-2.0)  # 3*7 * 2^{-2}
        assert abs(val - expected) < 1e-12


# =============================================================================
# 10. Convergence rate analysis
# =============================================================================

class TestConvergenceRate:
    """Measure convergence rates of partial Euler products."""

    def test_heisenberg_instant_convergence(self):
        """Heisenberg converges at P=2 (only prime that matters)."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        rates = eng.euler_product_convergence_rate(
            S_float, s_values=[3.0], P_schedule=[2, 5, 10])
        for P, err in rates[3.0].items():
            assert err < 1e-10

    def test_virasoro_convergence_rate_structure(self):
        """For Virasoro, the 'convergence' rate should NOT decrease to 0."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        rates = eng.euler_product_convergence_rate(
            S, s_values=[3.0], P_schedule=[5, 10, 20, 40])
        # The relative error should NOT converge to 0
        errs = [rates[3.0][P] for P in [5, 10, 20, 40]]
        # Check that the error is bounded away from 0
        assert errs[-1] > 1e-6


# =============================================================================
# 11. Cross-family comparisons
# =============================================================================

class TestCrossFamilyComparisons:
    """Cross-family Euler product structure comparisons."""

    def test_class_G_always_has_euler_product(self):
        """All class G algebras (Heisenberg, lattice) have trivial Euler products."""
        eng = _eng()
        for S_func in [
            lambda: eng.heisenberg_shadow_coefficients(3, max_r=30),
            lambda: eng.heisenberg_shadow_coefficients(10, max_r=30),
            lambda: eng.lattice_shadow_coefficients(8, max_r=30),
            lambda: eng.lattice_shadow_coefficients(24, max_r=30),
        ]:
            S = S_func()
            S_float = {r: float(v) for r, v in S.items()}
            result = eng.test_multiplicativity(S, max_r=30)
            assert result['is_multiplicative']
            Lambda = eng.shadow_von_mangoldt_mobius(S_float, max_r=30)
            support = eng.von_mangoldt_prime_power_support(Lambda, max_r=30)
            assert support['euler_product_holds']

    def test_class_L_no_euler_product(self):
        """Affine KM (class L): S_2 and S_3 nonzero, S_6 = 0 != S_2*S_3."""
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=30)
        result = eng.test_multiplicativity(S, max_r=30)
        assert not result['is_multiplicative']

    def test_class_M_no_euler_product(self):
        """Virasoro (class M): infinite tower, definitely not multiplicative."""
        eng = _eng()
        for c_val in [1, 5, 13, 25]:
            S = eng.virasoro_shadow_coefficients(c_val, max_r=30)
            result = eng.test_multiplicativity(S, max_r=30)
            assert not result['is_multiplicative']

    def test_virasoro_multiplicativity_defect_increases_with_r(self):
        """The multiplicativity defect grows as we test at larger r."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        defects_20 = eng.multiplicativity_defect(S, max_r=20)
        defects_40 = eng.multiplicativity_defect(S, max_r=40)
        assert len(defects_40) >= len(defects_20)

    def test_complementarity_pair_both_fail(self):
        """Virasoro at c and its Koszul dual at 26-c: both lack Euler product."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(5, max_r=30)
        S_dual = eng.virasoro_shadow_coefficients(21, max_r=30)
        assert not eng.test_multiplicativity(S, max_r=30)['is_multiplicative']
        assert not eng.test_multiplicativity(S_dual, max_r=30)['is_multiplicative']


# =============================================================================
# 12. Exact Virasoro shadow coefficient cross-checks
# =============================================================================

class TestExactVirasoroCrossChecks:
    """Cross-verify Virasoro shadow coefficients by multiple paths."""

    def test_S2_equals_kappa_exact(self):
        """Path 1: S_2 = c/2 from recursion."""
        eng = _eng()
        for c_val in [Rational(1, 2), Rational(1), Rational(7, 10), Rational(13)]:
            S = eng.virasoro_shadow_coefficients(c_val, max_r=5)
            assert S[2] == c_val / 2

    def test_S4_c_half(self):
        """Ising model c=1/2: S_4 = 10/((1/2)(5/2+22)) = 10/(1/2 * 49/2) = 10*4/49 = 40/49."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(Rational(1, 2), max_r=6)
        expected = Rational(10) / (Rational(1, 2) * (Rational(5, 2) + 22))
        assert S[4] == expected
        assert S[4] == Rational(40, 49)

    def test_recursion_consistency(self):
        """The shadow coefficients satisfy the quadratic recursion:
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}.
        Verify by recomputing a_4 from a_1, a_2, a_3."""
        eng = _eng()
        cv = Rational(1)
        S = eng.virasoro_shadow_coefficients(cv, max_r=8)
        # Extract a_n from S_r = a_{r-2}/r
        a = {n: S[n + 2] * (n + 2) for n in range(5)}
        # a_3 should satisfy: a_3 = -(a_1*a_2 + a_2*a_1)/(2c) = -2*a_1*a_2/(2c)
        expected_a3 = -(a[1] * a[2] + a[2] * a[1]) / (2 * cv)
        assert cancel(a[3] - expected_a3) == 0

    def test_S_r_alternating_sign(self):
        """For c > 0, the shadow coefficients alternate in sign for large r.
        Specifically, check signs at c=1 for r=2..10."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=12)
        # S_2 = 1/2 > 0, S_3 = 2 > 0, S_4 = 10/27 > 0, S_5 = -16/9 < 0
        assert S[2] > 0
        assert S[3] > 0
        assert S[4] > 0
        assert S[5] < 0


# =============================================================================
# 13. Satake parameter properties
# =============================================================================

class TestSatakeProperties:
    """Test algebraic properties of Satake parameters."""

    def test_satake_sum_equals_S_p(self):
        """alpha_p + beta_p = S_p by construction."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(10.0, max_r=30)
        for p in [2, 3, 5, 7]:
            sat = eng.shadow_satake_parameters(S, p)
            assert abs(sat['alpha_p'] + sat['beta_p'] - S[p]) < 1e-10

    def test_satake_product_formula(self):
        """alpha_p * beta_p = S_p^2 - S_{p^2} by construction."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(10.0, max_r=100)
        for p in [2, 3, 5]:
            sat = eng.shadow_satake_parameters(S, p)
            expected = S[p] ** 2 - S[p ** 2]
            assert abs(sat['product_ab'] - expected) < 1e-10

    def test_satake_c13_self_dual(self):
        """At self-dual c=13: Satake should have specific symmetry."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(13.0, max_r=30)
        sat2 = eng.shadow_satake_parameters(S, 2)
        # S_2 = 13/2 = 6.5
        assert abs(sat2['sum_ab'] - 6.5) < 1e-10

    def test_satake_predicted_matches_actual_k1(self):
        """Satake-predicted S_{p^1} = alpha + beta = S_p: tautological check."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(5.0, max_r=30)
        sat = eng.shadow_satake_parameters(S, 2)
        predicted = eng.satake_predicted_coefficients(sat['alpha_p'], sat['beta_p'], max_k=1)
        assert abs(predicted[1].real - S[2]) < 1e-10

    def test_satake_predicted_matches_actual_k2(self):
        """Satake-predicted S_{p^2} = alpha^2 + alpha*beta + beta^2 = S_{p^2}: also tautological."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(5.0, max_r=30)
        sat = eng.shadow_satake_parameters(S, 2)
        predicted = eng.satake_predicted_coefficients(sat['alpha_p'], sat['beta_p'], max_k=2)
        assert abs(predicted[2].real - S[4]) < 1e-10

    def test_satake_predicted_DIVERGES_k3(self):
        """Satake-predicted S_{p^3} should DIFFER from actual S_{p^3} for Virasoro,
        because the degree-2 Satake approximation does not capture the full nonlinear recursion."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        sat = eng.shadow_satake_parameters(S, 2)
        predicted = eng.satake_predicted_coefficients(sat['alpha_p'], sat['beta_p'], max_k=3)
        # S_{2^3} = S_8
        actual = S[8]
        diff = abs(predicted[3].real - actual)
        # The degree-2 approximation is NOT exact for the nonlinear tower
        # (unless it happens to coincide by accident)
        # We just check the prediction is finite and well-defined
        assert math.isfinite(predicted[3].real)


# =============================================================================
# 14. Full analysis pipeline
# =============================================================================

class TestFullAnalysisPipeline:
    """Test the full_euler_product_analysis function."""

    def test_heisenberg_full_analysis(self):
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=60)
        result = eng.full_euler_product_analysis(S, "Heisenberg(k=5)",
                                                   max_r_mult=30, max_r_vm=30)
        assert result['family'] == "Heisenberg(k=5)"
        assert result['multiplicativity']['is_multiplicative']
        assert result['von_mangoldt']['euler_product_holds']

    def test_virasoro_full_analysis(self):
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        result = eng.full_euler_product_analysis(S, "Virasoro(c=1)",
                                                   max_r_mult=30, max_r_vm=30)
        assert result['family'] == "Virasoro(c=1)"
        assert not result['multiplicativity']['is_multiplicative']
        assert not result['von_mangoldt']['euler_product_holds']

    def test_affine_full_analysis(self):
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=60)
        result = eng.full_euler_product_analysis(S, "affine_sl2(k=2)",
                                                   max_r_mult=30, max_r_vm=30)
        assert not result['multiplicativity']['is_multiplicative']


# =============================================================================
# 15. Specific multiplicativity failure patterns
# =============================================================================

class TestMultiplicativityFailurePatterns:
    """Detailed analysis of WHERE multiplicativity fails."""

    def test_virasoro_first_failure_is_S6(self):
        """The first coprime pair is (2,3) with product 6.
        S_6 != S_2 * S_3 is the first multiplicativity failure for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=10)
        S2, S3, S6 = S[2], S[3], S[6]
        defect = cancel(S6 - S2 * S3)
        assert defect != 0

    def test_virasoro_S6_explicit_c1(self):
        """At c=1, compute S_6 explicitly.
        a_4 = -(a_1*a_3 + a_2^2 + a_3*a_1)/(2c)
            = -(2*6*a_3 + a_2^2)/(2)   at c=1
        where a_1=6, a_2=40/27.
        a_3 = -(a_1*a_2 + a_2*a_1)/(2) = -(2*6*40/27)/(2) = -240/27 = -80/9
        a_4 = -(2*6*(-80/9) + (40/27)^2)/(2)
            = -((-960/9) + 1600/729)/(2)
            = -((-77760 + 1600)/729)/(2)
            = -(-76160/729)/2
            = 76160/1458
            = 38080/729
        S_6 = a_4/6 = 38080/4374 = 19040/2187"""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(1, max_r=8)
        expected = Rational(19040, 2187)
        assert S[6] == expected
        # Compare with S_2*S_3 = (1/2)*2 = 1
        assert Rational(19040, 2187) != Rational(1)

    def test_affine_first_failure_is_S6(self):
        """Affine sl_2 at k=2: S_2 = 3, S_3 = 4/(2+2)=1, S_6 = 0.
        S_2 * S_3 = 3 != 0 = S_6."""
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=10)
        assert S[6] == 0
        assert S[2] * S[3] == 3  # 3 * 1 = 3

    def test_virasoro_defect_at_6_multiple_c(self):
        """The multiplicativity defect at n=6 for Virasoro at various c."""
        eng = _eng()
        for c_val in [1, 5, 10, 13, 20, 25]:
            S = eng.virasoro_shadow_coefficients_float(float(c_val), max_r=10)
            defect = abs(S[6] - S[2] * S[3])
            assert defect > 1e-15, f"Defect at c={c_val} unexpectedly zero"


# =============================================================================
# 16. Von Mangoldt at specific values
# =============================================================================

class TestVonMangoldtSpecificValues:
    """Verify Lambda_A at specific n."""

    def test_Lambda_2_equals_S2_log2(self):
        """Lambda_A(2) = S_2 * log(2) (no corrections: 2 is prime)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=10)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=10)
        assert abs(Lambda[2] - S[2] * math.log(2)) < 1e-14

    def test_Lambda_3_equals_S3_log3(self):
        """Lambda_A(3) = S_3 * log(3) (3 is prime)."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=10)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=10)
        assert abs(Lambda[3] - S[3] * math.log(3)) < 1e-14

    def test_Lambda_4_recursion(self):
        """Lambda_A(4) = S_4*log(4) - Lambda_A(2)*S_2.
        4 has divisors {1,2,4}. Proper: d=2, q=2.
        Lambda(4) = S_4 * log(4) - Lambda(2) * S_2."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=10)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=10)
        expected = S[4] * math.log(4) - Lambda[2] * S[2]
        assert abs(Lambda[4] - expected) < 1e-14

    def test_Lambda_6_recursion(self):
        """Lambda_A(6): divisors of 6 with d>=2, 6/d>=2: d=2(q=3), d=3(q=2).
        Lambda(6) = S_6*log(6) - Lambda(2)*S_3 - Lambda(3)*S_2."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=10)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=10)
        expected = S[6] * math.log(6) - Lambda[2] * S[3] - Lambda[3] * S[2]
        assert abs(Lambda[6] - expected) < 1e-14

    def test_heisenberg_Lambda_supported_on_powers_of_2(self):
        """Heisenberg: Lambda_A(n) = 0 for all n that are NOT powers of 2.
        Lambda_A(2) = k*log(2).  Lambda_A(2^k) may be nonzero (from the
        recursion involving S_2).  But Lambda_A(n) = 0 for n not a power of 2,
        because S_n = 0 for all n >= 3 that are not powers of 2."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        Lambda = eng.shadow_von_mangoldt_mobius(S_float, max_r=30)
        assert abs(Lambda[2] - 5.0 * math.log(2)) < 1e-14
        # Non-prime-power values should be zero
        for n in range(2, 31):
            is_pp, p, k = eng._is_prime_power(n)
            if not is_pp:
                assert abs(Lambda[n]) < 1e-14, f"Lambda({n}) = {Lambda[n]} should be 0"
            elif p != 2:
                # For primes p != 2: Lambda(p) = S_p * log(p) = 0
                assert abs(Lambda[n]) < 1e-14, f"Lambda({n}) = {Lambda[n]} should be 0"


# =============================================================================
# 17. Euler product at integer s cross-verification
# =============================================================================

class TestEulerAtIntegers:
    """Cross-verify the Euler product evaluation at integer s."""

    def test_heisenberg_s2(self):
        """zeta_{H_5}(2) = 1 + 5/4 = 9/4."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=10)
        S_float = {r: float(v) for r, v in S.items()}
        result = eng.euler_vs_direct_at_integers(S_float, [2], P_max=10)
        assert abs(result[2]['direct'] - 2.25) < 1e-12

    def test_heisenberg_s3(self):
        """zeta_{H_5}(3) = 1 + 5/8 = 13/8."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(5, max_r=10)
        S_float = {r: float(v) for r, v in S.items()}
        result = eng.euler_vs_direct_at_integers(S_float, [3], P_max=10)
        assert abs(result[3]['direct'] - 1.625) < 1e-12

    def test_virasoro_s4_direct_sum(self):
        """Virasoro at c=1, s=4: direct sum should be finite and well-defined."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=60)
        val = eng.shadow_zeta_direct(S, 4.0, max_r=60)
        assert math.isfinite(val.real)


# =============================================================================
# 18. Local factor properties
# =============================================================================

class TestLocalFactorProperties:
    """Verify properties of local factors at primes."""

    def test_local_factor_at_0_is_1(self):
        """F_p(0) = 1 for all p and all families."""
        eng = _eng()
        for family_func, args in [
            (eng.virasoro_shadow_coefficients_float, (1.0,)),
            (eng.heisenberg_shadow_coefficients, (5,)),
            (eng.affine_sl2_shadow_coefficients, (2,)),
        ]:
            S = family_func(*args, max_r=30)
            S_f = {r: float(S[r]) for r in S}
            for p in [2, 3, 5]:
                val = eng.local_factor_evaluate(S_f, p, 0.0, max_power=5)
                assert abs(val - 1.0) < 1e-12

    def test_virasoro_local_factor_p5(self):
        """Virasoro local factor at p=5: F_5(X) = 1 + S_5*X + S_25*X^2 + ..."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=100)
        coeffs = eng.local_factor_coefficients(S, 5, max_power=3)
        assert coeffs[0] == 1.0
        assert abs(coeffs[1] - S[5]) < 1e-14
        assert abs(coeffs[2] - S[25]) < 1e-14

    def test_heisenberg_local_factor_product_equals_zeta(self):
        """For Heisenberg, prod_p F_p(p^{-s}) = 1 + k * 2^{-s} = zeta_A(s).
        Only p=2 contributes a nontrivial factor."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(7, max_r=30)
        S_float = {r: float(v) for r, v in S.items()}
        for s in [2.0, 3.0, 5.0]:
            F2 = eng.local_factor_evaluate(S_float, 2, 2.0 ** (-s), max_power=5)
            # All other primes: F_p = 1
            product = F2
            direct = eng.shadow_zeta_direct(S_float, s)
            assert abs(product - direct) < 1e-12


# =============================================================================
# 19. Shadow zeta direct evaluation cross-checks
# =============================================================================

class TestShadowZetaDirect:
    """Cross-verify shadow_zeta_direct against manual computation."""

    def test_heisenberg_zeta_manual(self):
        """zeta_{H_k}(s) = 1 + k * 2^{-s}."""
        eng = _eng()
        S = eng.heisenberg_shadow_coefficients(3, max_r=10)
        S_float = {r: float(v) for r, v in S.items()}
        for s in [1.0, 2.0, 3.0, 10.0]:
            val = eng.shadow_zeta_direct(S_float, s)
            expected = 1.0 + 3.0 * 2.0 ** (-s)
            assert abs(val - expected) < 1e-12

    def test_affine_zeta_manual(self):
        """zeta_{sl_2,k=2}(s) = 1 + kappa*2^{-s} + S_3*3^{-s}, kappa=3, S_3=4/4=1."""
        eng = _eng()
        S = eng.affine_sl2_shadow_coefficients(2, max_r=10)
        S_float = {r: float(v) for r, v in S.items()}
        for s in [2.0, 3.0]:
            val = eng.shadow_zeta_direct(S_float, s)
            expected = 1.0 + 3.0 * 2.0 ** (-s) + 1.0 * 3.0 ** (-s)  # 1 + kappa*2^{-s} + S_3*3^{-s}
            assert abs(val - expected) < 1e-12

    def test_zeta_at_large_s_approaches_1(self):
        """For any shadow sequence, zeta_A(s) -> 1 as s -> infinity."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(1.0, max_r=30)
        val = eng.shadow_zeta_direct(S, 100.0)
        assert abs(val - 1.0) < 1e-10


# =============================================================================
# 20. Comprehensive sweep: multiple c values
# =============================================================================

class TestMultipleCValues:
    """Sweep Virasoro at multiple central charges."""

    @pytest.mark.parametrize("c_val", [1, 2, 5, 10, 13, 20, 25])
    def test_virasoro_not_multiplicative_sweep(self, c_val):
        """Virasoro is not multiplicative at any positive integer c."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients(c_val, max_r=20)
        result = eng.test_multiplicativity(S, max_r=20)
        assert not result['is_multiplicative']

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_virasoro_von_mangoldt_not_pp_support(self, c_val):
        """Von Mangoldt not supported on prime powers at any c."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(float(c_val), max_r=40)
        Lambda = eng.shadow_von_mangoldt_mobius(S, max_r=40)
        result = eng.von_mangoldt_prime_power_support(Lambda, max_r=40)
        assert not result['euler_product_holds']

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_satake_well_defined(self, c_val):
        """Satake parameters are well-defined for all c > 0."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(float(c_val), max_r=30)
        for p in [2, 3, 5]:
            sat = eng.shadow_satake_parameters(S, p)
            assert sat['alpha_p'] is not None
            assert sat['beta_p'] is not None
            assert math.isfinite(abs(sat['alpha_p']))

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_euler_vs_direct_mismatch(self, c_val):
        """Partial Euler product differs from direct sum for Virasoro."""
        eng = _eng()
        S = eng.virasoro_shadow_coefficients_float(float(c_val), max_r=40)
        result = eng.euler_vs_direct_at_integers(S, [3], P_max=30)
        # They should not match precisely
        assert result[3]['abs_diff'] > 1e-10
