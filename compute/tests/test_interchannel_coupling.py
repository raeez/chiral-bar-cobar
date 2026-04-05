"""Tests for inter-channel coupling corrections.

Verifies the discovery that 1D projections of multi-generator shadow obstruction towers
receive coupling corrections from transverse channels.
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel, S

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'interchannel_coupling',
    os.path.join(_lib_dir, 'interchannel_coupling.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')
x_W = Symbol('x_W')


class TestNormalDerivatives:
    def test_sh2_normal_zero(self):
        """Sh_2 = (c/2)x_T^2 + (c/3)x_W^2 has dSh_2/dx_T|_{x_T=0} = 0."""
        from sympy import diff, Symbol
        x_T = Symbol('x_T')
        Sh_2 = c/2 * x_T**2 + c/3 * x_W**2
        nd = diff(Sh_2, x_T).subs(x_T, 0)
        assert nd == 0

    def test_sh3_normal_nonzero(self):
        """Sh_3 has nonzero normal derivative on W-line."""
        x_T = Symbol('x_T')
        Sh_3 = 2 * x_T**3 + 3 * x_T * x_W**2
        nd = _mod.normal_derivative_on_wline(Sh_3)
        assert nd != 0
        assert simplify(nd - 3 * x_W**2) == 0

    def test_sh4_normal_zero(self):
        """Sh_4 has zero normal derivative on W-line (even powers of x_T)."""
        x_T = Symbol('x_T')
        Q_TT = Rational(10) / (c * (5*c + 22))
        Q_TW = Rational(160) / (c * (5*c + 22)**2)
        Q_WW = Rational(2560) / (c * (5*c + 22)**3)
        Sh_4 = Q_TT * x_T**4 + 6 * Q_TW * x_T**2 * x_W**2 + Q_WW * x_W**4
        nd = _mod.normal_derivative_on_wline(Sh_4)
        assert simplify(nd) == 0


class TestArity6Correction:
    def test_correction_nonzero(self):
        """The arity-6 T-channel correction is nonzero."""
        a6 = _mod.arity6_correction_explicit()
        assert simplify(a6['shadow_correction']) != 0

    def test_correction_formula(self):
        """delta_6 = 576(5c+38)/[c^3(5c+22)^3]."""
        a6 = _mod.arity6_correction_explicit()
        expected = Rational(576) * (5*c + 38) / (c**3 * (5*c + 22)**3)
        assert simplify(a6['shadow_correction'] - expected) == 0

    def test_correction_finite_at_c1(self):
        """Correction is finite at c=1."""
        a6 = _mod.arity6_correction_explicit()
        val = a6['shadow_correction'].subs(c, 1)
        assert val.is_finite

    def test_correction_finite_at_c26(self):
        """Correction is finite at c=26."""
        a6 = _mod.arity6_correction_explicit()
        val = a6['shadow_correction'].subs(c, 26)
        assert val.is_finite

    def test_correction_pole_at_c0(self):
        """Correction has a pole at c=0."""
        a6 = _mod.arity6_correction_explicit()
        from sympy import limit, oo
        # Check that |correction| -> infinity as c -> 0
        val = a6['shadow_correction'].subs(c, Rational(1, 1000))
        assert abs(float(val)) > 1000

    def test_s14_coefficient(self):
        """S_{1,4} = -1152(5c+38)/[c^2(5c+22)^3]."""
        a6 = _mod.arity6_correction_explicit()
        expected = Rational(-1152) * (5*c + 38) / (c**2 * (5*c + 22)**3)
        assert simplify(a6['S_14'] - expected) == 0


class TestAutonomy:
    def test_tline_autonomous(self):
        """T-line is autonomous."""
        is_auto, _ = _mod.is_line_autonomous((1, 0))
        assert is_auto

    def test_wline_not_autonomous(self):
        """W-line is NOT autonomous."""
        is_auto, _ = _mod.is_line_autonomous((0, 1))
        assert not is_auto


class TestNormalDerivativeTower:
    def test_even_arities_zero(self):
        """Even-arity shadows have zero normal derivative on W-line."""
        ndt = _mod.normal_derivative_tower(8)
        for r in [2, 4, 6, 8]:
            if r in ndt:
                assert ndt[r]['zero'], f"Arity {r} should have zero normal deriv"

    def test_odd_arities_nonzero(self):
        """Odd-arity shadows have nonzero normal derivative on W-line."""
        ndt = _mod.normal_derivative_tower(8)
        for r in [3, 5, 7]:
            if r in ndt:
                assert not ndt[r]['zero'], f"Arity {r} should have nonzero normal deriv"

    def test_arity3_normal_deriv(self):
        """dSh_3/dx_T|_{W-line} = 3 x_W^2."""
        ndt = _mod.normal_derivative_tower(4)
        assert 2 in ndt[3]['coefficients']
        assert ndt[3]['coefficients'][2] == 3


class TestTChannelBracket:
    def test_same_function_t_channel(self):
        """T-channel of {f, f} is nonneg (being a square)."""
        f = 2 * _mod.x_T**3 + 3 * _mod.x_T * x_W**2
        t_bracket = _mod.t_channel_bracket_on_wline(f, f)
        # At x_T=0: (3 x_W^2)(2/c)(3 x_W^2) = 18 x_W^4 / c
        expected = 18 * x_W**4 / c
        assert simplify(t_bracket - expected) == 0
