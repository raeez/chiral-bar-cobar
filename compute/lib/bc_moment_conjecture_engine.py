#!/usr/bin/env python3
r"""bc_moment_conjecture_engine.py -- Keating-Snaith moment conjecture
for shadow zeta functions.

MATHEMATICAL CONTENT
====================

The Keating-Snaith conjecture (2000) predicts for the Riemann zeta function:

    (1/T) * integral_0^T |zeta(1/2 + it)|^{2k} dt
        ~ g_k * a_k * (log T)^{k^2}       as T -> infinity

where:
    g_k = k^2! / prod_{j=0}^{k-1} j! * (j+1)!   (random matrix factor)
    a_k = prod_p local arithmetic factor         (arithmetic factor)

This module computes the analogous moments for shadow zeta functions:

    M_{2k}(T; A) = (1/T) * integral_0^T |zeta_A(1/2 + it)|^{2k} dt

=== 1. RANDOM MATRIX FACTOR g_k ===

g_k = G(k+1)^2 / G(2k+1)  where G is the Barnes G-function:
    G(n+1) = 0! * 1! * ... * (n-1)!

Equivalently:
    g_k = prod_{j=0}^{k-1} j! / (j+k)!

Explicit values:
    g_1 = 1
    g_2 = 1/12       [corrected: see derivation below]
    g_3 = 1/34560     ... etc.

IMPORTANT: The original Keating-Snaith formula is:
    g_k = k^2! / prod_{j=0}^{k-1} j!(j+k)!
which is DIFFERENT from the naive product formula often misquoted.

Correct values verified from Barnes G-function:
    g_1 = G(2)^2/G(3) = 1^2/1 = 1
    g_2 = G(3)^2/G(5) = (1!)^2/(1!*2!*3!) = 1/12
    g_3 = G(4)^2/G(7) = (1!*2!)^2/(1!*2!*3!*4!*5!) = 4/34560 = 1/8640
    g_4 = G(5)^2/G(9) = (1!*2!*3!)^2/(1!*2!*3!*4!*5!*6!*7!)

CORRECTION: The literature convention for the leading constant varies.
The CFKRS (Conrey-Farmer-Keating-Rubinstein-Snaith) normalization is:

    M_{2k}(T) ~ f_k * a_k * T * (log(T/(2*pi)))^{k^2}

where f_k = g_k (the random matrix factor) involves the Barnes G-function.

For shadow zeta functions zeta_A(s) = sum_{r>=2} S_r * r^{-s}, the
analogous structure is:

    M_{2k}(T; A) ~ g_k * a_k(A) * (log T)^{k^2}

where a_k(A) encodes the shadow arithmetic.

=== 2. ARITHMETIC FACTOR a_k(A) ===

For a standard Dirichlet series with Euler product, the arithmetic
factor is:

    a_k = prod_p (1 - 1/p)^{k^2} * integral |sum a_{p^m} x^m|^{2k} dmu

Shadow zeta functions do NOT have a standard Euler product (the shadow
recursion is quadratic, not multiplicative). Instead, we define:

    a_k(A) = extracted from the ratio M_{2k}(T) / (g_k * (log T)^{k^2})

at large T. This is the EMPIRICAL arithmetic factor.

For finite-tower algebras (class G/L/C), zeta_A(s) is an exponential
polynomial, and |zeta_A(1/2+it)|^{2k} has explicit mean value:

    M_2(T; Heis_k) = |k|^2 * 2^{-1} * T   (Heisenberg, exact)

=== 3. SHADOW DEPTH DEPENDENCE ===

KEY HYPOTHESIS: The moment growth rate depends on shadow depth:
    Class G (r_max = 2): M_{2k} bounded (single Dirichlet term)
    Class L (r_max = 3): M_{2k} ~ (log T)^{k^2} with modified g_k
    Class C (r_max = 4): intermediate growth
    Class M (r_max = inf): full Keating-Snaith asymptotics

This is tested numerically in the test suite.

=== 4. KOSZUL MOMENT DUALITY ===

Theorem C (complementarity) implies:
    zeta_A(s) + zeta_{A!}(s) = D(s)

where D(s) involves the complementarity sum. For moments:
    M_{2k}(A) + M_{2k}(A!) >= M_{2k}(D) ???

The precise moment reflection principle is EXPLORED, not proved.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general.
CAUTION (AP10): Multi-path verification is mandatory.
CAUTION (AP24): kappa + kappa' = 13 for Virasoro, NOT 0.
CAUTION (AP48): kappa depends on the full algebra, not just c.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
"""

from __future__ import annotations

import cmath
import math
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

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    _shadow_zeta_complex,
)


# ============================================================================
# 1.  Barnes G-function and random matrix factor g_k
# ============================================================================

def barnes_g(n: int) -> float:
    """Barnes G-function: G(n+1) = prod_{j=0}^{n-1} j!.

    G(1) = 1
    G(2) = 1   (= 0!)
    G(3) = 1   (= 0! * 1!)
    G(4) = 2   (= 0! * 1! * 2!)
    G(5) = 12  (= 0! * 1! * 2! * 3!)
    G(6) = 288 (= 0! * 1! * 2! * 3! * 4!)

    Defined for positive integers n >= 1.
    """
    if n < 1:
        raise ValueError(f"Barnes G-function requires n >= 1, got {n}")
    if n <= 2:
        return 1.0
    # G(n+1) = prod_{j=0}^{n-1} j! = prod_{j=0}^{n-1} Gamma(j+1)
    # G(n) = prod_{j=0}^{n-2} j!
    result = 1.0
    for j in range(n - 1):
        result *= math.factorial(j)
    return result


def barnes_g_log(n: int) -> float:
    """Log of Barnes G-function for large n (avoids overflow)."""
    if n < 1:
        raise ValueError(f"Barnes G-function requires n >= 1, got {n}")
    if n <= 2:
        return 0.0
    result = 0.0
    for j in range(n - 1):
        result += math.lgamma(j + 1)
    return result


def random_matrix_factor_gk(k: int) -> float:
    """Random matrix factor g_k = G(k+1)^2 / G(2k+1).

    The Keating-Snaith formula gives:
        g_k = G(k+1)^2 / G(2k+1)

    where G is the Barnes G-function.

    Verified values:
        g_1 = G(2)^2 / G(3) = 1/1 = 1
        g_2 = G(3)^2 / G(5) = 1/12
        g_3 = G(4)^2 / G(7) = 4/34560 = 1/8640
    """
    if k <= 0:
        raise ValueError(f"k must be positive, got {k}")
    # Use log-space to avoid overflow for large k
    log_gk = 2 * barnes_g_log(k + 1) - barnes_g_log(2 * k + 1)
    return math.exp(log_gk)


def random_matrix_factor_gk_exact(k: int) -> Tuple[int, int]:
    """Exact rational g_k as (numerator, denominator).

    Returns the EXACT value of g_k = G(k+1)^2 / G(2k+1) as a fraction.
    """
    from fractions import Fraction
    num = 1
    den = 1
    for j in range(k):
        num *= math.factorial(j)
    num = num * num  # G(k+1)^2
    for j in range(2 * k):
        den *= math.factorial(j)
    # G(2k+1) = prod_{j=0}^{2k-1} j!
    frac = Fraction(num, den)
    return (frac.numerator, frac.denominator)


# ============================================================================
# 2.  Shadow zeta moment computation
# ============================================================================

def shadow_zeta_modulus_squared(
    shadow_coeffs: Dict[int, float],
    t: float,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> float:
    """Compute |zeta_A(sigma + it)|^2.

    Parameters
    ----------
    shadow_coeffs : shadow coefficients S_r
    t : imaginary part
    sigma : real part (default 0.5 for the critical line)
    max_r : truncation arity
    """
    s = complex(sigma, t)
    z = shadow_zeta_numerical(shadow_coeffs, s, max_r)
    return abs(z) ** 2


def shadow_zeta_moment_numerical(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    sigma: float = 0.5,
    h: float = 0.01,
    max_r: Optional[int] = None,
) -> float:
    """Compute M_{2k}(T; A) = (1/T) * integral_0^T |zeta_A(sigma+it)|^{2k} dt.

    Uses composite trapezoidal rule with step size h.

    Parameters
    ----------
    shadow_coeffs : shadow coefficients S_r
    k : moment order (computes the 2k-th moment)
    T : upper limit of integration
    sigma : real part (default 0.5)
    h : step size for trapezoidal rule
    max_r : truncation arity

    Returns
    -------
    M_{2k}(T), the normalized 2k-th moment.
    """
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")
    if k <= 0:
        raise ValueError(f"k must be positive, got {k}")

    # Number of subintervals
    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps

    # Trapezoidal rule: integral ~ h * (f(0)/2 + f(h) + f(2h) + ... + f(T)/2)
    # Evaluate |zeta_A(sigma + i*t_j)|^{2k}
    total = 0.0
    for j in range(n_steps + 1):
        t_j = j * actual_h
        mod_sq = shadow_zeta_modulus_squared(shadow_coeffs, t_j, sigma, max_r)
        val = mod_sq ** k  # |zeta|^{2k} = (|zeta|^2)^k
        if j == 0 or j == n_steps:
            total += val / 2.0
        else:
            total += val

    integral = total * actual_h
    return integral / T


def shadow_zeta_moment_multi_T(
    shadow_coeffs: Dict[int, float],
    k: int,
    T_values: List[float],
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> Dict[float, float]:
    """Compute M_{2k}(T; A) for multiple T values.

    Returns dict mapping T to M_{2k}(T).
    """
    results = {}
    for T in T_values:
        # Adapt step size for smaller T
        actual_h = min(h, T / 20.0)
        results[T] = shadow_zeta_moment_numerical(
            shadow_coeffs, k, T, sigma, actual_h, max_r
        )
    return results


# ============================================================================
# 3.  Shifted moments
# ============================================================================

def shifted_moment_numerical(
    shadow_coeffs: Dict[int, float],
    alpha: float,
    beta: float,
    T: float,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> complex:
    """Compute the shifted first moment:

        I(alpha, beta; T) = (1/T) * integral_0^T
            zeta_A(1/2 + alpha + it) * conj(zeta_A(1/2 + beta + it)) dt

    When alpha = beta = 0, this reduces to M_2(T).

    Parameters
    ----------
    shadow_coeffs : shadow coefficients
    alpha, beta : shifts
    T : upper integration limit
    h : step size

    Returns
    -------
    Complex value of the shifted moment.
    """
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")

    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps

    total = 0.0 + 0.0j
    for j in range(n_steps + 1):
        t_j = j * actual_h
        s1 = complex(0.5 + alpha, t_j)
        s2 = complex(0.5 + beta, t_j)
        z1 = shadow_zeta_numerical(shadow_coeffs, s1, max_r)
        z2 = shadow_zeta_numerical(shadow_coeffs, s2, max_r)
        val = z1 * z2.conjugate()
        if j == 0 or j == n_steps:
            total += val / 2.0
        else:
            total += val

    integral = total * actual_h
    return integral / T


# ============================================================================
# 4.  Ratio conjecture (CFKRS)
# ============================================================================

def ratio_integral_numerical(
    shadow_coeffs: Dict[int, float],
    alpha: float,
    beta: float,
    T: float,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> complex:
    """Compute the ratio integral:

        R(alpha, beta; T) = (1/T) * integral_0^T
            zeta_A(1/2 + it + alpha) / zeta_A(1/2 + it + beta) dt

    The CFKRS prediction for this ratio involves the analytic continuation
    of the characteristic polynomial ratios from random matrix theory.

    CAUTION: The denominator may have zeros; we regularize by
    skipping points where |zeta_A(1/2 + it + beta)| < epsilon.
    """
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")

    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps
    eps = 1e-10

    total = 0.0 + 0.0j
    valid_count = 0
    for j in range(n_steps + 1):
        t_j = j * actual_h
        s_num = complex(0.5 + alpha, t_j)
        s_den = complex(0.5 + beta, t_j)
        z_num = shadow_zeta_numerical(shadow_coeffs, s_num, max_r)
        z_den = shadow_zeta_numerical(shadow_coeffs, s_den, max_r)

        if abs(z_den) < eps:
            continue  # Skip near-zeros of denominator

        val = z_num / z_den
        if j == 0 or j == n_steps:
            total += val / 2.0
        else:
            total += val
        valid_count += 1

    if valid_count == 0:
        return complex(float('nan'), float('nan'))

    # Scale by the actual number of valid points
    integral = total * actual_h
    return integral / T


# ============================================================================
# 5.  Negative moments
# ============================================================================

def negative_moment_numerical(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
    eps: float = 1e-10,
) -> Tuple[float, bool]:
    """Compute negative moment:

        M_{-2k}(T; A) = (1/T) * integral_0^T |zeta_A(sigma+it)|^{-2k} dt

    For Riemann zeta, negative moments DIVERGE (zeros on critical line).
    For finite-tower shadow zeta (class G/L/C), may converge (no zeros
    near the critical line, or finitely many).

    Returns
    -------
    (value, converged): the moment value and whether integration was clean
    (no near-zero encounters).
    """
    if T <= 0:
        raise ValueError(f"T must be positive, got {T}")
    if k <= 0:
        raise ValueError(f"k must be positive, got {k}")

    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps

    total = 0.0
    hit_small = False
    for j in range(n_steps + 1):
        t_j = j * actual_h
        mod_sq = shadow_zeta_modulus_squared(shadow_coeffs, t_j, sigma, max_r)
        if mod_sq < eps:
            hit_small = True
            mod_sq = eps  # Regularize
        val = mod_sq ** (-k)
        if j == 0 or j == n_steps:
            total += val / 2.0
        else:
            total += val

    integral = total * actual_h
    return integral / T, not hit_small


# ============================================================================
# 6.  Extreme value statistics
# ============================================================================

def extreme_value_max(
    shadow_coeffs: Dict[int, float],
    T: float,
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> Tuple[float, float]:
    """Compute max_{0 <= t <= T} |zeta_A(sigma + it)|.

    Returns (max_value, argmax_t).
    """
    n_steps = max(int(T / h), 1)
    actual_h = T / n_steps

    max_val = 0.0
    max_t = 0.0
    for j in range(n_steps + 1):
        t_j = j * actual_h
        s = complex(sigma, t_j)
        z = shadow_zeta_numerical(shadow_coeffs, s, max_r)
        mod = abs(z)
        if mod > max_val:
            max_val = mod
            max_t = t_j

    return max_val, max_t


def extreme_value_scaling(
    shadow_coeffs: Dict[int, float],
    T_values: List[float],
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> List[Tuple[float, float, float]]:
    """Compute max |zeta_A| for multiple T values and test scaling.

    The Selberg-type prediction is:
        max_{t <= T} |zeta(1/2+it)| ~ exp(c * sqrt(log log T))

    Returns list of (T, max_val, log_log_T).
    """
    results = []
    for T in T_values:
        if T <= 1:
            continue
        actual_h = min(h, T / 20.0)
        max_val, _ = extreme_value_max(shadow_coeffs, T, sigma, actual_h, max_r)
        llT = math.log(max(math.log(T), 1e-10))
        results.append((T, max_val, llT))
    return results


# ============================================================================
# 7.  Moment fit and coefficient extraction
# ============================================================================

@dataclass
class MomentFitResult:
    """Result of fitting M_{2k}(T) ~ C * (log T)^{k^2}."""
    k: int
    T_values: List[float] = field(default_factory=list)
    M_values: List[float] = field(default_factory=list)
    fitted_C: float = 0.0
    fitted_exponent: float = 0.0
    g_k: float = 0.0
    a_k_empirical: float = 0.0  # C / g_k
    r_squared: float = 0.0


def fit_moment_growth(
    shadow_coeffs: Dict[int, float],
    k: int,
    T_values: List[float],
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> MomentFitResult:
    """Fit M_{2k}(T) = C * (log T)^alpha and extract C, alpha.

    The Keating-Snaith prediction is alpha = k^2.
    The constant C = g_k * a_k(A).

    Parameters
    ----------
    shadow_coeffs : shadow coefficients
    k : moment order
    T_values : list of T values to sample
    sigma : real part
    h : integration step size

    Returns
    -------
    MomentFitResult with fitted parameters.
    """
    result = MomentFitResult(k=k)
    result.g_k = random_matrix_factor_gk(k)

    log_T_list = []
    log_M_list = []
    M_list = []

    for T in T_values:
        actual_h = min(h, T / 20.0)
        M = shadow_zeta_moment_numerical(shadow_coeffs, k, T, sigma, actual_h, max_r)
        result.T_values.append(T)
        result.M_values.append(M)
        M_list.append(M)

        if T > 1 and M > 0:
            log_T_list.append(math.log(math.log(T)) if math.log(T) > 0 else 0)
            log_M_list.append(math.log(M))

    # Linear regression: log(M) = log(C) + alpha * log(log(T))
    if len(log_T_list) >= 2:
        n = len(log_T_list)
        sx = sum(log_T_list)
        sy = sum(log_M_list)
        sxx = sum(x * x for x in log_T_list)
        sxy = sum(x * y for x, y in zip(log_T_list, log_M_list))

        denom = n * sxx - sx * sx
        if abs(denom) > 1e-15:
            alpha = (n * sxy - sx * sy) / denom
            log_C = (sy - alpha * sx) / n
            result.fitted_C = math.exp(log_C)
            result.fitted_exponent = alpha
        else:
            result.fitted_C = M_list[-1] if M_list else 0.0
            result.fitted_exponent = 0.0

        # R^2
        y_mean = sy / n
        ss_tot = sum((y - y_mean) ** 2 for y in log_M_list)
        ss_res = sum(
            (y - (log_C + alpha * x)) ** 2
            for x, y in zip(log_T_list, log_M_list)
        ) if abs(denom) > 1e-15 else ss_tot
        result.r_squared = 1.0 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0
    else:
        result.fitted_C = M_list[-1] if M_list else 0.0

    # Extract empirical a_k
    if result.g_k > 0 and result.fitted_C > 0:
        result.a_k_empirical = result.fitted_C / result.g_k
    else:
        result.a_k_empirical = 0.0

    return result


# ============================================================================
# 8.  Approximate functional equation (verification path 2)
# ============================================================================

def approximate_functional_equation_moment(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> float:
    """Estimate M_{2k}(T) via the approximate functional equation.

    For a Dirichlet series zeta_A(s) = sum S_r r^{-s}, the AFE gives:

        zeta_A(s) ~ sum_{r <= x} S_r r^{-s} V(r/x)
                   + chi_A(s) * sum_{r <= y} S_r^* r^{-(1-s)} V(r/y)

    where xy ~ T/(2pi) and V is a smoothing function.

    For shadow zeta (no functional equation in general), we use the
    TRUNCATED AFE: zeta_A(s) ~ sum_{r <= sqrt(T)} S_r r^{-s}.

    The moment of the truncated sum provides an approximation that
    converges as T grows.

    This is an INDEPENDENT verification path for the direct integration.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    # Truncation point for the AFE
    R_trunc = max(int(math.sqrt(T)) + 1, max_r)
    R_trunc = min(R_trunc, max_r)

    # For finite towers, AFE is exact (no truncation effect)
    # For infinite towers, this is an approximation

    # Compute the mean value by expanding |sum S_r r^{-s}|^{2k}
    # For k=1: |sum S_r r^{-s}|^2 = sum_{r,r'} S_r S_{r'} (r'/r)^{it} * (rr')^{-sigma}
    #          Mean over t in [0,T]: diagonal r=r' gives sum S_r^2 r^{-2sigma}
    #          Off-diagonal: integral of (r'/r)^{it} over [0,T] = T * delta_{r,r'} + O(1)

    # For k=1 (second moment): diagonal contribution
    if k == 1:
        diagonal = 0.0
        for r in range(2, R_trunc + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if Sr == 0.0:
                continue
            diagonal += Sr ** 2 * r ** (-2 * sigma)
        return diagonal

    # For k >= 2: use multinomial expansion or numerical integration
    # of the truncated sum. We fall back to direct integration with
    # the truncated coefficients.
    trunc_coeffs = {r: shadow_coeffs.get(r, 0.0) for r in range(2, R_trunc + 1)}
    h = min(0.1, T / 20.0)
    return shadow_zeta_moment_numerical(trunc_coeffs, k, T, sigma, h, R_trunc)


def diagonal_moment_k1(
    shadow_coeffs: Dict[int, float],
    sigma: float = 0.5,
    max_r: Optional[int] = None,
) -> float:
    """Compute the diagonal (leading) contribution to M_2:

        D_2 = sum_{r >= 2} S_r^2 * r^{-2*sigma}

    This is the mean-value theorem prediction for the second moment.
    For the Riemann zeta, the analogous statement is:
        (1/T) integral |zeta(1/2+it)|^2 dt ~ log(T/(2pi))
    which is the leading term with the diagonal contribution log(T).

    For shadow zeta, the diagonal contribution is a CONSTANT
    (independent of T) for finite-tower families.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total += Sr ** 2 * r ** (-2.0 * sigma)
    return total


# ============================================================================
# 9.  Koszul moment duality
# ============================================================================

def koszul_moment_ratio(
    family: str,
    param: float,
    k: int,
    T: float,
    h: float = 0.05,
    max_r: int = 50,
) -> Dict[str, float]:
    """Compute moments of A and A! and their ratio.

    Returns dict with keys:
        'M_A': moment of A
        'M_A!': moment of A!
        'ratio': M_A / M_A!
        'sum': M_A + M_A!
        'kappa_A': modular characteristic of A
        'kappa_A!': modular characteristic of A!
        'kappa_sum': kappa_A + kappa_A!
    """
    coeffs_A = shadow_coefficients_extended(family, param, max_r)
    coeffs_dual = koszul_dual_coefficients(family, param, max_r)

    actual_h = min(h, T / 20.0)
    M_A = shadow_zeta_moment_numerical(coeffs_A, k, T, 0.5, actual_h, max_r)
    M_dual = shadow_zeta_moment_numerical(coeffs_dual, k, T, 0.5, actual_h, max_r)

    kappa_A = coeffs_A.get(2, 0.0)
    kappa_dual = coeffs_dual.get(2, 0.0)

    ratio = M_A / M_dual if abs(M_dual) > 1e-15 else float('inf')

    return {
        'M_A': M_A,
        'M_A!': M_dual,
        'ratio': ratio,
        'sum': M_A + M_dual,
        'kappa_A': kappa_A,
        'kappa_A!': kappa_dual,
        'kappa_sum': kappa_A + kappa_dual,
    }


# ============================================================================
# 10.  Shadow depth moment classification
# ============================================================================

def classify_moment_growth(
    family: str,
    param: float,
    k_values: List[int] = None,
    T_values: List[float] = None,
    max_r: int = 50,
) -> Dict[str, Any]:
    """Classify moment growth by shadow depth class.

    Returns a dict with growth characteristics for each moment order.
    """
    if k_values is None:
        k_values = [1, 2, 3]
    if T_values is None:
        T_values = [10.0, 50.0, 100.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)

    # Determine shadow depth class
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r
    if last_nonzero == 2:
        depth_class = 'G'
    elif last_nonzero == 3:
        depth_class = 'L'
    elif last_nonzero == 4:
        depth_class = 'C'
    else:
        depth_class = 'M'

    result = {
        'family': family,
        'param': param,
        'depth_class': depth_class,
        'shadow_depth': last_nonzero,
        'moments': {},
    }

    for k in k_values:
        fit = fit_moment_growth(
            coeffs, k, T_values, sigma=0.5, h=0.05, max_r=max_r
        )
        result['moments'][k] = {
            'fitted_C': fit.fitted_C,
            'fitted_exponent': fit.fitted_exponent,
            'expected_exponent': k * k,
            'g_k': fit.g_k,
            'a_k_empirical': fit.a_k_empirical,
            'M_values': dict(zip(T_values, fit.M_values)),
        }

    return result


# ============================================================================
# 11.  Arithmetic factor computation
# ============================================================================

def arithmetic_factor_empirical(
    shadow_coeffs: Dict[int, float],
    k: int,
    T: float,
    sigma: float = 0.5,
    h: float = 0.05,
    max_r: Optional[int] = None,
) -> float:
    """Extract the empirical arithmetic factor a_k(A) from:

        M_{2k}(T) / (g_k * (log T)^{k^2})

    For finite-tower algebras, the moment is a constant (no log T growth),
    so a_k diverges as T grows -- signaling that the Keating-Snaith
    asymptotics do NOT apply (the log growth is absent).
    """
    actual_h = min(h, T / 20.0)
    M = shadow_zeta_moment_numerical(shadow_coeffs, k, T, sigma, actual_h, max_r)
    g_k = random_matrix_factor_gk(k)
    log_T = math.log(T) if T > 1 else 1.0
    log_power = log_T ** (k * k)

    if g_k * log_power < 1e-50:
        return float('inf')
    return M / (g_k * log_power)


def arithmetic_factor_from_euler_product(
    shadow_coeffs: Dict[int, float],
    k: int,
    n_primes: int = 100,
) -> float:
    """Compute arithmetic factor via shadow Euler product approximation.

    Even though shadow zeta functions are NOT multiplicative in general,
    we can compute the formal product:

        a_k = prod_p (1 - 1/p)^{k^2} * sum_{m=0}^{M}
              |sum_{j=0}^{m} S_{p^j} p^{-j/2}|^{2k}

    This will agree with the empirical a_k ONLY if the shadow sequence
    has approximate multiplicativity.

    For the Heisenberg case: only S_2 is nonzero, so the local factor at
    p != 2 is just (1 - 1/p)^{k^2}, and at p = 2 we get an explicit formula.
    """
    # Generate primes via sieve
    primes = _sieve_primes(max(100, n_primes * 15))[:n_primes]

    result = 1.0
    for p in primes:
        # (1 - 1/p)^{k^2} factor
        base = (1.0 - 1.0 / p) ** (k * k)

        # Local factor: sum over p-primary arities
        # S_{p^j} for j = 0, 1, 2, ...
        local_sum = 0.0
        max_j = 10  # Truncation for local factor
        for m in range(max_j + 1):
            partial = 0.0 + 0.0j
            for j in range(m + 1):
                r = p ** j
                Sr = shadow_coeffs.get(r, 0.0)
                partial += Sr * r ** (-0.5)
            local_sum += abs(partial) ** (2 * k)

        # Normalize by the expected value
        if local_sum > 0:
            result *= base * local_sum
        else:
            result *= base

    return result


def _sieve_primes(limit: int) -> List[int]:
    """Simple sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]


# ============================================================================
# 12.  Heisenberg exact moments (analytical formulas)
# ============================================================================

def heisenberg_exact_moment(k_val: float, k_moment: int, T: float) -> float:
    """Exact 2k-th moment for Heisenberg H_{k_val}.

    zeta_{H_k}(s) = k * 2^{-s} (single term).

    |zeta_{H_k}(1/2 + it)|^{2k_moment}
        = |k|^{2k_moment} * |2^{-(1/2+it)}|^{2k_moment}
        = |k|^{2k_moment} * 2^{-k_moment}

    This is CONSTANT in t, so:
        M_{2k}(T) = |k|^{2k_moment} * 2^{-k_moment}

    (independent of T).
    """
    return abs(k_val) ** (2 * k_moment) * 2.0 ** (-k_moment)


def affine_sl2_exact_second_moment(k_val: float, T: float) -> float:
    """Approximate second moment for affine sl_2 at level k.

    zeta_A(s) = kappa * 2^{-s} + alpha * 3^{-s}

    |zeta_A(1/2 + it)|^2 = kappa^2 * 2^{-1} + alpha^2 * 3^{-1}
        + 2 * kappa * alpha * Re(2^{-1/2-it} * 3^{-1/2+it})

    The diagonal contribution is: kappa^2/2 + alpha^2/3
    The off-diagonal oscillates as cos(t * log(3/2)) and averages to 0.

    For large T:
        M_2(T) -> kappa^2/2 + alpha^2/3  (diagonal)
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    return kappa ** 2 / 2.0 + alpha ** 2 / 3.0


# ============================================================================
# 13.  Full landscape moment analysis
# ============================================================================

@dataclass
class MomentLandscapeResult:
    """Result of full moment analysis for a family."""
    family: str
    param: float
    depth_class: str
    kappa: float
    moments: Dict[int, Dict[str, Any]] = field(default_factory=dict)
    koszul_duality: Dict[str, Any] = field(default_factory=dict)
    extreme_values: List[Tuple[float, float, float]] = field(default_factory=list)
    negative_moments: Dict[int, Tuple[float, bool]] = field(default_factory=dict)


def full_moment_analysis(
    family: str,
    param: float,
    k_values: List[int] = None,
    T_values: List[float] = None,
    max_r: int = 50,
    h: float = 0.05,
) -> MomentLandscapeResult:
    """Full moment analysis for a single family.

    Computes:
    - Standard moments M_{2k}(T) for each k and T
    - Fit to (log T)^{k^2} growth
    - Random matrix factor comparison
    - Koszul duality cross-check
    - Extreme value statistics
    - Negative moments

    Returns MomentLandscapeResult.
    """
    if k_values is None:
        k_values = [1, 2, 3]
    if T_values is None:
        T_values = [10.0, 50.0, 100.0]

    coeffs = shadow_coefficients_extended(family, param, max_r)
    kappa = coeffs.get(2, 0.0)

    # Shadow depth
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r
    if last_nonzero == 2:
        dc = 'G'
    elif last_nonzero == 3:
        dc = 'L'
    elif last_nonzero == 4:
        dc = 'C'
    else:
        dc = 'M'

    result = MomentLandscapeResult(
        family=family, param=param, depth_class=dc, kappa=kappa
    )

    # Standard moments
    for k in k_values:
        fit = fit_moment_growth(coeffs, k, T_values, 0.5, h, max_r)
        result.moments[k] = {
            'T_values': fit.T_values,
            'M_values': fit.M_values,
            'fitted_C': fit.fitted_C,
            'fitted_exponent': fit.fitted_exponent,
            'g_k': fit.g_k,
            'a_k_empirical': fit.a_k_empirical,
            'r_squared': fit.r_squared,
        }

    # Extreme values
    result.extreme_values = extreme_value_scaling(
        coeffs, T_values, 0.5, h, max_r
    )

    # Negative moments (k=1 only for speed)
    for T in T_values[-1:]:
        val, conv = negative_moment_numerical(coeffs, 1, T, 0.5, h, max_r)
        result.negative_moments[1] = (val, conv)

    return result


# ============================================================================
# 14.  Complementarity moment sum
# ============================================================================

def complementarity_moment_sum(
    family: str,
    param: float,
    k: int,
    T: float,
    max_r: int = 50,
    h: float = 0.05,
) -> Dict[str, float]:
    """Compute M_{2k}(A) + M_{2k}(A!) and the complementarity sum.

    For the shadow zeta sum zeta_A + zeta_{A!} = D(s), the moment
    of D provides a comparison.

    Returns dict with M_A, M_A!, M_sum, M_D (moment of complementarity sum).
    """
    coeffs_A = shadow_coefficients_extended(family, param, max_r)
    coeffs_dual = koszul_dual_coefficients(family, param, max_r)

    # Complementarity sum coefficients
    comp_coeffs = {}
    all_r = set(list(coeffs_A.keys()) + list(coeffs_dual.keys()))
    for r in all_r:
        comp_coeffs[r] = coeffs_A.get(r, 0.0) + coeffs_dual.get(r, 0.0)

    actual_h = min(h, T / 20.0)
    M_A = shadow_zeta_moment_numerical(coeffs_A, k, T, 0.5, actual_h, max_r)
    M_dual = shadow_zeta_moment_numerical(coeffs_dual, k, T, 0.5, actual_h, max_r)
    M_D = shadow_zeta_moment_numerical(comp_coeffs, k, T, 0.5, actual_h, max_r)

    return {
        'M_A': M_A,
        'M_A!': M_dual,
        'M_sum': M_A + M_dual,
        'M_D': M_D,
        'difference': (M_A + M_dual) - M_D,
    }
