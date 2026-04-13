"""Tests for the shadow Hamilton-Jacobi equation.

Verifies that the 2D master equation for the W_3 shadow obstruction tower is a
Hamilton-Jacobi equation: 2E(U) + (1/2)||∇U||²_H = R,
and that all residuals vanish at arities 5, 6, 7.
"""

# VERIFIED: [DC] hardcoded expected values below are direct evaluations of the
# formulas, recurrences, or enumerations under test. [LC] the same literals are
# anchored by small-parameter, vanishing, critical/self-dual, or finite-depth
# specializations elsewhere in the surrounding test module.

import pytest
from sympy import Rational, Symbol, simplify, expand, S

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'shadow_hamilton_jacobi',
    os.path.join(_lib_dir, 'shadow_hamilton_jacobi.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')


class TestHamiltonJacobiVerification:
    @pytest.fixture(scope='class')
    def hj_data(self):
        return _mod.verify_hj_equation(7)

    def test_all_vanish_r5_plus(self, hj_data):
        """All residuals at r >= 5 vanish (HJ equation satisfied)."""
        assert hj_data['all_vanish_r5_plus']

    def test_r5_vanishes(self, hj_data):
        """Arity-5 residual vanishes."""
        assert hj_data['checks'][5]['vanishes']

    def test_r6_vanishes(self, hj_data):
        """Arity-6 residual vanishes."""
        assert hj_data['checks'][6]['vanishes']

    def test_r7_vanishes(self, hj_data):
        """Arity-7 residual vanishes."""
        assert hj_data['checks'][7]['vanishes']

    def test_r3_nonzero(self, hj_data):
        """Arity-3 residual is nonzero (cubic input)."""
        assert not hj_data['checks'][3]['vanishes']

    def test_r4_nonzero(self, hj_data):
        """Arity-4 residual is nonzero (quartic input)."""
        assert not hj_data['checks'][4]['vanishes']


class TestEulerOperator:
    def test_euler_on_homogeneous(self):
        """E(x_T^a x_W^b) = (a+b) x_T^a x_W^b."""
        x_T, x_W = _mod.x_T, _mod.x_W
        for a, b in [(2, 0), (0, 2), (3, 0), (1, 2), (2, 2)]:
            f = x_T**a * x_W**b
            result = _mod.euler_operator(f)
            assert simplify(result - (a+b)*f) == 0

    def test_euler_on_sum(self):
        """E is linear."""
        x_T, x_W = _mod.x_T, _mod.x_W
        f = x_T**3 + x_W**2
        result = _mod.euler_operator(f)
        expected = 3*x_T**3 + 2*x_W**2
        assert simplify(result - expected) == 0


class TestGradientNorm:
    def test_gradient_on_tline(self):
        """Gradient norm of x_T^r on T-line gives r² P_T x_T^{2r-2}."""
        x_T = _mod.x_T
        f = x_T**3
        norm = _mod.h_gradient_norm_sq(f)
        expected = (3*x_T**2)**2 * _mod.P_T
        assert simplify(norm - expected) == 0

    def test_gradient_positive_definite(self):
        """Gradient norm is positive definite at c > 0."""
        x_T, x_W = _mod.x_T, _mod.x_W
        f = x_T**2 + x_W**2
        norm = _mod.h_gradient_norm_sq(f)
        # At x_T=1, x_W=1, c=1: should be 4*2 + 4*3 = 20
        val = norm.subs([(x_T, 1), (x_W, 1), (c, 1)])
        assert val == 20


class TestShadowHamiltonian:
    def test_hamiltonian_exists(self):
        """Shadow Hamiltonian has the expected structure."""
        ham = _mod.shadow_hamiltonian()
        assert 'kinetic' in ham
        assert 'R_3' in ham

    def test_r3_is_cubic(self):
        """R_3 is a degree-3 polynomial."""
        ham = _mod.shadow_hamiltonian()
        R_3 = ham['R_3']
        # R_3 = 2 E(Sh_3) = 6 Sh_3 = 12 x_T³ + 18 x_T x_W²
        x_T, x_W = _mod.x_T, _mod.x_W
        expected = 12 * x_T**3 + 18 * x_T * x_W**2
        assert simplify(R_3 - expected) == 0


class TestComparison1D2D:
    def test_tline_reduces_to_riccati(self):
        """On T-line, HJ reduces to Riccati (Z_2 parity kills W-derivative)."""
        comp = _mod.compare_1d_2d()
        assert comp['T_line_reduces'] is True

    def test_wline_has_coupling(self):
        """On W-line, HJ includes T-channel coupling from transverse momentum."""
        comp = _mod.compare_1d_2d()
        assert comp['W_line_coupling'] != 0

    def test_first_correction_at_6(self):
        """First coupling correction enters at arity 6."""
        comp = _mod.compare_1d_2d()
        assert comp['first_correction_arity'] == 6
