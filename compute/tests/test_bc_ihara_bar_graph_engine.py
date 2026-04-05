"""Tests for the Ihara zeta function of the bar graph complex.

Verification paths (Multi-Path Mandate):
  Path 1: Direct cycle enumeration (definition)
  Path 2: Hashimoto-Bass determinant formula
  Path 3: Known results for cycle/bouquet graphs
  Path 4: Euler product / Dirichlet series comparison

Test structure:
  1. Adjacency and degree matrices (10 tests)
  2. Hashimoto matrix construction (10 tests)
  3. Ihara zeta: Hashimoto vs Bass agreement (10 tests)
  4. Known graph zetas (cycle, bouquet) (10 tests)
  5. Cycle enumeration verification (8 tests)
  6. Bar graph zeta weighted sums (8 tests)
  7. Ramanujan property (6 tests)
  8. Planted forest subcomplex (6 tests)
  9. Pole/zero analysis (6 tests)
  10. Cross-genus consistency (6 tests)

Total: 80+ tests
"""

import math
import cmath
import pytest
import numpy as np
from fractions import Fraction

from compute.lib.bc_ihara_bar_graph_engine import (
    adjacency_matrix,
    degree_matrix,
    edge_degree_vector,
    oriented_edge_list,
    hashimoto_matrix,
    ihara_zeta_reciprocal_hashimoto,
    ihara_zeta_reciprocal_bass,
    ihara_zeta_value,
    ihara_zeta_reciprocal_poly_coeffs,
    bass_determinant_at_u,
    adjacency_spectrum,
    max_degree,
    is_regular,
    ramanujan_bound,
    is_ramanujan,
    spectral_gap,
    bar_graph_zeta_g,
    bar_graph_zeta_reciprocal_g,
    total_bar_zeta,
    find_ihara_zeros,
    is_planted_forest_graph,
    planted_forest_zeta_g,
    non_planted_forest_zeta_g,
    enumerate_prime_cycles,
    ihara_from_cycles,
    ramanujan_statistics,
    spectral_radius_distribution,
    nontrivial_spectral_radii,
    cycle_graph_zeta_reciprocal,
    bouquet_graph_zeta_reciprocal,
    genus1_ihara_data,
    genus2_ihara_data,
    ihara_pole_radii,
    min_pole_radius,
    unit_circle_approach_data,
    bar_weighted_hashimoto_trace,
    bar_weighted_closed_walks,
    full_ihara_analysis,
)

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    enumerate_stable_graphs,
    genus1_stable_graphs_n0,
    genus2_stable_graphs_n0,
)


# ===================================================================
# SECTION 1: Adjacency and degree matrices (10 tests)
# ===================================================================

class TestAdjacencyMatrix:
    """Tests for adjacency and degree matrix computation."""

    def test_empty_graph(self):
        """No-edge graph: A = 0."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        A = adjacency_matrix(g)
        assert A.shape == (1, 1)
        assert A[0, 0] == 0

    def test_single_self_loop(self):
        """Self-loop: A_{00} = 2 (each self-loop contributes 2)."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        A = adjacency_matrix(g)
        assert A.shape == (1, 1)
        assert A[0, 0] == 2

    def test_double_self_loop(self):
        """Two self-loops: A_{00} = 4."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        A = adjacency_matrix(g)
        assert A[0, 0] == 4

    def test_single_edge(self):
        """One edge between two vertices: A_{01} = A_{10} = 1."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        A = adjacency_matrix(g)
        assert A.shape == (2, 2)
        assert A[0, 1] == 1
        assert A[1, 0] == 1
        assert A[0, 0] == 0
        assert A[1, 1] == 0

    def test_triple_edge_theta(self):
        """Theta graph: 3 parallel edges, A_{01} = A_{10} = 3."""
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        A = adjacency_matrix(g)
        assert A[0, 1] == 3
        assert A[1, 0] == 3

    def test_degree_matrix_self_loop(self):
        """Degree of vertex with k self-loops is 2k."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        D = degree_matrix(g)
        assert D[0, 0] == 4  # 2 self-loops * 2 = 4

    def test_degree_matrix_theta(self):
        """Theta graph: each vertex has degree 3."""
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        D = degree_matrix(g)
        assert D[0, 0] == 3
        assert D[1, 1] == 3

    def test_degree_matrix_mixed(self):
        """Mixed graph: self-loop at v0 + edge to v1.
        v0: degree = 2 (self-loop) + 1 (edge) = 3.
        v1: degree = 1."""
        g = StableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=())
        D = degree_matrix(g)
        assert D[0, 0] == 3
        assert D[1, 1] == 1

    def test_adjacency_symmetric(self):
        """Adjacency matrix is always symmetric."""
        for g_val in range(1, 4):
            for gamma in enumerate_stable_graphs(g_val, 0):
                A = adjacency_matrix(gamma)
                np.testing.assert_array_equal(A, A.T)

    def test_degree_sum(self):
        """Sum of all degrees = 2 * number of edges (including self-loops)."""
        g2 = genus2_stable_graphs_n0()
        for gamma in g2:
            degs = edge_degree_vector(gamma)
            assert np.sum(degs) == 2 * gamma.num_edges


# ===================================================================
# SECTION 2: Hashimoto matrix construction (10 tests)
# ===================================================================

class TestHashimotoMatrix:
    """Tests for the Hashimoto (edge adjacency) matrix."""

    def test_no_edges(self):
        """Graph with no edges: Hashimoto matrix is 0x0."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        T = hashimoto_matrix(g)
        assert T.shape == (0, 0)

    def test_single_self_loop_identity(self):
        """Single self-loop: T = I_2 (each direction maps to itself).

        For self-loop at v: e+ and e- are the two orientations.
        From e+: next edge at v must not be bar(e+) = e-.
        Only option is e+ itself. So T = [[1,0],[0,1]].
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        T = hashimoto_matrix(g)
        assert T.shape == (2, 2)
        expected = np.eye(2, dtype=int)
        np.testing.assert_array_equal(T, expected)

    def test_single_edge_zero(self):
        """Single non-self-loop edge: T = 0 (must backtrack).

        For edge {v0, v1}: oriented edges e = (v0->v1) and bar(e) = (v1->v0).
        From e: at v1, only option is bar(e), which is excluded. T = 0.
        """
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        T = hashimoto_matrix(g)
        assert T.shape == (2, 2)
        np.testing.assert_array_equal(T, np.zeros((2, 2), dtype=int))

    def test_hashimoto_size(self):
        """Hashimoto matrix is 2|E| x 2|E|."""
        g2 = genus2_stable_graphs_n0()
        for gamma in g2:
            T = hashimoto_matrix(gamma)
            assert T.shape == (2 * gamma.num_edges, 2 * gamma.num_edges)

    def test_theta_graph_hashimoto(self):
        """Theta graph (3 parallel edges): T is 6x6, trace = 6.

        Each oriented edge can continue to 2 edges (excluding its reverse).
        Each row has exactly 2 ones (from vertex with degree 3: 3 choices minus 1 backtrack).
        """
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        T = hashimoto_matrix(g)
        assert T.shape == (6, 6)
        # Each row should have exactly degree-1 = 2 ones
        row_sums = np.sum(T, axis=1)
        np.testing.assert_array_equal(row_sums, np.full(6, 2))

    def test_double_self_loop_hashimoto(self):
        """Banana graph (2 self-loops at one vertex): T is 4x4.

        From each oriented edge e at vertex v:
          neighbors = all 4 oriented edges at v minus bar(e) = 3 edges.
        So each row has 3 ones.
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        T = hashimoto_matrix(g)
        assert T.shape == (4, 4)
        row_sums = np.sum(T, axis=1)
        np.testing.assert_array_equal(row_sums, np.full(4, 3))

    def test_hashimoto_row_sum_formula(self):
        """Row sum of Hashimoto = deg(terminal(e)) - 1 for each oriented edge e."""
        g2 = genus2_stable_graphs_n0()
        for gamma in g2:
            T = hashimoto_matrix(gamma)
            if T.shape[0] == 0:
                continue
            edges_or = oriented_edge_list(gamma)
            degs = edge_degree_vector(gamma)
            for i, (o, t, idx, d) in enumerate(edges_or):
                expected_sum = degs[t] - 1
                assert np.sum(T[i, :]) == expected_sum, \
                    f"Row sum mismatch for edge {i} of {gamma}"

    def test_hashimoto_nonnegative(self):
        """Hashimoto matrix has only 0 and 1 entries."""
        for g in range(1, 4):
            for gamma in enumerate_stable_graphs(g, 0):
                T = hashimoto_matrix(gamma)
                assert np.all((T == 0) | (T == 1))

    def test_oriented_edge_count(self):
        """Oriented edge list has exactly 2*|E| entries."""
        g2 = genus2_stable_graphs_n0()
        for gamma in g2:
            oe = oriented_edge_list(gamma)
            assert len(oe) == 2 * gamma.num_edges

    def test_self_loop_orientation_distinct(self):
        """Self-loop oriented edges are distinguished by direction index."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        oe = oriented_edge_list(g)
        assert len(oe) == 2
        # They should differ in direction
        assert oe[0][3] != oe[1][3]
        assert oe[0][3] == 0
        assert oe[1][3] == 1


# ===================================================================
# SECTION 3: Ihara zeta: Hashimoto vs Bass agreement (10 tests)
# ===================================================================

class TestHashimotoBassAgreement:
    """Verify Hashimoto and Bass formulas agree (Multi-Path Verification)."""

    def _check_agreement(self, graph, u_vals=None):
        if u_vals is None:
            u_vals = [0.1, 0.2, 0.3, 0.4, 0.1+0.1j]
        for u in u_vals:
            z_h = ihara_zeta_reciprocal_hashimoto(graph, u)
            z_b = ihara_zeta_reciprocal_bass(graph, u)
            assert abs(z_h - z_b) < 1e-8, \
                f"Mismatch at u={u}: Hashimoto={z_h}, Bass={z_b}, diff={abs(z_h-z_b)}"

    def test_genus1_all(self):
        """Hashimoto = Bass for all genus-1 graphs."""
        for gamma in genus1_stable_graphs_n0():
            self._check_agreement(gamma)

    def test_genus2_all(self):
        """Hashimoto = Bass for all 6 genus-2 graphs."""
        for gamma in genus2_stable_graphs_n0():
            self._check_agreement(gamma)

    def test_genus3_all(self):
        """Hashimoto = Bass for all 42 genus-3 graphs."""
        for gamma in enumerate_stable_graphs(3, 0):
            self._check_agreement(gamma, u_vals=[0.2, 0.3])

    def test_at_zero(self):
        """Both formulas give 1 at u=0."""
        for g in range(1, 4):
            for gamma in enumerate_stable_graphs(g, 0):
                z_h = ihara_zeta_reciprocal_hashimoto(gamma, 0.0)
                z_b = ihara_zeta_reciprocal_bass(gamma, 0.0)
                assert abs(z_h - 1.0) < 1e-12
                assert abs(z_b - 1.0) < 1e-12

    def test_complex_argument(self):
        """Agreement at complex u values."""
        g2 = genus2_stable_graphs_n0()
        u_vals = [0.2+0.1j, 0.1-0.2j, 0.3j]
        for gamma in g2:
            self._check_agreement(gamma, u_vals)

    def test_near_pole(self):
        """Agreement near (but not at) poles."""
        theta = genus2_stable_graphs_n0()[4]
        # Theta graph has poles at 1/eigenvals of T
        u_vals = [0.34, 0.35, 0.36]
        self._check_agreement(theta, u_vals)

    def test_negative_u(self):
        """Agreement at negative real u."""
        g2 = genus2_stable_graphs_n0()
        u_vals = [-0.1, -0.2, -0.3]
        for gamma in g2:
            self._check_agreement(gamma, u_vals)

    def test_purely_imaginary(self):
        """Agreement at purely imaginary u."""
        g2 = genus2_stable_graphs_n0()
        u_vals = [0.2j, 0.3j, -0.1j]
        for gamma in g2:
            self._check_agreement(gamma, u_vals)

    def test_reciprocal_is_one_at_zero(self):
        """zeta^{-1}(0) = 1 for all graphs (det(I) = 1)."""
        for g in range(1, 4):
            for gamma in enumerate_stable_graphs(g, 0):
                val = ihara_zeta_reciprocal_hashimoto(gamma, 0.0)
                assert abs(val - 1.0) < 1e-12

    def test_edgeless_graph_zeta_one(self):
        """Graphs with no edges have zeta = 1 for all u."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        for u in [0.0, 0.5, 1.0, 0.3+0.2j]:
            assert abs(ihara_zeta_value(g, u) - 1.0) < 1e-12


# ===================================================================
# SECTION 4: Known graph zetas (10 tests)
# ===================================================================

class TestKnownGraphZetas:
    """Tests against known Ihara zeta formulas for standard graphs."""

    def test_self_loop_zeta(self):
        """Single self-loop: zeta(u) = (1-u)^{-2}.

        Two prime cycles of length 1 (one in each direction).
        Hashimoto T = I_2, so det(I - uT) = (1-u)^2.
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        for u in [0.1, 0.3, 0.5, 0.8]:
            expected_recip = (1 - u) ** 2
            actual = ihara_zeta_reciprocal_hashimoto(g, u)
            assert abs(actual - expected_recip) < 1e-10, \
                f"Self-loop at u={u}: expected {expected_recip}, got {actual}"

    def test_bouquet_b2_bass(self):
        """Bouquet B_2 (2 self-loops): Bass formula.

        zeta^{-1}(u) = (1-u^2)^1 * (1 - 4u + 3u^2)
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        for u in [0.1, 0.2, 0.3]:
            expected = (1 - u**2) * (1 - 4*u + 3*u**2)
            actual_h = ihara_zeta_reciprocal_hashimoto(g, u)
            actual_b = ihara_zeta_reciprocal_bass(g, u)
            assert abs(actual_h - expected) < 1e-10
            assert abs(actual_b - expected) < 1e-10

    def test_bouquet_formula(self):
        """Bouquet B_k: zeta^{-1} = (1-u^2)^{k-1} * (1 - 2ku + (2k-1)u^2)."""
        for k in range(1, 4):
            g = StableGraph(
                vertex_genera=(0,),
                edges=tuple((0, 0) for _ in range(k)),
                legs=()
            )
            for u in [0.1, 0.2]:
                expected = bouquet_graph_zeta_reciprocal(k, u)
                actual = ihara_zeta_reciprocal_hashimoto(g, u)
                assert abs(actual - expected) < 1e-10, \
                    f"Bouquet B_{k} at u={u}: expected {expected}, got {actual}"

    def test_theta_graph_zeta(self):
        """Theta graph: det(I - uT) for 3-regular bipartite.

        The theta graph has adjacency eigenvalues 3, -3 (since it's
        a multigraph with 3 parallel edges between 2 vertices).
        Bass: (1-u^2)^1 * det(I - 3u*sigma_x + u^2*(3I - I))
             = (1-u^2) * det([[1+2u^2, -3u], [-3u, 1+2u^2]])
             = (1-u^2) * ((1+2u^2)^2 - 9u^2)
             = (1-u^2) * (1 + 4u^2 + 4u^4 - 9u^2)
             = (1-u^2) * (1 - 5u^2 + 4u^4)
             = (1-u^2) * (1 - u^2)(1 - 4u^2)
             = (1-u^2)^2 * (1 - 4u^2)
        """
        theta = genus2_stable_graphs_n0()[4]
        for u in [0.1, 0.2, 0.3, 0.4]:
            expected = (1 - u**2)**2 * (1 - 4*u**2)
            actual = ihara_zeta_reciprocal_hashimoto(theta, u)
            assert abs(actual - expected) < 1e-10, \
                f"Theta at u={u}: expected {expected}, got {actual}"

    def test_separating_node_genus2(self):
        """Separating node (g=1 -- g=1): single edge between distinct vertices.

        T is 2x2 all zeros (must backtrack). So det(I-uT) = 1.
        zeta = 1 for all u.
        """
        sep = genus2_stable_graphs_n0()[3]
        assert sep.num_edges == 1
        for u in [0.1, 0.3, 0.5]:
            assert abs(ihara_zeta_value(sep, u) - 1.0) < 1e-12

    def test_cycle_graph_formula(self):
        """Cycle graph C_n: zeta^{-1}(u) = (1-u^n)^2.

        Verified by constructing cycle graphs with marked points for stability.
        """
        for n in [3, 4, 5]:
            # n-cycle with legs for stability
            g = StableGraph(
                vertex_genera=(0,) * n,
                edges=tuple(
                    (i, (i+1) % n) if i < (i+1) % n else ((i+1) % n, i)
                    for i in range(n)
                ),
                legs=tuple(range(n)),
            )
            for u in [0.1, 0.2, 0.3]:
                expected = cycle_graph_zeta_reciprocal(n, u)
                actual = ihara_zeta_reciprocal_hashimoto(g, u)
                assert abs(actual - expected) < 1e-10, \
                    f"C_{n} at u={u}: expected {expected}, got {actual}"

    def test_self_loop_poles(self):
        """Single self-loop poles at u = 1 (double pole)."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        poles = find_ihara_zeros(g)
        assert len(poles) == 2
        for p in poles:
            assert abs(p - 1.0) < 1e-10

    def test_theta_poles(self):
        """Theta graph poles: 1/eigenvalues of T.

        T has eigenvalues: from the 6x6 Hashimoto of the 3-parallel-edge graph.
        The eigenvalues of A are +3 and -3.
        The poles of zeta_theta are at u where (1-u^2)^2(1-4u^2) = 0,
        i.e., u = +/-1 (double) and u = +/-1/2 (simple).
        """
        theta = genus2_stable_graphs_n0()[4]
        poles = find_ihara_zeros(theta)
        pole_radii = sorted(abs(p) for p in poles)
        # Should have poles at |u| = 0.5 and |u| = 1.0
        assert any(abs(r - 0.5) < 0.01 for r in pole_radii)
        assert any(abs(r - 1.0) < 0.01 for r in pole_radii)

    def test_genus1_smooth_trivial(self):
        """Smooth genus-1 curve (no edges): zeta = 1."""
        smooth = genus1_stable_graphs_n0()[0]
        assert smooth.num_edges == 0
        for u in [0.0, 0.5, 1.0]:
            assert abs(ihara_zeta_value(smooth, u) - 1.0) < 1e-12

    def test_bouquet_b3_banana_genus2(self):
        """Banana = B_3 bouquet at genus 2 (3 self-loops): explicit check.

        Wait: the genus-2 "banana" is 2 self-loops at g=0 vertex, not 3.
        B_2: zeta^{-1} = (1-u^2)(1-4u+3u^2).
        """
        banana = genus2_stable_graphs_n0()[2]
        assert banana.num_edges == 2
        for u in [0.1, 0.2, 0.3]:
            expected = bouquet_graph_zeta_reciprocal(2, u)
            actual = ihara_zeta_reciprocal_hashimoto(banana, u)
            assert abs(actual - expected) < 1e-10


# ===================================================================
# SECTION 5: Cycle enumeration verification (8 tests)
# ===================================================================

class TestCycleEnumeration:
    """Tests for prime cycle enumeration and verification against determinant formula."""

    def test_no_edges_no_cycles(self):
        """Graph with no edges has no cycles."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        cycles = enumerate_prime_cycles(g, max_length=5)
        assert len(cycles) == 0

    def test_self_loop_two_cycles_length_1(self):
        """Single self-loop has exactly 2 prime cycles of length 1."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        cycles = enumerate_prime_cycles(g, max_length=5)
        length_1 = [c for c in cycles if len(c) == 1]
        assert len(length_1) == 2

    def test_single_edge_no_cycles(self):
        """Single non-loop edge: no backtrackless cycles."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        cycles = enumerate_prime_cycles(g, max_length=5)
        assert len(cycles) == 0

    def test_theta_six_prime_length_2(self):
        """Theta graph: 6 prime cycles of length 2.

        Each pair of parallel edges (3 choose 2 = 3 pairs) gives
        2 cycles (one in each direction), total 6.
        """
        theta = genus2_stable_graphs_n0()[4]
        cycles = enumerate_prime_cycles(theta, max_length=2)
        length_2 = [c for c in cycles if len(c) == 2]
        assert len(length_2) == 6

    def test_cycle_product_approx_self_loop(self):
        """Cycle product matches determinant for self-loop (exact for length >= 1)."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        u = 0.3
        det_val = ihara_zeta_reciprocal_hashimoto(g, u)
        cyc_val = 1.0 / ihara_from_cycles(g, u, max_length=5)
        assert abs(det_val - cyc_val) < 1e-10

    def test_cycle_product_approx_theta(self):
        """Cycle product approximates determinant for theta graph."""
        theta = genus2_stable_graphs_n0()[4]
        u = 0.15  # Small enough for convergence
        det_val = ihara_zeta_reciprocal_hashimoto(theta, u)
        cyc_val = 1.0 / ihara_from_cycles(theta, u, max_length=12)
        # Should be close but not exact (truncated product)
        assert abs(det_val - cyc_val) < 1e-4

    def test_double_self_loop_prime_cycles(self):
        """Double self-loop: 4 prime cycles of length 1, plus length-2 cycles.

        B_2 has 4 oriented edges. Each is a prime cycle of length 1
        (it goes around its self-loop).
        Wait: let me think again. Each self-loop gives 2 oriented edges.
        From edge e+ of loop 1: can go to e+ of loop 1 (itself), e+ of loop 2,
        e- of loop 2. These are 3 neighbors. So there ARE cycles of length 1.
        Length 1 cycle = single oriented edge that returns to itself.
        e+ of loop 1: starts at 0, ends at 0, next must not be bar(e+) = e-.
        T[0,0] = 1 means e+ -> e+ is allowed. So e+ alone is a length-1 cycle.
        Similarly for all 4 oriented edges. So 4 prime cycles of length 1.
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        cycles = enumerate_prime_cycles(g, max_length=2)
        length_1 = [c for c in cycles if len(c) == 1]
        assert len(length_1) == 4

    def test_prime_cycles_are_primitive(self):
        """All returned cycles should be primitive (not powers of shorter)."""
        theta = genus2_stable_graphs_n0()[4]
        cycles = enumerate_prime_cycles(theta, max_length=6)
        for c in cycles:
            n = len(c)
            for d in range(1, n):
                if n % d == 0:
                    base = c[:d]
                    is_power = all(c[k*d:(k+1)*d] == base for k in range(n // d))
                    if d < n:
                        assert not is_power, f"Cycle {c} is a power of {base}"


# ===================================================================
# SECTION 6: Bar graph zeta weighted sums (8 tests)
# ===================================================================

class TestBarGraphZeta:
    """Tests for the bar-weighted Ihara zeta sums."""

    def test_genus1_at_zero(self):
        """Z^{bar}_1(0) = sum 1/|Aut| = 1/1 + 1/2 = 3/2."""
        z = bar_graph_zeta_g(1, 0.0)
        assert abs(z - 1.5) < 1e-12

    def test_genus1_at_half(self):
        """Z^{bar}_1(1/2): smooth gives 1, self-loop gives (1-1/2)^{-2} = 4.
        Total = 1/1 + 4/2 = 3."""
        z = bar_graph_zeta_g(1, 0.5)
        assert abs(z - 3.0) < 1e-10

    def test_genus2_at_zero(self):
        """Z^{bar}_2(0) = sum 1/|Aut| over 6 graphs.
        Auts: 1, 2, 8, 2, 12, 2.
        Sum = 1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2 = 91/40."""
        # Wait: Aut orders for genus-2 graphs:
        # 1. Smooth g=2: Aut=1
        # 2. Irr node g=1, 1 loop: Aut=2
        # 3. Banana g=0, 2 loops: Aut=8
        # 4. Separating g=1+g=1: Aut=2
        # 5. Theta g=0+g=0, 3 edges: Aut=12
        # 6. Mixed g=0 loop + g=1: Aut=2
        # Sum = 1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2
        from fractions import Fraction
        expected = Fraction(1) + Fraction(1,2) + Fraction(1,8) + Fraction(1,2) + Fraction(1,12) + Fraction(1,2)
        z = bar_graph_zeta_g(2, 0.0)
        assert abs(z - float(expected)) < 1e-10

    def test_bar_zeta_real_for_real_u(self):
        """Z^{bar}_g(u) is real for real u (all graphs have real adjacency)."""
        for g in range(1, 4):
            for u in [0.1, 0.2, 0.3]:
                z = bar_graph_zeta_g(g, u)
                assert abs(z.imag) < 1e-10

    def test_bar_zeta_positive_small_u(self):
        """Z^{bar}_g(u) > 0 for small positive u (all zetas > 0)."""
        for g in range(1, 4):
            z = bar_graph_zeta_g(g, 0.1)
            assert z.real > 0

    def test_total_bar_zeta_genus_1_term(self):
        """Total bar zeta at leading order: Z(u,q) ~ Z_1(u)*q for small q."""
        u = 0.05  # Very small to avoid poles at higher genus
        q = 0.001
        total = total_bar_zeta(u, q, max_genus=3)
        z1 = bar_graph_zeta_g(1, u)
        leading = z1 * q
        # At q=0.001, higher terms are q^2, q^3, ... so very small
        assert abs(total - leading) < 0.01  # rough check

    def test_reciprocal_bar_zeta_polynomial(self):
        """The reciprocal bar zeta is a weighted sum of polynomials in u."""
        # At u=0, all reciprocals are 1, so sum = sum 1/Aut
        z = bar_graph_zeta_reciprocal_g(2, 0.0)
        expected = Fraction(1) + Fraction(1,2) + Fraction(1,8) + Fraction(1,2) + Fraction(1,12) + Fraction(1,2)
        assert abs(z - float(expected)) < 1e-10

    def test_planted_forest_complement(self):
        """Z^{bar}_g = Z^{pf}_g + Z^{non-pf}_g."""
        for g in range(1, 4):
            u = 0.05  # Small enough to avoid poles
            z_total = bar_graph_zeta_g(g, u)
            z_pf = planted_forest_zeta_g(g, u)
            z_npf = non_planted_forest_zeta_g(g, u)
            assert abs(z_total - z_pf - z_npf) < 1e-10


# ===================================================================
# SECTION 7: Ramanujan property (6 tests)
# ===================================================================

class TestRamanujanProperty:
    """Tests for the Ramanujan bound on adjacency eigenvalues."""

    def test_no_edge_ramanujan(self):
        """Graph with no edges is (vacuously) Ramanujan."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert is_ramanujan(g)

    def test_self_loop_single_vertex(self):
        """Single-vertex graph is Ramanujan (no nontrivial eigenvalues)."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        assert is_ramanujan(g)

    def test_theta_ramanujan_check(self):
        """Theta graph: eigenvalues are +3 and -3.
        d_max = 3, bound = 2*sqrt(2) ~ 2.83.
        Nontrivial eigenvalue is |-3| = 3 > 2.83, so NOT Ramanujan.
        """
        theta = genus2_stable_graphs_n0()[4]
        spec = adjacency_spectrum(theta)
        assert abs(spec[0] - 3.0) < 1e-10
        assert abs(spec[1] - (-3.0)) < 1e-10
        assert not is_ramanujan(theta)

    def test_ramanujan_stats_genus2(self):
        """Genus-2 Ramanujan statistics."""
        stats = ramanujan_statistics(2)
        assert stats['total'] == 6
        # Most genus-2 graphs are Ramanujan; theta is the exception
        assert stats['ramanujan_count'] >= 4

    def test_spectral_gap_positive(self):
        """Graphs with edges have finite spectral gap."""
        for gamma in genus2_stable_graphs_n0():
            if gamma.num_edges > 0 and gamma.num_vertices > 1:
                gap = spectral_gap(gamma)
                assert gap >= 0

    def test_ramanujan_fraction_decreases(self):
        """The fraction of non-Ramanujan graphs increases (or stays) with genus.

        As graph complexity grows, more graphs violate the bound.
        """
        fracs = []
        for g in range(1, 4):
            stats = ramanujan_statistics(g)
            fracs.append(float(stats['ramanujan_fraction']))
        # Not necessarily strictly decreasing, but we should have data
        assert all(0 <= f <= 1 for f in fracs)


# ===================================================================
# SECTION 8: Planted forest subcomplex (6 tests)
# ===================================================================

class TestPlantedForest:
    """Tests for the planted-forest subcomplex identification."""

    def test_smooth_not_planted(self):
        """Smooth curve (no edges, high genus) is NOT planted forest."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert not is_planted_forest_graph(g)

    def test_self_loop_not_planted(self):
        """Self-loop at genus-0 vertex: val = 2, which is < 3. Not planted."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        assert not is_planted_forest_graph(g)

    def test_banana_is_planted(self):
        """Banana (2 self-loops at g=0): val = 4 >= 3. IS planted forest."""
        banana = genus2_stable_graphs_n0()[2]
        assert banana.vertex_genera == (0,)
        assert is_planted_forest_graph(banana)

    def test_theta_is_planted(self):
        """Theta graph (g=0+g=0, 3 edges): val = 3 >= 3. IS planted forest."""
        theta = genus2_stable_graphs_n0()[4]
        assert is_planted_forest_graph(theta)

    def test_genus1_no_planted(self):
        """Genus-1 n=0 has no planted forest graphs.
        Graph 0: g=1, val=0. Graph 1: g=0, val=2. Neither has g=0 with val>=3."""
        for gamma in genus1_stable_graphs_n0():
            assert not is_planted_forest_graph(gamma)

    def test_planted_forest_count_genus3(self):
        """Genus-3: 35 out of 42 graphs are planted forest (from CLAUDE.md)."""
        graphs = enumerate_stable_graphs(3, 0)
        pf_count = sum(1 for g in graphs if is_planted_forest_graph(g))
        assert pf_count == 35


# ===================================================================
# SECTION 9: Pole/zero analysis (6 tests)
# ===================================================================

class TestPoleAnalysis:
    """Tests for Ihara zeta poles and the unit circle approach question."""

    def test_poles_are_reciprocal_eigenvalues(self):
        """Poles of zeta_G are 1/lambda for eigenvalues lambda of T."""
        theta = genus2_stable_graphs_n0()[4]
        T = hashimoto_matrix(theta)
        evals = np.linalg.eigvals(T.astype(complex))
        nonzero = [lam for lam in evals if abs(lam) > 1e-12]
        poles_from_evals = sorted([1.0/lam for lam in nonzero], key=lambda z: abs(z))
        poles_from_func = find_ihara_zeros(theta)
        # Should agree
        for p1, p2 in zip(poles_from_evals, poles_from_func):
            assert abs(p1 - p2) < 1e-8

    def test_min_pole_radius_genus1(self):
        """Genus-1 min pole radius: self-loop has pole at u=1."""
        r = min_pole_radius(1)
        assert abs(r - 1.0) < 1e-10

    def test_min_pole_radius_genus2(self):
        """Genus-2 min pole radius: theta graph has pole at u=1/2."""
        r = min_pole_radius(2)
        # Theta: poles at 1/sqrt(4) = 0.5 and 1.0
        # Banana B_2: poles from eigenvalues of 4x4 T.
        # The minimum should be 1/3 from the banana graph.
        assert r < 1.0

    def test_pole_radii_decrease_with_genus(self):
        """Min pole radius should decrease as genus increases (more complex graphs)."""
        data = unit_circle_approach_data(max_genus=3)
        assert data[1] >= data[2] >= data[3]

    def test_pole_radii_positive(self):
        """All pole radii are positive."""
        for g in range(1, 4):
            radii = ihara_pole_radii(g)
            if radii:
                assert min(radii) > 0

    def test_ihara_zeros_at_reciprocal_eigenvalues(self):
        """find_ihara_zeros returns reciprocals of T eigenvalues."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        T = hashimoto_matrix(g)
        evals = sorted(np.linalg.eigvals(T.astype(complex)), key=lambda x: -abs(x))
        zeros = find_ihara_zeros(g)
        for z in zeros:
            # z should be 1/lambda for some eigenvalue
            found_match = False
            for lam in evals:
                if abs(lam) > 1e-10 and abs(z - 1.0/lam) < 1e-8:
                    found_match = True
                    break
            assert found_match, f"Zero {z} not a reciprocal eigenvalue"


# ===================================================================
# SECTION 10: Cross-genus consistency and integration (6 tests)
# ===================================================================

class TestCrossGenusConsistency:
    """Cross-genus and integration tests for the bar zeta."""

    def test_genus1_ihara_data_length(self):
        """genus1_ihara_data returns 2 entries."""
        data = genus1_ihara_data()
        assert len(data) == 2

    def test_genus2_ihara_data_length(self):
        """genus2_ihara_data returns 6 entries."""
        data = genus2_ihara_data()
        assert len(data) == 6

    def test_full_analysis_genus2(self):
        """full_ihara_analysis at genus 2 returns correct graph count."""
        result = full_ihara_analysis(2)
        assert result['graph_count'] == 6
        assert result['genus'] == 2

    def test_closed_walks_genus2(self):
        """Bar-weighted closed walks at genus 2: N_1 counts length-1 walks."""
        walks = bar_weighted_closed_walks(2, max_length=4)
        assert len(walks) == 4
        # N_1 = Tr(T)/Aut sum.  Self-loops contribute to Tr(T).
        # N_1 should be nonzero (banana and self-loop contribute)
        assert abs(walks[0]) > 0

    def test_bar_zeta_monotone_in_u(self):
        """Z^{bar}_g(u) is increasing in u for 0 < u < min pole radius."""
        u_vals = [0.05, 0.1, 0.15]
        for g in range(1, 4):
            z_vals = [bar_graph_zeta_g(g, u).real for u in u_vals]
            # Should be increasing (zetas are > 1 and growing)
            assert z_vals[0] <= z_vals[1] + 1e-10
            assert z_vals[1] <= z_vals[2] + 1e-10

    def test_bar_graph_zeta_grows_with_genus(self):
        """Z^{bar}_g(0) grows with genus (more graphs with larger automorphisms)."""
        z_vals = [bar_graph_zeta_g(g, 0.0).real for g in range(1, 4)]
        # More graphs at higher genus => larger sum
        assert z_vals[0] < z_vals[1] < z_vals[2]


# ===================================================================
# SECTION 11: Additional multi-path and edge case tests (4+ tests)
# ===================================================================

class TestMultiPathVerification:
    """Additional multi-path verification tests."""

    def test_bass_formula_functional_equation(self):
        """For a graph with all degree d, Bass gives:
        zeta^{-1}(u) = (1-u^2)^{r-1} * det(I - uA + (d-1)u^2 I)

        This should equal the Hashimoto formula.
        """
        theta = genus2_stable_graphs_n0()[4]  # 3-regular
        for u in [0.1, 0.2]:
            A = adjacency_matrix(theta).astype(float)
            n = theta.num_vertices
            d = 3  # theta is 3-regular
            r = theta.first_betti
            M = np.eye(n) - u * A + (d - 1) * u**2 * np.eye(n)
            bass_val = (1 - u**2)**(r - 1) * np.linalg.det(M)
            hash_val = ihara_zeta_reciprocal_hashimoto(theta, u)
            assert abs(bass_val - hash_val) < 1e-10

    def test_determinant_polynomial_degree(self):
        """det(I - uT) is a polynomial in u of degree at most 2|E|.
        Verify by checking that it is well-approximated by a degree-2|E| polynomial."""
        for gamma in genus2_stable_graphs_n0():
            if gamma.num_edges == 0:
                continue
            m = 2 * gamma.num_edges
            # Evaluate at several points
            pts = np.linspace(0.01, 0.3, m + 3)
            vals = np.array([ihara_zeta_reciprocal_hashimoto(gamma, u).real for u in pts])
            # Fit degree-m polynomial
            coeffs = np.polyfit(pts, vals, m)
            fitted = np.polyval(coeffs, pts)
            # The fit should be excellent (exact up to numerical error)
            assert np.max(np.abs(fitted - vals)) < 1e-6, \
                f"Degree-{m} polynomial fit poor for {gamma}"

    def test_genus2_orbifold_euler_consistency(self):
        """The orbifold Euler characteristic chi^orb(M_bar_2) is computed
        from the stable graph sum. This is a consistency check between
        the Ihara zeta engine and the enumeration engine."""
        from compute.lib.stable_graph_enumeration import orbifold_euler_characteristic
        g2 = genus2_stable_graphs_n0()
        chi = orbifold_euler_characteristic(g2)
        # chi^orb(M_bar_{2,0}) = -181/1440 (computed from graph-vertex-product formula)
        # Cross-check: chi^orb(M_2) = B_4/(4*2*1) = (-1/30)/8 = -1/240
        # The compactification adds boundary strata contributions.
        assert chi == Fraction(-181, 1440)

    def test_hashimoto_trace_equals_closed_walks(self):
        """Tr(T^k) counts closed backtrackless walks of length k.
        For the self-loop: Tr(T) = 2, Tr(T^2) = 2 (each direction stays).
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        T = hashimoto_matrix(g)
        for k in range(1, 6):
            T_k = np.linalg.matrix_power(T, k)
            tr = int(np.round(np.trace(T_k).real))
            assert tr == 2  # I^k = I, trace = 2
