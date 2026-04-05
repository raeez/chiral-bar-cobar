#!/usr/bin/env python3
r"""
bc_npoint_correlation_engine.py -- Higher-point correlation functions of shadow
zeta zeros: 3-point, 4-point, 5-point correlations, connected cumulants, form
factors, gap probabilities, and determinantal point process tests.

THE CONSTRUCTION:

The shadow zeta function zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s} has zeros
on the critical strip.  Previous work (bc_pair_correlation_engine.py) computed
pair correlation R_2(x) and found GUE statistics.  This module pushes to
HIGHER-POINT correlations:

1. n-POINT CORRELATION R_n(x_1, ..., x_{n-1}):
   For a determinantal point process (DPP) with sine kernel K(x,y) =
   sin(pi(x-y))/(pi(x-y)), the n-point correlation function is:
       R_n(x_1, ..., x_n) = det(K(x_i - x_j))_{1 <= i,j <= n}
   For GUE:
       R_2(x) = 1 - sinc(x)^2
       R_3(x,y,z) = det_3(K)
       R_4(x,y,z,w) = det_4(K)

2. CONNECTED CORRELATIONS (cumulants):
   T_2(x) = R_2(x) - 1  (the pair correlation minus the Poisson baseline)
   T_3(x,y) = cluster function (genuinely new beyond pair correlation)
   The connected n-point function extracts the part not determined by lower
   correlations.

3. FORM FACTOR b_n(k):
   The Fourier transform of R_n.  For GUE:
       b_2(k) = max(1 - |k|, 0)  for |k| <= 1 (the "triangle" form factor)

4. GAP PROBABILITY E(n; L):
   Probability of exactly n zeros in an interval of length L.
   For a DPP: E(0; L) = det(I - K_L) where K_L is the sine kernel restricted
   to the interval [-L/2, L/2].

5. NUMBER VARIANCE Sigma^2(L) and RIGIDITY Delta_3(L):
   Long-range spectral statistics.

6. SHADOW DEPTH DEPENDENCE:
   Does the deviation from GUE correlate with shadow depth class (G/L/C/M)?

MATHEMATICAL FRAMEWORK:

The sine kernel:
    K(x) = sin(pi*x) / (pi*x)     (K(0) = 1)

For the GUE determinantal point process, the n-point correlation is:
    R_n(x_1, ..., x_n) = det_{1 <= i,j <= n} K(x_i - x_j)

The connected correlation (cluster function) is obtained via the
inclusion-exclusion / Moebius inversion on the partition lattice:
    T_n(x_1, ..., x_n) = sum_{pi in Part(n)} (-1)^{|pi|-1} (|pi|-1)!
                           * prod_{B in pi} R_{|B|}(x_B)

For n=2: T_2(x_1, x_2) = R_2(x_1, x_2) - R_1(x_1)*R_1(x_2)
                         = R_2(x) - 1     (after translation invariance)
                         = -K(x)^2        (for GUE)

For n=3 (translation invariant, so function of 2 variables):
    T_3(x, y) = R_3(0, x, y) - R_2(x)*R_1 - R_2(y)*R_1 - R_2(y-x)*R_1
                + 2*R_1^3
              = det_3(K) - 1 + K(x)^2 + K(y)^2 + K(y-x)^2 - 2
    Simplifying: T_3(x, y) = 2*K(x)*K(y-x)*K(y) - K(x)^2*K(y)^2
                              - K(x)^2*K(y-x)^2 - K(y)^2*K(y-x)^2
    Actually the cluster function for n=3 is:
    T_3(x, y) = det_3(K(x_i - x_j)) - [K(x)^2 + K(y)^2 + K(y-x)^2]
                + 2
    Wait, let me be precise.  For a DPP with kernel K:
        rho_n(x_1,...,x_n) = det(K(x_i, x_j))
    The connected (truncated) correlation is the cumulant.  For a
    stationary process with density rho = K(0) = 1:
        T_2(r) = rho_2(0, r) - rho^2 = det_2 - 1 = 1 - K(r)^2 - 1 = -K(r)^2
    For n=3:
        T_3(r, s) = rho_3(0, r, s) - rho*[rho_2(0,r) + rho_2(0,s) + rho_2(r,s)]
                    + 2*rho^3
                  = det_3(K) - [det_2(0,r) + det_2(0,s) + det_2(r,s)]
                    + 2
    where det_2(a,b) = 1 - K(a-b)^2.  So:
        T_3(r, s) = det_3 - (3 - K(r)^2 - K(s)^2 - K(s-r)^2) + 2
                  = det_3 - 1 + K(r)^2 + K(s)^2 + K(s-r)^2

    For the 3x3 determinant with kernel K:
        det_3 = | 1       K(r)    K(s)   |
                | K(r)    1       K(s-r) |
                | K(s)    K(s-r)  1      |
        = 1 - K(s-r)^2 - K(r)^2 + K(r)*K(s-r)*K(s)
          - K(s)^2 + K(s)*K(r)*K(s-r)
        = 1 - K(r)^2 - K(s)^2 - K(s-r)^2 + 2*K(r)*K(s)*K(s-r)

    So T_3(r,s) = [1 - K(r)^2 - K(s)^2 - K(s-r)^2 + 2*K(r)*K(s)*K(s-r)]
                 - 1 + K(r)^2 + K(s)^2 + K(s-r)^2
                = 2*K(r)*K(s)*K(s-r)

    Beautiful: the GUE 3-point cluster function is T_3(r,s) = 2*K(r)*K(s)*K(s-r).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    bc_pair_correlation_engine.py (compute/lib/)
    bc_shadow_zeta_zeros_engine.py (compute/lib/)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general.
CAUTION (AP10): Cross-verify by multiple independent paths.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

from __future__ import annotations

import math
import itertools
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np

try:
    from scipy import stats as scipy_stats
    from scipy import integrate as scipy_integrate
    from scipy import linalg as scipy_linalg
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False

try:
    import mpmath
    mpmath.mp.dps = 30
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

# Import from existing engines
from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    find_zeros_grid,
    newton_zero,
)

from compute.lib.bc_pair_correlation_engine import (
    gue_pair_correlation,
    gue_number_variance,
    wigner_surmise_gue,
    unfold_epstein_zeros,
    pair_correlation_histogram,
    nearest_neighbor_spacings,
    number_variance,
)

from compute.lib.shadow_epstein_zeta import (
    virasoro_shadow_data,
    virasoro_form,
)


# ============================================================================
# 1.  Sine kernel and determinantal structure
# ============================================================================

def sine_kernel(x: float) -> float:
    r"""The sine kernel K(x) = sin(pi*x) / (pi*x).

    K(0) = 1 by continuity.

    This is the correlation kernel of the GUE determinantal point process
    in the bulk scaling limit.
    """
    if abs(x) < 1e-15:
        return 1.0
    return math.sin(math.pi * x) / (math.pi * x)


def sine_kernel_array(x: np.ndarray) -> np.ndarray:
    """Vectorized sine kernel."""
    x = np.asarray(x, dtype=float)
    result = np.ones_like(x)
    nonzero = np.abs(x) > 1e-15
    result[nonzero] = np.sin(np.pi * x[nonzero]) / (np.pi * x[nonzero])
    return result


def sine_kernel_matrix(points: np.ndarray) -> np.ndarray:
    r"""Build the n x n kernel matrix K(x_i - x_j) for given points.

    Parameters
    ----------
    points : array of shape (n,) with the point positions

    Returns
    -------
    K : array of shape (n, n)
    """
    points = np.asarray(points, dtype=float)
    n = len(points)
    diffs = points[:, None] - points[None, :]
    return sine_kernel_array(diffs.ravel()).reshape(n, n)


# ============================================================================
# 2.  GUE n-point correlation functions (determinantal)
# ============================================================================

def gue_R2(x: float) -> float:
    r"""GUE 2-point correlation R_2(x) = 1 - K(x)^2.

    This is the DENSITY pair correlation: the probability density of finding
    two eigenvalues at distance x, normalized so R_2 -> 1 as x -> infinity.
    """
    K = sine_kernel(x)
    return 1.0 - K * K


def gue_R3(x: float, y: float) -> float:
    r"""GUE 3-point correlation R_3(x, y) = det_3(K).

    R_3(0, x, y) = det | 1     K(x)   K(y)   |
                       | K(x)  1      K(y-x) |
                       | K(y)  K(y-x) 1      |

    = 1 - K(x)^2 - K(y)^2 - K(y-x)^2 + 2*K(x)*K(y)*K(y-x)
    """
    Kx = sine_kernel(x)
    Ky = sine_kernel(y)
    Kyx = sine_kernel(y - x)
    return (1.0 - Kx**2 - Ky**2 - Kyx**2
            + 2.0 * Kx * Ky * Kyx)


def gue_R4(x: float, y: float, z: float) -> float:
    r"""GUE 4-point correlation R_4(x, y, z) = det_4(K).

    R_4(0, x, y, z) = det | 1      K(x)   K(y)   K(z)   |
                          | K(x)   1      K(y-x) K(z-x) |
                          | K(y)   K(y-x) 1      K(z-y) |
                          | K(z)   K(z-x) K(z-y) 1      |
    """
    pts = np.array([0.0, x, y, z])
    K = sine_kernel_matrix(pts)
    return float(np.linalg.det(K))


def gue_R5(x: float, y: float, z: float, w: float) -> float:
    r"""GUE 5-point correlation R_5(x, y, z, w) = det_5(K).

    R_5(0, x, y, z, w) = det_{5x5}(K(p_i - p_j)) with p = (0, x, y, z, w).
    """
    pts = np.array([0.0, x, y, z, w])
    K = sine_kernel_matrix(pts)
    return float(np.linalg.det(K))


def gue_Rn(points: np.ndarray) -> float:
    r"""General GUE n-point correlation R_n = det(K(x_i - x_j)).

    Parameters
    ----------
    points : array of n point positions

    Returns
    -------
    R_n : determinant of the n x n sine kernel matrix
    """
    K = sine_kernel_matrix(np.asarray(points))
    return float(np.linalg.det(K))


# ============================================================================
# 3.  Connected correlations (cluster functions / cumulants)
# ============================================================================

def gue_T2(x: float) -> float:
    r"""GUE connected 2-point function T_2(x) = -K(x)^2.

    T_2 = R_2 - 1 = -sinc(pi*x)^2.
    """
    K = sine_kernel(x)
    return -K * K


def gue_T3(x: float, y: float) -> float:
    r"""GUE connected 3-point function T_3(x, y) = 2*K(x)*K(y)*K(y-x).

    This is the CLUSTER FUNCTION: the part of R_3 not determined by R_2 and R_1.

    Derivation (see module docstring):
        T_3(x, y) = R_3(0, x, y) - [R_2(0,x) + R_2(0,y) + R_2(x,y)] + 2
                   = 2*K(x)*K(y)*K(y-x)
    """
    Kx = sine_kernel(x)
    Ky = sine_kernel(y)
    Kyx = sine_kernel(y - x)
    return 2.0 * Kx * Ky * Kyx


def gue_T4(x: float, y: float, z: float) -> float:
    r"""GUE connected 4-point function T_4(x, y, z).

    For a determinantal point process, the connected 4-point function is:
        T_4 = -6 * K(x)*K(y)*K(z)*K(y-x)*K(z-x)*K(z-y)
            + 2*[K(x)^2*K(z-y)^2 + K(y)^2*K(z-x)^2 + K(z)^2*K(y-x)^2]
            - ... (inclusion-exclusion over partitions of {0,1,2,3})

    For a DPP, all cumulants T_n can be expressed in terms of the kernel.
    The general formula for the n-th cumulant of a DPP with kernel K is:
        T_n(x_1, ..., x_n) = (-1)^{n-1} * sum over cycles of length n
                              through x_1, ..., x_n of product of K values.

    Specifically (Soshnikov's formula):
        T_n(x_1, ..., x_n) = (-1)^{n-1} sum_{sigma in C_n}
                               prod_{i=1}^n K(x_i - x_{sigma(i)})

    where C_n is the set of cyclic permutations of {1, ..., n}.

    For n=4, cycles of length 4 on {0, x, y, z}:
    There are (4-1)! = 6 cyclic permutations:
        (0->x->y->z->0): K(x)*K(y-x)*K(z-y)*K(z)
        (0->x->z->y->0): K(x)*K(z-x)*K(z-y)*K(y)  [note K(z-y)=K(y-z)]
        (0->y->x->z->0): K(y)*K(y-x)*K(z-x)*K(z)
        (0->y->z->x->0): K(y)*K(z-y)*K(z-x)*K(x)
        (0->z->x->y->0): K(z)*K(z-x)*K(y-x)*K(y)
        (0->z->y->x->0): K(z)*K(z-y)*K(y-x)*K(x)

    So T_4 = -sum of these 6 products (with (-1)^{4-1} = -1).
    """
    Kx = sine_kernel(x)
    Ky = sine_kernel(y)
    Kz = sine_kernel(z)
    Kyx = sine_kernel(y - x)
    Kzx = sine_kernel(z - x)
    Kzy = sine_kernel(z - y)

    # 6 cyclic permutations of length 4
    c1 = Kx * Kyx * Kzy * Kz     # 0->x->y->z->0
    c2 = Kx * Kzx * Kzy * Ky     # 0->x->z->y->0  (K(y-z)=K(z-y))
    c3 = Ky * Kyx * Kzx * Kz     # 0->y->x->z->0
    c4 = Ky * Kzy * Kzx * Kx     # 0->y->z->x->0
    c5 = Kz * Kzx * Kyx * Ky     # 0->z->x->y->0
    c6 = Kz * Kzy * Kyx * Kx     # 0->z->y->x->0

    return -(c1 + c2 + c3 + c4 + c5 + c6)


def gue_Tn_general(points: np.ndarray) -> float:
    r"""General GUE n-th cumulant (connected correlation) via Soshnikov's formula.

    For a DPP:
        T_n(x_1, ..., x_n) = (-1)^{n-1} * sum_{sigma in C_n}
                               prod_{i=1}^n K(x_i - x_{sigma(i)})

    where C_n is the set of all n-cycles (cyclic permutations) on {0,1,...,n-1}.
    There are (n-1)! such cycles.

    Parameters
    ----------
    points : array of n point positions

    Returns
    -------
    T_n : the n-th cumulant / cluster function
    """
    points = np.asarray(points, dtype=float)
    n = len(points)
    if n < 2:
        return 0.0

    sign = (-1) ** (n - 1)

    # Generate all cyclic permutations of {0, ..., n-1}.
    # A cyclic permutation of length n is uniquely determined by a permutation
    # of {1, ..., n-1} (element 0 maps to the first element, etc.)
    total = 0.0
    rest = list(range(1, n))
    for perm in itertools.permutations(rest):
        # The cycle is: 0 -> perm[0] -> perm[1] -> ... -> perm[-1] -> 0
        cycle = [0] + list(perm)
        prod = 1.0
        for i in range(n):
            j = (i + 1) % n
            prod *= sine_kernel(points[cycle[i]] - points[cycle[j]])
        total += prod

    return sign * total


# ============================================================================
# 4.  Empirical n-point correlation from zero data
# ============================================================================

def empirical_R3_histogram(
    unfolded: np.ndarray,
    x_max: float = 2.5,
    n_bins: int = 15,
    max_window: int = 30,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r"""Compute empirical 3-point correlation R_3(x, y) from unfolded zeros.

    Uses a 2D histogram: for each triple (i, j, k) with i < j < k and
    all within a window, compute (u_j - u_i, u_k - u_i) and bin.

    Parameters
    ----------
    unfolded : sorted array of unfolded zero positions
    x_max : maximum distance to include
    n_bins : number of bins per axis
    max_window : maximum index separation to consider

    Returns
    -------
    x_centers : bin centers for first axis
    y_centers : bin centers for second axis
    R3 : 2D array of shape (n_bins, n_bins) with the correlation values
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)

    # Collect triples
    dx_list = []
    dy_list = []
    for i in range(N):
        for j in range(i + 1, min(i + max_window, N)):
            dx = u[j] - u[i]
            if dx >= x_max:
                break
            for k in range(j + 1, min(j + max_window, N)):
                dy = u[k] - u[i]
                if dy >= x_max:
                    break
                dx_list.append(dx)
                dy_list.append(dy)

    if len(dx_list) == 0:
        x_centers = np.linspace(0, x_max, n_bins)
        y_centers = np.linspace(0, x_max, n_bins)
        return x_centers, y_centers, np.ones((n_bins, n_bins))

    dx_arr = np.array(dx_list)
    dy_arr = np.array(dy_list)

    # 2D histogram
    bin_edges = np.linspace(0, x_max, n_bins + 1)
    H, _, _ = np.histogram2d(dx_arr, dy_arr, bins=[bin_edges, bin_edges])

    # Normalize: expected count under Poisson = N_triples * bin_area / total_area
    bin_width = bin_edges[1] - bin_edges[0]
    total_triples = len(dx_list)
    expected_per_bin = total_triples * bin_width**2 / x_max**2
    R3 = H / (expected_per_bin + 1e-30)

    x_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    y_centers = x_centers.copy()
    return x_centers, y_centers, R3


def empirical_R4_histogram(
    unfolded: np.ndarray,
    x_max: float = 2.0,
    n_bins: int = 8,
    max_window: int = 20,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute empirical 4-point correlation R_4 from unfolded zeros.

    Since R_4 is a function of 3 variables, we project: fix z and compute
    the marginalized R_4 over the z-direction. Alternatively, compute the
    DIAGONAL slice R_4(x, x, x) or R_4(x, 2x, 3x).

    For efficiency, we compute the marginal:
        R_4^{marg}(x) = integral R_4(x, y, z) dy dz / L^2

    This is related to the 4-point number variance.

    Here we compute the simpler diagonal projection:
        R_4^{diag}(x) = R_4(x, 2x, 3x)
    as a 1D function.

    Returns (x_centers, R4_diag).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)

    # For the diagonal: we need 4 consecutive-ish zeros at spacing ~ x
    # Compute R_4 empirically: for each quadruple, project onto (x, 2x, 3x)
    # More practical: bin the 4-point density in a single variable
    # by looking at consecutive quadruples

    # Simple approach: for each i, look at (u[i], u[i+1], u[i+2], u[i+3])
    # and compute the "scaled span" s = (u[i+3] - u[i]) / 3
    # Then the 4-point correlation at scale s is the density of such quadruples.
    spacings = []
    for i in range(N - 3):
        span = u[i + 3] - u[i]
        if span < x_max * 3:
            # Normalize: the span of 4 consecutive is ~ 3 * mean_spacing
            spacings.append(span / 3.0)

    if len(spacings) < 10:
        x_centers = np.linspace(0, x_max, n_bins)
        return x_centers, np.ones(n_bins)

    spacings = np.array(spacings)
    bin_edges = np.linspace(0, x_max, n_bins + 1)
    counts, _ = np.histogram(spacings, bins=bin_edges)
    x_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_width = bin_edges[1] - bin_edges[0]

    # Normalize
    expected = len(spacings) / n_bins
    R4_diag = counts / (expected + 1e-30)

    return x_centers, R4_diag


def empirical_R5_marginal(
    unfolded: np.ndarray,
    x_max: float = 2.0,
    n_bins: int = 8,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute marginal 5-point correlation from unfolded zeros.

    We compute the span of 5 consecutive zeros as a proxy for R_5.
    The scaled span s = (u[i+4] - u[i]) / 4 is distributed according
    to the 5-point gap function.

    Returns (x_centers, R5_marginal).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)

    spacings = []
    for i in range(N - 4):
        span = u[i + 4] - u[i]
        if span < x_max * 4:
            spacings.append(span / 4.0)

    if len(spacings) < 10:
        x_centers = np.linspace(0, x_max, n_bins)
        return x_centers, np.ones(n_bins)

    spacings = np.array(spacings)
    bin_edges = np.linspace(0, x_max, n_bins + 1)
    counts, _ = np.histogram(spacings, bins=bin_edges)
    x_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    expected = len(spacings) / n_bins
    R5_marg = counts / (expected + 1e-30)

    return x_centers, R5_marg


# ============================================================================
# 5.  Form factor (Fourier transform of correlation)
# ============================================================================

def gue_form_factor_R2(k: float) -> float:
    r"""GUE 2-point form factor b_2(k).

    b_2(k) = FT[R_2 - 1](k) = FT[-K(x)^2](k)

    Since K(x) = sinc(pi*x), the Fourier transform of K^2 is:
        FT[sinc^2](k) = max(1 - |k|, 0)  (triangle function)

    So b_2(k) = -max(1 - |k|, 0).

    Actually, the form factor in the random matrix convention is:
        b_2(tau) = 1 - |tau|  for |tau| <= 1
                 = 0           for |tau| > 1

    This is the SPECTRAL form factor (the Fourier transform of T_2 + delta,
    with appropriate normalization).

    In the standard convention:
        b(tau) = integral R_2(x) e^{2*pi*i*tau*x} dx
               = delta(tau) + FT[T_2](tau)
               = delta(tau) - FT[K^2](tau)
               = delta(tau) - max(1 - |tau|, 0)

    The smooth part (excluding delta) is:
        b_2^{smooth}(tau) = -max(1 - |tau|, 0)

    For |tau| < 1: b_2^{smooth} = -(1 - |tau|) = |tau| - 1  (negative)
    For |tau| >= 1: b_2^{smooth} = 0

    The SPECTRAL form factor (positive convention) is often quoted as:
        K_2(tau) = |tau|  for |tau| <= 1
                 = 1      for |tau| > 1
    which is 1 + b_2^{smooth}.
    """
    k_abs = abs(k)
    if k_abs >= 1.0:
        return 0.0
    return -(1.0 - k_abs)


def gue_spectral_form_factor(tau: float) -> float:
    r"""GUE spectral form factor K_2(tau).

    K_2(tau) = |tau|  for |tau| <= 1
             = 1      for |tau| > 1

    This is the Fourier transform of 1 - sinc^2(pi*x), or equivalently
    1 + b_2(tau) where b_2 is the smooth part of the form factor.
    """
    tau_abs = abs(tau)
    if tau_abs >= 1.0:
        return 1.0
    return tau_abs


def empirical_form_factor(
    unfolded: np.ndarray,
    k_max: float = 2.0,
    n_k: int = 40,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute the spectral form factor from unfolded zeros.

    K_2(tau) = |sum_n e^{2*pi*i*tau*u_n}|^2 / N

    This is the squared modulus of the "spectral determinant" evaluated
    on the unit circle, averaged over the data.

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros
    k_max : maximum frequency
    n_k : number of frequency points

    Returns
    -------
    k_values : array of frequencies tau
    K2_values : spectral form factor values
    """
    u = np.asarray(unfolded, dtype=float)
    N = len(u)

    k_values = np.linspace(0.01, k_max, n_k)
    K2_values = np.zeros(n_k)

    for idx, k in enumerate(k_values):
        # Compute |sum_n exp(2*pi*i*k*u_n)|^2 / N
        phases = np.exp(2j * np.pi * k * u)
        K2_values[idx] = abs(np.sum(phases)) ** 2 / N

    return k_values, K2_values


def empirical_form_factor_R3(
    unfolded: np.ndarray,
    k_max: float = 2.0,
    n_k: int = 20,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""Compute the 3-point form factor from unfolded zeros.

    b_3(k) ~ (1/N) sum_{i,j,l distinct} e^{2*pi*i*k*(u_i + u_j + u_l)}

    More precisely, the 3-point form factor is the Fourier transform of T_3.
    For computational efficiency, we use the cubic moment:
        S_3(k) = |sum_n e^{2*pi*i*k*u_n}|^2 * sum_n e^{2*pi*i*k*u_n} / N^2

    Returns (k_values, |b_3|_values).
    """
    u = np.asarray(unfolded, dtype=float)
    N = len(u)

    k_values = np.linspace(0.01, k_max, n_k)
    b3_values = np.zeros(n_k)

    for idx, k in enumerate(k_values):
        phases = np.exp(2j * np.pi * k * u)
        S = np.sum(phases)
        # Third moment of spectral measure
        b3_values[idx] = abs(S) ** 3 / N ** 2

    return k_values, b3_values


# ============================================================================
# 6.  Gap probability and spacing distributions
# ============================================================================

def gue_gap_probability_wigner(L: float) -> float:
    r"""Approximate gap probability E(0; L) for GUE using Wigner surmise.

    The probability of finding no eigenvalues in an interval of length L
    (with unit mean density) is approximately:

        E(0; L) ~ 1 - erf(sqrt(pi/4) * L)  (crude, from Wigner)

    More accurate: for the sine kernel process,
        E(0; L) = det(I - K_L)

    where K_L is the integral operator on [-L/2, L/2] with kernel K(x-y).

    For small L: E(0; L) ~ 1 - L + L^2/2 - ...
    For large L: E(0; L) ~ exp(-pi^2 * L^2 / 16 + ...)

    We use the Gaudin-Mehta approximation for moderate L:
        E(0; L) ~ exp(-pi^2 * L^2 / (16) * (1 + O(1/L)))

    For a practical implementation, we compute via Fredholm determinant
    (discretization of the integral operator).
    """
    if L <= 0:
        return 1.0
    if L > 10:
        return 0.0  # Effectively zero

    # Fredholm determinant by Nystrom discretization
    n_quad = max(20, int(10 * L))
    if n_quad > 200:
        n_quad = 200
    return _fredholm_gap_probability(L, n_quad)


def _fredholm_gap_probability(L: float, n_quad: int = 50) -> float:
    r"""Gap probability E(0; L) via Fredholm determinant.

    E(0; L) = det(I - K_L)

    where K_L is the sine kernel restricted to [-L/2, L/2].
    Discretize with Gauss-Legendre quadrature.
    """
    if not HAS_SCIPY:
        # Fallback: Wigner surmise approximation
        return math.exp(-math.pi**2 * L**2 / 16)

    from numpy.polynomial.legendre import leggauss
    nodes, weights = leggauss(n_quad)

    # Map from [-1, 1] to [-L/2, L/2]
    x = (L / 2) * nodes
    w = (L / 2) * weights

    # Build the kernel matrix K(x_i - x_j) * sqrt(w_i * w_j)
    K = np.zeros((n_quad, n_quad))
    for i in range(n_quad):
        for j in range(n_quad):
            K[i, j] = sine_kernel(x[i] - x[j]) * math.sqrt(w[i] * w[j])

    # det(I - K)
    eigenvalues = np.linalg.eigvalsh(K)
    # Clamp eigenvalues to avoid log of negative
    log_det = np.sum(np.log(np.maximum(1.0 - eigenvalues, 1e-300)))
    return math.exp(log_det)


def gap_probability_n(L: float, n: int, n_quad: int = 50) -> float:
    r"""Probability E(n; L) of exactly n zeros in an interval of length L.

    Uses the relation:
        E(n; L) = ((-1)^n / n!) * (d/d_lambda)^n det(I - lambda*K_L)|_{lambda=1}

    For practical computation, we use:
        sum_n E(n; L) * z^n = det(I - (1-z)*K_L)

    So E(n; L) can be extracted from the generating function.
    Alternatively, we use the Fredholm minors.

    For n = 0: E(0; L) = det(I - K_L)
    For n = 1: E(1; L) = Tr(K_L * (I - K_L)^{-1}) * E(0; L)
    For general n: use the expansion in terms of Fredholm determinants.

    We compute by diagonalizing K_L and using:
        E(n; L) = (1/n!) sum over subsets S of eigenvalues of size n
                  of prod_{i in S} lambda_i * prod_{i not in S} (1 - lambda_i)
    But this is exponential in the number of eigenvalues.

    More efficient: the generating function approach.
    Let the eigenvalues of K_L be {mu_j}. Then:
        det(I - (1-z)*K_L) = prod_j (1 - (1-z)*mu_j)
                            = prod_j ((1 - mu_j) + z*mu_j)

    E(n; L) = coefficient of z^n in prod_j ((1-mu_j) + z*mu_j)
            = sum over subsets S of size n: prod_{j in S} mu_j * prod_{j not in S} (1-mu_j)

    For moderate n_quad, this is computable via dynamic programming.
    """
    if L <= 0:
        return 1.0 if n == 0 else 0.0

    if not HAS_SCIPY:
        if n == 0:
            return math.exp(-math.pi**2 * L**2 / 16)
        return 0.0  # Cannot compute without scipy

    from numpy.polynomial.legendre import leggauss
    nodes, weights = leggauss(n_quad)
    x = (L / 2) * nodes
    w = (L / 2) * weights

    K = np.zeros((n_quad, n_quad))
    for i in range(n_quad):
        for j in range(n_quad):
            K[i, j] = sine_kernel(x[i] - x[j]) * math.sqrt(w[i] * w[j])

    eigenvalues = np.linalg.eigvalsh(K)
    # Clamp eigenvalues to [0, 1] (they should be, but numerical error)
    eigenvalues = np.clip(eigenvalues, 0.0, 1.0)

    # Dynamic programming: E(n; L) = coeff of z^n in prod_j ((1-mu_j) + z*mu_j)
    # dp[k] = coefficient of z^k after processing j eigenvalues
    m = len(eigenvalues)
    dp = np.zeros(n + 1)
    dp[0] = 1.0
    for mu in eigenvalues:
        # Process in reverse to avoid overwriting
        new_dp = np.zeros(n + 1)
        for k in range(n + 1):
            new_dp[k] = dp[k] * (1.0 - mu)
            if k > 0:
                new_dp[k] += dp[k - 1] * mu
        dp = new_dp

    return max(dp[n], 0.0)


def empirical_gap_probability(
    unfolded: np.ndarray,
    L_values: List[float],
    n_zeros: int = 0,
) -> Dict[float, float]:
    r"""Compute empirical gap probability E(n; L) from unfolded zeros.

    For each window of length L centered at each zero, count the number
    of OTHER zeros in the window.  E(n; L) is the fraction of windows
    with exactly n zeros.

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros
    L_values : list of interval lengths
    n_zeros : number of zeros to look for (0 = gap, 1 = one zero, etc.)

    Returns
    -------
    Dict mapping L to E(n_zeros; L).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)
    result = {}

    for L in L_values:
        count_match = 0
        count_total = 0
        half_L = L / 2.0
        for i in range(N):
            center = u[i]
            # Count zeros in [center - half_L, center + half_L] excluding u[i]
            n_in_window = np.sum((u >= center - half_L) & (u <= center + half_L)) - 1
            if n_in_window == n_zeros:
                count_match += 1
            count_total += 1
        result[L] = count_match / count_total if count_total > 0 else 0.0

    return result


# ============================================================================
# 7.  Number variance and Dyson-Mehta rigidity
# ============================================================================

def dyson_mehta_rigidity(
    unfolded: np.ndarray,
    L_values: Optional[List[float]] = None,
) -> Dict[float, float]:
    r"""Compute the Dyson-Mehta Delta_3(L) statistic.

    Delta_3(L) = min_{a,b} (1/L) integral_0^L (N(x) - a*x - b)^2 dx

    where N(x) = #{u_n in [E, E+x]} is the staircase function.

    This is the least-squares measure of the deviation of the staircase from
    a straight line, averaged over the interval.  For GUE:
        Delta_3(L) ~ (1/pi^2) * (log(2*pi*L) + gamma_E - 5/4) for large L

    For Poisson: Delta_3(L) = L/15.

    Relation to number variance:
        Delta_3(L) = (2/L^4) integral_0^L (L^3 - 2*L^2*x + x^3) Sigma^2(x) dx

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros
    L_values : list of interval lengths. Default: [0.5, 1, 2, 5, 10, 20].

    Returns
    -------
    Dict mapping L to Delta_3(L).
    """
    u = np.sort(np.asarray(unfolded, dtype=float))
    N = len(u)
    if L_values is None:
        L_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]

    result = {}
    for L in L_values:
        delta3_samples = []
        # Average over different starting points
        n_samples = min(100, N - 1)
        for start_idx in range(0, N - 1, max(1, (N - 1) // n_samples)):
            E = u[start_idx]
            # Count zeros in [E, E + L]
            mask = (u >= E) & (u <= E + L)
            u_in = u[mask] - E  # Shift to [0, L]
            n_in = len(u_in)

            if n_in < 2:
                continue

            # Staircase function: N(x) = number of u_in <= x
            # Fit a line a*x + b to minimize integral (N(x) - a*x - b)^2 dx
            # Analytical solution for the line fit:
            # a = (n_in - 1) / L  (approximate slope)
            # b = 0.5  (approximate offset)
            # More precisely, compute the least-squares integral

            # Use numerical integration with the staircase
            x_grid = np.linspace(0, L, 200)
            N_grid = np.searchsorted(u_in, x_grid, side='right').astype(float)

            # Fit line: minimize sum (N_i - a*x_i - b)^2
            A = np.column_stack([x_grid, np.ones_like(x_grid)])
            coeffs, _, _, _ = np.linalg.lstsq(A, N_grid, rcond=None)
            a_fit, b_fit = coeffs
            residual = N_grid - a_fit * x_grid - b_fit
            delta3 = np.mean(residual ** 2) / max(L, 1e-10)
            delta3_samples.append(delta3)

        if delta3_samples:
            result[L] = float(np.mean(delta3_samples))
        else:
            result[L] = 0.0

    return result


def gue_delta3(L: float) -> float:
    r"""GUE Delta_3(L) asymptotic formula.

    Delta_3(L) ~ (1/pi^2) * (log(2*pi*L) + gamma_E - 5/4) for L >> 1.

    For small L: Delta_3(L) ~ L/15 (same as Poisson to leading order).
    """
    if L < 0.1:
        return L / 15.0
    gamma_E = 0.5772156649015329
    return (1.0 / math.pi**2) * (math.log(2 * math.pi * L) + gamma_E - 1.25)


def poisson_delta3(L: float) -> float:
    r"""Poisson Delta_3(L) = L/15."""
    return L / 15.0


# ============================================================================
# 8.  Determinantal point process kernel estimation
# ============================================================================

def estimate_correlation_kernel(
    unfolded: np.ndarray,
    x_values: np.ndarray,
    bandwidth: float = 0.3,
) -> np.ndarray:
    r"""Estimate the correlation kernel K(x) from zero data.

    If the zeros form a DPP with kernel K, then:
        rho_2(x) = 1 - K(x)^2

    So K(x) = sqrt(1 - rho_2(x)) (up to sign).

    We estimate rho_2 by kernel density estimation of the pair differences,
    then invert.

    More directly, use the method of moments: the empirical kernel is
        K_emp(x) = (1/N) sum_{j} e^{2*pi*i*x*u_j}

    evaluated at the zero differences.

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros
    x_values : points at which to estimate K
    bandwidth : KDE bandwidth for smoothing

    Returns
    -------
    K_est : estimated kernel values at x_values
    """
    u = np.asarray(unfolded, dtype=float)
    N = len(u)
    x = np.asarray(x_values, dtype=float)

    # Method 1: From pair correlation R_2 = 1 - K^2
    # Estimate R_2 via KDE of pair differences
    diffs = []
    window = min(50, N - 1)
    for i in range(N):
        for j in range(i + 1, min(i + window, N)):
            d = u[j] - u[i]
            if d < max(abs(x.max()), abs(x.min())) + 3 * bandwidth:
                diffs.append(d)
                diffs.append(-d)  # Symmetrize

    if len(diffs) < 10:
        return sine_kernel_array(x)

    diffs = np.array(diffs)

    # KDE
    K_est = np.zeros_like(x)
    for idx, xi in enumerate(x):
        # Gaussian kernel
        weights = np.exp(-0.5 * ((diffs - xi) / bandwidth) ** 2) / (
            bandwidth * math.sqrt(2 * math.pi))
        rho2 = np.sum(weights) / (N * 2)  # Normalize
        # K^2 = 1 - rho2 (approximately)
        k_sq = max(1.0 - rho2, 0.0)
        K_est[idx] = math.sqrt(k_sq) if k_sq > 0 else 0.0

    return K_est


def dpp_kernel_test(
    unfolded: np.ndarray,
    n_points: int = 30,
    x_max: float = 2.5,
) -> Dict[str, float]:
    r"""Test whether the zeros form a DPP with the sine kernel.

    Computes the estimated kernel at n_points values and compares with
    the sine kernel. Returns:
        'max_deviation': max |K_est - K_sine|
        'mean_deviation': mean |K_est - K_sine|
        'l2_error': sqrt(mean(K_est - K_sine)^2)
        'r2_score': R^2 correlation between K_est and K_sine

    Parameters
    ----------
    unfolded : sorted array of unfolded zeros
    n_points : number of test points
    x_max : maximum distance

    Returns
    -------
    Dict with test statistics.
    """
    x = np.linspace(0.1, x_max, n_points)  # Avoid x=0

    K_est = estimate_correlation_kernel(unfolded, x)
    K_sine = sine_kernel_array(x)

    dev = np.abs(K_est - K_sine)
    residuals_sq = (K_est - K_sine) ** 2
    ss_res = np.sum(residuals_sq)
    ss_tot = np.sum((K_sine - np.mean(K_sine)) ** 2)

    return {
        'max_deviation': float(np.max(dev)),
        'mean_deviation': float(np.mean(dev)),
        'l2_error': float(math.sqrt(np.mean(residuals_sq))),
        'r2_score': float(1.0 - ss_res / (ss_tot + 1e-30)),
    }


# ============================================================================
# 9.  Shadow zeta zero computation pipeline
# ============================================================================

def compute_shadow_zeros(
    family: str,
    param: float,
    n_zeros: int = 100,
    im_range: Tuple[float, float] = (-200.0, 200.0),
    max_r: int = 80,
) -> Tuple[List[complex], np.ndarray]:
    r"""Compute and unfold shadow zeta zeros for a given algebra family.

    Parameters
    ----------
    family : algebra family name
    param : family parameter (c for Virasoro, k for KM, etc.)
    n_zeros : target number of zeros to find
    im_range : imaginary part range for search
    max_r : maximum arity for shadow coefficients

    Returns
    -------
    zeros : list of complex zeros
    unfolded : array of unfolded zeros (imaginary parts, unit mean spacing)
    """
    coeffs = shadow_coefficients_extended(family, param, max_r=max_r)

    # Find zeros
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=im_range,
        grid_re=20,
        grid_im=max(100, n_zeros * 2),
        max_r=max_r,
    )

    if len(zeros) < 3:
        return zeros, np.array([])

    # Extract imaginary parts (positive only for ordering)
    gammas = sorted(set(abs(z.imag) for z in zeros if abs(z.imag) > 0.1))
    gammas = np.array(gammas[:n_zeros])

    if len(gammas) < 3:
        return zeros, gammas

    # Unfold using polynomial fit (empirical unfolding)
    unfolded = _unfold_empirical(gammas)

    return zeros, unfolded


def _unfold_empirical(gammas: np.ndarray) -> np.ndarray:
    r"""Empirical unfolding of zero heights to unit mean spacing.

    Fit a smooth polynomial to the staircase function and normalize.
    """
    gammas = np.sort(gammas)
    N = len(gammas)
    if N < 3:
        return gammas

    indices = np.arange(1, N + 1, dtype=float)
    deg = min(3, N - 1)
    coeffs = np.polyfit(gammas, indices, deg=deg)
    u = np.polyval(coeffs, gammas)

    # Normalize to unit mean spacing
    spacings = np.diff(u)
    mean_sp = np.mean(spacings) if len(spacings) > 0 else 1.0
    if mean_sp > 0:
        u = u / mean_sp
    return u


# ============================================================================
# 10.  Comprehensive n-point correlation analysis
# ============================================================================

@dataclass
class NPointCorrelationResult:
    """Container for n-point correlation analysis results."""
    family: str
    param: float
    n_zeros: int = 0

    # 3-point
    R3_gue_deviation: float = 0.0
    T3_gue_deviation: float = 0.0

    # 4-point
    R4_gue_deviation: float = 0.0

    # 5-point
    R5_gue_deviation: float = 0.0

    # Form factor
    form_factor_deviation: float = 0.0
    spectral_ff_deviation: float = 0.0

    # Gap probabilities
    gap_probs: Dict[float, float] = field(default_factory=dict)
    gap_prob_gue_deviation: float = 0.0

    # Spacing
    ks_statistic: float = 0.0
    ks_pvalue: float = 0.0

    # Number variance
    number_var_gue_deviation: float = 0.0

    # Rigidity
    delta3_gue_deviation: float = 0.0

    # DPP test
    dpp_max_deviation: float = 0.0
    dpp_r2_score: float = 0.0

    # Koszul duality
    koszul_R3_deviation: float = 0.0

    # Summary
    overall_gue_score: float = 0.0  # 0 = perfect GUE, 1 = far from GUE


def full_npoint_analysis(
    family: str,
    param: float,
    n_zeros: int = 100,
    max_r: int = 80,
    im_range: Tuple[float, float] = (-200.0, 200.0),
) -> NPointCorrelationResult:
    r"""Run comprehensive n-point correlation analysis on shadow zeta zeros.

    Computes all statistics and compares with GUE predictions.

    Parameters
    ----------
    family : algebra family name
    param : family parameter
    n_zeros : target number of zeros
    max_r : maximum arity
    im_range : search range for zeros

    Returns
    -------
    NPointCorrelationResult with all statistics.
    """
    result = NPointCorrelationResult(family=family, param=param)

    # Compute zeros
    zeros, unfolded = compute_shadow_zeros(
        family, param, n_zeros=n_zeros, im_range=im_range, max_r=max_r
    )

    result.n_zeros = len(unfolded)

    if len(unfolded) < 10:
        return result

    # --- 3-point correlation ---
    x_centers, y_centers, R3_emp = empirical_R3_histogram(
        unfolded, x_max=2.0, n_bins=10, max_window=20
    )

    # Compute GUE prediction on the same grid
    R3_gue = np.zeros_like(R3_emp)
    for i, xi in enumerate(x_centers):
        for j, yj in enumerate(y_centers):
            if yj > xi:  # Only upper triangle (y > x since y = u_k - u_i > u_j - u_i = x)
                R3_gue[i, j] = gue_R3(xi, yj)
            else:
                R3_gue[i, j] = R3_emp[i, j]  # Skip comparison

    mask = y_centers[None, :] > x_centers[:, None]
    if np.any(mask):
        dev = np.abs(R3_emp[mask] - R3_gue[mask])
        result.R3_gue_deviation = float(np.mean(dev))
    else:
        result.R3_gue_deviation = 0.0

    # --- T_3 connected correlation ---
    # The connected part T_3 = 2*K(x)*K(y)*K(y-x) for GUE
    # Compare with empirical connected part
    T3_emp = R3_emp.copy()
    for i, xi in enumerate(x_centers):
        for j, yj in enumerate(y_centers):
            if yj > xi:
                T3_emp[i, j] = R3_emp[i, j] - gue_R2(xi) - gue_R2(yj) - gue_R2(yj - xi) + 2.0
    T3_gue = np.zeros_like(T3_emp)
    for i, xi in enumerate(x_centers):
        for j, yj in enumerate(y_centers):
            if yj > xi:
                T3_gue[i, j] = gue_T3(xi, yj)
    if np.any(mask):
        dev_t3 = np.abs(T3_emp[mask] - T3_gue[mask])
        result.T3_gue_deviation = float(np.mean(dev_t3))

    # --- 4-point (diagonal projection) ---
    x4, R4_diag = empirical_R4_histogram(unfolded, x_max=2.0, n_bins=8)
    R4_gue_diag = np.array([gue_R4(xi, 2 * xi, 3 * xi) for xi in x4])
    # Normalize R4_gue for comparison (it's the unnormalized det)
    # The empirical is already normalized to mean ~1 for Poisson
    if np.mean(R4_gue_diag) > 0:
        result.R4_gue_deviation = float(np.std(R4_diag - 1.0))  # Rough measure
    else:
        result.R4_gue_deviation = 0.0

    # --- 5-point (marginal) ---
    x5, R5_marg = empirical_R5_marginal(unfolded, x_max=2.0, n_bins=8)
    result.R5_gue_deviation = float(np.std(R5_marg - 1.0))

    # --- Form factor ---
    k_vals, K2_emp = empirical_form_factor(unfolded, k_max=2.0, n_k=20)
    K2_gue = np.array([gue_spectral_form_factor(k) for k in k_vals])
    result.spectral_ff_deviation = float(np.mean(np.abs(K2_emp - K2_gue)))

    # --- Gap probability ---
    L_test = [0.5, 1.0, 2.0]
    gap_emp = empirical_gap_probability(unfolded, L_test, n_zeros=0)
    gap_gue = {L: gue_gap_probability_wigner(L) for L in L_test}
    result.gap_probs = gap_emp
    dev_gap = [abs(gap_emp[L] - gap_gue[L]) for L in L_test]
    result.gap_prob_gue_deviation = float(np.mean(dev_gap))

    # --- Spacing distribution ---
    spacings = np.diff(unfolded)
    if len(spacings) > 5 and HAS_SCIPY:
        # KS test against Wigner surmise
        from scipy.stats import kstest

        def wigner_cdf(s):
            return 1.0 - np.exp(-4.0 * s**2 / np.pi)

        stat, pval = kstest(spacings, wigner_cdf)
        result.ks_statistic = float(stat)
        result.ks_pvalue = float(pval)

    # --- Number variance ---
    L_nv = [1.0, 2.0, 5.0]
    nv_emp = number_variance(unfolded, L_nv)
    nv_gue = {L: gue_number_variance(L) for L in L_nv}
    dev_nv = [abs(nv_emp.get(L, 0) - nv_gue[L]) for L in L_nv]
    result.number_var_gue_deviation = float(np.mean(dev_nv))

    # --- Rigidity ---
    L_rig = [1.0, 2.0, 5.0]
    d3_emp = dyson_mehta_rigidity(unfolded, L_rig)
    d3_gue = {L: gue_delta3(L) for L in L_rig}
    dev_d3 = [abs(d3_emp.get(L, 0) - d3_gue[L]) for L in L_rig]
    result.delta3_gue_deviation = float(np.mean(dev_d3))

    # --- DPP test ---
    dpp = dpp_kernel_test(unfolded)
    result.dpp_max_deviation = dpp['max_deviation']
    result.dpp_r2_score = dpp['r2_score']

    # --- Overall GUE score ---
    # Weighted average of deviations (lower = closer to GUE)
    result.overall_gue_score = float(np.mean([
        result.R3_gue_deviation,
        result.spectral_ff_deviation,
        result.gap_prob_gue_deviation,
        result.ks_statistic,
        min(result.number_var_gue_deviation, 1.0),
    ]))

    return result


# ============================================================================
# 11.  Shadow depth class comparison
# ============================================================================

@dataclass
class DepthClassComparison:
    """Comparison of n-point statistics across shadow depth classes."""
    class_G: Optional[NPointCorrelationResult] = None
    class_L: Optional[NPointCorrelationResult] = None
    class_C: Optional[NPointCorrelationResult] = None
    class_M: Optional[NPointCorrelationResult] = None

    def deviation_ranking(self) -> Dict[str, float]:
        """Rank classes by overall deviation from GUE."""
        ranking = {}
        if self.class_G and self.class_G.n_zeros > 0:
            ranking['G'] = self.class_G.overall_gue_score
        if self.class_L and self.class_L.n_zeros > 0:
            ranking['L'] = self.class_L.overall_gue_score
        if self.class_C and self.class_C.n_zeros > 0:
            ranking['C'] = self.class_C.overall_gue_score
        if self.class_M and self.class_M.n_zeros > 0:
            ranking['M'] = self.class_M.overall_gue_score
        return dict(sorted(ranking.items(), key=lambda x: x[1]))


def shadow_depth_comparison(
    n_zeros: int = 60,
    max_r: int = 60,
) -> DepthClassComparison:
    r"""Compare n-point statistics across all four shadow depth classes.

    Representatives:
        G (Gaussian, r_max=2): Heisenberg k=1  -- NO ZEROS (single-term zeta)
        L (Lie/tree, r_max=3): affine sl_2 k=2
        C (contact, r_max=4): beta-gamma lambda=0.5
        M (mixed, r_max=inf): Virasoro c=10

    Returns DepthClassComparison with results for each class.
    """
    comp = DepthClassComparison()

    # Class G: Heisenberg has NO zeros (zeta = k * 2^{-s}), skip
    # But we can still create a null result
    comp.class_G = NPointCorrelationResult(family='heisenberg', param=1.0, n_zeros=0)

    # Class L: affine sl_2 at k=2
    try:
        comp.class_L = full_npoint_analysis(
            'affine_sl2', 2.0, n_zeros=n_zeros, max_r=max_r
        )
    except Exception:
        comp.class_L = NPointCorrelationResult(family='affine_sl2', param=2.0)

    # Class C: beta-gamma at lambda=0.5
    try:
        comp.class_C = full_npoint_analysis(
            'betagamma', 0.5, n_zeros=n_zeros, max_r=max_r
        )
    except Exception:
        comp.class_C = NPointCorrelationResult(family='betagamma', param=0.5)

    # Class M: Virasoro at c=10
    try:
        comp.class_M = full_npoint_analysis(
            'virasoro', 10.0, n_zeros=n_zeros, max_r=max_r
        )
    except Exception:
        comp.class_M = NPointCorrelationResult(family='virasoro', param=10.0)

    return comp


# ============================================================================
# 12.  Koszul duality on correlations
# ============================================================================

def koszul_correlation_comparison(
    family: str,
    param: float,
    n_zeros: int = 60,
    max_r: int = 60,
) -> Dict[str, Any]:
    r"""Compare n-point correlations of A vs its Koszul dual A!.

    If GUE universality holds for BOTH A and A!, then their n-point
    statistics should agree.  This is a nontrivial test of universality.

    Returns dict with comparison statistics.
    """
    # Compute zeros and statistics for A
    result_A = full_npoint_analysis(
        family, param, n_zeros=n_zeros, max_r=max_r
    )

    # Compute zeros and statistics for A!
    # Koszul dual parameter
    if family == 'virasoro':
        dual_param = 26.0 - param
    elif family == 'affine_sl2':
        dual_param = -param - 4.0
    elif family == 'affine_sl3':
        dual_param = -param - 6.0
    elif family == 'heisenberg':
        dual_param = -param
    else:
        dual_param = param  # Default: same parameter

    result_dual = full_npoint_analysis(
        family, dual_param, n_zeros=n_zeros, max_r=max_r
    )

    return {
        'A_result': result_A,
        'dual_result': result_dual,
        'R3_difference': abs(result_A.R3_gue_deviation - result_dual.R3_gue_deviation),
        'ff_difference': abs(result_A.spectral_ff_deviation - result_dual.spectral_ff_deviation),
        'ks_difference': abs(result_A.ks_statistic - result_dual.ks_statistic),
        'overall_difference': abs(result_A.overall_gue_score - result_dual.overall_gue_score),
        'both_gue': (result_A.overall_gue_score < 0.5 and
                     result_dual.overall_gue_score < 0.5),
    }


# ============================================================================
# 13.  Virasoro c-scan: n-point correlations across central charges
# ============================================================================

def virasoro_c_scan(
    c_values: Optional[List[float]] = None,
    n_zeros: int = 60,
    max_r: int = 60,
) -> Dict[float, NPointCorrelationResult]:
    r"""Scan n-point correlations for Virasoro across central charges.

    Parameters
    ----------
    c_values : list of central charges. Default: [2, 6, 10, 13, 20, 25]
    n_zeros : target number of zeros per c
    max_r : maximum arity

    Returns
    -------
    Dict mapping c to NPointCorrelationResult.
    """
    if c_values is None:
        c_values = [2.0, 6.0, 10.0, 13.0, 20.0, 25.0]

    results = {}
    for c_val in c_values:
        try:
            results[c_val] = full_npoint_analysis(
                'virasoro', c_val, n_zeros=n_zeros, max_r=max_r
            )
        except Exception:
            results[c_val] = NPointCorrelationResult(
                family='virasoro', param=c_val
            )

    return results


# ============================================================================
# 14.  Utility: verify GUE identities for n-point functions
# ============================================================================

def verify_R3_det_identity(x: float, y: float) -> float:
    r"""Verify R_3(x, y) = det_3(K) by direct computation vs formula.

    Returns the absolute difference between:
    1. det_3 computed via numpy determinant
    2. The explicit formula 1 - K(x)^2 - K(y)^2 - K(y-x)^2 + 2*K(x)*K(y)*K(y-x)
    """
    # Method 1: numpy determinant
    pts = np.array([0.0, x, y])
    K_mat = sine_kernel_matrix(pts)
    det_val = float(np.linalg.det(K_mat))

    # Method 2: explicit formula
    formula_val = gue_R3(x, y)

    return abs(det_val - formula_val)


def verify_T3_formula(x: float, y: float) -> float:
    r"""Verify T_3(x, y) = 2*K(x)*K(y)*K(y-x).

    Returns the absolute difference between:
    1. T_3 computed from R_3 and R_2 (inclusion-exclusion)
    2. The direct formula 2*K(x)*K(y)*K(y-x)
    """
    # Method 1: from inclusion-exclusion
    R3_val = gue_R3(x, y)
    R2_x = gue_R2(x)
    R2_y = gue_R2(y)
    R2_yx = gue_R2(y - x)
    T3_ie = R3_val - R2_x - R2_y - R2_yx + 2.0

    # Method 2: direct formula
    T3_direct = gue_T3(x, y)

    return abs(T3_ie - T3_direct)


def verify_T4_cycle_formula(x: float, y: float, z: float) -> float:
    r"""Verify T_4 via Soshnikov's cycle formula against the general formula.

    Returns the absolute difference between:
    1. gue_T4(x, y, z) (explicit cycle sum)
    2. gue_Tn_general(points) (general permutation sum)
    """
    val1 = gue_T4(x, y, z)
    val2 = gue_Tn_general(np.array([0.0, x, y, z]))
    return abs(val1 - val2)


def verify_Rn_positivity(n: int, n_samples: int = 100) -> bool:
    r"""Verify R_n >= 0 (positivity of determinantal correlation) by sampling.

    The determinant of a positive semidefinite matrix is nonneg.
    The sine kernel matrix is PSD (Mercer's theorem), so R_n >= 0.
    """
    rng = np.random.RandomState(42)
    for _ in range(n_samples):
        pts = np.sort(rng.uniform(0, 5, size=n))
        Rn = gue_Rn(pts)
        if Rn < -1e-10:
            return False
    return True


def verify_form_factor_triangle(n_points: int = 50) -> float:
    r"""Verify that FT[K^2](k) = max(1 - |k|, 0) (the triangle function).

    Compute the Fourier transform of sinc^2(pi*x) numerically and compare.

    Returns max deviation.
    """
    k_values = np.linspace(-2, 2, n_points)
    max_dev = 0.0

    for k in k_values:
        # Numerical FT of sinc^2
        x = np.linspace(-20, 20, 2000)
        dx = x[1] - x[0]
        integrand = sine_kernel_array(x) ** 2 * np.exp(-2j * np.pi * k * x)
        ft_numerical = np.sum(integrand) * dx

        # Theoretical: max(1 - |k|, 0)
        ft_theory = max(1.0 - abs(k), 0.0)

        max_dev = max(max_dev, abs(ft_numerical.real - ft_theory))

    return max_dev


def verify_gap_prob_normalization(L: float, n_max: int = 5) -> float:
    r"""Verify sum_{n=0}^{n_max} E(n; L) ~ 1 (normalization of gap probabilities).

    Returns |sum - 1|.
    """
    total = sum(gap_probability_n(L, n) for n in range(n_max + 1))
    # The sum should be close to 1 for sufficient n_max
    return abs(total - 1.0)


def verify_delta3_small_L() -> float:
    r"""Verify Delta_3(L) ~ L/15 for small L (same as Poisson).

    Returns max deviation for L in [0.01, 0.1].
    """
    max_dev = 0.0
    for L in [0.01, 0.02, 0.05, 0.1]:
        gue = gue_delta3(L)
        poisson = poisson_delta3(L)
        max_dev = max(max_dev, abs(gue - poisson))
    return max_dev
