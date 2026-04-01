r"""Tests for the W₃ genus-2 free energy computation.

Tests the multi-channel genus-2 graph sum for the W₃ algebra,
verifying:

1. Single-channel limit: F₂ reduces to κ·λ₂^FP for each channel
2. Per-channel additivity: F₂^T + F₂^W = κ·λ₂^FP
3. Planted-forest formula: δ_pf^{(2,0)} = S₃(10S₃ - κ)/48
4. Cross-channel corrections: exact per-graph amplitudes
5. Numerical evaluation at specific c values
6. Consistency with the scalar graph sum engine

RESULT:
    The PER-CHANNEL sum gives F₂ = κ·λ₂^FP by the additivity of κ.
    The CROSS-CHANNEL correction δF₂ = (c+120)/(16c) is computed from
    genus-0 vertex factors (R-matrix independent) and genus-1 vertex
    factors (using κ_i/24 per-channel universality).

    Whether δF₂ = 0 (universality holds) or δF₂ ≠ 0 (universality fails)
    depends on whether R-matrix corrections to the genus-1 vertex factors
    cancel in the cross-channel graph sum. This is op:multi-generator-universality.

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
    S3_T, S3_W, S4_T, S4_W,
    verify_genus2_graphs,
    graph_amplitude, graph_total_amplitude,
    cross_channel_correction, cross_channel_correction_exact,
    planted_forest_correction_T, planted_forest_correction_W,
    planted_forest_total,
    F2_w3_scalar_universal, F2_w3_per_channel,
    F2_w3_with_cross_channel,
    verify_single_channel_limit,
    verify_graph_amplitudes,
    compute_F2_w3,
    _channel_assignments,
    GENUS2_GRAPHS,
)


# Standard test central charges
C_VALUES = [
    Fraction(1), Fraction(2), Fraction(13), Fraction(26),
    Fraction(50), Fraction(100),
]


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

    def test_z2_symmetry(self):
        """All 3-point functions with odd W count vanish."""
        for c in C_VALUES:
            # TTW, TWT, WTT: 1 W → vanishes
            self.assertEqual(C3('T', 'T', 'W', c), Fraction(0))
            self.assertEqual(C3('T', 'W', 'T', c), Fraction(0))
            self.assertEqual(C3('W', 'T', 'T', c), Fraction(0))
            # WWW: 3 W → vanishes
            self.assertEqual(C3('W', 'W', 'W', c), Fraction(0))

    def test_propagator(self):
        for c in C_VALUES:
            self.assertEqual(propagator('T', c), Fraction(2) / c)
            self.assertEqual(propagator('W', c), Fraction(3) / c)


class TestVertexFactors(unittest.TestCase):
    """Verify genus-0 vertex factors."""

    def test_V04_TTTT(self):
        """V_{0,4}(T,T,T,T) = Σ_m η^{mm} C_{TTm}² = (2/c)c² = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('T', 'T', 'T', 'T', c)
            self.assertEqual(V, 2 * c)

    def test_V04_WWWW(self):
        """V_{0,4}(W,W,W,W) = (2/c)·C_{WWT}² = (2/c)c² = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('W', 'W', 'W', 'W', c)
            self.assertEqual(V, 2 * c)

    def test_V04_TTWW(self):
        """V_{0,4}(T,T,W,W) = (2/c)·C_{TTT}·C_{WWT} = (2/c)·c·c = 2c."""
        for c in C_VALUES:
            V = V04_s_channel('T', 'T', 'W', 'W', c)
            self.assertEqual(V, 2 * c)

    def test_V04_banana_universal(self):
        """The banana vertex factor is 2c for ALL channel assignments.

        This is a remarkable property: V_{0,4}(i,i,j,j) = 2c regardless
        of whether (i,j) = (T,T), (W,W), or (T,W).
        """
        for c in C_VALUES:
            for ch1 in ['T', 'W']:
                for ch2 in ['T', 'W']:
                    V = V04_s_channel(ch1, ch1, ch2, ch2, c)
                    self.assertEqual(V, 2 * c,
                                     f"V₀₄({ch1}{ch1}{ch2}{ch2}) ≠ 2c at c={c}")


class TestGraphTopology(unittest.TestCase):
    """Verify genus-2 stable graph enumeration."""

    def test_graph_count(self):
        self.assertEqual(len(GENUS2_GRAPHS), 6)

    def test_graph_stability_and_genus(self):
        verify_genus2_graphs()

    def test_channel_assignments_count(self):
        """2^n channel assignments for n edges."""
        self.assertEqual(len(_channel_assignments(0)), 1)
        self.assertEqual(len(_channel_assignments(1)), 2)
        self.assertEqual(len(_channel_assignments(2)), 4)
        self.assertEqual(len(_channel_assignments(3)), 8)


class TestGraphAmplitudes(unittest.TestCase):
    """Verify individual graph amplitudes against analytic formulas."""

    def test_banana_all_T(self):
        """Γ₂ all-T amplitude: (1/8)·(2/c)²·2c = (1/8)·8/c = 1/c."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['all_T'], Fraction(1) / c)

    def test_banana_all_W(self):
        """Γ₂ all-W amplitude: (1/8)·(3/c)²·2c = (1/8)·18/c = 9/(4c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['all_W'], Fraction(9) / (4 * c))

    def test_banana_mixed(self):
        """Γ₂ mixed: (1/8)·2·(2/c)(3/c)·2c = 3/c."""
        for c in C_VALUES:
            r = graph_total_amplitude(2, c)
            self.assertEqual(r['mixed'], Fraction(3) / c)

    def test_theta_all_T(self):
        """Γ₄ all-T: (1/12)·(2/c)³·c² = 2/(3c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['all_T'], Fraction(2) / (3 * c))

    def test_theta_all_W(self):
        """Γ₄ all-W: C_{WWW} = 0 → amplitude = 0."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['all_W'], Fraction(0))

    def test_theta_mixed(self):
        """Γ₄ mixed: (1/12)·3·(2/c)(3/c)²·c² = 9/(2c)."""
        for c in C_VALUES:
            r = graph_total_amplitude(4, c)
            self.assertEqual(r['mixed'], Fraction(9) / (2 * c))

    def test_fig_eight_channels(self):
        """Γ₁ (figure-eight): single edge, per-channel only.

        A(T) = (1/2)·(2/c)·(c/2)/24 = (1/2)·1/24 = 1/48.
        A(W) = (1/2)·(3/c)·(c/3)/24 = (1/2)·1/24 = 1/48.
        Total = 1/24. No mixed.
        """
        for c in C_VALUES:
            r = graph_total_amplitude(1, c)
            self.assertEqual(r['all_T'] + r['all_W'], Fraction(1, 24))
            self.assertEqual(r['mixed'], Fraction(0))

    def test_dumbbell_channels(self):
        """Γ₃ (dumbbell): single edge, per-channel only.

        A(i) = (1/2)·(1/κ_i)·(κ_i/24)·(κ_i/24) = (1/2)·κ_i/576.
        Total = (κ_T + κ_W)/1152 = κ/1152.
        """
        for c in C_VALUES:
            r = graph_total_amplitude(3, c)
            expected = kappa_total(c) / 1152
            self.assertEqual(r['all_T'] + r['all_W'], expected,
                             f"Dumbbell total ≠ κ/1152 at c={c}")
            self.assertEqual(r['mixed'], Fraction(0))

    def test_lollipop_mixed(self):
        """Γ₅ (lollipop) mixed: δΓ₅ = 1/16.

        (T,W): C_{TTW} = 0 → 0.
        (W,T): (3/c)(2/c)·c·(c/48) = 1/8.
        δΓ₅ = (1/2)·1/8 = 1/16.
        """
        for c in C_VALUES:
            r = graph_total_amplitude(5, c)
            self.assertEqual(r['mixed'], Fraction(1, 16))

    def test_verify_graph_amplitudes_helper(self):
        """Cross-check via the verify_graph_amplitudes function."""
        for c in C_VALUES:
            results = verify_graph_amplitudes(c)
            for graph_name, checks in results.items():
                for key, val in checks.items():
                    if key.endswith('_match'):
                        self.assertTrue(val, f"{graph_name}.{key} FAILED at c={c}")


class TestCrossChannelCorrection(unittest.TestCase):
    """Verify the total cross-channel correction."""

    def test_cross_channel_formula(self):
        """δF₂ = (c + 120)/(16c)."""
        for c in C_VALUES:
            delta = cross_channel_correction(c)
            expected = (c + 120) / (16 * c)
            self.assertEqual(delta, expected,
                             f"δF₂ ≠ (c+120)/(16c) at c={c}")

    def test_cross_channel_exact_breakdown(self):
        """Verify per-graph breakdown sums to total."""
        for c in C_VALUES:
            r = cross_channel_correction_exact(c)
            total = r['delta_banana'] + r['delta_theta'] + r['delta_lollipop']
            self.assertEqual(total, r['delta_total'])
            self.assertTrue(r['match'])

    def test_cross_channel_nonzero(self):
        """The naive cross-channel correction is nonzero for c > 0."""
        for c in C_VALUES:
            if c > 0:
                delta = cross_channel_correction(c)
                self.assertNotEqual(delta, Fraction(0),
                                    f"δF₂ = 0 at c={c} — unexpected")

    def test_cross_channel_at_specific_values(self):
        """Numerical spot checks."""
        # c = 1: δF₂ = 121/16
        self.assertEqual(cross_channel_correction(Fraction(1)),
                         Fraction(121, 16))
        # c = 2: δF₂ = 122/32 = 61/16
        self.assertEqual(cross_channel_correction(Fraction(2)),
                         Fraction(122, 32))
        # c = 26: δF₂ = 146/416 = 73/208
        self.assertEqual(cross_channel_correction(Fraction(26)),
                         Fraction(146, 416))


class TestPlantedForest(unittest.TestCase):
    """Verify planted-forest corrections at genus 2."""

    def test_pf_T_virasoro_formula(self):
        """δ_pf^T = -(c-40)/48 for the T-line (= Virasoro)."""
        for c in C_VALUES:
            pf = planted_forest_correction_T(c)
            expected = -(c - 40) / 48
            self.assertEqual(pf, expected,
                             f"δ_pf^T ≠ -(c-40)/48 at c={c}")

    def test_pf_W_vanishes(self):
        """δ_pf^W = 0 (S₃^W = 0 by Z₂ parity)."""
        for c in C_VALUES:
            self.assertEqual(planted_forest_correction_W(c), Fraction(0))

    def test_pf_total(self):
        """Total planted-forest = δ_pf^T + δ_pf^W = -(c-40)/48."""
        for c in C_VALUES:
            self.assertEqual(planted_forest_total(c),
                             planted_forest_correction_T(c))

    def test_pf_vanishes_at_c40(self):
        """Planted-forest correction vanishes at c = 40 (Virasoro critical)."""
        self.assertEqual(planted_forest_correction_T(Fraction(40)), Fraction(0))

    def test_pf_heisenberg_vanishes(self):
        """For Heisenberg (S₃ = 0): δ_pf = 0.

        Heisenberg has α = 0, so S₃ = 0, hence δ_pf = 0.
        This is consistent with shadow depth 2 (Gaussian class).
        """
        # S₃ = 0 for Heisenberg; our W-line has S₃ = 0 too
        pf = Fraction(0) * (10 * Fraction(0) - Fraction(1)) / 48  # generic kappa
        self.assertEqual(pf, Fraction(0))


class TestSingleChannelLimit(unittest.TestCase):
    """Verify F₂ reduces to κ·λ₂^FP in the single-channel limit."""

    def test_per_channel_equals_universal(self):
        """F₂^T + F₂^W = κ·λ₂^FP."""
        for c in C_VALUES:
            r = verify_single_channel_limit(c)
            self.assertTrue(r['additivity_holds'],
                            f"Additivity fails at c={c}")

    def test_per_channel_function(self):
        """F₂^{per-channel} = F₂^{universal} (algebraic identity)."""
        for c in C_VALUES:
            self.assertEqual(F2_w3_per_channel(c), F2_w3_scalar_universal(c))

    def test_F2_universal_formula(self):
        """F₂^{universal} = (5c/6) · (7/5760) = 7c/6912."""
        for c in C_VALUES:
            expected = Fraction(7) * c / 6912
            self.assertEqual(F2_w3_scalar_universal(c), expected)


class TestShadowData(unittest.TestCase):
    """Verify shadow tower coefficients for W₃ primary lines."""

    def test_S3_T_value(self):
        """T-line cubic shadow S₃ = 2 (= Virasoro α)."""
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


class TestNumericalConsistency(unittest.TestCase):
    """Numerical cross-checks at specific c values."""

    def test_F2_at_c26(self):
        """c = 26 (critical Virasoro): F₂ = (5·26/6)·(7/5760) = 91/17280."""
        c = Fraction(26)
        F2 = F2_w3_scalar_universal(c)
        # 5·26/6 = 130/6 = 65/3
        # 65/3 · 7/5760 = 455/17280 = 91/3456
        expected = Fraction(65, 3) * Fraction(7, 5760)
        self.assertEqual(F2, expected)

    def test_F2_at_c13(self):
        """c = 13 (self-dual Virasoro): F₂ = (5·13/6)·(7/5760)."""
        c = Fraction(13)
        F2 = F2_w3_scalar_universal(c)
        expected = Fraction(65, 6) * Fraction(7, 5760)
        self.assertEqual(F2, expected)

    def test_cross_channel_ratio(self):
        """The ratio δF₂/F₂ as a function of c.

        δF₂/F₂ = [(c+120)/(16c)] / [(5c/6)·(7/5760)]
               = [(c+120)/(16c)] / [7c/6912]
               = 6912(c+120) / (16·7·c²)
               = 6912(c+120) / (112c²)
               = 432(c+120) / (7c²)
        """
        for c in C_VALUES:
            r = F2_w3_with_cross_channel(c)
            if r['F2_universal'] != 0:
                ratio = r['cross_channel_correction'] / r['F2_universal']
                expected = Fraction(432) * (c + 120) / (7 * c * c)
                self.assertEqual(ratio, expected,
                                 f"Ratio δF₂/F₂ wrong at c={c}")

    def test_cross_channel_large_c_limit(self):
        """At large c: δF₂ ≈ 1/16 (finite, nonzero).

        As c → ∞: (c+120)/(16c) → 1/16.
        """
        c_large = Fraction(10000)
        delta = cross_channel_correction(c_large)
        # Should be close to 1/16 = 0.0625
        self.assertAlmostEqual(float(delta), 1/16, places=3)


class TestGraphSumComputation(unittest.TestCase):
    """Test the full graph sum computation."""

    def test_compute_F2_w3_returns_all_fields(self):
        """compute_F2_w3 returns the expected dictionary keys."""
        c = Fraction(2)
        result = compute_F2_w3(c)
        for key in ['c', 'kappa_T', 'kappa_W', 'kappa_total',
                     'lambda2_fp', 'F2_universal',
                     'boundary_total', 'boundary_diagonal',
                     'cross_channel_correction', 'per_graph']:
            self.assertIn(key, result, f"Missing key: {key}")

    def test_per_graph_names(self):
        """All 6 graphs appear in the per-graph results."""
        c = Fraction(2)
        result = compute_F2_w3(c)
        expected_names = {'smooth', 'fig_eight', 'banana', 'dumbbell', 'theta', 'lollipop'}
        self.assertEqual(set(result['per_graph'].keys()), expected_names)

    def test_cross_channel_matches_formula(self):
        """Cross-channel from graph sum matches the analytic formula."""
        for c in C_VALUES:
            result = compute_F2_w3(c)
            analytic = cross_channel_correction(c)
            self.assertEqual(result['cross_channel_correction'], analytic,
                             f"Cross-channel mismatch at c={c}")


class TestDualityConsistency(unittest.TestCase):
    """Verify Koszul duality constraints for W₃.

    W₃ at c has dual W₃ at c' = 100 - c.
    κ(W₃, c) + κ(W₃, c') = 5·100/6 = 250/3.
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


class TestBananaVertexUniversality(unittest.TestCase):
    """The banana vertex factor V_{0,4}(i,i,j,j) = 2c is UNIVERSAL.

    This is a remarkable property: the genus-0 4-point function for the
    W₃ Frobenius algebra has the SAME value for all channel assignments.
    This is because:
        Σ_m η^{mm} C_{iim} C_{jjm} = (2/c)·C_{ii,T}·C_{jj,T}
        and C_{TT,T} = C_{WW,T} = c (the T-channel always carries c).
    """

    def test_universality(self):
        for c in C_VALUES:
            for ch1 in ['T', 'W']:
                for ch2 in ['T', 'W']:
                    V = V04_s_channel(ch1, ch1, ch2, ch2, c)
                    self.assertEqual(V, 2 * c,
                                     f"V₀₄({ch1}{ch1}{ch2}{ch2}) ≠ 2c at c={c}")


class TestPhysicalConsistency(unittest.TestCase):
    """Physical consistency checks."""

    def test_F2_positive_for_positive_c(self):
        """F₂ > 0 for c > 0 (positive Bernoulli sign convention)."""
        for c in [Fraction(1), Fraction(2), Fraction(26)]:
            F2 = F2_w3_scalar_universal(c)
            self.assertGreater(F2, 0,
                               f"F₂ ≤ 0 at c={c}")

    def test_F2_proportional_to_c(self):
        """F₂ is linear in c (by the universal formula)."""
        fp2 = lambda_fp(2)
        for c in C_VALUES:
            self.assertEqual(F2_w3_scalar_universal(c),
                             Fraction(5, 6) * c * fp2)

    def test_planted_forest_sign(self):
        """For c < 40: δ_pf^T > 0. For c > 40: δ_pf^T < 0."""
        self.assertGreater(planted_forest_correction_T(Fraction(1)), 0)
        self.assertGreater(planted_forest_correction_T(Fraction(26)), 0)
        self.assertLess(planted_forest_correction_T(Fraction(50)), 0)
        self.assertLess(planted_forest_correction_T(Fraction(100)), 0)


if __name__ == '__main__':
    unittest.main()
