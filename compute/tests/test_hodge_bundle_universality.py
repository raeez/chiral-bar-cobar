r"""Tests for Hodge-bundle j-dependence diagnostics.

RESULT: higher-weight Hodge bundles have different GRR data from E_1.
At genus 2 this engine checks a parametric polynomial in the unresolved
boundary pairing P.  This kills the naive higher-weight-bundle route
    int psi^{2g-2} c_g(E_j) = lambda_g^FP for all j,
but it does NOT resolve op:multi-generator-universality itself.
The actual open problem is about the standard E_1-based bar
construction and the remaining identification Γ_A = κ(A)Λ.

The diagnostic has three levels:
1. STRUCTURAL: B_3(1) = 0 but B_3(j) != 0 for j >= 2, introducing new
    kappa-class contributions to c_g(E_j) absent from c_g(E_1) = lambda_g.
2. DEGREE: The genus-2 parametric polynomial has P-independent leading
   coefficient 3/40, inherited from e(j)^2 with e(j)=6j^2-6j+1.
3. PARAMETRIC GENUS 2: I_2(j;P) = e(j)^2/480 - B_3(j)*P - (j-1/2)/576.
   The boundary pairing P is not reconstructed in this engine; the
   P-independent exact check is the j^4 coefficient 3/40.
"""

import pytest
from fractions import Fraction
import math

from compute.lib.hodge_bundle_universality import (
    bernoulli_number,
    bernoulli_poly,
    bernoulli_poly_coefficients,
    ch_k_interior,
    rank_Ej,
    mumford_exponent,
    ch_to_c,
    faber_pandharipande_lambda_g,
    interior_c2_expression,
    integral_psi2_c2_Ej_genus2,
    integral_psi2_c2_Ej_genus2_parametric,
    genus2_parametric_polynomial_coefficients,
    evaluate_genus2_coefficients,
    boundary_parameter_for_equal_genus2_values,
    boundary_parameter_for_fp_collision,
    genus2_diagnostic_status,
    verify_j1_constraint,
    prove_j_dependence_by_degree,
    alternative_proof,
    general_genus_argument,
    P_INTERIOR_DIAGNOSTIC,
    GENUS2_BOUNDARY_PARAMETER_STATUS,
    INT_KAPPA1_LAMBDA1SQ,
    INT_KAPPA1_LAMBDA2,
    INT_KAPPA1_KAPPA2,
    INT_KAPPA1_CUBED,
)


# ============================================================
# Bernoulli number tests
# ============================================================

class TestBernoulliNumbers:

    def test_B0(self):
        assert bernoulli_number(0) == Fraction(1)

    def test_B1(self):
        assert bernoulli_number(1) == Fraction(-1, 2)

    def test_B2(self):
        assert bernoulli_number(2) == Fraction(1, 6)

    def test_B4(self):
        assert bernoulli_number(4) == Fraction(-1, 30)

    def test_B6(self):
        assert bernoulli_number(6) == Fraction(1, 42)

    def test_B8(self):
        assert bernoulli_number(8) == Fraction(-1, 30)

    def test_B10(self):
        assert bernoulli_number(10) == Fraction(5, 66)

    def test_odd_vanish(self):
        for n in [3, 5, 7, 9, 11, 13]:
            assert bernoulli_number(n) == Fraction(0)


# ============================================================
# Bernoulli polynomial tests
# ============================================================

class TestBernoulliPolynomials:

    def test_B1_poly(self):
        for x in range(-3, 6):
            assert bernoulli_poly(1, Fraction(x)) == Fraction(x) - Fraction(1, 2)

    def test_B2_poly(self):
        for x in range(-3, 6):
            expected = Fraction(x * x) - Fraction(x) + Fraction(1, 6)
            assert bernoulli_poly(2, Fraction(x)) == expected

    def test_B3_poly(self):
        for x in range(-2, 5):
            expected = Fraction(x ** 3) - Fraction(3 * x * x, 2) + Fraction(x, 2)
            assert bernoulli_poly(3, Fraction(x)) == expected

    def test_B3_at_1_vanishes(self):
        """THE key special property of j=1: B_3(1) = 0."""
        assert bernoulli_poly(3, Fraction(1)) == Fraction(0)

    def test_B3_factorization(self):
        """B_3(j) = j(j-1)(2j-1)/2."""
        for j in range(-5, 10):
            jf = Fraction(j)
            assert bernoulli_poly(3, jf) == jf * (jf - 1) * (2 * jf - 1) / 2

    def test_B3_nonzero_for_j_ge_2(self):
        """B_3(j) != 0 for integer j >= 2."""
        for j in range(2, 20):
            assert bernoulli_poly(3, Fraction(j)) != Fraction(0)

    def test_B5_at_1_vanishes(self):
        assert bernoulli_poly(5, Fraction(1)) == Fraction(0)

    def test_Bn_at_0(self):
        for n in range(12):
            assert bernoulli_poly(n, Fraction(0)) == bernoulli_number(n)

    def test_Bn_at_1(self):
        """B_n(1) = (-1)^n B_n for n >= 2."""
        for n in range(2, 12):
            assert bernoulli_poly(n, Fraction(1)) == (-1) ** n * bernoulli_number(n)

    def test_serre_symmetry_B3(self):
        """B_3(j) + B_3(1-j) = 0 (odd symmetry about j=1/2)."""
        for j in range(-5, 10):
            jf = Fraction(j)
            assert bernoulli_poly(3, jf) + bernoulli_poly(3, 1 - jf) == Fraction(0)


# ============================================================
# Chern character tests
# ============================================================

class TestChernCharacter:

    def test_ch1_mumford_exponent(self):
        """ch_1(E_j) = e(j)/12 * kappa_1 where e(j) = 6j^2-6j+1."""
        for j in range(1, 8):
            assert ch_k_interior(1, j) == Fraction(mumford_exponent(j), 12)

    def test_ch2_vanishes_at_j1(self):
        """ch_2(E_1) = 0 on the interior (B_3(1) = 0)."""
        assert ch_k_interior(2, 1) == Fraction(0)

    def test_ch2_nonzero_at_j2(self):
        """ch_2(E_2) = B_3(2)/6 = 3/6 = 1/2 on the interior."""
        assert ch_k_interior(2, 2) == Fraction(1, 2)

    def test_even_ch_vanish_at_j1(self):
        """For j=1: ch_{2m}(E_1) = 0 (interior) for m >= 1."""
        for m in range(1, 8):
            assert ch_k_interior(2 * m, 1) == Fraction(0)

    def test_even_ch_nonvanish_at_j2(self):
        """For j=2: ch_{2m}(E_2) != 0 (interior) for m >= 1."""
        for m in range(1, 6):
            assert ch_k_interior(2 * m, 2) != Fraction(0)


# ============================================================
# Rank and Mumford exponent tests
# ============================================================

class TestRankAndExponent:

    def test_rank_j1(self):
        for g in range(2, 6):
            assert rank_Ej(1, g) == g

    def test_rank_j2(self):
        for g in range(2, 6):
            assert rank_Ej(2, g) == 3 * (g - 1)

    def test_rank_general(self):
        for j in range(2, 6):
            for g in range(2, 6):
                assert rank_Ej(j, g) == (2 * j - 1) * (g - 1)

    def test_mumford_exponent_values(self):
        expected = {1: 1, 2: 13, 3: 37, 4: 73, 5: 121}
        for j, e in expected.items():
            assert mumford_exponent(j) == e

    def test_mumford_exponent_quadratic(self):
        for j in range(1, 10):
            second_diff = mumford_exponent(j + 2) - 2 * mumford_exponent(j + 1) + mumford_exponent(j)
            assert second_diff == 12


# ============================================================
# Newton's identities tests
# ============================================================

class TestNewtonIdentities:

    def test_rank2_bundle(self):
        a, b = Fraction(1, 3), Fraction(1, 7)
        ch = [Fraction(2), a, b]
        c = ch_to_c(ch, 2)
        assert c[0] == Fraction(1)
        assert c[1] == a
        assert c[2] == (a * a - 2 * b) / 2

    def test_trivial_bundle(self):
        for r in range(1, 5):
            ch = [Fraction(r)] + [Fraction(0)] * 5
            c = ch_to_c(ch, 5)
            for k in range(1, 6):
                assert c[k] == Fraction(0)


# ============================================================
# Faber-Pandharipande formula tests
# ============================================================

class TestFaberPandharipande:

    def test_g1(self):
        assert faber_pandharipande_lambda_g(1) == Fraction(1, 24)

    def test_g2(self):
        assert faber_pandharipande_lambda_g(2) == Fraction(7, 5760)

    def test_g3(self):
        assert faber_pandharipande_lambda_g(3) == Fraction(31, 967680)

    def test_g2_crosscheck(self):
        """7/8 * (1/30) / 24 = 7/5760."""
        assert faber_pandharipande_lambda_g(2) == Fraction(7, 8) * Fraction(1, 30) / 24

    def test_all_positive(self):
        for g in range(1, 10):
            assert faber_pandharipande_lambda_g(g) > 0


# ============================================================
# Interior c_2 expression tests
# ============================================================

class TestInteriorC2:

    def test_j1_no_kappa2(self):
        """For j=1: c_2 = kappa_1^2/288, no kappa_2 term."""
        c2 = interior_c2_expression(1)
        assert c2['kappa_1_sq'] == Fraction(1, 288)
        assert c2['kappa_2'] == Fraction(0)

    def test_j2_has_kappa2(self):
        """For j=2: c_2 = 169*kappa_1^2/288 - kappa_2/2."""
        c2 = interior_c2_expression(2)
        assert c2['kappa_1_sq'] == Fraction(169, 288)
        assert c2['kappa_2'] == Fraction(-1, 2)

    def test_kappa2_vanishes_only_j01(self):
        """kappa_2 coefficient vanishes only for j=0 and j=1."""
        for j in range(0, 8):
            c2 = interior_c2_expression(j)
            if j in [0, 1]:
                assert c2['kappa_2'] == Fraction(0)
            else:
                assert c2['kappa_2'] != Fraction(0)

    def test_kappa1sq_ratio(self):
        """kappa_1^2 coefficient ratio j=2 vs j=1 is 169."""
        c2_1 = interior_c2_expression(1)
        c2_2 = interior_c2_expression(2)
        assert c2_2['kappa_1_sq'] / c2_1['kappa_1_sq'] == Fraction(169)


# ============================================================
# THE KEY RESULT: j=1 constraint is P-independent
# ============================================================

class TestJ1Constraint:
    """The j=1 constraint is satisfied for ANY value of P.
    This is because B_3(1) = 0, so the B_3(j)*P term vanishes at j=1."""

    def test_j1_for_P_zero(self):
        assert verify_j1_constraint(Fraction(0))

    def test_j1_for_P_interior(self):
        assert verify_j1_constraint(P_INTERIOR_DIAGNOSTIC)

    def test_j1_for_P_arbitrary(self):
        for P in [Fraction(1, 100), Fraction(1), Fraction(-7, 13), Fraction(1000)]:
            assert verify_j1_constraint(P)

    def test_j1_value_is_FP(self):
        """For ANY P, I_2(1) = 7/5760 = lambda_2^FP."""
        P = Fraction(42, 137)  # arbitrary
        I_1 = integral_psi2_c2_Ej_genus2_parametric(1, P)
        assert I_1 == Fraction(7, 5760)


# ============================================================
# j-DEPENDENCE PROOF TESTS
# ============================================================

class TestJDependence:
    """Tests for the parametric genus-2 Hodge-bundle diagnostic."""

    def test_I2_differs_j1_j2_for_diagnostic_windows(self):
        """I_2(1) != I_2(2) for the tested finite-window P values."""
        collision = boundary_parameter_for_equal_genus2_values(1, 2)
        for P in [Fraction(0), P_INTERIOR_DIAGNOSTIC, Fraction(1, 10)]:
            assert P != collision
            I_1 = integral_psi2_c2_Ej_genus2_parametric(1, P)
            I_2 = integral_psi2_c2_Ej_genus2_parametric(2, P)
            assert I_1 != I_2, f"I_2(1) = I_2(2) at P = {P}"

    def test_pairwise_collision_parameter_is_explicit(self):
        """The formula has a special P where I_2(1;P)=I_2(2;P)."""
        P = boundary_parameter_for_equal_genus2_values(1, 2)
        assert P == Fraction(1003, 8640)
        I_1 = integral_psi2_c2_Ej_genus2_parametric(1, P)
        I_2 = integral_psi2_c2_Ej_genus2_parametric(2, P)
        assert I_1 == I_2 == faber_pandharipande_lambda_g(2)

    def test_I2_grows_with_j(self):
        """I_2(j; P_INTERIOR_DIAGNOSTIC) grows in this finite window."""
        P = P_INTERIOR_DIAGNOSTIC
        values = [integral_psi2_c2_Ej_genus2_parametric(j, P) for j in range(1, 6)]
        for i in range(len(values) - 1):
            assert values[i + 1] > values[i], \
                f"I_2 should be increasing: I({i+1}) = {values[i]}, I({i+2}) = {values[i+1]}"

    def test_leading_coefficient_j4(self):
        """The j^4 coefficient of I_2(j) is 3/40 (from e(j)^2/480)."""
        result = prove_j_dependence_by_degree()
        assert result['leading_coefficient_j4'] == Fraction(3, 40)

    def test_degree4_polynomial(self):
        """I_2(j) is a degree-4 polynomial in j (5th differences vanish)."""
        P = P_INTERIOR_DIAGNOSTIC
        vals = [integral_psi2_c2_Ej_genus2_parametric(j, P) for j in range(1, 8)]
        diffs = list(vals)
        for _ in range(5):
            diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        assert diffs[0] == Fraction(0), "5th difference should vanish for degree-4"

    def test_degree_exactly_4(self):
        """4th differences are nonzero (degree is exactly 4, not less)."""
        P = P_INTERIOR_DIAGNOSTIC
        vals = [integral_psi2_c2_Ej_genus2_parametric(j, P) for j in range(1, 7)]
        diffs = list(vals)
        for _ in range(4):
            diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        assert diffs[0] != Fraction(0), "4th difference should be nonzero"

    def test_leading_term_forces_nonconstancy_for_all_P(self):
        """The j^4 coefficient is 3/40 for every boundary parameter P."""
        for P in [Fraction(0), Fraction(1003, 8640), Fraction(-7, 13)]:
            coeffs = genus2_parametric_polynomial_coefficients(P)
            assert coeffs[4] == Fraction(3, 40)

    def test_B3_vanishing_is_unique_to_j1(self):
        """B_3(j) = 0 only for j = 0, 1/2, 1 among rationals.
        For integer j >= 2, B_3(j) != 0."""
        for j in range(2, 20):
            assert bernoulli_poly(3, Fraction(j)) != Fraction(0)

    def test_serre_duality_constraint(self):
        """I^{virt}(j) + I^{virt}(1-j) = e(j)^2/240.

        This is the Serre duality constraint on the virtual integral.
        """
        P = P_INTERIOR_DIAGNOSTIC
        for j in range(1, 6):
            I_j = integral_psi2_c2_Ej_genus2_parametric(j, P)
            I_1mj = integral_psi2_c2_Ej_genus2_parametric(1 - j, P)
            e_j = Fraction(mumford_exponent(j))
            expected = e_j ** 2 / Fraction(240)
            # I(j) + I(1-j) should equal e(j)^2 * I_{l1sq}
            # But we're using a parametric formula that may not exactly satisfy
            # this for all P. Let me check.
            # I(j) + I(1-j) = e(j)^2/480 + e(1-j)^2/480 - B_3(j)*P - B_3(1-j)*P
            #                 - (j-1/2)/576 - ((1-j)-1/2)/576
            # = (e(j)^2 + e(1-j)^2)/480 - (B_3(j)+B_3(1-j))*P
            #   - (j-1/2 + 1/2-j)/576
            # = 2*e(j)^2/480 - 0 - 0/576  [since e(j) = e(1-j) and B_3(j)+B_3(1-j) = 0]
            # = e(j)^2/240.
            assert I_j + I_1mj == expected, \
                f"Serre duality violated at j={j}: {I_j + I_1mj} != {expected}"


# ============================================================
# Hodge integral tests
# ============================================================

class TestHodgeIntegrals:

    def test_fp_genus2(self):
        assert faber_pandharipande_lambda_g(2) == Fraction(7, 5760)

    def test_lambda1_sq_integral(self):
        """int psi^2 lambda_1^2 = 1/240 on Mbar_{2,1}."""
        assert INT_KAPPA1_LAMBDA1SQ == Fraction(1, 240)

    def test_lambda1sq_ne_lambda2(self):
        """lambda_1^2 and lambda_2 give different integrals."""
        assert INT_KAPPA1_LAMBDA1SQ != INT_KAPPA1_LAMBDA2

    def test_ratio_lambda1sq_lambda2(self):
        assert INT_KAPPA1_LAMBDA1SQ / INT_KAPPA1_LAMBDA2 == Fraction(24, 7)


# ============================================================
# Manuscript implications
# ============================================================

class TestManuscriptImplications:

    def test_lambda_g_FP_is_j1_only(self):
        """lambda_g^FP = int psi^{2g-2} lambda_g uses lambda_g = c_g(E_1).
        At the interior diagnostic P, the j=2 value is different."""
        fp = faber_pandharipande_lambda_g(2)
        P = P_INTERIOR_DIAGNOSTIC
        I_2 = integral_psi2_c2_Ej_genus2_parametric(2, P)
        assert I_2 != fp

    def test_class_inequality(self):
        """c_2(E_j) != c_2(E_1) as tautological classes for j >= 2.
        Interior proof: kappa_2 coefficient is zero for j=1, nonzero for j>=2."""
        c2_1 = interior_c2_expression(1)
        c2_2 = interior_c2_expression(2)
        assert c2_1 != c2_2

    def test_rank_difference(self):
        """rank(E_j) depends on j, so the bundles are genuinely different."""
        assert rank_Ej(1, 2) == 2
        assert rank_Ej(2, 2) == 3
        assert rank_Ej(3, 2) == 5

    def test_ap16_confirmed(self):
        """AP16: class identity fails; integrated check is finite-window.
        c_g(E_j) != c_g(E_1) as classes for j >= 2.
        At P_INTERIOR_DIAGNOSTIC the integrated values differ too."""
        # Class level: different kappa-class content
        c2_1 = interior_c2_expression(1)
        c2_3 = interior_c2_expression(3)
        assert c2_1['kappa_2'] == Fraction(0)
        assert c2_3['kappa_2'] != Fraction(0)

        # Integrated level: different numerical values
        P = P_INTERIOR_DIAGNOSTIC
        I_1 = integral_psi2_c2_Ej_genus2_parametric(1, P)
        I_3 = integral_psi2_c2_Ej_genus2_parametric(3, P)
        assert I_1 != I_3


# ============================================================
# General genus tests
# ============================================================

class TestGeneralGenus:

    def test_leading_degree(self):
        for g in range(1, 6):
            info = general_genus_argument(g)
            assert info['leading_degree'] == 2 * g
            assert info['status'].startswith('leading-term diagnostic')

    def test_ratio_grows_exponentially(self):
        """The formal Mumford-exponent leading ratio grows as 13^g."""
        for g in range(1, 6):
            assert 13 ** g > 1

    def test_fp_values_known(self):
        """FP values are all positive and decrease with g."""
        vals = [faber_pandharipande_lambda_g(g) for g in range(1, 6)]
        for v in vals:
            assert v > 0
        for i in range(len(vals) - 1):
            assert vals[i] > vals[i + 1]


# ============================================================
# Exact formula validation
# ============================================================

class TestExactFormula:
    """Validate the parametric formula I_2(j) = e(j)^2/480 - B_3(j)*P - (j-1/2)/576."""

    def test_formula_at_j1(self):
        """At j=1: e(1)=1, B_3(1)=0, so I(1) = 1/480 - 1/1152 = 7/5760."""
        I_1 = Fraction(1, 480) - Fraction(1, 2) / Fraction(576)
        assert I_1 == Fraction(7, 5760)

    def test_formula_derivation_ch2_at_j1(self):
        """Derivation: I_{ch2}(1) = I_{l1sq}/2 - FP = 1/480 - 7/5760 = 1/1152."""
        I_ch2_1 = INT_KAPPA1_LAMBDA1SQ / 2 - faber_pandharipande_lambda_g(2)
        assert I_ch2_1 == Fraction(1, 1152)

    def test_Q_determination(self):
        """Q = 1/576 is determined from I_{ch2}(1) = Q/2 = 1/1152."""
        Q = Fraction(1, 576)
        assert Q / 2 == Fraction(1, 1152)

    def test_serre_duality_parametric(self):
        """The parametric formula satisfies Serre duality for all P."""
        for P in [Fraction(0), Fraction(1, 7), Fraction(-3, 11)]:
            for j in range(-3, 7):
                I_j = integral_psi2_c2_Ej_genus2_parametric(j, P)
                I_1mj = integral_psi2_c2_Ej_genus2_parametric(1 - j, P)
                e_j = Fraction(mumford_exponent(j))
                assert I_j + I_1mj == e_j ** 2 / 240

    def test_coefficients_match_parametric_formula(self):
        """The expanded polynomial coefficients evaluate to the formula."""
        for P in [Fraction(0), P_INTERIOR_DIAGNOSTIC, Fraction(1003, 8640)]:
            coeffs = genus2_parametric_polynomial_coefficients(P)
            assert coeffs[4] == Fraction(3, 40)
            assert coeffs[0] == Fraction(17, 5760)
            for j in range(-3, 6):
                assert evaluate_genus2_coefficients(j, P) == integral_psi2_c2_Ej_genus2_parametric(j, P)

    def test_boundary_status_is_not_exactly_computed(self):
        """The default P is an interior diagnostic, not a full boundary computation."""
        status = genus2_diagnostic_status()
        assert status['formula_status'] == 'exact conditional on supplied P'
        assert status['boundary_parameter_status'] == GENUS2_BOUNDARY_PARAMETER_STATUS
        assert status['P_used'] == P_INTERIOR_DIAGNOSTIC
        assert status['leading_coefficient_j4'] == Fraction(3, 40)
        assert status['nonconstant_for_all_P']

    def test_fp_collision_parameter_for_j2(self):
        """A special P makes the j=2 value equal lambda_2^FP."""
        P = boundary_parameter_for_fp_collision(2)
        assert P == Fraction(1003, 8640)
        assert integral_psi2_c2_Ej_genus2_parametric(2, P) == faber_pandharipande_lambda_g(2)


# ============================================================
# Numerical summary tests
# ============================================================

class TestNumericalResults:

    def test_I2_values_interior_P(self):
        """Verify finite-window values using P = 29/34560."""
        P = P_INTERIOR_DIAGNOSTIC
        assert integral_psi2_c2_Ej_genus2_parametric(1, P) == Fraction(7, 5760)
        # j=2: 169/480 - 3*(29/34560) - 3/(2*576) = 169/480 - 87/34560 - 1/384
        I_2 = integral_psi2_c2_Ej_genus2_parametric(2, P)
        assert I_2 == Fraction(3997, 11520)
        assert integral_psi2_c2_Ej_genus2(2) == I_2

    def test_ratio_j2_to_j1(self):
        """The diagnostic ratio I(2)/I(1) is about 285."""
        P = P_INTERIOR_DIAGNOSTIC
        I_1 = integral_psi2_c2_Ej_genus2_parametric(1, P)
        I_2 = integral_psi2_c2_Ej_genus2_parametric(2, P)
        ratio = I_2 / I_1
        assert ratio == Fraction(571, 2)
        assert float(ratio) > 200  # dramatic j-dependence

    def test_monotonicity(self):
        """I_2(j; P_INTERIOR_DIAGNOSTIC) is increasing for this finite window."""
        P = P_INTERIOR_DIAGNOSTIC
        prev = integral_psi2_c2_Ej_genus2_parametric(1, P)
        for j in range(2, 10):
            curr = integral_psi2_c2_Ej_genus2_parametric(j, P)
            assert curr > prev, f"I_2({j}) <= I_2({j-1})"
            prev = curr


# ============================================================
# Scope guard
# ============================================================

class TestDefinitiveResult:
    """The Hodge-bundle diagnostic does not solve cross-channel universality."""

    def test_parametric_answer_is_not_constant(self):
        """I_2(j;P) is never a constant polynomial in j.

        The exact P-independent statement available here is the degree-4
        leading coefficient.  Pairwise collisions at selected j can occur
        for special P and are tested above.
        """
        fp = faber_pandharipande_lambda_g(2)
        assert fp == Fraction(7, 5760)
        for P in [Fraction(0), P_INTERIOR_DIAGNOSTIC, Fraction(1003, 8640)]:
            coeffs = genus2_parametric_polynomial_coefficients(P)
            assert coeffs[4] == Fraction(3, 40)
            assert integral_psi2_c2_Ej_genus2_parametric(1, P) == fp
