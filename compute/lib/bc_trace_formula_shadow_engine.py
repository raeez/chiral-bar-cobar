r"""BC-101: Shadow trace formula engine — geometric vs spectral comparison.

The Selberg trace formula equates a spectral sum (over eigenvalues of the
Laplacian) with a geometric sum (over conjugacy classes / closed geodesics).
This module implements the shadow-algebraic analogue for modular Koszul
algebras, connecting the zeros of the shadow zeta function zeta_A(s)
to the shadow coefficients S_r(A) (the "geometric" data encoding OPE
structure = "closed geodesics" of the bar complex).

SPECTRAL SIDE:
    Sigma^{spec}_A(h) = sum_{rho: zeta_A(rho)=0} h(rho)
for a test function h (Schwartz class).

GEOMETRIC SIDE (Weil explicit formula):
    Sigma^{geom}_A(h) = (1/(2*pi)) int h(t) (zeta'_A/zeta_A)(1/2+it) dt
                      + (identity term) + (continuous spectrum)

TRACE FORMULA IDENTITY:
    Sigma^{spec} = Sigma^{geom}
via the explicit formula, tested numerically for Gaussian, Lorentzian,
and indicator test functions.

HEAT KERNEL FROM SHADOW ZEROS:
    K_A(t) = sum_{rho} e^{-t |rho|^2}
with small-t Weyl law expansion K_A(t) ~ a_0/t + a_1 + a_2 t + ...

PRIME GEODESIC THEOREM:
    pi^{sh}(x) = #{r <= e^x : S_r != 0}
For class M: pi^{sh}(x) = floor(e^x) - 1 ~ e^x.
Error term from oscillatory zero contributions.

KUZNETSOV FORMULA:
    Shadow bilinear spectral identity pairing S_m, S_n against
    zero-indexed "Fourier coefficients" a_rho(m) = m^{-rho}.

RELATIVE TRACE FORMULA (Koszul pairs):
    For (A, A!), shared zero structure from complementarity.
    Enhanced symmetry at c=13 (self-dual point for Virasoro).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify all results by >=3 independent paths.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Convention checks when comparing to classical number theory.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

import numpy as np

# ---------------------------------------------------------------------------
# Import shadow coefficient providers and zeta evaluation from existing engines
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    shadow_zeta_numerical,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    find_zeros_grid,
    newton_zero,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
    _deduplicate_zeros,
)


# ============================================================================
# 1.  Shadow coefficient providers (dispatch)
# ============================================================================

def virasoro_shadow_coefficients(c_val: float, max_r: int = 100) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c.

    Delegates to the canonical provider.  S_2 = c/2 = kappa(Vir_c).
    CAUTION (AP1): kappa(Vir_c) = c/2.  Do NOT use dim*k/2h^v.
    """
    return virasoro_shadow_coefficients_numerical(c_val, max_r)


def get_shadow_coefficients(
    family: str,
    param: float,
    max_r: int = 100,
) -> Dict[int, float]:
    """Dispatch shadow coefficients for any standard family."""
    return shadow_coefficients_extended(family, param, max_r)


# ============================================================================
# 2.  Shadow zeta zeros (from existing engine, with caching)
# ============================================================================

_ZERO_CACHE: Dict[Tuple[str, float, int], List[complex]] = {}


def get_shadow_zeros(
    family: str,
    param: float,
    n_zeros: int = 100,
    max_r: int = 100,
    im_range: Tuple[float, float] = (-200.0, 200.0),
    grid_re: int = 30,
    grid_im: int = 300,
) -> List[complex]:
    """Find zeros of zeta_A(s) for a given family, with caching.

    For finite towers (class G, L, C): uses exact formulas or grid search.
    For class M (Virasoro): grid Newton search over the strip.

    Returns zeros sorted by |Im(s)|.
    """
    cache_key = (family, param, n_zeros)
    if cache_key in _ZERO_CACHE:
        return _ZERO_CACHE[cache_key]

    coeffs = get_shadow_coefficients(family, param, max_r)

    # For Heisenberg: no zeros
    if family == 'heisenberg':
        _ZERO_CACHE[cache_key] = []
        return []

    # For affine sl_2 / sl_3: analytic zeros
    if family in ('affine_sl2', 'affine_sl3'):
        from compute.lib.bc_shadow_zeta_zeros_engine import (
            affine_sl2_zeros,
            affine_sl3_zeros,
        )
        if family == 'affine_sl2':
            zeros = affine_sl2_zeros(param, n_max=n_zeros)
        else:
            zeros = affine_sl3_zeros(param, n_max=n_zeros)
        _ZERO_CACHE[cache_key] = zeros
        return zeros

    # Grid search for general case
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-10.0, 10.0),
        im_range=im_range,
        grid_re=grid_re,
        grid_im=grid_im,
        max_r=max_r,
    )
    # Sort by |Im|
    zeros.sort(key=lambda z: abs(z.imag))
    if len(zeros) > n_zeros:
        zeros = zeros[:n_zeros]
    _ZERO_CACHE[cache_key] = zeros
    return zeros


# ============================================================================
# 3.  Test functions (Schwartz class)
# ============================================================================

def gaussian_test(s: complex, sigma: float = 1.0) -> complex:
    """h(s) = exp(-s^2 / (2*sigma^2)).  Gaussian test function.

    Handles overflow for large |s| by returning 0 when the real part
    of the exponent is very negative.
    """
    exponent = -s * s / (2.0 * sigma * sigma)
    if exponent.real < -700:
        return 0.0 + 0.0j
    try:
        return cmath.exp(exponent)
    except OverflowError:
        return 0.0 + 0.0j


def lorentzian_test(s: complex, a: float = 1.0) -> complex:
    """h(s) = 1/(s^2 + a^2).  Lorentzian test function.

    Handles near-pole cases by clamping to a large finite value.
    """
    denom = s * s + a * a
    if abs(denom) < 1e-300:
        return complex(1e300, 0)
    return 1.0 / denom


def indicator_test(s: complex, T: float = 10.0) -> complex:
    """h(s) = 1 if |Im(s)| < T, else 0.  Counting function.

    For complex s, we use a smoothed version for numerical stability:
    h(s) = 1 if |s.imag| < T, 0 otherwise (applied to imaginary part).
    When s is real, h(s) = 1 always (for |0| < T).
    """
    if abs(s.imag) < T:
        return 1.0 + 0.0j
    return 0.0 + 0.0j


def gaussian_fourier(t: float, sigma: float = 1.0) -> float:
    r"""Fourier transform of h(s) = exp(-s^2/(2*sigma^2)):
    h_hat(t) = sigma * sqrt(2*pi) * exp(-sigma^2 * t^2 / 2).
    """
    return sigma * math.sqrt(2.0 * math.pi) * math.exp(-sigma * sigma * t * t / 2.0)


def lorentzian_fourier(t: float, a: float = 1.0) -> float:
    r"""Fourier transform of h(s) = 1/(s^2 + a^2):
    h_hat(t) = (pi/a) * exp(-a * |t|).
    """
    return (math.pi / a) * math.exp(-a * abs(t))


# ============================================================================
# 4.  Spectral side: sum over zeros
# ============================================================================

def spectral_sum(
    zeros: List[complex],
    test_fn: Callable[[complex], complex],
) -> complex:
    r"""Sigma^{spec}_A(h) = sum_{rho: zeta_A(rho)=0} h(rho).

    Evaluates the test function at each zero and sums.
    """
    total = 0.0 + 0.0j
    for rho in zeros:
        total += test_fn(rho)
    return total


def spectral_sum_gaussian(
    zeros: List[complex],
    sigma: float = 1.0,
) -> complex:
    """Spectral sum with Gaussian test function."""
    return spectral_sum(zeros, lambda s: gaussian_test(s, sigma))


def spectral_sum_lorentzian(
    zeros: List[complex],
    a: float = 1.0,
) -> complex:
    """Spectral sum with Lorentzian test function."""
    return spectral_sum(zeros, lambda s: lorentzian_test(s, a))


def spectral_sum_indicator(
    zeros: List[complex],
    T: float = 10.0,
) -> complex:
    """Spectral sum with indicator test function = counting function N_A(T)."""
    return spectral_sum(zeros, lambda s: indicator_test(s, T))


# ============================================================================
# 5.  Geometric side: shadow length spectrum
# ============================================================================

def shadow_length_spectrum(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> List[Tuple[float, float]]:
    r"""The shadow length spectrum: {(log(r), w_r)} for each S_r != 0.

    ell_r = log(r)  (shadow "geodesic length")
    w_r = |S_r| / S_2  (normalized "multiplicity")

    Returns list of (length, weight) pairs sorted by length.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    S2 = shadow_coeffs.get(2, 0.0)
    if abs(S2) < 1e-300:
        S2 = 1.0  # fallback normalization

    spectrum = []
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300:
            spectrum.append((math.log(r), abs(Sr) / abs(S2)))
    return spectrum


def geometric_sum_direct(
    shadow_coeffs: Dict[int, float],
    test_fn_fourier: Callable[[float], float],
    max_r: Optional[int] = None,
) -> float:
    r"""Geometric side: sum_{r>=2} S_r * h_hat(log r).

    This is the geometric sum using the Fourier transform of the test
    function evaluated at the shadow "geodesic lengths" log(r).

    For the trace formula: sum S_r * h_hat(log r) should equal
    sum_rho h(gamma_rho) + correction terms.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * test_fn_fourier(math.log(r))
    return total


def geometric_sum_gaussian(
    shadow_coeffs: Dict[int, float],
    sigma: float = 1.0,
    max_r: Optional[int] = None,
) -> float:
    """Geometric sum with Gaussian h_hat."""
    return geometric_sum_direct(
        shadow_coeffs,
        lambda t: gaussian_fourier(t, sigma),
        max_r,
    )


def geometric_sum_lorentzian(
    shadow_coeffs: Dict[int, float],
    a: float = 1.0,
    max_r: Optional[int] = None,
) -> float:
    """Geometric sum with Lorentzian h_hat."""
    return geometric_sum_direct(
        shadow_coeffs,
        lambda t: lorentzian_fourier(t, a),
        max_r,
    )


# ============================================================================
# 6.  Explicit formula (Weil-type) for the shadow zeta
# ============================================================================

def weil_explicit_spectral(
    zeros: List[complex],
    test_fn: Callable[[complex], complex],
) -> complex:
    r"""Spectral side of the Weil explicit formula:

    W^{spec}(h) = sum_{rho} h(rho)

    Same as spectral_sum but named for the explicit formula context.
    """
    return spectral_sum(zeros, test_fn)


def weil_explicit_geometric(
    shadow_coeffs: Dict[int, float],
    test_fn_at_log: Callable[[float], float],
    max_r: Optional[int] = None,
) -> float:
    r"""Geometric side of the Weil explicit formula:

    W^{geom}(h) = sum_{r>=2} S_r * h_hat(log r) / sqrt(r)

    The sqrt(r) factor is the analogue of the p^{k/2} normalization.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * test_fn_at_log(math.log(r)) / math.sqrt(r)
    return total


def log_derivative_integral(
    shadow_coeffs: Dict[int, float],
    test_fn: Callable[[float], float],
    t_range: Tuple[float, float] = (-50.0, 50.0),
    n_points: int = 2000,
    max_r: Optional[int] = None,
) -> complex:
    r"""(1/(2*pi)) integral h(t) * (zeta'_A/zeta_A)(1/2 + it) dt.

    Numerical integration of the log-derivative against the test function
    along the line Re(s) = 1/2.

    This is the "analytic" form of the geometric side.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    dt = (t_range[1] - t_range[0]) / n_points
    total = 0.0 + 0.0j

    for k in range(n_points + 1):
        t = t_range[0] + k * dt
        s = complex(0.5, t)

        zeta_val = _shadow_zeta_complex(shadow_coeffs, s, max_r)
        zeta_deriv = _shadow_zeta_derivative(shadow_coeffs, s, max_r)

        if abs(zeta_val) < 1e-300:
            continue

        log_deriv = zeta_deriv / zeta_val
        w = 1.0 if (k == 0 or k == n_points) else 2.0  # trapezoidal
        total += test_fn(t) * log_deriv * dt * w / 2.0

    return total / (2.0 * math.pi)


# ============================================================================
# 7.  Trace formula comparison: spectral = geometric
# ============================================================================

@dataclass
class TraceFormulaResult:
    """Result of trace formula comparison."""
    spectral_sum: complex
    geometric_sum: float
    log_deriv_integral: complex
    relative_error_geom: float
    relative_error_logderiv: float
    sigma_or_param: float
    test_type: str


def trace_formula_gaussian(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    sigma: float = 1.0,
    max_r: Optional[int] = None,
) -> TraceFormulaResult:
    """Compare spectral and geometric sides for Gaussian test function.

    Spectral: sum_rho exp(-rho^2 / (2*sigma^2))
    Geometric: sum_r S_r * h_hat(log r) where h_hat = sigma*sqrt(2pi)*exp(...)

    The trace formula identity:
        sum_rho h(rho) = sum_r S_r h_hat(log r) + correction
    """
    spec = spectral_sum_gaussian(zeros, sigma)
    geom = geometric_sum_gaussian(shadow_coeffs, sigma, max_r)

    logderiv = log_derivative_integral(
        shadow_coeffs,
        lambda t: math.exp(-t * t / (2.0 * sigma * sigma)),
        t_range=(-5.0 * sigma, 5.0 * sigma),
        n_points=2000,
        max_r=max_r,
    )

    denom_geom = max(abs(geom), abs(spec.real), 1e-15)
    rel_err_geom = abs(spec.real - geom) / denom_geom

    denom_logderiv = max(abs(logderiv), abs(spec), 1e-15)
    rel_err_logderiv = abs(spec - logderiv) / denom_logderiv

    return TraceFormulaResult(
        spectral_sum=spec,
        geometric_sum=geom,
        log_deriv_integral=logderiv,
        relative_error_geom=rel_err_geom,
        relative_error_logderiv=rel_err_logderiv,
        sigma_or_param=sigma,
        test_type='gaussian',
    )


def trace_formula_lorentzian(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    a: float = 1.0,
    max_r: Optional[int] = None,
) -> TraceFormulaResult:
    """Compare spectral and geometric sides for Lorentzian test function.

    h(s) = 1/(s^2 + a^2),  h_hat(t) = (pi/a)*exp(-a|t|).
    """
    spec = spectral_sum_lorentzian(zeros, a)
    geom = geometric_sum_lorentzian(shadow_coeffs, a, max_r)

    logderiv = log_derivative_integral(
        shadow_coeffs,
        lambda t: 1.0 / (t * t + a * a),
        t_range=(-20.0 * a, 20.0 * a),
        n_points=2000,
        max_r=max_r,
    )

    denom_geom = max(abs(geom), abs(spec.real), 1e-15)
    rel_err_geom = abs(spec.real - geom) / denom_geom

    denom_logderiv = max(abs(logderiv), abs(spec), 1e-15)
    rel_err_logderiv = abs(spec - logderiv) / denom_logderiv

    return TraceFormulaResult(
        spectral_sum=spec,
        geometric_sum=geom,
        log_deriv_integral=logderiv,
        relative_error_geom=rel_err_geom,
        relative_error_logderiv=rel_err_logderiv,
        sigma_or_param=a,
        test_type='lorentzian',
    )


# ============================================================================
# 8.  Heat kernel from shadow zeros
# ============================================================================

def heat_kernel_spectral(
    zeros: List[complex],
    t: float,
) -> float:
    r"""K_A(t) = sum_{rho: zeta_A(rho)=0} e^{-t |rho|^2}.

    The spectral heat kernel: sum of Gaussians over zero locations.
    """
    total = 0.0
    for rho in zeros:
        mod_sq = rho.real ** 2 + rho.imag ** 2
        total += math.exp(-t * mod_sq)
    return total


def heat_kernel_from_coefficients(
    shadow_coeffs: Dict[int, float],
    lam: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Heat kernel from shadow coefficients: K(lam) = sum S_r exp(-lam*r)."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * math.exp(-lam * r)
    return total


def heat_kernel_weyl_coefficients(
    zeros: List[complex],
    t_values: List[float],
) -> Dict[str, float]:
    r"""Extract Weyl law coefficients from K_A(t) ~ a_0/t + a_1 + a_2*t.

    For small t, the heat kernel has an asymptotic expansion.
    a_0 / t dominates (divergent as t -> 0).
    We fit K(t) * t = a_0 + a_1 * t + a_2 * t^2 to extract a_0, a_1, a_2.
    """
    if len(t_values) < 3:
        return {'a_0': 0.0, 'a_1': 0.0, 'a_2': 0.0}

    t_arr = np.array(t_values)
    K_arr = np.array([heat_kernel_spectral(zeros, t) for t in t_values])
    Kt_arr = K_arr * t_arr  # K(t)*t = a_0 + a_1*t + a_2*t^2

    # Fit polynomial a_0 + a_1*t + a_2*t^2
    X = np.column_stack([np.ones_like(t_arr), t_arr, t_arr ** 2])
    try:
        coeffs, _, _, _ = np.linalg.lstsq(X, Kt_arr, rcond=None)
    except np.linalg.LinAlgError:
        return {'a_0': 0.0, 'a_1': 0.0, 'a_2': 0.0}

    return {
        'a_0': float(coeffs[0]),
        'a_1': float(coeffs[1]),
        'a_2': float(coeffs[2]),
    }


def heat_kernel_regularized(
    zeros: List[complex],
    t: float,
    a_0: float,
) -> float:
    r"""K_A(t) - a_0/t: regularized heat kernel (removes leading divergence)."""
    return heat_kernel_spectral(zeros, t) - a_0 / t


# ============================================================================
# 9.  Arthur trace formula: discrete + continuous + residual
# ============================================================================

def arthur_discrete_spectrum(
    zeros: List[complex],
    test_fn: Callable[[complex], complex],
) -> complex:
    """Discrete spectrum contribution = spectral sum over zeros."""
    return spectral_sum(zeros, test_fn)


def arthur_continuous_spectrum(
    shadow_coeffs: Dict[int, float],
    shadow_dual_coeffs: Dict[int, float],
    test_fn: Callable[[float], float],
    t_range: Tuple[float, float] = (-50.0, 50.0),
    n_points: int = 2000,
    max_r: Optional[int] = None,
) -> complex:
    r"""Continuous spectrum contribution from complementarity.

    For Virasoro: zeta_c(s) + zeta_{26-c}(s) = zeta_D(s).
    The "Eisenstein" contribution E_A(s) = zeta_D(s)/2.

    Continuous contribution:
        (1/(4*pi)) int h(t) (zeta'_D/zeta_D)(1/2+it) dt
    """
    if max_r is None:
        max_r = max(max(shadow_coeffs.keys()), max(shadow_dual_coeffs.keys()))

    dt = (t_range[1] - t_range[0]) / n_points
    total = 0.0 + 0.0j

    for k in range(n_points + 1):
        t = t_range[0] + k * dt
        s = complex(0.5, t)

        zeta_D = (_shadow_zeta_complex(shadow_coeffs, s, max_r) +
                  _shadow_zeta_complex(shadow_dual_coeffs, s, max_r))
        zeta_D_prime = (_shadow_zeta_derivative(shadow_coeffs, s, max_r) +
                        _shadow_zeta_derivative(shadow_dual_coeffs, s, max_r))

        if abs(zeta_D) < 1e-300:
            continue

        log_deriv_D = zeta_D_prime / zeta_D
        w = 1.0 if (k == 0 or k == n_points) else 2.0
        total += test_fn(t) * log_deriv_D * dt * w / 2.0

    return total / (4.0 * math.pi)


def eisenstein_contribution(
    shadow_coeffs: Dict[int, float],
    shadow_dual_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    r"""E_A(s) = zeta_D(s)/2 = (zeta_A(s) + zeta_{A!}(s)) / 2.

    The Eisenstein series contribution at a specific point.
    """
    zeta_A = _shadow_zeta_complex(shadow_coeffs, s, max_r)
    zeta_dual = _shadow_zeta_complex(shadow_dual_coeffs, s, max_r)
    return (zeta_A + zeta_dual) / 2.0


def arthur_full_trace(
    zeros: List[complex],
    dual_zeros: List[complex],
    shadow_coeffs: Dict[int, float],
    shadow_dual_coeffs: Dict[int, float],
    test_fn: Callable[[complex], complex],
    test_fn_real: Callable[[float], float],
    max_r: Optional[int] = None,
) -> Dict[str, complex]:
    """Full Arthur trace formula decomposition.

    Returns discrete + continuous + total contributions.
    """
    discrete = arthur_discrete_spectrum(zeros, test_fn)
    continuous = arthur_continuous_spectrum(
        shadow_coeffs, shadow_dual_coeffs,
        test_fn_real, max_r=max_r,
    )
    return {
        'discrete': discrete,
        'continuous': continuous,
        'total': discrete + continuous,
    }


# ============================================================================
# 10.  Prime geodesic theorem from shadow
# ============================================================================

def prime_geodesic_counting(
    shadow_coeffs: Dict[int, float],
    x_values: List[float],
) -> Dict[float, int]:
    r"""pi^{sh}(x) = #{r <= e^x : S_r != 0, r >= 2}.

    For class M (Virasoro): ALL S_r != 0, so pi^{sh}(x) = floor(e^x) - 1.
    """
    max_r = max(shadow_coeffs.keys())
    result = {}
    for x in x_values:
        upper = min(int(math.floor(math.exp(x))), max_r)
        count = 0
        for r in range(2, upper + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) > 1e-300:
                count += 1
        result[x] = count
    return result


def prime_geodesic_theorem_error(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    x: float,
) -> Dict[str, float]:
    r"""Error term in the prime geodesic theorem.

    pi^{sh}(x) = li(e^x) + sum_rho e^{rho*x}/rho + smaller terms.

    The main term is the logarithmic integral li(e^x) ~ e^x/x.
    The error term is the sum over zeros.
    """
    # Main term
    ex = math.exp(x)
    if x > 0:
        main_term = ex / x
    else:
        main_term = 0.0

    # Count
    max_r = max(shadow_coeffs.keys())
    upper = min(int(math.floor(ex)), max_r)
    actual_count = sum(1 for r in range(2, upper + 1)
                       if abs(shadow_coeffs.get(r, 0.0)) > 1e-300)

    # Oscillatory error from zeros
    osc_error = 0.0
    for rho in zeros:
        if abs(rho) > 1e-300:
            contrib = cmath.exp(rho * x) / rho
            osc_error += contrib.real  # Take real part

    return {
        'actual_count': float(actual_count),
        'main_term': main_term,
        'oscillatory_error': osc_error,
        'remainder': actual_count - main_term - osc_error,
    }


# ============================================================================
# 11.  Kuznetsov formula
# ============================================================================

def kuznetsov_spectral_side(
    zeros: List[complex],
    m: int,
    n: int,
) -> complex:
    r"""sum_rho a_rho(m) conj(a_rho(n)) where a_rho(m) = m^{-rho}.

    The spectral side of the Kuznetsov formula.
    """
    total = 0.0 + 0.0j
    for rho in zeros:
        a_m = m ** (-rho)  # m^{-rho} as complex number
        a_n_conj = n ** (-rho.conjugate())  # conj(n^{-rho}) = n^{-conj(rho)}
        total += a_m * a_n_conj
    return total


def kuznetsov_geometric_side(
    shadow_coeffs: Dict[int, float],
    m: int,
    n: int,
    max_r: Optional[int] = None,
) -> float:
    r"""Geometric side involving S_m, S_n.

    A naive shadow Kuznetsov: sum_r S_r * delta_{r=lcm(m,n)} * multiplicity
    More generally: cross-correlation of shadow coefficients weighted by
    the Bessel-type kernel.

    For the simplest form: sum_r S_r * r^{-s} evaluated at specific values
    pairing m and n.  We use the bilinear form:

        K(m,n) = S_m * S_n / S_2  (normalized bilinear pairing)

    as the geometric-side proxy.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Sm = shadow_coeffs.get(m, 0.0)
    Sn = shadow_coeffs.get(n, 0.0)
    S2 = shadow_coeffs.get(2, 0.0)
    if abs(S2) < 1e-300:
        return 0.0
    return Sm * Sn / S2


def kuznetsov_diagonal(
    zeros: List[complex],
    m: int,
) -> float:
    r"""Diagonal Kuznetsov: sum_rho |a_rho(m)|^2 = sum_rho m^{-2*Re(rho)}.

    This is always real and non-negative.
    """
    total = 0.0
    for rho in zeros:
        total += m ** (-2.0 * rho.real)
    return total


# ============================================================================
# 12.  Relative trace formula (Koszul pairs)
# ============================================================================

def relative_trace_spectral(
    zeros_A: List[complex],
    zeros_dual: List[complex],
    test_fn: Callable[[complex], complex],
) -> complex:
    r"""Relative spectral sum: sum_rho h(rho) over SHARED zeros.

    For Virasoro (c, 26-c): shared zeros = zeros of zeta_D = zeta_c + zeta_{26-c}.
    """
    spec_A = spectral_sum(zeros_A, test_fn)
    spec_dual = spectral_sum(zeros_dual, test_fn)
    return spec_A + spec_dual


def relative_trace_geometric(
    shadow_coeffs: Dict[int, float],
    shadow_dual_coeffs: Dict[int, float],
    test_fn_fourier: Callable[[float], float],
    max_r: Optional[int] = None,
) -> float:
    r"""Relative geometric sum: sum_r [S_r(A) + S_r(A!)] * h_hat(log r).

    For complementary pairs, this is the zeta_D geometric side.
    """
    if max_r is None:
        max_r = max(max(shadow_coeffs.keys()), max(shadow_dual_coeffs.keys()))
    total = 0.0
    for r in range(2, max_r + 1):
        Sr_A = shadow_coeffs.get(r, 0.0)
        Sr_dual = shadow_dual_coeffs.get(r, 0.0)
        D_r = Sr_A + Sr_dual
        if abs(D_r) < 1e-300:
            continue
        total += D_r * test_fn_fourier(math.log(r))
    return total


def relative_trace_asymmetry(
    shadow_coeffs: Dict[int, float],
    shadow_dual_coeffs: Dict[int, float],
    test_fn_fourier: Callable[[float], float],
    max_r: Optional[int] = None,
) -> float:
    r"""Asymmetry: sum_r [S_r(A) - S_r(A!)] * h_hat(log r).

    Measures the deviation from self-duality.
    At c = 13: this should vanish (Virasoro is self-dual).
    """
    if max_r is None:
        max_r = max(max(shadow_coeffs.keys()), max(shadow_dual_coeffs.keys()))
    total = 0.0
    for r in range(2, max_r + 1):
        Sr_A = shadow_coeffs.get(r, 0.0)
        Sr_dual = shadow_dual_coeffs.get(r, 0.0)
        diff = Sr_A - Sr_dual
        if abs(diff) < 1e-300:
            continue
        total += diff * test_fn_fourier(math.log(r))
    return total


# ============================================================================
# 13.  Self-duality enhanced symmetry (c = 13)
# ============================================================================

def self_dual_symmetry_test(
    c_val: float = 13.0,
    max_r: int = 50,
    sigmas: Optional[List[float]] = None,
) -> Dict[str, float]:
    r"""At c = 13 (Virasoro self-dual point), test enhanced symmetry.

    S_r(Vir_13) = S_r(Vir_{26-13}) = S_r(Vir_13).
    The asymmetry trace should vanish identically.
    kappa + kappa' = 13/2 + 13/2 = 13 (consistent with AP24).
    """
    if sigmas is None:
        sigmas = [1.0, 2.0, 5.0, 10.0]

    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    dual_coeffs = virasoro_shadow_coefficients(26.0 - c_val, max_r)

    results = {}

    # Coefficient-level test
    max_diff = 0.0
    for r in range(2, max_r + 1):
        diff = abs(coeffs.get(r, 0.0) - dual_coeffs.get(r, 0.0))
        max_diff = max(max_diff, diff)
    results['max_coefficient_diff'] = max_diff

    # kappa sum
    kappa = coeffs.get(2, 0.0)
    kappa_dual = dual_coeffs.get(2, 0.0)
    results['kappa_sum'] = kappa + kappa_dual
    results['kappa_sum_expected'] = 13.0

    # Trace asymmetry
    for sigma in sigmas:
        asym = relative_trace_asymmetry(
            coeffs, dual_coeffs,
            lambda t: gaussian_fourier(t, sigma),
            max_r,
        )
        results[f'asymmetry_sigma_{sigma}'] = asym

    return results


# ============================================================================
# 14.  Comprehensive trace formula comparison
# ============================================================================

@dataclass
class FullTraceFormulaComparison:
    """Full trace formula comparison results for a Virasoro algebra."""
    c_val: float
    kappa: float
    n_zeros: int
    gaussian_results: List[TraceFormulaResult]
    lorentzian_results: List[TraceFormulaResult]
    heat_weyl_coeffs: Dict[str, float]
    prime_geodesic: Dict[float, int]
    self_dual_test: Optional[Dict[str, float]]


def full_comparison(
    c_val: float,
    max_r: int = 60,
    n_zeros: int = 50,
    sigmas: Optional[List[float]] = None,
    lorentzian_as: Optional[List[float]] = None,
) -> FullTraceFormulaComparison:
    """Run the full trace formula comparison for Virasoro at central charge c.

    Parameters
    ----------
    c_val : central charge
    max_r : maximum arity for shadow coefficients
    n_zeros : target number of zeros to find
    sigmas : Gaussian widths to test
    lorentzian_as : Lorentzian parameters to test
    """
    if sigmas is None:
        sigmas = [1.0, 2.0, 5.0, 10.0]
    if lorentzian_as is None:
        lorentzian_as = [1.0, 2.0, 5.0]

    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    kappa = coeffs.get(2, 0.0)

    # Find zeros
    zeros = get_shadow_zeros('virasoro', c_val, n_zeros, max_r)

    # Gaussian trace formula
    gauss_results = []
    for sigma in sigmas:
        res = trace_formula_gaussian(coeffs, zeros, sigma, max_r)
        gauss_results.append(res)

    # Lorentzian trace formula
    lor_results = []
    for a in lorentzian_as:
        res = trace_formula_lorentzian(coeffs, zeros, a, max_r)
        lor_results.append(res)

    # Heat kernel Weyl law
    t_values = list(np.linspace(0.01, 0.5, 20))
    weyl_coeffs = heat_kernel_weyl_coefficients(zeros, t_values)

    # Prime geodesic counting
    x_values = [1.0, 2.0, 3.0, 4.0]
    pgc = prime_geodesic_counting(coeffs, x_values)

    # Self-dual test if c = 13
    sd_test = None
    if abs(c_val - 13.0) < 1e-10:
        sd_test = self_dual_symmetry_test(c_val, max_r)

    return FullTraceFormulaComparison(
        c_val=c_val,
        kappa=kappa,
        n_zeros=len(zeros),
        gaussian_results=gauss_results,
        lorentzian_results=lor_results,
        heat_weyl_coeffs=weyl_coeffs,
        prime_geodesic=pgc,
        self_dual_test=sd_test,
    )


# ============================================================================
# 15.  Complementarity trace formula sum D_r = S_r(c) + S_r(26-c)
# ============================================================================

def complementarity_sum_coefficients(
    c_val: float,
    max_r: int = 50,
) -> Dict[int, float]:
    r"""D_r(c) = S_r(Vir_c) + S_r(Vir_{26-c}).

    The complementarity sum of shadow coefficients.
    At r=2: D_2 = kappa + kappa' = c/2 + (26-c)/2 = 13 (AP24).
    """
    coeffs = virasoro_shadow_coefficients(c_val, max_r)
    dual_coeffs = virasoro_shadow_coefficients(26.0 - c_val, max_r)

    D = {}
    for r in range(2, max_r + 1):
        D[r] = coeffs.get(r, 0.0) + dual_coeffs.get(r, 0.0)
    return D


def complementarity_trace_formula(
    c_val: float,
    sigma: float = 2.0,
    max_r: int = 50,
    n_zeros: int = 50,
) -> Dict[str, float]:
    r"""Trace formula for the complementarity Dirichlet series zeta_D.

    zeta_D(s) = zeta_c(s) + zeta_{26-c}(s) = sum D_r * r^{-s}.

    The zeros of zeta_D include the shared zeros of the Koszul pair.
    """
    D_coeffs = complementarity_sum_coefficients(c_val, max_r)

    # Find zeros of zeta_D
    D_zeros = find_zeros_grid(
        D_coeffs,
        re_range=(-10.0, 10.0),
        im_range=(-100.0, 100.0),
        grid_re=20,
        grid_im=200,
        max_r=max_r,
    )

    spec = spectral_sum_gaussian(D_zeros, sigma)
    geom = geometric_sum_gaussian(D_coeffs, sigma, max_r)

    return {
        'D_2': D_coeffs.get(2, 0.0),
        'D_2_expected': 13.0,
        'n_D_zeros': len(D_zeros),
        'spectral_sum': spec.real,
        'geometric_sum': geom,
        'relative_error': abs(spec.real - geom) / max(abs(geom), abs(spec.real), 1e-15),
    }
