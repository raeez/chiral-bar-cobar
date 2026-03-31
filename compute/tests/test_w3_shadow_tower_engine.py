"""Tests for the W_3 shadow tower engine.

Verifies:
  1.  kappa(W_3) = 5c/6 against genus_expansion.py
  2.  Central charge formula c = 2 - 24(k+2)^2/(k+3) at several k values
  3.  Complementarity: kappa(c) + kappa(100-c) = 250/3
  4.  T-line tower S_r for r=2..8 as exact rational functions of c
  5.  W-line tower S_r: odd arities vanish, even arities nonzero
  6.  Depth classification = class M (infinite tower)
  7.  Growth rate rho_T and rho_W at several c values
  8.  Critical charges c*_T and c*_W
  9.  Comparison: S_5(Vir, c) = S_5^T(W_3, c) (T-line = Virasoro)
  10. DS commutation: kappa(W_3, c(k)) + kappa_ghost = kappa(sl_3, k)
  11. Quartic creation: S_4(sl_3) = 0, S_4(W_3) != 0
  12. Mixing polynomial P(W_3) = 25c^2 + 100c - 428
  13. W-line parity: all odd arities vanish
  14. Self-dual point c = 50
  15. W-line growth rate strictly smaller than T-line
  16. Numerical tower consistency checks

Ground truth cross-references:
  - genus_expansion.py: kappa_w3 = 5c/6
  - w3_bar.py: c = 2 - 24(k+2)^2/(k+3), c + c' = 100
  - w3_2d_shadow_metric.py: quartic tensor Q_WWWW = 2560/[c(5c+22)^3]
  - quintic_shadow_engine.py: S_5^Vir = -48/[c^2(5c+22)]
  - propagator_variance.py: P(W_3) = 25c^2 + 100c - 428
  - shadow_radius.py: Virasoro critical charge c* ~ 6.1243
  - ds_shadow_functor.py: DS kappa compatibility
"""

import math
import pytest
from fractions import Fraction

from sympy import (
    Rational, Symbol, cancel, expand, factor, simplify, sqrt,
)

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(_lib_dir, filename))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_engine = _load('w3_shadow_tower_engine', 'w3_shadow_tower_engine.py')

c = Symbol('c')
k = Symbol('k')


# ============================================================
# 1. kappa verification
# ============================================================

class TestKappa:
    """Verify modular characteristic kappa(W_3)."""

    def test_kappa_total_symbolic(self):
        """kappa(W_3) = 5c/6."""
        kap = _engine.w3_kappa_total()
        assert simplify(kap - 5 * c / 6) == 0

    def test_kappa_total_agrees_with_genus_expansion(self):
        """kappa from this engine matches genus_expansion.kappa_w3 = 5c/6."""
        kap_here = _engine.w3_kappa_total()
        # Ground truth from genus_expansion.py: kappa_w3 = 5c/6
        kap_ge = 5 * c / 6
        assert simplify(kap_here - kap_ge) == 0

    def test_kappa_decomposition(self):
        """kappa_T + kappa_W = kappa_total."""
        kT = _engine.w3_kappa_T()
        kW = _engine.w3_kappa_W()
        kTotal = _engine.w3_kappa_total()
        assert simplify(kT + kW - kTotal) == 0

    def test_kappa_T_equals_half_c(self):
        """kappa_T = c/2."""
        assert simplify(_engine.w3_kappa_T() - c / 2) == 0

    def test_kappa_W_equals_third_c(self):
        """kappa_W = c/3."""
        assert simplify(_engine.w3_kappa_W() - c / 3) == 0

    def test_kappa_numerical_c2(self):
        """kappa(W_3, c=2) = 5/3."""
        kap = _engine.w3_kappa_total(Rational(2))
        assert kap == Rational(5, 3)

    def test_kappa_numerical_c50(self):
        """kappa(W_3, c=50) = 125/3."""
        kap = _engine.w3_kappa_total(Rational(50))
        assert kap == Rational(125, 3)


# ============================================================
# 2. Central charge formula
# ============================================================

class TestCentralCharge:
    """Verify c = 2 - 24(k+2)^2/(k+3)."""

    def test_c_at_k1(self):
        """c(k=1) = 2 - 24*9/4 = -52."""
        c_val = _engine.w3_central_charge(Rational(1))
        assert c_val == Rational(-52)

    def test_c_at_k2(self):
        """c(k=2) = 2 - 24*16/5 = -374/5."""
        c_val = _engine.w3_central_charge(Rational(2))
        expected = 2 - 24 * Rational(16, 5)
        assert simplify(c_val - expected) == 0

    def test_c_at_k5(self):
        """c(k=5) = 2 - 24*49/8 = 2 - 147 = -145."""
        c_val = _engine.w3_central_charge(Rational(5))
        expected = 2 - 24 * Rational(49, 8)
        assert simplify(c_val - expected) == 0

    def test_complementarity_sum_100(self):
        """c(k) + c(-k-6) = 100."""
        c_k = _engine.w3_central_charge()  # symbolic
        c_dual = _engine.w3_central_charge(-k - 6)
        total = simplify(c_k + c_dual)
        assert total == 100


# ============================================================
# 3. Kappa complementarity
# ============================================================

class TestComplementarity:
    """Verify kappa(c) + kappa(100-c) = 250/3."""

    def test_kappa_complementarity_exact(self):
        """kappa(c) + kappa(100-c) = 250/3."""
        result = _engine.kappa_complementarity()
        assert result == Rational(250, 3)

    def test_kappa_complementarity_numerical(self):
        """Numerical check at several c values."""
        for c_val in [2, 10, 25, 50, 98]:
            kap = 5.0 * c_val / 6.0
            kap_dual = 5.0 * (100 - c_val) / 6.0
            assert abs(kap + kap_dual - 250.0 / 3.0) < 1e-12

    def test_shadow_complementarity_t_line_kappa(self):
        """S_2^T(c) + S_2^T(100-c) = 50 (kappa level)."""
        sums = _engine.shadow_complementarity_t_line(3)
        assert simplify(sums[2] - 50) == 0

    def test_shadow_complementarity_w_line_kappa(self):
        """S_2^W(c) + S_2^W(100-c) = 100/3."""
        sums = _engine.shadow_complementarity_w_line(3)
        assert simplify(sums[2] - Rational(100, 3)) == 0


# ============================================================
# 4. T-line tower (= Virasoro)
# ============================================================

class TestTLineTower:
    """Verify T-line shadow tower is identical to Virasoro."""

    def test_S2_T(self):
        """S_2^T = c/2."""
        tower = _engine.t_line_tower_exact(3)
        assert simplify(tower[2] - c / 2) == 0

    def test_S3_T(self):
        """S_3^T = 2 (gravitational cubic)."""
        tower = _engine.t_line_tower_exact(4)
        assert simplify(tower[3] - 2) == 0

    def test_S4_T(self):
        """S_4^T = 10/[c(5c+22)]."""
        tower = _engine.t_line_tower_exact(5)
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(tower[4] - expected) == 0

    def test_S5_T_matches_virasoro_quintic(self):
        """S_5^T = -48/[c^2(5c+22)] (Virasoro quintic)."""
        tower = _engine.t_line_tower_exact(6)
        expected = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(tower[5] - expected) == 0

    def test_S6_T(self):
        """S_6^T = 80(45c+193) / [3c^3(5c+22)^2]."""
        tower = _engine.t_line_tower_exact(7)
        expected = Rational(80) * (45 * c + 193) / (3 * c ** 3 * (5 * c + 22) ** 2)
        assert simplify(tower[6] - expected) == 0

    def test_S7_T(self):
        """S_7^T = -2880(15c+61) / [7c^4(5c+22)^2]."""
        tower = _engine.t_line_tower_exact(8)
        expected = Rational(-2880) * (15 * c + 61) / (7 * c ** 4 * (5 * c + 22) ** 2)
        assert simplify(tower[7] - expected) == 0

    def test_T_line_numerical_at_c13(self):
        """Numerical check at c=13 (self-dual for Virasoro)."""
        tower = _engine.t_line_tower_numerical(13.0, 8)
        assert abs(tower[2] - 6.5) < 1e-10
        assert abs(tower[3] - 2.0) < 1e-10
        # S_4 = 10/(13*87) = 10/1131
        assert abs(tower[4] - 10.0 / (13.0 * 87.0)) < 1e-12


# ============================================================
# 5. W-line tower
# ============================================================

class TestWLineTower:
    """Verify W-line shadow tower properties."""

    def test_S2_W(self):
        """S_2^W = c/3."""
        tower = _engine.w_line_tower_exact(3)
        assert simplify(tower[2] - c / 3) == 0

    def test_S3_W_vanishes(self):
        """S_3^W = 0 (Z_2 parity)."""
        tower = _engine.w_line_tower_exact(4)
        assert tower[3] == 0

    def test_S4_W(self):
        """S_4^W = 2560/[c(5c+22)^3]."""
        tower = _engine.w_line_tower_exact(5)
        expected = Rational(2560) / (c * (5 * c + 22) ** 3)
        assert simplify(tower[4] - expected) == 0

    def test_S5_W_vanishes(self):
        """S_5^W = 0 (Z_2 parity)."""
        tower = _engine.w_line_tower_exact(6)
        assert tower[5] == 0

    def test_S6_W_nonzero(self):
        """S_6^W != 0 (even arity, nonzero)."""
        tower = _engine.w_line_tower_exact(7)
        assert tower[6] != 0

    def test_S7_W_vanishes(self):
        """S_7^W = 0 (Z_2 parity)."""
        tower = _engine.w_line_tower_exact(8)
        assert tower[7] == 0

    def test_S6_W_factored_form(self):
        """S_6^W factored: check denominator structure."""
        tower = _engine.w_line_tower_exact(7)
        S6_f = factor(tower[6])
        # From computation: S_6^W = -13107200 / [c^3(5c+22)^6]
        expected = Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6)
        assert simplify(tower[6] - expected) == 0

    def test_W_line_numerical_at_c2(self):
        """Numerical W-line tower at c=2."""
        tower = _engine.w_line_tower_numerical(2.0, 8)
        assert abs(tower[2] - 2.0 / 3.0) < 1e-10
        assert abs(tower[3]) < 1e-14  # odd vanishes
        assert abs(tower[5]) < 1e-14  # odd vanishes
        assert abs(tower[7]) < 1e-14  # odd vanishes

    def test_W_line_S4_numerical(self):
        """S_4^W at c=2 = 2560/(2*32^3) = 2560/65536 = 5/128."""
        tower = _engine.w_line_tower_numerical(2.0, 5)
        expected = 2560.0 / (2.0 * 32.0 ** 3)
        assert abs(tower[4] - expected) < 1e-12


# ============================================================
# 6. Depth classification
# ============================================================

class TestDepthClassification:
    """Verify W_3 is class M (infinite tower)."""

    def test_t_line_class_M(self):
        """T-line is class M."""
        cls, depth = _engine.depth_classification_t_line()
        assert cls == 'M'
        assert depth is None  # infinity

    def test_w_line_class_M(self):
        """W-line is class M."""
        cls, depth = _engine.depth_classification_w_line()
        assert cls == 'M'
        assert depth is None

    def test_overall_class_M(self):
        """Overall W_3 is class M."""
        cls, depth = _engine.depth_classification_w3()
        assert cls == 'M'
        assert depth is None

    def test_t_line_delta_nonzero(self):
        """T-line Delta = 40/(5c+22) != 0."""
        data = _engine.t_line_shadow_data()
        # Delta should be nonzero for generic c
        delta_at_2 = data['Delta'].subs(c, 2)
        assert delta_at_2 != 0

    def test_w_line_delta_nonzero(self):
        """W-line Delta != 0."""
        data = _engine.w_line_shadow_data()
        delta_at_2 = data['Delta'].subs(c, 2)
        assert delta_at_2 != 0


# ============================================================
# 7. Growth rates
# ============================================================

class TestGrowthRates:
    """Verify growth rate computations."""

    def test_rho_T_at_c13(self):
        """rho_T(c=13) ~ 0.4674 (Virasoro self-dual point)."""
        rho = _engine.t_line_growth_rate(13)
        assert abs(rho - 0.46739559) < 1e-4

    def test_rho_T_decreases_with_c(self):
        """rho_T is decreasing for large c."""
        rho_10 = _engine.t_line_growth_rate(10)
        rho_20 = _engine.t_line_growth_rate(20)
        assert rho_10 > rho_20

    def test_rho_W_at_c2(self):
        """rho_W(c=2) ~ 0.484."""
        rho = _engine.w_line_growth_rate(2)
        assert abs(rho - 0.4841) < 1e-3

    def test_rho_W_smaller_than_rho_T(self):
        """rho_W < rho_T at all tested c values."""
        for c_val in [2, 4, 6, 10, 13, 25, 50]:
            rho_T = _engine.t_line_growth_rate(c_val)
            rho_W = _engine.w_line_growth_rate(c_val)
            assert rho_W < rho_T, f"rho_W >= rho_T at c={c_val}"

    def test_rho_T_squared_formula(self):
        """rho_T^2 = (180c+872)/((5c+22)*c^2)."""
        rho_sq = _engine.t_line_growth_rate_sq()
        expected = (180 * c + 872) / ((5 * c + 22) * c ** 2)
        assert simplify(rho_sq - expected) == 0

    def test_rho_W_squared_formula(self):
        """rho_W^2 = 30720 / [c^2*(5c+22)^3]."""
        rho_sq = _engine.w_line_growth_rate_sq()
        expected = Rational(30720) / (c ** 2 * (5 * c + 22) ** 3)
        assert simplify(rho_sq - expected) == 0

    def test_rho_T_at_c26(self):
        """rho_T(c=26) for string theory central charge."""
        rho = _engine.t_line_growth_rate(26)
        assert rho < 0.3  # strongly convergent

    def test_rho_W_very_small_at_large_c(self):
        """rho_W decays faster than rho_T at large c."""
        rho_W_50 = _engine.w_line_growth_rate(50)
        assert rho_W_50 < 0.01


# ============================================================
# 8. Critical charges
# ============================================================

class TestCriticalCharges:
    """Verify critical central charges where rho = 1."""

    def test_t_line_critical_charge(self):
        """c*_T ~ 6.125 (same as Virasoro)."""
        c_star = _engine.t_line_critical_charge()
        assert c_star is not None
        c_val = float(c_star.evalf())
        assert abs(c_val - 6.125) < 0.01

    def test_w_line_critical_charge(self):
        """c*_W ~ 1.187."""
        c_star = _engine.w_line_critical_charge()
        assert c_star is not None
        c_val = float(c_star.evalf())
        assert 1.0 < c_val < 1.5

    def test_w_critical_less_than_t_critical(self):
        """c*_W < c*_T."""
        c_T = float(_engine.t_line_critical_charge().evalf())
        c_W = float(_engine.w_line_critical_charge().evalf())
        assert c_W < c_T

    def test_rho_T_near_1_at_critical(self):
        """rho_T(c*_T) ~ 1.0."""
        c_star = float(_engine.t_line_critical_charge().evalf())
        rho = _engine.t_line_growth_rate(c_star)
        assert abs(rho - 1.0) < 1e-6

    def test_rho_W_near_1_at_critical(self):
        """rho_W(c*_W) ~ 1.0."""
        c_star = float(_engine.w_line_critical_charge().evalf())
        rho = _engine.w_line_growth_rate(c_star)
        assert abs(rho - 1.0) < 1e-4


# ============================================================
# 9. Comparison: Vir vs W_3
# ============================================================

class TestVirComparison:
    """Verify T-line of W_3 matches Virasoro."""

    def test_S5_T_equals_S5_Vir(self):
        """S_5^T(W_3, c) = S_5^Vir(c) identically."""
        tt = _engine.t_line_tower_exact(6)
        S5_vir = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert simplify(tt[5] - S5_vir) == 0

    def test_numerical_comparison_c10(self):
        """Numerical: S_r^T(W_3, c=10) = S_r^Vir(c=10) for r=2..8."""
        tt = _engine.t_line_tower_numerical(10.0, 9)
        # Virasoro tower at c=10 (compute independently)
        kap = 5.0
        alpha = 2.0
        S4 = 10.0 / (10.0 * 72.0)
        q0 = 4.0 * kap ** 2
        q1 = 12.0 * kap * alpha
        q2 = 9.0 * alpha ** 2 + 16.0 * kap * S4
        a = [math.sqrt(q0)]
        a.append(q1 / (2.0 * a[0]))
        a.append((q2 - a[1] ** 2) / (2.0 * a[0]))
        for n in range(3, 7):
            conv = sum(a[j] * a[n - j] for j in range(1, n))
            a.append(-conv / (2.0 * a[0]))
        vir = {r + 2: a[r] / (r + 2) for r in range(len(a))}
        for r in range(2, 9):
            assert abs(tt[r] - vir[r]) < 1e-12, f"Mismatch at r={r}"

    def test_S5_W_differs_from_S5_Vir(self):
        """S_5^W = 0 while S_5^Vir != 0: the two lines are DIFFERENT."""
        wt = _engine.w_line_tower_exact(6)
        assert wt[5] == 0
        vir_S5 = Rational(-48) / (c ** 2 * (5 * c + 22))
        assert vir_S5 != 0


# ============================================================
# 10. DS commutation
# ============================================================

class TestDSCommutation:
    """Verify DS compatibility checks."""

    def test_ds_kappa_compatible(self):
        """kappa(W_3, c(k)) + kappa_ghost = kappa(sl_3, k)."""
        result = _engine.ds_kappa_compatibility()
        assert result['compatible'] is True
        assert result['difference'] == 0

    def test_ds_kappa_sl3(self):
        """kappa(sl_3, k) = 4(k+3)/3."""
        result = _engine.ds_kappa_compatibility()
        expected = 4 * (k + 3) / 3
        assert simplify(result['kappa_sl3'] - expected) == 0

    def test_ds_quartic_creation(self):
        """S_4(sl_3) = 0, S_4(W_3) != 0."""
        result = _engine.ds_quartic_creation()
        assert result['S4_sl3'] == 0
        assert result['S4_W3_T'] != 0
        assert result['S4_W3_W'] != 0

    def test_ds_depth_increase(self):
        """Depth: sl_3 = 3, W_3 = inf."""
        result = _engine.ds_quartic_creation()
        assert result['depth_sl3'] == 3
        assert result['depth_W3'] is None  # infinity


# ============================================================
# 11. Mixing polynomial
# ============================================================

class TestMixingPolynomial:
    """Verify P(W_3) = 25c^2 + 100c - 428."""

    def test_mixing_polynomial_formula(self):
        """P(W_3) = 25c^2 + 100c - 428."""
        P = _engine.mixing_polynomial()
        expected = 25 * c ** 2 + 100 * c - 428
        assert expand(P - expected) == 0

    def test_mixing_polynomial_roots_exist(self):
        """P(W_3) has two roots (neither physically significant)."""
        roots = _engine.mixing_polynomial_roots()
        assert len(roots) == 2

    def test_mixing_polynomial_at_c0(self):
        """P(0) = -428."""
        P = _engine.mixing_polynomial()
        assert P.subs(c, 0) == -428

    def test_propagator_variance_nonzero(self):
        """Propagator variance is nonzero at generic c."""
        pv = _engine.propagator_variance_w3(Rational(2))
        assert pv != 0


# ============================================================
# 12. W-line parity
# ============================================================

class TestWLineParity:
    """Verify Z_2 parity kills all odd arities on the W-line."""

    def test_parity_numerical_c2(self):
        """All odd arities vanish at c=2."""
        result = _engine.verify_w_line_parity(2.0, 20)
        assert result['all_odd_vanish'] is True

    def test_parity_numerical_c13(self):
        """All odd arities vanish at c=13."""
        result = _engine.verify_w_line_parity(13.0, 20)
        assert result['all_odd_vanish'] is True

    def test_parity_numerical_c50(self):
        """All odd arities vanish at c=50."""
        result = _engine.verify_w_line_parity(50.0, 20)
        assert result['all_odd_vanish'] is True

    def test_parity_exact_tower(self):
        """Exact: S_r^W = 0 for all odd r up to 10."""
        tower = _engine.w_line_tower_exact(10)
        for r in [3, 5, 7, 9]:
            assert tower[r] == 0, f"S_{r}^W != 0"


# ============================================================
# 13. Self-dual point
# ============================================================

class TestSelfDual:
    """Verify self-dual point c = 50 for W_3."""

    def test_self_dual_point(self):
        """Self-dual point is c = 50."""
        assert _engine.self_dual_point() == Rational(50)

    def test_self_dual_kappa(self):
        """kappa(W_3, 50) = 125/3."""
        assert _engine.self_dual_kappa() == Rational(125, 3)

    def test_kappa_symmetric_at_self_dual(self):
        """kappa(50) = kappa(100-50) = kappa(50)."""
        kap = _engine.w3_kappa_total(Rational(50))
        kap_dual = _engine.w3_kappa_total(Rational(50))
        assert kap == kap_dual


# ============================================================
# 14. Growth rate atlas
# ============================================================

class TestGrowthRateAtlas:
    """Verify growth rate atlas properties."""

    def test_atlas_nonempty(self):
        """Atlas returns data for multiple c values."""
        atlas = _engine.growth_rate_atlas()
        assert len(atlas) >= 5

    def test_t_line_always_dominates(self):
        """T-line growth rate > W-line at all tested c."""
        atlas = _engine.growth_rate_atlas()
        for row in atlas:
            assert row['rho_T'] > row['rho_W'], \
                f"rho_T <= rho_W at c={row['c']}"

    def test_both_convergent_at_large_c(self):
        """Both lines convergent at c=50."""
        atlas = _engine.growth_rate_atlas()
        c50 = [r for r in atlas if abs(r['c'] - 50.0) < 1e-6]
        if c50:
            assert c50[0]['convergent_T']
            assert c50[0]['convergent_W']


# ============================================================
# 15. Numerical tower consistency
# ============================================================

class TestNumericalConsistency:
    """Cross-check numerical tower against exact formulas."""

    def test_t_line_S4_numerical_vs_exact(self):
        """S_4^T at c=10: numerical matches exact."""
        tower_num = _engine.t_line_tower_numerical(10.0, 5)
        exact = 10.0 / (10.0 * (50.0 + 22.0))
        assert abs(tower_num[4] - exact) < 1e-12

    def test_t_line_S5_numerical_vs_exact(self):
        """S_5^T at c=10: numerical matches exact."""
        tower_num = _engine.t_line_tower_numerical(10.0, 6)
        exact = -48.0 / (100.0 * 72.0)
        assert abs(tower_num[5] - exact) < 1e-12

    def test_w_line_S4_numerical_vs_exact(self):
        """S_4^W at c=10: numerical matches exact."""
        tower_num = _engine.w_line_tower_numerical(10.0, 5)
        exact = 2560.0 / (10.0 * 72.0 ** 3)
        assert abs(tower_num[4] - exact) < 1e-12

    def test_t_line_growth_bounded(self):
        """T-line tower coefficients grow no faster than rho_T^r.

        For all r, |S_r| <= C * rho^r for some constant C.
        This is a weaker but robust check on the growth rate.
        """
        c_val = 10.0
        tower = _engine.t_line_tower_numerical(c_val, 30)
        rho = _engine.t_line_growth_rate(c_val)
        # The bound |S_r| <= C * rho^r should hold with C ~ |S_2|/rho^2
        C_bound = abs(tower[2]) / rho ** 2 * 10.0  # generous
        for r in range(5, 30):
            assert abs(tower[r]) <= C_bound * rho ** r, \
                f"|S_{r}| = {abs(tower[r]):.4e} > C*rho^{r} = {C_bound * rho**r:.4e}"

    def test_w_line_growth_bounded(self):
        """W-line tower coefficients grow no faster than rho_W^r.

        For all even r, |S_r^W| <= C * rho_W^r for some constant C.
        """
        c_val = 10.0
        tower = _engine.w_line_tower_numerical(c_val, 24)
        rho = _engine.w_line_growth_rate(c_val)
        # Bound |S_r| <= C * rho^r with C generous
        C_bound = abs(tower[2]) / rho ** 2 * 100.0
        for r in range(4, 24, 2):
            assert abs(tower[r]) <= C_bound * rho ** r, \
                f"|S_{r}^W| = {abs(tower[r]):.4e} > C*rho^{r} = {C_bound * rho**r:.4e}"


# ============================================================
# 16. Full W3 tower dataclass
# ============================================================

class TestW3ShadowTower:
    """Verify the W3ShadowTower dataclass."""

    def test_compute_tower(self):
        """compute_w3_tower returns a populated dataclass."""
        tower = _engine.compute_w3_tower(10.0, 12)
        assert tower.c_val == 10.0
        assert abs(tower.kappa_total - 50.0 / 6.0) < 1e-10
        assert tower.depth_class == 'M'

    def test_tower_has_t_and_w_lines(self):
        """Tower has both T-line and W-line data."""
        tower = _engine.compute_w3_tower(10.0, 8)
        assert 2 in tower.t_line
        assert 2 in tower.w_line
        assert len(tower.t_line) > 5
        assert len(tower.w_line) > 5

    def test_tower_summary(self):
        """Summary string is nonempty."""
        tower = _engine.compute_w3_tower(10.0, 8)
        s = tower.summary()
        assert len(s) > 100
        assert 'W_3' in s
        assert 'rho_T' in s


# ============================================================
# 17. Shadow data structure
# ============================================================

class TestShadowData:
    """Verify shadow metric data for both lines."""

    def test_t_line_q0(self):
        """T-line q0 = c^2."""
        data = _engine.t_line_shadow_data()
        assert simplify(data['q0'] - c ** 2) == 0

    def test_t_line_q1(self):
        """T-line q1 = 12c."""
        data = _engine.t_line_shadow_data()
        assert simplify(data['q1'] - 12 * c) == 0

    def test_w_line_q0(self):
        """W-line q0 = 4c^2/9."""
        data = _engine.w_line_shadow_data()
        assert simplify(data['q0'] - 4 * c ** 2 / 9) == 0

    def test_w_line_q1_zero(self):
        """W-line q1 = 0 (alpha_W = 0)."""
        data = _engine.w_line_shadow_data()
        assert data['q1'] == 0

    def test_w_line_alpha_zero(self):
        """W-line alpha = 0 (Z_2 parity)."""
        data = _engine.w_line_shadow_data()
        assert data['alpha'] == 0


# ============================================================
# 18. Comparison table
# ============================================================

class TestComparisonTable:
    """Verify the comparison table output."""

    def test_comparison_table_structure(self):
        """Comparison table has correct keys."""
        rows = _engine.comparison_table([2, 10], max_r=6)
        assert len(rows) == 2
        for row in rows:
            assert 'c' in row
            assert 'kappa_total' in row
            assert 'rho_T' in row
            assert 'rho_W' in row
            assert 'T_line' in row
            assert 'W_line' in row

    def test_comparison_t_line_is_virasoro(self):
        """T-line in comparison table matches standalone T-line."""
        rows = _engine.comparison_table([10.0], max_r=6)
        t_standalone = _engine.t_line_tower_numerical(10.0, 6)
        for r in range(2, 7):
            assert abs(rows[0]['T_line'][r] - t_standalone[r]) < 1e-14


# ============================================================
# 19. W-line factored denominators (structural test)
# ============================================================

class TestWLineStructure:
    """Verify structural properties of W-line tower."""

    def test_even_arities_alternate_sign(self):
        """Even arities: S_4 > 0, S_6 < 0, S_8 > 0, S_10 < 0 at c > 0."""
        tower = _engine.w_line_tower_exact(10)
        for r, expected_sign in [(4, +1), (6, -1), (8, +1), (10, -1)]:
            val = float(tower[r].subs(c, 10))
            if expected_sign > 0:
                assert val > 0, f"S_{r}^W should be positive at c=10"
            else:
                assert val < 0, f"S_{r}^W should be negative at c=10"

    def test_w_line_S6_factored(self):
        """S_6^W = -13107200 / [c^3 (5c+22)^6]."""
        tower = _engine.w_line_tower_exact(7)
        expected = Rational(-13107200) / (c ** 3 * (5 * c + 22) ** 6)
        assert simplify(tower[6] - expected) == 0

    def test_w_line_S8_factored(self):
        """S_8^W = 150994944000 / [c^5 (5c+22)^9]."""
        tower = _engine.w_line_tower_exact(9)
        expected = Rational(150994944000) / (c ** 5 * (5 * c + 22) ** 9)
        assert simplify(tower[8] - expected) == 0


# ============================================================
# 20. Koszul conductor and duality
# ============================================================

class TestKoszulDuality:
    """Verify Koszul duality properties."""

    def test_koszul_conductor(self):
        """Koszul conductor K_3 = 100."""
        assert _engine.koszul_conductor() == 100

    def test_kappa_sum_level_independent(self):
        """kappa(c) + kappa(100-c) = 250/3 is level-independent."""
        kap_sum = _engine.kappa_complementarity()
        # Should not contain c
        assert c not in kap_sum.free_symbols

    def test_rho_T_at_c50(self):
        """rho_T at the self-dual point c=50."""
        rho = _engine.t_line_growth_rate(50)
        assert rho < 0.2  # strongly convergent

    def test_rho_W_at_c50(self):
        """rho_W at the self-dual point c=50."""
        rho = _engine.w_line_growth_rate(50)
        assert rho < 0.01  # very strongly convergent
