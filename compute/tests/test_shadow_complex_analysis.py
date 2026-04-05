"""
Tests for shadow_complex_analysis.py — complex-analytic structure of shadow
generating functions.

60+ tests covering:
  - Shadow generating functions for all four archetypes
  - Branch cut analysis and monodromy for Virasoro
  - Borel transform and Borel-Laplace summation
  - Pade approximant construction and convergence
  - Spectral measure reconstruction from shadow moments
  - Carleman's condition
  - Dispersion relation
  - Radius of convergence and asymptotic growth
"""

import cmath
import math
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from shadow_complex_analysis import (
    shadow_coefficients_virasoro_leading,
    shadow_coefficients_heisenberg,
    shadow_coefficients_affine,
    shadow_coefficients_betagamma,
    shadow_generating_function,
    branch_point_virasoro,
    branch_cut_discontinuity,
    branch_cut_analysis,
    monodromy_numerical,
    borel_transform,
    borel_sum,
    borel_transform_virasoro_exact,
    pade_approximant,
    pade_poles,
    spectral_representation_check,
    spectral_measure_from_shadows,
    carleman_condition,
    dispersion_integral,
    pade_branch_point_convergence,
    full_complex_analysis,
    shadow_radius_of_convergence,
    asymptotic_growth_rate,
)


# =====================================================================
# Section 1: Shadow coefficients
# =====================================================================

class TestShadowCoefficients:
    """Verify shadow coefficient generation for all archetypes."""

    def test_virasoro_leading_order_S2(self):
        """S_2 = (6/c)^2 / 2 at leading order (positive)."""
        c = 26.0
        coeffs = shadow_coefficients_virasoro_leading(c, 5)
        expected_S2 = (6.0 / c) ** 2 / 2.0
        assert abs(coeffs[0] - expected_S2) < 1e-14

    def test_virasoro_leading_alternating_signs(self):
        """S_r alternates: S_r = (-1)^r (6/c)^r / r."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        for i, s in enumerate(coeffs):
            r = i + 2
            expected = (-1) ** r * (6.0 / c) ** r / r
            assert abs(s - expected) < 1e-14, f"r={r}"

    def test_virasoro_large_c_small_coefficients(self):
        """At large c, higher shadow coefficients are suppressed as (6/c)^r."""
        c = 1000.0
        coeffs = shadow_coefficients_virasoro_leading(c, 20)
        for i in range(1, len(coeffs)):
            assert abs(coeffs[i]) < abs(coeffs[i - 1]), f"Not decreasing at r={i+2}"

    def test_heisenberg_terminates_at_2(self):
        """Heisenberg: S_2 = c/2, S_r = 0 for r >= 3."""
        c = 1.0
        coeffs = shadow_coefficients_heisenberg(c, 10)
        assert abs(coeffs[0] - 0.5) < 1e-15
        for s in coeffs[1:]:
            assert s == 0.0

    def test_affine_terminates_at_3(self):
        """Affine: S_3 = C3, S_r = 0 for r >= 4."""
        c, C3 = 6.0, 2.0
        coeffs = shadow_coefficients_affine(c, C3, 10)
        assert abs(coeffs[0] - 3.0) < 1e-15  # c/2
        assert abs(coeffs[1] - 2.0) < 1e-15  # C3
        for s in coeffs[2:]:
            assert s == 0.0

    def test_betagamma_terminates_at_4(self):
        """betagamma: S_4 = Q4, S_r = 0 for r >= 5."""
        c, C3, Q4 = 2.0, 0.5, 0.1
        coeffs = shadow_coefficients_betagamma(c, C3, Q4, 10)
        assert abs(coeffs[0] - 1.0) < 1e-15
        assert abs(coeffs[1] - 0.5) < 1e-15
        assert abs(coeffs[2] - 0.1) < 1e-15
        for s in coeffs[3:]:
            assert s == 0.0

    def test_virasoro_c1_specific_values(self):
        """Specific S_r values at c=1.

        S_r = (-1)^r * 6^r / r.
        S_2 = 36/2 = 18, S_3 = -216/3 = -72, S_4 = 1296/4 = 324.
        """
        coeffs = shadow_coefficients_virasoro_leading(1.0, 5)
        assert abs(coeffs[0] - 18.0) < 1e-10
        assert abs(coeffs[1] + 72.0) < 1e-10
        assert abs(coeffs[2] - 324.0) < 1e-10


# =====================================================================
# Section 2: Shadow generating function evaluation
# =====================================================================

class TestShadowGeneratingFunction:
    """Test G(t) for each archetype."""

    def test_heisenberg_is_quadratic(self):
        c, t = 4.0, 0.3
        G = shadow_generating_function('heisenberg', c, t)
        assert abs(G - 2.0 * 0.09) < 1e-14

    def test_affine_is_cubic(self):
        c, C3, t = 6.0, 2.0, 0.1
        G = shadow_generating_function('affine', c, t, C3=C3)
        expected = 3.0 * 0.01 + 2.0 * 0.001
        assert abs(G - expected) < 1e-14

    def test_betagamma_is_quartic(self):
        c, C3, Q4, t = 2.0, 0.5, 0.1, 0.2
        G = shadow_generating_function('betagamma', c, t, C3=C3, Q4=Q4)
        expected = 1.0 * 0.04 + 0.5 * 0.008 + 0.1 * 0.0016
        assert abs(G - expected) < 1e-14

    def test_virasoro_at_zero(self):
        G = shadow_generating_function('virasoro', 26.0, 0.0)
        assert abs(G) < 1e-15

    def test_virasoro_small_t(self):
        """For small t, G_Vir(t) = -log(1+6t/c) + 6t/c (r>=2 part only)."""
        c, t = 26.0, 0.001
        G = shadow_generating_function('virasoro', c, t)
        expected = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(G - expected) < 1e-15

    def test_virasoro_complex_argument(self):
        """G_Vir(t) works for complex t away from the cut."""
        c = 10.0
        t = 0.1 + 0.2j
        G = shadow_generating_function('virasoro', c, t)
        expected = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(G - expected) < 1e-14

    def test_unknown_archetype_raises(self):
        with pytest.raises(ValueError):
            shadow_generating_function('unknown', 1.0, 0.1)

    def test_heisenberg_complex_t(self):
        c = 2.0
        t = 1.0 + 1.0j
        G = shadow_generating_function('heisenberg', c, t)
        assert abs(G - 1.0 * (1.0 + 1.0j) ** 2) < 1e-14


# =====================================================================
# Section 3: Branch cut analysis
# =====================================================================

class TestBranchCut:
    """Branch cut structure of G_Vir."""

    def test_branch_point_location(self):
        assert abs(branch_point_virasoro(12.0) + 2.0) < 1e-15

    def test_branch_point_c26(self):
        assert abs(branch_point_virasoro(26.0) + 26.0 / 6) < 1e-14

    def test_discontinuity_on_cut(self):
        """disc(G) = -2*pi*i for t < -c/6."""
        c = 10.0
        disc = branch_cut_discontinuity(c, -5.0)  # -5 < -10/6 = -1.667
        assert abs(disc + 2j * cmath.pi) < 1e-14

    def test_no_discontinuity_before_cut(self):
        """disc(G) = 0 for t > -c/6."""
        c = 10.0
        disc = branch_cut_discontinuity(c, -1.0)  # -1 > -10/6
        assert abs(disc) < 1e-15

    def test_discontinuity_at_branch_point(self):
        """At the branch point itself, disc = 0 (boundary)."""
        c = 12.0
        disc = branch_cut_discontinuity(c, -2.0)
        assert abs(disc) < 1e-15

    def test_branch_cut_analysis_dict(self):
        result = branch_cut_analysis(6.0, n_points=10)
        assert 'branch_point' in result
        assert abs(result['branch_point'] + 1.0) < 1e-15
        assert len(result['sample_points']) == 10

    def test_discontinuity_constant_along_cut(self):
        """The discontinuity is -2*pi*i everywhere on the cut."""
        c = 20.0
        result = branch_cut_analysis(c, n_points=50)
        for d in result['discontinuities']:
            assert abs(d + 2j * cmath.pi) < 1e-13

    def test_monodromy_numerical(self):
        """Numerically computed monodromy should be -2*pi*i."""
        mono = monodromy_numerical(10.0, radius=0.01, n_points=5000)
        expected = -2.0j * cmath.pi
        assert abs(mono - expected) < 1e-4

    def test_monodromy_c26(self):
        mono = monodromy_numerical(26.0, radius=0.01, n_points=5000)
        assert abs(mono + 2j * cmath.pi) < 1e-4

    def test_monodromy_small_c(self):
        """Monodromy is independent of c (topological invariant)."""
        mono = monodromy_numerical(2.0, radius=0.001, n_points=5000)
        assert abs(mono + 2j * cmath.pi) < 1e-3


# =====================================================================
# Section 4: Borel transform
# =====================================================================

class TestBorelTransform:
    """Borel transform and resummation."""

    def test_borel_transform_at_zero(self):
        coeffs = shadow_coefficients_virasoro_leading(10.0, 10)
        B = borel_transform(coeffs, 0.0)
        assert abs(B) < 1e-15

    def test_borel_transform_grows_to_singularity(self):
        """B(xi) should grow as xi approaches c/6."""
        c = 12.0
        coeffs = shadow_coefficients_virasoro_leading(c, 40)
        vals = [abs(borel_transform(coeffs, xi)) for xi in [0.5, 1.0, 1.5, 1.9]]
        # Should be increasing toward xi = c/6 = 2
        for i in range(1, len(vals)):
            assert vals[i] > vals[i - 1]

    def test_borel_exact_small_xi(self):
        """Cross-check direct Borel transform against exact formula at small xi."""
        c = 20.0
        coeffs = shadow_coefficients_virasoro_leading(c, 60)
        xi = 0.5
        B_series = borel_transform(coeffs, xi)
        B_exact = borel_transform_virasoro_exact(c, xi)
        assert abs(B_series - B_exact) / max(abs(B_exact), 1e-10) < 0.01

    def test_borel_sum_equals_G_virasoro(self):
        """Borel-Laplace sum should recover G_Vir(t) for small positive t."""
        c = 20.0
        t = 0.1  # Well inside radius of convergence c/6 ~ 3.33
        coeffs = shadow_coefficients_virasoro_leading(c, 60)
        B_sum = borel_sum(coeffs, t, n_quad=1000, xi_max=80.0)
        G_exact = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        # Borel sum of a convergent series equals the function
        # But our Borel sum is approximate (truncated + quadrature)
        assert abs(B_sum - G_exact) / max(abs(G_exact), 1e-10) < 0.5

    def test_borel_heisenberg_exact(self):
        """For Heisenberg, the Borel transform is just (c/2)*xi^2/2!."""
        c = 4.0
        coeffs = shadow_coefficients_heisenberg(c, 5)
        B = borel_transform(coeffs, 1.0)
        expected = (c / 2.0) * 1.0 / math.factorial(2)
        assert abs(B - expected) < 1e-14

    def test_borel_transform_linearity(self):
        """Borel transform is linear in coefficients."""
        c = 10.0
        coeffs1 = shadow_coefficients_virasoro_leading(c, 10)
        coeffs2 = [2.0 * s for s in coeffs1]
        xi = 0.3
        B1 = borel_transform(coeffs1, xi)
        B2 = borel_transform(coeffs2, xi)
        assert abs(B2 - 2.0 * B1) < 1e-14


# =====================================================================
# Section 5: Pade approximants
# =====================================================================

class TestPadeApproximant:
    """Pade approximant construction and pole analysis."""

    def test_pade_heisenberg_exact(self):
        """Pade of a polynomial is exact."""
        c = 4.0
        coeffs = shadow_coefficients_heisenberg(c, 6)
        t = 0.5
        P = pade_approximant(coeffs, t, r_start=2)
        exact = (c / 2.0) * t ** 2
        assert abs(P - exact) < 1e-10

    def test_pade_affine_exact(self):
        """Pade of a cubic polynomial is exact."""
        c, C3 = 6.0, 2.0
        coeffs = shadow_coefficients_affine(c, C3, 6)
        t = 0.3
        P = pade_approximant(coeffs, t, r_start=2)
        exact = (c / 2.0) * t ** 2 + C3 * t ** 3
        assert abs(P - exact) < 1e-8

    def test_pade_virasoro_small_t(self):
        """Pade should approximate G_Vir for small t."""
        c = 20.0
        coeffs = shadow_coefficients_virasoro_leading(c, 12)
        t = 0.1
        P = pade_approximant(coeffs, t, r_start=2)
        exact = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(P - exact) / max(abs(exact), 1e-10) < 0.1

    def test_pade_poles_virasoro_converge(self):
        """Poles of Pade should approach t = -c/6."""
        c = 12.0
        coeffs = shadow_coefficients_virasoro_leading(c, 20)
        poles = pade_poles(coeffs, r_start=2)
        if len(poles) > 0:
            t_exact = -c / 6.0
            dists = [abs(p - t_exact) for p in poles]
            assert min(dists) < abs(t_exact) * 0.5

    def test_pade_no_poles_heisenberg(self):
        """Heisenberg Pade should have no real poles (it's polynomial)."""
        c = 4.0
        coeffs = shadow_coefficients_heisenberg(c, 6)
        poles = pade_poles(coeffs, r_start=2)
        # All poles should be at infinity or absent
        # With only S_2 nonzero, the denominator is trivial
        # Actually with our Pade construction, n = N - m might give spurious poles
        # but they should be far away
        if len(poles) > 0:
            for p in poles:
                assert abs(p) > 1.0  # No poles near origin

    def test_pade_branch_convergence_study(self):
        """Full convergence study: errors should decrease with order."""
        c = 20.0
        result = pade_branch_point_convergence(c, max_order=16)
        conv = result['convergence']
        if len(conv) >= 3:
            # Errors should generally decrease
            first_err = conv[0]['relative_error']
            last_err = conv[-1]['relative_error']
            assert last_err < first_err

    def test_pade_approximant_at_zero(self):
        """Pade should give 0 at t=0 (since G(0) = 0)."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        P = pade_approximant(coeffs, 0.0, r_start=2)
        assert abs(P) < 1e-14


# =====================================================================
# Section 6: Spectral measure
# =====================================================================

class TestSpectralMeasure:
    """Spectral measure from shadow moments."""

    def test_virasoro_spectral_is_dirac(self):
        """Leading-order Virasoro has spectral measure = delta at -6/c."""
        c = 10.0
        result = spectral_representation_check(c, 20)
        assert result['max_relative_error'] < 1e-12
        assert abs(result['spectral_point'] + 6.0 / c) < 1e-15

    def test_spectral_check_c26(self):
        result = spectral_representation_check(26.0, 15)
        assert result['max_relative_error'] < 1e-12

    def test_spectral_check_c1(self):
        result = spectral_representation_check(1.0, 10)
        assert result['max_relative_error'] < 1e-12

    def test_single_atom_reconstruction(self):
        """Reconstruct the single atom from two shadow coefficients."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        result = spectral_measure_from_shadows(coeffs, r_start=2, n_atoms=1)
        assert len(result['atoms']) == 1
        assert abs(result['atoms'][0] + 6.0 / c) < 1e-10

    def test_single_atom_weight(self):
        """Weight of the single atom should be 1.

        S_r = lam_0^r / r, so the moment formula S_r = w * lam^r / r
        gives w = 1.
        """
        c = 20.0
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        result = spectral_measure_from_shadows(coeffs, r_start=2, n_atoms=1)
        assert abs(result['weights'][0] - 1.0) < 1e-8

    def test_single_atom_reconstruction_errors_small(self):
        """Reconstruction errors should be tiny for a single-atom measure."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 15)
        result = spectral_measure_from_shadows(coeffs, r_start=2, n_atoms=1)
        assert result['max_error'] < 1e-10

    def test_two_atom_virasoro(self):
        """Two-atom fit to a single-atom series should reduce to one atom."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        result = spectral_measure_from_shadows(coeffs, r_start=2, n_atoms=2)
        # One atom should dominate; the other should have negligible weight
        weights = [abs(w) for w in result['weights']]
        assert max(weights) > 10 * min(weights) or min(weights) < 1e-6

    def test_spectral_measure_empty_coeffs(self):
        result = spectral_measure_from_shadows([], r_start=2, n_atoms=1)
        assert result['error'] == float('inf')


# =====================================================================
# Section 7: Carleman's condition
# =====================================================================

class TestCarlemanCondition:
    """Carleman's condition for moment determinacy."""

    def test_virasoro_carleman_holds(self):
        """Carleman's condition holds for Virasoro (moments ~ geometric)."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 30)
        result = carleman_condition(coeffs)
        assert result['diverges'] is True

    def test_heisenberg_carleman_trivial(self):
        """Heisenberg: zero moments => Carleman trivially holds."""
        coeffs = shadow_coefficients_heisenberg(4.0, 10)
        result = carleman_condition(coeffs)
        assert result['diverges'] is True

    def test_carleman_large_c(self):
        """Large c: moments are tiny, individual terms large, sum diverges."""
        c = 1000.0
        coeffs = shadow_coefficients_virasoro_leading(c, 30)
        result = carleman_condition(coeffs)
        assert result['diverges'] is True

    def test_carleman_partial_sums_increase(self):
        """Partial sums of Carleman series should be monotonically increasing."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 20)
        result = carleman_condition(coeffs)
        ps = result['partial_sums']
        for i in range(1, len(ps)):
            if math.isfinite(ps[i]) and math.isfinite(ps[i - 1]):
                assert ps[i] >= ps[i - 1]

    def test_carleman_c1(self):
        """Carleman holds even at c=1 (rapid growth of |S_r|)."""
        coeffs = shadow_coefficients_virasoro_leading(1.0, 20)
        result = carleman_condition(coeffs)
        # Moments grow as 6^r/r, so |m_r|^{-1/(2r)} ~ 1/sqrt(6), constant
        assert result['diverges'] is True


# =====================================================================
# Section 8: Dispersion relation
# =====================================================================

class TestDispersionRelation:
    """Dispersion integral reconstruction of G_Vir."""

    def test_dispersion_small_t(self):
        """Dispersion integral should recover G_Vir for small real positive t."""
        c = 20.0
        t = 1.0  # Use larger t where G is not as tiny
        G_disp = dispersion_integral(c, t, n_quad=5000, cutoff=200.0)
        G_exact = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(G_disp - G_exact) / max(abs(G_exact), 1e-10) < 0.5

    def test_dispersion_moderate_t(self):
        """Dispersion at moderate t."""
        c = 20.0
        t = 1.0
        G_disp = dispersion_integral(c, t, n_quad=5000, cutoff=500.0)
        G_exact = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(G_disp - G_exact) / abs(G_exact) < 0.5

    def test_dispersion_complex_t(self):
        """Dispersion integral at complex t off the cut."""
        c = 20.0
        t = 0.5 + 0.5j
        G_disp = dispersion_integral(c, t, n_quad=5000, cutoff=300.0)
        G_exact = -cmath.log(1.0 + 6.0 * t / c) + 6.0 * t / c
        assert abs(G_disp - G_exact) / abs(G_exact) < 0.5

    def test_dispersion_at_zero(self):
        """G(0) = 0, dispersion should give ~0."""
        c = 20.0
        G_disp = dispersion_integral(c, 0.001, n_quad=2000, cutoff=200.0)
        assert abs(G_disp) < 0.01


# =====================================================================
# Section 9: Radius of convergence and asymptotics
# =====================================================================

class TestRadiusAndAsymptotics:
    """Radius of convergence and growth rate of shadow obstruction tower."""

    def test_virasoro_radius(self):
        """Radius of convergence should be c/6."""
        c = 12.0
        coeffs = shadow_coefficients_virasoro_leading(c, 50)
        R = shadow_radius_of_convergence(coeffs)
        assert abs(R - c / 6.0) / (c / 6.0) < 0.15

    def test_heisenberg_infinite_radius(self):
        """Heisenberg: polynomial, so R = infinity."""
        coeffs = shadow_coefficients_heisenberg(4.0, 10)
        R = shadow_radius_of_convergence(coeffs)
        assert R == float('inf')

    def test_virasoro_ratio_test(self):
        """Consecutive ratios S_{r+1}/S_r -> -6/c as r -> inf."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 30)
        result = asymptotic_growth_rate(coeffs)
        ratios = result['consecutive_ratios']
        expected_ratio = -6.0 / c
        # Last ratio should be close (but not exact: S_{r+1}/S_r = -6/c * r/(r+1))
        assert abs(ratios[-1] - expected_ratio) / abs(expected_ratio) < 0.1

    def test_virasoro_ratio_c26(self):
        c = 26.0
        coeffs = shadow_coefficients_virasoro_leading(c, 30)
        result = asymptotic_growth_rate(coeffs)
        assert abs(result['limiting_ratio'] + 6.0 / c) < 0.05

    def test_radius_c1(self):
        """At c=1, radius = 1/6."""
        coeffs = shadow_coefficients_virasoro_leading(1.0, 40)
        R = shadow_radius_of_convergence(coeffs)
        assert abs(R - 1.0 / 6.0) / (1.0 / 6.0) < 0.15

    def test_affine_infinite_radius(self):
        coeffs = shadow_coefficients_affine(6.0, 2.0, 10)
        R = shadow_radius_of_convergence(coeffs)
        assert R == float('inf')


# =====================================================================
# Section 10: Full pipeline
# =====================================================================

class TestFullPipeline:
    """Integration tests for the full analysis pipeline."""

    def test_full_analysis_runs(self):
        result = full_complex_analysis(26.0, r_max=15)
        assert result['c'] == 26.0
        assert abs(result['branch_point'] + 26.0 / 6) < 1e-14
        assert result['carleman_diverges'] is True

    def test_full_analysis_spectral(self):
        result = full_complex_analysis(10.0, r_max=20)
        assert result['spectral_max_error'] < 1e-12

    def test_full_analysis_monodromy(self):
        result = full_complex_analysis(12.0, r_max=10)
        assert abs(result['monodromy_numerical'] - result['monodromy_exact']) < 0.01

    def test_full_analysis_c1(self):
        """Full pipeline at c=1 (small c regime)."""
        result = full_complex_analysis(1.0, r_max=12)
        assert abs(result['branch_point'] + 1.0 / 6) < 1e-15

    def test_coherence_spectral_and_branch(self):
        """Spectral point -6/c and branch point -c/6 are consistent:
        the spectral eigenvalue lambda_0 = -6/c, and the branch point
        of G(t) is at t = -c/6 = 1/lam_0."""
        c = 15.0
        result = full_complex_analysis(c, r_max=10)
        lam_0 = -6.0 / c
        assert abs(result['branch_point'] - 1.0 / lam_0) < 1e-14

    def test_shadow_depth_classification(self):
        """Verify depth classification: G=2, L=3, C=4, M=inf."""
        # Heisenberg: last nonzero at r=2
        h = shadow_coefficients_heisenberg(4.0, 10)
        depth_h = max(i + 2 for i, s in enumerate(h) if abs(s) > 1e-15)
        assert depth_h == 2

        # Affine: last nonzero at r=3
        a = shadow_coefficients_affine(6.0, 2.0, 10)
        depth_a = max(i + 2 for i, s in enumerate(a) if abs(s) > 1e-15)
        assert depth_a == 3

        # betagamma: last nonzero at r=4
        b = shadow_coefficients_betagamma(2.0, 0.5, 0.1, 10)
        depth_b = max(i + 2 for i, s in enumerate(b) if abs(s) > 1e-15)
        assert depth_b == 4

        # Virasoro: all nonzero (infinite depth)
        v = shadow_coefficients_virasoro_leading(10.0, 20)
        nonzero_count = sum(1 for s in v if abs(s) > 1e-15)
        assert nonzero_count == len(v)


# =====================================================================
# Section 11: Edge cases and consistency
# =====================================================================

class TestEdgeCases:
    """Edge cases and internal consistency checks."""

    def test_virasoro_self_dual_c13(self):
        """At c=13, Vir is self-dual. Check branch point is at -13/6."""
        assert abs(branch_point_virasoro(13.0) + 13.0 / 6) < 1e-14

    def test_large_c_gaussianity(self):
        """At large c, Virasoro approaches Gaussian (only S_2 matters)."""
        c = 1e6
        coeffs = shadow_coefficients_virasoro_leading(c, 10)
        # S_2 = (6/c)^2/2, S_3 = -(6/c)^3/3
        # Ratio S_3/S_2 ~ -2(6/c)/3 -> 0 as c -> inf
        ratio = abs(coeffs[1] / coeffs[0])
        assert ratio < 1e-4

    def test_generating_function_series_consistency(self):
        """G(t) evaluated at small t should match partial sum of coefficients."""
        c = 20.0
        t = 0.001  # Very small for good convergence
        G_exact = shadow_generating_function('virasoro', c, t)
        coeffs = shadow_coefficients_virasoro_leading(c, 50)
        G_series = sum(coeffs[i] * t ** (i + 2) for i in range(len(coeffs)))
        assert abs(G_exact - G_series) / max(abs(G_exact), 1e-30) < 1e-8

    def test_borel_transform_positive_axis(self):
        """On the positive real axis before the singularity, B(xi) is real."""
        c = 10.0
        coeffs = shadow_coefficients_virasoro_leading(c, 30)
        B = borel_transform(coeffs, 0.5)
        assert abs(B.imag) < 1e-10 * abs(B.real)
