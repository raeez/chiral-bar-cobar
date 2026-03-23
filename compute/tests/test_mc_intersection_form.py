"""
Tests for the MC intersection form module.

Verifies:
  1. Witten-Kontsevich intersection numbers (genus 0, 1, 2)
  2. Genus-0 multinomial formula
  3. String equation recursion
  4. Dilaton equation recursion
  5. MC bracket bilinear form on 1d primary line
  6. Intersection form on tautological ring
  7. MC bracket vs WK comparison (the main conjecture test)
  8. Symmetric power / L-function data
  9. Rankin bound from moments
  10. Fake spectral test
  11. Genus-1 bracket vs WK
  12. Virasoro shadow coefficients

Ground truth:
  - Witten (1991), Kontsevich (1992) for WK numbers
  - Faber-Pandharipande for genus-2 values
  - nonlinear_modular_shadows.tex for shadow tower data
  - virasoro_shadow_tower.py for H-Poisson bracket
"""

import pytest
from fractions import Fraction
from math import factorial

from sympy import Rational, Symbol, simplify, factor

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from mc_intersection_form import (
    witten_kontsevich_intersection,
    wk_table,
    kappa_intersection_from_psi,
    mc_bracket_bilinear_form,
    mc_bracket_genus1_correction,
    intersection_form_tautological,
    verify_bracket_equals_intersection,
    symmetric_power_from_shadow,
    spectral_atoms_from_shadows,
    rankin_bound_from_moments,
    fake_spectral_test,
    virasoro_shadow_coeffs_symbolic,
    virasoro_shadow_coeffs_numerical,
    relationship_theorem_genus0,
    genus0_bracket_vs_wk_explicit,
    genus1_self_energy_from_wk,
    genus1_bracket_comparison,
    c, P_inv_hess,
)


# =========================================================================
# I. Witten-Kontsevich base cases
# =========================================================================

class TestWKBaseCases:
    """Verify the fundamental base cases."""

    def test_tau0_cubed_g0(self):
        """<tau_0^3>_0 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_tau1_g1(self):
        """<tau_1>_1 = 1/24."""
        assert witten_kontsevich_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau4_g2(self):
        """<tau_4>_2 = 1/1152 (seed value from Witten's table)."""
        assert witten_kontsevich_intersection(2, (4,)) == Fraction(1, 1152)

    def test_tau2_tau3_g2(self):
        """<tau_2 tau_3>_2 = 29/5760 (seed value)."""
        assert witten_kontsevich_intersection(2, (2, 3)) == Fraction(29, 5760)


class TestWKSelectionRule:
    """Verify the selection rule sum d_i = 3g-3+n."""

    def test_selection_rule_fail_g0(self):
        """Violating selection rule gives 0."""
        # g=0, n=3: need sum = 0. (0,0,1) has sum = 1.
        assert witten_kontsevich_intersection(0, (0, 0, 1)) == Fraction(0)

    def test_selection_rule_fail_g1(self):
        """g=1, n=1: need sum = 1. (0,) has sum = 0."""
        assert witten_kontsevich_intersection(1, (0,)) == Fraction(0)

    def test_selection_rule_fail_g1_n2(self):
        """g=1, n=2: need sum = 2. (0,0) has sum = 0."""
        assert witten_kontsevich_intersection(1, (0, 0)) == Fraction(0)

    def test_selection_rule_pass_g0_n4(self):
        """g=0, n=4: need sum = 1. (0,0,0,1) passes."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 1)) == Fraction(1)

    def test_selection_rule_pass_g1_n2(self):
        """g=1, n=2: need sum = 2. (0,2) passes."""
        assert witten_kontsevich_intersection(1, (0, 2)) == Fraction(1, 24)

    def test_unstable_g0_n2(self):
        """M-bar_{0,2} is unstable: 2*0-2+2 = 0."""
        assert witten_kontsevich_intersection(0, (0, 0)) == Fraction(0)

    def test_unstable_g0_n1(self):
        """M-bar_{0,1} is unstable: 2*0-2+1 = -1."""
        assert witten_kontsevich_intersection(0, (0,)) == Fraction(0)

    def test_negative_d(self):
        """Negative d values give 0."""
        assert witten_kontsevich_intersection(0, (-1, 0, 0)) == Fraction(0)


# =========================================================================
# II. Genus-0 multinomial formula
# =========================================================================

class TestGenus0Multinomial:
    """
    At genus 0: <tau_{d_1}...tau_{d_n}>_0 = (n-3)!/prod(d_i!).
    Selection rule: sum d_i = n-3.
    """

    def test_3pt(self):
        """<tau_0^3>_0 = 0!/1 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_4pt_single_psi(self):
        """<tau_0^3 tau_1>_0 = 1!/1 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 1)) == Fraction(1)

    def test_5pt_one_psi2(self):
        """<tau_0^4 tau_2>_0 = 2!/2 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 0, 2)) == Fraction(1)

    def test_5pt_two_psi1(self):
        """<tau_0^3 tau_1^2>_0 = 2!/(1!*1!) = 2."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 1, 1)) == Fraction(2)

    def test_6pt_one_psi3(self):
        """<tau_0^5 tau_3>_0 = 3!/6 = 1."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 0, 0, 3)) == Fraction(1)

    def test_6pt_psi1_psi2(self):
        """<tau_0^4 tau_1 tau_2>_0 = 3!/(1!*2!) = 3."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 0, 1, 2)) == Fraction(3)

    def test_6pt_three_psi1(self):
        """<tau_0^3 tau_1^3>_0 = 3!/(1!*1!*1!) = 6."""
        assert witten_kontsevich_intersection(0, (0, 0, 0, 1, 1, 1)) == Fraction(6)

    @pytest.mark.parametrize("d_tuple,expected", [
        ((0, 0, 0), 1),
        ((0, 0, 0, 1), 1),
        ((0, 0, 0, 0, 2), 1),
        ((0, 0, 0, 1, 1), 2),
        ((0, 0, 0, 0, 0, 3), 1),
        ((0, 0, 0, 0, 1, 2), 3),
        ((0, 0, 0, 1, 1, 1), 6),
    ])
    def test_genus0_formula(self, d_tuple, expected):
        """Verify against closed-form multinomial."""
        n = len(d_tuple)
        dim = n - 3
        formula = factorial(dim)
        for d in d_tuple:
            formula //= factorial(d)
        assert witten_kontsevich_intersection(0, d_tuple) == Fraction(formula)
        assert formula == expected


# =========================================================================
# III. String equation tests
# =========================================================================

class TestStringEquation:
    """
    String equation: <tau_0 tau_{d_1}...tau_{d_n}>_g = sum_j <...tau_{d_j-1}...>_g.
    """

    def test_string_g0_4pt(self):
        """<tau_0 tau_0^2 tau_1>_0 = <tau_0^3>_0 = 1 (reduce tau_1)."""
        # <tau_0^3 tau_1>_0 = 1 (multinomial)
        # Equivalently: string eq on <tau_0 * (tau_0^2 tau_1)>:
        # = <tau_0^2 tau_0>_0 (reduce tau_1 -> tau_0) = <tau_0^3>_0 = 1
        assert witten_kontsevich_intersection(0, (0, 0, 0, 1)) == Fraction(1)

    def test_string_g1_2pt(self):
        """<tau_0 tau_2>_1 = <tau_1>_1 = 1/24."""
        val = witten_kontsevich_intersection(1, (0, 2))
        assert val == Fraction(1, 24)

    def test_string_g2_2pt(self):
        """<tau_0 tau_5>_2 = <tau_4>_2 = 1/1152."""
        val = witten_kontsevich_intersection(2, (0, 5))
        assert val == Fraction(1, 1152)

    def test_string_g2_3pt(self):
        """<tau_0 tau_2 tau_4>_2 = <tau_1 tau_4>_2 + <tau_2 tau_3>_2."""
        lhs = witten_kontsevich_intersection(2, (0, 2, 4))
        rhs = (witten_kontsevich_intersection(2, (1, 4))
               + witten_kontsevich_intersection(2, (2, 3)))
        assert lhs == rhs

    def test_string_iterative_g0(self):
        """Two string equation steps."""
        # <tau_0^2 tau_0 tau_2>_0 at n=4, g=0: sum=2, need 1. FAIL.
        # Actually: (0,0,0,2) at g=0, n=4: sum=2, need 1. Fails.
        assert witten_kontsevich_intersection(0, (0, 0, 0, 2)) == Fraction(0)
        # But at n=5: (0,0,0,0,2) sum=2, need 2. OK.
        assert witten_kontsevich_intersection(0, (0, 0, 0, 0, 2)) == Fraction(1)


# =========================================================================
# IV. Dilaton equation tests
# =========================================================================

class TestDilatonEquation:
    """
    Dilaton equation: <tau_1 tau_{d_1}...tau_{d_n}>_g = (2g-2+n+1)<tau_{d_1}...tau_{d_n}>_g.
    (The n+1 counts the tau_1 itself.)
    """

    def test_dilaton_g1_2pt(self):
        """<tau_1 tau_1>_1 = (2*1-2+2)*<tau_1>_1 = 2 * 1/24 = 1/12."""
        val = witten_kontsevich_intersection(1, (1, 1))
        assert val == Fraction(1, 12)

    def test_dilaton_g1_3pt(self):
        """<tau_1^3>_1 = (2*1-2+3)*<tau_1^2>_1 = 3 * 1/12 = 1/4."""
        val = witten_kontsevich_intersection(1, (1, 1, 1))
        assert val == Fraction(1, 4)

    def test_dilaton_g2_2pt(self):
        """<tau_1 tau_4>_2 = (2*2-2+2)*<tau_4>_2 = 4/1152 = 1/288."""
        val = witten_kontsevich_intersection(2, (1, 4))
        assert val == Fraction(1, 288)

    def test_dilaton_g2_chain(self):
        """<tau_1^2 tau_3>_2: dilaton gives (2+2+1)*<tau_1 tau_3>_2 = 5*<tau_1 tau_3>_2.
        But <tau_1 tau_3>_2: dilaton gives 4*<tau_3>_2. And <tau_3>_2=0 (sel rule).
        So <tau_1^2 tau_3>_2 uses string first."""
        # g=2, n=3: sum must be 6. 1+1+3=5 != 6. FAIL.
        assert witten_kontsevich_intersection(2, (1, 1, 3)) == Fraction(0)


# =========================================================================
# V. Genus-1 comprehensive
# =========================================================================

class TestGenus1:
    """Comprehensive genus-1 intersection number tests."""

    def test_tau1_fundamental(self):
        assert witten_kontsevich_intersection(1, (1,)) == Fraction(1, 24)

    def test_tau0_tau2_string(self):
        """String: <tau_0 tau_2>_1 = <tau_1>_1 = 1/24."""
        assert witten_kontsevich_intersection(1, (0, 2)) == Fraction(1, 24)

    def test_tau1_squared_dilaton(self):
        """Dilaton: <tau_1^2>_1 = 2*<tau_1>_1 = 1/12."""
        assert witten_kontsevich_intersection(1, (1, 1)) == Fraction(1, 12)

    def test_tau0_tau1_tau2(self):
        """String from 3pt: <tau_0 tau_1 tau_2>_1 = <tau_0 tau_2>_1 + <tau_1^2>_1
        = 1/24 + 1/12 = 1/8."""
        val = witten_kontsevich_intersection(1, (0, 1, 2))
        assert val == Fraction(1, 8)

    def test_tau1_cubed_dilaton(self):
        """Dilaton: <tau_1^3>_1 = 3*<tau_1^2>_1 = 3/12 = 1/4."""
        assert witten_kontsevich_intersection(1, (1, 1, 1)) == Fraction(1, 4)

    def test_tau0_squared_tau3(self):
        """String twice: <tau_0^2 tau_3>_1 = <tau_0 tau_2>_1 = 1/24."""
        assert witten_kontsevich_intersection(1, (0, 0, 3)) == Fraction(1, 24)

    def test_genus1_consistency(self):
        """Cross-check: string and dilaton give consistent results."""
        # <tau_0 tau_1 tau_2>_1 via string from <tau_0^2 tau_1 tau_2>:
        # No, that has wrong selection rule. Let me do a different check.
        # <tau_0 tau_1 tau_2>_1: g=1, n=3, sum=3=3. OK.
        # Via string: = <tau_0 tau_2>_1 + <tau_1^2>_1 = 1/24 + 1/12 = 1/8.
        # Via dilaton from <tau_1 tau_1 tau_2>_1... wait, need to check sel rule.
        # g=1, n=3, sum=1+1+2=4, need 3. FAIL.
        assert witten_kontsevich_intersection(1, (1, 1, 2)) == Fraction(0)


# =========================================================================
# VI. Genus-2 tests
# =========================================================================

class TestGenus2:
    """Genus-2 intersection numbers, verified against Witten/Faber tables."""

    def test_tau4_seed(self):
        """<tau_4>_2 = 1/1152 (Witten's table)."""
        assert witten_kontsevich_intersection(2, (4,)) == Fraction(1, 1152)

    def test_tau2_tau3_seed(self):
        """<tau_2 tau_3>_2 = 29/5760 (Witten's table)."""
        assert witten_kontsevich_intersection(2, (2, 3)) == Fraction(29, 5760)

    def test_tau0_tau5_string(self):
        """<tau_0 tau_5>_2 = <tau_4>_2 = 1/1152."""
        assert witten_kontsevich_intersection(2, (0, 5)) == Fraction(1, 1152)

    def test_tau1_tau4_dilaton(self):
        """<tau_1 tau_4>_2 = 4*<tau_4>_2 = 4/1152 = 1/288."""
        val = witten_kontsevich_intersection(2, (1, 4))
        assert val == Fraction(1, 288)
        assert val == Fraction(4) * Fraction(1, 1152)

    def test_tau0_tau2_tau4(self):
        """<tau_0 tau_2 tau_4>_2 = <tau_1 tau_4>_2 + <tau_2 tau_3>_2."""
        val = witten_kontsevich_intersection(2, (0, 2, 4))
        expected = Fraction(1, 288) + Fraction(29, 5760)
        assert val == expected

    def test_tau0_tau3_tau3(self):
        """<tau_0 tau_3^2>_2 = 2*<tau_2 tau_3>_2 = 29/2880."""
        val = witten_kontsevich_intersection(2, (0, 3, 3))
        assert val == 2 * Fraction(29, 5760)

    def test_tau0_squared_tau6(self):
        """<tau_0^2 tau_6>_2 = <tau_0 tau_5>_2 = 1/1152."""
        assert witten_kontsevich_intersection(2, (0, 0, 6)) == Fraction(1, 1152)

    def test_tau0_tau1_tau5(self):
        """<tau_0 tau_1 tau_5>_2 = <tau_0 tau_5>_2 + <tau_1 tau_4>_2."""
        # String on first tau_0: reduces tau_1->tau_0 and tau_5->tau_4.
        # <tau_0 tau_1 tau_5>_2 = <tau_0 tau_5>_2 (from reducing tau_1)
        #                       + <tau_1 tau_4>_2 (from reducing tau_5)
        val = witten_kontsevich_intersection(2, (0, 1, 5))
        expected = Fraction(1, 1152) + Fraction(1, 288)
        assert val == expected

    def test_dilaton_consistency_g2(self):
        """<tau_1^2 tau_3>_2 = 0 since sum=5 != 6 for g=2,n=3."""
        assert witten_kontsevich_intersection(2, (1, 1, 3)) == Fraction(0)


# =========================================================================
# VII. Kappa class intersection
# =========================================================================

class TestKappaIntersection:
    """Test kappa-class intersection numbers."""

    def test_kappa1_g2(self):
        """<kappa_1>_2 = <tau_2>_{2,1}. But sel rule: sum=2, need 4. = 0?
        Actually: <kappa_1>_g = <tau_2>_{g,1}. g=2, n=1: need sum=4. = 0.
        But kappa_1 on M-bar_{2,0}: dim = 3. <kappa_1> means int kappa_1 over M-bar_2.
        dim M-bar_2 = 3. kappa_1 has degree 1, so we need degree 3. Missing."""
        # Single kappa: <kappa_j>_g = <tau_{j+1}>_{g,1}
        # j=1: <tau_2>_{2,1}. sum=2, need 3*2-3+1=4. Fails.
        assert kappa_intersection_from_psi(2, [1]) == Fraction(0)

    def test_kappa3_g2(self):
        """<kappa_3>_2 = <tau_4>_{2,1} = 1/1152."""
        assert kappa_intersection_from_psi(2, [3]) == Fraction(1, 1152)

    def test_kappa1_g1(self):
        """<kappa_1>_1: on M-bar_{1,0}, dim=1. j=1, need sum j = 0. Fails."""
        assert kappa_intersection_from_psi(1, [1]) == Fraction(0)

    def test_kappa0_g1(self):
        """<kappa_0>_1 = <tau_1>_{1,1} = 1/24."""
        assert kappa_intersection_from_psi(1, [0]) == Fraction(1, 24)


# =========================================================================
# VIII. WK table generation
# =========================================================================

class TestWKTable:
    """Test the table generation function."""

    def test_genus0_table_entries(self):
        table = wk_table(0, 5)
        assert len(table) >= 3  # At least (0,0,0), (0,0,0,1), (0,0,0,0,2)
        assert table[(0, 0, 0)] == Fraction(1)
        assert table[(0, 0, 0, 1)] == Fraction(1)

    def test_genus1_table(self):
        table = wk_table(1, 3)
        assert (1,) in table
        assert table[(1,)] == Fraction(1, 24)

    def test_genus0_n6(self):
        table = wk_table(0, 6)
        assert (0, 0, 0, 1, 1, 1) in table
        assert table[(0, 0, 0, 1, 1, 1)] == Fraction(6)


# =========================================================================
# IX. MC bracket bilinear form
# =========================================================================

class TestMCBracket:
    """Test the MC bracket computation on the 1d primary line."""

    def test_bracket_22_virasoro(self):
        """[Sh_2, Sh_2] = 4*P*S_2^2 = 4*(2/c)*(c/2)^2 = 2c."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 2, 2)
        assert simplify(bracket - 2 * c) == 0

    def test_bracket_23_virasoro(self):
        """[Sh_2, Sh_3] = 2*3*P*S_2*S_3 = 6*(2/c)*(c/2)*2 = 12."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 2, 3)
        assert simplify(bracket - 12) == 0

    def test_bracket_33_virasoro(self):
        """[Sh_3, Sh_3] = 9*P*S_3^2 = 9*(2/c)*4 = 72/c."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 3, 3)
        assert simplify(bracket - Rational(72) / c) == 0

    def test_bracket_24_virasoro(self):
        """[Sh_2, Sh_4] = 8*P*S_2*S_4 = 8*(2/c)*(c/2)*Q0."""
        S = virasoro_shadow_coeffs_symbolic(4)
        Q0 = Rational(10) / (c * (5 * c + 22))
        expected = 8 * (Rational(2) / c) * (c / 2) * Q0
        bracket = mc_bracket_bilinear_form(S, 2, 4)
        assert simplify(bracket - expected) == 0

    def test_bracket_symmetry(self):
        """[Sh_r, Sh_s] = [Sh_s, Sh_r] (up to x-reindexing)."""
        S = virasoro_shadow_coeffs_symbolic(4)
        assert simplify(
            mc_bracket_bilinear_form(S, 2, 3)
            - mc_bracket_bilinear_form(S, 3, 2)
        ) == 0

    def test_bracket_zero_missing(self):
        """Bracket with missing shadow gives 0."""
        S = {2: c / 2}  # Only kappa
        bracket = mc_bracket_bilinear_form(S, 2, 5)
        assert bracket == 0

    def test_bracket_heisenberg(self):
        """Heisenberg: S_r = 0 for r >= 3, so [Sh_r, Sh_s] = 0 for r+s >= 5."""
        S_heis = {2: Rational(1)}  # kappa = 1 (rank 1 Heisenberg)
        assert mc_bracket_bilinear_form(S_heis, 2, 3) == 0
        assert mc_bracket_bilinear_form(S_heis, 3, 3) == 0


# =========================================================================
# X. MC bracket genus-1 correction
# =========================================================================

class TestMCBracketGenus1:
    """Test the genus-1 MC bracket correction."""

    def test_g1_bracket_22(self):
        """[Sh_2, Sh_2]^{(1)} = S_2 * 1/24 = c/48 for Virasoro."""
        S = virasoro_shadow_coeffs_symbolic(4)
        val = mc_bracket_genus1_correction(S, 2, 2)
        assert simplify(val - c / 48) == 0

    def test_g1_bracket_23_zero(self):
        """[Sh_2, Sh_3]^{(1)} = 0 (no self-loop at these arities)."""
        S = virasoro_shadow_coeffs_symbolic(4)
        val = mc_bracket_genus1_correction(S, 2, 3)
        assert val == 0

    def test_g1_bracket_involves_tau1_g1(self):
        """The genus-1 self-energy involves <tau_1>_1 = 1/24."""
        assert genus1_self_energy_from_wk() == Fraction(1, 24)


# =========================================================================
# XI. Intersection form on tautological ring
# =========================================================================

class TestIntersectionForm:
    """Test the intersection pairing on R*(M-bar_{g,n})."""

    def test_g0_3pt_trivial(self):
        """On M-bar_{0,3} (point): <1, 1> = 1."""
        val = intersection_form_tautological(0, 3, (0, 0, 0), (0, 0, 0))
        assert val == Fraction(1)

    def test_g0_4pt(self):
        """On M-bar_{0,4} (dim 1): <psi_1, 1> requires sum = 1."""
        # class_r = (1,0,0,0), class_s = (0,0,0,0): sum = (1,0,0,0), total sum = 1. OK.
        val = intersection_form_tautological(0, 4, (1, 0, 0, 0), (0, 0, 0, 0))
        assert val == witten_kontsevich_intersection(0, (0, 0, 0, 1))

    def test_g1_2pt(self):
        """On M-bar_{1,2} (dim 2): pairing of psi-classes."""
        # class_r = (1,0), class_s = (0,1): sum = (1,1), total 2.
        # Need 3*1-3+2 = 2. OK.
        val = intersection_form_tautological(1, 2, (1, 0), (0, 1))
        assert val == witten_kontsevich_intersection(1, (1, 1))
        assert val == Fraction(1, 12)

    def test_selection_rule_violation(self):
        """Wrong total degree gives 0."""
        val = intersection_form_tautological(0, 3, (1, 0, 0), (0, 0, 0))
        assert val == Fraction(0)


# =========================================================================
# XII. MC bracket vs WK (the main comparison)
# =========================================================================

class TestBracketVsIntersection:
    """
    The central test: does the MC bracket equal the intersection form?

    HONEST FINDING: They are NOT equal. The MC bracket [Sh_r, Sh_s] at
    tree level is a Feynman graph composition through a single propagator.
    The WK intersection numbers are topological integrals over M-bar.
    They are RELATED but distinct objects.
    """

    def test_bracket_not_equal_to_wk_23(self):
        """MC bracket [Sh_2, Sh_3] = 12, while <tau_0^3>_0 = 1.
        These are NOT equal."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 2, 3)
        wk_val = witten_kontsevich_intersection(0, (0, 0, 0))
        assert simplify(bracket - 12) == 0
        assert wk_val == Fraction(1)
        # NOT equal: 12 != 1

    def test_bracket_not_equal_to_wk_33(self):
        """MC bracket [Sh_3, Sh_3] = 72/c, WK <tau_0^3 tau_1>_0 = 1.
        NOT equal (ratio = 72/c)."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 3, 3)
        wk_val = witten_kontsevich_intersection(0, (0, 0, 0, 1))
        ratio = simplify(bracket / Rational(wk_val.numerator, wk_val.denominator))
        assert simplify(ratio - Rational(72) / c) == 0

    def test_bracket_carries_algebra_data(self):
        """The MC bracket depends on S_r (algebra data), while WK does not."""
        # Different algebras give different brackets
        S_vir = {2: c / 2, 3: Rational(2)}
        S_heis = {2: c / 2, 3: Rational(0)}
        b_vir = mc_bracket_bilinear_form(S_vir, 2, 3)
        b_heis = mc_bracket_bilinear_form(S_heis, 2, 3)
        assert simplify(b_vir - 12) == 0
        assert b_heis == 0

    def test_relationship_theorem_structure(self):
        """The relationship theorem documents the correct connection."""
        rel = relationship_theorem_genus0()
        assert 'not equal' in rel['relationship'].lower() or 'not' in rel['relationship'].lower()

    def test_genus0_comparison_table(self):
        """Verify the explicit genus-0 comparison table."""
        comp = genus0_bracket_vs_wk_explicit()
        assert '(2,2)' in comp
        assert '(2,3)' in comp
        assert '(3,3)' in comp

    def test_verify_function_runs(self):
        """The verify_bracket_equals_intersection function runs without error."""
        S = virasoro_shadow_coeffs_symbolic(4)
        results = verify_bracket_equals_intersection(S, 0, 5)
        assert len(results) > 0

    def test_wk_as_coefficient_not_value(self):
        """WK numbers enter as COEFFICIENTS in the genus expansion,
        not as values of the MC bracket.

        The genus-1 correction to [Sh_2,Sh_2] is:
          [Sh_2, Sh_2]^{(1)} = S_2 * <tau_1>_1 = (c/2) * (1/24) = c/48

        So 1/24 appears as a MULTIPLICATIVE FACTOR, not as the value
        of the bracket. The bracket value is c/48 (depends on c).
        """
        S = virasoro_shadow_coeffs_symbolic(4)
        g1_bracket = mc_bracket_genus1_correction(S, 2, 2)
        tau1 = Fraction(1, 24)
        # The bracket = S_2 * tau1 = (c/2) * (1/24) = c/48
        assert simplify(g1_bracket - c / 48) == 0
        # The WK number 1/24 is a coefficient, the bracket value is c/48
        assert simplify(g1_bracket - Rational(tau1.numerator, tau1.denominator)) != 0


# =========================================================================
# XIII. Genus-1 bracket comparison
# =========================================================================

class TestGenus1BracketComparison:
    """Test the genus-1 bracket vs WK comparison."""

    def test_genus1_comparison_runs(self):
        comp = genus1_bracket_comparison()
        assert 'wk_numbers' in comp
        assert 'mc_bracket_g1_22' in comp

    def test_genus1_wk_numbers_correct(self):
        comp = genus1_bracket_comparison()
        wk = comp['wk_numbers']
        assert wk['<tau_1>_1'] == Fraction(1, 24)
        assert wk['<tau_1^2>_1'] == Fraction(1, 12)
        assert wk['<tau_0 tau_2>_1'] == Fraction(1, 24)
        assert wk['<tau_0 tau_1 tau_2>_1'] == Fraction(1, 8)
        assert wk['<tau_1^3>_1'] == Fraction(1, 4)

    def test_genus1_mc_bracket_value(self):
        comp = genus1_bracket_comparison()
        mc_val = comp['mc_bracket_g1_22']
        assert simplify(mc_val - c / 48) == 0


# =========================================================================
# XIV. Symmetric power / L-function
# =========================================================================

class TestSymmetricPower:
    """Test the symmetric power extraction."""

    def test_power_sum_extraction(self):
        """p_r = r * S_r."""
        S = {2: 0.5, 3: 0.1, 4: -0.05}
        assert symmetric_power_from_shadow(S, 2) == pytest.approx(1.0)
        assert symmetric_power_from_shadow(S, 3) == pytest.approx(0.3)
        assert symmetric_power_from_shadow(S, 4) == pytest.approx(-0.2)

    def test_missing_arity_zero(self):
        S = {2: 0.5}
        assert symmetric_power_from_shadow(S, 5) == 0.0

    def test_spectral_atoms_single_eigenvalue(self):
        """For a single eigenvalue lambda=0.5 with c=1:
        S_r = -(1/r) * 0.5^r.
        Power sum: p_r = -r*S_r = 0.5^r."""
        lam = 0.5
        S = {r: -(1.0/r) * lam**r for r in range(2, 8)}
        atoms = spectral_atoms_from_shadows(S, 7)
        # Check power sums
        for r in range(2, 8):
            assert atoms['power_sums'][r] == pytest.approx(lam**r, rel=1e-10)

    def test_newton_identities(self):
        """Newton's identities recover elementary symmetric functions."""
        # Two eigenvalues: lambda_1 = 0.3, lambda_2 = 0.7
        lam1, lam2 = 0.3, 0.7
        S = {r: -(lam1**r + lam2**r)/r for r in range(1, 8)}
        atoms = spectral_atoms_from_shadows(S, 7)
        # e_1 = lam1 + lam2 = 1.0
        assert atoms['elementary_symmetric'][1] == pytest.approx(1.0, rel=1e-8)
        # e_2 = lam1 * lam2 = 0.21
        assert atoms['elementary_symmetric'][2] == pytest.approx(0.21, rel=1e-8)


# =========================================================================
# XV. Rankin bound from moments
# =========================================================================

class TestRankinBound:
    """Test the Rankin bound computation."""

    def test_single_eigenvalue_bound(self):
        """For a single eigenvalue lambda: bound -> |lambda|."""
        lam = 0.8
        S = {r: -(1.0/r) * lam**r for r in range(2, 20)}
        bounds = rankin_bound_from_moments(S, 19)
        # As r increases, (r*|S_r|)^{1/r} = |lambda| * r^{1/r} -> |lambda|
        assert bounds[-1] == pytest.approx(lam, rel=0.05)

    def test_convergence_to_largest(self):
        """With two eigenvalues, bound converges to the larger one."""
        lam1, lam2 = 0.3, 0.9
        S = {r: -(lam1**r + lam2**r)/r for r in range(2, 30)}
        bounds = rankin_bound_from_moments(S, 29)
        # Should converge to 0.9
        assert bounds[-1] == pytest.approx(lam2, rel=0.05)

    def test_zero_shadow_zero_bound(self):
        S = {r: 0.0 for r in range(2, 10)}
        bounds = rankin_bound_from_moments(S, 9)
        assert all(b == 0.0 for b in bounds)


# =========================================================================
# XVI. Fake spectral test
# =========================================================================

class TestFakeSpectral:
    """Test the fake spectral detection."""

    def test_real_bounded(self):
        """Real atoms with |lambda| <= 1 are bounded."""
        real = [(1.0, 0.5), (1.0, -0.3)]
        fake = [(1.0, 1.5), (1.0, -0.3)]
        result = fake_spectral_test(real, fake, r_max=15)
        assert result['real_bounded'] is True

    def test_fake_unbounded(self):
        """Fake atoms with |lambda| > 1 are eventually detected."""
        real = [(1.0, 0.5)]
        fake = [(1.0, 1.5)]
        result = fake_spectral_test(real, fake, r_max=15)
        assert result['fake_bounded'] is False
        assert result['first_divergence_arity'] is not None

    def test_fake_detection_arity(self):
        """Fake spectral measure detected at finite arity."""
        real = [(1.0, 0.9)]
        fake = [(1.0, 1.1)]
        result = fake_spectral_test(real, fake, r_max=20)
        # The fake measure grows like 1.1^r, so detection should be quick
        assert result['first_divergence_arity'] <= 10

    def test_marginal_case(self):
        """An eigenvalue exactly at |lambda|=1 is borderline."""
        borderline = [(1.0, 1.0)]
        result = fake_spectral_test(borderline, borderline, r_max=15)
        # |lambda|=1 means bounds stay at 1
        # (r * |S_r|)^{1/r} = (r * 1/r)^{1/r} = 1 for all r.
        # So it should be bounded.
        assert result['real_bounded'] is True

    def test_shadow_coefficient_computation(self):
        """Verify shadow coefficients for known spectral data."""
        atoms = [(2.0, 0.5)]
        result = fake_spectral_test(atoms, atoms, r_max=5)
        # S_r = -(1/r) * 2.0 * 0.5^r = -2 * 0.5^r / r
        for r in range(2, 6):
            expected = -2.0 * 0.5**r / r
            assert result['real_shadows'][r] == pytest.approx(expected)

    def test_empty_atoms(self):
        """Empty spectral data gives zero shadows."""
        result = fake_spectral_test([], [], r_max=5)
        for r in range(2, 6):
            assert result['real_shadows'][r] == 0.0


# =========================================================================
# XVII. Virasoro shadow coefficients
# =========================================================================

class TestVirasoroShadowCoeffs:
    """Test the Virasoro shadow coefficient interface."""

    def test_sh2_kappa(self):
        S = virasoro_shadow_coeffs_symbolic(4)
        assert simplify(S[2] - c / 2) == 0

    def test_sh3_cubic(self):
        S = virasoro_shadow_coeffs_symbolic(4)
        assert simplify(S[3] - 2) == 0

    def test_sh4_quartic(self):
        S = virasoro_shadow_coeffs_symbolic(4)
        Q0 = Rational(10) / (c * (5 * c + 22))
        assert simplify(S[4] - Q0) == 0

    def test_numerical_at_c1(self):
        S = virasoro_shadow_coeffs_numerical(1.0, 4)
        assert S[2] == pytest.approx(0.5)
        assert S[3] == pytest.approx(2.0)
        assert S[4] == pytest.approx(10.0 / 27.0)

    def test_numerical_at_c25(self):
        """c=25: kappa=25/2, cubic=2, Q0=10/(25*147) = 10/3675."""
        S = virasoro_shadow_coeffs_numerical(25.0, 4)
        assert S[2] == pytest.approx(12.5)
        assert S[3] == pytest.approx(2.0)
        assert S[4] == pytest.approx(10.0 / (25.0 * 147.0), rel=1e-8)


# =========================================================================
# XVIII. Specific computations from the specification
# =========================================================================

class TestSpecificComputations:
    """Verify the specific computations requested in the specification."""

    def test_genus0_3pt_fundamental(self):
        """<tau_0^3>_0 = 1 (the fundamental 3-point function)."""
        assert witten_kontsevich_intersection(0, (0, 0, 0)) == Fraction(1)

    def test_genus0_string_derived(self):
        """<tau_0 tau_1>_0 = 0 (n=2 is unstable for g=0)."""
        assert witten_kontsevich_intersection(0, (0, 1)) == Fraction(0)

    def test_genus0_psi_squared(self):
        """<tau_0^2 tau_2>_0: n=3, sum=2, need 0. Fails."""
        assert witten_kontsevich_intersection(0, (0, 0, 2)) == Fraction(0)

    def test_genus1_kappa_psi_relation(self):
        """In M-bar_{1,1}: kappa_1 = psi_1 - delta/12.
        <kappa_1>_1 = 1/24 = <psi_1>_1 (in M-bar_{1,1}).
        Note: kappa_1 = pi_*(psi^2) where pi forgets a point."""
        assert witten_kontsevich_intersection(1, (1,)) == Fraction(1, 24)

    def test_mc_bracket_22_genus0(self):
        """[Sh_2, Sh_2]_2 = {kappa, kappa}_H = 4*P*(c/2)^2 = 2c.
        (This is NOT equal to any WK number; M-bar_{0,2} is unstable.)"""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 2, 2)
        assert simplify(bracket - 2 * c) == 0

    def test_genus1_bracket_should_be_1_over_24_times_kappa(self):
        """[Sh_2, Sh_2]^{(1)} should equal kappa * <tau_1>_1 = c/48."""
        S = virasoro_shadow_coeffs_symbolic(4)
        val = mc_bracket_genus1_correction(S, 2, 2)
        assert simplify(val - c / 48) == 0

    def test_virasoro_c25_shadow_s2(self):
        """S_2 = c/2 = 12.5 at c=25."""
        S = virasoro_shadow_coeffs_numerical(25.0)
        assert S[2] == pytest.approx(12.5)

    def test_virasoro_c25_shadow_s3(self):
        """S_3 = 2 (c-independent cubic)."""
        S = virasoro_shadow_coeffs_numerical(25.0)
        assert S[3] == pytest.approx(2.0)


# =========================================================================
# XIX. Discrepancy analysis
# =========================================================================

class TestDiscrepancyAnalysis:
    """
    Careful analysis of WHY the MC bracket and intersection form differ.

    The MC bracket [Sh_r, Sh_s] at tree level = r*s*P*S_r*S_s.
    The WK number <tau_{d_1}...tau_{d_n}>_0 = (n-3)!/prod(d_i!).

    The RATIO between them is:
      [Sh_r, Sh_s] / <tau>_g = (algebra data) * (graph factor) / (WK)

    This ratio encodes the ALGEBRA CONTENT: how the shadow coefficients
    weight the universal WK numbers.
    """

    def test_ratio_23_is_12(self):
        """[Sh_2, Sh_3]_Vir / <tau_0^3>_0 = 12."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 2, 3)
        wk = Fraction(1)
        ratio = simplify(bracket / Rational(wk.numerator, wk.denominator))
        assert simplify(ratio - 12) == 0

    def test_ratio_33_is_72_over_c(self):
        """[Sh_3, Sh_3]_Vir / <tau_0^3 tau_1>_0 = 72/c."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket = mc_bracket_bilinear_form(S, 3, 3)
        wk = Fraction(1)  # <tau_0^3 tau_1>_0 = 1
        ratio = simplify(bracket / Rational(wk.numerator, wk.denominator))
        assert simplify(ratio - Rational(72) / c) == 0

    def test_ratio_depends_on_algebra(self):
        """Different algebras give different ratios."""
        S1 = {2: c / 2, 3: Rational(2)}   # Virasoro
        S2 = {2: c / 2, 3: Rational(3)}   # Hypothetical
        r1 = mc_bracket_bilinear_form(S1, 2, 3)
        r2 = mc_bracket_bilinear_form(S2, 2, 3)
        assert simplify(r1 - 12) == 0
        assert simplify(r2 - 18) == 0

    def test_genus1_ratio_involves_wk_as_factor(self):
        """At genus 1, the bracket involves WK as a MULTIPLICATIVE FACTOR:
        [Sh_2, Sh_2]^{(1)} = S_2 * <tau_1>_1 = S_2 / 24.
        The WK number 1/24 is a universal factor, not the value."""
        S = virasoro_shadow_coeffs_symbolic(4)
        bracket_g1 = mc_bracket_genus1_correction(S, 2, 2)
        # bracket_g1 = c/48 = (c/2) * (1/24)
        # Factored as: S_2 * <tau_1>_1
        s2 = S[2]
        tau1 = Rational(1, 24)
        assert simplify(bracket_g1 - s2 * tau1) == 0


# =========================================================================
# XX. Consistency checks and cross-verification
# =========================================================================

class TestConsistency:
    """Cross-checks and consistency tests."""

    def test_wk_positivity_g0(self):
        """All genus-0 WK numbers are positive."""
        table = wk_table(0, 6)
        for d, val in table.items():
            assert val > 0, f"<tau_{d}>_0 = {val} should be positive"

    def test_wk_positivity_g1(self):
        """All genus-1 WK numbers are positive."""
        table = wk_table(1, 4)
        for d, val in table.items():
            assert val > 0, f"<tau_{d}>_1 = {val} should be positive"

    def test_wk_string_dilaton_commute_g1(self):
        """String and dilaton should commute.
        <tau_0 tau_1 tau_2>_1 computed two ways:
        (a) String first: = <tau_0 tau_2>_1 + <tau_1^2>_1 = 1/24 + 1/12 = 1/8
        (b) Direct: 1/8."""
        val_a = (witten_kontsevich_intersection(1, (0, 2))
                 + witten_kontsevich_intersection(1, (1, 1)))
        val_b = witten_kontsevich_intersection(1, (0, 1, 2))
        assert val_a == val_b == Fraction(1, 8)

    def test_wk_dilaton_chain_g1(self):
        """Dilaton chain: <tau_1^n>_1 = n! / 24 * (n-1)!... let me check.
        <tau_1>_1 = 1/24.
        <tau_1^2>_1 = 2/24 = 1/12.
        <tau_1^3>_1 = 3*1/12 = 1/4.
        <tau_1^4>_1 = 4*1/4 = 1. (g=1, n=4, sum=4, need 4. OK.)"""
        vals = []
        for n in range(1, 5):
            d = tuple([1] * n)
            # Check selection rule: sum = n, need 3*1-3+n = n. OK.
            vals.append(witten_kontsevich_intersection(1, d))
        assert vals == [
            Fraction(1, 24),
            Fraction(1, 12),
            Fraction(1, 4),
            Fraction(1, 1),
        ]

    def test_g2_string_from_seed(self):
        """<tau_0 tau_2 tau_4>_2 derived from seeds + string."""
        # = <tau_1 tau_4>_2 + <tau_2 tau_3>_2
        # = 1/288 + 29/5760
        expected = Fraction(1, 288) + Fraction(29, 5760)
        val = witten_kontsevich_intersection(2, (0, 2, 4))
        assert val == expected

    def test_bracket_mc_equation_projection(self):
        """The MC equation [Theta, Theta] = 0 projected to arity r:
        sum_{j+k=r+2} [Sh_j, Sh_k] = 0 (at tree level).

        For the Virasoro shadow tower satisfying the master equation,
        the obstruction o^(r) = sum {Sh_j, Sh_k} and the master eq says
        nabla_H(Sh_r) + o^(r) = 0.

        This is NOT the same as saying the bracket equals an intersection
        number. It says the bracket is COMPENSATED by the next shadow."""
        S = virasoro_shadow_coeffs_symbolic(5)
        # o^(5) = {Sh_3, Sh_4}_H = 3*4*P*S_3*S_4
        Q0 = Rational(10) / (c * (5 * c + 22))
        o5 = 3 * 4 * P_inv_hess * Rational(2) * Q0
        # = 480 / (c^2 * (5c+22))
        expected_o5 = Rational(480) / (c**2 * (5*c + 22))
        assert simplify(o5 - expected_o5) == 0

        # nabla_H(Sh_5) = -o^(5), i.e., 2*5*S_5 = -o5
        S5 = S[5]
        nabla = 2 * 5 * S5
        assert simplify(nabla + expected_o5) == 0

    def test_bracket_bilinear_form_is_symmetric(self):
        """The bracket form is symmetric in the shadow coefficients."""
        S = virasoro_shadow_coeffs_symbolic(5)
        for r in range(2, 5):
            for s in range(r, 5):
                b_rs = mc_bracket_bilinear_form(S, r, s)
                b_sr = mc_bracket_bilinear_form(S, s, r)
                assert simplify(b_rs - b_sr) == 0
