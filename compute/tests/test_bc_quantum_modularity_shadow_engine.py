"""Tests for bc_quantum_modularity_shadow_engine.py.

Comprehensive test suite covering:
- AlgebraData construction for all families
- Shadow metric and tower coefficients
- Depth classification
- Root of unity evaluation and shadow q-series
- Algebraic number identification
- Quantum modularity defect
- Kontsevich-Zagier F and comparison
- q-Pochhammer and Habiro ring
- Nahm matrix and conjecture
- WRT invariants
- Instanton action and resurgence
- False theta functions
- Mock modularity
- Khovanov-type homology
- Cross-verification

Multi-path verification (AP10): every key result cross-checked.
"""

import cmath
import math
import unittest
from fractions import Fraction

from compute.lib.bc_quantum_modularity_shadow_engine import (
    AlgebraData,
    heisenberg_data,
    affine_sl2_data,
    affine_sl3_data,
    betagamma_data,
    virasoro_data,
    w3_data,
    lattice_voa_data,
    minimal_model_data,
    shadow_metric_coefficients,
    critical_discriminant,
    shadow_radius,
    shadow_tower_coefficients,
    classify_depth,
    root_of_unity,
    shadow_qseries_at_root,
    shadow_qseries_scan,
    identify_algebraic_number,
    mobius_action,
    quantum_modular_defect,
    kontsevich_zagier_F,
    kontsevich_zagier_F_at_root,
    shadow_vs_zagier_comparison,
    q_pochhammer,
    habiro_ring_test,
    nahm_matrix,
    wrt_invariant_lens_space,
    wrt_s3,
    wrt_from_shadow,
    instanton_action_from_shadow,
    false_theta_psi,
    false_theta_at_root,
    shadow_vs_false_theta,
    mock_modular_shadow_test,
    khovanov_shadow_euler,
    depth_modularity_classification,
    cross_verify_nahm_vs_radius,
    cross_verify_depth_vs_termination,
    GAMMA_T,
    GAMMA_S,
)


# =====================================================================
# 1. AlgebraData construction
# =====================================================================

class TestAlgebraData(unittest.TestCase):
    """Test AlgebraData construction for all families."""

    def test_heisenberg_kappa(self):
        d = heisenberg_data(3.0)
        self.assertAlmostEqual(d.kappa, 3.0)
        self.assertEqual(d.depth, 'G')
        self.assertAlmostEqual(d.alpha, 0.0)
        self.assertAlmostEqual(d.S4, 0.0)

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        d = virasoro_data(10.0)
        self.assertAlmostEqual(d.kappa, 5.0)
        self.assertEqual(d.depth, 'M')

    def test_virasoro_alpha(self):
        d = virasoro_data(10.0)
        self.assertAlmostEqual(d.alpha, 2.0)

    def test_virasoro_S4(self):
        """S4 = 10/(c*(5c+22))."""
        d = virasoro_data(10.0)
        expected = 10.0 / (10.0 * 72.0)
        self.assertAlmostEqual(d.S4, expected, places=10)

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k=1) = 3*3/4 = 9/4."""
        d = affine_sl2_data(1.0)
        self.assertAlmostEqual(d.kappa, 9.0 / 4.0)
        self.assertEqual(d.depth, 'L')

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k=1) = 8*4/6 = 16/3."""
        d = affine_sl3_data(1.0)
        self.assertAlmostEqual(d.kappa, 16.0 / 3.0)

    def test_w3_kappa(self):
        """kappa(W_3) = 5c/6."""
        d = w3_data(6.0)
        self.assertAlmostEqual(d.kappa, 5.0)

    def test_lattice_kappa(self):
        d = lattice_voa_data(24)
        self.assertAlmostEqual(d.kappa, 24.0)
        self.assertEqual(d.depth, 'G')

    def test_betagamma_class_C(self):
        d = betagamma_data()
        self.assertEqual(d.depth, 'C')

    def test_minimal_model(self):
        """M(3,4): c = 1 - 6/12 = 1/2."""
        d = minimal_model_data(3)
        self.assertAlmostEqual(d.params['c'], 0.5)

    def test_virasoro_c0_degenerate(self):
        d = virasoro_data(0.0)
        self.assertAlmostEqual(d.kappa, 0.0)


# =====================================================================
# 2. Shadow metric and tower coefficients
# =====================================================================

class TestShadowMetric(unittest.TestCase):
    """Test shadow metric computations."""

    def test_coefficients(self):
        d = virasoro_data(10.0)
        q0, q1, q2 = shadow_metric_coefficients(d)
        self.assertAlmostEqual(q0, 100.0)
        self.assertAlmostEqual(q1, 120.0)

    def test_heisenberg_constant(self):
        d = heisenberg_data(3.0)
        q0, q1, q2 = shadow_metric_coefficients(d)
        self.assertAlmostEqual(q0, 36.0)
        self.assertAlmostEqual(q1, 0.0)
        self.assertAlmostEqual(q2, 0.0)

    def test_discriminant(self):
        d = virasoro_data(10.0)
        Delta = critical_discriminant(d)
        expected = 40.0 / (5.0 * 10.0 + 22.0)
        self.assertAlmostEqual(Delta, expected)

    def test_heisenberg_discriminant_zero(self):
        d = heisenberg_data(3.0)
        self.assertAlmostEqual(critical_discriminant(d), 0.0)


class TestShadowRadius(unittest.TestCase):
    """Test shadow growth rate."""

    def test_heisenberg_zero_radius(self):
        d = heisenberg_data(3.0)
        self.assertAlmostEqual(shadow_radius(d), 0.0)

    def test_virasoro_positive_radius(self):
        d = virasoro_data(10.0)
        rho = shadow_radius(d)
        self.assertGreater(rho, 0)

    def test_virasoro_c13_self_dual(self):
        """Shadow radius at c=13 (self-dual point)."""
        d = virasoro_data(13.0)
        rho = shadow_radius(d)
        self.assertGreater(rho, 0)


class TestTowerCoefficients(unittest.TestCase):
    """Test shadow tower coefficient computation."""

    def test_virasoro_S2_kappa(self):
        d = virasoro_data(10.0)
        S = shadow_tower_coefficients(d, max_arity=5)
        self.assertAlmostEqual(S[2], d.kappa, places=8)

    def test_heisenberg_terminates(self):
        d = heisenberg_data(3.0)
        S = shadow_tower_coefficients(d, max_arity=10)
        self.assertAlmostEqual(S[2], 3.0, places=8)
        for r in range(3, 11):
            self.assertAlmostEqual(S[r], 0.0, places=10, msg=f"S_{r} should be 0")

    def test_virasoro_S3_equals_alpha(self):
        d = virasoro_data(10.0)
        S = shadow_tower_coefficients(d, max_arity=5)
        # S_3 = a_1 / 3 = 6/3 = 2 = alpha
        self.assertAlmostEqual(S[3], 2.0, places=6)

    def test_affine_sl2_tower(self):
        d = affine_sl2_data(1.0)
        S = shadow_tower_coefficients(d, max_arity=6)
        self.assertAlmostEqual(S[2], d.kappa, places=8)


# =====================================================================
# 3. Depth classification
# =====================================================================

class TestClassifyDepth(unittest.TestCase):
    """Test depth classification."""

    def test_heisenberg_G(self):
        self.assertEqual(classify_depth(heisenberg_data()), 'G')

    def test_affine_sl2_L(self):
        self.assertEqual(classify_depth(affine_sl2_data()), 'L')

    def test_betagamma_C(self):
        self.assertEqual(classify_depth(betagamma_data()), 'C')

    def test_virasoro_M(self):
        self.assertEqual(classify_depth(virasoro_data(10.0)), 'M')


# =====================================================================
# 4. Roots of unity and q-series
# =====================================================================

class TestRootOfUnity(unittest.TestCase):
    """Test root of unity computation."""

    def test_zeta_1(self):
        self.assertAlmostEqual(root_of_unity(1), 1.0)

    def test_zeta_2(self):
        self.assertAlmostEqual(root_of_unity(2), -1.0)

    def test_zeta_4(self):
        z4 = root_of_unity(4)
        self.assertAlmostEqual(z4.real, 0.0, places=10)
        self.assertAlmostEqual(z4.imag, 1.0, places=10)

    def test_zeta_N_power_N(self):
        """zeta_N^N = 1 for all N."""
        for N in range(1, 15):
            zN = root_of_unity(N)
            self.assertAlmostEqual(abs(zN**N - 1.0), 0.0, places=10)


class TestShadowQSeries(unittest.TestCase):
    """Test shadow q-series at roots of unity."""

    def test_heisenberg_finite(self):
        d = heisenberg_data(1.0)
        z = shadow_qseries_at_root(d, 5)
        self.assertTrue(math.isfinite(abs(z)))

    def test_virasoro_finite(self):
        d = virasoro_data(10.0)
        z = shadow_qseries_at_root(d, 5, max_arity=40)
        self.assertTrue(math.isfinite(abs(z)))

    def test_scan(self):
        d = heisenberg_data(1.0)
        result = shadow_qseries_scan(d, N_max=10, max_arity=20)
        self.assertEqual(len(result), 10)


# =====================================================================
# 5. Algebraic number identification
# =====================================================================

class TestIdentifyAlgebraic(unittest.TestCase):
    """Test algebraic number identification."""

    def test_rational(self):
        result = identify_algebraic_number(0.5 + 0j)
        self.assertEqual(result['type'], 'rational')
        self.assertEqual(result['value'], Fraction(1, 2))

    def test_integer(self):
        result = identify_algebraic_number(3.0 + 0j)
        self.assertEqual(result['type'], 'rational')

    def test_sqrt2(self):
        result = identify_algebraic_number(math.sqrt(2) + 0j)
        self.assertEqual(result['type'], 'quadratic')


# =====================================================================
# 6. Mobius action
# =====================================================================

class TestMobiusAction(unittest.TestCase):
    """Test SL_2(Z) Mobius action."""

    def test_T_action(self):
        """T: x -> x+1."""
        self.assertAlmostEqual(mobius_action(GAMMA_T, 0.5), 1.5)

    def test_S_action(self):
        """S: x -> -1/x."""
        self.assertAlmostEqual(mobius_action(GAMMA_S, 2.0), -0.5)

    def test_S_at_zero(self):
        """S at x=0 is singular."""
        self.assertIsNone(mobius_action(GAMMA_S, 0.0))


# =====================================================================
# 7. Kontsevich-Zagier F
# =====================================================================

class TestKontsevichZagier(unittest.TestCase):
    """Test Kontsevich-Zagier quantum modular form F(q)."""

    def test_F_at_1(self):
        """F(1) = sum_{n>=0} 0^n = 1 (only n=0 term survives since (1;1)_n=0 for n>=1)."""
        val = kontsevich_zagier_F_at_root(1)
        # (1;1)_0 = 1, (1;1)_1 = 1-1 = 0. So F(1) = 1.
        self.assertAlmostEqual(val.real, 1.0, places=8)

    def test_F_finite_at_roots(self):
        for N in range(1, 10):
            val = kontsevich_zagier_F_at_root(N)
            self.assertTrue(math.isfinite(abs(val)), f"F(zeta_{N}) not finite")

    def test_F_series_at_small_q(self):
        val = kontsevich_zagier_F(0.1 + 0j, max_terms=100)
        self.assertTrue(math.isfinite(abs(val)))


# =====================================================================
# 8. q-Pochhammer
# =====================================================================

class TestQPochhammer(unittest.TestCase):
    """Test q-Pochhammer symbol (q;q)_n."""

    def test_n0(self):
        self.assertAlmostEqual(q_pochhammer(0.5 + 0j, 0), 1.0)

    def test_n1(self):
        """(q;q)_1 = 1-q."""
        self.assertAlmostEqual(q_pochhammer(0.5 + 0j, 1), 0.5)

    def test_n2(self):
        """(q;q)_2 = (1-q)(1-q^2)."""
        q = 0.5
        expected = (1 - q) * (1 - q**2)
        self.assertAlmostEqual(q_pochhammer(q + 0j, 2), expected)

    def test_root_of_unity_vanishes(self):
        """(zeta_N; zeta_N)_N = 0 because 1 - zeta_N^N = 0."""
        for N in range(1, 8):
            zeta = root_of_unity(N)
            self.assertAlmostEqual(abs(q_pochhammer(zeta, N)), 0.0, places=8)


# =====================================================================
# 9. Habiro ring test
# =====================================================================

class TestHabiroRing(unittest.TestCase):
    """Test Habiro ring membership."""

    def test_heisenberg_finite(self):
        d = heisenberg_data(1.0)
        result = habiro_ring_test(d, 5, max_arity=30)
        self.assertTrue(result['finite'])

    def test_virasoro_finite(self):
        d = virasoro_data(10.0)
        result = habiro_ring_test(d, 5, max_arity=30)
        self.assertTrue(result['finite'])

    def test_pochhammer_at_N(self):
        d = heisenberg_data(1.0)
        result = habiro_ring_test(d, 5, max_arity=20)
        self.assertAlmostEqual(abs(result['pochhammer_at_N']), 0.0, places=8)


# =====================================================================
# 10. Nahm matrix
# =====================================================================

class TestNahmMatrix(unittest.TestCase):
    """Test Nahm matrix construction."""

    def test_virasoro_nahm(self):
        d = virasoro_data(10.0)
        result = nahm_matrix(d)
        self.assertIn('nahm_matrix', result)
        self.assertIn('eigenvalue', result)

    def test_heisenberg_nahm(self):
        d = heisenberg_data(1.0)
        result = nahm_matrix(d)
        self.assertIn('nahm_matrix', result)

    def test_heisenberg_eigenvalue_zero(self):
        """Heisenberg has rho=0, so Nahm eigenvalue=0."""
        d = heisenberg_data(1.0)
        result = nahm_matrix(d)
        self.assertAlmostEqual(result['eigenvalue'], 0.0)


# =====================================================================
# 11. WRT invariants
# =====================================================================

class TestWRTInvariants(unittest.TestCase):
    """Test WRT invariants of 3-manifolds."""

    def test_s3_positive(self):
        """WRT of S^3 should be positive for all k >= 1."""
        for k in range(1, 8):
            val = wrt_s3(k)
            self.assertGreater(val, 0, f"Z(S^3, k={k}) <= 0")

    def test_s3_formula(self):
        """Z(S^3, k) = sqrt(2/(k+2)) * sin(pi/(k+2))."""
        for k in [1, 2, 3, 5]:
            r = k + 2
            expected = math.sqrt(2.0 / r) * math.sin(math.pi / r)
            self.assertAlmostEqual(wrt_s3(k), expected, places=10)

    def test_lens_space_finite(self):
        val = wrt_invariant_lens_space(3, 1, 2)
        self.assertTrue(math.isfinite(abs(val)))

    def test_wrt_from_shadow(self):
        d = affine_sl2_data(1.0)
        result = wrt_from_shadow(d, 3, 2, max_arity=30)
        self.assertIn('wrt_L(p,1)', result)
        self.assertTrue(math.isfinite(abs(result['wrt_L(p,1)'])))


# =====================================================================
# 12. Instanton action and resurgence
# =====================================================================

class TestInstantonAction(unittest.TestCase):
    """Test instanton action from shadow branch points."""

    def test_virasoro_has_resurgence(self):
        d = virasoro_data(10.0)
        result = instanton_action_from_shadow(d)
        self.assertTrue(result['has_resurgent_structure'])
        self.assertTrue(math.isfinite(result['instanton_action_abs']))

    def test_heisenberg_no_resurgence(self):
        d = heisenberg_data(1.0)
        result = instanton_action_from_shadow(d)
        self.assertFalse(result['has_resurgent_structure'])


# =====================================================================
# 13. False theta functions
# =====================================================================

class TestFalseTheta(unittest.TestCase):
    """Test false theta function Psi(q)."""

    def test_Psi_at_small_q(self):
        val = false_theta_psi(0.5 + 0j)
        self.assertTrue(math.isfinite(abs(val)))

    def test_Psi_at_root(self):
        for N in range(2, 8):
            val = false_theta_at_root(N)
            self.assertTrue(math.isfinite(abs(val)))

    def test_shadow_vs_false_theta(self):
        d = virasoro_data(10.0)
        result = shadow_vs_false_theta(d, N_max=10)
        self.assertIn('ratios', result)


# =====================================================================
# 14. Mock modularity
# =====================================================================

class TestMockModularity(unittest.TestCase):
    """Test mock modularity analysis."""

    def test_virasoro_mock(self):
        d = virasoro_data(10.0)
        result = mock_modular_shadow_test(d)
        self.assertIn('E2', result)
        self.assertIn('E2_star', result)
        self.assertIn('mock_type', result)

    def test_heisenberg_mock_type(self):
        d = heisenberg_data(1.0)
        result = mock_modular_shadow_test(d)
        self.assertIn('modular', result['mock_type'])

    def test_invalid_tau(self):
        d = virasoro_data(10.0)
        result = mock_modular_shadow_test(d, tau_val=complex(0, -1))
        self.assertIn('error', result)


# =====================================================================
# 15. Khovanov-type homology
# =====================================================================

class TestKhovanovShadow(unittest.TestCase):
    """Test Khovanov-type Euler characteristic."""

    def test_heisenberg(self):
        d = heisenberg_data(1.0)
        result = khovanov_shadow_euler(d, max_arity=10)
        self.assertIn('total_dim', result)
        self.assertEqual(result['total_dim'], 1)  # Only S_2 nonzero

    def test_virasoro_many_nonzero(self):
        d = virasoro_data(10.0)
        result = khovanov_shadow_euler(d, max_arity=20)
        # Class M: many nonzero arities
        self.assertGreater(result['nonzero_arities'], 5)

    def test_euler_matches_shadow(self):
        """Euler characteristic matches shadow q-series."""
        d = virasoro_data(10.0)
        result = khovanov_shadow_euler(d, max_arity=20)
        self.assertTrue(result['euler_matches_shadow'])


# =====================================================================
# 16. Depth-modularity classification
# =====================================================================

class TestDepthModularity(unittest.TestCase):
    """Test depth-modularity classification."""

    def test_heisenberg_modular(self):
        d = heisenberg_data(1.0)
        result = depth_modularity_classification(d, max_arity=20)
        self.assertIn('depth', result)
        self.assertEqual(result['depth'], 'G')
        self.assertEqual(result['modularity_type'], 'theta-modular')

    def test_virasoro_quantum(self):
        d = virasoro_data(10.0)
        result = depth_modularity_classification(d, max_arity=20)
        self.assertIn('depth', result)
        self.assertEqual(result['depth'], 'M')


# =====================================================================
# 17. Cross-verification
# =====================================================================

class TestCrossVerification(unittest.TestCase):
    """Multi-path cross-verification (AP10)."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa for all families, verified via two paths."""
        for d in [heisenberg_data(3.0), virasoro_data(10.0), affine_sl2_data(1.0)]:
            S = shadow_tower_coefficients(d, max_arity=5)
            self.assertAlmostEqual(S[2], d.kappa, places=6,
                                   msg=f"S_2 != kappa for {d.name}")

    def test_heisenberg_tower_terminates(self):
        """Cross-check: Heisenberg tower terminates at arity 2."""
        d = heisenberg_data(5.0)
        result = cross_verify_depth_vs_termination(d, max_arity=20)
        self.assertEqual(result['depth'], 'G')
        self.assertTrue(result['consistent'])
        self.assertEqual(result['last_nonzero_arity'], 2)

    def test_nahm_vs_radius(self):
        d = virasoro_data(10.0)
        result = cross_verify_nahm_vs_radius(d)
        self.assertIn('nahm_eigenvalue', result)
        self.assertIn('rho_squared', result)
        self.assertTrue(result['agreement_nahm_radius'])

    def test_root_of_unity_periodicity(self):
        """zeta_N^{r+N} = zeta_N^r."""
        N = 7
        zeta = root_of_unity(N)
        for r in range(0, 10):
            self.assertAlmostEqual(abs(zeta**(r + N) - zeta**r), 0.0, places=10)

    def test_q_pochhammer_product(self):
        """(q;q)_n = (q;q)_{n-1} * (1 - q^n)."""
        q = 0.3 + 0.1j
        for n in range(1, 8):
            left = q_pochhammer(q, n)
            right = q_pochhammer(q, n - 1) * (1 - q**n)
            self.assertAlmostEqual(abs(left - right), 0.0, places=10)

    def test_virasoro_disc_negative(self):
        """For Virasoro: disc < 0 (class M verified two ways)."""
        d = virasoro_data(10.0)
        q0, q1, q2 = shadow_metric_coefficients(d)
        disc = q1**2 - 4 * q0 * q2
        self.assertLess(disc, 0)
        self.assertEqual(classify_depth(d), 'M')


class TestAdditionalAlgebraData(unittest.TestCase):
    """Additional AlgebraData tests."""

    def test_virasoro_c2_params(self):
        d = virasoro_data(2.0)
        self.assertEqual(d.params['c'], 2.0)

    def test_affine_sl2_params(self):
        d = affine_sl2_data(3.0)
        self.assertEqual(d.params['k'], 3.0)
        self.assertEqual(d.params['dim_g'], 3)

    def test_lattice_different_ranks(self):
        for rank in [1, 8, 24]:
            d = lattice_voa_data(rank)
            self.assertAlmostEqual(d.kappa, float(rank))

    def test_w3_depth_M(self):
        d = w3_data(10.0)
        self.assertEqual(d.depth, 'M')


class TestAdditionalTower(unittest.TestCase):
    """Additional shadow tower tests."""

    def test_virasoro_S4_value(self):
        """S_4 = 10/(c*(5c+22)) / 4 = a_2/4."""
        d = virasoro_data(2.0)
        S = shadow_tower_coefficients(d, max_arity=5)
        expected_a2 = 40.0 / (2.0 * 32.0)
        self.assertAlmostEqual(S[4], expected_a2 / 4.0, places=6)

    def test_tower_large_arity(self):
        """Tower computation doesn't crash for large arities."""
        d = virasoro_data(10.0)
        S = shadow_tower_coefficients(d, max_arity=60)
        self.assertEqual(len(S), 59)


class TestAdditionalQSeries(unittest.TestCase):
    """Additional q-series tests."""

    def test_heisenberg_qseries_is_kappa_zeta_sq(self):
        """For Heisenberg with only S_2 nonzero: Z_A(zeta_N) = kappa * zeta_N^2."""
        d = heisenberg_data(3.0)
        for N in range(2, 8):
            z = shadow_qseries_at_root(d, N, max_arity=10)
            expected = 3.0 * root_of_unity(N, 2)
            self.assertAlmostEqual(abs(z - expected), 0.0, places=6,
                                   msg=f"N={N}")

    def test_mobius_T_composition(self):
        """T^n: x -> x+n."""
        x = 0.3
        result = x
        for _ in range(5):
            result = mobius_action(GAMMA_T, result)
        self.assertAlmostEqual(result, x + 5.0, places=10)

    def test_S_squared_identity(self):
        """S^2: x -> -1/(-1/x) = x. Well, S^2 = -Id, so S^2(x) = x."""
        x = 0.5
        result = mobius_action(GAMMA_S, mobius_action(GAMMA_S, x))
        self.assertAlmostEqual(result, x, places=10)


if __name__ == '__main__':
    unittest.main()
