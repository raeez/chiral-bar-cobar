#!/usr/bin/env python3
r"""
bc_residue_atlas_engine.py -- Comprehensive atlas of the universal residue
factor A_c(rho) at nontrivial zeros of the Riemann zeta function, across
all standard chiral algebra families.

THE MATHEMATICAL CONTENT:

The Benjamin-Chang programme (arXiv:2208.02259) derives a constrained
Epstein functional equation for scalar primary operators in 2D CFTs with
U(1)^c symmetry.  The scattering factor

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s - 1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))

has poles at s = (1+rho)/2 where rho ranges over nontrivial zeros of
zeta(s).  The residue is the UNIVERSAL RESIDUE FACTOR:

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2)
                  * zeta'(rho))

This engine systematically computes A_c(rho_n) for:
  - n = 1, ..., 200 (first 200 nontrivial zeros)
  - c in {1/2, 1, 2, 4, 6, 12, 13, 24, 25, 26}
    spanning Heisenberg (c=1), affine KM (c=2,4,6), Virasoro self-dual
    (c=13), moonshine (c=24), critical (c=26), and edge cases (c=1/2,25).

CAUTION (AP1, AP48): kappa is family-specific.  kappa != c/2 in general.
  - kappa(Vir_c) = c/2
  - kappa(Heis_k) = k
  - kappa(KM_k(g)) = dim(g) * (k + h^v) / (2 * h^v)
  - kappa(W_N) = c * (H_N - 1)
The scattering factor F_c depends on c (central charge), NOT on kappa
directly.  But the shadow tower S_r depends on kappa and other data.
The cross-product A_c(rho) * S_r(A) bridges these two worlds.

VERIFICATION PATHS:
  Path 1: Direct mpmath computation from the closed-form formula
  Path 2: Numerical differentiation of F_c(s) near the pole s = (1+rho)/2
  Path 3: Contour integral (1/2pi i) oint F_c(s) ds around each pole
  Path 4: Complementarity check A_c / A_{26-c}

Manuscript references:
    eq:constrained-epstein-fe (arithmetic_shadows.tex, line 3303)
    def:universal-residue-factor (arithmetic_shadows.tex, line 3322)
    rem:koszul-epstein-constraints (arithmetic_shadows.tex, line 2864)
    [BenjaminChang22]: arXiv:2208.02259
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

try:
    import mpmath
    from mpmath import (
        mp, mpf, mpc, pi, zeta, gamma as mpgamma, log, exp,
        power, sqrt, re as mpre, im as mpim, conj as mpconj,
        diff, zetazero, inf, sin, cos, arg as mparg,
        fabs, quad, nstr, j as mpj,
    )
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ====================================================================
# Standard central charge values for the atlas
# ====================================================================

ATLAS_C_VALUES = [
    mpf('0.5'),   # Edge case: half-integer
    mpf('1'),     # Heisenberg (rank 1)
    mpf('2'),     # KM: sl_2 at k=1 has c = 3k/(k+2) = 1; or free bosons c=2
    mpf('4'),     # e.g. sl_2 at k=3: c = 9/5; or 4 free bosons
    mpf('6'),     # Intermediate
    mpf('12'),    # Half-moonshine
    mpf('13'),    # Virasoro self-dual (c + c' = 26, c = 13)
    mpf('24'),    # Moonshine module V^natural
    mpf('25'),    # Near-critical
    mpf('26'),    # Critical (ghost cancellation)
]

ATLAS_C_LABELS = {
    '0.5': 'edge_half',
    '1.0': 'heisenberg_rk1',
    '2.0': 'free_boson_2',
    '4.0': 'free_boson_4',
    '6.0': 'intermediate_6',
    '12.0': 'half_moonshine',
    '13.0': 'virasoro_self_dual',
    '24.0': 'moonshine',
    '25.0': 'near_critical',
    '26.0': 'critical',
}


def _ensure_mpmath():
    """Guard for mpmath availability."""
    if not HAS_MPMATH:
        raise RuntimeError("mpmath is required for bc_residue_atlas_engine")


# ====================================================================
# 1. Core residue computation: A_c(rho)
# ====================================================================

def universal_residue_factor(rho, c, dps=50):
    r"""Compute A_c(rho) via the closed-form residue formula.

    A_c(rho) = Gamma((1+rho)/2) * Gamma((c+rho-1)/2) * zeta(1+rho)
               / (2 * pi^{rho+1/2} * Gamma((c-rho-1)/2) * Gamma(rho/2)
                  * zeta'(rho))

    For large imaginary parts of rho, the Gamma functions can overflow.
    We therefore work in LOG SPACE using loggamma to maintain precision.

    Parameters
    ----------
    rho : complex or mpmath number
        A nontrivial zero of zeta(s).
    c : float or mpmath number
        Central charge.
    dps : int
        Decimal places of precision.

    Returns
    -------
    complex
        The value A_c(rho).
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        rho_m = mpc(rho)
        c_m = mpc(c)

        # Work in log space to avoid Gamma overflow for large Im(rho)
        log_num = (mpmath.loggamma((1 + rho_m) / 2)
                   + mpmath.loggamma((c_m + rho_m - 1) / 2))

        log_den = (log(mpc(2))
                   + (rho_m + mpf('0.5')) * log(pi)
                   + mpmath.loggamma((c_m - rho_m - 1) / 2)
                   + mpmath.loggamma(rho_m / 2))

        # The zeta factors must be computed directly (they don't overflow)
        zeta_1prho = zeta(1 + rho_m)
        zeta_prime_rho = diff(zeta, rho_m)

        if fabs(zeta_prime_rho) < power(10, -dps + 5):
            return complex(mpc(inf))

        log_ratio = log_num - log_den
        gamma_ratio = exp(log_ratio)

        result = gamma_ratio * zeta_1prho / zeta_prime_rho
        return complex(result)


def universal_residue_modulus_phase(rho, c, dps=50):
    r"""Compute |A_c(rho)| and arg(A_c(rho)).

    Returns
    -------
    dict with keys 'modulus', 'phase' (in radians), 'real', 'imag'.
    """
    _ensure_mpmath()
    A = universal_residue_factor(rho, c, dps)
    A_m = mpc(A)
    with mp.workdps(dps):
        return {
            'value': complex(A_m),
            'modulus': float(fabs(A_m)),
            'phase': float(mparg(A_m)),
            'real': float(mpre(A_m)),
            'imag': float(mpim(A_m)),
        }


# ====================================================================
# 2. Verification path 2: numerical differentiation of F_c(s) near pole
# ====================================================================

def scattering_factor_Fc(s, c, dps=50):
    r"""The scattering factor F_c(s) from the constrained Epstein FE.

    F_c(s) = Gamma(s) * Gamma(s + c/2 - 1) * zeta(2s)
             / (pi^{2s-1/2} * Gamma(c/2 - s) * Gamma(s - 1/2) * zeta(2s-1))
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        s_m = mpc(s)
        c_m = mpc(c)
        num = mpgamma(s_m) * mpgamma(s_m + c_m / 2 - 1) * zeta(2 * s_m)
        den = (power(pi, 2 * s_m - mpf('0.5'))
               * mpgamma(c_m / 2 - s_m)
               * mpgamma(s_m - mpf('0.5'))
               * zeta(2 * s_m - 1))
        if fabs(den) < power(10, -dps + 5):
            return complex(mpc(inf))
        return complex(num / den)


def residue_via_limit(rho, c, dps=50):
    r"""Verification path 2: compute the residue as
        lim_{s -> s_rho} (s - s_rho) * F_c(s)
    using numerical evaluation at several nearby points and Richardson
    extrapolation.

    The pole of F_c at s = s_rho = (1+rho)/2 arises from zeta(2s-1) = 0
    at 2s-1 = rho.  So (s - s_rho)*F_c(s) -> residue.
    """
    _ensure_mpmath()
    with mp.workdps(dps + 20):
        rho_m = mpc(rho)
        s_rho = (1 + rho_m) / 2

        # Evaluate (s - s_rho) * F_c(s) at progressively closer points
        # Use several step sizes for Richardson extrapolation
        epsilons = [power(10, -k) for k in range(8, 16)]
        estimates = []

        for eps_val in epsilons:
            # Approach from four directions and average
            vals = []
            for direction in [1, mpc(0, 1), -1, mpc(0, -1)]:
                s_test = s_rho + eps_val * direction
                try:
                    # F_c has a simple pole, so (s - s_rho)*F_c(s) -> residue
                    Fc_val = mpc(scattering_factor_Fc(s_test, c, dps + 20))
                    residue_est = (s_test - s_rho) * Fc_val
                    vals.append(residue_est)
                except (ZeroDivisionError, ValueError, OverflowError):
                    continue

            if vals:
                avg = sum(vals) / len(vals)
                estimates.append(complex(avg))

        if not estimates:
            return None

        # The best estimate is from the smallest epsilon
        best = estimates[-1]
        # Stability check: compare last two
        if len(estimates) >= 2:
            stability = abs(estimates[-1] - estimates[-2]) / max(abs(estimates[-1]), 1e-300)
        else:
            stability = float('inf')

        return {
            'residue': best,
            'estimates': estimates,
            'stability': stability,
        }


# ====================================================================
# 3. Verification path 3: contour integral
# ====================================================================

def residue_via_contour(rho, c, dps=50, radius=1e-6):
    r"""Verification path 3: compute the residue via contour integration.

        Res_{s=s_rho} F_c(s) = (1/2pi i) oint_{|s-s_rho|=r} F_c(s) ds

    We parametrise s = s_rho + r*exp(i*theta) and integrate over theta
    in [0, 2pi].
    """
    _ensure_mpmath()
    with mp.workdps(dps + 20):
        rho_m = mpc(rho)
        s_rho = (1 + rho_m) / 2
        r = mpf(radius)

        def integrand_real(theta):
            """Real part of F_c(s_rho + r*e^{i*theta}) * r*i*e^{i*theta}."""
            e_itheta = exp(mpc(0, 1) * theta)
            s_val = s_rho + r * e_itheta
            ds_dtheta = r * mpc(0, 1) * e_itheta
            Fc_val = mpc(scattering_factor_Fc(s_val, c, dps + 20))
            integrand_val = Fc_val * ds_dtheta
            return mpre(integrand_val)

        def integrand_imag(theta):
            """Imaginary part."""
            e_itheta = exp(mpc(0, 1) * theta)
            s_val = s_rho + r * e_itheta
            ds_dtheta = r * mpc(0, 1) * e_itheta
            Fc_val = mpc(scattering_factor_Fc(s_val, c, dps + 20))
            integrand_val = Fc_val * ds_dtheta
            return mpim(integrand_val)

        # Integrate using adaptive quadrature
        real_part = quad(integrand_real, [0, 2 * pi])
        imag_part = quad(integrand_imag, [0, 2 * pi])

        # Divide by 2*pi*i: result = (real_part + i*imag_part) / (2*pi*i)
        # = (real_part + i*imag_part) / (2*pi*i)
        # = (imag_part - i*real_part) * (-i)/(2*pi)  ... let's just compute
        # (1/(2*pi*i)) * (real + i*imag) = (imag + i*(-real)) / (2*pi)
        #                                = imag/(2*pi) - i*real/(2*pi)
        # Wait: 1/(2*pi*i) = -i/(2*pi), so:
        # (-i/(2*pi)) * (R + iI) = (-iR + I)/(2*pi) = I/(2*pi) - iR/(2*pi)
        two_pi = 2 * pi
        res_real = imag_part / two_pi
        res_imag = -real_part / two_pi

        return complex(mpc(res_real, res_imag))


# ====================================================================
# 4. Complementarity ratio A_c(rho) / A_{26-c}(rho)
# ====================================================================

def complementarity_ratio(rho, c, dps=50):
    r"""Compute A_c(rho) / A_{26-c}(rho).

    For Virasoro Koszul duality c -> 26-c, the c-INDEPENDENT factors
    (zeta(1+rho), zeta'(rho), pi^{rho+1/2}) cancel by inspection since
    they do not depend on c.  The surviving ratio is a product of Gamma
    functions because the c-dependent factors in A_c are all Gamma functions.
    This is a CONSISTENCY CHECK on the factored structure of A_c, not a
    deep structural theorem (AP7: scope honesty).

    The surviving terms are purely Gamma ratios:
        A_c / A_{26-c} = Gamma((c+rho-1)/2) * Gamma((26-c-rho-1)/2)
                         / (Gamma((c-rho-1)/2) * Gamma((26-c+rho-1)/2))
                       = Gamma((c+rho-1)/2) * Gamma((25-c-rho)/2)
                         / (Gamma((c-rho-1)/2) * Gamma((25-c+rho)/2))
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        rho_m = mpc(rho)
        c_m = mpc(c)
        c_dual = 26 - c_m

        A_c = mpc(universal_residue_factor(rho_m, c_m, dps))
        A_dual = mpc(universal_residue_factor(rho_m, c_dual, dps))

        if fabs(A_dual) < power(10, -dps + 5):
            return {
                'ratio': None,
                'A_c': complex(A_c),
                'A_dual': complex(A_dual),
                'c': float(mpre(c_m)),
                'c_dual': float(mpre(c_dual)),
            }

        ratio = A_c / A_dual
        return {
            'ratio': complex(ratio),
            'ratio_modulus': float(fabs(ratio)),
            'ratio_phase': float(mparg(ratio)),
            'A_c': complex(A_c),
            'A_dual': complex(A_dual),
            'c': float(mpre(c_m)),
            'c_dual': float(mpre(c_dual)),
        }


def complementarity_ratio_gamma_only(rho, c, dps=50):
    r"""The complementarity ratio expressed as a pure Gamma ratio.

    Since the zeta and pi factors cancel:
        A_c / A_{26-c} = Gamma((c+rho-1)/2) * Gamma((25-c-rho)/2)
                         / (Gamma((c-rho-1)/2) * Gamma((25-c+rho)/2))

    This is a verification that the ratio is PURELY Gamma-determined,
    with no arithmetic (zeta) content.
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        rho_m = mpc(rho)
        c_m = mpc(c)

        num = (mpgamma((c_m + rho_m - 1) / 2)
               * mpgamma((25 - c_m - rho_m) / 2))
        den = (mpgamma((c_m - rho_m - 1) / 2)
               * mpgamma((25 - c_m + rho_m) / 2))

        if fabs(den) < power(10, -dps + 5):
            return None

        return complex(num / den)


def self_dual_residue(rho, dps=50):
    r"""A_{13}(rho): the residue at the Virasoro self-dual point c=13.

    At c=13, the complementarity ratio is 1 (self-dual).
    The Gamma factors become:
        Gamma((1+rho)/2) * Gamma((12+rho)/2) * zeta(1+rho)
        / (2 * pi^{rho+1/2} * Gamma((12-rho)/2) * Gamma(rho/2) * zeta'(rho))
    """
    return universal_residue_factor(rho, 13, dps)


# ====================================================================
# 5. c-derivative: dA_c/dc at each zero
# ====================================================================

def residue_c_derivative(rho, c, dps=50, h=1e-8):
    r"""Compute dA_c/dc via central difference at fixed rho.

    Uses 4th-order central difference for accuracy:
        f'(x) approx (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h)) / (12h)
    """
    _ensure_mpmath()
    with mp.workdps(dps + 10):
        c_m = mpc(c)
        h_m = mpf(h)

        f_p2h = mpc(universal_residue_factor(rho, c_m + 2 * h_m, dps))
        f_ph = mpc(universal_residue_factor(rho, c_m + h_m, dps))
        f_mh = mpc(universal_residue_factor(rho, c_m - h_m, dps))
        f_m2h = mpc(universal_residue_factor(rho, c_m - 2 * h_m, dps))

        deriv = (-f_p2h + 8 * f_ph - 8 * f_mh + f_m2h) / (12 * h_m)
        return complex(deriv)


def residue_c_derivative_analytic(rho, c, dps=50):
    r"""Compute dA_c/dc analytically using the digamma function.

    d/dc A_c(rho) = A_c(rho) * (1/2) * [psi((c+rho-1)/2) - psi((c-rho-1)/2)]

    where psi = Gamma'/Gamma is the digamma function.
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        rho_m = mpc(rho)
        c_m = mpc(c)

        A = mpc(universal_residue_factor(rho_m, c_m, dps))

        psi_num = mpmath.digamma((c_m + rho_m - 1) / 2)
        psi_den = mpmath.digamma((c_m - rho_m - 1) / 2)

        deriv = A * (psi_num - psi_den) / 2
        return complex(deriv)


# ====================================================================
# 6. Factorisation analysis: |A_c(rho)| ~ f(gamma) * g(c) ?
# ====================================================================

def factorisation_test(n_zeros=20, c_values=None, dps=50):
    r"""Test whether |A_c(rho_n)| factorises as f(gamma_n) * g(c).

    If |A_c(rho_n)| = f(gamma_n) * g(c), then for any two zeros n, m:
        |A_c(rho_n)| / |A_c(rho_m)| = f(gamma_n) / f(gamma_m)
    is INDEPENDENT of c.

    We test this by computing the ratio for pairs of zeros and checking
    c-independence.

    Returns dict with ratio stability data.
    """
    _ensure_mpmath()
    if c_values is None:
        c_values = ATLAS_C_VALUES

    with mp.workdps(dps):
        # Compute moduli
        moduli = {}  # (n, c_idx) -> |A_c(rho_n)|
        zeros = []
        for n in range(1, n_zeros + 1):
            rho_n = zetazero(n)
            gamma_n = float(mpim(rho_n))
            zeros.append({'n': n, 'rho': complex(rho_n), 'gamma': gamma_n})

            for ci, c_val in enumerate(c_values):
                A = mpc(universal_residue_factor(rho_n, c_val, dps))
                moduli[(n, ci)] = float(fabs(A))

        # Test ratio independence: for fixed pair (n=1, n=2), compute
        # ratio across all c and check variation
        if n_zeros < 2:
            return {'zeros': zeros, 'moduli': moduli, 'factorised': None}

        ratios_by_c = []
        for ci in range(len(c_values)):
            m1 = moduli.get((1, ci), 0)
            m2 = moduli.get((2, ci), 0)
            if m2 > 1e-300:
                ratios_by_c.append(m1 / m2)

        if len(ratios_by_c) >= 2:
            mean_ratio = sum(ratios_by_c) / len(ratios_by_c)
            max_dev = max(abs(r - mean_ratio) / max(abs(mean_ratio), 1e-300)
                         for r in ratios_by_c)
            factorised = max_dev < 1e-6
        else:
            mean_ratio = None
            max_dev = None
            factorised = None

        return {
            'zeros': zeros,
            'moduli': moduli,
            'ratios_1_2': ratios_by_c,
            'mean_ratio': mean_ratio,
            'max_deviation': max_dev,
            'factorised': factorised,
        }


# ====================================================================
# 7. Shadow residue cross-product: A_c(rho) * S_r(A)
# ====================================================================

def _virasoro_shadow_coefficients(c_val, max_arity=8):
    r"""Compute Virasoro shadow tower S_r for r = 2, ..., max_arity.

    Uses the shadow metric Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22).
    The square root expansion gives S_r = a_{r-2} / r.

    Implemented directly here to avoid external dependencies that
    may require sympy (we work in mpmath for precision).
    """
    _ensure_mpmath()
    with mp.workdps(50):
        c_m = mpf(c_val)
        kappa = c_m / 2
        alpha = mpf(2)
        S4 = mpf(10) / (c_m * (5 * c_m + 22))

        q0 = 4 * kappa ** 2
        q1 = 12 * kappa * alpha
        q2 = 9 * alpha ** 2 + 16 * kappa * S4

        a0 = 2 * kappa
        max_n = max_arity - 2 + 1
        a = [mpf(0)] * (max_n + 1)
        a[0] = a0
        if max_n >= 1:
            a[1] = q1 / (2 * a0)
        if max_n >= 2:
            a[2] = (q2 - a[1] ** 2) / (2 * a0)
        for n in range(3, max_n + 1):
            conv = sum(a[jj] * a[n - jj] for jj in range(1, n))
            a[n] = -conv / (2 * a0)

        coeffs = {}
        for r in range(2, max_arity + 1):
            idx = r - 2
            if idx <= max_n:
                coeffs[r] = float(a[idx] / r)
        return coeffs


def _heisenberg_shadow_coefficients(k_level, max_arity=8):
    r"""Heisenberg shadow tower: S_2 = kappa = k, S_r = 0 for r >= 3.

    Heisenberg is Gaussian (class G, r_max = 2): the shadow tower
    terminates at arity 2.
    """
    coeffs = {2: float(k_level)}
    for r in range(3, max_arity + 1):
        coeffs[r] = 0.0
    return coeffs


def _shadow_coefficients_for_family(c_val, family='virasoro', max_arity=8):
    r"""Return shadow tower S_r for a given family and central charge.

    Supported families:
      'virasoro' (class M, infinite tower)
      'heisenberg' (class G, terminates at arity 2)
    """
    if family == 'virasoro':
        return _virasoro_shadow_coefficients(c_val, max_arity)
    elif family == 'heisenberg':
        return _heisenberg_shadow_coefficients(c_val, max_arity)
    else:
        raise ValueError(f"Unknown family: {family}")


def shadow_residue_cross_product(rho, c, family='virasoro',
                                 max_arity=8, dps=50):
    r"""Compute the shadow-residue cross product A_c(rho) * S_r(A).

    This pairs the zeta-zero residue data with the shadow obstruction
    tower, connecting the Eisenstein scattering to the bar complex.

    Returns dict {r: A_c(rho) * S_r} for r = 2, ..., max_arity.
    """
    _ensure_mpmath()
    A = universal_residue_factor(rho, c, dps)
    S = _shadow_coefficients_for_family(float(c) if not isinstance(c, float) else c,
                                        family, max_arity)

    cross = {}
    for r, s_val in S.items():
        cross[r] = A * s_val
    return cross


# ====================================================================
# 8. Full atlas computation
# ====================================================================

def compute_residue_at_zero(n, c, dps=50):
    r"""Compute A_c(rho_n) for the n-th nontrivial zeta zero.

    Returns dict with modulus, phase, real, imag parts.
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        rho = zetazero(n)
        gamma_val = float(mpim(rho))
        A = universal_residue_factor(rho, c, dps)
        A_m = mpc(A)

        return {
            'n': n,
            'gamma': gamma_val,
            'rho': complex(rho),
            'c': float(c) if isinstance(c, (int, float)) else float(mpre(mpc(c))),
            'A_c': complex(A_m),
            'modulus': float(fabs(A_m)),
            'phase': float(mparg(A_m)),
            'real': float(mpre(A_m)),
            'imag': float(mpim(A_m)),
        }


def compute_atlas_slice(c, n_max=200, dps=50):
    r"""Compute A_c(rho_n) for n=1,...,n_max at a fixed central charge c.

    Returns list of dicts, one per zero.
    """
    _ensure_mpmath()
    results = []
    with mp.workdps(dps):
        for n in range(1, n_max + 1):
            results.append(compute_residue_at_zero(n, c, dps))
    return results


def compute_full_atlas(n_max=200, c_values=None, dps=50):
    r"""Compute the full atlas: A_c(rho_n) for all (n, c) pairs.

    Returns dict keyed by float(c), each value a list of residue dicts.
    """
    _ensure_mpmath()
    if c_values is None:
        c_values = ATLAS_C_VALUES

    atlas = {}
    for c_val in c_values:
        c_key = float(c_val)
        atlas[c_key] = compute_atlas_slice(c_val, n_max, dps)
    return atlas


def compute_complementarity_atlas(n_max=200, c_values=None, dps=50):
    r"""Compute the complementarity ratio A_c/A_{26-c} for all (n, c) pairs.

    For c = 13, the ratio should be 1 (self-dual).

    Returns dict keyed by float(c), each value a list of ratio dicts.
    """
    _ensure_mpmath()
    if c_values is None:
        c_values = ATLAS_C_VALUES

    atlas = {}
    with mp.workdps(dps):
        for c_val in c_values:
            c_key = float(c_val)
            c_dual = 26 - c_val
            if c_dual <= 0:
                atlas[c_key] = None
                continue

            slice_data = []
            for n in range(1, n_max + 1):
                rho = zetazero(n)
                ratio_data = complementarity_ratio(rho, c_val, dps)
                ratio_data['n'] = n
                ratio_data['gamma'] = float(mpim(rho))
                slice_data.append(ratio_data)

            atlas[c_key] = slice_data

    return atlas


# ====================================================================
# 9. Growth analysis: how |A_c(rho_n)| behaves as gamma_n -> inf
# ====================================================================

def modulus_growth_analysis(c, n_zeros=100, dps=50):
    r"""Analyse the growth of |A_c(rho_n)| as n -> inf (gamma_n -> inf).

    The Stirling approximation for large gamma gives:
        |Gamma((c+rho-1)/2)| ~ |gamma/2|^{(c-2)/2} * exp(-pi*gamma/4) * sqrt(2*pi)
    so the dominant behaviour is exponential decay in gamma.

    Returns growth rate estimates.
    """
    _ensure_mpmath()
    data = []
    with mp.workdps(dps):
        for n in range(1, n_zeros + 1):
            rho = zetazero(n)
            gamma_n = float(mpim(rho))
            A = mpc(universal_residue_factor(rho, c, dps))
            mod = float(fabs(A))
            data.append({
                'n': n,
                'gamma': gamma_n,
                'modulus': mod,
                'log_modulus': float(log(mpf(mod))) if mod > 0 else float('-inf'),
            })

    # Fit log|A| ~ a*gamma + b (exponential decay rate)
    if len(data) >= 10:
        gammas = [d['gamma'] for d in data
                  if d['modulus'] > 0 and math.isfinite(d['log_modulus'])]
        log_mods = [d['log_modulus'] for d in data
                    if d['modulus'] > 0 and math.isfinite(d['log_modulus'])]
        if len(gammas) >= 2:
            n_fit = len(gammas)
            sum_g = sum(gammas)
            sum_l = sum(log_mods)
            sum_gl = sum(g * l for g, l in zip(gammas, log_mods))
            sum_g2 = sum(g * g for g in gammas)
            denom = n_fit * sum_g2 - sum_g ** 2
            if abs(denom) > 1e-30:
                slope = (n_fit * sum_gl - sum_g * sum_l) / denom
                intercept = (sum_l - slope * sum_g) / n_fit
            else:
                slope = intercept = None
        else:
            slope = intercept = None
    else:
        slope = intercept = None

    return {
        'data': data,
        'decay_rate': slope,        # should be ~ -pi/4 * [some c-dependent factor]
        'intercept': intercept,
        'c': float(c) if isinstance(c, (int, float)) else float(mpre(mpc(c))),
    }


# ====================================================================
# 10. Complementarity ratio Gamma-only verification
# ====================================================================

def verify_complementarity_gamma_cancellation(rho, c, dps=50):
    r"""Verify that A_c/A_{26-c} equals the pure Gamma ratio.

    This confirms that all zeta and pi factors cancel in the ratio.

    Returns relative error between the two computations.
    """
    _ensure_mpmath()
    with mp.workdps(dps):
        # Path A: ratio of full residues
        ratio_full = complementarity_ratio(rho, c, dps)
        R_full = ratio_full.get('ratio')

        # Path B: pure Gamma formula
        R_gamma = complementarity_ratio_gamma_only(rho, c, dps)

        if R_full is None or R_gamma is None:
            return {
                'ratio_full': R_full,
                'ratio_gamma': R_gamma,
                'relative_error': None,
                'match': None,
            }

        rel_err = abs(R_full - R_gamma) / max(abs(R_full), 1e-300)
        return {
            'ratio_full': R_full,
            'ratio_gamma': R_gamma,
            'relative_error': rel_err,
            'match': rel_err < 1e-12,
        }


# ====================================================================
# 11. Phase structure analysis
# ====================================================================

def phase_structure(c, n_zeros=50, dps=50):
    r"""Analyse the phase arg(A_c(rho_n)) as a function of gamma_n.

    For rho on the critical line (rho = 1/2 + i*gamma), the phase
    encodes the oscillatory content of the residue kernel.

    Returns phase data and detects any linear trend in gamma.
    """
    _ensure_mpmath()
    data = []
    with mp.workdps(dps):
        for n in range(1, n_zeros + 1):
            rho = zetazero(n)
            gamma_n = float(mpim(rho))
            A = mpc(universal_residue_factor(rho, c, dps))
            phase_val = float(mparg(A))
            data.append({
                'n': n,
                'gamma': gamma_n,
                'phase': phase_val,
            })

    # Detect linear trend: phase ~ a*gamma + b (mod 2*pi)
    # We unwrap phases first
    if len(data) >= 2:
        phases = [d['phase'] for d in data]
        gammas = [d['gamma'] for d in data]
        # Simple unwrap
        unwrapped = [phases[0]]
        for k in range(1, len(phases)):
            dp = phases[k] - phases[k - 1]
            if dp > math.pi:
                dp -= 2 * math.pi
            elif dp < -math.pi:
                dp += 2 * math.pi
            unwrapped.append(unwrapped[-1] + dp)

        # Linear regression on unwrapped phases
        n_fit = len(gammas)
        sg = sum(gammas)
        sp = sum(unwrapped)
        sgp = sum(g * p for g, p in zip(gammas, unwrapped))
        sg2 = sum(g * g for g in gammas)
        denom_fit = n_fit * sg2 - sg ** 2
        if abs(denom_fit) > 1e-30:
            phase_slope = (n_fit * sgp - sg * sp) / denom_fit
            phase_intercept = (sp - phase_slope * sg) / n_fit
        else:
            phase_slope = phase_intercept = None
    else:
        phase_slope = phase_intercept = None
        unwrapped = []

    return {
        'data': data,
        'unwrapped_phases': unwrapped,
        'phase_slope': phase_slope,
        'phase_intercept': phase_intercept,
        'c': float(c) if isinstance(c, (int, float)) else float(mpre(mpc(c))),
    }


# ====================================================================
# 12. Batch verification across paths
# ====================================================================

def verify_residue_three_paths(rho, c, dps=50):
    r"""Cross-verify A_c(rho) via three independent paths.

    Path 1: Closed-form formula
    Path 2: Numerical limit (s - s_rho) * F_c(s)
    Path 4: Complementarity Gamma-only (as internal consistency)

    Path 3 (contour integral) is expensive; use verify_residue_contour
    separately.

    Returns dict with values from each path and relative errors.
    """
    _ensure_mpmath()

    # Path 1: direct formula
    A_direct = universal_residue_factor(rho, c, dps)

    # Path 2: limit approach
    limit_data = residue_via_limit(rho, c, dps)
    A_limit = limit_data['residue'] if limit_data else None

    # Path 4: internal consistency via analytic derivative
    dA_numeric = residue_c_derivative(rho, c, dps)
    dA_analytic = residue_c_derivative_analytic(rho, c, dps)

    result = {
        'A_direct': A_direct,
        'A_limit': A_limit,
        'dA_numeric': dA_numeric,
        'dA_analytic': dA_analytic,
    }

    if A_limit is not None:
        err_12 = abs(A_direct - A_limit) / max(abs(A_direct), 1e-300)
        result['error_direct_vs_limit'] = err_12
    else:
        result['error_direct_vs_limit'] = None

    if dA_numeric is not None and dA_analytic is not None:
        err_deriv = abs(dA_numeric - dA_analytic) / max(abs(dA_analytic), 1e-300)
        result['error_deriv_numeric_vs_analytic'] = err_deriv
    else:
        result['error_deriv_numeric_vs_analytic'] = None

    return result


# ====================================================================
# 13. Summary statistics for the atlas
# ====================================================================

def atlas_summary_statistics(atlas_slice):
    r"""Compute summary statistics for an atlas slice (fixed c, all zeros).

    Parameters
    ----------
    atlas_slice : list of dicts from compute_atlas_slice

    Returns
    -------
    dict with max_modulus, min_modulus, mean_modulus, decay rate estimate.
    """
    moduli = [d['modulus'] for d in atlas_slice if d['modulus'] > 0]
    if not moduli:
        return {'count': 0}

    return {
        'count': len(moduli),
        'max_modulus': max(moduli),
        'min_modulus': min(moduli),
        'mean_modulus': sum(moduli) / len(moduli),
        'first_modulus': moduli[0] if moduli else None,
        'last_modulus': moduli[-1] if moduli else None,
        'decay_factor': moduli[-1] / moduli[0] if moduli[0] > 0 else None,
    }
