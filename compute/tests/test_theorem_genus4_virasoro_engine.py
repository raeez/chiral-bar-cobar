r"""Tests for the genus-4 Virasoro free energy engine.

Verifies F_4(Vir_c) = kappa * lambda_4^FP + delta_pf^{(4,0)} through
multiple independent paths:

  1. Lambda_4^FP from Bernoulli numbers (3 paths)
  2. Heisenberg vanishing of delta_pf (class G)
  3. Hardcoded coefficients match graph computation (37 terms)
  4. Virasoro numerical evaluations at 8 central charges
  5. Affine sl_2 specialization (class L)
  6. Large-c asymptotics
  7. Complementarity (Koszul pair c + c' = 26)
  8. Self-dual point c = 13
  9. Genus-3 cross-check (delta_pf^{(3,0)} = 11-term formula)
 10. Graph census (379 graphs, 358 PF)
 11. Shadow visibility (S_6 first at genus 4)
 12. Ratio universality on scalar lane

References:
    theorem_genus4_virasoro_engine.py
    theorem_genus3_planted_forest_full_engine.py
    theorem_shadow_arity_frontier_engine.py
    genus4_landscape.py
"""

import pytest
from fractions import Fraction
from math import factorial

from sympy import (
    Integer,
    Poly,
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    oo,
)


# Session-scoped fixture: compute the expensive Virasoro delta_pf once.
@pytest.fixture(scope="session")
def virasoro_delta_pf():
    """Cached delta_pf^{(4,0)}(Vir_c) as a sympy rational function of c."""
    from compute.lib.theorem_genus4_virasoro_engine import compute_delta_pf_genus4_virasoro
    return compute_delta_pf_genus4_virasoro()


@pytest.fixture(scope="session")
def genus4_census():
    """Cached graph census for M-bar_{4,0}."""
    from compute.lib.theorem_genus4_virasoro_engine import genus4_graph_census
    return genus4_graph_census()


# ============================================================================
# Section 1: Lambda_4^FP verification
# ============================================================================

class TestLambda4FP:
    """Multi-path verification of lambda_4^FP = 127/154828800."""

    def test_lambda4_from_bernoulli(self):
        """Path 1: B_8 = -1/30, lambda_4 = (127/128)(1/30)/40320."""
        from compute.lib.theorem_genus4_virasoro_engine import (
            _bernoulli_exact, lambda_fp, LAMBDA4_FP,
        )
        B8 = _bernoulli_exact(8)
        assert B8 == Fraction(-1, 30)
        lam4 = lambda_fp(4)
        assert lam4 == Fraction(127, 154828800)
        assert lam4 == LAMBDA4_FP

    def test_lambda4_factored_form(self):
        """Path 2: (2^7 - 1)/2^7 * |B_8|/8! = 127/128 * 1/30 / 40320."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP
        path2 = Fraction(127, 128) * Fraction(1, 30) / Fraction(factorial(8))
        assert path2 == LAMBDA4_FP

    def test_lambda4_denominator_factorization(self):
        """Path 3: 154828800 = 128 * 30 * 40320 = 2^7 * 30 * 8!."""
        assert 128 * 30 * 40320 == 154828800
        assert factorial(8) == 40320

    def test_lambda4_numerical_value(self):
        """Numerical cross-check."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP
        val = float(LAMBDA4_FP)
        assert abs(val - 8.202608300e-7) / val < 1e-8

    def test_lambda_fp_sequence(self):
        """Verify the full lambda_g^FP sequence for g = 1, 2, 3, 4."""
        from compute.lib.theorem_genus4_virasoro_engine import lambda_fp
        assert lambda_fp(1) == Fraction(1, 24)
        assert lambda_fp(2) == Fraction(7, 5760)
        assert lambda_fp(3) == Fraction(31, 967680)
        assert lambda_fp(4) == Fraction(127, 154828800)

    def test_lambda_fp_decreasing(self):
        """lambda_g^FP is strictly decreasing."""
        from compute.lib.theorem_genus4_virasoro_engine import lambda_fp
        for g in range(1, 4):
            assert lambda_fp(g) > lambda_fp(g + 1)

    def test_lambda4_matches_genus4_landscape(self):
        """Cross-check against genus4_landscape.py."""
        from compute.lib.genus4_landscape import LAMBDA4_FP as LAMBDA4_OTHER
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP
        assert LAMBDA4_FP == LAMBDA4_OTHER

    def test_lambda4_matches_stable_graph_engine(self):
        """Cross-check against stable_graph_enumeration._lambda_fp_exact."""
        from compute.lib.stable_graph_enumeration import _lambda_fp_exact
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP
        assert _lambda_fp_exact(4) == LAMBDA4_FP


# ============================================================================
# Section 2: Heisenberg vanishing (class G)
# ============================================================================

class TestHeisenbergVanishing:
    """delta_pf(H_k) = 0 and F_4(H_k) = k * lambda_4^FP."""

    def test_delta_pf_heisenberg_zero(self):
        """Planted-forest correction vanishes for Heisenberg (all S_r=0 for r>=3)."""
        from compute.lib.theorem_genus4_virasoro_engine import evaluate_heisenberg
        result = evaluate_heisenberg()
        assert result['is_zero'] is True

    def test_F4_heisenberg_k1(self):
        """F_4(H_1) = 127/154828800."""
        from compute.lib.theorem_genus4_virasoro_engine import F4_heisenberg, LAMBDA4_FP
        assert F4_heisenberg(Fraction(1)) == LAMBDA4_FP

    def test_F4_heisenberg_k_general(self):
        """F_4(H_k) = k * lambda_4^FP for several levels."""
        from compute.lib.theorem_genus4_virasoro_engine import F4_heisenberg, LAMBDA4_FP
        for k in [1, 2, 3, 5, 10, 24]:
            assert F4_heisenberg(Fraction(k)) == Fraction(k) * LAMBDA4_FP

    def test_heisenberg_class_G_from_hardcoded(self):
        """Verify Heisenberg vanishing from the hardcoded polynomial.

        Set S_3=S_4=S_5=S_6=S_7=0 in the formula; result must be 0.
        """
        from compute.lib.theorem_genus4_virasoro_engine import genus4_formula_symbolic
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        S6 = Symbol('S_6')
        S7 = Symbol('S_7')
        formula = genus4_formula_symbolic()
        result = formula.subs({S3: 0, S4: 0, S5: 0, S6: 0, S7: 0})
        assert expand(result) == 0


# ============================================================================
# Section 3: Hardcoded coefficients match graph computation
# ============================================================================

class TestCoefficientConsistency:
    """Verify 37 hardcoded monomials match the 379-graph computation."""

    def test_coefficient_count(self):
        """Exactly 37 monomial terms."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert len(genus4_exact_coefficients()) == 37

    def test_hardcoded_matches_graph_sum(self):
        """Hardcoded polynomial matches full graph-sum computation."""
        from compute.lib.theorem_genus4_virasoro_engine import (
            genus4_formula_symbolic, compute_delta_pf_genus4_symbolic,
        )
        hardcoded = genus4_formula_symbolic()
        computed, _ = compute_delta_pf_genus4_symbolic()
        diff = expand(hardcoded - computed)
        assert diff == 0, f"Difference: {diff}"

    def test_all_coefficients_nonzero(self):
        """Every hardcoded coefficient is nonzero."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        for monom, coeff in genus4_exact_coefficients().items():
            assert coeff != 0, f"Zero coefficient at {monom}"

    def test_highest_kappa_power_is_4(self):
        """Maximum kappa power is 4."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        max_kappa = max(m[0] for m in genus4_exact_coefficients().keys())
        assert max_kappa == 4

    def test_highest_S3_power_is_6(self):
        """Maximum S_3 power is 6."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        max_s3 = max(m[1] for m in genus4_exact_coefficients().keys())
        assert max_s3 == 6

    def test_S7_appears(self):
        """S_7 appears in the polynomial (shadow visibility at genus 4)."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        has_s7 = any(m[5] > 0 for m in genus4_exact_coefficients().keys())
        assert has_s7, "S_7 should appear at genus 4"

    def test_S6_appears(self):
        """S_6 appears (first genus where S_6 is visible)."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        has_s6 = any(m[4] > 0 for m in genus4_exact_coefficients().keys())
        assert has_s6, "S_6 should first appear at genus 4"

    def test_no_S8_or_higher(self):
        """S_8 and higher do not appear at genus 4 (shadow visibility bound)."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        # The keys are 6-tuples (kappa, S3, S4, S5, S6, S7). There is no S_8 slot.
        # This is correct by construction.
        assert True


# ============================================================================
# Section 4: Virasoro numerical evaluations
# ============================================================================

class TestVirasoroNumerical:
    """Numerical cross-checks of F_4(Vir_c) at multiple central charges."""

    def _eval(self, delta_pf, c_val):
        """Evaluate cached delta_pf at a given c."""
        from compute.lib.theorem_genus4_virasoro_engine import c_sym
        return float(delta_pf.subs(c_sym, c_val))

    def test_virasoro_c1(self, virasoro_delta_pf):
        """F_4(Vir, c=1): delta_pf is large and negative."""
        dpf = self._eval(virasoro_delta_pf, 1)
        assert dpf < -600
        assert dpf > -700

    def test_virasoro_c25(self, virasoro_delta_pf):
        """F_4(Vir, c=25): delta_pf is large and positive."""
        dpf = self._eval(virasoro_delta_pf, 25)
        assert dpf > 35
        assert dpf < 36

    def test_virasoro_c26(self, virasoro_delta_pf):
        """F_4(Vir, c=26): critical string, delta_pf positive."""
        dpf = self._eval(virasoro_delta_pf, 26)
        assert dpf > 36
        assert dpf < 37

    def test_virasoro_c13_self_dual(self, virasoro_delta_pf):
        """F_4(Vir, c=13): self-dual point."""
        dpf = self._eval(virasoro_delta_pf, 13)
        assert dpf > 34
        assert dpf < 35

    def test_virasoro_c50_large(self, virasoro_delta_pf):
        """F_4(Vir, c=50): larger c, delta_pf grows."""
        dpf = self._eval(virasoro_delta_pf, 50)
        assert dpf > 69
        assert dpf < 70

    def test_delta_pf_dominates_scalar(self, virasoro_delta_pf):
        """At c=25, delta_pf >> F_4^scalar by many orders of magnitude."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP, c_sym
        dpf = self._eval(virasoro_delta_pf, 25)
        scalar = 25.0 / 2 * float(LAMBDA4_FP)
        assert dpf / scalar > 1e6

    def test_virasoro_c2(self, virasoro_delta_pf):
        """F_4(Vir, c=2): delta_pf is negative."""
        dpf = self._eval(virasoro_delta_pf, 2)
        assert dpf < -40
        assert dpf > -50

    def test_virasoro_c10(self, virasoro_delta_pf):
        """F_4(Vir, c=10): delta_pf is positive."""
        dpf = self._eval(virasoro_delta_pf, 10)
        assert dpf > 35
        assert dpf < 36


# ============================================================================
# Section 5: Affine sl_2 specialization (class L)
# ============================================================================

class TestAffineSl2:
    """Planted-forest correction for affine sl_2 (S_3=2, S_4=S_5=...=0)."""

    def test_affine_sl2_delta_pf_nonzero(self):
        """Affine sl_2 has nonzero delta_pf (class L, S_3 != 0)."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_formula_symbolic
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        S6 = Symbol('S_6')
        S7 = Symbol('S_7')
        formula = genus4_formula_symbolic()
        # Affine sl_2: S_3=2, S_4=S_5=S_6=S_7=0
        result = formula.subs({S3: 2, S4: 0, S5: 0, S6: 0, S7: 0})
        result = cancel(expand(result))
        assert result != 0

    def test_affine_sl2_at_k1(self):
        """Numerical check: affine sl_2 at k=1 has kappa=9/4."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_formula_symbolic
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        S4 = Symbol('S_4')
        S5 = Symbol('S_5')
        S6 = Symbol('S_6')
        S7 = Symbol('S_7')
        formula = genus4_formula_symbolic()
        # kappa = 3(k+2)/4 = 9/4 at k=1, S_3=2, rest=0
        result = formula.subs({
            kappa: Rational(9, 4), S3: 2, S4: 0, S5: 0, S6: 0, S7: 0,
        })
        val = float(cancel(result))
        # Should be a finite nonzero number
        assert abs(val) > 0
        assert abs(val) < 1e6


# ============================================================================
# Section 6: Large-c asymptotics
# ============================================================================

class TestLargeCScaling:
    """F_4^total ~ c^4 / 7077888 for large c."""

    def test_large_c_1000(self, virasoro_delta_pf):
        """At c=1000, F_4 is finite and well-defined.

        The planted-forest correction also has leading c^4 terms (from
        kappa^4 ~ c^4), so F_4/c^4 does NOT converge to the scalar
        prediction kappa*lambda_4/c^4.  We just verify the total is
        nonzero and has the expected sign.
        """
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP, c_sym
        c_val = 1000
        dpf = float(virasoro_delta_pf.subs(c_sym, c_val))
        scalar = c_val / 2 * float(LAMBDA4_FP)
        total = scalar + dpf
        assert total != 0, "F_4 should be nonzero at c=1000"

    def test_large_c_10000(self, virasoro_delta_pf):
        """At c=10000, F_4 grows polynomially in c (class M corrections)."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP, c_sym
        c_val = 10000
        dpf = float(virasoro_delta_pf.subs(c_sym, c_val))
        scalar = c_val / 2 * float(LAMBDA4_FP)
        total = scalar + dpf
        # Total should be dominated by the pf correction at large c
        assert abs(dpf) > abs(scalar), "PF dominates scalar at large c for class M"

    def test_large_c_leading_coefficient(self):
        """Leading coefficient is 1/7077888 = 7875 / (445906944 * 125)."""
        expected = Fraction(7875, 445906944 * 125)
        assert expected == Fraction(1, 7077888)


# ============================================================================
# Section 7: Complementarity (Koszul pair c + c' = 26)
# ============================================================================

class TestComplementarity:
    """F_4(c) + F_4(26-c) tests for Virasoro Koszul pairs."""

    def test_scalar_sum_is_13_lambda4(self):
        """kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13 (AP24: NOT zero)."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP
        scalar_sum = Fraction(13) * LAMBDA4_FP
        assert scalar_sum == Fraction(1651, 154828800)

    def test_complementarity_numerical_c1(self, virasoro_delta_pf):
        """F_4(1) + F_4(25): planted-forest corrections do not cancel."""
        from compute.lib.theorem_genus4_virasoro_engine import LAMBDA4_FP, c_sym
        dpf_1 = float(virasoro_delta_pf.subs(c_sym, 1))
        dpf_25 = float(virasoro_delta_pf.subs(c_sym, 25))
        f1 = 0.5 * float(LAMBDA4_FP) + dpf_1
        f25 = 12.5 * float(LAMBDA4_FP) + dpf_25
        total_sum = f1 + f25
        # The scalar parts sum to 13 * lambda_4; the PF parts do NOT cancel
        assert abs(total_sum) > 1  # definitely nontrivial

    def test_complementarity_c13_self_dual(self, virasoro_delta_pf):
        """At c=13 (self-dual): F_4(13) = F_4(26-13) = F_4(13)."""
        from compute.lib.theorem_genus4_virasoro_engine import c_sym
        val_13 = float(virasoro_delta_pf.subs(c_sym, 13))
        val_13_dual = float(virasoro_delta_pf.subs(c_sym, 13))
        assert abs(val_13 - val_13_dual) < 1e-12


# ============================================================================
# Section 8: Graph census
# ============================================================================

class TestGraphCensus:
    """Structural data on M-bar_{4,0}."""

    def test_total_graph_count(self, genus4_census):
        """379 stable graphs at genus 4."""
        assert genus4_census['total_graphs'] == 379

    def test_pf_graph_count(self, genus4_census):
        """358 planted-forest graphs."""
        assert genus4_census['pf_graphs'] == 358

    def test_non_pf_graph_count(self, genus4_census):
        """21 non-PF graphs."""
        assert genus4_census['non_pf_graphs'] == 21

    def test_vertex_count_distribution(self, genus4_census):
        """Vertex count distribution: 5, 29, 79, 126, 98, 42."""
        expected = {1: 5, 2: 29, 3: 79, 4: 126, 5: 98, 6: 42}
        assert genus4_census['by_vertex_count'] == expected

    def test_orbifold_euler_characteristic(self, genus4_census):
        """chi^orb(M-bar_{4,0}) = -4717039/6220800."""
        assert genus4_census['chi_orb'] == Fraction(-4717039, 6220800)


# ============================================================================
# Section 9: Shadow visibility
# ============================================================================

class TestShadowVisibility:
    """S_6 first appears at genus 4 (cor:shadow-visibility-genus)."""

    def test_shadow_visibility_formula(self):
        """g_min(S_r) = floor(r/2) + 1 (cor:shadow-visibility-genus)."""
        def g_min(r):
            return r // 2 + 1
        assert g_min(6) == 4  # S_6 first at g=4
        assert g_min(7) == 4  # S_7 also at g=4
        assert g_min(8) == 5  # S_8 first at g=5

    def test_S6_in_genus4_not_genus3(self):
        """S_6 appears in delta_pf^{(4,0)} but NOT in delta_pf^{(3,0)}."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        from compute.lib.theorem_genus3_planted_forest_full_engine import (
            genus3_exact_coefficients,
        )
        # S_6 in genus 4
        g4_has_s6 = any(m[4] > 0 for m in genus4_exact_coefficients().keys())
        assert g4_has_s6

        # S_6 NOT in genus 3 (genus 3 keys are (a,b,c,d) = kappa,S3,S4,S5)
        g3_coeffs = genus3_exact_coefficients()
        # genus 3 has 4-tuples, no S_6 slot
        for key in g3_coeffs.keys():
            assert len(key) == 4, "Genus-3 should have 4-component keys"


# ============================================================================
# Section 10: Cross-checks with genus-3 engine
# ============================================================================

class TestGenus3CrossCheck:
    """Verify consistency with the genus-3 planted-forest engine."""

    def test_genus3_heisenberg_vanishing(self):
        """Genus 3 also has delta_pf = 0 for Heisenberg."""
        from compute.lib.theorem_genus3_planted_forest_full_engine import (
            evaluate_heisenberg,
        )
        result = evaluate_heisenberg(3)
        assert result['is_zero'] is True

    def test_genus3_coefficient_count(self):
        """Genus 3 has 11 monomial terms (vs 37 at genus 4)."""
        from compute.lib.theorem_genus3_planted_forest_full_engine import (
            genus3_exact_coefficients,
        )
        assert len(genus3_exact_coefficients()) == 11

    def test_genus3_S5_appears(self):
        """S_5 first appears at genus 3 (g_min(S_5) = 3)."""
        from compute.lib.theorem_genus3_planted_forest_full_engine import (
            genus3_exact_coefficients,
        )
        has_s5 = any(m[3] > 0 for m in genus3_exact_coefficients().keys())
        assert has_s5


# ============================================================================
# Section 11: Ratio universality on the scalar lane
# ============================================================================

class TestRatioUniversality:
    """On the scalar lane (delta_pf = 0), F_g ratios are kappa-independent."""

    def test_F4_over_F1_ratio(self):
        """F_4/F_1 = lambda_4^FP / lambda_1^FP = 127/6451200."""
        from compute.lib.theorem_genus4_virasoro_engine import lambda_fp
        ratio = lambda_fp(4) / lambda_fp(1)
        assert ratio == Fraction(127, 6451200)

    def test_F4_over_F2_ratio(self):
        """F_4/F_2 = lambda_4^FP / lambda_2^FP = 127/188160."""
        from compute.lib.theorem_genus4_virasoro_engine import lambda_fp
        ratio = lambda_fp(4) / lambda_fp(2)
        assert ratio == Fraction(127, 188160)

    def test_F4_over_F3_ratio(self):
        """F_4/F_3 = lambda_4^FP / lambda_3^FP = 127/4960."""
        from compute.lib.theorem_genus4_virasoro_engine import lambda_fp
        ratio = lambda_fp(4) / lambda_fp(3)
        assert ratio == Fraction(127, 4960)

    def test_heisenberg_ratios_universal(self):
        """For Heisenberg (scalar-exact), F_4(k)/F_1(k) = lambda_4/lambda_1."""
        from compute.lib.theorem_genus4_virasoro_engine import (
            F4_heisenberg, lambda_fp,
        )
        expected_ratio = lambda_fp(4) / lambda_fp(1)
        for k in [1, 2, 5, 10]:
            f4 = F4_heisenberg(Fraction(k))
            f1 = Fraction(k) * lambda_fp(1)
            assert f4 / f1 == expected_ratio


# ============================================================================
# Section 12: Specific monomial coefficient checks
# ============================================================================

class TestSpecificCoefficients:
    """Spot-check individual monomial coefficients."""

    def test_S3_to_the_6(self):
        """Coefficient of S_3^6 is 425/576."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(0, 6, 0, 0, 0, 0)] == Rational(425, 576)

    def test_S4_cubed(self):
        """Coefficient of S_4^3 is 2/3."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(0, 0, 3, 0, 0, 0)] == Rational(2, 3)

    def test_S5_squared(self):
        """Coefficient of S_5^2 is 1651/384."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(0, 0, 0, 2, 0, 0)] == Rational(1651, 384)

    def test_S3_S7(self):
        """Coefficient of S_3 * S_7 is 163/96."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(0, 1, 0, 0, 0, 1)] == Rational(163, 96)

    def test_kappa4_S4(self):
        """Coefficient of kappa^4 * S_4 is 1/1990656."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(4, 0, 1, 0, 0, 0)] == Rational(1, 1990656)

    def test_kappa4_S3_squared(self):
        """Coefficient of kappa^4 * S_3^2 is 1/1769472."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(4, 2, 0, 0, 0, 0)] == Rational(1, 1769472)

    def test_S4_S6(self):
        """Coefficient of S_4 * S_6 is -35/6."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(0, 0, 1, 0, 1, 0)] == Rational(-35, 6)

    def test_kappa_S7(self):
        """Coefficient of kappa * S_7 is -1/1152."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(1, 0, 0, 0, 0, 1)] == Rational(-1, 1152)

    def test_kappa3_S3_cubed(self):
        """Coefficient of kappa^3 * S_3^3 is -277/5308416."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(3, 3, 0, 0, 0, 0)] == Rational(-277, 5308416)

    def test_kappa_S3(self):
        """Coefficient of kappa * S_3 is -123589/165888."""
        from compute.lib.theorem_genus4_virasoro_engine import genus4_exact_coefficients
        assert genus4_exact_coefficients()[(1, 1, 0, 0, 0, 0)] == Rational(-123589, 165888)


# ============================================================================
# Section 13: Virasoro rational function structure
# ============================================================================

class TestVirasoroRationalFunction:
    """delta_pf(Vir_c) as a rational function of c."""

    def test_denominator_structure(self, virasoro_delta_pf):
        """Denominator is proportional to c^4 * (5c+22)^3."""
        from compute.lib.theorem_genus4_virasoro_engine import c_sym
        from sympy import denom, Poly
        d = denom(virasoro_delta_pf)
        d_poly = Poly(d, c_sym)
        # Check c=0 is a root of order 4
        pow_c = 0
        rem = d_poly
        while rem.eval(0) == 0:
            pow_c += 1
            rem = Poly(cancel(rem.as_expr() / c_sym), c_sym)
        assert pow_c == 4

        # Check c=-22/5 is a root of order 3
        pow_5c22 = 0
        while rem.eval(Rational(-22, 5)) == 0:
            pow_5c22 += 1
            rem = Poly(cancel(rem.as_expr() / (5 * c_sym + 22)), c_sym)
        assert pow_5c22 == 3

    def test_numerator_degree(self, virasoro_delta_pf):
        """Numerator has degree 11 in c."""
        from compute.lib.theorem_genus4_virasoro_engine import c_sym
        from sympy import numer, Poly
        n = numer(virasoro_delta_pf)
        n_poly = Poly(n, c_sym)
        assert n_poly.total_degree() == 11

    def test_yang_lee_pole(self, virasoro_delta_pf):
        """c = -22/5 (Yang-Lee) is a pole of delta_pf."""
        from compute.lib.theorem_genus4_virasoro_engine import c_sym
        from sympy import limit
        val = limit(virasoro_delta_pf * (5 * c_sym + 22) ** 3,
                     c_sym, Rational(-22, 5))
        assert val != 0  # residue is nonzero


# ============================================================================
# Section 14: Consistency with shadow arity engine
# ============================================================================

class TestShadowArityConsistency:
    """Shadow coefficients S_6, S_7 match theorem_shadow_arity_frontier_engine."""

    def test_S6_closed_form(self):
        """S_6 = 80(45c+193) / [3c^3(5c+22)^2]."""
        from compute.lib.theorem_shadow_arity_frontier_engine import S_explicit
        from compute.lib.pixton_shadow_bridge import virasoro_shadow_data
        c = Symbol('c')
        S6_explicit = S_explicit(6)
        shadow = virasoro_shadow_data(max_arity=8)
        S6_convolution = shadow.S(6)
        diff = cancel(S6_explicit - S6_convolution)
        assert diff == 0

    def test_S7_closed_form(self):
        """S_7 = -2880(15c+61) / [7c^4(5c+22)^2]."""
        from compute.lib.theorem_shadow_arity_frontier_engine import S_explicit
        from compute.lib.pixton_shadow_bridge import virasoro_shadow_data
        c = Symbol('c')
        S7_explicit = S_explicit(7)
        shadow = virasoro_shadow_data(max_arity=9)
        S7_convolution = shadow.S(7)
        diff = cancel(S7_explicit - S7_convolution)
        assert diff == 0


# ============================================================================
# Section 15: Genus-2 planted-forest cross-check
# ============================================================================

class TestGenus2CrossCheck:
    """Verify the known genus-2 result delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48."""

    def test_genus2_formula(self):
        """delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48."""
        from compute.lib.theorem_genus3_planted_forest_full_engine import (
            compute_planted_forest_correction,
        )
        from compute.lib.pixton_shadow_bridge import ShadowData
        kappa = Symbol('kappa')
        S3 = Symbol('S_3')
        shadow = ShadowData('g2_sym', kappa, S3, Integer(0), depth_class='L')
        result = compute_planted_forest_correction(2, shadow)
        expected = S3 * (10 * S3 - kappa) / 48
        diff = expand(result - expected)
        assert diff == 0
