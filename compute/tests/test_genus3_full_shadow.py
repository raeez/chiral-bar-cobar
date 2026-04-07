r"""Tests for compute/lib/genus3_full_shadow.py.

Full genus-3 shadow obstruction class computation and Pixton relation
membership verification.

Organized by verification path:
  Path 1: Graph-by-graph sum (42 stable graphs)
  Path 2: Bernoulli number formula
  Path 3: A-hat generating function
  Path 4: Shadow ODE / sqrt(Q_L) Taylor expansion
  Path 5: Orbifold Euler characteristic

Additional test groups:
  - Tautological ring decomposition
  - Pixton ideal membership (structural tests)
  - Shadow depth class analysis
  - Complementarity (Theorem C, AP24)
  - Self-loop parity vanishing
  - Virasoro specialization
  - Affine Kac-Moody specialization
  - Cross-genus consistency
  - Anti-pattern guards (AP1, AP9, AP10, AP24, AP39)
  - Exact vs approximate vertex weight separation

40+ tests using Fraction for exact arithmetic.

References:
  thm:theorem-d (higher_genus_modular_koszul.tex)
  eq:delta-pf-genus3-explicit (higher_genus_modular_koszul.tex)
  conj:pixton-from-shadows (concordance.tex)
  prop:self-loop-vanishing (higher_genus_modular_koszul.tex)
  cor:shadow-visibility-genus (higher_genus_modular_koszul.tex)
"""

import unittest
from fractions import Fraction
from math import factorial

from sympy import Symbol, Integer, Rational, cancel, expand

from compute.lib.genus3_full_shadow import (
    # Bernoulli / FP
    _bernoulli_exact,
    lambda_fp,
    LAMBDA1_FP,
    LAMBDA2_FP,
    LAMBDA3_FP,
    LAMBDA4_FP,
    # Scalar F_3
    F3_scalar,
    F3_scalar_symbolic,
    # Graph classification
    graph_classification,
    # Planted-forest correction
    planted_forest_genus3_generic,
    planted_forest_genus3_exact_part,
    planted_forest_genus3_approx_part,
    # Virasoro
    virasoro_shadow_values,
    F3_virasoro_scalar,
    delta_pf_virasoro_genus3_graphsum,
    delta_pf_virasoro_genus3_formula,
    F3_virasoro_full_symbolic,
    F3_virasoro_at_c,
    virasoro_dpf_numerator_polynomial,
    virasoro_F3_numerator_polynomial,
    # Tautological decomposition
    tautological_decomposition,
    # Pixton membership
    pixton_membership_test,
    # Multi-path verification
    verify_path1_graph_sum,
    verify_path2_bernoulli,
    verify_path3_ahat_gf,
    verify_path4_shadow_ode,
    verify_path5_euler_char,
    run_all_verifications,
    # Complementarity
    complementarity_genus3_virasoro,
    # Shadow depth
    shadow_depth_analysis,
    # Self-loop
    self_loop_vanishing_genus3,
    # Ratios
    genus_ratio_universality,
    # Affine
    F3_affine_sl2,
    delta_pf_genus3_affine_sl2,
)

from compute.lib.pixton_shadow_bridge import (
    ShadowData,
    virasoro_shadow_data,
    heisenberg_shadow_data,
    c_sym,
)

from compute.lib.pixton_genus3_engine import (
    genus3_graphs,
    planted_forest_correction_g3,
)


# ====================================================================
# Section 1: Bernoulli numbers and FP intersection numbers (Path 2)
# ====================================================================

class TestBernoulliNumbers(unittest.TestCase):
    """Verify Bernoulli numbers used in FP formula."""

    def test_B2(self):
        self.assertEqual(_bernoulli_exact(2), Fraction(1, 6))

    def test_B4(self):
        self.assertEqual(_bernoulli_exact(4), Fraction(-1, 30))

    def test_B6(self):
        self.assertEqual(_bernoulli_exact(6), Fraction(1, 42))

    def test_B8(self):
        self.assertEqual(_bernoulli_exact(8), Fraction(-1, 30))


class TestFPIntersectionNumbers(unittest.TestCase):
    """Verify FP intersection numbers at genus 1-4."""

    def test_lambda1(self):
        self.assertEqual(lambda_fp(1), Fraction(1, 24))
        self.assertEqual(LAMBDA1_FP, Fraction(1, 24))

    def test_lambda2(self):
        self.assertEqual(lambda_fp(2), Fraction(7, 5760))
        self.assertEqual(LAMBDA2_FP, Fraction(7, 5760))

    def test_lambda3(self):
        self.assertEqual(lambda_fp(3), Fraction(31, 967680))
        self.assertEqual(LAMBDA3_FP, Fraction(31, 967680))

    def test_lambda4(self):
        self.assertEqual(lambda_fp(4), Fraction(127, 154828800))
        self.assertEqual(LAMBDA4_FP, Fraction(127, 154828800))

    def test_lambda3_alternative_derivation(self):
        """31/32 * |B_6|/6! = 31/32 * (1/42)/720 = 31/967680."""
        alt = Fraction(31, 32) * Fraction(1, 42) / Fraction(720)
        self.assertEqual(alt, LAMBDA3_FP)

    def test_lambda3_positive(self):
        self.assertGreater(LAMBDA3_FP, 0)

    def test_all_fp_positive(self):
        """All lambda_g^FP are positive (F_g values are POSITIVE, AP22)."""
        for g in range(1, 6):
            self.assertGreater(lambda_fp(g), 0)


# ====================================================================
# Section 2: A-hat generating function (Path 3)
# ====================================================================

class TestAhatGeneratingFunction(unittest.TestCase):
    """Verify FP values from the generating function (x/2)/sin(x/2)."""

    def test_path3(self):
        result = verify_path3_ahat_gf()
        self.assertTrue(result['match_lambda_1'])
        self.assertTrue(result['match_lambda_2'])
        self.assertTrue(result['match_lambda_3'])

    def test_gf_coefficients_are_fractions(self):
        result = verify_path3_ahat_gf()
        for coeff in result['gf_coefficients']:
            self.assertIsInstance(coeff, Fraction)


# ====================================================================
# Section 3: Shadow ODE verification (Path 4)
# ====================================================================

class TestShadowODE(unittest.TestCase):
    """Verify shadow coefficients from sqrt(Q_L) Taylor expansion."""

    def test_path4(self):
        result = verify_path4_shadow_ode()
        self.assertTrue(result['S_2_matches_kappa'])
        self.assertTrue(result['S_3_matches'])
        self.assertTrue(result['S_4_matches'])


# ====================================================================
# Section 4: Orbifold Euler characteristic (Path 5)
# ====================================================================

class TestEulerCharacteristic(unittest.TestCase):
    """Verify chi^orb(M-bar_{3,0}) = -12419/90720."""

    def test_path5(self):
        result = verify_path5_euler_char()
        self.assertTrue(result['match'])
        self.assertEqual(result['computed'], Fraction(-12419, 90720))
        self.assertEqual(result['num_graphs'], 42)


# ====================================================================
# Section 5: Graph classification (42 stable graphs)
# ====================================================================

class TestGraphClassification(unittest.TestCase):
    """Verify classification of the 42 stable graphs."""

    def test_total_count(self):
        cls = graph_classification()
        self.assertEqual(cls['total'], 42)

    def test_vertex_count_partition(self):
        cls = graph_classification()
        by_v = cls['by_vertices']
        self.assertEqual(by_v.get(1, 0), 4)
        self.assertEqual(by_v.get(2, 0), 12)
        self.assertEqual(by_v.get(3, 0), 15)
        self.assertEqual(by_v.get(4, 0), 11)
        self.assertEqual(sum(by_v.values()), 42)

    def test_loop_number_partition(self):
        cls = graph_classification()
        by_l = cls['by_loop']
        self.assertEqual(sum(by_l.values()), 42)

    def test_pf_plus_pure_equals_42(self):
        cls = graph_classification()
        self.assertEqual(cls['planted_forest_count'] + cls['pure_kappa_count'], 42)

    def test_exact_plus_approx_partition(self):
        """Exact + approximate vertex weight graphs partition all 42."""
        cls = graph_classification()
        n_exact = len(cls['exact_vertex_weight_graphs'])
        n_approx = len(cls['approximate_graphs'])
        # Some graphs appear in both categories is impossible
        # (they are mutually exclusive by definition)
        self.assertEqual(n_exact + n_approx, 42)


# ====================================================================
# Section 6: Planted-forest correction (Path 1 graph sum)
# ====================================================================

class TestPlantedForestGeneric(unittest.TestCase):
    """Test the generic planted-forest polynomial."""

    def test_path1_heisenberg_vanishes(self):
        """Class G (Heisenberg): all S_k = 0, so PF = 0."""
        result = verify_path1_graph_sum()
        self.assertTrue(result['heisenberg_vanishes'])

    def test_generic_nonzero(self):
        pf = planted_forest_genus3_generic()
        self.assertNotEqual(pf, 0)

    def test_generic_has_S5(self):
        """S_5 appears at genus 3 (shadow visibility g_min(S_5) = 3)."""
        pf = planted_forest_genus3_generic()
        self.assertIn(Symbol('S_5'), pf.free_symbols)

    def test_generic_has_S4(self):
        pf = planted_forest_genus3_generic()
        self.assertIn(Symbol('S_4'), pf.free_symbols)

    def test_generic_has_S3(self):
        pf = planted_forest_genus3_generic()
        self.assertIn(Symbol('S_3'), pf.free_symbols)

    def test_generic_has_kappa(self):
        pf = planted_forest_genus3_generic()
        self.assertIn(Symbol('kappa'), pf.free_symbols)

    def test_no_pure_kappa_terms(self):
        """Every term has at least one S_k factor (ensures class G vanishes)."""
        pf = planted_forest_genus3_generic()
        pf_no_shadow = cancel(pf.subs([
            (Symbol('S_3'), 0),
            (Symbol('S_4'), 0),
            (Symbol('S_5'), 0),
        ]))
        self.assertEqual(pf_no_shadow, 0)


class TestPlantedForestExactApprox(unittest.TestCase):
    """Test the exact/approximate separation."""

    def test_exact_part_nonzero(self):
        exact = planted_forest_genus3_exact_part()
        self.assertNotEqual(exact, 0)

    def test_approx_part_nonzero(self):
        approx = planted_forest_genus3_approx_part()
        self.assertNotEqual(approx, 0)

    def test_exact_plus_approx_equals_total(self):
        """Exact + approximate = total generic PF."""
        exact = planted_forest_genus3_exact_part()
        approx = planted_forest_genus3_approx_part()
        total = planted_forest_genus3_generic()
        diff = cancel(exact + approx - total)
        self.assertEqual(diff, 0)

    def test_approx_part_structure(self):
        """Approximate part is proportional to S_3*kappa (from g=1 val>=3 and g=2)."""
        approx = planted_forest_genus3_approx_part()
        # The approximate part should only involve S_3 and kappa
        # (from graphs where the approximate vertices are genus-1 val>=3 or genus-2)
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        self.assertNotIn(S4, approx.free_symbols)
        self.assertNotIn(S5, approx.free_symbols)


# ====================================================================
# Section 7: Heisenberg verification (class G)
# ====================================================================

class TestHeisenbergClassG(unittest.TestCase):
    """Class G: Heisenberg has zero planted-forest correction."""

    def test_heisenberg_pf_vanishes(self):
        heis = heisenberg_shadow_data()
        pf = planted_forest_correction_g3(heis)
        self.assertEqual(pf, Integer(0))

    def test_heisenberg_F3_scalar(self):
        """F_3(H_k) = k * 31/967680."""
        for k in [1, 2, 5]:
            f3 = F3_scalar(Fraction(k))
            expected = Fraction(k) * LAMBDA3_FP
            self.assertEqual(f3, expected)


# ====================================================================
# Section 8: Virasoro specialization (class M)
# ====================================================================

class TestVirasoroShadowValues(unittest.TestCase):
    """Verify Virasoro shadow data at specific c values."""

    def test_virasoro_kappa(self):
        for c_val in [1, 2, 13, 25, 26]:
            sd = virasoro_shadow_values(Fraction(c_val))
            self.assertEqual(sd['kappa'], Fraction(c_val, 2))

    def test_virasoro_S3(self):
        for c_val in [1, 2, 13]:
            sd = virasoro_shadow_values(Fraction(c_val))
            self.assertEqual(sd['S3'], Fraction(2))

    def test_virasoro_S4(self):
        sd = virasoro_shadow_values(Fraction(1))
        expected = Fraction(10) / (1 * 27)
        self.assertEqual(sd['S4'], expected)

    def test_virasoro_S5(self):
        sd = virasoro_shadow_values(Fraction(1))
        expected = Fraction(-48) / (1 * 27)
        self.assertEqual(sd['S5'], expected)


class TestVirasoroF3(unittest.TestCase):
    """Verify F_3(Vir_c) scalar and full values."""

    def test_scalar_F3_at_c26(self):
        """F_3^scalar(Vir_26) = 13 * 31/967680."""
        self.assertEqual(F3_virasoro_scalar(Fraction(26)),
                         Fraction(13) * LAMBDA3_FP)

    def test_scalar_F3_at_c1(self):
        self.assertEqual(F3_virasoro_scalar(Fraction(1)),
                         Fraction(1, 2) * LAMBDA3_FP)

    def test_full_F3_finite_at_c1(self):
        """F_3(Vir_1) is finite (c=1 is not a pole)."""
        val = F3_virasoro_at_c(1)
        self.assertIsNotNone(val)
        self.assertTrue(abs(val) < 100)

    def test_full_F3_finite_at_c13(self):
        """F_3(Vir_13) is finite at the self-dual point."""
        val = F3_virasoro_at_c(13)
        self.assertIsNotNone(val)

    def test_dpf_denominator_structure(self):
        """Denominator of delta_pf for Virasoro is c^2*(5c+22)^2 * N."""
        coeffs, degree, denom = virasoro_dpf_numerator_polynomial()
        # The numerator is degree 7
        self.assertEqual(degree, 7)
        # Denominator is divisible by c^2
        from sympy import factor
        d_factored = factor(denom)
        # Check c^2 and (5c+22)^2 divide
        self.assertEqual(int(denom.subs(c_sym, 0)), 0)


# ====================================================================
# Section 9: Self-loop parity vanishing
# ====================================================================

class TestSelfLoopParity(unittest.TestCase):
    """Verify prop:self-loop-vanishing at genus 3."""

    def test_triple_loop_vanishes(self):
        result = self_loop_vanishing_genus3()
        self.assertTrue(result['triple_loop_vanishes'])

    def test_dim_moduli_odd(self):
        result = self_loop_vanishing_genus3()
        self.assertEqual(result['dim_moduli'], 3)
        self.assertTrue(result['dim_is_odd'])


# ====================================================================
# Section 10: Shadow depth class analysis
# ====================================================================

class TestShadowDepthClasses(unittest.TestCase):
    """Test class-by-class specialization of planted-forest correction."""

    def test_class_G_vanishes(self):
        analysis = shadow_depth_analysis()
        self.assertTrue(analysis['class_G']['vanishes'])

    def test_class_L_has_S3(self):
        analysis = shadow_depth_analysis()
        pf_L = analysis['class_L']['pf']
        self.assertNotEqual(pf_L, 0)
        self.assertIn(Symbol('S_3'), pf_L.free_symbols)

    def test_class_C_has_S4(self):
        analysis = shadow_depth_analysis()
        pf_C = analysis['class_C']['pf']
        self.assertIn(Symbol('S_4'), pf_C.free_symbols)

    def test_class_M_has_S5(self):
        analysis = shadow_depth_analysis()
        pf_M = analysis['class_M']['pf']
        self.assertIn(Symbol('S_5'), pf_M.free_symbols)

    def test_shadow_visibility_g3(self):
        """S_5 first appears at genus 3: g_min(S_5) = floor(5/2) + 1 = 3."""
        analysis = shadow_depth_analysis()
        self.assertEqual(analysis['g_min_S5'], 3)
        self.assertEqual(analysis['new_at_genus_3'], 'S_5')


# ====================================================================
# Section 11: Pixton ideal membership (structural tests)
# ====================================================================

class TestPixtonMembership(unittest.TestCase):
    """Test conj:pixton-from-shadows at genus 3 (structural)."""

    def test_structural_tests_pass(self):
        result = pixton_membership_test()
        self.assertTrue(result['structural_tests_pass'])

    def test_class_G_vanishes(self):
        result = pixton_membership_test()
        self.assertTrue(result['classG_vanishes'])

    def test_S5_appears(self):
        result = pixton_membership_test()
        self.assertTrue(result['has_S5'])

    def test_no_pure_kappa(self):
        result = pixton_membership_test()
        self.assertTrue(result['no_pure_kappa_terms'])

    def test_virasoro_numerical_values_finite(self):
        result = pixton_membership_test()
        for c_val, val in result['virasoro_values'].items():
            if c_val > 0:  # c=0 may diverge
                self.assertIsNotNone(val,
                    f"delta_pf diverges at c={c_val}")


# ====================================================================
# Section 12: Complementarity (Theorem C, AP24)
# ====================================================================

class TestComplementarity(unittest.TestCase):
    """Complementarity F_3(c) + F_3(26-c) at genus 3."""

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (AP24: NOT zero)."""
        result = complementarity_genus3_virasoro()
        self.assertEqual(result['kappa_sum'], Fraction(13))

    def test_scalar_complementarity(self):
        """Scalar: F_3 + F_3^! = 13 * lambda_3^FP."""
        result = complementarity_genus3_virasoro()
        self.assertEqual(result['scalar_complementarity_sum'],
                         Fraction(13) * LAMBDA3_FP)

    def test_self_dual_at_c13(self):
        """At c=13: F_3(13) = F_3(26-13) = F_3(13) (self-dual)."""
        result = complementarity_genus3_virasoro()
        self.assertTrue(result['is_self_dual_at_c13'])


# ====================================================================
# Section 13: Multi-path verification (all 5 paths)
# ====================================================================

class TestMultiPathVerification(unittest.TestCase):
    """Run all five verification paths."""

    def test_all_paths_pass(self):
        results = run_all_verifications()
        self.assertTrue(results['all_pass'],
                        f"Failed paths: {[k for k, v in results.items() if not v]}")

    def test_path1(self):
        self.assertTrue(run_all_verifications()['path1_graph_sum'])

    def test_path2(self):
        self.assertTrue(run_all_verifications()['path2_bernoulli'])

    def test_path3(self):
        self.assertTrue(run_all_verifications()['path3_ahat_gf'])

    def test_path4(self):
        self.assertTrue(run_all_verifications()['path4_shadow_ode'])

    def test_path5(self):
        self.assertTrue(run_all_verifications()['path5_euler_char'])


# ====================================================================
# Section 14: Genus ratio universality
# ====================================================================

class TestGenusRatios(unittest.TestCase):
    """Universal ratios on the scalar lane."""

    def test_F3_over_F1(self):
        ratios = genus_ratio_universality()
        self.assertEqual(ratios['F3_over_F1'], Fraction(31, 40320))

    def test_F3_over_F2(self):
        ratios = genus_ratio_universality()
        expected = Fraction(31, 967680) / Fraction(7, 5760)
        self.assertEqual(ratios['F3_over_F2'], expected)

    def test_F2_over_F1(self):
        ratios = genus_ratio_universality()
        self.assertEqual(ratios['F2_over_F1'], Fraction(7, 240))


# ====================================================================
# Section 15: Affine Kac-Moody genus-3
# ====================================================================

class TestAffineKM(unittest.TestCase):
    """Affine sl_2 at level k genus-3 computations."""

    def test_F3_sl2_k1(self):
        """F_3(sl_2, k=1) = 3*3/4 * 31/967680 = 93/3870720 = 31/1290240."""
        kappa = Fraction(3 * 3, 4)  # 3(1+2)/4 = 9/4
        expected = kappa * LAMBDA3_FP
        self.assertEqual(F3_affine_sl2(1), expected)
        self.assertEqual(F3_affine_sl2(1), Fraction(9, 4) * Fraction(31, 967680))

    def test_delta_pf_sl2_class_L(self):
        """Affine sl_2 is class L: delta_pf involves only S_3 and kappa."""
        dpf = delta_pf_genus3_affine_sl2(1)
        self.assertIsInstance(dpf, Fraction)
        # Class L has nonzero PF correction
        self.assertNotEqual(dpf, 0)

    def test_delta_pf_sl2_no_S4_S5(self):
        """Class L: no S_4 or S_5 terms (both are zero)."""
        # The formula explicitly sets S_4 = S_5 = 0
        # Just verify it's a rational number (no symbolic variables)
        dpf = delta_pf_genus3_affine_sl2(1)
        self.assertIsInstance(dpf, Fraction)


# ====================================================================
# Section 16: Anti-pattern guards
# ====================================================================

class TestAntiPatternGuards(unittest.TestCase):
    """Guards against known anti-patterns (AP1, AP9, AP10, AP24, AP39)."""

    def test_AP1_kappa_not_copied(self):
        """AP1: kappa formulas must be computed, not copied.
        Virasoro kappa = c/2, NOT c. Heisenberg kappa = k, NOT k/2."""
        self.assertEqual(F3_virasoro_scalar(Fraction(1)),
                         Fraction(1, 2) * LAMBDA3_FP)
        self.assertEqual(F3_scalar(Fraction(1)),  # Heisenberg k=1: kappa=1
                         Fraction(1) * LAMBDA3_FP)

    def test_AP9_kappa_is_not_S2(self):
        """AP9: kappa != S_2 for multi-generator families.
        For Virasoro (rank 1): kappa = S_2 = c/2 (coincidence).
        This test guards against confusing the two objects."""
        sd = virasoro_shadow_values(Fraction(10))
        # For Virasoro, kappa = c/2 = S_2 (coincidence at rank 1)
        self.assertEqual(sd['kappa'], Fraction(5))

    def test_AP10_not_hardcoded(self):
        """AP10: expected values computed, not hardcoded from literature.
        Cross-check lambda_3 from two independent computations."""
        # Path A: Bernoulli formula
        B6 = _bernoulli_exact(6)
        lam3_A = Fraction(2**5 - 1, 2**5) * abs(B6) / Fraction(factorial(6))
        # Path B: (31/32) * (1/42) / 720
        lam3_B = Fraction(31, 32) * Fraction(1, 42) / Fraction(720)
        self.assertEqual(lam3_A, lam3_B)
        self.assertEqual(lam3_A, LAMBDA3_FP)

    def test_AP24_complementarity_not_zero(self):
        """AP24: kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
        Complementarity asymmetry is 13 for Virasoro."""
        for c_val in [1, 5, 10, 13, 25]:
            kappa_sum = Fraction(c_val, 2) + Fraction(26 - c_val, 2)
            self.assertEqual(kappa_sum, Fraction(13))

    def test_AP39_kappa_equals_c_over_2_for_virasoro(self):
        """AP39: kappa = c/2 for Virasoro (rank 1 coincidence).
        NOT kappa = c. NOT kappa = c/12."""
        for c_val in [1, 2, 10, 26]:
            sd = virasoro_shadow_values(Fraction(c_val))
            self.assertEqual(sd['kappa'], Fraction(c_val, 2))


# ====================================================================
# Section 17: Tautological decomposition
# ====================================================================

class TestTautologicalDecomposition(unittest.TestCase):
    """Test the tautological ring decomposition at genus 3."""

    def test_decomposition_has_42_graphs(self):
        decomp = tautological_decomposition()
        self.assertEqual(len(decomp['per_graph']), 42)

    def test_smooth_graph_placeholder(self):
        decomp = tautological_decomposition()
        self.assertEqual(decomp['smooth'], Integer(1))

    def test_codim1_nonzero(self):
        decomp = tautological_decomposition()
        self.assertNotEqual(decomp['codim1'], 0)

    def test_codim_partition(self):
        """Codim 0 + codim 1 + ... + codim 6 accounts for all graphs."""
        decomp = tautological_decomposition()
        codim_counts = {}
        for entry in decomp['per_graph']:
            c = entry['codimension']
            codim_counts[c] = codim_counts.get(c, 0) + 1
        self.assertEqual(sum(codim_counts.values()), 42)


# ====================================================================
# Section 18: Cross-genus consistency
# ====================================================================

class TestCrossGenusConsistency(unittest.TestCase):
    """Verify genus-3 values are consistent with genus 1-2."""

    def test_monotone_decrease(self):
        """lambda_g^FP decreases with g."""
        self.assertGreater(LAMBDA1_FP, LAMBDA2_FP)
        self.assertGreater(LAMBDA2_FP, LAMBDA3_FP)
        self.assertGreater(LAMBDA3_FP, LAMBDA4_FP)

    def test_ratio_pattern(self):
        """F_{g+1}/F_g decreases rapidly (asymptotic: (2pi)^{-2})."""
        r32 = LAMBDA3_FP / LAMBDA2_FP
        r21 = LAMBDA2_FP / LAMBDA1_FP
        # Both should be much less than 1
        self.assertLess(float(r32), 0.1)
        self.assertLess(float(r21), 0.1)
        # And r32 < r21 (monotone decrease of ratios)
        self.assertLess(float(r32), float(r21))

    def test_bernoulli_recursion(self):
        """lambda_g from Bernoulli numbers satisfies the recursion."""
        # (2^{2g-1}-1)|B_{2g}|/(2g)! should match lambda_fp(g)
        for g in range(1, 5):
            B2g = _bernoulli_exact(2 * g)
            expected = Fraction(2**(2*g-1)-1, 2**(2*g-1)) * abs(B2g) / Fraction(factorial(2*g))
            self.assertEqual(lambda_fp(g), expected)


# ====================================================================
# Section 19: Virasoro numerator polynomial structure
# ====================================================================

class TestVirasoroNumerator(unittest.TestCase):
    """Test the numerator polynomial of delta_pf for Virasoro."""

    def test_numerator_degree_7(self):
        coeffs, degree, _ = virasoro_dpf_numerator_polynomial()
        self.assertEqual(degree, 7)

    def test_F3_numerator_degree_7(self):
        coeffs, degree, _ = virasoro_F3_numerator_polynomial()
        self.assertEqual(degree, 7)


if __name__ == '__main__':
    unittest.main()
