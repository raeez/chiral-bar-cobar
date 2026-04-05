"""Tests for bc_period_torelli_shadow_engine.py.

Comprehensive test suite covering:
- Kappa formulas for all families (AP1/AP39 compliant)
- Shadow metric coefficients and discriminant
- Period domain classification
- Period map computation (Virasoro and affine)
- Torelli theorem verification
- Griffiths transversality
- Monodromy representations
- Hodge metric (Weil-Petersson)
- Schmid orbit theorem
- Clemens-Schmid exact sequence
- Period map degree
- Calabi-Yau period check
- Koszul duality period relation
- Full period landscape

Multi-path verification (AP10): every numerical result cross-checked.
"""

import math
import unittest

import numpy as np
from sympy import Rational

from compute.lib.bc_period_torelli_shadow_engine import (
    kappa_virasoro,
    kappa_heisenberg,
    kappa_affine_slN,
    kappa_wN,
    virasoro_shadow_data_numerical,
    virasoro_shadow_data_symbolic,
    heisenberg_shadow_data_numerical,
    affine_slN_shadow_data_numerical,
    shadow_metric_coefficients,
    shadow_metric_discriminant,
    critical_discriminant_from_data,
    period_domain_type,
    period_domain_for_family,
    shadow_period_tau,
    virasoro_period_map,
    virasoro_period_map_explicit,
    affine_slN_period_map,
    virasoro_torelli_test,
    affine_torelli_test,
    virasoro_griffiths_transversality,
    griffiths_check_all_families,
    virasoro_monodromy_at_zero,
    virasoro_monodromy_at_lee_yang,
    virasoro_monodromy_at_infinity,
    virasoro_monodromy_group,
    affine_slN_monodromy_group,
    virasoro_hodge_metric,
    virasoro_hodge_metric_landscape,
    hodge_metric_singularity_analysis,
    schmid_orbit_at_zero,
    schmid_orbit_at_lee_yang,
    clemens_schmid_at_boundary,
    period_map_degree_virasoro,
    shadow_cy_check,
    virasoro_cy_periods_landscape,
    multi_parameter_period_map,
    shadow_connection_as_gauss_manin,
    koszul_duality_period_relation,
    full_period_landscape,
)


class TestKappaFormulas(unittest.TestCase):
    """Test kappa formulas for all families (AP1/AP39)."""

    def test_virasoro_kappa(self):
        self.assertEqual(kappa_virasoro(2), Rational(1))
        self.assertEqual(kappa_virasoro(10), Rational(5))
        self.assertEqual(kappa_virasoro(26), Rational(13))

    def test_heisenberg_kappa(self):
        self.assertEqual(kappa_heisenberg(3), Rational(3))
        self.assertEqual(kappa_heisenberg(1), Rational(1))

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        self.assertEqual(kappa_affine_slN(2, 1), Rational(3) * Rational(3) / 4)
        self.assertEqual(kappa_affine_slN(2, 2), Rational(3))

    def test_affine_sl3_kappa(self):
        """kappa(sl_3, k) = 8(k+3)/6 = 4(k+3)/3."""
        self.assertEqual(kappa_affine_slN(3, 1), Rational(8) * Rational(4) / 6)

    def test_wN_kappa(self):
        """kappa(W_N, c) = (H_N - 1)*c."""
        # W_2 = Virasoro: H_2 = 1 + 1/2 = 3/2, H_2-1 = 1/2
        self.assertEqual(kappa_wN(2, 2), Rational(1))  # (1/2)*2 = 1 = c/2

    def test_virasoro_kappa_not_c(self):
        """kappa != c in general (AP39)."""
        self.assertNotEqual(kappa_virasoro(4), 4)


class TestShadowData(unittest.TestCase):
    """Test shadow data construction."""

    def test_virasoro_numerical(self):
        kap, alpha, S4, Delta = virasoro_shadow_data_numerical(10.0)
        self.assertAlmostEqual(kap, 5.0)
        self.assertAlmostEqual(alpha, 2.0)
        self.assertAlmostEqual(S4, 10.0 / (10.0 * 72.0))
        self.assertAlmostEqual(Delta, 8.0 * 5.0 * S4)

    def test_virasoro_symbolic(self):
        from sympy import Symbol
        kap, alpha, S4, Delta = virasoro_shadow_data_symbolic()
        cs = Symbol('c')
        # Verify at c=2
        self.assertEqual(float(kap.subs(cs, 2)), 1.0)
        self.assertEqual(float(alpha), 2.0)

    def test_heisenberg_data(self):
        kap, alpha, S4, Delta = heisenberg_shadow_data_numerical(3.0)
        self.assertEqual(kap, 3.0)
        self.assertEqual(alpha, 0.0)
        self.assertEqual(S4, 0.0)
        self.assertEqual(Delta, 0.0)

    def test_affine_data(self):
        kap, alpha, S4, Delta = affine_slN_shadow_data_numerical(2, 1.0)
        self.assertAlmostEqual(kap, 3.0 * 3.0 / 4.0)


class TestShadowMetric(unittest.TestCase):
    """Test shadow metric coefficients."""

    def test_coefficients(self):
        q0, q1, q2 = shadow_metric_coefficients(5.0, 2.0, 0.1)
        self.assertAlmostEqual(q0, 100.0)
        self.assertAlmostEqual(q1, 120.0)
        self.assertAlmostEqual(q2, 36.0 + 80.0 * 0.1)

    def test_discriminant(self):
        q0, q1, q2 = shadow_metric_coefficients(5.0, 2.0, 0.0)
        disc = shadow_metric_discriminant(q0, q1, q2)
        # Delta=0 => disc = q1^2 - 4*q0*q2 = 14400 - 4*100*36 = 14400-14400 = 0
        self.assertAlmostEqual(disc, 0.0, places=8)

    def test_critical_discriminant(self):
        self.assertAlmostEqual(critical_discriminant_from_data(5.0, 0.1), 4.0)

    def test_virasoro_disc_negative(self):
        """For Virasoro: disc < 0 (class M, non-degenerate)."""
        kap, alpha, S4, Delta = virasoro_shadow_data_numerical(10.0)
        q0, q1, q2 = shadow_metric_coefficients(kap, alpha, S4)
        disc = shadow_metric_discriminant(q0, q1, q2)
        self.assertLess(disc, 0)


class TestPeriodDomain(unittest.TestCase):
    """Test period domain classification."""

    def test_class_G(self):
        pd = period_domain_type('G')
        self.assertEqual(pd['domain'], 'point')
        self.assertEqual(pd['dimension'], 0)

    def test_class_M(self):
        pd = period_domain_type('M')
        self.assertEqual(pd['domain'], 'upper_half_plane')
        self.assertEqual(pd['dimension'], 1)

    def test_family_mapping(self):
        self.assertEqual(period_domain_for_family('heisenberg')['shadow_class'], 'G')
        self.assertEqual(period_domain_for_family('virasoro')['shadow_class'], 'M')
        self.assertEqual(period_domain_for_family('affine_sl2')['shadow_class'], 'L')

    def test_w3_siegel(self):
        pd = period_domain_for_family('W3')
        self.assertEqual(pd['domain'], 'siegel_half_space')
        self.assertEqual(pd['siegel_degree'], 2)


class TestPeriodMap(unittest.TestCase):
    """Test period map computation."""

    def test_virasoro_im_positive(self):
        """Im(tau(c)) > 0 for all c in (0, 26)."""
        for c_val in [1, 5, 10, 13, 20, 25]:
            tau, re_tau, im_tau = virasoro_period_map(float(c_val))
            self.assertGreater(im_tau, 0, f"Im(tau) <= 0 at c={c_val}")

    def test_virasoro_re_formula(self):
        """Re(tau(c)) = -6/c."""
        for c_val in [2, 5, 10, 13]:
            tau, re_tau, im_tau = virasoro_period_map(float(c_val))
            self.assertAlmostEqual(re_tau, -6.0 / c_val, places=10)

    def test_two_path_agreement(self):
        """Period from shadow_period_tau agrees with explicit formula."""
        for c_val in [2.0, 5.0, 10.0, 13.0, 20.0]:
            tau1, re1, im1 = virasoro_period_map(c_val)
            tau2, re2, im2 = virasoro_period_map_explicit(c_val)
            self.assertAlmostEqual(re1, re2, places=10, msg=f"Re mismatch at c={c_val}")
            self.assertAlmostEqual(im1, im2, places=10, msg=f"Im mismatch at c={c_val}")

    def test_affine_degenerate(self):
        """Affine period is real (degenerate VHS)."""
        tau = affine_slN_period_map(2, 1.0)
        self.assertAlmostEqual(tau.imag, 0.0, places=10)

    def test_virasoro_explicit_c_positive_required(self):
        with self.assertRaises(ValueError):
            virasoro_period_map_explicit(-1.0)


class TestTorelli(unittest.TestCase):
    """Test Torelli theorem verification."""

    def test_virasoro_torelli_holds(self):
        result = virasoro_torelli_test(c_values=list(range(1, 26)))
        self.assertTrue(result['torelli_holds'])
        self.assertEqual(len(result['collisions']), 0)

    def test_real_part_monotone(self):
        result = virasoro_torelli_test(c_values=list(range(1, 26)))
        self.assertTrue(result['real_part_monotone'])

    def test_imag_part_monotone(self):
        result = virasoro_torelli_test(c_values=list(range(1, 26)))
        self.assertTrue(result['imag_part_monotone'])

    def test_affine_torelli(self):
        result = affine_torelli_test(2, k_values=list(range(1, 10)))
        self.assertTrue(result['torelli_holds'])
        self.assertTrue(result['degenerate_vhs'])


class TestGriffiths(unittest.TestCase):
    """Test Griffiths transversality."""

    def test_virasoro_transversality(self):
        result = virasoro_griffiths_transversality(10.0)
        self.assertTrue(result['transversality_holds'])
        self.assertTrue(result['im_tau_positive'])

    def test_derivative_agreement(self):
        """Numerical and analytical derivatives agree."""
        result = virasoro_griffiths_transversality(10.0)
        self.assertLess(result['relative_error'], 1e-4)

    def test_all_families(self):
        result = griffiths_check_all_families()
        self.assertTrue(result['virasoro']['all_hold'])


class TestMonodromy(unittest.TestCase):
    """Test monodromy representations."""

    def test_c0_minus_identity(self):
        result = virasoro_monodromy_at_zero()
        np.testing.assert_array_equal(result['monodromy_matrix'],
                                      np.array([[-1, 0], [0, -1]]))
        self.assertTrue(result['is_minus_identity'])
        self.assertEqual(result['order'], 2)

    def test_lee_yang_unipotent(self):
        result = virasoro_monodromy_at_lee_yang()
        self.assertTrue(result['is_unipotent'])
        self.assertTrue(result['N_squared_zero'])
        self.assertEqual(result['nilpotent_rank'], 1)

    def test_infinity_quasi_unipotent(self):
        result = virasoro_monodromy_at_infinity()
        self.assertFalse(result['is_unipotent'])
        self.assertTrue(result['is_quasi_unipotent'])

    def test_monodromy_relation(self):
        """T_0 * T_LY * T_inf = Id (up to sign conventions)."""
        T0 = virasoro_monodromy_at_zero()['monodromy_matrix']
        TLY = virasoro_monodromy_at_lee_yang()['monodromy_matrix']
        Tinf = virasoro_monodromy_at_infinity()['monodromy_matrix']
        product = T0 @ TLY @ Tinf
        np.testing.assert_array_equal(product, np.eye(2, dtype=int))

    def test_monodromy_group(self):
        result = virasoro_monodromy_group()
        self.assertTrue(result['is_arithmetic'])

    def test_affine_monodromy(self):
        result = affine_slN_monodromy_group(2)
        self.assertEqual(result['shadow_class'], 'L')


class TestHodgeMetric(unittest.TestCase):
    """Test Hodge (Weil-Petersson) metric."""

    def test_positive(self):
        for c_val in [2.0, 5.0, 10.0, 13.0, 20.0]:
            g_wp, _, _ = virasoro_hodge_metric(c_val)
            self.assertGreater(g_wp, 0)

    def test_landscape(self):
        result = virasoro_hodge_metric_landscape(c_values=[2.0, 5.0, 10.0, 13.0])
        self.assertGreater(len(result['metric_values']), 0)

    def test_singularity_at_zero(self):
        result = hodge_metric_singularity_analysis()
        # Power law exponent should be approximately -2
        self.assertTrue(result['consistent'])
        self.assertAlmostEqual(result['power_law_exponent'], -2.0, places=0)


class TestSchmidOrbit(unittest.TestCase):
    """Test Schmid orbit theorem analysis."""

    def test_c0_not_schmid(self):
        result = schmid_orbit_at_zero()
        self.assertFalse(result['schmid_applies'])
        self.assertEqual(result['singularity_type'], 'pole')

    def test_c0_limiting_behavior(self):
        result = schmid_orbit_at_zero()
        self.assertAlmostEqual(result['limiting_c_tau_real'], -6.0, places=2)

    def test_lee_yang_schmid(self):
        result = schmid_orbit_at_lee_yang()
        self.assertTrue(result['schmid_applies'])
        self.assertTrue(result['N_squared_zero'])


class TestClemensSchmid(unittest.TestCase):
    """Test Clemens-Schmid exact sequence."""

    def test_c0_sequence(self):
        result = clemens_schmid_at_boundary('c=0')
        self.assertEqual(result['N_map'], 'zero')
        self.assertEqual(result['monodromy_type'], 'semisimple')

    def test_lee_yang_sequence(self):
        result = clemens_schmid_at_boundary('c=-22/5')
        self.assertEqual(result['monodromy_type'], 'unipotent')
        self.assertEqual(result['H1_central_fiber']['dimension'], 1)

    def test_unknown_boundary(self):
        result = clemens_schmid_at_boundary('c=unknown')
        self.assertIn('error', result)


class TestPeriodMapDegree(unittest.TestCase):
    """Test period map degree."""

    def test_degree_one(self):
        result = period_map_degree_virasoro()
        self.assertEqual(result['degree'], 1)
        self.assertTrue(result['is_birational'])

    def test_recovery_verification(self):
        result = period_map_degree_virasoro()
        self.assertLess(result['verification']['error'], 1e-8)


class TestCYCheck(unittest.TestCase):
    """Test Calabi-Yau period check."""

    def test_virasoro_is_cy(self):
        result = shadow_cy_check('virasoro')
        self.assertTrue(result['is_cy'])
        self.assertEqual(result['h_n0'], 1)

    def test_heisenberg_not_cy(self):
        result = shadow_cy_check('heisenberg')
        self.assertFalse(result['is_cy'])

    def test_virasoro_with_params(self):
        result = shadow_cy_check('virasoro', params={'c': 10.0})
        self.assertIn('cy_period', result)

    def test_cy_landscape(self):
        result = virasoro_cy_periods_landscape()
        self.assertEqual(len(result), 25)
        for c_val in range(1, 26):
            self.assertIn(c_val, result)


class TestKoszulDualityPeriods(unittest.TestCase):
    """Test Koszul duality on periods (AP24)."""

    def test_self_dual_c13(self):
        result = koszul_duality_period_relation(13.0)
        self.assertTrue(result['is_self_dual'])

    def test_delta_sum(self):
        for c_val in [2.0, 5.0, 10.0, 20.0]:
            result = koszul_duality_period_relation(c_val)
            self.assertTrue(result['delta_sum_match'])
            self.assertEqual(result['complementarity_constant_numerator'], 6960)


class TestShadowConnectionGaussManin(unittest.TestCase):
    """Test shadow connection as Gauss-Manin."""

    def test_connection_form(self):
        result = shadow_connection_as_gauss_manin(10.0)
        self.assertAlmostEqual(result['connection_t_at_origin'],
                               result['expected_omega_t'], places=8)
        self.assertAlmostEqual(result['connection_c_at_origin'],
                               result['expected_omega_c'], places=8)

    def test_is_gauss_manin(self):
        result = shadow_connection_as_gauss_manin(5.0)
        self.assertTrue(result['is_gauss_manin'])


class TestMultiParameterPeriod(unittest.TestCase):
    """Test multi-parameter period maps."""

    def test_affine_degenerate(self):
        result = multi_parameter_period_map(2, 1.0)
        self.assertIn('degenerate', result['period_domain'])

    def test_wN_nondegenerate(self):
        result = multi_parameter_period_map(3, 1.0, c_val=10.0)
        self.assertIn('H', result['period_domain'])


class TestFullPeriodLandscape(unittest.TestCase):
    """Test full landscape computation."""

    def test_returns_all_sections(self):
        result = full_period_landscape()
        self.assertIn('period_domains', result)
        self.assertIn('virasoro_periods', result)
        self.assertIn('torelli', result)
        self.assertIn('monodromy', result)
        self.assertIn('cy_families', result)

    def test_torelli_holds(self):
        result = full_period_landscape()
        self.assertTrue(result['torelli']['torelli_holds'])


class TestCrossVerification(unittest.TestCase):
    """Multi-path cross-verification tests."""

    def test_kappa_virasoro_two_paths(self):
        """kappa via formula vs kappa via shadow data."""
        for c_val in [2, 10, 13]:
            path1 = float(kappa_virasoro(c_val))
            path2 = virasoro_shadow_data_numerical(float(c_val))[0]
            self.assertAlmostEqual(path1, path2, places=10)

    def test_discriminant_two_paths(self):
        """disc via metric coefficients vs direct formula -320c^2/(5c+22)."""
        for c_val in [2.0, 10.0, 25.0]:
            kap, alpha, S4, Delta = virasoro_shadow_data_numerical(c_val)
            q0, q1, q2 = shadow_metric_coefficients(kap, alpha, S4)
            disc_path1 = shadow_metric_discriminant(q0, q1, q2)
            disc_path2 = -320.0 * c_val**2 / (5.0 * c_val + 22.0)
            self.assertAlmostEqual(disc_path1, disc_path2, places=6,
                                   msg=f"disc mismatch at c={c_val}")

    def test_period_self_consistency(self):
        """tau(c) computed from data agrees with explicit formula."""
        for c_val in [3.0, 7.0, 15.0]:
            tau1, _, _ = virasoro_period_map(c_val)
            tau2, _, _ = virasoro_period_map_explicit(c_val)
            self.assertAlmostEqual(abs(tau1 - tau2), 0.0, places=8)

    def test_affine_kappa_linear_in_k(self):
        """kappa(sl_N, k) is linear in k (for fixed N)."""
        for N in [2, 3, 4]:
            k1 = float(kappa_affine_slN(N, 1))
            k2 = float(kappa_affine_slN(N, 2))
            k3 = float(kappa_affine_slN(N, 3))
            # Linear: k3 - k2 should equal k2 - k1
            self.assertAlmostEqual(k3 - k2, k2 - k1, places=10)


class TestAdditionalKappaFormulas(unittest.TestCase):
    """More kappa formula tests across families."""

    def test_virasoro_c13_self_dual(self):
        """At c=13: kappa = 13/2, kappa_dual = (26-13)/2 = 13/2."""
        self.assertEqual(kappa_virasoro(13), Rational(13, 2))

    def test_affine_sl2_level_dependency(self):
        """kappa increases with level k."""
        k1 = float(kappa_affine_slN(2, 1))
        k5 = float(kappa_affine_slN(2, 5))
        self.assertGreater(k5, k1)

    def test_affine_sl2_dim_g(self):
        """dim(sl_2) = 3, h^v = 2."""
        # kappa = 3*(k+2)/4
        self.assertEqual(kappa_affine_slN(2, 0), Rational(3, 2))

    def test_wN_at_c0(self):
        """kappa(W_N, 0) = 0."""
        self.assertEqual(kappa_wN(3, 0), 0)

    def test_w2_is_virasoro(self):
        """W_2 = Virasoro, so kappa_wN(2,c) = c/2."""
        for c_val in [2, 10, 13]:
            self.assertEqual(kappa_wN(2, c_val), kappa_virasoro(c_val))


class TestPeriodMapEdgeCases(unittest.TestCase):
    """Test period map at edge cases."""

    def test_small_c(self):
        """Period map at small c: tau has large imaginary part."""
        tau, re, im = virasoro_period_map(0.1)
        self.assertGreater(abs(re), 50)  # Re = -6/0.1 = -60

    def test_large_c(self):
        """Period map at large c: tau approaches 0."""
        tau, re, im = virasoro_period_map(100.0)
        self.assertAlmostEqual(re, -6.0 / 100.0, places=8)
        self.assertGreater(im, 0)

    def test_c13_special(self):
        """Self-dual point c=13 should produce valid period."""
        tau, re, im = virasoro_period_map(13.0)
        self.assertAlmostEqual(re, -6.0 / 13.0, places=10)
        self.assertGreater(im, 0)


class TestMetricDetails(unittest.TestCase):
    """Detailed tests for shadow metric."""

    def test_q0_equals_c_squared(self):
        """q0 = c^2 for Virasoro."""
        for c_val in [2.0, 10.0]:
            kap, alpha, S4, _ = virasoro_shadow_data_numerical(c_val)
            q0, _, _ = shadow_metric_coefficients(kap, alpha, S4)
            self.assertAlmostEqual(q0, c_val**2, places=8)

    def test_q1_equals_12c(self):
        """q1 = 12*c for Virasoro (since alpha=2)."""
        for c_val in [2.0, 10.0]:
            kap, alpha, S4, _ = virasoro_shadow_data_numerical(c_val)
            _, q1, _ = shadow_metric_coefficients(kap, alpha, S4)
            self.assertAlmostEqual(q1, 12.0 * c_val, places=8)

    def test_heisenberg_metric_constant(self):
        """Heisenberg: Q_L = 4k^2 (constant)."""
        kap, alpha, S4, _ = heisenberg_shadow_data_numerical(3.0)
        q0, q1, q2 = shadow_metric_coefficients(kap, alpha, S4)
        self.assertAlmostEqual(q0, 36.0)
        self.assertAlmostEqual(q1, 0.0)
        self.assertAlmostEqual(q2, 0.0)


class TestMonodromyDetails(unittest.TestCase):
    """Additional monodromy tests."""

    def test_c0_eigenvalues(self):
        result = virasoro_monodromy_at_zero()
        self.assertEqual(result['eigenvalues'], [-1, -1])

    def test_lee_yang_eigenvalues(self):
        result = virasoro_monodromy_at_lee_yang()
        self.assertEqual(result['eigenvalues'], [1, 1])

    def test_c0_not_unipotent(self):
        result = virasoro_monodromy_at_zero()
        self.assertFalse(result['is_unipotent'])

    def test_c0_semisimple(self):
        result = virasoro_monodromy_at_zero()
        self.assertTrue(result['is_semisimple'])

    def test_monodromy_group_generators(self):
        result = virasoro_monodromy_group()
        self.assertEqual(len(result['generators']), 2)


class TestAdditionalCYChecks(unittest.TestCase):
    """Additional CY period checks."""

    def test_betagamma_not_cy(self):
        result = shadow_cy_check('betagamma')
        self.assertFalse(result['is_cy'])

    def test_affine_not_cy(self):
        result = shadow_cy_check('affine_sl2')
        self.assertFalse(result['is_cy'])

    def test_w3_is_cy(self):
        result = shadow_cy_check('W3')
        self.assertTrue(result['is_cy'])
        self.assertEqual(result['h_n0'], 2)


class TestAdditionalGriffiths(unittest.TestCase):
    """Additional Griffiths transversality tests."""

    def test_at_multiple_c_values(self):
        for c_val in [3.0, 7.0, 15.0, 22.0]:
            result = virasoro_griffiths_transversality(c_val)
            self.assertTrue(result['transversality_holds'],
                            f"Griffiths failed at c={c_val}")
            self.assertLess(result['relative_error'], 1e-3,
                            f"Large error at c={c_val}")


if __name__ == '__main__':
    unittest.main()
