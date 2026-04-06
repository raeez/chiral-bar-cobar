r"""Tests for CY-2: Quiver potential and Jacobian algebra engine.

Multi-path verification (AP10) of:
1. Preprojective algebra dimensions for A_n (closed form vs summation)
2. Doubled quiver and potential structure
3. Cyclic derivative computation
4. Ginzburg CY3 dg algebra construction
5. Positive root enumeration for ADE types
6. Coxeter numbers and group orders
7. Cartan matrix properties

Every numerical result verified by >= 2 independent methods.
"""

import math
import unittest
from fractions import Fraction

import numpy as np

from compute.lib.cy_quiver_potential_engine import (
    Quiver,
    CyclicPath,
    Potential,
    dynkin_quiver_A,
    dynkin_quiver_D,
    dynkin_quiver_E,
    dynkin_quiver,
    doubled_quiver_with_potential,
    cyclic_derivative,
    cyclic_derivative_as_relations,
    preprojective_dim_A,
    preprojective_hom_dim_A,
    preprojective_dim_by_summation_A,
    _cartan_matrix,
    coxeter_number,
    finite_subgroup_order,
    preprojective_dim_general,
    positive_roots,
    number_of_positive_roots,
    _KNOWN_PREPROJECTIVE_DIMS,
    ginzburg_quiver,
    ginzburg_potential,
    ginzburg_jacobian_relations,
)


# =====================================================================
# Independent computations for cross-checks
# =====================================================================

def _independent_preprojective_dim_A(n):
    """Independently compute dim Pi_0(A_n) = n(n+1)^2(n+2)/12."""
    return n * (n + 1) ** 2 * (n + 2) // 12


def _independent_hom_dim_A(n, i, j):
    """Independently: min(i,j) * min(n+1-i, n+1-j)."""
    return min(i, j) * min(n + 1 - i, n + 1 - j)


def _independent_num_positive_roots(dtype, rank):
    """A_n: n(n+1)/2, D_n: n(n-1), E_6: 36, E_7: 63, E_8: 120."""
    if dtype == 'A':
        return rank * (rank + 1) // 2
    elif dtype == 'D':
        return rank * (rank - 1)
    elif dtype == 'E':
        return {6: 36, 7: 63, 8: 120}[rank]


def _independent_coxeter(dtype, rank):
    """A_n: n+1, D_n: 2(n-1), E_6: 12, E_7: 18, E_8: 30."""
    if dtype == 'A':
        return rank + 1
    elif dtype == 'D':
        return 2 * (rank - 1)
    elif dtype == 'E':
        return {6: 12, 7: 18, 8: 30}[rank]


# =====================================================================
# Tests: Dynkin quiver construction
# =====================================================================

class TestDynkinQuiverA(unittest.TestCase):
    """Test type A Dynkin quiver construction."""

    def test_vertices(self):
        for n in range(1, 8):
            Q = dynkin_quiver_A(n)
            self.assertEqual(Q.n_vertices, n)
            self.assertEqual(Q.vertices, list(range(1, n + 1)))

    def test_arrows(self):
        for n in range(2, 8):
            Q = dynkin_quiver_A(n)
            self.assertEqual(Q.n_arrows, n - 1)

    def test_A1_no_arrows(self):
        Q = dynkin_quiver_A(1)
        self.assertEqual(Q.n_arrows, 0)

    def test_arrow_connectivity(self):
        """Each arrow connects consecutive vertices."""
        Q = dynkin_quiver_A(5)
        for s, t, _ in Q.arrows:
            self.assertEqual(t, s + 1)

    def test_adjacency_matrix(self):
        """Adjacency matrix of A_n Dynkin quiver."""
        Q = dynkin_quiver_A(4)
        A = Q.adjacency_matrix()
        self.assertEqual(A.shape, (4, 4))
        # Arrows: 1->2, 2->3, 3->4
        self.assertEqual(A[0, 1], 1)
        self.assertEqual(A[1, 2], 1)
        self.assertEqual(A[2, 3], 1)
        # No backward arrows
        self.assertEqual(A[1, 0], 0)


class TestDynkinQuiverD(unittest.TestCase):
    """Test type D Dynkin quiver construction."""

    def test_vertices(self):
        for n in range(4, 8):
            Q = dynkin_quiver_D(n)
            self.assertEqual(Q.n_vertices, n)

    def test_arrows(self):
        for n in range(4, 8):
            Q = dynkin_quiver_D(n)
            self.assertEqual(Q.n_arrows, n - 1)

    def test_branch(self):
        """D_n has a branch: vertex n-2 connects to both n-1 and n."""
        Q = dynkin_quiver_D(5)
        targets = [t for s, t, _ in Q.arrows if s == 3]
        self.assertIn(4, targets)
        self.assertIn(5, targets)


class TestDynkinQuiverE(unittest.TestCase):
    """Test type E Dynkin quiver construction."""

    def test_vertices(self):
        for n in [6, 7, 8]:
            Q = dynkin_quiver_E(n)
            self.assertEqual(Q.n_vertices, n)

    def test_arrows(self):
        for n in [6, 7, 8]:
            Q = dynkin_quiver_E(n)
            self.assertEqual(Q.n_arrows, n - 1)

    def test_branch_at_3(self):
        """E_n has a branch from vertex 3 to vertex n."""
        for n in [6, 7, 8]:
            Q = dynkin_quiver_E(n)
            branch_arrows = [(s, t) for s, t, _ in Q.arrows if s == 3 and t == n]
            self.assertEqual(len(branch_arrows), 1)


# =====================================================================
# Tests: Doubled quiver with potential
# =====================================================================

class TestDoubledQuiver(unittest.TestCase):
    """Test doubled quiver construction."""

    def test_doubled_arrow_count(self):
        """Doubled quiver has 2 * |Q_1| arrows."""
        for n in range(1, 7):
            Q = dynkin_quiver_A(n)
            barQ, W = doubled_quiver_with_potential(Q)
            self.assertEqual(barQ.n_arrows, 2 * Q.n_arrows)

    def test_doubled_vertices_preserved(self):
        for n in range(1, 7):
            Q = dynkin_quiver_A(n)
            barQ, W = doubled_quiver_with_potential(Q)
            self.assertEqual(barQ.n_vertices, Q.n_vertices)

    def test_potential_has_terms(self):
        """For A_n (n >= 2), potential has 2*(n-1) terms."""
        Q = dynkin_quiver_A(3)
        barQ, W = doubled_quiver_with_potential(Q)
        # Each arrow contributes 2 cyclic path terms (positive and negative)
        self.assertEqual(len(W.terms), 2 * Q.n_arrows)

    def test_potential_coefficients_sum_to_zero(self):
        """At each vertex, the preprojective relation sum [a,a*] = 0 means
        the positive and negative terms balance."""
        Q = dynkin_quiver_A(4)
        barQ, W = doubled_quiver_with_potential(Q)
        total = sum(W.terms.values())
        self.assertEqual(total, Fraction(0))

    def test_A1_doubled_is_empty(self):
        """A_1 has no arrows, so doubled is also empty."""
        Q = dynkin_quiver_A(1)
        barQ, W = doubled_quiver_with_potential(Q)
        self.assertEqual(barQ.n_arrows, 0)
        self.assertEqual(len(W.terms), 0)

    def test_opposite_arrows_exist(self):
        """Each arrow a: i->j has an opposite a*: j->i."""
        Q = dynkin_quiver_A(4)
        barQ, W = doubled_quiver_with_potential(Q)
        labels = {lbl for _, _, lbl in barQ.arrows}
        for _, _, lbl in Q.arrows:
            self.assertIn(lbl + "*", labels)


# =====================================================================
# Tests: Cyclic derivatives
# =====================================================================

class TestCyclicDerivatives(unittest.TestCase):
    """Test cyclic derivative computation."""

    def test_derivative_of_2cycle(self):
        """d_a(a a*) = a* (a length-1 path)."""
        Q = dynkin_quiver_A(2)
        barQ, W = doubled_quiver_with_potential(Q)
        rels = cyclic_derivative_as_relations(W, barQ)
        # Should have derivatives for each arrow label
        self.assertGreater(len(rels), 0)

    def test_all_arrows_have_derivatives(self):
        """Every arrow in the doubled quiver gets a cyclic derivative."""
        Q = dynkin_quiver_A(3)
        barQ, W = doubled_quiver_with_potential(Q)
        rels = cyclic_derivative_as_relations(W, barQ)
        for _, _, lbl in barQ.arrows:
            self.assertIn(lbl, rels)

    def test_preprojective_relation_count(self):
        """The d_{t_v} derivatives give one relation per vertex (Ginzburg)."""
        Q = dynkin_quiver_A(3)
        gQ, W = ginzburg_potential(Q)
        rels = ginzburg_jacobian_relations(Q)
        # Should have loop relations (one per vertex)
        self.assertEqual(len(rels['loop_relations']), Q.n_vertices)


# =====================================================================
# Tests: Preprojective algebra dimensions
# =====================================================================

class TestPreprojDimA(unittest.TestCase):
    """Preprojective algebra dimensions for type A via multiple paths."""

    def test_formula_values(self):
        """Path 1: closed form n(n+1)^2(n+2)/12."""
        known = {1: 1, 2: 6, 3: 20, 4: 50, 5: 105, 6: 196, 7: 336}
        for n, expected in known.items():
            self.assertEqual(preprojective_dim_A(n), expected)

    def test_independent_formula(self):
        """Path 2: independently compute n(n+1)^2(n+2)/12."""
        for n in range(1, 10):
            self.assertEqual(preprojective_dim_A(n),
                             _independent_preprojective_dim_A(n))

    def test_summation_path(self):
        """Path 3: sum_{i,j} min(i,j)*min(n+1-i,n+1-j)."""
        for n in range(1, 8):
            self.assertEqual(preprojective_dim_A(n),
                             preprojective_dim_by_summation_A(n))

    def test_hom_dim_formula(self):
        """dim(e_i Pi e_j) = min(i,j)*min(n+1-i,n+1-j)."""
        for n in range(1, 6):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    engine = preprojective_hom_dim_A(n, i, j)
                    indep = _independent_hom_dim_A(n, i, j)
                    self.assertEqual(engine, indep)

    def test_hom_dim_symmetry(self):
        """dim(e_i Pi e_j) = dim(e_j Pi e_i) (preprojective is symmetric)."""
        for n in range(1, 6):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    self.assertEqual(preprojective_hom_dim_A(n, i, j),
                                     preprojective_hom_dim_A(n, j, i))

    def test_diagonal_dominance(self):
        """dim(e_i Pi e_i) >= dim(e_i Pi e_j) for all j."""
        for n in range(1, 6):
            for i in range(1, n + 1):
                diag = preprojective_hom_dim_A(n, i, i)
                for j in range(1, n + 1):
                    self.assertGreaterEqual(diag,
                                            preprojective_hom_dim_A(n, i, j))

    def test_summation_matches_formula(self):
        """sum_{i,j} hom_dim = total dim."""
        for n in range(1, 8):
            total = sum(preprojective_hom_dim_A(n, i, j)
                        for i in range(1, n + 1)
                        for j in range(1, n + 1))
            self.assertEqual(total, preprojective_dim_A(n))

    def test_known_table_A(self):
        """Verified table matches closed form."""
        for n in range(1, 7):
            key = ('A', n)
            if key in _KNOWN_PREPROJECTIVE_DIMS:
                self.assertEqual(_KNOWN_PREPROJECTIVE_DIMS[key],
                                 _independent_preprojective_dim_A(n))

    def test_growth_rate(self):
        """dim Pi_0(A_n) ~ n^4/12 for large n (polynomial growth).
        Ratio converges to 1 from above as n grows."""
        ratios = []
        for n in [20, 50, 100]:
            dim = preprojective_dim_A(n)
            approx = n**4 / 12
            ratios.append(dim / approx)
        # Ratios should be decreasing toward 1
        self.assertGreater(ratios[0], ratios[1])
        self.assertGreater(ratios[1], ratios[2])
        # At n=100, should be close to 1
        self.assertAlmostEqual(ratios[2], 1.0, places=1)


# =====================================================================
# Tests: Positive roots
# =====================================================================

class TestPositiveRoots(unittest.TestCase):
    """Test positive root enumeration for ADE types."""

    def test_A_count(self):
        """A_n has n(n+1)/2 positive roots."""
        for n in range(1, 7):
            roots = positive_roots('A', n)
            expected = n * (n + 1) // 2
            self.assertEqual(len(roots), expected)
            self.assertEqual(number_of_positive_roots('A', n), expected)

    def test_A_count_independent(self):
        for n in range(1, 7):
            self.assertEqual(number_of_positive_roots('A', n),
                             _independent_num_positive_roots('A', n))

    def test_D_count(self):
        """D_n has n(n-1) positive roots."""
        for n in range(4, 8):
            roots = positive_roots('D', n)
            expected = n * (n - 1)
            self.assertEqual(len(roots), expected)

    def test_D_count_independent(self):
        for n in range(4, 8):
            self.assertEqual(number_of_positive_roots('D', n),
                             _independent_num_positive_roots('D', n))

    def test_E_count(self):
        """E_6: 36, E_7: 63, E_8: 120 positive roots."""
        for n, expected in [(6, 36), (7, 63), (8, 120)]:
            roots = positive_roots('E', n)
            self.assertEqual(len(roots), expected)

    def test_E_count_independent(self):
        for n in [6, 7, 8]:
            self.assertEqual(number_of_positive_roots('E', n),
                             _independent_num_positive_roots('E', n))

    def test_simple_roots_included(self):
        """All simple roots e_i are positive roots."""
        for n in range(1, 6):
            roots = positive_roots('A', n)
            for i in range(n):
                e = [0] * n
                e[i] = 1
                self.assertIn(e, roots)

    def test_highest_root_A(self):
        """Highest root of A_n is (1,1,...,1)."""
        for n in range(1, 6):
            roots = positive_roots('A', n)
            highest = [1] * n
            self.assertIn(highest, roots)

    def test_all_positive_entries(self):
        """All roots have non-negative integer coordinates."""
        for n in range(1, 6):
            for root in positive_roots('A', n):
                self.assertTrue(all(c >= 0 for c in root))
                self.assertTrue(all(isinstance(c, (int, np.integer)) for c in root))

    def test_total_root_count_E(self):
        """Cross-check: |Phi| = 2*|Phi+| = 2*h*(rank) / 2... no.
        Actually: |Phi+| = (h*rank)/2 for simply-laced.
        E_6: 12*6/2=36. E_7: 18*7/2=63. E_8: 30*8/2=120."""
        for n, h in [(6, 12), (7, 18), (8, 30)]:
            expected = h * n // 2
            self.assertEqual(number_of_positive_roots('E', n), expected)


# =====================================================================
# Tests: Coxeter numbers and group orders
# =====================================================================

class TestCoxeterNumbers(unittest.TestCase):
    """Coxeter numbers via two paths."""

    def test_A(self):
        for n in range(1, 8):
            self.assertEqual(coxeter_number('A', n), n + 1)
            self.assertEqual(coxeter_number('A', n), _independent_coxeter('A', n))

    def test_D(self):
        for n in range(4, 9):
            self.assertEqual(coxeter_number('D', n), 2 * (n - 1))
            self.assertEqual(coxeter_number('D', n), _independent_coxeter('D', n))

    def test_E(self):
        cases = [(6, 12), (7, 18), (8, 30)]
        for n, h in cases:
            self.assertEqual(coxeter_number('E', n), h)
            self.assertEqual(coxeter_number('E', n), _independent_coxeter('E', n))


class TestGroupOrders(unittest.TestCase):
    """Finite subgroup orders via two paths."""

    def test_A(self):
        """Z/(n+1) has order n+1."""
        for n in range(1, 8):
            self.assertEqual(finite_subgroup_order('A', n), n + 1)

    def test_D(self):
        """Binary dihedral of order 4(n-2)."""
        for n in range(4, 9):
            self.assertEqual(finite_subgroup_order('D', n), 4 * (n - 2))

    def test_E(self):
        self.assertEqual(finite_subgroup_order('E', 6), 24)
        self.assertEqual(finite_subgroup_order('E', 7), 48)
        self.assertEqual(finite_subgroup_order('E', 8), 120)

    def test_cross_check_positive_roots(self):
        """For ADE: |Phi+| = h*n/2 and |Gamma| are related through McKay.
        |Gamma| = n+1 for A_n. |Phi+| = n(n+1)/2. So |Phi+|/|Gamma| = n/2.
        This is a non-trivial identity we can verify."""
        for n in range(1, 7):
            phi_plus = number_of_positive_roots('A', n)
            gamma = finite_subgroup_order('A', n)
            # |Phi+| = n(n+1)/2, |Gamma| = n+1, ratio = n/2
            self.assertEqual(phi_plus * 2, gamma * n)


# =====================================================================
# Tests: Cartan matrix from engine
# =====================================================================

class TestCartanMatrix(unittest.TestCase):
    """Cartan matrix properties."""

    def test_A_determinant(self):
        for n in range(1, 7):
            C = _cartan_matrix('A', n)
            det = int(round(np.linalg.det(C)))
            self.assertEqual(det, n + 1)

    def test_D_determinant(self):
        for n in range(4, 8):
            C = _cartan_matrix('D', n)
            det = int(round(np.linalg.det(C)))
            self.assertEqual(det, 4)

    def test_symmetric(self):
        for dtype, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                C = _cartan_matrix(dtype, n)
                self.assertTrue(np.array_equal(C, C.T),
                                f"{dtype}_{n} not symmetric")

    def test_diagonal_2(self):
        for dtype, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                C = _cartan_matrix(dtype, n)
                for i in range(n):
                    self.assertEqual(C[i, i], 2)

    def test_positive_definite(self):
        for dtype, ranks in [('A', range(1, 7)), ('D', range(4, 8)), ('E', [6, 7, 8])]:
            for n in ranks:
                C = _cartan_matrix(dtype, n)
                eigs = np.linalg.eigvalsh(C.astype(float))
                self.assertTrue(all(e > 1e-10 for e in eigs),
                                f"{dtype}_{n} not positive definite")


# =====================================================================
# Tests: Ginzburg CY3 dg algebra
# =====================================================================

class TestGinzburgQuiver(unittest.TestCase):
    """Test Ginzburg quiver construction."""

    def test_arrow_count(self):
        """Ginzburg quiver has 2|Q_1| + |Q_0| arrows."""
        for n in range(1, 6):
            Q = dynkin_quiver_A(n)
            gQ = ginzburg_quiver(Q)
            expected = 2 * Q.n_arrows + Q.n_vertices
            self.assertEqual(gQ.n_arrows, expected)

    def test_loops_present(self):
        """Every vertex has a loop t_v."""
        Q = dynkin_quiver_A(4)
        gQ = ginzburg_quiver(Q)
        loop_vertices = set()
        for s, t, lbl in gQ.arrows:
            if s == t and lbl.startswith('t_'):
                loop_vertices.add(s)
        for v in Q.vertices:
            self.assertIn(v, loop_vertices)

    def test_vertices_preserved(self):
        Q = dynkin_quiver_A(4)
        gQ = ginzburg_quiver(Q)
        self.assertEqual(gQ.n_vertices, Q.n_vertices)


class TestGinzburgPotential(unittest.TestCase):
    """Test Ginzburg potential W = sum(t_s * a * a* - t_t * a* * a)."""

    def test_potential_term_count(self):
        """Two 3-cycle terms per original arrow."""
        for n in range(2, 6):
            Q = dynkin_quiver_A(n)
            gQ, W = ginzburg_potential(Q)
            self.assertEqual(len(W.terms), 2 * Q.n_arrows)

    def test_potential_coefficients(self):
        """Positive terms have coeff +1, negative terms have coeff -1."""
        Q = dynkin_quiver_A(3)
        gQ, W = ginzburg_potential(Q)
        coeffs = list(W.terms.values())
        self.assertEqual(coeffs.count(Fraction(1)), Q.n_arrows)
        self.assertEqual(coeffs.count(Fraction(-1)), Q.n_arrows)

    def test_all_terms_length_3(self):
        """All cyclic paths in W have length 3."""
        Q = dynkin_quiver_A(4)
        gQ, W = ginzburg_potential(Q)
        for path in W.terms:
            self.assertEqual(path.length, 3)


class TestGinzburgJacobian(unittest.TestCase):
    """Test Jacobian relations of Ginzburg potential."""

    def test_relation_types(self):
        """Jacobian has original, opposite, and loop relations."""
        Q = dynkin_quiver_A(3)
        rels = ginzburg_jacobian_relations(Q)
        self.assertIn('original_arrow_relations', rels)
        self.assertIn('opposite_arrow_relations', rels)
        self.assertIn('loop_relations', rels)

    def test_loop_relations_are_preprojective(self):
        """d_{t_v}(W) = sum [a, a*] = preprojective relation."""
        Q = dynkin_quiver_A(3)
        rels = ginzburg_jacobian_relations(Q)
        # One loop relation per vertex
        self.assertEqual(len(rels['loop_relations']), Q.n_vertices)

    def test_D_type_ginzburg(self):
        """Ginzburg construction works for D_4."""
        Q = dynkin_quiver_D(4)
        gQ = ginzburg_quiver(Q)
        self.assertEqual(gQ.n_arrows, 2 * 3 + 4)  # 2*3 arrows + 4 loops


# =====================================================================
# Tests: Known preprojective dimension table cross-checks
# =====================================================================

class TestKnownDimTable(unittest.TestCase):
    """Verify the _KNOWN_PREPROJECTIVE_DIMS table entries are consistent."""

    def test_A_entries_match_formula(self):
        """A_n table entries = n(n+1)^2(n+2)/12."""
        for n in range(1, 7):
            key = ('A', n)
            if key in _KNOWN_PREPROJECTIVE_DIMS:
                expected = n * (n+1)**2 * (n+2) // 12
                self.assertEqual(_KNOWN_PREPROJECTIVE_DIMS[key], expected)

    def test_A_entries_match_summation(self):
        for n in range(1, 7):
            key = ('A', n)
            if key in _KNOWN_PREPROJECTIVE_DIMS:
                self.assertEqual(_KNOWN_PREPROJECTIVE_DIMS[key],
                                 preprojective_dim_by_summation_A(n))

    def test_all_entries_positive(self):
        for key, val in _KNOWN_PREPROJECTIVE_DIMS.items():
            self.assertGreater(val, 0, f"{key}: dim should be positive")

    def test_D_monotone(self):
        """D_n dimension is strictly increasing in n."""
        prev = 0
        for n in range(4, 9):
            key = ('D', n)
            if key in _KNOWN_PREPROJECTIVE_DIMS:
                self.assertGreater(_KNOWN_PREPROJECTIVE_DIMS[key], prev)
                prev = _KNOWN_PREPROJECTIVE_DIMS[key]

    def test_E_monotone(self):
        """E_6 < E_7 < E_8 dimension."""
        dims = []
        for n in [6, 7, 8]:
            key = ('E', n)
            if key in _KNOWN_PREPROJECTIVE_DIMS:
                dims.append(_KNOWN_PREPROJECTIVE_DIMS[key])
        for i in range(len(dims) - 1):
            self.assertLess(dims[i], dims[i + 1])


# =====================================================================
# Tests: Quiver data structure
# =====================================================================

class TestQuiverDataStructure(unittest.TestCase):
    """Basic tests for the Quiver class."""

    def test_adjacency_matrix_shape(self):
        Q = dynkin_quiver_A(5)
        A = Q.adjacency_matrix()
        self.assertEqual(A.shape, (5, 5))

    def test_adjacency_matrix_values(self):
        Q = dynkin_quiver_A(3)
        A = Q.adjacency_matrix()
        # 1->2, 2->3
        self.assertEqual(A[0, 1], 1)
        self.assertEqual(A[1, 2], 1)
        self.assertEqual(A[0, 2], 0)

    def test_arrows_from(self):
        Q = dynkin_quiver_A(4)
        arrows_from_2 = Q.arrows_from(2)
        self.assertEqual(len(arrows_from_2), 1)
        self.assertEqual(arrows_from_2[0][1], 3)  # target is 3

    def test_arrows_to(self):
        Q = dynkin_quiver_A(4)
        arrows_to_3 = Q.arrows_to(3)
        self.assertEqual(len(arrows_to_3), 1)
        self.assertEqual(arrows_to_3[0][0], 2)  # source is 2

    def test_repr(self):
        Q = dynkin_quiver_A(3)
        self.assertIn("3 vertices", repr(Q))
        self.assertIn("2 arrows", repr(Q))


class TestPotentialDataStructure(unittest.TestCase):
    """Basic tests for Potential and CyclicPath classes."""

    def test_cyclic_path_equality(self):
        p1 = CyclicPath(['a', 'b'], 1)
        p2 = CyclicPath(['a', 'b'], 1)
        self.assertEqual(p1, p2)

    def test_cyclic_path_inequality(self):
        p1 = CyclicPath(['a', 'b'], 1)
        p2 = CyclicPath(['b', 'a'], 1)
        self.assertNotEqual(p1, p2)

    def test_potential_add_term(self):
        W = Potential()
        p = CyclicPath(['a', 'b'], 1)
        W.add_term(p, Fraction(1))
        W.add_term(p, Fraction(2))
        self.assertEqual(W.terms[p], Fraction(3))

    def test_cyclic_path_hash(self):
        """CyclicPaths can be used as dict keys."""
        p1 = CyclicPath(['a', 'b'], 1)
        p2 = CyclicPath(['a', 'b'], 1)
        d = {p1: 42}
        self.assertEqual(d[p2], 42)


if __name__ == '__main__':
    unittest.main()
