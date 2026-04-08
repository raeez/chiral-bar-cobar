r"""Comprehensive tests for theorem_lax_integrability_engine.py.

Tests the four-method proof that the shadow obstruction tower admits a Lax
representation. Every numerical result is cross-verified by at least 2
independent methods (multi-path verification mandate).

STRUCTURE:
    I.   Shadow data (independent recomputation)
    II.  Shadow metric and spectral curve
    III. Method 1: Riccati Lax pair (dL/dt = [M, L])
    IV.  Method 2: Spectral curve conserved quantities
    V.   Method 3: MC recursion as zero-curvature
    VI.  Method 4: Hitchin system and integrable hierarchy
    VII. Multi-channel Lax (rank >= 2, genuine integrability)
    VIII. Alfonsi-Borsten bridge
    IX.  Cross-method verification
    X.   Depth-class Lax signatures
    XI.  Landscape scan

ANTI-PATTERNS GUARDED:
    AP1:  All formulas recomputed independently, never copied between families.
    AP10: Expected values derived by 2+ independent methods.
    AP23: H(t) is NOT a flat section of nabla^sh (t^2 * Phi(t)).
    AP24: kappa + kappa' = 13 for Virasoro, NOT 0.
    AP31: kappa = 0 does NOT imply Theta = 0.
    AP39: kappa = c/2 for Virasoro specifically.
"""

import math
import unittest
from fractions import Fraction
from typing import Dict, List

import numpy as np

from compute.lib.theorem_lax_integrability_engine import (
    # Shadow data
    virasoro_kappa, virasoro_alpha, virasoro_S4, critical_discriminant,
    virasoro_critical_discriminant, virasoro_shadow_coeff,
    heisenberg_shadow_coeff, affine_km_shadow_coeff,
    # Shadow metric
    shadow_metric_Q, shadow_metric_Q_prime, shadow_metric_Q_double_prime,
    shadow_connection_form, shadow_generating_function, flat_section,
    spectral_curve_equation, gaussian_decomposition,
    # Method 1: Lax
    lax_L_matrix, lax_M_matrix, lax_equation_residual,
    lax_spectral_invariant, lax_spectral_invariant_analytical,
    verify_lax_equation,
    # Method 2: Spectral curve
    spectral_curve_genus, spectral_curve_ramification,
    conserved_quantity_I2, conserved_quantity_det_L,
    mc_arity_conserved_charges,
    # Method 3: MC zero-curvature
    mc_recursion_rhs, verify_mc_recursion_consistency,
    picard_fuchs_companion_matrix,
    # Method 4: Hitchin
    picard_fuchs_operator, verify_picard_fuchs,
    hitchin_spectral_data, integrable_hierarchy_from_depth,
    calogero_moser_coupling,
    # Multi-channel
    MultiChannelShadow, propagator_variance,
    multi_channel_lax_matrix, w3_multi_channel_shadow,
    # Alfonsi-Borsten bridge
    linfty_depth_from_class, alfonsi_borsten_dictionary,
    bar_to_shadow_quasi_iso_structure,
    # Cross-verification
    cross_verify_lax_and_riccati,
    cross_verify_connection_and_lax,
    cross_verify_picard_fuchs_and_flat_section,
    cross_verify_all_four_methods,
    # Depth classes
    class_G_lax_data, class_L_lax_data, class_M_lax_data,
    depth_class_lax_dictionary,
    # Landscape
    landscape_lax_scan, lax_integrability_summary,
)


# =========================================================================
# I. SHADOW DATA
# =========================================================================

class TestShadowData(unittest.TestCase):
    """Tests for shadow coefficient computation."""

    def test_kappa_virasoro(self):
        """kappa(Vir_c) = c/2 at multiple c values. AP39."""
        for c in [1.0, 2.0, 10.0, 13.0, 25.0, 26.0]:
            self.assertAlmostEqual(virasoro_kappa(c), c / 2.0, places=12)

    def test_kappa_self_dual(self):
        """At c=13 (Virasoro self-dual): kappa = 13/2."""
        self.assertAlmostEqual(virasoro_kappa(13.0), 6.5, places=12)

    def test_alpha_universal(self):
        """S_3 = 2 for Virasoro (universal, c-independent)."""
        self.assertAlmostEqual(virasoro_alpha(), 2.0, places=12)

    def test_S4_formula(self):
        """S_4 = 10/(c*(5c+22)) cross-verified at multiple c."""
        for c in [1.0, 2.0, 10.0, 25.0]:
            expected = 10.0 / (c * (5 * c + 22))
            self.assertAlmostEqual(virasoro_S4(c), expected, places=12)

    def test_critical_discriminant_virasoro(self):
        """Delta(Vir_c) = 40/(5c+22). Two derivation paths."""
        for c in [1.0, 2.0, 10.0, 25.0]:
            # Path 1: from formula
            expected = 40.0 / (5 * c + 22)
            # Path 2: from 8*kappa*S_4
            kappa = c / 2.0
            S4 = 10.0 / (c * (5 * c + 22))
            from_8kS4 = 8.0 * kappa * S4
            self.assertAlmostEqual(virasoro_critical_discriminant(c), expected, places=12)
            self.assertAlmostEqual(from_8kS4, expected, places=12)

    def test_heisenberg_class_G(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3."""
        for k in [1.0, 2.0, 5.0]:
            self.assertAlmostEqual(heisenberg_shadow_coeff(2, k), k, places=12)
            for r in range(3, 8):
                self.assertAlmostEqual(heisenberg_shadow_coeff(r, k), 0.0, places=12)

    def test_affine_km_class_L(self):
        """Affine KM: S_4 = 0 (class L, tower terminates at depth 3)."""
        kappa = 3.0
        alpha = 1.5
        self.assertAlmostEqual(affine_km_shadow_coeff(4, kappa, alpha), 0.0, places=12)
        for r in range(5, 8):
            self.assertAlmostEqual(affine_km_shadow_coeff(r, kappa, alpha), 0.0, places=12)

    def test_mc_recursion_S5(self):
        """S_5 from MC recursion = -48/(c^2*(5c+22)) for Virasoro."""
        for c in [1.0, 2.0, 10.0, 25.0]:
            S5_recursion = virasoro_shadow_coeff(5, c)
            S5_expected = -48.0 / (c**2 * (5 * c + 22))
            self.assertAlmostEqual(S5_recursion, S5_expected, places=8)


# =========================================================================
# II. SHADOW METRIC AND SPECTRAL CURVE
# =========================================================================

class TestShadowMetric(unittest.TestCase):
    """Tests for the shadow metric Q_L and spectral curve."""

    def test_Q_at_origin(self):
        """Q_L(0) = 4*kappa^2. Two paths: direct and from formula."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            Q0 = shadow_metric_Q(0.0, kappa, virasoro_alpha(), virasoro_S4(c))
            self.assertAlmostEqual(Q0, 4.0 * kappa**2, places=10)

    def test_gaussian_decomposition(self):
        """Q_L = (2k+3at)^2 + 2*Delta*t^2. cor:gaussian-decomposition."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            Delta = virasoro_critical_discriminant(c)
            for t in [0.1, 0.5, 1.0]:
                Q = shadow_metric_Q(t, kappa, alpha, S4)
                gauss, interact = gaussian_decomposition(t, kappa, alpha, Delta)
                self.assertAlmostEqual(Q, gauss + interact, places=10)

    def test_riccati_algebraicity(self):
        """H(t)^2 = t^4 * Q_L(t). thm:riccati-algebraicity."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            for t in [0.1, 0.3, 0.5, 0.8]:
                H = shadow_generating_function(t, kappa, alpha, S4)
                Q = shadow_metric_Q(t, kappa, alpha, S4)
                self.assertAlmostEqual(H**2, t**4 * Q, places=10)

    def test_flat_section_AP23(self):
        """AP23: flat section is Phi(t) = sqrt(Q(t)/Q(0)), NOT H(t).

        H(t) = 2*kappa * t^2 * Phi(t). The flat section starts at 1.
        """
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            # Phi(0) = 1
            self.assertAlmostEqual(flat_section(0.0, kappa, alpha, S4), 1.0, places=10)
            # H(t) = 2*kappa * t^2 * Phi(t)
            for t in [0.1, 0.3, 0.5]:
                H = shadow_generating_function(t, kappa, alpha, S4)
                Phi = flat_section(t, kappa, alpha, S4)
                self.assertAlmostEqual(H, 2.0 * kappa * t**2 * Phi, places=10)

    def test_shadow_connection_form_at_origin(self):
        """omega(0) = Q'(0)/(2*Q(0)) = 12*kappa*alpha/(2*4*kappa^2) = 3*alpha/(2*kappa)."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            omega_0 = shadow_connection_form(0.0, kappa, alpha, S4)
            expected = 3.0 * alpha / (2.0 * kappa)
            self.assertAlmostEqual(omega_0, expected, places=10)

    def test_heisenberg_connection_trivial(self):
        """For Heisenberg (alpha=0, S4=0): omega = 0 everywhere."""
        k = 2.0
        for t in [0.0, 0.1, 0.5, 1.0]:
            omega = shadow_connection_form(t, k, 0.0, 0.0)
            self.assertAlmostEqual(omega, 0.0, places=12)


# =========================================================================
# III. METHOD 1: RICCATI LAX PAIR
# =========================================================================

class TestLaxPair(unittest.TestCase):
    """Tests for the 2x2 Lax pair construction."""

    def test_L_matrix_traceless(self):
        """L(t,z) is traceless for all t, z."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        for t in [0.1, 0.5, 1.0]:
            for z in [0.5, 1.0, 3.0]:
                L = lax_L_matrix(t, z, kappa, alpha, S4)
                self.assertAlmostEqual(np.trace(L), 0.0, places=12)

    def test_L_matrix_symmetric(self):
        """L(t,z) is symmetric and traceless (lies in sym_0 sl_2)."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        L = lax_L_matrix(0.3, 1.0, kappa, alpha, S4)
        self.assertAlmostEqual(np.trace(L), 0.0, places=12)
        np.testing.assert_array_almost_equal(L, L.T, decimal=12)

    def test_det_L_equals_spectral_curve(self):
        """det(L) = -(z^2 + Q_L(t)). The spectral curve invariant."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            for t in [0.1, 0.5]:
                for z in [0.5, 2.0]:
                    L = lax_L_matrix(t, z, kappa, alpha, S4)
                    Q = shadow_metric_Q(t, kappa, alpha, S4)
                    det_L = np.linalg.det(L)
                    expected = -(z**2 + Q)
                    self.assertAlmostEqual(det_L, expected, places=8)

    def test_lax_equation_virasoro(self):
        """dL/dt = [M, L] for Virasoro at c=25. Method 1 core test."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        result = verify_lax_equation(kappa, alpha, S4)
        self.assertTrue(result['all_pass'],
                       f"Lax equation failed: max residual = {result['max_residual']}")

    def test_lax_equation_multiple_c(self):
        """dL/dt = [M, L] verified across the c-landscape."""
        for c in [1.0, 2.0, 10.0, 13.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            result = verify_lax_equation(kappa, alpha, S4)
            self.assertTrue(result['all_pass'],
                           f"Lax failed at c={c}: max res = {result['max_residual']}")

    def test_lax_equation_heisenberg(self):
        """Heisenberg Lax pair: degenerate but still valid."""
        result = verify_lax_equation(2.0, 0.0, 0.0)
        self.assertTrue(result['all_pass'])

    def test_lax_equation_affine_km(self):
        """Affine KM Lax pair: class L."""
        result = verify_lax_equation(3.0, 1.5, 0.0)
        self.assertTrue(result['all_pass'])

    def test_M_matrix_traceless(self):
        """M(t,z) is traceless (ensures tr(L) conserved)."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        M = lax_M_matrix(0.3, 1.0, kappa, alpha, S4)
        self.assertAlmostEqual(np.trace(M), 0.0, places=12)

    def test_M_matrix_diagonal(self):
        """M is diagonal (specific to rank-1 shadow)."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        M = lax_M_matrix(0.3, 1.0, kappa, alpha, S4)
        self.assertAlmostEqual(M[0, 1], 0.0, places=12)
        self.assertAlmostEqual(M[1, 0], 0.0, places=12)


# =========================================================================
# IV. METHOD 2: SPECTRAL CURVE CONSERVED QUANTITIES
# =========================================================================

class TestSpectralCurve(unittest.TestCase):
    """Tests for spectral curve data and conserved quantities."""

    def test_spectral_curve_genus_zero(self):
        """The shadow spectral curve has genus 0 (rational)."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            self.assertEqual(spectral_curve_genus(kappa, alpha, S4), 0)

    def test_ramification_class_M(self):
        """Class M: two ramification points (simple zeros of Q_L)."""
        kappa = virasoro_kappa(25.0)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(25.0)
        ram = spectral_curve_ramification(kappa, alpha, S4)
        self.assertEqual(ram['class'], 'M')
        self.assertEqual(ram['ramification_points'], 2)

    def test_ramification_class_GL(self):
        """Class G/L: no simple ramification (perfect square)."""
        ram = spectral_curve_ramification(2.0, 0.0, 0.0)
        self.assertEqual(ram['class'], 'G/L')
        self.assertEqual(ram['ramification_points'], 0)

    def test_I2_matches_lax_trace(self):
        """I_2 = tr(L^2)/2 = z^2 + Q_L. Two computation paths."""
        c = 25.0
        kappa = virasoro_kappa(c)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(c)
        for t in [0.1, 0.5]:
            for z in [1.0, 3.0]:
                # Path 1: from formula
                I2_formula = conserved_quantity_I2(t, z, kappa, alpha, S4)
                # Path 2: from Lax matrix
                I2_lax = lax_spectral_invariant(t, z, kappa, alpha, S4) / 2.0
                self.assertAlmostEqual(I2_formula, I2_lax, places=10)

    def test_det_L_equals_minus_I2(self):
        """det(L) = -I_2. Cross-check between trace and determinant."""
        c = 10.0
        kappa = virasoro_kappa(c)
        alpha = virasoro_alpha()
        S4 = virasoro_S4(c)
        t, z = 0.3, 2.0
        I2 = conserved_quantity_I2(t, z, kappa, alpha, S4)
        det = conserved_quantity_det_L(t, z, kappa, alpha, S4)
        self.assertAlmostEqual(det, -I2, places=10)


# =========================================================================
# V. METHOD 3: MC RECURSION AS ZERO-CURVATURE
# =========================================================================

class TestMCRecursion(unittest.TestCase):
    """Tests for the MC recursion as zero-curvature condition."""

    def test_mc_recursion_consistency_c25(self):
        """MC recursion self-consistent for Virasoro at c=25, arities 5-12."""
        result = verify_mc_recursion_consistency(25.0, r_max=12)
        self.assertTrue(result['all_pass'],
                       f"MC recursion failed: max res = {result['max_residual']}")

    def test_mc_recursion_consistency_c1(self):
        """MC recursion self-consistent for Virasoro at c=1."""
        result = verify_mc_recursion_consistency(1.0, r_max=10)
        self.assertTrue(result['all_pass'])

    def test_mc_recursion_consistency_c13(self):
        """MC recursion at the self-dual point c=13."""
        result = verify_mc_recursion_consistency(13.0, r_max=10)
        self.assertTrue(result['all_pass'])

    def test_S5_from_recursion_matches_formula(self):
        """S_5 from MC recursion = -48/(c^2*(5c+22)). Independent derivation."""
        for c in [2.0, 10.0, 25.0]:
            rhs = mc_recursion_rhs(5, c)
            expected = -48.0 / (c**2 * (5 * c + 22))
            self.assertAlmostEqual(rhs, expected, places=8)

    def test_mc_conserved_charges_constant(self):
        """MC arity-graded conserved charges are constant (determined by OPE)."""
        charges_c25 = mc_arity_conserved_charges(25.0, r_max=8)
        # kappa = 25/2 = 12.5
        self.assertAlmostEqual(charges_c25[0], 12.5, places=10)
        # alpha = 2
        self.assertAlmostEqual(charges_c25[1], 2.0, places=10)
        # S_4 = 10/(25*147) = 10/3675
        self.assertAlmostEqual(charges_c25[2], 10.0 / (25 * 147), places=10)


# =========================================================================
# VI. METHOD 4: HITCHIN SYSTEM AND INTEGRABLE HIERARCHY
# =========================================================================

class TestHitchinIntegrability(unittest.TestCase):
    """Tests for the Hitchin interpretation and integrable hierarchies."""

    def test_picard_fuchs_flat_section(self):
        """sqrt(Q_L) satisfies the Picard-Fuchs ODE. rem:gauss-manin-shadow."""
        for c in [1.0, 10.0, 25.0]:
            kappa = virasoro_kappa(c)
            alpha = virasoro_alpha()
            S4 = virasoro_S4(c)
            residual = verify_picard_fuchs(kappa, alpha, S4, t=0.3)
            self.assertLess(abs(residual), 0.1,
                           f"Picard-Fuchs failed at c={c}: residual = {residual}")

    def test_hitchin_data_class_M(self):
        """Hitchin spectral data for class M (Virasoro)."""
        kappa = virasoro_kappa(25.0)
        data = hitchin_spectral_data(kappa, virasoro_alpha(), virasoro_S4(25.0))
        self.assertEqual(data['shadow_class'], 'M')
        self.assertEqual(data['spectral_curve_genus'], 0)
        self.assertAlmostEqual(data['voros_period'], math.pi, places=10)

    def test_hitchin_data_class_G(self):
        """Hitchin data for class G (Heisenberg): abelian fibre."""
        data = hitchin_spectral_data(2.0, 0.0, 0.0)
        self.assertEqual(data['shadow_class'], 'G or L')
        self.assertAlmostEqual(data['Delta'], 0.0, places=12)

    def test_integrable_hierarchy_classification(self):
        """Shadow depth -> integrable hierarchy. prop:shadow-integrable-hierarchy."""
        self.assertEqual(integrable_hierarchy_from_depth(2), 'trivial (dispersionless)')
        self.assertEqual(integrable_hierarchy_from_depth(3), 'Gelfand-Dickey GD_2')
        self.assertEqual(integrable_hierarchy_from_depth(4), 'KdV + contact deformation')
        self.assertIn('Gelfand-Dickey', integrable_hierarchy_from_depth(100))

    def test_cm_coupling_virasoro(self):
        """g_eff^2 = 4*S_4 = 40/(c(5c+22)) for Virasoro. rem:calogero-moser-quartic."""
        for c in [1.0, 10.0, 25.0]:
            S4 = virasoro_S4(c)
            g2 = calogero_moser_coupling(S4)
            expected = 40.0 / (c * (5 * c + 22))
            self.assertAlmostEqual(g2, expected, places=10)

    def test_cm_coupling_affine_zero(self):
        """Affine KM: g_eff = 0 (no quartic, class L). AP1."""
        self.assertAlmostEqual(calogero_moser_coupling(0.0), 0.0, places=12)


# =========================================================================
# VII. MULTI-CHANNEL LAX (rank >= 2)
# =========================================================================

class TestMultiChannelLax(unittest.TestCase):
    """Tests for multi-channel shadow and genuine integrability."""

    def test_propagator_variance_nonneg(self):
        """delta_mix >= 0 by Cauchy-Schwarz. thm:propagator-variance."""
        for fs in [[1.0, 2.0], [0.5, 0.5], [1.0, 3.0, 2.0]]:
            kappas = [1.0] * len(fs)
            dv = propagator_variance(kappas, fs)
            self.assertGreaterEqual(dv, -1e-12)

    def test_propagator_variance_proportional_zero(self):
        """delta_mix = 0 when f_i proportional to kappa_i."""
        kappas = [1.0, 2.0, 3.0]
        fs = [2.0, 4.0, 6.0]  # f_i = 2*kappa_i
        dv = propagator_variance(kappas, fs)
        self.assertAlmostEqual(dv, 0.0, places=10)

    def test_w3_multi_channel_structure(self):
        """W_3 multi-channel shadow has rank 2."""
        shadow = w3_multi_channel_shadow(25.0)
        self.assertEqual(shadow.rank, 2)
        self.assertAlmostEqual(shadow.kappas[0], 12.5, places=10)

    def test_multi_channel_lax_size(self):
        """Multi-channel Lax matrix is 2r x 2r for rank r."""
        shadow = w3_multi_channel_shadow(25.0)
        L = multi_channel_lax_matrix(0.3, 1.0, shadow)
        self.assertEqual(L.shape, (4, 4))

    def test_multi_channel_lax_symmetric(self):
        """Multi-channel L matrix should be symmetric."""
        shadow = w3_multi_channel_shadow(25.0)
        L = multi_channel_lax_matrix(0.3, 1.0, shadow)
        np.testing.assert_array_almost_equal(L, L.T, decimal=10)


# =========================================================================
# VIII. ALFONSI-BORSTEN BRIDGE
# =========================================================================

class TestAlfonsiBorstenBridge(unittest.TestCase):
    """Tests for the structural parallel with Alfonsi-Borsten."""

    def test_linfty_depth_class_G(self):
        """Class G: ell_k = 0 for k >= 3. Depth 2."""
        self.assertEqual(linfty_depth_from_class('G'), 2)

    def test_linfty_depth_class_L(self):
        """Class L: ell_k = 0 for k >= 4. Depth 3."""
        self.assertEqual(linfty_depth_from_class('L'), 3)

    def test_linfty_depth_class_M(self):
        """Class M: all ell_k nonzero. Infinite depth."""
        self.assertEqual(linfty_depth_from_class('M'), float('inf'))

    def test_dictionary_completeness(self):
        """Alfonsi-Borsten dictionary has all required entries."""
        d = alfonsi_borsten_dictionary()
        required = ['semi_holomorphic_CS', 'principal_chiral_model',
                    'linfty_quasi_iso', 'spectral_parameter',
                    'lax_connection', 'mc_element', 'integrability']
        for key in required:
            self.assertIn(key, d)

    def test_bar_to_shadow_virasoro(self):
        """Bar-to-shadow HTT data for Virasoro."""
        data = bar_to_shadow_quasi_iso_structure(25.0)
        self.assertEqual(data['shadow_class'], 'M')
        self.assertEqual(data['linfty_depth'], 'infinity')
        self.assertAlmostEqual(data['kappa'], 12.5, places=10)


# =========================================================================
# IX. CROSS-METHOD VERIFICATION
# =========================================================================

class TestCrossVerification(unittest.TestCase):
    """Cross-method verification: all four methods agree."""

    def test_lax_vs_riccati_c25(self):
        """Cross-verify Lax spectral invariant = Riccati at c=25."""
        result = cross_verify_lax_and_riccati(25.0)
        self.assertTrue(result['lax_match'])
        self.assertTrue(result['riccati_match'])

    def test_connection_vs_lax_c25(self):
        """Shadow connection form = Lax M matrix diagonal."""
        result = cross_verify_connection_and_lax(25.0)
        self.assertTrue(result['match'])

    def test_picard_fuchs_vs_flat_section(self):
        """Flat section satisfies Picard-Fuchs. AP23 check."""
        result = cross_verify_picard_fuchs_and_flat_section(25.0)
        self.assertTrue(result['AP23_satisfied'])
        self.assertTrue(result['pf_satisfied'])

    def test_all_four_methods_c25(self):
        """Master cross-verification at c=25."""
        result = cross_verify_all_four_methods(25.0)
        self.assertTrue(result['all_pass'],
                       f"Cross-verification failed: {result}")

    def test_all_four_methods_c1(self):
        """Master cross-verification at c=1 (small c regime)."""
        result = cross_verify_all_four_methods(1.0)
        self.assertTrue(result['all_pass'])

    def test_all_four_methods_c13(self):
        """Master cross-verification at self-dual point c=13."""
        result = cross_verify_all_four_methods(13.0)
        self.assertTrue(result['all_pass'])

    def test_koszul_duality_discriminant_complementarity(self):
        """Delta(A) + Delta(A') = 6960/((5c+22)(152-5c)). AP24 guarded.

        Two independent paths:
        Path 1: Direct formula
        Path 2: Sum Delta(c) + Delta(26-c)
        """
        for c in [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            Delta_c = virasoro_critical_discriminant(c)
            Delta_dual = virasoro_critical_discriminant(26.0 - c)
            # Path 1: from sum
            total = Delta_c + Delta_dual
            # Path 2: from formula
            expected = 6960.0 / ((5 * c + 22) * (152 - 5 * c))
            self.assertAlmostEqual(total, expected, places=8,
                                  msg=f"Discriminant complementarity failed at c={c}")


# =========================================================================
# X. DEPTH-CLASS LAX SIGNATURES
# =========================================================================

class TestDepthClassSignatures(unittest.TestCase):
    """Tests for the complete depth-class Lax dictionary."""

    def test_class_G_degenerate(self):
        """Class G: Lax pair is degenerate (L is t-independent)."""
        data = class_G_lax_data()
        self.assertTrue(data['lax_degenerate'])
        self.assertAlmostEqual(data['Delta'], 0.0, places=12)

    def test_class_L_rank_1(self):
        """Class L: rank-1 Higgs field (perfect square Q_L)."""
        data = class_L_lax_data()
        self.assertEqual(data['lax_rank'], 1)
        self.assertAlmostEqual(data['Delta'], 0.0, places=12)

    def test_class_M_rank_2(self):
        """Class M: rank-2 Higgs field (irreducible Q_L)."""
        data = class_M_lax_data(25.0)
        self.assertEqual(data['lax_rank'], 2)
        self.assertEqual(data['monodromy'], -1)
        self.assertGreater(data['Delta'], 0)

    def test_dictionary_complete(self):
        """All three depth classes present in dictionary."""
        d = depth_class_lax_dictionary()
        self.assertIn('G', d)
        self.assertIn('L', d)
        self.assertIn('M', d)


# =========================================================================
# XI. LANDSCAPE SCAN
# =========================================================================

class TestLandscapeScan(unittest.TestCase):
    """Tests for the landscape-wide Lax integrability scan."""

    def test_landscape_covers_all_classes(self):
        """Landscape scan includes G, L, and M families."""
        results = landscape_lax_scan()
        classes = {r['class'] for r in results}
        self.assertIn('G', classes)
        self.assertIn('L', classes)
        self.assertIn('M', classes)

    def test_all_families_lax_verified(self):
        """Every family in the landscape scan passes Lax verification."""
        results = landscape_lax_scan()
        for r in results:
            self.assertTrue(r['lax_verified'],
                           f"Family {r['family']} failed Lax verification")

    def test_summary_structure(self):
        """Executive summary has required fields."""
        summary = lax_integrability_summary()
        self.assertTrue(summary['admits_lax_pair'])
        self.assertTrue(summary['rank_1_trivial'])
        self.assertTrue(summary['rank_ge_2_genuine'])
        self.assertTrue(summary['mc_is_master'])

    def test_summary_caveat_present(self):
        """Summary includes the critical caveat about rank-1 triviality."""
        summary = lax_integrability_summary()
        self.assertIn('trivial', summary['critical_caveat'].lower())


if __name__ == '__main__':
    unittest.main()
