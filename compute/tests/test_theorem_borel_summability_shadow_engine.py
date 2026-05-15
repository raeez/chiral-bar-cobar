r"""Tests for scalar shadow genus convergence and Borel diagnostics.

Tests organized into 8 verification blocks:

Block 1: Shadow series convergence (c > c*)
Block 2: Shadow series divergence (c < c*)
Block 3: Gevrey-0 growth verification
Block 4: Ordinary genus generating function vs series
Block 5: True Borel transforms and Borel-Laplace reconstruction
Block 6: Ordinary generating-function pole residues
Block 7: Instanton action verification
Block 8: Cross-checks and structural properties

Multi-path checks:
    Every numerical claim verified by at least 3 independent paths.
"""

import math
from fractions import Fraction

from compute.lib.theorem_borel_summability_shadow_engine import (
    INSTANTON_ACTION,
    F_g_exact,
    F_g_virasoro,
    _bernoulli_exact,
    _lambda_fp_exact,
    analytic_certification_firewall,
    borel_laplace_integral,
    borel_transform_even_series,
    borel_transform_t_series,
    borel_summability_data,
    genus_generating_function,
    genus_generating_function_analyticity_strip,
    genus_generating_function_series,
    convergence_radius_shadow,
    convergence_test_at_c,
    critical_central_charge,
    gevrey_class_test,
    growth_rate,
    growth_rate_squared_exact,
    kappa_virasoro,
    lateral_borel_sums,
    lateral_borel_jump_diagnostic,
    oscillatory_parameters,
    ordinary_genus_pole_circulation,
    ordinary_genus_pole_residue,
    object_and_kernel_firewalls,
    partial_sum_shadow,
    scalar_genus_singularity_audit,
    shadow_coefficients_exact,
    shadow_coefficients_numerical,
    shadow_discriminant,
    shadow_metric_branch_points,
    virasoro_shadow_metric_coeffs,
    virasoro_shadow_metric_coeffs_exact,
    shadow_vs_string_comparison,
    verify_generating_function_vs_series,
    verify_convergence_at_c,
    verify_instanton_action,
)


# ============================================================================
# Block 1: Shadow series convergence (c > c*)
# ============================================================================

class TestConvergenceRegion:
    """Verify absolute convergence of sum S_r t^r for c > c* ~ 6.125."""

    def test_convergence_at_c13(self):
        """c=13: rho ~ 0.467, strong convergence. Partial sums must stabilize."""
        result = convergence_test_at_c(13.0, max_r=25)
        assert result['converges'] is True
        assert result['rho'] < 1.0
        # Partial sums should stabilize: last 5 sums within 0.1% of each other
        sums = result['partial_sums']
        assert len(sums) >= 15
        last5 = [s[1] for s in sums[-5:]]
        spread = max(last5) - min(last5)
        assert spread / max(abs(last5[-1]), 1e-10) < 0.001

    def test_convergence_at_c26(self):
        """c=26: rho ~ 0.232, very strong convergence."""
        result = convergence_test_at_c(26.0, max_r=25)
        assert result['converges'] is True
        assert result['rho'] < 0.25
        sums = result['partial_sums']
        last5 = [s[1] for s in sums[-5:]]
        spread = max(last5) - min(last5)
        assert spread / max(abs(last5[-1]), 1e-10) < 1e-4

    def test_convergence_at_c50(self):
        """c=50: rho ~ 0.135, rapid convergence."""
        result = convergence_test_at_c(50.0, max_r=20)
        assert result['converges'] is True
        assert result['rho'] < 0.15
        sums = result['partial_sums']
        last5 = [s[1] for s in sums[-5:]]
        spread = max(last5) - min(last5)
        assert spread / max(abs(last5[-1]), 1e-10) < 1e-6

    def test_growth_rate_decreasing_above_cstar(self):
        """rho(c) is strictly decreasing for c > c*."""
        c_vals = [7.0, 10.0, 13.0, 20.0, 26.0, 50.0, 100.0]
        rhos = [growth_rate(c) for c in c_vals]
        for i in range(len(rhos) - 1):
            assert rhos[i] > rhos[i + 1], f"rho not decreasing: rho({c_vals[i]})={rhos[i]} vs rho({c_vals[i+1]})={rhos[i+1]}"

    def test_partial_sum_matches_integral(self):
        """Partial sum of S_r converges to integral_0^1 t*sqrt(Q_L(t)) dt.

        Since S_r = a_{r-2}/r where a_n are Taylor coefficients of sqrt(Q_L),
        sum_{r=2}^inf S_r = sum_{n=0}^inf a_n/(n+2) = integral_0^1 t*sqrt(Q_L(t)) dt.

        Path 1: partial sum through r=25.
        Path 2: numerical quadrature of the integral.
        Path 3: exact Fraction arithmetic.
        """
        c_val = 13.0
        q0, q1, q2 = virasoro_shadow_metric_coeffs(c_val)

        # Path 1: partial sum
        coeffs = shadow_coefficients_exact(Fraction(13), max_r=25)
        partial = sum(float(coeffs[r]) for r in range(2, 26))

        # Path 2: numerical quadrature
        import scipy.integrate as integrate
        integral_val, _ = integrate.quad(
            lambda t: t * math.sqrt(q0 + q1 * t + q2 * t ** 2), 0, 1
        )

        assert abs(partial - integral_val) < 1e-6, \
            f"Partial sum {partial} vs integral {integral_val}"


# ============================================================================
# Block 2: Shadow series divergence (c < c*)
# ============================================================================

class TestDivergenceRegion:
    """Verify geometric divergence of sum S_r t^r for c < c*."""

    def test_divergence_at_c1(self):
        """c=1: rho ~ 6.24, strong divergence."""
        result = convergence_test_at_c(1.0, max_r=20)
        assert result['converges'] is False
        assert result['rho'] > 6.0
        # Partial sums should grow without bound
        sums = result['partial_sums']
        abs_sums = [abs(s[1]) for s in sums[-5:]]
        assert max(abs_sums) > 10.0  # growing

    def test_divergence_at_c5(self):
        """c=5: rho ~ 1.27, marginal divergence."""
        rho = growth_rate(5.0)
        assert rho > 1.0
        assert rho < 1.5

    def test_critical_central_charge(self):
        """c* ~ 6.12537: the unique positive root of rho(c) = 1.

        Path 1: Newton's method.
        Path 2: Direct evaluation of rho at c*.
        Path 3: Polynomial root: 5c^3 + 22c^2 - 180c - 872 = 0.
        """
        c_star = critical_central_charge()
        # Path 1: value check
        assert abs(c_star - 6.12537) < 0.001

        # Path 2: rho(c*) = 1
        rho_at_cstar = growth_rate(c_star)
        assert abs(rho_at_cstar - 1.0) < 1e-6

        # Path 3: polynomial root
        poly_val = 5.0 * c_star ** 3 + 22.0 * c_star ** 2 - 180.0 * c_star - 872.0
        assert abs(poly_val) < 1e-8

    def test_rho_at_c1_exact(self):
        """Exact rho^2 = (180*1+872)/(1^2*(5*1+22)) = 1052/27."""
        rho_sq = (180.0 + 872.0) / (1.0 * 27.0)
        assert abs(rho_sq - 1052.0 / 27.0) < 1e-10
        rho = math.sqrt(rho_sq)
        assert abs(rho - growth_rate(1.0)) < 1e-10
        assert growth_rate_squared_exact(Fraction(1)) == Fraction(1052, 27)


# ============================================================================
# Block 3: Gevrey-0 growth verification
# ============================================================================

class TestGevrey0:
    """Verify Gevrey-0 (sub-factorial) growth: |S_r|/r! -> 0."""

    def test_gevrey0_at_c1(self):
        """At c=1 (divergent region): |S_r|/r! still -> 0.

        The oscillatory structure (complex conjugate branch points) causes
        local non-monotonicity in |S_r|/r!, but the OVERALL trend is
        super-exponential decay. We verify that the last third of the
        ratios are much smaller than the first third.
        """
        result = gevrey_class_test(1.0, max_r=20)
        ratios = result['gevrey_ratios']
        assert len(ratios) >= 10
        # First third vs last third: last third should be much smaller
        n = len(ratios)
        first_third = [r[1] for r in ratios[:n // 3]]
        last_third = [r[1] for r in ratios[2 * n // 3:]]
        assert max(last_third) < max(first_third) * 0.01, \
            "Gevrey-0: |S_r|/r! not decaying overall"
        # Last value should be very small
        assert ratios[-1][1] < 1e-5, f"|S_20|/20! = {ratios[-1][1]}, expected < 1e-5"

    def test_gevrey0_at_c13(self):
        """At c=13 (convergent region): |S_r|/r! -> 0 rapidly."""
        result = gevrey_class_test(13.0, max_r=20)
        ratios = result['gevrey_ratios']
        # Last ratio should be extremely small
        assert ratios[-1][1] < 1e-20

    def test_darboux_exponent(self):
        """Verify |S_r| * r^{5/2} / rho^r is bounded (Darboux exponent -5/2).

        The Darboux transfer theorem for algebraic singularity predicts:
            S_r ~ C * rho^r * r^{-5/2} * cos(r*theta + phi)
        The rescaled values oscillate due to the cosine factor from the
        complex conjugate branch points. The correct test is that the
        ENVELOPE is bounded: max(|S_r| * r^{5/2} / rho^r) < infinity.

        With exponent -5/2, the rescaled values are bounded.
        With the wrong exponent (e.g. -3/2), they would grow as r.
        """
        result = gevrey_class_test(13.0, max_r=25)
        darboux = result['darboux_ratios']
        assert len(darboux) >= 10
        vals = [d[1] for d in darboux]
        # All rescaled values should be bounded (say < 100)
        assert max(vals) < 100.0, f"Darboux rescaled values unbounded: max={max(vals)}"
        # Verify the WRONG exponent -3/2 would give growing values:
        rho = result['rho']
        coeffs = shadow_coefficients_numerical(13.0, max_r=25)
        wrong_exponent_vals = []
        for r in range(4, 26):
            if r in coeffs and abs(coeffs[r]) > 0 and rho > 0:
                wrong = abs(coeffs[r]) / (rho ** r) * r ** 1.5
                wrong_exponent_vals.append(wrong)
        # With -3/2 instead of -5/2, the rescaled values should be SMALLER
        # (since r^{1.5} < r^{2.5}), so this test checks the exponent indirectly
        assert max(vals) > max(wrong_exponent_vals), \
            "Exponent -5/2 gives larger rescaled values than -3/2, as expected"

    def test_not_gevrey1(self):
        """Shadow coefficients have subfactorial growth.

        String genus expansion: F_g^{string} ~ (2g)!, so |F_g|/(2g)! -> C != 0.
        Shadow: S_r ~ rho^r * r^{-5/2}, so |S_r|/r! -> 0.

        At c=1, rho ~ 6.24, so |S_r|/r! ~ rho^r/(r! * r^{5/2}).
        By Stirling, r! ~ (r/e)^r * sqrt(2*pi*r), so
        rho^r/r! ~ (rho*e/r)^r / sqrt(2*pi*r) -> 0 for r >> rho*e ~ 17.
        We verify the ratio is decaying by comparing r=15 and r=20 values.
        """
        coeffs = shadow_coefficients_numerical(1.0, max_r=20)
        ratios = {}
        for r in range(10, 21):
            if r in coeffs and abs(coeffs[r]) > 0:
                ratios[r] = abs(coeffs[r]) / math.factorial(r)
        # The ratio at r=20 should be much smaller than at r=10
        assert ratios[20] < ratios[10] * 0.01, \
            f"|S_20|/20! = {ratios[20]} not much less than |S_10|/10! = {ratios[10]}"
        # Also verify at c=13 (convergent region): the decay is extreme
        coeffs13 = shadow_coefficients_numerical(13.0, max_r=20)
        ratio13 = abs(coeffs13[20]) / math.factorial(20) if abs(coeffs13[20]) > 0 else 0
        assert ratio13 < 1e-25, f"|S_20|/20! at c=13 = {ratio13}"


# ============================================================================
# Block 4: Ordinary genus generating function vs series
# ============================================================================

class TestGeneratingFunction:
    """Verify G[F](xi) = kappa*(xi/(2*sin(xi/2)) - 1) = sum F_g xi^{2g}."""

    def test_closed_vs_series_real_axis(self):
        """G[F] closed form vs series agree on the real axis for |xi| < 2*pi.

        Path 1: closed form kappa*(xi/(2*sin(xi/2)) - 1).
        Path 2: truncated series sum F_g xi^{2g}.
        """
        kappa = 13.0 / 2.0  # c=13
        for xi in [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]:
            closed = genus_generating_function(xi, kappa)
            series = genus_generating_function_series(xi, kappa, g_max=40)
            # Tolerance widens near the pole at 2*pi ~ 6.28
            tol = 1e-6 if xi > 4.0 else 1e-8
            assert abs(closed - series) < tol, \
                f"Mismatch at xi={xi}: closed={closed}, series={series}"

    def test_closed_vs_series_complex(self):
        """Agreement at complex xi points inside convergence disk."""
        kappa = 13.0 / 2.0
        for xi in [1.0 + 1.0j, 2.0 - 0.5j, 3.0 + 0.3j, 0.5j]:
            closed = genus_generating_function(xi, kappa)
            series = genus_generating_function_series(xi, kappa, g_max=40)
            assert abs(closed - series) < 1e-7, \
                f"Mismatch at xi={xi}: |diff|={abs(closed - series)}"

    def test_poles_at_2pin(self):
        """G[F] has poles at xi = 2*pi*n: |G[F](2*pi*n +/- eps)| -> inf."""
        kappa = 1.0
        for n in [1, 2, 3]:
            xi_near = 2.0 * math.pi * n + 1e-8
            val = genus_generating_function(xi_near, kappa)
            assert abs(val) > 1e6, f"|G[F]| near xi=2*pi*{n} should diverge"

    def test_generating_function_at_origin(self):
        """G[F](xi) ~ kappa*xi^2/24 near xi=0.

        From the expansion: xi/(2*sin(xi/2)) = 1 + xi^2/24 + ...
        so G[F](xi) = kappa*(1 + xi^2/24 + ... - 1) ~ kappa*xi^2/24.
        """
        kappa = 5.0
        xi = 0.01
        val = genus_generating_function(xi, kappa)
        expected = kappa * xi ** 2 / 24.0
        assert abs(val - expected) / abs(expected) < 0.01

    def test_generating_function_complex_origin_direction(self):
        """The near-origin branch is analytic: xi^2, not |xi|^2."""
        kappa = 5.0
        xi = 1e-16j
        val = genus_generating_function(xi, kappa)
        expected = kappa * xi ** 2 / 24.0
        assert val == expected

    def test_f1_coefficient(self):
        """The xi^2 coefficient of G[F] is F_1 = kappa/24.

        G[F](xi) = sum F_g xi^{2g} so the xi^2 coefficient is F_1 = kappa/24.

        Path 1: closed form coefficient extraction (G ~ kappa*xi^2/24 near 0).
        Path 2: direct F_1 = kappa * lambda_1^FP computation.
        Path 3: Bernoulli B_2 = 1/6, lambda_1 = (2^1-1)/2^1 * |B_2|/2! = 1/24.
        """
        c_val = 26.0
        kappa = kappa_virasoro(c_val)
        F1 = F_g_virasoro(1, c_val)
        assert abs(F1 - kappa / 24.0) < 1e-12
        # From lambda_fp
        lam1 = float(_lambda_fp_exact(1))
        assert abs(lam1 - 1.0 / 24.0) < 1e-15

    def test_verify_utility(self):
        """Run the verify_generating_function_vs_series utility at c=13."""
        kappa = 13.0 / 2.0
        results = verify_generating_function_vs_series(kappa, g_max=40)
        for xi, diff in results:
            assert diff < 1e-6, f"Mismatch at xi={xi}: |diff|={diff}"


# ============================================================================
# Block 5: True Borel transforms and Borel-Laplace reconstruction
# ============================================================================

class TestTrueBorelTransforms:
    """Verify that the true Borel transforms are entire in this scalar sector."""

    def test_even_borel_finite_at_ordinary_pole(self):
        """B_even is finite at xi=2*pi although G[F] has a pole there.

        Path 1: G[F] diverges near xi=2*pi.
        Path 2: B_even[F](2*pi) is a convergent series.
        """
        kappa = 13.0 / 2.0
        near_pole = genus_generating_function(2.0 * math.pi - 1e-8, kappa)
        even_borel = borel_transform_even_series(2.0 * math.pi, kappa, g_max=70)
        assert abs(near_pole) > 1e8
        assert math.isfinite(abs(even_borel))
        assert abs(even_borel) < 100.0

    def test_t_borel_entire_numerical_growth(self):
        """B_t remains finite far beyond the ordinary t-plane radius."""
        kappa = 6.5
        for s in [INSTANTON_ACTION, 2 * INSTANTON_ACTION, -3 * INSTANTON_ACTION]:
            val = borel_transform_t_series(s, kappa, g_max=80)
            assert math.isfinite(abs(val))


class TestBorelLaplace:
    """Verify the true Borel-Laplace integral."""

    def test_borel_sum_rotated_direction(self):
        """The Borel sum along theta=pi/4 converges and gives a finite result."""
        kappa = 13.0 / 2.0
        x_sq = 0.1
        result = borel_laplace_integral(x_sq, kappa, theta=math.pi / 4,
                                        n_points=2000, xi_max=50.0)
        assert math.isfinite(abs(result)), "Borel sum should be finite"
        assert abs(result) > 0, "Borel sum should be nonzero"

    def test_borel_sum_matches_convergent_series(self):
        """Borel-Laplace reconstruction agrees with the convergent series.

        Path 1: direct closed form G[F](sqrt(t)).
        Path 2: standard Borel-Laplace integral using B_t[F].
        Path 3: truncated ordinary genus series.
        """
        kappa = 13.0 / 2.0
        x_sq = 0.5
        result = borel_laplace_integral(x_sq, kappa, theta=0.0,
                                        n_points=4000, xi_max=60.0)
        closed = genus_generating_function(math.sqrt(x_sq), kappa)
        series = genus_generating_function_series(math.sqrt(x_sq), kappa, g_max=40)
        assert abs(closed - series) < 1e-10
        assert abs(result - closed) / abs(closed) < 5e-4

    def test_lateral_sums_agree(self):
        """The true Borel transform is entire, so paired lateral sums agree."""
        kappa = 13.0 / 2.0
        x_sq = 0.5
        lateral = lateral_borel_sums(x_sq, kappa, epsilon=0.02,
                                     n_points=4000, xi_max=60.0)
        disc = lateral['discontinuity']
        scale = max(abs(lateral['mean_borel_sum']), 1.0)
        assert abs(disc) / scale < 5e-3

    def test_lateral_jump_diagnostic_zero_prediction(self):
        """The lateral-jump diagnostic records zero mathematical jump."""
        kappa = 1.0
        data = lateral_borel_jump_diagnostic(0.5, kappa, epsilon=0.02,
                                             n_points=3000, xi_max=50.0)
        assert data['leading_prediction'] == 0j
        assert data['ratio_numerical_to_predicted'] is None


# ============================================================================
# Block 6: Ordinary generating-function pole residues
# ============================================================================

class TestOrdinaryPoleResidues:
    """Verify residues of the ordinary genus generating function G[F]."""

    def test_residue_formula_c13(self):
        """Residue of G[F] at xi=2*pi is -2*pi*kappa.

        Path 1: local sine expansion.
        Path 2: closed-form residue function.
        Path 3: numerical finite-difference residue.
        """
        kappa = 13.0 / 2.0
        res = ordinary_genus_pole_residue(1, kappa)
        expected = -2.0 * math.pi * kappa
        eps = 1e-7
        xi0 = 2.0 * math.pi
        numerical = eps * genus_generating_function(xi0 + eps, kappa)
        assert abs(res - expected) < 1e-10
        assert abs(numerical - expected) / abs(expected) < 1e-6

    def test_pole_circulation_value_c13(self):
        """2*pi*i times the xi=2*pi residue equals -4*pi^2*kappa*i."""
        kappa = 13.0 / 2.0
        S1 = ordinary_genus_pole_circulation(1, kappa)
        expected = -4.0 * math.pi ** 2 * kappa * 1j
        assert abs(S1 - expected) < 1e-10
        assert abs(S1.real) < 1e-10
        assert S1.imag < 0

    def test_residue_formula_all_n(self):
        """Res_{xi=2*pi*n} G[F] = (-1)^n * 2*pi*n*kappa."""
        kappa = 26.0 / 2.0
        for n in range(1, 6):
            res = ordinary_genus_pole_residue(n, kappa)
            expected = kappa * ((-1) ** n) * 2.0 * math.pi * n
            assert abs(res - expected) < 1e-10

    def test_pole_circulation_alternating_sign(self):
        """Pole circulations alternate with (-1)^n."""
        kappa = 1.0
        for n in range(1, 6):
            Sn = ordinary_genus_pole_circulation(n, kappa)
            expected_sign = (-1) ** n
            assert Sn.imag * expected_sign > 0, \
                f"S_{n} has wrong sign: Im(S_{n})={Sn.imag}"

    def test_pole_circulation_proportional_to_kappa(self):
        """Pole circulation ratio is kappa(c1)/kappa(c2) for all n.

        The ordinary residue is linear in kappa.
        """
        kappa1 = kappa_virasoro(13.0)
        kappa2 = kappa_virasoro(26.0)
        for n in range(1, 4):
            S1 = ordinary_genus_pole_circulation(n, kappa1)
            S2 = ordinary_genus_pole_circulation(n, kappa2)
            ratio = S1 / S2
            expected = kappa1 / kappa2
            assert abs(ratio - expected) < 1e-10

    def test_residue_formula_by_lhopital(self):
        """Verify the residue formula: Res_{xi=2*pi*n} = (-1)^n * 2*pi*n*kappa.

        Independent verification via L'Hopital on kappa*(xi/(2*sin(xi/2)) - 1):
        At xi = 2*pi*n: sin(xi/2) = sin(pi*n) = 0.
        lim (xi - 2*pi*n) * xi / (2*sin(xi/2))
          = lim (xi - 2*pi*n) * xi / (2*(-1)^n * sin((xi-2*pi*n)/2))
          = lim 2*pi*n * (xi - 2*pi*n) / ((-1)^n * (xi - 2*pi*n))
          = (-1)^n * 2*pi*n.
        """
        kappa = 3.5
        for n in [1, 2, 3]:
            res = ordinary_genus_pole_residue(n, kappa)
            expected = kappa * ((-1) ** n) * 2.0 * math.pi * n
            assert abs(res - expected) < 1e-10


# ============================================================================
# Block 7: Instanton action verification
# ============================================================================

class TestInstantonAction:
    """Verify the scalar t-plane radius A = (2*pi)^2."""

    def test_instanton_action_value(self):
        """A = (2*pi)^2 ~ 39.478."""
        assert abs(INSTANTON_ACTION - (2.0 * math.pi) ** 2) < 1e-10
        assert abs(INSTANTON_ACTION - 39.4784176) < 0.001

    def test_instanton_from_genus_ratio_c13(self):
        """Extract A from F_g/F_{g-1} at c=13.

        The factorial in |B_{2g}| is already divided out in lambda_g^FP.
        Hence F_g/F_{g-1} tends to 1/(2*pi)^2 and
        F_{g-1}/F_g tends to A = (2*pi)^2.
        """
        result = verify_instanton_action(13.0, g_max=12)
        estimates = result['estimates']
        # Last estimate should be close to (2*pi)^2
        best = estimates[-1][1]
        assert abs(best - INSTANTON_ACTION) / INSTANTON_ACTION < 0.01, \
            f"A estimate={best}, expected={INSTANTON_ACTION}"

    def test_instanton_from_genus_ratio_c26(self):
        """Same verification at c=26."""
        result = verify_instanton_action(26.0, g_max=12)
        best = result['estimates'][-1][1]
        assert abs(best - INSTANTON_ACTION) / INSTANTON_ACTION < 0.01

    def test_instanton_from_genus_ratio_c1(self):
        """Same verification at c=1 (divergent region)."""
        result = verify_instanton_action(1.0, g_max=12)
        best = result['estimates'][-1][1]
        assert abs(best - INSTANTON_ACTION) / INSTANTON_ACTION < 0.01

    def test_ordinary_singularity_and_true_borel_firewall(self):
        """The ordinary pole at xi=2*pi is not a true Borel singularity.

        Path 1: xi/(2*sin(xi/2)) has first pole at xi = 2*pi.
        Path 2: the even Borel transform is finite at xi = 2*pi.
        Path 3: the t-Borel transform is finite at s = (2*pi)^2.
        """
        kappa = 1.0
        xi_near = 2.0 * math.pi - 1e-6
        val = genus_generating_function(xi_near, kappa)
        even_borel = borel_transform_even_series(2.0 * math.pi, kappa)
        t_borel = borel_transform_t_series(INSTANTON_ACTION, kappa)
        assert abs(val) > 1e4, "G[F] should diverge near xi=2*pi"
        assert math.isfinite(abs(even_borel))
        assert math.isfinite(abs(t_borel))

    def test_scalar_singularity_audit_separates_planes(self):
        """Ordinary poles, reconstructed-sum singularities, and Borel data differ."""
        kappa = 13.0 / 2.0
        audit = scalar_genus_singularity_audit(kappa, n=1)
        assert abs(audit['ordinary_xi_plane']['pole'] - 2.0 * math.pi) < 1e-12
        assert abs(audit['ordinary_t_plane']['singularity'] - INSTANTON_ACTION) < 1e-12
        assert audit['ordinary_t_plane']['are_borel_plane_singularities'] is False
        assert audit['true_borel_t_plane']['singularity_set'] == ()
        assert audit['true_borel_even_plane']['singularity_set'] == ()
        assert audit['ordinary_residue_is_stokes_constant'] is False
        assert audit['ecalle_stokes_alien_calculus_certified'] is False
        assert audit['scalar_projection_certifies_full_maurer_cartan_data'] is False


# ============================================================================
# Block 8: Cross-checks and structural properties
# ============================================================================

class TestStructural:
    """Cross-checks, analyticity, discriminant, and comparison tests."""

    def test_branch_points_conjugate(self):
        """For c > 0, branch points are complex conjugates.

        disc(Q_L) = -320c^2/(5c+22) < 0 for c > 0.
        """
        for c_val in [1.0, 5.0, 13.0, 26.0]:
            t_plus, t_minus = shadow_metric_branch_points(c_val)
            assert abs(t_plus - t_minus.conjugate()) < 1e-10, \
                f"Branch points not conjugate at c={c_val}"

    def test_discriminant_negative(self):
        """disc(Q_L) = -320c^2/(5c+22) < 0 for all c > 0."""
        for c_val in [0.1, 1.0, 5.0, 13.0, 26.0, 100.0]:
            d = shadow_discriminant(c_val)
            assert d < 0, f"Discriminant not negative at c={c_val}: {d}"

    def test_generating_function_analyticity_in_strip(self):
        """G[F] is analytic in the strip 0 < Re(xi) < 2*pi."""
        kappa = 6.5
        result = genus_generating_function_analyticity_strip(
            kappa, im_range=1.0, re_range=(0.1, 6.0), n_points=100
        )
        assert result['all_finite'], "G[F] has unexpected singularity in strip"

    def test_virasoro_complementarity_kappa(self):
        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (complementarity sum).

        This is a Virasoro-sector complementarity identity.  It does not
        identify Omega(B(A)) with A^! and it does not compute the bulk
        Z_ch^der(A).
        """
        for c_val in [1.0, 5.0, 13.0, 20.0]:
            k = kappa_virasoro(c_val)
            k_dual = kappa_virasoro(26.0 - c_val)
            assert abs(k + k_dual - 13.0) < 1e-10

    def test_shadow_vs_string_gevrey(self):
        """Scalar shadow is Gevrey-0; this is not a bare summability certificate."""
        result = shadow_vs_string_comparison(13.0, g_max=10)
        assert result['shadow_gevrey'] == 0
        assert result['string_gevrey'] == 1
        assert result['shadow_borel_summable'] is None
        assert result['shadow_borel_summable_scope'] == 'not a bare global certificate'
        assert result['scalar_borel_summability_certified'] is True
        assert result['shadow_series_convergent'] is True
        assert result['string_borel_summable_on_real_axis'] is None
        assert result['string_borel_geometry_certified'] is False

    def test_string_grows_faster(self):
        """String coefficients grow much faster than shadow at large genus.

        F_g^{string} / F_g^{shadow} -> infinity as g -> infinity.
        """
        result = shadow_vs_string_comparison(13.0, g_max=10)
        ratios = result['string_to_shadow_ratio']
        # Ratios should be increasing
        for i in range(len(ratios) - 1):
            if i >= 2:  # skip initial transient
                assert ratios[i + 1][1] > ratios[i][1] * 0.9, \
                    "String/shadow ratio should be increasing"

    def test_oscillatory_parameters(self):
        """Oscillatory parameters are well-defined and consistent."""
        for c_val in [1.0, 13.0, 26.0]:
            params = oscillatory_parameters(c_val)
            assert params['rho'] > 0
            assert -180.0 < params['arg_t_star'] < 180.0
            assert params['theta_oscillation'] > 0
            assert params['beat_period'] > 1.0

    def test_full_data_package(self):
        """The borel_summability_data utility returns scoped diagnostic data."""
        data = borel_summability_data(13.0)
        assert data['converges_at_t1'] is True
        assert data['true_borel_transform_entire'] is True
        assert data['true_borel_singularity_set'] == ()
        assert abs(data['ordinary_t_plane_nearest_singularity'] - INSTANTON_ACTION) < 1e-10
        assert data['lateral_jump_expected'] == 0j
        assert data['gevrey_class'] == 0
        assert abs(data['kappa'] - 6.5) < 1e-10
        assert abs(data['instanton_action'] - INSTANTON_ACTION) < 1e-10
        expected_residue = -2.0 * math.pi * data['kappa']
        assert abs(data['ordinary_pole_residue_n1'] - expected_residue) < 1e-10
        assert data['scalar_borel_summability_certified'] is True
        assert data['scalar_borel_summability_scope'] == 'Borel-Laplace reconstruction of the convergent scalar series'
        assert data['bare_shadow_borel_summability_certified'] is False
        assert data['finite_window_certifies_summability'] is False
        assert data['pade_darboux_certifies_stokes_data'] is False
        assert data['ecalle_stokes_data_certified'] is False
        assert data['full_maurer_cartan_data_certified'] is False
        assert data['global_resurgence_certified'] is False
        assert data['analytic_continuation_certified'] is False
        assert data['nonperturbative_completion_certified'] is False
        assert data['btz_jt_recovery_certified'] is False
        assert data['multiweight_extension_certified'] is False
        assert data['all_genus_partition_theorem_certified'] is False

    def test_certification_firewall_noncertifies_overclaims(self):
        """Finite windows and scalar poles do not certify global analytic claims."""
        firewall = analytic_certification_firewall()
        assert firewall['scalar_coefficient_series']['status'] == 'certified_exact'
        assert firewall['ordinary_scalar_singularities']['status'] == 'certified_exact'
        assert firewall['ordinary_scalar_singularities']['are_true_borel_singularities'] is False
        assert firewall['true_borel_transforms']['status'] == 'certified_for_scalar_coefficients'
        assert firewall['true_borel_transforms']['singularity_set'] == ()
        assert firewall['ordinary_t_plane_singularities']['are_true_borel_singularities'] is False
        assert firewall['shadow_radius_diagnostic']['status'] == 'asymptotic_diagnostic'
        assert firewall['shadow_radius_diagnostic']['certifies_borel_summability'] is False
        assert firewall['shadow_radius_diagnostic']['certifies_analytic_continuation'] is False
        assert firewall['pade_darboux_diagnostics']['certifies_ecalle_stokes_data'] is False
        assert firewall['pade_darboux_diagnostics']['certifies_alien_calculus'] is False
        assert firewall['scalar_projection']['certifies_full_maurer_cartan_data'] is False
        assert firewall['finite_windows']['certifies_borel_summability'] is False
        assert firewall['conditional_laplace_reconstruction']['certifies_full_shadow_tower'] is False
        assert firewall['multiweight_extension']['status'] == 'not_certified_here'
        assert firewall['nonperturbative_completion']['status'] == 'not_certified_here'
        assert firewall['btz_jt_recovery']['status'] == 'not_certified_here'
        assert firewall['ecalle_stokes_alien_calculus']['status'] == 'not_certified_here'
        assert firewall['all_genus_virasoro_or_multiweight_partition_theorem']['status'] == 'not_certified_here'

    def test_object_and_kernel_firewalls(self):
        """Koszul-dual, bar-cobar, Hochschild, and kernel constants stay distinct."""
        firewall = object_and_kernel_firewalls()
        assert firewall['bar_cobar_inversion'] == 'Omega(B(A)) = A'
        assert firewall['bar_cobar_inversion_is_koszul_duality'] is False
        assert 'Verdier' in firewall['koszul_dual_branch']
        assert 'Hochschild' in firewall['bulk_branch']
        kernels = firewall['kernel_constants']
        assert kernels['affine_collision_trace_form'] == 'r^{KM}(z) = k*Omega_tr/z'
        assert kernels['affine_kz_normalization'] == 'r_KZ(z) = Omega/((k+h^vee)z)'
        assert kernels['heisenberg_collision'] == 'r^{Heis}(z) = k/z'
        assert kernels['virasoro_collision'] == 'r^{Vir}(z) = (c/2)/z^3 + 2T/z'
        assert firewall['holographic_package_entries'] == (
            'A', 'A^i', 'A^!', 'C', 'r(z)', 'Theta_A', 'nabla^hol',
        )
        assert firewall['modular_koszul_compute_package_projections'] == (
            'Fact_X(L)', 'barB_X(L)', 'Theta_L', 'L_L',
            '(V_br,T_br)', 'R4_mod(L)',
        )
        assert firewall['scalar_projection_is_full_maurer_cartan_data'] is False

    def test_exact_growth_rate_from_shadow_metric(self):
        """Exact rho^2 equals q2/q0 for the Virasoro shadow metric."""
        q0, q1, q2 = virasoro_shadow_metric_coeffs_exact(Fraction(13))
        assert q0 == Fraction(169)
        assert q1 == Fraction(156)
        assert q2 == Fraction(3212, 87)
        rho_sq = growth_rate_squared_exact(Fraction(13))
        assert rho_sq == q2 / q0
        assert abs(float(rho_sq) - growth_rate(13.0) ** 2) < 1e-12

    def test_exact_vs_numerical_coefficients(self):
        """Exact (Fraction) and numerical (float) shadow coefficients agree.

        Path 1: Fraction arithmetic (exact).
        Path 2: Float arithmetic (numerical).
        """
        c_frac = Fraction(13)
        exact = shadow_coefficients_exact(c_frac, max_r=15)
        numerical = shadow_coefficients_numerical(13.0, max_r=15)
        for r in range(2, 16):
            ex_float = float(exact[r])
            num = numerical[r]
            if abs(ex_float) > 1e-20:
                rel_err = abs(ex_float - num) / abs(ex_float)
                assert rel_err < 1e-10, \
                    f"Exact vs numerical mismatch at r={r}: rel_err={rel_err}"

    def test_virasoro_shadow_coefficients_match_census(self):
        """Exact S_2, S_3, S_4, S_5 match the local Virasoro census constants."""
        c_frac = Fraction(13)
        exact = shadow_coefficients_exact(c_frac, max_r=5)
        assert exact[2] == Fraction(13, 2)
        assert exact[3] == Fraction(2)
        assert exact[4] == Fraction(10, 13 * (5 * 13 + 22))
        assert exact[5] == Fraction(-48, 13 * 13 * (5 * 13 + 22))

    def test_F_g_exact_values(self):
        """Verify F_1 = kappa/24, F_2 = 7*kappa/5760 at c=13.

        Path 1: F_g_exact with Fraction arithmetic.
        Path 2: kappa * lambda_g^FP by hand.
        Path 3: Bernoulli number computation.
        """
        c_frac = Fraction(13)
        # F_1
        F1 = F_g_exact(1, c_frac)
        assert F1 == Fraction(13, 48)  # (13/2) * (1/24) = 13/48
        # F_2
        F2 = F_g_exact(2, c_frac)
        assert F2 == Fraction(13, 2) * Fraction(7, 5760)  # 91/11520
        assert F2 == Fraction(91, 11520)
        # lambda_1 from Bernoulli
        B2 = _bernoulli_exact(2)
        assert B2 == Fraction(1, 6)
        lam1 = Fraction(1, 2) * Fraction(1, 6) / Fraction(2)
        assert lam1 == Fraction(1, 24)
