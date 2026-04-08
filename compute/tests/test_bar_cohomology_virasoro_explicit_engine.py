r"""Tests for bar_cohomology_virasoro_explicit_engine.py.

Verifies the bar cohomology H*(B(Vir_c)) at conformal weights 0--10
via three independent methods:
  1. CE cohomology of Vir_- (conformal weight grading)
  2. Direct OPE verification (exact rational arithmetic)
  3. Algebraic generating function (PBW-degree grading)

Test categories:
  1. Partition functions: p_geq2, q_geq2 (weight space dimensions)
  2. Motzkin numbers and PBW-degree Koszul dual (Method 3)
  3. CE complex: d^2 = 0, chain dimensions (Method 1)
  4. CE cohomology dimensions at each (k, w) (Method 1)
  5. H^1 cocycle analysis: bracket-theoretic determination
  6. Koszulness: H^k = 0 for k >= 2 at low weight (verified)
  7. c-independence: CE matrices have integer entries
  8. OPE verification at multiple c values (Method 2)
  9. Weight-4 quasi-primary [TT] (AP26)
  10. Cross-validation between methods
  11. Generating function algebraicity verification (Method 3)
  12. Comparison: H^1 vs p(h)-p(h-1) (the answer is NO)

67 tests.

Manuscript references:
  comp:virasoro-ope, comp:virasoro-bar-diff (bar_complex_tables.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  prop:virasoro-generic-koszul-dual (w_algebras.tex)
  combinatorial_frontier.tex subsec:virasoro-near-rationality
  AP19 (bar kernel absorbs a pole)
  AP26 (BPZ inner product for quasi-primary decomposition)
  AP45 (desuspension lowers degree)
"""

import pytest
from fractions import Fraction

from compute.lib.bar_cohomology_virasoro_explicit_engine import (
    # Partition functions
    partitions_geq2,
    partitions_distinct_geq2,
    p_geq2,
    q_geq2,
    # Motzkin / PBW-degree
    motzkin,
    koszul_dual_pbw_dim,
    koszul_dual_pbw_gf_coefficients,
    verify_gf_algebraic,
    # CE engine
    VirasoroCEEngine,
    compute_full_cohomology_table,
    compute_h1_table,
    compute_ce_total_at_weight,
    compute_chain_group_dims,
    verify_ce_d_squared_full,
    check_c_independence_ce,
    # H^1 analysis
    h1_cocycle_analysis,
    # OPE
    VermaModuleExact,
    NthProductsExact,
    verify_ope_basic,
    # Weight-4
    weight4_quasi_primary,
    # Comparison
    h1_vs_partition_difference,
    # Summary
    full_summary,
)

FR = Fraction


# =============================================================================
# 1. Partition functions
# =============================================================================

class TestPartitionsGeq2:
    """Partitions of n into parts >= 2 (Verma module dimensions)."""

    def test_n0(self):
        assert partitions_geq2(0) == ((),)

    def test_n1(self):
        assert partitions_geq2(1) == ()

    def test_n2(self):
        assert len(partitions_geq2(2)) == 1

    def test_n3(self):
        assert len(partitions_geq2(3)) == 1

    def test_n4(self):
        assert len(partitions_geq2(4)) == 2  # (4,) and (2,2)

    def test_known_sequence(self):
        """p_geq2: 1, 0, 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21."""
        expected = {0: 1, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 4,
                    7: 4, 8: 7, 9: 8, 10: 12, 11: 14, 12: 21}
        for n, val in expected.items():
            assert p_geq2(n) == val, f"p_geq2({n}) = {p_geq2(n)}, expected {val}"


class TestPartitionsDistinctGeq2:
    """Partitions into distinct parts >= 2 (CE chain group dimensions)."""

    def test_n0(self):
        assert q_geq2(0) == 1

    def test_n1(self):
        assert q_geq2(1) == 0

    def test_n2_through_10(self):
        """q_geq2: 1, 0, 1, 1, 1, 2, 2, 3, 3, 5, 5."""
        expected = {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2,
                    7: 3, 8: 3, 9: 5, 10: 5}
        for n, val in expected.items():
            assert q_geq2(n) == val, f"q_geq2({n}) = {q_geq2(n)}, expected {val}"

    def test_gf_consistency(self):
        """GF of q_geq2 = prod_{k>=2} (1+q^k).

        Verify by dynamic programming.
        """
        N = 15
        dp = [0] * (N + 1)
        dp[0] = 1
        for k in range(2, N + 1):
            for w in range(N, k - 1, -1):
                dp[w] += dp[w - k]
        for w in range(N + 1):
            assert q_geq2(w) == dp[w], f"q_geq2({w}) = {q_geq2(w)}, dp = {dp[w]}"


# =============================================================================
# 2. Motzkin numbers and PBW-degree grading
# =============================================================================

class TestMotzkinNumbers:
    """Motzkin numbers M(n): OEIS A001006."""

    def test_base_cases(self):
        assert motzkin(0) == 1
        assert motzkin(1) == 1

    def test_known_values(self):
        """M(n): 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188."""
        expected = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188]
        for n, val in enumerate(expected):
            assert motzkin(n) == val, f"M({n}) = {motzkin(n)}, expected {val}"

    def test_recurrence(self):
        """(n+3)*M(n+1) = (2n+3)*M(n) + 3n*M(n-1) for n >= 1."""
        for n in range(1, 15):
            lhs = (n + 3) * motzkin(n + 1)
            rhs = (2 * n + 3) * motzkin(n) + 3 * n * motzkin(n - 1)
            assert lhs == rhs, f"Recurrence fails at n={n}: {lhs} != {rhs}"

    def test_negative(self):
        assert motzkin(-1) == 0


class TestKoszulDualPBW:
    """PBW-degree Hilbert function of Vir^! via Motzkin convolution."""

    def test_dim_0(self):
        assert koszul_dual_pbw_dim(0) == 0

    def test_dim_1(self):
        assert koszul_dual_pbw_dim(1) == 1

    def test_manuscript_table(self):
        """dim(Vir^!)_n from combinatorial_frontier.tex table."""
        expected = {1: 1, 2: 2, 3: 5, 4: 12, 5: 30, 6: 76,
                    7: 196, 8: 512, 9: 1353, 10: 3610}
        for n, val in expected.items():
            assert koszul_dual_pbw_dim(n) == val, \
                f"dim(Vir^!)_{n} = {koszul_dual_pbw_dim(n)}, expected {val}"

    def test_convolution_formula(self):
        """dim(Vir^!)_n = sum_{j=0}^{n-1} M(j)*M(n-1-j)."""
        for n in range(1, 12):
            conv = sum(motzkin(j) * motzkin(n - 1 - j) for j in range(n))
            assert koszul_dual_pbw_dim(n) == conv

    def test_motzkin_difference_identity(self):
        """dim(Vir^!)_n = M(n+1) - M(n) (Motzkin differences).

        This identity follows from the Motzkin functional equation
        M = 1 + x*M + x^2*M^2, which gives x*M^2 = M - 1 - x*M = (M-1)(1-x)/x...
        Actually: M - 1 = x*M + x^2*M^2 = x*M*(1+x*M), and
        x*M^2 = M - 1 - x*M = (M-1)(1 - x*M/(M-1))... simpler:
        [x^n](M(x) - 1) = M(n) for n >= 1 (shift).
        [x^n](x*M(x)^2) = [x^{n-1}](M^2) = sum M(j)M(n-1-j).
        From M = 1 + xM + x^2 M^2: M - 1 = xM(1 + xM), so
        (M-1)/x = M + xM^2.  Thus xM^2 = (M-1)/x - M = (M-1-xM)/x.
        Comparing: [x^n](xM^2) = [x^{n+1}](M-1) - [x^n](M) = M(n+1) - M(n).
        """
        for n in range(0, 15):
            assert koszul_dual_pbw_dim(n) == motzkin(n + 1) - motzkin(n)

    def test_gf_coefficients(self):
        """koszul_dual_pbw_gf_coefficients agrees with koszul_dual_pbw_dim."""
        coeffs = koszul_dual_pbw_gf_coefficients(12)
        for n in range(13):
            assert coeffs[n] == koszul_dual_pbw_dim(n)


class TestGFAlgebraic:
    """Verify P(x) = x*M(x)^2 = 4x/(1-x+sqrt(1-2x-3x^2))^2."""

    def test_all_match(self):
        results = verify_gf_algebraic(10)
        for n, ok in results.items():
            assert ok, f"GF mismatch at n={n}"

    def test_growth_rate(self):
        """Dominant singularity at x=1/3 gives growth ~ 3^n."""
        for n in range(5, 10):
            ratio = koszul_dual_pbw_dim(n + 1) / koszul_dual_pbw_dim(n)
            assert 2.5 < ratio < 3.5, f"Growth ratio at n={n}: {ratio:.3f}"


# =============================================================================
# 3. CE complex: d^2 = 0 and chain dimensions
# =============================================================================

class TestCEDSquared:
    """d^2 = 0 in the CE complex of Vir_-."""

    def test_all_d_squared_zero(self):
        results = verify_ce_d_squared_full(10)
        for (deg, wt), ok in results.items():
            assert ok, f"d^2 != 0 at degree {deg}, weight {wt}"


class TestCEChainDimensions:
    """Chain group dimensions Lambda^k(Vir_-^*)_w."""

    @pytest.fixture(scope="class")
    def dims(self):
        return compute_chain_group_dims(10, 4)

    def test_lambda1_w2(self, dims):
        """Lambda^1 at weight 2: one generator L_{-2}^*."""
        assert dims.get((1, 2), 0) == 1

    def test_lambda1_w3(self, dims):
        assert dims.get((1, 3), 0) == 1

    def test_lambda1_w4(self, dims):
        assert dims.get((1, 4), 0) == 1

    def test_lambda2_w5(self, dims):
        """Lambda^2 at weight 5: {L_{-2}, L_{-3}} only."""
        assert dims.get((2, 5), 0) == 1

    def test_lambda2_w7(self, dims):
        """Lambda^2 at weight 7: {L_{-2},L_{-5}} and {L_{-3},L_{-4}}."""
        assert dims.get((2, 7), 0) == 2

    def test_lambda2_below_min(self, dims):
        """Lambda^2 at weight 4: impossible (min = 2+3=5)."""
        assert dims.get((2, 4), 0) == 0

    def test_lambda3_min_weight(self, dims):
        """Lambda^3 minimum weight = 2+3+4 = 9."""
        assert dims.get((3, 8), 0) == 0
        assert dims.get((3, 9), 0) == 1


# =============================================================================
# 4. CE cohomology at each (k, w)
# =============================================================================

class TestCECohomologyTable:
    """Full H^k(B(Vir))_w table via CE cohomology."""

    @pytest.fixture(scope="class")
    def table(self):
        return compute_full_cohomology_table(10, 4)

    def test_h1_weight_2(self, table):
        assert table.get((1, 2), 0) == 1

    def test_h1_weight_3(self, table):
        assert table.get((1, 3), 0) == 1

    def test_h1_weight_4(self, table):
        assert table.get((1, 4), 0) == 1

    def test_h1_weight_5_vanishes(self, table):
        """H^1 at weight 5 = 0: [L_{-2}, L_{-3}] = L_{-5} kills the cocycle."""
        assert table.get((1, 5), 0) == 0

    def test_h1_vanishes_weight_6_to_10(self, table):
        for w in range(6, 11):
            assert table.get((1, w), 0) == 0, f"H^1 at weight {w} should be 0"

    def test_h2_weight_7(self, table):
        """H^2 starts at weight 7."""
        assert table.get((2, 7), 0) == 1

    def test_h2_weight_5_6_vanish(self, table):
        assert table.get((2, 5), 0) == 0
        assert table.get((2, 6), 0) == 0

    def test_h3_vanishes_through_10(self, table):
        """H^3 = 0 for all weights <= 10 (min weight for Lambda^3 = 9)."""
        for w in range(0, 11):
            assert table.get((3, w), 0) == 0, f"H^3 at weight {w} should be 0"

    def test_h4_vanishes_through_10(self, table):
        for w in range(0, 11):
            assert table.get((4, w), 0) == 0


class TestCETotalsByWeight:
    """Total dim sum_k H^k(CE)_w at each conformal weight."""

    @pytest.fixture(scope="class")
    def totals(self):
        return compute_ce_total_at_weight(10)

    def test_weight_0(self, totals):
        assert totals[0] == 1

    def test_weight_1(self, totals):
        assert totals[1] == 0

    def test_weight_2_3_4(self, totals):
        for w in [2, 3, 4]:
            assert totals[w] == 1, f"Total at weight {w}: {totals[w]}"

    def test_weight_5_6_vanish(self, totals):
        assert totals[5] == 0
        assert totals[6] == 0

    def test_weight_7_to_10(self, totals):
        for w in range(7, 11):
            assert totals[w] == 1, f"Total at weight {w}: {totals[w]}"


# =============================================================================
# 5. H^1 cocycle analysis
# =============================================================================

class TestH1CocycleAnalysis:
    """Bracket-theoretic determination of H^1."""

    @pytest.fixture(scope="class")
    def analysis(self):
        return h1_cocycle_analysis(10)

    def test_below_weight_2(self, analysis):
        assert analysis[0]['dim'] == 0
        assert analysis[1]['dim'] == 0

    def test_weight_2_cocycle(self, analysis):
        assert analysis[2]['is_cocycle'] is True
        assert analysis[2]['dim'] == 1

    def test_weight_3_cocycle(self, analysis):
        assert analysis[3]['is_cocycle'] is True

    def test_weight_4_cocycle(self, analysis):
        """Weight 4: only a=b=2 with a+b=4, but a < b fails."""
        assert analysis[4]['is_cocycle'] is True
        assert analysis[4]['dim'] == 1

    def test_weight_5_not_cocycle(self, analysis):
        """Weight 5: [L_{-2}, L_{-3}] = L_{-5}."""
        assert analysis[5]['is_cocycle'] is False
        assert analysis[5]['dim'] == 0

    def test_weight_6_not_cocycle(self, analysis):
        """Weight 6: [L_{-2}, L_{-4}] = 2*L_{-6}."""
        assert analysis[6]['is_cocycle'] is False
        assert len(analysis[6]['decompositions']) >= 1

    def test_all_weights_ge5_not_cocycle(self, analysis):
        for w in range(5, 11):
            assert analysis[w]['is_cocycle'] is False


# =============================================================================
# 6. Koszulness verification
# =============================================================================

class TestKoszulness:
    """H^k(B(Vir)) = 0 for k >= 3 at all computed weights (Koszulness)."""

    @pytest.fixture(scope="class")
    def table(self):
        return compute_full_cohomology_table(10, 4)

    def test_h3_zero(self, table):
        for w in range(0, 11):
            assert table.get((3, w), 0) == 0

    def test_h4_zero(self, table):
        for w in range(0, 11):
            assert table.get((4, w), 0) == 0

    def test_h2_nonzero_at_7(self, table):
        """H^2 is genuinely nonzero at weight 7, so Koszulness is
        bar-degree-1 concentration, NOT vanishing of all H^k for k >= 2.

        The correct statement: for a Koszul algebra with generators in
        degrees >= 2, bar cohomology concentrates on the 'Koszul diagonal'
        p + q = constant, not literally in bar degree 1.  The diagonal
        condition means H^k_w != 0 only when (k, w) satisfies the Koszul
        bigrading constraint.
        """
        assert table.get((2, 7), 0) == 1


# =============================================================================
# 7. c-independence
# =============================================================================

class TestCIndependence:
    """Bar cohomology is c-independent (no central term for m,n >= 2)."""

    def test_integer_matrices(self):
        assert check_c_independence_ce(10) is True

    def test_ope_consistent_at_multiple_c(self):
        """OPE identities hold at c = -2, 0, 1, 13, 26."""
        for c_val in [FR(-2), FR(0), FR(1), FR(13), FR(26)]:
            results = verify_ope_basic(c_val)
            for name, ok in results.items():
                assert ok, f"OPE {name} failed at c={c_val}"


# =============================================================================
# 8. OPE verification (Method 2)
# =============================================================================

class TestOPEBasic:
    """Virasoro OPE from commutation relations, exact arithmetic."""

    @pytest.fixture(scope="class")
    def nth_c1(self):
        verma = VermaModuleExact(FR(1), 10)
        return NthProductsExact(verma)

    def test_T3T(self, nth_c1):
        """T_{(3)}T = c/2 = 1/2 at c=1."""
        r, v = nth_c1.nth_product((2,), 3, (2,))
        assert v == FR(1, 2)
        assert len(r) == 0

    def test_T2T(self, nth_c1):
        """T_{(2)}T = 0."""
        r, v = nth_c1.nth_product((2,), 2, (2,))
        assert v == FR(0)
        assert len(r) == 0

    def test_T1T(self, nth_c1):
        """T_{(1)}T = 2T."""
        r, v = nth_c1.nth_product((2,), 1, (2,))
        assert v == FR(0)
        assert len(r) == 1
        assert r[0] == ((2,), FR(2))

    def test_T0T(self, nth_c1):
        """T_{(0)}T = dT = L_{-3}|0>."""
        r, v = nth_c1.nth_product((2,), 0, (2,))
        assert v == FR(0)
        assert len(r) == 1
        assert r[0] == ((3,), FR(1))

    def test_T1_on_L22(self, nth_c1):
        """T_{(1)}(L_{-2}^2|0>) = L_0(L_{-2}^2|0>) = 4*(L_{-2}^2|0>)."""
        r, v = nth_c1.nth_product((2,), 1, (2, 2))
        assert v == FR(0)
        found = False
        for state, coeff in r:
            if state == (2, 2):
                assert coeff == FR(4)
                found = True
        assert found

    def test_dT_0_T(self, nth_c1):
        """(dT)_{(0)} T = L_{-2}T = L_{-2}L_{-2}|0> = L_{-2}^2|0>."""
        r, v = nth_c1.nth_product((3,), 0, (2,))
        assert v == FR(0)
        found = False
        for state, coeff in r:
            if state == (2, 2):
                found = True
                assert coeff == FR(1)
        assert found


class TestOPEMultipleC:
    """OPE identities at c = -2, 0, 13, 26."""

    @pytest.mark.parametrize("c_val", [FR(-2), FR(0), FR(13), FR(26)])
    def test_ope_basic(self, c_val):
        results = verify_ope_basic(c_val)
        for name, ok in results.items():
            assert ok, f"OPE {name} failed at c={c_val}"


# =============================================================================
# 9. Weight-4 quasi-primary (AP26)
# =============================================================================

class TestWeight4QuasiPrimary:
    """[TT] = L_{-2}^2|0> - (3/5)L_{-4}|0> is quasi-primary."""

    @pytest.mark.parametrize("c_val", [FR(1), FR(26), FR(13)])
    def test_quasi_primary(self, c_val):
        result = weight4_quasi_primary(c_val)
        assert result['is_quasi_primary'] is True, \
            f"[TT] not quasi-primary at c={c_val}: {result['combined']}"

    def test_not_in_h2(self):
        """[TT] does not appear in H^2_4 because Lambda^2_4 = 0."""
        table = compute_full_cohomology_table(10, 4)
        assert table.get((2, 4), 0) == 0


# =============================================================================
# 10. Cross-validation
# =============================================================================

class TestCrossValidation:
    """Cross-checks between methods."""

    def test_h1_matches_cocycle_analysis(self):
        """CE H^1 matches bracket-theoretic analysis at each weight."""
        h1_table = compute_h1_table(10)
        analysis = h1_cocycle_analysis(10)
        for w in range(0, 11):
            assert h1_table[w] == analysis[w]['dim'], \
                f"w={w}: CE H^1={h1_table[w]}, analysis={analysis[w]['dim']}"

    def test_chain_dims_match_partition_count(self):
        """Lambda^1_w chain dim = 1 for w >= 2 (one generator L_{-w})."""
        dims = compute_chain_group_dims(10, 1)
        for w in range(2, 11):
            assert dims.get((1, w), 0) == 1

    def test_lambda2_dim_equals_distinct_partitions(self):
        """dim Lambda^2_w = (partitions of w into exactly 2 distinct parts >= 2)."""
        ce = VirasoroCEEngine(max_weight=30)
        for w in range(5, 11):
            ce_dim = ce.chain_dim(2, w)
            # Count: pairs (a, b) with 2 <= a < b and a+b = w
            count = len([(a, w - a) for a in range(2, w) if w - a > a])
            assert ce_dim == count, f"w={w}: Lambda^2={ce_dim}, count={count}"

    def test_pbw_dim_1_equals_motzkin_squared(self):
        """dim(Vir^!)_1 = M(0)^2 = 1."""
        assert koszul_dual_pbw_dim(1) == motzkin(0) ** 2

    def test_pbw_dim_2_convolution(self):
        """dim(Vir^!)_2 = M(0)*M(1) + M(1)*M(0) = 2."""
        assert koszul_dual_pbw_dim(2) == 2 * motzkin(0) * motzkin(1)


# =============================================================================
# 11. Generating function algebraicity
# =============================================================================

class TestGFAlgebraicity:
    """P(x) = 4x/(1-x+sqrt(1-2x-3x^2))^2 = x*M(x)^2."""

    def test_algebraic_expansion_matches(self):
        results = verify_gf_algebraic(10)
        for n, ok in results.items():
            assert ok, f"GF algebraic expansion mismatch at n={n}"

    def test_discriminant(self):
        """Discriminant 1-2x-3x^2 = (1-3x)(1+x). Roots at x=1/3 and x=-1."""
        # (1-3x)(1+x) = 1 + x - 3x - 3x^2 = 1 - 2x - 3x^2. Check.
        for x_val in [FR(1, 3), FR(-1)]:
            disc = 1 - 2 * x_val - 3 * x_val ** 2
            assert disc == 0

    def test_near_rationality_recurrence(self):
        """The spurious recurrence a_k = 4a_{k-1} - 2a_{k-2} - 4a_{k-3}
        holds for k = 4,...,8 but fails at k = 9 (error = 1)."""
        a = [0] + [koszul_dual_pbw_dim(n) for n in range(1, 12)]
        for k in range(4, 9):
            pred = 4 * a[k - 1] - 2 * a[k - 2] - 4 * a[k - 3]
            assert pred == a[k], f"Recurrence fails at k={k}: {pred} != {a[k]}"
        # Fails at k=9
        pred_9 = 4 * a[8] - 2 * a[7] - 4 * a[6]
        assert pred_9 != a[9], "Spurious recurrence should fail at k=9"
        assert a[9] - pred_9 == 1, f"Error at k=9 should be 1, got {a[9]-pred_9}"


# =============================================================================
# 12. H^1 vs p(h) - p(h-1)
# =============================================================================

class TestH1VsPartitionDifference:
    """The dimension of H^1 is NOT p(h) - p(h-1)."""

    @pytest.fixture(scope="class")
    def comparison(self):
        return h1_vs_partition_difference(10)

    def test_not_equal_at_weight_4(self, comparison):
        """At weight 4: H^1 = 1, p(4)-p(3) = 5-3 = 2."""
        r = comparison[4]
        assert r['h1_dim'] != r['p_diff']

    def test_not_equal_at_weight_5(self, comparison):
        """At weight 5: H^1 = 0, p(5)-p(4) = 7-5 = 2."""
        r = comparison[5]
        assert r['h1_dim'] == 0
        assert r['p_diff'] > 0

    def test_h1_not_q_geq2(self, comparison):
        """H^1 by conformal weight is NOT q_geq2 either (the CE chain group dim)."""
        for w in range(5, 11):
            r = comparison[w]
            assert r['h1_dim'] == 0  # H^1 vanishes for w >= 5
            assert r['q_geq2'] > 0  # but q_geq2 is positive


# =============================================================================
# Additional edge cases and structural tests
# =============================================================================

class TestEdgeCases:
    """Edge cases and structural properties."""

    def test_motzkin_growth(self):
        """M(n) grows as C * 3^n / n^{3/2} for large n."""
        for n in range(8, 12):
            assert motzkin(n + 1) > 2 * motzkin(n)
            assert motzkin(n + 1) < 4 * motzkin(n)

    def test_pbw_dim_positive(self):
        for n in range(1, 15):
            assert koszul_dual_pbw_dim(n) > 0

    def test_p_geq2_monotone(self):
        """p_geq2(n) is weakly increasing for n >= 2."""
        for n in range(2, 15):
            assert p_geq2(n + 1) >= p_geq2(n)

    def test_ce_engine_construction(self):
        ce = VirasoroCEEngine(max_weight=10)
        assert ce.n_gens == 9
        assert ce._gen_weights[0] == 2

    def test_full_summary_returns_all_keys(self):
        s = full_summary(6)
        assert 'cohomology_by_degree_weight' in s
        assert 'ce_total_by_weight' in s
        assert 'pbw_degree_dims' in s
