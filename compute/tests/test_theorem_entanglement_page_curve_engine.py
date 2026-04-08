r"""Tests for the entanglement Page curve engine.

Multi-path verification of:
  (a) Renyi entropy universality: S_n = kappa * f_n * log(L/eps)
  (b) Entanglement spectrum by shadow class (G/L/C/M)
  (c) Page curve and transition: t_P = 3*S_BH/13, transition width
  (d) QEC rate simplification after Holstein-Rivera
  (e) Modular entanglement entropy S^mod_g at genus g

Each numerical result is verified by at least 3 independent paths
(Multi-Path Verification Mandate).
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, simplify, Abs, pi

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

    def test_von_neumann_limit_virasoro_c13(self):
        """lim_{n->1} S_n = 13/3 for Virasoro at c=13."""
        data = renyi_von_neumann_limit(Rational(13, 2))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_EE'], Rational(13, 3))

    def test_renyi_spectrum_class_g_exact(self):
        """Class G has exact scalar Renyi (no corrections)."""
        data = renyi_spectrum_by_class('heisenberg')
        self.assertTrue(data['exact_at_scalar'])
        self.assertEqual(data['shadow_class'], 'G')
        self.assertEqual(data['n_corrections'], 0)

    def test_renyi_spectrum_class_m_not_exact(self):
        """Class M has infinite correction tower."""
        data = renyi_spectrum_by_class('virasoro')
        self.assertFalse(data['exact_at_scalar'])
        self.assertEqual(data['shadow_class'], 'M')


# =========================================================================
#  2. ENTANGLEMENT SPECTRUM
# =========================================================================

class TestEntanglementSpectrum(unittest.TestCase):
    """Tests for entanglement spectrum by shadow class."""

    def test_thermal_spectrum_class_g(self):
        """Class G spectrum is exactly thermal."""
        spec = entanglement_spectrum_thermal(Rational(1), 5)
        self.assertTrue(spec['is_thermal'])
        self.assertEqual(spec['shadow_class'], 'G')
        self.assertEqual(spec['n_levels'], 5)

    def test_thermal_spacing(self):
        """Thermal spectrum has unit spacing in natural units."""
        spec = entanglement_spectrum_thermal(Rational(1), 10)
        self.assertEqual(spec['spacing'], Rational(1))

    def test_class_m_spectrum_virasoro(self):
        """Class M spectrum at c=26 is convergent (rho < 1)."""
        spec = entanglement_spectrum_class_m(Rational(26), 5)
        self.assertEqual(spec['shadow_class'], 'M')
        self.assertTrue(spec['convergent'])
        self.assertLess(spec['rho'], 1.0)

    def test_class_m_self_dual(self):
        """Class M at c=13 is self-dual."""
        spec = entanglement_spectrum_class_m(Rational(13), 3)
        self.assertTrue(spec['self_dual'])

    def test_spectral_complexity_classification(self):
        """Four shadow classes have correct correction counts."""
        data = spectral_complexity_by_class()
        self.assertEqual(data['G']['n_corrections'], 0)
        self.assertEqual(data['L']['n_corrections'], 1)
        self.assertEqual(data['C']['n_corrections'], 2)
        self.assertEqual(data['M']['n_corrections'], -1)  # infinite


# =========================================================================
#  3. PAGE CURVE AND TRANSITION
# =========================================================================

class TestPageCurve(unittest.TestCase):
    """Tests for the Page curve and transition."""

    def test_page_time_classical(self):
        """t_P = 3*S_BH/13."""
        self.assertEqual(page_time_classical(Rational(100)), Rational(300, 13))
        self.assertEqual(page_time_classical(Rational(130)), Rational(30))
        self.assertEqual(page_time_classical(Rational(13)), Rational(3))

    def test_page_time_independence_of_c(self):
        """Page time is independent of c.

        Multi-path: verify at c=1, c=7/10, c=13, c=26, c=50.
        """
        checks = verify_page_time_independence_of_c()
        self.assertTrue(all(checks.values()),
                        f"Failed: {[k for k, v in checks.items() if not v]}")

    def test_page_entropy_at_transition_self_dual(self):
        """At c=13: S_Page = S_BH/2 (exactly half).

        Multi-path: radiation branch, island branch, direct formula.
        """
        data = page_entropy_at_transition(Rational(13), Rational(100))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_page'], Rational(50))
        self.assertEqual(data['fraction'], Rational(1, 2))

    def test_page_entropy_at_transition_critical(self):
        """At c=26: S_Page = S_BH (full evaporation at Page time)."""
        data = page_entropy_at_transition(Rational(26), Rational(100))
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['S_page'], Rational(100))
        self.assertEqual(data['fraction'], Rational(1))

    def test_page_entropy_fraction_monotone(self):
        """S_Page/S_BH = c/26 is monotone increasing in c."""
        fractions = []
        for c in [Rational(1), Rational(6), Rational(13), Rational(20), Rational(26)]:
            data = page_entropy_at_transition(c, Rational(100))
            fractions.append(data['fraction'])
        for i in range(len(fractions) - 1):
            self.assertLess(fractions[i], fractions[i + 1])

    def test_page_quantum_correction_self_dual(self):
        """At c=13: quantum correction to Page time vanishes."""
        data = page_time_quantum_correction(Rational(13))
        self.assertEqual(data['delta_t_coefficient'], 0)
        self.assertTrue(data['self_dual'])

    def test_page_quantum_correction_convergence(self):
        """The A-hat sum converges: partial sum matches (1/2)/sin(1/2)-1."""
        data = page_time_quantum_correction(Rational(26), max_genus=20)
        self.assertTrue(data['sum_converged'])

    def test_page_transition_width_class_g(self):
        """Class G has no quantum smearing of the Page transition."""
        data = page_transition_width_by_class('heisenberg')
        self.assertEqual(data['quantum_smearing'], 0)
        self.assertEqual(data['shadow_class'], 'G')

    def test_page_transition_width_class_m(self):
        """Class M at c=26 has finite smearing (rho < 1)."""
        data = page_transition_width_by_class('virasoro', Rational(26), Rational(100))
        self.assertGreater(data['quantum_smearing'], 0)
        self.assertTrue(data['convergent'])

    def test_page_curve_full_self_dual(self):
        """Full Page curve at c=13 is symmetric."""
        data = page_curve_full(Rational(13), Rational(100), 5)
        self.assertTrue(data['self_dual'])
        self.assertEqual(data['page_time'], Rational(300, 13))

    def test_page_curve_genus_corrections(self):
        """Genus corrections use correct Faber-Pandharipande coefficients.

        Cross-check against independently computed lambda_g^FP.
        """
        data = page_curve_full(Rational(26), Rational(100), 5, max_genus=3)
        kappa = kappa_virasoro(Rational(26))
        for g in [1, 2, 3]:
            expected_fg = kappa * faber_pandharipande(g)
            self.assertEqual(data['genus_corrections'][g]['F_g'], expected_fg)


# =========================================================================
#  4. QEC RATE WITH HOLSTEIN-RIVERA
# =========================================================================

class TestQECRate(unittest.TestCase):
    """Tests for QEC rate simplification."""

    def test_before_hr_chain_length(self):
        """Before HR: 4-step verification chain."""
        chain = qec_verification_chain_before_hr()
        self.assertEqual(chain['n_steps'], 4)
        self.assertEqual(chain['rate'], Rational(1, 2))

    def test_after_hr_chain_length(self):
        """After HR: 2-step verification chain (P3 removed)."""
        chain = qec_verification_chain_after_hr()
        self.assertEqual(chain['n_steps'], 2)
        self.assertEqual(chain['hypothesis_removed'], 'P3 (properness/perfectness)')

    def test_qec_rate_universal_half(self):
        """R = 1/2 for all standard families after HR.

        Universal across the landscape: all Koszul algebras have R = 1/2.
        """
        for family in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            data = qec_rate_by_family_simplified(family)
            self.assertEqual(data['rate'], Rational(1, 2),
                             f"Rate != 1/2 for {family}")
            self.assertEqual(data['verification_steps'], 2)
            self.assertFalse(data['P3_needed'])

    def test_qec_distance_universal_2(self):
        """Code distance d = 2 for all families (bar degree shift)."""
        for family in ['heisenberg', 'virasoro', 'affine', 'betagamma']:
            data = qec_rate_by_family_simplified(family)
            self.assertEqual(data['distance'], 2)

    def test_qec_channels_by_class(self):
        """Redundancy channels depend on shadow depth."""
        self.assertEqual(qec_rate_by_family_simplified('heisenberg')['channels'], 0)
        self.assertEqual(qec_rate_by_family_simplified('affine')['channels'], 1)
        self.assertEqual(qec_rate_by_family_simplified('betagamma')['channels'], 2)
        self.assertEqual(qec_rate_by_family_simplified('virasoro')['channels'], -1)


# =========================================================================
#  5. MODULAR ENTANGLEMENT ENTROPY
# =========================================================================

class TestModularEntanglement(unittest.TestCase):
    """Tests for the bar-Verdier modular entanglement S^mod_g."""

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
        """Total modular entanglement converges to closed form.

        sum S^mod_g = |kappa-kappa!| * ((1/2)/sin(1/2) - 1).
        """
        data = modular_entanglement_genus_tower(Rational(1), Rational(-1), max_genus=20)
        self.assertAlmostEqual(float(data['total']),
                               data['total_closed_form'],
                               places=8)

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
        """Full analysis at c=13: self-dual, S^mod = 0, R=1/2."""
        data = full_page_curve_analysis(Rational(13), Rational(100))
        self.assertTrue(data['self_dual'])
        self.assertEqual(data['qec_rate'], Rational(1, 2))
        self.assertEqual(data['page_time'], Rational(300, 13))
        self.assertEqual(data['S_mod_1'], 0)
        self.assertEqual(data['page_fraction'], Rational(1, 2))

    def test_full_analysis_critical(self):
        """Full analysis at c=26: critical string, S^mod_1 = 13/24."""
        data = full_page_curve_analysis(Rational(26), Rational(100))
        self.assertFalse(data['self_dual'])
        self.assertEqual(data['S_mod_1'], Rational(13, 24))
        self.assertEqual(data['page_fraction'], Rational(1))

    def test_landscape_survey_completeness(self):
        """Survey covers at least 6 families."""
        survey = entanglement_landscape_survey()
        self.assertGreaterEqual(len(survey), 6)

    def test_landscape_survey_universal_rate(self):
        """All families in the survey have R = 1/2."""
        survey = entanglement_landscape_survey()
        for row in survey:
            self.assertEqual(row['qec_rate'], Rational(1, 2),
                             f"Rate != 1/2 for {row['family']}")

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
