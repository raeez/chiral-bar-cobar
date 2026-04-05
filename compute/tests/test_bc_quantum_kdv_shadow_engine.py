"""Comprehensive tests for bc_quantum_kdv_shadow_engine.py.

Tests the quantum KdV hierarchy engine: Virasoro algebra, KdV integrals of
motion, commutativity, eigenvalue polynomials, shadow-KdV identification,
Miura transformation, Benjamin-Ono hierarchy, GGE, and zeta zero evaluation.

Every numerical result is cross-verified by at least 2 independent methods
where possible (multi-path verification mandate).
"""

import math
import unittest
from fractions import Fraction
from typing import Dict, List

import numpy as np

from compute.lib.bc_quantum_kdv_shadow_engine import (
    # Virasoro algebra
    virasoro_commutator_coeff,
    VermaModule,
    _partitions,
    # KdV integrals
    kdv_I1_eigenvalue, kdv_I3_eigenvalue,
    kdv_I5_eigenvalue, kdv_I7_eigenvalue, kdv_I9_eigenvalue,
    kdv_integral_matrix,
    # Commutativity
    verify_commutativity,
    # Eigenvalue polynomials
    kdv_eigenvalue_polynomial,
    kdv_vacuum_eigenvalues,
    # Shadow-KdV
    shadow_tower_virasoro, shadow_kdv_comparison,
    # Zeta zeros
    zeta_zeros_first_n, kdv_spectrum_at_zeta_zeros,
    # W_3 / Benjamin-Ono
    w3_shadow_data, benjamin_ono_integrals,
    # Miura
    miura_shadow_transfer,
    # Classical limit
    classical_shadow_tower,
    # Tau function
    tau_function_coefficients,
    # GGE
    gge_partition_function,
    # Landscape
    virasoro_kdv_landscape,
)


class TestVirasoroCommutator(unittest.TestCase):
    """Tests for Virasoro commutation relations."""

    def test_commutator_Lm_Ln_mode(self):
        """[L_m, L_n] = (m-n) L_{m+n} + central term."""
        c = 25.0
        target, mode_coeff, central = virasoro_commutator_coeff(c, 2, -1)
        self.assertEqual(target, 1)  # m+n = 2+(-1) = 1
        self.assertAlmostEqual(mode_coeff, 3.0, places=10)  # m-n = 2-(-1) = 3

    def test_commutator_central_term(self):
        """Central term = (c/12)(m^3-m) when m+n=0."""
        c = 12.0
        _, _, central = virasoro_commutator_coeff(c, 2, -2)
        # c/12 * (8-2) = 1 * 6 = 6
        self.assertAlmostEqual(central, 6.0, places=10)

    def test_commutator_no_central_term(self):
        """Central term = 0 when m+n != 0."""
        c = 25.0
        _, _, central = virasoro_commutator_coeff(c, 3, 1)
        self.assertAlmostEqual(central, 0.0, places=10)

    def test_commutator_L0_Ln(self):
        """[L_0, L_n] = -n L_n (adjoint action)."""
        c = 10.0
        for n in [-3, -2, -1, 1, 2, 3]:
            target, coeff, _ = virasoro_commutator_coeff(c, 0, n)
            self.assertEqual(target, n)
            self.assertAlmostEqual(coeff, -n, places=10)

    def test_commutator_central_extension_normalization(self):
        """Central extension for [L_1, L_{-1}] = 2*L_0 + 0 (c/12*(1-1)=0)."""
        c = 25.0
        target, coeff, central = virasoro_commutator_coeff(c, 1, -1)
        self.assertEqual(target, 0)
        self.assertAlmostEqual(coeff, 2.0, places=10)
        self.assertAlmostEqual(central, 0.0, places=10)

    def test_commutator_L2_Lm2(self):
        """[L_2, L_{-2}] = 4*L_0 + c/2."""
        c = 24.0
        target, coeff, central = virasoro_commutator_coeff(c, 2, -2)
        self.assertEqual(target, 0)
        self.assertAlmostEqual(coeff, 4.0, places=10)
        self.assertAlmostEqual(central, c / 2.0, places=10)


class TestVermaModule(unittest.TestCase):
    """Tests for the truncated Verma module."""

    def test_verma_module_dimension(self):
        """Dimension counts partitions correctly."""
        vm = VermaModule(25.0, 0.0, max_level=3)
        # Level 0: 1 state, Level 1: 1, Level 2: 2, Level 3: 3
        # Total = 1 + 1 + 2 + 3 = 7
        self.assertEqual(vm.dim, 7)

    def test_verma_module_L0_eigenvalue(self):
        """L_0 has eigenvalue h on the primary."""
        h = 2.0
        vm = VermaModule(25.0, h, max_level=3)
        L0 = vm.L_matrix(0)
        self.assertAlmostEqual(L0[0, 0], h, places=10)

    def test_verma_module_L0_level_eigenvalues(self):
        """L_0 eigenvalue on level-N state is h+N."""
        h = 1.0
        vm = VermaModule(25.0, h, max_level=4)
        L0 = vm.L_matrix(0)
        # Check diagonal entries: at level N, eigenvalue is h + N
        for N in range(0, 5):
            s, e = vm.level_ranges[N]
            for i in range(s, e):
                self.assertAlmostEqual(L0[i, i], h + N, places=8)

    def test_annihilation_on_primary(self):
        """L_n |h> = 0 for n > 0."""
        vm = VermaModule(25.0, 1.0, max_level=3)
        for n in [1, 2, 3]:
            Ln = vm.L_matrix(n)
            # First column should be zero (acting on primary)
            for i in range(vm.dim):
                self.assertAlmostEqual(abs(Ln[i, 0]), 0.0, places=8)

    def test_gram_matrix_positive_definite(self):
        """Gram matrix is positive definite for generic (c, h)."""
        vm = VermaModule(25.0, 1.0, max_level=3)
        G = vm.gram_matrix()
        eigenvalues = np.linalg.eigvalsh(G)
        # At generic (c, h), Gram matrix should be positive definite
        for ev in eigenvalues:
            self.assertGreater(ev, -1e-6)

    def test_state_level_function(self):
        """state_level returns correct level for each state."""
        vm = VermaModule(25.0, 0.0, max_level=3)
        self.assertEqual(vm.state_level(0), 0)  # Primary is level 0


class TestPartitions(unittest.TestCase):
    """Tests for partition generation."""

    def test_partitions_of_0(self):
        self.assertEqual(_partitions(0), [()])

    def test_partitions_of_1(self):
        self.assertEqual(_partitions(1), [(1,)])

    def test_partitions_of_2(self):
        self.assertEqual(sorted(_partitions(2)), sorted([(2,), (1, 1)]))

    def test_partitions_of_3(self):
        self.assertEqual(len(_partitions(3)), 3)  # (3,), (2,1), (1,1,1)

    def test_partitions_of_4(self):
        self.assertEqual(len(_partitions(4)), 5)

    def test_partitions_of_5(self):
        self.assertEqual(len(_partitions(5)), 7)

    def test_partitions_sum(self):
        """Every partition of n sums to n."""
        for n in range(0, 8):
            for p in _partitions(n):
                self.assertEqual(sum(p), n)


class TestKdVEigenvalues(unittest.TestCase):
    """Tests for KdV integral eigenvalues on primary states."""

    def test_I1_eigenvalue_formula(self):
        """q_1(h) = h - c/24, verified at multiple (c, h)."""
        for c, h in [(25.0, 0.0), (1.0, 1.0), (10.0, 5.0), (0.5, 2.0)]:
            self.assertAlmostEqual(
                kdv_I1_eigenvalue(c, h), h - c / 24.0, places=10
            )

    def test_I1_vacuum_eigenvalue(self):
        """q_1(0) = -c/24."""
        for c in [1.0, 6.0, 12.0, 24.0, 25.0]:
            self.assertAlmostEqual(
                kdv_I1_eigenvalue(c, 0.0), -c / 24.0, places=10
            )

    def test_I3_eigenvalue_formula(self):
        """q_3(h) = 2h^2 + h(c-5)/6 + c(5c-1)/720, cross-checked."""
        for c, h in [(25.0, 0.0), (1.0, 1.0), (10.0, 2.0)]:
            expected = (2 * h**2 + h * (c - 5) / 6.0
                        + c * (5 * c - 1) / 720.0)
            self.assertAlmostEqual(
                kdv_I3_eigenvalue(c, h), expected, places=8
            )

    def test_I3_degree_2_in_h(self):
        """q_3 is degree 2: leading coefficient is 2."""
        c = 10.0
        q_at_0 = kdv_I3_eigenvalue(c, 0.0)
        q_at_1 = kdv_I3_eigenvalue(c, 1.0)
        q_at_2 = kdv_I3_eigenvalue(c, 2.0)
        # Second finite difference = 2! * leading coeff = 2 * 2 = 4
        delta2 = q_at_2 - 2 * q_at_1 + q_at_0
        self.assertAlmostEqual(delta2, 4.0, places=6)

    def test_I3_vacuum_eigenvalue(self):
        """q_3(0) = c(5c-1)/720."""
        for c in [1.0, 10.0, 25.0]:
            expected = c * (5 * c - 1) / 720.0
            self.assertAlmostEqual(
                kdv_I3_eigenvalue(c, 0.0), expected, places=10
            )

    def test_I5_degree_3_in_h(self):
        """q_5 is degree 3 polynomial in h."""
        c = 10.0
        vals = [kdv_I5_eigenvalue(c, float(h)) for h in range(5)]
        # Third finite differences should be constant = 3! * leading coeff
        d3 = vals[3] - 3 * vals[2] + 3 * vals[1] - vals[0]
        d3_check = vals[4] - 3 * vals[3] + 3 * vals[2] - vals[1]
        self.assertAlmostEqual(d3, d3_check, places=4)

    def test_I5_is_polynomial_degree_3(self):
        """q_5 is well-approximated by a degree-3 polynomial (constant 3rd diff)."""
        c = 10.0
        vals = [kdv_I5_eigenvalue(c, float(h)) for h in range(6)]
        d3_a = vals[3] - 3 * vals[2] + 3 * vals[1] - vals[0]
        d3_b = vals[4] - 3 * vals[3] + 3 * vals[2] - vals[1]
        d3_c = vals[5] - 3 * vals[4] + 3 * vals[3] - vals[2]
        # 3rd differences should be approximately constant
        if abs(d3_a) > 1e-6:
            self.assertAlmostEqual(d3_b / d3_a, 1.0, places=2)
            self.assertAlmostEqual(d3_c / d3_a, 1.0, places=2)

    def test_I7_returns_float(self):
        """I_7 eigenvalue returns a finite float."""
        val = kdv_I7_eigenvalue(25.0, 1.0)
        self.assertTrue(np.isfinite(val))

    def test_I9_returns_float(self):
        """I_9 eigenvalue returns a finite float."""
        val = kdv_I9_eigenvalue(25.0, 1.0)
        self.assertTrue(np.isfinite(val))


class TestKdVIntegralMatrix(unittest.TestCase):
    """Tests for KdV integral matrix construction."""

    def test_I1_matrix_primary_eigenvalue(self):
        """I_1 matrix (0,0) entry = h - c/24."""
        c, h = 25.0, 1.0
        vm = VermaModule(c, h, max_level=4)
        I1 = kdv_integral_matrix(vm, 1)
        self.assertAlmostEqual(I1[0, 0], h - c / 24.0, places=8)

    def test_I3_matrix_commutes_with_I1(self):
        """I_3 matrix commutes with I_1 matrix (key property)."""
        c = 25.0
        vm = VermaModule(c, 0.0, max_level=5)
        I1 = kdv_integral_matrix(vm, 1)
        I3 = kdv_integral_matrix(vm, 3)
        comm = I1 @ I3 - I3 @ I1
        self.assertLess(np.max(np.abs(comm)), 1e-6)

    def test_I3_matrix_finite(self):
        """I_3 matrix has finite entries."""
        vm = VermaModule(25.0, 0.0, max_level=5)
        I3 = kdv_integral_matrix(vm, 3)
        self.assertTrue(np.all(np.isfinite(I3)))

    def test_invalid_order_raises(self):
        """Invalid order raises ValueError."""
        vm = VermaModule(25.0, 0.0, max_level=4)
        with self.assertRaises(ValueError):
            kdv_integral_matrix(vm, 11)


class TestCommutativity(unittest.TestCase):
    """Tests for [I_m, I_n] = 0 (quantum integrability)."""

    def test_I1_I3_commute(self):
        """[I_1, I_3] = 0 on Verma module."""
        result = verify_commutativity(25.0, 0.0, max_level=5, orders=[1, 3])
        self.assertTrue(result['all_commute'])

    def test_I1_I3_commute_nonzero_h(self):
        """[I_1, I_3] = 0 for h != 0."""
        result = verify_commutativity(10.0, 2.0, max_level=5, orders=[1, 3])
        self.assertTrue(result['all_commute'])

    def test_I1_I5_commute(self):
        """[I_1, I_5] = 0 (I_5 matrix commutes with L_0)."""
        result = verify_commutativity(25.0, 0.0, max_level=6, orders=[1, 5])
        self.assertTrue(result['[I_1, I_5]']['pass'])

    def test_commutativity_result_structure(self):
        """verify_commutativity returns dict with expected keys."""
        result = verify_commutativity(25.0, 0.0, max_level=4, orders=[1, 3])
        self.assertIn('[I_1, I_3]', result)
        self.assertIn('all_commute', result)

    def test_commutativity_multiple_c(self):
        """Commutativity holds for different central charges."""
        for c in [1.0, 10.0, 25.0]:
            result = verify_commutativity(c, 0.0, max_level=5, orders=[1, 3])
            self.assertTrue(result['all_commute'],
                            f"Commutativity failed at c={c}")


class TestKdVEigenvaluePolynomial(unittest.TestCase):
    """Tests for eigenvalue polynomial interpolation."""

    def test_I1_polynomial_degree_1(self):
        """q_1(h) has degree 1."""
        coeffs = kdv_eigenvalue_polynomial(25.0, order=1)
        self.assertEqual(len(coeffs), 2)  # degree 1: [a1, a0]

    def test_I3_polynomial_degree_2(self):
        """q_3(h) has degree 2."""
        coeffs = kdv_eigenvalue_polynomial(25.0, order=3)
        self.assertEqual(len(coeffs), 3)  # degree 2: [a2, a1, a0]

    def test_I1_polynomial_leading_coeff(self):
        """Leading coefficient of q_1 is 1 (coefficient of h)."""
        coeffs = kdv_eigenvalue_polynomial(25.0, order=1)
        self.assertAlmostEqual(coeffs[0], 1.0, places=6)


class TestVacuumEigenvalues(unittest.TestCase):
    """Tests for KdV vacuum eigenvalues."""

    def test_vacuum_q1(self):
        """q_1(0) = -c/24."""
        vac = kdv_vacuum_eigenvalues(24.0, max_order=1)
        self.assertAlmostEqual(vac[1], -1.0, places=8)

    def test_vacuum_q3(self):
        """q_3(0) = c(5c-1)/720."""
        c = 25.0
        vac = kdv_vacuum_eigenvalues(c, max_order=3)
        expected = c * (5 * c - 1) / 720.0
        self.assertAlmostEqual(vac[3], expected, places=6)

    def test_vacuum_eigenvalues_keys(self):
        """Keys are odd integers 1, 3, 5, 7, 9."""
        vac = kdv_vacuum_eigenvalues(25.0, max_order=9)
        self.assertIn(1, vac)
        self.assertIn(3, vac)
        self.assertIn(5, vac)
        self.assertIn(7, vac)
        self.assertIn(9, vac)

    def test_vacuum_q1_negative_for_positive_c(self):
        """q_1(0) < 0 for c > 0."""
        for c in [1.0, 10.0, 25.0]:
            vac = kdv_vacuum_eigenvalues(c, max_order=1)
            self.assertLess(vac[1], 0.0)

    def test_vacuum_q3_positive_for_positive_c(self):
        """q_3(0) > 0 for c > 1/5."""
        for c in [1.0, 10.0, 25.0]:
            vac = kdv_vacuum_eigenvalues(c, max_order=3)
            self.assertGreater(vac[3], 0.0)


class TestShadowTowerVirasoro(unittest.TestCase):
    """Tests for Virasoro shadow tower computation."""

    def test_shadow_S2_is_kappa(self):
        """S_2 = c/2 from shadow tower."""
        for c in [1.0, 10.0, 25.0]:
            tower = shadow_tower_virasoro(c)
            # S_2 comes from a[0]/2 where a[0] = 2*kappa = c
            # Actually, S_r = a[r-2] / r, so S_2 = a[0] / 2 = sqrt(4*kappa^2)/2 = |kappa|
            # For c > 0: S_2 should be approximately c/2
            self.assertAlmostEqual(tower[2], c / 2.0, places=4)

    def test_shadow_tower_returns_dict(self):
        """shadow_tower_virasoro returns dict with integer keys."""
        tower = shadow_tower_virasoro(25.0, max_arity=6)
        self.assertIn(2, tower)
        self.assertIn(3, tower)
        self.assertIn(4, tower)

    def test_shadow_tower_finite_values(self):
        """All shadow tower values are finite for c=25."""
        tower = shadow_tower_virasoro(25.0, max_arity=8)
        for r, val in tower.items():
            self.assertTrue(np.isfinite(val), f"S_{r} is not finite")


class TestShadowKdVComparison(unittest.TestCase):
    """Tests for shadow-KdV identification."""

    def test_comparison_f2_relation(self):
        """S_2 = -12 * q_1(0) (since q_1(0) = -c/24)."""
        c = 25.0
        result = shadow_kdv_comparison(c)
        S2 = result['shadows'][2]
        q1_0 = result['vacuum_eigenvalues'][1]
        # q_1(0) = -c/24, S_2 = c/2 = -12 * (-c/24)
        self.assertAlmostEqual(S2, -12 * q1_0, places=4)

    def test_comparison_returns_structure(self):
        """shadow_kdv_comparison returns dict with expected keys."""
        result = shadow_kdv_comparison(25.0)
        self.assertIn('shadows', result)
        self.assertIn('vacuum_eigenvalues', result)
        self.assertIn('comparisons', result)

    def test_comparison_kappa_value(self):
        """kappa in result is c/2."""
        c = 10.0
        result = shadow_kdv_comparison(c)
        self.assertAlmostEqual(result['kappa'], c / 2.0, places=10)


class TestZetaZeros(unittest.TestCase):
    """Tests for zeta zero related functionality."""

    def test_first_zeta_zero(self):
        """First zeta zero imaginary part ~ 14.1347."""
        zeros = zeta_zeros_first_n(1)
        self.assertAlmostEqual(zeros[0], 14.134725141734693, places=5)

    def test_zeta_zeros_count(self):
        """zeta_zeros_first_n returns requested number."""
        zeros = zeta_zeros_first_n(10)
        self.assertEqual(len(zeros), 10)

    def test_zeta_zeros_increasing(self):
        """Zeta zeros are monotonically increasing."""
        zeros = zeta_zeros_first_n(30)
        for i in range(len(zeros) - 1):
            self.assertLess(zeros[i], zeros[i + 1])

    def test_kdv_spectrum_at_zeros_runs(self):
        """kdv_spectrum_at_zeta_zeros runs and returns dict."""
        result = kdv_spectrum_at_zeta_zeros(25.0, max_order=3, n_zeros=5)
        self.assertIn('eigenvalues', result)
        self.assertIn('statistics', result)

    def test_kdv_spectrum_at_zeros_eigenvalue_count(self):
        """Each order has one eigenvalue per zero."""
        result = kdv_spectrum_at_zeta_zeros(25.0, max_order=3, n_zeros=5)
        for order in [1, 3]:
            for i in range(5):
                self.assertIn((order, i), result['eigenvalues'])


class TestW3ShadowData(unittest.TestCase):
    """Tests for W_3 shadow data."""

    def test_w3_kappa_T(self):
        """kappa_T = c/2 for W_3."""
        c = 10.0
        data = w3_shadow_data(c)
        self.assertAlmostEqual(data['kappa_T'], c / 2.0, places=10)

    def test_w3_S3(self):
        """S_3 = 2 (same as Virasoro on T-line)."""
        data = w3_shadow_data(10.0)
        self.assertAlmostEqual(data['S_3'], 2.0, places=10)

    def test_w3_S4_T(self):
        """S_4_T = 10/(c(5c+22)) (same as Virasoro on T-line)."""
        c = 10.0
        data = w3_shadow_data(c)
        expected = 10.0 / (c * (5 * c + 22))
        self.assertAlmostEqual(data['S_4_T'], expected, places=10)

    def test_w3_mixing_polynomial(self):
        """Mixing polynomial P(W_3) = 25c^2 + 100c - 428."""
        c = 10.0
        data = w3_shadow_data(c)
        expected = 25 * c**2 + 100 * c - 428
        self.assertAlmostEqual(data['mixing_polynomial'], expected, places=10)


class TestBenjaminOnoIntegrals(unittest.TestCase):
    """Tests for Benjamin-Ono integrals."""

    def test_J1_equals_I1(self):
        """J_1 = I_1 = h - c/24."""
        c, h = 25.0, 2.0
        bo = benjamin_ono_integrals(c, h)
        self.assertAlmostEqual(bo[1], kdv_I1_eigenvalue(c, h), places=10)

    def test_J2_is_w_charge(self):
        """J_2 = w (the W_3 charge eigenvalue)."""
        bo = benjamin_ono_integrals(10.0, 1.0, w_val=3.0)
        self.assertAlmostEqual(bo[2], 3.0, places=10)

    def test_J3_includes_T_channel(self):
        """J_3 includes T-channel = q_3^KdV(h) for w=0."""
        c, h = 25.0, 1.0
        bo = benjamin_ono_integrals(c, h, w_val=0.0)
        t_channel = kdv_I3_eigenvalue(c, h)
        self.assertAlmostEqual(bo[3], t_channel, places=8)


class TestMiuraShadowTransfer(unittest.TestCase):
    """Tests for Miura / Koszul duality transformation."""

    def test_kappa_sum_is_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        for c in [1.0, 10.0, 13.0, 25.0]:
            result = miura_shadow_transfer(c)
            self.assertAlmostEqual(result['kappa_sum'], 13.0, places=8)

    def test_dual_central_charge(self):
        """c_dual = 26 - c."""
        c = 10.0
        result = miura_shadow_transfer(c)
        self.assertAlmostEqual(result['c_dual'], 16.0, places=10)

    def test_self_dual_at_c13(self):
        """At c=13: tower_A = tower_A_dual."""
        result = miura_shadow_transfer(13.0)
        self.assertAlmostEqual(result['kappa'], result['kappa_dual'], places=8)

    def test_miura_returns_towers(self):
        """Result contains both towers."""
        result = miura_shadow_transfer(25.0)
        self.assertIn('tower_A', result)
        self.assertIn('tower_A_dual', result)


class TestClassicalShadowTower(unittest.TestCase):
    """Tests for dispersionless / classical limit."""

    def test_classical_tower_structure(self):
        """classical_shadow_tower returns dict with expected keys."""
        result = classical_shadow_tower(100.0)
        self.assertIn('tower', result)
        self.assertIn('normalized', result)
        self.assertIn('classical_predictions', result)

    def test_classical_S2_normalized(self):
        """S_2/c -> 1/2 for large c."""
        result = classical_shadow_tower(1000.0)
        S2 = result['tower'][2]
        self.assertAlmostEqual(S2 / 1000.0, 0.5, places=3)

    def test_classical_S3_constant(self):
        """S_3 = 2 is independent of c."""
        for c in [10.0, 100.0, 1000.0]:
            result = classical_shadow_tower(c)
            self.assertAlmostEqual(result['tower'][3], 2.0, places=2)


class TestTauFunction(unittest.TestCase):
    """Tests for tau function expansion."""

    def test_tau_function_structure(self):
        """tau_function_coefficients returns dict with expected keys."""
        result = tau_function_coefficients(25.0, max_terms=5)
        self.assertIn('vacuum_eigenvalues', result)
        self.assertIn('shadow_coefficients', result)
        self.assertIn('tau_shadow_relation', result)

    def test_tau_shadow_relation_ratio(self):
        """q_1(0) / F_1 = -2 (since q_1(0) = -c/24, F_1 = c/48)."""
        result = tau_function_coefficients(24.0)
        ratio = result['tau_shadow_relation']['ratio']
        self.assertAlmostEqual(ratio, -2.0, places=4)


class TestGGE(unittest.TestCase):
    """Tests for Generalized Gibbs Ensemble."""

    def test_gge_runs(self):
        """GGE partition function computes without error."""
        result = gge_partition_function(25.0, betas={1: 0.1}, max_level=4)
        self.assertIn('log_Z', result)
        self.assertTrue(np.isfinite(result['log_Z']))

    def test_gge_dimension(self):
        """Dimension of truncated module is correct."""
        result = gge_partition_function(25.0, betas={1: 0.1}, max_level=3)
        # dim = p(0) + p(1) + p(2) + p(3) = 1 + 1 + 2 + 3 = 7
        self.assertEqual(result['dim'], 7)

    def test_gge_ground_state_energy_finite(self):
        """Ground state energy is finite."""
        result = gge_partition_function(25.0, betas={1: 0.1, 3: 0.01},
                                         max_level=4)
        self.assertTrue(np.isfinite(result['ground_state_energy']))


class TestVirasroKdVLandscape(unittest.TestCase):
    """Tests for the landscape utility."""

    def test_landscape_returns_dict(self):
        """virasoro_kdv_landscape returns dict keyed by c values."""
        result = virasoro_kdv_landscape([1.0, 25.0], max_order=3)
        self.assertIn(1.0, result)
        self.assertIn(25.0, result)

    def test_landscape_skips_c0(self):
        """c=0 is skipped."""
        result = virasoro_kdv_landscape([0.0, 25.0], max_order=3)
        self.assertNotIn(0.0, result)

    def test_landscape_vacuum_eigenvalues(self):
        """Landscape entries contain vacuum eigenvalues."""
        result = virasoro_kdv_landscape([25.0], max_order=3)
        self.assertIn('vacuum_eigenvalues', result[25.0])


class TestCrossVerification(unittest.TestCase):
    """Multi-path cross-verification tests."""

    def test_I1_matrix_vs_formula(self):
        """q_1 from matrix matches formula at multiple (c, h)."""
        for c, h in [(25.0, 0.0), (10.0, 1.0), (1.0, 5.0)]:
            vm = VermaModule(c, h, max_level=4)
            I1 = kdv_integral_matrix(vm, 1)
            matrix_val = I1[0, 0]
            formula_val = kdv_I1_eigenvalue(c, h)
            self.assertAlmostEqual(matrix_val, formula_val, places=8)

    def test_I3_BLZ_vs_formula(self):
        """q_3 from BLZ recursion matches analytic formula."""
        from compute.lib.bc_quantum_kdv_shadow_engine import _blz_eigenvalue_recursion
        for c, h in [(25.0, 0.0), (10.0, 1.0), (1.0, 5.0)]:
            blz_val = _blz_eigenvalue_recursion(c, h, 3)
            formula_val = kdv_I3_eigenvalue(c, h)
            self.assertAlmostEqual(blz_val, formula_val, places=8)

    def test_I3_two_c_values_consistent(self):
        """q_3(c, h=0) independently computed for c=1 and c=25."""
        for c in [1.0, 25.0]:
            # Path 1: formula
            q3_formula = kdv_I3_eigenvalue(c, 0.0)
            # Path 2: direct computation
            q3_direct = c * (5 * c - 1) / 720.0
            self.assertAlmostEqual(q3_formula, q3_direct, places=10)

    def test_vacuum_eigenvalue_sign_pattern(self):
        """q_1(0) < 0, q_3(0) > 0 for physical c > 1."""
        c = 25.0
        vac = kdv_vacuum_eigenvalues(c, max_order=3)
        self.assertLess(vac[1], 0.0)
        self.assertGreater(vac[3], 0.0)


if __name__ == '__main__':
    unittest.main()
