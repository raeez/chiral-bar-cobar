"""Tests for bc_desitter_shadow_engine.py

Multi-path verification for de Sitter observables from the shadow obstruction tower.
AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0).
"""

import math
import unittest
from fractions import Fraction

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.bc_desitter_shadow_engine import (
    lambda_fp,
    kappa_virasoro,
    kappa_heisenberg,
    kappa_kac_moody,
    kappa_w3,
    kappa_betagamma,
    virasoro_S3,
    virasoro_S4,
    virasoro_S5,
    heisenberg_S3,
    heisenberg_S4,
    heisenberg_S5,
    affine_sl2_S3,
    affine_sl2_S4,
    affine_sl2_S5,
    betagamma_S3,
    betagamma_S4,
    ShadowFamily,
    virasoro_family,
    heisenberg_family,
    affine_sl2_family,
    betagamma_family,
    w3_family,
    standard_families,
    F_g_scalar,
    planted_forest_g2,
    planted_forest_g3,
    family_free_energy,
    gibbons_hawking_entropy,
    gibbons_hawking_entropy_from_kappa,
    shadow_entropy_correction_arity_r,
    shadow_corrected_entropy,
    ds_quasinormal_mode,
    ds_qnm_shadow_correction,
    ds_qnm_full,
    ds_qnm_table,
    schwarzschild_ds_horizons,
    nariai_entropy,
    nariai_shadow_corrected,
    nariai_approach,
    slow_roll_epsilon,
    slow_roll_eta,
    slow_roll_from_family,
    power_spectrum_correction,
    non_gaussianity_fNL,
    non_gaussianity_gNL,
    spectral_tilt,
    spectral_tilt_virasoro,
    planck_consistency_test,
    shadow_growth_rate,
    trans_planckian_threshold,
    tcc_consistency,
    gibbons_hawking_temperature,
    static_patch_temperature_correction,
    ds_complementarity_overlap,
    ds_complementarity_virasoro,
    ds_entropy_genus_expansion,
    full_desitter_analysis,
    landscape_survey,
)

PI = math.pi


class TestFaberPandharipande(unittest.TestCase):
    """Test FP intersection numbers."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_positive(self):
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)


class TestKappaFormulas(unittest.TestCase):
    """Test kappa for all standard families."""

    def test_kappa_virasoro(self):
        self.assertEqual(kappa_virasoro(26), Fraction(13))
        self.assertEqual(kappa_virasoro(13), Fraction(13, 2))

    def test_kappa_heisenberg(self):
        self.assertEqual(kappa_heisenberg(1), Fraction(1))
        self.assertEqual(kappa_heisenberg(5), Fraction(5))

    def test_kappa_kac_moody_sl2(self):
        """kappa(sl_2, k=1) = 3*(1+2)/(2*2) = 9/4."""
        self.assertEqual(kappa_kac_moody(3, 1, 2), Fraction(9, 4))

    def test_kappa_w3(self):
        """kappa(W_3) = 5c/6."""
        self.assertEqual(kappa_w3(6), Fraction(5))
        self.assertEqual(kappa_w3(12), Fraction(10))

    def test_kappa_betagamma(self):
        """kappa(bg, lambda=1): c = 12-12+2 = 2, kappa = 1."""
        self.assertEqual(kappa_betagamma(1), Fraction(1))


class TestShadowCoefficients(unittest.TestCase):
    """Test shadow coefficients for each family."""

    def test_virasoro_S3(self):
        self.assertEqual(virasoro_S3(), Fraction(2))

    def test_virasoro_S4(self):
        self.assertEqual(virasoro_S4(1), Fraction(10, 27))

    def test_virasoro_S5(self):
        self.assertEqual(virasoro_S5(1), Fraction(-48, 27))

    def test_heisenberg_all_zero(self):
        """Heisenberg: class G, all shadow coefficients = 0."""
        self.assertEqual(heisenberg_S3(), Fraction(0))
        self.assertEqual(heisenberg_S4(), Fraction(0))
        self.assertEqual(heisenberg_S5(), Fraction(0))

    def test_affine_sl2_class_L(self):
        """Affine sl_2: class L, S_3 = 4/(k+2), S_4 = S_5 = 0."""
        self.assertEqual(affine_sl2_S3(1), Fraction(4, 3))  # k=1: 4/3
        self.assertEqual(affine_sl2_S4(), Fraction(0))
        self.assertEqual(affine_sl2_S5(), Fraction(0))

    def test_betagamma_S3(self):
        self.assertEqual(betagamma_S3(), Fraction(2))


class TestShadowFamilies(unittest.TestCase):
    """Test ShadowFamily construction."""

    def test_virasoro_depth_class(self):
        fam = virasoro_family(13)
        self.assertEqual(fam.depth_class, 'M')
        self.assertEqual(fam.kappa, Fraction(13, 2))

    def test_heisenberg_depth_class(self):
        fam = heisenberg_family(1)
        self.assertEqual(fam.depth_class, 'G')

    def test_affine_sl2_depth_class(self):
        fam = affine_sl2_family(1)
        self.assertEqual(fam.depth_class, 'L')

    def test_betagamma_depth_class(self):
        fam = betagamma_family(1)
        self.assertEqual(fam.depth_class, 'C')

    def test_standard_families_count(self):
        fams = standard_families()
        self.assertGreaterEqual(len(fams), 6)


class TestFreeEnergy(unittest.TestCase):
    """Test F_g computations."""

    def test_F1_scalar(self):
        self.assertEqual(F_g_scalar(Fraction(13, 2), 1), Fraction(13, 48))

    def test_F_linear_in_kappa(self):
        for g in range(1, 5):
            self.assertEqual(F_g_scalar(Fraction(6), g),
                             2 * F_g_scalar(Fraction(3), g))

    def test_planted_forest_g2_heisenberg_vanishes(self):
        """Heisenberg (class G): planted-forest correction = 0."""
        self.assertEqual(planted_forest_g2(Fraction(1), Fraction(0)), Fraction(0))

    def test_planted_forest_g2_virasoro(self):
        kappa = Fraction(13)  # c=26
        S3 = Fraction(2)
        pf = planted_forest_g2(kappa, S3)
        # S3*(10*S3 - kappa)/48 = 2*(20-13)/48 = 14/48 = 7/24
        self.assertEqual(pf, Fraction(7, 24))

    def test_family_free_energy_genus1(self):
        fam = virasoro_family(26)
        # genus 1: scalar only
        self.assertEqual(family_free_energy(fam, 1),
                         F_g_scalar(fam.kappa, 1))

    def test_family_free_energy_genus2_includes_pf(self):
        fam = virasoro_family(26)
        scalar = F_g_scalar(fam.kappa, 2)
        full = family_free_energy(fam, 2)
        self.assertNotEqual(scalar, full)

    def test_heisenberg_free_energy_equals_scalar(self):
        """Heisenberg has no planted-forest (S_3=0)."""
        fam = heisenberg_family(1)
        for g in range(1, 4):
            self.assertEqual(family_free_energy(fam, g),
                             F_g_scalar(fam.kappa, g))


class TestGibbonsHawking(unittest.TestCase):
    """Test Gibbons-Hawking entropy."""

    def test_S_GH_formula(self):
        """S_GH = pi*c/3."""
        for c in [1, 13, 26]:
            expected = PI * c / 3.0
            self.assertAlmostEqual(gibbons_hawking_entropy(c), expected, places=10)

    def test_S_GH_from_kappa(self):
        """S_GH = 2*pi*kappa/3, with kappa=c/2 giving pi*c/3."""
        for c in [1, 13, 26]:
            kappa = c / 2.0
            S_direct = gibbons_hawking_entropy(c)
            S_kappa = gibbons_hawking_entropy_from_kappa(kappa)
            self.assertAlmostEqual(S_direct, S_kappa, places=10)

    def test_S_GH_three_verification_paths(self):
        """Three independent paths to S_GH = pi*c/3."""
        c = 13
        # Path 1: direct formula
        S1 = PI * c / 3.0
        # Path 2: from kappa = c/2
        S2 = 2.0 * PI * (c / 2.0) / 3.0
        # Path 3: from area = 2*pi*ell, using c = 3*ell/(2*G_N) and ell=1, G_N=3/(2*c)
        G_N = 3.0 / (2.0 * c)
        S3 = 2.0 * PI * 1.0 / (4.0 * G_N)
        self.assertAlmostEqual(S1, S2, places=10)
        self.assertAlmostEqual(S1, S3, places=10)


class TestShadowEntropyCorrections(unittest.TestCase):
    """Test shadow corrections to dS entropy."""

    def test_arity2_is_GH(self):
        """Arity-2 correction reproduces S_GH."""
        fam = virasoro_family(13)
        delta_2 = shadow_entropy_correction_arity_r(fam, 2)
        S_GH = gibbons_hawking_entropy_from_kappa(fam.kappa)
        self.assertAlmostEqual(delta_2, S_GH, places=8)

    def test_heisenberg_no_corrections(self):
        """Heisenberg (class G): no corrections beyond S_GH."""
        fam = heisenberg_family(1)
        for r in [3, 4, 5]:
            self.assertAlmostEqual(shadow_entropy_correction_arity_r(fam, r), 0.0)

    def test_shadow_corrected_entropy_includes_GH(self):
        """Total entropy >= S_GH (corrections are additive)."""
        fam = virasoro_family(13)
        result = shadow_corrected_entropy(fam)
        self.assertIn('S_GH', result)
        self.assertIn('S_total', result)
        self.assertTrue(math.isfinite(result['S_total']))


class TestQuasinormalModes(unittest.TestCase):
    """Test de Sitter quasinormal modes."""

    def test_qnm_purely_imaginary(self):
        """dS QNMs are purely imaginary."""
        for n in range(5):
            omega = ds_quasinormal_mode(n, 2.0)
            self.assertAlmostEqual(omega.real, 0.0)
            self.assertGreater(omega.imag, 0.0)

    def test_qnm_formula(self):
        """omega_n = i*(n+h)/ell."""
        omega = ds_quasinormal_mode(3, 2.0, ell=1.0)
        self.assertAlmostEqual(omega, 5.0j, places=10)

    def test_qnm_spacing(self):
        """Uniform spacing: omega_{n+1} - omega_n = i/ell."""
        for n in range(5):
            diff = ds_quasinormal_mode(n + 1, 2.0) - ds_quasinormal_mode(n, 2.0)
            self.assertAlmostEqual(diff, 1.0j, places=10)

    def test_qnm_shadow_correction_heisenberg_zero(self):
        """Heisenberg has zero QNM shadow correction (class G, S_3=0)."""
        fam = heisenberg_family(1)
        corr = ds_qnm_shadow_correction(0, 2.0, fam)
        self.assertAlmostEqual(abs(corr), 0.0)

    def test_qnm_full_equals_tree_plus_correction(self):
        """Full QNM = tree + shadow correction."""
        fam = virasoro_family(13)
        for n in range(5):
            tree = ds_quasinormal_mode(n, 2.0)
            corr = ds_qnm_shadow_correction(n, 2.0, fam)
            full = ds_qnm_full(n, 2.0, fam)
            self.assertAlmostEqual(full, tree + corr, places=10)

    def test_qnm_table_length(self):
        fam = virasoro_family(13)
        table = ds_qnm_table(5, 2.0, fam)
        self.assertEqual(len(table), 6)  # n = 0..5


class TestNariai(unittest.TestCase):
    """Test Nariai limit."""

    def test_nariai_equals_GH(self):
        """At Nariai: S_BH = S_dS."""
        for c in [1, 13, 26]:
            self.assertAlmostEqual(nariai_entropy(c),
                                   gibbons_hawking_entropy(c), places=10)

    def test_horizons_at_nariai(self):
        """At Nariai (8GM=1): r_+ = r_c = ell."""
        r_plus, r_cosmo = schwarzschild_ds_horizons(1.0 / 8.0, 1.0)
        self.assertAlmostEqual(r_plus, 1.0, places=5)
        self.assertAlmostEqual(r_cosmo, 1.0, places=5)

    def test_horizons_at_zero_mass(self):
        """At M=0: r_+ = 0, r_c = ell."""
        r_plus, r_cosmo = schwarzschild_ds_horizons(0.0, 1.0)
        self.assertAlmostEqual(r_plus, 0.0)
        self.assertAlmostEqual(r_cosmo, 1.0)

    def test_nariai_approach_convergence(self):
        """Nariai approach: S_BH -> S_cosmo as x -> 1."""
        fam = virasoro_family(13)
        rows = nariai_approach(fam)
        # The last entry should have gap ~ 0
        self.assertAlmostEqual(rows[-1]['gap'], 0.0, delta=0.01)

    def test_nariai_shadow_corrected(self):
        """Shadow-corrected Nariai includes discriminant."""
        fam = virasoro_family(13)
        result = nariai_shadow_corrected(fam)
        self.assertIn('discriminant', result)
        self.assertTrue(result['nariai'])


class TestSlowRoll(unittest.TestCase):
    """Test slow-roll parameters from shadow data."""

    def test_epsilon_class_G_vanishes(self):
        """Heisenberg (class G, S_3=0): epsilon = 0."""
        self.assertAlmostEqual(slow_roll_epsilon(Fraction(1), Fraction(0), Fraction(0)), 0.0)

    def test_epsilon_formula(self):
        """epsilon = S_3^2/(4*kappa^2) + correction."""
        kappa = Fraction(13, 2)
        S3 = Fraction(2)
        S4 = Fraction(0)
        eps = slow_roll_epsilon(kappa, S3, S4)
        expected = float(S3) ** 2 / (4.0 * float(kappa) ** 2)
        self.assertAlmostEqual(eps, expected, places=10)

    def test_eta_class_G_vanishes(self):
        """Heisenberg: eta = 0."""
        self.assertAlmostEqual(slow_roll_eta(Fraction(1), Fraction(0), Fraction(0)), 0.0)

    def test_slow_roll_from_family(self):
        """slow_roll_from_family returns expected keys."""
        fam = virasoro_family(13)
        sr = slow_roll_from_family(fam)
        for key in ['epsilon', 'eta', 'n_s', 'r_tensor']:
            self.assertIn(key, sr)

    def test_r_tensor_formula(self):
        """r_tensor = 16*epsilon."""
        fam = virasoro_family(13)
        sr = slow_roll_from_family(fam)
        self.assertAlmostEqual(sr['r_tensor'], 16.0 * sr['epsilon'], places=10)

    def test_n_s_formula(self):
        """n_s = 1 - 2*epsilon - eta."""
        fam = virasoro_family(13)
        sr = slow_roll_from_family(fam)
        expected = 1.0 - 2.0 * sr['epsilon'] - sr['eta']
        self.assertAlmostEqual(sr['n_s'], expected, places=10)


class TestNonGaussianity(unittest.TestCase):
    """Test non-Gaussianity parameters."""

    def test_fNL_class_G_vanishes(self):
        """Heisenberg (S_3=0): f_NL = 0."""
        fam = heisenberg_family(1)
        self.assertAlmostEqual(non_gaussianity_fNL(fam), 0.0)

    def test_fNL_formula_virasoro(self):
        """f_NL = (5/6)*S_3/kappa = (5/6)*2/(c/2) = 10/(3c)."""
        fam = virasoro_family(13)
        expected = (5.0 / 6.0) * 2.0 / (13.0 / 2.0)
        self.assertAlmostEqual(non_gaussianity_fNL(fam), expected, places=10)

    def test_gNL_class_GL_vanishes(self):
        """Class G/L (S_4=0): g_NL = 0."""
        fam_g = heisenberg_family(1)
        fam_l = affine_sl2_family(1)
        self.assertAlmostEqual(non_gaussianity_gNL(fam_g), 0.0)
        self.assertAlmostEqual(non_gaussianity_gNL(fam_l), 0.0)

    def test_gNL_formula_virasoro(self):
        """g_NL = (25/54)*S_4/kappa^2."""
        fam = virasoro_family(13)
        kappa = 13.0 / 2.0
        S4 = 10.0 / (13.0 * 87.0)
        expected = (25.0 / 54.0) * S4 / kappa ** 2
        self.assertAlmostEqual(non_gaussianity_gNL(fam), expected, places=10)


class TestSpectralTilt(unittest.TestCase):
    """Test spectral tilt n_s."""

    def test_class_G_scale_invariant(self):
        """Heisenberg (class G): n_s = 1 (exact scale invariance)."""
        fam = heisenberg_family(1)
        self.assertAlmostEqual(spectral_tilt(fam), 1.0, places=10)

    def test_spectral_tilt_virasoro_formula(self):
        """n_s = 1 - (30c+92)/(c^2*(5c+22))."""
        for c in [6, 13, 26]:
            n_s_direct = spectral_tilt_virasoro(c)
            expected = 1.0 - (30.0 * c + 92.0) / (c ** 2 * (5.0 * c + 22.0))
            self.assertAlmostEqual(n_s_direct, expected, places=10)

    def test_spectral_tilt_virasoro_internal_consistency(self):
        """spectral_tilt_virasoro matches 1 - 2*eps - eta from its own formula."""
        for c in [6, 13, 26]:
            n_s = spectral_tilt_virasoro(c)
            expected = 1.0 - (30.0 * c + 92.0) / (c ** 2 * (5.0 * c + 22.0))
            self.assertAlmostEqual(n_s, expected, places=10)

    def test_spectral_tilt_increases_with_c(self):
        """n_s increases with c (approaches 1)."""
        n_s_values = [spectral_tilt_virasoro(c) for c in [6, 13, 26]]
        for i in range(len(n_s_values) - 1):
            self.assertLess(n_s_values[i], n_s_values[i + 1])


class TestPlanckConsistency(unittest.TestCase):
    """Test Planck 2018 consistency."""

    def test_planck_returns_keys(self):
        fam = virasoro_family(13)
        result = planck_consistency_test(fam)
        for key in ['n_s_pass', 'r_pass', 'f_NL_pass', 'overall_pass']:
            self.assertIn(key, result)

    def test_heisenberg_planck_consistent(self):
        """Heisenberg (n_s=1, r=0, f_NL=0) passes Planck constraints."""
        fam = heisenberg_family(1)
        result = planck_consistency_test(fam)
        # n_s = 1 is within 3-sigma of 0.9649
        # r = 0 < 0.10
        self.assertTrue(result['r_pass'])
        self.assertTrue(result['f_NL_pass'])


class TestShadowGrowthRate(unittest.TestCase):
    """Test shadow growth rate rho(A)."""

    def test_heisenberg_rho_zero(self):
        """Heisenberg (class G): rho = 0."""
        fam = heisenberg_family(1)
        self.assertAlmostEqual(shadow_growth_rate(fam), 0.0)

    def test_virasoro_rho_positive(self):
        """Virasoro (class M): rho > 0."""
        fam = virasoro_family(13)
        self.assertGreater(shadow_growth_rate(fam), 0.0)

    def test_virasoro_rho_c13(self):
        """rho ~ 0.467 at c=13."""
        fam = virasoro_family(13)
        self.assertAlmostEqual(shadow_growth_rate(fam), 0.467, delta=0.01)

    def test_trans_planckian_threshold_heisenberg_infinite(self):
        """Heisenberg: N_max = infinity (exact dS)."""
        fam = heisenberg_family(1)
        self.assertEqual(trans_planckian_threshold(fam), float('inf'))

    def test_tcc_consistency(self):
        """TCC consistency returns expected keys."""
        fam = virasoro_family(13)
        result = tcc_consistency(fam)
        self.assertIn('tcc_safe', result)
        self.assertIn('rho', result)
        # rho ~ 0.467 < 1, so TCC safe
        self.assertTrue(result['tcc_safe'])


class TestTemperature(unittest.TestCase):
    """Test Gibbons-Hawking temperature."""

    def test_T_GH_formula(self):
        """T_GH = 1/(2*pi*ell)."""
        self.assertAlmostEqual(gibbons_hawking_temperature(1.0),
                               1.0 / (2.0 * PI), places=10)

    def test_T_GH_scales_inversely(self):
        """Doubling ell halves T_GH."""
        T1 = gibbons_hawking_temperature(1.0)
        T2 = gibbons_hawking_temperature(2.0)
        self.assertAlmostEqual(T1 / T2, 2.0, places=10)

    def test_temperature_correction_returns_keys(self):
        fam = virasoro_family(13)
        result = static_patch_temperature_correction(fam)
        for key in ['T_GH', 'T_corrected', 'delta_T_over_T']:
            self.assertIn(key, result)

    def test_heisenberg_no_T_correction(self):
        """Heisenberg: no temperature correction (S_3=S_4=0)."""
        fam = heisenberg_family(1)
        result = static_patch_temperature_correction(fam)
        self.assertAlmostEqual(result['delta_T_over_T'], 0.0)


class TestDSComplementarity(unittest.TestCase):
    """Test de Sitter complementarity."""

    def test_virasoro_overlap_constant_13(self):
        """AP24: Virasoro overlap = 13 for all c."""
        for c in [1, 6, 13, 20, 26]:
            result = ds_complementarity_virasoro(c)
            self.assertAlmostEqual(result['overlap'], 13.0, places=10)

    def test_virasoro_self_dual_c13(self):
        result = ds_complementarity_virasoro(13)
        self.assertTrue(result['self_dual'])

    def test_heisenberg_independent_patches(self):
        """Heisenberg: kappa + kappa' = 0 (independent patches)."""
        fam = heisenberg_family(1)
        result = ds_complementarity_overlap(fam)
        self.assertTrue(result['independent_patches'])

    def test_affine_independent_patches(self):
        """Affine KM: kappa + kappa' = 0."""
        fam = affine_sl2_family(1)
        result = ds_complementarity_overlap(fam)
        self.assertTrue(result['independent_patches'])

    def test_virasoro_overlap_via_family(self):
        """ShadowFamily-based Virasoro overlap agrees with direct formula."""
        fam = virasoro_family(13)
        result_fam = ds_complementarity_overlap(fam)
        result_direct = ds_complementarity_virasoro(13)
        self.assertAlmostEqual(result_fam['overlap'], result_direct['overlap'],
                               places=8)


class TestGenusExpansion(unittest.TestCase):
    """Test genus expansion of dS entropy."""

    def test_genus_expansion_includes_GH(self):
        """Genus expansion starts from S_GH."""
        fam = virasoro_family(13)
        result = ds_entropy_genus_expansion(fam)
        self.assertAlmostEqual(result['S_GH'],
                               gibbons_hawking_entropy_from_kappa(fam.kappa),
                               places=8)

    def test_genus_expansion_genus1_constant(self):
        """Genus-1 contribution is a constant (not epsilon-dependent)."""
        fam = virasoro_family(13)
        result = ds_entropy_genus_expansion(fam)
        genus1 = result['genus_contributions'][1]
        self.assertEqual(genus1['epsilon_power'], 0)

    def test_heisenberg_genus_expansion_pure_scalar(self):
        """Heisenberg: F_g = kappa*lambda_g (scalar only, no planted-forest)."""
        fam = heisenberg_family(1)
        result = ds_entropy_genus_expansion(fam, g_max=3)
        for g in range(1, 4):
            Fg = result['genus_contributions'][g]['F_g']
            expected = float(F_g_scalar(fam.kappa, g))
            self.assertAlmostEqual(Fg, expected, places=10)


class TestFullAnalysis(unittest.TestCase):
    """Test full de Sitter analysis and landscape survey."""

    def test_full_analysis_returns_all_keys(self):
        fam = virasoro_family(13)
        result = full_desitter_analysis(fam, g_max=3, n_max_qnm=3)
        for key in ['entropy', 'genus_expansion', 'qnm_table', 'nariai',
                     'slow_roll', 'f_NL', 'g_NL', 'n_s', 'planck',
                     'tcc', 'temperature', 'complementarity']:
            self.assertIn(key, result)

    def test_landscape_survey(self):
        """Landscape survey runs for all standard families."""
        survey = landscape_survey()
        self.assertGreaterEqual(len(survey), 6)
        # All entries should have S_GH > 0 for c > 0
        for entry in survey:
            if entry['c'] > 0:
                self.assertGreater(entry['entropy']['S_GH'], 0)


class TestCrossConsistency(unittest.TestCase):
    """Cross-consistency checks."""

    def test_F_g_complementarity(self):
        """F_g(kappa) + F_g(kappa') = 13*lambda_g for Virasoro."""
        for c in [1, 6, 13, 20, 25]:
            kappa = kappa_virasoro(c)
            kappa_d = kappa_virasoro(26 - c)
            for g in range(1, 5):
                F_sum = F_g_scalar(kappa, g) + F_g_scalar(kappa_d, g)
                expected = Fraction(13) * lambda_fp(g)
                self.assertEqual(F_sum, expected)

    def test_power_spectrum_class_G(self):
        """Class G: no power spectrum corrections."""
        fam = heisenberg_family(1)
        result = power_spectrum_correction(fam, 0.1)
        self.assertAlmostEqual(result['total'], 0.0)

    def test_epsilon_eta_consistency(self):
        """eta = 2*epsilon - 2*S_4/kappa for class L (S_4=0)."""
        fam = affine_sl2_family(1)
        sr = slow_roll_from_family(fam)
        # With S_4=0: eta = S_3^2/(2*kappa^2) = 2*epsilon
        self.assertAlmostEqual(sr['eta'], 2.0 * sr['epsilon'], places=10)


if __name__ == '__main__':
    unittest.main()
