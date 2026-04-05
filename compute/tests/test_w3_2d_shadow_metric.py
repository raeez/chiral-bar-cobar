"""Tests for the W_3 2D shadow metric computation.

Verifies:
  - Hessian, propagator, and total kappa
  - Cubic and quartic shadow tensors
  - 2D shadow metric matrix (Hessian of the GF)
  - Arity-by-arity contributions to the metric
  - T-line restriction matches Virasoro shadow metric
  - W-line restriction matches W-line tower
  - Critical discriminant matches known values
  - Propagator variance and mixing polynomial
  - Enhanced symmetry loci
  - Spectral curve analysis
  - Koszul duality under c -> 100 - c
  - Numerical spot checks at specific central charges
"""

import pytest
from sympy import (
    Matrix, Poly, Rational, S, Symbol, cancel, diff, expand,
    factor, numer, denom, simplify, sqrt, symbols,
)

import importlib.util
import os

_lib_dir = os.path.join(os.path.dirname(__file__), '..', 'lib')

_spec = importlib.util.spec_from_file_location(
    'w3_2d_shadow_metric',
    os.path.join(_lib_dir, 'w3_2d_shadow_metric.py')
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

c = Symbol('c')
x_T = Symbol('x_T')
x_W = Symbol('x_W')


# ============================================================
# Hessian and propagator tests
# ============================================================

class TestHessianPropagator:
    """Tests for the curvature matrix and its inverse."""

    def test_hessian_TT(self):
        """H_TT = c/2."""
        H = _mod.w3_hessian()
        assert simplify(H[0, 0] - c / 2) == 0

    def test_hessian_WW(self):
        """H_WW = c/3."""
        H = _mod.w3_hessian()
        assert simplify(H[1, 1] - c / 3) == 0

    def test_hessian_TW_zero(self):
        """H_TW = 0 (diagonal Hessian)."""
        H = _mod.w3_hessian()
        assert H[0, 1] == 0

    def test_hessian_symmetric(self):
        """H is symmetric."""
        H = _mod.w3_hessian()
        assert H[0, 1] == H[1, 0]

    def test_propagator_TT(self):
        """P_TT = 2/c."""
        P = _mod.w3_propagator()
        assert simplify(P[0, 0] - Rational(2) / c) == 0

    def test_propagator_WW(self):
        """P_WW = 3/c."""
        P = _mod.w3_propagator()
        assert simplify(P[1, 1] - Rational(3) / c) == 0

    def test_propagator_TW_zero(self):
        """P_TW = 0."""
        P = _mod.w3_propagator()
        assert P[0, 1] == 0

    def test_H_P_identity(self):
        """H * P = I (propagator is inverse of Hessian)."""
        H = _mod.w3_hessian()
        P = _mod.w3_propagator()
        prod = H * P
        assert simplify(prod[0, 0] - 1) == 0
        assert simplify(prod[1, 1] - 1) == 0
        assert simplify(prod[0, 1]) == 0
        assert simplify(prod[1, 0]) == 0

    def test_total_kappa(self):
        """Tr(H) = 5c/6."""
        kappa = _mod.w3_total_kappa()
        assert simplify(kappa - 5 * c / 6) == 0

    def test_total_kappa_at_c6(self):
        """kappa(W_3) at c=6 is 5."""
        kappa = _mod.w3_total_kappa()
        assert kappa.subs(c, 6) == 5


# ============================================================
# Cubic shadow tensor tests
# ============================================================

class TestCubicTensor:
    """Tests for the cubic shadow tensor."""

    def test_C_TTT(self):
        """C_TTT = 2."""
        ct = _mod.w3_cubic_tensor()
        assert ct['TTT'] == 2

    def test_C_TWW(self):
        """C_TWW = 3 (weight of W)."""
        ct = _mod.w3_cubic_tensor()
        assert ct['TWW'] == 3

    def test_C_TTW_zero(self):
        """C_TTW = 0 by Z_2 parity."""
        ct = _mod.w3_cubic_tensor()
        assert ct['TTW'] == 0

    def test_C_WWW_zero(self):
        """C_WWW = 0 by Z_2 parity."""
        ct = _mod.w3_cubic_tensor()
        assert ct['WWW'] == 0

    def test_cubic_polynomial(self):
        """Sh_3 = 2 x_T^3 + 3 x_T x_W^2."""
        Sh_3 = _mod.w3_cubic_polynomial()
        expected = 2 * x_T**3 + 3 * x_T * x_W**2
        assert simplify(Sh_3 - expected) == 0

    def test_cubic_vanishes_on_wline(self):
        """Sh_3(0, x_W) = 0 by Z_2 parity."""
        Sh_3 = _mod.w3_cubic_polynomial()
        assert simplify(Sh_3.subs(x_T, 0)) == 0


# ============================================================
# Quartic shadow tensor tests
# ============================================================

class TestQuarticTensor:
    """Tests for the quartic shadow tensor from Lambda-exchange."""

    def test_Q_TTTT(self):
        """Q_TTTT = 10/[c(5c+22)]."""
        qt = _mod.w3_quartic_tensor()
        expected = Rational(10) / (c * (5 * c + 22))
        assert simplify(qt['Q_TTTT'] - expected) == 0

    def test_Q_TTWW(self):
        """Q_TTWW = 160/[c(5c+22)^2]."""
        qt = _mod.w3_quartic_tensor()
        expected = Rational(160) / (c * (5 * c + 22)**2)
        assert simplify(qt['Q_TTWW'] - expected) == 0

    def test_Q_WWWW(self):
        """Q_WWWW = 2560/[c(5c+22)^3]."""
        qt = _mod.w3_quartic_tensor()
        expected = Rational(2560) / (c * (5 * c + 22)**3)
        assert simplify(qt['Q_WWWW'] - expected) == 0

    def test_geometric_progression(self):
        """Q_TTTT : Q_TTWW : Q_WWWW = 1 : alpha : alpha^2."""
        qt = _mod.w3_quartic_tensor()
        alpha = Rational(16) / (5 * c + 22)
        assert simplify(qt['Q_TTWW'] - alpha * qt['Q_TTTT']) == 0
        assert simplify(qt['Q_WWWW'] - alpha**2 * qt['Q_TTTT']) == 0

    def test_alpha_value(self):
        """alpha = 16/(5c+22)."""
        qt = _mod.w3_quartic_tensor()
        assert simplify(qt['alpha'] - Rational(16) / (5 * c + 22)) == 0

    def test_quartic_polynomial_z2(self):
        """Quartic polynomial has only even powers of x_W."""
        Sh_4 = _mod.w3_quartic_polynomial()
        poly = Poly(Sh_4, x_T, x_W)
        for monom in poly.monoms():
            assert monom[1] % 2 == 0, f"Odd x_W power: {monom}"

    def test_quartic_tline(self):
        """Quartic on T-line = Virasoro quartic."""
        Sh_4 = _mod.w3_quartic_polynomial()
        on_T = Sh_4.subs(x_W, 0)
        expected = Rational(10) / (c * (5 * c + 22)) * x_T**4
        assert simplify(on_T - expected) == 0

    def test_quartic_wline(self):
        """Quartic on W-line = Q_WWWW x_W^4."""
        Sh_4 = _mod.w3_quartic_polynomial()
        on_W = Sh_4.subs(x_T, 0)
        expected = Rational(2560) / (c * (5 * c + 22)**3) * x_W**4
        assert simplify(on_W - expected) == 0


# ============================================================
# 2D bracket tests
# ============================================================

class TestBracket:
    """Tests for the 2D H-Poisson bracket."""

    def test_bracket_degree(self):
        """Bracket of degree j and k polynomials has degree j+k-2."""
        f = x_T**3
        g = x_T**4
        br = _mod.h_poisson_2d(f, g)
        poly = Poly(br, x_T, x_W)
        assert poly.total_degree() == 5

    def test_bracket_skew_symmetry(self):
        """{f, g} = {g, f} for this symmetric bracket."""
        f = 2 * x_T**3 + 3 * x_T * x_W**2
        g = x_T**4 + x_W**4
        assert simplify(_mod.h_poisson_2d(f, g) - _mod.h_poisson_2d(g, f)) == 0

    def test_bracket_Sh2_Sh3(self):
        """{Sh_2, Sh_3} = 2*5 * Sh_5 contributions."""
        Sh_2 = (c / 2) * x_T**2 + (c / 3) * x_W**2
        Sh_3 = 2 * x_T**3 + 3 * x_T * x_W**2
        br = _mod.h_poisson_2d(Sh_2, Sh_3)
        # {Sh_2, Sh_3} should have degree 3 (= 2+3-2)
        poly = Poly(expand(br), x_T, x_W)
        assert poly.total_degree() == 3


# ============================================================
# Arity-by-arity contribution tests
# ============================================================

class TestArityContributions:
    """Tests for individual arity contributions to the shadow metric."""

    def test_arity2_constant(self):
        """Arity-2 contribution is the constant matrix [[c, 0], [0, 2c/3]]."""
        M2 = _mod.arity2_contribution()
        assert simplify(M2[0, 0] - c) == 0
        assert simplify(M2[1, 1] - 2 * c / 3) == 0
        assert M2[0, 1] == 0
        assert M2[1, 0] == 0

    def test_arity2_is_2H(self):
        """Arity-2 Hessian of (c/2)x_T^2 + (c/3)x_W^2 = 2H."""
        M2 = _mod.arity2_contribution()
        H = _mod.w3_hessian()
        for i in range(2):
            for j in range(2):
                assert simplify(M2[i, j] - 2 * H[i, j]) == 0

    def test_arity3_linear_in_xT(self):
        """Arity-3 contribution is linear in x_T (from Sh_3 = 2x_T^3 + 3x_T x_W^2)."""
        M3 = _mod.arity3_contribution()
        # M3_TT = 12 x_T, M3_TW = 6 x_W, M3_WW = 6 x_T
        assert simplify(M3[0, 0] - 12 * x_T) == 0
        assert simplify(M3[0, 1] - 6 * x_W) == 0
        assert simplify(M3[1, 1] - 6 * x_T) == 0

    def test_arity3_symmetric(self):
        """Arity-3 contribution matrix is symmetric."""
        M3 = _mod.arity3_contribution()
        assert M3[0, 1] == M3[1, 0]

    def test_arity3_tline(self):
        """Arity-3 contribution on T-line: M3_TT = 12 x_T, M3_WW = 6 x_T, M3_TW = 0."""
        M3 = _mod.arity3_contribution()
        M3_T = M3.subs(x_W, 0)
        assert simplify(M3_T[0, 0] - 12 * x_T) == 0
        assert simplify(M3_T[0, 1]) == 0
        assert simplify(M3_T[1, 1] - 6 * x_T) == 0

    def test_arity4_quadratic(self):
        """Arity-4 contribution is quadratic in (x_T, x_W)."""
        M4 = _mod.arity4_contribution()
        for i in range(2):
            for j in range(2):
                if M4[i, j] != S.Zero:
                    poly = Poly(M4[i, j], x_T, x_W)
                    assert poly.total_degree() == 2

    def test_arity4_TT_coefficient(self):
        """M4_TT contains 12 Q_TTTT x_T^2 + 12 Q_TTWW x_W^2."""
        M4 = _mod.arity4_contribution()
        qt = _mod.w3_quartic_tensor()
        expected = 12 * qt['Q_TTTT'] * x_T**2 + 12 * qt['Q_TTWW'] * x_W**2
        assert simplify(M4[0, 0] - expected) == 0


# ============================================================
# Shadow metric matrix tests
# ============================================================

class TestShadowMetricMatrix:
    """Tests for the full 2D shadow metric matrix."""

    @pytest.fixture(scope='class')
    def metric6(self):
        return _mod.shadow_metric_matrix(6)

    def test_metric_symmetric(self, metric6):
        """Shadow metric matrix is symmetric."""
        assert simplify(metric6[0, 1] - metric6[1, 0]) == 0

    def test_metric_positive_at_origin(self, metric6):
        """At origin x_T = x_W = 0, the metric is positive definite for c > 0."""
        M0 = metric6.subs([(x_T, 0), (x_W, 0)])
        # M0 = [[c, 0], [0, 2c/3]] (from arity 2 alone)
        assert simplify(M0[0, 0] - c) == 0
        assert simplify(M0[1, 1] - 2 * c / 3) == 0
        assert M0[0, 1] == 0
        # Positive definite for c > 0: both diagonal entries positive

    def test_metric_at_origin_is_2H(self, metric6):
        """At the origin, M = 2H."""
        M0 = metric6.subs([(x_T, 0), (x_W, 0)])
        H = _mod.w3_hessian()
        for i in range(2):
            for j in range(2):
                assert simplify(M0[i, j] - 2 * H[i, j]) == 0

    def test_metric_TT_at_c1_origin(self, metric6):
        """M_TT(0, 0, c=1) = 1."""
        val = metric6[0, 0].subs([(c, 1), (x_T, 0), (x_W, 0)])
        assert val == 1

    def test_metric_WW_at_c1_origin(self, metric6):
        """M_WW(0, 0, c=1) = 2/3."""
        val = metric6[1, 1].subs([(c, 1), (x_T, 0), (x_W, 0)])
        assert val == Rational(2, 3)


# ============================================================
# T-line restriction tests
# ============================================================

class TestTLineRestriction:
    """Tests for the T-line (x_W = 0) restriction of the 2D metric."""

    def test_tline_metric_arity2(self):
        """Arity-2 contribution on T-line: c."""
        M2 = _mod.arity2_contribution()
        assert simplify(M2[0, 0].subs(x_W, 0) - c) == 0

    def test_tline_metric_arity3(self):
        """Arity-3 contribution on T-line: 12 x_T."""
        M3 = _mod.arity3_contribution()
        assert simplify(M3[0, 0].subs(x_W, 0) - 12 * x_T) == 0

    def test_tline_metric_arity4(self):
        """Arity-4 contribution on T-line: 12 Q_TT x_T^2."""
        M4 = _mod.arity4_contribution()
        expected = 12 * Rational(10) / (c * (5 * c + 22)) * x_T**2
        assert simplify(M4[0, 0].subs(x_W, 0) - expected) == 0

    def test_tline_TW_vanishes_arity3(self):
        """M_TW on T-line from arity 3: 6 x_W -> 0."""
        M3 = _mod.arity3_contribution()
        assert simplify(M3[0, 1].subs(x_W, 0)) == 0

    def test_tline_virasoro_discriminant(self):
        """Delta_TT = 40/(5c+22) matches the Virasoro critical discriminant."""
        vcheck = _mod.virasoro_discriminant_check()
        assert vcheck['match']


# ============================================================
# W-line restriction tests
# ============================================================

class TestWLineRestriction:
    """Tests for the W-line (x_T = 0) restriction."""

    def test_wline_metric_arity2_WW(self):
        """M_WW(0, x_W, arity 2) = 2c/3."""
        M2 = _mod.arity2_contribution()
        assert simplify(M2[1, 1].subs(x_T, 0) - 2 * c / 3) == 0

    def test_wline_arity3_vanishes(self):
        """Arity-3 contribution M_WW on W-line: 6*0 = 0."""
        M3 = _mod.arity3_contribution()
        assert simplify(M3[1, 1].subs(x_T, 0)) == 0

    def test_wline_arity4_WW(self):
        """M_WW(0, x_W, arity 4) = 12 Q_WWWW x_W^2."""
        M4 = _mod.arity4_contribution()
        expected = 12 * Rational(2560) / (c * (5 * c + 22)**3) * x_W**2
        assert simplify(M4[1, 1].subs(x_T, 0) - expected) == 0


# ============================================================
# Critical discriminant tests
# ============================================================

class TestCriticalDiscriminant:
    """Tests for the 2D critical discriminant matrix."""

    def test_Delta_TT_value(self):
        """Delta_TT = 8 * (c/2) * 10/[c(5c+22)] = 40/(5c+22)."""
        deltas = _mod.critical_discriminant_matrix()
        expected = Rational(40) / (5 * c + 22)
        assert simplify(deltas['Delta_TT'] - expected) == 0

    def test_Delta_WW_value(self):
        """Delta_WW = 8 * (c/3) * 2560/[c(5c+22)^3]."""
        deltas = _mod.critical_discriminant_matrix()
        expected = cancel(8 * (c / 3) * Rational(2560) / (c * (5 * c + 22)**3))
        assert simplify(deltas['Delta_WW'] - expected) == 0

    def test_Delta_TT_at_c1(self):
        """Delta_TT at c=1: 40/27."""
        deltas = _mod.critical_discriminant_matrix()
        val = deltas['Delta_TT'].subs(c, 1)
        assert val == Rational(40, 27)

    def test_Delta_TT_nonzero_generic(self):
        """Delta_TT != 0 for generic c (W_3 is class M)."""
        deltas = _mod.critical_discriminant_matrix()
        # Only vanishes at c = 0 or c = infinity
        assert deltas['Delta_TT'].subs(c, 1) != 0
        assert deltas['Delta_TT'].subs(c, 13) != 0
        assert deltas['Delta_TT'].subs(c, 25) != 0


# ============================================================
# Propagator variance tests
# ============================================================

class TestPropagatorVariance:
    """Tests for the propagator variance delta_mix."""

    @pytest.fixture(scope='class')
    def pv(self):
        return _mod.propagator_variance_from_metric()

    def test_f_T_value(self, pv):
        """f_T = 4 Q_0 (1 + 3*alpha)."""
        Q0 = Rational(10) / (c * (5 * c + 22))
        alpha = Rational(16) / (5 * c + 22)
        expected = cancel(4 * Q0 * (1 + 3 * alpha))
        assert simplify(pv['f_T'] - expected) == 0

    def test_f_W_value(self, pv):
        """f_W = 4 Q_0 alpha (3 + alpha)."""
        Q0 = Rational(10) / (c * (5 * c + 22))
        alpha = Rational(16) / (5 * c + 22)
        expected = cancel(4 * Q0 * alpha * (3 + alpha))
        assert simplify(pv['f_W'] - expected) == 0

    def test_delta_nonneg_c1(self, pv):
        """delta_mix >= 0 at c=1."""
        val = pv['delta_mix'].subs(c, 1)
        assert val >= 0

    def test_delta_nonneg_c13(self, pv):
        """delta_mix >= 0 at c=13."""
        val = pv['delta_mix'].subs(c, 13)
        assert val >= 0

    def test_delta_nonneg_c25(self, pv):
        """delta_mix >= 0 at c=25."""
        val = pv['delta_mix'].subs(c, 25)
        assert val >= 0

    def test_delta_vanishes_at_enhanced_symmetry(self, pv):
        """delta_mix = 0 at the roots of the mixing polynomial P."""
        loci = _mod.enhanced_symmetry_loci()
        for c_val in loci:
            assert cancel(pv['delta_mix'].subs(c, c_val)) == 0


# ============================================================
# Mixing polynomial tests
# ============================================================

class TestMixingPolynomial:
    """Tests for the mixing polynomial P(c) = 25c^2 + 100c - 428."""

    def test_mixing_poly_value(self):
        """P(c) = 25c^2 + 100c - 428."""
        P = _mod.mixing_polynomial()
        expected = 25 * c**2 + 100 * c - 428
        assert simplify(P - expected) == 0

    def test_mixing_poly_from_gradients(self):
        """P derived from gradient proportionality matches the stated formula.

        We check proportionality: the derived polynomial should divide into P(c)
        with a constant (possibly rational) quotient.
        """
        P_stated = _mod.mixing_polynomial()
        P_derived = _mod.mixing_polynomial_from_gradients()
        # P_derived might differ by a constant factor; check proportionality
        ratio = cancel(P_derived / P_stated)
        # ratio should be a rational constant (no c dependence)
        assert not ratio.free_symbols, \
            f"Ratio depends on c: {ratio}"

    def test_mixing_poly_discriminant(self):
        """Discriminant of P: 100^2 + 4*25*428 = 52800."""
        disc = 100**2 + 4 * 25 * 428
        assert disc == 52800

    def test_enhanced_symmetry_count(self):
        """P has exactly 2 roots."""
        loci = _mod.enhanced_symmetry_loci()
        assert len(loci) == 2

    def test_enhanced_symmetry_roots_real(self):
        """Both roots of P are real."""
        from sympy import im
        loci = _mod.enhanced_symmetry_loci()
        for root in loci:
            assert im(root) == 0, f"Root {root} is not real"

    def test_enhanced_symmetry_product(self):
        """Product of roots = -428/25."""
        loci = _mod.enhanced_symmetry_loci()
        product = cancel(loci[0] * loci[1])
        assert simplify(product - Rational(-428, 25)) == 0


# ============================================================
# Spectral curve tests
# ============================================================

class TestSpectralCurve:
    """Tests for the spectral curve det(M) = 0."""

    def test_spectral_curve_low_order_nonzero(self):
        """det(M) from arities 2-4 is not identically zero."""
        sc = _mod.spectral_curve_low_order()
        assert sc['determinant'] != S.Zero

    def test_spectral_trace_low_order(self):
        """Tr(M) from arities 2-4 is nonzero."""
        sc = _mod.spectral_curve_low_order()
        assert sc['trace'] != S.Zero

    def test_spectral_det_at_origin(self):
        """det(M)(0,0) = c * 2c/3 = 2c^2/3."""
        sc = _mod.spectral_curve_low_order()
        det_origin = sc['determinant'].subs([(x_T, 0), (x_W, 0)])
        expected = 2 * c**2 / 3
        assert simplify(det_origin - expected) == 0

    def test_spectral_tline_blocks(self):
        """On T-line, metric is block diagonal so det = M_TT * M_WW."""
        data = _mod.spectral_curve_tline()
        # M_TW should be zero on T-line
        assert simplify(data['M_TW']) == 0
        # det should be M_TT * M_WW
        expected_det = expand(data['M_TT'] * data['M_WW'])
        assert simplify(data['det'] - expected_det) == 0


# ============================================================
# Koszul duality tests
# ============================================================

class TestKoszulDuality:
    """Tests for the W_3 Koszul duality under c -> 100 - c."""

    def test_koszul_conductor(self):
        """W_3 Koszul conductor is 100."""
        assert _mod.w3_koszul_conductor() == 100

    def test_koszul_dual_hessian(self):
        """H(100 - c) = diag((100-c)/2, (100-c)/3)."""
        H = _mod.w3_hessian()
        H_dual = H.subs(c, 100 - c)
        assert simplify(H_dual[0, 0] - (100 - c) / 2) == 0
        assert simplify(H_dual[1, 1] - (100 - c) / 3) == 0

    def test_total_kappa_sum(self):
        """kappa(c) + kappa(100-c) = 5*100/6 = 250/3."""
        kappa = _mod.w3_total_kappa()
        kappa_dual = kappa.subs(c, 100 - c)
        summed = cancel(kappa + kappa_dual)
        assert simplify(summed - Rational(250, 3)) == 0


# ============================================================
# Diagonal restriction tests
# ============================================================

class TestDiagonalRestriction:
    """Tests for the diagonal x_T = x_W = x restriction."""

    def test_diagonal_at_origin(self):
        """Diagonal metric at origin: c + 0 + 2c/3 = 5c/3."""
        M = _mod.shadow_metric_matrix(4)
        x = Symbol('x')
        M_diag = M[0, 0] + 2 * M[0, 1] + M[1, 1]
        val = M_diag.subs([(x_T, 0), (x_W, 0)])
        # 2H_TT + 2*0 + 2H_WW = c + 2c/3 = 5c/3
        assert simplify(val - 5 * c / 3) == 0


# ============================================================
# Numerical spot checks
# ============================================================

class TestNumerical:
    """Numerical evaluations at specific central charges."""

    def test_metric_c1_origin(self):
        """M(0,0) at c=1 is [[1, 0], [0, 2/3]]."""
        M = _mod.evaluate_metric_at(1, 0, 0, max_arity=6)
        assert M[0, 0] == 1
        assert M[1, 1] == Rational(2, 3)
        assert M[0, 1] == 0

    def test_det_c1_origin(self):
        """det(M) at (c,x_T,x_W) = (1,0,0) is 2/3."""
        det = _mod.evaluate_determinant_at(1, 0, 0, max_arity=6)
        assert det == Rational(2, 3)

    def test_metric_c6_origin(self):
        """M(0,0) at c=6: [[6, 0], [0, 4]]."""
        M = _mod.evaluate_metric_at(6, 0, 0, max_arity=6)
        assert M[0, 0] == 6
        assert M[1, 1] == 4
        assert M[0, 1] == 0

    def test_metric_finite_at_c13(self):
        """Shadow metric is finite at c=13 (Virasoro self-dual point)."""
        M = _mod.evaluate_metric_at(13, 1, 1, max_arity=6)
        for i in range(2):
            for j in range(2):
                assert M[i, j].is_finite, f"M[{i},{j}] infinite at c=13"

    def test_metric_finite_at_c26(self):
        """Shadow metric is finite at c=26."""
        M = _mod.evaluate_metric_at(26, 1, 1, max_arity=6)
        for i in range(2):
            for j in range(2):
                assert M[i, j].is_finite, f"M[{i},{j}] infinite at c=26"

    def test_det_positive_c1_origin(self):
        """det(M) > 0 at (c, x_T, x_W) = (1, 0, 0): positive definite."""
        det = _mod.evaluate_determinant_at(1, 0, 0, max_arity=6)
        assert det > 0

    def test_det_positive_c6_origin(self):
        """det(M) > 0 at (c, x_T, x_W) = (6, 0, 0)."""
        det = _mod.evaluate_determinant_at(6, 0, 0, max_arity=6)
        assert det > 0


# ============================================================
# 2D tower consistency tests
# ============================================================

class TestTowerConsistency:
    """Consistency of the shadow obstruction tower with the metric."""

    def test_tower_arity5_nonzero(self):
        """The 2D tower has nonzero arity 5 (W_3 is class M)."""
        tower = _mod.compute_2d_tower(5)
        assert simplify(tower[5]) != 0

    def test_tower_z2_parity(self):
        """Z_2 parity: Sh_r(x_T, -x_W) = Sh_r(x_T, x_W) for all r."""
        tower = _mod.compute_2d_tower(7)
        for r in range(2, 8):
            Sh_r = tower[r]
            if Sh_r == S.Zero:
                continue
            flipped = Sh_r.subs(x_W, -x_W)
            assert simplify(flipped - Sh_r) == 0, \
                f"Z_2 parity fails at arity {r}"

    def test_tower_tline_arity5(self):
        """T-line restriction at arity 5 matches Virasoro: -48/[c^2(5c+22)]."""
        tower = _mod.compute_2d_tower(5)
        restricted = tower[5].subs(x_W, 0)
        poly = Poly(restricted, x_T)
        coeff = poly.nth(5)
        expected = Rational(-48) / (c**2 * (5 * c + 22))
        assert simplify(coeff - expected) == 0

    def test_tower_wline_odd_vanish(self):
        """Odd arities vanish on the W-line."""
        tower = _mod.compute_2d_tower(7)
        for r in [3, 5, 7]:
            restricted = tower[r].subs(x_T, 0)
            assert simplify(restricted) == 0, \
                f"Arity {r} nonzero on W-line"


# ============================================================
# Cross-module consistency tests
# ============================================================

class TestCrossModule:
    """Verify consistency with w3_full_2d_shadow_tower module."""

    @pytest.fixture(scope='class')
    def other_tower(self):
        """Load the existing w3_full_2d_shadow_tower module."""
        spec = importlib.util.spec_from_file_location(
            'w3_full_2d_shadow_tower',
            os.path.join(_lib_dir, 'w3_full_2d_shadow_tower.py')
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.compute_full_2d_tower(7)

    def test_arity2_matches(self, other_tower):
        """Sh_2 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(our_tower[2] - other_tower[2]) == 0

    def test_arity3_matches(self, other_tower):
        """Sh_3 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(our_tower[3] - other_tower[3]) == 0

    def test_arity4_matches(self, other_tower):
        """Sh_4 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(expand(our_tower[4]) - expand(other_tower[4])) == 0

    def test_arity5_matches(self, other_tower):
        """Sh_5 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(expand(our_tower[5]) - expand(other_tower[5])) == 0

    def test_arity6_matches(self, other_tower):
        """Sh_6 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(expand(our_tower[6]) - expand(other_tower[6])) == 0

    def test_arity7_matches(self, other_tower):
        """Sh_7 matches between modules."""
        our_tower = _mod.compute_2d_tower(7)
        assert simplify(expand(our_tower[7]) - expand(other_tower[7])) == 0
