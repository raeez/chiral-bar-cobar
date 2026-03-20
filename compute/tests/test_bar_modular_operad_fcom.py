"""Tests for compute/lib/bar_modular_operad_fcom.py

Verifies thm:bar-modular-operad: {B^(g,n)(A)} forms an FCom-algebra,
and d^2=0 at all genera follows formally from the operadic structure.

Ground truth:
  - sl_2 CE complex: d^2=0 verified directly (Jacobi identity)
  - sl_2 Killing form trace: kappa = 2 (only kappa(h,h) nonzero on diagonal)
  - B^(1,0) = Tr(B^(0,2)): genus-1 curvature from genus-0 data
  - Heisenberg: kappa = 1 (single generator, kappa(J,J)=1)
  - Edge contraction preserves total genus and total arity

References:
  thm:bar-modular-operad (bar_cobar_adjunction_curved.tex)
  CLAUDE.md: Chriss-Ginzburg Principle item 4
"""

import pytest
import numpy as np
from math import comb, factorial

from compute.lib.bar_modular_operad_fcom import (
    # Stable graph data
    StableVertex,
    StableEdge,
    StableGraph,
    contract_edge,
    # A-infinity data
    AInfinityData,
    sl2_ainfty,
    heisenberg_ainfty,
    abelian_ainfty,
    # Bar complex
    BarData,
    bar_genus0_arity_n,
    bar_genus0_curvature,
    bar_genus1_arity0,
    # Edge contraction and trace
    trace_map,
    edge_contraction,
    genus1_from_genus0,
    # BarModularData
    BarModularData,
    build_bar_modular_data,
    # Verification
    verify_d_squared_genus0,
    verify_d_squared_genus1,
    verify_d_squared_operadic,
    operadic_d_squared_zero_proof,
    fcom_algebra_axiom_check,
    # Composition
    composition_map_graph,
    verify_genus0_composition,
    verify_edge_contraction_genus,
    # Tables and specific algebras
    stable_graph_composition_table,
    sl2_bar_modular_data,
    kappa_from_trace,
)


# =========================================================================
# Stable graph structure
# =========================================================================

class TestStableVertex:
    """Test stable vertex data."""

    def test_genus0_arity3_stable(self):
        """(g=0, n=3): 2*0-2+3 = 1 > 0, stable."""
        v = StableVertex(genus=0, arity=3, label=0)
        assert v.is_stable

    def test_genus0_arity2_unstable(self):
        """(g=0, n=2): 2*0-2+2 = 0, NOT stable."""
        v = StableVertex(genus=0, arity=2, label=0)
        assert not v.is_stable

    def test_genus1_arity0_unstable(self):
        """(g=1, n=0): 2*1-2+0 = 0, NOT stable."""
        v = StableVertex(genus=1, arity=0, label=0)
        assert not v.is_stable

    def test_genus1_arity1_stable(self):
        """(g=1, n=1): 2*1-2+1 = 1 > 0, stable."""
        v = StableVertex(genus=1, arity=1, label=0)
        assert v.is_stable

    def test_genus2_arity0_stable(self):
        """(g=2, n=0): 2*2-2+0 = 2 > 0, stable."""
        v = StableVertex(genus=2, arity=0, label=0)
        assert v.is_stable


class TestStableGraph:
    """Test stable graph topology."""

    def test_self_loop_genus(self):
        """Self-loop on (0,2): h^1 = 1, total genus = 1."""
        v = StableVertex(0, 2, 0)
        e = StableEdge(0, 0, 0)
        g = StableGraph((v,), (e,))
        assert g.first_betti == 1
        assert g.total_genus == 1

    def test_self_loop_arity(self):
        """Self-loop on (0,2): n = 2 - 2*1 = 0."""
        v = StableVertex(0, 2, 0)
        e = StableEdge(0, 0, 0)
        g = StableGraph((v,), (e,))
        assert g.total_arity == 0

    def test_binary_edge_genus(self):
        """(0,2)-(0,2) edge: h^1 = 0, total genus = 0."""
        v1 = StableVertex(0, 2, 0)
        v2 = StableVertex(0, 2, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        assert g.first_betti == 0
        assert g.total_genus == 0

    def test_binary_edge_arity(self):
        """(0,2)-(0,2) edge: n = 2+2-2 = 2."""
        v1 = StableVertex(0, 2, 0)
        v2 = StableVertex(0, 2, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        assert g.total_arity == 2

    def test_trinary_binary_arity(self):
        """(0,3)-(0,2) edge: n = 3+2-2 = 3."""
        v1 = StableVertex(0, 3, 0)
        v2 = StableVertex(0, 2, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        assert g.total_arity == 3

    def test_chain_graph_genus(self):
        """(0,2)-(0,3)-(0,2) chain: h^1=0, genus=0."""
        v1 = StableVertex(0, 2, 0)
        v2 = StableVertex(0, 3, 1)
        v3 = StableVertex(0, 2, 2)
        e1 = StableEdge(0, 0, 1)
        e2 = StableEdge(1, 1, 2)
        g = StableGraph((v1, v2, v3), (e1, e2))
        assert g.first_betti == 0
        assert g.total_genus == 0

    def test_chain_graph_arity(self):
        """(0,2)-(0,3)-(0,2) chain: n = 2+3+2 - 2*2 = 3."""
        v1 = StableVertex(0, 2, 0)
        v2 = StableVertex(0, 3, 1)
        v3 = StableVertex(0, 2, 2)
        e1 = StableEdge(0, 0, 1)
        e2 = StableEdge(1, 1, 2)
        g = StableGraph((v1, v2, v3), (e1, e2))
        assert g.total_arity == 3

    def test_genus_sum_formula(self):
        """g(Gamma) = h^1 + sum g_v for mixed-genus vertices."""
        v1 = StableVertex(1, 1, 0)
        v2 = StableVertex(0, 3, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        # h^1 = 0, sum g_v = 1
        assert g.total_genus == 1
        assert g.total_arity == 1 + 3 - 2  # = 2


class TestEdgeContraction:
    """Test edge contraction on stable graphs."""

    def test_contraction_preserves_genus(self):
        """Edge contraction preserves total genus."""
        results = verify_edge_contraction_genus()
        for r in results:
            assert r["genus_preserved"], (
                f"Genus changed from {r['genus_before']} to {r['genus_after']} "
                f"in {r['original']}"
            )

    def test_contraction_preserves_arity(self):
        """Edge contraction preserves total arity."""
        results = verify_edge_contraction_genus()
        for r in results:
            assert r["arity_preserved"], (
                f"Arity changed from {r['arity_before']} to {r['arity_after']} "
                f"in {r['original']}"
            )

    def test_contraction_reduces_edges(self):
        """Edge contraction reduces edge count by 1."""
        results = verify_edge_contraction_genus()
        for r in results:
            assert r["edges_after"] == r["edges_before"] - 1

    def test_self_loop_contraction_vertex_count(self):
        """Self-loop contraction keeps vertex count the same."""
        v = StableVertex(0, 2, 0)
        e = StableEdge(0, 0, 0)
        g = StableGraph((v,), (e,))
        gc = contract_edge(g, 0)
        assert gc.num_vertices == 1

    def test_non_loop_contraction_merges_vertices(self):
        """Non-loop contraction merges two vertices into one."""
        v1 = StableVertex(0, 3, 0)
        v2 = StableVertex(0, 3, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        gc = contract_edge(g, 0)
        assert gc.num_vertices == 1

    def test_contracted_vertex_genus(self):
        """After contracting (0,3)-(0,3), new vertex has g=0, n=4."""
        v1 = StableVertex(0, 3, 0)
        v2 = StableVertex(0, 3, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,))
        gc = contract_edge(g, 0)
        new_v = gc.vertices[0]
        assert new_v.genus == 0
        assert new_v.arity == 4

    def test_self_loop_adds_genus(self):
        """Contracting a self-loop adds 1 to the vertex genus."""
        v = StableVertex(0, 4, 0)
        e = StableEdge(0, 0, 0)
        g = StableGraph((v,), (e,))
        gc = contract_edge(g, 0)
        new_v = gc.vertices[0]
        assert new_v.genus == 1
        assert new_v.arity == 2


# =========================================================================
# A-infinity data
# =========================================================================

class TestAInfinityData:
    """Test A-infinity algebra data."""

    def test_sl2_dim(self):
        a = sl2_ainfty()
        assert a.dim == 3

    def test_sl2_bracket_ef(self):
        """[e, f] = h for sl_2."""
        a = sl2_ainfty()
        assert a.m2(0, 2) == {1: 1}

    def test_sl2_bracket_antisymmetry(self):
        """[a, b] = -[b, a] for sl_2."""
        a = sl2_ainfty()
        for i in range(3):
            for j in range(3):
                m2_ij = a.m2(i, j)
                m2_ji = a.m2(j, i)
                for c in set(list(m2_ij.keys()) + list(m2_ji.keys())):
                    assert m2_ij.get(c, 0) == -m2_ji.get(c, 0), (
                        f"Antisymmetry fails for ({i},{j}) at output {c}"
                    )

    def test_sl2_killing_symmetric(self):
        """kappa(a, b) = kappa(b, a) for sl_2."""
        a = sl2_ainfty()
        for i in range(3):
            for j in range(3):
                assert a.m0_pairing(i, j) == a.m0_pairing(j, i)

    def test_heisenberg_dim(self):
        a = heisenberg_ainfty()
        assert a.dim == 1

    def test_heisenberg_no_bracket(self):
        """Heisenberg has no simple pole -> no bracket."""
        a = heisenberg_ainfty()
        assert a.m2(0, 0) == {}

    def test_heisenberg_killing(self):
        """Heisenberg has kappa(J, J) = 1."""
        a = heisenberg_ainfty()
        assert a.m0_pairing(0, 0) == 1

    def test_abelian_no_bracket(self):
        a = abelian_ainfty(5)
        assert a.dim == 5
        for i in range(5):
            for j in range(5):
                assert a.m2(i, j) == {}


# =========================================================================
# Bar complex at genus 0
# =========================================================================

class TestBarGenus0:
    """Test genus-0 bar complex construction."""

    def test_sl2_arity1_dim(self):
        """B^(0,1) for sl_2 has dim 3."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 1)
        assert B.dim == 3
        assert B.genus == 0
        assert B.arity == 1

    def test_sl2_arity2_dim(self):
        """B^(0,2) for sl_2 has dim 9."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 2)
        assert B.dim == 9

    def test_sl2_arity3_dim(self):
        """B^(0,3) for sl_2 has dim 27."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 3)
        assert B.dim == 27

    def test_sl2_arity_n_dim_formula(self):
        """B^(0,n) for sl_2 has dim = 3^n."""
        a = sl2_ainfty()
        for n in range(1, 5):
            B = bar_genus0_arity_n(a, n)
            assert B.dim == 3 ** n

    def test_sl2_arity2_differential_shape(self):
        """d: g^2 -> g has shape (3, 9)."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 2)
        assert B.differential.shape == (3, 9)

    def test_sl2_arity3_differential_shape(self):
        """d: g^3 -> g^2 has shape (9, 27)."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 3)
        assert B.differential.shape == (9, 27)

    def test_sl2_arity1_diff_zero(self):
        """d: g -> k is the zero map."""
        a = sl2_ainfty()
        B = bar_genus0_arity_n(a, 1)
        assert np.allclose(B.differential, 0)

    def test_heisenberg_arity2_diff_zero(self):
        """Heisenberg has no bracket -> d: g^2 -> g is zero."""
        a = heisenberg_ainfty()
        B = bar_genus0_arity_n(a, 2)
        assert np.allclose(B.differential, 0)

    def test_abelian_diff_zero(self):
        """Abelian algebra has zero differential at all arities."""
        a = abelian_ainfty(3)
        for n in range(2, 5):
            B = bar_genus0_arity_n(a, n)
            assert np.allclose(B.differential, 0)


# =========================================================================
# d^2 = 0 at genus 0 (Jacobi identity)
# =========================================================================

class TestDSquaredGenus0:
    """Verify d^2 = 0 at genus 0 for the CE differential."""

    def test_sl2_d_squared_zero(self):
        """d^2 = 0 for sl_2 at all arities 2..4."""
        a = sl2_ainfty()
        results = verify_d_squared_genus0(a, max_n=4)
        for n, is_zero in results.items():
            assert is_zero, f"d^2 != 0 at arity {n} for sl_2"

    def test_sl2_d_squared_arity3_explicit(self):
        """Explicit d^2 check: d_{2} o d_{3} = 0 for sl_2."""
        a = sl2_ainfty()
        B3 = bar_genus0_arity_n(a, 3)
        B2 = bar_genus0_arity_n(a, 2)
        d_sq = B2.differential @ B3.differential
        assert np.allclose(d_sq, 0, atol=1e-12)

    def test_sl2_d_squared_arity4_explicit(self):
        """Explicit d^2 check: d_{3} o d_{4} = 0 for sl_2."""
        a = sl2_ainfty()
        B4 = bar_genus0_arity_n(a, 4)
        B3 = bar_genus0_arity_n(a, 3)
        d_sq = B3.differential @ B4.differential
        assert np.allclose(d_sq, 0, atol=1e-12)

    def test_heisenberg_d_squared_zero(self):
        """d^2 = 0 trivially for Heisenberg (d = 0)."""
        a = heisenberg_ainfty()
        results = verify_d_squared_genus0(a, max_n=4)
        for n, is_zero in results.items():
            assert is_zero

    def test_abelian_d_squared_zero(self):
        """d^2 = 0 trivially for abelian (d = 0)."""
        a = abelian_ainfty(4)
        results = verify_d_squared_genus0(a, max_n=4)
        for n, is_zero in results.items():
            assert is_zero


# =========================================================================
# Genus 1 from genus 0 (FCom self-loop)
# =========================================================================

class TestGenus1FromGenus0:
    """Test B^(1,0) = Tr(B^(0,2)) via FCom."""

    def test_sl2_trace_map_shape(self):
        """Trace map for sl_2: R^9 -> R."""
        a = sl2_ainfty()
        tr = trace_map(a, None)
        assert tr.shape == (9,)

    def test_sl2_trace_map_values(self):
        """Trace map picks up kappa(a,b): nonzero at (e,f), (f,e), (h,h)."""
        a = sl2_ainfty()
        tr = trace_map(a, None)
        # Basis order: (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)
        # kappa(0,2)=1 -> index 2
        # kappa(1,1)=2 -> index 4
        # kappa(2,0)=1 -> index 6
        assert tr[2] == 1.0   # kappa(e, f)
        assert tr[4] == 2.0   # kappa(h, h)
        assert tr[6] == 1.0   # kappa(f, e)
        # All others zero
        for i in [0, 1, 3, 5, 7, 8]:
            assert tr[i] == 0.0

    def test_sl2_genus1_dim(self):
        """B^(1,0) for sl_2 has dim 1."""
        a = sl2_ainfty()
        B = bar_genus1_arity0(a)
        assert B.dim == 1
        assert B.genus == 1
        assert B.arity == 0

    def test_sl2_kappa_from_trace(self):
        """kappa(sl_2) = Tr(Killing) = kappa(h,h) = 2."""
        a = sl2_ainfty()
        kappa = kappa_from_trace(a)
        assert kappa == 2.0

    def test_heisenberg_kappa_from_trace(self):
        """kappa(Heisenberg) = kappa(J,J) = 1."""
        a = heisenberg_ainfty()
        kappa = kappa_from_trace(a)
        assert kappa == 1.0

    def test_abelian_kappa_from_trace(self):
        """kappa(abelian_d) = d (identity Killing form)."""
        for d in [1, 2, 3, 5]:
            a = abelian_ainfty(d)
            kappa = kappa_from_trace(a)
            assert kappa == float(d)

    def test_genus1_from_genus0_graph(self):
        """The self-loop graph has total genus 1, arity 0."""
        a = sl2_ainfty()
        result = genus1_from_genus0(a)
        assert result["total_genus"] == 1
        assert result["total_arity"] == 0

    def test_genus1_from_genus0_kappa(self):
        """kappa from genus-0 data matches direct computation."""
        a = sl2_ainfty()
        result = genus1_from_genus0(a)
        assert result["kappa"] == 2.0


# =========================================================================
# Genus-1 Leibniz: Tr(d(x)) = 0
# =========================================================================

class TestGenus1Leibniz:
    """Verify the Leibniz compatibility at genus 1."""

    def test_sl2_trace_of_coboundary_zero(self):
        """Tr(d_{0,3}(x)) = 0 for all x in B^(0,3) (sl_2).

        This is the key Leibniz identity for the self-loop contraction.
        It says: the trace of a CE coboundary vanishes.
        Equivalently: kappa is ad-invariant.
        """
        a = sl2_ainfty()
        result = verify_d_squared_genus1(a)
        assert result["trace_of_coboundary_zero"]

    def test_heisenberg_trace_of_coboundary_zero(self):
        """Trivially zero for Heisenberg (d = 0)."""
        a = heisenberg_ainfty()
        result = verify_d_squared_genus1(a)
        assert result["trace_of_coboundary_zero"]

    def test_abelian_trace_of_coboundary_zero(self):
        """Trivially zero for abelian (d = 0)."""
        a = abelian_ainfty(3)
        result = verify_d_squared_genus1(a)
        assert result["trace_of_coboundary_zero"]

    def test_sl2_ad_invariance_of_killing(self):
        """Direct check: kappa([a,b], c) + kappa(b, [a,c]) = 0.

        This is the Leibniz identity in components.
        """
        a = sl2_ainfty()
        d = a.dim
        for x in range(d):
            for y in range(d):
                for z in range(d):
                    # kappa([x,y], z)
                    bracket_xy = a.m2(x, y)
                    term1 = sum(
                        float(coeff) * float(a.m0_pairing(c, z))
                        for c, coeff in bracket_xy.items()
                    )
                    # kappa(y, [x,z])
                    bracket_xz = a.m2(x, z)
                    term2 = sum(
                        float(coeff) * float(a.m0_pairing(y, c))
                        for c, coeff in bracket_xz.items()
                    )
                    assert abs(term1 + term2) < 1e-12, (
                        f"ad-invariance fails for x={x}, y={y}, z={z}: "
                        f"kappa([x,y],z) + kappa(y,[x,z]) = {term1 + term2}"
                    )


# =========================================================================
# Edge contraction
# =========================================================================

class TestEdgeContractionMap:
    """Test the edge contraction composition map."""

    def test_sl2_contraction_shape(self):
        """Contraction (0,2) x (0,2) -> (0,2): shape (9, 81)."""
        a = sl2_ainfty()
        bd1 = BarData(genus=0, arity=2, dim=9)
        bd2 = BarData(genus=0, arity=2, dim=9)
        mu = edge_contraction(a, bd1, bd2)
        assert mu.shape == (9, 81)

    def test_sl2_contraction_nonzero(self):
        """Contraction matrix is nonzero for sl_2."""
        a = sl2_ainfty()
        bd1 = BarData(genus=0, arity=2, dim=9)
        bd2 = BarData(genus=0, arity=2, dim=9)
        mu = edge_contraction(a, bd1, bd2)
        assert np.any(np.abs(mu) > 1e-15)

    def test_heisenberg_contraction_arity1(self):
        """Contraction (0,1) x (0,1) -> (0,0): shape (1, 1)."""
        a = heisenberg_ainfty()
        bd1 = BarData(genus=0, arity=1, dim=1)
        bd2 = BarData(genus=0, arity=1, dim=1)
        mu = edge_contraction(a, bd1, bd2)
        assert mu.shape == (1, 1)
        # kappa(0, 0) = 1
        assert abs(mu[0, 0] - 1.0) < 1e-12


# =========================================================================
# FCom algebra axioms
# =========================================================================

class TestFComAxioms:
    """Test FCom algebra axioms."""

    def test_sl2_equivariance(self):
        """S_2 equivariance at arity 2 for sl_2."""
        a = sl2_ainfty()
        results = fcom_algebra_axiom_check(a)
        assert results["equivariance_n2"]

    def test_sl2_composition_associativity(self):
        """Composition associativity for sl_2 (implied by d^2=0)."""
        a = sl2_ainfty()
        results = fcom_algebra_axiom_check(a)
        assert results["composition_associativity"]

    def test_sl2_unit_axiom(self):
        a = sl2_ainfty()
        results = fcom_algebra_axiom_check(a)
        assert results["unit_axiom"]


# =========================================================================
# Full operadic d^2 = 0 proof
# =========================================================================

class TestOperadicDSquared:
    """Test the operadic proof that D^2 = 0."""

    def test_sl2_operadic_proof(self):
        """Full operadic d^2=0 proof for sl_2."""
        a = sl2_ainfty()
        result = operadic_d_squared_zero_proof(a)
        assert result["theorem_holds"]

    def test_sl2_type_I(self):
        """Type I: d_v^2 = 0 at each vertex."""
        a = sl2_ainfty()
        result = operadic_d_squared_zero_proof(a)
        for n, ok in result["type_I_d_squared"].items():
            assert ok, f"Type I fails at arity {n}"

    def test_sl2_type_II(self):
        """Type II: Leibniz for edge contraction."""
        a = sl2_ainfty()
        result = operadic_d_squared_zero_proof(a)
        assert result["type_II_leibniz"]["trace_of_coboundary_zero"]

    def test_sl2_type_III(self):
        """Type III: edge contractions commute (trivial at genus <= 1)."""
        a = sl2_ainfty()
        result = operadic_d_squared_zero_proof(a)
        assert result["type_III_associativity"]

    def test_heisenberg_operadic_proof(self):
        """Full operadic d^2=0 proof for Heisenberg."""
        a = heisenberg_ainfty()
        result = operadic_d_squared_zero_proof(a)
        assert result["theorem_holds"]

    def test_operadic_vs_direct(self):
        """Operadic proof and direct computation agree for sl_2."""
        a = sl2_ainfty()
        direct = verify_d_squared_genus0(a, max_n=4)
        operadic = verify_d_squared_operadic(a, max_g=1)
        for n in direct:
            assert direct[n] == operadic["genus_0"][n]


# =========================================================================
# Composition map for stable graphs
# =========================================================================

class TestCompositionMap:
    """Test composition maps for stable graphs."""

    def test_self_loop_map(self):
        """Self-loop composition is the trace map."""
        a = sl2_ainfty()
        v = StableVertex(0, 2, 0)
        e = StableEdge(0, 0, 0)
        g = StableGraph((v,), (e,), "self-loop")
        result = composition_map_graph(a, g)
        assert result["map_type"] == "trace"
        assert result["total_genus"] == 1
        assert result["total_arity"] == 0

    def test_binary_edge_map(self):
        """Binary edge composition is edge contraction."""
        a = sl2_ainfty()
        v1 = StableVertex(0, 2, 0)
        v2 = StableVertex(0, 2, 1)
        e = StableEdge(0, 0, 1)
        g = StableGraph((v1, v2), (e,), "binary")
        result = composition_map_graph(a, g)
        assert result["map_type"] == "edge_contraction"

    def test_no_edge_map(self):
        """No-edge graph gives identity."""
        a = sl2_ainfty()
        v = StableVertex(0, 3, 0)
        g = StableGraph((v,), (), "single")
        result = composition_map_graph(a, g)
        assert result["map_type"] == "identity"


# =========================================================================
# Stable graph composition table
# =========================================================================

class TestCompositionTable:
    """Test the stable graph composition table."""

    def test_table_nonempty(self):
        """Composition table has entries."""
        table = stable_graph_composition_table()
        assert len(table) > 0

    def test_self_loop_in_table(self):
        """Self-loop graph is in the table."""
        table = stable_graph_composition_table()
        names = [t["name"] for t in table]
        assert "self-loop" in names

    def test_table_genus_arity(self):
        """All table entries have consistent genus and arity."""
        table = stable_graph_composition_table()
        for entry in table:
            # total_genus >= 0, total_arity >= 0
            assert entry["total_genus"] >= 0
            assert entry["total_arity"] >= 0


# =========================================================================
# sl_2 full modular bar data
# =========================================================================

class TestSl2BarModularData:
    """Test the full sl_2 bar-modular operad data."""

    def test_genus0_present(self):
        """Genus-0 data present at arities 1..4."""
        bmd = sl2_bar_modular_data()
        for n in range(1, 5):
            assert bmd.get(0, n) is not None

    def test_genus1_present(self):
        """Genus-1 data present at arity 0."""
        bmd = sl2_bar_modular_data()
        assert bmd.get(1, 0) is not None

    def test_genus0_dims(self):
        """Genus-0 dims = 3^n."""
        bmd = sl2_bar_modular_data()
        for n in range(1, 5):
            assert bmd.get(0, n).dim == 3**n

    def test_genus1_dim(self):
        """B^(1,0) has dim 1."""
        bmd = sl2_bar_modular_data()
        assert bmd.get(1, 0).dim == 1


# =========================================================================
# Curvature map
# =========================================================================

class TestCurvatureMap:
    """Test genus-0 curvature map."""

    def test_sl2_curvature_arity2_shape(self):
        """d_curv: g^2 -> k has shape (1, 9)."""
        a = sl2_ainfty()
        mat = bar_genus0_curvature(a, 2)
        assert mat.shape == (1, 9)

    def test_sl2_curvature_arity2_nonzero(self):
        """Curvature is nonzero for sl_2."""
        a = sl2_ainfty()
        mat = bar_genus0_curvature(a, 2)
        assert np.any(np.abs(mat) > 1e-15)

    def test_sl2_curvature_arity3_shape(self):
        """d_curv: g^3 -> g has shape (3, 27)."""
        a = sl2_ainfty()
        mat = bar_genus0_curvature(a, 3)
        assert mat.shape == (3, 27)

    def test_heisenberg_curvature_arity2(self):
        """Heisenberg curvature at arity 2: trace of kappa."""
        a = heisenberg_ainfty()
        mat = bar_genus0_curvature(a, 2)
        assert mat.shape == (1, 1)
        # kappa(0,0) = 1 with sign (-1)^{0+1-1} = 1
        # Actually sign = (-1)^{0+1-1} = (-1)^0 = 1
        assert abs(mat[0, 0] - 1.0) < 1e-12


# =========================================================================
# Genus-0 composition verification
# =========================================================================

class TestGenus0Composition:
    """Test the genus-0 composition B^(0,2) x B^(0,2) -> B^(0,2)."""

    def test_sl2_composition_nonzero(self):
        """Composition map is nonzero for sl_2."""
        a = sl2_ainfty()
        result = verify_genus0_composition(a)
        assert result["contraction_matrix_nonzero"]

    def test_sl2_composition_shape(self):
        """Composition shape is (9, 81) for sl_2."""
        a = sl2_ainfty()
        result = verify_genus0_composition(a)
        assert result["mu_shape"] == (9, 81)


# =========================================================================
# Jacobi identity at the CE level
# =========================================================================

class TestJacobiIdentity:
    """The Jacobi identity is the reason d^2 = 0 at genus 0.

    [[a,b],c] + [[b,c],a] + [[c,a],b] = 0.
    """

    def test_sl2_jacobi(self):
        """Verify the Jacobi identity for sl_2."""
        a = sl2_ainfty()
        d = a.dim
        for x in range(d):
            for y in range(d):
                for z in range(d):
                    # [[x,y],z] + [[y,z],x] + [[z,x],y] = 0
                    def double_bracket(i, j, k):
                        inner = a.m2(i, j)
                        total = {}
                        for c, coeff in inner.items():
                            outer = a.m2(c, k)
                            for e, coeff2 in outer.items():
                                total[e] = total.get(e, 0) + float(coeff) * float(coeff2)
                        return total

                    t1 = double_bracket(x, y, z)
                    t2 = double_bracket(y, z, x)
                    t3 = double_bracket(z, x, y)

                    for e in set(list(t1.keys()) + list(t2.keys()) + list(t3.keys())):
                        total = t1.get(e, 0) + t2.get(e, 0) + t3.get(e, 0)
                        assert abs(total) < 1e-12, (
                            f"Jacobi fails for ({x},{y},{z}) at output {e}"
                        )


# =========================================================================
# BarModularData construction
# =========================================================================

class TestBarModularDataConstruction:
    """Test BarModularData build process."""

    def test_build_default(self):
        """Default build: genus 0 arities 1-4, genus 1 arity 0."""
        a = sl2_ainfty()
        bmd = build_bar_modular_data(a)
        assert len(bmd.bar_data) == 5  # 4 genus-0 + 1 genus-1

    def test_build_custom_max_n(self):
        """Custom max_n = 2: genus 0 arities 1-2, genus 1 arity 0."""
        a = sl2_ainfty()
        bmd = build_bar_modular_data(a, max_n=2)
        assert len(bmd.bar_data) == 3  # 2 genus-0 + 1 genus-1

    def test_build_genus0_only(self):
        """max_g=0: genus 0 only."""
        a = sl2_ainfty()
        bmd = build_bar_modular_data(a, max_g=0)
        assert len(bmd.bar_data) == 4  # 4 genus-0 only
        assert bmd.get(1, 0) is None

    def test_genus0_range(self):
        """genus0_range returns sorted arities."""
        a = sl2_ainfty()
        bmd = build_bar_modular_data(a, max_n=3)
        assert bmd.genus0_range() == [1, 2, 3]
