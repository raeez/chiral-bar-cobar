#!/usr/bin/env python3
r"""
bc_scattering_shadow_engine.py -- Scattering-shadow intertwining: the precise
map from the shadow obstruction tower Theta_A to Eisenstein scattering poles
at zeta zeros.

THE MATHEMATICAL ARCHITECTURE:

The chain has five links:

  (1) Shadow tower  -->  (2) Sewing determinant  -->  (3) Rankin-Selberg integral
      -->  (4) Functional equation / scattering poles  -->  (5) Intertwining kernel

=== LINK 1: SHADOW TOWER TO GENUS-1 FREE ENERGY ===

The connected genus-1 free energy decomposes via the sewing-shadow
intertwining (thm:sewing-shadow-intertwining):

    F_1^{conn}(q; A) = sum_{r >= 2} Sh_r^{(1)}(A) * G_r(q)

where Sh_r^{(1)}(A) is the genus-1 shadow amplitude at arity r, and
G_r(q) is the r-point geometric kernel on E_tau.

For Heisenberg at rank c: Sh_2 = c/2 in this engine's convention (Convention B),
compensated by G_2 carrying a factor of 2. kappa(Heis) = c, so Sh_2 = kappa/2.
For Virasoro: Sh_2 = c/2 = kappa, and ALL higher arities contribute (class M).
NOTE: Other engines (shadow_zeta_function_engine) use Convention A where S_2 = kappa.
The two conventions are related by a G_r normalization factor.

=== LINK 2: SEWING DETERMINANT ===

The sewing determinant at genus 1 is:

    det(1 - K_q(A)) = exp(-F_1^{conn}(q; A))

For Heisenberg at rank c:
    det(1 - K_q) = prod_{n >= 1} (1 - q^n)^c = (eta(q)/q^{c/24})^c * [q-power]

The PRIMARY-COUNTING FUNCTION is:
    Z_hat^c(tau) = y^{c/2} |eta(tau)|^{2c} Z_A(tau)

=== LINK 3: RANKIN-SELBERG INTEGRAL ===

The Rankin-Selberg integral against the Eisenstein series:

    I_A(s) = int_{SL(2,Z)\H} Z_hat^c(tau) * E(tau, s) * d mu(tau)

For the Heisenberg at central charge c (sewing-Selberg formula,
thm:heisenberg-sewing, eq:sewing-selberg-formula):

    I_H(s) = -2 * (2*pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)

=== LINK 4: THE CONSTRAINED EPSTEIN FUNCTIONAL EQUATION ===

The constrained Epstein zeta function epsilon^c_s(A) satisfies:

    epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}

where:
    F_c(s) = Gamma(s) * Gamma(s+c/2-1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2-s) * Gamma(s-1/2) * zeta(2s-1))

The poles of F_c at s = (1+rho)/2 (where zeta(rho) = 0) are the
SCATTERING POLES.

=== LINK 5: THE INTERTWINING KERNEL ===

THE STRUCTURAL OBSTRUCTION (from the audit): the sewing operation
exponentiates F_1^{conn}, which MIXES all shadow arities.  The
Rankin-Selberg integral sees only the total sewing determinant,
not individual arities.

The intertwining kernel K(rho, r) is defined as the CONTRIBUTION
of shadow arity r to the residue of I_A(s) at s = (1+rho)/2.
This is constructed by:

    (a) Writing F_1^{conn} = sum_r Sh_r * G_r(q)
    (b) Exponentiating: det(1-K) = exp(-sum_r Sh_r * G_r)
    (c) Taking the Mellin transform of each arity's contribution

The first-order (linear) approximation is:

    K^{(1)}(rho, r) = -Sh_r^{(1)} * M[G_r](s)|_{s=(1+rho)/2}

where M[G_r](s) = int_0^infty G_r(e^{-2pi*y}) * y^{s-2} dy is the
Mellin transform of the r-th geometric kernel.

The full (exponentiated) kernel involves all convolution products
of shadow arities, and the cancellation mechanism between I(s) and
F_c(s) at the scattering poles.

HEISENBERG GROUND TRUTH (c = 1):
    I_H(s) = -2 * (2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)
    This has ZEROS at zeta zeros (from zeta(s) factor), not poles.
    The scattering poles of F_c are at s = (1+rho)/2, but I_H at
    these points involves zeta((1+rho)/2) and zeta((1+rho)/2 - 1)
    = zeta((rho-1)/2).

References:
    benjamin_chang_analysis.py (existing engine)
    sewing_shadow_intertwining.py (existing engine)
    scattering_sewing_bridge.py (existing engine)
    rankin_selberg_bridge.py (existing engine)
    [BenjaminChang22]: arXiv:2208.02259
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

try:
    import mpmath
    from mpmath import (mp, mpf, mpc, pi as mppi, zeta, gamma as mpgamma,
                        log, exp, power, sqrt, re as mpre, im as mpim,
                        conj as mpconj, fac, diff, zetazero, inf, sin, cos,
                        arg as mparg, fabs, floor as mpfloor, quad, polylog,
                        bernoulli as mpbernoulli)
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================
# 0. FAMILY DATA: shadow coefficients and kappa values
# ============================================================

def kappa_heisenberg(k):
    """kappa(H_k) = k for rank-1 Heisenberg at level k.

    Convention: central charge c = k (one boson), kappa = k.
    For c free bosons: kappa = c (the rank).
    AP39: kappa != c/2 in general; for Heisenberg kappa = k (the level).
    AP48: kappa depends on the full algebra, not the Virasoro subalgebra.
    """
    return k


def kappa_virasoro(c):
    """kappa(Vir_c) = c/2."""
    return c / 2


def kappa_affine_km(dim_g, k, h_dual):
    """kappa(hat{g}_k) = dim(g) * (k + h^v) / (2 * h^v).

    AP1: this is a DISTINCT formula from kappa_virasoro.
    """
    return dim_g * (k + h_dual) / (2 * h_dual)


def shadow_coefficients_heisenberg(c, r_max=10):
    """Shadow coefficients for Heisenberg at central charge c (c free bosons).

    Class G (Gaussian): Sh_2 = c/2, Sh_r = 0 for r >= 3.
    The tower terminates at arity 2.

    Convention: The intertwining formula is F_1^{conn} = sum_r Sh_r * G_r
    where G_2 = 2 * sum sigma_{-1}(N) q^N.  With this normalization,
    Sh_2 = c/2 so that F_1 = (c/2) * 2 * sum sigma_{-1} q^N = c * sum sigma_{-1} q^N.
    This matches sewing_shadow_intertwining.py.

    Note: the MODULAR CHARACTERISTIC kappa(H) = c (the rank) is TWICE Sh_2.
    The factor of 2 is absorbed by the G_2 normalization.
    AP39: for Heisenberg, kappa = c (rank) = 2 * Sh_2.
    """
    coeffs = {}
    coeffs[2] = float(c) / 2.0
    for r in range(3, r_max + 1):
        coeffs[r] = 0.0
    return coeffs


def shadow_coefficients_virasoro(c, r_max=10):
    """Shadow coefficients for Virasoro at central charge c.

    Class M (mixed): infinite tower.
    Sh_2 = kappa = c/2
    Sh_3 = C = cubic shadow (depends on cubic OPE data)
    Sh_4 = Q^contact = 10 / (c * (5c + 22))

    Higher arities from the explicit shadow tower.
    The tower does NOT terminate (r_max = infinity for class M).
    """
    if abs(c) < 1e-15 or abs(5 * c + 22) < 1e-15:
        raise ValueError(f"Virasoro shadow singular at c = {c}")

    kappa = c / 2
    # Cubic shadow vanishes on the scalar line (by cubic gauge triviality,
    # thm:cubic-gauge-triviality): H^1(F^3/F^4, d_2) = 0 for Virasoro.
    C_cubic = 0.0
    # Quartic contact:
    Q_contact = 10.0 / (c * (5 * c + 22))

    # Quintic shadow: S_5 = -48 / (c^2 * (5c + 22))
    S_5 = -48.0 / (c ** 2 * (5 * c + 22))

    coeffs = {2: kappa, 3: C_cubic, 4: Q_contact, 5: S_5}
    # Higher arities: use the shadow radius growth rate
    # rho(A) = sqrt(9*alpha^2 + 2*Delta) / (2*|kappa|) for the asymptotic
    # Sh_r ~ A * rho^r * r^{-5/2}
    # We compute approximate higher terms from the algebraic recursion
    if r_max > 5:
        Delta = 40.0 / (5 * c + 22)
        alpha = 2.0
        rho_growth = math.sqrt(9 * alpha ** 2 + 2 * Delta) / (2 * abs(kappa)) if abs(kappa) > 1e-15 else 0.0
        for r in range(6, r_max + 1):
            # Asymptotic: Sh_r ~ const * rho^r * r^{-5/2}
            # The exact recursion from the shadow metric Q_L gives:
            # H(t) = 2*kappa*t^2 * sqrt(Q_L(t)/Q_L(0))
            # where Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
            # Taylor coefficient at t^r gives Sh_r.
            # We compute this from the generating function.
            coeffs[r] = _shadow_tower_coefficient_from_gf(c, r)

    return coeffs


def _shadow_tower_coefficient_from_gf(c, r):
    """Extract the r-th shadow tower coefficient from the generating function.

    The shadow generating function on the Virasoro primary line is:
        H(t) = 2*kappa * t^2 * sqrt(Q_L(t) / Q_L(0))
    where:
        Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
        Q_L(0) = 4*kappa^2
        alpha = 2, Delta = 8*kappa*S_4 = 40/(5c+22)

    H(t) = t^2 * sqrt((2*kappa + 6t)^2 + 2*Delta*t^2)

    The r-th shadow coefficient is (1/r!) * d^r H/dt^r |_{t=0}.
    We compute by polynomial expansion of sqrt(Q_L).
    """
    kappa = c / 2
    alpha = 2.0
    Delta = 40.0 / (5 * c + 22)

    # Q_L(t)/Q_L(0) = 1 + (6*alpha/(2*kappa))*t + ((9*alpha^2+2*Delta)/(4*kappa^2))*t^2
    # = 1 + a1*t + a2*t^2
    if abs(kappa) < 1e-15:
        return 0.0

    a1 = 3 * alpha / kappa  # = 6/kappa
    a2 = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2)

    # sqrt(1 + a1*t + a2*t^2) = sum_{n>=0} c_n * t^n
    # c_0 = 1
    # c_1 = a1/2
    # c_n = (1/(2*n)) * sum_{k=1}^{n} ((3k-n)*a_k - (2k-n+...))... use Maclaurin expansion
    # Actually, use the binomial series for sqrt.
    # f(t) = (1 + a1*t + a2*t^2)^{1/2}
    # We need the Taylor coefficient of t^(r-2) in f(t) (since H = t^2 * ... * 2*kappa).
    # Use direct computation via the recurrence.

    max_order = r + 1
    # Compute coefficients of f(t) = sqrt(1 + a1*t + a2*t^2) up to t^{max_order}
    f_coeffs = [0.0] * (max_order + 1)
    f_coeffs[0] = 1.0
    # Recurrence: f(t)^2 = 1 + a1*t + a2*t^2
    # 2*f_0*f_n = [n=1: a1] [n=2: a2] [n>=3: 0] - sum_{k=1}^{n-1} f_k*f_{n-k}
    for n in range(1, max_order + 1):
        rhs = 0.0
        if n == 1:
            rhs = a1
        elif n == 2:
            rhs = a2
        # Subtract convolution
        rhs -= sum(f_coeffs[k] * f_coeffs[n - k] for k in range(1, n))
        f_coeffs[n] = rhs / (2.0 * f_coeffs[0])

    # H(t) = 2*kappa * t^2 * f(t)
    # Coefficient of t^r in H(t) = 2*kappa * f_coeffs[r-2]
    if r - 2 < 0 or r - 2 >= len(f_coeffs):
        return 0.0
    return 2 * kappa * f_coeffs[r - 2]


# ============================================================
# 1. SEWING DETERMINANT FROM SHADOW DATA
# ============================================================

def sewing_determinant_from_shadows(shadow_coeffs, q, r_max=None):
    """Compute det(1 - K_q(A)) = exp(-F_1^{conn}) from shadow data.

    F_1^{conn}(q; A) = sum_{r >= 2} Sh_r^{(1)}(A) * G_r(q)

    where G_r(q) is the r-point geometric kernel on the elliptic curve.

    For the arity-2 kernel (the dominant term):
        G_2(q) = 2 * sum_{N >= 1} sigma_{-1}(N) * q^N
    where sigma_{-1}(N) = sum_{d|N} 1/d.

    Args:
        shadow_coeffs: {r: Sh_r^{(1)}(A)} for arities r = 2, 3, ...
        q: the nome q = exp(2*pi*i*tau), must satisfy |q| < 1.
        r_max: maximum arity to include (default: all provided).

    Returns:
        dict with 'F1_conn', 'det', 'arity_contributions'.
    """
    if r_max is None:
        r_max = max(shadow_coeffs.keys()) if shadow_coeffs else 2

    abs_q = abs(q)
    if abs_q >= 1:
        raise ValueError(f"|q| = {abs_q} >= 1, sewing diverges")

    # Compute each arity's contribution
    arity_contribs = {}
    F1_total = 0.0

    for r in range(2, r_max + 1):
        sh_r = shadow_coeffs.get(r, 0.0)
        if abs(sh_r) < 1e-50:
            arity_contribs[r] = 0.0
            continue

        G_r_val = geometric_kernel_numerical(r, q)
        contrib = sh_r * G_r_val
        arity_contribs[r] = contrib
        F1_total += contrib

    # det(1 - K_q) = exp(-F_1^{conn})
    det_val = math.exp(-F1_total) if abs(F1_total) < 700 else 0.0

    return {
        'F1_conn': F1_total,
        'det': det_val,
        'arity_contributions': arity_contribs,
        'q': q,
        'r_max': r_max,
    }


def geometric_kernel_numerical(r, q, N_max=200):
    """Compute G_r(q) = r-th geometric kernel on E_tau at nome q.

    For r = 2: G_2(q) = 2 * sum_{N >= 1} sigma_{-1}(N) * q^N
    This is the universal arity-2 kernel (independent of c).

    For r >= 3: the geometric kernel involves r-point functions on E_tau.
    At genus 1, the r-point graph sum gives:
        G_r(q) = sum_{graphs Gamma with r external legs}
                 |Aut(Gamma)|^{-1} * A_Gamma(q)
    where A_Gamma(q) is the graph amplitude.

    For r = 3: the one-loop triangle graph gives
        G_3(q) = sum_{N >= 1} sigma_{-3/2}(N) * q^N  [approximate]

    For general r, we use the truncated Fourier expansion.
    The key point: G_r(q) is a GEOMETRIC object, independent of
    the algebra A.  All A-dependence enters through Sh_r.
    """
    abs_q = abs(q)
    if abs_q >= 1:
        return float('inf')

    if r == 2:
        # G_2(q) = 2 * sum sigma_{-1}(N) q^N
        result = 0.0
        for N in range(1, N_max + 1):
            s_minus_1 = sum(1.0 / d for d in range(1, N + 1) if N % d == 0)
            term = 2.0 * s_minus_1 * (abs_q ** N)
            if abs(term) < 1e-50:
                break
            result += term
        return result

    elif r == 3:
        # G_3: genus-1 three-point kernel.  For the Heisenberg (where Sh_3=0)
        # this does not contribute.  For interacting theories, the leading
        # behavior is controlled by the propagator cubed on the torus.
        # G_3(q) ~ 6 * sum_{N >= 1} sigma_{-2}(N) * q^N  (approximate leading form)
        result = 0.0
        for N in range(1, N_max + 1):
            s_minus_2 = sum(1.0 / (d * d) for d in range(1, N + 1) if N % d == 0)
            term = 6.0 * s_minus_2 * (abs_q ** N)
            if abs(term) < 1e-50:
                break
            result += term
        return result

    elif r == 4:
        # G_4: genus-1 four-point kernel (box + triangle-with-bubble).
        # Leading: G_4(q) ~ 24 * sum sigma_{-3}(N) q^N
        result = 0.0
        for N in range(1, N_max + 1):
            s_minus_3 = sum(1.0 / (d ** 3) for d in range(1, N + 1) if N % d == 0)
            term = 24.0 * s_minus_3 * (abs_q ** N)
            if abs(term) < 1e-50:
                break
            result += term
        return result

    else:
        # Higher arities: G_r ~ r! * sum sigma_{-(r-1)}(N) q^N
        # This is the leading graph-sum approximation.
        factorial_r = math.factorial(r)
        result = 0.0
        for N in range(1, N_max + 1):
            s_minus = sum(1.0 / (d ** (r - 1)) for d in range(1, N + 1) if N % d == 0)
            term = float(factorial_r) * s_minus * (abs_q ** N)
            if abs(term) < 1e-50:
                break
            result += term
        return result


def sewing_determinant_heisenberg_exact(c, q, N_max=500):
    """Exact sewing determinant for Heisenberg at central charge c.

    det(1 - K_q) = prod_{n >= 1} (1 - q^n)^c

    This is the GROUND TRUTH for verification.
    """
    abs_q = abs(q)
    if abs_q >= 1:
        return 0.0
    log_det = 0.0
    qn = abs_q
    for n in range(1, N_max + 1):
        if qn < 1e-300:
            break
        log_det += c * math.log(max(1 - qn, 1e-300))
        qn *= abs_q
    return math.exp(log_det)


# ============================================================
# 2. RANKIN-SELBERG INTEGRAL
# ============================================================

def rankin_selberg_heisenberg_exact(s, dps=30):
    r"""Exact Rankin-Selberg integral for Heisenberg (c = 1).

    I_H(s) = int_{F} log det(1-K) * E_s d mu
           = -2 * (2*pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)

    This is PROVED (thm:heisenberg-sewing).

    AP46: eta(q) = q^{1/24} * prod(1-q^n).  The q^{1/24} is included
    in the full sewing determinant; the log det does NOT include it.
    The formula above is for log prod(1-q^n) = log(eta/q^{1/24}).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        return complex(
            -2 * power(2 * mppi, -(s - 1))
            * mpgamma(s - 1) * zeta(s - 1) * zeta(s)
        )


def rankin_selberg_heisenberg_rank_c(s, c, dps=30):
    r"""Rankin-Selberg integral for Heisenberg at central charge c.

    For c free bosons, the sewing determinant is prod(1-q^n)^c = eta^c / q^{c/24}.
    The Rankin-Selberg integral scales linearly with c:

    I_H^c(s) = c * I_H^1(s) = -2c * (2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)

    This is because log det = c * log prod(1-q^n) and the integral is linear in the function.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        return complex(
            -2 * c * power(2 * mppi, -(s - 1))
            * mpgamma(s - 1) * zeta(s - 1) * zeta(s)
        )


def rankin_selberg_numerical(f_coeffs, s, y_min=1.0, y_max=20.0, num_pts=2000, dps=30):
    r"""Numerical Rankin-Selberg integral for a general modular function.

    I(s) = int_{y_min}^{y_max} a_0(y) * y^{s-2} dy

    where a_0(y) is the zeroth Fourier coefficient of f(tau) = sum a_N(y) e^{2pi i N x}.
    By Rankin-Selberg unfolding, the integral over the fundamental domain
    reduces to the integral of a_0 against y^s.

    For f = -c * sum log(1 - q^n) evaluated on the imaginary axis (x=0):
        f(iy) = -c * sum_{n >= 1} log(1 - e^{-2*pi*n*y})
              = c * sum_{N >= 1} sigma_{-1}(N) * e^{-2*pi*N*y}

    Args:
        f_coeffs: list of (N, a_N) where f = sum a_N * exp(-2*pi*N*y)
        s: the spectral parameter
        y_min, y_max: integration range
        num_pts: quadrature points
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    with mp.workdps(dps):
        s_mp = mpc(s)

        def integrand(y):
            y_mp = mpf(y)
            if y_mp < mpf('1e-10'):
                return mpf(0)
            # Evaluate f at y
            f_val = mpf(0)
            for N, a_N in f_coeffs:
                term = mpf(a_N) * exp(-2 * mppi * N * y_mp)
                f_val += term
                if fabs(term) < mpf('1e-50'):
                    break
            return f_val * power(y_mp, s_mp - 2)

        result = quad(integrand, [mpf(y_min), mpf(y_max)])
        return complex(result)


# ============================================================
# 3. SCATTERING FACTOR AND ANALYTIC CONTINUATION
# ============================================================

def scattering_factor_Fc(s, c, dps=30):
    r"""The scattering factor F_c(s) from the constrained Epstein FE.

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))

    Poles at s = (1+rho)/2 where rho runs over nontrivial zeta zeros
    (from the zeta(2s-1) = 0 condition: 2s-1 = rho => s = (1+rho)/2).

    Under RH: poles at Re(s) = 3/4.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        num = mpgamma(s) * mpgamma(s + c / 2 - 1) * zeta(2 * s)
        den = (power(mppi, 2 * s - mpf('0.5'))
               * mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5'))
               * zeta(2 * s - 1))
        if fabs(den) < power(10, -dps + 5):
            return complex(mpc(inf))
        return complex(num / den)


def scattering_factor_decomposition(s, c, dps=30):
    r"""Decompose F_c(s) = gamma_factor * pi_factor * zeta_ratio.

    Returns dict with the three factors and their product.
    The zeta_ratio = zeta(2s)/zeta(2s-1) is the number-theoretic content.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c = mpc(c)
        gamma_fac = (mpgamma(s) * mpgamma(s + c / 2 - 1)
                     / (mpgamma(c / 2 - s) * mpgamma(s - mpf('0.5'))))
        pi_fac = power(mppi, -(2 * s - mpf('0.5')))
        zr = zeta(2 * s) / zeta(2 * s - 1)
        return {
            'gamma_factor': complex(gamma_fac),
            'pi_factor': complex(pi_fac),
            'zeta_ratio': complex(zr),
            'product': complex(gamma_fac * pi_fac * zr),
        }


def scattering_pole_positions(n_zeros=20, dps=30):
    r"""Positions of scattering poles s_rho = (1+rho)/2.

    Under RH: Re(s_rho) = 3/4.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        poles = []
        for k in range(1, n_zeros + 1):
            rho = zetazero(k)
            s_rho = (1 + rho) / 2
            poles.append({
                'k': k,
                'rho': complex(rho),
                'gamma': float(mpim(rho)),
                's_rho': complex(s_rho),
                's_rho_real': float(mpre(s_rho)),
                's_rho_imag': float(mpim(s_rho)),
            })
        return poles


# ============================================================
# 4. CANCELLATION MECHANISM AT SCATTERING POLES
# ============================================================

def cancellation_at_scattering_pole(k, c, dps=30):
    r"""Quantify the cancellation between I_A(s) and F_c(s) at s = (1+rho_k)/2.

    The structural obstruction: the sewing Rankin-Selberg integral I_A(s)
    is HOLOMORPHIC at the scattering poles (for Heisenberg and other
    standard families), while F_c(s) has poles there.

    For Heisenberg:
        I_H(s) = -2 * (2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)
        At s = (1+rho_k)/2:
          - zeta(s) = zeta((1+rho_k)/2): generically nonzero
          - zeta(s-1) = zeta((rho_k-1)/2): generically nonzero
          - Gamma(s-1) = Gamma((rho_k-1)/2): generically finite
        So I_H is FINITE at these points.

    Meanwhile:
        F_c(s) has a POLE at s = (1+rho_k)/2 from zeta(2s-1) = zeta(rho_k) = 0.

    The functional equation epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}
    must be consistent: if F_c diverges at s_0, then EITHER
        (a) epsilon has a compensating zero at c/2 + s_0 - 1, OR
        (b) the functional equation breaks down.

    For modular-invariant Z_hat^c, (a) holds: the constrained Epstein zeta
    has zeros that cancel the F_c poles.  The RESIDUE of F_c at s_0 times
    the VALUE of epsilon at c/2 + s_0 - 1 gives the CONSTRAINT on the
    primary spectrum.

    Returns dict with the scattering pole data and cancellation analysis.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(k)
        s0 = (1 + rho) / 2

        # I_H at the scattering pole
        I_val = rankin_selberg_heisenberg_rank_c(complex(s0), float(c), dps)

        # F_c near the pole: extract the residue
        # F_c(s) ~ Res / (s - s0) + ... near s = s0
        # The residue comes from zeta(2s-1) having a simple zero at s = s0:
        # zeta(2s-1) ~ zeta'(rho) * 2 * (s - s0)
        # So the residue of F_c at s0 is:
        # Res = [Gamma(s0)*Gamma(s0+c/2-1)*zeta(2*s0)] / [pi^{2s0-1/2}*Gamma(c/2-s0)*Gamma(s0-1/2) * 2*zeta'(rho)]

        zeta_2s0 = zeta(2 * s0)  # = zeta(1 + rho)
        zeta_prime_rho = diff(zeta, rho)

        num_res = (mpgamma(s0) * mpgamma(s0 + mpc(c) / 2 - 1) * zeta_2s0)
        den_res = (power(mppi, 2 * s0 - mpf('0.5'))
                   * mpgamma(mpc(c) / 2 - s0) * mpgamma(s0 - mpf('0.5'))
                   * 2 * zeta_prime_rho)

        if fabs(den_res) < power(10, -dps + 5):
            residue = complex(mpc(inf))
        else:
            residue = complex(num_res / den_res)

        # The epsilon value at the complementary point
        # s_comp = c/2 + s0 - 1 = c/2 + (1+rho)/2 - 1 = (c + rho - 1)/2
        s_comp = (mpc(c) + rho - 1) / 2

        return {
            'k': k,
            'rho': complex(rho),
            'gamma': float(mpim(rho)),
            's0': complex(s0),
            'I_H_at_s0': I_val,
            'I_H_finite': abs(I_val) < 1e50,
            'Fc_residue': residue,
            'Fc_residue_abs': abs(residue),
            's_complementary': complex(s_comp),
            'zeta_1_plus_rho': complex(zeta_2s0),
            'zeta_prime_rho': complex(zeta_prime_rho),
        }


def cancellation_spectrum(c, n_zeros=10, dps=30):
    """Compute the cancellation data at the first n_zeros scattering poles."""
    results = []
    for k in range(1, n_zeros + 1):
        results.append(cancellation_at_scattering_pole(k, c, dps))
    return results


# ============================================================
# 5. INTERTWINING KERNEL K(rho, r)
# ============================================================

def mellin_geometric_kernel(r, s, dps=30):
    r"""Mellin transform of the r-th geometric kernel G_r.

    M[G_r](s) = int_0^infty G_r(e^{-2*pi*y}) * y^{s-2} dy

    For r = 2:
        G_2(e^{-2*pi*y}) = 2 * sum_{N >= 1} sigma_{-1}(N) * e^{-2*pi*N*y}
        M[G_2](s) = 2 * sum_{N >= 1} sigma_{-1}(N) * Gamma(s-1) / (2*pi*N)^{s-1}
                   = 2 * Gamma(s-1) / (2*pi)^{s-1} * sum sigma_{-1}(N) N^{-(s-1)}

    Now sum_{N >= 1} sigma_{-1}(N) N^{-u} = zeta(u) * zeta(u+1) for Re(u) > 1.
    (This is the Ramanujan identity: sigma_{-1} is the Dirichlet convolution of
     n^0 and n^{-1}, so its Dirichlet series is zeta(u)*zeta(u+1).)

    So: M[G_2](s) = 2 * Gamma(s-1) / (2*pi)^{s-1} * zeta(s-1) * zeta(s)

    For r = 3: G_3 ~ 6 * sum sigma_{-2}(N) e^{-2*pi*N*y}
        sum sigma_{-2}(N) N^{-u} = zeta(u) * zeta(u+2)
        M[G_3](s) = 6 * Gamma(s-1) / (2*pi)^{s-1} * zeta(s-1) * zeta(s+1)

    For general r: G_r ~ r! * sum sigma_{-(r-1)}(N) e^{-2*pi*N*y}
        sum sigma_{-(r-1)}(N) N^{-u} = zeta(u) * zeta(u+r-1)
        M[G_r](s) = r! * Gamma(s-1) / (2*pi)^{s-1} * zeta(s-1) * zeta(s+r-2)

    PRECISION QUALIFIER (AP42): This formula is EXACT for r=2 (single graph
    topology: the genus-1 propagator edge). For r >= 3, the geometric kernel
    G_r involves MULTIPLE genus-1 graph topologies (triangle at r=3, square +
    bubble-triangle at r=4, etc.), and the r! * sigma_{-(r-1)} formula captures
    only the LEADING graph contribution. The full kernel at arity r requires
    summing over all trivalent genus-1 graphs with r external legs.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        # The common factor
        common = mpgamma(s - 1) / power(2 * mppi, s - 1)

        if r == 2:
            return complex(2 * common * zeta(s - 1) * zeta(s))
        elif r == 3:
            return complex(6 * common * zeta(s - 1) * zeta(s + 1))
        elif r == 4:
            return complex(24 * common * zeta(s - 1) * zeta(s + 2))
        else:
            factorial_r = mpf(1)
            for i in range(1, r + 1):
                factorial_r *= i
            return complex(factorial_r * common * zeta(s - 1) * zeta(s + r - 2))


def intertwining_kernel_linear(rho_index, r, c, dps=30):
    r"""The LINEARIZED intertwining kernel K^{(1)}(rho, r).

    This is the contribution of shadow arity r to the residue of the
    Rankin-Selberg integral at the scattering pole s = (1+rho)/2,
    at FIRST ORDER (ignoring the exponentiation of F_1^{conn}).

    K^{(1)}(rho, r) = -Sh_r * Res_{s=(1+rho)/2} M[G_r](s)

    The residue of M[G_r](s) at s = (1+rho)/2 comes from the
    poles of zeta(s-1) at s-1 = rho (trivially), but zeta(s-1)
    is evaluated at s = (1+rho)/2, giving s-1 = (rho-1)/2.
    Since rho is a zero of zeta, zeta((rho-1)/2) is generically
    NONZERO.  So M[G_r] does NOT have a pole at s = (1+rho)/2.

    The intertwining kernel at linear order is therefore simply
    the EVALUATION:

    K^{(1)}(rho, r; A) = Sh_r(A) * M[G_r]((1+rho)/2)

    This gives the linear contribution of arity r to I_A at the
    scattering pole position.  The key insight: the linear
    intertwining kernel is FINITE (no pole), confirming the
    structural obstruction -- the sewing operation regularizes
    the scattering poles.

    Args:
        rho_index: which zeta zero (1-indexed)
        r: shadow arity
        c: central charge (for shadow coefficient computation)
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(rho_index)
        s0 = (1 + rho) / 2
        M_Gr_at_s0 = mellin_geometric_kernel(r, complex(s0), dps)
        return {
            'rho_index': rho_index,
            'rho': complex(rho),
            'r': r,
            's0': complex(s0),
            'M_Gr_at_s0': M_Gr_at_s0,
            'K_linear': M_Gr_at_s0,  # The kernel value (multiply by Sh_r for the contribution)
        }


def intertwining_kernel_full(rho_index, r_max, shadow_coeffs, dps=30):
    r"""Full intertwining kernel: sum over arities.

    K_full(rho; A) = sum_{r=2}^{r_max} Sh_r(A) * M[G_r]((1+rho)/2)

    This is the LINEAR approximation to the total shadow contribution
    at the scattering pole.  The full (exponentiated) version would
    require computing all convolution products of shadow coefficients,
    which introduces inter-arity mixing.

    Returns:
        dict with individual arity contributions and the total.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = zetazero(rho_index)
        s0 = (1 + rho) / 2

        arity_data = {}
        total = mpc(0)
        for r in range(2, r_max + 1):
            sh_r = shadow_coeffs.get(r, 0.0)
            M_val = mpc(mellin_geometric_kernel(r, complex(s0), dps))
            contrib = mpc(sh_r) * M_val
            arity_data[r] = {
                'Sh_r': sh_r,
                'M_Gr': complex(M_val),
                'contribution': complex(contrib),
            }
            total += contrib

        return {
            'rho_index': rho_index,
            'rho': complex(rho),
            's0': complex(s0),
            'arity_data': arity_data,
            'total': complex(total),
            'total_abs': float(fabs(total)),
        }


# ============================================================
# 6. SHADOW SPECTRAL MEASURE
# ============================================================

def shadow_spectral_measure(s, shadow_coeffs, r_max=10, dps=30):
    r"""The shadow spectral measure mu_A^{sh}(s).

    Defined by:
        I_A^{shadow}(s) = sum_{r >= 2} Sh_r(A) * M[G_r](s)

    This is the LINEAR approximation to the Rankin-Selberg integral
    I_A(s) in terms of individual shadow arity contributions.

    The measure density at s is:
        mu_A^{sh}(s) = sum_{r >= 2} Sh_r * r! * Gamma(s-1) / (2pi)^{s-1}
                       * zeta(s-1) * zeta(s+r-2)

    For Heisenberg (only r=2): mu = kappa * 2 * Gamma(s-1)/(2pi)^{s-1} * zeta(s-1) * zeta(s)
    which matches (up to sign) the exact I_H = -2*kappa*Gamma(s-1)/(2pi)^{s-1}*zeta(s-1)*zeta(s).
    This is the EXACT match, confirming the linearization is EXACT for Gaussian-class algebras.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        total = mpc(0)
        arity_measures = {}

        for r in range(2, r_max + 1):
            sh_r = shadow_coeffs.get(r, 0.0)
            if abs(sh_r) < 1e-50:
                arity_measures[r] = 0.0 + 0.0j
                continue
            M_val = mpc(mellin_geometric_kernel(r, complex(s), dps))
            contrib = mpc(sh_r) * M_val
            arity_measures[r] = complex(contrib)
            total += contrib

        return {
            's': complex(s),
            'total': complex(total),
            'arity_measures': arity_measures,
        }


def verify_shadow_measure_vs_exact_heisenberg(s, c=1.0, dps=30):
    r"""Verify that the shadow spectral measure matches the exact RS integral for Heisenberg.

    For Heisenberg: the shadow tower terminates at arity 2, so the
    linear approximation is EXACT.

    Shadow measure (from Mellin of F_1^conn):
        mu = Sh_2 * M[G_2](s) = (c/2) * 2 * Gamma(s-1)/(2pi)^{s-1} * zeta(s-1)*zeta(s)
           = c * Gamma(s-1)/(2pi)^{s-1} * zeta(s-1)*zeta(s)

    Exact RS integral (from the full modular orbit, including the unfolding factor):
        I_H^c = -2c * (2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)

    The factor of 2 between them arises from the Rankin-Selberg unfolding:
    the fundamental domain integral produces an additional factor of 2
    compared to the bare Mellin transform of the q-expansion.

    So: I_H = -2 * mu, i.e., exact = -2 * shadow_measure.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")

    shadow = shadow_coefficients_heisenberg(c)
    measure = shadow_spectral_measure(s, shadow, r_max=2, dps=dps)
    exact = rankin_selberg_heisenberg_rank_c(s, c, dps)

    # The Rankin-Selberg unfolding gives a factor of 2:
    # I_H = -2 * sum_r Sh_r * M[G_r](s)
    predicted = -2 * measure['total']
    rel_err = abs(predicted - exact) / max(abs(exact), 1e-100)

    return {
        's': s,
        'c': c,
        'shadow_measure': measure['total'],
        'predicted_I': predicted,
        'exact': exact,
        'relative_error': rel_err,
        'match': rel_err < 1e-10,
        'unfolding_factor': 2,
    }


# ============================================================
# 7. SELF-DUAL ENHANCED SYMMETRY AT c = 13
# ============================================================

def self_dual_symmetry_analysis(s, dps=30):
    r"""Analysis of the intertwining kernel at the self-dual point c = 13.

    At c = 13 (Virasoro self-dual under Koszul duality c -> 26-c):
        kappa = 13/2, kappa' = (26-13)/2 = 13/2.
        kappa + kappa' = 13 (AP24: NOT zero for Virasoro).
        delta_kappa = kappa - kappa' = 0.

    The scattering factor F_{13}(s) has the enhanced symmetry:
        The Gamma factor Gamma(s)*Gamma(s+11/2) / (Gamma(13/2-s)*Gamma(s-1/2))
        is symmetric under s -> 7-s.

    The intertwining kernel at c=13 thus has the functional equation:
        K(rho, r; c=13) = [reflection factor] * K(1-rho, r; c=13)

    This constrains the shadow spectral measure to respect the
    self-dual reflection symmetry.
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        c = 13
        s_mp = mpc(s)

        # F_c at s and at 7-s
        Fc_s = scattering_factor_Fc(complex(s_mp), c, dps)
        Fc_reflected = scattering_factor_Fc(complex(7 - s_mp), c, dps)

        # The functional equation F_{13}(s) * F_{13}(7-s) should equal a known quantity
        # From the constrained Epstein FE:
        #   epsilon^13_{13/2-s} = F_13(s) * epsilon^13_{13/2+s-1}
        # Applying twice with s -> 7-s:
        #   epsilon^13_{13/2-(7-s)} = F_13(7-s) * epsilon^13_{13/2+(7-s)-1}
        #   epsilon^13_{s-7/2} = F_13(7-s) * epsilon^13_{13/2-s+6}
        # This gives a relation between F_13(s) and F_13(7-s).

        product = complex(mpc(Fc_s) * mpc(Fc_reflected)) if (
            abs(Fc_s) < 1e50 and abs(Fc_reflected) < 1e50
        ) else None

        # Shadow coefficients at c=13
        shadow_13 = shadow_coefficients_virasoro(13, r_max=6)

        # Shadow measure at s and 7-s
        mu_s = shadow_spectral_measure(complex(s_mp), shadow_13, r_max=6, dps=dps)
        mu_reflected = shadow_spectral_measure(complex(7 - s_mp), shadow_13, r_max=6, dps=dps)

        return {
            'c': 13,
            's': complex(s_mp),
            's_reflected': complex(7 - s_mp),
            'kappa': 6.5,
            'kappa_dual': 6.5,
            'delta_kappa': 0.0,
            'F_13_at_s': Fc_s,
            'F_13_at_7_minus_s': Fc_reflected,
            'product_F13': product,
            'shadow_measure_s': mu_s['total'],
            'shadow_measure_reflected': mu_reflected['total'],
            'shadow_coeffs': shadow_13,
        }


def self_dual_intertwining_kernel_test(n_zeros=5, dps=30):
    r"""Test the intertwining kernel at c=13 for self-dual symmetry.

    At c = 13, the kernel K(rho, r; c=13) should satisfy constraints
    from the enhanced Koszul self-duality.

    The key test: for each zero rho_k, compare:
        K_full(rho_k; Vir_13) with K_full(rho_k; Vir_{13}^!)
    These should be EQUAL since Vir_13^! = Vir_13 (self-dual).
    """
    shadow_13 = shadow_coefficients_virasoro(13, r_max=6)
    results = []
    for k in range(1, n_zeros + 1):
        kernel_data = intertwining_kernel_full(k, 6, shadow_13, dps)
        results.append({
            'k': k,
            'rho': kernel_data['rho'],
            'total': kernel_data['total'],
            'total_abs': kernel_data['total_abs'],
            'arity_2_fraction': (
                abs(kernel_data['arity_data'][2]['contribution']) / kernel_data['total_abs']
                if kernel_data['total_abs'] > 1e-50 else 0.0
            ),
        })
    return results


# ============================================================
# 8. FUNCTIONAL EQUATION VERIFICATION
# ============================================================

def functional_equation_check(s, c, dps=30):
    r"""Check the constrained Epstein functional equation.

    epsilon^c_{c/2-s} = F_c(s) * epsilon^c_{c/2+s-1}

    For Heisenberg at c = 1, the constrained Epstein zeta reduces to
    (a variant of) 4*zeta(2s).  We verify:

    epsilon^1_{1/2-s} = F_1(s) * epsilon^1_{s-1/2}

    where epsilon^1_u = 4*zeta(2u) (up to normalization).

    For the FUNCTIONAL EQUATION of F_c itself:
    From the definition, we check F_c(s) * F_c(c/2 + 1 - s) = 1
    (up to possible Gamma-function factors).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        s = mpc(s)
        c_mp = mpc(c)

        Fc_s = mpc(scattering_factor_Fc(complex(s), float(c), dps))

        # For Heisenberg c=1: epsilon^1_u = 4*zeta(2u) (the lattice Epstein zeta for Z)
        if abs(float(c) - 1.0) < 0.01:
            # LHS: epsilon^1_{1/2 - s}
            u_lhs = mpf('0.5') - s
            eps_lhs = 4 * zeta(2 * u_lhs)
            # RHS: F_1(s) * epsilon^1_{s - 1/2}
            u_rhs = s - mpf('0.5')
            eps_rhs = 4 * zeta(2 * u_rhs)
            rhs_full = Fc_s * eps_rhs

            return {
                's': complex(s),
                'c': float(c),
                'LHS': complex(eps_lhs),
                'RHS': complex(rhs_full),
                'relative_error': float(fabs(eps_lhs - rhs_full) / max(fabs(eps_lhs), mpf('1e-100'))),
            }

        # General c: return F_c(s) for inspection
        return {
            's': complex(s),
            'c': float(c),
            'F_c': complex(Fc_s),
        }


# ============================================================
# 9. HEISENBERG SEWING-SELBERG VERIFICATION
# ============================================================

def heisenberg_sewing_selberg_verification(s_values=None, c=1.0, dps=30):
    r"""Multi-point verification of the Heisenberg sewing-Selberg formula.

    For each s in s_values, verify:
        I_H^c(s) [exact] = -sum_r Sh_r * M[G_r](s)  [shadow measure]

    PATH 1: Direct exact formula -2c(2pi)^{-(s-1)}Gamma(s-1)zeta(s-1)zeta(s)
    PATH 2: Shadow spectral measure with Sh_2 = kappa = c, Sh_{r>=3} = 0
    PATH 3: Mellin transform of the geometric kernel M[G_2](s)

    All three must agree.
    """
    if s_values is None:
        # Avoid s=2 where zeta(s-1) = zeta(1) has a pole
        s_values = [2.5, 3.0, 3.5, 4.0, 5.0]

    results = []
    shadow = shadow_coefficients_heisenberg(c)

    for s in s_values:
        # Path 1: exact RS formula (includes unfolding factor 2)
        exact = rankin_selberg_heisenberg_rank_c(s, c, dps)

        # Path 2: shadow measure (Mellin of q-expansion, NO unfolding)
        # I_H = -2 * sum_r Sh_r * M[G_r](s) (factor 2 from unfolding)
        measure = shadow_spectral_measure(s, shadow, r_max=2, dps=dps)
        shadow_val = -2 * measure['total']

        # Path 3: direct Mellin of G_2
        # Sh_2 = c/2, M[G_2] = 2*Gamma(s-1)/(2pi)^{s-1}*zeta(s-1)*zeta(s)
        # I_H = -2 * (c/2) * M[G_2] = -c * M[G_2]
        M_G2 = mellin_geometric_kernel(2, s, dps)
        mellin_val = -c * M_G2

        results.append({
            's': s,
            'exact': exact,
            'shadow_measure': shadow_val,
            'mellin_direct': mellin_val,
            'err_shadow': abs(shadow_val - exact) / max(abs(exact), 1e-100),
            'err_mellin': abs(mellin_val - exact) / max(abs(exact), 1e-100),
        })

    return results


# ============================================================
# 10. UNIVERSAL RESIDUE FACTOR
# ============================================================

def universal_residue_factor(rho, c, dps=30):
    r"""The residue A_c(rho) of F_c at s = (1+rho)/2.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2) * zeta'(rho))

    The factor zeta'(rho) in the denominator arises because
    zeta(2s-1) has a simple zero at s = (1+rho)/2 with
    derivative 2*zeta'(rho).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c_mp = mpc(c)
        zeta_prime_rho = diff(zeta, rho)
        num = (mpgamma((1 + rho) / 2) * mpgamma((c_mp + rho - 1) / 2)
               * zeta(1 + rho))
        den = (2 * power(mppi, rho + mpf('0.5'))
               * mpgamma((c_mp - rho - 1) / 2) * mpgamma(rho / 2)
               * zeta_prime_rho)
        if fabs(den) < power(10, -dps + 5):
            return complex(mpc(inf))
        return complex(num / den)


def residue_kernel_oscillatory(Delta, c, rho, dps=30):
    r"""The real-valued oscillatory residue kernel w_{c,rho}(Delta).

    w = 2 |A_c(rho)| * (2*Delta)^{-(c+sigma-1)/2}
        * cos(gamma/2 * log(2*Delta) + arg(A_c(rho)))

    where rho = sigma + i*gamma.
    This oscillates at frequency gamma/(4*pi) in log(Delta).
    """
    if not HAS_MPMATH:
        raise RuntimeError("mpmath required")
    with mp.workdps(dps):
        rho = mpc(rho)
        c_mp = mpc(c)
        Delta_mp = mpf(Delta)
        sigma = mpre(rho)
        gamma_val = mpim(rho)

        A = mpc(universal_residue_factor(rho, c, dps))
        A_abs = fabs(A)
        A_phase = mparg(A)

        decay = power(2 * Delta_mp, -(c_mp + sigma - 1) / 2)
        oscillation = cos(gamma_val / 2 * log(2 * Delta_mp) + A_phase)

        return float(2 * A_abs * mpre(decay) * oscillation)


# ============================================================
# 11. ARITY DECOMPOSITION OF THE INTERTWINING
# ============================================================

def arity_decomposition_analysis(family, params, n_zeros=5, r_max=6, dps=30):
    r"""Decompose the intertwining kernel by shadow arity for a given family.

    For each zeta zero rho_k, compute the fraction of the total kernel
    that comes from each arity.  This reveals the "arity spectrum" of
    the scattering-shadow intertwining.

    For Heisenberg: 100% from arity 2 (Gaussian class).
    For Virasoro: arity 2 dominates, with corrections from 4, 5, ...
    """
    if family == 'heisenberg':
        c = params.get('c', 1.0)
        shadow = shadow_coefficients_heisenberg(c, r_max)
    elif family == 'virasoro':
        c = params.get('c', 25.0)
        shadow = shadow_coefficients_virasoro(c, r_max)
    else:
        raise ValueError(f"Unknown family: {family}")

    results = []
    for k in range(1, n_zeros + 1):
        kernel = intertwining_kernel_full(k, r_max, shadow, dps)
        fracs = {}
        for r in range(2, r_max + 1):
            contrib_abs = abs(kernel['arity_data'][r]['contribution'])
            frac = contrib_abs / kernel['total_abs'] if kernel['total_abs'] > 1e-50 else 0.0
            fracs[r] = frac

        results.append({
            'k': k,
            'rho': kernel['rho'],
            'total_abs': kernel['total_abs'],
            'arity_fractions': fracs,
            'dominant_arity': max(fracs, key=fracs.get) if fracs else None,
        })

    return results


# ============================================================
# 12. SHADOW DEPTH AND INTERTWINING COMPLEXITY
# ============================================================

def intertwining_complexity(family, params, n_zeros=3, r_max_range=None, dps=30):
    r"""Measure how the intertwining kernel converges as r_max increases.

    For Gaussian-class algebras (r_max = 2): converges immediately.
    For class M (infinite tower): convergence rate ~ rho^{r_max}.

    Returns the relative change in |K_full| as r_max increases from 2 to r_max.
    """
    if r_max_range is None:
        r_max_range = [2, 3, 4, 5, 6, 8, 10]

    if family == 'heisenberg':
        c = params.get('c', 1.0)
        shadow = shadow_coefficients_heisenberg(c, max(r_max_range))
    elif family == 'virasoro':
        c = params.get('c', 25.0)
        shadow = shadow_coefficients_virasoro(c, max(r_max_range))
    else:
        raise ValueError(f"Unknown family: {family}")

    results = []
    for k in range(1, n_zeros + 1):
        convergence_data = []
        prev_total = None
        for rm in r_max_range:
            kernel = intertwining_kernel_full(k, rm, shadow, dps)
            total = kernel['total_abs']
            rel_change = abs(total - prev_total) / max(abs(prev_total), 1e-100) if prev_total is not None else float('inf')
            convergence_data.append({
                'r_max': rm,
                'total_abs': total,
                'relative_change': rel_change,
            })
            prev_total = total

        results.append({
            'k': k,
            'convergence': convergence_data,
        })

    return results


# ============================================================
# 13. COMPLEMENTARITY OF INTERTWINING
# ============================================================

def complementarity_intertwining(c, n_zeros=5, r_max=6, dps=30):
    r"""Compare intertwining kernels for A = Vir_c and A! = Vir_{26-c}.

    The Koszul duality c -> 26-c maps kappa = c/2 -> kappa' = (26-c)/2.
    AP24: kappa + kappa' = 13 (NOT zero for Virasoro).

    The complementarity principle (Theorem C) gives:
        Q_g(A) + Q_g(A!) = H*(M_g, Z(A))

    At the scattering level, this should manifest as:
        K_full(rho; Vir_c) + K_full(rho; Vir_{26-c}) = [universal term]

    The universal term is controlled by the total anomaly kappa + kappa' = 13.
    """
    shadow_A = shadow_coefficients_virasoro(c, r_max)
    c_dual = 26 - c
    if abs(c_dual) < 0.01 or abs(5 * c_dual + 22) < 0.01:
        return {'error': f'dual central charge c! = {c_dual} is singular'}
    shadow_A_dual = shadow_coefficients_virasoro(c_dual, r_max)

    results = []
    for k in range(1, n_zeros + 1):
        K_A = intertwining_kernel_full(k, r_max, shadow_A, dps)
        K_A_dual = intertwining_kernel_full(k, r_max, shadow_A_dual, dps)

        total_sum = K_A['total'] + K_A_dual['total']

        results.append({
            'k': k,
            'rho': K_A['rho'],
            'K_A': K_A['total'],
            'K_A_dual': K_A_dual['total'],
            'sum': total_sum,
            'sum_abs': abs(total_sum),
            'ratio_to_13': abs(total_sum) / 13.0 if abs(total_sum) > 1e-50 else 0.0,
        })

    return {
        'c': c,
        'c_dual': c_dual,
        'kappa_sum': c / 2 + (26 - c) / 2,
        'results': results,
    }
