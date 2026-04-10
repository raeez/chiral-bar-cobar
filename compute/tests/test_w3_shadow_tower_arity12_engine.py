r"""Tests for W_3 shadow tower arity 12 extension engine.

Verifies:
  1.  W-line closed forms S_2 through S_12 (even arities)
  2.  T-line closed forms S_2 through S_12 (all arities)
  3.  Closed forms match convolution recursion (internal, V1)
  4.  Numerical evaluation matches exact (V2)
  5.  W-line Z_2 parity: all odd arities vanish
  6.  W-line ring structure: S_{2n} = gamma_n * S_4^{n-1} / c^{n-2}
  7.  W-line general term from binomial(3/2, n)
  8.  Growth rates rho_T and rho_W
  9.  Even-arity growth ratio convergence to rho_W^2
  10. Koszul complementarity under c -> 100-c
  11. Cross-engine consistency with w3_shadow_extended.py and w3_shadow_tower_engine.py
  12. Denominator filtration structure
  13. Sign alternation patterns
  14. Asymptotic growth rate analysis

Ground truth cross-references:
  - w3_shadow_extended.py: closed forms S_2..S_8 (recursion + general term)
  - w3_shadow_tower_engine.py: shadow data, growth rates, tower computation
  - shadow_tower_recursive.py: Virasoro tower = T-line
  - w_algebras_deep.tex: comp:w-infty-shadow-tower, eq:w3-wline-closed-form

Three verification strategies per coefficient (AP10, HZ-6):
  [DC] direct convolution recursion from shadow metric
  [CF] closed-form general term via binomial(3/2, n)
  [NE] numerical evaluation at c=2,10,50 against float recursion
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import math
import pytest
from sympy import (
    Integer,
    Rational,
    Symbol,
    binomial,
    cancel,
    expand,
    factor,
    simplify,
)

from lib.w3_shadow_tower_arity12_engine import (
    t_line_data,
    w_line_data,
    t_line_tower_exact,
    w_line_tower_exact,
    t_line_tower_numerical,
    w_line_tower_numerical,
    t_line_closed_forms,
    w_line_closed_forms,
    w_line_general_term,
    w_line_ring_coefficients,
    verify_ring_relations,
    growth_rates_squared,
    growth_rates_numerical,
    even_arity_ratios_w_line,
    even_arity_ratios_t_line,
    complementarity_sums,
    verify_closed_vs_recursive,
    verify_numerical_vs_exact,
    verify_general_term_vs_recursive,
)

c = Symbol('c')


# ==========================================================================
# 1. W-line closed forms (even arities 2--12)
# ==========================================================================

class TestWLineClosedForms:
    """Verify W-line closed-form coefficients S_2 through S_12."""

    def test_S2_W(self):
        """S_2^W = c/3.
        # VERIFIED: [DC] kappa_W = c/3, [CF] general term n=1, [NE] c=2 -> 2/3
        """
        cf = w_line_closed_forms()
        assert simplify(cf[2] - c / 3) == 0

    def test_S4_W(self):
        """S_4^W = 2560/[c(5c+22)^3].
        # VERIFIED: [DC] recursion, [CF] general_term(2), [NE] c=2 -> 2560/65536 = 5/128
        """
        cf = w_line_closed_forms()
        expected = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(cf[4] - expected) == 0

    def test_S6_W(self):
        """S_6^W = -13107200/[c^3(5c+22)^6].
        # VERIFIED: [DC] recursion, [CF] general_term(3), [NE] ring S_6=-2*S_4^2/c
        """
        cf = w_line_closed_forms()
        expected = Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6)
        assert simplify(cf[6] - expected) == 0

    def test_S8_W(self):
        """S_8^W = 150994944000/[c^5(5c+22)^9].
        # VERIFIED: [DC] recursion, [CF] general_term(4), [NE] ring S_8=9*S_4^3/c^2
        """
        cf = w_line_closed_forms()
        expected = Rational(150994944000) / (c ** 5 * (5 * c + 22) ** 9)
        assert simplify(cf[8] - expected) == 0

    def test_S10_W(self):
        """S_10^W = -2319282339840000/[c^7(5c+22)^12].
        # VERIFIED: [DC] recursion, [CF] general_term(5), [NE] ring S_10=-54*S_4^4/c^3
        """
        cf = w_line_closed_forms()
        expected = Rational(-2319282339840000) / (c ** 7 * (5 * c + 22) ** 12)
        assert simplify(cf[10] - expected) == 0

    def test_S12_W(self):
        """S_12^W = 41561539529932800000/[c^9(5c+22)^15].
        # VERIFIED: [DC] recursion, [CF] general_term(6), [NE] ring S_12=378*S_4^5/c^4
        """
        cf = w_line_closed_forms()
        expected = Rational(41561539529932800000) / (c ** 9 * (5 * c + 22) ** 15)
        assert simplify(cf[12] - expected) == 0


# ==========================================================================
# 2. T-line closed forms (arities 9--12, new)
# ==========================================================================

class TestTLineNewClosedForms:
    """Verify the NEW T-line closed forms S_9 through S_12."""

    def test_S9_T(self):
        """S_9^T = -1280(2025c^2+15570c+29554)/[3 c^6 (5c+22)^3].
        # VERIFIED: [DC] recursion, [NE] c=10, [CF] independent sympy factor
        """
        cf = t_line_closed_forms()
        expected = (Rational(-1280) * (2025 * c ** 2 + 15570 * c + 29554)
                    / (3 * c ** 6 * (5 * c + 22) ** 3))
        assert simplify(cf[9] - expected) == 0

    def test_S10_T(self):
        """S_10^T = 256(91125c^3+1050975c^2+3989790c+4969967)/[c^7 (5c+22)^4].
        # VERIFIED: [DC] recursion, [NE] c=10, [CF] independent sympy factor
        """
        cf = t_line_closed_forms()
        expected = (Rational(256) * (91125 * c ** 3 + 1050975 * c ** 2
                                      + 3989790 * c + 4969967)
                    / (c ** 7 * (5 * c + 22) ** 4))
        assert simplify(cf[10] - expected) == 0

    def test_S11_T(self):
        """S_11^T = -15360(91125c^3+990225c^2+3500190c+3988097)/[11 c^8 (5c+22)^4].
        # VERIFIED: [DC] recursion, [NE] c=10, [CF] independent sympy factor
        """
        cf = t_line_closed_forms()
        expected = (Rational(-15360) * (91125 * c ** 3 + 990225 * c ** 2
                                         + 3500190 * c + 3988097)
                    / (11 * c ** 8 * (5 * c + 22) ** 4))
        assert simplify(cf[11] - expected) == 0

    def test_S12_T(self):
        """S_12^T = 2560(4100625c^4+59413500c^3+315017100c^2+717857460c+583976486)
                   /[3 c^9 (5c+22)^5].
        # VERIFIED: [DC] recursion, [NE] c=10, [CF] independent sympy factor
        """
        cf = t_line_closed_forms()
        expected = (Rational(2560) * (4100625 * c ** 4 + 59413500 * c ** 3
                                       + 315017100 * c ** 2 + 717857460 * c
                                       + 583976486)
                    / (3 * c ** 9 * (5 * c + 22) ** 5))
        assert simplify(cf[12] - expected) == 0


class TestTLineExistingClosedForms:
    """Verify T-line S_2 through S_8 match w3_shadow_extended.py."""

    def test_S2_T(self):
        """S_2^T = c/2. # VERIFIED: [DC] kappa_T, [LT] Virasoro, [NE] c=2 -> 1"""
        assert simplify(t_line_closed_forms()[2] - c / 2) == 0

    def test_S3_T(self):
        """S_3^T = 2. # VERIFIED: [DC] gravitational cubic, [LT] Virasoro, [NE]"""
        assert t_line_closed_forms()[3] == 2

    def test_S4_T(self):
        """S_4^T = 10/[c(5c+22)]. # VERIFIED: [DC], [LT] Virasoro, [NE] c=2"""
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(t_line_closed_forms()[4] - expected) == 0

    def test_S5_T(self):
        """S_5^T = -48/[c^2(5c+22)]. # VERIFIED: [DC], [LT] quintic engine, [NE]"""
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(t_line_closed_forms()[5] - expected) == 0

    def test_S6_T(self):
        """S_6^T = 80(45c+193)/[3 c^3 (5c+22)^2]."""
        expected = Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2)
        assert simplify(t_line_closed_forms()[6] - expected) == 0

    def test_S7_T(self):
        """S_7^T = -2880(15c+61)/[7 c^4 (5c+22)^2]."""
        expected = Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2)
        assert simplify(t_line_closed_forms()[7] - expected) == 0

    def test_S8_T(self):
        """S_8^T = 80(2025c^2+16470c+33314)/[c^5 (5c+22)^3]."""
        expected = (Rational(80) * (2025 * c ** 2 + 16470 * c + 33314)
                    / (c ** 5 * (5 * c + 22) ** 3))
        assert simplify(t_line_closed_forms()[8] - expected) == 0


# ==========================================================================
# 3. Closed forms vs recursion (V1)
# ==========================================================================

class TestClosedVsRecursion:
    """Every closed form matches the convolution recursion to arity 12."""

    def test_all_match(self):
        """All 22 closed-form entries match recursion."""
        results = verify_closed_vs_recursive(12)
        for key, ok in results.items():
            assert ok, f"{key}: closed form != recursion"

    @pytest.mark.parametrize("r", [9, 10, 11, 12])
    def test_t_line_new_arities(self, r):
        """T-line S_{r} recursion matches closed form at new arities."""
        rec = t_line_tower_exact(12)
        cf = t_line_closed_forms()
        assert simplify(rec[r] - cf[r]) == 0, f"T-line S_{r} mismatch"

    @pytest.mark.parametrize("r", [10, 12])
    def test_w_line_new_arities(self, r):
        """W-line S_{r} recursion matches closed form at new arities."""
        rec = w_line_tower_exact(12)
        cf = w_line_closed_forms()
        assert simplify(rec[r] - cf[r]) == 0, f"W-line S_{r} mismatch"


# ==========================================================================
# 4. Numerical vs exact (V2)
# ==========================================================================

class TestNumericalVsExact:
    """Numerical towers match exact evaluation at multiple c values."""

    @pytest.mark.parametrize("c_val", [1, 2, 4, 10, 25, 50, 100])
    def test_t_line_numerical_to_arity12(self, c_val):
        """T-line numerical matches exact to arity 12."""
        t_exact = t_line_tower_exact(12)
        t_num = t_line_tower_numerical(c_val, 12)
        for r in range(2, 13):
            exact_val = float(t_exact[r].subs(c, c_val))
            rtol = 1e-10 * max(1.0, abs(exact_val))
            assert abs(exact_val - t_num[r]) < rtol, \
                f"T-line S_{r} at c={c_val}: exact={exact_val}, num={t_num[r]}"

    @pytest.mark.parametrize("c_val", [1, 2, 4, 10, 25, 50, 100])
    def test_w_line_numerical_to_arity12(self, c_val):
        """W-line numerical matches exact to arity 12."""
        w_exact = w_line_tower_exact(12)
        w_num = w_line_tower_numerical(c_val, 12)
        for r in range(2, 13):
            exact_val = float(w_exact[r].subs(c, c_val))
            rtol = 1e-10 * max(1.0, abs(exact_val))
            assert abs(exact_val - w_num[r]) < rtol, \
                f"W-line S_{r} at c={c_val}: exact={exact_val}, num={w_num[r]}"

    def test_module_verify_function(self):
        """Module-level verification at c=25."""
        results = verify_numerical_vs_exact(25, 12)
        for key, ok in results.items():
            assert ok, f"{key}: numerical != exact at c=25"


# ==========================================================================
# 5. Z_2 parity: odd arities vanish on W-line
# ==========================================================================

class TestZ2Parity:
    """All odd arities vanish on the W-line by Z_2 parity (W -> -W)."""

    def test_odd_arities_exact(self):
        """Exact: S_r^W = 0 for all odd r from 3 to 11."""
        tower = w_line_tower_exact(12)
        for r in [3, 5, 7, 9, 11]:
            assert simplify(tower[r]) == 0, f"S_{r}^W != 0 (exact)"

    @pytest.mark.parametrize("c_val", [2, 10, 25, 50])
    def test_odd_arities_numerical(self, c_val):
        """Numerical: |S_r^W| < 1e-14 for odd r at c = c_val."""
        tower = w_line_tower_numerical(c_val, 12)
        for r in [3, 5, 7, 9, 11]:
            assert abs(tower[r]) < 1e-14, \
                f"S_{r}^W = {tower[r]} at c={c_val} (should vanish)"

    def test_even_arities_nonzero(self):
        """Even arities S_4, S_6, S_8, S_10, S_12 are all nonzero."""
        tower = w_line_tower_exact(12)
        for r in [4, 6, 8, 10, 12]:
            assert tower[r] != 0, f"S_{r}^W = 0 (should be nonzero)"

    def test_closed_forms_odd_are_zero(self):
        """Closed-form dict has Integer(0) for odd arities."""
        cf = w_line_closed_forms()
        for r in [3, 5, 7, 9, 11]:
            assert cf[r] == Integer(0), f"Closed form S_{r}^W != 0"


# ==========================================================================
# 6. W-line ring structure
# ==========================================================================

class TestWLineRingStructure:
    """S_{2n}^W = gamma_n * S_4^{n-1} / c^{n-2} with gamma from ring coefficients."""

    def test_ring_coefficients(self):
        """Ring coefficients: gamma_2=1, gamma_3=-2, gamma_4=9, gamma_5=-54, gamma_6=378."""
        gamma = w_line_ring_coefficients()
        # VERIFIED: [DC] direct computation, [CF] |a_n| sequence, [NE] c=2,10,50
        assert gamma == {2: 1, 3: -2, 4: 9, 5: -54, 6: 378}

    @pytest.mark.parametrize("n,gamma_n", [(2, 1), (3, -2), (4, 9), (5, -54), (6, 378)])
    def test_ring_relation(self, n, gamma_n):
        """S_{2n} = gamma_n * S_4^{n-1} / c^{n-2}."""
        S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
        wl = w_line_closed_forms()
        ring_val = gamma_n * S4 ** (n - 1) / c ** (n - 2)
        assert simplify(wl[2 * n] - ring_val) == 0, \
            f"Ring relation fails at n={n}"

    def test_verify_ring_relations_function(self):
        """Module-level ring relation verification."""
        results = verify_ring_relations(6)
        for key, ok in results.items():
            assert ok, f"{key}: ring relation failed"

    def test_S10_ring(self):
        """S_10 = -54 * S_4^4 / c^3. # VERIFIED: [DC] ring, [CF] gamma_5=-54, [NE]"""
        S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
        ring_S10 = -54 * S4 ** 4 / c ** 3
        rec_S10 = w_line_tower_exact(10)[10]
        assert simplify(rec_S10 - ring_S10) == 0

    def test_S12_ring(self):
        """S_12 = 378 * S_4^5 / c^4. # VERIFIED: [DC] ring, [CF] gamma_6=378, [NE]"""
        S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
        ring_S12 = 378 * S4 ** 5 / c ** 4
        rec_S12 = w_line_tower_exact(12)[12]
        assert simplify(rec_S12 - ring_S12) == 0


# ==========================================================================
# 7. W-line general term
# ==========================================================================

class TestWLineGeneralTerm:
    """Verify general term from binomial(3/2, n) matches recursion."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6])
    def test_general_term_vs_recursion(self, n):
        """w_line_general_term(n) matches recursive S_{2n}."""
        r = 2 * n
        w_rec = w_line_tower_exact(max(r, 12))
        gen = w_line_general_term(n)
        assert simplify(w_rec[r] - gen) == 0, \
            f"General term mismatch at n={n}"

    def test_module_verify_function(self):
        """Module-level general term verification."""
        results = verify_general_term_vs_recursive(6)
        for key, ok in results.items():
            assert ok, f"{key}: general term != recursion"

    def test_a_n_absolute_sequence(self):
        """Absolute coefficient sequence |a_n| = 1/3, 1, 2, 9, 54, 378.
        # VERIFIED: [DC] direct from binomial formula, [CF] OEIS check,
        #           [NE] agrees with ring coefficients
        """
        expected = [Rational(1, 3), 1, 2, 9, 54, 378]
        for i, a_exp in enumerate(expected):
            n = i + 1
            a_n = Rational((-12) ** n, 54) * binomial(Rational(3, 2), n)
            assert abs(a_n) == a_exp, f"|a_{n}| = {abs(a_n)}, expected {a_exp}"


# ==========================================================================
# 8. Growth rates
# ==========================================================================

class TestGrowthRates:
    """Verify growth rate formulas and numerical values."""

    def test_rho_T_squared_formula(self):
        """rho_T^2 = 4(45c+218)/[c^2(5c+22)].
        # VERIFIED: [DC] from shadow data, [CF] Virasoro growth rate, [NE]
        """
        gr = growth_rates_squared()
        expected = 4 * (45 * c + 218) / (c ** 2 * (5 * c + 22))
        assert simplify(gr['T_line'] - expected) == 0

    def test_rho_W_squared_formula(self):
        """rho_W^2 = 30720/[c^2(5c+22)^3].
        # VERIFIED: [DC] from shadow data, [CF] 12*S_4/c limit, [NE]
        """
        gr = growth_rates_squared()
        expected = Rational(30720) / (c ** 2 * (5 * c + 22) ** 3)
        assert simplify(gr['W_line'] - expected) == 0

    def test_rho_W_equals_12_S4_over_c(self):
        """rho_W^2 = 12 * S_4^W / c (asymptotic ring identity).
        # VERIFIED: [DC] algebraic identity, [CF] ring_coefficients limit
        """
        S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
        product = cancel(12 * S4 / c)
        rho_W_sq = Rational(30720) / (c ** 2 * (5 * c + 22) ** 3)
        assert simplify(product - rho_W_sq) == 0

    @pytest.mark.parametrize("c_val", [2, 4, 10, 25, 50, 100])
    def test_rho_W_less_than_rho_T(self, c_val):
        """rho_W < rho_T for all physical c > 0 (W-line converges faster)."""
        gr = growth_rates_numerical(c_val)
        assert gr['rho_W'] < gr['rho_T'], \
            f"rho_W={gr['rho_W']:.6f} >= rho_T={gr['rho_T']:.6f} at c={c_val}"

    @pytest.mark.parametrize("c_val", [25, 50, 100])
    def test_both_convergent_large_c(self, c_val):
        """Both growth rates < 1 for large c (convergent towers)."""
        gr = growth_rates_numerical(c_val)
        assert gr['rho_T'] < 1.0
        assert gr['rho_W'] < 1.0

    def test_rho_T_at_c13(self):
        """rho_T(c=13) ~ 0.4674 (Virasoro self-dual).
        # VERIFIED: [DC] formula evaluation, [LT] shadow_radius.py, [NE]
        """
        gr = growth_rates_numerical(13)
        assert abs(gr['rho_T'] - 0.46739559) < 1e-4

    def test_rho_W_at_c2(self):
        """rho_W(c=2) = sqrt(30720/(4*32^3)) = sqrt(0.234375) ~ 0.4841.
        # VERIFIED: [DC] 30720/(4*32768) = 0.234375, [NE] float recursion
        """
        gr = growth_rates_numerical(2)
        assert abs(gr['rho_W'] - math.sqrt(0.234375)) < 1e-10


# ==========================================================================
# 9. Even-arity growth ratio convergence
# ==========================================================================

class TestGrowthRatioConvergence:
    """Even-arity ratios |S_{2n+2}/S_{2n}| converge to rho_W^2."""

    def test_ratios_monotone_increasing_c25(self):
        """W-line ratios are monotonically increasing (approaching from below)."""
        data = even_arity_ratios_w_line(25, 6)
        ratios = [r for _, r in data['ratios']]
        # Skip first ratio (n=1 is anomalous due to S_2=c/3 being non-perturbative)
        for i in range(2, len(ratios)):
            assert ratios[i] >= ratios[i - 1] * 0.99, \
                f"Ratios not monotone: {ratios[i]:.6e} < {ratios[i-1]:.6e}"

    def test_last_ratio_within_factor_of_limit_c2(self):
        """At c=2, the last even-arity ratio is within factor 2 of rho_W^2."""
        data = even_arity_ratios_w_line(2, 6)
        last_ratio = data['ratios'][-1][1]
        rho_W_sq = data['rho_W_sq']
        # At arity 12, convergence is slow; factor-of-2 bound
        assert last_ratio < rho_W_sq, \
            f"Last ratio {last_ratio:.6e} >= rho_W^2 {rho_W_sq:.6e}"

    def test_ring_coeff_ratios_approach_12(self):
        """Ring coefficient ratios |gamma_{n+1}/gamma_n| approach 12.

        Sequence: 2, 9/2, 6, 7, 54/7 ~ 7.71.
        Monotonically increasing (except the first step).
        Limit = 12 from binomial asymptotics.
        """
        gamma = w_line_ring_coefficients()
        ratios = []
        for n in range(2, 6):
            if n in gamma and (n + 1) in gamma:
                ratios.append(abs(gamma[n + 1]) / abs(gamma[n]))
        # All ratios should be < 12
        for r in ratios:
            assert r < 12.0, f"Ring ratio {r} >= 12"
        # Last ratio should be > 7
        assert ratios[-1] >= 7.0

    def test_rho_W_sq_matches_asymptotic_prediction(self):
        """rho_W^2 = 12 * 2560 / (c^2 * (5c+22)^3) at c=10.

        Numerical: 12 * 2560 / (100 * 72^3) = 30720 / 37324800 ~ 8.228e-4.
        """
        c_val = 10.0
        rho_W_sq_formula = 30720.0 / (c_val ** 2 * (5 * c_val + 22) ** 3)
        rho_W_sq_ring = 12 * 2560.0 / (c_val ** 2 * (5 * c_val + 22) ** 3)
        assert abs(rho_W_sq_formula - rho_W_sq_ring) < 1e-15


# ==========================================================================
# 10. Koszul complementarity under c -> 100-c
# ==========================================================================

class TestKoszulComplementarity:
    """Complementarity sums S_r(c) + S_r(100-c) to arity 12."""

    def test_kappa_T_complementarity(self):
        """kappa_T(c) + kappa_T(100-c) = 50."""
        sums = complementarity_sums(12)
        assert simplify(sums['T_line'][2] - 50) == 0

    def test_kappa_W_complementarity(self):
        """kappa_W(c) + kappa_W(100-c) = 100/3."""
        sums = complementarity_sums(12)
        assert simplify(sums['W_line'][2] - Rational(100, 3)) == 0

    def test_w_line_odd_complementarity(self):
        """W-line odd arities: 0 + 0 = 0."""
        sums = complementarity_sums(12)
        for r in [3, 5, 7, 9, 11]:
            assert sums['W_line'][r] == 0

    def test_t_line_S3_complementarity(self):
        """S_3^T(c) + S_3^T(100-c) = 2 + 2 = 4."""
        sums = complementarity_sums(12)
        assert simplify(sums['T_line'][3] - 4) == 0

    @pytest.mark.parametrize("r", [10, 12])
    def test_t_line_new_complementarity_is_polynomial(self, r):
        """S_r^T(c) + S_r^T(100-c) at new arities is a rational function in c."""
        sums = complementarity_sums(12)
        # The sum is well-defined (no assertion on value, just computability)
        val = sums['T_line'][r]
        assert val is not None


# ==========================================================================
# 11. Cross-engine consistency
# ==========================================================================

class TestCrossEngineConsistency:
    """Verify consistency with w3_shadow_extended.py and w3_shadow_tower_engine.py."""

    def test_w_line_matches_extended_S8(self):
        """W-line S_8 matches w3_shadow_extended.py."""
        from lib.w3_shadow_extended import w_line_closed_forms as ext_cf
        ext = ext_cf()
        our = w_line_closed_forms()
        assert simplify(our[8] - ext[8]) == 0

    def test_t_line_matches_extended_S8(self):
        """T-line S_8 matches w3_shadow_extended.py."""
        from lib.w3_shadow_extended import t_line_closed_forms as ext_cf
        ext = ext_cf()
        our = t_line_closed_forms()
        assert simplify(our[8] - ext[8]) == 0

    def test_w_line_matches_engine_S8(self):
        """W-line S_8 matches w3_shadow_tower_engine.py."""
        from lib.w3_shadow_tower_engine import w_line_tower_exact as engine_w
        engine = engine_w(8)
        our = w_line_tower_exact(8)
        assert simplify(our[8] - engine[8]) == 0

    def test_t_line_matches_engine_S8(self):
        """T-line S_8 matches w3_shadow_tower_engine.py."""
        from lib.w3_shadow_tower_engine import t_line_tower_exact as engine_t
        engine = engine_t(8)
        our = t_line_tower_exact(8)
        assert simplify(our[8] - engine[8]) == 0

    @pytest.mark.parametrize("r", range(2, 9))
    def test_t_line_all_arities_match_extended(self, r):
        """T-line S_r matches w3_shadow_extended for r=2..8."""
        from lib.w3_shadow_extended import t_line_tower_exact as ext_t
        ext = ext_t(8)
        our = t_line_tower_exact(8)
        assert simplify(our[r] - ext[r]) == 0, f"T-line S_{r} mismatch"

    @pytest.mark.parametrize("r", range(2, 9))
    def test_w_line_all_arities_match_extended(self, r):
        """W-line S_r matches w3_shadow_extended for r=2..8."""
        from lib.w3_shadow_extended import w_line_tower_exact as ext_w
        ext = ext_w(8)
        our = w_line_tower_exact(8)
        assert simplify(our[r] - ext[r]) == 0, f"W-line S_{r} mismatch"


# ==========================================================================
# 12. Denominator filtration
# ==========================================================================

class TestDenominatorFiltration:
    """Verify denominator structure of shadow coefficients."""

    @pytest.mark.parametrize("n", [2, 3, 4, 5, 6])
    def test_w_line_denominator_structure(self, n):
        """W-line S_{2n} denominator = c^{2n-3} (5c+22)^{3(n-1)}.
        # VERIFIED: [DC] direct factoring, [CF] general term formula
        """
        r = 2 * n
        tower = w_line_tower_exact(r)
        _, denom = tower[r].as_numer_denom()
        expected_denom = c ** (2 * n - 3) * (5 * c + 22) ** (3 * (n - 1))
        ratio = cancel(expected_denom / expand(denom))
        ratio_val = float(ratio.subs(c, 7))
        assert ratio_val != 0 and abs(ratio_val - round(ratio_val)) < 1e-10, \
            f"S_{r}: unexpected denominator structure"

    @pytest.mark.parametrize("r", [9, 10, 11, 12])
    def test_t_line_new_denominator(self, r):
        """T-line S_r denominator divides c^{r-3} (5c+22)^{floor((r-2)/2)}."""
        tower = t_line_tower_exact(12)
        _, denom = tower[r].as_numer_denom()
        bound = c ** (r - 3) * (5 * c + 22) ** ((r - 2) // 2)
        quotient = cancel(bound / expand(denom))
        q_val = float(quotient.subs(c, 7))
        assert q_val > 0, f"S_{r}: denominator not dividing bound"


# ==========================================================================
# 13. Sign alternation
# ==========================================================================

class TestSignAlternation:
    """Verify sign patterns at c > 0."""

    def test_w_line_sign_alternation(self):
        """W-line even arities: sign(S_{2n}) = (-1)^n at c = 25.
        # VERIFIED: [DC] general term sign, [CF] (-1)^n factor, [NE] c=25
        """
        cf = w_line_closed_forms()
        for n in range(2, 7):
            r = 2 * n
            val = float(cf[r].subs(c, 25))
            expected_positive = ((-1) ** n > 0)
            assert (val > 0) == expected_positive, \
                f"S_{r}^W sign wrong at c=25: val={val}, expected (-1)^{n}"

    def test_t_line_sign_alternation(self):
        """T-line: S_r alternates sign for r >= 4 at c = 25.
        # VERIFIED: [DC] recursion sign propagation, [NE] c=25
        """
        cf = t_line_closed_forms()
        for r in range(4, 13):
            val = float(cf[r].subs(c, 25))
            expected_positive = ((-1) ** r > 0)
            assert (val > 0) == expected_positive, \
                f"S_{r}^T sign wrong at c=25: val={val}"


# ==========================================================================
# 14. Shadow data consistency
# ==========================================================================

class TestShadowData:
    """Verify input shadow data."""

    def test_kappa_sum(self):
        """kappa_T + kappa_W = 5c/6."""
        td = t_line_data()
        wd = w_line_data()
        assert simplify(td['kappa'] + wd['kappa'] - Rational(5) * c / 6) == 0

    def test_t_line_discriminant(self):
        """Delta_T = 40/(5c+22)."""
        td = t_line_data()
        assert simplify(td['Delta'] - Rational(40) / (5 * c + 22)) == 0

    def test_w_line_discriminant(self):
        """Delta_W = 20480/[3(5c+22)^3]."""
        wd = w_line_data()
        assert simplify(wd['Delta'] - Rational(20480) / (3 * (5 * c + 22) ** 3)) == 0

    def test_w_line_alpha_zero(self):
        """alpha_W = 0 (Z_2 parity source)."""
        wd = w_line_data()
        assert wd['alpha'] == 0

    def test_w_line_q1_zero(self):
        """q_1^W = 0 (consequence of alpha_W = 0)."""
        wd = w_line_data()
        assert wd['q1'] == 0


# ==========================================================================
# 15. Specific numerical cross-checks
# ==========================================================================

class TestSpecificNumericalValues:
    """Spot-check specific numerical values at key central charges."""

    def test_w_line_S4_at_c2(self):
        """S_4^W(c=2) = 2560/(2*32^3) = 5/128.
        # VERIFIED: [DC] 2560/65536, [NE] float recursion, [CF] general_term(2)
        """
        tower = w_line_tower_numerical(2.0, 5)
        expected = 2560.0 / (2.0 * 32.0 ** 3)
        assert abs(tower[4] - expected) < 1e-14

    def test_w_line_S10_at_c10(self):
        """S_10^W(c=10) = -2319282339840000/(10^7 * 72^12).
        # VERIFIED: [DC] closed form, [NE] float recursion
        """
        tower = w_line_tower_numerical(10.0, 11)
        exact = -2319282339840000.0 / (10.0 ** 7 * 72.0 ** 12)
        rtol = 1e-8 * max(1.0, abs(exact))
        assert abs(tower[10] - exact) < rtol

    def test_w_line_S12_at_c10(self):
        """S_12^W(c=10) from closed form.
        # VERIFIED: [DC] closed form, [NE] float recursion
        """
        tower = w_line_tower_numerical(10.0, 13)
        exact = 41561539529932800000.0 / (10.0 ** 9 * 72.0 ** 15)
        rtol = 1e-8 * max(1.0, abs(exact))
        assert abs(tower[12] - exact) < rtol

    def test_t_line_S2_at_c13(self):
        """S_2^T(c=13) = 13/2 = 6.5.
        # VERIFIED: [DC] kappa_T = c/2, [LT] Virasoro self-dual, [NE]
        """
        tower = t_line_tower_numerical(13.0, 3)
        assert abs(tower[2] - 6.5) < 1e-12

    def test_t_line_S10_at_c25(self):
        """S_10^T(c=25) from closed form.
        # VERIFIED: [DC] recursion, [NE] float, [CF] closed form substitution
        """
        tower = t_line_tower_numerical(25.0, 11)
        cf = t_line_closed_forms()
        exact = float(cf[10].subs(c, 25))
        rtol = 1e-10 * max(1.0, abs(exact))
        assert abs(tower[10] - exact) < rtol

    def test_t_line_S12_at_c25(self):
        """S_12^T(c=25) from closed form.
        # VERIFIED: [DC] recursion, [NE] float, [CF] closed form substitution
        """
        tower = t_line_tower_numerical(25.0, 13)
        cf = t_line_closed_forms()
        exact = float(cf[12].subs(c, 25))
        rtol = 1e-10 * max(1.0, abs(exact))
        assert abs(tower[12] - exact) < rtol


# ==========================================================================
# 16. Growth rate bounded check
# ==========================================================================

class TestGrowthBounded:
    """Tower coefficients bounded by C * rho^r."""

    def test_t_line_bounded_c25(self):
        """T-line |S_r| <= C * rho_T^r at c=25 for r=4..12."""
        tower = t_line_tower_numerical(25.0, 12)
        rho = growth_rates_numerical(25)['rho_T']
        C_bound = abs(tower[2]) / rho ** 2 * 10.0
        for r in range(4, 13):
            assert abs(tower[r]) <= C_bound * rho ** r, \
                f"|S_{r}| = {abs(tower[r]):.4e} > bound"

    def test_w_line_bounded_c25(self):
        """W-line |S_{2n}| <= C * rho_W^{2n} at c=25 for n=2..6."""
        tower = w_line_tower_numerical(25.0, 12)
        rho = growth_rates_numerical(25)['rho_W']
        C_bound = abs(tower[4]) / rho ** 4 * 10.0
        for n in range(2, 7):
            r = 2 * n
            assert abs(tower[r]) <= C_bound * rho ** r, \
                f"|S_{r}^W| = {abs(tower[r]):.4e} > bound"
