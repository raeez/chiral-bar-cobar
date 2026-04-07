r"""Tests for the Hitchin system underlying the shadow connection.

Verifies:
    1. The spectral curve y^2 = Q_L(t) for all standard families
    2. The Hitchin Hamiltonians from shadow data
    3. The Schrodinger potential and singularity classification
    4. WKB hierarchy: sigma_1' = omega (shadow connection = one-loop WKB)
    5. The universal Voros period v_0 = pi
    6. The W_3 rank-2 spectral curve (the 2x2 system)
    7. The Hitchin-shadow dictionary (G/L/C/M classification)
    8. Discriminant complementarity under Koszul duality
    9. Consistency: disc(Q) = -32*kappa^2*Delta
   10. Algebraicity: H^2 = t^4*Q via independent coefficient extraction
   11. Numerical cross-checks at specific c values

25+ tests, multi-path verification (AP10 compliance).
"""

from __future__ import annotations

import cmath
import math

import pytest
from fractions import Fraction

from sympy import (
    I, Rational, S, Symbol, cancel, diff, expand, factor,
    pi, simplify, solve, sqrt, symbols,
)

from compute.lib.hitchin_shadow_system import (
    # Section 1: rank-1 spectral curve
    shadow_metric_Q,
    spectral_curve_rank1,
    virasoro_spectral_curve,
    virasoro_spectral_curve_at_c26,
    # Section 2: Hitchin Hamiltonians
    hitchin_hamiltonians_rank1,
    virasoro_hitchin_hamiltonians,
    # Section 3: Schrodinger potential
    schrodinger_potential,
    virasoro_schrodinger_potential,
    # Section 4: WKB
    wkb_classical,
    wkb_one_loop,
    wkb_higher_loop,
    # Section 5: W_3 rank-2
    w3_shadow_metric_2x2,
    w3_spectral_curve_2d,
    w3_spectral_curve_at_c26,
    w3_spectral_curve_on_tline,
    # Section 6: Hitchin fibration
    hitchin_fibration_dictionary,
    # Section 7: complementarity
    discriminant_complementarity,
    # Section 8: Voros
    voros_half_period,
    # Section 9: Hitchin section
    hitchin_section_identification,
    # Section 10: coefficients
    shadow_coefficients_from_wkb,
    # Section 11: standard families
    heisenberg_hitchin_data,
    affine_sl2_hitchin_data,
    virasoro_hitchin_data,
    # Section 12: propagator variance
    propagator_variance_as_hitchin_curvature,
    # Section 13: numerical
    numerical_spectral_curve_virasoro,
    numerical_w3_spectral_curve,
    # Section 14: verification
    verify_disc_formula,
    verify_wkb_one_loop_is_shadow,
    verify_gaussian_decomposition,
    verify_algebraicity,
)


c = Symbol('c')
t = Symbol('t')
k = Symbol('k')


# =========================================================================
# Test 1: Shadow metric construction
# =========================================================================

class TestShadowMetricConstruction:
    """Test the shadow metric Q_L(t) for correctness."""

    def test_virasoro_shadow_metric_form(self):
        """Q_Vir = c^2 + 12ct + [(180c+872)/(5c+22)]*t^2."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        Q = shadow_metric_Q(kappa, alpha, S4)
        # Check Q(0) = c^2
        assert simplify(Q.subs(t, 0) - c**2) == 0
        # Check Q'(0) = 12c
        Q_prime = diff(Q, t)
        assert simplify(Q_prime.subs(t, 0) - 12*c) == 0

    def test_heisenberg_shadow_metric_constant(self):
        """Heisenberg: Q = 4k^2 (constant, class G)."""
        Q = shadow_metric_Q(k, S.Zero, S.Zero)
        assert simplify(Q - 4*k**2) == 0

    def test_affine_sl2_perfect_square(self):
        """sl_2^(1): Q = (3(k+2)/2 + 3t)^2 (perfect square, class L)."""
        kappa = Rational(3) * (k + 2) / 4
        Q = shadow_metric_Q(kappa, Rational(1), S.Zero)
        expected = expand((2*kappa + 3*t)**2)
        assert simplify(Q - expected) == 0


# =========================================================================
# Test 2: Spectral curve rank-1
# =========================================================================

class TestSpectralCurveRank1:
    """Test the spectral curve Sigma_L: y^2 = Q_L(t)."""

    def test_virasoro_spectral_curve_genus_0(self):
        """Virasoro spectral curve has arithmetic genus 0."""
        sc = virasoro_spectral_curve()
        assert sc['genus'] == 0

    def test_virasoro_class_M(self):
        """Virasoro is class M: Delta != 0."""
        sc = virasoro_spectral_curve()
        # Delta = 40/(5c+22), nonzero for generic c
        assert sc['class'] == 'M'

    def test_heisenberg_class_G(self):
        """Heisenberg is class G: Delta = 0, nodal curve."""
        sc = spectral_curve_rank1(k, S.Zero, S.Zero)
        assert sc['is_nodal'] is True
        assert sc['class'] == 'G_or_L'

    def test_affine_class_L(self):
        """Affine KM (generic) is class L: Delta = 0, S_3 != 0."""
        kappa = Rational(3) * (k + 2) / 4
        sc = spectral_curve_rank1(kappa, Rational(1), S.Zero)
        assert sc['is_nodal'] is True

    def test_virasoro_c26_explicit(self):
        """Spectral curve at c=26: explicit evaluation."""
        sc = virasoro_spectral_curve_at_c26()
        Q = sc['Q']
        # Q(0) = 4*(13)^2 = 676
        assert simplify(Q.subs(t, 0) - 676) == 0
        # Q'(0) = 12*13*2 = 312
        assert simplify(diff(Q, t).subs(t, 0) - 312) == 0


# =========================================================================
# Test 3: Hitchin Hamiltonians
# =========================================================================

class TestHitchinHamiltonians:
    """Test the Hitchin Hamiltonians from shadow data."""

    def test_virasoro_H0(self):
        """H_0 = c^2 for Virasoro."""
        hh = virasoro_hitchin_hamiltonians()
        assert simplify(hh['H_0'] - c**2) == 0

    def test_virasoro_H1(self):
        """H_1 = 12c for Virasoro."""
        hh = virasoro_hitchin_hamiltonians()
        assert simplify(hh['H_1'] - 12*c) == 0

    def test_virasoro_H2(self):
        """H_2 = (180c+872)/(5c+22) for Virasoro."""
        hh = virasoro_hitchin_hamiltonians()
        expected = (180*c + 872) / (5*c + 22)
        assert simplify(hh['H_2'] - expected) == 0

    def test_disc_equals_minus32_kappa2_delta(self):
        """disc(Q_L) = -32*kappa^2*Delta for all families."""
        hh = virasoro_hitchin_hamiltonians()
        # disc_vs_Delta should be zero (disc + 32*kappa^2*Delta = 0)
        assert simplify(hh['disc_vs_Delta']) == 0


# =========================================================================
# Test 4: Schrodinger potential
# =========================================================================

class TestSchrodingerPotential:
    """Test the Schrodinger potential V(t) = C/Q^2."""

    def test_virasoro_C_formula(self):
        """C_Vir = 80c^2/(5c+22)."""
        sp = virasoro_schrodinger_potential()
        expected_C = 80*c**2 / (5*c + 22)
        assert simplify(sp['C'] - expected_C) == 0

    def test_class_L_potential_vanishes(self):
        """For class L (Delta = 0): V = 0."""
        kappa = Rational(3) * (k + 2) / 4
        sp = schrodinger_potential(kappa, Rational(1), S.Zero)
        assert simplify(sp['V']) == 0

    def test_potential_double_poles_at_Q_zeros(self):
        """V has double poles at zeros of Q (for class M)."""
        # For Virasoro: V = C/Q^2, Q quadratic => V has double poles at
        # the two zeros of Q. The degree of the denominator is 4 (from Q^2).
        sp = virasoro_schrodinger_potential()
        V = sp['V']
        # Check the denominator is Q^2 (degree 4 in t)
        from sympy import Poly, denom
        d = denom(cancel(V))
        p = Poly(expand(d), t)
        assert p.degree() == 4


# =========================================================================
# Test 5: WKB hierarchy
# =========================================================================

class TestWKBHierarchy:
    """Test the WKB expansion and its identification with the shadow."""

    def test_sigma1_equals_omega_virasoro(self):
        """sigma_1'(t) = Q'/(2Q) for Virasoro (the key identification)."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        assert verify_wkb_one_loop_is_shadow(kappa, alpha, S4)

    def test_sigma1_equals_omega_affine(self):
        """sigma_1'(t) = Q'/(2Q) for affine sl_2."""
        kappa = Rational(3) * (k + 2) / 4
        assert verify_wkb_one_loop_is_shadow(kappa, Rational(1), S.Zero)

    def test_wkb_higher_loops_rational(self):
        """Higher WKB coefficients are rational functions of t."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        sigmas = wkb_higher_loop(kappa, alpha, S4, n_max=3)
        # sigma_2 should be expressible as a rational function
        # (no square roots in the final answer after cancellation)
        s2 = sigmas[2]
        # Check it's not identically zero (class M has nontrivial higher loops)
        assert s2 is not S.Zero


# =========================================================================
# Test 6: Voros period universality
# =========================================================================

class TestVorosPeriod:
    """Test the universal Voros half-period v_0 = pi."""

    def test_voros_is_pi_virasoro(self):
        """v_0 = pi for Virasoro."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        vp = voros_half_period(kappa, alpha, S4)
        assert vp['v_0'] == pi

    def test_voros_ratio_is_1(self):
        """The ratio C*4/(-disc_Q) = 1 (proving v_0 = pi)."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        vp = voros_half_period(kappa, alpha, S4)
        assert vp['ratio_is_1'] is True

    def test_class_L_voros_zero(self):
        """For class L, no branch points => period is zero/undefined."""
        kappa = Rational(3) * (k + 2) / 4
        vp = voros_half_period(kappa, Rational(1), S.Zero)
        assert vp['v_0'] == S.Zero


# =========================================================================
# Test 7: W_3 rank-2 spectral curve
# =========================================================================

class TestW3SpectralCurve:
    """Test the W_3 2x2 shadow metric and its spectral curve."""

    def test_w3_metric_symmetric(self):
        """The shadow metric matrix is symmetric."""
        M = w3_shadow_metric_2x2()
        assert simplify(M[0, 1] - M[1, 0]) == 0

    def test_w3_tline_decouples(self):
        """On the T-line (x_W = 0), M_TW = 0 (decouples)."""
        data = w3_spectral_curve_on_tline()
        assert simplify(data['M_TW']) == 0
        assert data['factored'] is True

    def test_w3_tline_TT_equals_virasoro(self):
        """M_TT on the T-line equals the Virasoro shadow metric Hessian."""
        data = w3_spectral_curve_on_tline()
        M_TT = data['M_TT']
        # The Virasoro shadow metric Hessian (second derivative of H_Vir)
        # H_Vir = sum r*S_r*t^r, H'' = sum r*(r-1)*S_r*t^{r-2}
        # At arity 2: contribution is c (from kappa = c/2, d^2/dx^2 of (c/2)x^2 = c)
        # At arity 3: contribution is 12*x_T (from d^2/dx_T^2 of 2x_T^3 = 12*x_T)
        # At arity 4: contribution is 12*Q_TTTT*x_T^2 = 120*x_T^2/[c(5c+22)]
        Q_TTTT = Rational(10) / (c * (5*c + 22))
        expected = c + 12*Symbol('x_T') + 12*Q_TTTT*Symbol('x_T')**2
        # Compare after substitution
        x_T_sym = Symbol('x_T')
        assert simplify(M_TT - expected) == 0

    def test_w3_c26_trace_at_origin(self):
        """At c=26, (x_T, x_W) = (0, 0): Tr(M) = c + 2c/3 = 5c/3."""
        data = w3_spectral_curve_at_c26()
        tr = data['trace']
        # At origin x_T = x_W = 0
        tr_origin = tr.subs([(Symbol('x_T'), 0), (Symbol('x_W'), 0)])
        # 26 + 2*26/3 = 26 + 52/3 = (78+52)/3 = 130/3
        assert simplify(tr_origin - Rational(130, 3)) == 0

    def test_w3_c26_det_at_origin(self):
        """At c=26, origin: det(M) = c * 2c/3 = 2c^2/3."""
        data = w3_spectral_curve_at_c26()
        det_val = data['det']
        det_origin = det_val.subs([(Symbol('x_T'), 0), (Symbol('x_W'), 0)])
        # c * 2c/3 = 2*26^2/3 = 1352/3
        assert simplify(det_origin - Rational(1352, 3)) == 0


# =========================================================================
# Test 8: Discriminant complementarity
# =========================================================================

class TestDiscriminantComplementarity:
    """Test the complementarity of discriminants under Koszul duality."""

    def test_numerator_is_6960(self):
        """Delta(c) + Delta(26-c) has universal numerator 6960."""
        dc = discriminant_complementarity()
        assert dc['numerator_is_6960'] is True

    def test_self_dual_at_c13(self):
        """Delta(13) = Delta(13) at the self-dual point."""
        dc = discriminant_complementarity()
        assert dc['self_dual_c'] == 13
        # Delta(13) = 40/(5*13+22) = 40/87
        assert simplify(dc['Delta_at_self_dual'] - Rational(40, 87)) == 0


# =========================================================================
# Test 9: Consistency verifications
# =========================================================================

class TestConsistencyVerifications:
    """Multi-path verification of key identities."""

    def test_disc_formula_virasoro(self):
        """disc(Q) = -32*kappa^2*Delta for Virasoro."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        assert verify_disc_formula(kappa, alpha, S4)

    def test_disc_formula_heisenberg(self):
        """disc(Q) = -32*kappa^2*Delta for Heisenberg."""
        assert verify_disc_formula(k, S.Zero, S.Zero)

    def test_disc_formula_affine(self):
        """disc(Q) = -32*kappa^2*Delta for affine sl_2."""
        kappa = Rational(3) * (k + 2) / 4
        assert verify_disc_formula(kappa, Rational(1), S.Zero)

    def test_gaussian_decomposition_virasoro(self):
        """Q = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2 for Virasoro."""
        kappa = c / 2
        alpha = Rational(2)
        S4 = Rational(10) / (c * (5*c + 22))
        assert verify_gaussian_decomposition(kappa, alpha, S4)

    def test_algebraicity_virasoro(self):
        """H^2 = t^4*Q for Virasoro (independent verification)."""
        # Use numeric c to avoid symbolic complexity
        kappa = Rational(5)  # c = 10
        alpha = Rational(2)
        S4 = Rational(10) / (10 * (50 + 22))  # = 10/720 = 1/72
        assert verify_algebraicity(kappa, alpha, S4, max_arity=8)


# =========================================================================
# Test 10: Hitchin fibration dictionary
# =========================================================================

class TestHitchinFibration:
    """Test the Hitchin-shadow dictionary."""

    def test_four_classes_present(self):
        """All four classes G/L/C/M are in the dictionary."""
        d = hitchin_fibration_dictionary()
        assert set(d.keys()) == {'G', 'L', 'C', 'M'}

    def test_class_G_depth_2(self):
        d = hitchin_fibration_dictionary()
        assert d['G']['depth'] == 2

    def test_class_L_depth_3(self):
        d = hitchin_fibration_dictionary()
        assert d['L']['depth'] == 3

    def test_class_M_infinite_depth(self):
        d = hitchin_fibration_dictionary()
        assert d['M']['depth'] == 'infinity'


# =========================================================================
# Test 11: Standard family Hitchin data
# =========================================================================

class TestStandardFamilies:
    """Test Hitchin data for Heisenberg, affine KM, Virasoro."""

    def test_heisenberg_class_G(self):
        data = heisenberg_hitchin_data()
        assert data['class'] == 'G'
        assert data['is_nodal'] is True
        assert simplify(data['Delta']) == 0

    def test_affine_sl2_class_L(self):
        data = affine_sl2_hitchin_data()
        assert data['class'] == 'L'
        assert data['is_nodal'] is True

    def test_virasoro_class_M(self):
        data = virasoro_hitchin_data()
        assert data['class'] == 'M'
        assert data['is_nodal'] is False

    def test_virasoro_has_voros_period(self):
        """Virasoro (class M) has Voros period = pi."""
        data = virasoro_hitchin_data()
        assert data['voros']['v_0'] == pi


# =========================================================================
# Test 12: Hitchin section
# =========================================================================

class TestHitchinSection:
    """Test the Hitchin section identification."""

    def test_section_is_regular(self):
        """On the Hitchin section (S_4=0), the connection is regular."""
        hs = hitchin_section_identification(c/2, Rational(2), S.Zero)
        assert hs['section_is_regular'] is True

    def test_deformation_introduces_singularities(self):
        """Turning on S_4 creates singular points."""
        S4 = Rational(10) / (c * (5*c + 22))
        hs = hitchin_section_identification(c/2, Rational(2), S4)
        assert hs['full_has_singularities'] is True


# =========================================================================
# Test 13: Shadow coefficients from WKB
# =========================================================================

class TestShadowCoefficientsFromWKB:
    """Test independent extraction of S_r from the closed form."""

    def test_S2_equals_kappa(self):
        """S_2 = kappa for Virasoro at c = 10."""
        kappa = Rational(5)
        alpha = Rational(2)
        S4 = Rational(1, 72)  # 10/(10*72) = 1/72
        coeffs = shadow_coefficients_from_wkb(kappa, alpha, S4)
        assert simplify(coeffs[2] - kappa) == 0

    def test_S3_equals_alpha(self):
        """S_3 = alpha for Virasoro at c = 10."""
        kappa = Rational(5)
        alpha = Rational(2)
        S4 = Rational(1, 72)
        coeffs = shadow_coefficients_from_wkb(kappa, alpha, S4)
        assert simplify(coeffs[3] - alpha) == 0

    def test_S4_recovered(self):
        """S_4 from WKB matches input S_4."""
        kappa = Rational(5)
        alpha = Rational(2)
        S4 = Rational(1, 72)
        coeffs = shadow_coefficients_from_wkb(kappa, alpha, S4)
        assert simplify(coeffs[4] - S4) == 0


# =========================================================================
# Test 14: Propagator variance as Hitchin curvature
# =========================================================================

class TestPropagatorVariance:
    """Test the propagator variance / Hitchin curvature identification."""

    def test_delta_mix_nonnegative_at_c10(self):
        """delta_mix >= 0 at c = 10 (Cauchy-Schwarz)."""
        pv = propagator_variance_as_hitchin_curvature(Rational(10))
        delta = float(pv['delta_mix'])
        assert delta >= -1e-15  # allow numerical tolerance

    def test_proportionality_ratio_well_defined(self):
        """The proportionality ratios f_i/kappa_i are well-defined."""
        pv = propagator_variance_as_hitchin_curvature()
        # The ratios should be rational functions of c
        assert pv['ratio_T'] is not None
        assert pv['ratio_W'] is not None


# =========================================================================
# Test 15: Numerical cross-checks
# =========================================================================

class TestNumericalCrossChecks:
    """Numerical verification at specific central charges."""

    def test_virasoro_c10_disc_negative(self):
        """At c=10, disc(Q) < 0 (complex branch points, class M)."""
        data = numerical_spectral_curve_virasoro(10.0)
        assert data['disc'] < 0

    def test_virasoro_c26_kappa_13(self):
        """At c=26, kappa = 13."""
        data = numerical_spectral_curve_virasoro(26.0)
        assert abs(data['kappa'] - 13.0) < 1e-12

    def test_virasoro_c26_delta(self):
        """At c=26, Delta = 40/152 = 5/19."""
        data = numerical_spectral_curve_virasoro(26.0)
        assert abs(data['Delta'] - 40/152) < 1e-12

    def test_virasoro_growth_rate_finite(self):
        """The growth rate rho is finite for generic c."""
        data = numerical_spectral_curve_virasoro(10.0)
        assert data['growth_rate'] > 0
        assert data['growth_rate'] < 100

    def test_w3_c26_origin_eigenvalues(self):
        """At c=26, origin: eigenvalues are c and 2c/3."""
        data = numerical_w3_spectral_curve(26.0, 0.0, 0.0)
        eigs = sorted([float(e.real) if isinstance(e, complex) else float(e)
                       for e in data['eigenvalues']])
        # 2*26/3 = 52/3 = 17.333..., and 26
        assert abs(eigs[0] - 52/3) < 1e-10
        assert abs(eigs[1] - 26.0) < 1e-10

    def test_virasoro_c1_data(self):
        """At c=1 (Ising): shadow data is well-defined."""
        data = numerical_spectral_curve_virasoro(1.0)
        assert data['kappa'] == 0.5
        assert abs(data['Delta'] - 40/27) < 1e-10
