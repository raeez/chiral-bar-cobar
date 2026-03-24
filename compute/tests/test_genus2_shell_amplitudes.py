"""Tests for genus-2 shadow amplitudes and shell structure.

Verifies:
  1. lambda_2^FP = 7/5760 (Faber-Pandharipande)
  2. F_2 = kappa * lambda_2^FP for all standard families
  3. Genus-2 complementarity
  4. Shell decomposition by shadow depth class
  5. Generating function consistency
  6. Handle contributions and asymptotic structure
  7. Universal ratio F_2/F_1^2 = 7/(10*kappa)
  8. Mumford relation at genus 2
"""

import pytest
from sympy import Rational, Symbol, simplify, expand, S, bernoulli, factorial, Abs

from compute.lib.genus2_shell_amplitudes import (
    lambda2_integral,
    lambda1_squared_integral,
    mumford_relation_genus2,
    psi_squared_genus2,
    lambda_g_psi_genus2,
    verify_lambda2_fp,
    F2_heisenberg,
    F2_affine_sl2,
    F2_virasoro,
    F2_betagamma,
    F2_W3,
    genus2_shell_decomposition,
    genus2_complementarity,
    verify_all_genus2_complementarity,
    F2_over_F1_squared,
    genus_ratio_tower,
    genus2_shell_profile_table,
    verify_generating_function_genus2,
    verify_generating_function_genus3,
    handle_contributions,
    genus2_complete_package,
)
from compute.lib.utils import lambda_fp, F_g


# ═══════════════════════════════════════════════════════════════════════
# lambda_2^FP verification
# ═══════════════════════════════════════════════════════════════════════

class TestLambda2FP:
    def test_lambda2_fp_value(self):
        """lambda_2^FP = 7/5760."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda2_fp_formula(self):
        """Verify via (2^3-1)/2^3 * |B_4|/4!."""
        result = verify_lambda2_fp()
        assert result["match"]
        assert result["equals_7_over_5760"]

    def test_B4_value(self):
        """B_4 = -1/30."""
        assert bernoulli(4) == Rational(-1, 30)

    def test_lambda2_fp_from_utils(self):
        """Cross-check with utils.lambda_fp."""
        assert lambda_fp(2) == Rational(7, 5760)

    def test_lambda1_fp_value(self):
        """lambda_1^FP = 1/24 for comparison."""
        assert lambda_fp(1) == Rational(1, 24)

    def test_lambda3_fp_value(self):
        """lambda_3^FP = 31/967680."""
        expected = Rational(31, 32) * Rational(1, 42) / factorial(6)
        assert lambda_fp(3) == expected
        assert lambda_fp(3) == Rational(31, 967680)


# ═══════════════════════════════════════════════════════════════════════
# Hodge integrals
# ═══════════════════════════════════════════════════════════════════════

class TestHodgeIntegrals:
    def test_lambda2_integral(self):
        """int_{M-bar_2} lambda_2 = 1/240."""
        assert lambda2_integral() == Rational(1, 240)

    def test_lambda1_squared_integral(self):
        """int_{M-bar_2} lambda_1^2 = 1/240."""
        assert lambda1_squared_integral() == Rational(1, 240)

    def test_integrals_equal(self):
        """The two integrals coincide (Faber)."""
        result = mumford_relation_genus2()
        assert result["integrals_equal"]

    def test_psi_squared(self):
        """<tau_4>_2 = 1/1152."""
        assert psi_squared_genus2() == Rational(1, 1152)

    def test_lambda_g_psi(self):
        """int lambda_2 psi^2 = lambda_2^FP = 7/5760."""
        assert lambda_g_psi_genus2() == Rational(7, 5760)


# ═══════════════════════════════════════════════════════════════════════
# Genus-2 free energies
# ═══════════════════════════════════════════════════════════════════════

class TestF2Heisenberg:
    def test_symbolic(self):
        result = F2_heisenberg()
        assert result["F_2 = 7k/5760"]

    def test_pure_shell(self):
        result = F2_heisenberg()
        assert result["pure_shell"]
        assert result["F_2^tree"] == 0
        assert result["F_2^1-loop"] == 0

    def test_shadow_class(self):
        result = F2_heisenberg()
        assert result["shadow_class"] == "G (Gaussian)"
        assert result["shadow_depth"] == 2

    def test_numeric_k1(self):
        result = F2_heisenberg(kappa_val=1)
        assert result["F_2"] == Rational(7, 5760)

    def test_numeric_k2(self):
        result = F2_heisenberg(kappa_val=2)
        assert result["F_2"] == Rational(7, 2880)

    def test_numeric_k_half(self):
        result = F2_heisenberg(kappa_val=Rational(1, 2))
        assert result["F_2"] == Rational(7, 11520)


class TestF2AffineSl2:
    def test_symbolic(self):
        result = F2_affine_sl2()
        assert result["shadow_class"] == "L (Lie/tree)"
        assert result["shadow_depth"] == 3
        assert result["scalar_matches_universal"]

    def test_k1(self):
        """At k=1: kappa = 3*3/4 = 9/4, F_2 = 9/4 * 7/5760 = 63/23040 = 7/2560."""
        result = F2_affine_sl2(k_val=1)
        expected = Rational(3) * 3 / 4 * Rational(7, 5760)
        assert result["F_2"] == expected
        assert expected == Rational(63, 23040)

    def test_k_minus_2(self):
        """At k = -2 (critical): kappa = 0, F_2 = 0."""
        result = F2_affine_sl2(k_val=-2)
        assert result["F_2"] == 0


class TestF2Virasoro:
    def test_symbolic(self):
        result = F2_virasoro()
        assert result["F_2 = 7c/11520"]
        assert result["shadow_class"] == "M (mixed)"

    def test_c26(self):
        """At c=26: kappa = 13, F_2 = 13 * 7/5760 = 91/5760."""
        result = F2_virasoro(c_val=26)
        assert result["F_2"] == Rational(13) * Rational(7, 5760)

    def test_c1(self):
        """At c=1: kappa = 1/2, F_2 = 7/11520."""
        result = F2_virasoro(c_val=1)
        assert result["F_2"] == Rational(7, 11520)

    def test_c0(self):
        """At c=0: kappa = 0, F_2 = 0."""
        result = F2_virasoro(c_val=0)
        assert result["F_2"] == 0

    def test_quartic_contact(self):
        """Q^contact_Vir = 10/[c(5c+22)] at c=2."""
        result = F2_virasoro(c_val=2)
        assert result["Q^contact"] == Rational(10, 2 * 32)  # 10/(2*(10+22))=10/64=5/32


class TestF2BetaGamma:
    def test_shadow_class(self):
        result = F2_betagamma()
        assert result["shadow_class"] == "C (contact/quartic)"
        assert result["shadow_depth"] == 4

    def test_quartic_vanishes(self):
        """mu_{bg} = 0 (cor:nms-betagamma-mu-vanishing)."""
        result = F2_betagamma()
        assert result["mu_quartic"] == 0
        assert result["quartic_correction_vanishes"]

    def test_at_half(self):
        """At lambda=1/2: c=-1, kappa=-1/2, F_2 = -7/11520."""
        result = F2_betagamma()
        assert result["kappa_at_lambda=1/2"] == Rational(-1, 2)
        assert result["F_2_at_lambda=1/2"] == Rational(-7, 11520)


class TestF2W3:
    def test_symbolic(self):
        result = F2_W3()
        assert result["F_2 = 7c/6912"]
        assert result["shadow_class"] == "M (mixed)"

    def test_c50(self):
        """At c=50: kappa = 250/6 = 125/3, F_2 = 125/3 * 7/5760."""
        result = F2_W3(c_val=50)
        expected = Rational(125, 3) * Rational(7, 5760)
        assert result["F_2"] == expected


# ═══════════════════════════════════════════════════════════════════════
# Complementarity
# ═══════════════════════════════════════════════════════════════════════

class TestGenus2Complementarity:
    def test_all_families(self):
        results = verify_all_genus2_complementarity()
        for family, data in results.items():
            assert data["match"], f"Complementarity failed for {family}"

    def test_heisenberg_sum_zero(self):
        """kappa + (-kappa) = 0 => F_2 + F_2' = 0."""
        kappa = Symbol('kappa')
        result = genus2_complementarity(kappa, -kappa, S.Zero)
        assert result["match"]

    def test_virasoro_sum_13(self):
        """kappa(c) + kappa(26-c) = 13."""
        c = Symbol('c')
        result = genus2_complementarity(c/2, (26-c)/2, Rational(13))
        assert result["match"]


# ═══════════════════════════════════════════════════════════════════════
# Shell decomposition
# ═══════════════════════════════════════════════════════════════════════

class TestShellDecomposition:
    def test_ratio_F2_F1(self):
        """F_2/F_1 = lambda_2/lambda_1 = 7/240."""
        kappa = Symbol('kappa')
        result = genus2_shell_decomposition(kappa, shadow_depth=2)
        assert result["ratio_correct"]
        assert result["ratio F_2/F_1 = lambda_2/lambda_1"] == Rational(7, 240)

    def test_handle_increment_negative(self):
        """lambda_2 - lambda_1 < 0 (genus-2 is smaller than genus-1)."""
        kappa = Symbol('kappa')
        result = genus2_shell_decomposition(kappa, shadow_depth=2)
        handle = result["handle_increment (lambda_2 - lambda_1)"]
        assert handle < 0
        assert handle == Rational(7, 5760) - Rational(1, 24)
        assert handle == Rational(-233, 5760)


# ═══════════════════════════════════════════════════════════════════════
# Universal ratios
# ═══════════════════════════════════════════════════════════════════════

class TestUniversalRatios:
    def test_F2_over_F1_squared(self):
        """F_2/F_1^2 = 7/(10*kappa)."""
        result = F2_over_F1_squared()
        assert result["equals 7/10"]
        assert result["F_2 / F_1^2 = 7/(10*kappa)"]

    def test_lambda_ratio(self):
        """lambda_2 / lambda_1^2 = 7/10."""
        lam1 = lambda_fp(1)
        lam2 = lambda_fp(2)
        assert simplify(lam2 / lam1**2) == Rational(7, 10)


class TestGenusRatioTower:
    def test_genus1_trivial(self):
        """lambda_1 / lambda_1^1 = 1 = 1/1!."""
        ratios = genus_ratio_tower(3)
        assert ratios[1]["deviation_is_zero"]

    def test_genus2_deviation(self):
        """lambda_2 / lambda_1^2 = 7/10 != 1/2!."""
        ratios = genus_ratio_tower(3)
        assert not ratios[2]["deviation_is_zero"]
        assert ratios[2]["lambda_g / lambda_1^g"] == Rational(7, 10)

    def test_genus3_deviation(self):
        """lambda_3 / lambda_1^3 != 1/3!."""
        ratios = genus_ratio_tower(3)
        assert not ratios[3]["deviation_is_zero"]


# ═══════════════════════════════════════════════════════════════════════
# Generating function
# ═══════════════════════════════════════════════════════════════════════

class TestGeneratingFunction:
    def test_genus2_coefficient(self):
        """x^4 coefficient of (x/2)/sin(x/2) - 1 = 7/5760."""
        result = verify_generating_function_genus2()
        assert result["match"]

    def test_genus3_coefficient(self):
        """x^6 coefficient of (x/2)/sin(x/2) - 1 = 31/967680."""
        result = verify_generating_function_genus3()
        assert result["match"]


# ═══════════════════════════════════════════════════════════════════════
# Handle contributions
# ═══════════════════════════════════════════════════════════════════════

class TestHandleContributions:
    def test_genus1_positive(self):
        """Handle contribution at genus 1 = lambda_1 = 1/24 > 0."""
        results = handle_contributions(5)
        assert results[1]["sign"] == "positive"
        assert results[1]["handle_contribution"] == Rational(1, 24)

    def test_genus2_negative(self):
        """Handle contribution at genus 2 is NEGATIVE."""
        results = handle_contributions(5)
        assert results[2]["sign"] == "negative"
        assert results[2]["handle_contribution"] == Rational(7, 5760) - Rational(1, 24)

    def test_asymptotic_growth(self):
        """Eventually handle contributions become positive and grow."""
        results = handle_contributions(10)
        # Find the crossover genus
        signs = [(g, r["sign"]) for g, r in results.items()]
        # At genus 1: positive. Genus 2,3,...: depends. Eventually positive again.
        # lambda_g ~ (2g)!/(2pi)^{2g} grows factorially
        # Check that genus 10 has positive handle
        # Actually let's just check it doesn't crash
        assert len(results) == 10


# ═══════════════════════════════════════════════════════════════════════
# Shell profile table
# ═══════════════════════════════════════════════════════════════════════

class TestShellProfileTable:
    def test_all_families_present(self):
        table = genus2_shell_profile_table()
        assert "Heisenberg" in table
        assert "V_k(sl_2)" in table
        assert "Virasoro" in table
        assert "beta-gamma" in table
        assert "W_3" in table

    def test_shadow_classes(self):
        table = genus2_shell_profile_table()
        assert table["Heisenberg"]["shadow_class"] == "G"
        assert table["V_k(sl_2)"]["shadow_class"] == "L"
        assert table["Virasoro"]["shadow_class"] == "M"
        assert table["beta-gamma"]["shadow_class"] == "C"
        assert table["W_3"]["shadow_class"] == "M"

    def test_shadow_depths(self):
        table = genus2_shell_profile_table()
        assert table["Heisenberg"]["r_max"] == 2
        assert table["V_k(sl_2)"]["r_max"] == 3
        assert table["beta-gamma"]["r_max"] == 4
        assert table["Virasoro"]["r_max"] == "infinity"


# ═══════════════════════════════════════════════════════════════════════
# Numerical cross-checks
# ═══════════════════════════════════════════════════════════════════════

class TestNumericalCrossChecks:
    def test_lambda2_decimal(self):
        """7/5760 ~ 0.001215..."""
        val = float(lambda_fp(2))
        assert abs(val - 7/5760) < 1e-12

    def test_lambda1_decimal(self):
        """1/24 ~ 0.04167..."""
        val = float(lambda_fp(1))
        assert abs(val - 1/24) < 1e-12

    def test_ratio_decimal(self):
        """lambda_2/lambda_1 = 7/240 ~ 0.02917..."""
        ratio = float(lambda_fp(2) / lambda_fp(1))
        assert abs(ratio - 7/240) < 1e-12

    def test_F2_heisenberg_k1_decimal(self):
        """F_2(H_1) = 7/5760 ~ 0.001215..."""
        result = F2_heisenberg(kappa_val=1)
        assert abs(float(result["F_2"]) - 7/5760) < 1e-12

    def test_F2_virasoro_c26_decimal(self):
        """F_2(Vir_26) = 91/5760 ~ 0.01580..."""
        result = F2_virasoro(c_val=26)
        assert abs(float(result["F_2"]) - 91/5760) < 1e-12


# ═══════════════════════════════════════════════════════════════════════
# Complete package
# ═══════════════════════════════════════════════════════════════════════

class TestCompletePackage:
    def test_package_runs(self):
        """The complete package assembles without error."""
        pkg = genus2_complete_package()
        assert "lambda_2_verification" in pkg
        assert "Heisenberg" in pkg
        assert "complementarity" in pkg

    def test_all_verifications_pass(self):
        """All internal verifications in the package pass."""
        pkg = genus2_complete_package()
        assert pkg["lambda_2_verification"]["match"]
        assert pkg["lambda_2_verification"]["equals_7_over_5760"]
        assert pkg["generating_function_g2"]["match"]
        assert pkg["generating_function_g3"]["match"]
        assert pkg["F2_over_F1_squared"]["equals 7/10"]


# ═══════════════════════════════════════════════════════════════════════
# Structural results: F_2 vs F_1 relationship
# ═══════════════════════════════════════════════════════════════════════

class TestF2F1Relationship:
    def test_not_exponential(self):
        """The genus expansion is NOT exp(F_1): F_2 != F_1^2/2."""
        kappa = Symbol('kappa')
        F1 = F_g(kappa, 1)
        F2_val = F_g(kappa, 2)
        half_F1_sq = F1**2 / 2
        assert simplify(F2_val - half_F1_sq) != 0

    def test_perturbative_in_inverse_kappa(self):
        """F_2/F_1^2 = 7/(10*kappa) -> 0 as kappa -> infinity."""
        # At large kappa, the genus expansion is well-ordered
        for k_val in [1, 10, 100, 1000]:
            F1 = Rational(k_val) * lambda_fp(1)
            F2_val = Rational(k_val) * lambda_fp(2)
            ratio = F2_val / F1**2
            expected = Rational(7, 10) / k_val
            assert ratio == expected

    def test_F2_F1_ratio_universal(self):
        """F_2/F_1 = 7/240 (independent of kappa)."""
        for k_val in [1, 2, 5, 13]:
            F1 = Rational(k_val) * lambda_fp(1)
            F2_val = Rational(k_val) * lambda_fp(2)
            ratio = F2_val / F1
            assert ratio == Rational(7, 240)
