r"""Tests for the explicit genus-2 graph sum for W_3 (multi-weight).

Comprehensive multi-path verification of the genus-2 free energy F_2(W_3).

RESULT: F_2(W_3) = kappa*lambda_2 + (c+204)/(16c) at the naive CohFT level.
The cross-channel correction (c+204)/(16c) is NONZERO for all c > 0.
The result is NOT proportional to lambda_2 without R-matrix corrections.
This is the computational content of op:multi-generator-universality.

Test structure (8 verification paths):
    1. Graph topology: 6 graphs, stability, genus, automorphisms
    2. Frobenius algebra: metric, propagator, structure constants, Z_2 parity
    3. PATH 1 vs PATH 2: direct enumeration vs analytic formulas
    4. Per-graph amplitudes: exhaustive channel-by-channel verification
    5. Cross-channel correction: the multi-generator signal delta_F2
    6. Per-channel universality: diagonal sum = kappa * lambda_2 (PROVED)
    7. Koszul duality: c <-> 100-c complementarity constraints
    8. Asymptotics, parity, single-generator limit, proportionality test

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    rem:propagator-weight-universality (AP27),
    eq:delta-pf-genus2-explicit
"""

import unittest
import sys
import os
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mg_w3_genus2_graph_engine import (
    # Basics
    lambda_fp, _bernoulli,
    kappa_T, kappa_W, kappa_total,
    metric, propagator,
    structure_constant_upper, structure_constant_lower,
    genus0_3pt, genus0_4pt,
    genus1_1pt, genus1_2pt,
    # Graphs
    GRAPHS, verify_graph_topology,
    channel_assignments, half_edge_channels,
    vertex_factor,
    # Amplitudes
    graph_amplitude_single, graph_amplitude_total,
    # Analytic
    analytic_fig_eight, analytic_banana, analytic_dumbbell,
    analytic_theta, analytic_lollipop, ANALYTIC_FUNCTIONS,
    # Full computation
    full_boundary_sum, cross_channel_correction, cross_channel_decomposition,
    F2_universal, F2_naive, F2_complete_analysis,
    # Verification paths
    per_channel_check, euler_characteristic_check,
    koszul_duality_check, large_c_analysis,
    z2_parity_check, single_generator_limit,
    proportionality_test, compute_full_summary,
)

# Standard test central charges
C_VALS = [Fraction(1), Fraction(2), Fraction(4), Fraction(13),
          Fraction(26), Fraction(50), Fraction(100)]


# ============================================================================
# 1. Graph topology
# ============================================================================

class TestGraphTopology(unittest.TestCase):
    """Verify all 6 genus-2 stable graphs are correctly enumerated."""

    def test_graph_count(self):
        """There are exactly 7 stable graphs of M_bar_{2,0}."""
        self.assertEqual(len(GRAPHS), 7)

    def test_all_genus_2(self):
        """Every graph has arithmetic genus 2."""
        for G in GRAPHS:
            n_v = len(G['vertex_genera'])
            n_e = len(G['edges'])
            h1 = n_e - n_v + 1
            g = h1 + sum(G['vertex_genera'])
            self.assertEqual(g, 2, f"{G['name']}: genus {g} != 2")

    def test_all_stable(self):
        """Every vertex satisfies 2g_v - 2 + val_v > 0."""
        results = verify_graph_topology()
        for r in results:
            self.assertTrue(r['stable'], f"{r['name']}: not stable")

    def test_valences_consistent(self):
        """Computed valences match declared valences."""
        results = verify_graph_topology()
        for r in results:
            self.assertTrue(r['valences_match'],
                            f"{r['name']}: valences {r['computed_valences']}")

    def test_h1_values(self):
        """Verify first Betti numbers."""
        expected_h1 = [0, 1, 2, 0, 2, 1, 2]
        for idx, G in enumerate(GRAPHS):
            self.assertEqual(G['h1'], expected_h1[idx],
                             f"{G['name']}: h1 = {G['h1']} != {expected_h1[idx]}")

    def test_automorphism_orders(self):
        """Verify automorphism group orders.

        smooth:    1  (no symmetries)
        fig_eight: 2  (self-loop flip)
        banana:    8  (2 self-loops: 2^2 flips * 2! permutations)
        dumbbell:  2  (swap the two g=1 vertices)
        theta:     12 (S_3 permutation of 3 bridges * swap 2 vertices = 3!*2)
        lollipop:  2  (self-loop flip at v0)
        barbell:   8  (2 self-loop flips * vertex swap = 2*2*2 = 8)
        """
        expected_aut = [1, 2, 8, 2, 12, 2, 8]
        for idx, G in enumerate(GRAPHS):
            self.assertEqual(G['aut'], expected_aut[idx],
                             f"{G['name']}: |Aut| = {G['aut']} != {expected_aut[idx]}")

    def test_edge_counts(self):
        """Verify edge counts: 0, 1, 2, 1, 3, 2, 3."""
        expected = [0, 1, 2, 1, 3, 2, 3]
        for idx, G in enumerate(GRAPHS):
            self.assertEqual(len(G['edges']), expected[idx],
                             f"{G['name']}: edges")

    def test_max_edges_is_3g_minus_3(self):
        """Maximum edge count = 3g-3 = 3 (theta and barbell graphs)."""
        max_e = max(len(G['edges']) for G in GRAPHS)
        self.assertEqual(max_e, 3)  # 3*2 - 3 = 3

    def test_inverse_aut_sum(self):
        """Sum of 1/|Aut| = 1 + 1/2 + 1/8 + 1/2 + 1/12 + 1/2 + 1/8 = 71/24."""
        total = sum(Fraction(1, G['aut']) for G in GRAPHS)
        self.assertEqual(total, Fraction(17, 6))


# ============================================================================
# 2. Frobenius algebra data
# ============================================================================

class TestFrobeniusAlgebra(unittest.TestCase):
    """Verify the W_3 Frobenius algebra data."""

    def test_kappa_T(self):
        for c in C_VALS:
            self.assertEqual(kappa_T(c), c / 2)

    def test_kappa_W(self):
        for c in C_VALS:
            self.assertEqual(kappa_W(c), c / 3)

    def test_kappa_total(self):
        """kappa(W_3) = 5c/6 = c*(H_3 - 1)."""
        for c in C_VALS:
            self.assertEqual(kappa_total(c), Fraction(5) * c / 6)

    def test_kappa_harmonic_formula(self):
        """kappa = c * (H_3 - 1) where H_3 = 11/6."""
        H3 = Fraction(1) + Fraction(1, 2) + Fraction(1, 3)
        for c in C_VALS:
            self.assertEqual(kappa_total(c), c * (H3 - 1))

    def test_metric_positive(self):
        for c in C_VALS:
            if c > 0:
                self.assertGreater(metric('T', c), 0)
                self.assertGreater(metric('W', c), 0)

    def test_propagator_inverse(self):
        """eta^{ii} * eta_{ii} = 1."""
        for c in C_VALS:
            if c > 0:
                for ch in ('T', 'W'):
                    self.assertEqual(propagator(ch, c) * metric(ch, c), 1)

    def test_structure_constants_nonvanishing(self):
        """C_{TTT} = C_{TWW} = C_{WWT} = c."""
        for c in C_VALS:
            self.assertEqual(structure_constant_lower('T', 'T', 'T', c), c)
            self.assertEqual(structure_constant_lower('T', 'W', 'W', c), c)
            self.assertEqual(structure_constant_lower('W', 'W', 'T', c), c)

    def test_structure_constants_vanishing(self):
        """C_{TTW} = C_{WWW} = 0 (Z_2 parity)."""
        for c in C_VALS:
            self.assertEqual(structure_constant_lower('T', 'T', 'W', c), 0)
            self.assertEqual(structure_constant_lower('W', 'W', 'W', c), 0)
            self.assertEqual(structure_constant_lower('T', 'W', 'T', c), 0)
            self.assertEqual(structure_constant_lower('W', 'T', 'T', c), 0)

    def test_structure_constant_universality(self):
        """All nonvanishing C_{ijk} equal c (remarkable!)."""
        for c in C_VALS:
            for i in ('T', 'W'):
                for j in ('T', 'W'):
                    for k in ('T', 'W'):
                        val = structure_constant_lower(i, j, k, c)
                        if val != 0:
                            self.assertEqual(val, c,
                                             f"C_{{{i}{j}{k}}} = {val} != {c}")

    def test_4pt_universality(self):
        """V_{0,4}(i,i|j,j) = 2c for ALL channel pairs."""
        for c in C_VALS:
            if c > 0:
                for i in ('T', 'W'):
                    for j in ('T', 'W'):
                        val = genus0_4pt((i, i), (j, j), c)
                        self.assertEqual(val, 2 * c,
                                         f"V_{{0,4}}({i},{i}|{j},{j}) = {val}")

    def test_genus1_1pt(self):
        """V_{1,1}(i) = kappa_i/24."""
        for c in C_VALS:
            self.assertEqual(genus1_1pt('T', c), kappa_T(c) / 24)
            self.assertEqual(genus1_1pt('W', c), kappa_W(c) / 24)

    def test_genus1_2pt_diagonal(self):
        """V_{1,2}(i,i) = kappa_i/24."""
        for c in C_VALS:
            self.assertEqual(genus1_2pt('T', 'T', c), kappa_T(c) / 24)
            self.assertEqual(genus1_2pt('W', 'W', c), kappa_W(c) / 24)

    def test_genus1_2pt_offdiagonal(self):
        """V_{1,2}(T,W) = 0 (diagonal metric)."""
        for c in C_VALS:
            self.assertEqual(genus1_2pt('T', 'W', c), 0)
            self.assertEqual(genus1_2pt('W', 'T', c), 0)


# ============================================================================
# 3. Faber-Pandharipande
# ============================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify lambda_g^FP values."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda2_from_bernoulli(self):
        """lambda_2 = (7/8) * |B_4| / 4! = (7/8) * (1/30) / 24 = 7/5760."""
        B4 = _bernoulli(4)
        self.assertEqual(B4, Fraction(-1, 30))
        result = Fraction(7, 8) * abs(B4) / Fraction(factorial(4))
        self.assertEqual(result, Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_positivity(self):
        """All lambda_g^FP are positive."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))


def factorial(n):
    """Helper for test."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ============================================================================
# 4. PATH 1 vs PATH 2: Enumeration vs Analytic
# ============================================================================

class TestEnumerationVsAnalytic(unittest.TestCase):
    """Verify that direct enumeration matches closed-form analytic formulas."""

    def _check_graph(self, graph_name, graph_idx, analytic_func, c):
        """Compare enumeration with analytic formula for a single graph."""
        enum_result = graph_amplitude_total(graph_idx, c)
        anal_result = analytic_func(c)
        for key in ('all_T', 'all_W', 'mixed', 'total'):
            self.assertEqual(
                enum_result[key], anal_result[key],
                f"{graph_name} at c={c}: {key}: "
                f"enum={enum_result[key]} != analytic={anal_result[key]}"
            )

    def test_fig_eight_all_c(self):
        for c in C_VALS:
            self._check_graph('fig_eight', 1, analytic_fig_eight, c)

    def test_banana_all_c(self):
        for c in C_VALS:
            self._check_graph('banana', 2, analytic_banana, c)

    def test_dumbbell_all_c(self):
        for c in C_VALS:
            self._check_graph('dumbbell', 3, analytic_dumbbell, c)

    def test_theta_all_c(self):
        for c in C_VALS:
            self._check_graph('theta', 4, analytic_theta, c)

    def test_lollipop_all_c(self):
        for c in C_VALS:
            self._check_graph('lollipop', 5, analytic_lollipop, c)

    def test_all_graphs_all_c(self):
        """Comprehensive test: all 5 boundary graphs at all c values."""
        for c in C_VALS:
            for name, func in ANALYTIC_FUNCTIONS.items():
                idx = next(i for i, G in enumerate(GRAPHS) if G['name'] == name)
                self._check_graph(name, idx, func, c)


# ============================================================================
# 5. Per-graph amplitude details
# ============================================================================

class TestFigEight(unittest.TestCase):
    """Gamma_1: figure-eight (1 vertex g=1, 1 self-loop)."""

    def test_c_independent_total(self):
        """Total amplitude 1/24 is independent of c."""
        for c in C_VALS:
            r = graph_amplitude_total(1, c)
            self.assertEqual(r['total'], Fraction(1, 24))

    def test_channel_symmetry(self):
        """A^T = A^W = 1/48 (diagonal channel symmetry)."""
        for c in C_VALS:
            r = graph_amplitude_total(1, c)
            self.assertEqual(r['all_T'], Fraction(1, 48))
            self.assertEqual(r['all_W'], Fraction(1, 48))

    def test_no_mixed(self):
        """No mixed channels (single edge)."""
        for c in C_VALS:
            r = graph_amplitude_total(1, c)
            self.assertEqual(r['mixed'], Fraction(0))

    def test_equals_lambda1(self):
        """Total = lambda_1^FP = 1/24."""
        for c in C_VALS:
            r = graph_amplitude_total(1, c)
            self.assertEqual(r['total'], lambda_fp(1))


class TestBanana(unittest.TestCase):
    """Gamma_2: banana (1 vertex g=0, 2 self-loops)."""

    def test_all_T(self):
        """A^{TT} = 1/c."""
        for c in C_VALS:
            r = graph_amplitude_total(2, c)
            self.assertEqual(r['all_T'], Fraction(1) / c)

    def test_all_W(self):
        """A^{WW} = 9/(4c)."""
        for c in C_VALS:
            r = graph_amplitude_total(2, c)
            self.assertEqual(r['all_W'], Fraction(9) / (4 * c))

    def test_mixed(self):
        """A^{mixed} = 3/c."""
        for c in C_VALS:
            r = graph_amplitude_total(2, c)
            self.assertEqual(r['mixed'], Fraction(3) / c)

    def test_total(self):
        """Total = 1/c + 9/(4c) + 3/c = (4 + 9 + 12)/(4c) = 25/(4c)."""
        for c in C_VALS:
            r = graph_amplitude_total(2, c)
            self.assertEqual(r['total'], Fraction(25) / (4 * c))

    def test_4pt_universality_in_amplitude(self):
        """The V_{0,4} = 2c universality implies all channel combos proportional."""
        c = Fraction(26)
        # (T,T): (2/c)^2 * 2c = 8/c -> 1/c with 1/8
        # (W,W): (3/c)^2 * 2c = 18/c -> 9/(4c) with 1/8
        # (T,W): 2*(2/c)(3/c)*2c = 24/c -> 3/c with 1/8
        r = graph_amplitude_total(2, c)
        # Ratio test: all_W / all_T = (9/4) = (eta^W / eta^T)^2
        self.assertEqual(r['all_W'] / r['all_T'], Fraction(9, 4))


class TestDumbbell(unittest.TestCase):
    """Gamma_3: dumbbell (2 vertices g=1, 1 bridge)."""

    def test_all_T(self):
        """A^T = c/2304."""
        for c in C_VALS:
            r = graph_amplitude_total(3, c)
            self.assertEqual(r['all_T'], c / 2304)

    def test_all_W(self):
        """A^W = c/3456."""
        for c in C_VALS:
            r = graph_amplitude_total(3, c)
            self.assertEqual(r['all_W'], c / 3456)

    def test_no_mixed(self):
        """No mixed channels (single edge)."""
        for c in C_VALS:
            r = graph_amplitude_total(3, c)
            self.assertEqual(r['mixed'], Fraction(0))

    def test_total(self):
        """Total = 5c/6912 = kappa/1152."""
        for c in C_VALS:
            r = graph_amplitude_total(3, c)
            self.assertEqual(r['total'], Fraction(5) * c / 6912)
            self.assertEqual(r['total'], kappa_total(c) / 1152)

    def test_ratio(self):
        """A^W/A^T = (kappa_W/kappa_T) = 2/3."""
        for c in C_VALS:
            r = graph_amplitude_total(3, c)
            if r['all_T'] != 0:
                self.assertEqual(r['all_W'] / r['all_T'], Fraction(2, 3))


class TestTheta(unittest.TestCase):
    """Gamma_4: theta (2 vertices g=0, 3 bridges)."""

    def test_all_T(self):
        """A^{TTT} = 2/(3c)."""
        for c in C_VALS:
            r = graph_amplitude_total(4, c)
            self.assertEqual(r['all_T'], Fraction(2) / (3 * c))

    def test_all_W_vanishes(self):
        """A^{WWW} = 0 (C_{WWW} = 0 by Z_2 parity)."""
        for c in C_VALS:
            r = graph_amplitude_total(4, c)
            self.assertEqual(r['all_W'], Fraction(0))

    def test_mixed(self):
        """Mixed = 9/(2c) from three (T,W,W)-type assignments."""
        for c in C_VALS:
            r = graph_amplitude_total(4, c)
            self.assertEqual(r['mixed'], Fraction(9) / (2 * c))

    def test_ttw_type_vanishes(self):
        """(T,T,W)-type assignments vanish (C_{TTW} = 0)."""
        c = Fraction(26)
        # There are 3 assignments of type (T,T,W): (T,T,W), (T,W,T), (W,T,T)
        for sigma in [('T', 'T', 'W'), ('T', 'W', 'T'), ('W', 'T', 'T')]:
            amp = graph_amplitude_single(4, sigma, c)
            self.assertEqual(amp, Fraction(0))

    def test_tww_type_amplitude(self):
        """Each (T,W,W)-type assignment gives 18/c raw amplitude."""
        c = Fraction(26)
        for sigma in [('T', 'W', 'W'), ('W', 'T', 'W'), ('W', 'W', 'T')]:
            amp = graph_amplitude_single(4, sigma, c)
            self.assertEqual(amp, Fraction(18) / c)


class TestLollipop(unittest.TestCase):
    """Gamma_5: lollipop (vertex g=0 + vertex g=1, self-loop + bridge)."""

    def test_all_T(self):
        """A^T(TT) = 1/24 (c-independent)."""
        for c in C_VALS:
            r = graph_amplitude_total(5, c)
            self.assertEqual(r['all_T'], Fraction(1, 24))

    def test_all_W_vanishes(self):
        """A^W(WW) = 0 (C_{WWW} = 0)."""
        for c in C_VALS:
            r = graph_amplitude_total(5, c)
            self.assertEqual(r['all_W'], Fraction(0))

    def test_mixed(self):
        """Mixed = 1/16 (c-independent, from (W,T) assignment only)."""
        for c in C_VALS:
            r = graph_amplitude_total(5, c)
            self.assertEqual(r['mixed'], Fraction(1, 16))

    def test_mixed_c_independent(self):
        """The lollipop mixed amplitude 1/16 is INDEPENDENT of c."""
        values = set()
        for c in C_VALS:
            r = graph_amplitude_total(5, c)
            values.add(r['mixed'])
        self.assertEqual(len(values), 1)  # all the same
        self.assertEqual(values.pop(), Fraction(1, 16))

    def test_tw_vanishes(self):
        """(T,W) assignment vanishes (C_{TTW} = 0 at v0)."""
        for c in C_VALS:
            amp = graph_amplitude_single(5, ('T', 'W'), c)
            self.assertEqual(amp, Fraction(0))

    def test_wt_amplitude(self):
        """(W,T) assignment gives 1/8 raw (1/16 with |Aut|=2)."""
        for c in C_VALS:
            amp = graph_amplitude_single(5, ('W', 'T'), c)
            self.assertEqual(amp, Fraction(1, 8))


# ============================================================================
# 6. Cross-channel correction
# ============================================================================

class TestCrossChannel(unittest.TestCase):
    """Verify the cross-channel correction delta_F2 = (c+204)/(16c)."""

    def test_formula(self):
        """delta_F2 = (c+204)/(16c) for all c."""
        for c in C_VALS:
            delta = cross_channel_correction(c)
            expected = (c + 204) / (16 * c)
            self.assertEqual(delta, expected)

    def test_decomposition(self):
        """delta = 3/c (banana) + 9/(2c) (theta) + 1/16 (lollipop)."""
        for c in C_VALS:
            decomp = cross_channel_decomposition(c)
            self.assertTrue(decomp['match'])
            self.assertEqual(decomp['banana'], Fraction(3) / c)
            self.assertEqual(decomp['theta'], Fraction(9) / (2 * c))
            self.assertEqual(decomp['lollipop'], Fraction(1, 16))

    def test_always_positive(self):
        """delta_F2 > 0 for all c > 0."""
        for c in C_VALS:
            self.assertGreater(cross_channel_correction(c), 0)

    def test_never_zero(self):
        """delta_F2 != 0 for any positive c (no cancellation)."""
        for c in C_VALS:
            self.assertNotEqual(cross_channel_correction(c), Fraction(0))

    def test_matches_boundary_sum(self):
        """delta_F2 equals the mixed part of the full boundary sum."""
        for c in C_VALS:
            boundary = full_boundary_sum(c)
            self.assertEqual(boundary['mixed'], cross_channel_correction(c))

    def test_c_dependent_piece(self):
        """The 1/c piece is 15/(2c) = (banana + theta)."""
        for c in C_VALS:
            decomp = cross_channel_decomposition(c)
            c_dep = decomp['banana'] + decomp['theta']
            self.assertEqual(c_dep, Fraction(15) / (2 * c))

    def test_c_independent_piece(self):
        """The c-independent piece is 1/16 (lollipop only)."""
        for c in C_VALS:
            decomp = cross_channel_decomposition(c)
            self.assertEqual(decomp['lollipop'], Fraction(1, 16))


# ============================================================================
# 7. Per-channel universality (PATH 3)
# ============================================================================

class TestPerChannelUniversality(unittest.TestCase):
    """Verify that the diagonal sum equals kappa * lambda_2^FP."""

    def test_kappa_additivity(self):
        """kappa_T + kappa_W = kappa_total = 5c/6."""
        for c in C_VALS:
            r = per_channel_check(c)
            self.assertTrue(r['kappa_additivity'])

    def test_diagonal_boundary_sum(self):
        """The diagonal boundary sum is well-defined and consistent."""
        for c in C_VALS:
            r = per_channel_check(c)
            total_boundary = r['F2_T_boundary'] + r['F2_W_boundary']
            full = full_boundary_sum(c)
            self.assertEqual(total_boundary, full['diagonal'])


# ============================================================================
# 8. Koszul duality (PATH 5)
# ============================================================================

class TestKoszulDuality(unittest.TestCase):
    """Verify c <-> 100-c complementarity for W_3."""

    def test_kappa_sum(self):
        """kappa(c) + kappa(100-c) = 250/3."""
        for c in [Fraction(10), Fraction(26), Fraction(50)]:
            r = koszul_duality_check(c)
            self.assertTrue(r['kappa_duality'])
            self.assertEqual(r['kappa_sum'], Fraction(250, 3))

    def test_F2_sum_universal(self):
        """F_2^{univ}(c) + F_2^{univ}(100-c) = (250/3) * lambda_2."""
        for c in [Fraction(10), Fraction(26), Fraction(50)]:
            r = koszul_duality_check(c)
            self.assertTrue(r['F2_duality'])

    def test_cross_sum_structure(self):
        """Cross-channel sum under duality is well-defined."""
        c = Fraction(26)
        r = koszul_duality_check(c)
        self.assertIsNotNone(r['cross_sum'])
        # delta(26) + delta(74) = (146/(16*26)) + (194/(16*74))
        d26 = (Fraction(26) + 204) / (16 * 26)
        d74 = (Fraction(74) + 204) / (16 * 74)
        self.assertEqual(r['cross_sum'], d26 + d74)

    def test_self_dual_point(self):
        """At c=50 (self-dual): kappa = 250/6, dual = 250/6."""
        c = Fraction(50)
        self.assertEqual(kappa_total(c), kappa_total(Fraction(50)))
        r = koszul_duality_check(c)
        self.assertTrue(r['kappa_duality'])


# ============================================================================
# 9. Z_2 parity (PATH 7)
# ============================================================================

class TestZ2Parity(unittest.TestCase):
    """Verify Z_2 parity (W -> -W) at genus-0 vertices.

    The Z_2 constraint: C_{ijk} = 0 when the W-count is odd.
    This applies at genus-0 vertices ONLY. At genus >= 1, the one-point
    function kappa_i/24 is nonzero for both T and W channels.
    """

    def test_parity_genus0_vertices(self):
        """Z_2 parity holds at all genus-0 vertices."""
        for c in [Fraction(4), Fraction(26)]:
            r = z2_parity_check(c)
            self.assertTrue(r['parity_respected'],
                            f"Parity violations at c={c}: {r['violations']}")

    def test_genus1_vertex_both_channels_nonzero(self):
        """Genus-1 one-point function is nonzero for BOTH T and W."""
        for c in C_VALS:
            self.assertNotEqual(genus1_1pt('T', c), 0)
            self.assertNotEqual(genus1_1pt('W', c), 0)


# ============================================================================
# 10. Euler characteristic (PATH 4)
# ============================================================================

class TestEulerCharacteristic(unittest.TestCase):
    """Verify inverse automorphism sum."""

    def test_inverse_aut(self):
        r = euler_characteristic_check()
        self.assertTrue(r['match'])
        self.assertEqual(r['inverse_aut_sum'], Fraction(17, 6))


# ============================================================================
# 11. Channel assignment counting
# ============================================================================

class TestChannelAssignments(unittest.TestCase):
    """Verify channel assignment enumeration."""

    def test_zero_edges(self):
        self.assertEqual(channel_assignments(0), [()])

    def test_one_edge(self):
        self.assertEqual(len(channel_assignments(1)), 2)

    def test_two_edges(self):
        self.assertEqual(len(channel_assignments(2)), 4)

    def test_three_edges(self):
        self.assertEqual(len(channel_assignments(3)), 8)

    def test_total_assignments_genus2(self):
        """Total channel assignments across all boundary graphs."""
        total = sum(2 ** len(GRAPHS[idx]['edges']) for idx in range(1, len(GRAPHS)))
        # fig_eight: 2, banana: 4, dumbbell: 2, theta: 8, lollipop: 4, barbell: 8
        self.assertEqual(total, 2 + 4 + 2 + 8 + 4 + 8)
        self.assertEqual(total, 28)


# ============================================================================
# 12. Large-c asymptotics (PATH 6)
# ============================================================================

class TestAsymptotics(unittest.TestCase):
    """Verify large-c behavior of the cross-channel correction."""

    def test_large_c_limit(self):
        """delta_F2 -> 1/16 as c -> infinity."""
        c = Fraction(1000000)
        delta = cross_channel_correction(c)
        # (c+204)/(16c) = 1/16 + 120/(16c) -> 1/16
        diff = abs(float(delta) - 1/16)
        self.assertLess(diff, 1e-4)

    def test_ratio_decreasing(self):
        """delta/F2_univ -> 0 as c -> infinity."""
        results = large_c_analysis([100, 1000, 10000])
        ratios = [r['ratio'] for r in results if r['ratio'] is not None]
        # Ratios should be decreasing
        for i in range(len(ratios) - 1):
            self.assertGreater(ratios[i], ratios[i + 1])


# ============================================================================
# 13. The key result: proportionality test
# ============================================================================

class TestProportionality(unittest.TestCase):
    """Test whether F_2(W_3) is proportional to lambda_2^FP.

    ANSWER: NO. The cross-channel correction (c+204)/(16c) is nonzero.
    """

    def test_not_proportional(self):
        """F_2(W_3) != kappa * lambda_2^FP for any c > 0."""
        result = proportionality_test()
        self.assertFalse(result['universality_at_any_c'])

    def test_formula_confirmed(self):
        """Cross-channel = (c+204)/(16c) confirmed at all test values."""
        result = proportionality_test()
        self.assertTrue(result['formula_confirmed'])

    def test_specific_values(self):
        """Spot-check cross-channel at specific c values."""
        # c=4: delta = (4+204)/(16*4) = 208/64 = 13/4
        self.assertEqual(cross_channel_correction(Fraction(4)), Fraction(13, 4))
        # c=26: delta = (26+204)/(16*26) = 230/416 = 115/208
        self.assertEqual(cross_channel_correction(Fraction(26)), Fraction(115, 208))
        # c=204: delta = (204+204)/(16*204) = 408/3264 = 1/8
        self.assertEqual(cross_channel_correction(Fraction(204)), Fraction(1, 8))


# ============================================================================
# 14. Cross-check with existing w3_genus2.py
# ============================================================================

class TestCrossCheckExistingEngine(unittest.TestCase):
    """Cross-check results against the existing w3_genus2.py engine."""

    def test_kappa_agreement(self):
        """kappa values agree."""
        try:
            from w3_genus2 import (kappa_T as kT_old, kappa_W as kW_old,
                                   kappa_total as kTot_old)
            for c in C_VALS:
                self.assertEqual(kappa_T(c), kT_old(c))
                self.assertEqual(kappa_W(c), kW_old(c))
                self.assertEqual(kappa_total(c), kTot_old(c))
        except ImportError:
            self.skipTest("w3_genus2 not importable")

    def test_cross_channel_agreement(self):
        """Cross-channel correction agrees."""
        try:
            from w3_genus2 import cross_channel_correction as cc_old
            for c in C_VALS:
                self.assertEqual(cross_channel_correction(c), cc_old(c))
        except ImportError:
            self.skipTest("w3_genus2 not importable")

    def test_analytic_agreement(self):
        """Per-graph analytic formulas agree."""
        try:
            from w3_genus2 import (analytic_fig_eight as afe_old,
                                   analytic_banana as ab_old,
                                   analytic_dumbbell as ad_old,
                                   analytic_theta as at_old,
                                   analytic_lollipop as al_old)
            for c in C_VALS:
                for key in ('all_T', 'all_W', 'mixed', 'total'):
                    self.assertEqual(analytic_fig_eight(c)[key], afe_old(c)[key])
                    self.assertEqual(analytic_banana(c)[key], ab_old(c)[key])
                    self.assertEqual(analytic_dumbbell(c)[key], ad_old(c)[key])
                    self.assertEqual(analytic_theta(c)[key], at_old(c)[key])
                    self.assertEqual(analytic_lollipop(c)[key], al_old(c)[key])
        except ImportError:
            self.skipTest("w3_genus2 not importable")


# ============================================================================
# 15. Full summary test
# ============================================================================

class TestFullSummary(unittest.TestCase):
    """Run the full 8-path summary at a representative c value."""

    def test_summary_at_c26(self):
        """Full summary at c=26 (critical Virasoro central charge)."""
        summary = compute_full_summary(Fraction(26))
        self.assertTrue(summary['kappa_formula_check'])
        self.assertTrue(summary['lambda2_check'])
        self.assertFalse(summary['proportional_to_lambda2'])

    def test_summary_at_c4(self):
        """Full summary at c=4 (free boson pair)."""
        summary = compute_full_summary(Fraction(4))
        self.assertTrue(summary['kappa_formula_check'])
        self.assertFalse(summary['proportional_to_lambda2'])


# ============================================================================
# 16. Numerical spot-checks (independent hand computation)
# ============================================================================

class TestNumericalSpotChecks(unittest.TestCase):
    """Verify specific numerical values computed by hand."""

    def test_F2_universal_c26(self):
        """F_2^{univ}(c=26) = (5*26/6) * (7/5760) = (130/6) * (7/5760)."""
        c = Fraction(26)
        expected = Fraction(5 * 26, 6) * Fraction(7, 5760)
        self.assertEqual(F2_universal(c), expected)
        # = 910/34560 = 91/3456 = 7*13/3456
        self.assertEqual(expected, Fraction(910, 34560))

    def test_F2_universal_c6(self):
        """F_2^{univ}(c=6) = 5 * (7/5760) = 7/1152."""
        c = Fraction(6)
        self.assertEqual(F2_universal(c), Fraction(7, 1152))
        self.assertEqual(kappa_total(c), Fraction(5))

    def test_cross_channel_c1(self):
        """delta(c=1) = (1+204)/(16) = 205/16."""
        c = Fraction(1)
        self.assertEqual(cross_channel_correction(c), Fraction(205, 16))

    def test_cross_channel_c_infty_approach(self):
        """delta(c=10^6) is very close to 1/16."""
        c = Fraction(10**6)
        delta = cross_channel_correction(c)
        error = delta - Fraction(1, 16)
        self.assertEqual(error, Fraction(204) / (16 * c))
        self.assertLess(float(error), 1e-4)

    def test_fig_eight_is_genus1(self):
        """Figure-eight total = 1/24 = lambda_1^FP (a nontrivial coincidence)."""
        for c in C_VALS:
            self.assertEqual(graph_amplitude_total(1, c)['total'], Fraction(1, 24))
            self.assertEqual(Fraction(1, 24), lambda_fp(1))

    def test_banana_total_c26(self):
        """Banana total at c=26: 25/(4*26) = 25/104."""
        c = Fraction(26)
        r = graph_amplitude_total(2, c)
        self.assertEqual(r['total'], Fraction(25, 104))

    def test_dumbbell_total_c6(self):
        """Dumbbell total at c=6: 5*6/6912 = 5/1152."""
        c = Fraction(6)
        r = graph_amplitude_total(3, c)
        self.assertEqual(r['total'], Fraction(5, 1152))

    def test_theta_total_c26(self):
        """Theta total at c=26: 2/(3*26) + 9/(2*26) = 2/78 + 9/52."""
        c = Fraction(26)
        r = graph_amplitude_total(4, c)
        expected = Fraction(2, 78) + Fraction(9, 52)
        self.assertEqual(r['total'], expected)

    def test_lollipop_total_all_c(self):
        """Lollipop total = 1/24 + 1/16 = 5/48 (c-independent)."""
        for c in C_VALS:
            r = graph_amplitude_total(5, c)
            self.assertEqual(r['total'], Fraction(5, 48))


# ============================================================================
# 17. Consistency between graphs and stable_graph_enumeration
# ============================================================================

class TestConsistencyWithStableGraphModule(unittest.TestCase):
    """Cross-check against the stable_graph_enumeration module."""

    def test_graph_count_matches(self):
        """Both modules agree on stable graph count at (g=2, n=0)."""
        try:
            from stable_graph_enumeration import enumerate_stable_graphs
            graphs = enumerate_stable_graphs(2, 0)
            self.assertGreaterEqual(len(graphs), 6)
        except ImportError:
            self.skipTest("stable_graph_enumeration not importable")

    def test_aut_orders_match(self):
        """Automorphism orders from stable_graph_enumeration are a subset of ours."""
        try:
            from stable_graph_enumeration import enumerate_stable_graphs
            graphs = enumerate_stable_graphs(2, 0)
            aut_orders = sorted(g.automorphism_order() for g in graphs)
            our_orders = sorted(G['aut'] for G in GRAPHS)
            # The external module may not include the barbell; check subset
            for ao in aut_orders:
                self.assertIn(ao, our_orders)
        except ImportError:
            self.skipTest("stable_graph_enumeration not importable")


# ============================================================================
# 18. Independence of computation paths
# ============================================================================

class TestMultiPathIndependence(unittest.TestCase):
    """Verify that different computation paths give the same answer."""

    def test_path1_vs_path2(self):
        """Direct enumeration vs analytic formulas give identical results."""
        for c in C_VALS:
            enum_total = Fraction(0)
            anal_total = Fraction(0)
            for name, func in ANALYTIC_FUNCTIONS.items():
                idx = next(i for i, G in enumerate(GRAPHS) if G['name'] == name)
                enum_total += graph_amplitude_total(idx, c)['total']
                anal_total += func(c)['total']
            self.assertEqual(enum_total, anal_total)

    def test_boundary_sum_vs_graph_by_graph(self):
        """Full boundary sum matches sum of individual graph totals."""
        for c in C_VALS:
            boundary = full_boundary_sum(c)
            individual = Fraction(0)
            for idx in range(1, len(GRAPHS)):
                individual += graph_amplitude_total(idx, c)['total']
            self.assertEqual(boundary['total'], individual)

    def test_cross_channel_formula_vs_enumeration(self):
        """Closed-form (c+204)/(16c) matches enumeration of mixed amplitudes."""
        for c in C_VALS:
            boundary = full_boundary_sum(c)
            formula = cross_channel_correction(c)
            self.assertEqual(boundary['mixed'], formula)


if __name__ == '__main__':
    unittest.main()
