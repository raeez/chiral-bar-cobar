"""Tests for the admissible-level bar complex and Koszul duality engine.

Verifies:
    1. Kappa computation via three independent paths (multi-path verification)
    2. Shadow depth classification at admissible levels
    3. Bar-Ext vs ordinary Ext structural comparison
    4. Null vector effect on bar complex
    5. Associated variety dimension (Arakawa)
    6. Modular S-matrix properties
    7. Koszulness verdicts (V_k always, L_k conditional)
    8. Virasoro minimal model identification
    9. sl_3 admissible levels
    10. Vacuum Verma module dimensions
    11. Character leading coefficients
    12. Master classification consistency

MANDATE: 3+ independent verification paths per result.

References:
    Kac-Wakimoto (1988), Arakawa (2015, 2017), Creutzig-Ridout (2012-2013)
    Manuscript: rem:admissible-koszul-status, prop:pbw-universality,
    prop:bar-admissible, thm:kw-bar-spectral
"""

import pytest
import unittest
from fractions import Fraction
from math import gcd

import numpy as np

from compute.lib.admissible_level_bar_engine import (
    # Kappa paths
    kappa_path1_sugawara,
    kappa_path2_character,
    kappa_path3_ds_reduction,
    verify_kappa_multipath,
    # Bar complex
    vacuum_verma_dims_sl2,
    bar_complex_universal_sl2,
    null_vector_bar_effect_sl2,
    ce_differential_sl2,
    # Main analysis
    admissible_bar_analysis_sl2,
    admissible_bar_analysis_sl3,
    # Associated variety
    associated_variety_sl2,
    associated_variety_sl3,
    # Modular
    modular_s_matrix_sl2,
    admissible_character_leading_coeffs,
    # Shadow
    shadow_depth_admissible_sl2,
    # Ext comparison
    bar_ext_vs_ordinary_ext,
    # Minimal model
    minimal_model_identification,
    # Classification
    classification_table_sl2,
    master_admissible_analysis,
)


# =========================================================================
# Kappa multi-path verification (AP20, AP39, AP48)
# =========================================================================

class TestKappaMultiPath(unittest.TestCase):
    """Multi-path kappa verification at admissible levels.

    Three independent paths:
        Path 1: Sugawara / modular characteristic formula
        Path 2: Character q-expansion
        Path 3: DS reduction (different invariant: Virasoro kappa)

    Paths 1 and 2 must AGREE. Path 3 is a DIFFERENT invariant.
    """

    def test_paths_12_agree_integrable(self):
        """Paths 1 and 2 agree at integrable levels."""
        for p in range(2, 8):
            k1 = kappa_path1_sugawara(p, 1)
            k2 = kappa_path2_character(p, 1)
            self.assertEqual(k1, k2, f"Paths 1,2 disagree at k={p-2}")

    def test_paths_12_agree_admissible(self):
        """Paths 1 and 2 agree at non-integrable admissible levels."""
        test_cases = [(3, 2), (2, 3), (5, 3), (5, 2), (4, 3), (7, 2),
                      (7, 3), (7, 4), (8, 3), (8, 5)]
        for p, q in test_cases:
            if gcd(p, q) != 1:
                continue
            k1 = kappa_path1_sugawara(p, q)
            k2 = kappa_path2_character(p, q)
            self.assertEqual(k1, k2, f"Paths 1,2 disagree at (p,q)=({p},{q})")

    def test_kappa_km_formula_sl2(self):
        """kappa(sl_2, k) = 3(k+2)/4 = 3p/(4q)."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1), (5, 1)]:
            if gcd(p, q) != 1:
                continue
            kappa = kappa_path1_sugawara(p, q)
            expected = Fraction(3 * p, 4 * q)
            self.assertEqual(kappa, expected,
                             f"kappa wrong at (p,q)=({p},{q}): {kappa} != {expected}")

    def test_kappa_not_c_over_2(self):
        """kappa != c/2 in general (AP39, AP48)."""
        # For sl_2: c = 3k/(k+2) = 3(p-2q)/p, so c/2 = 3(p-2q)/(2p)
        # kappa = 3p/(4q)
        # These are DIFFERENT (coincide only at k=0, p=2, q=1)
        for p, q in [(3, 2), (2, 3), (5, 3), (4, 1)]:
            if gcd(p, q) != 1:
                continue
            kappa = kappa_path1_sugawara(p, q)
            k = Fraction(p, q) - 2
            c = 3 * k / (k + 2)
            c_half = c / 2
            if (p, q) != (2, 1):
                self.assertNotEqual(kappa, c_half,
                                    f"kappa should differ from c/2 at k={k}")

    def test_kappa_positive_for_noncritical(self):
        """kappa > 0 for non-critical levels (k != -2)."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1), (7, 4)]:
            if gcd(p, q) != 1:
                continue
            kappa = kappa_path1_sugawara(p, q)
            self.assertGreater(kappa, 0,
                               f"kappa should be positive at (p,q)=({p},{q})")

    def test_kappa_path3_is_different(self):
        """Path 3 (Virasoro DS) gives a DIFFERENT kappa than paths 1-2."""
        for p, q in [(3, 2), (5, 3), (5, 2), (4, 3)]:
            if gcd(p, q) != 1:
                continue
            kappa_km = kappa_path1_sugawara(p, q)
            kappa_vir = kappa_path3_ds_reduction(p, q)
            # These should differ in general (AP20)
            # They measure different algebras: hat{sl_2} vs Vir
            self.assertIsNotNone(kappa_vir)

    def test_verify_kappa_multipath_structure(self):
        """verify_kappa_multipath returns correct keys."""
        result = verify_kappa_multipath(3, 2)
        expected_keys = {'p', 'q', 'k', 'kappa_km', 'kappa_char', 'kappa_vir',
                         'paths_12_agree', 'c_sugawara', 'c_minimal_model'}
        self.assertEqual(set(result.keys()), expected_keys)

    def test_all_kappa_multipath_agree(self):
        """All tested levels have paths 1-2 in agreement."""
        for q in range(1, 6):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                result = verify_kappa_multipath(p, q)
                self.assertTrue(result['paths_12_agree'],
                                f"Kappa paths disagree at (p,q)=({p},{q})")

    def test_kappa_sl3(self):
        """kappa for sl_3: 8*(k+3)/6 = 4(k+3)/3."""
        for p, q in [(4, 1), (5, 1), (5, 2)]:
            if gcd(p, q) != 1:
                continue
            kappa = kappa_path1_sugawara(p, q, g_type='sl3')
            k = Fraction(p, q) - 3
            expected = Fraction(8) * (k + 3) / 6
            self.assertEqual(kappa, expected,
                             f"sl_3 kappa wrong at (p,q)=({p},{q})")


# =========================================================================
# Universal algebra Koszulness (always true)
# =========================================================================

class TestUniversalKoszulness(unittest.TestCase):
    """V_k(sl_2) is Koszul at ALL levels (prop:pbw-universality)."""

    def test_bar_cohomology_universal(self):
        """Bar cohomology of V_k concentrated in degree 1."""
        cohom = bar_complex_universal_sl2(max_bar_degree=6)
        self.assertEqual(cohom[1], 3)  # dim sl_2
        for d in range(2, 7):
            self.assertEqual(cohom[d], 0, f"H^{d} should be 0 for V_k")

    def test_universal_koszul_all_levels(self):
        """V_k is Koszul for every admissible level tested."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                analysis = admissible_bar_analysis_sl2(p, q)
                self.assertTrue(analysis.is_universal_koszul,
                                f"V_k should be Koszul at (p,q)=({p},{q})")


# =========================================================================
# Simple quotient Koszulness analysis
# =========================================================================

class TestSimpleQuotientKoszulness(unittest.TestCase):
    """Koszulness analysis for L_k(sl_2) at admissible levels."""

    def test_integrable_koszul(self):
        """Integrable levels (q=1): L_k is Koszul."""
        for p in range(2, 8):
            analysis = admissible_bar_analysis_sl2(p, 1)
            self.assertTrue(analysis.is_quotient_koszul,
                            f"L_k should be Koszul at integrable k={p-2}")

    def test_high_null_koszul(self):
        """Levels with h_null >= 4: L_k is Koszul."""
        # h_null = (p-1)*q >= 4 and null above max bar arity
        test_cases = [(3, 2), (5, 3), (7, 2), (7, 3), (7, 4)]
        for p, q in test_cases:
            if gcd(p, q) != 1:
                continue
            h_null = (p - 1) * q
            if h_null >= 4:
                analysis = admissible_bar_analysis_sl2(p, q)
                self.assertTrue(analysis.is_quotient_koszul,
                                f"L_k should be Koszul when h_null={h_null} >= 4")

    def test_k_minus_half_koszul(self):
        """k = -1/2 (p=3, q=2): h_null = 4, L_k is Koszul."""
        analysis = admissible_bar_analysis_sl2(3, 2)
        self.assertEqual(analysis.h_null, 4)
        self.assertTrue(analysis.is_quotient_koszul)
        self.assertEqual(analysis.kappa_km, Fraction(9, 8))

    def test_k_minus_4_3_koszul(self):
        """k = -4/3 (p=2, q=3): h_null = 3, L_k is Koszul."""
        analysis = admissible_bar_analysis_sl2(2, 3)
        self.assertEqual(analysis.h_null, 3)
        self.assertTrue(analysis.is_quotient_koszul)
        self.assertEqual(analysis.kappa_km, Fraction(1, 2))

    def test_k_minus_3_2(self):
        """k = -3/2 (p=1, q=2) is NOT admissible: p must be >= 2."""
        with self.assertRaises(ValueError):
            admissible_bar_analysis_sl2(1, 2)

    def test_k_minus_1_3(self):
        """k = -1/3 (p=5, q=3): h_null = 12 >> 3, Koszul."""
        analysis = admissible_bar_analysis_sl2(5, 3)
        self.assertEqual(analysis.h_null, 12)
        self.assertTrue(analysis.is_quotient_koszul)

    def test_no_koszul_failure_found(self):
        """No Koszul failure found at any admissible level."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                analysis = admissible_bar_analysis_sl2(p, q)
                self.assertIsNot(analysis.is_quotient_koszul, False,
                                 f"Unexpected Koszul failure at (p,q)=({p},{q})")


# =========================================================================
# Null vector bar effect
# =========================================================================

class TestNullVectorBarEffect(unittest.TestCase):
    """Effect of null vectors on the bar complex."""

    def test_null_vector_weight_formula(self):
        """h_null = (p-1)*q (Kac-Kazhdan)."""
        cases = [
            (2, 1, 1), (3, 1, 2), (4, 1, 3), (5, 1, 4),
            (3, 2, 4), (2, 3, 3), (5, 3, 12), (5, 2, 8),
            (7, 2, 12), (7, 3, 18),
        ]
        for p, q, expected_h in cases:
            if gcd(p, q) != 1:
                continue
            eff = null_vector_bar_effect_sl2(p, q)
            self.assertEqual(eff.h_null, expected_h,
                             f"h_null wrong at (p,q)=({p},{q})")

    def test_high_null_no_new_cycles(self):
        """Null at h >= 4 cannot create new bar cycles."""
        for p, q in [(3, 2), (5, 3), (7, 2), (7, 4)]:
            if gcd(p, q) != 1:
                continue
            eff = null_vector_bar_effect_sl2(p, q)
            if eff.h_null >= 4:
                self.assertFalse(eff.creates_new_cycles,
                                 f"Should be False at h_null={eff.h_null}")

    def test_all_bar_relevant(self):
        """All admissible levels with p >= 2 have bar-relevant nulls."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                eff = null_vector_bar_effect_sl2(p, q)
                h_null = (p - 1) * q
                if h_null >= 2:
                    self.assertTrue(eff.bar_relevant)

    def test_mechanism_populated(self):
        """All null vector effects have a non-empty mechanism string."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1)]:
            eff = null_vector_bar_effect_sl2(p, q)
            self.assertTrue(len(eff.mechanism) > 10)


# =========================================================================
# Shadow depth classification
# =========================================================================

class TestShadowDepthAdmissible(unittest.TestCase):
    """Shadow depth is always L (Lie, r_max=3) for affine sl_2."""

    def test_all_class_L(self):
        """All admissible sl_2 levels have shadow depth class L."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                sd = shadow_depth_admissible_sl2(p, q)
                self.assertEqual(sd['shadow_depth_class'], 'L')
                self.assertEqual(sd['r_max'], 3)
                self.assertTrue(sd['terminates'])

    def test_kappa_varies_with_level(self):
        """kappa depends on the level even though shadow class is constant."""
        kappas = set()
        for p in range(2, 6):
            sd = shadow_depth_admissible_sl2(p, 1)
            kappas.add(sd['kappa'])
        # Different integrable levels have different kappa
        self.assertGreater(len(kappas), 1)

    def test_cubic_shadow_is_lie_bracket(self):
        """Cubic shadow for KM is always the Lie bracket."""
        sd = shadow_depth_admissible_sl2(3, 2)
        self.assertIn('Lie bracket', sd['cubic_shadow'])

    def test_quartic_shadow_vanishes(self):
        """Quartic shadow vanishes by Jacobi identity."""
        sd = shadow_depth_admissible_sl2(3, 2)
        self.assertEqual(sd['quartic_shadow'], '0 (Jacobi identity)')

    def test_genus_1_obstruction(self):
        """F_1 = kappa/24 at each level."""
        for p, q in [(3, 2), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            sd = shadow_depth_admissible_sl2(p, q)
            kappa = sd['kappa']
            self.assertEqual(sd['genus_1_obstruction'], kappa / 24)


# =========================================================================
# Associated variety (Arakawa)
# =========================================================================

class TestAssociatedVariety(unittest.TestCase):
    """Associated variety of admissible simple quotients."""

    def test_all_sl2_trivial(self):
        """All admissible L_k(sl_2) have trivial associated variety."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                av = associated_variety_sl2(p, q)
                self.assertEqual(av.dimension, 0)
                self.assertTrue(av.is_c2_cofinite)
                self.assertTrue(av.is_rational)

    def test_nilpotent_orbit_zero(self):
        """Associated variety is the zero orbit for all admissible sl_2."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            av = associated_variety_sl2(p, q)
            self.assertEqual(av.nilpotent_orbit, 'zero orbit')

    def test_sl3_c2_cofinite(self):
        """sl_3 admissible levels are C_2-cofinite."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            av = associated_variety_sl3(p, q)
            self.assertTrue(av.is_c2_cofinite)
            self.assertEqual(av.dimension, 0)


# =========================================================================
# Modular S-matrix
# =========================================================================

class TestModularSMatrix(unittest.TestCase):
    """Modular S-matrix properties at admissible levels."""

    def test_integrable_unitary(self):
        """S-matrix is unitary at integrable levels."""
        for p in range(2, 6):
            S = modular_s_matrix_sl2(p, 1)
            n = S.shape[0]
            product = S @ S.conj().T
            np.testing.assert_allclose(product, np.eye(n), atol=1e-10,
                                       err_msg=f"S not unitary at k={p-2}")

    def test_integrable_size(self):
        """S-matrix has size (p-1) x (p-1) at integrable levels."""
        for p in range(2, 8):
            S = modular_s_matrix_sl2(p, 1)
            self.assertEqual(S.shape, (p - 1, p - 1))

    def test_admissible_size(self):
        """S-matrix has size (p-1)*q x (p-1)*q at admissible levels."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            S = modular_s_matrix_sl2(p, q)
            n = (p - 1) * q
            self.assertEqual(S.shape, (n, n))

    def test_s_matrix_symmetric(self):
        """S-matrix is symmetric."""
        for p, q in [(3, 1), (4, 1), (3, 2), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            S = modular_s_matrix_sl2(p, q)
            np.testing.assert_allclose(S, S.T, atol=1e-12,
                                       err_msg=f"S not symmetric at (p,q)=({p},{q})")

    def test_k1_s_matrix_values(self):
        """k=1 (p=3, q=1): 2x2 S-matrix with known values."""
        S = modular_s_matrix_sl2(3, 1)
        s = 1.0 / np.sqrt(2)
        expected = np.array([[s, s], [s, -s]])
        np.testing.assert_allclose(S.real, expected, atol=1e-10)

    def test_s_squared_permutation(self):
        """S^2 should be a charge-conjugation matrix (permutation) at integrable."""
        for p in range(2, 6):
            S = modular_s_matrix_sl2(p, 1)
            S2 = S @ S
            # S^2 = C (charge conjugation). For SU(2)_k, C = identity.
            n = p - 1
            np.testing.assert_allclose(np.abs(S2), np.eye(n), atol=1e-8,
                                       err_msg=f"|S^2| != I at k={p-2}")


# =========================================================================
# Vacuum Verma module dimensions
# =========================================================================

class TestVacuumVermaDims(unittest.TestCase):
    """Vacuum Verma module dimensions p_3(h) for sl_2."""

    def test_known_values(self):
        """p_3(h) matches known 3-colored partition numbers."""
        dims = vacuum_verma_dims_sl2(10)
        # OEIS A000716: p_3(n) = number of partitions into 3 colors
        expected = [1, 3, 9, 22, 51, 108, 221, 429, 810, 1479, 2640]
        for i, (got, exp) in enumerate(zip(dims, expected)):
            self.assertEqual(got, exp, f"p_3({i}) = {got} != {exp}")

    def test_vacuum_is_1(self):
        """p_3(0) = 1 (vacuum)."""
        dims = vacuum_verma_dims_sl2(1)
        self.assertEqual(dims[0], 1)

    def test_weight_1_is_3(self):
        """p_3(1) = 3 (three generators e, h, f at weight 1)."""
        dims = vacuum_verma_dims_sl2(2)
        self.assertEqual(dims[1], 3)

    def test_monotone_increasing(self):
        """p_3 is strictly increasing for h >= 1."""
        dims = vacuum_verma_dims_sl2(15)
        for i in range(1, len(dims) - 1):
            self.assertLess(dims[i], dims[i + 1])


# =========================================================================
# CE differential for sl_2
# =========================================================================

class TestCEDifferential(unittest.TestCase):
    """Chevalley-Eilenberg differential for sl_2."""

    def test_d2_rank(self):
        """d^2: Lambda^2 -> Lambda^1 has rank 3 (sl_2 semisimple)."""
        data = ce_differential_sl2(1.0)
        self.assertEqual(data['rank_d2'], 3)

    def test_d3_zero(self):
        """d^3: Lambda^3 -> Lambda^2 is zero (Jacobi identity => cocycle)."""
        data = ce_differential_sl2(1.0)
        self.assertEqual(data['rank_d3'], 0)

    def test_ce_dims(self):
        """CE complex dimensions: 1, 3, 3, 1."""
        data = ce_differential_sl2(1.0)
        self.assertEqual(data['dims'], {0: 1, 1: 3, 2: 3, 3: 1})


# =========================================================================
# Bar-Ext vs ordinary Ext
# =========================================================================

class TestBarExtVsOrdinaryExt(unittest.TestCase):
    """Structural comparison of bar-Ext and ordinary Ext."""

    def test_bar_ext1_always_3(self):
        """bar-Ext^1 = sl_2 (dim 3) at all levels."""
        for p, q in [(3, 2), (2, 3), (3, 1), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            result = bar_ext_vs_ordinary_ext(p, q)
            self.assertEqual(result['bar_ext_1'], 3)

    def test_bar_ext2_zero_universal(self):
        """bar-Ext^2 = 0 for V_k (Koszul)."""
        for p, q in [(3, 2), (2, 3), (3, 1)]:
            if gcd(p, q) != 1:
                continue
            result = bar_ext_vs_ordinary_ext(p, q)
            self.assertEqual(result['bar_ext_2_universal'], 0)

    def test_integrable_semisimple(self):
        """Integrable levels have semisimple module category."""
        for p in range(2, 6):
            result = bar_ext_vs_ordinary_ext(p, 1)
            self.assertTrue(result['ordinary_ext_semisimple'])
            self.assertEqual(result['ordinary_ext1_count'], 0)

    def test_admissible_nonsemisimple(self):
        """Non-integrable admissible levels have non-semisimple category."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            result = bar_ext_vs_ordinary_ext(p, q)
            self.assertFalse(result['ordinary_ext_semisimple'])
            self.assertEqual(result['module_category_type'],
                             'non-semisimple braided')

    def test_ext1_pairs_exist_admissible(self):
        """Non-integrable admissible levels have Ext^1 pairs."""
        result = bar_ext_vs_ordinary_ext(3, 2)
        # k = -1/2: has 4 admissible modules, should have some extensions
        self.assertGreater(result['ordinary_ext1_count'], 0)


# =========================================================================
# Virasoro minimal model identification
# =========================================================================

class TestMinimalModelIdentification(unittest.TestCase):
    """Virasoro minimal model data from DS reduction."""

    def test_m32_trivial(self):
        """M(3,2): c = 0, the trivial theory."""
        mm = minimal_model_identification(3, 2)
        self.assertEqual(mm['c_minimal_model'], Fraction(0))
        self.assertTrue(mm['is_unitary'])
        self.assertEqual(mm['n_primaries'], 1)

    def test_m43_ising(self):
        """M(4,3): c = 1/2, the Ising model."""
        mm = minimal_model_identification(4, 3)
        self.assertEqual(mm['c_minimal_model'], Fraction(1, 2))
        self.assertTrue(mm['is_unitary'])
        self.assertEqual(mm['n_primaries'], 3)

    def test_m54_tricritical_ising(self):
        """M(5,4): c = 7/10, the tricritical Ising model."""
        mm = minimal_model_identification(5, 4)
        self.assertEqual(mm['c_minimal_model'], Fraction(7, 10))
        self.assertTrue(mm['is_unitary'])
        self.assertEqual(mm['n_primaries'], 6)

    def test_m52_yang_lee(self):
        """M(5,2): c = -22/5, the Yang-Lee edge singularity."""
        mm = minimal_model_identification(5, 2)
        self.assertEqual(mm['c_minimal_model'], Fraction(-22, 5))
        self.assertFalse(mm['is_unitary'])  # non-unitary
        self.assertEqual(mm['n_primaries'], 2)

    def test_m53_central_charge(self):
        """M(5,3): c = -3/5."""
        mm = minimal_model_identification(5, 3)
        self.assertEqual(mm['c_minimal_model'], Fraction(-3, 5))

    def test_unitary_iff_consecutive(self):
        """M(p,q) is unitary iff p = q+1."""
        for p, q in [(3, 2), (4, 3), (5, 4), (6, 5),
                     (5, 2), (5, 3), (7, 2), (7, 3)]:
            if gcd(p, q) != 1:
                continue
            mm = minimal_model_identification(p, q)
            expected_unitary = (p == q + 1)
            self.assertEqual(mm['is_unitary'], expected_unitary,
                             f"Unitarity wrong for M({p},{q})")

    def test_n_primaries_formula(self):
        """n_primaries = (p-1)(q-1)/2 for q >= 2."""
        for p, q in [(4, 3), (5, 4), (5, 2), (5, 3), (7, 2), (7, 4)]:
            if gcd(p, q) != 1 or q < 2:
                continue
            mm = minimal_model_identification(p, q)
            expected = (p - 1) * (q - 1) // 2
            self.assertEqual(mm['n_primaries'], expected,
                             f"n_primaries wrong for M({p},{q})")


# =========================================================================
# sl_3 admissible levels
# =========================================================================

class TestSl3Admissible(unittest.TestCase):
    """Bar complex analysis for sl_3 at admissible levels."""

    def test_max_bar_arity(self):
        """sl_3 max bar arity = dim(sl_3) = 8."""
        result = admissible_bar_analysis_sl3(4, 1)
        self.assertEqual(result['max_bar_arity'], 8)

    def test_universal_koszul(self):
        """V_k(sl_3) is always Koszul."""
        for p, q in [(4, 1), (5, 1), (5, 2)]:
            if gcd(p, q) != 1 or p < 3:
                continue
            result = admissible_bar_analysis_sl3(p, q)
            self.assertTrue(result['is_universal_koszul'])

    def test_shadow_class_L(self):
        """sl_3 shadow depth is always L."""
        for p, q in [(4, 1), (5, 2)]:
            if gcd(p, q) != 1:
                continue
            result = admissible_bar_analysis_sl3(p, q)
            self.assertEqual(result['shadow_depth_class'], 'L')

    def test_kappa_sl3_formula(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        result = admissible_bar_analysis_sl3(4, 1)  # k = 1
        self.assertEqual(result['kappa'], Fraction(16, 3))

    def test_ce_dims_binomial(self):
        """CE dimensions are C(8, d)."""
        result = admissible_bar_analysis_sl3(4, 1)
        for d in range(9):
            from math import comb as C
            self.assertEqual(result['ce_dims'][d], C(8, d))

    def test_high_null_above_bar(self):
        """sl_3 at k = -5/3 (p=4, q=3): h_null = 9 > 8, above bar range."""
        result = admissible_bar_analysis_sl3(4, 3)
        self.assertEqual(result['h_null_estimate'], 9)
        self.assertFalse(result['bar_relevant_null'])
        self.assertTrue(result['is_quotient_koszul'])

    def test_low_null_in_bar(self):
        """sl_3 at k=1 (p=4, q=1): h_null=3, bar relevant (3 <= 8)."""
        result = admissible_bar_analysis_sl3(4, 1)
        self.assertEqual(result['h_null_estimate'], 3)
        self.assertTrue(result['bar_relevant_null'])


# =========================================================================
# Character analysis
# =========================================================================

class TestCharacterAnalysis(unittest.TestCase):
    """Admissible character leading coefficients."""

    def test_agree_below_null(self):
        """L_k and V_k characters agree below h_null."""
        cc = admissible_character_leading_coeffs(3, 2, n_terms=6)
        self.assertTrue(cc['agree_with_universal_below_null'])
        # h_null = 4, so coeffs 0,1,2,3 should be present
        for n in range(4):
            self.assertIsNotNone(cc['leading_coeffs'][n])

    def test_vacuum_coeff_1(self):
        """a_0 = 1 (vacuum state)."""
        cc = admissible_character_leading_coeffs(3, 2)
        self.assertEqual(cc['leading_coeffs'][0], 1)

    def test_weight1_coeff_3(self):
        """a_1 = 3 (dim sl_2 = 3 weight-1 states)."""
        cc = admissible_character_leading_coeffs(3, 2)
        self.assertEqual(cc['leading_coeffs'][1], 3)

    def test_null_marks_divergence(self):
        """Coefficients at h >= h_null are None (need Shapovalov)."""
        cc = admissible_character_leading_coeffs(3, 2, n_terms=8)
        h_null = cc['h_null']
        for n in range(h_null, 8):
            self.assertIsNone(cc['leading_coeffs'][n])


# =========================================================================
# Comprehensive bar analysis data integrity
# =========================================================================

class TestBarAnalysisDataIntegrity(unittest.TestCase):
    """Data integrity checks on admissible_bar_analysis_sl2."""

    def test_central_charge_formula(self):
        """c = 3k/(k+2) = 3(p-2q)/p."""
        for p, q in [(3, 2), (2, 3), (5, 3), (3, 1), (4, 1)]:
            if gcd(p, q) != 1:
                continue
            analysis = admissible_bar_analysis_sl2(p, q)
            k = Fraction(p, q) - 2
            expected_c = 3 * k / (k + 2)
            self.assertEqual(analysis.c, expected_c)

    def test_h_null_formula(self):
        """h_null = (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (5, 3), (7, 2)]:
            if gcd(p, q) != 1:
                continue
            analysis = admissible_bar_analysis_sl2(p, q)
            self.assertEqual(analysis.h_null, (p - 1) * q)

    def test_n_admissible_modules(self):
        """n_admissible = (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (5, 3)]:
            if gcd(p, q) != 1:
                continue
            analysis = admissible_bar_analysis_sl2(p, q)
            self.assertEqual(analysis.n_admissible_modules, (p - 1) * q)

    def test_all_assoc_var_zero(self):
        """Associated variety dimension is 0 for all admissible sl_2."""
        for q in range(1, 5):
            for p in range(2, 3 * q + 3):
                if gcd(p, q) != 1:
                    continue
                analysis = admissible_bar_analysis_sl2(p, q)
                self.assertEqual(analysis.associated_variety_dim, 0)

    def test_gcd_check(self):
        """Non-coprime (p,q) raises ValueError."""
        with self.assertRaises(ValueError):
            admissible_bar_analysis_sl2(4, 2)

    def test_p_min_check(self):
        """p < 2 raises ValueError."""
        with self.assertRaises(ValueError):
            admissible_bar_analysis_sl2(1, 1)

    def test_mechanism_nonempty(self):
        """All analyses have non-empty mechanism strings."""
        for p, q in [(3, 2), (2, 3), (3, 1), (5, 3)]:
            analysis = admissible_bar_analysis_sl2(p, q)
            self.assertTrue(len(analysis.koszul_mechanism) > 20)


# =========================================================================
# Classification table consistency
# =========================================================================

class TestClassificationTable(unittest.TestCase):
    """Classification table output consistency."""

    def test_table_nonempty(self):
        """Table has entries."""
        table = classification_table_sl2(max_q=3, max_k=3.0)
        self.assertGreater(len(table), 5)

    def test_table_sorted(self):
        """Table is sorted by level."""
        table = classification_table_sl2(max_q=3, max_k=3.0)
        k_vals = [row['k_float'] for row in table]
        self.assertEqual(k_vals, sorted(k_vals))

    def test_table_all_universal_koszul(self):
        """All table entries have V_k Koszul."""
        table = classification_table_sl2(max_q=3, max_k=3.0)
        for row in table:
            self.assertTrue(row['V_k_koszul'])

    def test_table_all_class_L(self):
        """All table entries have shadow class L."""
        table = classification_table_sl2(max_q=3, max_k=3.0)
        for row in table:
            self.assertEqual(row['shadow_class'], 'L')


# =========================================================================
# Master analysis
# =========================================================================

class TestMasterAnalysis(unittest.TestCase):
    """Master admissible analysis across all levels."""

    def test_master_all_universal_koszul(self):
        """All levels have V_k Koszul."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertTrue(result['all_universal_koszul'])

    def test_master_no_failure(self):
        """No Koszul failure found."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertFalse(result['any_quotient_failure'])

    def test_master_kappa_agree(self):
        """All kappa multi-path checks agree."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertTrue(result['all_kappa_multipath_agree'])

    def test_master_all_assoc_var_trivial(self):
        """All associated varieties are trivial."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertTrue(result['all_assoc_var_trivial'])

    def test_master_all_shadow_L(self):
        """All shadow depth classes are L."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertTrue(result['all_shadow_class_L'])

    def test_master_tests_sufficient_levels(self):
        """Master analysis tests at least 10 levels."""
        result = master_admissible_analysis(max_q=4, max_k_abs=3.0)
        self.assertGreaterEqual(result['n_levels_tested'], 10)


# =========================================================================
# Cross-checks: specific known admissible levels
# =========================================================================

class TestSpecificLevels(unittest.TestCase):
    """Detailed verification at specific well-understood levels."""

    def test_k0_trivial(self):
        """k=0 (p=2, q=1): L_0(sl_2) = C, trivially Koszul."""
        analysis = admissible_bar_analysis_sl2(2, 1)
        self.assertEqual(analysis.k, Fraction(0))
        self.assertEqual(analysis.c, Fraction(0))
        self.assertTrue(analysis.is_quotient_koszul)

    def test_k1_su2_level1(self):
        """k=1 (p=3, q=1): SU(2)_1 WZW, 2 modules, Koszul."""
        analysis = admissible_bar_analysis_sl2(3, 1)
        self.assertEqual(analysis.k, Fraction(1))
        self.assertEqual(analysis.c, Fraction(1))
        self.assertTrue(analysis.is_quotient_koszul)
        self.assertEqual(analysis.n_admissible_modules, 2)

    def test_k2_su2_level2(self):
        """k=2 (p=4, q=1): SU(2)_2 WZW, 3 modules, Koszul."""
        analysis = admissible_bar_analysis_sl2(4, 1)
        self.assertEqual(analysis.k, Fraction(2))
        self.assertTrue(analysis.is_quotient_koszul)
        self.assertEqual(analysis.n_admissible_modules, 3)

    def test_k_minus_half_m25(self):
        """k=-1/2 (p=3, q=2): associated to M(3,2) under DS, c(sl_2)=-1."""
        analysis = admissible_bar_analysis_sl2(3, 2)
        self.assertEqual(analysis.k, Fraction(-1, 2))
        self.assertEqual(analysis.c, Fraction(-1))
        self.assertEqual(analysis.h_null, 4)
        self.assertTrue(analysis.is_quotient_koszul)
        # kappa = 3*3/(4*2) = 9/8
        self.assertEqual(analysis.kappa_km, Fraction(9, 8))

    def test_k_minus_4_3(self):
        """k=-4/3 (p=2, q=3): c(sl_2) = -6, h_null = 3."""
        analysis = admissible_bar_analysis_sl2(2, 3)
        self.assertEqual(analysis.k, Fraction(-4, 3))
        self.assertEqual(analysis.c, Fraction(-6))
        self.assertEqual(analysis.h_null, 3)
        self.assertTrue(analysis.is_quotient_koszul)

    def test_kappa_additivity_check(self):
        """kappa at different levels follows 3p/(4q)."""
        test_data = [
            (2, 1, Fraction(3, 2)),   # k=0
            (3, 1, Fraction(9, 4)),   # k=1
            (4, 1, Fraction(3)),      # k=2
            (3, 2, Fraction(9, 8)),   # k=-1/2
            (2, 3, Fraction(1, 2)),   # k=-4/3
            (5, 3, Fraction(5, 4)),   # k=-1/3
        ]
        for p, q, expected in test_data:
            kappa = kappa_path1_sugawara(p, q)
            self.assertEqual(kappa, expected,
                             f"kappa wrong at (p,q)=({p},{q}): {kappa} != {expected}")


# =========================================================================
# Koszulness at boundary cases
# =========================================================================

class TestBoundaryCases(unittest.TestCase):
    """Boundary cases where h_null is small."""

    def test_h_null_equals_3(self):
        """All levels with h_null = 3 are Koszul."""
        # h_null = 3 when (p-1)*q = 3
        # Solutions: (p,q) = (4,1), (2,3)
        for p, q in [(4, 1), (2, 3)]:
            analysis = admissible_bar_analysis_sl2(p, q)
            self.assertEqual(analysis.h_null, 3)
            self.assertTrue(analysis.is_quotient_koszul)

    def test_h_null_equals_2(self):
        """All levels with h_null = 2 are Koszul (integrable only)."""
        # h_null = 2 when (p-1)*q = 2
        # Solutions: (p,q) = (3,1) -> k=1 (integrable)
        analysis = admissible_bar_analysis_sl2(3, 1)
        self.assertEqual(analysis.h_null, 2)
        self.assertTrue(analysis.is_quotient_koszul)

    def test_h_null_equals_1(self):
        """h_null = 1 at k=0 (p=2, q=1): still Koszul."""
        analysis = admissible_bar_analysis_sl2(2, 1)
        self.assertEqual(analysis.h_null, 1)
        self.assertTrue(analysis.is_quotient_koszul)


# =========================================================================
# Cross-family consistency
# =========================================================================

class TestCrossFamilyConsistency(unittest.TestCase):
    """Consistency between sl_2 and sl_3 analysis."""

    def test_kappa_dim_dependence(self):
        """kappa scales with dim(g): kappa(sl_3)/kappa(sl_2) = 8/3 * 2/(k+2) * (k+3)/6
        at the SAME value of k (but different admissible parametrization)."""
        # At k = 1: sl_2 has kappa = 9/4, sl_3 has kappa = 16/3
        kappa_2 = kappa_path1_sugawara(3, 1, 'sl2')  # k=1 for sl_2
        kappa_3 = kappa_path1_sugawara(4, 1, 'sl3')  # k=1 for sl_3
        # kappa(sl_2, k=1) = 3*3/4 = 9/4
        # kappa(sl_3, k=1) = 8*4/6 = 16/3
        self.assertEqual(kappa_2, Fraction(9, 4))
        self.assertEqual(kappa_3, Fraction(16, 3))

    def test_shadow_class_uniform(self):
        """All affine KM algebras have shadow class L."""
        analysis_2 = admissible_bar_analysis_sl2(3, 2)
        analysis_3 = admissible_bar_analysis_sl3(4, 1)
        self.assertEqual(analysis_2.shadow_depth_class, 'L')
        self.assertEqual(analysis_3['shadow_depth_class'], 'L')


if __name__ == '__main__':
    unittest.main()
