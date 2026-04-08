#!/usr/bin/env python3
r"""Tests for the Holstein-Rivera CY rectification engine.

Tests verify:
1. Smooth CY existence for all standard families
2. Proper CY on bar complexes (HR24 consequence)
3. K11 hypothesis verification (P1)-(P3)
4. Shifted symplectic pairing for sl_2
5. HR24 interchange consistency
6. Kappa complementarity (AP24 cross-check)
7. Complementarity dimensions at genus 1 and 2
8. P3 redundancy analysis
9. HR24 Lie algebra application (unimodularity)
10. Finding register consistency

Ground truth sources:
  - higher_genus_complementarity.tex (Theorem C, thm:quantum-complementarity-main)
  - chiral_koszul_pairs.tex (K11, thm:koszul-equivalences-meta item (xi))
  - bar_cobar_adjunction_inversion.tex (prop:lagrangian-perfectness)
  - Holstein-Rivera, arXiv:2410.03604 (Theorem 1.1, 1.3)
  - Calaque-Safronov, arXiv:2407.08622

Multi-path verification (per CLAUDE.md mandate):
  Path 1: Direct computation from definitions
  Path 2: Cross-family consistency (AP24, AP39)
  Path 3: HR24 interchange consistency
"""

import unittest
from fractions import Fraction

from compute.lib.theorem_thm_c_cy_rectification_engine import (
    smooth_cy_dimension_lie,
    smooth_cy_exists_affine_km,
    smooth_cy_exists_heisenberg,
    smooth_cy_exists_virasoro,
    smooth_cy_exists_bc,
    smooth_cy_exists_betagamma,
    proper_cy_on_bar,
    verify_k11_hypotheses,
    shifted_symplectic_pairing_sl2,
    verify_hr24_interchange,
    kappa_from_family,
    kappa_complementarity_sum,
    complementarity_dimensions_genus1,
    complementarity_dimensions_genus2,
    p3_redundancy_analysis,
    hr24_lie_algebra_application,
    FINDING_REGISTER,
)


class TestSmoothCYDimensionLie(unittest.TestCase):
    """Test CY dimension computation for finite-dim Lie algebras."""

    def test_sl2_dim(self):
        dim, uni = smooth_cy_dimension_lie('A', 1)
        self.assertEqual(dim, 3)
        self.assertTrue(uni)

    def test_sl3_dim(self):
        dim, uni = smooth_cy_dimension_lie('A', 2)
        self.assertEqual(dim, 8)
        self.assertTrue(uni)

    def test_sl4_dim(self):
        dim, uni = smooth_cy_dimension_lie('A', 3)
        self.assertEqual(dim, 15)
        self.assertTrue(uni)

    def test_so5_dim(self):
        dim, uni = smooth_cy_dimension_lie('B', 2)
        self.assertEqual(dim, 10)
        self.assertTrue(uni)

    def test_sp4_dim(self):
        dim, uni = smooth_cy_dimension_lie('C', 2)
        self.assertEqual(dim, 10)
        self.assertTrue(uni)

    def test_so8_dim(self):
        dim, uni = smooth_cy_dimension_lie('D', 4)
        self.assertEqual(dim, 28)
        self.assertTrue(uni)

    def test_g2_dim(self):
        dim, uni = smooth_cy_dimension_lie('G', 2)
        self.assertEqual(dim, 14)
        self.assertTrue(uni)

    def test_e8_dim(self):
        dim, uni = smooth_cy_dimension_lie('E', 8)
        self.assertEqual(dim, 248)
        self.assertTrue(uni)

    def test_all_semisimple_unimodular(self):
        """All simple Lie algebras are unimodular."""
        for (g, r) in [('A', 1), ('A', 2), ('A', 3), ('B', 2), ('C', 2),
                        ('D', 4), ('G', 2), ('F', 4), ('E', 6), ('E', 7), ('E', 8)]:
            _, uni = smooth_cy_dimension_lie(g, r)
            self.assertTrue(uni, f"{g}_{r} should be unimodular")


class TestSmoothCYHeisenberg(unittest.TestCase):
    """Test smooth CY for Heisenberg."""

    def test_positive_level(self):
        result = smooth_cy_exists_heisenberg(1)
        self.assertTrue(result['has_smooth_cy'])

    def test_negative_level(self):
        result = smooth_cy_exists_heisenberg(-3)
        self.assertTrue(result['has_smooth_cy'])

    def test_zero_level_degenerates(self):
        result = smooth_cy_exists_heisenberg(0)
        self.assertFalse(result['has_smooth_cy'])

    def test_fractional_level(self):
        result = smooth_cy_exists_heisenberg(Fraction(1, 2))
        self.assertTrue(result['has_smooth_cy'])


class TestSmoothCYAffineKM(unittest.TestCase):
    """Test smooth CY for affine Kac-Moody."""

    def test_sl2_generic_level(self):
        result = smooth_cy_exists_affine_km('A', 1, 1)
        self.assertTrue(result['has_smooth_cy'])
        self.assertFalse(result['is_critical'])

    def test_sl2_critical_level(self):
        """At k = -h^v = -2: critical level. Invariant form still nondegenerate."""
        result = smooth_cy_exists_affine_km('A', 1, -2)
        # k = -2 != 0, so form is nondegenerate
        self.assertTrue(result['has_smooth_cy'])
        self.assertTrue(result['is_critical'])

    def test_sl2_zero_level(self):
        result = smooth_cy_exists_affine_km('A', 1, 0)
        self.assertFalse(result['has_smooth_cy'])

    def test_sl3_generic(self):
        result = smooth_cy_exists_affine_km('A', 2, 5)
        self.assertTrue(result['has_smooth_cy'])

    def test_e8_generic(self):
        result = smooth_cy_exists_affine_km('E', 8, 1)
        self.assertTrue(result['has_smooth_cy'])

    def test_g2_critical(self):
        """G2 has h^v = 4. Critical at k = -4."""
        result = smooth_cy_exists_affine_km('G', 2, -4)
        self.assertTrue(result['has_smooth_cy'])
        self.assertTrue(result['is_critical'])


class TestSmoothCYVirasoro(unittest.TestCase):
    """Test smooth CY for Virasoro."""

    def test_generic_c(self):
        result = smooth_cy_exists_virasoro(7)
        self.assertTrue(result['has_smooth_cy'])

    def test_c_equals_26(self):
        result = smooth_cy_exists_virasoro(26)
        self.assertTrue(result['has_smooth_cy'])

    def test_c_equals_13_selfdual(self):
        result = smooth_cy_exists_virasoro(13)
        self.assertTrue(result['has_smooth_cy'])

    def test_ising_minimal_model(self):
        """Ising model: c = 1/2 (p=4, q=3)."""
        result = smooth_cy_exists_virasoro(Fraction(1, 2))
        self.assertTrue(result['is_minimal_model'])
        self.assertFalse(result['has_smooth_cy'])

    def test_tricritical_ising(self):
        """Tricritical Ising: c = 7/10 (p=5, q=4)."""
        result = smooth_cy_exists_virasoro(Fraction(7, 10))
        self.assertTrue(result['is_minimal_model'])
        self.assertFalse(result['has_smooth_cy'])

    def test_c_zero_minimal(self):
        """c = 0 (p=3, q=2) is a minimal model."""
        result = smooth_cy_exists_virasoro(0)
        self.assertTrue(result['is_minimal_model'])


class TestSmoothCYFreeFields(unittest.TestCase):
    """Test smooth CY for free field systems."""

    def test_bc_always(self):
        result = smooth_cy_exists_bc()
        self.assertTrue(result['has_smooth_cy'])

    def test_betagamma_always(self):
        result = smooth_cy_exists_betagamma()
        self.assertTrue(result['has_smooth_cy'])


class TestProperCYOnBar(unittest.TestCase):
    """Test HR24 proper CY on bar complex."""

    def test_heisenberg_proper_cy(self):
        result = proper_cy_on_bar('heisenberg', {'k': 1})
        self.assertTrue(result['has_proper_cy'])
        self.assertTrue(result['hr24_applies'])

    def test_heisenberg_zero_no_proper(self):
        result = proper_cy_on_bar('heisenberg', {'k': 0})
        self.assertFalse(result['has_proper_cy'])

    def test_affine_km_proper_cy(self):
        result = proper_cy_on_bar('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertTrue(result['has_proper_cy'])

    def test_virasoro_generic_proper_cy(self):
        result = proper_cy_on_bar('virasoro', {'c': 7})
        self.assertTrue(result['has_proper_cy'])

    def test_bc_proper_cy(self):
        result = proper_cy_on_bar('bc', {})
        self.assertTrue(result['has_proper_cy'])

    def test_betagamma_proper_cy(self):
        result = proper_cy_on_bar('betagamma', {})
        self.assertTrue(result['has_proper_cy'])


class TestK11Hypotheses(unittest.TestCase):
    """Test K11 hypothesis verification."""

    def test_heisenberg_k1(self):
        result = verify_k11_hypotheses('heisenberg', {'k': 1})
        self.assertTrue(result['valid'])
        self.assertTrue(result['P1']['holds'])
        self.assertTrue(result['P2']['holds'])
        self.assertTrue(result['P3']['holds'])
        self.assertTrue(result['k11_unconditional'])

    def test_heisenberg_k0_fails(self):
        result = verify_k11_hypotheses('heisenberg', {'k': 0})
        self.assertFalse(result['valid'])
        self.assertFalse(result['P2']['holds'])

    def test_sl2_generic(self):
        result = verify_k11_hypotheses('affine_km',
                                        {'g_type': 'A', 'rank': 1, 'k': 1})
        self.assertTrue(result['valid'])

    def test_sl2_dual_zero(self):
        """k = -2h^v = -4 gives dual level 0. P3 fails."""
        result = verify_k11_hypotheses('affine_km',
                                        {'g_type': 'A', 'rank': 1, 'k': -4})
        # k = -4, h^v = 2, k_dual = -(-4) - 2*2 = 4 - 4 = 0
        self.assertFalse(result['P3']['holds'])
        self.assertFalse(result['valid'])

    def test_virasoro_generic(self):
        result = verify_k11_hypotheses('virasoro', {'c': 7})
        self.assertTrue(result['valid'])

    def test_virasoro_c13_selfdual(self):
        result = verify_k11_hypotheses('virasoro', {'c': 13})
        self.assertTrue(result['valid'])
        self.assertTrue(result['P3']['holds'])

    def test_bc_unconditional(self):
        result = verify_k11_hypotheses('bc', {})
        self.assertTrue(result['valid'])
        self.assertTrue(result['k11_unconditional'])

    def test_betagamma_unconditional(self):
        result = verify_k11_hypotheses('betagamma', {})
        self.assertTrue(result['valid'])

    def test_hr24_fiber_perfectness_comment(self):
        """HR24 comment should explain fiber vs family perfectness."""
        result = verify_k11_hypotheses('heisenberg', {'k': 1})
        self.assertIn('fiber-level', result['hr24_comment'])
        self.assertIn('Family-level', result['hr24_comment'])


class TestShiftedSymplecticPairing(unittest.TestCase):
    """Test shifted symplectic pairing for sl_2."""

    def test_sl2_k1_low_weight_nondegenerate(self):
        """At k=1 (admissible level for sl_2), Shapovalov form is
        nondegenerate at weights 0,1,2 but has null vectors at weight 3
        (because k+2=3, so the Kac-Kazhdan factor vanishes at r=3).
        This is CORRECT: admissible levels have null vectors.
        The smooth CY on A (invariant form nondegenerate) is a DIFFERENT
        statement from Shapovalov nondegeneracy at all weights."""
        result = shifted_symplectic_pairing_sl2(1, weight_max=2)
        self.assertTrue(result['nondegenerate'])
        self.assertTrue(result['lagrangian_condition_met'])

    def test_sl2_k1_null_vector_at_weight3(self):
        """At k=1: null vector appears at weight 3 (k+2=3, r=3, s=1).
        This is the correct Kac-Kazhdan prediction."""
        result = shifted_symplectic_pairing_sl2(1, weight_max=3)
        self.assertFalse(result['weight_data'][3]['nondegenerate'])
        # But weights 0,1,2 are still nondegenerate
        self.assertTrue(result['weight_data'][0]['nondegenerate'])
        self.assertTrue(result['weight_data'][1]['nondegenerate'])
        self.assertTrue(result['weight_data'][2]['nondegenerate'])

    def test_sl2_k0_degenerate(self):
        result = shifted_symplectic_pairing_sl2(0)
        self.assertFalse(result['nondegenerate'])

    def test_sl2_k2_nondegenerate_below_null(self):
        """At k=2: k+2=4, null vector at weight 4. Nondegenerate at 0..3."""
        result = shifted_symplectic_pairing_sl2(2, weight_max=3)
        self.assertTrue(result['nondegenerate'])

    def test_sl2_generic_level_nondegenerate(self):
        """At generic (non-integer) level, no null vectors at any weight."""
        result = shifted_symplectic_pairing_sl2(Fraction(7, 3), weight_max=6)
        self.assertTrue(result['nondegenerate'])

    def test_sl2_weight0_dim1(self):
        result = shifted_symplectic_pairing_sl2(1, weight_max=0)
        self.assertEqual(result['weight_data'][0]['dim'], 1)

    def test_sl2_weight1_dim3(self):
        """Weight 1: 3 states J^+_{-1}|0>, J^-_{-1}|0>, J^0_{-1}|0>."""
        result = shifted_symplectic_pairing_sl2(1, weight_max=1)
        self.assertEqual(result['weight_data'][1]['dim'], 3)

    def test_sl2_weight2_dim9(self):
        """Weight 2: 3-colored partitions of 2.
        (2): 3 choices, (1,1): 3*3 - 3 + 3*2/2 = 6 choices.
        Total: 3 + 6 = 9."""
        result = shifted_symplectic_pairing_sl2(1, weight_max=2)
        self.assertEqual(result['weight_data'][2]['dim'], 9)

    def test_sl2_admissible_k_minus1(self):
        """k = -1: admissible level for sl_2. Should have null vectors."""
        result = shifted_symplectic_pairing_sl2(-1, weight_max=3)
        # k + 2 = 1, so Shapovalov det vanishes when r = 1, rs <= n
        # At weight 1: r=1, s=1, factor = k+2-1 = 0. Det = 0.
        self.assertFalse(result['weight_data'][1]['nondegenerate'])


class TestHR24Interchange(unittest.TestCase):
    """Test HR24 smooth<->proper CY interchange."""

    def test_heisenberg_interchange(self):
        result = verify_hr24_interchange('heisenberg', {'k': 1})
        self.assertTrue(result['A_smooth_cy'])
        self.assertTrue(result['BA_proper_cy'])
        self.assertTrue(result['A_dual_smooth_cy'])
        self.assertTrue(result['BA_dual_proper_cy'])
        self.assertTrue(result['verdier_consistent'])
        self.assertTrue(result['all_verified'])

    def test_sl2_interchange(self):
        result = verify_hr24_interchange('affine_km',
                                          {'g_type': 'A', 'rank': 1, 'k': 3})
        self.assertTrue(result['all_verified'])

    def test_virasoro_interchange(self):
        result = verify_hr24_interchange('virasoro', {'c': 7})
        self.assertTrue(result['all_verified'])

    def test_bc_betagamma_interchange(self):
        result_bc = verify_hr24_interchange('bc', {})
        result_bg = verify_hr24_interchange('betagamma', {})
        self.assertTrue(result_bc['all_verified'])
        self.assertTrue(result_bg['all_verified'])

    def test_virasoro_c13_selfdual_interchange(self):
        result = verify_hr24_interchange('virasoro', {'c': 13})
        self.assertTrue(result['all_verified'])
        self.assertTrue(result['verdier_consistent'])


class TestKappaComplementarity(unittest.TestCase):
    """Test kappa values and complementarity sums (AP24 cross-check)."""

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        self.assertEqual(kappa_from_family('heisenberg', {'k': 3}), Fraction(3))

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        self.assertEqual(kappa_from_family('virasoro', {'c': 10}), Fraction(5))

    def test_sl2_kappa(self):
        """kappa(V_k(sl_2)) = 3(k+2)/(2*2) = 3(k+2)/4."""
        k = Fraction(1)
        expected = Fraction(3) * (k + 2) / 4
        self.assertEqual(kappa_from_family('affine_km',
                         {'g_type': 'A', 'rank': 1, 'k': 1}), expected)

    def test_bc_kappa(self):
        """kappa(bc) = -1."""
        self.assertEqual(kappa_from_family('bc', {}), Fraction(-1))

    def test_betagamma_kappa(self):
        """kappa(betagamma) = 1."""
        self.assertEqual(kappa_from_family('betagamma', {}), Fraction(1))

    def test_heisenberg_complementarity_sum_zero(self):
        """AP24: kappa(H_k) + kappa(H_k^!) = k + (-k) = 0."""
        result = kappa_complementarity_sum('heisenberg', {'k': 5})
        self.assertEqual(result['sum'], 0)

    def test_virasoro_complementarity_sum_13(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        for c in [0, 1, 7, 13, 26, 100]:
            result = kappa_complementarity_sum('virasoro', {'c': c})
            self.assertEqual(result['sum'], 13,
                             f"Failed at c={c}: got {result['sum']}")

    def test_affine_km_complementarity_sum_zero(self):
        """AP24: kappa(V_k(g)) + kappa(V_{-k-2h^v}(g)) = 0 (Feigin-Frenkel)."""
        result = kappa_complementarity_sum('affine_km',
                                            {'g_type': 'A', 'rank': 1, 'k': 3})
        self.assertEqual(result['sum'], 0)

    def test_bc_betagamma_complementarity_sum_zero(self):
        """kappa(bc) + kappa(betagamma) = -1 + 1 = 0."""
        result = kappa_complementarity_sum('bc', {})
        self.assertEqual(result['sum'], 0)

    def test_multiple_km_families_sum_zero(self):
        """Verify kappa + kappa' = 0 for multiple KM families."""
        for (g, r) in [('A', 1), ('A', 2), ('B', 2), ('G', 2)]:
            for k in [1, 3, 7]:
                result = kappa_complementarity_sum(
                    'affine_km', {'g_type': g, 'rank': r, 'k': k})
                self.assertEqual(result['sum'], 0,
                                 f"Failed for {g}_{r} at k={k}")


class TestComplementarityDimensions(unittest.TestCase):
    """Test complementarity dimension counts."""

    def test_genus1_heisenberg(self):
        result = complementarity_dimensions_genus1('heisenberg', {'k': 1})
        self.assertTrue(result['complementarity_holds'])
        self.assertEqual(result['dim_Q_A'] + result['dim_Q_A_dual'],
                         result['dim_H_total'])

    def test_genus1_virasoro(self):
        result = complementarity_dimensions_genus1('virasoro', {'c': 7})
        self.assertTrue(result['complementarity_holds'])
        self.assertTrue(result['lagrangian'])

    def test_genus1_all_families(self):
        """All standard families have complementarity at genus 1."""
        families = [
            ('heisenberg', {'k': 1}),
            ('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1}),
            ('virasoro', {'c': 7}),
            ('bc', {}),
            ('betagamma', {}),
        ]
        for fam, params in families:
            result = complementarity_dimensions_genus1(fam, params)
            self.assertTrue(result['complementarity_holds'],
                            f"Failed for {fam}")

    def test_genus2_heisenberg(self):
        result = complementarity_dimensions_genus2('heisenberg', {'k': 1})
        self.assertTrue(result['complementarity_holds'])
        self.assertTrue(result['lagrangian'])

    def test_genus2_half_rank(self):
        """Lagrangian = half rank of total space."""
        result = complementarity_dimensions_genus2('virasoro', {'c': 7})
        self.assertEqual(result['dim_Q_A'], result['dim_Q_A_dual'])
        self.assertEqual(2 * result['dim_Q_A'], result['dim_H_total'])


class TestP3Redundancy(unittest.TestCase):
    """Test P3 redundancy analysis."""

    def test_p3_not_redundant_general(self):
        """P3 is NOT redundant in general."""
        result = p3_redundancy_analysis('heisenberg', {'k': 1})
        self.assertFalse(result['p3_redundant'])

    def test_p3_redundant_bc(self):
        """P3 is redundant for bc (dual = betagamma, always smooth CY)."""
        result = p3_redundancy_analysis('bc', {})
        self.assertTrue(result['p3_redundant'])

    def test_p3_redundant_betagamma(self):
        result = p3_redundancy_analysis('betagamma', {})
        self.assertTrue(result['p3_redundant'])

    def test_p3_redundant_virasoro_c13(self):
        """At c=13: Vir_c self-dual, P3 follows from P2."""
        result = p3_redundancy_analysis('virasoro', {'c': 13})
        self.assertTrue(result['p3_redundant'])

    def test_p3_not_redundant_virasoro_generic(self):
        """At generic c: Vir_c != Vir_{26-c}, P3 independent."""
        result = p3_redundancy_analysis('virasoro', {'c': 7})
        self.assertFalse(result['p3_redundant'])

    def test_p3_not_redundant_km(self):
        """For KM, P3 independent (dual at different level)."""
        result = p3_redundancy_analysis('affine_km',
                                         {'g_type': 'A', 'rank': 1, 'k': 3})
        self.assertFalse(result['p3_redundant'])


class TestHR24LieAlgebra(unittest.TestCase):
    """Test HR24 Lie algebra application."""

    def test_sl2_unimodular(self):
        result = hr24_lie_algebra_application('A', 1)
        self.assertTrue(result['is_unimodular'])
        self.assertEqual(result['cy_dimension'], 3)
        self.assertTrue(result['smooth_cy_on_Ug'])
        self.assertTrue(result['proper_cy_on_CE'])

    def test_e8_unimodular(self):
        result = hr24_lie_algebra_application('E', 8)
        self.assertTrue(result['is_unimodular'])
        self.assertEqual(result['cy_dimension'], 248)

    def test_g2_unimodular(self):
        result = hr24_lie_algebra_application('G', 2)
        self.assertTrue(result['is_unimodular'])
        self.assertEqual(result['cy_dimension'], 14)

    def test_all_classical_unimodular(self):
        """All classical Lie algebras are unimodular."""
        for (g, r) in [('A', 1), ('A', 2), ('A', 3), ('A', 4),
                        ('B', 2), ('B', 3), ('C', 2), ('C', 3), ('D', 4)]:
            result = hr24_lie_algebra_application(g, r)
            self.assertTrue(result['is_unimodular'], f"{g}_{r}")
            self.assertIsNotNone(result['cy_dimension'])

    def test_cy_dim_equals_lie_dim(self):
        """CY dimension = dim(g) for unimodular g."""
        for (g, r) in [('A', 1), ('A', 2), ('E', 6), ('E', 8)]:
            result = hr24_lie_algebra_application(g, r)
            self.assertEqual(result['cy_dimension'], result['dim_g'])


class TestFindingRegister(unittest.TestCase):
    """Test finding register consistency."""

    def test_all_findings_have_required_fields(self):
        for key, finding in FINDING_REGISTER.items():
            self.assertIn('severity', finding, f"Missing severity in {key}")
            self.assertIn('class', finding, f"Missing class in {key}")
            self.assertIn('finding', finding, f"Missing finding in {key}")
            self.assertIn('status', finding, f"Missing status in {key}")
            self.assertIn('action', finding, f"Missing action in {key}")

    def test_f7_critical_no_false_claims(self):
        """F7 is the critical finding: no claims become false."""
        self.assertEqual(FINDING_REGISTER['F7']['severity'], 'CRITICAL')
        self.assertEqual(FINDING_REGISTER['F7']['status'], 'CONFIRMED')

    def test_severity_values(self):
        valid = {'CRITICAL', 'SERIOUS', 'MODERATE', 'MINOR'}
        for key, finding in FINDING_REGISTER.items():
            self.assertIn(finding['severity'], valid, f"Invalid severity in {key}")

    def test_class_values(self):
        valid = {'A', 'B', 'C', 'D', 'E'}
        for key, finding in FINDING_REGISTER.items():
            self.assertIn(finding['class'], valid, f"Invalid class in {key}")


class TestCrossConsistency(unittest.TestCase):
    """Cross-family and cross-method consistency checks."""

    def test_kappa_is_positive_for_unitary_families(self):
        """For physical (unitary) families, kappa > 0."""
        self.assertGreater(kappa_from_family('heisenberg', {'k': 1}), 0)
        self.assertGreater(kappa_from_family('virasoro', {'c': 26}), 0)
        self.assertGreater(kappa_from_family('affine_km',
                           {'g_type': 'A', 'rank': 1, 'k': 1}), 0)

    def test_hr24_interchange_both_sides(self):
        """If A has smooth CY and A! has smooth CY, both bar complexes have
        proper CY. Verdier intertwining is consistent."""
        for fam, params in [
            ('heisenberg', {'k': 1}),
            ('virasoro', {'c': 7}),
            ('bc', {}),
        ]:
            result = verify_hr24_interchange(fam, params)
            if result['A_smooth_cy'] and result['A_dual_smooth_cy']:
                self.assertTrue(result['verdier_consistent'],
                                f"Verdier inconsistent for {fam}")

    def test_k11_valid_implies_hr24_valid(self):
        """If K11 hypotheses hold, HR24 must also give proper CY on both sides."""
        for fam, params in [
            ('heisenberg', {'k': 1}),
            ('virasoro', {'c': 7}),
            ('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1}),
            ('bc', {}),
            ('betagamma', {}),
        ]:
            k11 = verify_k11_hypotheses(fam, params)
            hr24 = verify_hr24_interchange(fam, params)
            if k11['valid']:
                self.assertTrue(hr24['BA_proper_cy'],
                                f"K11 valid but HR24 fails for {fam}")
                self.assertTrue(hr24['BA_dual_proper_cy'],
                                f"K11 valid but HR24 dual fails for {fam}")

    def test_complementarity_lagrangian_at_genus1_all_families(self):
        """All standard families are Lagrangian at genus 1."""
        for fam, params in [
            ('heisenberg', {'k': 1}),
            ('virasoro', {'c': 7}),
            ('affine_km', {'g_type': 'A', 'rank': 1, 'k': 1}),
            ('bc', {}),
            ('betagamma', {}),
        ]:
            result = complementarity_dimensions_genus1(fam, params)
            self.assertTrue(result['lagrangian'],
                            f"Not Lagrangian at g=1 for {fam}")


if __name__ == '__main__':
    unittest.main()
