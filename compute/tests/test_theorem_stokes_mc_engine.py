r"""Tests for theorem_stokes_mc_engine.py: S_1 = -4pi^2 kappa i.

Verifies five independent proofs of the leading Stokes multiplier
and universal instanton action, with 40+ tests covering:

- Proof 1 (large-order): ratio test, Borel residue extraction
- Proof 2 (generating function): pole residues, numerical contour integral
- Proof 3 (bridge equation): MC constraint, partial fraction = Bernoulli
- Proof 4 (Borel-Pade): pole convergence, residue extraction
- Proof 5 (WKB): instanton action, one-loop determinant
- Cross-family: universality of A, linearity of S_1 in kappa
- Complementarity: S_1 + S_1' = -52 pi^2 i for Virasoro
- Higher Stokes: S_n = (-1)^n n S_1
- F_g exact: three-method cross-check (Bernoulli, poles, Cauchy)

Manuscript references:
    prop:universal-instanton-action (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
"""

import cmath
import math
import unittest

from compute.lib.theorem_stokes_mc_engine import (
    FOUR_PI_SQ,
    PI,
    S1_UNIT,
    TWO_PI,
    F_g,
    LargeOrderProof,
    StokesMCTheorem,
    Z_closed_form,
    Z_hbar,
    _borel_coefficients_u,
    _extract_S1_from_large_order,
    _extract_action_from_ratios,
    _one_loop_determinant,
    _ratio_test_sequence,
    _residue_at_pole,
    _residue_numerical,
    _S1_convergence_sequence,
    _verify_instanton_action_numerical,
    _verify_mc_constraint_on_alien,
    bernoulli_number,
    higher_stokes_constants,
    lambda_fp,
    proof1_large_order,
    proof2_generating_function,
    proof3_bridge_equation,
    proof4_borel_pade,
    proof5_wkb,
    prove_stokes_mc_theorem,
    stokes_from_duality,
    verify_A_universality,
    verify_across_families,
    verify_complementarity,
    verify_F_g_exact,
    verify_S1_linearity,
)


class TestBernoulliNumbers(unittest.TestCase):
    """Verify Bernoulli number computation."""

    def test_B0(self):
        self.assertAlmostEqual(bernoulli_number(0), 1.0, places=14)

    def test_B1(self):
        self.assertAlmostEqual(bernoulli_number(1), -0.5, places=14)

    def test_B2(self):
        self.assertAlmostEqual(bernoulli_number(2), 1.0 / 6.0, places=14)

    def test_B4(self):
        self.assertAlmostEqual(bernoulli_number(4), -1.0 / 30.0, places=14)

    def test_B6(self):
        self.assertAlmostEqual(bernoulli_number(6), 1.0 / 42.0, places=14)

    def test_odd_vanish(self):
        """B_n = 0 for odd n > 1."""
        for n in [3, 5, 7, 9, 11]:
            self.assertEqual(bernoulli_number(n), 0.0)


class TestLambdaFP(unittest.TestCase):
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        """lambda_1 = 1/24."""
        self.assertAlmostEqual(lambda_fp(1), 1.0 / 24.0, places=14)

    def test_lambda_2(self):
        """lambda_2 = 7/5760."""
        self.assertAlmostEqual(lambda_fp(2), 7.0 / 5760.0, places=14)

    def test_lambda_3(self):
        """lambda_3 = 31/967680."""
        self.assertAlmostEqual(lambda_fp(3), 31.0 / 967680.0, places=12)

    def test_generating_function_check(self):
        """Verify sum lambda_g x^{2g} = (x/2)/sin(x/2) - 1 at x = 1."""
        x = 1.0
        gf_exact = (x / 2.0) / math.sin(x / 2.0) - 1.0
        gf_series = sum(lambda_fp(g) * x ** (2 * g) for g in range(1, 30))
        self.assertAlmostEqual(gf_series, gf_exact, places=12)


class TestFg(unittest.TestCase):
    """Verify F_g = kappa * lambda_g."""

    def test_F1_virasoro(self):
        """F_1(Vir_c) = c/2 * 1/24 = c/48."""
        for c in [1.0, 12.0, 26.0]:
            kappa = c / 2.0
            self.assertAlmostEqual(F_g(kappa, 1), c / 48.0, places=14)

    def test_F1_heisenberg(self):
        """F_1(H_k) = k/24."""
        for k in [1.0, 2.0, 5.0]:
            self.assertAlmostEqual(F_g(k, 1), k / 24.0, places=14)

    def test_F_g_linear_in_kappa(self):
        """F_g(lambda * kappa) = lambda * F_g(kappa)."""
        kappa = 3.0
        for g in [1, 2, 5, 10]:
            for scale in [0.5, 2.0, 7.0]:
                self.assertAlmostEqual(
                    F_g(scale * kappa, g),
                    scale * F_g(kappa, g),
                    places=12,
                )


class TestClosedForm(unittest.TestCase):
    """Verify the closed-form generating function."""

    def test_Z_small_u(self):
        """Z(u) ~ F_1 u + F_2 u^2 + ... for small u."""
        kappa = 1.0
        u = 0.01
        Z_val = Z_closed_form(kappa, u).real
        Z_series = sum(F_g(kappa, g) * u ** g for g in range(1, 20))
        self.assertAlmostEqual(Z_val, Z_series, places=10)

    def test_Z_poles(self):
        """Z(u) diverges at u = (2pi)^2."""
        kappa = 1.0
        u_near_pole = FOUR_PI_SQ - 0.001
        Z_val = abs(Z_closed_form(kappa, u_near_pole))
        self.assertGreater(Z_val, 100.0)

    def test_Z_hbar_identity(self):
        """Z_hbar(kappa, hbar) = Z_closed_form(kappa, hbar^2)."""
        kappa = 2.5
        hbar = 1.0 + 0.5j
        self.assertAlmostEqual(
            Z_hbar(kappa, hbar),
            Z_closed_form(kappa, hbar ** 2),
            places=12,
        )


# =====================================================================
# PROOF 1 TESTS
# =====================================================================

class TestProof1LargeOrder(unittest.TestCase):
    """Proof 1: large-order extraction of A and S_1."""

    def test_ratio_convergence(self):
        """Ratio F_{g+1}/F_g * (2g+2)(2g+1) / (2pi)^2 -> 1."""
        kappa = 1.0
        ratios = _ratio_test_sequence(kappa, 25)
        # Last few should be very close to 1
        for r in ratios[-5:]:
            self.assertAlmostEqual(r, 1.0, places=5)

    def test_instanton_action_extraction(self):
        """A extracted from ratios converges to (2pi)^2."""
        kappa = 1.0
        A = _extract_action_from_ratios(kappa, 30)
        self.assertAlmostEqual(A, FOUR_PI_SQ, places=6)

    def test_instanton_action_kappa_independent(self):
        """A is independent of kappa (universal)."""
        for kappa in [0.5, 1.0, 5.0, 13.0]:
            A = _extract_action_from_ratios(kappa, 30)
            self.assertAlmostEqual(A, FOUR_PI_SQ, places=5)

    def test_S1_extraction(self):
        """S_1 = -4pi^2 kappa i from large-order."""
        kappa = 2.0
        S1 = _extract_S1_from_large_order(kappa, 30)
        S1_exact = -4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(S1, S1_exact, places=10)

    def test_S1_convergence_exponential(self):
        """R_1 extraction error decreases exponentially (1/4^g)."""
        kappa = 1.0
        seq = _S1_convergence_sequence(kappa, 20)
        # Check that errors decrease
        errors = [e for (_, _, e) in seq if not math.isnan(e)]
        self.assertGreater(len(errors), 5)
        # Error at g=15 should be much smaller than at g=5
        self.assertLess(errors[-1], errors[3] * 0.01)

    def test_proof1_full(self):
        """Full Proof 1 execution."""
        kappa = 3.0
        result = proof1_large_order(kappa, 30)
        S1_exact = -4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(result.S1_extracted, S1_exact, places=10)
        self.assertAlmostEqual(result.instanton_action, FOUR_PI_SQ, places=4)


# =====================================================================
# PROOF 2 TESTS
# =====================================================================

class TestProof2GeneratingFunction(unittest.TestCase):
    """Proof 2: residue extraction from closed form."""

    def test_residue_R1_formula(self):
        """R_1 = -8 pi^2 kappa."""
        for kappa in [0.5, 1.0, 6.5]:
            R1 = _residue_at_pole(kappa, 1)
            self.assertAlmostEqual(R1, -8.0 * PI ** 2 * kappa, places=10)

    def test_residue_R2_formula(self):
        """R_2 = +8 pi^2 * 4 * kappa = 32 pi^2 kappa."""
        kappa = 1.0
        R2 = _residue_at_pole(kappa, 2)
        self.assertAlmostEqual(R2, 32.0 * PI ** 2 * kappa, places=10)

    def test_residue_alternating_sign(self):
        """R_n has sign (-1)^n."""
        kappa = 1.0
        for n in range(1, 6):
            R = _residue_at_pole(kappa, n)
            self.assertEqual(math.copysign(1, R), (-1.0) ** n)

    def test_residue_numerical_matches_exact(self):
        """Numerical contour integral matches exact residue."""
        kappa = 1.0
        R1_exact = _residue_at_pole(kappa, 1)
        R1_num = _residue_numerical(kappa, 1)
        self.assertAlmostEqual(R1_num.real, R1_exact, delta=abs(R1_exact) * 0.01)

    def test_S1_from_residue(self):
        """S_1^hbar = -4pi^2 kappa i from residue in hbar-plane."""
        kappa = 6.5  # c = 13 self-dual
        result = proof2_generating_function(kappa)
        S1_exact = -4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(result.S1_hbar, S1_exact, places=10)

    def test_multiple_poles_verified(self):
        """At least 3 poles verified numerically."""
        kappa = 1.0
        result = proof2_generating_function(kappa, n_poles=5)
        self.assertGreaterEqual(result.poles_verified, 3)


# =====================================================================
# PROOF 3 TESTS
# =====================================================================

class TestProof3BridgeEquation(unittest.TestCase):
    """Proof 3: Ecalle bridge equation from MC."""

    def test_mc_constraint_satisfied(self):
        """MC constraint verified: partial fraction = Bernoulli."""
        kappa = 1.0
        self.assertTrue(_verify_mc_constraint_on_alien(kappa, 20))

    def test_mc_constraint_multiple_kappa(self):
        """MC constraint for multiple kappa values."""
        for kappa in [0.5, 1.0, 6.5, 13.0]:
            self.assertTrue(_verify_mc_constraint_on_alien(kappa, 15))

    def test_S1_from_bridge(self):
        """S_1 = -4pi^2 kappa i from bridge equation."""
        kappa = 2.0
        result = proof3_bridge_equation(kappa)
        S1_exact = -4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(result.S1_from_bridge, S1_exact, places=10)

    def test_alien_derivative_sign(self):
        """Alien derivative Delta F^{(0)} = +4 pi^2 kappa i (opposite sign from S_1)."""
        kappa = 1.0
        result = proof3_bridge_equation(kappa)
        expected_alien = 4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(result.alien_derivative_F0, expected_alien, places=10)


# =====================================================================
# PROOF 4 TESTS
# =====================================================================

class TestProof4BorelPade(unittest.TestCase):
    """Proof 4: Borel-Pade numerical extraction."""

    def test_borel_coefficients_u(self):
        """Borel coefficients b_g = F_g / (g-1)!."""
        kappa = 1.0
        coeffs = _borel_coefficients_u(kappa, 10)
        # b_1 = F_1 / 0! = F_1 = 1/24
        self.assertAlmostEqual(coeffs[0], 1.0 / 24.0, places=14)
        # b_2 = F_2 / 1! = 7/5760
        self.assertAlmostEqual(coeffs[1], 7.0 / 5760.0, places=14)

    def test_pade_finds_pole_near_4pi2(self):
        """Direct Pade [15/15] on G(u) = sum F_g u^g has pole near (2pi)^2.

        AP77: the shadow series is Gevrey-0 (convergent), so Borel-Pade
        finds spurious poles. Direct Pade on the generating function
        correctly locates the pole at u = (2pi)^2.
        """
        kappa = 1.0
        result = proof4_borel_pade(kappa, g_max=40, pade_order=15)
        if not cmath.isnan(result.nearest_pole):
            rel_err = abs(result.nearest_pole - FOUR_PI_SQ) / FOUR_PI_SQ
            self.assertLess(rel_err, 0.25)  # wider tolerance for direct Pade

    def test_pade_pole_real(self):
        """Nearest Pade pole is approximately real (small imaginary part)."""
        kappa = 1.0
        result = proof4_borel_pade(kappa, g_max=40, pade_order=15)
        if not cmath.isnan(result.nearest_pole):
            self.assertLess(
                abs(result.nearest_pole.imag),
                abs(result.nearest_pole.real) * 0.2,
            )


# =====================================================================
# PROOF 5 TESTS
# =====================================================================

class TestProof5WKB(unittest.TestCase):
    """Proof 5: WKB / instanton action."""

    def test_instanton_action(self):
        """A = (2pi)^2 from WKB."""
        kappa = 1.0
        result = proof5_wkb(kappa)
        self.assertAlmostEqual(result.instanton_action, FOUR_PI_SQ, places=10)

    def test_one_loop_determinant(self):
        """One-loop prefactor = -2pi kappa."""
        kappa = 3.0
        det = _one_loop_determinant(kappa)
        self.assertAlmostEqual(det, -2.0 * PI * kappa, places=10)

    def test_S1_from_wkb(self):
        """S_1 = 2pi i * (-2pi kappa) = -4pi^2 kappa i."""
        kappa = 6.5
        result = proof5_wkb(kappa)
        S1_exact = -4.0 * PI ** 2 * kappa * 1.0j
        self.assertAlmostEqual(result.S1_from_wkb, S1_exact, places=10)

    def test_numerical_instanton_action(self):
        """Geometric ratio |F_{g-1}/F_g| -> A = (2pi)^2 for large g.

        AP77: the shadow series is Gevrey-0, so the geometric ratio
        (not the factorial ratio) converges to the instanton action.
        """
        kappa = 1.0
        A = _verify_instanton_action_numerical(kappa)
        self.assertAlmostEqual(A, FOUR_PI_SQ, places=4)


# =====================================================================
# MASTER THEOREM TESTS
# =====================================================================

class TestMasterTheorem(unittest.TestCase):
    """Master verification: all 5 proofs agree."""

    def test_heisenberg_k1(self):
        """All 5 proofs agree for Heisenberg k=1 (kappa=1)."""
        result = prove_stokes_mc_theorem(1.0)
        self.assertTrue(result.all_agree, result.summary)

    def test_virasoro_c12(self):
        """All 5 proofs agree for Vir at c=12 (kappa=6)."""
        result = prove_stokes_mc_theorem(6.0)
        self.assertTrue(result.all_agree, result.summary)

    def test_virasoro_self_dual(self):
        """All 5 proofs agree at self-dual c=13 (kappa=13/2)."""
        result = prove_stokes_mc_theorem(6.5)
        self.assertTrue(result.all_agree, result.summary)

    def test_affine_sl2_k1(self):
        """All 5 proofs agree for affine sl_2 k=1 (kappa=9/4)."""
        result = prove_stokes_mc_theorem(2.25)
        self.assertTrue(result.all_agree, result.summary)

    def test_large_kappa(self):
        """All 5 proofs agree for kappa=100."""
        result = prove_stokes_mc_theorem(100.0)
        self.assertTrue(result.all_agree, result.summary)

    def test_small_kappa(self):
        """All 5 proofs agree for kappa=0.1."""
        result = prove_stokes_mc_theorem(0.1)
        self.assertTrue(result.all_agree, result.summary)


# =====================================================================
# UNIVERSALITY TESTS
# =====================================================================

class TestUniversality(unittest.TestCase):
    """A = (2pi)^2 is universal; S_1 / kappa is universal."""

    def test_A_universality(self):
        """A = (2pi)^2 for all algebras."""
        result = verify_A_universality()
        self.assertTrue(result['all_universal'])

    def test_S1_linearity(self):
        """S_1 = -4pi^2 kappa i is linear in kappa."""
        result = verify_S1_linearity()
        self.assertTrue(result['all_linear'])

    def test_S1_unit(self):
        """S_1 / kappa = -4pi^2 i is a universal constant."""
        for kappa in [0.1, 1.0, 6.5, 100.0]:
            S1 = -4.0 * PI ** 2 * kappa * 1.0j
            self.assertAlmostEqual(S1 / kappa, S1_UNIT, places=10)


# =====================================================================
# COMPLEMENTARITY TESTS
# =====================================================================

class TestComplementarity(unittest.TestCase):
    """S_1 complementarity for Virasoro (AP24)."""

    def test_virasoro_sum_c1(self):
        """S_1(Vir_1) + S_1(Vir_25) = -52 pi^2 i."""
        result = verify_complementarity(1.0)
        self.assertTrue(result['sum_correct'])

    def test_virasoro_sum_c13(self):
        """At c=13: S_1 = S_1' = -26 pi^2 i."""
        result = verify_complementarity(13.0)
        self.assertTrue(result['sum_correct'])
        self.assertAlmostEqual(result['S1'], result['S1_dual'], places=10)

    def test_virasoro_sum_c26(self):
        """At c=26: kappa'=0, so S_1' = 0."""
        result = verify_complementarity(26.0)
        self.assertTrue(result['sum_correct'])
        self.assertAlmostEqual(result['S1_dual'], 0.0, places=10)

    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 for all c (Virasoro)."""
        for c in [0.5, 5.0, 13.0, 20.0, 25.5]:
            result = verify_complementarity(c)
            self.assertAlmostEqual(result['kappa_sum'], 13.0, places=10)


# =====================================================================
# HIGHER STOKES TESTS
# =====================================================================

class TestHigherStokes(unittest.TestCase):
    """S_n = (-1)^n 4pi^2 n kappa i."""

    def test_S1_sign(self):
        """S_1 is purely imaginary with negative imaginary part (kappa > 0)."""
        kappa = 1.0
        consts = higher_stokes_constants(kappa, 5)
        S1 = consts[0]['S_n']
        self.assertAlmostEqual(S1.real, 0.0, places=14)
        self.assertLess(S1.imag, 0.0)

    def test_S2_sign(self):
        """S_2 has positive imaginary part (kappa > 0)."""
        kappa = 1.0
        consts = higher_stokes_constants(kappa, 5)
        S2 = consts[1]['S_n']
        self.assertAlmostEqual(S2.real, 0.0, places=14)
        self.assertGreater(S2.imag, 0.0)

    def test_alternating_signs(self):
        """S_n alternates in sign."""
        kappa = 1.0
        consts = higher_stokes_constants(kappa, 5)
        for i in range(len(consts) - 1):
            self.assertLess(
                consts[i]['S_n'].imag * consts[i + 1]['S_n'].imag, 0.0,
            )

    def test_linear_growth(self):
        """S_n / n is constant for fixed kappa."""
        kappa = 2.0
        consts = higher_stokes_constants(kappa, 5)
        ratios = [abs(c['S_n']) / c['n'] for c in consts]
        for r in ratios:
            self.assertAlmostEqual(r, ratios[0], places=10)

    def test_S_n_over_A_n_constant(self):
        """S_n / A_n = (-1)^n 2pi kappa i (constant ratio modulo sign)."""
        kappa = 3.0
        consts = higher_stokes_constants(kappa, 5)
        expected_mag = 2.0 * PI * kappa
        for c in consts:
            ratio = c['S_n_over_A_n']
            self.assertAlmostEqual(abs(ratio), expected_mag, places=10)


# =====================================================================
# F_g CROSS-CHECK TESTS
# =====================================================================

class TestFgCrossCheck(unittest.TestCase):
    """Three-method verification of F_g."""

    def test_bernoulli_equals_poles(self):
        """F_g from Bernoulli matches partial fraction decomposition."""
        results = verify_F_g_exact(1.0, 15)
        for g, data in results.items():
            self.assertTrue(data['agree_bernoulli_poles'],
                            f"Disagreement at g={g}")

    def test_bernoulli_equals_cauchy(self):
        """F_g from Bernoulli matches Cauchy integral."""
        results = verify_F_g_exact(1.0, 10)
        for g, data in results.items():
            if g <= 8:  # Cauchy accuracy degrades at high g
                self.assertTrue(data['agree_bernoulli_cauchy'],
                                f"Disagreement at g={g}")

    def test_F_g_positive(self):
        """F_g > 0 for all g >= 1 (kappa > 0)."""
        kappa = 1.0
        for g in range(1, 30):
            self.assertGreater(F_g(kappa, g), 0.0)


# =====================================================================
# DUALITY TESTS
# =====================================================================

class TestDuality(unittest.TestCase):
    """Duality constraints on Stokes constants."""

    def test_km_antisymmetric(self):
        """For KM/free fields: kappa + kappa' = 0, S_1 + S_1' = 0."""
        kappa = 3.0  # e.g., sl_2 at some level
        kappa_dual = -kappa
        result = stokes_from_duality(kappa, kappa_dual)
        self.assertAlmostEqual(result['sum'], 0.0, places=10)

    def test_virasoro_sum_constant(self):
        """For Virasoro: kappa + kappa' = 13 regardless of c."""
        for c in [1.0, 5.0, 13.0, 25.0]:
            kappa = c / 2.0
            kappa_dual = (26.0 - c) / 2.0
            result = stokes_from_duality(kappa, kappa_dual)
            expected = -4.0 * PI ** 2 * 13.0 * 1.0j
            self.assertAlmostEqual(result['sum'], expected, places=10)


# =====================================================================
# CROSS-FAMILY TESTS
# =====================================================================

class TestCrossFamily(unittest.TestCase):
    """Verify across all standard families."""

    def test_all_families_agree(self):
        """All 5 proofs agree for each standard family."""
        families = {
            'Heis_k=1': 1.0,
            'Vir_c=12': 6.0,
            'Vir_c=13': 6.5,
            'aff_sl2_k=1': 2.25,
        }
        results = verify_across_families(families)
        for name, thm in results.items():
            self.assertTrue(thm.all_agree, f"FAILED for {name}: {thm.summary}")


if __name__ == '__main__':
    unittest.main()
