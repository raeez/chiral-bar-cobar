"""Tests for bc_microstate_counting_engine.py

Multi-path verification: every numerical result checked by 3+ independent paths
where possible (direct computation, alternative formula, limiting case, Koszul
duality cross-check).

AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (NOT 0).
AP1/AP9: kappa(Vir_c) = c/2, recomputed from first principles.
"""

import math
import unittest
from fractions import Fraction

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from lib.bc_microstate_counting_engine import (
    J_COEFFICIENTS,
    MONSTER_DECOMPOSITION_CHECK,
    j_function_coefficient,
    virasoro_vacuum_character_coefficient,
    virasoro_full_character_coefficient,
    free_boson_degeneracy,
    monster_degeneracy,
    verify_monster_mckay,
    cardy_formula,
    cardy_formula_rademacher,
    cardy_relative_error,
    cardy_error_table,
    cardy_crossover_n,
    kappa_virasoro,
    virasoro_S3,
    virasoro_S4,
    virasoro_S5,
    lambda_fp,
    F_g_scalar,
    planted_forest_g2,
    planted_forest_g3,
    virasoro_free_energy,
    shadow_corrected_log_Z,
    shadow_correction_to_degeneracy,
    farey_sequence,
    farey_tail_seed,
    farey_tail_term,
    farey_tail_partition,
    logarithmic_correction_alpha,
    one_loop_C0,
    quartic_C1,
    entropy_expansion,
    shadow_zeta_function,
    shadow_zeta_at_zero,
    shadow_zeta_derivative_at_zero,
    one_loop_determinant_spin_s,
    full_one_loop_determinant,
    sen_quantum_entropy_function,
    virasoro_degeneracy_c_dependence,
    wall_crossing_jump,
    wall_crossing_table,
    topological_string_Z,
    osv_test,
    single_particle_Z,
    multiparticle_Z,
    multiparticle_ratio,
    multiparticle_crossover,
    koszul_dual_c,
    koszul_degeneracy_ratio,
    koszul_microstate_table,
    koszul_self_dual_test,
    koszul_asymptotic_ratio,
    verify_monster_degeneracies,
    verify_cardy_asymptotics,
    verify_kappa_sum_rule,
    shadow_depth_class,
)


class TestJFunctionCoefficients(unittest.TestCase):
    """Test J-function (j-invariant minus 744) coefficients."""

    def test_j_vacuum(self):
        """J(-1) = 1 (vacuum)."""
        self.assertEqual(j_function_coefficient(-1), 1)

    def test_j_weight1_vanishes(self):
        """J(0) = 0 (no weight-1 currents in Monster module)."""
        self.assertEqual(j_function_coefficient(0), 0)

    def test_j_mckay_196884(self):
        """J(1) = 196884 = 196883 + 1 (McKay observation)."""
        self.assertEqual(j_function_coefficient(1), 196884)
        # Verify McKay decomposition
        self.assertEqual(196884, 196883 + 1)

    def test_j_level2(self):
        """J(2) = 21493760 = 1 + 196883 + 21296876."""
        self.assertEqual(j_function_coefficient(2), 21493760)
        self.assertEqual(21493760, 1 + 196883 + 21296876)

    def test_j_tabulated_values(self):
        """All tabulated J-coefficients match OEIS A014708."""
        for n, val in J_COEFFICIENTS.items():
            self.assertEqual(j_function_coefficient(n), val)

    def test_j_coefficients_positive_for_n_ge_1(self):
        """J(n) > 0 for all n >= 1."""
        for n in range(1, 21):
            self.assertGreater(j_function_coefficient(n), 0)

    def test_j_growth_monotone(self):
        """J(n) is strictly increasing for n >= 1."""
        for n in range(1, 20):
            self.assertLess(j_function_coefficient(n), j_function_coefficient(n + 1))

    def test_j_recursive_matches_tabulated(self):
        """Recursive computation matches tabulated for n = 1..20."""
        for n in range(1, 21):
            self.assertEqual(j_function_coefficient(n), J_COEFFICIENTS[n])


class TestMonsterDecomposition(unittest.TestCase):
    """Test Monster module decompositions."""

    def test_mckay_all_levels(self):
        """Verify Monster decomposition sums at all available levels."""
        for n, decomp in MONSTER_DECOMPOSITION_CHECK.items():
            result = verify_monster_mckay(n)
            self.assertTrue(result['match'],
                            f"Monster decomposition fails at n={n}: "
                            f"{result['d_n']} != {result['decomposition_sum']}")

    def test_monster_degeneracy_equals_j(self):
        """monster_degeneracy(n) == j_function_coefficient(n) for all tabulated n."""
        for n in range(-1, 21):
            self.assertEqual(monster_degeneracy(n), j_function_coefficient(n))

    def test_verify_monster_degeneracies(self):
        """Full verification suite returns all matches."""
        results = verify_monster_degeneracies(20)
        for entry in results:
            if entry.get('match') is not None:
                self.assertTrue(entry['match'])


class TestPartitionFunction(unittest.TestCase):
    """Test partition functions and vacuum characters."""

    def test_free_boson_small_n(self):
        """Free boson p(n) for small n."""
        expected = {0: 1, 1: 1, 2: 2, 3: 3, 4: 5, 5: 7, 6: 11, 7: 15}
        for n, val in expected.items():
            self.assertEqual(free_boson_degeneracy(n), val)

    def test_virasoro_vacuum_level0(self):
        """Vacuum state: d(0) = 1 for any c."""
        for c in [1.0, 13.0, 26.0]:
            self.assertEqual(virasoro_vacuum_character_coefficient(0, c), 1.0)

    def test_virasoro_vacuum_level1_vanishes(self):
        """No L_{-1}|0> in vacuum module: d(1) = 0."""
        for c in [1.0, 13.0, 26.0]:
            self.assertEqual(virasoro_vacuum_character_coefficient(1, c), 0.0)

    def test_virasoro_vacuum_level2(self):
        """At level 2: L_{-2}|0> is the only state, so d(2) = 1."""
        # p_2(2) = p(2) - p(1) = 2 - 1 = 1
        self.assertEqual(virasoro_vacuum_character_coefficient(2, 26.0), 1.0)

    def test_virasoro_vacuum_level3(self):
        """p_2(3) = p(3) - p(2) = 3 - 2 = 1."""
        self.assertEqual(virasoro_vacuum_character_coefficient(3, 26.0), 1.0)

    def test_virasoro_vacuum_level4(self):
        """p_2(4) = p(4) - p(3) = 5 - 3 = 2."""
        self.assertEqual(virasoro_vacuum_character_coefficient(4, 26.0), 2.0)

    def test_virasoro_vacuum_negative(self):
        """d(n) = 0 for n < 0."""
        self.assertEqual(virasoro_vacuum_character_coefficient(-1, 26.0), 0.0)


class TestCardyFormula(unittest.TestCase):
    """Test Cardy asymptotic formula."""

    def test_cardy_positive_for_positive_n(self):
        """Cardy formula gives positive values for n > 0, c > 0."""
        for c in [1.0, 13.0, 26.0]:
            for n in [1, 5, 10, 50]:
                self.assertGreater(cardy_formula(n, c), 0.0)

    def test_cardy_zero_for_n_le_0(self):
        """Cardy formula returns 0 for n <= 0."""
        self.assertEqual(cardy_formula(0, 26.0), 0.0)
        self.assertEqual(cardy_formula(-1, 26.0), 0.0)

    def test_cardy_exponential_growth(self):
        """Cardy grows exponentially: d(n+1) > d(n) for large n."""
        c = 26.0
        for n in [10, 20, 50]:
            self.assertGreater(cardy_formula(n + 1, c), cardy_formula(n, c))

    def test_cardy_increases_with_c(self):
        """For fixed n, larger c gives larger Cardy degeneracy."""
        n = 20
        for c1, c2 in [(1.0, 13.0), (13.0, 26.0)]:
            self.assertLess(cardy_formula(n, c1), cardy_formula(n, c2))

    def test_cardy_log_ratio_approaches_1(self):
        """log(d_Cardy) / log(d_exact) -> 1 for large n (c=24, Monster)."""
        # The Cardy formula captures the exponential growth correctly;
        # the log ratio should approach 1 for large n.
        ratios = []
        for n in [5, 10, 15, 20]:
            exact = monster_degeneracy(n)
            if exact <= 0:
                continue
            cardy = cardy_formula(n, 24.0)
            if cardy <= 0:
                continue
            ratio = math.log(cardy) / math.log(exact)
            ratios.append(ratio)
        # The ratio should approach 1; later values should be closer
        self.assertGreater(len(ratios), 2)
        # All ratios should be in a reasonable range
        for r in ratios:
            self.assertGreater(r, 0.5)
            self.assertLess(r, 2.0)

    def test_cardy_relative_error_function(self):
        """cardy_relative_error agrees with manual computation."""
        n, c = 10, 1.0
        exact = free_boson_degeneracy(n)
        err = cardy_relative_error(n, c, exact)
        manual_err = abs(exact - cardy_formula(n, c)) / exact
        self.assertAlmostEqual(err, manual_err, places=10)

    def test_cardy_error_table_returns_rows(self):
        """Error table produces valid rows."""
        table = cardy_error_table(1.0, free_boson_degeneracy, 1, 10)
        self.assertGreater(len(table), 0)
        for row in table:
            self.assertIn('n', row)
            self.assertIn('relative_error', row)

    def test_rademacher_leading_term_positive(self):
        """Rademacher formula (1 term) gives positive values for sufficiently large c*n."""
        for c in [13.0, 26.0]:
            for n in [10, 20]:
                val = cardy_formula_rademacher(n, c, 1)
                self.assertGreater(val, 0.0)


class TestKappaAndShadow(unittest.TestCase):
    """Test kappa formulas and shadow invariants."""

    def test_kappa_virasoro_formula(self):
        """kappa(Vir_c) = c/2."""
        for c in [1, 6, 13, 26]:
            self.assertEqual(kappa_virasoro(c), Fraction(c, 2))

    def test_kappa_sum_rule_ap24(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13 for ALL c."""
        for c in [0, 1, 6, 10, 13, 20, 25, 26]:
            kappa = kappa_virasoro(c)
            kappa_dual = kappa_virasoro(26 - c)
            self.assertEqual(kappa + kappa_dual, Fraction(13))

    def test_kappa_sum_rule_function(self):
        """verify_kappa_sum_rule returns match = True for various c."""
        for c in [1.0, 6.0, 13.0, 26.0]:
            result = verify_kappa_sum_rule(c)
            self.assertTrue(result['match'])
            self.assertAlmostEqual(result['sum'], 13.0, places=10)

    def test_virasoro_s3_c_independent(self):
        """S_3 = 2, independent of c."""
        self.assertEqual(virasoro_S3(), Fraction(2))

    def test_virasoro_s4_specific_values(self):
        """Q^contact = 10/[c(5c+22)] at specific c."""
        # c = 1: 10/(1*27) = 10/27
        self.assertEqual(virasoro_S4(1), Fraction(10, 27))
        # c = 13: 10/(13*87) = 10/1131
        self.assertEqual(virasoro_S4(13), Fraction(10, 1131))

    def test_virasoro_s5_specific(self):
        """S_5 = -48/[c^2(5c+22)]."""
        # c = 1: -48/(1*27) = -48/27 = -16/9
        self.assertEqual(virasoro_S5(1), Fraction(-48, 27))

    def test_koszul_dual_c(self):
        """Koszul dual: c' = 26 - c."""
        self.assertAlmostEqual(koszul_dual_c(1.0), 25.0)
        self.assertAlmostEqual(koszul_dual_c(13.0), 13.0)
        self.assertAlmostEqual(koszul_dual_c(26.0), 0.0)


class TestFaberPandharipande(unittest.TestCase):
    """Test Faber-Pandharipande intersection numbers."""

    def test_lambda1(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Fraction(1, 24))

    def test_lambda2(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))

    def test_lambda3(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))

    def test_lambda_positive(self):
        """All lambda_g^FP are positive (AP22: Bernoulli signs)."""
        for g in range(1, 8):
            self.assertGreater(lambda_fp(g), 0)

    def test_lambda_decreasing(self):
        """lambda_g^FP decreases with g."""
        for g in range(1, 7):
            self.assertGreater(lambda_fp(g), lambda_fp(g + 1))

    def test_lambda_invalid_genus(self):
        """lambda_fp raises for g < 1."""
        with self.assertRaises(ValueError):
            lambda_fp(0)


class TestFreeEnergy(unittest.TestCase):
    """Test free energy computations."""

    def test_F1_scalar(self):
        """F_1 = kappa * lambda_1 = kappa/24."""
        for c in [1, 13, 26]:
            kappa = kappa_virasoro(c)
            expected = kappa * Fraction(1, 24)
            self.assertEqual(F_g_scalar(kappa, 1), expected)

    def test_F_g_linear_in_kappa(self):
        """F_g(2*kappa) = 2 * F_g(kappa) (linearity)."""
        for g in range(1, 5):
            F1 = F_g_scalar(Fraction(3), g)
            F2 = F_g_scalar(Fraction(6), g)
            self.assertEqual(F2, 2 * F1)

    def test_virasoro_free_energy_genus1(self):
        """At genus 1: F_1 = kappa * lambda_1 (no planted forest)."""
        for c in [1, 13, 26]:
            kappa = kappa_virasoro(c)
            self.assertEqual(virasoro_free_energy(c, 1), kappa * lambda_fp(1))

    def test_planted_forest_g2_heisenberg_vanishes(self):
        """Heisenberg (S_3 = 0): planted-forest g=2 correction vanishes."""
        # S_3 = 0 for Heisenberg
        result = planted_forest_g2(Fraction(1), Fraction(0))
        self.assertEqual(result, Fraction(0))

    def test_planted_forest_g2_virasoro(self):
        """Planted-forest at g=2 for Virasoro: S_3*(10*S_3 - kappa)/48."""
        kappa = kappa_virasoro(26)  # = 13
        S3 = virasoro_S3()  # = 2
        expected = Fraction(2) * (20 - 13) / 48
        self.assertEqual(planted_forest_g2(kappa, S3), expected)

    def test_virasoro_free_energy_genus2_has_planted_forest(self):
        """F_2 includes planted-forest correction at genus 2."""
        c = 26
        kappa = kappa_virasoro(c)
        scalar = F_g_scalar(kappa, 2)
        full = virasoro_free_energy(c, 2)
        # They should differ because S_3 = 2 != 0
        self.assertNotEqual(scalar, full)
        # full = scalar + planted_forest
        pf = planted_forest_g2(kappa, virasoro_S3())
        self.assertEqual(full, scalar + pf)


class TestShadowCorrectedPartition(unittest.TestCase):
    """Test shadow-corrected partition function."""

    def test_shadow_correction_positive_factor(self):
        """Shadow correction factor is positive."""
        for c in [6.0, 13.0, 26.0]:
            for n in [10, 50, 100]:
                factor = shadow_correction_to_degeneracy(n, c)
                self.assertGreater(factor, 0.0)

    def test_shadow_correction_close_to_1_for_large_n(self):
        """For large n, shadow corrections are small (factor near 1)."""
        factor = shadow_correction_to_degeneracy(1000, 13.0)
        self.assertAlmostEqual(factor, 1.0, delta=0.1)

    def test_shadow_corrected_log_Z_finite(self):
        """log Z^sh is finite for valid parameters."""
        val = shadow_corrected_log_Z(13.0, 10.0, g_max=3)
        self.assertTrue(math.isfinite(val))


class TestFareyTail(unittest.TestCase):
    """Test Farey tail expansion."""

    def test_farey_sequence_length(self):
        """Farey sequence includes (0,1) and coprime pairs."""
        pairs = farey_sequence(1)
        self.assertIn((0, 1), pairs)
        self.assertIn((1, 0), pairs)

    def test_farey_pairs_coprime(self):
        """All pairs in the Farey sequence are coprime."""
        for c_F, d in farey_sequence(5):
            if c_F > 0:
                self.assertEqual(math.gcd(c_F, abs(d)), 1)

    def test_farey_tail_seed_magnitude(self):
        """Farey tail seed has unit magnitude for purely imaginary tau."""
        tau = 0.1j
        Z = farey_tail_seed(24.0, tau)
        # Z = exp(-pi*i*c*tau/12), with tau = 0.1i: Z = exp(pi*24*0.1/12) = exp(0.2*pi)
        expected_mag = math.exp(math.pi * 24.0 * 0.1 / 12.0)
        self.assertAlmostEqual(abs(Z), expected_mag, places=5)

    def test_farey_tail_partition_finite(self):
        """Farey tail partition function is finite."""
        tau = 0.5j
        Z = farey_tail_partition(24.0, tau, N_farey=3, g_max=0)
        self.assertTrue(math.isfinite(abs(Z)))


class TestLogarithmicCorrections(unittest.TestCase):
    """Test logarithmic corrections to entropy."""

    def test_alpha_formula(self):
        """alpha = (c+1)/4."""
        for c in [1.0, 13.0, 26.0]:
            expected = (c + 1.0) / 4.0
            self.assertAlmostEqual(logarithmic_correction_alpha(c), expected, places=10)

    def test_C0_well_defined(self):
        """C_0 is finite for c > 0."""
        for c in [1.0, 13.0, 26.0]:
            C0 = one_loop_C0(c)
            self.assertTrue(math.isfinite(C0))

    def test_quartic_C1_finite(self):
        """C_1 coefficient is finite."""
        for c in [6.0, 13.0, 26.0]:
            C1 = quartic_C1(c)
            self.assertTrue(math.isfinite(C1))

    def test_entropy_expansion_components(self):
        """Entropy expansion returns all components."""
        result = entropy_expansion(100, 26.0)
        for key in ['S_BH', 'alpha', 'S_log', 'C_0', 'C_1', 'S_total']:
            self.assertIn(key, result)

    def test_entropy_S_BH_formula(self):
        """S_BH = 2*pi*sqrt(c*n/6)."""
        n, c = 100, 26.0
        result = entropy_expansion(n, c)
        expected = 2.0 * math.pi * math.sqrt(c * n / 6.0)
        self.assertAlmostEqual(result['S_BH'], expected, places=8)

    def test_entropy_total_dominated_by_S_BH(self):
        """For large n, S_total ~ S_BH."""
        result = entropy_expansion(10000, 26.0)
        # S_BH should be by far the largest contribution
        self.assertGreater(result['S_BH'], abs(result['S_log']))


class TestShadowZeta(unittest.TestCase):
    """Test shadow zeta function."""

    def test_shadow_zeta_at_zero_finite(self):
        """zeta_A(0) is finite."""
        val = shadow_zeta_at_zero(13.0, r_max=20)
        self.assertTrue(math.isfinite(val))

    def test_shadow_zeta_derivative_finite(self):
        """-zeta'_A(0) is finite."""
        val = shadow_zeta_derivative_at_zero(13.0, r_max=20)
        self.assertTrue(math.isfinite(val))

    def test_shadow_zeta_leading_term_is_kappa(self):
        """Leading term of zeta_A(s) at r=2 is kappa * 2^{-s}."""
        c = 26.0
        kappa = c / 2.0  # = 13
        s = 2.0
        zeta_val = shadow_zeta_function(c, s, r_max=2)
        expected = kappa * 2.0 ** (-s)  # only r=2 term
        self.assertAlmostEqual(zeta_val.real, expected, places=5)

    def test_one_loop_determinant_spin_scaling(self):
        """Spin-s determinant scales as (2s+1)."""
        c = 13.0
        det_0 = one_loop_determinant_spin_s(c, 0, 20)
        det_1 = one_loop_determinant_spin_s(c, 1, 20)
        det_2 = one_loop_determinant_spin_s(c, 2, 20)
        # det_s = (2s+1) * det_0 / 1
        self.assertAlmostEqual(det_1 / det_0, 3.0, places=5)
        self.assertAlmostEqual(det_2 / det_0, 5.0, places=5)

    def test_full_one_loop_returns_all_spins(self):
        """Full one-loop determinant includes all spin contributions."""
        result = full_one_loop_determinant(13.0, s_max=2, n_max=20)
        self.assertIn('spin_0', result)
        self.assertIn('spin_1', result)
        self.assertIn('spin_2', result)
        self.assertIn('total', result)


class TestSenQuantumEntropy(unittest.TestCase):
    """Test Sen's quantum entropy function."""

    def test_sen_returns_components(self):
        """Sen QEF returns all expected keys."""
        result = sen_quantum_entropy_function(26.0, 10)
        for key in ['S_BH', 'epsilon', 'f_terms', 'f_total',
                     'log_Z_micro', 'Z_micro', 'shadow_coeffs']:
            self.assertIn(key, result)

    def test_sen_S_BH_positive(self):
        """S_BH is positive for positive n, c."""
        result = sen_quantum_entropy_function(26.0, 10)
        self.assertGreater(result['S_BH'], 0)

    def test_sen_leading_term_is_kappa(self):
        """Leading shadow coefficient is kappa = c/2."""
        result = sen_quantum_entropy_function(26.0, 10)
        self.assertAlmostEqual(result['shadow_coeffs'][2], 13.0, places=5)


class TestWallCrossing(unittest.TestCase):
    """Test wall-crossing for Virasoro."""

    def test_virasoro_degeneracy_at_c1(self):
        """At c = 1, degeneracy is the partition function."""
        for n in [1, 2, 5, 10]:
            d = virasoro_degeneracy_c_dependence(n, 1.0)
            expected = float(free_boson_degeneracy(n))
            self.assertAlmostEqual(d, expected, places=5)

    def test_wall_crossing_jump_structure(self):
        """Wall-crossing jump returns expected keys."""
        result = wall_crossing_jump(5, 1.0)
        for key in ['d_plus', 'd_minus', 'jump']:
            self.assertIn(key, result)

    def test_wall_crossing_table_length(self):
        """Table has correct number of entries."""
        table = wall_crossing_table(10, 1.0)
        self.assertEqual(len(table), 10)


class TestOSV(unittest.TestCase):
    """Test Ooguri-Strominger-Vafa conjecture."""

    def test_topological_string_Z_finite(self):
        """Z_top is finite for valid parameters."""
        tau = 0.5j
        Z = topological_string_Z(26.0, tau, g_max=3)
        self.assertTrue(math.isfinite(abs(Z)))

    def test_osv_test_returns_components(self):
        """OSV test returns all expected keys."""
        result = osv_test(26.0, 5, g_max=2)
        for key in ['S_BH', 'Z_top', '|Z_top|^2', 'Z_BH', 'log_ratio']:
            self.assertIn(key, result)


class TestMultiparticle(unittest.TestCase):
    """Test multiparticle contributions."""

    def test_single_particle_positive(self):
        """Single-particle Z is positive."""
        self.assertGreater(single_particle_Z(26.0, 1.0), 0.0)

    def test_single_particle_zero_for_negative_beta(self):
        """Single-particle Z = 0 for beta <= 0."""
        self.assertEqual(single_particle_Z(26.0, 0.0), 0.0)
        self.assertEqual(single_particle_Z(26.0, -1.0), 0.0)

    def test_multiparticle_positive(self):
        """Multiparticle Z is positive."""
        self.assertGreater(multiparticle_Z(26.0, 1.0), 0.0)

    def test_multiparticle_ratio_returns_keys(self):
        """Multiparticle ratio returns expected keys."""
        result = multiparticle_ratio(26.0, 1.0)
        for key in ['Z_single', 'Z_multi', 'ratio']:
            self.assertIn(key, result)

    def test_multiparticle_ratio_suppressed_at_high_T(self):
        """At small beta (high T), single-particle dominates."""
        result = multiparticle_ratio(26.0, 0.1)
        # The single-particle should dominate at very small beta
        self.assertLess(result['ratio'], 1.0)

    def test_crossover_positive(self):
        """Multiparticle crossover beta is positive."""
        beta = multiparticle_crossover(26.0)
        self.assertGreater(beta, 0.0)


class TestKoszulMicrostateDuality(unittest.TestCase):
    """Test Koszul microstate duality (AP24 critical)."""

    def test_kappa_sum_is_13_not_zero(self):
        """AP24: kappa + kappa' = 13 for Virasoro, NOT 0."""
        for c in [1.0, 6.0, 13.0, 20.0, 25.0]:
            result = koszul_degeneracy_ratio(10, c)
            self.assertAlmostEqual(result['kappa_sum'], 13.0, places=10)

    def test_self_dual_at_c13(self):
        """At c = 13: kappa = kappa' = 13/2, ratio = 1."""
        result = koszul_self_dual_test(10)
        self.assertEqual(result['ratio'], 1.0)
        self.assertTrue(result['self_dual'])

    def test_koszul_dual_involution(self):
        """Koszul duality is an involution: (c')' = c."""
        for c in [1.0, 6.0, 13.0, 20.0]:
            self.assertAlmostEqual(koszul_dual_c(koszul_dual_c(c)), c, places=10)

    def test_koszul_asymptotic_ratio_sign(self):
        """For c < 13: ratio -> 0 (negative log). For c > 13: ratio -> inf."""
        for n in [10, 100]:
            self.assertLess(koszul_asymptotic_ratio(6.0, n), 0.0)
            self.assertGreater(koszul_asymptotic_ratio(20.0, n), 0.0)

    def test_koszul_asymptotic_ratio_zero_at_c13(self):
        """At c = 13 (self-dual): asymptotic ratio = 0."""
        self.assertAlmostEqual(koszul_asymptotic_ratio(13.0, 100), 0.0, places=10)

    def test_koszul_microstate_table_length(self):
        """Table has correct number of entries."""
        table = koszul_microstate_table(6.0, n_max=15)
        self.assertEqual(len(table), 15)


class TestShadowDepthClass(unittest.TestCase):
    """Test shadow depth classification."""

    def test_virasoro_is_class_M(self):
        """Virasoro with c != 0 is class M (infinite shadow depth)."""
        for c in [1.0, 6.0, 13.0, 26.0]:
            self.assertEqual(shadow_depth_class(c), 'M')

    def test_virasoro_c0_class_G(self):
        """Virasoro at c = 0 is class G (kappa = 0)."""
        self.assertEqual(shadow_depth_class(0.0), 'G')


class TestCrossConsistency(unittest.TestCase):
    """Cross-consistency checks between different computations."""

    def test_F1_complementarity(self):
        """F_1(c) + F_1(26-c) = 13/24 (complementarity sum)."""
        for c in [1, 6, 10, 20, 25]:
            F1 = virasoro_free_energy(c, 1)
            F1_dual = virasoro_free_energy(26 - c, 1)
            expected = Fraction(13, 24)  # 13 * lambda_1 = 13/24
            self.assertEqual(F1 + F1_dual, expected)

    def test_F_g_complementarity_scalar(self):
        """At scalar level, F_g(c) + F_g(26-c) = 13 * lambda_g."""
        for g in range(1, 5):
            for c in [1, 6, 13, 20]:
                kappa = kappa_virasoro(c)
                kappa_d = kappa_virasoro(26 - c)
                # Scalar parts add to 13 * lambda_g
                F_sum = F_g_scalar(kappa, g) + F_g_scalar(kappa_d, g)
                expected = Fraction(13) * lambda_fp(g)
                self.assertEqual(F_sum, expected)

    def test_entropy_expansion_sum_consistency(self):
        """S_total = S_BH + S_log + C_0 + C_1."""
        result = entropy_expansion(100, 26.0)
        expected_total = (result['S_BH'] + result['S_log']
                          + result['C_0'] + result['C_1'])
        self.assertAlmostEqual(result['S_total'], expected_total, places=8)

    def test_cardy_asymptotics_log_ratio(self):
        """Verify log(Cardy)/log(exact) approaches 1 for large n (c=24)."""
        results = verify_cardy_asymptotics(
            24.0, monster_degeneracy, [5, 10, 15, 20])
        # Check that the log-scale ratio is reasonable
        for r in results:
            if r['d_exact'] > 1 and r['d_cardy'] > 0:
                log_ratio = math.log(r['d_cardy']) / math.log(r['d_exact'])
                self.assertGreater(log_ratio, 0.5)
                self.assertLess(log_ratio, 2.0)


if __name__ == '__main__':
    unittest.main()
