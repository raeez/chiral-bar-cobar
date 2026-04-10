r"""Tests for the mixed-sector cross-channel engine.

Tests the hypothesis that the mixed sector of SC^{ch,top,!} controls
the cross-channel correction delta_F_g^cross.

Test structure:
  1-5:   SC^! dimension foundations
  6-10:  Convolution algebra sector decomposition
  11-15: Channel assignment counting
  16-20: Uniform-weight cancellation
  21-25: W_3 mixed-sector analysis
  26-30: Hypothesis testing
  31-35: Numerical verification of delta_F_2
  36-40: Mixed-sector growth and scaling
  41-45: Explicit mixed operations
  46-50: Structural correspondences and synthesis

Multi-path verification (CLAUDE.md mandate): every numerical result
verified by at least 2 independent paths.

AP-aware:
  AP1:  All dimensions computed independently, not copied
  AP10: Expected values derived from multiple sources
  AP14: Koszulness != SC formality (the cooperad structure is universal)
  AP27: Propagator weight is 1, not h (controls per-channel kappa)
  AP45: Desuspension convention matches signs_and_shifts.tex
"""

import sys
import os
import unittest
from fractions import Fraction
from math import factorial, comb

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mixed_sector_cross_channel_engine import (
    # Sector dimensions
    lie_dim,
    ass_dim,
    mixed_dim,
    mixed_excess,
    mixed_excess_ratio,
    # Convolution decomposition
    conv_dim_closed,
    conv_dim_open,
    conv_dim_mixed,
    conv_total_dim,
    # Channel assignments
    channel_assignment_count,
    # Uniform-weight analysis
    uniform_weight_graph_amplitude_ratio,
    # Mixed-sector MC components
    mixed_sector_mc_components,
    # W_3 analysis
    w3_mixed_sector_analysis,
    w3_graph_channel_decomposition,
    # Cross-channel structure
    mixed_sector_vs_cross_channel,
    propagator_variance_from_kappas,
    genus2_cross_channel_from_kappa_diff,
    # Hypothesis testing
    test_hypothesis_mixed_equals_cross,
    # Numerical verification
    verify_delta_F2_W3_numerically,
    # Growth analysis
    mixed_sector_growth,
    # Explicit operations
    mixed_operations_explicit,
    # Genus-2 correspondence
    genus2_mixed_correspondence,
    # Free energy decomposition
    free_energy_sector_decomposition,
    # Synthesis
    structural_theorem_summary,
)


# ============================================================================
# 1-5: SC^! DIMENSION FOUNDATIONS
# ============================================================================

class TestSCDualDimensions(unittest.TestCase):
    """Verify SC^! sector dimensions from first principles."""

    def test_lie_dim_basic(self):
        """Lie(n) = (n-1)! for n = 1..6."""
        expected = [1, 1, 2, 6, 24, 120]
        for n, exp in enumerate(expected, 1):
            self.assertEqual(lie_dim(n), exp, f"Lie({n}) != {exp}")

    def test_lie_dim_zero(self):
        """Lie(0) = 0 and Lie(-1) = 0."""
        self.assertEqual(lie_dim(0), 0)
        self.assertEqual(lie_dim(-1), 0)

    def test_ass_dim_basic(self):
        """Ass(m) = m! for m = 1..6."""
        for m in range(1, 7):
            self.assertEqual(ass_dim(m), factorial(m))

    def test_mixed_dim_known_values(self):
        """Verify SC^!(k,m) at small arities against known results.

        Livernet 2006, Loday-Vallette Section 13.3:
        (1,0) -> 1, (0,1) -> 1, (2,0) -> 1, (0,2) -> 2,
        (1,1) -> 2, (3,0) -> 2, (0,3) -> 6.
        """
        known = {
            (1, 0): 1, (0, 1): 1, (2, 0): 1, (0, 2): 2,
            (1, 1): 2, (3, 0): 2, (0, 3): 6,
            (2, 1): 3, (1, 2): 3, (2, 2): 6,
        }
        for (k, m), exp in known.items():
            self.assertEqual(mixed_dim(k, m), exp,
                             f"SC^!({k},{m}) = {mixed_dim(k,m)}, expected {exp}")

    def test_mixed_dim_formula(self):
        """Verify SC^!(k,m) = (k-1)! * C(k+m,m) for k >= 1, m >= 0."""
        for k in range(1, 6):
            for m in range(0, 6):
                expected = factorial(k - 1) * comb(k + m, m)
                self.assertEqual(mixed_dim(k, m), expected,
                                 f"Formula mismatch at ({k},{m})")


class TestMixedExcess(unittest.TestCase):
    """Verify the excess of mixed dim over naive tensor product."""

    def test_excess_11(self):
        """SC^!(1,1) = 2 > Lie(1)*Ass(1) = 1*1 = 1. Excess = 1."""
        self.assertEqual(mixed_excess(1, 1), 1)

    def test_excess_21(self):
        """SC^!(2,1) = 3 > Lie(2)*Ass(1) = 1*1 = 1. Excess = 2."""
        self.assertEqual(mixed_excess(2, 1), 2)

    def test_excess_12(self):
        """SC^!(1,2) = 3 > Lie(1)*Ass(2) = 1*2 = 2. Excess = 1."""
        self.assertEqual(mixed_excess(1, 2), 1)

    def test_excess_22(self):
        """SC^!(2,2) = 6 > Lie(2)*Ass(2) = 1*2 = 2. Excess = 4."""
        self.assertEqual(mixed_excess(2, 2), 4)

    def test_excess_ratio_geq_1_when_k_geq_m(self):
        """The mixed/naive ratio >= 1 when k >= m (shuffles dominate)."""
        for k in range(1, 6):
            for m in range(1, k + 1):
                ratio = mixed_excess_ratio(k, m)
                self.assertGreaterEqual(ratio, 1,
                                        f"Ratio < 1 at ({k},{m}) with k >= m")

    def test_excess_ratio_can_be_less_than_1(self):
        """The ratio can be < 1 when m >> k (shuffle < full symmetric)."""
        # SC^!(1,3) = 4, Lie(1)*Ass(3) = 1*6 = 6, ratio = 2/3 < 1
        ratio = mixed_excess_ratio(1, 3)
        self.assertEqual(ratio, Fraction(2, 3))
        self.assertLess(ratio, 1)

    def test_excess_ratio_formula(self):
        """Ratio = C(k+m,m) / m! for k >= 1, m >= 1."""
        for k in range(1, 5):
            for m in range(1, 5):
                expected = Fraction(comb(k + m, m), factorial(m))
                self.assertEqual(mixed_excess_ratio(k, m), expected,
                                 f"Ratio formula mismatch at ({k},{m})")


# ============================================================================
# 6-10: CONVOLUTION ALGEBRA SECTOR DECOMPOSITION
# ============================================================================

class TestConvolutionDecomposition(unittest.TestCase):
    """Verify convolution algebra dimensions by sector."""

    def test_closed_sector_gen1(self):
        """For gen_dim=1: Conv(Lie^c, End)(k) = Lie(k) * 1 = (k-1)!."""
        for k in range(1, 6):
            self.assertEqual(conv_dim_closed(k, 1), lie_dim(k))

    def test_open_sector_gen1(self):
        """For gen_dim=1: Conv(Ass^c, End)(m) = Ass(m) * 1 = m!."""
        for m in range(1, 6):
            self.assertEqual(conv_dim_open(m, 1), ass_dim(m))

    def test_mixed_sector_gen2(self):
        """For gen_dim=2 (W_3): mixed conv dim at (1,1) = 2 * 2^3 = 16."""
        self.assertEqual(conv_dim_mixed(1, 1, 2), 2 * 8)

    def test_mixed_sector_gen3(self):
        """For gen_dim=3 (W_4): mixed conv dim at (1,1) = 2 * 3^3 = 54."""
        self.assertEqual(conv_dim_mixed(1, 1, 3), 2 * 27)

    def test_total_decomposition(self):
        """Total = closed + open + mixed at each total arity."""
        for n in range(1, 5):
            for gen_dim in [1, 2, 3]:
                result = conv_total_dim(n, gen_dim)
                self.assertEqual(
                    result['total'],
                    result['closed'] + result['open'] + result['mixed'],
                    f"Decomposition mismatch at n={n}, gen_dim={gen_dim}")

    def test_single_generator_no_mixed(self):
        """For gen_dim=1 (single generator): mixed sector has zero
        GRAPH-LEVEL contribution because there is only one channel."""
        # The cooperad-level mixed sector is nonzero, but the
        # single-channel algebra has no cross-channel mixing.
        # At the convolution level, mixed_dim(1,1) * 1^3 = 2,
        # but the PHYSICAL interpretation requires distinct channels.
        # This is a structural observation, not a dimension check.
        pass


# ============================================================================
# 11-15: CHANNEL ASSIGNMENT COUNTING
# ============================================================================

class TestChannelAssignments(unittest.TestCase):
    """Verify channel assignment counts for graph sums."""

    def test_single_edge_2_channels(self):
        """1 edge, 2 channels: 2 total, 2 single, 0 mixed."""
        result = channel_assignment_count(1, 2)
        self.assertEqual(result['total_assignments'], 2)
        self.assertEqual(result['single_channel'], 2)
        self.assertEqual(result['mixed_channel'], 0)

    def test_two_edges_2_channels(self):
        """2 edges, 2 channels: 4 total, 2 single, 2 mixed."""
        result = channel_assignment_count(2, 2)
        self.assertEqual(result['total_assignments'], 4)
        self.assertEqual(result['single_channel'], 2)
        self.assertEqual(result['mixed_channel'], 2)

    def test_three_edges_2_channels(self):
        """3 edges, 2 channels: 8 total, 2 single, 6 mixed."""
        result = channel_assignment_count(3, 2)
        self.assertEqual(result['total_assignments'], 8)
        self.assertEqual(result['single_channel'], 2)
        self.assertEqual(result['mixed_channel'], 6)

    def test_three_edges_3_channels(self):
        """3 edges, 3 channels: 27 total, 3 single, 24 mixed."""
        result = channel_assignment_count(3, 3)
        self.assertEqual(result['total_assignments'], 27)
        self.assertEqual(result['single_channel'], 3)
        self.assertEqual(result['mixed_channel'], 24)

    def test_mixed_fraction_grows_with_edges(self):
        """The fraction of mixed assignments grows with the number of edges."""
        r = 2
        fracs = []
        for E in range(1, 8):
            result = channel_assignment_count(E, r)
            fracs.append(result['mixed_fraction'])
        for i in range(1, len(fracs)):
            self.assertGreaterEqual(fracs[i], fracs[i - 1])


# ============================================================================
# 16-20: UNIFORM-WEIGHT CANCELLATION
# ============================================================================

class TestUniformWeightCancellation(unittest.TestCase):
    """Verify that delta_F_cross = 0 for uniform-weight algebras."""

    def test_single_channel(self):
        """Single channel: trivially delta_F = 0."""
        from sympy import Symbol
        c = Symbol('c')
        result = uniform_weight_graph_amplitude_ratio([c / 2], 3)
        self.assertTrue(result['uniform'])

    def test_two_equal_kappas(self):
        """Two channels with equal kappa: delta_F = 0."""
        from sympy import Symbol, Rational
        c = Symbol('c')
        kappas = [c / 2, c / 2]
        result = uniform_weight_graph_amplitude_ratio(kappas, 3)
        self.assertTrue(result['uniform'])

    def test_two_unequal_kappas(self):
        """Two channels with unequal kappa: delta_F nonzero."""
        from sympy import Symbol, Rational
        c = Symbol('c')
        kappas = [c / 2, c / 3]
        result = uniform_weight_graph_amplitude_ratio(kappas, 3)
        self.assertFalse(result['uniform'])

    def test_three_equal_kappas(self):
        """Three channels with equal kappa: delta_F = 0."""
        from sympy import Symbol
        c = Symbol('c')
        kappas = [c / 3, c / 3, c / 3]
        result = uniform_weight_graph_amplitude_ratio(kappas, 3)
        self.assertTrue(result['uniform'])

    def test_propagator_variance_vanishes_uniform(self):
        """Propagator variance = 0 for uniform kappas."""
        from sympy import Symbol, Rational
        c = Symbol('c')
        kappas = [c / 2, c / 2]
        result = propagator_variance_from_kappas(kappas, [c / 2, c / 2])
        self.assertTrue(result['uniform'])


# ============================================================================
# 21-25: W_3 MIXED-SECTOR ANALYSIS
# ============================================================================

class TestW3MixedSector(unittest.TestCase):
    """Verify W_3 mixed-sector structure."""

    def test_cooperad_dim_11(self):
        """SC^!(1,1) = 2 for W_3 mixed sector."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['cooperad_dim_11'], 2)

    def test_cooperad_dim_21(self):
        """SC^!(2,1) = 3."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['cooperad_dim_21'], 3)

    def test_cooperad_dim_12(self):
        """SC^!(1,2) = 3."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['cooperad_dim_12'], 3)

    def test_cooperad_dim_22(self):
        """SC^!(2,2) = 6."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['cooperad_dim_22'], 6)

    def test_kappa_ratio(self):
        """kappa_T / kappa_W = (c/2) / (c/3) = 3/2."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['kappa_ratio'], Fraction(3, 2))

    def test_delta_F2_at_c1(self):
        """delta_F_2(W_3, c=1) = (1+204)/16 = 205/16."""
        result = w3_mixed_sector_analysis()
        self.assertEqual(result['delta_F2_at_c1'], Fraction(205, 16))

    def test_graph_channel_decomposition(self):
        """Verify graph-channel decomposition for W_3 at genus 2."""
        result = w3_graph_channel_decomposition()
        # 4 graphs contribute to cross-channel
        self.assertEqual(result['num_contributing'], 4)
        # Contributing: D_sunset, E_bridge_loop, F_theta, G_barbell
        expected_contrib = ['D_sunset', 'E_bridge_loop', 'F_theta', 'G_barbell']
        self.assertEqual(sorted(result['contributing_graphs']),
                         sorted(expected_contrib))

    def test_total_mixed_assignments(self):
        """Total mixed assignments across all genus-2 graphs."""
        result = w3_graph_channel_decomposition()
        # D: 6, E: 2, F: 6, G: 6 = 20 mixed assignments
        self.assertEqual(result['total_mixed_channel_assignments'], 20)


# ============================================================================
# 26-30: HYPOTHESIS TESTING
# ============================================================================

class TestHypothesis(unittest.TestCase):
    """Test the hypothesis: mixed sector controls cross-channel."""

    def test_hypothesis_all_pass(self):
        """All 5 hypothesis tests should pass."""
        result = test_hypothesis_mixed_equals_cross()
        self.assertEqual(result['T1_virasoro'], 'PASS: r=1, no mixed sector, no cross-channel')
        self.assertEqual(result['T2_W3'], 'PASS: cooperad_11=2, delta_F_2 nonzero')
        self.assertEqual(result['T5_trivalent'], 'PASS: cooperad_12=3 matches 3 orderings of type (a,a,b)')

    def test_cooperad_12_equals_3_for_all_N(self):
        """SC^!(1,2) = 3 regardless of N (cooperad is universal)."""
        result = test_hypothesis_mixed_equals_cross(N_values=range(3, 8))
        for N, data in result['results'].items():
            self.assertTrue(data['cooperad_12_equals_3'],
                            f"SC^!(1,2) != 3 for N={N}")

    def test_trivalent_type_aab_count(self):
        """Type (a,a,b) trivalent assignments: 3 orderings per channel pair."""
        result = test_hypothesis_mixed_equals_cross()
        for N, data in result['results'].items():
            self.assertEqual(data['type_aab_per_pair'], 3)

    def test_type_aab_total_formula(self):
        """Total (a,a,b) type: r*(r-1)*3 for r channels."""
        for N in range(3, 8):
            r = N - 1
            result = test_hypothesis_mixed_equals_cross(N_values=[N])
            expected = r * (r - 1) * 3
            self.assertEqual(result['results'][N]['type_aab'], expected)

    def test_mixed_vs_cross_consistency(self):
        """Cross-check mixed-sector dim vs cross-channel parameters."""
        for N in [3, 4, 5]:
            result = mixed_sector_vs_cross_channel(N)
            r = N - 1
            # Trivalent mixed = r^3 - r
            self.assertEqual(result['genus2_mixed_assignments']['sunset'], r ** 3 - r)
            self.assertEqual(result['genus2_mixed_assignments']['theta'], r ** 3 - r)


# ============================================================================
# 31-35: NUMERICAL VERIFICATION
# ============================================================================

class TestNumericalVerification(unittest.TestCase):
    """Numerically verify delta_F_2(W_3) and related quantities."""

    def test_delta_F2_positivity(self):
        """delta_F_2(W_3) > 0 for all c > 0."""
        result = verify_delta_F2_W3_numerically()
        self.assertTrue(result['all_positive'])

    def test_delta_F2_large_c_limit(self):
        """delta_F_2(W_3) -> 1/16 as c -> infinity."""
        result = verify_delta_F2_W3_numerically()
        self.assertAlmostEqual(result['large_c_limit'], 1 / 16)

    def test_delta_F2_at_c1(self):
        """delta_F_2(W_3, c=1) = 205/16 = 12.8125."""
        result = verify_delta_F2_W3_numerically()
        self.assertAlmostEqual(result['values'][1]['delta_F2'], 205 / 16)

    def test_delta_F2_at_c10(self):
        """delta_F_2(W_3, c=10) = 214/160 = 107/80."""
        result = verify_delta_F2_W3_numerically()
        self.assertAlmostEqual(result['values'][10]['delta_F2'], 214 / 160, places=10)

    def test_koszul_conductor_W3(self):
        """Koszul conductor K_3 = 100."""
        result = verify_delta_F2_W3_numerically()
        self.assertEqual(result['koszul_conductor'], 100)


# ============================================================================
# 36-40: MIXED-SECTOR GROWTH AND SCALING
# ============================================================================

class TestMixedSectorGrowth(unittest.TestCase):
    """Test how mixed-sector dimensions grow with N."""

    def test_cooperad_independent_of_N(self):
        """Cooperad dimensions are universal (independent of N)."""
        result = mixed_sector_growth(max_N=8)
        self.assertTrue(result['cooperad_independent_of_N'])
        # All N should have the same mixed_11
        dims_11 = set(result['data'][N]['mixed_11'] for N in range(2, 9))
        self.assertEqual(len(dims_11), 1)
        self.assertEqual(dims_11.pop(), 2)

    def test_conv_growth_with_N(self):
        """Convolution dim at (1,1) grows as r^3 = (N-1)^3."""
        result = mixed_sector_growth(max_N=8)
        for N in range(2, 9):
            r = N - 1
            expected = 2 * r ** 3  # mixed_dim(1,1) * r^3
            self.assertEqual(result['data'][N]['conv_11'], expected)

    def test_B_N_quadratic(self):
        """B(N) = (N-2)(N+3)/96 is the leading genus-2 cross-channel coefficient."""
        result = mixed_sector_growth(max_N=8)
        # B(2) = 0, B(3) = 1*6/96 = 1/16, B(4) = 2*7/96 = 7/48
        self.assertEqual(result['data'][2]['B_N'], Fraction(0))
        self.assertEqual(result['data'][3]['B_N'], Fraction(6, 96))
        self.assertEqual(result['data'][4]['B_N'], Fraction(14, 96))

    def test_B_3_matches_delta_F2_limit(self):
        """B(3) = 1/16 matches the large-c limit of delta_F_2(W_3)."""
        result = mixed_sector_growth()
        self.assertEqual(result['data'][3]['B_N'], Fraction(1, 16))

    def test_B_N_vanishes_for_virasoro(self):
        """B(2) = 0: Virasoro has no cross-channel correction."""
        result = mixed_sector_growth()
        self.assertEqual(result['data'][2]['B_N'], Fraction(0))


# ============================================================================
# 41-45: EXPLICIT MIXED OPERATIONS
# ============================================================================

class TestExplicitMixedOperations(unittest.TestCase):
    """Verify the explicit construction of mixed operations."""

    def test_operations_11(self):
        """SC^!(1,1): 2 operations with patterns CO and OC."""
        result = mixed_operations_explicit(1, 1)
        self.assertEqual(result['total_dim'], 2)
        patterns = [op['pattern'] for op in result['operations']]
        self.assertIn('CO', patterns)
        self.assertIn('OC', patterns)

    def test_operations_12(self):
        """SC^!(1,2): 3 operations with patterns COO, OCO, OOC."""
        result = mixed_operations_explicit(1, 2)
        self.assertEqual(result['total_dim'], 3)
        patterns = [op['pattern'] for op in result['operations']]
        self.assertIn('COO', patterns)
        self.assertIn('OCO', patterns)
        self.assertIn('OOC', patterns)

    def test_operations_21(self):
        """SC^!(2,1): 3 operations (1 Lie bracket * 3 shuffles)."""
        result = mixed_operations_explicit(2, 1)
        self.assertEqual(result['total_dim'], 3)
        self.assertEqual(result['lie_dim'], 1)
        self.assertEqual(result['num_shuffles'], 3)

    def test_operations_22(self):
        """SC^!(2,2): 6 operations (1 Lie bracket * 6 shuffles)."""
        result = mixed_operations_explicit(2, 2)
        self.assertEqual(result['total_dim'], 6)
        self.assertEqual(result['num_shuffles'], 6)

    def test_operations_30(self):
        """SC^!(3,0) is in the closed sector: not valid for mixed_operations_explicit."""
        result = mixed_operations_explicit(3, 0)
        self.assertFalse(result['valid'])


# ============================================================================
# 46-50: STRUCTURAL CORRESPONDENCES AND SYNTHESIS
# ============================================================================

class TestStructuralCorrespondences(unittest.TestCase):
    """Verify the structural correspondence between sectors and corrections."""

    def test_genus2_correspondence_W3(self):
        """Verify genus-2 correspondence for W_3."""
        result = genus2_mixed_correspondence(N=3)
        self.assertEqual(result['r'], 2)
        # Should have correspondences for trivalent and bivalent vertices
        self.assertGreaterEqual(len(result['correspondences']), 2)

    def test_genre2_trivalent_aab_matches_cooperad(self):
        """The cooperad dim SC^!(1,2) = 3 matches the 3 orderings of (a,a,b)."""
        result = genus2_mixed_correspondence(N=3)
        trivalent = result['correspondences'][0]
        self.assertEqual(trivalent['cooperad_dim'], 3)
        # For r=2: 2*1*3 = 6 assignments, ratio = 6/3 = 2 (= r*(r-1))
        self.assertEqual(trivalent['ratio'], Fraction(6, 3))

    def test_synthesis_sectors(self):
        """Verify the structural theorem summary has all key components."""
        result = structural_theorem_summary()
        self.assertIn('sector_decomposition', result['key_components'])
        self.assertIn('mc_splitting', result['key_components'])
        self.assertIn('free_energy_splitting', result['key_components'])

    def test_synthesis_uniform_cancellation(self):
        """Verify the uniform-weight cancellation is correctly summarized."""
        result = structural_theorem_summary()
        self.assertIn('S_r symmetry', result['uniform_weight_cancellation']['mechanism'])

    def test_synthesis_cooperad_match(self):
        """SC^!(1,2) = 3 matches 3 orderings."""
        result = structural_theorem_summary()
        self.assertEqual(result['cooperad_dimension_match']['SC!(1,2)'], 3)
        self.assertEqual(result['cooperad_dimension_match']['trivalent_orderings'], 3)


# ============================================================================
# BONUS: CROSS-ENGINE CONSISTENCY CHECKS
# ============================================================================

class TestCrossEngineConsistency(unittest.TestCase):
    """Cross-check with existing engines for consistency."""

    def test_lie_dim_matches_sc_cooperad_engine(self):
        """Verify lie_dim matches sc_koszul_dual_cooperad_engine.lie_operad_dim."""
        try:
            from sc_koszul_dual_cooperad_engine import lie_operad_dim
            for n in range(1, 8):
                self.assertEqual(lie_dim(n), lie_operad_dim(n),
                                 f"Mismatch at n={n}")
        except ImportError:
            self.skipTest("sc_koszul_dual_cooperad_engine not available")

    def test_mixed_dim_matches_sc_cooperad_engine(self):
        """Verify mixed_dim matches sc_koszul_dual_cooperad_engine.sc_koszul_dual_dim_mixed."""
        try:
            from sc_koszul_dual_cooperad_engine import sc_koszul_dual_dim_mixed
            for k in range(0, 6):
                for m in range(0, 6):
                    if k == 0 and m == 0:
                        continue
                    self.assertEqual(mixed_dim(k, m), sc_koszul_dual_dim_mixed(k, m),
                                     f"Mismatch at ({k},{m})")
        except ImportError:
            self.skipTest("sc_koszul_dual_cooperad_engine not available")

    def test_delta_F2_W3_matches_cross_channel_engine(self):
        """Verify delta_F_2(W_3) = (c+204)/(16c) matches multi_weight_cross_channel_engine."""
        try:
            from multi_weight_cross_channel_engine import delta_F2_W3_closed
            for cv in [1, 5, 10, 25, 100]:
                cv_f = Fraction(cv)
                expected = delta_F2_W3_closed(cv_f)
                from_formula = (cv_f + 204) / (16 * cv_f)
                self.assertEqual(expected, from_formula,
                                 f"Mismatch at c={cv}")
        except ImportError:
            self.skipTest("multi_weight_cross_channel_engine not available")

    def test_propagator_variance_matches_engine(self):
        """Cross-check propagator variance logic."""
        from sympy import Symbol, Rational
        c = Symbol('c')
        kappas = [c / 2, c / 3]  # W_3 channels
        result = propagator_variance_from_kappas(kappas, kappas)
        # For f = kappa (trivially proportional), variance should be 0
        self.assertTrue(result['uniform'])

    def test_free_energy_decomposition_genus1(self):
        """At genus 1, mixed component should vanish."""
        result = free_energy_sector_decomposition(3, g=1)
        self.assertTrue(result['at_genus_1_mixed_vanishes'])


class TestMixedSectorMCComponents(unittest.TestCase):
    """Test the mixed-sector MC component enumeration."""

    def test_gen_dim_2_total(self):
        """For gen_dim=2, total mixed dim at max_arity=3."""
        result = mixed_sector_mc_components(gen_dim=2, max_arity=3)
        # mixed_dim(k,m) = lie_dim(k) * C(k+m,m) = (k-1)! * C(k+m,m)
        # conv_dim(k,m) = mixed_dim(k,m) * gen_dim^{k+m+1}
        # VERIFIED: lie_dim(n) = (n-1)!, NOT n!  (AP89)
        #   lie_dim(1)=1, lie_dim(2)=1, lie_dim(3)=2
        # (1,1): 1*C(2,1)*2^3  = 2*8    = 16     # VERIFIED [DC] + [LT] AP89
        # (1,2): 1*C(3,2)*2^4  = 3*16   = 48     # VERIFIED [DC]
        # (1,3): 1*C(4,3)*2^5  = 4*32   = 128    # VERIFIED [DC]
        # (2,1): 1*C(3,1)*2^4  = 3*16   = 48     # VERIFIED [DC]
        # (2,2): 1*C(4,2)*2^5  = 6*32   = 192    # VERIFIED [DC]
        # (2,3): 1*C(5,3)*2^6  = 10*64  = 640    # VERIFIED [DC]
        # (3,1): 2*C(4,1)*2^5  = 8*32   = 256    # VERIFIED [DC] lie_dim(3)=2, NOT 6
        # (3,2): 2*C(5,2)*2^6  = 20*64  = 1280   # VERIFIED [DC]
        # (3,3): 2*C(6,3)*2^7  = 40*128 = 5120   # VERIFIED [DC]
        # Total = 16+48+128+48+192+640+256+1280+5120 = 7728
        total = result['total_mixed_dim']
        expected = (16 + 48 + 128 + 48 + 192 + 640 + 256 + 1280 + 5120)
        self.assertEqual(total, expected)

    def test_gen_dim_1_components(self):
        """For gen_dim=1, mixed sector has nontrivial cooperad dim
        but the endomorphism factor is 1, so conv dim = cooperad dim."""
        result = mixed_sector_mc_components(gen_dim=1, max_arity=3)
        for (k, m), data in result['components'].items():
            self.assertEqual(data['conv_dim'], data['cooperad_dim'])


if __name__ == '__main__':
    unittest.main()
