"""Tests for compute/lib/wk_and_bracket_verifications.py

Task 1: Witten-Kontsevich intersection numbers through genus 3.
Task 2: Bracket bilinear form for Leech lattice 2x2.

Ground truth:
  - g=0: <tau_0^3> = 1 (fundamental class of Mbar_{0,3})
  - g=1: <tau_1> = 1/24 (Euler characteristic of Mbar_{1,1})
  - g=2: <tau_4> = 1/1152 (Faber's tables)
  - g=3: <tau_7> = 1/82944 (Faber's tables)
  - String equation, dilaton equation, DVV/Virasoro constraints
  - Ramanujan tau function: tau(n) for n = 1..12
  - Leech lattice theta decomposition: c_E = 1, c_Delta = -65520/691
  - Hecke orthogonality: bracket matrix is diagonal

References:
  thm:shadow-archetype-classification (concordance.tex)
  Witten, Two-dimensional gravity (1990)
  Kontsevich, Intersection theory on moduli (1992)
  Faber, Algorithms for intersection numbers (2007)
"""

import pytest
from fractions import Fraction
from math import factorial

# Reset mpmath precision (may be lowered by earlier test modules)
try:
    import mpmath
    mpmath.mp.dps = 50
except ImportError:
    pass

from compute.lib.wk_and_bracket_verifications import (
    # WK internals
    _dim_check,
    _stability_check,
    _double_factorial_odd,
    _partitions_into_n,
    # WK main
    wk_correlator,
    wk_table,
    # WK verification
    verify_string_equation,
    verify_dilaton_equation,
    double_factorial,
    genus_g_free_energy_coefficients,
    correlator_via_dilaton_chain,
    # Leech lattice
    ramanujan_tau,
    RAMANUJAN_TAU_TABLE,
    eisenstein_eigenvalue,
    cusp_eigenvalue,
    sigma_k,
    hecke_eigenvalue_n,
    _prime_factorization,
    leech_theta_decomposition,
    leech_shadow_component,
    bracket_matrix,
    bracket_matrix_rational,
    bracket_signature,
    bracket_cusp_positive,
    bracket_proportionality_check,
    leech_bracket_table,
    _petersson_norm_delta_sq,
    _regularized_eisenstein_norm_sq,
    LEECH_RANK,
    LEECH_MIN_NORM,
    LEECH_THETA_COEFFS,
)


# =========================================================================
# Part 1: Witten-Kontsevich intersection numbers
# =========================================================================


class TestDimensionAndStability:
    """Test dimension and stability checks."""

    def test_dim_g0_n3_all_zero(self):
        """g=0, n=3, d=(0,0,0): sum=0 = 3*0-3+3 = 0. Passes."""
        assert _dim_check(0, (0, 0, 0))

    def test_dim_g0_n3_sum1(self):
        """g=0, n=3, d=(0,0,1): sum=1 != 0. Fails."""
        assert not _dim_check(0, (0, 0, 1))

    def test_dim_g1_n1_tau1(self):
        """g=1, n=1, d=(1,): sum=1 = 3-3+1 = 1. Passes."""
        assert _dim_check(1, (1,))

    def test_dim_g2_n1_tau4(self):
        """g=2, n=1, d=(4,): sum=4 = 6-3+1 = 4. Passes."""
        assert _dim_check(2, (4,))

    def test_dim_g3_n1_tau7(self):
        """g=3, n=1, d=(7,): sum=7 = 9-3+1 = 7. Passes."""
        assert _dim_check(3, (7,))

    def test_stability_g0_n2(self):
        """g=0, n=2: 2*0-2+2 = 0, unstable."""
        assert not _stability_check(0, 2)

    def test_stability_g0_n3(self):
        """g=0, n=3: 2*0-2+3 = 1 > 0, stable."""
        assert _stability_check(0, 3)

    def test_stability_g1_n0(self):
        """g=1, n=0: 2-2+0 = 0, unstable."""
        assert not _stability_check(1, 0)

    def test_stability_g1_n1(self):
        """g=1, n=1: 2-2+1 = 1 > 0, stable."""
        assert _stability_check(1, 1)


class TestDoubleFactorial:
    """Test double factorial computation."""

    def test_dfact_0(self):
        assert _double_factorial_odd(0) == 1   # 1!!

    def test_dfact_1(self):
        assert _double_factorial_odd(1) == 3   # 3!!

    def test_dfact_2(self):
        assert _double_factorial_odd(2) == 15  # 5!!

    def test_dfact_3(self):
        assert _double_factorial_odd(3) == 105  # 7!!

    def test_dfact_4(self):
        assert _double_factorial_odd(4) == 945  # 9!!

    def test_dfact_neg1(self):
        """(-1)!! = 1 by convention."""
        assert _double_factorial_odd(-1) == 1

    def test_standalone_double_factorial(self):
        assert double_factorial(1) == 1
        assert double_factorial(3) == 3
        assert double_factorial(5) == 15
        assert double_factorial(7) == 105
        assert double_factorial(9) == 945


class TestPartitions:
    """Test partition generation."""

    def test_partition_0_into_0(self):
        assert _partitions_into_n(0, 0) == [()]

    def test_partition_3_into_1(self):
        assert _partitions_into_n(3, 1) == [(3,)]

    def test_partition_2_into_2(self):
        result = _partitions_into_n(2, 2)
        assert (0, 2) in result
        assert (1, 1) in result
        assert len(result) == 2

    def test_partition_3_into_3(self):
        result = _partitions_into_n(3, 3)
        assert (0, 0, 3) in result
        assert (0, 1, 2) in result
        assert (1, 1, 1) in result
        assert len(result) == 3


class TestWKGenus0:
    """Genus 0 intersection numbers."""

    def test_tau0_cubed(self):
        """<tau_0^3>_0 = 1. Fundamental class of Mbar_{0,3}."""
        assert wk_correlator(0, (0, 0, 0)) == Fraction(1)

    def test_tau1_genus0_unstable(self):
        """<tau_1>_0 = 0. Unstable: n=1, g=0."""
        assert wk_correlator(0, (1,)) == Fraction(0)

    def test_tau0_4_tau1(self):
        """<tau_0^4 tau_1>_0: dim = 1 != 2. Zero."""
        assert wk_correlator(0, (0, 0, 0, 0, 1)) == Fraction(0)

    def test_tau0_tau0_tau2(self):
        """<tau_0^2 tau_2>_0: dim check sum=2, need 3*0-3+3=0. 2 != 0. Zero."""
        assert wk_correlator(0, (0, 0, 2)) == Fraction(0)

    def test_genus0_4point(self):
        """<tau_0 tau_0 tau_0 tau_1>_0 = 1. By string/dilaton from <tau_0^3>."""
        # dim: sum=1, n=4, need 4-3=1. OK.
        assert wk_correlator(0, (0, 0, 0, 1)) == Fraction(1)

    def test_genus0_5point_all_tau0_tau2(self):
        """<tau_0^3 tau_2>_0: dim = 2, need 4-3=1. Fails (2 != 1). Zero."""
        assert wk_correlator(0, (0, 0, 0, 2)) == Fraction(0)

    def test_genus0_string_tau0_cubed_tau1(self):
        """By string: <tau_0^3 tau_1>_0 = 3 * <tau_0^3>_0 = ... wait.
        String removes one tau_0: <tau_0 * (tau_0, tau_0, tau_1)>_0.
        For d=0 in (tau_0, tau_0, tau_1): skip.
        For d=0 in (tau_0, tau_0, tau_1): skip.
        For d=1 in (tau_0, tau_0, tau_1): <tau_0^3>_0 = 1.
        So result = 1."""
        assert wk_correlator(0, (0, 0, 0, 1)) == Fraction(1)

    def test_genus0_tau1_cubed_via_dilaton(self):
        """<tau_1^3>_0: dim=3, n=3, need 0. 3 != 0. Zero."""
        assert wk_correlator(0, (1, 1, 1)) == Fraction(0)

    def test_genus0_high_point(self):
        """<tau_0^5 tau_2>_0: dim=2, n=6, need 3. 2 != 3. Zero."""
        assert wk_correlator(0, (0, 0, 0, 0, 0, 2)) == Fraction(0)


class TestWKGenus1:
    """Genus 1 intersection numbers."""

    def test_tau1_genus1(self):
        """<tau_1>_1 = 1/24. From L_0 Virasoro constraint."""
        assert wk_correlator(1, (1,)) == Fraction(1, 24)

    def test_tau0_tau2_genus1(self):
        """<tau_0 tau_2>_1 = 1/24. By string equation from <tau_1>_1."""
        assert wk_correlator(1, (0, 2)) == Fraction(1, 24)

    def test_tau1_squared_genus1(self):
        """<tau_1^2>_1 = 1/24. By dilaton: (2-2+1)*<tau_1>_1 = 1/24."""
        assert wk_correlator(1, (1, 1)) == Fraction(1, 24)

    def test_tau0_tau1_tau2_genus1(self):
        """<tau_0 tau_1 tau_2>_1 = 1/12. String: <tau_0 tau_2> + <tau_1^2> = 1/12."""
        assert wk_correlator(1, (0, 1, 2)) == Fraction(1, 12)

    def test_tau1_cubed_genus1(self):
        """<tau_1^3>_1: dilaton twice gives (2-2+2)*<tau_1^2>_1 = 2/24 = 1/12."""
        assert wk_correlator(1, (1, 1, 1)) == Fraction(1, 12)

    def test_tau0_squared_tau3_genus1(self):
        """<tau_0^2 tau_3>_1 = 1/24. By two string reductions."""
        assert wk_correlator(1, (0, 0, 3)) == Fraction(1, 24)

    def test_genus1_4pt_0013(self):
        """<tau_0 tau_0 tau_1 tau_3>_1: dim=4=4. OK."""
        assert wk_correlator(1, (0, 0, 1, 3)) == Fraction(1, 8)

    def test_genus1_4pt_0022(self):
        """<tau_0^2 tau_2^2>_1: dim=4=4. OK."""
        assert wk_correlator(1, (0, 0, 2, 2)) == Fraction(1, 6)

    def test_genus1_4pt_0112(self):
        """<tau_0 tau_1^2 tau_2>_1: dim=4=4."""
        assert wk_correlator(1, (0, 1, 1, 2)) == Fraction(1, 4)

    def test_genus1_4pt_1111(self):
        """<tau_1^4>_1: by dilaton, (2-2+3)*<tau_1^3>_1 = 3/12 = 1/4."""
        assert wk_correlator(1, (1, 1, 1, 1)) == Fraction(1, 4)

    def test_genus1_all_reduce_to_base(self):
        """All genus-1 correlators with only tau_0 and tau_1 ultimately
        reduce to <tau_1>_1 = 1/24 via string/dilaton."""
        # <tau_0^{2k} tau_1>_1 = 1/24 for all k (string eq is identity here)
        for k in range(5):
            ins = tuple([0] * (2 * k)) + (1,)
            # dim: sum=1, n=2k+1, need 2k+1. 1 != 2k+1 for k >= 1. ZERO.
            if k == 0:
                assert wk_correlator(1, ins) == Fraction(1, 24)
            else:
                assert wk_correlator(1, ins) == Fraction(0)


class TestWKGenus2:
    """Genus 2 intersection numbers."""

    def test_tau4_genus2(self):
        """<tau_4>_2 = 1/1152. From Faber's tables."""
        assert wk_correlator(2, (4,)) == Fraction(1, 1152)

    def test_tau0_tau5_genus2(self):
        """<tau_0 tau_5>_2 = 1/1152. By string from <tau_4>_2."""
        assert wk_correlator(2, (0, 5)) == Fraction(1, 1152)

    def test_tau1_tau4_genus2(self):
        """<tau_1 tau_4>_2 = (2*2-2+1)*<tau_4>_2 = 3/1152 = 1/384."""
        assert wk_correlator(2, (1, 4)) == Fraction(1, 384)

    def test_tau2_tau3_genus2(self):
        """<tau_2 tau_3>_2 = 29/5760. From DVV recursion."""
        assert wk_correlator(2, (2, 3)) == Fraction(29, 5760)

    def test_genus2_3pt_024(self):
        """<tau_0 tau_2 tau_4>_2 = 11/1440."""
        assert wk_correlator(2, (0, 2, 4)) == Fraction(11, 1440)

    def test_genus2_3pt_114(self):
        """<tau_1^2 tau_4>_2 = 1/96. Dilaton from <tau_1 tau_4>_2."""
        assert wk_correlator(2, (1, 1, 4)) == Fraction(1, 96)

    def test_genus2_3pt_222(self):
        """<tau_2^3>_2 = 7/240."""
        assert wk_correlator(2, (2, 2, 2)) == Fraction(7, 240)

    def test_genus2_3pt_033(self):
        """<tau_0 tau_3^2>_2 = 29/2880."""
        assert wk_correlator(2, (0, 3, 3)) == Fraction(29, 2880)

    def test_genus2_wrong_dim_fails(self):
        """<tau_3 tau_1>_2: sum=4, need 5. Zero."""
        assert wk_correlator(2, (1, 3)) == Fraction(0)

    def test_genus2_wrong_dim_tau2_squared(self):
        """<tau_2^2>_2: sum=4, need 5. Zero."""
        assert wk_correlator(2, (2, 2)) == Fraction(0)


class TestWKGenus3:
    """Genus 3 intersection numbers."""

    def test_tau7_genus3(self):
        """<tau_7>_3 = 1/82944. From Faber's tables."""
        assert wk_correlator(3, (7,)) == Fraction(1, 82944)

    def test_tau1_tau7_genus3(self):
        """<tau_1 tau_7>_3 = 5/82944. Dilaton from <tau_7>_3."""
        assert wk_correlator(3, (1, 7)) == Fraction(5, 82944)

    def test_tau2_tau6_genus3(self):
        """<tau_2 tau_6>_3 = 77/414720. From DVV."""
        assert wk_correlator(3, (2, 6)) == Fraction(77, 414720)

    def test_tau3_tau5_genus3(self):
        """<tau_3 tau_5>_3 = 503/1451520."""
        assert wk_correlator(3, (3, 5)) == Fraction(503, 1451520)

    def test_tau4_squared_genus3(self):
        """<tau_4^2>_3 = 607/1451520."""
        assert wk_correlator(3, (4, 4)) == Fraction(607, 1451520)

    def test_tau0_tau8_genus3(self):
        """<tau_0 tau_8>_3 = 1/82944. By string from <tau_7>_3."""
        assert wk_correlator(3, (0, 8)) == Fraction(1, 82944)


class TestStringEquation:
    """Verify string equation: <tau_0 tau_S>_g = sum_i <..tau_{d_i-1}..>_g."""

    def test_string_g0_tau0_cubed_tau1(self):
        """String eq applied to <tau_0^3 tau_1>_0 = <tau_0^3>_0 = 1."""
        assert verify_string_equation(0, (0, 0, 1))

    def test_string_g0_4pt(self):
        assert verify_string_equation(0, (0, 0, 1))

    def test_string_g1_tau2(self):
        assert verify_string_equation(1, (2,))

    def test_string_g1_tau1_tau2(self):
        assert verify_string_equation(1, (1, 2))

    def test_string_g2_tau5(self):
        assert verify_string_equation(2, (5,))

    def test_string_g2_tau2_tau3(self):
        assert verify_string_equation(2, (2, 3))


class TestDilatonEquation:
    """Verify dilaton equation: <tau_1 tau_S>_g = (2g-2+|S|) <tau_S>_g."""

    def test_dilaton_g1_tau1(self):
        assert verify_dilaton_equation(1, (1,))

    def test_dilaton_g1_tau2(self):
        assert verify_dilaton_equation(1, (2,))

    def test_dilaton_g2_tau4(self):
        assert verify_dilaton_equation(2, (4,))

    def test_dilaton_g2_tau2_tau3(self):
        assert verify_dilaton_equation(2, (2, 3))

    def test_dilaton_g3_tau7(self):
        assert verify_dilaton_equation(3, (7,))


class TestWKSymmetry:
    """Test symmetry properties of WK correlators."""

    def test_permutation_invariance_g0(self):
        """<tau_{d_1}...tau_{d_n}> is symmetric in the d_i."""
        val1 = wk_correlator(0, (0, 0, 0, 1))
        val2 = wk_correlator(0, (1, 0, 0, 0))
        val3 = wk_correlator(0, (0, 1, 0, 0))
        assert val1 == val2 == val3

    def test_permutation_invariance_g2(self):
        val1 = wk_correlator(2, (1, 2, 3))
        val2 = wk_correlator(2, (3, 1, 2))
        val3 = wk_correlator(2, (2, 3, 1))
        assert val1 == val2 == val3

    def test_negative_insertions_zero(self):
        """Negative d_i gives zero."""
        assert wk_correlator(0, (-1, 0, 0)) == Fraction(0)
        assert wk_correlator(1, (-2,)) == Fraction(0)

    def test_empty_correlator_zero(self):
        """Empty insertion list gives zero."""
        assert wk_correlator(0, ()) == Fraction(0)
        assert wk_correlator(1, ()) == Fraction(0)


class TestWKConsistency:
    """Cross-consistency checks between genera."""

    def test_dilaton_chain_g1(self):
        """<tau_1>_1 via direct = 1/24."""
        assert correlator_via_dilaton_chain(1, 1) == Fraction(1, 24)

    def test_dilaton_chain_g2(self):
        """<tau_4>_2 via direct = 1/1152."""
        assert correlator_via_dilaton_chain(2, 4) == Fraction(1, 1152)

    def test_dilaton_chain_g3(self):
        """<tau_7>_3 via direct = 1/82944."""
        assert correlator_via_dilaton_chain(3, 7) == Fraction(1, 82944)

    def test_genus0_many_tau0(self):
        """<tau_0^n tau_{n-3}>_0 = 1 for all n >= 3."""
        for n in range(3, 8):
            ins = tuple([0] * (n - 1)) + (n - 3,)
            assert wk_correlator(0, ins) == Fraction(1)

    def test_genus1_dilaton_tower(self):
        """<tau_1^n>_1 = (n-1)!/24 for n >= 1 (factorial growth from dilaton).

        Dilaton: <tau_1 X>_g = (2g-2+|X|)<X>_g.
        <tau_1^n>_1 = (n-1) * <tau_1^{n-1}>_1.
        So <tau_1^n>_1 = (n-1)! / 24 for n >= 1 (with 0! = 1).
        """
        for n in range(1, 6):
            expected = Fraction(factorial(n - 1), 24)
            val = wk_correlator(1, tuple([1] * n))
            assert val == expected, f"<tau_1^{n}>_1 = {val} != {expected}"


class TestWKTable:
    """Test the table generation function."""

    def test_table_genus0(self):
        table = wk_table(max_genus=0)
        assert (0, (0, 0, 0)) in table
        assert table[(0, (0, 0, 0))] == Fraction(1)

    def test_table_genus1(self):
        table = wk_table(max_genus=1)
        assert (1, (1,)) in table
        assert table[(1, (1,))] == Fraction(1, 24)

    def test_table_genus2(self):
        table = wk_table(max_genus=2)
        assert (2, (4,)) in table
        assert table[(2, (4,))] == Fraction(1, 1152)


# =========================================================================
# Part 2: Leech lattice bracket bilinear form
# =========================================================================


class TestRamanujanTau:
    """Test Ramanujan tau function."""

    @pytest.mark.parametrize("n,expected", list(RAMANUJAN_TAU_TABLE.items()))
    def test_tau_known_values(self, n, expected):
        assert ramanujan_tau(n) == expected

    def test_tau_zero(self):
        assert ramanujan_tau(0) == 0

    def test_tau_negative(self):
        assert ramanujan_tau(-1) == 0

    def test_tau_multiplicativity(self):
        """tau(mn) = tau(m)*tau(n) for gcd(m,n)=1."""
        # tau(6) = tau(2)*tau(3) since gcd(2,3)=1
        assert ramanujan_tau(6) == ramanujan_tau(2) * ramanujan_tau(3)
        # tau(10) = tau(2)*tau(5)
        assert ramanujan_tau(10) == ramanujan_tau(2) * ramanujan_tau(5)

    def test_tau_hecke_recurrence(self):
        """tau(p^2) = tau(p)^2 - p^{11} for prime p."""
        # tau(4) = tau(2)^2 - 2^{11}
        assert ramanujan_tau(4) == ramanujan_tau(2) ** 2 - 2 ** 11
        # tau(9) = tau(3)^2 - 3^{11}
        assert ramanujan_tau(9) == ramanujan_tau(3) ** 2 - 3 ** 11

    def test_tau_ramanujan_bound(self):
        """Deligne's theorem: |tau(p)| <= 2*p^{11/2} for prime p."""
        import math
        for p in [2, 3, 5, 7, 11]:
            bound = 2 * p ** (11 / 2)
            assert abs(ramanujan_tau(p)) <= bound + 1  # +1 for float rounding


class TestEisensteinEigenvalue:
    """Test Eisenstein eigenvalues."""

    def test_p2(self):
        assert eisenstein_eigenvalue(2) == 1 + 2 ** 11  # 2049

    def test_p3(self):
        assert eisenstein_eigenvalue(3) == 1 + 3 ** 11  # 177148

    def test_p5(self):
        assert eisenstein_eigenvalue(5) == 1 + 5 ** 11


class TestHeckeEigenvalueN:
    """Test Hecke eigenvalues at composite n."""

    def test_n1(self):
        assert hecke_eigenvalue_n(1, "eisenstein") == 1
        assert hecke_eigenvalue_n(1, "cusp") == 1

    def test_n_prime_eisenstein(self):
        """At primes, should match eisenstein_eigenvalue."""
        for p in [2, 3, 5, 7]:
            assert hecke_eigenvalue_n(p, "eisenstein") == eisenstein_eigenvalue(p)

    def test_n_prime_cusp(self):
        """At primes, should match cusp_eigenvalue."""
        for p in [2, 3, 5, 7]:
            assert hecke_eigenvalue_n(p, "cusp") == cusp_eigenvalue(p)

    def test_n4_eisenstein(self):
        """lambda_E(4) = lambda_E(2)^2 - 2^{11}."""
        lam2 = eisenstein_eigenvalue(2)
        expected = lam2 ** 2 - 2 ** 11
        assert hecke_eigenvalue_n(4, "eisenstein") == expected

    def test_n6_cusp(self):
        """lambda_Delta(6) = tau(2)*tau(3) since gcd(2,3)=1."""
        assert hecke_eigenvalue_n(6, "cusp") == ramanujan_tau(2) * ramanujan_tau(3)


class TestSigmaK:
    """Test divisor sum function."""

    def test_sigma0(self):
        """sigma_0(n) = number of divisors."""
        assert sigma_k(1, 0) == 1
        assert sigma_k(6, 0) == 4  # 1,2,3,6

    def test_sigma1(self):
        """sigma_1(n) = sum of divisors."""
        assert sigma_k(6, 1) == 12  # 1+2+3+6
        assert sigma_k(12, 1) == 28

    def test_sigma11_at_primes(self):
        """sigma_11(p) = 1 + p^{11} for prime p."""
        for p in [2, 3, 5]:
            assert sigma_k(p, 11) == eisenstein_eigenvalue(p)


class TestPrimeFactorization:
    """Test prime factorization."""

    def test_prime(self):
        assert _prime_factorization(7) == {7: 1}

    def test_prime_power(self):
        assert _prime_factorization(8) == {2: 3}

    def test_composite(self):
        assert _prime_factorization(12) == {2: 2, 3: 1}


class TestLeechThetaDecomposition:
    """Test theta function decomposition."""

    def test_coefficients(self):
        c_E, c_Delta = leech_theta_decomposition()
        assert c_E == Fraction(1)
        assert c_Delta == Fraction(-65520, 691)

    def test_q0_coefficient(self):
        """Constant term of theta = 1 = c_E * 1 + c_Delta * 0."""
        c_E, c_Delta = leech_theta_decomposition()
        # E_{12} has constant term 1, Delta has constant term 0
        assert c_E * 1 + c_Delta * 0 == 1

    def test_q1_coefficient_vanishes(self):
        """Coefficient of q^1 in theta_Lambda = 0 (no norm-2 vectors)."""
        c_E, c_Delta = leech_theta_decomposition()
        # q^1 coeff of E_{12} is 65520/691, of Delta is 1
        e12_q1 = Fraction(65520, 691)
        delta_q1 = Fraction(1)
        assert c_E * e12_q1 + c_Delta * delta_q1 == 0

    def test_q2_coefficient(self):
        """Coefficient of q^2 = 196560 (kissing number of Leech)."""
        c_E, c_Delta = leech_theta_decomposition()
        # q^2 coeff of E_{12} is (65520/691) * sigma_11(2) = (65520/691) * 2049
        e12_q2 = Fraction(65520, 691) * sigma_k(2, 11)
        delta_q2 = Fraction(ramanujan_tau(2))  # -24
        computed = c_E * e12_q2 + c_Delta * delta_q2
        assert computed == Fraction(196560)


class TestLeechShadowComponent:
    """Test shadow Sh_r projected onto Hecke eigenspaces."""

    def test_eisenstein_r2(self):
        """Sh_2^E = c_E * lambda_E^1 = 1 * 2049 = 2049."""
        assert leech_shadow_component(2, "eisenstein") == Fraction(2049)

    def test_cusp_r2(self):
        """Sh_2^Delta = c_Delta * lambda_Delta^1 = (-65520/691) * (-24)."""
        c_E, c_Delta = leech_theta_decomposition()
        expected = c_Delta * Fraction(-24)
        assert leech_shadow_component(2, "cusp") == expected

    def test_cusp_r3(self):
        """Sh_3^Delta = c_Delta * (-24)^2 = c_Delta * 576."""
        c_E, c_Delta = leech_theta_decomposition()
        expected = c_Delta * Fraction(576)
        assert leech_shadow_component(3, "cusp") == expected


class TestBracketMatrixRational:
    """Test the rational (structural) part of the bracket matrix."""

    def test_diagonal(self):
        """Bracket matrix is diagonal (Hecke orthogonality)."""
        for r in range(2, 5):
            for s in range(r, 5):
                B = bracket_matrix_rational(r, s)
                assert B[0][1] == Fraction(0)
                assert B[1][0] == Fraction(0)

    def test_eisenstein_block_positive(self):
        """Eisenstein block c_E^2 * lambda_E^{r+s-2} is always positive."""
        for r in range(2, 5):
            for s in range(r, 5):
                B = bracket_matrix_rational(r, s)
                assert B[0][0] > 0

    def test_cusp_block_sign(self):
        """Cusp block: c_Delta^2 * (-24)^{r+s-2}. Positive iff r+s even."""
        for r in range(2, 5):
            for s in range(r, 5):
                B = bracket_matrix_rational(r, s)
                if (r + s) % 2 == 0:
                    assert B[1][1] > 0
                else:
                    assert B[1][1] < 0

    def test_scaling_consistency(self):
        """B(r+1,s) / B(r,s) should scale by eigenvalue on each block."""
        lam_E = Fraction(eisenstein_eigenvalue(2))
        lam_Delta = Fraction(cusp_eigenvalue(2))
        r, s = 2, 2
        B1 = bracket_matrix_rational(r, s)
        B2 = bracket_matrix_rational(r + 1, s)
        # Eisenstein: ratio = lambda_E
        assert B2[0][0] == B1[0][0] * lam_E
        # Cusp: ratio = lambda_Delta
        assert B2[1][1] == B1[1][1] * lam_Delta


class TestBracketMatrixFull:
    """Test the full bracket matrix with Petersson norms."""

    def test_diagonal_structure(self):
        """Full bracket matrix is diagonal."""
        import mpmath
        B = bracket_matrix(2, 2)
        assert B[0][1] == mpmath.mpf(0)
        assert B[1][0] == mpmath.mpf(0)

    def test_both_entries_nonzero(self):
        """Both diagonal entries are nonzero for r=s=2."""
        B = bracket_matrix(2, 2)
        assert B[0][0] != 0
        assert B[1][1] != 0

    def test_eisenstein_entry_positive(self):
        """Eisenstein entry is always positive."""
        for r in range(2, 5):
            for s in range(r, 5):
                B = bracket_matrix(r, s)
                assert B[0][0] > 0


class TestBracketSignature:
    """Test bracket matrix signature."""

    def test_signature_even_sum(self):
        """When r+s is even, signature should be (2,0)."""
        assert bracket_signature(2, 2) == (2, 0)
        assert bracket_signature(2, 4) == (2, 0)
        assert bracket_signature(3, 3) == (2, 0)
        assert bracket_signature(4, 4) == (2, 0)

    def test_signature_odd_sum(self):
        """When r+s is odd, cusp block flips sign: signature (1,1)."""
        assert bracket_signature(2, 3) == (1, 1)
        assert bracket_signature(3, 4) == (1, 1)


class TestBracketCuspPositive:
    """Test positivity on the cusp subspace."""

    def test_cusp_positive_even_sum(self):
        """Cusp block positive when r+s even."""
        assert bracket_cusp_positive(2, 2) is True
        assert bracket_cusp_positive(3, 3) is True
        assert bracket_cusp_positive(4, 4) is True

    def test_cusp_negative_odd_sum(self):
        """Cusp block negative when r+s odd (lambda_Delta = -24 < 0)."""
        assert bracket_cusp_positive(2, 3) is False
        assert bracket_cusp_positive(3, 4) is False


class TestBracketProportionality:
    """Test that B is proportional to diag(||E||^2, ||Delta||^2)."""

    def test_proportionality_structure(self):
        """The scaling factors should match the exact rational computation."""
        import mpmath
        mpmath.mp.dps = 50
        result = bracket_proportionality_check(2, 2)
        # Eisenstein scale = c_E^2 * lambda_E^{r+s-2} = 1 * 2049^2
        expected_E = mpmath.mpf(2049) ** 2
        assert mpmath.almosteq(result["eisenstein_scale"], expected_E, 1e-40)

    def test_ratio_r2s2(self):
        """Ratio of scaling factors at r=s=2."""
        result = bracket_proportionality_check(2, 2)
        # ratio = (c_E^2 * lambda_E^2) / (c_Delta^2 * lambda_Delta^2)
        # = (1 * 2049^2) / ((65520/691)^2 * 576)
        import mpmath
        mpmath.mp.dps = 50
        c_D = mpmath.mpf(65520) / mpmath.mpf(691)
        expected_ratio = mpmath.mpf(2049) ** 2 / (c_D ** 2 * mpmath.mpf(576))
        assert mpmath.almosteq(result["ratio"], expected_ratio, 1e-40)


class TestBracketTable:
    """Test the bracket table generation."""

    def test_table_contains_all_pairs(self):
        table = leech_bracket_table(r_max=4)
        for r in range(2, 5):
            for s in range(r, 5):
                assert (r, s) in table

    def test_table_symmetry(self):
        """B(r,s) == B(s,r) since bracket is symmetric."""
        import mpmath
        table_full = {}
        for r in range(2, 5):
            for s in range(2, 5):
                table_full[(r, s)] = bracket_matrix(r, s)
        for r in range(2, 5):
            for s in range(2, 5):
                for i in range(2):
                    for j in range(2):
                        assert mpmath.almosteq(
                            table_full[(r, s)][i][j],
                            table_full[(s, r)][i][j],
                            1e-40
                        )


class TestPeterssonNorms:
    """Test Petersson norm computations."""

    def test_delta_norm_order_of_magnitude(self):
        """||Delta||^2 ~ 10^{-6}."""
        import mpmath
        mpmath.mp.dps = 50
        norm = _petersson_norm_delta_sq()
        assert mpmath.mpf("1e-7") < norm < mpmath.mpf("1e-5")

    def test_eisenstein_norm_positive(self):
        """Regularized ||E_{12}||^2 > 0."""
        import mpmath
        mpmath.mp.dps = 50
        norm = _regularized_eisenstein_norm_sq(12)
        assert norm > 0

    def test_eisenstein_norm_small(self):
        """Regularized ||E_{12}||^2 is a small positive number."""
        import mpmath
        mpmath.mp.dps = 50
        norm = _regularized_eisenstein_norm_sq(12)
        # Should be much smaller than 1 (Gamma(11)/(4*pi)^{12} ~ 10^{-7})
        assert norm < 1


class TestLeechLatticeConstants:
    """Test Leech lattice parameters."""

    def test_rank(self):
        assert LEECH_RANK == 24

    def test_min_norm(self):
        """Leech lattice has no vectors of norm 2."""
        assert LEECH_MIN_NORM == 4

    def test_theta_constant_term(self):
        assert LEECH_THETA_COEFFS[0] == 1

    def test_kissing_number(self):
        """196560 vectors of norm 4 (kissing number)."""
        assert LEECH_THETA_COEFFS[2] == 196560
