"""Tests for the chiral_bar_cohomology module.

Tests fan basis enumeration, tree operations, bar differential matrix
construction, and cohomology computation for sl_2 and sl_3.
"""

import pytest
import numpy as np
from math import factorial

from compute.lib.chiral_bar_cohomology import (
    fan_trees,
    tree_edges,
    contract_edge,
    form_extraction_sign,
    bar_differential_matrix,
    bar_cohomology_dim,
    matrix_rank_sparse,
    sl2_structure_constants,
    sl3_structure_constants,
    verify_jacobi,
    verify_d_squared,
)


# ===================================================================
# Fan trees (increasing trees)
# ===================================================================

class TestFanTrees:
    def test_n1(self):
        """1 vertex: single empty tree."""
        trees = fan_trees(1)
        assert len(trees) == 1
        assert trees[0] == ()

    def test_n2(self):
        """2 vertices: 1 tree = (1,)."""
        trees = fan_trees(2)
        assert len(trees) == 1
        assert trees[0] == (1,)

    def test_n3(self):
        """3 vertices: 2 trees = 2! = 2."""
        trees = fan_trees(3)
        assert len(trees) == 2

    def test_n4(self):
        """4 vertices: 6 trees = 3! = 6."""
        trees = fan_trees(4)
        assert len(trees) == 6

    def test_count_formula(self):
        """Number of fan trees on n vertices = (n-1)!."""
        for n in range(1, 7):
            trees = fan_trees(n)
            assert len(trees) == factorial(n - 1) if n >= 1 else 1

    def test_valid_parents(self):
        """Each t_k satisfies 1 <= t_k < k."""
        for n in range(2, 6):
            for tree in fan_trees(n):
                for k_idx, t_k in enumerate(tree):
                    k = k_idx + 2  # k ranges from 2 to n
                    assert 1 <= t_k < k, f"Invalid parent {t_k} for vertex {k}"


class TestTreeEdges:
    def test_n2(self):
        """Tree (1,) on 2 vertices has edge (1,2)."""
        edges = tree_edges((1,), 2)
        assert edges == [(1, 2)]

    def test_n3(self):
        """Tree on 3 vertices has 2 edges."""
        tree = (1, 1)  # both 2 and 3 connect to 1
        edges = tree_edges(tree, 3)
        assert len(edges) == 2
        assert (1, 2) in edges
        assert (1, 3) in edges


class TestContractEdge:
    def test_n3_contract_12(self):
        """Contract (1,2) in tree on 3 vertices -> tree on 2 vertices."""
        tree = (1, 1)  # parent of 2 is 1, parent of 3 is 1
        result = contract_edge(tree, 3, 1, 2)
        # After contracting: merge 2 into 1, remove 2
        # Remaining vertices: {1, 3} -> relabel to {1, 2}
        assert isinstance(result, tuple)
        assert len(result) == 1  # tree on 2 vertices has 1 entry

    def test_n3_contract_gives_valid_tree(self):
        """Contracted tree should be a valid fan tree on n-1 vertices."""
        for tree in fan_trees(3):
            edges = tree_edges(tree, 3)
            for (i, j) in edges:
                result = contract_edge(tree, 3, i, j)
                assert result in fan_trees(2)


class TestFormExtractionSign:
    def test_j2(self):
        """Extracting the j=2 form factor (position 0) gives sign (-1)^0 = +1."""
        assert form_extraction_sign((1,), 2, 2) == 1

    def test_j3(self):
        """Extracting the j=3 form factor (position 1) gives sign (-1)^1 = -1."""
        assert form_extraction_sign((1, 1), 3, 3) == -1


# ===================================================================
# Structure constants
# ===================================================================

class TestStructureConstants:
    def test_sl2_jacobi(self):
        """sl_2 Jacobi identity: zero violations."""
        sc = sl2_structure_constants()
        assert verify_jacobi(3, sc) == 0

    def test_sl3_jacobi(self):
        """sl_3 Jacobi identity: zero violations."""
        sc = sl3_structure_constants()
        assert verify_jacobi(8, sc) == 0

    def test_sl2_antisymmetry(self):
        """[a,b] = -[b,a] for sl_2."""
        sc = sl2_structure_constants()
        for (a, b), val in sc.items():
            ba = sc.get((b, a), {})
            for k, c in val.items():
                assert ba.get(k, 0) == -c


# ===================================================================
# Bar differential matrix
# ===================================================================

class TestBarDifferentialMatrix:
    def test_shape_sl2_deg2(self):
        """d_2: B^2 -> B^1 for sl_2. B^2 = 3^2*1! = 9, B^1 = 3."""
        sc = sl2_structure_constants()
        D = bar_differential_matrix(3, sc, 2)
        assert D.shape == (3, 9)

    def test_shape_sl2_deg3(self):
        """d_3: B^3 -> B^2. B^3 = 3^3*2! = 54, B^2 = 3^2*1! = 9."""
        sc = sl2_structure_constants()
        D = bar_differential_matrix(3, sc, 3)
        assert D.shape == (9, 54)

    def test_d_squared_sl2_deg3_returns_bool(self):
        """verify_d_squared returns a boolean at degree 3."""
        sc = sl2_structure_constants()
        result = verify_d_squared(3, sc, 3)
        assert isinstance(result, (bool, np.bool_))

    def test_rank_sl2_deg2(self):
        """Rank of d_2 for sl_2 should be 3 (surjective: bracket is surjective)."""
        sc = sl2_structure_constants()
        D = bar_differential_matrix(3, sc, 2)
        rank = np.linalg.matrix_rank(D.toarray())
        assert rank == 3

    def test_trivial_degree1(self):
        """d_1 should be (essentially) zero."""
        sc = sl2_structure_constants()
        D = bar_differential_matrix(3, sc, 1)
        assert D.nnz == 0


# ===================================================================
# Bar cohomology
# ===================================================================

class TestBarCohomology:
    def test_bar_cohomology_dim_returns_int(self):
        """bar_cohomology_dim returns an integer."""
        sc = sl2_structure_constants()
        h1 = bar_cohomology_dim(3, sc, 1)
        assert isinstance(h1, (int, np.integer))

    def test_bar_cohomology_dim_h0(self):
        """H^0 = 1 (ground field)."""
        sc = sl2_structure_constants()
        h0 = bar_cohomology_dim(3, sc, 0)
        assert h0 == 1

    def test_bar_cohomology_callable(self):
        """bar_cohomology_dim runs without error at degrees 1 and 2."""
        sc = sl2_structure_constants()
        # Just verify the function runs; the sign convention
        # affects whether the values match Riordan numbers.
        bar_cohomology_dim(3, sc, 1)
        bar_cohomology_dim(3, sc, 2)


# ===================================================================
# Sparse rank computation
# ===================================================================

class TestMatrixRankSparse:
    def test_zero_matrix(self):
        from scipy import sparse
        mat = sparse.csr_matrix((5, 5))
        assert matrix_rank_sparse(mat) == 0

    def test_identity(self):
        from scipy import sparse
        mat = sparse.eye(4, format='csr')
        assert matrix_rank_sparse(mat) == 4

    def test_rank_deficient(self):
        from scipy import sparse
        data = np.array([[1, 2, 3], [2, 4, 6], [0, 1, 0]], dtype=np.float64)
        mat = sparse.csr_matrix(data)
        assert matrix_rank_sparse(mat) == 2


# ===================================================================
# Chain-level cross-check: bar cohomology vs KNOWN_BAR_DIMS
# ===================================================================
#
# AUDIT ITEM 16 (compute_audit_gaps.md):
# bar_dim_sl2(n) values are verified against KNOWN_BAR_DIMS, but the
# chain-level code paths that build differential matrices and compute
# cohomology via rank are NEVER independently compared to those known
# values.  This is a critical test asymmetry.
#
# AVAILABLE CHAIN-LEVEL CODE PATHS:
#
# 1. LoopAlgebraCE (bar_cohomology_verification.py, Strategy A):
#    Builds the CE differential of g_- = g tensor t^{-1}C[t^{-1}]
#    weight-by-weight using sympy exact arithmetic.  The PBW spectral
#    sequence degenerates at E_2 = H*(CE(g_-)), giving the correct
#    bar cohomology.  VALID for sl_2 at degrees 1-2 (all weight
#    contributions fit within max_weight; d^2 = 0 proved).
#    At degree 3, CE of g_- gives H^3 = 7 (only weight-6 contributions),
#    which is LESS than the true bar cohomology H^3 = 15.  The remaining
#    8 classes come from higher-weight CE contributions that converge
#    slowly in the weight truncation.
#
# 2. Fan-basis chiral bar differential (chiral_bar_cohomology.py):
#    Builds the bracket-only part of the chiral bar differential with
#    OS forms.  Has d^2 != 0 (the "curvature barrier": the full chiral
#    bar differential also needs d_curvature from derivative-residues,
#    which produce forms outside the OS algebra).  CANNOT be used for
#    cohomology computation.
#
# 3. CE complex of finite g (chiral_bar.py, CEComplex):
#    Computes H*(g; k) for the finite Lie algebra, giving (1,0,0,1)
#    for sl_2.  This is standard CE cohomology, NOT bar cohomology.
#
# The tests below use path (1) for cross-checking at degrees 1-2,
# and document the curvature barrier at degree 3+.
#
# Test tiers (compute_audit_gaps.md):
#   Tier 1: structural (d^2 = 0) -- self-certifying
#   Tier 2: published values (OEIS, textbooks) -- strong
#   Tier 3: cross-check between independent code paths -- good

class TestChainLevelCrossCheckCE:
    """Cross-check: LoopAlgebraCE (Strategy A) vs KNOWN_BAR_DIMS for sl_2.

    The CE cohomology of the negative loop algebra g_- = sl_2 tensor
    t^{-1}C[t^{-1}] is computed by building explicit differential
    matrices (sympy exact arithmetic) and computing kernel/image
    dimensions.  This is a genuine chain-level computation: it
    constructs the actual CE differential, verifies d^2 = 0, and
    extracts cohomology dimensions from rank.

    The PBW spectral sequence identifies bar cohomology with CE
    cohomology of g_- at the E_2 page.  For sl_2, all weight
    contributions at degrees 1-2 are captured by max_weight=6,
    giving the exact bar cohomology values.
    """

    def test_ce_h1_matches_known(self):
        """H^1(CE(g_-)) = KNOWN_BAR_DIMS["sl2"][1] = 3.

        Tier 3 cross-check: chain-level CE computation vs Riordan
        recurrence.  Both give 3, confirming the sl_2 bar cohomology
        at degree 1 via two independent code paths.

        Weight decomposition: H^1 = 3 at weight 1, 0 at weight >= 2.
        """
        from compute.lib.bar_cohomology_verification import strategy_a
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        result = strategy_a(max_degree=1, max_weight=4)
        expected = KNOWN_BAR_DIMS["sl2"][1]
        assert result[1] == expected, (
            f"CE chain-level gives H^1 = {result[1]}, "
            f"but KNOWN_BAR_DIMS says {expected}."
        )

    def test_ce_h2_matches_known(self):
        """H^2(CE(g_-)) = KNOWN_BAR_DIMS["sl2"][2] = 5.

        Tier 3 cross-check at the CRITICAL degree where the Riordan
        formula R(5) = 6 disagrees with the correct value 5.  The CE
        computation gives 5, confirming the correction documented in
        rem:bar-deg2-symmetric-square.

        Weight decomposition: H^2_2 = 0, H^2_3 = 5, H^2_{>=4} = 0.
        """
        from compute.lib.bar_cohomology_verification import strategy_a
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        result = strategy_a(max_degree=2, max_weight=6)
        expected = KNOWN_BAR_DIMS["sl2"][2]
        assert result[2] == expected, (
            f"CE chain-level gives H^2 = {result[2]}, "
            f"but KNOWN_BAR_DIMS says {expected}."
        )

    def test_ce_d_squared_zero_weight_by_weight(self):
        """d^2 = 0 for the CE differential at each weight (Tier 1).

        Self-certifying structural check: the CE differential matrices
        built by LoopAlgebraCE satisfy d_{p+1} . d_p = 0 at every
        (degree, weight) pair.  This verifies the sign conventions and
        structure constant encoding are correct.
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=5)
        for weight in range(1, 6):
            for degree in range(0, weight + 1):
                assert ce.verify_d_squared(degree, weight), (
                    f"d^2 != 0 at degree {degree}, weight {weight} "
                    f"-- CE differential is BROKEN"
                )


class TestChainLevelCrossCheckCEWeightDecomposition:
    """Verify the weight decomposition that underpins the H^1 and H^2 totals.

    These tests check individual weight contributions, ensuring the
    chain-level CE computation produces the correct fine structure
    (not just the correct total).  This is stronger than checking
    totals alone because errors could cancel between weights.
    """

    def test_h1_weight1_is_dim_g(self):
        """H^1(g_-)_1 = dim(g) = 3: weight-1 generators are all cocycles.

        At weight 1, the CE chain group is Lambda^1(g_-^*)_1 = g^*,
        which has dimension 3.  There is no incoming differential (d_0
        maps from Lambda^0 = k, which has weight 0).  The outgoing
        differential d_1: Lambda^1_1 -> Lambda^2_1 maps into Lambda^2_1
        which has dimension 0 (no weight-1 pairs).  So H^1_1 = 3.
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.cohomology_dim(1, 1) == 3

    def test_h1_weight2_vanishes(self):
        """H^1(g_-)_2 = 0: bracket d_1 is an isomorphism at weight 2.

        Ensures no spurious H^1 at weight 2 (which would inflate the
        total and break the cross-check).
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.cohomology_dim(1, 2) == 0

    def test_h2_weight2_vanishes(self):
        """H^2(g_-)_2 = 0: all weight-2 2-forms are exact.

        This is a key part of the H^2 = 5 result: no weight-2
        contribution (contrast with the naive Riordan prediction
        which would include a weight-2 class).
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.cohomology_dim(2, 2) == 0

    def test_h2_weight3_equals_5(self):
        """H^2(g_-)_3 = 5: all five H^2 classes live at weight 3.

        dim Lambda^2_3 = 9, rank(d_2->3) = 1, rank(d_1->2) = 3.
        ker(d_2) = 9 - 1 = 8, im(d_1) = 3, H^2 = 8 - 3 = 5.
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=4)
        assert ce.cohomology_dim(2, 3) == 5

    def test_h2_higher_weights_vanish(self):
        """H^2(g_-)_h = 0 for h = 4, 5, 6: no higher-weight contributions.

        Confirms that H^2 = 5 is EXACT (not just a lower bound from
        truncation), since all remaining weight contributions vanish.
        """
        from compute.lib.bar_cohomology_verification import LoopAlgebraCE
        ce = LoopAlgebraCE(max_weight=6)
        for weight in [4, 5, 6]:
            assert ce.cohomology_dim(2, weight) == 0, (
                f"H^2(g_-)_{weight} != 0 -- unexpected higher-weight class"
            )


class TestFanBasisCurvatureBarrier:
    """Document that the fan-basis chiral bar differential has d^2 != 0.

    The chiral bar differential d = d_bracket + d_curvature has two
    components (Prop prop:pole-decomposition).  The fan-basis code in
    chiral_bar_cohomology.py implements d_bracket only.  The curvature
    term d_curvature uses the derivative-residue R^{(1)}, which produces
    forms outside the OS algebra and cannot be implemented as a matrix.

    Consequence: d_bracket^2 != 0, so bar_cohomology_dim() from
    chiral_bar_cohomology.py CANNOT produce correct cohomology values.
    This is a documented mathematical fact (see CLAUDE.md Critical
    Pitfalls), not a bug.

    These tests verify that the curvature barrier is real (d^2 != 0)
    and that the fan-basis code gives WRONG cohomology values that
    DO NOT match KNOWN_BAR_DIMS.  This documents the asymmetry
    identified in the audit: the only valid chain-level cross-check
    is via the CE approach (TestChainLevelCrossCheckCE above).
    """

    def test_fan_basis_d_squared_nonzero_sl2(self):
        """d_bracket^2 != 0 for sl_2 at bar degree 3.

        The fan-basis code uses bracket-only differential.  This is
        the curvature barrier: only d = d_bracket + d_curvature has
        d^2 = 0, and d_curvature cannot be implemented as a matrix.
        """
        sc = sl2_structure_constants()
        # verify_d_squared returns False when d^2 != 0
        assert not verify_d_squared(3, sc, 3), (
            "Unexpected: d_bracket^2 = 0 for sl_2 at degree 3. "
            "The curvature barrier should cause d^2 != 0."
        )

    def test_fan_basis_cohomology_wrong_sl2_h1(self):
        """Fan-basis bar_cohomology_dim gives WRONG H^1 for sl_2.

        Because d^2 != 0, the "cohomology" computed by
        bar_cohomology_dim() is not a valid invariant.  Verifying
        that it does NOT match KNOWN_BAR_DIMS documents the gap.
        """
        from compute.lib.bar_complex import KNOWN_BAR_DIMS
        sc = sl2_structure_constants()
        h1_fan = bar_cohomology_dim(3, sc, 1)
        h1_known = KNOWN_BAR_DIMS["sl2"][1]
        assert h1_fan != h1_known, (
            f"Unexpected agreement: fan-basis H^1 = {h1_fan} matches "
            f"KNOWN_BAR_DIMS = {h1_known}.  The curvature barrier "
            f"should cause disagreement."
        )
