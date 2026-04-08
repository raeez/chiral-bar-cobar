"""Tests for bar_loop_group_engine: loop-group CE cohomology and Garland-Lepowsky.

Multi-path verification of the claim:
    "H*(B(V_k(g))) depends only on dim(g)".

Tested separately for Euler series (TRUE) and bigraded dimensions (FALSE).
"""

from __future__ import annotations

import pytest

from compute.lib.bar_loop_group_engine import (
    abelian_bracket,
    bar_bidegree_table,
    bar_euler_from_bidegrees,
    bar_total_dims,
    bar_cohomology_comparison_table,
    bott_pontryagin_generators,
    bott_pontryagin_poincare_series,
    ce_euler_series,
    dim_only_falsification,
    garland_lepowsky_sl2,
    garland_lepowsky_total_dim_sl2,
    heisenberg3_bracket,
    pbw_hilbert_series,
    sl2_bracket,
    sl2_garland_lepowsky_verification,
    sl3_bracket,
    so4_bracket,
)
from compute.lib.bar_cohomology_dimensions import CECurrentAlgebra


# ============================================================================
# Group 1: Euler series depends only on dim(g) — the CORRECT dim-only claim
# ============================================================================


class TestEulerSeriesDimOnly:
    """The signed Euler characteristic prod (1-t^n)^d depends only on d."""

    def test_euler_d1_weights_0_to_10(self):
        """d=1 Euler series: [1,-1,-1,0,0,1,0,1,0,0,0]."""
        coeffs = ce_euler_series(10, 1)
        assert coeffs == (1, -1, -1, 0, 0, 1, 0, 1, 0, 0, 0)

    def test_euler_d3_sl2_dim(self):
        """d=3 (sl_2 dim) Euler series matches prod(1-t^n)^3."""
        coeffs = ce_euler_series(10, 3)
        assert coeffs == (1, -3, 0, 5, 0, 0, -7, 0, 0, 0, 9)

    def test_euler_d8_sl3_dim(self):
        """d=8 (sl_3 dim) Euler series leading coefficients."""
        coeffs = ce_euler_series(5, 8)
        # prod(1-t^n)^8 = 1 - 8t + 20 t^2 + 0 t^3 - 70 t^4 + 64 t^5 + ...
        assert coeffs[0] == 1
        assert coeffs[1] == -8
        assert coeffs[2] == 20
        assert coeffs[3] == 0
        assert coeffs[4] == -70
        assert coeffs[5] == 64

    def test_euler_series_caching(self):
        """Euler series is pure (cacheable); same inputs give same output."""
        a = ce_euler_series(8, 3)
        b = ce_euler_series(8, 3)
        assert a == b

    def test_euler_series_length(self):
        """Euler series has length max_weight + 1."""
        coeffs = ce_euler_series(7, 5)
        assert len(coeffs) == 8

    def test_euler_constant_term_is_one(self):
        """Constant term of prod (1-t^n)^d is 1 for all d."""
        for d in [1, 2, 3, 5, 8, 14, 52]:
            coeffs = ce_euler_series(5, d)
            assert coeffs[0] == 1

    def test_euler_first_coefficient_is_minus_d(self):
        """Coefficient of t^1 in prod (1-t^n)^d equals -d."""
        for d in [1, 2, 3, 5, 8]:
            coeffs = ce_euler_series(3, d)
            assert coeffs[1] == -d


# ============================================================================
# Group 2: PBW Hilbert series
# ============================================================================


class TestPBWHilbert:
    """H_{U(g_-)}(t) = prod (1-t^n)^{-d} is the PBW Hilbert series."""

    def test_pbw_d1_partition_numbers(self):
        """For d=1, PBW coefficients are partition numbers p(n).

        Wait: U(g_-) for abelian rank 1 is the symmetric algebra
        on one generator at each mode, which is the partition algebra.
        Coefficient at weight n is p(n).
        """
        coeffs = pbw_hilbert_series(10, 1)
        # p(0)=1, p(1)=1, p(2)=2, p(3)=3, p(4)=5, p(5)=7, p(6)=11, p(7)=15, p(8)=22, p(9)=30, p(10)=42
        assert coeffs == (1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42)

    def test_pbw_d3_matches_known_product(self):
        """For d=3, PBW = prod (1-t^n)^{-3}, check first few coefficients."""
        coeffs = pbw_hilbert_series(5, 3)
        # prod (1-t^n)^{-3} = 1 + 3t + 9t^2 + 22t^3 + ...
        assert coeffs[0] == 1
        assert coeffs[1] == 3
        assert coeffs[2] == 9
        # verify: expand 1/(1-t)^3 * 1/(1-t^2)^3 * 1/(1-t^3)^3 * ...
        # coef of t^2: C(2+2,2) + 3*0 = 6 from 1/(1-t)^3 alone is 6, plus
        # contribution from (1-t^2)^{-3} = 1 + 3t^2 + ... giving 3.
        # Total at t^2: 6 + 3 = 9. Correct.

    def test_pbw_euler_inverse_relation(self):
        """prod (1-t^n)^d * prod (1-t^n)^{-d} = 1."""
        for d in [1, 2, 3, 5]:
            max_w = 6
            euler = ce_euler_series(max_w, d)
            pbw = pbw_hilbert_series(max_w, d)
            # Convolution should give 1, 0, 0, 0, ...
            product = [0] * (max_w + 1)
            for i in range(max_w + 1):
                for j in range(max_w + 1 - i):
                    product[i + j] += euler[i] * pbw[j]
            assert product[0] == 1
            for k in range(1, max_w + 1):
                assert product[k] == 0, \
                    f"d={d}, k={k}: product[k]={product[k]} should be 0"


# ============================================================================
# Group 3: Garland-Lepowsky formula for sl_2
# ============================================================================


class TestGarlandLepowskyS12:
    """H^p(g_-, k) for sl_2 is concentrated at (p, p(p+1)/2) with dim 2p+1."""

    def test_garland_lepowsky_table_diagonal(self):
        """The explicit Garland-Lepowsky table gives (p, p(p+1)/2) -> 2p+1."""
        table = garland_lepowsky_sl2(max_degree=5)
        assert table[(0, 0)] == 1
        assert table[(1, 1)] == 3
        assert table[(2, 3)] == 5
        assert table[(3, 6)] == 7
        assert table[(4, 10)] == 9
        assert table[(5, 15)] == 11

    def test_garland_lepowsky_total_dim(self):
        """Total dim at triangular weight = 2p+1."""
        assert garland_lepowsky_total_dim_sl2(0) == 1
        assert garland_lepowsky_total_dim_sl2(1) == 3
        assert garland_lepowsky_total_dim_sl2(3) == 5
        assert garland_lepowsky_total_dim_sl2(6) == 7
        assert garland_lepowsky_total_dim_sl2(10) == 9

    def test_garland_lepowsky_non_triangular_vanishes(self):
        """At non-triangular weights, total dim is 0."""
        for w in [2, 4, 5, 7, 8, 9, 11, 12, 13, 14]:
            assert garland_lepowsky_total_dim_sl2(w) == 0

    def test_garland_lepowsky_matches_ce_computation(self):
        """Predicted values match direct CE cohomology computation."""
        result = sl2_garland_lepowsky_verification(max_weight=15)
        assert result["all_checks_pass"] is True
        assert result["off_diagonal_nonzero_count"] == 0
        # At least 5 diagonal checks (p=1..5)
        assert len(result["diagonal_checks"]) >= 5
        for c in result["diagonal_checks"]:
            assert c["match"] is True

    def test_sl2_off_diagonal_zero(self):
        """sl_2: direct CE computation gives zero off the Garland-Lepowsky diagonal."""
        br = sl2_bracket()
        ce = CECurrentAlgebra(3, br, max_weight=10)
        for w in range(1, 11):
            for p in range(0, w + 1):
                if p == 0:
                    continue
                w_tri = p * (p + 1) // 2
                if w == w_tri:
                    continue
                dim = int(ce.cohomology_at_weight(p, w))
                assert dim == 0, \
                    f"sl_2 has nonzero H^{p}_{w} = {dim} at non-diagonal"

    def test_sl2_diagonal_matches_2p_plus_1(self):
        """dim H^p(g_-, k)_{p(p+1)/2} = 2p+1 for sl_2 at p = 1, 2, 3, 4."""
        br = sl2_bracket()
        ce = CECurrentAlgebra(3, br, max_weight=10)
        for p in range(1, 5):
            w = p * (p + 1) // 2
            dim = int(ce.cohomology_at_weight(p, w))
            assert dim == 2 * p + 1


# ============================================================================
# Group 4: Falsification — same dim_g, different bar cohomology
# ============================================================================


class TestDimOnlyFalsification:
    """Different Lie algebras at the same dim_g have different bar cohomology."""

    def test_dim3_sl2_bar_total_dims(self):
        """sl_2 total bar dims at weights 1..6: [3, 0, 5, 0, 0, 7]."""
        totals = bar_total_dims(3, sl2_bracket(), max_weight=6)
        assert totals == [3, 0, 5, 0, 0, 7]

    def test_dim3_abelian_bar_total_dims(self):
        """abelian^3 total bar dims at weights 1..6 are larger than sl_2."""
        totals = bar_total_dims(3, abelian_bracket(3), max_weight=6)
        # Precomputed: [3, 6, 13, 24, 42, 73]
        assert totals == [3, 6, 13, 24, 42, 73]

    def test_dim3_nilp_heis_bar_total_dims(self):
        """3-dim Heisenberg Lie algebra total bar dims."""
        totals = bar_total_dims(3, heisenberg3_bracket(), max_weight=6)
        # Precomputed: [3, 4, 9, 16, 24, 39]
        assert totals == [3, 4, 9, 16, 24, 39]

    def test_dim3_falsification_totals_differ(self):
        """At dim_g = 3, three algebras give three different totals."""
        s = bar_total_dims(3, sl2_bracket(), max_weight=6)
        a = bar_total_dims(3, abelian_bracket(3), max_weight=6)
        n = bar_total_dims(3, heisenberg3_bracket(), max_weight=6)
        assert s != a
        assert s != n
        assert a != n

    def test_dim3_euler_series_all_agree(self):
        """All three dim-3 algebras have the same Euler series."""
        pred = ce_euler_series(6, 3)
        for br in [sl2_bracket(), abelian_bracket(3), heisenberg3_bracket()]:
            euler = bar_euler_from_bidegrees(3, br, max_weight=6)
            for w in range(1, 7):
                assert euler[w - 1] == pred[w]

    def test_dim_only_report(self):
        """The falsification report has the expected verdict."""
        report = dim_only_falsification(max_weight=6)
        v = report["verdict"]
        assert v["all_euler_equal"] is True
        assert v["totals_differ_across_algebras"] is True
        assert v["falsifies_dim_only_claim_for_totals"] is True
        assert v["confirms_dim_only_claim_for_euler"] is True

    def test_dim8_sl3_vs_abelian(self):
        """sl_3 vs abelian^8 have same Euler but different totals."""
        s = bar_total_dims(8, sl3_bracket(), max_weight=4)
        a = bar_total_dims(8, abelian_bracket(8), max_weight=4)
        # sl_3 totals: [8, 20, 0, 63]
        # abelian^8 totals: large
        assert s != a
        assert s == [8, 20, 0, 63]

        # But Euler matches
        pred = ce_euler_series(4, 8)
        es = bar_euler_from_bidegrees(8, sl3_bracket(), max_weight=4)
        ea = bar_euler_from_bidegrees(8, abelian_bracket(8), max_weight=4)
        for w in range(1, 5):
            assert es[w - 1] == pred[w]
            assert ea[w - 1] == pred[w]


# ============================================================================
# Group 5: sl_3 bidegree structure
# ============================================================================


class TestSl3Bidegrees:
    """sl_3 has its own concentration pattern (different from sl_2)."""

    def test_sl3_nonzero_bidegrees_up_to_w4(self):
        """sl_3 bar cohomology is concentrated at specific (p, w)."""
        table = bar_bidegree_table(8, sl3_bracket(), max_weight=4)
        # Computed nonzero: (1,1)->8, (2,2)->20, (3,4)->63
        assert table[(1, 1)] == 8
        assert table[(2, 2)] == 20
        assert table[(3, 4)] == 63
        # Nothing else up to w=4
        for key in table:
            assert key in [(1, 1), (2, 2), (3, 4)]

    def test_sl3_h1_equals_dim_g(self):
        """dim H^1(g_-)_1 = dim g = 8 for sl_3."""
        table = bar_bidegree_table(8, sl3_bracket(), max_weight=3)
        assert table[(1, 1)] == 8

    def test_sl3_vs_sl2_different_concentrations(self):
        """sl_2 and sl_3 have different concentration patterns."""
        sl2_table = bar_bidegree_table(3, sl2_bracket(), max_weight=3)
        sl3_table = bar_bidegree_table(8, sl3_bracket(), max_weight=3)
        # sl_2: (1,1)->3, (2,3)->5
        # sl_3: (1,1)->8, (2,2)->20
        # Different non-trivial bidegrees: (2,3) for sl_2, (2,2) for sl_3
        assert sl2_table.get((2, 3)) == 5
        assert sl3_table.get((2, 2)) == 20
        assert sl2_table.get((2, 2), 0) == 0  # sl_2 has 0 at (2,2)
        assert sl3_table.get((2, 3), 0) == 0  # sl_3 has 0 at (2,3)


# ============================================================================
# Group 6: Bott Pontryagin comparison
# ============================================================================


class TestBottPontryagin:
    """Bott's polynomial structure for H*(Omega G; Q)."""

    def test_su2_single_generator(self):
        """H*(Omega SU(2); Q) = Q[x_2], single generator at degree 2."""
        gens = bott_pontryagin_generators("A", 1)
        assert gens == [2]

    def test_su3_two_generators(self):
        """H*(Omega SU(3); Q) = Q[x_2, x_4]."""
        gens = bott_pontryagin_generators("A", 2)
        assert gens == [2, 4]

    def test_sp2_generators(self):
        """H*(Omega Sp(2); Q) = Q[x_2, x_6]."""
        gens = bott_pontryagin_generators("C", 2)
        assert gens == [2, 6]

    def test_g2_generators(self):
        """H*(Omega G_2; Q) generators at degrees 2, 10."""
        gens = bott_pontryagin_generators("G", 2)
        assert gens == [2, 10]

    def test_f4_generators(self):
        """H*(Omega F_4; Q) generators at degrees 2, 10, 14, 22."""
        gens = bott_pontryagin_generators("F", 4)
        assert gens == [2, 10, 14, 22]

    def test_e8_generators(self):
        """H*(Omega E_8; Q) generators from E_8 exponents."""
        gens = bott_pontryagin_generators("E", 8)
        # Exponents of E_8: 1, 7, 11, 13, 17, 19, 23, 29
        assert gens == [2, 14, 22, 26, 34, 38, 46, 58]

    def test_su2_poincare_periodic(self):
        """H*(Omega SU(2); Q) has 1-dim in every even degree."""
        ps = bott_pontryagin_poincare_series("A", 1, 10)
        # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        for i, v in enumerate(ps):
            expected = 1 if i % 2 == 0 else 0
            assert v == expected

    def test_su3_poincare_series_t8(self):
        """H*(Omega SU(3); Q) Poincare series coefficient at t^8."""
        ps = bott_pontryagin_poincare_series("A", 2, 8)
        # prod 1/(1-t^2)(1-t^4): at t^8 we have partitions of 8 with parts in {2,4}
        # (2,2,2,2), (2,2,4), (4,4) - three.
        assert ps[8] == 3

    def test_bott_topological_vs_conformal_grading_different(self):
        """Bott's topological grading differs from bar complex conformal weight.

        For sl_2: Bott gives H^{2k}(Omega SU(2)) = 1 for all k >= 0.
        Bar complex gives dim H^p_{p(p+1)/2} = 2p+1 (conformal weight grading).
        These are different gradings encoding the same loop Lie algebra data.
        """
        bott = bott_pontryagin_poincare_series("A", 1, 15)
        # Bott in topological degree: 1 at t^0, t^2, t^4, ... (always 1)
        assert bott[0] == 1
        assert bott[14] == 1
        assert bott[15] == 0  # odd degrees vanish

        # Bar in conformal grading: sl_2 totals at weights 1..15
        bar = bar_total_dims(3, sl2_bracket(), max_weight=15)
        # [3, 0, 5, 0, 0, 7, 0, 0, 0, 9, 0, 0, 0, 0, 11]
        assert bar[0] == 3     # weight 1
        assert bar[2] == 5     # weight 3
        assert bar[5] == 7     # weight 6
        assert bar[9] == 9     # weight 10
        assert bar[14] == 11   # weight 15

        # Different sequences; Bott is 1-periodic, bar is triangular-spaced.


# ============================================================================
# Group 7: Comparison table and aggregate
# ============================================================================


class TestComparisonTable:
    """Cross-dim comparison."""

    def test_comparison_table_dim3_has_three_entries(self):
        """At dim=3, the table has sl_2, abelian, nilp_Heis_3."""
        t = bar_cohomology_comparison_table([3], max_weight=4)
        algs = t[3]["algebras"]
        assert "sl_2" in algs
        assert "abelian" in algs
        assert "nilp_Heis_3" in algs

    def test_comparison_table_dim8_has_sl3(self):
        """At dim=8, the table includes sl_3."""
        t = bar_cohomology_comparison_table([8], max_weight=3)
        algs = t[8]["algebras"]
        assert "sl_3" in algs
        assert algs["sl_3"] == [8, 20, 0]

    def test_euler_prediction_matches_in_comparison_table(self):
        """The comparison table includes the Euler prediction."""
        t = bar_cohomology_comparison_table([3], max_weight=6)
        pred = t[3]["euler_prediction"]
        # prod (1-t^n)^3 at weights 1..6: -3, 0, 5, 0, 0, -7
        assert pred == [-3, 0, 5, 0, 0, -7]


# ============================================================================
# Group 8: Cross-checks with heisenberg formula and chiral Heisenberg
# ============================================================================


class TestChiralHeisenbergDistinction:
    """The chiral Heisenberg vertex algebra is NOT the loop CE of abelian rank 1.

    The chiral Heisenberg H_k has OPE J(z)J(w) ~ k/(z-w)^2 with NO simple
    pole. Its bar complex is CURVED (m_0 = k) and its bar cohomology
    sequence is [1,1,1,2,3,5,7,11,...] (Heisenberg partition formula).

    The loop CE of the abelian rank-1 Lie algebra has a bracket that is
    ZERO, but its cohomology is NOT the same: the chiral curvature is
    invisible to the CE-of-loop computation.
    """

    def test_abelian_rank1_loop_ce_differs_from_chiral_heisenberg(self):
        """Abelian rank-1 loop CE ≠ chiral Heisenberg bar cohomology.

        Abelian rank-1 loop CE totals: [1, 1, 2, 2, 3, 4, 5, 6]
        Chiral Heisenberg bar totals: [1, 1, 1, 2, 3, 5, 7, 11]
        """
        from compute.lib.bar_cohomology_dimensions import (
            heisenberg_bar_cohomology_formula,
        )
        chiral = [heisenberg_bar_cohomology_formula(w) for w in range(1, 9)]
        loop_ce = bar_total_dims(1, abelian_bracket(1), max_weight=8)
        assert chiral != loop_ce
        # Chiral has partition-like growth
        assert chiral[-1] == 11  # p(6) = 11
        # Loop CE is smaller
        assert loop_ce[-1] < chiral[-1]


# ============================================================================
# Group 9: Broader landscape checks
# ============================================================================


class TestBroaderLandscape:
    """Euler series behaviour for several family dimensions."""

    def test_euler_matches_prediction_for_all_tested_algebras(self):
        """Direct CE Euler computation matches prod(1-t^n)^d for every tested
        bracket."""
        test_cases = [
            (3, sl2_bracket(), 6),
            (3, abelian_bracket(3), 6),
            (3, heisenberg3_bracket(), 6),
            (6, so4_bracket(), 4),
            (6, abelian_bracket(6), 4),
            (8, sl3_bracket(), 4),
            (8, abelian_bracket(8), 4),
        ]
        for d, br, max_w in test_cases:
            pred = ce_euler_series(max_w, d)
            actual = bar_euler_from_bidegrees(d, br, max_w)
            for w in range(1, max_w + 1):
                assert actual[w - 1] == pred[w], \
                    f"Mismatch at d={d}, w={w}: pred={pred[w]} actual={actual[w-1]}"

    def test_so4_splits_as_sl2_plus_sl2(self):
        """so_4 = sl_2 x sl_2; total dims should relate by a Kunneth."""
        # H*(g x g') = H*(g) tensor H*(g')
        # Specifically: Euler char (so_4) = Euler char (sl_2)^2 as series.
        pred6 = ce_euler_series(6, 6)
        pred3 = ce_euler_series(6, 3)
        # Compute (pred3 * pred3)[w] = sum_i pred3[i] pred3[w-i]
        conv = [0] * 7
        for i in range(7):
            for j in range(7 - i):
                conv[i + j] += pred3[i] * pred3[j]
        for w in range(7):
            assert conv[w] == pred6[w], \
                f"Kunneth fails at w={w}: conv={conv[w]} pred6={pred6[w]}"

    def test_bar_cohomology_h1_equals_dim_g(self):
        """H^1(g_-, k)_1 = dim(g) for any Lie algebra (abelianization)."""
        for d, br in [
            (3, sl2_bracket()),
            (3, abelian_bracket(3)),
            (6, so4_bracket()),
            (8, sl3_bracket()),
        ]:
            table = bar_bidegree_table(d, br, max_weight=2)
            assert table[(1, 1)] == d

    def test_bar_cohomology_h0_vanishes(self):
        """H^0(g_-, k)_w = 0 for w >= 1 (no constant 0-cochains at positive weight)."""
        ce = CECurrentAlgebra(3, sl2_bracket(), max_weight=5)
        for w in range(1, 6):
            assert int(ce.cohomology_at_weight(0, w)) == 0


# ============================================================================
# Group 10: Central claim verification (the direct answer)
# ============================================================================


class TestCentralClaim:
    """Direct tests of the central claim 'bar cohomology depends only on dim(g)'."""

    def test_claim_false_at_bidegree_level(self):
        """The claim FAILS for individual bidegrees (p, w).

        At dim_g = 3, dim H^2_3 differs across algebras:
        sl_2 -> 5, abelian^3 -> 9, nilp Heis_3 -> 7.
        """
        dims = {}
        for name, br in [
            ("sl_2", sl2_bracket()),
            ("abelian", abelian_bracket(3)),
            ("nilp_heis", heisenberg3_bracket()),
        ]:
            ce = CECurrentAlgebra(3, br, max_weight=3)
            dims[name] = int(ce.cohomology_at_weight(2, 3))

        # All three different
        assert dims["sl_2"] == 5
        assert dims["abelian"] == 9
        assert dims["nilp_heis"] == 7
        # not equal
        assert len({dims["sl_2"], dims["abelian"], dims["nilp_heis"]}) == 3

    def test_claim_false_for_total_dim_per_weight(self):
        """The claim FAILS even for total dim per weight at dim_g = 3.

        sl_2 has zeros at non-triangular weights; abelian never vanishes.
        """
        s = bar_total_dims(3, sl2_bracket(), 6)
        a = bar_total_dims(3, abelian_bracket(3), 6)
        assert s != a
        # sl_2 has zero at weight 2; abelian has 6
        assert s[1] == 0
        assert a[1] == 6

    def test_claim_true_for_euler_series(self):
        """The claim HOLDS for signed Euler series."""
        for d in [1, 2, 3, 5, 8]:
            pred = ce_euler_series(5, d)
            brs = [abelian_bracket(d)]
            if d == 3:
                brs.append(sl2_bracket())
                brs.append(heisenberg3_bracket())
            if d == 6:
                brs.append(so4_bracket())
            if d == 8:
                brs.append(sl3_bracket())
            for br in brs:
                actual = bar_euler_from_bidegrees(d, br, 5)
                for w in range(1, 6):
                    assert actual[w - 1] == pred[w]

    def test_claim_accidentally_true_for_sl2_totals(self):
        """For sl_2, the total dim per weight EQUALS |Euler coefficient|.

        This is because Garland-Lepowsky concentrates the cohomology onto
        a diagonal with one bidegree per weight, so the signed Euler sum
        has no cancellation and equals the total dim in absolute value.
        """
        pred = ce_euler_series(10, 3)  # sl_2 has dim 3
        totals = bar_total_dims(3, sl2_bracket(), 10)
        for w in range(1, 11):
            assert totals[w - 1] == abs(pred[w])

    def test_claim_fails_accidentally_for_abelian_totals(self):
        """For abelian^3, the total dim per weight is LARGER than |Euler|.

        The signed Euler sum has cancellation from multiple bidegrees,
        so |Euler| < total. This breaks the accidental sl_2 identity.
        """
        pred = ce_euler_series(6, 3)
        totals = bar_total_dims(3, abelian_bracket(3), 6)
        # At weight 2: Euler = 0, total = 6 > 0
        assert pred[2] == 0
        assert totals[1] == 6
        # At weight 3: Euler = 5, total = 13 > 5
        assert pred[3] == 5
        assert totals[2] == 13


# ============================================================================
# Group 11: Stress tests at higher weight
# ============================================================================


class TestHigherWeightStress:
    """Push the Garland-Lepowsky prediction to larger weights."""

    def test_sl2_gl_at_weight_21_p6(self):
        """For sl_2: dim H^6(g_-)_{21} should be 13 = 2*6 + 1."""
        ce = CECurrentAlgebra(3, sl2_bracket(), max_weight=21)
        dim = int(ce.cohomology_at_weight(6, 21))
        assert dim == 13

    def test_sl2_total_dim_triangular_vs_non(self):
        """Total bar dim is nonzero only at triangular weights for sl_2."""
        totals = bar_total_dims(3, sl2_bracket(), max_weight=15)
        for w in range(1, 16):
            tri = any(p * (p + 1) // 2 == w for p in range(1, 6))
            if tri:
                assert totals[w - 1] > 0, \
                    f"triangular weight {w} has zero total (unexpected)"
            else:
                assert totals[w - 1] == 0, \
                    f"non-triangular weight {w} has nonzero total {totals[w-1]}"


# ============================================================================
# Group 12: Multi-path cross-checks (AP10 prevention)
# ============================================================================


class TestMultiPathCrossChecks:
    """Every hardcoded value must be derivable by at least two independent paths.

    Each test below computes a quantity via two (or more) distinct methods
    and verifies they agree. This prevents AP10 (tests with hardcoded wrong
    expected values) — the verification is from AGREEMENT across methods,
    not from any single hardcoded number.
    """

    def test_euler_series_direct_product_vs_inclusion_exclusion(self):
        """Two independent computations of prod (1-t^n)^d agree.

        Path 1: Engine's ce_euler_series (builds the product mode-by-mode
                with binomial coefficients).
        Path 2: Direct multiplication of polynomial factors (1-t^n)^d by
                iterated convolution.
        """
        for d in [1, 2, 3, 5, 8]:
            max_w = 6
            path1 = ce_euler_series(max_w, d)

            # Path 2: iterated polynomial multiplication
            # start with 1, multiply by (1 - t^n)^d for each n >= 1
            path2 = [0] * (max_w + 1)
            path2[0] = 1
            for n in range(1, max_w + 1):
                # compute (1 - t^n)^d as a polynomial
                factor = [0] * (max_w + 1)
                for j in range(d + 1):
                    deg = j * n
                    if deg > max_w:
                        break
                    from math import comb
                    factor[deg] = comb(d, j) * ((-1) ** j)
                # convolve path2 with factor
                new_path2 = [0] * (max_w + 1)
                for i in range(max_w + 1):
                    if path2[i] == 0:
                        continue
                    for k in range(max_w + 1 - i):
                        new_path2[i + k] += path2[i] * factor[k]
                path2 = new_path2
            for w in range(max_w + 1):
                assert path1[w] == path2[w], \
                    f"d={d}, w={w}: path1={path1[w]} != path2={path2[w]}"

    def test_sl2_gl_formula_matches_ce_computation_at_multiple_weights(self):
        """Garland-Lepowsky formula vs direct CE computation agree.

        Path 1: Formula dim H^p = 2p + 1 at w = p(p+1)/2.
        Path 2: Direct CE cohomology via CECurrentAlgebra.
        Two independent implementations in the same function.
        """
        br = sl2_bracket()
        ce = CECurrentAlgebra(3, br, max_weight=21)
        for p in range(1, 7):
            w = p * (p + 1) // 2
            formula = 2 * p + 1
            computed = int(ce.cohomology_at_weight(p, w))
            assert formula == computed, \
                f"p={p}, w={w}: GL formula={formula} vs CE={computed}"

    def test_pbw_euler_are_multiplicative_inverses(self):
        """PBW Hilbert series and Euler series are multiplicative inverses.

        Path 1: Direct products prod(1-t^n)^{-d} and prod(1-t^n)^d.
        Path 2: Convolve them to verify they multiply to the constant 1.
        If they match by ONLY the first path we are not checking anything
        structural. The convolution test is the cross-check.
        """
        for d in [1, 2, 3, 5, 8]:
            max_w = 6
            euler = ce_euler_series(max_w, d)
            pbw = pbw_hilbert_series(max_w, d)
            # Path 1 agreement: convolution = delta
            prod = [0] * (max_w + 1)
            for i in range(max_w + 1):
                for j in range(max_w + 1 - i):
                    prod[i + j] += euler[i] * pbw[j]
            # Path 2: deduce the first few Euler coefficients from PBW via
            # the Newton-Girard identity for the exponential generating
            # function? We use the simpler convolution check:
            assert prod[0] == 1
            for k in range(1, max_w + 1):
                assert prod[k] == 0

    def test_sl2_totals_match_via_three_paths(self):
        """Three independent paths to sl_2 total bar dim per weight.

        Path 1: Direct CE computation via bar_total_dims.
        Path 2: Garland-Lepowsky explicit formula (2p+1 at w=p(p+1)/2, 0 else).
        Path 3: Absolute value of signed Euler coefficient (since sl_2 is
                concentrated on a single bidegree per nonzero weight, the
                signed sum has no cancellation and |chi| = total).
        """
        max_w = 15
        path1 = bar_total_dims(3, sl2_bracket(), max_w)
        path2 = [garland_lepowsky_total_dim_sl2(w) for w in range(1, max_w + 1)]
        pred = ce_euler_series(max_w, 3)
        path3 = [abs(pred[w]) for w in range(1, max_w + 1)]
        assert path1 == path2 == path3

    def test_dim_only_claim_three_algebras_cross_check(self):
        """Euler series agreement across three rank-3 algebras, three ways.

        Path 1: Engine's ce_euler_series (closed formula).
        Path 2: bar_euler_from_bidegrees on sl_2 (actual CE computation).
        Path 3: bar_euler_from_bidegrees on abelian^3 (actual CE computation).
        Path 4: bar_euler_from_bidegrees on nilp Heis_3 (actual CE computation).
        All four must agree.
        """
        max_w = 6
        path1 = list(ce_euler_series(max_w, 3)[1:])
        path2 = bar_euler_from_bidegrees(3, sl2_bracket(), max_w)
        path3 = bar_euler_from_bidegrees(3, abelian_bracket(3), max_w)
        path4 = bar_euler_from_bidegrees(3, heisenberg3_bracket(), max_w)
        assert path1 == path2 == path3 == path4

    def test_h1_equals_dim_g_three_ways(self):
        """H^1(g_-)_1 = dim g via three paths.

        Path 1: Direct CE computation.
        Path 2: Theory: H^1(g_-)_1 = (g_-)_1 / [g_-, g_-]_1 = g / {0} = g.
        Path 3: Coefficient of (-t) in prod (1-t^n)^d is -d, matching
                chi_1 = -dim H^1_1.
        """
        for d, br in [
            (3, sl2_bracket()),
            (3, abelian_bracket(3)),
            (8, sl3_bracket()),
            (6, so4_bracket()),
        ]:
            ce = CECurrentAlgebra(d, br, max_weight=2)
            path1 = int(ce.cohomology_at_weight(1, 1))
            path2 = d  # theory
            path3 = -ce_euler_series(1, d)[1]  # -chi_1 = dim H^1_1
            assert path1 == path2 == path3 == d

    def test_so4_kunneth_three_ways(self):
        """so_4 = sl_2 x sl_2 Kunneth check across three paths.

        Path 1: Direct CE of so_4 (loop of sl_2 x sl_2).
        Path 2: Euler series prod (1-t^n)^6 = (prod (1-t^n)^3)^2.
        Path 3: Convolution of sl_2 CE Euler series with itself.
        """
        max_w = 5
        # Path 1: Direct
        path1 = bar_euler_from_bidegrees(6, so4_bracket(), max_w)
        # Path 2: Direct d=6 Euler
        pred6 = ce_euler_series(max_w, 6)
        path2 = list(pred6[1:])
        # Path 3: Convolve d=3 Euler with itself
        pred3 = ce_euler_series(max_w, 3)
        path3_full = [0] * (max_w + 1)
        for i in range(max_w + 1):
            for j in range(max_w + 1 - i):
                path3_full[i + j] += pred3[i] * pred3[j]
        path3 = path3_full[1:]
        assert path1 == path2 == path3

    def test_sl3_bidegree_cross_check_euler_vs_ce(self):
        """sl_3 nonzero bidegree (1,1)->8, (2,2)->20, (3,4)->63 cross-checked.

        Path 1: bar_bidegree_table direct output.
        Path 2: bar_total_dims at each weight (must equal sum over p).
        Path 3: Signed Euler series = sum_p (-1)^p dim (must match prod (1-t^n)^8).
        """
        max_w = 4
        br = sl3_bracket()
        table = bar_bidegree_table(8, br, max_w)
        # Path 1: read table
        path1 = [table.get((1, 1), 0), table.get((2, 2), 0),
                 table.get((2, 3), 0) + table.get((3, 3), 0),
                 table.get((2, 4), 0) + table.get((3, 4), 0)
                 + table.get((4, 4), 0)]
        # Path 2: totals
        path2 = bar_total_dims(8, br, max_w)
        assert path1 == path2
        # Path 3: signed Euler matches prod (1-t^n)^8
        pred = ce_euler_series(max_w, 8)
        path3 = bar_euler_from_bidegrees(8, br, max_w)
        for w in range(1, max_w + 1):
            assert path3[w - 1] == pred[w]

    def test_bott_poincare_series_expansion_cross_check(self):
        """Bott Poincare series cross-checked by direct partition counting.

        Path 1: Engine's bott_pontryagin_poincare_series.
        Path 2: Direct partition counting: coefficient of t^n in
                prod 1/(1-t^{d_i}) = number of multisets drawn from
                {d_1, d_2, ...} summing to n.
        """
        gens = bott_pontryagin_generators("A", 2)  # SU(3): [2, 4]
        max_d = 12
        path1 = bott_pontryagin_poincare_series("A", 2, max_d)

        # Path 2: count (a, b) >= 0 with 2a + 4b = n
        path2 = [0] * (max_d + 1)
        for a in range(max_d // 2 + 1):
            for b in range((max_d - 2 * a) // 4 + 1):
                n = 2 * a + 4 * b
                if n <= max_d:
                    path2[n] += 1
        assert path1 == path2

    def test_falsification_claim_three_ways(self):
        """The falsification 'dim H^2_3 differs by algebra at dim_g=3' is verified.

        Path 1: Direct CE computation of dim H^2_3 for sl_2.
        Path 2: Direct CE computation of dim H^2_3 for abelian^3.
        Path 3: Direct CE computation of dim H^2_3 for nilp Heis_3.
        The three values must be pairwise DISTINCT, proving the
        dim-only claim fails.
        """
        def h2_w3(br):
            ce = CECurrentAlgebra(3, br, max_weight=3)
            return int(ce.cohomology_at_weight(2, 3))

        v_sl2 = h2_w3(sl2_bracket())
        v_abel = h2_w3(abelian_bracket(3))
        v_nilp = h2_w3(heisenberg3_bracket())
        # Cross-check: signed Euler chi_3 = sum_p (-1)^p dim H^p_3
        # Euler at w=3 is +5 (coefficient of t^3 in prod(1-t^n)^3).
        chi3 = ce_euler_series(3, 3)[3]
        assert chi3 == 5
        # For sl_2: H^1_3 = 0, H^2_3 = 5, H^3_3 = 0 so chi = 5.
        # For abelian^3: H^1_3=3, H^2_3=9, H^3_3=1 so chi = -3+9-1 = 5.
        # For nilp Heis_3: H^1_3=2, H^2_3=7, H^3_3=0 so chi = -2+7 = 5.
        # Each algebra has a DIFFERENT decomposition but the SAME Euler.
        assert v_sl2 == 5
        assert v_abel == 9
        assert v_nilp == 7
        # All three different
        assert len({v_sl2, v_abel, v_nilp}) == 3

    def test_sl2_gl_predicts_3_5_7_9_11_13(self):
        """Garland-Lepowsky predicts odd sequence 3,5,7,9,11,13 at triangular weights.

        Path 1: 2p+1 formula for p = 1..6.
        Path 2: Direct CE computation at (p, p(p+1)/2) for each p.
        Path 3: The sequence is OEIS A005408 (odd numbers), recognised by
                the invariant 2p+1.
        """
        br = sl2_bracket()
        ce = CECurrentAlgebra(3, br, max_weight=21)
        path1 = [2 * p + 1 for p in range(1, 7)]
        path2 = [int(ce.cohomology_at_weight(p, p * (p + 1) // 2))
                 for p in range(1, 7)]
        path3 = [3, 5, 7, 9, 11, 13]
        assert path1 == path2 == path3

    def test_abelian_bar_total_dims_convolution_structure(self):
        """Abelian total dims factor as a convolution over modes.

        For abelian g of dim d, g_- is a free graded abelian Lie algebra;
        its CE complex is the exterior algebra on d generators per mode.

        Path 1: bar_total_dims direct.
        Path 2: The total exterior algebra dimension per weight is
                the coefficient of t^w in prod_{n >= 1}(1+t^n)^d (sum
                of bidegrees). Cross-check this against direct computation.
        """
        from math import comb

        d = 3
        max_w = 6

        # Path 1: direct bar total dims
        totals_path1 = bar_total_dims(d, abelian_bracket(d), max_w)

        # Path 2: coefficient of t^w in prod (1+t^n)^d
        # (total dim of Lambda^*(g_-)^*_w, bigraded by antisymmetric subsets)
        coeffs = [0] * (max_w + 1)
        coeffs[0] = 1
        for n in range(1, max_w + 1):
            old = list(coeffs)
            for j in range(1, d + 1):
                deg = j * n
                if deg > max_w:
                    break
                cdj = comb(d, j)
                for w in range(max_w + 1 - deg):
                    coeffs[w + deg] += cdj * old[w]
        # For abelian g the cohomology equals the full exterior algebra
        # MINUS the constant term at weight 0. So totals_path1 should equal
        # coeffs[1:max_w+1].
        assert totals_path1 == coeffs[1:max_w + 1]
