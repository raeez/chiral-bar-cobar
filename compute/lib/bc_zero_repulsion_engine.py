r"""Zero repulsion and Deuring-Heilbronn phenomenon for shadow zeta functions.

The Deuring-Heilbronn phenomenon: if an L-function has a real zero beta
close to s=1, then ALL other zeros are pushed away from the 1-line.
For shadow zeta zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}, we investigate:

1. EXCEPTIONAL ZEROS:  For Virasoro at c near 0 or 26, kappa(Vir_c) = c/2
   is small, so zeta_A has small leading coefficient.  Does this produce a
   "Siegel zero" -- a real zero near the edge of the critical strip?

2. ZERO REPULSION QUANTIFICATION:  For each pair of adjacent zeros rho_n,
   rho_{n+1}, compute the repulsion distance |rho_{n+1} - rho_n| as a
   function of Im(rho_n).  Compare with GUE prediction: nearest-neighbor
   spacing ~ Wigner surmise p(s) = (32/pi^2) s^2 exp(-4s^2/pi).

3. COMPLEMENTARITY REPULSION:  At the self-dual point c=13,
   zeta_{Vir_13}(s) = zeta_D(s)/2.  The zeros are symmetric under
   c -> 26-c.  Does self-duality ENHANCE or REDUCE repulsion?

4. ZERO CLUSTERING:  At s = 1/2 + i*gamma where gamma = 14.134...
   (first Riemann zero), do shadow zeros cluster?

5. REPULSION BY SHADOW DEPTH:  Class G (no zeros for k>0), class L
   (isolated zeros on vertical lines), class C (finitely many zeros),
   class M (infinitely many zeros).

MATHEMATICAL FRAMEWORK:

The Deuring-Heilbronn repulsion distance for a zero beta_0 near s=1 is:
    d(beta_0) >= C / log(1 / (1 - beta_0))
where C is an effective constant.  For shadow zeta, the analogous
phenomenon occurs when kappa(A) = S_2(A) is small relative to S_3, S_4, ...
because the leading term kappa * 2^{-s} is small and the higher-arity
terms dominate, potentially creating a real zero near the abscissa.

VERIFICATION PATHS (Multi-Path Verification Mandate):
    1. Direct zero-finding via Newton-Raphson
    2. Argument principle contour integral for zero counting
    3. Cross-check via complementarity: zeros of zeta_c and zeta_{26-c}
    4. Statistical tests (Kolmogorov-Smirnov against GUE/Poisson)
    5. Monotonicity checks: repulsion varies smoothly with c

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify zeros by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP31): kappa = 0 does NOT imply Theta_A = 0.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

# ---------------------------------------------------------------------------
# Import infrastructure from existing engines
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

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    newton_zero,
    muller_zero,
    find_zeros_grid,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
    _deduplicate_zeros,
    affine_sl2_zeros,
    affine_sl3_zeros,
    heisenberg_zeros,
    betagamma_zeros_numerical,
    argument_principle_count,
)


# ============================================================================
# 1.  Shadow zeta evaluation helpers
# ============================================================================

def shadow_zeta_real_line(
    shadow_coeffs: Dict[int, float],
    sigma: float,
    max_r: Optional[int] = None,
) -> float:
    """Evaluate zeta_A(sigma) on the real line (s = sigma + 0i).

    Returns a real number (the imaginary part is zero for real s
    when all S_r are real).
    """
    val = _shadow_zeta_complex(shadow_coeffs, complex(sigma, 0), max_r)
    return val.real


def shadow_zeta_log_derivative(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute the logarithmic derivative zeta'/zeta at s.

    Returns zeta_A'(s) / zeta_A(s).  Used for Newton refinement and
    the argument principle.
    """
    f = _shadow_zeta_complex(shadow_coeffs, s, max_r)
    fp = _shadow_zeta_derivative(shadow_coeffs, s, max_r)
    if abs(f) < 1e-300:
        return complex(float('inf'), 0)
    return fp / f


# ============================================================================
# 2.  Exceptional zero (Siegel zero) analysis
# ============================================================================

def find_real_zeros_brentq(
    shadow_coeffs: Dict[int, float],
    sigma_lo: float = -20.0,
    sigma_hi: float = 20.0,
    n_scan: int = 2000,
    tol: float = 1e-12,
    max_r: Optional[int] = None,
) -> List[float]:
    r"""Find real zeros of zeta_A(sigma) via sign-change scanning + bisection.

    Scans the interval [sigma_lo, sigma_hi] for sign changes of the real
    function sigma -> zeta_A(sigma), then refines each bracket via bisection
    (Brent's method without scipy dependency).

    Returns sorted list of real zeros.
    """
    step = (sigma_hi - sigma_lo) / n_scan
    prev_val = shadow_zeta_real_line(shadow_coeffs, sigma_lo, max_r)
    zeros = []

    for i in range(1, n_scan + 1):
        sigma = sigma_lo + i * step
        curr_val = shadow_zeta_real_line(shadow_coeffs, sigma, max_r)

        if prev_val * curr_val < 0:
            # Sign change: bisect to find the zero
            a, b = sigma - step, sigma
            fa, fb = prev_val, curr_val
            for _ in range(100):
                mid = (a + b) / 2.0
                fm = shadow_zeta_real_line(shadow_coeffs, mid, max_r)
                if abs(fm) < tol or (b - a) / 2.0 < tol:
                    zeros.append(mid)
                    break
                if fa * fm < 0:
                    b, fb = mid, fm
                else:
                    a, fa = mid, fm
            else:
                zeros.append((a + b) / 2.0)

        prev_val = curr_val

    return sorted(zeros)


def rightmost_real_zero(
    shadow_coeffs: Dict[int, float],
    sigma_lo: float = -20.0,
    sigma_hi: float = 20.0,
    n_scan: int = 2000,
    tol: float = 1e-12,
    max_r: Optional[int] = None,
) -> Optional[float]:
    """Find the rightmost real zero of zeta_A(sigma).

    Returns None if no real zero is found in [sigma_lo, sigma_hi].
    """
    zeros = find_real_zeros_brentq(shadow_coeffs, sigma_lo, sigma_hi, n_scan, tol, max_r)
    if not zeros:
        return None
    return max(zeros)


def exceptional_zero_scan(
    c_values: List[float],
    max_r: int = 50,
    sigma_lo: float = -20.0,
    sigma_hi: float = 20.0,
) -> Dict[float, Optional[float]]:
    r"""Scan for the rightmost real zero of zeta_{Vir_c} across c values.

    For c near 0 or 26, kappa is small and a "Siegel zero" may appear
    near the right edge of the convergence region.

    Returns dict mapping c to the rightmost real zero (None if no real
    zeros exist in the scan range).
    """
    result = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            rz = rightmost_real_zero(coeffs, sigma_lo, sigma_hi, max_r=max_r)
            result[c_val] = rz
        except (ValueError, ZeroDivisionError):
            result[c_val] = None
    return result


def siegel_zero_distance(
    shadow_coeffs: Dict[int, float],
    abscissa_estimate: float = 0.0,
    max_r: Optional[int] = None,
) -> Optional[float]:
    """Distance from the rightmost real zero to the abscissa of convergence.

    A small distance indicates a Siegel-type exceptional zero.
    Returns None if no real zero is found.
    """
    rz = rightmost_real_zero(shadow_coeffs, sigma_lo=-30.0, sigma_hi=30.0, max_r=max_r)
    if rz is None:
        return None
    return rz - abscissa_estimate


# ============================================================================
# 3.  Zero repulsion: nearest-neighbor spacing statistics
# ============================================================================

@dataclass
class ZeroSpacingData:
    """Container for nearest-neighbor spacing statistics of shadow zeros."""
    family: str
    param: float
    zeros: List[complex]
    spacings: List[float]           # |rho_{n+1} - rho_n| for adjacent zeros
    normalized_spacings: List[float] # spacings / mean_spacing
    mean_spacing: float
    min_spacing: float
    max_spacing: float
    spacing_variance: float
    n_zeros: int


def compute_nn_spacings(
    zeros: List[complex],
    sort_by_imag: bool = True,
) -> List[float]:
    r"""Compute nearest-neighbor spacings for a list of zeros.

    Sorts zeros by imaginary part (optionally), then computes
    |rho_{n+1} - rho_n| for consecutive zeros.

    Parameters
    ----------
    zeros : list of complex zeros
    sort_by_imag : if True, sort by Im(s) before computing spacings.
        For zeros on a vertical line, this gives the natural ordering.

    Returns
    -------
    List of nearest-neighbor spacings.
    """
    if len(zeros) < 2:
        return []

    if sort_by_imag:
        sorted_zeros = sorted(zeros, key=lambda z: z.imag)
    else:
        sorted_zeros = list(zeros)

    spacings = []
    for i in range(len(sorted_zeros) - 1):
        gap = abs(sorted_zeros[i + 1] - sorted_zeros[i])
        spacings.append(gap)

    return spacings


def compute_spacing_statistics(
    family: str,
    param: float,
    zeros: List[complex],
) -> ZeroSpacingData:
    """Compute full nearest-neighbor spacing statistics for a set of zeros."""
    spacings = compute_nn_spacings(zeros)
    if not spacings:
        return ZeroSpacingData(
            family=family, param=param, zeros=zeros,
            spacings=[], normalized_spacings=[],
            mean_spacing=0.0, min_spacing=0.0, max_spacing=0.0,
            spacing_variance=0.0, n_zeros=len(zeros),
        )

    mean_s = sum(spacings) / len(spacings)
    if mean_s > 0:
        normalized = [s / mean_s for s in spacings]
    else:
        normalized = spacings[:]

    var_s = sum((s - mean_s) ** 2 for s in spacings) / len(spacings)

    return ZeroSpacingData(
        family=family,
        param=param,
        zeros=zeros,
        spacings=spacings,
        normalized_spacings=normalized,
        mean_spacing=mean_s,
        min_spacing=min(spacings),
        max_spacing=max(spacings),
        spacing_variance=var_s,
        n_zeros=len(zeros),
    )


def wigner_surmise_gue(s: float) -> float:
    r"""GUE Wigner surmise: p(s) = (32/pi^2) s^2 exp(-4 s^2 / pi).

    This is the nearest-neighbor spacing distribution for GUE random
    matrices.  It applies to zeros of L-functions with unitary symmetry.
    """
    return (32.0 / (math.pi ** 2)) * s ** 2 * math.exp(-4.0 * s ** 2 / math.pi)


def wigner_surmise_goe(s: float) -> float:
    r"""GOE Wigner surmise: p(s) = (pi/2) s exp(-pi s^2 / 4).

    This is the nearest-neighbor spacing distribution for GOE random
    matrices.  It applies to L-functions with orthogonal symmetry.
    """
    return (math.pi / 2.0) * s * math.exp(-math.pi * s ** 2 / 4.0)


def poisson_spacing(s: float) -> float:
    r"""Poisson spacing distribution: p(s) = exp(-s).

    This is the nearest-neighbor spacing distribution for uncorrelated
    (independent) levels.
    """
    return math.exp(-s)


def wigner_surmise_cdf_gue(s: float) -> float:
    r"""CDF of the GUE Wigner surmise: P(gap > x) = 1 - CDF(x).

    CDF(s) = 1 - exp(-4 s^2 / pi).
    The Wigner surmise is an approximation; the exact CDF is more complex
    but this suffices for statistical comparison.
    """
    return 1.0 - math.exp(-4.0 * s ** 2 / math.pi)


def gap_exceedance_distribution(
    normalized_spacings: List[float],
    x_values: List[float],
) -> Dict[float, float]:
    """Compute P(gap > x) for a list of x values.

    Parameters
    ----------
    normalized_spacings : list of normalized spacings s/mean
    x_values : threshold values at which to compute exceedance

    Returns
    -------
    Dict mapping x to P(gap > x) = fraction of spacings exceeding x.
    """
    n = len(normalized_spacings)
    if n == 0:
        return {x: 0.0 for x in x_values}

    result = {}
    for x in x_values:
        count = sum(1 for s in normalized_spacings if s > x)
        result[x] = count / n
    return result


# ============================================================================
# 4.  Level spacing variance (number variance)
# ============================================================================

def number_variance(
    zeros: List[complex],
    L_values: List[float],
    T_center: Optional[float] = None,
    n_windows: int = 50,
) -> Dict[float, float]:
    r"""Compute the level spacing variance Sigma_2(L).

    Sigma_2(L) = Var(N(t+L) - N(t)) / E[N(t+L) - N(t)]

    where N(t) counts zeros with Im(rho) < t.

    For GUE: Sigma_2(L) ~ (2/pi^2) * (log(2*pi*L) + gamma_E + 1 - pi^2/8)
    For Poisson: Sigma_2(L) = L

    Parameters
    ----------
    zeros : list of complex zeros
    L_values : list of window sizes L to test
    T_center : center of the sampling region (default: median of Im parts)
    n_windows : number of sampling windows per L

    Returns
    -------
    Dict mapping L to Sigma_2(L).
    """
    if len(zeros) < 3:
        return {L: 0.0 for L in L_values}

    # Extract imaginary parts and sort
    gammas = sorted([z.imag for z in zeros])

    if T_center is None:
        T_center = gammas[len(gammas) // 2]

    result = {}
    for L in L_values:
        counts = []
        # Sample windows [t, t+L] for various t
        t_lo = T_center - n_windows * L / 2
        for i in range(n_windows):
            t = t_lo + i * L
            # Count zeros in [t, t+L]
            count = sum(1 for g in gammas if t <= g < t + L)
            counts.append(count)

        if not counts:
            result[L] = 0.0
            continue

        mean_c = sum(counts) / len(counts)
        if mean_c == 0:
            result[L] = 0.0
            continue

        var_c = sum((c - mean_c) ** 2 for c in counts) / len(counts)
        result[L] = var_c / mean_c

    return result


def gue_number_variance(L: float) -> float:
    r"""GUE prediction for the number variance:

    Sigma_2^{GUE}(L) ~ (2/pi^2) * (log(2*pi*L) + gamma_E + 1 - pi^2/8)

    for large L.  gamma_E = 0.5772156649... is the Euler-Mascheroni constant.
    """
    if L <= 0:
        return 0.0
    gamma_E = 0.5772156649015329
    return (2.0 / (math.pi ** 2)) * (
        math.log(2.0 * math.pi * L) + gamma_E + 1.0 - math.pi ** 2 / 8.0
    )


def poisson_number_variance(L: float) -> float:
    r"""Poisson prediction: Sigma_2^{Poisson}(L) = L."""
    return L


# ============================================================================
# 5.  Complementarity repulsion analysis
# ============================================================================

def complementarity_zero_relation(
    c_val: float,
    max_r: int = 50,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 80,
) -> Dict[str, Any]:
    r"""Analyze the complementarity relation on zeros.

    For Virasoro: zeta_{Vir_c}(s) + zeta_{Vir_{26-c}}(s) = zeta_D(s)

    At c=13 (self-dual): zeta_D(s) = 2 * zeta_{Vir_13}(s).

    Returns a dict with:
        'zeros_c' : zeros of zeta_{Vir_c}
        'zeros_dual' : zeros of zeta_{Vir_{26-c}}
        'zeros_sum' : zeros of the complementarity sum zeta_D
        'interleaving_score' : measure of how well zeros interleave
    """
    c_dual = 26.0 - c_val

    coeffs_c = virasoro_shadow_coefficients_numerical(c_val, max_r)
    try:
        coeffs_dual = virasoro_shadow_coefficients_numerical(c_dual, max_r)
    except (ValueError, ZeroDivisionError):
        return {
            'zeros_c': [],
            'zeros_dual': [],
            'zeros_sum': [],
            'interleaving_score': 0.0,
        }

    # Complementarity sum coefficients: D_r = S_r(c) + S_r(26-c)
    max_arity = max(max(coeffs_c.keys()), max(coeffs_dual.keys()))
    coeffs_sum = {}
    for r in range(2, max_arity + 1):
        coeffs_sum[r] = coeffs_c.get(r, 0.0) + coeffs_dual.get(r, 0.0)

    zeros_c = find_zeros_grid(
        coeffs_c, re_range, im_range, grid_re, grid_im, max_r=max_r
    )
    zeros_dual = find_zeros_grid(
        coeffs_dual, re_range, im_range, grid_re, grid_im, max_r=max_r
    )
    zeros_sum = find_zeros_grid(
        coeffs_sum, re_range, im_range, grid_re, grid_im, max_r=max_r
    )

    # Interleaving: for zeros on a common vertical line, measure how well
    # the zeros of zeta_c and zeta_{26-c} alternate
    interleaving = _interleaving_score(zeros_c, zeros_dual)

    return {
        'zeros_c': zeros_c,
        'zeros_dual': zeros_dual,
        'zeros_sum': zeros_sum,
        'interleaving_score': interleaving,
    }


def _interleaving_score(
    zeros_a: List[complex],
    zeros_b: List[complex],
    tol: float = 0.5,
) -> float:
    r"""Compute interleaving score for two zero sets.

    Score 1.0 = perfectly interleaved (every zero of A has a zero of B
    between it and the next zero of A).  Score 0.0 = no interleaving.

    We measure this on zeros with similar real parts (within tol).
    """
    if len(zeros_a) < 2 or len(zeros_b) < 2:
        return 0.0

    # Filter to zeros near the same vertical line
    re_a = [z.real for z in zeros_a]
    re_b = [z.real for z in zeros_b]
    if not re_a or not re_b:
        return 0.0

    # Use the median real part as the reference line
    median_re = (sum(re_a) / len(re_a) + sum(re_b) / len(re_b)) / 2.0

    near_a = sorted([z.imag for z in zeros_a if abs(z.real - median_re) < tol])
    near_b = sorted([z.imag for z in zeros_b if abs(z.real - median_re) < tol])

    if len(near_a) < 2 or not near_b:
        return 0.0

    interleaved = 0
    total = 0
    for i in range(len(near_a) - 1):
        lo, hi = near_a[i], near_a[i + 1]
        # Count B-zeros in (lo, hi)
        between = sum(1 for b in near_b if lo < b < hi)
        if between > 0:
            interleaved += 1
        total += 1

    return interleaved / total if total > 0 else 0.0


def self_dual_repulsion_enhancement(
    c_values: List[float],
    max_r: int = 50,
    im_range: Tuple[float, float] = (-80.0, 80.0),
) -> Dict[float, float]:
    r"""Measure repulsion strength as a function of c.

    For each c, computes the mean normalized spacing of the first few
    zeros of zeta_{Vir_c}(s).  At the self-dual point c=13, the
    functional equation may enhance or reduce repulsion.

    Returns dict mapping c to mean_normalized_spacing.
    """
    result = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            zeros = find_zeros_grid(
                coeffs, re_range=(-5.0, 5.0), im_range=im_range,
                grid_re=15, grid_im=60, max_r=max_r
            )
            stats = compute_spacing_statistics('virasoro', c_val, zeros)
            result[c_val] = stats.mean_spacing
        except (ValueError, ZeroDivisionError):
            result[c_val] = 0.0
    return result


# ============================================================================
# 6.  Zero clustering near special imaginary parts
# ============================================================================

FIRST_RIEMANN_ZERO_GAMMA = 14.134725141734693

def cluster_score_near_height(
    zeros: List[complex],
    target_gamma: float,
    window: float = 1.0,
) -> float:
    r"""Count the density of shadow zeros near a target imaginary part.

    Returns the number of zeros with |Im(rho) - target_gamma| < window,
    normalized by the expected density (total zeros / total height range).

    A score > 1 indicates clustering; score < 1 indicates avoidance.
    """
    if len(zeros) < 2:
        return 0.0

    gammas = [z.imag for z in zeros]
    gamma_range = max(gammas) - min(gammas)
    if gamma_range <= 0:
        return 0.0

    # Expected density: n_zeros / range
    expected_density = len(zeros) / gamma_range

    # Count zeros near target
    near_count = sum(1 for g in gammas if abs(g - target_gamma) < window)

    # Observed density: near_count / (2 * window)
    observed_density = near_count / (2.0 * window)

    return observed_density / expected_density if expected_density > 0 else 0.0


def riemann_zero_clustering(
    shadow_coeffs: Dict[int, float],
    riemann_gammas: Optional[List[float]] = None,
    window: float = 1.0,
    max_r: Optional[int] = None,
    im_range: Tuple[float, float] = (-100.0, 100.0),
) -> Dict[float, float]:
    r"""Test whether shadow zeros cluster near Riemann zero heights.

    If zeta^{DK}_{sl_2}(s) = zeta(s) (categorical zeta connection), then
    sl_2 shadow zeros ARE Riemann zeros.  For Virasoro (different algebra),
    the zeros should be INDEPENDENT.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dict
    riemann_gammas : list of Im parts of Riemann zeros to test.
        Default: first 5 Riemann zeros.
    window : half-width of clustering window
    max_r : truncation arity
    im_range : range for zero search

    Returns
    -------
    Dict mapping gamma to cluster_score.
    """
    if riemann_gammas is None:
        riemann_gammas = [
            14.134725141734693,
            21.022039638771555,
            25.010857580145688,
            30.424876125859513,
            32.935061587739189,
        ]

    zeros = find_zeros_grid(
        shadow_coeffs,
        re_range=(-5.0, 5.0),
        im_range=im_range,
        grid_re=15,
        grid_im=80,
        max_r=max_r,
    )

    result = {}
    for gamma in riemann_gammas:
        result[gamma] = cluster_score_near_height(zeros, gamma, window)
    return result


# ============================================================================
# 7.  Repulsion as a function of shadow depth
# ============================================================================

@dataclass
class DepthRepulsionData:
    """Repulsion statistics for a specific shadow depth class."""
    shadow_class: str    # G, L, C, M
    family: str
    param: float
    n_zeros: int
    has_zeros: bool
    mean_spacing: float
    min_spacing: float
    max_spacing: float
    spacing_variance: float
    spacings: List[float] = field(default_factory=list)


def class_g_repulsion(k_val: float = 1.0) -> DepthRepulsionData:
    """Repulsion for class G (Heisenberg): no zeros for k > 0.

    The Heisenberg shadow zeta zeta_{H_k}(s) = k * 2^{-s} has no zeros
    for k != 0 (exponential function is never zero).
    """
    return DepthRepulsionData(
        shadow_class='G',
        family='heisenberg',
        param=k_val,
        n_zeros=0,
        has_zeros=False,
        mean_spacing=float('inf'),
        min_spacing=float('inf'),
        max_spacing=0.0,
        spacing_variance=0.0,
    )


def class_l_repulsion(
    k_val: float = 1.0,
    algebra: str = 'sl2',
    n_max: int = 50,
) -> DepthRepulsionData:
    r"""Repulsion for class L (affine KM): isolated zeros on vertical lines.

    For affine sl_2: zeros at s = -(log(kappa/alpha) + i*pi*(2n+1)) / log(3/2).
    These lie on a SINGLE vertical line.  The spacing is uniform:
        |rho_{n+1} - rho_n| = 2*pi / log(3/2) for all n.

    Returns repulsion data with uniform spacing.
    """
    if algebra == 'sl2':
        zeros = affine_sl2_zeros(k_val, n_max)
    elif algebra == 'sl3':
        zeros = affine_sl3_zeros(k_val, n_max)
    else:
        raise ValueError(f"Unknown algebra: {algebra}")

    stats = compute_spacing_statistics(f'affine_{algebra}', k_val, zeros)

    return DepthRepulsionData(
        shadow_class='L',
        family=f'affine_{algebra}',
        param=k_val,
        n_zeros=len(zeros),
        has_zeros=len(zeros) > 0,
        mean_spacing=stats.mean_spacing,
        min_spacing=stats.min_spacing,
        max_spacing=stats.max_spacing,
        spacing_variance=stats.spacing_variance,
        spacings=stats.spacings,
    )


def class_c_repulsion(
    lam_val: float = 0.5,
    re_range: Tuple[float, float] = (-10.0, 10.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
) -> DepthRepulsionData:
    r"""Repulsion for class C (beta-gamma): finitely many zeros.

    The beta-gamma shadow zeta is a 3-term exponential polynomial:
        zeta(s) = S_2 * 2^{-s} + S_3 * 3^{-s} + S_4 * 4^{-s}

    This has infinitely many zeros (on quasi-periodic vertical lines),
    but the algebraic structure is simpler than class M.
    """
    zeros = betagamma_zeros_numerical(lam_val, re_range, im_range)
    stats = compute_spacing_statistics('betagamma', lam_val, zeros)

    return DepthRepulsionData(
        shadow_class='C',
        family='betagamma',
        param=lam_val,
        n_zeros=len(zeros),
        has_zeros=len(zeros) > 0,
        mean_spacing=stats.mean_spacing,
        min_spacing=stats.min_spacing,
        max_spacing=stats.max_spacing,
        spacing_variance=stats.spacing_variance,
        spacings=stats.spacings,
    )


def class_m_repulsion(
    c_val: float = 1.0,
    max_r: int = 50,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-80.0, 80.0),
    grid_re: int = 15,
    grid_im: int = 60,
) -> DepthRepulsionData:
    r"""Repulsion for class M (Virasoro, W_N): infinitely many zeros.

    The shadow zeta is an infinite Dirichlet series whose zeros
    (when the series is entire, i.e. rho < 1) form an infinite set.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r
    )
    stats = compute_spacing_statistics('virasoro', c_val, zeros)

    return DepthRepulsionData(
        shadow_class='M',
        family='virasoro',
        param=c_val,
        n_zeros=len(zeros),
        has_zeros=len(zeros) > 0,
        mean_spacing=stats.mean_spacing,
        min_spacing=stats.min_spacing,
        max_spacing=stats.max_spacing,
        spacing_variance=stats.spacing_variance,
        spacings=stats.spacings,
    )


def repulsion_by_depth_class(
    max_r: int = 50,
) -> Dict[str, DepthRepulsionData]:
    r"""Compute repulsion statistics for each shadow depth class.

    Uses canonical representatives:
        G: Heisenberg k=1
        L: affine sl_2 k=1
        C: beta-gamma lambda=1/2
        M: Virasoro c=1
    """
    return {
        'G': class_g_repulsion(1.0),
        'L': class_l_repulsion(1.0, 'sl2'),
        'C': class_c_repulsion(0.5),
        'M': class_m_repulsion(1.0, max_r),
    }


# ============================================================================
# 8.  Statistical tests: KS test against GUE/Poisson
# ============================================================================

def ks_test_against_distribution(
    normalized_spacings: List[float],
    reference_cdf: Callable[[float], float],
) -> Tuple[float, float]:
    r"""Kolmogorov-Smirnov test of normalized spacings against a reference CDF.

    Returns (D_n statistic, approximate p-value).

    D_n = max_x |F_empirical(x) - F_reference(x)|.

    The p-value is from the Kolmogorov distribution:
        P(D_n > x) ~ 2 * sum_{k=1}^{infty} (-1)^{k-1} exp(-2 k^2 n x^2)

    Parameters
    ----------
    normalized_spacings : list of spacings normalized to unit mean
    reference_cdf : CDF function for the reference distribution

    Returns
    -------
    (D_n, p_value) where D_n is the KS statistic and p_value is approximate.
    """
    if len(normalized_spacings) < 2:
        return (0.0, 1.0)

    sorted_data = sorted(normalized_spacings)
    n = len(sorted_data)

    d_max = 0.0
    for i, x in enumerate(sorted_data):
        ecdf = (i + 1) / n
        ecdf_prev = i / n
        ref = reference_cdf(x)
        d_max = max(d_max, abs(ecdf - ref), abs(ecdf_prev - ref))

    # Approximate p-value via Kolmogorov distribution
    sqrt_n = math.sqrt(n)
    lam = (sqrt_n + 0.12 + 0.11 / sqrt_n) * d_max
    if lam <= 0:
        return (d_max, 1.0)

    # K(lam) = 2 sum_{k=1}^inf (-1)^{k-1} exp(-2 k^2 lam^2)
    p_val = 0.0
    for k in range(1, 101):
        term = 2.0 * ((-1) ** (k - 1)) * math.exp(-2.0 * k ** 2 * lam ** 2)
        p_val += term
        if abs(term) < 1e-15:
            break

    p_val = max(0.0, min(1.0, p_val))
    return (d_max, p_val)


def poisson_cdf(x: float) -> float:
    """CDF of exponential distribution (Poisson spacing): 1 - exp(-x)."""
    if x < 0:
        return 0.0
    return 1.0 - math.exp(-x)


def ks_against_gue(normalized_spacings: List[float]) -> Tuple[float, float]:
    """KS test against GUE Wigner surmise CDF."""
    return ks_test_against_distribution(normalized_spacings, wigner_surmise_cdf_gue)


def ks_against_poisson(normalized_spacings: List[float]) -> Tuple[float, float]:
    """KS test against Poisson (exponential) CDF."""
    return ks_test_against_distribution(normalized_spacings, poisson_cdf)


# ============================================================================
# 9.  Repulsion as function of height (near-real-axis enhancement)
# ============================================================================

def repulsion_vs_height(
    zeros: List[complex],
    height_bins: Optional[List[float]] = None,
) -> Dict[float, float]:
    r"""Compute mean spacing as a function of height |Im(rho)|.

    For Riemann zeta, repulsion STRENGTHENS near the real axis (small
    imaginary parts have larger normalized spacings).  Test if shadow
    zeta shows the same behaviour.

    Parameters
    ----------
    zeros : list of complex zeros
    height_bins : bin edges for |Im(rho)|.  Default: [0, 5, 10, 20, 40, 80].

    Returns
    -------
    Dict mapping bin midpoint to mean spacing in that bin.
    """
    if height_bins is None:
        height_bins = [0.0, 5.0, 10.0, 20.0, 40.0, 80.0]

    if len(zeros) < 2:
        return {}

    sorted_zeros = sorted(zeros, key=lambda z: z.imag)
    spacings_with_heights = []
    for i in range(len(sorted_zeros) - 1):
        gap = abs(sorted_zeros[i + 1] - sorted_zeros[i])
        avg_height = (abs(sorted_zeros[i].imag) + abs(sorted_zeros[i + 1].imag)) / 2.0
        spacings_with_heights.append((avg_height, gap))

    result = {}
    for j in range(len(height_bins) - 1):
        lo, hi = height_bins[j], height_bins[j + 1]
        mid = (lo + hi) / 2.0
        bin_spacings = [gap for h, gap in spacings_with_heights if lo <= h < hi]
        if bin_spacings:
            result[mid] = sum(bin_spacings) / len(bin_spacings)
        else:
            result[mid] = 0.0

    return result


# ============================================================================
# 10. Deuring-Heilbronn repulsion bound
# ============================================================================

def deuring_heilbronn_bound(
    shadow_coeffs: Dict[int, float],
    beta_0: float,
    max_r: Optional[int] = None,
) -> float:
    r"""Estimate the Deuring-Heilbronn repulsion distance.

    If beta_0 is a real zero of zeta_A near the abscissa sigma_c,
    then other zeros are repelled by at least:
        d >= C / log(1 / |sigma_c - beta_0|)

    where C is an effective constant depending on the shadow tower.

    For shadow zeta, we estimate C from the ratio S_3 / S_2:
        C ~ 1 / (|S_3/S_2| * log(3/2))

    This is a HEURISTIC bound based on the two-term approximation.
    The real bound depends on the full Dirichlet series structure.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dict
    beta_0 : the exceptional real zero
    max_r : truncation arity

    Returns
    -------
    Estimated repulsion distance (lower bound on gap to next zero).
    """
    kappa = shadow_coeffs.get(2, 0.0)
    S3 = shadow_coeffs.get(3, 0.0)

    if abs(S3) < 1e-300 or abs(kappa) < 1e-300:
        return float('inf')

    ratio = abs(S3 / kappa)
    log_32 = math.log(3.0 / 2.0)

    # Effective constant
    C_eff = 1.0 / (ratio * log_32)

    # Compute distance from beta_0 to the zeta value edge
    zeta_at_beta = abs(shadow_zeta_real_line(shadow_coeffs, beta_0, max_r))
    if zeta_at_beta > 1e-6:
        # Not actually a zero: return 0
        return 0.0

    # Estimate the gap
    return C_eff


def repulsion_strength_vs_kappa(
    c_values: List[float],
    max_r: int = 50,
) -> Dict[float, float]:
    r"""Measure how repulsion strength varies with kappa.

    For each c, compute the minimum spacing among the first few zeros.
    Small kappa (c near 0 or 26) should show enhanced repulsion
    (Deuring-Heilbronn effect).

    Returns dict mapping c to min_spacing.
    """
    result = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            zeros = find_zeros_grid(
                coeffs, re_range=(-5.0, 5.0), im_range=(-50.0, 50.0),
                grid_re=12, grid_im=40, max_r=max_r
            )
            spacings = compute_nn_spacings(zeros)
            if spacings:
                result[c_val] = min(spacings)
            else:
                result[c_val] = float('inf')
        except (ValueError, ZeroDivisionError):
            result[c_val] = float('inf')
    return result


# ============================================================================
# 11. Monotonicity of repulsion statistics
# ============================================================================

def repulsion_monotonicity_test(
    c_values: List[float],
    max_r: int = 50,
    im_range: Tuple[float, float] = (-50.0, 50.0),
) -> Dict[str, Any]:
    r"""Test whether repulsion statistics vary smoothly with c.

    Computes mean_spacing and spacing_variance as functions of c,
    then checks smoothness via finite differences.

    Returns dict with:
        'c_values': the c values
        'mean_spacings': mean spacing at each c
        'variances': spacing variance at each c
        'mean_finite_diffs': finite differences of mean_spacing
        'is_smooth': True if no sudden jumps
    """
    means = []
    variances = []

    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
            zeros = find_zeros_grid(
                coeffs, re_range=(-5.0, 5.0), im_range=im_range,
                grid_re=12, grid_im=40, max_r=max_r
            )
            stats = compute_spacing_statistics('virasoro', c_val, zeros)
            means.append(stats.mean_spacing)
            variances.append(stats.spacing_variance)
        except (ValueError, ZeroDivisionError):
            means.append(float('nan'))
            variances.append(float('nan'))

    # Finite differences
    diffs = []
    for i in range(1, len(means)):
        if math.isfinite(means[i]) and math.isfinite(means[i - 1]):
            diffs.append(abs(means[i] - means[i - 1]))
        else:
            diffs.append(float('nan'))

    # Smoothness: no finite difference exceeds 10x the median
    finite_diffs = [d for d in diffs if math.isfinite(d) and d > 0]
    if finite_diffs:
        median_diff = sorted(finite_diffs)[len(finite_diffs) // 2]
        is_smooth = all(
            d < 10 * median_diff
            for d in finite_diffs
        )
    else:
        is_smooth = True

    return {
        'c_values': c_values,
        'mean_spacings': means,
        'variances': variances,
        'mean_finite_diffs': diffs,
        'is_smooth': is_smooth,
    }


# ============================================================================
# 12. Verification: argument principle cross-check
# ============================================================================

def verify_zero_count_argument_principle(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    n_points: int = 4000,
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Cross-check zero count from Newton search against argument principle.

    The argument principle gives the exact number of zeros in a rectangle.
    We compare this with the number found by the grid Newton search.

    Returns dict with:
        'newton_count': number of zeros from Newton search
        'ap_count': number from argument principle
        'discrepancy': newton_count - ap_count
        'agrees': True if |discrepancy| <= 1
    """
    newton_count = len(zeros)
    ap_count = argument_principle_count(
        shadow_coeffs, re_range, im_range, n_points, max_r
    )

    return {
        'newton_count': newton_count,
        'ap_count': ap_count,
        'discrepancy': newton_count - ap_count,
        'agrees': abs(newton_count - ap_count) <= 1,
    }


# ============================================================================
# 13. Full repulsion analysis pipeline
# ============================================================================

@dataclass
class RepulsionAnalysis:
    """Complete repulsion analysis for a shadow zeta function."""
    family: str
    param: float
    shadow_class: str
    n_zeros: int
    real_zeros: List[float]
    rightmost_real_zero: Optional[float]
    spacing_stats: ZeroSpacingData
    ks_gue: Tuple[float, float]      # (D_n, p_value)
    ks_poisson: Tuple[float, float]   # (D_n, p_value)
    height_profile: Dict[float, float]
    deuring_heilbronn_dist: float


def full_repulsion_analysis(
    family: str,
    param: float,
    max_r: int = 50,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-60.0, 60.0),
    grid_re: int = 15,
    grid_im: int = 50,
) -> RepulsionAnalysis:
    """Run the full repulsion analysis pipeline for a single algebra.

    Parameters
    ----------
    family : algebra family name
    param : family parameter
    max_r : maximum arity for shadow coefficients
    re_range, im_range : search region for zeros
    grid_re, grid_im : grid density for Newton search

    Returns
    -------
    RepulsionAnalysis with all statistics.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    # Classify shadow depth
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r

    if family == 'heisenberg':
        shadow_class = 'G'
    elif family in ('affine_sl2', 'affine_sl3'):
        shadow_class = 'L'
    elif family == 'betagamma':
        shadow_class = 'C'
    else:
        shadow_class = 'M'

    # Find zeros
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r
    )

    # Real zeros
    real_z = find_real_zeros_brentq(coeffs, re_range[0], re_range[1], max_r=max_r)
    rz = max(real_z) if real_z else None

    # Spacing statistics
    stats = compute_spacing_statistics(family, param, zeros)

    # KS tests
    if stats.normalized_spacings:
        ks_g = ks_against_gue(stats.normalized_spacings)
        ks_p = ks_against_poisson(stats.normalized_spacings)
    else:
        ks_g = (0.0, 1.0)
        ks_p = (0.0, 1.0)

    # Height profile
    height_prof = repulsion_vs_height(zeros)

    # Deuring-Heilbronn
    if rz is not None:
        dh_dist = deuring_heilbronn_bound(coeffs, rz, max_r)
    else:
        dh_dist = float('inf')

    return RepulsionAnalysis(
        family=family,
        param=param,
        shadow_class=shadow_class,
        n_zeros=len(zeros),
        real_zeros=real_z,
        rightmost_real_zero=rz,
        spacing_stats=stats,
        ks_gue=ks_g,
        ks_poisson=ks_p,
        height_profile=height_prof,
        deuring_heilbronn_dist=dh_dist,
    )
