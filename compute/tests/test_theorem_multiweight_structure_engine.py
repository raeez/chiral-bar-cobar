r"""Tests for the multi-weight structural theorem engine.

Verifies all structural properties of the cross-channel correction
delta_F_g^cross(W_3, c) at genus g = 2, 3, 4.

40+ tests organized by structural theorem:
  (S1) Betti decomposition
  (S2) Numerator degree
  (S3) Positivity
  (S4) Tree vanishing
  (S5) Large-c ratio
  (S6) Betti coefficient match
  (S7) Koszul asymmetry
  (S8) Propagator variance independence
  Cross-verification against existing engines

Multi-path verification mandate: every numerical result confirmed by 3+ paths.
"""

import unittest
from fractions import Fraction
from math import factorial


from compute.lib.theorem_multiweight_structure_engine import (
    # Basics
    bernoulli,
    lambda_fp,
    # Betti coefficients
    BETTI_COEFFICIENTS,
    betti_coefficient,
    betti_decomposition,
    # Closed forms
    NUMERATOR_COEFFICIENTS,
    DENOMINATOR_CONSTANTS,
    delta_Fg_closed,
    delta_Fg_from_betti,
    # Structural invariants
    numerator_degree,
    denominator_power,
    net_degree,
    tree_stratum_vanishes,
    nonzero_strata_count,
    # Large-c ratio
    large_c_ratio,
    LARGE_C_RATIOS,
    # Inter-stratum ratios
    inter_stratum_ratio,
    max_betti_ratio,
    max_betti_coefficient,
    max_betti_growth_ratio,
    MAX_BETTI_GROWTH,
    # Denominator
    factorize,
    DENOMINATOR_FACTORIZATIONS,
    # Koszul
    W3_KOSZUL_CONDUCTOR,
    koszul_dual_c,
    koszul_asymmetry,
    koszul_sum,
    # Positivity
    all_coefficients_positive,
    all_betti_positive,
    positivity_at_c,
    # Verification
    verify_closed_vs_betti,
    verify_large_c_ratio,
    verify_denominator_factorization,
    # Summary
    structural_summary,
    genus_tower_summary,
    cross_channel_dominance_genus,
    betti_dominance_pattern,
)


# ============================================================================
# (S1) Betti decomposition
# ============================================================================

class TestBettiDecomposition(unittest.TestCase):
    """Verify the Betti stratum decomposition (S1)."""

    def test_g2_strata_count(self):
        """g=2 has 3 Betti strata (h=0,1,2) but h=0 vanishes."""
        d = betti_decomposition(2)
        self.assertEqual(len(d), 3)

    def test_g3_strata_count(self):
        """g=3 has 4 Betti strata (h=0,1,2,3)."""
        d = betti_decomposition(3)
        self.assertEqual(len(d), 4)

    def test_g4_strata_count(self):
        """g=4 has 5 Betti strata (h=0,1,2,3,4)."""
        d = betti_decomposition(4)
        self.assertEqual(len(d), 5)

    def test_g2_alpha_values(self):
        """Exact Betti coefficients at g=2."""
        self.assertEqual(betti_coefficient(2, 0), Fraction(0))
        self.assertEqual(betti_coefficient(2, 1), Fraction(1, 16))
        self.assertEqual(betti_coefficient(2, 2), Fraction(51, 4))

    def test_g3_alpha_values(self):
        """Exact Betti coefficients at g=3."""
        self.assertEqual(betti_coefficient(3, 0), Fraction(1, 27648))
        self.assertEqual(betti_coefficient(3, 1), Fraction(79, 2880))
        self.assertEqual(betti_coefficient(3, 2), Fraction(133, 16))
        self.assertEqual(betti_coefficient(3, 3), Fraction(6281, 4))

    def test_g4_alpha_values(self):
        """Exact Betti coefficients at g=4."""
        self.assertEqual(betti_coefficient(4, 0), Fraction(41, 2488320))
        self.assertEqual(betti_coefficient(4, 1), Fraction(89627, 5806080))
        self.assertEqual(betti_coefficient(4, 2), Fraction(229079, 34560))
        self.assertEqual(betti_coefficient(4, 3), Fraction(163829, 96))
        self.assertEqual(betti_coefficient(4, 4), Fraction(5138841, 16))

    def test_betti_vs_closed_g2(self):
        """Betti decomposition matches closed form at g=2, multiple c values."""
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(cv)
            self.assertTrue(verify_closed_vs_betti(2, c),
                            f"Mismatch at g=2, c={cv}")

    def test_betti_vs_closed_g3(self):
        """Betti decomposition matches closed form at g=3, multiple c values."""
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(cv)
            self.assertTrue(verify_closed_vs_betti(3, c),
                            f"Mismatch at g=3, c={cv}")

    def test_betti_vs_closed_g4(self):
        """Betti decomposition matches closed form at g=4, multiple c values."""
        for cv in [1, 2, 5, 10, 26, 50, 100]:
            c = Fraction(cv)
            self.assertTrue(verify_closed_vs_betti(4, c),
                            f"Mismatch at g=4, c={cv}")


# ============================================================================
# (S2) Numerator degree
# ============================================================================

class TestNumeratorDegree(unittest.TestCase):
    """Verify the numerator degree pattern (S2)."""

    def test_degree_g2(self):
        self.assertEqual(numerator_degree(2), 1)

    def test_degree_g3(self):
        self.assertEqual(numerator_degree(3), 3)

    def test_degree_g4(self):
        self.assertEqual(numerator_degree(4), 4)

    def test_net_degree_g2(self):
        """Net degree = 0 at g=2 (constant at large c)."""
        self.assertEqual(net_degree(2), 0)

    def test_net_degree_g3(self):
        """Net degree = 1 at g=3 (linear growth)."""
        self.assertEqual(net_degree(3), 1)

    def test_net_degree_g4(self):
        """Net degree = 1 at g=4 (linear growth)."""
        self.assertEqual(net_degree(4), 1)

    def test_denominator_power(self):
        """Denominator power = g-1."""
        for g in [2, 3, 4]:
            self.assertEqual(denominator_power(g), g - 1)

    def test_coefficient_count_matches_degree(self):
        """Number of numerator coefficients = deg + 1."""
        for g in [2, 3, 4]:
            self.assertEqual(len(NUMERATOR_COEFFICIENTS[g]),
                             numerator_degree(g) + 1)


# ============================================================================
# (S3) Positivity
# ============================================================================

class TestPositivity(unittest.TestCase):
    """Verify positivity of all coefficients (S3)."""

    def test_all_numerator_positive_g2(self):
        self.assertTrue(all_coefficients_positive(2))

    def test_all_numerator_positive_g3(self):
        self.assertTrue(all_coefficients_positive(3))

    def test_all_numerator_positive_g4(self):
        self.assertTrue(all_coefficients_positive(4))

    def test_all_betti_positive_g2(self):
        self.assertTrue(all_betti_positive(2))

    def test_all_betti_positive_g3(self):
        self.assertTrue(all_betti_positive(3))

    def test_all_betti_positive_g4(self):
        self.assertTrue(all_betti_positive(4))

    def test_positivity_at_integer_c_g2(self):
        """delta_F_2 > 0 for all positive integer c."""
        for cv in [1, 2, 5, 10, 13, 26, 50, 100, 1000]:
            self.assertTrue(positivity_at_c(2, Fraction(cv)),
                            f"Failed at c={cv}")

    def test_positivity_at_integer_c_g3(self):
        """delta_F_3 > 0 for all positive integer c."""
        for cv in [1, 2, 5, 10, 13, 26, 50, 100, 1000]:
            self.assertTrue(positivity_at_c(3, Fraction(cv)),
                            f"Failed at c={cv}")

    def test_positivity_at_integer_c_g4(self):
        """delta_F_4 > 0 for all positive integer c."""
        for cv in [1, 2, 5, 10, 13, 26, 50, 100, 1000]:
            self.assertTrue(positivity_at_c(4, Fraction(cv)),
                            f"Failed at c={cv}")


# ============================================================================
# (S4) Tree vanishing at genus 2
# ============================================================================

class TestTreeVanishing(unittest.TestCase):
    """Verify tree stratum vanishing (S4)."""

    def test_tree_vanishes_g2(self):
        self.assertTrue(tree_stratum_vanishes(2))

    def test_tree_nonzero_g3(self):
        self.assertFalse(tree_stratum_vanishes(3))

    def test_tree_nonzero_g4(self):
        self.assertFalse(tree_stratum_vanishes(4))

    def test_alpha_20_is_zero(self):
        self.assertEqual(betti_coefficient(2, 0), Fraction(0))

    def test_alpha_30_is_positive(self):
        self.assertGreater(betti_coefficient(3, 0), 0)

    def test_alpha_40_is_positive(self):
        self.assertGreater(betti_coefficient(4, 0), 0)


# ============================================================================
# (S5) Large-c asymptotic ratio
# ============================================================================

class TestLargeCRatio(unittest.TestCase):
    """Verify large-c asymptotic ratios (S5)."""

    def test_ratio_g2_is_zero(self):
        """R_2 = 0 (sub-linear growth at genus 2)."""
        self.assertEqual(large_c_ratio(2), Fraction(0))

    def test_ratio_g3(self):
        """R_3 = 42/31 (cross-channel exceeds scalar at large c)."""
        self.assertEqual(large_c_ratio(3), Fraction(42, 31))

    def test_ratio_g4(self):
        """R_4 = 9184/381."""
        self.assertEqual(large_c_ratio(4), Fraction(9184, 381))

    def test_ratio_g3_exceeds_1(self):
        """At genus 3, cross-channel exceeds scalar at large c."""
        self.assertGreater(large_c_ratio(3), 1)

    def test_ratio_growth(self):
        """R_4 >> R_3: the ratio grows rapidly with genus."""
        self.assertGreater(large_c_ratio(4), large_c_ratio(3) * 10)

    def test_stored_ratios_match(self):
        """Stored LARGE_C_RATIOS match computed values."""
        for g in [2, 3, 4]:
            self.assertTrue(verify_large_c_ratio(g))

    def test_large_c_numerical_check(self):
        """At c=10000, ratio approaches the asymptotic limit.

        Convergence is O(1/c), so at c=10000 the genus-3 ratio may
        still be ~8% away from the asymptote.  Use 10% tolerance.
        """
        c = Fraction(10000)
        for g in [3, 4]:
            delta = delta_Fg_closed(g, c)
            kl = Fraction(5, 6) * c * lambda_fp(g)
            actual_ratio = delta / kl
            expected = large_c_ratio(g)
            rel_err = abs(actual_ratio - expected) / expected
            self.assertLess(float(rel_err), 0.10,
                            f"g={g}: ratio {float(actual_ratio):.6f} not within "
                            f"10% of {float(expected):.6f}")


# ============================================================================
# (S6) Betti coefficient match
# ============================================================================

class TestBettiCoefficientMatch(unittest.TestCase):
    """Verify number of nonzero strata matches coefficient count (S6)."""

    def test_match_g2(self):
        d = betti_decomposition(2)
        nonzero = sum(1 for v in d.values() if v != 0)
        self.assertEqual(nonzero, len(NUMERATOR_COEFFICIENTS[2]))

    def test_match_g3(self):
        d = betti_decomposition(3)
        nonzero = sum(1 for v in d.values() if v != 0)
        self.assertEqual(nonzero, len(NUMERATOR_COEFFICIENTS[3]))

    def test_match_g4(self):
        d = betti_decomposition(4)
        nonzero = sum(1 for v in d.values() if v != 0)
        self.assertEqual(nonzero, len(NUMERATOR_COEFFICIENTS[4]))

    def test_nonzero_count_g2(self):
        self.assertEqual(nonzero_strata_count(2), 2)

    def test_nonzero_count_g3(self):
        self.assertEqual(nonzero_strata_count(3), 4)

    def test_nonzero_count_g4(self):
        self.assertEqual(nonzero_strata_count(4), 5)


# ============================================================================
# (S7) Koszul asymmetry
# ============================================================================

class TestKoszulAsymmetry(unittest.TestCase):
    """Verify Koszul asymmetry (S7)."""

    def test_koszul_conductor(self):
        """K_3 = 100."""
        self.assertEqual(W3_KOSZUL_CONDUCTOR, 100)

    def test_koszul_dual_c(self):
        self.assertEqual(koszul_dual_c(Fraction(26)), Fraction(74))

    def test_asymmetry_nonzero_g2(self):
        """delta_F_2(c) != delta_F_2(K-c) for c != 50."""
        asym = koszul_asymmetry(2, Fraction(26))
        self.assertNotEqual(asym, 0)

    def test_asymmetry_nonzero_g3(self):
        asym = koszul_asymmetry(3, Fraction(10))
        self.assertNotEqual(asym, 0)

    def test_self_dual_point(self):
        """At c=50 (self-dual), asymmetry vanishes trivially."""
        asym = koszul_asymmetry(2, Fraction(50))
        self.assertEqual(asym, 0)

    def test_koszul_sum_positive_g2(self):
        """Koszul sum is positive for all tested c."""
        for cv in [1, 10, 26, 49]:
            s = koszul_sum(2, Fraction(cv))
            self.assertGreater(s, 0, f"Failed at c={cv}")


# ============================================================================
# (S8) Propagator variance independence
# ============================================================================

class TestPropagatorVariance(unittest.TestCase):
    """Verify propagator variance independence (S8)."""

    def test_different_c_scaling(self):
        """delta_F_g and delta_mix have incompatible c-scalings.

        delta_F_g has terms c^1 through c^{1-g}; delta_mix ~ c^{-3}.
        If delta_F_g were a polynomial in delta_mix, all terms would be
        powers of c^{-3}, contradicting the c^1 term at g >= 3.
        """
        # At g=3: the c^1 term (tree) is 1/27648, nonzero.
        # delta_mix ~ c^{-3}, so any polynomial in delta_mix would have
        # c-powers that are multiples of -3. But c^1 is not a multiple of -3.
        self.assertGreater(betti_coefficient(3, 0), 0)
        # Therefore delta_F_3 is NOT a polynomial in delta_mix.

    def test_genus2_not_proportional_to_variance(self):
        """At g=2: delta_F_2 ~ 1/16 + O(1/c), delta_mix ~ 1/c^3.
        ratio diverges as c -> inf, so not proportional."""
        c1, c2 = Fraction(10), Fraction(100)
        d1 = delta_Fg_closed(2, c1)
        d2 = delta_Fg_closed(2, c2)
        # If proportional to delta_mix, ratio d1/d2 = (c2/c1)^3 = 1000
        ratio = d1 / d2
        self.assertNotEqual(ratio, Fraction(1000))


# ============================================================================
# Cross-verification with existing engines
# ============================================================================

class TestCrossVerification(unittest.TestCase):
    """Cross-verify against multi_weight_genus_tower and genus3 engines."""

    def test_g2_matches_genus_tower(self):
        from compute.lib.multi_weight_genus_tower import delta_F2_closed_form
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(2, c), delta_F2_closed_form(c),
                             f"Mismatch at c={cv}")

    def test_g3_matches_genus_tower(self):
        from compute.lib.multi_weight_genus_tower import delta_F3_closed_form
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(3, c), delta_F3_closed_form(c),
                             f"Mismatch at c={cv}")

    def test_g4_matches_genus_tower(self):
        from compute.lib.multi_weight_genus_tower import delta_F4_closed_form
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(4, c), delta_F4_closed_form(c),
                             f"Mismatch at c={cv}")

    def test_g2_matches_frontier_engine(self):
        from compute.lib.theorem_thm_d_multiweight_frontier_engine import (
            w3_genus2_cross,
        )
        for cv in [1, 5, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(2, c), w3_genus2_cross(c),
                             f"Mismatch at c={cv}")

    def test_g3_matches_frontier_engine(self):
        from compute.lib.theorem_thm_d_multiweight_frontier_engine import (
            w3_genus3_cross,
        )
        for cv in [1, 5, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(3, c), w3_genus3_cross(c),
                             f"Mismatch at c={cv}")

    def test_g4_matches_frontier_engine(self):
        from compute.lib.theorem_thm_d_multiweight_frontier_engine import (
            w3_genus4_cross,
        )
        for cv in [1, 5, 26]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(4, c), w3_genus4_cross(c),
                             f"Mismatch at c={cv}")

    def test_g3_matches_genus3_engine(self):
        from compute.lib.theorem_multi_weight_genus3_engine import (
            w3_delta_F3_closed,
        )
        for cv in [1, 10, 26, 50]:
            c = Fraction(cv)
            self.assertEqual(delta_Fg_closed(3, c), w3_delta_F3_closed(c),
                             f"Mismatch at c={cv}")


# ============================================================================
# Denominator factorization
# ============================================================================

class TestDenominatorFactorization(unittest.TestCase):
    """Verify denominator factorizations."""

    def test_D2_factorization(self):
        self.assertEqual(factorize(16), {2: 4})

    def test_D3_factorization(self):
        self.assertEqual(factorize(138240), {2: 10, 3: 3, 5: 1})

    def test_D4_factorization(self):
        self.assertEqual(factorize(17418240), {2: 11, 3: 5, 5: 1, 7: 1})

    def test_stored_factorizations(self):
        for g in [2, 3, 4]:
            self.assertTrue(verify_denominator_factorization(g))

    def test_D3_over_D2(self):
        """D_3 / D_2 = 8640."""
        self.assertEqual(DENOMINATOR_CONSTANTS[3] // DENOMINATOR_CONSTANTS[2], 8640)


# ============================================================================
# Inter-stratum ratios
# ============================================================================

class TestInterStratumRatios(unittest.TestCase):
    """Verify inter-stratum ratio structure."""

    def test_max_betti_ratio_g2(self):
        """alpha_{2,2} / alpha_{2,1} = 204."""
        self.assertEqual(max_betti_ratio(2), Fraction(204))

    def test_max_betti_ratio_g3(self):
        """alpha_{3,3} / alpha_{3,2} = 25124/133."""
        self.assertEqual(max_betti_ratio(3), Fraction(25124, 133))

    def test_max_betti_ratio_g4(self):
        """alpha_{4,4} / alpha_{4,3} = 30833046/163829."""
        self.assertEqual(max_betti_ratio(4), Fraction(30833046, 163829))

    def test_ratios_decrease_within_genus(self):
        """Inter-stratum ratios decrease as h increases within each genus."""
        for g in [3, 4]:
            ratios = []
            for h in range(g):
                r = inter_stratum_ratio(g, h)
                if r is not None:
                    ratios.append(r)
            for i in range(len(ratios) - 1):
                self.assertGreater(ratios[i], ratios[i + 1],
                                   f"g={g}: ratio at h={i} not > h={i+1}")

    def test_max_betti_growth(self):
        """Max-Betti growth: alpha_{g+1,g+1}/alpha_{g,g}."""
        self.assertEqual(MAX_BETTI_GROWTH[2], Fraction(6281, 51))
        self.assertEqual(MAX_BETTI_GROWTH[3], Fraction(5138841, 25124))


# ============================================================================
# Bernoulli and lambda_fp sanity
# ============================================================================

class TestBernoulliLambda(unittest.TestCase):
    """Verify Bernoulli and Faber-Pandharipande values."""

    def test_B2(self):
        self.assertEqual(bernoulli(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(bernoulli(4), Fraction(-1, 30))

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))


# ============================================================================
# Closed-form formula values
# ============================================================================

class TestClosedFormValues(unittest.TestCase):
    """Verify specific closed-form evaluations."""

    def test_g2_c1(self):
        self.assertEqual(delta_Fg_closed(2, Fraction(1)),
                         Fraction(205, 16))

    def test_g2_c26(self):
        """delta_F_2(26) = (26 + 204)/(16*26) = 230/416 = 115/208."""
        self.assertEqual(delta_Fg_closed(2, Fraction(26)),
                         Fraction(115, 208))

    def test_g3_c1(self):
        expected = Fraction(5 + 3792 + 1149120 + 217071360, 138240)
        self.assertEqual(delta_Fg_closed(3, Fraction(1)), expected)

    def test_g4_c1(self):
        expected = Fraction(287 + 268881 + 115455816 + 29725133760
                            + 5594347866240, 17418240)
        self.assertEqual(delta_Fg_closed(4, Fraction(1)), expected)

    def test_g2_self_dual(self):
        """delta_F_2(50) = (50 + 204)/(16*50) = 254/800 = 127/400."""
        self.assertEqual(delta_Fg_closed(2, Fraction(50)),
                         Fraction(127, 400))


# ============================================================================
# Summary and dominance
# ============================================================================

class TestSummary(unittest.TestCase):
    """Test summary and dominance analysis."""

    def test_structural_summary_g3(self):
        s = structural_summary(3)
        self.assertEqual(s['genus'], 3)
        self.assertEqual(s['numerator_degree'], 3)
        self.assertEqual(s['denominator_power'], 2)
        self.assertEqual(s['net_degree'], 1)
        self.assertTrue(s['all_positive'])

    def test_genus_tower(self):
        tower = genus_tower_summary(Fraction(26))
        self.assertIn(2, tower)
        self.assertIn(3, tower)
        self.assertIn(4, tower)
        for g in [2, 3, 4]:
            self.assertGreater(tower[g]['delta_F_g'], 0)

    def test_dominance_at_large_c(self):
        """At c=10000, cross-channel dominates at g >= 3."""
        c = Fraction(10000)
        for g in [3, 4]:
            delta = delta_Fg_closed(g, c)
            kl = Fraction(5, 6) * c * lambda_fp(g)
            self.assertGreater(delta, kl,
                               f"g={g}: cross-channel should dominate at c={c}")

    def test_betti_dominance_pattern(self):
        """Max-Betti stratum dominates at moderate c."""
        pattern = betti_dominance_pattern(3, Fraction(10))
        # h=3 (max Betti) should contribute the largest fraction
        self.assertGreater(pattern[3], pattern[0])
        self.assertGreater(pattern[3], pattern[1])
        self.assertGreater(pattern[3], pattern[2])


if __name__ == '__main__':
    unittest.main()
