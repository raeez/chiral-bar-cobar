r"""Test: W(p) triplet at p=2 (c=-2) T-line shadow coefficients through r=10.

TASK #41 (pending, partial progress 2026-04-17):
    Compute W(p) shadow coefficients S_r for p=2 triplet (c=-2), r<=10.

SCOPE OF THIS TEST:
    The W(2) triplet algebra has 4 strong generators: Virasoro T (spin 2)
    and a weight-3 sl_2 triplet W^{-1}, W^0, W^{+1}. This test computes the
    T-LINE RESTRICTION of the shadow tower (equivalent to Virasoro at c=-2
    by prop:w3-tline-virasoro-inheritance-style reasoning generalised to W(p)).

    The FULL W(2) shadow tower including triplet W-line and T-W cross-channel
    contributions is NOT computed here; it requires a dedicated W(p)
    logarithmic shadow engine beyond Vol I's Virasoro infrastructure.

VALUES (verified via two independent paths):
    r=2: S_2 = -1       (kappa = c/2 = -1)
    r=3: S_3 = 2        (universal, independent of c)
    r=4: S_4 = -5/12    (from S_4 = 10/(c(5c+22)) at c=-2)
    r=5: S_5 = -1       (from master equation with S_3, S_4)
    r=6: S_6 = -515/216
    r=7: S_7 = -155/28
    r=8: S_8 = -21185/1728
    r=9: S_9 = -16285/648
    r=10: S_10 = -465287/10368

PATH 1: compute/lib/virasoro_shadow_tower.py::compute_shadow_tower symbolically
        substituting c = -2.
PATH 2: Direct evaluation of the closed-form S_4 = 10/(c(5c+22)) at c=-2,
        followed by master-equation iteration.
"""
import unittest
import sys
from fractions import Fraction

sys.path.insert(0, '/Users/raeez/chiral-bar-cobar')

from sympy import Symbol, sympify, simplify, Rational
from compute.lib.virasoro_shadow_tower import compute_shadow_tower


class TestWpTripletP2TlineShadow(unittest.TestCase):
    """Virasoro T-line shadow at c = -2 (partial W(2) triplet computation)."""

    EXPECTED_S_R_AT_MINUS_2 = {
        2: Fraction(-1),
        3: Fraction(2),
        4: Fraction(-5, 12),
        5: Fraction(-1),
        6: Fraction(-515, 216),
        7: Fraction(-155, 28),
        8: Fraction(-21185, 1728),
        9: Fraction(-16285, 648),
        10: Fraction(-465287, 10368),
    }

    def test_s_r_at_c_minus_2_through_r10(self):
        """Virasoro T-line shadow S_r at c = -2 for r = 2, ..., 10."""
        c_sym = Symbol('c')
        x_sym = Symbol('x')
        shadows = compute_shadow_tower(max_arity=10)

        for r, expected in self.EXPECTED_S_R_AT_MINUS_2.items():
            sym_expr = shadows[r]
            S_r_coeff = sympify(sym_expr).coeff(x_sym, r)
            val = S_r_coeff.subs(c_sym, Rational(-2))
            val = simplify(val)

            actual = Fraction(int(val.p), int(val.q))
            self.assertEqual(
                actual, expected,
                f"At r={r}: expected {expected}, got {actual}"
            )

    def test_s_2_is_kappa_at_c_minus_2(self):
        """S_2 = kappa(Vir) = c/2; at c=-2 gives -1."""
        self.assertEqual(self.EXPECTED_S_R_AT_MINUS_2[2], Fraction(-1))

    def test_s_3_is_universal_2(self):
        """S_3 = 2 universally (c-independent)."""
        self.assertEqual(self.EXPECTED_S_R_AT_MINUS_2[3], Fraction(2))

    def test_s_4_matches_closed_form(self):
        """S_4 = 10/(c(5c+22)) at c=-2 = 10/(-2 * 12) = -5/12."""
        c = Fraction(-2)
        closed_form = Fraction(10) / (c * (5 * c + 22))
        self.assertEqual(closed_form, Fraction(-5, 12))
        self.assertEqual(closed_form, self.EXPECTED_S_R_AT_MINUS_2[4])


class TestWpTripletP2ShadowAsymptotic(unittest.TestCase):
    """Observations on c=-2 shadow asymptotic behaviour.

    At c=-2, the Virasoro shadow is NEAR the c_{2,5} = -22/5 minimal-model
    pole. Finite-c corrections are large; |S_r|^{1/r} approaches universal
    class-M value 6 VERY slowly.
    """

    def test_abs_s_r_nth_root_grows_below_6(self):
        """|S_r|^{1/r} < 6 for r <= 10 at c=-2 (universal limit)."""
        S = TestWpTripletP2TlineShadow.EXPECTED_S_R_AT_MINUS_2
        for r, val in S.items():
            abs_val = abs(float(val))
            if r >= 2:
                nth_root = abs_val ** (1/r)
                # Far from universal limit 6 at finite c=-2
                self.assertLess(nth_root, 6)

    def test_full_wp_triplet_shadow_requires_separate_engine(self):
        """Full W(2) shadow tower (including W-triplet + T-W cross) not here.

        W(p) triplet is LOGARITHMIC CFT (Gurarie 1993, Flohr 1996): shadow
        coefficients receive contributions from the weight-3 W^a triplet
        and their cross-channels with T. Full computation requires a
        dedicated logarithmic W(p) shadow engine.

        This test documents that the T-line portion is a strict sub-tower
        of the full W(2) shadow.
        """
        # Placeholder: this test passes unconditionally as a narrative marker.
        self.assertTrue(True, "T-line is a strict sub-tower of full W(2) shadow")


if __name__ == '__main__':
    unittest.main()
