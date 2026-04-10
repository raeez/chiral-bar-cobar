"""Tests for independent genus-4 stable graph enumeration engine.

Cross-checks the CC7 census claim (379 genus-4 stable graphs at n=0)
via two independent algorithmic enumeration engines that agree on:
  1. Total count
  2. Distribution by vertex count, edge count, and loop number
  3. Automorphism spectrum
  4. Orbifold Euler characteristic

Multi-path verification (AP10/HZ-6): every expected value below is
verified by at least 2 independent sources:
  [DC] direct computation from the independent engine
  [XC] cross-check against primary engine (stable_graph_enumeration.py)
  [EC] orbifold Euler characteristic consistency
  [LT] literature (Faber 1999, Harer-Zagier 1986)
  [LC] limiting case / lower genus consistency

References:
  higher_genus_modular_koszul.tex: sec:genus-4-amplitude, 379 graphs
  stable_graph_enumeration.py: primary engine
  genus4_stable_graph_enumeration.py: independent engine (this module's target)
"""

import pytest
from fractions import Fraction
from math import factorial
from collections import Counter

from compute.lib.genus4_stable_graph_enumeration import (
    enumerate_stable_graphs_independent,
    count_stable_graphs,
    count_by_vertices,
    count_by_edges,
    count_by_loop_number,
    count_by_ve,
    automorphism_spectrum,
    inverse_aut_sum,
    orbifold_euler_char,
    cross_check_with_primary,
    _genus_distributions,
    _bernoulli,
    _chi_orb_open,
)


# ============================================================================
# 1. Total count verification (5 tests)
# ============================================================================

class TestTotalCount:
    """Verify the genus-4 stable graph count = 379."""

    def test_genus4_count_is_379(self):
        """There are exactly 379 stable graphs at (g=4, n=0).

        # VERIFIED: [DC] independent adjacency-matrix enumeration,
        #           [XC] cross-check with primary edge-tuple engine
        """
        assert count_stable_graphs(4) == 379

    def test_genus2_count_is_7(self):
        """There are exactly 7 stable graphs at (g=2, n=0).

        # VERIFIED: [DC] independent enumeration, [LT] AP123 (7 NOT 6),
        #           [XC] primary engine
        """
        assert count_stable_graphs(2) == 7

    def test_genus3_count_is_42(self):
        """There are exactly 42 stable graphs at (g=3, n=0).

        # VERIFIED: [DC] independent enumeration,
        #           [XC] primary engine,
        #           [LT] higher_genus_modular_koszul.tex
        """
        assert count_stable_graphs(3) == 42

    def test_all_graphs_have_genus_4(self):
        """Every enumerated graph has arithmetic genus 4."""
        for gr in enumerate_stable_graphs_independent(4):
            g_arith = gr['h1'] + sum(gr['genera'])
            assert g_arith == 4, f"Wrong genus: {gr}"

    def test_all_graphs_are_stable(self):
        """Every enumerated graph satisfies 2*g(v)-2+val(v) > 0."""
        for gr in enumerate_stable_graphs_independent(4):
            for v in range(gr['num_vertices']):
                gv = gr['genera'][v]
                val_v = gr['valence'][v]
                assert 2 * gv - 2 + val_v > 0, (
                    f"Unstable vertex {v}: g={gv}, val={val_v} in {gr}"
                )


# ============================================================================
# 2. Distribution tests (8 tests)
# ============================================================================

class TestDistributions:
    """Verify subcounts by vertices, edges, and loop number."""

    def test_by_vertex_count(self):
        """By vertex count: 5 + 29 + 79 + 126 + 98 + 42 = 379.

        # VERIFIED: [DC] independent engine, [XC] primary engine
        """
        expected = {1: 5, 2: 29, 3: 79, 4: 126, 5: 98, 6: 42}
        assert count_by_vertices(4) == expected
        assert sum(expected.values()) == 379

    def test_by_edge_count(self):
        """By edge count: 1+3+7+21+43+75+89+81+42+17 = 379.

        # VERIFIED: [DC] independent engine, [XC] primary engine
        """
        expected = {
            0: 1, 1: 3, 2: 7, 3: 21, 4: 43,
            5: 75, 6: 89, 7: 81, 8: 42, 9: 17,
        }
        assert count_by_edges(4) == expected
        assert sum(expected.values()) == 379

    def test_by_loop_number(self):
        """By loop number h1: 11+36+93+128+111 = 379.

        # VERIFIED: [DC] independent engine, [XC] primary engine
        """
        expected = {0: 11, 1: 36, 2: 93, 3: 128, 4: 111}
        assert count_by_loop_number(4) == expected
        assert sum(expected.values()) == 379

    def test_max_edge_count_is_dim(self):
        """Maximum edge count = dim M_4 = 3*4-3 = 9.

        # VERIFIED: [DC] enumeration, [LT] dim M_g = 3g-3
        """
        graphs = enumerate_stable_graphs_independent(4)
        assert max(gr['num_edges'] for gr in graphs) == 9

    def test_min_edge_count_is_zero(self):
        """Minimum edge count = 0 (the smooth genus-4 curve)."""
        graphs = enumerate_stable_graphs_independent(4)
        assert min(gr['num_edges'] for gr in graphs) == 0

    def test_max_vertices_is_6(self):
        """Maximum vertex count = 2*4-2 = 6.

        # VERIFIED: [DC] enumeration, [LT] stability bound
        """
        graphs = enumerate_stable_graphs_independent(4)
        assert max(gr['num_vertices'] for gr in graphs) == 6

    def test_single_vertex_count(self):
        """5 single-vertex graphs: genera 0,1,2,3,4 with self-loops.

        # VERIFIED: [DC] direct enumeration, [LC] genus <= 4 self-loops
        """
        graphs = enumerate_stable_graphs_independent(4)
        single_v = [gr for gr in graphs if gr['num_vertices'] == 1]
        assert len(single_v) == 5

    def test_maximal_loop_graphs_all_genus_zero(self):
        """All h1=4 graphs have all vertex genera = 0.

        # VERIFIED: [DC] enumeration (h1 = g - sum(g_v), so h1=4 => sum(g_v)=0)
        """
        graphs = enumerate_stable_graphs_independent(4)
        for gr in graphs:
            if gr['h1'] == 4:
                assert all(gv == 0 for gv in gr['genera'])


# ============================================================================
# 3. Cross-check with primary engine (5 tests)
# ============================================================================

class TestCrossCheck:
    """Cross-check against the primary engine in stable_graph_enumeration.py."""

    def test_genus4_full_cross_check(self):
        """Full cross-check at genus 4: count, V, E, h1 all match.

        # VERIFIED: [XC] two independent engines agree
        """
        cc = cross_check_with_primary(4)
        assert cc['all_match'], f"Cross-check failed: {cc}"

    def test_genus3_cross_check(self):
        """Cross-check at genus 3."""
        cc = cross_check_with_primary(3)
        assert cc['all_match']

    def test_genus2_cross_check(self):
        """Cross-check at genus 2."""
        cc = cross_check_with_primary(2)
        assert cc['all_match']

    def test_automorphism_spectrum_matches(self):
        """Automorphism spectra agree between engines at genus 4.

        # VERIFIED: [XC] two independent automorphism computations agree
        """
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        primary = enumerate_stable_graphs(4, 0)
        primary_auts = sorted(g.automorphism_order() for g in primary)
        indep_auts = automorphism_spectrum(4)
        assert primary_auts == indep_auts

    def test_inverse_aut_sum_matches(self):
        """Sum of 1/|Aut| matches between engines.

        # VERIFIED: [XC] cross-engine, [DC] independent sum
        """
        from compute.lib.stable_graph_enumeration import enumerate_stable_graphs
        primary = enumerate_stable_graphs(4, 0)
        primary_sum = sum(
            Fraction(1, g.automorphism_order()) for g in primary
        )
        indep_sum = inverse_aut_sum(4)
        assert primary_sum == indep_sum
        assert indep_sum == Fraction(15521, 240)


# ============================================================================
# 4. Orbifold Euler characteristic (6 tests)
# ============================================================================

class TestEulerCharacteristic:
    """Verify orbifold Euler characteristic from the independent graph sum."""

    def test_chi_mbar4(self):
        """chi^orb(M_bar_{4,0}) = -4717039/6220800.

        # VERIFIED: [EC] graph sum over 379 graphs,
        #           [LT] consistent with Harer-Zagier + Faber
        """
        chi = orbifold_euler_char(4)
        assert chi == Fraction(-4717039, 6220800)

    def test_chi_mbar3(self):
        """chi^orb(M_bar_{3,0}) = -12419/90720.

        # VERIFIED: [EC] graph sum, [XC] primary engine
        """
        chi = orbifold_euler_char(3)
        assert chi == Fraction(-12419, 90720)

    def test_chi_mbar2(self):
        """chi^orb(M_bar_{2,0}) = -1/1440.

        # VERIFIED: [EC] graph sum, [LT] Harer-Zagier
        """
        chi = orbifold_euler_char(2)
        assert chi == Fraction(-1, 1440)

    def test_chi_open_4_from_bernoulli(self):
        """chi^orb(M_4) = B_8/(4*4*3) = -1/1440.

        # VERIFIED: [DC] Bernoulli computation, [LT] Harer-Zagier
        """
        B8 = _bernoulli(8)
        assert B8 == Fraction(-1, 30)
        chi = B8 / Fraction(48)
        assert chi == Fraction(-1, 1440)

    def test_smooth_graph_contribution(self):
        """Smooth genus-4 curve contributes chi^orb(M_4) = -1/1440."""
        graphs = enumerate_stable_graphs_independent(4)
        smooth = [gr for gr in graphs if gr['num_edges'] == 0]
        assert len(smooth) == 1
        gr = smooth[0]
        assert gr['genera'] == (4,)
        chi_smooth = _chi_orb_open(4, 0) / Fraction(gr['aut_order'])
        assert chi_smooth == Fraction(-1, 1440)

    def test_euler_char_increasing_magnitude(self):
        """|chi^orb(M_bar_g)| increases with g for g=2,3,4.

        # VERIFIED: [EC] computed from independent engine at each genus
        """
        chi2 = abs(orbifold_euler_char(2))
        chi3 = abs(orbifold_euler_char(3))
        chi4 = abs(orbifold_euler_char(4))
        assert chi2 < chi3 < chi4


# ============================================================================
# 5. Boundary cases and named graphs (6 tests)
# ============================================================================

class TestNamedGraphs:
    """Verify specific named graphs exist in the enumeration."""

    def test_smooth_genus4(self):
        """The smooth genus-4 curve exists: g=(4,), 0 edges."""
        graphs = enumerate_stable_graphs_independent(4)
        smooth = [gr for gr in graphs
                  if gr['genera'] == (4,) and gr['num_edges'] == 0]
        assert len(smooth) == 1
        assert smooth[0]['aut_order'] == 1

    def test_irreducible_node(self):
        """Irreducible node: g=(3,), 1 self-loop, aut=2."""
        graphs = enumerate_stable_graphs_independent(4)
        irr = [gr for gr in graphs
               if gr['genera'] == (3,) and gr['num_edges'] == 1]
        assert len(irr) == 1
        assert irr[0]['aut_order'] == 2

    def test_quadruple_self_loop(self):
        """Genus-0 vertex with 4 self-loops: g=(0,), E=4, aut=4!*2^4=384."""
        graphs = enumerate_stable_graphs_independent(4)
        quad = [gr for gr in graphs
                if gr['genera'] == (0,) and gr['num_edges'] == 4]
        assert len(quad) == 1
        assert quad[0]['aut_order'] == factorial(4) * 2**4
        assert quad[0]['aut_order'] == 384

    def test_separating_divisors(self):
        """Three codimension-1 boundary divisors: Delta_irr, Delta_1, Delta_2.

        # VERIFIED: [DC] enumeration, [LT] boundary of M_bar_4
        """
        graphs = enumerate_stable_graphs_independent(4)
        codim1 = [gr for gr in graphs if gr['num_edges'] == 1]
        assert len(codim1) == 3
        # Delta_irr: (3,) with self-loop
        # Delta_1: (3,1) separating
        # Delta_2: (2,2) separating
        genera_set = {gr['genera'] for gr in codim1}
        assert genera_set == {(3,), (3, 1), (2, 2)}

    def test_max_automorphism_384(self):
        """Maximum automorphism order is 384 = 4! * 2^4.

        # VERIFIED: [DC] the (0,) with 4 self-loops, [XC] primary engine
        """
        auts = automorphism_spectrum(4)
        assert max(auts) == 384

    def test_trivalent_graphs_at_maximal_codim(self):
        """At maximal codimension (9 edges), all vertices have valence 3.

        # VERIFIED: [DC] enumeration, [LT] trivalent = maximal codimension
        """
        graphs = enumerate_stable_graphs_independent(4)
        max_codim = [gr for gr in graphs if gr['num_edges'] == 9]
        assert len(max_codim) == 17
        for gr in max_codim:
            for v in range(gr['num_vertices']):
                assert gr['valence'][v] == 3, (
                    f"Non-trivalent vertex in maximal-codimension graph: {gr}"
                )


# ============================================================================
# 6. Cross-genus consistency (5 tests)
# ============================================================================

class TestCrossGenusConsistency:
    """Verify consistency across genera."""

    def test_counts_increasing(self):
        """Graph counts are strictly increasing: 7 < 42 < 379.

        # VERIFIED: [DC] enumeration at each genus
        """
        c2 = count_stable_graphs(2)
        c3 = count_stable_graphs(3)
        c4 = count_stable_graphs(4)
        assert c2 == 7
        assert c3 == 42
        assert c4 == 379
        assert c2 < c3 < c4

    def test_max_edges_equals_dim(self):
        """Max edges = 3g-3 at each genus g=2,3,4.

        # VERIFIED: [DC] enumeration, [LT] dim M_g = 3g-3
        """
        for g in [2, 3, 4]:
            graphs = enumerate_stable_graphs_independent(g)
            assert max(gr['num_edges'] for gr in graphs) == 3 * g - 3

    def test_max_vertices_equals_2g_minus_2(self):
        """Max vertices = 2g-2 at each genus.

        # VERIFIED: [DC] stability bound
        """
        for g in [2, 3, 4]:
            graphs = enumerate_stable_graphs_independent(g)
            assert max(gr['num_vertices'] for gr in graphs) == 2 * g - 2

    def test_codim1_count(self):
        """Codimension-1 boundary has floor(g/2)+1 divisors.

        # VERIFIED: [DC] enumeration, [LT] Delta_irr + Delta_1 + ... + Delta_{g/2}
        """
        for g in [2, 3, 4]:
            graphs = enumerate_stable_graphs_independent(g)
            codim1 = [gr for gr in graphs if gr['num_edges'] == 1]
            assert len(codim1) == g // 2 + 1

    def test_single_vertex_count_is_g(self):
        """Number of single-vertex graphs at genus g is g+1 (for g >= 2).

        Genera (g,), (g-1,) with 1 loop, ..., (0,) with g loops.
        Actually: single-vertex with k self-loops has g_v = g-k, so
        g_v ranges from 0 to g, giving g+1 options. But stability
        requires 2*g_v - 2 + 2*k > 0, i.e. 2*g - 2 > 0 (always true for g>=2).
        So all g+1 are stable.

        # VERIFIED: [DC] enumeration, [LC] g=2 has 3, g=3 has 4
        """
        for g in [2, 3, 4]:
            graphs = enumerate_stable_graphs_independent(g)
            sv = [gr for gr in graphs if gr['num_vertices'] == 1]
            assert len(sv) == g + 1


# ============================================================================
# 7. Genus distribution function tests (3 tests)
# ============================================================================

class TestGenusDistributions:
    """Verify the genus distribution generator."""

    def test_genus_dist_v3_sum3(self):
        """V=3, sum<=3 includes (1,1,1)."""
        dists = list(_genus_distributions(3, 3))
        assert (1, 1, 1) in dists

    def test_genus_dist_v4_sum3(self):
        """V=4, sum<=3 includes (1,1,1,0)."""
        dists = list(_genus_distributions(3, 4))
        assert (1, 1, 1, 0) in dists

    def test_genus_dist_all_non_increasing(self):
        """All generated tuples are non-increasing."""
        for max_g in range(5):
            for num_v in range(1, 5):
                for t in _genus_distributions(max_g, num_v):
                    for i in range(len(t) - 1):
                        assert t[i] >= t[i + 1], (
                            f"Not non-increasing: {t}"
                        )


# ============================================================================
# 8. Bernoulli and Euler characteristic sanity (3 tests)
# ============================================================================

class TestBernoulliSanity:
    """Verify Bernoulli numbers and Euler characteristics used internally."""

    def test_bernoulli_8(self):
        """B_8 = -1/30.

        # VERIFIED: [DC] Akiyama-Tanigawa, [LT] standard tables
        """
        assert _bernoulli(8) == Fraction(-1, 30)

    def test_chi_m04(self):
        r"""chi^orb(M_{0,4}) = -1.

        # VERIFIED: [DC] chi^orb(M_{0,n}) = (-1)^{n-1} (n-3)!
        #           n=4: (-1)^3 * 1! = -1
        #           [LT] chi^orb(P^1 \setminus {0,1,inf,x}) = -1
        """
        assert _chi_orb_open(0, 4) == Fraction(-1)

    def test_chi_m11(self):
        """chi^orb(M_{1,1}) = -1/12.

        # VERIFIED: [LT] SL_2(Z) orbifold
        """
        assert _chi_orb_open(1, 1) == Fraction(-1, 12)
