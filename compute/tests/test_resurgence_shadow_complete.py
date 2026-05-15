r"""Tests for scalar genus diagnostics of the shadow partition function.

Verification of the genus-direction scalar pipeline:

1. Exact Bernoulli/Faber--Pandharipande coefficients
2. Exact A-hat scalar poles and residues
3. Entire factorial-divided Borel-transform diagnostics
4. Formal residue multipliers and trans-series diagnostics
5. Pade and partial-sum comparison with the scalar closed form
6. Finite-pole asymptotic estimates
7. Verdier-branch complementarity diagnostics
8. Firewalls preventing promotion to Borel summability, BTZ/JT,
   non-perturbative completion, or multiweight partition theorems

All tests use independently computed values.  No pattern matching or
copy-paste.

References:
    compute/lib/resurgence_shadow_complete.py
    compute/lib/shadow_partition_function.py
    compute/lib/resurgence_frontier_engine.py
    compute/lib/resurgence_stokes_engine.py
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
# Helpers
# =====================================================================

def bernoulli_number(n):
    """Independent Bernoulli number computation."""
    import mpmath
    return float(mpmath.bernoulli(n))


def lambda_fp_independent(g):
    """Independent computation of lambda_g^FP."""
    B2g = abs(bernoulli_number(2 * g))
    prefac = (2 ** (2 * g - 1) - 1) / (2 ** (2 * g - 1))
    return prefac * B2g / math.factorial(2 * g)


def F_g_independent(kappa, g):
    """Independent F_g = kappa * lambda_g^FP."""
    return kappa * lambda_fp_independent(g)


# =====================================================================
# Section 1: Algebra data
# =====================================================================

class TestAlgebraData:
    """Test algebra data construction."""

    def test_heisenberg_kappa(self):
        from lib.resurgence_shadow_complete import heisenberg_algebra
        h = heisenberg_algebra(rank=1)
        assert abs(h.kappa - 1.0) < 1e-14

    def test_heisenberg_kappa_rank2(self):
        from lib.resurgence_shadow_complete import heisenberg_algebra
        h = heisenberg_algebra(rank=2)
        assert abs(h.kappa - 2.0) < 1e-14

    def test_heisenberg_dual_kappa(self):
        """kappa + kappa' = 0 for the Heisenberg Verdier branch."""
        from lib.resurgence_shadow_complete import heisenberg_algebra
        h = heisenberg_algebra(rank=3)
        assert abs(h.kappa + h.kappa_dual) < 1e-14

    def test_virasoro_kappa(self):
        from lib.resurgence_shadow_complete import virasoro_algebra
        for c in [1.0, 13.0, 25.0, 26.0]:
            v = virasoro_algebra(c)
            assert abs(v.kappa - c / 2.0) < 1e-14

    def test_virasoro_dual_kappa(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13."""
        from lib.resurgence_shadow_complete import virasoro_algebra
        for c in [1.0, 6.0, 13.0, 25.0]:
            v = virasoro_algebra(c)
            assert abs(v.kappa + v.kappa_dual - 13.0) < 1e-14

    def test_virasoro_self_dual_c13(self):
        from lib.resurgence_shadow_complete import virasoro_algebra
        v = virasoro_algebra(13.0)
        assert abs(v.kappa - v.kappa_dual) < 1e-14

    def test_affine_sl2_kappa(self):
        from lib.resurgence_shadow_complete import affine_sl2_algebra
        a = affine_sl2_algebra(k=1.0)
        assert abs(a.kappa - 3.0 * 3.0 / 4.0) < 1e-14  # 3*(1+2)/4 = 9/4

    def test_affine_sl2_dual_kappa(self):
        """kappa + kappa' = 0 for the affine scalar dual-level branch."""
        from lib.resurgence_shadow_complete import affine_sl2_algebra
        a = affine_sl2_algebra(k=1.0)
        assert abs(a.kappa + a.kappa_dual) < 1e-14


# =====================================================================
# Section 2: Faber-Pandharipande and F_g
# =====================================================================

class TestFaberPandharipande:
    """Test the lambda_g^FP and F_g computations."""

    def test_lambda_fp_g1(self):
        """lambda_1^FP = 1/24."""
        from lib.resurgence_shadow_complete import lambda_fp
        assert abs(lambda_fp(1) - 1.0 / 24.0) < 1e-14

    def test_lambda_fp_g2(self):
        """lambda_2^FP = 7/5760."""
        from lib.resurgence_shadow_complete import lambda_fp
        assert abs(lambda_fp(2) - 7.0 / 5760.0) < 1e-14

    def test_lambda_fp_exact_g5(self):
        """lambda_5^FP = 73/3503554560."""
        from fractions import Fraction
        from lib.resurgence_shadow_complete import lambda_fp_exact
        assert lambda_fp_exact(5) == Fraction(73, 3503554560)

    def test_lambda_fp_matches_independent(self):
        from lib.resurgence_shadow_complete import lambda_fp
        for g in range(1, 15):
            assert abs(lambda_fp(g) - lambda_fp_independent(g)) < 1e-12 * max(abs(lambda_fp(g)), 1e-50)

    def test_F_g_scalar_kappa_1(self):
        """F_g(kappa=1) = lambda_g^FP."""
        from lib.resurgence_shadow_complete import F_g_scalar, lambda_fp
        for g in range(1, 10):
            assert abs(F_g_scalar(1.0, g) - lambda_fp(g)) < 1e-14

    def test_F_g_scalar_linearity(self):
        """F_g is linear in kappa."""
        from lib.resurgence_shadow_complete import F_g_scalar
        for g in range(1, 8):
            for kappa in [0.5, 2.0, 6.5]:
                assert abs(F_g_scalar(kappa, g) - kappa * F_g_scalar(1.0, g)) < 1e-13

    def test_F_g_array_length(self):
        from lib.resurgence_shadow_complete import F_g_array
        arr = F_g_array(1.0, 20)
        assert len(arr) == 20

    def test_F_g_positive(self):
        """F_g are positive for kappa > 0."""
        from lib.resurgence_shadow_complete import F_g_scalar
        for g in range(1, 20):
            assert F_g_scalar(1.0, g) > 0


# =====================================================================
# Section 3: Borel transform
# =====================================================================

class TestBorelTransformGenus:
    """Test the entire factorial-divided diagnostic transforms."""

    def test_borel_at_zero(self):
        from lib.resurgence_shadow_complete import borel_transform_genus
        val = borel_transform_genus(1.0, 0.0)
        assert abs(val) < 1e-14

    def test_borel_small_zeta(self):
        """At small zeta, B[F](zeta) ~ F_1 * zeta / Gamma(2) = kappa/24 * zeta."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        kappa = 1.0
        zeta = 0.01
        val = borel_transform_genus(kappa, zeta, g_max=50)
        leading = kappa / 24.0 * zeta  # F_1 = kappa/24, Gamma(2) = 1
        assert abs(val - leading) / abs(leading) < 0.01

    def test_borel_real_convergent(self):
        """B[F](zeta) is finite at sampled real points."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        for zeta in [1.0, 3.0, 5.0, 10.0]:
            val = borel_transform_genus(1.0, zeta, g_max=100)
            assert math.isfinite(abs(val))

    def test_borel_linearity_in_kappa(self):
        from lib.resurgence_shadow_complete import borel_transform_genus
        zeta = 2.0
        B1 = borel_transform_genus(1.0, zeta)
        B2 = borel_transform_genus(3.5, zeta)
        assert abs(B2 - 3.5 * B1) < 1e-10 * abs(B2)

    def test_borel_imaginary_zeta(self):
        """B[F] at imaginary zeta is finite at sampled points."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        val = borel_transform_genus(1.0, 3.0j, g_max=80)
        assert math.isfinite(abs(val))

    def test_borel_u_plane_at_zero(self):
        from lib.resurgence_shadow_complete import borel_transform_u_plane
        val = borel_transform_u_plane(1.0, 0.0)
        # B_u(0) = F_1 / Gamma(1) = F_1 = kappa/24
        assert abs(val - 1.0 / 24.0) < 1e-12

    def test_borel_u_plane_convergent(self):
        """B_u is finite at sampled u-plane points."""
        from lib.resurgence_shadow_complete import borel_transform_u_plane
        for xi in [1.0, 10.0, 30.0, 100.0]:
            val = borel_transform_u_plane(1.0, xi, g_max=80)
            assert math.isfinite(abs(val))

    def test_borel_coefficients_genus_count(self):
        from lib.resurgence_shadow_complete import borel_coefficients_genus
        coeffs = borel_coefficients_genus(1.0, 20)
        assert len(coeffs) == 20
        # First entry is (1, F_1/Gamma(2)) = (1, kappa/24).
        assert coeffs[0][0] == 1
        assert abs(coeffs[0][1] - 1.0 / 24.0) < 1e-14


# =====================================================================
# Section 4: Scalar A-hat poles and Borel radius firewall
# =====================================================================

class TestScalarAhatPoles:
    """Test scalar A-hat pole data and Borel-transform separation."""

    def test_scalar_pole_locations(self):
        from lib.resurgence_shadow_complete import borel_singularities_genus
        sings = borel_singularities_genus(5)
        assert len(sings) == 5
        for s in sings:
            n = s['n']
            assert abs(s['zeta_location'] - 2.0 * PI * n) < 1e-12
            assert s['object'] == 'scalar_ahat_closed_form'
            assert not s['borel_transform_singularity']

    def test_scalar_pole_u_locations(self):
        from lib.resurgence_shadow_complete import borel_singularities_genus
        sings = borel_singularities_genus(3)
        for s in sings:
            n = s['n']
            assert abs(s['u_location'] - (2.0 * PI * n) ** 2) < 1e-10

    def test_scalar_pole_residues(self):
        """Residue of (hbar/2)/sin(hbar/2) at hbar=2*pi*n is (-1)^n * 2*pi*n."""
        from lib.resurgence_shadow_complete import borel_singularities_genus
        sings = borel_singularities_genus(4)
        for s in sings:
            n = s['n']
            expected = (-1) ** n * 2.0 * PI * n
            assert abs(s['residue_of_ahat'] - expected) < 1e-10

    def test_borel_transform_radius_is_infinite(self):
        from lib.resurgence_shadow_complete import borel_radius_genus
        assert math.isinf(borel_radius_genus())

    def test_scalar_genus_radius(self):
        from lib.resurgence_shadow_complete import (
            scalar_genus_radius_hbar,
            scalar_genus_radius_u,
        )
        assert abs(scalar_genus_radius_hbar() - TWO_PI) < 1e-12
        assert abs(scalar_genus_radius_u() - FOUR_PI_SQ) < 1e-10

    def test_verify_borel_radius_from_coefficients(self):
        from lib.resurgence_shadow_complete import verify_borel_radius_from_coefficients
        result = verify_borel_radius_from_coefficients(1.0, g_max=40)
        assert result['converged']
        assert abs(result['predicted_u_radius'] - FOUR_PI_SQ) < 1e-10
        assert math.isinf(result['borel_transform_radius'])
        assert result['certification'] == 'finite_window_diagnostic'


# =====================================================================
# Section 5: Heisenberg Borel analysis
# =====================================================================

class TestHeisenbergBorel:
    """Test Heisenberg-specific scalar-pole diagnostics."""

    def test_heisenberg_borel_coefficients(self):
        from lib.resurgence_shadow_complete import heisenberg_borel_coefficients
        coeffs = heisenberg_borel_coefficients(1.0, 10)
        assert len(coeffs) == 10
        # First: g=1, F_1 = 1/24, Gamma(2) = 1, so b_1 = 1/24
        assert abs(coeffs[0]['borel_coeff'] - 1.0 / 24.0) < 1e-14

    def test_heisenberg_singularity_structure(self):
        from lib.resurgence_shadow_complete import heisenberg_borel_singularity_structure
        result = heisenberg_borel_singularity_structure(1.0)
        assert math.isinf(result['borel_radius'])
        assert abs(result['scalar_hbar_radius'] - TWO_PI) < 1e-12
        assert result['certification'] == 'certified_exact'
        assert len(result['singularities']) == 5

    def test_heisenberg_first_singularity_residue(self):
        from lib.resurgence_shadow_complete import heisenberg_borel_singularity_structure
        result = heisenberg_borel_singularity_structure(1.0)
        s1 = result['singularities'][0]
        # Residue at n=1: kappa * (-1)^1 * 2*pi*1 = -2*pi
        assert abs(s1['residue'] - (-2.0 * PI)) < 1e-10


# =====================================================================
# Section 6: Virasoro Borel analysis
# =====================================================================

class TestVirasoroBorel:
    """Test Virasoro genus-direction Borel transform."""

    def test_virasoro_borel_at_zero(self):
        from lib.resurgence_shadow_complete import virasoro_borel_genus
        val = virasoro_borel_genus(13.0, 0.0)
        assert abs(val) < 1e-14

    def test_virasoro_borel_small_zeta(self):
        from lib.resurgence_shadow_complete import virasoro_borel_genus
        c = 13.0
        kappa = 6.5
        zeta = 0.01
        val = virasoro_borel_genus(c, zeta, g_max=50)
        # Leading: F_1 * zeta / Gamma(2) = kappa/24 * zeta
        leading = kappa / 24.0 * zeta
        assert abs(val - leading) / abs(leading) < 0.01

    def test_virasoro_borel_scan_convergence(self):
        from lib.resurgence_shadow_complete import virasoro_borel_scan
        results = virasoro_borel_scan(
            c_values=[1.0, 13.0, 26.0],
            zeta_values=[1.0, 3.0],
            g_max=60,
        )
        for r in results:
            if r['within_radius']:
                assert math.isfinite(r['modulus_borel'])
            assert r['borel_certification'] == 'borel_transform_entire_diagnostic'

    def test_virasoro_c_half_borel(self):
        """Virasoro at c=1/2 (Ising): kappa = 1/4."""
        from lib.resurgence_shadow_complete import virasoro_borel_genus
        val = virasoro_borel_genus(0.5, 1.0, g_max=60)
        assert math.isfinite(abs(val))

    def test_virasoro_c26_borel(self):
        """Virasoro at c=26: kappa = 13 (critical)."""
        from lib.resurgence_shadow_complete import virasoro_borel_genus
        val = virasoro_borel_genus(26.0, 1.0, g_max=60)
        assert math.isfinite(abs(val))


# =====================================================================
# Section 7: Formal residue multipliers
# =====================================================================

class TestStokesMultipliers:
    """Test formal residue multipliers for the scalar pole model."""

    def test_S1_formula(self):
        """S_1 = kappa * (-1)^1 * 4*pi^2 * i = -4*pi^2*kappa*i."""
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_leading
        kappa = 1.0
        S1 = stokes_multiplier_genus_leading(kappa)
        expected = -FOUR_PI_SQ * 1.0j
        assert abs(S1 - expected) < 1e-10

    def test_S1_linearity(self):
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_leading
        S1_a = stokes_multiplier_genus_leading(1.0)
        S1_b = stokes_multiplier_genus_leading(3.0)
        assert abs(S1_b - 3.0 * S1_a) < 1e-10

    def test_S2_formula(self):
        """S_2 = kappa * (-1)^2 * 4*pi^2*2*i = 8*pi^2*kappa*i."""
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_n
        kappa = 1.0
        S2 = stokes_multiplier_genus_n(kappa, 2)
        expected = FOUR_PI_SQ * 2.0 * 1.0j
        assert abs(S2 - expected) < 1e-10

    def test_S3_formula(self):
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_n
        kappa = 2.0
        S3 = stokes_multiplier_genus_n(kappa, 3)
        expected = kappa * (-1) ** 3 * FOUR_PI_SQ * 3.0 * 1.0j
        assert abs(S3 - expected) < 1e-10

    def test_stokes_multiplier_purely_imaginary(self):
        """All S_n are purely imaginary."""
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_n
        for n in range(1, 6):
            Sn = stokes_multiplier_genus_n(1.0, n)
            assert abs(Sn.real) < 1e-10

    def test_stokes_alternating_sign(self):
        """S_n alternates in sign: S_1 < 0 imag, S_2 > 0 imag, etc."""
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_n
        for n in range(1, 6):
            Sn = stokes_multiplier_genus_n(1.0, n)
            expected_sign = (-1) ** n
            assert Sn.imag * expected_sign > 0


# =====================================================================
# Section 8: Trans-series
# =====================================================================

class TestTransseries:
    """Test the diagnostic genus trans-series construction."""

    def test_transseries_instanton_action(self):
        from lib.resurgence_shadow_complete import build_genus_transseries
        ts = build_genus_transseries(1.0, 20)
        assert abs(ts.instanton_action - FOUR_PI_SQ) < 1e-10
        assert ts.certification == 'analytic_resurgence_hypothesis'

    def test_transseries_perturbative_equals_F_g(self):
        from lib.resurgence_shadow_complete import build_genus_transseries, F_g_scalar
        ts = build_genus_transseries(1.0, 15)
        for g in range(1, 16):
            assert abs(ts.perturbative[g - 1] - F_g_scalar(1.0, g)) < 1e-14

    def test_transseries_one_instanton_decay(self):
        """One-instanton coefficients decay as 1/(2*pi)^{2g}."""
        from lib.resurgence_shadow_complete import build_genus_transseries
        ts = build_genus_transseries(1.0, 20)
        for g in range(1, 20):
            expected_order = 2.0 / TWO_PI ** (2 * g)
            assert abs(ts.one_instanton[g - 1]) < 10.0 * expected_order

    def test_transseries_two_instanton_faster_decay(self):
        """Two-instanton coefficients decay as 1/(4*pi)^{2g}, faster than one-instanton."""
        from lib.resurgence_shadow_complete import build_genus_transseries
        ts = build_genus_transseries(1.0, 15)
        for g in range(3, 15):
            assert abs(ts.two_instanton[g - 1]) < abs(ts.one_instanton[g - 1])

    def test_transseries_evaluate_perturbative(self):
        """With n_inst=0, trans-series reduces to perturbative sum."""
        from lib.resurgence_shadow_complete import (
            build_genus_transseries, transseries_evaluate_genus,
            genus_series_partial_sum,
        )
        kappa = 1.0
        hbar = 0.5
        ts = build_genus_transseries(kappa, 30)
        val = transseries_evaluate_genus(ts, hbar, n_inst=0)
        partial = genus_series_partial_sum(kappa, hbar, 30)
        assert abs(val - partial) < 1e-12

    def test_transseries_instanton_suppressed(self):
        """At small hbar, instanton corrections are exponentially suppressed."""
        from lib.resurgence_shadow_complete import (
            build_genus_transseries, transseries_evaluate_genus,
        )
        ts = build_genus_transseries(1.0, 20)
        val_0 = transseries_evaluate_genus(ts, 0.1, n_inst=0)
        val_1 = transseries_evaluate_genus(ts, 0.1, n_inst=1)
        # At hbar=0.1: exp(-A/hbar^2) = exp(-(2*pi)^2/0.01) ~ exp(-3948) ~ 0
        assert abs(val_1 - val_0) < 1e-100


# =====================================================================
# Section 9: Scalar closed form and ray-integral diagnostics
# =====================================================================

class TestScalarClosedForm:
    """Test scalar closed form, Pade, and partial sums."""

    def test_pade_genus_series_small_hbar(self):
        """Pade matches the scalar closed form at small hbar."""
        from lib.resurgence_shadow_complete import (
            pade_genus_series, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 0.5
        pade_val = pade_genus_series(kappa, hbar, g_max=20)
        exact = genus_series_closed_form(kappa, hbar)
        assert abs(pade_val - exact) / abs(exact) < 0.01

    def test_pade_genus_series_medium_hbar(self):
        """Pade matches the scalar closed form at medium hbar."""
        from lib.resurgence_shadow_complete import (
            pade_genus_series, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 2.0
        pade_val = pade_genus_series(kappa, hbar, g_max=25)
        exact = genus_series_closed_form(kappa, hbar)
        assert abs(pade_val - exact) / abs(exact) < 0.05

    def test_partial_sum_matches_exact(self):
        """Partial sum converges to exact within convergence radius."""
        from lib.resurgence_shadow_complete import (
            genus_series_partial_sum, genus_series_closed_form,
        )
        kappa = 1.0
        hbar = 1.0
        partial = genus_series_partial_sum(kappa, hbar, g_max=50)
        exact = genus_series_closed_form(kappa, hbar)
        assert abs(partial - exact) / abs(exact) < 1e-8

    def test_closed_form_pole_at_2pi(self):
        """Closed form diverges as hbar -> 2*pi."""
        from lib.resurgence_shadow_complete import genus_series_closed_form
        val1 = abs(genus_series_closed_form(1.0, TWO_PI - 0.1))
        val2 = abs(genus_series_closed_form(1.0, TWO_PI - 0.01))
        assert val2 > val1  # getting larger as we approach the pole

    def test_closed_form_at_small_hbar(self):
        """At small hbar: Z ~ kappa * hbar^2/24 (leading term)."""
        from lib.resurgence_shadow_complete import genus_series_closed_form
        kappa = 1.0
        hbar = 0.01
        val = genus_series_closed_form(kappa, hbar)
        leading = kappa * hbar ** 2 / 24.0
        assert abs(val - leading) / abs(leading) < 0.01


# =====================================================================
# Section 10: Finite-pole coefficient asymptotics
# =====================================================================

class TestLargeOrderRelations:
    """Test finite-pole asymptotic predictions for F_g."""

    def test_large_order_leading_heisenberg(self):
        """For Heisenberg, large-order prediction matches Bernoulli asymptotics."""
        from lib.resurgence_shadow_complete import large_order_prediction, F_g_scalar
        kappa = 1.0
        for g in range(5, 15):
            Fg = F_g_scalar(kappa, g)
            Fg_pred = large_order_prediction(kappa, g, n_inst=3)
            rel_err = abs(Fg - Fg_pred) / abs(Fg)
            assert rel_err < 0.5

    def test_finite_pole_error_drops_with_g(self):
        """Relative error of large-order prediction decreases with g."""
        from lib.resurgence_shadow_complete import large_order_prediction, F_g_scalar
        kappa = 1.0
        errors = []
        for g in range(3, 20):
            Fg = F_g_scalar(kappa, g)
            Fg_pred = large_order_prediction(kappa, g, n_inst=5)
            errors.append(abs(Fg - Fg_pred) / abs(Fg))
        # Check that errors generally decrease (not necessarily monotonically)
        assert errors[-1] < errors[0]

    def test_more_scalar_poles_improve_prediction(self):
        """Including more scalar poles improves the prediction."""
        from lib.resurgence_shadow_complete import large_order_prediction, F_g_scalar
        kappa = 1.0
        g = 10
        Fg = F_g_scalar(kappa, g)
        err_1 = abs(Fg - large_order_prediction(kappa, g, 1)) / abs(Fg)
        err_3 = abs(Fg - large_order_prediction(kappa, g, 3)) / abs(Fg)
        assert err_3 < err_1

    def test_large_order_verification_output(self):
        from lib.resurgence_shadow_complete import large_order_verification
        result = large_order_verification(1.0, g_max=15, n_inst=3)
        assert len(result['results']) == 15
        assert result['error_at_gmax'] is not None
        assert result['certification'] == 'finite_window_diagnostic'

    def test_large_order_virasoro(self):
        """Virasoro large-order: same structure as Heisenberg (scalar level)."""
        from lib.resurgence_shadow_complete import large_order_prediction, F_g_scalar
        kappa = 6.5  # c = 13
        g = 12
        Fg = F_g_scalar(kappa, g)
        Fg_pred = large_order_prediction(kappa, g, n_inst=3)
        rel_err = abs(Fg - Fg_pred) / abs(Fg)
        assert rel_err < 0.3

    def test_large_order_prediction_at_g1(self):
        """At g=1, the prediction is nonzero but not exact."""
        from lib.resurgence_shadow_complete import large_order_prediction, F_g_scalar
        kappa = 1.0
        Fg = F_g_scalar(kappa, 1)
        Fg_pred = large_order_prediction(kappa, 1, n_inst=10)
        # At g=1, the prediction is less accurate
        assert abs(Fg_pred) > 0

    def test_large_order_sign_pattern(self):
        """F_g and the finite-pole prediction are positive in this range."""
        from lib.resurgence_shadow_complete import large_order_prediction
        kappa = 1.0
        for g in range(2, 15):
            pred = large_order_prediction(kappa, g, n_inst=5)
            assert pred > 0  # All F_g are positive


# =====================================================================
# Section 11: Formal Peacock-table diagnostics
# =====================================================================

class TestPeacockPattern:
    """Test the formal residue table shaped like a Peacock pattern."""

    def test_peacock_S10_equals_S1(self):
        """S_{1,0} = S_1 (first Stokes multiplier)."""
        from lib.resurgence_shadow_complete import (
            peacock_stokes_constant, stokes_multiplier_genus_leading,
        )
        kappa = 1.0
        S10 = peacock_stokes_constant(kappa, 1, 0)
        S1 = stokes_multiplier_genus_leading(kappa)
        assert abs(S10 - S1) < 1e-10

    def test_peacock_S20_equals_S2(self):
        from lib.resurgence_shadow_complete import (
            peacock_stokes_constant, stokes_multiplier_genus_n,
        )
        kappa = 1.0
        S20 = peacock_stokes_constant(kappa, 2, 0)
        S2 = stokes_multiplier_genus_n(kappa, 2)
        assert abs(S20 - S2) < 1e-10

    def test_peacock_S21_equals_S1(self):
        """S_{2,1} = S_{2-1} = S_1 in the simple-pole model."""
        from lib.resurgence_shadow_complete import (
            peacock_stokes_constant, stokes_multiplier_genus_n,
        )
        kappa = 1.0
        S21 = peacock_stokes_constant(kappa, 2, 1)
        S1 = stokes_multiplier_genus_n(kappa, 1)
        assert abs(S21 - S1) < 1e-10

    def test_peacock_table_size(self):
        from lib.resurgence_shadow_complete import peacock_pattern_table
        table = peacock_pattern_table(1.0, n_max=4)
        # Entries: (1,0), (2,0), (2,1), (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (4,3)
        assert len(table) == 10

    def test_peacock_triangle_structure(self):
        from lib.resurgence_shadow_complete import peacock_resurgence_triangle
        triangle = peacock_resurgence_triangle(1.0, 4)
        assert len(triangle) == 4
        assert len(triangle[0]) == 1  # row 1: S_{1,0}
        assert len(triangle[1]) == 2  # row 2: S_{2,0}, S_{2,1}
        assert len(triangle[2]) == 3  # row 3
        assert len(triangle[3]) == 4  # row 4

    def test_peacock_purely_imaginary(self):
        """All peacock entries are purely imaginary."""
        from lib.resurgence_shadow_complete import peacock_resurgence_triangle
        triangle = peacock_resurgence_triangle(1.0, 4)
        for row in triangle:
            for entry in row:
                assert abs(entry.real) < 1e-10

    def test_peacock_S_nm_zero_for_n_leq_m(self):
        from lib.resurgence_shadow_complete import peacock_stokes_constant
        assert abs(peacock_stokes_constant(1.0, 1, 1)) < 1e-14
        assert abs(peacock_stokes_constant(1.0, 2, 3)) < 1e-14


# =====================================================================
# Section 12: Verdier-branch complementarity diagnostics
# =====================================================================

class TestVerdierBranchComplementarity:
    """Test dual-branch diagnostics without object conflation."""

    def test_koszul_np_heisenberg(self):
        from lib.resurgence_shadow_complete import (
            heisenberg_algebra, koszul_nonperturbative_genus,
        )
        alg = heisenberg_algebra(rank=1)
        result = koszul_nonperturbative_genus(alg, 0.5, g_max=20)
        assert math.isfinite(result['F_perturbative'])
        assert result['dual_branch'] == 'A^! Verdier/continuous-linear dual branch'
        assert result['certification'] == 'analytic_resurgence_hypothesis'
        # The Heisenberg dual branch has kappa = -1, so F_pert_dual is negative.
        assert result['F_perturbative_dual'] < 0

    def test_koszul_np_virasoro(self):
        from lib.resurgence_shadow_complete import (
            virasoro_algebra, koszul_nonperturbative_genus,
        )
        alg = virasoro_algebra(13.0)
        result = koszul_nonperturbative_genus(alg, 1.0, g_max=20)
        assert result['is_self_dual']
        assert abs(result['kappa'] - result['kappa_dual']) < 1e-10

    def test_koszul_self_dual_check(self):
        from lib.resurgence_shadow_complete import koszul_self_dual_check
        result = koszul_self_dual_check(c_val=13.0, hbar=1.0)
        assert result['kappa_equals_kappa_dual']
        assert result['symmetry'] == 'scalar branch fixed point'

    def test_koszul_not_self_dual(self):
        from lib.resurgence_shadow_complete import koszul_self_dual_check
        result = koszul_self_dual_check(c_val=1.0, hbar=1.0)
        assert not result['kappa_equals_kappa_dual']
        assert result['symmetry'] == 'scalar branches distinct'

    def test_koszul_instanton_suppressed(self):
        """At small hbar, instanton correction is negligible."""
        from lib.resurgence_shadow_complete import (
            virasoro_algebra, koszul_nonperturbative_genus,
        )
        alg = virasoro_algebra(13.0)
        result = koszul_nonperturbative_genus(alg, 0.1, g_max=20)
        assert result['exp_suppression'] < 1e-100

    def test_koszul_complementarity_sum(self):
        """kappa + kappa' = 13 for the Virasoro scalar dual branch."""
        from lib.resurgence_shadow_complete import virasoro_algebra
        for c in [1.0, 6.0, 13.0, 25.0]:
            alg = virasoro_algebra(c)
            assert abs(alg.kappa + alg.kappa_dual - 13.0) < 1e-14

    def test_object_firewall_records_five_distinct_objects(self):
        from lib.resurgence_shadow_complete import OBJECT_FIREWALLS
        for key in ['A', 'B(A)', 'A^i', 'A^!', 'Z_ch^der(A)']:
            assert key in OBJECT_FIREWALLS
        assert 'inversion, not Koszul duality' in OBJECT_FIREWALLS['bar_cobar']

    def test_kernel_normalization_firewall(self):
        from lib.resurgence_shadow_complete import KERNEL_NORMALIZATIONS
        assert KERNEL_NORMALIZATIONS['affine_raw_collision'] == 'k*Omega_tr/z'
        assert KERNEL_NORMALIZATIONS['affine_KZ'] == 'Omega/((k+h_vee)z)'
        assert KERNEL_NORMALIZATIONS['heisenberg'] == 'k/z'
        assert KERNEL_NORMALIZATIONS['virasoro'] == '(c/2)/z^3 + 2T/z'


# =====================================================================
# Section 13: Optimal truncation
# =====================================================================

class TestOptimalTruncation:
    """Test finite-window truncation diagnostics for the genus series."""

    def test_optimal_N_star_formula(self):
        """Diagnostic N* = floor(A / hbar^2) = floor((2*pi)^2 / hbar^2)."""
        from lib.resurgence_shadow_complete import optimal_truncation_genus
        result = optimal_truncation_genus(1.0, 1.0)
        A = FOUR_PI_SQ
        expected_N = int(A / 1.0)  # = 39
        assert result['N_star_predicted'] == expected_N
        assert result['certification'] == 'finite_window_diagnostic'

    def test_optimal_truncation_hbar_2(self):
        """At hbar = 2: N* = floor(4*pi^2 / 4) = floor(9.87) = 9."""
        from lib.resurgence_shadow_complete import optimal_truncation_genus
        result = optimal_truncation_genus(1.0, 2.0)
        A = FOUR_PI_SQ
        expected_N = int(A / 4.0)
        assert result['N_star_predicted'] == expected_N

    def test_optimal_truncation_minimum_error(self):
        """The displayed window contains the diagnostic scale."""
        from lib.resurgence_shadow_complete import optimal_truncation_genus
        result = optimal_truncation_genus(1.0, 1.0)
        N_star = result['N_star_predicted']
        if result['N_star_actual'] is not None:
            assert abs(result['N_star_actual'] - N_star) <= 3

    def test_optimal_truncation_np_suppression(self):
        """Non-perturbative suppression exp(-A/hbar^2)."""
        from lib.resurgence_shadow_complete import optimal_truncation_genus
        result = optimal_truncation_genus(1.0, 1.0)
        expected = math.exp(-FOUR_PI_SQ)
        assert abs(result['np_suppression'] - expected) / expected < 1e-10


# =====================================================================
# Section 14: Full pipeline
# =====================================================================

class TestFullPipeline:
    """Test the scalar diagnostic analysis bundle."""

    def test_full_analysis_runs(self):
        from lib.resurgence_shadow_complete import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, g_max=15)
        assert 'borel' in result
        assert 'stokes' in result
        assert 'large_order' in result
        assert 'peacock_triangle' in result

    def test_full_analysis_borel_radius(self):
        from lib.resurgence_shadow_complete import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, g_max=15)
        assert math.isinf(result['borel']['radius'])
        assert abs(result['borel']['scalar_hbar_radius'] - TWO_PI) < 1e-12

    def test_full_analysis_stokes_S1(self):
        from lib.resurgence_shadow_complete import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, g_max=15)
        S1 = result['stokes']['S_1']
        assert abs(S1 - (-FOUR_PI_SQ * 1.0j)) < 1e-10
        assert result['stokes']['certification'] == 'analytic_resurgence_hypothesis'

    def test_full_analysis_peacock_triangle(self):
        from lib.resurgence_shadow_complete import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, g_max=15)
        triangle = result['peacock_triangle']
        assert len(triangle) == 4

    def test_full_analysis_certification_firewall(self):
        from lib.resurgence_shadow_complete import full_resurgence_analysis
        result = full_resurgence_analysis(1.0, g_max=8)
        summary = result['certification_summary']
        assert summary['borel_transform_entire'] == 'certified_exact'
        assert summary['formal_stokes_multipliers'] == 'analytic_resurgence_hypothesis'
        assert summary['nonperturbative_completion'] == 'analytic_resurgence_hypothesis'
        assert summary['BTZ_JT_recovery'] == 'not_certified_here'
        assert summary['all_genus_multiweight_partition_theorem'] == 'not_certified_here'


# =====================================================================
# Section 15: Cross-family comparison
# =====================================================================

class TestCrossFamilyComparison:
    """Test scalar A-hat diagnostics across families."""

    def test_family_comparison_runs(self):
        from lib.resurgence_shadow_complete import family_comparison
        results = family_comparison(g_max=10)
        assert len(results) >= 5

    def test_universal_instanton_action(self):
        """All scalar diagnostics share pole scale (2*pi)^2."""
        from lib.resurgence_shadow_complete import family_comparison
        results = family_comparison(g_max=10)
        for name, data in results.items():
            assert abs(data['instanton_action'] - FOUR_PI_SQ) < 1e-10

    def test_borel_transform_entire_and_scalar_radius(self):
        """All sampled families have entire Borel transforms and scalar radius 2*pi."""
        from lib.resurgence_shadow_complete import family_comparison
        results = family_comparison(g_max=10)
        for name, data in results.items():
            assert math.isinf(data['borel_radius'])
            assert abs(data['scalar_hbar_radius'] - TWO_PI) < 1e-12
            assert data['certification'] == 'finite_window_diagnostic'
            assert 'multiweight partition theorem' in data['not_certified']

    def test_S1_proportional_to_kappa(self):
        """S_1 = -4*pi^2*kappa*i for all families."""
        from lib.resurgence_shadow_complete import family_comparison
        results = family_comparison(g_max=10)
        for name, data in results.items():
            S1 = data['S_1']
            kappa = data['kappa']
            expected = -FOUR_PI_SQ * kappa * 1.0j
            assert abs(S1 - expected) < 1e-8

    def test_F1_proportional_to_kappa(self):
        """F_1 = kappa/24 for all families."""
        from lib.resurgence_shadow_complete import family_comparison
        results = family_comparison(g_max=10)
        for name, data in results.items():
            assert abs(data['F_1'] - data['kappa'] / 24.0) < 1e-14


# =====================================================================
# Section 16: Convergence radius from coefficient ratios
# =====================================================================

class TestCoefficientRatios:
    """Test convergence radius determination from coefficient ratios."""

    def test_genus_ratio_limit(self):
        """Ratio F_{g+1}/F_g -> 1/(2*pi)^2 as g -> infty."""
        from lib.resurgence_shadow_complete import F_g_scalar
        kappa = 1.0
        ratios = []
        for g in range(5, 25):
            Fg = F_g_scalar(kappa, g)
            Fg1 = F_g_scalar(kappa, g + 1)
            ratios.append(Fg1 / Fg)
        target = 1.0 / (TWO_PI ** 2)
        assert abs(ratios[-1] - target) / target < 0.01

    def test_bernoulli_growth_rate(self):
        """B_{2g} ~ (-1)^{g+1} 2(2g)! / (2*pi)^{2g} at large g."""
        for g in range(5, 15):
            B2g = bernoulli_number(2 * g)
            predicted = (-1) ** (g + 1) * 2.0 * math.factorial(2 * g) / TWO_PI ** (2 * g)
            ratio = B2g / predicted
            assert abs(ratio - 1.0) < 0.1  # Converges to 1


# =====================================================================
# Section 17: Borel plane visualization data
# =====================================================================

class TestBorelPlaneVisualization:
    """Test data generation for Borel plane visualization."""

    def test_borel_on_real_axis(self):
        """B[F](zeta) on the real axis should be smooth for 0 < zeta < 2*pi."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        kappa = 1.0
        prev = 0.0
        for zeta in [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]:
            val = borel_transform_genus(kappa, zeta, g_max=60)
            assert math.isfinite(abs(val))
            assert abs(val) > prev  # monotonically increasing (for kappa > 0)
            prev = abs(val)

    def test_borel_on_imaginary_axis(self):
        """B[F](i*y) is finite for real kappa."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        kappa = 1.0
        for y in [1.0, 2.0, 3.0]:
            val = borel_transform_genus(kappa, 1.0j * y, g_max=60)
            assert math.isfinite(abs(val))


# =====================================================================
# Section 18: Special values and cross-checks
# =====================================================================

class TestSpecialValues:
    """Test special values and cross-checks."""

    def test_F1_exact(self):
        """F_1 = kappa/24 (universal)."""
        from lib.resurgence_shadow_complete import F_g_scalar
        for kappa in [0.5, 1.0, 6.5, 13.0]:
            assert abs(F_g_scalar(kappa, 1) - kappa / 24.0) < 1e-14

    def test_F2_exact(self):
        """F_2 = kappa * 7/5760."""
        from lib.resurgence_shadow_complete import F_g_scalar
        for kappa in [0.5, 1.0, 6.5]:
            assert abs(F_g_scalar(kappa, 2) - kappa * 7.0 / 5760.0) < 1e-14

    def test_closed_form_at_hbar_1(self):
        """Z^sh(kappa=1, hbar=1) = (1/2)/sin(1/2) - 1."""
        from lib.resurgence_shadow_complete import genus_series_closed_form
        val = genus_series_closed_form(1.0, 1.0)
        expected = 0.5 / math.sin(0.5) - 1.0
        assert abs(val - expected) < 1e-14

    def test_closed_form_symmetry(self):
        """Z^sh(hbar) = Z^sh(-hbar) (even function)."""
        from lib.resurgence_shadow_complete import genus_series_closed_form
        for hbar in [0.5, 1.0, 2.0, 5.0]:
            assert abs(genus_series_closed_form(1.0, hbar) -
                       genus_series_closed_form(1.0, -hbar)) < 1e-14

    def test_F_g_sum_convergence_at_hbar_1(self):
        """sum_{g=1}^G F_g -> Z^sh(hbar=1) as G -> infty."""
        from lib.resurgence_shadow_complete import (
            genus_series_partial_sum, genus_series_closed_form,
        )
        kappa = 1.0
        exact = genus_series_closed_form(kappa, 1.0)
        for G in [10, 20, 30]:
            partial = genus_series_partial_sum(kappa, 1.0, G)
            assert abs(partial - exact) < 10.0 ** (-(G // 3))

    def test_borel_transform_kappa_zero(self):
        """At kappa = 0: everything vanishes."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        val = borel_transform_genus(0.0, 1.0)
        assert abs(val) < 1e-14

    def test_stokes_kappa_zero(self):
        """At kappa = 0: all Stokes multipliers vanish."""
        from lib.resurgence_shadow_complete import stokes_multiplier_genus_n
        for n in range(1, 5):
            assert abs(stokes_multiplier_genus_n(0.0, n)) < 1e-14


# =====================================================================
# Section 19: Consistency with existing modules
# =====================================================================

class TestConsistencyWithExisting:
    """Cross-check with existing resurgence and shadow partition function modules."""

    def test_F_g_matches_utils(self):
        """F_g matches the utils module."""
        try:
            from lib.utils import lambda_fp as utils_lambda_fp, F_g as utils_F_g
            from lib.resurgence_shadow_complete import F_g_scalar, lambda_fp
            from sympy import Rational
            for g in range(1, 10):
                # utils returns Rational, our module returns float
                utils_val = float(utils_lambda_fp(g))
                our_val = lambda_fp(g)
                assert abs(utils_val - our_val) / abs(utils_val) < 1e-12
        except ImportError:
            pytest.skip("utils module not available")

    def test_scalar_radius_matches_shadow_pf(self):
        """Scalar genus radius matches shadow_pf_convergence."""
        try:
            from lib.shadow_pf_convergence import genus_convergence_radius
            from lib.resurgence_shadow_complete import scalar_genus_radius_hbar
            assert abs(genus_convergence_radius() - scalar_genus_radius_hbar()) < 1e-12
        except ImportError:
            pytest.skip("shadow_pf_convergence not available")

    def test_closed_form_matches_shadow_pf(self):
        """Closed form matches shadow_pf_convergence."""
        try:
            from lib.shadow_pf_convergence import genus_series_closed_form as spf_closed
            from lib.resurgence_shadow_complete import genus_series_closed_form
            kappa = 1.0
            for hbar in [0.5, 1.0, 2.0]:
                val1 = spf_closed(kappa, hbar)
                val2 = genus_series_closed_form(kappa, hbar)
                assert abs(val1 - val2) < 1e-12
        except ImportError:
            pytest.skip("shadow_pf_convergence not available")


# =====================================================================
# Section 20: Edge cases and robustness
# =====================================================================

class TestEdgeCases:
    """Test edge cases and robustness."""

    def test_borel_at_large_zeta(self):
        """Borel transform handles large |zeta| without crashing."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        # The finite truncation is a diagnostic value beyond the scalar disk.
        val = borel_transform_genus(1.0, 10.0, g_max=30)
        assert isinstance(val, complex)

    def test_negative_kappa(self):
        """Negative kappa values from dual branches are supported."""
        from lib.resurgence_shadow_complete import F_g_scalar, borel_transform_genus
        kappa = -1.0
        assert F_g_scalar(kappa, 1) < 0
        val = borel_transform_genus(kappa, 1.0)
        assert math.isfinite(abs(val))

    def test_large_kappa(self):
        from lib.resurgence_shadow_complete import F_g_scalar, borel_transform_genus
        kappa = 1000.0
        assert F_g_scalar(kappa, 1) == kappa / 24.0
        val = borel_transform_genus(kappa, 0.1)
        assert math.isfinite(abs(val))

    def test_g_max_1(self):
        """With g_max=1, only the first term contributes."""
        from lib.resurgence_shadow_complete import borel_transform_genus
        kappa = 1.0
        zeta = 1.0
        val = borel_transform_genus(kappa, zeta, g_max=1)
        expected = kappa / 24.0 * zeta  # F_1 * zeta / Gamma(2)
        assert abs(val - expected) < 1e-14

    def test_transseries_at_hbar_zero(self):
        from lib.resurgence_shadow_complete import (
            build_genus_transseries, transseries_evaluate_genus,
        )
        ts = build_genus_transseries(1.0, 10)
        val = transseries_evaluate_genus(ts, 0.0)
        assert abs(val) < 1e-14

    def test_peacock_empty_for_small_n(self):
        from lib.resurgence_shadow_complete import peacock_resurgence_triangle
        triangle = peacock_resurgence_triangle(1.0, 1)
        assert len(triangle) == 1
        assert len(triangle[0]) == 1
