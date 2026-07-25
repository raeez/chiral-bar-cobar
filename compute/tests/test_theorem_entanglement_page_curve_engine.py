r"""Tests for the entanglement Page curve engine.

Verification of:
  (a) Renyi entropy universality: S_n = kappa * f_n * log(L/eps)
  (b) formal spectrum and Page-branch candidates
  (c) exact Theorem A / certificate-bound Theorem B status
  (d) conditional entropy, QES/JLMS, Hilbert-QEC, and Page bridges
  (e) scalar free-energy asymmetry at genus g

Each numerical result is verified by at least 3 independent paths
(Multi-Path Verification Mandate).
"""

import math
import unittest
from fractions import Fraction

from sympy import Matrix, Rational, simplify, Abs, pi

from compute.lib.qec_koszul_code_engine import (
    quadratic_comparison_cone,
    theorem_b_certificate_from_cone,
)

from compute.lib.theorem_entanglement_page_curve_engine import (
    # Section 1: Renyi universality
    renyi_universal_function,
    renyi_min_entropy_coefficient,
    verify_renyi_universality,
    renyi_von_neumann_limit,
    renyi_spectrum_by_class,
    # Section 2: Entanglement spectrum
    entanglement_spectrum_thermal,
    entanglement_spectrum_class_m,
    spectral_complexity_by_class,
    # Section 3: Page curve
    page_time_classical,
    page_time_quantum_correction,
    page_transition_width_by_class,
    page_curve_full,
    page_entropy_at_transition,
    # Section 4: QEC rate
    qec_verification_chain_before_hr,
    qec_verification_chain_after_hr,
    qec_rate_by_family_simplified,
    # Section 5: Modular entanglement
    modular_entanglement_entropy,
    modular_entanglement_heisenberg,
    modular_entanglement_virasoro,
    modular_entanglement_affine_sl2,
    modular_entanglement_genus_tower,
    verify_modular_entanglement_heisenberg_g1,
    # Section 6: Cross-checks
    verify_renyi_factorization_all_families,
    verify_page_time_independence_of_c,
    verify_modular_entanglement_self_dual_vanishing,
    verify_modular_entanglement_km_formula,
    full_page_curve_analysis,
    entanglement_landscape_survey,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_affine,
    kappa_heisenberg,
    kappa_betagamma,
    kappa_wN,
    von_neumann_entropy_scalar,
    renyi_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    shadow_depth_class,
)


def _quadratic_certificate(
    algebra_id,
    comparison_entry=1,
    h_cl_verified=True,
    strong_convergence_verified=True,
):
    """Build an exact one-term Theorem B certificate."""
    cone = quadratic_comparison_cone(
        source_dimensions={0: 1},
        target_dimensions={0: 1},
        source_differentials={},
        target_differentials={},
        comparison_maps={0: Matrix([[comparison_entry]])},
    )
    return theorem_b_certificate_from_cone(
        cone,
        algebra_id=algebra_id,
        presentation='A = T(V)/(R), one-term finite model',
        h_cl_verified=h_cl_verified,
        strong_convergence_verified=strong_convergence_verified,
    )


# =========================================================================
#  1. RENYI ENTROPY UNIVERSALITY
# =========================================================================

class TestRenyiUniversality(unittest.TestCase):
    """Tests for the universal Renyi function f_n = (1/3)(1+1/n)."""

    def test_f_1_von_neumann_limit(self):
        """f_1 = 2/3 (von Neumann limit)."""
        self.assertEqual(renyi_universal_function(1), Rational(2, 3))

    def test_f_2(self):
        """f_2 = 1/2."""
        self.assertEqual(renyi_universal_function(2), Rational(1, 2))

    def test_f_3(self):
        """f_3 = 4/9."""
        self.assertEqual(renyi_universal_function(3), Rational(4, 9))

    def test_f_10(self):
        """f_10 = 11/30."""
        self.assertEqual(renyi_universal_function(10), Rational(11, 30))

    def test_min_entropy_coefficient(self):
        """lim_{n->inf} f_n = 1/3."""
        self.assertEqual(renyi_min_entropy_coefficient(), Rational(1, 3))

    def test_f_n_decreasing(self):
        """f_n is strictly decreasing in n."""
        for n in range(1, 20):
            self.assertGreater(renyi_universal_function(n),
                               renyi_universal_function(n + 1))

    def test_renyi_factorization_heisenberg(self):
        """S_n(H_1) = kappa * f_n for Heisenberg at kappa=1.

        Multi-path: Path 1 (twist), Path 2 (direct), Path 3 (factored).
        """
        data = verify_renyi_universality(Rational(1), 2)
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_n'], Rational(1, 2))
        self.assertIsNone(data['physical_renyi_entropy'])
        self.assertEqual(
            data['physical_renyi_status'],
            'CONDITIONAL_ON_REPLICA_STATE_AND_ANALYTIC_CONTINUATION',
        )

    def test_renyi_identity_handles_n1_limiting_case(self):
        data = verify_renyi_universality(Rational(1), 1)
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_n'], Rational(2, 3))

    def test_renyi_factorization_virasoro_c13(self):
        """S_n(Vir_13) = (13/2) * f_n at n=3.

        Multi-path verification for the self-dual point.
        """
        data = verify_renyi_universality(Rational(13, 2), 3)
        self.assertTrue(data['paths_agree'])
        expected = Rational(13, 2) * Rational(4, 9)
        self.assertEqual(data['S_n'], expected)

    def test_renyi_factorization_all_families_n2(self):
        """S_2 = kappa * f_2 for all standard families.

        Cross-family consistency check (AP10).
        """
        checks = verify_renyi_factorization_all_families(2)
        self.assertTrue(all(checks.values()),
                        f"Failed families: {[k for k, v in checks.items() if not v]}")

    def test_renyi_factorization_all_families_n5(self):
        """S_5 = kappa * f_5 for all standard families."""
        checks = verify_renyi_factorization_all_families(5)
        self.assertTrue(all(checks.values()))

    def test_von_neumann_limit_heisenberg(self):
        """lim_{n->1} S_n = S_EE = 2/3 for Heisenberg at kappa=1.

        Multi-path: algebraic limit, replica trick, direct formula.
        """
        data = renyi_von_neumann_limit(Rational(1))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_EE'], Rational(2, 3))
        self.assertIsNone(data['physical_von_neumann_entropy'])

    def test_von_neumann_limit_virasoro_c13(self):
        """lim_{n->1} S_n = 13/3 for Virasoro at c=13."""
        data = renyi_von_neumann_limit(Rational(13, 2))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_EE'], Rational(13, 3))

    def test_renyi_spectrum_class_g_exact(self):
        """Class G has the scalar formula and scalar-only arity metadata."""
        data = renyi_spectrum_by_class('heisenberg')
        self.assertTrue(data['exact_at_scalar'])
        self.assertTrue(data['scalar_formula_verified'])
        self.assertEqual(data['shadow_class'], 'G')
        self.assertEqual(data['supported_higher_arities'], [])
        self.assertIsNone(data['n_corrections'])
        self.assertIsNone(data['physical_renyi_spectrum'])

    def test_renyi_spectrum_class_m_has_unbounded_arity_metadata(self):
        data = renyi_spectrum_by_class('virasoro')
        self.assertTrue(data['exact_at_scalar'])
        self.assertEqual(data['shadow_class'], 'M')
        self.assertEqual(data['supported_higher_arities'], list(range(3, 11)))
        self.assertIsNone(data['correction_arities'])


# =========================================================================
#  2. ENTANGLEMENT SPECTRUM
# =========================================================================

class TestEntanglementSpectrum(unittest.TestCase):
    """Tests for formal spectrum candidates and bridge status."""

    def test_thermal_spectrum_class_g(self):
        """The equally spaced candidate is distinct from a physical spectrum."""
        spec = entanglement_spectrum_thermal(Rational(1), 5)
        self.assertIsNone(spec['is_thermal'])
        self.assertTrue(spec['formal_spectrum_candidate'])
        self.assertIsNone(spec['physical_spectrum'])
        self.assertEqual(spec['shadow_class'], 'G')
        self.assertEqual(spec['n_levels'], 5)

    def test_thermal_spacing(self):
        """Thermal spectrum has unit spacing in natural units."""
        spec = entanglement_spectrum_thermal(Rational(1), 10)
        self.assertEqual(spec['spacing'], Rational(1))

    def test_class_m_formal_bound_virasoro(self):
        spec = entanglement_spectrum_class_m(Rational(26), 5)
        self.assertEqual(spec['shadow_class'], 'M')
        self.assertIsNone(spec['convergent'])
        self.assertTrue(spec['formal_geometric_bound_converges'])
        self.assertIsNone(spec['physical_spectrum'])
        self.assertLess(spec['rho'], 1.0)

    def test_class_m_self_dual(self):
        """Class M at c=13 is self-dual."""
        spec = entanglement_spectrum_class_m(Rational(13), 3)
        self.assertTrue(spec['self_dual'])

    def test_spectral_complexity_classification(self):
        """Four shadow classes retain their arity counts."""
        data = spectral_complexity_by_class()
        self.assertEqual(data['G']['formal_higher_arity_slots'], 0)
        self.assertEqual(data['L']['formal_higher_arity_slots'], 1)
        self.assertEqual(data['C']['formal_higher_arity_slots'], 2)
        self.assertEqual(data['M']['formal_higher_arity_slots'], -1)
        for cls in ['G', 'L', 'C', 'M']:
            self.assertIsNone(data[cls]['n_corrections'])
            self.assertIsNone(data[cls]['spectrum'])
            self.assertIsNone(data[cls]['complexity'])


# =========================================================================
#  3. PAGE CURVE AND TRANSITION
# =========================================================================

class TestPageCurve(unittest.TestCase):
    """Tests for formal branch candidates and the Page bridge."""

    def test_page_time_classical(self):
        """The chosen linear branches cross at 3*S_BH/13."""
        self.assertEqual(page_time_classical(Rational(100)), Rational(300, 13))
        self.assertEqual(page_time_classical(Rational(130)), Rational(30))
        self.assertEqual(page_time_classical(Rational(13)), Rational(3))

    def test_page_time_independence_of_c(self):
        """The formal branch crossing is independent of c.

        Multi-path: verify at c=1, c=7/10, c=13, c=26, c=50.
        """
        checks = verify_page_time_independence_of_c()
        self.assertTrue(all(checks.values()),
                        f"Failed: {[k for k, v in checks.items() if not v]}")

    def test_formal_transition_value_self_dual(self):
        """At c=13 the formal branches meet at S_BH/2.

        Multi-path: radiation branch, island branch, direct formula.
        """
        data = page_entropy_at_transition(Rational(13), Rational(100))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['formal_transition_value'], Rational(50))
        self.assertEqual(data['formal_fraction'], Rational(1, 2))
        self.assertIsNone(data['S_page'])
        self.assertIsNone(data['page_time'])

    def test_formal_transition_value_c26(self):
        data = page_entropy_at_transition(Rational(26), Rational(100))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['formal_transition_value'], Rational(100))
        self.assertEqual(data['formal_fraction'], Rational(1))

    def test_formal_transition_fraction_monotone(self):
        fractions = []
        for c in [Rational(1), Rational(6), Rational(13), Rational(20), Rational(26)]:
            data = page_entropy_at_transition(c, Rational(100))
            fractions.append(data['formal_fraction'])
        for i in range(len(fractions) - 1):
            self.assertLess(fractions[i], fractions[i + 1])

    def test_page_quantum_correction_self_dual(self):
        """The formal asymmetry coefficient vanishes at c=13."""
        data = page_time_quantum_correction(Rational(13))
        self.assertEqual(data['formal_delta_t_coefficient'], 0)
        self.assertIsNone(data['delta_t_coefficient'])
        self.assertIsNone(data['physical_page_time_correction'])
        self.assertTrue(data['self_dual'])

    def test_page_quantum_correction_convergence(self):
        """The A-hat sum converges: partial sum matches (1/2)/sin(1/2)-1."""
        data = page_time_quantum_correction(Rational(26), max_genus=20)
        self.assertTrue(data['sum_converged'])

    def test_page_width_class_g_is_bridge_pending(self):
        data = page_transition_width_by_class('heisenberg')
        self.assertIsNone(data['quantum_smearing'])
        self.assertEqual(data['formal_arity_terms'], 0)
        self.assertEqual(data['shadow_class'], 'G')

    def test_page_width_class_m_formal_bound(self):
        data = page_transition_width_by_class('virasoro', Rational(26), Rational(100))
        self.assertIsNone(data['quantum_smearing'])
        self.assertGreater(data['formal_geometric_bound'], 0)
        self.assertTrue(data['formal_geometric_bound_converges'])

    def test_formal_page_branches_self_dual(self):
        data = page_curve_full(Rational(13), Rational(100), 5)
        self.assertTrue(data['self_dual'])
        self.assertEqual(data['formal_crossing_time'], Rational(300, 13))
        self.assertIsNone(data['page_time'])
        self.assertIsNone(data['s_page'])
        self.assertEqual(len(data['formal_scalar_envelope']), 5)

    def test_page_curve_genus_corrections(self):
        """Genus corrections use correct Faber-Pandharipande coefficients.

        Cross-check against independently computed lambda_g^FP.
        """
        data = page_curve_full(Rational(26), Rational(100), 5, max_genus=3)
        kappa = kappa_virasoro(Rational(26))
        for g in [1, 2, 3]:
            expected_fg = kappa * faber_pandharipande(g)
            self.assertEqual(data['genus_corrections'][g]['F_g'], expected_fg)

    def test_corrected_crossing_solves_implemented_branches(self):
        c_val = Rational(26)
        S_BH = Rational(100)
        data = page_curve_full(c_val, S_BH, 5, max_genus=4)
        t_cross = data['formal_crossing_time']
        s_rad = c_val * t_cross / 6 + data['F_total']
        s_island = (
            S_BH - (26 - c_val) * t_cross / 6 + data['F_total_dual']
        )
        self.assertEqual(simplify(s_rad - s_island), 0)
        self.assertEqual(
            t_cross,
            data['formal_classical_crossing_time']
            + data['formal_genus_crossing_shift'],
        )


# =========================================================================
#  4. QEC RATE WITH HOLSTEIN-RIVERA
# =========================================================================

class TestQECRate(unittest.TestCase):
    """Tests for typed algebraic and physical QEC status."""

    def test_before_hr_chain_length(self):
        """Before HR: 4-step verification chain."""
        chain = qec_verification_chain_before_hr()
        self.assertEqual(chain['n_steps'], 4)
        self.assertIsNone(chain['rate'])
        self.assertEqual(chain['lagrangian_fraction_candidate'], Rational(1, 2))

    def test_after_hr_chain_length(self):
        """The proposed post-HR lane remains source-qualified."""
        chain = qec_verification_chain_after_hr()
        self.assertEqual(chain['n_steps'], 2)
        self.assertIsNone(chain['hypothesis_removed'])
        self.assertEqual(
            chain['claimed_hypothesis_removed'], 'P3 (properness/perfectness)'
        )
        self.assertEqual(
            chain['lane_status'],
            'REQUIRES_THEOREM_C_AND_HOLSTEIN_RIVERA_PACKAGE',
        )

    def test_family_labels_leave_theorem_b_and_rate_pending(self):
        for family in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            data = qec_rate_by_family_simplified(family)
            self.assertTrue(data['universal_reconstruction'])
            self.assertIsNone(data['is_koszul'])
            self.assertIsNone(data['exact_quadratic_recovery'])
            self.assertEqual(data['quadratic_recovery_status'], 'UNVERIFIED')
            self.assertIsNone(data['rate'])
            self.assertIsNone(data['distance'])
            self.assertIsNone(data['lagrangian_fraction'])

    def test_qec_arity_floor_is_separate_from_distance(self):
        for family in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            data = qec_rate_by_family_simplified(family)
            self.assertEqual(data['arity_floor'], 2)
            self.assertIsNone(data['distance'])
            self.assertIsNone(data['physical_distance'])
            self.assertEqual(
                data['physical_distance_status'],
                'CONDITIONAL_ON_HILBERT_ERROR_ALGEBRA_AND_RECOVERY_MAPS',
            )

    def test_higher_arity_slots_by_class(self):
        self.assertEqual(qec_rate_by_family_simplified('heisenberg')['formal_higher_arity_slots'], 0)
        self.assertEqual(qec_rate_by_family_simplified('affine')['formal_higher_arity_slots'], 1)
        self.assertEqual(qec_rate_by_family_simplified('betagamma')['formal_higher_arity_slots'], 2)
        self.assertEqual(qec_rate_by_family_simplified('virasoro')['formal_higher_arity_slots'], -1)
        self.assertIsNone(qec_rate_by_family_simplified('virasoro')['channels'])

    def test_exact_cone_certificate_transitions_theorem_b(self):
        algebra_id = 'heisenberg:k=1'
        data = qec_rate_by_family_simplified(
            'heisenberg',
            k=1,
            algebra_id=algebra_id,
            quadratic_certificate=_quadratic_certificate(algebra_id),
        )
        self.assertTrue(data['universal_reconstruction'])
        self.assertTrue(data['is_koszul'])
        self.assertTrue(data['exact_quadratic_recovery'])
        self.assertEqual(data['quadratic_recovery_status'], 'CERTIFIED')
        self.assertIsNone(data['rate'])

    def test_obstructed_cone_transitions_theorem_b(self):
        algebra_id = 'affine:sl2:k=1'
        data = qec_rate_by_family_simplified(
            'affine',
            algebra_id=algebra_id,
            quadratic_certificate=_quadratic_certificate(
                algebra_id, comparison_entry=0
            ),
        )
        self.assertFalse(data['is_koszul'])
        self.assertFalse(data['exact_quadratic_recovery'])
        self.assertEqual(
            data['quadratic_recovery_status'], 'OBSTRUCTED_IN_FINITE_MODEL'
        )

    def test_incomplete_certificate_keeps_theorem_b_pending(self):
        algebra_id = 'betagamma:lambda=1'
        data = qec_rate_by_family_simplified(
            'betagamma',
            algebra_id=algebra_id,
            quadratic_certificate=_quadratic_certificate(
                algebra_id, strong_convergence_verified=False
            ),
        )
        self.assertIsNone(data['is_koszul'])
        self.assertEqual(data['quadratic_recovery_status'], 'INCOMPLETE_PACKAGE')

    def test_mismatched_certificate_is_rejected(self):
        certificate = _quadratic_certificate('virasoro:c=13')
        with self.assertRaisesRegex(ValueError, 'algebra_id'):
            qec_rate_by_family_simplified(
                'virasoro',
                c=26,
                algebra_id='virasoro:c=26',
                quadratic_certificate=certificate,
            )

    def test_theorem_c_hr_package_transitions_lagrangian_fraction_only(self):
        data = qec_rate_by_family_simplified(
            'heisenberg', theorem_c_hr_package_verified=True
        )
        self.assertEqual(data['lagrangian_fraction'], Rational(1, 2))
        self.assertIsNone(data['rate'])


# =========================================================================
#  5. MODULAR ENTANGLEMENT ENTROPY
# =========================================================================

class TestModularEntanglement(unittest.TestCase):
    """Tests for the scalar free-energy-asymmetry coefficients."""

    def test_heisenberg_g1(self):
        """S^mod_1(H_1) = 1/12.

        Multi-path: free energy, formula, complementarity (3 paths).
        """
        checks = verify_modular_entanglement_heisenberg_g1()
        self.assertTrue(all(checks.values()))
        self.assertEqual(modular_entanglement_heisenberg(Rational(1), 1),
                         Rational(1, 12))

    def test_heisenberg_g2(self):
        """S^mod_2(H_1) = 7/2880."""
        self.assertEqual(modular_entanglement_heisenberg(Rational(1), 2),
                         Rational(7, 2880))

    def test_heisenberg_k2_g1(self):
        """S^mod_1(H_2) = 2*2*1/24 = 1/6."""
        self.assertEqual(modular_entanglement_heisenberg(Rational(2), 1),
                         Rational(1, 6))

    def test_virasoro_self_dual_vanishing(self):
        """S^mod_g(Vir_13) = 0 for all g (bar-Verdier entanglement vanishes).

        At c=13: kappa = kappa!, so F_g = F_g! and S^mod = 0.
        """
        checks = verify_modular_entanglement_self_dual_vanishing()
        self.assertTrue(all(checks.values()),
                        f"Failed genera: {[k for k, v in checks.items() if not v]}")

    def test_virasoro_c26_g1(self):
        """S^mod_1(Vir_26) = 13/24.

        kappa - kappa! = 13 - 0 = 13, lambda_1 = 1/24.
        """
        self.assertEqual(modular_entanglement_virasoro(Rational(26), 1),
                         Rational(13, 24))

    def test_virasoro_c1_g1(self):
        """S^mod_1(Vir_1) = |1-25|/2 * 1/24 = 12 * 1/24 = 1/2.

        kappa(Vir_1) = 1/2, kappa(Vir_25) = 25/2.
        |1/2 - 25/2| = 12. S^mod_1 = 12*(1/24) = 1/2.
        """
        self.assertEqual(modular_entanglement_virasoro(Rational(1), 1),
                         Rational(1, 2))

    def test_affine_sl2_k1_g1(self):
        """S^mod_1(V_1(sl_2)) = 3/16.

        kappa = 9/4, kappa! = -9/4. |kappa-kappa!| = 9/2.
        S^mod_1 = (9/2)*(1/24) = 9/48 = 3/16.
        """
        self.assertEqual(modular_entanglement_affine_sl2(Rational(1), 1),
                         Rational(3, 16))

    def test_km_complementarity_formula(self):
        """S^mod_g = 2*|kappa|*lambda_g for KM families (kappa+kappa!=0).

        Cross-family: Heisenberg k=1,2,5 at genus 1,2,3.
        """
        checks = verify_modular_entanglement_km_formula()
        self.assertTrue(all(checks.values()))

    def test_modular_entanglement_antisymmetry(self):
        """S^mod_g(Vir_c) = S^mod_g(Vir_{26-c}) (complementarity symmetry).

        The bar-Verdier entanglement depends only on |c-13|.
        """
        for c_val in [Rational(1), Rational(7, 10), Rational(6), Rational(20)]:
            for g in [1, 2]:
                s1 = modular_entanglement_virasoro(c_val, g)
                s2 = modular_entanglement_virasoro(26 - c_val, g)
                self.assertEqual(s1, s2,
                                 f"Antisymmetry failed at c={c_val}, g={g}")

    def test_genus_tower_decay(self):
        """Modular entanglement decays with genus (Bernoulli decay)."""
        data = modular_entanglement_genus_tower(Rational(1), Rational(-1))
        for g in range(1, 4):
            self.assertGreater(data['S_mod'][g], data['S_mod'][g + 1])

    def test_genus_tower_convergence(self):
        """The scalar asymmetry series converges to its closed form.

        sum S^mod_g = |kappa-kappa!| * ((1/2)/sin(1/2) - 1).
        """
        data = modular_entanglement_genus_tower(Rational(1), Rational(-1), max_genus=20)
        self.assertAlmostEqual(float(data['total']),
                               data['total_closed_form'],
                               places=8)
        self.assertIsNone(data['physical_modular_entanglement'])
        self.assertEqual(
            data['physical_modular_status'],
            'CONDITIONAL_ON_TOMITA_JLMS_OPERATOR_ALGEBRA_PACKAGE',
        )

    def test_genus_tower_self_dual_total_zero(self):
        """Total modular entanglement at c=13 is zero."""
        data = modular_entanglement_genus_tower(
            Rational(13, 2), Rational(13, 2), max_genus=5)
        self.assertEqual(data['total'], 0)


# =========================================================================
#  6. CROSS-CHECKS AND LANDSCAPE SURVEY
# =========================================================================

class TestCrossChecks(unittest.TestCase):
    """Cross-family and cross-quantity consistency checks."""

    def test_full_analysis_self_dual(self):
        """Full analysis separates scalar candidates from physical status."""
        data = full_page_curve_analysis(Rational(13), Rational(100))
        self.assertTrue(data['self_dual'])
        self.assertIsNone(data['qec_rate'])
        self.assertIsNone(data['page_time'])
        self.assertEqual(data['formal_crossing_time'], Rational(300, 13))
        self.assertTrue(data['universal_reconstruction'])
        self.assertIsNone(data['is_koszul'])
        self.assertEqual(data['quadratic_recovery_status'], 'UNVERIFIED')
        self.assertEqual(data['S_mod_1'], 0)
        self.assertEqual(data['formal_transition_fraction'], Rational(1, 2))
        self.assertIsNone(data['page_fraction'])

    def test_full_analysis_critical(self):
        """Full analysis at c=26: critical string, S^mod_1 = 13/24."""
        data = full_page_curve_analysis(Rational(26), Rational(100))
        self.assertFalse(data['self_dual'])
        self.assertEqual(data['S_mod_1'], Rational(13, 24))
        self.assertEqual(data['formal_transition_fraction'], Rational(1))

    def test_full_analysis_certificate_transitions_only_theorem_b(self):
        algebra_id = 'virasoro:c=13'
        data = full_page_curve_analysis(
            Rational(13),
            Rational(100),
            algebra_id=algebra_id,
            quadratic_certificate=_quadratic_certificate(algebra_id),
        )
        self.assertTrue(data['exact_quadratic_recovery'])
        self.assertEqual(data['quadratic_recovery_status'], 'CERTIFIED')
        self.assertIsNone(data['qec_rate'])
        self.assertIsNone(data['page_time'])

    def test_landscape_survey_completeness(self):
        """Survey covers at least 6 families."""
        survey = entanglement_landscape_survey()
        self.assertGreaterEqual(len(survey), 6)

    def test_landscape_survey_keeps_theorem_b_and_rate_pending(self):
        survey = entanglement_landscape_survey()
        for row in survey:
            self.assertTrue(row['universal_reconstruction'])
            self.assertIsNone(row['is_koszul'])
            self.assertIsNone(row['exact_quadratic_recovery'])
            self.assertEqual(row['quadratic_recovery_status'], 'UNVERIFIED')
            self.assertIsNone(row['qec_rate'])
            self.assertIsNone(row['S_EE_scalar'])

    def test_landscape_certificate_is_bound_to_one_algebra(self):
        algebra_id = 'heisenberg:k=1'
        survey = entanglement_landscape_survey(
            {algebra_id: _quadratic_certificate(algebra_id)}
        )
        certified = [
            row for row in survey
            if row['quadratic_recovery_status'] == 'CERTIFIED'
        ]
        self.assertEqual([row['algebra_id'] for row in certified], [algebra_id])
        self.assertTrue(certified[0]['exact_quadratic_recovery'])
        self.assertIsNone(certified[0]['qec_rate'])

    def test_landscape_rejects_mismatched_certificate(self):
        certificate = _quadratic_certificate('heisenberg:k=2')
        with self.assertRaisesRegex(ValueError, 'algebra_id'):
            entanglement_landscape_survey({'heisenberg:k=1': certificate})

    def test_landscape_survey_universal_f2(self):
        """All families have f_2 = 1/2 (Renyi universality)."""
        survey = entanglement_landscape_survey()
        for row in survey:
            self.assertEqual(row['f_2'], Rational(1, 2))

    def test_renyi_and_von_neumann_consistency(self):
        """S_1 from Renyi matches von Neumann for all families.

        This is the n=1 consistency check: the two formulas must agree.
        """
        for kap in [Rational(1), Rational(13, 2), Rational(9, 4)]:
            s_renyi_1 = kap * renyi_universal_function(1)
            s_vn = von_neumann_entropy_scalar(kap, 1)
            self.assertEqual(s_renyi_1, s_vn,
                             f"Renyi-VN mismatch at kappa={kap}")


if __name__ == '__main__':
    unittest.main()
