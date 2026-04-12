"""Tests for averaging_kernel_dim_engine.

Cross-algebra averaging kernel dimensions and information ratios
for sl_2 (d=3), sl_3 (d=8), sl_4 (d=15) at arities 2,3,4,5.

Every hardcoded expected value has a VERIFIED comment citing 2+
independent sources (AP10/HZ-6):
  [DC] direct computation (binomial formula shown)
  [DA] dimensional analysis (d^n total verified)
  [SY] symmetry (Sigma_n coinvariant structure)
  [CF] cross-family consistency
  [LC] limiting case
"""

from fractions import Fraction

import pytest

from compute.lib.averaging_kernel_dim_engine import (
    LIE_ALGEBRA_DIMS,
    alt_dim,
    averaging_kernel_datum,
    coinvariant_dim,
    cross_algebra_table,
    info_ratio,
    info_ratio_growth_table,
    kernel_dim,
    surviving_ratio,
    sym_alt_decomposition,
    sym_alt_ratio,
    sym_dim,
    total_dim,
)


# =====================================================================
# sl_2 (d=3) at arities 2,3,4,5
# =====================================================================

class TestSl2:
    """sl_2: dim = 3, even parity."""

    def test_dim_g(self):
        # VERIFIED: [DC] 2^2 - 1 = 3; [LT] Humphreys Ch.1
        assert LIE_ALGEBRA_DIMS["sl_2"] == 3

    def test_arity2(self):
        # total = 3^2 = 9
        # coinv = binom(3+2-1, 2) = binom(4,2) = 6
        # kernel = 9 - 6 = 3
        # info_ratio = 3/9 = 1/3
        # VERIFIED: [DC] binom(4,2) = 4!/(2!2!) = 6; [DA] 3^2 = 9
        assert total_dim(3, 2) == 9
        assert coinvariant_dim(3, 2) == 6
        assert kernel_dim(3, 2) == 3
        assert info_ratio(3, 2) == Fraction(1, 3)
        assert surviving_ratio(3, 2) == Fraction(2, 3)

    def test_arity3(self):
        # total = 3^3 = 27
        # coinv = binom(3+3-1, 3) = binom(5,3) = 10
        # kernel = 27 - 10 = 17
        # info_ratio = 17/27
        # VERIFIED: [DC] binom(5,3) = 5!/(3!2!) = 10; [DA] 3^3 = 27
        assert total_dim(3, 3) == 27
        assert coinvariant_dim(3, 3) == 10
        assert kernel_dim(3, 3) == 17
        assert info_ratio(3, 3) == Fraction(17, 27)

    def test_arity4(self):
        # total = 3^4 = 81
        # coinv = binom(3+4-1, 4) = binom(6,4) = 15
        # kernel = 81 - 15 = 66
        # info_ratio = 66/81 = 22/27
        # VERIFIED: [DC] binom(6,4) = 6!/(4!2!) = 15; [DA] 3^4 = 81
        assert total_dim(3, 4) == 81
        assert coinvariant_dim(3, 4) == 15
        assert kernel_dim(3, 4) == 66
        assert info_ratio(3, 4) == Fraction(22, 27)

    def test_arity5(self):
        # total = 3^5 = 243
        # coinv = binom(3+5-1, 5) = binom(7,5) = 21
        # kernel = 243 - 21 = 222
        # info_ratio = 222/243 = 74/81
        # VERIFIED: [DC] binom(7,5) = 7!/(5!2!) = 21; [DA] 3^5 = 243
        assert total_dim(3, 5) == 243
        assert coinvariant_dim(3, 5) == 21
        assert kernel_dim(3, 5) == 222
        assert info_ratio(3, 5) == Fraction(74, 81)


# =====================================================================
# sl_3 (d=8) at arities 2,3,4,5
# =====================================================================

class TestSl3:
    """sl_3: dim = 8, even parity."""

    def test_dim_g(self):
        # VERIFIED: [DC] 3^2 - 1 = 8; [LT] Humphreys Ch.1
        assert LIE_ALGEBRA_DIMS["sl_3"] == 8

    def test_arity2(self):
        # total = 8^2 = 64
        # coinv = binom(8+2-1, 2) = binom(9,2) = 36
        # kernel = 64 - 36 = 28
        # info_ratio = 28/64 = 7/16
        # VERIFIED: [DC] binom(9,2) = 9*8/2 = 36; [DA] 8^2 = 64;
        # [CF] matches averaging_kernel_engine.py sl3 test
        assert total_dim(8, 2) == 64
        assert coinvariant_dim(8, 2) == 36
        assert kernel_dim(8, 2) == 28
        assert info_ratio(8, 2) == Fraction(7, 16)

    def test_arity3(self):
        # total = 8^3 = 512
        # coinv = binom(8+3-1, 3) = binom(10,3) = 120
        # kernel = 512 - 120 = 392
        # info_ratio = 392/512 = 49/64
        # VERIFIED: [DC] binom(10,3) = 10*9*8/(3*2*1) = 120; [DA] 8^3 = 512
        assert total_dim(8, 3) == 512
        assert coinvariant_dim(8, 3) == 120
        assert kernel_dim(8, 3) == 392
        assert info_ratio(8, 3) == Fraction(49, 64)

    def test_arity4(self):
        # total = 8^4 = 4096
        # coinv = binom(8+4-1, 4) = binom(11,4) = 330
        # kernel = 4096 - 330 = 3766
        # info_ratio = 3766/4096 = 1883/2048
        # VERIFIED: [DC] binom(11,4) = 11*10*9*8/(4*3*2*1) = 330; [DA] 8^4 = 4096
        assert total_dim(8, 4) == 4096
        assert coinvariant_dim(8, 4) == 330
        assert kernel_dim(8, 4) == 3766
        assert info_ratio(8, 4) == Fraction(1883, 2048)

    def test_arity5(self):
        # total = 8^5 = 32768
        # coinv = binom(8+5-1, 5) = binom(12,5) = 792
        # kernel = 32768 - 792 = 31976
        # info_ratio = 31976/32768 = 3997/4096
        # VERIFIED: [DC] binom(12,5) = 12*11*10*9*8/(5*4*3*2*1) = 792; [DA] 8^5 = 32768
        assert total_dim(8, 5) == 32768
        assert coinvariant_dim(8, 5) == 792
        assert kernel_dim(8, 5) == 31976
        assert info_ratio(8, 5) == Fraction(3997, 4096)


# =====================================================================
# sl_4 (d=15) at arities 2,3,4,5
# =====================================================================

class TestSl4:
    """sl_4: dim = 15, even parity."""

    def test_dim_g(self):
        # VERIFIED: [DC] 4^2 - 1 = 15; [LT] Humphreys Ch.1
        assert LIE_ALGEBRA_DIMS["sl_4"] == 15

    def test_arity2(self):
        # total = 15^2 = 225
        # coinv = binom(15+2-1, 2) = binom(16,2) = 120
        # kernel = 225 - 120 = 105
        # info_ratio = 105/225 = 7/15
        # VERIFIED: [DC] binom(16,2) = 16*15/2 = 120; [DA] 15^2 = 225
        assert total_dim(15, 2) == 225
        assert coinvariant_dim(15, 2) == 120
        assert kernel_dim(15, 2) == 105
        assert info_ratio(15, 2) == Fraction(7, 15)

    def test_arity3(self):
        # total = 15^3 = 3375
        # coinv = binom(15+3-1, 3) = binom(17,3) = 680
        # kernel = 3375 - 680 = 2695
        # info_ratio = 2695/3375 = 539/675
        # VERIFIED: [DC] binom(17,3) = 17*16*15/(3*2*1) = 680; [DA] 15^3 = 3375
        assert total_dim(15, 3) == 3375
        assert coinvariant_dim(15, 3) == 680
        assert kernel_dim(15, 3) == 2695
        assert info_ratio(15, 3) == Fraction(539, 675)

    def test_arity4(self):
        # total = 15^4 = 50625
        # coinv = binom(15+4-1, 4) = binom(18,4) = 3060
        # kernel = 50625 - 3060 = 47565
        # info_ratio = 47565/50625 = 3171/3375
        # VERIFIED: [DC] binom(18,4) = 18*17*16*15/(4*3*2*1) = 3060; [DA] 15^4 = 50625
        assert total_dim(15, 4) == 50625
        assert coinvariant_dim(15, 4) == 3060
        assert kernel_dim(15, 4) == 47565
        assert info_ratio(15, 4) == Fraction(3171, 3375)

    def test_arity5(self):
        # total = 15^5 = 759375
        # coinv = binom(15+5-1, 5) = binom(19,5) = 11628
        # kernel = 759375 - 11628 = 747747
        # info_ratio = 747747/759375 = 249249/253125
        # VERIFIED: [DC] binom(19,5) = 19*18*17*16*15/(5*4*3*2*1) = 11628;
        # [DA] 15^5 = 759375
        assert total_dim(15, 5) == 759375
        assert coinvariant_dim(15, 5) == 11628
        assert kernel_dim(15, 5) == 747747
        assert info_ratio(15, 5) == Fraction(249249, 253125)


# =====================================================================
# Arity-1 boundary: kernel = 0, no averaging at arity 1
# =====================================================================

class TestArity1Boundary:
    """At arity 1, av is the identity: kernel_dim = 0 for all algebras."""

    @pytest.mark.parametrize("alg", ["sl_2", "sl_3", "sl_4"])
    def test_arity1_kernel_zero(self, alg):
        d = LIE_ALGEBRA_DIMS[alg]
        # VERIFIED: [DC] binom(d+0, 1) = d; [LC] n=1 means no permutation
        assert kernel_dim(d, 1) == 0
        assert info_ratio(d, 1) == Fraction(0, 1)
        assert surviving_ratio(d, 1) == Fraction(1, 1)


# =====================================================================
# Information ratio bounds: strictly between 0 and 1 for d >= 2, n >= 2
# =====================================================================

class TestInfoRatioBounds:
    """info_ratio in (0, 1) for all d >= 2, n >= 2."""

    @pytest.mark.parametrize("alg", ["sl_2", "sl_3", "sl_4"])
    @pytest.mark.parametrize("n", [2, 3, 4, 5])
    def test_info_ratio_strictly_between_0_and_1(self, alg, n):
        d = LIE_ALGEBRA_DIMS[alg]
        ir = info_ratio(d, n)
        assert ir > 0, f"info_ratio should be > 0 for d={d}, n={n}"
        assert ir < 1, f"info_ratio should be < 1 for d={d}, n={n}"

    @pytest.mark.parametrize("alg", ["sl_2", "sl_3", "sl_4"])
    def test_kernel_nonneg_all_arities(self, alg):
        d = LIE_ALGEBRA_DIMS[alg]
        for n in range(1, 11):
            k = kernel_dim(d, n)
            assert k >= 0, f"kernel_dim < 0 for {alg} at n={n}: {k}"


# =====================================================================
# Monotonicity: info_ratio is non-decreasing in arity for d >= 2
# =====================================================================

class TestInfoRatioMonotone:
    """For d >= 2, info_ratio(d, n) is non-decreasing in n."""

    @pytest.mark.parametrize("alg", ["sl_2", "sl_3", "sl_4"])
    def test_monotone_nondecreasing(self, alg):
        d = LIE_ALGEBRA_DIMS[alg]
        prev = info_ratio(d, 1)
        for n in range(2, 11):
            curr = info_ratio(d, n)
            assert curr >= prev, (
                f"info_ratio decreased at n={n} for {alg}: "
                f"{float(prev):.6f} -> {float(curr):.6f}"
            )
            prev = curr


# =====================================================================
# Cross-algebra ordering: larger d -> larger info_ratio at same arity
# =====================================================================

class TestCrossAlgebraOrdering:
    """At fixed arity n >= 2, larger d gives larger info_ratio."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5])
    def test_sl2_lt_sl3_lt_sl4(self, n):
        # VERIFIED: [SY] larger d means Sym^n(V) is a smaller fraction of V^{otimes n}
        ir2 = info_ratio(LIE_ALGEBRA_DIMS["sl_2"], n)
        ir3 = info_ratio(LIE_ALGEBRA_DIMS["sl_3"], n)
        ir4 = info_ratio(LIE_ALGEBRA_DIMS["sl_4"], n)
        assert ir2 < ir3 < ir4, (
            f"Expected sl_2 < sl_3 < sl_4 info_ratio at n={n}: "
            f"{float(ir2):.6f}, {float(ir3):.6f}, {float(ir4):.6f}"
        )


# =====================================================================
# Arity-2 universal formula: info_ratio(d, 2) = (d-1)/(2d)
# =====================================================================

class TestArity2UniversalFormula:
    """At arity 2 (even parity):
    coinv = binom(d+1,2) = d(d+1)/2
    kernel = d^2 - d(d+1)/2 = d(d-1)/2
    info_ratio = (d-1)/(2d)

    VERIFIED: [DC] algebraic simplification; [CF] matches all three algebras.
    """

    @pytest.mark.parametrize("alg,d", [("sl_2", 3), ("sl_3", 8), ("sl_4", 15)])
    def test_arity2_formula(self, alg, d):
        expected_ir = Fraction(d - 1, 2 * d)
        assert info_ratio(d, 2) == expected_ir


# =====================================================================
# Sym/Alt decomposition
# =====================================================================

class TestSymAltDecomposition:
    """Sym/Alt decomposition for R-matrix analysis."""

    def test_sl2_arity2_sym_alt(self):
        # d=3, n=2: Sym^2 = binom(4,2) = 6, Alt^2 = binom(3,2) = 3
        # total = 9, mixed = 9 - 6 - 3 = 0
        # sym/alt = 6/3 = 2
        # VERIFIED: [DC] 3x3 matrices decompose as 6 sym + 3 alt = 9;
        # [SY] no mixed component at n=2 (Sigma_2 has only two irreps)
        dec = sym_alt_decomposition(3, 2)
        assert dec["sym_dim"] == 6
        assert dec["alt_dim"] == 3
        assert dec["mixed_dim"] == 0
        assert dec["sym_alt_ratio"] == Fraction(2, 1)

    def test_sl2_arity3_sym_alt(self):
        # d=3, n=3: Sym^3 = binom(5,3) = 10, Alt^3 = binom(3,3) = 1
        # total = 27, mixed = 27 - 10 - 1 = 16
        # sym/alt = 10/1 = 10
        # VERIFIED: [DC] binom(5,3)=10, binom(3,3)=1; [DA] 10+1+16=27
        dec = sym_alt_decomposition(3, 3)
        assert dec["sym_dim"] == 10
        assert dec["alt_dim"] == 1
        assert dec["mixed_dim"] == 16
        assert dec["sym_alt_ratio"] == Fraction(10, 1)

    def test_sl3_arity2_sym_alt(self):
        # d=8, n=2: Sym^2 = binom(9,2) = 36, Alt^2 = binom(8,2) = 28
        # total = 64, mixed = 64 - 36 - 28 = 0
        # sym/alt = 36/28 = 9/7
        # VERIFIED: [DC] binom(9,2)=36, binom(8,2)=28; [SY] n=2 has no mixed
        dec = sym_alt_decomposition(8, 2)
        assert dec["sym_dim"] == 36
        assert dec["alt_dim"] == 28
        assert dec["mixed_dim"] == 0
        assert dec["sym_alt_ratio"] == Fraction(9, 7)

    def test_sl4_arity2_sym_alt(self):
        # d=15, n=2: Sym^2 = binom(16,2) = 120, Alt^2 = binom(15,2) = 105
        # total = 225, mixed = 225 - 120 - 105 = 0
        # sym/alt = 120/105 = 8/7
        # VERIFIED: [DC] binom(16,2)=120, binom(15,2)=105; [SY] n=2 exhaustive
        dec = sym_alt_decomposition(15, 2)
        assert dec["sym_dim"] == 120
        assert dec["alt_dim"] == 105
        assert dec["mixed_dim"] == 0
        assert dec["sym_alt_ratio"] == Fraction(8, 7)

    def test_n2_mixed_always_zero(self):
        """At n=2, Sigma_2 has exactly two irreps (trivial + sign),
        so Sym^2 + Alt^2 = V^{otimes 2} and mixed = 0.

        VERIFIED: [SY] Maschke for Sigma_2; [DC] d^2 = d(d+1)/2 + d(d-1)/2.
        """
        for d in [3, 8, 15]:
            dec = sym_alt_decomposition(d, 2)
            assert dec["mixed_dim"] == 0

    def test_sym_alt_ratio_arity2(self):
        """At arity 2: sym/alt = (d+1)/(d-1).

        VERIFIED: [DC] binom(d+1,2)/binom(d,2) = d(d+1)/(d(d-1)) = (d+1)/(d-1).
        """
        for d in [3, 8, 15]:
            expected = Fraction(d + 1, d - 1)
            assert sym_alt_ratio(d, 2) == expected

    def test_alt_vanishes_beyond_d(self):
        """Alt^n(V) = 0 for n > d."""
        # sl_2 (d=3): Alt^4 = binom(3,4) = 0
        assert alt_dim(3, 4) == 0
        assert alt_dim(3, 5) == 0
        # sl_3 (d=8): Alt^9 = 0
        assert alt_dim(8, 9) == 0


# =====================================================================
# Cross-algebra table structure
# =====================================================================

class TestCrossAlgebraTable:
    """Tests for the cross_algebra_table function."""

    def test_default_table_length(self):
        rows = cross_algebra_table()
        # 3 algebras x 4 arities = 12 rows
        assert len(rows) == 12

    def test_custom_table(self):
        rows = cross_algebra_table(
            algebras=["sl_2", "sl_4"],
            arities=[2, 5],
        )
        assert len(rows) == 4

    def test_table_keys(self):
        rows = cross_algebra_table()
        expected_keys = {
            "lie_algebra", "dim_g", "arity", "total_dim",
            "coinvariant_dim", "kernel_dim", "info_ratio",
            "surviving_ratio", "parity",
        }
        for r in rows:
            assert set(r.keys()) == expected_keys


# =====================================================================
# Info ratio growth table
# =====================================================================

class TestInfoRatioGrowthTable:
    """Tests for info_ratio_growth_table."""

    def test_sl4_growth_table_length(self):
        rows = info_ratio_growth_table("sl_4", max_arity=8)
        assert len(rows) == 8

    def test_sl4_growth_approaches_1(self):
        """For d=15, info_ratio should approach 1 as n grows."""
        rows = info_ratio_growth_table("sl_4", max_arity=10)
        # At n=10, info_ratio should be > 0.99
        assert rows[-1]["info_ratio_float"] > 0.99

    def test_sl2_growth_approaches_1(self):
        """For d=3, info_ratio grows slower but still approaches 1."""
        rows = info_ratio_growth_table("sl_2", max_arity=20)
        # At n=20, should be very close to 1
        assert rows[-1]["info_ratio_float"] > 0.99


# =====================================================================
# averaging_kernel_datum function
# =====================================================================

class TestAveragingKernelDatum:
    """Tests for the per-algebra, per-arity datum function."""

    def test_sl4_arity3(self):
        datum = averaging_kernel_datum("sl_4", 3)
        assert datum["lie_algebra"] == "sl_4"
        assert datum["dim_g"] == 15
        assert datum["arity"] == 3
        assert datum["total_dim"] == 3375
        assert datum["coinvariant_dim"] == 680
        assert datum["kernel_dim"] == 2695

    def test_unknown_algebra_raises(self):
        with pytest.raises(KeyError):
            averaging_kernel_datum("sl_99", 2)


# =====================================================================
# Consistency with existing averaging_kernel_engine
# =====================================================================

class TestConsistencyWithExistingEngine:
    """Cross-check against the existing averaging_kernel_engine values.

    VERIFIED: [CF] existing engine test anchors at sl2 n=2,3,4.
    """

    def test_sl2_arity2_matches(self):
        # Existing engine: surviving ratio = 2/3
        assert surviving_ratio(3, 2) == Fraction(2, 3)

    def test_sl2_arity3_matches(self):
        # Existing engine: surviving ratio = 10/27
        assert surviving_ratio(3, 3) == Fraction(10, 27)

    def test_sl2_arity4_matches(self):
        # Existing engine: surviving ratio = 15/81 = 5/27
        assert surviving_ratio(3, 4) == Fraction(5, 27)

    def test_sl3_arity2_matches(self):
        # Existing engine: surviving = 36, total = 64, ratio = 36/64 = 9/16
        assert surviving_ratio(8, 2) == Fraction(9, 16)


# =====================================================================
# Hecke algebra / Schur-Weyl decomposition for V = C^2 (fundamental)
# =====================================================================
#
# This section computes ker(av_n) for the FUNDAMENTAL representation
# V = C^2 of sl_2, using the Hecke algebra H_n(q) at generic q.
#
# The decomposition uses Schur-Weyl duality:
#   V^{tensor n} = bigoplus_{j=0}^{floor(n/2)} S_{(n-j,j)} tensor V_{(n-j,j)}
#
# The trivial S_n-isotypic component is lambda = (n, 0):
#   dim = 1 * (n+1) = n+1 = dim Sym^n(C^2).
# ker(av_n) = 2^n - (n+1).
#
# This is DIFFERENT from the adjoint-representation computation in
# TestSl2 above (d=3, coinvariant = binom(n+2, n)).
# The fundamental computation is relevant to:
#   - The KZ local system on Conf_n^ord(C) with V^{tensor n} coefficients
#   - The standalone paper ordered_chiral_homology.tex
#   - The Yangian Y(sl_2) R-matrix / Hecke algebra analysis
#
# Verification paths:
#   [DC] direct binomial computation
#   [DC2] explicit Reynolds operator on (C^2)^{tensor n} (path C above)
#   [LT] Schur-Weyl duality / hook-length formula
#   [CF] consistency with standalone paper ker(av_2) = 1, ker(av_3) = 1
#        (the paper's ker(av_3) = Lambda^3(g) = C uses the ADJOINT g = C^3;
#         on the fundamental V = C^2, ker(av_3) = 4 is the full non-trivial
#         part, of which the associator occupies a 1-dim subspace)
# =====================================================================

from compute.lib.averaging_kernel_dim_engine import (
    hecke_kernel_dim_sl2_fund,
    hecke_kernel_decomposition_sl2_fund,
    hecke_kernel_table_sl2_fund,
    schur_weyl_decomposition_sl2,
    specht_dim_two_row,
    gl2_irrep_dim,
)


class TestHeckeKernelSl2Fund:
    """ker(av_n) for V = C^2 (fundamental of sl_2) via Hecke algebra."""

    def test_arity1_kernel_zero(self):
        # n=1: 2^1 = 2, coinv = 2, ker = 0
        # VERIFIED: [DC] 2 - 2 = 0; [SY] S_1 is trivial, no kernel
        assert hecke_kernel_dim_sl2_fund(1) == 0

    def test_arity2_kernel_1(self):
        # n=2: 2^2 = 4, coinv = 3 (Sym^2(C^2)), ker = 1 (Lambda^2(C^2))
        # VERIFIED: [DC] 4 - 3 = 1; [CF] standalone paper eq:yangian-ker-av2
        # gives ker(av_2) = Lambda^2(V) = C, dim 1
        assert hecke_kernel_dim_sl2_fund(2) == 1

    def test_arity3_kernel_4(self):
        # n=3: 2^3 = 8, coinv = 4 (Sym^3(C^2) = C^4), ker = 4
        # VERIFIED: [DC] 8 - 4 = 4;
        # [DC2] Reynolds operator rank computation gives rank 4;
        # [LT] Schur-Weyl: S_{(2,1)} tensor V_{(2,1)} = 2 x 2 = 4
        # NOTE: The standalone paper says ker(av_3) = Lambda^3(g) = C^1
        # for g = sl_2 (adjoint, dim 3). This is the ADJOINT computation.
        # On the fundamental V = C^2, ker(av_3) = 4, of which the
        # Drinfeld associator occupies 1 dimension (the Lambda^3(g)
        # subspace within the multiplicity space of the KZ system).
        assert hecke_kernel_dim_sl2_fund(3) == 4

    def test_arity4_kernel_11(self):
        # n=4: 2^4 = 16, coinv = 5 (Sym^4(C^2)), ker = 11
        # VERIFIED: [DC] 16 - 5 = 11;
        # [DC2] explicit Reynolds operator on (C^2)^{tensor 4} gives rank 5;
        # [LT] Schur-Weyl decomposition:
        #   S_{(3,1)} tensor V_{(3,1)} = 3 x 3 = 9
        #   S_{(2,2)} tensor V_{(2,2)} = 2 x 1 = 2
        #   Total kernel = 9 + 2 = 11
        assert hecke_kernel_dim_sl2_fund(4) == 11

    def test_arity5_kernel_26(self):
        # n=5: 2^5 = 32, coinv = 6 (Sym^5(C^2)), ker = 26
        # VERIFIED: [DC] 32 - 6 = 26;
        # [DC2] explicit Reynolds operator on (C^2)^{tensor 5} gives rank 6;
        # [LT] Schur-Weyl decomposition:
        #   S_{(4,1)} tensor V_{(4,1)} = 4 x 4 = 16
        #   S_{(3,2)} tensor V_{(3,2)} = 5 x 2 = 10
        #   Total kernel = 16 + 10 = 26
        assert hecke_kernel_dim_sl2_fund(5) == 26

    def test_arity6_kernel_57(self):
        # n=6: 2^6 = 64, coinv = 7 (Sym^6(C^2)), ker = 57
        # VERIFIED: [DC] 64 - 7 = 57;
        # [DC2] explicit Reynolds operator on (C^2)^{tensor 6} gives rank 7;
        # [LT] Schur-Weyl decomposition:
        #   S_{(5,1)} tensor V_{(5,1)} = 5 x 5 = 25
        #   S_{(4,2)} tensor V_{(4,2)} = 9 x 3 = 27
        #   S_{(3,3)} tensor V_{(3,3)} = 5 x 1 = 5
        #   Total kernel = 25 + 27 + 5 = 57
        assert hecke_kernel_dim_sl2_fund(6) == 57

    def test_general_formula(self):
        """ker(av_n) = 2^n - (n + 1) for all n = 1..10."""
        for n in range(1, 11):
            expected = 2**n - (n + 1)
            assert hecke_kernel_dim_sl2_fund(n) == expected


class TestSchurWeylDecompositionSl2:
    """Schur-Weyl decomposition of (C^2)^{tensor n}."""

    def test_total_dimension(self):
        """Sum of dim(S_lambda) * dim(V_lambda) = 2^n."""
        for n in range(1, 11):
            decomp = schur_weyl_decomposition_sl2(n)
            total = sum(row["product"] for row in decomp)
            assert total == 2**n

    def test_trivial_isotypic(self):
        """Trivial isotypic component has dim = n + 1 = dim Sym^n(C^2)."""
        for n in range(1, 11):
            decomp = schur_weyl_decomposition_sl2(n)
            trivial = [r for r in decomp if r["is_trivial"]]
            assert len(trivial) == 1
            assert trivial[0]["product"] == n + 1
            assert trivial[0]["specht_dim"] == 1
            assert trivial[0]["gl2_dim"] == n + 1

    def test_number_of_components(self):
        """Number of Young diagrams = floor(n/2) + 1."""
        for n in range(1, 11):
            decomp = schur_weyl_decomposition_sl2(n)
            assert len(decomp) == n // 2 + 1

    def test_arity4_decomposition(self):
        # VERIFIED: [DC] binom(4,1)-binom(4,0) = 3; dim V_{(3,1)} = 3
        # [DC] binom(4,2)-binom(4,1) = 2; dim V_{(2,2)} = 1
        decomp = schur_weyl_decomposition_sl2(4)
        assert decomp[0]["partition"] == (4, 0)
        assert decomp[0]["product"] == 5  # trivial: 1 * 5
        assert decomp[1]["partition"] == (3, 1)
        assert decomp[1]["specht_dim"] == 3
        assert decomp[1]["gl2_dim"] == 3
        assert decomp[1]["product"] == 9
        assert decomp[2]["partition"] == (2, 2)
        assert decomp[2]["specht_dim"] == 2
        assert decomp[2]["gl2_dim"] == 1
        assert decomp[2]["product"] == 2

    def test_arity6_decomposition(self):
        # VERIFIED: [DC] direct binomial computation for each component
        decomp = schur_weyl_decomposition_sl2(6)
        assert len(decomp) == 4  # j = 0, 1, 2, 3
        # j=0: (6,0), trivial, 1 * 7 = 7
        assert decomp[0]["product"] == 7
        # j=1: (5,1), dim_S = binom(6,1) - binom(6,0) = 5, dim_V = 5, prod = 25
        assert decomp[1]["specht_dim"] == 5
        assert decomp[1]["gl2_dim"] == 5
        assert decomp[1]["product"] == 25
        # j=2: (4,2), dim_S = binom(6,2) - binom(6,1) = 15-6 = 9, dim_V = 3, prod = 27
        assert decomp[2]["specht_dim"] == 9
        assert decomp[2]["gl2_dim"] == 3
        assert decomp[2]["product"] == 27
        # j=3: (3,3), dim_S = binom(6,3) - binom(6,2) = 20-15 = 5, dim_V = 1, prod = 5
        assert decomp[3]["specht_dim"] == 5
        assert decomp[3]["gl2_dim"] == 1
        assert decomp[3]["product"] == 5


class TestHeckeKernelDecomposition:
    """Decomposition of ker(av_n) by S_n-isotypic component."""

    def test_arity4_parts(self):
        parts = hecke_kernel_decomposition_sl2_fund(4)
        assert len(parts) == 2
        assert sum(p["contribution"] for p in parts) == 11

    def test_arity5_parts(self):
        parts = hecke_kernel_decomposition_sl2_fund(5)
        assert len(parts) == 2
        assert sum(p["contribution"] for p in parts) == 26

    def test_arity6_parts(self):
        parts = hecke_kernel_decomposition_sl2_fund(6)
        assert len(parts) == 3
        assert sum(p["contribution"] for p in parts) == 57

    def test_parts_sum_to_kernel(self):
        """Sum of non-trivial contributions = hecke_kernel_dim for all n."""
        for n in range(1, 11):
            parts = hecke_kernel_decomposition_sl2_fund(n)
            total = sum(p["contribution"] for p in parts)
            assert total == hecke_kernel_dim_sl2_fund(n)


class TestSpechtDimTwoRow:
    """Specht module dimensions for two-row partitions."""

    def test_trivial_rep(self):
        """S_{(n, 0)} is trivial: dim = 1."""
        for n in range(1, 11):
            assert specht_dim_two_row(n, 0) == 1

    def test_sign_rep_at_n2(self):
        """S_{(1,1)} is the sign representation of S_2: dim = 1."""
        # VERIFIED: [DC] binom(2,1) - binom(2,0) = 2 - 1 = 1
        assert specht_dim_two_row(2, 1) == 1

    def test_standard_rep_at_n3(self):
        """S_{(2,1)} is the standard rep of S_3: dim = 2."""
        # VERIFIED: [DC] binom(3,1) - binom(3,0) = 3 - 1 = 2
        assert specht_dim_two_row(3, 1) == 2

    def test_known_values(self):
        # VERIFIED: [DC] ballot numbers = binom(n,j) - binom(n,j-1)
        assert specht_dim_two_row(4, 1) == 3   # binom(4,1) - binom(4,0) = 3
        assert specht_dim_two_row(4, 2) == 2   # binom(4,2) - binom(4,1) = 2
        assert specht_dim_two_row(5, 1) == 4   # binom(5,1) - binom(5,0) = 4
        assert specht_dim_two_row(5, 2) == 5   # binom(5,2) - binom(5,1) = 5
        assert specht_dim_two_row(6, 1) == 5   # binom(6,1) - binom(6,0) = 5
        assert specht_dim_two_row(6, 2) == 9   # binom(6,2) - binom(6,1) = 9
        assert specht_dim_two_row(6, 3) == 5   # binom(6,3) - binom(6,2) = 5

    def test_out_of_range(self):
        """specht_dim = 0 for j > floor(n/2) or j < 0."""
        assert specht_dim_two_row(4, 3) == 0
        assert specht_dim_two_row(5, 3) == 0
        assert specht_dim_two_row(3, -1) == 0


class TestGl2IrrepDim:
    """GL_2 irrep dimensions."""

    def test_symmetric_power(self):
        """V_{(n, 0)} = Sym^n(C^2): dim = n + 1."""
        for n in range(1, 11):
            assert gl2_irrep_dim(n, 0) == n + 1

    def test_determinant(self):
        """V_{(1, 1)} = det: dim = 1."""
        assert gl2_irrep_dim(2, 1) == 1

    def test_known_values(self):
        assert gl2_irrep_dim(4, 1) == 3  # spin 3/2, dim 3
        assert gl2_irrep_dim(4, 2) == 1  # spin 0, dim 1
        assert gl2_irrep_dim(6, 1) == 5  # spin 2, dim 5
        assert gl2_irrep_dim(6, 2) == 3  # spin 1, dim 3
        assert gl2_irrep_dim(6, 3) == 1  # spin 0, dim 1


class TestHeckeKernelTable:
    """Table of kernel dimensions for V = C^2."""

    def test_table_length(self):
        rows = hecke_kernel_table_sl2_fund(max_arity=8)
        assert len(rows) == 8

    def test_table_values(self):
        rows = hecke_kernel_table_sl2_fund(max_arity=6)
        expected_ker = [0, 1, 4, 11, 26, 57]
        for row, ek in zip(rows, expected_ker):
            assert row["kernel_dim"] == ek

    def test_info_ratio_nondecreasing(self):
        """Information ratio is nondecreasing for n >= 1."""
        rows = hecke_kernel_table_sl2_fund(max_arity=10)
        for i in range(1, len(rows)):
            assert rows[i]["info_ratio"] >= rows[i - 1]["info_ratio"]

    def test_info_ratio_approaches_1(self):
        """For large n, almost all of V^{tensor n} lies in ker(av)."""
        rows = hecke_kernel_table_sl2_fund(max_arity=20)
        assert float(rows[-1]["info_ratio"]) > 0.99


class TestHeckeVsAdjointComparison:
    """Compare fundamental (V=C^2) vs adjoint (g=C^3) kernel dimensions.

    These are DIFFERENT computations on DIFFERENT spaces.
    The adjoint computes ker(av) on g^{tensor n} where g = sl_2 (dim 3).
    The fundamental computes ker(av) on V^{tensor n} where V = C^2.
    """

    def test_adjoint_larger_at_arity2(self):
        # Adjoint (d=3): ker = 3^2 - binom(4,2) = 9 - 6 = 3
        # Fundamental (d=2): ker = 2^2 - 3 = 1
        # VERIFIED: [DC] different spaces, adjoint strictly larger
        assert kernel_dim(3, 2) == 3
        assert hecke_kernel_dim_sl2_fund(2) == 1

    def test_adjoint_larger_at_arity3(self):
        # Adjoint: 27 - 10 = 17
        # Fundamental: 8 - 4 = 4
        assert kernel_dim(3, 3) == 17
        assert hecke_kernel_dim_sl2_fund(3) == 4

    def test_adjoint_larger_at_arity4(self):
        # Adjoint: 81 - 15 = 66
        # Fundamental: 16 - 5 = 11
        assert kernel_dim(3, 4) == 66
        assert hecke_kernel_dim_sl2_fund(4) == 11
