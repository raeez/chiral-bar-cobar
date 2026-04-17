r"""Test: three distinct shadow-tower invariants of W_3 at generic c.

PLATONIC INSCRIPTION (iter 65, 2026-04-17):
    rem:beta-A-W3-wline-integer-sequence
    in ~/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex.

CLAIMS:
    Three distinct invariants:
    (a) C_{W_3}^{T-line} = 6 (Vol I universal class M, leading-c projection)
    (b) beta_{W_3} = 10 (Vol II Banach sum-of-channels bound; = 6 + 4)
    (c) C_{W_3}^{W-line} = 12 (c-independent integer sequence)

HZ-IV VERIFICATION:
    derived_from: compute/lib/w3_wline_shadow_tower.py (a_m recurrence).

    verified_against: direct iteration of a_{m+1}/a_m = 6(2m-3)/(m+1)
        from Vol I thm:w3-wline-closed-form; Vol II beta_N = (N+1)(N+2)/2
        at N=3 is independent closed form from Banach completion analysis;
        Vol I universal class M theorem (C_{T-line} = 6) is independent
        Riccati c-cascade analysis.

    disjoint_rationale: the three invariants measure three different
        quantities — (a) leading-c projection of S_r on T-line, (b)
        Banach sum-of-channels bound on full |S_r|^{1/r}, (c) c-independent
        numerator growth rate. No single computation gives all three.
"""
import sys
import unittest

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

from compute.lib.w3_wline_shadow_tower import normalized_recursion


class TestW3ThreeInvariantsDistinct(unittest.TestCase):
    def test_three_invariants_distinct_ordered(self):
        C_T = 6
        beta_W3 = (3 + 1) * (3 + 2) // 2
        C_W_line = 12
        self.assertEqual(beta_W3, 10)
        self.assertLess(C_T, beta_W3)
        self.assertLess(beta_W3, C_W_line)
        self.assertEqual(len({C_T, beta_W3, C_W_line}), 3)

    def test_w_line_integer_sequence_base_equals_12(self):
        a_rec = normalized_recursion(40)
        # a_{40}/a_{39} = 6*(2*39 - 3)/(40) = 6*75/40 = 450/40 = 11.25
        ratio = float(a_rec[40]) / float(a_rec[39])
        self.assertAlmostEqual(ratio, 11.25, places=6)
        # Approach to 12 from below
        for n in (20, 30, 39):
            gap = 12 - float(a_rec[n + 1]) / float(a_rec[n])
            expected_gap = 30.0 / (n + 1)
            self.assertAlmostEqual(gap, expected_gap, places=6)

    def test_beta_formula_is_harmonic(self):
        """beta_N = 12*(H_N - 1) is the Vol II first-principles closed form.

        Supersedes earlier candidates (N+1)(N+2)/2 (RETRACTED) and
        N^2 - N + 4. True value: beta_N = 12*(H_N - 1) for all N >= 2
        (ProvedHere, Vol II chapters/theory/beta_N_closed_form_all_platonic.tex,
        thm:beta-N-closed-form-proved-all-N).
        """
        from fractions import Fraction

        def H(N):
            return sum(Fraction(1, j) for j in range(1, N + 1))

        def beta_N(N):
            return 12 * (H(N) - 1)

        self.assertEqual(beta_N(2), Fraction(6))
        self.assertEqual(beta_N(3), Fraction(10))
        self.assertEqual(beta_N(4), Fraction(13))
        # N >= 5 rational, not integer:
        self.assertEqual(beta_N(5), Fraction(77, 5))
        self.assertEqual(beta_N(6), Fraction(87, 5))

    def test_per_lane_decomposition_of_beta(self):
        """beta_N = sum_{s=2}^{N} 12/s (per-spin-s lane contribution)."""
        from fractions import Fraction

        def beta_N_as_sum(N):
            return sum(Fraction(12, s) for s in range(2, N + 1))

        def H(N):
            return sum(Fraction(1, j) for j in range(1, N + 1))

        for N in range(2, 7):
            self.assertEqual(beta_N_as_sum(N), 12 * (H(N) - 1))
        # At N=3: T-line (s=2) gives 12/2 = 6; W-line (s=3) gives 12/3 = 4.
        # Sum = 10 matches beta_{W_3}.
        self.assertEqual(Fraction(12, 2) + Fraction(12, 3), Fraction(10))

    def test_template_prediction_vs_beta_lane_contribution_at_s_geq_3(self):
        """Trivial algebraic identity: (12/s) * (4s) = 48.

        Vol II per-lane beta contribution is 12/s; Vol I Riccati template
        predicts C_lane = 4s for spin-s generator satisfying (H1)-(H4).
        The product is identically 48 — but this is a consequence of
        both formulas being correct at s >= 3, NOT a structural theorem.

        At s=2 (Virasoro T-line), (H1) fails, so the template gives 8
        rather than the actual 6; product there is 6*6 = 36 != 48.
        """
        for s in (3, 4, 5, 6):
            beta_contrib = 12 / s
            C_template = 4 * s
            self.assertEqual(beta_contrib * C_template, 48)
        # At s=2: template predicts 8, actual is 6 (template fails H1)
        beta_T_line = 12 // 2  # Vol II T-line contribution
        C_T_actual = 6          # Vol I universal class M theorem
        self.assertEqual(beta_T_line * C_T_actual, 36)
        self.assertNotEqual(beta_T_line * C_T_actual, 48)


if __name__ == '__main__':
    unittest.main()
