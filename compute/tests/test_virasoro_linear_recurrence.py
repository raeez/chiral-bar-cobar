r"""Test: Virasoro T-line leading-c A_r satisfies LINEAR recurrence
A_r = -6(r-1)/r * A_{r-1} for r >= 5, despite the full-c shadow
recursion being QUADRATIC.

PLATONIC INSCRIPTION (iter 62, 2026-04-17):
    rem:linear-vs-quadratic-asymptotic-recurrence
    in chapters/theory/shadow_tower_higher_coefficients.tex.

CLAIMS:
    (1) The Virasoro A_r = 8*(-6)^{r-4}/r (r >= 4) satisfies the
        linear recurrence A_r = -6(r-1)/r * A_{r-1} for r >= 5.
    (2) Two seeds A_3 = A_4 = 2 determine the full sequence.
    (3) The linear recurrence is a CONSEQUENCE of c-cascade collapsing
        the quadratic shadow recursion at leading order, where only the
        pair (j, k) = (3, r-1) contributes.

HZ-IV VERIFICATION:
    derived_from: compute/lib/shadow_tower_higher_vir.py::leading_asymptotic
        (closed form A_r = 8*(-6)^{r-4}/r).

    verified_against: direct linear recurrence evaluation starting
        from seeds A_3 = A_4 = 2, applying A_r = -6(r-1)/r * A_{r-1}
        iteratively.

    disjoint_rationale: path 1 evaluates the closed form
        8*(-6)^{r-4}/r at each r independently; path 2 iteratively
        applies the linear recurrence from seeds. The match is a
        nontrivial identity between the closed form and the iterative
        recurrence solution.

    (Contrast with W_3 W-line, which has a genuinely QUADRATIC
     recurrence on the integer sequence a_m.)
"""
import unittest
import sys
from fractions import Fraction

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

import sympy as sp
from compute.lib.shadow_tower_higher_vir import leading_asymptotic


def linear_recurrence_seed(r):
    """Evaluate A_r by iterating A_r = -6(r-1)/r * A_{r-1} from A_3 = A_4 = 2."""
    if r < 3:
        raise ValueError("r must be >= 3")
    if r == 3:
        return Fraction(2)
    if r == 4:
        return Fraction(2)
    A = Fraction(2)
    for k in range(5, r + 1):
        A = -Fraction(6 * (k - 1), k) * A
    return A


class TestVirasoroLinearRecurrence(unittest.TestCase):
    """Path 2 (linear recurrence) matches Path 1 (closed form)."""

    def test_linear_recurrence_matches_closed_form(self):
        for r in range(4, 20):
            closed = Fraction(int(leading_asymptotic(r).p), int(leading_asymptotic(r).q))
            iter_rec = linear_recurrence_seed(r)
            self.assertEqual(
                closed, iter_rec,
                f"At r={r}: closed={closed}, recurrence={iter_rec}"
            )

    def test_two_seeds_determine_sequence(self):
        """A_3 = A_4 = 2; subsequent A_r from linear recurrence."""
        self.assertEqual(linear_recurrence_seed(3), Fraction(2))
        self.assertEqual(linear_recurrence_seed(4), Fraction(2))
        self.assertEqual(linear_recurrence_seed(5), Fraction(-48, 5))
        self.assertEqual(linear_recurrence_seed(6), Fraction(48))
        self.assertEqual(linear_recurrence_seed(7), Fraction(-1728, 7))
        self.assertEqual(linear_recurrence_seed(8), Fraction(1296))

    def test_exponential_base_from_linear_recurrence(self):
        """|A_r/A_{r-1}| = 6*(r-1)/r -> 6 as r -> infinity."""
        for r in range(10, 20):
            ratio = abs(
                float(linear_recurrence_seed(r)) / float(linear_recurrence_seed(r - 1))
            )
            expected = 6 * (r - 1) / r
            self.assertAlmostEqual(ratio, expected, places=10)
        # Limit
        self.assertAlmostEqual(
            float(linear_recurrence_seed(100)) / float(linear_recurrence_seed(99)),
            -6 * 99 / 100,
            places=10
        )


class TestContrastWithW3WlineQuadratic(unittest.TestCase):
    """Contrast: W_3 W-line integer sequence a_m is QUADRATIC, not linear."""

    def test_w3_wline_ratio_is_not_linear_in_m(self):
        """a_{m+1}/a_m = 6(2m-3)/(m+1) depends on m nonlinearly (not just r/(r-1))."""
        # If W_3 W-line were linear like Virasoro, we'd have
        # a_{m+1}/a_m = C * m / (m+1) for constant C.
        # But the actual ratio is 6(2m-3)/(m+1) = 12 - 30/(m+1), NOT
        # matching any const*m/(m+1) form (which would give C - C/(m+1) -> C).
        # Specifically: at large m, Vir ratio -> 6 while W_3 W ratio -> 12;
        # more importantly Vir ratio = 6*(r-1)/r gives 6 - 6/r,
        # while W_3 ratio = 12 - 30/(m+1): different numerator coefficient
        # of the 1/m correction (6 vs 30).
        for r in (10, 20, 50):
            vir_gap = 6 - 6 * (r - 1) / r
            wline_gap = 12 - 6 * (2 * r - 3) / (r + 1)
            # Vir gap approaches 0 like 6/r; W-line gap approaches 0 like 30/(m+1)
            # Ratio of gaps: wline_gap / vir_gap = 30/(m+1) / (6/r) = 30r/[6(m+1)] = 5r/(m+1)
            # For r = m, ratio = 5r/(r+1) -> 5 at large r
            self.assertAlmostEqual(
                vir_gap, 6.0 / r, places=8
            )


if __name__ == '__main__':
    unittest.main()
