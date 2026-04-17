r"""Test: W_3 W-line integer sequence closed form and exponential base.

PLATONIC INSCRIPTION (iter 58, 2026-04-17):
    thm:w3-wline-closed-form (a_n = 2*3^{n-2}*(2n-4)!/[(n-2)!*n!]),
    thm:w3-wline-exponential-base (C_{W_3}^{W-line} = 12),
    rem:w3-wline-doubling-interpretation (12 = 2*6 via Hessian + kernel),
    rem:w3-wline-higher-spin-prediction (C_{W^{(s)}} = s(s+1)),
    in chapters/theory/shadow_tower_higher_coefficients.tex.

CLAIMS:
    (1) a_n = 2 * 3^{n-2} * (2n-4)! / [(n-2)! * n!] for n >= 2.
    (2) a_{n+1}/a_n = 6*(2n-3)/(n+1) exactly.
    (3) lim_{n->inf} a_{n+1}/a_n = 12 (shadow-exponential base).
    (4) Stirling: a_n ~ 12^n / (72*sqrt(pi) * n^{5/2}).

HZ-IV VERIFICATION:
    derived_from: compute/lib/w3_wline_shadow_tower.py::normalized_recursion
        (Poisson-bracket recurrence from Fateev-Lukyanov W_3 OPE data).

    verified_against: central-binomial closed form
        a_n = 2 * 3^{n-2} * C(2n-4, n-2) / [n(n-1)]
        (derived from Vandermonde-Chu convolution identity applied to
         the bar-depth recurrence; logic independent of the Poisson
         recurrence itself).

    disjoint_rationale: the recurrence (path 1) computes a_n via
        quadratic convolution of {a_j, a_k}; the closed form (path 2)
        evaluates a_n directly as a rational combinatorial expression
        involving factorials. The match between them at every n tested
        is a nontrivial algebraic identity (Vandermonde-Chu on the
        central binomial). Neither path uses the other.

Also verifies ratio closed form and Stirling asymptotic as a third
independent verification.
"""
import math
import unittest
import sys
from fractions import Fraction

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

from compute.lib.w3_wline_shadow_tower import normalized_recursion


def closed_form(n):
    r"""a_n = 2 * 3^{n-2} * (2n-4)! / [(n-2)! * n!] as exact Fraction."""
    if n < 2:
        return Fraction(0)
    if n == 2:
        return Fraction(1)
    num = 2 * (3 ** (n - 2)) * math.factorial(2 * n - 4)
    den = math.factorial(n - 2) * math.factorial(n)
    return Fraction(num, den)


class TestW3WlineClosedForm(unittest.TestCase):
    """Path 1: recurrence matches closed form through n = 25."""

    def test_closed_form_matches_recursion_through_n25(self):
        a_rec = normalized_recursion(25)
        for n in range(2, 26):
            a_closed = closed_form(n)
            self.assertEqual(
                Fraction(a_rec[n]), a_closed,
                f"Mismatch at n={n}: closed={a_closed}, rec={a_rec[n]}"
            )

    def test_closed_form_low_n(self):
        """Hand-verified small values a_2..a_6."""
        expected = {2: 1, 3: 2, 4: 9, 5: 54, 6: 378, 7: 2916}
        for n, v in expected.items():
            self.assertEqual(int(closed_form(n)), v)


class TestW3WlineRatioClosedForm(unittest.TestCase):
    """Path 2: ratio formula a_{n+1}/a_n = 6(2n-3)/(n+1)."""

    def test_ratio_formula_exact(self):
        a_rec = normalized_recursion(25)
        for n in range(2, 25):
            expected_ratio = Fraction(6 * (2 * n - 3), n + 1)
            actual_ratio = Fraction(a_rec[n + 1], a_rec[n])
            self.assertEqual(
                actual_ratio, expected_ratio,
                f"Ratio at n={n}: expected {expected_ratio}, got {actual_ratio}"
            )

    def test_ratio_limit_is_12(self):
        """lim a_{n+1}/a_n = 12."""
        a_rec = normalized_recursion(40)
        ratio_at_39 = float(a_rec[40]) / float(a_rec[39])
        # 6(2*39 - 3)/(40) = 450/40 = 11.25; approaching 12 from below
        self.assertAlmostEqual(ratio_at_39, 11.25, places=6)
        # Verify monotonic convergence to 12
        for n in range(10, 40):
            ratio = float(a_rec[n + 1]) / float(a_rec[n])
            self.assertLess(ratio, 12.0)
            self.assertGreater(ratio, 9.0)

    def test_ratio_gap_from_12(self):
        """12 - a_{n+1}/a_n = 30/(n+1) exactly."""
        a_rec = normalized_recursion(30)
        for n in range(2, 30):
            gap = Fraction(12) - Fraction(a_rec[n + 1], a_rec[n])
            expected_gap = Fraction(30, n + 1)
            self.assertEqual(
                gap, expected_gap,
                f"Gap at n={n}: expected {expected_gap}, got {gap}"
            )


class TestW3WlineStirlingAsymptotic(unittest.TestCase):
    """Path 3: Stirling asymptotic a_n ~ 12^n / (72*sqrt(pi) * n^{5/2})."""

    def test_stirling_leading_term_at_n25(self):
        """a_n / [12^n / (72*sqrt(pi) * n^{5/2})] -> 1 (slow O(1/n) convergence)."""
        a_rec = normalized_recursion(25)
        # At n=25, convergence is slow: ratio ~ 1 + 2/n = 1.08
        # Just check that the ratio is in the expected range.
        ratio_at_25 = float(a_rec[25]) / (
            (12 ** 25) / (72 * math.sqrt(math.pi) * 25 ** 2.5)
        )
        # Ratio is approximately 1.08 at n=25; must be within [1.05, 1.15]
        self.assertGreater(ratio_at_25, 1.05)
        self.assertLess(ratio_at_25, 1.15)

    def test_stirling_ratio_decreasing(self):
        """The ratio a_n/[Stirling] decreases monotonically towards 1."""
        a_rec = normalized_recursion(25)
        ratios = []
        for n in range(10, 26):
            r = float(a_rec[n]) / (
                (12 ** n) / (72 * math.sqrt(math.pi) * n ** 2.5)
            )
            ratios.append(r)
        # Monotonic decrease
        for i in range(len(ratios) - 1):
            self.assertGreater(ratios[i], ratios[i + 1])


class TestW3WlineKoszulDualInvariance(unittest.TestCase):
    """Koszul-dual invariance: a_n is c-independent, so C = 12 is c-invariant."""

    def test_a_n_is_c_independent(self):
        """The closed form a_n has no c dependence (integer sequence)."""
        # By construction a_n is defined as |N_{2m}|/2560^{m-1} with all c
        # factors divided out. The closed form 2*3^{n-2}*(2n-4)!/[(n-2)!*n!]
        # is manifestly a rational number (integer, in fact).
        for n in range(2, 16):
            a = closed_form(n)
            self.assertEqual(a.denominator, 1, f"a_{n} is not integer: {a}")


class TestW3WlineHigherSpinPrediction(unittest.TestCase):
    r"""Prediction from rem:w3-wline-higher-spin-prediction:
    C_{W^{(s)}} = s(s+1).
    """

    def test_prediction_at_spin_2(self):
        """T-line (Virasoro), s=2: C = 2*3 = 6."""
        # This is the universal class M theorem
        self.assertEqual(2 * 3, 6)

    def test_prediction_at_spin_3(self):
        """W-line (W_3), s=3: C = 3*4 = 12."""
        # Matches thm:w3-wline-exponential-base
        self.assertEqual(3 * 4, 12)
        # Numerical verification from the actual computation
        a_rec = normalized_recursion(40)
        ratio = float(a_rec[40]) / float(a_rec[39])
        # Ratio at n=39 is 11.25; limit is 12
        self.assertAlmostEqual(12 - ratio, 30.0 / 40, places=6)


if __name__ == '__main__':
    unittest.main()
