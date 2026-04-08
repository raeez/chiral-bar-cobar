r"""Tests for kappa_painleve_engine.py -- kappa-deformed Painleve I.

Covers the seven tasks:
  1. Numerical solution of kappa-P_I at kappa = 1, 13, 24
  2. Tritronquee asymptotics
  3. Stokes multipliers (Kapaev)
  4. Dispersionless limit
  5. Fredholm / kernel structure (benchmarks vs. Airy)
  6. Isomonodromic deformation
  7. Random matrix / beta-ensemble identification

Plus:
  - Rescaling theorem (the load-bearing identity): cross-verification via two
    independent integration paths.
  - Multi-path verification of all published constants.
  - Anti-pattern guards (AP24, AP39, AP48 for kappa values).

Total: 50+ tests.
"""

import math
import cmath
import pytest
import numpy as np

from compute.lib.kappa_painleve_engine import (
    # Family kappa values
    kappa_virasoro, kappa_heisenberg, kappa_lattice, kappa_moonshine,
    kappa_virasoro_self_dual, kappa_AP24_sum,
    # Rescaling theorem
    rescale_x_to_X, rescale_X_to_x, rescale_Y_to_y, rescale_y_to_Y,
    verify_rescaling_at,
    # Numerical solver
    standard_pi_rhs, solve_standard_pi, solve_kappa_pi,
    # Tritronquee
    tritronquee_initial_data, kappa_tritronquee_initial_data,
    kappa_tritronquee_first_pole, kappa_tritronquee_asymptotic,
    integrate_kappa_tritronquee,
    # Stokes
    KAPAEV_TRITRONQUEE_STOKES, kappa_stokes_multipliers,
    kappa_wkb_action_along_Boutroux, trans_series_first_correction,
    # Dispersionless
    dispersionless_limit_riccati, true_riccati_first_integral,
    verify_dispersionless_at_large_kappa,
    # Fredholm
    airy_kernel, pi_kernel_structure, tau_pi_minus_log_det_relation,
    # Isomonodromic
    isomonodromic_check_kappa,
    # Random matrix
    beta_ensemble_identification, pi_matrix_model_correspondence,
    # Verification
    verify_tritronquee_initial_data_by_shooting,
    verify_first_pole_by_integration,
    cross_verify_kappa_pi_via_rescaling,
    # Summary
    kappa_pi_summary_for_kappa, landscape_summary,
    # Constants
    X_TRITRONQUEE_FIRST_POLE_POS_REAL,
    Y_TRITRONQUEE_AT_ZERO, YPRIME_TRITRONQUEE_AT_ZERO,
    ALPHA_BOUTROUX, SECTOR_HALFWIDTH,
)


# ============================================================================
# Section 1: Family kappa values (AP1, AP24, AP39, AP48 guards)
# ============================================================================

class TestFamilyKappaValues:
    def test_virasoro_kappa_equals_half_c(self):
        """AP39: kappa(Vir_c) = c/2, Virasoro-specific."""
        assert kappa_virasoro(2.0).kappa == 1.0
        assert kappa_virasoro(26.0).kappa == 13.0
        assert kappa_virasoro(13.0).kappa == 6.5

    def test_heisenberg_kappa_equals_k(self):
        """AP1, AP48: Heisenberg kappa = k (level), NOT c/2."""
        assert kappa_heisenberg(1.0).kappa == 1.0
        assert kappa_heisenberg(2.0).kappa == 2.0

    def test_lattice_kappa_equals_rank(self):
        """AP48: lattice VOA has kappa = rank, NOT c/2."""
        assert kappa_lattice(24).kappa == 24.0
        assert kappa_lattice(8).kappa == 8.0

    def test_moonshine_uses_niemeier_convention(self):
        """User asked about kappa = 24; moonshine Niemeier convention returns 24."""
        assert kappa_moonshine().kappa == 24.0

    def test_virasoro_self_dual_c13_has_kappa_13_over_2(self):
        """AP24: at c=13, kappa = 13/2 = 6.5, NOT 13.  The 13 is the SUM."""
        assert kappa_virasoro_self_dual().kappa == 6.5

    def test_AP24_sum_kappa_is_literal_13(self):
        """The literal kappa=13 the user asked about: it's the AP24 sum."""
        assert kappa_AP24_sum().kappa == 13.0

    def test_kappa_values_have_provenance(self):
        """Every kappa carries audit trail."""
        for f in [kappa_virasoro(2.0), kappa_heisenberg(1.0),
                  kappa_lattice(24), kappa_moonshine()]:
            assert isinstance(f.source, str)
            assert len(f.source) > 0


# ============================================================================
# Section 2: Rescaling theorem (the load-bearing identity)
# ============================================================================

class TestRescalingTheorem:
    def test_rescaling_roundtrip_x(self):
        """rescale_X_to_x composed with rescale_x_to_X is identity."""
        for kappa in [1.0, 13.0, 24.0, 0.5]:
            for x in [-3.0, -1.0, 1.0, 5.0]:
                X = rescale_x_to_X(x, kappa)
                x_back = rescale_X_to_x(X, kappa)
                assert abs(x_back - x) < 1e-12

    def test_rescaling_roundtrip_Y(self):
        for kappa in [1.0, 13.0, 24.0]:
            for Y in [-1.0, 0.0, 0.5, 2.0]:
                y = rescale_Y_to_y(Y, kappa)
                Y_back = rescale_y_to_Y(y, kappa)
                assert abs(Y_back - Y) < 1e-12

    def test_rescaling_kappa_1_is_identity(self):
        """At kappa=1, rescaling is identity."""
        for x in [-2.0, 0.0, 3.0]:
            assert abs(rescale_x_to_X(x, 1.0) - x) < 1e-12
        for Y in [-1.0, 0.5]:
            assert abs(rescale_Y_to_y(Y, 1.0) - Y) < 1e-12

    def test_rescaling_kappa_13_exponents(self):
        """Numerical check: kappa^(1/5), kappa^(3/5), kappa^(2/5)."""
        k = 13.0
        assert abs(rescale_X_to_x(1.0, k) - k ** 0.2) < 1e-12
        assert abs(rescale_Y_to_y(1.0, k) - k ** 0.6) < 1e-12

    def test_rescaling_preserves_painleve_equation(self):
        """Algebraic verification: if Y'' = 6 Y^2 + X then rescaled y satisfies
        y'' = (6/kappa) y^2 + x.  Test at several points on the standard
        P_I tritronquee."""
        Y0, Y0p = tritronquee_initial_data()
        result = solve_standard_pi(0.0, -1.5, Y0, Y0p, max_step=0.01)
        for idx in [0, 50, 100, -1]:
            X_val = float(result['sol'].t[idx])
            Y_val = float(result['sol'].y[0][idx])
            Yp_val = float(result['sol'].y[1][idx])
            Ydp_val = 6 * Y_val * Y_val + X_val
            for kappa in [1.0, 13.0, 24.0]:
                x_val = rescale_X_to_x(X_val, kappa)
                ver = verify_rescaling_at(x_val, kappa, Y_val, Yp_val, Ydp_val)
                assert abs(ver['standard_residual']) < 1e-8, f"Standard P_I residual @ kappa={kappa}"
                assert abs(ver['kappa_residual']) < 1e-7, f"kappa-P_I residual @ kappa={kappa}"


# ============================================================================
# Section 3: Standard P_I numerical solver (ground truth)
# ============================================================================

class TestStandardPainleveI:
    def test_rhs_at_origin(self):
        """At (X, Y, Y') = (0, 0, 0): Y'' = 6*0 + 0 = 0."""
        state = np.array([0.0, 0.0])
        rhs = standard_pi_rhs(0.0, state)
        assert rhs[0] == 0.0
        assert rhs[1] == 0.0

    def test_rhs_at_simple_point(self):
        """(X, Y, Y') = (1, 2, 3): Y'' = 6*4 + 1 = 25."""
        state = np.array([2.0, 3.0])
        rhs = standard_pi_rhs(1.0, state)
        assert rhs[0] == 3.0
        assert rhs[1] == 25.0

    def test_solver_on_trivial_ivp(self):
        """Y(0) = Y'(0) = 0: solution near 0 should stay small."""
        result = solve_standard_pi(0.0, 0.1, 0.0, 0.0, max_step=0.001)
        # Y(X) ~ X^3/6 near X=0 for zero IC (leading term from Y'' = X)
        assert abs(result['final_Y']) < 0.01
        assert not result['reached_pole']

    def test_solver_detects_pole_from_large_ic(self):
        """Large positive initial data should blow up."""
        result = solve_standard_pi(0.0, 2.0, 10.0, 0.0, max_step=0.001,
                                   blow_up_threshold=1e6)
        # With Y(0)=10, Y'(0)=0, Y'' = 600 > 0 so Y grows; should hit pole
        assert result['reached_pole']


class TestTritronqueeConstants:
    def test_initial_data_signs(self):
        """Y(0) is negative (on Boutroux negative branch), Y'(0) is POSITIVE
        (the tritronquee is increasing through X=0 as it moves from the
        negative-branch asymptotic toward the positive-real-axis pole)."""
        Y0, Y0p = tritronquee_initial_data()
        assert Y0 < 0
        assert Y0p > 0
        assert abs(Y0 - Y_TRITRONQUEE_AT_ZERO) < 1e-10
        assert abs(Y0p - YPRIME_TRITRONQUEE_AT_ZERO) < 1e-10

    def test_shooting_recovers_initial_data(self):
        """Cross-verify Y(0), Y'(0) by shooting from x_far = -100 inward.
        At L=100 the Boutroux correction 1/(48 L^2) ~ 2e-6, so we expect
        agreement to ~1e-4 in both Y(0) and Y'(0).
        """
        result = verify_tritronquee_initial_data_by_shooting(x_far=-100.0)
        assert result['Y_diff'] < 1e-3, f"Y(0) shooting diff = {result['Y_diff']}"
        assert result['Yp_diff'] < 1e-3, f"Y'(0) shooting diff = {result['Yp_diff']}"

    def test_first_pole_by_numerical_integration(self):
        """Numerically confirm the first pole location ~ +2.378 on POSITIVE
        real axis.

        Note: pole detection fires when |y| exceeds the blow-up threshold,
        which is slightly BEFORE the actual singularity.  Expect agreement
        within ~0.01 (not tighter, because the singular approach is
        extremely steep and the event trigger must fire below infinity).
        """
        result = verify_first_pole_by_integration()
        assert result['reached_pole']
        # Pole location within 0.01 of published value (event fires slightly
        # before the actual singularity as |y| crosses 1e8).
        assert result['difference'] < 0.01, f"Pole diff = {result['difference']}"
        assert result['pole_location_numerical'] > 0, "Pole must be positive"


# ============================================================================
# Section 4: kappa-Tritronquee (Task 1 + Task 2)
# ============================================================================

class TestKappaTritronquee:
    def test_initial_data_kappa_1_matches_standard(self):
        """At kappa=1, kappa-tritronquee IC = standard IC."""
        Y0, Y0p = tritronquee_initial_data()
        y0, y0p = kappa_tritronquee_initial_data(1.0)
        assert abs(y0 - Y0) < 1e-12
        assert abs(y0p - Y0p) < 1e-12

    def test_initial_data_scales_correctly(self):
        """y(0) = kappa^(3/5) Y(0), y'(0) = kappa^(2/5) Y'(0)."""
        Y0, Y0p = tritronquee_initial_data()
        for kappa in [1.0, 13.0, 24.0, 0.5]:
            y0, y0p = kappa_tritronquee_initial_data(kappa)
            assert abs(y0 - kappa ** 0.6 * Y0) < 1e-12
            assert abs(y0p - kappa ** 0.4 * Y0p) < 1e-12

    def test_first_pole_kappa_1(self):
        """kappa=1: first pole at the standard positive value."""
        x_pole = kappa_tritronquee_first_pole(1.0)
        assert abs(x_pole - X_TRITRONQUEE_FIRST_POLE_POS_REAL) < 1e-12

    def test_first_pole_scales_kappa_one_fifth(self):
        """First pole of kappa-tritronquee = kappa^(1/5) * standard, positive."""
        for kappa in [1.0, 13.0, 24.0, 0.5, 100.0]:
            x_pole = kappa_tritronquee_first_pole(kappa)
            expected = kappa ** 0.2 * X_TRITRONQUEE_FIRST_POLE_POS_REAL
            assert abs(x_pole - expected) < 1e-12
            assert x_pole > 0  # always on positive real axis

    def test_first_pole_kappa_13(self):
        """Explicit value at kappa=13.  13^(1/5) ~ 1.670."""
        x_pole = kappa_tritronquee_first_pole(13.0)
        expected = 13.0 ** 0.2 * X_TRITRONQUEE_FIRST_POLE_POS_REAL
        assert abs(x_pole - expected) < 1e-10
        assert x_pole > 0
        # Approximate magnitude: 1.670 * 2.378 ~ 3.97
        assert 3.9 < x_pole < 4.0

    def test_first_pole_kappa_24(self):
        """Explicit value at kappa=24.  24^(1/5) ~ 1.888."""
        x_pole = kappa_tritronquee_first_pole(24.0)
        expected = 24.0 ** 0.2 * X_TRITRONQUEE_FIRST_POLE_POS_REAL
        assert abs(x_pole - expected) < 1e-10
        # Sanity: 24^(1/5) ~ 1.888
        assert 1.88 < 24 ** 0.2 < 1.89
        # Approximate magnitude: 1.888 * 2.378 ~ 4.49
        assert 4.4 < x_pole < 4.6

    def test_asymptotic_at_x_negative(self):
        """y_eq(x << 0) = -sqrt(-kappa x / 6) (Boutroux negative branch)."""
        for kappa in [1.0, 13.0, 24.0]:
            x = -6.0
            y_eq = kappa_tritronquee_asymptotic(x, kappa)
            expected = -math.sqrt(-kappa * x / 6.0)
            assert abs(y_eq - expected) < 1e-12
            assert y_eq < 0  # negative branch

    def test_asymptotic_is_nan_for_x_positive(self):
        """Boutroux asymptotic only valid for x << 0."""
        for kappa in [1.0, 13.0, 24.0]:
            y_eq = kappa_tritronquee_asymptotic(1.0, kappa)
            assert math.isnan(y_eq)

    def test_integrate_tritronquee_stays_finite_in_pole_free_sector(self):
        """Integrating kappa=1 tritronquee from 0 to -10 (along the entire
        negative real axis, which is the Boutroux pole-free direction)
        should stay finite."""
        result = integrate_kappa_tritronquee(1.0, x_start=0.0, x_end=-10.0)
        assert not result['reached_pole']


# ============================================================================
# Section 5: Cross-verification of kappa-P_I via rescaling (core theorem)
# ============================================================================

class TestCrossVerificationRescaling:
    """These are the highest-value tests: they verify that two independent
    numerical integrations (direct kappa-P_I vs. standard P_I + rescaling)
    agree, which is equivalent to verifying the rescaling theorem numerically.
    """

    def test_kappa_1_direct_vs_rescaled_at_x_neg_1(self):
        res = cross_verify_kappa_pi_via_rescaling(1.0, x_eval=-1.0)
        assert res['relative_error'] < 1e-8

    def test_kappa_13_direct_vs_rescaled_at_x_neg_1(self):
        res = cross_verify_kappa_pi_via_rescaling(13.0, x_eval=-1.0)
        assert res['relative_error'] < 1e-6

    def test_kappa_24_direct_vs_rescaled_at_x_neg_1(self):
        res = cross_verify_kappa_pi_via_rescaling(24.0, x_eval=-1.0)
        assert res['relative_error'] < 1e-6

    def test_kappa_half_direct_vs_rescaled_at_x_neg_half(self):
        """Non-standard kappa to exclude hardcoded-value bugs (AP10)."""
        res = cross_verify_kappa_pi_via_rescaling(0.5, x_eval=-0.5)
        assert res['relative_error'] < 1e-6


# ============================================================================
# Section 6: Stokes multipliers (Task 3)
# ============================================================================

class TestStokesMultipliers:
    def test_tritronquee_has_s2_equals_zero(self):
        """Kapaev: tritronquee is characterized by s_2 = 0 (no recessive
        contribution in the central sector)."""
        assert KAPAEV_TRITRONQUEE_STOKES['s_2'] == 0.0

    def test_kappa_invariance_of_stokes_multipliers(self):
        """Rescaling theorem + Stokes invariance: multipliers are kappa-independent."""
        s1 = kappa_stokes_multipliers(1.0)
        s13 = kappa_stokes_multipliers(13.0)
        s24 = kappa_stokes_multipliers(24.0)
        for k in ['s_0', 's_1', 's_2', 's_3', 's_4']:
            assert s1[k] == s13[k] == s24[k]

    def test_stokes_multipliers_match_kapaev(self):
        """Cross-check: our table matches the KAPAEV_TRITRONQUEE_STOKES."""
        s = kappa_stokes_multipliers(1.0)
        for k, v in KAPAEV_TRITRONQUEE_STOKES.items():
            assert s[k] == v

    def test_stokes_raises_for_nonpositive_kappa(self):
        """Negative or zero kappa: rescaling invalid."""
        with pytest.raises(ValueError):
            kappa_stokes_multipliers(0.0)
        with pytest.raises(ValueError):
            kappa_stokes_multipliers(-1.0)


class TestWKBAction:
    def test_wkb_action_kappa_1(self):
        """S(X) = (4 sqrt(2)/15) (-X)^(5/2) for standard P_I."""
        X = -1.0
        S = kappa_wkb_action_along_Boutroux(X, 1.0)
        expected = ALPHA_BOUTROUX * 1.0 ** 2.5
        assert abs(S - expected) < 1e-12

    def test_wkb_action_scales_kappa_neg_half(self):
        """S_kappa(x) = kappa^(-1/2) * S_1(x)."""
        x = -2.0
        S1 = kappa_wkb_action_along_Boutroux(x, 1.0)
        for kappa in [4.0, 13.0, 24.0, 100.0]:
            Sk = kappa_wkb_action_along_Boutroux(x, kappa)
            expected = S1 * kappa ** (-0.5)
            assert abs(Sk - expected) < 1e-12, f"kappa={kappa}"

    def test_wkb_action_positive_for_x_negative(self):
        for kappa in [1.0, 13.0, 24.0]:
            assert kappa_wkb_action_along_Boutroux(-5.0, kappa) > 0

    def test_wkb_action_nan_for_x_positive(self):
        assert math.isnan(kappa_wkb_action_along_Boutroux(1.0, 13.0))

    def test_trans_series_decays(self):
        """First exponential correction decays as |x| -> infinity."""
        kappa = 13.0
        prev = 1e100
        for x in [-1.0, -2.0, -5.0, -10.0]:
            t = trans_series_first_correction(x, kappa, stokes_constant=1.0)
            assert t > 0
            assert t < prev  # monotone decrease
            prev = t


# ============================================================================
# Section 7: Dispersionless limit (Task 4)
# ============================================================================

class TestDispersionlessLimit:
    def test_riccati_limit_matches_boutroux_asymptotic(self):
        """The dispersionless limit equals the Boutroux equilibrium."""
        for kappa in [1.0, 13.0, 24.0]:
            for x in [-1.0, -10.0, -100.0]:
                assert abs(
                    dispersionless_limit_riccati(x, kappa)
                    - kappa_tritronquee_asymptotic(x, kappa)
                ) < 1e-12

    def test_riccati_limit_scales_sqrt_kappa(self):
        """|y_disp(x, kappa)| / |y_disp(x, 1)| = sqrt(kappa).

        Both values are negative (Boutroux branch), so the ratio is positive.
        """
        x = -1.0
        y1 = dispersionless_limit_riccati(x, 1.0)
        assert y1 < 0  # negative branch
        for kappa in [4.0, 13.0, 24.0]:
            yk = dispersionless_limit_riccati(x, kappa)
            assert yk < 0  # negative branch
            assert abs(yk / y1 - math.sqrt(kappa)) < 1e-12

    def test_first_integral_is_conserved_on_autonomous_solutions(self):
        """At x = 0 (autonomous), E = (1/2) y'^2 - (2/kappa) y^3 is conserved.
        Integrate the autonomous ODE y'' = (6/kappa) y^2 starting from small IC
        and check E stays constant."""
        kappa = 13.0

        def rhs(t, state):
            y, yp = state
            return [yp, (6.0 / kappa) * y * y]

        from scipy.integrate import solve_ivp
        y0, y0p = 0.5, 0.1
        E0 = true_riccati_first_integral(0.0, y0, y0p, kappa)
        sol = solve_ivp(rhs, (0.0, 0.5), [y0, y0p], method='DOP853',
                        rtol=1e-12, atol=1e-14, max_step=0.01)
        E_final = true_riccati_first_integral(0.0, sol.y[0][-1], sol.y[1][-1], kappa)
        # Conservation: |E_final - E0| should be tiny
        assert abs(E_final - E0) < 1e-9

    def test_large_kappa_convergence(self):
        """At fixed x in the Boutroux regime, kappa -> infinity: the ratio
        y_asym / y_disp is identically 1 (they're the same function)."""
        res = verify_dispersionless_at_large_kappa(x=-10.0, kappa_max=1000.0)
        for r in res['ratios']:
            assert abs(r - 1.0) < 1e-12, f"Ratio = {r}"


# ============================================================================
# Section 8: Fredholm / Tracy-Widom relation (Task 5)
# ============================================================================

class TestFredholmKernel:
    def test_airy_kernel_symmetric(self):
        """K_Ai(x, y; s) is symmetric in x, y."""
        assert abs(airy_kernel(0.5, 1.2, 0.0) - airy_kernel(1.2, 0.5, 0.0)) < 1e-10

    def test_airy_kernel_diagonal(self):
        """Diagonal value: K(x,x;0) = Ai'(x)^2 - x Ai(x)^2."""
        from scipy.special import airy
        x = 0.7
        Ai_x, Aip_x, _, _ = airy(x)
        expected = Aip_x ** 2 - x * Ai_x ** 2
        assert abs(airy_kernel(x, x, 0.0) - expected) < 1e-10

    def test_kernel_structure_reports_pi_not_tracy_widom(self):
        """P_I does NOT have Tracy-Widom Fredholm form (AP42)."""
        info = pi_kernel_structure()
        assert info['painleve_type'] == 'P_I'
        assert 'NOT' in info['fredholm_status']
        assert 'P_II' in info['tracy_widom_relation']

    def test_tau_pi_log_det_relation_kappa_power(self):
        """log tau_kappa = kappa * log tau_std: matches shadow-KW identity."""
        for kappa in [1.0, 13.0, 24.0]:
            rel = tau_pi_minus_log_det_relation(-1.0, kappa)
            assert rel['kappa_power'] == kappa
            assert rel['matches_shadow_KW'] is True

    def test_tau_pi_kappa_1_reduces_to_standard(self):
        rel = tau_pi_minus_log_det_relation(-1.0, 1.0)
        assert rel['kappa_power'] == 1.0
        assert abs(rel['X']) == 1.0  # no rescaling at kappa=1


# ============================================================================
# Section 9: Isomonodromic check (Task 6)
# ============================================================================

class TestIsomonodromic:
    def test_standard_pi_is_isomonodromic(self):
        assert isomonodromic_check_kappa(1.0)['isomonodromic']

    def test_kappa_13_is_isomonodromic(self):
        info = isomonodromic_check_kappa(13.0)
        assert info['isomonodromic']
        assert info['stokes_data_kappa_dependent'] is False

    def test_kappa_24_is_isomonodromic(self):
        info = isomonodromic_check_kappa(24.0)
        assert info['isomonodromic']
        assert info['stokes_data_kappa_dependent'] is False

    def test_wkb_action_is_kappa_dependent(self):
        """Structural: S(x) is kappa-dependent (kappa^(-1/2)) even though the
        Stokes data are not.  This matches the trans-series / instanton
        interpretation."""
        for kappa in [1.0, 13.0, 24.0]:
            info = isomonodromic_check_kappa(kappa)
            assert info['wkb_action_kappa_dependent'] is True


# ============================================================================
# Section 10: Random matrix / beta-ensemble identification (Task 7)
# ============================================================================

class TestBetaEnsembleIdentification:
    def test_kappa_1_identifies_with_GUE(self):
        """kappa = 1 = GUE (beta = 2) = Witten-Kontsevich."""
        res = beta_ensemble_identification(1.0)
        assert res['standard_beta_match'] == 'GUE_beta_2'
        assert res['is_standard_dyson']

    def test_kappa_half_identifies_with_GOE(self):
        res = beta_ensemble_identification(0.5)
        assert res['standard_beta_match'] == 'GOE_beta_1'

    def test_kappa_2_identifies_with_GSE(self):
        res = beta_ensemble_identification(2.0)
        assert res['standard_beta_match'] == 'GSE_beta_4'

    def test_kappa_13_NOT_standard_ensemble(self):
        """No standard ensemble has beta = 13."""
        res = beta_ensemble_identification(13.0)
        assert res['standard_beta_match'] is None
        assert not res['is_standard_dyson']

    def test_kappa_24_NOT_standard_ensemble(self):
        res = beta_ensemble_identification(24.0)
        assert res['standard_beta_match'] is None

    def test_matrix_model_minimal_model_is_23(self):
        """P_I corresponds to the (2,3) minimal model = pure 2D gravity."""
        for kappa in [1.0, 13.0, 24.0]:
            res = pi_matrix_model_correspondence(kappa)
            assert '(2,3)' in res['minimal_model']

    def test_matrix_model_string_coupling_scales_kappa_neg_half(self):
        """g_s_eff = g_s / sqrt(kappa)."""
        res = pi_matrix_model_correspondence(4.0)
        # Should contain factor sqrt(4) = 2
        assert '2.00' in res['string_coupling_scaling']


# ============================================================================
# Section 11: Landscape summary smoke tests
# ============================================================================

class TestLandscapeSummary:
    def test_summary_kappa_1(self):
        s = kappa_pi_summary_for_kappa(1.0)
        assert s['kappa'] == 1.0
        assert s['isomonodromic']
        assert abs(s['first_pole_positive_real'] - X_TRITRONQUEE_FIRST_POLE_POS_REAL) < 1e-10

    def test_summary_kappa_13(self):
        s = kappa_pi_summary_for_kappa(13.0)
        assert s['kappa'] == 13.0
        assert s['first_pole_positive_real'] > 0  # positive real axis
        # Stokes data are kappa-independent
        assert s['stokes_multipliers'] == KAPAEV_TRITRONQUEE_STOKES

    def test_summary_kappa_24(self):
        s = kappa_pi_summary_for_kappa(24.0)
        assert s['kappa'] == 24.0
        assert s['beta_match'] is None

    def test_landscape_summary_keys(self):
        summary = landscape_summary()
        assert 'kappa_1_standard_PI' in summary
        assert 'kappa_13_AP24_sum' in summary
        assert 'kappa_24_Niemeier_Monster' in summary


# ============================================================================
# Section 12: Universal constants (multi-path)
# ============================================================================

class TestUniversalConstants:
    def test_alpha_boutroux_value(self):
        """ALPHA_BOUTROUX = 4 sqrt(2) / 15 ~ 0.37712."""
        assert abs(ALPHA_BOUTROUX - 4.0 * math.sqrt(2.0) / 15.0) < 1e-15
        assert abs(ALPHA_BOUTROUX - 0.37712361663282534) < 1e-12

    def test_sector_halfwidth_is_4pi_over_5(self):
        assert abs(SECTOR_HALFWIDTH - 4.0 * math.pi / 5.0) < 1e-15

    def test_tritronquee_constants_signs(self):
        """Y(0) < 0 (Boutroux negative branch), Y'(0) > 0 (increasing toward
        the positive-real-axis pole)."""
        assert Y_TRITRONQUEE_AT_ZERO < 0
        assert YPRIME_TRITRONQUEE_AT_ZERO > 0

    def test_first_pole_magnitude(self):
        """First pole on POSITIVE real axis has |x| ~ 2.378."""
        assert 2.3 < X_TRITRONQUEE_FIRST_POLE_POS_REAL < 2.4
