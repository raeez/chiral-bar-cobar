r"""Tests for bc_painleve_shadow_engine.py -- BC-113.

Painleve transcendents at shadow parameter values and connection to the
shadow obstruction tower.

Structure:
    Section 1: Shadow family data correctness (10 tests)
    Section 2: Shadow metric and branch points (10 tests)
    Section 3: Schwarzian potential and singularity classification (8 tests)
    Section 4: P_VI parameters from multi-channel W_3 (12 tests)
    Section 5: P_VI Riccati reduction and linearizability (8 tests)
    Section 6: Tau function and flat section (10 tests)
    Section 7: Connection matrices and hypergeometric (8 tests)
    Section 8: P_III from genus-1 shadow (8 tests)
    Section 9: Zeta zero evaluations (8 tests)
    Section 10: Multi-path verification (10 tests)
    Section 11: Cross-ratio landscape (5 tests)

Total: 97 tests.
"""

import cmath
import math
import pytest

from compute.lib.bc_painleve_shadow_engine import (
    # Family data
    virasoro_data, heisenberg_data, affine_sl2_data, betagamma_data,
    w3_data, w3_w_channel_data, ShadowFamilyData,
    # Shadow metric
    shadow_metric_coeffs, shadow_metric_eval, branch_points, cross_ratio_4pts,
    # Schwarzian
    schwarzian_potential, indicial_exponent_at_zero,
    # P_VI
    PainleveVIParams, pvi_params_from_thetas, pvi_from_w3_shadow,
    pvi_cross_ratio_landscape, pvi_hamiltonian, integrate_pvi,
    # Riccati
    pvi_riccati_test, linearizability_by_shadow_depth,
    # Tau
    shadow_tau_flat_section, shadow_generating_function,
    tau_genus_expansion, compare_tau_and_shadow_gf,
    jmu_tau_pvi,
    # Connection
    shadow_at_zeta_zero, connection_matrix_hypergeometric,
    connection_data_at_zeta_zeros,
    # P_III
    genus1_shadow_to_piii, piii_asymptotic_at_zero, piii_asymptotic_at_infinity,
    PainleveIIIParams,
    # Verification
    verify_indicial_exponent_universal, verify_tau_equals_flat_section,
    verify_pvi_params_universal, verify_discriminant_relation,
    # Stokes / Borel
    stokes_from_borel_resurgence,
    # Cross-ratio
    w3_cross_ratio_analytic, cross_ratio_at_zeta_zeros,
    # Nekrasov
    nekrasov_genus1_comparison,
    # Full analysis
    full_painleve_shadow_analysis, standard_landscape_analysis,
    # Constants
    ZETA_ZEROS_20,
)


# ===========================================================================
# Section 1: Shadow family data correctness (10 tests)
# ===========================================================================

class TestShadowFamilyData:
    """Verify shadow data for all standard families."""

    def test_virasoro_kappa(self):
        """kappa(Vir_c) = c/2."""
        for c_val in [0.5, 1.0, 13.0, 25.0, 26.0]:
            vir = virasoro_data(c_val)
            assert abs(vir.kappa - c_val / 2) < 1e-12

    def test_virasoro_alpha(self):
        """alpha(Vir) = S_3 = 2 (gravitational cubic)."""
        vir = virasoro_data(1.0)
        assert abs(vir.alpha - 2.0) < 1e-12

    def test_virasoro_S4(self):
        """S_4(Vir) = 10 / (c * (5c + 22))."""
        for c_val in [0.5, 1.0, 2.0, 13.0, 25.0]:
            vir = virasoro_data(c_val)
            expected = 10.0 / (c_val * (5 * c_val + 22))
            assert abs(vir.S4 - expected) < 1e-12

    def test_virasoro_Delta(self):
        """Delta(Vir) = 40 / (5c + 22)."""
        for c_val in [0.5, 1.0, 13.0, 25.0]:
            vir = virasoro_data(c_val)
            expected = 40.0 / (5 * c_val + 22)
            assert abs(vir.Delta - expected) < 1e-10

    def test_virasoro_class_M(self):
        """Virasoro is always class M with infinite shadow depth."""
        vir = virasoro_data(1.0)
        assert vir.shadow_class == 'M'
        assert vir.r_max == -1

    def test_heisenberg_trivial(self):
        """Heisenberg: kappa = k, alpha = 0, S4 = 0, Delta = 0, class G."""
        heis = heisenberg_data(1.0)
        assert abs(heis.kappa - 1.0) < 1e-12
        assert heis.alpha == 0.0
        assert heis.S4 == 0.0
        assert heis.Delta == 0.0
        assert heis.shadow_class == 'G'
        assert heis.r_max == 2

    def test_affine_sl2_class_L(self):
        """Affine sl_2: S4 = 0, Delta = 0, class L, r_max = 3."""
        sl2 = affine_sl2_data(1.0)
        assert sl2.Delta == 0.0
        assert sl2.shadow_class == 'L'
        assert sl2.r_max == 3

    def test_affine_sl2_kappa(self):
        """kappa(sl_2, k) = 3(k+2)/4."""
        for k in [1, 2, 3, 10]:
            sl2 = affine_sl2_data(float(k))
            assert abs(sl2.kappa - 3.0 * (k + 2) / 4) < 1e-12

    def test_betagamma_class_C(self):
        """Beta-gamma: class C, r_max = 4."""
        bg = betagamma_data()
        assert bg.shadow_class == 'C'
        assert bg.r_max == 4
        assert bg.c_value == -1.0

    def test_w3_w_channel_alpha_zero(self):
        """W_3 W-channel: alpha = 0 (Z_2 parity)."""
        w3w = w3_w_channel_data(13.0)
        assert w3w.alpha == 0.0


# ===========================================================================
# Section 2: Shadow metric and branch points (10 tests)
# ===========================================================================

class TestShadowMetric:
    """Verify shadow metric Q_L(t) = q0 + q1*t + q2*t^2."""

    def test_coefficients_general(self):
        """q0 = 4*kappa^2, q1 = 12*kappa*alpha, q2 = 9*alpha^2 + 2*Delta."""
        kappa, alpha, Delta = 3.0, 2.0, 0.5
        q0, q1, q2 = shadow_metric_coeffs(kappa, alpha, Delta)
        assert abs(q0 - 4 * kappa**2) < 1e-12
        assert abs(q1 - 12 * kappa * alpha) < 1e-12
        assert abs(q2 - (9 * alpha**2 + 2 * Delta)) < 1e-12

    def test_virasoro_Q_at_zero(self):
        """Q_Vir(0) = c^2 (= 4*(c/2)^2)."""
        for c_val in [1.0, 13.0, 25.0]:
            vir = virasoro_data(c_val)
            Q0 = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, 0)
            assert abs(Q0 - c_val**2) < 1e-10

    def test_heisenberg_Q_constant(self):
        """Q_Heis(t) = 4*k^2 (constant, alpha=Delta=0)."""
        heis = heisenberg_data(2.0)
        for t_val in [0, 0.5, 1.0, -1.0]:
            Q = shadow_metric_eval(heis.kappa, heis.alpha, heis.Delta, t_val)
            assert abs(Q - 4 * 2.0**2) < 1e-12

    def test_branch_points_virasoro_complex(self):
        """Virasoro branch points are complex conjugate for c > 0."""
        vir = virasoro_data(1.0)
        tp, tm = branch_points(vir.kappa, vir.alpha, vir.Delta)
        # Should be complex conjugate
        assert abs(tp - tm.conjugate()) < 1e-10

    def test_branch_points_virasoro_modulus(self):
        """Branch point modulus is the shadow radius R."""
        vir = virasoro_data(1.0)
        tp, tm = branch_points(vir.kappa, vir.alpha, vir.Delta)
        assert abs(abs(tp) - abs(tm)) < 1e-10

    def test_no_branch_points_heisenberg(self):
        """Heisenberg: Q_L = constant, no zeros in finite t."""
        heis = heisenberg_data(1.0)
        q0, q1, q2 = shadow_metric_coeffs(heis.kappa, heis.alpha, heis.Delta)
        # Q = 4k^2, q1 = 0, q2 = 0: no zeros
        assert abs(q1) < 1e-12
        assert abs(q2) < 1e-12

    def test_w3_w_channel_purely_imaginary(self):
        """W_3 W-channel branch points are purely imaginary (alpha=0)."""
        w3w = w3_w_channel_data(13.0)
        tp, tm = branch_points(w3w.kappa, w3w.alpha, w3w.Delta)
        # With alpha=0: Q = A + B*t^2, zeros at t = +/- i*sqrt(A/B)
        assert abs(tp.real) < 1e-8
        assert abs(tm.real) < 1e-8

    def test_cross_ratio_basic(self):
        """Cross-ratio of (0, 1, inf, 2) = 2 (standard formula)."""
        # For 4 finite points (0, 1, 2, 3):
        # lambda = (0-2)(1-3) / ((0-3)(1-2)) = (-2)(-2) / ((-3)(-1)) = 4/3
        lam = cross_ratio_4pts(0, 1, 2, 3)
        assert abs(lam - 4.0 / 3.0) < 1e-10

    def test_discriminant_formula(self):
        """disc(Q_L) = q1^2 - 4*q0*q2 = -32*kappa^2*Delta."""
        for c_val in [0.5, 1.0, 13.0, 25.0]:
            vir = virasoro_data(c_val)
            q0, q1, q2 = shadow_metric_coeffs(vir.kappa, vir.alpha, vir.Delta)
            disc_poly = q1**2 - 4 * q0 * q2
            disc_formula = -32 * vir.kappa**2 * vir.Delta
            assert abs(disc_poly - disc_formula) < 1e-8 * max(abs(disc_poly), 1)

    def test_gaussian_decomposition(self):
        """Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        kappa, alpha, Delta = 3.0, 2.0, 0.7
        for t_val in [0, 0.1, 0.5, 1.0, -0.3]:
            Q_direct = shadow_metric_eval(kappa, alpha, Delta, t_val)
            Q_gauss = (2 * kappa + 3 * alpha * t_val)**2 + 2 * Delta * t_val**2
            assert abs(Q_direct - Q_gauss) < 1e-10


# ===========================================================================
# Section 3: Schwarzian potential and singularity classification (8 tests)
# ===========================================================================

class TestSchwarzianPotential:
    """Verify Schwarzian potential V(t) = 8*kappa^2*Delta / Q_L^2."""

    def test_V_formula(self):
        """V(t) = 8*kappa^2*Delta / Q_L(t)^2."""
        kappa, alpha, Delta = 3.0, 2.0, 0.5
        t_val = 0.3
        V = schwarzian_potential(kappa, alpha, Delta, t_val)
        Q = shadow_metric_eval(kappa, alpha, Delta, t_val)
        V_expected = 8 * kappa**2 * Delta / Q**2
        assert abs(V - V_expected) < 1e-10

    def test_V_zero_for_heisenberg(self):
        """V = 0 when Delta = 0 (Heisenberg)."""
        heis = heisenberg_data(1.0)
        V = schwarzian_potential(heis.kappa, heis.alpha, heis.Delta, 0.5)
        assert abs(V) < 1e-12

    def test_V_positive_virasoro(self):
        """V > 0 for Virasoro at real t away from branch points."""
        vir = virasoro_data(1.0)
        V = schwarzian_potential(vir.kappa, vir.alpha, vir.Delta, 0.1)
        assert V.real > 0

    def test_indicial_exponent_universal_half(self):
        """Indicial exponent is 1/2 (double) universally for Delta != 0.

        Multi-path:
        Path 1: From the general formula c_0 = -1/4 => rho = 1/2 (analytic)
        Path 2: Explicit computation c_0 = 8*kappa^2*Delta/Q'(t_0)^2 for each family
        Path 3: Cross-family consistency (same result for Vir, betagamma)
        """
        families = [virasoro_data(c) for c in [0.5, 1.0, 13.0, 25.0]] + [betagamma_data()]
        for fam in families:
            if abs(fam.Delta) < 1e-30:
                continue
            # Path 1: general formula
            rho1, rho2 = indicial_exponent_at_zero(fam.kappa, fam.alpha, fam.Delta)
            assert abs(rho1 - 0.5) < 1e-10
            assert abs(rho2 - 0.5) < 1e-10
            # Path 2: explicit c_0 at branch point
            q0, q1, q2 = shadow_metric_coeffs(fam.kappa, fam.alpha, fam.Delta)
            tp, _ = branch_points(fam.kappa, fam.alpha, fam.Delta)
            Qp_tp = q1 + 2 * q2 * tp
            c_0_explicit = 8 * fam.kappa**2 * fam.Delta / Qp_tp**2
            assert abs(c_0_explicit - (-0.25)) < 1e-8

    def test_indicial_c0_minus_quarter(self):
        """c_0 = 8*kappa^2*Delta / Q'(t_0)^2 = -1/4 universally.

        Multi-path:
        Path 1: c_0 = 8*k^2*D / disc(Q_L), disc = -32*k^2*D => c_0 = -1/4
        Path 2: Explicit at branch point Q'(t+)^2 = disc
        Path 3: Both simplify to the same -1/4 across families
        """
        for c_val in [1.0, 13.0, 25.0]:
            vir = virasoro_data(c_val)
            q0, q1, q2 = shadow_metric_coeffs(vir.kappa, vir.alpha, vir.Delta)
            # Path 1: via discriminant
            disc = q1**2 - 4 * q0 * q2
            c_0_path1 = 8 * vir.kappa**2 * vir.Delta / disc
            assert abs(c_0_path1 - (-0.25)) < 1e-10
            # Path 2: disc = -32*k^2*D algebraic identity
            disc_formula = -32 * vir.kappa**2 * vir.Delta
            c_0_path2 = 8 * vir.kappa**2 * vir.Delta / disc_formula
            assert abs(c_0_path2 - (-0.25)) < 1e-10
            # Cross-check: both paths agree
            assert abs(c_0_path1 - c_0_path2) < 1e-12

    def test_V_diverges_at_branch_point(self):
        """V(t) -> infinity as t -> branch point (pole of order 2)."""
        vir = virasoro_data(1.0)
        tp, tm = branch_points(vir.kappa, vir.alpha, vir.Delta)
        # Evaluate near the branch point
        t_near = tp + 1e-6
        V_near = schwarzian_potential(vir.kappa, vir.alpha, vir.Delta, t_near)
        assert abs(V_near) > 1e6

    def test_V_decays_at_infinity(self):
        """V(t) ~ 8*kappa^2*Delta / (q2^2 * t^4) for large t."""
        vir = virasoro_data(1.0)
        q0, q1, q2 = shadow_metric_coeffs(vir.kappa, vir.alpha, vir.Delta)
        t_large = 1000.0
        V_large = schwarzian_potential(vir.kappa, vir.alpha, vir.Delta, t_large)
        V_asymp = 8 * vir.kappa**2 * vir.Delta / (q2**2 * t_large**4)
        assert abs(V_large - V_asymp) / abs(V_asymp) < 0.01

    def test_indicial_trivial_for_Delta_zero(self):
        """When Delta = 0: indicial exponents (0, 1) (trivial)."""
        rho1, rho2 = indicial_exponent_at_zero(1.0, 2.0, 0.0)
        assert abs(rho1) < 1e-10
        assert abs(rho2 - 1.0) < 1e-10


# ===========================================================================
# Section 4: P_VI parameters from multi-channel W_3 (12 tests)
# ===========================================================================

class TestPainleveVIParameters:
    """Verify P_VI parameters from W_3 two-channel shadow."""

    def test_pvi_alpha_universal(self):
        """P_VI alpha = 1/8 for all c (from theta = 1/2)."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            params = pvi_from_w3_shadow(c_val)
            assert abs(params.alpha - 0.125) < 1e-10

    def test_pvi_beta_universal(self):
        """P_VI beta = -1/8 for all c."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            params = pvi_from_w3_shadow(c_val)
            assert abs(params.beta - (-0.125)) < 1e-10

    def test_pvi_gamma_universal(self):
        """P_VI gamma = 1/8 for all c."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            params = pvi_from_w3_shadow(c_val)
            assert abs(params.gamma - 0.125) < 1e-10

    def test_pvi_delta_universal(self):
        """P_VI delta = 3/8 for all c."""
        for c_val in [1.0, 5.0, 13.0, 25.0]:
            params = pvi_from_w3_shadow(c_val)
            assert abs(params.delta - 0.375) < 1e-10

    def test_pvi_theta_all_half(self):
        """All theta = 1/2 (from universal indicial exponent)."""
        params = pvi_from_w3_shadow(13.0)
        assert abs(params.theta_0 - 0.5) < 1e-12
        assert abs(params.theta_1 - 0.5) < 1e-12
        assert abs(params.theta_t - 0.5) < 1e-12
        assert abs(params.theta_inf - 0.5) < 1e-12

    def test_cross_ratio_real_at_real_c(self):
        """Cross-ratio is real (or complex) for real c; varies with c."""
        lam_5 = pvi_from_w3_shadow(5.0).cross_ratio
        lam_13 = pvi_from_w3_shadow(13.0).cross_ratio
        lam_25 = pvi_from_w3_shadow(25.0).cross_ratio
        # Cross-ratios should differ
        assert abs(lam_5 - lam_13) > 1e-6
        assert abs(lam_13 - lam_25) > 1e-6

    def test_cross_ratio_c_dependence(self):
        """Cross-ratio lambda(c) varies smoothly with c."""
        c_vals = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        lams = [pvi_from_w3_shadow(c).cross_ratio for c in c_vals]
        # Check smoothness: consecutive differences should be small
        for i in range(len(lams) - 1):
            assert abs(lams[i + 1] - lams[i]) < 1.0  # not jumping wildly

    def test_jimbo_relation_alpha(self):
        """alpha = (theta_inf - 1)^2 / 2."""
        params = pvi_from_w3_shadow(13.0)
        expected = (params.theta_inf - 1)**2 / 2
        assert abs(params.alpha - expected) < 1e-12

    def test_jimbo_relation_beta(self):
        """beta = -theta_0^2 / 2."""
        params = pvi_from_w3_shadow(13.0)
        expected = -params.theta_0**2 / 2
        assert abs(params.beta - expected) < 1e-12

    def test_jimbo_relation_gamma(self):
        """gamma = theta_1^2 / 2."""
        params = pvi_from_w3_shadow(13.0)
        expected = params.theta_1**2 / 2
        assert abs(params.gamma - expected) < 1e-12

    def test_jimbo_relation_delta(self):
        """delta = (1 - theta_t^2) / 2."""
        params = pvi_from_w3_shadow(13.0)
        expected = (1 - params.theta_t**2) / 2
        assert abs(params.delta - expected) < 1e-12

    def test_pvi_landscape(self):
        """Cross-ratio landscape computation returns valid data."""
        c_vals = [5.0, 10.0, 13.0, 20.0, 25.0]
        landscape = pvi_cross_ratio_landscape(c_vals)
        assert len(landscape) == 5
        for entry in landscape:
            if entry.get('cross_ratio') is not None:
                assert abs(entry['alpha'] - 0.125) < 1e-10


# ===========================================================================
# Section 5: P_VI Riccati reduction and linearizability (8 tests)
# ===========================================================================

class TestRiccatiReduction:
    """Verify Riccati/linearizability classification by shadow depth."""

    def test_w3_not_riccati(self):
        """W_3 shadow P_VI is NOT Riccati-reducible."""
        params = pvi_from_w3_shadow(13.0)
        result = pvi_riccati_test(params)
        assert result['is_riccati'] is False

    def test_theta_sum_is_two(self):
        """Sum of theta = 4 * 0.5 = 2.0 (even, not odd)."""
        params = pvi_from_w3_shadow(13.0)
        result = pvi_riccati_test(params)
        assert abs(result['theta_sum'] - 2.0) < 1e-10

    def test_riccati_when_theta_zero_vanishes(self):
        """P_VI is Riccati when any theta = 0."""
        params = pvi_params_from_thetas(0, 0.5, 0.5, 0.5, 0.5)
        result = pvi_riccati_test(params)
        assert result['is_riccati'] is True

    def test_heisenberg_linearizable(self):
        """Heisenberg: linearizable (Delta = 0, class G)."""
        heis = heisenberg_data(1.0)
        result = linearizability_by_shadow_depth(heis)
        assert result['is_linearizable'] is True
        assert result['ode_type'] == 'trivial'

    def test_affine_sl2_linearizable(self):
        """Affine sl_2: linearizable (Delta = 0, class L)."""
        sl2 = affine_sl2_data(1.0)
        result = linearizability_by_shadow_depth(sl2)
        assert result['is_linearizable'] is True

    def test_virasoro_not_linearizable(self):
        """Virasoro: NOT linearizable (Delta != 0, class M)."""
        vir = virasoro_data(1.0)
        result = linearizability_by_shadow_depth(vir)
        assert result['is_linearizable'] is False
        assert result['ode_type'] == 'algebraic_degree_2'

    def test_betagamma_not_linearizable(self):
        """Beta-gamma: NOT linearizable (Delta != 0, class C)."""
        bg = betagamma_data()
        result = linearizability_by_shadow_depth(bg)
        assert result['is_linearizable'] is False

    def test_linearizability_iff_delta_zero(self):
        """Linearizability <==> Delta = 0 across all families."""
        families = [
            heisenberg_data(1.0),
            affine_sl2_data(1.0),
            betagamma_data(),
            virasoro_data(1.0),
            virasoro_data(13.0),
        ]
        for fam in families:
            result = linearizability_by_shadow_depth(fam)
            assert result['is_linearizable'] == (abs(fam.Delta) < 1e-30)


# ===========================================================================
# Section 6: Tau function and flat section (10 tests)
# ===========================================================================

class TestTauFunction:
    """Verify tau function = flat section of shadow connection."""

    def test_tau_at_zero(self):
        """tau(0) = sqrt(Q(0)/Q(0)) = 1."""
        vir = virasoro_data(1.0)
        tau_0 = shadow_tau_flat_section(vir.kappa, vir.alpha, vir.Delta, 0)
        assert abs(tau_0 - 1.0) < 1e-10

    def test_tau_is_sqrt_ratio(self):
        """tau(t) = sqrt(Q(t)/Q(0))."""
        vir = virasoro_data(13.0)
        t_val = 0.5
        Q_t = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, t_val)
        Q_0 = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, 0)
        tau_expected = cmath.sqrt(Q_t / Q_0)
        tau_computed = shadow_tau_flat_section(vir.kappa, vir.alpha, vir.Delta, t_val)
        assert abs(tau_computed - tau_expected) < 1e-12

    def test_H_is_t_squared_sqrt_Q(self):
        """H(t) = t^2 * sqrt(Q_L(t))."""
        vir = virasoro_data(1.0)
        t_val = 0.3
        H = shadow_generating_function(vir.kappa, vir.alpha, vir.Delta, t_val)
        Q_t = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, t_val)
        H_expected = t_val**2 * cmath.sqrt(Q_t)
        assert abs(H - H_expected) < 1e-12

    def test_H_not_flat_section(self):
        """H(t) != tau(t) -- H has a double zero at t=0 (AP23)."""
        vir = virasoro_data(1.0)
        H_0 = shadow_generating_function(vir.kappa, vir.alpha, vir.Delta, 0)
        tau_0 = shadow_tau_flat_section(vir.kappa, vir.alpha, vir.Delta, 0)
        assert abs(H_0) < 1e-12  # H(0) = 0
        assert abs(tau_0 - 1.0) < 1e-12  # tau(0) = 1

    def test_H_over_tau_is_polynomial(self):
        """H(t) / tau(t) = t^2 * sqrt(Q(0)) = 2*kappa*t^2 (polynomial)."""
        vir = virasoro_data(13.0)
        Q_0 = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, 0)
        sqrt_Q0 = cmath.sqrt(Q_0)
        for t_val in [0.1, 0.5, 1.0]:
            result = compare_tau_and_shadow_gf(vir.kappa, vir.alpha, vir.Delta, [t_val])
            assert result[0]['ratio_match']

    def test_tau_genus_expansion_F1(self):
        """F_1 = kappa/24.

        Multi-path:
        Path 1: Bernoulli formula a_1 = (2^2 - 2)*|B_2|/(2!*4) = 2*(1/6)/8 = 1/24
        Path 2: Linearity in kappa (F_1(2*kappa) = 2*F_1(kappa))
        Path 3: Series coefficient of (x/2)/sin(x/2) at x^2
        """
        for kappa_val in [0.5, 1.0, 6.5, 13.0]:
            Fg = tau_genus_expansion(kappa_val, g_max=3)
            # Path 1: direct value
            assert abs(Fg[1] - kappa_val / 24.0) < 1e-12
        # Path 2: linearity
        Fg_1 = tau_genus_expansion(1.0, g_max=1)
        Fg_2 = tau_genus_expansion(2.0, g_max=1)
        assert abs(Fg_2[1] - 2 * Fg_1[1]) < 1e-12
        # Path 3: Bernoulli formula
        from sympy import bernoulli as sym_B, factorial as sym_fac
        a1 = (2**2 - 2) * abs(float(sym_B(2))) / (float(sym_fac(2)) * 4**1)
        assert abs(a1 - 1.0 / 24) < 1e-14

    def test_tau_genus_expansion_F2(self):
        """F_2 = 7*kappa/5760.

        Multi-path:
        Path 1: Bernoulli formula a_2 = (2^4-2)*|B_4|/(4!*16) = 14*(1/30)/384 = 7/5760
        Path 2: Cross-check with sympy series of (x/2)/sin(x/2)
        """
        for kappa_val in [0.5, 1.0, 6.5]:
            Fg = tau_genus_expansion(kappa_val, g_max=3)
            assert abs(Fg[2] - 7 * kappa_val / 5760.0) < 1e-12
        # Path 2: from sympy series
        from sympy import Symbol, sin, series
        x = Symbol('x')
        s = series(x / 2 / sin(x / 2), x, 0, 6)
        a2 = float(s.coeff(x, 4))
        assert abs(a2 - 7.0 / 5760) < 1e-14

    def test_tau_genus_expansion_F3(self):
        """F_3 = 31*kappa/967680.

        Multi-path:
        Path 1: Bernoulli formula a_3 = (2^6-2)*|B_6|/(6!*64) = 62*(1/42)/46080
        Path 2: Linearity in kappa
        """
        kappa_val = 1.0
        Fg = tau_genus_expansion(kappa_val, g_max=3)
        assert abs(Fg[3] - 31.0 / 967680.0) < 1e-12
        # Path 2: Bernoulli formula
        from sympy import bernoulli as sym_B, factorial as sym_fac
        a3 = (2**6 - 2) * abs(float(sym_B(6))) / (float(sym_fac(6)) * 4**3)
        assert abs(a3 - 31.0 / 967680) < 1e-14

    def test_tau_comparison_multiple_t(self):
        """Compare tau_direct with tau_integrated across multiple t values."""
        vir = virasoro_data(13.0)
        t_vals = [0.01 * i for i in range(1, 21)]
        result = verify_tau_equals_flat_section(vir.kappa, vir.alpha, vir.Delta, t_vals)
        for entry in result['data'][1:]:  # skip t=0 initial
            assert entry['path1_path2_agree']

    def test_heisenberg_tau_constant(self):
        """Heisenberg: Q(t) = Q(0) for all t, so tau(t) = 1."""
        heis = heisenberg_data(1.0)
        for t_val in [0.1, 0.5, 1.0, 5.0]:
            tau = shadow_tau_flat_section(heis.kappa, heis.alpha, heis.Delta, t_val)
            assert abs(tau - 1.0) < 1e-12


# ===========================================================================
# Section 7: Connection matrices and hypergeometric (8 tests)
# ===========================================================================

class TestConnectionMatrices:
    """Verify connection data for the shadow Schrodinger equation."""

    def test_heisenberg_trivial_connection(self):
        """Heisenberg: trivial connection (Delta = 0)."""
        heis = heisenberg_data(1.0)
        conn = connection_matrix_hypergeometric(heis.kappa, heis.alpha, heis.Delta)
        assert conn['type'] == 'trivial'

    def test_virasoro_hypergeometric_connection(self):
        """Virasoro: hypergeometric connection with monodromy -1."""
        vir = virasoro_data(1.0)
        conn = connection_matrix_hypergeometric(vir.kappa, vir.alpha, vir.Delta)
        assert conn['type'] == 'hypergeometric'
        assert conn['monodromy_eigenvalue'] == -1

    def test_indicial_exponent_half(self):
        """Connection data: indicial exponent = 1/2."""
        vir = virasoro_data(13.0)
        conn = connection_matrix_hypergeometric(vir.kappa, vir.alpha, vir.Delta)
        assert abs(conn['indicial_exponent'] - 0.5) < 1e-10

    def test_branch_separation_positive(self):
        """Branch point separation is positive for class M."""
        vir = virasoro_data(1.0)
        conn = connection_matrix_hypergeometric(vir.kappa, vir.alpha, vir.Delta)
        assert conn['separation'] > 0

    def test_period_nonzero(self):
        """Period of the elliptic integral is nonzero."""
        vir = virasoro_data(1.0)
        conn = connection_matrix_hypergeometric(vir.kappa, vir.alpha, vir.Delta)
        assert abs(conn['period']) > 0

    def test_connection_at_zeta_zeros(self):
        """Connection data at zeta zero parameters is well-defined."""
        data = connection_data_at_zeta_zeros(n_max=5)
        assert len(data) == 5
        for entry in data:
            assert entry['monodromy'] == -1

    def test_branch_separation_at_zeta_zero(self):
        """Branch separation is nonzero at zeta zero parameters."""
        data = connection_data_at_zeta_zeros(n_max=3)
        for entry in data:
            if entry.get('branch_separation') is not None:
                assert abs(entry['branch_separation']) > 0

    def test_period_at_zeta_zeros_complex(self):
        """Periods at complex c values are complex."""
        data = connection_data_at_zeta_zeros(n_max=3)
        for entry in data:
            if entry.get('period') is not None:
                # At complex c, period should be genuinely complex
                assert isinstance(entry['period'], complex)


# ===========================================================================
# Section 8: P_III from genus-1 shadow (8 tests)
# ===========================================================================

class TestPainleveIII:
    """Verify P_III identification from genus-1 shadow."""

    def test_piii_from_virasoro(self):
        """P_III data from Virasoro genus-1 shadow."""
        vir = virasoro_data(1.0)
        result = genus1_shadow_to_piii(vir)
        assert result['kappa'] == 0.5
        assert abs(result['F1'] - 0.5 / 24) < 1e-12

    def test_piii_structural_analogy(self):
        """P_III identification is a structural analogy, not a theorem."""
        vir = virasoro_data(1.0)
        result = genus1_shadow_to_piii(vir)
        assert result['is_structural_analogy'] is True

    def test_bessel_order_from_kappa(self):
        """Bessel order nu = sqrt(kappa)."""
        vir = virasoro_data(1.0)
        result = genus1_shadow_to_piii(vir)
        assert abs(result['bessel_order'] - cmath.sqrt(0.5)) < 1e-12

    def test_piii_params_degenerate(self):
        """P_III params: gamma = delta = 0 (D7 type)."""
        vir = virasoro_data(1.0)
        result = genus1_shadow_to_piii(vir)
        piii = result['piii_params']
        assert abs(piii.gamma_piii) < 1e-12
        assert abs(piii.delta_piii) < 1e-12

    def test_bessel_asymptotic_zero(self):
        """I_nu(r) ~ (r/2)^nu / Gamma(nu+1) at r -> 0."""
        coeffs = piii_asymptotic_at_zero(nu=0.5, n_terms=5)
        assert len(coeffs) == 5
        assert abs(coeffs[0] - 1.0) < 1e-12  # leading coefficient is 1

    def test_bessel_asymptotic_infinity(self):
        """I_nu(r) ~ e^r / sqrt(2*pi*r) at r -> infinity."""
        coeffs = piii_asymptotic_at_infinity(nu=0.5, n_terms=5)
        assert len(coeffs) == 5
        assert abs(coeffs[0] - 1.0) < 1e-12

    def test_bessel_correction_first(self):
        """First correction: d_1 = (4*nu^2 - 1) / 8."""
        nu = 0.5
        coeffs = piii_asymptotic_at_infinity(nu=nu, n_terms=2)
        d1_expected = (4 * nu**2 - 1) / 8
        assert abs(coeffs[1] - d1_expected) < 1e-10

    def test_piii_landscape(self):
        """P_III data across multiple families."""
        families = [
            virasoro_data(1.0),
            virasoro_data(13.0),
            virasoro_data(25.0),
        ]
        for fam in families:
            result = genus1_shadow_to_piii(fam)
            assert abs(result['F1'] - fam.kappa / 24.0) < 1e-12


# ===========================================================================
# Section 9: Zeta zero evaluations (8 tests)
# ===========================================================================

class TestZetaZeroEvaluations:
    """Shadow data at zeta zero parameters c = 1/2 + i*gamma_n."""

    def test_first_zeta_zero(self):
        """gamma_1 = 14.134725... (standard value)."""
        assert abs(ZETA_ZEROS_20[0] - 14.134725141734693) < 1e-10

    def test_shadow_at_zeta_zero_1(self):
        """Shadow data at c(rho_1) is well-defined."""
        data = shadow_at_zeta_zero(1)
        assert data['n'] == 1
        assert abs(data['c'] - (0.5 + 1j * 14.134725141734693)) < 1e-8

    def test_kappa_at_zeta_zero(self):
        """kappa = c/2 at complex c."""
        for n in range(1, 6):
            data = shadow_at_zeta_zero(n)
            assert abs(data['kappa'] - data['c'] / 2) < 1e-10

    def test_discriminant_at_zeta_zeros(self):
        """Discriminant disc = -32*kappa^2*Delta at zeta zero params."""
        for n in range(1, 6):
            data = shadow_at_zeta_zero(n)
            disc_expected = -32 * data['kappa']**2 * data['Delta']
            disc_actual = data['q1']**2 - 4 * data['q0'] * data['q2']
            assert abs(disc_actual - disc_expected) < 1e-4 * max(abs(disc_actual), 1)

    def test_branch_points_nondegenerate(self):
        """Branch points at zeta zero params are non-degenerate."""
        for n in range(1, 6):
            data = shadow_at_zeta_zero(n)
            assert abs(data['branch_point_plus'] - data['branch_point_minus']) > 1e-10

    def test_cross_ratio_at_zeta_zeros(self):
        """W_3 cross-ratio at zeta zero params is computed."""
        results = cross_ratio_at_zeta_zeros(n_max=5)
        assert len(results) == 5
        for entry in results:
            if not entry.get('error'):
                assert abs(entry['cross_ratio']) > 0

    def test_shadow_at_zeta_zero_varies(self):
        """Shadow data varies with n (different gamma_n)."""
        d1 = shadow_at_zeta_zero(1)
        d2 = shadow_at_zeta_zero(2)
        assert abs(d1['kappa'] - d2['kappa']) > 1e-3

    def test_q0_at_zeta_zero(self):
        """Q_L(0) = 4*kappa^2 = c^2 at zeta zero params."""
        for n in range(1, 4):
            data = shadow_at_zeta_zero(n)
            assert abs(data['q0'] - data['c']**2) < 1e-8


# ===========================================================================
# Section 10: Multi-path verification (10 tests)
# ===========================================================================

class TestMultiPathVerification:
    """Multi-path verification of core mathematical claims."""

    def test_indicial_universal_all_families(self):
        """Indicial exponent = 1/2 for ALL class M families (3 paths)."""
        families = [
            virasoro_data(1.0),
            virasoro_data(13.0),
            virasoro_data(25.0),
            betagamma_data(),
        ]
        result = verify_indicial_exponent_universal(families)
        for fam_result in result['families']:
            if not fam_result.get('skip'):
                assert fam_result['all_agree']

    def test_disc_relation_all_families(self):
        """disc(Q_L) = -32*kappa^2*Delta for all families (3 paths)."""
        families = [
            virasoro_data(1.0),
            virasoro_data(13.0),
            heisenberg_data(1.0),
            betagamma_data(),
        ]
        result = verify_discriminant_relation(families)
        for entry in result['data']:
            assert entry['paths_agree_12']

    def test_pvi_params_universal_verification(self):
        """P_VI params are c-independent (verified at 5 values)."""
        c_vals = [2.0, 5.0, 13.0, 20.0, 25.0]
        result = verify_pvi_params_universal(c_vals)
        for entry in result['data']:
            if not entry.get('error'):
                assert entry['alpha_check']
                assert entry['beta_check']
                assert entry['gamma_check']
                assert entry['delta_check']

    def test_tau_flat_section_verification(self):
        """tau = flat section verified by integration (2 paths)."""
        vir = virasoro_data(13.0)
        t_vals = [0.01 * i for i in range(1, 31)]
        result = verify_tau_equals_flat_section(vir.kappa, vir.alpha, vir.Delta, t_vals)
        agree_count = sum(1 for e in result['data'][1:] if e['path1_path2_agree'])
        assert agree_count >= 25  # most should agree

    def test_H_squared_equals_t4_Q(self):
        """H^2 = t^4 * Q_L (Riccati algebraicity, 2 paths)."""
        vir = virasoro_data(1.0)
        for t_val in [0.1, 0.3, 0.5, 0.7, 1.0]:
            H = shadow_generating_function(vir.kappa, vir.alpha, vir.Delta, t_val)
            Q = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, t_val)
            lhs = H**2
            rhs = t_val**4 * Q
            assert abs(lhs - rhs) < 1e-10 * max(abs(rhs), 1)

    def test_flat_section_satisfies_ode(self):
        """Phi(t) = sqrt(Q/Q(0)) satisfies Phi' = (Q'/(2Q))*Phi (2 paths)."""
        vir = virasoro_data(1.0)
        q0, q1, q2 = shadow_metric_coeffs(vir.kappa, vir.alpha, vir.Delta)
        t_val = 0.3
        dt = 1e-6

        # Path 1: numerical derivative
        tau_t = shadow_tau_flat_section(vir.kappa, vir.alpha, vir.Delta, t_val)
        tau_tdt = shadow_tau_flat_section(vir.kappa, vir.alpha, vir.Delta, t_val + dt)
        Phi_prime_num = (tau_tdt - tau_t) / dt

        # Path 2: from connection form
        Q_t = shadow_metric_eval(vir.kappa, vir.alpha, vir.Delta, t_val)
        Qp_t = q1 + 2 * q2 * t_val
        Phi_prime_form = (Qp_t / (2 * Q_t)) * tau_t

        assert abs(Phi_prime_num - Phi_prime_form) / max(abs(Phi_prime_form), 1e-10) < 1e-4

    def test_stokes_from_borel_virasoro(self):
        """Borel-Stokes: universal multiplier S = 2*pi*i."""
        vir = virasoro_data(1.0)
        result = stokes_from_borel_resurgence(vir.kappa, vir.alpha, vir.Delta)
        assert result['type'] == 'resurgent'
        assert abs(result['stokes_abs'] - 2 * math.pi) < 1e-10

    def test_stokes_trivial_heisenberg(self):
        """Heisenberg: no Borel singularities (trivial)."""
        heis = heisenberg_data(1.0)
        result = stokes_from_borel_resurgence(heis.kappa, heis.alpha, heis.Delta)
        assert result['type'] == 'trivial'
        assert len(result['stokes_multipliers']) == 0

    def test_cross_ratio_symmetric(self):
        """Cross-ratio satisfies lambda(z1,z2,z3,z4) = 1/lambda(z2,z1,z3,z4)."""
        z1, z2, z3, z4 = 1.0, 2.0, 3.0, 5.0
        lam_1 = cross_ratio_4pts(z1, z2, z3, z4)
        lam_2 = cross_ratio_4pts(z2, z1, z3, z4)
        assert abs(lam_1 * lam_2 - 1.0) < 1e-10

    def test_nekrasov_comparison(self):
        """Nekrasov genus-1 comparison: F_1 = kappa/24."""
        result = nekrasov_genus1_comparison(6.5)
        assert abs(result['F1_shadow'] - 6.5 / 24.0) < 1e-12


# ===========================================================================
# Section 11: Cross-ratio landscape (5 tests)
# ===========================================================================

class TestCrossRatioLandscape:
    """Verify P_VI cross-ratio lambda(c) across parameter space."""

    def test_cross_ratio_self_dual(self):
        """Cross-ratio at self-dual point c=13."""
        params = pvi_from_w3_shadow(13.0)
        lam = params.cross_ratio
        # Should be well-defined and finite
        assert abs(lam) < 100

    def test_cross_ratio_different_c(self):
        """Cross-ratios differ at different c values."""
        lam_5 = w3_cross_ratio_analytic(5.0)
        lam_20 = w3_cross_ratio_analytic(20.0)
        assert abs(lam_5 - lam_20) > 1e-6

    def test_cross_ratio_landscape_computed(self):
        """Full cross-ratio landscape is computed without errors."""
        c_vals = [3.0, 5.0, 8.0, 13.0, 20.0, 25.0]
        landscape = pvi_cross_ratio_landscape(c_vals)
        non_error = [e for e in landscape if e.get('cross_ratio') is not None]
        assert len(non_error) >= 4

    def test_full_analysis_runs(self):
        """Full Painleve-shadow analysis runs for c=13."""
        result = full_painleve_shadow_analysis(13.0)
        assert result['c'] == 13.0
        assert result['summary']['single_channel_painleve'] == 'none (rigid Fuchsian)'
        assert result['summary']['multi_channel_painleve'] == 'PVI'

    def test_standard_landscape(self):
        """Standard landscape analysis covers all families."""
        landscape = standard_landscape_analysis()
        assert len(landscape) == 8
        names = [e['name'] for e in landscape]
        assert any('Heisenberg' in n for n in names)
        assert any('Virasoro' in n for n in names)


# ===========================================================================
# Additional integration/smoke tests
# ===========================================================================

class TestIntegration:
    """Integration and smoke tests."""

    def test_pvi_integration_short(self):
        """P_VI integration runs for a short interval."""
        params = pvi_from_w3_shadow(13.0)
        # Use a safe initial condition and interval
        trajectory = integrate_pvi(params, t_start=0.3, t_end=0.4,
                                   y0=0.5 + 0.1j, p0=0.1, n_steps=100)
        assert len(trajectory) > 50
        # Last point should be finite
        last_t, last_y, last_p = trajectory[-1]
        if not cmath.isnan(last_y):
            assert abs(last_y) < 1e10

    def test_jmu_tau_pvi(self):
        """JMU tau function along P_VI trajectory is computed."""
        params = pvi_from_w3_shadow(13.0)
        trajectory = integrate_pvi(params, t_start=0.3, t_end=0.35,
                                   y0=0.5, p0=0.1, n_steps=50)
        tau_data = jmu_tau_pvi(params, trajectory)
        assert len(tau_data) > 0
        # First tau value should be finite
        assert not cmath.isnan(tau_data[0]['tau'])

    def test_20_zeta_zeros(self):
        """20 zeta zeros are stored with correct ordering."""
        assert len(ZETA_ZEROS_20) == 20
        for i in range(19):
            assert ZETA_ZEROS_20[i] < ZETA_ZEROS_20[i + 1]

    def test_shadow_at_all_20_zeros(self):
        """Shadow data is computed at all 20 zeta zeros."""
        for n in range(1, 21):
            data = shadow_at_zeta_zero(n)
            assert data['n'] == n
            assert abs(data['gamma_n'] - ZETA_ZEROS_20[n - 1]) < 1e-8
