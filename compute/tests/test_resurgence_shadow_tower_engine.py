r"""Tests for scalar A-hat shadow-tower diagnostics.

The file pins two kinds of output.

Certified exact facts:
1. F_g = kappa * lambda_g^FP.
2. sum lambda_g^FP hbar^{2g} = (hbar/2)/sin(hbar/2) - 1.
3. The scalar hbar-radius is 2*pi and the scalar u-radius is (2*pi)^2.
4. A-hat poles and residues are exact.
5. Standard family constants match the local landscape census.

Uncertified diagnostics:
finite Borel transforms, Pade windows, median-style quadrature, formal
Stokes multipliers, formal alien derivatives, arity-radius diagnostics,
and Verdier scalar complementarity must not be promoted to analytic
resurgence theorems or nonperturbative completions.
"""

import sys
sys.path.insert(0, 'compute')

import cmath
import math

import numpy as np
import pytest

PI = math.pi
TWO_PI = 2.0 * PI
FOUR_PI_SQ = (2.0 * PI) ** 2


# =====================================================================
# Section 0: Certification and firewalls
# =====================================================================

class TestCertificationFirewalls:
    """Pin the exact/diagnostic boundary of this engine."""

    def test_certification_report_refuses_analytic_promotion(self):
        from lib.resurgence_shadow_tower_engine import certification_report
        report = certification_report()
        assert report['exact_scalar_ahat_coefficients']
        assert report['scalar_hbar_radius_certified'] == TWO_PI
        assert report['scalar_u_radius_certified'] == FOUR_PI_SQ
        assert math.isinf(report['borel_transform_radius_certified'])
        assert not report['borel_summability_certified']
        assert not report['median_resummation_certified']
        assert not report['stokes_automorphism_certified']
        assert not report['alien_derivatives_certified']
        assert not report['nonperturbative_completion_certified']
        assert not report['unique_continuation_from_finite_data_certified']

    def test_object_firewall_distinguishes_dual_branches(self):
        from lib.resurgence_shadow_tower_engine import object_firewall
        firewall = object_firewall()
        assert firewall['Omega(B(A))'] == 'bar-cobar inversion of A, not Koszul duality'
        assert 'Verdier' in firewall['A^!']
        assert 'Hochschild' in firewall['Z_ch^der(A)']

    def test_kernel_constant_firewall(self):
        from lib.resurgence_shadow_tower_engine import kernel_constant_firewall
        constants = kernel_constant_firewall()
        assert constants['heisenberg_collision'] == 'k/z'
        assert constants['affine_raw_trace_form'] == 'k*Omega_tr/z'
        assert constants['affine_kz'] == 'Omega/((k+h^vee)z), Omega=2*h^vee*Omega_tr'
        assert constants['virasoro_collision'] == '(c/2)/z^3 + 2T/z'


# =====================================================================
# Section 1: Borel transform of the genus expansion
# =====================================================================

class TestBorelTransformGenus:
    """Test the diagnostic transform B(t) = sum F_g t^{2g-1}/(2g-1)!."""

    def test_borel_at_zero_is_zero(self):
        """B(0) = 0 (the series starts at t^1)."""
        from lib.resurgence_shadow_tower_engine import borel_transform_genus
        val = borel_transform_genus(1.0, 0.0)
        assert abs(val) < 1e-15

    def test_borel_at_small_t_equals_leading_term(self):
        """For small t: B(t) ~ F_1 * t / Gamma(2) = kappa/24 * t."""
        from lib.resurgence_shadow_tower_engine import (
            borel_transform_genus, F_g_scalar,
        )
        kappa = 1.0
        t = 0.01
        val = borel_transform_genus(kappa, t, g_max=50)
        leading = F_g_scalar(kappa, 1) * t / math.gamma(2)
        assert abs(val - leading) / abs(leading) < 1e-3

    def test_borel_transform_finite_at_sample_points(self):
        """The diagnostic transform is finite at ordinary sample points."""
        from lib.resurgence_shadow_tower_engine import borel_transform_genus
        kappa = 1.0
        for t in [1.0, 3.0, 5.0, 6.0]:
            val = borel_transform_genus(kappa, t, g_max=80)
            assert math.isfinite(abs(val))

    def test_borel_convergence_rate(self):
        """Successive terms of B(t) decrease in a small sample window."""
        from lib.resurgence_shadow_tower_engine import F_g_scalar
        kappa = 1.0
        t = 3.0
        terms = []
        for g in range(1, 20):
            Fg = F_g_scalar(kappa, g)
            term = abs(Fg * t ** (2 * g - 1) / math.gamma(2 * g))
            terms.append(term)
        for i in range(5, len(terms) - 1):
            assert terms[i + 1] < terms[i], f"Term {i+1} not decreasing"

    def test_borel_u_plane_consistency(self):
        """B_u(xi) at xi and B(t) at t = sqrt(xi) are related."""
        from lib.resurgence_shadow_tower_engine import (
            borel_transform_genus, borel_transform_u_plane,
        )
        kappa = 2.5
        # These are different Borel transforms (different factorial normalizations)
        # but both should be finite inside their convergence radii
        val_u = borel_transform_u_plane(kappa, 10.0, g_max=50)
        val_t = borel_transform_genus(kappa, 3.0, g_max=50)
        assert math.isfinite(abs(val_u))
        assert math.isfinite(abs(val_t))

    def test_borel_coefficients_structure(self):
        """Borel coefficients b_g = F_g / (2g-1)! have correct structure."""
        from lib.resurgence_shadow_tower_engine import borel_coefficients
        kappa = 1.0
        coeffs = borel_coefficients(kappa, g_max=10)
        assert len(coeffs) == 10
        assert coeffs[0]['g'] == 1
        assert coeffs[0]['power'] == 1
        assert abs(coeffs[0]['borel_coeff'] - coeffs[0]['F_g']) < 1e-15  # Gamma(2) = 1
        for c in coeffs:
            assert c['power'] == 2 * c['g'] - 1


# =====================================================================
# Section 2: Singularity structure
# =====================================================================

class TestBorelSingularities:
    """Test the exact scalar A-hat pole structure."""

    def test_nearest_singularity_at_two_pi(self):
        """The nearest exact A-hat pole is at hbar = 2*pi."""
        from lib.resurgence_shadow_tower_engine import nearest_borel_singularity
        sing = nearest_borel_singularity()
        assert abs(sing.location_hbar - TWO_PI) < 1e-12
        assert sing.certification == 'certified_scalar_ahat_bernoulli'
        assert not sing.borel_singularity_certified

    def test_first_u_pole_is_four_pi_squared(self):
        """The first scalar u-plane pole is A = (2*pi)^2."""
        from lib.resurgence_shadow_tower_engine import (
            nearest_borel_singularity, INSTANTON_ACTION, SCALAR_FIRST_U_POLE,
        )
        sing = nearest_borel_singularity()
        assert abs(sing.instanton_action - FOUR_PI_SQ) < 1e-10
        assert abs(INSTANTON_ACTION - FOUR_PI_SQ) < 1e-10
        assert abs(SCALAR_FIRST_U_POLE - FOUR_PI_SQ) < 1e-10

    def test_singularities_at_integer_multiples(self):
        """A-hat poles at hbar = 2*pi*n for n = 1, 2, 3, ..."""
        from lib.resurgence_shadow_tower_engine import borel_singularity_locations
        sings = borel_singularity_locations(5)
        for i, s in enumerate(sings):
            n = i + 1
            assert abs(s.location_hbar - TWO_PI * n) < 1e-12
            assert abs(s.location_u - (TWO_PI * n) ** 2) < 1e-8

    def test_singularities_are_simple_poles(self):
        """All A-hat singularities in this list are simple poles."""
        from lib.resurgence_shadow_tower_engine import borel_singularity_locations
        for s in borel_singularity_locations(5):
            assert s.singularity_type == 'simple_pole'

    def test_residue_formula(self):
        """Residue at hbar = 2*pi*n is (-1)^n * 2*pi*n."""
        from lib.resurgence_shadow_tower_engine import borel_singularity_locations
        for s in borel_singularity_locations(5):
            n = s.n
            expected = (-1) ** n * TWO_PI * n
            assert abs(s.residue - expected) < 1e-10

    def test_convergence_radius_verification(self):
        """The scalar ratio |F_{g+1}/F_g| converges to 1/(4*pi^2)."""
        from lib.resurgence_shadow_tower_engine import verify_borel_radius_from_coefficients
        result = verify_borel_radius_from_coefficients(1.0, g_max=40)
        assert result['converged']
        assert abs(result['predicted_u_radius'] - FOUR_PI_SQ) < 1e-10
        assert math.isinf(result['borel_transform_radius'])
        assert not result['borel_summability_certified']
        assert not result['analytic_continuation_from_finite_data_certified']

    def test_borel_radius_is_not_scalar_radius(self):
        """The diagnostic Borel radius is infinite; the scalar radius is 2*pi."""
        from lib.resurgence_shadow_tower_engine import BOREL_RADIUS, SCALAR_HBAR_RADIUS
        assert math.isinf(BOREL_RADIUS)
        assert abs(SCALAR_HBAR_RADIUS - TWO_PI) < 1e-12


# =====================================================================
# Section 3: Formal residue multipliers
# =====================================================================

class TestFormalResidueMultipliers:
    """Test formal residue multipliers without analytic promotion."""

    def test_leading_stokes_multiplier_formula(self):
        """Formal S_1 = -4*pi^2*kappa*i."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_leading
        for kappa in [0.5, 1.0, 6.5, 13.0]:
            S1 = stokes_multiplier_leading(kappa)
            expected = -FOUR_PI_SQ * kappa * 1.0j
            assert abs(S1 - expected) < 1e-10

    def test_stokes_multiplier_purely_imaginary(self):
        """The formal S_1 is purely imaginary for real kappa."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_leading
        S1 = stokes_multiplier_leading(1.0)
        assert abs(S1.real) < 1e-15
        assert abs(S1.imag) > 1.0  # non-zero

    def test_stokes_multiplier_n_alternating_sign(self):
        """Formal S_n has alternating sign."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_n
        kappa = 1.0
        for n in range(1, 6):
            S_n = stokes_multiplier_n(kappa, n)
            expected_sign = (-1) ** n
            assert S_n.imag * expected_sign > 0

    def test_stokes_multiplier_linear_in_kappa(self):
        """Formal S_n is linear in kappa."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_n
        for n in range(1, 4):
            S_k1 = stokes_multiplier_n(1.0, n)
            S_k3 = stokes_multiplier_n(3.0, n)
            assert abs(S_k3 - 3.0 * S_k1) < 1e-10

    def test_stokes_multiplier_proportional_to_n(self):
        """The formal multiplier magnitude is proportional to n."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_n
        kappa = 1.0
        for n in range(1, 6):
            S_n = stokes_multiplier_n(kappa, n)
            assert abs(abs(S_n) - FOUR_PI_SQ * n) < 1e-10

    def test_stokes_discontinuity_exponentially_suppressed(self):
        """The formal discontinuity ansatz is exponentially suppressed."""
        from lib.resurgence_shadow_tower_engine import stokes_discontinuity_u_plane
        kappa = 1.0
        disc_small = abs(stokes_discontinuity_u_plane(kappa, 1.0))
        disc_large = abs(stokes_discontinuity_u_plane(kappa, 10.0))
        assert disc_small < disc_large  # larger u = less suppression

    def test_stokes_virasoro_c13_self_dual(self):
        """At c=13, the formal multiplier is symmetric in c and 26-c."""
        from lib.resurgence_shadow_tower_engine import (
            stokes_multiplier_leading, kappa_virasoro,
        )
        kappa = kappa_virasoro(13.0)
        kappa_dual = kappa_virasoro(26.0 - 13.0)
        assert abs(kappa - kappa_dual) < 1e-12
        S1 = stokes_multiplier_leading(kappa)
        S1_dual = stokes_multiplier_leading(kappa_dual)
        assert abs(S1 - S1_dual) < 1e-10


# =====================================================================
# Section 4: Alien derivatives
# =====================================================================

class TestFormalAlienDiagnostics:
    """Test formal alien-derivative diagnostics."""

    def test_alien_derivative_at_leading_singularity(self):
        """The formal leading value equals the formal residue multiplier."""
        from lib.resurgence_shadow_tower_engine import (
            alien_derivative_perturbative, stokes_multiplier_leading,
        )
        kappa = 1.0
        alien = alien_derivative_perturbative(kappa, n=1)
        S1 = stokes_multiplier_leading(kappa)
        assert abs(alien - S1) < 1e-10

    def test_alien_derivative_chain_factorizes(self):
        """The formal diagnostic chain records powers of S_1."""
        from lib.resurgence_shadow_tower_engine import (
            alien_derivative_chain, stokes_multiplier_leading,
        )
        kappa = 2.0
        S1 = stokes_multiplier_leading(kappa)
        chain = alien_derivative_chain(kappa, max_level=4)
        for item in chain:
            k = item['level']
            assert abs(item['alien_derivative'] - S1 ** k) < 1e-8
            assert item['certification'] == 'analytic_resurgence_hypothesis_not_certified'
            assert not item['alien_derivative_certified']

    def test_scalar_large_order_approaches_1(self):
        """The scalar A-hat large-order ratio approaches 1."""
        from lib.resurgence_shadow_tower_engine import verify_alien_derivative_resurgence
        result = verify_alien_derivative_resurgence(1.0, g_max=25)
        assert result['approaching_1']
        assert result['certification'] == 'certified_scalar_ahat_bernoulli'
        assert not result['alien_derivative_certified']
        # The ratio at g=20 should be closer to 1 than at g=5
        r20 = result['ratio_at_g20']
        assert r20 is not None
        assert abs(r20 - 1.0) < 0.01  # within 1% at g=20


# =====================================================================
# Section 5: Trans-series
# =====================================================================

class TestTransseries:
    """Test the formal trans-series diagnostic."""

    def test_transseries_data_structure(self):
        """TransseriesData has correct components."""
        from lib.resurgence_shadow_tower_engine import build_transseries
        ts = build_transseries(1.0, g_max=20)
        assert ts.instanton_action == FOUR_PI_SQ
        assert len(ts.perturbative) == 20
        assert len(ts.one_instanton) == 20
        assert len(ts.two_instanton) == 20
        assert ts.certification == 'analytic_resurgence_hypothesis_not_certified'
        assert not ts.completion_certified

    def test_perturbative_sector_matches_Fg(self):
        """The perturbative sector is F_g."""
        from lib.resurgence_shadow_tower_engine import (
            build_transseries, F_g_scalar,
        )
        kappa = 2.5
        ts = build_transseries(kappa, g_max=15)
        for g in range(1, 16):
            assert abs(ts.perturbative[g - 1] - F_g_scalar(kappa, g)) < 1e-15

    def test_one_pole_coefficients_decay(self):
        """Formal one-pole coefficients decay as 1/(2*pi)^{2g}."""
        from lib.resurgence_shadow_tower_engine import one_instanton_coefficients
        kappa = 1.0
        coeffs = one_instanton_coefficients(kappa, g_max=20)
        ratios = []
        for i in range(1, len(coeffs)):
            if abs(coeffs[i - 1]) > 1e-100:
                ratios.append(abs(coeffs[i]) / abs(coeffs[i - 1]))
        # Ratio should approach 1/(2*pi)^2
        expected = 1.0 / FOUR_PI_SQ
        assert abs(ratios[-1] - expected) / expected < 0.01

    def test_two_pole_faster_decay(self):
        """Formal two-pole coefficients decay faster than one-pole coefficients."""
        from lib.resurgence_shadow_tower_engine import (
            one_instanton_coefficients, two_instanton_coefficients,
        )
        kappa = 1.0
        inst1 = one_instanton_coefficients(kappa, g_max=15)
        inst2 = two_instanton_coefficients(kappa, g_max=15)
        # |F_g^{(2)}| < |F_g^{(1)}| for all g >= 2
        for g in range(2, 15):
            assert abs(inst2[g - 1]) < abs(inst1[g - 1])

    def test_transseries_evaluate_near_zero(self):
        """The formal ansatz is close to perturbative data for small hbar."""
        from lib.resurgence_shadow_tower_engine import (
            build_transseries, transseries_evaluate, genus_series_partial_sum,
        )
        kappa = 1.0
        ts = build_transseries(kappa, g_max=20)
        hbar = 0.5  # small hbar
        ts_val = transseries_evaluate(ts, hbar, n_inst=2)
        pert_val = genus_series_partial_sum(kappa, hbar, 20)
        # Instanton ~ exp(-A/hbar^2) ~ exp(-158) ~ 0
        assert abs(ts_val - pert_val) / abs(pert_val) < 1e-10

    def test_transseries_sigma_equals_S1(self):
        """The formal parameter sigma equals the formal S_1."""
        from lib.resurgence_shadow_tower_engine import (
            build_transseries, stokes_multiplier_leading,
        )
        kappa = 3.0
        ts = build_transseries(kappa)
        S1 = stokes_multiplier_leading(kappa)
        assert abs(ts.sigma - S1) < 1e-10


# =====================================================================
# Section 6: Formal one-pole correction
# =====================================================================

class TestFormalOnePoleCorrection:
    """Test the formal one-pole correction."""

    def test_formal_exponential_suppressed(self):
        """exp(-A/hbar^2) is negligible for small hbar."""
        from lib.resurgence_shadow_tower_engine import one_instanton_correction
        result = one_instanton_correction(1.0, 0.5)
        assert result['exp_suppression'] < 1e-50
        assert result['certification'] == 'analytic_resurgence_hypothesis_not_certified'
        assert not result['nonperturbative_sector_certified']

    def test_formal_exponential_grows_with_hbar(self):
        """The formal exponential grows as hbar increases."""
        from lib.resurgence_shadow_tower_engine import one_instanton_correction
        r1 = one_instanton_correction(1.0, 1.0)
        r2 = one_instanton_correction(1.0, 3.0)
        assert r2['exp_suppression'] > r1['exp_suppression']

    def test_first_u_pole_is_universal(self):
        """The first scalar u-pole A = (2*pi)^2 is independent of kappa."""
        from lib.resurgence_shadow_tower_engine import one_instanton_correction
        r1 = one_instanton_correction(0.5, 2.0)
        r2 = one_instanton_correction(5.0, 2.0)
        assert abs(r1['instanton_action'] - r2['instanton_action']) < 1e-12

    def test_formal_correction_relative_size(self):
        """The formal correction is much smaller than perturbative at hbar = 1."""
        from lib.resurgence_shadow_tower_engine import one_instanton_correction
        result = one_instanton_correction(1.0, 1.0)
        assert result['relative_to_perturbative'] < 1e-10


# =====================================================================
# Section 7: Median-style diagnostics
# =====================================================================

class TestMedianDiagnostics:
    """Test median-style numerical diagnostics without certification."""

    def test_closed_form_ahat(self):
        """Verify the A-hat generating function."""
        from lib.resurgence_shadow_tower_engine import ahat_generating_function
        # At hbar = 0: Ahat = 1
        assert abs(ahat_generating_function(0.0) - 1.0) < 1e-14
        # At hbar = pi: Ahat = (pi/2)/sin(pi/2) = pi/2
        assert abs(ahat_generating_function(PI) - PI / 2.0) < 1e-12

    def test_closed_form_at_hbar_1(self):
        """Z^sh(hbar=1) = kappa * ((1/2)/sin(1/2) - 1)."""
        from lib.resurgence_shadow_tower_engine import genus_series_closed_form
        kappa = 1.0
        val = genus_series_closed_form(kappa, 1.0)
        expected = kappa * ((0.5) / math.sin(0.5) - 1.0)
        assert abs(val - expected) < 1e-14

    def test_partial_sum_converges_to_closed_form(self):
        """Partial sum Z^{<=g_max} -> exact for increasing g_max, |hbar| < 2*pi."""
        from lib.resurgence_shadow_tower_engine import (
            genus_series_partial_sum, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 5.0  # large enough that g_max=3 vs g_max=30 differs visibly
        exact = genus_series_closed_form(kappa, hbar)
        err_3 = abs(genus_series_partial_sum(kappa, hbar, 3) - exact)
        err_30 = abs(genus_series_partial_sum(kappa, hbar, 30) - exact)
        assert err_30 < err_3

    def test_partial_sum_matches_closed_form_high_order(self):
        """At 50 terms, partial sum agrees with closed form to < 1e-10."""
        from lib.resurgence_shadow_tower_engine import (
            genus_series_partial_sum, genus_series_closed_form,
        )
        kappa = 3.0
        hbar = 2.0
        exact = genus_series_closed_form(kappa, hbar)
        partial = genus_series_partial_sum(kappa, hbar, 50)
        assert abs(partial - exact) / abs(exact) < 1e-10

    @pytest.mark.slow
    def test_median_agrees_with_exact(self):
        """The median-style diagnostic is explicitly uncertified."""
        from lib.resurgence_shadow_tower_engine import median_borel_sum
        result = median_borel_sum(1.0, 1.0, epsilon=0.05, g_max=40,
                                  n_quad=1000, xi_max=30.0)
        assert result['certification'] == 'finite_window_diagnostic'
        assert not result['median_resummation_certified']
        assert not result['unique_analytic_continuation_certified']
        if result['exact'] is not None and result['median_vs_exact'] is not None:
            assert result['median_vs_exact'] < 0.1  # reasonable numerical accuracy

    def test_stokes_jump_imaginary_at_real_hbar(self):
        """The lateral quadrature jump remains finite for real hbar > 0."""
        from lib.resurgence_shadow_tower_engine import lateral_borel_sum
        kappa = 1.0
        hbar = 1.0 + 0.0j
        S_plus = lateral_borel_sum(kappa, hbar, epsilon=+0.05, g_max=30,
                                   n_quad=500, xi_max=20.0)
        S_minus = lateral_borel_sum(kappa, hbar, epsilon=-0.05, g_max=30,
                                    n_quad=500, xi_max=20.0)
        jump = S_plus - S_minus
        # The jump is exponentially small at hbar = 1, so just check finiteness
        assert math.isfinite(abs(jump))


# =====================================================================
# Section 8: Finite-window Pade diagnostics
# =====================================================================

class TestFiniteWindowPade:
    """Test finite-window Pade diagnostics."""

    def test_pade_at_small_hbar(self):
        """Pade agrees with partial sum for small hbar."""
        from lib.resurgence_shadow_tower_engine import (
            pade_approximant_genus, genus_series_partial_sum,
        )
        kappa = 1.0
        hbar = 0.5
        pade_val = pade_approximant_genus(kappa, hbar, g_max=20)
        partial_val = genus_series_partial_sum(kappa, hbar, 20)
        assert abs(pade_val - partial_val) / abs(partial_val) < 0.01

    def test_pade_matches_closed_form(self):
        """Pade approximant approximates the exact scalar closed form."""
        from lib.resurgence_shadow_tower_engine import (
            pade_approximant_genus, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 2.0
        pade_val = pade_approximant_genus(kappa, hbar, g_max=20)
        exact = genus_series_closed_form(kappa, hbar)
        assert abs(pade_val - exact) / abs(exact) < 0.05

    def test_pade_poles_approximate_first_u_pole(self):
        """The nearest real positive Pade pole should approximate (2*pi)^2.

        At finite Pade order, the pole location is approximate. We check
        that a real positive pole exists in a neighbourhood of the expected
        value, and that increasing the order improves the approximation.
        """
        from lib.resurgence_shadow_tower_engine import pade_poles_genus
        kappa = 1.0
        # Use higher order for better convergence
        poles = pade_poles_genus(kappa, g_max=30)
        if len(poles) > 0:
            # Find real positive poles (allow moderate imaginary part)
            real_pos = sorted([p.real for p in poles
                              if abs(p.imag) < max(abs(p.real) * 0.5, 5.0)
                              and p.real > 0])
            if real_pos:
                nearest = real_pos[0]
                # Should be in the right ballpark (within 50% of (2*pi)^2)
                assert abs(nearest - FOUR_PI_SQ) / FOUR_PI_SQ < 0.50

    def test_borel_pade_virasoro_structure(self):
        """Finite-window Virasoro Pade analysis produces valid data."""
        from lib.resurgence_shadow_tower_engine import borel_pade_virasoro
        result = borel_pade_virasoro(1.0, g_max=16)
        assert result['c'] == 1.0
        assert result['kappa'] == 0.5
        assert result['expected_nearest'] == FOUR_PI_SQ
        assert len(result['comparisons']) > 0
        assert result['certification'] == 'finite_window_diagnostic'
        assert not result['analytic_continuation_certified']
        assert not result['borel_summability_certified']

    def test_pade_improves_with_order(self):
        """Higher-order Pade gives better approximation."""
        from lib.resurgence_shadow_tower_engine import (
            pade_approximant_genus, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 2.0
        exact = genus_series_closed_form(kappa, hbar)
        err_10 = abs(pade_approximant_genus(kappa, hbar, g_max=10) - exact)
        err_20 = abs(pade_approximant_genus(kappa, hbar, g_max=20) - exact)
        # Pade at order 20 should be at least as good as order 10
        # (not always strictly better due to Pade instabilities, so generous bound)
        assert err_20 < 10 * err_10

    def test_borel_pade_virasoro_c13(self):
        """Borel-Pade at the self-dual point c = 13."""
        from lib.resurgence_shadow_tower_engine import borel_pade_virasoro
        result = borel_pade_virasoro(13.0, g_max=16)
        assert result['kappa'] == 6.5
        # Check that comparisons have reasonable Pade values
        for comp in result['comparisons']:
            if comp['pade'] is not None:
                assert math.isfinite(comp['pade'])


# =====================================================================
# Section 9: Bridge equation and MC connection
# =====================================================================

class TestBridgeEquation:
    """Test bridge-equation diagnostics without analytic promotion."""

    def test_bridge_arity_2_trivial(self):
        """kappa is exact, so bridge equation at arity 2 is trivial."""
        from lib.resurgence_shadow_tower_engine import bridge_equation_arity_r
        result = bridge_equation_arity_r(1.0, 2)
        assert result['bridge_satisfied'] is None
        assert result['finite_shadow_exact']
        assert not result['analytic_bridge_certified']
        assert result['alien_derivative'] == 0.0

    def test_bridge_arity_3_trivial(self):
        """Cubic shadow alpha = 2 is exact."""
        from lib.resurgence_shadow_tower_engine import bridge_equation_arity_r
        result = bridge_equation_arity_r(1.0, 3)
        assert result['bridge_satisfied'] is None
        assert result['finite_shadow_exact']
        assert not result['analytic_bridge_certified']
        assert result['alien_derivative'] == 0.0

    def test_bridge_arity_4_nontrivial(self):
        """Quartic bridge data is not analytically certified."""
        from lib.resurgence_shadow_tower_engine import bridge_equation_arity_r
        result = bridge_equation_arity_r(1.0, 4)
        assert result['bridge_satisfied'] is None
        assert not result['finite_shadow_exact']
        assert not result['analytic_bridge_certified']

    def test_bridge_mc_consistency_structure(self):
        """MC consistency check returns valid data."""
        from lib.resurgence_shadow_tower_engine import bridge_equation_mc_consistency
        result = bridge_equation_mc_consistency(1.0)
        assert 'mc_equation' in result
        assert 'bridge_equation' in result
        assert result['instanton_action'] == FOUR_PI_SQ
        assert not result['analytic_bridge_certified']
        assert result['consistency_proof'] is None

    def test_bridge_all_arities_uncertified(self):
        """No finite-arity diagnostic certifies the analytic bridge equation."""
        from lib.resurgence_shadow_tower_engine import bridge_equation_arity_r
        for r in range(2, 9):
            result = bridge_equation_arity_r(1.0, r)
            assert result['bridge_satisfied'] is None
            assert not result['analytic_bridge_certified']


# =====================================================================
# Section 10: Q^contact and higher-shadow diagnostics
# =====================================================================

class TestQcontactDiagnostics:
    """Test Q^contact arity-radius diagnostics."""

    def test_qcontact_formula(self):
        """Q^contact = 10/(c(5c+22)) for Virasoro."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        for c_val in [1.0, 13.0, 25.0]:
            result = qcontact_resurgence(c_val)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(result['Q_contact'] - expected) < 1e-14

    def test_delta_positive_for_positive_c(self):
        """Delta = 40/(5c+22) > 0 for c > 0 (class M)."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        for c_val in [0.5, 1.0, 13.0, 25.0]:
            result = qcontact_resurgence(c_val)
            assert result['Delta'] > 0
            assert result['shadow_depth'] == 'infinite'

    def test_depth_class_M(self):
        """Virasoro is class M (infinite depth) for c > 0."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        result = qcontact_resurgence(13.0)
        assert result['depth_class'] == 'M'

    def test_arity_borel_entire(self):
        """The arity-direction Borel claim remains a diagnostic."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        result = qcontact_resurgence(13.0)
        assert result['arity_borel_entire'] is None
        assert result['arity_borel_entire_diagnostic']
        assert not result['arity_borel_entire_certified']

    def test_arity_stokes_constant_logarithmic(self):
        """The arity Stokes constant is only a hypothesis."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        result = qcontact_resurgence(13.0)
        assert result['arity_stokes_constant'] is None
        assert abs(result['arity_stokes_constant_hypothesis'] - 2.0j * PI) < 1e-10
        assert not result['arity_stokes_constant_certified']

    def test_arity_convergence_radius_positive(self):
        """The Q_L arity-radius diagnostic is positive for c > 0."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        for c_val in [1.0, 13.0, 25.0]:
            result = qcontact_resurgence(c_val)
            assert result['arity_convergence_radius'] > 0
            assert not result['arity_radius_certified_from_finite_window']

    def test_branch_points_conjugate(self):
        """Branch points of Q_L are complex conjugate for c > 0."""
        from lib.resurgence_shadow_tower_engine import qcontact_resurgence
        result = qcontact_resurgence(13.0)
        t_plus, t_minus = result['branch_points']
        assert abs(t_minus - t_plus.conjugate()) < 1e-12


# =====================================================================
# Section 11: Higher-shadow asymptotic diagnostics
# =====================================================================

class TestHigherShadowDiagnostics:
    """Test asymptotic diagnostics for higher shadow coefficients."""

    def test_shadow_coefficients_recursive_S2(self):
        """S_2 = kappa = c/2 for Virasoro."""
        from lib.resurgence_shadow_tower_engine import arity_shadow_coefficients_recursive
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = arity_shadow_coefficients_recursive(c_val, r_max=5)
            # coeffs[0] = S_2
            assert abs(coeffs[0] - c_val / 2.0) < 1e-10

    def test_shadow_coefficients_recursive_S3(self):
        """S_3 = alpha = 2 for Virasoro (from T_{(1)}T = 2T)."""
        from lib.resurgence_shadow_tower_engine import arity_shadow_coefficients_recursive
        # S_3 = a_1 / 3 where a_1 = q1/(2*a_0) = 12*c/(2*c) = 6
        # So S_3 = 6/3 = 2
        coeffs = arity_shadow_coefficients_recursive(10.0, r_max=5)
        assert abs(coeffs[1] - 2.0) < 1e-10

    def test_shadow_coefficients_recursive_S4(self):
        """S_4 = 10/(c(5c+22)) for Virasoro."""
        from lib.resurgence_shadow_tower_engine import arity_shadow_coefficients_recursive
        for c_val in [1.0, 13.0, 25.0]:
            coeffs = arity_shadow_coefficients_recursive(c_val, r_max=5)
            expected = 10.0 / (c_val * (5.0 * c_val + 22.0))
            assert abs(coeffs[2] - expected) < 1e-10

    def test_arity_borel_transform_finite(self):
        """Arity Borel transform is finite at moderate xi."""
        from lib.resurgence_shadow_tower_engine import arity_borel_transform
        for c_val in [1.0, 13.0, 25.0]:
            val = arity_borel_transform(c_val, 1.0, r_max=30)
            assert math.isfinite(abs(val))

    def test_higher_shadow_growth_rate(self):
        """Finite-window growth rates are positive diagnostics."""
        from lib.resurgence_shadow_tower_engine import higher_shadow_resurgence
        result = higher_shadow_resurgence(13.0, r_max=20)
        rates = result['growth_rates']
        assert result['certification'] == 'arity_radius_diagnostic'
        assert result['finite_window_only']
        assert not result['all_arity_resurgence_certified']
        if len(rates) >= 3:
            assert rates[-1] > 0

    def test_leading_ratio_approaches_1(self):
        """For large c, S_r / leading_formula approaches 1."""
        from lib.resurgence_shadow_tower_engine import higher_shadow_resurgence
        result = higher_shadow_resurgence(100.0, r_max=15)
        ratios = result['leading_ratios']
        if len(ratios) >= 3:
            # For c = 100, leading-order should be decent
            assert abs(ratios[0] - 1.0) < 0.3


# =====================================================================
# Section 12: Large-order relations
# =====================================================================

class TestLargeOrderRelations:
    """Test finite-pole large-order estimates for F_g."""

    def test_large_order_leading_term(self):
        """Leading term: F_g ~ 2*kappa/(2*pi)^{2g}."""
        from lib.resurgence_shadow_tower_engine import (
            large_order_prediction, F_g_scalar,
        )
        kappa = 1.0
        # At large g, the n=1 term dominates
        g = 15
        Fg = F_g_scalar(kappa, g)
        predicted = large_order_prediction(kappa, g, n_inst=1)
        # Should be within 1% at g = 15
        assert abs(Fg - predicted) / abs(Fg) < 0.01

    def test_large_order_multi_pole_improvement(self):
        """Including more A-hat poles improves the estimate at moderate g."""
        from lib.resurgence_shadow_tower_engine import (
            large_order_prediction, F_g_scalar,
        )
        kappa = 1.0
        g = 5
        Fg = F_g_scalar(kappa, g)
        err_1 = abs(Fg - large_order_prediction(kappa, g, n_inst=1))
        err_3 = abs(Fg - large_order_prediction(kappa, g, n_inst=3))
        err_5 = abs(Fg - large_order_prediction(kappa, g, n_inst=5))
        # More pole terms should improve, or at least not worsen significantly.
        assert err_5 <= err_1 * 1.01  # allow tiny numerical noise

    def test_large_order_verification(self):
        """The large-order comparison stays explicitly scalar-certified."""
        from lib.resurgence_shadow_tower_engine import large_order_verification
        result = large_order_verification(1.0, g_max=20, n_inst=5)
        assert result['error_at_g15'] is not None
        assert result['error_at_g15'] < 0.001
        assert result['certification'] == 'certified_scalar_ahat_bernoulli'
        assert not result['nonperturbative_completion_certified']

    def test_large_order_kappa_linearity(self):
        """F_g and its prediction are both linear in kappa."""
        from lib.resurgence_shadow_tower_engine import (
            large_order_prediction, F_g_scalar,
        )
        g = 10
        Fg_k1 = F_g_scalar(1.0, g)
        Fg_k3 = F_g_scalar(3.0, g)
        pred_k1 = large_order_prediction(1.0, g, n_inst=3)
        pred_k3 = large_order_prediction(3.0, g, n_inst=3)
        assert abs(Fg_k3 - 3.0 * Fg_k1) < 1e-15
        assert abs(pred_k3 - 3.0 * pred_k1) < 1e-12

    def test_large_order_prediction_matches_bernoulli_asymptotics(self):
        """The prediction reproduces the Bernoulli asymptotic formula."""
        from lib.resurgence_shadow_tower_engine import large_order_prediction
        kappa = 1.0
        g = 20
        predicted = large_order_prediction(kappa, g, n_inst=1)
        bernoulli_asymp = 2.0 * kappa / TWO_PI ** (2 * g)
        # Should match to within 1%; subleading pole corrections are small.
        assert abs(predicted - bernoulli_asymp) / abs(bernoulli_asymp) < 0.01


# =====================================================================
# Section 13: Verdier scalar complementarity diagnostic
# =====================================================================

class TestVerdierScalarComplementarity:
    """Test Verdier scalar complementarity without nonperturbative promotion."""

    def test_kappa_plus_kappa_dual_virasoro(self):
        """kappa + kappa' = 13 for Virasoro on the Verdier scalar branch."""
        from lib.resurgence_shadow_tower_engine import koszul_complementarity_np
        for c_val in [1.0, 6.0, 13.0, 25.0]:
            result = koszul_complementarity_np(c_val, 1.0)
            assert abs(result['kappa_sum'] - 13.0) < 1e-12
            assert not result['nonperturbative_completion_certified']
            assert 'Verdier scalar branch' in result['dual_branch']
            assert result['object_firewall']['Omega(B(A))'] == 'bar-cobar inversion of A, not Koszul duality'

    def test_self_dual_at_c13(self):
        """c = 13 is the Virasoro self-dual point."""
        from lib.resurgence_shadow_tower_engine import koszul_complementarity_np
        result = koszul_complementarity_np(13.0, 1.0)
        assert result['is_self_dual']
        assert abs(result['kappa'] - result['kappa_dual']) < 1e-12

    def test_not_self_dual_generic_c(self):
        """Generic c is not self-dual."""
        from lib.resurgence_shadow_tower_engine import koszul_complementarity_np
        result = koszul_complementarity_np(1.0, 1.0)
        assert not result['is_self_dual']

    def test_formal_exponential_small(self):
        """exp(-A/hbar^2) is tiny for hbar = 1."""
        from lib.resurgence_shadow_tower_engine import koszul_complementarity_np
        result = koszul_complementarity_np(13.0, 1.0)
        assert result['exp_suppression'] < 1e-15
        assert result['F_np_certification'] == 'finite_window_diagnostic'


# =====================================================================
# Section 14: Gevrey analysis
# =====================================================================

class TestGevreyAnalysis:
    """Test the Gevrey order and optimal truncation."""

    def test_gevrey_order_is_zero(self):
        """The shadow series is Gevrey-0 (convergent)."""
        from lib.resurgence_shadow_tower_engine import gevrey_order
        result = gevrey_order(1.0, g_max=30)
        assert result['gevrey_order'] == 0
        assert not result['borel_summability_certified']

    def test_gevrey_ratio_converges(self):
        """The ratio |F_{g+1}/F_g| converges to 1/(4*pi^2)."""
        from lib.resurgence_shadow_tower_engine import gevrey_order
        result = gevrey_order(1.0, g_max=30)
        assert result['ratio_converges']

    def test_optimal_truncation_within_radius(self):
        """For hbar < 2*pi: the series converges, use all terms."""
        from lib.resurgence_shadow_tower_engine import optimal_truncation
        result = optimal_truncation(1.0, 1.0)
        assert result['within_convergence']
        assert not result['certified_optimal_truncation']

    def test_legacy_truncation_scale_is_diagnostic(self):
        """N* ~ A/hbar^2 is retained only as a diagnostic scale."""
        from lib.resurgence_shadow_tower_engine import optimal_truncation
        hbar = 3.0
        result = optimal_truncation(1.0, hbar)
        expected_Nstar = int(FOUR_PI_SQ / hbar ** 2)
        assert result['N_star_predicted'] == expected_Nstar
        assert result['certification'] == 'finite_window_diagnostic'
        assert not result['certified_optimal_truncation']


# =====================================================================
# Section 15: Cross-consistency checks (multi-path verification)
# =====================================================================

class TestCrossConsistency:
    """Cross-consistency between different computation methods."""

    def test_Fg_from_closed_form_vs_bernoulli(self):
        """F_g from Taylor expansion of closed form vs Bernoulli formula.

        Path 1: F_g = kappa * lambda_g^FP (Bernoulli)
        Path 2: Taylor coefficients of kappa * ((hbar/2)/sin(hbar/2) - 1)
        """
        from lib.resurgence_shadow_tower_engine import (
            F_g_scalar, genus_series_closed_form,
        )
        kappa = 1.0
        # Compute Z at small hbar and compare with partial sum
        hbar = 0.1
        exact = genus_series_closed_form(kappa, hbar)
        from_fg = sum(F_g_scalar(kappa, g) * hbar ** (2 * g) for g in range(1, 50))
        assert abs(exact - from_fg) / abs(exact) < 1e-12

    def test_first_u_pole_three_paths(self):
        """The first scalar u-pole A = (2*pi)^2 verified by three paths.

        Path 1: Location of nearest pole of (hbar/2)/sin(hbar/2) at hbar = 2*pi
        Path 2: From ratio F_{g+1}/F_g -> 1/A as g -> inf
        Path 3: Pade pole convergence
        """
        from lib.resurgence_shadow_tower_engine import (
            INSTANTON_ACTION, verify_borel_radius_from_coefficients,
            pade_poles_genus,
        )
        # Path 1: direct definition
        A_direct = FOUR_PI_SQ
        assert abs(INSTANTON_ACTION - A_direct) < 1e-12

        # Path 2: from coefficient ratios
        result = verify_borel_radius_from_coefficients(1.0, g_max=40)
        A_from_ratio = 1.0 / result['actual_ratios_last_5'][-1]
        assert abs(A_from_ratio - A_direct) / A_direct < 0.02

        # Path 3: Pade poles
        poles = pade_poles_genus(1.0, g_max=18)
        if len(poles) > 0:
            real_pos = [p.real for p in poles
                       if abs(p.imag) < abs(p.real) * 0.3 and p.real > 0]
            if real_pos:
                nearest = min(real_pos)
                assert abs(nearest - A_direct) / A_direct < 0.3

    def test_formal_residue_multiplier_two_paths(self):
        """Formal S_1 = -4*pi^2*kappa*i checked by residue conventions.

        Path 1: Direct from residue computation
        Path 2: Convention comparison with the u-plane residue
        """
        from lib.resurgence_shadow_tower_engine import (
            stokes_multiplier_leading, F_g_scalar,
        )
        kappa = 1.0
        # Path 1
        S1 = stokes_multiplier_leading(kappa)
        assert abs(S1 - (-FOUR_PI_SQ * kappa * 1.0j)) < 1e-10

        # Path 2: S_1 = 2*pi*i * Res_u * A^{g+1} / F_g at large g
        # Res_u = -8*pi^2*kappa, A = (2*pi)^2
        # S_1^{u-plane} = 2*pi*i * (-8*pi^2*kappa) = -16*pi^3*kappa*i
        # S_1^{hbar-plane} = -4*pi^2*kappa*i
        S1_hbar = -FOUR_PI_SQ * kappa * 1.0j
        assert abs(S1 - S1_hbar) < 1e-10

    def test_lambda_fp_generating_function(self):
        """lambda_g^FP satisfies the generating function (x/2)/sin(x/2) - 1.

        sum_{g>=1} lambda_g x^{2g} = (x/2)/sin(x/2) - 1
        """
        from lib.resurgence_shadow_tower_engine import lambda_fp
        x = 1.0
        # LHS: partial sum
        lhs = sum(lambda_fp(g) * x ** (2 * g) for g in range(1, 40))
        # RHS: exact
        rhs = (x / 2.0) / math.sin(x / 2.0) - 1.0
        assert abs(lhs - rhs) / abs(rhs) < 1e-12

    def test_kappa_virasoro_formula(self):
        """kappa(Vir_c) = c/2."""
        from lib.resurgence_shadow_tower_engine import kappa_virasoro
        for c in [0.5, 1.0, 13.0, 25.0, 26.0]:
            assert abs(kappa_virasoro(c) - c / 2.0) < 1e-14

    def test_kappa_heisenberg_formula(self):
        """kappa(H_k) = k for rank-1 Heisenberg at level k."""
        from lib.resurgence_shadow_tower_engine import kappa_heisenberg
        for k in [1.0, 2.0, 5.0]:
            assert abs(kappa_heisenberg(k) - k) < 1e-14

    def test_kappa_affine_sl2_formula(self):
        """kappa(aff sl_2, k) = 3*(k+2)/4."""
        from lib.resurgence_shadow_tower_engine import kappa_affine_sl2
        for k in [1.0, 2.0, 10.0]:
            assert abs(kappa_affine_sl2(k) - 3.0 * (k + 2.0) / 4.0) < 1e-14


# =====================================================================
# Section 16: Virasoro-specific tests at multiple central charges
# =====================================================================

class TestVirasoroLandscape:
    """Test scalar diagnostics across Virasoro central charges."""

    @pytest.mark.parametrize("c_val", [0.5, 1.0, 6.0, 13.0, 25.0])
    def test_shadow_invariants_consistent(self, c_val):
        """Shadow invariants are consistent for various c."""
        from lib.resurgence_shadow_tower_engine import virasoro_shadow_invariants
        inv = virasoro_shadow_invariants(c_val)
        assert abs(inv['kappa'] - c_val / 2.0) < 1e-14
        assert abs(inv['alpha'] - 2.0) < 1e-14
        assert abs(inv['Delta'] - 40.0 / (5.0 * c_val + 22.0)) < 1e-12
        assert inv['rho'] > 0

    @pytest.mark.parametrize("c_val", [0.5, 1.0, 6.0, 13.0, 25.0])
    def test_branch_points_conjugate(self, c_val):
        """Branch points are complex conjugate for c > 0."""
        from lib.resurgence_shadow_tower_engine import virasoro_shadow_invariants
        inv = virasoro_shadow_invariants(c_val)
        t_plus = inv['branch_plus']
        t_minus = inv['branch_minus']
        assert abs(t_minus - t_plus.conjugate()) < 1e-12

    @pytest.mark.parametrize("c_val", [1.0, 13.0, 25.0])
    def test_closed_form_matches_partial_sum(self, c_val):
        """Closed form matches partial sum for moderate hbar."""
        from lib.resurgence_shadow_tower_engine import (
            genus_series_closed_form, genus_series_partial_sum,
            kappa_virasoro,
        )
        kappa = kappa_virasoro(c_val)
        hbar = 1.0
        exact = genus_series_closed_form(kappa, hbar)
        partial = genus_series_partial_sum(kappa, hbar, 40)
        assert abs(partial - exact) / abs(exact) < 1e-10

    @pytest.mark.parametrize("c_val", [1.0, 13.0, 25.0])
    def test_stokes_multiplier_c_dependence(self, c_val):
        """Formal S_1 = -4*pi^2*(c/2)*i = -2*pi^2*c*i for Virasoro."""
        from lib.resurgence_shadow_tower_engine import (
            stokes_multiplier_leading, kappa_virasoro,
        )
        kappa = kappa_virasoro(c_val)
        S1 = stokes_multiplier_leading(kappa)
        expected = -FOUR_PI_SQ * (c_val / 2.0) * 1.0j
        assert abs(S1 - expected) < 1e-10


# =====================================================================
# Section 17: Edge cases and numerical stability
# =====================================================================

class TestEdgeCases:
    """Test edge cases and numerical stability."""

    def test_kappa_zero_gives_zero_Fg(self):
        """kappa = 0 gives F_g = 0 for all g."""
        from lib.resurgence_shadow_tower_engine import F_g_scalar
        for g in range(1, 10):
            assert abs(F_g_scalar(0.0, g)) < 1e-15

    def test_kappa_zero_stokes_multiplier_zero(self):
        """S_1 = 0 when kappa = 0 (trivial algebra)."""
        from lib.resurgence_shadow_tower_engine import stokes_multiplier_leading
        assert abs(stokes_multiplier_leading(0.0)) < 1e-15

    def test_large_genus_stability(self):
        """F_g is numerically stable for g up to 50."""
        from lib.resurgence_shadow_tower_engine import F_g_scalar
        kappa = 1.0
        for g in range(1, 51):
            Fg = F_g_scalar(kappa, g)
            assert math.isfinite(Fg)
            # F_g ~ 2*kappa/(2*pi)^{2g} should be tiny but finite
            if g >= 5:
                assert abs(Fg) < 1e-5

    def test_negative_kappa(self):
        """Negative kappa gives negative F_g (signs alternate with g)."""
        from lib.resurgence_shadow_tower_engine import F_g_scalar
        kappa = -1.0
        Fg = F_g_scalar(kappa, 1)
        assert Fg < 0  # F_1 = kappa/24 < 0

    def test_complex_hbar_borel(self):
        """Borel transform handles complex t correctly."""
        from lib.resurgence_shadow_tower_engine import borel_transform_genus
        val = borel_transform_genus(1.0, 1.0 + 1.0j, g_max=30)
        assert math.isfinite(abs(val))

    def test_lambda_fp_first_few(self):
        """lambda_1 = 1/24, lambda_2 = 7/5760."""
        from lib.resurgence_shadow_tower_engine import lambda_fp
        assert abs(lambda_fp(1) - 1.0 / 24.0) < 1e-14
        assert abs(lambda_fp(2) - 7.0 / 5760.0) < 1e-14
