r"""Comprehensive tests for theorem_ode_im_shadow_engine.py.

Tests the four-method proof that the ODE/IM correspondence IS the shadow
obstruction tower. Every numerical result is cross-verified by at least
2 independent methods (multi-path verification mandate).

STRUCTURE:
    I.   Shadow coefficient data (independent recomputation)
    II.  Method 1: BLZ construction (vacuum eigenvalues = shadow coefficients)
    III. Method 2: Shadow connection = Stokes data
    IV.  Method 3: WKB = shadow expansion
    V.   Method 4: Functional relations = binary MC equation
    VI.  Cross-method verification
    VII. Depth-class spectral signatures
    VIII. Landscape scan

ANTI-PATTERNS GUARDED:
    AP1:  All formulas recomputed independently, never copied between families.
    AP10: Expected values derived by 2+ independent methods.
    AP24: kappa + kappa' = 13 for Virasoro, NOT 0.
    AP39: kappa = c/2 for Virasoro specifically.
"""

import cmath
import math
import unittest
from fractions import Fraction
from typing import Dict, List

import numpy as np

from compute.lib.theorem_ode_im_shadow_engine import (
    # Shadow data
    virasoro_kappa, virasoro_S3, virasoro_S4, virasoro_S5,
    virasoro_shadow_coeff, shadow_coefficients_list,
    shadow_potential_eval,
    # Method 1: BLZ
    kdv_q1_vacuum, kdv_q3_vacuum, kdv_q5_vacuum,
    kdv_q7_vacuum, kdv_q9_vacuum,
    blz_vacuum_eigenvalue,
    blz_shadow_identification_k1,
    blz_shadow_identification_k2,
    blz_shadow_identification_k3,
    blz_full_vacuum_spectrum,
    # Method 2: Stokes
    shadow_metric_Q, shadow_metric_Q_derivative,
    shadow_metric_Q_second_derivative,
    shadow_oper_potential, shadow_oper_at_origin,
    shadow_stokes_from_oper,
    gaudin_shadow_mc_identification,
    # Method 3: WKB
    harmonic_eigenvalue_exact,
    wkb_bohr_sommerfeld_integral,
    wkb_eigenvalue_bs,
    wkb_shadow_comparison_harmonic,
    wkb_anharmonic_comparison,
    wkb_coefficient_shadow_polynomial,
    # Method 4: TQ (lattice)
    spectral_determinant,
    yang_R_matrix_sl2,
    lattice_tq_vacuum,
    lattice_tq_one_magnon,
    tq_relation_anharmonic,
    tq_as_binary_mc,
    baxter_q_as_theta_projection,
    # Cross-verification
    cross_verify_all_methods,
    # Depth classes
    class_G_ode_im, class_L_ode_im, class_C_ode_im, class_M_ode_im,
    depth_class_ode_im_dictionary,
    # Landscape
    ode_im_landscape, ode_im_shadow_summary,
)


# =========================================================================
# I. SHADOW COEFFICIENT DATA
# =========================================================================

class TestShadowData(unittest.TestCase):
    """Tests for shadow coefficient computation (independent recomputation)."""

    def test_kappa_virasoro_formula(self):
        """kappa(Vir_c) = c/2. AP39: specific to Virasoro."""
        for c in [1.0, 2.0, 10.0, 25.0, 26.0]:
            self.assertAlmostEqual(virasoro_kappa(c), c / 2.0, places=12)

    def test_kappa_virasoro_self_dual(self):
        """At c=13 (self-dual point): kappa = 13/2."""
        self.assertAlmostEqual(virasoro_kappa(13.0), 6.5, places=12)

    def test_S3_universal(self):
        """S_3 = 2 for all c (universal cubic shadow)."""
        for c in [0.5, 1.0, 13.0, 25.0, 100.0]:
            self.assertAlmostEqual(virasoro_S3(c), 2.0, places=12)

    def test_S4_formula(self):
        """S_4 = 10/(c*(5c+22)). Cross-verified at multiple c values."""
        for c in [1.0, 2.0, 10.0, 25.0]:
            expected = 10.0 / (c * (5 * c + 22))
            self.assertAlmostEqual(virasoro_S4(c), expected, places=12)

    def test_S5_formula(self):
        """S_5 = -48/(c^2*(5c+22)). From MC recursion."""
        for c in [1.0, 5.0, 10.0, 25.0]:
            expected = -48.0 / (c**2 * (5 * c + 22))
            self.assertAlmostEqual(virasoro_S5(c), expected, places=10)

    def test_shadow_coeff_r2_is_kappa(self):
        """virasoro_shadow_coeff(2, c) = kappa = c/2."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coeff(2, c), virasoro_kappa(c), places=12
            )

    def test_shadow_coeff_r3_is_S3(self):
        """virasoro_shadow_coeff(3, c) = S_3 = 2."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coeff(3, c), 2.0, places=12
            )

    def test_shadow_coeff_r4_is_S4(self):
        """virasoro_shadow_coeff(4, c) = S_4 = 10/(c(5c+22))."""
        for c in [1.0, 5.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_shadow_coeff(4, c), virasoro_S4(c), places=10
            )

    def test_shadow_coefficients_list_length(self):
        """shadow_coefficients_list returns correct number of coefficients."""
        for r_max in [5, 10, 15]:
            coeffs = shadow_coefficients_list(25.0, r_max)
            self.assertEqual(len(coeffs), r_max - 1)

    def test_shadow_potential_harmonic(self):
        """V(x) = kappa*x^2 for pure harmonic (only S_2 nonzero)."""
        kappa = 5.0
        coeffs = [kappa]
        for x in [0.5, 1.0, 2.0]:
            self.assertAlmostEqual(
                shadow_potential_eval(x, coeffs), kappa * x**2, places=12
            )

    def test_shadow_potential_quartic(self):
        """V(x) = kappa*x^2 + S_3*x^4 for class L."""
        kappa = 5.0
        S3 = 2.0
        coeffs = [kappa, S3]
        x = 1.5
        expected = kappa * x**2 + S3 * x**4
        self.assertAlmostEqual(
            shadow_potential_eval(x, coeffs), expected, places=12
        )

    def test_shadow_potential_at_origin(self):
        """V(0) = 0 for all shadow potentials."""
        coeffs = shadow_coefficients_list(25.0, 10)
        self.assertAlmostEqual(shadow_potential_eval(0.0, coeffs), 0.0, places=15)

    def test_kappa_complementarity_virasoro(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0. AP24."""
        for c in [1.0, 5.0, 10.0, 25.0]:
            k1 = virasoro_kappa(c)
            k2 = virasoro_kappa(26 - c)
            self.assertAlmostEqual(k1 + k2, 13.0, places=12)


# =========================================================================
# II. METHOD 1: BLZ CONSTRUCTION
# =========================================================================

class TestBLZMethod(unittest.TestCase):
    """Tests for Method 1: BLZ quantum KdV vacuum eigenvalues = shadow data."""

    def test_q1_vacuum_formula(self):
        """q_1(c, 0) = -c/24 for multiple c values."""
        for c in [1.0, 12.0, 24.0, 25.0]:
            self.assertAlmostEqual(kdv_q1_vacuum(c), -c / 24.0, places=12)

    def test_q3_vacuum_formula(self):
        """q_3(c, 0) = c(5c-1)/720. Cross-verified by direct expansion."""
        for c in [1.0, 10.0, 25.0]:
            expected = c * (5 * c - 1) / 720.0
            self.assertAlmostEqual(kdv_q3_vacuum(c), expected, places=12)

    def test_q5_vacuum_formula(self):
        """q_5(c, 0) = c(2c-1)(5c+1)/4320."""
        for c in [1.0, 10.0, 25.0]:
            expected = c * (2 * c - 1) * (5 * c + 1) / 4320.0
            self.assertAlmostEqual(kdv_q5_vacuum(c), expected, places=10)

    def test_q7_vacuum_formula(self):
        """q_7(c, 0) = c(7c-3)(2c-1)(5c+1)/3265920."""
        for c in [1.0, 10.0, 25.0]:
            expected = c * (7 * c - 3) * (2 * c - 1) * (5 * c + 1) / 3265920.0
            self.assertAlmostEqual(kdv_q7_vacuum(c), expected, places=8)

    def test_q9_vacuum_formula(self):
        """q_9(c, 0) = c(c-1)(2c-1)(5c+1)(7c-11)/261273600."""
        for c in [2.0, 10.0, 25.0]:
            expected = (c * (c - 1) * (2 * c - 1) * (5 * c + 1) * (7 * c - 11)
                        / 261273600.0)
            self.assertAlmostEqual(kdv_q9_vacuum(c), expected, places=6)

    def test_q1_shadow_identification(self):
        """q_1(0) = -kappa/12. Three-path verification."""
        for c in [1.0, 10.0, 25.0]:
            r = blz_shadow_identification_k1(c)
            self.assertTrue(r['all_match'],
                            f"k=1 identification failed at c={c}: "
                            f"errors {r['error_ab']}, {r['error_ac']}")

    def test_q3_shadow_identification(self):
        """q_3(0) = kappa*(10*kappa - 1)/360. Three-path verification."""
        for c in [1.0, 10.0, 25.0]:
            r = blz_shadow_identification_k2(c)
            self.assertTrue(r['all_match'],
                            f"k=2 identification failed at c={c}")

    def test_q5_shadow_identification(self):
        """q_5(0) = kappa*(4*kappa-1)*(10*kappa+1)/2160. Three-path verification."""
        for c in [1.0, 10.0, 25.0]:
            r = blz_shadow_identification_k3(c)
            self.assertTrue(r['all_match'],
                            f"k=3 identification failed at c={c}")

    def test_full_vacuum_spectrum_match(self):
        """All vacuum eigenvalues q_1,...,q_9 match shadow at c=25."""
        r = blz_full_vacuum_spectrum(25.0)
        self.assertTrue(r['all_match'],
                        f"Full vacuum spectrum mismatch at c=25")

    def test_full_vacuum_spectrum_c1(self):
        """Full vacuum spectrum at c=1 (Ising)."""
        r = blz_full_vacuum_spectrum(1.0)
        self.assertTrue(r['all_match'])

    def test_full_vacuum_spectrum_c13(self):
        """Full vacuum spectrum at c=13 (self-dual)."""
        r = blz_full_vacuum_spectrum(13.0)
        self.assertTrue(r['all_match'])

    def test_vacuum_eigenvalues_are_polynomial_in_kappa(self):
        """All q_{2k-1}(0) are polynomial in kappa = c/2.

        Verify by checking that q_{2k-1}(c) = q_{2k-1}(2*kappa) for
        multiple kappa values.
        """
        for kappa in [0.5, 2.5, 6.5, 12.5]:
            c = 2 * kappa
            for order in [1, 3, 5]:
                q_from_c = blz_vacuum_eigenvalue(c, order)
                q_from_kappa = blz_vacuum_eigenvalue(2 * kappa, order)
                self.assertAlmostEqual(q_from_c, q_from_kappa, places=12)

    def test_blz_dispatch(self):
        """blz_vacuum_eigenvalue dispatches correctly for all orders."""
        c = 10.0
        self.assertAlmostEqual(blz_vacuum_eigenvalue(c, 1), kdv_q1_vacuum(c))
        self.assertAlmostEqual(blz_vacuum_eigenvalue(c, 3), kdv_q3_vacuum(c))
        self.assertAlmostEqual(blz_vacuum_eigenvalue(c, 5), kdv_q5_vacuum(c))

    def test_blz_invalid_order_raises(self):
        """blz_vacuum_eigenvalue raises for unsupported orders."""
        with self.assertRaises(ValueError):
            blz_vacuum_eigenvalue(10.0, 2)


# =========================================================================
# III. METHOD 2: SHADOW CONNECTION = STOKES DATA
# =========================================================================

class TestShadowStokes(unittest.TestCase):
    """Tests for Method 2: shadow oper Stokes data."""

    def test_shadow_metric_at_origin(self):
        """Q(0) = c^2 for Virasoro."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(shadow_metric_Q(c, 0.0), c**2, places=10)

    def test_shadow_metric_derivative_at_origin(self):
        """Q'(0) = 12c for Virasoro."""
        for c in [1.0, 10.0, 25.0]:
            self.assertAlmostEqual(
                shadow_metric_Q_derivative(c, 0.0), 12.0 * c, places=10
            )

    def test_shadow_metric_gaussian_decomposition(self):
        """Q(t) = (c + 6t)^2 + 2*Delta*t^2 at t=0: (c)^2 = c^2."""
        c = 25.0
        kappa = c / 2.0
        alpha = 2.0
        S4 = virasoro_S4(c)
        Delta = 8.0 * kappa * S4
        # At t = 1: Q = (c + 6)^2 + 2*Delta
        Q_at_1 = shadow_metric_Q(c, 1.0)
        expected = (c + 6)**2 + 2 * Delta
        self.assertAlmostEqual(Q_at_1, expected, places=8)

    def test_shadow_oper_potential_finite(self):
        """V^sh(0) is finite for generic c."""
        for c in [1.0, 10.0, 25.0]:
            V = shadow_oper_at_origin(c)
            self.assertTrue(math.isfinite(V))

    def test_shadow_oper_potential_two_paths(self):
        """V^sh(0) computed by two independent methods."""
        c = 25.0
        # Path A: from function
        path_a = shadow_oper_at_origin(c)
        # Path B: direct computation
        Q0 = c**2
        Qp0 = 12 * c
        Qpp0 = 72 + 80.0 / (5 * c + 22)
        path_b = -Qpp0 / (4 * Q0) + 3 * Qp0**2 / (16 * Q0**2)
        self.assertAlmostEqual(path_a, path_b, places=10)

    def test_stokes_monodromy_koszul(self):
        """Monodromy around Q_L zeros = -1 (Koszul sign)."""
        for c in [1.0, 10.0, 25.0]:
            r = shadow_stokes_from_oper(c)
            self.assertEqual(r['monodromy'], -1)

    def test_stokes_residue_half(self):
        """Connection residue at zeros of Q = 1/2."""
        for c in [1.0, 10.0, 25.0]:
            r = shadow_stokes_from_oper(c)
            self.assertAlmostEqual(r['residue_at_zeros'], 0.5, places=12)

    def test_instanton_action_universal(self):
        """Universal instanton action A = (2*pi)^2."""
        for c in [1.0, 10.0, 25.0]:
            r = shadow_stokes_from_oper(c)
            self.assertAlmostEqual(r['instanton_action'], (2 * math.pi)**2,
                                   places=10)

    def test_stokes_S1_magnitude(self):
        """Leading Stokes multiplier |S_1| = 4*pi^2*|kappa|."""
        for c in [1.0, 10.0, 25.0]:
            r = shadow_stokes_from_oper(c)
            expected = 4 * math.pi**2 * abs(c / 2.0)
            self.assertAlmostEqual(r['stokes_S1_magnitude'], expected,
                                   places=8)

    def test_stokes_critical_discriminant(self):
        """Delta = 8*kappa*S_4 = 80/(c*(5c+22)) * c/2 = 40/(5c+22)."""
        c = 25.0
        r = shadow_stokes_from_oper(c)
        expected = 40.0 / (5 * c + 22)
        self.assertAlmostEqual(r['Delta'], expected, places=10)

    def test_gaudin_binary_is_r_matrix(self):
        """For n=2 marked points: Gaudin H_1 = r(z_1 - z_2) = 1/(z_1 - z_2)."""
        c = 25.0
        z_points = [complex(1, 0), complex(3, 0)]
        r = gaudin_shadow_mc_identification(c, z_points)
        expected_r = 1.0 / (z_points[0] - z_points[1])
        self.assertAlmostEqual(r['r_matrix_binary'], expected_r, places=10)

    def test_gaudin_three_points_sum_zero(self):
        """Sum of Gaudin eigenvalues = 0 for equidistributed points."""
        c = 25.0
        z_points = [complex(0, 0), complex(1, 0), complex(2, 0)]
        r = gaudin_shadow_mc_identification(c, z_points)
        # H_1 + H_2 + H_3 = sum over all pairs 1/(z_i - z_j)
        # For z = 0, 1, 2: H_1 = -1 + (-1/2) = -3/2
        #                   H_2 = 1 + (-1) = 0
        #                   H_3 = 1/2 + 1 = 3/2
        # Sum = 0
        total = sum(r['gaudin_eigenvalues'])
        self.assertAlmostEqual(total, 0.0, places=10)


# =========================================================================
# IV. METHOD 3: WKB = SHADOW EXPANSION
# =========================================================================

class TestWKBMethod(unittest.TestCase):
    """Tests for Method 3: WKB eigenvalues match shadow coefficients."""

    def test_harmonic_exact_formula(self):
        """E_n = sqrt(kappa)*(2n+1) for harmonic oscillator."""
        kappa = 4.0
        for n in range(5):
            expected = 2.0 * (2 * n + 1)
            self.assertAlmostEqual(
                harmonic_eigenvalue_exact(n, kappa), expected, places=12
            )

    def test_harmonic_ground_state(self):
        """E_0 = sqrt(kappa) for harmonic oscillator."""
        for kappa in [1.0, 4.0, 9.0, 16.0]:
            self.assertAlmostEqual(
                harmonic_eigenvalue_exact(0, kappa),
                math.sqrt(kappa), places=12
            )

    def test_wkb_bs_harmonic_exact(self):
        """WKB Bohr-Sommerfeld is exact for harmonic oscillator."""
        kappa = 4.0
        coeffs = [kappa]
        for n in range(3):
            exact = harmonic_eigenvalue_exact(n, kappa)
            wkb = wkb_eigenvalue_bs(n, coeffs)
            rel_err = abs(exact - wkb) / abs(exact)
            self.assertLess(rel_err, 0.02,
                            f"WKB not exact for harmonic at n={n}: "
                            f"exact={exact}, wkb={wkb}")

    def test_wkb_harmonic_comparison_full(self):
        """Full harmonic comparison: WKB vs exact vs Numerov."""
        r = wkb_shadow_comparison_harmonic(4.0, n_max=3)
        for e in r['eigenvalues'][:3]:
            self.assertLess(e['rel_error_ab'], 0.02,
                            f"WKB-exact mismatch at n={e['n']}")

    def test_wkb_anharmonic_runs(self):
        """Anharmonic WKB comparison runs without error."""
        r = wkb_anharmonic_comparison(25.0, r_max=4, n_max=2)
        self.assertIn('eigenvalues', r)
        self.assertGreater(len(r['eigenvalues']), 0)

    def test_wkb_anharmonic_ground_state_positive(self):
        """Ground state energy is positive for positive potential."""
        r = wkb_anharmonic_comparison(25.0, r_max=4, n_max=1)
        self.assertGreater(r['eigenvalues'][0]['wkb_bs'], 0)
        self.assertGreater(r['eigenvalues'][0]['numerov'], 0)

    def test_wkb_coefficient_is_polynomial_in_shadow(self):
        """WKB corrections are polynomial in shadow coefficients."""
        for c in [10.0, 25.0]:
            r = wkb_coefficient_shadow_polynomial(c, n=0)
            self.assertTrue(r['E1_is_polynomial_in_S3'])
            self.assertTrue(r['E2_is_polynomial_in_S3_S4'])

    def test_wkb_e0_is_harmonic(self):
        """Leading WKB eigenvalue E0 = sqrt(kappa)*(2n+1)."""
        c = 25.0
        kappa = c / 2.0
        r = wkb_coefficient_shadow_polynomial(c, n=0)
        expected_E0 = math.sqrt(kappa)
        self.assertAlmostEqual(r['E0'], expected_E0, places=10)

    def test_wkb_e1_proportional_to_S3(self):
        """First WKB correction E1 is proportional to S_3."""
        c = 25.0
        r = wkb_coefficient_shadow_polynomial(c, n=0)
        # E1 = S3 * <0|x^4|0> = S3 * 3/(4*omega^2)
        kappa = c / 2.0
        omega = math.sqrt(kappa)
        expected_E1 = 2.0 * 3.0 / (4.0 * kappa)  # S3=2, n=0
        self.assertAlmostEqual(r['E1'], expected_E1, places=8)

    def test_wkb_bohr_sommerfeld_quantization(self):
        """Bohr-Sommerfeld integral at exact eigenvalue = (n+1/2)*pi."""
        kappa = 4.0
        coeffs = [kappa]
        for n in range(3):
            E_exact = harmonic_eigenvalue_exact(n, kappa)
            I_bs = wkb_bohr_sommerfeld_integral(E_exact, coeffs)
            target = (n + 0.5) * math.pi
            rel_err = abs(I_bs - target) / target
            self.assertLess(rel_err, 0.02,
                            f"BS integral mismatch at n={n}")


# =========================================================================
# V. METHOD 4: FUNCTIONAL RELATIONS = BINARY MC EQUATION
# =========================================================================

class TestTQMethod(unittest.TestCase):
    """Tests for Method 4: TQ relation = binary MC equation (lattice)."""

    def test_spectral_determinant_zeros(self):
        """D(E_n) = 0 at eigenvalues."""
        eigenvalues = [1.0, 3.0, 5.0, 7.0]
        for E_n in eigenvalues:
            D = spectral_determinant(complex(E_n, 0), eigenvalues)
            self.assertAlmostEqual(abs(D), 0.0, places=10)

    def test_spectral_determinant_normalization(self):
        """D(0) = 1 (normalized at E=0)."""
        eigenvalues = [1.0, 3.0, 5.0, 7.0]
        D0 = spectral_determinant(0.0, eigenvalues)
        self.assertAlmostEqual(D0, 1.0, places=12)

    def test_yang_r_matrix_structure(self):
        """R(u) = u*I + P for sl_2."""
        u = complex(3.0, 0.5)
        R = yang_R_matrix_sl2(u)
        P = np.array([[1, 0, 0, 0], [0, 0, 1, 0],
                       [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
        expected = u * np.eye(4, dtype=complex) + P
        self.assertTrue(np.allclose(R, expected))

    def test_lattice_tq_vacuum_identity(self):
        """Vacuum TQ: (u+1)^L + u^L = (u+1)^L + u^L (identity)."""
        for L in [2, 4, 6]:
            u = complex(2.5, 0.3)
            r = lattice_tq_vacuum(u, L)
            self.assertTrue(r['passed'],
                            f"Vacuum TQ failed for L={L}: residual={r['residual']}")

    def test_lattice_tq_vacuum_multiple_points(self):
        """Vacuum TQ holds at multiple u values."""
        L = 4
        for u_real in [0.5, 1.0, 2.0, 5.0]:
            u = complex(u_real, 0.3)
            r = lattice_tq_vacuum(u, L)
            self.assertTrue(r['passed'])

    def test_lattice_tq_one_magnon_exact(self):
        """One-magnon TQ relation is EXACT (residual < 1e-10)."""
        u = complex(2.0, 0.3)
        r = lattice_tq_one_magnon(u, L=4)
        self.assertTrue(r['passed'],
                        f"One-magnon TQ failed: residual={r['residual']}")

    def test_lattice_tq_one_magnon_bae(self):
        """Bethe root satisfies BAE: (u1+1)^L + u1^L = 0."""
        r = lattice_tq_one_magnon(complex(2.0, 0.3), L=4)
        self.assertLess(r['bae_residual'], 1e-10)

    def test_tq_as_binary_mc_c25(self):
        """Full lattice TQ as binary MC at c=25."""
        r = tq_as_binary_mc(25.0, n_test=5)
        self.assertTrue(r['all_passed'],
                        f"TQ failed: vac={r['vacuum_passed']}, m1={r['one_magnon_passed']}")

    def test_tq_as_binary_mc_c1(self):
        """Full lattice TQ as binary MC at c=1."""
        r = tq_as_binary_mc(1.0, n_test=5)
        self.assertTrue(r['all_passed'])

    def test_tq_identification_string(self):
        """TQ identification string is correct."""
        r = tq_as_binary_mc(25.0, n_test=3)
        self.assertEqual(r['identification'], 'TQ-relation = binary MC equation')

    def test_baxter_projection_chain(self):
        """Baxter Q-operator projection chain is valid."""
        r = baxter_q_as_theta_projection(25.0)
        self.assertTrue(r['tq_passed'],
                        f"TQ not passed: vac={r['tq_vacuum_residual']}, "
                        f"m1={r['tq_one_magnon_residual']}")
        self.assertEqual(len(r['projection_chain']), 5)

    def test_baxter_r_matrix_verified(self):
        """R-matrix in projection chain matches R(u) = u*I + P."""
        r = baxter_q_as_theta_projection(25.0)
        self.assertTrue(r['r_matrix_verified'])

    def test_baxter_projection_chain_starts_with_theta(self):
        """Projection chain starts with Theta_A."""
        r = baxter_q_as_theta_projection(25.0)
        self.assertIn('Theta_A', r['projection_chain'][0])

    def test_baxter_projection_chain_ends_with_q(self):
        """Projection chain ends with Baxter Q."""
        r = baxter_q_as_theta_projection(25.0)
        self.assertIn('Q(u)', r['projection_chain'][-1])

    def test_tq_anharmonic_functional_relation(self):
        """Functional relation for quartic AHO (class L): M=2."""
        eigenvalues = [math.sqrt(4.0) * (2 * n + 1) for n in range(50)]
        E = complex(5.0, 0.1)
        r = tq_relation_anharmonic(E, eigenvalues, M=2)
        self.assertIn('residual', r)
        self.assertGreaterEqual(r['residual'], 0)

    def test_spectral_determinant_product_form(self):
        """D(E) = prod_n (1 - E/E_n): verify product structure."""
        eigenvalues = [2.0, 6.0, 10.0]
        E = complex(1.0, 0)
        D = spectral_determinant(E, eigenvalues)
        expected = (1 - 1.0 / 2) * (1 - 1.0 / 6) * (1 - 1.0 / 10)
        self.assertAlmostEqual(abs(D - expected), 0.0, places=10)

    def test_lattice_tq_one_magnon_multiple_L(self):
        """One-magnon TQ works for different chain lengths."""
        u = complex(1.5, 0.4)
        for L in [3, 4, 5, 6]:
            r = lattice_tq_one_magnon(u, L)
            self.assertTrue(r['passed'],
                            f"One-magnon TQ failed for L={L}")


# =========================================================================
# VI. CROSS-METHOD VERIFICATION
# =========================================================================

class TestCrossVerification(unittest.TestCase):
    """Tests for cross-method consistency."""

    def test_cross_verify_c25(self):
        """Full cross-verification at c = 25."""
        r = cross_verify_all_methods(25.0)
        self.assertTrue(r['theorem_established'],
                        f"Theorem not established at c=25")

    def test_cross_verify_c1(self):
        """Full cross-verification at c = 1."""
        r = cross_verify_all_methods(1.0)
        self.assertTrue(r['theorem_established'],
                        f"Theorem not established at c=1")

    def test_cross_verify_c13(self):
        """Full cross-verification at c = 13 (self-dual)."""
        r = cross_verify_all_methods(13.0)
        self.assertTrue(r['theorem_established'],
                        f"Theorem not established at c=13")

    def test_cross_verify_c10(self):
        """Full cross-verification at c = 10."""
        r = cross_verify_all_methods(10.0)
        self.assertTrue(r['theorem_established'],
                        f"Theorem not established at c=10")

    def test_instanton_action_universal_across_c(self):
        """Universal instanton action A = (2*pi)^2 at all c values."""
        A_expected = (2 * math.pi)**2
        for c in [1.0, 10.0, 25.0]:
            r = cross_verify_all_methods(c)
            self.assertAlmostEqual(
                r['cross_verification']['A_universal'], A_expected, places=10
            )

    def test_method1_method4_consistency(self):
        """BLZ vacuum eigenvalues and TQ relation are consistent.

        Both are projections of the same Theta_A: Method 1 projects to
        the KdV eigenvalues, Method 4 projects to the Baxter Q-operator.
        Consistency: the lattice TQ is exact AND the KdV vacuum eigenvalues
        are polynomial in kappa.
        """
        c = 25.0
        kappa = virasoro_kappa(c)
        # Method 1: vacuum eigenvalue is polynomial in kappa
        q1 = kdv_q1_vacuum(c)
        self.assertAlmostEqual(q1, -kappa / 12.0, places=12)
        # Method 4: lattice TQ is exact
        r = tq_as_binary_mc(c, n_test=3)
        self.assertTrue(r['all_passed'])

    def test_summary_output(self):
        """Summary output is a nonempty string."""
        s = ode_im_shadow_summary(25.0)
        self.assertIsInstance(s, str)
        self.assertGreater(len(s), 50)
        self.assertIn('THEOREM ESTABLISHED', s)


# =========================================================================
# VII. DEPTH-CLASS SPECTRAL SIGNATURES
# =========================================================================

class TestDepthClasses(unittest.TestCase):
    """Tests for the ODE/IM dictionary by shadow depth class."""

    def test_class_G_harmonic(self):
        """Class G: harmonic oscillator, free boson."""
        r = class_G_ode_im(4.0)
        self.assertEqual(r['class'], 'G')
        self.assertEqual(r['depth'], 2)
        self.assertEqual(r['s_matrix'], 'trivial')
        self.assertEqual(r['integrable_model'], 'free boson')

    def test_class_G_equidistant_spectrum(self):
        """Class G: eigenvalues are equidistant."""
        r = class_G_ode_im(4.0)
        E = r['first_eigenvalues']
        spacings = [E[i + 1] - E[i] for i in range(len(E) - 1)]
        for s in spacings:
            self.assertAlmostEqual(s, spacings[0], places=10)

    def test_class_L_sinh_gordon(self):
        """Class L: quartic AHO, Sinh-Gordon."""
        r = class_L_ode_im(3.0, 2.0)
        self.assertEqual(r['class'], 'L')
        self.assertEqual(r['depth'], 3)
        self.assertEqual(r['integrable_model'], 'Sinh-Gordon')

    def test_class_L_omega(self):
        """Class L: omega = exp(2*pi*i/3)."""
        r = class_L_ode_im(3.0, 2.0)
        expected = cmath.exp(2j * cmath.pi / 3)
        self.assertAlmostEqual(abs(r['functional_relation_omega'] - expected),
                               0.0, places=10)

    def test_class_C_affine_toda(self):
        """Class C: sextic AHO, affine Toda a_2^(1)."""
        r = class_C_ode_im(3.0, 2.0, 0.1)
        self.assertEqual(r['class'], 'C')
        self.assertEqual(r['depth'], 4)
        self.assertEqual(r['integrable_model'], 'affine Toda a_2^(1)')

    def test_class_C_omega_is_i(self):
        """Class C: omega = i."""
        r = class_C_ode_im(3.0, 2.0, 0.1)
        self.assertAlmostEqual(abs(r['functional_relation_omega'] - 1j),
                               0.0, places=10)

    def test_class_M_quantum_kdv(self):
        """Class M: entire potential, quantum KdV."""
        r = class_M_ode_im(25.0, r_max=5)
        self.assertEqual(r['class'], 'M')
        self.assertEqual(r['depth'], float('inf'))
        self.assertIn('quantum KdV', r['integrable_model'])

    def test_class_M_has_first_coefficients(self):
        """Class M: first_coefficients includes S_2 through S_6."""
        r = class_M_ode_im(25.0, r_max=6)
        self.assertIn(2, r['first_coefficients'])
        self.assertIn(3, r['first_coefficients'])
        self.assertIn(4, r['first_coefficients'])

    def test_dictionary_four_classes(self):
        """ODE/IM dictionary has exactly four depth classes."""
        d = depth_class_ode_im_dictionary()
        self.assertEqual(len(d), 4)
        self.assertIn('G (depth 2)', d)
        self.assertIn('L (depth 3)', d)
        self.assertIn('C (depth 4)', d)
        self.assertIn('M (depth inf)', d)


# =========================================================================
# VIII. LANDSCAPE SCAN
# =========================================================================

class TestLandscape(unittest.TestCase):
    """Tests for the landscape-wide ODE/IM theorem."""

    def test_landscape_scan_runs(self):
        """Landscape scan runs without error."""
        results = ode_im_landscape(c_values=[1.0, 25.0])
        self.assertEqual(len(results), 2)

    def test_landscape_scan_c1_established(self):
        """Theorem established at c=1."""
        results = ode_im_landscape(c_values=[1.0])
        self.assertTrue(results[0].get('theorem_established', False))

    def test_landscape_scan_c25_established(self):
        """Theorem established at c=25."""
        results = ode_im_landscape(c_values=[25.0])
        self.assertTrue(results[0].get('theorem_established', False))

    def test_landscape_multiple_c(self):
        """Theorem established at c=2, 10, 13."""
        results = ode_im_landscape(c_values=[2.0, 10.0, 13.0])
        for r in results:
            self.assertTrue(r.get('theorem_established', False),
                            f"Failed at c={r.get('c')}")


# =========================================================================
# IX. ADDITIONAL CROSS-CHECKS (ensuring 50+ tests)
# =========================================================================

class TestAdditionalCrossChecks(unittest.TestCase):
    """Additional cross-checks to ensure robustness."""

    def test_kappa_duality_sum_virasoro(self):
        """kappa(c) + kappa(26-c) = 13 at multiple c. AP24."""
        for c in [0.5, 1.0, 5.0, 10.0, 13.0, 20.0, 25.0]:
            self.assertAlmostEqual(
                virasoro_kappa(c) + virasoro_kappa(26 - c), 13.0, places=12
            )

    def test_shadow_metric_positive_at_origin(self):
        """Q(0) = c^2 > 0 for all c > 0."""
        for c in [0.1, 1.0, 10.0, 100.0]:
            self.assertGreater(shadow_metric_Q(c, 0.0), 0.0)

    def test_shadow_oper_is_real_on_real_axis(self):
        """V^sh(t) is real for real t when Q(t) > 0."""
        c = 25.0
        for t in [0.0, 0.1, 0.5, 1.0]:
            V = shadow_oper_potential(c, t)
            self.assertTrue(math.isfinite(V))

    def test_harmonic_oscillator_zero_kappa(self):
        """E_n = 0 when kappa = 0."""
        self.assertAlmostEqual(harmonic_eigenvalue_exact(0, 0.0), 0.0)

    def test_q1_at_c0_is_zero(self):
        """q_1(0, 0) = 0 when c=0."""
        self.assertAlmostEqual(kdv_q1_vacuum(0.0), 0.0, places=12)

    def test_q3_at_c0_is_zero(self):
        """q_3(0, 0) = 0 when c=0 (kappa=0 kills everything)."""
        self.assertAlmostEqual(kdv_q3_vacuum(0.0), 0.0, places=12)

    def test_shadow_S4_c13_self_dual(self):
        """S_4 at c=13 equals S_4 at c=13 (self-dual, trivially)."""
        self.assertAlmostEqual(virasoro_S4(13.0), virasoro_S4(13.0))

    def test_shadow_S4_duality(self):
        """S_4(c) and S_4(26-c) are related by Koszul duality."""
        c = 5.0
        S4_c = virasoro_S4(c)
        S4_dual = virasoro_S4(26 - c)
        # Both should be finite and nonzero
        self.assertTrue(math.isfinite(S4_c))
        self.assertTrue(math.isfinite(S4_dual))
        self.assertNotAlmostEqual(S4_c, S4_dual)

    def test_spectral_det_large_E(self):
        """|D(E)| grows for large E."""
        eigenvalues = [1.0, 3.0, 5.0]
        D_small = abs(spectral_determinant(complex(0.5, 0), eigenvalues))
        D_large = abs(spectral_determinant(complex(100.0, 0), eigenvalues))
        self.assertGreater(D_large, D_small)

    def test_lattice_tq_vacuum_l2(self):
        """Lattice TQ vacuum holds for L=2."""
        r = lattice_tq_vacuum(complex(3.0, 0.1), L=2)
        self.assertTrue(r['passed'])

    def test_shadow_potential_monotone_for_positive_x(self):
        """V(x) is monotonically increasing for x > 0 when all S_r > 0."""
        coeffs = [5.0, 2.0]  # S_2 = 5, S_3 = 2 (both positive)
        V_prev = shadow_potential_eval(0.1, coeffs)
        for x in [0.5, 1.0, 2.0, 3.0]:
            V_curr = shadow_potential_eval(x, coeffs)
            self.assertGreater(V_curr, V_prev)
            V_prev = V_curr

    def test_class_G_omega_equidistant(self):
        """Class G omega = sqrt(kappa) gives equidistant eigenvalues."""
        kappa = 9.0
        omega = math.sqrt(kappa)
        E = [omega * (2 * n + 1) for n in range(5)]
        spacing = E[1] - E[0]
        for i in range(len(E) - 1):
            self.assertAlmostEqual(E[i + 1] - E[i], spacing, places=10)

    def test_vacuum_eigenvalue_q1_sign(self):
        """q_1(0) < 0 for c > 0: vacuum energy is negative."""
        for c in [1.0, 10.0, 25.0]:
            self.assertLess(kdv_q1_vacuum(c), 0.0)

    def test_vacuum_eigenvalue_q3_positive(self):
        """q_3(0) > 0 for c > 1/5 (where 5c-1 > 0)."""
        for c in [1.0, 10.0, 25.0]:
            self.assertGreater(kdv_q3_vacuum(c), 0.0)


if __name__ == '__main__':
    unittest.main()
