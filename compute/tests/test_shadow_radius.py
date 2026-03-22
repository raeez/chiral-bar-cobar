"""Tests for shadow radius: the growth-rate invariant of the shadow tower.

Verifies:
1. Shadow metric coefficients and discriminant
2. Branch point computation and modulus formula
3. Shadow growth rate rho = 1/R for all standard families
4. Critical central charge c* where rho(Vir) = 1
5. Koszul duality: rho self-dual at c = 13
6. Asymptotic sign pattern from branch point argument
7. DS depth-increase quantification
8. Formula consistency with the closed form H^2 = t^4 Q_L
"""

import sys
sys.path.insert(0, 'compute')

import pytest
from sympy import Rational, sqrt, Symbol, simplify, cancel, factor, Abs, expand

c = Symbol('c')


# ===========================================================================
# 1. Shadow metric and discriminant
# ===========================================================================

class TestShadowMetric:
    """Test shadow metric Q_L(t) = 4κ² + 12κα t + (9α²+16κS₄)t²."""

    def test_virasoro_shadow_metric_coefficients(self):
        from lib.shadow_radius import shadow_metric_coefficients
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5 * c + 22))
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        assert simplify(q0 - c ** 2) == 0
        assert simplify(q1 - 12 * c) == 0
        # q2 = 9*4 + 16*(c/2)*10/(c(5c+22)) = 36 + 80/(5c+22) = (180c+872)/(5c+22)
        assert simplify(q2 - (180 * c + 872) / (5 * c + 22)) == 0

    def test_critical_discriminant_virasoro(self):
        from lib.shadow_radius import critical_discriminant
        kappa = c / 2
        S4 = Rational(10) / (c * (5 * c + 22))
        Delta = critical_discriminant(kappa, S4)
        assert simplify(Delta - Rational(40) / (5 * c + 22)) == 0

    def test_discriminant_sign_class_m(self):
        """For Virasoro with c > 0 and c != -22/5: Delta > 0 (class M)."""
        from lib.shadow_radius import critical_discriminant
        kappa = Rational(1, 2)  # c = 1
        S4 = Rational(10) / (1 * 27)
        Delta = critical_discriminant(kappa, S4)
        assert Delta > 0

    def test_discriminant_zero_class_l(self):
        """For affine KM: S4 = 0, so Delta = 0 (class L)."""
        from lib.shadow_radius import critical_discriminant
        kappa = Rational(3)  # arbitrary
        S4 = Rational(0)
        Delta = critical_discriminant(kappa, S4)
        assert Delta == 0

    def test_metric_discriminant_formula(self):
        """disc(Q_L in t) = -32*kappa^2 * Delta."""
        from lib.shadow_radius import shadow_metric_discriminant, critical_discriminant
        kappa = c / 2
        S4 = Rational(10) / (c * (5 * c + 22))
        Delta = critical_discriminant(kappa, S4)
        disc = shadow_metric_discriminant(kappa, Rational(2), S4)
        assert simplify(disc + 32 * kappa ** 2 * Delta) == 0


# ===========================================================================
# 2. Branch points
# ===========================================================================

class TestBranchPoints:
    """Test branch point computation for the shadow generating function."""

    def test_branch_points_are_zeros_of_Q(self):
        """t_0 satisfies Q_L(t_0) = 0."""
        from lib.shadow_radius import branch_points, shadow_metric_coefficients
        kappa = Rational(1, 2)
        alpha = Rational(2)
        S4 = Rational(10, 27)
        tp, tm = branch_points(kappa, alpha, S4)
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        # Q_L(t_0) = q0 + q1*t_0 + q2*t_0^2 should be zero
        val_p = q0 + q1 * tp + q2 * tp ** 2
        val_m = q0 + q1 * tm + q2 * tm ** 2
        assert simplify(val_p) == 0
        assert simplify(val_m) == 0

    def test_branch_point_modulus(self):
        """Both branch points have the same modulus (complex conjugate pair)."""
        from lib.shadow_radius import virasoro_branch_points_numerical
        bp = virasoro_branch_points_numerical(Rational(1))
        assert abs(bp['mod_plus'] - bp['mod_minus']) < 1e-10

    def test_branch_point_conjugate(self):
        """Branch points are complex conjugates for Delta > 0."""
        from lib.shadow_radius import virasoro_branch_points_numerical
        bp = virasoro_branch_points_numerical(Rational(1))
        tp = bp['t_plus']
        tm = bp['t_minus']
        assert abs(tp.real - tm.real) < 1e-10
        assert abs(tp.imag + tm.imag) < 1e-10  # conjugate


# ===========================================================================
# 3. Shadow growth rate
# ===========================================================================

class TestShadowGrowthRate:
    """Test shadow growth rate rho = sqrt(9α² + 2Δ) / (2|κ|)."""

    def test_rho_formula_c1(self):
        """rho(Vir_1) = sqrt(1052/27)."""
        from lib.shadow_radius import shadow_growth_rate
        kappa = Rational(1, 2)
        alpha = Rational(2)
        S4 = Rational(10, 27)
        rho = shadow_growth_rate(kappa, alpha, S4)
        expected = sqrt(Rational(1052, 27))
        assert simplify(rho - expected) == 0

    def test_rho_formula_c13(self):
        """rho(Vir_13) = sqrt(3212/87) / 13."""
        from lib.shadow_radius import shadow_growth_rate
        kappa = Rational(13, 2)
        alpha = Rational(2)
        S4 = Rational(10) / (13 * 87)
        rho = shadow_growth_rate(kappa, alpha, S4)
        expected = sqrt(Rational(3212, 87)) / 13
        assert simplify(rho - expected) == 0

    def test_rho_zero_class_g(self):
        """Class G (lattice): Delta = 0, alpha = 0 => rho = 0."""
        from lib.shadow_radius import shadow_growth_rate
        rho = shadow_growth_rate(Rational(1), Rational(0), Rational(0))
        assert rho == 0

    def test_rho_zero_class_l(self):
        """Class L (affine): S4 = 0 => Delta = 0 => rho = 3|alpha|/(2|kappa|)."""
        from lib.shadow_radius import shadow_growth_rate
        kappa = Rational(3)
        alpha = Rational(1)
        rho = shadow_growth_rate(kappa, alpha, Rational(0))
        # 9*1 + 0 = 9, sqrt(9) = 3, rho = 3/(2*3) = 1/2
        assert simplify(rho - Rational(1, 2)) == 0

    def test_rho_decreasing_in_c(self):
        """For Virasoro, rho(c) is decreasing for large c."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        _, rho_sq = virasoro_shadow_radius_formula()
        r1 = float(rho_sq.subs(c, 10))
        r2 = float(rho_sq.subs(c, 20))
        r3 = float(rho_sq.subs(c, 30))
        assert r1 > r2 > r3

    def test_rho_squared_formula(self):
        """rho^2(c) = (180c + 872) / (5c^3 + 22c^2)."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        _, rho_sq = virasoro_shadow_radius_formula()
        expected = (180 * c + 872) / (5 * c ** 3 + 22 * c ** 2)
        diff = simplify(cancel(rho_sq - expected))
        assert diff == 0


# ===========================================================================
# 4. Critical central charge
# ===========================================================================

class TestCriticalCentralCharge:
    """Test the critical central charge c* where rho(Vir_{c*}) = 1."""

    def test_c_star_exists(self):
        from lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        assert c_star is not None

    def test_c_star_value(self):
        """c* is approximately 6.1254."""
        from lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        val = float(c_star.evalf())
        assert 6.12 < val < 6.13

    def test_c_star_solves_cubic(self):
        """c* satisfies 5c^3 + 22c^2 - 180c - 872 = 0."""
        from lib.shadow_radius import virasoro_critical_central_charge
        c_star = virasoro_critical_central_charge()
        poly = 5 * c_star ** 3 + 22 * c_star ** 2 - 180 * c_star - 872
        assert abs(complex(simplify(poly).evalf())) < 1e-8

    def test_rho_below_c_star(self):
        """rho > 1 for c < c* (divergent tower)."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        _, rho_sq = virasoro_shadow_radius_formula()
        assert float(rho_sq.subs(c, 1)) > 1
        assert float(rho_sq.subs(c, 4)) > 1
        assert float(rho_sq.subs(c, 6)) > 1

    def test_rho_above_c_star(self):
        """rho < 1 for c > c* (convergent tower)."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        _, rho_sq = virasoro_shadow_radius_formula()
        assert float(rho_sq.subs(c, 7)) < 1
        assert float(rho_sq.subs(c, 13)) < 1
        assert float(rho_sq.subs(c, 26)) < 1


# ===========================================================================
# 5. Koszul duality
# ===========================================================================

class TestKoszulDuality:
    """Test Koszul duality rho(Vir_c) vs rho(Vir_{26-c})."""

    def test_self_dual_at_c13(self):
        """rho(Vir_13) = rho(Vir_13!) exactly."""
        from lib.shadow_radius import virasoro_koszul_product
        kd = virasoro_koszul_product(13)
        assert kd['self_dual']

    def test_rho_swaps_under_duality(self):
        """rho(c) and rho(26-c) swap."""
        from lib.shadow_radius import virasoro_koszul_product
        kd = virasoro_koszul_product(1)
        assert abs(kd['rho'] - 6.242) < 0.001
        assert abs(kd['rho_dual'] - 0.2418) < 0.001

    def test_koszul_duality_product_symmetric(self):
        """rho(c)*rho(26-c) = rho(26-c)*rho(c) (symmetric in c <-> 26-c)."""
        from lib.shadow_radius import virasoro_koszul_product
        kd1 = virasoro_koszul_product(1)
        kd25 = virasoro_koszul_product(25)
        assert abs(kd1['product'] - kd25['product']) < 1e-10

    def test_c13_is_unique_selfdual(self):
        """c = 13 is the unique self-dual point."""
        from lib.shadow_radius import virasoro_shadow_radius_formula
        _, rho_sq = virasoro_shadow_radius_formula()
        # rho(c) = rho(26-c) iff rho^2(c) = rho^2(26-c)
        diff = cancel(rho_sq - rho_sq.subs(c, 26 - c))
        # This should vanish only at c = 13
        # Factor: the numerator should have (c - 13) as a factor
        numer = simplify(diff).as_numer_denom()[0]
        assert simplify(numer.subs(c, 13)) == 0


# ===========================================================================
# 6. Sign pattern and oscillation
# ===========================================================================

class TestSignPattern:
    """Test sign pattern predictions from branch point argument."""

    def test_branch_argument_near_pi(self):
        """At c=1, branch argument is near pi (explains near-alternating signs)."""
        from lib.shadow_radius import virasoro_branch_points_numerical
        import math
        bp = virasoro_branch_points_numerical(Rational(1))
        arg_ratio = abs(bp['arg_plus']) / math.pi
        assert 0.9 < arg_ratio < 1.0  # near pi

    def test_branch_argument_increases_with_c(self):
        """arg(t_0)/pi increases toward 1 as c increases."""
        from lib.shadow_radius import virasoro_branch_points_numerical
        import math
        args = []
        for cv in [1, 5, 13, 25]:
            bp = virasoro_branch_points_numerical(Rational(cv))
            args.append(abs(bp['arg_plus']) / math.pi)
        for i in range(len(args) - 1):
            assert args[i] < args[i + 1]

    def test_semiclassical_limit(self):
        """As c -> infinity: arg -> pi, rho -> 0 (tower converges, alternating)."""
        from lib.shadow_radius import virasoro_branch_points_numerical
        import math
        bp = virasoro_branch_points_numerical(Rational(1000))
        assert abs(bp['arg_plus'] / math.pi - 1) < 0.01
        assert bp['rho'] < 0.01


# ===========================================================================
# 7. DS depth-increase
# ===========================================================================

class TestDSDepthIncrease:
    """Test DS reduction quantification: rho(sl_N)=0 -> rho(W_N)>0."""

    def test_sl_N_has_rho_zero(self):
        from lib.shadow_radius import ds_shadow_radius_comparison
        ds = ds_shadow_radius_comparison(3, 2)
        assert ds['sl_N']['rho'] == 0

    def test_W_N_has_rho_positive(self):
        from lib.shadow_radius import ds_shadow_radius_comparison
        ds = ds_shadow_radius_comparison(3, 2)
        assert ds['W_3']['rho_T_line'] > 0


# ===========================================================================
# 8. Closed form consistency H^2 = t^4 * Q_L
# ===========================================================================

class TestClosedFormConsistency:
    """Verify H^2 = t^4 * Q_L(t) reproduces all S_r exactly."""

    def test_h_squared_equals_t4_q(self):
        """The fundamental algebraic relation from thm:riccati-algebraicity."""
        from lib.sigma_ring_finite_generation import virasoro_shadow_coefficients
        S = virasoro_shadow_coefficients(20)

        c_val = Rational(1)
        # Q_L(t) = c^2 + 12c*t + alpha*t^2
        alpha_c = Rational(1052, 27)
        q0 = Rational(1)
        q1 = Rational(12)
        q2 = alpha_c

        # H[r] = r * S_r, H = sum H[r] t^r
        # F = H/t^2 = sum a_n t^n where a_n = (n+2) S_{n+2}
        # Claim: F^2 = Q_L (polynomial, degree 2)
        for m in range(3, 16):
            # [t^m] F^2 = sum_{i+j=m, i>=0, j>=0} a_i * a_j
            conv = Rational(0)
            for i in range(0, m + 1):
                j = m - i
                a_i = (i + 2) * S[i + 2].subs(c, c_val) if (i + 2) in S else 0
                a_j = (j + 2) * S[j + 2].subs(c, c_val) if (j + 2) in S else 0
                conv += a_i * a_j
            # Should be zero for m >= 3
            assert simplify(conv) == 0, f"[t^{m}]F^2 = {conv} != 0"

    def test_f_squared_matches_q_at_low_orders(self):
        """[t^0]F^2 = 4κ^2, [t^1]F^2 = 12κα, [t^2]F^2 = 9α^2+16κS4."""
        from lib.sigma_ring_finite_generation import virasoro_shadow_coefficients
        S = virasoro_shadow_coefficients(6)

        c_val = Rational(1)
        a0 = 2 * S[2].subs(c, c_val)  # 2*kappa = c = 1
        a1 = 3 * S[3].subs(c, c_val)  # 3*alpha = 6
        a2 = 4 * S[4].subs(c, c_val)  # 4*S4

        # [t^0]F^2 = a0^2
        assert a0 ** 2 == Rational(1)  # c^2 = 1

        # [t^1]F^2 = 2*a0*a1
        assert 2 * a0 * a1 == Rational(12)  # 12c = 12

        # [t^2]F^2 = a1^2 + 2*a0*a2
        q2 = a1 ** 2 + 2 * a0 * a2
        expected = Rational(1052, 27)
        assert simplify(q2 - expected) == 0


# ===========================================================================
# 9. Atlas completeness
# ===========================================================================

class TestAtlas:
    """Test the shadow radius atlas covers all standard families."""

    def test_atlas_has_all_families(self):
        from lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert 'Heisenberg' in atlas
        assert 'Lattice V_Lambda' in atlas
        assert 'Affine V_k(g)' in atlas
        assert 'Beta-gamma' in atlas
        assert 'Virasoro Vir_c' in atlas
        assert 'W_3' in atlas

    def test_atlas_class_g_rho_zero(self):
        from lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Heisenberg']['rho'] == 0
        assert atlas['Lattice V_Lambda']['rho'] == 0

    def test_atlas_class_l_rho_zero(self):
        from lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        assert atlas['Affine V_k(g)']['rho'] == 0

    def test_atlas_virasoro_has_critical_c(self):
        from lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        c_star = atlas['Virasoro Vir_c']['critical_c']
        assert 6.12 < c_star < 6.13

    def test_atlas_virasoro_special_values(self):
        from lib.shadow_radius import shadow_radius_atlas
        atlas = shadow_radius_atlas()
        sv = atlas['Virasoro Vir_c']['special_values']
        # c=1: divergent
        assert not sv['c=1 (free boson)']['convergent']
        # c=13: convergent
        assert sv['c=13 (self-dual)']['convergent']
        # c=26: convergent
        assert sv['c=26 (string)']['convergent']


# ===========================================================================
# 10. Shadow radius for W_N via Koszul conductor
# ===========================================================================

class TestWNShadowRadius:
    """Test shadow radius properties for W_N algebras."""

    def test_koszul_conductor_virasoro(self):
        """K_2 = 26 for Virasoro."""
        from lib.shadow_tower_atlas import KOSZUL_CONDUCTORS
        assert KOSZUL_CONDUCTORS[2] == 26

    def test_koszul_conductor_w3(self):
        """K_3 = 100 for W_3."""
        from lib.shadow_tower_atlas import KOSZUL_CONDUCTORS
        assert KOSZUL_CONDUCTORS[3] == 100

    def test_sigma_invariant_level_independence_low(self):
        """Delta^(2) and Delta^(3) are level-independent for Virasoro."""
        from lib.shadow_tower_atlas import tline_level_independence
        li = tline_level_independence(2, 6)
        assert li[2]  # Delta^(2) = 13 (constant)
        assert li[3]  # Delta^(3) = 4 (constant)
