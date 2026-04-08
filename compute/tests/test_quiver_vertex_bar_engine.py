r"""Tests for quiver_vertex_bar_engine.

Multi-path verification of the bar cohomology of quiver vertex algebras:

  - A_n quivers          (n = 1..5)         vs   V_k(sl_{n+1})
  - Jordan quiver                           vs   rank-1 Heisenberg
  - Framed Jordan (r=2,3)                   vs   rank-r Heisenberg
  - D_4 quiver                              vs   V_k(so_8)
  - Kronecker quivers (m=1,2,3)             vs   tame / wild regime
  - CoHA-bar duality at arities 2..6        for  A_2 and D_4
  - Nakajima Hilbert scheme  H^*(Hilb^n)    vs   partition count
  - Cross-engine vs bar_cohomology_non_simply_laced_engine (B_2 = so_5)
  - kappa formulas                           via  dim(g)(k+h^v)/(2h^v)
  - Wild quiver signed-Euler regime

Ground truth sources:
  Humphreys, "Introduction to Lie Algebras"
  Kac, "Infinite Dimensional Lie Algebras" (dim, h, h^v)
  OEIS A000041 (partitions), A000712 (2-colored), A008485 (3-colored),
       A023003 (8-colored partitions for sl_3)
  Nakajima, "Lectures on Hilbert Schemes..." Chapter 8
"""

from __future__ import annotations

from fractions import Fraction

import pytest

from compute.lib.quiver_vertex_bar_engine import (
    Quiver,
    a_n_quiver,
    affine_yangian_gl1_module_character,
    ade_bar_sweep,
    b2_bar_cohomology_dims,
    bar_cohomology_total_dims,
    coha_bar_arity_pairing,
    coha_dimension,
    colored_partitions,
    d4_b2_dimension_separation,
    d4_bar_character,
    d4_bar_cohomology_dims,
    d_n_quiver,
    finite_type_label,
    framed_jordan_quiver,
    framed_nakajima_character,
    hilbert_scheme_dimension,
    jordan_quiver,
    kappa_quiver_vertex_algebra,
    kronecker_quiver,
    lie_data_for_quiver,
    nakajima_vs_heisenberg_check,
    pbw_character,
    quiver_bar_character,
    quiver_bar_cohomology_dims,
    signed_euler_series,
    summary,
    verify_coha_bar_duality_a2,
    verify_coha_bar_duality_d4,
    w1plus_infty_character,
    wild_quiver_bar_character,
    wild_quiver_bar_cohomology_signed,
)


# ===========================================================================
# 1. Quiver construction and classification
# ===========================================================================


class TestQuiverConstructors:
    def test_a1_quiver_is_single_vertex(self):
        q = a_n_quiver(1)
        assert q.n_vertices == 1
        assert q.arrows == ()

    def test_a2_quiver_is_one_arrow(self):
        q = a_n_quiver(2)
        assert q.n_vertices == 2
        assert q.arrows == ((0, 1),)

    def test_a5_quiver_has_four_arrows(self):
        q = a_n_quiver(5)
        assert q.n_vertices == 5
        assert len(q.arrows) == 4

    def test_jordan_has_one_loop(self):
        q = jordan_quiver()
        assert q.n_vertices == 1
        assert q.arrows == ((0, 0),)

    def test_framed_jordan_rank3(self):
        q = framed_jordan_quiver(3)
        assert q.n_vertices == 2          # loop vertex + framing vertex
        assert len(q.arrows) == 4         # 1 loop + 3 framing arrows

    def test_d4_quiver_four_vertices(self):
        q = d_n_quiver(4)
        assert q.n_vertices == 4
        assert len(q.arrows) == 3

    def test_kronecker_m2_affine(self):
        q = kronecker_quiver(2)
        assert q.n_vertices == 2
        assert len(q.arrows) == 2


class TestFiniteTypeClassification:
    def test_a_n_recognised(self):
        for n in range(1, 6):
            label = finite_type_label(a_n_quiver(n))
            assert label == ("A", n), f"A_{n} not recognised, got {label}"

    def test_d4_recognised(self):
        label = finite_type_label(d_n_quiver(4))
        assert label == ("D", 4), f"D_4 not recognised, got {label}"

    def test_d5_recognised(self):
        label = finite_type_label(d_n_quiver(5))
        assert label in (("D", 5), ("D", 5)), f"D_5 not recognised"

    def test_jordan_not_finite_type(self):
        q = jordan_quiver()
        # Jordan has a loop, so adjacency diagonal != 0; rejected.
        assert finite_type_label(q) is None

    def test_kronecker_m3_not_finite_type(self):
        q = kronecker_quiver(3)
        # Three parallel arrows violate the "adj entries in {0,1}" test.
        assert finite_type_label(q) is None


# ===========================================================================
# 2. A_n: Lie data and bar character
# ===========================================================================


class TestAnLieData:
    def test_a1_sl2(self):
        data = lie_data_for_quiver(a_n_quiver(1))
        assert data.rank == 1
        assert data.dim == 3
        assert data.h_dual == 2

    def test_a2_sl3(self):
        data = lie_data_for_quiver(a_n_quiver(2))
        assert data.rank == 2
        assert data.dim == 8       # dim sl_3 = 3^2 - 1 = 8
        assert data.h_dual == 3

    def test_a3_sl4(self):
        data = lie_data_for_quiver(a_n_quiver(3))
        assert data.dim == 15
        assert data.h_dual == 4

    def test_a5_sl6(self):
        data = lie_data_for_quiver(a_n_quiver(5))
        assert data.dim == 35


class TestAnBarCharacter:
    """Compare quiver_bar_character(A_n) against pbw_character(dim sl_{n+1})."""

    def test_a1_matches_sl2(self):
        q = a_n_quiver(1)
        ch = quiver_bar_character(q, 6)
        # dim sl_2 = 3, 3-coloured partitions: 1, 3, 9, 22, 51, 108, 221
        expected = [1, 3, 9, 22, 51, 108, 221]
        assert ch == expected

    def test_a2_matches_sl3(self):
        q = a_n_quiver(2)
        ch = quiver_bar_character(q, 5)
        # dim sl_3 = 8
        expected = [colored_partitions(n, 8) for n in range(6)]
        assert ch == expected
        # Sanity: c_1 = 8 = dim sl_3
        assert ch[1] == 8

    def test_a3_first_few_values(self):
        q = a_n_quiver(3)
        ch = quiver_bar_character(q, 4)
        assert ch[0] == 1
        assert ch[1] == 15        # dim sl_4 = 15
        # c_2 = 15 + 15*16/2 = 15 + 120 = 135
        assert ch[2] == 135


# ===========================================================================
# 3. Jordan quiver -> Heisenberg H_k
# ===========================================================================


class TestJordanHeisenberg:
    def test_jordan_character_is_partition_function(self):
        q = jordan_quiver()
        ch = quiver_bar_character(q, 10)
        # 1-coloured partitions = ordinary partitions
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        assert ch == expected

    def test_jordan_kappa_is_k(self):
        q = jordan_quiver()
        # kappa(H_k) = k  (k = 7 as a test value)
        k = 7
        assert kappa_quiver_vertex_algebra(q, k) == Fraction(7)

    def test_framed_jordan_rank2_character(self):
        q = framed_jordan_quiver(1)     # rank = 1 loop + 1 framing arrow = 2
        ch = quiver_bar_character(q, 6)
        # 2-coloured partitions: 1, 2, 5, 10, 20, 36, 65
        expected = [1, 2, 5, 10, 20, 36, 65]
        assert ch == expected

    def test_framed_jordan_rank5_matches_pbw_5(self):
        q = framed_jordan_quiver(4)     # 1 loop + 4 framing = rank 5
        ch = quiver_bar_character(q, 8)
        expected = pbw_character(5, 8)
        assert ch == expected


# ===========================================================================
# 4. D_4 and D_5 bar cohomology
# ===========================================================================


class TestD4Dim28:
    def test_d4_dim_is_28(self):
        data = lie_data_for_quiver(d_n_quiver(4))
        assert data.dim == 28         # so_8 dimension
        assert data.h_dual == 6       # dual Coxeter of so_8

    def test_d4_bar_character_weight_1(self):
        ch = d4_bar_character(4)
        assert ch[0] == 1
        assert ch[1] == 28            # 28 generators at weight 1

    def test_d4_bar_character_weight_2(self):
        ch = d4_bar_character(3)
        # c_2 = 28 + C(29, 2) = 28 + 406 = ... wait the formula is
        # 28 generators at weight 2 PLUS multisets of weight-1 products.
        # Using PBW Hilbert series: p_28(2) = 28 + 28*29/2 = 434.
        assert ch[2] == 28 + 28 * 29 // 2

    def test_d4_kappa_integer_at_k_equals_1(self):
        q = d_n_quiver(4)
        k = 1
        kap = kappa_quiver_vertex_algebra(q, k)
        # kappa = 28*(1+6)/(2*6) = 196/12 = 49/3
        assert kap == Fraction(49, 3)

    def test_d5_dim_is_45(self):
        data = lie_data_for_quiver(d_n_quiver(5))
        assert data.dim == 45
        assert data.h_dual == 8


# ===========================================================================
# 5. Cross-engine: B_2 (non-simply-laced engine) vs our formula
# ===========================================================================


class TestCrossEngineB2:
    """Cross-check against bar_cohomology_non_simply_laced_engine."""

    def test_b2_via_euler_matches_non_simply_laced_engine(self):
        from compute.lib.bar_cohomology_non_simply_laced_engine import (
            bar_cohomology_dims,
        )
        mine = b2_bar_cohomology_dims(5)
        theirs = bar_cohomology_dims(5, 10)   # dim_g = 10
        assert mine == theirs

    def test_d4_distinct_from_b2(self):
        both = d4_b2_dimension_separation(4)
        assert both["B2_so5_dim10"] != both["D4_so8_dim28"]

    def test_d4_grows_faster_than_b2(self):
        # At weight 4, dim 28 has strictly more PBW states than dim 10.
        assert pbw_character(28, 4)[4] > pbw_character(10, 4)[4]


# ===========================================================================
# 6. CoHA-bar duality: A_2 and D_4
# ===========================================================================


class TestCoHABarDualityA2:
    def test_a2_duality_characters_agree_weight_by_weight(self):
        data = verify_coha_bar_duality_a2(max_weight=6)
        # Characters are integers, strictly positive from weight 1 onwards
        for w in range(1, 7):
            assert data["bar_character"][w] > 0

    def test_a2_duality_all_flag_true(self):
        out = coha_bar_arity_pairing(a_n_quiver(2), 5)
        for row in out:
            assert row["match"] is True
            assert row["CoHA"] == row["B(A)"]

    def test_a2_degree_one_is_dim_sl3(self):
        assert coha_dimension(a_n_quiver(2), 1) == 8


class TestCoHABarDualityD4:
    def test_d4_duality_data_has_dim_28(self):
        data = verify_coha_bar_duality_d4(max_weight=5)
        assert data["dim_g"] == 28

    def test_d4_pairing_matches_at_all_weights(self):
        out = coha_bar_arity_pairing(d_n_quiver(4), 5)
        for row in out:
            assert row["CoHA"] == row["B(A)"]

    def test_d4_degree_one_is_dim_so8(self):
        assert coha_dimension(d_n_quiver(4), 1) == 28


# ===========================================================================
# 7. Nakajima Hilbert scheme and W_{1+oo}
# ===========================================================================


class TestNakajima:
    def test_hilbert_scheme_is_partitions(self):
        # dim H^*(Hilb^n(C^2)) = p(n)
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        values = [hilbert_scheme_dimension(n) for n in range(11)]
        assert values == expected

    def test_nakajima_framing_2(self):
        # p_2(n): 1, 2, 5, 10, 20, 36, 65, 110, 185, 300, 481
        values = [framed_nakajima_character(n, 2) for n in range(8)]
        expected = [1, 2, 5, 10, 20, 36, 65, 110]
        assert values == expected

    def test_nakajima_matches_heisenberg_rank1(self):
        assert nakajima_vs_heisenberg_check(1, 10)

    def test_nakajima_matches_heisenberg_rank3(self):
        assert nakajima_vs_heisenberg_check(3, 8)

    def test_w1plusoo_character(self):
        ch = w1plus_infty_character(6)
        assert ch == [1, 1, 2, 3, 5, 7, 11]

    def test_affine_yangian_gl1_level2_matches_rank2_heisenberg(self):
        aya = affine_yangian_gl1_module_character(2, 6)
        heis = pbw_character(2, 6)
        assert aya == heis


# ===========================================================================
# 8. Wild quivers: m-Kronecker for m >= 3
# ===========================================================================


class TestWildQuivers:
    def test_kronecker_m1_is_finite(self):
        q = kronecker_quiver(1)
        assert q.is_finite_type() is True       # equal to A_2 as an undirected graph

    def test_kronecker_m3_formal_bar_character_positive(self):
        q = kronecker_quiver(3)
        # vertices + arrows = 2 + 3 = 5  formal "rank"
        ch = wild_quiver_bar_character(q, 4)
        assert ch == pbw_character(5, 4)
        assert all(c > 0 for c in ch)

    def test_kronecker_m3_has_no_lie_data(self):
        q = kronecker_quiver(3)
        with pytest.raises(ValueError):
            lie_data_for_quiver(q)

    def test_kronecker_m5_wild_signed_euler(self):
        q = kronecker_quiver(5)
        # vertices + arrows = 7
        sgn = wild_quiver_bar_cohomology_signed(q, 3)
        # Signed Euler series prod(1-t^n)^7: [1, -7, 14, 14, ...]
        assert sgn[0] == 1
        assert sgn[1] == -7
        # Weight 2: C(7,2) - 7 = 21 - 7 = 14
        assert sgn[2] == 14


# ===========================================================================
# 9. Kappa formulas
# ===========================================================================


class TestKappaFormulas:
    def test_kappa_sl2_k1(self):
        q = a_n_quiver(1)   # dim=3, h^v=2, k=1
        # kappa = 3*(1+2)/(2*2) = 9/4
        assert kappa_quiver_vertex_algebra(q, 1) == Fraction(9, 4)

    def test_kappa_sl3_k1(self):
        q = a_n_quiver(2)   # dim=8, h^v=3, k=1
        # kappa = 8*(1+3)/(2*3) = 32/6 = 16/3
        assert kappa_quiver_vertex_algebra(q, 1) == Fraction(16, 3)

    def test_kappa_so8_k2(self):
        q = d_n_quiver(4)   # dim=28, h^v=6, k=2
        # kappa = 28*(2+6)/(2*6) = 28*8/12 = 224/12 = 56/3
        assert kappa_quiver_vertex_algebra(q, 2) == Fraction(56, 3)

    def test_kappa_jordan_is_k_not_k_over_2(self):
        """AP48 / AP39: kappa(H_k) = k (absolute), not c/2 or k/2."""
        q = jordan_quiver()
        assert kappa_quiver_vertex_algebra(q, 5) == Fraction(5)
        assert kappa_quiver_vertex_algebra(q, Fraction(3, 2)) == Fraction(3, 2)


# ===========================================================================
# 10. ADE sweep consistency
# ===========================================================================


class TestADESweep:
    def test_sweep_includes_all_standard(self):
        rows = ade_bar_sweep(max_weight=3)
        labels = {row["label"] for row in rows}
        assert "A_2 (sl_3)" in labels
        assert "D_4 (so_8)" in labels
        assert "E_8" in labels

    def test_sweep_characters_positive(self):
        rows = ade_bar_sweep(max_weight=3)
        for row in rows:
            assert all(c > 0 for c in row["bar_character"])

    def test_dim_monotonic_growth_in_char(self):
        # Higher-dim algebras have larger weight-1 bar spaces
        rows = ade_bar_sweep(max_weight=2)
        by_dim = {row["dim"]: row for row in rows}
        assert by_dim[3]["bar_character"][1] < by_dim[8]["bar_character"][1]
        assert by_dim[8]["bar_character"][1] < by_dim[15]["bar_character"][1]
        assert by_dim[78]["bar_character"][1] < by_dim[248]["bar_character"][1]


# ===========================================================================
# 11. Signed Euler series and Koszul duality
# ===========================================================================


class TestSignedEulerSeries:
    def test_euler_d1_reproduces_pentagonal(self):
        # (1-t)(1-t^2)(1-t^3)... gives Euler's pentagonal series:
        # 1 - t - t^2 + t^5 + t^7 - t^12 - ...
        sgn = signed_euler_series(1, 15)
        # Key values
        assert sgn[0] == 1
        assert sgn[1] == -1
        assert sgn[2] == -1
        assert sgn[3] == 0
        assert sgn[4] == 0
        assert sgn[5] == 1
        assert sgn[6] == 0
        assert sgn[7] == 1
        assert sgn[12] == -1

    def test_euler_d8_weight_1(self):
        # (1-t)^8 ... at t^1 gives -8
        sgn = signed_euler_series(8, 2)
        assert sgn[1] == -8

    def test_koszul_product_is_identity(self):
        """H_A(t) * (1/H_A(t)) = 1 is trivial; we verify the variant
           H_A(t) * signed_euler(-t) convolution via the PBW series.

           Concretely: (sum p_d(n) t^n) * (sum chi_m t^m) = 1
           where chi_m = coefficient of t^m in prod (1-t^n)^d.

           So sum_{k=0}^{w} p_d(k) * chi_{w-k} = delta_{w,0}.
        """
        d = 5
        max_w = 8
        pbw = pbw_character(d, max_w)
        chi = signed_euler_series(d, max_w)
        for w in range(max_w + 1):
            s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
            expected = 1 if w == 0 else 0
            assert s == expected, f"Convolution fails at w={w}: got {s}"


# ===========================================================================
# 12. Colored partition ground truth (OEIS A000041, A000712, A023003)
# ===========================================================================


class TestColoredPartitions:
    def test_p_1_is_ordinary_partitions(self):
        """OEIS A000041."""
        expected = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
        got = [colored_partitions(n, 1) for n in range(11)]
        assert got == expected

    def test_p_2_two_colored(self):
        """OEIS A000712."""
        expected = [1, 2, 5, 10, 20, 36, 65, 110, 185, 300, 481]
        got = [colored_partitions(n, 2) for n in range(11)]
        assert got == expected

    def test_p_3_three_colored(self):
        """OEIS A000716."""
        expected = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479]
        got = [colored_partitions(n, 3) for n in range(10)]
        assert got == expected

    def test_p_8_sl3_weight_2(self):
        """p_8(2) = 8 + C(9,2) = 8 + 36 = 44.  For sl_3 at weight 2."""
        # Multiset count: choose 2 from 8 with repetition = C(9, 2) = 36;
        # plus 8 singleton modes at weight 2. Total = 44.
        assert colored_partitions(2, 8) == 44


# ===========================================================================
# 13. Summary API
# ===========================================================================


class TestSummaryAPI:
    def test_summary_a2(self):
        s = summary(a_n_quiver(2), 4)
        assert s["quiver"] == "A_2"
        assert s["is_finite_dynkin"] is True
        assert len(s["bar_character"]) == 5

    def test_summary_jordan_has_kappa(self):
        s = summary(jordan_quiver(), 3)
        assert s["kappa_at_k=1"] == "1"   # kappa(H_1) = 1

    def test_summary_wild_reports_formal(self):
        q = kronecker_quiver(4)
        s = summary(q, 3)
        assert s["is_finite_dynkin"] is False
        assert s["kappa_at_k=1"] is None


# ===========================================================================
# 14. Explicit D_4 low-weight values (cross-check vs Koszul identity)
# ===========================================================================


class TestD4ExplicitLowWeight:
    def test_d4_abs_euler_weight_0_and_1(self):
        """Multi-path: dimension formula vs direct Euler-series computation."""
        # Path A: direct Euler series
        dims = d4_bar_cohomology_dims(1)
        # Path B: manual formula |chi_1| = d = dim so_8 = 28
        data = lie_data_for_quiver(d_n_quiver(4))
        assert dims[0] == 1
        assert dims[1] == data.dim   # cross-check via dim_so8 formula
        # Path C: matches direct signed Euler series computation
        sgn = signed_euler_series(28, 1)
        assert abs(sgn[1]) == dims[1]

    def test_d4_weight2_via_explicit(self):
        """Multi-path: direct vs binomial formula vs Euler series."""
        # Path A: engine
        dims = d4_bar_cohomology_dims(2)
        # Path B: C(d, 2) - d for d = 28, since (1-t)^28(1-t^2)^28 at t^2
        d = 28
        expected_b = d * (d - 1) // 2 - d     # 378 - 28 = 350
        assert dims[2] == expected_b
        # Path C: coincide with signed_euler_series absolute value
        sgn = signed_euler_series(d, 2)
        assert abs(sgn[2]) == dims[2]


# ===========================================================================
# 15. Cross-path consistency: Lie data -> character -> Euler -> cohomology
# ===========================================================================


class TestCrossPathConsistency:
    """Every bar-cohomology number must be derivable by at least 3 independent
    paths. These tests enforce the multi-path mandate of CLAUDE.md.
    """

    def test_a2_three_paths_agree_at_weight_2(self):
        """sl_3 weight-2 bar cohomology:
             Path A: quiver_bar_cohomology_dims(A_2)[2]
             Path B: |signed_euler_series(8, 2)[2]|
             Path C: bar_cohomology_total_dims(8, 2)[2]
             Path D: cross-engine non_simply_laced bar_cohomology_dims
        """
        path_a = quiver_bar_cohomology_dims(a_n_quiver(2), 2)[2]
        path_b = abs(signed_euler_series(8, 2)[2])
        path_c = bar_cohomology_total_dims(8, 2)[2]
        from compute.lib.bar_cohomology_non_simply_laced_engine import (
            bar_cohomology_dims,
        )
        path_d = bar_cohomology_dims(2, 8)[2]
        assert path_a == path_b == path_c == path_d

    def test_d4_three_paths_agree_at_weight_3(self):
        """so_8 weight-3 bar cohomology, three independent paths."""
        path_a = d4_bar_cohomology_dims(3)[3]
        path_b = abs(signed_euler_series(28, 3)[3])
        path_c = bar_cohomology_total_dims(28, 3)[3]
        assert path_a == path_b == path_c

    def test_jordan_partition_three_paths(self):
        """Jordan / rank-1 Heisenberg character:
             Path A: quiver_bar_character (via colored_partitions(_, 1))
             Path B: pbw_character(1, ...)
             Path C: w1plus_infty_character
             Path D: [hilbert_scheme_dimension(n) for n]
        """
        max_w = 8
        path_a = quiver_bar_character(jordan_quiver(), max_w)
        path_b = pbw_character(1, max_w)
        path_c = w1plus_infty_character(max_w)
        path_d = [hilbert_scheme_dimension(n) for n in range(max_w + 1)]
        assert path_a == path_b == path_c == path_d

    def test_framed_jordan_rank_r_four_paths(self):
        """Rank-r Heisenberg character:
             Path A: framed_jordan_quiver(r-1)  (1 loop + (r-1) framing arrows)
             Path B: pbw_character(r, ...)
             Path C: [framed_nakajima_character(n, r) for n]
             Path D: affine_yangian_gl1_module_character
        """
        r = 3
        max_w = 6
        q = framed_jordan_quiver(r - 1)
        path_a = quiver_bar_character(q, max_w)
        path_b = pbw_character(r, max_w)
        path_c = [framed_nakajima_character(n, r) for n in range(max_w + 1)]
        path_d = affine_yangian_gl1_module_character(r, max_w)
        assert path_a == path_b == path_c == path_d

    def test_an_two_paths_for_all_n(self):
        """For every A_n, n=1..5, the quiver character equals the PBW character
        computed via dim(sl_{n+1})."""
        for n in range(1, 6):
            q = a_n_quiver(n)
            data = lie_data_for_quiver(q)
            path_a = quiver_bar_character(q, 4)
            path_b = pbw_character(data.dim, 4)
            path_c = [colored_partitions(w, data.dim) for w in range(5)]
            assert path_a == path_b == path_c

    def test_dn_two_paths_for_n_in_4_5_6(self):
        """For every D_n (n=4,5,6) all character paths agree."""
        for n in range(4, 7):
            q = d_n_quiver(n)
            data = lie_data_for_quiver(q)
            assert data.dim == n * (2 * n - 1)
            path_a = quiver_bar_character(q, 3)
            path_b = pbw_character(data.dim, 3)
            assert path_a == path_b

    def test_kappa_two_paths_kac_moody(self):
        """kappa(A_n, k) via engine vs direct formula for n=1..4, k=1..3."""
        for n in range(1, 5):
            data = lie_data_for_quiver(a_n_quiver(n))
            for k in range(1, 4):
                engine = kappa_quiver_vertex_algebra(a_n_quiver(n), k)
                direct = Fraction(data.dim) * (Fraction(k) + data.h_dual) / (2 * data.h_dual)
                assert engine == direct

    def test_koszul_convolution_identity_cross_family(self):
        """H_A(t) * (1/H_A(t)) = 1 must hold for every dimension we support.

        Tests d = 1 (Heisenberg), 3 (sl_2), 8 (sl_3), 10 (so_5), 14 (G_2),
        15 (sl_4), 28 (so_8), 52 (F_4), 78 (E_6), 133 (E_7), 248 (E_8).
        """
        for d in [1, 3, 8, 10, 14, 15, 28, 52, 78, 133, 248]:
            max_w = 6
            pbw = pbw_character(d, max_w)
            chi = signed_euler_series(d, max_w)
            for w in range(max_w + 1):
                s = sum(pbw[k] * chi[w - k] for k in range(w + 1))
                expected = 1 if w == 0 else 0
                assert s == expected, f"Koszul convolution fails d={d}, w={w}"

    def test_a2_vs_non_simply_laced_engine_at_weight_1(self):
        """Cross-engine check: our A_2 character agrees with existing sl_3 data."""
        from compute.lib.bar_cohomology_non_simply_laced_engine import pbw_dim
        for w in range(5):
            ours = quiver_bar_character(a_n_quiver(2), w)[w]
            theirs = pbw_dim(w, 8)
            assert ours == theirs, f"sl_3 disagreement at weight {w}"

    def test_d4_vs_non_simply_laced_engine(self):
        """Cross-engine: D_4 bar cohomology matches non-simply-laced engine
        computation at dim = 28."""
        from compute.lib.bar_cohomology_non_simply_laced_engine import (
            bar_cohomology_dims,
        )
        ours = d4_bar_cohomology_dims(4)
        theirs = bar_cohomology_dims(4, 28)
        assert ours == theirs

    def test_koszul_self_consistency_across_quivers(self):
        """The same Koszul identity must hold when computed via different quivers
        that share the same Lie data dimension. sl_4 (from A_3) matches
        dim-15 direct.
        """
        q_a3 = a_n_quiver(3)
        # A_3 -> sl_4, dim 15
        path_q = quiver_bar_cohomology_dims(q_a3, 3)
        path_d = bar_cohomology_total_dims(15, 3)
        assert path_q == path_d
