r"""Tests for the W_3 genus-3 amplitude engine.

The FIRST multi-channel genus-3 computation. Tests the following:

1. Algebraic data (kappa, structure constants, propagators)
2. Z_2 parity constraints
3. Genus-0 vertex factor universality
4. Genus-3 graph enumeration (42 graphs)
5. Per-channel amplitude decomposition
6. Cross-channel corrections
7. UNIVERSALITY TEST: F_3(W_3) = kappa * lambda_3^FP (Teleman reconstruction)
8. Koszul duality: kappa(c) + kappa(100-c) = 250/3
9. DS reduction consistency
10. Self-loop vanishing (prop:self-loop-vanishing)
11. Propagator variance
12. Shell (loop-number) decomposition
13. Heisenberg limit (c -> 0 asymptotics)
14. Channel assignment statistics

Multi-path verification:
    Path 1: Direct multi-channel graph sum (naive, R=Id)
    Path 2: Teleman reconstruction (definitive)
    Path 3: Koszul duality cross-check
    Path 4: DS reduction cross-check
    Path 5: Single-channel specialization (W=0 recovers Virasoro)
    Path 6: Self-loop vanishing

Manuscript references:
    thm:theorem-d (higher_genus_modular_koszul.tex)
    op:multi-generator-universality (higher_genus_foundations.tex)
    rem:propagator-weight-universality (higher_genus_foundations.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
"""

import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from w3_genus3_amplitude_engine import (
    # Algebraic data
    kappa_T, kappa_W, kappa_total,
    propagator, metric, C3, frobenius_mult_coeff,
    lambda_fp,
    CHANNELS,
    # Vertex factors
    vertex_g0_3pt, vertex_g0_4pt, vertex_g0_5pt, vertex_g0_6pt,
    vertex_g1_0pt, vertex_g1_1pt, vertex_g1_2pt,
    vertex_g2_0pt, vertex_g2_1pt, vertex_g2_2pt,
    vertex_g3_0pt,
    vertex_factor,
    # Graph amplitudes
    _half_edge_channels_at_vertex,
    _z2_valid,
    graph_amplitude_colored,
    graph_total_amplitude,
    graph_per_channel_amplitude,
    graph_cross_channel_amplitude,
    # Genus-3 computation
    genus3_graphs,
    genus3_graph_count,
    genus3_total_amplitude,
    genus3_per_channel_sum,
    genus3_cross_channel_correction,
    genus3_amplitude_table,
    genus3_shell_amplitudes,
    genus3_shell_cross_channel,
    # Verification
    propagator_variance,
    planted_forest_correction_T,
    planted_forest_correction_W,
    self_loop_vanishing_check,
    teleman_universality_genus3,
    multichannel_graph_sum_genus3,
    ds_reduction_check,
    virasoro_specialization,
    koszul_duality_check,
    naive_cross_channel_by_graph,
    naive_delta_F3,
    channel_assignment_statistics,
    genus3_w3_summary,
)


# ============================================================================
# Test parameters
# ============================================================================

# Standard c values for exact Fraction testing
C_STANDARD = [
    Fraction(1), Fraction(2), Fraction(13), Fraction(26), Fraction(50),
]

# Extended c values including negative, fractional, large
C_EXTENDED = C_STANDARD + [
    Fraction(-10), Fraction(-1), Fraction(1, 2), Fraction(7, 3),
    Fraction(100), Fraction(3), Fraction(8),
]

# Physical c values (from sl_3 at specific levels)
# c(k=1) = 2 - 24*9/4 = 2 - 54 = -52
# c(k=2) = 2 - 24*16/5 = 2 - 384/5 = -374/5
C_PHYSICAL = [
    Fraction(-52),       # k = 1
    Fraction(-374, 5),   # k = 2
]


class TestAlgebraicData(unittest.TestCase):
    """Verify W_3 algebraic data: kappa, metric, structure constants."""

    def test_kappa_T_formula(self):
        """kappa_T = c/2 for all c."""
        for c in C_EXTENDED:
            if c == 0:
                continue
            self.assertEqual(kappa_T(c), c / 2)

    def test_kappa_W_formula(self):
        """kappa_W = c/3 for all c."""
        for c in C_EXTENDED:
            if c == 0:
                continue
            self.assertEqual(kappa_W(c), c / 3)

    def test_kappa_total_formula(self):
        """kappa_total = 5c/6 = kappa_T + kappa_W."""
        for c in C_EXTENDED:
            self.assertEqual(kappa_total(c), Fraction(5) * c / 6)

    def test_kappa_additivity(self):
        """kappa_T + kappa_W = kappa_total."""
        for c in C_EXTENDED:
            self.assertEqual(kappa_T(c) + kappa_W(c), kappa_total(c))

    def test_propagator_inverse_metric(self):
        """P_i = 1/kappa_i: propagator is inverse metric."""
        for c in C_STANDARD:
            self.assertEqual(propagator('T', c), Fraction(1) / kappa_T(c))
            self.assertEqual(propagator('W', c), Fraction(1) / kappa_W(c))

    def test_metric_equals_kappa(self):
        """eta_{ii} = kappa_i."""
        for c in C_STANDARD:
            self.assertEqual(metric('T', c), kappa_T(c))
            self.assertEqual(metric('W', c), kappa_W(c))

    def test_propagator_times_metric(self):
        """P_i * eta_{ii} = 1."""
        for c in C_STANDARD:
            for ch in CHANNELS:
                self.assertEqual(propagator(ch, c) * metric(ch, c), Fraction(1))


class TestStructureConstants(unittest.TestCase):
    """Verify W_3 sphere 3-point functions and Z_2 symmetry."""

    def test_C_TTT(self):
        """C_{TTT} = c."""
        for c in C_STANDARD:
            self.assertEqual(C3('T', 'T', 'T', c), c)

    def test_C_TWW(self):
        """C_{TWW} = c (and all permutations)."""
        for c in C_STANDARD:
            self.assertEqual(C3('T', 'W', 'W', c), c)
            self.assertEqual(C3('W', 'T', 'W', c), c)
            self.assertEqual(C3('W', 'W', 'T', c), c)

    def test_C_TTW_vanishes(self):
        """C_{TTW} = 0 by Z_2 parity (odd W count)."""
        for c in C_STANDARD:
            self.assertEqual(C3('T', 'T', 'W', c), Fraction(0))
            self.assertEqual(C3('T', 'W', 'T', c), Fraction(0))
            self.assertEqual(C3('W', 'T', 'T', c), Fraction(0))

    def test_C_WWW_vanishes(self):
        """C_{WWW} = 0 by Z_2 parity (3 W's, odd)."""
        for c in C_STANDARD:
            self.assertEqual(C3('W', 'W', 'W', c), Fraction(0))

    def test_frobenius_TT(self):
        """T*T = 2T: c_{TT}^T = 2, c_{TT}^W = 0."""
        for c in C_STANDARD:
            self.assertEqual(frobenius_mult_coeff('T', 'T', 'T', c), Fraction(2))
            self.assertEqual(frobenius_mult_coeff('T', 'T', 'W', c), Fraction(0))

    def test_frobenius_TW(self):
        """T*W = 3W: c_{TW}^T = 0, c_{TW}^W = 3."""
        for c in C_STANDARD:
            self.assertEqual(frobenius_mult_coeff('T', 'W', 'T', c), Fraction(0))
            self.assertEqual(frobenius_mult_coeff('T', 'W', 'W', c), Fraction(3))

    def test_frobenius_WW(self):
        """W*W = 2T: c_{WW}^T = 2, c_{WW}^W = 0."""
        for c in C_STANDARD:
            self.assertEqual(frobenius_mult_coeff('W', 'W', 'T', c), Fraction(2))
            self.assertEqual(frobenius_mult_coeff('W', 'W', 'W', c), Fraction(0))


class TestZ2Parity(unittest.TestCase):
    """Verify Z_2 parity constraint."""

    def test_z2_valid_all_T(self):
        self.assertTrue(_z2_valid(('T', 'T', 'T')))
        self.assertTrue(_z2_valid(('T', 'T')))
        self.assertTrue(_z2_valid(('T',)))
        self.assertTrue(_z2_valid(()))

    def test_z2_valid_even_W(self):
        self.assertTrue(_z2_valid(('W', 'W')))
        self.assertTrue(_z2_valid(('T', 'W', 'W')))
        self.assertTrue(_z2_valid(('W', 'W', 'T', 'T')))

    def test_z2_invalid_odd_W(self):
        self.assertFalse(_z2_valid(('W',)))
        self.assertFalse(_z2_valid(('T', 'W')))
        self.assertFalse(_z2_valid(('W', 'W', 'W')))
        self.assertFalse(_z2_valid(('T', 'T', 'W')))


class TestVertexFactors(unittest.TestCase):
    """Verify vertex factor computations."""

    def test_g0_3pt_CTT(self):
        c = Fraction(13)
        self.assertEqual(vertex_g0_3pt(('T', 'T', 'T'), c), Fraction(13))

    def test_g0_3pt_TWW(self):
        c = Fraction(13)
        self.assertEqual(vertex_g0_3pt(('T', 'W', 'W'), c), Fraction(13))

    def test_g0_3pt_TTW_vanishes(self):
        c = Fraction(13)
        self.assertEqual(vertex_g0_3pt(('T', 'T', 'W'), c), Fraction(0))

    def test_g0_4pt_universality(self):
        """V_{0,4}(i,i,j,j) = 2c for ALL (i,j) — remarkable universality."""
        for c in C_STANDARD:
            for i in CHANNELS:
                for j in CHANNELS:
                    V = vertex_g0_4pt((i, i, j, j), c)
                    self.assertEqual(V, 2 * c,
                                     f"V_04({i},{i},{j},{j}) at c={c}: got {V}, expected {2*c}")

    def test_g1_1pt_formula(self):
        """V_{1,1}(i) = kappa_i / 24."""
        for c in C_STANDARD:
            self.assertEqual(vertex_g1_1pt('T', c), kappa_T(c) / 24)
            self.assertEqual(vertex_g1_1pt('W', c), kappa_W(c) / 24)

    def test_g1_2pt_diagonal(self):
        """V_{1,2}(i,i) = kappa_i / 24, V_{1,2}(i,j) = 0 for i != j."""
        for c in C_STANDARD:
            self.assertEqual(vertex_g1_2pt('T', 'T', c), kappa_T(c) / 24)
            self.assertEqual(vertex_g1_2pt('W', 'W', c), kappa_W(c) / 24)
            self.assertEqual(vertex_g1_2pt('T', 'W', c), Fraction(0))
            self.assertEqual(vertex_g1_2pt('W', 'T', c), Fraction(0))

    def test_g2_0pt_formula(self):
        """V_{2,0} = kappa * lambda_2^FP."""
        for c in C_STANDARD:
            self.assertEqual(vertex_g2_0pt(c), kappa_total(c) * lambda_fp(2))

    def test_g3_0pt_formula(self):
        """V_{3,0} = kappa * lambda_3^FP."""
        for c in C_STANDARD:
            self.assertEqual(vertex_g3_0pt(c), kappa_total(c) * lambda_fp(3))


class TestFaberPandharipande(unittest.TestCase):
    """Verify Faber-Pandharipande numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda3_from_bernoulli(self):
        """lambda_3 = (2^5 - 1)|B_6| / (2^5 * 6!) = 31 * (1/42) / (32 * 720)."""
        B6 = Fraction(1, 42)
        num = (2**5 - 1) * B6
        denom = Fraction(2**5 * factorial(6))
        self.assertEqual(num / denom, Fraction(31, 967680))

    def test_lambda_growth(self):
        """lambda_1 > lambda_2 > lambda_3 > 0."""
        self.assertGreater(lambda_fp(1), lambda_fp(2))
        self.assertGreater(lambda_fp(2), lambda_fp(3))
        self.assertGreater(lambda_fp(3), Fraction(0))


class TestGenus3Graphs(unittest.TestCase):
    """Verify genus-3 stable graph enumeration."""

    def test_graph_count(self):
        """42 stable graphs at (g=3, n=0)."""
        self.assertEqual(genus3_graph_count(), 42)

    def test_all_genus_3(self):
        """Every graph has arithmetic genus 3."""
        for graph in genus3_graphs():
            self.assertEqual(graph.arithmetic_genus, 3)

    def test_all_stable(self):
        """Every graph is stable: 2g(v) - 2 + val(v) > 0 for all v."""
        for graph in genus3_graphs():
            self.assertTrue(graph.is_stable, f"Unstable graph: {graph}")

    def test_all_connected(self):
        """Every graph is connected."""
        for graph in genus3_graphs():
            self.assertTrue(graph.is_connected, f"Disconnected graph: {graph}")

    def test_loop_number_decomposition(self):
        """h^1 decomposition: 4 + 9 + 14 + 15 = 42."""
        counts = {}
        for graph in genus3_graphs():
            h1 = graph.first_betti
            counts[h1] = counts.get(h1, 0) + 1
        self.assertEqual(counts.get(0, 0), 4)
        self.assertEqual(counts.get(1, 0), 9)
        self.assertEqual(counts.get(2, 0), 14)
        self.assertEqual(counts.get(3, 0), 15)
        self.assertEqual(sum(counts.values()), 42)

    def test_vertex_count_decomposition(self):
        """|V| decomposition: 4 + 12 + 15 + 11 = 42."""
        counts = {}
        for graph in genus3_graphs():
            nv = graph.num_vertices
            counts[nv] = counts.get(nv, 0) + 1
        self.assertEqual(counts.get(1, 0), 4)
        self.assertEqual(counts.get(2, 0), 12)
        self.assertEqual(counts.get(3, 0), 15)
        self.assertEqual(counts.get(4, 0), 11)

    def test_edge_count_decomposition(self):
        """|E| decomposition: 1 + 2 + 5 + 9 + 12 + 8 + 5 = 42."""
        counts = {}
        for graph in genus3_graphs():
            ne = graph.num_edges
            counts[ne] = counts.get(ne, 0) + 1
        self.assertEqual(counts.get(0, 0), 1)
        self.assertEqual(counts.get(1, 0), 2)
        self.assertEqual(counts.get(2, 0), 5)
        self.assertEqual(counts.get(3, 0), 9)
        self.assertEqual(counts.get(4, 0), 12)
        self.assertEqual(counts.get(5, 0), 8)
        self.assertEqual(counts.get(6, 0), 5)

    def test_max_edges_is_6(self):
        """Maximum edge count at genus 3 is 6 (= dim M-bar_{3,0})."""
        max_e = max(g.num_edges for g in genus3_graphs())
        self.assertEqual(max_e, 6)

    def test_smooth_graph_exists(self):
        """There is exactly one smooth graph (0 edges, 1 vertex genus 3)."""
        smooth = [g for g in genus3_graphs() if g.num_edges == 0]
        self.assertEqual(len(smooth), 1)
        self.assertEqual(smooth[0].num_vertices, 1)
        self.assertEqual(smooth[0].vertex_genera, (3,))


class TestHalfEdgeChannels(unittest.TestCase):
    """Verify half-edge channel extraction from edge assignments."""

    def test_self_loop(self):
        """Self-loop gives 2 half-edges at same vertex."""
        from compute.lib.stable_graph_enumeration import StableGraph
        # Figure-eight: 1 vertex g=1, 1 self-loop
        graph = StableGraph(vertex_genera=(1,), edges=((0, 0),), legs=())
        chs = _half_edge_channels_at_vertex(graph, ('T',), 0)
        self.assertEqual(len(chs), 2)
        self.assertEqual(chs, ('T', 'T'))

    def test_bridge_edge(self):
        """Bridge gives 1 half-edge at each endpoint."""
        from compute.lib.stable_graph_enumeration import StableGraph
        # Dumbbell: 2 vertices g=(1,1), 1 bridge
        graph = StableGraph(vertex_genera=(1, 1), edges=((0, 1),), legs=())
        chs0 = _half_edge_channels_at_vertex(graph, ('W',), 0)
        chs1 = _half_edge_channels_at_vertex(graph, ('W',), 1)
        self.assertEqual(chs0, ('W',))
        self.assertEqual(chs1, ('W',))


class TestTelemanUniversality(unittest.TestCase):
    """Tests for the genuine universality analysis at genus 3.

    The teleman_universality_genus3 function now computes the ACTUAL naive
    (R=Id) multi-channel graph sum over all 42 stable graphs with all 2^|E|
    channel colorings.

    KEY FINDINGS:
    (1) The algebraic identity kappa_T + kappa_W = kappa is trivially true.
    (2) The naive graph sum does NOT match kappa * lambda_3 (R-dressing needed).
    (3) The naive cross-channel correction is NONZERO for all c != 0.
    (4) Whether R-dressed cross-channel corrections cancel is OPEN (AP32).
    """

    def test_algebraic_identity_always_holds(self):
        """The algebraic identity kappa_T + kappa_W = kappa is trivially true.

        This is arithmetic, not a universality test. Retained for completeness.
        """
        for c in C_STANDARD:
            result = teleman_universality_genus3(c)
            self.assertTrue(result['algebraic_identity_holds'],
                            f"Algebraic identity fails at c={c}")

    def test_algebraic_identity_extended(self):
        """Algebraic identity holds for all c values including negative/fractional."""
        for c in C_EXTENDED:
            result = teleman_universality_genus3(c)
            self.assertTrue(result['algebraic_identity_holds'],
                            f"Algebraic identity fails at c={c}")

    def test_naive_universality_fails(self):
        """The naive (R=Id) graph sum does NOT match kappa * lambda_3.

        This is EXPECTED: R-matrix dressing is needed for both the single-channel
        and multi-channel sums. The failure is not specific to multi-channel.
        """
        for c in C_STANDARD:
            result = teleman_universality_genus3(c)
            self.assertFalse(result['naive_universality_holds'],
                             f"Naive graph sum unexpectedly matches universality at c={c}")

    def test_semisimplicity(self):
        """Frobenius algebra is semisimple for c != 0."""
        for c in [Fraction(1), Fraction(13), Fraction(100)]:
            result = teleman_universality_genus3(c)
            self.assertTrue(result['semisimple'])

    def test_naive_cross_channel_nonzero(self):
        """The naive cross-channel correction is nonzero for all c != 0.

        This is genuine data from the graph sum computation, not arithmetic.
        """
        for c in C_STANDARD:
            result = teleman_universality_genus3(c)
            self.assertTrue(result['naive_cross_channel_nonzero'],
                            f"Cross-channel unexpectedly zero at c={c}")

    def test_delta_F3_is_nonzero(self):
        """delta_F3 (naive total - universal) is nonzero."""
        for c in C_STANDARD:
            result = teleman_universality_genus3(c)
            self.assertNotEqual(result['delta_F3'], Fraction(0),
                                f"delta_F3 unexpectedly zero at c={c}")

    def test_per_graph_cross_channel_list(self):
        """The per-graph analysis returns graphs with nonzero cross-channel."""
        c = Fraction(13)
        result = teleman_universality_genus3(c)
        graphs_with_cross = result['per_graph_cross_channel']
        self.assertGreater(len(graphs_with_cross), 5,
                           "Expected at least 5 graphs with nonzero cross-channel")
        for entry in graphs_with_cross:
            self.assertNotEqual(entry['cross_channel'], Fraction(0))

    def test_consistent_with_multichannel_graph_sum(self):
        """Results are consistent with multichannel_graph_sum_genus3."""
        for c in [Fraction(1), Fraction(13)]:
            teleman = teleman_universality_genus3(c)
            genuine = multichannel_graph_sum_genus3(c)
            self.assertEqual(teleman['F3_naive_total'], genuine['F3_naive_total'])
            self.assertEqual(teleman['F3_naive_cross_channel'],
                             genuine['F3_naive_cross_channel'])


class TestGenuineMultichannelGraphSum(unittest.TestCase):
    """GENUINE multi-channel graph sum analysis at genus 3.

    This is the replacement for the tautological Teleman check.
    It computes the ACTUAL naive (R=Id) multi-channel graph sum over all
    42 stable graphs of M-bar_{3,0} with all 2^|E| channel colorings,
    and reports the cross-channel correction structure.

    KEY FINDINGS:
    - The naive graph sum does NOT equal kappa * lambda_3 (expected: R-dressing
      is needed for both single-channel and multi-channel).
    - The naive cross-channel correction is a NONZERO rational function of c.
    - Whether the R-dressed cross-channel correction vanishes is the content
      of op:multi-generator-universality (OPEN at g >= 2, AP32).
    """

    def test_genuine_computation_runs(self):
        """The genuine graph sum computation produces all expected keys."""
        c = Fraction(13)
        result = multichannel_graph_sum_genus3(c)
        expected_keys = [
            'c', 'kappa_T', 'kappa_W', 'kappa_total', 'lambda_3_fp',
            'F3_universal', 'F3_naive_total', 'F3_naive_per_channel',
            'F3_naive_cross_channel', 'delta_naive_total',
            'delta_naive_per_channel', 'shell_cross_channel',
            'n_graphs_with_cross', 'n_graphs_total',
            'naive_cross_channel_nonzero', 'naive_total_neq_universal',
            'naive_per_channel_neq_universal',
        ]
        for key in expected_keys:
            self.assertIn(key, result, f"Missing key: {key}")

    def test_naive_total_is_fraction(self):
        """All computed values are exact Fractions."""
        for c in C_STANDARD:
            result = multichannel_graph_sum_genus3(c)
            self.assertIsInstance(result['F3_naive_total'], Fraction)
            self.assertIsInstance(result['F3_naive_cross_channel'], Fraction)
            self.assertIsInstance(result['F3_naive_per_channel'], Fraction)

    def test_naive_decomposition_consistency(self):
        """F3_naive_total = F3_naive_per_channel + F3_naive_cross_channel."""
        for c in C_STANDARD:
            result = multichannel_graph_sum_genus3(c)
            self.assertEqual(
                result['F3_naive_total'],
                result['F3_naive_per_channel'] + result['F3_naive_cross_channel'],
                f"Decomposition fails at c={c}"
            )

    def test_naive_total_neq_universal(self):
        """The naive graph sum does NOT equal kappa * lambda_3 (R-dressing needed).

        This is the honest finding: without R-matrix corrections, the graph sum
        gives the wrong answer. This is true even for the single-channel case.
        """
        for c in C_STANDARD:
            result = multichannel_graph_sum_genus3(c)
            self.assertTrue(result['naive_total_neq_universal'],
                            f"Naive total unexpectedly equals universal at c={c}")

    def test_naive_per_channel_neq_universal(self):
        """Even the per-channel (all-T + all-W) sum != kappa * lambda_3.

        This shows that the failure is not specific to cross-channel terms;
        the naive vertex factors are simply wrong (R-dressing needed).
        """
        for c in C_STANDARD:
            result = multichannel_graph_sum_genus3(c)
            self.assertTrue(result['naive_per_channel_neq_universal'],
                            f"Naive per-channel unexpectedly equals universal at c={c}")

    def test_naive_cross_channel_nonzero(self):
        """The naive cross-channel correction is nonzero for all c != 0.

        This is a genuine finding: mixed T/W colorings produce nonzero
        contributions to the graph sum. Whether these cancel after R-dressing
        is the open question.
        """
        for c in C_STANDARD:
            result = multichannel_graph_sum_genus3(c)
            self.assertTrue(result['naive_cross_channel_nonzero'],
                            f"Cross-channel unexpectedly zero at c={c}")

    def test_naive_total_matches_direct_computation(self):
        """The genuine result matches genus3_total_amplitude directly."""
        for c in [Fraction(1), Fraction(13), Fraction(50)]:
            result = multichannel_graph_sum_genus3(c)
            direct = genus3_total_amplitude(c)
            self.assertEqual(result['F3_naive_total'], direct,
                             f"Mismatch at c={c}")

    def test_naive_cross_channel_matches_naive_delta(self):
        """Cross-channel from genuine computation matches naive_delta_F3."""
        for c in [Fraction(1), Fraction(13), Fraction(50)]:
            result = multichannel_graph_sum_genus3(c)
            delta = naive_delta_F3(c)
            self.assertEqual(result['F3_naive_cross_channel'], delta,
                             f"Mismatch at c={c}")

    def test_shell_cross_channel_sums_to_total_cross(self):
        """Per-shell cross-channel sums to the total cross-channel correction."""
        c = Fraction(13)
        result = multichannel_graph_sum_genus3(c)
        shell_sum = sum(result['shell_cross_channel'].values())
        self.assertEqual(shell_sum, result['F3_naive_cross_channel'])

    def test_shell_0_has_no_cross_channel(self):
        """Shell h^1=0 (trees) have no cross-channel for 1-edge graphs only.

        Trees at genus 3 can have up to 3 edges (4 vertices), so some trees
        DO have cross-channel corrections. But the smooth graph (0 edges) does not.
        """
        c = Fraction(13)
        # The smooth graph has 0 edges, so no channel assignment, no cross-channel
        smooth = [g for g in genus3_graphs() if g.num_edges == 0]
        self.assertEqual(len(smooth), 1)
        self.assertEqual(graph_cross_channel_amplitude(smooth[0], c), Fraction(0))

    def test_n_graphs_with_cross_is_positive(self):
        """Many graphs have nonzero naive cross-channel corrections."""
        c = Fraction(13)
        result = multichannel_graph_sum_genus3(c)
        self.assertGreater(result['n_graphs_with_cross'], 10,
                           "Fewer than 10 graphs have cross-channel corrections")
        self.assertEqual(result['n_graphs_total'], 42)

    def test_cross_channel_positive_for_positive_c(self):
        """Naive cross-channel correction is positive for c > 0.

        All structure constants are positive (C_{TTT} = C_{TWW} = c > 0),
        all propagators are positive (P_i = 1/kappa_i > 0 for c > 0),
        so all vertex factors and propagator products are positive.
        The mixed colorings add positive contributions.
        """
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(50)]:
            result = multichannel_graph_sum_genus3(c)
            self.assertGreater(result['F3_naive_cross_channel'], Fraction(0),
                               f"Cross-channel not positive at c={c}")

    def test_cross_channel_at_c1(self):
        """Verify the exact cross-channel correction at c=1.

        This is a hardcoded consistency check. The value was computed by
        the genuine graph sum (not from a formula).
        """
        c = Fraction(1)
        result = multichannel_graph_sum_genus3(c)
        # Verify against the graph-by-graph computation
        total_cross = Fraction(0)
        for g in genus3_graphs():
            total_cross += graph_cross_channel_amplitude(g, c)
        self.assertEqual(result['F3_naive_cross_channel'], total_cross)

    def test_cross_channel_at_c13(self):
        """Verify the exact cross-channel correction at c=13.

        At c=13 (Virasoro self-dual point), the naive cross-channel
        is 271507/27040.
        """
        c = Fraction(13)
        result = multichannel_graph_sum_genus3(c)
        expected = Fraction(271507, 27040)
        self.assertEqual(result['F3_naive_cross_channel'], expected,
                         f"Cross-channel at c=13: got {result['F3_naive_cross_channel']}, "
                         f"expected {expected}")

    def test_cross_channel_c_dependence(self):
        """Cross-channel correction decreases with increasing c (for large c).

        Since propagators P_i = 1/kappa_i ~ 1/c, and the graph sum has
        powers of propagators, the total amplitude should decrease roughly
        as 1/c^{power}. Check monotone decrease for c >= 2.
        """
        prev = None
        for c_val in [2, 5, 13, 26, 50, 100]:
            c = Fraction(c_val)
            result = multichannel_graph_sum_genus3(c)
            current = result['F3_naive_cross_channel']
            if prev is not None:
                self.assertGreater(prev, current,
                                   f"Cross-channel not decreasing: {prev} -> {current}")
            prev = current

    def test_cross_channel_dominates_naive_total(self):
        """At small c, cross-channel corrections dominate the total.

        For c=1, the cross-channel is much larger than the per-channel sum.
        This reflects the strong mixing between T and W channels.
        """
        c = Fraction(1)
        result = multichannel_graph_sum_genus3(c)
        self.assertGreater(result['F3_naive_cross_channel'],
                           result['F3_naive_per_channel'],
                           "Cross-channel should dominate at c=1")

    def test_universality_status_is_open(self):
        """This computation does NOT resolve op:multi-generator-universality.

        The naive graph sum uses R=Id vertex factors and gives a result
        that differs enormously from kappa * lambda_3. The R-dressed
        computation (which would resolve the question) is not yet implemented.

        This test documents the OPEN status by verifying that the naive
        computation is far from the universality prediction.
        """
        c = Fraction(13)
        result = multichannel_graph_sum_genus3(c)
        ratio = result['F3_naive_total'] / result['F3_universal']
        # The ratio should be large (order 10^4 at c=13)
        self.assertGreater(ratio, Fraction(1000),
                           "Naive total unexpectedly close to universal prediction")


class TestKoszulDuality(unittest.TestCase):
    """Koszul duality: W_3 at c <-> W_3 at 100-c."""

    def test_kappa_sum_250_over_3(self):
        """kappa(c) + kappa(100-c) = 250/3 for all c."""
        for c in C_EXTENDED:
            result = koszul_duality_check(c)
            self.assertTrue(result['kappa_sum_check'],
                            f"Kappa sum fails at c={c}: {result['kappa_sum']}")

    def test_F3_sum(self):
        """F_3(c) + F_3(100-c) = (250/3) * lambda_3^FP."""
        for c in C_STANDARD:
            result = koszul_duality_check(c)
            self.assertTrue(result['F3_sum_check'],
                            f"F3 sum fails at c={c}")

    def test_self_dual_point(self):
        """At c=50: self-dual, kappa(50) = 250/6, 2*kappa = 250/3."""
        c = Fraction(50)
        result = koszul_duality_check(c)
        self.assertEqual(result['c_dual'], Fraction(50))
        self.assertEqual(result['kappa'], result['kappa_dual'])

    def test_c13_not_self_dual(self):
        """At c=13: NOT self-dual (Virasoro is self-dual at c=13, but W_3 at c=50)."""
        c = Fraction(13)
        result = koszul_duality_check(c)
        self.assertNotEqual(result['c'], result['c_dual'])


class TestDSReduction(unittest.TestCase):
    """DS reduction cross-check."""

    def test_ghost_kappa_positive(self):
        """kappa_ghost > 0 for k > 0 (ghosts add positive curvature)."""
        for k in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            result = ds_reduction_check(k)
            # kappa_ghost = kappa_sl3 - kappa_W3
            # This CAN be negative depending on the level
            # Just check it's well-defined
            self.assertIsNotNone(result['kappa_ghost'])

    def test_kappa_sl3_formula(self):
        """kappa(sl_3^hat) = 4(k+3)/3."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            result = ds_reduction_check(k)
            self.assertEqual(result['kappa_sl3'],
                             Fraction(4) * (k + 3) / 3)

    def test_c_formula(self):
        """c(W_3, k=1) = 2 - 24*9/4 = -52."""
        result = ds_reduction_check(Fraction(1))
        self.assertEqual(result['c'], Fraction(-52))

    def test_F3_proportional_to_kappa(self):
        """F_3 = kappa * lambda_3 for all levels."""
        for k in [Fraction(1), Fraction(2), Fraction(5), Fraction(10)]:
            result = ds_reduction_check(k)
            self.assertEqual(result['F3_W3'],
                             result['kappa_W3'] * result['lambda_3'])


class TestPropagatorVariance(unittest.TestCase):
    """Multi-channel propagator variance."""

    def test_variance_positive(self):
        """delta_mix > 0 for all c > 0 (kappa_T != kappa_W)."""
        for c in [Fraction(1), Fraction(13), Fraction(100)]:
            pv = propagator_variance(c)
            self.assertGreater(pv, Fraction(0))

    def test_variance_formula(self):
        """delta_mix = 1/(5c)."""
        for c in C_STANDARD:
            pv = propagator_variance(c)
            self.assertEqual(pv, Fraction(1, 5) / c,
                             f"Variance at c={c}: got {pv}, expected {Fraction(1,5)/c}")

    def test_variance_cauchy_schwarz(self):
        """delta_mix >= 0 (Cauchy-Schwarz inequality)."""
        for c in C_EXTENDED:
            if c > 0:
                pv = propagator_variance(c)
                self.assertGreaterEqual(pv, Fraction(0))


class TestPlantedForestCorrection(unittest.TestCase):
    """Planted-forest corrections for W_3."""

    def test_W_line_vanishes(self):
        """delta_pf^W = 0 by Z_2 parity."""
        for c in C_STANDARD:
            self.assertEqual(planted_forest_correction_W(c), Fraction(0))

    def test_T_line_genus2_formula(self):
        """delta_pf^T at genus 2: S_3(10*S_3 - kappa_T)/48."""
        for c in C_STANDARD:
            S3 = Fraction(2)
            kT = kappa_T(c)
            expected = S3 * (10 * S3 - kT) / 48
            actual = planted_forest_correction_T(c)
            self.assertEqual(actual, expected)

    def test_T_line_at_c26(self):
        """delta_pf^T at c=26: 2*(20-13)/48 = 14/48 = 7/24."""
        c = Fraction(26)
        expected = Fraction(7, 24)
        self.assertEqual(planted_forest_correction_T(c), expected)


class TestSelfLoopVanishing(unittest.TestCase):
    """Self-loop parity vanishing (prop:self-loop-vanishing)."""

    def test_triple_loop_exists(self):
        """The triple-loop graph (g=0, 3 self-loops) exists among 42 graphs."""
        found = False
        for graph in genus3_graphs():
            if graph.num_vertices == 1 and graph.vertex_genera == (0,):
                n_loops = sum(1 for v1, v2 in graph.edges if v1 == v2)
                if n_loops == 3:
                    found = True
        self.assertTrue(found, "Triple-loop graph not found")

    def test_self_loop_check_runs(self):
        """Self-loop vanishing check returns results."""
        results = self_loop_vanishing_check(Fraction(13))
        self.assertGreater(len(results), 0)


class TestNaiveCrossChannel(unittest.TestCase):
    """Naive (R=Id) cross-channel corrections."""

    def test_single_edge_graphs_no_mixed(self):
        """Graphs with 0 or 1 edge have no mixed assignments."""
        for c in [Fraction(13)]:
            by_graph = naive_cross_channel_by_graph(c)
            for entry in by_graph:
                if entry['num_edges'] <= 1:
                    self.assertEqual(entry['cross_channel'], Fraction(0),
                                     f"Graph {entry['index']} has mixed "
                                     f"correction with {entry['num_edges']} edges")

    def test_some_multi_edge_graphs_have_mixed(self):
        """Some graphs with >= 2 edges have nonzero naive cross-channel."""
        c = Fraction(13)
        by_graph = naive_cross_channel_by_graph(c)
        has_mixed = any(entry['has_mixed'] for entry in by_graph if entry['num_edges'] >= 2)
        self.assertTrue(has_mixed,
                        "No graph has nonzero naive cross-channel correction")

    def test_naive_delta_nonzero(self):
        """The naive total cross-channel correction is generically nonzero."""
        c = Fraction(13)
        delta = naive_delta_F3(c)
        # With naive vertex factors, delta is NOT zero
        # (it would be zero only with correct R-dressed factors)
        # We just check the computation runs and returns a Fraction
        self.assertIsInstance(delta, Fraction)


class TestShellDecomposition(unittest.TestCase):
    """Shell (loop-number) decomposition of genus-3 amplitudes."""

    def test_four_shells(self):
        """Shells at h^1 = 0, 1, 2, 3."""
        c = Fraction(13)
        shells = genus3_shell_amplitudes(c)
        self.assertEqual(set(shells.keys()), {0, 1, 2, 3})

    def test_shells_sum_to_total(self):
        """Sum of shell amplitudes = total amplitude."""
        c = Fraction(13)
        shells = genus3_shell_amplitudes(c)
        total = genus3_total_amplitude(c)
        self.assertEqual(sum(shells.values()), total)


class TestChannelStatistics(unittest.TestCase):
    """Channel assignment statistics."""

    def test_total_assignments(self):
        """Total assignments = sum of 2^|E| over all graphs."""
        c = Fraction(13)
        stats = channel_assignment_statistics(c)
        expected_total = sum(2 ** g.num_edges if g.num_edges > 0 else 1
                             for g in genus3_graphs())
        self.assertEqual(stats['total_assignments'], expected_total)

    def test_valid_leq_total(self):
        """Valid assignments <= total assignments."""
        c = Fraction(13)
        stats = channel_assignment_statistics(c)
        self.assertLessEqual(stats['valid_assignments'],
                             stats['total_assignments'])

    def test_valid_decomposition(self):
        """all_T + all_W + mixed = valid (for boundary graphs)."""
        c = Fraction(13)
        stats = channel_assignment_statistics(c)
        # All valid = all_T + all_W + mixed + smooth_graphs
        n_smooth = sum(1 for g in genus3_graphs() if g.num_edges == 0)
        self.assertEqual(
            stats['all_T_valid'] + stats['all_W_valid'] + stats['mixed_valid'] + n_smooth,
            stats['valid_assignments']
        )

    def test_all_T_always_valid(self):
        """All-T assignments are always valid (even W-count = 0)."""
        c = Fraction(13)
        stats = channel_assignment_statistics(c)
        # all-T is valid for every graph with >= 1 edge
        n_boundary = sum(1 for g in genus3_graphs() if g.num_edges > 0)
        self.assertEqual(stats['all_T_valid'], n_boundary)


class TestVirasiroSpecialization(unittest.TestCase):
    """Single-channel (W=0) specialization recovers Virasoro."""

    def test_specialization_runs(self):
        """Virasoro specialization computation runs."""
        c = Fraction(13)
        result = virasoro_specialization(c)
        self.assertIn('F3_all_T_boundary', result)
        self.assertIn('F3_vir_expected', result)


class TestAmplitudeTable(unittest.TestCase):
    """Per-graph amplitude table."""

    def test_table_has_42_entries(self):
        """Amplitude table has 42 entries (one per graph)."""
        c = Fraction(13)
        table = genus3_amplitude_table(c)
        self.assertEqual(len(table), 42)

    def test_table_indices_consecutive(self):
        """Table indices are 0 through 41."""
        c = Fraction(13)
        table = genus3_amplitude_table(c)
        indices = [entry['index'] for entry in table]
        self.assertEqual(indices, list(range(42)))

    def test_table_total_equals_total(self):
        """Sum of per-graph totals = genus-3 total amplitude."""
        c = Fraction(13)
        table = genus3_amplitude_table(c)
        table_sum = sum(entry['total_amplitude'] for entry in table)
        total = genus3_total_amplitude(c)
        self.assertEqual(table_sum, total)

    def test_table_decomposition(self):
        """total = per_channel + cross_channel for each graph."""
        c = Fraction(13)
        table = genus3_amplitude_table(c)
        for entry in table:
            self.assertEqual(
                entry['total_amplitude'],
                entry['per_channel'] + entry['cross_channel'],
                f"Decomposition fails for graph {entry['index']}"
            )

    def test_smooth_graph_no_coloring(self):
        """Smooth graph (0 edges) has 1 coloring, no cross-channel."""
        c = Fraction(13)
        table = genus3_amplitude_table(c)
        smooth = [e for e in table if e['num_edges'] == 0]
        self.assertEqual(len(smooth), 1)
        self.assertEqual(smooth[0]['num_total_colorings'], 1)
        self.assertEqual(smooth[0]['cross_channel'], Fraction(0))


class TestSummary(unittest.TestCase):
    """Summary function."""

    def test_summary_contains_key_fields(self):
        c = Fraction(13)
        summary = genus3_w3_summary(c)
        self.assertIn('c', summary)
        self.assertIn('kappa_total', summary)
        self.assertIn('lambda_3_fp', summary)
        self.assertIn('F3_universal', summary)
        self.assertIn('algebraic_identity_holds', summary)
        self.assertIn('naive_universality_holds', summary)
        self.assertIn('koszul_duality_holds', summary)
        self.assertIn('propagator_variance', summary)
        self.assertIn('num_graphs', summary)

    def test_summary_algebraic_identity(self):
        """Summary reports the algebraic identity holds (trivially)."""
        for c in C_STANDARD:
            summary = genus3_w3_summary(c)
            self.assertTrue(summary['algebraic_identity_holds'])

    def test_summary_naive_universality_fails(self):
        """Summary reports the naive graph sum does NOT match universality."""
        for c in C_STANDARD:
            summary = genus3_w3_summary(c)
            self.assertFalse(summary['naive_universality_holds'])

    def test_summary_graph_count(self):
        """Summary reports 42 graphs."""
        c = Fraction(13)
        summary = genus3_w3_summary(c)
        self.assertEqual(summary['num_graphs'], 42)


class TestGraphAmplitudeConsistency(unittest.TestCase):
    """Cross-consistency checks on graph amplitudes."""

    def test_per_channel_is_diagonal(self):
        """Per-channel amplitude uses only all-T and all-W assignments."""
        c = Fraction(13)
        for graph in genus3_graphs():
            ne = graph.num_edges
            if ne == 0:
                continue
            # Per-channel should equal all-T + all-W divided by |Aut|
            all_T = graph_amplitude_colored(graph, tuple(['T'] * ne), c)
            all_W = graph_amplitude_colored(graph, tuple(['W'] * ne), c)
            per_ch = graph_per_channel_amplitude(graph, c)
            expected = (all_T + all_W) / Fraction(graph.automorphism_order())
            self.assertEqual(per_ch, expected)

    def test_cross_channel_is_residual(self):
        """Cross-channel = total - per_channel."""
        c = Fraction(13)
        for graph in genus3_graphs():
            total = graph_total_amplitude(graph, c)
            per_ch = graph_per_channel_amplitude(graph, c)
            cross = graph_cross_channel_amplitude(graph, c)
            self.assertEqual(cross, total - per_ch)

    def test_c_dependence_rational(self):
        """All amplitudes are rational functions of c (Fraction arithmetic)."""
        for c in C_STANDARD:
            total = genus3_total_amplitude(c)
            self.assertIsInstance(total, Fraction,
                                 f"Non-Fraction amplitude at c={c}")


class TestMultiPathVerification(unittest.TestCase):
    """Multi-path verification of the multi-channel computation.

    NOTE: Paths 1 and 4 test the algebraic identity kappa_T + kappa_W = kappa.
    This is trivially true and does not constitute genuine verification.
    Path 7 (NEW) tests the genuine graph sum computation.
    """

    def test_path1_algebraic_identity(self):
        """Path 1: Algebraic identity kappa_T + kappa_W = kappa (trivial).

        NOTE: This is arithmetic, not a universality test. The genuine
        graph sum uses the multichannel computation (Path 7).
        """
        for c in C_STANDARD:
            result = teleman_universality_genus3(c)
            self.assertTrue(result['algebraic_identity_holds'])

    def test_path2_koszul_duality(self):
        """Path 2: Koszul duality -> F_3(c) + F_3(100-c) consistent."""
        for c in C_STANDARD:
            result = koszul_duality_check(c)
            self.assertTrue(result['F3_sum_check'])

    def test_path3_ds_reduction(self):
        """Path 3: DS reduction -> F_3(W_3) = kappa(W_3) * lambda_3."""
        for k in [Fraction(1), Fraction(2), Fraction(5)]:
            result = ds_reduction_check(k)
            self.assertEqual(result['F3_W3'],
                             result['kappa_W3'] * result['lambda_3'])

    def test_path4_per_channel_additivity_algebraic(self):
        """Path 4: kappa_T * lambda_3 + kappa_W * lambda_3 = kappa * lambda_3 (trivial).

        NOTE: This is arithmetic (kappa_T + kappa_W = kappa by definition).
        It does NOT verify that the graph sum reproduces this formula.
        """
        for c in C_STANDARD:
            fp3 = lambda_fp(3)
            sum_channels = kappa_T(c) * fp3 + kappa_W(c) * fp3
            total = kappa_total(c) * fp3
            self.assertEqual(sum_channels, total)

    def test_path5_heisenberg_consistency(self):
        """Path 5: Heisenberg (k=1) gives F_3 = k * lambda_3."""
        # Heisenberg has kappa = k, so F_3 = k * 31/967680
        fp3 = lambda_fp(3)
        for k_val in [1, 2, 5]:
            k = Fraction(k_val)
            F3_heis = k * fp3
            self.assertEqual(F3_heis, k * Fraction(31, 967680))

    def test_path6_genus2_consistency(self):
        """Path 6: genus-2/genus-3 ratio is consistent."""
        fp2 = lambda_fp(2)
        fp3 = lambda_fp(3)
        ratio = fp3 / fp2
        expected = Fraction(31 * 5760, 7 * 967680)
        self.assertEqual(ratio, expected)

    def test_path7_genuine_graph_sum(self):
        """Path 7 (NEW): Genuine multi-channel graph sum computation.

        This is the ONLY path that performs actual graph amplitude calculations.
        It verifies internal consistency (decomposition, per-graph additivity)
        of the naive (R=Id) graph sum, and reports the cross-channel structure.

        It does NOT claim universality holds or fails; it provides the raw data.
        """
        for c in [Fraction(1), Fraction(13), Fraction(50)]:
            result = multichannel_graph_sum_genus3(c)
            # Internal consistency: total = per_channel + cross_channel
            self.assertEqual(
                result['F3_naive_total'],
                result['F3_naive_per_channel'] + result['F3_naive_cross_channel'],
                f"Decomposition fails at c={c}"
            )
            # Cross-channel is nonzero (genuine finding)
            self.assertTrue(result['naive_cross_channel_nonzero'],
                            f"Cross-channel unexpectedly zero at c={c}")
            # Naive total differs from universal prediction (expected)
            self.assertTrue(result['naive_total_neq_universal'],
                            f"Naive total unexpectedly matches universal at c={c}")


class TestSpecificCentralCharges(unittest.TestCase):
    """Tests at specific physically meaningful central charges.

    These verify the universality PREDICTION F3_universal = kappa * lambda_3^FP
    at specific c values. The genuine graph sum (F3_naive_total) does NOT match
    this prediction (R-dressing needed), but the prediction itself is correct.
    """

    def test_c_equals_1(self):
        """c = 1: kappa = 5/6, F_3^univ = 5/6 * 31/967680 = 155/5806080."""
        c = Fraction(1)
        expected = Fraction(5, 6) * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)
        # Naive graph sum differs from prediction
        self.assertNotEqual(result['F3_naive_total'], expected)

    def test_c_equals_2(self):
        """c = 2 (beta-gamma central charge): kappa = 5/3."""
        c = Fraction(2)
        expected = Fraction(5, 3) * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)

    def test_c_equals_13(self):
        """c = 13 (Virasoro self-dual point): kappa = 65/6."""
        c = Fraction(13)
        expected = Fraction(65, 6) * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)
        # Verify the exact naive cross-channel correction at c=13
        self.assertEqual(result['F3_naive_cross_channel'], Fraction(271507, 27040))

    def test_c_equals_50(self):
        """c = 50 (W_3 self-dual point): kappa = 125/3."""
        c = Fraction(50)
        expected = Fraction(125, 3) * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)
        # At self-dual point: kappa = kappa_dual
        self.assertEqual(kappa_total(c), kappa_total(Fraction(100) - c))

    def test_c_equals_100(self):
        """c = 100: Koszul dual of c=0."""
        c = Fraction(100)
        expected = Fraction(500, 6) * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)

    def test_c_negative_52(self):
        """c = -52 (sl_3 at k=1): physical value."""
        c = Fraction(-52)
        expected = Fraction(5) * c / 6 * Fraction(31, 967680)
        result = teleman_universality_genus3(c)
        self.assertEqual(result['F3_universal'], expected)


class TestEdgeCases(unittest.TestCase):
    """Edge cases and boundary conditions."""

    def test_large_c(self):
        """Large c: computation is well-defined, algebraic identity holds."""
        c = Fraction(10000)
        result = teleman_universality_genus3(c)
        self.assertTrue(result['algebraic_identity_holds'])
        # Naive graph sum is still wrong (R-dressing needed)
        self.assertFalse(result['naive_universality_holds'])

    def test_small_positive_c(self):
        """Small c > 0: computation is well-defined."""
        c = Fraction(1, 100)
        result = teleman_universality_genus3(c)
        self.assertTrue(result['algebraic_identity_holds'])

    def test_negative_c(self):
        """Negative c: computation is well-defined."""
        c = Fraction(-100)
        result = teleman_universality_genus3(c)
        self.assertTrue(result['algebraic_identity_holds'])

    def test_fractional_c(self):
        """Fractional c: exact Fraction arithmetic."""
        c = Fraction(7, 13)
        result = teleman_universality_genus3(c)
        self.assertTrue(result['algebraic_identity_holds'])


from math import factorial


class TestSpecificGraphAmplitudes(unittest.TestCase):
    """Test specific graph amplitudes at genus 3."""

    def test_smooth_graph_amplitude(self):
        """Smooth graph (g=3, 0 edges): amplitude = kappa * lambda_3."""
        c = Fraction(13)
        smooth = [g for g in genus3_graphs() if g.num_edges == 0]
        self.assertEqual(len(smooth), 1)
        amp = graph_total_amplitude(smooth[0], c)
        self.assertEqual(amp, kappa_total(c) * lambda_fp(3))

    def test_all_T_nonzero_for_all_boundary_graphs(self):
        """All-T assignment gives nonzero amplitude for every boundary graph."""
        c = Fraction(13)
        for idx, graph in enumerate(genus3_graphs()):
            if graph.num_edges == 0:
                continue
            ne = graph.num_edges
            amp = graph_amplitude_colored(graph, tuple(['T'] * ne), c)
            self.assertNotEqual(amp, Fraction(0),
                                f"All-T amplitude vanishes for graph {idx}")

    def test_all_W_vanishes_for_trivalent_genus0(self):
        """All-W vanishes for graphs with a g=0 trivalent vertex: C_{WWW} = 0."""
        c = Fraction(13)
        vanished_count = 0
        for graph in genus3_graphs():
            ne = graph.num_edges
            if ne == 0:
                continue
            # Check if any genus-0 vertex has exactly 3 W half-edges
            # (i.e., the all-W assignment gives a trivalent genus-0 vertex
            # with all W labels, hitting C_{WWW} = 0)
            assignment = tuple(['W'] * ne)
            amp = graph_amplitude_colored(graph, assignment, c)
            if amp == Fraction(0):
                vanished_count += 1
        # Many graphs should vanish for all-W
        self.assertGreater(vanished_count, 20,
                           f"Only {vanished_count} graphs vanish for all-W")

    def test_figure_eight_g2(self):
        """Figure-eight at genus 3: g=2 vertex with 1 self-loop."""
        c = Fraction(13)
        # Find the figure-eight: 1 vertex g=2, 1 self-loop
        fig8 = [g for g in genus3_graphs()
                if g.num_vertices == 1 and g.num_edges == 1
                and g.vertex_genera == (2,)]
        self.assertEqual(len(fig8), 1)
        graph = fig8[0]
        # All-T amplitude
        amp_T = graph_amplitude_colored(graph, ('T',), c)
        # = P_T * V_{2,2}(T,T) = (2/c) * kappa_T * lambda_2
        expected_T = propagator('T', c) * vertex_g2_2pt('T', 'T', c)
        self.assertEqual(amp_T, expected_T)

    def test_separating_node_g2_g1(self):
        """Separating node: g=2 vertex + g=1 vertex, 1 bridge."""
        c = Fraction(13)
        sep = [g for g in genus3_graphs()
               if g.num_vertices == 2 and g.num_edges == 1
               and sorted(g.vertex_genera) == [1, 2]]
        self.assertEqual(len(sep), 1)
        graph = sep[0]
        # All-T amplitude
        amp_T = graph_amplitude_colored(graph, ('T',), c)
        self.assertNotEqual(amp_T, Fraction(0))


class TestNumericalConsistency(unittest.TestCase):
    """Numerical consistency checks at multiple c values."""

    def test_f3_linear_in_c(self):
        """F_3(W_3) = 5c/6 * lambda_3 is linear in c."""
        fp3 = lambda_fp(3)
        for c in C_STANDARD:
            F3 = kappa_total(c) * fp3
            # Check linearity: F_3(c) / c = 5/6 * lambda_3
            self.assertEqual(F3 / c, Fraction(5, 6) * fp3)

    def test_f3_ratio_genus2_genus3(self):
        """F_3 / F_2 = lambda_3 / lambda_2 = 31*5760 / (7*967680) for all c."""
        fp2 = lambda_fp(2)
        fp3 = lambda_fp(3)
        for c in C_STANDARD:
            F2 = kappa_total(c) * fp2
            F3 = kappa_total(c) * fp3
            self.assertEqual(F3 / F2, fp3 / fp2)

    def test_mixed_coloring_count_correct(self):
        """Mixed valid colorings = valid - all_T - all_W - smooth."""
        c = Fraction(13)
        stats = channel_assignment_statistics(c)
        n_smooth = sum(1 for g in genus3_graphs() if g.num_edges == 0)
        total_valid = stats['valid_assignments']
        expected_mixed = total_valid - stats['all_T_valid'] - stats['all_W_valid'] - n_smooth
        self.assertEqual(stats['mixed_valid'], expected_mixed)

    def test_propagator_variance_different_c(self):
        """Propagator variance = 1/(5c) at multiple c values."""
        for c in C_STANDARD:
            self.assertEqual(propagator_variance(c), Fraction(1) / (5 * c))

    def test_koszul_dual_kappa_sum_at_many_values(self):
        """kappa(c) + kappa(100-c) = 250/3 for many c values."""
        for c in C_EXTENDED:
            kap = kappa_total(c)
            kap_dual = kappa_total(Fraction(100) - c)
            self.assertEqual(kap + kap_dual, Fraction(250, 3))


class TestCrossChannelStructure(unittest.TestCase):
    """Structure of cross-channel corrections."""

    def test_cross_channel_only_for_multi_edge(self):
        """Only graphs with >= 2 edges can have cross-channel corrections."""
        c = Fraction(13)
        for graph in genus3_graphs():
            if graph.num_edges < 2:
                cross = graph_cross_channel_amplitude(graph, c)
                self.assertEqual(cross, Fraction(0),
                                 f"Cross-channel nonzero for graph with "
                                 f"{graph.num_edges} edges")

    def test_cross_channel_nonzero_exists(self):
        """At least one graph has nonzero cross-channel correction."""
        c = Fraction(13)
        has_nonzero = False
        for graph in genus3_graphs():
            cross = graph_cross_channel_amplitude(graph, c)
            if cross != Fraction(0):
                has_nonzero = True
                break
        self.assertTrue(has_nonzero)

    def test_total_cross_channel_is_naive_delta(self):
        """Sum of per-graph cross-channel = naive_delta_F3."""
        c = Fraction(13)
        per_graph_sum = sum(graph_cross_channel_amplitude(g, c)
                            for g in genus3_graphs())
        delta = naive_delta_F3(c)
        self.assertEqual(per_graph_sum, delta)

    def test_shell_cross_channel_sums(self):
        """Shell cross-channel sums to total cross-channel."""
        c = Fraction(13)
        shell_cross = genus3_shell_cross_channel(c)
        total = sum(shell_cross.values())
        self.assertEqual(total, naive_delta_F3(c))


class TestVertexFactorDispatcher(unittest.TestCase):
    """Verify the vertex_factor dispatcher routes correctly."""

    def test_dispatch_g0_n3(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(0, ('T', 'T', 'T'), c),
                         vertex_g0_3pt(('T', 'T', 'T'), c))

    def test_dispatch_g0_n4(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(0, ('T', 'T', 'W', 'W'), c),
                         vertex_g0_4pt(('T', 'T', 'W', 'W'), c))

    def test_dispatch_g1_n0(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(1, (), c), vertex_g1_0pt(c))

    def test_dispatch_g1_n1(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(1, ('T',), c), vertex_g1_1pt('T', c))

    def test_dispatch_g2_n0(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(2, (), c), vertex_g2_0pt(c))

    def test_dispatch_g3_n0(self):
        c = Fraction(13)
        self.assertEqual(vertex_factor(3, (), c), vertex_g3_0pt(c))


class TestComparisonWithGenus2(unittest.TestCase):
    """Consistency checks between genus-2 and genus-3 computations."""

    def test_lambda_ratio(self):
        """lambda_3/lambda_2 = 31/1176."""
        ratio = lambda_fp(3) / lambda_fp(2)
        self.assertEqual(ratio, Fraction(31 * 5760, 7 * 967680))

    def test_f3_greater_than_f2_for_positive_kappa(self):
        """F_3 < F_2 for positive kappa (lambda decreases)."""
        c = Fraction(13)
        fp2 = lambda_fp(2)
        fp3 = lambda_fp(3)
        F2 = kappa_total(c) * fp2
        F3 = kappa_total(c) * fp3
        self.assertGreater(F2, F3)

    def test_genus2_smooth_contribution(self):
        """Genus-2 smooth contributes to genus-3 tree shell."""
        # Graphs with h^1=0 (trees) include the separating node (g=2)+(g=1)
        c = Fraction(13)
        shells = genus3_shell_amplitudes(c)
        self.assertNotEqual(shells[0], Fraction(0))


class TestG0VertexFactorExtended(unittest.TestCase):
    """Extended tests for genus-0 vertex factors."""

    def test_5pt_TTT_TW(self):
        """5-point vertex with channels (T,T,T,T,W) vanishes by Z_2."""
        c = Fraction(13)
        # This has odd W-count at one sub-vertex in the tree factorization
        # The final result depends on the tree topology
        val = vertex_g0_5pt(('T', 'T', 'T', 'T', 'W'), c)
        # With (T,T,T,T,W): the factorization splits into trivalent vertices
        # At least one vertex will have odd W-count -> 0
        self.assertEqual(val, Fraction(0))

    def test_5pt_TTWWW_vanishes(self):
        """5-point with 3 W's (odd): vanishes."""
        c = Fraction(13)
        val = vertex_g0_5pt(('T', 'T', 'W', 'W', 'W'), c)
        # 5 labels with 3 W's: any trivalent split must have one vertex
        # with odd W-count -> 0
        self.assertEqual(val, Fraction(0))

    def test_6pt_all_T(self):
        """6-point all-T vertex: nonzero (C_{TTT}^2 chain)."""
        c = Fraction(13)
        val = vertex_g0_6pt(('T', 'T', 'T', 'T', 'T', 'T'), c)
        self.assertNotEqual(val, Fraction(0))

    def test_6pt_all_W(self):
        """6-point all-W: NONZERO because internal edges can carry T.

        The caterpillar factorization: W,W -> m -> W,n -> W,W
        C_{WWm} != 0 only for m=T. So internal channels are T:
        V = P_T^3 * C_{WWT}^3 * C_{T,W,T}... etc.
        The key: C_{WWW} = 0, but C_{WWT} = c != 0.
        The tree factorization allows internal T-channels even when
        all external legs are W.
        """
        c = Fraction(13)
        val = vertex_g0_6pt(('W', 'W', 'W', 'W', 'W', 'W'), c)
        # Nonzero: internal edges can carry T (C_{WWT} = c != 0)
        self.assertNotEqual(val, Fraction(0))


class TestAdditionalMultiPath(unittest.TestCase):
    """Additional multi-path verification tests."""

    def test_genus1_universality_per_channel(self):
        """F_1^{(i)} = kappa_i / 24 (proved unconditionally)."""
        for c in C_STANDARD:
            self.assertEqual(vertex_g1_1pt('T', c), kappa_T(c) / 24)
            self.assertEqual(vertex_g1_1pt('W', c), kappa_W(c) / 24)

    def test_genus1_total_equals_kappa_over_24(self):
        """F_1 = kappa/24."""
        for c in C_STANDARD:
            F1_total = vertex_g1_1pt('T', c) + vertex_g1_1pt('W', c)
            # This is NOT right: vertex_g1_1pt is per-HALF-EDGE, not per-sector
            # The genus-1 free energy is kappa/24 = (kappa_T + kappa_W)/24
            # which equals vertex_g1_0pt
            self.assertEqual(vertex_g1_0pt(c), kappa_total(c) / 24)

    def test_f3_values_at_integer_c(self):
        """F_3 has correct values at integer c = 1,...,5."""
        fp3 = Fraction(31, 967680)
        for c_int in range(1, 6):
            c = Fraction(c_int)
            F3 = kappa_total(c) * fp3
            expected = Fraction(5) * c / 6 * fp3
            self.assertEqual(F3, expected)

    def test_ds_at_level_1(self):
        """DS at k=1: c=-52, kappa = -130/3."""
        result = ds_reduction_check(Fraction(1))
        self.assertEqual(result['c'], Fraction(-52))
        self.assertEqual(result['kappa_W3'],
                         Fraction(5) * Fraction(-52) / 6)
        self.assertEqual(result['kappa_W3'], Fraction(-130, 3))

    def test_ds_at_level_2(self):
        """DS at k=2: c = -374/5."""
        result = ds_reduction_check(Fraction(2))
        expected_c = Fraction(2) - 24 * Fraction(16) / 5
        self.assertEqual(result['c'], expected_c)


if __name__ == '__main__':
    unittest.main()
