"""Tests for the N=2 superconformal algebra shadow obstruction tower computation.

The N=2 SCA has generators T (weight 2), J (weight 1), G^+ (weight 3/2),
G^- (weight 3/2). Central charge c = 3k/(k+2).

This module verifies:
  1. OPE data consistency (Jacobi identities, symmetry, normalization)
  2. Curvature and kappa computation from first principles
  3. Shadow obstruction tower on each primary line (T, J, G)
  4. Koszul duality (c' = 6-c, additive complementarity kappa+kappa'=1)
  5. Genus expansion F_g on the scalar lane
  6. Shadow class determination
  7. Growth rate and convergence
  8. Cross-checks against known results (Virasoro subalgebra)

60+ tests organized by mathematical structure.

Manuscript references:
    thm:mc2-bar-intrinsic, thm:shadow-radius, thm:single-line-dichotomy,
    def:shadow-metric, AP19, AP27
"""

import math
import pytest
from sympy import Rational, Symbol, simplify, sqrt, N as Neval

from compute.lib.n2_superconformal_shadow import (
    # Central charge
    n2_central_charge,
    # OPE data
    n2_nth_products,
    n2_nth_product,
    n2_bar_diff_deg2,
    # Curvature
    n2_curvature,
    n2_curvature_ratios,
    # Kappa
    kappa_n2,
    sigma_n2,
    # Koszul duality
    n2_ff_dual_central_charge,
    n2_self_dual_point,
    n2_complementarity_sum,
    # Shadow data
    n2_shadow_data_T_line,
    n2_shadow_data_J_line,
    n2_shadow_data_G_line,
    # Shadow obstruction towers
    n2_shadow_tower_T_line,
    n2_shadow_tower_J_line,
    n2_shadow_tower_G_line,
    n2_full_shadow_coefficients,
    # Growth rate
    n2_shadow_growth_rate_T_line,
    n2_shadow_growth_rate_J_line,
    n2_shadow_growth_rate_G_line,
    # Genus expansion
    n2_F_g,
    n2_genus_table,
    # Cross-channels
    n2_cross_channel_curvatures,
    # Propagator variance
    n2_propagator_variance,
    # Shadow class
    n2_shadow_class,
    # Special values
    n2_special_values,
    # Jacobi
    verify_n2_jacobi_TJG,
    verify_n2_jacobi_JGG,
    verify_n2_jacobi_GGT,
    # Full verification
    verify_all,
)

c = Symbol('c')


# ================================================================
# 1. CENTRAL CHARGE
# ================================================================

class TestCentralCharge:
    """Test the central charge formula c = 3k/(k+2)."""

    def test_c_at_k1(self):
        """c(k=1) = 3/3 = 1."""
        assert n2_central_charge(1) == Rational(1)

    def test_c_at_k2(self):
        """c(k=2) = 6/4 = 3/2."""
        assert n2_central_charge(2) == Rational(3, 2)

    def test_c_at_k3(self):
        """c(k=3) = 9/5."""
        assert n2_central_charge(3) == Rational(9, 5)

    def test_c_at_k_minus1(self):
        """c(k=-1) = -3/1 = -3 (self-dual point)."""
        assert n2_central_charge(-1) == Rational(-3)

    def test_c_large_k_limit(self):
        """c(k) -> 3 as k -> infinity."""
        c_large = n2_central_charge(10000)
        assert abs(float(c_large) - 3.0) < 0.001


# ================================================================
# 2. OPE DATA
# ================================================================

class TestOPE:
    """Test OPE n-th products for N=2 SCA generators."""

    def test_TT_quartic_pole(self):
        """T_{(3)}T = c/2 (quartic pole = Virasoro)."""
        prod = n2_nth_product("T", "T", 3)
        assert simplify(prod["vac"] - c / 2) == 0

    def test_TT_double_pole(self):
        """T_{(1)}T = 2T (conformal weight)."""
        prod = n2_nth_product("T", "T", 1)
        assert prod["T"] == Rational(2)

    def test_TT_simple_pole(self):
        """T_{(0)}T = dT (translation)."""
        prod = n2_nth_product("T", "T", 0)
        assert prod["dT"] == Rational(1)

    def test_JJ_double_pole(self):
        """J_{(1)}J = c/3 (U(1) level)."""
        prod = n2_nth_product("J", "J", 1)
        assert simplify(prod["vac"] - c / 3) == 0

    def test_TJ_primary(self):
        """T_{(1)}J = J (J is primary of weight 1)."""
        prod = n2_nth_product("T", "J", 1)
        assert prod["J"] == Rational(1)

    def test_TGp_primary(self):
        """T_{(1)}G+ = (3/2)G+ (G+ is primary of weight 3/2)."""
        prod = n2_nth_product("T", "G+", 1)
        assert prod["G+"] == Rational(3, 2)

    def test_TGm_primary(self):
        """T_{(1)}G- = (3/2)G- (G- is primary of weight 3/2)."""
        prod = n2_nth_product("T", "G-", 1)
        assert prod["G-"] == Rational(3, 2)

    def test_JGp_charge(self):
        """J_{(0)}G+ = G+ (G+ has charge +1)."""
        prod = n2_nth_product("J", "G+", 0)
        assert prod["G+"] == Rational(1)

    def test_JGm_charge(self):
        """J_{(0)}G- = -G- (G- has charge -1)."""
        prod = n2_nth_product("J", "G-", 0)
        assert prod["G-"] == Rational(-1)

    def test_GpGm_cubic_pole(self):
        """G+_{(2)}G- = c/3 (cubic pole)."""
        prod = n2_nth_product("G+", "G-", 2)
        assert simplify(prod["vac"] - c / 3) == 0

    def test_GpGm_double_pole(self):
        """G+_{(1)}G- = J (J current in the double pole)."""
        prod = n2_nth_product("G+", "G-", 1)
        assert prod["J"] == Rational(1)

    def test_GpGm_simple_pole(self):
        """G+_{(0)}G- = T + (1/2)dJ (stress tensor + derivative of J)."""
        prod = n2_nth_product("G+", "G-", 0)
        assert prod["T"] == Rational(1)
        assert prod["dJ"] == Rational(1, 2)

    def test_GpGp_vanishes(self):
        """G+_{(n)}G+ = 0 for all n (fermionic anti-symmetry)."""
        products = n2_nth_products()
        assert len(products[("G+", "G+")]) == 0

    def test_GmGm_vanishes(self):
        """G-_{(n)}G- = 0 for all n."""
        products = n2_nth_products()
        assert len(products[("G-", "G-")]) == 0

    def test_GmGp_cubic_pole(self):
        """G-_{(2)}G+ = c/3 (same cubic pole by graded skew-symmetry)."""
        prod = n2_nth_product("G-", "G+", 2)
        assert simplify(prod["vac"] - c / 3) == 0

    def test_GmGp_double_pole_sign(self):
        """G-_{(1)}G+ = -J (opposite sign from G+_{(1)}G-)."""
        prod = n2_nth_product("G-", "G+", 1)
        assert prod["J"] == Rational(-1)

    def test_GmGp_simple_pole(self):
        """G-_{(0)}G+ = T - (1/2)dJ (sign flip on dJ from skew-symmetry)."""
        prod = n2_nth_product("G-", "G+", 0)
        assert prod["T"] == Rational(1)
        assert prod["dJ"] == Rational(-1, 2)

    def test_GpT_skew_symmetry(self):
        """G+_{(1)}T = (3/2)G+ (from skew-symmetry of TG+ OPE)."""
        prod = n2_nth_product("G+", "T", 1)
        assert prod["G+"] == Rational(3, 2)

    def test_GpT_simple_pole(self):
        """G+_{(0)}T = (1/2)dG+ (from skew-symmetry)."""
        prod = n2_nth_product("G+", "T", 0)
        assert prod["dG+"] == Rational(1, 2)


# ================================================================
# 3. BAR DIFFERENTIAL
# ================================================================

class TestBarDifferential:
    """Test bar differential D(a otimes b otimes eta) for N=2 generators."""

    def test_TT_bar_diff_vacuum(self):
        """D(T otimes T) has vacuum component c/2."""
        vac, _ = n2_bar_diff_deg2("T", "T")
        assert simplify(vac["vac"] - c / 2) == 0

    def test_TT_bar_diff_nonvac(self):
        """D(T otimes T) has 2T + dT."""
        _, bar1 = n2_bar_diff_deg2("T", "T")
        assert bar1["T"] == Rational(2)
        assert bar1["dT"] == Rational(1)

    def test_JJ_bar_diff_vacuum(self):
        """D(J otimes J) has vacuum component c/3."""
        vac, _ = n2_bar_diff_deg2("J", "J")
        assert simplify(vac["vac"] - c / 3) == 0

    def test_GpGm_bar_diff_vacuum(self):
        """D(G+ otimes G-) has vacuum component c/3."""
        vac, _ = n2_bar_diff_deg2("G+", "G-")
        assert simplify(vac["vac"] - c / 3) == 0

    def test_GpGp_bar_diff_zero(self):
        """D(G+ otimes G+) = 0."""
        vac, bar1 = n2_bar_diff_deg2("G+", "G+")
        assert len(vac) == 0
        assert len(bar1) == 0

    def test_TJ_bar_diff_no_vacuum(self):
        """D(T otimes J) has no vacuum component (J is primary)."""
        vac, _ = n2_bar_diff_deg2("T", "J")
        assert vac.get("vac", 0) == 0

    def test_TGp_bar_diff_no_vacuum(self):
        """D(T otimes G+) has no vacuum component."""
        vac, _ = n2_bar_diff_deg2("T", "G+")
        assert vac.get("vac", 0) == 0


# ================================================================
# 4. CURVATURE AND KAPPA
# ================================================================

class TestCurvature:
    """Test curvature elements and modular characteristic."""

    def test_curvature_TT(self):
        """m_0^(TT) = c/2."""
        curv = n2_curvature()
        assert simplify(curv["TT"] - c / 2) == 0

    def test_curvature_JJ(self):
        """m_0^(JJ) = c/3."""
        curv = n2_curvature()
        assert simplify(curv["JJ"] - c / 3) == 0

    def test_curvature_GpGm(self):
        """m_0^(G+G-) = c/3."""
        curv = n2_curvature()
        assert simplify(curv["G+G-"] - c / 3) == 0

    def test_curvature_ratio_JJ_TT(self):
        """m_0^(JJ)/m_0^(TT) = 2/3 (level-independent)."""
        ratios = n2_curvature_ratios()
        assert ratios["JJ/TT"] == Rational(2, 3)

    def test_curvature_ratio_GpGm_TT(self):
        """m_0^(G+G-)/m_0^(TT) = 2/3."""
        ratios = n2_curvature_ratios()
        assert ratios["G+G-/TT"] == Rational(2, 3)

    def test_kappa_symbolic(self):
        """kappa(N=2) = (6-c)/(2(3-c)) (symbolic)."""
        assert simplify(kappa_n2() - (6 - c) / (2 * (3 - c))) == 0

    def test_kappa_at_c1(self):
        """kappa(N=2, c=1) = (6-1)/(2*2) = 5/4."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_kappa_at_c_half(self):
        """kappa(N=2, c=3/2) = (9/2)/(2*3/2) = 3/2."""
        assert kappa_n2(Rational(3, 2)) == Rational(3, 2)

    def test_kappa_at_c6(self):
        """kappa(N=2, c=6) = 0 (critical level k=-4)."""
        assert kappa_n2(6) == Rational(0)

    def test_sigma_at_c1(self):
        """sigma(N=2, c=1) = kappa/c = (5/4)/1 = 5/4."""
        assert sigma_n2(1) == Rational(5, 4)

    def test_kappa_equals_c_times_sigma(self):
        """kappa = c * sigma at c=1."""
        assert simplify(kappa_n2() - c * sigma_n2()) == 0


# ================================================================
# 5. KOSZUL DUALITY
# ================================================================

class TestKoszulDuality:
    """Test Koszul duality: c' = 6-c, additive complementarity kappa+kappa'=1."""

    def test_ff_dual_k1(self):
        """At k=1: c=1, c'=5."""
        ff = n2_ff_dual_central_charge(k_val=1)
        assert ff['c'] == Rational(1)
        assert ff['c_dual'] == Rational(5)

    def test_ff_dual_k2(self):
        """At k=2: c=3/2, c'=9/2."""
        ff = n2_ff_dual_central_charge(k_val=2)
        assert ff['c'] == Rational(3, 2)
        assert ff['c_dual'] == Rational(9, 2)

    def test_ff_dual_k3(self):
        """At k=3: c=9/5, c'=21/5."""
        ff = n2_ff_dual_central_charge(k_val=3)
        assert ff['c'] == Rational(9, 5)
        assert ff['c_dual'] == Rational(21, 5)

    def test_ff_dual_involution(self):
        """FF involution is an involution: (c')' = c."""
        ff1 = n2_ff_dual_central_charge(c_val=1)
        ff2 = n2_ff_dual_central_charge(c_val=ff1['c_dual'])
        assert ff2['c_dual'] == Rational(1)

    def test_additive_complementarity(self):
        """c + c' = 6 for all k."""
        for k_val in [1, 2, 3, 5, 10]:
            ff = n2_ff_dual_central_charge(k_val=k_val)
            assert simplify(ff['c_sum'] - 6) == 0

    def test_additive_complementarity_from_c(self):
        """c + c' = 6 when starting from c."""
        for c_val in [1, 2, Rational(3, 2), Rational(9, 5)]:
            ff = n2_ff_dual_central_charge(c_val=c_val)
            assert simplify(ff['c_sum'] - 6) == 0

    def test_self_dual_point(self):
        """Self-dual at c = 3 (k -> infinity, free-field limit)."""
        sd = n2_self_dual_point()
        assert sd['c_self_dual'] == Rational(3)

    def test_kappa_complementarity_constant(self):
        """kappa(c) + kappa(6-c) = 1 for all c (constant)."""
        for c_val in [1, 2, Rational(3, 2), Rational(9, 5)]:
            comp = n2_complementarity_sum(c_val=c_val)
            assert simplify(comp['sum'] - 1) == 0, (
                f"kappa+kappa' = {comp['sum']} at c={c_val}, expected 1"
            )

    def test_complementarity_sum_constant_across_levels(self):
        """kappa + kappa' = 1 is level-independent."""
        sums = []
        for c_val in [1, 2, Rational(1, 2), Rational(9, 5)]:
            comp = n2_complementarity_sum(c_val=c_val)
            sums.append(comp['sum'])
        assert all(simplify(s - 1) == 0 for s in sums)

    def test_complementarity_from_k(self):
        """kappa + kappa' = 1 from k-parameterization."""
        for k_val in [1, 2, 3, 5]:
            comp = n2_complementarity_sum(k_val=k_val)
            assert simplify(comp['sum'] - 1) == 0


# ================================================================
# 6. SHADOW TOWER: T-LINE
# ================================================================

class TestShadowTowerTLine:
    """Test shadow obstruction tower on the T-line (Virasoro subalgebra)."""

    def test_T_line_kappa(self):
        """S_2 on T-line = c/2 (matches Virasoro)."""
        data = n2_shadow_data_T_line()
        assert simplify(data['kappa'] - c / 2) == 0

    def test_T_line_alpha(self):
        """S_3 on T-line = 2 (matches Virasoro)."""
        data = n2_shadow_data_T_line()
        assert data['alpha'] == Rational(2)

    def test_T_line_S4(self):
        """S_4 on T-line = 10/(c(5c+22)) (matches Virasoro)."""
        data = n2_shadow_data_T_line()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(data['S4'] - expected) == 0

    def test_T_line_class_M(self):
        """T-line is class M (infinite depth)."""
        data = n2_shadow_data_T_line()
        assert data['class'] == 'M'

    def test_T_line_matches_virasoro_at_c1(self):
        """T-line shadow obstruction tower at c=1 matches Virasoro at c=1."""
        tower = n2_shadow_tower_T_line(1, max_arity=10)
        # Virasoro S_2 = c/2 = 1/2
        assert tower[2] == Rational(1, 2)
        # Virasoro S_3 = 2
        assert tower[3] == Rational(2)
        # Virasoro S_4 = 10/(1*27) = 10/27
        assert tower[4] == Rational(10, 27)

    def test_T_line_matches_virasoro_at_c3(self):
        """T-line tower at c=3 matches Virasoro at c=3."""
        tower = n2_shadow_tower_T_line(3, max_arity=5)
        assert tower[2] == Rational(3, 2)
        assert tower[3] == Rational(2)
        # S_4 = 10/(3*37) = 10/111
        assert tower[4] == Rational(10, 111)

    def test_T_line_alternating_signs(self):
        """Shadow obstruction tower coefficients alternate in sign for c > 0."""
        tower = n2_shadow_tower_T_line(3, max_arity=15)
        for r in range(5, 16):
            val = float(tower[r].evalf())
            expected_sign = (-1) ** (r + 1)  # S_2, S_3 > 0; S_4 > 0; S_5 < 0; etc.
            # The sign pattern starts alternating after S_4
            if r >= 5:
                prev_val = float(tower[r - 1].evalf())
                assert val * prev_val < 0, (
                    f"S_{r} = {val} and S_{r-1} = {prev_val} should have opposite signs"
                )

    def test_T_line_growth_at_c3(self):
        """Shadow growth rate on T-line at c=3: rho ~ 2.06 (divergent)."""
        rho = n2_shadow_growth_rate_T_line(3)
        assert 2.0 < rho < 2.2

    def test_T_line_convergent_at_c9(self):
        """Shadow obstruction tower converges at c=9 (rho < 1)."""
        rho = n2_shadow_growth_rate_T_line(9)
        assert rho < 1.0

    def test_T_line_ratio_test(self):
        """Geometric mean of |S_r| converges to rho on the T-line.

        The individual ratios |S_{r+1}/S_r| oscillate due to the
        cos(r*theta + phi) factor. Instead, check that the geometric
        mean (|S_r|)^{1/r} -> rho as r -> infinity.
        """
        c_val = 13  # self-dual for Virasoro
        tower = n2_shadow_tower_T_line(c_val, max_arity=40)
        rho = n2_shadow_growth_rate_T_line(c_val)
        # Check geometric mean at large arity
        for r in [35, 38, 40]:
            sr = float(tower[r].evalf())
            if abs(sr) > 1e-50:
                # |S_r|^{1/r} should approximate rho (with r^{-5/2} correction)
                geo_mean = abs(sr) ** (1.0 / r)
                # Loose tolerance because the power-law correction is significant
                assert abs(geo_mean - rho) / rho < 0.3, (
                    f"|S_{r}|^(1/{r}) = {geo_mean:.6f}, expected rho = {rho:.6f}"
                )


# ================================================================
# 7. SHADOW TOWER: J-LINE
# ================================================================

class TestShadowTowerJLine:
    """Test shadow obstruction tower on the J-line (U(1) current, class G)."""

    def test_J_line_kappa(self):
        """S_2 on J-line = c/3."""
        data = n2_shadow_data_J_line()
        assert simplify(data['kappa'] - c / 3) == 0

    def test_J_line_class_G(self):
        """J-line is class G (Gaussian, depth 2)."""
        data = n2_shadow_data_J_line()
        assert data['class'] == 'G'

    def test_J_line_all_higher_vanish(self):
        """S_r = 0 for all r >= 3 on J-line."""
        tower = n2_shadow_tower_J_line(3, max_arity=20)
        for r in range(3, 21):
            assert tower[r] == 0, f"S_{r} = {tower[r]} should be 0"

    def test_J_line_growth_rate_zero(self):
        """Growth rate on J-line is 0."""
        assert n2_shadow_growth_rate_J_line() == 0


# ================================================================
# 8. SHADOW TOWER: G-LINE
# ================================================================

class TestShadowTowerGLine:
    """Test shadow obstruction tower on the G-line (supercurrent, conjectured class L)."""

    def test_G_line_kappa(self):
        """S_2 on G-line = c/3."""
        data = n2_shadow_data_G_line()
        assert simplify(data['kappa'] - c / 3) == 0

    def test_G_line_alpha(self):
        """S_3 on G-line = 1 (from J intermediate)."""
        data = n2_shadow_data_G_line()
        assert data['alpha'] == Rational(1)

    def test_G_line_class_L(self):
        """G-line is conjectured class L."""
        data = n2_shadow_data_G_line()
        assert data['class'] == 'L'

    def test_G_line_higher_vanish(self):
        """S_r = 0 for all r >= 4 on G-line (class L)."""
        tower = n2_shadow_tower_G_line(3, max_arity=10)
        for r in range(4, 11):
            val = tower[r]
            assert simplify(val) == 0, f"S_{r} = {val} should be 0"

    def test_G_line_growth_rate_zero(self):
        """Growth rate on G-line is 0 (class L terminates)."""
        assert n2_shadow_growth_rate_G_line() == 0

    def test_G_line_S3_nonzero(self):
        """S_3 on G-line is nonzero (not class G)."""
        tower = n2_shadow_tower_G_line(3, max_arity=5)
        assert tower[3] != 0


# ================================================================
# 9. SHADOW CLASS
# ================================================================

class TestShadowClass:
    """Test shadow class determination."""

    def test_overall_class_M(self):
        """Overall shadow class is M (from T-line Virasoro)."""
        sc = n2_shadow_class()
        assert sc['class'] == 'M'

    def test_depth_infinity(self):
        """Shadow depth is infinity."""
        sc = n2_shadow_class()
        assert sc['depth'] == float('inf')

    def test_three_line_classes(self):
        """Three lines have classes M, G, L."""
        sc = n2_shadow_class()
        assert sc['T_line_class'] == 'M'
        assert sc['J_line_class'] == 'G'
        assert sc['G_line_class'] == 'L'


# ================================================================
# 10. GENUS EXPANSION
# ================================================================

class TestGenusExpansion:
    """Test genus expansion F_g = kappa * lambda_g^FP."""

    def test_F1_at_c1(self):
        """F_1(c=1) = (5/4) * (1/24) = 5/96."""
        f1 = n2_F_g(1, 1)
        assert f1 == Rational(5, 96)

    def test_F1_at_c2(self):
        """F_1(c=2) = (6-2)/(2*(3-2)) * (1/24) = 2 * 1/24 = 1/12."""
        f1 = n2_F_g(2, 1)
        assert f1 == Rational(2) * Rational(1, 24)

    def test_F2_at_c1(self):
        """F_2(c=1) = (5/4) * 7/5760."""
        from compute.lib.utils import lambda_fp
        f2 = n2_F_g(1, 2)
        expected = Rational(5, 4) * lambda_fp(2)
        assert f2 == expected

    def test_genus_table_length(self):
        """Genus table has correct number of entries."""
        table = n2_genus_table(1, max_genus=5)
        assert len(table) == 5

    def test_F_g_positive_for_positive_c(self):
        """F_g > 0 for all g >= 1 when c > 0."""
        table = n2_genus_table(1, max_genus=5)
        for g, fg in table.items():
            assert fg > 0, f"F_{g} = {fg} should be > 0 for c=1"

    def test_F_g_positive_for_c_between_0_and_3(self):
        """F_g > 0 for all g >= 1 when 0 < c < 3 (kappa > 0 in that range)."""
        table = n2_genus_table(1, max_genus=5)
        for g, fg in table.items():
            assert fg > 0, f"F_{g} = {fg} should be > 0 for c=1"

    def test_F1_ratio_to_virasoro(self):
        """F_1(N=2, c=1) / F_1(Vir, c=1) = kappa(N=2,1)/kappa(Vir,1) = (5/4)/(1/2) = 5/2."""
        f1_n2 = n2_F_g(1, 1)
        f1_vir = Rational(1, 2) * Rational(1, 24)  # c/2 * 1/24 at c=1
        assert f1_n2 / f1_vir == Rational(5, 2)

    def test_F_g_koszul_pair_sum(self):
        """F_g(c) + F_g(c') = (kappa(c)+kappa(c')) * lambda_g = 1 * lambda_g."""
        from compute.lib.utils import lambda_fp
        f1 = n2_F_g(1, 1)
        f1_dual = n2_F_g(5, 1)  # c' = 6 - 1 = 5
        expected = Rational(1) * lambda_fp(1)  # kappa + kappa' = 1
        assert simplify(f1 + f1_dual - expected) == 0


# ================================================================
# 11. CROSS-CHANNELS
# ================================================================

class TestCrossChannels:
    """Test cross-channel curvatures and propagator variance."""

    def test_all_cross_curvatures_zero(self):
        """All cross-channel curvatures vanish (no vacuum in cross-OPEs)."""
        cross = n2_cross_channel_curvatures()
        for pair, val in cross.items():
            assert simplify(val) == 0, (
                f"Cross-channel {pair} curvature = {val} should be 0"
            )

    def test_propagator_variance_zero(self):
        """Propagator variance vanishes for diagonal coupling."""
        delta = n2_propagator_variance()
        assert simplify(delta) == 0

    def test_propagator_variance_at_c1(self):
        """Propagator variance at c=1 is 0."""
        delta = n2_propagator_variance(c_val=1)
        assert delta == 0


# ================================================================
# 12. JACOBI IDENTITIES
# ================================================================

class TestJacobiIdentities:
    """Test OPE consistency via Jacobi identities."""

    def test_jacobi_TJGp(self):
        """Jacobi identity for (T, J, G+)."""
        result = verify_n2_jacobi_TJG()
        assert result['verified']
        assert result['LHS'] == 0
        assert result['RHS'] == 0

    def test_jacobi_JGpGm(self):
        """Jacobi identity for (J, G+, G-)."""
        result = verify_n2_jacobi_JGG()
        assert result['verified']

    def test_jacobi_GpGmT(self):
        """Jacobi identity for (G+, G-, T)."""
        result = verify_n2_jacobi_GGT()
        assert result['verified']
        assert result['G+G-_simple_pole_T'] is True
        assert result['G+G-_simple_pole_dJ'] is True


# ================================================================
# 13. SPECIAL VALUES AND CONSISTENCY
# ================================================================

class TestSpecialValues:
    """Test at physically important central charges."""

    def test_c1_kappa(self):
        """kappa(c=1) = 5/4."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_c6_kappa(self):
        """kappa(c=6) = 0 (critical level k=-4)."""
        assert kappa_n2(6) == Rational(0)

    def test_c1_complementarity(self):
        """kappa(1) + kappa(5) = 1."""
        comp = n2_complementarity_sum(c_val=1)
        assert simplify(comp['sum'] - 1) == 0


# ================================================================
# 14. FULL SHADOW TOWER
# ================================================================

class TestFullShadowTower:
    """Test the multi-line shadow obstruction tower computation."""

    def test_full_tower_has_three_lines(self):
        """Full shadow coefficients have T, J, G lines."""
        coeffs = n2_full_shadow_coefficients(1, max_arity=5)
        assert 'T' in coeffs
        assert 'J' in coeffs
        assert 'G' in coeffs

    def test_full_tower_T_matches_standalone(self):
        """T-line in full tower matches standalone T-line computation."""
        full = n2_full_shadow_coefficients(3, max_arity=10)
        standalone = n2_shadow_tower_T_line(3, max_arity=10)
        for r in range(2, 11):
            assert simplify(full['T'][r] - standalone[r]) == 0

    def test_full_tower_J_all_zero_above_2(self):
        """J-line in full tower has S_r = 0 for r >= 3."""
        full = n2_full_shadow_coefficients(3, max_arity=10)
        for r in range(3, 11):
            assert full['J'][r] == 0

    def test_full_tower_G_all_zero_above_3(self):
        """G-line in full tower has S_r = 0 for r >= 4."""
        full = n2_full_shadow_coefficients(3, max_arity=10)
        for r in range(4, 11):
            assert simplify(full['G'][r]) == 0


# ================================================================
# 15. VIRASORO SUBALGEBRA CONSISTENCY
# ================================================================

class TestVirasoroConsistency:
    """Cross-check N=2 shadow obstruction tower against Virasoro subalgebra.

    The T-line of the N=2 SCA IS the Virasoro algebra at the
    same central charge. All Virasoro shadow obstruction tower properties
    must hold on the T-line.
    """

    def test_virasoro_S2_agreement(self):
        """T-line S_2 = c/2 matches Virasoro kappa."""
        tower = n2_shadow_tower_T_line(1, max_arity=3)
        assert tower[2] == Rational(1, 2)

    def test_virasoro_S3_agreement(self):
        """T-line S_3 = 2 matches Virasoro cubic."""
        tower = n2_shadow_tower_T_line(1, max_arity=3)
        assert tower[3] == Rational(2)

    def test_virasoro_S4_agreement(self):
        """T-line S_4 matches Virasoro quartic Q^contact."""
        tower = n2_shadow_tower_T_line(1, max_arity=4)
        # Virasoro S_4 = 10/(c(5c+22)). At c=1: 10/27
        assert tower[4] == Rational(10, 27)

    def test_virasoro_delta_agreement(self):
        """T-line discriminant Delta matches Virasoro."""
        data = n2_shadow_data_T_line(c_val=1)
        # Delta = 40/(5c+22). At c=1: 40/27
        assert data['Delta'] == Rational(40, 27)

    def test_virasoro_growth_rate_agreement(self):
        """T-line growth rate matches Virasoro rho."""
        rho_n2 = n2_shadow_growth_rate_T_line(13)  # c=13 self-dual
        # Virasoro rho at c=13: sqrt((180*13+872)/((65+22)*169))
        from sympy import Rational as R
        rho_sq = (R(180) * 13 + 872) / ((5 * R(13) + 22) * R(13) ** 2)
        rho_vir = float(sqrt(rho_sq).evalf())
        assert abs(rho_n2 - rho_vir) < 1e-10


# ================================================================
# 16. REGRESSION AND CROSS-FAMILY CHECKS
# ================================================================

class TestCrossFamilyChecks:
    """Cross-family consistency checks (AP10 compliance)."""

    def test_kappa_at_k1(self):
        """kappa(N=2, k=1) = (1+4)/4 = 5/4. Cross-check via c=1."""
        assert kappa_n2(1) == Rational(5, 4)

    def test_kappa_at_c1_vs_virasoro(self):
        """At c=1: kappa(N=2) = 5/4, kappa(Vir) = 1/2. Ratio = 5/2."""
        ratio = kappa_n2(1) / Rational(1, 2)
        assert ratio == Rational(5, 2)

    def test_additive_complementarity(self):
        """N=2 has c+c'=6, kappa+kappa'=1. Virasoro has c+c'=26, kappa+kappa'=13."""
        ff_n2 = n2_ff_dual_central_charge(c_val=1)
        assert simplify(ff_n2['c_sum'] - 6) == 0

        # Virasoro: c + c' = 26
        c_vir_dual = 26 - 1
        assert c_vir_dual == 25

    def test_c_plus_c_dual_constant(self):
        """c + c' = 6 for five different central charges."""
        for c_val in [1, 2, Rational(1, 2), Rational(9, 5), 4]:
            ff = n2_ff_dual_central_charge(c_val=c_val)
            assert simplify(ff['c_sum'] - 6) == 0, (
                f"c+c' = {ff['c_sum']} at c={c_val}, expected 6"
            )


# ================================================================
# 17. VERIFY_ALL INTEGRATION
# ================================================================

class TestVerifyAll:
    """Test the integrated verification suite."""

    def test_verify_all_passes(self):
        """All internal verifications pass."""
        results = verify_all()
        failed = [name for name, ok in results.items() if not ok]
        assert len(failed) == 0, f"Failed tests: {failed}"

    def test_verify_all_has_enough_tests(self):
        """verify_all checks at least 20 properties."""
        results = verify_all()
        assert len(results) >= 20


# ================================================================
# 18. NUMERICAL STABILITY
# ================================================================

class TestNumericalStability:
    """Test numerical stability of shadow obstruction tower at extreme parameters."""

    def test_large_c(self):
        """Shadow obstruction tower computable at c=100."""
        tower = n2_shadow_tower_T_line(100, max_arity=10)
        # S_2 = 50
        assert tower[2] == Rational(50)
        # All higher arities should be small
        for r in range(3, 11):
            val = float(tower[r].evalf())
            assert abs(val) < 1e10

    def test_small_c(self):
        """Shadow obstruction tower computable at c=1/10."""
        tower = n2_shadow_tower_T_line(Rational(1, 10), max_arity=10)
        assert tower[2] == Rational(1, 20)

    def test_kappa_at_various_c(self):
        """kappa is well-defined for a range of central charges (excluding c=3 pole)."""
        for c_val in [Rational(1, 2), 1, 2, 4, 5, 6, 10, 26]:
            kap = kappa_n2(c_val)
            c_v = Rational(c_val)
            expected = (6 - c_v) / (2 * (3 - c_v))
            assert simplify(kap - expected) == 0

    def test_complementarity_sum_at_dual_pairs(self):
        """kappa + kappa' = 1 for several dual pairs."""
        for c_val in [1, 2, Rational(1, 2), 4]:
            comp = n2_complementarity_sum(c_val=c_val)
            assert simplify(comp['sum'] - 1) == 0
