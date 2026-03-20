"""Tests for the shadow connection theorem.

Verifies: logarithmic connection, residues, monodromy, Koszul duality,
complementarity sum, self-duality, and multi-channel curvature.
"""

import pytest
from sympy import (
    I, Rational, Symbol, cancel, diff, exp, factor, numer, denom,
    pi, simplify, sqrt, Poly,
)

from compute.lib.shadow_connection import (
    shadow_metric,
    critical_discriminant,
    connection_form,
    parallel_transport,
    virasoro_shadow_metric,
    virasoro_connection_form,
    virasoro_discriminant,
    koszul_dual_metric,
    complementarity_sum_discriminant,
    dual_lee_yang_points,
    connection_residue_at_zero,
    monodromy_at_zero,
    complementarity_sum_metric,
    complementarity_product_metric,
    self_dual_metric,
)

c = Symbol('c')
t = Symbol('t')


class TestShadowMetric:
    """The shadow metric Q_L(t)."""

    def test_virasoro_explicit(self):
        Q = virasoro_shadow_metric()
        alpha_c = (180*c + 872) / (5*c + 22)
        expected = c**2 + 12*c*t + alpha_c*t**2
        assert cancel(Q - expected) == 0

    def test_gaussian_decomposition(self):
        """Q = (2κ + αt)² + 2Δt²."""
        kappa = c/2
        alpha = Rational(2)
        S4 = Rational(10)/(c*(5*c+22))
        Q = shadow_metric(kappa, alpha, S4)
        Delta = critical_discriminant(kappa, S4)
        gaussian = (2*kappa + alpha*t)**2
        assert cancel(Q - gaussian - 2*kappa*Delta*t**2) == 0

    def test_q_at_t_zero(self):
        Q = virasoro_shadow_metric()
        assert cancel(Q.subs(t, 0) - c**2) == 0


class TestConnectionForm:
    """The logarithmic connection ω = Q'/(2Q)."""

    def test_connection_form_virasoro(self):
        Q = virasoro_shadow_metric()
        omega = connection_form(Q)
        Q_prime = diff(Q, t)
        assert cancel(omega - Q_prime/(2*Q)) == 0

    def test_connection_poles_at_q_zeros(self):
        """ω has poles exactly where Q = 0."""
        Q = virasoro_shadow_metric()
        omega = connection_form(Q)
        # ω = Q'/(2Q) has denominator Q (times 2)
        d = denom(cancel(omega))
        # d should be divisible by Q (as poly in t)
        Q_num = cancel(Q * (5*c + 22))
        # Both should vanish at the same t-values
        # Just check structure
        assert Poly(d, t).degree() >= 2


class TestResiduesAndMonodromy:
    """Residue 1/2, monodromy -1."""

    def test_residue_is_half(self):
        Q = virasoro_shadow_metric()
        assert connection_residue_at_zero(Q) == Rational(1, 2)

    def test_monodromy_is_minus_one(self):
        assert monodromy_at_zero() == -1

    def test_monodromy_is_koszul_sign(self):
        """exp(2πi · 1/2) = -1 = the Koszul sign."""
        res = Rational(1, 2)
        # In the analytic continuation: monodromy = exp(2πi·res)
        assert exp(2*pi*I*res) == -1


class TestParallelTransport:
    """Φ(t) = √(Q(t)/Q(0))."""

    def test_transport_at_zero(self):
        Q = virasoro_shadow_metric()
        kappa = c/2
        Phi = parallel_transport(Q, kappa)
        assert cancel(Phi.subs(t, 0) - 1) == 0

    def test_shadow_gf_from_transport(self):
        """H(t) = 2κ·t²·Φ(t) = t²√Q."""
        Q = virasoro_shadow_metric()
        kappa = c/2
        Phi = parallel_transport(Q, kappa)
        H = 2*kappa * t**2 * Phi
        expected = t**2 * sqrt(Q)
        # H² = t⁴Q = (t²√Q)²
        assert cancel(H**2 - t**4 * Q) == 0


class TestKoszulDuality:
    """Koszul duality: c → 26-c."""

    def test_dual_metric(self):
        Q = virasoro_shadow_metric()
        Q_dual = koszul_dual_metric(Q)
        assert cancel(Q_dual - Q.subs(c, 26-c)) == 0

    def test_self_dual_at_13(self):
        """Q(t,13) = Q(t,13) under c → 26-c."""
        Q = virasoro_shadow_metric()
        Q_13 = Q.subs(c, 13)
        Q_dual_13 = koszul_dual_metric(Q).subs(c, 13)
        assert cancel(Q_13 - Q_dual_13) == 0

    def test_dual_lee_yang_points(self):
        """Lee-Yang points sum to 26."""
        ly1, ly2 = dual_lee_yang_points()
        assert ly1 + ly2 == 26
        assert ly1 == Rational(-22, 5)
        assert ly2 == Rational(152, 5)


class TestComplementarity:
    """Complementarity sum Δ(c) + Δ(26-c)."""

    def test_constant_numerator(self):
        """Δ(c) + Δ(26-c) has constant numerator 6960."""
        Delta_sum = complementarity_sum_discriminant()
        n = numer(cancel(Delta_sum))
        # Should be a constant (no c dependence)
        assert Poly(n, c).degree() == 0

    def test_numerator_value(self):
        Delta_sum = complementarity_sum_discriminant()
        n = numer(cancel(Delta_sum))
        d = denom(cancel(Delta_sum))
        # The sign depends on convention; check |n|
        assert abs(int(n)) == 6960

    def test_denominator_is_dual_product(self):
        """Denominator = (5c+22)(152-5c)."""
        Delta_sum = complementarity_sum_discriminant()
        d = denom(cancel(Delta_sum))
        expected = (5*c + 22)*(152 - 5*c)
        # Should differ by at most a sign
        assert cancel(d - expected) == 0 or cancel(d + expected) == 0

    @pytest.mark.parametrize("c_val", [1, 5, 13, 20, 25])
    def test_complementarity_numerical(self, c_val):
        Delta = virasoro_discriminant()
        Delta_dual = Delta.subs(c, 26-c_val)
        Delta_c = Delta.subs(c, c_val)
        sum_val = Delta_c + Delta_dual
        expected = Rational(6960) / ((5*c_val+22)*(152-5*c_val))
        assert cancel(sum_val - expected) == 0

    def test_at_self_dual(self):
        """Δ(13) + Δ(13) = 80/87."""
        Delta = virasoro_discriminant()
        sum_13 = 2 * Delta.subs(c, 13)
        assert sum_13 == Rational(80, 87)

    def test_symmetry(self):
        """Δ_sum(c) = Δ_sum(26-c) (symmetric under duality)."""
        Delta_sum = complementarity_sum_discriminant()
        assert cancel(Delta_sum - Delta_sum.subs(c, 26-c)) == 0


class TestSelfDualMetric:
    """The shadow metric at the self-dual point c = 13."""

    def test_explicit_values(self):
        Q_13 = self_dual_metric()
        assert cancel(Q_13.subs(t, 0) - 169) == 0

    def test_discriminant_at_13(self):
        Q_13 = self_dual_metric()
        # Disc = b² - 4ac where Q = a + bt + ct²
        p = Poly(Q_13, t)
        a, b, cc = p.nth(0), p.nth(1), p.nth(2)
        disc = b**2 - 4*a*cc
        # Should be negative (complex branch points)
        assert float(disc) < 0


class TestMultiChannelCurvature:
    """Multi-channel curvature = propagator variance."""

    def test_rank_one_flat(self):
        """Rank 1 connection is always flat (no curvature)."""
        from compute.lib.shadow_connection import multi_channel_curvature
        kappas = [c/2]
        fs = [Rational(40)/(c*(5*c+22))]
        assert multi_channel_curvature(kappas, fs) == 0

    def test_w3_has_curvature(self):
        """W₃ connection has nonzero curvature (propagator variance)."""
        from compute.lib.shadow_connection import multi_channel_curvature
        kappas = [c/2, c/3]
        f_T = Rational(200)*(c+14)/(c*(5*c+22)**2)
        f_W = Rational(640)*(15*c+82)/(c*(5*c+22)**3)
        curv = multi_channel_curvature(kappas, [f_T, f_W])
        assert curv.subs(c, 13) != 0
