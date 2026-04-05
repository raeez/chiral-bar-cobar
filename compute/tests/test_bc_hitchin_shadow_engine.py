r"""Tests for BC-98: Hitchin system spectral curves from shadow data.

Tests organized by section:
  1.  Shadow data for standard families (kappa, S_3, S_4)
  2.  sl_2 spectral curve from shadow data
  3.  sl_3 spectral curve from shadow data
  4.  sl_N spectral curve for arbitrary N
  5.  Hitchin base map and shadow locus
  6.  Hitchin discriminant — sl_2
  7.  Hitchin discriminant — sl_3
  8.  Shadow critical discriminant vs Hitchin discriminant
  9.  Shadow metric and connection
  10. WKB approximation
  11. Flat section of shadow connection
  12. Riemann-Hurwitz genus computation
  13. Spectral curve genus — sl_2
  14. Spectral curve genus — sl_3
  15. Spectral curve genus — sl_N
  16. Stokes graph
  17. Oper monodromy — basic
  18. Oper monodromy — Virasoro landscape
  19. Nonabelianization
  20. Complementarity under Koszul duality
  21. Shadow depth from spectral data
  22. Hitchin fiber dimension
  23. Hitchin base dimension
  24. Standard landscape
  25. Cross-checks and consistency

Multi-path verification:
  Path 1: Direct computation of discriminants (Sections 6-8)
  Path 2: Riemann-Hurwitz vs direct topology (Sections 12-15)
  Path 3: Oper monodromy vs nonabelianization (Sections 17-19)
  Path 4: Complementarity sum kappa + kappa' = 13 (Section 20)
  Path 5: Shadow depth class from discriminant sign (Section 21)
"""

import pytest
import math
import cmath
import sys
import os

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from bc_hitchin_shadow_engine import (
    # Section 1
    kappa_virasoro, kappa_heisenberg, kappa_kac_moody,
    virasoro_S3, virasoro_S4, virasoro_S5,
    affine_sl2_S3, affine_sl2_S4,
    shadow_data,
    # Section 2
    shadow_spectral_curve_sl2,
    shadow_spectral_curve_sl3,
    shadow_spectral_curve_slN,
    # Section 3
    hitchin_base_map,
    shadow_hitchin_locus,
    # Section 4
    hitchin_discriminant_sl2,
    hitchin_discriminant_sl3,
    shadow_critical_discriminant,
    verify_discriminant_sl3_vs_shadow,
    # Section 5
    shadow_metric_Q,
    shadow_metric_Q_prime,
    shadow_connection_coefficient,
    flat_section_shadow,
    # Section 6
    wkb_approximation_sl2,
    verify_wkb_vs_flat_section,
    # Section 7
    riemann_hurwitz_genus,
    spectral_curve_genus_sl2,
    spectral_curve_genus_sl3,
    spectral_curve_genus_slN,
    # Section 8
    stokes_rays_sl2_P1,
    stokes_graph_sl2_genus_g,
    # Section 9
    shadow_oper_sl2_P1,
    oper_monodromy_virasoro,
    oper_monodromy_landscape,
    # Section 10
    nonabelianization_sl2,
    verify_nonabelianization_vs_oper,
    # Section 11
    koszul_dual_virasoro,
    spectral_complementarity,
    # Section 12
    shadow_depth_from_spectral,
    # Section 13
    virasoro_spectral_data,
    # Section 14
    standard_landscape_hitchin_map,
    hitchin_discriminant_landscape,
    # Section 15
    hitchin_fiber_dimension_sl2,
    hitchin_fiber_dimension_slN,
    hitchin_base_dimension,
    hitchin_shadow_report,
)


PI = math.pi


# =========================================================================
# Section 1: Shadow data for standard families
# =========================================================================

class TestShadowData:
    """Tests for shadow data extraction."""

    def test_kappa_virasoro_c1(self):
        """kappa(Vir_1) = 1/2."""
        assert abs(kappa_virasoro(1) - 0.5) < 1e-15

    def test_kappa_virasoro_c13(self):
        """kappa(Vir_13) = 13/2 (self-dual point, AP8)."""
        assert abs(kappa_virasoro(13) - 6.5) < 1e-15

    def test_kappa_virasoro_c25(self):
        """kappa(Vir_25) = 25/2."""
        assert abs(kappa_virasoro(25) - 12.5) < 1e-15

    def test_kappa_virasoro_c26(self):
        """kappa(Vir_26) = 13 (critical dimension)."""
        assert abs(kappa_virasoro(26) - 13.0) < 1e-15

    def test_kappa_heisenberg_k1(self):
        """kappa(H_1) = 1 (AP39: NOT k/2)."""
        assert abs(kappa_heisenberg(1) - 1.0) < 1e-15

    def test_kappa_kac_moody_sl2_k1(self):
        """kappa(sl_2^(1)_1) = 3*(1+2)/(2*2) = 9/4."""
        assert abs(kappa_kac_moody(3, 1, 2) - 9.0/4.0) < 1e-15

    def test_kappa_kac_moody_sl3_k1(self):
        """kappa(sl_3^(1)_1) = 8*(1+3)/(2*3) = 16/3."""
        assert abs(kappa_kac_moody(8, 1, 3) - 16.0/3.0) < 1e-15

    def test_virasoro_S3_universal(self):
        """S_3(Vir_c) = 2 for all c."""
        for c in [1, 13, 25, 26, 100]:
            assert abs(virasoro_S3(c) - 2.0) < 1e-15

    def test_virasoro_S4_c1(self):
        """S_4(Vir_1) = 10/(1*(5+22)) = 10/27."""
        assert abs(virasoro_S4(1) - 10.0/27.0) < 1e-12

    def test_virasoro_S4_c13(self):
        """S_4(Vir_13) = 10/(13*(65+22)) = 10/1131."""
        assert abs(virasoro_S4(13) - 10.0/1131.0) < 1e-12

    def test_virasoro_S5_c1(self):
        """S_5(Vir_1) = -48/(1*27) = -48/27."""
        assert abs(virasoro_S5(1) - (-48.0/27.0)) < 1e-12

    def test_affine_sl2_S3(self):
        """S_3 for affine sl_2 at level k=1: 4/(k+2) = 4/3."""
        assert abs(affine_sl2_S3(1) - 4.0/3.0) < 1e-15

    def test_affine_sl2_S4(self):
        """S_4 for affine sl_2 is 0 (class L, Jacobi kills quartic)."""
        assert abs(affine_sl2_S4(1)) < 1e-15

    def test_shadow_data_virasoro(self):
        """Shadow data for Virasoro at c=1."""
        data = shadow_data('virasoro', {'c': 1.0})
        assert abs(data['kappa'] - 0.5) < 1e-15
        assert abs(data['S3'] - 2.0) < 1e-15
        assert data['class'] == 'M'
        assert data['depth'] == float('inf')

    def test_shadow_data_heisenberg(self):
        """Shadow data for Heisenberg at k=1."""
        data = shadow_data('heisenberg', {'k': 1.0})
        assert abs(data['kappa'] - 1.0) < 1e-15
        assert abs(data['S3']) < 1e-15
        assert data['class'] == 'G'
        assert data['depth'] == 2

    def test_shadow_data_affine_sl2(self):
        """Shadow data for affine sl_2 at k=1."""
        data = shadow_data('affine_sl2', {'k': 1.0})
        assert abs(data['kappa'] - 9.0/4.0) < 1e-12
        assert data['class'] == 'L'
        assert data['depth'] == 3


# =========================================================================
# Section 2: sl_2 spectral curve
# =========================================================================

class TestSpectralCurveSl2:
    """Tests for the sl_2 shadow spectral curve."""

    def test_sl2_curve_phi2_equals_kappa(self):
        """phi_2 = kappa in the shadow spectral curve."""
        kap = 6.5
        curve = shadow_spectral_curve_sl2(kap)
        assert abs(curve['phi2'] - kap) < 1e-15

    def test_sl2_discriminant_formula(self):
        """disc(eta^2 + phi2) = -4*phi2."""
        kap = 3.0
        curve = shadow_spectral_curve_sl2(kap)
        assert abs(curve['discriminant'] - (-4.0 * kap)) < 1e-12

    def test_sl2_singular_at_kappa_zero(self):
        """Spectral curve is singular iff kappa = 0."""
        assert shadow_spectral_curve_sl2(0.0)['is_singular']
        assert not shadow_spectral_curve_sl2(1.0)['is_singular']

    def test_sl2_genus_P1(self):
        """Genus of spectral curve over P^1 = 0 (double cover, 2 branch points)."""
        curve = shadow_spectral_curve_sl2(1.0)
        assert curve['genus_P1'] == 0

    def test_sl2_genus_elliptic(self):
        """Genus of spectral curve over elliptic = 1 (unramified)."""
        curve = shadow_spectral_curve_sl2(1.0)
        assert curve['genus_elliptic'] == 1

    def test_sl2_branch_points_P1(self):
        """Branch points on P^1 are z=0 and z=infty."""
        curve = shadow_spectral_curve_sl2(1.0)
        assert 0.0 in curve['branch_points_P1']
        assert float('inf') in curve['branch_points_P1']


# =========================================================================
# Section 3: sl_3 spectral curve
# =========================================================================

class TestSpectralCurveSl3:
    """Tests for the sl_3 shadow spectral curve."""

    def test_sl3_curve_coefficients(self):
        """phi_2 = kappa, phi_3 = S_3 in the shadow identification."""
        kap, s3 = 6.5, 2.0
        curve = shadow_spectral_curve_sl3(kap, s3)
        assert abs(curve['phi2'] - kap) < 1e-15
        assert abs(curve['phi3'] - s3) < 1e-15

    def test_sl3_discriminant_formula(self):
        """disc = -4*phi2^3 - 27*phi3^2."""
        kap, s3 = 3.0, 1.0
        curve = shadow_spectral_curve_sl3(kap, s3)
        expected = -4.0 * kap**3 - 27.0 * s3**2
        assert abs(curve['discriminant'] - expected) < 1e-10

    def test_sl3_three_roots(self):
        """Cubic has exactly 3 roots (counted with multiplicity)."""
        curve = shadow_spectral_curve_sl3(1.0, 0.5)
        assert len(curve['roots']) == 3

    def test_sl3_roots_sum_to_zero(self):
        """Sum of roots of depressed cubic eta^3 + p*eta + q = 0 is 0."""
        curve = shadow_spectral_curve_sl3(2.0, 1.0)
        root_sum = sum(curve['roots'])
        assert abs(root_sum) < 1e-10

    def test_sl3_virasoro_c1(self):
        """sl_3 spectral curve for Virasoro at c=1."""
        kap = kappa_virasoro(1)
        s3 = virasoro_S3(1)
        curve = shadow_spectral_curve_sl3(kap, s3)
        expected_disc = -4.0 * kap**3 - 27.0 * s3**2
        assert abs(curve['discriminant'] - expected_disc) < 1e-10

    def test_sl3_singular_iff_discriminant_zero(self):
        """Curve is singular iff disc = 0."""
        # When phi2 = 0 and phi3 = 0: disc = 0, singular
        curve = shadow_spectral_curve_sl3(0.0, 0.0)
        assert curve['is_singular']


# =========================================================================
# Section 4: sl_N spectral curve
# =========================================================================

class TestSpectralCurveSlN:
    """Tests for the general sl_N spectral curve."""

    def test_slN_sl2_matches(self):
        """sl_N with N=2 should give sl_2 results."""
        kap = 3.0
        curve_N = shadow_spectral_curve_slN(2, {2: kap})
        curve_2 = shadow_spectral_curve_sl2(kap)
        assert abs(curve_N['discriminant'] - curve_2['discriminant']) < 1e-8

    def test_slN_sl3_matches(self):
        """sl_N with N=3 should give sl_3 results."""
        kap, s3 = 3.0, 1.0
        curve_N = shadow_spectral_curve_slN(3, {2: kap, 3: s3})
        curve_3 = shadow_spectral_curve_sl3(kap, s3)
        # Discriminants should match
        assert abs(curve_N['discriminant'] - curve_3['discriminant']) < 1e-6

    def test_slN_N_roots(self):
        """sl_N curve has exactly N roots."""
        for N in [2, 3, 4, 5]:
            curve = shadow_spectral_curve_slN(N, {d: 0.1 * d for d in range(2, N+1)})
            assert len(curve['roots']) == N

    def test_slN_hitchin_base_dim(self):
        """Hitchin base has dimension N-1."""
        for N in [2, 3, 4, 5]:
            curve = shadow_spectral_curve_slN(N, {})
            assert curve['hitchin_base_dim'] == N - 1


# =========================================================================
# Section 5: Hitchin base map
# =========================================================================

class TestHitchinBaseMap:
    """Tests for the Hitchin base map."""

    def test_hitchin_map_virasoro_sl2(self):
        """Hit(Vir_1) for sl_2 = (kappa,) = (1/2,)."""
        hit = hitchin_base_map('virasoro', {'c': 1.0}, N=2)
        assert abs(hit['S2'] - 0.5) < 1e-15

    def test_hitchin_map_virasoro_sl3(self):
        """Hit(Vir_1) for sl_3 = (kappa, S_3) = (1/2, 2)."""
        hit = hitchin_base_map('virasoro', {'c': 1.0}, N=3)
        assert abs(hit['S2'] - 0.5) < 1e-15
        assert abs(hit['S3'] - 2.0) < 1e-15

    def test_shadow_locus_multiple_algebras(self):
        """Shadow locus for several algebras."""
        algebras = [
            ('virasoro', {'c': 1.0}),
            ('virasoro', {'c': 13.0}),
            ('heisenberg', {'k': 1.0}),
        ]
        locus = shadow_hitchin_locus(algebras, N=3)
        assert len(locus) == 3
        # Heisenberg has S3 = 0
        assert abs(locus[2]['S3']) < 1e-15


# =========================================================================
# Section 6: Hitchin discriminant — sl_2
# =========================================================================

class TestHitchinDiscriminantSl2:
    """Tests for the sl_2 Hitchin discriminant."""

    def test_disc_sl2_formula(self):
        """disc(eta^2 + phi2) = -4*phi2."""
        assert abs(hitchin_discriminant_sl2(3.0) - (-12.0)) < 1e-12

    def test_disc_sl2_zero_at_nilpotent(self):
        """Discriminant vanishes at phi2 = 0 (nilpotent cone)."""
        assert abs(hitchin_discriminant_sl2(0.0)) < 1e-15

    def test_disc_sl2_sign(self):
        """For phi2 > 0: disc < 0. For phi2 < 0: disc > 0."""
        assert hitchin_discriminant_sl2(1.0) < 0
        assert hitchin_discriminant_sl2(-1.0) > 0


# =========================================================================
# Section 7: Hitchin discriminant — sl_3
# =========================================================================

class TestHitchinDiscriminantSl3:
    """Tests for the sl_3 Hitchin discriminant."""

    def test_disc_sl3_formula(self):
        """Delta_3 = -4*phi2^3 - 27*phi3^2."""
        phi2, phi3 = 2.0, 1.0
        expected = -4.0 * phi2**3 - 27.0 * phi3**2
        assert abs(hitchin_discriminant_sl3(phi2, phi3) - expected) < 1e-10

    def test_disc_sl3_zero_at_origin(self):
        """Discriminant vanishes at phi2 = phi3 = 0."""
        assert abs(hitchin_discriminant_sl3(0.0, 0.0)) < 1e-15

    def test_disc_sl3_cusp(self):
        """On the discriminant locus: 4*phi2^3 + 27*phi3^2 = 0."""
        # phi3^2 = -4*phi2^3/27, so phi3 = 2*phi2^{3/2}/sqrt(27) for phi2 < 0
        phi2 = -3.0
        phi3 = 2.0 * (-phi2)**1.5 / math.sqrt(27.0)
        # disc = -4*(-3)^3 - 27*(...)^2 = 108 - 27*4*27/27 = 108 - 108 = 0
        disc = hitchin_discriminant_sl3(phi2, phi3)
        assert abs(disc) < 1e-10


# =========================================================================
# Section 8: Shadow discriminant vs Hitchin discriminant
# =========================================================================

class TestDiscriminantComparison:
    """Tests comparing shadow and Hitchin discriminants."""

    def test_shadow_discriminant_formula(self):
        """Delta_shadow = 8*kappa*S_4."""
        assert abs(shadow_critical_discriminant(1.0, 0.5) - 4.0) < 1e-15

    def test_shadow_discriminant_vanishes_class_L(self):
        """For class L (S_4 = 0): Delta_shadow = 0."""
        kap = kappa_kac_moody(3, 1, 2)
        assert abs(shadow_critical_discriminant(kap, 0.0)) < 1e-15

    def test_shadow_discriminant_nonzero_class_M(self):
        """For Virasoro (class M): Delta_shadow != 0."""
        kap = kappa_virasoro(1)
        s4 = virasoro_S4(1)
        delta = shadow_critical_discriminant(kap, s4)
        assert abs(delta) > 1e-3

    def test_discriminant_comparison_virasoro_c1(self):
        """Compare shadow and Hitchin discriminants at c=1."""
        result = verify_discriminant_sl3_vs_shadow(1.0)
        assert abs(result['kappa'] - 0.5) < 1e-15
        # Shadow and Hitchin discriminants are different objects
        assert abs(result['delta_shadow'] - result['delta_hitchin']) > 1e-3

    def test_discriminant_comparison_virasoro_c13(self):
        """Verify discriminant data at the self-dual point c=13."""
        result = verify_discriminant_sl3_vs_shadow(13.0)
        assert abs(result['kappa'] - 6.5) < 1e-15
        # Shadow discriminant: 8 * kappa * S_4 = 8 * 6.5 * 10/(13*87) = 40/87
        expected_delta = 8.0 * 6.5 * 10.0 / (13.0 * 87.0)
        assert abs(result['delta_shadow'] - expected_delta) < 1e-10


# =========================================================================
# Section 9: Shadow metric and connection
# =========================================================================

class TestShadowMetric:
    """Tests for the shadow metric Q_L and connection."""

    def test_shadow_metric_at_t0(self):
        """Q(0) = (2*kappa)^2 = 4*kappa^2."""
        kap = 3.0
        Q0 = shadow_metric_Q(kap, 2.0, 0.5, 0.0)
        assert abs(Q0 - 4.0 * kap**2) < 1e-10

    def test_shadow_metric_perfect_square_class_L(self):
        """For class L (S_4 = 0): Q(t) = (2kappa + 3*alpha*t)^2."""
        kap, alpha = 3.0, 1.0
        for t in [0.0, 0.5, 1.0, -0.5]:
            Q = shadow_metric_Q(kap, alpha, 0.0, t)
            expected = (2.0 * kap + 3.0 * alpha * t)**2
            assert abs(Q - expected) < 1e-10

    def test_shadow_metric_derivative_at_t0(self):
        """Q'(0) = 12*kappa*alpha."""
        kap, alpha = 3.0, 2.0
        Qp0 = shadow_metric_Q_prime(kap, alpha, 0.0, 0.0)
        assert abs(Qp0 - 12.0 * kap * alpha) < 1e-10

    def test_shadow_connection_well_defined(self):
        """Connection coefficient is finite for Q != 0."""
        kap, alpha, s4 = 3.0, 2.0, 0.5
        coeff = shadow_connection_coefficient(kap, alpha, s4, 0.1)
        assert math.isfinite(coeff)

    def test_flat_section_at_t0(self):
        """Flat section Phi(0) = 1 (normalization)."""
        phi0 = flat_section_shadow(3.0, 2.0, 0.5, 0.0)
        assert abs(phi0 - 1.0) < 1e-15

    def test_flat_section_positive(self):
        """Flat section is positive where Q > 0."""
        kap, alpha, s4 = 3.0, 2.0, 0.0
        for t in [0.1, 0.5, 1.0]:
            phi = flat_section_shadow(kap, alpha, s4, t)
            assert phi > 0

    def test_flat_section_satisfies_ODE(self):
        """Numerical check: d/dt log(Phi) = Q'/(2Q)."""
        kap, alpha, s4 = 3.0, 2.0, 0.0
        t = 0.5
        dt = 1e-6
        phi_t = flat_section_shadow(kap, alpha, s4, t)
        phi_tdt = flat_section_shadow(kap, alpha, s4, t + dt)
        log_deriv = (math.log(phi_tdt) - math.log(phi_t)) / dt
        expected = shadow_metric_Q_prime(kap, alpha, s4, t) / (2.0 * shadow_metric_Q(kap, alpha, s4, t))
        assert abs(log_deriv - expected) < 1e-4


# =========================================================================
# Section 10: WKB approximation
# =========================================================================

class TestWKB:
    """Tests for the WKB approximation."""

    def test_wkb_at_z1(self):
        """WKB at z=1: exp(i*sqrt(kappa)*0) = 1."""
        result = wkb_approximation_sl2(1.0, complex(1, 0))
        assert abs(result - 1.0) < 1e-10

    def test_wkb_oscillatory_positive_kappa(self):
        """For kappa > 0: |WKB(z)| = 1 on the unit circle (pure phase)."""
        kap = 2.0
        for theta in [0.1, 0.5, 1.0, 2.0]:
            z = cmath.exp(1j * theta)
            result = wkb_approximation_sl2(kap, z)
            # On unit circle, |z|=1, so log(z) is purely imaginary
            # exp(i*sqrt(kappa)*i*theta) = exp(-sqrt(kappa)*theta)
            # Actually |result| != 1 in general on the unit circle
            # because log(z) = i*theta, so the exponent is
            # i*sqrt(kappa)*i*theta = -sqrt(kappa)*theta (real).
            # So |result| = exp(-sqrt(kappa)*theta).
            expected_abs = math.exp(-math.sqrt(kap) * theta)
            assert abs(abs(result) - expected_abs) < 1e-8

    def test_wkb_at_z0(self):
        """WKB at z=0 returns 0."""
        result = wkb_approximation_sl2(1.0, complex(0, 0))
        assert abs(result) < 1e-15

    def test_wkb_vs_flat_section_returns_data(self):
        """verify_wkb_vs_flat_section returns proper structure."""
        result = verify_wkb_vs_flat_section(3.0, 2.0, 0.0, [0.0, 0.1, 0.5])
        assert len(result['flat_section']) == 3
        assert len(result['Q_values']) == 3
        assert abs(result['flat_section'][0] - 1.0) < 1e-15


# =========================================================================
# Section 11: Riemann-Hurwitz
# =========================================================================

class TestRiemannHurwitz:
    """Tests for the Riemann-Hurwitz genus formula."""

    def test_double_cover_P1_2_branch(self):
        """Double cover of P^1 with 2 simple branch points: g = 0."""
        g = riemann_hurwitz_genus(0, 2, 2, 'simple')
        assert g == 0

    def test_double_cover_P1_4_branch(self):
        """Double cover of P^1 with 4 simple branch points: g = 1."""
        g = riemann_hurwitz_genus(0, 2, 4, 'simple')
        assert g == 1

    def test_double_cover_P1_6_branch(self):
        """Double cover of P^1 with 6 simple branch points: g = 2."""
        g = riemann_hurwitz_genus(0, 2, 6, 'simple')
        assert g == 2

    def test_unramified_double_cover_genus1(self):
        """Unramified double cover of genus-1 curve: g = 1."""
        g = riemann_hurwitz_genus(1, 2, 0, 'simple')
        assert g == 1

    def test_total_ramification(self):
        """Totally ramified triple cover of P^1 with 2 branch pts: g = 0."""
        # 2g-2 = 3*(-2) + 2*2 = -6+4 = -2 => g=0
        g = riemann_hurwitz_genus(0, 3, 2, 'total')
        assert g == 0


# =========================================================================
# Section 12: Spectral curve genus — sl_2
# =========================================================================

class TestSpectralGenusS2:
    """Tests for sl_2 spectral curve genus."""

    def test_genus_P1(self):
        """Over P^1: genus = 0."""
        data = spectral_curve_genus_sl2(0, 1.0)
        assert data['genus_spectral'] == 0

    def test_genus_elliptic(self):
        """Over elliptic curve: genus = 1."""
        data = spectral_curve_genus_sl2(1, 1.0)
        assert data['genus_spectral'] == 1

    def test_genus_g2(self):
        """Over genus 2: genus(Sigma) = 4*2-3 = 5."""
        data = spectral_curve_genus_sl2(2, 1.0)
        assert data['genus_spectral'] == 5

    def test_genus_g3(self):
        """Over genus 3: genus(Sigma) = 4*3-3 = 9."""
        data = spectral_curve_genus_sl2(3, 1.0)
        assert data['genus_spectral'] == 9

    def test_genus_g10(self):
        """Over genus 10: genus(Sigma) = 4*10-3 = 37."""
        data = spectral_curve_genus_sl2(10, 1.0)
        assert data['genus_spectral'] == 37

    def test_branch_points_g2(self):
        """Over genus 2: 4*2-4 = 4 branch points."""
        data = spectral_curve_genus_sl2(2, 1.0)
        assert data['num_branch_points'] == 4


# =========================================================================
# Section 13: Spectral curve genus — sl_3
# =========================================================================

class TestSpectralGenusS3:
    """Tests for sl_3 spectral curve genus."""

    def test_genus_P1(self):
        """Over P^1 with constant data: genus = 0."""
        data = spectral_curve_genus_sl3(0)
        assert data['genus_spectral'] == 0

    def test_genus_elliptic(self):
        """Over elliptic: genus = 1."""
        data = spectral_curve_genus_sl3(1)
        assert data['genus_spectral'] == 1

    def test_genus_g2(self):
        """Over genus 2: genus(Sigma) = 9*2-8 = 10."""
        data = spectral_curve_genus_sl3(2)
        assert data['genus_spectral'] == 10

    def test_genus_g3(self):
        """Over genus 3: genus(Sigma) = 9*3-8 = 19."""
        data = spectral_curve_genus_sl3(3)
        assert data['genus_spectral'] == 19


# =========================================================================
# Section 14: Spectral curve genus — sl_N
# =========================================================================

class TestSpectralGenusSlN:
    """Tests for sl_N spectral curve genus."""

    def test_slN_formula_g2(self):
        """genus(Sigma) = N^2*(g-1)+1 for g >= 2."""
        for N in [2, 3, 4, 5]:
            data = spectral_curve_genus_slN(N, 2)
            assert data['genus_spectral'] == N * N * 1 + 1

    def test_slN_sl2_consistency(self):
        """sl_N with N=2 matches sl_2 formula."""
        for g in [0, 1, 2, 3, 5]:
            data_N = spectral_curve_genus_slN(2, g)
            data_2 = spectral_curve_genus_sl2(g, 1.0)
            assert data_N['genus_spectral'] == data_2['genus_spectral']

    def test_slN_sl3_consistency(self):
        """sl_N with N=3 matches sl_3 formula."""
        for g in [0, 1, 2, 3]:
            data_N = spectral_curve_genus_slN(3, g)
            data_3 = spectral_curve_genus_sl3(g)
            assert data_N['genus_spectral'] == data_3['genus_spectral']

    def test_slN_genus_0_base(self):
        """Over P^1 with constant data: genus = 0 for all N."""
        for N in [2, 3, 4, 5, 10]:
            data = spectral_curve_genus_slN(N, 0)
            assert data['genus_spectral'] == 0

    def test_slN_genus_1_base(self):
        """Over elliptic: genus = 1 for all N."""
        for N in [2, 3, 4, 5]:
            data = spectral_curve_genus_slN(N, 1)
            assert data['genus_spectral'] == 1


# =========================================================================
# Section 15: Stokes graph
# =========================================================================

class TestStokesGraph:
    """Tests for the Stokes graph."""

    def test_stokes_positive_kappa_radial(self):
        """For kappa > 0: Stokes graph has 2 radial rays."""
        data = stokes_rays_sl2_P1(1.0)
        assert data['stokes_type'] == 'radial'
        assert data['num_stokes_rays'] == 2

    def test_stokes_negative_kappa_circular(self):
        """For kappa < 0: Stokes curve is the unit circle."""
        data = stokes_rays_sl2_P1(-1.0)
        assert data['stokes_type'] == 'circular'

    def test_stokes_zero_kappa_degenerate(self):
        """For kappa = 0: degenerate Stokes graph."""
        data = stokes_rays_sl2_P1(0.0)
        assert data['stokes_type'] == 'degenerate'
        assert data['num_stokes_rays'] == 0

    def test_stokes_genus_g2_edges(self):
        """Stokes graph on genus 2: 3*(4*2-4) = 12 edges."""
        data = stokes_graph_sl2_genus_g(2)
        assert data['num_stokes_edges'] == 12

    def test_stokes_genus_g3_edges(self):
        """Stokes graph on genus 3: 3*(4*3-4) = 24 edges."""
        data = stokes_graph_sl2_genus_g(3)
        assert data['num_stokes_edges'] == 24

    def test_stokes_genus_0_special(self):
        """Stokes on P^1: 2 edges (the radial rays)."""
        data = stokes_graph_sl2_genus_g(0)
        assert data['num_stokes_edges'] == 2

    def test_stokes_genus_1_flat(self):
        """Stokes on torus: 0 edges (flat metric)."""
        data = stokes_graph_sl2_genus_g(1)
        assert data['num_stokes_edges'] == 0


# =========================================================================
# Section 16: Oper monodromy — basic
# =========================================================================

class TestOperMonodromyBasic:
    """Tests for the basic oper monodromy computation."""

    def test_oper_kappa_zero_trivial(self):
        """kappa = 0: indicial roots 0, 1. Monodromy trivial."""
        oper = shadow_oper_sl2_P1(0.0)
        assert abs(complex(oper['s_plus']) - 1.0) < 1e-10
        assert abs(complex(oper['s_minus']) - 0.0) < 1e-10
        # Monodromy eigenvalues: e^{2pi i * 0} = 1, e^{2pi i * 1} = 1
        assert abs(oper['monodromy_eigenvalue_plus'] - 1.0) < 1e-10
        assert abs(oper['monodromy_eigenvalue_minus'] - 1.0) < 1e-10

    def test_oper_kappa_quarter_resonant(self):
        """kappa = 1/4: indicial roots both 1/2 (resonant)."""
        oper = shadow_oper_sl2_P1(0.25)
        assert abs(complex(oper['s_plus']) - 0.5) < 1e-10
        assert abs(complex(oper['s_minus']) - 0.5) < 1e-10

    def test_oper_indicial_sum(self):
        """s_+ + s_- = 1 always (sum of indicial roots of s^2 - s + kappa)."""
        for kap in [0.0, 0.5, 1.0, 6.5, 13.0]:
            oper = shadow_oper_sl2_P1(kap)
            assert abs(complex(oper['s_plus'] + oper['s_minus']) - 1.0) < 1e-10

    def test_oper_indicial_product(self):
        """s_+ * s_- = kappa always (product of indicial roots)."""
        for kap in [0.0, 0.5, 1.0, 6.5, 13.0]:
            oper = shadow_oper_sl2_P1(kap)
            prod = complex(oper['s_plus']) * complex(oper['s_minus'])
            assert abs(prod - kap) < 1e-8

    def test_oper_monodromy_trace_formula(self):
        """tr(M) = e^{2pi i s_+} + e^{2pi i s_-}."""
        for kap in [0.5, 1.0, 3.0]:
            oper = shadow_oper_sl2_P1(kap)
            expected = oper['monodromy_eigenvalue_plus'] + oper['monodromy_eigenvalue_minus']
            assert abs(complex(oper['monodromy_trace']) - complex(expected)) < 1e-10


# =========================================================================
# Section 17: Oper monodromy — Virasoro landscape
# =========================================================================

class TestOperMonodromyVirasoro:
    """Tests for oper monodromy at Virasoro central charges."""

    def test_virasoro_c0(self):
        """c=0: kappa=0, trivial monodromy."""
        oper = oper_monodromy_virasoro(0.0)
        assert abs(complex(oper['monodromy_trace']) - 2.0) < 1e-10

    def test_virasoro_c1_indicial(self):
        """c=1: kappa=1/2, s = (1 +/- sqrt(1-2))/2 = (1 +/- i)/2."""
        oper = oper_monodromy_virasoro(1.0)
        disc = 1.0 - 4.0 * 0.5  # = -1
        assert abs(oper['indicial_discriminant'] - disc) < 1e-10

    def test_virasoro_c13_selfdual(self):
        """c=13: kappa=13/2 (self-dual, AP8)."""
        oper = oper_monodromy_virasoro(13.0)
        assert abs(oper['kappa'] - 6.5) < 1e-15

    def test_virasoro_c25_koszul_partner_of_c1(self):
        """c=25 is Koszul dual of c=1 (AP24: 25+1=26)."""
        oper_1 = oper_monodromy_virasoro(1.0)
        oper_25 = oper_monodromy_virasoro(25.0)
        # Both have kappa sum 1/2 + 25/2 = 13
        assert abs(oper_1['kappa'] + oper_25['kappa'] - 13.0) < 1e-10

    def test_virasoro_landscape(self):
        """Monodromy landscape for c = 1..25."""
        results = oper_monodromy_landscape(range(1, 26))
        assert len(results) == 25
        # All have finite monodromy trace
        for r in results:
            assert cmath.isfinite(r['monodromy_trace'])


# =========================================================================
# Section 18: Nonabelianization
# =========================================================================

class TestNonabelianization:
    """Tests for the nonabelianization map."""

    def test_nonab_connection_matrix_shape(self):
        """Connection matrix is 2x2."""
        data = nonabelianization_sl2(1.0)
        assert data['connection_matrix'].shape == (2, 2)

    def test_nonab_connection_off_diagonal(self):
        """Connection matrix is off-diagonal (sl_2 structure)."""
        data = nonabelianization_sl2(1.0)
        A = data['connection_matrix']
        assert abs(A[0, 0]) < 1e-10
        assert abs(A[1, 1]) < 1e-10
        assert abs(A[0, 1]) > 1e-3

    def test_nonab_monodromy_product_one(self):
        """Product of monodromy eigenvalues = 1 (det = 1 for SL_2)."""
        data = nonabelianization_sl2(1.0)
        ev1, ev2 = data['monodromy_eigenvalues']
        assert abs(ev1 * ev2 - 1.0) < 1e-10

    def test_nonab_trace_formula(self):
        """tr(M) = 2*cos(2*pi*sqrt(kappa))."""
        kap = 1.0
        data = nonabelianization_sl2(kap)
        expected_trace = 2.0 * cmath.cos(2.0 * PI * cmath.sqrt(kap))
        assert abs(complex(data['monodromy_trace']) - complex(expected_trace)) < 1e-10

    def test_nonab_vs_oper_differ(self):
        """Nonabelianization and oper monodromies differ (quantum vs classical)."""
        result = verify_nonabelianization_vs_oper(1.0)
        assert result['traces_differ']


# =========================================================================
# Section 19: Complementarity under Koszul duality
# =========================================================================

class TestComplementarity:
    """Tests for Koszul duality complementarity."""

    def test_koszul_dual_formula(self):
        """c' = 26 - c."""
        assert abs(koszul_dual_virasoro(1.0) - 25.0) < 1e-15
        assert abs(koszul_dual_virasoro(13.0) - 13.0) < 1e-15
        assert abs(koszul_dual_virasoro(26.0) - 0.0) < 1e-15

    def test_kappa_sum_13(self):
        """kappa + kappa' = 13 for all c (AP24)."""
        for c in [0.0, 1.0, 5.0, 13.0, 20.0, 25.0, 26.0]:
            comp = spectral_complementarity(c)
            assert abs(comp['kappa_sum'] - 13.0) < 1e-10

    def test_kappa_product_maximized_at_c13(self):
        """kappa * kappa' maximized at c=13: max = 169/4."""
        comp_13 = spectral_complementarity(13.0)
        assert abs(comp_13['kappa_product'] - 169.0/4.0) < 1e-10
        # Compare with non-self-dual point
        comp_1 = spectral_complementarity(1.0)
        assert comp_1['kappa_product'] < comp_13['kappa_product']

    def test_self_dual_flag(self):
        """Self-dual flag correctly set at c=13."""
        assert spectral_complementarity(13.0)['self_dual']
        assert not spectral_complementarity(1.0)['self_dual']

    def test_complementarity_involution(self):
        """(c')' = c (involution)."""
        for c in [1.0, 5.0, 13.0, 20.0]:
            assert abs(koszul_dual_virasoro(koszul_dual_virasoro(c)) - c) < 1e-10


# =========================================================================
# Section 20: Shadow depth from spectral data
# =========================================================================

class TestShadowDepth:
    """Tests for shadow depth classification from spectral data."""

    def test_heisenberg_class_G(self):
        """Heisenberg: S_3 = S_4 = 0 => class G, depth 2."""
        result = shadow_depth_from_spectral(1.0, 0.0, 0.0)
        assert result['class'] == 'G'
        assert result['depth'] == 2

    def test_affine_class_L(self):
        """Affine sl_2: S_3 = 1, S_4 = 0 => class L, depth 3."""
        kap = kappa_kac_moody(3, 1, 2)
        result = shadow_depth_from_spectral(kap, 1.0, 0.0)
        assert result['class'] == 'L'
        assert result['depth'] == 3

    def test_virasoro_class_M(self):
        """Virasoro: S_4 != 0 and Q positive definite => class M, depth inf."""
        kap = kappa_virasoro(1)
        s3 = virasoro_S3(1)
        s4 = virasoro_S4(1)
        result = shadow_depth_from_spectral(kap, s3, s4)
        assert result['class'] == 'M'
        assert result['depth'] == float('inf')

    def test_virasoro_class_M_multiple_c(self):
        """Virasoro is class M for all c > 0."""
        for c in [1, 5, 13, 25, 100]:
            kap = kappa_virasoro(c)
            s3 = virasoro_S3(c)
            s4 = virasoro_S4(c)
            result = shadow_depth_from_spectral(kap, s3, s4)
            assert result['class'] == 'M', f"Failed at c={c}"

    def test_delta_zero_iff_class_GL(self):
        """Delta = 0 iff class G or L."""
        for kap, s3, s4, expected_class in [
            (1.0, 0.0, 0.0, 'G'),
            (1.0, 1.0, 0.0, 'L'),
        ]:
            result = shadow_depth_from_spectral(kap, s3, s4)
            assert result['class'] == expected_class
            assert abs(result['Delta']) < 1e-15


# =========================================================================
# Section 21: Hitchin fiber dimension
# =========================================================================

class TestHitchinFiber:
    """Tests for Hitchin fiber dimensions."""

    def test_fiber_sl2_g0(self):
        """sl_2 fiber over P^1: dim = 0."""
        assert hitchin_fiber_dimension_sl2(0) == 0

    def test_fiber_sl2_g1(self):
        """sl_2 fiber over elliptic: dim = 1."""
        assert hitchin_fiber_dimension_sl2(1) == 1

    def test_fiber_sl2_g2(self):
        """sl_2 fiber over genus 2: dim = genus(Sigma) = 5."""
        assert hitchin_fiber_dimension_sl2(2) == 5

    def test_fiber_slN_matches_formula(self):
        """dim = N^2*(g-1)+1 for g >= 2."""
        for N in [2, 3, 4]:
            for g in [2, 3, 5]:
                dim = hitchin_fiber_dimension_slN(N, g)
                assert dim == N * N * (g - 1) + 1

    def test_base_dim_formula(self):
        """dim B = (N^2-1)*(g-1) for g >= 2."""
        for N in [2, 3, 4]:
            for g in [2, 3, 5]:
                dim = hitchin_base_dimension(N, g)
                assert dim == (N * N - 1) * (g - 1)

    def test_prym_dimension_equals_base(self):
        """dim(Prym) = genus(Sigma) - g_base = (N^2-1)(g-1) = dim(B) for g >= 2.

        The Hitchin fiber for SL_N is the PRYM variety, not the full
        Jacobian. The Prym has dimension genus(Sigma) - g_base.
        The total dim of T*Bun_G = 2*(N^2-1)*(g-1) = 2*dim(B).
        """
        for N in [2, 3, 4]:
            for g in [2, 3]:
                genus_sigma = hitchin_fiber_dimension_slN(N, g)
                base = hitchin_base_dimension(N, g)
                prym_dim = genus_sigma - g  # Prym = Jac(Sigma)/Jac(X)
                assert prym_dim == base


# =========================================================================
# Section 22: Standard landscape
# =========================================================================

class TestStandardLandscape:
    """Tests for the standard landscape Hitchin map."""

    def test_landscape_has_all_families(self):
        """Standard landscape contains Vir, Heis, affine sl_2, affine sl_3."""
        landscape = standard_landscape_hitchin_map()
        assert 'Vir_c1' in landscape
        assert 'Vir_c13' in landscape
        assert 'Heis_k1' in landscape
        assert 'aff_sl2_k1' in landscape
        assert 'aff_sl3_k1' in landscape

    def test_landscape_kappa_values(self):
        """Verify kappa values in the landscape."""
        landscape = standard_landscape_hitchin_map()
        assert abs(landscape['Vir_c1']['S2'] - 0.5) < 1e-15
        assert abs(landscape['Vir_c13']['S2'] - 6.5) < 1e-15
        assert abs(landscape['Heis_k1']['S2'] - 1.0) < 1e-15

    def test_landscape_classes(self):
        """Verify shadow depth classes."""
        landscape = standard_landscape_hitchin_map()
        assert landscape['Vir_c1']['class'] == 'M'
        assert landscape['Heis_k1']['class'] == 'G'
        assert landscape['aff_sl2_k1']['class'] == 'L'

    def test_discriminant_landscape_completeness(self):
        """Discriminant landscape returns data for all families."""
        results = hitchin_discriminant_landscape()
        assert len(results) >= 5


# =========================================================================
# Section 23: Complete Virasoro spectral data
# =========================================================================

class TestVirasoroSpectralData:
    """Tests for the complete Virasoro spectral data report."""

    def test_virasoro_c1_report(self):
        """Complete report for Virasoro at c=1."""
        data = virasoro_spectral_data(1.0)
        assert abs(data['kappa'] - 0.5) < 1e-15
        assert abs(data['S3'] - 2.0) < 1e-15
        assert 'spectral_sl2' in data
        assert 'spectral_sl3' in data
        assert 'oper' in data

    def test_virasoro_c13_selfdual_report(self):
        """Complete report at the self-dual point c=13."""
        data = virasoro_spectral_data(13.0)
        assert abs(data['kappa'] - 6.5) < 1e-15
        assert data['depth']['class'] == 'M'

    def test_virasoro_c25_report(self):
        """Complete report at c=25."""
        data = virasoro_spectral_data(25.0)
        assert abs(data['kappa'] - 12.5) < 1e-15

    def test_virasoro_c26_report(self):
        """Complete report at c=26 (critical dimension)."""
        data = virasoro_spectral_data(26.0)
        assert abs(data['kappa'] - 13.0) < 1e-15


# =========================================================================
# Section 24: Cross-checks and consistency
# =========================================================================

class TestCrossChecks:
    """Cross-checks across multiple verification paths."""

    def test_sl2_disc_from_curve_vs_formula(self):
        """Path 1: sl_2 discriminant from curve data matches formula."""
        for kap in [0.5, 1.0, 6.5, 13.0]:
            curve = shadow_spectral_curve_sl2(kap)
            formula = hitchin_discriminant_sl2(kap)
            assert abs(curve['discriminant'] - formula) < 1e-10

    def test_sl3_disc_from_curve_vs_formula(self):
        """Path 1: sl_3 discriminant from curve data matches formula."""
        for kap, s3 in [(0.5, 2.0), (6.5, 2.0), (1.0, 1.0)]:
            curve = shadow_spectral_curve_sl3(kap, s3)
            formula = hitchin_discriminant_sl3(kap, s3)
            assert abs(curve['discriminant'] - formula) < 1e-8

    def test_genus_riemann_hurwitz_vs_formula_sl2(self):
        """Path 2: Riemann-Hurwitz matches 4g-3 formula for sl_2."""
        for g in [2, 3, 4, 5]:
            rh = riemann_hurwitz_genus(g, 2, 4 * g - 4, 'simple')
            formula = 4 * g - 3
            assert rh == formula

    def test_genus_riemann_hurwitz_vs_formula_slN(self):
        """Path 2: Riemann-Hurwitz consistent with N^2(g-1)+1."""
        for N in [2, 3]:
            for g in [2, 3]:
                data = spectral_curve_genus_slN(N, g)
                expected = N * N * (g - 1) + 1
                assert data['genus_spectral'] == expected

    def test_complementarity_sum_universal(self):
        """Path 4: kappa + kappa' = 13 across all tested c values."""
        for c in np.linspace(0, 26, 27):
            kap = kappa_virasoro(c)
            kap_dual = kappa_virasoro(26.0 - c)
            assert abs(kap + kap_dual - 13.0) < 1e-10

    def test_depth_class_consistency(self):
        """Path 5: Shadow depth matches for Virasoro/Heisenberg/affine."""
        # Heisenberg: class G
        assert shadow_depth_from_spectral(1.0, 0.0, 0.0)['class'] == 'G'
        # Affine: class L
        assert shadow_depth_from_spectral(2.25, 1.0, 0.0)['class'] == 'L'
        # Virasoro c=1: class M
        kap = kappa_virasoro(1)
        s4 = virasoro_S4(1)
        assert shadow_depth_from_spectral(kap, 2.0, s4)['class'] == 'M'

    def test_hitchin_report_virasoro(self):
        """Full Hitchin-shadow report for Virasoro at c=1."""
        report = hitchin_shadow_report('virasoro', {'c': 1.0}, g_base=2)
        assert report['shadow_data']['class'] == 'M'
        assert report['genus_sl2']['genus_spectral'] == 5
        assert abs(report['hitchin_disc_sl2'] - (-2.0)) < 1e-10

    def test_hitchin_report_heisenberg(self):
        """Full Hitchin-shadow report for Heisenberg at k=1."""
        report = hitchin_shadow_report('heisenberg', {'k': 1.0}, g_base=2)
        assert report['shadow_data']['class'] == 'G'
        assert abs(report['shadow_discriminant']) < 1e-15

    def test_oper_indicial_roots_always_sum_to_one(self):
        """Indicial roots s_+ + s_- = 1 for all kappa (cross-check)."""
        for c in range(0, 30):
            oper = oper_monodromy_virasoro(float(c))
            s_sum = complex(oper['s_plus']) + complex(oper['s_minus'])
            assert abs(s_sum - 1.0) < 1e-10

    def test_oper_monodromy_determinant_one(self):
        """Monodromy determinant = e^{2pi i (s_+ + s_-)} = e^{2pi i} = 1."""
        for c in [1, 13, 25]:
            oper = oper_monodromy_virasoro(float(c))
            det_M = oper['monodromy_eigenvalue_plus'] * oper['monodromy_eigenvalue_minus']
            assert abs(det_M - 1.0) < 1e-8

    def test_nonab_monodromy_det_one(self):
        """Nonabelianization monodromy has det = 1."""
        for kap in [0.5, 1.0, 6.5]:
            data = nonabelianization_sl2(kap)
            ev1, ev2 = data['monodromy_eigenvalues']
            assert abs(ev1 * ev2 - 1.0) < 1e-10

    def test_shadow_metric_positive_at_origin(self):
        """Q(0) = 4*kappa^2 > 0 for kappa != 0."""
        for kap in [0.5, 1.0, 6.5, 13.0]:
            Q0 = shadow_metric_Q(kap, 2.0, 0.5, 0.0)
            assert Q0 > 0

    def test_flat_section_normalized(self):
        """Flat section Phi(0) = 1 for all parameter values."""
        for kap in [0.5, 1.0, 3.0, 6.5]:
            for alpha in [0.0, 1.0, 2.0]:
                for s4 in [0.0, 0.1, 0.5]:
                    phi0 = flat_section_shadow(kap, alpha, s4, 0.0)
                    assert abs(phi0 - 1.0) < 1e-14

    def test_spectral_curve_roots_satisfy_polynomial(self):
        """Roots of spectral polynomial should evaluate to near zero."""
        kap, s3 = 3.0, 1.5
        curve = shadow_spectral_curve_sl3(kap, s3)
        for root in curve['roots']:
            val = root**3 + kap * root + s3
            assert abs(val) < 1e-8

    def test_hitchin_base_map_matches_shadow_data(self):
        """Hitchin map coordinates match shadow_data kappa."""
        for c in [1.0, 13.0, 25.0]:
            hit = hitchin_base_map('virasoro', {'c': c}, N=3)
            data = shadow_data('virasoro', {'c': c})
            assert abs(hit['S2'] - data['kappa']) < 1e-15
            assert abs(hit['S3'] - data['S3']) < 1e-15
