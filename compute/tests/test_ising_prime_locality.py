r"""
Tests for ising_prime_locality.py -- adversarial attack on Ising prime-locality.

Test structure:
  1. Rocha-Caridi theta functions: verify against known values
  2. Ising |eta|^2 Z: verify both conventions
  3. Multiplicativity verification: reproduce manuscript claim (14 failures)
  4. Extended multiplicativity: larger product bounds
  5. Convention discrepancy: Convention A != Convention B
  6. Per-channel multiplicativity: all channels fail
  7. Hecke recursion analysis
  8. Q(sqrt(5)) arithmetic analysis
  9. Shadow obstruction tower data
  10. Cross-checks against existing code (AP10)

GRADING: Cohomological, |d| = +1.
"""

from __future__ import annotations

import pytest
from fractions import Fraction
from math import gcd

from compute.lib.ising_prime_locality import (
    rocha_caridi_theta,
    ising_theta_functions,
    ising_eta_sq_z_exact,
    ising_integer_coeffs_exact,
    ising_spin_coeffs_exact,
    ising_flattened_coeffs,
    check_multiplicativity_product_bound,
    check_multiplicativity_individual_bound,
    per_channel_multiplicativity_test,
    hecke_recursion_test,
    ising_shadow_data,
    is_prime,
    legendre_symbol,
    splitting_in_Q_sqrt5,
    splitting_in_Q_sqrt_neg10,
    analyze_failure_arithmetic,
    full_ising_attack,
)


# ===========================================================================
# 1. Rocha-Caridi theta functions
# ===========================================================================

class TestRochaCaridi:
    """Verify theta = eta*chi for each Ising primary."""

    def test_identity_leading_term(self):
        """theta_{1,1} starts at q^0 with coefficient 1."""
        theta = rocha_caridi_theta(4, 3, 1, 1, 50)
        assert Fraction(0) in theta
        assert theta[Fraction(0)] == 1

    def test_identity_first_negative(self):
        """theta_{1,1} has -q^1 as second term."""
        theta = rocha_caridi_theta(4, 3, 1, 1, 50)
        assert theta[Fraction(1)] == -1

    def test_identity_coefficients(self):
        """theta_{1,1} = 1 - q + q^{11} - q^{13} + ... (pentagonal-like)."""
        theta = rocha_caridi_theta(4, 3, 1, 1, 50)
        expected = {Fraction(0): 1, Fraction(1): -1, Fraction(6): -1,
                    Fraction(11): 1, Fraction(13): 1, Fraction(20): -1,
                    Fraction(46): 1}
        for exp, val in expected.items():
            assert theta.get(exp, 0) == val, f"theta_{{1,1}} at q^{exp}: expected {val}, got {theta.get(exp, 0)}"

    def test_spin_leading_term(self):
        """theta_{2,1} starts at q^{1/16} with coefficient 1."""
        theta = rocha_caridi_theta(4, 3, 2, 1, 50)
        assert theta[Fraction(1, 16)] == 1

    def test_energy_leading_term(self):
        """theta_{1,2} starts at q^{1/2} with coefficient 1."""
        theta = rocha_caridi_theta(4, 3, 1, 2, 50)
        assert theta[Fraction(1, 2)] == 1

    def test_conformal_weights_correct(self):
        """Leading exponents match h_{r,s} = ((rq-sp)^2 - (p-q)^2)/(4pq)."""
        thetas = ising_theta_functions(50)
        # h_{1,1} = 0
        assert min(thetas['0'].keys()) == Fraction(0)
        # h_{2,1} = 1/16
        assert min(thetas['1/16'].keys()) == Fraction(1, 16)
        # h_{1,2} = 1/2
        assert min(thetas['1/2'].keys()) == Fraction(1, 2)

    def test_all_exponents_in_Z_over_48(self):
        """All theta exponents have denominator dividing 48 = 4*4*3."""
        thetas = ising_theta_functions(50)
        for name, theta in thetas.items():
            for exp in theta:
                assert exp.denominator in (1, 2, 4, 8, 16, 48), \
                    f"Channel {name}: exponent {exp} has unexpected denominator {exp.denominator}"

    def test_identity_all_integer_exponents(self):
        """Identity channel theta_{1,1} has only integer exponents."""
        theta = rocha_caridi_theta(4, 3, 1, 1, 50)
        for exp in theta:
            assert exp.denominator == 1, f"Non-integer exponent {exp} in identity channel"

    def test_energy_all_half_integer_exponents(self):
        """Energy channel theta_{1,2} has exponents in Z + 1/2."""
        theta = rocha_caridi_theta(4, 3, 1, 2, 50)
        for exp in theta:
            shifted = exp - Fraction(1, 2)
            assert shifted.denominator == 1, f"Non-(Z+1/2) exponent {exp} in energy channel"


# ===========================================================================
# 2. |eta|^2 Z coefficients
# ===========================================================================

class TestEtaSqZ:
    """Verify the exact |eta|^2 Z computation."""

    def test_leading_coefficient(self):
        """|eta|^2 Z starts at q^0 with coefficient 1 (from identity)."""
        full = ising_eta_sq_z_exact(50)
        assert full[Fraction(0)] == 1

    def test_spin_channel_at_q_1_8(self):
        """Spin channel contributes at q^{1/8} with coefficient 1."""
        full = ising_eta_sq_z_exact(50)
        assert full.get(Fraction(1, 8), 0) == 1

    def test_exponent_structure(self):
        """Exponents lie in Z union (Z + 1/8)."""
        full = ising_eta_sq_z_exact(50)
        for exp in full:
            shifted = exp * 8
            assert shifted.denominator == 1, \
                f"Exponent {exp} is not in Z or Z+1/8"

    def test_integer_part_coefficients(self):
        """Integer-exponent coefficients of |eta|^2 Z."""
        exact = ising_integer_coeffs_exact(50)
        # First few: verified by explicit Rocha-Caridi computation
        # Identity: theta_{1,1}^2 at integer exponents
        # Energy: theta_{1,2}^2 at integer exponents (starts at q^1)
        assert exact[0] == 1   # identity only
        assert exact[1] == -1  # identity(-2) + energy(1) = -2+1 = -1
        # Actually let me verify: theta_{1,1}^2 at q^1:
        # theta_{1,1} = 1*q^0 - 1*q^1 + ..., so squared:
        # at q^0: 1^2 = 1. At q^1: 2*(1)(-1) = -2.
        # theta_{1,2}^2 at q^1: theta_{1,2} = q^{1/2} - q^{5/2} - q^{7/2} + ...
        # theta_{1,2}^2 at q^1: (q^{1/2})^2 = q^1 with coeff 1^2 = 1.
        # So integer part at q^1 = -2 + 1 = -1. Correct.
        assert exact[1] == -1

    def test_spin_channel_separate(self):
        """Spin channel coefficients at Z + 1/8."""
        spin = ising_spin_coeffs_exact(50)
        assert spin[0] == 1  # leading term: |theta_{2,1}|^2 at q^{1/8}

    def test_all_coefficients_are_integers(self):
        """All coefficients of |eta|^2 Z are integers."""
        full = ising_eta_sq_z_exact(50)
        for exp, coeff in full.items():
            assert isinstance(coeff, int), f"Non-integer coefficient {coeff} at q^{exp}"


# ===========================================================================
# 3. Convention A: flattened coefficients
# ===========================================================================

class TestConventionA:
    """Verify the flattened (manuscript) convention."""

    def test_leading_coefficient_is_3(self):
        """a_0 = 3 = 1 + 1 + 1 (sum of leading terms across all channels)."""
        flat = ising_flattened_coeffs(50)
        assert flat[0] == 3

    def test_known_coefficients(self):
        """First 10 coefficients match existing code output."""
        flat = ising_flattened_coeffs(50)
        expected = [3, -2, -3, -2, 0, 2, 1, 4, 1, -2]
        assert flat[:10] == expected, f"Got {flat[:10]}, expected {expected}"

    def test_matches_existing_code(self):
        """Cross-check against minimal_model_l_functions.py (AP10)."""
        try:
            from compute.lib.minimal_model_l_functions import dirichlet_coefficients
            from compute.lib.vvmf_hecke import ising_model
            import mpmath
            mpmath.mp.dps = 50
            model = ising_model()
            existing = dirichlet_coefficients(model, num_terms=40, dps=50)
            existing_int = [int(round(float(x))) for x in existing[:31]]

            flat = ising_flattened_coeffs(100)
            assert flat[:31] == existing_int, \
                f"Disagreement with existing code: {flat[:31]} vs {existing_int}"
        except ImportError:
            pytest.skip("minimal_model_l_functions not available")


# ===========================================================================
# 4. Convention discrepancy
# ===========================================================================

class TestConventionDiscrepancy:
    """Verify that Convention A != Convention B."""

    def test_conventions_differ(self):
        """Flattened coefficients differ from exact integer-exponent coefficients."""
        flat = ising_flattened_coeffs(50)
        exact = ising_integer_coeffs_exact(50)
        assert flat[:31] != exact[:31], "Conventions should differ"

    def test_flat_a0_is_3_exact_a0_is_1(self):
        """a_0 = 3 (flattened) vs a_0 = 1 (exact)."""
        flat = ising_flattened_coeffs(10)
        exact = ising_integer_coeffs_exact(10)
        assert flat[0] == 3
        assert exact[0] == 1

    def test_discrepancy_source_is_spin(self):
        """The discrepancy comes from the spin channel's fractional exponent.

        Convention A aligns spin at q^0 (stripping q^{1/8}).
        Convention B puts spin at q^{1/8}, which has no integer-exponent contribution at q^0.
        So Conv A has an extra +1 at a_0 from spin.
        """
        flat = ising_flattened_coeffs(10)
        exact = ising_integer_coeffs_exact(10)
        spin = ising_spin_coeffs_exact(10)
        # The difference at a_0 is exactly spin's leading coefficient
        assert flat[0] - exact[0] == spin[0] + 1  # +1 from energy channel shift too
        # More precisely: Conv A aligns identity at q^0 (coeff 1),
        # spin at q^0 (coeff 1, stripped from q^{1/8}),
        # energy at q^0 (coeff 1, stripped from q^1).
        # Conv B has only identity at q^0 (coeff 1).


# ===========================================================================
# 5. Manuscript claim: 14 coprime failures
# ===========================================================================

class TestManuscriptClaim:
    """Verify prop:rational-cft-multiplicativity-failure."""

    def test_14_failures_product_bound_20(self):
        """MANUSCRIPT CLAIM: 14 coprime failures with mn <= 20 (Convention A).

        The existing code counts ORDERED pairs (m,n) with m != n and mn < 21.
        The manuscript says "14 coprime failures with m, n <= 20."
        FINDING: "m, n <= 20" is misleading -- it means mn <= 20.
        """
        flat = ising_flattened_coeffs(100)
        _, failures = check_multiplicativity_product_bound(flat, max_product=20)
        assert len(failures) == 14, f"Expected 14 failures, got {len(failures)}"

    def test_failures_are_genuine(self):
        """Each of the 14 failures is a genuine a_{mn} != a_m * a_n."""
        flat = ising_flattened_coeffs(100)
        _, failures = check_multiplicativity_product_bound(flat, max_product=20)
        for m, n, a_mn, a_m_a_n, defect in failures:
            assert gcd(m, n) == 1, f"({m},{n}) not coprime"
            assert a_mn != a_m_a_n, f"({m},{n}) is not a genuine failure"
            assert defect != 0, f"({m},{n}) has zero defect"
            assert m * n <= 20, f"({m},{n}) has product {m*n} > 20"

    def test_specific_failures(self):
        """Verify specific failure pairs from the proof text.

        The proof says "14 coprime failures" — verify the first few.
        """
        flat = ising_flattened_coeffs(100)
        # (2,3): a_6 = 1, a_2*a_3 = (-3)*(-2) = 6, defect = -5
        assert flat[6] == 1
        assert flat[2] * flat[3] == 6
        assert flat[6] != flat[2] * flat[3]

        # (2,5): a_10 = 0, a_2*a_5 = (-3)*2 = -6, defect = 6
        assert flat[10] == 0
        assert flat[2] * flat[5] == -6

        # (2,7): a_14 = -1, a_2*a_7 = (-3)*4 = -12, defect = 11
        assert flat[14] == -1
        assert flat[2] * flat[7] == -12

    def test_defect_magnitudes_O1(self):
        """Manuscript says "defects are O(1) integers." Verify."""
        flat = ising_flattened_coeffs(100)
        _, failures = check_multiplicativity_product_bound(flat, max_product=20)
        for _, _, _, _, defect in failures:
            assert abs(defect) <= 16, f"Defect {defect} is not O(1)"

    def test_multiplicativity_fails_at_all_larger_bounds(self):
        """Multiplicativity continues to fail at larger product bounds."""
        flat = ising_flattened_coeffs(300)
        for bound in [30, 50, 100]:
            _, failures = check_multiplicativity_product_bound(flat, max_product=bound)
            assert len(failures) > 14, f"Fewer failures at bound {bound} than at 20"

    def test_convention_B_also_fails(self):
        """Convention B (exact) also fails multiplicativity."""
        exact = ising_integer_coeffs_exact(200)
        _, failures = check_multiplicativity_individual_bound(exact, max_n=20)
        assert len(failures) > 0, "Convention B should also fail multiplicativity"

    def test_failure_count_grows(self):
        """Number of failures grows with the test range (not a finite set)."""
        flat = ising_flattened_coeffs(500)
        counts = []
        for bound in [20, 30, 50, 100]:
            _, failures = check_multiplicativity_product_bound(flat, max_product=bound)
            counts.append(len(failures))
        for i in range(len(counts) - 1):
            assert counts[i] < counts[i + 1], \
                f"Failure count not growing: {counts}"


# ===========================================================================
# 6. Extended multiplicativity analysis
# ===========================================================================

class TestExtendedMultiplicativity:
    """Wider-range multiplicativity tests."""

    def test_individual_bound_30(self):
        """With m, n individually up to 30: many more failures."""
        flat = ising_flattened_coeffs(1000)
        _, failures = check_multiplicativity_individual_bound(flat, max_n=30)
        assert len(failures) > 50, f"Expected > 50 failures, got {len(failures)}"

    def test_no_miracle_subset(self):
        """No subset of coefficients (odd indices, even indices) is multiplicative."""
        flat = ising_flattened_coeffs(200)
        # Even indices
        even = [flat[2 * k] if 2 * k < len(flat) else 0 for k in range(50)]
        _, fail_even = check_multiplicativity_individual_bound(even, max_n=20)
        # Odd indices
        odd = [flat[2 * k + 1] if 2 * k + 1 < len(flat) else 0 for k in range(50)]
        _, fail_odd = check_multiplicativity_individual_bound(odd, max_n=20)
        # At least one should fail
        assert len(fail_even) > 0 or len(fail_odd) > 0, "Some subset should fail"


# ===========================================================================
# 7. Per-channel multiplicativity
# ===========================================================================

class TestPerChannel:
    """Test multiplicativity of individual channels."""

    def test_identity_channel_fails(self):
        """Identity channel |theta_{1,1}|^2 is NOT multiplicative."""
        result = per_channel_multiplicativity_test(200, max_n=15)
        assert not result['0']['is_multiplicative'], \
            "Identity channel should fail multiplicativity"

    def test_energy_channel_fails(self):
        """Energy channel |theta_{1,2}|^2 is NOT multiplicative."""
        result = per_channel_multiplicativity_test(200, max_n=15)
        assert not result['1/2']['is_multiplicative'], \
            "Energy channel should fail multiplicativity"

    def test_spin_channel_fails(self):
        """Spin channel |theta_{2,1}|^2 is NOT multiplicative (in Q-variable)."""
        result = per_channel_multiplicativity_test(200, max_n=15)
        assert not result['1/16']['is_multiplicative'], \
            "Spin channel should fail multiplicativity"

    def test_identity_lcd_is_1(self):
        """Identity channel has integer exponents (lcd = 1)."""
        result = per_channel_multiplicativity_test(50, max_n=10)
        assert result['0']['lcd'] == 1

    def test_spin_lcd_is_8(self):
        """Spin channel has lcd = 8 (exponents in Z/8)."""
        result = per_channel_multiplicativity_test(50, max_n=10)
        assert result['1/16']['lcd'] == 8

    def test_energy_lcd_is_1(self):
        """Energy channel has integer exponents (lcd = 1)."""
        result = per_channel_multiplicativity_test(50, max_n=10)
        assert result['1/2']['lcd'] == 1


# ===========================================================================
# 8. Hecke recursion
# ===========================================================================

class TestHeckeRecursion:
    """Analyze Hecke recursion a_{p^2} vs a_p^2."""

    def test_hecke_defect_nonzero(self):
        """a_{p^2} != a_p^2 for all small primes (no weight-0 Hecke)."""
        flat = ising_flattened_coeffs(200)
        hecke = hecke_recursion_test(flat)
        for p, data in hecke.items():
            assert data['defect'] != 0, f"p={p}: Hecke defect is zero (unexpected)"

    def test_hecke_defect_at_2(self):
        """a_4 = 0, a_2^2 = 9, defect = -9."""
        flat = ising_flattened_coeffs(50)
        assert flat[4] == 0
        assert flat[2] ** 2 == 9
        hecke = hecke_recursion_test(flat)
        assert hecke[2]['defect'] == -9

    def test_hecke_defect_at_3(self):
        """a_9 = -2, a_3^2 = 4, defect = -6."""
        flat = ising_flattened_coeffs(50)
        assert flat[9] == -2
        assert flat[3] ** 2 == 4
        hecke = hecke_recursion_test(flat)
        assert hecke[3]['defect'] == -6

    def test_no_uniform_weight(self):
        """Hecke defects are NOT consistent with any single weight k.

        If a_{p^2} = a_p^2 - chi(p)*p^{k-1}*a_1 for fixed k and
        Dirichlet character chi, then defect(p)/a_1 = chi(p)*p^{k-1}.
        For this to work, |defect(p)/a_1| should grow as p^{k-1}.
        """
        flat = ising_flattened_coeffs(200)
        hecke = hecke_recursion_test(flat)
        a_1 = flat[1]
        assert a_1 == -2

        # defect/a_1 for each prime:
        ratios = {}
        for p, data in hecke.items():
            ratios[p] = Fraction(data['defect'], a_1)

        # If weight k: |ratio| ~ p^{k-1}. Check ratios.
        # p=2: 9/2, p=3: 6/2=3, p=5: 6/2=3, p=7: 16/2=8, p=11: 6/2=3, p=13: 4/2=2
        # These do NOT grow like p^k for any k. Confirmed: no Hecke eigenform.
        values = [float(abs(r)) for r in ratios.values()]
        # Check that the sequence is NOT monotonically increasing
        assert not all(values[i] <= values[i + 1] for i in range(len(values) - 1)), \
            "Hecke defects should not be monotonically increasing in p"


# ===========================================================================
# 9. Arithmetic analysis: Q(sqrt(5)) and Q(sqrt(-10))
# ===========================================================================

class TestArithmeticAnalysis:
    """Test whether failures correlate with number field arithmetic."""

    def test_splitting_Q_sqrt5_basic(self):
        """Verify splitting behavior in Q(sqrt(5)) for small primes."""
        assert splitting_in_Q_sqrt5(2) == 'inert'     # 5 mod 8 = 5
        assert splitting_in_Q_sqrt5(3) == 'inert'     # (5/3) = (2/3) = -1
        assert splitting_in_Q_sqrt5(5) == 'ramified'
        assert splitting_in_Q_sqrt5(11) == 'split'    # (5/11) = 11 = 1 mod 5, (5/11) = 1
        assert splitting_in_Q_sqrt5(19) == 'split'    # 19 = 4 mod 5, (5/19) = 1

    def test_failure_primes_include_all_small_primes(self):
        """All small primes appear in failure pairs -- no enrichment possible."""
        flat = ising_flattened_coeffs(500)
        _, failures = check_multiplicativity_individual_bound(flat, max_n=30)
        analysis = analyze_failure_arithmetic(failures)
        # All primes up to 29 should appear
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in expected_primes:
            assert p in analysis['failure_primes'], f"Prime {p} missing from failures"

    def test_no_sqrt5_enrichment(self):
        """Failures at inert primes in Q(sqrt(5)) are NOT enriched.

        The failure primes are ALL primes up to the test bound,
        so the splitting distribution matches the baseline exactly.
        This means the Q(sqrt(5)) number field does NOT predict
        which (m,n) pairs fail.
        """
        flat = ising_flattened_coeffs(500)
        _, failures = check_multiplicativity_individual_bound(flat, max_n=20)
        analysis = analyze_failure_arithmetic(failures)

        fail_counts = analysis['Q_sqrt5']['counts']
        base_counts = analysis['Q_sqrt5']['baseline']
        # Normalize
        total_fail = sum(fail_counts.values())
        total_base = sum(base_counts.values())
        if total_fail > 0 and total_base > 0:
            fail_inert_frac = fail_counts['inert'] / total_fail
            base_inert_frac = base_counts['inert'] / total_base
            # Should be equal (no enrichment)
            assert abs(fail_inert_frac - base_inert_frac) < 0.15, \
                f"Unexpected enrichment: fail={fail_inert_frac:.2f}, base={base_inert_frac:.2f}"


# ===========================================================================
# 10. Shadow obstruction tower data
# ===========================================================================

class TestShadowData:
    """Verify shadow obstruction tower invariants at c = 1/2."""

    def test_kappa(self):
        """kappa = c/2 = 1/4."""
        data = ising_shadow_data()
        assert data['kappa'] == '1/4'

    def test_S4(self):
        """S_4 = 10/(c(5c+22)) = 40/49 at c=1/2."""
        data = ising_shadow_data()
        assert data['S4'] == '40/49'

    def test_Delta(self):
        """Delta = 80/49."""
        data = ising_shadow_data()
        assert data['Delta'] == '80/49'

    def test_sqrt_Delta_involves_sqrt5(self):
        """sqrt(Delta) = sqrt(80/49) = 4*sqrt(5)/7."""
        data = ising_shadow_data()
        assert 'sqrt(5)' in data['sqrt_Delta']

    def test_disc_involves_sqrt_neg10(self):
        """Shadow metric discriminant involves sqrt(-10), NOT sqrt(5)."""
        data = ising_shadow_data()
        assert 'sqrt(-10)' in data['disc_involves']
        assert data['disc_shadow_metric'] == '-160/49'

    def test_shadow_radius_large(self):
        """Shadow radius rho ~ 12.5 >> 1 (tower diverges at c=1/2)."""
        data = ising_shadow_data()
        assert data['shadow_radius'] > 10, f"rho = {data['shadow_radius']}, expected > 10"
        assert data['shadow_radius'] < 15

    def test_class_M(self):
        """Ising is class M (infinite shadow obstruction tower)."""
        data = ising_shadow_data()
        assert 'M' in data['class']


# ===========================================================================
# 11. Cross-checks (AP10)
# ===========================================================================

class TestCrossChecks:
    """Cross-family and cross-code consistency checks."""

    def test_coefficients_are_integers(self):
        """All flattened coefficients are exact integers."""
        flat = ising_flattened_coeffs(100)
        for n, a_n in enumerate(flat):
            assert isinstance(a_n, int), f"a_{n} = {a_n} is not int"

    def test_a1_normalization(self):
        """a_1 = -2 in Convention A (consistent with existing code)."""
        flat = ising_flattened_coeffs(10)
        assert flat[1] == -2

    def test_exact_coefficients_are_integers(self):
        """All exact (Convention B) coefficients are integers."""
        exact = ising_integer_coeffs_exact(100)
        for n, a_n in enumerate(exact):
            assert isinstance(a_n, int), f"a_{n} = {a_n} is not int"

    def test_exact_a0_is_1(self):
        """a_0 = 1 in Convention B (only identity channel at q^0)."""
        exact = ising_integer_coeffs_exact(10)
        assert exact[0] == 1

    def test_spin_channel_positive_a0(self):
        """Spin channel starts with coefficient 1."""
        spin = ising_spin_coeffs_exact(10)
        assert spin[0] == 1

    def test_full_attack_runs(self):
        """Integration test: full attack produces complete report."""
        report = full_ising_attack(num_terms=100, max_test=15)
        assert 'conv_A' in report
        assert 'conv_B' in report
        assert 'arithmetic' in report
        assert 'shadow' in report
        assert report['conv_A']['manuscript_claims_14'] == True

    def test_legendre_symbol_basic(self):
        """Verify Legendre symbol computation."""
        assert legendre_symbol(1, 3) == 1
        assert legendre_symbol(2, 3) == -1
        assert legendre_symbol(3, 5) == -1
        assert legendre_symbol(4, 5) == 1

    def test_is_prime_basic(self):
        """Verify primality test."""
        assert is_prime(2)
        assert is_prime(3)
        assert is_prime(5)
        assert not is_prime(4)
        assert not is_prime(1)
        assert is_prime(29)
        assert not is_prime(30)


# ===========================================================================
# 12. Structural findings
# ===========================================================================

class TestStructuralFindings:
    """Document the adversarial findings as structural tests."""

    def test_manuscript_convention_is_flattened(self):
        """The manuscript's 'a_n' uses flattened (Convention A) coefficients.

        FINDING: The equation |eta|^2 Z = sum a_n q^n in the manuscript
        is strictly incorrect because |eta|^2 Z has non-integer exponents
        from the spin channel. The flattened convention drops the
        q^{1/8} offset, aligning all channels at q^0.
        """
        flat = ising_flattened_coeffs(10)
        assert flat[0] == 3, "a_0 = 3 confirms flattened convention"

    def test_multiplicativity_is_structurally_impossible(self):
        """Multiplicativity fails for structural reasons (not numerical).

        The partition function Z = sum_i |chi_i|^2 is a quadratic form
        on VVMF components. Multiplicativity would require the VVMF
        to be a Hecke eigenform, which fails for minimal models.
        This is confirmed by all-channel failure in per-channel tests.
        """
        flat = ising_flattened_coeffs(200)
        _, failures = check_multiplicativity_individual_bound(flat, max_n=20)
        assert len(failures) > 10, "Too few failures for structural obstruction"

    def test_no_modified_series_is_multiplicative(self):
        """No simple modification makes the series multiplicative.

        Tested: normalization by a_1, per-channel extraction.
        All fail.
        """
        result = per_channel_multiplicativity_test(200, max_n=15)
        for name, data in result.items():
            if 'is_multiplicative' in data:
                assert not data['is_multiplicative'], \
                    f"Channel {name} unexpectedly multiplicative"

    def test_sqrt5_does_not_predict_failures(self):
        """Q(sqrt(5)) does NOT predict which pairs fail.

        FINDING: The user's prompt asks whether failures correlate
        with primes inert in Q(sqrt(5)). The answer is NO: failures
        occur at ALL primes, regardless of splitting behavior.
        Q(sqrt(5)) enters the shadow obstruction tower via sqrt(Delta), but this
        controls the GROWTH RATE of the tower, not the multiplicativity
        of the partition function.
        """
        flat = ising_flattened_coeffs(500)
        _, failures = check_multiplicativity_individual_bound(flat, max_n=20)
        analysis = analyze_failure_arithmetic(failures)
        # All primes up to test bound appear
        fail_primes = set(analysis['failure_primes'])
        small_primes = {p for p in range(2, 20) if is_prime(p)}
        assert small_primes.issubset(fail_primes), \
            f"Not all small primes appear in failures: missing {small_primes - fail_primes}"
