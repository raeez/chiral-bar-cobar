"""Tests for non-scalar saturation Candidate 3: Admissible levels.

Verifies:
    - Admissible level classification for sl_2
    - Sugawara central charges at admissible levels
    - Admissible weight module structure
    - Zhu algebra computation and (non-)semisimplicity
    - Fusion rules via Verlinde formula
    - Module category non-semisimplicity
    - H^2_cyc,prim analysis: KM, W-algebra, extension cases
    - Comprehensive frontier analysis for conj:scalar-saturation-universality
"""

import pytest
import unittest
from fractions import Fraction
from math import gcd

from compute.lib.nonscalar_admissible_level import (
    # Classification
    AdmissibleLevel,
    admissible_level_sl2,
    list_admissible_levels_sl2,
    # Modules
    AdmissibleWeight,
    admissible_weights_sl2,
    # Zhu algebra
    ZhuAlgebraData,
    zhu_algebra_sl2,
    # Fusion
    admissible_modular_s_matrix_sl2,
    fusion_rules_sl2,
    verify_fusion_integrality,
    # Module category
    module_category_sl2_admissible,
    # H^2_cyc analysis
    h2_cyc_analysis_sl2,
    h2_cyc_analysis_w_algebra_admissible,
    h2_cyc_analysis_extension_voa,
    # Frontier
    frontier_analysis_sl2,
    frontier_analysis_w_algebras,
    frontier_analysis_extensions,
    comprehensive_saturation_analysis,
    # Ext bounds
    ext_bound_from_fusion,
)


class TestAdmissibleLevelClassification(unittest.TestCase):
    """Verify admissible level data for sl_2."""

    def test_level_minus_half(self):
        """k = -1/2: (p,q) = (3,2)."""
        level = admissible_level_sl2(3, 2)
        self.assertEqual(level.k, Fraction(-1, 2))
        self.assertFalse(level.is_integrable)

    def test_level_minus_four_thirds(self):
        """k = -4/3: (p,q) = (2,3)."""
        level = admissible_level_sl2(2, 3)
        self.assertEqual(level.k, Fraction(-4, 3))
        self.assertFalse(level.is_integrable)

    def test_integrable_level_0(self):
        """k = 0: (p,q) = (2,1)."""
        level = admissible_level_sl2(2, 1)
        self.assertEqual(level.k, Fraction(0))
        self.assertTrue(level.is_integrable)

    def test_integrable_level_1(self):
        """k = 1: (p,q) = (3,1)."""
        level = admissible_level_sl2(3, 1)
        self.assertEqual(level.k, Fraction(1))
        self.assertTrue(level.is_integrable)

    def test_integrable_level_2(self):
        """k = 2: (p,q) = (4,1)."""
        level = admissible_level_sl2(4, 1)
        self.assertEqual(level.k, Fraction(2))
        self.assertTrue(level.is_integrable)

    def test_central_charge_at_minus_half(self):
        """c(sl_2, -1/2) = 3*(-1/2)/(-1/2+2) = -1."""
        level = admissible_level_sl2(3, 2)
        self.assertEqual(level.c, Fraction(-1))

    def test_central_charge_at_level_1(self):
        """c(sl_2, 1) = 3*1/3 = 1."""
        level = admissible_level_sl2(3, 1)
        self.assertEqual(level.c, Fraction(1))

    def test_central_charge_formula(self):
        """c = 3(p-2q)/p for k = p/q - 2."""
        for p, q in [(3, 2), (2, 3), (5, 2), (5, 3), (7, 4)]:
            if gcd(p, q) == 1 and p >= 2:
                level = admissible_level_sl2(p, q)
                expected = Fraction(3 * (p - 2 * q), p)
                self.assertEqual(level.c, expected,
                                 f"Failed for (p,q)=({p},{q})")

    def test_n_simples_formula(self):
        """Number of simples = (p-1)*q."""
        for p, q in [(3, 2), (2, 3), (5, 2), (4, 3)]:
            if gcd(p, q) == 1 and p >= 2:
                level = admissible_level_sl2(p, q)
                self.assertEqual(level.n_simples, (p - 1) * q)

    def test_coprimality_check(self):
        """Non-coprime (p,q) should raise."""
        with self.assertRaises(ValueError):
            admissible_level_sl2(4, 2)

    def test_p_too_small(self):
        """p < 2 should raise."""
        with self.assertRaises(ValueError):
            admissible_level_sl2(1, 1)

    def test_list_admissible_sorted(self):
        """Listed levels are sorted by k value."""
        levels = list_admissible_levels_sl2(max_denom=3)
        k_values = [float(a.k) for a in levels]
        self.assertEqual(k_values, sorted(k_values))


class TestAdmissibleWeights(unittest.TestCase):
    """Verify admissible weight module data."""

    def test_integrable_k1_weights(self):
        """At k=1 (p=3,q=1): 2 modules with j = 0, 1/2."""
        level = admissible_level_sl2(3, 1)
        weights = admissible_weights_sl2(level)
        self.assertEqual(len(weights), 2)
        j_values = sorted([w.j for w in weights])
        self.assertEqual(j_values, [Fraction(0), Fraction(1, 2)])

    def test_integrable_k2_weights(self):
        """At k=2 (p=4,q=1): 3 modules with j = 0, 1/2, 1."""
        level = admissible_level_sl2(4, 1)
        weights = admissible_weights_sl2(level)
        self.assertEqual(len(weights), 3)
        j_values = sorted([w.j for w in weights])
        self.assertEqual(j_values, [Fraction(0), Fraction(1, 2), Fraction(1)])

    def test_vacuum_module_present(self):
        """Every admissible level has a vacuum module with j=0, h=0."""
        for p, q in [(3, 1), (4, 1), (3, 2), (5, 2)]:
            if gcd(p, q) == 1 and p >= 2:
                level = admissible_level_sl2(p, q)
                weights = admissible_weights_sl2(level)
                vacuum = [w for w in weights if w.r == 1 and w.s == 1]
                self.assertEqual(len(vacuum), 1)
                self.assertEqual(vacuum[0].j, Fraction(0))
                self.assertEqual(vacuum[0].h, Fraction(0))

    def test_count_at_minus_half(self):
        """At k=-1/2 (p=3,q=2): (3-1)*2 = 4 modules."""
        level = admissible_level_sl2(3, 2)
        weights = admissible_weights_sl2(level)
        self.assertEqual(len(weights), 4)


class TestZhuAlgebra(unittest.TestCase):
    """Verify Zhu algebra computation."""

    def test_integrable_semisimple(self):
        """At integrable levels, Zhu algebra should be semisimple."""
        for p in range(2, 6):
            level = admissible_level_sl2(p, 1)
            zhu = zhu_algebra_sl2(level)
            # At integrable level: distinct Casimir eigenvalues => semisimple
            self.assertTrue(zhu.is_semisimple,
                            f"Level k={level.k} should be semisimple")

    def test_integrable_n_simples(self):
        """At k = p-2 (integrable): p-1 simple modules."""
        for p in range(2, 6):
            level = admissible_level_sl2(p, 1)
            zhu = zhu_algebra_sl2(level)
            self.assertEqual(zhu.n_simples, p - 1)

    def test_zhu_dimension(self):
        """Zhu algebra dimension = number of admissible weights."""
        for p, q in [(3, 2), (5, 2), (4, 3)]:
            if gcd(p, q) == 1:
                level = admissible_level_sl2(p, q)
                zhu = zhu_algebra_sl2(level)
                self.assertEqual(zhu.dimension, (p - 1) * q)

    def test_casimir_eigenvalue_zero(self):
        """Vacuum module always has Casimir eigenvalue 0."""
        for p, q in [(3, 1), (3, 2), (5, 2)]:
            if gcd(p, q) == 1:
                level = admissible_level_sl2(p, q)
                zhu = zhu_algebra_sl2(level)
                self.assertIn(Fraction(0), zhu.polynomial_roots)


class TestFusionRules(unittest.TestCase):
    """Verify fusion rules at admissible levels."""

    def test_integrable_k1_fusion(self):
        """At k=1: fusion rules for SU(2)_1 WZW model.

        2 modules: L_0, L_{1/2}.
        Fusion: L_{1/2} x L_{1/2} = L_0 (truncated tensor product).
        """
        level = admissible_level_sl2(3, 1)
        result = verify_fusion_integrality(level)
        # Should be approximately integral
        self.assertLess(result["max_fractional_part"], 0.2)

    def test_integrable_k2_fusion(self):
        """At k=2: fusion rules for SU(2)_2 WZW model."""
        level = admissible_level_sl2(4, 1)
        result = verify_fusion_integrality(level)
        self.assertLess(result["max_fractional_part"], 0.2)

    def test_s_matrix_shape(self):
        """S-matrix has correct shape."""
        level = admissible_level_sl2(3, 2)
        S = admissible_modular_s_matrix_sl2(level)
        n = level.n_simples
        self.assertEqual(S.shape, (n, n))

    def test_s_matrix_unitarity_integrable(self):
        """At integrable levels, S S^dagger = I (unitarity)."""
        import numpy as np
        for p in range(3, 7):
            level = admissible_level_sl2(p, 1)
            S = admissible_modular_s_matrix_sl2(level)
            prod = S @ S.conj().T
            n = S.shape[0]
            np.testing.assert_allclose(
                prod, np.eye(n), atol=1e-10,
                err_msg=f"S-matrix not unitary at k={level.k}")

    def test_integrable_fusion_tight_integrality(self):
        """At integrable levels, Verlinde coefficients are exactly integral."""
        for p in range(3, 7):
            level = admissible_level_sl2(p, 1)
            result = verify_fusion_integrality(level)
            self.assertLess(result["max_fractional_part"], 1e-10,
                            f"Fusion not integral at k={level.k}")
            self.assertEqual(result["negative_coefficients"], 0)

    def test_integrable_vacuum_fusion_identity(self):
        """Fusion with vacuum is identity: N_{0,j}^k = delta_{jk}."""
        import numpy as np
        level = admissible_level_sl2(4, 1)  # k=2, 3 modules
        N_tensor = fusion_rules_sl2(level)
        n = N_tensor.shape[0]
        for j in range(n):
            for k in range(n):
                expected = 1.0 if j == k else 0.0
                np.testing.assert_allclose(
                    N_tensor[0, j, k].real, expected, atol=1e-10,
                    err_msg=f"Vacuum fusion N_{{0,{j}}}^{k}")


class TestModuleCategory(unittest.TestCase):
    """Verify module category structure at admissible levels."""

    def test_integrable_semisimple(self):
        """Integrable levels have semisimple module categories."""
        for p in range(2, 6):
            level = admissible_level_sl2(p, 1)
            cat = module_category_sl2_admissible(level)
            self.assertTrue(cat.is_semisimple)
            self.assertEqual(len(cat.non_split_extensions), 0)

    def test_admissible_non_semisimple(self):
        """Non-integrable admissible levels have non-semisimple categories."""
        level = admissible_level_sl2(3, 2)  # k = -1/2
        cat = module_category_sl2_admissible(level)
        self.assertFalse(cat.is_semisimple)
        self.assertGreater(len(cat.non_split_extensions), 0)

    def test_extensions_exist_at_minus_half(self):
        """At k=-1/2: non-trivial extensions between modules."""
        level = admissible_level_sl2(3, 2)
        cat = module_category_sl2_admissible(level)
        self.assertGreater(len(cat.non_split_extensions), 0)

    def test_n_simples_matches(self):
        """Module category simple count matches admissible level data."""
        for p, q in [(3, 2), (5, 2), (4, 3)]:
            if gcd(p, q) == 1:
                level = admissible_level_sl2(p, q)
                cat = module_category_sl2_admissible(level)
                self.assertEqual(cat.n_simples, level.n_simples)


class TestH2CycAnalysis(unittest.TestCase):
    """Verify H^2_cyc analysis at admissible levels."""

    def test_km_always_saturated(self):
        """Pure Kac-Moody sl_2 is scalar-saturated at ALL admissible levels."""
        for level in list_admissible_levels_sl2(max_denom=4):
            result = h2_cyc_analysis_sl2(level)
            self.assertTrue(result.scalar_saturated,
                            f"sl_2 at k={level.k} should be saturated")
            self.assertEqual(result.h2_cyc_level_component, 1)
            self.assertEqual(result.h2_cyc_prim_upper_bound, 0)

    def test_km_whitehead_always_applies(self):
        """Whitehead decomposition (Stage 1) applies at all non-critical levels."""
        for level in list_admissible_levels_sl2(max_denom=3):
            result = h2_cyc_analysis_sl2(level)
            self.assertTrue(result.whitehead_applies)

    def test_km_no_primary_generators(self):
        """The mechanism for KM: no primary generators."""
        level = admissible_level_sl2(3, 2)  # k = -1/2
        result = h2_cyc_analysis_sl2(level)
        self.assertIn("primary", result.mechanism.lower())

    def test_w_algebra_brst_saturated(self):
        """W-algebras are saturated via BRST rigidity, even at admissible levels."""
        for N in [2, 3, 4]:
            level = admissible_level_sl2(3, 2)  # prototype level
            result = h2_cyc_analysis_w_algebra_admissible(N, level)
            self.assertTrue(result.scalar_saturated)
            self.assertTrue(result.brst_rigidity)
            self.assertEqual(result.h2_cyc_prim_upper_bound, 0)

    def test_extension_voa_open(self):
        """Simple current extensions at admissible levels: status OPEN."""
        level = admissible_level_sl2(3, 2)
        result = h2_cyc_analysis_extension_voa("test", level, 2)
        # scalar_saturated is None (unknown)
        self.assertIsNone(result.scalar_saturated)
        self.assertFalse(result.kl_semisimplicity)
        self.assertFalse(result.brst_rigidity)

    def test_extension_voa_integrable_ok(self):
        """Extensions at integrable levels: saturated by KL."""
        level = admissible_level_sl2(3, 1)  # k = 1, integrable
        result = h2_cyc_analysis_extension_voa("test", level, 2)
        self.assertTrue(result.scalar_saturated)
        self.assertTrue(result.kl_semisimplicity)


class TestFrontierAnalysis(unittest.TestCase):
    """Verify comprehensive frontier analysis."""

    def test_sl2_frontier_all_saturated(self):
        """All admissible levels of sl_2 are scalar-saturated."""
        results = frontier_analysis_sl2()
        for r in results:
            self.assertTrue(r.scalar_saturated,
                            f"Failed at k={r.level.k}")

    def test_w_algebras_frontier_all_saturated(self):
        """All W-algebras at admissible levels are saturated."""
        results = frontier_analysis_w_algebras()
        for r in results:
            self.assertTrue(r.scalar_saturated)

    def test_extensions_have_open_cases(self):
        """Extension frontier has genuinely open cases."""
        results = frontier_analysis_extensions()
        open_cases = [r for r in results if r.scalar_saturated is None]
        self.assertGreater(len(open_cases), 0)


class TestComprehensiveAnalysis(unittest.TestCase):
    """Master test: comprehensive saturation analysis."""

    def test_km_proved(self):
        result = comprehensive_saturation_analysis()
        self.assertEqual(result["kac_moody"]["status"], "PROVED")
        self.assertTrue(result["kac_moody"]["all_saturated"])

    def test_w_algebras_proved_generic(self):
        result = comprehensive_saturation_analysis()
        self.assertEqual(result["w_algebras"]["status"], "PROVED_GENERIC")
        self.assertTrue(result["w_algebras"]["all_saturated"])

    def test_extensions_open(self):
        result = comprehensive_saturation_analysis()
        self.assertEqual(result["extensions"]["status"], "OPEN")
        self.assertGreater(result["extensions"]["open"], 0)

    def test_conjecture_identification(self):
        """The comprehensive analysis identifies the correct conjecture."""
        result = comprehensive_saturation_analysis()
        self.assertIn("scalar-saturation-universality",
                       result["overall"]["conjecture"])

    def test_proved_vs_open_classes(self):
        """Correctly separates proved classes from open frontier."""
        result = comprehensive_saturation_analysis()
        self.assertIn("Kac-Moody", result["overall"]["proved_classes"])
        self.assertIn("W-algebra", result["overall"]["proved_classes"])
        self.assertIn("non-ds", result["overall"]["open_class"].lower())


class TestExtBounds(unittest.TestCase):
    """Verify Ext group bounds from fusion rules."""

    def test_integrable_no_extensions(self):
        """At integrable levels: no non-split extensions."""
        level = admissible_level_sl2(3, 1)
        result = ext_bound_from_fusion(level)
        self.assertTrue(result["is_semisimple"])
        self.assertEqual(result["n_extensions"], 0)

    def test_admissible_has_extensions(self):
        """At admissible non-integrable levels: extensions exist."""
        level = admissible_level_sl2(3, 2)
        result = ext_bound_from_fusion(level)
        self.assertFalse(result["is_semisimple"])
        self.assertGreater(result["n_extensions"], 0)

    def test_ext2_bimod_vs_ext1_mod(self):
        """Ext^2_bimod and Ext^1_mod are different: documented in output."""
        level = admissible_level_sl2(3, 2)
        result = ext_bound_from_fusion(level)
        self.assertIn("bimod", result["ext2_bimod_status"])
