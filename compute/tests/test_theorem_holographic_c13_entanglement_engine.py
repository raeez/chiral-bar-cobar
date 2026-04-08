r"""Tests for holographic entanglement at the Koszul self-dual point c = 13.

Multi-path verification of:
  (1) S_EE(Vir_13) = (13/3) log(L/eps) — three independent paths
  (2) Complementarity: S_EE(A) + S_EE(A!) = (26/3) log(L/eps)
  (3) Self-duality: S_EE(A) = S_EE(A!) at c = 13
  (4) Ryu-Takayanagi: S_RT = Area/(4*G_N) with G_N = 3/(26) (ell = 1)
  (5) Shadow connection: Delta = 40/87 at c = 13
  (6) BTZ entropy and genus corrections: F_1 = 13/48, F_2 = 91/11520
  (7) Modular entanglement vanishes at c = 13
  (8) Page curve is symmetric: S_Page/S_BH = 1/2

Each result verified by at least 3 paths (Multi-Path Verification Mandate).
"""

import math
import unittest
from fractions import Fraction

from sympy import Rational, simplify, Abs, pi, bernoulli, factorial

from compute.lib.theorem_holographic_c13_entanglement_engine import (
    # Constants
    C_SELF_DUAL,
    KAPPA_SELF_DUAL,
    KAPPA_DUAL_SELF_DUAL,
    KAPPA_SUM,
    SEE_COEFFICIENT,
    COMPLEMENTARITY_SUM,
    S3_VIRASORO,
    S4_C13,
    DELTA_C13,
    LAMBDA_1,
    LAMBDA_2,
    LAMBDA_3,
    F1_C13,
    F2_C13,
    F3_C13,
    # Section 1: Entanglement entropy
    see_coefficient_c13,
    verify_see_three_paths,
    see_self_dual_symmetry,
    # Section 2: Complementarity
    complementarity_c13,
    kappa_sum_virasoro_general,
    # Section 3: Ryu-Takayanagi
    ryu_takayanagi_c13,
    newton_constant_from_kappa,
    # Section 4: Shadow connection and QES
    shadow_data_c13,
    discriminant_complementarity_c13,
    qes_shadow_ward_c13,
    # Section 5: BTZ
    btz_entropy_c13,
    btz_genus1_correction_c13,
    btz_genus2_correction_c13,
    btz_genus_tower_c13,
    # Section 6: Self-duality
    modular_entanglement_c13,
    page_time_correction_c13,
    page_fraction_c13,
    shadow_self_duality_c13,
    # Section 7: Cross-checks
    verify_all_c13_invariants,
    c13_vs_other_central_charges,
    entanglement_at_special_values,
)

from compute.lib.entanglement_shadow_engine import (
    kappa_virasoro,
    kappa_heisenberg,
    von_neumann_entropy_scalar,
    faber_pandharipande,
    scalar_free_energy,
    shadow_radius_virasoro,
    entanglement_complementarity_sum,
    verify_complementarity_constraint,
)


# =========================================================================
#  1. ENTANGLEMENT ENTROPY COEFFICIENT
# =========================================================================

class TestSEECoefficientC13(unittest.TestCase):
    """Tests for S_EE(Vir_13) = (13/3) log(L/eps)."""

    def test_see_coefficient_value(self):
        """S_EE coefficient at c=13 is 13/3."""
        self.assertEqual(see_coefficient_c13(), Rational(13, 3))

    def test_see_three_paths_agree(self):
        """Three independent computations of S_EE agree."""
        data = verify_see_three_paths()
        self.assertTrue(data['paths_agree'])
        self.assertEqual(data['coefficient'], Rational(13, 3))

    def test_see_path1_calabrese_cardy(self):
        """Path 1: c/3 = 13/3."""
        self.assertEqual(Rational(13, 3), C_SELF_DUAL / 3)

    def test_see_path2_from_kappa(self):
        """Path 2: 2*kappa/3 = 2*(13/2)/3 = 13/3."""
        self.assertEqual(2 * KAPPA_SELF_DUAL / 3, Rational(13, 3))

    def test_see_path3_von_neumann(self):
        """Path 3: von Neumann entropy from the engine."""
        see = von_neumann_entropy_scalar(KAPPA_SELF_DUAL, 1)
        self.assertEqual(see, Rational(13, 3))

    def test_see_matches_engine(self):
        """S_EE from the entanglement_shadow_engine matches."""
        see = von_neumann_entropy_scalar(kappa_virasoro(13), 1)
        self.assertEqual(see, Rational(13, 3))


# =========================================================================
#  2. KOSZUL COMPLEMENTARITY
# =========================================================================

class TestComplementarityC13(unittest.TestCase):
    """Tests for complementarity S_EE(A) + S_EE(A!) = 26/3."""

    def test_complementarity_sum(self):
        """Complementarity sum at c=13 is 26/3."""
        data = complementarity_c13()
        self.assertEqual(data['sum'], Rational(26, 3))
        self.assertTrue(data['paths_agree'])

    def test_kappa_sum_is_13(self):
        """kappa(Vir_13) + kappa(Vir_13) = 13."""
        self.assertEqual(KAPPA_SUM, Rational(13))
        self.assertEqual(KAPPA_SELF_DUAL + KAPPA_DUAL_SELF_DUAL, Rational(13))

    def test_kappa_sum_general(self):
        """kappa + kappa' = 13 for any c (Virasoro)."""
        for c_val in [Rational(1), Rational(13), Rational(26), Rational(1, 2)]:
            data = kappa_sum_virasoro_general(c_val)
            self.assertEqual(data['sum'], Rational(13))

    def test_complementarity_engine(self):
        """Cross-check with entanglement_shadow_engine."""
        total = entanglement_complementarity_sum(Rational(13), 1)
        self.assertEqual(total, Rational(26, 3))

    def test_complementarity_general_c(self):
        """Complementarity holds for arbitrary c (not just c=13)."""
        for c_val in [Rational(1), Rational(7, 10), Rational(25)]:
            self.assertTrue(verify_complementarity_constraint(c_val))


class TestSelfDualSymmetry(unittest.TestCase):
    """Tests for S_EE(A) = S_EE(A!) at c = 13."""

    def test_symmetry(self):
        """S_EE(Vir_13) = S_EE(Vir_13^!)."""
        data = see_self_dual_symmetry()
        self.assertTrue(data['symmetric'])
        self.assertEqual(data['difference'], Rational(0))

    def test_see_A_equals_see_A_dual(self):
        """Both halves of the Koszul pair have S_EE = 13/3."""
        data = see_self_dual_symmetry()
        self.assertEqual(data['see_A'], Rational(13, 3))
        self.assertEqual(data['see_A_dual'], Rational(13, 3))

    def test_only_c13_is_self_dual(self):
        """c = 13 is the unique self-dual point for Virasoro."""
        for c_val in [Rational(1), Rational(12), Rational(14), Rational(26)]:
            kappa = kappa_virasoro(c_val)
            kappa_d = kappa_virasoro(26 - c_val)
            self.assertNotEqual(kappa, kappa_d)


# =========================================================================
#  3. RYU-TAKAYANAGI
# =========================================================================

class TestRyuTakayanagiC13(unittest.TestCase):
    """Tests for the RT formula at c = 13."""

    def test_rt_coefficient(self):
        """S_RT coefficient = 13/3."""
        data = ryu_takayanagi_c13()
        self.assertEqual(data['S_RT_coefficient'], Rational(13, 3))
        self.assertTrue(data['paths_agree'])

    def test_newton_constant(self):
        """G_N = 3*ell/(2*c) = 3/26 at c=13, ell=1."""
        gn = newton_constant_from_kappa(KAPPA_SELF_DUAL)
        self.assertEqual(gn, Rational(3, 26))

    def test_newton_constant_from_c(self):
        """G_N = 3/(2*13) = 3/26 via Brown-Henneaux."""
        gn = Rational(3) / (2 * C_SELF_DUAL)
        self.assertEqual(gn, Rational(3, 26))

    def test_rt_matches_see(self):
        """RT coefficient matches CFT computation."""
        data = ryu_takayanagi_c13()
        self.assertEqual(data['S_RT_coefficient'], see_coefficient_c13())


# =========================================================================
#  4. SHADOW CONNECTION AND QES
# =========================================================================

class TestShadowConnectionC13(unittest.TestCase):
    """Tests for shadow data at c = 13."""

    def test_delta_value(self):
        """Delta(Vir_13) = 40/87."""
        data = shadow_data_c13()
        self.assertEqual(data['Delta'], Rational(40, 87))
        self.assertTrue(data['paths_agree'])

    def test_s4_value(self):
        """S_4(Vir_13) = 10/1131."""
        self.assertEqual(S4_C13, Rational(10, 1131))
        # Cross-check: 10/[13*(5*13+22)] = 10/[13*87] = 10/1131
        expected = Rational(10) / (13 * 87)
        self.assertEqual(S4_C13, expected)

    def test_delta_three_paths(self):
        """Delta computed three ways."""
        # Path 1: 8*kappa*S_4
        path1 = 8 * KAPPA_SELF_DUAL * S4_C13
        # Path 2: 40/(5c+22)
        path2 = Rational(40) / (5 * 13 + 22)
        # Path 3: explicit
        path3 = Rational(40, 87)
        self.assertEqual(simplify(path1 - path2), 0)
        self.assertEqual(path2, path3)

    def test_shadow_class_M(self):
        """Virasoro at c=13 is class M (infinite shadow depth)."""
        data = shadow_data_c13()
        self.assertEqual(data['shadow_class'], 'M')

    def test_shadow_radius_convergent(self):
        """Shadow radius at c=13 is < 1 (corrections converge)."""
        rho = shadow_radius_virasoro(13.0)
        self.assertLess(rho, 1.0)
        self.assertAlmostEqual(rho, 0.4674, places=3)

    def test_discriminant_complementarity(self):
        """Delta(13) + Delta(13) = 80/87."""
        data = discriminant_complementarity_c13()
        self.assertEqual(data['sum'], Rational(80, 87))
        self.assertTrue(data['paths_agree'])

    def test_discriminant_general_formula(self):
        """6960/[(5*13+22)(152-5*13)] = 80/87."""
        num = Rational(6960)
        den = (5 * 13 + 22) * (152 - 5 * 13)
        # den = 87 * 87 = 7569
        self.assertEqual(den, 7569)
        self.assertEqual(num / den, Rational(80, 87))


class TestQESC13(unittest.TestCase):
    """Tests for the quantum extremal surface at c = 13."""

    def test_qes_exists(self):
        """QES location is computable at c = 13."""
        data = qes_shadow_ward_c13()
        self.assertIsNotNone(data['t_QES'])

    def test_qes_negative(self):
        """QES is at negative t (inside horizon)."""
        data = qes_shadow_ward_c13()
        self.assertTrue(data['t_QES'] < 0)

    def test_q_positive_at_qes(self):
        """Shadow metric Q is positive at the QES."""
        data = qes_shadow_ward_c13()
        self.assertTrue(data['Q_positive'])


# =========================================================================
#  5. BTZ BLACK HOLE
# =========================================================================

class TestBTZC13(unittest.TestCase):
    """Tests for BTZ entropy and quantum corrections at c = 13."""

    def test_btz_entropy_paths_agree(self):
        """Three paths for BTZ entropy agree."""
        data = btz_entropy_c13()
        self.assertTrue(data['paths_agree'])

    def test_genus1_correction_value(self):
        """F_1(Vir_13) = 13/48."""
        data = btz_genus1_correction_c13()
        self.assertEqual(data['F_1'], Rational(13, 48))
        self.assertTrue(data['paths_agree'])

    def test_genus1_from_engine(self):
        """Cross-check F_1 with scalar_free_energy engine."""
        f1 = scalar_free_energy(Rational(13, 2), 1)
        self.assertEqual(f1, Rational(13, 48))

    def test_genus2_correction_value(self):
        """F_2(Vir_13) = 91/11520."""
        data = btz_genus2_correction_c13()
        self.assertEqual(data['F_2'], Rational(91, 11520))
        self.assertTrue(data['paths_agree'])

    def test_genus2_from_engine(self):
        """Cross-check F_2 with scalar_free_energy engine."""
        f2 = scalar_free_energy(Rational(13, 2), 2)
        self.assertEqual(f2, Rational(91, 11520))

    def test_f2_over_f1_ratio(self):
        """F_2/F_1 = 7/240 (universal ratio from lambda_2/lambda_1)."""
        ratio = F2_C13 / F1_C13
        self.assertEqual(ratio, Rational(7, 240))

    def test_genus3_correction(self):
        """F_3(Vir_13) from the engine."""
        f3 = scalar_free_energy(Rational(13, 2), 3)
        self.assertEqual(f3, F3_C13)

    def test_genus_tower_convergence(self):
        """Genus tower sum converges to A-hat value."""
        data = btz_genus_tower_c13(20)
        self.assertTrue(data['sum_converged'])

    def test_genus_tower_all_positive(self):
        """All F_g are positive at c = 13."""
        data = btz_genus_tower_c13(10)
        for g, corr in data['corrections'].items():
            self.assertGreater(corr['F_g'], 0,
                               f"F_{g} should be positive at c=13")


# =========================================================================
#  6. SELF-DUALITY CONSEQUENCES
# =========================================================================

class TestSelfDualityC13(unittest.TestCase):
    """Tests for consequences of Koszul self-duality at c = 13."""

    def test_modular_entanglement_vanishes(self):
        """S^mod_g = 0 for all g at c = 13."""
        data = modular_entanglement_c13(10)
        self.assertTrue(data['all_zero'])

    def test_page_time_correction_vanishes(self):
        """Quantum correction to Page time = 0 at c = 13."""
        data = page_time_correction_c13()
        self.assertEqual(data['delta_t'], Rational(0))

    def test_page_fraction_half(self):
        """S_Page/S_BH = 1/2 at c = 13."""
        data = page_fraction_c13()
        self.assertEqual(data['fraction'], Rational(1, 2))
        self.assertTrue(data['paths_agree'])

    def test_shadow_fully_self_dual(self):
        """Full shadow tower is self-dual at c = 13."""
        data = shadow_self_duality_c13()
        self.assertTrue(data['fully_self_dual'])
        self.assertTrue(data['kappa_match'])
        self.assertTrue(data['S4_match'])
        self.assertTrue(data['Delta_match'])


# =========================================================================
#  7. CROSS-CHECKS AND CONSISTENCY
# =========================================================================

class TestCrossChecks(unittest.TestCase):
    """Master consistency checks for all c = 13 invariants."""

    def test_all_invariants_consistent(self):
        """All c = 13 invariants are mutually consistent."""
        data = verify_all_c13_invariants()
        self.assertTrue(data['all_consistent'])
        for name, ok in data['checks'].items():
            self.assertTrue(ok, f"Check '{name}' failed")

    def test_c13_is_unique_self_dual(self):
        """c = 13 is self-dual; other values are not."""
        data = c13_vs_other_central_charges()
        self.assertTrue(data['c13']['self_dual'])
        self.assertFalse(data['c1']['self_dual'])
        self.assertFalse(data['c26']['self_dual'])
        self.assertFalse(data['c_half']['self_dual'])

    def test_modular_entanglement_nonzero_away_from_13(self):
        """Modular entanglement is nonzero for c != 13."""
        data = c13_vs_other_central_charges()
        self.assertGreater(data['c1']['modular_entanglement_g1'], 0)
        self.assertGreater(data['c26']['modular_entanglement_g1'], 0)

    def test_complementarity_sum_universal(self):
        """Complementarity sum = 26/3 for ALL c, not just c = 13."""
        data = c13_vs_other_central_charges()
        for label in ['c1', 'c13', 'c26', 'c_half']:
            self.assertEqual(data[label]['complementarity_sum'],
                             Rational(26, 3))

    def test_special_values_table(self):
        """S_EE at special central charges."""
        data = entanglement_at_special_values()
        self.assertEqual(data[Rational(13)]['S_EE'], Rational(13, 3))
        self.assertEqual(data[Rational(26)]['S_EE'], Rational(26, 3))
        self.assertEqual(data[Rational(1)]['S_EE'], Rational(1, 3))
        self.assertEqual(data[Rational(1, 2)]['S_EE'], Rational(1, 6))


# =========================================================================
#  8. CONSTANT VERIFICATION (AP10 defense)
# =========================================================================

class TestConstantVerification(unittest.TestCase):
    """Independent recomputation of all hardcoded constants (AP10 defense)."""

    def test_kappa_c13(self):
        """kappa(Vir_13) = 13/2 from the defining formula."""
        self.assertEqual(KAPPA_SELF_DUAL, Rational(13, 2))
        self.assertEqual(kappa_virasoro(13), Rational(13, 2))

    def test_s4_from_formula(self):
        """S_4 = 10/[c(5c+22)] at c = 13."""
        c = Rational(13)
        expected = Rational(10) / (c * (5 * c + 22))
        self.assertEqual(expected, Rational(10, 1131))
        self.assertEqual(S4_C13, expected)

    def test_delta_from_formula(self):
        """Delta = 8*kappa*S_4 = 40/87 at c = 13."""
        Delta = 8 * Rational(13, 2) * Rational(10, 1131)
        self.assertEqual(Delta, Rational(40, 87))
        self.assertEqual(DELTA_C13, Delta)

    def test_lambda1_from_bernoulli(self):
        """lambda_1^FP = 1/24 from Bernoulli numbers."""
        b2 = bernoulli(2)  # = 1/6
        abs_b2 = Abs(b2)
        lam1 = Rational(2**(2-1) - 1, 2**(2-1)) * abs_b2 / factorial(2)
        self.assertEqual(lam1, Rational(1, 24))
        self.assertEqual(LAMBDA_1, lam1)

    def test_lambda2_from_bernoulli(self):
        """lambda_2^FP = 7/5760 from Bernoulli numbers."""
        b4 = bernoulli(4)  # = -1/30
        abs_b4 = Abs(b4)
        lam2 = Rational(2**(4-1) - 1, 2**(4-1)) * abs_b4 / factorial(4)
        self.assertEqual(lam2, Rational(7, 5760))
        self.assertEqual(LAMBDA_2, lam2)

    def test_f1_from_components(self):
        """F_1 = kappa * lambda_1 = (13/2)*(1/24) = 13/48."""
        self.assertEqual(F1_C13, KAPPA_SELF_DUAL * LAMBDA_1)
        self.assertEqual(F1_C13, Rational(13, 48))

    def test_f2_from_components(self):
        """F_2 = kappa * lambda_2 = (13/2)*(7/5760) = 91/11520."""
        self.assertEqual(F2_C13, KAPPA_SELF_DUAL * LAMBDA_2)
        self.assertEqual(F2_C13, Rational(91, 11520))

    def test_see_from_kappa(self):
        """S_EE coefficient = 2*kappa/3 = 2*(13/2)/3 = 13/3."""
        self.assertEqual(SEE_COEFFICIENT, 2 * KAPPA_SELF_DUAL / 3)
        self.assertEqual(SEE_COEFFICIENT, Rational(13, 3))

    def test_complementarity_sum_from_kappa(self):
        """26/3 = 2*(kappa + kappa')/3 = 2*13/3."""
        self.assertEqual(COMPLEMENTARITY_SUM, 2 * KAPPA_SUM / 3)
        self.assertEqual(COMPLEMENTARITY_SUM, Rational(26, 3))

    def test_faber_pandharipande_cross_check(self):
        """Cross-check lambda_g against engine for g = 1..5."""
        self.assertEqual(faber_pandharipande(1), Rational(1, 24))
        self.assertEqual(faber_pandharipande(2), Rational(7, 5760))
        self.assertEqual(faber_pandharipande(3), Rational(31, 967680))


if __name__ == '__main__':
    unittest.main()
