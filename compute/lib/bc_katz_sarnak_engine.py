r"""BC-75: Katz-Sarnak symmetry type classification for shadow zeta zeros.

THE KATZ-SARNAK PHILOSOPHY:

The low-lying zero statistics of a family of L-functions are governed
by a classical compact group G from the list:

    USp(2N), SO(2N), SO(2N+1), U(N), O^-(2N)

The symmetry type is determined by:
  - Sign of functional equation (omega = +1 or -1)
  - Vanishing/non-vanishing at the central point s = 1/2
  - The 1-level density D_1(phi) for test functions phi with restricted
    Fourier support

For each compact group, the 1-level density prediction is:
    USp:      W(x) = 1 - sin(2*pi*x)/(2*pi*x)
    SO(even): W(x) = 1 + sin(2*pi*x)/(2*pi*x)
    SO(odd):  W(x) = 1 + (1/2)*delta_0(x) + sin(2*pi*x)/(2*pi*x)
    U(N):     W(x) = 1
    O^-:      W(x) = 1 - (1/2)*delta_0(x) + sin(2*pi*x)/(2*pi*x)

(Note: the delta_0 terms are detected by the excess/deficit of zeros
near the central point, not by the smooth 1-level density away from 0.)

This module classifies the symmetry type of shadow zeta zero families:

1. ONE-LEVEL DENSITY for Virasoro families c in [1,25]
2. FUNCTIONAL EQUATION SIGN from complementarity (Theorem C)
3. LOW-LYING ZEROS per depth class (G/L/C/M)
4. n-LEVEL CORRELATIONS (n = 2, 3) against GUE kernel predictions
5. NUMBER VARIANCE Sigma^2(L) against GUE/GOE/Poisson
6. NEAREST-NEIGHBOR SPACING p(s) against Wigner surmises
7. SYMMETRY TYPE as function of shadow depth class

Manuscript references:
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify by 3+ independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Literature convention mismatches for spectral statistics.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

try:
    import mpmath
    mpmath.mp.dps = 30
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    from scipy import stats as scipy_stats
    from scipy.special import erf as scipy_erf
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# ---------------------------------------------------------------------------
# Import from existing engines
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    find_zeros_grid,
    newton_zero,
    affine_sl2_zeros,
    heisenberg_zeros,
    betagamma_zeros_numerical,
    normalized_spacings,
    _shadow_zeta_complex,
)

from compute.lib.shadow_epstein_zeta import (
    virasoro_form,
)

from compute.lib.bc_pair_correlation_engine import (
    gue_pair_correlation,
    wigner_surmise_gue,
    wigner_surmise_goe,
    poisson_spacing,
    gue_number_variance as gue_nv_asymptotic,
    goe_number_variance as goe_nv_asymptotic,
    poisson_number_variance as poisson_nv,
    virasoro_epstein_zeros,
    unfold_epstein_zeros,
    nearest_neighbor_spacings,
    spacing_histogram,
    number_variance as compute_number_variance,
    ks_test_spacing,
    pair_correlation_histogram,
)


# ============================================================================
# 1. Katz-Sarnak 1-level density predictions
# ============================================================================

def usp_one_level_density(x: np.ndarray) -> np.ndarray:
    r"""USp(2N) 1-level density: W(x) = 1 - sin(2*pi*x)/(2*pi*x).

    At x = 0: W(0) = 0 (strong repulsion from the central point).
    """
    x = np.asarray(x, dtype=float)
    result = np.ones_like(x)
    nonzero = np.abs(x) > 1e-15
    result[nonzero] = 1.0 - np.sin(2 * np.pi * x[nonzero]) / (2 * np.pi * x[nonzero])
    result[~nonzero] = 0.0
    return result


def so_even_one_level_density(x: np.ndarray) -> np.ndarray:
    r"""SO(2N) 1-level density: W(x) = 1 + sin(2*pi*x)/(2*pi*x).

    At x = 0: W(0) = 2.
    """
    x = np.asarray(x, dtype=float)
    result = np.ones_like(x)
    nonzero = np.abs(x) > 1e-15
    result[nonzero] = 1.0 + np.sin(2 * np.pi * x[nonzero]) / (2 * np.pi * x[nonzero])
    result[~nonzero] = 2.0
    return result


def so_odd_one_level_density(x: np.ndarray) -> np.ndarray:
    r"""SO(2N+1) 1-level density (smooth part): W(x) = 1 + sin(2*pi*x)/(2*pi*x).

    The full SO(odd) density includes a (1/2)*delta_0 term at x = 0
    (forced vanishing at the central point). The smooth part away from x = 0
    has the same formula as SO(even). The delta term is detected by counting
    zeros at the central point, not from the smooth density.
    """
    return so_even_one_level_density(x)


def unitary_one_level_density(x: np.ndarray) -> np.ndarray:
    r"""U(N) 1-level density: W(x) = 1 (flat).

    Unitary symmetry gives no correlation with the central point.
    """
    return np.ones_like(np.asarray(x, dtype=float))


def o_minus_one_level_density(x: np.ndarray) -> np.ndarray:
    r"""O^-(2N) 1-level density (smooth part): same as SO(even).

    The full O^- density has a -(1/2)*delta_0 term (zero forced to vanish
    at the central point). The smooth part is the same as SO(even).
    """
    return so_even_one_level_density(x)


# Dictionary for convenience
ONE_LEVEL_DENSITY_PREDICTIONS = {
    'USp': usp_one_level_density,
    'SO_even': so_even_one_level_density,
    'SO_odd': so_odd_one_level_density,
    'U': unitary_one_level_density,
    'O_minus': o_minus_one_level_density,
}


# ============================================================================
# 2. Functional equation sign
# ============================================================================

def functional_equation_sign_epstein(c_val: float) -> Dict[str, Any]:
    r"""Determine the functional equation sign for the Virasoro Epstein zeta.

    The completed Epstein zeta Xi_Q(s) = Xi_Q(1-s) always has sign +1
    for a positive-definite binary quadratic form (Epstein's functional
    equation is sign-preserving for self-dual lattices).

    The complementarity structure gives additional information:
      - At c = 13 (self-dual): the form Q_{Vir_13} is self-complementary
      - For c != 13: Q_{Vir_c} and Q_{Vir_{26-c}} form a Koszul dual pair

    The shadow zeta zeta_A(s) = sum S_r * r^{-s} does NOT have a standard
    functional equation, but the Epstein zeta does. We classify by the
    Epstein sign.
    """
    a, b, cc, D = virasoro_form(c_val)
    # For a positive-definite binary quadratic form, the completed Epstein
    # zeta satisfies Xi_Q(s) = Xi_Q(1-s). The functional equation sign is +1.
    # Whether this is USp-like or SO-like depends on the FAMILY structure.

    # Evaluate near the center s = 1/2 to detect vanishing.
    # Note: _chowla_selberg_completed(t, ...) evaluates at s = 1/2 + it.
    # At t = 0 exactly, the Chowla-Selberg formula hits the zeta(2s) = zeta(1)
    # pole. Evaluate at a small offset t = epsilon instead, which gives
    # Xi_Q(1/2 + i*epsilon) ~ Xi_Q(1/2) for small epsilon.
    if HAS_MPMATH:
        from compute.lib.bc_pair_correlation_engine import _chowla_selberg_completed
        try:
            xi_half = _chowla_selberg_completed(1e-4, a, b, cc)
            central_value = xi_half.real
        except (ValueError, ZeroDivisionError):
            central_value = float('nan')
    else:
        central_value = float('nan')

    # For Epstein zeta: the functional equation is always Xi(s) = Xi(1-s)
    # with sign omega = +1. The question is which compact group.
    omega = +1  # Epstein functional equation is self-dual

    # Self-dual at c = 13
    is_self_dual = abs(c_val - 13.0) < 0.01

    # Koszul dual central charge
    c_dual = 26.0 - c_val

    return {
        'c': c_val,
        'c_dual': c_dual,
        'omega': omega,
        'is_self_dual': is_self_dual,
        'central_value': float(central_value) if not np.isnan(central_value) else None,
        'vanishes_at_center': abs(central_value) < 1e-6 if not np.isnan(central_value) else None,
    }


def functional_equation_sign_family(c_values: List[float]) -> List[Dict[str, Any]]:
    """Compute functional equation data for a family of Virasoro algebras."""
    return [functional_equation_sign_epstein(c) for c in c_values]


# ============================================================================
# 3. Low-lying zero statistics per depth class
# ============================================================================

@dataclass
class LowLyingZeroData:
    """Container for low-lying zero statistics of a shadow algebra."""
    family: str
    param: float
    depth_class: str  # G, L, C, M
    n_zeros: int
    first_zero_height: Optional[float]  # height of the lowest zero
    central_point_density: float  # density of zeros near s = 1/2
    one_level_density_values: Optional[np.ndarray] = None
    one_level_density_x: Optional[np.ndarray] = None
    zeros: Optional[List[complex]] = field(default=None, repr=False)


def classify_depth_class(family: str) -> str:
    """Return the shadow depth class (G/L/C/M) of a family."""
    if family == 'heisenberg':
        return 'G'
    elif family in ('affine_sl2', 'affine_sl3'):
        return 'L'
    elif family == 'betagamma':
        return 'C'
    elif family in ('virasoro', 'w3_t', 'w3_w'):
        return 'M'
    else:
        return 'unknown'


def low_lying_zeros_class_G(k_val: float) -> LowLyingZeroData:
    r"""Low-lying zeros for class G (Heisenberg).

    zeta_{H_k}(s) = k * 2^{-s} has NO zeros for k != 0.
    Shadow depth r_max = 2, symmetry type = trivial.
    """
    zeros = heisenberg_zeros(k_val)
    return LowLyingZeroData(
        family='heisenberg',
        param=k_val,
        depth_class='G',
        n_zeros=len(zeros),
        first_zero_height=None,
        central_point_density=0.0,
        zeros=zeros,
    )


def low_lying_zeros_class_L(
    k_val: float,
    n_max: int = 200,
) -> LowLyingZeroData:
    r"""Low-lying zeros for class L (affine KM).

    Two-term exponential polynomial: zeros on vertical lines.
    All zeros have the SAME real part Re(s) = -log(kappa/alpha)/log(3/2).
    Imaginary parts: Im(s) = -pi*(2n+1)/log(3/2), uniformly spaced.

    Symmetry type determined by the crystalline (equally-spaced) structure.
    """
    zeros = affine_sl2_zeros(k_val, n_max)
    positive_im = [z for z in zeros if z.imag > 0]

    first_height = min(abs(z.imag) for z in zeros) if zeros else None

    return LowLyingZeroData(
        family='affine_sl2',
        param=k_val,
        depth_class='L',
        n_zeros=len(zeros),
        first_zero_height=first_height,
        central_point_density=0.0,  # No zero at s = 1/2
        zeros=zeros,
    )


def low_lying_zeros_class_C(
    lam_val: float = 0.5,
    t_max: float = 100.0,
) -> LowLyingZeroData:
    r"""Low-lying zeros for class C (beta-gamma).

    Three-term exponential polynomial: finitely many zeros in any strip.
    """
    zeros = betagamma_zeros_numerical(lam_val, im_range=(-t_max, t_max))
    positive_im = [z for z in zeros if z.imag > 0]

    first_height = min(abs(z.imag) for z in positive_im) if positive_im else None

    return LowLyingZeroData(
        family='betagamma',
        param=lam_val,
        depth_class='C',
        n_zeros=len(zeros),
        first_zero_height=first_height,
        central_point_density=0.0,
        zeros=zeros,
    )


def low_lying_zeros_class_M(
    c_val: float,
    t_max: float = 100.0,
    dt: float = 0.3,
) -> LowLyingZeroData:
    r"""Low-lying zeros for class M (Virasoro) via Epstein zeta.

    Infinitely many zeros. Compute the first batch up to height t_max.
    """
    zeros_heights = virasoro_epstein_zeros(c_val, t_max=t_max, dt=dt)

    first_height = float(zeros_heights[0]) if len(zeros_heights) > 0 else None

    # Estimate density near the central point
    low_count = np.sum(zeros_heights < 5.0) if len(zeros_heights) > 0 else 0
    central_density = float(low_count) / 5.0 if len(zeros_heights) > 0 else 0.0

    # Convert to complex zeros on the critical line
    zeros_complex = [complex(0.5, t) for t in zeros_heights]

    return LowLyingZeroData(
        family='virasoro',
        param=c_val,
        depth_class='M',
        n_zeros=len(zeros_heights),
        first_zero_height=first_height,
        central_point_density=central_density,
        zeros=zeros_complex,
    )


# ============================================================================
# 4. One-level density computation
# ============================================================================

def one_level_density_empirical(
    zero_heights: np.ndarray,
    conductor_log: float,
    x_max: float = 2.0,
    n_bins: int = 40,
    phi_type: str = 'gaussian',
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute the empirical 1-level density from a family of zero heights.

    D_1(phi) = (1/|F|) * sum_{zeta in F} sum_rho phi(gamma_rho * L / (2*pi))

    where L = log(conductor)/(2*pi) is the effective log-conductor.

    For a single member of the family (one algebra), this is:
        sum_rho phi(gamma_rho * L / (2*pi))

    We compute the histogram of scaled zero heights gamma * L/(2*pi)
    and return the density estimate.

    Parameters
    ----------
    zero_heights : array of positive imaginary parts of zeros
    conductor_log : log of the analytic conductor
    x_max : range of x for the density
    n_bins : number of histogram bins
    phi_type : 'gaussian' (smooth), 'boxcar', or 'sinc'

    Returns
    -------
    (x, density) where x is bin centers and density is the 1-level density.
    """
    gammas = np.sort(np.asarray(zero_heights, dtype=float))
    gammas = gammas[gammas > 0]
    N = len(gammas)
    if N == 0:
        x = np.linspace(-x_max, x_max, n_bins)
        return x, np.zeros(n_bins)

    # Scale zero heights by log-conductor
    L = conductor_log / (2 * np.pi)
    if L <= 0:
        L = 1.0

    scaled = gammas * L

    x = np.linspace(-x_max, x_max, n_bins)

    if phi_type == 'gaussian':
        # Kernel density with Gaussian test function
        bandwidth = 0.15
        density = np.zeros(n_bins)
        for k, xk in enumerate(x):
            kernel = np.exp(-0.5 * ((scaled - xk) / bandwidth) ** 2) / (
                bandwidth * np.sqrt(2 * np.pi))
            density[k] = np.sum(kernel) / max(N, 1)
        # The 1-level density should be normalized so that integral = N/|F|
        # For a single algebra, integral = number of zeros
    elif phi_type == 'boxcar':
        bin_edges = np.linspace(-x_max, x_max, n_bins + 1)
        counts, _ = np.histogram(scaled, bins=bin_edges)
        bin_width = bin_edges[1] - bin_edges[0]
        density = counts / (N * bin_width) if N > 0 else counts * 0
        x = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    else:
        raise ValueError(f"Unknown phi_type: {phi_type}")

    return x, density


def effective_conductor_epstein(a_c: float, b_c: float, c_c: float) -> float:
    r"""Effective analytic conductor for an Epstein zeta function.

    For a binary quadratic form Q(m,n) = a*m^2 + b*mn + c*n^2 with
    discriminant D = b^2 - 4ac, the analytic conductor is:
        C(eps_Q) = |D|/4 = a*c - (b/2)^2

    The log-conductor is log(|D|/4).
    """
    D_E = a_c * c_c - (b_c / 2.0) ** 2
    return math.log(abs(D_E)) if D_E != 0 else 0.0


def one_level_density_virasoro_family(
    c_values: List[float],
    t_max: float = 50.0,
    dt: float = 0.3,
    x_max: float = 2.0,
    n_bins: int = 40,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute the family-averaged 1-level density for Virasoro at various c.

    D_1(phi) = (1/|F|) * sum_{c in F} sum_rho phi(gamma_rho * log(C_c)/(2*pi))

    This is the KEY object that determines the Katz-Sarnak symmetry type.
    """
    all_scaled = []

    for c_val in c_values:
        zeros = virasoro_epstein_zeros(c_val, t_max=t_max, dt=dt)
        if len(zeros) == 0:
            continue
        a, b, cc, D = virasoro_form(c_val)
        log_cond = effective_conductor_epstein(a, b, cc)
        L = log_cond / (2 * np.pi)
        if L <= 0:
            L = 1.0
        scaled = zeros * L
        all_scaled.extend(scaled.tolist())

    if len(all_scaled) == 0:
        x = np.linspace(-x_max, x_max, n_bins)
        return x, np.zeros(n_bins)

    all_scaled = np.array(all_scaled)
    N_family = len(c_values)

    # Kernel density estimate
    x = np.linspace(0.01, x_max, n_bins)
    bandwidth = 0.2
    density = np.zeros(n_bins)
    for k, xk in enumerate(x):
        kernel = np.exp(-0.5 * ((all_scaled - xk) / bandwidth) ** 2) / (
            bandwidth * np.sqrt(2 * np.pi))
        density[k] = np.sum(kernel) / N_family

    return x, density


# ============================================================================
# 5. Symmetry type classification via L2 fitting
# ============================================================================

def classify_symmetry_type_one_level(
    x: np.ndarray,
    density: np.ndarray,
) -> Dict[str, Any]:
    r"""Classify the symmetry type by fitting the 1-level density to predictions.

    Returns the best-fit symmetry type and L2 distances to each prediction.
    """
    # Restrict to x > 0.1 (avoid the delta function region)
    mask = x > 0.1
    if np.sum(mask) < 3:
        return {'best_fit': 'unknown', 'distances': {}}

    x_fit = x[mask]
    d_fit = density[mask]

    distances = {}
    for name, pred_fn in ONE_LEVEL_DENSITY_PREDICTIONS.items():
        pred = pred_fn(x_fit)
        # Normalize both to compare shapes (the absolute normalization
        # depends on the number of zeros and family size)
        if np.max(np.abs(d_fit)) > 1e-15:
            d_norm = d_fit / np.max(np.abs(d_fit))
        else:
            d_norm = d_fit
        if np.max(np.abs(pred)) > 1e-15:
            p_norm = pred / np.max(np.abs(pred))
        else:
            p_norm = pred
        dist = float(np.sqrt(np.mean((d_norm - p_norm) ** 2)))
        distances[name] = dist

    best_fit = min(distances, key=distances.get)

    return {
        'best_fit': best_fit,
        'distances': distances,
    }


# ============================================================================
# 6. n-level correlations (n = 2, 3)
# ============================================================================

def sine_kernel(x: np.ndarray) -> np.ndarray:
    r"""Sine kernel K(x) = sin(pi*x)/(pi*x), with K(0) = 1."""
    x = np.asarray(x, dtype=float)
    result = np.ones_like(x)
    nonzero = np.abs(x) > 1e-15
    result[nonzero] = np.sin(np.pi * x[nonzero]) / (np.pi * x[nonzero])
    return result


def gue_two_point_correlation(x: np.ndarray) -> np.ndarray:
    r"""GUE 2-point correlation: R_2(x) = 1 - K(x)^2.

    Identical to gue_pair_correlation but expressed via sine kernel.
    """
    K = sine_kernel(x)
    return 1.0 - K ** 2


def gue_three_point_cluster(r: np.ndarray, s: np.ndarray) -> np.ndarray:
    r"""GUE 3-point connected cluster function.

    T_3(r, s) = 2 * K(r) * K(s) * K(s - r)

    This is the beautiful result for the GUE determinantal point process:
    the 3-point cluster function is the triple product of the sine kernel.
    """
    Kr = sine_kernel(r)
    Ks = sine_kernel(s)
    Ksr = sine_kernel(s - r)
    return 2.0 * Kr * Ks * Ksr


def gue_three_point_full(r: np.ndarray, s: np.ndarray) -> np.ndarray:
    r"""Full GUE 3-point correlation R_3(0, r, s) = det_3(K).

    R_3 = 1 - K(r)^2 - K(s)^2 - K(s-r)^2 + 2*K(r)*K(s)*K(s-r)
    """
    Kr = sine_kernel(r)
    Ks = sine_kernel(s)
    Ksr = sine_kernel(s - r)
    return 1.0 - Kr**2 - Ks**2 - Ksr**2 + 2 * Kr * Ks * Ksr


def empirical_two_point_correlation(
    unfolded_zeros: np.ndarray,
    x_max: float = 3.0,
    n_bins: int = 60,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute empirical R_2(x) from unfolded zeros (proxy for pair correlation)."""
    return pair_correlation_histogram(unfolded_zeros, x_max=x_max, n_bins=n_bins)


def empirical_three_point_correlation(
    unfolded_zeros: np.ndarray,
    r_max: float = 2.0,
    s_max: float = 2.0,
    n_bins: int = 20,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r"""Compute empirical 3-point connected correlation from unfolded zeros.

    For each triple (i, j, k) of distinct zeros, compute the
    differences r = u_j - u_i, s = u_k - u_i and bin to get T_3(r, s).

    Returns (r_grid, s_grid, T_3_values) on a 2D grid.
    """
    u = np.sort(np.asarray(unfolded_zeros, dtype=float))
    N = len(u)

    r_edges = np.linspace(0, r_max, n_bins + 1)
    s_edges = np.linspace(0, s_max, n_bins + 1)
    r_centers = 0.5 * (r_edges[:-1] + r_edges[1:])
    s_centers = 0.5 * (s_edges[:-1] + s_edges[1:])

    counts = np.zeros((n_bins, n_bins))
    window = min(30, N - 1)

    for i in range(N):
        for j in range(i + 1, min(i + window, N)):
            rij = u[j] - u[i]
            if rij >= r_max:
                break
            for k in range(j + 1, min(j + window, N)):
                sik = u[k] - u[i]
                if sik >= s_max:
                    break
                # Bin (rij, sik)
                ri = int(rij / r_max * n_bins)
                si = int(sik / s_max * n_bins)
                if 0 <= ri < n_bins and 0 <= si < n_bins:
                    counts[ri, si] += 1

    # Normalize to get density
    total = np.sum(counts)
    if total > 0:
        bin_area = (r_max / n_bins) * (s_max / n_bins)
        # Expected count under Poisson (independence)
        expected_per_bin = total / (n_bins * n_bins)
        T_3 = counts / (expected_per_bin + 1e-30) - 1.0
    else:
        T_3 = counts

    return r_centers, s_centers, T_3


# ============================================================================
# 7. Number variance computation
# ============================================================================

def number_variance_from_zeros(
    unfolded_zeros: np.ndarray,
    L_values: np.ndarray,
) -> np.ndarray:
    r"""Compute Sigma^2(L) from unfolded zeros.

    Sigma^2(L) = Var(N([a, a+L])) averaged over starting points a.
    """
    u = np.asarray(unfolded_zeros, dtype=float)
    L = np.asarray(L_values, dtype=float)
    if len(u) < 2:
        return np.zeros(len(L))
    return compute_number_variance(u, L)


def classify_by_number_variance(
    L_values: np.ndarray,
    sigma2_observed: np.ndarray,
) -> Dict[str, Any]:
    r"""Classify the symmetry type by comparing number variance to predictions.

    GUE: Sigma^2 ~ (2/pi^2) * log(L) (logarithmic, slow growth)
    GOE: Sigma^2 ~ (2/pi^2) * (log(L) + const) (slightly larger than GUE)
    Poisson: Sigma^2 = L (linear growth)

    The key discriminant is the GROWTH RATE:
    - logarithmic => random matrix (GUE or GOE)
    - linear => Poisson (uncorrelated)
    """
    L = np.asarray(L_values, dtype=float)
    s2 = np.asarray(sigma2_observed, dtype=float)

    mask = (L > 0.5) & (s2 > 0)
    if np.sum(mask) < 3:
        return {'type': 'insufficient_data'}

    L_fit = L[mask]
    s2_fit = s2[mask]

    # Fit to a*log(L) + b
    log_L = np.log(L_fit)
    A = np.column_stack([log_L, np.ones_like(log_L)])
    try:
        coeffs_log, _, _, _ = np.linalg.lstsq(A, s2_fit, rcond=None)
        pred_log = A @ coeffs_log
        resid_log = np.sum((s2_fit - pred_log) ** 2)
    except np.linalg.LinAlgError:
        resid_log = float('inf')
        coeffs_log = [0, 0]

    # Fit to a*L + b (Poisson)
    B = np.column_stack([L_fit, np.ones_like(L_fit)])
    try:
        coeffs_lin, _, _, _ = np.linalg.lstsq(B, s2_fit, rcond=None)
        pred_lin = B @ coeffs_lin
        resid_lin = np.sum((s2_fit - pred_lin) ** 2)
    except np.linalg.LinAlgError:
        resid_lin = float('inf')
        coeffs_lin = [0, 0]

    # L2 distances to GUE and Poisson predictions
    gue_pred = gue_nv_asymptotic(L_fit)
    poisson_pred = poisson_nv(L_fit)

    dist_gue = float(np.sqrt(np.mean((s2_fit - gue_pred) ** 2)))
    dist_poisson = float(np.sqrt(np.mean((s2_fit - poisson_pred) ** 2)))

    # Classification
    if resid_log < resid_lin * 0.5:
        growth_type = 'logarithmic'
    elif resid_lin < resid_log * 0.5:
        growth_type = 'linear'
    else:
        growth_type = 'ambiguous'

    if dist_gue < dist_poisson:
        nv_type = 'GUE'
    else:
        nv_type = 'Poisson'

    return {
        'type': nv_type,
        'growth_type': growth_type,
        'dist_gue': dist_gue,
        'dist_poisson': dist_poisson,
        'log_slope': float(coeffs_log[0]),
        'lin_slope': float(coeffs_lin[0]),
        'resid_log': float(resid_log),
        'resid_lin': float(resid_lin),
    }


# ============================================================================
# 8. Nearest-neighbor spacing distribution
# ============================================================================

def wigner_surmise_gue_pdf(s: np.ndarray) -> np.ndarray:
    r"""GUE Wigner surmise: p(s) = (32/pi^2) * s^2 * exp(-4*s^2/pi)."""
    return wigner_surmise_gue(s)


def wigner_surmise_goe_pdf(s: np.ndarray) -> np.ndarray:
    r"""GOE Wigner surmise: p(s) = (pi/2) * s * exp(-pi*s^2/4)."""
    return wigner_surmise_goe(s)


def poisson_spacing_pdf(s: np.ndarray) -> np.ndarray:
    r"""Poisson spacing: p(s) = exp(-s)."""
    return poisson_spacing(s)


def wigner_surmise_gue_cdf(s: np.ndarray) -> np.ndarray:
    r"""CDF of GUE Wigner surmise.

    F(s) = erf(2s/sqrt(pi)) - (4s/pi) * exp(-4s^2/pi)
    """
    s = np.asarray(s, dtype=float)
    if HAS_SCIPY:
        return scipy_erf(2.0 * s / np.sqrt(np.pi)) - (4.0 * s / np.pi) * np.exp(-4.0 * s ** 2 / np.pi)
    else:
        # Fallback: numerical integration
        result = np.zeros_like(s)
        for i, si in enumerate(s.flat):
            t = np.linspace(0, si, 200)
            dt = t[1] - t[0] if len(t) > 1 else 1.0
            result.flat[i] = np.sum(wigner_surmise_gue(t)) * dt
        return result


def wigner_surmise_goe_cdf(s: np.ndarray) -> np.ndarray:
    r"""CDF of GOE Wigner surmise: F(s) = 1 - exp(-pi*s^2/4)."""
    s = np.asarray(s, dtype=float)
    return 1.0 - np.exp(-np.pi * s ** 2 / 4.0)


def poisson_spacing_cdf(s: np.ndarray) -> np.ndarray:
    r"""CDF of Poisson spacing: F(s) = 1 - exp(-s)."""
    s = np.asarray(s, dtype=float)
    return 1.0 - np.exp(-s)


SPACING_CDFS = {
    'GUE': wigner_surmise_gue_cdf,
    'GOE': wigner_surmise_goe_cdf,
    'Poisson': poisson_spacing_cdf,
}


def ks_test_against_all(spacings: np.ndarray) -> Dict[str, Dict[str, float]]:
    r"""Run KS test of spacing distribution against GUE, GOE, and Poisson.

    Returns dict mapping distribution name to {statistic, p_value}.
    """
    s = np.sort(np.asarray(spacings, dtype=float))
    s = s[s >= 0]
    N = len(s)
    if N < 5:
        return {name: {'statistic': float('nan'), 'p_value': 0.0}
                for name in SPACING_CDFS}

    ecdf = np.arange(1, N + 1) / N
    results = {}

    for name, cdf_fn in SPACING_CDFS.items():
        cdf = cdf_fn(s)
        ks_stat = float(np.max(np.abs(ecdf - cdf)))
        # Kolmogorov limiting distribution approximation
        lam = (np.sqrt(N) + 0.12 + 0.11 / np.sqrt(N)) * ks_stat
        p_value = 0.0
        for k in range(1, 20):
            p_value += (-1) ** (k + 1) * np.exp(-2.0 * k ** 2 * lam ** 2)
        p_value = max(0.0, min(1.0, 2.0 * p_value))
        results[name] = {
            'statistic': ks_stat,
            'p_value': p_value,
        }

    return results


def classify_by_spacing(spacings: np.ndarray) -> Dict[str, Any]:
    r"""Classify symmetry type from nearest-neighbor spacing distribution.

    The level repulsion exponent beta distinguishes:
        beta = 0: Poisson (no repulsion)
        beta = 1: GOE (linear repulsion)
        beta = 2: GUE (quadratic repulsion)
    """
    ks_results = ks_test_against_all(spacings)

    # Find best fit by smallest KS statistic
    best_name = min(ks_results, key=lambda n: ks_results[n]['statistic'])

    # Estimate level repulsion exponent from small-s behavior
    s = np.sort(spacings)
    small_mask = (s > 0.01) & (s < 0.5)
    if np.sum(small_mask) > 5:
        log_s = np.log(s[small_mask])
        # p(s) ~ s^beta => log p ~ beta * log s
        # Use histogram to estimate p(s)
        bins = np.linspace(0.01, 0.5, 20)
        counts, edges = np.histogram(s[small_mask], bins=bins, density=True)
        centers = 0.5 * (edges[:-1] + edges[1:])
        positive = counts > 0
        if np.sum(positive) > 3:
            log_c = np.log(centers[positive])
            log_p = np.log(counts[positive])
            # Linear fit: log_p = beta * log_c + const
            A = np.column_stack([log_c, np.ones_like(log_c)])
            try:
                fit, _, _, _ = np.linalg.lstsq(A, log_p, rcond=None)
                beta_est = float(fit[0])
            except np.linalg.LinAlgError:
                beta_est = float('nan')
        else:
            beta_est = float('nan')
    else:
        beta_est = float('nan')

    return {
        'best_fit': best_name,
        'ks_results': ks_results,
        'beta_estimate': beta_est,
        'beta_type': (
            'Poisson' if beta_est < 0.5 else
            'GOE' if beta_est < 1.5 else
            'GUE' if beta_est < 2.5 else
            'unknown'
        ) if not np.isnan(beta_est) else 'unknown',
    }


# ============================================================================
# 9. Symmetry type as function of depth class
# ============================================================================

@dataclass
class SymmetryClassification:
    """Full symmetry type classification for a shadow algebra."""
    family: str
    param: float
    depth_class: str
    spacing_type: str
    nv_type: str
    one_level_type: str
    beta_estimate: float
    overall_type: str
    details: Dict[str, Any] = field(default_factory=dict)


def classify_depth_class_symmetry(
    depth_class: str,
    zeros_or_heights: np.ndarray,
    form_data: Optional[Tuple[float, float, float, float]] = None,
) -> SymmetryClassification:
    r"""Classify symmetry type for a given depth class.

    Uses multiple diagnostics:
    1. Nearest-neighbor spacing distribution
    2. Number variance growth
    3. KS tests against GUE/GOE/Poisson

    Parameters
    ----------
    depth_class : 'G', 'L', 'C', or 'M'
    zeros_or_heights : array of zero heights (positive reals)
    form_data : optional (a, b, c, D) for Epstein form (for unfolding)
    """
    heights = np.sort(np.asarray(zeros_or_heights, dtype=float))
    heights = heights[heights > 0]

    if len(heights) < 10:
        return SymmetryClassification(
            family='', param=0, depth_class=depth_class,
            spacing_type='insufficient', nv_type='insufficient',
            one_level_type='insufficient', beta_estimate=float('nan'),
            overall_type='insufficient',
        )

    # Unfold
    if form_data is not None:
        a, b, cc, D = form_data
        unfolded = unfold_epstein_zeros(heights, a, b, cc)
    else:
        # Generic unfolding via polynomial fit
        indices = np.arange(1, len(heights) + 1, dtype=float)
        coeffs = np.polyfit(heights, indices, deg=min(3, len(heights) - 1))
        unfolded = np.polyval(coeffs, heights)
        spacings_raw = np.diff(unfolded)
        mean_sp = np.mean(spacings_raw)
        if mean_sp > 0:
            unfolded = unfolded / mean_sp

    # Spacing analysis
    spacings = nearest_neighbor_spacings(unfolded)
    spacing_class = classify_by_spacing(spacings)

    # Number variance
    L_values = np.array([0.5, 1.0, 2.0, 5.0, 10.0])
    sigma2 = number_variance_from_zeros(unfolded, L_values)
    nv_class = classify_by_number_variance(L_values, sigma2)

    return SymmetryClassification(
        family='',
        param=0.0,
        depth_class=depth_class,
        spacing_type=spacing_class['best_fit'],
        nv_type=nv_class.get('type', 'unknown'),
        one_level_type='',
        beta_estimate=spacing_class.get('beta_estimate', float('nan')),
        overall_type=spacing_class['best_fit'],
        details={
            'spacing': spacing_class,
            'number_variance': nv_class,
            'n_zeros': len(heights),
        },
    )


def symmetry_vs_depth_class(
    c_values_M: Optional[List[float]] = None,
    k_values_L: Optional[List[float]] = None,
    t_max: float = 80.0,
) -> Dict[str, List[SymmetryClassification]]:
    r"""Compute symmetry type for each depth class.

    Conjecture 1: Class M algebras have GUE statistics (= U(N) type)
    Conjecture 2: The symmetry type is an INVARIANT of the depth class

    Returns dict mapping depth class to list of classifications.
    """
    if c_values_M is None:
        c_values_M = [1.0, 5.0, 10.0, 13.0, 20.0, 25.0]
    if k_values_L is None:
        k_values_L = [1.0, 2.0, 5.0, 10.0]

    results = {'G': [], 'L': [], 'C': [], 'M': []}

    # Class G: no zeros, trivially classified
    for k in [1.0, 2.0, 5.0]:
        results['G'].append(SymmetryClassification(
            family='heisenberg', param=k, depth_class='G',
            spacing_type='trivial', nv_type='trivial',
            one_level_type='trivial', beta_estimate=float('nan'),
            overall_type='trivial',
        ))

    # Class L: crystalline (equally spaced zeros)
    for k in k_values_L:
        zeros = affine_sl2_zeros(k, n_max=200)
        heights = np.array(sorted([z.imag for z in zeros if z.imag > 0.5]))
        if len(heights) > 10:
            cls = classify_depth_class_symmetry('L', heights)
            cls.family = 'affine_sl2'
            cls.param = k
            results['L'].append(cls)

    # Class M: Epstein zeros
    for c_val in c_values_M:
        heights = virasoro_epstein_zeros(c_val, t_max=t_max, dt=0.3)
        if len(heights) > 10:
            a, b, cc, D = virasoro_form(c_val)
            cls = classify_depth_class_symmetry('M', heights, (a, b, cc, D))
            cls.family = 'virasoro'
            cls.param = c_val
            results['M'].append(cls)

    return results


# ============================================================================
# 10. Complementarity: c <-> 26-c consistency
# ============================================================================

def complementarity_symmetry_test(
    c_val: float,
    t_max: float = 80.0,
) -> Dict[str, Any]:
    r"""Test that the symmetry type is consistent under Koszul duality c <-> 26-c.

    The pair (Vir_c, Vir_{26-c}) should have related statistics.
    At c = 13 (self-dual): the statistics should be maximally symmetric.

    CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    """
    c_dual = 26.0 - c_val

    zeros_c = virasoro_epstein_zeros(c_val, t_max=t_max, dt=0.3)
    zeros_dual = virasoro_epstein_zeros(c_dual, t_max=t_max, dt=0.3)

    if len(zeros_c) < 10 or len(zeros_dual) < 10:
        return {
            'c': c_val, 'c_dual': c_dual,
            'consistent': None, 'note': 'insufficient zeros',
        }

    # Unfold both
    a, b, cc, D = virasoro_form(c_val)
    unf_c = unfold_epstein_zeros(zeros_c, a, b, cc)
    a2, b2, cc2, D2 = virasoro_form(c_dual)
    unf_dual = unfold_epstein_zeros(zeros_dual, a2, b2, cc2)

    # Spacing analysis for both
    sp_c = nearest_neighbor_spacings(unf_c)
    sp_dual = nearest_neighbor_spacings(unf_dual)

    class_c = classify_by_spacing(sp_c)
    class_dual = classify_by_spacing(sp_dual)

    consistent = class_c['best_fit'] == class_dual['best_fit']

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa_c': c_val / 2.0,
        'kappa_dual': c_dual / 2.0,
        'kappa_sum': c_val / 2.0 + c_dual / 2.0,  # Should be 13
        'type_c': class_c['best_fit'],
        'type_dual': class_dual['best_fit'],
        'consistent': consistent,
        'beta_c': class_c.get('beta_estimate', float('nan')),
        'beta_dual': class_dual.get('beta_estimate', float('nan')),
        'n_zeros_c': len(zeros_c),
        'n_zeros_dual': len(zeros_dual),
    }


# ============================================================================
# 11. Comprehensive analysis pipeline
# ============================================================================

def comprehensive_katz_sarnak_analysis(
    c_val: float,
    t_max: float = 80.0,
    dt: float = 0.3,
) -> Dict[str, Any]:
    r"""Full Katz-Sarnak analysis for Virasoro at a single central charge.

    Combines all diagnostics:
    1. Zero computation
    2. Spacing analysis (KS tests)
    3. Number variance
    4. Functional equation sign
    5. Complementarity test
    6. Symmetry type classification
    """
    # 1. Find zeros
    zeros = virasoro_epstein_zeros(c_val, t_max=t_max, dt=dt)
    n_zeros = len(zeros)

    if n_zeros < 10:
        return {
            'c': c_val, 'n_zeros': n_zeros,
            'status': 'insufficient_zeros',
        }

    # 2. Unfold
    a, b, cc, D = virasoro_form(c_val)
    unfolded = unfold_epstein_zeros(zeros, a, b, cc)

    # 3. Spacing
    spacings = nearest_neighbor_spacings(unfolded)
    spacing_class = classify_by_spacing(spacings)

    # 4. Number variance
    L_vals = np.array([0.5, 1.0, 2.0, 5.0, 10.0])
    sigma2 = number_variance_from_zeros(unfolded, L_vals)
    nv_class = classify_by_number_variance(L_vals, sigma2)

    # 5. Functional equation
    fe_data = functional_equation_sign_epstein(c_val)

    # 6. Overall classification
    overall_type = spacing_class['best_fit']

    return {
        'c': c_val,
        'kappa': c_val / 2.0,
        'n_zeros': n_zeros,
        'first_zero': float(zeros[0]) if n_zeros > 0 else None,
        'spacing_type': spacing_class['best_fit'],
        'beta_estimate': spacing_class.get('beta_estimate', float('nan')),
        'nv_type': nv_class.get('type', 'unknown'),
        'nv_growth': nv_class.get('growth_type', 'unknown'),
        'fe_omega': fe_data['omega'],
        'overall_type': overall_type,
        'details': {
            'spacing': spacing_class,
            'number_variance': nv_class,
            'functional_equation': fe_data,
            'sigma2_values': sigma2.tolist() if isinstance(sigma2, np.ndarray) else list(sigma2),
        },
    }


# ============================================================================
# 12. Level spacing ratio (r-statistic)
# ============================================================================

GUE_MEAN_R = 0.5307  # <r> for GUE
GOE_MEAN_R = 0.5359  # <r> for GOE (slightly different from GUE)
POISSON_MEAN_R = 2.0 * math.log(2) - 1.0  # <r> = 2*ln(2) - 1 ~ 0.3863


def spacing_ratios(spacings: np.ndarray) -> np.ndarray:
    r"""Compute level spacing ratios r_n = min(s_n, s_{n+1})/max(s_n, s_{n+1}).

    The spacing ratio avoids the need for unfolding since it is
    dimensionless. For GUE: <r> ~ 0.5307. For Poisson: <r> ~ 0.3863.
    """
    s = np.asarray(spacings, dtype=float)
    if len(s) < 2:
        return np.array([])
    r = np.minimum(s[:-1], s[1:]) / (np.maximum(s[:-1], s[1:]) + 1e-30)
    return r


def mean_spacing_ratio(spacings: np.ndarray) -> float:
    r"""Mean spacing ratio <r>.

    GUE: <r> ~ 0.5307
    Poisson: <r> ~ 0.3863
    GOE: <r> ~ 0.5359
    """
    r = spacing_ratios(spacings)
    if len(r) == 0:
        return float('nan')
    return float(np.mean(r))


def classify_by_spacing_ratio(spacings: np.ndarray) -> str:
    r"""Classify by mean spacing ratio."""
    r_mean = mean_spacing_ratio(spacings)
    if np.isnan(r_mean):
        return 'unknown'
    # Decision boundaries
    midpoint_poisson_goe = (POISSON_MEAN_R + GOE_MEAN_R) / 2  # ~ 0.46
    if r_mean < midpoint_poisson_goe:
        return 'Poisson'
    else:
        return 'GUE'  # GUE and GOE are hard to distinguish by <r> alone


# ============================================================================
# 13. Cross-consistency checks
# ============================================================================

def cross_consistency_check(
    spacings: np.ndarray,
    unfolded_zeros: np.ndarray,
) -> Dict[str, Any]:
    r"""Verify that spacing and number variance diagnostics agree.

    This is a CONSISTENCY CHECK: the spacing distribution and the number
    variance must agree on the symmetry type. If they disagree, the data
    is insufficient or the model is wrong.
    """
    # Spacing classification
    sp_class = classify_by_spacing(spacings)

    # Number variance
    L_vals = np.array([0.5, 1.0, 2.0, 5.0])
    sigma2 = number_variance_from_zeros(unfolded_zeros, L_vals)
    nv_class = classify_by_number_variance(L_vals, sigma2)

    # Spacing ratio
    r_type = classify_by_spacing_ratio(spacings)

    # Check agreement
    types = [
        sp_class.get('best_fit', 'unknown'),
        nv_class.get('type', 'unknown'),
        r_type,
    ]
    # Filter out 'unknown' and 'insufficient'
    valid_types = [t for t in types if t not in ('unknown', 'insufficient', 'insufficient_data')]

    if len(valid_types) == 0:
        agreement = 'no_data'
    elif len(set(valid_types)) == 1:
        agreement = 'unanimous'
    elif len(set(valid_types)) == 2:
        agreement = 'partial'
    else:
        agreement = 'inconsistent'

    return {
        'spacing_type': sp_class.get('best_fit', 'unknown'),
        'nv_type': nv_class.get('type', 'unknown'),
        'ratio_type': r_type,
        'agreement': agreement,
        'all_types': types,
    }


# ============================================================================
# 14. Affine family (class L) exact spacing analysis
# ============================================================================

def affine_crystalline_period(k_val: float) -> float:
    r"""Exact period of the crystalline zero spacing for affine sl_2.

    For affine sl_2 at level k, zeros are equally spaced with period:
        Delta = pi / log(3/2)

    This is INDEPENDENT of k (the level only shifts the real part).
    The imaginary parts are: Im(s_n) = pi*(2n+1)/log(3/2).
    Adjacent spacing: 2*pi/log(3/2).
    """
    return 2.0 * math.pi / math.log(3.0 / 2.0)


def affine_spacing_uniformity(k_val: float, n_max: int = 100) -> Dict[str, float]:
    r"""Test that affine sl_2 zeros have perfectly uniform spacing.

    The coefficient of variation (std/mean) should be exactly 0
    for a perfectly crystalline spectrum.
    """
    zeros = affine_sl2_zeros(k_val, n_max)
    heights = np.array(sorted([z.imag for z in zeros if z.imag > 0]))

    if len(heights) < 3:
        return {'mean_spacing': float('nan'), 'std_spacing': float('nan'), 'cv': float('nan')}

    spacings = np.diff(heights)
    mean_sp = float(np.mean(spacings))
    std_sp = float(np.std(spacings))
    cv = std_sp / mean_sp if mean_sp > 0 else float('nan')

    # Compare with exact period
    exact_period = affine_crystalline_period(k_val)

    return {
        'mean_spacing': mean_sp,
        'std_spacing': std_sp,
        'cv': cv,
        'exact_period': exact_period,
        'period_error': abs(mean_sp - exact_period) / exact_period if exact_period > 0 else float('nan'),
    }
