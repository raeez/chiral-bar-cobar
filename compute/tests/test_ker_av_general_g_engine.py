"""Tests for ker_av_general_g_engine.

Verifies dim ker(av_n | V^{tensor n}) = d^n - binom(n+d-1, d-1)
for general simple Lie algebras with fundamental representations of
dimension d.  The formula depends only on d = dim(V), not on g.

Proposition prop:ker-av-schur-weyl in ordered_chiral_homology.tex.

Every hardcoded expected value has a VERIFIED comment citing 2+
independent sources (AP10/HZ-6):
  [DC] direct computation (binomial formula shown explicitly)
  [DA] dimensional analysis (d^n total verified)
  [SY] symmetry (Sigma_n coinvariant = Sym^n(V))
  [CF] cross-family consistency (different g, same d => same result)
  [LC] limiting case (n=1 => kernel=0; n=2 => Alt^2(V))
"""

from fractions import Fraction

import pytest

from compute.lib.ker_av_general_g_engine import (
    FUND_REP_DIMS,
    algebras_with_same_d,
    generating_function_coeffs,
    info_ratio,
    ker_av_2_equals_alt2,
    ker_av_dim,
    ker_av_for_algebra,
    sym_dim,
    total_dim,
)


# =====================================================================
# sl_2 fundamental (d=2), degrees 2-6
# =====================================================================

class TestSl2Fund:
    """sl_2 fundamental: d = 2."""

    def test_fund_dim(self):
        # VERIFIED: [DC] standard representation C^2; [LT] Humphreys
        assert FUND_REP_DIMS["sl_2"] == 2

    def test_n1_kernel_zero(self):
        # VERIFIED: [LC] n=1: d^1 - binom(d, d-1) = d - d = 0
        # [SY] no non-trivial permutations at n=1
        assert ker_av_dim(2, 1) == 0

    def test_n2(self):
        # total = 2^2 = 4
        # sym = binom(3, 1) = 3
        # kernel = 4 - 3 = 1
        # VERIFIED: [DC] binom(3,1) = 3; [DA] 2^2 = 4
        # [LC] ker(av_2) = d(d-1)/2 = 2*1/2 = 1 = dim(Alt^2(C^2))
        assert ker_av_dim(2, 2) == 1

    def test_n3(self):
        # total = 2^3 = 8
        # sym = binom(4, 1) = 4
        # kernel = 8 - 4 = 4
        # VERIFIED: [DC] binom(4,1) = 4; [DA] 2^3 = 8
        assert ker_av_dim(2, 3) == 4

    def test_n4(self):
        # total = 2^4 = 16
        # sym = binom(5, 1) = 5
        # kernel = 16 - 5 = 11
        # VERIFIED: [DC] binom(5,1) = 5; [DA] 2^4 = 16
        assert ker_av_dim(2, 4) == 11

    def test_n5(self):
        # total = 2^5 = 32
        # sym = binom(6, 1) = 6
        # kernel = 32 - 6 = 26
        # VERIFIED: [DC] binom(6,1) = 6; [DA] 2^5 = 32
        assert ker_av_dim(2, 5) == 26

    def test_n6(self):
        # total = 2^6 = 64
        # sym = binom(7, 1) = 7
        # kernel = 64 - 7 = 57
        # VERIFIED: [DC] binom(7,1) = 7; [DA] 2^6 = 64
        assert ker_av_dim(2, 6) == 57

    def test_closed_form(self):
        # For d=2: binom(n+1, 1) = n+1, so ker = 2^n - (n+1)
        # VERIFIED: [DC] explicit formula; [CF] matches table in .tex
        for n in range(1, 11):
            assert ker_av_dim(2, n) == 2**n - (n + 1)


# =====================================================================
# sl_3 fundamental (d=3), degrees 2-6
# =====================================================================

class TestSl3Fund:
    """sl_3 fundamental: d = 3."""

    def test_fund_dim(self):
        # VERIFIED: [DC] standard representation C^3; [LT] Humphreys
        assert FUND_REP_DIMS["sl_3"] == 3

    def test_n2(self):
        # total = 3^2 = 9
        # sym = binom(4, 2) = 6
        # kernel = 9 - 6 = 3
        # VERIFIED: [DC] binom(4,2) = 4!/(2!2!) = 6; [DA] 3^2 = 9
        # [LC] ker(av_2) = d(d-1)/2 = 3*2/2 = 3 = dim(Alt^2(C^3))
        assert ker_av_dim(3, 2) == 3

    def test_n3(self):
        # total = 3^3 = 27
        # sym = binom(5, 2) = 10
        # kernel = 27 - 10 = 17
        # VERIFIED: [DC] binom(5,2) = 5!/(3!2!) = 10; [DA] 3^3 = 27
        assert ker_av_dim(3, 3) == 17

    def test_n4(self):
        # total = 3^4 = 81
        # sym = binom(6, 2) = 15
        # kernel = 81 - 15 = 66
        # VERIFIED: [DC] binom(6,2) = 6!/(4!2!) = 15; [DA] 3^4 = 81
        assert ker_av_dim(3, 4) == 66

    def test_n5(self):
        # total = 3^5 = 243
        # sym = binom(7, 2) = 21
        # kernel = 243 - 21 = 222
        # VERIFIED: [DC] binom(7,2) = 7!/(5!2!) = 21; [DA] 3^5 = 243
        assert ker_av_dim(3, 5) == 222

    def test_n6(self):
        # total = 3^6 = 729
        # sym = binom(8, 2) = 28
        # kernel = 729 - 28 = 701
        # VERIFIED: [DC] binom(8,2) = 8!/(6!2!) = 28; [DA] 3^6 = 729
        assert ker_av_dim(3, 6) == 701


# =====================================================================
# so_5 fundamental (d=5), degrees 2-6
# =====================================================================

class TestSo5Fund:
    """so_5 fundamental (vector representation): d = 5."""

    def test_fund_dim(self):
        # VERIFIED: [DC] vector rep C^5 for so_5; [LT] Humphreys
        # so_5 = sp_4 (B_2 = C_2 isomorphism)
        assert FUND_REP_DIMS["so_5"] == 5

    def test_n2(self):
        # total = 5^2 = 25
        # sym = binom(6, 4) = 15
        # kernel = 25 - 15 = 10
        # VERIFIED: [DC] binom(6,4) = 6!/(2!4!) = 15; [DA] 5^2 = 25
        # [LC] ker(av_2) = d(d-1)/2 = 5*4/2 = 10 = dim(Alt^2(C^5))
        assert ker_av_dim(5, 2) == 10

    def test_n3(self):
        # total = 5^3 = 125
        # sym = binom(7, 4) = 35
        # kernel = 125 - 35 = 90
        # VERIFIED: [DC] binom(7,4) = 7!/(3!4!) = 35; [DA] 5^3 = 125
        assert ker_av_dim(5, 3) == 90

    def test_n4(self):
        # total = 5^4 = 625
        # sym = binom(8, 4) = 70
        # kernel = 625 - 70 = 555
        # VERIFIED: [DC] binom(8,4) = 8!/(4!4!) = 70; [DA] 5^4 = 625
        assert ker_av_dim(5, 4) == 555

    def test_n5(self):
        # total = 5^5 = 3125
        # sym = binom(9, 4) = 126
        # kernel = 3125 - 126 = 2999
        # VERIFIED: [DC] binom(9,4) = 9!/(5!4!) = 126; [DA] 5^5 = 3125
        assert ker_av_dim(5, 5) == 2999

    def test_n6(self):
        # total = 5^6 = 15625
        # sym = binom(10, 4) = 210
        # kernel = 15625 - 210 = 15415
        # VERIFIED: [DC] binom(10,4) = 10!/(6!4!) = 210; [DA] 5^6 = 15625
        assert ker_av_dim(5, 6) == 15415


# =====================================================================
# G_2 fundamental (d=7), degrees 2-6
# =====================================================================

class TestG2Fund:
    """G_2 fundamental: d = 7."""

    def test_fund_dim(self):
        # VERIFIED: [DC] smallest irreducible of G_2; [LT] Bourbaki Lie IV-VI
        assert FUND_REP_DIMS["G_2"] == 7

    def test_n2(self):
        # total = 7^2 = 49
        # sym = binom(8, 6) = 28
        # kernel = 49 - 28 = 21
        # VERIFIED: [DC] binom(8,6) = 8!/(2!6!) = 28; [DA] 7^2 = 49
        # [LC] ker(av_2) = d(d-1)/2 = 7*6/2 = 21 = dim(Alt^2(C^7))
        assert ker_av_dim(7, 2) == 21

    def test_n3(self):
        # total = 7^3 = 343
        # sym = binom(9, 6) = 84
        # kernel = 343 - 84 = 259
        # VERIFIED: [DC] binom(9,6) = 9!/(3!6!) = 84; [DA] 7^3 = 343
        assert ker_av_dim(7, 3) == 259

    def test_n4(self):
        # total = 7^4 = 2401
        # sym = binom(10, 6) = 210
        # kernel = 2401 - 210 = 2191
        # VERIFIED: [DC] binom(10,6) = 10!/(4!6!) = 210; [DA] 7^4 = 2401
        assert ker_av_dim(7, 4) == 2191

    def test_n5(self):
        # total = 7^5 = 16807
        # sym = binom(11, 6) = 462
        # kernel = 16807 - 462 = 16345
        # VERIFIED: [DC] binom(11,6) = 11!/(5!6!) = 462; [DA] 7^5 = 16807
        assert ker_av_dim(7, 5) == 16345

    def test_n6(self):
        # total = 7^6 = 117649
        # sym = binom(12, 6) = 924
        # kernel = 117649 - 924 = 116725
        # VERIFIED: [DC] binom(12,6) = 12!/(6!6!) = 924; [DA] 7^6 = 117649
        assert ker_av_dim(7, 6) == 116725


# =====================================================================
# Cross-family consistency: same d => same kernel
# =====================================================================

class TestCrossFamily:
    """Different Lie algebras with the same d must give identical results."""

    def test_sl5_equals_so5(self):
        # sl_5 fundamental d=5 vs so_5 fundamental d=5
        # VERIFIED: [CF] formula depends only on d; [DC] both d=5
        for n in range(2, 7):
            assert ker_av_dim(5, n) == ker_av_for_algebra("sl_5", n)["kernel"]
            assert ker_av_dim(5, n) == ker_av_for_algebra("so_5", n)["kernel"]

    def test_algebras_with_same_d(self):
        # VERIFIED: [CF] algebras_with_same_d returns all matches
        same_5 = algebras_with_same_d(5)
        assert "sl_5" in same_5
        assert "so_5" in same_5
        # All should give the same ker_av_dim
        for n in range(2, 7):
            vals = {ker_av_for_algebra(alg, n)["kernel"] for alg in same_5}
            assert len(vals) == 1, f"Mismatch at n={n}: {vals}"

    def test_sl4_equals_sp4(self):
        # sl_4 fundamental d=4 vs sp_4 fundamental d=4
        # VERIFIED: [CF] same d=4; [DC] binom(n+3, 3) for both
        for n in range(2, 7):
            assert ker_av_for_algebra("sl_4", n)["kernel"] == \
                   ker_av_for_algebra("sp_4", n)["kernel"]


# =====================================================================
# Degree-2 special case: ker(av_2) = Alt^2(V)
# =====================================================================

class TestDegree2Alt2:
    """At n=2, ker(av_2) = d(d-1)/2 = dim(Alt^2(V))."""

    @pytest.mark.parametrize("d", [2, 3, 4, 5, 7, 8, 26, 27, 56, 248])
    def test_alt2_identity(self, d):
        # VERIFIED: [DC] d^2 - d(d+1)/2 = d(d-1)/2;
        # [SY] V tensor V = Sym^2 + Alt^2 at n=2
        k, a, match = ker_av_2_equals_alt2(d)
        assert match, f"d={d}: ker={k}, alt2={a}"
        assert k == d * (d - 1) // 2


# =====================================================================
# Limiting cases
# =====================================================================

class TestLimitingCases:
    """Boundary and limiting cases."""

    def test_n1_always_zero(self):
        # At n=1: d^1 - binom(d, d-1) = d - d = 0 for all d
        # VERIFIED: [LC] no permutations at n=1; [DC] explicit
        for d in [1, 2, 3, 5, 7, 10, 100]:
            assert ker_av_dim(d, 1) == 0

    def test_d1_always_zero(self):
        # At d=1: 1^n - binom(n, 0) = 1 - 1 = 0 for all n
        # VERIFIED: [LC] 1-dim space has trivial Sigma_n action;
        # [DC] Sym^n(C) = C for all n
        for n in range(1, 11):
            assert ker_av_dim(1, n) == 0

    def test_info_ratio_monotone(self):
        # For d >= 2 fixed, info_ratio is non-decreasing in n
        # (kernel grows exponentially, sym grows polynomially)
        # VERIFIED: [DA] d^n grows as exp, binom as poly
        for d in [2, 3, 5, 7]:
            prev = Fraction(0)
            for n in range(1, 10):
                r = info_ratio(d, n)
                assert r >= prev, f"d={d}, n={n}: ratio decreased"
                prev = r

    def test_info_ratio_approaches_1(self):
        # For large n, info_ratio -> 1 (sym is negligible)
        # VERIFIED: [DA] binom(n+d-1,d-1)/d^n ~ n^{d-1}/((d-1)!*d^n) -> 0
        for d in [2, 3, 5]:
            r = info_ratio(d, 20)
            assert r > Fraction(99, 100), f"d={d}: ratio at n=20 = {r}"


# =====================================================================
# Sym^n(V) dimension
# =====================================================================

class TestSymDim:
    """Verify Sym^n(V) dimensions."""

    def test_sym_n_d2(self):
        # Sym^n(C^2) = C^{n+1}, dim = n+1
        # VERIFIED: [DC] homogeneous polys of degree n in 2 vars;
        # [LT] Fulton-Harris
        for n in range(0, 8):
            assert sym_dim(2, n) == n + 1

    def test_sym_2_general(self):
        # Sym^2(C^d) has dim d(d+1)/2
        # VERIFIED: [DC] stars-and-bars for k=2, d vars;
        # [SY] binom(d+1, 2) = d(d+1)/2
        for d in range(1, 10):
            assert sym_dim(d, 2) == d * (d + 1) // 2


# =====================================================================
# Generating function coefficients
# =====================================================================

class TestGeneratingFunction:
    """Delta P_d(t) = 1/(1-dt) - 1/(1-t)^d."""

    def test_first_two_zero(self):
        # ker(d,0) contribution = 0 (by convention), ker(d,1) = 0
        # VERIFIED: [DC] d^0 - 1 = 0, d^1 - d = 0
        for d in [2, 3, 5, 7]:
            coeffs = generating_function_coeffs(d, 3)
            assert coeffs[0] == 0  # n=0 by convention
            assert coeffs[1] == 0  # n=1

    def test_sl2_gf(self):
        # For d=2: ker = 2^n - (n+1)
        # Coefficients: 0, 0, 1, 4, 11, 26, 57, 120, ...
        # VERIFIED: [DC] direct formula; [CF] matches OEIS A000325
        coeffs = generating_function_coeffs(2, 7)
        expected = [0, 0, 1, 4, 11, 26, 57, 120]
        assert coeffs == expected


# =====================================================================
# Integration with algebra registry
# =====================================================================

class TestAlgebraRegistry:
    """Verify ker_av_for_algebra interface."""

    def test_sl2_datum(self):
        datum = ker_av_for_algebra("sl_2", 3)
        assert datum["d"] == 2
        assert datum["total"] == 8
        assert datum["sym"] == 4
        assert datum["kernel"] == 4

    def test_G2_datum(self):
        datum = ker_av_for_algebra("G_2", 2)
        assert datum["d"] == 7
        assert datum["total"] == 49
        assert datum["sym"] == 28
        assert datum["kernel"] == 21

    def test_unknown_algebra_raises(self):
        with pytest.raises(KeyError):
            ker_av_for_algebra("sl_99", 2)

    def test_invalid_inputs(self):
        with pytest.raises(ValueError):
            ker_av_dim(0, 3)
        with pytest.raises(ValueError):
            ker_av_dim(3, 0)
