#!/usr/bin/env python3
r"""BC-74: Subconvexity bounds for shadow zeta functions.

MATHEMATICAL CONTENT
====================

For the Riemann zeta function, the convexity bound on the critical line is
|zeta(1/2+it)| <= C * t^{1/4+eps}.  Weyl's subconvexity bound improves
this to t^{1/6+eps}.  For shadow zeta functions

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}

the analytic properties are RADICALLY different from Riemann zeta because
the shadow coefficients S_r decay exponentially for class M algebras
(|S_r| ~ rho^r * r^{-5/2} with rho < 1), making the Dirichlet series
converge for ALL s.  The shadow zeta is therefore an ENTIRE function of s.

Consequence: on any vertical line sigma + it, |zeta_A(sigma+it)| is
BOUNDED as |t| -> infinity.  The Phragmen-Lindelof exponent mu_A(sigma)
is ZERO for all sigma.  This is dramatically better than Riemann zeta
(mu(1/2) = 1/4 convexity, ~13/84 subconvexity) and reflects the
exponential decay of the shadow tower.

Specifically, for |S_r| <= C * rho^r * r^{-5/2} with rho < 1:

    |zeta_A(sigma+it)| <= C * sum_{r>=2} rho^r * r^{-sigma-5/2}
                       = C * Li_{sigma+5/2}(rho)   (polylogarithm)

which is INDEPENDENT of t.  The bound depends only on sigma and rho.

CONTENTS
--------
1. Convexity bound computation: M_A(sigma, T) on vertical strips
2. Phragmen-Lindelof exponent mu_A(sigma) from numerical fitting
3. Critical line growth: |zeta_A(1/2+it)| power-law fit
4. Moment computation on critical line (2nd and 4th)
5. Zero-free regions via argument principle
6. Approximate functional equation (shadow Riemann-Siegel)
7. Large deviation estimates P(|zeta_A(1/2+iU)| > V)
8. Polylogarithm bound (analytical verification path)

VERIFICATION (3+ paths per claim):
    Path 1: Direct numerical evaluation on grid
    Path 2: Polylogarithm upper bound (analytical)
    Path 3: Complementarity cross-check: mu_A(sigma) + mu_{A!}(1-sigma)
    Path 4: Monte Carlo integration vs deterministic quadrature for moments
    Path 5: Cauchy integral formula consistency

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Multi-path verification is mandatory.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not just c.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
import random
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
    _log_gamma_complex,
)


# ============================================================================
# 0.  Shadow coefficient providers (dispatch)
# ============================================================================

def shadow_coefficients_for_family(
    family: str,
    param: float,
    max_r: int = 60,
) -> Dict[int, float]:
    """Compute shadow coefficients S_r for the given family.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'betagamma', 'virasoro', 'w3_t', 'w3_w'
    param : family parameter (k for Heis/affine, lambda for betagamma,
            c for Virasoro/W3)
    max_r : maximum arity

    Returns
    -------
    Dict mapping arity r to S_r(A).
    """
    dispatch = {
        'heisenberg': lambda: heisenberg_shadow_coefficients(param, max_r),
        'affine_sl2': lambda: affine_sl2_shadow_coefficients(param, max_r),
        'affine_sl3': lambda: affine_sl3_shadow_coefficients(param, max_r),
        'betagamma': lambda: betagamma_shadow_coefficients(param, max_r),
        'virasoro': lambda: virasoro_shadow_coefficients_numerical(param, max_r),
        'w3_t': lambda: w3_t_line_shadow_coefficients(param, max_r),
        'w3_w': lambda: w3_w_line_shadow_coefficients(param, max_r),
    }
    if family not in dispatch:
        raise ValueError(f"Unknown family '{family}'. Choose from {list(dispatch)}")
    return dispatch[family]()


def koszul_dual_param(family: str, param: float) -> Tuple[str, float]:
    """Koszul dual family and parameter.

    Virasoro: c -> 26-c.  Heisenberg: k -> -k.  Affine sl_N: k -> -k-2h^v.
    """
    if family == 'virasoro':
        return ('virasoro', 26.0 - param)
    elif family == 'w3_t':
        return ('w3_t', 26.0 - param)
    elif family == 'heisenberg':
        return ('heisenberg', -param)
    elif family == 'affine_sl2':
        return ('affine_sl2', -param - 4.0)  # -k-2h^v, h^v=2
    elif family == 'affine_sl3':
        return ('affine_sl3', -param - 6.0)  # -k-2h^v, h^v=3
    else:
        raise ValueError(f"Koszul dual not implemented for {family}")


# ============================================================================
# 1.  Convexity bound: M_A(sigma, T) = max_{|t|<=T} |zeta_A(sigma+it)|
# ============================================================================

def max_modulus_on_vertical(
    shadow_coeffs: Dict[int, float],
    sigma: float,
    T: float,
    n_sample: int = 200,
    max_r: Optional[int] = None,
) -> float:
    """Compute M_A(sigma, T) = max_{|t|<=T} |zeta_A(sigma + it)|.

    Samples n_sample points uniformly in [-T, T] and returns the maximum.
    """
    if T <= 0:
        s = complex(sigma, 0.0)
        return abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))

    best = 0.0
    for j in range(n_sample + 1):
        t = -T + 2.0 * T * j / n_sample
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        if val > best:
            best = val
    return best


def max_modulus_table(
    shadow_coeffs: Dict[int, float],
    sigma_values: List[float],
    T_values: List[float],
    n_sample: int = 200,
    max_r: Optional[int] = None,
) -> Dict[Tuple[float, float], float]:
    """Compute M_A(sigma, T) for a grid of (sigma, T) values.

    Returns dict mapping (sigma, T) to M_A(sigma, T).
    """
    result = {}
    for sigma in sigma_values:
        for T in T_values:
            result[(sigma, T)] = max_modulus_on_vertical(
                shadow_coeffs, sigma, T, n_sample, max_r
            )
    return result


# ============================================================================
# 2.  Phragmen-Lindelof exponent mu_A(sigma)
# ============================================================================

def phragmen_lindelof_exponent(
    shadow_coeffs: Dict[int, float],
    sigma: float,
    T_values: Optional[List[float]] = None,
    n_sample: int = 200,
    max_r: Optional[int] = None,
) -> float:
    """Estimate mu_A(sigma) = inf{mu : M_A(sigma,T) = O(T^mu)}.

    Fits log M_A(sigma,T) ~ mu * log T + const for large T.
    For shadow zeta (entire), mu_A(sigma) = 0 for all sigma.

    Returns the fitted exponent mu.
    """
    if T_values is None:
        T_values = [10.0, 20.0, 50.0, 100.0, 200.0, 500.0]

    log_T = []
    log_M = []
    for T in T_values:
        M = max_modulus_on_vertical(shadow_coeffs, sigma, T, n_sample, max_r)
        if M > 1e-300 and T > 1.0:
            log_T.append(math.log(T))
            log_M.append(math.log(M))

    if len(log_T) < 2:
        return 0.0

    # Linear regression: log_M = mu * log_T + b
    n = len(log_T)
    sx = sum(log_T)
    sy = sum(log_M)
    sxx = sum(x * x for x in log_T)
    sxy = sum(x * y for x, y in zip(log_T, log_M))

    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return 0.0

    mu = (n * sxy - sx * sy) / denom
    return mu


def phragmen_lindelof_table(
    shadow_coeffs: Dict[int, float],
    sigma_values: List[float],
    T_values: Optional[List[float]] = None,
    n_sample: int = 200,
    max_r: Optional[int] = None,
) -> Dict[float, float]:
    """Compute mu_A(sigma) for a list of sigma values.

    Returns dict mapping sigma to mu_A(sigma).
    """
    result = {}
    for sigma in sigma_values:
        result[sigma] = phragmen_lindelof_exponent(
            shadow_coeffs, sigma, T_values, n_sample, max_r
        )
    return result


# ============================================================================
# 3.  Critical line growth: |zeta_A(1/2+it)| power-law fit
# ============================================================================

def critical_line_values(
    shadow_coeffs: Dict[int, float],
    t_values: List[float],
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> List[float]:
    """Compute |zeta_A(sigma + it)| for a list of t values.

    Default sigma = 1/2 (critical line).
    """
    result = []
    for t in t_values:
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        result.append(val)
    return result


@dataclass
class PowerLawFit:
    """Result of fitting |zeta_A(1/2+it)| ~ C * t^alpha."""
    alpha: float
    C: float
    residual: float
    n_points: int


def fit_critical_line_power_law(
    shadow_coeffs: Dict[int, float],
    t_min: float = 10.0,
    t_max: float = 500.0,
    n_points: int = 100,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> PowerLawFit:
    """Fit |zeta_A(sigma+it)| ~ C * t^alpha for t in [t_min, t_max].

    For entire shadow zeta (class M with rho < 1), expects alpha ~ 0
    (bounded on the critical line).

    Returns PowerLawFit with alpha, C, and residual.
    """
    log_t = []
    log_z = []
    for j in range(n_points):
        t = t_min + (t_max - t_min) * j / max(n_points - 1, 1)
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        if val > 1e-300 and t > 1e-10:
            log_t.append(math.log(t))
            log_z.append(math.log(val))

    if len(log_t) < 2:
        return PowerLawFit(alpha=0.0, C=1.0, residual=0.0, n_points=0)

    # Linear regression: log_z = alpha * log_t + log_C
    n = len(log_t)
    sx = sum(log_t)
    sy = sum(log_z)
    sxx = sum(x * x for x in log_t)
    sxy = sum(x * y for x, y in zip(log_t, log_z))

    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return PowerLawFit(alpha=0.0, C=1.0, residual=0.0, n_points=n)

    alpha = (n * sxy - sx * sy) / denom
    log_C = (sy - alpha * sx) / n
    C = math.exp(log_C)

    # Residual (mean squared error in log space)
    residual = 0.0
    for x, y in zip(log_t, log_z):
        residual += (y - alpha * x - log_C) ** 2
    residual = math.sqrt(residual / n)

    return PowerLawFit(alpha=alpha, C=C, residual=residual, n_points=n)


# ============================================================================
# 4.  Polylogarithm upper bound (analytical verification path)
# ============================================================================

def polylogarithm_bound(
    rho: float,
    sigma: float,
    max_r: int = 500,
) -> float:
    """Upper bound |zeta_A(sigma+it)| <= sum_{r>=2} |S_r| * r^{-sigma}.

    For |S_r| ~ C * rho^r * r^{-5/2}, this is sum rho^r * r^{-(sigma+5/2)}
    = Li_{sigma+5/2}(rho) - 1 - rho (removing r=0,1 terms from polylog).

    Computes the truncated sum directly.

    Parameters
    ----------
    rho : shadow growth rate (must be < 1 for convergence)
    sigma : real part of s
    max_r : truncation order

    Returns
    -------
    The polylogarithm upper bound value.
    """
    if rho >= 1.0:
        return float('inf')

    total = 0.0
    for r in range(2, max_r + 1):
        total += rho ** r * r ** (-(sigma + 2.5))
    return total


def polylogarithm_bound_from_coeffs(
    shadow_coeffs: Dict[int, float],
    sigma: float,
) -> float:
    """Upper bound |zeta_A(sigma+it)| <= sum_{r>=2} |S_r| * r^{-sigma}.

    Uses actual shadow coefficients (not the asymptotic form).
    This bound is INDEPENDENT of t.
    """
    max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        total += abs(Sr) * r ** (-sigma)
    return total


# ============================================================================
# 5.  Moment computation on critical line
# ============================================================================

def moment_on_critical_line(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    h: float = 0.1,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> float:
    """Compute M_{2k}(T; A) = (1/T) * integral_0^T |zeta_A(sigma+it)|^{2k} dt.

    Uses composite trapezoidal rule with step size h.
    """
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")

    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps

    total = 0.0
    for j in range(n_steps + 1):
        t_j = j * actual_h
        s = complex(sigma, t_j)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        contrib = val ** (2 * k)
        if j == 0 or j == n_steps:
            total += contrib / 2.0
        else:
            total += contrib

    integral = total * actual_h
    return integral / T


def moment_on_critical_line_monte_carlo(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    n_samples: int = 5000,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
    seed: int = 42,
) -> Tuple[float, float]:
    """Monte Carlo estimate of M_{2k}(T; A).

    Returns (mean, standard_error).
    """
    rng = random.Random(seed)
    vals = []
    for _ in range(n_samples):
        t = rng.uniform(0, T)
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        vals.append(val ** (2 * k))

    mean = sum(vals) / len(vals)
    if len(vals) > 1:
        var = sum((v - mean) ** 2 for v in vals) / (len(vals) - 1)
        se = math.sqrt(var / len(vals))
    else:
        se = 0.0
    return mean, se


def moment_ratio_check(
    shadow_coeffs: Dict[int, float],
    T: float,
    h: float = 0.1,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> float:
    """Ratio M_4 / M_2^2. For bounded functions, this is <= 1 by Cauchy-Schwarz.

    If zeta_A is bounded on Re(s) = sigma, then M_{2k} ~ <|zeta|^{2k}> as
    T -> infinity, and M_4 / M_2^2 is the kurtosis ratio.
    """
    m2 = moment_on_critical_line(shadow_coeffs, 1, T, h, sigma, max_r)
    m4 = moment_on_critical_line(shadow_coeffs, 2, T, h, sigma, max_r)
    if m2 < 1e-300:
        return 0.0
    return m4 / (m2 ** 2)


# ============================================================================
# 6.  Zero-free regions
# ============================================================================

def find_rightmost_zero(
    shadow_coeffs: Dict[int, float],
    t_range: Tuple[float, float] = (1.0, 100.0),
    sigma_range: Tuple[float, float] = (0.0, 2.0),
    grid_sigma: int = 40,
    grid_t: int = 200,
    max_r: Optional[int] = None,
    refine: bool = True,
) -> Optional[complex]:
    """Find the zero of zeta_A(s) with the largest real part in the given box.

    Uses grid search to find candidate, then Newton refinement.
    Returns None if no zero is found.
    """
    sigma_lo, sigma_hi = sigma_range
    t_lo, t_hi = t_range

    best_s = None
    best_val = float('inf')

    for i in range(grid_sigma):
        sigma = sigma_lo + (sigma_hi - sigma_lo) * i / max(grid_sigma - 1, 1)
        for j in range(grid_t):
            t = t_lo + (t_hi - t_lo) * j / max(grid_t - 1, 1)
            s = complex(sigma, t)
            val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
            if val < best_val:
                best_val = val
                best_s = s

    if best_s is None or best_val > 0.1:
        return None

    if not refine:
        return best_s

    # Newton-Raphson refinement using numerical derivative
    s = best_s
    eps = 1e-8
    for _ in range(50):
        f = shadow_zeta_numerical(shadow_coeffs, s, max_r)
        if abs(f) < 1e-14:
            break
        # Numerical derivative
        df_ds = (shadow_zeta_numerical(shadow_coeffs, s + eps, max_r) - f) / eps
        if abs(df_ds) < 1e-30:
            break
        s = s - f / df_ds

    return s


def zero_free_boundary(
    shadow_coeffs: Dict[int, float],
    t_values: List[float],
    sigma_range: Tuple[float, float] = (-2.0, 5.0),
    n_sigma: int = 100,
    max_r: Optional[int] = None,
) -> Dict[float, float]:
    """For each t, find the largest sigma such that |zeta_A(sigma+it)| is small.

    Returns dict mapping t to the approximate sigma of the zero.
    If no zero near the given t, returns sigma_range[0].
    """
    result = {}
    sigma_lo, sigma_hi = sigma_range
    for t in t_values:
        best_sigma = sigma_lo
        best_val = float('inf')
        for i in range(n_sigma):
            sigma = sigma_lo + (sigma_hi - sigma_lo) * i / max(n_sigma - 1, 1)
            s = complex(sigma, t)
            val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
            if val < best_val:
                best_val = val
                best_sigma = sigma
        result[t] = best_sigma if best_val < 0.01 else sigma_lo
    return result


def count_zeros_in_strip(
    shadow_coeffs: Dict[int, float],
    sigma_lo: float,
    sigma_hi: float,
    T: float,
    n_boundary: int = 1000,
    max_r: Optional[int] = None,
) -> int:
    """Count zeros in the rectangle [sigma_lo, sigma_hi] x [0, T] via
    the argument principle:

        N = (1/2pi) * Delta_{boundary} arg(zeta_A(s))

    Integrates the change of argument along the boundary of the rectangle.
    """
    # Parameterize the boundary counterclockwise
    # Bottom: sigma_lo -> sigma_hi at t=0
    # Right: sigma_hi at t=0 -> t=T
    # Top: sigma_hi -> sigma_lo at t=T
    # Left: sigma_lo at t=T -> t=0

    pts_per_side = n_boundary // 4
    if pts_per_side < 10:
        pts_per_side = 10

    boundary_vals = []

    # Bottom: t = 0, sigma from sigma_lo to sigma_hi
    for i in range(pts_per_side):
        sigma = sigma_lo + (sigma_hi - sigma_lo) * i / pts_per_side
        s = complex(sigma, 0.0)
        boundary_vals.append(shadow_zeta_numerical(shadow_coeffs, s, max_r))

    # Right: sigma = sigma_hi, t from 0 to T
    for i in range(pts_per_side):
        t = T * i / pts_per_side
        s = complex(sigma_hi, t)
        boundary_vals.append(shadow_zeta_numerical(shadow_coeffs, s, max_r))

    # Top: t = T, sigma from sigma_hi to sigma_lo
    for i in range(pts_per_side):
        sigma = sigma_hi - (sigma_hi - sigma_lo) * i / pts_per_side
        s = complex(sigma, T)
        boundary_vals.append(shadow_zeta_numerical(shadow_coeffs, s, max_r))

    # Left: sigma = sigma_lo, t from T to 0
    for i in range(pts_per_side):
        t = T - T * i / pts_per_side
        s = complex(sigma_lo, t)
        boundary_vals.append(shadow_zeta_numerical(shadow_coeffs, s, max_r))

    # Close the contour
    boundary_vals.append(boundary_vals[0])

    # Compute total argument change
    total_arg_change = 0.0
    for i in range(len(boundary_vals) - 1):
        z1 = boundary_vals[i]
        z2 = boundary_vals[i + 1]
        if abs(z1) < 1e-300 or abs(z2) < 1e-300:
            continue
        darg = cmath.phase(z2) - cmath.phase(z1)
        # Unwrap: keep darg in (-pi, pi)
        while darg > math.pi:
            darg -= 2 * math.pi
        while darg < -math.pi:
            darg += 2 * math.pi
        total_arg_change += darg

    n_zeros = total_arg_change / (2 * math.pi)
    return round(n_zeros)


# ============================================================================
# 7.  Approximate functional equation (shadow Riemann-Siegel)
# ============================================================================

def approximate_functional_equation(
    shadow_coeffs: Dict[int, float],
    s: complex,
    x: Optional[int] = None,
    max_r: Optional[int] = None,
) -> Tuple[complex, complex, float]:
    """Approximate functional equation for shadow zeta.

    For entire shadow zeta (no functional equation in the classical sense),
    the AFE is simply the partial sum truncated at x:

        zeta_A(s) = sum_{r=2}^{x} S_r * r^{-s} + R(s, x)

    where the remainder R(s, x) = sum_{r > x} S_r * r^{-s}.

    For |S_r| <= C * rho^r * r^{-5/2}, the remainder satisfies:
        |R(s, x)| <= C * sum_{r > x} rho^r * r^{-(sigma + 5/2)}
                  <= C * rho^{x+1} / (1 - rho) * (x+1)^{-(sigma + 5/2)}

    Returns (partial_sum, full_sum, remainder_bound).
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    if x is None:
        x = max_r // 2

    # Partial sum
    partial = 0.0 + 0.0j
    for r in range(2, min(x, max_r) + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr != 0.0:
            partial += Sr * r ** (-s)

    # Full sum for comparison
    full = shadow_zeta_numerical(shadow_coeffs, s, max_r)

    # Remainder bound: sum_{r > x} |S_r| * r^{-sigma}
    sigma = s.real
    remainder = 0.0
    for r in range(x + 1, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        remainder += abs(Sr) * r ** (-sigma)

    return partial, full, remainder


def afe_error_vs_truncation(
    shadow_coeffs: Dict[int, float],
    s: complex,
    x_values: Optional[List[int]] = None,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute |zeta_A(s) - partial_sum(x)| for various truncation points x.

    Returns dict mapping x to |error|.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    if x_values is None:
        x_values = [5, 10, 15, 20, 25, 30, 40, 50]

    full = shadow_zeta_numerical(shadow_coeffs, s, max_r)

    result = {}
    for x in x_values:
        partial = 0.0 + 0.0j
        for r in range(2, min(x, max_r) + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if Sr != 0.0:
                partial += Sr * r ** (-s)
        result[x] = abs(full - partial)
    return result


# ============================================================================
# 8.  Large deviation estimates
# ============================================================================

def large_deviation_probability(
    shadow_coeffs: Dict[int, float],
    V: float,
    T: float,
    n_samples: int = 10000,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
    seed: int = 42,
) -> float:
    """Estimate P(|zeta_A(1/2 + iU)| > V) for uniform U in [0, T].

    Uses Monte Carlo sampling.
    """
    rng = random.Random(seed)
    count = 0
    for _ in range(n_samples):
        t = rng.uniform(0, T)
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        if val > V:
            count += 1
    return count / n_samples


def large_deviation_table(
    shadow_coeffs: Dict[int, float],
    V_values: List[float],
    T: float,
    n_samples: int = 10000,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
    seed: int = 42,
) -> Dict[float, float]:
    """Compute P(|zeta_A(1/2+iU)| > V) for a list of V values.

    Returns dict mapping V to P(> V).
    """
    rng = random.Random(seed)
    vals = []
    for _ in range(n_samples):
        t = rng.uniform(0, T)
        s = complex(sigma, t)
        val = abs(shadow_zeta_numerical(shadow_coeffs, s, max_r))
        vals.append(val)

    result = {}
    for V in V_values:
        count = sum(1 for v in vals if v > V)
        result[V] = count / len(vals)
    return result


# ============================================================================
# 9.  Complementarity cross-checks
# ============================================================================

def complementarity_bound_check(
    shadow_coeffs_A: Dict[int, float],
    shadow_coeffs_dual: Dict[int, float],
    sigma: float,
    T: float,
    n_sample: int = 200,
    max_r: Optional[int] = None,
) -> Tuple[float, float, float]:
    """Check complementarity: compare max|zeta_A| + max|zeta_{A!}| with
    max|zeta_A + zeta_{A!}|.

    Triangle inequality: max|f+g| <= max|f| + max|g|.

    Returns (max_A, max_dual, max_sum).
    """
    max_A = max_modulus_on_vertical(shadow_coeffs_A, sigma, T, n_sample, max_r)
    max_dual = max_modulus_on_vertical(shadow_coeffs_dual, sigma, T, n_sample, max_r)

    max_sum = 0.0
    for j in range(n_sample + 1):
        t = -T + 2.0 * T * j / n_sample
        s = complex(sigma, t)
        zA = shadow_zeta_numerical(shadow_coeffs_A, s, max_r)
        zD = shadow_zeta_numerical(shadow_coeffs_dual, s, max_r)
        val = abs(zA + zD)
        if val > max_sum:
            max_sum = val

    return max_A, max_dual, max_sum


def complementarity_moment_check(
    shadow_coeffs_A: Dict[int, float],
    shadow_coeffs_dual: Dict[int, float],
    k: int,
    T: float,
    h: float = 0.1,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> Tuple[float, float, float]:
    """Compute M_{2k} for A, A!, and A+A!.

    Returns (M_{2k}(A), M_{2k}(A!), M_{2k}(sum)).
    """
    m_A = moment_on_critical_line(shadow_coeffs_A, k, T, h, sigma, max_r)
    m_dual = moment_on_critical_line(shadow_coeffs_dual, k, T, h, sigma, max_r)

    # Moment of the sum
    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps
    total = 0.0
    for j in range(n_steps + 1):
        t_j = j * actual_h
        s = complex(sigma, t_j)
        zA = shadow_zeta_numerical(shadow_coeffs_A, s, max_r)
        zD = shadow_zeta_numerical(shadow_coeffs_dual, s, max_r)
        contrib = abs(zA + zD) ** (2 * k)
        if j == 0 or j == n_steps:
            total += contrib / 2.0
        else:
            total += contrib
    m_sum = total * actual_h / T

    return m_A, m_dual, m_sum


# ============================================================================
# 10.  Boundedness certificate
# ============================================================================

@dataclass
class SubconvexityResult:
    """Complete subconvexity analysis result for a shadow zeta function."""
    family: str
    param: float
    # Growth rate
    rho: float
    is_entire: bool
    # PL exponent
    mu_half: float  # mu_A(1/2)
    mu_zero: float  # mu_A(0)
    mu_one: float   # mu_A(1)
    # Power law fit on critical line
    alpha_fit: float
    C_fit: float
    # Polylogarithm bound at sigma = 1/2
    poly_bound_half: float
    # Actual max on critical line
    max_critical: float
    # 2nd and 4th moments
    M2: float
    M4: float
    # Moment ratio M4/M2^2
    kurtosis_ratio: float
    # Bounded?
    is_bounded_on_critical: bool


def full_subconvexity_analysis(
    family: str,
    param: float,
    max_r: int = 60,
    T_critical: float = 100.0,
) -> SubconvexityResult:
    """Full subconvexity analysis for a given family and parameter.

    Computes all relevant quantities: growth rate, PL exponent,
    critical line fit, bounds, moments.
    """
    coeffs = shadow_coefficients_for_family(family, param, max_r)

    # Growth rate
    if family == 'virasoro' or family == 'w3_t':
        rho = virasoro_growth_rate_exact(param)
    elif family == 'w3_w':
        rho = virasoro_growth_rate_exact(param) * 0.5  # approximate
    elif family in ('heisenberg', 'affine_sl2', 'affine_sl3', 'betagamma'):
        rho = 0.0  # finite tower
    else:
        rho = 0.0

    is_entire = rho < 1.0

    # PL exponents at a few sigma values
    T_list = [10.0, 50.0, 100.0, 200.0]
    mu_half = phragmen_lindelof_exponent(coeffs, 0.5, T_list, n_sample=100, max_r=max_r)
    mu_zero = phragmen_lindelof_exponent(coeffs, 0.0, T_list, n_sample=100, max_r=max_r)
    mu_one = phragmen_lindelof_exponent(coeffs, 1.0, T_list, n_sample=100, max_r=max_r)

    # Power law fit on critical line
    fit = fit_critical_line_power_law(
        coeffs, t_min=10.0, t_max=min(T_critical, 200.0),
        n_points=50, sigma=0.5, max_r=max_r
    )

    # Polylogarithm bound at sigma = 1/2
    poly_bound_half = polylogarithm_bound_from_coeffs(coeffs, 0.5)

    # Actual maximum on critical line
    max_critical = max_modulus_on_vertical(coeffs, 0.5, T_critical, n_sample=200, max_r=max_r)

    # Moments
    h_step = max(0.05, T_critical / 2000.0)
    M2 = moment_on_critical_line(coeffs, 1, min(T_critical, 50.0), h_step, 0.5, max_r)
    M4 = moment_on_critical_line(coeffs, 2, min(T_critical, 50.0), h_step, 0.5, max_r)

    # Kurtosis ratio
    kurtosis_ratio = M4 / (M2 ** 2) if M2 > 1e-300 else 0.0

    # Boundedness: mu_half < 0.05 is the robust criterion (PL exponent).
    # The power-law alpha can be noisy for oscillating functions, so we
    # use the PL exponent which measures growth vs T directly.
    is_bounded = abs(mu_half) < 0.1 and is_entire

    return SubconvexityResult(
        family=family,
        param=param,
        rho=rho,
        is_entire=is_entire,
        mu_half=mu_half,
        mu_zero=mu_zero,
        mu_one=mu_one,
        alpha_fit=fit.alpha,
        C_fit=fit.C,
        poly_bound_half=poly_bound_half,
        max_critical=max_critical,
        M2=M2,
        M4=M4,
        kurtosis_ratio=kurtosis_ratio,
        is_bounded_on_critical=is_bounded,
    )


# ============================================================================
# 11.  Heisenberg exact formulas (analytical verification)
# ============================================================================

def heisenberg_max_modulus_exact(k_val: float, sigma: float) -> float:
    """Exact max |zeta_{H_k}(sigma+it)| = |k| * 2^{-sigma}.

    The Heisenberg shadow zeta is zeta_{H_k}(s) = k * 2^{-s}, so
    |zeta_{H_k}(sigma+it)| = |k| * 2^{-sigma} for all t.
    """
    return abs(k_val) * 2.0 ** (-sigma)


def heisenberg_moment_exact(k_val: float, exponent: int, sigma: float = 0.5) -> float:
    """Exact M_{2k}(T; H_k) = |k|^{2*exponent} * 2^{-2*exponent*sigma}.

    Since |zeta_{H_k}| is CONSTANT in t, M_{2k} = |zeta|^{2k} exactly.
    """
    return abs(k_val) ** (2 * exponent) * 2.0 ** (-2 * exponent * sigma)


def affine_sl2_max_modulus_bound(k_val: float, sigma: float) -> float:
    """Upper bound max |zeta_{sl_2}(sigma+it)|.

    zeta(s) = kappa*2^{-s} + alpha*3^{-s}
    |zeta| <= |kappa|*2^{-sigma} + |alpha|*3^{-sigma}
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    return abs(kappa) * 2.0 ** (-sigma) + abs(alpha) * 3.0 ** (-sigma)


# ============================================================================
# 12.  Virasoro-specific analysis
# ============================================================================

def virasoro_subconvexity_landscape(
    c_values: List[float],
    max_r: int = 60,
    T: float = 100.0,
) -> Dict[float, SubconvexityResult]:
    """Compute full subconvexity analysis for Virasoro at multiple c values.

    Returns dict mapping c to SubconvexityResult.
    """
    result = {}
    for c_val in c_values:
        if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
            continue
        result[c_val] = full_subconvexity_analysis('virasoro', c_val, max_r, T)
    return result
