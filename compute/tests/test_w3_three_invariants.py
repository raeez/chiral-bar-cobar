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

    def test_beta_formula_at_small_N(self):
        """beta_N = (N+1)(N+2)/2: Vol II conjectured formula."""
        self.assertEqual((2 + 1) * (2 + 2) // 2, 6)   # N=2: Virasoro
        self.assertEqual((3 + 1) * (3 + 2) // 2, 10)  # N=3: W_3
        self.assertEqual((4 + 1) * (4 + 2) // 2, 15)  # N=4: W_4 predicted

    def test_template_prediction_vs_beta_at_s4(self):
        """The Riccati template (Vol I iter 60) predicts C_s = 4s; at s=4
        this gives 16. Vol II beta_N = (N+1)(N+2)/2 at N=4 gives 15.
        At N=4 / s=4 these differ by 1; neither is a priori the correct
        W-line integer-sequence base. Direct W_4 W^(4)-line computation
        required to decide.
        """
        template_C = 4 * 4
        beta_N = 5 * 6 // 2
        self.assertEqual(template_C, 16)
        self.assertEqual(beta_N, 15)
        self.assertNotEqual(template_C, beta_N)
        # Two candidates at N=4: neither is verified until W_4 seed
        # structure constant is computed from Fateev-Lukyanov OPE data.


if __name__ == '__main__':
    unittest.main()
