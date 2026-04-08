r"""Tests for the Zeng large-N engine: shadow invariants via Deligne category.

VERIFICATION PATHS (multi-path mandate: 3+ per claim):

1. Direct computation from defining formulas
2. Cross-verification with existing engines (large_n_delta_f2, kappa tables)
3. Limiting cases (N=2 Virasoro, k=-h^v critical, large N)
4. Koszul duality constraints (kappa + kappa' = 0 for KM)
5. 't Hooft limit consistency
6. Deligne interpolation at integer points
7. Dimensional/degree analysis
8. Cross-family consistency (sl_N -> W_N via DS)

Manuscript references:
    thm:winfty-scalar, thm:multi-weight-genus-expansion
    conj:ht-deformation-quantization, thm:kz-classical-quantum-bridge
    theorem_large_n_delta_f2_engine.py
    AP1, AP24, AP39, AP48
"""

import unittest
import sys
import os
from fractions import Fraction
from math import log

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from theorem_zeng_large_n_engine import (
    all_genera_completion_status,
    central_charge_sl_N,
    c_W_N_from_sl_N,
    dim_sl_N,
    dual_coxeter_sl_N,
    faber_pandharipande_lambda_g,
    genus_0_quantization_seed,
    genus_1_obstruction_status,
    harmonic_number,
    kappa_affine_sl_N,
    kappa_affine_sl_N_dual,
    kappa_deligne_at_integer,
    kappa_deligne_interpolation,
    kappa_deligne_thooft,
    kappa_sl_N_fixed_level,
    kappa_sl_N_thooft,
    kappa_thooft_normalized,
    kappa_W_N,
    kappa_W_N_from_sl_N,
    kappa_W_N_thooft,
    large_n_shadow_table,
    large_n_wn_table,
    pva_classical_central_charge,
    q_ht_bridge_layers,
    verify_deligne_interpolation_table,
    verify_kappa_antisymmetry_sl_N,
    verify_kappa_specialization_N2,
    verify_kappa_thooft_large_N_limit,
    verify_kappa_W2_is_virasoro,
    winfty_cyclic_cohomology_dim,
    winfty_kappa_divergence,
    winfty_shadow_depth,
    zeng_assessment,
    zeng_vs_monograph_comparison,
)


class TestDimAndDualCoxeter(unittest.TestCase):
    """Test basic sl_N invariants."""

    def test_dim_sl_2(self):
        self.assertEqual(dim_sl_N(2), 3)

    def test_dim_sl_3(self):
        self.assertEqual(dim_sl_N(3), 8)

    def test_dim_sl_5(self):
        self.assertEqual(dim_sl_N(5), 24)

    def test_dual_coxeter_sl_N(self):
        for N in range(2, 11):
            self.assertEqual(dual_coxeter_sl_N(N), N)

    def test_dim_sl_N_invalid(self):
        with self.assertRaises(ValueError):
            dim_sl_N(1)


class TestKappaAffineSLN(unittest.TestCase):
    """Test kappa(sl_N, k) = dim(sl_N) * (k + h^v) / (2h^v)."""

    def test_kappa_sl_2_level_1(self):
        # kappa(sl_2, 1) = 3 * (1+2) / (2*2) = 9/4
        self.assertEqual(kappa_affine_sl_N(2, 1), Fraction(9, 4))

    def test_kappa_sl_3_level_1(self):
        # kappa(sl_3, 1) = 8 * (1+3) / (2*3) = 32/6 = 16/3
        self.assertEqual(kappa_affine_sl_N(3, 1), Fraction(16, 3))

    def test_kappa_critical_level_is_zero(self):
        """At critical level k = -h^v = -N, kappa = 0 (Feigin-Frenkel)."""
        for N in range(2, 11):
            self.assertEqual(kappa_affine_sl_N(N, -N), 0)

    def test_kappa_antisymmetry_sl_2(self):
        """kappa(sl_2, k) + kappa(sl_2, k') = 0 with k' = -k-4."""
        for k in [1, 2, 3, 5, 10]:
            self.assertTrue(verify_kappa_antisymmetry_sl_N(2, k))

    def test_kappa_antisymmetry_sl_3(self):
        """kappa(sl_3, k) + kappa(sl_3, k') = 0 with k' = -k-6."""
        for k in [1, 2, 5]:
            self.assertTrue(verify_kappa_antisymmetry_sl_N(3, k))

    def test_kappa_antisymmetry_all_types(self):
        """AP24-safe: kappa + kappa' = 0 for ALL affine KM."""
        for N in range(2, 8):
            for k in [1, 3, 7]:
                self.assertTrue(
                    verify_kappa_antisymmetry_sl_N(N, k),
                    f"Anti-symmetry failed for sl_{N} at k={k}"
                )

    def test_kappa_ap39_sl2_not_c_over_2(self):
        """AP39: kappa(sl_2, k) != c(sl_2, k)/2 in general."""
        k = 1
        kappa = kappa_affine_sl_N(2, k)
        c = central_charge_sl_N(2, k)
        # kappa = 9/4, c/2 = 1/2, these are NOT equal
        self.assertNotEqual(kappa, c / 2)

    def test_kappa_sl_10_level_1(self):
        # kappa(sl_10, 1) = 99 * 11 / 20 = 1089/20
        self.assertEqual(kappa_affine_sl_N(10, 1), Fraction(1089, 20))


class TestCentralChargeSLN(unittest.TestCase):
    """Test c(sl_N, k) = k * dim(sl_N) / (k + h^v)."""

    def test_c_sl_2_level_1(self):
        # c(sl_2, 1) = 1 * 3 / (1+2) = 1
        self.assertEqual(central_charge_sl_N(2, 1), 1)

    def test_c_sl_3_level_1(self):
        # c(sl_3, 1) = 1 * 8 / (1+3) = 2
        self.assertEqual(central_charge_sl_N(3, 1), 2)

    def test_c_critical_level_raises(self):
        """c is undefined at critical level k = -h^v."""
        with self.assertRaises(ValueError):
            central_charge_sl_N(3, -3)


class TestLargeNExpansion(unittest.TestCase):
    """Test large-N limits of kappa(sl_N, k)."""

    def test_fixed_level_expansion_matches(self):
        """Verify the expansion formula matches exact kappa."""
        for N in [5, 10, 20, 50]:
            result = kappa_sl_N_fixed_level(N, 1)
            self.assertTrue(result['match'],
                           f"Expansion mismatch at N={N}")

    def test_fixed_level_leading_order(self):
        """Leading term is N^2/2 at fixed k."""
        for N in [10, 20, 50, 100]:
            result = kappa_sl_N_fixed_level(N, 1)
            ratio = float(result['exact'] / result['leading_N2'])
            self.assertAlmostEqual(ratio, 1.0, delta=0.1,
                                  msg=f"Leading order bad at N={N}")

    def test_thooft_normalization_converges(self):
        """kappa/N^2 -> 1/(2*lambda) as N -> infinity."""
        lam = Fraction(1, 2)
        for N in [10, 50, 100, 500]:
            result = verify_kappa_thooft_large_N_limit(N, lam)
            # Relative error should decrease with N
            if result['relative_error'] is not None:
                self.assertLess(result['relative_error'], 1.0 / N,
                              msg=f"Convergence too slow at N={N}")

    def test_thooft_kappa_exact(self):
        """kappa(sl_N, lambda) = (N^2-1)/(2*lambda)."""
        N, lam = 5, Fraction(1, 3)
        kappa = kappa_sl_N_thooft(N, lam)
        self.assertEqual(kappa, Fraction(24, 1) / (2 * lam))
        self.assertEqual(kappa, Fraction(36))


class TestHarmonicNumber(unittest.TestCase):
    """Test harmonic number computation."""

    def test_H_1(self):
        self.assertEqual(harmonic_number(1), 1)

    def test_H_2(self):
        self.assertEqual(harmonic_number(2), Fraction(3, 2))

    def test_H_3(self):
        self.assertEqual(harmonic_number(3), Fraction(11, 6))

    def test_H_4(self):
        self.assertEqual(harmonic_number(4), Fraction(25, 12))


class TestKappaWN(unittest.TestCase):
    """Test kappa(W_N) = c * (H_N - 1)."""

    def test_kappa_W2_is_virasoro(self):
        """W_2 = Virasoro: kappa = c/2."""
        for k in [1, 2, 5, 10]:
            self.assertTrue(verify_kappa_W2_is_virasoro(k),
                           f"W_2 != Virasoro at k={k}")

    def test_kappa_W3_from_sl3(self):
        """kappa(W_3, k=1) = c(W_3, 1) * (H_3 - 1)."""
        c = c_W_N_from_sl_N(3, 1)
        H_3_minus_1 = Fraction(5, 6)  # 1/2 + 1/3
        kappa = kappa_W_N(3, c)
        self.assertEqual(kappa, c * H_3_minus_1)

    def test_c_W2_from_sl2(self):
        """c(W_2, k) matches Virasoro formula c = 1 - 6(k+1)^2/(k+2).
        For sl_2: c = 1 - 6(k+1)^2/(k+2).
        From the general formula: (N-1) - N(N^2-1)(k+N-1)^2/(k+N)
        At N=2: 1 - 2*3*(k+1)^2/(k+2) = 1 - 6(k+1)^2/(k+2)."""
        for k in [1, 2, 3]:
            k_f = Fraction(k)
            c_formula = c_W_N_from_sl_N(2, k_f)
            c_virasoro = 1 - 6 * (k_f + 1)**2 / (k_f + 2)
            self.assertEqual(c_formula, c_virasoro,
                           f"c(W_2, {k}) mismatch")

    def test_kappa_WN_diverges_with_N(self):
        """kappa(W_N, c_fixed) ~ c * log(N) -> infinity."""
        c = Fraction(10)
        prev_kappa = Fraction(0)
        for N in [2, 5, 10, 20, 50]:
            kappa = kappa_W_N(N, c)
            self.assertGreater(kappa, prev_kappa,
                             f"kappa should be increasing at N={N}")
            prev_kappa = kappa


class TestDeligneInterpolation(unittest.TestCase):
    """Test Deligne category interpolation at integer points."""

    def test_all_integer_points(self):
        """Deligne interpolation at t=N matches standard formula."""
        results = verify_deligne_interpolation_table()
        for r in results:
            self.assertTrue(r['deligne_match'],
                           f"Mismatch at N={r['N']}, k={r['k']}")

    def test_deligne_thooft_matches(self):
        """Deligne 't Hooft matches standard 't Hooft at integer N."""
        for N in [3, 5, 10]:
            lam = Fraction(1, 3)
            kappa_std = kappa_sl_N_thooft(N, lam)
            kappa_del = kappa_deligne_thooft(Fraction(N), lam)
            self.assertEqual(kappa_std, kappa_del,
                           f"Deligne 't Hooft mismatch at N={N}")

    def test_deligne_noninteger(self):
        """Deligne interpolation at t=5/2 gives a well-defined value."""
        t = Fraction(5, 2)
        k = 1
        kappa = kappa_deligne_interpolation(t, k)
        # (25/4 - 1) * (1 + 5/2) / (2 * 5/2) = 21/4 * 7/2 / 5 = 147/40
        expected = Fraction(21, 4) * Fraction(7, 2) / 5
        self.assertEqual(kappa, expected)


class TestPVAQuantization(unittest.TestCase):
    """Test PVA classical limit and quantization analysis."""

    def test_genus_0_seed_sl_3(self):
        """Genus-0 quantization seed for sl_3 at level 1."""
        result = genus_0_quantization_seed(3, 1)
        self.assertEqual(result['c'], 2)
        self.assertEqual(result['kappa'], Fraction(16, 3))
        self.assertIn('PROVED', result['genus_0_status'])

    def test_genus_1_virasoro_proved(self):
        """Genus-1 obstruction for Virasoro is PROVED to vanish."""
        status = genus_1_obstruction_status('virasoro')
        self.assertEqual(status['obstruction'], 'VANISHES')
        self.assertIn('PROVED', status['status'])

    def test_genus_1_w3_proved(self):
        """Genus-1 obstruction for W_3 is PROVED to vanish."""
        status = genus_1_obstruction_status('w3')
        self.assertEqual(status['obstruction'], 'VANISHES')
        self.assertIn('PROVED', status['status'])

    def test_genus_1_general_pva_conditional(self):
        """Genus-1 obstruction for general PVA is CONDITIONAL."""
        status = genus_1_obstruction_status('general_pva')
        self.assertIn('CONDITIONAL', status['status'])

    def test_all_genera_algebraic_proved(self):
        """All-genera algebraic completion is PROVED."""
        status = all_genera_completion_status()
        self.assertIn('PROVED', status['algebraic'])

    def test_all_genera_geometric_conjectural(self):
        """All-genera geometric comparison is CONJECTURAL."""
        status = all_genera_completion_status()
        self.assertIn('CONJECTURAL', status['geometric_higher_genus'])


class TestQHTBridge(unittest.TestCase):
    """Test Q_HT bridge layer analysis."""

    def test_three_layers_exist(self):
        """Q_HT bridge has three layers."""
        layers = q_ht_bridge_layers()
        self.assertIn('layer_1_algebraic', layers)
        self.assertIn('layer_2_geometric', layers)
        self.assertIn('layer_3_functorial', layers)
        self.assertIn('zeng_role', layers)

    def test_layer_1_proved(self):
        layers = q_ht_bridge_layers()
        self.assertEqual(layers['layer_1_algebraic']['status'], 'PROVED')

    def test_layer_2_conditional(self):
        layers = q_ht_bridge_layers()
        self.assertEqual(layers['layer_2_geometric']['status'], 'CONDITIONAL')

    def test_layer_3_conjectural(self):
        layers = q_ht_bridge_layers()
        self.assertEqual(layers['layer_3_functorial']['status'], 'CONJECTURAL')

    def test_zeng_limitation(self):
        """Zeng does NOT provide modular/higher-genus content."""
        layers = q_ht_bridge_layers()
        self.assertIn('No modular', layers['zeng_role']['limitation'])


class TestWInftyLimit(unittest.TestCase):
    """Test W_{1+infinity} limit analysis."""

    def test_cyclic_cohomology_dim_1(self):
        """dim H^2_cyc(W_{1+infinity}) = 1 (thm:winfty-scalar)."""
        self.assertEqual(winfty_cyclic_cohomology_dim(), 1)

    def test_kappa_divergence_monotone(self):
        """H_N - 1 is strictly increasing."""
        results = winfty_kappa_divergence()
        for i in range(1, len(results)):
            self.assertGreater(
                results[i]['H_N_minus_1'],
                results[i-1]['H_N_minus_1']
            )

    def test_kappa_divergence_ratio_to_log(self):
        """H_N - 1 ~ log(N) + gamma - 1 at large N.
        Ratio (H_N - 1)/log(N) -> 1 as N -> infinity."""
        results = winfty_kappa_divergence([50, 100, 500, 1000])
        for r in results:
            if r['ratio_to_log_N'] is not None:
                self.assertAlmostEqual(r['ratio_to_log_N'], 1.0, delta=0.15,
                                      msg=f"Ratio bad at N={r['N']}")

    def test_shadow_depth_class_M(self):
        """W_{1+infinity} is class M* (infinite shadow depth)."""
        info = winfty_shadow_depth()
        self.assertEqual(info['class'], 'M* (class M at the limit)')
        self.assertEqual(info['r_max'], 'infinity')

    def test_cross_channel_diverges(self):
        """Cross-channel correction delta_F_2 DIVERGES."""
        info = winfty_shadow_depth()
        self.assertIn('DIVERGES', info['cross_channel'])


class TestZengAssessment(unittest.TestCase):
    """Test the overall Zeng assessment."""

    def test_assessment_keys(self):
        assessment = zeng_assessment()
        self.assertIn('q_ht_route', assessment)
        self.assertIn('large_n_kappa', assessment)
        self.assertIn('winfty_rigor', assessment)
        self.assertIn('modular_koszul_at_infinity', assessment)

    def test_assessment_partial(self):
        """Q_HT route is PARTIAL."""
        assessment = zeng_assessment()
        self.assertIn('PARTIAL', assessment['q_ht_route'])

    def test_assessment_open_bar(self):
        """Bar complex in Rep(GL_t) is OPEN."""
        assessment = zeng_assessment()
        self.assertIn('OPEN', assessment['modular_koszul_at_infinity'])

    def test_comparison_gap_identified(self):
        """The comparison correctly identifies the gap."""
        comparison = zeng_vs_monograph_comparison()
        self.assertIn('bar_in_deligne_cat', comparison['gap'])
        self.assertEqual(comparison['gap']['bar_in_deligne_cat'], 'OPEN')

    def test_zeng_provides_pva(self):
        """Zeng provides PVA limit."""
        comparison = zeng_vs_monograph_comparison()
        self.assertEqual(comparison['zeng_provides']['pva_limit'], 'YES (classical shadow)')

    def test_zeng_no_bar(self):
        """Zeng does NOT provide bar complex."""
        comparison = zeng_vs_monograph_comparison()
        self.assertEqual(comparison['zeng_provides']['bar_complex'], 'NO')


class TestLargeNTables(unittest.TestCase):
    """Test table generation."""

    def test_shadow_table_class_L(self):
        """All affine KM are class L."""
        table = large_n_shadow_table()
        for row in table:
            self.assertEqual(row['shadow_class'], 'L')

    def test_shadow_table_kappa_positive(self):
        """kappa > 0 for all sl_N at level k=1."""
        table = large_n_shadow_table()
        for row in table:
            self.assertGreater(row['kappa'], 0)

    def test_wn_table_class_M(self):
        """All W_N for N >= 2 are class M."""
        table = large_n_wn_table()
        for row in table:
            self.assertEqual(row['shadow_class'], 'M')

    def test_kappa_over_N2_converges(self):
        """kappa(sl_N, 1)/N^2 converges at large N."""
        table = large_n_shadow_table([10, 50, 100, 500])
        ratios = [float(row['kappa_over_N2']) for row in table]
        # Should converge to 1/2 (at fixed k=1: kappa ~ N^2/2)
        for r in ratios:
            self.assertAlmostEqual(r, 0.5, delta=0.1)


class TestCrossVerification(unittest.TestCase):
    """Cross-verification with other engines and known values."""

    def test_kappa_sl_2_vs_landscape(self):
        """kappa(sl_2, 1) = 9/4 matches the landscape census."""
        self.assertEqual(kappa_affine_sl_N(2, 1), Fraction(9, 4))

    def test_faber_pandharipande_lambda_1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(faber_pandharipande_lambda_g(1), Fraction(1, 24))

    def test_faber_pandharipande_lambda_2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(faber_pandharipande_lambda_g(2), Fraction(7, 5760))

    def test_genus_1_free_energy_sl_3(self):
        """F_1(sl_3, k=1) = kappa/24 = 16/(3*24) = 2/9."""
        kappa = kappa_affine_sl_N(3, 1)
        F_1 = kappa * faber_pandharipande_lambda_g(1)
        self.assertEqual(F_1, Fraction(2, 9))

    def test_koszul_dual_level(self):
        """The Koszul dual level for sl_N is k' = -k - 2N."""
        N, k = 3, 1
        k_dual = -Fraction(k) - 2 * N
        self.assertEqual(k_dual, -7)
        kappa_dual = kappa_affine_sl_N(N, k_dual)
        self.assertEqual(kappa_dual, -kappa_affine_sl_N(N, k))

    def test_thooft_at_lambda_half(self):
        """At lambda=1/2 (k=N): kappa(sl_N, N) = (N^2-1)(2N)/(2N) = (N^2-1)/2.
        't Hooft: kappa = (N^2-1)/(2*1/2) = N^2-1. Wait...
        lambda = N/(k+N) = N/(N+N) = 1/2, so k = N.
        kappa = (N^2-1)(k+N)/(2N) = (N^2-1)*2N/(2N) = N^2-1.
        't Hooft formula: (N^2-1)/(2*lambda) = (N^2-1)/1 = N^2-1. OK."""
        for N in [3, 5, 10]:
            kappa_direct = kappa_affine_sl_N(N, N)
            kappa_thooft = kappa_sl_N_thooft(N, Fraction(1, 2))
            self.assertEqual(kappa_direct, kappa_thooft)
            self.assertEqual(kappa_direct, N**2 - 1)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""

    def test_invalid_N(self):
        with self.assertRaises(ValueError):
            kappa_affine_sl_N(1, 1)

    def test_critical_level_c_raises(self):
        with self.assertRaises(ValueError):
            central_charge_sl_N(5, -5)

    def test_zero_lambda_raises(self):
        with self.assertRaises(ValueError):
            kappa_sl_N_thooft(3, Fraction(0))

    def test_fractional_level(self):
        """kappa at fractional level k=1/2."""
        kappa = kappa_affine_sl_N(3, Fraction(1, 2))
        # (8) * (1/2 + 3) / (2*3) = 8 * 7/2 / 6 = 28/6 = 14/3
        self.assertEqual(kappa, Fraction(14, 3))

    def test_negative_level(self):
        """kappa at negative (but not critical) level."""
        kappa = kappa_affine_sl_N(3, -1)
        # (8) * (-1+3) / (2*3) = 8*2/6 = 8/3
        self.assertEqual(kappa, Fraction(8, 3))


if __name__ == '__main__':
    unittest.main()
