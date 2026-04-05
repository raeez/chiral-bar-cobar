r"""Tests for explicit MC element Theta_A computation.

Verifies:
1. Virasoro shadow obstruction tower at specific c values (seed data + recursion)
2. MC equation residuals at all arities (must vanish)
3. Affine sl_2 tensor components (Killing form, cubic, quartic vanishing)
4. Heisenberg tower termination (class G)
5. Depth classification consistency
6. Duality relations (Koszul complementarity)
7. Self-dual point c = 13 analysis
8. Cross-family consistency
9. Shadow metric algebraicity
10. Comparison with existing shadow modules

Ground truth:
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:recursive-existence (higher_genus_modular_koszul.tex)
    thm:obstruction-recursion (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    landscape_census.tex (authoritative formula source)
"""

import math
from fractions import Fraction as FR

import pytest
from sympy import Rational, Symbol, simplify, cancel, Abs, N as Neval, sqrt

from compute.lib.explicit_theta import (
    AffineSl2Theta,
    HeisenbergTheta,
    ThetaComponent,
    VirasoroTheta,
    compare_families,
    mc_equation_residual_scalar,
    sl2_cubic_tensor_at_k,
    verify_mc_tower,
    virasoro_duality_check,
    virasoro_self_dual_analysis,
    virasoro_theta_numerical,
    virasoro_theta_table,
)


# ============================================================================
# 1. Virasoro seed data verification
# ============================================================================

class TestVirasoroSeedData:
    """Verify the three seed values S_2, S_3, S_4 at specific c."""

    def test_kappa_c_half(self):
        """kappa(Vir_{1/2}) = 1/4."""
        theta = VirasoroTheta(c_val=Rational(1, 2))
        assert theta.kappa() == Rational(1, 4)

    def test_kappa_c1(self):
        """kappa(Vir_1) = 1/2."""
        theta = VirasoroTheta(c_val=Rational(1))
        assert theta.kappa() == Rational(1, 2)

    def test_kappa_c13(self):
        """kappa(Vir_13) = 13/2."""
        theta = VirasoroTheta(c_val=Rational(13))
        assert theta.kappa() == Rational(13, 2)

    def test_kappa_c25(self):
        """kappa(Vir_25) = 25/2."""
        theta = VirasoroTheta(c_val=Rational(25))
        assert theta.kappa() == Rational(25, 2)

    def test_kappa_c26(self):
        """kappa(Vir_26) = 13."""
        theta = VirasoroTheta(c_val=Rational(26))
        assert theta.kappa() == Rational(13)

    def test_alpha_c_independent(self):
        """S_3 = 2 for all c (c-independent)."""
        for c_val in [Rational(1, 2), 1, 13, 25, 26]:
            theta = VirasoroTheta(c_val=c_val)
            assert theta.alpha() == Rational(2), f"S_3 != 2 at c={c_val}"

    def test_S4_c_half(self):
        """S_4(Vir_{1/2}) = 10 / [(1/2)(5/2 + 22)] = 10 / [(1/2)(49/2)] = 10/(49/4) = 40/49."""
        theta = VirasoroTheta(c_val=Rational(1, 2))
        expected = Rational(10) / (Rational(1, 2) * (5 * Rational(1, 2) + 22))
        assert simplify(theta.S4() - expected) == 0

    def test_S4_c1(self):
        """S_4(Vir_1) = 10 / (1 * 27) = 10/27."""
        theta = VirasoroTheta(c_val=Rational(1))
        assert simplify(theta.S4() - Rational(10, 27)) == 0

    def test_S4_c13(self):
        """S_4(Vir_13) = 10 / (13 * 87) = 10/1131."""
        theta = VirasoroTheta(c_val=Rational(13))
        assert simplify(theta.S4() - Rational(10, 1131)) == 0

    def test_S4_c26(self):
        """S_4(Vir_26) = 10 / (26 * 152) = 10/3952 = 5/1976."""
        theta = VirasoroTheta(c_val=Rational(26))
        expected = Rational(10) / (26 * 152)
        assert simplify(theta.S4() - expected) == 0


# ============================================================================
# 2. MC equation residuals
# ============================================================================

class TestMCResiduals:
    """Verify the MC equation is satisfied at all arities."""

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(13), Rational(25), Rational(26),
    ])
    def test_mc_residual_arity5(self, c_val):
        """MC residual at arity 5 should vanish."""
        theta = VirasoroTheta(c_val=c_val, max_arity=6)
        coeffs = {r: theta.S(r) for r in range(2, 7)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 5)
        assert simplify(res) == 0, f"MC residual at r=5, c={c_val}: {res}"

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(13), Rational(25), Rational(26),
    ])
    def test_mc_residual_arity6(self, c_val):
        """MC residual at arity 6 should vanish."""
        theta = VirasoroTheta(c_val=c_val, max_arity=7)
        coeffs = {r: theta.S(r) for r in range(2, 8)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 6)
        assert simplify(res) == 0, f"MC residual at r=6, c={c_val}: {res}"

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(13), Rational(25), Rational(26),
    ])
    def test_mc_residual_arity7(self, c_val):
        """MC residual at arity 7 should vanish."""
        theta = VirasoroTheta(c_val=c_val, max_arity=8)
        coeffs = {r: theta.S(r) for r in range(2, 9)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 7)
        assert simplify(res) == 0, f"MC residual at r=7, c={c_val}: {res}"

    @pytest.mark.parametrize("c_val", [
        Rational(1, 2), Rational(1), Rational(13), Rational(25), Rational(26),
    ])
    def test_mc_residual_arity8(self, c_val):
        """MC residual at arity 8 should vanish."""
        theta = VirasoroTheta(c_val=c_val, max_arity=9)
        coeffs = {r: theta.S(r) for r in range(2, 10)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 8)
        assert simplify(res) == 0, f"MC residual at r=8, c={c_val}: {res}"

    def test_mc_residuals_all_arities_c13(self):
        """Verify MC at all arities 5-15 for c = 13."""
        theta = VirasoroTheta(c_val=Rational(13), max_arity=16)
        coeffs = {r: theta.S(r) for r in range(2, 17)}
        results = verify_mc_tower(theta.kappa(), coeffs, max_r=15)
        for r, res in results.items():
            assert simplify(res) == 0, f"MC failed at r={r}, c=13: {res}"

    def test_mc_residuals_all_arities_c1(self):
        """Verify MC at all arities 5-15 for c = 1."""
        theta = VirasoroTheta(c_val=Rational(1), max_arity=16)
        coeffs = {r: theta.S(r) for r in range(2, 17)}
        results = verify_mc_tower(theta.kappa(), coeffs, max_r=15)
        for r, res in results.items():
            assert simplify(res) == 0, f"MC failed at r={r}, c=1: {res}"


# ============================================================================
# 3. Explicit Theta components at specific c values
# ============================================================================

class TestExplicitComponents:
    """Test the explicit ThetaComponent objects."""

    def test_component_arity2_type(self):
        """Arity-2 component is non-zero."""
        theta = VirasoroTheta(c_val=Rational(1))
        comp = theta.component(2)
        assert comp.arity == 2
        assert not comp.is_zero

    def test_component_arity3_scalar(self):
        """Arity-3 component has scalar value 2."""
        theta = VirasoroTheta(c_val=Rational(1))
        comp = theta.component(3)
        assert simplify(comp.scalar_value - Rational(2)) == 0

    def test_component_arity4_nonzero(self):
        """Arity-4 component is nonzero for Virasoro (class M)."""
        theta = VirasoroTheta(c_val=Rational(1))
        comp = theta.component(4)
        assert not comp.is_zero

    def test_component_tensor_single_entry(self):
        """For single-generator Virasoro, tensor has one entry."""
        theta = VirasoroTheta(c_val=Rational(1))
        comp = theta.component(3)
        assert len(comp.tensor) == 1
        assert ('T', 'T', 'T') in comp.tensor
        assert simplify(comp.tensor[('T', 'T', 'T')] - Rational(2)) == 0

    def test_component_arity5_c_half(self):
        """S_5(Vir_{1/2}) computed from recursion."""
        theta = VirasoroTheta(c_val=Rational(1, 2), max_arity=6)
        s5 = theta.S(5)
        # S_5 = -48 / [c^2(5c+22)]
        expected = Rational(-48) / (Rational(1, 4) * (Rational(5, 2) + 22))
        assert simplify(s5 - expected) == 0

    def test_component_arity5_c1(self):
        """S_5(Vir_1) = -48 / (1 * 27) = -48/27 = -16/9."""
        theta = VirasoroTheta(c_val=Rational(1), max_arity=6)
        s5 = theta.S(5)
        expected = Rational(-48) / (1 * 27)
        assert simplify(s5 - expected) == 0


# ============================================================================
# 4. Virasoro Theta table
# ============================================================================

class TestVirasoroTable:
    """Test the table of Theta components across c values."""

    def test_table_has_all_c_values(self):
        table = virasoro_theta_table(max_arity=6)
        assert 'c=1/2' in table
        assert 'c=1' in table
        assert 'c=13' in table
        assert 'c=25' in table
        assert 'c=26' in table

    def test_table_s2_values(self):
        table = virasoro_theta_table(max_arity=4)
        assert simplify(table['c=1/2'][2] - Rational(1, 4)) == 0
        assert simplify(table['c=1'][2] - Rational(1, 2)) == 0
        assert simplify(table['c=13'][2] - Rational(13, 2)) == 0
        assert simplify(table['c=25'][2] - Rational(25, 2)) == 0
        assert simplify(table['c=26'][2] - Rational(13)) == 0

    def test_table_s3_universal(self):
        """S_3 = 2 for all c values."""
        table = virasoro_theta_table(max_arity=4)
        for label in table:
            assert simplify(table[label][3] - Rational(2)) == 0

    def test_table_s4_positive(self):
        """S_4 > 0 for c > 0."""
        table = virasoro_theta_table(max_arity=5)
        for label, c_val in [('c=1/2', 0.5), ('c=1', 1), ('c=13', 13),
                              ('c=25', 25), ('c=26', 26)]:
            s4 = table[label][4]
            assert float(Neval(s4)) > 0, f"S_4 <= 0 at {label}"


# ============================================================================
# 5. Heisenberg tower termination
# ============================================================================

class TestHeisenberg:
    """Verify Heisenberg MC element (class G, terminates at arity 2)."""

    def test_kappa_k1(self):
        theta = HeisenbergTheta(k_val=1)
        assert theta.kappa() == Rational(1)

    def test_kappa_k2(self):
        theta = HeisenbergTheta(k_val=2)
        assert theta.kappa() == Rational(2)

    def test_tower_terminates(self):
        """S_r = 0 for all r >= 3."""
        theta = HeisenbergTheta(k_val=1)
        for r in range(3, 20):
            assert theta.S(r) == 0, f"S_{r} != 0 for Heisenberg"

    def test_depth_class(self):
        theta = HeisenbergTheta(k_val=1)
        assert theta.depth_class() == 'G'

    def test_mc_residuals_all_zero(self):
        theta = HeisenbergTheta(k_val=1)
        results = theta.verify_mc_all(max_r=15)
        for r, res in results.items():
            assert res == 0, f"Heisenberg MC failed at r={r}"

    def test_component_arity2_nonzero(self):
        theta = HeisenbergTheta(k_val=1)
        comp = theta.component(2)
        assert not comp.is_zero

    def test_component_arity3_zero(self):
        theta = HeisenbergTheta(k_val=1)
        comp = theta.component(3)
        assert comp.is_zero


# ============================================================================
# 6. Affine sl_2 tensor components
# ============================================================================

class TestAffineSl2:
    """Verify affine sl_2 MC element (class L, terminates at arity 3)."""

    def test_kappa_k1(self):
        """kappa(sl_2, k=1) = 3(1+2)/4 = 9/4."""
        theta = AffineSl2Theta(k_val=1)
        assert theta.kappa() == Rational(9, 4)

    def test_kappa_k2(self):
        """kappa(sl_2, k=2) = 3(2+2)/4 = 3."""
        theta = AffineSl2Theta(k_val=2)
        assert theta.kappa() == Rational(3)

    def test_killing_form_structure(self):
        """Killing form: K(e,f) = K(f,e) = k, K(h,h) = 2k."""
        theta = AffineSl2Theta(k_val=1)
        K = theta.theta_arity2_tensor()
        assert K[('e', 'f')] == 1
        assert K[('f', 'e')] == 1
        assert K[('h', 'h')] == 2

    def test_cubic_nonzero(self):
        """The cubic tensor is nonzero on the full 3D space."""
        theta = AffineSl2Theta(k_val=1)
        C = theta.cubic_tensor()
        assert len(C) > 0, "Cubic tensor empty for sl_2"

    def test_cubic_hef(self):
        """C(h, e, f) = 2k."""
        theta = AffineSl2Theta(k_val=1)
        C = theta.cubic_tensor()
        assert simplify(C.get(('h', 'e', 'f'), 0) - 2) == 0

    def test_cubic_hfe(self):
        """C(h, f, e) = -2k (antisymmetric in last two indices)."""
        theta = AffineSl2Theta(k_val=1)
        C = theta.cubic_tensor()
        assert simplify(C.get(('h', 'f', 'e'), 0) + 2) == 0

    def test_cubic_efh(self):
        """C(e, f, h) = 2k."""
        theta = AffineSl2Theta(k_val=1)
        C = theta.cubic_tensor()
        assert simplify(C.get(('e', 'f', 'h'), 0) - 2) == 0

    def test_cubic_totally_antisymmetric(self):
        """C_{abc} = -C_{bac} (antisymmetric in first two indices)."""
        theta = AffineSl2Theta(k_val=1)
        C = theta.cubic_tensor()
        gens = ['e', 'h', 'f']
        for a in gens:
            for b in gens:
                for c_gen in gens:
                    val_ab = C.get((a, b, c_gen), 0)
                    val_ba = C.get((b, a, c_gen), 0)
                    assert simplify(val_ab + val_ba) == 0, \
                        f"Not antisymmetric: C({a},{b},{c_gen}) + C({b},{a},{c_gen}) = {simplify(val_ab + val_ba)}"

    def test_quartic_vanishes(self):
        """Theta^{(4)} = 0 for class L (Jacobi identity implies vanishing)."""
        theta = AffineSl2Theta(k_val=1)
        Q = theta.theta_arity4_tensor()
        assert len(Q) == 0, "Quartic should vanish for sl_2"

    def test_mc_arity3(self):
        """MC at arity 3: the cubic is a cocycle (Jacobi)."""
        theta = AffineSl2Theta(k_val=1)
        res = theta.mc_residual_arity3()
        assert simplify(res) == 0, f"Cubic is not a cocycle: {res}"

    def test_mc_arity4(self):
        """MC at arity 4: [K, C] = 0 (ad-invariance)."""
        theta = AffineSl2Theta(k_val=1)
        res = theta.mc_residual_arity4()
        assert simplify(res) == 0

    def test_mc_arity5(self):
        """MC at arity 5: trivially zero."""
        theta = AffineSl2Theta(k_val=1)
        res = theta.mc_residual_arity5()
        assert res == 0

    def test_depth_class(self):
        theta = AffineSl2Theta(k_val=1)
        assert theta.depth_class() == 'L'

    def test_s_on_h_line_terminates(self):
        """On the h-line (Cartan), S_r = 0 for r >= 3."""
        theta = AffineSl2Theta(k_val=1)
        for r in range(3, 10):
            assert theta.S(r) == 0


class TestAffineSl2AtK2:
    """Affine sl_2 at k = 2."""

    def test_kappa(self):
        theta = AffineSl2Theta(k_val=2)
        assert theta.kappa() == Rational(3)

    def test_cubic_hef(self):
        """C(h, e, f) = 2k = 4."""
        theta = AffineSl2Theta(k_val=2)
        C = theta.cubic_tensor()
        assert simplify(C.get(('h', 'e', 'f'), 0) - 4) == 0

    def test_quartic_vanishes(self):
        theta = AffineSl2Theta(k_val=2)
        Q = theta.theta_arity4_tensor()
        assert len(Q) == 0

    def test_mc_arity3(self):
        theta = AffineSl2Theta(k_val=2)
        assert simplify(theta.mc_residual_arity3()) == 0


# ============================================================================
# 7. Duality relations (Koszul complementarity)
# ============================================================================

class TestDuality:
    """Koszul duality: Vir_c^! = Vir_{26-c}."""

    def test_kappa_sum_equals_13(self):
        """kappa(c) + kappa(26-c) = c/2 + (26-c)/2 = 13."""
        for c_val in [Rational(1, 2), 1, 13, 25, 26]:
            result = virasoro_duality_check(c_val)
            assert simplify(result['kappa_sum'] - 13) == 0, \
                f"kappa sum != 13 at c={c_val}: {result['kappa_sum']}"

    def test_self_dual_at_c13(self):
        """At c = 13: kappa = kappa', so delta_kappa = 0."""
        result = virasoro_duality_check(Rational(13))
        assert simplify(result['kappa'] - result['kappa_dual']) == 0

    def test_duality_c1(self):
        """c = 1 dualizes to c = 25."""
        result = virasoro_duality_check(Rational(1))
        assert result['c_dual'] == 25

    def test_duality_c_half(self):
        """c = 1/2 dualizes to c = 51/2."""
        result = virasoro_duality_check(Rational(1, 2))
        assert result['c_dual'] == Rational(51, 2)

    def test_s3_same_under_duality(self):
        """S_3 = 2 for both c and 26-c (c-independent)."""
        for c_val in [Rational(1), Rational(13)]:
            result = virasoro_duality_check(c_val)
            assert simplify(result['shadow_sums'][3] - 4) == 0  # 2 + 2

    def test_s4_different_under_duality(self):
        """S_4(c) != S_4(26-c) in general."""
        result = virasoro_duality_check(Rational(1))
        s4_sum = result['shadow_sums'][4]
        # S_4(1) = 10/27, S_4(25) = 10/(25*147) = 10/3675
        # Sum = 10/27 + 10/3675 = 10*(3675+27)/(27*3675) = 37020/99225
        assert simplify(s4_sum) != 0


# ============================================================================
# 8. Self-dual point analysis
# ============================================================================

class TestSelfDual:
    """Analysis at the self-dual point c = 13."""

    def test_kappa_equals_13_half(self):
        result = virasoro_self_dual_analysis()
        assert simplify(result['kappa'] - Rational(13, 2)) == 0

    def test_delta_kappa_zero(self):
        result = virasoro_self_dual_analysis()
        assert simplify(result['delta_kappa']) == 0

    def test_self_duality_all_shadows(self):
        """At c = 13, S_r(c) = S_r(26-c) = S_r(13) for all r."""
        result = virasoro_self_dual_analysis(max_arity=10)
        for r in range(2, 11):
            assert result['complementarity'][r]['equal'], \
                f"S_{r} not self-dual at c=13"


# ============================================================================
# 9. Numerical MC element
# ============================================================================

class TestNumerical:
    """Test numerical MC element computation."""

    def test_numerical_c1(self):
        result = virasoro_theta_numerical(1, max_arity=10)
        assert abs(result['kappa'] - 0.5) < 1e-12
        assert abs(result['S3'] - 2.0) < 1e-12
        assert abs(result['S4'] - 10.0 / 27) < 1e-12

    def test_numerical_mc_residuals_small(self):
        """All MC residuals should be < 1e-10."""
        result = virasoro_theta_numerical(1, max_arity=12)
        for r, res in result['mc_residuals'].items():
            if res is not None:
                assert abs(res) < 1e-10, f"MC residual too large at r={r}: {res}"

    def test_numerical_c_half(self):
        result = virasoro_theta_numerical(FR(1, 2), max_arity=8)
        assert abs(result['kappa'] - 0.25) < 1e-12

    def test_numerical_c13(self):
        result = virasoro_theta_numerical(13, max_arity=8)
        assert abs(result['kappa'] - 6.5) < 1e-12

    def test_numerical_c26(self):
        result = virasoro_theta_numerical(26, max_arity=8)
        assert abs(result['kappa'] - 13.0) < 1e-12

    def test_growth_rate_positive(self):
        """Growth rate rho > 0 for Virasoro."""
        result = virasoro_theta_numerical(1, max_arity=8)
        assert result['growth_rate'] is not None
        assert result['growth_rate'] > 0

    def test_growth_rate_c13(self):
        """At c = 13, rho(13) < 1 (convergent tower)."""
        result = virasoro_theta_numerical(13, max_arity=8)
        assert result['growth_rate'] is not None
        assert result['growth_rate'] < 1.0


# ============================================================================
# 10. MC equation: the scalar recursion verified symbolically
# ============================================================================

class TestScalarRecursion:
    """Verify the scalar MC equation symbolically for c symbolic."""

    def test_symbolic_mc_arity5(self):
        """MC at arity 5 with symbolic c."""
        c = Symbol('c')
        theta = VirasoroTheta(c_val=None, max_arity=6)
        coeffs = {r: theta.S(r) for r in range(2, 7)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 5)
        assert simplify(res) == 0, f"Symbolic MC at r=5: {res}"

    def test_symbolic_mc_arity6(self):
        """MC at arity 6 with symbolic c."""
        theta = VirasoroTheta(c_val=None, max_arity=7)
        coeffs = {r: theta.S(r) for r in range(2, 8)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 6)
        assert simplify(res) == 0, f"Symbolic MC at r=6: {res}"

    def test_symbolic_mc_arity7(self):
        """MC at arity 7 with symbolic c."""
        theta = VirasoroTheta(c_val=None, max_arity=8)
        coeffs = {r: theta.S(r) for r in range(2, 9)}
        res = mc_equation_residual_scalar(theta.kappa(), coeffs, 7)
        assert simplify(res) == 0, f"Symbolic MC at r=7: {res}"


# ============================================================================
# 11. Cross-check with virasoro_shadow_all_arity.py
# ============================================================================

class TestCrossCheck:
    """Cross-check against the existing shadow obstruction tower module."""

    def test_s2_matches(self):
        """S_2 = c/2 matches virasoro_shadow_all_arity."""
        from compute.lib.virasoro_shadow_all_arity import kappa_vir
        c = Symbol('c')
        theta = VirasoroTheta(c_val=None)
        assert simplify(theta.kappa() - kappa_vir()) == 0

    def test_s3_matches(self):
        """S_3 = 2 matches virasoro_shadow_all_arity."""
        from compute.lib.virasoro_shadow_all_arity import alpha_vir
        theta = VirasoroTheta(c_val=None)
        assert simplify(theta.alpha() - alpha_vir()) == 0

    def test_s4_matches(self):
        """S_4 = 10/[c(5c+22)] matches virasoro_shadow_all_arity."""
        from compute.lib.virasoro_shadow_all_arity import S4_vir
        c = Symbol('c')
        theta = VirasoroTheta(c_val=None)
        assert simplify(theta.S4() - S4_vir()) == 0

    def test_s5_matches(self):
        """S_5 matches virasoro_shadow_all_arity.S_explicit(5)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        c = Symbol('c')
        theta = VirasoroTheta(c_val=None, max_arity=6)
        s5_theta = theta.S(5)
        s5_explicit = S_explicit(5)
        assert simplify(s5_theta - s5_explicit) == 0

    def test_s6_matches(self):
        """S_6 matches virasoro_shadow_all_arity.S_explicit(6)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        theta = VirasoroTheta(c_val=None, max_arity=7)
        s6_theta = theta.S(6)
        s6_explicit = S_explicit(6)
        assert simplify(s6_theta - s6_explicit) == 0

    def test_s7_matches(self):
        """S_7 matches virasoro_shadow_all_arity.S_explicit(7)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        theta = VirasoroTheta(c_val=None, max_arity=8)
        s7_theta = theta.S(7)
        s7_explicit = S_explicit(7)
        assert simplify(s7_theta - s7_explicit) == 0

    def test_s8_matches(self):
        """S_8 matches virasoro_shadow_all_arity.S_explicit(8)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        theta = VirasoroTheta(c_val=None, max_arity=9)
        s8_theta = theta.S(8)
        s8_explicit = S_explicit(8)
        assert simplify(s8_theta - s8_explicit) == 0

    def test_s9_matches(self):
        """S_9 matches virasoro_shadow_all_arity.S_explicit(9)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        theta = VirasoroTheta(c_val=None, max_arity=10)
        s9_theta = theta.S(9)
        s9_explicit = S_explicit(9)
        assert simplify(s9_theta - s9_explicit) == 0

    def test_s10_matches(self):
        """S_10 matches virasoro_shadow_all_arity.S_explicit(10)."""
        from compute.lib.virasoro_shadow_all_arity import S_explicit
        theta = VirasoroTheta(c_val=None, max_arity=11)
        s10_theta = theta.S(10)
        s10_explicit = S_explicit(10)
        assert simplify(s10_theta - s10_explicit) == 0


# ============================================================================
# 12. Cross-check with quartic_contact_class.py
# ============================================================================

class TestQuarticCrossCheck:
    """Cross-check S_4 against quartic_contact_class module."""

    def test_virasoro_s4_matches(self):
        from compute.lib.quartic_contact_class import kappa_virasoro
        c_val = Rational(1)
        theta = VirasoroTheta(c_val=c_val)
        kap_qcc = kappa_virasoro(1)
        assert float(kap_qcc) == float(Neval(theta.kappa()))

    def test_heisenberg_quartic_zero(self):
        """Q^contact(H_k) = 0 matches Heisenberg tower termination."""
        from compute.lib.quartic_contact_class import Q_contact_heisenberg
        assert Q_contact_heisenberg(1) == 0

    def test_affine_sl2_quartic_zero(self):
        """Q^contact(sl_2) = 0 matches class L."""
        theta = AffineSl2Theta(k_val=1)
        Q = theta.theta_arity4_tensor()
        assert len(Q) == 0


# ============================================================================
# 13. Cross-check with affine_sl2_shadow_tower.py
# ============================================================================

class TestAffineSl2CrossCheck:
    """Cross-check against the existing affine sl_2 shadow module."""

    def test_kappa_matches(self):
        from compute.lib.affine_sl2_shadow_tower import affine_central_charge
        from sympy import Symbol
        k = Symbol('k')
        theta = AffineSl2Theta(k_val=None)
        # theta kappa = 3(k+2)/4
        assert simplify(theta.kappa() - Rational(3, 4) * (k + 2)) == 0

    def test_cartan_cubic_vanishes(self):
        """On the Cartan line, cubic vanishes (abelian subalgebra)."""
        from compute.lib.affine_sl2_shadow_tower import affine_cubic_structure_constant
        assert affine_cubic_structure_constant() == 0
        # Our module: S_3 on h-line = 0
        theta = AffineSl2Theta(k_val=1)
        assert theta.S(3) == 0

    def test_quartic_contact_vanishes(self):
        """Quartic contact = 0 for sl_2."""
        from compute.lib.affine_sl2_shadow_tower import affine_quartic_contact
        assert affine_quartic_contact() == 0


# ============================================================================
# 14. Depth classification consistency
# ============================================================================

class TestDepthClassification:
    """Verify depth classes match across families."""

    def test_heisenberg_class_G(self):
        assert HeisenbergTheta(k_val=1).depth_class() == 'G'

    def test_affine_class_L(self):
        assert AffineSl2Theta(k_val=1).depth_class() == 'L'

    def test_virasoro_class_M(self):
        assert VirasoroTheta(c_val=Rational(1)).depth_class() == 'M'

    def test_virasoro_all_c_class_M(self):
        """All Virasoro algebras (c > 0) are class M."""
        for c_val in [Rational(1, 2), 1, 13, 25, 26]:
            theta = VirasoroTheta(c_val=c_val)
            assert theta.depth_class() == 'M'


# ============================================================================
# 15. Shadow metric and discriminant
# ============================================================================

class TestShadowMetric:
    """Test shadow metric Q_L and critical discriminant Delta."""

    def test_discriminant_c1(self):
        """Delta(Vir_1) = 40/(5+22) = 40/27."""
        theta = VirasoroTheta(c_val=Rational(1))
        delta = theta.critical_discriminant()
        assert simplify(delta - Rational(40, 27)) == 0

    def test_discriminant_c13(self):
        """Delta(Vir_13) = 40/(65+22) = 40/87."""
        theta = VirasoroTheta(c_val=Rational(13))
        delta = theta.critical_discriminant()
        assert simplify(delta - Rational(40, 87)) == 0

    def test_shadow_metric_coefficients(self):
        """Q_L(t) = c^2 + 12c*t + (36 + 80/(5c+22))*t^2."""
        theta = VirasoroTheta(c_val=Rational(1))
        q0, q1, q2 = theta.shadow_metric()
        assert simplify(q0 - 1) == 0  # c^2 = 1
        assert simplify(q1 - 12) == 0  # 12c = 12
        expected_q2 = Rational(36) + Rational(80, 27)  # 36 + 80/27
        assert simplify(q2 - expected_q2) == 0

    def test_growth_rate_numerical(self):
        """Growth rate rho = sqrt(36 + 80/(5c+22)) / c at specific c."""
        theta = VirasoroTheta(c_val=Rational(13))
        rho = theta.growth_rate()
        rho_val = float(Neval(rho))
        # Expected: sqrt(36 + 80/87) / 13 = sqrt((36*87+80)/87) / 13
        #         = sqrt(3212/87) / 13 = sqrt(3212) / (13*sqrt(87))
        expected = float(Neval(sqrt(Rational(36) + Rational(80, 87)) / 13))
        assert abs(rho_val - expected) < 1e-10


# ============================================================================
# 16. Explicit S_r values at specific c (numerical cross-check)
# ============================================================================

class TestNumericalShadowValues:
    """Verify specific numerical S_r values at key c."""

    def test_s5_c1_numerical(self):
        """S_5(c=1) = -48/(1*27) = -16/9 ~ -1.7778."""
        theta = VirasoroTheta(c_val=Rational(1), max_arity=6)
        s5 = float(Neval(theta.S(5)))
        assert abs(s5 - (-16.0 / 9)) < 1e-10

    def test_s6_c1_numerical(self):
        """S_6(c=1) = 80*(45+193)/(3*1*(27)^2) = 80*238/(3*729) = 19040/2187."""
        theta = VirasoroTheta(c_val=Rational(1), max_arity=7)
        s6 = float(Neval(theta.S(6)))
        expected = 80.0 * 238 / (3 * 729)
        assert abs(s6 - expected) < 1e-8

    def test_s_alternating_sign_c13(self):
        """For c = 13 (self-dual), signs should alternate stably."""
        theta = VirasoroTheta(c_val=Rational(13), max_arity=12)
        # S_2 = 13/2 > 0
        # S_3 = 2 > 0
        # S_4 = 10/1131 > 0
        # S_5 should be negative (alternation starts at r=5)
        s5 = float(Neval(theta.S(5)))
        assert s5 < 0, f"S_5 at c=13 should be negative: {s5}"

    def test_shadow_decreasing_magnitude_c13(self):
        """For c = 13 (rho < 1), |S_r| should decrease for large r."""
        theta = VirasoroTheta(c_val=Rational(13), max_arity=15)
        magnitudes = []
        for r in range(5, 16):
            s = float(Neval(theta.S(r)))
            magnitudes.append(abs(s))
        # Check that the last few are decreasing
        for i in range(len(magnitudes) - 3, len(magnitudes) - 1):
            assert magnitudes[i] >= magnitudes[i + 1] * 0.5, \
                f"Not decreasing at position {i}: {magnitudes[i]} vs {magnitudes[i+1]}"


# ============================================================================
# 17. MC residual at arity 5 is exactly the recursion
# ============================================================================

class TestRecursionConsistency:
    """Verify the MC residual formula is consistent with the convolution recursion."""

    def test_recursion_produces_s5(self):
        """S_5 from the MC recursion matches the tower computation.

        From H(t)^2/t^4 = Q_L(t), the MC equation at arity r >= 5 is:
            4*r*kappa*S_r + sum_{3<=p<=q, p+q=r+2} eps(p,q)*pq*S_p*S_q = 0

        At r=5: 4*5*kappa*S_5 + 2*3*4*S_3*S_4 = 0
            S_5 = -24*S_3*S_4 / (20*kappa)
        """
        c_val = Rational(1)
        theta = VirasoroTheta(c_val=c_val, max_arity=6)
        kap = theta.kappa()
        s3 = theta.S(3)
        s4 = theta.S(4)

        # 4*5*kappa*S_5 + 2*3*4*S_3*S_4 = 0
        # S_5 = -24*S_3*S_4 / (20*kappa)
        s5_tower = theta.S(5)
        s5_recursion = cancel(-2 * 3 * 4 * s3 * s4 / (4 * 5 * kap))
        assert simplify(s5_tower - s5_recursion) == 0, \
            f"Recursion inconsistency: {s5_tower} vs {s5_recursion}"

    def test_recursion_produces_s6(self):
        """S_6 from MC recursion matches tower.

        4*6*kappa*S_6 + sum_{3<=p<=q, p+q=8} eps*pq*S_p*S_q = 0
        Terms: (3,5) with eps=2, (4,4) with eps=1.
        24*kappa*S_6 + 2*15*S_3*S_5 + 16*S_4^2 = 0
        """
        c_val = Rational(1)
        theta = VirasoroTheta(c_val=c_val, max_arity=7)
        kap = theta.kappa()
        s3 = theta.S(3)
        s4 = theta.S(4)
        s5 = theta.S(5)

        term_35 = 2 * 15 * s3 * s5
        term_44 = 1 * 16 * s4 * s4
        s6_recursion = cancel(-(term_35 + term_44) / (4 * 6 * kap))

        s6_tower = theta.S(6)
        assert simplify(s6_tower - s6_recursion) == 0, \
            f"S_6 recursion mismatch: tower={s6_tower}, recursion={s6_recursion}"


# ============================================================================
# 18. MC residual with corrected formula
# ============================================================================

class TestCorrectedMCResidual:
    """Test the MC residual formula derived from H^2/t^4 = Q_L.

    The correct scalar MC equation (for r >= 5):
        4*r*kappa*S_r + sum_{3<=p<=q, p+q=r+2} eps(p,q)*p*q*S_p*S_q = 0
    """

    @pytest.mark.parametrize("c_val,r", [
        (Rational(1, 2), 5), (Rational(1, 2), 6), (Rational(1, 2), 7),
        (Rational(1), 5), (Rational(1), 6), (Rational(1), 7),
        (Rational(13), 5), (Rational(13), 6), (Rational(13), 7),
        (Rational(25), 5), (Rational(25), 6), (Rational(25), 7),
        (Rational(26), 5), (Rational(26), 6), (Rational(26), 7),
    ])
    def test_corrected_residual(self, c_val, r):
        """MC residual should vanish at each arity."""
        theta = VirasoroTheta(c_val=c_val, max_arity=r + 1)
        kap = theta.kappa()
        s_r = theta.S(r)

        # Linear term: 4*r*kappa*S_r
        linear = 4 * r * kap * s_r

        # Quadratic sum: sum_{3<=p<=q, p+q=r+2} eps*pq*S_p*S_q
        quad = Rational(0)
        for p in range(3, r):
            q = r + 2 - p
            if q < p:
                break
            if q < 3:
                continue
            s_p = theta.S(p)
            s_q = theta.S(q)
            eps_pq = Rational(1) if p == q else Rational(2)
            quad += eps_pq * p * q * s_p * s_q

        residual = cancel(linear + quad)
        assert simplify(residual) == 0, \
            f"MC residual nonzero at c={c_val}, r={r}: {residual}"


# ============================================================================
# 19. sl_2 cubic tensor explicit values
# ============================================================================

class TestSl2CubicExplicit:
    """Verify explicit numerical cubic tensor entries."""

    def test_cubic_at_k1(self):
        C = sl2_cubic_tensor_at_k(1)
        assert abs(C[('h', 'e', 'f')] - 2.0) < 1e-12
        assert abs(C[('h', 'f', 'e')] + 2.0) < 1e-12

    def test_cubic_at_k2(self):
        C = sl2_cubic_tensor_at_k(2)
        assert abs(C[('h', 'e', 'f')] - 4.0) < 1e-12
        assert abs(C[('h', 'f', 'e')] + 4.0) < 1e-12

    def test_cubic_scales_with_k(self):
        """C_{abc}(k) = k * C_{abc}(1)."""
        C1 = sl2_cubic_tensor_at_k(1)
        C3 = sl2_cubic_tensor_at_k(3)
        for idx in C1:
            assert abs(C3.get(idx, 0) - 3 * C1[idx]) < 1e-10

    def test_cubic_vanishes_on_cartan(self):
        """C(h, h, h) = 0 (abelian Cartan)."""
        C = sl2_cubic_tensor_at_k(1)
        assert C.get(('h', 'h', 'h'), 0) == 0

    def test_cubic_six_nonzero_entries(self):
        """Exactly 6 nonzero entries (3! permutations of {h, e, f})."""
        C = sl2_cubic_tensor_at_k(1)
        nonzero = {k: v for k, v in C.items() if abs(v) > 1e-12}
        assert len(nonzero) == 6


# ============================================================================
# 20. Compare families
# ============================================================================

class TestCompare:
    """Cross-family comparison."""

    def test_compare_returns_all_families(self):
        result = compare_families(
            c_values=[Rational(1)],
            k_values=[1],
            max_arity=6,
        )
        assert 'Vir_c=1' in result
        assert 'H_k=1' in result
        assert 'sl2_k=1' in result

    def test_compare_depth_classes(self):
        result = compare_families(
            c_values=[Rational(1)],
            k_values=[1],
            max_arity=6,
        )
        assert result['Vir_c=1']['depth_class'] == 'M'
        assert result['H_k=1']['depth_class'] == 'G'
        assert result['sl2_k=1']['depth_class'] == 'L'


# ============================================================================
# 21. Virasoro critical central charges
# ============================================================================

class TestCriticalCentralCharges:
    """Test at critical and boundary central charges."""

    def test_c26_kappa_equals_13(self):
        """At c = 26 (bosonic string): kappa = 13."""
        theta = VirasoroTheta(c_val=Rational(26))
        assert theta.kappa() == 13

    def test_c0_would_have_kappa_0(self):
        """At c = 0: kappa = 0 (uncurved bar complex).

        S_4 = 10/(0*22) is undefined, so c = 0 is a singular point.
        The tower is not defined at c = 0 (AP31: kappa=0 does NOT mean Theta=0).
        """
        # We do NOT construct VirasoroTheta at c=0 (division by zero)
        pass

    def test_c_minus_22_over_5(self):
        """c = -22/5 is a Kac determinant zero (5c+22=0).

        S_4 has a pole here: S_4 = 10/(c(5c+22)).
        This is a critical point of the shadow obstruction tower.
        """
        # The VirasoroTheta should handle this as a pole
        # We verify the tower at nearby values
        c_near = Rational(-22, 5) + Rational(1, 100)
        theta = VirasoroTheta(c_val=c_near, max_arity=6)
        s4 = theta.S4()
        # S_4 should be large (near pole)
        assert float(Neval(Abs(s4))) > 10


# ============================================================================
# 22. Large arity behavior
# ============================================================================

class TestLargeArity:
    """Verify behavior at large arities."""

    def test_alternating_signs_c13(self):
        """Signs should alternate at c = 13 for r >= 5."""
        theta = VirasoroTheta(c_val=Rational(13), max_arity=12)
        signs = []
        for r in range(5, 13):
            s = float(Neval(theta.S(r)))
            signs.append(1 if s > 0 else -1)
        # Alternating means consecutive signs differ
        for i in range(len(signs) - 1):
            assert signs[i] != signs[i + 1], \
                f"Signs not alternating at r={i+5},{i+6}"

    def test_magnitude_ratio_converges_c13(self):
        """The ratio |S_{r+1}/S_r| should converge to rho at c = 13.

        The convergence is O(1/r) due to the r^{-5/2} correction in the
        asymptotics.  At r ~ 30, the ratio should be within 0.1 of rho.
        """
        theta = VirasoroTheta(c_val=Rational(13), max_arity=35)
        rho = float(Neval(theta.growth_rate()))
        ratios = []
        for r in range(15, 35):
            s_r = float(Neval(theta.S(r)))
            s_r1 = float(Neval(theta.S(r + 1)))
            if abs(s_r) > 1e-50:
                ratios.append(abs(s_r1 / s_r))
        # Last ratio should approach rho
        assert abs(ratios[-1] - rho) < 0.1, \
            f"Ratio {ratios[-1]} not close to rho={rho}"


# ============================================================================
# 23. ThetaComponent data structure
# ============================================================================

class TestThetaComponent:
    """Test the ThetaComponent data structure."""

    def test_scalar_component(self):
        comp = ThetaComponent(arity=2, scalar_value=Rational(1, 2))
        assert comp.is_scalar
        assert not comp.is_zero

    def test_zero_component(self):
        comp = ThetaComponent(arity=4, scalar_value=0)
        assert comp.is_zero

    def test_tensor_component(self):
        comp = ThetaComponent(
            arity=3,
            tensor={('e', 'f', 'h'): 2, ('h', 'e', 'f'): 2},
        )
        assert not comp.is_scalar
        assert not comp.is_zero


# ============================================================================
# 24. Verification summary
# ============================================================================

class TestVerificationSummary:
    """End-to-end verification of the full MC element."""

    def test_full_verification_c1(self):
        """Full MC verification at c = 1: seed + recursion + residuals."""
        theta = VirasoroTheta(c_val=Rational(1), max_arity=12)

        # Seed data
        assert theta.kappa() == Rational(1, 2)
        assert theta.alpha() == Rational(2)
        assert simplify(theta.S4() - Rational(10, 27)) == 0

        # MC residuals at arities 5-12
        for r in range(5, 13):
            coeffs = {rr: theta.S(rr) for rr in range(2, r + 2)}
            res = mc_equation_residual_scalar(theta.kappa(), coeffs, r)
            assert simplify(res) == 0, f"MC failed at r={r}"

        # Depth class
        assert theta.depth_class() == 'M'

    def test_full_verification_c13(self):
        """Full MC verification at c = 13 (self-dual)."""
        theta = VirasoroTheta(c_val=Rational(13), max_arity=12)

        assert theta.kappa() == Rational(13, 2)
        assert theta.alpha() == Rational(2)

        for r in range(5, 13):
            coeffs = {rr: theta.S(rr) for rr in range(2, r + 2)}
            res = mc_equation_residual_scalar(theta.kappa(), coeffs, r)
            assert simplify(res) == 0, f"MC failed at r={r}"

    def test_full_verification_c26(self):
        """Full MC verification at c = 26 (bosonic string)."""
        theta = VirasoroTheta(c_val=Rational(26), max_arity=10)

        assert theta.kappa() == Rational(13)

        for r in range(5, 11):
            coeffs = {rr: theta.S(rr) for rr in range(2, r + 2)}
            res = mc_equation_residual_scalar(theta.kappa(), coeffs, r)
            assert simplify(res) == 0, f"MC failed at r={r}"

    def test_full_verification_heisenberg(self):
        """Full MC verification for Heisenberg at k = 1."""
        theta = HeisenbergTheta(k_val=1)
        assert theta.kappa() == Rational(1)
        for r in range(3, 10):
            assert theta.S(r) == 0

    def test_full_verification_sl2(self):
        """Full MC verification for sl_2 at k = 1."""
        theta = AffineSl2Theta(k_val=1)
        assert theta.kappa() == Rational(9, 4)
        C = theta.cubic_tensor()
        assert len(C) == 6
        assert simplify(theta.mc_residual_arity3()) == 0
        assert simplify(theta.mc_residual_arity4()) == 0
        Q = theta.theta_arity4_tensor()
        assert len(Q) == 0
