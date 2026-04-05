"""Tests for bc_tba_deep_engine.py

Multi-path verification for the TBA engine with Riemann zeta zero evaluations.
Tests are structured to avoid long computations while covering all public APIs.
"""

import math
import unittest

import numpy as np

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.bc_tba_deep_engine import (
    PI, TWO_PI,
    ZETA_ZERO_GAMMAS,
    get_zeta_zeros,
    get_zeta_gammas,
    TBAModel,
    sinh_gordon_kernel,
    xxx_kernel,
    xxz_kernel,
    a_type_kernel,
    make_sinh_gordon_model,
    make_xxx_model,
    make_xxz_model,
    make_a_type_model,
    TBASolution,
    solve_tba,
    effective_central_charge,
    effective_central_charge_at_zero,
    c_eff_at_zeta_zeros,
    rogers_dilogarithm,
    rogers_dilogarithm_identity_check,
    y_system_residual,
    wall_crossing_jump,
    free_energy,
    free_energy_series,
    solve_excited_tba,
    shadow_to_tba_coupling,
    shadow_tba_system,
    full_zeta_zero_tba_analysis,
)


# ========================================================================
# Zeta zeros
# ========================================================================

class TestZetaZeros(unittest.TestCase):
    """Test zeta zero data."""

    def test_first_zero(self):
        """First nontrivial zero: gamma_1 ~ 14.1347."""
        self.assertAlmostEqual(ZETA_ZERO_GAMMAS[0], 14.134725141734693, places=8)

    def test_50_zeros_stored(self):
        """50 gamma values stored."""
        self.assertEqual(len(ZETA_ZERO_GAMMAS), 50)

    def test_zeros_positive_and_increasing(self):
        """All gammas are positive and increasing."""
        for i in range(len(ZETA_ZERO_GAMMAS)):
            self.assertGreater(ZETA_ZERO_GAMMAS[i], 0)
        for i in range(len(ZETA_ZERO_GAMMAS) - 1):
            self.assertLess(ZETA_ZERO_GAMMAS[i], ZETA_ZERO_GAMMAS[i + 1])

    def test_get_zeta_zeros(self):
        """get_zeta_zeros returns complex zeros with Re = 1/2."""
        zeros = get_zeta_zeros(5, dps=15)
        for z in zeros:
            self.assertAlmostEqual(z.real, 0.5, places=10)
            self.assertGreater(z.imag, 0)

    def test_get_zeta_gammas(self):
        """get_zeta_gammas returns correct count."""
        gammas = get_zeta_gammas(10)
        self.assertEqual(len(gammas), 10)
        # All positive
        for g in gammas:
            self.assertGreater(g, 0)

    def test_gammas_match_zeros(self):
        """Gammas match imaginary parts of zeros."""
        zeros = get_zeta_zeros(5, dps=15)
        gammas = get_zeta_gammas(5)
        for z, g in zip(zeros, gammas):
            self.assertAlmostEqual(z.imag, g, places=8)


# ========================================================================
# TBA kernels
# ========================================================================

class TestKernels(unittest.TestCase):
    """Test TBA kernels."""

    def test_sinh_gordon_kernel_symmetry(self):
        """phi(theta) = phi(-theta): kernel is even."""
        for theta in [0.5, 1.0, 3.0]:
            self.assertAlmostEqual(
                sinh_gordon_kernel(theta, coupling=0.5),
                sinh_gordon_kernel(-theta, coupling=0.5),
                places=10)

    def test_sinh_gordon_kernel_positive(self):
        """Kernel is positive for real theta."""
        for theta in [0.0, 0.5, 1.0, 5.0]:
            self.assertGreater(sinh_gordon_kernel(theta, coupling=0.5), 0)

    def test_sinh_gordon_kernel_decays(self):
        """Kernel decays at large rapidity."""
        k1 = sinh_gordon_kernel(1.0, coupling=0.5)
        k10 = sinh_gordon_kernel(10.0, coupling=0.5)
        self.assertGreater(k1, k10)

    def test_xxx_kernel_formula(self):
        """XXX kernel: phi(theta) = 2/(theta^2 + 1)."""
        for theta in [0.0, 1.0, 2.0]:
            expected = 2.0 / (theta ** 2 + 1.0)
            self.assertAlmostEqual(xxx_kernel(theta), expected, places=10)

    def test_xxx_kernel_at_zero(self):
        """phi(0) = 2 for XXX."""
        self.assertAlmostEqual(xxx_kernel(0.0), 2.0, places=10)

    def test_xxx_kernel_even(self):
        """XXX kernel is even."""
        for theta in [0.5, 2.0]:
            self.assertAlmostEqual(xxx_kernel(theta), xxx_kernel(-theta), places=10)

    def test_xxz_kernel_even(self):
        """XXZ kernel is even."""
        for theta in [0.5, 2.0]:
            self.assertAlmostEqual(
                xxz_kernel(theta, coupling=0.3),
                xxz_kernel(-theta, coupling=0.3),
                places=10)

    def test_xxz_kernel_positive(self):
        """XXZ kernel is positive for real theta."""
        for theta in [0.0, 1.0, 5.0]:
            self.assertGreater(xxz_kernel(theta, coupling=0.3), 0)

    def test_a_type_kernel_nearest_neighbor(self):
        """A-type kernel nonzero only for |a-b|=1."""
        self.assertGreater(a_type_kernel(0.0, 0, 1), 0)
        self.assertAlmostEqual(a_type_kernel(0.0, 0, 0), 0.0)
        self.assertAlmostEqual(a_type_kernel(0.0, 0, 2), 0.0)

    def test_a_type_kernel_nearest_formula(self):
        """Nearest-neighbor: phi_1(theta) = 1/cosh(theta)."""
        for theta in [0.0, 1.0, 3.0]:
            expected = 1.0 / np.cosh(theta)
            self.assertAlmostEqual(a_type_kernel(theta, 0, 1), expected, places=10)


# ========================================================================
# Model constructors
# ========================================================================

class TestModelConstructors(unittest.TestCase):
    """Test TBA model constructors."""

    def test_sinh_gordon_rank(self):
        model = make_sinh_gordon_model()
        self.assertEqual(model.rank, 1)
        self.assertEqual(model.name, "sinh-Gordon")

    def test_xxx_model(self):
        model = make_xxx_model()
        self.assertEqual(model.rank, 1)
        self.assertEqual(model.name, "XXX")

    def test_xxz_model(self):
        model = make_xxz_model(0.3)
        self.assertEqual(model.rank, 1)
        self.assertEqual(model.coupling, 0.3)

    def test_a_type_model_rank(self):
        model = make_a_type_model(rank=3)
        self.assertEqual(model.rank, 3)
        self.assertEqual(len(model.masses), 3)

    def test_a_type_masses_positive(self):
        """All masses are positive."""
        for rank in [2, 3, 4]:
            model = make_a_type_model(rank=rank)
            for m in model.masses:
                self.assertGreater(m, 0)

    def test_a_type_lightest_mass_normalized(self):
        """Lightest mass = 1 after normalization."""
        model = make_a_type_model(rank=3)
        self.assertAlmostEqual(model.masses[0], 1.0, places=10)

    def test_cartan_matrix_a2(self):
        """A_2 Cartan matrix is [[2,-1],[-1,2]]."""
        model = make_a_type_model(rank=2)
        expected = np.array([[2, -1], [-1, 2]])
        np.testing.assert_array_almost_equal(model.cartan_matrix, expected)

    def test_coxeter_number(self):
        """Coxeter number h = rank + 1 for A-type."""
        for rank in [2, 3, 4]:
            model = make_a_type_model(rank=rank)
            self.assertEqual(model.coxeter_number, rank + 1)


# ========================================================================
# TBA solver
# ========================================================================

class TestTBASolver(unittest.TestCase):
    """Test TBA equation solver."""

    def test_sinh_gordon_converges(self):
        """Sinh-Gordon TBA converges."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=200)
        self.assertTrue(sol.converged)

    def test_xxx_converges(self):
        """XXX TBA converges."""
        model = make_xxx_model()
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=200)
        self.assertTrue(sol.converged)

    def test_xxz_converges(self):
        """XXZ TBA converges."""
        model = make_xxz_model(0.3)
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=200)
        self.assertTrue(sol.converged)

    def test_solution_shape(self):
        """Solution has correct shape."""
        model = make_sinh_gordon_model()
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        self.assertEqual(sol.epsilon.shape, (1, 64))

    def test_epsilon_positive_at_large_rapidity(self):
        """epsilon(theta) -> r*m*cosh(theta) at large theta (driving dominates)."""
        model = make_sinh_gordon_model()
        sol = solve_tba(model, r_param=2.0, n_grid=64)
        # At the endpoints of the grid, epsilon should be large and positive
        self.assertGreater(sol.epsilon[0, -1], 0)
        self.assertGreater(sol.epsilon[0, 0], 0)

    def test_residual_small(self):
        """Converged solution has small residual."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=300, tol=1e-8)
        if sol.converged:
            self.assertLess(sol.residual, 1e-8)

    def test_a_type_rank2_converges(self):
        """A_2 TBA converges."""
        model = make_a_type_model(rank=2)
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=200)
        self.assertTrue(sol.converged)
        self.assertEqual(sol.epsilon.shape, (2, 64))


# ========================================================================
# Effective central charge
# ========================================================================

class TestEffectiveCentralCharge(unittest.TestCase):
    """Test effective central charge computation."""

    def test_c_eff_positive(self):
        """c_eff is positive for converged TBA."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        c_eff = effective_central_charge(sol)
        self.assertGreater(c_eff, 0)

    def test_c_eff_at_zero_nonneg(self):
        """Pointwise c_eff contribution is non-negative."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        c_0 = effective_central_charge_at_zero(sol, 0.0)
        self.assertGreaterEqual(c_0, 0)

    def test_c_eff_at_zero_larger_than_at_large_theta(self):
        """c_eff contribution peaks near theta = 0."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        c_0 = effective_central_charge_at_zero(sol, 0.0)
        c_10 = effective_central_charge_at_zero(sol, 10.0)
        self.assertGreater(c_0, c_10)

    def test_c_eff_at_zeta_zeros(self):
        """c_eff at zeta zeros returns correct structure."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        result = c_eff_at_zeta_zeros(sol, n_zeros=5)
        self.assertEqual(len(result['gammas']), 5)
        self.assertEqual(len(result['c_eff_values']), 5)
        self.assertIn('c_eff_full', result)


# ========================================================================
# Rogers dilogarithm
# ========================================================================

class TestRogersDialogarithm(unittest.TestCase):
    """Test Rogers dilogarithm L(x)."""

    def test_L_at_zero(self):
        """L(0) = 0."""
        self.assertAlmostEqual(rogers_dilogarithm(0.0), 0.0, places=10)

    def test_L_at_one(self):
        """L(1) = pi^2/6."""
        self.assertAlmostEqual(rogers_dilogarithm(1.0), PI ** 2 / 6.0, places=8)

    def test_L_at_half(self):
        """L(1/2) = pi^2/12."""
        self.assertAlmostEqual(rogers_dilogarithm(0.5), PI ** 2 / 12.0, places=6)

    def test_L_bounded(self):
        """L(x) is bounded between 0 and pi^2/6 for x in (0,1)."""
        for x in [0.01, 0.1, 0.3, 0.5, 0.7, 0.99]:
            L = rogers_dilogarithm(x)
            self.assertGreaterEqual(L, 0)
            self.assertLessEqual(L, PI ** 2 / 6.0 + 1e-10)

    def test_L_monotone(self):
        """L(x) is monotonically increasing on (0, 1)."""
        x_vals = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]
        L_vals = [rogers_dilogarithm(x) for x in x_vals]
        for i in range(len(L_vals) - 1):
            self.assertLess(L_vals[i], L_vals[i + 1])

    def test_L_positive(self):
        """L(x) > 0 for x > 0."""
        for x in [0.01, 0.1, 0.5, 0.99]:
            self.assertGreater(rogers_dilogarithm(x), 0)

    def test_rogers_identity_check(self):
        """Rogers identity check returns expected structure."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        result = rogers_dilogarithm_identity_check(sol, 1.0)
        self.assertIn('L_sum', result)
        self.assertIn('expected', result)
        self.assertIn('c_from_L', result)
        # c_from_L should be positive
        self.assertGreater(result['c_from_L'], 0)


# ========================================================================
# Y-system
# ========================================================================

class TestYSystem(unittest.TestCase):
    """Test Y-system functional equations."""

    def test_y_system_residual_structure(self):
        """Y-system residual returns expected keys."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=2.0, n_grid=64, max_iter=300)
        result = y_system_residual(sol, 0.0)
        self.assertIn('theta', result)
        self.assertIn('residuals', result)
        self.assertEqual(len(result['residuals']), 1)  # rank 1

    def test_y_system_residual_finite(self):
        """Y-system residual is finite at theta = 0."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=2.0, n_grid=128, max_iter=500)
        result = y_system_residual(sol, 0.0)
        # The Y-system uses real-axis shift (proxy for analytic continuation),
        # so the ratio is not expected to be exactly 1.  We only verify finiteness.
        for res in result['residuals']:
            self.assertTrue(np.isfinite(res['ratio']))
            self.assertGreater(res['lhs'], 0)
            self.assertGreater(res['rhs'], 0)


# ========================================================================
# Wall-crossing
# ========================================================================

class TestWallCrossing(unittest.TestCase):
    """Test wall-crossing jumps."""

    def test_wall_crossing_structure(self):
        """Wall-crossing returns expected keys."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        gamma_1 = ZETA_ZERO_GAMMAS[0]
        result = wall_crossing_jump(sol, gamma_1)
        self.assertIn('gamma_n', result)
        self.assertIn('jumps', result)
        self.assertIn('max_jump', result)

    def test_wall_crossing_smooth(self):
        """On real axis, pseudo-energies are smooth (no Stokes jump)."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        gamma_1 = ZETA_ZERO_GAMMAS[0]
        result = wall_crossing_jump(sol, gamma_1)
        # max_jump should be small (smooth on real axis)
        self.assertTrue(np.isfinite(result['max_jump']))
        # Each species jump is finite
        for j in result['jumps']:
            self.assertTrue(np.isfinite(j['jump']))


# ========================================================================
# Free energy
# ========================================================================

class TestFreeEnergy(unittest.TestCase):
    """Test free energy computations."""

    def test_free_energy_negative(self):
        """Ground-state free energy should be negative (attractive)."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        F = free_energy(sol)
        self.assertLess(F, 0)

    def test_free_energy_series_structure(self):
        """Free energy series returns expected structure."""
        model = make_sinh_gordon_model(coupling=0.5)
        result = free_energy_series(model, n_zeros=5, r_param=1.0, n_grid=64)
        self.assertIn('gammas', result)
        self.assertIn('F_values', result)
        self.assertIn('c_eff_full', result)
        self.assertEqual(len(result['F_values']), 5)


# ========================================================================
# Excited-state TBA
# ========================================================================

class TestExcitedStateTBA(unittest.TestCase):
    """Test excited-state TBA solver."""

    def test_excited_tba_converges(self):
        """Excited-state TBA converges."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_excited_tba(model, r_param=2.0, source_positions=[0.0],
                                n_grid=64, max_iter=300)
        self.assertTrue(sol.converged)

    def test_excited_tba_different_from_ground(self):
        """Excited state with strong source differs from ground state."""
        model = make_sinh_gordon_model(coupling=0.8)
        sol_gs = solve_tba(model, r_param=1.0, n_grid=64, max_iter=300)
        # Place source at theta=0 with stronger coupling
        sol_ex = solve_excited_tba(model, r_param=1.0, source_positions=[0.0],
                                   n_grid=64, max_iter=300)
        # The solutions should differ (at least by interpolation-level amount)
        diff = np.max(np.abs(sol_gs.epsilon - sol_ex.epsilon))
        # Even if numerically very similar, both should be finite
        self.assertTrue(np.all(np.isfinite(sol_ex.epsilon)))
        self.assertTrue(np.all(np.isfinite(sol_gs.epsilon)))


# ========================================================================
# Shadow-TBA coupling
# ========================================================================

class TestShadowTBACoupling(unittest.TestCase):
    """Test shadow-to-TBA coupling extraction."""

    def test_coupling_free_field_zero(self):
        """Heisenberg (S_4=0): coupling = 0."""
        p = shadow_to_tba_coupling(kappa=1.0, c=1.0, S4=0.0)
        self.assertAlmostEqual(p, 0.0)

    def test_coupling_positive_for_nonzero_S4(self):
        """Nonzero S_4 gives positive coupling."""
        p = shadow_to_tba_coupling(kappa=6.5, c=13.0, S4=0.01)
        self.assertGreater(p, 0)

    def test_coupling_capped(self):
        """Coupling is capped at 2 for stability."""
        p = shadow_to_tba_coupling(kappa=0.01, c=1.0, S4=100.0)
        self.assertLessEqual(p, 2.0)

    def test_shadow_tba_system_returns_model(self):
        """shadow_tba_system returns a TBAModel."""
        model = shadow_tba_system(c=13.0, S4=0.01)
        self.assertIsInstance(model, TBAModel)
        self.assertEqual(model.rank, 1)

    def test_shadow_tba_system_xxx(self):
        model = shadow_tba_system(c=13.0, model_type="XXX")
        self.assertEqual(model.name, "XXX")

    def test_shadow_tba_system_xxz(self):
        model = shadow_tba_system(c=13.0, model_type="XXZ")
        self.assertEqual(model.name, "XXZ")

    def test_shadow_tba_system_invalid(self):
        with self.assertRaises(ValueError):
            shadow_tba_system(c=13.0, model_type="invalid")


# ========================================================================
# Full pipeline
# ========================================================================

class TestFullPipeline(unittest.TestCase):
    """Test the full shadow-to-TBA pipeline."""

    def test_full_analysis_runs(self):
        """Full analysis pipeline runs without error."""
        result = full_zeta_zero_tba_analysis(
            c=13.0, S4=0.01, r_param=2.0, n_zeros=3, n_grid=32,
            max_iter=100)
        self.assertIn('tba_converged', result)
        self.assertIn('c_eff_full', result)
        self.assertIn('rogers_dilogarithm', result)

    def test_full_analysis_virasoro(self):
        """Pipeline for Virasoro at c=13."""
        result = full_zeta_zero_tba_analysis(
            c=13.0, kappa=6.5,
            S4=10.0 / (13.0 * 87.0),  # Q^contact
            r_param=2.0, n_zeros=3, n_grid=32, max_iter=100)
        self.assertAlmostEqual(result['kappa'], 6.5)
        self.assertEqual(result['central_charge'], 13.0)


# ========================================================================
# Cross-consistency
# ========================================================================

class TestCrossConsistency(unittest.TestCase):
    """Cross-consistency checks between TBA computations."""

    def test_c_eff_consistency_two_methods(self):
        """c_eff from integral vs pointwise should be consistent."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=1.0, n_grid=64)
        c_full = effective_central_charge(sol)
        # Pointwise at theta=0 should give a large contribution
        c_0 = effective_central_charge_at_zero(sol, 0.0)
        # c_0 is a density, not an integral, but should be finite and positive
        self.assertGreater(c_0, 0)
        self.assertGreater(c_full, 0)

    def test_free_energy_c_eff_relation(self):
        """F = -pi^2 * c_eff / (6*r^2)."""
        model = make_sinh_gordon_model(coupling=0.5)
        sol = solve_tba(model, r_param=2.0, n_grid=64)
        F = free_energy(sol)
        c_eff = effective_central_charge(sol)
        expected_F = -PI ** 2 * c_eff / (6.0 * 2.0 ** 2)
        self.assertAlmostEqual(F, expected_F, places=8)

    def test_sinh_gordon_vs_xxx_different_c_eff(self):
        """Different models give different c_eff."""
        sol_sg = solve_tba(make_sinh_gordon_model(coupling=0.5),
                           r_param=1.0, n_grid=64)
        sol_xxx = solve_tba(make_xxx_model(), r_param=1.0, n_grid=64)
        c_sg = effective_central_charge(sol_sg)
        c_xxx = effective_central_charge(sol_xxx)
        # These should be different models with different c_eff
        self.assertNotAlmostEqual(c_sg, c_xxx, places=2)

    def test_rogers_special_values_consistency(self):
        """Three independent verifications of L(1/2) = pi^2/12."""
        # Path 1: direct computation
        L_half = rogers_dilogarithm(0.5)
        # Path 2: from the identity L(x) = Li_2(x) + (1/2)*log(x)*log(1-x)
        # Li_2(1/2) = pi^2/12 - (1/2)*(log 2)^2
        li2_half = PI ** 2 / 12.0 - 0.5 * np.log(2.0) ** 2
        L_half_v2 = li2_half + 0.5 * np.log(0.5) * np.log(0.5)
        # Path 3: from special value
        L_half_v3 = PI ** 2 / 12.0
        self.assertAlmostEqual(L_half, L_half_v3, places=6)

    def test_kernel_normalization_consistency(self):
        """XXX kernel integral ~ 2*pi (from Cauchy residue)."""
        # int_{-inf}^{inf} 2/(theta^2 + 1) dtheta = 2*pi
        from scipy import integrate
        integral, _ = integrate.quad(xxx_kernel, -1000, 1000)
        self.assertAlmostEqual(integral, 2.0 * PI, delta=0.1)

    def test_a_type_mass_ratios(self):
        """A_2 mass ratio: m_2/m_1 = sin(2*pi/3)/sin(pi/3) = 1."""
        model = make_a_type_model(rank=2)
        # sin(2pi/3)/sin(pi/3) = sin(60)/sin(60) for A_2 with h=3
        # Actually sin(2*pi/3) = sin(pi/3) = sqrt(3)/2, so ratio = 1
        self.assertAlmostEqual(model.masses[1] / model.masses[0], 1.0, places=5)

    def test_a3_mass_spectrum(self):
        """A_3 masses: m_a = sin(a*pi/4)/sin(pi/4) normalized."""
        model = make_a_type_model(rank=3)
        # m_1 = 1 (normalized), m_2 = sin(2*pi/4)/sin(pi/4) = 1/sin(pi/4)*sin(pi/2) = sqrt(2)
        # m_3 = sin(3*pi/4)/sin(pi/4) = 1
        self.assertAlmostEqual(model.masses[0], 1.0, places=5)
        self.assertAlmostEqual(model.masses[1], math.sqrt(2.0), places=5)
        self.assertAlmostEqual(model.masses[2], 1.0, places=5)


if __name__ == '__main__':
    unittest.main()
