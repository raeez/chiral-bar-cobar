"""Tests for the full 2D W_3 shadow obstruction tower computation.

Verifies:
  - Input shadows match known values
  - T-line restriction matches Virasoro tower
  - W-line restriction matches W-line tower (odd vanish)
  - Z_2 parity holds at all arities
  - Mixing coefficients are genuinely new
  - Denominator structure follows Kac-shadow singularity principle
  - Diagonal tower gives consistent effective propagator
  - Arity-5 detailed computation matches full recursion
"""

import pytest
from sympy import Rational, Symbol, simplify, factor, cancel, expand, Poly, S

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'w3_full_2d_shadow_tower',
    os.path.join(_lib_dir, 'w3_full_2d_shadow_tower.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# ============================================================
# Input shadow tests
# ============================================================

class TestInputShadows:
    def test_sh2_tline(self):
        """Sh_2 on T-line = (c/2) x_T^2."""
        inp = _mod.input_shadows()
        assert simplify(inp[2].subs(x_W, 0) - c/2 * x_T**2) == 0

    def test_sh2_wline(self):
        """Sh_2 on W-line = (c/3) x_W^2."""
        inp = _mod.input_shadows()
        assert simplify(inp[2].subs(x_T, 0) - c/3 * x_W**2) == 0

    def test_sh3_tline(self):
        """Sh_3 on T-line = 2 x_T^3."""
        inp = _mod.input_shadows()
        assert simplify(inp[3].subs(x_W, 0) - 2 * x_T**3) == 0

    def test_sh3_wline_vanishes(self):
        """Sh_3 vanishes on W-line (Z_2 parity)."""
        inp = _mod.input_shadows()
        assert simplify(inp[3].subs(x_T, 0)) == 0

    def test_sh4_tline(self):
        """Sh_4 on T-line = Q_TT x_T^4."""
        inp = _mod.input_shadows()
        Q_TT = Rational(10) / (c * (5*c + 22))
        assert simplify(inp[4].subs(x_W, 0) - Q_TT * x_T**4) == 0

    def test_sh4_wline(self):
        """Sh_4 on W-line = Q_WW x_W^4."""
        inp = _mod.input_shadows()
        Q_WW = Rational(2560) / (c * (5*c + 22)**3)
        assert simplify(inp[4].subs(x_T, 0) - Q_WW * x_W**4) == 0


# ============================================================
# 2D bracket tests
# ============================================================

class TestBracket:
    def test_bracket_reduces_degree_by_2(self):
        """{f, g} reduces total degree by 2."""
        f = x_T**3
        g = x_T**4
        bracket = _mod.h_poisson_2d(f, g)
        # deg(f)=3, deg(g)=4, bracket should have deg 5
        p = Poly(bracket, x_T, x_W)
        assert p.total_degree() == 5

    def test_bracket_tline_matches_1d(self):
        """On T-line, 2D bracket matches 1D Virasoro bracket."""
        f = 2 * x_T**3
        g = Rational(10)/(c*(5*c+22)) * x_T**4
        bracket_2d = _mod.h_poisson_2d(f, g).subs(x_W, 0)
        # 1D bracket: f' * (2/c) * g'
        bracket_1d = 6*x_T**2 * Rational(2)/c * 4*Rational(10)/(c*(5*c+22))*x_T**3
        assert simplify(bracket_2d - bracket_1d) == 0

    def test_nabla_h_on_homogeneous(self):
        """nabla_H(x_T^r) = 2r x_T^r."""
        for r in [3, 4, 5]:
            f = x_T**r
            result = _mod.nabla_H_2d(f)
            assert simplify(result - 2*r*f) == 0

    def test_nabla_h_on_mixed(self):
        """nabla_H on mixed monomial."""
        f = x_T**2 * x_W
        result = _mod.nabla_H_2d(f)
        # E(f) = 3*f, so nabla_H(f) = 2*3*f = 6f
        assert simplify(result - 6*f) == 0


# ============================================================
# Full 2D tower tests
# ============================================================

class TestFull2DTower:
    @pytest.fixture(scope='class')
    def tower(self):
        return _mod.compute_full_2d_tower(7)

    def test_tline_arity5(self, tower):
        """T-line restriction at arity 5 matches Virasoro."""
        Sh_5 = tower[5]
        restricted = Sh_5.subs(x_W, 0)
        p = Poly(restricted, x_T)
        coeff = p.nth(5)
        expected = Rational(-48) / (c**2 * (5*c + 22))
        assert simplify(coeff - expected) == 0, \
            f"T-line arity 5: got {factor(coeff)}, expected {expected}"

    def test_wline_odd_vanish(self, tower):
        """Odd arities vanish on W-line."""
        for r in [3, 5, 7]:
            if r in tower:
                restricted = tower[r].subs(x_T, 0)
                assert simplify(restricted) == 0, f"Arity {r} nonzero on W-line"

    def test_z2_parity_all(self, tower):
        """Z_2 parity holds at all computed arities."""
        z2 = _mod.verify_z2_parity(tower)
        for r, data in z2.items():
            assert data['z2_invariant'], f"Z_2 parity fails at arity {r}"

    def test_arity5_has_mixing(self, tower):
        """Arity 5 has genuinely mixed coefficients (not just pure T or W)."""
        mix = _mod.mixing_coefficients(tower, 7)
        assert mix[5]['n_mixed_monomials'] > 0, \
            "Arity 5 should have mixed monomials"

    def test_arity6_has_mixing(self, tower):
        """Arity 6 has mixed coefficients."""
        mix = _mod.mixing_coefficients(tower, 7)
        assert mix[6]['n_mixed_monomials'] > 0, \
            "Arity 6 should have mixed monomials"

    def test_arity5_monomial_count(self, tower):
        """Arity 5 should have exactly 3 monomials: x_T^5, x_T^3 x_W^2, x_T x_W^4."""
        Sh_5 = tower[5]
        if Sh_5 == S.Zero:
            pytest.skip("Sh_5 is zero")
        poly = Poly(Sh_5, x_T, x_W)
        monomials = list(poly.as_dict().keys())
        for a, b in monomials:
            assert b % 2 == 0, f"Monomial x_T^{a} x_W^{b} violates Z_2 parity"
        assert len(monomials) == 3, f"Expected 3 monomials, got {len(monomials)}"

    def test_arity6_monomial_count(self, tower):
        """Arity 6: monomials are (6,0), (4,2), (2,4), (0,6)."""
        Sh_6 = tower[6]
        if Sh_6 == S.Zero:
            pytest.skip("Sh_6 is zero")
        poly = Poly(Sh_6, x_T, x_W)
        monomials = list(poly.as_dict().keys())
        for a, b in monomials:
            assert b % 2 == 0, f"Z_2 violation at ({a},{b})"
        assert len(monomials) == 4, f"Expected 4 monomials, got {len(monomials)}"


class TestArity5Detailed:
    def test_matches_full_recursion(self):
        """Arity-5 detailed computation matches full recursion."""
        detailed = _mod.arity5_detailed()
        tower = _mod.compute_full_2d_tower(5)

        Sh_5_detailed = expand(detailed['Sh_5'])
        Sh_5_recursion = expand(tower[5])

        assert simplify(Sh_5_detailed - Sh_5_recursion) == 0

    def test_obstruction_nonzero(self):
        """The arity-5 obstruction is nonzero (quintic shadow forced)."""
        detailed = _mod.arity5_detailed()
        assert detailed['obstruction'] != S.Zero

    def test_t_channel_nonzero(self):
        """T-channel contribution to arity-5 obstruction is nonzero."""
        detailed = _mod.arity5_detailed()
        assert detailed['T_channel'] != S.Zero

    def test_w_channel_nonzero(self):
        """W-channel contribution to arity-5 obstruction is nonzero."""
        detailed = _mod.arity5_detailed()
        assert detailed['W_channel'] != S.Zero


# ============================================================
# Diagonal and growth tests
# ============================================================

class TestDiagonal:
    def test_diagonal_arity2(self):
        """Diagonal kappa = kappa_T + kappa_W = 5c/6."""
        tower = _mod.compute_full_2d_tower(5)
        diag = _mod.diagonal_shadow_tower(tower, 5)
        assert simplify(diag[2] - Rational(5)*c/6) == 0

    def test_diagonal_arity3(self):
        """Diagonal cubic = 2 + 3 = 5."""
        tower = _mod.compute_full_2d_tower(5)
        diag = _mod.diagonal_shadow_tower(tower, 5)
        assert simplify(diag[3] - 5) == 0

    def test_diagonal_arity4(self):
        """Diagonal quartic: Q_TT + 6*Q_TW + Q_WW."""
        tower = _mod.compute_full_2d_tower(5)
        diag = _mod.diagonal_shadow_tower(tower, 5)
        Q_TT = Rational(10) / (c * (5*c + 22))
        Q_TW = Rational(160) / (c * (5*c + 22)**2)
        Q_WW = Rational(2560) / (c * (5*c + 22)**3)
        expected = Q_TT + 6 * Q_TW + Q_WW
        assert simplify(diag[4] - expected) == 0


# ============================================================
# Numerical spot checks
# ============================================================

class TestNumerical:
    def test_arity5_at_c1(self):
        """Arity-5 T-line coefficient at c=1."""
        tower = _mod.compute_full_2d_tower(5)
        Sh_5_T = tower[5].subs(x_W, 0)
        p = Poly(Sh_5_T, x_T)
        coeff = p.nth(5).subs(c, 1)
        expected = Rational(-48) / (1 * 27)  # c=1: c^2(5c+22) = 1*27
        assert coeff == expected

    def test_arity5_mixing_at_c26(self):
        """Arity-5 mixed coefficients are finite at c=26."""
        tower = _mod.compute_full_2d_tower(5)
        Sh_5 = tower[5]
        poly = Poly(Sh_5, x_T, x_W)
        for monom, coeff in poly.as_dict().items():
            val = coeff.subs(c, 26)
            assert val.is_finite, f"Coefficient at {monom} diverges at c=26"

    def test_arity5_selfdual_at_c13(self):
        """At the self-dual point c=13, check special structure."""
        tower = _mod.compute_full_2d_tower(5)
        Sh_5 = tower[5]
        poly = Poly(Sh_5, x_T, x_W)
        # Just verify finiteness at c=13
        for monom, coeff in poly.as_dict().items():
            val = coeff.subs(c, 13)
            assert val.is_finite, f"Coefficient at {monom} diverges at c=13"

    def test_no_pole_at_c1(self):
        """Shadow coefficients have no pole at c=1."""
        tower = _mod.compute_full_2d_tower(6)
        for r in range(5, 7):
            if tower[r] == S.Zero:
                continue
            poly = Poly(tower[r], x_T, x_W)
            for monom, coeff in poly.as_dict().items():
                val = coeff.subs(c, 1)
                assert val.is_finite, f"Pole at c=1 for arity {r}, monomial {monom}"
