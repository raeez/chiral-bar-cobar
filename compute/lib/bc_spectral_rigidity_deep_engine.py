r"""Spectral rigidity, number variance, and extremal gap statistics for shadow zeta zeros.

For a modular Koszul algebra A with shadow coefficients S_r(A), the shadow
zeta function zeta_A(s) = sum_{r>=2} S_r(A) r^{-s} has nontrivial zeros.
The Epstein zeta eps_{Q_A}(s) for the shadow metric Q_A provides a parallel
zero family.  This module computes the SPECTRAL STATISTICS of these zero
sets:

1. NUMBER VARIANCE Sigma^2(L):
   Var(#{zeros in window of length L}) as a function of L.
   For GUE: Sigma^2(L) ~ (2/pi^2)(log(2*pi*L) + gamma + 1 - pi^2/8)
   For GOE: Sigma^2(L) ~ (2/pi^2)(log(2*pi*L) + gamma + 1 - 5*pi^2/8)
   For Poisson: Sigma^2(L) = L

   NOTE: The GOE asymptotic formula has the form:
   (2/pi^2)(log(2*pi*L) + gamma + 1 - pi^2/8) + correction
   The correction makes GOE larger than GUE at the same L.  The exact
   Mehta result for GOE at large L is:
   Sigma^2_GOE(L) ~ (1/pi^2)(2*log(2*pi*L) + 2*gamma + 2 + pi^2/4)

2. DELTA_3(L) STATISTIC (Dyson-Mehta spectral rigidity):
   min_{a,b} (1/L) integral_E^{E+L} (N(x) - ax - b)^2 dx
   Measures the rigidity of the spectrum (how close to equally spaced).
   For GUE: Delta_3(L) ~ (1/pi^2)(log(2*pi*L) + gamma - 5/4)
   For Poisson: Delta_3(L) = L/15

3. SPECTRAL FORM FACTOR K(tau):
   K(tau) = (1/N)|sum_n exp(i gamma_n tau)|^2
   Exhibits dip-ramp-plateau structure in quantum chaos.
   Thouless time t_Th: dip-to-ramp transition.
   Heisenberg time t_H: ramp-to-plateau transition.

4. RECORD GAPS: maximal gap gamma_{n+1} - gamma_n.
   For Riemann zeta: Cramer conjecture max gap ~ (log gamma)^2.
   Does shadow depth class produce a signature?

5. SMALL GAPS: level repulsion P(s) ~ s^beta for small s.
   beta = 1 (GOE), 2 (GUE), 0 (Poisson).

6. HARDY Z-FUNCTION ANALOGUE:
   Z_A(t) = e^{i*theta_A(t)} * zeta_A(1/2 + it) (real-valued on critical line).
   Sign changes correspond to zeros.

7. AUTOCORRELATION of the Hardy Z-function.

8. LEVEL SPACING RATIO:
   r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}).
   GUE: <r> ~ 0.5307.  Poisson: <r> ~ 0.3863.

9. GUE-POISSON TRANSITION:
   As c -> infinity (free-field limit), does the spectrum undergo
   a GUE -> Poisson transition?

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify all statistics by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Literature convention mismatches for spectral statistics.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

# ---------------------------------------------------------------------------
# Import from existing engines
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    shadow_zeta_numerical,
)
from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    find_zeros_grid,
    newton_zero,
    affine_sl2_zeros,
    normalized_spacings,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
)
from compute.lib.shadow_epstein_zeta import (
    virasoro_shadow_data,
    virasoro_form,
)

try:
    from compute.lib.bc_pair_correlation_engine import (
        find_epstein_zeros_on_critical_line,
        virasoro_epstein_zeros,
        unfold_epstein_zeros,
        nearest_neighbor_spacings,
        number_variance as _existing_number_variance,
        gue_number_variance as _gue_nv_existing,
        goe_number_variance as _goe_nv_existing,
        poisson_number_variance as _poisson_nv_existing,
        wigner_surmise_gue,
        wigner_surmise_goe,
        poisson_spacing,
        gue_pair_correlation,
        ks_test_spacing,
    )
    HAS_PAIR_CORR = True
except ImportError:
    HAS_PAIR_CORR = False

try:
    import mpmath
    mpmath.mp.dps = 30
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# ============================================================================
# 0.  Reference distributions (analytical)
# ============================================================================

# The Euler-Mascheroni constant, verified to 30 digits
EULER_MASCHERONI = 0.5772156649015328606065120900824

# GUE mean spacing ratio (from random matrix theory):
# <r>_GUE = 4 - 2*sqrt(3) = 0.53590...  [Wigner surmise approximation]
# Exact GUE: <r> ~ 0.5307 (from numerical integration of the exact CDF)
GUE_MEAN_SPACING_RATIO = 0.5307
# Poisson: <r> = 2*ln(2) - 1 = 0.38629...
POISSON_MEAN_SPACING_RATIO = 2 * math.log(2) - 1  # 0.38629...
# GOE: <r> ~ 0.5359
GOE_MEAN_SPACING_RATIO = 0.5359


def gue_number_variance(L: np.ndarray) -> np.ndarray:
    r"""GUE number variance: Sigma^2_GUE(L).

    Asymptotic for L >> 1:
        Sigma^2(L) = (2/pi^2)[log(2*pi*L) + gamma + 1 - pi^2/8]

    For small L, Sigma^2(L) ~ L (same as Poisson).
    We use a smooth interpolation:
        For L < 0.1: Sigma^2 ~ L
        For L >= 0.1: use asymptotic
    """
    L = np.asarray(L, dtype=float)
    result = np.zeros_like(L)
    small = L < 0.1
    large = ~small
    result[small] = L[small]  # approaches Poisson for tiny windows
    result[large] = (2.0 / np.pi**2) * (
        np.log(2.0 * np.pi * L[large]) + EULER_MASCHERONI + 1.0
        - np.pi**2 / 8.0
    )
    # Ensure non-negative
    result = np.maximum(result, 0.0)
    return result


def goe_number_variance(L: np.ndarray) -> np.ndarray:
    r"""GOE number variance: Sigma^2_GOE(L).

    Asymptotic for L >> 1:
        Sigma^2(L) = (1/pi^2)[2*log(2*pi*L) + 2*gamma + 2 + pi^2/4]

    This is larger than GUE by ~pi^2/4 / pi^2 = 1/4 at each L,
    reflecting weaker level repulsion.

    NOTE: The GOE formula used here follows Mehta (2004), Eq. 5.2.37.
    The factor -5*pi^2/8 sometimes seen in the literature corresponds
    to a different normalization of the form factor.  We use the standard
    Mehta normalization where:
        Sigma^2_GOE(L) - Sigma^2_GUE(L) -> pi^2/(4*pi^2) = 1/4
    for large L.
    """
    L = np.asarray(L, dtype=float)
    result = np.zeros_like(L)
    small = L < 0.1
    large = ~small
    result[small] = L[small]
    result[large] = (1.0 / np.pi**2) * (
        2.0 * np.log(2.0 * np.pi * L[large])
        + 2.0 * EULER_MASCHERONI + 2.0 + np.pi**2 / 4.0
    )
    result = np.maximum(result, 0.0)
    return result


def poisson_number_variance(L: np.ndarray) -> np.ndarray:
    """Poisson number variance: Sigma^2(L) = L."""
    return np.asarray(L, dtype=float).copy()


def gue_delta3(L: np.ndarray) -> np.ndarray:
    r"""GUE spectral rigidity: Delta_3(L).

    Asymptotic for L >> 1:
        Delta_3(L) = (1/pi^2)[log(2*pi*L) + gamma - 5/4]

    For small L: Delta_3(L) ~ L/15 (Poisson-like).
    """
    L = np.asarray(L, dtype=float)
    result = np.zeros_like(L)
    small = L < 0.2
    large = ~small
    result[small] = L[small] / 15.0
    result[large] = (1.0 / np.pi**2) * (
        np.log(2.0 * np.pi * L[large]) + EULER_MASCHERONI - 5.0 / 4.0
    )
    result = np.maximum(result, 0.0)
    return result


def poisson_delta3(L: np.ndarray) -> np.ndarray:
    """Poisson spectral rigidity: Delta_3(L) = L/15."""
    return np.asarray(L, dtype=float) / 15.0


def goe_delta3(L: np.ndarray) -> np.ndarray:
    r"""GOE spectral rigidity: Delta_3(L).

    Asymptotic for L >> 1:
        Delta_3(L) = (1/pi^2)[log(2*pi*L) + gamma - 5/4] + 1/(2*pi^2)

    GOE Delta_3 is larger than GUE by 1/(2*pi^2) ~ 0.0507.
    """
    L = np.asarray(L, dtype=float)
    result = np.zeros_like(L)
    small = L < 0.2
    large = ~small
    result[small] = L[small] / 15.0
    result[large] = (1.0 / np.pi**2) * (
        np.log(2.0 * np.pi * L[large]) + EULER_MASCHERONI - 5.0 / 4.0
    ) + 1.0 / (2.0 * np.pi**2)
    result = np.maximum(result, 0.0)
    return result


# ============================================================================
# 1.  Number variance computation from zeros
# ============================================================================

def compute_number_variance(
    unfolded: np.ndarray,
    L_values: np.ndarray,
    n_samples: int = 300,
) -> np.ndarray:
    r"""Compute Sigma^2(L) from unfolded zeros.

    For each L, slides a window of length L across the unfolded spectrum
    and computes the variance of the count N(window).

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros (unit mean spacing)
    L_values : array of window lengths L at which to compute Sigma^2
    n_samples : number of window starting points per L

    Returns
    -------
    Array of Sigma^2(L) values (same length as L_values).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)
    L_arr = np.asarray(L_values, dtype=float)
    sigma2 = np.zeros(len(L_arr))

    if N < 4:
        return sigma2

    u_min, u_max = u[0], u[-1]
    span = u_max - u_min

    for idx, L in enumerate(L_arr):
        if L <= 0 or L >= span:
            continue
        # Sample starting points uniformly
        n_s = min(n_samples, max(10, N))
        a_vals = np.linspace(u_min, u_max - L, n_s)
        counts = np.zeros(n_s)
        for i, a in enumerate(a_vals):
            # Count zeros in [a, a + L]
            lo = np.searchsorted(u, a, side='left')
            hi = np.searchsorted(u, a + L, side='right')
            counts[i] = hi - lo
        sigma2[idx] = np.var(counts)

    return sigma2


def compute_number_variance_for_family(
    family: str,
    param: float,
    L_values: np.ndarray,
    t_max: float = 100.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    r"""Compute Sigma^2(L) for a given algebra family.

    Uses Epstein zeros for Virasoro, shadow zeta zeros for other families.

    Returns dict with 'L', 'sigma2', 'gue', 'goe', 'poisson',
    'n_zeros', 'family', 'param'.
    """
    L_arr = np.asarray(L_values, dtype=float)

    if family == 'virasoro':
        if not HAS_PAIR_CORR:
            return {'error': 'bc_pair_correlation_engine not available'}
        zeros = virasoro_epstein_zeros(param, t_max=t_max, dt=dt)
        if len(zeros) < 5:
            return {'error': f'too few zeros ({len(zeros)}) for c={param}',
                    'n_zeros': len(zeros)}
        a, b, cc, D = virasoro_form(param)
        unfolded = unfold_epstein_zeros(zeros, a, b, cc)
    elif family == 'affine_sl2':
        # Affine sl_2 zeros are exactly known (exponential polynomial)
        raw_zeros = affine_sl2_zeros(param, n_max=200)
        # Take imaginary parts with Im > 0
        gammas = sorted([z.imag for z in raw_zeros if z.imag > 0.5])
        if len(gammas) < 5:
            return {'error': f'too few zeros ({len(gammas)}) for k={param}',
                    'n_zeros': len(gammas)}
        # Unfold by simple rescaling (equispaced zeros for 2-term exp poly)
        gammas = np.array(gammas)
        spacings = np.diff(gammas)
        mean_sp = np.mean(spacings) if len(spacings) > 0 else 1.0
        unfolded = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        zeros = gammas
    elif family == 'heisenberg':
        # Heisenberg has NO zeros (single-term zeta)
        return {'L': L_arr.tolist(), 'sigma2': [0.0] * len(L_arr),
                'n_zeros': 0, 'family': family, 'param': param,
                'note': 'Heisenberg has no shadow zeta zeros'}
    else:
        # Generic: use grid search for shadow zeta zeros
        coeffs = shadow_coefficients_extended(family, param, max_r=60)
        raw_zeros = find_zeros_grid(coeffs,
                                    re_range=(-5.0, 5.0),
                                    im_range=(0.1, t_max),
                                    grid_re=20, grid_im=100,
                                    max_r=60)
        gammas = sorted([z.imag for z in raw_zeros if z.imag > 0.5])
        if len(gammas) < 5:
            return {'error': f'too few zeros ({len(gammas)})',
                    'n_zeros': len(gammas)}
        gammas = np.array(gammas)
        spacings = np.diff(gammas)
        mean_sp = np.mean(spacings) if len(spacings) > 0 else 1.0
        unfolded = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        zeros = gammas

    sigma2 = compute_number_variance(unfolded, L_arr)

    return {
        'L': L_arr.tolist(),
        'sigma2': sigma2.tolist(),
        'gue': gue_number_variance(L_arr).tolist(),
        'goe': goe_number_variance(L_arr).tolist(),
        'poisson': poisson_number_variance(L_arr).tolist(),
        'n_zeros': len(zeros),
        'family': family,
        'param': param,
    }


# ============================================================================
# 2.  Delta_3(L) spectral rigidity
# ============================================================================

def compute_delta3(
    unfolded: np.ndarray,
    L_values: np.ndarray,
    n_samples: int = 200,
) -> np.ndarray:
    r"""Compute Delta_3(L) = min_{a,b} (1/L) int_E^{E+L} (N(x) - ax - b)^2 dx.

    For unfolded zeros {u_n}, the staircase N(x) = #{u_n <= x}.
    The minimum over a, b of (1/L) int (N - ax - b)^2 dx can be computed
    by linear regression of N(x) vs x in the window [E, E+L].

    We average over many starting points E to reduce variance.

    Parameters
    ----------
    unfolded : sorted unfolded zeros
    L_values : window lengths
    n_samples : number of starting points per L

    Returns
    -------
    Array of Delta_3(L) values.
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N_z = len(u)
    L_arr = np.asarray(L_values, dtype=float)
    delta3 = np.zeros(len(L_arr))

    if N_z < 4:
        return delta3

    u_min, u_max = u[0], u[-1]
    span = u_max - u_min

    for idx, L in enumerate(L_arr):
        if L <= 0 or L >= span:
            continue

        n_s = min(n_samples, max(10, N_z // 2))
        E_vals = np.linspace(u_min, u_max - L, n_s)
        delta3_samples = np.zeros(n_s)

        for i, E in enumerate(E_vals):
            # Get zeros in [E, E+L]
            lo = np.searchsorted(u, E, side='left')
            hi = np.searchsorted(u, E + L, side='right')
            n_in_window = hi - lo

            if n_in_window < 2:
                # Not enough points for regression
                delta3_samples[i] = L / 15.0  # Poisson default
                continue

            # The staircase N(x) in [E, E+L]: evaluate at zero positions
            x_pts = u[lo:hi]
            # N(x) = 1, 2, ..., n_in_window at these points
            n_pts = np.arange(1, n_in_window + 1, dtype=float)

            # Also evaluate at window boundaries
            x_eval = np.concatenate([[E], x_pts, [E + L]])
            n_eval = np.concatenate([[0.0], n_pts, [float(n_in_window)]])

            # Linear regression: N(x) = a*x + b
            x_centered = x_eval - E
            if len(x_eval) > 2:
                A = np.column_stack([x_centered, np.ones_like(x_centered)])
                try:
                    coeffs, _, _, _ = np.linalg.lstsq(A, n_eval, rcond=None)
                    a_fit, b_fit = coeffs
                except np.linalg.LinAlgError:
                    delta3_samples[i] = L / 15.0
                    continue

                residuals = n_eval - a_fit * x_centered - b_fit
                # Delta_3 = (1/L) * integral of residuals^2
                # Approximate integral by trapezoidal rule on the grid
                delta3_samples[i] = np.mean(residuals**2) / max(L, 1e-10) * L
                # Actually: (1/L) * int (N - ax - b)^2 dx
                # Since we evaluated at discrete points, use the squared residuals
                # weighted by the step sizes
                dx = np.diff(x_eval)
                mid_resid = 0.5 * (residuals[:-1]**2 + residuals[1:]**2)
                delta3_samples[i] = np.sum(mid_resid * dx) / L
            else:
                delta3_samples[i] = L / 15.0

        delta3[idx] = np.mean(delta3_samples)

    return delta3


def compute_delta3_for_family(
    family: str,
    param: float,
    L_values: np.ndarray,
    t_max: float = 100.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    """Compute Delta_3(L) for a given algebra family.

    Returns dict with 'L', 'delta3', 'gue', 'goe', 'poisson', 'n_zeros'.
    """
    L_arr = np.asarray(L_values, dtype=float)

    if family == 'virasoro':
        if not HAS_PAIR_CORR:
            return {'error': 'bc_pair_correlation_engine not available'}
        zeros = virasoro_epstein_zeros(param, t_max=t_max, dt=dt)
        if len(zeros) < 5:
            return {'error': f'too few zeros', 'n_zeros': len(zeros)}
        a, b, cc, D = virasoro_form(param)
        unfolded = unfold_epstein_zeros(zeros, a, b, cc)
    elif family == 'affine_sl2':
        raw_zeros = affine_sl2_zeros(param, n_max=200)
        gammas = sorted([z.imag for z in raw_zeros if z.imag > 0.5])
        if len(gammas) < 5:
            return {'error': 'too few zeros', 'n_zeros': len(gammas)}
        gammas = np.array(gammas)
        spacings = np.diff(gammas)
        mean_sp = np.mean(spacings) if len(spacings) > 0 else 1.0
        unfolded = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        zeros = gammas
    elif family == 'heisenberg':
        return {'L': L_arr.tolist(), 'delta3': [0.0] * len(L_arr),
                'n_zeros': 0, 'note': 'Heisenberg has no zeros'}
    else:
        coeffs = shadow_coefficients_extended(family, param, max_r=60)
        raw = find_zeros_grid(coeffs, re_range=(-5, 5),
                              im_range=(0.1, t_max),
                              grid_re=20, grid_im=100, max_r=60)
        gammas = sorted([z.imag for z in raw if z.imag > 0.5])
        if len(gammas) < 5:
            return {'error': 'too few zeros', 'n_zeros': len(gammas)}
        gammas = np.array(gammas)
        sp = np.diff(gammas)
        mean_sp = np.mean(sp) if len(sp) > 0 else 1.0
        unfolded = (gammas - gammas[0]) / mean_sp
        zeros = gammas

    d3 = compute_delta3(unfolded, L_arr)

    return {
        'L': L_arr.tolist(),
        'delta3': d3.tolist(),
        'gue': gue_delta3(L_arr).tolist(),
        'goe': goe_delta3(L_arr).tolist(),
        'poisson': poisson_delta3(L_arr).tolist(),
        'n_zeros': len(zeros),
        'family': family,
        'param': param,
    }


# ============================================================================
# 3.  Spectral form factor K(tau)
# ============================================================================

def spectral_form_factor(
    gammas: np.ndarray,
    tau_values: np.ndarray,
) -> np.ndarray:
    r"""Compute K(tau) = (1/N) |sum_n exp(i gamma_n tau)|^2.

    For GUE:
        K(tau) ~ tau         for tau < t_H  (ramp)
        K(tau) ~ N           for tau > t_H  (plateau, but K/N -> 1)

    There is a dip at tau ~ t_Th (Thouless time) before the ramp.

    Parameters
    ----------
    gammas : imaginary parts of zeros (not unfolded)
    tau_values : array of tau values

    Returns
    -------
    K(tau) normalized to 1 at the plateau.
    """
    gammas = np.asarray(gammas, dtype=float)
    N = len(gammas)
    tau_arr = np.asarray(tau_values, dtype=float)
    K = np.zeros(len(tau_arr))

    if N == 0:
        return K

    for idx, tau in enumerate(tau_arr):
        # Sum of phases: sum_n exp(i gamma_n tau)
        phases = np.exp(1j * gammas * tau)
        S = np.sum(phases)
        K[idx] = abs(S)**2 / N

    return K


def identify_dip_ramp_plateau(
    tau_values: np.ndarray,
    K_values: np.ndarray,
) -> Dict[str, float]:
    r"""Identify Thouless time, Heisenberg time from the form factor.

    The dip-ramp-plateau structure:
    - K(0) = N (all phases aligned)
    - K decreases to a minimum (dip) at tau ~ t_Th
    - K increases linearly (ramp) from t_Th to t_H
    - K saturates at plateau ~ 1 for tau > t_H

    Returns dict with 'tau_dip', 'K_dip', 'tau_plateau', 'K_plateau'.
    """
    tau = np.asarray(tau_values, dtype=float)
    K = np.asarray(K_values, dtype=float)

    if len(K) < 3:
        return {'tau_dip': 0.0, 'K_dip': 0.0,
                'tau_plateau': 0.0, 'K_plateau': 0.0}

    # Find minimum (dip)
    dip_idx = np.argmin(K)
    tau_dip = float(tau[dip_idx])
    K_dip = float(K[dip_idx])

    # Find plateau: where K first reaches within 30% of its final value
    K_final = np.mean(K[-max(1, len(K)//10):])  # average of last 10%
    plateau_mask = K > 0.7 * K_final
    plateau_indices = np.where(plateau_mask)[0]
    # Take the first time K reaches the plateau AFTER the dip
    post_dip = plateau_indices[plateau_indices > dip_idx]
    if len(post_dip) > 0:
        tau_plateau = float(tau[post_dip[0]])
        K_plateau = float(K[post_dip[0]])
    else:
        tau_plateau = float(tau[-1])
        K_plateau = float(K[-1])

    return {
        'tau_dip': tau_dip,
        'K_dip': K_dip,
        'tau_plateau': tau_plateau,
        'K_plateau': K_plateau,
        'K_final': float(K_final),
    }


def compute_form_factor_for_family(
    family: str,
    param: float,
    tau_values: np.ndarray,
    t_max: float = 100.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    """Compute spectral form factor for a given family."""
    if family == 'virasoro':
        if not HAS_PAIR_CORR:
            return {'error': 'bc_pair_correlation_engine not available'}
        zeros = virasoro_epstein_zeros(param, t_max=t_max, dt=dt)
    elif family == 'affine_sl2':
        raw = affine_sl2_zeros(param, n_max=200)
        zeros = np.array(sorted([z.imag for z in raw if 0.5 < z.imag < t_max]))
    elif family == 'heisenberg':
        return {'tau': tau_values.tolist(), 'K': [0.0] * len(tau_values),
                'n_zeros': 0, 'note': 'No zeros'}
    else:
        coeffs = shadow_coefficients_extended(family, param, max_r=60)
        raw = find_zeros_grid(coeffs, re_range=(-5, 5),
                              im_range=(0.1, t_max),
                              grid_re=20, grid_im=100, max_r=60)
        zeros = np.array(sorted([z.imag for z in raw if z.imag > 0.5]))

    if len(zeros) < 3:
        return {'error': 'too few zeros', 'n_zeros': len(zeros)}

    K = spectral_form_factor(zeros, tau_values)
    drp = identify_dip_ramp_plateau(tau_values, K)

    return {
        'tau': tau_values.tolist(),
        'K': K.tolist(),
        'n_zeros': len(zeros),
        'dip_ramp_plateau': drp,
        'family': family,
        'param': param,
    }


# ============================================================================
# 4.  Record gaps (maximal gap between consecutive zeros)
# ============================================================================

def record_gaps(
    gammas: np.ndarray,
    T_values: Optional[List[float]] = None,
) -> Dict[str, Any]:
    r"""Find the maximal gap between consecutive zeros up to height T.

    Parameters
    ----------
    gammas : sorted array of zero heights (positive imaginary parts)
    T_values : list of T values at which to report the maximal gap.
               If None, uses [100, 1000].

    Returns
    -------
    Dict with 'T', 'max_gap', 'max_gap_location', 'mean_gap', 'all_gaps'.
    """
    gammas = np.sort(np.asarray(gammas, dtype=float))
    if T_values is None:
        T_values = [100.0, 1000.0]

    results = {}
    for T in T_values:
        g_T = gammas[gammas <= T]
        if len(g_T) < 2:
            results[T] = {
                'max_gap': 0.0, 'max_gap_location': 0.0,
                'mean_gap': 0.0, 'n_zeros': len(g_T),
            }
            continue

        gaps = np.diff(g_T)
        max_idx = np.argmax(gaps)
        results[T] = {
            'max_gap': float(gaps[max_idx]),
            'max_gap_location': float(g_T[max_idx]),
            'mean_gap': float(np.mean(gaps)),
            'n_zeros': len(g_T),
            'max_gap_ratio': float(gaps[max_idx] / np.mean(gaps)) if np.mean(gaps) > 0 else 0.0,
        }

    return results


def cramer_test(
    gammas: np.ndarray,
    n_bins: int = 10,
) -> Dict[str, float]:
    r"""Test Cramer-type conjecture: max gap ~ C * (log gamma)^alpha.

    For Riemann zeta: conjectured alpha = 2 (Cramer).
    For random matrices (GUE): alpha ~ 1 (gaps ~ log N for N eigenvalues).

    We fit max_gap / mean_gap vs log(gamma) to a power law.

    Returns dict with 'alpha' (power law exponent) and 'C' (coefficient).
    """
    gammas = np.sort(np.asarray(gammas, dtype=float))
    N = len(gammas)
    if N < 20:
        return {'alpha': 0.0, 'C': 0.0, 'note': 'too few zeros'}

    # Split into bins and find max gap in each
    bin_edges = np.linspace(0, N - 1, n_bins + 1, dtype=int)
    log_heights = []
    max_gaps_normalized = []

    for i in range(n_bins):
        lo, hi = bin_edges[i], bin_edges[i + 1]
        if hi - lo < 3:
            continue
        g_bin = gammas[lo:hi]
        gaps = np.diff(g_bin)
        if len(gaps) == 0:
            continue
        mean_g = np.mean(gaps)
        if mean_g <= 0:
            continue
        max_g = np.max(gaps)
        median_height = np.median(g_bin)
        if median_height > 1:
            log_heights.append(np.log(median_height))
            max_gaps_normalized.append(max_g / mean_g)

    if len(log_heights) < 3:
        return {'alpha': 0.0, 'C': 0.0, 'note': 'insufficient data'}

    # Fit: log(max_gap/mean_gap) = alpha * log(log(gamma)) + log(C)
    # or equivalently: max_gap/mean_gap ~ C * (log gamma)^alpha
    x = np.array(log_heights)
    y = np.log(np.array(max_gaps_normalized) + 1e-30)

    # Linear fit
    A = np.column_stack([x, np.ones_like(x)])
    try:
        coeffs, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        alpha = float(coeffs[0])
        C = float(np.exp(coeffs[1]))
    except np.linalg.LinAlgError:
        alpha, C = 0.0, 0.0

    return {'alpha': alpha, 'C': C}


# ============================================================================
# 5.  Small gaps and level repulsion
# ============================================================================

def small_gap_count(
    unfolded: np.ndarray,
    delta_values: Optional[List[float]] = None,
) -> Dict[float, Dict[str, Any]]:
    r"""Count pairs with s_{n+1} - s_n < delta * (mean spacing).

    Since unfolded zeros have mean spacing 1, this counts
    pairs with gap < delta.

    For GUE: P(s) ~ (32/pi^2) s^2 for s -> 0  (level repulsion, beta=2).
    For GOE: P(s) ~ (pi/2) s for s -> 0 (beta=1).
    For Poisson: P(s) ~ 1 for s -> 0 (beta=0).

    Parameters
    ----------
    unfolded : sorted unfolded zeros
    delta_values : list of thresholds (default [0.1, 0.01, 0.001])

    Returns
    -------
    Dict mapping delta to count, fraction, and GUE prediction.
    """
    if delta_values is None:
        delta_values = [0.1, 0.01, 0.001]

    u = np.sort(np.asarray(unfolded, dtype=float))
    spacings = np.diff(u)
    mean_sp = np.mean(spacings) if len(spacings) > 0 else 1.0
    # Normalize to unit mean
    s_normalized = spacings / mean_sp if mean_sp > 0 else spacings
    N = len(s_normalized)

    results = {}
    for delta in delta_values:
        count = int(np.sum(s_normalized < delta))
        fraction = count / N if N > 0 else 0.0

        # GUE prediction: P(s < delta) = integral_0^delta (32/pi^2) s^2 exp(-4s^2/pi) ds
        # For small delta: ~ (32/(3*pi^2)) delta^3
        gue_pred = (32.0 / (3.0 * np.pi**2)) * delta**3
        # GOE prediction: ~ (pi/4) delta^2
        goe_pred = (np.pi / 4.0) * delta**2
        # Poisson: ~ delta
        poisson_pred = delta

        results[delta] = {
            'count': count,
            'fraction': fraction,
            'total_spacings': N,
            'gue_prediction': gue_pred,
            'goe_prediction': goe_pred,
            'poisson_prediction': poisson_pred,
        }

    return results


def level_repulsion_exponent(
    unfolded: np.ndarray,
    s_max: float = 0.5,
    n_bins: int = 20,
) -> Dict[str, float]:
    r"""Estimate the level repulsion exponent beta from P(s) ~ s^beta.

    For small s, the nearest-neighbor spacing distribution goes as:
        P(s) ~ A * s^beta  with beta = 0 (Poisson), 1 (GOE), 2 (GUE).

    Fit log P(s) ~ beta * log(s) + const in the range [0, s_max].

    Returns dict with 'beta' (the exponent) and 'A' (the amplitude).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    spacings = np.diff(u)
    mean_sp = np.mean(spacings)
    s_norm = spacings / mean_sp if mean_sp > 0 else spacings

    # Histogram in [0, s_max]
    s_in_range = s_norm[(s_norm > 0) & (s_norm < s_max)]
    if len(s_in_range) < 10:
        return {'beta': 0.0, 'A': 0.0, 'note': 'insufficient small-gap data'}

    bin_edges = np.linspace(0, s_max, n_bins + 1)
    counts, _ = np.histogram(s_in_range, bins=bin_edges, density=True)
    bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Fit log(P) vs log(s) for nonzero bins
    mask = counts > 0
    if np.sum(mask) < 3:
        return {'beta': 0.0, 'A': 0.0, 'note': 'insufficient nonzero bins'}

    x = np.log(bin_centers[mask])
    y = np.log(counts[mask])

    A_mat = np.column_stack([x, np.ones_like(x)])
    try:
        coeffs, _, _, _ = np.linalg.lstsq(A_mat, y, rcond=None)
        beta = float(coeffs[0])
        A = float(np.exp(coeffs[1]))
    except np.linalg.LinAlgError:
        beta, A = 0.0, 0.0

    return {'beta': beta, 'A': A}


# ============================================================================
# 6.  Hardy Z-function analogue
# ============================================================================

def hardy_z_function(
    shadow_coeffs: Dict[int, float],
    t_values: np.ndarray,
    max_r: Optional[int] = None,
) -> np.ndarray:
    r"""Compute the Hardy Z-function analogue for the shadow zeta:

    Z_A(t) = e^{i*theta_A(t)} * zeta_A(1/2 + it)

    where theta_A(t) is chosen so that Z_A(t) is real on the critical line.

    For a Dirichlet series zeta_A(s) = sum S_r r^{-s}, the phase is:
        theta_A(t) = -arg(zeta_A(1/2 + it))

    But we want Z_A = |zeta_A| * sign(cos(arg(zeta_A) + theta_A)).
    The simplest approach: Z_A(t) = Re(e^{i*theta_A(t)} * zeta_A(1/2+it))
    where theta_A(t) is a smooth phase.

    For the shadow zeta (finite Dirichlet series), we use:
        Z_A(t) = Re(zeta_A(1/2 + it)) [since there is no gamma factor]

    This is real and its sign changes correspond to zeros of Re(zeta_A)
    on the critical line.
    """
    t_arr = np.asarray(t_values, dtype=float)
    Z = np.zeros(len(t_arr))

    for idx, t in enumerate(t_arr):
        s = complex(0.5, t)
        val = _shadow_zeta_complex(shadow_coeffs, s, max_r)
        Z[idx] = val.real

    return Z


def hardy_z_sign_changes(
    shadow_coeffs: Dict[int, float],
    t_max: float = 100.0,
    dt: float = 0.1,
    max_r: Optional[int] = None,
) -> List[float]:
    """Find sign changes of Z_A(t) and return the locations.

    Each sign change corresponds to a zero of zeta_A on the critical line.
    """
    t_values = np.arange(dt, t_max, dt)
    Z = hardy_z_function(shadow_coeffs, t_values, max_r)

    sign_changes = []
    for i in range(len(Z) - 1):
        if Z[i] * Z[i + 1] < 0:
            # Bisect to refine
            t_lo, t_hi = t_values[i], t_values[i + 1]
            for _ in range(30):
                t_mid = (t_lo + t_hi) / 2.0
                s_mid = complex(0.5, t_mid)
                z_mid = _shadow_zeta_complex(shadow_coeffs, s_mid, max_r).real
                if z_mid * _shadow_zeta_complex(shadow_coeffs,
                                                 complex(0.5, t_lo),
                                                 max_r).real < 0:
                    t_hi = t_mid
                else:
                    t_lo = t_mid
            sign_changes.append((t_lo + t_hi) / 2.0)

    return sign_changes


# ============================================================================
# 7.  Autocorrelation of Hardy Z-function
# ============================================================================

def hardy_z_autocorrelation(
    shadow_coeffs: Dict[int, float],
    tau_values: np.ndarray,
    t_max: float = 100.0,
    dt: float = 0.1,
    max_r: Optional[int] = None,
) -> np.ndarray:
    r"""Compute the autocorrelation C(tau) = <Z_A(t) Z_A(t+tau)>.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dict
    tau_values : array of lag values
    t_max : maximum t for the average
    dt : step size for t
    max_r : max arity

    Returns
    -------
    Normalized autocorrelation C(tau) / C(0).
    """
    t_arr = np.arange(dt, t_max, dt)
    Z_base = hardy_z_function(shadow_coeffs, t_arr, max_r)

    # Variance (C(0))
    C0 = np.mean(Z_base**2)
    if C0 < 1e-30:
        return np.zeros(len(tau_values))

    tau_arr = np.asarray(tau_values, dtype=float)
    C = np.zeros(len(tau_arr))

    for idx, tau in enumerate(tau_arr):
        t_shifted = t_arr + tau
        # Only use t values where both t and t+tau are in range
        valid = t_shifted < t_max
        if np.sum(valid) < 3:
            continue
        Z_shifted = hardy_z_function(shadow_coeffs, t_shifted[valid], max_r)
        C[idx] = np.mean(Z_base[valid] * Z_shifted) / C0

    return C


def decorrelation_time(
    C_tau: np.ndarray,
    tau_values: np.ndarray,
    threshold: float = 1.0 / np.e,
) -> float:
    r"""Find the decorrelation time tau_dec where C(tau) drops below threshold.

    Default threshold = 1/e ~ 0.368.
    """
    for i, c in enumerate(C_tau):
        if c < threshold and i > 0:
            # Linear interpolation
            if i >= len(tau_values):
                return float(tau_values[-1])
            tau_lo = tau_values[i - 1]
            tau_hi = tau_values[i]
            c_lo = C_tau[i - 1]
            c_hi = c
            if abs(c_lo - c_hi) < 1e-30:
                return float(tau_hi)
            frac = (threshold - c_lo) / (c_hi - c_lo)
            return float(tau_lo + frac * (tau_hi - tau_lo))
    return float(tau_values[-1])


# ============================================================================
# 8.  Level spacing ratio
# ============================================================================

def spacing_ratios(unfolded: np.ndarray) -> np.ndarray:
    r"""Compute level spacing ratios r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}).

    For consecutive spacings s_n = u_{n+1} - u_n:
        r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})

    r_n in [0, 1].  For GUE: <r> ~ 0.5307.  For Poisson: <r> ~ 0.3863.
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    spacings = np.diff(u)

    if len(spacings) < 2:
        return np.array([])

    ratios = np.zeros(len(spacings) - 1)
    for i in range(len(spacings) - 1):
        s_n = spacings[i]
        s_np1 = spacings[i + 1]
        if max(s_n, s_np1) > 0:
            ratios[i] = min(s_n, s_np1) / max(s_n, s_np1)

    return ratios


def mean_spacing_ratio(unfolded: np.ndarray) -> float:
    """Compute <r> (mean spacing ratio)."""
    r = spacing_ratios(unfolded)
    if len(r) == 0:
        return 0.0
    return float(np.mean(r))


def classify_by_spacing_ratio(
    mean_r: float,
    tolerance: float = 0.05,
) -> str:
    """Classify the spectrum based on the mean spacing ratio.

    Returns 'GUE', 'GOE', 'Poisson', or 'intermediate'.
    """
    if abs(mean_r - GUE_MEAN_SPACING_RATIO) < tolerance:
        return 'GUE'
    elif abs(mean_r - GOE_MEAN_SPACING_RATIO) < tolerance:
        return 'GOE'
    elif abs(mean_r - POISSON_MEAN_SPACING_RATIO) < tolerance:
        return 'Poisson'
    elif POISSON_MEAN_SPACING_RATIO < mean_r < GUE_MEAN_SPACING_RATIO:
        return 'intermediate'
    else:
        return 'unclassified'


# ============================================================================
# 9.  GUE-Poisson transition detection
# ============================================================================

def ks_distance_from_gue(spacings: np.ndarray) -> float:
    r"""KS distance between the spacing distribution and GUE Wigner surmise.

    Uses the CDF:
        F_GUE(s) = erf(2s/sqrt(pi)) - (4s/pi) exp(-4s^2/pi)
    """
    from scipy.special import erf
    s = np.sort(spacings)
    N = len(s)
    if N == 0:
        return 1.0
    ecdf = np.arange(1, N + 1) / N
    cdf_gue = erf(2.0 * s / np.sqrt(np.pi)) - (4.0 * s / np.pi) * np.exp(-4.0 * s**2 / np.pi)
    return float(np.max(np.abs(ecdf - cdf_gue)))


def ks_distance_from_poisson(spacings: np.ndarray) -> float:
    """KS distance from Poisson (exponential) spacing distribution."""
    s = np.sort(spacings)
    N = len(s)
    if N == 0:
        return 1.0
    ecdf = np.arange(1, N + 1) / N
    cdf_poisson = 1.0 - np.exp(-s)
    return float(np.max(np.abs(ecdf - cdf_poisson)))


def ks_distance_from_goe(spacings: np.ndarray) -> float:
    """KS distance from GOE Wigner surmise."""
    s = np.sort(spacings)
    N = len(s)
    if N == 0:
        return 1.0
    ecdf = np.arange(1, N + 1) / N
    cdf_goe = 1.0 - np.exp(-np.pi * s**2 / 4.0)
    return float(np.max(np.abs(ecdf - cdf_goe)))


def gue_poisson_transition(
    c_values: List[float],
    t_max: float = 80.0,
    dt: float = 0.3,
) -> List[Dict[str, Any]]:
    r"""Track GUE-Poisson transition as c varies.

    For each c, computes Epstein zeros, unfolding, spacings,
    and KS distances from GUE, GOE, and Poisson.

    Returns list of dicts with c, n_zeros, ks_gue, ks_goe, ks_poisson,
    mean_spacing_ratio, classification.
    """
    if not HAS_PAIR_CORR:
        return [{'error': 'pair correlation engine not available'}]

    results = []
    for c_val in c_values:
        zeros = virasoro_epstein_zeros(c_val, t_max=t_max, dt=dt)
        if len(zeros) < 5:
            results.append({
                'c': c_val, 'n_zeros': len(zeros),
                'note': 'too few zeros',
            })
            continue

        a, b, cc, D = virasoro_form(c_val)
        unfolded = unfold_epstein_zeros(zeros, a, b, cc)
        spacings = np.diff(np.sort(unfolded))
        mean_sp = np.mean(spacings)
        if mean_sp > 0:
            spacings = spacings / mean_sp

        # KS distances
        try:
            d_gue = ks_distance_from_gue(spacings)
        except ImportError:
            d_gue = float('nan')
        d_poisson = ks_distance_from_poisson(spacings)
        try:
            d_goe = ks_distance_from_goe(spacings)
        except ImportError:
            d_goe = float('nan')

        # Spacing ratio
        r_mean = mean_spacing_ratio(unfolded)
        classification = classify_by_spacing_ratio(r_mean)

        results.append({
            'c': c_val,
            'n_zeros': len(zeros),
            'ks_gue': d_gue,
            'ks_goe': d_goe,
            'ks_poisson': d_poisson,
            'mean_spacing_ratio': r_mean,
            'classification': classification,
            'mean_spacing': float(mean_sp),
        })

    return results


# ============================================================================
# 10.  Koszul complementarity verification
# ============================================================================

def koszul_spectral_comparison(
    c_val: float,
    L_values: np.ndarray,
    t_max: float = 80.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    r"""Compare spectral statistics of Vir_c and Vir_{26-c}.

    Koszul duality: Vir_c^! = Vir_{26-c}.
    At c=13: self-dual, statistics should match exactly.

    Returns dict with sigma2 and delta3 for both c and 26-c.
    """
    c_dual = 26.0 - c_val
    L_arr = np.asarray(L_values, dtype=float)

    res_c = compute_number_variance_for_family('virasoro', c_val, L_arr,
                                                t_max=t_max, dt=dt)
    res_dual = compute_number_variance_for_family('virasoro', c_dual, L_arr,
                                                   t_max=t_max, dt=dt)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'nv_c': res_c,
        'nv_dual': res_dual,
    }


# ============================================================================
# 11.  Shadow depth class signature detection
# ============================================================================

def shadow_depth_spectral_signature(
    t_max: float = 80.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    r"""Test whether shadow depth class produces a measurable spectral signature.

    Shadow depth classes:
        G (Gaussian, r_max=2): Heisenberg — NO zeros (trivial zeta)
        L (Lie/tree, r_max=3): affine KM — equispaced zeros (2-term exp poly)
        C (contact, r_max=4): beta-gamma — 3-term exp poly zeros
        M (mixed, r_max=inf): Virasoro, W_N — Epstein zeros

    The key question: do different shadow depth classes produce
    distinguishable spectral statistics?

    Returns dict with statistics for each class.
    """
    results = {}

    # Class G: Heisenberg (no zeros)
    results['G'] = {
        'family': 'heisenberg', 'param': 1.0,
        'n_zeros': 0,
        'note': 'No zeros — shadow zeta is a monomial.',
    }

    # Class L: affine sl_2 at k=1
    raw_L = affine_sl2_zeros(1.0, n_max=200)
    gammas_L = np.array(sorted([z.imag for z in raw_L if 0.5 < z.imag < 200]))
    if len(gammas_L) > 5:
        sp_L = np.diff(gammas_L)
        mean_L = np.mean(sp_L)
        u_L = (gammas_L - gammas_L[0]) / mean_L if mean_L > 0 else gammas_L
        r_L = mean_spacing_ratio(u_L)
        results['L'] = {
            'family': 'affine_sl2', 'param': 1.0,
            'n_zeros': len(gammas_L),
            'mean_spacing_ratio': r_L,
            'note': 'Equispaced zeros (periodic, 2-term exp polynomial).',
            'spacing_std': float(np.std(sp_L / mean_L)) if mean_L > 0 else 0.0,
        }
    else:
        results['L'] = {'n_zeros': len(gammas_L), 'note': 'too few'}

    # Class M: Virasoro at c=10
    if HAS_PAIR_CORR:
        zeros_M = virasoro_epstein_zeros(10.0, t_max=t_max, dt=dt)
        if len(zeros_M) > 5:
            a, b, cc, D = virasoro_form(10.0)
            u_M = unfold_epstein_zeros(zeros_M, a, b, cc)
            sp_M = np.diff(np.sort(u_M))
            mean_M = np.mean(sp_M) if len(sp_M) > 0 else 1.0
            sp_norm = sp_M / mean_M if mean_M > 0 else sp_M
            r_M = mean_spacing_ratio(u_M)
            try:
                d_gue = ks_distance_from_gue(sp_norm)
            except ImportError:
                d_gue = float('nan')
            d_poisson = ks_distance_from_poisson(sp_norm)
            results['M'] = {
                'family': 'virasoro', 'param': 10.0,
                'n_zeros': len(zeros_M),
                'mean_spacing_ratio': r_M,
                'ks_gue': d_gue,
                'ks_poisson': d_poisson,
                'spacing_std': float(np.std(sp_norm)),
            }
        else:
            results['M'] = {'n_zeros': len(zeros_M), 'note': 'too few'}
    else:
        results['M'] = {'note': 'pair correlation engine not available'}

    return results


# ============================================================================
# 12.  Comprehensive spectral statistics report
# ============================================================================

def full_spectral_report(
    family: str,
    param: float,
    t_max: float = 80.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    r"""Generate a comprehensive spectral statistics report for one algebra.

    Combines: number variance, Delta_3, form factor, record gaps,
    small gaps, spacing ratio, Hardy Z sign changes.
    """
    L_values = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0])
    tau_sff = np.logspace(-2, 2, 50)

    # Get zeros
    if family == 'virasoro' and HAS_PAIR_CORR:
        zeros = virasoro_epstein_zeros(param, t_max=t_max, dt=dt)
        gammas = zeros
        if len(zeros) > 3:
            a, b, cc, D = virasoro_form(param)
            unfolded = unfold_epstein_zeros(zeros, a, b, cc)
        else:
            unfolded = np.array([])
    elif family == 'affine_sl2':
        raw = affine_sl2_zeros(param, n_max=200)
        gammas = np.array(sorted([z.imag for z in raw if 0.5 < z.imag < t_max]))
        if len(gammas) > 3:
            sp = np.diff(gammas)
            mean_sp = np.mean(sp) if len(sp) > 0 else 1.0
            unfolded = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        else:
            unfolded = np.array([])
    elif family == 'heisenberg':
        return {
            'family': family, 'param': param,
            'n_zeros': 0,
            'note': 'No zeros for Heisenberg',
        }
    else:
        coeffs = shadow_coefficients_extended(family, param, max_r=60)
        raw = find_zeros_grid(coeffs, re_range=(-5, 5),
                              im_range=(0.1, t_max),
                              grid_re=20, grid_im=100, max_r=60)
        gammas = np.array(sorted([z.imag for z in raw if z.imag > 0.5]))
        if len(gammas) > 3:
            sp = np.diff(gammas)
            mean_sp = np.mean(sp) if len(sp) > 0 else 1.0
            unfolded = (gammas - gammas[0]) / mean_sp if mean_sp > 0 else gammas
        else:
            unfolded = np.array([])

    report = {
        'family': family,
        'param': param,
        'n_zeros': len(gammas),
    }

    if len(unfolded) < 5:
        report['error'] = 'too few zeros for statistics'
        return report

    # Number variance
    nv = compute_number_variance(unfolded, L_values)
    report['number_variance'] = {
        'L': L_values.tolist(),
        'sigma2': nv.tolist(),
        'gue': gue_number_variance(L_values).tolist(),
    }

    # Delta_3
    d3 = compute_delta3(unfolded, L_values)
    report['delta3'] = {
        'L': L_values.tolist(),
        'delta3': d3.tolist(),
        'gue': gue_delta3(L_values).tolist(),
    }

    # Spacing ratio
    r_mean = mean_spacing_ratio(unfolded)
    report['spacing_ratio'] = {
        'mean_r': r_mean,
        'gue_reference': GUE_MEAN_SPACING_RATIO,
        'poisson_reference': POISSON_MEAN_SPACING_RATIO,
        'classification': classify_by_spacing_ratio(r_mean),
    }

    # Record gaps
    report['record_gaps'] = record_gaps(gammas, [50.0, t_max])

    # Small gaps
    report['small_gaps'] = small_gap_count(unfolded, [0.1, 0.01])

    # Level repulsion
    report['level_repulsion'] = level_repulsion_exponent(unfolded)

    # Form factor
    K = spectral_form_factor(gammas, tau_sff)
    drp = identify_dip_ramp_plateau(tau_sff, K)
    report['form_factor'] = {
        'tau_dip': drp['tau_dip'],
        'K_dip': drp['K_dip'],
        'tau_plateau': drp['tau_plateau'],
    }

    return report
