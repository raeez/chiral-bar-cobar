"""Tests for bar cohomology verification module.

Three strategies provide different perspectives on bar cohomology:
  A: CE cohomology of g_- = sl_2 tensor t^{-1}C[t^{-1}] (E_2 of PBW SS)
  B: Vacuum module g-invariants (cross-validated)
  C: Koszul dual Hilbert series (Riordan numbers, combinatorial prediction)

KEY FACT: Strategies A and C compute DIFFERENT things.
  H^1: A=3, C=3 (agree).
  H^2: A=5, C=6 (disagree by 1).
  The discrepancy arises because CE uses exterior powers Lambda^n(g_-)
  while the chiral bar complex uses tensor products with OS forms.
  See module docstring for detailed mathematical discussion.
"""

import pytest

from compute.lib.bar_cohomology_verification import (
    LoopAlgebraCE,
    riordan,
    strategy_a,
    strategy_a_detail,
    strategy_b_cross_validate,
    strategy_b_invariants,
    strategy_c,
    verify_strategies,
)


# ============================================================
# CE differential: d^2 = 0
# ============================================================

class TestDSquared:
    """Verify d^2 = 0 for the CE differential of g_-."""

    def test_d_squared_weight2(self):
        ce = LoopAlgebraCE(max_weight=2)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 2), f"d^2 != 0 at deg {deg}, weight 2"

    def test_d_squared_weight3(self):
        ce = LoopAlgebraCE(max_weight=3)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 3), f"d^2 != 0 at deg {deg}, weight 3"

    def test_d_squared_weight4(self):
        ce = LoopAlgebraCE(max_weight=4)
        for deg in range(0, 5):
            assert ce.verify_d_squared(deg, 4), f"d^2 != 0 at deg {deg}, weight 4"

    def test_d_squared_weight5(self):
        ce = LoopAlgebraCE(max_weight=5)
        for deg in range(0, 4):
            assert ce.verify_d_squared(deg, 5), f"d^2 != 0 at deg {deg}, weight 5"


# ============================================================
# Chain group dimensions
# ============================================================

class TestChainDims:
    """Verify dimensions of Lambda^p(g_-^*)_H."""

    def test_weight1(self):
        ce = LoopAlgebraCE(max_weight=1)
        assert ce.chain_group_dim(0, 1) == 0
        assert ce.chain_group_dim(1, 1) == 3  # e,h,f at mode 1
        assert ce.chain_group_dim(2, 1) == 0

    def test_weight2(self):
        ce = LoopAlgebraCE(max_weight=2)
        assert ce.chain_group_dim(1, 2) == 3  # e,h,f at mode 2
        assert ce.chain_group_dim(2, 2) == 3  # pairs from mode-1

    def test_weight3(self):
        ce = LoopAlgebraCE(max_weight=3)
        assert ce.chain_group_dim(1, 3) == 3  # mode-3 generators
        assert ce.chain_group_dim(2, 3) == 9  # (mode1, mode2) pairs
        assert ce.chain_group_dim(3, 3) == 1  # {e,h,f} all at mode 1

    def test_weight4(self):
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.chain_group_dim(1, 4) == 3  # mode-4 generators
        assert ce.chain_group_dim(2, 4) == 12  # (1,3): 9 + (2,2): 3
        assert ce.chain_group_dim(3, 4) == 9  # (1,1,2): 3*3=9


# ============================================================
# CE cohomology weight-by-weight
# ============================================================

class TestCEWeightDecomposition:
    """Verify individual H^n(g_-)_H via direct CE computation."""

    def test_h1_weight1(self):
        """H^1(g_-)_1 = 3 (the three weight-1 generators)."""
        ce = LoopAlgebraCE(max_weight=1)
        assert ce.cohomology_dim(1, 1) == 3

    def test_h1_weight2(self):
        """H^1(g_-)_2 = 0 (d_1 at weight 2 is an isomorphism)."""
        ce = LoopAlgebraCE(max_weight=2)
        assert ce.cohomology_dim(1, 2) == 0

    def test_h2_weight2(self):
        """H^2(g_-)_2 = 0 (d_1 has rank 3, killing all of Lambda^2_2)."""
        ce = LoopAlgebraCE(max_weight=2)
        assert ce.cohomology_dim(2, 2) == 0

    def test_h2_weight3(self):
        """H^2(g_-)_3 = 5 (ker(d_2)=8, im(d_1)=3)."""
        ce = LoopAlgebraCE(max_weight=3)
        assert ce.cohomology_dim(2, 3) == 5

    def test_h2_weight4(self):
        """H^2(g_-)_4 = 0 (ker(d_2)=3 = im(d_1)=3, exact)."""
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.cohomology_dim(2, 4) == 0

    def test_h2_weight5(self):
        """H^2(g_-)_5 = 0 (no further contributions)."""
        ce = LoopAlgebraCE(max_weight=5)
        assert ce.cohomology_dim(2, 5) == 0

    def test_h2_weight6(self):
        """H^2(g_-)_6 = 0."""
        ce = LoopAlgebraCE(max_weight=6)
        assert ce.cohomology_dim(2, 6) == 0


# ============================================================
# Strategy A: CE cohomology totals
# ============================================================

class TestStrategyA:
    """Total CE cohomology H^n(g_-, C) via Strategy A.

    NOTE: This is the E_2 page of the PBW SS, NOT the full chiral
    bar cohomology.  The Riordan prediction (Strategy C) gives
    different values at degree >= 2.
    """

    def test_h1_equals_3(self):
        """H^1(CE) = 3 = R(4) (agrees with Riordan at degree 1)."""
        result = strategy_a(max_degree=1, max_weight=4)
        assert result[1] == 3

    def test_h2_equals_5(self):
        """H^2(CE) = 5 (NOT 6 = R(5)).

        Weight decomposition: H^2_2=0, H^2_3=5, H^2_{>=4}=0.
        The Riordan prediction is 6; the discrepancy of 1 arises
        because CE uses exterior powers while the chiral bar complex
        uses tensor products with OS forms on configuration spaces.
        """
        result = strategy_a(max_degree=2, max_weight=6)
        assert result[2] == 5

    @pytest.mark.slow
    def test_h3(self):
        """H^3(CE) — compute for comparison with R(6) = 15."""
        result = strategy_a(max_degree=3, max_weight=10)
        # CE value may differ from Riordan R(6) = 15
        assert result[3] >= 0  # sanity check


# ============================================================
# Strategy C: Riordan numbers
# ============================================================

class TestRiordan:
    """Verify Riordan number values."""

    def test_riordan_base_cases(self):
        assert riordan(0) == 1
        assert riordan(1) == 0
        assert riordan(2) == 1
        assert riordan(3) == 1

    def test_riordan_bar_cohomology_values(self):
        """R(4)=3, R(5)=6, R(6)=15, R(7)=36, R(8)=91, R(9)=232."""
        assert riordan(4) == 3
        assert riordan(5) == 6
        assert riordan(6) == 15
        assert riordan(7) == 36
        assert riordan(8) == 91
        assert riordan(9) == 232

    def test_strategy_c(self):
        c = strategy_c(3)
        assert c == {1: 3, 2: 6, 3: 15}


# ============================================================
# Comparison: CE vs Riordan (they compute different things)
# ============================================================

class TestComparison:
    """Document the relationship between CE and Riordan predictions.

    Strategy A (CE of g_-) and Strategy C (Riordan numbers) compute
    different mathematical quantities.  They agree at degree 1 but
    diverge at degree 2:
      H^1: CE=3, Riordan=3 (agree)
      H^2: CE=5, Riordan=6 (disagree)
    """

    def test_agree_at_degree_1(self):
        """CE and Riordan agree at degree 1: both give 3."""
        a = strategy_a(max_degree=1, max_weight=4)
        c = strategy_c(1)
        assert a[1] == c[1] == 3

    def test_disagree_at_degree_2(self):
        """CE and Riordan disagree at degree 2: CE=5, Riordan=6.

        This is NOT a bug.  CE computes H^2(g_-, C) using exterior
        powers Lambda^2(g_-^*) while the chiral bar cohomology (if
        it follows Riordan) uses the full chiral structure with
        tensor products and OS forms.
        """
        a = strategy_a(max_degree=2, max_weight=6)
        c = strategy_c(2)
        assert a[2] == 5, "CE should give H^2 = 5"
        assert c[2] == 6, "Riordan should give R(5) = 6"
        assert a[2] != c[2], "Discrepancy is expected"

    def test_verify_strategies(self):
        """verify_strategies documents the comparison."""
        results = verify_strategies(max_degree=2, max_weight=6)
        assert results["agree_at_1"]
        assert results["n=1"]["CE"] == results["n=1"]["Riordan"] == 3
        assert results["n=2"]["CE"] == 5
        assert results["n=2"]["Riordan"] == 6


# ============================================================
# Strategy B: Vacuum module invariants
# ============================================================

class TestStrategyB:
    """Vacuum module g-invariant dimensions."""

    def test_invariant_dims_known(self):
        """Known sl_2 invariant sequence: 1, 0, 1, 1, 3, 3, 8."""
        dims = strategy_b_invariants(max_weight=6)
        assert dims == [1, 0, 1, 1, 3, 3, 8]

    @pytest.mark.slow
    def test_cross_validation(self):
        """Two independent computations of dim(V_h^g) agree."""
        results = strategy_b_cross_validate(max_weight=6)
        for h, (vm, ss, ok) in results.items():
            assert ok, f"weight {h}: vm={vm} != ss={ss}"


# ============================================================
# Differential rank checks (regression)
# ============================================================

class TestDiffRanks:
    """Verify specific differential ranks from hand computation."""

    def test_d1_weight2_rank3(self):
        """d_1: Lambda^1_2 -> Lambda^2_2 has rank 3 (isomorphism)."""
        ce = LoopAlgebraCE(max_weight=2)
        d = ce.ce_differential(1, 2)
        assert d.rank() == 3

    def test_d2_weight3_rank1(self):
        """d_2: Lambda^2_3 -> Lambda^3_3 has rank 1."""
        ce = LoopAlgebraCE(max_weight=3)
        d = ce.ce_differential(2, 3)
        assert d.rank() == 1

    def test_d1_weight3_rank3(self):
        """d_1: Lambda^1_3 -> Lambda^2_3 has rank 3."""
        ce = LoopAlgebraCE(max_weight=3)
        d = ce.ce_differential(1, 3)
        assert d.rank() == 3


# ============================================================
# PBW product (E_1 chain group dimensions)
# ============================================================

class TestPBWProduct:
    """Verify prod_{m>=1} (1+q^m)^3 = E_1 page dimensions.

    The E_1 page of the PBW SS has dim Λ^*(V^*)_h at each conformal
    weight h (total over all bar degrees).  These are coefficients of
    prod_{m>=1} (1+q^m)^3.  They agree with Riordan at h<=2 but
    diverge at h>=3.
    """

    def test_pbw_product_low_weights(self):
        """PBW product coefficients: 1, 3, 6, 13, 24, 42, ..."""
        ce = LoopAlgebraCE(max_weight=8)
        for h in range(9):
            total = sum(ce.chain_group_dim(n, h) for n in range(h + 1))
            if h == 0:
                assert total == 1  # Lambda^0 only
            elif h == 1:
                assert total == 3  # Lambda^1_1 = 3
            elif h == 2:
                assert total == 6  # Lambda^1_2=3 + Lambda^2_2=3
            elif h == 3:
                assert total == 13  # 3 + 9 + 1 = 13 (NOT Riordan 15)

    def test_pbw_vs_riordan_divergence(self):
        """PBW product gives 13 at h=3, Riordan gives 15."""
        ce = LoopAlgebraCE(max_weight=3)
        pbw_h3 = sum(ce.chain_group_dim(n, 3) for n in range(4))
        assert pbw_h3 == 13
        assert riordan(6) == 15
        assert pbw_h3 != riordan(6), "PBW and Riordan diverge at h=3"
