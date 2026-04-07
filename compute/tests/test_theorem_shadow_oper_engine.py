r"""Tests for the shadow oper rigidity theorem.

THEOREM: The shadow connection nabla^sh = d - Q'/(2Q) dt is a rigid
hypergeometric oper with Koszul monodromy -1.

Tests organized by proof method:
  Method 1: Direct computation of residues (partial fractions)
  Method 2: Riemann-Hilbert / hypergeometric identification
  Method 3: Rigidity from shadow metric uniqueness
  Method 4: Monodromy representation

Cross-verifications:
  - Multi-path residue computation (3 independent derivations)
  - Koszul duality compatibility
  - Class degeneration analysis
  - Full landscape scan
  - Numerical monodromy integration

Beilinson compliance:
  AP1:  kappa recomputed from first principles per family.
  AP3:  No pattern-matching; each test derives independently.
  AP10: Cross-family consistency, not hardcoded values only.
"""

import cmath
import math
import unittest

import numpy as np

from compute.lib.theorem_shadow_oper_engine import (
    # Shadow data
    shadow_metric_Q,
    shadow_metric_coeffs,
    critical_disc,
    virasoro_data,
    heisenberg_data,
    affine_sl2_data,
    w3_wline_data,
    # Method 1
    connection_form_residues,
    partial_fraction_verification,
    # Method 2
    shadow_oper_riemann_scheme,
    hypergeometric_parameters,
    n_accessory_parameters,
    RiemannScheme,
    # Method 3
    shadow_metric_uniqueness_proof,
    # Method 4
    monodromy_representation,
    verify_monodromy_numerically,
    # Cross-verification
    residue_from_partial_fractions,
    residue_from_laurent_expansion,
    residue_from_residue_theorem,
    exponent_from_indicial_equation,
    verify_fuchs_relation,
    shadow_oper_landscape,
    # Symbolic
    symbolic_residue_proof,
    symbolic_indicial_exponents,
    symbolic_fuchs_relation_check,
    symbolic_monodromy_computation,
    # Koszul duality
    koszul_duality_oper_compatibility,
    koszul_duality_discriminant_sum,
    # Class analysis
    class_degeneration_analysis,
    # Full theorem
    prove_shadow_oper_rigidity,
)


# =========================================================================
# Method 1: Direct computation of residues
# =========================================================================

class TestMethod1DirectResidues(unittest.TestCase):
    """Method 1: Direct computation of connection form residues."""

    def test_virasoro_residues_c1(self):
        """Virasoro at c=1: residues are 1/2 at both zeros."""
        kappa, alpha, S4, _ = virasoro_data(1.0)
        result = connection_form_residues(kappa, alpha, S4)
        self.assertEqual(result['type'], 'two_simple_zeros')
        self.assertEqual(result['residues'], [0.5, 0.5])

    def test_virasoro_residues_c25(self):
        """Virasoro at c=25: residues are 1/2 at both zeros."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = connection_form_residues(kappa, alpha, S4)
        self.assertEqual(result['residues'], [0.5, 0.5])

    def test_virasoro_residues_c13_selfdual(self):
        """Virasoro at self-dual c=13: residues are 1/2."""
        kappa, alpha, S4, _ = virasoro_data(13.0)
        result = connection_form_residues(kappa, alpha, S4)
        self.assertEqual(result['residues'], [0.5, 0.5])

    def test_residue_universal_across_c(self):
        """Residue = 1/2 is UNIVERSAL: independent of c (for class M)."""
        for c_val in [0.5, 1.0, 2.0, 5.0, 10.0, 13.0, 25.0, 50.0, 100.0]:
            kappa, alpha, S4, Delta = virasoro_data(c_val)
            if abs(Delta) < 1e-30:
                continue
            result = connection_form_residues(kappa, alpha, S4)
            self.assertEqual(
                result['residues'], [0.5, 0.5],
                f"Failed at c={c_val}"
            )

    def test_numerical_residue_matches_analytic(self):
        """Numerical limit Res = lim (t-t0)*omega matches 1/2."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = connection_form_residues(kappa, alpha, S4)
        self.assertAlmostEqual(
            abs(result['numerical_residue_plus']), 0.5, places=5
        )
        self.assertAlmostEqual(
            abs(result['numerical_residue_minus']), 0.5, places=5
        )

    def test_two_zeros_for_class_M(self):
        """Class M algebras have exactly 2 zeros of Q_L."""
        for c_val in [1.0, 5.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            result = connection_form_residues(kappa, alpha, S4)
            self.assertEqual(result['n_zeros'], 2)

    def test_partial_fraction_pointwise(self):
        """Verify omega = 1/(2(t-t+)) + 1/(2(t-t-)) pointwise."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = partial_fraction_verification(kappa, alpha, S4)
        self.assertEqual(result['status'], 'verified')
        self.assertLess(result['max_error'], 1e-10)

    def test_partial_fraction_multiple_c(self):
        """Partial fraction identity holds for multiple c values."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            result = partial_fraction_verification(kappa, alpha, S4)
            self.assertLess(
                result['max_error'], 1e-8,
                f"Failed at c={c_val}"
            )

    def test_w3_wline_residues(self):
        """W_3 W-line also has residues 1/2 (universality)."""
        kappa, alpha, S4, Delta = w3_wline_data(25.0)
        if abs(Delta) > 1e-30:
            result = connection_form_residues(kappa, alpha, S4)
            self.assertEqual(result['residues'], [0.5, 0.5])

    def test_heisenberg_degenerate(self):
        """Heisenberg has Delta = 0: no singular points, degenerate."""
        kappa, alpha, S4, _ = heisenberg_data(1.0)
        result = connection_form_residues(kappa, alpha, S4)
        self.assertEqual(result['type'], 'degenerate')


# =========================================================================
# Method 2: Riemann-Hilbert / hypergeometric identification
# =========================================================================

class TestMethod2RiemannHilbert(unittest.TestCase):
    """Method 2: Riemann scheme and hypergeometric identification."""

    def test_riemann_scheme_3_singular(self):
        """Class M: Riemann scheme has 3 singular points (2 finite + inf)."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        self.assertEqual(scheme.n_singular, 3)

    def test_zero_accessory_parameters(self):
        """Hypergeometric equation has 0 accessory parameters (RIGID)."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        self.assertEqual(scheme.n_accessory, 0)

    def test_n_accessory_formula(self):
        """n_accessory = max(0, n - 3) for order 2 Fuchsian equations."""
        self.assertEqual(n_accessory_parameters(3, 2), 0)   # hypergeometric
        self.assertEqual(n_accessory_parameters(4, 2), 1)   # Heun
        self.assertEqual(n_accessory_parameters(5, 2), 2)
        self.assertEqual(n_accessory_parameters(2, 2), 0)
        self.assertEqual(n_accessory_parameters(1, 2), 0)

    def test_exponent_difference_half(self):
        """Exponent difference at each finite zero is 1/2."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        diffs = scheme.exponent_differences
        # First two are for finite zeros
        self.assertAlmostEqual(diffs[0], 0.5, places=10)
        self.assertAlmostEqual(diffs[1], 0.5, places=10)

    def test_finite_exponents_quarter_three_quarter(self):
        """Exponents at each finite zero are {1/4, 3/4}."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        for (rho1, rho2) in scheme.exponents[:2]:
            self.assertAlmostEqual(rho1, 0.25, places=10)
            self.assertAlmostEqual(rho2, 0.75, places=10)

    def test_fuchs_relation(self):
        """Fuchs relation: sum of all exponents = n - 2 = 1."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        check = verify_fuchs_relation(scheme)
        self.assertTrue(check['satisfied'])
        self.assertAlmostEqual(check['actual_sum'], 1.0, places=10)

    def test_indicial_exponents_from_leading_coeff(self):
        """Indicial exponents from V ~ 3/16/(t-t0)^2 are {1/4, 3/4}."""
        rho_plus, rho_minus = exponent_from_indicial_equation(3.0 / 16.0)
        self.assertAlmostEqual(rho_plus, 0.75, places=10)
        self.assertAlmostEqual(rho_minus, 0.25, places=10)

    def test_degenerate_no_singular_points(self):
        """Delta = 0: Riemann scheme has no singular points."""
        kappa, alpha, S4, _ = heisenberg_data(1.0)
        scheme = shadow_oper_riemann_scheme(kappa, alpha, S4)
        self.assertEqual(scheme.n_singular, 0)
        self.assertEqual(scheme.n_accessory, 0)

    def test_hypergeometric_parameters(self):
        """The shadow oper matches _2F_1 parameters."""
        params = hypergeometric_parameters()
        self.assertAlmostEqual(params['exponent_diff_0'], 0.5, places=10)
        self.assertAlmostEqual(params['exponent_diff_1'], 0.5, places=10)


# =========================================================================
# Method 3: Rigidity from shadow metric uniqueness
# =========================================================================

class TestMethod3Uniqueness(unittest.TestCase):
    """Method 3: Shadow metric Q_L is uniquely determined."""

    def test_uniqueness_virasoro_c25(self):
        """Q_L for Virasoro at c=25 is uniquely determined by 3 conditions."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = shadow_metric_uniqueness_proof(kappa, alpha, S4)
        self.assertTrue(result['is_uniquely_determined'])
        self.assertTrue(result['coefficients_match'])

    def test_normalization_at_zero(self):
        """Q_L(0) = 4 kappa^2 (normalization condition)."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            result = shadow_metric_uniqueness_proof(kappa, alpha, S4)
            self.assertTrue(result['normalization_ok'])

    def test_derivative_at_zero(self):
        """Q_L'(0) = 12 kappa alpha (derivative condition)."""
        for c_val in [1.0, 5.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            result = shadow_metric_uniqueness_proof(kappa, alpha, S4)
            self.assertTrue(result['derivative_ok'])

    def test_three_conditions_three_coefficients(self):
        """3 conditions (q0, q1, q2) fix the degree-2 polynomial uniquely."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = shadow_metric_uniqueness_proof(kappa, alpha, S4)
        self.assertEqual(result['n_conditions'], 3)
        self.assertEqual(result['n_coefficients'], 3)

    def test_uniqueness_implies_rigidity(self):
        """Unique Q_L => unique connection => 0 free parameters => rigid."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = shadow_metric_uniqueness_proof(kappa, alpha, S4)
        self.assertTrue(result['is_uniquely_determined'])
        # This algebraic uniqueness is METHOD 3's proof of rigidity.


# =========================================================================
# Method 4: Monodromy representation
# =========================================================================

class TestMethod4Monodromy(unittest.TestCase):
    """Method 4: Monodromy representation factors through Z/2."""

    def test_monodromy_minus_one(self):
        """Monodromy eigenvalue = exp(2 pi i * 1/2) = -1."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertTrue(result['monodromy_is_minus_one'])

    def test_monodromy_is_koszul_sign(self):
        """Monodromy = -1 is the Koszul sign (bar-cobar Z/2 symmetry)."""
        for c_val in [1.0, 5.0, 13.0, 25.0, 50.0]:
            kappa, alpha, S4, Delta = virasoro_data(c_val)
            if abs(Delta) < 1e-30:
                continue
            result = monodromy_representation(kappa, alpha, S4)
            self.assertTrue(
                result['is_koszul'],
                f"Failed at c={c_val}"
            )

    def test_monodromy_involutive(self):
        """Monodromy^2 = 1 (involutive: Z/2 action)."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertTrue(result['is_involutive'])

    def test_fundamental_group_Z(self):
        r"""pi_1(P^1 \ {2 pts}) = Z (cylinder)."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertEqual(result['fundamental_group'], 'Z')

    def test_monodromy_image_Z2(self):
        """Image of monodromy representation is Z/2 = {+1, -1}."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertEqual(result['monodromy_image'], {1, -1})
        self.assertEqual(result['monodromy_image_order'], 2)

    def test_monodromy_at_infinity_trivial(self):
        """Monodromy at infinity for the rank-1 connection is trivial.

        Res_inf = -(1/2 + 1/2) = -1, so exp(2 pi i * (-1)) = 1.
        """
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertTrue(result['infinity_is_trivial'])

    def test_heisenberg_trivial_monodromy(self):
        """Heisenberg (class G): trivial monodromy."""
        kappa, alpha, S4, _ = heisenberg_data(1.0)
        result = monodromy_representation(kappa, alpha, S4)
        self.assertEqual(result['type'], 'trivial')

    def test_numerical_monodromy_minus_one(self):
        """Numerical parallel transport around a zero gives monodromy -1."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        result = verify_monodromy_numerically(kappa, alpha, S4)
        self.assertTrue(
            result['is_minus_one'],
            f"Monodromy = {result['monodromy']}, expected -1"
        )

    def test_numerical_monodromy_multiple_c(self):
        """Numerical monodromy = -1 for multiple c values."""
        for c_val in [5.0, 10.0, 25.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            result = verify_monodromy_numerically(kappa, alpha, S4, n_steps=20000)
            self.assertTrue(
                result['is_minus_one'],
                f"Failed at c={c_val}: monodromy = {result['monodromy']}"
            )


# =========================================================================
# Cross-verification: 3 independent residue computations
# =========================================================================

class TestMultiPathResidues(unittest.TestCase):
    """Three independent derivations of the residue 1/2."""

    def test_path1_partial_fractions(self):
        """Path 1: Partial fractions give residue 1/2."""
        self.assertEqual(residue_from_partial_fractions(), 0.5)

    def test_path2_laurent_expansion(self):
        """Path 2: Laurent expansion near zero gives residue 1/2."""
        self.assertEqual(residue_from_laurent_expansion(), 0.5)

    def test_path3_residue_theorem(self):
        """Path 3: P^1 residue theorem gives residue 1/2."""
        self.assertEqual(residue_from_residue_theorem(), 0.5)

    def test_all_three_agree(self):
        """All three paths give the same universal residue 1/2."""
        r1 = residue_from_partial_fractions()
        r2 = residue_from_laurent_expansion()
        r3 = residue_from_residue_theorem()
        self.assertEqual(r1, r2)
        self.assertEqual(r2, r3)
        self.assertEqual(r1, 0.5)


# =========================================================================
# Symbolic verification (sympy)
# =========================================================================

class TestSymbolicProofs(unittest.TestCase):
    """Symbolic (exact) proofs using sympy."""

    def test_symbolic_residue(self):
        """Sympy proof: Res_{t_0}(Q'/(2Q)) = 1/2 for any simple zero."""
        result = symbolic_residue_proof()
        if result['status'] == 'sympy_unavailable':
            self.skipTest("sympy unavailable")
        self.assertTrue(result['is_half'])

    def test_symbolic_indicial_exponents(self):
        """Sympy proof: indicial exponents are {1/4, 3/4}."""
        result = symbolic_indicial_exponents()
        if result['status'] == 'sympy_unavailable':
            self.skipTest("sympy unavailable")
        roots = sorted(result['roots_numerical'])
        self.assertAlmostEqual(roots[0], 0.25, places=10)
        self.assertAlmostEqual(roots[1], 0.75, places=10)

    def test_symbolic_exponent_difference_half(self):
        """Sympy proof: exponent difference = 1/2."""
        result = symbolic_indicial_exponents()
        if result['status'] == 'sympy_unavailable':
            self.skipTest("sympy unavailable")
        self.assertTrue(result['difference_is_half'])

    def test_symbolic_fuchs_relation(self):
        """Sympy proof: Fuchs relation satisfied."""
        result = symbolic_fuchs_relation_check()
        if result['status'] == 'sympy_unavailable':
            self.skipTest("sympy unavailable")
        self.assertTrue(result['fuchs_satisfied'])

    def test_symbolic_monodromy_minus_one(self):
        """Sympy proof: exp(2 pi i * 1/2) = -1."""
        result = symbolic_monodromy_computation()
        if result['status'] == 'sympy_unavailable':
            self.skipTest("sympy unavailable")
        self.assertTrue(result['is_minus_one'])


# =========================================================================
# Koszul duality compatibility
# =========================================================================

class TestKoszulDuality(unittest.TestCase):
    """Koszul duality c -> 26 - c preserves oper structure."""

    def test_koszul_dual_oper_isomorphic(self):
        """The Koszul dual oper (c -> 26-c) is isomorphic (same local data)."""
        for c_val in [1.0, 5.0, 10.0, 25.0]:
            result = koszul_duality_oper_compatibility(c_val)
            self.assertTrue(
                result['oper_isomorphic'],
                f"Failed at c={c_val}"
            )

    def test_selfdual_c13(self):
        """At c = 13: the oper is self-dual under Koszul involution."""
        result = koszul_duality_oper_compatibility(13.0)
        self.assertTrue(result['is_self_dual_point'])
        self.assertTrue(result['oper_isomorphic'])

    def test_discriminant_complementarity_sum(self):
        """Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c))."""
        for c_val in [1.0, 5.0, 10.0, 13.0, 25.0]:
            result = koszul_duality_discriminant_sum(c_val)
            self.assertTrue(
                result['match'],
                f"Failed at c={c_val}: sum={result['sum']}, "
                f"expected={result['expected']}"
            )


# =========================================================================
# Class degeneration analysis
# =========================================================================

class TestClassDegeneration(unittest.TestCase):
    """Shadow depth class determines oper behavior."""

    def test_class_G_trivial(self):
        """Class G (Heisenberg): trivial monodromy, no singularities."""
        results = class_degeneration_analysis()
        self.assertTrue(results['class_G']['monodromy_trivial'])
        self.assertAlmostEqual(results['class_G']['Delta'], 0.0)

    def test_class_L_trivial(self):
        """Class L (affine KM): trivial monodromy on diagonal primary line."""
        results = class_degeneration_analysis()
        self.assertTrue(results['class_L']['monodromy_trivial'])
        self.assertAlmostEqual(results['class_L']['Delta'], 0.0)

    def test_class_M_koszul_monodromy(self):
        """Class M (Virasoro): monodromy -1 (Koszul sign)."""
        results = class_degeneration_analysis()
        self.assertTrue(results['class_M']['monodromy_minus_one'])

    def test_class_M_w3_koszul_monodromy(self):
        """Class M (W_3 W-line): monodromy -1 (Koszul sign)."""
        results = class_degeneration_analysis()
        self.assertTrue(results['class_M_W3']['monodromy_minus_one'])

    def test_delta_zero_iff_trivial(self):
        """Delta = 0 iff monodromy is trivial (no singular points)."""
        results = class_degeneration_analysis()
        # Class G: Delta = 0, trivial
        self.assertAlmostEqual(results['class_G']['Delta'], 0.0)
        self.assertTrue(results['class_G']['monodromy_trivial'])
        # Class M: Delta != 0, nontrivial
        self.assertGreater(abs(results['class_M']['Delta']), 1e-10)
        self.assertTrue(results['class_M']['monodromy_minus_one'])


# =========================================================================
# Full landscape scan
# =========================================================================

class TestLandscapeScan(unittest.TestCase):
    """Verify the theorem across the full central charge landscape."""

    def test_landscape_all_consistent(self):
        """All four methods agree across the landscape."""
        results = shadow_oper_landscape()
        for entry in results:
            self.assertTrue(
                entry['all_consistent'],
                f"Inconsistency at c={entry['c']}"
            )

    def test_landscape_all_rigid(self):
        """All class M opers in the landscape are rigid."""
        results = shadow_oper_landscape()
        for entry in results:
            if entry['Delta'] > 1e-30:
                self.assertEqual(
                    entry['method2_n_accessory'], 0,
                    f"Non-rigid at c={entry['c']}"
                )

    def test_landscape_koszul_monodromy(self):
        """All class M opers have Koszul monodromy -1."""
        results = shadow_oper_landscape()
        for entry in results:
            if entry['Delta'] > 1e-30:
                self.assertTrue(
                    entry['method4_koszul'],
                    f"Non-Koszul monodromy at c={entry['c']}"
                )


# =========================================================================
# Full theorem assembly
# =========================================================================

class TestFullTheorem(unittest.TestCase):
    """Test the complete theorem proof assembly."""

    def test_full_proof_virasoro_c25(self):
        """Full proof for Virasoro at c = 25."""
        kappa, alpha, S4, _ = virasoro_data(25.0)
        proof = prove_shadow_oper_rigidity(kappa, alpha, S4)
        self.assertTrue(proof['is_class_M'])
        self.assertTrue(proof['is_hypergeometric'])
        self.assertTrue(proof['is_rigid'])
        self.assertTrue(proof['residues_universal'])
        self.assertTrue(proof['monodromy_koszul'])
        self.assertTrue(proof['all_methods_agree'])

    def test_full_proof_virasoro_c13(self):
        """Full proof for Virasoro at self-dual c = 13."""
        kappa, alpha, S4, _ = virasoro_data(13.0)
        proof = prove_shadow_oper_rigidity(kappa, alpha, S4)
        self.assertTrue(proof['all_methods_agree'])

    def test_full_proof_w3_wline(self):
        """Full proof for W_3 on the W-line at c = 25."""
        kappa, alpha, S4, Delta = w3_wline_data(25.0)
        proof = prove_shadow_oper_rigidity(kappa, alpha, S4)
        if abs(Delta) > 1e-30:
            self.assertTrue(proof['all_methods_agree'])

    def test_full_proof_heisenberg_degenerate(self):
        """Full proof for Heisenberg (degenerate case)."""
        kappa, alpha, S4, _ = heisenberg_data(1.0)
        proof = prove_shadow_oper_rigidity(kappa, alpha, S4)
        self.assertFalse(proof['is_class_M'])
        self.assertTrue(proof['all_methods_agree'])

    def test_full_proof_multiple_c(self):
        """Full proof agrees across multiple c values."""
        for c_val in [1.0, 2.0, 5.0, 10.0, 13.0, 25.0, 50.0]:
            kappa, alpha, S4, _ = virasoro_data(c_val)
            proof = prove_shadow_oper_rigidity(kappa, alpha, S4)
            self.assertTrue(
                proof['all_methods_agree'],
                f"Methods disagree at c={c_val}"
            )


if __name__ == '__main__':
    unittest.main()
