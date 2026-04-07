r"""Tests for theorem_tau_shadow_kw_engine.py.

70+ tests verifying the theorem tau_shadow = tau_KW^kappa from four
independent proofs, with scope checks and negative results.

THEOREM: For uniform-weight chirally Koszul algebras,
    tau_shadow(A) = tau_KW^{kappa(A)}.

FOUR PROOFS:
  1. Generating function identity (algebraic)
  2. MC equation scalar projection (bar-intrinsic)
  3. Hodge bundle / intersection theory (geometric)
  4. Kontsevich matrix model (analytic)

SCOPE CHECKS:
  - Uniform-weight: PASSES at all genera
  - Multi-weight (W_3): FAILS at genus >= 2
  - Genus 1: UNIVERSAL (all families)
  - kappa = 0: trivial (tau = 1)
  - kappa = 1: recovers tau_KW

NEGATIVE RESULTS:
  - tau_KW^kappa does NOT satisfy KdV for kappa != 0, 1
  - The shadow partition function is NOT a KdV tau-function

MULTI-PATH VERIFICATION:
  Every numerical value verified by at least 3 independent paths.
  Exact arithmetic (sympy Rational) throughout.

Ground truth:
  thm:theorem-d (higher_genus_modular_koszul.tex)
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
  FP03: Faber-Pandharipande, Ann. Math. 157 (2003), 97-124.
  Kon92: Kontsevich, Comm. Math. Phys. 147 (1992), 1-23.
"""

import unittest
from sympy import Rational, factorial, bernoulli, pi, sin, Symbol, series

from compute.lib.theorem_tau_shadow_kw_engine import (
    # Core functions
    lambda_fp,
    shadow_free_energy,
    _bernoulli_number,
    # Proof 1
    ahat_generating_function,
    shadow_generating_function,
    kw_generating_function,
    proof1_generating_function_identity,
    # Proof 2
    proof2_mc_scalar_projection,
    # Proof 3
    hodge_lambda_integral,
    mumford_formula_c1,
    proof3_hodge_bundle,
    # Proof 4
    kontsevich_matrix_integral_asymptotic,
    proof4_matrix_model,
    # Cross-proof
    verify_all_four_proofs,
    # Scope
    multi_weight_failure_genus2_w3,
    genus1_universality,
    # KdV
    kdv_compatibility_check,
    # Virasoro constraints
    free_energy_virasoro_constraints,
    # Convergence
    convergence_radius_shadow,
    # Families
    standard_family_verification_table,
    kappa_zero_degenerate_case,
    kappa_one_recovers_kw,
    # Complementarity
    complementarity_tau_functions,
)


# ====================================================================
# Section 1: Faber-Pandharipande numbers (10 tests)
# ====================================================================

class TestFaberPandharipande(unittest.TestCase):
    """Faber-Pandharipande intersection numbers lambda_g^FP."""

    def test_lambda1_value(self):
        """lambda_1^FP = 1/24."""
        self.assertEqual(lambda_fp(1), Rational(1, 24))

    def test_lambda2_value(self):
        """lambda_2^FP = 7/5760."""
        self.assertEqual(lambda_fp(2), Rational(7, 5760))

    def test_lambda3_value(self):
        """lambda_3^FP = 31/967680."""
        self.assertEqual(lambda_fp(3), Rational(31, 967680))

    def test_lambda4_value(self):
        """lambda_4^FP = 127/154828800."""
        self.assertEqual(lambda_fp(4), Rational(127, 154828800))

    def test_lambda5_value(self):
        """lambda_5^FP = 73/3503554560."""
        self.assertEqual(lambda_fp(5), Rational(73, 3503554560))

    def test_all_positive(self):
        """lambda_g^FP > 0 for all g >= 1."""
        for g in range(1, 12):
            self.assertGreater(lambda_fp(g), 0, f"lambda_{g}^FP should be positive")

    def test_generating_function_match(self):
        """lambda_g^FP matches coefficients of (x/2)/sin(x/2) - 1."""
        x = Symbol('x')
        gf = series(x / 2 / sin(x / 2) - 1, x, 0, 20)
        for g in range(1, 9):
            self.assertEqual(
                Rational(gf.coeff(x, 2 * g)), lambda_fp(g),
                f"GF mismatch at genus {g}"
            )

    def test_bernoulli_formula(self):
        """lambda_g^FP = (2^{2g-1}-1)/2^{2g-1} * |B_{2g}|/(2g)!."""
        for g in range(1, 10):
            B2g = abs(_bernoulli_number(2 * g))
            expected = (2**(2*g-1) - 1) * B2g / (2**(2*g-1) * factorial(2*g))
            self.assertEqual(lambda_fp(g), expected, f"Formula mismatch at genus {g}")

    def test_invalid_genus_raises(self):
        """lambda_fp(0) should raise ValueError."""
        with self.assertRaises(ValueError):
            lambda_fp(0)

    def test_ratio_convergence(self):
        """Ratio lambda_{g+1}/lambda_g -> 1/(4*pi^2) as g -> infinity."""
        # Check that ratio is decreasing and approaching 1/(4*pi^2) ~ 0.02533
        target = 1.0 / (4 * float(pi)**2)
        for g in range(5, 10):
            ratio = float(lambda_fp(g + 1) / lambda_fp(g))
            self.assertAlmostEqual(ratio, target, places=1,
                                   msg=f"Ratio at g={g} not approaching limit")


# ====================================================================
# Section 2: Proof 1 -- Generating function identity (8 tests)
# ====================================================================

class TestProof1GeneratingFunction(unittest.TestCase):
    """Proof 1: tau_shadow = tau_KW^kappa via generating functions."""

    def test_proof1_virasoro_c10(self):
        """Proof 1 passes for Virasoro c=10 (kappa=5)."""
        result = proof1_generating_function_identity(5, g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof1_heisenberg_k7(self):
        """Proof 1 passes for Heisenberg k=7."""
        result = proof1_generating_function_identity(7, g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof1_half_integer_kappa(self):
        """Proof 1 passes for kappa = 3/2 (Virasoro c=3)."""
        result = proof1_generating_function_identity(Rational(3, 2), g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof1_kappa_one(self):
        """Proof 1 at kappa=1: shadow = KW."""
        result = proof1_generating_function_identity(1, g_max=8)
        self.assertTrue(result['all_match'])
        for g in range(1, 9):
            self.assertEqual(
                result['details'][g]['F_g_shadow'], lambda_fp(g)
            )

    def test_proof1_four_paths_agree(self):
        """All four paths in Proof 1 give the same result."""
        result = proof1_generating_function_identity(Rational(13, 2), g_max=6)
        for g in range(1, 7):
            d = result['details'][g]
            self.assertTrue(d['all_four_match'], f"Four paths disagree at genus {g}")

    def test_shadow_gf_is_kappa_times_kw_gf(self):
        """shadow_generating_function = kappa * kw_generating_function."""
        kappa = Rational(7, 3)
        x = Symbol('x')
        sgf = shadow_generating_function(kappa, x, 16)
        kgf = kw_generating_function(x, 16)
        diff = series(sgf - kappa * kgf, x, 0, 16)
        # All coefficients should be zero
        for k in range(2, 16):
            self.assertEqual(Rational(diff.coeff(x, k)), 0,
                             f"Coefficient mismatch at x^{k}")

    def test_ahat_gf_starts_at_x2(self):
        """A-hat(ix) - 1 has no constant or x^1 term."""
        x = Symbol('x')
        gf = ahat_generating_function(x, 10)
        self.assertEqual(Rational(gf.coeff(x, 0)), 0)
        self.assertEqual(Rational(gf.coeff(x, 1)), 0)

    def test_ahat_gf_leading_term(self):
        """Leading term of A-hat(ix) - 1 is x^2/24."""
        x = Symbol('x')
        gf = ahat_generating_function(x, 10)
        self.assertEqual(Rational(gf.coeff(x, 2)), Rational(1, 24))


# ====================================================================
# Section 3: Proof 2 -- MC scalar projection (7 tests)
# ====================================================================

class TestProof2MCProjection(unittest.TestCase):
    """Proof 2: MC element scalar projection."""

    def test_proof2_kappa5(self):
        """Proof 2 passes for kappa=5."""
        result = proof2_mc_scalar_projection(5, g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof2_kappa_half(self):
        """Proof 2 passes for kappa=1/2 (Virasoro c=1)."""
        result = proof2_mc_scalar_projection(Rational(1, 2), g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof2_three_paths_genus1(self):
        """Three paths agree at genus 1 for kappa=3."""
        result = proof2_mc_scalar_projection(3, g_max=1)
        d = result['details'][1]
        self.assertEqual(d['path_a'], d['path_b'])
        self.assertEqual(d['path_b'], d['path_c'])

    def test_proof2_genus1_graph_sum(self):
        """Genus-1 graph sum: F_1 = kappa/24."""
        kappa = Rational(7)
        result = proof2_mc_scalar_projection(kappa, g_max=1)
        self.assertEqual(result['details'][1]['path_b'], kappa / 24)

    def test_proof2_genus2_graph_sum(self):
        """Genus-2 graph sum: F_2 = kappa * 7/5760."""
        kappa = Rational(3)
        result = proof2_mc_scalar_projection(kappa, g_max=2)
        self.assertEqual(result['details'][2]['path_b'], kappa * Rational(7, 5760))

    def test_proof2_large_kappa(self):
        """Proof 2 passes for large kappa=100."""
        result = proof2_mc_scalar_projection(100, g_max=5)
        self.assertTrue(result['all_match'])

    def test_proof2_negative_kappa(self):
        """Proof 2 passes for negative kappa=-3 (Feigin-Frenkel dual)."""
        result = proof2_mc_scalar_projection(-3, g_max=5)
        self.assertTrue(result['all_match'])


# ====================================================================
# Section 4: Proof 3 -- Hodge bundle (7 tests)
# ====================================================================

class TestProof3HodgeBundle(unittest.TestCase):
    """Proof 3: Hodge bundle / intersection theory."""

    def test_proof3_kappa5(self):
        """Proof 3 passes for kappa=5."""
        result = proof3_hodge_bundle(5, g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof3_kappa_half(self):
        """Proof 3 passes for kappa=1/2."""
        result = proof3_hodge_bundle(Rational(1, 2), g_max=8)
        self.assertTrue(result['all_match'])

    def test_hodge_integral_equals_lambda_fp(self):
        """hodge_lambda_integral(g) = lambda_fp(g) for all g."""
        for g in range(1, 10):
            self.assertEqual(hodge_lambda_integral(g), lambda_fp(g))

    def test_mumford_formula_weight1(self):
        """Mumford formula at weight 1: c_1(E_1) = lambda_1."""
        result = mumford_formula_c1(1)
        self.assertIn('lambda_1', result)

    def test_proof3_three_paths_agree(self):
        """Three paths in Proof 3 agree for kappa=13/2."""
        result = proof3_hodge_bundle(Rational(13, 2), g_max=6)
        for g in range(1, 7):
            d = result['details'][g]
            self.assertTrue(d['match'], f"Paths disagree at genus {g}")

    def test_proof3_bernoulli_path(self):
        """The Bernoulli formula path gives correct F_g."""
        kappa = Rational(5)
        result = proof3_hodge_bundle(kappa, g_max=5)
        for g in range(1, 6):
            self.assertEqual(
                result['details'][g]['bernoulli_formula'],
                kappa * lambda_fp(g)
            )

    def test_proof3_negative_kappa(self):
        """Proof 3 passes for negative kappa."""
        result = proof3_hodge_bundle(-7, g_max=5)
        self.assertTrue(result['all_match'])


# ====================================================================
# Section 5: Proof 4 -- Matrix model (7 tests)
# ====================================================================

class TestProof4MatrixModel(unittest.TestCase):
    """Proof 4: Kontsevich matrix model."""

    def test_proof4_kappa5(self):
        """Proof 4 passes for kappa=5."""
        result = proof4_matrix_model(5, g_max=8)
        self.assertTrue(result['all_match'])

    def test_proof4_kappa1_recovers_kw(self):
        """Proof 4 at kappa=1: kappa copies = 1 copy = KW."""
        result = proof4_matrix_model(1, g_max=8)
        for g in range(1, 9):
            self.assertEqual(
                result['details'][g]['kappa_copies'], lambda_fp(g)
            )

    def test_kontsevich_asymptotic_equals_lambda_fp(self):
        """Kontsevich matrix integral asymptotic = lambda_g^FP."""
        for g in range(1, 10):
            self.assertEqual(kontsevich_matrix_integral_asymptotic(g), lambda_fp(g))

    def test_proof4_three_paths_agree(self):
        """Three paths in Proof 4 agree."""
        result = proof4_matrix_model(Rational(9, 4), g_max=6)
        for g in range(1, 7):
            d = result['details'][g]
            self.assertTrue(d['match'], f"Paths disagree at genus {g}")

    def test_proof4_kdv_negative_result(self):
        """Proof 4 reports KdV non-compatibility."""
        result = proof4_matrix_model(5, g_max=3)
        self.assertIn('NOT satisfy KdV', result['kdv_negative_result'])

    def test_proof4_integer_kappa_literal(self):
        """For integer kappa: kappa copies of Kontsevich integral."""
        for n in range(1, 6):
            result = proof4_matrix_model(n, g_max=5)
            self.assertTrue(result['all_match'], f"Failed for kappa={n}")

    def test_proof4_rational_kappa(self):
        """For rational kappa: polynomial interpolation."""
        result = proof4_matrix_model(Rational(7, 3), g_max=5)
        self.assertTrue(result['all_match'])


# ====================================================================
# Section 6: Cross-proof consistency (5 tests)
# ====================================================================

class TestCrossProofConsistency(unittest.TestCase):
    """Cross-proof consistency: all four proofs give the same answer."""

    def test_cross_consistency_kappa5(self):
        """All four proofs agree for kappa=5."""
        result = verify_all_four_proofs(5, g_max=6)
        self.assertTrue(result['all_proofs_ok'])
        self.assertTrue(result['cross_consistent'])

    def test_cross_consistency_kappa_half(self):
        """All four proofs agree for kappa=1/2."""
        result = verify_all_four_proofs(Rational(1, 2), g_max=6)
        self.assertTrue(result['all_proofs_ok'])
        self.assertTrue(result['cross_consistent'])

    def test_cross_consistency_virasoro_c13(self):
        """All four proofs agree for Virasoro c=13 (self-dual, kappa=13/2)."""
        result = verify_all_four_proofs(Rational(13, 2), g_max=6)
        self.assertTrue(result['all_proofs_ok'])
        self.assertTrue(result['cross_consistent'])

    def test_cross_consistency_affine_sl2(self):
        """All four proofs agree for affine sl_2 at k=1 (kappa=9/4)."""
        result = verify_all_four_proofs(Rational(9, 4), g_max=6)
        self.assertTrue(result['all_proofs_ok'])
        self.assertTrue(result['cross_consistent'])

    def test_cross_values_match(self):
        """Check actual F_g values match across all proofs."""
        kappa = Rational(3)
        result = verify_all_four_proofs(kappa, g_max=5)
        for g in range(1, 6):
            d = result['cross_details'][g]
            expected = kappa * lambda_fp(g)
            self.assertEqual(d['proof1'], expected)
            self.assertEqual(d['proof2'], expected)
            self.assertEqual(d['proof3'], expected)
            self.assertEqual(d['proof4'], expected)


# ====================================================================
# Section 7: Scope verification -- multi-weight failure (5 tests)
# ====================================================================

class TestMultiWeightFailure(unittest.TestCase):
    """Verify tau_shadow = tau_KW^kappa FAILS for multi-weight algebras."""

    def test_w3_genus2_failure_c100(self):
        """W_3 at c=100: delta_F_2 = (100+204)/(16*100) = 304/1600 != 0."""
        result = multi_weight_failure_genus2_w3(100)
        self.assertTrue(result['tau_power_fails'])
        self.assertTrue(result['correction_positive'])
        self.assertEqual(result['delta_F2_cross'], Rational(304, 1600))

    def test_w3_genus2_failure_c10(self):
        """W_3 at c=10: delta_F_2 = 214/160 != 0."""
        result = multi_weight_failure_genus2_w3(10)
        self.assertTrue(result['tau_power_fails'])
        self.assertTrue(result['correction_positive'])

    def test_w3_correction_always_positive(self):
        """delta_F_2(W_3) > 0 for all c > 0."""
        for c in [1, 2, 5, 10, 26, 50, 100, 1000]:
            result = multi_weight_failure_genus2_w3(c)
            self.assertTrue(result['correction_positive'],
                            f"Correction not positive at c={c}")

    def test_w3_scalar_not_equal_full(self):
        """F_2^scalar != F_2^full for W_3."""
        result = multi_weight_failure_genus2_w3(10)
        self.assertFalse(result['scalar_equals_full'])

    def test_w3_correction_formula(self):
        """delta_F_2(W_3) = (c+204)/(16c) matches the manuscript."""
        c = Rational(50)
        result = multi_weight_failure_genus2_w3(c)
        expected = (c + 204) / (16 * c)
        self.assertEqual(result['delta_F2_cross'], expected)


# ====================================================================
# Section 8: Genus 1 universality (4 tests)
# ====================================================================

class TestGenus1Universality(unittest.TestCase):
    """F_1 = kappa/24 holds UNCONDITIONALLY for all families."""

    def test_genus1_heisenberg(self):
        """F_1(Heisenberg_k) = k/24."""
        result = genus1_universality(7)
        self.assertTrue(result['match'])

    def test_genus1_virasoro(self):
        """F_1(Virasoro_c) = c/48."""
        result = genus1_universality(Rational(1, 2))
        self.assertEqual(result['F_1'], Rational(1, 48))

    def test_genus1_formula(self):
        """F_1 = kappa * lambda_1^FP = kappa/24."""
        for kappa_val in [Rational(1), Rational(5), Rational(13, 2), Rational(-3)]:
            result = genus1_universality(kappa_val)
            self.assertEqual(result['F_1'], kappa_val / 24)

    def test_genus1_universal_flag(self):
        """genus1_universal flag is always True."""
        result = genus1_universality(42)
        self.assertTrue(result['genus1_universal'])


# ====================================================================
# Section 9: KdV non-compatibility (5 tests)
# ====================================================================

class TestKdVNonCompatibility(unittest.TestCase):
    """tau_KW^kappa does NOT satisfy KdV for kappa != 0, 1."""

    def test_kdv_kappa1_compatible(self):
        """kappa=1: satisfies KdV (it IS tau_KW)."""
        result = kdv_compatibility_check(1)
        self.assertTrue(result['satisfies_kdv'])

    def test_kdv_kappa0_compatible(self):
        """kappa=0: satisfies KdV (trivially, tau=1)."""
        result = kdv_compatibility_check(0)
        self.assertTrue(result['satisfies_kdv'])

    def test_kdv_kappa2_incompatible(self):
        """kappa=2: does NOT satisfy KdV."""
        result = kdv_compatibility_check(2)
        self.assertFalse(result['satisfies_kdv'])
        self.assertEqual(result['discrepancy_coefficient'], Rational(-2))

    def test_kdv_kappa_half_incompatible(self):
        """kappa=1/2: does NOT satisfy KdV."""
        result = kdv_compatibility_check(Rational(1, 2))
        self.assertFalse(result['satisfies_kdv'])
        self.assertEqual(result['discrepancy_coefficient'], Rational(1, 4))

    def test_kdv_discrepancy_formula(self):
        """Discrepancy coefficient is kappa(1-kappa)."""
        for k in [2, 3, 5, Rational(1, 2), Rational(13, 2)]:
            result = kdv_compatibility_check(k)
            expected = Rational(k) * (1 - Rational(k))
            self.assertEqual(result['discrepancy_coefficient'], expected)


# ====================================================================
# Section 10: Special cases (5 tests)
# ====================================================================

class TestSpecialCases(unittest.TestCase):
    """Special cases: kappa=0, kappa=1, complementarity."""

    def test_kappa_zero_trivial(self):
        """kappa=0: all F_g = 0, tau = 1."""
        result = kappa_zero_degenerate_case()
        self.assertTrue(result['all_Fg_zero'])

    def test_kappa_zero_ap31_caveat(self):
        """kappa=0: AP31 caveat is stated."""
        result = kappa_zero_degenerate_case()
        self.assertIn('AP31', result['ap31_caveat'])

    def test_kappa_one_recovers(self):
        """kappa=1: recovers KW tau-function."""
        result = kappa_one_recovers_kw()
        self.assertTrue(result['recovers_kw'])
        self.assertTrue(result['satisfies_kdv'])

    def test_complementarity_km(self):
        """KM complementarity: kappa + kappa' = 0, product = tau_KW^0 = 1."""
        result = complementarity_tau_functions(Rational(9, 4), Rational(-9, 4))
        self.assertTrue(result['product_trivial'])
        self.assertEqual(result['kappa_sum'], 0)

    def test_complementarity_virasoro(self):
        """Virasoro complementarity: kappa + kappa' = 13, product = tau_KW^13."""
        # Vir_c: kappa = c/2. Vir_{26-c}: kappa' = (26-c)/2. Sum = 13.
        result = complementarity_tau_functions(Rational(5), Rational(8))
        self.assertEqual(result['kappa_sum'], 13)
        self.assertFalse(result['product_trivial'])


# ====================================================================
# Section 11: Virasoro constraints at free energy level (3 tests)
# ====================================================================

class TestFreeEnergyConstraints(unittest.TestCase):
    """Virasoro constraints at the free energy level."""

    def test_string_equation_compatible(self):
        """String equation compatible with kappa rescaling."""
        result = free_energy_virasoro_constraints(5)
        self.assertTrue(result['string_equation_compatible'])

    def test_dilaton_equation_compatible(self):
        """Dilaton equation compatible with kappa rescaling."""
        result = free_energy_virasoro_constraints(5)
        self.assertTrue(result['dilaton_equation_compatible'])

    def test_fg_ratio_is_kappa(self):
        """F_g^shadow / F_g^KW = kappa for all g."""
        kappa = Rational(7)
        result = free_energy_virasoro_constraints(kappa, g_max=5)
        for g in range(1, 6):
            self.assertEqual(result[f'F_{g}_ratio'], kappa)


# ====================================================================
# Section 12: Convergence (3 tests)
# ====================================================================

class TestConvergence(unittest.TestCase):
    """Convergence radius of the shadow generating function."""

    def test_radius_independent_of_kappa(self):
        """Convergence radius |hbar| = 2*pi, independent of kappa."""
        result = convergence_radius_shadow(5)
        self.assertTrue(result['radius_independent_of_kappa'])

    def test_radius_value(self):
        """Radius of convergence is 2*pi."""
        result = convergence_radius_shadow(1)
        self.assertEqual(result['radius_of_convergence_hbar'], '2*pi')

    def test_ratios_decrease(self):
        """Successive ratios lambda_{g+1}/lambda_g are decreasing."""
        result = convergence_radius_shadow(1)
        ratios = result['ratios']
        for g in range(2, 7):
            self.assertLess(
                ratios[g]['numerical'], ratios[g-1]['numerical'],
                f"Ratio at g={g} not less than at g={g-1}"
            )


# ====================================================================
# Section 13: Standard family table (6 tests)
# ====================================================================

class TestStandardFamilyTable(unittest.TestCase):
    """Verify tau_shadow = tau_KW^kappa across standard families."""

    def test_all_families_pass(self):
        """All standard uniform-weight families pass all four proofs."""
        table = standard_family_verification_table(g_max=5)
        for name, data in table.items():
            self.assertTrue(data['all_proofs_ok'],
                            f"Family {name} failed")
            self.assertTrue(data['cross_consistent'],
                            f"Family {name} cross-inconsistent")

    def test_heisenberg_k1(self):
        """Heisenberg k=1: kappa=1, tau_shadow = tau_KW."""
        table = standard_family_verification_table(g_max=3)
        self.assertEqual(table['Heisenberg_k=1']['kappa'], Rational(1))

    def test_virasoro_c13_self_dual(self):
        """Virasoro c=13 (self-dual): kappa = 13/2."""
        table = standard_family_verification_table(g_max=3)
        self.assertEqual(table['Virasoro_c=13']['kappa'], Rational(13, 2))

    def test_virasoro_c26_critical(self):
        """Virasoro c=26 (critical): kappa = 13."""
        table = standard_family_verification_table(g_max=3)
        self.assertEqual(table['Virasoro_c=26']['kappa'], Rational(13))

    def test_affine_sl2_k1(self):
        """Affine sl_2 at k=1: kappa = 9/4."""
        table = standard_family_verification_table(g_max=3)
        self.assertEqual(table['Affine_sl2_k=1']['kappa'], Rational(9, 4))

    def test_affine_sl2_k2(self):
        """Affine sl_2 at k=2: kappa = 3."""
        table = standard_family_verification_table(g_max=3)
        self.assertEqual(table['Affine_sl2_k=2']['kappa'], Rational(3))


# ====================================================================
# Section 14: Deep numerical verification (5 tests)
# ====================================================================

class TestDeepNumerical(unittest.TestCase):
    """Deep numerical verification through high genus."""

    def test_genus8_identity(self):
        """Identity holds at genus 8 for kappa=5."""
        kappa = Rational(5)
        F8_shadow = shadow_free_energy(kappa, 8)
        F8_kw = lambda_fp(8)
        self.assertEqual(F8_shadow, kappa * F8_kw)

    def test_genus10_identity(self):
        """Identity holds at genus 10 for kappa=13/2."""
        kappa = Rational(13, 2)
        F10_shadow = shadow_free_energy(kappa, 10)
        F10_kw = lambda_fp(10)
        self.assertEqual(F10_shadow, kappa * F10_kw)

    def test_genus12_identity(self):
        """Identity holds at genus 12."""
        kappa = Rational(7)
        F12 = shadow_free_energy(kappa, 12)
        self.assertEqual(F12, kappa * lambda_fp(12))

    def test_negative_kappa_genus5(self):
        """Identity holds for negative kappa at genus 5."""
        kappa = Rational(-3, 2)
        F5 = shadow_free_energy(kappa, 5)
        self.assertEqual(F5, kappa * lambda_fp(5))
        self.assertLess(F5, 0)  # Negative kappa gives negative free energy

    def test_large_kappa_genus3(self):
        """Identity holds for kappa=1000 at genus 3."""
        kappa = Rational(1000)
        F3 = shadow_free_energy(kappa, 3)
        self.assertEqual(F3, Rational(1000) * Rational(31, 967680))


if __name__ == '__main__':
    unittest.main()
