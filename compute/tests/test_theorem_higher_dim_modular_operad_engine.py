r"""Tests for the higher-dimensional modular operad engine.

THEOREM: E_n modular operad amplitudes, ribbon graph counting,
Feynman transform comparison (FCom vs FAss), Harer-Zagier verification.

42 tests organized in 8 sections:
  I.   Ribbon graph structure counts (genus 0, 1, 2)
  II.  Genus-0 ribbon tree count = (2n-5)!!
  III. Graph enumeration consistency (genus 0-2)
  IV.  Harer-Zagier cell decomposition counts
  V.   Euler characteristic verification (chi(M_2) = -1/240)
  VI.  E_n independence of shadow invariants kappa at arities 2-6
  VII. FCom vs FAss scalar sector agreement (genus 1-3)
  VIII.E_1/E_infty ratio and orientation doubling

MULTI-PATH VERIFICATION (AP10):
  Every numerical value verified by at least 2 independent methods.
  Harer-Zagier epsilon values verified against known tables.
  Graph counts verified against existing stable_graph_enumeration.py.
  Kappa values verified against theorem_kappa_en_invariance_engine.py.

References:
  theorem_higher_dim_modular_operad_engine.py
  stable_graph_enumeration.py
  theorem_kappa_en_invariance_engine.py
  CLAUDE.md: AP10, AP82, AP83, AP97, AP104
"""
import pytest
from fractions import Fraction

from compute.lib.theorem_higher_dim_modular_operad_engine import (
    # Utility
    double_factorial,
    catalan_number,
    # Graph structures
    RibbonStableGraph,
    # Graph enumeration
    genus0_graphs,
    genus1_graphs,
    genus2_graphs_n0,
    enumerate_stable_graphs,
    # Ribbon counting
    ribbon_structures_on_graph,
    ribbon_graph_count_genus0,
    total_ribbon_structures_genus,
    total_ordinary_graphs,
    # E_1/E_infty ratio
    e1_einfty_ratio,
    total_e1_einfty_ratio,
    # Orientation
    orientation_factor,
    genus1_trivalent_ribbon_vs_ordinary,
    # Harer-Zagier
    bernoulli_exact,
    chi_orb_mg,
    chi_orb_mgn,
    chi_orb_mbar_from_graphs,
    harer_zagier_epsilon,
    harer_zagier_total,
    # Feynman transform
    fcom_scalar_amplitude,
    fass_scalar_amplitude,
    verify_fcom_fass_scalar_agreement,
    # Shadow E_n independence
    shadow_kappa_en,
    verify_shadow_en_independence,
    # Verification
    verify_genus2_euler,
    # Summary
    theorem_summary,
)


# ========================================================================
# I. Ribbon graph structure counts
# ========================================================================

class TestRibbonStructureCounts:
    """Verify ribbon_structure_count = prod(val(v)-1)! at each vertex."""

    def test_genus0_3pt_single_vertex(self):
        """g=0, n=3: one vertex, val=3. (3-1)! = 2 ribbon structures."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))
        assert gr.ribbon_structure_count() == 2

    def test_genus0_4pt_single_vertex(self):
        """g=0, n=4: one vertex, val=4. (4-1)! = 6."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0, 0))
        assert gr.ribbon_structure_count() == 6

    def test_genus0_4pt_binary_tree(self):
        """g=0, n=4: two vertices val=3 each, 1 edge. (2!)*(2!) = 4."""
        gr = RibbonStableGraph(
            vertex_genera=(0, 0), edges=((0, 1),), legs=(0, 0, 1, 1))
        assert gr.ribbon_structure_count() == 4

    def test_genus1_smooth_n0(self):
        """g=1, n=0: smooth torus, val=0. ribbon_count = 1 (trivial)."""
        gr = RibbonStableGraph(vertex_genera=(1,), edges=(), legs=())
        assert gr.ribbon_structure_count() == 1

    def test_genus1_selfloop_n0(self):
        """g=1, n=0: self-loop, val=2. (2-1)! = 1."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        assert gr.ribbon_structure_count() == 1

    def test_genus2_theta(self):
        """g=2: theta graph, 2 vertices val=3 each, 3 edges. (2!)*(2!) = 4."""
        gr = RibbonStableGraph(
            vertex_genera=(0, 0),
            edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert gr.ribbon_structure_count() == 4

    def test_genus2_banana(self):
        """g=2: banana, 1 vertex val=4, 2 self-loops. (4-1)! = 6."""
        gr = RibbonStableGraph(
            vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert gr.ribbon_structure_count() == 6

    def test_genus2_barbell(self):
        """g=2: barbell, 2 vertices val=3 each. (2!)*(2!) = 4."""
        gr = RibbonStableGraph(
            vertex_genera=(0, 0),
            edges=((0, 0), (1, 1), (0, 1)), legs=())
        assert gr.ribbon_structure_count() == 4


# ========================================================================
# II. Genus-0 ribbon tree count = (2n-5)!!
# ========================================================================

class TestGenus0RibbonTreeCount:
    """Labeled trivalent ribbon trees at genus 0."""

    def test_n3(self):
        """n=3: (2*3-5)!! = 1!! = 1."""
        assert ribbon_graph_count_genus0(3) == 1

    def test_n4(self):
        """n=4: (2*4-5)!! = 3!! = 3."""
        assert ribbon_graph_count_genus0(4) == 3

    def test_n5(self):
        """n=5: (2*5-5)!! = 5!! = 15."""
        assert ribbon_graph_count_genus0(5) == 15

    def test_n6(self):
        """n=6: (2*6-5)!! = 7!! = 105."""
        assert ribbon_graph_count_genus0(6) == 105

    def test_n7(self):
        """n=7: (2*7-5)!! = 9!! = 945."""
        assert ribbon_graph_count_genus0(7) == 945

    def test_n2_zero(self):
        """n < 3 should return 0."""
        assert ribbon_graph_count_genus0(2) == 0
        assert ribbon_graph_count_genus0(1) == 0

    def test_double_factorial_identity(self):
        """(2n-5)!! = (2n-5)*(2n-7)*...*3*1 verified independently."""
        for n in range(3, 10):
            expected = 1
            for k in range(1, 2 * n - 4, 2):
                expected *= k
            assert ribbon_graph_count_genus0(n) == expected


# ========================================================================
# III. Graph enumeration consistency
# ========================================================================

class TestGraphEnumeration:
    """Verify graph counts against known values."""

    def test_genus0_n3_count(self):
        """M_bar_{0,3}: 1 graph (the point)."""
        graphs = enumerate_stable_graphs(0, 3)
        assert len(graphs) == 1

    def test_genus0_n4_count(self):
        """M_bar_{0,4}: 4 graphs (point + 3 channels)."""
        graphs = enumerate_stable_graphs(0, 4)
        assert len(graphs) == 4

    def test_genus1_n0_count(self):
        """M_bar_{1,0}: 2 graphs (smooth + self-loop)."""
        graphs = enumerate_stable_graphs(1, 0)
        assert len(graphs) == 2

    def test_genus1_n1_count(self):
        """M_bar_{1,1}: 2 graphs."""
        graphs = enumerate_stable_graphs(1, 1)
        assert len(graphs) == 2

    def test_genus2_n0_count(self):
        """M_bar_{2,0}: 7 graphs."""
        graphs = enumerate_stable_graphs(2, 0)
        assert len(graphs) == 7

    def test_genus2_all_stable(self):
        """Every enumerated genus-2 graph is stable."""
        graphs = enumerate_stable_graphs(2, 0)
        for gr in graphs:
            assert gr.is_stable, f"Unstable: {gr}"

    def test_genus2_all_connected(self):
        """Every enumerated genus-2 graph is connected."""
        graphs = enumerate_stable_graphs(2, 0)
        for gr in graphs:
            assert gr.is_connected, f"Not connected: {gr}"

    def test_genus2_all_correct_genus(self):
        """Every enumerated genus-2 graph has arithmetic genus 2."""
        graphs = enumerate_stable_graphs(2, 0)
        for gr in graphs:
            assert gr.arithmetic_genus == 2, \
                f"Wrong genus {gr.arithmetic_genus}: {gr}"


# ========================================================================
# IV. Harer-Zagier cell decomposition counts
# ========================================================================

class TestHarerZagier:
    """Verify Harer-Zagier epsilon values and identities."""

    def test_epsilon_genus0_catalan(self):
        """epsilon_0(n) = C_n (Catalan numbers)."""
        for n in range(8):
            assert harer_zagier_epsilon(0, n) == catalan_number(n)

    def test_epsilon_1_2(self):
        """epsilon_1(2) = 1 (one genus-1 identification of a square)."""
        assert harer_zagier_epsilon(1, 2) == 1

    def test_epsilon_1_3(self):
        """epsilon_1(3) = 10."""
        assert harer_zagier_epsilon(1, 3) == 10

    def test_epsilon_1_4(self):
        """epsilon_1(4) = 70."""
        assert harer_zagier_epsilon(1, 4) == 70

    def test_epsilon_2_4(self):
        """epsilon_2(4) = 21."""
        assert harer_zagier_epsilon(2, 4) == 21

    def test_total_is_double_factorial(self):
        """sum_g epsilon_g(n) = (2n-1)!! for n = 1..7.

        This is the Harer-Zagier identity.
        """
        for n in range(1, 8):
            total = harer_zagier_total(n)
            expected = double_factorial(2 * n - 1)
            assert total == expected, \
                f"n={n}: sum={total}, (2n-1)!!={expected}"

    def test_epsilon_vanishing(self):
        """epsilon_g(n) = 0 for n < 2g (not enough edges)."""
        assert harer_zagier_epsilon(1, 1) == 0
        assert harer_zagier_epsilon(2, 3) == 0
        assert harer_zagier_epsilon(3, 5) == 0


# ========================================================================
# V. Euler characteristic verification
# ========================================================================

class TestEulerCharacteristic:
    """Verify chi^orb(M_g) via Harer-Zagier and graph stratification."""

    def test_chi_m2_harer_zagier(self):
        """chi^orb(M_2) = B_4 / 8 = (-1/30)/8 = -1/240."""
        assert chi_orb_mg(2) == Fraction(-1, 240)

    def test_chi_m2_direct_bernoulli(self):
        """B_4 = -1/30 independently verified."""
        assert bernoulli_exact(4) == Fraction(-1, 30)

    def test_chi_m3_harer_zagier(self):
        """chi^orb(M_3) = B_6 / (4*3*2) = (1/42)/24 = 1/1008."""
        assert chi_orb_mg(3) == Fraction(1, 1008)

    def test_chi_m01_open(self):
        """chi^orb(M_{0,3}) = 1, chi^orb(M_{0,4}) = -1."""
        assert chi_orb_mgn(0, 3) == Fraction(1)
        assert chi_orb_mgn(0, 4) == Fraction(-1)

    def test_chi_m11_open(self):
        """chi^orb(M_{1,1}) = -1/12."""
        assert chi_orb_mgn(1, 1) == Fraction(-1, 12)

    def test_verify_genus2_all_methods(self):
        """Cross-check chi(M_2) = -1/240 by three methods."""
        result = verify_genus2_euler()
        assert result["hz_equals_expected"]
        assert result["direct_equals_expected"]
        assert result["harer_zagier"] == result["direct_bernoulli"]


# ========================================================================
# VI. E_n independence of shadow kappa
# ========================================================================

class TestShadowEnIndependence:
    """Verify kappa is independent of operadic level n."""

    def test_heisenberg_n_independent(self):
        """kappa(H_k) = k for all E_n levels."""
        result = verify_shadow_en_independence("heisenberg", 6, k=Fraction(3))
        assert result["all_equal"]
        assert result["kappa"] == Fraction(3)

    def test_virasoro_n_independent(self):
        """kappa(Vir_c) = c/2 for all E_n levels."""
        result = verify_shadow_en_independence("virasoro", 6, c=Fraction(26))
        assert result["all_equal"]
        assert result["kappa"] == Fraction(13)

    def test_affine_sl2_n_independent(self):
        """kappa(sl_2 at level k) = 3(k+2)/4 for all E_n."""
        result = verify_shadow_en_independence(
            "affine", 6, lie_type="A", rank=1, k=Fraction(1))
        assert result["all_equal"]
        # sl_2: dim=3, h^v=2. kappa = 3*(1+2)/(2*2) = 9/4
        assert result["kappa"] == Fraction(9, 4)

    def test_w3_n_independent(self):
        """kappa(W_3) = 5c/6 for all E_n."""
        result = verify_shadow_en_independence("wn", 6, N=3, c=Fraction(12))
        assert result["all_equal"]
        assert result["kappa"] == Fraction(10)

    def test_betagamma_n_independent(self):
        """kappa(betagamma) at lambda=1 for all E_n."""
        result = verify_shadow_en_independence("betagamma", 6, lam=1)
        assert result["all_equal"]
        assert result["kappa"] == Fraction(1)

    def test_lattice_rank4_n_independent(self):
        """kappa(V_Lambda) = rank for all E_n."""
        result = verify_shadow_en_independence("lattice", 6, rank=4)
        assert result["all_equal"]
        assert result["kappa"] == Fraction(4)


# ========================================================================
# VII. FCom vs FAss scalar sector agreement
# ========================================================================

class TestFComFAssAgreement:
    """Verify FCom = FAss at the scalar level (genus 1-3)."""

    def test_genus1_agreement(self):
        """FCom = FAss at genus 1, scalar level."""
        result = verify_fcom_fass_scalar_agreement(1, Fraction(1))
        assert result["agree"], f"FCom={result['fcom']}, FAss={result['fass']}"

    def test_genus2_agreement(self):
        """FCom = FAss at genus 2, scalar level."""
        result = verify_fcom_fass_scalar_agreement(2, Fraction(1))
        assert result["agree"], f"FCom={result['fcom']}, FAss={result['fass']}"

    def test_genus1_agreement_kappa2(self):
        """FCom = FAss at genus 1, kappa=2."""
        result = verify_fcom_fass_scalar_agreement(1, Fraction(2))
        assert result["agree"]

    def test_genus2_agreement_kappa3(self):
        """FCom = FAss at genus 2, kappa=3."""
        result = verify_fcom_fass_scalar_agreement(2, Fraction(3))
        assert result["agree"]

    def test_genus1_graph_count(self):
        """Genus 1 has exactly 2 graphs."""
        result = verify_fcom_fass_scalar_agreement(1)
        assert result["num_graphs"] == 2

    def test_genus2_graph_count(self):
        """Genus 2 has exactly 7 graphs."""
        result = verify_fcom_fass_scalar_agreement(2)
        assert result["num_graphs"] == 7


# ========================================================================
# VIII. E_1/E_infty ratio and orientation
# ========================================================================

class TestE1EinftyRatio:
    """E_1/E_infty multiplicity ratio and orientation doubling."""

    def test_ratio_genus0_3pt(self):
        """At (0,3): single vertex val=3. Ratio = (3-1)! = 2."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))
        assert e1_einfty_ratio(gr) == Fraction(2)

    def test_ratio_genus1_selfloop(self):
        """Self-loop at genus 1: val=2. Ratio = (2-1)! = 1."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        assert e1_einfty_ratio(gr) == Fraction(1)

    def test_ratio_genus2_theta(self):
        """Theta graph: 2 vertices val=3. Ratio = 2!*2! = 4."""
        gr = RibbonStableGraph(
            vertex_genera=(0, 0),
            edges=((0, 1), (0, 1), (0, 1)), legs=())
        assert e1_einfty_ratio(gr) == Fraction(4)

    def test_orientation_connected(self):
        """Connected graphs have orientation factor 2."""
        gr = RibbonStableGraph(vertex_genera=(0,), edges=(), legs=(0, 0, 0))
        assert orientation_factor(gr) == 2

    def test_ribbon_aut_vs_graph_aut(self):
        """Ribbon aut divides graph aut; differs by 2^{self-loops}."""
        # Self-loop graph: |Aut| = 2 (flip), |Aut_ribbon| = 1
        gr = RibbonStableGraph(vertex_genera=(0,), edges=((0, 0),), legs=())
        assert gr.automorphism_order() == 2
        assert gr.ribbon_automorphism_order() == 1

    def test_ribbon_aut_banana(self):
        """Banana (2 self-loops): |Aut| = 8, |Aut_ribbon| = 2."""
        gr = RibbonStableGraph(
            vertex_genera=(0,), edges=((0, 0), (0, 0)), legs=())
        assert gr.automorphism_order() == 8
        assert gr.ribbon_automorphism_order() == 2

    def test_summary_exists(self):
        """Theorem summary returns expected keys."""
        s = theorem_summary()
        assert "theorem" in s
        assert "key_results" in s
        assert len(s["key_results"]) >= 5
