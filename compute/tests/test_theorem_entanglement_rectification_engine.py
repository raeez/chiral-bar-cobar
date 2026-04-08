r"""Tests for the entanglement rectification engine.

Multi-path verification of:
  (a) CoHA/DT entanglement for the Koszul pair (V_k(sl_2), V_{-k-4}(sl_2))
  (b) K11 Lagrangian QEC rate simplification (Holstein-Rivera)
  (c) Page curve saturation genus for the shadow CohFT
  (d) W_3 code distance and infinite-depth QEC
  (e) Shifted symplectic structure as QEC inner product

Each numerical result is verified by at least 3 independent paths
(Multi-Path Verification Mandate).
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, simplify

from compute.lib.theorem_entanglement_rectification_engine import (
    # Section 1: CoHA / DT
    kappa_affine_sl2,
    kappa_affine_sl2_dual,
    verify_km_complementarity_sl2,
    central_charge_sl2,
    central_charge_sl2_dual,
    verify_cc_complementarity_sl2,
    coha_entanglement_sl2,
    coha_entanglement_spectrum_sl2,
    # Section 2: K11 QEC
    qec_rate_lagrangian,
    qec_rate_with_perfectness,
    qec_parameters_by_family,
    # Section 3: Page saturation
    page_correction_genus,
    page_correction_antisymmetry,
    page_saturation_genus,
    page_curve_shadow_cohft,
    page_saturation_table,
    # Section 4: W_3 code
    w3_code_parameters,
    w3_redundancy_analysis,
    # Section 5: Shifted symplectic
    shifted_symplectic_degree,
    verdier_pairing_isotropy,
    symplectic_code_metrics,
    # Section 6: DT entanglement
    dt_partition_function_sl2,
    coha_entropy_from_dt,
    # Section 7: Cross-checks
    verify_km_entanglement_complementarity,
    verify_page_correction_properties,
    verify_qec_universality,
    verify_shifted_symplectic_independence,
    # Section 8: Full analysis
    full_entanglement_rectification,
    entanglement_landscape_census,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    von_neumann_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
)


# =========================================================================
#  1. CoHA / DT ENTANGLEMENT FOR sl_2 KOSZUL PAIRS
# =========================================================================

class TestCoHAEntanglementSl2(unittest.TestCase):
    """Tests for CoHA/DT entanglement computation."""

    def test_kappa_sl2_level1(self):
        """kappa(V_1(sl_2)) = 3*(1+2)/4 = 9/4."""
        self.assertEqual(kappa_affine_sl2(Rational(1)), Rational(9, 4))

    def test_kappa_sl2_level2(self):
        """kappa(V_2(sl_2)) = 3*(2+2)/4 = 3."""
        self.assertEqual(kappa_affine_sl2(Rational(2)), Rational(3))

    def test_kappa_sl2_critical(self):
        """kappa(V_{-2}(sl_2)) = 0 (critical level k = -h^v = -2)."""
        self.assertEqual(kappa_affine_sl2(Rational(-2)), Rational(0))

    def test_kappa_dual_sl2_level1(self):
        """kappa(V_{-5}(sl_2)) = -9/4."""
        self.assertEqual(kappa_affine_sl2_dual(Rational(1)), Rational(-9, 4))

    def test_km_complementarity_kappa_zero(self):
        """kappa + kappa' = 0 for all KM families (AP24)."""
        for k in [Rational(1), Rational(2), Rational(5),
                  Rational(10), Rational(1, 2), Rational(1, 3)]:
            self.assertTrue(verify_km_complementarity_sl2(k),
                            f"kappa + kappa' != 0 at k={k}")

    def test_central_charge_sl2_level1(self):
        """c(V_1(sl_2)) = 3*1/(1+2) = 1."""
        self.assertEqual(central_charge_sl2(Rational(1)), Rational(1))

    def test_central_charge_sl2_level4(self):
        """c(V_4(sl_2)) = 3*4/(4+2) = 2."""
        self.assertEqual(central_charge_sl2(Rational(4)), Rational(2))

    def test_cc_complementarity_sl2(self):
        """c + c' = 6 for sl_2 Koszul pairs."""
        for k in [Rational(1), Rational(2), Rational(5), Rational(10)]:
            self.assertTrue(verify_cc_complementarity_sl2(k),
                            f"c + c' != 6 at k={k}")

    def test_coha_entanglement_paths_agree(self):
        """Three derivation paths agree for S_EE."""
        for k in [Rational(1), Rational(2), Rational(4), Rational(10)]:
            data = coha_entanglement_sl2(k)
            self.assertTrue(data['paths_agree'],
                            f"Paths disagree at k={k}")

    def test_coha_see_values(self):
        """S_EE(V_k(sl_2)) = c/3 = k/(k+2) (for log_ratio=1)."""
        # k=1: c=1, S = 1/3
        self.assertEqual(coha_entanglement_sl2(Rational(1))['S_EE_scalar'], Rational(1, 3))
        # k=2: c=3/2, S = 1/2
        self.assertEqual(coha_entanglement_sl2(Rational(2))['S_EE_scalar'], Rational(1, 2))
        # k=4: c=2, S = 2/3
        self.assertEqual(coha_entanglement_sl2(Rational(4))['S_EE_scalar'], Rational(2, 3))

    def test_coha_complementarity_sum(self):
        """S_EE + S_EE' = 2 for sl_2 at all levels."""
        for k in [Rational(1), Rational(2), Rational(4)]:
            data = coha_entanglement_sl2(k)
            self.assertEqual(data['complementarity_sum'], Rational(2))

    def test_coha_kappa_complementarity(self):
        """kappa + kappa' = 0 verified through CoHA computation."""
        for k in [Rational(1), Rational(2), Rational(5)]:
            data = coha_entanglement_sl2(k)
            self.assertEqual(data['kappa_complementarity'], Rational(0))

    def test_coha_cc_complementarity(self):
        """c + c' = 6 verified through CoHA computation."""
        for k in [Rational(1), Rational(2), Rational(5)]:
            data = coha_entanglement_sl2(k)
            self.assertEqual(data['cc_complementarity'], Rational(6))

    def test_coha_shadow_class(self):
        """Affine sl_2 is class L (shadow depth 3)."""
        data = coha_entanglement_sl2(Rational(1))
        self.assertEqual(data['shadow_class'], 'L')

    def test_coha_f1_sum_zero(self):
        """F_1 + F_1' = 0 for KM families."""
        for k in [Rational(1), Rational(2), Rational(4)]:
            data = coha_entanglement_sl2(k)
            self.assertEqual(data['F1_sum'], Rational(0))

    def test_entanglement_spectrum_level1(self):
        """sl_2 at level 1 has 2 primaries: j=0, j=1/2."""
        spec = coha_entanglement_spectrum_sl2(Rational(1))
        self.assertEqual(spec['n_primaries'], 2)
        self.assertEqual(spec['dimensions'][0], Rational(0))  # j=0

    def test_entanglement_spectrum_level2(self):
        """sl_2 at level 2 has 3 primaries: j=0, 1/2, 1."""
        spec = coha_entanglement_spectrum_sl2(Rational(2))
        self.assertEqual(spec['n_primaries'], 3)
        self.assertEqual(spec['dimensions'][0], Rational(0))  # j=0
        # j=1: h = 1*2/(2+2) = 1/2
        self.assertEqual(spec['dimensions'][2], Rational(1, 2))


# =========================================================================
#  2. K11 LAGRANGIAN QEC RATE
# =========================================================================

class TestK11QECRate(unittest.TestCase):
    """Tests for the K11 Lagrangian QEC rate simplification."""

    def test_universal_rate_half(self):
        """QEC rate is universally 1/2."""
        self.assertEqual(qec_rate_lagrangian(), Rational(1, 2))

    def test_koszul_rate(self):
        """Koszul algebra gives rate 1/2."""
        data = qec_rate_with_perfectness(True, True)
        self.assertEqual(data['rate'], Rational(1, 2))

    def test_non_koszul_no_rate(self):
        """Non-Koszul algebra gives no code rate."""
        data = qec_rate_with_perfectness(False, True)
        self.assertIsNone(data['rate'])

    def test_HR_simplification(self):
        """Holstein-Rivera simplifies K11."""
        data = qec_rate_with_perfectness(True, True)
        self.assertTrue(data['simplified_by_HR'])

    def test_universal_distance(self):
        """Code distance is universally 2."""
        for fam in ['heisenberg', 'affine', 'betagamma', 'virasoro', 'w3']:
            params = qec_parameters_by_family(fam)
            self.assertEqual(params['distance'], 2,
                             f"Distance != 2 for {fam}")

    def test_universal_rate_across_families(self):
        """Rate 1/2 for all standard families."""
        for fam in ['heisenberg', 'lattice', 'affine', 'betagamma',
                     'virasoro', 'w3']:
            params = qec_parameters_by_family(fam)
            self.assertEqual(params['rate'], Rational(1, 2),
                             f"Rate != 1/2 for {fam}")

    def test_symplectic_code_type(self):
        """Code type is symplectic for all families."""
        for fam in ['heisenberg', 'affine', 'virasoro', 'w3']:
            params = qec_parameters_by_family(fam)
            self.assertEqual(params['code_type'], 'symplectic',
                             f"Not symplectic for {fam}")

    def test_channels_heisenberg(self):
        """Heisenberg (class G): 0 channels."""
        params = qec_parameters_by_family('heisenberg')
        self.assertEqual(params['channels'], 0)

    def test_channels_affine(self):
        """Affine KM (class L): 1 channel."""
        params = qec_parameters_by_family('affine')
        self.assertEqual(params['channels'], 1)

    def test_channels_betagamma(self):
        """Beta-gamma (class C): 2 channels."""
        params = qec_parameters_by_family('betagamma')
        self.assertEqual(params['channels'], 2)

    def test_channels_virasoro(self):
        """Virasoro (class M): infinite channels."""
        params = qec_parameters_by_family('virasoro')
        self.assertEqual(params['channels'], -1)


# =========================================================================
#  3. PAGE CURVE SATURATION
# =========================================================================

class TestPageCurveSaturation(unittest.TestCase):
    """Tests for Page curve saturation genus."""

    def test_self_dual_all_corrections_vanish(self):
        """At c=13, ALL Page corrections vanish."""
        for g in range(1, 20):
            self.assertEqual(page_correction_genus(Rational(13), g), Rational(0),
                             f"Correction nonzero at c=13, g={g}")

    def test_self_dual_saturation_genus_1(self):
        """At c=13, saturation genus is 1."""
        self.assertEqual(page_saturation_genus(Rational(13)), 1)

    def test_antisymmetry(self):
        """Page corrections are antisymmetric under c <-> 26-c."""
        for c in [Rational(1), Rational(7), Rational(12), Rational(20)]:
            for g in range(1, 6):
                self.assertTrue(page_correction_antisymmetry(c, g),
                                f"Antisymmetry fails at c={c}, g={g}")

    def test_correction_genus1_c14(self):
        """delta^(1)(14) = (14-13) * 1/24 = 1/24."""
        self.assertEqual(page_correction_genus(Rational(14), 1), Rational(1, 24))

    def test_correction_genus1_c12(self):
        """delta^(1)(12) = (12-13) * 1/24 = -1/24."""
        self.assertEqual(page_correction_genus(Rational(12), 1), Rational(-1, 24))

    def test_correction_linearity(self):
        """delta^(g)(c) = (c-13) * lambda_g^FP."""
        for g in range(1, 6):
            for c in [Rational(1), Rational(7), Rational(20)]:
                expected = (c - 13) * faber_pandharipande(g)
                actual = page_correction_genus(c, g)
                self.assertEqual(actual, expected,
                                 f"Linearity fails at c={c}, g={g}")

    def test_page_time_classical(self):
        """Classical Page time = 3*S_BH/13."""
        data = page_curve_shadow_cohft(Rational(13), 100)
        self.assertEqual(data['page_time_classical'], Rational(300, 13))

    def test_page_curve_self_dual_entropy(self):
        """At c=13, Page entropy = S_BH/2."""
        data = page_curve_shadow_cohft(Rational(13), 100)
        # S_page = (c/6) * t_P = (13/6) * (300/13) = 300/6 = 50
        self.assertEqual(data['S_page_classical'], Rational(50))
        # = S_BH / 2 = 100/2 = 50
        self.assertEqual(data['S_page_classical'], Rational(100) / 2)

    def test_saturation_finite_for_all_c(self):
        """Saturation genus is finite for all reasonable c."""
        for c in [Rational(1, 2), Rational(1), Rational(13),
                  Rational(25), Rational(26)]:
            g_sat = page_saturation_genus(c)
            self.assertLess(g_sat, 100, f"g_sat too large at c={c}")

    def test_saturation_table_structure(self):
        """Saturation table has expected entries."""
        table = page_saturation_table()
        self.assertGreaterEqual(len(table), 5)
        # c=13 entry should have g_sat = 1
        c13_entries = [row for row in table if row['c'] == 13]
        self.assertEqual(len(c13_entries), 1)
        self.assertEqual(c13_entries[0]['g_sat'], 1)

    def test_page_correction_decay(self):
        """Page corrections decay factorially (Bernoulli numbers)."""
        c = Rational(20)
        corrections = [abs(float(page_correction_genus(c, g))) for g in range(1, 8)]
        # Each correction should be smaller than the previous
        for i in range(1, len(corrections)):
            self.assertLess(corrections[i], corrections[i - 1],
                            f"Corrections not decreasing at g={i+1}")


# =========================================================================
#  4. W_3 CODE DISTANCE AND INFINITE-DEPTH QEC
# =========================================================================

class TestW3CodeParameters(unittest.TestCase):
    """Tests for W_3 code parameters."""

    def test_w3_rate(self):
        """W_3 code rate is 1/2."""
        params = w3_code_parameters()
        self.assertEqual(params['rate'], Rational(1, 2))

    def test_w3_distance(self):
        """W_3 code distance is 2."""
        params = w3_code_parameters()
        self.assertEqual(params['distance'], 2)

    def test_w3_class_M(self):
        """W_3 is class M (infinite shadow depth)."""
        params = w3_code_parameters()
        self.assertEqual(params['shadow_class'], 'M')

    def test_w3_infinite_channels(self):
        """W_3 has infinite redundancy channels."""
        params = w3_code_parameters()
        self.assertEqual(params['channels'], -1)

    def test_w3_symplectic(self):
        """W_3 code is symplectic."""
        params = w3_code_parameters()
        self.assertEqual(params['code_type'], 'symplectic')

    def test_w3_convergent_large_c(self):
        """W_3 recovery converges for large c."""
        params = w3_code_parameters(Rational(50))
        self.assertTrue(params['convergent'])

    def test_w3_kappa_c50(self):
        """kappa(W_3, c=50) = 50 * (H_3 - 1) = 50 * 5/6 = 125/3."""
        from compute.lib.entanglement_shadow_engine import kappa_wN
        self.assertEqual(kappa_wN(3, 50), Rational(125, 3))

    def test_w3_redundancy_structure(self):
        """W_3 redundancy analysis returns correct channel count."""
        analysis = w3_redundancy_analysis(Rational(50))
        self.assertEqual(analysis['n_channels'], 8)  # max_arity=10, channels = 10-2

    def test_w3_scalar_datum_not_recoverable(self):
        """The scalar datum kappa is fundamental, not recoverable."""
        analysis = w3_redundancy_analysis(Rational(50))
        self.assertIn('not recoverable', analysis['recovery_status'][2])

    def test_w3_cubic_independent(self):
        """The cubic shadow is an independent datum."""
        analysis = w3_redundancy_analysis(Rational(50))
        self.assertIn('independent', analysis['recovery_status'][3])

    def test_w3_quartic_determined(self):
        """The quartic shadow is determined by MC from lower arities."""
        analysis = w3_redundancy_analysis(Rational(50))
        self.assertIn('determined by MC', analysis['recovery_status'][4])


# =========================================================================
#  5. SHIFTED SYMPLECTIC STRUCTURE
# =========================================================================

class TestShiftedSymplecticQEC(unittest.TestCase):
    """Tests for the shifted symplectic QEC inner product."""

    def test_shift_minus_one(self):
        """Shifted symplectic degree is -1 at all genera."""
        for g in range(1, 10):
            self.assertEqual(shifted_symplectic_degree(g), -1,
                             f"Wrong shift at genus {g}")

    def test_verdier_isotropy_koszul(self):
        """Verdier isotropy gives code/error decoupling."""
        data = verdier_pairing_isotropy(True)
        self.assertTrue(data['code_error_decoupled'])
        self.assertEqual(data['code_type'], 'symplectic')

    def test_verdier_non_koszul_failure(self):
        """Non-Koszul: no code/error decoupling."""
        data = verdier_pairing_isotropy(False)
        self.assertFalse(data['code_error_decoupled'])

    def test_symplectic_metrics_genus1(self):
        """At genus 1: dim Q_1 = 1, dim C_1 = 2."""
        metrics = symplectic_code_metrics(1)
        self.assertEqual(metrics['dim_code'], 1)
        self.assertEqual(metrics['dim_ambient'], 2)
        self.assertEqual(metrics['rate'], Rational(1, 2))

    def test_symplectic_rate_all_genera(self):
        """Rate 1/2 at all genera."""
        for g in range(1, 5):
            metrics = symplectic_code_metrics(g)
            self.assertEqual(metrics['rate'], Rational(1, 2))

    def test_inner_product_source(self):
        """Inner product is the (-1)-shifted symplectic Verdier pairing."""
        data = verdier_pairing_isotropy(True)
        self.assertIn('Verdier', data['inner_product_source'])
        self.assertIn('-1', data['inner_product_source'])


# =========================================================================
#  6. DT PARTITION FUNCTION
# =========================================================================

class TestDTPartitionFunction(unittest.TestCase):
    """Tests for DT partition function for sl_2."""

    def test_dt_chi_M1(self):
        """chi(M_1) = dim(sl_2) = 3."""
        data = dt_partition_function_sl2()
        self.assertEqual(data['chi_M1'], 3)

    def test_dt_constant_term(self):
        """DT partition function starts at 1."""
        data = dt_partition_function_sl2()
        self.assertEqual(data['coeffs'][0], Rational(1))

    def test_dt_linear_term(self):
        """Coefficient of q^1 in prod(1-q^n)^{-3} = 3."""
        data = dt_partition_function_sl2()
        self.assertEqual(data['coeffs'][1], Rational(3))

    def test_dt_quadratic_term(self):
        """Coefficient of q^2 in prod(1-q^n)^{-3} = 9."""
        # (1-q)^{-3} contributes C(4,2) = 6 at q^2
        # (1-q^2)^{-3} contributes C(3,2) = 3 at q^2
        # Total: 6 + 3 = 9
        data = dt_partition_function_sl2()
        self.assertEqual(data['coeffs'][2], Rational(9))

    def test_coha_entropy_verification(self):
        """DT-derived entropy agrees with Calabrese-Cardy."""
        for k in [Rational(1), Rational(2), Rational(4)]:
            data = coha_entropy_from_dt(k)
            self.assertTrue(data['verification'],
                            f"DT entropy disagrees at k={k}")

    def test_coha_entropy_level1(self):
        """S_EE(V_1(sl_2)) = c/3 = 1/3 (AP39: use c, not kappa)."""
        data = coha_entropy_from_dt(Rational(1))
        c = central_charge_sl2(Rational(1))
        self.assertEqual(c, Rational(1))
        self.assertEqual(data['S_EE'], Rational(1, 3))

    def test_coha_entropy_level4(self):
        """S_EE(V_4(sl_2)) = c/3 = 2/3."""
        data = coha_entropy_from_dt(Rational(4))
        self.assertEqual(data['S_EE'], Rational(2, 3))


# =========================================================================
#  7. MULTI-PATH VERIFICATION
# =========================================================================

class TestMultiPathVerification(unittest.TestCase):
    """Multi-path verification of all key results."""

    def test_km_complementarity_multipath(self):
        """All 4 paths verify KM complementarity."""
        for k in [Rational(1), Rational(2), Rational(5), Rational(10)]:
            checks = verify_km_entanglement_complementarity(k)
            for key, val in checks.items():
                self.assertTrue(val, f"Check {key} failed at k={k}")

    def test_page_correction_properties(self):
        """All structural properties of Page corrections hold."""
        checks = verify_page_correction_properties()
        for key, val in checks.items():
            self.assertTrue(val, f"Property {key} failed")

    def test_qec_universality(self):
        """QEC parameters are universal across families."""
        checks = verify_qec_universality()
        for key, val in checks.items():
            self.assertTrue(val, f"Universality {key} failed")

    def test_shifted_symplectic_independence(self):
        """Shifted symplectic degree is genus-independent."""
        checks = verify_shifted_symplectic_independence()
        for key, val in checks.items():
            self.assertTrue(val, f"Independence {key} failed")

    def test_virasoro_vs_km_complementarity(self):
        """Virasoro: kappa + kappa' = 13. KM: kappa + kappa' = 0.
        These are DIFFERENT (AP24)."""
        # Virasoro
        kappa_vir = kappa_virasoro(Rational(10))
        kappa_vir_d = kappa_virasoro(Rational(16))  # 26 - 10
        self.assertEqual(kappa_vir + kappa_vir_d, Rational(13))

        # KM sl_2
        kappa_km = kappa_affine_sl2(Rational(1))
        kappa_km_d = kappa_affine_sl2_dual(Rational(1))
        self.assertEqual(kappa_km + kappa_km_d, Rational(0))

    def test_entanglement_uses_c_not_kappa(self):
        """The Calabrese-Cardy formula uses c/3, NOT 2*kappa/3 (AP39/AP48).
        For Virasoro: c = 2*kappa, so c/3 = 2*kappa/3 (agree).
        For KM: c != 2*kappa, so they DISAGREE."""
        # Virasoro: agree
        c_vir = Rational(10)
        kappa_vir = kappa_virasoro(c_vir)
        self.assertEqual(c_vir / 3, 2 * kappa_vir / 3)

        # KM sl_2: disagree
        k = Rational(1)
        c_km = central_charge_sl2(k)
        kappa_km = kappa_affine_sl2(k)
        self.assertNotEqual(c_km / 3, 2 * kappa_km / 3)
        # c/3 = 1/3, 2*kappa/3 = 2*(9/4)/3 = 3/2
        self.assertEqual(c_km / 3, Rational(1, 3))
        self.assertEqual(2 * kappa_km / 3, Rational(3, 2))


# =========================================================================
#  8. FULL ANALYSIS AND LANDSCAPE CENSUS
# =========================================================================

class TestFullAnalysis(unittest.TestCase):
    """Tests for the full entanglement rectification analysis."""

    def test_full_analysis_structure(self):
        """Full analysis returns all five components."""
        result = full_entanglement_rectification(Rational(13), Rational(1))
        self.assertIn('virasoro', result)
        self.assertIn('coha', result)
        self.assertIn('qec', result)
        self.assertIn('page', result)
        self.assertIn('w3', result)
        self.assertIn('symplectic', result)

    def test_full_analysis_self_dual(self):
        """Self-dual c=13 analysis."""
        result = full_entanglement_rectification(Rational(13), Rational(1))
        self.assertTrue(result['virasoro']['self_dual'])
        self.assertEqual(result['page']['saturation_genus'], 1)

    def test_landscape_census_structure(self):
        """Census has all standard families."""
        census = entanglement_landscape_census()
        self.assertGreaterEqual(len(census), 6)

    def test_landscape_census_universal_rate(self):
        """All families have rate 1/2."""
        census = entanglement_landscape_census()
        for entry in census:
            self.assertEqual(entry['qec_rate'], Rational(1, 2),
                             f"Rate != 1/2 for {entry['family']}")

    def test_landscape_census_universal_distance(self):
        """All families have distance 2."""
        census = entanglement_landscape_census()
        for entry in census:
            self.assertEqual(entry['qec_distance'], 2,
                             f"Distance != 2 for {entry['family']}")

    def test_landscape_census_symplectic(self):
        """All families have symplectic code type."""
        census = entanglement_landscape_census()
        for entry in census:
            self.assertEqual(entry['code_type'], 'symplectic',
                             f"Not symplectic for {entry['family']}")

    def test_landscape_census_positive_entropy(self):
        """All families with positive kappa have positive entropy."""
        census = entanglement_landscape_census()
        for entry in census:
            if entry['kappa'] > 0:
                self.assertGreater(entry['S_EE_coeff'], 0,
                                   f"Non-positive S_EE for {entry['family']}")


# =========================================================================
#  9. BEILINSON ANTI-PATTERN GUARDS
# =========================================================================

class TestBeilinsonAntiPatternGuards(unittest.TestCase):
    """Tests that verify known anti-patterns are NOT present."""

    def test_AP24_km_not_virasoro(self):
        """AP24: kappa + kappa' = 0 for KM, NOT 13.
        The complementarity constant 13 is SPECIFIC to Virasoro."""
        self.assertEqual(kappa_affine_sl2(Rational(1)) +
                         kappa_affine_sl2_dual(Rational(1)), Rational(0))
        # NOT 13:
        self.assertNotEqual(kappa_affine_sl2(Rational(1)) +
                            kappa_affine_sl2_dual(Rational(1)), Rational(13))

    def test_AP39_kappa_ne_c_over_2_for_km(self):
        """AP39: kappa != c/2 for non-Virasoro families."""
        k = Rational(1)
        kappa = kappa_affine_sl2(k)
        c = central_charge_sl2(k)
        self.assertNotEqual(kappa, c / 2)

    def test_AP48_kappa_family_dependent(self):
        """AP48: kappa depends on the full algebra, not just Virasoro sub."""
        # For sl_2 at level 1: kappa = 9/4, c = 1
        # The Virasoro formula would give kappa = c/2 = 1/2
        # The correct formula gives kappa = 9/4
        self.assertNotEqual(kappa_affine_sl2(Rational(1)),
                            central_charge_sl2(Rational(1)) / 2)

    def test_AP14_koszulness_ne_formality(self):
        """AP14: All standard families are Koszul. Class M (Virasoro, W_3)
        are Koszul but NOT Swiss-cheese formal. Shadow depth classifies
        complexity WITHIN the Koszul world."""
        # W_3 is Koszul (class M) but has infinite shadow depth
        params = qec_parameters_by_family('w3')
        self.assertTrue(params['lagrangian'])  # Koszul => Lagrangian
        self.assertEqual(params['shadow_class'], 'M')  # infinite depth
        self.assertEqual(params['channels'], -1)  # infinite channels

    def test_AP25_bar_ne_cobar_ne_verdier(self):
        """AP25: The QEC uses bar (encoding), cobar (decoding), and
        Verdier (inner product). These are THREE DIFFERENT operations."""
        data = verdier_pairing_isotropy(True)
        # The inner product comes from Verdier, not bar or cobar
        self.assertIn('Verdier', data['inner_product_source'])

    def test_AP42_code_distance_not_shadow_depth(self):
        """AP42: Code distance d=2 is universal, NOT equal to shadow depth.
        Shadow depth controls redundancy channels, not distance."""
        # Heisenberg: depth 2, distance 2 (coincidence)
        params_h = qec_parameters_by_family('heisenberg')
        self.assertEqual(params_h['distance'], 2)
        self.assertEqual(params_h['r_max'], 2)

        # Virasoro: depth infinite, distance STILL 2
        params_v = qec_parameters_by_family('virasoro')
        self.assertEqual(params_v['distance'], 2)
        self.assertEqual(params_v['r_max'], -1)  # infinite

        # The distance is universal; depth is not
        self.assertEqual(params_h['distance'], params_v['distance'])
        self.assertNotEqual(params_h['r_max'], params_v['r_max'])


if __name__ == '__main__':
    unittest.main()
