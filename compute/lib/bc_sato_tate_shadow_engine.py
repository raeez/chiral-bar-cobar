r"""Sato-Tate distribution analysis for shadow Hecke eigenvalues.

MATHEMATICAL FRAMEWORK
======================

The shadow Hecke eigenvalues {a_p(A)} at primes p are defined from the
shadow coefficient sequence {S_r(A)} via the Hecke operator

    (T_p S)(r) = S(p*r) + p^{w-1} S(r/p)

with weight w = 2.  If S is an eigenform, T_p(S) = lambda_p * S.

At each prime p, define the normalized shadow Hecke angle:

    theta_p(A) = arccos(lambda_p / (2 * p^{(w-1)/2}))

where the Ramanujan bound |lambda_p| <= 2 p^{(w-1)/2} ensures the
argument lies in [-1, 1] when tempered.

The Sato-Tate conjecture (proved for elliptic curves by Taylor et al.,
2006-2011) predicts that for a generic non-CM family:

    #{p <= x : theta_p in [alpha, beta]} / pi(x) -> (2/pi) int_alpha^beta sin^2(theta) d theta

For shadow zeta, the distribution depends on the depth class:
  - Class G (Heisenberg): S_r = 0 for r >= 3, degenerate.
  - Class L (affine KM): terminates at arity 3, too few primes.
  - Class C (beta-gamma): terminates at arity 4, too few primes.
  - Class M (Virasoro, W_N): infinite tower, genuine test.

VERIFICATION PATHS (>= 3 per claim):
  1. Direct histogram vs Sato-Tate density
  2. Moment comparison (analytic vs empirical)
  3. Kolmogorov-Smirnov test
  4. Complementarity: theta_p(Vir_c) vs theta_p(Vir_{26-c})
  5. Self-dual c=13: enhanced symmetry

CONVENTIONS:
  - Cohomological grading (|d| = +1), bar uses desuspension.
  - Shadow coefficients S_r from shadow_euler_product_engine.py.
  - Default weight w = 2.
  - kappa = S_2.
  - Virasoro: kappa = c/2 (AP48: this is specific to Virasoro).
  - For W_3: two primary lines (T-line and W-line) with independent towers.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP10): Cross-family consistency checks are the real verification.
CAUTION (AP15): E_2* is quasi-modular; shadow forms are NOT classical.
CAUTION (AP38): Normalization conventions must be tracked.

Manuscript references:
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:operadic-rankin-selberg (arithmetic_shadows.tex)
    prop:shadow-symmetric-power (arithmetic_shadows.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

# ---------------------------------------------------------------------------
# Imports from existing infrastructure
# ---------------------------------------------------------------------------
try:
    from shadow_euler_product_engine import (
        virasoro_shadow_coefficients,
        heisenberg_shadow_coefficients,
        affine_sl2_shadow_coefficients,
        lattice_shadow_coefficients,
        betagamma_shadow_coefficients,
        shadow_hecke_operator,
        hecke_eigenvalue_test,
        shadow_dirichlet_series_float,
    )
except ImportError:
    from .shadow_euler_product_engine import (
        virasoro_shadow_coefficients,
        heisenberg_shadow_coefficients,
        affine_sl2_shadow_coefficients,
        lattice_shadow_coefficients,
        betagamma_shadow_coefficients,
        shadow_hecke_operator,
        hecke_eigenvalue_test,
        shadow_dirichlet_series_float,
    )

try:
    from w3_shadow_tower_engine import (
        t_line_tower_numerical,
        w_line_tower_numerical,
    )
except ImportError:
    try:
        from .w3_shadow_tower_engine import (
            t_line_tower_numerical,
            w_line_tower_numerical,
        )
    except ImportError:
        t_line_tower_numerical = None
        w_line_tower_numerical = None

from sympy import Rational


# ============================================================================
# 0.  Utility: prime sieve
# ============================================================================

def _primes_up_to(n: int) -> List[int]:
    """Sieve of Eratosthenes up to n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


PRIMES_541 = _primes_up_to(541)  # first 100 primes: 2, 3, 5, ..., 541
PRIMES_100_PRIMES = PRIMES_541[:100]  # exactly the first 100 primes


# ============================================================================
# 1.  Shadow coefficient extraction with float cache
# ============================================================================

def virasoro_shadow_coefficients_float(c_val: float,
                                        max_r: int = 600) -> Dict[int, float]:
    """Virasoro shadow coefficients using the convolution recursion (float).

    Uses the recursion:
        a_0 = c, a_1 = 6, a_2 = 40/(c(5c+22))
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3
        S_r = a_{r-2} / r
    """
    if abs(c_val) < 1e-15:
        raise ValueError("Virasoro shadow coefficients undefined at c=0.")

    a = [0.0] * (max_r - 1)
    a[0] = c_val
    if max_r > 2:
        a[1] = 6.0
    if max_r > 3:
        a[2] = 40.0 / (c_val * (5.0 * c_val + 22.0))

    inv_2c = -1.0 / (2.0 * c_val)
    for n in range(3, max_r - 1):
        conv = 0.0
        for j in range(1, n):
            conv += a[j] * a[n - j]
        a[n] = inv_2c * conv

    result = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / r
    return result


def _get_shadow_coeffs(family: str, param, max_r: int = 600) -> Dict[int, float]:
    """Get shadow coefficients as floats for the given family.

    For speed we use float recursion for Virasoro.
    Other families terminate early so exact Rational is fine.
    """
    if family == 'virasoro':
        return virasoro_shadow_coefficients_float(float(param), max_r)
    elif family == 'heisenberg':
        exact = heisenberg_shadow_coefficients(Rational(param), min(max_r, 60))
        return {r: float(v) for r, v in exact.items()}
    elif family == 'affine_sl2':
        exact = affine_sl2_shadow_coefficients(Rational(param), min(max_r, 60))
        return {r: float(v) for r, v in exact.items()}
    elif family == 'lattice':
        exact = lattice_shadow_coefficients(int(param), min(max_r, 60))
        return {r: float(v) for r, v in exact.items()}
    elif family == 'betagamma':
        exact = betagamma_shadow_coefficients(Rational(param), min(max_r, 60))
        return {r: float(v) for r, v in exact.items()}
    else:
        raise ValueError(f"Unknown family: {family}")


# ============================================================================
# 2.  Shadow Hecke eigenvalues at primes
# ============================================================================

def shadow_hecke_eigenvalue_at_prime(S: Dict[int, float],
                                      p: int,
                                      weight: float = 2.0) -> float:
    """Compute approximate Hecke eigenvalue lambda_p from S via projection.

    For shadow sequences that are NOT exact eigenforms, we use the
    projection: lambda_p ~ T_p(S)(r_ref) / S(r_ref) at a reference
    arity r_ref where S(r_ref) != 0.

    For exact eigenforms, this is independent of r_ref.  For non-eigenforms,
    we use r_ref = 2 (the kappa component).
    """
    # T_p(S)(2) = S(2p) + p^{w-1} * S(2/p)
    # For p >= 3: S(2/p) = 0 since 2/p is not integer >= 2.
    # For p = 2: S(2/2) = S(1) = 0 by convention.
    # So T_p(S)(2) = S(2p) for all primes p.
    pw = p ** (weight - 1.0)

    S2 = S.get(2, 0.0)
    if abs(S2) < 1e-50:
        return 0.0

    # Use kappa projection: lambda_p ~ S(2p) / S(2)
    # This is exact when S is an eigenform.
    S_2p = S.get(2 * p, 0.0)
    # For r=2: T_p(S)(2) = S(2p) + p^{w-1}*S(2/p) = S(2p) (since 2/p < 2 for p>=2)
    lambda_p = S_2p / S2

    return lambda_p


def shadow_hecke_eigenvalues_float(S: Dict[int, float],
                                     primes: Optional[List[int]] = None,
                                     weight: float = 2.0) -> Dict[int, float]:
    """Compute approximate Hecke eigenvalues for all primes."""
    if primes is None:
        primes = PRIMES_100_PRIMES
    return {p: shadow_hecke_eigenvalue_at_prime(S, p, weight)
            for p in primes}


# ============================================================================
# 3.  Normalized Hecke angles (Sato-Tate normalization)
# ============================================================================

def _find_normalization_exponent(S: Dict[int, float],
                                  primes: List[int],
                                  weight: float = 2.0) -> float:
    """Find sigma_0 such that |lambda_p| / (2 * p^{sigma_0/2}) <= 1 for all p.

    The Ramanujan bound for weight-w modular forms gives sigma_0 = w - 1.
    But for shadow sequences, this may not hold.  We find the minimal
    sigma_0 that normalizes to [-1, 1].

    Returns sigma_0.
    """
    eigenvalues = shadow_hecke_eigenvalues_float(S, primes, weight)

    sigma_0 = weight - 1.0  # classical value

    for p, lam in eigenvalues.items():
        if abs(lam) < 1e-50:
            continue
        # Need |lam| <= 2 * p^{sigma_0/2}
        # => sigma_0 >= 2 * log(|lam|/2) / log(p)
        ratio = abs(lam) / 2.0
        if ratio > 1e-300 and ratio > 1.0:
            needed = 2.0 * math.log(ratio) / math.log(p)
            if needed > sigma_0:
                sigma_0 = needed

    return sigma_0


def normalized_hecke_angle(lambda_p: float,
                            p: int,
                            sigma_0: float) -> Optional[float]:
    """Compute theta_p = arccos(lambda_p / (2 * p^{sigma_0/2})).

    Returns theta_p in [0, pi], or None if the argument is out of [-1, 1].
    """
    bound = 2.0 * p ** (sigma_0 / 2.0)
    if abs(bound) < 1e-300:
        return None
    arg = lambda_p / bound
    # Clamp to [-1, 1] for numerical safety
    arg = max(-1.0, min(1.0, arg))
    return math.acos(arg)


def compute_hecke_angles(S: Dict[int, float],
                          primes: Optional[List[int]] = None,
                          weight: float = 2.0,
                          sigma_0: Optional[float] = None
                          ) -> Dict[str, Any]:
    """Compute normalized Hecke angles for all primes.

    Returns a dict with:
      'angles': {p: theta_p}
      'eigenvalues': {p: lambda_p}
      'sigma_0': the normalization exponent used
      'ramanujan_violations': list of primes violating the classical bound
    """
    if primes is None:
        primes = PRIMES_100_PRIMES
    eigenvalues = shadow_hecke_eigenvalues_float(S, primes, weight)

    if sigma_0 is None:
        sigma_0 = _find_normalization_exponent(S, primes, weight)

    angles = {}
    ramanujan_violations = []
    classical_sigma = weight - 1.0

    for p in primes:
        lam = eigenvalues.get(p, 0.0)
        classical_bound = 2.0 * p ** (classical_sigma / 2.0)
        if abs(lam) > classical_bound * (1.0 + 1e-10):
            ramanujan_violations.append(p)

        theta = normalized_hecke_angle(lam, p, sigma_0)
        if theta is not None:
            angles[p] = theta

    return {
        'angles': angles,
        'eigenvalues': eigenvalues,
        'sigma_0': sigma_0,
        'ramanujan_violations': ramanujan_violations,
    }


# ============================================================================
# 4.  Sato-Tate distribution functions
# ============================================================================

def sato_tate_density(theta: float) -> float:
    """Sato-Tate density mu_ST(theta) = (2/pi) sin^2(theta).

    Defined on [0, pi].
    """
    return (2.0 / math.pi) * math.sin(theta) ** 2


def sato_tate_cdf(theta: float) -> float:
    """Sato-Tate CDF: F_ST(theta) = (2/pi) int_0^theta sin^2(t) dt.

    = (2/pi) * (theta/2 - sin(2*theta)/4)
    = (1/pi) * (theta - sin(2*theta)/2)
    """
    return (1.0 / math.pi) * (theta - math.sin(2.0 * theta) / 2.0)


def uniform_cdf(theta: float) -> float:
    """Uniform CDF on [0, pi]: F(theta) = theta / pi."""
    return theta / math.pi


def sato_tate_moment(k: int) -> float:
    """Compute the k-th moment of cos(theta) under Sato-Tate distribution.

    M_k = int_0^pi cos^k(theta) * (2/pi) sin^2(theta) d theta.

    Analytic results (computed by integration):
      k=0: 1
      k=1: 0
      k=2: 1/4
      k=3: 0
      k=4: 1/8
    General: M_k = 0 for odd k; M_{2n} = C(2n,n) / 4^n * 1/(n+1)
             = (2n)! / (n! * (n+1)! * 2^{2n})  [Catalan-related]
    Actually, the moment is the integral of x^k against the Wigner
    semicircle on [-1,1] (change of variable x = cos(theta)):
      M_k = (2/pi) int_{-1}^{1} x^k sqrt(1-x^2) dx
    which is 0 for odd k, and for even k=2n:
      M_{2n} = (2/pi) * pi * C(2n,n) / (2^{2n+1} * (n+1))
             = C(2n,n) / (2^{2n} * (n+1))
    This is exactly 1/(n+1) * C(2n,n) / 4^n = Catalan number C_n / 4^n... no.
    Let me compute directly.

    M_0 = 1
    M_2 = (2/pi) int_0^pi cos^2 sin^2 dtheta = (2/pi)(pi/8) = 1/4
    M_4 = (2/pi) int_0^pi cos^4 sin^2 dtheta = (2/pi)(pi/16) = 1/8
    General M_{2n} = (2/pi) * pi * (2n-1)!! * 1 / ((2n+2)!! ) ... use recursion.

    In fact: int_0^pi cos^{2n}(t) sin^2(t) dt = pi * C(2n,n) / 2^{2n+1} * 1/(n+1)... no.

    By direct integration using the beta function:
      I(2n) = int_0^pi cos^{2n}(t) sin^2(t) dt
      Let u = cos(t), then:
      = int_{-1}^{1} u^{2n} (1-u^2)^{1/2} du  [Wigner semicircle]
      = B(n+1/2, 3/2) = Gamma(n+1/2)*Gamma(3/2)/Gamma(n+2)
      = (sqrt(pi)*(2n)!/(4^n*n!)) * (sqrt(pi)/2) / ((n+1)!)
      = pi*(2n)!/(2*4^n*n!*(n+1)!)

    So M_{2n} = (2/pi) * pi*(2n)!/(2*4^n*n!*(n+1)!) = (2n)!/(4^n*n!*(n+1)!)
    """
    if k < 0:
        return 0.0
    if k % 2 == 1:
        return 0.0
    n = k // 2
    # M_{2n} = (2n)! / (4^n * n! * (n+1)!)
    from math import factorial
    return factorial(2 * n) / (4.0 ** n * factorial(n) * factorial(n + 1))


# ============================================================================
# 5.  Empirical distribution and statistical tests
# ============================================================================

def empirical_cdf(angles: List[float]) -> List[Tuple[float, float]]:
    """Compute the empirical CDF from a list of angles.

    Returns list of (theta, F(theta)) pairs sorted by theta.
    """
    sorted_angles = sorted(angles)
    n = len(sorted_angles)
    return [(sorted_angles[i], (i + 1) / n) for i in range(n)]


def kolmogorov_smirnov_statistic(angles: List[float],
                                   cdf_func) -> float:
    """Compute the KS statistic D = sup |F_n(x) - F(x)|.

    Parameters
    ----------
    angles : list of angles in [0, pi]
    cdf_func : theoretical CDF function F: [0, pi] -> [0, 1]

    Returns D_n (the KS statistic).
    """
    sorted_angles = sorted(angles)
    n = len(sorted_angles)
    if n == 0:
        return 0.0

    D = 0.0
    for i, theta in enumerate(sorted_angles):
        F_theory = cdf_func(theta)
        # D+ = max of (i+1)/n - F(theta)
        D = max(D, abs((i + 1) / n - F_theory))
        # D- = max of F(theta) - i/n
        D = max(D, abs(F_theory - i / n))
    return D


def ks_critical_value(n: int, alpha: float = 0.05) -> float:
    """Approximate KS critical value at significance level alpha.

    For large n, the critical value is approximately:
      c(alpha) / sqrt(n)
    where c(0.05) ~ 1.358, c(0.01) ~ 1.628.
    """
    if alpha <= 0.01:
        c_alpha = 1.628
    elif alpha <= 0.05:
        c_alpha = 1.358
    elif alpha <= 0.10:
        c_alpha = 1.224
    else:
        c_alpha = 1.073
    return c_alpha / math.sqrt(n)


def empirical_moments(angles: List[float], max_k: int = 4) -> Dict[int, float]:
    """Compute empirical moments M_k = (1/N) sum cos^k(theta_p).

    Parameters
    ----------
    angles : list of theta_p
    max_k : highest moment to compute

    Returns {k: M_k} for k = 0, 1, ..., max_k.
    """
    n = len(angles)
    if n == 0:
        return {k: 0.0 for k in range(max_k + 1)}
    cos_vals = [math.cos(theta) for theta in angles]
    moments = {}
    for k_val in range(max_k + 1):
        moments[k_val] = sum(c_v ** k_val for c_v in cos_vals) / n
    return moments


def moment_comparison(angles: List[float],
                       max_k: int = 4) -> Dict[int, Dict[str, float]]:
    """Compare empirical moments with Sato-Tate predictions.

    Returns {k: {'empirical': M_k^emp, 'sato_tate': M_k^ST, 'delta': diff}}.
    """
    emp = empirical_moments(angles, max_k)
    result = {}
    for k_val in range(max_k + 1):
        st = sato_tate_moment(k_val)
        result[k_val] = {
            'empirical': emp[k_val],
            'sato_tate': st,
            'delta': abs(emp[k_val] - st),
        }
    return result


# ============================================================================
# 6.  Anomalous primes
# ============================================================================

def anomalous_primes(S: Dict[int, float],
                      primes: Optional[List[int]] = None,
                      threshold: float = 1e-10,
                      weight: float = 2.0) -> Dict[str, Any]:
    """Find primes where the Hecke eigenvalue is anomalously small.

    Returns:
      'zero_primes': primes where |lambda_p| < threshold
      'small_primes': primes where |lambda_p| < 0.1 * mean(|lambda_p|)
      'eigenvalues': all eigenvalues
    """
    if primes is None:
        primes = PRIMES_100_PRIMES
    eigenvalues = shadow_hecke_eigenvalues_float(S, primes, weight)

    zero_primes = []
    abs_vals = []
    for p in primes:
        lam = eigenvalues.get(p, 0.0)
        abs_lam = abs(lam)
        abs_vals.append(abs_lam)
        if abs_lam < threshold:
            zero_primes.append(p)

    mean_abs = sum(abs_vals) / len(abs_vals) if abs_vals else 0.0
    small_primes = [p for p in primes
                    if abs(eigenvalues.get(p, 0.0)) < 0.1 * mean_abs
                    and abs(eigenvalues.get(p, 0.0)) >= threshold]

    return {
        'zero_primes': zero_primes,
        'small_primes': small_primes,
        'mean_abs_eigenvalue': mean_abs,
        'eigenvalues': eigenvalues,
    }


# ============================================================================
# 7.  Complementarity analysis
# ============================================================================

def complementarity_angles(c_val: float,
                             primes: Optional[List[int]] = None,
                             max_r: int = 600,
                             weight: float = 2.0
                             ) -> Dict[str, Any]:
    """Compare Hecke angles for Vir_c and Vir_{26-c} (Koszul dual).

    For Virasoro: A = Vir_c, A! = Vir_{26-c}.
    kappa(Vir_c) = c/2, kappa(Vir_{26-c}) = (26-c)/2.
    The complementarity sum: kappa + kappa' = 13 (NOT 0; AP24).

    Returns comparison data.
    """
    if primes is None:
        primes = PRIMES_100_PRIMES
    c_dual = 26.0 - c_val

    S_A = virasoro_shadow_coefficients_float(c_val, max_r)
    S_A_dual = virasoro_shadow_coefficients_float(c_dual, max_r)

    data_A = compute_hecke_angles(S_A, primes, weight)
    data_Ad = compute_hecke_angles(S_A_dual, primes, weight)

    angles_A = data_A['angles']
    angles_Ad = data_Ad['angles']

    # Compute correlation and comparison
    common_primes = sorted(set(angles_A.keys()) & set(angles_Ad.keys()))
    theta_A = [angles_A[p] for p in common_primes]
    theta_Ad = [angles_Ad[p] for p in common_primes]

    if len(theta_A) > 1:
        mean_A = sum(theta_A) / len(theta_A)
        mean_Ad = sum(theta_Ad) / len(theta_Ad)
        cov = sum((a - mean_A) * (b - mean_Ad) for a, b in zip(theta_A, theta_Ad))
        var_A = sum((a - mean_A) ** 2 for a in theta_A)
        var_Ad = sum((b - mean_Ad) ** 2 for b in theta_Ad)
        if var_A > 0 and var_Ad > 0:
            correlation = cov / math.sqrt(var_A * var_Ad)
        else:
            correlation = 0.0
    else:
        correlation = 0.0

    return {
        'c': c_val,
        'c_dual': c_dual,
        'angles_A': angles_A,
        'angles_A_dual': angles_Ad,
        'data_A': data_A,
        'data_A_dual': data_Ad,
        'common_primes': common_primes,
        'correlation': correlation,
        'kappa_sum': c_val / 2.0 + c_dual / 2.0,  # should be 13
    }


# ============================================================================
# 8.  Self-dual point analysis (c = 13)
# ============================================================================

def self_dual_analysis(primes: Optional[List[int]] = None,
                        max_r: int = 600,
                        weight: float = 2.0) -> Dict[str, Any]:
    """Analyze the self-dual point c = 13 for Virasoro.

    At c = 13: Vir_c = Vir_{26-c}, so the shadow tower is self-dual.
    Expect enhanced symmetry in the Hecke angle distribution.

    Returns detailed analysis.
    """
    if primes is None:
        primes = PRIMES_100_PRIMES

    S = virasoro_shadow_coefficients_float(13.0, max_r)
    data = compute_hecke_angles(S, primes, weight)

    angles_list = sorted(data['angles'].values())
    n = len(angles_list)

    # Test for enhanced symmetry around theta = pi/2
    # Under perfect symmetry, the distribution of (theta - pi/2) should be symmetric
    centered = [theta - math.pi / 2.0 for theta in angles_list]
    skewness = 0.0
    if n > 2:
        m2 = sum(x ** 2 for x in centered) / n
        m3 = sum(x ** 3 for x in centered) / n
        if m2 > 0:
            skewness = m3 / m2 ** 1.5

    # KS tests
    ks_st = kolmogorov_smirnov_statistic(angles_list, sato_tate_cdf)
    ks_uniform = kolmogorov_smirnov_statistic(angles_list, uniform_cdf)

    # Moment comparison
    moments = moment_comparison(angles_list, 4)

    return {
        'c': 13,
        'angles': data['angles'],
        'eigenvalues': data['eigenvalues'],
        'sigma_0': data['sigma_0'],
        'ramanujan_violations': data['ramanujan_violations'],
        'ks_sato_tate': ks_st,
        'ks_uniform': ks_uniform,
        'ks_critical_005': ks_critical_value(n),
        'moments': moments,
        'skewness_about_pi2': skewness,
        'n_angles': n,
    }


# ============================================================================
# 9.  Full Sato-Tate analysis for a family
# ============================================================================

def full_sato_tate_analysis(family: str,
                              param,
                              primes: Optional[List[int]] = None,
                              max_r: int = 600,
                              weight: float = 2.0) -> Dict[str, Any]:
    """Complete Sato-Tate analysis for a given algebra.

    Computes: eigenvalues, angles, KS tests, moments, anomalous primes.
    """
    if primes is None:
        primes = PRIMES_100_PRIMES

    S = _get_shadow_coeffs(family, param, max_r)
    data = compute_hecke_angles(S, primes, weight)

    angles_list = sorted(data['angles'].values())
    n = len(angles_list)

    ks_st = kolmogorov_smirnov_statistic(angles_list, sato_tate_cdf)
    ks_uniform = kolmogorov_smirnov_statistic(angles_list, uniform_cdf)
    ks_crit = ks_critical_value(n) if n > 0 else float('inf')

    moments = moment_comparison(angles_list, 4)
    anom = anomalous_primes(S, primes, weight=weight)

    return {
        'family': family,
        'param': param,
        'n_angles': n,
        'angles': data['angles'],
        'eigenvalues': data['eigenvalues'],
        'sigma_0': data['sigma_0'],
        'ramanujan_violations': data['ramanujan_violations'],
        'ks_sato_tate': ks_st,
        'ks_uniform': ks_uniform,
        'ks_critical_005': ks_crit,
        'moments': moments,
        'anomalous': anom,
    }


# ============================================================================
# 10. Virasoro landscape: c = 1..25
# ============================================================================

def virasoro_landscape_analysis(c_values: Optional[List[int]] = None,
                                  primes: Optional[List[int]] = None,
                                  max_r: int = 600,
                                  weight: float = 2.0) -> Dict[int, Dict[str, Any]]:
    """Run Sato-Tate analysis for Virasoro at c = 1, 2, ..., 25.

    Returns {c: analysis_dict}.
    """
    if c_values is None:
        c_values = list(range(1, 26))
    if primes is None:
        primes = PRIMES_100_PRIMES

    results = {}
    for c_val in c_values:
        results[c_val] = full_sato_tate_analysis('virasoro', c_val,
                                                   primes, max_r, weight)
    return results


# ============================================================================
# 11. Higher Sato-Tate groups: W_3 two-line analysis
# ============================================================================

def w3_two_line_joint_distribution(c_val: float,
                                     primes: Optional[List[int]] = None,
                                     max_r: int = 100,
                                     weight: float = 2.0) -> Dict[str, Any]:
    """Joint distribution of shadow Hecke eigenvalues on T-line and W-line.

    For W_3, the two primary lines give independent shadow towers.
    The joint Sato-Tate group should be:
      - SU(2) x SU(2) if the lines are independent
      - USp(4) if there are cross-correlations

    Returns joint data for the first primes.
    """
    if primes is None:
        primes = PRIMES_100_PRIMES[:50]

    if t_line_tower_numerical is None or w_line_tower_numerical is None:
        return {
            'error': 'w3_shadow_tower_engine not available',
            'c': c_val,
        }

    S_T = t_line_tower_numerical(c_val, max_r)
    S_W = w_line_tower_numerical(c_val, max_r)

    data_T = compute_hecke_angles(S_T, primes, weight)
    data_W = compute_hecke_angles(S_W, primes, weight)

    angles_T = data_T['angles']
    angles_W = data_W['angles']

    common = sorted(set(angles_T.keys()) & set(angles_W.keys()))
    joint = [(angles_T[p], angles_W[p]) for p in common]

    # Test independence: correlation of angles
    if len(joint) > 1:
        t_vals = [x[0] for x in joint]
        w_vals = [x[1] for x in joint]
        mean_t = sum(t_vals) / len(t_vals)
        mean_w = sum(w_vals) / len(w_vals)
        cov = sum((a - mean_t) * (b - mean_w) for a, b in zip(t_vals, w_vals))
        var_t = sum((a - mean_t) ** 2 for a in t_vals)
        var_w = sum((b - mean_w) ** 2 for b in w_vals)
        if var_t > 0 and var_w > 0:
            correlation = cov / math.sqrt(var_t * var_w)
        else:
            correlation = 0.0
    else:
        correlation = 0.0

    # Marginal KS tests
    t_list = sorted(data_T['angles'].values())
    w_list = sorted(data_W['angles'].values())

    ks_t_st = kolmogorov_smirnov_statistic(t_list, sato_tate_cdf)
    ks_w_st = kolmogorov_smirnov_statistic(w_list, sato_tate_cdf)

    return {
        'c': c_val,
        'data_T': data_T,
        'data_W': data_W,
        'joint_angles': joint,
        'common_primes': common,
        'correlation': correlation,
        'ks_T_sato_tate': ks_t_st,
        'ks_W_sato_tate': ks_w_st,
        'marginal_moments_T': moment_comparison(t_list, 4),
        'marginal_moments_W': moment_comparison(w_list, 4),
    }


# ============================================================================
# 12. Shadow Hecke algebra: T_p eigenvalues
# ============================================================================

def shadow_hecke_operator_float(S: Dict[int, float],
                                  p: int,
                                  weight: float = 2.0,
                                  max_r: Optional[int] = None) -> Dict[int, float]:
    """Apply T_p to shadow sequence (float version).

    (T_p S)(r) = S(p*r) + p^{w-1} S(r/p)  [S(r/p) = 0 if p does not divide r]
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)
    pw = p ** (weight - 1.0)
    result = {}
    for r in range(2, max_r + 1):
        pr = p * r
        term1 = S.get(pr, 0.0)
        term2 = 0.0
        if r % p == 0:
            rp = r // p
            if rp >= 2:
                term2 = pw * S.get(rp, 0.0)
        result[r] = term1 + term2
    return result


def hecke_eigenvalue_residuals(S: Dict[int, float],
                                  p: int,
                                  weight: float = 2.0,
                                  max_r: Optional[int] = None) -> Dict[str, Any]:
    """Compute T_p(S)(r) - lambda_p * S(r) for each r, where lambda_p is
    the approximate eigenvalue from the kappa projection.

    Returns eigenvalue, residuals, and relative residuals.
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)
    TpS = shadow_hecke_operator_float(S, p, weight, max_r)
    lambda_p = shadow_hecke_eigenvalue_at_prime(S, p, weight)

    residuals = {}
    rel_residuals = {}
    for r in range(2, max_r + 1):
        resid = TpS.get(r, 0.0) - lambda_p * S.get(r, 0.0)
        residuals[r] = resid
        sr_val = S.get(r, 0.0)
        if abs(sr_val) > 1e-50:
            rel_residuals[r] = abs(resid) / abs(sr_val)
        else:
            rel_residuals[r] = abs(resid)  # absolute when S(r) ~ 0

    max_rel = max(rel_residuals.values()) if rel_residuals else 0.0

    return {
        'p': p,
        'lambda_p': lambda_p,
        'residuals': residuals,
        'relative_residuals': rel_residuals,
        'max_relative_residual': max_rel,
        'is_eigenform': max_rel < 1e-8,
    }


def eigenform_quality(S: Dict[int, float],
                        primes: Optional[List[int]] = None,
                        weight: float = 2.0,
                        max_r: int = 100) -> Dict[str, Any]:
    """Assess how close S is to being a Hecke eigenform at all primes.

    Returns summary of residuals for each prime.
    """
    if primes is None:
        primes = PRIMES_100_PRIMES[:20]
    results = {}
    for p in primes:
        results[p] = hecke_eigenvalue_residuals(S, p, weight, max_r)

    overall_eigenform = all(r['is_eigenform'] for r in results.values())
    max_residual = max(r['max_relative_residual'] for r in results.values())

    return {
        'per_prime': results,
        'is_eigenform_overall': overall_eigenform,
        'max_residual_overall': max_residual,
    }


# ============================================================================
# 13. Depth class classification for Sato-Tate
# ============================================================================

def classify_depth_for_st(family: str, param,
                           max_r: int = 60) -> Dict[str, Any]:
    """Classify the depth class and determine if ST analysis is meaningful.

    Classes G/L/C: tower terminates, ST analysis is degenerate.
    Class M: infinite tower, genuine ST test possible.
    """
    S = _get_shadow_coeffs(family, param, max_r)

    # Count nonzero arities
    nonzero_arities = [r for r, v in S.items() if abs(v) > 1e-50]
    max_nonzero = max(nonzero_arities) if nonzero_arities else 0

    if max_nonzero <= 2:
        depth_class = 'G'
        st_meaningful = False
        reason = 'Class G: tower terminates at arity 2 (Heisenberg/lattice)'
    elif max_nonzero <= 3:
        depth_class = 'L'
        st_meaningful = False
        reason = 'Class L: tower terminates at arity 3 (affine KM)'
    elif max_nonzero <= 4:
        depth_class = 'C'
        st_meaningful = False
        reason = 'Class C: tower terminates at arity 4 (beta-gamma)'
    else:
        depth_class = 'M'
        st_meaningful = True
        reason = 'Class M: infinite tower (Virasoro/W_N)'

    return {
        'family': family,
        'param': param,
        'depth_class': depth_class,
        'st_meaningful': st_meaningful,
        'reason': reason,
        'max_nonzero_arity': max_nonzero,
        'n_nonzero_arities': len(nonzero_arities),
    }


# ============================================================================
# 14. Histogram computation (for external plotting)
# ============================================================================

def angle_histogram(angles: List[float],
                     n_bins: int = 20) -> Dict[str, Any]:
    """Compute histogram of angles in [0, pi].

    Returns bin edges, counts, and the ST reference curve.
    """
    bin_width = math.pi / n_bins
    edges = [i * bin_width for i in range(n_bins + 1)]
    counts = [0] * n_bins

    for theta in angles:
        idx = min(int(theta / bin_width), n_bins - 1)
        if idx < 0:
            idx = 0
        counts[idx] += 1

    n = len(angles)
    density = [c_val / (n * bin_width) if n > 0 else 0.0 for c_val in counts]

    # ST reference density at bin midpoints
    midpoints = [edges[i] + bin_width / 2.0 for i in range(n_bins)]
    st_ref = [sato_tate_density(m) for m in midpoints]

    return {
        'edges': edges,
        'midpoints': midpoints,
        'counts': counts,
        'density': density,
        'sato_tate_reference': st_ref,
        'n_total': n,
        'n_bins': n_bins,
    }


# ============================================================================
# 15. Summary statistics
# ============================================================================

def distribution_summary(angles: List[float]) -> Dict[str, float]:
    """Compute summary statistics of the angle distribution."""
    if not angles:
        return {'mean': 0.0, 'std': 0.0, 'median': 0.0, 'min': 0.0, 'max': 0.0}

    n = len(angles)
    mean = sum(angles) / n
    var = sum((a - mean) ** 2 for a in angles) / n
    std = math.sqrt(var)
    sorted_a = sorted(angles)
    median = sorted_a[n // 2]

    # ST expected mean and std
    # E[theta] = int_0^pi theta (2/pi)sin^2(theta) d theta = pi/2
    # Var[theta] = E[theta^2] - (E[theta])^2
    # E[theta^2] = int_0^pi theta^2 (2/pi)sin^2 dtheta = pi^2/3 - 1/2
    # Var = pi^2/3 - 1/2 - pi^2/4 = pi^2/12 - 1/2
    st_mean = math.pi / 2.0
    st_var = math.pi ** 2 / 12.0 - 0.5
    st_std = math.sqrt(st_var)

    return {
        'mean': mean,
        'std': std,
        'median': median,
        'min': sorted_a[0],
        'max': sorted_a[-1],
        'n': n,
        'st_mean': st_mean,
        'st_std': st_std,
        'mean_deviation_from_st': abs(mean - st_mean),
        'std_deviation_from_st': abs(std - st_std),
    }
