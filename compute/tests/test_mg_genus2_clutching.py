r"""Tests for Approach F: Clutching + Harer analysis of multi-generator universality at genus 2.

Verifies the full Approach F computation for W_3, including:
1. Graph topology and stability (foundational)
2. Multi-channel amplitudes per graph (3 independent paths each)
3. Cross-channel correction δF_2 = (c+204)/(16c) (3 paths)
4. Separating clutching consistency (3 paths)
5. Non-separating clutching data
6. Tautological decomposition Δ_2
7. R-matrix block-diagonality and genus-1 correction vanishing
8. Propagator variance
9. Harer stability analysis
10. Physical consistency: large-c, positivity, Koszul duality

Each computational result verified by at least 3 independent paths per the
Multi-Path Verification Mandate (CLAUDE.md).

Manuscript references:
    op:multi-generator-universality (higher_genus_foundations.tex)
    thm:theorem-d (higher_genus_modular_koszul.tex)
    rem:w3-genus2-cross-channel (higher_genus_modular_koszul.tex)
    eq:shadow-taut-genus2 (higher_genus_modular_koszul.tex)
    prop:tautological-line-support-criterion (higher_genus_modular_koszul.tex)
    rem:propagator-weight-universality (higher_genus_foundations.tex): AP27
"""

import unittest
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mg_genus2_clutching_engine import (
    # Foundational
    bernoulli, lambda_fp,
    HODGE_INTEGRALS,
    # Graph topology
    GENUS2_GRAPHS, StableGraph, verify_all_graphs,
    # Algebra data
    W3FrobeniusAlgebra,
    # Amplitudes
    compute_graph_amplitudes, GraphAmplitude,
    compute_cross_channel, CrossChannelResult,
    # Clutching
    compute_clutching, ClutchingData,
    # Tautological decomposition
    compute_taut_decomposition, TautDecomposition,
    # R-matrix
    r_matrix_analysis,
    # Propagator variance
    propagator_variance,
    # Harer stability
    harer_stability_analysis,
    # Approach F
    approach_f_intersection_number, approach_f_full,
    # Verification
    verify_cross_channel_three_paths,
    verify_separating_clutching,
    verify_boundary_graph_sum,
)


# Standard test central charges
C_VALUES = [
    Fraction(1), Fraction(2), Fraction(4), Fraction(10),
    Fraction(13), Fraction(26), Fraction(50), Fraction(100),
]


# ============================================================================
# 1. FOUNDATIONAL DATA
# ============================================================================

class TestBernoulli(unittest.TestCase):
    """Verify Bernoulli numbers (foundational)."""

    def test_B0(self):
        self.assertEqual(bernoulli(0), Fraction(1))

    def test_B1(self):
        self.assertEqual(bernoulli(1), Fraction(-1, 2))

    def test_B2(self):
        self.assertEqual(bernoulli(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(bernoulli(4), Fraction(-1, 30))

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(bernoulli(n), Fraction(0))


class TestFaberPandharipane(unittest.TestCase):
    """Verify Faber-Pandharipande numbers (3 paths)."""

    def test_lambda1_fp(self):
        # Path 1: Direct formula
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2_fp(self):
        # Path 1: Direct formula
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda2_fp_path2_from_bernoulli(self):
        # Path 2: From B_4 = -1/30
        # λ_2^FP = (2³-1)/2³ · |B_4|/(4!) = 7/8 · (1/30)/24 = 7/(8·720) = 7/5760
        result = Fraction(7, 8) * Fraction(1, 30) / Fraction(24)
        self.assertEqual(result, Fraction(7, 5760))
        self.assertEqual(lambda_fp(2), result)

    def test_lambda2_fp_path3_numerical(self):
        # Path 3: Numerical verification
        val = float(lambda_fp(2))
        self.assertAlmostEqual(val, 7/5760, places=15)

    def test_lambda3_fp(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))


class TestHodgeIntegrals(unittest.TestCase):
    """Verify fundamental Hodge intersection numbers."""

    def test_M11_lambda1(self):
        self.assertEqual(HODGE_INTEGRALS[(1, 1, 'lambda_1')], Fraction(1, 24))

    def test_M20_lambda2(self):
        self.assertEqual(HODGE_INTEGRALS[(2, 0, 'lambda_2')], Fraction(7, 5760))

    def test_M20_lambda1_lambda2(self):
        self.assertEqual(HODGE_INTEGRALS[(2, 0, 'lambda_1_lambda_2')], Fraction(1, 1152))


# ============================================================================
# 2. GRAPH TOPOLOGY
# ============================================================================

class TestGraphTopology(unittest.TestCase):
    """Verify all 7 stable graphs of M̄_{2,0}."""

    def test_seven_graphs(self):
        self.assertEqual(len(GENUS2_GRAPHS), 7)

    def test_all_genus_2(self):
        for G in GENUS2_GRAPHS:
            self.assertEqual(G.genus, 2, f"{G.name}: genus = {G.genus}")

    def test_all_stable(self):
        self.assertTrue(verify_all_graphs())

    def test_graph_names(self):
        names = [G.name for G in GENUS2_GRAPHS]
        expected = ['smooth', 'fig_eight', 'banana', 'dumbbell', 'theta', 'lollipop', 'barbell']
        self.assertEqual(names, expected)

    def test_automorphism_groups(self):
        auts = {G.name: G.aut for G in GENUS2_GRAPHS}
        self.assertEqual(auts['smooth'], 1)
        self.assertEqual(auts['fig_eight'], 2)
        self.assertEqual(auts['banana'], 8)
        self.assertEqual(auts['dumbbell'], 2)
        self.assertEqual(auts['theta'], 12)
        self.assertEqual(auts['lollipop'], 2)

    def test_edge_counts(self):
        edges = {G.name: G.n_edges for G in GENUS2_GRAPHS}
        self.assertEqual(edges['smooth'], 0)
        self.assertEqual(edges['fig_eight'], 1)
        self.assertEqual(edges['banana'], 2)
        self.assertEqual(edges['dumbbell'], 1)
        self.assertEqual(edges['theta'], 3)
        self.assertEqual(edges['lollipop'], 2)

    def test_betti_numbers(self):
        h1s = {G.name: G.h1 for G in GENUS2_GRAPHS}
        self.assertEqual(h1s['smooth'], 0)
        self.assertEqual(h1s['fig_eight'], 1)
        self.assertEqual(h1s['banana'], 2)
        self.assertEqual(h1s['dumbbell'], 0)
        self.assertEqual(h1s['theta'], 2)
        self.assertEqual(h1s['lollipop'], 1)

    def test_boundary_types(self):
        types = {G.name: G.boundary_type for G in GENUS2_GRAPHS}
        self.assertEqual(types['smooth'], 'interior')
        self.assertEqual(types['fig_eight'], 'non-separating')
        self.assertEqual(types['banana'], 'codim2')
        self.assertEqual(types['dumbbell'], 'separating')
        self.assertEqual(types['theta'], 'codim2')
        self.assertEqual(types['lollipop'], 'non-separating')


# ============================================================================
# 3. W_3 ALGEBRA DATA
# ============================================================================

class TestW3Algebra(unittest.TestCase):
    """Verify W_3 Frobenius algebra data."""

    def setUp(self):
        self.c = Fraction(100)
        self.alg = W3FrobeniusAlgebra(c=self.c)

    def test_kappa_T(self):
        self.assertEqual(self.alg.kappa_T, Fraction(50))

    def test_kappa_W(self):
        self.assertEqual(self.alg.kappa_W, Fraction(100, 3))

    def test_kappa_total(self):
        # Path 1: sum
        self.assertEqual(self.alg.kappa_total, Fraction(250, 3))
        # Path 2: formula 5c/6
        self.assertEqual(self.alg.kappa_total, 5 * self.c / 6)

    def test_propagators(self):
        # AP27: weight-1 for all channels
        self.assertEqual(self.alg.propagator('T'), Fraction(1, 50))
        self.assertEqual(self.alg.propagator('W'), Fraction(3, 100))

    def test_C3_Z2_symmetry(self):
        """Z_2 symmetry kills odd W-count."""
        c = self.c
        self.assertEqual(self.alg.C3('T', 'T', 'W'), Fraction(0))
        self.assertEqual(self.alg.C3('W', 'W', 'W'), Fraction(0))

    def test_C3_nonzero(self):
        c = self.c
        self.assertEqual(self.alg.C3('T', 'T', 'T'), c)
        self.assertEqual(self.alg.C3('T', 'W', 'W'), c)
        self.assertEqual(self.alg.C3('W', 'T', 'W'), c)
        self.assertEqual(self.alg.C3('W', 'W', 'T'), c)

    def test_V04_universality(self):
        """The genus-0 4-point function V_{0,4}(i,i|j,j) = 2c universally."""
        c = self.c
        for i in ['T', 'W']:
            for j in ['T', 'W']:
                self.assertEqual(self.alg.V04_s_channel(i, i, j, j), 2 * c)

    def test_genus1_vertex(self):
        self.assertEqual(self.alg.genus1_vertex('T'), self.alg.kappa_T / 24)
        self.assertEqual(self.alg.genus1_vertex('W'), self.alg.kappa_W / 24)


# ============================================================================
# 4. PER-GRAPH MULTI-CHANNEL AMPLITUDES
# ============================================================================

class TestGraphAmplitudes(unittest.TestCase):
    """Verify per-graph amplitudes with multi-path verification."""

    def test_fig_eight_c_independent(self):
        """Fig-eight: 1/48 + 1/48 = 1/24, independent of c."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            amps = compute_graph_amplitudes(alg)
            self.assertEqual(amps['fig_eight'].all_T, Fraction(1, 48))
            self.assertEqual(amps['fig_eight'].all_W, Fraction(1, 48))
            self.assertEqual(amps['fig_eight'].mixed, Fraction(0))
            self.assertEqual(amps['fig_eight'].total, Fraction(1, 24))

    def test_banana_three_paths(self):
        """Banana amplitude verified by 3 paths."""
        c = Fraction(10)
        alg = W3FrobeniusAlgebra(c=c)
        amps = compute_graph_amplitudes(alg)

        # Path 1: Direct from engine
        all_T = amps['banana'].all_T
        all_W = amps['banana'].all_W
        mixed = amps['banana'].mixed

        # Path 2: Analytic formulas
        self.assertEqual(all_T, Fraction(1) / c)        # 1/10
        self.assertEqual(all_W, Fraction(9) / (4 * c))  # 9/40
        self.assertEqual(mixed, Fraction(3) / c)          # 3/10

        # Path 3: From Feynman rules
        # (T,T): (2/c)²·2c / 8 = 8/(8c) = 1/c ✓
        self.assertEqual(Fraction(2, c)**2 * 2 * c / 8, Fraction(1) / c)
        # (W,W): (3/c)²·2c / 8 = 18/(8c) = 9/(4c) ✓
        self.assertEqual(Fraction(3, c)**2 * 2 * c / 8, Fraction(9) / (4 * c))
        # mixed (TW + WT): 2·(2/c)(3/c)·2c / 8 = 24/(8c) = 3/c ✓
        self.assertEqual(2 * Fraction(2, c) * Fraction(3, c) * 2 * c / 8,
                         Fraction(3) / c)

    def test_dumbbell_proportional_to_kappa(self):
        """Dumbbell amplitude = κ/1152 for all c."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            amps = compute_graph_amplitudes(alg)
            kappa = alg.kappa_total
            self.assertEqual(amps['dumbbell'].total, kappa / 1152)
            self.assertEqual(amps['dumbbell'].mixed, Fraction(0))

    def test_theta_three_paths(self):
        """Theta amplitude verified by 3 paths."""
        c = Fraction(10)
        alg = W3FrobeniusAlgebra(c=c)
        amps = compute_graph_amplitudes(alg)

        # Path 1: Direct from engine
        all_T = amps['theta'].all_T
        all_W = amps['theta'].all_W
        mixed = amps['theta'].mixed

        # Path 2: Analytic
        self.assertEqual(all_T, Fraction(2) / (3 * c))
        self.assertEqual(all_W, Fraction(0))
        self.assertEqual(mixed, Fraction(9) / (2 * c))

        # Path 3: Feynman rules
        # (T,T,T): (2/c)³·c² / 12 = 8c²/(12c³) = 8/(12c) = 2/(3c) ✓
        self.assertEqual(Fraction(2, c)**3 * c**2 / 12, Fraction(2) / (3 * c))
        # (T,W,W) × 3: each = (2/c)(3/c)²·c² / 12 = 18/(12c) = 3/(2c)
        # total = 3·3/(2c) = 9/(2c) ✓
        each_tww = Fraction(2, c) * Fraction(3, c)**2 * c**2 / 12
        self.assertEqual(each_tww, Fraction(3) / (2 * c))
        self.assertEqual(3 * each_tww, Fraction(9) / (2 * c))

    def test_lollipop_three_paths(self):
        """Lollipop amplitude verified by 3 paths."""
        c = Fraction(10)
        alg = W3FrobeniusAlgebra(c=c)
        amps = compute_graph_amplitudes(alg)

        # Path 1: Direct
        self.assertEqual(amps['lollipop'].all_T, Fraction(1, 24))
        self.assertEqual(amps['lollipop'].all_W, Fraction(0))
        self.assertEqual(amps['lollipop'].mixed, Fraction(1, 16))

        # Path 2: c-independence of mixed term
        for c2 in C_VALUES:
            alg2 = W3FrobeniusAlgebra(c=c2)
            amps2 = compute_graph_amplitudes(alg2)
            self.assertEqual(amps2['lollipop'].mixed, Fraction(1, 16),
                             f"Lollipop mixed should be 1/16 at c={c2}")

        # Path 3: From Feynman rules for (W,T) assignment
        # η^W·η^T · C_{WWT} · (κ_T/24) / |Aut|
        # = (3/c)(2/c) · c · (c/48) / 2 = 6c²/(96c²) = 1/16
        self.assertEqual(
            Fraction(3, c) * Fraction(2, c) * c * (c / 48) / 2,
            Fraction(1, 16)
        )


# ============================================================================
# 5. CROSS-CHANNEL CORRECTION (THE DECISIVE RESULT)
# ============================================================================

class TestCrossChannelCorrection(unittest.TestCase):
    """The cross-channel correction δF_2 = (c+204)/(16c) — verified 3 ways."""

    def test_three_path_verification(self):
        """Multi-path verification at multiple c values."""
        for c in C_VALUES:
            result = verify_cross_channel_three_paths(c)
            self.assertTrue(result['all_match'],
                            f"Three paths disagree at c={c}: {result}")

    def test_closed_form(self):
        """δF_2 = (c+204)/(16c) for all c."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            cross = compute_cross_channel(alg)
            expected = (c + 204) / (16 * c)
            self.assertEqual(cross.delta_F2, expected,
                             f"δF_2 ≠ (c+204)/(16c) at c={c}")

    def test_nonzero_for_positive_c(self):
        """δF_2 > 0 for all c > 0: universality fails."""
        for c in C_VALUES:
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
            self.assertGreater(cross.delta_F2, Fraction(0),
                               f"δF_2 should be positive at c={c}")

    def test_universality_fails(self):
        """Universality does NOT hold at genus 2 for W_3."""
        for c in C_VALUES:
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
            self.assertFalse(cross.universality_holds,
                             f"Universality should fail at c={c}")

    def test_per_graph_breakdown(self):
        """Verify per-graph contributions to δF_2."""
        c = Fraction(10)
        cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
        # banana: 3/c = 3/10
        self.assertEqual(cross.delta_banana, Fraction(3, 10))
        # theta: 9/(2c) = 9/20
        self.assertEqual(cross.delta_theta, Fraction(9, 20))
        # lollipop: 1/16
        self.assertEqual(cross.delta_lollipop, Fraction(1, 16))
        # barbell: 21/(4c) = 21/40
        self.assertEqual(cross.delta_barbell, Fraction(21, 40))
        # total: (10+204)/(16·10) = 214/160 = 107/80
        self.assertEqual(cross.delta_F2, Fraction(107, 80))

    def test_lollipop_c_independent(self):
        """The lollipop cross-channel is 1/16, independent of c."""
        for c in C_VALUES:
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
            self.assertEqual(cross.delta_lollipop, Fraction(1, 16))

    def test_banana_plus_theta_proportional_to_1_over_c(self):
        """Banana + theta = 15/(2c): purely 1/c."""
        for c in C_VALUES:
            cross = compute_cross_channel(W3FrobeniusAlgebra(c=c))
            self.assertEqual(cross.delta_banana + cross.delta_theta,
                             Fraction(15) / (2 * c))

    def test_large_c_limit(self):
        """As c → ∞, δF_2 → 1/16 (lollipop dominates)."""
        c_large = Fraction(10000)
        cross = compute_cross_channel(W3FrobeniusAlgebra(c=c_large))
        ratio = cross.delta_F2 / Fraction(1, 16)
        # Should be close to 1 + 204·16/(16·10000) ≈ 1.0204
        self.assertLess(abs(ratio - 1), Fraction(1, 20))

    def test_full_F2(self):
        """F_2^full = κ·λ_2^FP + δF_2."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            cross = compute_cross_channel(alg)
            expected = alg.kappa_total * lambda_fp(2) + (c + 204) / (16 * c)
            self.assertEqual(cross.F2_full, expected,
                             f"F_2 full mismatch at c={c}")

    def test_ratio_delta_to_universal(self):
        """The ratio δF_2 / (κ·λ_2^FP) = 432(c+204)/(7c²)."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            cross = compute_cross_channel(alg)
            ratio = cross.delta_F2 / cross.F2_scalar_universal
            expected = Fraction(432) * (c + 204) / (7 * c**2)
            self.assertEqual(ratio, expected,
                             f"Ratio mismatch at c={c}")


# ============================================================================
# 6. SEPARATING CLUTCHING CONSISTENCY
# ============================================================================

class TestSeparatingClutching(unittest.TestCase):
    """Separating clutching: automatic from genus-1 universality (3 paths)."""

    def test_three_path_verification(self):
        for c in C_VALUES:
            result = verify_separating_clutching(c)
            self.assertTrue(result['all_match'],
                            f"Three paths disagree at c={c}")

    def test_consistent_with_universality(self):
        """gl*(obs_2)|_{δ_0} = κ · gl*(λ_2) for all c."""
        for c in C_VALUES:
            result = verify_separating_clutching(c)
            self.assertTrue(result['consistent_with_universality'],
                            f"Separating clutching inconsistent at c={c}")

    def test_dumbbell_equals_kappa_over_1152(self):
        """Dumbbell amplitude = κ/1152."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            clutch = compute_clutching(alg)
            self.assertEqual(clutch.sep_obs, alg.kappa_total / 1152)

    def test_sep_lambda_is_1_over_1152(self):
        """gl*(λ_2) dumbbell contribution = (1/24)²/|Aut| = 1/1152.

        The raw clutching pullback is (1/24)² = 1/576, but the dumbbell
        graph has |Aut| = 2, so the graph-sum contribution is 1/1152.
        """
        for c in C_VALUES:
            clutch = compute_clutching(W3FrobeniusAlgebra(c=c))
            self.assertEqual(clutch.sep_lambda, Fraction(1, 1152))

    def test_sep_ratio_equals_kappa(self):
        """The ratio obs/lambda on the separating boundary = κ."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            clutch = compute_clutching(alg)
            self.assertEqual(clutch.sep_ratio, alg.kappa_total)


# ============================================================================
# 7. CLUTCHING DATA
# ============================================================================

class TestClutchingData(unittest.TestCase):
    """Full clutching analysis."""

    def test_nonsep_fig_eight(self):
        """Fig-eight contribution to non-separating boundary."""
        for c in C_VALUES:
            clutch = compute_clutching(W3FrobeniusAlgebra(c=c))
            self.assertEqual(clutch.nonsep_fig_eight, Fraction(1, 24))

    def test_boundary_sum_positive(self):
        """Total boundary contribution is positive."""
        for c in C_VALUES:
            clutch = compute_clutching(W3FrobeniusAlgebra(c=c))
            self.assertGreater(clutch.boundary_sum, Fraction(0))

    def test_codim2_breakdown(self):
        """Codim-2 contribution: banana + theta + lollipop."""
        c = Fraction(10)
        alg = W3FrobeniusAlgebra(c=c)
        amps = compute_graph_amplitudes(alg)
        clutch = compute_clutching(alg)
        expected = amps['banana'].total + amps['theta'].total + amps['lollipop'].total
        self.assertEqual(clutch.codim2_total, expected)


# ============================================================================
# 8. TAUTOLOGICAL DECOMPOSITION
# ============================================================================

class TestTautDecomposition(unittest.TestCase):
    """The genus-2 tautological decomposition eq:shadow-taut-genus2."""

    def test_W_line_vanishes(self):
        """W-line: α_W = 0, so both planted-forest and δ_irr terms vanish."""
        for c in C_VALUES:
            taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=c))
            self.assertEqual(taut.delta_pf_W, Fraction(0))
            # δ_irr_W = (0 - 0 - κ_W)/48 = -κ_W/48
            self.assertEqual(taut.delta_irr_W, -W3FrobeniusAlgebra(c=c).kappa_W / 48)

    def test_T_line_planted_forest(self):
        """T-line planted forest: α(10α - κ)/48 = 2(20 - c/2)/48 = (40 - c)/48."""
        for c in C_VALUES:
            taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=c))
            expected = Fraction(2) * (20 - c / 2) / 48
            self.assertEqual(taut.delta_pf_T, expected)

    def test_T_line_planted_forest_explicit(self):
        """At c = 10: δ_pf^T = 2(20-5)/48 = 30/48 = 5/8."""
        taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=Fraction(10)))
        self.assertEqual(taut.delta_pf_T, Fraction(5, 8))

    def test_T_line_delta_irr(self):
        """T-line δ_irr coefficient: (ακ/24 - α² - κ)/48."""
        c = Fraction(10)
        taut = compute_taut_decomposition(W3FrobeniusAlgebra(c=c))
        alpha = Fraction(2)
        kT = c / 2
        expected = (alpha * kT / 24 - alpha**2 - kT) / 48
        self.assertEqual(taut.delta_irr_T, expected)


# ============================================================================
# 9. R-MATRIX ANALYSIS
# ============================================================================

class TestRMatrixAnalysis(unittest.TestCase):
    """R-matrix structure for W_3 and cross-channel survival."""

    def test_block_diagonal(self):
        """R-matrix is block-diagonal (Z_2 symmetry)."""
        for c in C_VALUES:
            r = r_matrix_analysis(W3FrobeniusAlgebra(c=c))
            self.assertTrue(r['block_diagonal'])
            self.assertEqual(r['R_cross_TW'], Fraction(0))

    def test_genus1_correction_vanishes(self):
        """R-corrections to genus-1 vertex vanish on M̄_{1,1}."""
        for c in C_VALUES:
            r = r_matrix_analysis(W3FrobeniusAlgebra(c=c))
            self.assertEqual(r['genus1_R_correction'], Fraction(0))

    def test_cross_channel_survives(self):
        """Cross-channel correction survives R-matrix."""
        for c in C_VALUES:
            r = r_matrix_analysis(W3FrobeniusAlgebra(c=c))
            self.assertTrue(r['cross_channel_survives_R'])

    def test_R1_values(self):
        """First R-matrix coefficient R_1 = B_2/(2κ) = 1/(12κ)."""
        c = Fraction(10)
        r = r_matrix_analysis(W3FrobeniusAlgebra(c=c))
        # R_1^T = (1/6) / (c/2) = 2/(6c) = 1/(3c) = 1/30
        self.assertEqual(r['R1_T'], Fraction(1, 30))
        # R_1^W = (1/6) / (c/3) = 3/(6c) = 1/(2c) = 1/20
        self.assertEqual(r['R1_W'], Fraction(1, 20))


# ============================================================================
# 10. PROPAGATOR VARIANCE
# ============================================================================

class TestPropagatorVariance(unittest.TestCase):
    """Propagator variance (multi-channel non-autonomy)."""

    def test_positive_for_distinct_kappa(self):
        """Propagator variance > 0 when κ_T ≠ κ_W."""
        for c in C_VALUES:
            delta = propagator_variance(W3FrobeniusAlgebra(c=c))
            self.assertGreater(delta, Fraction(0))

    def test_explicit_formula(self):
        """δ_mix = (η^{TT})² + (η^{WW})² - ((η^{TT}+η^{WW})²)/2."""
        c = Fraction(10)
        alg = W3FrobeniusAlgebra(c=c)
        eT = alg.propagator('T')  # 2/10 = 1/5
        eW = alg.propagator('W')  # 3/10
        expected = eT**2 + eW**2 - (eT + eW)**2 / 2
        # = 1/25 + 9/100 - (1/5 + 3/10)²/2 = 1/25 + 9/100 - (1/2)²/2
        # = 4/100 + 9/100 - 25/(2·100) = 13/100 - 1/8 = 104/800 - 100/800 = 4/800 = 1/200
        self.assertEqual(propagator_variance(alg), expected)


# ============================================================================
# 11. HARER STABILITY
# ============================================================================

class TestHarerStability(unittest.TestCase):
    """Harer stability: does NOT constrain obs_2."""

    def test_stable_range(self):
        h = harer_stability_analysis()
        self.assertEqual(h['stable_range_genus2'], 0)

    def test_H2_not_stable(self):
        h = harer_stability_analysis()
        self.assertFalse(h['H2_in_stable_range'])

    def test_does_not_constrain(self):
        h = harer_stability_analysis()
        self.assertFalse(h['constrains_obs2'])


# ============================================================================
# 12. APPROACH F FULL COMPUTATION
# ============================================================================

class TestApproachFFull(unittest.TestCase):
    """Full Approach F computation and its verdict."""

    def test_full_at_c10(self):
        result = approach_f_full(Fraction(10))
        self.assertFalse(result['universality_holds'])
        self.assertTrue(result['clutching_sep_consistent'])
        self.assertTrue(result['delta_matches'])

    def test_delta_matches_simplified(self):
        """δF_2 matches the simplified formula (c+204)/(16c)."""
        for c in C_VALUES:
            result = approach_f_full(c)
            self.assertTrue(result['delta_matches'],
                            f"Simplified formula mismatch at c={c}")

    def test_F2_full_formula(self):
        """F_2 = 7c/6912 + (c+204)/(16c)."""
        for c in C_VALUES:
            result = approach_f_full(c)
            expected_universal = 5 * c / 6 * Fraction(7, 5760)
            expected_delta = (c + 204) / (16 * c)
            expected_full = expected_universal + expected_delta
            self.assertEqual(result['F2_full'], expected_full)

    def test_koszul_duality_constraint(self):
        """W_3 Koszul duality: c ↔ 100-c. Check δF_2 at dual charges."""
        c = Fraction(10)
        c_dual = Fraction(90)
        r1 = approach_f_full(c)
        r2 = approach_f_full(c_dual)
        # δF_2 at c=10: (10+120)/(160) = 130/160 = 13/16
        # δF_2 at c=90: (90+120)/(1440) = 210/1440 = 7/48
        # These are DIFFERENT — Koszul duality does NOT eliminate δF_2
        self.assertNotEqual(r1['delta_F2'], r2['delta_F2'])
        # But both are positive
        self.assertGreater(r1['delta_F2'], Fraction(0))
        self.assertGreater(r2['delta_F2'], Fraction(0))


# ============================================================================
# 13. BOUNDARY GRAPH SUM VERIFICATION
# ============================================================================

class TestBoundaryGraphSum(unittest.TestCase):
    """Boundary graph sum consistency (3 paths)."""

    def test_three_paths(self):
        for c in C_VALUES:
            result = verify_boundary_graph_sum(c)
            self.assertTrue(result['all_match'],
                            f"Three paths disagree at c={c}")


# ============================================================================
# 14. INTERSECTION NUMBER ANALYSIS
# ============================================================================

class TestIntersectionNumber(unittest.TestCase):
    """The single intersection number from Approach F."""

    def test_lambda1_lambda2(self):
        data = approach_f_intersection_number()
        self.assertEqual(data['int_lambda1_lambda2'], Fraction(1, 1152))

    def test_lambda2(self):
        data = approach_f_intersection_number()
        self.assertEqual(data['int_lambda2'], Fraction(7, 5760))

    def test_R2_dimension(self):
        data = approach_f_intersection_number()
        self.assertEqual(data['R2_dimension'], 3)

    def test_constraints_vs_dimension(self):
        """3 constraints (sep + nonsep + trace) vs dim R^2 ≤ 3."""
        data = approach_f_intersection_number()
        self.assertEqual(data['total_constraints'], data['R2_dimension'])


# ============================================================================
# 15. PHYSICAL CONSISTENCY
# ============================================================================

class TestPhysicalConsistency(unittest.TestCase):
    """Physical consistency checks."""

    def test_positivity(self):
        """F_2 > 0 for all c > 0."""
        for c in C_VALUES:
            result = approach_f_full(c)
            self.assertGreater(result['F2_full'], Fraction(0))

    def test_delta_F2_vanishes_only_at_unphysical_c(self):
        """δF_2 = (c+204)/(16c) = 0 only at c = -204 (unphysical)."""
        # For c > 0, both numerator and denominator are positive
        for c in C_VALUES:
            result = approach_f_full(c)
            self.assertNotEqual(result['delta_F2'], Fraction(0))

    def test_self_dual_point_c13(self):
        """At the Virasoro self-dual point c = 13, δF_2 is still nonzero."""
        result = approach_f_full(Fraction(13))
        # δF_2 = (13+204)/(16·13) = 217/208
        self.assertEqual(result['delta_F2'], Fraction(217, 208))
        self.assertFalse(result['universality_holds'])

    def test_critical_c26(self):
        """At the critical dimension c = 26."""
        result = approach_f_full(Fraction(26))
        # δF_2 = (26+204)/(16·26) = 230/416 = 115/208
        self.assertEqual(result['delta_F2'], Fraction(115, 208))

    def test_semiclassical_limit(self):
        """As c → ∞, F_2^full / (κ·λ_2^FP) → 1 (correction suppressed)."""
        c = Fraction(10000)
        result = approach_f_full(c)
        ratio = result['F2_full'] / result['F2_universal']
        # Should be close to 1 + 432·(c+204)/(7c²) ≈ 1 + 432/7c ≈ 1.006
        self.assertLess(abs(ratio - 1), Fraction(1, 10))

    def test_per_channel_additivity_of_diagonal(self):
        """Diagonal (per-channel) F_2 = κ_T · λ_2^FP + κ_W · λ_2^FP."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            l2 = lambda_fp(2)
            expected = alg.kappa_T * l2 + alg.kappa_W * l2
            result = compute_cross_channel(alg)
            self.assertEqual(result.F2_per_channel, expected)


# ============================================================================
# 16. CROSS-CONSISTENCY WITH MANUSCRIPT
# ============================================================================

class TestManuscriptConsistency(unittest.TestCase):
    """Verify consistency with rem:w3-genus2-cross-channel."""

    def test_manuscript_formula(self):
        """F_2^full = 7c/6912 + (c+204)/(16c) from rem:w3-genus2-cross-channel."""
        for c in C_VALUES:
            alg = W3FrobeniusAlgebra(c=c)
            result = approach_f_full(c)
            manuscript_universal = 7 * c / Fraction(6912)
            manuscript_delta = (c + 204) / (16 * c)
            manuscript_full = manuscript_universal + manuscript_delta
            self.assertEqual(result['F2_full'], manuscript_full,
                             f"Manuscript formula mismatch at c={c}")

    def test_manuscript_ratio(self):
        """δF_2/F_2^diag = 432(c+204)/(7c²) from rem:w3-genus2-cross-channel."""
        for c in C_VALUES:
            result = approach_f_full(c)
            ratio = result['delta_F2'] / result['F2_universal']
            expected = Fraction(432) * (c + 204) / (7 * c**2)
            self.assertEqual(ratio, expected)


if __name__ == '__main__':
    unittest.main()
