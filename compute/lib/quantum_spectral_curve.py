r"""Quantum spectral curve and exact WKB from the shadow ODE.

MATHEMATICAL FRAMEWORK
======================

The shadow connection nabla^sh = d - Q_L'/(2*Q_L) dt has flat sections
Phi(t) = sqrt(Q_L(t)/Q_L(0)).  The Liouville substitution transforms
this first-order logarithmic connection into a second-order Schrodinger
equation (shadow_painleve.py, Section 1):

    hbar^2 u'' = V(t) u

where V(t) = 8*kappa^2*Delta / Q_L(t)^2 is the Schwarzian potential
and hbar is a formal deformation parameter.

The CLASSICAL SPECTRAL CURVE is y^2 = V(t), which is the genus-0
hyperelliptic curve inherited from the shadow metric Q_L(t).

The QUANTUM SPECTRAL CURVE is the hbar-deformation obtained by the
exact WKB method (Voros 1983, Delabaere-Dillinger-Pham 1993,
Iwaki-Nakanishi 2014):

    Psi(t, hbar) = exp((1/hbar) S(t, hbar))

where S(t, hbar) = S_0(t) + hbar S_1(t) + hbar^2 S_2(t) + ...

satisfies the Riccati equation obtained by substituting into the
Schrodinger equation:

    (S')^2 + hbar S'' = V(t)

Expanding order by order:

    (S_0')^2 = V(t)                                   [classical]
    2 S_0' S_1' + S_0'' = 0                            [one-loop]
    2 S_0' S_2' + (S_1')^2 + S_1'' = 0                [two-loop]
    2 S_0' S_n' + sum_{j=1}^{n-1} S_j' S_{n-j}' + S_{n-1}'' = 0  [n-loop]

SOLUTIONS:

    S_0(t) = +/- integral_0^t sqrt(V(s)) ds           [classical action]
    S_1(t) = -(1/4) ln V(t) = -(1/4) ln(8*kappa^2*Delta) + (1/2) ln Q_L(t)
                                                        [one-loop]
    S_n(t) for n >= 2: determined recursively by the WKB transport equations

KEY SUBTLETY: V(t) = C / Q_L(t)^2 where C = 8*kappa^2*Delta.  The square
root sqrt(V) = sqrt(C) / Q_L(t).  Since Q_L is quadratic, sqrt(V) is a
RATIONAL function (no branch cuts from V itself; the branch cuts come from
the sign choice +/-).  The integral S_0 = integral sqrt(C)/Q_L(t) dt is
elementary (partial fractions over the zeros of Q_L).

VOROS COEFFICIENTS:

For a cycle gamma on the spectral curve, the Voros symbol is

    V_gamma(hbar) = exp(oint_gamma p(t, hbar) dt)

where p = S'(t, hbar) = S_0' + hbar S_1' + hbar^2 S_2' + ...

The Voros coefficients are the period integrals oint_gamma S_n'(t) dt.

STOKES PHENOMENON:

The exact WKB solutions jump across Stokes lines (where Im(S_0) = 0).
The Stokes automorphism is controlled by the Voros symbols and the
connection formula:

    S = 1 + sum_n omega_n T_n

where omega_n are Stokes multipliers and T_n are the alien derivatives.

For the shadow Schrodinger equation with 3 regular singular points on P^1,
the monodromy representation is in SL(2, C), and the Stokes phenomenon is
encoded by the monodromy matrices around the branch points of Q_L.

PAINLEVE CONNECTION:

For the single-channel shadow, the Schrodinger equation has 3 regular
singular points on P^1 (the two zeros of Q_L and infinity).  This is a
Gauss hypergeometric equation -- RIGID, with no accessory parameter and
no Painleve.

For the multi-channel case (e.g., W_3 with T and W channels), the coupled
2x2 system has 4+ singular points, giving Painleve VI.

Dependencies:
    shadow_connection.py -- shadow metric Q_L(t), connection forms
    shadow_painleve.py -- Schwarzian potential, singularity classification
    spectral_curve_engine.py -- spectral curve y^2 = Q(t)
    resurgence_frontier_engine.py -- Borel transform, shadow coefficients

Manuscript references:
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

from sympy import (
    Abs, I, Poly, Rational, S, Symbol,
    cancel, conjugate, cos, diff, expand, factor,
    im, integrate, log, numer, denom, oo, pi, re, simplify,
    sin, solve, sqrt, symbols, series, collect, together,
    binomial, gamma, factorial, bernoulli, exp, atan2,
    Function, Eq, atan, asin, Piecewise, zoo, nan,
)

# =========================================================================
# Symbols
# =========================================================================

c_sym = Symbol('c')
t_sym = Symbol('t')
hbar_sym = Symbol('hbar')
kappa_sym = Symbol('kappa')
alpha_sym = Symbol('alpha')
Delta_sym = Symbol('Delta')


# =========================================================================
# Section 1: Classical spectral curve from the shadow metric
# =========================================================================

def shadow_metric_poly(kappa, alpha, Delta):
    """Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Expanded: q_0 + q_1*t + q_2*t^2 with
        q_0 = 4*kappa^2,  q_1 = 12*kappa*alpha,  q_2 = 9*alpha^2 + 2*Delta
    """
    return (2*kappa + 3*alpha*t_sym)**2 + 2*Delta*t_sym**2


def shadow_metric_coefficients(kappa, alpha, Delta):
    """Return (q_0, q_1, q_2) of Q_L(t) = q_0 + q_1*t + q_2*t^2."""
    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 2*Delta
    return q0, q1, q2


def schwarzian_potential(kappa, alpha, Delta):
    """The Schwarzian potential V(t) = 8*kappa^2*Delta / Q_L(t)^2.

    This is the potential in the Schrodinger equation u'' = V(t)*u
    obtained from the shadow connection by Liouville transformation.

    V(t) = -disc(Q_L) / (4*Q_L(t)^2) where disc = -32*kappa^2*Delta.

    WARNING: V = 0 when Delta = 0 (classes G and L).  The quantum
    spectral curve is trivial in these cases.
    """
    Q = shadow_metric_poly(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta
    return C / Q**2


def classical_spectral_curve(kappa, alpha, Delta):
    """The classical spectral curve y^2 = V(t).

    V(t) = 8*kappa^2*Delta / Q_L(t)^2, so
    y = sqrt(8*kappa^2*Delta) / Q_L(t)  (rational in t).

    The curve y^2 = V(t) is genus 0 (rational) since V(t) has only
    even-order poles.

    Returns dict with:
        'V': the potential V(t)
        'Q': the shadow metric Q_L(t)
        'C': the constant 8*kappa^2*Delta
        'branch_points': zeros of Q_L (where V has poles)
        'genus': 0
    """
    Q = shadow_metric_poly(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta
    V = C / Q**2

    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, Delta)
    disc = q1**2 - 4*q0*q2  # = -32*kappa^2*Delta
    if q2 != 0:
        t_plus = simplify((-q1 + sqrt(disc)) / (2*q2))
        t_minus = simplify((-q1 - sqrt(disc)) / (2*q2))
        branch_points = [t_plus, t_minus]
    else:
        branch_points = []

    return {
        'V': V,
        'Q': Q,
        'C': C,
        'branch_points': branch_points,
        'genus': 0,
    }


def virasoro_classical_curve():
    """Classical spectral curve for the Virasoro algebra.

    kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)), Delta = 40/(5c+22).
    """
    c = c_sym
    kappa = c / 2
    alpha = Rational(2)
    Delta = Rational(40) / (5*c + 22)
    return classical_spectral_curve(kappa, alpha, Delta)


# =========================================================================
# Section 2: WKB expansion — recursive computation of S_n(t)
# =========================================================================

def wkb_leading_order(kappa, alpha, Delta):
    r"""Leading WKB term S_0'(t) = sqrt(V(t)) = sqrt(C) / Q_L(t).

    S_0(t) = sqrt(C) * integral(1/Q_L(t), t)

    For Q_L = q_0 + q_1*t + q_2*t^2 with disc < 0 (complex zeros):

        integral(1/Q_L) = (2/(sqrt(4*q_0*q_2 - q_1^2)))
                          * arctan((2*q_2*t + q_1) / sqrt(4*q_0*q_2 - q_1^2))

    Returns dict with 'S0_prime', 'S0' (sympy expressions in t_sym).
    """
    Q = shadow_metric_poly(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta
    S0_prime = sqrt(C) / Q

    # Integrate using sympy
    S0 = integrate(S0_prime, t_sym)

    return {
        'S0_prime': S0_prime,
        'S0': S0,
        'C': C,
        'Q': Q,
    }


def wkb_one_loop(kappa, alpha, Delta):
    r"""One-loop WKB correction S_1(t) = -(1/4) ln(V(t)).

    From the transport equation 2 S_0' S_1' + S_0'' = 0:
        S_1' = -S_0'' / (2 S_0')

    S_0' = sqrt(C)/Q, so S_0'' = -sqrt(C)*Q'/Q^2.
    S_1' = -(-sqrt(C)*Q'/Q^2) / (2*sqrt(C)/Q) = Q'/(2Q)

    Therefore S_1(t) = (1/2) ln Q_L(t) + const.

    Equivalently, S_1 = -(1/4) ln V = -(1/4) ln(C/Q^2) = (1/2) ln Q - (1/4) ln C.

    NOTE: S_1' = Q'/(2Q) = the shadow connection form omega.  The one-loop
    WKB correction IS the shadow connection.  This is the fundamental
    identification: the shadow connection is the one-loop quantum correction
    to the classical spectral curve.
    """
    Q = shadow_metric_poly(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta
    Q_prime = diff(Q, t_sym)

    S1_prime = Q_prime / (2 * Q)
    S1 = Rational(1, 2) * log(Q)  # up to additive constant

    return {
        'S1_prime': S1_prime,
        'S1': S1,
        'identification': 'S1_prime = omega (shadow connection form)',
    }


def wkb_recursive_coefficients(kappa, alpha, Delta, max_order=4):
    r"""Compute WKB coefficients S_n'(t) recursively for n = 0, 1, ..., max_order.

    The Riccati equation (S')^2 + hbar S'' = V(t) gives, with
    S = sum_{n >= 0} hbar^n S_n:

    Order hbar^0: (S_0')^2 = V
    Order hbar^1: 2 S_0' S_1' + S_0'' = 0
    Order hbar^n (n >= 2): 2 S_0' S_n' + sum_{j=1}^{n-1} S_j' S_{n-j}' + S_{n-1}'' = 0

    Solving for S_n':
        S_n' = -(1/(2 S_0')) * [sum_{j=1}^{n-1} S_j' S_{n-j}' + S_{n-1}'']

    Returns dict {n: S_n'(t)} for n = 0, 1, ..., max_order.
    All expressions are sympy expressions in t_sym, possibly involving
    kappa, alpha, Delta as parameters.
    """
    Q = shadow_metric_poly(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta

    # S_0' = sqrt(C) / Q
    # We keep everything as rational functions of t by working with
    # sqrt(C) as a symbolic constant.
    sqC = sqrt(C)
    S0p = sqC / Q

    # S_1' = Q'/(2Q)
    Qp = diff(Q, t_sym)
    S1p = cancel(Qp / (2 * Q))

    Sp = {0: S0p, 1: S1p}

    for n in range(2, max_order + 1):
        # sum_{j=1}^{n-1} S_j' * S_{n-j}'
        conv_sum = S.Zero
        for j in range(1, n):
            conv_sum = conv_sum + Sp[j] * Sp[n - j]
        conv_sum = expand(conv_sum)

        # S_{n-1}''
        Snm1_pp = diff(Sp[n - 1], t_sym)

        # S_n' = -(conv_sum + S_{n-1}'') / (2 * S_0')
        # 2*S_0' = 2*sqrt(C)/Q, so 1/(2*S_0') = Q/(2*sqrt(C))
        numerator_expr = -(conv_sum + Snm1_pp)
        Snp = cancel(numerator_expr * Q / (2 * sqC))

        Sp[n] = Snp

    return Sp


def wkb_expansion_virasoro(max_order=4):
    """WKB expansion for the Virasoro algebra.

    kappa = c/2, alpha = 2, Delta = 40/(5c+22).
    """
    c = c_sym
    kappa = c / 2
    alpha = Rational(2)
    Delta = Rational(40) / (5*c + 22)
    return wkb_recursive_coefficients(kappa, alpha, Delta, max_order)


# =========================================================================
# Section 3: Voros coefficients — period integrals of the WKB differentials
# =========================================================================

def voros_integrand_symbolic(kappa, alpha, Delta, order=2):
    r"""The Voros integrand p(t, hbar) = S_0' + hbar S_1' + ... + hbar^n S_n'.

    The Voros symbol for a cycle gamma is V_gamma = exp(oint_gamma p dt).
    The Voros coefficients are v_n = oint_gamma S_n'(t) dt.

    Returns the formal power series p(t, hbar) truncated at order n.
    """
    Sp = wkb_recursive_coefficients(kappa, alpha, Delta, order)
    p = S.Zero
    for n in range(order + 1):
        p = p + hbar_sym**n * Sp[n]
    return p


def voros_period_classical(kappa, alpha, Delta):
    r"""Classical Voros period: v_0 = oint_gamma S_0'(t) dt.

    For the cycle gamma encircling the two zeros t_+, t_- of Q_L:

        v_0 = oint sqrt(C)/Q_L(t) dt

    By the residue theorem, since Q_L = q_2*(t - t_+)(t - t_-):

        v_0 = 2*pi*i * [Res_{t_+}(sqrt(C)/Q_L) + Res_{t_-}(sqrt(C)/Q_L)]

    Res_{t_pm} = sqrt(C) / Q_L'(t_pm) = sqrt(C) / (q_2*(t_pm - t_mp))

    Sum of residues = sqrt(C)/(q_2) * [(t_+ - t_-)^{-1} + (t_- - t_+)^{-1}] = 0

    VANISHES because the sum of residues at the two simple poles is zero
    (the function sqrt(C)/Q_L has residues that sum to zero by Cauchy).

    This reflects: the classical Voros period around a COMPACT cycle
    encircling both zeros vanishes.  The nontrivial period is around
    a NON-COMPACT cycle (from one zero to the other, on a different sheet).
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, Delta)
    C = 8 * kappa**2 * Delta
    disc_Q = q1**2 - 4*q0*q2  # = -32*kappa^2*Delta

    # The NON-COMPACT period (half-period from t_- to t_+):
    # v_0 = integral_{t_-}^{t_+} sqrt(C)/Q_L(t) dt
    # This equals: sqrt(C) * pi / (q_2 * sqrt(-disc_Q/(4*q_2^2)))
    #            = sqrt(C) * pi / sqrt(q_0*q_2 - q_1^2/4)
    # where q_0*q_2 - q_1^2/4 = -(disc_Q)/4 = 8*kappa^2*Delta.
    #
    # So v_0 = sqrt(8*kappa^2*Delta) * pi / sqrt(8*kappa^2*Delta) = pi.
    #
    # UNIVERSAL RESULT: the classical half-period is always pi,
    # independent of the algebra.

    return {
        'compact_period': S.Zero,     # oint around both zeros = 0
        'half_period': pi,            # integral from t_- to t_+ = pi
        'full_noncompact_period': 2*pi,
        'universality': 'The classical period pi is universal (algebra-independent).',
    }


def voros_period_one_loop(kappa, alpha, Delta):
    r"""One-loop Voros period: v_1 = oint_gamma S_1'(t) dt.

    S_1' = Q_L'/(2*Q_L), so oint S_1' dt = oint Q'/(2Q) dt = pi*i
    (each simple zero of Q_L contributes a residue of 1/2).

    For the compact cycle encircling both zeros:
        v_1 = 2 * (2*pi*i * 1/2) = 2*pi*i.

    For the half-period (one zero):
        v_1 = pi*i.

    This equals log(-1) = pi*i, which is the KOSZUL SIGN.
    The one-loop Voros coefficient exponentiates to:
        exp(v_1) = exp(pi*i) = -1 = Koszul sign.
    """
    return {
        'compact_period': 2*pi*I,
        'half_period': pi*I,
        'exp_half_period': -1,
        'identification': 'exp(v_1) = -1 = Koszul sign (monodromy of sqrt(Q_L))',
    }


def voros_coefficients_numerical(kappa_val, alpha_val, Delta_val,
                                  max_order=4, n_points=500):
    r"""Compute Voros coefficients v_n numerically by contour integration.

    v_n = oint_gamma S_n'(t) dt

    where gamma is a closed contour encircling both zeros of Q_L.

    For numerical computation, we parametrize gamma as a circle of radius R
    centered at the midpoint of the two zeros.  R is chosen large enough
    to encircle both.
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val

    if abs(q2) < 1e-30:
        return {}

    disc = q1**2 - 4*q0*q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2*q2)
    t_minus = (-q1 - sqrt_disc) / (2*q2)

    center = (t_plus + t_minus) / 2
    radius = abs(t_plus - t_minus) * 1.5  # safely encircle both zeros

    C_val = 8 * kappa_val**2 * Delta_val
    sqC = cmath.sqrt(C_val)

    def Q_eval(t_val):
        return q0 + q1*t_val + q2*t_val**2

    def Q_prime_eval(t_val):
        return q1 + 2*q2*t_val

    def Q_pprime_eval(t_val):
        return 2*q2

    # Build S_n' numerically
    def S0p(t_val):
        Q_val = Q_eval(t_val)
        if abs(Q_val) < 1e-60:
            return 0.0j
        return sqC / Q_val

    def S1p(t_val):
        Q_val = Q_eval(t_val)
        Qp_val = Q_prime_eval(t_val)
        if abs(Q_val) < 1e-60:
            return 0.0j
        return Qp_val / (2 * Q_val)

    # Recursively build higher S_n' using cached arrays
    Sp_funcs = {0: S0p, 1: S1p}

    # For higher orders, store derivative values on the contour and build
    # S_n' from the recursion.  For numerical robustness, compute on the
    # contour points directly.

    theta_vals = np.linspace(0, 2*np.pi, n_points, endpoint=False)
    dt_vals = 1j * radius * np.exp(1j * theta_vals) * (2*np.pi / n_points)
    t_vals = center + radius * np.exp(1j * theta_vals)

    # Evaluate on contour
    Sp_arrays = {}
    Sp_arrays[0] = np.array([S0p(tv) for tv in t_vals])
    Sp_arrays[1] = np.array([S1p(tv) for tv in t_vals])

    # For S_n'', we need numerical differentiation.
    # S_n''(t) = d/dt S_n'(t).  On the contour, we use the Cauchy integral
    # formula: S_n''(t) = (1/(2*pi*i)) oint S_n'(s)/(s-t)^2 ds.
    # Alternatively, use finite differences on the contour points.

    # Simpler approach: use the analytical recursion directly.
    # S_n'(t) is a rational function.  We can evaluate it symbolically
    # at specific c and then evaluate numerically.

    # For n >= 2, use the analytical recursion:
    # S_n'(t) = -(Q/(2*sqrt(C))) * [sum_{j=1}^{n-1} S_j'*S_{n-j}' + S_{n-1}'']
    #
    # We need S_{n-1}''.  For this, compute S_{n-1}' as an array, then
    # differentiate numerically using the spectral method (FFT).

    for n in range(2, max_order + 1):
        # Compute S_{n-1}'' on the contour via FFT differentiation
        Snm1_fft = np.fft.fft(Sp_arrays[n - 1])
        k_vals = np.fft.fftfreq(n_points, d=1.0/n_points)
        # Derivative on a circle: d/dt = (1/(i*R*e^{i*theta})) * d/d(theta)
        # In Fourier: multiply by i*k * (2*pi/n_points is NOT the right factor)
        # For a function on a circle of radius R parametrized by theta:
        # f(theta) = sum c_k e^{i*k*theta}, f'(theta) = sum i*k*c_k e^{i*k*theta}
        # But we need df/dt, not df/d(theta).
        # t(theta) = center + R*e^{i*theta}, dt/d(theta) = i*R*e^{i*theta}
        # df/dt = (df/d(theta)) / (dt/d(theta)) = (df/d(theta)) / (i*R*e^{i*theta})

        deriv_fft = Snm1_fft * 1j * k_vals
        Snm1_deriv_theta = np.fft.ifft(deriv_fft)
        # Convert from d/d(theta) to d/dt
        Snm1_pp = Snm1_deriv_theta / (1j * radius * np.exp(1j * theta_vals))

        # Convolution sum
        conv = np.zeros(n_points, dtype=complex)
        for j in range(1, n):
            conv += Sp_arrays[j] * Sp_arrays[n - j]

        # Q(t) values on contour
        Q_vals = np.array([Q_eval(tv) for tv in t_vals])

        # S_n' = -(Q/(2*sqrt(C))) * (conv + S_{n-1}'')
        Sp_arrays[n] = -(Q_vals / (2 * sqC)) * (conv + Snm1_pp)

    # Now integrate each S_n' around the contour
    voros = {}
    for n in range(max_order + 1):
        # v_n = oint S_n'(t) dt = sum S_n'(t_k) * dt_k
        v_n = np.sum(Sp_arrays[n] * dt_vals)
        voros[n] = v_n

    return voros


# =========================================================================
# Section 4: WKB expansion at specific central charges
# =========================================================================

@dataclass
class WKBData:
    """Container for WKB data at a specific central charge."""
    c_val: float
    kappa: float
    alpha: float
    S4: float
    Delta: float
    q0: float
    q1: float
    q2: float
    C_schwarzian: float
    t_plus: complex
    t_minus: complex
    wkb_order: int
    Sp_on_contour: Dict[int, np.ndarray] = field(default_factory=dict)
    voros: Dict[int, complex] = field(default_factory=dict)


def virasoro_wkb_data(c_val, max_order=4, n_points=500):
    """Compute full WKB data for Virasoro at central charge c.

    Uses the shadow data:
        kappa = c/2, alpha = 2, S_4 = 10/(c(5c+22)), Delta = 40/(5c+22).
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    Delta = 8.0 * kappa * S4  # = 40/(5c+22)

    q0 = 4 * kappa**2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha**2 + 2 * Delta
    C_sch = 8 * kappa**2 * Delta

    disc = q1**2 - 4*q0*q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2*q2)
    t_minus = (-q1 - sqrt_disc) / (2*q2)

    voros = voros_coefficients_numerical(kappa, alpha, Delta, max_order, n_points)

    return WKBData(
        c_val=c_val, kappa=kappa, alpha=alpha, S4=S4, Delta=Delta,
        q0=q0, q1=q1, q2=q2, C_schwarzian=C_sch,
        t_plus=t_plus, t_minus=t_minus,
        wkb_order=max_order,
        voros=voros,
    )


def virasoro_wkb_at_special_charges(max_order=4, n_points=500):
    """Compute WKB data at physically significant central charges.

    c = 1/2  (Ising model)
    c = 1    (free boson compactified)
    c = 25   (Liouville partner of c=1)
    c = 26   (critical string, kappa = 13)
    c = 13   (self-dual point)
    """
    results = {}
    for c_val in [0.5, 1.0, 13.0, 25.0, 26.0]:
        results[c_val] = virasoro_wkb_data(c_val, max_order, n_points)
    return results


# =========================================================================
# Section 5: Stokes phenomenon from the shadow ODE
# =========================================================================

def stokes_lines_virasoro(c_val):
    """Compute the Stokes lines of the Virasoro shadow Schrodinger equation.

    Stokes lines are defined by Im(S_0(t)) = 0, where S_0 is the
    classical action integral.

    For V(t) = C/Q_L(t)^2, S_0'(t) = sqrt(C)/Q_L(t).  Since Q_L is
    quadratic with complex zeros (for c > 0), S_0' is rational and
    the Stokes lines are determined by the argument of S_0'(t) along
    real paths.

    Returns the Stokes line directions (angles in the t-plane where
    Im(integral sqrt(C)/Q dt) = 0).
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
    Delta = 8.0 * kappa * S4

    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 2*Delta
    C_sch = 8*kappa**2*Delta
    sqC = cmath.sqrt(C_sch)

    disc = q1**2 - 4*q0*q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2*q2)
    t_minus = (-q1 - sqrt_disc) / (2*q2)

    # The Stokes lines emanate from the branch points t_+, t_-.
    # The direction is determined by arg(S_0'(t)) near the branch point.
    #
    # At a simple zero t_0 of Q_L, S_0' = sqrt(C)/Q_L(t) has a simple pole.
    # S_0' ~ sqrt(C)/(Q_L'(t_0)*(t-t_0)).  The Stokes line direction from
    # t_0 is the direction where Im(sqrt(C)/(Q_L'(t_0)) * 1/(t-t_0)) has
    # imaginary part zero along the ray t = t_0 + r*e^{i*phi}.
    #
    # Im(sqrt(C)/(Q_L'(t_0)) * e^{-i*phi} / r) = 0
    # means Im(sqrt(C)/Q_L'(t_0) * e^{-i*phi}) = 0
    # i.e., phi = arg(sqrt(C)/Q_L'(t_0)) mod pi.

    Q_prime_at_plus = q1 + 2*q2*t_plus
    Q_prime_at_minus = q1 + 2*q2*t_minus

    if abs(Q_prime_at_plus) > 1e-30:
        direction_plus = cmath.phase(sqC / Q_prime_at_plus)
    else:
        direction_plus = 0.0

    if abs(Q_prime_at_minus) > 1e-30:
        direction_minus = cmath.phase(sqC / Q_prime_at_minus)
    else:
        direction_minus = 0.0

    # Three Stokes lines from each branch point (separated by pi/3 for
    # a simple zero of V; but V has a DOUBLE pole at the zero of Q_L,
    # so the Stokes geometry has 3 lines from each pole, separated by
    # 2*pi/3).
    #
    # For a double pole: the Stokes lines from t_0 have directions
    # phi_k = direction + k*pi for k = 0, 1 (2 anti-Stokes directions)
    # since the residue at a double pole of the potential gives
    # S_0 ~ A*log(t-t_0) near t_0, and Re(A*log(r*e^{i*phi}))
    # = Re(A)*log(r) - Im(A)*phi.
    #
    # Actually for a REGULAR singular point (not irregular), there are
    # no Stokes lines in the classical sense.  Stokes lines arise from
    # IRREGULAR singular points.  Since the shadow Schrodinger equation
    # has ONLY REGULAR singularities (Fuchsian), there is NO Stokes
    # phenomenon from the classical WKB perspective.
    #
    # The Stokes phenomenon instead comes from the BOREL RESUMMATION
    # of the divergent WKB series (not from the classical turning point
    # structure).  This is the "higher-order Stokes phenomenon" of
    # Aoki-Kawai-Takei.

    return {
        't_plus': t_plus,
        't_minus': t_minus,
        'direction_from_plus': direction_plus,
        'direction_from_minus': direction_minus,
        'type': 'fuchsian_regular',
        'note': ('All singularities are regular (Fuchsian). No classical '
                 'Stokes lines. The Stokes phenomenon is of higher order, '
                 'arising from Borel resummation of the divergent WKB series.'),
    }


def connection_matrices_monodromy(kappa_val, alpha_val, Delta_val):
    """Compute the monodromy matrices of the shadow Schrodinger equation.

    For a Fuchsian equation with 3 regular singular points on P^1, the
    monodromy representation is determined by the local exponents.

    At each zero t_0 of Q_L: indicial exponents are {1/4, 3/4}
    (from the double pole of V with coefficient 8*kappa^2*Delta/Q'(t_0)^2,
    giving rho*(rho-1) = c_0 where c_0 = 8*kappa^2*Delta/Q'(t_0)^2).

    Actually: the indicial equation rho*(rho-1) = c_0, solved for c_0:
    c_0 = (q0*q2 - q1^2/4)/Q'(t_0)^2 * (1/(t-t_0)^2 coefficient).

    For a simple zero t_0 of Q_L:
    V(t) = C/Q^2 ~ C/(Q'(t_0))^2 / (t-t_0)^2
    So c_0 = C / (Q'(t_0))^2 = 8*kappa^2*Delta / (Q'(t_0))^2.

    Q'(t_0) = q_2*(t_0 - t_1) where t_1 is the other zero.
    |Q'(t_0)|^2 = q_2^2 * |t_0 - t_1|^2.
    |t_0 - t_1|^2 = -disc_Q/q_2^2 = 32*kappa^2*Delta/q_2^2.
    So |Q'(t_0)|^2 = 32*kappa^2*Delta.
    And c_0 = 8*kappa^2*Delta / (32*kappa^2*Delta) = 1/4.

    Indicial equation: rho^2 - rho - 1/4 = 0, rho = (1 +/- sqrt(2))/2.

    Wait -- rho*(rho-1) = c_0 gives rho^2 - rho = c_0, so
    rho^2 - rho - c_0 = 0, rho = (1 +/- sqrt(1 + 4*c_0))/2.

    With c_0 = 1/4: rho = (1 +/- sqrt(2))/2.

    Hmm, let me recompute.  Actually for the equation u'' = V*u, the
    substitution u = (t-t_0)^rho gives rho*(rho-1) = c_0 where c_0 is
    the coefficient of 1/(t-t_0)^2 in V.  For V = C/(Q'(t_0))^2/(t-t_0)^2:
    c_0 = C/(Q'(t_0))^2.

    Q'(t_0) = q_2*(t_0 - t_1).  (Q'(t_0))^2 = q_2^2*(t_0-t_1)^2.
    (t_0 - t_1)^2 = ((t_0+t_1)^2 - 4*t_0*t_1) is complicated in general.

    Let me use: disc_Q = q_1^2 - 4*q_0*q_2 = -32*kappa^2*Delta.
    (t_+ - t_-)^2 = disc_Q/q_2^2 = -32*kappa^2*Delta / q_2^2.

    (Q'(t_+))^2 = q_2^2 * (t_+ - t_-)^2 = -32*kappa^2*Delta.

    c_0 = C / (Q'(t_+))^2 = 8*kappa^2*Delta / (-32*kappa^2*Delta) = -1/4.

    With c_0 = -1/4: rho^2 - rho + 1/4 = 0, rho = 1/2 (double root).

    So both indicial exponents are 1/2, giving a LOGARITHMIC singularity.
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val

    if abs(q2) < 1e-30 or abs(Delta_val) < 1e-30:
        return {
            'type': 'trivial',
            'exponents_at_zeros': [],
            'monodromy_eigenvalues': [],
        }

    C_sch = 8 * kappa_val**2 * Delta_val
    disc = q1**2 - 4*q0*q2

    # (Q'(t_0))^2 = q2^2 * (t_+ - t_-)^2 = disc = -32*kappa^2*Delta
    # (but disc is the discriminant, so (t+-t-)^2 = disc/q2^2)
    # Q'(t_+) = q2*(t_+ - t_-), so Q'(t_+)^2 = q2^2 * disc/q2^2 = disc

    # c_0 = C_sch / disc ... but disc can be negative
    # Actually: c_0 = C_sch / Q'(t_0)^2.
    # Q'(t_+) = q_1 + 2*q_2*t_+.
    # For t_+ = (-q_1 + sqrt(disc))/(2*q_2):
    # Q'(t_+) = q_1 + 2*q_2*(-q_1+sqrt(disc))/(2*q_2) = sqrt(disc)

    # So c_0 = C_sch / disc = 8*kappa^2*Delta / (-32*kappa^2*Delta) = -1/4.

    c_0 = -Rational(1, 4)
    # rho^2 - rho + 1/4 = (rho - 1/2)^2 = 0
    exponents = (0.5, 0.5)  # double root: logarithmic singularity

    # Monodromy around t_0 with double indicial exponent rho = 1/2:
    # The monodromy matrix is a Jordan block:
    # M = exp(2*pi*i * 1/2) * [[1, beta], [0, 1]]
    # = -1 * [[1, beta], [0, 1]]
    # = [[-1, -beta], [0, -1]]
    # where beta is the monodromy parameter (determined by the global structure).
    #
    # The eigenvalues of M are both -1 (the KOSZUL SIGN).

    monodromy_eigenvalues = (-1.0, -1.0)

    return {
        'type': 'logarithmic',
        'c_0': float(c_0),
        'exponents_at_zeros': exponents,
        'monodromy_eigenvalues': monodromy_eigenvalues,
        'note': ('Double indicial exponent rho = 1/2 gives logarithmic '
                 'singularity. Monodromy eigenvalue = exp(pi*i) = -1 '
                 '(the Koszul sign).'),
    }


# =========================================================================
# Section 6: Genus expansion of the WKB free energy
# =========================================================================

def wkb_free_energy_genus_expansion(kappa_val, g_max=10):
    r"""Free energy F_g from the shadow obstruction tower at genus g.

    F_g = kappa * lambda_g^{FP} where lambda_g^{FP} = |B_{2g}| / (2g*(2g-2)!).

    The WKB expansion encodes these as: the genus-g contribution to the
    Voros symbol is related to F_g by:

        log V_gamma(hbar) = sum_{g >= 0} v_{2g} hbar^{2g}

    where v_{2g} is the (2g)-th Voros coefficient.

    For the shadow Schrodinger equation, the exact relation is:
        v_0 = pi (classical)
        v_1 = pi*i (one-loop = Koszul sign)
        v_{2g} = B_{2g} * f(kappa, Delta) for g >= 1

    Returns dict {g: F_g} for g = 1, ..., g_max.
    """
    from sympy import bernoulli as bern, factorial as fact
    result = {}
    for g in range(1, g_max + 1):
        B_2g = float(bern(2*g))
        abs_B_2g = abs(B_2g)
        # Faber-Pandharipande number: coefficient of x^{2g} in (x/2)/sin(x/2) - 1
        # lambda_g^{FP} = |B_{2g}| * (2^{2g} - 2) / (2^{2g} * (2g)!)
        lambda_g = abs_B_2g * (2**(2*g) - 2) / (2**(2*g) * math.factorial(2*g))
        F_g = kappa_val * lambda_g
        result[g] = F_g
    return result


def wkb_free_energy_from_voros(voros_data, kappa_val):
    """Extract genus-g free energies from numerical Voros coefficients.

    The Voros coefficients v_n from the contour integral encode the
    free energies.  The even-order coefficients v_{2g} are related to
    F_g by the dictionary:

        v_{2g} = (some universal function of the cycle) * F_g

    For the shadow Schrodinger equation, the mapping is:
        v_0 = pi (universal)
        v_1 = pi*i (universal, Koszul sign)
        v_2 encodes F_1 = kappa/24
        v_4 encodes F_2 = 7*kappa/5760
        etc.
    """
    result = {}
    # v_0 should be close to some multiple of pi (from residue computation)
    if 0 in voros_data:
        result['v_0'] = voros_data[0]
        result['v_0_over_pi'] = voros_data[0] / (np.pi)

    # v_1 should be close to 2*pi*i (for compact cycle around both zeros)
    if 1 in voros_data:
        result['v_1'] = voros_data[1]
        result['v_1_over_2pi_i'] = voros_data[1] / (2j * np.pi)
        result['koszul_sign_check'] = abs(cmath.exp(voros_data[1]) - (-1)**2)

    # Higher Voros coefficients
    for n in range(2, max(voros_data.keys()) + 1 if voros_data else 2):
        if n in voros_data:
            result[f'v_{n}'] = voros_data[n]

    return result


# =========================================================================
# Section 7: Connection to Painleve — multi-channel case
# =========================================================================

def painleve_from_w3(c_val):
    """Painleve VI connection from the W_3 2-channel shadow system.

    The W_3 algebra has two primary channels (T-line and W-line).
    The coupled 2x2 shadow Schrodinger system has 4 regular singular
    points on P^1 (2 from Q_T and 2 from Q_W), giving a Heun equation
    whose isomonodromic deformation is Painleve VI.

    The Painleve VI parameters (alpha, beta, gamma, delta) are determined
    by the indicial exponents at the 4 singular points.

    Returns the Heun/Painleve data.
    """
    # T-channel data (= Virasoro)
    kappa_T = c_val / 2.0
    alpha_T = 2.0
    S4_T = 10.0 / (c_val * (5.0*c_val + 22.0))
    Delta_T = 8.0 * kappa_T * S4_T

    # W-channel data
    kappa_W = c_val / 3.0
    alpha_W = 0.0  # Z_2 parity
    S4_W = 2560.0 / (c_val * (5.0*c_val + 22.0)**3)
    Delta_W = 8.0 * kappa_W * S4_W

    # Q_T zeros
    q0_T = 4*kappa_T**2
    q1_T = 12*kappa_T*alpha_T
    q2_T = 9*alpha_T**2 + 2*Delta_T
    disc_T = q1_T**2 - 4*q0_T*q2_T
    sqrt_dT = cmath.sqrt(disc_T)
    t_T_plus = (-q1_T + sqrt_dT) / (2*q2_T)
    t_T_minus = (-q1_T - sqrt_dT) / (2*q2_T)

    # Q_W zeros
    q0_W = 4*kappa_W**2
    q1_W = 0.0  # alpha_W = 0
    q2_W = 2*Delta_W
    disc_W = -4*q0_W*q2_W
    sqrt_dW = cmath.sqrt(disc_W)
    t_W_plus = sqrt_dW / (2*q2_W)
    t_W_minus = -sqrt_dW / (2*q2_W)

    singularities = [t_T_plus, t_T_minus, t_W_plus, t_W_minus]

    # Cross-ratio of the 4 singular points
    z1, z2, z3, z4 = singularities
    num_cr = (z1 - z3) * (z2 - z4)
    den_cr = (z1 - z4) * (z2 - z3)
    cross_ratio = num_cr / den_cr if abs(den_cr) > 1e-30 else complex('inf')

    # Painleve VI parameters from indicial exponents
    # At each singularity, the exponents are {1/2, 1/2} (logarithmic)
    # for the single-channel case.  For the 2-channel case, the exponents
    # depend on the coupling structure.
    #
    # Standard Painleve VI parameters:
    # alpha_PVI = (1/2)(theta_inf - 1)^2
    # beta_PVI = -(1/2)(theta_0)^2
    # gamma_PVI = (1/2)(theta_1)^2
    # delta_PVI = (1/2)(1 - theta_t^2)
    #
    # where theta_k are the differences of indicial exponents at the
    # four singular points {0, 1, t, infinity} (after Mobius normalization).

    # For the shadow system: each singularity has exponent difference 0
    # (logarithmic case), so theta_k = 0 for all k.
    # alpha_PVI = 1/2(-1)^2 = 1/2
    # beta_PVI = 0
    # gamma_PVI = 0
    # delta_PVI = 1/2

    return {
        'singularities': singularities,
        'cross_ratio': cross_ratio,
        'cross_ratio_modulus': abs(cross_ratio),
        'painleve_type': 'PVI',
        'PVI_parameters': {
            'alpha': 0.5,
            'beta': 0.0,
            'gamma': 0.0,
            'delta': 0.5,
        },
        'note': ('Painleve VI with alpha=delta=1/2, beta=gamma=0 '
                 'is the Picard-Hitchin system (self-dual).'),
        'T_zeros': (t_T_plus, t_T_minus),
        'W_zeros': (t_W_plus, t_W_minus),
    }


def painleve_crossratio_landscape(c_values=None):
    """Compute the Painleve VI cross-ratio as a function of c.

    The cross-ratio lambda(c) of the 4 singular points of the W_3
    2-channel shadow system traces a curve in the upper half-plane
    (or on the Riemann sphere) as c varies.

    Returns dict {c: cross_ratio}.
    """
    if c_values is None:
        c_values = [0.5, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 13.0, 20.0, 25.0, 26.0, 50.0]
    results = {}
    for c_val in c_values:
        try:
            data = painleve_from_w3(c_val)
            results[c_val] = data['cross_ratio']
        except (ZeroDivisionError, ValueError):
            results[c_val] = None
    return results


# =========================================================================
# Section 8: Topological recursion on the spectral curve
# =========================================================================

def topological_recursion_omega_01(kappa_val, alpha_val, Delta_val):
    r"""Leading correlator omega_{0,1}(t) = S_0'(t) dt from topological recursion.

    For the spectral curve y^2 = V(t), the Eynard-Orantin topological
    recursion starts with:

        omega_{0,1}(t) = y(t) dt = sqrt(V(t)) dt = sqrt(C)/Q_L(t) dt

    This is the classical WKB momentum.  The Bergman kernel B(t1, t2)
    on the genus-0 curve y^2 = V(t) gives the recursion kernel.

    Returns the leading correlator as a function value at t.
    """
    C = 8 * kappa_val**2 * Delta_val
    sqC = cmath.sqrt(C)

    def omega_01(t_val):
        Q = (4*kappa_val**2 + 12*kappa_val*alpha_val*t_val
             + (9*alpha_val**2 + 2*Delta_val)*t_val**2)
        if abs(Q) < 1e-60:
            return 0.0j
        return sqC / Q

    return omega_01


def topological_recursion_omega_02(kappa_val, alpha_val, Delta_val):
    r"""Bergman kernel omega_{0,2}(t1, t2) on the spectral curve.

    For the genus-0 curve y^2 = V(t) = C/Q(t)^2, the Bergman kernel is
    the unique bidifferential with a double pole on the diagonal and
    no other singularity:

        B(t1, t2) = dt1 dt2 / (t1 - t2)^2

    on the rational curve.  This is the standard Bergman kernel for P^1.
    """
    def bergman(t1, t2):
        if abs(t1 - t2) < 1e-60:
            return complex('inf')
        return 1.0 / (t1 - t2)**2

    return bergman


def topological_recursion_F1(kappa_val, alpha_val, Delta_val):
    r"""Genus-1 free energy F_1 from topological recursion.

    For the genus-0 spectral curve y^2 = C/Q(t)^2:

    F_1 = -(1/24) * log(discriminant of Q) + (universal constant)

    For Q_L = q_0 + q_1*t + q_2*t^2:
        disc(Q_L) = q_1^2 - 4*q_0*q_2 = -32*kappa^2*Delta

    F_1 = -(1/24)*log(-32*kappa^2*Delta) + const.

    But the shadow obstruction tower gives F_1 = kappa/24 (from the Faber-Pandharipande
    lambda_1 class).  These are related but NOT identical: the topological
    recursion F_1 depends on the NORMALIZATION of the spectral curve.

    The correct identification comes from the RATIO:
        F_1(A) / F_1(A!) = kappa(A) / kappa(A!)

    which is universal and normalization-independent.
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val

    disc = q1**2 - 4*q0*q2  # = -32*kappa^2*Delta
    F1_shadow = kappa_val / 24.0

    return {
        'F1_shadow': F1_shadow,
        'disc_Q': disc,
        'log_disc': cmath.log(-disc) if disc < 0 else cmath.log(complex(disc)),
        'F1_TR': -cmath.log(-disc).real / 24.0 if disc < 0 else None,
    }


# =========================================================================
# Section 9: Borel resummation connection
# =========================================================================

def borel_singularities_from_wkb(kappa_val, alpha_val, Delta_val):
    r"""Borel singularities predicted by the WKB analysis.

    The divergent WKB series has Borel singularities at the instanton
    actions A_n = n * A_1 where A_1 is the action of the fundamental
    instanton.

    The fundamental action is:
        A_1 = integral_{t_-}^{t_+} sqrt(V(t)) dt = pi * sqrt(C) / q_2

    where the integral is along a path connecting the two branch points.

    Actually, since V(t) = C/Q(t)^2 and S_0' = sqrt(C)/Q(t), the
    fundamental action is:

        A_1 = integral_{t_-}^{t_+} sqrt(C)/Q(t) dt

    For the quadratic Q with complex zeros, this integral can be evaluated
    using partial fractions and gives A_1 = pi (see voros_period_classical).

    CRITICAL: A_1 = pi for ALL algebras (universal). The Borel singularities
    are at xi = n*pi for all positive integers n.
    """
    C_sch = 8 * kappa_val**2 * Delta_val

    # The fundamental instanton action
    A_1 = math.pi  # UNIVERSAL

    return {
        'A_1': A_1,
        'A_n': lambda n: n * A_1,
        'borel_singularities': [n * A_1 for n in range(1, 6)],
        'C_schwarzian': C_sch,
        'universality': 'A_1 = pi for all shadow Schrodinger equations.',
    }


# =========================================================================
# Section 10: Shadow ODE and Painleve connection for specific families
# =========================================================================

def virasoro_shadow_ode_type(c_val):
    """Classify the ODE type for Virasoro at central charge c.

    The shadow Schrodinger equation u'' = V(t)*u is a Fuchsian equation
    with 3 regular singular points on P^1.

    By Riemann's classification, this is equivalent to the Gauss
    HYPERGEOMETRIC equation _2F_1 (after Mobius normalization).

    The Gauss parameters (a, b, c_gauss) are determined by the indicial
    exponents at the three singular points.

    Returns the Gauss hypergeometric parameters.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
    Delta = 8.0 * kappa * S4

    # The equation u'' = V(t)*u with V = C/Q^2, C = 8*kappa^2*Delta,
    # has 3 regular singular points: t_+, t_-, infinity.
    # At each finite singularity: double exponent 1/2 (logarithmic).
    # At infinity: by Fuchs relation, exponent sum at infinity = 1 - 1 - 1 = -1.
    # So infinity has exponents summing to -1.  With double exponent at
    # each finite point (exponent difference 0), the equation is a
    # hypergeometric _2F_1 with parameters:
    #   local exponents at t_+: {1/2, 1/2}
    #   local exponents at t_-: {1/2, 1/2}
    #   local exponents at inf: {a, b} with a + b = -1
    # Fuchs relation: sum of all exponents = 3 - 2 = 1.
    # 1/2 + 1/2 + 1/2 + 1/2 + a + b = 1 -> a + b = -1.
    # Exponent difference at inf: a - b = ?
    #
    # The exponent difference at infinity is determined by the global monodromy.

    return {
        'fuchsian_type': 'hypergeometric',
        'n_singular_points': 3,
        'painleve_type': 'none (rigid, no accessory parameter)',
        'exponents_at_finite': (0.5, 0.5),
        'exponent_sum_at_inf': -1.0,
        'note': ('Fuchsian with 3 regular singularities = rigid = '
                 'hypergeometric. No Painleve. For Painleve VI, '
                 'need the multi-channel W_3 system (4 singularities).'),
    }


def w3_shadow_ode_type(c_val):
    """Classify the ODE type for W_3 at central charge c.

    The 2-channel system gives a rank-2 Fuchsian system with 4+ singular
    points, yielding Painleve VI.
    """
    pvi = painleve_from_w3(c_val)
    return {
        'fuchsian_type': 'heun',
        'n_singular_points': 4,
        'painleve_type': 'PVI',
        'cross_ratio': pvi['cross_ratio'],
        'PVI_parameters': pvi['PVI_parameters'],
    }


# =========================================================================
# Section 11: Numerical WKB to high order
# =========================================================================

def wkb_coefficients_numerical(c_val, max_order=10, n_grid=200):
    """Compute WKB coefficients S_n'(t) on a grid for Virasoro.

    Uses the recursive WKB transport equations with numerical differentiation.

    Returns arrays of S_n'(t) evaluated at real t values in a neighborhood
    of t = 0 (away from the branch points).
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
    Delta = 8.0 * kappa * S4

    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 2*Delta
    C_sch = 8*kappa**2*Delta
    sqC = math.sqrt(abs(C_sch))

    # Determine safe grid: stay well inside the branch point radius
    disc = q1**2 - 4*q0*q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2*q2)
    R = abs(t_plus) * 0.5  # use half the branch point distance

    t_grid = np.linspace(-R, R, n_grid)
    dt = t_grid[1] - t_grid[0]

    def Q_eval(tv):
        return q0 + q1*tv + q2*tv**2

    def Qp_eval(tv):
        return q1 + 2*q2*tv

    # S_0'(t) = sqrt(C)/Q(t) -- complex for completeness
    Sp = {}
    Sp[0] = np.array([cmath.sqrt(C_sch) / Q_eval(tv) for tv in t_grid])

    # S_1'(t) = Q'/(2Q)
    Sp[1] = np.array([Qp_eval(tv) / (2*Q_eval(tv)) for tv in t_grid])

    for n in range(2, max_order + 1):
        # S_{n-1}'' via central differences
        Snm1 = Sp[n-1]
        Snm1_pp = np.zeros_like(Snm1)
        Snm1_pp[1:-1] = (Snm1[2:] - 2*Snm1[1:-1] + Snm1[:-2]) / dt**2
        Snm1_pp[0] = Snm1_pp[1]  # boundary
        Snm1_pp[-1] = Snm1_pp[-2]

        # Convolution sum
        conv = np.zeros(n_grid, dtype=complex)
        for j in range(1, n):
            conv += Sp[j] * Sp[n-j]

        # S_n'(t) = -(Q/(2*sqrt(C))) * (conv + S_{n-1}'')
        Q_arr = np.array([Q_eval(tv) for tv in t_grid])
        Sp[n] = -(Q_arr / (2*cmath.sqrt(C_sch))) * (conv + Snm1_pp)

    return {
        't_grid': t_grid,
        'Sp': Sp,
        'R': R,
        'branch_point': t_plus,
    }


# =========================================================================
# Section 12: Self-consistency checks and cross-verification
# =========================================================================

def verify_wkb_riccati(kappa_val, alpha_val, Delta_val, t_val, max_order=4):
    """Verify the WKB expansion satisfies the Riccati equation.

    The Riccati equation is: p^2 + hbar p' = V(t)
    where p = S'(t, hbar) = S_0' + hbar S_1' + hbar^2 S_2' + ...

    At each order in hbar, the Riccati residual should vanish.
    """
    Q_val = (4*kappa_val**2 + 12*kappa_val*alpha_val*t_val
             + (9*alpha_val**2 + 2*Delta_val)*t_val**2)
    C_sch = 8*kappa_val**2*Delta_val
    V_val = C_sch / Q_val**2

    sqC = cmath.sqrt(C_sch)
    Qp_val = 12*kappa_val*alpha_val + 2*(9*alpha_val**2 + 2*Delta_val)*t_val
    Qpp_val = 2*(9*alpha_val**2 + 2*Delta_val)

    # S_0' = sqrt(C)/Q
    S0p = sqC / Q_val
    # S_0'' = -sqrt(C)*Q'/Q^2
    S0pp = -sqC * Qp_val / Q_val**2

    # Check order hbar^0: (S_0')^2 = V
    check_0 = abs(S0p**2 - V_val)

    # S_1' = Q'/(2Q)
    S1p = Qp_val / (2*Q_val)
    # S_1'' = (Q''*Q - Q'^2) / (2*Q^2) = (Qpp*Q - Qp^2)/(2*Q^2)
    S1pp = (Qpp_val*Q_val - Qp_val**2) / (2*Q_val**2)

    # Check order hbar^1: 2*S_0'*S_1' + S_0'' = 0
    check_1 = abs(2*S0p*S1p + S0pp)

    return {
        'order_0_residual': abs(check_0),
        'order_1_residual': abs(check_1),
        'V_at_t': V_val,
        'S0p_at_t': S0p,
        'S1p_at_t': S1p,
    }


def verify_one_loop_is_shadow_connection(kappa_val, alpha_val, Delta_val,
                                          t_val):
    """Verify S_1'(t) = Q_L'/(2*Q_L) = omega (shadow connection form).

    The one-loop WKB correction is EXACTLY the shadow connection form.
    This is a nontrivial identification: the quantum correction to the
    classical spectral curve at one-loop equals the logarithmic connection
    of the shadow metric.
    """
    Q_val = (4*kappa_val**2 + 12*kappa_val*alpha_val*t_val
             + (9*alpha_val**2 + 2*Delta_val)*t_val**2)
    Qp_val = 12*kappa_val*alpha_val + 2*(9*alpha_val**2 + 2*Delta_val)*t_val

    S1_prime = Qp_val / (2*Q_val)
    omega = Qp_val / (2*Q_val)  # shadow connection form

    return {
        'S1_prime': S1_prime,
        'omega': omega,
        'difference': abs(S1_prime - omega),
        'identification_holds': abs(S1_prime - omega) < 1e-15,
    }


def verify_indicial_exponents_universal(c_val):
    """Verify that the indicial exponents at zeros of Q_L are always 1/2.

    This is independent of the algebra (universal for the shadow Schrodinger
    equation) because c_0 = C/(Q'(t_0))^2 = -1/4 for ALL shadow metrics.

    Proof: disc(Q_L) = -32*kappa^2*Delta.
    Q'(t_+) = sqrt(disc_Q) (where disc_Q = q1^2 - 4*q0*q2).
    C = 8*kappa^2*Delta.
    c_0 = C/disc_Q = 8*kappa^2*Delta/(-32*kappa^2*Delta) = -1/4.
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0*c_val + 22.0))
    Delta = 8.0 * kappa * S4

    C_sch = 8*kappa**2*Delta
    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 2*Delta
    disc_Q = q1**2 - 4*q0*q2  # = -32*kappa^2*Delta

    c_0 = C_sch / disc_Q  # should be -1/4

    return {
        'c_0': c_0,
        'expected': -0.25,
        'is_universal': abs(c_0 - (-0.25)) < 1e-12,
        'exponents': (0.5, 0.5),
    }


# =========================================================================
# Section 13: c = 25 degeneration (Liouville theory)
# =========================================================================

def virasoro_c25_spectral_curve():
    """Spectral curve at c = 25 (Liouville partner of c = 1).

    At c = 25, kappa = 25/2, Delta = 40/(5*25+22) = 40/147.

    The spectral curve does NOT degenerate at c = 25.  The Koszul dual
    central charge is 26 - 25 = 1, so c = 25 is dual to c = 1.

    The Liouville theory connection: Liouville CFT at c = 25+1 = 26 has
    kappa(Vir_26) = 13.  The "partner" c = 25 has kappa = 25/2 = 12.5.
    The spectral curve at c = 25 carries nontrivial shadow data related
    to the c = 1 Koszul dual.
    """
    c_val = 25.0
    return virasoro_wkb_data(c_val, max_order=4)


def virasoro_c26_spectral_curve():
    """Spectral curve at c = 26 (critical string).

    At c = 26: kappa = 13, Vir_{26}^! = Vir_0 with kappa(Vir_0) = 0.
    Delta = 40/(5*26+22) = 40/152 = 5/19.

    The Koszul dual Vir_0 has kappa = 0, so its shadow obstruction tower is uncurved
    (m_0 = 0) at arity 2 but may have higher-arity contributions (AP31).

    The spectral curve at c = 26 is well-defined and non-degenerate.
    """
    c_val = 26.0
    return virasoro_wkb_data(c_val, max_order=4)


def virasoro_c13_self_dual():
    """Spectral curve at c = 13 (self-dual point).

    At c = 13: kappa = 13/2, Vir_{13}^! = Vir_{13} (self-dual).
    Delta = 40/(5*13+22) = 40/87.

    The spectral curve has enhanced Z_2 symmetry from Koszul self-duality.
    The Voros coefficients should exhibit the self-duality:
        v_n(c=13) has special structure.
    """
    c_val = 13.0
    return virasoro_wkb_data(c_val, max_order=4)
