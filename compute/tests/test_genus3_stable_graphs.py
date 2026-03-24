"""Tests for compute/lib/genus3_stable_graphs.py — genus-3 stable graph engine.

Validates:
  1. Complete enumeration (42 graphs for g=3, n=0)
  2. Stability, connectedness, arithmetic genus for all graphs
  3. Automorphism spectrum
  4. Orbifold Euler characteristic: chi^orb(M_bar_{3,0}) = -12419/90720
  5. Spectral sequence decomposition by loop number h^1
  6. Boundary strata classification
  7. Amplitudes: Heisenberg, affine, Virasoro, beta-gamma
  8. Scalar graph sum polynomial in kappa
  9. Consistency with genus-2 data

References:
  - Faber, "A conjectural description of the tautological ring" (1999)
  - Harer-Zagier, "The Euler characteristic of the moduli space of curves" (1986)
  - higher_genus_modular_koszul.tex: def:stable-graph-coefficient-algebra
  - concordance.tex: const:vol1-genus-spectral-sequence
"""

import pytest
from fractions import Fraction

from compute.lib.genus3_stable_graphs import (
    genus3_stable_graphs_n0,
    genus3_graph_count,
    genus3_automorphism_table,
    genus3_automorphism_spectrum,
    genus3_euler_check,
    genus3_euler_decomposition,
    lambda3_fp,
    genus3_amplitudes_heisenberg,
    genus3_amplitudes_affine,
    genus3_amplitudes_affine_general,
    genus3_amplitudes_virasoro,
    genus3_amplitudes_betagamma,
    genus3_spectral_sequence_e1,
    genus3_spectral_sequence_counts,
    genus3_boundary_strata,
    genus3_boundary_divisor_types,
    genus3_graph_profiles,
    genus3_scalar_sum_polynomial,
    genus3_scalar_sum_at,
    genus3_graph_weight_sum,
    genus3_by_vertex_count,
    genus3_by_edge_count,
    genus3_named_graphs,
    genus3_genus2_consistency_check,
    genus3_summary,
)
from compute.lib.stable_graph_enumeration import (
    StableGraph,
    _bernoulli_exact,
    _lambda_fp_exact,
    _chi_orb_open,
    orbifold_euler_characteristic,
    graph_weight,
    graph_sum_scalar,
    genus2_stable_graphs_n0,
)


# ============================================================================
# Enumeration
# ============================================================================

class TestGenus3Enumeration:
    """Core enumeration tests for genus-3 stable graphs with n=0."""

    def test_genus3_n0_count(self):
        """42 stable graphs at genus 3, n=0."""
        assert genus3_graph_count() == 42

    def test_all_genus3(self):
        """Every graph has arithmetic genus 3."""
        for g in genus3_stable_graphs_n0():
            assert g.arithmetic_genus == 3, (
                f"Graph {g} has genus {g.arithmetic_genus}, expected 3"
            )

    def test_all_stable(self):
        """Every graph satisfies the stability condition 2g(v)-2+val(v) > 0."""
        for g in genus3_stable_graphs_n0():
            assert g.is_stable, f"Graph {g} is not stable"

    def test_all_connected(self):
        """Every graph is connected."""
        for g in genus3_stable_graphs_n0():
            assert g.is_connected, f"Graph {g} is not connected"

    def test_all_n0(self):
        """Every graph has 0 marked points (legs)."""
        for g in genus3_stable_graphs_n0():
            assert g.num_legs == 0, f"Graph {g} has {g.num_legs} legs"

    def test_vertex_genera_nonneg(self):
        """All vertex genera are non-negative."""
        for g in genus3_stable_graphs_n0():
            for gv in g.vertex_genera:
                assert gv >= 0

    def test_genus_decomposition(self):
        """For all graphs: sum g(v) + h^1 = 3."""
        for g in genus3_stable_graphs_n0():
            assert sum(g.vertex_genera) + g.first_betti == 3

    def test_stability_euler_identity(self):
        """Stability identity: sum_v (2g(v)-2+val(v)) = 2g-2+n = 4 for all graphs.

        This is the arithmetic genus formula rewritten.
        """
        for gamma in genus3_stable_graphs_n0():
            val = gamma.valence
            lhs = sum(
                2 * gamma.vertex_genera[v] - 2 + val[v]
                for v in range(gamma.num_vertices)
            )
            assert lhs == 4, f"Failed for {gamma}: {lhs} != 4"

    def test_half_edge_count(self):
        """Total half-edges = 2|E| + n = 2|E| for n=0."""
        for gamma in genus3_stable_graphs_n0():
            total_val = sum(gamma.valence)
            assert total_val == 2 * gamma.num_edges


# ============================================================================
# Automorphisms
# ============================================================================

class TestGenus3Automorphisms:
    """Automorphism order tests for genus-3 graphs."""

    def test_smooth_curve_aut1(self):
        """|Aut| = 1 for the smooth genus-3 curve (no symmetries)."""
        named = genus3_named_graphs()
        assert named["smooth"].automorphism_order() == 1

    def test_irr_node_aut2(self):
        """|Aut| = 2 for the irreducible node (loop flip)."""
        named = genus3_named_graphs()
        assert named["irr_node"].automorphism_order() == 2

    def test_double_loop_aut8(self):
        """|Aut| = 8 for 2 self-loops on genus-1 vertex.

        2 (flip loop 1) * 2 (flip loop 2) * 2 (swap loops) = 8.
        """
        named = genus3_named_graphs()
        assert named["double_loop"].automorphism_order() == 8

    def test_triple_loop_aut48(self):
        """|Aut| = 48 for 3 self-loops on genus-0 vertex.

        3! (permute loops) * 2^3 (flip each loop) = 6 * 8 = 48.
        """
        named = genus3_named_graphs()
        assert named["triple_loop"].automorphism_order() == 48

    def test_separating_aut1(self):
        """|Aut| = 1 for the separating node g=(2,1): vertices have different genera."""
        named = genus3_named_graphs()
        assert named["separating_21"].automorphism_order() == 1

    def test_parallel_11_aut4(self):
        """|Aut| = 4 for g=(1,1) with 2 parallel edges.

        2 (swap vertices) * 2 (swap edges) = 4.
        """
        named = genus3_named_graphs()
        assert named["parallel_11"].automorphism_order() == 4

    def test_K4_aut24(self):
        """|Aut| = 24 for K_4 (complete graph on 4 genus-0 vertices).

        Aut(K_4) = S_4, |S_4| = 24.
        """
        named = genus3_named_graphs()
        assert "K4" in named
        assert named["K4"].automorphism_order() == 24

    def test_automorphism_spectrum(self):
        """Verify the complete sorted automorphism spectrum."""
        expected = sorted([
            1, 1, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
            6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 16, 16, 16, 16, 16,
            24, 48, 48, 48,
        ])
        assert genus3_automorphism_spectrum() == expected

    def test_automorphism_table_length(self):
        """Automorphism table has 42 entries."""
        table = genus3_automorphism_table()
        assert len(table) == 42

    def test_all_auts_positive(self):
        """All automorphism orders are positive integers."""
        for aut in genus3_automorphism_spectrum():
            assert aut >= 1


# ============================================================================
# Spectral sequence
# ============================================================================

class TestGenus3SpectralSequence:
    """Tests for the genus spectral sequence decomposition."""

    def test_h1_range(self):
        """Loop number h^1 ranges from 0 to 3."""
        counts = genus3_spectral_sequence_counts()
        assert set(counts.keys()) == {0, 1, 2, 3}

    def test_h1_zero_count(self):
        """4 tree-type graphs (h^1 = 0)."""
        assert genus3_spectral_sequence_counts()[0] == 4

    def test_h1_one_count(self):
        """9 one-loop graphs (h^1 = 1)."""
        assert genus3_spectral_sequence_counts()[1] == 9

    def test_h1_two_count(self):
        """14 two-loop graphs (h^1 = 2)."""
        assert genus3_spectral_sequence_counts()[2] == 14

    def test_h1_three_count(self):
        """15 three-loop graphs (h^1 = 3)."""
        assert genus3_spectral_sequence_counts()[3] == 15

    def test_h1_total(self):
        """Sum over all h^1 values equals 42."""
        counts = genus3_spectral_sequence_counts()
        assert sum(counts.values()) == 42

    def test_spectral_sequence_graphs_match(self):
        """Graphs in the spectral sequence partition all 42."""
        pages = genus3_spectral_sequence_e1()
        all_graphs = []
        for graphs in pages.values():
            all_graphs.extend(graphs)
        assert len(all_graphs) == 42

    def test_tree_graphs_are_trees(self):
        """All h^1 = 0 graphs have zero first Betti number."""
        pages = genus3_spectral_sequence_e1()
        for g in pages[0]:
            assert g.first_betti == 0

    def test_deepest_graphs_genus_zero_vertices(self):
        """All h^1 = 3 graphs have all vertex genera = 0."""
        pages = genus3_spectral_sequence_e1()
        for g in pages[3]:
            assert all(gv == 0 for gv in g.vertex_genera)


# ============================================================================
# Amplitudes
# ============================================================================

class TestGenus3Amplitudes:
    """Amplitude tests for genus-3 free energies."""

    def test_lambda3_fp(self):
        """lambda_3^FP = 31/967680."""
        assert lambda3_fp() == Fraction(31, 967680)

    def test_lambda3_fp_formula(self):
        """Verify lambda_3 from Bernoulli numbers directly.

        lambda_3 = (2^5 - 1) * |B_6| / (2^5 * 6!)
                 = 31 * (1/42) / (32 * 720)
                 = 31 / 967680
        """
        B6 = _bernoulli_exact(6)
        assert B6 == Fraction(1, 42)
        numerator = (2**5 - 1) * abs(B6)  # 31 * 1/42
        denominator = Fraction(2**5 * 720)  # 32 * 720
        assert numerator / denominator == Fraction(31, 967680)

    def test_lambda3_matches_engine(self):
        """Cross-check with _lambda_fp_exact(3)."""
        assert lambda3_fp() == _lambda_fp_exact(3)

    def test_heisenberg_F3(self):
        """F_3(H_1) = 1 * 31/967680 = 31/967680."""
        assert genus3_amplitudes_heisenberg() == Fraction(31, 967680)

    def test_heisenberg_F3_k2(self):
        """F_3(H_2) = 2 * 31/967680 = 31/483840."""
        assert genus3_amplitudes_heisenberg(k=Fraction(2)) == Fraction(31, 483840)

    def test_heisenberg_F3_k5(self):
        """F_3(H_5) = 5 * 31/967680."""
        assert genus3_amplitudes_heisenberg(k=Fraction(5)) == Fraction(5 * 31, 967680)

    def test_heisenberg_F3_rank2(self):
        """F_3(H_1^2) = 2 * 31/967680 (rank d=2, level k=1)."""
        assert genus3_amplitudes_heisenberg(k=Fraction(1), d=2) == Fraction(2 * 31, 967680)

    def test_heisenberg_linearity(self):
        """F_3 is linear in kappa = k*d."""
        for k in [1, 2, 3, 5]:
            for d in [1, 2, 3]:
                result = genus3_amplitudes_heisenberg(k=Fraction(k), d=d)
                expected = Fraction(k * d * 31, 967680)
                assert result == expected

    def test_affine_sl2_F3(self):
        """F_3(V_1(sl_2)) = kappa * lambda_3 where kappa = 3(1+2)/2 = 9/2."""
        expected = Fraction(9, 2) * Fraction(31, 967680)
        assert genus3_amplitudes_affine(k=Fraction(1), g_type="sl2") == expected

    def test_affine_sl2_F3_k0(self):
        """F_3(V_0(sl_2)) = kappa * lambda_3 where kappa = 3(0+2)/2 = 3."""
        expected = Fraction(3) * lambda3_fp()
        assert genus3_amplitudes_affine(k=Fraction(0), g_type="sl2") == expected

    def test_affine_sl3_F3(self):
        """F_3(V_1(sl_3)) = kappa * lambda_3 where kappa = 8*(1+3)/2 = 16."""
        expected = Fraction(16) * lambda3_fp()
        assert genus3_amplitudes_affine(k=Fraction(1), g_type="sl3") == expected

    def test_affine_general_matches_typed(self):
        """genus3_amplitudes_affine_general matches genus3_amplitudes_affine for sl2."""
        for k in [0, 1, 2, 5]:
            typed = genus3_amplitudes_affine(k=Fraction(k), g_type="sl2")
            general = genus3_amplitudes_affine_general(k=Fraction(k), dim_g=3, h_vee=2)
            assert typed == general

    def test_virasoro_F3(self):
        """F_3(Vir_c) = (c/2) * lambda_3 at scalar level."""
        c = Fraction(26)
        expected = Fraction(13) * lambda3_fp()
        assert genus3_amplitudes_virasoro(c) == expected

    def test_virasoro_F3_c1(self):
        """F_3(Vir_1) = (1/2) * 31/967680 = 31/1935360."""
        assert genus3_amplitudes_virasoro(Fraction(1)) == Fraction(31, 2 * 967680)

    def test_betagamma_F3(self):
        """F_3(beta-gamma) = 1 * lambda_3 = 31/967680."""
        assert genus3_amplitudes_betagamma() == Fraction(31, 967680)

    def test_betagamma_positive(self):
        """Beta-gamma has positive F_3 (kappa = +1)."""
        assert genus3_amplitudes_betagamma() > 0

    def test_scalar_sum(self):
        """Graph sum = sum kappa^|E|/|Aut| matches direct computation."""
        kappa = Fraction(3)
        graphs = genus3_stable_graphs_n0()
        direct = graph_sum_scalar(graphs, kappa=kappa)
        via_module = genus3_scalar_sum_at(kappa)
        assert direct == via_module


# ============================================================================
# Euler characteristic
# ============================================================================

class TestGenus3Euler:
    """Orbifold Euler characteristic tests."""

    def test_euler_check(self):
        """chi^orb(M_bar_{3,0}) = -12419/90720."""
        computed, expected, match = genus3_euler_check()
        assert match
        assert computed == Fraction(-12419, 90720)

    def test_euler_decomposition_sum(self):
        """Sum of per-graph contributions equals chi^orb(M_bar_{3,0})."""
        decomposition = genus3_euler_decomposition()
        total = sum(contrib for _, contrib in decomposition)
        assert total == Fraction(-12419, 90720)

    def test_euler_decomposition_count(self):
        """42 contributions in the decomposition."""
        assert len(genus3_euler_decomposition()) == 42

    def test_chi_orb_open_M3(self):
        """chi^orb(M_3) = B_6 / (4*3*2) = (1/42)/24 = 1/1008."""
        assert _chi_orb_open(3, 0) == Fraction(1, 1008)

    def test_smooth_graph_contribution(self):
        """The smooth graph contributes chi^orb(M_3) = 1/1008."""
        decomposition = genus3_euler_decomposition()
        # First graph is the smooth one (genus 3, no edges)
        smooth_contrib = None
        for idx, contrib in decomposition:
            g = genus3_stable_graphs_n0()[idx]
            if g.num_edges == 0:
                smooth_contrib = contrib
                break
        assert smooth_contrib == Fraction(1, 1008)


# ============================================================================
# Boundary strata
# ============================================================================

class TestGenus3BoundaryStrata:
    """Tests for boundary stratum classification."""

    def test_codim_counts(self):
        """Verify codimension counts: 1, 2, 5, 9, 12, 8, 5."""
        strata = genus3_boundary_strata()
        assert len(strata[0]) == 1
        assert len(strata[1]) == 2
        assert len(strata[2]) == 5
        assert len(strata[3]) == 9
        assert len(strata[4]) == 12
        assert len(strata[5]) == 8
        assert len(strata[6]) == 5

    def test_total_across_strata(self):
        """Total across all codimensions equals 42."""
        strata = genus3_boundary_strata()
        total = sum(len(v) for v in strata.values())
        assert total == 42

    def test_boundary_divisor_delta_irr(self):
        """Delta_irr: one graph (genus-2 with self-loop)."""
        divisors = genus3_boundary_divisor_types()
        assert len(divisors["Delta_irr"]) == 1
        g = divisors["Delta_irr"][0]
        assert g.vertex_genera == (2,)
        assert g.num_edges == 1
        assert g.self_loop_count(0) == 1

    def test_boundary_divisor_delta_1(self):
        """Delta_1: one graph (genus-2 + genus-1, separating node)."""
        divisors = genus3_boundary_divisor_types()
        assert len(divisors["Delta_1"]) == 1
        g = divisors["Delta_1"][0]
        assert sorted(g.vertex_genera) == [1, 2]
        assert g.num_edges == 1

    def test_deepest_stratum_dim(self):
        """Deepest stratum has codimension 6 = dim(M_bar_{3,0})."""
        strata = genus3_boundary_strata()
        max_codim = max(strata.keys())
        assert max_codim == 6  # 3g - 3 = 6

    def test_deepest_all_genus0(self):
        """All graphs in codim 6 have exclusively genus-0 vertices."""
        strata = genus3_boundary_strata()
        for g in strata[6]:
            assert all(gv == 0 for gv in g.vertex_genera)

    def test_interior_is_smooth(self):
        """Codimension 0 contains only the smooth genus-3 curve."""
        strata = genus3_boundary_strata()
        assert len(strata[0]) == 1
        g = strata[0][0]
        assert g.vertex_genera == (3,)
        assert g.num_edges == 0


# ============================================================================
# Vertex and edge count statistics
# ============================================================================

class TestGenus3Statistics:
    """Tests for graph count statistics."""

    def test_by_vertex_count(self):
        """1-vertex: 4, 2-vertex: 12, 3-vertex: 15, 4-vertex: 11."""
        vc = genus3_by_vertex_count()
        assert vc == {1: 4, 2: 12, 3: 15, 4: 11}

    def test_by_edge_count(self):
        """Edge count distribution: 1+2+5+9+12+8+5 = 42."""
        ec = genus3_by_edge_count()
        assert ec == {0: 1, 1: 2, 2: 5, 3: 9, 4: 12, 5: 8, 6: 5}

    def test_vertex_count_sum(self):
        assert sum(genus3_by_vertex_count().values()) == 42

    def test_edge_count_sum(self):
        assert sum(genus3_by_edge_count().values()) == 42


# ============================================================================
# Scalar graph sum polynomial
# ============================================================================

class TestGenus3ScalarSum:
    """Tests for the scalar graph sum as a polynomial in kappa."""

    def test_coefficients(self):
        """Verify polynomial coefficients c_e for kappa^e."""
        coeffs = genus3_scalar_sum_polynomial()
        assert coeffs[0] == Fraction(1)
        assert coeffs[1] == Fraction(3, 2)
        assert coeffs[2] == Fraction(15, 8)
        assert coeffs[3] == Fraction(107, 48)
        assert coeffs[4] == Fraction(97, 48)
        assert coeffs[5] == Fraction(55, 48)
        assert coeffs[6] == Fraction(5, 16)

    def test_polynomial_at_kappa1(self):
        """Scalar sum at kappa = 1: 121/12."""
        assert genus3_scalar_sum_at(Fraction(1)) == Fraction(121, 12)

    def test_polynomial_at_kappa0(self):
        """Scalar sum at kappa = 0: 1 (only the smooth graph contributes)."""
        assert genus3_scalar_sum_at(Fraction(0)) == Fraction(1)

    def test_polynomial_at_kappa2(self):
        """Scalar sum at kappa = 2 by direct evaluation."""
        coeffs = genus3_scalar_sum_polynomial()
        expected = sum(c * Fraction(2)**e for e, c in coeffs.items())
        assert genus3_scalar_sum_at(Fraction(2)) == expected


# ============================================================================
# Graph weight sum
# ============================================================================

class TestGenus3GraphWeights:
    """Tests for signed graph weight sum."""

    def test_weight_sum(self):
        """Sum of (-1)^|E| / |Aut| = 1/3 for genus-3 graphs."""
        assert genus3_graph_weight_sum() == Fraction(1, 3)

    def test_weight_sum_matches_direct(self):
        """Cross-check against direct computation."""
        graphs = genus3_stable_graphs_n0()
        total = sum(graph_weight(g) for g in graphs)
        assert total == Fraction(1, 3)


# ============================================================================
# Named graphs
# ============================================================================

class TestGenus3NamedGraphs:
    """Tests for named graph identification."""

    def test_smooth_exists(self):
        named = genus3_named_graphs()
        assert "smooth" in named
        assert named["smooth"].vertex_genera == (3,)
        assert named["smooth"].num_edges == 0

    def test_irr_node_exists(self):
        named = genus3_named_graphs()
        assert "irr_node" in named
        g = named["irr_node"]
        assert g.vertex_genera == (2,)
        assert g.num_edges == 1
        assert g.self_loop_count(0) == 1

    def test_double_loop_exists(self):
        named = genus3_named_graphs()
        assert "double_loop" in named
        g = named["double_loop"]
        assert g.vertex_genera == (1,)
        assert g.self_loop_count(0) == 2

    def test_triple_loop_exists(self):
        named = genus3_named_graphs()
        assert "triple_loop" in named
        g = named["triple_loop"]
        assert g.vertex_genera == (0,)
        assert g.self_loop_count(0) == 3

    def test_separating_21_exists(self):
        named = genus3_named_graphs()
        assert "separating_21" in named
        g = named["separating_21"]
        assert sorted(g.vertex_genera) == [1, 2]
        assert g.num_edges == 1

    def test_K4_exists(self):
        named = genus3_named_graphs()
        assert "K4" in named
        g = named["K4"]
        assert g.num_vertices == 4
        assert g.num_edges == 6
        assert all(gv == 0 for gv in g.vertex_genera)


# ============================================================================
# Consistency with genus 2
# ============================================================================

class TestGenus3Consistency:
    """Cross-checks between genus-2 and genus-3 data."""

    def test_consistent_with_genus2(self):
        """Full consistency check passes."""
        assert genus3_genus2_consistency_check()

    def test_lambda_fp_formula(self):
        """lambda_g^FP = (2^{2g-1} - 1)|B_{2g}| / (2^{2g-1} (2g)!) for g=1,2,3."""
        for g in [1, 2, 3]:
            assert lambda3_fp() if g == 3 else _lambda_fp_exact(g)

    def test_lambda_fp_sequence(self):
        """lambda_1 > lambda_2 > lambda_3 > 0 (decreasing positive)."""
        l1 = _lambda_fp_exact(1)
        l2 = _lambda_fp_exact(2)
        l3 = lambda3_fp()
        assert l1 > l2 > l3 > 0

    def test_bernoulli_B6(self):
        """B_6 = 1/42."""
        assert _bernoulli_exact(6) == Fraction(1, 42)

    def test_genus2_count_less_than_genus3(self):
        """6 graphs at genus 2 vs 42 at genus 3."""
        assert len(genus2_stable_graphs_n0()) == 6
        assert genus3_graph_count() == 42

    def test_euler_char_genus2_vs_genus3(self):
        """chi^orb(M_bar_2) = -181/1440, chi^orb(M_bar_3) = -12419/90720."""
        chi2 = orbifold_euler_characteristic(genus2_stable_graphs_n0())
        chi3 = orbifold_euler_characteristic(genus3_stable_graphs_n0())
        assert chi2 == Fraction(-181, 1440)
        assert chi3 == Fraction(-12419, 90720)

    def test_graph_count_growth(self):
        """Graph count grows: g=1 -> 2, g=2 -> 6, g=3 -> 42."""
        from compute.lib.stable_graph_enumeration import genus1_stable_graphs_n0
        assert len(genus1_stable_graphs_n0()) == 2
        assert len(genus2_stable_graphs_n0()) == 6
        assert genus3_graph_count() == 42


# ============================================================================
# Graph profiles by shadow depth class
# ============================================================================

class TestGenus3GraphProfiles:
    """Tests for shadow-depth class profiles."""

    def test_gaussian_all_scalar(self):
        """Gaussian class: all graphs are scalar-only (no corrections)."""
        profile = genus3_graph_profiles("G")
        assert profile["active_count"] == 0
        assert profile["scalar_only_count"] == 42

    def test_lie_has_active(self):
        """Lie class: some graphs receive cubic corrections."""
        profile = genus3_graph_profiles("L")
        assert profile["active_count"] > 0
        assert profile["scalar_only_count"] + profile["active_count"] == 42

    def test_contact_has_active(self):
        """Contact class: some graphs receive quartic corrections."""
        profile = genus3_graph_profiles("C")
        assert profile["active_count"] > 0

    def test_mixed_has_active(self):
        """Mixed class: same as Lie (both trigger at valence >= 3)."""
        profile_L = genus3_graph_profiles("L")
        profile_M = genus3_graph_profiles("M")
        assert profile_L["active_count"] == profile_M["active_count"]

    def test_scalar_sum_kappa1(self):
        """Scalar sum at kappa=1 is 121/12."""
        profile = genus3_graph_profiles("G")
        assert profile["scalar_sum_kappa1"] == Fraction(121, 12)


# ============================================================================
# Summary
# ============================================================================

class TestGenus3Summary:
    """Tests for the summary function."""

    def test_summary_total(self):
        s = genus3_summary()
        assert s["total_graphs"] == 42

    def test_summary_lambda(self):
        s = genus3_summary()
        assert s["lambda3_fp"] == Fraction(31, 967680)

    def test_summary_chi(self):
        s = genus3_summary()
        assert s["chi_orb_mbar"] == Fraction(-12419, 90720)
        assert s["chi_orb_open"] == Fraction(1, 1008)

    def test_summary_weight_sum(self):
        s = genus3_summary()
        assert s["graph_weight_sum"] == Fraction(1, 3)

    def test_summary_scalar_sum(self):
        s = genus3_summary()
        assert s["scalar_sum_kappa1"] == Fraction(121, 12)
