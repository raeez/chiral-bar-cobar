#!/usr/bin/env python3
r"""Tests for the CY exchange proof analysis engine.

Tests verify:
  1. The five obstructions (OB1-OB5) that prevent CY exchange from
     replacing Theorem A
  2. The four genuine values (VAL1-VAL4) of the CY perspective
  3. CY exchange consistency for all 17 standard families
  4. Kappa complementarity under CY exchange (AP24 cross-check)
  5. CY dimension consistency (always 1 for chiral algebras on curves)
  6. Shifted symplectic degree at each genus
  7. Lagrangian dimension verification
  8. Dependency DAG correctness
  9. The full analysis report

Ground truth sources:
  - bar_cobar_adjunction_curved.tex (Theorem A, thm:bar-cobar-adjunction)
  - higher_genus_complementarity.tex (Theorem C, thm:quantum-complementarity-main)
  - chiral_koszul_pairs.tex (K11, thm:koszul-equivalences-meta item (xi))
  - Holstein-Rivera, arXiv:2410.03604 (Theorems 1.1, 1.3)
  - Calaque-Safronov, arXiv:2407.08622

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct computation from definitions
  Path 2: Cross-family consistency (AP24, AP39)
  Path 3: Dependency DAG analysis
  Path 4: Numerical evaluation at specific parameter values
"""

import unittest
from fractions import Fraction

from compute.lib.theorem_cy_exchange_proof_engine import (
    DEPENDENCY_DAG,
    STANDARD_FAMILIES,
    OBSTRUCTION_REGISTER,
    VALUE_REGISTER,
    get_dependency_chain,
    verify_cy_cannot_bypass_thm_a,
    verify_categorical_level_mismatch,
    verify_perfectness_gap,
    verify_thm_c_not_special_case_of_thm_a,
    verify_k11_not_free,
    smooth_cy_data,
    proper_cy_data,
    koszul_dual_cy_data,
    kappa_value,
    verify_cy_exchange_all_families,
    shifted_symplectic_degree_genus,
    shifted_symplectic_degree_total,
    verify_lagrangian_dimension,
    verify_val1_fiber_perfectness,
    verify_val2_p3_redundancy,
    verify_val3_conceptual_framework,
    verify_val4_shadow_tower_from_aksz,
    full_cy_exchange_analysis,
    kappa_complementarity_under_cy,
    cy_dimension_consistency,
)


# ============================================================
# Test Group 1: Five obstructions (OB1-OB5)
# ============================================================

class TestOB1Circularity(unittest.TestCase):
    """OB1: CY exchange presupposes the bar construction."""

    def test_circularity_detected(self):
        result = verify_cy_cannot_bypass_thm_a()
        self.assertTrue(result['circular'])
        self.assertEqual(result['obstruction'], 'OB1')

    def test_hr24_requires_bar(self):
        result = verify_cy_cannot_bypass_thm_a()
        self.assertTrue(result['hr24_requires_bar'])

    def test_hr24_requires_d_squared_zero(self):
        result = verify_cy_cannot_bypass_thm_a()
        self.assertTrue(result['hr24_requires_d2'])

    def test_thm_a_provides_bar(self):
        result = verify_cy_cannot_bypass_thm_a()
        self.assertTrue(result['thm_a_provides_bar'])


class TestOB2CategoricalMismatch(unittest.TestCase):
    """OB2: Functor adjunction vs object-level CY property."""

    def test_mismatch_detected(self):
        result = verify_categorical_level_mismatch()
        self.assertTrue(result['mismatch'])
        self.assertEqual(result['obstruction'], 'OB2')

    def test_thm_a_is_functor_level(self):
        result = verify_categorical_level_mismatch()
        self.assertEqual(result['thm_a_level'], 'functor_adjunction')

    def test_hr24_is_object_level(self):
        result = verify_categorical_level_mismatch()
        self.assertEqual(result['hr24_level'], 'object_property')

    def test_gap_requires_model_structure(self):
        result = verify_categorical_level_mismatch()
        self.assertIn('model_structure', result['gap_requires'])


class TestOB3PerfectnessGap(unittest.TestCase):
    """OB3: Fiber-level vs family-level perfectness."""

    def test_gap_detected(self):
        result = verify_perfectness_gap()
        self.assertTrue(result['gap_exists'])
        self.assertEqual(result['obstruction'], 'OB3')

    def test_fiber_level_from_hr24(self):
        result = verify_perfectness_gap()
        self.assertTrue(result['fiber_level_from_hr24'])

    def test_family_level_requires_pbw(self):
        result = verify_perfectness_gap()
        self.assertIn('pbw_filterability', result['family_level_requires'])

    def test_family_level_requires_base_change(self):
        result = verify_perfectness_gap()
        self.assertIn('base_change', result['family_level_requires'])


class TestOB4DependencyReversal(unittest.TestCase):
    """OB4: Theorem C is downstream of Theorem A, not a special case."""

    def test_reversal_detected(self):
        result = verify_thm_c_not_special_case_of_thm_a()
        self.assertTrue(result['reversal'])
        self.assertEqual(result['obstruction'], 'OB4')

    def test_a_in_chain_of_c(self):
        result = verify_thm_c_not_special_case_of_thm_a()
        self.assertTrue(result['a_in_chain_of_c'])

    def test_c_not_in_chain_of_a(self):
        result = verify_thm_c_not_special_case_of_thm_a()
        self.assertFalse(result['c_in_chain_of_a'])

    def test_direction_a_implies_c(self):
        result = verify_thm_c_not_special_case_of_thm_a()
        self.assertEqual(result['dependency_direction'], 'A_implies_C')


class TestOB5K11NotFree(unittest.TestCase):
    """OB5: K11 does not come for free from CY exchange."""

    def test_k11_not_free(self):
        result = verify_k11_not_free()
        self.assertTrue(result['k11_not_free'])
        self.assertEqual(result['obstruction'], 'OB5')

    def test_cy_missing_family_perfectness(self):
        result = verify_k11_not_free()
        self.assertIn('family_level_perfectness', result['cy_missing'])

    def test_cy_provides_fiber_perfectness(self):
        result = verify_k11_not_free()
        self.assertIn('fiber_level_perfectness', result['cy_provides'])

    def test_cy_provides_p3_redundancy(self):
        result = verify_k11_not_free()
        self.assertIn('p3_redundancy', result['cy_provides'])


# ============================================================
# Test Group 2: Smooth CY data for standard families
# ============================================================

class TestSmoothCYHeisenberg(unittest.TestCase):
    """Smooth CY for Heisenberg: nondegenerate iff k != 0."""

    def test_positive_k(self):
        self.assertTrue(smooth_cy_data('heisenberg', {'k': 1})['has_smooth_cy'])

    def test_negative_k(self):
        self.assertTrue(smooth_cy_data('heisenberg', {'k': -3})['has_smooth_cy'])

    def test_fractional_k(self):
        self.assertTrue(smooth_cy_data('heisenberg', {'k': Fraction(1, 2)})['has_smooth_cy'])

    def test_zero_k_degenerates(self):
        self.assertFalse(smooth_cy_data('heisenberg', {'k': 0})['has_smooth_cy'])

    def test_cy_dim_is_1(self):
        self.assertEqual(smooth_cy_data('heisenberg', {'k': 1})['cy_dimension'], 1)


class TestSmoothCYAffineKM(unittest.TestCase):
    """Smooth CY for affine KM: nondegenerate iff k != 0."""

    def test_sl2_generic(self):
        self.assertTrue(
            smooth_cy_data('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})['has_smooth_cy'])

    def test_sl2_critical(self):
        # k = -h^v = -2: critical level, but form is still nondegenerate
        self.assertTrue(
            smooth_cy_data('affine_km', {'g_type': 'A', 'rank': 1, 'k': -2})['has_smooth_cy'])

    def test_sl2_zero_degenerates(self):
        self.assertFalse(
            smooth_cy_data('affine_km', {'g_type': 'A', 'rank': 1, 'k': 0})['has_smooth_cy'])

    def test_e8_generic(self):
        self.assertTrue(
            smooth_cy_data('affine_km', {'g_type': 'E', 'rank': 8, 'k': 1})['has_smooth_cy'])

    def test_g2_generic(self):
        self.assertTrue(
            smooth_cy_data('affine_km', {'g_type': 'G', 'rank': 2, 'k': 1})['has_smooth_cy'])


class TestSmoothCYVirasoro(unittest.TestCase):
    """Smooth CY for Virasoro: nondegenerate for non-minimal-model c."""

    def test_generic_c(self):
        self.assertTrue(smooth_cy_data('virasoro', {'c': 1})['has_smooth_cy'])

    def test_c_equals_13(self):
        self.assertTrue(smooth_cy_data('virasoro', {'c': 13})['has_smooth_cy'])

    def test_c_equals_26(self):
        self.assertTrue(smooth_cy_data('virasoro', {'c': 26})['has_smooth_cy'])

    def test_minimal_model_c_half(self):
        # c = 1/2 is the Ising model (p=4, q=3)
        self.assertFalse(smooth_cy_data('virasoro', {'c': Fraction(1, 2)})['has_smooth_cy'])

    def test_cy_dim_is_1(self):
        self.assertEqual(smooth_cy_data('virasoro', {'c': 1})['cy_dimension'], 1)


class TestSmoothCYFreeFields(unittest.TestCase):
    """Smooth CY for bc and betagamma: always nondegenerate."""

    def test_bc(self):
        self.assertTrue(smooth_cy_data('bc', {})['has_smooth_cy'])

    def test_betagamma(self):
        self.assertTrue(smooth_cy_data('betagamma', {})['has_smooth_cy'])


# ============================================================
# Test Group 3: Proper CY on bar (HR24 consequence)
# ============================================================

class TestProperCY(unittest.TestCase):
    """Proper CY on B(A) via Holstein-Rivera exchange."""

    def test_heisenberg_proper(self):
        self.assertTrue(proper_cy_data('heisenberg', {'k': 1})['has_proper_cy'])

    def test_heisenberg_zero_not_proper(self):
        self.assertFalse(proper_cy_data('heisenberg', {'k': 0})['has_proper_cy'])

    def test_affine_km_proper(self):
        self.assertTrue(
            proper_cy_data('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})['has_proper_cy'])

    def test_virasoro_proper(self):
        self.assertTrue(proper_cy_data('virasoro', {'c': 1})['has_proper_cy'])

    def test_bc_proper(self):
        self.assertTrue(proper_cy_data('bc', {})['has_proper_cy'])

    def test_betagamma_proper(self):
        self.assertTrue(proper_cy_data('betagamma', {})['has_proper_cy'])


# ============================================================
# Test Group 4: Koszul dual CY data
# ============================================================

class TestKoszulDualCY(unittest.TestCase):
    """CY data for Koszul duals, with AP24 kappa sum checks."""

    def test_heisenberg_dual_smooth(self):
        result = koszul_dual_cy_data('heisenberg', {'k': 1})
        self.assertTrue(result['dual_has_smooth_cy'])

    def test_heisenberg_kappa_sum_zero(self):
        """AP24: kappa(H_k) + kappa(H_k^!) = k + (-k) = 0."""
        result = koszul_dual_cy_data('heisenberg', {'k': 1})
        self.assertEqual(result['kappa_sum'], 0)

    def test_virasoro_dual_smooth(self):
        result = koszul_dual_cy_data('virasoro', {'c': 1})
        self.assertTrue(result['dual_has_smooth_cy'])

    def test_virasoro_kappa_sum_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        result = koszul_dual_cy_data('virasoro', {'c': 1})
        self.assertEqual(result['kappa_sum'], Fraction(13))

    def test_virasoro_c13_self_dual(self):
        """At c=13: Vir_c^! = Vir_{26-c} = Vir_13 (self-dual)."""
        result = koszul_dual_cy_data('virasoro', {'c': 13})
        self.assertEqual(result['kappa_A'], Fraction(13, 2))
        self.assertEqual(result['kappa_A_dual'], Fraction(13, 2))
        self.assertEqual(result['kappa_sum'], 13)

    def test_affine_kappa_sum_zero(self):
        """AP24: kappa(V_k(g)) + kappa(V_{-k-2h^v}(g)) = 0."""
        result = koszul_dual_cy_data('affine_km',
                                      {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertEqual(result['kappa_sum'], 0)

    def test_bc_betagamma_kappa_sum_zero(self):
        """AP24: kappa(bc) + kappa(betagamma) = -1 + 1 = 0."""
        result = koszul_dual_cy_data('bc', {})
        self.assertEqual(result['kappa_sum'], 0)


# ============================================================
# Test Group 5: Kappa values (AP1/AP20/AP39 cross-checks)
# ============================================================

class TestKappaValues(unittest.TestCase):
    """Kappa computation with AP1 cross-checks."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        self.assertEqual(kappa_value('heisenberg', {'k': 1}), 1)
        self.assertEqual(kappa_value('heisenberg', {'k': Fraction(3, 2)}),
                         Fraction(3, 2))

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        self.assertEqual(kappa_value('virasoro', {'c': 26}), 13)
        self.assertEqual(kappa_value('virasoro', {'c': 1}), Fraction(1, 2))

    def test_sl2_kappa(self):
        """kappa(V_k(sl_2)) = 3*(k+2)/4. At k=1: 9/4."""
        result = kappa_value('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertEqual(result, Fraction(9, 4))

    def test_sl3_kappa(self):
        """kappa(V_k(sl_3)) = 8*(k+3)/6 = 4*(k+3)/3. At k=1: 16/3."""
        result = kappa_value('affine_km', {'g_type': 'A', 'rank': 2, 'k': 1})
        self.assertEqual(result, Fraction(16, 3))

    def test_bc_kappa(self):
        """kappa(bc) = -1."""
        self.assertEqual(kappa_value('bc', {}), Fraction(-1))

    def test_betagamma_kappa(self):
        """kappa(betagamma) = 1."""
        self.assertEqual(kappa_value('betagamma', {}), Fraction(1))

    def test_e8_kappa(self):
        """kappa(V_1(E_8)) = 248*(1+30)/60 = 248*31/60 = 7688/60 = 1922/15."""
        result = kappa_value('affine_km', {'g_type': 'E', 'rank': 8, 'k': 1})
        self.assertEqual(result, Fraction(248 * 31, 60))


# ============================================================
# Test Group 6: CY exchange consistency across all families
# ============================================================

class TestCYExchangeAllFamilies(unittest.TestCase):
    """Verify CY exchange consistency for all 17 standard families."""

    def test_all_families_consistent(self):
        """HR24 exchange: smooth CY => proper CY on bar, each side independently."""
        results = verify_cy_exchange_all_families()
        for r in results:
            self.assertTrue(
                r['exchange_consistent'],
                f"CY exchange inconsistent for {r['family']} "
                f"with params {r['params']}"
            )

    def test_symmetric_pairs(self):
        """Pairs where both A and A! have smooth CY are CY-symmetric."""
        results = verify_cy_exchange_all_families()
        for r in results:
            if r['smooth_cy_on_A'] and r['smooth_cy_on_A_dual']:
                self.assertTrue(r['cy_symmetric'],
                                f"Expected CY-symmetric for {r['family']}")

    def test_virasoro_c26_asymmetric(self):
        """Vir_26 has smooth CY but Vir_0 (its dual) is a minimal model.

        This is a genuine CY asymmetry: the Koszul dual lands at a
        degenerate point.  Verdier intertwining D_Ran(B(A)) ~ B(A!)
        does NOT require the CY structures to match.
        """
        results = verify_cy_exchange_all_families()
        c26_result = [r for r in results
                      if r['family'] == 'virasoro' and r['params'] == {'c': 26}][0]
        self.assertTrue(c26_result['smooth_cy_on_A'])
        self.assertFalse(c26_result['smooth_cy_on_A_dual'])
        self.assertFalse(c26_result['cy_symmetric'])
        # But exchange is still consistent: each side satisfies HR24 independently
        self.assertTrue(c26_result['exchange_consistent'])

    def test_seventeen_families_tested(self):
        results = verify_cy_exchange_all_families()
        self.assertEqual(len(results), len(STANDARD_FAMILIES))


# ============================================================
# Test Group 7: Shifted symplectic degree
# ============================================================

class TestShiftedSymplecticDegree(unittest.TestCase):
    """Shifted symplectic degree on C_g(A) and M_comp."""

    def test_genus_0_shift(self):
        self.assertEqual(shifted_symplectic_degree_genus(0), 3)

    def test_genus_1_shift(self):
        """Genus 1: shift = 0 (ordinary symplectic)."""
        self.assertEqual(shifted_symplectic_degree_genus(1), 0)

    def test_genus_2_shift(self):
        self.assertEqual(shifted_symplectic_degree_genus(2), -3)

    def test_genus_3_shift(self):
        self.assertEqual(shifted_symplectic_degree_genus(3), -6)

    def test_total_shift(self):
        """Total deformation space: (-1)-shifted symplectic."""
        self.assertEqual(shifted_symplectic_degree_total(), -1)

    def test_shift_formula(self):
        """shift(g) = -(3g-3) for all g."""
        for g in range(10):
            self.assertEqual(
                shifted_symplectic_degree_genus(g), -(3 * g - 3))


# ============================================================
# Test Group 8: Lagrangian dimension
# ============================================================

class TestLagrangianDimension(unittest.TestCase):
    """Lagrangian subspaces have half dimension."""

    def test_genus_1_lagrangian(self):
        result = verify_lagrangian_dimension(1, 1)
        self.assertTrue(result['lagrangian'])
        self.assertEqual(result['dim_total'], 2)
        self.assertEqual(result['dim_Q_A'], 1)

    def test_genus_2_lagrangian(self):
        result = verify_lagrangian_dimension(2, 1)
        self.assertTrue(result['lagrangian'])
        self.assertEqual(result['dim_total'], 4)
        self.assertEqual(result['dim_Q_A'], 2)


# ============================================================
# Test Group 9: Genuine values (VAL1-VAL4)
# ============================================================

class TestVAL1FiberPerfectness(unittest.TestCase):
    """VAL1: HR24 explains fiber-level perfectness."""

    def test_heisenberg(self):
        result = verify_val1_fiber_perfectness('heisenberg', {'k': 1})
        self.assertTrue(result['val1_holds'])

    def test_virasoro(self):
        result = verify_val1_fiber_perfectness('virasoro', {'c': 1})
        self.assertTrue(result['val1_holds'])

    def test_affine_km(self):
        result = verify_val1_fiber_perfectness(
            'affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertTrue(result['val1_holds'])

    def test_degenerate_case(self):
        result = verify_val1_fiber_perfectness('heisenberg', {'k': 0})
        self.assertTrue(result['val1_holds'])  # both sides False


class TestVAL2P3Redundancy(unittest.TestCase):
    """VAL2: (P3) is redundant on the Koszul locus."""

    def test_heisenberg(self):
        result = verify_val2_p3_redundancy('heisenberg', {'k': 1})
        self.assertTrue(result['p3_redundant'])

    def test_virasoro(self):
        result = verify_val2_p3_redundancy('virasoro', {'c': 1})
        self.assertTrue(result['p3_redundant'])

    def test_affine_km(self):
        result = verify_val2_p3_redundancy(
            'affine_km', {'g_type': 'A', 'rank': 2, 'k': 1})
        self.assertTrue(result['p3_redundant'])

    def test_degenerate_not_redundant(self):
        result = verify_val2_p3_redundancy('heisenberg', {'k': 0})
        self.assertFalse(result['p3_redundant'])


class TestVAL3ConceptualFramework(unittest.TestCase):
    """VAL3: CY gives conceptual framework for Theorem C."""

    def test_val3_holds(self):
        result = verify_val3_conceptual_framework()
        self.assertTrue(result['val3_holds'])

    def test_mechanism_has_five_steps(self):
        result = verify_val3_conceptual_framework()
        self.assertEqual(len(result['mechanism_chain']), 5)


class TestVAL4ShadowTowerAKSZ(unittest.TestCase):
    """VAL4: Shadow tower connected to AKSZ."""

    def test_val4_holds(self):
        result = verify_val4_shadow_tower_from_aksz()
        self.assertTrue(result['val4_holds'])

    def test_kappa_is_arity2(self):
        result = verify_val4_shadow_tower_from_aksz()
        self.assertEqual(result['identification']['kappa'], 'arity-2 AKSZ datum')


# ============================================================
# Test Group 10: Full analysis report
# ============================================================

class TestFullAnalysis(unittest.TestCase):
    """The complete CY exchange analysis."""

    def test_cannot_replace_thm_a(self):
        report = full_cy_exchange_analysis()
        self.assertFalse(report['can_replace_thm_a'])

    def test_provides_genuine_value(self):
        report = full_cy_exchange_analysis()
        self.assertTrue(report['provides_genuine_value'])

    def test_five_obstructions(self):
        report = full_cy_exchange_analysis()
        self.assertEqual(len(report['obstructions']), 5)

    def test_all_families_consistent(self):
        report = full_cy_exchange_analysis()
        self.assertTrue(report['all_families_consistent'])


# ============================================================
# Test Group 11: Kappa complementarity (AP24)
# ============================================================

class TestKappaComplementarity(unittest.TestCase):
    """AP24 cross-check under CY exchange."""

    def test_heisenberg_sum_zero(self):
        result = kappa_complementarity_under_cy('heisenberg', {'k': 1})
        self.assertEqual(result['kappa_sum'], 0)
        self.assertTrue(result['ap24_consistent'])

    def test_heisenberg_negative_sum_zero(self):
        result = kappa_complementarity_under_cy('heisenberg', {'k': -5})
        self.assertEqual(result['kappa_sum'], 0)

    def test_virasoro_sum_13(self):
        result = kappa_complementarity_under_cy('virasoro', {'c': 1})
        self.assertEqual(result['kappa_sum'], 13)
        self.assertTrue(result['ap24_consistent'])

    def test_virasoro_c26_sum_13(self):
        result = kappa_complementarity_under_cy('virasoro', {'c': 26})
        self.assertEqual(result['kappa_sum'], 13)

    def test_affine_km_sum_zero(self):
        result = kappa_complementarity_under_cy(
            'affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertEqual(result['kappa_sum'], 0)
        self.assertTrue(result['ap24_consistent'])

    def test_affine_e8_sum_zero(self):
        result = kappa_complementarity_under_cy(
            'affine_km', {'g_type': 'E', 'rank': 8, 'k': 1})
        self.assertEqual(result['kappa_sum'], 0)

    def test_bc_sum_zero(self):
        result = kappa_complementarity_under_cy('bc', {})
        self.assertEqual(result['kappa_sum'], 0)
        self.assertTrue(result['ap24_consistent'])


# ============================================================
# Test Group 12: CY dimension consistency
# ============================================================

class TestCYDimensionConsistency(unittest.TestCase):
    """CY dimension is 1 for all chiral algebras on curves."""

    def test_heisenberg(self):
        result = cy_dimension_consistency('heisenberg', {'k': 1})
        self.assertEqual(result['cy_dim'], 1)
        self.assertTrue(result['consistent'])

    def test_virasoro(self):
        result = cy_dimension_consistency('virasoro', {'c': 1})
        self.assertEqual(result['cy_dim'], 1)

    def test_affine_km(self):
        result = cy_dimension_consistency(
            'affine_km', {'g_type': 'E', 'rank': 8, 'k': 1})
        self.assertEqual(result['cy_dim'], 1)

    def test_bc(self):
        result = cy_dimension_consistency('bc', {})
        self.assertEqual(result['cy_dim'], 1)


# ============================================================
# Test Group 13: Dependency DAG
# ============================================================

class TestDependencyDAG(unittest.TestCase):
    """Dependency DAG correctness."""

    def test_thm_a_in_chain_of_c(self):
        chain = get_dependency_chain('thm_C_complementarity')
        self.assertIn('thm_A_adjunction', chain)

    def test_thm_b_in_chain_of_c(self):
        chain = get_dependency_chain('thm_C_complementarity')
        self.assertIn('thm_B_inversion', chain)

    def test_thm_c_not_in_chain_of_a(self):
        chain = get_dependency_chain('thm_A_adjunction')
        self.assertNotIn('thm_C_complementarity', chain)

    def test_k11_depends_on_c(self):
        chain = get_dependency_chain('K11_lagrangian_criterion')
        self.assertIn('thm_C_complementarity', chain)

    def test_hr24_depends_on_bar(self):
        deps = DEPENDENCY_DAG['HR24_cy_exchange']['depends_on']
        self.assertIn('bar_construction_exists', deps)

    def test_perfectness_depends_on_pbw(self):
        deps = DEPENDENCY_DAG['perfectness_criterion']['depends_on']
        self.assertIn('pbw_filterability', deps)


# ============================================================
# Test Group 14: Obstruction and value registers
# ============================================================

class TestRegisters(unittest.TestCase):
    """Obstruction and value registers are complete."""

    def test_five_obstructions_registered(self):
        self.assertEqual(len(OBSTRUCTION_REGISTER), 5)

    def test_four_values_registered(self):
        self.assertEqual(len(VALUE_REGISTER), 4)

    def test_ob1_is_fatal(self):
        self.assertEqual(OBSTRUCTION_REGISTER['OB1']['severity'], 'FATAL')

    def test_ob2_is_fatal(self):
        self.assertEqual(OBSTRUCTION_REGISTER['OB2']['severity'], 'FATAL')

    def test_ob4_is_fatal(self):
        self.assertEqual(OBSTRUCTION_REGISTER['OB4']['severity'], 'FATAL')


if __name__ == '__main__':
    unittest.main()
