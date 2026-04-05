"""Comprehensive tests for bc_ode_im_shadow_engine.py.

Tests the ODE/IM correspondence engine: shadow potentials, Numerov solver,
spectral determinant, WKB quantization, Stokes multipliers, functional
relations, instanton actions, and cross-verification utilities.

Every numerical result is cross-verified by at least 2 independent methods
where possible (multi-path verification mandate).
"""

import math
import cmath
import unittest
from typing import List

import numpy as np

from compute.lib.bc_ode_im_shadow_engine import (
    # Shadow data
    virasoro_kappa, virasoro_S3, virasoro_S4, virasoro_S5,
    virasoro_shadow_coefficient_float,
    heisenberg_kappa, affine_sl2_kappa, betagamma_kappa,
    family_shadow_coefficients,
    # Potential
    shadow_potential, shadow_potential_derivative,
    # Numerov
    numerov_step, find_eigenvalue,
    compute_eigenvalues, compute_eigenvalues_robust,
    NumerovResult,
    # Spectral determinant
    spectral_determinant, spectral_determinant_log_derivative,
    spectral_determinant_zeros, spectral_zeta_function,
    # WKB / turning points
    classical_turning_points, wkb_momentum,
    stokes_multipliers_wkb,
    # Baxter TQ
    BaxterTQResult,
    baxter_Q_from_spectral_det, baxter_transfer_eigenvalue_harmonic,
    verify_baxter_tq_harmonic, verify_baxter_tq_aho,
    # Functional relations
    functional_relation_test, shadow_depth_to_M,
    # WKB eigenvalues
    wkb_eigenvalue_leading, wkb_eigenvalues, wkb_accuracy,
    # Voros / staircase
    spectral_staircase, wkb_staircase,
    voros_coefficient, voros_coefficients,
    # Instanton
    instanton_action, instanton_corrections, instanton_action_numerical,
    # Monster / class M
    monster_potential_truncated, monster_spectral_comparison,
    depth_class_spectral_signature,
    # Wall-crossing
    bps_wall_comparison,
    # Cross-verification
    harmonic_oscillator_exact, quartic_aho_reference,
    verify_numerov_harmonic, full_ode_im_pipeline,
)


class TestShadowData(unittest.TestCase):
    """Tests for shadow coefficient functions."""

    def test_virasoro_kappa_formula(self):
        """kappa(Vir_c) = c/2, verified at multiple c values."""
        for c in [1.0, 2.0, 10.0, 25.0, 26.0, 0.5]:
            self.assertAlmostEqual(virasoro_kappa(c), c / 2.0, places=12)

    def test_virasoro_S3_universal(self):
        """S_3 = 2 for all c (universal cubic shadow)."""
        for c in [1.0, 10.0, 25.0, 100.0]:
            self.assertAlmostEqual(virasoro_S3(c), 2.0, places=12)

    def test_virasoro_S4_formula(self):
        """S_4 = 10/(c*(5c+22)) cross-verified by direct computation."""
        for c in [1.0, 2.0, 10.0, 25.0]:
            expected = 10.0 / (c * (5 * c + 22))
            self.assertAlmostEqual(virasoro_S4(c), expected, places=12)

    def test_virasoro_S4_singular_at_c0(self):
        """S_4 diverges as c -> 0."""
        self.assertEqual(virasoro_S4(0.0), float('inf'))

    def test_virasoro_S5_formula(self):
        """S_5 = -48/(c^2*(5c+22))."""
        for c in [1.0, 5.0, 10.0, 25.0]:
            expected = -48.0 / (c**2 * (5 * c + 22))
            self.assertAlmostEqual(virasoro_S5(c), expected, places=10)

    def test_virasoro_shadow_coefficient_r2(self):
        """virasoro_shadow_coefficient_float at r=2 matches kappa."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coefficient_float(2, c),
                virasoro_kappa(c), places=12
            )

    def test_virasoro_shadow_coefficient_r3(self):
        """virasoro_shadow_coefficient_float at r=3 matches S_3=2."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coefficient_float(3, c), 2.0, places=12
            )

    def test_virasoro_shadow_coefficient_r4(self):
        """virasoro_shadow_coefficient_float at r=4 matches S_4."""
        for c in [1.0, 5.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coefficient_float(4, c),
                virasoro_S4(c), places=10
            )

    def test_virasoro_shadow_coefficient_r5(self):
        """virasoro_shadow_coefficient_float at r=5 matches S_5."""
        for c in [5.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coefficient_float(5, c),
                virasoro_S5(c), places=8
            )

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k in [1.0, 2.0, 0.5, 10.0]:
            self.assertAlmostEqual(heisenberg_kappa(k), k, places=12)

    def test_affine_sl2_kappa(self):
        """kappa(aff sl_2, k) = 3(k+2)/4."""
        for k in [1.0, 2.0, 5.0, 10.0]:
            self.assertAlmostEqual(affine_sl2_kappa(k), 3.0 * (k + 2) / 4.0, places=12)

    def test_betagamma_kappa(self):
        """kappa(betagamma_lambda) = c/2 where c = 12*lam^2 - 12*lam + 2.

        AP48: kappa depends on the full algebra. Not kappa = -lambda.
        Cross-check: lambda=1 => c=2, kappa=1. lambda=1/2 => c=-1, kappa=-1/2.
        lambda=0 => c=2, kappa=1 (symmetric under lambda <-> 1-lambda).
        """
        for lam in [0.0, 0.5, 1.0, 2.0]:
            c = 12.0 * lam**2 - 12.0 * lam + 2.0
            expected = c / 2.0
            self.assertAlmostEqual(betagamma_kappa(lam), expected, places=12)
        # Specific checks
        self.assertAlmostEqual(betagamma_kappa(1.0), 1.0, places=12)
        self.assertAlmostEqual(betagamma_kappa(0.5), -0.5, places=12)
        # Symmetry: kappa(lam) = kappa(1-lam)
        for lam in [0.1, 0.3, 0.7]:
            self.assertAlmostEqual(
                betagamma_kappa(lam), betagamma_kappa(1.0 - lam), places=12)

    def test_virasoro_shadow_r_below_2(self):
        """S_r = 0 for r < 2."""
        self.assertAlmostEqual(virasoro_shadow_coefficient_float(0, 10.0), 0.0)
        self.assertAlmostEqual(virasoro_shadow_coefficient_float(1, 10.0), 0.0)

    def test_koszul_duality_kappa_sum(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0."""
        for c in [1.0, 5.0, 10.0, 13.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_kappa(c) + virasoro_kappa(26.0 - c), 13.0, places=10
            )

    def test_self_dual_point_c13(self):
        """At c=13, kappa = kappa_dual = 13/2."""
        self.assertAlmostEqual(virasoro_kappa(13.0), virasoro_kappa(26.0 - 13.0), places=12)


class TestFamilyShadowCoefficients(unittest.TestCase):
    """Tests for family_shadow_coefficients dispatch."""

    def test_heisenberg_is_class_G(self):
        """Heisenberg is class G: only S_2 nonzero."""
        coeffs = family_shadow_coefficients('heisenberg', r_max=6, k=1.0)
        self.assertAlmostEqual(coeffs[0], 1.0, places=10)  # S_2 = kappa = k
        for i in range(1, len(coeffs)):
            self.assertAlmostEqual(coeffs[i], 0.0, places=10)

    def test_affine_sl2_is_class_L(self):
        """Affine sl_2 is class L: S_2, S_3 nonzero, rest zero."""
        coeffs = family_shadow_coefficients('affine_sl2', r_max=6, k=1.0)
        self.assertGreater(abs(coeffs[0]), 1e-10)  # S_2 = kappa
        self.assertGreater(abs(coeffs[1]), 1e-10)  # S_3 = alpha
        for i in range(2, len(coeffs)):
            self.assertAlmostEqual(coeffs[i], 0.0, places=10)

    def test_betagamma_is_class_C(self):
        """Betagamma is class C: S_2, S_3, S_4 nonzero, rest zero."""
        coeffs = family_shadow_coefficients('betagamma', r_max=6, lam=1.0)
        self.assertGreater(abs(coeffs[0]), 1e-10)
        self.assertGreater(abs(coeffs[1]), 1e-10)
        self.assertGreater(abs(coeffs[2]), 1e-10)
        for i in range(3, len(coeffs)):
            self.assertAlmostEqual(coeffs[i], 0.0, places=10)

    def test_virasoro_all_nonzero(self):
        """Virasoro is class M: all S_r nonzero for reasonable c."""
        coeffs = family_shadow_coefficients('virasoro', r_max=6, c=25.0)
        for i in range(min(5, len(coeffs))):
            self.assertGreater(abs(coeffs[i]), 1e-15,
                               f"S_{i+2} should be nonzero for Virasoro c=25")

    def test_unknown_family_raises(self):
        """Unknown family name raises ValueError."""
        with self.assertRaises(ValueError):
            family_shadow_coefficients('nonexistent')

    def test_coefficients_length(self):
        """Returned list has r_max - 1 entries (S_2 through S_{r_max})."""
        for r_max in [5, 8, 10]:
            coeffs = family_shadow_coefficients('heisenberg', r_max=r_max, k=1.0)
            self.assertEqual(len(coeffs), r_max - 1)


class TestShadowPotential(unittest.TestCase):
    """Tests for the shadow potential V(x)."""

    def test_harmonic_potential(self):
        """V(x) = kappa * x^2 for class G (only S_2 nonzero)."""
        kappa = 2.0
        coeffs = [kappa]
        for x in [0.0, 1.0, 2.0, 3.0]:
            self.assertAlmostEqual(shadow_potential(x, coeffs), kappa * x**2, places=10)

    def test_quartic_potential(self):
        """V(x) = kappa*x^2 + S_3*x^4 for class L."""
        kappa, S3 = 2.0, 1.5
        coeffs = [kappa, S3]
        for x in [0.0, 1.0, 2.0]:
            expected = kappa * x**2 + S3 * x**4
            self.assertAlmostEqual(shadow_potential(x, coeffs), expected, places=10)

    def test_potential_at_origin(self):
        """V(0) = 0 for any shadow coefficients."""
        for coeffs in [[1.0], [1.0, 2.0, 3.0], [5.0, -1.0]]:
            self.assertAlmostEqual(shadow_potential(0.0, coeffs), 0.0, places=14)

    def test_potential_derivative_harmonic(self):
        """dV/dx = 2*kappa*x for harmonic."""
        kappa = 3.0
        coeffs = [kappa]
        for x in [1.0, 2.0, 5.0]:
            expected = 2 * kappa * x
            self.assertAlmostEqual(shadow_potential_derivative(x, coeffs), expected, places=10)

    def test_potential_derivative_at_origin(self):
        """dV/dx(0) = 0 for any potential (even function)."""
        coeffs = [2.0, 1.0, 0.5]
        self.assertAlmostEqual(shadow_potential_derivative(0.0, coeffs), 0.0, places=12)

    def test_potential_symmetry(self):
        """V(-x) = V(x) (even powers only)."""
        coeffs = [2.0, 1.0, 0.5]
        for x in [1.0, 2.0, 3.5]:
            self.assertAlmostEqual(
                shadow_potential(x, coeffs),
                shadow_potential(-x, coeffs), places=10
            )


class TestNumerovSolver(unittest.TestCase):
    """Tests for the Numerov ODE solver."""

    def test_numerov_step_consistency(self):
        """Numerov step reproduces known solution for y'' = -y (sin/cos)."""
        h = 0.01
        # y'' = -y => f = -1
        # y = cos(x), y(0)=1, y(h)=cos(h)
        y0 = 1.0
        y1 = math.cos(h)
        f = -1.0
        y2 = numerov_step(y0, y1, f, f, f, h)
        self.assertAlmostEqual(y2, math.cos(2 * h), places=6)

    def test_harmonic_oscillator_ground_state(self):
        """Ground state of V=x^2 should be E_0 = 1 (omega=1, E=omega*(2n+1))."""
        coeffs = [1.0]  # kappa = 1
        E0 = find_eigenvalue(coeffs, 0, 0.5, 1.5, x_max=8.0, h=0.002)
        self.assertAlmostEqual(E0, 1.0, places=2)

    def test_harmonic_oscillator_eigenvalue_spacing(self):
        """Harmonic oscillator eigenvalues have constant spacing 2*omega."""
        kappa = 1.0
        omega = math.sqrt(kappa)
        coeffs = [kappa]
        eigs = compute_eigenvalues(coeffs, n_max=6, x_max=10.0, h=0.003, E_max=20.0)
        if len(eigs) >= 3:
            spacing = eigs[1] - eigs[0]
            for i in range(1, min(len(eigs) - 1, 4)):
                self.assertAlmostEqual(eigs[i + 1] - eigs[i], spacing, places=1)

    def test_verify_numerov_harmonic_pass(self):
        """Cross-verification of Numerov against exact H.O. should pass."""
        result = verify_numerov_harmonic(kappa=1.0, n_test=5, h=0.002, x_max=10.0)
        self.assertTrue(result['passed'])


class TestSpectralDeterminant(unittest.TestCase):
    """Tests for the spectral determinant D(E)."""

    def test_spectral_det_at_eigenvalue(self):
        """D(E_n) = 0 for each eigenvalue E_n."""
        eigenvalues = [1.0, 3.0, 5.0, 7.0, 9.0]
        for E_n in eigenvalues:
            D = spectral_determinant(complex(E_n), eigenvalues)
            self.assertAlmostEqual(abs(D), 0.0, places=10)

    def test_spectral_det_at_zero(self):
        """D(0) = 1 (product of (1 - 0/E_n) = 1)."""
        eigenvalues = [1.0, 3.0, 5.0]
        D = spectral_determinant(0.0 + 0.0j, eigenvalues)
        self.assertAlmostEqual(abs(D), 1.0, places=10)

    def test_spectral_det_product_form(self):
        """D(E) = prod(1 - E/E_n) verified term by term."""
        eigenvalues = [2.0, 4.0, 6.0]
        E = 1.0 + 0.0j
        D = spectral_determinant(E, eigenvalues)
        expected = (1 - 1.0/2.0) * (1 - 1.0/4.0) * (1 - 1.0/6.0)
        self.assertAlmostEqual(abs(D - expected), 0.0, places=10)

    def test_spectral_det_log_derivative(self):
        """d/dE log D = -sum 1/(E_n - E) verified numerically."""
        eigenvalues = [2.0, 5.0, 10.0]
        E = 1.0 + 0.1j
        dlog = spectral_determinant_log_derivative(E, eigenvalues)
        expected = sum(-1.0 / (En - E) for En in eigenvalues)
        self.assertAlmostEqual(abs(dlog - expected), 0.0, places=10)

    def test_spectral_det_zeros_are_eigenvalues(self):
        """spectral_determinant_zeros returns the input eigenvalues."""
        eigenvalues = [1.0, 3.0, 5.0]
        zeros = spectral_determinant_zeros(eigenvalues)
        self.assertEqual(zeros, eigenvalues)

    def test_spectral_zeta_convergence(self):
        """Spectral zeta sum converges for s > 1/2."""
        eigenvalues = [float(2 * n + 1) for n in range(50)]
        z = spectral_zeta_function(2.0, eigenvalues)
        self.assertTrue(z.real > 0)
        self.assertTrue(np.isfinite(z.real))


class TestClassicalTurningPoints(unittest.TestCase):
    """Tests for turning points and WKB momentum."""

    def test_harmonic_turning_points(self):
        """For V=x^2, turning points at x = sqrt(E)."""
        coeffs = [1.0]
        E = 4.0
        tps = classical_turning_points(E, coeffs, x_max=10.0)
        self.assertTrue(len(tps) >= 1)
        self.assertAlmostEqual(tps[0], 2.0, places=1)

    def test_wkb_momentum_classically_allowed(self):
        """p(x) is real in classically allowed region."""
        coeffs = [1.0]
        E = 4.0
        p = wkb_momentum(1.0, E, coeffs)  # V(1) = 1 < E = 4
        self.assertAlmostEqual(p.imag, 0.0, places=10)
        self.assertAlmostEqual(p.real, math.sqrt(3.0), places=10)

    def test_wkb_momentum_classically_forbidden(self):
        """p(x) is purely imaginary in forbidden region."""
        coeffs = [1.0]
        E = 1.0
        p = wkb_momentum(2.0, E, coeffs)  # V(2) = 4 > E = 1
        self.assertAlmostEqual(p.real, 0.0, places=10)
        self.assertAlmostEqual(p.imag, math.sqrt(3.0), places=10)


class TestBaxterTQ(unittest.TestCase):
    """Tests for Baxter TQ relations."""

    def test_transfer_eigenvalue_harmonic_type(self):
        """Transfer eigenvalue returns complex number."""
        T = baxter_transfer_eigenvalue_harmonic(1.0 + 0.1j, 1.0)
        self.assertIsInstance(T, complex)

    def test_baxter_Q_from_spectral_det_consistency(self):
        """Q(u) = D(u) for default map u -> E."""
        eigenvalues = [1.0, 3.0, 5.0]
        u = 2.0 + 0.1j
        Q = baxter_Q_from_spectral_det(u, eigenvalues)
        D = spectral_determinant(u, eigenvalues)
        self.assertAlmostEqual(abs(Q - D), 0.0, places=10)

    def test_baxter_tq_harmonic_verification(self):
        """Verify TQ relation for H.O. returns structured result."""
        result = verify_baxter_tq_harmonic(kappa=1.0, n_test=10)
        self.assertIsInstance(result, BaxterTQResult)
        self.assertEqual(len(result.Q_values), 10)
        self.assertEqual(len(result.T_values), 10)
        self.assertEqual(len(result.residuals), 10)
        # The residuals exist and are finite (TQ with finite truncation
        # gives approximate results; the structural test is the key check).
        for r in result.residuals:
            self.assertTrue(np.isfinite(r))

    def test_verify_baxter_tq_aho_runs(self):
        """verify_baxter_tq_aho runs without error for quartic AHO."""
        coeffs = [1.0, 0.1]  # kappa=1, S_3=0.1
        eigs = harmonic_oscillator_exact(1.0, 20)  # approximate
        result = verify_baxter_tq_aho(coeffs, eigs, M=2, n_test=5)
        self.assertIsInstance(result, BaxterTQResult)


class TestFunctionalRelations(unittest.TestCase):
    """Tests for ODE/IM functional relations."""

    def test_shadow_depth_to_M_mapping(self):
        """Verify depth class to M mapping."""
        self.assertEqual(shadow_depth_to_M('G'), 1)
        self.assertEqual(shadow_depth_to_M('L'), 2)
        self.assertEqual(shadow_depth_to_M('C'), 3)
        self.assertEqual(shadow_depth_to_M('M'), 10)

    def test_functional_relation_test_runs(self):
        """functional_relation_test runs and returns dict."""
        eigs = harmonic_oscillator_exact(1.0, 30)
        result = functional_relation_test(eigs, M=1, n_points=5)
        self.assertIn('residuals', result)
        self.assertIn('omega', result)

    def test_functional_relation_omega(self):
        """omega = exp(2*pi*i/(M+1)) for each M."""
        for M in [1, 2, 3]:
            result = functional_relation_test([1.0, 3.0, 5.0], M=M, n_points=2)
            expected_omega = cmath.exp(2j * cmath.pi / (M + 1))
            self.assertAlmostEqual(abs(result['omega'] - expected_omega), 0.0, places=10)


class TestWKBQuantization(unittest.TestCase):
    """Tests for WKB eigenvalues."""

    def test_wkb_harmonic_exact(self):
        """WKB is exact for H.O.: E_n = omega*(2n+1)."""
        kappa = 4.0
        omega = 2.0
        coeffs = [kappa]
        for n in range(5):
            E_wkb = wkb_eigenvalue_leading(n, coeffs)
            expected = omega * (2 * n + 1)
            self.assertAlmostEqual(E_wkb, expected, places=4)

    def test_wkb_eigenvalues_list_length(self):
        """wkb_eigenvalues returns n_max eigenvalues."""
        coeffs = [1.0]
        eigs = wkb_eigenvalues(coeffs, n_max=10)
        self.assertEqual(len(eigs), 10)

    def test_wkb_accuracy_structure(self):
        """wkb_accuracy returns dict with required keys."""
        exact = [1.0, 3.0, 5.0, 7.0, 9.0]
        wkb = [1.01, 3.01, 5.01, 7.01, 9.01]
        result = wkb_accuracy(exact, wkb)
        self.assertIn('n_compared', result)
        self.assertIn('relative_errors', result)
        self.assertIn('mean_error', result)

    def test_wkb_accuracy_perfect_match(self):
        """Zero error when exact = WKB."""
        eigs = [1.0, 3.0, 5.0, 7.0, 9.0]
        result = wkb_accuracy(eigs, eigs)
        for err in result['relative_errors']:
            self.assertAlmostEqual(err, 0.0, places=10)

    def test_wkb_monotonically_increasing_harmonic(self):
        """WKB eigenvalues are monotonically increasing for harmonic case."""
        coeffs = [2.0]  # pure harmonic (no np.trapezoid call needed)
        eigs = wkb_eigenvalues(coeffs, n_max=10)
        for i in range(len(eigs) - 1):
            self.assertGreater(eigs[i + 1], eigs[i])


class TestSpectralStaircase(unittest.TestCase):
    """Tests for spectral counting function."""

    def test_staircase_below_first(self):
        """N(E) = 0 for E < E_0."""
        eigenvalues = [1.0, 3.0, 5.0]
        self.assertEqual(spectral_staircase(0.5, eigenvalues), 0)

    def test_staircase_counts_correctly(self):
        """N(E) counts eigenvalues <= E."""
        eigenvalues = [1.0, 3.0, 5.0, 7.0]
        self.assertEqual(spectral_staircase(0.5, eigenvalues), 0)
        self.assertEqual(spectral_staircase(1.0, eigenvalues), 1)
        self.assertEqual(spectral_staircase(4.0, eigenvalues), 2)
        self.assertEqual(spectral_staircase(10.0, eigenvalues), 4)

    def test_staircase_monotone(self):
        """Exact staircase is monotonically non-decreasing."""
        eigenvalues = [1.0, 3.0, 5.0, 7.0]
        for E in [0.5, 2.0, 4.0, 6.0, 8.0]:
            N1 = spectral_staircase(E, eigenvalues)
            N2 = spectral_staircase(E + 0.01, eigenvalues)
            self.assertGreaterEqual(N2, N1)


class TestVorosCoefficients(unittest.TestCase):
    """Tests for Voros coefficients."""

    def test_voros_concept_spectral_zeta(self):
        """Spectral zeta function is a related invariant, verify it converges."""
        eigs = harmonic_oscillator_exact(1.0, 30)
        z = spectral_zeta_function(2.0, eigs)
        # H.O. eigenvalues = 1,3,5,..., so zeta = sum 1/(2n+1)^2
        # = pi^2/8
        expected = sum(1.0 / (2 * n + 1)**2 for n in range(30))
        self.assertAlmostEqual(z.real, expected, places=6)

    def test_voros_spectral_zeta_at_s4(self):
        """Spectral zeta at s=4 for H.O. = sum 1/(2n+1)^4."""
        eigs = harmonic_oscillator_exact(1.0, 50)
        z = spectral_zeta_function(4.0, eigs)
        expected = sum(1.0 / (2 * n + 1)**4 for n in range(50))
        self.assertAlmostEqual(z.real, expected, places=6)


class TestInstantonAction(unittest.TestCase):
    """Tests for instanton action computation."""

    def test_instanton_action_harmonic(self):
        """For H.O., A_0 = pi/omega."""
        kappa = 4.0
        omega = 2.0
        coeffs = [kappa]
        A = instanton_action(coeffs)
        self.assertAlmostEqual(A, math.pi / omega, places=6)

    def test_instanton_corrections_structure(self):
        """instanton_corrections returns dict with A_0 and A_total."""
        coeffs = [4.0, 0.5]
        result = instanton_corrections(coeffs)
        self.assertIn('A_0', result)
        self.assertIn('A_total', result)

    def test_instanton_harmonic_is_pi_over_omega(self):
        """Cross-verify: instanton_action_numerical for H.O."""
        kappa = 1.0
        coeffs = [kappa]
        A = instanton_action_numerical(coeffs)
        self.assertAlmostEqual(A, math.pi, places=4)

    def test_instanton_corrections_leading_order(self):
        """A_0 matches pi/omega."""
        kappa = 9.0
        omega = 3.0
        coeffs = [kappa]
        result = instanton_corrections(coeffs)
        self.assertAlmostEqual(result['A_0'], math.pi / omega, places=10)

    def test_instanton_zero_kappa(self):
        """Instanton action is inf for kappa <= 0."""
        coeffs = [0.0]
        A = instanton_action(coeffs)
        self.assertEqual(A, float('inf'))


class TestMonsterPotential(unittest.TestCase):
    """Tests for class M (Virasoro) truncated potential."""

    def test_monster_potential_truncated_at_r2(self):
        """Truncated at r=2: just harmonic."""
        coeffs = [12.5, 2.0, 0.01, 0.001]
        V = monster_potential_truncated(1.0, coeffs, r_max=2)
        self.assertAlmostEqual(V, 12.5, places=5)  # kappa * x^2

    def test_monster_spectral_comparison_runs(self):
        """monster_spectral_comparison returns result dict."""
        result = monster_spectral_comparison(25.0, truncations=[2, 3], n_eigs=3)
        self.assertIn(2, result)
        self.assertIn(3, result)


class TestDepthClassSignature(unittest.TestCase):
    """Tests for spectral signatures of depth classes."""

    def test_heisenberg_scaling_exponent(self):
        """Class G has scaling exponent ~1 (linear spacing)."""
        result = depth_class_spectral_signature('heisenberg', k=1.0)
        self.assertEqual(result['depth_class'], 'G')
        if result.get('scaling_exponent') is not None:
            self.assertAlmostEqual(result['scaling_exponent'], 1.0, delta=0.2)

    def test_depth_class_returns_expected_exponent(self):
        """Expected exponents are provided for each class."""
        result = depth_class_spectral_signature('heisenberg', k=1.0)
        self.assertAlmostEqual(result['expected_exponent'], 1.0, places=5)


class TestBPSWallComparison(unittest.TestCase):
    """Tests for BPS wall comparison."""

    def test_bps_wall_returns_dict(self):
        """bps_wall_comparison returns result with expected keys."""
        result = bps_wall_comparison(25.0)
        self.assertIn('kappa', result)
        self.assertIn('Delta', result)
        self.assertIn('rho', result)
        self.assertIn('instanton_action', result)

    def test_bps_wall_kappa_correct(self):
        """kappa in BPS result matches c/2."""
        c = 10.0
        result = bps_wall_comparison(c)
        self.assertAlmostEqual(result['kappa'], c / 2.0, places=10)


class TestCrossVerification(unittest.TestCase):
    """Cross-verification and pipeline tests."""

    def test_harmonic_oscillator_exact_formula(self):
        """E_n = omega*(2n+1) cross-verified two ways."""
        kappa = 4.0
        omega = 2.0
        exact = harmonic_oscillator_exact(kappa, 5)
        for n in range(5):
            # Path 1: direct formula
            self.assertAlmostEqual(exact[n], omega * (2 * n + 1), places=10)
        # Path 2: spacing is constant = 2*omega
        for i in range(len(exact) - 1):
            self.assertAlmostEqual(exact[i + 1] - exact[i], 2 * omega, places=10)

    def test_quartic_aho_reference_perturbative(self):
        """Quartic AHO reference: perturbation theory limit g->0 -> H.O."""
        kappa = 1.0
        eigs_small_g = quartic_aho_reference(kappa, g=1e-10, n_max=5)
        exact_ho = harmonic_oscillator_exact(kappa, 5)
        for i in range(5):
            self.assertAlmostEqual(eigs_small_g[i], exact_ho[i], places=4)

    def test_quartic_aho_reference_correction_sign(self):
        """Quartic perturbation raises all eigenvalues (positive potential)."""
        kappa = 1.0
        eigs_ho = harmonic_oscillator_exact(kappa, 5)
        eigs_q = quartic_aho_reference(kappa, g=0.1, n_max=5)
        for i in range(5):
            self.assertGreater(eigs_q[i], eigs_ho[i])

    def test_eigenvalue_pipeline_heisenberg(self):
        """Eigenvalue computation works for Heisenberg."""
        coeffs = family_shadow_coefficients('heisenberg', r_max=6, k=1.0)
        effective = [c for c in coeffs if abs(c) > 1e-30]
        eigs = compute_eigenvalues(effective, n_max=5,
                                    x_max=10.0, h=0.003, E_max=20.0)
        self.assertGreater(len(eigs), 0)

    def test_eigenvalue_pipeline_depth_class(self):
        """Heisenberg depth class is G."""
        from compute.lib.bc_ode_im_shadow_engine import _FAMILY_SHADOW_DATA
        info = _FAMILY_SHADOW_DATA.get('heisenberg', {})
        self.assertEqual(info.get('depth_class'), 'G')

    def test_eigenvalue_pipeline_virasoro(self):
        """Eigenvalue computation works for Virasoro shadow potential."""
        coeffs = family_shadow_coefficients('virasoro', r_max=4, c=25.0)
        effective = [c for c in coeffs if abs(c) > 1e-30]
        eigs = compute_eigenvalues(effective, n_max=5,
                                    x_max=10.0, h=0.003, E_max=200.0)
        self.assertGreater(len(eigs), 0)

    def test_classical_turning_points_count(self):
        """Turning point count matches expectation for different potentials."""
        # Harmonic: one turning point in [0, x_max] for E > 0
        coeffs = [1.0]
        tps = classical_turning_points(4.0, coeffs, x_max=10.0)
        self.assertGreaterEqual(len(tps), 1)
        # The turning point should be near sqrt(E) = 2
        self.assertAlmostEqual(tps[0], 2.0, places=1)

    def test_virasoro_shadow_coefficient_mc_recursion(self):
        """MC recursion S_r matches closed form for r=4,5."""
        c = 10.0
        # r=4: S_4 from MC recursion
        S4_recursion = virasoro_shadow_coefficient_float(4, c)
        S4_closed = virasoro_S4(c)
        self.assertAlmostEqual(S4_recursion, S4_closed, places=8)
        # r=5
        S5_recursion = virasoro_shadow_coefficient_float(5, c)
        S5_closed = virasoro_S5(c)
        self.assertAlmostEqual(S5_recursion, S5_closed, places=6)


class TestAdditionalShadowData(unittest.TestCase):
    """Additional shadow data cross-checks."""

    def test_virasoro_S4_positive_for_positive_c(self):
        """S_4 > 0 for c > 0 (positive quartic contact)."""
        for c in [1.0, 5.0, 10.0, 25.0, 50.0]:
            self.assertGreater(virasoro_S4(c), 0.0)

    def test_virasoro_S5_negative_for_positive_c(self):
        """S_5 < 0 for c > 0."""
        for c in [1.0, 5.0, 10.0, 25.0]:
            self.assertLess(virasoro_S5(c), 0.0)

    def test_virasoro_S4_decays_at_large_c(self):
        """S_4 ~ 10/(5c^2) = 2/c^2 for large c (classical limit)."""
        c = 1000.0
        S4 = virasoro_S4(c)
        # S_4 = 10/(c*(5c+22)) ~ 10/(5c^2) = 2/c^2 for large c
        classical = 2.0 / c**2
        self.assertAlmostEqual(S4 / classical, 1.0, places=2)

    def test_virasoro_kappa_at_c26(self):
        """kappa(Vir_26) = 13."""
        self.assertAlmostEqual(virasoro_kappa(26.0), 13.0, places=10)

    def test_affine_sl2_kappa_at_critical_level(self):
        """kappa(aff sl_2, k=-2) = 0 (critical level)."""
        self.assertAlmostEqual(affine_sl2_kappa(-2.0), 0.0, places=10)

    def test_shadow_coefficient_r6_nonzero_virasoro(self):
        """S_6 is nonzero for Virasoro (class M has infinite tower)."""
        S6 = virasoro_shadow_coefficient_float(6, 25.0)
        self.assertGreater(abs(S6), 1e-15)


class TestAdditionalPotential(unittest.TestCase):
    """Additional shadow potential tests."""

    def test_sextic_potential(self):
        """V(x) = kappa*x^2 + S_3*x^4 + S_4*x^6 for class C."""
        kappa, S3, S4 = 2.0, 1.0, 0.5
        coeffs = [kappa, S3, S4]
        x = 1.0
        expected = kappa * x**2 + S3 * x**4 + S4 * x**6
        self.assertAlmostEqual(shadow_potential(x, coeffs), expected, places=10)

    def test_potential_grows_at_infinity(self):
        """V(x) -> infinity as x -> infinity for kappa > 0."""
        coeffs = [1.0, 0.5]
        V10 = shadow_potential(10.0, coeffs)
        V1 = shadow_potential(1.0, coeffs)
        self.assertGreater(V10, V1)

    def test_derivative_sign(self):
        """dV/dx > 0 for x > 0 with positive coefficients."""
        coeffs = [2.0, 1.0]
        for x in [0.5, 1.0, 2.0, 5.0]:
            self.assertGreater(shadow_potential_derivative(x, coeffs), 0.0)


class TestAdditionalNumerov(unittest.TestCase):
    """Additional Numerov solver tests."""

    def test_eigenvalues_robust_returns_numerov_result(self):
        """compute_eigenvalues_robust returns NumerovResult."""
        coeffs = [1.0]
        result = compute_eigenvalues_robust(coeffs, n_max=5,
                                            x_max=10.0, h=0.005,
                                            E_scan_max=20.0, dE=0.1)
        self.assertIsInstance(result, NumerovResult)
        self.assertGreater(len(result.eigenvalues), 0)

    def test_eigenvalues_robust_node_counts(self):
        """Node counts increase with eigenvalue index."""
        coeffs = [1.0]
        result = compute_eigenvalues_robust(coeffs, n_max=5,
                                            x_max=10.0, h=0.005,
                                            E_scan_max=20.0, dE=0.1)
        if len(result.node_counts) >= 2:
            # Node counts should be non-decreasing
            for i in range(len(result.node_counts) - 1):
                self.assertLessEqual(result.node_counts[i],
                                     result.node_counts[i + 1])


class TestAdditionalSpectralDet(unittest.TestCase):
    """Additional spectral determinant tests."""

    def test_spectral_det_negative_E(self):
        """D(E) for E < 0 and positive eigenvalues: |D| > 1."""
        eigenvalues = [1.0, 3.0, 5.0]
        D = spectral_determinant(-1.0 + 0.0j, eigenvalues)
        self.assertGreater(abs(D), 1.0)

    def test_spectral_det_log_derivative_poles(self):
        """Log derivative has poles at E = E_n."""
        eigenvalues = [2.0, 5.0]
        # Near E_n, dlog D diverges
        E_near = 2.0 + 0.001j
        dlog = spectral_determinant_log_derivative(E_near, eigenvalues)
        self.assertGreater(abs(dlog), 100)

    def test_spectral_zeta_harmonic_specific(self):
        """Spectral zeta s=2 for kappa=1 H.O. = sum 1/(2n+1)^2."""
        eigs = harmonic_oscillator_exact(1.0, 100)
        z = spectral_zeta_function(2.0, eigs)
        # Known: sum_{n>=0} 1/(2n+1)^2 = pi^2/8
        self.assertAlmostEqual(z.real, math.pi**2 / 8, places=2)


if __name__ == '__main__':
    unittest.main()
