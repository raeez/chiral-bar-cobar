"""Tests for compute/lib/stable_graph_enumeration.py — stable graph engine.

Validates:
  1. StableGraph properties (genus, stability, valence, automorphisms)
  2. Explicit enumerations at small (g, n)
  3. Orbifold Euler characteristic via vertex-product formula
  4. Heisenberg free energies F_g = kappa * lambda_g^FP
  5. General enumeration engine
  6. Graph amplitude computations

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Harer-Zagier, "The Euler characteristic of the moduli space of curves" (1986)
  - higher_genus_modular_koszul.tex: def:stable-graph-coefficient-algebra
"""

import pytest
from fractions import Fraction

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    genus0_stable_graphs_n3,
    genus0_stable_graphs_n4,
    genus1_stable_graphs_n0,
    genus1_stable_graphs_n1,
    genus1_stable_graphs_n2,
    genus2_stable_graphs_n0,
    enumerate_stable_graphs,
    orbifold_euler_characteristic,
    graph_weight,
    graph_sum_scalar,
    heisenberg_free_energy,
    affine_sl2_free_energy,
)


# ============================================================================
# StableGraph basics
# ============================================================================

class TestStableGraphBasics:
    """Core StableGraph property tests."""

    def test_smooth_genus2(self):
        """Smooth genus-2 curve: 1 vertex g=2, no edges, no legs."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert g.num_vertices == 1
        assert g.num_edges == 0
        assert g.num_legs == 0
        assert g.arithmetic_genus == 2
        assert g.first_betti == 0
        assert g.valence == (0,)
        assert g.is_stable  # 2*2 - 2 + 0 = 2 > 0
        assert g.is_connected

    def test_stability_check_unstable(self):
        """A genus-0 vertex with only 2 half-edges is unstable."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        # val(0) = 2, so 2*0 - 2 + 2 = 0, NOT > 0
        assert not g.is_stable

    def test_stability_check_genus0_three_legs(self):
        """Genus-0 with 3 legs: 2*0 - 2 + 3 = 1 > 0."""
        g = StableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))
        assert g.is_stable

    def test_stability_check_genus1_one_leg(self):
        """Genus-1 with 1 leg: 2*1 - 2 + 1 = 1 > 0."""
        g = StableGraph(vertex_genera=(1,), edges=(), legs=(0,))
        assert g.is_stable

    def test_valence_selfloop(self):
        """A self-loop contributes 2 to the valence of its vertex."""
        g = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        assert g.valence == (2,)

    def test_valence_two_selfloops(self):
        """Two self-loops on the same vertex give valence 4."""
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert g.valence == (4,)

    def test_valence_edge_between_vertices(self):
        """An edge between two vertices contributes 1 to each."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        assert g.valence == (1, 1)

    def test_valence_mixed(self):
        """Self-loop + edge: val(v0) = 2 + 1 = 3, val(v1) = 1."""
        g = StableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=())
        assert g.valence == (3, 1)

    def test_arithmetic_genus_selfloop(self):
        """1 vertex g=1, 1 self-loop: h^1 = 1, total genus = 2."""
        g = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        assert g.first_betti == 1
        assert g.arithmetic_genus == 2

    def test_arithmetic_genus_theta(self):
        """Theta graph: 2 vertices g=0, 3 edges. h^1 = 3 - 2 + 1 = 2."""
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert g.first_betti == 2
        assert g.arithmetic_genus == 2

    def test_arithmetic_genus_separating(self):
        """Separating node: 2 vertices g=1, 1 edge. h^1 = 0, total = 2."""
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        assert g.first_betti == 0
        assert g.arithmetic_genus == 2

    def test_is_connected_simple(self):
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1))
        assert g.is_connected

    def test_selfloop_count(self):
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert g.self_loop_count(0) == 2

    def test_edge_multiplicity(self):
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert g.edge_multiplicity(0, 1) == 3
        assert g.edge_multiplicity(1, 0) == 3


# ============================================================================
# Automorphism computation
# ============================================================================

class TestAutomorphisms:
    """Automorphism order tests for known graphs."""

    def test_smooth_genus2_aut(self):
        """|Aut| = 1 for smooth curve (no symmetries with labeled legs)."""
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert g.automorphism_order() == 1

    def test_selfloop_aut(self):
        """|Aut| = 2 for a single self-loop (loop flip)."""
        g = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        assert g.automorphism_order() == 2

    def test_two_selfloops_aut(self):
        """|Aut| = 8 for two self-loops on a single vertex.

        Factor breakdown: 2 (flip loop 1) * 2 (flip loop 2) * 2 (swap the two loops) = 8.
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert g.automorphism_order() == 8

    def test_separating_node_aut(self):
        """|Aut| = 2 for two genus-1 vertices connected by one edge.

        The two vertices are interchangeable (same genus, no legs).
        """
        g = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        assert g.automorphism_order() == 2

    def test_theta_graph_aut(self):
        """|Aut| = 12 for the theta graph (two genus-0 vertices, 3 parallel edges).

        Factor breakdown: S_3 (permute 3 edges) * Z/2 (swap vertices) = 6 * 2 = 12.
        """
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert g.automorphism_order() == 12

    def test_mixed_genus2_aut(self):
        """|Aut| = 2 for genus-0 (self-loop + edge) -> genus-1.

        Vertices have different genera, so no vertex swap. Self-loop flip gives 2.
        """
        g = StableGraph(vertex_genera=(0, 1), edges=((0, 0), (0, 1)), legs=())
        assert g.automorphism_order() == 2

    def test_point_with_legs_aut(self):
        """|Aut| = 1 for genus-0 with 3 labeled legs."""
        g = StableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))
        assert g.automorphism_order() == 1

    def test_channel_graph_aut(self):
        """|Aut| = 1 for a channel graph (12|34) with labeled legs."""
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1, 1))
        assert g.automorphism_order() == 1

    def test_genus1_selfnode_with_leg_aut(self):
        """|Aut| = 2 for genus-0 with self-loop and 1 leg.

        The leg is fixed, but the self-loop can flip.
        """
        g = StableGraph(vertex_genera=(0,), edges=((0, 0),), legs=(0,))
        assert g.automorphism_order() == 2

    def test_separating_with_legs_aut(self):
        """Asymmetric legs prevent vertex swap: |Aut| = 1."""
        # Vertex 0 (g=0) carries leg 0 and 1; vertex 1 (g=0) carries leg 2.
        # Plus an edge (0,1). Genera match but legs don't, so |Aut| = 1.
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1))
        assert g.automorphism_order() == 1


# ============================================================================
# Genus-0 enumeration
# ============================================================================

class TestGenus0Enumeration:
    """Tests for genus-0 graph enumeration."""

    def test_genus0_n3_count(self):
        """1 stable graph at genus 0, n=3."""
        assert len(genus0_stable_graphs_n3()) == 1

    def test_genus0_n3_is_point(self):
        g = genus0_stable_graphs_n3()[0]
        assert g.vertex_genera == (0,)
        assert g.num_edges == 0
        assert g.num_legs == 3
        assert g.arithmetic_genus == 0
        assert g.is_stable

    def test_genus0_n4_count(self):
        """4 stable graphs at genus 0, n=4: point + 3 channels."""
        assert len(genus0_stable_graphs_n4()) == 4

    def test_genus0_n4_all_stable(self):
        for g in genus0_stable_graphs_n4():
            assert g.is_stable

    def test_genus0_n4_all_genus0(self):
        for g in genus0_stable_graphs_n4():
            assert g.arithmetic_genus == 0

    def test_genus0_n4_automorphisms(self):
        auts = [g.automorphism_order() for g in genus0_stable_graphs_n4()]
        assert all(a == 1 for a in auts)


# ============================================================================
# Genus-1 enumeration
# ============================================================================

class TestGenus1Enumeration:
    """Tests for genus-1 graph enumeration."""

    def test_genus1_n0_count(self):
        """2 genus-1 graphs with no marked points.

        NOTE: These are NOT stable in the DM sense (2g-2+n = 0).
        They represent the graph types contributing to the genus-1
        partition function (modular integral with weighting).
        """
        assert len(genus1_stable_graphs_n0()) == 2

    def test_genus1_n0_not_stable(self):
        """The (1,0) graphs are on the stability boundary: 2g-2+n = 0."""
        for g in genus1_stable_graphs_n0():
            # 2*g_v - 2 + val(v) = 0 for each vertex
            assert not g.is_stable

    def test_genus1_n0_automorphisms(self):
        auts = sorted([g.automorphism_order() for g in genus1_stable_graphs_n0()])
        assert auts == [1, 2]

    def test_genus1_n1_count(self):
        """2 stable graphs at genus 1, n=1."""
        assert len(genus1_stable_graphs_n1()) == 2

    def test_genus1_n1_all_stable(self):
        for g in genus1_stable_graphs_n1():
            assert g.is_stable

    def test_genus1_n1_all_genus1(self):
        for g in genus1_stable_graphs_n1():
            assert g.arithmetic_genus == 1

    def test_genus1_n1_automorphisms(self):
        auts = sorted([g.automorphism_order() for g in genus1_stable_graphs_n1()])
        assert auts == [1, 2]

    def test_genus1_n2_count(self):
        """5 stable graphs at genus 1, n=2."""
        assert len(genus1_stable_graphs_n2()) == 5

    def test_genus1_n2_all_stable(self):
        for g in genus1_stable_graphs_n2():
            assert g.is_stable

    def test_genus1_n2_all_genus1(self):
        for g in genus1_stable_graphs_n2():
            assert g.arithmetic_genus == 1


# ============================================================================
# Genus-2 enumeration
# ============================================================================

class TestGenus2Enumeration:
    """Tests for genus-2 graph enumeration — the key validation suite."""

    def test_genus2_n0_count(self):
        """6 stable graphs at genus 2, n=0."""
        graphs = genus2_stable_graphs_n0()
        assert len(graphs) == 6

    def test_genus2_automorphisms(self):
        """Known automorphism orders: {1, 2, 2, 2, 8, 12}."""
        graphs = genus2_stable_graphs_n0()
        auts = sorted([g.automorphism_order() for g in graphs])
        assert auts == [1, 2, 2, 2, 8, 12]

    def test_genus2_all_stable(self):
        for g in genus2_stable_graphs_n0():
            assert g.is_stable

    def test_genus2_all_genus2(self):
        for g in genus2_stable_graphs_n0():
            assert g.arithmetic_genus == 2

    def test_genus2_all_connected(self):
        for g in genus2_stable_graphs_n0():
            assert g.is_connected

    def test_genus2_edge_counts(self):
        """Edge counts: 0, 1, 2, 1, 3, 2."""
        graphs = genus2_stable_graphs_n0()
        edges = sorted([g.num_edges for g in graphs])
        assert edges == [0, 1, 1, 2, 2, 3]

    def test_genus2_first_betti(self):
        """First Betti numbers: 0, 1, 2, 0, 2, 1."""
        graphs = genus2_stable_graphs_n0()
        h1s = sorted([g.first_betti for g in graphs])
        assert h1s == [0, 0, 1, 1, 2, 2]

    def test_genus2_vertex_genera_sum(self):
        """Sum of vertex genera + h^1 = 2 for all graphs."""
        for g in genus2_stable_graphs_n0():
            assert sum(g.vertex_genera) + g.first_betti == 2

    def test_genus2_smooth_graph(self):
        """The smooth graph: 1 vertex g=2, 0 edges."""
        g = genus2_stable_graphs_n0()[0]
        assert g.vertex_genera == (2,)
        assert g.num_edges == 0
        assert g.automorphism_order() == 1

    def test_genus2_irreducible_node(self):
        """The irreducible node: 1 vertex g=1, 1 self-loop."""
        g = genus2_stable_graphs_n0()[1]
        assert g.vertex_genera == (1,)
        assert g.num_edges == 1
        assert g.self_loop_count(0) == 1
        assert g.automorphism_order() == 2

    def test_genus2_banana(self):
        """The banana graph: 1 vertex g=0, 2 self-loops."""
        g = genus2_stable_graphs_n0()[2]
        assert g.vertex_genera == (0,)
        assert g.num_edges == 2
        assert g.self_loop_count(0) == 2
        assert g.automorphism_order() == 8

    def test_genus2_separating(self):
        """The separating node: 2 vertices g=1, 1 edge."""
        g = genus2_stable_graphs_n0()[3]
        assert g.vertex_genera == (1, 1)
        assert g.num_edges == 1
        assert g.automorphism_order() == 2

    def test_genus2_theta(self):
        """The theta graph: 2 vertices g=0, 3 parallel edges."""
        g = genus2_stable_graphs_n0()[4]
        assert g.vertex_genera == (0, 0)
        assert g.num_edges == 3
        assert g.edge_multiplicity(0, 1) == 3
        assert g.automorphism_order() == 12

    def test_genus2_mixed(self):
        """The mixed graph: g=0 (self-loop) -> g=1."""
        g = genus2_stable_graphs_n0()[5]
        assert sorted(g.vertex_genera) == [0, 1]
        assert g.num_edges == 2
        assert g.automorphism_order() == 2


# ============================================================================
# Orbifold Euler characteristic
# ============================================================================

class TestOrbifoldEuler:
    """Orbifold Euler characteristic via vertex-product formula.

    chi^orb(M_bar_{g,n}) = sum_Gamma prod_v chi^orb(M_{g(v),val(v)}) / |Aut(Gamma)|

    Known values:
      chi^orb(M_{0,3}) = 1
      chi^orb(M_{1,1}) = -1/12
      chi^orb(M_2) = -1/240  (Harer-Zagier)
    """

    def test_euler_mbar03(self):
        """chi^orb(M_bar_{0,3}) = chi(M_{0,3}) = 1."""
        assert orbifold_euler_characteristic(genus0_stable_graphs_n3()) == Fraction(1)

    def test_euler_mbar04(self):
        """chi^orb(M_bar_{0,4}) = 2.

        M_bar_{0,4} = P^1 has chi^top = 2. The formula gives:
          chi(M_{0,4})/1 + 3 * chi(M_{0,3})^2 / 1
          = (-1)/1 + 3 * 1 / 1 = -1 + 3 = 2.
        """
        assert orbifold_euler_characteristic(genus0_stable_graphs_n4()) == Fraction(2)

    def test_euler_mbar11(self):
        """chi^orb(M_bar_{1,1}) = 5/12.

        Decomposition:
          Smooth (g=1,1 leg): chi(M_{1,1})/1 = -1/12
          Nodal (g=0, self-loop, 1 leg): chi(M_{0,3})/2 = 1/2
          Total: -1/12 + 1/2 = 5/12
        """
        assert orbifold_euler_characteristic(genus1_stable_graphs_n1()) == Fraction(5, 12)

    def test_euler_mbar20(self):
        """chi^orb(M_bar_{2,0}) = -181/1440.

        This is the non-trivial 6-graph identity verifying the enumeration:
          -1/240 - 1/24 - 1/8 + 1/288 + 1/12 - 1/24 = -181/1440.
        """
        assert orbifold_euler_characteristic(genus2_stable_graphs_n0()) == Fraction(-181, 1440)

    def test_euler_mbar20_decomposition(self):
        """Verify each graph's contribution to chi^orb(M_bar_{2,0})."""
        expected_contributions = [
            Fraction(-1, 240),     # smooth
            Fraction(-1, 24),      # irr node
            Fraction(-1, 8),       # banana
            Fraction(1, 288),      # separating
            Fraction(1, 12),       # theta
            Fraction(-1, 24),      # mixed
        ]
        graphs = genus2_stable_graphs_n0()
        assert len(graphs) == len(expected_contributions)

        from compute.lib.stable_graph_enumeration import _chi_orb_open
        for i, gamma in enumerate(graphs):
            val = gamma.valence
            vertex_product = Fraction(1)
            for v in range(gamma.num_vertices):
                vertex_product *= _chi_orb_open(gamma.vertex_genera[v], val[v])
            contrib = vertex_product / Fraction(gamma.automorphism_order())
            assert contrib == expected_contributions[i], (
                f"Graph {i+1}: expected {expected_contributions[i]}, got {contrib}"
            )

    def test_euler_mbar12(self):
        """chi^orb(M_bar_{1,2}) via the 5 genus-1 2-pointed graphs."""
        chi = orbifold_euler_characteristic(genus1_stable_graphs_n2())
        # Graph 1 (smooth g=1, 2 legs): chi(M_{1,2})/1 = -1/12
        # Graph 2 (nodal g=0, self-loop, 2 legs): chi(M_{0,4})/2 = -1/2
        # Graph 3 (g=1 -- edge -- g=0 with 2 legs): chi(M_{1,1})*chi(M_{0,3})/1 = -1/12
        # Graph 4 (g=0 self-loop+bridge -- g=0 2legs+bridge): chi(M_{0,3})*chi(M_{0,3})/2 = 1/2
        # Graph 5 (double bridge, 1 leg each): chi(M_{0,3})*chi(M_{0,3})/2 = 1/2
        expected = (Fraction(-1, 12) + Fraction(-1, 2) + Fraction(-1, 12)
                    + Fraction(1, 2) + Fraction(1, 2))
        assert chi == expected


# ============================================================================
# Open moduli Euler characteristics (Harer-Zagier)
# ============================================================================

class TestHarerZagier:
    """Verify the Harer-Zagier formula for chi^orb of open moduli spaces."""

    def test_chi_M03(self):
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(0, 3) == Fraction(1)

    def test_chi_M04(self):
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(0, 4) == Fraction(-1)

    def test_chi_M05(self):
        """chi(M_{0,5}) = (-1)^4 * 2! = 2."""
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(0, 5) == Fraction(2)

    def test_chi_M06(self):
        """chi(M_{0,6}) = (-1)^5 * 3! = -6."""
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(0, 6) == Fraction(-6)

    def test_chi_M11(self):
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(1, 1) == Fraction(-1, 12)

    def test_chi_M12(self):
        """chi(M_{1,2}) = (2*1-2+2-1) * chi(M_{1,1}) = 1 * (-1/12) = -1/12."""
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(1, 2) == Fraction(-1, 12)

    def test_chi_M2(self):
        """chi(M_2) = B_4 / (4*2*1) = (-1/30)/8 = -1/240."""
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(2, 0) == Fraction(-1, 240)

    def test_chi_M3(self):
        """chi(M_3) = B_6 / (4*3*2) = (1/42)/24 = 1/1008."""
        from compute.lib.stable_graph_enumeration import _chi_orb_open
        assert _chi_orb_open(3, 0) == Fraction(1, 1008)


# ============================================================================
# Graph weights
# ============================================================================

class TestGraphWeights:
    """Tests for the combinatorial weight (-1)^|E| / |Aut|."""

    def test_graph_weight_smooth(self):
        g = StableGraph(vertex_genera=(2,), edges=(), legs=())
        assert graph_weight(g) == Fraction(1)

    def test_graph_weight_selfloop(self):
        g = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        assert graph_weight(g) == Fraction(-1, 2)

    def test_graph_weight_banana(self):
        g = StableGraph(vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert graph_weight(g) == Fraction(1, 8)

    def test_graph_weight_theta(self):
        g = StableGraph(vertex_genera=(0, 0), edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert graph_weight(g) == Fraction(-1, 12)

    def test_graph_weight_sum_genus2(self):
        """Sum of (-1)^|E|/|Aut| over genus-2 graphs = 13/24."""
        total = sum(graph_weight(g) for g in genus2_stable_graphs_n0())
        assert total == Fraction(13, 24)


# ============================================================================
# Heisenberg free energies
# ============================================================================

class TestHeisenbergFreeEnergy:
    """F_g(H_k) = k * lambda_g^FP (Theorem D for Heisenberg).

    lambda_1^FP = 1/24, lambda_2^FP = 7/5760, lambda_3^FP = 31/967680.
    """

    def test_F1_rank1_level1(self):
        """F_1(H_1) = 1/24."""
        assert heisenberg_free_energy(1) == Fraction(1, 24)

    def test_F2_rank1_level1(self):
        """F_2(H_1) = 7/5760."""
        assert heisenberg_free_energy(2) == Fraction(7, 5760)

    def test_F3_rank1_level1(self):
        """F_3(H_1) = 31/967680."""
        assert heisenberg_free_energy(3) == Fraction(31, 967680)

    def test_F1_rank1_level_k(self):
        """F_1(H_k) = k/24."""
        for k in [1, 2, 3, 5, 10]:
            assert heisenberg_free_energy(1, k=Fraction(k)) == Fraction(k, 24)

    def test_F1_rank_d(self):
        """F_1(H_k^d) = k*d/24: kappa(H_k^d) = k*d."""
        assert heisenberg_free_energy(1, k=Fraction(1), d=3) == Fraction(3, 24)
        assert heisenberg_free_energy(1, k=Fraction(2), d=5) == Fraction(10, 24)

    def test_F2_level_k(self):
        """F_2(H_k) = 7k/5760."""
        for k in [1, 2, 5]:
            expected = Fraction(7 * k, 5760)
            assert heisenberg_free_energy(2, k=Fraction(k)) == expected

    def test_lambda_fp_values(self):
        """Verify lambda_g^FP directly."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        assert _lambda_fp_exact(1) == Fraction(1, 24)
        assert _lambda_fp_exact(2) == Fraction(7, 5760)
        assert _lambda_fp_exact(3) == Fraction(31, 967680)


# ============================================================================
# Affine sl_2 free energies
# ============================================================================

class TestAffineSl2FreeEnergy:
    """F_g(V_k(sl_2)) = kappa(V_k(sl_2)) * lambda_g^FP.

    kappa(V_k(sl_2)) = 3(k + h^v)/2 = 3(k + 2)/2.
    """

    def test_F1_level1(self):
        """F_1(V_1(sl_2)) = 3*3/(2*24) = 9/48 = 3/16."""
        assert affine_sl2_free_energy(1, k=Fraction(1)) == Fraction(3, 16)

    def test_F1_level_k(self):
        """F_1(V_k(sl_2)) = 3(k+2)/(2*24) = (k+2)/16."""
        for k in [1, 2, 5, 10]:
            expected = Fraction(k + 2, 16)
            assert affine_sl2_free_energy(1, k=Fraction(k)) == expected

    def test_F2_level1(self):
        """F_2(V_1(sl_2)) = 3*3/(2*5760/7) = 9/2 * 7/5760 = 63/11520 = 7/1280."""
        expected = Fraction(3 * 3, 2) * Fraction(7, 5760)
        assert affine_sl2_free_energy(2, k=Fraction(1)) == expected


# ============================================================================
# Scalar graph sum
# ============================================================================

class TestGraphSumScalar:
    """Tests for the scalar graph sum sum_Gamma |Aut|^{-1} * kappa^{|E|}."""

    def test_genus2_scalar_sum(self):
        """Scalar graph sum at genus 2 for kappa = 1."""
        total = graph_sum_scalar(genus2_stable_graphs_n0(), kappa=Fraction(1))
        # With kappa=1: each graph contributes kappa^|E|/|Aut| = 1/|Aut|
        # Sum = 1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2 = (24+12+3+12+2+12)/24 = 65/24
        assert total == Fraction(65, 24)

    def test_genus2_scalar_sum_kappa_k(self):
        """Graph sum at genus 2 for Heisenberg with kappa = k.

        sum = k^0/1 + k^1/2 + k^2/8 + k^1/2 + k^3/12 + k^2/2
            = 1 + k/2 + k^2/8 + k/2 + k^3/12 + k^2/2
            = 1 + k + 5k^2/8 + k^3/12
        """
        k = Fraction(2)
        total = graph_sum_scalar(genus2_stable_graphs_n0(), kappa=k)
        expected = 1 + k + 5 * k**2 / 8 + k**3 / 12
        assert total == expected

    def test_genus1_n1_scalar_sum(self):
        """Scalar graph sum at genus 1, n=1."""
        total = graph_sum_scalar(genus1_stable_graphs_n1(), kappa=Fraction(1))
        # 1/1 + 1/2 = 3/2
        assert total == Fraction(3, 2)


# ============================================================================
# General enumeration engine
# ============================================================================

class TestGeneralEnumeration:
    """Tests for the general enumeration engine."""

    def test_general_matches_explicit_03(self):
        explicit = genus0_stable_graphs_n3()
        general = enumerate_stable_graphs(0, 3)
        assert len(general) == len(explicit)

    def test_general_matches_explicit_04(self):
        explicit = genus0_stable_graphs_n4()
        general = enumerate_stable_graphs(0, 4)
        assert len(general) == len(explicit)

    def test_general_matches_explicit_11(self):
        explicit = genus1_stable_graphs_n1()
        general = enumerate_stable_graphs(1, 1)
        assert len(general) == len(explicit)

    def test_general_matches_explicit_12(self):
        explicit = genus1_stable_graphs_n2()
        general = enumerate_stable_graphs(1, 2)
        assert len(general) == len(explicit)

    def test_general_matches_explicit_20(self):
        explicit = genus2_stable_graphs_n0()
        general = enumerate_stable_graphs(2, 0)
        assert len(general) == len(explicit)

    def test_general_euler_matches_explicit_20(self):
        """Orbifold Euler characteristic matches between general and explicit enumeration."""
        explicit = genus2_stable_graphs_n0()
        general = enumerate_stable_graphs(2, 0)
        chi_explicit = orbifold_euler_characteristic(explicit)
        chi_general = orbifold_euler_characteristic(general)
        assert chi_explicit == chi_general

    def test_unstable_returns_empty(self):
        """Unstable (g,n) pairs return empty lists."""
        assert enumerate_stable_graphs(0, 0) == []
        assert enumerate_stable_graphs(0, 1) == []
        assert enumerate_stable_graphs(0, 2) == []


# ============================================================================
# Bernoulli numbers
# ============================================================================

class TestBernoulliNumbers:
    """Verify exact Bernoulli number computation."""

    def test_B0(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(0) == Fraction(1)

    def test_B1(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(1) == Fraction(-1, 2)

    def test_B2(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(2) == Fraction(1, 6)

    def test_B4(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(4) == Fraction(-1, 30)

    def test_B6(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_B8(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(8) == Fraction(-1, 30)

    def test_B10(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        assert _bernoulli_exact(10) == Fraction(5, 66)

    def test_odd_bernoulli_vanish(self):
        from compute.lib.stable_graph_enumeration import _bernoulli_exact
        for n in [3, 5, 7, 9, 11]:
            assert _bernoulli_exact(n) == Fraction(0)


# ============================================================================
# Boundary strata and edge contraction
# ============================================================================

class TestBoundaryStrata:
    """Tests for boundary stratum structure."""

    def test_genus2_boundary_types(self):
        """Classify genus-2 boundary graphs by edge structure.

        Boundary = all graphs with |E| > 0. Three boundary divisor types:
          Delta_0 (irreducible): self-loop on genus-1 vertex
          Delta_1 (separating): two genus-1 vertices, one edge
          Deeper boundary: |E| >= 2
        """
        graphs = genus2_stable_graphs_n0()
        boundary = [g for g in graphs if g.num_edges > 0]
        assert len(boundary) == 5  # all except smooth

        # Delta_irr: irreducible node
        delta_irr = [g for g in boundary if g.num_vertices == 1 and g.num_edges == 1]
        assert len(delta_irr) == 1

        # Delta_1: separating node
        delta_1 = [g for g in boundary if g.num_vertices == 2 and g.num_edges == 1]
        assert len(delta_1) == 1
        assert delta_1[0].vertex_genera == (1, 1)

    def test_genus2_boundary_codimension(self):
        """Boundary stratum codimension = number of edges.

        dim(M_bar_{2,0}) = 3, so:
          codim 0: smooth (|E|=0)
          codim 1: |E|=1 (irr node, separating node)
          codim 2: |E|=2 (banana, mixed)
          codim 3: |E|=3 (theta)
        """
        graphs = genus2_stable_graphs_n0()
        by_codim = {}
        for g in graphs:
            codim = g.num_edges
            by_codim.setdefault(codim, []).append(g)

        assert len(by_codim[0]) == 1  # smooth
        assert len(by_codim[1]) == 2  # irr + separating
        assert len(by_codim[2]) == 2  # banana + mixed
        assert len(by_codim[3]) == 1  # theta

    def test_genus1_n1_boundary(self):
        """At genus 1 n=1: one smooth, one boundary graph."""
        graphs = genus1_stable_graphs_n1()
        smooth = [g for g in graphs if g.num_edges == 0]
        boundary = [g for g in graphs if g.num_edges > 0]
        assert len(smooth) == 1
        assert len(boundary) == 1
        assert boundary[0].self_loop_count(0) == 1


# ============================================================================
# Consistency checks
# ============================================================================

class TestConsistency:
    """Cross-checks between different computations."""

    def test_lambda_fp_matches_utils(self):
        """Cross-check lambda_g^FP against compute.lib.utils."""
        try:
            from compute.lib.utils import lambda_fp as utils_lambda_fp
            from compute.lib.stable_graph_enumeration import _lambda_fp_exact
            for g in [1, 2, 3]:
                # utils version returns sympy Rational, ours returns Fraction
                ours = _lambda_fp_exact(g)
                theirs = utils_lambda_fp(g)
                assert float(ours) == pytest.approx(float(theirs), rel=1e-15)
        except ImportError:
            pytest.skip("compute.lib.utils not available")

    def test_heisenberg_matches_utils(self):
        """Cross-check F_g against compute.lib.utils."""
        try:
            from compute.lib.utils import F_g as utils_F_g
            import sympy
            k = sympy.Symbol('k')
            for g in [1, 2, 3]:
                # utils version: F_g(kappa, g) with kappa = k*dim/2... actually
                # F_g(kappa, g) = kappa * lambda_g
                # For Heisenberg of rank 1: kappa = k, so F_g = k * lambda_g
                our_val = heisenberg_free_energy(g, k=Fraction(7))
                their_val = utils_F_g(7, g)
                assert float(our_val) == pytest.approx(float(their_val), rel=1e-15)
        except ImportError:
            pytest.skip("compute.lib.utils not available")

    def test_genus_arithmetic_identity(self):
        """For all genus-2 graphs: sum g(v) + h^1 = 2."""
        for gamma in genus2_stable_graphs_n0():
            assert gamma.arithmetic_genus == 2

    def test_stability_euler_identity(self):
        """Stability identity: sum_v (2g(v)-2+val(v)) = 2(g-1) + n.

        This is the arithmetic genus formula rewritten:
        2g-2+n = sum_v (2g(v)-2+val(v)) for stable graphs.
        """
        for graphs, g, n in [
            (genus0_stable_graphs_n3(), 0, 3),
            (genus0_stable_graphs_n4(), 0, 4),
            (genus1_stable_graphs_n1(), 1, 1),
            (genus1_stable_graphs_n2(), 1, 2),
            (genus2_stable_graphs_n0(), 2, 0),
        ]:
            for gamma in graphs:
                val = gamma.valence
                lhs = sum(
                    2 * gamma.vertex_genera[v] - 2 + val[v]
                    for v in range(gamma.num_vertices)
                )
                rhs = 2 * g - 2 + n
                assert lhs == rhs, f"Failed for {gamma}: {lhs} != {rhs}"

    def test_half_edge_count(self):
        """Total half-edges = 2|E| + n (legs are fixed points of sigma)."""
        for gamma in genus2_stable_graphs_n0():
            total_val = sum(gamma.valence)
            assert total_val == 2 * gamma.num_edges + gamma.num_legs
