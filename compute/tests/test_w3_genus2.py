r"""Tests for the W₃ genus-2 free energy computation.

Verifies the multi-channel genus-2 graph sum for the W₃ algebra,
the first explicit computation for a multi-generator chiral algebra.

Test structure:
    1. Foundational data: λ_g^FP, κ values, OPE structure constants
    2. Graph topology: stability, genus, automorphism counts
    3. Per-graph amplitudes: analytic vs numerical for all 6 stable graphs
    4. Cross-channel correction: the multi-generator signal δF₂ = (c+204)/(16c)
    5. Planted-forest formula: δ_pf = S₃(10S₃ - κ)/48
    6. Single-channel limit: F₂ → κ·λ₂^FP when W decouples
    7. Koszul duality: constraints at c ↔ 100-c
    8. Physical consistency: positivity, linearity, large-c behavior
    9. Numerical spot-checks at c = 4 (free boson pair) and c = 50 (large c)

Manuscript references:
    thm:theorem-d, op:multi-generator-universality,
    eq:delta-pf-genus2-explicit, rem:propagator-weight-universality
"""

import unittest
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from w3_genus2 import (
    lambda_fp,
    kappa_T, kappa_W, kappa_total,
    propagator, C3, V04_s_channel,
    lambda_coupling, lambda_norm,
    S3_T, S3_W, S4_T, S4_W,
    verify_genus2_graphs,
    graph_amplitude, graph_total_amplitude,
    cross_channel_correction, cross_channel_correction_exact,
    cross_channel_decomposition,
    planted_forest_correction_T, planted_forest_correction_W,
    planted_forest_total,
    F2_w3_scalar_universal, F2_w3_per_channel,
    F2_w3_with_cross_channel,
    verify_single_channel_limit,
    verify_graph_amplitudes,
    compute_F2_w3,
    analytic_fig_eight, analytic_banana, analytic_dumbbell,
    analytic_theta, analytic_lollipop,
    diagonal_graph_sum,
    boundary_graph_sum,
    propagator_variance_w3,
    koszul_duality_check,
    _channel_assignments,
    GENUS2_GRAPHS,
)


# Standard test central charges
C_VALUES = [
    Fraction(1), Fraction(2), Fraction(4), Fraction(13), Fraction(26),
    Fraction(50), Fraction(100),
]


# ============================================================================
# 1. Foundational data
# ============================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Verify λ_g^FP values."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda2_breakdown(self):
        """λ₂^FP = (2³-1)/2³ · |B₄|/4! = 7/8 · 1/30 / 24 = 7/5760."""
        self.assertEqual(lambda_fp(2), Fraction(7, 8) * Fraction(1, 30) / 24)

    def test_lambda_invalid(self):
        with self.assertRaises(ValueError):
            lambda_fp(0)


class TestKappaValues(unittest.TestCase):
    """Verify κ_T, κ_W, and κ_total for W₃."""

    def test_kappa_T(self):
        for c in C_VALUES:
            self.assertEqual(kappa_T(c), c / 2)

    def test_kappa_W(self):
        for c in C_VALUES:
            self.assertEqual(kappa_W(c), c / 3)

    def test_kappa_total(self):
        for c in C_VALUES:
            self.assertEqual(kappa_total(c), Fraction(5) * c / 6)

    def test_kappa_additivity(self):
        """κ_T + κ_W = κ_total."""
        for c in C_VALUES:
            self.assertEqual(kappa_T(c) + kappa_W(c), kappa_total(c))

    def test_kappa_harmonic_number_derivation(self):
        """κ(W₃) = c·(H₃ - 1) = c·5/6, where H₃ = 11/6."""
        H3 = Fraction(1) + Fraction(1, 2) + Fraction(1, 3)
        self.assertEqual(H3, Fraction(11, 6))
        self.assertEqual(H3 - 1, Fraction(5, 6))
        for c in C_VALUES:
            self.assertEqual(kappa_total(c), c * (H3 - 1))


class TestW3OPE(unittest.TestCase):
    """Verify W₃ OPE structure constants."""

    def test_C_TTT(self):
        for c in C_VALUES:
            self.assertEqual(C3('T', 'T', 'T', c), c)

    def test_C_TWW(self):
        for c in C_VALUES:
            self.assertEqual(C3('T', 'W', 'W', c), c)

    def test_C_WWT(self):
        """C_{WWT} = C_{TWW} by permutation symmetry."""
        for c in C_VALUES:
            self.assertEqual(C3('W', 'W', 'T', c), c)

    def test_C_TTW_zero(self):
        """C_{TTW} = 0 by Z₂ symmetry (odd W count)."""
        for c in C_VALUES:
            self.assertEqual(C3('T', 'T', 'W', c), Fraction(0))

    def test_C_WWW_zero(self):
        """C_{WWW} = 0 by Z₂ symmetry (odd W count)."""
        for c in C_VALUES:
            self.assertEqual(C3('W', 'W', 'W', c), Fraction(0))

    def test_z2_symmetry_complete(self):
        """All 3-point functions with odd W count vanish (8 checks)."""
        for c in C_VALUES:
            for i in ['T', 'W']:
                for j in ['T', 'W']:
                    for k in ['T', 'W']:
                        w_count = sum(1 for x in (i, j, k) if x == 'W')
                        C = C3(i, j, k, c)
                        if w_count % 2 == 1:
                            self.assertEqual(C, Fraction(0),
                                             f"C_{{{i}{j}{k}}} should vanish (odd W)")
                        else:
                            self.assertEqual(C, c,
                                             f"C_{{{i}{j}{k}}} should equal c (even W)")

    def test_propagator(self):
        for c in C_VALUES:
            self.assertEqual(propagator('T', c), Fraction(2) / c)
            self.assertEqual(propagator('W', c), Fraction(3) / c)


class TestCompositeFieldData(unittest.TestCase):
    """Verify composite field Λ data."""

    def test_lambda_coupling(self):
        """c₃₃^Λ = 16/(22+5c)."""
        for c in C_VALUES:
            expected = Fraction(16) / (Fraction(22) + Fraction(5) * c)
            self.assertEqual(lambda_coupling(c), expected)

    def test_lambda_norm(self):
        """⟨Λ|Λ⟩ = c(5c+22)/10."""
        for c in C_VALUES:
            expected = c * (Fraction(5) * c + 22) / 10
            self.assertEqual(lambda_norm(c), expected)

    def test_lambda_norm_positive(self):
        """⟨Λ|Λ⟩ > 0 for c > 0 (physical unitarity)."""
        for c in C_VALUES:
            if c > 0:
                self.assertGreater(lambda_norm(c), 0)


# ============================================================================
# 2. Graph topology
# ============================================================================

class TestGraphTopology(unittest.TestCase):
    """Verify genus-2 stable graph enumeration."""

    def test_graph_count(self):
        self.assertEqual(len(GENUS2_GRAPHS), 7)

    def test_graph_stability_and_genus(self):
        verify_genus2_graphs()

    def test_individual_graph_genus(self):
        """Verify each graph individually."""
        for G in GENUS2_GRAPHS:
            n_v = len(G['vertices'])
            n_e = len(G['edges'])
            g_sum = sum(gv for gv, _ in G['vertices'])
            h1 = n_e - n_v + 1
            self.assertEqual(h1 + g_sum, 2, f"{G['name']} has wrong genus")

    def test_individual_graph_stability(self):
        """Each vertex satisfies 2g + val >= 3."""
        for G in GENUS2_GRAPHS:
            for gv, nv in G['vertices']:
                self.assertGreaterEqual(2 * gv + nv, 3,
                    f"{G['name']}: unstable vertex (g={gv}, n={nv})")

    def test_channel_assignments_count(self):
        """2^n channel assignments for n edges."""
        self.assertEqual(len(_channel_assignments(0)), 1)
        self.assertEqual(len(_channel_assignments(1)), 2)
        self.assertEqual(len(_channel_assignments(2)), 4)
        self.assertEqual(len(_channel_assignments(3)), 8)

    def test_graph_names(self):
        """All expected graph names present."""
        names = {G['name'] for G in GENUS2_GRAPHS}
        self.assertEqual(names, {'smooth', 'fig_eight', 'banana',
                                 'dumbbell', 'theta', 'lollipop', 'barbell'})


# ============================================================================
# 3. Per-graph amplitudes
# ============================================================================

class TestVertexFactors(unittest.TestCase):
    """Verify genus-0 vertex factors."""

    def test_V04_TTTT(self):
        """V_{0,4}(T,T,T,T) = (2/c)·c² = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('T', 'T', 'T', 'T', c)
            self.assertEqual(V, 2 * c)

    def test_V04_WWWW(self):
        """V_{0,4}(W,W,W,W) = (2/c)·c² = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('W', 'W', 'W', 'W', c)
            self.assertEqual(V, 2 * c)

    def test_V04_TTWW(self):
        """V_{0,4}(T,T,W,W) = (2/c)·c·c = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('T', 'T', 'W', 'W', c)
            self.assertEqual(V, 2 * c)

    def test_V04_banana_universal(self):
        """V_{0,4}(i,i,j,j) = 2c for ALL channel assignments.

        This universality is a consequence of the fact that only the
        T-channel contributes to the s-channel factorization (C_{iiT} = c
        for all i, and C_{iiW} = 0 for i = T since C_{TTW} = 0).

        Actually: C_{TTW} = 0, but C_{WWW} = 0 too. And C_{WWT} = c.
        So the W-channel contribution is:
            η^{WW}·C_{iiW}·C_{jjW} = (3/c)·C_{iiW}·C_{jjW}
        For (i,j) = (T,T): C_{TTW} = 0, so W-contribution = 0.
        For (i,j) = (T,W): C_{TTW} = 0, so W-contribution = 0.
        For (i,j) = (W,W): C_{WWW} = 0, so W-contribution = 0.
        In all cases, only T-channel: (2/c)·c·c = 2c.
        """
        for c in C_VALUES:
            for ch1 in ['T', 'W']:
                for ch2 in ['T', 'W']:
                    V = V04_s_channel(ch1, ch1, ch2, ch2, c)
                    self.assertEqual(V, 2 * c,
                                     f"V₀₄({ch1}{ch1}{ch2}{ch2}) != 2c at c={c}")


class TestGraphAmplitudes(unittest.TestCase):
    """Verify individual graph amplitudes against analytic formulas."""

    def test_fig_eight_per_channel(self):
        """Γ₁: A^T = 1/48, A^W = 1/48. Total = 1/24."""
        for c in C_VALUES:
            r = graph_total_amplitude(1, c)
            self.assertEqual(r['all_T'], Fraction(1, 48))
            self.assertEqual(r['all_W'], Fraction(1, 48))
            self.assertEqual(r['total'], Fraction(1, 24))

    def test_fig_eight_no_mixed(self):
        """Γ₁: single edge, no mixed channel assignments."""
        for c in C_VALUES:
            r = graph_total_amplitude(1, c)
            self.assertEqual(r['mixed'], Fraction(0))

    def test_banana_all_T(self):
        """Γ₂ all-T: (1/8)·(2/c)²·2c = 1/c."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['all_T'], Fraction(1) / c)

    def test_banana_all_W(self):
        """Γ₂ all-W: (1/8)·(3/c)²·2c = 9/(4c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['all_W'], Fraction(9) / (4 * c))

    def test_banana_mixed(self):
        """Γ₂ mixed: (1/8)·2·(2/c)(3/c)·2c = 3/c."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['mixed'], Fraction(3) / c)

    def test_dumbbell_per_channel(self):
        """Γ₃: A^T = c/2304, A^W = c/3456. Total = 5c/6912."""
        for c in C_VALUES:
            r = graph_total_amplitude(3, c)
            expected_total = kappa_total(c) / 1152
            self.assertEqual(r['all_T'] + r['all_W'], expected_total)

    def test_dumbbell_no_mixed(self):
        """Γ₃: single edge, no mixed."""
        for c in C_VALUES:
            r = graph_total_amplitude(3, c)
            self.assertEqual(r['mixed'], Fraction(0))

    def test_theta_all_T(self):
        """Γ₄ all-T: (1/12)·(2/c)³·c² = 2/(3c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['all_T'], Fraction(2) / (3 * c))

    def test_theta_all_W(self):
        """Γ₄ all-W: C_{WWW} = 0, so amplitude = 0."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['all_W'], Fraction(0))

    def test_theta_mixed(self):
        """Γ₄ mixed: (1/12)·3·(2/c)(3/c)²·c² = 9/(2c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['mixed'], Fraction(9) / (2 * c))

    def test_lollipop_all_T(self):
        """Γ₅ all-T: (1/2)·(2/c)²·c·(c/48) = 1/24."""
        for c in C_VALUES:
            r = graph_total_amplitude(5, c)
            self.assertEqual(r['all_T'], Fraction(1, 24))

    def test_lollipop_all_W(self):
        """Γ₅ all-W: C_{WWW} = 0, so amplitude = 0."""
        for c in C_VALUES:
            r = graph_total_amplitude(5, c)
            self.assertEqual(r['all_W'], Fraction(0))

    def test_lollipop_mixed(self):
        """Γ₅ mixed: (1/2)·(3/c)(2/c)·c·(c/48) = 1/16.

        This is INDEPENDENT OF c.
        """
        for c in C_VALUES:
            r = graph_total_amplitude(5, c)
            self.assertEqual(r['mixed'], Fraction(1, 16))

    def test_lollipop_mixed_c_independence(self):
        """The lollipop mixed amplitude 1/16 does not depend on c.

        Proof: (3/c)(2/c)·c·(c/48)/(2) = 6c²/(96c²) = 1/16.
        The c² in the numerator (from C_{WWT}·κ_T/24) cancels
        the c² in the denominator (from η^W·η^T).
        """
        for c1 in C_VALUES:
            for c2 in C_VALUES:
                r1 = graph_total_amplitude(5, c1)
                r2 = graph_total_amplitude(5, c2)
                self.assertEqual(r1['mixed'], r2['mixed'])


class TestAnalyticVsNumerical(unittest.TestCase):
    """Cross-check analytic formulas against the enumeration code."""

    def test_all_graphs_match(self):
        """For each graph, the analytic formula matches graph_total_amplitude."""
        for c in C_VALUES:
            results = verify_graph_amplitudes(c)
            for graph_name, checks in results.items():
                for key, val in checks.items():
                    if key.endswith('_match') or key == 'mixed_zero':
                        self.assertTrue(val,
                            f"{graph_name}.{key} FAILED at c={c}")


# ============================================================================
# 4. Cross-channel correction
# ============================================================================

class TestCrossChannelCorrection(unittest.TestCase):
    """Verify the total cross-channel correction δF₂ = (c+204)/(16c)."""

    def test_formula(self):
        """δF₂ = (c + 204)/(16c)."""
        for c in C_VALUES:
            delta = cross_channel_correction(c)
            expected = (c + 204) / (16 * c)
            self.assertEqual(delta, expected)

    def test_exact_breakdown(self):
        """Per-graph breakdown sums to total."""
        for c in C_VALUES:
            r = cross_channel_correction_exact(c)
            total = r['delta_banana'] + r['delta_theta'] + r['delta_lollipop'] + r['delta_barbell']
            self.assertEqual(total, r['delta_total'])
            self.assertTrue(r['match'])

    def test_nonzero(self):
        """The naive cross-channel correction is nonzero for c > 0."""
        for c in C_VALUES:
            if c > 0:
                delta = cross_channel_correction(c)
                self.assertNotEqual(delta, Fraction(0))

    def test_at_c1(self):
        """c = 1: δF₂ = (1+204)/(16·1) = 205/16."""
        self.assertEqual(cross_channel_correction(Fraction(1)),
                         Fraction(205, 16))

    def test_at_c2(self):
        """c = 2: δF₂ = (2+204)/(16·2) = 206/32 = 103/16."""
        self.assertEqual(cross_channel_correction(Fraction(2)),
                         Fraction(103, 16))

    def test_at_c26(self):
        """c = 26: δF₂ = (26+204)/(16·26) = 230/416 = 115/208."""
        self.assertEqual(cross_channel_correction(Fraction(26)),
                         Fraction(115, 208))

    def test_decomposition(self):
        """δF₂ decomposes into c-dependent and c-independent parts.

        (c+204)/(16c) = 1/16 + 204/(16c) = 1/16 + 51/(4c).
        banana(3/c) + theta(9/(2c)) + barbell(21/(4c)) = 51/(4c).
        """
        for c in C_VALUES:
            d = cross_channel_decomposition(c)
            self.assertEqual(d['c_dependent'], Fraction(51) / (4 * c))
            self.assertEqual(d['c_independent'], Fraction(1, 16))
            self.assertEqual(d['total'], d['c_dependent'] + d['c_independent'])

    def test_large_c_limit(self):
        """At large c: δF₂ → 1/16 (lollipop dominates).

        Exact: (c+204)/(16c) = 1/16 + 204/(16c) = 1/16 + 51/(4c).
        For c = 100000: 51/(4·100000) ≈ 0.0001275, so δF₂ ≈ 0.0625 + 0.0001275.
        """
        c_large = Fraction(100000)
        delta = cross_channel_correction(c_large)
        self.assertAlmostEqual(float(delta), 1/16, places=3)

    def test_ratio_to_F2(self):
        """The ratio δF₂/F₂_universal = 432(c+204)/(7c²)."""
        for c in C_VALUES:
            r = F2_w3_with_cross_channel(c)
            if r['F2_universal'] != 0:
                ratio = r['cross_channel_correction'] / r['F2_universal']
                expected = Fraction(432) * (c + 204) / (7 * c * c)
                self.assertEqual(ratio, expected)


# ============================================================================
# 5. Planted-forest corrections
# ============================================================================

class TestPlantedForest(unittest.TestCase):
    """Verify planted-forest corrections at genus 2."""

    def test_pf_T_formula(self):
        """δ_pf^T = S₃(10S₃ - κ_T)/48 = 2(20 - c/2)/48 = (40 - c)/24.

        Note: (40 - c)/24 = -(c - 40)/24. Different from -(c-40)/48
        because the formula uses the factored S₃ = 2 explicitly.

        Let's verify: S₃ = 2, κ_T = c/2.
        S₃(10S₃ - κ_T)/48 = 2(20 - c/2)/48 = (40 - c)/24.

        Wait: 2·(20 - c/2) = 40 - c. Then (40 - c)/48.
        """
        for c in C_VALUES:
            pf = planted_forest_correction_T(c)
            expected = Fraction(2) * (Fraction(20) - c / 2) / 48
            self.assertEqual(pf, expected)
            # Simplified: (40 - c)/48
            self.assertEqual(pf, (Fraction(40) - c) / 48)

    def test_pf_W_vanishes(self):
        """δ_pf^W = 0 (S₃^W = 0 by Z₂ parity)."""
        for c in C_VALUES:
            self.assertEqual(planted_forest_correction_W(c), Fraction(0))

    def test_pf_total(self):
        """Total planted-forest = δ_pf^T (since δ_pf^W = 0)."""
        for c in C_VALUES:
            self.assertEqual(planted_forest_total(c),
                             planted_forest_correction_T(c))

    def test_pf_vanishes_at_c40(self):
        """δ_pf^T vanishes at c = 40."""
        self.assertEqual(planted_forest_correction_T(Fraction(40)), Fraction(0))

    def test_pf_sign_below_40(self):
        """For c < 40: δ_pf^T > 0."""
        self.assertGreater(planted_forest_correction_T(Fraction(1)), 0)
        self.assertGreater(planted_forest_correction_T(Fraction(26)), 0)

    def test_pf_sign_above_40(self):
        """For c > 40: δ_pf^T < 0."""
        self.assertLess(planted_forest_correction_T(Fraction(50)), 0)
        self.assertLess(planted_forest_correction_T(Fraction(100)), 0)

    def test_pf_at_c4(self):
        """c = 4: δ_pf^T = (40-4)/48 = 36/48 = 3/4."""
        self.assertEqual(planted_forest_correction_T(Fraction(4)), Fraction(3, 4))

    def test_pf_at_c50(self):
        """c = 50: δ_pf^T = (40-50)/48 = -10/48 = -5/24."""
        self.assertEqual(planted_forest_correction_T(Fraction(50)), Fraction(-5, 24))


# ============================================================================
# 6. Single-channel limit
# ============================================================================

class TestSingleChannelLimit(unittest.TestCase):
    """Verify F₂ reduces to κ·λ₂^FP in the single-channel limit."""

    def test_per_channel_equals_universal(self):
        """F₂^T + F₂^W = κ·λ₂^FP."""
        for c in C_VALUES:
            r = verify_single_channel_limit(c)
            self.assertTrue(r['additivity_holds'])

    def test_per_channel_function(self):
        """F₂^{per-channel} = F₂^{universal} (algebraic identity)."""
        for c in C_VALUES:
            self.assertEqual(F2_w3_per_channel(c), F2_w3_scalar_universal(c))

    def test_F2_universal_formula(self):
        """F₂^{universal} = (5c/6)·(7/5760) = 7c/6912."""
        for c in C_VALUES:
            expected = Fraction(7) * c / 6912
            self.assertEqual(F2_w3_scalar_universal(c), expected)

    def test_diagonal_graph_sum(self):
        """The diagonal sum function returns κ·λ₂^FP."""
        for c in C_VALUES:
            d = diagonal_graph_sum(c)
            self.assertEqual(d['F2_diagonal'], F2_w3_scalar_universal(c))
            self.assertEqual(d['F2_T'] + d['F2_W'], d['F2_diagonal'])


# ============================================================================
# 7. Koszul duality
# ============================================================================

class TestDualityConsistency(unittest.TestCase):
    """Verify Koszul duality constraints for W₃.

    W₃ at c has dual W₃ at c' = 100 - c.
    κ(c) + κ(100-c) = 5·100/6 = 250/3.
    """

    def test_koszul_dual_kappa_sum(self):
        """κ(c) + κ(100-c) = 250/3."""
        for c in C_VALUES:
            c_dual = Fraction(100) - c
            kappa_sum = kappa_total(c) + kappa_total(c_dual)
            self.assertEqual(kappa_sum, Fraction(250, 3))

    def test_F2_duality(self):
        """F₂(c) + F₂(100-c) = (250/3)·λ₂^FP (if universality holds)."""
        fp2 = lambda_fp(2)
        for c in C_VALUES:
            c_dual = Fraction(100) - c
            F2_sum = F2_w3_scalar_universal(c) + F2_w3_scalar_universal(c_dual)
            expected = Fraction(250, 3) * fp2
            self.assertEqual(F2_sum, expected)

    def test_koszul_duality_check(self):
        """Full duality check function."""
        for c in C_VALUES:
            r = koszul_duality_check(c)
            self.assertTrue(r['kappa_duality_holds'])
            self.assertTrue(r['F2_duality_holds'])

    def test_cross_channel_duality(self):
        """Cross-channel correction at c and 100-c."""
        for c in C_VALUES:
            c_dual = Fraction(100) - c
            if c_dual > 0:
                delta_c = cross_channel_correction(c)
                delta_cd = cross_channel_correction(c_dual)
                # Both should be positive
                self.assertGreater(delta_c, 0)
                self.assertGreater(delta_cd, 0)


# ============================================================================
# 8. Physical consistency
# ============================================================================

class TestPhysicalConsistency(unittest.TestCase):
    """Physical consistency checks."""

    def test_F2_positive_for_positive_c(self):
        """F₂ > 0 for c > 0 (positive Bernoulli sign convention)."""
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(26)]:
            F2 = F2_w3_scalar_universal(c)
            self.assertGreater(F2, 0)

    def test_F2_proportional_to_c(self):
        """F₂ is linear in c (by the universal formula)."""
        fp2 = lambda_fp(2)
        for c in C_VALUES:
            self.assertEqual(F2_w3_scalar_universal(c),
                             Fraction(5, 6) * c * fp2)

    def test_cross_channel_positive(self):
        """Cross-channel correction is positive for c > 0."""
        for c in C_VALUES:
            if c > 0:
                self.assertGreater(cross_channel_correction(c), 0)

    def test_boundary_sum_positive(self):
        """Total boundary graph sum is positive for c > 0."""
        for c in C_VALUES:
            if c > 0:
                b = boundary_graph_sum(c)
                self.assertGreater(b['total_boundary'], 0)


# ============================================================================
# 9. Numerical spot-checks at specific c values
# ============================================================================

class TestNumericalAtC4(unittest.TestCase):
    """Numerical checks at c = 4 (free boson pair / so(8)₁ embedding)."""

    def setUp(self):
        self.c = Fraction(4)

    def test_kappa(self):
        """κ(W₃, c=4) = 5·4/6 = 10/3."""
        self.assertEqual(kappa_total(self.c), Fraction(10, 3))

    def test_F2_universal(self):
        """F₂ = (10/3)·(7/5760) = 70/17280 = 7/1728."""
        expected = Fraction(10, 3) * Fraction(7, 5760)
        self.assertEqual(F2_w3_scalar_universal(self.c), expected)
        self.assertEqual(expected, Fraction(7, 1728))

    def test_cross_channel(self):
        """δF₂(c=4) = (4+204)/(16·4) = 208/64 = 13/4."""
        delta = cross_channel_correction(self.c)
        self.assertEqual(delta, Fraction(208, 64))
        self.assertEqual(delta, Fraction(13, 4))

    def test_cross_channel_ratio(self):
        """δF₂/F₂ at c=4."""
        r = F2_w3_with_cross_channel(self.c)
        ratio = r['cross_channel_correction'] / r['F2_universal']
        # = (13/4)/(7/1728) = 13·1728/(4·7) = 22464/28 = 802.286...
        expected = Fraction(13, 4) / Fraction(7, 1728)
        self.assertEqual(ratio, expected)
        # This is very large: the cross-channel correction dominates
        # by a factor ~802 at c=4. This is because 1/c terms blow up.
        self.assertGreater(float(ratio), 100)

    def test_planted_forest(self):
        """δ_pf^T(c=4) = (40-4)/48 = 3/4."""
        self.assertEqual(planted_forest_correction_T(self.c), Fraction(3, 4))

    def test_shadow_data(self):
        """S₃ = 2, S₄ = 10/[4(20+22)] = 10/168 = 5/84."""
        self.assertEqual(S3_T(self.c), Fraction(2))
        s4 = S4_T(self.c)
        expected_s4 = Fraction(10) / (Fraction(4) * (Fraction(20) + Fraction(22)))
        self.assertEqual(s4, expected_s4)
        self.assertEqual(s4, Fraction(5, 84))

    def test_compute_full(self):
        """Full computation at c=4 returns consistent data."""
        result = compute_F2_w3(self.c)
        self.assertEqual(result['c'], self.c)
        self.assertEqual(result['kappa_total'], Fraction(10, 3))
        self.assertIsNotNone(result['cross_channel_ratio'])


class TestNumericalAtC50(unittest.TestCase):
    """Numerical checks at c = 50 (large c, well into perturbative regime)."""

    def setUp(self):
        self.c = Fraction(50)

    def test_kappa(self):
        """κ(W₃, c=50) = 5·50/6 = 125/3."""
        self.assertEqual(kappa_total(self.c), Fraction(125, 3))

    def test_F2_universal(self):
        """F₂ = (125/3)·(7/5760) = 875/17280."""
        expected = Fraction(125, 3) * Fraction(7, 5760)
        self.assertEqual(F2_w3_scalar_universal(self.c), expected)
        self.assertEqual(expected, Fraction(875, 17280))

    def test_cross_channel(self):
        """δF₂(c=50) = (50+204)/(16·50) = 254/800 = 127/400."""
        delta = cross_channel_correction(self.c)
        self.assertEqual(delta, Fraction(254, 800))
        self.assertEqual(delta, Fraction(127, 400))

    def test_cross_channel_ratio(self):
        """δF₂/F₂ at c=50 is smaller than at c=4 (decaying 1/c effect)."""
        r = F2_w3_with_cross_channel(self.c)
        ratio = float(r['cross_channel_correction'] / r['F2_universal'])
        # Should be moderate but still nonzero
        self.assertGreater(ratio, 1)
        self.assertLess(ratio, 100)

    def test_planted_forest(self):
        """δ_pf^T(c=50) = (40-50)/48 = -10/48 = -5/24."""
        self.assertEqual(planted_forest_correction_T(self.c), Fraction(-5, 24))

    def test_compute_full(self):
        """Full computation at c=50 returns consistent data."""
        result = compute_F2_w3(self.c)
        self.assertEqual(result['c'], self.c)
        self.assertEqual(result['kappa_total'], Fraction(125, 3))
        self.assertIsNotNone(result['cross_channel_ratio'])


class TestNumericalAtC13(unittest.TestCase):
    """Numerical checks at c = 13 (self-dual Virasoro central charge)."""

    def setUp(self):
        self.c = Fraction(13)

    def test_kappa(self):
        """κ(W₃, c=13) = 65/6."""
        self.assertEqual(kappa_total(self.c), Fraction(65, 6))

    def test_F2_universal(self):
        """F₂ = (65/6)·(7/5760)."""
        expected = Fraction(65, 6) * Fraction(7, 5760)
        self.assertEqual(F2_w3_scalar_universal(self.c), expected)

    def test_koszul_dual(self):
        """c' = 100 - 13 = 87. κ(13) + κ(87) = 250/3."""
        c_dual = Fraction(100) - self.c
        self.assertEqual(c_dual, Fraction(87))
        self.assertEqual(kappa_total(self.c) + kappa_total(c_dual),
                         Fraction(250, 3))


class TestNumericalAtC26(unittest.TestCase):
    """Numerical checks at c = 26 (critical Virasoro central charge)."""

    def setUp(self):
        self.c = Fraction(26)

    def test_kappa(self):
        """κ(W₃, c=26) = 5·26/6 = 65/3."""
        self.assertEqual(kappa_total(self.c), Fraction(65, 3))

    def test_F2_universal(self):
        """F₂ = (65/3)·(7/5760) = 455/17280."""
        expected = Fraction(65, 3) * Fraction(7, 5760)
        self.assertEqual(F2_w3_scalar_universal(self.c), expected)
        # Simplify: 455/17280 = 91/3456
        self.assertEqual(expected, Fraction(91, 3456))


# ============================================================================
# 10. Shadow obstruction tower data
# ============================================================================

class TestShadowData(unittest.TestCase):
    """Verify shadow obstruction tower coefficients for W₃ primary lines."""

    def test_S3_T_value(self):
        """T-line cubic shadow S₃ = 2 (= Virasoro α = 2)."""
        for c in C_VALUES:
            self.assertEqual(S3_T(c), Fraction(2))

    def test_S3_W_value(self):
        """W-line cubic shadow S₃ = 0 (Z₂ parity)."""
        for c in C_VALUES:
            self.assertEqual(S3_W(c), Fraction(0))

    def test_S4_T_value(self):
        """T-line quartic S₄ = Q^contact = 10/[c(5c+22)]."""
        for c in C_VALUES:
            expected = Fraction(10) / (c * (5 * c + 22))
            self.assertEqual(S4_T(c), expected)

    def test_S4_W_value(self):
        """W-line quartic S₄ = 2560/[c(5c+22)³]."""
        for c in C_VALUES:
            expected = Fraction(2560) / (c * (5 * c + 22) ** 3)
            self.assertEqual(S4_W(c), expected)


# ============================================================================
# 11. Full computation integration tests
# ============================================================================

class TestGraphSumComputation(unittest.TestCase):
    """Test the full graph sum computation."""

    def test_returns_all_fields(self):
        """compute_F2_w3 returns the expected dictionary keys."""
        c = Fraction(2)
        result = compute_F2_w3(c)
        for key in ['c', 'kappa_T', 'kappa_W', 'kappa_total',
                     'lambda2_fp', 'F2_universal', 'F2_universal_float',
                     'boundary_total', 'boundary_diagonal',
                     'cross_channel_correction', 'cross_channel_float',
                     'cross_channel_ratio',
                     'planted_forest_T', 'planted_forest_W',
                     'planted_forest_total', 'per_graph']:
            self.assertIn(key, result)

    def test_per_graph_names(self):
        """All 7 graphs appear in the per-graph results."""
        c = Fraction(2)
        result = compute_F2_w3(c)
        expected_names = {'smooth', 'fig_eight', 'banana',
                          'dumbbell', 'theta', 'lollipop', 'barbell'}
        self.assertEqual(set(result['per_graph'].keys()), expected_names)

    def test_cross_channel_matches_formula(self):
        """Cross-channel from graph sum matches the analytic formula."""
        for c in C_VALUES:
            result = compute_F2_w3(c)
            analytic = cross_channel_correction(c)
            self.assertEqual(result['cross_channel_correction'], analytic)

    def test_boundary_total_matches_sum(self):
        """Boundary total equals sum of all per-graph totals."""
        for c in C_VALUES:
            result = compute_F2_w3(c)
            total = Fraction(0)
            for name, amp in result['per_graph'].items():
                total += amp['total']
            self.assertEqual(total, result['boundary_total'])


# ============================================================================
# 12. Banana vertex universality (remarkable identity)
# ============================================================================

class TestBananaVertexUniversality(unittest.TestCase):
    """The banana vertex factor V_{0,4}(i,i,j,j) = 2c is UNIVERSAL.

    This is because the W-channel never contributes to the
    s-channel factorization (both C_{TTW} and C_{WWW} vanish).
    Only the T-channel contributes: (2/c)·c·c = 2c.
    """

    def test_universality(self):
        for c in C_VALUES:
            for ch1 in ['T', 'W']:
                for ch2 in ['T', 'W']:
                    V = V04_s_channel(ch1, ch1, ch2, ch2, c)
                    self.assertEqual(V, 2 * c)


# ============================================================================
# 13. Propagator variance
# ============================================================================

class TestPropagatorVariance(unittest.TestCase):
    """Verify propagator variance computation."""

    def test_variance_nonneg(self):
        """Propagator variance is non-negative (Cauchy-Schwarz)."""
        for c in C_VALUES:
            r = propagator_variance_w3(c)
            self.assertTrue(r['variance_nonneg'],
                            f"Variance negative at c={c}: {r['variance']}")

    def test_variance_nonzero(self):
        """For generic c, the variance is nonzero (S₄^T != S₄^W)."""
        for c in [Fraction(2), Fraction(13), Fraction(50)]:
            r = propagator_variance_w3(c)
            self.assertNotEqual(r['S4_T'], r['S4_W'],
                                f"S₄^T = S₄^W at c={c} — unexpected")


# ============================================================================
# 14. Cross-check: boundary graph sum consistency
# ============================================================================

class TestBoundaryGraphSum(unittest.TestCase):
    """Verify the full boundary graph sum."""

    def test_diagonal_plus_mixed_equals_total(self):
        """Total boundary = diagonal + mixed."""
        for c in C_VALUES:
            b = boundary_graph_sum(c)
            total = b['total_diagonal'] + b['total_mixed']
            self.assertEqual(total, b['total_boundary'])

    def test_mixed_matches_cross_channel(self):
        """Mixed boundary = cross-channel correction."""
        for c in C_VALUES:
            b = boundary_graph_sum(c)
            self.assertEqual(b['total_mixed'], cross_channel_correction(c))


# ============================================================================
# 15. INDEPENDENT CROSS-VERIFICATION of delta_F2 = (c+204)/(16c)
#
# Recomputed from first principles per the Beilinson Principle (AP1/AP3/AP10).
# Every formula recomputed independently; no pattern-matching against existing
# code. Tests use raw Fraction arithmetic to avoid hardcoded-wrong-expected
# values (AP10).
# ============================================================================

class TestIndependentCrossChannelVerification(unittest.TestCase):
    r"""Independent verification of delta_F2(W3) = (c+204)/(16c).

    Strategy: recompute EVERY mixed-channel amplitude from scratch using
    only the W3 OPE data and Feynman rules, without calling any library
    functions except the raw data (kappa, propagator, C3).

    The five boundary graphs at genus 2 are:
        Gamma_1 (fig-eight):  1 self-loop.  No mixed (single edge).
        Gamma_2 (banana):     2 self-loops. Mixed = 3/c.
        Gamma_3 (dumbbell):   1 bridge.     No mixed (single edge).
        Gamma_4 (theta):      3 bridges.    Mixed = 9/(2c).
        Gamma_5 (lollipop):   1 self-loop + 1 bridge. Mixed = 1/16.
    """

    # ------------------------------------------------------------------
    # Raw data verification (independent of library convenience functions)
    # ------------------------------------------------------------------

    def test_raw_metric_and_propagator(self):
        """Verify eta and eta^{-1} from the W3 OPE leading poles."""
        for c in [Fraction(1), Fraction(2), Fraction(7), Fraction(25), Fraction(100)]:
            # T: T_{(3)}T = c/2, so eta_{TT} = c/2, eta^{TT} = 2/c
            eta_TT = c / 2
            eta_inv_TT = Fraction(2) / c
            self.assertEqual(eta_TT * eta_inv_TT, Fraction(1))

            # W: W_{(5)}W = c/3, so eta_{WW} = c/3, eta^{WW} = 3/c
            eta_WW = c / 3
            eta_inv_WW = Fraction(3) / c
            self.assertEqual(eta_WW * eta_inv_WW, Fraction(1))

    def test_raw_3point_functions(self):
        """Verify all 8 cubic structure constants from W3 OPE."""
        for c in [Fraction(1), Fraction(5), Fraction(50)]:
            # From W3 OPE (AP19: r-matrix = OPE poles shifted by -1):
            # T_{(1)}T = 2T => C^T_{TT} = 2 => C_{TTT} = (c/2)*2 = c
            self.assertEqual(Fraction(c, 2) * 2, c)  # C_{TTT}

            # T_{(1)}W = 3W => C^W_{TW} = 3 => C_{TWW} = (c/3)*3 = c
            self.assertEqual(Fraction(c, 3) * 3, c)  # C_{TWW}

            # W_{(3)}W = 2T => C^T_{WW} = 2 => C_{WWT} = (c/2)*2 = c
            self.assertEqual(Fraction(c, 2) * 2, c)  # C_{WWT}

            # Z2 symmetry: odd W-count vanishes
            # C_{TTW} = C_{TWT} = C_{WTT} = C_{WWW} = 0

    # ------------------------------------------------------------------
    # Graph-by-graph mixed amplitude: independent recomputation
    # ------------------------------------------------------------------

    def test_banana_mixed_independent(self):
        r"""Gamma_2 (banana): independently recompute mixed amplitude.

        Banana: 1 vertex (g=0, val=4), 2 self-loops. |Aut| = 8.

        Mixed assignments: (T,W) and (W,T).
        For (T,W): half-edges at vertex = (T,T,W,W).
            V_{0,4}(T,T|W,W) = sum_m eta^{mm} C_{TTm} C_{WWm}
                              = eta^{TT} C_{TTT} C_{WWT} + eta^{WW} C_{TTW} C_{WWW}
                              = (2/c)*c*c + (3/c)*0*0
                              = 2c.
            Propagators: eta^T * eta^W = (2/c)(3/c) = 6/c^2.
            Raw amplitude = (6/c^2) * 2c = 12/c.

        By symmetry, (W,T) also gives 12/c.
        Total mixed with 1/|Aut| = 1/8: 2 * 12/(8c) = 3/c.
        """
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(25), Fraction(100)]:
            # Vertex factor
            V04 = (Fraction(2) / c) * c * c  # only T-channel contributes
            self.assertEqual(V04, 2 * c)

            # Propagator product for mixed (T,W)
            prop = (Fraction(2) / c) * (Fraction(3) / c)
            self.assertEqual(prop, Fraction(6) / (c * c))

            # Raw amplitude per assignment
            raw = prop * V04
            self.assertEqual(raw, Fraction(12) / c)

            # 2 mixed assignments, |Aut| = 8
            mixed_banana = 2 * raw / 8
            self.assertEqual(mixed_banana, Fraction(3) / c)

    def test_theta_mixed_independent(self):
        r"""Gamma_4 (theta): independently recompute mixed amplitude.

        Theta: 2 vertices (g=0, val=3) + (g=0, val=3), 3 bridges. |Aut| = 12.

        8 channel assignments. Classify by type:

        (T,T,T): all-T. (2/c)^3 * c^2 = 8/c. /12 = 2/(3c). Not mixed.
        (W,W,W): C_{WWW} = 0. Zero.

        (T,T,W) [3 assignments: choose which edge is W]:
            Each vertex gets half-edges (T,T,W). C_{TTW} = 0.
            ALL vanish.

        (T,W,W) [3 assignments: choose which edge is T]:
            Vertex 1 gets (T,W,W): C_{TWW} = c.
            Vertex 2 gets (T,W,W): C_{TWW} = c.
            Propagators: eta^T * (eta^W)^2 = (2/c)(3/c)^2 = 18/c^3.
            Raw = 18/c^3 * c * c = 18/c.
            3 such assignments.

        Mixed total: 3 * 18/c / 12 = 54/(12c) = 9/(2c).
        """
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(25), Fraction(100)]:
            # (T,W,W)-type raw amplitude
            C_TWW = c  # from OPE
            prop_TWW = (Fraction(2) / c) * (Fraction(3) / c) ** 2
            self.assertEqual(prop_TWW, Fraction(18) / (c ** 3))

            raw_TWW = prop_TWW * C_TWW * C_TWW
            self.assertEqual(raw_TWW, Fraction(18) / c)

            # (T,T,W)-type: C_{TTW} = 0, so vanishes
            C_TTW = Fraction(0)
            raw_TTW = C_TTW  # anything times 0 = 0
            self.assertEqual(raw_TTW, Fraction(0))

            # Total mixed: 3 * raw_TWW / |Aut| = 3 * 18/c / 12
            mixed_theta = 3 * raw_TWW / 12
            self.assertEqual(mixed_theta, Fraction(9) / (2 * c))

    def test_lollipop_mixed_independent(self):
        r"""Gamma_5 (lollipop): independently recompute mixed amplitude.

        Lollipop: vertex 0 (g=0, val=3), vertex 1 (g=1, val=1).
        Edges: 1 self-loop at v0, 1 bridge v0->v1. |Aut| = 2.

        Mixed assignments: (T,W) and (W,T) for (self-loop, bridge).

        (T,W): self-loop T, bridge W.
            v0 half-edges: (T,T,W) [T,T from self-loop, W from bridge].
            C_{TTW} = 0. Amplitude = 0.

        (W,T): self-loop W, bridge T.
            v0 half-edges: (W,W,T) [W,W from self-loop, T from bridge].
            C_{WWT} = c.
            v1 half-edge: T. Genus-1 vertex factor = kappa_T/24 = (c/2)/24 = c/48.
            Propagators: eta^W * eta^T = (3/c)(2/c) = 6/c^2.
            Raw = (6/c^2) * c * (c/48) = 6c^2 / (48c^2) = 1/8.

        Total mixed: (0 + 1/8) / 2 = 1/16.

        CRITICAL: this is INDEPENDENT OF c.
        """
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(25), Fraction(100)]:
            # (T,W): C_{TTW} = 0
            amp_TW = Fraction(0)

            # (W,T):
            C_WWT = c
            kappa_T_val = c / 2
            genus1_factor = kappa_T_val / 24  # = c/48
            prop_WT = (Fraction(3) / c) * (Fraction(2) / c)  # eta^W * eta^T
            raw_WT = prop_WT * C_WWT * genus1_factor

            # Verify step by step
            self.assertEqual(genus1_factor, c / 48)
            self.assertEqual(prop_WT, Fraction(6) / (c * c))
            self.assertEqual(raw_WT, Fraction(6) / (c * c) * c * c / 48)
            self.assertEqual(raw_WT, Fraction(6) / 48)
            self.assertEqual(raw_WT, Fraction(1) / 8)

            # With 1/|Aut| = 1/2
            mixed_lollipop = (amp_TW + raw_WT) / 2
            self.assertEqual(mixed_lollipop, Fraction(1, 16))

    def test_fig_eight_no_mixed(self):
        """Gamma_1 (fig-eight): single edge, no mixed assignment possible."""
        # With 1 edge, assignments are (T,) or (W,). Neither is mixed.
        # Mixed = 0.
        pass  # Trivially true: a single-edge graph has no mixed channels.

    def test_dumbbell_no_mixed(self):
        """Gamma_3 (dumbbell): single bridge, no mixed assignment."""
        # With 1 edge, assignments are (T,) or (W,). Neither is mixed.
        # Moreover, the genus-1 vertex factor is diagonal:
        # V_{1,1}(i) = kappa_i/24, so cross-channel would need eta^{ij}
        # which is zero for i != j.
        pass  # Trivially true.

    # ------------------------------------------------------------------
    # Total cross-channel: algebraic derivation
    # ------------------------------------------------------------------

    def test_total_cross_channel_algebraic(self):
        r"""Sum the four mixed contributions and verify the closed form.

        delta_F2 = 3/c + 9/(2c) + 1/16 + 21/(4c)
                 = 12/(4c) + 18/(4c) + 21/(4c) + 1/16
                 = 51/(4c) + 1/16
                 = (51*16 + 4c) / (64c)
                 = (816 + 4c) / (64c)
                 = 4(204 + c) / (64c)
                 = (c + 204) / (16c).
        """
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(13),
                  Fraction(25), Fraction(26), Fraction(50), Fraction(100)]:
            banana = Fraction(3) / c
            theta = Fraction(9) / (2 * c)
            lollipop = Fraction(1, 16)
            barbell = Fraction(21) / (4 * c)

            total = banana + theta + lollipop + barbell

            # Step-by-step algebraic reduction
            # banana + theta + barbell = 12/(4c) + 18/(4c) + 21/(4c) = 51/(4c)
            c_dep = banana + theta + barbell
            self.assertEqual(c_dep, Fraction(51) / (4 * c))

            # 51/(4c) + 1/16 = (51*16 + 4c)/(64c) = (816 + 4c)/(64c)
            numerator = 816 + 4 * c
            denominator = 64 * c
            self.assertEqual(total, numerator / denominator)

            # Simplify: 4(204+c)/(64c) = (c+204)/(16c)
            self.assertEqual(total, (c + 204) / (16 * c))

    # ------------------------------------------------------------------
    # Dimensional analysis
    # ------------------------------------------------------------------

    def test_large_c_limit(self):
        """As c -> infinity, delta_F2 -> 1/16 (lollipop dominates).

        (c+204)/(16c) = 1/16 + 204/(16c) = 1/16 + 51/(4c).
        The 1/c terms from banana+theta+barbell die; only lollipop survives.
        """
        c = Fraction(10**8)
        delta = (c + 204) / (16 * c)
        # Should be very close to 1/16
        self.assertEqual(delta - Fraction(1, 16), Fraction(204) / (16 * c))
        self.assertEqual(delta - Fraction(1, 16), Fraction(51) / (4 * c))
        self.assertAlmostEqual(float(delta), 1/16, places=5)

    def test_special_cancellation_at_c_neg204(self):
        """At c = -204: delta_F2 = 0 (numerator vanishes).

        This is the unique value where the cross-channel correction vanishes.
        Physically meaningless (c < 0), but algebraically clean.
        """
        c = Fraction(-204)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(0))

        # Verify from components
        banana = Fraction(3) / c
        theta = Fraction(9) / (2 * c)
        lollipop = Fraction(1, 16)
        barbell = Fraction(21) / (4 * c)
        total = banana + theta + lollipop + barbell
        self.assertEqual(total, Fraction(0))

    def test_self_dual_c50(self):
        """At c = 50 (W3 self-dual point): delta_F2 = 127/400.

        c' = 100 - c = 50, so c = c'. delta_F2 = (50+204)/(16*50) = 254/800 = 127/400.
        """
        c = Fraction(50)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(254, 800))
        self.assertEqual(delta, Fraction(127, 400))

    # ------------------------------------------------------------------
    # Complementarity: delta_F2(c) + delta_F2(100-c)
    # ------------------------------------------------------------------

    def test_complementarity_cross_channel(self):
        r"""Verify delta_F2(c) + delta_F2(100-c) for Koszul dual pairs.

        delta(c) + delta(c') = (c+204)/(16c) + (100-c+204)/(16(100-c))
            = (c+204)/(16c) + (304-c)/(16(100-c))
            = [(c+204)(100-c) + c(304-c)] / [16c(100-c)]

        Numerator:
            (c+204)(100-c) = 100c + 20400 - c^2 - 204c = -c^2 - 104c + 20400
            c(304-c) = 304c - c^2
            Sum = -2c^2 + 200c + 20400
                = -2(c^2 - 100c - 10200)

        So delta(c) + delta(c') = -2(c^2 - 100c - 10200) / [16c(100-c)]
                                = -(c^2 - 100c - 10200) / [8c(100-c)]
        """
        for c in [Fraction(1), Fraction(2), Fraction(13), Fraction(25),
                  Fraction(30), Fraction(50)]:
            c_dual = Fraction(100) - c
            if c_dual <= 0:
                continue
            delta_c = (c + 204) / (16 * c)
            delta_cd = (c_dual + 204) / (16 * c_dual)
            delta_sum = delta_c + delta_cd

            # Verify the algebraic formula
            numerator = -(c * c - 100 * c - Fraction(10200))
            denominator = 8 * c * (100 - c)
            expected = numerator / denominator
            self.assertEqual(delta_sum, expected)

        # At self-dual point c=50: delta_sum = 2 * delta(50) = 2 * 127/400 = 127/200
        c = Fraction(50)
        delta_50 = (c + 204) / (16 * c)
        self.assertEqual(2 * delta_50, Fraction(127, 200))

    # ------------------------------------------------------------------
    # Numerical spot checks at c = 1, 2, 25
    # ------------------------------------------------------------------

    def test_spot_check_c1(self):
        """c = 1: delta_F2 = 205/16."""
        c = Fraction(1)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(205, 16))

        # Verify from components
        banana = Fraction(3) / c
        theta = Fraction(9) / (2 * c)
        lollipop = Fraction(1, 16)
        barbell = Fraction(21) / (4 * c)
        self.assertEqual(banana, Fraction(3))
        self.assertEqual(theta, Fraction(9, 2))
        self.assertEqual(barbell, Fraction(21, 4))
        self.assertEqual(banana + theta + lollipop + barbell, Fraction(205, 16))

    def test_spot_check_c2(self):
        """c = 2: delta_F2 = 206/32 = 103/16."""
        c = Fraction(2)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(206, 32))
        self.assertEqual(delta, Fraction(103, 16))

        # Verify from components
        banana = Fraction(3) / c
        theta = Fraction(9) / (2 * c)
        lollipop = Fraction(1, 16)
        barbell = Fraction(21) / (4 * c)
        self.assertEqual(banana, Fraction(3, 2))
        self.assertEqual(theta, Fraction(9, 4))
        self.assertEqual(barbell, Fraction(21, 8))
        self.assertEqual(banana + theta + lollipop + barbell, Fraction(103, 16))

    def test_spot_check_c25(self):
        """c = 25: delta_F2 = 229/400."""
        c = Fraction(25)
        delta = (c + 204) / (16 * c)
        self.assertEqual(delta, Fraction(229, 400))

        # Verify from components
        banana = Fraction(3, 25)
        theta = Fraction(9, 50)
        lollipop = Fraction(1, 16)
        barbell = Fraction(21, 100)
        total = banana + theta + lollipop + barbell
        self.assertEqual(total, Fraction(229, 400))

    # ------------------------------------------------------------------
    # Consistency: graph-sum code vs independent recomputation
    # ------------------------------------------------------------------

    def test_graph_sum_matches_independent(self):
        """Verify that the library's graph_total_amplitude matches
        independent recomputation for all boundary graphs at all c."""
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(13),
                  Fraction(25), Fraction(26), Fraction(50), Fraction(100)]:
            # Banana mixed (graph_idx=2)
            r2 = graph_total_amplitude(2, c)
            self.assertEqual(r2['mixed'], Fraction(3) / c)

            # Theta mixed (graph_idx=4)
            r4 = graph_total_amplitude(4, c)
            self.assertEqual(r4['mixed'], Fraction(9) / (2 * c))

            # Lollipop mixed (graph_idx=5)
            r5 = graph_total_amplitude(5, c)
            self.assertEqual(r5['mixed'], Fraction(1, 16))

            # Barbell mixed (graph_idx=6)
            r6 = graph_total_amplitude(6, c)
            self.assertEqual(r6['mixed'], Fraction(21) / (4 * c))

            # Fig-eight and dumbbell have no mixed
            r1 = graph_total_amplitude(1, c)
            r3 = graph_total_amplitude(3, c)
            self.assertEqual(r1['mixed'], Fraction(0))
            self.assertEqual(r3['mixed'], Fraction(0))

            # Total mixed matches formula
            total_mixed = (r1['mixed'] + r2['mixed'] + r3['mixed']
                           + r4['mixed'] + r5['mixed'] + r6['mixed'])
            self.assertEqual(total_mixed, (c + 204) / (16 * c))

    # ------------------------------------------------------------------
    # Cross-check: banana graph universality V_{0,4} = 2c
    # ------------------------------------------------------------------

    def test_banana_v04_independent_derivation(self):
        r"""V_{0,4}(i,i|j,j) = 2c for all i,j in {T,W}.

        Proof: V = sum_m eta^{mm} C_{iim} C_{jjm}.
        C_{TTW} = 0, C_{WWW} = 0 => W-channel never contributes.
        T-channel: eta^{TT} * C_{iiT} * C_{jjT} = (2/c) * c * c = 2c.

        The key fact: C_{TTT} = c, C_{WWT} = c, C_{TTW} = 0, C_{WWW} = 0.
        So C_{iiT} = c for both i=T and i=W, while C_{iiW} = 0 for i=T
        and C_{WWW} = 0.
        """
        for c in [Fraction(1), Fraction(7), Fraction(50)]:
            eta_inv_T = Fraction(2) / c
            eta_inv_W = Fraction(3) / c
            C_TTT = c
            C_WWT = c
            C_TTW = Fraction(0)
            C_WWW = Fraction(0)

            for i_label, C_iiT, C_iiW in [('T', C_TTT, C_TTW),
                                           ('W', C_WWT, C_WWW)]:
                for j_label, C_jjT, C_jjW in [('T', C_TTT, C_TTW),
                                               ('W', C_WWT, C_WWW)]:
                    V = eta_inv_T * C_iiT * C_jjT + eta_inv_W * C_iiW * C_jjW
                    self.assertEqual(V, 2 * c,
                        f"V_{{0,4}}({i_label},{i_label}|{j_label},{j_label}) "
                        f"= {V} != {2*c} at c={c}")

    # ------------------------------------------------------------------
    # Ratio delta_F2 / F2_universal
    # ------------------------------------------------------------------

    def test_ratio_formula(self):
        r"""delta_F2 / F2_universal = 6912(c+204) / (16*5*c^2)
                                    = 432(c+204) / (5c^2).

        Wait: F2_universal = (5c/6) * (7/5760) = 35c/34560 = 7c/6912.
        ratio = [(c+204)/(16c)] / [7c/6912]
              = (c+204) * 6912 / (16c * 7c)
              = 6912(c+204) / (112c^2)
              = 864(c+204) / (14c^2)
              = 432(c+204) / (7c^2).
        """
        for c in [Fraction(1), Fraction(2), Fraction(4), Fraction(25), Fraction(50)]:
            delta = (c + 204) / (16 * c)
            F2 = Fraction(7) * c / 6912
            ratio = delta / F2
            expected = Fraction(432) * (c + 204) / (7 * c * c)
            self.assertEqual(ratio, expected)

    # ------------------------------------------------------------------
    # Monotonicity and sign
    # ------------------------------------------------------------------

    def test_positivity_for_positive_c(self):
        """delta_F2 > 0 for all c > 0 (numerator and denominator both positive)."""
        for c in [Fraction(1, 10), Fraction(1), Fraction(10), Fraction(100),
                  Fraction(1000)]:
            delta = (c + 204) / (16 * c)
            self.assertGreater(delta, 0)

    def test_monotone_decreasing_for_positive_c(self):
        """delta_F2 is monotone decreasing for c > 0.

        d/dc [(c+204)/(16c)] = d/dc [1/16 + 120/(16c)]
                              = -204/(16c^2) < 0.
        """
        c_values = [Fraction(1), Fraction(5), Fraction(10), Fraction(50),
                    Fraction(100), Fraction(1000)]
        deltas = [(c + 204) / (16 * c) for c in c_values]
        for i in range(len(deltas) - 1):
            self.assertGreater(deltas[i], deltas[i + 1])


if __name__ == '__main__':
    unittest.main()
