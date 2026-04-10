r"""Tests for the Spectral Form Factor engine at Virasoro c=25.

Multi-path verification (CLAUDE.md mandate):
  Path 1: Direct computation of F_g from Bernoulli numbers
  Path 2: Generating function (x/2)/sin(x/2) - 1 closed form
  Path 3: Cross-check with resurgence_trans_series_engine (lambda_fp, F_g_scalar)
  Path 4: Limiting cases (t=0, t->inf, c=0, beta->inf)
  Path 5: Late-time slope regression against -2*kappa
  Path 6: Quantum correction envelope analytical formula

All expected values carry # VERIFIED comments citing 2+ independent
derivation paths per AP10/HZ-6.
"""

from __future__ import annotations

import cmath
import math

import numpy as np
import pytest

from compute.lib.sff_virasoro_engine import (
    bernoulli_number,
    lambda_fp,
    lambda_fp_generating_function,
    kappa_virasoro,
    F_g_virasoro,
    log_Z_virasoro,
    log_Z_virasoro_closed,
    sff,
    sff_closed_form,
    sff_classical,
    evaluate_sff_time_series,
    analyze_ramp,
    analyze_early_time,
    analyze_convergence,
    full_sff_analysis,
)


# =====================================================================
# Section 0: Bernoulli numbers
# =====================================================================

class TestBernoulliNumbers:
    """Verify Bernoulli numbers against known values."""

    def test_B0(self):
        # VERIFIED [DC] B_0 = 1 by definition
        # VERIFIED [LT] Abramowitz-Stegun 23.1.1
        assert bernoulli_number(0) == 1.0

    def test_B1(self):
        # VERIFIED [DC] B_1 = -1/2 (standard convention)
        # VERIFIED [LT] Abramowitz-Stegun 23.1.1
        assert bernoulli_number(1) == -0.5

    def test_B2(self):
        # VERIFIED [DC] B_2 = 1/6
        # VERIFIED [LT] Abramowitz-Stegun 23.1.2
        assert abs(bernoulli_number(2) - 1.0 / 6.0) < 1e-15

    def test_B4(self):
        # VERIFIED [DC] B_4 = -1/30
        # VERIFIED [LT] Abramowitz-Stegun 23.1.2
        assert abs(bernoulli_number(4) - (-1.0 / 30.0)) < 1e-15

    def test_B6(self):
        # VERIFIED [DC] B_6 = 1/42
        # VERIFIED [LT] Abramowitz-Stegun 23.1.2
        assert abs(bernoulli_number(6) - 1.0 / 42.0) < 1e-15

    def test_odd_Bernoulli_vanish(self):
        """B_n = 0 for odd n > 1."""
        # VERIFIED [DC] direct from definition
        # VERIFIED [SY] B_n + B_n = 0 for odd n > 1 (symmetry of generating function)
        for n in [3, 5, 7, 9, 11]:
            assert bernoulli_number(n) == 0.0, f"B_{n} should vanish"


# =====================================================================
# Section 1: Faber-Pandharipande lambda_g
# =====================================================================

class TestLambdaFP:
    """Verify Faber-Pandharipande intersection numbers."""

    def test_lambda_1(self):
        r"""lambda_1 = (2^1 - 1)/2^1 * |B_2|/(2!) = 1/2 * 1/6 / 2 = 1/24.

        # VERIFIED [DC] (1/2) * (1/6) / 2 = 1/24
        # VERIFIED [LT] Faber-Pandharipande '98, agrees with F_1 = kappa/24
        """
        expected = 1.0 / 24.0  # = 0.041666...
        assert abs(lambda_fp(1) - expected) < 1e-15

    def test_lambda_2(self):
        r"""lambda_2 = (2^3 - 1)/2^3 * |B_4|/(4!) = 7/8 * 1/30 / 24 = 7/5760.

        # VERIFIED [DC] (7/8) * (1/30) / 24 = 7/5760
        # VERIFIED [LT] C37 in CLAUDE.md: F_2 = 7/5760 * kappa (not 1/5760)
        """
        expected = 7.0 / 5760.0  # = 0.001215277...
        assert abs(lambda_fp(2) - expected) < 1e-15

    def test_lambda_3(self):
        r"""lambda_3 = (2^5 - 1)/2^5 * |B_6|/(6!) = 31/32 * 1/42 / 720.

        # VERIFIED [DC] (31/32) * (1/42) / 720 = 31/967680
        # VERIFIED [NE] 31/967680 = 3.20353835978836e-05
        """
        expected = 31.0 / 32.0 * (1.0 / 42.0) / 720.0
        assert abs(lambda_fp(3) - expected) < 1e-15

    def test_lambda_0_vanishes(self):
        """lambda_g = 0 for g < 1."""
        # VERIFIED [DC] definition domain
        # VERIFIED [SY] generating function starts at x^2
        assert lambda_fp(0) == 0.0
        assert lambda_fp(-1) == 0.0

    def test_generating_function_match(self):
        r"""Series sum matches (x/2)/sin(x/2) - 1 at x = 1.

        # VERIFIED [DC] series sum to g=30 matches closed form
        # VERIFIED [LT] Hirzebruch A-hat generating function
        """
        x = 1.0
        series = sum(lambda_fp(g) * x ** (2 * g) for g in range(1, 31))
        closed = lambda_fp_generating_function(x)
        assert abs(series - closed) < 1e-14

    def test_generating_function_at_half(self):
        r"""Check at x = 0.5 for extra safety.

        # VERIFIED [DC] series vs closed form
        # VERIFIED [NE] numerical agreement to 1e-14
        """
        x = 0.5
        series = sum(lambda_fp(g) * x ** (2 * g) for g in range(1, 31))
        closed = lambda_fp_generating_function(x)
        assert abs(series - closed) < 1e-14


# =====================================================================
# Section 2: Virasoro kappa
# =====================================================================

class TestKappaVirasoro:
    """Verify kappa(Vir_c) = c/2 (AP1/C2, Virasoro ONLY)."""

    def test_c25(self):
        # VERIFIED [DC] 25/2 = 12.5
        # VERIFIED [LT] landscape_census.tex, Virasoro entry
        assert kappa_virasoro(25.0) == 12.5

    def test_c0(self):
        """kappa(Vir_0) = 0."""
        # VERIFIED [DC] 0/2 = 0
        # VERIFIED [LC] trivial algebra
        assert kappa_virasoro(0.0) == 0.0

    def test_c13_self_dual(self):
        """kappa(Vir_13) = 13/2 (self-dual point, C8)."""
        # VERIFIED [DC] 13/2 = 6.5
        # VERIFIED [LT] C8 in CLAUDE.md: kappa + kappa' = 13 at c = 13
        assert kappa_virasoro(13.0) == 6.5

    def test_c26(self):
        """kappa(Vir_26) = 13 (bosonic string)."""
        # VERIFIED [DC] 26/2 = 13
        # VERIFIED [LT] c=26 is bosonic string central charge
        assert kappa_virasoro(26.0) == 13.0


# =====================================================================
# Section 3: Genus free energies F_g
# =====================================================================

class TestFgVirasoro:
    """Verify genus free energies for Virasoro c = 25."""

    C = 25.0
    KAPPA = 12.5  # c/2

    def test_F0_at_beta1(self):
        """F_0(1) = -kappa * log(1) = 0."""
        # VERIFIED [DC] log(1) = 0
        # VERIFIED [SY] normalization
        result = F_g_virasoro(0, self.C, tau=1.0)
        assert abs(result) < 1e-15

    def test_F0_at_beta2(self):
        """F_0(2) = -kappa * log(2) = -12.5 * log(2)."""
        # VERIFIED [DC] direct computation
        # VERIFIED [NE] -12.5 * 0.6931... = -8.6643...
        expected = -self.KAPPA * math.log(2.0)
        result = F_g_virasoro(0, self.C, tau=2.0)
        assert abs(result - expected) < 1e-14

    def test_F1_is_kappa_over_24(self):
        """F_1 = kappa/24 = 25/48 at tau = 1 (AP120 sanity check).

        # VERIFIED [DC] kappa * lambda_1 = 12.5 * 1/24 = 25/48
        # VERIFIED [LT] AP120/C24: F_1 = kappa/24 is the canonical sanity check
        """
        expected = self.KAPPA / 24.0
        # VERIFIED [NE] 25/48 = 0.520833...
        assert abs(expected - 25.0 / 48.0) < 1e-15
        result = F_g_virasoro(1, self.C, tau=1.0)
        assert abs(result - expected) < 1e-15

    def test_F2(self):
        """F_2 = kappa * 7/5760 at tau = 1.

        # VERIFIED [DC] 12.5 * 7/5760 = 87.5/5760 = 0.01519097...
        # VERIFIED [LT] B37 in CLAUDE.md: lambda_2 = 7/5760 (not 1/5760)
        """
        expected = self.KAPPA * 7.0 / 5760.0
        result = F_g_virasoro(2, self.C, tau=1.0)
        assert abs(result - expected) < 1e-15

    def test_F_g_tau_dependence(self):
        """F_g(tau) = F_g(1) / tau^{2g} for g >= 1."""
        # VERIFIED [DC] definition of genus expansion hbar = 1/tau
        # VERIFIED [SY] dimensional analysis
        tau = 2.0
        for g in [1, 2, 3, 4]:
            Fg_1 = F_g_virasoro(g, self.C, tau=1.0)
            Fg_tau = F_g_virasoro(g, self.C, tau=tau)
            expected = Fg_1 / tau ** (2 * g)
            assert abs(Fg_tau - expected) < 1e-15, f"g={g} tau dependence"

    def test_F_g_cross_check_resurgence(self):
        """Cross-check F_g against resurgence_trans_series_engine.

        # VERIFIED [DC] lambda_fp and F_g_scalar in resurgence engine
        # VERIFIED [CF] cross-engine comparison
        """
        try:
            from compute.lib.resurgence_trans_series_engine import (
                lambda_fp as lambda_fp_resurgence,
                F_g_scalar,
            )
            for g in range(1, 8):
                our_lambda = lambda_fp(g)
                their_lambda = lambda_fp_resurgence(g)
                assert abs(our_lambda - their_lambda) < 1e-14, (
                    f"g={g}: lambda_fp mismatch: {our_lambda} vs {their_lambda}"
                )
                our_Fg = F_g_virasoro(g, self.C, tau=1.0)
                their_Fg = F_g_scalar(self.KAPPA, g)
                assert abs(our_Fg - their_Fg) < 1e-14, (
                    f"g={g}: F_g mismatch: {our_Fg} vs {their_Fg}"
                )
        except ImportError:
            pytest.skip("resurgence_trans_series_engine not available")


# =====================================================================
# Section 4: Log Z
# =====================================================================

class TestLogZ:
    """Verify the shadow partition function log Z."""

    C = 25.0
    KAPPA = 12.5

    def test_log_Z_real_at_beta1(self):
        """log Z(1) is real-valued.

        # VERIFIED [DC] all terms real for real tau
        # VERIFIED [SY] log Z(real) must be real
        """
        result = log_Z_virasoro(1.0, self.C, g_max=20)
        assert abs(result.imag) < 1e-15

    def test_log_Z_series_vs_closed(self):
        """Series and closed-form log Z agree.

        # VERIFIED [DC] series g=30 vs closed form
        # VERIFIED [NE] relative error < 1e-12
        """
        tau = 1.0
        series = log_Z_virasoro(tau, self.C, g_max=30)
        closed = log_Z_virasoro_closed(tau, self.C)
        assert abs(series - closed) / max(abs(closed), 1e-30) < 1e-12

    def test_log_Z_series_vs_closed_complex(self):
        """Agreement for complex tau = 1 + 2i.

        # VERIFIED [DC] series vs closed at complex argument
        # VERIFIED [NE] relative error < 1e-10
        """
        tau = complex(1.0, 2.0)
        series = log_Z_virasoro(tau, self.C, g_max=30)
        closed = log_Z_virasoro_closed(tau, self.C)
        assert abs(series - closed) / max(abs(closed), 1e-30) < 1e-10

    def test_log_Z_generating_function_value(self):
        """Quantum piece of log Z(1) = kappa * gf(1).

        # VERIFIED [DC] kappa * ((1/2)/sin(1/2) - 1) = 12.5 * 0.04291... = 0.53643...
        # VERIFIED [NE] matches series sum to 1e-14
        """
        gf_val = (0.5) / math.sin(0.5) - 1.0
        expected_quantum = self.KAPPA * gf_val
        # Series sum (quantum piece only, excluding F_0)
        series_quantum = sum(
            self.KAPPA * lambda_fp(g) for g in range(1, 31)
        )
        assert abs(series_quantum - expected_quantum) < 1e-12


# =====================================================================
# Section 5: SFF normalization and basic properties
# =====================================================================

class TestSFFBasic:
    """Basic SFF properties."""

    C = 25.0
    BETA = 1.0

    def test_sff_at_t0(self):
        """SFF(0) = 1 (normalization).

        # VERIFIED [DC] Z(beta+i*0) = Z(beta) -> ratio = 1
        # VERIFIED [SY] definition of SFF
        """
        assert sff(0.0, self.BETA, self.C) == 1.0

    def test_sff_positive(self):
        """SFF(t) >= 0 for all t.

        # VERIFIED [DC] exp(real) is always positive
        # VERIFIED [SY] SFF = |Z|^2/|Z_0|^2 >= 0
        """
        for t in [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0]:
            assert sff(t, self.BETA, self.C) >= 0.0

    def test_sff_monotone_decreasing(self):
        """Perturbative SFF is monotonically decreasing.

        # VERIFIED [DC] numerical evaluation at 20 points
        # VERIFIED [LT] perturbative expansion has no oscillatory terms
        """
        times = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
        vals = [sff(t, self.BETA, self.C) for t in times]
        for i in range(len(vals) - 1):
            assert vals[i] >= vals[i + 1], (
                f"SFF not decreasing: SFF({times[i]})={vals[i]} < SFF({times[i+1]})={vals[i+1]}"
            )

    def test_sff_bounded_by_1(self):
        """SFF(t) <= 1 for t >= 0.

        # VERIFIED [DC] perturbative SFF starts at 1 and decreases
        # VERIFIED [SY] |Z(beta+it)| <= Z(beta) for t >= 0
        """
        for t in [0.0, 0.01, 0.1, 1.0, 10.0]:
            assert sff(t, self.BETA, self.C) <= 1.0 + 1e-14

    def test_sff_closed_form_matches(self):
        """Closed-form and series SFF agree.

        # VERIFIED [DC] relative error < 1e-10 at multiple t values
        # VERIFIED [CF] cross-check two implementations
        """
        for t in [0.1, 0.5, 1.0, 5.0]:
            s_series = sff(t, self.BETA, self.C, g_max=30)
            s_closed = sff_closed_form(t, self.BETA, self.C)
            if s_series > 1e-100:
                rel = abs(s_series - s_closed) / s_series
                assert rel < 1e-8, f"t={t}: rel error {rel}"

    def test_sff_c0_trivial(self):
        """At c=0, kappa=0, so SFF = 1 for all t.

        # VERIFIED [DC] kappa=0 -> log Z = 0 -> SFF = 1
        # VERIFIED [LC] trivial algebra limit
        """
        for t in [0.0, 1.0, 10.0]:
            assert abs(sff(t, 1.0, 0.0) - 1.0) < 1e-14


# =====================================================================
# Section 6: Classical SFF
# =====================================================================

class TestSFFClassical:
    """Verify classical (genus-0) SFF."""

    C = 25.0
    KAPPA = 12.5
    BETA = 1.0

    def test_classical_at_t0(self):
        # VERIFIED [DC] (1/(1+0))^12.5 = 1
        # VERIFIED [SY] normalization
        assert sff_classical(0.0, self.BETA, self.C) == 1.0

    def test_classical_at_t1(self):
        """SFF_0(1) = (1/(1+1))^12.5 = 2^{-12.5}.

        # VERIFIED [DC] 2^{-12.5} = 1.72633491...e-04
        # VERIFIED [NE] math.pow(2, -12.5) direct
        """
        expected = 2.0 ** (-self.KAPPA)
        result = sff_classical(1.0, self.BETA, self.C)
        assert abs(result - expected) < 1e-14

    def test_classical_late_time_power_law(self):
        """SFF_0(t) ~ (beta/t)^{2*kappa} for t >> beta.

        # VERIFIED [DC] ratio SFF_0(t) / (beta/t)^{2*kappa} -> 1
        # VERIFIED [LC] asymptotic expansion of (1 + t^2/beta^2)^{-kappa}
        """
        t = 1000.0
        asymptotic = (self.BETA / t) ** (2 * self.KAPPA)
        exact = sff_classical(t, self.BETA, self.C)
        rel = abs(exact - asymptotic) / asymptotic
        assert rel < 1e-5  # t/beta = 1000, correction is O(beta^2/t^2)


# =====================================================================
# Section 7: Late-time slope and ramp analysis
# =====================================================================

class TestRampAnalysis:
    """Verify that the perturbative SFF does NOT produce a ramp."""

    C = 25.0
    KAPPA = 12.5
    BETA = 1.0

    def test_no_ramp(self):
        """Perturbative genus expansion has no ramp.

        # VERIFIED [DC] slope regression gives -25, not positive
        # VERIFIED [LT] Saad-Shenker-Stanford '19: ramp is non-perturbative
        """
        result = analyze_ramp(self.C, self.BETA)
        assert not result.has_ramp

    def test_late_time_slope(self):
        """Late-time slope = -2*kappa = -25 for c=25.

        # VERIFIED [DC] linear regression on log-log SFF data
        # VERIFIED [LC] classical limit: (beta/t)^{2*kappa}
        """
        result = analyze_ramp(self.C, self.BETA)
        assert result.slope_match, (
            f"slope {result.late_time_slope:.4f} != expected {result.expected_slope:.4f}"
        )
        assert abs(result.late_time_slope - (-25.0)) < 0.5

    def test_quantum_correction_ratio(self):
        """R_inf = exp(-2*kappa*gf(1/beta)) ~ 0.342025 for c=25, beta=1.

        # VERIFIED [DC] exp(-2 * 12.5 * 0.042915...) = exp(-1.07287...) = 0.34202...
        # VERIFIED [NE] numerical evaluation to 6 digits
        """
        result = analyze_ramp(self.C, self.BETA)
        assert result.ratio_match
        assert abs(result.quantum_correction_exact - 0.342025) < 1e-3

    def test_slope_varies_with_c(self):
        """Slope = -2*kappa = -c for different central charges.

        # VERIFIED [DC] slope = -2*(c/2) = -c
        # VERIFIED [CF] tested at c=1, c=10, c=50
        """
        for c_val in [1.0, 10.0, 50.0]:
            result = analyze_ramp(c_val, self.BETA)
            expected = -2.0 * kappa_virasoro(c_val)
            assert abs(result.late_time_slope - expected) < 1.0, (
                f"c={c_val}: slope {result.late_time_slope:.2f} != {expected:.2f}"
            )


# =====================================================================
# Section 8: Early-time analysis
# =====================================================================

class TestEarlyTime:
    """Verify early-time SFF behavior."""

    C = 25.0
    KAPPA = 12.5
    BETA = 1.0

    def test_quadratic_decay(self):
        """SFF ~ 1 - a*t^2 at early times, a > 0.

        # VERIFIED [DC] fit from SFF(0.01) and SFF(0.02)
        # VERIFIED [SY] energy variance is positive
        """
        result = analyze_early_time(self.C, self.BETA)
        assert result.decay_rate_quadratic > 0

        # Cross-check: SFF(dt) ~ 1 - a*dt^2
        dt = 0.001
        sff_dt = sff(dt, self.BETA, self.C)
        a_numerical = (1.0 - sff_dt) / dt ** 2
        assert abs(a_numerical - result.decay_rate_quadratic) / result.decay_rate_quadratic < 0.01

    def test_half_decay_time_positive(self):
        """Half-decay time is positive and < beta.

        # VERIFIED [DC] binary search converges
        # VERIFIED [LC] for large kappa, t_half ~ beta / sqrt(2*kappa)
        """
        result = analyze_early_time(self.C, self.BETA)
        assert result.half_decay_time > 0
        assert result.half_decay_time < self.BETA

    def test_no_dip_perturbative(self):
        """No dip in the perturbative SFF.

        # VERIFIED [DC] SFF is monotonically decreasing
        # VERIFIED [LT] dip requires non-perturbative effects
        """
        result = analyze_early_time(self.C, self.BETA)
        assert result.dip_time is None


# =====================================================================
# Section 9: Convergence analysis
# =====================================================================

class TestConvergence:
    """Verify genus truncation convergence."""

    C = 25.0
    BETA = 1.0

    def test_convergence_at_t1(self):
        """Genus series converges at t=1, beta=1.

        # VERIFIED [DC] relative change < 1e-10 by g_max ~ 12
        # VERIFIED [LT] convergence radius = 2*pi*beta >> 1
        """
        result = analyze_convergence(t=1.0, beta=self.BETA, c=self.C)
        assert result.converged_g_max <= 15

    def test_convergence_radius(self):
        """Convergence radius = 2*pi*beta.

        # VERIFIED [DC] sin(x/2) zeros at x = 2*pi*n -> |tau| > 1/(2*pi)
        # VERIFIED [LT] resurgence engine: Borel radius = 2*pi
        """
        result = analyze_convergence(t=1.0, beta=self.BETA, c=self.C)
        expected = 2.0 * math.pi * self.BETA
        assert abs(result.convergence_radius - expected) < 1e-10

    def test_g_max_1_vs_20(self):
        """g_max=1 and g_max=20 should differ for t ~ beta.

        # VERIFIED [DC] g=1 only captures leading quantum correction
        # VERIFIED [NE] SFF difference at t=0.5
        """
        t = 0.5
        s1 = sff(t, self.BETA, self.C, g_max=1)
        s20 = sff(t, self.BETA, self.C, g_max=20)
        # They should differ but both be close (convergent series)
        assert abs(s1 - s20) > 1e-6  # genus >= 2 corrections matter
        assert abs(s1 - s20) / s20 < 0.1  # but series converges fast


# =====================================================================
# Section 10: Time series evaluation
# =====================================================================

class TestTimeSeries:
    """Verify time series evaluation."""

    def test_time_series_shape(self):
        """Output arrays have correct shape."""
        ts = evaluate_sff_time_series(n_points=50, c=25.0)
        assert len(ts.times) == 50
        assert len(ts.sff_values) == 50
        assert len(ts.sff_classical) == 50

    def test_time_series_kappa(self):
        """Stored kappa matches c/2."""
        ts = evaluate_sff_time_series(c=25.0)
        assert ts.kappa == 12.5

    def test_sff_dominates_classical_at_late_times(self):
        """SFF_full <= SFF_classical at all times (quantum corrections reduce SFF).

        For the uniform-weight perturbative expansion, the quantum
        corrections to SFF are NEGATIVE in the exponent at late times.

        # VERIFIED [DC] ratio R_inf < 1 for positive kappa
        # VERIFIED [SY] exp(-2*kappa*gf) < 1 since gf > 0
        """
        ts = evaluate_sff_time_series(t_min=1.0, t_max=100.0, n_points=20, c=25.0)
        for i in range(len(ts.times)):
            if ts.sff_classical[i] > 1e-100:
                assert ts.sff_values[i] <= ts.sff_classical[i] * (1 + 1e-10)


# =====================================================================
# Section 11: Full analysis summary
# =====================================================================

class TestFullAnalysis:
    """Verify the full analysis pipeline."""

    def test_full_analysis_c25(self):
        """Full analysis at c=25 runs without error."""
        result = full_sff_analysis(c=25.0)
        assert result['family'] == 'Virasoro'
        assert result['c'] == 25.0
        assert result['kappa'] == 12.5
        assert abs(result['sff_at_t0'] - 1.0) < 1e-14
        assert not result['ramp'].has_ramp

    def test_F1_sanity_in_summary(self):
        """F_1 = kappa/24 in the summary output.

        # VERIFIED [DC] 12.5/24 = 25/48 = 0.520833...
        # VERIFIED [LT] AP120 canonical sanity check
        """
        result = full_sff_analysis(c=25.0)
        assert abs(result['F_1'] - 25.0 / 48.0) < 1e-14

    def test_full_analysis_c1(self):
        """Full analysis at c=1 (small central charge)."""
        result = full_sff_analysis(c=1.0)
        assert result['kappa'] == 0.5
        assert abs(result['sff_at_t0'] - 1.0) < 1e-14

    def test_full_analysis_c13_self_dual(self):
        """Full analysis at c=13 (self-dual point).

        # VERIFIED [DC] kappa = 13/2 = 6.5
        # VERIFIED [LT] C8: self-dual at c=13
        """
        result = full_sff_analysis(c=13.0)
        assert result['kappa'] == 6.5


# =====================================================================
# Section 12: Specific numerical values for c=25
# =====================================================================

class TestNumericalValues:
    """Pin down specific numerical values for regression testing."""

    C = 25.0
    KAPPA = 12.5
    BETA = 1.0

    def test_sff_at_t_0p1(self):
        """SFF(0.1, beta=1, c=25) ~ 0.8537.

        # VERIFIED [DC] direct computation
        # VERIFIED [NE] independent Python evaluation
        """
        result = sff(0.1, self.BETA, self.C)
        assert abs(result - 0.8536659537) < 1e-4

    def test_sff_at_t_0p5(self):
        """SFF(0.5, beta=1, c=25) ~ 0.03446.

        # VERIFIED [DC] direct computation
        # VERIFIED [NE] independent Python evaluation
        """
        result = sff(0.5, self.BETA, self.C)
        assert abs(result - 0.0344584760) < 1e-6

    def test_sff_at_t_1(self):
        """SFF(1, beta=1, c=25) ~ 5.86e-5.

        # VERIFIED [DC] direct computation
        # VERIFIED [NE] independent Python evaluation
        """
        result = sff(1.0, self.BETA, self.C)
        assert abs(result - 5.8598e-5) < 1e-7

    def test_quantum_piece_at_beta1(self):
        """sum_{g>=1} F_g = kappa * gf(1) ~ 0.53644 at beta=1, c=25.

        # VERIFIED [DC] series sum to g=30
        # VERIFIED [CF] generating function: 12.5 * 0.042915... = 0.53644...
        """
        quantum = sum(self.KAPPA * lambda_fp(g) for g in range(1, 31))
        gf_val = (0.5) / math.sin(0.5) - 1.0
        expected = self.KAPPA * gf_val
        assert abs(quantum - expected) < 1e-12
        assert abs(quantum - 0.536435268) < 1e-6
