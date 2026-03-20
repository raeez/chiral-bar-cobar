"""Tests for Kac-Chevalley analysis: Gram matrices, determinants, discriminants.

Ground truth:
  Level 4 Gram: G11 = 5c, G12 = 3c, G22 = c(c+8)/2   [Virasoro Verma]
  det(G_4) = c^2(5c+22)/2                               [Kac determinant]
  Kac-Chevalley connection: SPURIOUS at level 4          [det does NOT divide disc]
  Eigenvalue collision at c = -22/5 (rank drop)          [Kac null vector]
  (5c+22) in both det and disc at level 6                [shared factor]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from sympy import (
    Symbol, Rational, simplify, factor, expand, S, Matrix,
    Poly
)

from lib.kac_chevalley_test import (
    virasoro_level4_gram,
    virasoro_level4_analysis,
    virasoro_level6_gram,
    virasoro_level6_analysis,
    w3_level4_gram,
    w3_level4_analysis,
    char_poly_discriminant_2x2,
    char_poly_as_sympy_poly,
    poly_discriminant,
)

c = Symbol('c')
lam = Symbol('lambda')


# ===========================================================================
# TestLevel4Gram (L1-L5)
# ===========================================================================

class TestLevel4Gram:
    """Virasoro level-4 Gram matrix entries and determinant."""

    def test_L1_G11_equals_5c(self):
        """G[0,0] = <L_4 L_{-4}> = 5c (from [L_4,L_{-4}] on vacuum)."""
        G = virasoro_level4_gram()
        assert simplify(G[0, 0] - 5*c) == 0

    def test_L2_G12_equals_3c(self):
        """G[0,1] = <L_4 L_{-2}^2> = 3c."""
        G = virasoro_level4_gram()
        assert simplify(G[0, 1] - 3*c) == 0

    def test_L3_G22_equals_c_times_cplus8_over2(self):
        """G[1,1] = <L_2^2 L_{-2}^2> = c(c+8)/2."""
        G = virasoro_level4_gram()
        expected = c * (c + 8) / 2
        assert simplify(G[1, 1] - expected) == 0

    def test_L4_gram_symmetric(self):
        """Gram matrix is symmetric."""
        G = virasoro_level4_gram()
        assert simplify(G[0, 1] - G[1, 0]) == 0

    def test_L5_det_equals_c_sq_5cplus22_over2(self):
        """det(G_4) = c^2(5c+22)/2."""
        G = virasoro_level4_gram()
        det_G = factor(G.det())
        expected = c**2 * (5*c + 22) / 2
        assert simplify(expand(det_G) - expand(expected)) == 0


# ===========================================================================
# TestKacChevalleySpurious (KC1-KC4)
# ===========================================================================

class TestKacChevalleySpurious:
    """The Kac-Chevalley connection is SPURIOUS: det does not divide discriminant."""

    def test_KC1_det_does_not_divide_disc(self):
        """det(G_4) does NOT divide disc(char poly) at level 4."""
        a4 = virasoro_level4_analysis()
        tr4 = a4['tr_G']
        det4 = expand(a4['det_G'])
        disc4 = expand(char_poly_discriminant_2x2(tr4, det4))

        det4_poly = Poly(det4, c)
        disc4_poly = Poly(disc4, c)
        _, remainder = disc4_poly.div(det4_poly)
        assert not remainder.is_zero, "det should NOT divide disc — connection is spurious"

    def test_KC2_disc_at_minus22over5_nonzero(self):
        """disc(char poly) at c=-22/5 is nonzero: eigenvalues do NOT coincide there.

        At level 4, the Kac zero c=-22/5 makes det(G)=0 but the
        discriminant does NOT vanish, so the eigenvalues do not collide.
        """
        a4 = virasoro_level4_analysis()
        tr4 = a4['tr_G']
        det4 = expand(a4['det_G'])
        disc4 = expand(char_poly_discriminant_2x2(tr4, det4))
        val = disc4.subs(c, Rational(-22, 5))
        assert val != 0, "disc should be nonzero at c=-22/5"

    def test_KC3_eigenvalue_collision_at_minus22over5(self):
        """At c=-22/5: det(G)=0 means one eigenvalue is zero (rank drop),
        but the other eigenvalue is nonzero, so they do NOT coincide."""
        G = virasoro_level4_gram()
        G_eval = G.subs(c, Rational(-22, 5))
        det_eval = G_eval.det()
        assert det_eval == 0, "det should vanish at c=-22/5"
        # Rank should be 1 (one zero eigenvalue, one nonzero)
        assert G_eval.rank() == 1

    def test_KC4_det_expected_value(self):
        """Cross-check: analysis function returns correct expected determinant."""
        a4 = virasoro_level4_analysis()
        expected = a4['det_G_expected']
        assert simplify(expand(a4['det_G']) - expand(expected)) == 0


# ===========================================================================
# TestLevel6Shared (L6_1-L6_3)
# ===========================================================================

class TestLevel6Shared:
    """(5c+22) appears in both det and disc at level 6."""

    def test_L6_1_det_has_5cplus22_factor(self):
        """det(G_6) vanishes at c=-22/5."""
        G6 = virasoro_level6_gram()
        det6 = expand(G6.det())
        val = det6.subs(c, Rational(-22, 5))
        assert val == 0, "det(G_6) should vanish at c=-22/5"

    def test_L6_2_disc_has_5cplus22_factor(self):
        """disc(char poly) at level 6 also vanishes at c=-22/5.

        At level 6 (4x4), the Kac zero c=-22/5 IS shared with the
        discriminant — eigenvalues DO collide there.
        """
        G6 = virasoro_level6_gram()
        cp6 = char_poly_as_sympy_poly(G6)
        disc6 = expand(poly_discriminant(cp6))
        val = disc6.subs(c, Rational(-22, 5))
        assert val == 0, "disc should vanish at c=-22/5 at level 6"

    def test_L6_3_gram_symmetric(self):
        """Level-6 Gram matrix is symmetric."""
        G6 = virasoro_level6_gram()
        for i in range(4):
            for j in range(i+1, 4):
                assert simplify(G6[i, j] - G6[j, i]) == 0


# ===========================================================================
# TestW3Level4 (W1-W2)
# ===========================================================================

class TestW3Level4:
    """W_3 level-4 Gram matrix."""

    def test_W1_block_diagonal(self):
        """W_3 level-4 Gram is block diagonal: Virasoro 2x2 + W-scalar."""
        G = w3_level4_gram()
        # Cross terms vanish
        assert G[0, 2] == 0
        assert G[1, 2] == 0
        assert G[2, 0] == 0
        assert G[2, 1] == 0

    def test_W2_det_equals_c_cubed_5cplus22(self):
        """det(G_{W_3,level4}) = c^3(5c+22)."""
        G = w3_level4_gram()
        det_G = expand(G.det())
        expected = expand(c**3 * (5*c + 22))
        assert simplify(det_G - expected) == 0
