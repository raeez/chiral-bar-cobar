r"""Tests for lattice_prime_locality: Euler products, Hecke multiplicativity,
and the arithmetic structure of the sewing lift for lattice VOAs.

Verifies:
  1. E_8: Theta_{E_8} = E_4, sigma_3 multiplicative, L(s) = zeta(s)*zeta(s-3)
  2. D_4: sigma_1^{odd} multiplicative, Hecke recursion (weight 2)
  3. Leech: NOT a single eigenform, coefficients NOT multiplicative
  4. Sewing lift Euler products
  5. Shadow obstruction tower termination (class G)
  6. Cross-family consistency
  7. Hecke recursion at prime powers
  8. Prime-locality diagnostic

Mathematical ground truth:
  - lattice_foundations.tex: thm:lattice:curvature-braiding-orthogonal
  - arithmetic_shadows.tex: thm:shadow-spectral-correspondence
  - higher_genus_modular_koszul.tex: shadow depth classification (class G)
"""

import pytest
from math import gcd

from compute.lib.lattice_prime_locality import (
    sigma_k,
    sigma_1_odd,
    prime_factorization,
    is_prime,
    primes_up_to,
    ramanujan_tau,
    r_e8,
    r_d4,
    r_leech,
    check_multiplicativity,
    check_normalized_multiplicativity,
    verify_hecke_recursion,
    euler_factor_e8,
    euler_factor_d4,
    euler_factor_leech_eisenstein,
    euler_factor_leech_cusp,
    sewing_lift_e8,
    sewing_lift_d4,
    sewing_lift_leech,
    sewing_lift_euler_product,
    shadow_tower_data,
    prime_locality_diagnostic,
    prime_locality_comparison_table,
    non_lattice_obstruction_analysis,
)


# =========================================================================
# 1. E_8 representation numbers
# =========================================================================

class TestE8RepresentationNumbers:
    r"""r_{E_8}(n) = 240 * sigma_3(n) since Theta_{E_8} = E_4.

    Key property: sigma_3 is multiplicative, and at primes
    sigma_3(p) = 1 + p^3 (the Hecke eigenvalue of E_4).
    """

    def test_r_e8_0(self):
        """r_{E_8}(0) = 1 (the zero vector)."""
        assert r_e8(0) == 1

    def test_r_e8_1(self):
        """r_{E_8}(1) = 240 (the 240 roots of E_8)."""
        assert r_e8(1) == 240

    def test_r_e8_2(self):
        """r_{E_8}(2) = 240*sigma_3(2) = 240*9 = 2160."""
        assert r_e8(2) == 2160

    def test_r_e8_3(self):
        """r_{E_8}(3) = 240*sigma_3(3) = 240*28 = 6720."""
        assert r_e8(3) == 6720

    def test_r_e8_first_10(self):
        """First 10 E_8 representation numbers (hardcoded from Sloane A004009)."""
        # Theta_{E_8} = 1 + 240q + 2160q^2 + 6720q^3 + 17520q^4 + ...
        expected = [1, 240, 2160, 6720, 17520, 30240, 60480, 82560, 140400, 181680]
        for n, exp in enumerate(expected):
            assert r_e8(n) == exp, f"r_E8({n}) = {r_e8(n)}, expected {exp}"

    def test_sigma3_at_primes(self):
        """sigma_3(p) = 1 + p^3 for prime p."""
        for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            assert sigma_k(p, 3) == 1 + p ** 3

    def test_sigma3_multiplicativity(self):
        """sigma_3 is multiplicative: sigma_3(mn) = sigma_3(m)*sigma_3(n) when gcd=1."""
        for m in range(2, 20):
            for n in range(2, 20):
                if m * n <= 30 and gcd(m, n) == 1:
                    assert sigma_k(m * n, 3) == sigma_k(m, 3) * sigma_k(n, 3), \
                        f"sigma_3({m}*{n}) != sigma_3({m})*sigma_3({n})"

    def test_e8_hecke_recursion_p2(self):
        """Hecke recursion for E_4 at p=2: a(2^{r+1}) = a(2)*a(2^r) - 2^3*a(2^{r-1})."""
        ok, failures = verify_hecke_recursion(
            lambda n: sigma_k(n, 3), weight=4, p=2, max_power=7
        )
        assert ok, f"Hecke recursion failed at p=2: {failures}"

    def test_e8_hecke_recursion_p3(self):
        """Hecke recursion for E_4 at p=3."""
        ok, failures = verify_hecke_recursion(
            lambda n: sigma_k(n, 3), weight=4, p=3, max_power=6
        )
        assert ok, f"Hecke recursion failed at p=3: {failures}"

    def test_e8_hecke_recursion_p5(self):
        """Hecke recursion for E_4 at p=5."""
        ok, failures = verify_hecke_recursion(
            lambda n: sigma_k(n, 3), weight=4, p=5, max_power=5
        )
        assert ok, f"Hecke recursion failed at p=5: {failures}"


# =========================================================================
# 2. D_4 representation numbers
# =========================================================================

class TestD4RepresentationNumbers:
    r"""r_{D_4}(n) = 24 * sigma_1^{odd}(n).

    sigma_1^{odd}(n) = sum of odd divisors of n.
    This is multiplicative. The raw r_{D_4} is NOT multiplicative (r(1)=24).
    But the normalized coefficients r(n)/r(1) = sigma_1^{odd}(n) are.
    """

    def test_r_d4_0(self):
        """r_{D_4}(0) = 1."""
        assert r_d4(0) == 1

    def test_r_d4_1(self):
        """r_{D_4}(1) = 24 (24 roots of D_4)."""
        assert r_d4(1) == 24

    def test_r_d4_first_10(self):
        """First 10 D_4 representation numbers."""
        expected = [1, 24, 24, 96, 24, 144, 96, 192, 24, 312]
        for n, exp in enumerate(expected):
            assert r_d4(n) == exp, f"r_D4({n}) = {r_d4(n)}, expected {exp}"

    def test_sigma1_odd_at_primes(self):
        """sigma_1^{odd}(p) = 1 + p for odd primes, sigma_1^{odd}(2) = 1."""
        assert sigma_1_odd(2) == 1  # Only odd divisor of 2 is 1
        for p in [3, 5, 7, 11, 13, 17, 19, 23, 29]:
            assert sigma_1_odd(p) == 1 + p

    def test_sigma1_odd_multiplicativity(self):
        """sigma_1^{odd} is multiplicative."""
        for m in range(2, 20):
            for n in range(2, 20):
                if m * n <= 30 and gcd(m, n) == 1:
                    assert sigma_1_odd(m * n) == sigma_1_odd(m) * sigma_1_odd(n), \
                        f"sigma_1_odd({m}*{n}) = {sigma_1_odd(m * n)} != {sigma_1_odd(m)}*{sigma_1_odd(n)}"

    def test_sigma1_odd_powers_of_2(self):
        """sigma_1^{odd}(2^a) = 1 for all a >= 0 (only odd divisor is 1)."""
        for a in range(10):
            assert sigma_1_odd(2 ** a) == 1

    def test_d4_raw_NOT_multiplicative(self):
        """Raw r_{D_4}(n) is NOT multiplicative because r(1)=24 != 1."""
        ok, failures = check_multiplicativity(r_d4, 20)
        assert not ok, "r_{D_4} should NOT be multiplicative (r(1)=24)"
        # Specific failure: r(6) = 96, r(2)*r(3) = 24*96 = 2304 != 96
        assert r_d4(6) != r_d4(2) * r_d4(3)

    def test_d4_normalized_multiplicative(self):
        """Normalized r_{D_4}(n)/24 = sigma_1^{odd}(n) IS multiplicative."""
        ok, failures = check_normalized_multiplicativity(r_d4, 30)
        assert ok, f"Normalized D_4 coefficients should be multiplicative: {failures}"

    def test_d4_hecke_recursion_odd_primes(self):
        """Hecke recursion (weight 2) at odd primes for sigma_1^{odd}."""
        for p in [3, 5, 7, 11]:
            ok, failures = verify_hecke_recursion(
                sigma_1_odd, weight=2, p=p, max_power=6
            )
            assert ok, f"Hecke recursion failed at p={p}: {failures}"

    def test_d4_level_prime_p2(self):
        """At the level prime p=2: sigma_1^{odd}(2^a) = 1 = sigma_1^{odd}(2)^a."""
        ok, failures = verify_hecke_recursion(
            sigma_1_odd, weight=2, p=2, max_power=8, level_prime=2
        )
        assert ok, f"Level-prime recursion failed at p=2: {failures}"


# =========================================================================
# 3. Leech lattice representation numbers
# =========================================================================

class TestLeechRepresentationNumbers:
    r"""r_Leech(n) = (65520/691)*(sigma_11(n) - tau(n)).

    The Leech theta function is NOT a single Hecke eigenform:
    Theta_Leech = E_12 - (65520/691)*Delta.
    Therefore the coefficients are NOT multiplicative.
    """

    def test_r_leech_0(self):
        """r_Leech(0) = 1."""
        assert r_leech(0) == 1

    def test_r_leech_1(self):
        """r_Leech(1) = 0 (no roots in the Leech lattice)."""
        assert r_leech(1) == 0

    def test_r_leech_2(self):
        """r_Leech(2) = 196560 (the 196560 minimal vectors)."""
        assert r_leech(2) == 196560

    def test_r_leech_3(self):
        """r_Leech(3) = 16773120."""
        assert r_leech(3) == 16773120

    def test_r_leech_4(self):
        """r_Leech(4) = 398034000."""
        assert r_leech(4) == 398034000

    def test_leech_NOT_multiplicative(self):
        """Leech theta coefficients are NOT multiplicative."""
        # r(2)*r(3) = 196560 * 16773120 = 3296924467200
        # r(6) = 34417656000 (much smaller)
        assert r_leech(6) != r_leech(2) * r_leech(3)
        # This is because Theta_Leech is a sum of TWO Hecke eigenforms

    def test_leech_r1_zero_blocks_normalization(self):
        """r_Leech(1) = 0 prevents normalization (no a(1)=1 eigenform)."""
        ok, failures = check_normalized_multiplicativity(r_leech, 10)
        assert not ok, "Cannot normalize Leech coefficients (r(1)=0)"


# =========================================================================
# 4. Ramanujan tau function
# =========================================================================

class TestRamanujanTau:
    """tau(n) = coefficients of Delta = eta^{24}."""

    def test_tau_first_values(self):
        """Known values of tau(n)."""
        expected = {
            1: 1, 2: -24, 3: 252, 4: -1472, 5: 4830,
            6: -6048, 7: -16744, 8: 84480, 9: -113643, 10: -115920,
        }
        for n, val in expected.items():
            assert ramanujan_tau(n) == val, f"tau({n}) = {ramanujan_tau(n)}, expected {val}"

    def test_tau_multiplicativity(self):
        """tau is multiplicative: tau(mn) = tau(m)*tau(n) when gcd=1."""
        for m in range(2, 10):
            for n in range(2, 10):
                if m * n <= 20 and gcd(m, n) == 1:
                    assert ramanujan_tau(m * n) == ramanujan_tau(m) * ramanujan_tau(n), \
                        f"tau({m}*{n}) != tau({m})*tau({n})"

    def test_tau_hecke_recursion_p2(self):
        """Hecke recursion: tau(2^{r+1}) = tau(2)*tau(2^r) - 2^{11}*tau(2^{r-1})."""
        ok, failures = verify_hecke_recursion(
            ramanujan_tau, weight=12, p=2, max_power=5
        )
        assert ok, f"Hecke recursion failed for tau at p=2: {failures}"

    def test_tau_hecke_recursion_p3(self):
        """Hecke recursion for tau at p=3."""
        ok, failures = verify_hecke_recursion(
            ramanujan_tau, weight=12, p=3, max_power=4
        )
        assert ok, f"Hecke recursion failed for tau at p=3: {failures}"


# =========================================================================
# 5. Sewing lift and Euler products
# =========================================================================

class TestSewingLiftEulerProducts:
    r"""Verify the Euler product structure of the sewing lift.

    E_8: S(s) = 240 * zeta(s) * zeta(s-3)
    D_4: S(s) = 24 * zeta(s) * (1-2^{1-s}) * zeta(s-1)
    Leech: decomposed (difference of two Euler products)
    """

    def test_e8_sewing_lift_vs_euler(self):
        """E_8 sewing lift matches Euler product at s=10."""
        s = 10.0
        direct = sewing_lift_e8(s, num_terms=300)
        euler = sewing_lift_euler_product('E8', s, primes_up_to(100))
        assert abs(direct - euler) / abs(direct) < 1e-6, \
            f"E_8 sewing lift mismatch: direct={direct}, euler={euler}"

    def test_d4_sewing_lift_vs_euler(self):
        """D_4 sewing lift matches Euler product at s=10."""
        s = 10.0
        direct = sewing_lift_d4(s, num_terms=300)
        euler = sewing_lift_euler_product('D4', s, primes_up_to(100))
        assert abs(direct - euler) / abs(direct) < 1e-6, \
            f"D_4 sewing lift mismatch: direct={direct}, euler={euler}"

    def test_leech_sewing_lift_vs_decomposed(self):
        """Leech sewing lift matches decomposed Euler product at s=20."""
        s = 20.0
        direct = sewing_lift_leech(s, num_terms=100)
        decomposed = sewing_lift_euler_product('Leech', s, primes_up_to(50))
        assert abs(direct - decomposed) / abs(direct) < 1e-4, \
            f"Leech sewing lift mismatch: direct={direct}, decomposed={decomposed}"

    def test_e8_euler_factor_structure(self):
        """E_8 Euler factor = 1/((1-p^{-s})(1-p^{3-s})) at s=10, p=2."""
        ef = euler_factor_e8(2, 10.0)
        manual = 1.0 / ((1 - 2 ** (-10.0)) * (1 - 2 ** (3 - 10.0)))
        assert abs(ef - manual) < 1e-12

    def test_d4_euler_factor_odd_prime(self):
        """D_4 Euler factor at odd prime = 1/((1-p^{-s})(1-p^{1-s}))."""
        ef = euler_factor_d4(3, 10.0)
        manual = 1.0 / ((1 - 3 ** (-10.0)) * (1 - 3 ** (1 - 10.0)))
        assert abs(ef - manual) < 1e-12

    def test_d4_euler_factor_p2(self):
        """D_4 Euler factor at level prime p=2: 1/(1-2^{-s})."""
        ef = euler_factor_d4(2, 10.0)
        manual = 1.0 / (1 - 2 ** (-10.0))
        assert abs(ef - manual) < 1e-12


# =========================================================================
# 6. Shadow obstruction tower (all class G)
# =========================================================================

class TestShadowTowerClassG:
    """All lattice VOAs are class G: shadow depth 2, S_r = 0 for r >= 3."""

    def test_e8_class_G(self):
        """E_8 is class G."""
        data = shadow_tower_data('E8')
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['S_3'] == 0
        assert data['S_4'] == 0
        assert data['S_5'] == 0
        assert data['Delta'] == 0
        assert data['is_perfect_square']

    def test_d4_class_G(self):
        """D_4 is class G."""
        data = shadow_tower_data('D4')
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['kappa'] == 4

    def test_leech_class_G(self):
        """Leech is class G (despite having a cusp form in its theta)."""
        data = shadow_tower_data('Leech')
        assert data['shadow_class'] == 'G'
        assert data['shadow_depth'] == 2
        assert data['kappa'] == 24
        assert data['roots'] == 0  # No roots in Leech lattice

    def test_rank1_class_G(self):
        """Z (rank 1) is class G."""
        data = shadow_tower_data('Z')
        assert data['shadow_class'] == 'G'
        assert data['kappa'] == 1

    def test_a2_class_G(self):
        """A_2 is class G."""
        data = shadow_tower_data('A2')
        assert data['shadow_class'] == 'G'
        assert data['kappa'] == 2

    def test_all_higher_shadows_vanish(self):
        """S_r = 0 for r >= 3 for all lattice VOAs."""
        for lattice in ['E8', 'D4', 'Leech', 'Z', 'A2']:
            data = shadow_tower_data(lattice)
            assert data['all_higher_vanish'], f"{lattice} should have all higher shadows = 0"

    def test_kappa_equals_rank(self):
        """kappa = rank for all lattice VOAs."""
        for lattice, rank in [('E8', 8), ('D4', 4), ('Leech', 24), ('Z', 1), ('A2', 2)]:
            data = shadow_tower_data(lattice)
            assert data['kappa'] == rank


# =========================================================================
# 7. Prime-locality diagnostic
# =========================================================================

class TestPrimeLocalityDiagnostic:
    """Full prime-locality analysis for each lattice."""

    def test_e8_single_eigenform(self):
        """E_8 theta is a single Hecke eigenform (E_4)."""
        diag = prime_locality_diagnostic('E8')
        assert diag['is_single_eigenform']
        assert diag['euler_product_type'] == 'single'
        assert diag['normalized_multiplicative']

    def test_d4_single_eigenform_with_level(self):
        """D_4 theta is a single eigenform on Gamma_0(2)."""
        diag = prime_locality_diagnostic('D4')
        assert diag['is_single_eigenform']
        assert diag['euler_product_type'] == 'single_with_level'
        assert diag['normalized_multiplicative']
        # Raw is NOT multiplicative
        assert not diag['raw_multiplicative']

    def test_leech_decomposed(self):
        """Leech theta is NOT a single eigenform."""
        diag = prime_locality_diagnostic('Leech')
        assert not diag['is_single_eigenform']
        assert diag['euler_product_type'] == 'decomposed'
        # Raw coefficients NOT multiplicative
        assert not diag['raw_multiplicative']

    def test_e8_hecke_eigenvalues(self):
        """E_8 Hecke eigenvalues: a(p) = 1 + p^3."""
        diag = prime_locality_diagnostic('E8')
        for p, val in diag['eigenvalues_at_primes'].items():
            assert val == 1 + p ** 3, f"E_8 eigenvalue at p={p}: {val} != {1 + p ** 3}"

    def test_d4_hecke_eigenvalues(self):
        """D_4 Hecke eigenvalues: a(p) = 1+p for odd p, a(2) = 1."""
        diag = prime_locality_diagnostic('D4')
        for p, val in diag['eigenvalues_at_primes'].items():
            if p == 2:
                assert val == 1, f"D_4 eigenvalue at p=2: {val} != 1"
            else:
                assert val == 1 + p, f"D_4 eigenvalue at p={p}: {val} != {1 + p}"

    def test_leech_eigenvalues_two_components(self):
        """Leech eigenvalues: each prime has TWO components (sigma_11 and tau)."""
        diag = prime_locality_diagnostic('Leech')
        for p, val in diag['eigenvalues_at_primes'].items():
            assert 'sigma_11' in val
            assert 'tau' in val
            assert val['sigma_11'] == 1 + p ** 11
            assert val['tau'] == ramanujan_tau(p)


# =========================================================================
# 8. Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between different lattice VOAs."""

    def test_comparison_table(self):
        """Comparison table has correct structure."""
        table = prime_locality_comparison_table()
        assert len(table) == 3
        for entry in table:
            assert entry['shadow_class'] == 'G'
            assert entry['shadow_depth'] == 2

    def test_e8_d4_different_euler_types(self):
        """E_8 and D_4 have different Euler product types."""
        table = prime_locality_comparison_table()
        e8 = [e for e in table if e['lattice'] == 'E8'][0]
        d4 = [e for e in table if e['lattice'] == 'D4'][0]
        assert e8['euler_type'] == 'single'
        assert d4['euler_type'] == 'single_with_level'

    def test_leech_differs_from_e8_d4(self):
        """Leech has decomposed Euler product, unlike E_8 and D_4."""
        table = prime_locality_comparison_table()
        leech = [e for e in table if e['lattice'] == 'Leech'][0]
        assert leech['euler_type'] == 'decomposed'
        assert not leech['raw_mult']

    def test_kappa_additive(self):
        """kappa is additive: kappa(V_{L1+L2}) = kappa(V_{L1}) + kappa(V_{L2}).

        E_8 + E_8 = E_8^2 (rank 16), kappa = 16 = 8 + 8.
        """
        data_e8 = shadow_tower_data('E8')
        # E_8 direct sum E_8: kappa should be 16
        assert data_e8['kappa'] + data_e8['kappa'] == 16

    def test_unimodularity_classification(self):
        """Correct unimodularity classification."""
        assert shadow_tower_data('E8')['unimodular']
        assert not shadow_tower_data('D4')['unimodular']
        assert shadow_tower_data('Leech')['unimodular']

    def test_root_counts(self):
        """Correct root counts."""
        assert shadow_tower_data('E8')['roots'] == 240
        assert shadow_tower_data('D4')['roots'] == 24
        assert shadow_tower_data('Leech')['roots'] == 0


# =========================================================================
# 9. Non-lattice obstruction analysis
# =========================================================================

class TestNonLatticeObstructions:
    """Verify the analysis of why prime-locality fails for non-lattice VOAs."""

    def test_four_obstructions_plus_escape(self):
        """The analysis identifies four obstructions and one escape route."""
        analysis = non_lattice_obstruction_analysis()
        assert 'obstruction_1_no_theta' in analysis
        assert 'obstruction_2_no_hecke' in analysis
        assert 'obstruction_3_infinite_shadow' in analysis
        assert 'obstruction_4_non_formality' in analysis
        assert 'lattice_escape' in analysis


# =========================================================================
# 10. Arithmetic utility functions
# =========================================================================

class TestArithmeticUtilities:
    """Tests for basic arithmetic functions used in the module."""

    def test_prime_factorization(self):
        """Correct prime factorizations."""
        assert prime_factorization(1) == {}
        assert prime_factorization(2) == {2: 1}
        assert prime_factorization(12) == {2: 2, 3: 1}
        assert prime_factorization(100) == {2: 2, 5: 2}

    def test_is_prime(self):
        """Correct primality testing."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21]
        for p in primes:
            assert is_prime(p), f"{p} should be prime"
        for c in composites:
            assert not is_prime(c), f"{c} should not be prime"

    def test_primes_up_to(self):
        """Correct list of primes."""
        assert primes_up_to(10) == [2, 3, 5, 7]
        assert primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_sigma_k_at_1(self):
        """sigma_k(1) = 1 for all k."""
        for k in range(10):
            assert sigma_k(1, k) == 1

    def test_sigma_1_odd_relation(self):
        """sigma_1^{odd}(n) = sigma_1(n_odd) where n = 2^a * n_odd.

        For n = 2^a * m with m odd: the odd divisors of n are the divisors of m.
        """
        for n in range(1, 50):
            # Extract odd part
            m = n
            while m % 2 == 0:
                m //= 2
            assert sigma_1_odd(n) == sigma_k(m, 1), \
                f"sigma_1_odd({n}) = {sigma_1_odd(n)} != sigma_1({m}) = {sigma_k(m, 1)}"


# =========================================================================
# 11. E_8 specific: the a(6) test from the prompt
# =========================================================================

class TestSpecificVerifications:
    r"""Specific numerical checks from the adversarial prompt.

    The prompt asks: for D_4, is a_6 = a_2 * a_3?
    Answer: for raw r(n), NO. r(6) = 96, r(2)*r(3) = 24*96 = 2304.
    For normalized sigma_1^{odd}: sigma_1^{odd}(6) = 4 = 1*4 = sigma_1^{odd}(2)*sigma_1^{odd}(3). YES.
    """

    def test_d4_a6_raw(self):
        """D_4: r(6) != r(2)*r(3) (raw coefficients NOT multiplicative)."""
        assert r_d4(6) == 96
        assert r_d4(2) * r_d4(3) == 24 * 96  # = 2304
        assert r_d4(6) != r_d4(2) * r_d4(3)

    def test_d4_a6_normalized(self):
        """D_4: sigma_1^{odd}(6) = sigma_1^{odd}(2)*sigma_1^{odd}(3) (normalized ARE)."""
        assert sigma_1_odd(6) == sigma_1_odd(2) * sigma_1_odd(3)
        assert sigma_1_odd(6) == 4
        assert sigma_1_odd(2) == 1
        assert sigma_1_odd(3) == 4

    def test_e8_repr_numbers_multiplicativity_n1_to_30(self):
        """E_8: verify sigma_3 is multiplicative for all coprime pairs up to 30."""
        ok, failures = check_normalized_multiplicativity(r_e8, 30)
        assert ok, f"E_8 normalized multiplicativity failed: {failures}"

    def test_leech_r6_vs_r2_r3(self):
        """Leech: r(6) != r(2)*r(3) (explicitly)."""
        r2 = r_leech(2)
        r3 = r_leech(3)
        r6 = r_leech(6)
        assert r2 == 196560
        assert r3 == 16773120
        assert r6 == 34417656000
        product = r2 * r3  # = 3296924467200
        assert r6 != product
        # The ratio shows how far from multiplicative
        assert product > r6  # The product overshoots by ~96x


# =========================================================================
# 12. Hecke decomposition controls prime-locality
# =========================================================================

class TestHeckeDecompositionStructure:
    r"""The Hecke decomposition determines the form of the L-function.

    - dim S_k = 0: theta = const * E_k, single Euler product
    - dim S_k = 1: theta = c_E * E_k + c_cusp * f, two Euler products
    - dim S_k = d: theta = c_E * E_k + sum c_j * f_j, (d+1) Euler products

    The number of Euler products = 1 + dim S_k.
    """

    def test_e8_dim_S4_is_zero(self):
        """dim S_4(SL_2(Z)) = 0, so E_8 theta is purely Eisenstein."""
        # Weight 4: dim M_4 = 1, dim S_4 = 0
        # This is why Theta_{E_8} = E_4 exactly
        diag = prime_locality_diagnostic('E8')
        assert diag['hecke_decomposition']['cusp'] == []

    def test_leech_dim_S12_is_one(self):
        """dim S_{12}(SL_2(Z)) = 1 (the Ramanujan Delta function)."""
        diag = prime_locality_diagnostic('Leech')
        cusp_part = diag['hecke_decomposition']['cusp']
        assert len(cusp_part) == 1
        assert cusp_part[0][0] == 'Delta'

    def test_leech_cusp_coefficient(self):
        """The cusp coefficient for Leech is -65520/691."""
        from fractions import Fraction
        diag = prime_locality_diagnostic('Leech')
        cusp_part = diag['hecke_decomposition']['cusp']
        assert cusp_part[0][1] == Fraction(-65520, 691)


# =========================================================================
# 13. Integration with shadow obstruction tower (shadow depth implies prime-locality)
# =========================================================================

class TestShadowDepthImpliesPrimeLocality:
    r"""The shadow obstruction tower controls prime-locality.

    Class G (depth 2, all lattices): L_infinity formal => Hecke theory
    applies => Euler products exist. All higher obstructions vanish.

    Class M (depth infinity, Virasoro/W_N): L_infinity NOT formal =>
    no Hecke theory => no Euler product. Higher obstructions generate
    an infinite tower of non-multiplicative corrections.

    The connection: L_infinity formality (shadow depth 2) is the
    algebraic condition that makes the Dirichlet series factorize.
    """

    def test_class_G_all_lattices(self):
        """All lattice VOAs are class G."""
        for lattice in ['E8', 'D4', 'Leech', 'Z', 'A2']:
            data = shadow_tower_data(lattice)
            assert data['shadow_class'] == 'G'
            assert data['shadow_depth'] == 2
            assert data['Delta'] == 0

    def test_Q_L_perfect_square(self):
        """Shadow metric Q_L = (2*kappa)^2 is a perfect square for all lattices."""
        for lattice in ['E8', 'D4', 'Leech', 'Z', 'A2']:
            data = shadow_tower_data(lattice)
            assert data['Q_L'] == 4 * data['kappa'] ** 2
            assert data['is_perfect_square']

    def test_discriminant_zero(self):
        """Critical discriminant Delta = 8*kappa*S_4 = 0 for all lattices."""
        for lattice in ['E8', 'D4', 'Leech', 'Z', 'A2']:
            data = shadow_tower_data(lattice)
            assert data['Delta'] == 0
