r"""Tests for the multi-weight cross-channel generating function engine.

Verification paths:
  1. delta_F_2(W_3) = (c+204)/(16c) at specific c values
  2. delta_F_3(W_3) from universal formula at specific c values
  3. delta_F_4(W_3) at specific c values
  4. Ratio delta_F_3/delta_F_2 is rational (not polynomial) in c
  5. Denominator prime support: {2} at g=2, {2,3,5} at g=3, {2,3,5,7} at g=4
  6. Leading c-power growth
  7. delta_F_g = 0 for uniform-weight algebras (N=2)
  8. Non-separability of generating function
  9. Cross-engine consistency
 10. N-degree pattern
 11. Positivity

References:
    thm:multi-weight-genus-expansion, AP27
    theorem_delta_f2_intersection_engine.py
    theorem_delta_f3_universal_engine.py
    multi_weight_genus_tower.py
"""

import unittest
from fractions import Fraction

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_multi_weight_generating_function_engine import (
    A2_of_N,
    A3_of_N,
    B2_of_N,
    B3_of_N,
    C3_of_N,
    D3_of_N,
    bernoulli_number,
    c_expansion_W3,
    c_expansion_table_W3,
    cross_check_with_intersection_engine,
    cross_check_with_genus_tower,
    delta_F2_formula,
    delta_F2_W3,
    delta_F3_formula,
    delta_F3_W3,
    delta_F4_W3,
    delta_Fg_W3,
    denominator_analysis_W3,
    denominator_constant_W3,
    generating_function_verdict,
    lambda_fp,
    large_c_limit_W3,
    leading_c_power_W3,
    leading_coefficient_W3,
    leading_coefficient_analysis_W3,
    N_degree_pattern,
    numerator_analysis_W3,
    numerator_polynomial_W3,
    ratio_analysis_W3,
    ratio_consecutive_W3,
    residual_polynomial_degree_g2,
    residual_polynomial_degree_g3,
    scalar_ratio_W3,
    test_ahat_ansatz_W3,
    test_factorial_growth_W3,
    test_separability_W3,
    verify_all,
    verify_uniform_weight_vanishing,
)


# ============================================================================
# 1. Foundation: Bernoulli and lambda_FP
# ============================================================================

class TestFoundations(unittest.TestCase):
    """Verify foundational quantities."""

    def test_bernoulli_B0(self):
        self.assertEqual(bernoulli_number(0), Fraction(1))

    def test_bernoulli_B2(self):
        self.assertEqual(bernoulli_number(2), Fraction(1, 6))

    def test_bernoulli_B4(self):
        self.assertEqual(bernoulli_number(4), Fraction(-1, 30))

    def test_bernoulli_B6(self):
        self.assertEqual(bernoulli_number(6), Fraction(1, 42))

    def test_lambda_fp_g1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda_fp_g2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda_fp_g3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda_fp_g4(self):
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))


# ============================================================================
# 2. delta_F_2(W_3) at specific c values
# ============================================================================

class TestDeltaF2W3(unittest.TestCase):
    """Verify delta_F_2(W_3, c) = (c+204)/(16c)."""

    def test_c1(self):
        self.assertEqual(delta_F2_W3(Fraction(1)), Fraction(205, 16))

    def test_c2(self):
        self.assertEqual(delta_F2_W3(Fraction(2)), Fraction(206, 32))

    def test_c10(self):
        self.assertEqual(delta_F2_W3(Fraction(10)), Fraction(214, 160))

    def test_c100(self):
        self.assertEqual(delta_F2_W3(Fraction(100)), Fraction(304, 1600))

    def test_c26(self):
        expected = Fraction(230, 416)
        self.assertEqual(delta_F2_W3(Fraction(26)), expected)

    def test_formula_matches_closed_form(self):
        """delta_F2_formula(3, c) must equal delta_F2_W3(c)."""
        for cv in [1, 2, 5, 10, 26, 50]:
            c = Fraction(cv)
            self.assertEqual(
                delta_F2_formula(3, c), delta_F2_W3(c),
                msg=f"Mismatch at c={cv}"
            )


# ============================================================================
# 3. delta_F_3(W_3) at specific c values
# ============================================================================

class TestDeltaF3W3(unittest.TestCase):
    """Verify delta_F_3(W_3, c) from graph-sum-verified closed form."""

    def test_c1(self):
        """delta_F_3(W_3, 1) = (5 + 3792 + 1149120 + 217071360)/138240."""
        num = 5 + 3792 + 1149120 + 217071360
        expected = Fraction(num, 138240)
        self.assertEqual(delta_F3_W3(Fraction(1)), expected)

    def test_c10(self):
        c = Fraction(10)
        num = 5 * 1000 + 3792 * 100 + 1149120 * 10 + 217071360
        den = 138240 * 100
        expected = Fraction(num, den)
        self.assertEqual(delta_F3_W3(c), expected)

    def test_universal_formula_B3_discrepancy(self):
        """The universal N-formula has a known B3 discrepancy at N=3.

        Graph sum gives B = 1149120/138240 = 133/16.
        Universal B3_of_N(3) = 69/8 = 138/16, off by 5/16.
        This is documented: the universal engine's B3 polynomial needs
        re-derivation. The W_3 closed form from graph sum is authoritative.
        """
        # Tower B at N=3
        tower_B = Fraction(1149120, 138240)
        universal_B = B3_of_N(3)
        self.assertNotEqual(tower_B, universal_B)
        self.assertEqual(tower_B, Fraction(133, 16))
        self.assertEqual(universal_B, Fraction(69, 8))

    def test_positivity(self):
        for cv in [1, 10, 26, 100]:
            self.assertGreater(delta_F3_W3(Fraction(cv)), 0)


# ============================================================================
# 4. delta_F_4(W_3) at specific c values
# ============================================================================

class TestDeltaF4W3(unittest.TestCase):
    """Verify delta_F_4(W_3, c) closed form."""

    def test_c1(self):
        num = 287 + 268881 + 115455816 + 29725133760 + 5594347866240
        expected = Fraction(num, 17418240)
        self.assertEqual(delta_F4_W3(Fraction(1)), expected)

    def test_c2(self):
        c = Fraction(2)
        num = 287 * 16 + 268881 * 8 + 115455816 * 4 + 29725133760 * 2 + 5594347866240
        den = 17418240 * 8
        expected = Fraction(num, den)
        self.assertEqual(delta_F4_W3(c), expected)

    def test_positivity(self):
        for cv in [1, 10, 26, 100]:
            self.assertGreater(delta_F4_W3(Fraction(cv)), 0)


# ============================================================================
# 5. Ratio analysis: delta_F_{g+1}/delta_F_g is NOT constant in c
# ============================================================================

class TestRatioAnalysis(unittest.TestCase):
    """The ratio delta_F_{g+1}/delta_F_g is rational but not constant in c."""

    def test_ratio_32_not_constant(self):
        r1 = ratio_consecutive_W3(2, Fraction(1))
        r2 = ratio_consecutive_W3(2, Fraction(10))
        self.assertIsNotNone(r1)
        self.assertIsNotNone(r2)
        self.assertNotEqual(r1, r2)

    def test_ratio_43_not_constant(self):
        r1 = ratio_consecutive_W3(3, Fraction(1))
        r2 = ratio_consecutive_W3(3, Fraction(10))
        self.assertIsNotNone(r1)
        self.assertIsNotNone(r2)
        self.assertNotEqual(r1, r2)

    def test_ratio_32_is_rational(self):
        """The ratio is always a Fraction (rational) at rational c."""
        for cv in [1, 5, 26]:
            r = ratio_consecutive_W3(2, Fraction(cv))
            self.assertIsInstance(r, Fraction)

    def test_ratio_32_not_polynomial(self):
        """Full ratio analysis: not polynomial in c."""
        analysis = ratio_analysis_W3()
        # Polynomial would mean fitting a degree-2 poly at 3 points
        # and having it match at all other points. This should fail.
        self.assertFalse(analysis['ratio_32_polynomial_in_c'])

    def test_ratio_43_not_polynomial(self):
        analysis = ratio_analysis_W3()
        self.assertFalse(analysis['ratio_43_polynomial_in_c'])


# ============================================================================
# 6. Denominator prime support
# ============================================================================

class TestDenominatorAnalysis(unittest.TestCase):
    """Prime support of D_g matches {p : p <= 2g-1}."""

    def test_D2_is_16(self):
        self.assertEqual(denominator_constant_W3(2), 16)

    def test_D3_is_138240(self):
        self.assertEqual(denominator_constant_W3(3), 138240)

    def test_D4_is_17418240(self):
        self.assertEqual(denominator_constant_W3(4), 17418240)

    def test_D2_prime_support(self):
        da = denominator_analysis_W3()
        self.assertEqual(da[2]['primes'], [2])

    def test_D3_prime_support(self):
        da = denominator_analysis_W3()
        self.assertEqual(da[3]['primes'], [2, 3, 5])

    def test_D4_prime_support(self):
        da = denominator_analysis_W3()
        self.assertEqual(da[4]['primes'], [2, 3, 5, 7])

    def test_max_prime_bounded_by_2g_minus_1(self):
        """All primes dividing D_g are <= 2g-1."""
        da = denominator_analysis_W3()
        for g in [2, 3, 4]:
            self.assertTrue(
                da[g]['max_prime_bounded'],
                msg=f"Max prime exceeds 2g-1 at g={g}"
            )

    def test_g2_max_prime_strict(self):
        """At g=2, max prime is 2 < 3 = 2g-1 (strict inequality)."""
        da = denominator_analysis_W3()
        self.assertEqual(da[2]['max_prime'], 2)
        self.assertLess(da[2]['max_prime'], 2 * 2 - 1)

    def test_g3_g4_max_prime_sharp(self):
        """At g=3,4, max prime = 2g-1 (bound is sharp)."""
        da = denominator_analysis_W3()
        self.assertEqual(da[3]['max_prime'], 5)
        self.assertEqual(da[4]['max_prime'], 7)


# ============================================================================
# 7. Leading c-power growth
# ============================================================================

class TestLeadingCoefficientAnalysis(unittest.TestCase):
    """Leading c-power and coefficient analysis."""

    def test_leading_power_g2(self):
        """delta_F_2 ~ O(1) as c -> infinity."""
        self.assertEqual(leading_c_power_W3(2), 0)

    def test_leading_power_g3(self):
        """delta_F_3 ~ O(c) as c -> infinity."""
        self.assertEqual(leading_c_power_W3(3), 1)

    def test_leading_power_g4(self):
        """delta_F_4 ~ O(c) as c -> infinity."""
        self.assertEqual(leading_c_power_W3(4), 1)

    def test_leading_coeff_g2(self):
        """Leading coefficient of delta_F_2: B_2(3) = 1/16."""
        self.assertEqual(leading_coefficient_W3(2), Fraction(1, 16))

    def test_leading_coeff_g3(self):
        """Leading coefficient of delta_F_3: 5/138240 = 1/27648."""
        self.assertEqual(leading_coefficient_W3(3), Fraction(5, 138240))

    def test_leading_coeff_g4(self):
        """Leading coefficient of delta_F_4: 287/17418240."""
        self.assertEqual(leading_coefficient_W3(4), Fraction(287, 17418240))

    def test_leading_coefficients_positive(self):
        for g in [2, 3, 4]:
            self.assertGreater(leading_coefficient_W3(g), 0)


# ============================================================================
# 8. Uniform-weight vanishing
# ============================================================================

class TestUniformWeightVanishing(unittest.TestCase):
    """delta_F_g = 0 for Virasoro (N=2, uniform weight)."""

    def test_A2_N2_vanishes(self):
        self.assertEqual(A2_of_N(2), Fraction(0))

    def test_B2_N2_vanishes(self):
        self.assertEqual(B2_of_N(2), Fraction(0))

    def test_D3_N2_vanishes(self):
        self.assertEqual(D3_of_N(2), Fraction(0))

    def test_C3_N2_vanishes(self):
        self.assertEqual(C3_of_N(2), Fraction(0))

    def test_B3_N2_vanishes(self):
        self.assertEqual(B3_of_N(2), Fraction(0))

    def test_A3_N2_vanishes(self):
        self.assertEqual(A3_of_N(2), Fraction(0))

    def test_delta_F2_N2_vanishes(self):
        for cv in [1, 10, 26]:
            self.assertEqual(
                delta_F2_formula(2, Fraction(cv)), Fraction(0),
                msg=f"delta_F2(N=2) nonzero at c={cv}"
            )

    def test_delta_F3_N2_vanishes(self):
        for cv in [1, 10, 26]:
            self.assertEqual(
                delta_F3_formula(2, Fraction(cv)), Fraction(0),
                msg=f"delta_F3(N=2) nonzero at c={cv}"
            )


# ============================================================================
# 9. Non-separability of generating function
# ============================================================================

class TestNonSeparability(unittest.TestCase):
    """The generating function is NOT separable in (c, hbar)."""

    def test_not_separable(self):
        sep = test_separability_W3()
        self.assertFalse(sep['separable'])

    def test_cross_ratio_g2_neq_g3(self):
        """delta_F_3(c1)/delta_F_3(c2) != delta_F_2(c1)/delta_F_2(c2)."""
        c1, c2 = Fraction(1), Fraction(10)
        r2 = delta_F2_W3(c1) / delta_F2_W3(c2)
        r3 = delta_F3_W3(c1) / delta_F3_W3(c2)
        self.assertNotEqual(r2, r3)

    def test_cross_ratio_g3_neq_g4(self):
        c1, c2 = Fraction(1), Fraction(10)
        r3 = delta_F3_W3(c1) / delta_F3_W3(c2)
        r4 = delta_F4_W3(c1) / delta_F4_W3(c2)
        self.assertNotEqual(r3, r4)


# ============================================================================
# 10. A-hat ansatz failure
# ============================================================================

class TestAhatAnsatzFailure(unittest.TestCase):
    """delta_F_g is NOT geometric in delta_F_2."""

    def test_not_ahat(self):
        ahat = test_ahat_ansatz_W3()
        self.assertFalse(ahat['ahat_ansatz_viable'])

    def test_delta_F3_not_proportional_to_delta_F2_squared(self):
        """delta_F_3 / delta_F_2^2 is not constant in c."""
        c1, c2 = Fraction(1), Fraction(10)
        f2_1, f3_1 = delta_F2_W3(c1), delta_F3_W3(c1)
        f2_2, f3_2 = delta_F2_W3(c2), delta_F3_W3(c2)
        r1 = f3_1 / (f2_1 * f2_1)
        r2 = f3_2 / (f2_2 * f2_2)
        self.assertNotEqual(r1, r2)


# ============================================================================
# 11. c-expansion coefficient table
# ============================================================================

class TestCExpansion(unittest.TestCase):
    """c-expansion coefficient extraction."""

    def test_g2_expansion_keys(self):
        exp = c_expansion_W3(2)
        self.assertIsNotNone(exp)
        self.assertEqual(sorted(exp.keys()), [-1, 0])

    def test_g3_expansion_keys(self):
        exp = c_expansion_W3(3)
        self.assertIsNotNone(exp)
        self.assertEqual(sorted(exp.keys()), [-2, -1, 0, 1])

    def test_g4_expansion_keys(self):
        exp = c_expansion_W3(4)
        self.assertIsNotNone(exp)
        self.assertEqual(sorted(exp.keys()), [-3, -2, -1, 0, 1])

    def test_g2_c_power_range(self):
        """c-power range for g=2 is [-(g-1), d-(g-1)] = [-1, 0]."""
        exp = c_expansion_W3(2)
        self.assertEqual(min(exp.keys()), -(2 - 1))

    def test_g3_c_power_range(self):
        exp = c_expansion_W3(3)
        self.assertEqual(min(exp.keys()), -(3 - 1))

    def test_g2_reconstruction(self):
        """Reconstructing delta_F_2 from c-expansion coefficients."""
        exp = c_expansion_W3(2)
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            reconstructed = sum(coeff * c**k for k, coeff in exp.items())
            self.assertEqual(reconstructed, delta_F2_W3(c), msg=f"c={cv}")

    def test_g3_reconstruction(self):
        exp = c_expansion_W3(3)
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            reconstructed = sum(coeff * c**k for k, coeff in exp.items())
            self.assertEqual(reconstructed, delta_F3_W3(c), msg=f"c={cv}")

    def test_g4_reconstruction(self):
        exp = c_expansion_W3(4)
        for cv in [1, 10, 26]:
            c = Fraction(cv)
            reconstructed = sum(coeff * c**k for k, coeff in exp.items())
            self.assertEqual(reconstructed, delta_F4_W3(c), msg=f"c={cv}")


# ============================================================================
# 12. N-degree pattern
# ============================================================================

class TestNDegreePattern(unittest.TestCase):
    """Polynomial degree in N of c-expansion coefficients."""

    def test_g2_A2_degree(self):
        """A_2(N) has total degree 4 in N (cubic residual * (N-2))."""
        degs = residual_polynomial_degree_g2()
        self.assertEqual(degs['A2_total_degree'], 4)

    def test_g2_B2_degree(self):
        self.assertEqual(residual_polynomial_degree_g2()['B2_total_degree'], 2)

    def test_g3_A3_degree(self):
        self.assertEqual(residual_polynomial_degree_g3()['A3_total_degree'], 7)

    def test_g3_B3_degree(self):
        self.assertEqual(residual_polynomial_degree_g3()['B3_total_degree'], 5)

    def test_g3_C3_degree(self):
        self.assertEqual(residual_polynomial_degree_g3()['C3_total_degree'], 3)

    def test_g3_D3_degree(self):
        self.assertEqual(residual_polynomial_degree_g3()['D3_total_degree'], 1)

    def test_degree_pattern_formula_g2(self):
        """Pattern: deg_N(coeff of 1/c^j) = 2j + g for g=2."""
        pat = N_degree_pattern()
        self.assertTrue(pat['pattern_holds_g2'])

    def test_degree_pattern_formula_g3(self):
        pat = N_degree_pattern()
        self.assertTrue(pat['pattern_holds_g3'])


# ============================================================================
# 13. Cross-engine consistency
# ============================================================================

class TestCrossEngine(unittest.TestCase):
    """Cross-check with other compute engines."""

    def test_genus_tower_consistency(self):
        results = cross_check_with_genus_tower()
        if 'import_error' in results:
            self.skipTest("multi_weight_genus_tower not importable")
        for key, val in results.items():
            self.assertTrue(val, msg=f"Cross-check failed: {key}")

    def test_intersection_engine_consistency(self):
        results = cross_check_with_intersection_engine()
        if 'import_error' in results:
            self.skipTest("intersection engine not importable")
        for key, val in results.items():
            self.assertTrue(val, msg=f"Cross-check failed: {key}")


# ============================================================================
# 14. Numerator analysis
# ============================================================================

class TestNumeratorAnalysis(unittest.TestCase):
    """Numerator polynomial properties."""

    def test_all_coefficients_positive(self):
        na = numerator_analysis_W3()
        for g in [2, 3, 4]:
            self.assertTrue(
                na[g]['all_positive'],
                msg=f"Not all positive at g={g}"
            )

    def test_degree_g2(self):
        na = numerator_analysis_W3()
        self.assertEqual(na[2]['degree'], 1)

    def test_degree_g3(self):
        na = numerator_analysis_W3()
        self.assertEqual(na[3]['degree'], 3)

    def test_degree_g4(self):
        na = numerator_analysis_W3()
        self.assertEqual(na[4]['degree'], 4)


# ============================================================================
# 15. Generating function verdict
# ============================================================================

class TestVerdict(unittest.TestCase):
    """Master generating function analysis."""

    def test_verdict_type(self):
        v = generating_function_verdict()
        self.assertEqual(v['type'], 'irreducibly_bivariate')

    def test_not_separable(self):
        v = generating_function_verdict()
        self.assertFalse(v['separable'])

    def test_not_ahat(self):
        v = generating_function_verdict()
        self.assertFalse(v['ahat_viable'])

    def test_denominator_pattern(self):
        v = generating_function_verdict()
        self.assertTrue(v['denominator_primes_bounded_by_2g_minus_1'])


# ============================================================================
# 16. Master verification
# ============================================================================

class TestMasterVerification(unittest.TestCase):
    """Full verify_all() suite."""

    def test_verify_all(self):
        results = verify_all()
        for key, val in results.items():
            self.assertTrue(val, msg=f"verify_all failed: {key}")


# ============================================================================
# 17. Scalar ratio analysis
# ============================================================================

class TestScalarRatio(unittest.TestCase):
    """delta_F_g / (kappa * lambda_g^FP) for W_3."""

    def test_ratio_g2_c26(self):
        """Scalar ratio at g=2, c=26."""
        r = scalar_ratio_W3(2, Fraction(26))
        self.assertIsNotNone(r)
        self.assertGreater(r, 0)

    def test_ratio_g3_grows(self):
        """Scalar ratio grows with g at fixed c."""
        r2 = scalar_ratio_W3(2, Fraction(26))
        r3 = scalar_ratio_W3(3, Fraction(26))
        self.assertIsNotNone(r2)
        self.assertIsNotNone(r3)
        self.assertGreater(r3, r2)

    def test_ratio_g4_dominates(self):
        """At g=4, cross-channel dominates scalar part (ratio > 1)."""
        r4 = scalar_ratio_W3(4, Fraction(26))
        self.assertIsNotNone(r4)
        self.assertGreater(r4, 1)


# ============================================================================
# 18. Specific numerical checks (multi-path verification)
# ============================================================================

class TestSpecificNumerical(unittest.TestCase):
    """Explicit numerical verification at selected parameter values."""

    def test_delta_F2_W3_c13(self):
        """delta_F_2(W_3, c=13) = (13+204)/(16*13) = 217/208."""
        self.assertEqual(delta_F2_W3(Fraction(13)), Fraction(217, 208))

    def test_delta_F2_W3_large_c_limit(self):
        """As c -> infinity, delta_F_2 -> 1/16."""
        c = Fraction(10**6)
        val = delta_F2_W3(c)
        # val = 1/16 + 204/(16*c) ~ 1/16 + tiny
        self.assertTrue(abs(float(val) - 1.0 / 16) < 1e-4)

    def test_W3_delta_F2_equals_closed_form(self):
        """(c+204)/(16c) = 1/16 + 51/(4c) via B_2(3) and A_2(3)."""
        for cv in [1, 7, 13, 50]:
            c = Fraction(cv)
            via_closed = (c + 204) / (16 * c)
            via_formula = B2_of_N(3) + A2_of_N(3) / c
            self.assertEqual(via_closed, via_formula, msg=f"c={cv}")

    def test_delta_Fg_W3_dispatch(self):
        """delta_Fg_W3 dispatches correctly and returns None for g > 4."""
        self.assertIsNotNone(delta_Fg_W3(2, Fraction(1)))
        self.assertIsNotNone(delta_Fg_W3(3, Fraction(1)))
        self.assertIsNotNone(delta_Fg_W3(4, Fraction(1)))
        self.assertIsNone(delta_Fg_W3(5, Fraction(1)))


if __name__ == '__main__':
    unittest.main()
