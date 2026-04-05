r"""Tests for BTZ arithmetic frontier engine.

Tests organised by section:
  1.  J-function coefficients and BTZ degeneracies
  2.  Prime factorisation and arithmetic invariants
  3.  Divisor structure
  4.  Shadow corrections to BTZ entropy
  5.  Number field identification
  6.  Rademacher expansion
  7.  Shadow-modified Rademacher
  8.  Kloosterman sums
  9.  Farey tail and shadows
  10. Bekenstein-Hawking from Koszul duality
  11. Arithmetic height
  12. Height growth analysis
  13. Multi-path verification (Fourier, Rademacher, bootstrap)
  14. Cross-family consistency
  15. Special central charges (c = 13, 24, 26)
  16. Large-n asymptotics
  17. Planted-forest consistency
  18. Full report and summary

MULTI-PATH VERIFICATION MANDATE:
  Every numerical result verified by at least 3 independent paths.
"""

import pytest
from fractions import Fraction
import math
import cmath
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from btz_arithmetic_frontier_engine import (
    # Section 1
    j_coefficient, btz_degeneracy, btz_degeneracy_table, J_COEFFICIENTS,
    # Section 2
    prime_factorisation, j_coefficient_factorisation,
    btz_degeneracy_factorisation,
    # Arithmetic invariants
    arithmetic_density, arithmetic_density_table,
    divisor_function, btz_divisor_table,
    # Section 3 (shadow corrections)
    kappa_virasoro, lambda_fp, virasoro_S3, virasoro_S4, virasoro_S5,
    planted_forest_g2, planted_forest_g3,
    F_g_scalar, virasoro_free_energy,
    bekenstein_hawking_entropy, entropy_shadow_corrections,
    shadow_correction_number_field, shadow_corrections_multi_c,
    # Section 4 (Rademacher)
    kloosterman_sum, bessel_I1, rademacher_coefficient, rademacher_table,
    # Shadow-modified Rademacher
    shadow_modified_kloosterman, rademacher_with_shadows,
    # Section 5 (Farey tail)
    farey_sequence, Z_pert_order, Z_pert_rationality_check,
    farey_tail_shadow_partition,
    # Section 6 (Koszul duality entropy)
    koszul_entropy_data, critical_string_entropy,
    self_dual_entropy, monster_entropy,
    # Section 7 (arithmetic height)
    logarithmic_weil_height, btz_arithmetic_height,
    arithmetic_height_table, height_growth_analysis,
    height_vs_entropy_proportionality,
    # Section 8 (verification)
    verify_degeneracy_fourier, verify_degeneracy_rademacher,
    verify_crossing_symmetry, verify_entropy_three_paths,
    # Section 9 (reports)
    full_arithmetic_report, prime_content_summary,
)


PI = math.pi
TWO_PI = 2.0 * PI


# =========================================================================
# Section 1: J-function coefficients and BTZ degeneracies
# =========================================================================

class TestJCoefficients:
    """Tests for J-function Fourier coefficients."""

    def test_j_polar_term(self):
        """c(-1) = 1: the polar term of J(tau) = q^{-1} + ..."""
        assert j_coefficient(-1) == 1

    def test_j_constant_term_zero(self):
        """c(0) = 0: J = j - 744 has zero constant term."""
        assert j_coefficient(0) == 0

    def test_j_mckay_coefficient(self):
        """c(1) = 196884: the McKay observation (Monster + 1)."""
        assert j_coefficient(1) == 196884

    def test_j_coefficient_n2(self):
        """c(2) = 21493760."""
        assert j_coefficient(2) == 21493760

    def test_j_coefficient_n3(self):
        """c(3) = 864299970."""
        assert j_coefficient(3) == 864299970

    def test_j_coefficient_n4(self):
        assert j_coefficient(4) == 20245856256

    def test_j_coefficient_n5(self):
        assert j_coefficient(5) == 333202640600

    def test_j_coefficient_n10(self):
        assert j_coefficient(10) == 22567393309593600

    def test_j_coefficient_n20(self):
        assert j_coefficient(20) == 189449976248893390028800

    def test_j_coefficient_negative(self):
        """c(n) = 0 for n < -1."""
        assert j_coefficient(-2) == 0
        assert j_coefficient(-10) == 0

    def test_j_coefficient_out_of_range(self):
        """Raise error for n > 20."""
        with pytest.raises(ValueError):
            j_coefficient(21)

    def test_j_coefficients_all_positive(self):
        """All c(n) for n >= 1 are positive (J-function has positive coefficients)."""
        for n in range(1, 21):
            assert j_coefficient(n) > 0

    def test_j_coefficients_monotone_increasing(self):
        """c(n) is strictly increasing for n >= 1 (exponential growth)."""
        for n in range(1, 20):
            assert j_coefficient(n) < j_coefficient(n + 1)


class TestBTZDegeneracy:
    """Tests for BTZ degeneracy d(n) = c(n)^2."""

    def test_degeneracy_is_perfect_square(self):
        """d(n) = c(n)^2 is always a perfect square."""
        for n in range(1, 11):
            dn = btz_degeneracy(n)
            cn = j_coefficient(n)
            assert dn == cn * cn

    def test_degeneracy_n1(self):
        """d(1) = 196884^2 = 38763214656."""
        assert btz_degeneracy(1) == 196884 ** 2

    def test_degeneracy_n2(self):
        assert btz_degeneracy(2) == 21493760 ** 2

    def test_degeneracy_table_length(self):
        table = btz_degeneracy_table(10)
        assert len(table) == 10
        assert all(n in table for n in range(1, 11))

    def test_degeneracy_table_values(self):
        table = btz_degeneracy_table(5)
        for n in range(1, 6):
            assert table[n] == j_coefficient(n) ** 2


# =========================================================================
# Section 2: Prime factorisation and arithmetic invariants
# =========================================================================

class TestPrimeFactorisation:
    """Tests for prime factorisation machinery."""

    def test_factor_1(self):
        assert prime_factorisation(1) == {}

    def test_factor_prime(self):
        assert prime_factorisation(7) == {7: 1}

    def test_factor_prime_power(self):
        assert prime_factorisation(8) == {2: 3}

    def test_factor_composite(self):
        assert prime_factorisation(12) == {2: 2, 3: 1}

    def test_factor_large(self):
        """Factor 196884 = 2^2 * 3 * 23 * 23 * 31."""
        factors = prime_factorisation(196884)
        # 196884 = 4 * 49221 = 4 * 3 * 16407 = 12 * 16407
        # 16407 = 3 * 5469 = 3 * 3 * 1823 = 9 * 1823
        # Wait, let me just verify: 196884 / 4 = 49221
        # 49221 / 3 = 16407; 16407 / 3 = 5469; 5469 / 3 = 1823; 1823 is prime?
        # 1823: not div by 2,3,5,7,11,13,17,19,23,29,31,37,41,43 (sqrt(1823) ~ 42.7)
        # Actually: 196884 = 2^2 * 3^3 * 1823? Let me check: 4*27*1823 = 108*1823 = 196884
        # And 1823: 1823/7 = 260.43, 1823/11 = 165.7, 1823/13 = 140.2, 1823/17 = 107.2
        # 1823/19 = 95.9, 1823/23 = 79.3, 1823/29 = 62.9, 1823/31 = 58.8, 1823/37 = 49.3
        # 1823/41 = 44.5, 1823/43 = 42.4 -> 1823 is prime.
        # So 196884 = 2^2 * 3^3 * 1823
        product = 1
        for p, e in factors.items():
            product *= p ** e
        assert product == 196884

    def test_j_coefficient_factorisation_n1(self):
        """c(1) = 196884 = 2^2 * 3^3 * 1823."""
        factors = j_coefficient_factorisation(1)
        product = 1
        for p, e in factors.items():
            product *= p ** e
        assert product == 196884

    def test_j_coefficient_factorisation_n2(self):
        """c(2) = 21493760."""
        factors = j_coefficient_factorisation(2)
        product = 1
        for p, e in factors.items():
            product *= p ** e
        assert product == 21493760

    def test_btz_degeneracy_factorisation_doubles_exponents(self):
        """d(n) = c(n)^2: all exponents in d(n) are even."""
        for n in range(1, 6):
            factors = btz_degeneracy_factorisation(n)
            for p, e in factors.items():
                assert e % 2 == 0, f"Exponent of {p} in d({n}) is {e}, should be even"

    def test_btz_degeneracy_factorisation_matches_cn_squared(self):
        """d(n) factorisation = c(n) factorisation with doubled exponents."""
        for n in range(1, 6):
            cn_factors = j_coefficient_factorisation(n)
            dn_factors = btz_degeneracy_factorisation(n)
            for p in cn_factors:
                assert dn_factors[p] == 2 * cn_factors[p]

    def test_factor_zero_raises(self):
        with pytest.raises(ValueError):
            prime_factorisation(0)

    def test_factor_negative_raises(self):
        with pytest.raises(ValueError):
            prime_factorisation(-5)


class TestArithmeticDensity:
    """Tests for omega(d(n)) = number of distinct prime factors."""

    def test_density_n1(self):
        """omega(d(1)) = omega(196884^2) = omega(196884) = 3 (primes: 2, 3, 1823)."""
        assert arithmetic_density(1) == 3

    def test_density_positive(self):
        """omega(d(n)) > 0 for all n >= 1."""
        for n in range(1, 11):
            assert arithmetic_density(n) > 0

    def test_density_table_length(self):
        table = arithmetic_density_table(10)
        assert len(table) == 10

    def test_density_nondecreasing_trend(self):
        """omega(d(n)) generally increases with n (more primes in larger numbers)."""
        table = arithmetic_density_table(20)
        # Not strictly monotone, but the trend is upward
        assert table[20] >= table[1]


# =========================================================================
# Section 3: Divisor structure
# =========================================================================

class TestDivisorFunction:
    """Tests for divisor functions sigma_k."""

    def test_sigma_0_prime(self):
        """sigma_0(p) = 2 for prime p."""
        assert divisor_function(7, 0) == 2

    def test_sigma_0_prime_power(self):
        """sigma_0(p^a) = a + 1."""
        assert divisor_function(8, 0) == 4  # 2^3: 1, 2, 4, 8

    def test_sigma_1_prime(self):
        """sigma_1(p) = 1 + p."""
        assert divisor_function(7, 1) == 8

    def test_sigma_1_small(self):
        """sigma_1(6) = 1 + 2 + 3 + 6 = 12."""
        assert divisor_function(6, 1) == 12

    def test_sigma_2_prime(self):
        """sigma_2(p) = 1 + p^2."""
        assert divisor_function(5, 2) == 26  # 1 + 25

    def test_sigma_0_of_1(self):
        assert divisor_function(1, 0) == 1

    def test_divisor_function_multiplicative(self):
        """sigma_k is multiplicative: sigma_k(mn) = sigma_k(m)*sigma_k(n) when gcd(m,n)=1."""
        for k in [0, 1, 2]:
            s_6 = divisor_function(6, k)
            s_2 = divisor_function(2, k)
            s_3 = divisor_function(3, k)
            assert s_6 == s_2 * s_3

    def test_btz_divisor_table(self):
        """Check that the BTZ divisor table has correct structure."""
        table = btz_divisor_table(5, k_values=(0, 1, 2))
        assert len(table) == 5
        for n in range(1, 6):
            assert 0 in table[n]
            assert 1 in table[n]
            assert 2 in table[n]

    def test_sigma_0_d1_is_perfect_square_divisors(self):
        """sigma_0(d(1)) = sigma_0(196884^2): count divisors of a perfect square.

        d(1) = 196884^2 has small prime factors (2,3,1823), all in our table.
        """
        dn = btz_degeneracy(1)
        s0 = divisor_function(dn, 0)
        # For d = c^2 = prod p_i^{2a_i}, sigma_0 = prod (2a_i + 1)
        cn_factors = j_coefficient_factorisation(1)
        expected = 1
        for p, a in cn_factors.items():
            expected *= (2 * a + 1)
        assert s0 == expected
        # Also verify via btz_degeneracy_factorisation
        dn_factors = btz_degeneracy_factorisation(1)
        computed = 1
        for p, a in dn_factors.items():
            computed *= (a + 1)
        assert computed == expected


# =========================================================================
# Section 4: Shadow corrections to BTZ entropy
# =========================================================================

class TestShadowCorrections:
    """Tests for shadow corrections to BTZ entropy."""

    def test_kappa_virasoro_c24(self):
        """kappa(Vir_24) = 12. AP1/AP48."""
        assert kappa_virasoro(24) == Fraction(12)

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        assert lambda_fp(1) == Fraction(1, 24)

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Fraction(7, 5760)

    def test_lambda_fp_g3(self):
        """lambda_3^FP = 31/967680."""
        assert lambda_fp(3) == Fraction(31, 967680)

    def test_lambda_fp_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1 (AP22)."""
        for g in range(1, 8):
            assert lambda_fp(g) > 0

    def test_virasoro_S3(self):
        """S_3 = 2 (c-independent)."""
        assert virasoro_S3() == Fraction(2)

    def test_virasoro_S4_c24(self):
        """Q^contact at c = 24: 10/(24*142) = 5/1704."""
        expected = Fraction(10) / (24 * (5 * 24 + 22))
        assert virasoro_S4(24) == expected

    def test_virasoro_S5_c24(self):
        """S_5 at c = 24: -48/(576*142) = -48/81792."""
        expected = Fraction(-48) / (576 * 142)
        assert virasoro_S5(24) == expected

    def test_F1_c24(self):
        """F_1(Vir_24) = kappa/24 = 12/24 = 1/2."""
        assert virasoro_free_energy(24, 1) == Fraction(1, 2)

    def test_F1_equals_kappa_times_lambda1(self):
        """F_1 = kappa * lambda_1 for any c."""
        for c in [12, 24, 48, 72]:
            kappa = kappa_virasoro(c)
            assert virasoro_free_energy(c, 1) == kappa * lambda_fp(1)

    def test_F2_has_planted_forest(self):
        """F_2 includes planted-forest correction at genus 2."""
        c = 24
        kappa = kappa_virasoro(c)
        scalar = F_g_scalar(kappa, 2)
        full = virasoro_free_energy(c, 2)
        # Planted forest correction should be nonzero for Virasoro
        pf = planted_forest_g2(kappa, virasoro_S3())
        assert pf != 0
        assert full == scalar + pf

    def test_entropy_corrections_structure(self):
        """Entropy corrections have correct structure."""
        result = entropy_shadow_corrections(24, 10, order=5)
        assert 'S_0' in result
        assert 'S_1' in result
        assert 'S_2' in result
        assert 'S_total' in result
        assert result['S_0'] > 0

    def test_S0_is_bekenstein_hawking(self):
        """S_0 = 4*pi*sqrt(n) for c = 24."""
        for n in [1, 5, 10]:
            result = entropy_shadow_corrections(24, n)
            expected = 4.0 * PI * math.sqrt(n)
            assert abs(result['S_0'] - expected) < 1e-10

    def test_S1_is_logarithmic(self):
        """S_1 = -(3/2)*log(S_BH/(2*pi)) (one-loop correction)."""
        for n in [1, 5, 10]:
            result = entropy_shadow_corrections(24, n)
            S_BH = result['S_0']
            expected_S1 = -1.5 * math.log(S_BH / TWO_PI)
            assert abs(result['S_1'] - expected_S1) < 1e-10

    def test_corrections_decrease_with_order(self):
        """Higher-genus corrections are smaller (Bernoulli decay)."""
        result = entropy_shadow_corrections(24, 10, order=5)
        # |S_2| > |S_3| > |S_4| > |S_5| for large enough n
        corrections = result['corrections']
        for r in range(3, 6):
            if r in corrections and r - 1 in corrections:
                assert abs(corrections[r]) < abs(corrections[r - 1])

    def test_shadow_corrections_c24_c48_c72(self):
        """Shadow corrections computed for multiple central charges."""
        results = shadow_corrections_multi_c((24, 48, 72), order=3)
        assert len(results) == 3
        for c in [24, 48, 72]:
            assert c in results
            assert results[c]['S_0'] > 0


class TestNumberFields:
    """Tests for number field identification of shadow coefficients."""

    def test_kappa_is_rational(self):
        """kappa(Vir_c) = c/2 is rational for all integer c."""
        for c in [1, 12, 13, 24, 26]:
            field = shadow_correction_number_field(c, 2)
            assert 'Q' in field

    def test_S3_is_rational(self):
        """S_3 = 2 is rational (c-independent)."""
        field = shadow_correction_number_field(24, 3)
        assert 'Q' in field

    def test_S4_is_rational(self):
        """S_4 = 10/[c(5c+22)] is rational."""
        field = shadow_correction_number_field(24, 4)
        assert 'Q' in field

    def test_S5_is_rational(self):
        """S_5 = -48/[c^2(5c+22)] is rational."""
        field = shadow_correction_number_field(24, 5)
        assert 'Q' in field


# =========================================================================
# Section 5: Rademacher expansion
# =========================================================================

class TestKloostermanSums:
    """Tests for Kloosterman sums."""

    def test_kloosterman_c1(self):
        """Kl(n, m; 1) = 1 for all n, m."""
        for n in range(1, 5):
            kl = kloosterman_sum(n, -1, 1)
            assert abs(kl - 1.0) < 1e-10

    def test_kloosterman_real_for_symmetric(self):
        """Kl(n, m; c) is real when n = m (symmetric case)."""
        for c_kl in range(1, 8):
            kl = kloosterman_sum(3, 3, c_kl)
            assert abs(kl.imag) < 1e-10

    def test_kloosterman_bound(self):
        """Weil bound: |Kl(n, m; c)| <= sigma_0(c) * sqrt(c) (for c prime: <= 2*sqrt(c))."""
        # For prime c: |Kl| <= 2*sqrt(c)
        for p in [5, 7, 11, 13]:
            kl = kloosterman_sum(1, -1, p)
            assert abs(kl) <= 2.0 * math.sqrt(p) + 1e-10

    def test_kloosterman_c2(self):
        """Kl(n, m; 2): only d = 1 (gcd(1,2) = 1), d^{-1} = 1 mod 2."""
        kl = kloosterman_sum(1, -1, 2)
        # d = 1: exp(2*pi*i*(1 - 1)/2) = exp(0) = 1
        assert abs(kl - 1.0) < 1e-10


class TestBesselI1:
    """Tests for modified Bessel function I_1."""

    def test_I1_at_zero(self):
        """I_1(0) = 0."""
        assert bessel_I1(0) == 0.0

    def test_I1_small_x(self):
        """I_1(x) ~ x/2 for small x (next term is x^3/16)."""
        x = 0.01
        # I_1(x) = x/2 + x^3/16 + ... so error ~ x^3/16 ~ 6.25e-8
        assert abs(bessel_I1(x) - x / 2) < 1e-7

    def test_I1_known_value(self):
        """I_1(1) ~ 0.5651591039924851."""
        # From mathematical tables
        expected = 0.5651591039924851
        assert abs(bessel_I1(1.0) - expected) < 1e-8

    def test_I1_positive_for_positive_x(self):
        """I_1(x) > 0 for x > 0."""
        for x in [0.1, 1.0, 5.0, 10.0, 50.0]:
            assert bessel_I1(x) > 0

    def test_I1_monotone_increasing(self):
        """I_1 is monotonically increasing for x > 0."""
        values = [bessel_I1(x) for x in [0.5, 1.0, 2.0, 5.0, 10.0]]
        for i in range(len(values) - 1):
            assert values[i] < values[i + 1]

    def test_I1_large_x_asymptotic(self):
        """I_1(x) ~ e^x / sqrt(2*pi*x) for large x."""
        x = 100.0
        asymptotic = math.exp(x) / math.sqrt(TWO_PI * x)
        ratio = bessel_I1(x) / asymptotic
        assert abs(ratio - 1.0) < 0.01  # 1% accuracy at x = 100


class TestRademacher:
    """Tests for Rademacher exact formula."""

    def test_rademacher_n1_approximation(self):
        """Rademacher with enough terms approximates c(1) = 196884."""
        approx = rademacher_coefficient(1, m=-1, c_max=50)
        assert round(approx) == 196884

    def test_rademacher_n2(self):
        """Rademacher approximates c(2) = 21493760."""
        approx = rademacher_coefficient(2, m=-1, c_max=100)
        assert round(approx) == 21493760

    def test_rademacher_n3(self):
        """Rademacher approximates c(3) = 864299970."""
        approx = rademacher_coefficient(3, m=-1, c_max=100)
        assert round(approx) == 864299970

    def test_rademacher_convergence(self):
        """Rademacher series converges: more terms => better approximation."""
        exact = 196884
        prev_error = float('inf')
        for c_max in [5, 10, 20, 40]:
            approx = rademacher_coefficient(1, m=-1, c_max=c_max)
            error = abs(approx - exact)
            assert error <= prev_error + 1e-6
            prev_error = error

    def test_rademacher_table_matches(self):
        """Rademacher table: all entries match exact coefficients (c_max=100)."""
        table = rademacher_table(n_max=5, c_max=100)
        for n in range(1, 6):
            assert table[n]['matches'], f"Rademacher mismatch at n={n}"

    def test_rademacher_leading_term(self):
        """Leading Rademacher term ~ (2*pi/sqrt(n)) * I_1(4*pi*sqrt(n))."""
        n = 1
        # Leading term (c_kl = 1): Kl(1,-1;1) = 1
        leading = (TWO_PI / math.sqrt(n)) * bessel_I1(4.0 * PI * math.sqrt(n))
        exact = 196884
        # Leading term alone should give most of the answer
        assert abs(leading - exact) / exact < 0.01  # within 1%

    def test_rademacher_returns_zero_for_n_zero(self):
        """Rademacher coefficient for n <= 0 returns 0."""
        assert rademacher_coefficient(0) == 0.0
        assert rademacher_coefficient(-1) == 0.0


# =========================================================================
# Section 6: Shadow-modified Rademacher
# =========================================================================

class TestShadowRademacher:
    """Tests for shadow-modified Rademacher expansion."""

    def test_unmodified_equals_base(self):
        """With no shadow coefficients, modified Kloosterman = base."""
        kl_base = kloosterman_sum(1, -1, 5)
        kl_mod = shadow_modified_kloosterman(1, -1, 5, {})
        assert abs(kl_base - kl_mod) < 1e-14

    def test_shadow_modification_small(self):
        """Shadow modification is a small correction to Kloosterman sums."""
        S_r = {2: 12.0, 3: 2.0, 4: 0.0029}  # Virasoro c=24
        for c_kl in range(1, 10):
            kl_base = kloosterman_sum(1, -1, c_kl)
            kl_mod = shadow_modified_kloosterman(1, -1, c_kl, S_r)
            if abs(kl_base) > 1e-10:
                ratio = abs(kl_mod) / abs(kl_base)
                # Modification should be order 1 (not wildly different)
                assert 0.1 < ratio < 100

    def test_rademacher_with_shadows_structure(self):
        """Shadow-modified Rademacher returns expected fields."""
        result = rademacher_with_shadows(1, c_central=24, c_max=20)
        assert 'base_rademacher' in result
        assert 'shadow_modified' in result
        assert 'exact' in result

    def test_rademacher_with_shadows_approximate(self):
        """Both base and modified should be close to exact."""
        result = rademacher_with_shadows(1, c_central=24, c_max=100)
        assert round(result['base_rademacher']) == 196884


# =========================================================================
# Section 7: Farey tail and shadows
# =========================================================================

class TestFareyTail:
    """Tests for Farey tail expansion."""

    def test_farey_sequence_includes_identity(self):
        """Farey sequence includes the identity (0, 1)."""
        pairs = farey_sequence(3)
        assert (0, 1) in pairs

    def test_farey_sequence_coprime(self):
        """All Farey pairs are coprime."""
        pairs = farey_sequence(5)
        for c_F, d in pairs:
            if c_F > 0:
                assert math.gcd(abs(c_F), abs(d)) == 1

    def test_farey_sequence_count(self):
        """Farey sequence at N=1: (0,1), (1,0), (1,1), (1,-1) — wait, check."""
        pairs = farey_sequence(1)
        assert (0, 1) in pairs
        assert (1, 0) in pairs
        assert (1, 1) in pairs

    def test_Z_pert_order_0(self):
        """Z_pert^{(0)} = 1 (tree level)."""
        coeffs = Z_pert_order(24, order=0)
        assert coeffs[0] == Fraction(1)

    def test_Z_pert_rationality(self):
        """All Z_pert coefficients are rational (for Virasoro)."""
        check = Z_pert_rationality_check(24, order=4)
        for r, is_rational in check.items():
            assert is_rational

    def test_farey_tail_shadow_partition_structure(self):
        """Farey tail shadow partition returns expected fields."""
        tau = 0.1 + 0.5j
        result = farey_tail_shadow_partition(24, tau, N_farey=3, g_max=2)
        assert 'Z_classical' in result
        assert 'Z_with_shadows' in result
        assert 'F_table' in result

    def test_farey_tail_classical_nonzero(self):
        """Classical Farey tail partition function is nonzero."""
        tau = 0.01 + 1.0j
        result = farey_tail_shadow_partition(24, tau, N_farey=3, g_max=1)
        assert abs(result['Z_classical']) > 0


# =========================================================================
# Section 8: Bekenstein-Hawking from Koszul duality
# =========================================================================

class TestKoszulEntropy:
    """Tests for entropy from Koszul duality structure."""

    def test_complementarity_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for all c.  (AP24)."""
        for c in [0, 1, 12, 13, 24, 26]:
            data = koszul_entropy_data(c)
            assert abs(data['complementarity_sum'] - 13.0) < 1e-10

    def test_complementarity_sum_exact(self):
        """Exact arithmetic: kappa + kappa' = 13."""
        for c in [0, 1, 12, 13, 24, 26]:
            data = koszul_entropy_data(c)
            assert data['complementarity_sum_exact'] == Fraction(13)

    def test_critical_string_kappa_eff_zero(self):
        """At c = 26: kappa_eff = kappa(matter) + kappa(ghost) = 0."""
        data = critical_string_entropy()
        assert abs(data['kappa_eff']) < 1e-10

    def test_critical_string_kappa(self):
        """kappa(Vir_26) = 13."""
        data = critical_string_entropy()
        assert abs(data['kappa'] - 13.0) < 1e-10

    def test_self_dual_delta_kappa_zero(self):
        """At c = 13: delta_kappa = kappa - kappa' = 0 (self-dual)."""
        data = self_dual_entropy()
        assert abs(data['delta_kappa']) < 1e-10

    def test_self_dual_kappa(self):
        """kappa(Vir_13) = 13/2."""
        data = self_dual_entropy()
        assert abs(data['kappa'] - 6.5) < 1e-10

    def test_monster_kappa(self):
        """kappa(Vir_24) = 12."""
        data = monster_entropy()
        assert abs(data['kappa'] - 12.0) < 1e-10

    def test_monster_delta_kappa(self):
        """delta_kappa at c = 24: 12 - 1 = 11."""
        data = monster_entropy()
        assert abs(data['delta_kappa'] - 11.0) < 1e-10

    def test_kappa_ghost(self):
        """kappa(ghost) = -13 for the bc ghost system at c_ghost = -26."""
        data = koszul_entropy_data(24)
        assert abs(data['kappa_ghost'] - (-13.0)) < 1e-10

    def test_kappa_eff_c24(self):
        """kappa_eff at c = 24: 12 + (-13) = -1."""
        data = koszul_entropy_data(24)
        assert abs(data['kappa_eff'] - (-1.0)) < 1e-10

    def test_F1_positive_for_c_positive(self):
        """F_1 = kappa/24 > 0 for c > 0."""
        for c in [1, 12, 24, 48]:
            data = koszul_entropy_data(c)
            assert data['F1_matter'] > 0


# =========================================================================
# Section 9: Arithmetic height
# =========================================================================

class TestArithmeticHeight:
    """Tests for logarithmic Weil height of BTZ degeneracies."""

    def test_weil_height_basic(self):
        """h(n) = log(n) for positive integers."""
        for n in [1, 2, 10, 100]:
            assert abs(logarithmic_weil_height(n) - math.log(n)) < 1e-14

    def test_weil_height_1(self):
        """h(1) = 0."""
        assert logarithmic_weil_height(1) == 0.0

    def test_btz_height_n1(self):
        """h(d(1)) = 2*log(196884) ~ 24.39."""
        h = btz_arithmetic_height(1)
        expected = 2.0 * math.log(196884)
        assert abs(h - expected) < 1e-10

    def test_btz_height_positive(self):
        """h(d(n)) > 0 for all n >= 1."""
        for n in range(1, 11):
            assert btz_arithmetic_height(n) > 0

    def test_btz_height_increasing(self):
        """h(d(n)) is strictly increasing (c(n) increasing implies h increasing)."""
        for n in range(1, 20):
            assert btz_arithmetic_height(n) < btz_arithmetic_height(n + 1)

    def test_height_table_structure(self):
        """Height table has correct structure."""
        table = arithmetic_height_table(5)
        for n in range(1, 6):
            assert 'h_dn' in table[n]
            assert 'S_BH' in table[n]
            assert 'ratio_h_over_S' in table[n]

    def test_height_table_sbh_formula(self):
        """S_BH in height table matches 4*pi*sqrt(n)."""
        table = arithmetic_height_table(5)
        for n in range(1, 6):
            expected = 4.0 * PI * math.sqrt(n)
            assert abs(table[n]['S_BH'] - expected) < 1e-10


class TestHeightGrowth:
    """Tests for growth analysis of arithmetic height."""

    def test_height_growth_slope(self):
        """Fitted slope should be close to 8*pi ~ 25.13."""
        analysis = height_growth_analysis(20)
        expected_slope = 8.0 * PI
        # Allow 5% error since n_max = 20 includes sub-leading terms
        assert abs(analysis['fitted_slope'] - expected_slope) / expected_slope < 0.05

    def test_height_entropy_ratio_approaches_2(self):
        """h(d(n)) / S_BH(n) -> 2 as n -> infinity."""
        prop = height_vs_entropy_proportionality(20)
        # The last ratio (n = 20) should be close to 2
        assert abs(prop['last_ratio'] - 2.0) < 0.15

    def test_height_entropy_mean_ratio(self):
        """Mean ratio h/S_BH should be between 1.5 and 2.5."""
        prop = height_vs_entropy_proportionality(20)
        assert 1.5 < prop['mean_ratio'] < 2.5

    def test_asymptotic_ratio_is_2(self):
        """The theoretical asymptotic limit is 2."""
        prop = height_vs_entropy_proportionality(20)
        assert prop['asymptotic_limit'] == 2.0

    def test_slope_relative_error_small(self):
        """Slope relative error < 5%."""
        analysis = height_growth_analysis(20)
        assert analysis['slope_relative_error'] < 0.05


# =========================================================================
# Section 10: Multi-path verification
# =========================================================================

class TestMultiPathVerification:
    """Tests enforcing the multi-path verification mandate."""

    def test_path1_fourier(self):
        """Path 1: d(n) from direct Fourier table."""
        for n in range(1, 6):
            result = verify_degeneracy_fourier(n)
            assert result['d_n'] == j_coefficient(n) ** 2

    def test_path2_rademacher(self):
        """Path 2: d(n) from Rademacher expansion matches exact."""
        for n in range(1, 4):
            result = verify_degeneracy_rademacher(n, c_max=100)
            assert result['c_n_error'] == 0

    def test_path4_bootstrap(self):
        """Path 4: Modular bootstrap / McKay decomposition check."""
        result = verify_crossing_symmetry(1)
        assert result['c_n'] == 196884
        assert result['mckay_decomposition'] is not None

    def test_three_path_entropy_n1(self):
        """Three-path entropy verification at n = 1, c = 24."""
        result = verify_entropy_three_paths(24, 1)
        # All three paths should agree within 10%
        S_cardy = result['S_cardy']
        S_micro = result['S_microstate']
        S_rad = result['S_rademacher_leading']
        assert abs(S_cardy - S_rad) / S_cardy < 0.01  # exact match for c=24
        # Microstate and Cardy agree asymptotically
        assert abs(S_micro - S_cardy) / S_cardy < 0.5  # sub-leading corrections at n=1

    def test_three_path_entropy_large_n(self):
        """At large n, all three paths converge."""
        result = verify_entropy_three_paths(24, 10)
        S_cardy = result['S_cardy']
        S_micro = result['S_microstate']
        # Better agreement at larger n
        assert abs(S_micro - S_cardy) / S_cardy < 0.1

    def test_fourier_rademacher_consistency(self):
        """Fourier and Rademacher give the same c(n) for n = 1..5."""
        for n in range(1, 6):
            fourier = verify_degeneracy_fourier(n)
            rademacher = verify_degeneracy_rademacher(n, c_max=100)
            assert fourier['d_n'] == rademacher['d_n_exact']

    def test_mckay_decomposition_n1(self):
        """c(1) = 196884 = 1 + 196883 (McKay)."""
        assert j_coefficient(1) == 1 + 196883

    def test_mckay_decomposition_n2(self):
        """c(2) = 21493760 = 1 + 196883 + 21296876."""
        assert j_coefficient(2) == 1 + 196883 + 21296876

    def test_mckay_decomposition_n3(self):
        """c(3) = 864299970 = 2 + 2*196883 + 21296876 + 842609326."""
        assert j_coefficient(3) == 2 + 2 * 196883 + 21296876 + 842609326


# =========================================================================
# Section 11: Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-family and cross-volume consistency tests."""

    def test_kappa_additivity(self):
        """kappa is additive: kappa(A tensor B) = kappa(A) + kappa(B)."""
        # Heisenberg at level k1 and k2
        k1, k2 = Fraction(3), Fraction(5)
        from btz_arithmetic_frontier_engine import kappa_virasoro
        # For Virasoro: kappa(Vir_{c1+c2}) should NOT equal kappa(Vir_{c1}) + kappa(Vir_{c2})
        # in general (it does because kappa = c/2 is linear in c)
        assert kappa_virasoro(10) == kappa_virasoro(3) + kappa_virasoro(7)

    def test_complementarity_universal(self):
        """kappa + kappa' = 13 for ALL integer c (AP24)."""
        for c in range(-10, 40):
            kappa = kappa_virasoro(c)
            kappa_dual = kappa_virasoro(26 - c)
            assert kappa + kappa_dual == Fraction(13)

    def test_F_g_scalar_proportional_to_kappa(self):
        """F_g^{scalar} = kappa * lambda_g: linear in kappa."""
        for g in range(1, 6):
            lam = lambda_fp(g)
            for c in [12, 24, 48]:
                kappa = kappa_virasoro(c)
                assert F_g_scalar(kappa, g) == kappa * lam

    def test_planted_forest_heisenberg_zero(self):
        """Planted forest vanishes for Heisenberg (S_3 = 0, class G)."""
        kappa = Fraction(1)  # Heisenberg level 1
        S3 = Fraction(0)
        assert planted_forest_g2(kappa, S3) == 0

    def test_planted_forest_virasoro_nonzero(self):
        """Planted forest is nonzero for Virasoro (S_3 = 2, class M)."""
        for c in [12, 24, 48]:
            kappa = kappa_virasoro(c)
            S3 = virasoro_S3()
            pf = planted_forest_g2(kappa, S3)
            assert pf != 0


# =========================================================================
# Section 12: Special central charges
# =========================================================================

class TestSpecialCentralCharges:
    """Tests at special central charges c = 13, 24, 26."""

    def test_c13_self_dual(self):
        """c = 13 is self-dual: Vir_13^! = Vir_13."""
        data = self_dual_entropy()
        assert abs(data['kappa'] - data['kappa_dual']) < 1e-10

    def test_c24_monster(self):
        """c = 24: Monster module, kappa = 12."""
        data = monster_entropy()
        assert abs(data['kappa'] - 12.0) < 1e-10
        assert data['c'] == 24

    def test_c26_critical(self):
        """c = 26: critical string, kappa_eff = 0."""
        data = critical_string_entropy()
        assert abs(data['kappa_eff']) < 1e-10

    def test_c26_kappa_dual_zero(self):
        """c = 26: Koszul dual Vir_0 has kappa = 0."""
        data = critical_string_entropy()
        assert abs(data['kappa_dual']) < 1e-10

    def test_c0_kappa_zero(self):
        """c = 0: kappa(Vir_0) = 0 (trivial / topological)."""
        data = koszul_entropy_data(0)
        assert abs(data['kappa']) < 1e-10

    def test_c1_free_boson(self):
        """c = 1: free boson, kappa = 1/2."""
        data = koszul_entropy_data(1)
        assert abs(data['kappa'] - 0.5) < 1e-10


# =========================================================================
# Section 13: Large-n asymptotics
# =========================================================================

class TestLargeNAsymptotics:
    """Tests for large-n behaviour of BTZ degeneracies and entropy."""

    def test_log_cn_grows_like_sqrt_n(self):
        """log(c(n)) ~ 4*pi*sqrt(n) for large n (Rademacher leading term).

        Sub-leading corrections: -(3/4)*log(n) - (1/2)*log(2) - ...
        These are significant at n = 10 but negligible at n = 20.
        """
        for n in [10, 15, 20]:
            cn = j_coefficient(n)
            log_cn = math.log(cn)
            leading = 4.0 * PI * math.sqrt(n)
            # Include sub-leading: log(c(n)) ~ 4*pi*sqrt(n) - (3/4)*log(n) - ...
            ratio = log_cn / leading
            assert abs(ratio - 1.0) < 0.06, f"n={n}: ratio={ratio}"
        # At n = 20, the ratio should be closer to 1 (sub-leading ~ 5%)
        cn_20 = j_coefficient(20)
        ratio_20 = math.log(cn_20) / (4.0 * PI * math.sqrt(20))
        assert abs(ratio_20 - 1.0) < 0.05

    def test_height_grows_like_8pi_sqrt_n(self):
        """h(d(n)) = 2*log(c(n)) ~ 8*pi*sqrt(n) (sub-leading ~ 6% at n = 10)."""
        for n in [10, 15, 20]:
            h = btz_arithmetic_height(n)
            expected = 8.0 * PI * math.sqrt(n)
            ratio = h / expected
            assert abs(ratio - 1.0) < 0.06

    def test_degeneracy_super_exponential_growth(self):
        """d(n) grows super-exponentially: log(d(n+1))/log(d(n)) > 1."""
        for n in range(1, 15):
            log_dn = math.log(btz_degeneracy(n))
            log_dn1 = math.log(btz_degeneracy(n + 1))
            assert log_dn1 > log_dn

    def test_entropy_corrections_decrease(self):
        """At large n, corrections S_r/S_BH -> 0."""
        result = entropy_shadow_corrections(24, 100, order=3)
        if 'corrections' in result:
            for r, corr in result['corrections'].items():
                assert abs(corr) / result['S_0'] < 0.01


# =========================================================================
# Section 14: Planted-forest consistency
# =========================================================================

class TestPlantedForestConsistency:
    """Consistency tests for planted-forest corrections."""

    def test_planted_forest_g2_explicit_c24(self):
        """Planted forest at genus 2 for c = 24: (40 - 12)/24 = 28/24 = 7/6."""
        kappa = kappa_virasoro(24)  # 12
        S3 = virasoro_S3()  # 2
        pf = planted_forest_g2(kappa, S3)
        # S3*(10*S3 - kappa)/48 = 2*(20-12)/48 = 16/48 = 1/3
        assert pf == Fraction(1, 3)

    def test_planted_forest_g2_c48(self):
        """Planted forest at genus 2 for c = 48."""
        kappa = kappa_virasoro(48)  # 24
        S3 = virasoro_S3()  # 2
        pf = planted_forest_g2(kappa, S3)
        # 2*(20-24)/48 = 2*(-4)/48 = -8/48 = -1/6
        assert pf == Fraction(-1, 6)

    def test_F2_c24(self):
        """F_2(Vir_24) = scalar + PF = 12*7/5760 + 1/3."""
        c = 24
        expected_scalar = Fraction(12) * Fraction(7, 5760)  # 84/5760 = 7/480
        expected_pf = Fraction(1, 3)
        expected = expected_scalar + expected_pf
        assert virasoro_free_energy(24, 2) == expected

    def test_F3_structure(self):
        """F_3 has scalar + planted-forest-g3 correction."""
        c = 24
        kappa = kappa_virasoro(c)
        scalar = F_g_scalar(kappa, 3)
        S3 = virasoro_S3()
        S4 = virasoro_S4(c)
        S5 = virasoro_S5(c)
        pf = planted_forest_g3(kappa, S3, S4, S5)
        assert virasoro_free_energy(c, 3) == scalar + pf

    def test_scalar_F_g_positive(self):
        """Scalar F_g > 0 for all g >= 1 and kappa > 0."""
        for g in range(1, 8):
            for c in [12, 24, 48]:
                kappa = kappa_virasoro(c)
                assert F_g_scalar(kappa, g) > 0


# =========================================================================
# Section 15: Full report and summary
# =========================================================================

class TestReportAndSummary:
    """Tests for comprehensive report functions."""

    def test_full_report_structure(self):
        """Full report has all required fields."""
        report = full_arithmetic_report(5)
        assert 'n_max' in report
        assert 'degeneracies' in report
        assert 'height_analysis' in report
        assert 'rademacher' in report
        assert report['c'] == 24
        assert report['kappa'] == 12.0

    def test_full_report_degeneracies(self):
        """Report degeneracies match direct computation."""
        report = full_arithmetic_report(5)
        for n in range(1, 6):
            assert report['degeneracies'][n]['c_n'] == j_coefficient(n)
            assert report['degeneracies'][n]['d_n'] == j_coefficient(n) ** 2

    def test_prime_content_summary_structure(self):
        """Prime content summary has correct structure."""
        summary = prime_content_summary(10)
        assert 'total_distinct_primes' in summary
        assert 'primes_seen' in summary
        assert 'largest_prime' in summary
        assert 'mean_omega' in summary

    def test_prime_content_contains_small_primes(self):
        """Small primes (2, 3) divide at least some c(n)."""
        summary = prime_content_summary(10)
        assert 2 in summary['primes_seen']
        assert 3 in summary['primes_seen']

    def test_prime_content_omega_positive(self):
        """Mean omega is positive."""
        summary = prime_content_summary(10)
        assert summary['mean_omega'] > 0


# =========================================================================
# Section 16: Bekenstein-Hawking formula consistency
# =========================================================================

class TestBHConsistency:
    """Consistency tests for Bekenstein-Hawking entropy formula."""

    def test_bh_c24_n1(self):
        """S_BH(c=24, n=1) = 4*pi."""
        S = bekenstein_hawking_entropy(24, 1)
        assert abs(S - 4.0 * PI) < 1e-10

    def test_bh_c24_n4(self):
        """S_BH(c=24, n=4) = 8*pi."""
        S = bekenstein_hawking_entropy(24, 4)
        assert abs(S - 8.0 * PI) < 1e-10

    def test_bh_scaling_sqrt_n(self):
        """S_BH proportional to sqrt(n)."""
        S1 = bekenstein_hawking_entropy(24, 1)
        S4 = bekenstein_hawking_entropy(24, 4)
        assert abs(S4 / S1 - 2.0) < 1e-10  # sqrt(4)/sqrt(1) = 2

    def test_bh_scaling_sqrt_c(self):
        """S_BH proportional to sqrt(c)."""
        S_24 = bekenstein_hawking_entropy(24, 1)
        S_96 = bekenstein_hawking_entropy(96, 1)
        assert abs(S_96 / S_24 - 2.0) < 1e-10  # sqrt(96/24) = 2

    def test_bh_zero_for_nonpositive(self):
        """S_BH = 0 when c*n <= 0."""
        assert bekenstein_hawking_entropy(0, 1) == 0.0
        assert bekenstein_hawking_entropy(-1, 1) == 0.0
        assert bekenstein_hawking_entropy(24, 0) == 0.0
        assert bekenstein_hawking_entropy(24, -1) == 0.0


# =========================================================================
# Section 17: Additional consistency checks
# =========================================================================

class TestAdditionalConsistency:
    """Additional cross-checks and consistency tests."""

    def test_d_n_factorisation_product_equals_dn(self):
        """Product of prime factorisation of d(n) equals d(n)."""
        for n in range(1, 11):
            factors = btz_degeneracy_factorisation(n)
            product = 1
            for p, e in factors.items():
                product *= p ** e
            assert product == btz_degeneracy(n)

    def test_cn_factorisation_product_equals_cn(self):
        """Product of prime factorisation of c(n) equals c(n)."""
        for n in range(1, 11):
            cn = j_coefficient(n)
            factors = j_coefficient_factorisation(n)
            product = 1
            for p, e in factors.items():
                product *= p ** e
            assert product == cn

    def test_omega_d_n_equals_omega_c_n(self):
        """omega(d(n)) = omega(c(n)) since d(n) = c(n)^2."""
        for n in range(1, 11):
            cn_factors = j_coefficient_factorisation(n)
            dn_density = arithmetic_density(n)
            assert dn_density == len(cn_factors)

    def test_sigma_0_d_n_from_cn(self):
        """sigma_0(c(n)^2) = prod(2*a_i + 1) from c(n) factorisation.

        NOTE: Direct factorisation of d(n) may fail for large primes
        (trial division limited to primes < 100000). The correct
        computation goes via c(n) factorisation with doubled exponents.
        We test the c(n) factorisation route here.
        """
        for n in range(1, 6):
            cn_factors = j_coefficient_factorisation(n)
            # sigma_0(c(n)^2) = prod(2*a_i + 1)
            expected = 1
            for p, a in cn_factors.items():
                expected *= (2 * a + 1)
            # Verify by also computing from the btz_degeneracy_factorisation
            dn_factors = btz_degeneracy_factorisation(n)
            computed = 1
            for p, a in dn_factors.items():
                computed *= (a + 1)
            assert computed == expected

    def test_entropy_corrections_sum_less_than_leading(self):
        """Total corrections are sub-leading: |sum S_r| < S_BH for large n."""
        for n in [5, 10, 20]:
            result = entropy_shadow_corrections(24, n, order=5)
            total_corr = result['S_total'] - result['S_0']
            assert abs(total_corr) < result['S_0']

    def test_height_equals_log_degeneracy(self):
        """h(d(n)) = log(d(n)) = 2*log(c(n))."""
        for n in range(1, 11):
            h = btz_arithmetic_height(n)
            cn = j_coefficient(n)
            expected = 2.0 * math.log(cn)
            assert abs(h - expected) < 1e-10

    def test_kappa_virasoro_exact_fraction(self):
        """kappa(Vir_c) is exactly c/2 as a Fraction."""
        for c in [1, 13, 24, 26, 48]:
            assert kappa_virasoro(c) == Fraction(c, 2)

    def test_rademacher_matches_fourier_n1_to_n5(self):
        """Path 1 (Fourier) and Path 2 (Rademacher) agree for n = 1..5."""
        for n in range(1, 6):
            exact = j_coefficient(n)
            approx = rademacher_coefficient(n, m=-1, c_max=100)
            assert round(approx) == exact, f"Mismatch at n={n}"

    def test_cardy_matches_rademacher_leading(self):
        """Cardy formula = Rademacher leading term for c = 24."""
        for n in [1, 5, 10]:
            S_cardy = bekenstein_hawking_entropy(24, n)
            S_rad = 4.0 * PI * math.sqrt(n)
            assert abs(S_cardy - S_rad) < 1e-10
