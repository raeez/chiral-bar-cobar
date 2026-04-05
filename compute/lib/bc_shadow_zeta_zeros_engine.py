r"""Shadow zeta zeros: zero distribution, pair correlation, and Li coefficients.

For a modular Koszul algebra A with shadow coefficients S_r(A), define
the shadow zeta function:

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}

This module computes and classifies the ZEROS of zeta_A(s):

FINITE TOWERS (class G, L, C):
    zeta_A(s) = sum_{r=2}^{r_max} S_r * r^{-s}
    Substituting w = 2^{-s} (for class G), or w_r = r^{-s}, this becomes a
    polynomial/exponential polynomial.  For the Heisenberg case (class G):
        zeta_{H_k}(s) = k * 2^{-s} = 0  has NO zeros (k != 0).
    For class L (e.g., affine sl_2):
        zeta(s) = kappa * 2^{-s} + alpha * 3^{-s}
    Setting u = 3^{-s}/2^{-s} = (2/3)^s:
        zeros when u = -kappa/alpha, i.e., s = log(-kappa/alpha) / log(2/3).
        Since kappa, alpha > 0 for affine KM, the argument is negative:
        s is complex with Im(s) = pi / log(3/2) * (2n+1).
    For class C:
        zeta(s) = S_2 * 2^{-s} + S_3 * 3^{-s} + S_4 * 4^{-s}
        Three-term exponential polynomial; zeros found numerically.

INFINITE TOWERS (class M):
    The Dirichlet series converges for Re(s) > sigma_c.  When rho < 1
    (entire function), the zero set is discrete and countable.  The
    zero-counting function N_A(T) = #{zeros with |Im(s)| < T} satisfies
    a Riemann-von Mangoldt type estimate:
        N_A(T) ~ (T / pi) * log(T / (2*pi*e)) + O(log T)
    modified by the growth characteristics of the shadow tower.

PAIR CORRELATION:
    For the normalized zero spacings delta_n = (gamma_{n+1} - gamma_n) *
    (log(gamma_n)/(2*pi)), the pair correlation function
        R_2(x) = lim_{N->infty} (1/N) * #{n <= N : delta_n * N/gamma_N < x}
    is tested against:
        GUE: R_2(x) = 1 - (sin(pi*x)/(pi*x))^2  (random matrix)
        Poisson: R_2(x) = 1  (independent)

FUNCTIONAL EQUATION (from Theorem C):
    For Virasoro: zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) = zeta_D(s)
    where D_r(c) = S_r(c) + S_r(26-c) is the complementarity sum.
    At the self-dual point c = 13: zeta_{Vir_13}(s) = zeta_D(s) / 2.

SHADOW LI COEFFICIENTS:
    lambda_n^sh(A) = sum_rho (1 - (1 - 1/rho)^n)
    where the sum runs over nontrivial zeros rho of zeta_A.
    Positivity of lambda_n^sh for all n >= 1 is the analogue of the
    Li criterion for the Riemann zeta function.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify zeros by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# ---------------------------------------------------------------------------
# Import shadow coefficient providers from the existing engine
# ---------------------------------------------------------------------------
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
# 1.  Extended shadow coefficient computation through arity 100
# ============================================================================

def shadow_coefficients_extended(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Compute shadow coefficients S_r through arity max_r for a given family.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'betagamma', 'virasoro', 'w3_t', 'w3_w'
    param : family parameter (k for Heis/affine, lambda for betagamma,
            c for Virasoro/W3)
    max_r : maximum arity (default 100)

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
        raise ValueError(f"Unknown family: {family}. Choose from {list(dispatch.keys())}")
    return dispatch[family]()


def koszul_dual_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Shadow coefficients of the Koszul dual A!.

    Uses the family-specific Koszul duality:
        Heisenberg:  H_k^! has kappa = -k (but H_k^! != H_{-k}, see AP33).
                     Shadow coeffs: S_2 = -k, S_r = 0 for r >= 3.
        Affine sl_2: V_k(sl_2)^! ~ V_{-k-4}(sl_2) at the level of shadows.
                     kappa' = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
        Affine sl_3: V_k(sl_3)^! ~ V_{-k-6}(sl_3) at shadow level.
                     kappa' = 8(-k-6+3)/6 = -4(k+3)/3.
        Virasoro:    Vir_c^! = Vir_{26-c}.
        Beta-gamma:  bg(lambda)^! has c' = 26 - c(lambda).
        W_3:         W_3(c)^! corresponds to W_3(c') with c' from duality.

    CAUTION (AP33): H_k^! = Sym^ch(V*) != H_{-k}.
    CAUTION (AP24): kappa + kappa' = 13 for Virasoro, NOT 0.
    """
    if family == 'heisenberg':
        # H_k^! has kappa = -k at the shadow level
        # This gives a single-term zeta with NEGATIVE coefficient
        result = {2: -float(param)}
        for r in range(3, max_r + 1):
            result[r] = 0.0
        return result
    elif family == 'affine_sl2':
        # Feigin-Frenkel: k -> -k - 2h^v = -k - 4
        return affine_sl2_shadow_coefficients(-param - 4.0, max_r)
    elif family == 'affine_sl3':
        return affine_sl3_shadow_coefficients(-param - 6.0, max_r)
    elif family == 'virasoro':
        return virasoro_shadow_coefficients_numerical(26.0 - param, max_r)
    elif family == 'betagamma':
        c_val = 2.0 * (6.0 * param ** 2 - 6.0 * param + 1.0)
        c_dual = 26.0 - c_val
        # beta-gamma dual is Virasoro-like at c_dual
        return virasoro_shadow_coefficients_numerical(c_dual, max_r)
    elif family in ('w3_t', 'w3_w'):
        # W_3 duality is more complex; use c -> c' duality on the T/W line
        # For the T-line, Koszul duality acts as Virasoro duality c -> 26-c
        if family == 'w3_t':
            return w3_t_line_shadow_coefficients(26.0 - param, max_r)
        else:
            return w3_w_line_shadow_coefficients(26.0 - param, max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 2.  Zero-finding engine
# ============================================================================

def _shadow_zeta_complex(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate zeta_A(s) for complex s.  Thin wrapper."""
    return shadow_zeta_numerical(shadow_coeffs, s, max_r)


def _shadow_zeta_derivative(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate zeta_A'(s) = -sum_{r >= 2} S_r * log(r) * r^{-s}."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total -= Sr * math.log(r) * r ** (-s)
    return total


def newton_zero(
    shadow_coeffs: Dict[int, float],
    s0: complex,
    max_iter: int = 200,
    tol: float = 1e-12,
    max_r: Optional[int] = None,
) -> Optional[complex]:
    """Find a zero of zeta_A(s) near s0 using Newton's method.

    Returns the zero if convergence is achieved within max_iter steps,
    or None if the method fails to converge.
    """
    s = s0
    for _ in range(max_iter):
        f = _shadow_zeta_complex(shadow_coeffs, s, max_r)
        fp = _shadow_zeta_derivative(shadow_coeffs, s, max_r)
        if abs(fp) < 1e-300:
            return None
        ds = f / fp
        s = s - ds
        if abs(ds) < tol:
            # Verify that we are at a zero
            f_check = _shadow_zeta_complex(shadow_coeffs, s, max_r)
            if abs(f_check) < tol * 100:
                return s
            else:
                return None
    return None


def muller_zero(
    shadow_coeffs: Dict[int, float],
    s0: complex,
    s1: complex,
    s2: complex,
    max_iter: int = 200,
    tol: float = 1e-12,
    max_r: Optional[int] = None,
) -> Optional[complex]:
    """Find a zero of zeta_A(s) using Muller's method (no derivative needed).

    Takes three initial guesses s0, s1, s2.
    """
    f = lambda z: _shadow_zeta_complex(shadow_coeffs, z, max_r)
    z0, z1, z2 = s0, s1, s2
    f0, f1, f2 = f(z0), f(z1), f(z2)

    for _ in range(max_iter):
        # Divided differences
        h1 = z1 - z0
        h2 = z2 - z1
        if abs(h1) < 1e-300 or abs(h2) < 1e-300:
            return None
        delta1 = (f1 - f0) / h1
        delta2 = (f2 - f1) / h2
        d = (delta2 - delta1) / (h2 + h1)
        # Quadratic coefficients
        b = delta2 + h2 * d
        # Discriminant
        disc = b * b - 4.0 * f2 * d
        sq = cmath.sqrt(disc)
        # Pick denominator with larger absolute value (avoid cancellation)
        denom1 = b + sq
        denom2 = b - sq
        denom = denom1 if abs(denom1) >= abs(denom2) else denom2
        if abs(denom) < 1e-300:
            return None
        dz = -2.0 * f2 / denom
        z3 = z2 + dz

        if abs(dz) < tol:
            f3 = f(z3)
            if abs(f3) < tol * 100:
                return z3
            else:
                return None

        z0, z1, z2 = z1, z2, z3
        f0, f1, f2 = f1, f2, f(z3)

    return None


def find_zeros_grid(
    shadow_coeffs: Dict[int, float],
    re_range: Tuple[float, float] = (-10.0, 10.0),
    im_range: Tuple[float, float] = (-100.0, 100.0),
    grid_re: int = 40,
    grid_im: int = 200,
    tol: float = 1e-10,
    max_r: Optional[int] = None,
    dedup_tol: float = 1e-6,
) -> List[complex]:
    """Find zeros of zeta_A(s) in the strip re_range x im_range.

    Seeds Newton's method from a grid of starting points.  Deduplicates
    results that converge to the same zero.

    Parameters
    ----------
    shadow_coeffs : dict of shadow coefficients
    re_range : (Re_min, Re_max) for the search strip
    im_range : (Im_min, Im_max) for the search strip
    grid_re : number of grid points along Re axis
    grid_im : number of grid points along Im axis
    tol : convergence tolerance for Newton's method
    max_r : maximum arity for zeta evaluation
    dedup_tol : tolerance for deduplication

    Returns
    -------
    Sorted list of zeros (by imaginary part, then real part).
    """
    zeros = []

    re_step = (re_range[1] - re_range[0]) / max(grid_re - 1, 1)
    im_step = (im_range[1] - im_range[0]) / max(grid_im - 1, 1)

    for i in range(grid_re):
        for j in range(grid_im):
            re = re_range[0] + i * re_step
            im = im_range[0] + j * im_step
            s0 = complex(re, im)

            z = newton_zero(shadow_coeffs, s0, tol=tol, max_r=max_r)
            if z is not None:
                # Check it is in the search region (with some margin)
                margin = 2.0
                if (re_range[0] - margin <= z.real <= re_range[1] + margin and
                        im_range[0] - margin <= z.imag <= im_range[1] + margin):
                    zeros.append(z)

    return _deduplicate_zeros(zeros, dedup_tol)


def _deduplicate_zeros(zeros: List[complex], tol: float = 1e-6) -> List[complex]:
    """Remove duplicate zeros (those within tol of each other)."""
    if not zeros:
        return []
    unique = []
    for z in zeros:
        is_dup = False
        for u in unique:
            if abs(z - u) < tol:
                is_dup = True
                break
        if not is_dup:
            unique.append(z)
    # Sort by imaginary part, then real part
    unique.sort(key=lambda z: (z.imag, z.real))
    return unique


# ============================================================================
# 3.  Exact zeros for finite towers
# ============================================================================

def heisenberg_zeros(k_val: float) -> List[complex]:
    """Zeros of zeta_{H_k}(s) = k * 2^{-s}.

    For k != 0: no zeros (k * 2^{-s} != 0 for all s).
    For k = 0: identically zero (every s is a "zero").
    """
    if k_val == 0.0:
        return []  # Degenerate: identically zero
    return []  # No zeros


def affine_sl2_zeros(
    k_val: float,
    n_max: int = 50,
) -> List[complex]:
    """Zeros of zeta_{sl_2,k}(s) = kappa * 2^{-s} + alpha * 3^{-s}.

    Setting u = (3/2)^{-s}:
        0 = kappa + alpha * u  =>  u = -kappa/alpha
        (3/2)^{-s} = -kappa/alpha
        -s * log(3/2) = log(-kappa/alpha)
        s = -log(-kappa/alpha) / log(3/2)

    For kappa, alpha > 0: -kappa/alpha < 0, so:
        log(-kappa/alpha) = log(kappa/alpha) + i*pi*(2n+1)
        s = -(log(kappa/alpha) + i*pi*(2n+1)) / log(3/2)
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)

    if alpha == 0 or kappa == 0:
        return []

    ratio = kappa / alpha
    log_32 = math.log(3.0 / 2.0)

    zeros = []
    for n in range(-n_max, n_max + 1):
        # s = -(log(ratio) + i*pi*(2n+1)) / log(3/2)
        s_real = -math.log(ratio) / log_32
        s_imag = -math.pi * (2 * n + 1) / log_32
        zeros.append(complex(s_real, s_imag))

    zeros.sort(key=lambda z: (abs(z.imag), z.real))
    return zeros


def affine_sl3_zeros(
    k_val: float,
    n_max: int = 50,
) -> List[complex]:
    """Zeros of zeta_{sl_3,k}(s) = kappa * 2^{-s} + alpha * 3^{-s}.

    Same structure as sl_2: two-term exponential polynomial.
    """
    h_dual = 3.0
    dim_g = 8.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)

    if alpha == 0 or kappa == 0:
        return []

    ratio = kappa / alpha
    log_32 = math.log(3.0 / 2.0)

    zeros = []
    for n in range(-n_max, n_max + 1):
        s_real = -math.log(ratio) / log_32
        s_imag = -math.pi * (2 * n + 1) / log_32
        zeros.append(complex(s_real, s_imag))

    zeros.sort(key=lambda z: (abs(z.imag), z.real))
    return zeros


def betagamma_zeros_numerical(
    lam_val: float = 0.5,
    re_range: Tuple[float, float] = (-10.0, 10.0),
    im_range: Tuple[float, float] = (-100.0, 100.0),
    grid_re: int = 30,
    grid_im: int = 100,
) -> List[complex]:
    """Zeros of zeta_{bg}(s) = S_2*2^{-s} + S_3*3^{-s} + S_4*4^{-s}.

    Three-term exponential polynomial.  No closed-form in general;
    use grid Newton search.
    """
    coeffs = betagamma_shadow_coefficients(lam_val, max_r=4)
    return find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=4)


# ============================================================================
# 4.  Zero counting function N_A(T)
# ============================================================================

def zero_counting_function(
    zeros: List[complex],
    T_values: List[float],
) -> Dict[float, int]:
    """N_A(T) = #{zeros with |Im(s)| < T}.

    Parameters
    ----------
    zeros : list of zeros (complex)
    T_values : list of T values at which to evaluate N_A

    Returns
    -------
    Dict mapping T to N_A(T).
    """
    result = {}
    for T in T_values:
        count = sum(1 for z in zeros if abs(z.imag) < T)
        result[T] = count
    return result


def fit_riemann_von_mangoldt(
    zeros: List[complex],
    T_min: float = 10.0,
    T_max: float = 100.0,
    n_points: int = 20,
) -> Dict[str, float]:
    """Fit N_A(T) ~ (C1/pi) * T * log(T) + C2 * T + C3.

    The Riemann-von Mangoldt formula for the Riemann zeta is:
        N(T) = (T/(2*pi)) * log(T/(2*pi*e)) + O(log T)
             = (T/(2*pi)) * log(T) - (T/(2*pi))*(1 + log(2*pi)) + O(log T)

    For the shadow zeta, we fit the analogous form
        N_A(T) = a * T * log(T) + b * T + c
    and extract the effective coefficients.

    Returns dict with 'a', 'b', 'c', 'r_squared'.
    """
    import numpy as np

    T_vals = np.linspace(T_min, T_max, n_points)
    N_vals = []
    for T in T_vals:
        count = sum(1 for z in zeros if abs(z.imag) < T)
        N_vals.append(count)

    N_vals = np.array(N_vals, dtype=float)

    # Design matrix: [T*log(T), T, 1]
    X = np.column_stack([
        T_vals * np.log(T_vals),
        T_vals,
        np.ones_like(T_vals),
    ])

    # Least squares fit
    try:
        coeffs, residuals, _, _ = np.linalg.lstsq(X, N_vals, rcond=None)
    except np.linalg.LinAlgError:
        return {'a': 0.0, 'b': 0.0, 'c': 0.0, 'r_squared': 0.0}

    a, b, c = coeffs

    # R-squared
    N_pred = X @ coeffs
    ss_res = np.sum((N_vals - N_pred) ** 2)
    ss_tot = np.sum((N_vals - np.mean(N_vals)) ** 2)
    r_sq = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0

    return {'a': float(a), 'b': float(b), 'c': float(c), 'r_squared': float(r_sq)}


# ============================================================================
# 5.  Argument principle: contour integral of zeta'/zeta
# ============================================================================

def argument_principle_count(
    shadow_coeffs: Dict[int, float],
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    n_points: int = 2000,
    max_r: Optional[int] = None,
) -> int:
    """Count zeros of zeta_A(s) in a rectangle via the argument principle.

    The argument principle states:
        (1/(2*pi*i)) * oint (zeta'/zeta)(s) ds = N - P

    where N = number of zeros and P = number of poles inside the contour.
    For a Dirichlet series with no poles in the region, N = winding number.

    We integrate along the boundary of the rectangle
    [re_range[0], re_range[1]] x [im_range[0], im_range[1]].

    Returns the estimated number of zeros (rounded to nearest integer).
    """
    def zeta(s):
        return _shadow_zeta_complex(shadow_coeffs, s, max_r)

    # Parameterize the rectangular contour
    re_lo, re_hi = re_range
    im_lo, im_hi = im_range

    # Four sides: bottom, right, top, left
    total_winding = 0.0

    def _integrate_segment(s_start, s_end, n_pts):
        """Compute (1/(2*pi*i)) * integral of zeta'/zeta along segment."""
        winding = 0.0
        prev_val = zeta(s_start)
        for k in range(1, n_pts + 1):
            t_frac = k / n_pts
            s = s_start + t_frac * (s_end - s_start)
            curr_val = zeta(s)
            if abs(prev_val) > 1e-300 and abs(curr_val) > 1e-300:
                ratio = curr_val / prev_val
                # Accumulate the argument change
                winding += cmath.phase(ratio)
            prev_val = curr_val
        return winding

    pts_per_side = n_points // 4

    # Bottom: left to right
    w1 = _integrate_segment(complex(re_lo, im_lo), complex(re_hi, im_lo), pts_per_side)
    # Right: bottom to top
    w2 = _integrate_segment(complex(re_hi, im_lo), complex(re_hi, im_hi), pts_per_side)
    # Top: right to left
    w3 = _integrate_segment(complex(re_hi, im_hi), complex(re_lo, im_hi), pts_per_side)
    # Left: top to bottom
    w4 = _integrate_segment(complex(re_lo, im_hi), complex(re_lo, im_lo), pts_per_side)

    total_winding = w1 + w2 + w3 + w4
    n_zeros = total_winding / (2.0 * math.pi)
    return round(n_zeros)


# ============================================================================
# 6.  Pair correlation of zeros
# ============================================================================

def normalized_spacings(zeros: List[complex]) -> List[float]:
    """Compute normalized spacings between consecutive zeros on the imaginary axis.

    Given zeros sorted by Im(s), the normalized spacing is:
        delta_n = (Im(s_{n+1}) - Im(s_n)) * mean_density

    where mean_density = N / (Im(s_N) - Im(s_1)).
    """
    # Extract imaginary parts of zeros with positive imaginary part (by symmetry)
    gammas = sorted([z.imag for z in zeros if z.imag > 0.1])
    if len(gammas) < 3:
        return []

    mean_density = (len(gammas) - 1) / (gammas[-1] - gammas[0])
    spacings = []
    for i in range(len(gammas) - 1):
        delta = (gammas[i + 1] - gammas[i]) * mean_density
        spacings.append(delta)
    return spacings


def pair_correlation_histogram(
    zeros: List[complex],
    n_bins: int = 30,
    x_max: float = 3.0,
) -> Tuple[List[float], List[float]]:
    """Compute the pair correlation histogram R_2(x).

    Bins the normalized spacings and compares to GUE and Poisson predictions.

    Returns (bin_centers, histogram_values) where histogram_values are the
    empirical pair correlation densities.
    """
    spacings = normalized_spacings(zeros)
    if not spacings:
        return [], []

    bin_edges = [i * x_max / n_bins for i in range(n_bins + 1)]
    bin_centers = [(bin_edges[i] + bin_edges[i + 1]) / 2 for i in range(n_bins)]
    counts = [0] * n_bins
    for s in spacings:
        if s < x_max:
            idx = int(s * n_bins / x_max)
            if 0 <= idx < n_bins:
                counts[idx] += 1

    total = len(spacings)
    dx = x_max / n_bins
    histogram = [c / (total * dx) if total > 0 else 0.0 for c in counts]
    return bin_centers, histogram


def gue_pair_correlation(x: float) -> float:
    """GUE (Gaussian Unitary Ensemble) pair correlation function.

    R_2^{GUE}(x) = 1 - (sin(pi*x) / (pi*x))^2  for x > 0.

    This is the Montgomery conjecture prediction for the zeros of the
    Riemann zeta function.
    """
    if abs(x) < 1e-15:
        return 0.0
    sinc = math.sin(math.pi * x) / (math.pi * x)
    return 1.0 - sinc * sinc


def poisson_pair_correlation(x: float) -> float:
    """Poisson (uncorrelated) pair correlation function.

    R_2^{Poisson}(x) = 1 for all x.
    """
    return 1.0


def pair_correlation_statistic(
    zeros: List[complex],
    n_bins: int = 30,
    x_max: float = 3.0,
) -> Dict[str, float]:
    """Compute chi-squared statistics against GUE and Poisson models.

    Returns dict with:
        'chi2_gue': chi-squared statistic against GUE
        'chi2_poisson': chi-squared statistic against Poisson
        'n_spacings': number of spacings used
        'mean_spacing': mean normalized spacing
        'variance_spacing': variance of normalized spacings
        'classification': 'GUE', 'Poisson', or 'intermediate'
    """
    bin_centers, histogram = pair_correlation_histogram(zeros, n_bins, x_max)
    if not histogram:
        return {
            'chi2_gue': float('inf'),
            'chi2_poisson': float('inf'),
            'n_spacings': 0,
            'mean_spacing': 0.0,
            'variance_spacing': 0.0,
            'classification': 'insufficient_data',
        }

    spacings = normalized_spacings(zeros)
    n_sp = len(spacings)
    mean_sp = sum(spacings) / n_sp if n_sp > 0 else 0.0
    var_sp = sum((s - mean_sp) ** 2 for s in spacings) / n_sp if n_sp > 1 else 0.0

    chi2_gue = 0.0
    chi2_poisson = 0.0
    for xc, h in zip(bin_centers, histogram):
        expected_gue = gue_pair_correlation(xc)
        expected_poisson = poisson_pair_correlation(xc)
        if expected_gue > 1e-10:
            chi2_gue += (h - expected_gue) ** 2 / expected_gue
        if expected_poisson > 1e-10:
            chi2_poisson += (h - expected_poisson) ** 2 / expected_poisson

    # Classification based on which model fits better
    if n_sp < 10:
        classification = 'insufficient_data'
    elif chi2_gue < chi2_poisson:
        classification = 'GUE'
    else:
        classification = 'Poisson'

    return {
        'chi2_gue': chi2_gue,
        'chi2_poisson': chi2_poisson,
        'n_spacings': n_sp,
        'mean_spacing': mean_sp,
        'variance_spacing': var_sp,
        'classification': classification,
    }


# ============================================================================
# 7.  Functional equation from complementarity (Theorem C)
# ============================================================================

def complementarity_sum_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """D_r = S_r(A) + S_r(A!) for each r.

    For Virasoro: D_r(c) = S_r(c) + S_r(26-c).
    At r=2: D_2 = c/2 + (26-c)/2 = 13 (Theorem C scalar level, AP24).
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    dual_coeffs = koszul_dual_coefficients(family, param, max_r)
    result = {}
    for r in range(2, max_r + 1):
        result[r] = coeffs.get(r, 0.0) + dual_coeffs.get(r, 0.0)
    return result


def functional_equation_zeta(
    family: str,
    param: float,
    s_values: List[complex],
    max_r: int = 100,
) -> List[Dict[str, complex]]:
    """Test zeta_A(s) + zeta_{A!}(s) = zeta_D(s) at given s-values.

    Returns list of dicts with 'zeta_A', 'zeta_dual', 'zeta_sum', 'zeta_D',
    and 'error' for each s.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    dual_coeffs = koszul_dual_coefficients(family, param, max_r)
    D_coeffs = complementarity_sum_coefficients(family, param, max_r)

    results = []
    for s in s_values:
        zA = _shadow_zeta_complex(coeffs, s, max_r)
        zD_dual = _shadow_zeta_complex(dual_coeffs, s, max_r)
        zD_sum = zA + zD_dual
        zD = _shadow_zeta_complex(D_coeffs, s, max_r)
        error = abs(zD_sum - zD)
        results.append({
            's': s,
            'zeta_A': zA,
            'zeta_dual': zD_dual,
            'zeta_sum': zD_sum,
            'zeta_D': zD,
            'error': error,
        })
    return results


def zero_complementarity_analysis(
    family: str,
    param: float,
    max_r: int = 100,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
) -> Dict[str, Any]:
    """Analyze how zeros of zeta_A and zeta_{A!} relate.

    For each zero rho of zeta_A, compute zeta_{A!}(rho) and vice versa.
    If there is a functional equation, zeros should be related.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    dual_coeffs = koszul_dual_coefficients(family, param, max_r)

    zeros_A = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)
    zeros_dual = find_zeros_grid(dual_coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)

    # For each zero of A, evaluate zeta_{A!}
    dual_at_A_zeros = []
    for z in zeros_A:
        val = _shadow_zeta_complex(dual_coeffs, z, max_r)
        dual_at_A_zeros.append((z, val))

    # For each zero of A!, evaluate zeta_A
    A_at_dual_zeros = []
    for z in zeros_dual:
        val = _shadow_zeta_complex(coeffs, z, max_r)
        A_at_dual_zeros.append((z, val))

    return {
        'zeros_A': zeros_A,
        'zeros_dual': zeros_dual,
        'n_zeros_A': len(zeros_A),
        'n_zeros_dual': len(zeros_dual),
        'dual_at_A_zeros': dual_at_A_zeros,
        'A_at_dual_zeros': A_at_dual_zeros,
    }


# ============================================================================
# 8.  Shadow Li coefficients
# ============================================================================

def shadow_li_coefficients(
    zeros: List[complex],
    n_max: int = 20,
) -> List[float]:
    """Compute shadow Li coefficients lambda_n^sh(A).

    lambda_n = sum_rho (1 - (1 - 1/rho)^n)

    where the sum runs over nontrivial zeros rho of zeta_A.

    For the Riemann zeta, the Li criterion states:
        lambda_n >= 0 for all n >= 1  <==>  RH holds.

    We compute the analogous invariants for the shadow zeta.

    Parameters
    ----------
    zeros : list of nontrivial zeros
    n_max : compute lambda_1, ..., lambda_{n_max}

    Returns
    -------
    List [lambda_1, lambda_2, ..., lambda_{n_max}].
    """
    if not zeros:
        return [0.0] * n_max

    lambdas = []
    for n in range(1, n_max + 1):
        total = 0.0
        for rho in zeros:
            if abs(rho) < 1e-15:
                continue
            w = 1.0 - 1.0 / rho
            try:
                term = 1.0 - w ** n
                total += term.real  # Take real part (imaginary parts cancel in conjugate pairs)
            except (OverflowError, ZeroDivisionError):
                pass
        lambdas.append(total)
    return lambdas


def li_criterion_test(
    zeros: List[complex],
    n_max: int = 20,
) -> Dict[str, Any]:
    """Test the shadow Li criterion: are all lambda_n^sh positive?

    Returns dict with:
        'coefficients': list of lambda_n values
        'all_positive': bool
        'first_negative': index of first negative lambda (or -1)
        'min_value': minimum lambda_n
    """
    lambdas = shadow_li_coefficients(zeros, n_max)
    all_pos = all(lam >= -1e-10 for lam in lambdas)
    first_neg = -1
    for i, lam in enumerate(lambdas):
        if lam < -1e-10:
            first_neg = i + 1  # 1-indexed
            break

    return {
        'coefficients': lambdas,
        'all_positive': all_pos,
        'first_negative': first_neg,
        'min_value': min(lambdas) if lambdas else 0.0,
    }


# ============================================================================
# 9.  Product over zeros reconstruction (verification path 3)
# ============================================================================

def hadamard_product_reconstruction(
    zeros: List[complex],
    s: complex,
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    s_ref: complex = complex(5.0, 0),
) -> Dict[str, complex]:
    """Reconstruct zeta_A(s) from product over zeros (Hadamard factorization).

    For an entire function of finite order with zeros {rho_k}:
        f(s) = f(s_ref) * prod_k (1 - s/rho_k) / (1 - s_ref/rho_k)

    We normalize by comparing at s_ref = 5.0 (safely in the convergence region).

    Returns dict with 'product_value', 'direct_value', 'relative_error'.
    """
    direct = _shadow_zeta_complex(shadow_coeffs, s, max_r)
    ref_val = _shadow_zeta_complex(shadow_coeffs, s_ref, max_r)

    if abs(ref_val) < 1e-300:
        return {
            'product_value': complex(0, 0),
            'direct_value': direct,
            'relative_error': float('inf'),
        }

    product = ref_val
    for rho in zeros:
        if abs(rho) < 1e-15:
            continue
        num = 1.0 - s / rho
        den = 1.0 - s_ref / rho
        if abs(den) > 1e-15:
            product *= num / den

    rel_err = abs(product - direct) / abs(direct) if abs(direct) > 1e-300 else float('inf')

    return {
        'product_value': product,
        'direct_value': direct,
        'relative_error': rel_err,
    }


# ============================================================================
# 10. Self-dual point analysis (c = 13 for Virasoro)
# ============================================================================

def self_dual_zero_analysis(
    c_val: float = 13.0,
    max_r: int = 100,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
) -> Dict[str, Any]:
    """Analyze zeros at the self-dual point c = 13 for Virasoro.

    At c = 13: Vir_c^! = Vir_{26-c} = Vir_{13}, so A = A!.
    The functional equation becomes 2*zeta_{Vir_13}(s) = zeta_D(s).
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    zeros = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)

    rho = virasoro_growth_rate_exact(c_val)

    return {
        'c': c_val,
        'kappa': c_val / 2.0,
        'growth_rate': rho,
        'n_zeros': len(zeros),
        'zeros': zeros,
        'is_self_dual': abs(c_val - 13.0) < 1e-10,
    }


# ============================================================================
# 11. Zero distribution statistics
# ============================================================================

def zero_real_part_statistics(
    zeros: List[complex],
) -> Dict[str, float]:
    """Statistics on the real parts of zeros.

    For a "critical line" analogy: if zeros cluster around Re(s) = sigma_0,
    this sigma_0 plays the role of the critical line Re(s) = 1/2 for
    the Riemann zeta.
    """
    if not zeros:
        return {'mean_re': 0.0, 'std_re': 0.0, 'median_re': 0.0,
                'min_re': 0.0, 'max_re': 0.0, 'n_zeros': 0}

    re_parts = [z.real for z in zeros]
    n = len(re_parts)
    mean_re = sum(re_parts) / n
    std_re = math.sqrt(sum((r - mean_re) ** 2 for r in re_parts) / n) if n > 1 else 0.0
    sorted_re = sorted(re_parts)
    median_re = sorted_re[n // 2] if n % 2 == 1 else (sorted_re[n // 2 - 1] + sorted_re[n // 2]) / 2

    return {
        'mean_re': mean_re,
        'std_re': std_re,
        'median_re': median_re,
        'min_re': min(re_parts),
        'max_re': max(re_parts),
        'n_zeros': n,
    }


def zero_spacing_statistics(
    zeros: List[complex],
) -> Dict[str, float]:
    """Statistics on the imaginary-part spacings of zeros.

    For the Riemann zeta, the mean spacing of zeros at height T is
    2*pi / log(T/(2*pi)).  We compute the analogous quantities.
    """
    gammas = sorted([z.imag for z in zeros if z.imag > 0.1])
    if len(gammas) < 2:
        return {'mean_gap': 0.0, 'min_gap': 0.0, 'max_gap': 0.0,
                'n_positive_zeros': len(gammas)}

    gaps = [gammas[i + 1] - gammas[i] for i in range(len(gammas) - 1)]
    mean_gap = sum(gaps) / len(gaps)
    min_gap = min(gaps)
    max_gap = max(gaps)

    return {
        'mean_gap': mean_gap,
        'min_gap': min_gap,
        'max_gap': max_gap,
        'n_positive_zeros': len(gammas),
    }


# ============================================================================
# 12. Full landscape zero analysis
# ============================================================================

@dataclass
class ShadowZetaZeroData:
    """Complete zero analysis for a shadow zeta function."""
    family: str
    param: float
    shadow_class: str  # G, L, C, M
    kappa: float
    growth_rate: float
    zeros: List[complex] = field(default_factory=list)
    n_zeros: int = 0
    zero_real_stats: Dict[str, float] = field(default_factory=dict)
    zero_spacing_stats: Dict[str, float] = field(default_factory=dict)
    pair_correlation: Dict[str, float] = field(default_factory=dict)
    li_test: Dict[str, Any] = field(default_factory=dict)
    counting_fit: Dict[str, float] = field(default_factory=dict)


def analyze_family(
    family: str,
    param: float,
    shadow_class: str,
    max_r: int = 100,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 80,
) -> ShadowZetaZeroData:
    """Full zero analysis for a given algebra family.

    Combines:
    - Zero finding (Newton grid search)
    - Real-part statistics
    - Spacing statistics
    - Pair correlation (GUE vs Poisson)
    - Li criterion
    - Riemann-von Mangoldt counting fit
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    kappa = coeffs.get(2, 0.0)

    # Compute growth rate
    if shadow_class == 'M' and family == 'virasoro':
        rho = virasoro_growth_rate_exact(param)
    else:
        rho = 0.0

    # Find zeros
    if shadow_class == 'G':
        zeros = heisenberg_zeros(param)
    elif shadow_class == 'L':
        if family == 'affine_sl2':
            zeros = affine_sl2_zeros(param)
            # Filter to search region
            zeros = [z for z in zeros
                     if re_range[0] <= z.real <= re_range[1]
                     and im_range[0] <= z.imag <= im_range[1]]
        elif family == 'affine_sl3':
            zeros = affine_sl3_zeros(param)
            zeros = [z for z in zeros
                     if re_range[0] <= z.real <= re_range[1]
                     and im_range[0] <= z.imag <= im_range[1]]
        else:
            zeros = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)
    elif shadow_class == 'C':
        zeros = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)
    else:  # M
        zeros = find_zeros_grid(coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r)

    result = ShadowZetaZeroData(
        family=family,
        param=param,
        shadow_class=shadow_class,
        kappa=kappa,
        growth_rate=rho,
        zeros=zeros,
        n_zeros=len(zeros),
    )

    result.zero_real_stats = zero_real_part_statistics(zeros)
    result.zero_spacing_stats = zero_spacing_statistics(zeros)

    if len(zeros) >= 10:
        result.pair_correlation = pair_correlation_statistic(zeros)
        result.li_test = li_criterion_test(zeros)
        result.counting_fit = fit_riemann_von_mangoldt(zeros)

    return result


def compute_full_landscape_zeros(
    max_r: int = 60,
    im_range: Tuple[float, float] = (-50.0, 50.0),
) -> Dict[str, ShadowZetaZeroData]:
    """Compute zero analysis for the full standard landscape."""
    landscape = {}

    # Class G: Heisenberg
    for k in [1, 2, 5]:
        name = f'Heis_k={k}'
        landscape[name] = analyze_family('heisenberg', float(k), 'G', max_r,
                                         im_range=im_range)

    # Class L: Affine KM
    for k in [1, 2, 3]:
        name = f'aff_sl2_k={k}'
        landscape[name] = analyze_family('affine_sl2', float(k), 'L', max_r,
                                         im_range=im_range)

    # Class C: Beta-gamma
    for lam in [0.5, 1.0]:
        name = f'bg_lam={lam}'
        landscape[name] = analyze_family('betagamma', lam, 'C', max_r,
                                         im_range=im_range)

    # Class M: Virasoro
    for c_val in [1.0, 6.0, 13.0, 25.0, 26.0]:
        name = f'Vir_c={c_val}'
        landscape[name] = analyze_family('virasoro', c_val, 'M', max_r,
                                         im_range=im_range)

    return landscape


# ============================================================================
# 13. Verification: polynomial root-finding for finite towers
# ============================================================================

def finite_tower_polynomial_zeros(
    shadow_coeffs: Dict[int, float],
    re_range: Tuple[float, float] = (-10.0, 10.0),
    im_range: Tuple[float, float] = (-100.0, 100.0),
    n_sample: int = 200,
) -> List[complex]:
    """For finite towers, convert to polynomial and find exact roots.

    For a tower with S_r != 0 only for r in {r_1, ..., r_k}:
        zeta_A(s) = sum_i S_{r_i} * r_i^{-s}

    Setting w = b^{-s} for some base b (smallest r_i):
        zeta_A = S_{r_1} * w^{a_1} + ... + S_{r_k} * w^{a_k}

    where a_i = log(r_i)/log(b).  If the r_i are not powers of a common
    base, we use numerical root-finding instead.

    This provides an independent verification of the grid Newton search.
    """
    # Find the nonzero terms
    nonzero = [(r, s) for r, s in shadow_coeffs.items() if abs(s) > 1e-50]
    if not nonzero:
        return []
    nonzero.sort()

    # For two-term series: exact solution
    if len(nonzero) == 1:
        return []  # Single nonzero term: no zeros (a * r^{-s} = 0 impossible)

    if len(nonzero) == 2:
        (r1, S1), (r2, S2) = nonzero
        # S1 * r1^{-s} + S2 * r2^{-s} = 0
        # r1^{-s} / r2^{-s} = -S2 / S1
        # (r2/r1)^s = -S2/S1
        ratio = -S2 / S1
        base = r2 / r1
        if abs(ratio) < 1e-300 or base <= 0:
            return []
        log_base = math.log(base)
        log_ratio_abs = math.log(abs(ratio))
        # s = (log|ratio| + i*(arg(ratio) + 2*n*pi)) / log(base)
        arg_ratio = math.pi if ratio < 0 else 0.0
        zeros = []
        for n in range(-n_sample, n_sample + 1):
            s_real = log_ratio_abs / log_base
            s_imag = (arg_ratio + 2 * n * math.pi) / log_base
            z = complex(s_real, s_imag)
            if (re_range[0] <= z.real <= re_range[1] and
                    im_range[0] <= z.imag <= im_range[1]):
                zeros.append(z)
        return _deduplicate_zeros(zeros)

    # For three or more terms: use grid Newton as fallback
    # (general multi-term exponential polynomials have no closed-form)
    max_r = max(r for r, _ in nonzero)
    return find_zeros_grid(shadow_coeffs, re_range, im_range,
                           grid_re=30, grid_im=100, max_r=max_r)


# ============================================================================
# 14. Critical line detector
# ============================================================================

def detect_critical_line(
    zeros: List[complex],
    tol: float = 0.5,
) -> Dict[str, Any]:
    """Detect whether zeros cluster around a critical line Re(s) = sigma_0.

    Analogous to Re(s) = 1/2 for the Riemann zeta function.

    Returns dict with:
        'sigma_0': estimated critical line
        'fraction_near': fraction of zeros with |Re(s) - sigma_0| < tol
        'has_critical_line': bool (True if > 80% of zeros are near the line)
    """
    if len(zeros) < 3:
        return {
            'sigma_0': float('nan'),
            'fraction_near': 0.0,
            'has_critical_line': False,
        }

    stats = zero_real_part_statistics(zeros)
    sigma_0 = stats['median_re']

    near_count = sum(1 for z in zeros if abs(z.real - sigma_0) < tol)
    fraction = near_count / len(zeros)

    return {
        'sigma_0': sigma_0,
        'fraction_near': fraction,
        'has_critical_line': fraction > 0.8,
        'std_re': stats['std_re'],
    }
