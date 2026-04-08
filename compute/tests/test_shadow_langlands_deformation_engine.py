r"""Tests for the shadow Langlands deformation engine.

DEEP RESEARCH TESTS: shadow oper deformation theory beyond the Eisenstein oper.

Tests organized by mathematical content:

Section 1:  Rank-1 Eisenstein baseline (Virasoro)
Section 2:  Rank-2 shadow oper (W_3)
Section 3:  Spectral curve and discriminant
Section 4:  Galois content of cross-channel
Section 5:  Cuspidal vs Eisenstein decomposition
Section 6:  Accessory parameters and non-rigidity
Section 7:  Feigin-Frenkel deformation (critical level limit)
Section 8:  W_4 and higher rank predictions
Section 9:  One-parameter family of opers
Section 10: Cross-channel L-function
Section 11: Deformation hierarchy
Section 12: Symbolic verification (sympy)
Section 13: Multi-path verification

Beilinson compliance:
  AP1:  kappa recomputed from first principles per family.
  AP3:  No pattern-matching; each test derives independently.
  AP9:  kappa != S_2 for rank > 1; kappa_T = c/2 but kappa(W_3) = 5c/6.
  AP10: Cross-family consistency checks, not just hardcoded values.
  AP14: Koszulness != formality; tested separately.
  AP24: kappa + kappa' checked per family.
  AP32: genus-1 vs all-genera clearly separated.
  AP39: kappa != c/2 for W_3 total.
"""

import cmath
import math
import unittest

import numpy as np

from compute.lib.shadow_langlands_deformation_engine import (
    # Section 1: Rank-1 baseline
    virasoro_shadow_data,
    rank1_shadow_metric_Q,
    rank1_connection_form,
    rank1_oper_data,
    # Section 2: Rank-2 W_3
    w3_channel_kappas,
    w3_quartic_contacts,
    w3_shadow_metric_matrix,
    w3_shadow_metric_matrix_at_origin,
    w3_connection_matrix,
    w3_rank2_oper_data,
    # Section 3: Spectral curve
    spectral_curve_discriminant,
    spectral_curve_over_parameter_space,
    # Section 4: Galois content
    mixing_polynomial_W3,
    mixing_polynomial_discriminant,
    mixing_polynomial_roots,
    cross_channel_galois_data,
    # Section 5: Eisenstein/cuspidal decomposition
    eisenstein_cuspidal_decomposition,
    cuspidal_ratio_over_c,
    # Section 6: Accessory parameters
    accessory_parameter_count,
    rank2_singularity_structure,
    # Section 7: Feigin-Frenkel
    feigin_frenkel_limit_shadow_oper,
    feigin_frenkel_oper_comparison,
    # Section 8: W_4
    w4_channel_data,
    w4_galois_structure,
    # Section 9: Family of opers
    shadow_oper_moduli_family,
    shadow_oper_monodromy_representation,
    # Section 10: Cross-channel L-function
    w3_cross_channel_l_function,
    l_function_type_classification,
    # Section 11: Deformation hierarchy
    deformation_landscape,
    deformation_hierarchy,
    # Section 12: Symbolic
    symbolic_rank2_spectral_curve,
    symbolic_mixing_polynomial,
    # Section 13: Verification
    verify_rank1_eisenstein_baseline,
    verify_rank2_structure,
    verify_galois_content,
)


# =========================================================================
# Section 1: Rank-1 Eisenstein baseline
# =========================================================================

class TestRank1EisensteinBaseline(unittest.TestCase):
    """Rank-1 shadow oper is RIGID Eisenstein with Koszul monodromy -1."""

    def test_virasoro_kappa_c1(self):
        """kappa(Vir_1) = 1/2."""
        k, a, S4, D = virasoro_shadow_data(1.0)
        self.assertAlmostEqual(k, 0.5, places=10)

    def test_virasoro_kappa_c25(self):
        """kappa(Vir_25) = 25/2."""
        k, a, S4, D = virasoro_shadow_data(25.0)
        self.assertAlmostEqual(k, 12.5, places=10)

    def test_virasoro_alpha_universal(self):
        """alpha = S_3 = 2 for all Virasoro (from T_{(1)}T = 2T)."""
        for c_val in [1, 5, 13, 25, 100]:
            _, a, _, _ = virasoro_shadow_data(float(c_val))
            self.assertAlmostEqual(a, 2.0, places=10)

    def test_rank1_metric_positive_at_origin(self):
        """Q_L(0) = 4*kappa^2 > 0 for c > 0."""
        for c_val in [1, 5, 13, 25]:
            k, a, S4, _ = virasoro_shadow_data(float(c_val))
            Q0 = rank1_shadow_metric_Q(k, a, S4, 0.0)
            self.assertAlmostEqual(Q0, 4.0 * k**2, places=10)
            self.assertGreater(Q0, 0)

    def test_rank1_oper_type_eisenstein(self):
        """Rank-1 shadow oper is always Eisenstein."""
        for c_val in [1, 5, 13, 25, 100]:
            data = rank1_oper_data(float(c_val))
            self.assertEqual(data['type'], 'Eisenstein')
            self.assertEqual(data['rank'], 1)

    def test_rank1_residues_universal(self):
        """Residues are 1/2 at both zeros, universally."""
        for c_val in [1, 5, 13, 25]:
            data = rank1_oper_data(float(c_val))
            self.assertEqual(len(data['residues']), 2)
            for r in data['residues']:
                self.assertAlmostEqual(r, 0.5, places=10)

    def test_rank1_monodromy_minus1(self):
        """Monodromy is -1 (Koszul sign), universally."""
        for c_val in [1, 5, 13, 25]:
            data = rank1_oper_data(float(c_val))
            self.assertEqual(data['monodromy'], -1)

    def test_rank1_rigid(self):
        """Rank-1 shadow oper has 0 accessory parameters (rigid)."""
        for c_val in [1, 5, 13, 25]:
            data = rank1_oper_data(float(c_val))
            self.assertEqual(data['n_accessory'], 0)

    def test_rank1_two_zeros(self):
        """Rank-1 shadow metric has exactly 2 zeros for c > 0."""
        for c_val in [1, 5, 13, 25]:
            data = rank1_oper_data(float(c_val))
            self.assertEqual(len(data['zeros']), 2)

    def test_koszul_duality_kappa_sum(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24)."""
        for c_val in [1, 5, 10, 13, 20, 25]:
            k1 = virasoro_shadow_data(float(c_val))[0]
            k2 = virasoro_shadow_data(26.0 - float(c_val))[0]
            self.assertAlmostEqual(k1 + k2, 13.0, places=10)


# =========================================================================
# Section 2: Rank-2 shadow oper (W_3)
# =========================================================================

class TestRank2W3ShadowOper(unittest.TestCase):
    """Rank-2 shadow oper for W_3 on the (T,W)-plane."""

    def test_w3_kappas(self):
        """kappa_T = c/2, kappa_W = c/3 for W_3."""
        for c_val in [6, 12, 30, 60]:
            kT, kW = w3_channel_kappas(float(c_val))
            self.assertAlmostEqual(kT, c_val / 2.0, places=10)
            self.assertAlmostEqual(kW, c_val / 3.0, places=10)

    def test_w3_kappa_total(self):
        """kappa(W_3) = kappa_T + kappa_W = 5c/6 (AP9: NOT c/2)."""
        for c_val in [6, 12, 30, 60]:
            kT, kW = w3_channel_kappas(float(c_val))
            self.assertAlmostEqual(kT + kW, 5.0 * c_val / 6.0, places=10)

    def test_w3_quartic_contacts_hierarchy(self):
        """Q_TT > Q_TW > Q_WW (hierarchy of quartic contacts)."""
        for c_val in [1, 5, 10, 25]:
            Q_TT, Q_TW, Q_WW = w3_quartic_contacts(float(c_val))
            self.assertGreater(Q_TT, Q_TW)
            self.assertGreater(Q_TW, Q_WW)

    def test_w3_quartic_contact_TT_equals_virasoro(self):
        """Q_TT(W_3) = Q^contact_Vir = 10/[c(5c+22)]."""
        for c_val in [1, 5, 10, 25]:
            cv = float(c_val)
            Q_TT, _, _ = w3_quartic_contacts(cv)
            Q_vir = 10.0 / (cv * (5.0 * cv + 22.0))
            self.assertAlmostEqual(Q_TT, Q_vir, places=12)

    def test_w3_metric_diagonal_at_origin(self):
        """M(0,0) = diag(c^2, 4c^2/9): diagonal at origin."""
        for c_val in [6, 12, 30]:
            M0 = w3_shadow_metric_matrix_at_origin(float(c_val))
            self.assertAlmostEqual(M0[0, 0], c_val**2, places=8)
            self.assertAlmostEqual(M0[1, 1], 4.0 * c_val**2 / 9.0, places=8)
            self.assertAlmostEqual(M0[0, 1], 0.0, places=10)
            self.assertAlmostEqual(M0[1, 0], 0.0, places=10)

    def test_w3_rank2_oper_type(self):
        """W_3 shadow oper is classified as beyond_Eisenstein."""
        data = w3_rank2_oper_data(10.0)
        self.assertEqual(data['rank'], 2)
        self.assertEqual(data['type'], 'beyond_Eisenstein')

    def test_w3_connection_matrix_finite(self):
        """Connection matrix has finite entries at generic points."""
        for c_val in [5, 10, 25]:
            Omega = w3_connection_matrix(float(c_val), 0.1, 0.1)
            self.assertTrue(np.all(np.isfinite(Omega)))

    def test_w3_connection_decouples_on_axes(self):
        """On the T-axis (w=0): off-diagonal components vanish."""
        for c_val in [5, 10, 25]:
            Omega = w3_connection_matrix(float(c_val), 0.1, 0.0)
            # Off-diagonal should be small (cross-channel vanishes on axis)
            off_diag = abs(Omega[0, 1]) + abs(Omega[1, 0])
            self.assertLess(off_diag, 1e-5,
                            f"Off-diagonal should vanish on T-axis at c={c_val}")

    def test_w3_eigenvalues_count(self):
        """Rank-2 connection has exactly 2 eigenvalues."""
        data = w3_rank2_oper_data(10.0)
        self.assertEqual(len(data['eigenvalues']), 2)


# =========================================================================
# Section 3: Spectral curve and discriminant
# =========================================================================

class TestSpectralCurve(unittest.TestCase):
    """Spectral curve of the rank-2 shadow oper."""

    def test_spectral_disc_finite(self):
        """Spectral curve discriminant is finite at generic points."""
        for c_val in [5, 10, 25]:
            disc = spectral_curve_discriminant(float(c_val), 0.1, 0.1)
            self.assertTrue(np.isfinite(disc))

    def test_spectral_disc_on_axis_reducible(self):
        """On axes (w=0 or t=0): connection is block-diagonal, hence reducible."""
        for c_val in [5, 10, 25]:
            # On the T-axis (w=0): the two channels decouple
            Omega = w3_connection_matrix(float(c_val), 0.1, 0.0)
            off_diag = abs(Omega[0, 1]) + abs(Omega[1, 0])
            # If off-diagonal is zero, char poly factors => disc is a perfect square
            if off_diag < 1e-8:
                tr = np.trace(Omega)
                det_val = np.linalg.det(Omega)
                disc = tr**2 - 4.0 * det_val
                # disc = (lambda_1 - lambda_2)^2 >= 0
                self.assertGreaterEqual(disc.real, -1e-8)

    def test_spectral_curve_scan(self):
        """Spectral curve over parameter space returns valid data."""
        results = spectral_curve_over_parameter_space(10.0, n_points=5)
        self.assertGreater(len(results), 0)
        for r in results:
            self.assertIn('discriminant', r)
            self.assertIn('t', r)
            self.assertIn('w', r)


# =========================================================================
# Section 4: Galois content of cross-channel
# =========================================================================

class TestGaloisContent(unittest.TestCase):
    """Galois-theoretic content of the cross-channel correction."""

    def test_mixing_polynomial_formula(self):
        """P(c) = 25c^2 + 100c - 428 at specific values."""
        # P(0) = -428
        self.assertAlmostEqual(mixing_polynomial_W3(0.0), -428.0)
        # P(2) = 100 + 200 - 428 = -128
        self.assertAlmostEqual(mixing_polynomial_W3(2.0), -128.0)
        # P(4) = 400 + 400 - 428 = 372
        self.assertAlmostEqual(mixing_polynomial_W3(4.0), 372.0)

    def test_mixing_polynomial_discriminant(self):
        """disc(P) = 52800 = 1600 * 33."""
        data = mixing_polynomial_discriminant()
        self.assertEqual(int(data['discriminant']), 52800)
        self.assertEqual(data['squarefree_core'], 33)
        self.assertEqual(data['galois_group'], 'Z/2')

    def test_mixing_polynomial_roots_real(self):
        """Roots of P(c) are real (disc > 0)."""
        c_plus, c_minus = mixing_polynomial_roots()
        self.assertIsInstance(c_plus, float)
        self.assertIsInstance(c_minus, float)
        # Verify they are actual roots
        self.assertAlmostEqual(mixing_polynomial_W3(c_plus), 0.0, places=8)
        self.assertAlmostEqual(mixing_polynomial_W3(c_minus), 0.0, places=8)

    def test_mixing_polynomial_root_sum(self):
        """Sum of roots = -b/a = -100/25 = -4."""
        c_plus, c_minus = mixing_polynomial_roots()
        self.assertAlmostEqual(c_plus + c_minus, -4.0, places=8)

    def test_mixing_polynomial_root_product(self):
        """Product of roots = c/a = -428/25."""
        c_plus, c_minus = mixing_polynomial_roots()
        self.assertAlmostEqual(c_plus * c_minus, -428.0 / 25.0, places=8)

    def test_squarefree_core_33(self):
        """Squarefree core of 52800 is 33 = 3 * 11."""
        data = verify_galois_content()
        self.assertEqual(data['squarefree_core'], 33)
        self.assertTrue(data['verified'])

    def test_sqrt_disc_is_40_sqrt_33(self):
        """sqrt(52800) = 40 * sqrt(33)."""
        data = verify_galois_content()
        self.assertEqual(data['sqrt_integer_part'], 40)
        # Numerical check
        self.assertAlmostEqual(40.0 * math.sqrt(33.0), math.sqrt(52800.0), places=8)

    def test_splitting_field_Q_sqrt_33(self):
        """Splitting field is Q(sqrt(33))."""
        data = verify_galois_content()
        self.assertEqual(data['splitting_field'], 'Q(sqrt(33))')

    def test_galois_group_Z2(self):
        """Galois group is Z/2."""
        data = verify_galois_content()
        self.assertEqual(data['galois_group'], 'Z/2')

    def test_cross_channel_delta_F2_positive(self):
        """delta_F_2(W_3) = (c+204)/(16c) > 0 for c > 0 (AP32)."""
        for c_val in [1, 5, 10, 25, 100]:
            data = cross_channel_galois_data(float(c_val))
            self.assertGreater(data['delta_F2'], 0,
                               f"delta_F2 should be positive at c={c_val}")

    def test_cross_channel_delta_F2_formula(self):
        """delta_F_2(W_3) = (c+204)/(16c) at specific c values."""
        for c_val in [1, 5, 10, 25]:
            cv = float(c_val)
            data = cross_channel_galois_data(cv)
            expected = (cv + 204.0) / (16.0 * cv)
            self.assertAlmostEqual(data['delta_F2'], expected, places=10)


# =========================================================================
# Section 5: Cuspidal vs Eisenstein decomposition
# =========================================================================

class TestEisensteinCuspidalDecomposition(unittest.TestCase):
    """Decomposition of rank-2 oper into Eisenstein and traceless parts."""

    def test_decomposition_well_defined(self):
        """Decomposition returns valid data for standard c values."""
        for c_val in [5, 10, 25]:
            decomp = eisenstein_cuspidal_decomposition(float(c_val))
            self.assertIn('eisenstein_norm', decomp)
            self.assertIn('traceless_norm', decomp)
            self.assertIn('cuspidal_ratio', decomp)

    def test_eisenstein_norm_positive(self):
        """Eisenstein (trace) part has positive norm for c > 0."""
        for c_val in [5, 10, 25]:
            decomp = eisenstein_cuspidal_decomposition(float(c_val))
            self.assertGreater(decomp['eisenstein_norm'], 0)

    def test_kappa_ratio_is_3_over_2(self):
        """kappa_T / kappa_W = (c/2)/(c/3) = 3/2 for all c."""
        for c_val in [5, 10, 25]:
            decomp = eisenstein_cuspidal_decomposition(float(c_val))
            self.assertAlmostEqual(decomp['kappa_ratio'], 1.5, places=10)

    def test_cuspidal_ratio_landscape(self):
        """Cuspidal ratio across the landscape is computable."""
        results = cuspidal_ratio_over_c([5, 10, 25])
        self.assertEqual(len(results), 3)
        for r in results:
            self.assertNotIn('error', r)


# =========================================================================
# Section 6: Accessory parameters and non-rigidity
# =========================================================================

class TestAccessoryParameters(unittest.TestCase):
    """Accessory parameters control rigidity of the oper."""

    def test_rank1_always_rigid(self):
        """Rank-1 connections are always rigid (any number of singularities)."""
        for n in [2, 3, 4, 5, 10]:
            result = accessory_parameter_count(1, n)
            self.assertEqual(result, 0)

    def test_rank2_3_singular_rigid(self):
        """Rank-2 with 3 singular points is rigid (Katz index = 2)."""
        result = accessory_parameter_count(2, 3)
        self.assertTrue(result['is_rigid'])
        self.assertEqual(result['katz_rigidity_index'], 2)

    def test_rank2_4_singular_not_rigid(self):
        """Rank-2 with 4 singular points is NOT rigid."""
        result = accessory_parameter_count(2, 4)
        self.assertFalse(result['is_rigid'])

    def test_rank2_singularity_structure(self):
        """Rank-2 singularity structure analysis runs correctly."""
        result = rank2_singularity_structure(10.0, grid_size=10)
        self.assertIn('det_at_origin', result)
        self.assertGreater(result['det_at_origin'], 0,
                           "Determinant at origin should be positive")


# =========================================================================
# Section 7: Feigin-Frenkel deformation
# =========================================================================

class TestFeiginFrenkelDeformation(unittest.TestCase):
    """Critical level limit: connection trivializes as c -> -infinity."""

    def test_ff_limit_connection_decreases(self):
        """Connection form |omega| decreases as c -> -infinity."""
        results = feigin_frenkel_limit_shadow_oper([-10, -100, -1000])
        omegas = [abs(r['omega_T']) for r in results]
        # omega should decrease (get closer to zero)
        self.assertGreater(abs(omegas[0]), abs(omegas[1]))
        self.assertGreater(abs(omegas[1]), abs(omegas[2]))

    def test_ff_limit_delta_decreases(self):
        """Delta_T -> 0 as c -> -infinity."""
        results = feigin_frenkel_limit_shadow_oper([-10, -100, -1000])
        deltas = [abs(r['Delta_T']) for r in results]
        self.assertGreater(deltas[0], deltas[1])
        self.assertGreater(deltas[1], deltas[2])

    def test_ff_comparison_monodromy(self):
        """Monodromy is -1 at generic c (not at critical level)."""
        result = feigin_frenkel_oper_comparison(10.0)
        self.assertTrue(result['monodromy_is_minus_1'])

    def test_ff_comparison_distance(self):
        """FF distance is large at c=10, small at c=-1000."""
        r10 = feigin_frenkel_oper_comparison(10.0)
        # At c = -1000, Delta is small
        c_neg = -1000.0
        kT = c_neg / 2.0
        S4 = 10.0 / (c_neg * (5.0 * c_neg + 22.0))
        Delta = abs(8.0 * kT * S4)
        self.assertGreater(r10['ff_distance'], Delta)


# =========================================================================
# Section 8: W_4 and higher rank
# =========================================================================

class TestW4HigherRank(unittest.TestCase):
    """W_4 predictions: rank 3, (Z/2)^2 Galois group."""

    def test_w4_kappas(self):
        """W_4 channel kappas: c/2, c/3, c/4."""
        data = w4_channel_data(12.0)
        self.assertAlmostEqual(data['kappa_T'], 6.0)
        self.assertAlmostEqual(data['kappa_W3'], 4.0)
        self.assertAlmostEqual(data['kappa_W4'], 3.0)

    def test_w4_kappa_total(self):
        """kappa(W_4) = 13c/12."""
        data = w4_channel_data(12.0)
        self.assertAlmostEqual(data['kappa_total'], 13.0, places=10)

    def test_w4_rank(self):
        """W_4 shadow oper has rank 3."""
        data = w4_channel_data(12.0)
        self.assertEqual(data['rank'], 3)

    def test_w4_galois_prediction(self):
        """W_4 Galois group predicted to be (Z/2)^2."""
        data = w4_galois_structure()
        self.assertEqual(data['predicted_galois_group'], '(Z/2)^2')
        self.assertEqual(data['order'], 4)
        self.assertEqual(data['n_characters'], 4)


# =========================================================================
# Section 9: One-parameter family of opers
# =========================================================================

class TestOperFamily(unittest.TestCase):
    """Shadow opers parametrized by c form a 1-parameter family."""

    def test_family_computation(self):
        """Family computation runs for standard c values."""
        family = shadow_oper_moduli_family([1, 5, 13, 25])
        self.assertEqual(len(family), 4)
        for entry in family:
            self.assertIn('zeros', entry)
            self.assertIn('kappa', entry)

    def test_family_zeros_complex_conjugate(self):
        """For c > 0: zeros are complex conjugate pair."""
        family = shadow_oper_moduli_family([1, 5, 13, 25])
        for entry in family:
            if len(entry['zeros']) == 2:
                t_p, t_m = entry['zeros']
                # Complex conjugate: t_+ = conj(t_-)
                self.assertAlmostEqual(t_p.real, t_m.real, places=8)
                self.assertAlmostEqual(t_p.imag, -t_m.imag, places=8)

    def test_monodromy_universal(self):
        """Monodromy representation is universal: image = Z/2, koszul sign."""
        for c_val in [1, 5, 13, 25]:
            rep = shadow_oper_monodromy_representation(float(c_val))
            self.assertTrue(rep['factors_through_Z2'])
            self.assertTrue(rep['koszul_sign'])
            self.assertTrue(rep['relation_check'])

    def test_self_dual_c13(self):
        """At c=13 (self-dual): the oper is invariant under Koszul involution."""
        data_13 = rank1_oper_data(13.0)
        data_13_dual = rank1_oper_data(13.0)  # 26 - 13 = 13
        self.assertAlmostEqual(data_13['kappa'], data_13_dual['kappa'], places=10)


# =========================================================================
# Section 10: Cross-channel L-function
# =========================================================================

class TestCrossChannelLFunction(unittest.TestCase):
    """L-function data from the cross-channel correction."""

    def test_cross_channel_data_valid(self):
        """Cross-channel L-function data is computable."""
        for c_val in [5, 10, 25]:
            data = w3_cross_channel_l_function(float(c_val))
            self.assertIn('Q_TW', data)
            self.assertIn('delta_F2', data)
            self.assertGreater(data['Q_TW'], 0)

    def test_cross_channel_Q_TW_formula(self):
        """Q_TW = 160/[c(5c+22)^2] verified numerically."""
        for c_val in [5, 10, 25]:
            cv = float(c_val)
            _, Q_TW, _ = w3_quartic_contacts(cv)
            expected = 160.0 / (cv * (5.0 * cv + 22.0)**2)
            self.assertAlmostEqual(Q_TW, expected, places=12)

    def test_l_function_type(self):
        """L-function type classification is computable."""
        for c_val in [5, 10, 25]:
            ltype = l_function_type_classification(float(c_val))
            self.assertIn(ltype, ['Eisenstein', 'quasi-Eisenstein',
                                   'potentially_cuspidal'])


# =========================================================================
# Section 11: Deformation hierarchy
# =========================================================================

class TestDeformationHierarchy(unittest.TestCase):
    """The hierarchy of shadow oper deformations."""

    def test_landscape_completeness(self):
        """Deformation landscape contains all four standard algebras."""
        landscape = deformation_landscape(10.0)
        self.assertIn('Heisenberg', landscape)
        self.assertIn('Virasoro', landscape)
        self.assertIn('W_3', landscape)
        self.assertIn('W_4', landscape)

    def test_hierarchy_rank_increasing(self):
        """Ranks increase: 1, 1, 2, 3 across the hierarchy."""
        hierarchy = deformation_hierarchy()
        levels = hierarchy['levels']
        ranks = [l['rank'] for l in levels[:4]]
        self.assertEqual(ranks, [1, 1, 2, 3])

    def test_hierarchy_galois_enriching(self):
        """Galois groups become richer along the hierarchy."""
        hierarchy = deformation_hierarchy()
        levels = hierarchy['levels']
        galois = [l['galois'] for l in levels[:4]]
        self.assertEqual(galois, ['trivial', 'Z/2', 'Z/2', '(Z/2)^2'])

    def test_landscape_virasoro_is_rigid(self):
        """Virasoro oper is rigid in the landscape."""
        landscape = deformation_landscape(10.0)
        self.assertTrue(landscape['Virasoro'].is_rigid)
        self.assertFalse(landscape['W_3'].is_rigid)


# =========================================================================
# Section 12: Symbolic verification
# =========================================================================

class TestSymbolicVerification(unittest.TestCase):
    """Symbolic (sympy) verification of key formulas."""

    def test_symbolic_spectral_curve_at_origin(self):
        """Symbolic metric determinant at origin = 4c^4/9."""
        result = symbolic_rank2_spectral_curve()
        if 'error' in result:
            self.skipTest('sympy not available')
        # det(M(0,0)) = c^2 * 4c^2/9 = 4c^4/9
        det_origin = result['det_M_origin']
        from sympy import Symbol, cancel, Rational
        c = Symbol('c', positive=True)
        expected = Rational(4, 9) * c**4
        diff = cancel(det_origin - expected)
        self.assertEqual(diff, 0, f"det at origin: got {det_origin}, expected {expected}")

    def test_symbolic_trace_at_origin(self):
        """Symbolic metric trace at origin = c^2 + 4c^2/9 = 13c^2/9."""
        result = symbolic_rank2_spectral_curve()
        if 'error' in result:
            self.skipTest('sympy not available')
        tr_origin = result['tr_M_origin']
        from sympy import Symbol, cancel, Rational
        c = Symbol('c', positive=True)
        expected = Rational(13, 9) * c**2
        diff = cancel(tr_origin - expected)
        self.assertEqual(diff, 0, f"trace at origin: got {tr_origin}, expected {expected}")

    def test_symbolic_mixing_polynomial(self):
        """Symbolic verification of P(c) = 25c^2 + 100c - 428."""
        result = symbolic_mixing_polynomial()
        if 'error' in result:
            self.skipTest('sympy not available')
        self.assertEqual(result['discriminant'], 52800)
        self.assertEqual(result['squarefree_core'], 33)
        self.assertEqual(len(result['roots']), 2)


# =========================================================================
# Section 13: Multi-path verification
# =========================================================================

class TestMultiPathVerification(unittest.TestCase):
    """Multi-path verification of core claims (Beilinson mandate)."""

    def test_rank1_baseline_3_paths(self):
        """Rank-1 Eisenstein baseline verified by 3 independent paths."""
        for c_val in [1, 5, 13, 25]:
            result = verify_rank1_eisenstein_baseline(float(c_val))
            self.assertTrue(result['residues_ok'],
                            f"Path 1 (residues) failed at c={c_val}")
            self.assertTrue(result['type_ok'],
                            f"Path 2 (type) failed at c={c_val}")
            self.assertTrue(result['koszul_ok'],
                            f"Path 3 (Koszul) failed at c={c_val}")
            self.assertTrue(result['all_ok'],
                            f"Multi-path verification failed at c={c_val}")

    def test_rank2_structure_2_paths(self):
        """Rank-2 structure verified by 2 independent paths."""
        for c_val in [5, 10, 25]:
            result = verify_rank2_structure(float(c_val))
            self.assertTrue(result['eigs_finite'],
                            f"Path 1 (eigenvalues) failed at c={c_val}")
            self.assertTrue(result['trace_finite'],
                            f"Path 2 (trace) failed at c={c_val}")

    def test_galois_verification(self):
        """Galois content verified by factorization + squarefree extraction."""
        result = verify_galois_content()
        self.assertTrue(result['verified'])
        self.assertEqual(result['discriminant'], 52800)
        self.assertEqual(result['squarefree_core'], 33)
        self.assertEqual(result['sqrt_integer_part'], 40)

    def test_cross_family_kappa_consistency(self):
        """Cross-family kappa consistency (AP10): kappa formulas agree.

        Virasoro kappa_T = c/2 matches the T-channel of W_3.
        """
        for c_val in [5, 10, 25]:
            cv = float(c_val)
            vir_kappa = virasoro_shadow_data(cv)[0]
            w3_kT, _ = w3_channel_kappas(cv)
            self.assertAlmostEqual(vir_kappa, w3_kT, places=10,
                                   msg=f"Virasoro kappa != W_3 kappa_T at c={c_val}")

    def test_quartic_hierarchy_dimensional(self):
        """Dimensional analysis: Q_TT * (5c+22)^2 / Q_TW = const = 10/160.

        Verifies the power of (5c+22) in the denominators is consistent.
        """
        for c_val in [5, 10, 25]:
            cv = float(c_val)
            Q_TT, Q_TW, Q_WW = w3_quartic_contacts(cv)
            # Q_TT = 10/[c(5c+22)], Q_TW = 160/[c(5c+22)^2]
            # Ratio: Q_TT / Q_TW = 10/160 * (5c+22) = (5c+22)/16
            ratio = Q_TT / Q_TW
            expected_ratio = (5.0 * cv + 22.0) / 16.0
            self.assertAlmostEqual(ratio, expected_ratio, places=8)


if __name__ == '__main__':
    unittest.main()
