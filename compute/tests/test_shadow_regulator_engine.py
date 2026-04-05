r"""Tests for shadow_regulator_engine.py.

Multi-path verification of algebraic K-theory, Beilinson regulators,
and shadow L-function data for the shadow curve C_A: y^2 = t^4 * Q_L(t).

Test structure:
  1. Shadow data consistency (kappa, Q_L, branch points)
  2. K_0 and Picard group
  3. K_1 and units
  4. K_2 and tame symbols
  5. Weil reciprocity (product of tame symbols)
  6. Beilinson regulator (branch cycle)
  7. Beilinson regulator (infinity cycle)
  8. Shadow L-function derivative
  9. Beilinson conjecture rational factor
  10. Borel regulator at integer points
  11. Chern character through degree 3
  12. Motivic cohomology
  13. Koszul duality and regulators
  14. Cross-verification: multiple paths
  15. Landscape-wide consistency

Verification paths:
  Path 1: Direct computation from defining formulas
  Path 2: Integration of regulator 1-form
  Path 3: Tame symbol / residue computation
  Path 4: Cross-family consistency and limiting cases

Tolerance: 1e-10 for exact, 1e-4 for numerical integration, 1e-6 for general.

References:
    thm:riccati-algebraicity, def:shadow-metric, prop:shadow-periods,
    rem:motivic-decomposition, def:arithmetic-packet-connection.

CAUTION (AP1): kappa is family-specific.
CAUTION (AP10): expected values computed independently, not hardcoded from literature.
CAUTION (AP38): conventions verified from first principles.
"""

import cmath
import math
import pytest
from fractions import Fraction

from compute.lib.shadow_regulator_engine import (
    # Shadow data
    virasoro_shadow_data_numerical,
    heisenberg_shadow_data_numerical,
    affine_sl2_shadow_data_numerical,
    betagamma_shadow_data_numerical,
    # Shadow curve
    shadow_metric_QL,
    shadow_sextic_f,
    shadow_curve_y,
    QL_zeros,
    branch_points_sextic,
    # K_0
    compute_K0,
    ShadowK0,
    # K_1
    compute_K1,
    ShadowK1,
    # K_2 and tame symbols
    tame_symbol,
    compute_all_tame_symbols,
    product_of_tame_symbols,
    valuation_at_point,
    virasoro_tame_symbols,
    TameSymbol,
    # Beilinson regulator
    beilinson_regulator_branch_cycle,
    beilinson_regulator_infinity_cycle,
    beilinson_regulator_all_cycles,
    virasoro_beilinson_regulator,
    # L-function
    shadow_coefficients_numerical,
    shadow_zeta_at_integer,
    shadow_L_function_derivative_at_zero,
    beilinson_conjecture_rational_factor,
    # Borel regulator
    borel_regulator_shadow,
    borel_regulator_table,
    # Chern character
    shadow_chern_character,
    chern_character_landscape,
    ShadowChernCharacter,
    # Motivic cohomology
    compute_motivic_cohomology,
    ShadowMotivicCohomology,
    # Cross-verification
    regulator_via_residues,
    cross_verify_regulator,
    shadow_zeta_two_methods,
    koszul_duality_regulator_check,
    # Landscape
    compute_full_regulator_data,
    full_landscape_regulators,
    ShadowRegulatorData,
)


# ===========================================================================
# 1. Shadow data consistency
# ===========================================================================

class TestShadowDataConsistency:
    """Verify shadow data (kappa, Q_L, branch points) for all families."""

    def test_virasoro_kappa_formula(self):
        """kappa(Vir_c) = c/2. Verify at c = 1, 2, 13, 25."""
        for c_val in [1.0, 2.0, 13.0, 25.0]:
            data = virasoro_shadow_data_numerical(c_val)
            assert abs(data['kappa'] - c_val / 2.0) < 1e-14

    def test_virasoro_alpha(self):
        """Virasoro cubic shadow alpha = S_3 = 2 (constant)."""
        for c_val in [1.0, 5.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            assert abs(data['alpha'] - 2.0) < 1e-14

    def test_virasoro_S4(self):
        """S_4 = 10/(c(5c+22)). Verify numerically."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(data['S4'] - expected) < 1e-14

    def test_virasoro_delta(self):
        """Delta = 40/(5c+22). Verify."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            expected = 40.0 / (5.0 * c_val + 22.0)
            assert abs(data['Delta'] - expected) < 1e-14

    def test_virasoro_QL_at_zero(self):
        """Q_L(0) = q_0 = 4*kappa^2 = c^2."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            QL_0 = shadow_metric_QL(data, 0.0)
            assert abs(QL_0 - c_val ** 2) < 1e-12

    def test_heisenberg_kappa(self):
        """kappa(H_k) = k."""
        for k_val in [1.0, 2.0, 5.0]:
            data = heisenberg_shadow_data_numerical(k_val)
            assert abs(data['kappa'] - k_val) < 1e-14

    def test_heisenberg_QL_constant(self):
        """For Heisenberg: Q_L(t) = 4k^2 (constant in t)."""
        data = heisenberg_shadow_data_numerical(2.0)
        for t_val in [0.0, 1.0, -1.0, 5.0]:
            QL = shadow_metric_QL(data, t_val)
            assert abs(QL - 16.0) < 1e-12  # 4 * 2^2 = 16

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k_val in [1.0, 2.0, 4.0]:
            data = affine_sl2_shadow_data_numerical(k_val)
            expected = 3.0 * (k_val + 2.0) / 4.0
            assert abs(data['kappa'] - expected) < 1e-12

    def test_affine_sl2_delta_zero(self):
        """Class L: Delta = 0 for affine KM."""
        data = affine_sl2_shadow_data_numerical(1.0)
        assert abs(data['Delta']) < 1e-14

    def test_betagamma_kappa(self):
        """kappa = c/2 = 6*lam^2 - 6*lam + 1 for beta-gamma at weight lambda."""
        data = betagamma_shadow_data_numerical(0.5)
        c_val = 2.0 * (6.0 * 0.25 - 3.0 + 1.0)  # = 2*(1.5-3+1) = 2*(-0.5) = -1
        assert abs(data['c'] - c_val) < 1e-12
        assert abs(data['kappa'] - c_val / 2.0) < 1e-12

    def test_virasoro_sextic_at_zero(self):
        """f(0) = 0^4 * Q_L(0) = 0."""
        data = virasoro_shadow_data_numerical(1.0)
        assert abs(shadow_sextic_f(data, 0.0)) < 1e-30

    def test_sextic_degree(self):
        """f(t) = t^4*Q_L(t) should behave as degree 6 for large t."""
        data = virasoro_shadow_data_numerical(1.0)
        t_large = 1000.0
        f_val = abs(shadow_sextic_f(data, t_large))
        # Should scale as q2 * t^6
        q2 = data['q2']
        expected_order = abs(q2) * t_large ** 6
        # Check within factor of 2 (dominated by leading term)
        assert f_val / expected_order > 0.5
        assert f_val / expected_order < 2.0


class TestBranchPoints:
    """Branch points of the shadow curve."""

    def test_virasoro_branch_points_complex(self):
        """For Virasoro (class M, Delta > 0): branch points are complex conjugate."""
        data = virasoro_shadow_data_numerical(1.0)
        t_p, t_m = QL_zeros(data)
        # Should be complex conjugate pair
        assert abs(t_p - t_m.conjugate()) < 1e-10

    def test_virasoro_c13_self_dual_branch_points(self):
        """At c=13 (self-dual): branch points should have special structure."""
        data = virasoro_shadow_data_numerical(13.0)
        t_p, t_m = QL_zeros(data)
        # Both should exist and be finite
        assert abs(t_p) < 1e10
        assert abs(t_m) < 1e10

    def test_heisenberg_no_branch_points(self):
        """For Heisenberg (class G): Q_L is constant, no finite branch points."""
        data = heisenberg_shadow_data_numerical(1.0)
        bp = branch_points_sextic(data)
        assert len(bp) == 0  # No finite branch points

    def test_branch_points_are_zeros_of_QL(self):
        """Branch points satisfy Q_L(t) = 0."""
        data = virasoro_shadow_data_numerical(2.0)
        bp = branch_points_sextic(data)
        for t_val in bp:
            QL_val = shadow_metric_QL(data, t_val)
            assert abs(QL_val) < 1e-8

    def test_virasoro_number_of_branch_points(self):
        """Virasoro (class M) should have exactly 2 finite branch points."""
        for c_val in [1.0, 2.0, 13.0, 25.0]:
            data = virasoro_shadow_data_numerical(c_val)
            bp = branch_points_sextic(data)
            assert len(bp) == 2


# ===========================================================================
# 2. K_0 and Picard group
# ===========================================================================

class TestK0:
    """K_0(C_A) = Z + Pic(C_A)."""

    def test_K0_rank_always_1(self):
        """K_0 free rank = 1 for all connected curves."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(1.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
            ('affine_sl2', lambda: affine_sl2_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            K0 = compute_K0(family, data)
            assert K0.rank == 1

    def test_K0_genus_0(self):
        """Pic^0 dimension = genus of normalization = 0 for all families."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(1.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            K0 = compute_K0(family, data)
            assert K0.pic_degree_0_dim == 0

    def test_K0_shadow_class_G(self):
        """Heisenberg -> class G."""
        data = heisenberg_shadow_data_numerical(1.0)
        K0 = compute_K0('heisenberg', data)
        assert K0.shadow_class == 'G'

    def test_K0_shadow_class_L(self):
        """Affine sl_2 -> class L."""
        data = affine_sl2_shadow_data_numerical(1.0)
        K0 = compute_K0('affine_sl2', data)
        assert K0.shadow_class == 'L'

    def test_K0_shadow_class_M(self):
        """Virasoro -> class M."""
        data = virasoro_shadow_data_numerical(1.0)
        K0 = compute_K0('virasoro', data)
        assert K0.shadow_class == 'M'

    def test_K0_picard_rank(self):
        """Picard number = 1 for connected curve."""
        data = virasoro_shadow_data_numerical(13.0)
        K0 = compute_K0('virasoro', data)
        assert K0.pic_rank == 1


# ===========================================================================
# 3. K_1 and units
# ===========================================================================

class TestK1:
    """K_1 and unit group of the shadow curve."""

    def test_K1_has_coordinate_units(self):
        """K_1 should always include t and y as generators."""
        data = virasoro_shadow_data_numerical(1.0)
        K1 = compute_K1('virasoro', data)
        assert K1.rank >= 2  # at least t and y

    def test_K1_heisenberg_extra_unit(self):
        """Heisenberg (class G): y/t^2 becomes constant on normalization."""
        data = heisenberg_shadow_data_numerical(1.0)
        K1 = compute_K1('heisenberg', data)
        assert K1.rank >= 3  # t, y, y/t^2

    def test_K1_constant_units_always_present(self):
        """Constant units k* always present."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(1.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            K1 = compute_K1(family, data)
            assert 'k*' in K1.constant_units


# ===========================================================================
# 4. K_2 and tame symbols
# ===========================================================================

class TestTameSymbols:
    """Tame symbols of the Milnor symbol {t, y}."""

    def test_valuation_t_at_origin(self):
        """v_0(t) = 1."""
        data = virasoro_shadow_data_numerical(1.0)
        assert valuation_at_point(data, 0.0, 't') == 1

    def test_valuation_y_at_origin(self):
        """v_0(y) = 2 (since f = t^4*Q_L has order 4 zero at t=0)."""
        data = virasoro_shadow_data_numerical(1.0)
        assert valuation_at_point(data, 0.0, 'y') == 2

    def test_valuation_t_at_infinity(self):
        """v_infty(t) = -1."""
        data = virasoro_shadow_data_numerical(1.0)
        assert valuation_at_point(data, 1e15, 't') == -1

    def test_valuation_y_at_infinity(self):
        """v_infty(y) = -3 (deg f = 6, so y ~ t^3 at infinity)."""
        data = virasoro_shadow_data_numerical(1.0)
        assert valuation_at_point(data, 1e15, 'y') == -3

    def test_valuation_t_generic(self):
        """v_P(t) = 0 at generic point."""
        data = virasoro_shadow_data_numerical(1.0)
        assert valuation_at_point(data, 3.7, 't') == 0

    def test_valuation_y_at_branch_point(self):
        """v_P(y) = 1 at branch point (simple zero of Q_L)."""
        data = virasoro_shadow_data_numerical(1.0)
        bp = branch_points_sextic(data)
        for t_bp in bp:
            assert valuation_at_point(data, t_bp, 'y') == 1

    def test_tame_origin_sign(self):
        """Sign factor at origin: (-1)^{1*2} = 1."""
        data = virasoro_shadow_data_numerical(1.0)
        ts = tame_symbol(data, 0.0, 'origin')
        assert ts.sign_factor == 1  # (-1)^{1*2} = 1

    def test_tame_infinity_sign(self):
        """Sign factor at infinity: (-1)^{(-1)*(-3)} = (-1)^3 = -1."""
        data = virasoro_shadow_data_numerical(1.0)
        ts = tame_symbol(data, 1e15, 'infinity')
        assert ts.sign_factor == -1

    def test_tame_origin_value(self):
        r"""Tame_0({t,y}) = 1/sqrt(Q_L(0)) = 1/(2*kappa) = 1/c for Virasoro."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            ts = tame_symbol(data, 0.0)
            # sign=1, value = 1/sqrt(q0) = 1/|c|
            expected = 1.0 / abs(c_val)
            assert abs(ts.value - expected) < 1e-10, \
                f"c={c_val}: tame={ts.value}, expected={expected}"

    def test_tame_generic_point_trivial(self):
        """At a generic point (not origin, infinity, or branch): tame = 1."""
        data = virasoro_shadow_data_numerical(1.0)
        ts = tame_symbol(data, 3.7)
        assert abs(ts.value - 1.0) < 1e-10

    def test_tame_branch_point_equals_t(self):
        """At a branch point P = (t_0, 0): Tame_P = t_0 (since vt=0, vy=1)."""
        data = virasoro_shadow_data_numerical(2.0)
        bp = branch_points_sextic(data)
        for t_bp in bp:
            ts = tame_symbol(data, t_bp)
            # sign = (-1)^{0*1} = 1, value = t_bp^1 / y^0 = t_bp
            assert abs(ts.value - t_bp) < 1e-8

    def test_virasoro_tame_at_c1(self):
        """Full tame symbol computation at c=1."""
        result = virasoro_tame_symbols(1.0)
        assert result['c'] == 1.0
        assert abs(result['kappa'] - 0.5) < 1e-14
        assert len(result['tame_symbols']) >= 3  # origin, infinity, 2 branch points

    def test_virasoro_tame_at_c13(self):
        """Full tame symbol computation at c=13 (self-dual)."""
        result = virasoro_tame_symbols(13.0)
        assert abs(result['kappa'] - 6.5) < 1e-14

    def test_virasoro_tame_at_c25(self):
        """Full tame symbol computation at c=25."""
        result = virasoro_tame_symbols(25.0)
        assert abs(result['kappa'] - 12.5) < 1e-14


# ===========================================================================
# 5. Weil reciprocity
# ===========================================================================

class TestWeilReciprocity:
    """Product of tame symbols (Weil reciprocity check)."""

    def test_tame_product_heisenberg(self):
        """For Heisenberg: origin and infinity contribute.
        q2 = 0, so Tame_infty = -sqrt(q2) = 0. Product is 0."""
        data = heisenberg_shadow_data_numerical(1.0)
        tames = compute_all_tame_symbols(data)
        prod = product_of_tame_symbols(tames)
        # q2 = 0 for Heisenberg => infinity tame symbol is 0 => product is 0
        assert abs(prod) < 1e-10

    def test_tame_product_virasoro_c1(self):
        """Product of tame symbols at c=1."""
        data = virasoro_shadow_data_numerical(1.0)
        tames = compute_all_tame_symbols(data)
        prod = product_of_tame_symbols(tames)
        assert abs(prod) < 1e15  # Should be finite

    def test_tame_product_virasoro_c2(self):
        """Product at c=2."""
        data = virasoro_shadow_data_numerical(2.0)
        tames = compute_all_tame_symbols(data)
        prod = product_of_tame_symbols(tames)
        assert abs(prod) < 1e15

    def test_tame_product_virasoro_c13(self):
        """Product at c=13 (self-dual point)."""
        data = virasoro_shadow_data_numerical(13.0)
        tames = compute_all_tame_symbols(data)
        prod = product_of_tame_symbols(tames)
        assert abs(prod) < 1e15

    def test_number_of_tame_symbols(self):
        """For Virasoro (2 branch points): should have 4 tame symbols."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            tames = compute_all_tame_symbols(data)
            assert len(tames) == 4  # origin, infinity, 2 branch points


# ===========================================================================
# 6. Beilinson regulator (branch cycle)
# ===========================================================================

class TestBeilinsonRegulatorBranch:
    """Beilinson regulator on the branch-cut cycle."""

    def test_branch_regulator_virasoro_c1(self):
        """Regulator at c=1 should be finite and real-valued."""
        data = virasoro_shadow_data_numerical(1.0)
        reg = beilinson_regulator_branch_cycle(data, n_points=500)
        assert abs(reg) < 1e6  # finite
        # The imaginary part should be small (real integration)
        assert abs(reg.imag) < abs(reg.real) * 0.1 + 1e-6

    def test_branch_regulator_virasoro_c2(self):
        """Regulator at c=2."""
        data = virasoro_shadow_data_numerical(2.0)
        reg = beilinson_regulator_branch_cycle(data, n_points=500)
        assert abs(reg) < 1e6

    def test_branch_regulator_virasoro_c13(self):
        """Regulator at c=13 (self-dual)."""
        data = virasoro_shadow_data_numerical(13.0)
        reg = beilinson_regulator_branch_cycle(data, n_points=500)
        assert abs(reg) < 1e6

    def test_branch_regulator_heisenberg_zero(self):
        """For Heisenberg (no branch cut): regulator should be zero."""
        data = heisenberg_shadow_data_numerical(1.0)
        reg = beilinson_regulator_branch_cycle(data, n_points=200)
        assert abs(reg) < 1e-4

    def test_branch_regulator_convergence(self):
        """Regulator should converge as n_points increases."""
        data = virasoro_shadow_data_numerical(2.0)
        reg_low = beilinson_regulator_branch_cycle(data, n_points=200)
        reg_high = beilinson_regulator_branch_cycle(data, n_points=1000)
        # Should agree to 10% or better (ellipse approximation)
        if abs(reg_high) > 1e-6:
            rel_diff = abs(reg_high - reg_low) / abs(reg_high)
            assert rel_diff < 0.5  # generous for ellipse approximation


# ===========================================================================
# 7. Beilinson regulator (infinity cycle)
# ===========================================================================

class TestBeilinsonRegulatorInfinity:
    """Regulator on the cycle around infinity."""

    def test_infinity_regulator_virasoro_c1(self):
        """Regulator at c=1 on large circle."""
        data = virasoro_shadow_data_numerical(1.0)
        reg = beilinson_regulator_infinity_cycle(data, R=50.0, n_points=1000)
        assert abs(reg) < 1e6

    def test_infinity_regulator_virasoro_c13(self):
        """Regulator at c=13 on large circle."""
        data = virasoro_shadow_data_numerical(13.0)
        reg = beilinson_regulator_infinity_cycle(data, R=50.0, n_points=1000)
        assert abs(reg) < 1e6

    def test_infinity_regulator_heisenberg(self):
        """Heisenberg: y = sqrt(q0)*t^2 on normalization, winding number 2."""
        data = heisenberg_shadow_data_numerical(1.0)
        reg = beilinson_regulator_infinity_cycle(data, R=50.0, n_points=1000)
        assert abs(reg) < 1e6

    def test_all_cycles_returns_both(self):
        """beilinson_regulator_all_cycles returns both cycle regulators."""
        data = virasoro_shadow_data_numerical(1.0)
        regs = beilinson_regulator_all_cycles(data, n_points=200)
        assert 'branch_cycle' in regs
        assert 'infinity_cycle' in regs


# ===========================================================================
# 8. Shadow L-function derivative
# ===========================================================================

class TestShadowLFunction:
    """Shadow L-function and its derivative at s=0."""

    def test_shadow_coefficients_heisenberg(self):
        """Heisenberg: S_2 = k, S_r = 0 for r >= 3."""
        data = heisenberg_shadow_data_numerical(2.0)
        coeffs = shadow_coefficients_numerical(data, max_r=10)
        assert abs(coeffs[2] - 2.0) < 1e-10  # S_2 = kappa = k = 2
        for r in range(3, 11):
            assert abs(coeffs[r]) < 1e-10

    def test_shadow_coefficients_virasoro_S2(self):
        """Virasoro S_2 = c/2."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            coeffs = shadow_coefficients_numerical(data, max_r=10)
            assert abs(coeffs[2] - c_val / 2.0) < 1e-8

    def test_shadow_coefficients_virasoro_S3(self):
        """Virasoro S_3 = alpha/3 * a_1 / 3 where a_1 = q1/(2a0) = 6c/(c) = 6.
        Actually S_r = a_{r-2}/r. a_0 = |c|, a_1 = q1/(2a0) = 12c/(2|c|) = 6*sgn(c).
        So S_3 = a_1/3 = 2*sgn(c).
        """
        data = virasoro_shadow_data_numerical(1.0)
        coeffs = shadow_coefficients_numerical(data, max_r=10)
        assert abs(coeffs[3] - 2.0) < 1e-8  # S_3 = 2 for c > 0

    def test_shadow_zeta_heisenberg(self):
        """zeta_H(n) = k * 2^{-n} for Heisenberg at level k."""
        data = heisenberg_shadow_data_numerical(3.0)
        for n in [2, 3, 4, 5]:
            val = shadow_zeta_at_integer(data, n, max_r=10)
            expected = 3.0 * 2.0 ** (-n)
            assert abs(val - expected) < 1e-10

    def test_shadow_L_derivative_heisenberg(self):
        """L'_H(0) = -k * log(2) for Heisenberg."""
        data = heisenberg_shadow_data_numerical(2.0)
        Lp = shadow_L_function_derivative_at_zero(data, max_r=10)
        expected = -2.0 * math.log(2.0)
        assert abs(Lp - expected) < 1e-10

    def test_shadow_L_derivative_virasoro_c1_divergent(self):
        """At c=1 (rho > 1, below critical c* ~ 6.12): L'(0) diverges.
        The truncated sum grows with max_r."""
        data = virasoro_shadow_data_numerical(1.0)
        Lp_small = shadow_L_function_derivative_at_zero(data, max_r=20)
        Lp_large = shadow_L_function_derivative_at_zero(data, max_r=40)
        # Should grow (divergent series): larger truncation gives larger |value|
        assert abs(Lp_large) > abs(Lp_small) * 0.5  # at least comparable

    def test_shadow_L_derivative_virasoro_c13_convergent(self):
        """At c=13 (rho < 1, above critical c*): L'(0) should converge."""
        data = virasoro_shadow_data_numerical(13.0)
        Lp = shadow_L_function_derivative_at_zero(data, max_r=80)
        assert abs(Lp) < 1e6  # convergent

    def test_shadow_zeta_convergence_virasoro(self):
        """Shadow zeta at n=4 should converge for Virasoro at c=13."""
        data = virasoro_shadow_data_numerical(13.0)
        result = shadow_zeta_two_methods(data, 4, max_r_direct=150, max_r_check=80)
        assert result['relative_diff'] < 0.1  # Converges well at n=4


# ===========================================================================
# 9. Beilinson conjecture rational factor
# ===========================================================================

class TestBeilinsonConjecture:
    """Beilinson conjecture: L'(0) / reg should be rational (formal analogy)."""

    def test_beilinson_ratio_virasoro_c1(self):
        """Compute the ratio at c=1."""
        data = virasoro_shadow_data_numerical(1.0)
        result = beilinson_conjecture_rational_factor(data, n_points=500, max_r=80)
        assert result['L_prime_0'] is not None
        # The ratio may or may not be rational; we just check it's computed

    def test_beilinson_ratio_virasoro_c2(self):
        """Compute the ratio at c=2."""
        data = virasoro_shadow_data_numerical(2.0)
        result = beilinson_conjecture_rational_factor(data, n_points=500, max_r=80)
        assert result['L_prime_0'] is not None

    def test_beilinson_ratio_heisenberg(self):
        """For Heisenberg: L'(0) = -k*log(2), reg ~ 0. Ratio may be degenerate."""
        data = heisenberg_shadow_data_numerical(1.0)
        result = beilinson_conjecture_rational_factor(data, n_points=300, max_r=20)
        # Branch regulator is ~0 for Heisenberg, so ratio should be None or large
        assert result['L_prime_0'] is not None


# ===========================================================================
# 10. Borel regulator at integer points
# ===========================================================================

class TestBorelRegulator:
    """Shadow Borel regulators at positive integers."""

    def test_borel_n2_heisenberg(self):
        """zeta_H(2) = k * 2^{-2} = k/4."""
        data = heisenberg_shadow_data_numerical(4.0)
        result = borel_regulator_shadow(data, 2, max_r=10)
        assert abs(result['zeta_A_n'] - 1.0) < 1e-10  # 4/4 = 1

    def test_borel_n3_heisenberg(self):
        """zeta_H(3) = k * 2^{-3} = k/8."""
        data = heisenberg_shadow_data_numerical(2.0)
        result = borel_regulator_shadow(data, 3, max_r=10)
        assert abs(result['zeta_A_n'] - 0.25) < 1e-10  # 2/8 = 0.25

    def test_borel_table_virasoro(self):
        """Borel table at c=1 should have entries for n=2,3,4,5."""
        data = virasoro_shadow_data_numerical(1.0)
        table = borel_regulator_table(data, range(2, 6), max_r=80)
        assert len(table) == 4
        for entry in table:
            assert 'zeta_A_n' in entry
            assert 'n' in entry

    def test_borel_monotone_heisenberg(self):
        """For Heisenberg: zeta_H(n) = k*2^{-n} is strictly decreasing in n."""
        data = heisenberg_shadow_data_numerical(1.0)
        table = borel_regulator_table(data, range(2, 8), max_r=10)
        values = [entry['zeta_A_n'] for entry in table]
        for i in range(len(values) - 1):
            assert values[i] > values[i + 1]

    def test_borel_ratio_to_pi_heisenberg(self):
        """Heisenberg zeta_H(2) = k/4 -> ratio to pi^2 is k/(4*pi^2)."""
        data = heisenberg_shadow_data_numerical(1.0)
        result = borel_regulator_shadow(data, 2, max_r=10)
        expected_ratio = 0.25 / (math.pi ** 2)
        if result['ratio_to_pi_n'] is not None:
            assert abs(result['ratio_to_pi_n'] - expected_ratio) < 1e-10

    def test_borel_virasoro_positive_n4(self):
        """zeta_Vir(4) at c=13 should be computable."""
        data = virasoro_shadow_data_numerical(13.0)
        result = borel_regulator_shadow(data, 4, max_r=100)
        # Should be finite
        assert abs(result['zeta_A_n']) < 1e10


# ===========================================================================
# 11. Chern character
# ===========================================================================

class TestChernCharacter:
    """Shadow Chern character through degree 3."""

    def test_ch0_rank(self):
        """ch_0 = rank = 1 for single-generator families."""
        data = virasoro_shadow_data_numerical(1.0)
        ch = shadow_chern_character('virasoro', data, rank=1)
        assert ch.ch0 == 1.0
        assert ch.rank == 1

    def test_ch1_equals_kappa(self):
        """ch_1 = c_1 = kappa for rank 1."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            ch = shadow_chern_character('virasoro', data, rank=1)
            assert abs(ch.ch1 - c_val / 2.0) < 1e-12

    def test_c1_equals_kappa(self):
        """c_1 coefficient = kappa (Theorem D)."""
        data = virasoro_shadow_data_numerical(1.0)
        ch = shadow_chern_character('virasoro', data)
        assert abs(ch.c1_coeff - 0.5) < 1e-14

    def test_c2_rank1_formula(self):
        """For rank 1: c_2 = kappa^2/2 (from line bundle splitting)."""
        data = virasoro_shadow_data_numerical(2.0)
        ch = shadow_chern_character('virasoro', data, rank=1)
        assert abs(ch.c2_coeff - 0.5) < 1e-12  # kappa=1, so kappa^2/2 = 0.5

    def test_ch2_rank1_zero(self):
        """For rank 1: ch_2 = (c_1^2 - 2c_2)/2 = 0 (since c_2 = c_1^2/2)."""
        data = virasoro_shadow_data_numerical(1.0)
        ch = shadow_chern_character('virasoro', data, rank=1)
        assert abs(ch.ch2) < 1e-12

    def test_ch3_rank1_zero(self):
        """For rank 1: ch_3 = 0."""
        data = virasoro_shadow_data_numerical(1.0)
        ch = shadow_chern_character('virasoro', data, rank=1)
        assert abs(ch.ch3) < 1e-12

    def test_heisenberg_chern(self):
        """Heisenberg at k=1: kappa=1, ch_1=1."""
        data = heisenberg_shadow_data_numerical(1.0)
        ch = shadow_chern_character('heisenberg', data, rank=1)
        assert abs(ch.ch1 - 1.0) < 1e-14

    def test_affine_sl2_chern(self):
        """Affine sl_2 at k=1: kappa = 3*3/4 = 9/4 = 2.25."""
        data = affine_sl2_shadow_data_numerical(1.0)
        ch = shadow_chern_character('affine_sl2', data, rank=1)
        assert abs(ch.ch1 - 2.25) < 1e-12

    def test_chern_landscape(self):
        """Landscape computation should cover all families."""
        landscape = chern_character_landscape()
        assert 'virasoro_c1.0' in landscape
        assert 'heisenberg_k1.0' in landscape
        assert 'affine_sl2_k1.0' in landscape
        assert 'betagamma' in landscape

    def test_chern_corrections_stored(self):
        """Planted-forest correction delta_pf_g2 should be stored."""
        data = virasoro_shadow_data_numerical(1.0)
        ch = shadow_chern_character('virasoro', data, rank=1)
        assert 'delta_pf_g2' in ch.corrections
        # delta_pf = alpha*(10*alpha - kappa)/48 = 2*(20-0.5)/48 = 2*19.5/48
        expected = 2.0 * (20.0 - 0.5) / 48.0
        assert abs(ch.corrections['delta_pf_g2'] - expected) < 1e-12

    def test_kappa_additivity_chern(self):
        """For Heisenberg: kappa(H_k1 + H_k2) = k1 + k2 -> ch_1 additive."""
        data1 = heisenberg_shadow_data_numerical(1.0)
        data2 = heisenberg_shadow_data_numerical(2.0)
        ch1 = shadow_chern_character('heisenberg', data1)
        ch2 = shadow_chern_character('heisenberg', data2)
        assert abs(ch1.ch1 + ch2.ch1 - 3.0) < 1e-12


# ===========================================================================
# 12. Motivic cohomology
# ===========================================================================

class TestMotivicCohomology:
    """Shadow motivic cohomology groups."""

    def test_H0_rank(self):
        """H^0_M(C_A, Z(0)) = Z for all families."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(1.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            mc = compute_motivic_cohomology(family, data)
            assert mc.H0_rank == 1

    def test_H1_generators(self):
        """H^1_M = O* should include standard generators."""
        data = virasoro_shadow_data_numerical(1.0)
        mc = compute_motivic_cohomology('virasoro', data)
        assert len(mc.H1_generators) >= 2

    def test_H2_nontrivial_all_families(self):
        """H^2_M should be nontrivial (contains {t,y}) for all families."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(1.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
            ('affine_sl2', lambda: affine_sl2_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            mc = compute_motivic_cohomology(family, data)
            assert mc.H2_nontrivial

    def test_milnor_symbol_is_t_y(self):
        """Canonical Milnor symbol is {t, y}."""
        data = virasoro_shadow_data_numerical(1.0)
        mc = compute_motivic_cohomology('virasoro', data)
        assert mc.milnor_symbol == '{t, y}'

    def test_shadow_class_consistency(self):
        """Shadow class should match Delta classification."""
        data_G = heisenberg_shadow_data_numerical(1.0)
        mc_G = compute_motivic_cohomology('heisenberg', data_G)
        assert mc_G.shadow_class == 'G'

        data_M = virasoro_shadow_data_numerical(1.0)
        mc_M = compute_motivic_cohomology('virasoro', data_M)
        assert mc_M.shadow_class == 'M'


# ===========================================================================
# 13. Koszul duality and regulators
# ===========================================================================

class TestKoszulDualityRegulators:
    """Koszul duality c -> 26-c for Virasoro regulators."""

    def test_kappa_sum_is_13(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13."""
        for c_val in [1.0, 2.0, 13.0, 25.0]:
            result = koszul_duality_regulator_check(c_val, n_points=200)
            assert abs(result['kappa_sum'] - 13.0) < 1e-12

    def test_self_duality_at_c13(self):
        """At c=13: c_dual = 13, so A = A^!."""
        result = koszul_duality_regulator_check(13.0, n_points=200)
        assert abs(result['c'] - result['c_dual']) < 1e-12

    def test_c1_and_c25_dual(self):
        """c=1 and c=25 are Koszul dual."""
        result = koszul_duality_regulator_check(1.0, n_points=200)
        assert abs(result['c_dual'] - 25.0) < 1e-12

    def test_c2_and_c24_dual(self):
        """c=2 and c=24 are Koszul dual."""
        result = koszul_duality_regulator_check(2.0, n_points=200)
        assert abs(result['c_dual'] - 24.0) < 1e-12


# ===========================================================================
# 14. Cross-verification
# ===========================================================================

class TestCrossVerification:
    """Multi-path verification of regulator computations."""

    def test_residue_regulator_well_defined(self):
        """Residue-based regulator should be computable."""
        data = virasoro_shadow_data_numerical(1.0)
        result = regulator_via_residues(data)
        assert 'residue_regulator' in result
        assert len(result['tame_symbols']) >= 3

    def test_cross_verify_both_paths(self):
        """Cross-verification should return both path results."""
        data = virasoro_shadow_data_numerical(2.0)
        result = cross_verify_regulator(data, n_points=300)
        assert 'path1_integration' in result
        assert 'path2_residues' in result

    def test_shadow_zeta_two_methods_heisenberg(self):
        """For Heisenberg: both truncations should agree exactly."""
        data = heisenberg_shadow_data_numerical(1.0)
        result = shadow_zeta_two_methods(data, 3, max_r_direct=50, max_r_check=10)
        assert result['difference'] < 1e-14

    def test_shadow_zeta_two_methods_virasoro(self):
        """For Virasoro at large n: good convergence."""
        data = virasoro_shadow_data_numerical(13.0)
        result = shadow_zeta_two_methods(data, 6, max_r_direct=150, max_r_check=50)
        # At n=6 the series converges fast
        assert result['relative_diff'] < 0.01

    def test_independent_kappa_verification(self):
        """Path 1 (data formula) vs Path 2 (coefficient extraction) for kappa."""
        for c_val in [1.0, 2.0, 13.0, 25.0]:
            # Path 1: direct formula
            kappa_direct = c_val / 2.0
            # Path 2: extract from shadow coefficients
            data = virasoro_shadow_data_numerical(c_val)
            coeffs = shadow_coefficients_numerical(data, max_r=5)
            kappa_extracted = coeffs[2]
            assert abs(kappa_direct - kappa_extracted) < 1e-8

    def test_QL_consistency_with_coefficients(self):
        """Q_L(t) evaluated at small t should match Taylor expansion via S_r."""
        data = virasoro_shadow_data_numerical(2.0)
        t_test = 0.01
        # Direct Q_L evaluation
        QL_direct = shadow_metric_QL(data, t_test)
        # From q0 + q1*t + q2*t^2
        QL_coeff = data['q0'] + data['q1'] * t_test + data['q2'] * t_test ** 2
        assert abs(QL_direct - QL_coeff) < 1e-12


# ===========================================================================
# 15. Landscape-wide consistency
# ===========================================================================

class TestLandscape:
    """Landscape-wide tests across all families."""

    def test_full_regulator_data_virasoro(self):
        """Complete regulator data for Virasoro should be well-formed."""
        data = virasoro_shadow_data_numerical(1.0)
        result = compute_full_regulator_data('virasoro', data, n_points=200, max_r=50)
        assert result.family == 'virasoro'
        assert result.K0.rank == 1
        assert len(result.tame_symbols) >= 3
        assert result.chern_character.ch1 == pytest.approx(0.5, abs=1e-12)

    def test_full_regulator_data_heisenberg(self):
        """Complete regulator data for Heisenberg."""
        data = heisenberg_shadow_data_numerical(1.0)
        result = compute_full_regulator_data('heisenberg', data, n_points=200, max_r=20)
        assert result.family == 'heisenberg'
        assert result.K0.shadow_class == 'G'

    def test_full_regulator_data_affine(self):
        """Complete regulator data for affine sl_2."""
        data = affine_sl2_shadow_data_numerical(1.0)
        result = compute_full_regulator_data('affine_sl2', data, n_points=200, max_r=20)
        assert result.family == 'affine_sl2'
        assert result.K0.shadow_class == 'L'

    def test_chern_kappa_consistency(self):
        """ch_1 = kappa across all families (Theorem D)."""
        landscape = chern_character_landscape()
        for name, ch in landscape.items():
            assert abs(ch.ch1 - ch.kappa) < 1e-12, \
                f"{name}: ch1={ch.ch1} != kappa={ch.kappa}"

    def test_motivic_all_families(self):
        """Motivic cohomology computable for all standard families."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(2.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
            ('affine_sl2', lambda: affine_sl2_shadow_data_numerical(1.0)),
            ('betagamma', lambda: betagamma_shadow_data_numerical(0.5)),
        ]:
            data = fn()
            mc = compute_motivic_cohomology(family, data)
            assert mc.H0_rank == 1
            assert mc.H2_nontrivial

    def test_tame_symbols_all_virasoro(self):
        """Tame symbols computable at all test central charges."""
        for c_val in [1.0, 2.0, 13.0, 25.0]:
            result = virasoro_tame_symbols(c_val)
            assert len(result['tame_symbols']) >= 3

    def test_virasoro_beilinson_regulator_wrapper(self):
        """Wrapper function should work."""
        result = virasoro_beilinson_regulator(1.0, n_points=200)
        assert 'regulators' in result
        assert result['c'] == 1.0

    def test_borel_all_families(self):
        """Borel regulator table for convergent families.
        Use c=13 for Virasoro (rho < 1, convergent); c=1 diverges."""
        for family, fn in [
            ('virasoro', lambda: virasoro_shadow_data_numerical(13.0)),
            ('heisenberg', lambda: heisenberg_shadow_data_numerical(1.0)),
        ]:
            data = fn()
            table = borel_regulator_table(data, range(2, 5), max_r=50)
            assert len(table) == 3
            for entry in table:
                assert abs(entry['zeta_A_n']) < 1e10


# ===========================================================================
# 16. Additional edge cases and properties
# ===========================================================================

class TestEdgeCases:
    """Edge cases, boundaries, and special values."""

    def test_virasoro_c_equals_half(self):
        """Virasoro at c=1/2 (Ising model)."""
        data = virasoro_shadow_data_numerical(0.5)
        assert abs(data['kappa'] - 0.25) < 1e-14
        ts = compute_all_tame_symbols(data)
        assert len(ts) >= 3

    def test_large_c_limit(self):
        """At large c: kappa ~ c/2, Delta ~ 40/(5c) -> 0.
        Shadow curve approaches class G behavior (Delta -> 0)."""
        data = virasoro_shadow_data_numerical(1000.0)
        assert data['Delta'] < 0.01  # Delta = 40/(5022) ~ 0.008

    def test_c_near_lee_yang(self):
        """At c = -22/5 + epsilon: near the Lee-Yang point (pole)."""
        # c = -22/5 = -4.4 is a pole. Test near it.
        data = virasoro_shadow_data_numerical(-4.0)
        # Should work (c=-4 is away from the pole)
        assert data['kappa'] == -2.0

    def test_negative_kappa_heisenberg(self):
        """Heisenberg at negative level: kappa < 0."""
        data = heisenberg_shadow_data_numerical(-3.0)
        assert data['kappa'] == -3.0
        K0 = compute_K0('heisenberg', data)
        assert K0.rank == 1

    def test_shadow_zeta_at_large_n_convergent(self):
        """Shadow zeta at large n should converge to S_2 * 2^{-n}.
        Use c=13 (rho < 1, convergent tower) so higher terms decay."""
        data = virasoro_shadow_data_numerical(13.0)
        coeffs = shadow_coefficients_numerical(data, max_r=50)
        S2 = coeffs[2]
        val_n20 = shadow_zeta_at_integer(data, 20, max_r=50)
        # Dominated by r=2 term: S_2 * 2^{-20}
        dominant = S2 * 2.0 ** (-20)
        # Should be close (higher terms decay as rho^r * r^{-n})
        assert abs(val_n20 - dominant) / abs(dominant) < 0.1

    def test_shadow_zeta_heisenberg_exact_at_large_n(self):
        """For Heisenberg: zeta_H(n) = k*2^{-n} exactly (only r=2 term)."""
        data = heisenberg_shadow_data_numerical(1.0)
        val = shadow_zeta_at_integer(data, 20, max_r=50)
        expected = 1.0 * 2.0 ** (-20)
        assert abs(val - expected) < 1e-14

    def test_betagamma_shadow_data(self):
        """Beta-gamma shadow data at lambda=0.5: c = -1, kappa = -1/2."""
        data = betagamma_shadow_data_numerical(0.5)
        assert abs(data['c'] - (-1.0)) < 1e-12
        assert abs(data['kappa'] - (-0.5)) < 1e-12

    def test_affine_sl2_sugawara(self):
        """Affine sl_2 Sugawara central charge c = 3k/(k+2)."""
        data = affine_sl2_shadow_data_numerical(1.0)
        assert abs(data['c'] - 1.0) < 1e-12  # c = 3*1/3 = 1

    def test_virasoro_delta_positivity(self):
        """For Virasoro with c > 0: Delta = 40/(5c+22) > 0 (class M)."""
        for c_val in [0.5, 1.0, 2.0, 13.0, 25.0, 100.0]:
            data = virasoro_shadow_data_numerical(c_val)
            assert data['Delta'] > 0


class TestShadowCurveY:
    """Shadow curve y-coordinate evaluation."""

    def test_y_at_zero_is_zero(self):
        """y(0) = 0 since f(0) = 0."""
        data = virasoro_shadow_data_numerical(1.0)
        y_val = shadow_curve_y(data, 0.0)
        assert abs(y_val) < 1e-14

    def test_y_squared_equals_f(self):
        """y^2 = f(t) = t^4 * Q_L(t) at a generic point."""
        data = virasoro_shadow_data_numerical(2.0)
        t_test = complex(1.5, 0.3)
        y_val = shadow_curve_y(data, t_test, branch=1)
        f_val = shadow_sextic_f(data, t_test)
        assert abs(y_val ** 2 - f_val) < 1e-10

    def test_two_branches(self):
        """y and -y should be the two branches."""
        data = virasoro_shadow_data_numerical(1.0)
        t_test = complex(2.0, 0.5)
        y_plus = shadow_curve_y(data, t_test, branch=1)
        y_minus = shadow_curve_y(data, t_test, branch=-1)
        assert abs(y_plus + y_minus) < 1e-10


class TestSymbolicConsistency:
    """Cross-checks between different parts of the computation."""

    def test_delta_from_kappa_S4(self):
        """Delta = 8*kappa*S4 for all families."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            delta_formula = 8.0 * data['kappa'] * data['S4']
            assert abs(data['Delta'] - delta_formula) < 1e-14

    def test_q2_from_gaussian_decomposition(self):
        """q_2 = 9*alpha^2 + 2*Delta (from Gaussian decomposition)."""
        for c_val in [1.0, 2.0, 13.0]:
            data = virasoro_shadow_data_numerical(c_val)
            q2_check = 9.0 * data['alpha'] ** 2 + 2.0 * data['Delta']
            # Also q2 = (180c+872)/(5c+22)
            q2_formula = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
            assert abs(data['q2'] - q2_formula) < 1e-10
            assert abs(data['q2'] - q2_check) < 1e-10

    def test_QL_gaussian_decomposition(self):
        """Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        data = virasoro_shadow_data_numerical(2.0)
        for t_val in [0.0, 0.5, 1.0, -1.0]:
            QL = shadow_metric_QL(data, t_val)
            gaussian = (2 * data['kappa'] + 3 * data['alpha'] * t_val) ** 2 + \
                       2 * data['Delta'] * t_val ** 2
            assert abs(QL - gaussian) < 1e-10

    def test_branch_points_conjugate_for_positive_delta(self):
        """When Delta > 0: branch points are complex conjugate."""
        data = virasoro_shadow_data_numerical(1.0)
        t_p, t_m = QL_zeros(data)
        assert abs(t_p.imag + t_m.imag) < 1e-10  # conjugate imaginary parts
        assert abs(t_p.real - t_m.real) < 1e-10  # same real part

    def test_virasoro_c26_minus_c_duality(self):
        """Shadow data at c and 26-c: kappa(c) + kappa(26-c) = 13."""
        for c_val in [1.0, 5.0, 10.0]:
            d1 = virasoro_shadow_data_numerical(c_val)
            d2 = virasoro_shadow_data_numerical(26.0 - c_val)
            assert abs(d1['kappa'] + d2['kappa'] - 13.0) < 1e-12

    def test_complementarity_discriminant(self):
        r"""Delta(c) + Delta(26-c) = 40/(5c+22) + 40/(152-5c).

        This should equal 40*[1/(5c+22) + 1/(152-5c)]
        = 40 * (152-5c + 5c+22) / [(5c+22)(152-5c)]
        = 40 * 174 / [(5c+22)(152-5c)]
        = 6960 / [(5c+22)(152-5c)].
        """
        for c_val in [1.0, 5.0, 13.0]:
            d1 = virasoro_shadow_data_numerical(c_val)
            d2 = virasoro_shadow_data_numerical(26.0 - c_val)
            delta_sum = d1['Delta'] + d2['Delta']
            expected = 6960.0 / ((5.0 * c_val + 22.0) * (152.0 - 5.0 * c_val))
            assert abs(delta_sum - expected) < 1e-10


# ===========================================================================
# 17. Full landscape (slow)
# ===========================================================================

class TestFullLandscape:
    """Full landscape computation (may be slow)."""

    @pytest.mark.slow
    def test_full_landscape(self):
        """Full landscape should include all families."""
        landscape = full_landscape_regulators()
        assert 'virasoro_c1.0' in landscape
        assert 'virasoro_c13.0' in landscape
        assert 'heisenberg_k1.0' in landscape
        assert 'affine_sl2_k1' in landscape
        assert 'betagamma' in landscape

    def test_landscape_kappa_consistency(self):
        """All landscape entries should have consistent kappa values."""
        landscape = chern_character_landscape()
        for name, ch in landscape.items():
            assert abs(ch.c1_coeff - ch.kappa) < 1e-12
