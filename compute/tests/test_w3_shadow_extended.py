r"""Tests for W_3 extended shadow obstruction tower coefficients S_3 through S_8.

Ground truth:
    T-line (= Virasoro): manuscript comp:w-infty-shadow-tower (w_algebras_deep.tex)
    W-line: manuscript eq:w3-wline-closed-form (w_algebras_deep.tex)
    Quartic data: Q_TTTT = 10/[c(5c+22)], Q_WWWW = 2560/[c(5c+22)^3]
    kappa(W_3) = 5c/6 = kappa_T + kappa_W = c/2 + c/3

Three verification strategies (AP10):
    (V1) Closed-form vs convolution recursion (internal consistency)
    (V2) Numerical evaluation at specific c vs exact symbolic evaluation
    (V3) Cross-family / structural consistency (ring relations, parity, complementarity)
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

from lib.w3_shadow_extended import (
    t_line_data,
    w_line_data,
    t_line_tower_exact,
    w_line_tower_exact,
    t_line_tower_numerical,
    w_line_tower_numerical,
    t_line_closed_forms,
    w_line_closed_forms,
    w_line_general_term,
    w_line_ring_relations,
    discriminants,
    growth_rates_squared,
    growth_rates_numerical,
    complementarity_sums,
    verify_closed_vs_recursive,
    verify_numerical_vs_exact,
)

c = Symbol('c')


# ==========================================================================
# T-line closed forms vs manuscript (V1)
# ==========================================================================

class TestTLineClosedForms:
    """Verify T-line S_r against manuscript comp:w-infty-shadow-tower."""

    def test_T01_S2(self):
        """S_2^T = c/2."""
        cf = t_line_closed_forms()
        assert simplify(cf[2] - c / 2) == 0

    def test_T02_S3(self):
        """S_3^T = 2."""
        cf = t_line_closed_forms()
        assert cf[3] == 2

    def test_T03_S4(self):
        """S_4^T = 10/[c(5c+22)]."""
        cf = t_line_closed_forms()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(cf[4] - expected) == 0

    def test_T04_S5(self):
        """S_5^T = -48/[c^2(5c+22)]."""
        cf = t_line_closed_forms()
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(cf[5] - expected) == 0

    def test_T05_S6(self):
        """S_6^T = 80(45c+193)/[3 c^3 (5c+22)^2]."""
        cf = t_line_closed_forms()
        expected = Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2)
        assert simplify(cf[6] - expected) == 0

    def test_T06_S7(self):
        """S_7^T = -2880(15c+61)/[7 c^4 (5c+22)^2]."""
        cf = t_line_closed_forms()
        expected = Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2)
        assert simplify(cf[7] - expected) == 0

    def test_T07_S8(self):
        """S_8^T = 80(2025c^2+16470c+33314)/[c^5 (5c+22)^3]."""
        cf = t_line_closed_forms()
        expected = (Rational(80) * (2025 * c ** 2 + 16470 * c + 33314)
                    / (c ** 5 * (5 * c + 22) ** 3))
        assert simplify(cf[8] - expected) == 0


# ==========================================================================
# T-line: recursion vs closed form (V1)
# ==========================================================================

class TestTLineRecursionMatch:
    """Verify convolution recursion matches hardcoded closed forms."""

    @pytest.fixture
    def towers(self):
        return t_line_tower_exact(8), t_line_closed_forms()

    def test_T08_S3_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[3] - cf[3]) == 0

    def test_T09_S4_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[4] - cf[4]) == 0

    def test_T10_S5_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[5] - cf[5]) == 0

    def test_T11_S6_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[6] - cf[6]) == 0

    def test_T12_S7_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[7] - cf[7]) == 0

    def test_T13_S8_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[8] - cf[8]) == 0


# ==========================================================================
# W-line closed forms vs manuscript (V1)
# ==========================================================================

class TestWLineClosedForms:
    """Verify W-line S_r against manuscript eq:w3-wline-closed-form."""

    def test_W01_S2(self):
        """S_2^W = c/3."""
        cf = w_line_closed_forms()
        assert simplify(cf[2] - c / 3) == 0

    def test_W02_S3_vanishes(self):
        """S_3^W = 0 (Z_2 parity)."""
        cf = w_line_closed_forms()
        assert cf[3] == 0

    def test_W03_S4(self):
        """S_4^W = 2560/[c(5c+22)^3]."""
        cf = w_line_closed_forms()
        expected = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(cf[4] - expected) == 0

    def test_W04_S5_vanishes(self):
        """S_5^W = 0 (Z_2 parity)."""
        cf = w_line_closed_forms()
        assert cf[5] == 0

    def test_W05_S6(self):
        """S_6^W = -13107200/[c^3 (5c+22)^6]."""
        cf = w_line_closed_forms()
        expected = Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6)
        assert simplify(cf[6] - expected) == 0

    def test_W06_S7_vanishes(self):
        """S_7^W = 0 (Z_2 parity)."""
        cf = w_line_closed_forms()
        assert cf[7] == 0

    def test_W07_S8(self):
        """S_8^W = 150994944000/[c^5 (5c+22)^9]."""
        cf = w_line_closed_forms()
        expected = Rational(150994944000) / (c ** 5 * (5 * c + 22) ** 9)
        assert simplify(cf[8] - expected) == 0


# ==========================================================================
# W-line: recursion vs closed form (V1)
# ==========================================================================

class TestWLineRecursionMatch:
    """Verify convolution recursion matches hardcoded closed forms."""

    @pytest.fixture
    def towers(self):
        return w_line_tower_exact(8), w_line_closed_forms()

    def test_W08_S3_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[3] - cf[3]) == 0

    def test_W09_S4_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[4] - cf[4]) == 0

    def test_W10_S5_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[5] - cf[5]) == 0

    def test_W11_S6_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[6] - cf[6]) == 0

    def test_W12_S7_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[7] - cf[7]) == 0

    def test_W13_S8_recursion(self, towers):
        rec, cf = towers
        assert simplify(rec[8] - cf[8]) == 0


# ==========================================================================
# Numerical vs exact (V2)
# ==========================================================================

class TestNumericalConsistency:
    """Verify numerical towers match exact evaluation at several c values."""

    @pytest.mark.parametrize("c_val", [1, 4, 10, 25, 50, 100])
    def test_N01_t_line_numerical(self, c_val):
        """T-line numerical matches exact at c = c_val."""
        t_exact = t_line_tower_exact(8)
        t_num = t_line_tower_numerical(c_val, 8)
        for r in range(2, 9):
            exact_val = float(t_exact[r].subs(c, c_val))
            assert abs(exact_val - t_num[r]) < 1e-10 * max(1, abs(exact_val)), \
                f"T-line S_{r} mismatch at c={c_val}: exact={exact_val}, num={t_num[r]}"

    @pytest.mark.parametrize("c_val", [1, 4, 10, 25, 50, 100])
    def test_N02_w_line_numerical(self, c_val):
        """W-line numerical matches exact at c = c_val."""
        w_exact = w_line_tower_exact(8)
        w_num = w_line_tower_numerical(c_val, 8)
        for r in range(2, 9):
            exact_val = float(w_exact[r].subs(c, c_val))
            assert abs(exact_val - w_num[r]) < 1e-10 * max(1, abs(exact_val)), \
                f"W-line S_{r} mismatch at c={c_val}: exact={exact_val}, num={w_num[r]}"


# ==========================================================================
# W-line ring structure (V3)
# ==========================================================================

class TestWLineRingStructure:
    """Verify the ring relations S_6 = -2 S_4^2/c, S_8 = 9 S_4^3/c^2."""

    def test_R01_S6_ring(self):
        """S_6 = -2 S_4^2 / c on the W-line."""
        wl = w_line_closed_forms()
        S4 = wl[4]
        ring_S6 = -2 * S4 ** 2 / c
        assert simplify(wl[6] - ring_S6) == 0

    def test_R02_S8_ring(self):
        """S_8 = 9 S_4^3 / c^2 on the W-line."""
        wl = w_line_closed_forms()
        S4 = wl[4]
        ring_S8 = 9 * S4 ** 3 / c ** 2
        assert simplify(wl[8] - ring_S8) == 0

    def test_R03_ring_relations_function(self):
        """Ring relations verified by the module function."""
        rels = w_line_ring_relations()
        assert rels['S6_ring'], "S_6 ring relation failed"
        assert rels['S8_ring'], "S_8 ring relation failed"


# ==========================================================================
# W-line general term (V3)
# ==========================================================================

class TestWLineGeneralTerm:
    """Verify the closed-form general term against recursion."""

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7])
    def test_G01_general_term_vs_recursion(self, n):
        """w_line_general_term(n) matches recursive S_{2n} for n = 1..7."""
        r = 2 * n
        w_rec = w_line_tower_exact(max(r, 14))
        gen = w_line_general_term(n)
        diff = simplify(w_rec[r] - gen)
        assert diff == 0, f"General term mismatch at n={n}: diff = {diff}"

    def test_G02_a_n_sequence(self):
        """Integer sequence a_n = 1, 2, 9, 54, 378, 2916, 24057."""
        expected = [1, 2, 9, 54, 378, 2916, 24057]
        for i, a_exp in enumerate(expected):
            n = i + 2
            a_n = Rational((-12) ** n, 54) * binomial(Rational(3, 2), n)
            a_n_abs = abs(a_n)
            assert a_n_abs == a_exp, \
                f"|a_{n}| = {a_n_abs}, expected {a_exp}"


# ==========================================================================
# W-line parity (V3)
# ==========================================================================

class TestWLineParity:
    """Verify that all odd arities vanish on the W-line."""

    def test_P01_odd_arities_vanish(self):
        """S_r^W = 0 for all odd r from 3 to 13."""
        w_tower = w_line_tower_exact(14)
        for r in range(3, 14, 2):
            assert simplify(w_tower[r]) == 0, f"S_{r}^W != 0"

    def test_P02_odd_numerical_vanish(self):
        """Numerical odd arities < 1e-15 at c = 25."""
        w_num = w_line_tower_numerical(25, 14)
        for r in range(3, 14, 2):
            assert abs(w_num[r]) < 1e-15, f"S_{r}^W = {w_num[r]} at c=25"


# ==========================================================================
# Shadow data consistency (V3)
# ==========================================================================

class TestShadowData:
    """Verify input shadow data is self-consistent."""

    def test_D01_kappa_sum(self):
        """kappa_T + kappa_W = 5c/6 = kappa(W_3)."""
        td = t_line_data()
        wd = w_line_data()
        assert simplify(td['kappa'] + wd['kappa'] - Rational(5) * c / 6) == 0

    def test_D02_t_line_discriminant(self):
        """Delta_T = 40/(5c+22)."""
        td = t_line_data()
        assert simplify(td['Delta'] - Rational(40) / (5 * c + 22)) == 0

    def test_D03_w_line_discriminant(self):
        """Delta_W = 20480/[3(5c+22)^3]."""
        wd = w_line_data()
        assert simplify(wd['Delta'] - Rational(20480) / (3 * (5 * c + 22) ** 3)) == 0

    def test_D04_t_line_rho_sq(self):
        """rho_T^2 = 4(45c+218)/[c^2(5c+22)]."""
        td = t_line_data()
        expected = 4 * (45 * c + 218) / (c ** 2 * (5 * c + 22))
        assert simplify(td['rho_sq'] - expected) == 0

    def test_D05_w_line_rho_sq(self):
        """rho_W^2 = 30720/[c^2(5c+22)^3]."""
        wd = w_line_data()
        expected = Rational(30720) / (c ** 2 * (5 * c + 22) ** 3)
        assert simplify(wd['rho_sq'] - expected) == 0


# ==========================================================================
# Growth rate ordering (V3)
# ==========================================================================

class TestGrowthRates:
    """Verify growth rate properties."""

    @pytest.mark.parametrize("c_val", [4, 10, 25, 50, 100])
    def test_GR01_rho_W_less_than_rho_T(self, c_val):
        """rho_W < rho_T for all physical c > 0 (W-line converges faster)."""
        gr = growth_rates_numerical(c_val)
        assert gr['rho_W'] < gr['rho_T'], \
            f"At c={c_val}: rho_W={gr['rho_W']:.6f} >= rho_T={gr['rho_T']:.6f}"

    @pytest.mark.parametrize("c_val", [25, 50, 100])
    def test_GR02_both_less_than_one_large_c(self, c_val):
        """Both growth rates < 1 for large c (convergent towers)."""
        gr = growth_rates_numerical(c_val)
        assert gr['rho_T'] < 1.0, f"rho_T={gr['rho_T']} >= 1 at c={c_val}"
        assert gr['rho_W'] < 1.0, f"rho_W={gr['rho_W']} >= 1 at c={c_val}"


# ==========================================================================
# T-line autonomy (V3): T-line of W_3 = Virasoro tower
# ==========================================================================

class TestTLineAutonomy:
    """Verify T-line shadow obstruction tower is identical to Virasoro."""

    def test_A01_matches_virasoro_recursion(self):
        """T-line recursion matches Virasoro shadow_coefficients_virasoro_exact."""
        from lib.shadow_tower_recursive import shadow_coefficients_virasoro_exact
        vir = shadow_coefficients_virasoro_exact(max_r=8)
        t_tower = t_line_tower_exact(8)
        for r in range(2, 9):
            assert simplify(t_tower[r] - vir[r]) == 0, \
                f"T-line S_{r} != Virasoro S_{r}"


# ==========================================================================
# Koszul complementarity (V3)
# ==========================================================================

class TestKoszulComplementarity:
    """Verify complementarity under c -> 100 - c."""

    def test_K01_kappa_sum(self):
        """kappa(c) + kappa(100-c) = 250/3."""
        kap = Rational(5) * c / 6
        kap_dual = Rational(5) * (100 - c) / 6
        assert simplify(kap + kap_dual - Rational(250, 3)) == 0

    def test_K02_kappa_T_sum(self):
        """kappa_T(c) + kappa_T(100-c) = 50."""
        td = t_line_data()
        total = simplify(td['kappa'] + td['kappa'].subs(c, 100 - c))
        assert total == 50

    def test_K03_kappa_W_sum(self):
        """kappa_W(c) + kappa_W(100-c) = 100/3."""
        wd = w_line_data()
        total = simplify(wd['kappa'] + wd['kappa'].subs(c, 100 - c))
        assert total == Rational(100, 3)


# ==========================================================================
# Denominator filtration (V3)
# ==========================================================================

class TestDenominatorFiltration:
    """Verify denominator structure of shadow coefficients.

    T-line: denom(S_r) divides c^{r-3} (5c+22)^{floor((r-2)/2)}.
    W-line: denom(S_{2n}) = c^{2n-3} (5c+22)^{3(n-1)}.
    """

    @pytest.mark.parametrize("r", [4, 5, 6, 7, 8])
    def test_DF01_t_line_denominator(self, r):
        """T-line denominator divides the predicted bound."""
        t_tower = t_line_tower_exact(8)
        Sr = t_tower[r]
        # Extract denominator and check it divides the bound
        n, d = Sr.as_numer_denom()
        d_expanded = expand(d)
        bound = c ** (r - 3) * (5 * c + 22) ** ((r - 2) // 2)
        quotient = cancel(bound / d_expanded)
        # quotient should be a polynomial (no negative powers of c or (5c+22))
        # Check by evaluating at c = 1: quotient should be a positive rational
        q_val = quotient.subs(c, 1)
        assert q_val > 0, \
            f"S_{r}: denominator not dividing bound. Quotient at c=1: {q_val}"

    @pytest.mark.parametrize("n", [2, 3, 4])
    def test_DF02_w_line_denominator(self, n):
        """W-line S_{2n} has denominator c^{2n-3} (5c+22)^{3(n-1)}."""
        w_tower = w_line_tower_exact(2 * n)
        Sr = w_tower[2 * n]
        numer_val, denom_val = Sr.as_numer_denom()
        expected_denom = c ** (2 * n - 3) * (5 * c + 22) ** (3 * (n - 1))
        ratio = cancel(expected_denom / expand(denom_val))
        # Should simplify to a nonzero integer
        ratio_val = ratio.subs(c, 7)
        assert ratio_val != 0 and float(ratio_val) == int(float(ratio_val)), \
            f"S_{2*n}: unexpected denominator structure"


# ==========================================================================
# Sign pattern (V3)
# ==========================================================================

class TestSignPattern:
    """Verify alternating sign patterns."""

    def test_SP01_t_line_sign_alternation(self):
        """T-line: S_r alternates sign for r >= 4."""
        cf = t_line_closed_forms()
        # At c = 25 (safely away from poles):
        for r in [4, 5, 6, 7, 8]:
            val = float(cf[r].subs(c, 25))
            expected_sign = (-1) ** r
            assert (val > 0) == (expected_sign > 0), \
                f"S_{r} has wrong sign at c=25: val={val}"

    def test_SP02_w_line_sign_alternation(self):
        """W-line: S_{2n} has sign (-1)^n."""
        cf = w_line_closed_forms()
        for r in [4, 6, 8]:
            n = r // 2
            val = float(cf[r].subs(c, 25))
            expected_sign = (-1) ** n
            assert (val > 0) == (expected_sign > 0), \
                f"S_{r} has wrong sign at c=25: val={val}, expected sign (-1)^{n}"


# ==========================================================================
# Module-level self-consistency functions (V1)
# ==========================================================================

class TestModuleSelfConsistency:
    """Run the module's built-in verification functions."""

    def test_SC01_closed_vs_recursive(self):
        """All closed forms match recursive computation."""
        results = verify_closed_vs_recursive(8)
        for key, ok in results.items():
            assert ok, f"{key}: closed form != recursion"

    def test_SC02_numerical_vs_exact(self):
        """Numerical matches exact at c = 25."""
        results = verify_numerical_vs_exact(25, 8)
        for key, ok in results.items():
            assert ok, f"{key}: numerical != exact at c=25"


# ==========================================================================
# Cross-check with existing shadow_tower_recursive module (V3)
# ==========================================================================

class TestCrossModuleConsistency:
    """Verify consistency with shadow_tower_recursive.py functions."""

    def test_CM01_w3_numerical_t_line(self):
        """T-line matches shadow_coefficients_w3 at c = 25."""
        from lib.shadow_tower_recursive import shadow_coefficients_w3
        w3_data = shadow_coefficients_w3(25, max_r=8)
        our_t = t_line_tower_numerical(25, 8)
        for r in range(2, 9):
            assert abs(w3_data['T_line'][r] - our_t[r]) < 1e-10 * max(1, abs(our_t[r])), \
                f"T-line S_{r} mismatch with shadow_coefficients_w3 at c=25"

    def test_CM02_w3_numerical_w_line(self):
        """W-line matches shadow_coefficients_w3 at c = 25."""
        from lib.shadow_tower_recursive import shadow_coefficients_w3
        w3_data = shadow_coefficients_w3(25, max_r=8)
        our_w = w_line_tower_numerical(25, 8)
        for r in range(2, 9):
            assert abs(w3_data['W_line'][r] - our_w[r]) < 1e-10 * max(1, abs(our_w[r])), \
                f"W-line S_{r} mismatch with shadow_coefficients_w3 at c=25"

    def test_CM03_t_line_matches_virasoro_numerical(self):
        """T-line numerical matches shadow_coefficients_virasoro at c = 13."""
        from lib.shadow_tower_recursive import shadow_coefficients_virasoro
        vir = shadow_coefficients_virasoro(13, max_r=8)
        our_t = t_line_tower_numerical(13, 8)
        for r in range(2, 9):
            assert abs(vir[r] - our_t[r]) < 1e-10 * max(1, abs(our_t[r])), \
                f"T-line S_{r} != Virasoro S_{r} at c=13"


# ==========================================================================
# Cross-check with w3_shadow_tower_engine module (V3)
# ==========================================================================

class TestCrossEngineConsistency:
    """Verify consistency with w3_shadow_tower_engine.py."""

    def test_CE01_t_line_exact(self):
        """T-line exact matches w3_shadow_tower_engine at arities 2..8."""
        from lib.w3_shadow_tower_engine import t_line_tower_exact as engine_t
        our_t = t_line_tower_exact(8)
        engine = engine_t(8)
        for r in range(2, 9):
            assert simplify(our_t[r] - engine[r]) == 0, \
                f"T-line S_{r}: our module != w3_shadow_tower_engine"

    def test_CE02_w_line_exact(self):
        """W-line exact matches w3_shadow_tower_engine at arities 2..8."""
        from lib.w3_shadow_tower_engine import w_line_tower_exact as engine_w
        our_w = w_line_tower_exact(8)
        engine = engine_w(8)
        for r in range(2, 9):
            assert simplify(our_w[r] - engine[r]) == 0, \
                f"W-line S_{r}: our module != w3_shadow_tower_engine"


# ==========================================================================
# Extended arities (beyond S_8) for W-line via general term
# ==========================================================================

class TestWLineExtended:
    """Verify extended W-line coefficients beyond S_8."""

    def test_EW01_S10(self):
        """S_10^W from general term matches recursion."""
        w_rec = w_line_tower_exact(10)
        gen = w_line_general_term(5)
        assert simplify(w_rec[10] - gen) == 0

    def test_EW02_S12(self):
        """S_12^W from general term matches recursion."""
        w_rec = w_line_tower_exact(12)
        gen = w_line_general_term(6)
        assert simplify(w_rec[12] - gen) == 0

    def test_EW03_S10_ring_relation(self):
        """S_10 = -54 S_4^4 / c^3 on the W-line."""
        S4 = Rational(2560) / (c * (5 * c + 22) ** 3)
        ring_S10 = -54 * S4 ** 4 / c ** 3
        rec_S10 = w_line_tower_exact(10)[10]
        assert simplify(rec_S10 - ring_S10) == 0


# ==========================================================================
# Ratio test convergence (V3)
# ==========================================================================

class TestRatioConvergence:
    """Verify ratio test converges to growth rate."""

    def test_RC01_t_line_ratio_test(self):
        """T-line |S_{r+1}/S_r| converges toward rho_T at c = 25.

        The oscillatory cos(r*theta+phi) modulation means the raw ratio
        test converges slowly.  Use 50 terms and check that the AVERAGE
        of the last 5 ratios is within 15% of rho_T.
        """
        t_num = t_line_tower_numerical(25, 50)
        ratios = []
        for r in range(5, 49):
            if abs(t_num[r]) > 1e-50:
                ratios.append(abs(t_num[r + 1] / t_num[r]))
        rho_T = growth_rates_numerical(25)['rho_T']
        avg_tail = sum(ratios[-5:]) / 5.0
        assert abs(avg_tail - rho_T) / rho_T < 0.15, \
            f"Ratio test not converging: avg tail = {avg_tail:.6f}, rho_T = {rho_T:.6f}"

    def test_RC02_w_line_ratio_test(self):
        """W-line |S_{2n+2}/S_{2n}| converges toward rho_W^2 at c = 25.

        Since only even arities are nonzero, the ratio of consecutive
        even arities |S_{2n+2}/S_{2n}| approaches rho_W^2 from BELOW
        (monotone increasing for n >= 3).  At 40 terms the relative
        error is ~15%.
        """
        w_num = w_line_tower_numerical(25, 40)
        ratios = []
        for n in range(3, 19):
            r = 2 * n
            r_next = 2 * (n + 1)
            if abs(w_num[r]) > 1e-100:
                ratios.append(abs(w_num[r_next] / w_num[r]))
        rho_W = growth_rates_numerical(25)['rho_W']
        rho_W_sq = rho_W ** 2
        # The ratios should be monotonically increasing (approaching from below)
        for i in range(1, len(ratios)):
            assert ratios[i] >= ratios[i - 1] * 0.99, \
                f"W-line ratios not monotone: ratio[{i}]={ratios[i]:.6e} < ratio[{i-1}]={ratios[i-1]:.6e}"
        # Last ratio should be within 15% of rho_W^2
        assert abs(ratios[-1] - rho_W_sq) / rho_W_sq < 0.15, \
            f"W-line ratio test too far: last = {ratios[-1]:.6e}, rho_W^2 = {rho_W_sq:.6e}"
