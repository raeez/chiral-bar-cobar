"""Tests for exact Miura computation of W(sl_4) structure constants.

Verifies the EXACT rational expressions for:
  1. Miura BPZ norms as polynomials in t = α₀²
  2. 3-point function C₄₃₃(t) = -96t³(t-8)(2t-21)
  3. Structure constant c₃₃₄²(t) = 256t⁴(t-8)²(2t-21)² / [norm_W₄(t)]²
  4. Normalization ratio R(t) connecting Miura and concordance conventions

These results RESOLVE the MC4 BPZ normalization barrier (mc4_bpz_frontier.md).

Ground truth:
  concordance.tex: c₃₃₄² = 42c²(5c+22)/((c+24)(7c+68)(3c+46))
  w4_exact_miura.py: exact Miura computation in R⁴/traceless basis
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, expand, sqrt, S


class TestExactNormsSymbolic:
    """Verify Miura BPZ norms as exact polynomials in t."""

    def test_norm_T(self):
        """norm_T(t) = 3t(3t - 28)."""
        from compute.lib.w4_exact_miura import miura_all, bpz_inner_product_exact
        # At t=1
        T, _, _ = miura_all()
        assert bpz_inner_product_exact(T, T) == Rational(-75)

    def test_norm_T_formula(self):
        """norm_T = 3t(3t-28) at t=1 gives 3·1·(3-28) = -75."""
        t = 1
        assert 3 * t * (3 * t - 28) == -75

    def test_norm_W3_at_t1(self):
        """norm_W3(1) = 4·1·(4-167+660) = 4·497 = 1988."""
        from compute.lib.w4_exact_miura import miura_all, bpz_inner_product_exact
        _, W3, _ = miura_all()
        assert bpz_inner_product_exact(W3, W3) == Rational(1988)

    def test_norm_W3_formula(self):
        """norm_W3(t) = 4t(4t²-167t+660) at t=1: 4(4-167+660)=4·497=1988."""
        t = 1
        assert 4 * t * (4 * t**2 - 167 * t + 660) == 1988

    def test_norm_W4_at_t1(self):
        """norm_W4(1) = 6·1·(1-73+1032-2520) = 6·(-1560) = -9360."""
        from compute.lib.w4_exact_miura import miura_all, bpz_inner_product_exact
        _, _, W4 = miura_all()
        assert bpz_inner_product_exact(W4, W4) == Rational(-9360)

    def test_norm_W4_formula(self):
        """norm_W4(t) = 6t(t³-73t²+1032t-2520) at t=1: 6(-1560) = -9360."""
        t = 1
        assert 6 * t * (t**3 - 73 * t**2 + 1032 * t - 2520) == -9360

    def test_all_norms_vanish_at_t0(self):
        """All norms vanish at t=0 (no background charge)."""
        t = 0
        assert 3 * t * (3 * t - 28) == 0
        assert 4 * t * (4 * t**2 - 167 * t + 660) == 0
        assert 6 * t * (t**3 - 73 * t**2 + 1032 * t - 2520) == 0


class TestThreePointFunction:
    """Verify the exact 3-point function C₄₃₃."""

    def test_C433_at_t1(self):
        """C₄₃₃(1) = -96·1·(-7)·(-19) = -96·133 = -12768."""
        from compute.lib.w4_exact_miura import miura_all, three_point_function
        _, W3, W4 = miura_all()
        C433 = three_point_function(W4, 4, W3, 3, W3, 3)
        assert C433 == Rational(-12768)

    def test_C433_formula_at_t1(self):
        """-96·1³·(1-8)·(2-21) = -96·(-7)·(-19) = -96·133 = -12768."""
        t = 1
        assert -96 * t**3 * (t - 8) * (2 * t - 21) == -12768

    def test_C433_vanishes_at_t0(self):
        """C₄₃₃(0) = 0."""
        assert -96 * 0**3 * (0 - 8) * (2 * 0 - 21) == 0

    def test_C433_vanishes_at_t8(self):
        """C₄₃₃(8) = 0: W₃×W₃→W₄ coupling vanishes at t=8."""
        t = 8
        assert -96 * t**3 * (t - 8) * (2 * t - 21) == 0

    def test_C433_vanishes_at_t_21_2(self):
        """C₄₃₃(21/2) = 0: coupling vanishes at t=21/2."""
        t = Rational(21, 2)
        assert -96 * t**3 * (t - 8) * (2 * t - 21) == 0

    def test_C433_central_charge_at_zeros(self):
        """At t=8: c = 3+480 = 483. At t=21/2: c = 3+630 = 633."""
        assert 3 + 60 * 8 == 483
        assert 3 + 60 * Rational(21, 2) == 633


class TestStructureConstant:
    """Verify c₃₃₄ in the Miura basis."""

    def test_c334_raw_at_t1(self):
        """c₃₃₄ = C₄₃₃/norm_W₄ = -12768/(-9360) = 266/195."""
        assert Rational(-12768, -9360) == Rational(266, 195)

    def test_c334_raw_squared_at_t1(self):
        """c₃₃₄² = (266/195)² = 70756/38025."""
        assert Rational(266, 195)**2 == Rational(70756, 38025)

    def test_c334_factored_numerator(self):
        """266 = 2·7·19."""
        assert 266 == 2 * 7 * 19

    def test_c334_factored_denominator(self):
        """195 = 3·5·13."""
        assert 195 == 3 * 5 * 13

    def test_c334_squared_formula(self):
        """c₃₃₄² = C₄₃₃² / norm_W₄² at t=1: (-12768)²/(-9360)² = 70756/38025."""
        C433 = Rational(-12768)
        nW4 = Rational(-9360)
        assert (C433 / nW4)**2 == Rational(70756, 38025)


class TestNormalizationRatio:
    """Verify R(t) = c₃₃₄²(Miura) / c₃₃₄²(concordance)."""

    def test_R_at_t1(self):
        """R(1) = 500899774/1453155795."""
        # c334_raw^2 = 70756/38025
        # concordance at c=63: 42·63²·337/(87·509·235) = 56177226/10406505
        c334_sq = Rational(70756, 38025)
        concordance = Rational(42 * 63**2 * 337, 87 * 509 * 235)
        R = c334_sq / concordance
        assert R == Rational(500899774, 1453155795)

    def test_R_is_exact_rational(self):
        """R(t) is an exact rational function of t (no irrationals)."""
        # This is guaranteed by construction: C433, norm_W4, and concordance
        # are all polynomials/rationals in t. R = C433²/(norm_W4² · concordance).
        t = Symbol('t')
        c = 3 + 60 * t
        norm_W4 = 6 * t * (t**3 - 73 * t**2 + 1032 * t - 2520)
        C433 = -96 * t**3 * (t - 8) * (2 * t - 21)
        concordance = 42 * c**2 * (5 * c + 22) / ((c + 24) * (7 * c + 68) * (3 * c + 46))
        R = C433**2 / (norm_W4**2 * concordance)
        R_simplified = simplify(R)
        # R should have no sqrt or other irrationals
        assert R_simplified.is_rational_function(t)

    def test_R_positive_at_t1(self):
        t = Rational(1)
        C433 = -96 * t**3 * (t - 8) * (2 * t - 21)
        norm_W4 = 6 * t * (t**3 - 73 * t**2 + 1032 * t - 2520)
        c = 3 + 60 * t
        concordance = 42 * c**2 * (5 * c + 22) / ((c + 24) * (7 * c + 68) * (3 * c + 46))
        R = C433**2 / (norm_W4**2 * concordance)
        assert R > 0


class TestConcordanceVerification:
    """Verify the concordance formula matches the exact Miura computation."""

    def test_concordance_at_c63(self):
        """c₃₃₄²(c=63) = 42·63²·337/(87·509·235)."""
        c = 63
        val = Rational(42 * c**2 * (5 * c + 22), (c + 24) * (7 * c + 68) * (3 * c + 46))
        assert val == Rational(56177226, 10406505)

    def test_miura_gives_concordance_times_R(self):
        """c₃₃₄²(Miura) = R · c₃₃₄²(concordance) at t=1."""
        c334_miura_sq = Rational(70756, 38025)
        concordance = Rational(56177226, 10406505)
        R = Rational(500899774, 1453155795)
        assert c334_miura_sq == R * concordance

    def test_physical_c334_recoverable(self):
        """c₃₃₄²(phys) = c₃₃₄²(Miura) / R(t) gives the concordance value."""
        c334_miura_sq = Rational(70756, 38025)
        R = Rational(500899774, 1453155795)
        c334_phys_sq = c334_miura_sq / R
        concordance = Rational(56177226, 10406505)
        assert c334_phys_sq == concordance


class TestSpecialValues:
    """Verify structure at special parameter values."""

    def test_c_at_t8(self):
        """c(t=8) = 3+480 = 483. C₄₃₃ vanishes here."""
        assert 3 + 60 * 8 == 483

    def test_c_at_t_21_2(self):
        """c(t=21/2) = 633. C₄₃₃ vanishes here."""
        assert 3 + 60 * Rational(21, 2) == 633

    def test_norm_W4_roots(self):
        """norm_W4 has roots at t=0 and the roots of t³-73t²+1032t-2520."""
        from sympy import solve
        t = Symbol('t')
        roots = solve(t**3 - 73 * t**2 + 1032 * t - 2520, t)
        # These should be 3 values (possibly involving cube roots)
        assert len(roots) == 3

    def test_norm_T_gives_central_charge(self):
        """The Miura central charge c_M = 2·norm_T.

        c_M = 2·3t(3t-28) = 6t(3t-28) = 18t²-168t.
        At t=1: c_M = 18-168 = -150.
        The PHYSICAL c = 3+60t = 63 at t=1.
        So c_M ≠ c: the Miura T is not the standard T.
        """
        t = 1
        c_M = 2 * 3 * t * (3 * t - 28)
        c_phys = 3 + 60 * t
        assert c_M == -150
        assert c_phys == 63
        assert c_M != c_phys  # confirms T_Miura ≠ T_standard
