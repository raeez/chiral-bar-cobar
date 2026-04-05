r"""bc_btz_form_factor_engine.py -- BTZ spectral form factor from shadow pair correlation.

BC-91: SPECTRAL FORM FACTOR FROM SHADOW ZETA

THE CONSTRUCTION:

The spectral form factor (SFF) g(t) = |Z(beta + it)|^2 / |Z(beta)|^2 is the
primary diagnostic for quantum chaos in gravitational systems.  For BTZ black
holes, Z(beta) = sum e^{-beta E_n} sums over black hole microstates, and the
time-dependent form factor probes the statistical distribution of energy levels.

The shadow zeta function zeta_A(s) = sum_{r>=2} S_r(A) r^{-s} provides a
Dirichlet-series spectral decomposition attached to each modular Koszul
algebra A.  The shadow SFF is:

    g_A(t, beta) = |zeta_A(beta + it)|^2 / |zeta_A(beta)|^2

The SFF exhibits four regimes:

    1. SLOPE: initial decay g(t) ~ t^{-alpha} for small t.
    2. DIP: minimum at t = t_dip ("dip time").
    3. RAMP: linear growth g(t) ~ t/t_H for t_dip < t < t_H
       (signature of quantum chaos / random matrix universality).
    4. PLATEAU: g(t) -> g_inf for t > t_H (Heisenberg time).

The RAMP is the hallmark of GUE statistics:
    - GUE: ramp exists (linear in t), plateau at 1/D.
    - Poisson: no ramp (flat after dip).

For class M algebras (Virasoro, W_N) with infinite shadow depth, the
shadow SFF should exhibit GUE ramp, matching pair correlation findings.
For class G/L/C (finite tower), the SFF should be Poisson-like (no ramp).

CONNECTIONS:

1. The SFF is the Fourier transform of the 2-point correlation:
       g(t) = integral R_2(E) e^{itE} dE
   This connects to bc_pair_correlation_engine.

2. BTZ Hawking temperature: beta_H = 2*pi/kappa(A).
   At this temperature, g_A(t, 2*pi/kappa) is the "black hole form factor."

3. The plateau g_inf = 1/e^{S_BH} relates to Bekenstein-Hawking entropy.

4. The ramp slope determines the Thouless time, which scales with shadow
   depth: class G (no ramp) > class L > class C > class M (smallest t_Th).

Manuscript references:
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    shadow_zeta_function_engine.py (compute/lib/)
    bc_pair_correlation_engine.py (compute/lib/)
    bc_btz_spectral_zeta_engine.py (compute/lib/)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np


# ============================================================================
# 0.  Imports from existing engines (shadow coefficients, zeta evaluation)
# ============================================================================

from compute.lib.shadow_zeta_function_engine import (
    virasoro_shadow_coefficients_numerical,
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
)


# ============================================================================
# 1.  Shadow spectral form factor: direct computation
# ============================================================================

def shadow_sff_direct(
    shadow_coeffs: Dict[int, float],
    t: float,
    beta: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Shadow spectral form factor g_A(t, beta) by direct computation.

    g_A(t, beta) = |zeta_A(beta + it)|^2 / |zeta_A(beta)|^2

    Parameters
    ----------
    shadow_coeffs : dict mapping arity r to shadow coefficient S_r
    t : real time parameter
    beta : inverse temperature (real, positive)
    max_r : truncation arity

    Returns
    -------
    g_A(t, beta) >= 0.
    """
    z_beta = shadow_zeta_numerical(shadow_coeffs, complex(beta, 0), max_r)
    norm_sq_beta = abs(z_beta) ** 2
    if norm_sq_beta < 1e-300:
        return float('nan')
    z_complex = shadow_zeta_numerical(shadow_coeffs, complex(beta, t), max_r)
    return abs(z_complex) ** 2 / norm_sq_beta


def shadow_sff_time_series(
    shadow_coeffs: Dict[int, float],
    t_values: np.ndarray,
    beta: float,
    max_r: Optional[int] = None,
) -> np.ndarray:
    r"""Compute g_A(t, beta) for an array of time values.

    Vectorized for efficiency: precomputes |zeta_A(beta)|^2 once.
    """
    z_beta = shadow_zeta_numerical(shadow_coeffs, complex(beta, 0), max_r)
    norm_sq_beta = abs(z_beta) ** 2
    if norm_sq_beta < 1e-300:
        return np.full(len(t_values), float('nan'))

    result = np.zeros(len(t_values))
    for i, t in enumerate(t_values):
        z_t = shadow_zeta_numerical(shadow_coeffs, complex(beta, t), max_r)
        result[i] = abs(z_t) ** 2 / norm_sq_beta
    return result


def shadow_sff_virasoro(
    c_val: float,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> np.ndarray:
    r"""SFF for Virasoro at central charge c.

    Uses the Virasoro shadow coefficients from the convolution recursion.

    CAUTION (AP9): kappa(Vir_c) = c/2.  The shadow_sff uses the full
    Dirichlet series zeta_A(s), not just the leading kappa term.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    return shadow_sff_time_series(coeffs, t_values, beta, max_r)


# ============================================================================
# 2.  Normalization check: g_A(0, beta) = 1
# ============================================================================

def sff_normalization_check(
    shadow_coeffs: Dict[int, float],
    beta: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Verify g_A(0, beta) = 1.

    Returns |g_A(0, beta) - 1|. Should be < machine epsilon.
    """
    g0 = shadow_sff_direct(shadow_coeffs, 0.0, beta, max_r)
    return abs(g0 - 1.0)


# ============================================================================
# 3.  Dip, ramp, plateau identification
# ============================================================================

def find_dip_time(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 100.0,
    n_points: int = 1000,
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    r"""Find the dip time t_dip = argmin g_A(t, beta).

    Returns dict with:
        't_dip': time of minimum
        'g_dip': value at the dip
        'found': True if a clear minimum was found
    """
    t_values = np.linspace(0.01, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)

    # Find minimum
    idx_min = np.argmin(g_values)
    t_dip = t_values[idx_min]
    g_dip = g_values[idx_min]

    # Check if it's a genuine dip (not at the boundary)
    found = (0 < idx_min < n_points - 1)

    return {
        't_dip': float(t_dip),
        'g_dip': float(g_dip),
        'found': found,
    }


def estimate_heisenberg_time(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 200.0,
    n_points: int = 2000,
    max_r: Optional[int] = None,
    plateau_window: float = 0.2,
) -> Dict[str, float]:
    r"""Estimate the Heisenberg time t_H (onset of plateau).

    The Heisenberg time is t_H ~ 1/Delta where Delta is the mean level
    spacing of the shadow zeros.

    We estimate t_H by finding where g_A(t) first enters and stays within
    a tolerance of its late-time average.

    Returns dict with:
        't_H': estimated Heisenberg time
        'g_plateau': estimated plateau value
        'found': True if plateau was identified
    """
    t_values = np.linspace(0.01, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)

    # Estimate plateau from late-time average (last 30% of time window)
    late_start = int(0.7 * n_points)
    g_plateau = np.mean(g_values[late_start:])
    g_std = np.std(g_values[late_start:])

    # Find first time g enters the plateau band
    tol = max(plateau_window * g_plateau, g_std * 2, 0.01)
    t_H = t_max
    found = False

    # Scan from the dip forward
    dip_info = find_dip_time(shadow_coeffs, beta, t_max, n_points // 2, max_r)
    start_idx = 0
    if dip_info['found']:
        start_idx = int(dip_info['t_dip'] / t_max * n_points)

    # Check for sustained plateau: g must stay within tol of g_plateau
    # for a window of consecutive points
    window_size = max(int(0.05 * n_points), 10)
    for i in range(start_idx, n_points - window_size):
        segment = g_values[i:i + window_size]
        if np.all(np.abs(segment - g_plateau) < tol):
            t_H = t_values[i]
            found = True
            break

    return {
        't_H': float(t_H),
        'g_plateau': float(g_plateau),
        'g_std': float(g_std),
        'found': found,
    }


def measure_ramp_slope(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 100.0,
    n_points: int = 1000,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Measure the ramp slope dg/dt in the ramp region.

    The ramp region is between t_dip and t_H.
    For GUE: dg/dt = 1/t_H (linear ramp).
    For Poisson: dg/dt ~ 0 (no ramp).

    Returns dict with:
        'slope': measured slope dg/dt
        'r_squared': R^2 of linear fit in ramp region
        'has_ramp': True if slope is significantly positive
        't_dip', 't_H': dip and Heisenberg times used
    """
    t_values = np.linspace(0.01, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)

    dip = find_dip_time(shadow_coeffs, beta, t_max, n_points, max_r)
    plateau = estimate_heisenberg_time(shadow_coeffs, beta, t_max * 2,
                                       n_points * 2, max_r)

    t_dip = dip['t_dip']
    t_H = plateau['t_H']

    # Extract the ramp region
    mask = (t_values > t_dip * 1.1) & (t_values < t_H * 0.9)
    if np.sum(mask) < 5:
        return {
            'slope': 0.0,
            'r_squared': 0.0,
            'has_ramp': False,
            't_dip': t_dip,
            't_H': t_H,
        }

    t_ramp = t_values[mask]
    g_ramp = g_values[mask]

    # Linear fit
    coeffs = np.polyfit(t_ramp, g_ramp, 1)
    slope = coeffs[0]

    # R^2
    g_pred = np.polyval(coeffs, t_ramp)
    ss_res = np.sum((g_ramp - g_pred) ** 2)
    ss_tot = np.sum((g_ramp - np.mean(g_ramp)) ** 2)
    r_squared = 1.0 - ss_res / (ss_tot + 1e-30) if ss_tot > 1e-30 else 0.0

    return {
        'slope': float(slope),
        'r_squared': float(r_squared),
        'has_ramp': slope > 1e-6 and r_squared > 0.3,
        't_dip': t_dip,
        't_H': t_H,
    }


def plateau_value(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 200.0,
    n_points: int = 2000,
    max_r: Optional[int] = None,
) -> float:
    r"""Compute the late-time plateau value g_inf.

    g_inf = lim_{T->inf} (1/T) integral_0^T g(t) dt

    Approximated by averaging g over a large time window.
    For GUE: g_inf ~ 1/D where D is the effective dimension.
    """
    t_values = np.linspace(t_max * 0.5, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)
    return float(np.mean(g_values))


# ============================================================================
# 4.  SFF from pair correlation via Fourier transform
# ============================================================================

def sff_from_pair_correlation_analytic(
    t: float,
    model: str = 'gue',
) -> float:
    r"""Analytic SFF for standard random matrix models.

    For GUE with D levels:
        g_GUE(t) = |t|/D   for |t| < D
        g_GUE(t) = 1        for |t| >= D

    For Poisson (uncorrelated):
        g_Poisson(t) = 1    for all t (after dip)

    The GUE form factor is the Fourier transform of R_2^{GUE}(x) = 1 - sinc^2(pi x).

    We return the CONNECTED part (subtracting the delta function at t=0):
        b_2(t) = 1 - |t|   for |t| < 1  (GUE, normalized)
        b_2(t) = 0          for |t| >= 1

    This is the 2-point "form factor" or "spectral rigidity" kernel in the
    random matrix literature.  The ramp is the region 0 < t < 1 where
    b_2(t) = 1 - t (decreasing), meaning the SFF is g(t) = t (increasing).
    """
    t_abs = abs(t)
    if model == 'gue':
        if t_abs < 1.0:
            return t_abs  # The ramp: g(t) = t (normalized)
        else:
            return 1.0  # The plateau
    elif model == 'poisson':
        return 1.0  # Flat (no ramp)
    elif model == 'goe':
        if t_abs < 1.0:
            return 2.0 * t_abs - t_abs * math.log(1 + 2.0 * t_abs)
        else:
            return 2.0 - t_abs * math.log((2.0 * t_abs + 1) / (2.0 * t_abs - 1))
    else:
        raise ValueError(f"Unknown model: {model}")


def sff_from_pair_correlation_fft(
    R2_values: np.ndarray,
    x_values: np.ndarray,
    t_values: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute SFF from pair correlation via discrete Fourier transform.

    The SFF is the Fourier transform of the 2-point correlation function:
        g(t) = integral R_2(x) e^{i t x} dx

    More precisely, the connected SFF b_2(t) is the Fourier transform of
    the connected pair correlation 1 - R_2(x).  Since R_2 -> 1 at large x,
    the connected part decays and the FT is well-defined.

    Parameters
    ----------
    R2_values : pair correlation values on x_values grid
    x_values : x-grid points (should be uniformly spaced)
    t_values : if provided, evaluate at these t values.
               Otherwise, use FFT natural frequencies.

    Returns
    -------
    (t_out, g_out): time values and form factor values
    """
    dx = x_values[1] - x_values[0] if len(x_values) > 1 else 1.0
    N = len(R2_values)

    # Connected part: R_2^c(x) = R_2(x) - 1
    R2_connected = R2_values - 1.0

    if t_values is not None:
        # Direct numerical Fourier transform at requested t values
        g_out = np.zeros(len(t_values))
        for i, t in enumerate(t_values):
            integrand = R2_connected * np.exp(1j * t * x_values)
            g_out[i] = np.abs(np.trapezoid(integrand, x_values))
        return t_values, g_out

    # FFT path
    ft = np.fft.fft(R2_connected)
    freqs = np.fft.fftfreq(N, d=dx) * 2 * np.pi
    # Take positive frequencies only
    pos = freqs > 0
    return freqs[pos], np.abs(ft[pos]) * dx


# ============================================================================
# 5.  GUE vs Poisson classification from SFF
# ============================================================================

def classify_sff(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 100.0,
    n_points: int = 1000,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Classify the SFF as GUE-like, Poisson-like, or intermediate.

    GUE signature: clear ramp with positive slope and good linear fit.
    Poisson signature: flat or monotonically decaying after dip.

    Returns dict with:
        'class': 'GUE', 'Poisson', or 'intermediate'
        'ramp_data': output of measure_ramp_slope
        'dip_data': output of find_dip_time
        'plateau_data': output of estimate_heisenberg_time
    """
    ramp_data = measure_ramp_slope(shadow_coeffs, beta, t_max, n_points, max_r)
    dip_data = find_dip_time(shadow_coeffs, beta, t_max, n_points, max_r)
    plateau_data = estimate_heisenberg_time(shadow_coeffs, beta, t_max * 2,
                                             n_points * 2, max_r)

    if ramp_data['has_ramp'] and ramp_data['r_squared'] > 0.5:
        cls = 'GUE'
    elif ramp_data['slope'] < 1e-8:
        cls = 'Poisson'
    else:
        cls = 'intermediate'

    return {
        'class': cls,
        'ramp_data': ramp_data,
        'dip_data': dip_data,
        'plateau_data': plateau_data,
    }


# ============================================================================
# 6.  BTZ connection: form factor at Hawking temperature
# ============================================================================

def kappa_virasoro(c_val: float) -> float:
    r"""Modular characteristic kappa(Vir_c) = c/2.

    CAUTION (AP1, AP9): kappa(Vir_c) = c/2.  This is specific to Virasoro.
    For KM: kappa = dim(g)(k + h^v)/(2h^v).
    For Heisenberg: kappa = k.
    """
    return c_val / 2.0


def hawking_inverse_temperature(kappa: float) -> float:
    r"""BTZ Hawking inverse temperature beta_H = 2*pi / kappa.

    This is the AdS_3/CFT_2 dictionary identification: the inverse Hawking
    temperature of the BTZ black hole at mass ~ kappa is 2*pi/kappa.

    Requires kappa > 0.
    """
    if kappa <= 0:
        return float('inf')
    return 2.0 * math.pi / kappa


def btz_sff_at_hawking(
    shadow_coeffs: Dict[int, float],
    kappa: float,
    t_values: np.ndarray,
    max_r: Optional[int] = None,
) -> np.ndarray:
    r"""SFF at the BTZ Hawking temperature beta_H = 2*pi/kappa.

    This is the "black hole form factor" --- the SFF evaluated at the
    physically natural temperature determined by the modular characteristic.
    """
    beta_H = hawking_inverse_temperature(kappa)
    if math.isinf(beta_H):
        return np.full(len(t_values), float('nan'))
    return shadow_sff_time_series(shadow_coeffs, t_values, beta_H, max_r)


def virasoro_btz_sff(
    c_val: float,
    t_values: np.ndarray,
    max_r: int = 30,
) -> np.ndarray:
    r"""BTZ spectral form factor for Virasoro at central charge c.

    Evaluates at the Hawking temperature beta_H = 2*pi/kappa = 4*pi/c.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    kappa = kappa_virasoro(c_val)
    return btz_sff_at_hawking(coeffs, kappa, t_values, max_r)


# ============================================================================
# 7.  Late-time plateau and shadow entropy
# ============================================================================

def plateau_from_shadow_norm(
    shadow_coeffs: Dict[int, float],
    beta: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Estimate plateau from shadow coefficient norms.

    The late-time plateau g_inf relates to the "effective dimension":
        g_inf ~ sum |S_r|^2 r^{-2*beta} / (sum S_r r^{-beta})^2

    This is the participation ratio of the shadow spectrum at inverse
    temperature beta.

    For a Dirichlet series zeta_A(s) = sum S_r r^{-s}:
        <|zeta_A(beta + it)|^2>_t = sum |S_r|^2 r^{-2*beta}

    by Parseval's theorem for Dirichlet series (the off-diagonal terms
    average to zero over t).  So:

        g_inf = sum |S_r|^2 r^{-2*beta} / |zeta_A(beta)|^2
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    sum_sq = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        sum_sq += Sr ** 2 * r ** (-2 * beta)

    z_beta = shadow_zeta_numerical(shadow_coeffs, complex(beta, 0), max_r)
    norm_sq = abs(z_beta) ** 2
    if norm_sq < 1e-300:
        return float('nan')

    return sum_sq / norm_sq


def effective_dimension(
    shadow_coeffs: Dict[int, float],
    beta: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Effective dimension D_eff = 1 / g_inf.

    For GUE with D levels: D_eff = D.
    For Poisson: D_eff = 1 (trivially).

    Larger D_eff indicates more chaotic spectrum.
    """
    g_inf = plateau_from_shadow_norm(shadow_coeffs, beta, max_r)
    if g_inf <= 0 or math.isnan(g_inf):
        return float('nan')
    return 1.0 / g_inf


def shadow_entropy_from_plateau(
    shadow_coeffs: Dict[int, float],
    beta: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Shadow entropy S_sh = log(D_eff) = -log(g_inf).

    This is the shadow analogue of the Bekenstein-Hawking entropy:
        S_BH ~ -log(g_inf) at the Hawking temperature.
    """
    g_inf = plateau_from_shadow_norm(shadow_coeffs, beta, max_r)
    if g_inf <= 0 or math.isnan(g_inf):
        return float('nan')
    return -math.log(g_inf)


# ============================================================================
# 8.  Thouless time and shadow depth
# ============================================================================

def thouless_time_from_ramp(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 100.0,
    n_points: int = 1000,
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    r"""Thouless time from the ramp slope.

    t_Th = (D_eff * dg/dt)^{-1}

    For the shadow: t_Th should scale with shadow depth r_max:
        Class G: t_Th = infinity (no ramp)
        Class L: t_Th finite but large
        Class C: t_Th moderate
        Class M: t_Th ~ 1/kappa (smallest)

    Returns dict with 't_Th', 'D_eff', 'ramp_slope'.
    """
    ramp = measure_ramp_slope(shadow_coeffs, beta, t_max, n_points, max_r)
    D_eff = effective_dimension(shadow_coeffs, beta, max_r)

    slope = ramp['slope']
    if slope < 1e-12 or math.isnan(D_eff):
        return {
            't_Th': float('inf'),
            'D_eff': D_eff,
            'ramp_slope': slope,
            'has_ramp': ramp['has_ramp'],
        }

    t_Th = 1.0 / (D_eff * slope) if D_eff > 0 else float('inf')

    return {
        't_Th': float(t_Th),
        'D_eff': float(D_eff),
        'ramp_slope': float(slope),
        'has_ramp': ramp['has_ramp'],
    }


def shadow_depth_from_coeffs(
    shadow_coeffs: Dict[int, float],
    tol: float = 1e-15,
) -> int:
    r"""Shadow depth r_max from the coefficients.

    r_max is the largest r with |S_r| > tol.
    For finite towers (G/L/C): returns 2, 3, or 4.
    For infinite towers (M): returns the truncation arity.
    """
    max_r = max(shadow_coeffs.keys())
    for r in range(max_r, 1, -1):
        if abs(shadow_coeffs.get(r, 0.0)) > tol:
            return r
    return 2


# ============================================================================
# 9.  Disorder average (average over central charge)
# ============================================================================

def disorder_averaged_sff_virasoro(
    c_range: Tuple[float, float],
    n_c: int,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> np.ndarray:
    r"""Disorder-averaged SFF: <g_{Vir_c}(t, beta)>_c.

    Averages the shadow SFF over a range of central charges.
    In SYK/random matrix theory, the ramp appears after averaging
    over disorder.  The shadow analogue: "disorder" = average over c.

    Parameters
    ----------
    c_range : (c_min, c_max) for the central charge range
    n_c : number of c values to sample
    t_values : time array
    beta : inverse temperature
    max_r : truncation arity

    Returns
    -------
    Averaged g(t) array.
    """
    c_min, c_max = c_range
    c_values = np.linspace(c_min, c_max, n_c)

    g_sum = np.zeros(len(t_values))
    n_valid = 0

    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            g = shadow_sff_time_series(coeffs, t_values, beta, max_r)
            if not np.any(np.isnan(g)):
                g_sum += g
                n_valid += 1
        except (ValueError, ZeroDivisionError):
            continue

    if n_valid == 0:
        return np.full(len(t_values), float('nan'))
    return g_sum / n_valid


# ============================================================================
# 10. Slope exponent and early-time behavior
# ============================================================================

def early_time_slope_exponent(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 10.0,
    n_points: int = 500,
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    r"""Measure the early-time slope exponent alpha: g(t) ~ t^{-alpha}.

    For chaotic systems: alpha ~ 3 (slope phase).
    For integrable systems: alpha ~ 1 (or no slope).

    We fit log(g) vs log(t) in the early-time regime to extract alpha.

    Returns dict with:
        'alpha': slope exponent
        'r_squared': goodness of fit
    """
    t_values = np.linspace(0.1, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)

    # Find the slope region: g decreasing and g > 0
    # Use the first portion where g is decreasing
    mask = (g_values > 1e-10) & (g_values < 0.95)
    if np.sum(mask) < 5:
        return {'alpha': 0.0, 'r_squared': 0.0}

    t_slope = t_values[mask]
    g_slope = g_values[mask]

    log_t = np.log(t_slope)
    log_g = np.log(g_slope)

    # Linear fit: log(g) = -alpha * log(t) + const
    try:
        coeffs = np.polyfit(log_t, log_g, 1)
        alpha = -coeffs[0]
        g_pred = np.polyval(coeffs, log_t)
        ss_res = np.sum((log_g - g_pred) ** 2)
        ss_tot = np.sum((log_g - np.mean(log_g)) ** 2)
        r_squared = 1.0 - ss_res / (ss_tot + 1e-30) if ss_tot > 1e-30 else 0.0
    except (np.linalg.LinAlgError, FloatingPointError):
        alpha = 0.0
        r_squared = 0.0

    return {
        'alpha': float(alpha),
        'r_squared': float(r_squared),
    }


# ============================================================================
# 11. Heisenberg time from mean level spacing
# ============================================================================

def heisenberg_time_from_spacing(mean_spacing: float) -> float:
    r"""Heisenberg time t_H = 2*pi / Delta.

    Delta = mean level spacing of shadow zeros.
    t_H = 2*pi/Delta is the time at which the form factor transitions
    from ramp to plateau.
    """
    if mean_spacing <= 0:
        return float('inf')
    return 2.0 * math.pi / mean_spacing


def mean_level_spacing_from_shadow_zeros(
    zeros: np.ndarray,
) -> float:
    r"""Mean level spacing from an array of shadow zero heights.

    Delta = mean(t_{n+1} - t_n) where t_n are sorted zero heights.
    """
    if len(zeros) < 2:
        return float('inf')
    sorted_zeros = np.sort(zeros)
    spacings = np.diff(sorted_zeros)
    return float(np.mean(spacings))


# ============================================================================
# 12. Plateau beta-independence check
# ============================================================================

def plateau_beta_independence(
    shadow_coeffs: Dict[int, float],
    beta_values: List[float],
    t_max: float = 200.0,
    n_points: int = 1000,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Check that the plateau value is independent of beta (for beta large).

    For sufficiently large beta, the plateau g_inf should converge to a
    beta-independent value (determined by the spectral statistics).

    Returns dict with:
        'plateaus': list of (beta, g_inf) pairs
        'variation': max - min of plateau values
        'mean_plateau': mean plateau value
    """
    plateaus = []
    for beta in beta_values:
        g_inf = plateau_from_shadow_norm(shadow_coeffs, beta, max_r)
        plateaus.append((beta, g_inf))

    values = [v for _, v in plateaus if not math.isnan(v)]
    if not values:
        return {
            'plateaus': plateaus,
            'variation': float('nan'),
            'mean_plateau': float('nan'),
        }

    return {
        'plateaus': plateaus,
        'variation': max(values) - min(values),
        'mean_plateau': np.mean(values),
    }


# ============================================================================
# 13. Full form factor report
# ============================================================================

def full_sff_report(
    shadow_coeffs: Dict[int, float],
    beta: float,
    kappa: float,
    family_name: str = 'unknown',
    t_max: float = 100.0,
    n_points: int = 500,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Full spectral form factor report for a modular Koszul algebra.

    Returns comprehensive dictionary with all SFF diagnostics.
    """
    # Basic data
    g0 = shadow_sff_direct(shadow_coeffs, 0.0, beta, max_r)
    depth = shadow_depth_from_coeffs(shadow_coeffs)

    # Dip
    dip = find_dip_time(shadow_coeffs, beta, t_max, n_points, max_r)

    # Plateau
    g_inf = plateau_from_shadow_norm(shadow_coeffs, beta, max_r)
    D_eff = effective_dimension(shadow_coeffs, beta, max_r)
    S_sh = shadow_entropy_from_plateau(shadow_coeffs, beta, max_r)

    # Ramp
    ramp = measure_ramp_slope(shadow_coeffs, beta, t_max, n_points, max_r)

    # Classification
    classification = classify_sff(shadow_coeffs, beta, t_max, n_points, max_r)

    return {
        'family': family_name,
        'beta': beta,
        'kappa': kappa,
        'shadow_depth': depth,
        'g_at_0': g0,
        'normalization_error': abs(g0 - 1.0),
        'dip_time': dip['t_dip'],
        'dip_value': dip['g_dip'],
        'plateau_value': g_inf,
        'effective_dimension': D_eff,
        'shadow_entropy': S_sh,
        'ramp_slope': ramp['slope'],
        'ramp_r_squared': ramp['r_squared'],
        'has_ramp': ramp['has_ramp'],
        'classification': classification['class'],
    }


# ============================================================================
# 14. Family-specific convenience functions
# ============================================================================

def heisenberg_sff(
    k_val: float,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> np.ndarray:
    """SFF for Heisenberg H_k (class G, depth 2)."""
    coeffs = heisenberg_shadow_coefficients(k_val, max_r)
    return shadow_sff_time_series(coeffs, t_values, beta, max_r)


def affine_sl2_sff(
    k_val: float,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> np.ndarray:
    """SFF for affine V_k(sl_2) (class L, depth 3)."""
    coeffs = affine_sl2_shadow_coefficients(k_val, max_r)
    return shadow_sff_time_series(coeffs, t_values, beta, max_r)


def betagamma_sff(
    lam_val: float,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> np.ndarray:
    """SFF for beta-gamma at weight lambda (class C, depth 4)."""
    coeffs = betagamma_shadow_coefficients(lam_val, max_r)
    return shadow_sff_time_series(coeffs, t_values, beta, max_r)


# ============================================================================
# 15. Cross-verification: SFF monotonicity and bounds
# ============================================================================

def verify_sff_bounds(
    shadow_coeffs: Dict[int, float],
    beta: float,
    t_max: float = 50.0,
    n_points: int = 200,
    max_r: Optional[int] = None,
) -> Dict[str, bool]:
    r"""Verify basic SFF bounds:

    1. g_A(t, beta) >= 0 for all t (it's |z|^2 / |z_0|^2).
    2. g_A(0, beta) = 1 (normalization).
    3. g_A(t, beta) <= D_eff for all t (bounded by effective dimension).
       Actually g can exceed D_eff temporarily, so we check a weaker bound.

    Returns dict of boolean test results.
    """
    t_values = np.linspace(0, t_max, n_points)
    g_values = shadow_sff_time_series(shadow_coeffs, t_values, beta, max_r)

    return {
        'nonnegative': bool(np.all(g_values >= -1e-10)),
        'normalized': bool(abs(g_values[0] - 1.0) < 1e-10),
        'finite': bool(np.all(np.isfinite(g_values))),
    }


# ============================================================================
# 16. Koszul complementarity on SFF
# ============================================================================

def koszul_dual_sff_virasoro(
    c_val: float,
    t_values: np.ndarray,
    beta: float,
    max_r: int = 30,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""SFF for Virasoro and its Koszul dual Vir_{26-c}.

    Koszul duality: Vir_c^! = Vir_{26-c}.
    kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
    kappa + kappa' = 13 (NOT zero; AP24).

    Returns (g_A, g_A!) evaluated at the same (t, beta).
    """
    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    g_A = shadow_sff_time_series(coeffs_A, t_values, beta, max_r)
    g_dual = shadow_sff_time_series(coeffs_dual, t_values, beta, max_r)

    return g_A, g_dual


def complementarity_plateau_sum(
    c_val: float,
    beta: float,
    max_r: int = 30,
) -> float:
    r"""Sum of plateau entropies: S_sh(A) + S_sh(A!).

    For Koszul pairs, we expect structural relations between the
    SFF of A and A!.  The entropy sum S_sh(A) + S_sh(A!) should
    exhibit constraints from Theorem C (complementarity).
    """
    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)

    S_A = shadow_entropy_from_plateau(coeffs_A, beta, max_r)
    S_dual = shadow_entropy_from_plateau(coeffs_dual, beta, max_r)

    if math.isnan(S_A) or math.isnan(S_dual):
        return float('nan')
    return S_A + S_dual
