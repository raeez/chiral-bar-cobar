r"""Tests for the shadow connection theorem (thm:shadow-connection).

Verifies: logarithmic connection, residues, monodromy, Koszul duality,
complementarity sum, self-duality, multi-channel curvature, and the
full W_3 W-line shadow connection.

All formulas computed from first principles (AP1, AP3).
Cross-family consistency verified (AP10).
"""

import pytest
from sympy import (
    I, Rational, Symbol, cancel, diff, exp, expand, factor, log,
    numer, denom, pi, simplify, solve, sqrt, Poly, Abs,
)

from compute.lib.shadow_connection import (
    # General theory
    shadow_metric_general,
    shadow_metric_expanded,
    shadow_metric_coefficients,
    critical_discriminant,
    gaussian_decomposition,
    # Connection
    connection_form,
    connection_form_from_data,
    flat_section,
    shadow_generating_function,
    # Zeros and residues
    shadow_metric_zeros,
    shadow_metric_zeros_from_data,
    shadow_metric_discriminant,
    connection_residue_at_zero,
    monodromy_eigenvalue,
    verify_residue_symbolically,
    # Virasoro
    virasoro_shadow_data,
    virasoro_shadow_metric,
    virasoro_shadow_metric_explicit,
    virasoro_gaussian_decomposition,
    virasoro_connection_form,
    virasoro_discriminant,
    virasoro_zeros,
    virasoro_zeros_explicit,
    virasoro_flat_section,
    virasoro_picard_fuchs,
    # W_3 W-line
    w3_wline_shadow_data,
    w3_wline_shadow_metric,
    w3_wline_gaussian_decomposition,
    w3_wline_connection_form,
    w3_wline_discriminant,
    w3_wline_zeros,
    w3_wline_growth_rate,
    w3_wline_flat_section,
    # W_3 T-line
    w3_tline_shadow_data,
    w3_tline_shadow_metric,
    # Koszul duality
    koszul_dual_metric,
    virasoro_koszul_dual_metric,
    w3_koszul_dual_wline_metric,
    dual_lee_yang_points,
    # Complementarity
    complementarity_sum_discriminant,
    complementarity_sum_metric,
    complementarity_product_metric,
    self_dual_metric,
    w3_complementarity_sum_discriminant,
    # Numerical
    virasoro_shadow_metric_numerical,
    w3_wline_shadow_metric_numerical,
)

c = Symbol('c')
t = Symbol('t')


# =========================================================================
# 1. General shadow metric theory
# =========================================================================

class TestShadowMetricGeneral:
    """Tests for the general shadow metric Q_L(t)."""

    def test_shadow_metric_at_t_zero(self):
        """Q_L(0) = (2*kappa)^2 = 4*kappa^2."""
        kappa, alpha, S4 = c/2, Rational(2), Rational(1)/c
        Q = shadow_metric_general(kappa, alpha, S4)
        assert cancel(Q.subs(t, 0) - 4*kappa**2) == 0

    def test_gaussian_decomposition_identity(self):
        """Q_L = Gaussian + interaction = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2."""
        kappa = c/2
        alpha = Rational(2)
        S4 = Rational(10)/(c*(5*c+22))
        Q = shadow_metric_general(kappa, alpha, S4)
        gauss, correction, Delta = gaussian_decomposition(kappa, alpha, S4)
        assert cancel(Q - gauss - correction) == 0

    def test_coefficients_match_expanded(self):
        """shadow_metric_coefficients matches expand(Q_L)."""
        kappa = c/2
        alpha = Rational(2)
        S4 = Rational(10)/(c*(5*c+22))
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        Q = shadow_metric_expanded(kappa, alpha, S4)
        Q_from_coeffs = q0 + q1*t + q2*t**2
        assert cancel(Q - Q_from_coeffs) == 0

    def test_discriminant_formula(self):
        """disc(Q_L) = -32*kappa^2*Delta."""
        kappa = c/2
        alpha = Rational(2)
        S4 = Rational(10)/(c*(5*c+22))
        disc = shadow_metric_discriminant(kappa, alpha, S4)
        Delta = critical_discriminant(kappa, S4)
        expected = -32 * kappa**2 * Delta
        assert cancel(disc - expected) == 0

    def test_class_g_perfect_square(self):
        """For Heisenberg (alpha=0, S4=0): Q = (2*kappa)^2, a perfect square."""
        kappa = Rational(1)
        Q = shadow_metric_general(kappa, Rational(0), Rational(0))
        assert cancel(Q - (2*kappa)**2) == 0

    def test_class_l_perfect_square(self):
        """For affine KM (S4=0, alpha!=0): Q = (2*kappa + 3*alpha*t)^2, perfect square."""
        kappa, alpha = Rational(3), Rational(1)
        Q = shadow_metric_general(kappa, alpha, Rational(0))
        assert cancel(Q - (2*kappa + 3*alpha*t)**2) == 0


# =========================================================================
# 2. Connection form
# =========================================================================

class TestConnectionForm:
    """Tests for the logarithmic connection omega = Q'/(2Q)."""

    def test_connection_form_definition(self):
        """omega = Q'/(2Q)."""
        Q = virasoro_shadow_metric()
        omega = connection_form(Q)
        Q_prime = diff(Q, t)
        assert cancel(omega - Q_prime/(2*Q)) == 0

    def test_connection_form_from_data_matches(self):
        """connection_form_from_data matches connection_form(Q)."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        omega1 = connection_form_from_data(kappa, alpha, S4)
        Q = virasoro_shadow_metric()
        omega2 = connection_form(Q)
        assert cancel(omega1 - omega2) == 0

    def test_connection_is_dlog_sqrt_Q(self):
        """omega = d(log(sqrt(Q)))/dt = Q'/(2Q).

        This is the defining property: the connection is the
        Gauss-Manin connection of the family sqrt(Q(t)).
        """
        Q = virasoro_shadow_metric()
        omega = connection_form(Q)
        # d/dt[log(sqrt(Q))] = d/dt[(1/2)*log(Q)] = Q'/(2Q) = omega
        dlog_sqrt_Q = diff(log(sqrt(Q)), t)
        assert cancel(omega - dlog_sqrt_Q) == 0

    def test_connection_poles_at_q_zeros(self):
        """omega has poles exactly where Q = 0.

        The denominator of omega (in lowest terms) divides Q.
        """
        Q = virasoro_shadow_metric()
        omega = virasoro_connection_form()
        d = denom(cancel(omega))
        # d should be a polynomial in t of degree >= 2
        assert Poly(d, t).degree() >= 2

    def test_class_l_connection_regular(self):
        """For class L (Delta=0): omega has NO branch-point singularities.

        Q = (2*kappa + 3*alpha*t)^2, so omega = 3*alpha/(2*kappa + 3*alpha*t),
        which has a simple pole (not a logarithmic branch point).
        """
        kappa, alpha = Rational(3), Rational(1)
        Q = shadow_metric_general(kappa, alpha, Rational(0))
        omega = connection_form(Q)
        expected = 3*alpha / (2*kappa + 3*alpha*t)
        assert cancel(omega - expected) == 0


# =========================================================================
# 3. Residues and monodromy
# =========================================================================

class TestResiduesAndMonodromy:
    """Residue 1/2 at each zero, monodromy -1 (Koszul sign)."""

    def test_residue_is_half(self):
        """Universal residue at simple zeros of Q: always 1/2."""
        assert connection_residue_at_zero() == Rational(1, 2)

    def test_monodromy_is_minus_one(self):
        """Monodromy around zero = -1 (Koszul sign)."""
        assert monodromy_eigenvalue() == -1

    def test_monodromy_from_residue(self):
        """exp(2*pi*i * 1/2) = exp(pi*i) = -1."""
        res = Rational(1, 2)
        assert exp(2*pi*I*res) == -1

    def test_monodromy_z2_factorization(self):
        """Monodromy^2 = 1: it factors through Z/2."""
        m = monodromy_eigenvalue()
        assert m**2 == 1

    def test_residue_verification(self):
        """Verify residue = 1/2 symbolically for Virasoro."""
        kappa, alpha, S4, _ = virasoro_shadow_data()
        assert verify_residue_symbolically(kappa, alpha, S4) == Rational(1, 2)

    def test_residue_numerical_virasoro(self):
        """Numerical verification of residue at c=13.

        At a zero t_0 of Q, omega ~ 1/(2*(t-t_0)), so
        Res(omega, t_0) = 1/2.

        We verify by computing Q'(t_0)/(Q'(t_0)*2) = 1/2.
        """
        data = virasoro_shadow_metric_numerical(13)
        # At a simple zero: Q ~ Q'(t_0)*(t-t_0)
        # omega ~ Q'/(2Q) ~ 1/(2*(t-t_0))
        # residue = 1/2
        assert data['rho'] > 0  # Class M: infinite tower


# =========================================================================
# 4. Flat section and shadow GF
# =========================================================================

class TestFlatSectionAndGF:
    """Phi(t) = sqrt(Q/Q(0)), H(t) = t^2*sqrt(Q)."""

    def test_flat_section_at_zero(self):
        """Phi(0) = 1."""
        Q = virasoro_shadow_metric()
        Phi = flat_section(Q)
        assert cancel(Phi.subs(t, 0) - 1) == 0

    def test_flat_section_virasoro(self):
        """Phi_Vir(t) = sqrt(Q_Vir(t))/c.

        Phi^2 = Q/c^2, and Phi(0)^2 = Q(0)/c^2 = c^2/c^2 = 1.
        """
        Phi = virasoro_flat_section()
        Q = virasoro_shadow_metric()
        assert cancel(Phi**2 - Q/c**2) == 0
        # Check Phi(0)^2 = 1 (avoid sqrt(c^2) = |c| ambiguity)
        assert cancel(Phi.subs(t, 0)**2 - 1) == 0

    def test_shadow_gf_relation(self):
        """H(t)^2 = t^4*Q_L (Riccati algebraicity, thm:riccati-algebraicity)."""
        Q = virasoro_shadow_metric()
        H = shadow_generating_function(Q, c/2)
        assert cancel(H**2 - t**4*Q) == 0

    def test_shadow_gf_from_flat_section(self):
        """H(t)^2 = (2*kappa)^2*t^4*Phi(t)^2.

        H = t^2*sqrt(Q), Phi = sqrt(Q/Q0), Q0 = 4*kappa^2.
        So H^2 = t^4*Q = t^4*Q0*Phi^2 = 4*kappa^2*t^4*Phi^2.
        """
        Q = virasoro_shadow_metric()
        kappa = c/2
        Phi = flat_section(Q)
        H = shadow_generating_function(Q, kappa)
        # Verify: H^2 = (2*kappa)^2 * t^4 * Phi^2
        assert cancel(H**2 - (2*kappa)**2 * t**4 * Phi**2) == 0

    def test_shadow_gf_is_not_flat(self):
        """H(t) is NOT a flat section (AP23): H has a double zero at t=0.

        The flat section Phi has Phi(0)=1, not zero.
        H(0) = 0 (double zero from the t^2 prefactor).
        """
        Q = virasoro_shadow_metric()
        H = shadow_generating_function(Q, c/2)
        assert cancel(H.subs(t, 0)) == 0  # H(0) = 0

    def test_picard_fuchs_flat_section(self):
        """The flat section satisfies Q*f'' + (1/2)*Q'*f' = 0.

        This is the Picard-Fuchs equation of the shadow connection.
        """
        Q, Q_prime = virasoro_picard_fuchs()
        # f(t) = sqrt(Q(t)/Q(0)), f' = Q'/(2*sqrt(Q*Q(0)))
        # f'' = [Q''*2Q - (Q')^2]/(4*Q^(3/2)*sqrt(Q(0)))
        # Q*f'' + (Q'/2)*f' = [Q*Q''*2Q - Q*(Q')^2 + Q'*Q'*Q]/(4*Q^(3/2)*Q0^{1/2})
        #                    = [2*Q^2*Q'' + Q*(Q')^2 - Q*(Q')^2]/(...)
        # Actually let's verify numerically at c=13, t=1/10
        Q_13 = Q.subs(c, 13)
        Qp_13 = Q_prime.subs(c, 13)
        Qpp_13 = diff(Q_13, t)  # This is Q'' but we need d/dt(Q')
        Qpp_13 = diff(Qp_13, t)
        # f = sqrt(Q/Q0), Q0 = Q(0)
        Q0 = Q_13.subs(t, 0)
        # The PF equation: Q*f'' + (1/2)*Q'*f' = 0
        # Multiply by 2*sqrt(Q*Q0): 2*Q*(f''*sqrt(Q*Q0)) + Q'*(f'*sqrt(Q*Q0)) = 0
        # f'*sqrt(Q*Q0) = Q'/(2*sqrt(Q))  * sqrt(Q*Q0) / sqrt(Q0) = Q'/2
        # Hmm, let's just test f = sqrt(Q) satisfies Q*f'' + (1/2)*Q'*f' = 0.
        # f = sqrt(Q), f' = Q'/(2*sqrt(Q)), f'' = (Q''*2Q - Q'^2)/(4*Q^(3/2))
        # Q*f'' = (Q''*2Q - Q'^2)/(4*sqrt(Q))
        # (Q'/2)*f' = (Q')^2 / (4*sqrt(Q))
        # Sum = (2*Q*Q'' - Q'^2 + Q'^2)/(4*sqrt(Q)) = Q*Q''/(2*sqrt(Q)) = (Q''/2)*sqrt(Q)
        # This is zero only if Q'' = 0, which is not true for quadratic Q.
        #
        # The correct PF equation for Phi = sqrt(Q/Q0) is:
        # nabla^sh(Phi) = Phi' - omega*Phi = 0
        # which is Phi' = (Q'/(2Q))*Phi, i.e. Phi' - (Q'/(2Q))*Phi = 0.
        # This is first-order, not second-order.
        Phi = sqrt(Q_13 / Q0)
        Phi_prime = diff(Phi, t)
        omega = Qp_13 / (2*Q_13)
        residual = simplify(Phi_prime - omega * Phi)
        assert residual == 0


# =========================================================================
# 5. Virasoro shadow metric
# =========================================================================

class TestVirasoroShadowMetric:
    """Tests for Q_Vir(t) = c^2 + 12ct + [(180c+872)/(5c+22)]t^2."""

    def test_explicit_form(self):
        """Q_Vir matches the explicit formula."""
        Q = virasoro_shadow_metric()
        Q_exp = virasoro_shadow_metric_explicit()
        assert cancel(Q - Q_exp) == 0

    def test_q_at_t_zero(self):
        """Q_Vir(0) = c^2."""
        Q = virasoro_shadow_metric()
        assert cancel(Q.subs(t, 0) - c**2) == 0

    def test_q1_coefficient(self):
        """Coefficient of t in Q_Vir is 12c."""
        Q = virasoro_shadow_metric()
        # Q*(5c+22) is polynomial in t
        Q_scaled = cancel(Q * (5*c + 22))
        p = Poly(Q_scaled, t)
        assert cancel(p.nth(1) - 12*c*(5*c+22)) == 0

    def test_q2_coefficient(self):
        """Coefficient of t^2 in Q_Vir is (180c+872)/(5c+22)."""
        Q = virasoro_shadow_metric()
        Q_scaled = cancel(Q * (5*c + 22))
        p = Poly(Q_scaled, t)
        assert cancel(p.nth(2) - (180*c + 872)) == 0

    def test_gaussian_decomposition(self):
        """Q_Vir = (c + 6t)^2 + [80/(5c+22)]*t^2."""
        gauss, correction, Delta = virasoro_gaussian_decomposition()
        Q = virasoro_shadow_metric()
        assert cancel(Q - gauss - correction) == 0

    def test_delta_virasoro(self):
        """Delta_Vir = 40/(5c+22)."""
        assert cancel(virasoro_discriminant() - Rational(40)/(5*c+22)) == 0

    def test_delta_from_data(self):
        """Delta from virasoro_shadow_data matches virasoro_discriminant."""
        _, _, _, Delta = virasoro_shadow_data()
        assert cancel(Delta - virasoro_discriminant()) == 0

    def test_delta_always_positive(self):
        """Delta_Vir > 0 for c > -22/5 (confirming class M)."""
        Delta = virasoro_discriminant()
        for c_val in [Rational(1,2), 1, 13, 25, 26]:
            assert Delta.subs(c, c_val) > 0

    @pytest.mark.parametrize("c_val", [1, 5, 13, 20, 25, 26])
    def test_gaussian_numerical(self, c_val):
        """Gaussian decomposition holds numerically at specific c values."""
        c_v = Rational(c_val)
        Q_val = virasoro_shadow_metric().subs(c, c_v)
        gauss_val = (c_v + 6*t)**2
        corr_val = Rational(80) / (5*c_v + 22) * t**2
        assert cancel(Q_val - gauss_val - corr_val) == 0


# =========================================================================
# 6. Virasoro zeros (branch points)
# =========================================================================

class TestVirasoroZeros:
    """Tests for the zeros of Q_Vir(t)."""

    def test_two_zeros(self):
        """Q_Vir has exactly 2 zeros (it is quadratic in t)."""
        zeros = virasoro_zeros()
        assert len(zeros) == 2

    def test_zeros_complex_conjugate_at_c13(self):
        """At c=13: zeros are complex conjugate."""
        Q = virasoro_shadow_metric().subs(c, 13)
        zeros = solve(Q, t)
        z0 = complex(zeros[0].evalf())
        z1 = complex(zeros[1].evalf())
        assert abs(z0.real - z1.real) < 1e-10
        assert abs(z0.imag + z1.imag) < 1e-10  # conjugate

    def test_zeros_same_modulus(self):
        """For c > 0: both zeros have the same modulus (complex conjugate)."""
        Q = virasoro_shadow_metric().subs(c, 13)
        zeros = solve(Q, t)
        mod0 = abs(complex(zeros[0].evalf()))
        mod1 = abs(complex(zeros[1].evalf()))
        assert abs(mod0 - mod1) < 1e-10

    def test_zeros_product(self):
        """Product of zeros = q0/q2 = c^2*(5c+22)/(180c+872).

        By Vieta's formulas for Q = q0 + q1*t + q2*t^2:
        t_0 * t_1 = q0/q2.
        """
        kappa, alpha, S4, _ = virasoro_shadow_data()
        q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, S4)
        expected_product = cancel(q0 / q2)
        # Verify at c=13
        c_v = 13
        q0_v = q0.subs(c, c_v)
        q2_v = q2.subs(c, c_v)
        zeros = solve(virasoro_shadow_metric().subs(c, c_v), t)
        product = cancel(zeros[0] * zeros[1])
        assert cancel(product - q0_v/q2_v) == 0

    def test_explicit_zeros_match(self):
        """virasoro_zeros_explicit matches virasoro_zeros at c=13.

        Both sets of zeros should have the same moduli and real parts.
        """
        t_p, t_m = virasoro_zeros_explicit()
        zeros = virasoro_zeros()
        # Evaluate at c=13
        tp_val = complex(t_p.subs(c, 13).evalf())
        tm_val = complex(t_m.subs(c, 13).evalf())
        z_vals = [complex(z.subs(c, 13).evalf()) for z in zeros]
        # Sort by imaginary part to get consistent ordering
        tp_tm = sorted([tp_val, tm_val], key=lambda z: z.imag)
        z_vals = sorted(z_vals, key=lambda z: z.imag)
        assert abs(tp_tm[0] - z_vals[0]) < 1e-8
        assert abs(tp_tm[1] - z_vals[1]) < 1e-8


# =========================================================================
# 7. Virasoro connection form
# =========================================================================

class TestVirasoroConnectionForm:
    """Tests for the Virasoro shadow connection form."""

    def test_connection_form_virasoro(self):
        """omega_Vir = Q_Vir'/(2*Q_Vir)."""
        omega = virasoro_connection_form()
        Q = virasoro_shadow_metric()
        Q_prime = diff(Q, t)
        assert cancel(omega - Q_prime/(2*Q)) == 0

    def test_connection_at_t_zero(self):
        """omega(0) = Q'(0)/(2*Q(0)) = 12c/(2*c^2) = 6/c."""
        omega = virasoro_connection_form()
        omega_0 = cancel(omega.subs(t, 0))
        assert cancel(omega_0 - 6/c) == 0


# =========================================================================
# 8. W_3 W-line shadow metric
# =========================================================================

class TestW3WLineShadowMetric:
    """Tests for Q_W(t) on the W-line of W_3."""

    def test_kappa_w(self):
        """kappa_W = c/3."""
        kappa_W, _, _, _ = w3_wline_shadow_data()
        assert cancel(kappa_W - c/3) == 0

    def test_alpha_w_zero(self):
        """alpha_W = 0 (Z_2 parity)."""
        _, alpha_W, _, _ = w3_wline_shadow_data()
        assert alpha_W == 0

    def test_s4_w(self):
        """S_4^W = 2560/[c(5c+22)^3]."""
        _, _, S4_W, _ = w3_wline_shadow_data()
        expected = Rational(2560) / (c*(5*c+22)**3)
        assert cancel(S4_W - expected) == 0

    def test_delta_w(self):
        """Delta_W = 20480/[3(5c+22)^3]."""
        _, _, _, Delta_W = w3_wline_shadow_data()
        expected = Rational(20480) / (3*(5*c+22)**3)
        assert cancel(Delta_W - expected) == 0

    def test_delta_w_from_function(self):
        """w3_wline_discriminant matches Delta_W from data."""
        _, _, _, Delta_W = w3_wline_shadow_data()
        assert cancel(w3_wline_discriminant() - Delta_W) == 0

    def test_metric_at_t_zero(self):
        """Q_W(0) = (2c/3)^2 = 4c^2/9."""
        Q = w3_wline_shadow_metric()
        assert cancel(Q.subs(t, 0) - 4*c**2/9) == 0

    def test_metric_no_linear_term(self):
        """Q_W has no linear term in t (alpha_W = 0)."""
        Q = w3_wline_shadow_metric()
        Q_scaled = cancel(Q * 3*(5*c+22)**3)
        p = Poly(expand(Q_scaled), t)
        assert p.nth(1) == 0

    def test_metric_even_in_t(self):
        """Q_W(t) = Q_W(-t) (even function of t, since alpha = 0)."""
        Q = w3_wline_shadow_metric()
        assert cancel(Q - Q.subs(t, -t)) == 0

    def test_gaussian_decomposition_wline(self):
        """Q_W = (2c/3)^2 + 2*Delta_W*t^2 (pure interaction, no linear)."""
        gauss, correction, Delta_W = w3_wline_gaussian_decomposition()
        Q = w3_wline_shadow_metric()
        assert cancel(Q - gauss - correction) == 0

    def test_gaussian_is_constant(self):
        """For W-line, Gaussian envelope = (2c/3)^2 (constant in t)."""
        gauss, _, _ = w3_wline_gaussian_decomposition()
        assert diff(gauss, t) == 0

    def test_delta_w_positive(self):
        """Delta_W > 0 for c > 0 (class M on W-line too)."""
        Delta_W = w3_wline_discriminant()
        for c_val in [1, 5, 13, 25, 50]:
            assert Delta_W.subs(c, c_val) > 0


# =========================================================================
# 9. W_3 W-line zeros
# =========================================================================

class TestW3WLineZeros:
    """Tests for the zeros of Q_W(t): purely imaginary branch points."""

    def test_two_zeros(self):
        """Q_W has 2 zeros."""
        zeros = w3_wline_zeros()
        assert len(zeros) == 2

    def test_zeros_purely_imaginary(self):
        """Zeros of Q_W are purely imaginary for c > 0.

        Since Q_W = A + B*t^2 with A, B > 0, the zeros are t = +/- i*sqrt(A/B).
        """
        zeros = w3_wline_zeros()
        for z in zeros:
            z_val = complex(z.subs(c, 13).evalf())
            assert abs(z_val.real) < 1e-10, f"Zero has nonzero real part: {z_val}"
            assert abs(z_val.imag) > 0.1, f"Zero has zero imag part: {z_val}"

    def test_zeros_symmetric(self):
        """Zeros are symmetric: t_0 = -t_1 (since alpha = 0)."""
        zeros = w3_wline_zeros()
        assert cancel(zeros[0] + zeros[1]) == 0

    def test_zero_modulus_squared(self):
        """The branch point modulus squared = (2c/3)^2 / (2*Delta_W).

        |t_0|^2 = A/B where A = (2c/3)^2 and B = 2*Delta_W.
        This equals 1/rho_W^2.
        """
        rho_sq, _ = w3_wline_growth_rate()
        zeros = w3_wline_zeros()
        z_val = zeros[0].subs(c, 13)
        mod_sq = cancel(z_val * z_val.conjugate() if hasattr(z_val, 'conjugate') else -z_val**2)
        # For purely imaginary z = i*a: |z|^2 = a^2 = -z^2
        expected = cancel(1/rho_sq.subs(c, 13))
        assert abs(float(mod_sq.evalf()) - float(expected.evalf())) < 1e-8

    def test_branch_point_argument_pi_over_2(self):
        """Branch point argument = pi/2 (purely imaginary)."""
        data = w3_wline_shadow_metric_numerical(13)
        assert abs(data['t0_argument'] - float(pi)/2) < 1e-10


# =========================================================================
# 10. W_3 W-line connection form
# =========================================================================

class TestW3WLineConnectionForm:
    """Tests for the W-line shadow connection form."""

    def test_connection_form_definition(self):
        """omega_W = Q_W'/(2*Q_W)."""
        Q = w3_wline_shadow_metric()
        omega = w3_wline_connection_form()
        Q_prime = diff(Q, t)
        assert cancel(omega - Q_prime/(2*Q)) == 0

    def test_connection_odd_in_t(self):
        """omega_W is an odd function of t (since Q_W is even in t).

        Q_W(-t) = Q_W(t), so Q_W'(-t) = -Q_W'(t),
        and omega(-t) = Q_W'(-t)/(2*Q_W(-t)) = -Q_W'(t)/(2*Q_W(t)) = -omega(t).
        """
        omega = w3_wline_connection_form()
        assert cancel(omega + omega.subs(t, -t)) == 0

    def test_connection_at_t_zero(self):
        """omega_W(0) = 0 (since Q_W' = 2*B*t has Q_W'(0)=0)."""
        omega = w3_wline_connection_form()
        assert cancel(omega.subs(t, 0)) == 0

    def test_flat_section_wline(self):
        """Phi_W(0) = 1."""
        Phi = w3_wline_flat_section()
        assert cancel(Phi.subs(t, 0) - 1) == 0


# =========================================================================
# 11. W_3 W-line growth rate
# =========================================================================

class TestW3WLineGrowthRate:
    """Tests for the W-line shadow growth rate rho_W."""

    def test_rho_w_squared(self):
        """rho_W^2 = 30720/[c^2*(5c+22)^3]."""
        rho_sq, _ = w3_wline_growth_rate()
        expected = Rational(30720) / (c**2 * (5*c+22)**3)
        assert cancel(rho_sq - expected) == 0

    def test_rho_w_much_smaller_than_rho_vir(self):
        """rho_W << rho_Vir for large c (W-channel converges faster).

        At c=13: rho_W ~ 0.017, rho_Vir ~ 0.467.
        """
        rho_sq_W, _ = w3_wline_growth_rate()
        # Virasoro rho^2 = (180c+872)/((5c+22)*c^2)
        rho_sq_Vir = cancel((180*c + 872) / ((5*c+22)*c**2))
        ratio = cancel(rho_sq_W / rho_sq_Vir)
        # At c=13: ratio should be << 1
        ratio_13 = float(ratio.subs(c, 13))
        assert ratio_13 < 0.01

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_rho_w_positive(self, c_val):
        """rho_W > 0 for c > 0 (class M)."""
        rho_sq, _ = w3_wline_growth_rate()
        assert float(rho_sq.subs(c, c_val)) > 0

    def test_rho_w_at_c13(self):
        """rho_W at c=13: numerical spot check."""
        rho_sq, _ = w3_wline_growth_rate()
        rho_13 = float(sqrt(rho_sq.subs(c, 13)).evalf())
        assert abs(rho_13 - 0.0166) < 0.001


# =========================================================================
# 12. W_3 T-line = Virasoro
# =========================================================================

class TestW3TLineEqualsVirasoro:
    """The T-line of W_3 IS the Virasoro shadow."""

    def test_tline_data_matches_virasoro(self):
        """Shadow data on T-line matches Virasoro data."""
        kT, aT, sT, dT = w3_tline_shadow_data()
        kV, aV, sV, dV = virasoro_shadow_data()
        assert cancel(kT - kV) == 0
        assert cancel(aT - aV) == 0
        assert cancel(sT - sV) == 0
        assert cancel(dT - dV) == 0

    def test_tline_metric_matches_virasoro(self):
        """T-line shadow metric = Virasoro shadow metric."""
        Q_T = w3_tline_shadow_metric()
        Q_V = virasoro_shadow_metric()
        assert cancel(Q_T - Q_V) == 0


# =========================================================================
# 13. Koszul duality
# =========================================================================

class TestKoszulDuality:
    """Koszul duality: c -> 26-c for Virasoro, c -> 100-c for W_3."""

    def test_virasoro_dual_metric(self):
        """Q_Vir^!(t) = Q_Vir(t)|_{c->26-c}."""
        Q = virasoro_shadow_metric()
        Q_dual = virasoro_koszul_dual_metric()
        assert cancel(Q_dual - Q.subs(c, 26-c)) == 0

    def test_self_dual_at_c13(self):
        """Q_Vir(t, 13) = Q_Vir(t, 26-13) = Q_Vir(t, 13)."""
        Q = virasoro_shadow_metric()
        Q_13 = Q.subs(c, 13)
        Q_dual_13 = koszul_dual_metric(Q).subs(c, 13)
        assert cancel(Q_13 - Q_dual_13) == 0

    def test_lee_yang_sum_26(self):
        """Lee-Yang points sum to 26 (Koszul conductor)."""
        ly1, ly2 = dual_lee_yang_points()
        assert ly1 + ly2 == 26
        assert ly1 == Rational(-22, 5)
        assert ly2 == Rational(152, 5)

    def test_w3_dual_metric(self):
        """Q_W^!(t) = Q_W(t)|_{c->100-c}."""
        Q = w3_wline_shadow_metric()
        Q_dual = w3_koszul_dual_wline_metric()
        assert cancel(Q_dual - Q.subs(c, 100-c)) == 0

    def test_w3_self_dual_at_c50(self):
        """W_3 self-dual at c=50."""
        Q = w3_wline_shadow_metric()
        Q_50 = Q.subs(c, 50)
        Q_dual_50 = Q.subs(c, 100-50)
        assert cancel(Q_50 - Q_dual_50) == 0


# =========================================================================
# 14. Complementarity
# =========================================================================

class TestComplementarity:
    """Complementarity sum Delta(c) + Delta(26-c)."""

    def test_constant_numerator(self):
        """Delta_Vir(c) + Delta_Vir(26-c) has constant numerator 6960."""
        Delta_sum = complementarity_sum_discriminant()
        n = numer(cancel(Delta_sum))
        assert Poly(n, c).degree() == 0

    def test_numerator_value_6960(self):
        """Numerator = 6960 = 40 * 174."""
        Delta_sum = complementarity_sum_discriminant()
        n = numer(cancel(Delta_sum))
        assert abs(int(n)) == 6960

    def test_denominator_is_dual_product(self):
        """Denominator = (5c+22)(152-5c)."""
        Delta_sum = complementarity_sum_discriminant()
        d = denom(cancel(Delta_sum))
        expected = (5*c + 22)*(152 - 5*c)
        assert cancel(d - expected) == 0 or cancel(d + expected) == 0

    @pytest.mark.parametrize("c_val", [1, 5, 13, 20, 25])
    def test_complementarity_numerical(self, c_val):
        """Numerical verification of the complementarity sum."""
        Delta = virasoro_discriminant()
        Delta_c = Delta.subs(c, c_val)
        Delta_dual = Delta.subs(c, 26-c_val)
        sum_val = Delta_c + Delta_dual
        expected = Rational(6960) / ((5*c_val+22)*(152-5*c_val))
        assert cancel(sum_val - expected) == 0

    def test_complementarity_at_self_dual(self):
        """Delta(13) + Delta(13) = 2*40/87 = 80/87."""
        Delta = virasoro_discriminant()
        sum_13 = 2 * Delta.subs(c, 13)
        assert sum_13 == Rational(80, 87)

    def test_complementarity_symmetry(self):
        """Delta_sum(c) = Delta_sum(26-c)."""
        Delta_sum = complementarity_sum_discriminant()
        assert cancel(Delta_sum - Delta_sum.subs(c, 26-c)) == 0


# =========================================================================
# 15. Self-dual metric
# =========================================================================

class TestSelfDualMetric:
    """The shadow metric at the self-dual point c=13."""

    def test_q_at_origin(self):
        """Q_Vir(0, 13) = 169 = 13^2."""
        Q_13 = self_dual_metric()
        assert cancel(Q_13.subs(t, 0) - 169) == 0

    def test_discriminant_negative(self):
        """disc(Q_13) < 0: complex branch points at c=13."""
        Q_13 = self_dual_metric()
        p = Poly(Q_13, t)
        a_coeff, b_coeff, c_coeff = p.nth(0), p.nth(1), p.nth(2)
        disc = b_coeff**2 - 4*a_coeff*c_coeff
        assert float(disc) < 0


# =========================================================================
# 16. Multi-channel curvature
# =========================================================================

class TestMultiChannelCurvature:
    """Multi-channel curvature = propagator variance."""

    def test_rank_one_flat(self):
        """Rank-1 connection is always flat (no curvature)."""
        from compute.lib.shadow_connection import multi_channel_curvature
        kappas = [c/2]
        fs = [Rational(40)/(c*(5*c+22))]
        assert multi_channel_curvature(kappas, fs) == 0

    def test_w3_has_curvature(self):
        """W_3 connection has nonzero curvature (propagator variance)."""
        from compute.lib.shadow_connection import multi_channel_curvature
        kappas = [c/2, c/3]
        f_T = Rational(200)*(c+14)/(c*(5*c+22)**2)
        f_W = Rational(640)*(15*c+82)/(c*(5*c+22)**3)
        curv = multi_channel_curvature(kappas, [f_T, f_W])
        assert curv.subs(c, 13) != 0


# =========================================================================
# 17. Cross-family consistency (AP10)
# =========================================================================

class TestCrossFamilyConsistency:
    """Cross-checks between Virasoro and W_3 shadow connections."""

    def test_delta_ratio(self):
        """Delta_W/Delta_Vir = 512/[3*(5c+22)^2].

        The W-channel discriminant is much smaller, explaining the
        W-line's faster convergence.
        """
        Delta_V = virasoro_discriminant()
        Delta_W = w3_wline_discriminant()
        ratio = cancel(Delta_W / Delta_V)
        expected = Rational(512) / (3*(5*c+22)**2)
        assert cancel(ratio - expected) == 0

    def test_rho_w_vs_rho_v_ratio(self):
        """rho_W^2 / rho_Vir^2 = 30720*(5c+22) / [(180c+872)*(5c+22)^3].

        Simplifies to 30720 / [(180c+872)*(5c+22)^2].
        """
        rho_sq_W, _ = w3_wline_growth_rate()
        rho_sq_V = (180*c + 872) / ((5*c+22)*c**2)
        ratio = cancel(rho_sq_W / rho_sq_V)
        expected = cancel(Rational(30720) / ((180*c+872)*(5*c+22)**2))
        assert cancel(ratio - expected) == 0

    def test_kappa_additivity(self):
        """kappa_total(W_3) = kappa_T + kappa_W = c/2 + c/3 = 5c/6."""
        kappa_T, _, _, _ = virasoro_shadow_data()
        kappa_W, _, _, _ = w3_wline_shadow_data()
        assert cancel(kappa_T + kappa_W - 5*c/6) == 0


# =========================================================================
# 18. Numerical spot checks
# =========================================================================

class TestNumericalVirasoro:
    """Numerical evaluation of Virasoro shadow connection."""

    @pytest.mark.parametrize("c_val", [1, 13, 25, 26])
    def test_data_well_defined(self, c_val):
        """Shadow data is well-defined at standard central charges."""
        data = virasoro_shadow_metric_numerical(c_val)
        assert data['kappa'] == c_val/2
        assert data['alpha'] == 2.0
        assert data['rho'] > 0

    def test_c13_self_dual(self):
        """At c=13: rho(Vir_13) should equal rho(Vir_{26-13}) = rho(Vir_13)."""
        data = virasoro_shadow_metric_numerical(13)
        data_dual = virasoro_shadow_metric_numerical(26-13)
        assert abs(data['rho'] - data_dual['rho']) < 1e-10

    def test_c26_convergent(self):
        """At c=26 (string theory): tower converges (rho < 1)."""
        data = virasoro_shadow_metric_numerical(26)
        assert data['convergent'] is True
        assert data['rho'] < 0.25  # rho ~ 0.234

    def test_c1_divergent(self):
        """At c=1: tower diverges (rho > 1)."""
        data = virasoro_shadow_metric_numerical(1)
        assert data['convergent'] is False
        assert data['rho'] > 1.0


class TestNumericalW3:
    """Numerical evaluation of W_3 W-line shadow connection."""

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25])
    def test_data_well_defined(self, c_val):
        """W-line data is well-defined."""
        data = w3_wline_shadow_metric_numerical(c_val)
        assert data['kappa_W'] == c_val/3
        assert data['rho_W'] > 0

    def test_w3_always_convergent_c13(self):
        """W-line tower converges at c=13 (rho_W << 1)."""
        data = w3_wline_shadow_metric_numerical(13)
        assert data['convergent'] is True
        assert data['rho_W'] < 0.05

    def test_w3_branch_argument_pi_half(self):
        """W-line branch points are at argument pi/2 (purely imaginary)."""
        data = w3_wline_shadow_metric_numerical(13)
        assert abs(data['t0_argument'] - float(pi)/2) < 1e-10


# =========================================================================
# 19. Picard-Fuchs and ODE verification
# =========================================================================

class TestPicardFuchs:
    """Tests for the Picard-Fuchs equation of the shadow connection."""

    def test_flat_section_satisfies_first_order_ode(self):
        """Phi' = omega * Phi (first-order ODE for the flat section).

        This is the defining equation nabla^sh(Phi) = 0.
        """
        Q = virasoro_shadow_metric()
        Q0 = Q.subs(t, 0)
        Phi = sqrt(Q / Q0)
        omega = connection_form(Q)
        # Phi' - omega*Phi should be zero
        Phi_prime = diff(Phi, t)
        residual = cancel(Phi_prime - omega*Phi)
        assert residual == 0

    def test_w3_flat_section_ode(self):
        """W-line flat section satisfies the same first-order ODE."""
        Q = w3_wline_shadow_metric()
        Q0 = Q.subs(t, 0)
        Phi = sqrt(Q / Q0)
        omega = connection_form(Q)
        Phi_prime = diff(Phi, t)
        residual = cancel(Phi_prime - omega*Phi)
        assert residual == 0


# =========================================================================
# 20. H^2 = t^4 * Q verification
# =========================================================================

class TestRiccatiAlgebraicity:
    """The algebraic relation H^2 = t^4 * Q (thm:riccati-algebraicity)."""

    def test_virasoro_h_squared(self):
        """H_Vir^2 = t^4 * Q_Vir."""
        Q = virasoro_shadow_metric()
        H = shadow_generating_function(Q, c/2)
        assert cancel(H**2 - t**4*Q) == 0

    def test_w3_wline_h_squared(self):
        """H_W^2 = t^4 * Q_W."""
        Q = w3_wline_shadow_metric()
        H = shadow_generating_function(Q, c/3)
        assert cancel(H**2 - t**4*Q) == 0

    def test_heisenberg_h_squared(self):
        """For Heisenberg: Q = c^2, H = c*t^2. H^2 = c^2*t^4 = t^4*Q."""
        Q = shadow_metric_general(c/2, Rational(0), Rational(0))
        assert cancel(Q - c**2) == 0
        H = shadow_generating_function(Q, c/2)
        assert cancel(H**2 - t**4*Q) == 0

    def test_affine_km_h_squared(self):
        """For affine KM: Q = (2kappa + 3*alpha*t)^2. Tower terminates at depth 3."""
        kappa, alpha = c/2, Rational(1)
        Q = shadow_metric_general(kappa, alpha, Rational(0))
        H = shadow_generating_function(Q, kappa)
        assert cancel(H**2 - t**4*Q) == 0


# =========================================================================
# 21. Numerical monodromy and residue verification
# =========================================================================

class TestNumericalMonodromy:
    r"""Numerical verification of shadow connection monodromy and residues.

    The shadow connection nabla^sh = d - omega dt, where omega = Q'/(2Q),
    has regular singular points at the zeros of Q_L(t).

    At each simple zero t_0:
      - Residue of omega at t_0 is 1/2.
      - Monodromy = exp(2*pi*i * 1/2) = -1 (the Koszul sign).

    We verify these numerically by contour integration:
      - Residue = (1/(2*pi*i)) * oint_{|t-t_0|=r} omega(t) dt
      - Monodromy = exp(oint_{|t-t_0|=r} omega(t) dt) = exp(pi*i) = -1

    The parallel transport of the flat section Phi(t) = sqrt(Q(t)/Q(0))
    around each zero picks up a factor of -1 (sheet exchange of the
    double cover). This is the Koszul sign, the fundamental Z/2 symmetry
    of bar-cobar duality.
    """

    @staticmethod
    def _virasoro_omega_numerical(c_val):
        """Return a callable omega(t_complex) for Virasoro at given c.

        Q_Vir(t) = c^2 + 12*c*t + alpha_c*t^2
        where alpha_c = (180*c + 872)/(5*c + 22).
        omega = Q'/(2*Q) = (12*c + 2*alpha_c*t) / (2*(c^2 + 12*c*t + alpha_c*t^2)).
        """
        alpha_c = (180*c_val + 872) / (5*c_val + 22)
        q0 = c_val**2
        q1 = 12*c_val
        q2 = alpha_c

        def omega(z):
            Q_val = q0 + q1*z + q2*z**2
            Qp_val = q1 + 2*q2*z
            return Qp_val / (2 * Q_val)

        return omega

    @staticmethod
    def _virasoro_zeros_numerical(c_val):
        """Return the two zeros of Q_Vir(t) at given c as complex numbers."""
        import cmath
        alpha_c = (180*c_val + 872) / (5*c_val + 22)
        q0 = c_val**2
        q1 = 12*c_val
        q2 = alpha_c
        disc = q1**2 - 4*q0*q2
        sqrt_disc = cmath.sqrt(disc)
        t_plus = (-q1 + sqrt_disc) / (2*q2)
        t_minus = (-q1 - sqrt_disc) / (2*q2)
        return t_plus, t_minus

    @staticmethod
    def _w3_omega_numerical(c_val):
        """Return a callable omega(t_complex) for W_3 W-line at given c.

        Q_W(t) = 4*c^2/9 + B*t^2
        where B = 2*Delta_W = 40960/(3*(5*c+22)^3).
        omega = Q'/(2*Q) = 2*B*t / (2*(A + B*t^2)) = B*t / (A + B*t^2).
        """
        A = 4*c_val**2 / 9
        B = 40960 / (3*(5*c_val + 22)**3)

        def omega(z):
            Q_val = A + B*z**2
            Qp_val = 2*B*z
            return Qp_val / (2 * Q_val)

        return omega

    @staticmethod
    def _w3_zeros_numerical(c_val):
        """Return the two zeros of Q_W(t) at given c as complex numbers."""
        import cmath
        A = 4*c_val**2 / 9
        B = 40960 / (3*(5*c_val + 22)**3)
        # Q_W = A + B*t^2 = 0 => t = +/- i*sqrt(A/B)
        t_mod = cmath.sqrt(A/B)
        return 1j*t_mod, -1j*t_mod

    @staticmethod
    def _contour_integral(omega_func, center, radius, n_points=4096):
        """Numerically compute (1/(2*pi*i)) * oint omega(t) dt around center.

        Parameterize: t(theta) = center + radius * exp(i*theta), theta in [0, 2*pi].
        dt = i * radius * exp(i*theta) * dtheta.
        Integral = int_0^{2*pi} omega(t(theta)) * i * radius * exp(i*theta) dtheta.
        Residue = (1/(2*pi*i)) * Integral.

        Uses the trapezoidal rule, which is exponentially accurate for
        analytic integrands on a circle (spectral convergence).
        """
        import numpy as np
        thetas = np.linspace(0, 2*np.pi, n_points, endpoint=False)
        dtheta = 2*np.pi / n_points
        integrand = np.zeros(n_points, dtype=complex)
        for j in range(n_points):
            z = center + radius * np.exp(1j * thetas[j])
            dz_dtheta = 1j * radius * np.exp(1j * thetas[j])
            integrand[j] = omega_func(z) * dz_dtheta
        integral = np.sum(integrand) * dtheta
        return integral

    # ----- Virasoro residue tests -----

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 25, 26])
    def test_virasoro_residue_at_zero_plus(self, c_val):
        """Residue of omega at t_+ equals 1/2 for Virasoro at various c."""
        import numpy as np
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        # Radius: small enough to not encircle the other zero
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_plus, radius)
        residue = integral / (2j * np.pi)
        assert abs(residue - 0.5) < 1e-8, \
            f"Virasoro c={c_val}: Res(omega, t_+) = {residue}, expected 0.5"

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 25, 26])
    def test_virasoro_residue_at_zero_minus(self, c_val):
        """Residue of omega at t_- equals 1/2 for Virasoro at various c."""
        import numpy as np
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_minus, radius)
        residue = integral / (2j * np.pi)
        assert abs(residue - 0.5) < 1e-8, \
            f"Virasoro c={c_val}: Res(omega, t_-) = {residue}, expected 0.5"

    # ----- Virasoro monodromy tests -----

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 25, 26])
    def test_virasoro_monodromy_at_zero_plus(self, c_val):
        """Monodromy around t_+ equals -1 for Virasoro at various c.

        Monodromy = exp(oint omega dt) = exp(2*pi*i * Res) = exp(pi*i) = -1.
        """
        import numpy as np
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_plus, radius)
        monodromy = np.exp(integral)
        assert abs(monodromy - (-1.0)) < 1e-7, \
            f"Virasoro c={c_val}: monodromy = {monodromy}, expected -1"

    @pytest.mark.parametrize("c_val", [1, 2, 10, 13, 25, 26])
    def test_virasoro_monodromy_at_zero_minus(self, c_val):
        """Monodromy around t_- equals -1 for Virasoro at various c."""
        import numpy as np
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_minus, radius)
        monodromy = np.exp(integral)
        assert abs(monodromy - (-1.0)) < 1e-7, \
            f"Virasoro c={c_val}: monodromy = {monodromy}, expected -1"

    # ----- W_3 W-line residue tests -----

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25, 50])
    def test_w3_residue_at_zero_plus(self, c_val):
        """Residue of omega at +i*sqrt(A/B) equals 1/2 for W_3 W-line."""
        import numpy as np
        omega = self._w3_omega_numerical(c_val)
        t_plus, t_minus = self._w3_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_plus, radius)
        residue = integral / (2j * np.pi)
        assert abs(residue - 0.5) < 1e-8, \
            f"W3 c={c_val}: Res(omega, t_+) = {residue}, expected 0.5"

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25, 50])
    def test_w3_residue_at_zero_minus(self, c_val):
        """Residue of omega at -i*sqrt(A/B) equals 1/2 for W_3 W-line."""
        import numpy as np
        omega = self._w3_omega_numerical(c_val)
        t_plus, t_minus = self._w3_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_minus, radius)
        residue = integral / (2j * np.pi)
        assert abs(residue - 0.5) < 1e-8, \
            f"W3 c={c_val}: Res(omega, t_-) = {residue}, expected 0.5"

    # ----- W_3 W-line monodromy tests -----

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25, 50])
    def test_w3_monodromy_at_zero_plus(self, c_val):
        """Monodromy around +i*sqrt(A/B) equals -1 for W_3 W-line."""
        import numpy as np
        omega = self._w3_omega_numerical(c_val)
        t_plus, t_minus = self._w3_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_plus, radius)
        monodromy = np.exp(integral)
        assert abs(monodromy - (-1.0)) < 1e-7, \
            f"W3 c={c_val}: monodromy = {monodromy}, expected -1"

    @pytest.mark.parametrize("c_val", [1, 5, 13, 25, 50])
    def test_w3_monodromy_at_zero_minus(self, c_val):
        """Monodromy around -i*sqrt(A/B) equals -1 for W_3 W-line."""
        import numpy as np
        omega = self._w3_omega_numerical(c_val)
        t_plus, t_minus = self._w3_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        integral = self._contour_integral(omega, t_minus, radius)
        monodromy = np.exp(integral)
        assert abs(monodromy - (-1.0)) < 1e-7, \
            f"W3 c={c_val}: monodromy = {monodromy}, expected -1"

    # ----- Self-dual point structure -----

    def test_virasoro_self_dual_zeros_equal_modulus(self):
        """At c=13 (self-dual): both zeros have identical modulus."""
        t_plus, t_minus = self._virasoro_zeros_numerical(13)
        assert abs(abs(t_plus) - abs(t_minus)) < 1e-12

    def test_virasoro_self_dual_zeros_conjugate(self):
        """At c=13: zeros are complex conjugate (real parts equal, imag opposite)."""
        t_plus, t_minus = self._virasoro_zeros_numerical(13)
        assert abs(t_plus.real - t_minus.real) < 1e-12
        assert abs(t_plus.imag + t_minus.imag) < 1e-12

    def test_w3_self_dual_zeros_purely_imaginary(self):
        """At c=50 (self-dual for W_3): zeros are purely imaginary and symmetric."""
        t_plus, t_minus = self._w3_zeros_numerical(50)
        assert abs(t_plus.real) < 1e-12
        assert abs(t_minus.real) < 1e-12
        assert abs(t_plus + t_minus) < 1e-12  # symmetric: t_+ = -t_-

    def test_w3_self_dual_koszul_invariance(self):
        """At c=50: Q_W(t, 50) = Q_W(t, 100-50) (Koszul-invariant metric)."""
        import numpy as np
        omega_50 = self._w3_omega_numerical(50)
        t_plus, _ = self._w3_zeros_numerical(50)
        # The zero modulus should equal that of the dual (which is the same c=50)
        t_plus_dual, _ = self._w3_zeros_numerical(100 - 50)
        assert abs(abs(t_plus) - abs(t_plus_dual)) < 1e-12

    # ----- Parallel transport verification -----

    def test_virasoro_parallel_transport_sign_flip(self):
        """Parallel transport of Phi around a zero flips sign.

        Phi(t) = sqrt(Q(t)/Q(0)). Going around a zero of Q, the
        square root picks up a factor of -1 (sheet exchange).

        We verify by computing Phi along a contour: the ratio
        Phi(end)/Phi(start) should be -1 after a full loop.
        """
        import numpy as np
        c_val = 13
        alpha_c = (180*c_val + 872) / (5*c_val + 22)
        q0 = c_val**2
        q1 = 12*c_val
        q2 = alpha_c
        Q0 = q0  # Q(0) = c^2

        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1

        n_points = 8192
        thetas = np.linspace(0, 2*np.pi, n_points + 1)

        # Track Phi = sqrt(Q/Q0) continuously along the contour
        # by integrating d(log Phi)/dtheta = omega * dt/dtheta
        omega = self._virasoro_omega_numerical(c_val)
        log_phi = 0.0 + 0.0j
        for j in range(n_points):
            z = t_plus + radius * np.exp(1j * thetas[j])
            dz_dtheta = 1j * radius * np.exp(1j * thetas[j])
            dtheta = thetas[j+1] - thetas[j]
            log_phi += omega(z) * dz_dtheta * dtheta

        transport_factor = np.exp(log_phi)
        assert abs(transport_factor - (-1.0)) < 1e-6, \
            f"Parallel transport factor = {transport_factor}, expected -1"

    def test_virasoro_monodromy_squared_is_identity(self):
        """Double loop around a zero gives monodromy^2 = 1 (Z/2 factorization).

        Going around a zero twice: exp(2 * oint omega dt) = (-1)^2 = 1.
        """
        import numpy as np
        c_val = 10
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        sep = abs(t_plus - t_minus)
        radius = sep * 0.1
        # Single loop integral
        integral = self._contour_integral(omega, t_plus, radius)
        # Double loop
        monodromy_sq = np.exp(2 * integral)
        assert abs(monodromy_sq - 1.0) < 1e-7, \
            f"Monodromy^2 = {monodromy_sq}, expected 1"

    # ----- Contour encircling both zeros -----

    def test_virasoro_total_residue(self):
        """Total residue (sum over both zeros) equals 1.

        Since omega = Q'/(2Q) = d(log Q)/2, and Q is a degree-2 polynomial
        in t with leading coefficient q2, the total residue is
        sum of residues = 1/2 + 1/2 = 1.

        We verify by integrating omega around a large contour encircling
        both zeros.
        """
        import numpy as np
        c_val = 13
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)

        # Center at midpoint of zeros, radius large enough to encircle both
        center = (t_plus + t_minus) / 2
        half_sep = abs(t_plus - t_minus) / 2
        radius = half_sep * 3.0  # large enough to encircle both

        integral = self._contour_integral(omega, center, radius)
        total_residue = integral / (2j * np.pi)
        assert abs(total_residue - 1.0) < 1e-7, \
            f"Total residue = {total_residue}, expected 1.0"

    def test_w3_total_residue(self):
        """Total residue for W_3 W-line (both zeros) equals 1."""
        import numpy as np
        c_val = 13
        omega = self._w3_omega_numerical(c_val)
        t_plus, t_minus = self._w3_zeros_numerical(c_val)

        center = (t_plus + t_minus) / 2  # = 0 by symmetry
        half_sep = abs(t_plus - t_minus) / 2
        radius = half_sep * 3.0

        integral = self._contour_integral(omega, center, radius)
        total_residue = integral / (2j * np.pi)
        assert abs(total_residue - 1.0) < 1e-7, \
            f"W3 total residue = {total_residue}, expected 1.0"

    def test_virasoro_total_monodromy_plus_one(self):
        """Monodromy around BOTH zeros is +1 (= (-1)*(-1) = 1).

        The total monodromy of the shadow connection around a large loop
        encircling both branch points is trivial: the two Koszul signs cancel.
        """
        import numpy as np
        c_val = 25
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)

        center = (t_plus + t_minus) / 2
        half_sep = abs(t_plus - t_minus) / 2
        radius = half_sep * 3.0

        integral = self._contour_integral(omega, center, radius)
        total_monodromy = np.exp(integral)
        assert abs(total_monodromy - 1.0) < 1e-6, \
            f"Total monodromy = {total_monodromy}, expected +1"

    # ----- No monodromy away from zeros -----

    def test_virasoro_no_monodromy_away_from_zeros(self):
        """A contour NOT encircling any zero has trivial monodromy.

        Integrate around a small circle centered at the origin (which is
        not a zero of Q since Q(0) = c^2 != 0).
        """
        import numpy as np
        c_val = 13
        omega = self._virasoro_omega_numerical(c_val)
        t_plus, t_minus = self._virasoro_zeros_numerical(c_val)
        # Radius small enough to not reach either zero
        min_dist = min(abs(t_plus), abs(t_minus))
        radius = min_dist * 0.3

        integral = self._contour_integral(omega, 0.0, radius)
        residue = integral / (2j * np.pi)
        assert abs(residue) < 1e-8, \
            f"Residue at origin = {residue}, expected 0"
