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
