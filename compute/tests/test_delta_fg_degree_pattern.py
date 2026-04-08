r"""Tests for the delta_F_g degree pattern prediction engine.

30+ tests verifying:
  1. Known closed-form formulas (3 paths per genus)
  2. Degree pattern analysis
  3. Genus-5 prediction
  4. Coefficient growth analysis
  5. Denominator pattern
  6. Large-c asymptotic ratios
  7. Cross-checks with multi_weight_genus_tower.py

References:
    delta_fg_degree_pattern_engine.py
    multi_weight_genus_tower.py
    thm:multi-weight-genus-expansion
"""

import pytest
import unittest
from fractions import Fraction

from compute.lib.delta_fg_degree_pattern_engine import (
    KNOWN_NUMERATOR_COEFFS,
    KNOWN_DENOMINATORS,
    delta_fg_closed_form,
    degree_pattern,
    predict_genus5,
    coefficient_growth_analysis,
    denominator_pattern,
    large_c_ratios,
    verify_predictions_against_known,
    prediction_table,
    _prime_factorization,
)


# =========================================================================
# 1. Known formulas (3 paths each)
# =========================================================================

class TestKnownFormulas(unittest.TestCase):
    """Verify known closed-form formulas for delta_F_g."""

    def test_genus2_at_c1(self):
        """Path 1: delta_F_2(c=1) = (1+204)/16 = 205/16."""
        result = delta_fg_closed_form(2, Fraction(1))
        self.assertEqual(result, Fraction(205, 16))

    def test_genus2_at_c2(self):
        """Path 2: delta_F_2(c=2) = (2+204)/32 = 206/32 = 103/16."""
        result = delta_fg_closed_form(2, Fraction(2))
        self.assertEqual(result, Fraction(206, 32))

    def test_genus2_at_c100(self):
        """Path 3: delta_F_2(c=100) = (100+204)/1600 = 304/1600 = 19/100."""
        result = delta_fg_closed_form(2, Fraction(100))
        self.assertEqual(result, Fraction(304, 1600))

    def test_genus3_at_c1(self):
        """delta_F_3(c=1): verify numerator and denominator."""
        result = delta_fg_closed_form(3, Fraction(1))
        expected_num = 5 + 3792 + 1149120 + 217071360
        expected = Fraction(expected_num, 138240)
        self.assertEqual(result, expected)

    def test_genus4_at_c1(self):
        """delta_F_4(c=1)."""
        result = delta_fg_closed_form(4, Fraction(1))
        coeffs = KNOWN_NUMERATOR_COEFFS[4]
        expected_num = sum(coeffs)
        expected = Fraction(expected_num, KNOWN_DENOMINATORS[4])
        self.assertEqual(result, expected)

    def test_genus2_positive_for_positive_c(self):
        """delta_F_2 > 0 for all c > 0."""
        for c in [Fraction(1, 10), Fraction(1), Fraction(10), Fraction(100)]:
            result = delta_fg_closed_form(2, c)
            self.assertGreater(result, 0,
                               f"delta_F_2 not positive at c={c}")

    def test_genus3_positive_for_positive_c(self):
        """delta_F_3 > 0 for all c > 0."""
        for c in [Fraction(1), Fraction(10), Fraction(100)]:
            result = delta_fg_closed_form(3, c)
            self.assertGreater(result, 0)

    def test_genus4_positive_for_positive_c(self):
        """delta_F_4 > 0 for all c > 0."""
        for c in [Fraction(1), Fraction(10), Fraction(100)]:
            result = delta_fg_closed_form(4, c)
            self.assertGreater(result, 0)

    def test_genus5_returns_none(self):
        """delta_F_5 not known yet."""
        self.assertIsNone(delta_fg_closed_form(5, Fraction(1)))


# =========================================================================
# 2. Degree pattern analysis
# =========================================================================

class TestDegreePattern(unittest.TestCase):
    """Degree pattern: d_g, e_g, n_g."""

    def test_genus2_degree(self):
        """d_2 = 1."""
        pattern = degree_pattern()
        self.assertEqual(pattern[2]['deg_numerator'], 1)

    def test_genus3_degree(self):
        """d_3 = 3."""
        pattern = degree_pattern()
        self.assertEqual(pattern[3]['deg_numerator'], 3)

    def test_genus4_degree(self):
        """d_4 = 4."""
        pattern = degree_pattern()
        self.assertEqual(pattern[4]['deg_numerator'], 4)

    def test_genus2_net_degree(self):
        """e_2 = 0 (constant at large c)."""
        pattern = degree_pattern()
        self.assertEqual(pattern[2]['net_degree'], 0)

    def test_genus3_net_degree(self):
        """e_3 = 1 (linear at large c)."""
        pattern = degree_pattern()
        self.assertEqual(pattern[3]['net_degree'], 1)

    def test_genus4_net_degree(self):
        """e_4 = 1 (linear at large c)."""
        pattern = degree_pattern()
        self.assertEqual(pattern[4]['net_degree'], 1)

    def test_genus2_n_terms(self):
        """n_2 = 2."""
        pattern = degree_pattern()
        self.assertEqual(pattern[2]['n_terms'], 2)

    def test_genus3_n_terms(self):
        """n_3 = 4."""
        pattern = degree_pattern()
        self.assertEqual(pattern[3]['n_terms'], 4)

    def test_genus4_n_terms(self):
        """n_4 = 5."""
        pattern = degree_pattern()
        self.assertEqual(pattern[4]['n_terms'], 5)


# =========================================================================
# 3. Pattern rules verification
# =========================================================================

class TestPatternRules(unittest.TestCase):
    """Verify the pattern rules against known data."""

    def test_all_rules_match(self):
        """All pattern rules match known data."""
        result = verify_predictions_against_known()
        self.assertTrue(result['all_match'],
                        f"Pattern mismatch: {result['per_genus']}")

    def test_degree_rule_d_g_equals_g(self):
        """d_g = g for g >= 3."""
        for g in [3, 4]:
            pattern = degree_pattern()
            self.assertEqual(pattern[g]['deg_numerator'], g)

    def test_net_degree_rule(self):
        """e_g = 1 for g >= 3."""
        for g in [3, 4]:
            pattern = degree_pattern()
            self.assertEqual(pattern[g]['net_degree'], 1)


# =========================================================================
# 4. Genus-5 prediction
# =========================================================================

class TestGenus5Prediction(unittest.TestCase):
    """Prediction for delta_F_5 structure."""

    def test_predicted_degree(self):
        """Predicted d_5 = 5."""
        pred = predict_genus5()
        self.assertEqual(pred['predicted_numerator_degree'], 5)

    def test_predicted_n_terms(self):
        """Predicted n_5 = 6."""
        pred = predict_genus5()
        self.assertEqual(pred['predicted_n_terms'], 6)

    def test_predicted_net_degree(self):
        """Predicted e_5 = 1 (linear in c)."""
        pred = predict_genus5()
        self.assertEqual(pred['predicted_net_degree'], 1)

    def test_predicted_denom_pole(self):
        """Predicted denominator pole = 4 = g-1."""
        pred = predict_genus5()
        self.assertEqual(pred['predicted_denom_pole'], 4)

    def test_high_confidence(self):
        """Prediction has high confidence."""
        pred = predict_genus5()
        self.assertIn('HIGH', pred['confidence'].upper())


# =========================================================================
# 5. Denominator pattern
# =========================================================================

class TestDenominatorPattern(unittest.TestCase):
    """Denominator factorization pattern."""

    def test_d2_factorization(self):
        """D_2 = 16 = 2^4."""
        result = denominator_pattern()
        self.assertEqual(result[2]['factorization'], {2: 4})

    def test_d3_factorization(self):
        """D_3 = 138240 = 2^10 * 3^3 * 5."""
        result = denominator_pattern()
        self.assertEqual(result[3]['factorization'], {2: 10, 3: 3, 5: 1})

    def test_d4_factorization(self):
        """D_4 = 17418240 = 2^11 * 3^5 * 5 * 7."""
        result = denominator_pattern()
        self.assertEqual(result[4]['factorization'], {2: 11, 3: 5, 5: 1, 7: 1})

    def test_max_prime_is_2g_minus_1(self):
        """Max prime in D_g equals 2g-1 for g=3,4."""
        result = denominator_pattern()
        for g in [3, 4]:
            self.assertTrue(result[g]['max_prime_is_2g_minus_1'],
                            f"Max prime of D_{g} is not 2*{g}-1")


# =========================================================================
# 6. Coefficient growth
# =========================================================================

class TestCoefficientGrowth(unittest.TestCase):
    """Growth of coefficients in the numerator polynomial."""

    def test_all_positive_coefficients(self):
        """All coefficients of P_g are positive."""
        for g in [2, 3, 4]:
            coeffs = KNOWN_NUMERATOR_COEFFS[g]
            for i, c in enumerate(coeffs):
                self.assertGreater(c, 0,
                                   f"g={g}: coefficient {i} = {c} not positive")

    def test_coefficient_growth_supralinear(self):
        """Successive ratios grow (at least for g=3,4)."""
        analysis = coefficient_growth_analysis()
        for g in [3, 4]:
            ratios = analysis[g]['successive_ratios']
            self.assertGreater(len(ratios), 1)
            # All ratios are > 1 (coefficients are increasing)
            for r in ratios:
                self.assertGreater(r, 1,
                                   f"g={g}: ratio {r} not > 1")


# =========================================================================
# 7. Cross-check with multi_weight_genus_tower
# =========================================================================

class TestCrossCheckWithTower(unittest.TestCase):
    """Cross-check with the multi_weight_genus_tower engine."""

    def test_genus2_matches_tower(self):
        """delta_F_2 matches the graph-sum computation."""
        try:
            from compute.lib.multi_weight_genus_tower import delta_F2_closed_form
            for c in [Fraction(1), Fraction(2), Fraction(10)]:
                ours = delta_fg_closed_form(2, c)
                tower = delta_F2_closed_form(c)
                self.assertEqual(ours, tower,
                                 f"delta_F_2 mismatch at c={c}")
        except ImportError:
            self.skipTest("multi_weight_genus_tower not available")

    def test_genus3_matches_tower(self):
        """delta_F_3 matches the graph-sum computation."""
        try:
            from compute.lib.multi_weight_genus_tower import delta_F3_closed_form
            for c in [Fraction(1), Fraction(2), Fraction(10)]:
                ours = delta_fg_closed_form(3, c)
                tower = delta_F3_closed_form(c)
                self.assertEqual(ours, tower,
                                 f"delta_F_3 mismatch at c={c}")
        except ImportError:
            self.skipTest("multi_weight_genus_tower not available")

    def test_genus4_matches_tower(self):
        """delta_F_4 matches the graph-sum computation."""
        try:
            from compute.lib.multi_weight_genus_tower import delta_F4_closed_form
            for c in [Fraction(1), Fraction(2), Fraction(10)]:
                ours = delta_fg_closed_form(4, c)
                tower = delta_F4_closed_form(c)
                self.assertEqual(ours, tower,
                                 f"delta_F_4 mismatch at c={c}")
        except ImportError:
            self.skipTest("multi_weight_genus_tower not available")


# =========================================================================
# 8. Prediction table
# =========================================================================

class TestPredictionTable(unittest.TestCase):
    """Summary prediction table for g=2..7."""

    def test_table_has_known_genera(self):
        """Table contains g=2,3,4."""
        table = prediction_table()
        for g in [2, 3, 4]:
            self.assertIn(g, table)

    def test_table_has_predictions(self):
        """Table contains predictions for g=5,6,7."""
        table = prediction_table()
        for g in [5, 6, 7]:
            self.assertIn(g, table)
            self.assertEqual(table[g]['status'], 'PREDICTED')

    def test_known_are_proved(self):
        """Known genera are marked PROVED."""
        table = prediction_table()
        for g in [2, 3, 4]:
            self.assertEqual(table[g]['status'], 'PROVED')

    def test_predicted_degrees_follow_pattern(self):
        """Predicted degrees follow d_g = g for g >= 3."""
        table = prediction_table()
        for g in [5, 6, 7]:
            self.assertEqual(table[g]['deg_numerator'], g)

    def test_predicted_net_degree_is_1(self):
        """Predicted net degree is 1 for g >= 3."""
        table = prediction_table()
        for g in [5, 6, 7]:
            self.assertEqual(table[g]['net_degree'], 1)


# =========================================================================
# 9. Prime factorization utility
# =========================================================================

class TestPrimeFactorization(unittest.TestCase):
    """Prime factorization utility tests."""

    def test_small_primes(self):
        self.assertEqual(_prime_factorization(2), {2: 1})
        self.assertEqual(_prime_factorization(3), {3: 1})
        self.assertEqual(_prime_factorization(4), {2: 2})

    def test_d2(self):
        self.assertEqual(_prime_factorization(16), {2: 4})

    def test_d3(self):
        self.assertEqual(_prime_factorization(138240), {2: 10, 3: 3, 5: 1})

    def test_d4(self):
        self.assertEqual(_prime_factorization(17418240), {2: 11, 3: 5, 5: 1, 7: 1})


# =========================================================================
# 10. Large-c ratios
# =========================================================================

class TestLargeCRatios(unittest.TestCase):
    """Large-c asymptotic ratio delta_F_g / (kappa * lambda_g)."""

    def test_genus2_ratio_zero(self):
        """g=2: ratio -> 0 at large c (constant / linear)."""
        try:
            ratios = large_c_ratios()
            self.assertEqual(ratios[2]['ratio_at_large_c'], 0)
        except ImportError:
            self.skipTest("multi_weight_genus_tower not available")

    def test_genus3_ratio_finite(self):
        """g=3: ratio is finite nonzero at large c."""
        try:
            ratios = large_c_ratios()
            r3 = ratios[3]['ratio_at_large_c']
            self.assertIsNotNone(r3)
            self.assertGreater(r3, 0)
        except ImportError:
            self.skipTest("multi_weight_genus_tower not available")


if __name__ == '__main__':
    unittest.main()
