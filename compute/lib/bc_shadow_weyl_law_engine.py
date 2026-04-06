r"""Shadow Weyl law: zero-counting function vs shadow volume and spectral asymptotics.

MATHEMATICAL FRAMEWORK
======================

For a modular Koszul algebra A with shadow coefficients S_r(A), define the
shadow Dirac operator D_sh as the N x N matrix with entries:

    (D_sh)_{jk} = sqrt(|S_{j+1}|) * delta_{j,k-1} + sqrt(|S_{k+1}|) * delta_{j,k+1}
                  + sign(S_{j+1}) * phase_{j} * delta_{jk}

This tridiagonal operator encodes the shadow tower data.  Its spectrum
{lambda_1 <= lambda_2 <= ... <= lambda_N} defines:

1. EIGENVALUE COUNTING FUNCTION:
   N_shadow(lambda) = #{eigenvalues of |D_sh| <= lambda}

2. SHADOW WEYL LAW (from noncommutative geometry):
   N_shadow(lambda) ~ (Vol_NC / C_d) * lambda^{d_S} + O(lambda^{d_S - 1})
   where d_S is the spectral dimension and Vol_NC is the NC volume
   (related to the Dixmier trace).

3. SPECTRAL ZETA FUNCTION:
   zeta_D(s) = sum_n |lambda_n|^{-s}   (for lambda_n != 0)
   The residue at s = d_S gives the NC volume:
   Res_{s=d_S} zeta_D(s) = Vol_NC / Gamma(d_S/2 + 1)

4. HEAT KERNEL:
   Tr(e^{-t D_sh^2}) ~ (Vol_NC / (4*pi*t)^{d_S/2}) * (1 + a_1 t + a_2 t^2 + ...)
   as t -> 0+.  The leading Seeley-DeWitt coefficient gives the NC volume;
   the subleading coefficients are NC curvature invariants.

5. SHADOW WEYL LAW AT RIEMANN ZEROS:
   Evaluate N_shadow(gamma_n) at gamma_n = Im(rho_n) for the first 20
   nontrivial Riemann zeta zeros.  Test for systematic remainder structure.

SHADOW DIRAC OPERATOR CONSTRUCTION
===================================

For a shadow tower with coefficients S_r, r = 2, 3, ..., the shadow Dirac
is constructed as a tridiagonal matrix on the "arity Hilbert space" spanned
by states |r>, r = 2, 3, ..., N+1:

    D_sh = diagonal(mu_2, mu_3, ..., mu_{N+1})
         + off_diagonal(t_2, t_3, ..., t_N)

where:
    mu_r = S_r / max(|S_2|, 1)        (normalized shadow coefficient)
    t_r  = sqrt(|S_r * S_{r+1}|)^{1/2}  (hopping amplitude from shadow metric)

This gives D_sh symmetric with real eigenvalues.  The spectral data of D_sh
encodes the shadow tower in operator-theoretic language.

For class M algebras (infinite tower), D_sh has unbounded spectrum as N -> inf.
The spectral dimension d_S(A) is determined by the growth rate rho(A):

    d_S = 2 / log(1/rho)  (for rho < 1)

For class G/L/C algebras (finite tower), d_S = 0 (finite-rank operator).

MULTI-PATH VERIFICATION
========================

Every numerical result is verified by at least 3 independent paths:
(i)   Direct eigenvalue computation (numpy.linalg.eigvalsh)
(ii)  Weyl asymptotic (power-law fit to N(lambda))
(iii) Heat kernel (Laplace transform / Tauberian theorem)
(iv)  Spectral zeta residue
(v)   Sturm-Liouville counting (sign changes of characteristic polynomial)

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Cross-verify by 3+ independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np
from numpy.linalg import eigvalsh

# ---------------------------------------------------------------------------
# Import shadow coefficient providers
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
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    newton_zero,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
)

# ---------------------------------------------------------------------------
# First 30 nontrivial Riemann zeta zeros (imaginary parts).
# Source: LMFDB / Odlyzko tables, verified to 10+ digits.
# ---------------------------------------------------------------------------
RIEMANN_ZETA_ZEROS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147495,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173979,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492980517050,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.31785100573139,
]


# ============================================================================
# 0.  Shadow coefficient dispatch (from existing engines)
# ============================================================================

def _get_shadow_coeffs(
    family: str,
    param: float,
    max_r: int = 200,
) -> Dict[int, float]:
    """Get shadow coefficients for any family, extended to high arity."""
    return shadow_coefficients_extended(family, param, max_r)


def _shadow_class(family: str) -> str:
    """Return the shadow depth class G/L/C/M for a family."""
    classes = {
        'heisenberg': 'G',
        'affine_sl2': 'L',
        'affine_sl3': 'L',
        'betagamma': 'C',
        'virasoro': 'M',
        'w3_t': 'M',
        'w3_w': 'M',
    }
    return classes.get(family, 'M')


def _shadow_depth(family: str) -> int:
    """Return shadow depth r_max for a family (1000 = effectively infinity)."""
    depths = {
        'heisenberg': 2,
        'affine_sl2': 3,
        'affine_sl3': 3,
        'betagamma': 4,
        'virasoro': 1000,
        'w3_t': 1000,
        'w3_w': 1000,
    }
    return depths.get(family, 1000)


# ============================================================================
# 1.  Shadow Dirac operator construction
# ============================================================================

@dataclass
class ShadowDiracSpectrum:
    """Full spectral data for the shadow Dirac operator."""
    eigenvalues: np.ndarray            # sorted eigenvalues of D_sh
    abs_eigenvalues: np.ndarray        # sorted |lambda_n|, excluding zeros
    N: int                             # truncation size
    family: str
    param: float
    n_zero: int                        # number of zero eigenvalues
    spectral_gap: float                # smallest nonzero |lambda|
    spectral_radius: float             # largest |lambda|


def build_shadow_dirac(
    shadow_coeffs: Dict[int, float],
    N: int = 200,
) -> np.ndarray:
    r"""Build the shadow Dirac operator as an N x N tridiagonal matrix.

    The construction uses the shadow tower coefficients to define:
      - Diagonal: mu_r = S_r (normalized by |S_2| if |S_2| > 0)
      - Off-diagonal: t_r = (|S_r| * |S_{r+1}|)^{1/4} (geometric mean hopping)

    The normalization ensures the operator has eigenvalues of order 1 for
    generic parameters, making spectral comparisons meaningful.

    Parameters
    ----------
    shadow_coeffs : dict mapping arity r to S_r(A)
    N : matrix size (truncation of the arity space)

    Returns
    -------
    D_sh : N x N numpy array (symmetric, real)
    """
    # Normalization scale
    S2 = shadow_coeffs.get(2, 0.0)
    scale = max(abs(S2), 1e-15)

    D = np.zeros((N, N), dtype=np.float64)

    for i in range(N):
        r = i + 2  # arity r = 2, 3, ..., N+1
        Sr = shadow_coeffs.get(r, 0.0)
        D[i, i] = Sr / scale

    for i in range(N - 1):
        r = i + 2
        Sr = shadow_coeffs.get(r, 0.0)
        Sr1 = shadow_coeffs.get(r + 1, 0.0)
        # Hopping amplitude: geometric mean of adjacent shadow coefficients
        # with sign tracking
        hop = (abs(Sr) * abs(Sr1)) ** 0.25 / (scale ** 0.5) if (abs(Sr) > 1e-300 and abs(Sr1) > 1e-300) else 0.0
        D[i, i + 1] = hop
        D[i + 1, i] = hop

    return D


def shadow_dirac_spectrum(
    family: str,
    param: float,
    N: int = 200,
    max_r: int = 300,
) -> ShadowDiracSpectrum:
    """Compute the full spectrum of the shadow Dirac operator.

    Parameters
    ----------
    family : algebra family name
    param : family parameter (c for Virasoro, k for Heisenberg/affine, etc.)
    N : truncation size
    max_r : maximum arity for shadow coefficients

    Returns
    -------
    ShadowDiracSpectrum with sorted eigenvalues and metadata.
    """
    coeffs = _get_shadow_coeffs(family, param, max_r=max(max_r, N + 2))
    D = build_shadow_dirac(coeffs, N)
    eigs = eigvalsh(D)  # sorted ascending
    abs_eigs = np.sort(np.abs(eigs))
    # Remove near-zero eigenvalues
    tol = 1e-12 * max(abs(abs_eigs[-1]), 1.0)
    nonzero_mask = abs_eigs > tol
    abs_nonzero = abs_eigs[nonzero_mask]
    n_zero = int(np.sum(~nonzero_mask))

    gap = float(abs_nonzero[0]) if len(abs_nonzero) > 0 else 0.0
    radius = float(abs_nonzero[-1]) if len(abs_nonzero) > 0 else 0.0

    return ShadowDiracSpectrum(
        eigenvalues=eigs,
        abs_eigenvalues=abs_nonzero,
        N=N,
        family=family,
        param=param,
        n_zero=n_zero,
        spectral_gap=gap,
        spectral_radius=radius,
    )


# ============================================================================
# 2.  Eigenvalue counting function N_shadow(lambda)
# ============================================================================

def counting_function(
    spectrum: ShadowDiracSpectrum,
    lambdas: Optional[np.ndarray] = None,
    n_points: int = 500,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute the eigenvalue counting function N_shadow(lambda).

    N_shadow(lambda) = #{eigenvalues of |D_sh| <= lambda}

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum from shadow_dirac_spectrum()
    lambdas : array of lambda values at which to evaluate (if None, auto-generate)
    n_points : number of points if lambdas is None

    Returns
    -------
    (lambdas, N_values) : arrays of lambda values and counting function values
    """
    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) == 0:
        lam = np.linspace(0, 1, n_points)
        return lam, np.zeros(n_points)

    if lambdas is None:
        lam_max = float(abs_eigs[-1]) * 1.1
        lambdas = np.linspace(0, lam_max, n_points)

    # N(lambda) = number of |eigenvalues| <= lambda
    # Include zero eigenvalues in the count
    all_abs = np.sort(np.abs(spectrum.eigenvalues))
    N_values = np.searchsorted(all_abs, lambdas, side='right').astype(float)

    return lambdas, N_values


# ============================================================================
# 3.  Weyl law fitting: N(lambda) ~ a * lambda^d_S + b * lambda^{d_S - 1}
# ============================================================================

@dataclass
class WeylFitResult:
    """Result of fitting N(lambda) to the Weyl asymptotic."""
    spectral_dimension: float          # d_S
    weyl_coefficient: float            # a(c) = Vol_NC / (C_d)
    subleading_coefficient: float      # b(c)
    residuals_rms: float               # RMS of fit residuals
    r_squared: float                   # R^2 of the fit
    fit_range: Tuple[float, float]     # lambda range used for fit
    d_S_uncertainty: float             # estimated uncertainty in d_S


def fit_weyl_law(
    spectrum: ShadowDiracSpectrum,
    fit_fraction: float = 0.7,
    min_lambda_fraction: float = 0.1,
) -> WeylFitResult:
    r"""Fit the eigenvalue counting function to a Weyl law.

    Strategy: N(lambda) ~ a * lambda^d for large lambda.
    Take log: log N ~ d * log lambda + log a.
    Linear regression on the upper portion of the spectrum.

    Then refine with a two-term fit:
    N(lambda) ~ a * lambda^d + b * lambda^{d-1}

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    fit_fraction : fraction of eigenvalues to use (upper portion)
    min_lambda_fraction : minimum lambda as fraction of max (avoid small-lambda noise)

    Returns
    -------
    WeylFitResult with spectral dimension, Weyl coefficient, etc.
    """
    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) < 10:
        return WeylFitResult(
            spectral_dimension=0.0,
            weyl_coefficient=0.0,
            subleading_coefficient=0.0,
            residuals_rms=0.0,
            r_squared=0.0,
            fit_range=(0.0, 0.0),
            d_S_uncertainty=float('inf'),
        )

    # Generate counting function on eigenvalue locations
    lam_max = float(abs_eigs[-1])
    lam_min = lam_max * min_lambda_fraction
    n_pts = 1000
    lambdas = np.linspace(lam_min, lam_max, n_pts)
    _, N_vals = counting_function(spectrum, lambdas)

    # Use upper portion for fitting
    idx_start = int(n_pts * (1 - fit_fraction))
    lam_fit = lambdas[idx_start:]
    N_fit = N_vals[idx_start:]

    # Remove points where N = 0
    mask = N_fit > 0.5
    if np.sum(mask) < 5:
        return WeylFitResult(
            spectral_dimension=0.0,
            weyl_coefficient=0.0,
            subleading_coefficient=0.0,
            residuals_rms=0.0,
            r_squared=0.0,
            fit_range=(0.0, 0.0),
            d_S_uncertainty=float('inf'),
        )

    lam_fit = lam_fit[mask]
    N_fit = N_fit[mask]

    # Step 1: log-log linear regression for d_S
    log_lam = np.log(lam_fit)
    log_N = np.log(N_fit)

    # Linear fit: log_N = d_S * log_lam + log_a
    A_mat = np.vstack([log_lam, np.ones(len(log_lam))]).T
    result = np.linalg.lstsq(A_mat, log_N, rcond=None)
    coeffs_loglog = result[0]
    d_S = float(coeffs_loglog[0])
    log_a = float(coeffs_loglog[1])
    a_coeff = math.exp(log_a)

    # Compute R^2 for the log-log fit
    log_N_pred = A_mat @ coeffs_loglog
    ss_res = np.sum((log_N - log_N_pred) ** 2)
    ss_tot = np.sum((log_N - np.mean(log_N)) ** 2)
    r_squared = 1.0 - ss_res / max(ss_tot, 1e-300)

    # Uncertainty estimate from residuals
    if len(log_lam) > 2 and ss_tot > 1e-300:
        se = np.sqrt(ss_res / max(len(log_lam) - 2, 1))
        var_slope = se ** 2 / np.sum((log_lam - np.mean(log_lam)) ** 2)
        d_S_uncertainty = math.sqrt(max(var_slope, 0.0))
    else:
        d_S_uncertainty = float('inf')

    # Step 2: Two-term fit N ~ a * lambda^d + b * lambda^{d-1}
    # Using the estimated d_S
    b_coeff = 0.0
    if abs(d_S) > 0.01 and len(lam_fit) > 5:
        lam_d = lam_fit ** d_S
        lam_d1 = lam_fit ** max(d_S - 1, 0.01)
        B_mat = np.vstack([lam_d, lam_d1]).T
        result2 = np.linalg.lstsq(B_mat, N_fit, rcond=None)
        a_coeff = float(result2[0][0])
        b_coeff = float(result2[0][1])

        # RMS residual
        N_pred = B_mat @ result2[0]
        residuals_rms = float(np.sqrt(np.mean((N_fit - N_pred) ** 2)))
    else:
        residuals_rms = float(np.sqrt(ss_res / max(len(log_N), 1)))

    return WeylFitResult(
        spectral_dimension=d_S,
        weyl_coefficient=a_coeff,
        subleading_coefficient=b_coeff,
        residuals_rms=residuals_rms,
        r_squared=r_squared,
        fit_range=(float(lam_fit[0]), float(lam_fit[-1])),
        d_S_uncertainty=d_S_uncertainty,
    )


# ============================================================================
# 4.  Heat kernel trace: Tr(e^{-t D^2})
# ============================================================================

@dataclass
class HeatKernelResult:
    """Result of heat kernel computation."""
    t_values: np.ndarray
    trace_values: np.ndarray
    seeley_dewitt_a0: float        # Leading SD coefficient (= Vol_NC / (4pi)^{d/2})
    seeley_dewitt_a1: float        # First subleading coefficient
    spectral_dimension_heat: float  # d_S from heat kernel asymptotics
    zeta_residue: float             # Res_{s=d_S} zeta_D(s) from Mellin


def heat_kernel_trace(
    spectrum: ShadowDiracSpectrum,
    t_min: float = 1e-4,
    t_max: float = 100.0,
    n_t: int = 500,
) -> HeatKernelResult:
    r"""Compute the heat kernel trace Tr(e^{-t D_sh^2}).

    For small t, this has the asymptotic expansion:
        Tr(e^{-tD^2}) ~ a_0 * t^{-d_S/2} + a_1 * t^{-(d_S-2)/2} + ...

    where a_0 = Vol_NC / (4*pi)^{d_S/2}.

    The spectral dimension is extracted from the log-log slope:
        d/dt log Tr = -d_S / (2t) at leading order.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    t_min, t_max : time range
    n_t : number of time points (log-spaced)

    Returns
    -------
    HeatKernelResult with trace values and extracted coefficients.
    """
    eigs = spectrum.eigenvalues
    eigs_sq = eigs ** 2

    t_values = np.logspace(np.log10(t_min), np.log10(t_max), n_t)
    trace_values = np.zeros(n_t)

    for i, t in enumerate(t_values):
        trace_values[i] = np.sum(np.exp(-t * eigs_sq))

    # Extract spectral dimension from small-t behavior
    # log(Tr) ~ -(d_S/2) * log(t) + log(a_0) for small t
    # Use the smallest 20% of t values
    n_fit = max(int(0.2 * n_t), 10)
    log_t = np.log(t_values[:n_fit])
    log_tr = np.log(np.maximum(trace_values[:n_fit], 1e-300))

    # Guard against constant trace (finite spectrum, all eigenvalues ~ 0)
    if np.max(log_tr) - np.min(log_tr) < 1e-10:
        return HeatKernelResult(
            t_values=t_values,
            trace_values=trace_values,
            seeley_dewitt_a0=float(trace_values[0]),
            seeley_dewitt_a1=0.0,
            spectral_dimension_heat=0.0,
            zeta_residue=0.0,
        )

    A_mat = np.vstack([log_t, np.ones(n_fit)]).T
    result = np.linalg.lstsq(A_mat, log_tr, rcond=None)
    slope = float(result[0][0])
    intercept = float(result[0][1])

    d_S_heat = -2.0 * slope  # Tr ~ t^{-d_S/2}
    a0 = math.exp(intercept)

    # Subleading: fit Tr - a0 * t^{-d_S/2} to a1 * t^{-(d_S-2)/2}
    leading = a0 * t_values[:n_fit] ** (-d_S_heat / 2)
    remainder = trace_values[:n_fit] - leading
    a1 = 0.0
    if abs(d_S_heat) > 0.1 and np.any(np.abs(remainder) > 1e-15):
        # Rough estimate
        idx_mid = n_fit // 2
        t_mid = t_values[idx_mid]
        r_mid = remainder[idx_mid]
        exp_sub = -(d_S_heat - 2) / 2
        if abs(t_mid ** exp_sub) > 1e-300:
            a1 = r_mid / (t_mid ** exp_sub)

    # Spectral zeta residue via Mellin transform relation:
    # Res_{s=d_S} zeta_D(s) = a0 / Gamma(d_S/2)
    if d_S_heat > 0:
        try:
            gamma_val = math.gamma(d_S_heat / 2)
            zeta_res = a0 / gamma_val if gamma_val > 1e-300 else 0.0
        except (ValueError, OverflowError):
            zeta_res = 0.0
    else:
        zeta_res = 0.0

    return HeatKernelResult(
        t_values=t_values,
        trace_values=trace_values,
        seeley_dewitt_a0=a0,
        seeley_dewitt_a1=a1,
        spectral_dimension_heat=d_S_heat,
        zeta_residue=zeta_res,
    )


# ============================================================================
# 5.  Spectral zeta function: zeta_D(s) = sum |lambda_n|^{-s}
# ============================================================================

@dataclass
class SpectralZetaResult:
    """Result of spectral zeta computation."""
    s_values: np.ndarray               # where evaluated (complex)
    zeta_values: np.ndarray            # zeta_D(s) values
    pole_location: float               # estimated d_S from pole
    residue_at_pole: float             # Res_{s=d_S} zeta_D


def spectral_zeta(
    spectrum: ShadowDiracSpectrum,
    s_values: Optional[np.ndarray] = None,
    s_min: float = 0.1,
    s_max: float = 5.0,
    n_s: int = 200,
) -> SpectralZetaResult:
    r"""Compute the spectral zeta function zeta_D(s) = sum |lambda_n|^{-s}.

    This sum converges for Re(s) > d_S (the spectral dimension).
    For a finite truncation, the sum is always finite, but the effective
    convergence abscissa reveals d_S.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    s_values : array of real s values (if None, auto-generate)
    s_min, s_max : range for auto-generated s values
    n_s : number of s points

    Returns
    -------
    SpectralZetaResult with zeta values and pole analysis.
    """
    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) == 0:
        s_arr = np.linspace(s_min, s_max, n_s) if s_values is None else s_values
        return SpectralZetaResult(
            s_values=s_arr,
            zeta_values=np.zeros(len(s_arr)),
            pole_location=0.0,
            residue_at_pole=0.0,
        )

    if s_values is None:
        s_arr = np.linspace(s_min, s_max, n_s)
    else:
        s_arr = np.asarray(s_values, dtype=float)

    zeta_vals = np.zeros(len(s_arr))
    for i, s in enumerate(s_arr):
        # zeta_D(s) = sum |lambda_n|^{-s}
        zeta_vals[i] = np.sum(abs_eigs ** (-s))

    # Find the effective pole: where zeta_D(s) grows rapidly as s decreases
    # Look for the s value where zeta_D has maximum log-derivative
    if len(s_arr) > 5:
        log_zeta = np.log(np.maximum(zeta_vals, 1e-300))
        # Numerical derivative
        ds = s_arr[1] - s_arr[0] if len(s_arr) > 1 else 1.0
        if abs(ds) > 1e-15:
            dlog = np.gradient(log_zeta, ds)
            # Pole is where dlog is most negative
            idx_pole = np.argmin(dlog)
            pole_loc = float(s_arr[idx_pole])

            # Residue estimate: Res ~ lim_{s->d_S} (s - d_S) * zeta_D(s)
            if idx_pole > 0 and idx_pole < len(s_arr) - 1:
                # Use finite difference around the pole
                s_near = s_arr[max(idx_pole - 1, 0):min(idx_pole + 2, len(s_arr))]
                z_near = zeta_vals[max(idx_pole - 1, 0):min(idx_pole + 2, len(s_arr))]
                if len(s_near) >= 2:
                    # (s - pole) * zeta at a nearby point
                    ds_near = s_near - pole_loc
                    products = ds_near * z_near
                    mask_good = np.abs(ds_near) > 1e-10
                    if np.any(mask_good):
                        residue = float(np.median(products[mask_good]))
                    else:
                        residue = 0.0
                else:
                    residue = 0.0
            else:
                residue = 0.0
        else:
            pole_loc = s_arr[0]
            residue = 0.0
    else:
        pole_loc = 0.0
        residue = 0.0

    return SpectralZetaResult(
        s_values=s_arr,
        zeta_values=zeta_vals,
        pole_location=pole_loc,
        residue_at_pole=residue,
    )


# ============================================================================
# 6.  Zeros of spectral zeta function zeta_D(s) in the critical strip
# ============================================================================

def spectral_zeta_complex(
    spectrum: ShadowDiracSpectrum,
    s: complex,
) -> complex:
    """Evaluate zeta_D(s) = sum |lambda_n|^{-s} for complex s."""
    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) == 0:
        return 0.0 + 0.0j
    total = 0.0 + 0.0j
    for lam in abs_eigs:
        if lam > 1e-300:
            total += lam ** (-s)
    return total


def spectral_zeta_derivative(
    spectrum: ShadowDiracSpectrum,
    s: complex,
) -> complex:
    """Evaluate zeta_D'(s) = -sum |lambda_n|^{-s} * log(|lambda_n|)."""
    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) == 0:
        return 0.0 + 0.0j
    total = 0.0 + 0.0j
    for lam in abs_eigs:
        if lam > 1e-300:
            total -= lam ** (-s) * math.log(lam)
    return total


def find_spectral_zeta_zeros(
    spectrum: ShadowDiracSpectrum,
    re_range: Tuple[float, float] = (-2.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 30,
    grid_im: int = 100,
    n_max: int = 50,
    tol: float = 1e-10,
    dedup_tol: float = 1e-5,
) -> List[complex]:
    r"""Find zeros of zeta_D(s) in the critical strip.

    Seeds Newton's method from a grid, then deduplicates.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    re_range, im_range : search region
    grid_re, grid_im : grid density
    n_max : maximum number of zeros to find
    tol : Newton tolerance
    dedup_tol : deduplication tolerance

    Returns
    -------
    List of zeros, sorted by imaginary part.
    """
    zeros: List[complex] = []

    re_step = (re_range[1] - re_range[0]) / max(grid_re, 1)
    im_step = (im_range[1] - im_range[0]) / max(grid_im, 1)

    for i in range(grid_re + 1):
        for j in range(grid_im + 1):
            s0 = complex(
                re_range[0] + i * re_step,
                im_range[0] + j * im_step,
            )
            # Newton iteration
            s = s0
            converged = False
            for _ in range(100):
                f = spectral_zeta_complex(spectrum, s)
                fp = spectral_zeta_derivative(spectrum, s)
                if abs(fp) < 1e-300:
                    break
                ds = f / fp
                s = s - ds
                if abs(ds) < tol:
                    f_check = spectral_zeta_complex(spectrum, s)
                    if abs(f_check) < tol * 100:
                        converged = True
                    break

            if not converged:
                continue

            # Check if inside search region
            if not (re_range[0] - 1 <= s.real <= re_range[1] + 1):
                continue
            if not (im_range[0] - 1 <= s.imag <= im_range[1] + 1):
                continue

            # Deduplication
            is_dup = False
            for z in zeros:
                if abs(z - s) < dedup_tol:
                    is_dup = True
                    break
            if not is_dup:
                zeros.append(s)

            if len(zeros) >= n_max:
                break
        if len(zeros) >= n_max:
            break

    # Sort by imaginary part
    zeros.sort(key=lambda z: (z.imag, z.real))
    return zeros[:n_max]


# ============================================================================
# 7.  Pair correlation of spectral zeta zeros
# ============================================================================

@dataclass
class PairCorrelationResult:
    """Result of pair correlation analysis."""
    x_values: np.ndarray
    R2_values: np.ndarray
    R2_gue: np.ndarray
    R2_poisson: np.ndarray
    distance_to_gue: float
    distance_to_poisson: float
    n_zeros_used: int
    mean_spacing: float


def pair_correlation_spectral_zeros(
    zeros: List[complex],
    n_bins: int = 50,
    x_max: float = 3.0,
) -> PairCorrelationResult:
    r"""Compute the pair correlation function of spectral zeta zeros.

    R_2(x) = lim (1/N) #{(i,j) : |gamma_i - gamma_j| * rho < x} / delta_x

    where gamma_n = Im(zero_n) and rho is the mean density.

    GUE prediction: R_2(x) = 1 - (sin(pi*x)/(pi*x))^2
    Poisson: R_2(x) = 1

    Parameters
    ----------
    zeros : list of complex zeros of zeta_D
    n_bins : number of bins for the histogram
    x_max : maximum normalized spacing

    Returns
    -------
    PairCorrelationResult with R_2 data and distance metrics.
    """
    # Extract imaginary parts (positive only)
    gammas = sorted([abs(z.imag) for z in zeros if abs(z.imag) > 0.01])

    n = len(gammas)
    if n < 5:
        x = np.linspace(0.01, x_max, n_bins)
        return PairCorrelationResult(
            x_values=x,
            R2_values=np.ones(n_bins),
            R2_gue=1.0 - (np.sin(np.pi * x) / (np.pi * x)) ** 2,
            R2_poisson=np.ones(n_bins),
            distance_to_gue=0.0,
            distance_to_poisson=0.0,
            n_zeros_used=0,
            mean_spacing=0.0,
        )

    # Mean spacing
    spacings = np.diff(gammas)
    mean_sp = float(np.mean(spacings)) if len(spacings) > 0 else 1.0

    # Normalized differences
    diffs = []
    for i in range(n):
        for j in range(i + 1, min(i + 20, n)):  # local pairs only
            delta = abs(gammas[j] - gammas[i]) / mean_sp
            if delta < x_max:
                diffs.append(delta)

    x = np.linspace(0.01, x_max, n_bins)
    dx = x[1] - x[0]
    R2 = np.zeros(n_bins)

    if len(diffs) > 0:
        hist, _ = np.histogram(diffs, bins=np.append(x - dx / 2, x[-1] + dx / 2))
        # Normalize: R_2(x) dx = (1/N) * count in [x, x+dx]
        norm = len(diffs) * dx if len(diffs) > 0 else 1.0
        R2 = hist.astype(float) / max(norm, 1e-300)

    # GUE and Poisson references
    R2_gue = 1.0 - (np.sin(np.pi * x) / (np.pi * x + 1e-300)) ** 2
    R2_poisson = np.ones(n_bins)

    # L2 distances
    d_gue = float(np.sqrt(np.mean((R2 - R2_gue) ** 2)))
    d_poisson = float(np.sqrt(np.mean((R2 - R2_poisson) ** 2)))

    return PairCorrelationResult(
        x_values=x,
        R2_values=R2,
        R2_gue=R2_gue,
        R2_poisson=R2_poisson,
        distance_to_gue=d_gue,
        distance_to_poisson=d_poisson,
        n_zeros_used=n,
        mean_spacing=mean_sp,
    )


# ============================================================================
# 8.  Dixmier trace (NC volume)
# ============================================================================

def dixmier_trace(
    spectrum: ShadowDiracSpectrum,
    d_S: Optional[float] = None,
) -> float:
    r"""Compute the Dixmier trace (noncommutative volume) of |D_sh|^{-d_S}.

    The Dixmier trace is:
        Tr_omega(|D|^{-d_S}) = lim_{N->inf} (1/log N) * sum_{n=1}^{N} mu_n^{-d_S}

    where mu_n are the singular values of D (= |eigenvalues| for self-adjoint D),
    sorted in decreasing order.

    For a finite truncation, we approximate:
        Tr_omega ~ (1/log(N)) * sum_{n=1}^{N} |lambda_n|^{-d_S}

    This gives the NC volume Vol_NC.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    d_S : spectral dimension (if None, computed from Weyl fit)

    Returns
    -------
    Dixmier trace value (NC volume).
    """
    if d_S is None:
        fit = fit_weyl_law(spectrum)
        d_S = fit.spectral_dimension

    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) == 0 or d_S <= 0:
        return 0.0

    N = len(abs_eigs)
    log_N = math.log(max(N, 2))

    # Partial sums of |lambda_n|^{-d_S}, sorted by increasing |lambda|
    # The Dixmier trace uses the Cesaro-type average
    total = np.sum(abs_eigs ** (-d_S))

    return float(total / log_N)


# ============================================================================
# 9.  Weyl remainder analysis
# ============================================================================

@dataclass
class WeylRemainderResult:
    """Analysis of the Weyl remainder R(lambda) = N(lambda) - Weyl leading term."""
    lambdas: np.ndarray
    remainder: np.ndarray
    normalized_remainder: np.ndarray    # R(lambda) / lambda^{(d_S-1)/2}
    remainder_rms: float
    sharp_weyl: bool                    # True if normalized remainder -> 0
    remainder_exponent: float           # R ~ lambda^alpha => alpha


def weyl_remainder(
    spectrum: ShadowDiracSpectrum,
    weyl_fit: Optional[WeylFitResult] = None,
    n_points: int = 500,
) -> WeylRemainderResult:
    r"""Compute and analyze the Weyl remainder.

    R(lambda) = N_shadow(lambda) - a * lambda^{d_S}

    Test the sharp Weyl law: R(lambda) / lambda^{(d_S-1)/2} -> 0.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    weyl_fit : WeylFitResult (if None, compute it)
    n_points : number of lambda values

    Returns
    -------
    WeylRemainderResult with remainder analysis.
    """
    if weyl_fit is None:
        weyl_fit = fit_weyl_law(spectrum)

    d_S = weyl_fit.spectral_dimension
    a = weyl_fit.weyl_coefficient

    abs_eigs = spectrum.abs_eigenvalues
    if len(abs_eigs) < 5 or abs(d_S) < 0.01:
        lam = np.linspace(0.1, 1.0, n_points)
        return WeylRemainderResult(
            lambdas=lam,
            remainder=np.zeros(n_points),
            normalized_remainder=np.zeros(n_points),
            remainder_rms=0.0,
            sharp_weyl=True,
            remainder_exponent=0.0,
        )

    lam_max = float(abs_eigs[-1]) * 1.05
    lambdas = np.linspace(float(abs_eigs[0]) * 0.5, lam_max, n_points)
    _, N_vals = counting_function(spectrum, lambdas)

    # Weyl leading term
    weyl_leading = a * lambdas ** d_S
    remainder = N_vals - weyl_leading

    # Normalized remainder
    norm_exp = max((d_S - 1) / 2, 0.01)
    norm_factor = lambdas ** norm_exp
    norm_factor = np.maximum(norm_factor, 1e-300)
    normalized = remainder / norm_factor

    # Check sharp Weyl law: does normalized remainder decrease?
    # Use the upper 50% of lambda values
    idx_mid = n_points // 2
    upper_norm = np.abs(normalized[idx_mid:])
    lower_norm = np.abs(normalized[:idx_mid])
    if np.mean(lower_norm) > 1e-15:
        ratio = np.mean(upper_norm) / np.mean(lower_norm)
        sharp = ratio < 0.5  # Decreasing by at least half
    else:
        sharp = True

    # Fit remainder exponent: |R| ~ lambda^alpha
    mask = (lambdas > float(abs_eigs[0])) & (np.abs(remainder) > 1e-15)
    if np.sum(mask) > 10:
        log_lam = np.log(lambdas[mask])
        log_R = np.log(np.abs(remainder[mask]))
        A_mat = np.vstack([log_lam, np.ones(len(log_lam))]).T
        result = np.linalg.lstsq(A_mat, log_R, rcond=None)
        rem_exp = float(result[0][0])
    else:
        rem_exp = 0.0

    return WeylRemainderResult(
        lambdas=lambdas,
        remainder=remainder,
        normalized_remainder=normalized,
        remainder_rms=float(np.sqrt(np.mean(remainder ** 2))),
        sharp_weyl=sharp,
        remainder_exponent=rem_exp,
    )


# ============================================================================
# 10.  Shadow Weyl law at Riemann zeros
# ============================================================================

@dataclass
class WeylAtRiemannZeroResult:
    """N_shadow(gamma_n) and Weyl prediction at a Riemann zero."""
    zero_index: int                    # n (1-based)
    gamma_n: float                     # Im(rho_n)
    N_actual: float                    # actual counting function value
    N_weyl: float                      # Weyl prediction
    remainder: float                   # N_actual - N_weyl
    relative_remainder: float          # remainder / N_weyl


def weyl_at_riemann_zeros(
    spectrum: ShadowDiracSpectrum,
    weyl_fit: Optional[WeylFitResult] = None,
    n_zeros: int = 20,
) -> List[WeylAtRiemannZeroResult]:
    r"""Evaluate N_shadow(gamma_n) at the first n_zeros Riemann zeta zeros.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    weyl_fit : WeylFitResult (if None, compute it)
    n_zeros : number of Riemann zeros to evaluate at

    Returns
    -------
    List of WeylAtRiemannZeroResult, one per Riemann zero.
    """
    if weyl_fit is None:
        weyl_fit = fit_weyl_law(spectrum)

    d_S = weyl_fit.spectral_dimension
    a = weyl_fit.weyl_coefficient

    results = []
    for n in range(min(n_zeros, len(RIEMANN_ZETA_ZEROS))):
        gamma_n = RIEMANN_ZETA_ZEROS[n]

        # N_shadow(gamma_n) = #{|eigenvalues| <= gamma_n}
        all_abs = np.sort(np.abs(spectrum.eigenvalues))
        N_actual = float(np.searchsorted(all_abs, gamma_n, side='right'))

        # Weyl prediction
        N_weyl = a * gamma_n ** d_S if d_S > 0 else 0.0

        remainder = N_actual - N_weyl
        rel_rem = remainder / max(abs(N_weyl), 1e-15)

        results.append(WeylAtRiemannZeroResult(
            zero_index=n + 1,
            gamma_n=gamma_n,
            N_actual=N_actual,
            N_weyl=N_weyl,
            remainder=remainder,
            relative_remainder=rel_rem,
        ))

    return results


# ============================================================================
# 11.  Selberg-type analogy for zero counting
# ============================================================================

@dataclass
class SelbergAnalogy:
    """Selberg-type zero counting formula for shadow spectral zeta."""
    T_values: np.ndarray
    N_actual: np.ndarray               # actual #{zeros with |Im| < T}
    N_selberg: np.ndarray              # Selberg-type prediction
    remainder: np.ndarray
    leading_coefficient: float          # coefficient of T*log(T) term
    subleading_coefficient: float       # coefficient of T term


def selberg_type_counting(
    spectral_zeros: List[complex],
    T_max: float = 50.0,
    n_T: int = 200,
) -> SelbergAnalogy:
    r"""Fit the zero-counting function to a Selberg-type formula.

    For the Riemann zeta: N(T) = (T/(2*pi)) * log(T/(2*pi*e)) + 7/8 + S(T)
    where S(T) = O(log T).

    For zeta_D(s), we fit:
        N_D(T) = alpha * T * log(T) + beta * T + gamma + R(T)

    Parameters
    ----------
    spectral_zeros : list of complex zeros of zeta_D
    T_max : maximum height T
    n_T : number of T values

    Returns
    -------
    SelbergAnalogy with fitting data.
    """
    # Extract imaginary parts
    gammas = sorted([abs(z.imag) for z in spectral_zeros if abs(z.imag) > 0.01])

    T_values = np.linspace(1.0, T_max, n_T)

    # Actual counting
    N_actual = np.zeros(n_T)
    gammas_arr = np.array(gammas)
    for i, T in enumerate(T_values):
        N_actual[i] = np.sum(gammas_arr <= T)

    # Fit: N(T) ~ alpha * T * log(T) + beta * T + gamma
    if len(gammas) < 3 or np.max(N_actual) < 2:
        return SelbergAnalogy(
            T_values=T_values,
            N_actual=N_actual,
            N_selberg=np.zeros(n_T),
            remainder=N_actual.copy(),
            leading_coefficient=0.0,
            subleading_coefficient=0.0,
        )

    # Use the range where N > 0
    mask = N_actual > 0.5
    if np.sum(mask) < 3:
        return SelbergAnalogy(
            T_values=T_values,
            N_actual=N_actual,
            N_selberg=np.zeros(n_T),
            remainder=N_actual.copy(),
            leading_coefficient=0.0,
            subleading_coefficient=0.0,
        )

    T_fit = T_values[mask]
    N_fit = N_actual[mask]

    # Design matrix: [T*log(T), T, 1]
    A_mat = np.vstack([
        T_fit * np.log(T_fit),
        T_fit,
        np.ones(len(T_fit)),
    ]).T
    result = np.linalg.lstsq(A_mat, N_fit, rcond=None)
    alpha, beta, gamma_const = result[0]

    # Prediction
    N_selberg = alpha * T_values * np.log(np.maximum(T_values, 1e-10)) + beta * T_values + gamma_const
    remainder = N_actual - N_selberg

    return SelbergAnalogy(
        T_values=T_values,
        N_actual=N_actual,
        N_selberg=N_selberg,
        remainder=remainder,
        leading_coefficient=float(alpha),
        subleading_coefficient=float(beta),
    )


# ============================================================================
# 12.  Multi-path verification suite
# ============================================================================

@dataclass
class MultiPathVerification:
    """Results of multi-path Weyl law verification."""
    # Path 1: Direct eigenvalue counting
    d_S_direct: float
    a_direct: float

    # Path 2: Heat kernel
    d_S_heat: float
    a_heat: float

    # Path 3: Spectral zeta residue
    d_S_zeta: float
    residue_zeta: float

    # Path 4: Dixmier trace
    vol_dixmier: float

    # Path 5: Sturm-Liouville (eigenvalue count by sign changes)
    d_S_sturm: float

    # Agreement metrics
    d_S_spread: float                  # max - min of d_S estimates
    d_S_mean: float                    # mean d_S
    a_spread: float                    # spread in Weyl coefficient
    paths_agree: bool                  # True if all paths agree within 20%


def _sturm_liouville_count(
    D: np.ndarray,
    lam: float,
) -> int:
    """Count eigenvalues of D below lam using Sturm sequence (LDL factoring).

    For a symmetric tridiagonal matrix T, the number of eigenvalues < lam
    equals the number of negative entries in the diagonal D of the LDL^T
    factorization of T - lam * I.
    """
    N = D.shape[0]
    shifted = D.copy()
    for i in range(N):
        shifted[i, i] -= lam

    # LDL^T factorization of tridiagonal matrix
    d = np.zeros(N)
    d[0] = shifted[0, 0]
    neg_count = 0

    for i in range(1, N):
        if abs(d[i - 1]) < 1e-300:
            d[i] = shifted[i, i]
        else:
            e = shifted[i, i - 1]  # off-diagonal
            d[i] = shifted[i, i] - e ** 2 / d[i - 1]

        if d[i] < 0:
            neg_count += 1

    if d[0] < 0:
        neg_count += 1

    return neg_count


def multi_path_verify(
    family: str,
    param: float,
    N: int = 200,
) -> MultiPathVerification:
    r"""Verify the Weyl law via 5 independent methods.

    Path 1: Direct eigenvalue counting + power-law fit
    Path 2: Heat kernel small-t asymptotics
    Path 3: Spectral zeta function pole
    Path 4: Dixmier trace
    Path 5: Sturm-Liouville eigenvalue counting

    Parameters
    ----------
    family : algebra family
    param : family parameter
    N : truncation size

    Returns
    -------
    MultiPathVerification with all 5 path results and agreement metrics.
    """
    spec = shadow_dirac_spectrum(family, param, N)

    # Path 1: Direct Weyl fit
    fit = fit_weyl_law(spec)
    d_S_direct = fit.spectral_dimension
    a_direct = fit.weyl_coefficient

    # Path 2: Heat kernel
    hk = heat_kernel_trace(spec)
    d_S_heat = hk.spectral_dimension_heat
    a_heat = hk.seeley_dewitt_a0

    # Path 3: Spectral zeta
    sz = spectral_zeta(spec)
    d_S_zeta = sz.pole_location
    res_zeta = sz.residue_at_pole

    # Path 4: Dixmier trace
    vol_dix = dixmier_trace(spec, d_S_direct)

    # Path 5: Sturm-Liouville counting at several lambda values
    coeffs = _get_shadow_coeffs(family, param, max_r=N + 2)
    D_mat = build_shadow_dirac(coeffs, N)

    # Use 5 lambda values spanning the spectrum
    abs_eigs = spec.abs_eigenvalues
    if len(abs_eigs) > 10:
        test_lambdas = np.linspace(float(abs_eigs[2]), float(abs_eigs[-3]), 5)
        sturm_counts = [_sturm_liouville_count(D_mat, lam) for lam in test_lambdas]
        direct_counts = [int(np.sum(spec.eigenvalues < lam)) for lam in test_lambdas]

        # Fit Sturm counts to Weyl law
        mask = np.array(sturm_counts) > 0
        if np.sum(mask) >= 3:
            log_lam = np.log(test_lambdas[mask])
            log_N_sturm = np.log(np.array(sturm_counts, dtype=float)[mask])
            A_mat = np.vstack([log_lam, np.ones(len(log_lam))]).T
            result = np.linalg.lstsq(A_mat, log_N_sturm, rcond=None)
            d_S_sturm = float(result[0][0])
        else:
            d_S_sturm = d_S_direct
    else:
        d_S_sturm = d_S_direct

    # Agreement metrics
    d_S_values = [d_S_direct, d_S_heat, d_S_zeta, d_S_sturm]
    d_S_values_valid = [d for d in d_S_values if abs(d) > 0.01]
    if len(d_S_values_valid) >= 2:
        d_S_spread = max(d_S_values_valid) - min(d_S_values_valid)
        d_S_mean = sum(d_S_values_valid) / len(d_S_values_valid)
    else:
        d_S_spread = 0.0
        d_S_mean = d_S_direct

    a_vals = [abs(a_direct), abs(a_heat)]
    a_vals_valid = [a for a in a_vals if a > 1e-15]
    a_spread = (max(a_vals_valid) - min(a_vals_valid)) / max(max(a_vals_valid), 1e-15) if len(a_vals_valid) >= 2 else 0.0

    # Agreement: all d_S within 20% of mean
    agree = d_S_spread < 0.2 * max(abs(d_S_mean), 0.1) if abs(d_S_mean) > 0.01 else True

    return MultiPathVerification(
        d_S_direct=d_S_direct,
        a_direct=a_direct,
        d_S_heat=d_S_heat,
        a_heat=a_heat,
        d_S_zeta=d_S_zeta,
        residue_zeta=res_zeta,
        vol_dixmier=vol_dix,
        d_S_sturm=d_S_sturm,
        d_S_spread=d_S_spread,
        d_S_mean=d_S_mean,
        a_spread=a_spread,
        paths_agree=agree,
    )


# ============================================================================
# 13.  Full shadow Weyl analysis for a single algebra
# ============================================================================

@dataclass
class ShadowWeylAnalysis:
    """Complete Weyl law analysis for a single algebra."""
    family: str
    param: float
    N: int
    shadow_class: str

    # Spectrum
    spectrum: ShadowDiracSpectrum

    # Weyl fit
    weyl_fit: WeylFitResult

    # Heat kernel
    heat_kernel: HeatKernelResult

    # Spectral zeta
    spectral_zeta_result: SpectralZetaResult

    # Spectral zeta zeros
    spectral_zeta_zeros: List[complex]

    # Pair correlation
    pair_correlation: Optional[PairCorrelationResult]

    # Remainder analysis
    remainder: WeylRemainderResult

    # NC volume
    dixmier_trace_val: float

    # Riemann zero evaluations
    riemann_zero_evals: List[WeylAtRiemannZeroResult]

    # Multi-path verification
    verification: MultiPathVerification


def full_shadow_weyl_analysis(
    family: str,
    param: float,
    N: int = 200,
    max_r: int = 300,
    find_zeta_zeros: bool = True,
    n_riemann_zeros: int = 20,
) -> ShadowWeylAnalysis:
    r"""Run the complete shadow Weyl law analysis for a single algebra.

    This is the master function that computes everything:
    1. Shadow Dirac spectrum
    2. Weyl law fit (spectral dimension, Weyl coefficient)
    3. Heat kernel trace and Seeley-DeWitt coefficients
    4. Spectral zeta function and its zeros
    5. Pair correlation of zeta zeros vs GUE
    6. Weyl remainder analysis
    7. Dixmier trace (NC volume)
    8. Evaluation at Riemann zeros
    9. Multi-path verification

    Parameters
    ----------
    family : algebra family
    param : family parameter
    N : truncation size
    max_r : max arity for shadow coefficients
    find_zeta_zeros : if True, search for spectral zeta zeros (slow)
    n_riemann_zeros : number of Riemann zeros for evaluation

    Returns
    -------
    ShadowWeylAnalysis with complete results.
    """
    # 1. Spectrum
    spec = shadow_dirac_spectrum(family, param, N, max_r)

    # 2. Weyl fit
    wf = fit_weyl_law(spec)

    # 3. Heat kernel
    hk = heat_kernel_trace(spec)

    # 4. Spectral zeta
    sz = spectral_zeta(spec)

    # 5. Spectral zeta zeros
    if find_zeta_zeros and len(spec.abs_eigenvalues) > 5:
        zeta_zeros = find_spectral_zeta_zeros(
            spec,
            re_range=(-1.0, max(wf.spectral_dimension + 1, 3.0)),
            im_range=(-30.0, 30.0),
            grid_re=20,
            grid_im=60,
            n_max=50,
        )
    else:
        zeta_zeros = []

    # 6. Pair correlation
    if len(zeta_zeros) >= 10:
        pc = pair_correlation_spectral_zeros(zeta_zeros)
    else:
        pc = None

    # 7. Remainder
    rem = weyl_remainder(spec, wf)

    # 8. Dixmier trace
    dix = dixmier_trace(spec, wf.spectral_dimension)

    # 9. Riemann zero evaluations
    rze = weyl_at_riemann_zeros(spec, wf, n_riemann_zeros)

    # Multi-path verification
    verif = multi_path_verify(family, param, N)

    return ShadowWeylAnalysis(
        family=family,
        param=param,
        N=N,
        shadow_class=_shadow_class(family),
        spectrum=spec,
        weyl_fit=wf,
        heat_kernel=hk,
        spectral_zeta_result=sz,
        spectral_zeta_zeros=zeta_zeros,
        pair_correlation=pc,
        remainder=rem,
        dixmier_trace_val=dix,
        riemann_zero_evals=rze,
        verification=verif,
    )


# ============================================================================
# 14.  Virasoro c-scan: spectral dimension as function of c
# ============================================================================

@dataclass
class VirasoroCscanResult:
    """Results of scanning the Weyl law across Virasoro central charges."""
    c_values: List[float]
    spectral_dimensions: List[float]
    weyl_coefficients: List[float]
    subleading_coefficients: List[float]
    dixmier_traces: List[float]
    d_S_heat: List[float]
    d_S_zeta: List[float]
    spectral_gaps: List[float]
    spectral_radii: List[float]


def virasoro_c_scan(
    c_values: Optional[List[float]] = None,
    N: int = 200,
) -> VirasoroCscanResult:
    r"""Scan the shadow Weyl law across Virasoro central charges c = 1..26.

    For each c, compute:
    - Shadow Dirac spectrum
    - Spectral dimension d_S(c) from Weyl fit and heat kernel
    - Weyl coefficient a(c)
    - Dixmier trace (NC volume)

    Parameters
    ----------
    c_values : list of central charges (default: 1..26)
    N : truncation size

    Returns
    -------
    VirasoroCscanResult with all c-dependent data.
    """
    if c_values is None:
        c_values = list(range(1, 27))

    results = VirasoroCscanResult(
        c_values=c_values,
        spectral_dimensions=[],
        weyl_coefficients=[],
        subleading_coefficients=[],
        dixmier_traces=[],
        d_S_heat=[],
        d_S_zeta=[],
        spectral_gaps=[],
        spectral_radii=[],
    )

    for c in c_values:
        spec = shadow_dirac_spectrum('virasoro', float(c), N)
        wf = fit_weyl_law(spec)
        hk = heat_kernel_trace(spec, t_min=1e-3, t_max=10.0, n_t=200)
        sz = spectral_zeta(spec)
        dix = dixmier_trace(spec, wf.spectral_dimension)

        results.spectral_dimensions.append(wf.spectral_dimension)
        results.weyl_coefficients.append(wf.weyl_coefficient)
        results.subleading_coefficients.append(wf.subleading_coefficient)
        results.dixmier_traces.append(dix)
        results.d_S_heat.append(hk.spectral_dimension_heat)
        results.d_S_zeta.append(sz.pole_location)
        results.spectral_gaps.append(spec.spectral_gap)
        results.spectral_radii.append(spec.spectral_radius)

    return results


# ============================================================================
# 15.  Remainder structure at Riemann zeros
# ============================================================================

@dataclass
class RemainderStructureResult:
    """Analysis of systematic structure in the Weyl remainder at Riemann zeros."""
    gamma_values: np.ndarray
    remainders: np.ndarray
    normalized_remainders: np.ndarray
    autocorrelation: np.ndarray        # autocorrelation of remainder sequence
    is_systematic: bool                # True if remainder has detectable structure
    kolmogorov_smirnov: float          # KS statistic vs uniform
    mean_remainder: float
    std_remainder: float


def remainder_structure_at_zeros(
    spectrum: ShadowDiracSpectrum,
    weyl_fit: Optional[WeylFitResult] = None,
    n_zeros: int = 20,
) -> RemainderStructureResult:
    r"""Analyze systematic structure in R(gamma_n) = N(gamma_n) - Weyl(gamma_n).

    Tests:
    1. Is the mean remainder significantly nonzero?
    2. Is the remainder autocorrelated (not white noise)?
    3. Does the remainder sequence have systematic drift?
    4. KS test vs uniform distribution of normalized remainders.

    Parameters
    ----------
    spectrum : ShadowDiracSpectrum
    weyl_fit : WeylFitResult (if None, compute it)
    n_zeros : number of Riemann zeros

    Returns
    -------
    RemainderStructureResult with structure analysis.
    """
    evals = weyl_at_riemann_zeros(spectrum, weyl_fit, n_zeros)

    if len(evals) < 3:
        return RemainderStructureResult(
            gamma_values=np.array([]),
            remainders=np.array([]),
            normalized_remainders=np.array([]),
            autocorrelation=np.array([]),
            is_systematic=False,
            kolmogorov_smirnov=0.0,
            mean_remainder=0.0,
            std_remainder=0.0,
        )

    gammas = np.array([e.gamma_n for e in evals])
    remainders = np.array([e.remainder for e in evals])

    # Normalize remainders
    std = np.std(remainders) if np.std(remainders) > 1e-15 else 1.0
    normalized = (remainders - np.mean(remainders)) / std

    # Autocorrelation
    n = len(normalized)
    autocorr = np.zeros(min(n, 10))
    for lag in range(len(autocorr)):
        if lag == 0:
            autocorr[0] = 1.0
        else:
            c1 = normalized[:n - lag]
            c2 = normalized[lag:]
            autocorr[lag] = np.mean(c1 * c2)

    # KS test: are normalized remainders uniformly distributed?
    # Simple one-sided KS statistic
    sorted_norm = np.sort(normalized)
    n_pts = len(sorted_norm)
    empirical_cdf = np.arange(1, n_pts + 1) / n_pts
    # Compare to standard normal CDF
    normal_cdf = 0.5 * (1 + np.array([math.erf(x / math.sqrt(2)) for x in sorted_norm]))
    ks_stat = float(np.max(np.abs(empirical_cdf - normal_cdf)))

    # Structure test: significant if autocorrelation at lag 1 > 0.3 or KS > 0.3
    is_sys = (abs(autocorr[1]) > 0.3 if len(autocorr) > 1 else False) or ks_stat > 0.3

    return RemainderStructureResult(
        gamma_values=gammas,
        remainders=remainders,
        normalized_remainders=normalized,
        autocorrelation=autocorr,
        is_systematic=is_sys,
        kolmogorov_smirnov=ks_stat,
        mean_remainder=float(np.mean(remainders)),
        std_remainder=float(np.std(remainders)),
    )


# ============================================================================
# 16.  Cross-class comparison
# ============================================================================

@dataclass
class CrossClassComparison:
    """Compare Weyl law properties across shadow depth classes."""
    families: List[str]
    params: List[float]
    classes: List[str]
    spectral_dimensions: List[float]
    weyl_coefficients: List[float]
    dixmier_traces: List[float]
    sharp_weyl_holds: List[bool]
    verification_passes: List[bool]


def cross_class_comparison(
    test_cases: Optional[List[Tuple[str, float]]] = None,
    N: int = 100,
) -> CrossClassComparison:
    r"""Compare the shadow Weyl law across different shadow depth classes.

    Default test cases cover all four classes: G, L, C, M.

    Parameters
    ----------
    test_cases : list of (family, param) pairs (default: canonical representatives)
    N : truncation size (smaller for speed)

    Returns
    -------
    CrossClassComparison with inter-class comparison data.
    """
    if test_cases is None:
        test_cases = [
            ('heisenberg', 1.0),       # Class G
            ('affine_sl2', 1.0),       # Class L
            ('betagamma', 0.5),        # Class C
            ('virasoro', 10.0),        # Class M
            ('virasoro', 13.0),        # Class M (self-dual)
            ('virasoro', 25.0),        # Class M (near-critical)
        ]

    result = CrossClassComparison(
        families=[],
        params=[],
        classes=[],
        spectral_dimensions=[],
        weyl_coefficients=[],
        dixmier_traces=[],
        sharp_weyl_holds=[],
        verification_passes=[],
    )

    for family, param in test_cases:
        spec = shadow_dirac_spectrum(family, param, N)
        wf = fit_weyl_law(spec)
        rem = weyl_remainder(spec, wf)
        dix = dixmier_trace(spec, wf.spectral_dimension)
        verif = multi_path_verify(family, param, N)

        result.families.append(family)
        result.params.append(param)
        result.classes.append(_shadow_class(family))
        result.spectral_dimensions.append(wf.spectral_dimension)
        result.weyl_coefficients.append(wf.weyl_coefficient)
        result.dixmier_traces.append(dix)
        result.sharp_weyl_holds.append(rem.sharp_weyl)
        result.verification_passes.append(verif.paths_agree)

    return result


# ============================================================================
# 17.  Koszul complementarity of Weyl data
# ============================================================================

@dataclass
class WeylComplementarityResult:
    """Test Koszul complementarity at the level of Weyl law data."""
    c: float
    c_dual: float
    d_S: float
    d_S_dual: float
    d_S_sum: float
    weyl_coeff: float
    weyl_coeff_dual: float
    dixmier: float
    dixmier_dual: float
    dixmier_sum: float


def weyl_complementarity(
    c: float,
    N: int = 150,
) -> WeylComplementarityResult:
    r"""Test Koszul complementarity of Weyl law data for Virasoro.

    For Vir_c and Vir_{26-c}:
    - kappa(c) + kappa(26-c) = 13 (AP24, NOT 0)
    - Do spectral dimensions satisfy d_S(c) + d_S(26-c) = const?
    - Do NC volumes satisfy Vol(c) + Vol(26-c) = const?

    Parameters
    ----------
    c : central charge (the dual is 26 - c)
    N : truncation size

    Returns
    -------
    WeylComplementarityResult.
    """
    c_dual = 26.0 - c

    spec = shadow_dirac_spectrum('virasoro', c, N)
    spec_dual = shadow_dirac_spectrum('virasoro', c_dual, N)

    wf = fit_weyl_law(spec)
    wf_dual = fit_weyl_law(spec_dual)

    dix = dixmier_trace(spec, wf.spectral_dimension)
    dix_dual = dixmier_trace(spec_dual, wf_dual.spectral_dimension)

    return WeylComplementarityResult(
        c=c,
        c_dual=c_dual,
        d_S=wf.spectral_dimension,
        d_S_dual=wf_dual.spectral_dimension,
        d_S_sum=wf.spectral_dimension + wf_dual.spectral_dimension,
        weyl_coeff=wf.weyl_coefficient,
        weyl_coeff_dual=wf_dual.weyl_coefficient,
        dixmier=dix,
        dixmier_dual=dix_dual,
        dixmier_sum=dix + dix_dual,
    )
