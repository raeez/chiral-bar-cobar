r"""Shadow Hecke eigenvalue engine: Hecke operators, eigenvalue extraction,
Hecke L-functions, Satake parameters, and Rankin-Selberg convolutions for
shadow tower sequences viewed as automorphic Fourier coefficients.

MATHEMATICAL FRAMEWORK
======================

The shadow coefficient sequence {S_r(A)}_{r >= 2} of a modular Koszul algebra
A can be viewed as the "Fourier coefficients" of a formal automorphic object.
This module investigates the Hecke-theoretic structure of this sequence.

1. SHADOW HECKE OPERATORS

   (T_p . S)(r) = S(p*r) + p^{w-1} S(r/p)    (S(r/p) = 0 if p does not divide r)

   where w is the "weight" parameter.  For the shadow tower the natural weight
   is w = 2 (matching the bar propagator d log E(z,w) of weight 1 in each
   variable, so the "level" of the shadow is weight 2).

2. HECKE EIGENVALUE PROBLEM

   If T_p(S) = lambda_p * S for all r, then S is a Hecke eigenform with
   eigenvalue lambda_p.  For terminating towers (class G/L/C), the Hecke
   operator maps most of the sequence to zero, so the eigenvalue problem
   degenerates.  For class M (Virasoro, W_N), the tower is infinite and the
   eigenvalue structure is nontrivial.

3. HECKE L-FUNCTION

   L^{Hecke}_A(s) = prod_p (1 - lambda_p p^{-s} + p^{w-1-2s})^{-1}

   where the product runs over primes p.  When S_r is a Hecke eigenform
   of weight w, this equals the standard Dirichlet series sum S_r r^{-s}
   (by the Euler product formula for Hecke eigenforms).

4. SATAKE PARAMETERS

   At each prime p, the Hecke eigenvalue determines the Satake parameters
   alpha_p, beta_p via:
     lambda_p = alpha_p + beta_p,  alpha_p * beta_p = p^{w-1}.

   These are roots of X^2 - lambda_p X + p^{w-1} = 0.

5. RAMANUJAN BOUND

   The Ramanujan conjecture for weight-w modular forms states:
     |lambda_p| <= 2 p^{(w-1)/2}
   equivalently |alpha_p| = |beta_p| = p^{(w-1)/2} (tempered).

6. SYMMETRIC POWER L-FUNCTIONS

   L(Sym^n A, s) = prod_p prod_{j=0}^{n} (1 - alpha_p^{n-j} beta_p^j p^{-s})^{-1}

7. RANKIN-SELBERG CONVOLUTIONS

   L(A x B, s) = prod_p prod_{i,j in {0,1}} (1 - alpha_p^{(A,i)} alpha_p^{(B,j)} p^{-s})^{-1}

   where alpha_p^{(A,0)} = alpha_p(A), alpha_p^{(A,1)} = beta_p(A).

8. COMPARISON WITH RIEMANN ZETA

   If lambda_p(A) = p^{it} + p^{-it} for some t in R, then
   L^{Hecke}_A(s) ~ zeta(s + it) zeta(s - it).  The parameter t
   would be related to a Riemann zeta zero imaginary part if the shadow
   tower "sees" zeta zeros.

CONVENTIONS:
  - Cohomological grading (|d| = +1), bar uses desuspension.
  - Shadow coefficients S_r from shadow_euler_product_engine.py.
  - Default weight w = 2.
  - kappa = S_2.  S_r = 0 for r >= 3 (Heisenberg, class G).
  - S_3 = alpha (affine, class L).  S_4 = quartic (betagamma, class C).
  - Virasoro: full infinite tower, class M.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general.
CAUTION (AP10): Cross-family consistency checks are the real verification.
CAUTION (AP15): E_2* is quasi-modular; shadow forms are NOT classical.
CAUTION (AP38): Normalisation conventions must be tracked.

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

from sympy import (
    Rational,
    Symbol,
    cancel,
    sqrt as sym_sqrt,
    oo,
    N as Neval,
    simplify,
    I as sym_I,
    re as sym_re,
    im as sym_im,
)

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
        rankin_selberg_shadow_product,
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
        rankin_selberg_shadow_product,
    )

c = Symbol('c', positive=True)


# =============================================================================
# 0. Utility: prime sieve
# =============================================================================

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


PRIMES_100 = _primes_up_to(100)  # [2, 3, 5, 7, 11, ..., 97]


# =============================================================================
# 1. Shadow Hecke operators for all standard families
# =============================================================================

def shadow_family_coefficients(family: str,
                                param: Union[Rational, int, Fraction],
                                max_r: int = 60) -> Dict[int, Rational]:
    """Return shadow coefficients for a named family.

    Parameters
    ----------
    family : one of 'heisenberg', 'virasoro', 'affine_sl2', 'lattice', 'betagamma'
    param : the family parameter (k for Heisenberg, c for Virasoro, k for
            affine sl_2, rank for lattice, lambda for betagamma)
    max_r : truncation arity
    """
    if family == 'heisenberg':
        return heisenberg_shadow_coefficients(param, max_r)
    elif family == 'virasoro':
        return virasoro_shadow_coefficients(param, max_r)
    elif family == 'affine_sl2':
        return affine_sl2_shadow_coefficients(param, max_r)
    elif family == 'lattice':
        return lattice_shadow_coefficients(int(param), max_r)
    elif family == 'betagamma':
        return betagamma_shadow_coefficients(param, max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


def hecke_action_all_primes(S: Dict[int, Rational],
                             weight: Rational = Rational(2),
                             primes: Optional[List[int]] = None,
                             max_r: Optional[int] = None) -> Dict[int, Dict[int, Rational]]:
    """Apply T_p for each prime p and return {p: T_p(S)}.

    Parameters
    ----------
    S : shadow sequence {r: S_r}
    weight : the modular weight w (default 2)
    primes : list of primes; defaults to [2, 3, 5, ..., 97]
    max_r : truncation
    """
    if primes is None:
        primes = PRIMES_100
    if max_r is None:
        max_r = max(S.keys(), default=2)
    return {p: shadow_hecke_operator(S, p, weight, max_r) for p in primes}


# =============================================================================
# 2. Eigenvalue problem: is S_r a Hecke eigenform?
# =============================================================================

def hecke_eigenvalue_analysis(S: Dict[int, Rational],
                               weight: Rational = Rational(2),
                               primes: Optional[List[int]] = None,
                               max_r: Optional[int] = None) -> Dict[int, Dict[str, Any]]:
    """For each prime p, test whether S is an eigenform of T_p.

    Returns {p: {'is_eigenform': bool, 'eigenvalue': Rational or None,
                 'residuals': dict, 'projection_ratio': dict}}.

    The 'projection_ratio' is T_p(S)(r) / S(r) for each r where both
    are nonzero, providing a per-arity view of the eigenvalue structure.
    """
    if primes is None:
        primes = PRIMES_100
    if max_r is None:
        max_r = max(S.keys(), default=2)

    results = {}
    for p in primes:
        basic = hecke_eigenvalue_test(S, p, weight, max_r)

        # Compute per-arity ratio T_p(S)(r) / S(r)
        TpS = shadow_hecke_operator(S, p, weight, max_r)
        ratios = {}
        for r in range(2, max_r + 1):
            Sr = S.get(r, Rational(0))
            TpSr = TpS.get(r, Rational(0))
            if Sr != 0:
                ratios[r] = cancel(TpSr / Sr)
            elif TpSr != 0:
                ratios[r] = None  # T_p(S)(r) != 0 but S(r) = 0

        basic['projection_ratio'] = ratios
        results[p] = basic

    return results


def extract_eigenvalue(S: Dict[int, Rational],
                        p: int,
                        weight: Rational = Rational(2),
                        max_r: Optional[int] = None) -> Optional[Rational]:
    """Extract the Hecke eigenvalue lambda_p if S is an eigenform of T_p.

    Returns lambda_p or None if S is not an eigenform.
    """
    result = hecke_eigenvalue_test(S, p, weight, max_r)
    if result['is_eigenform']:
        return result['eigenvalue']
    return None


def hecke_eigenvalues_all_primes(S: Dict[int, Rational],
                                  weight: Rational = Rational(2),
                                  primes: Optional[List[int]] = None,
                                  max_r: Optional[int] = None) -> Dict[int, Optional[Rational]]:
    """Compute lambda_p for each prime p, returning None where not an eigenform."""
    if primes is None:
        primes = PRIMES_100
    return {p: extract_eigenvalue(S, p, weight, max_r) for p in primes}


# =============================================================================
# 3. Hecke L-function
# =============================================================================

def hecke_local_factor(lambda_p: Union[Rational, float],
                        p: int,
                        weight: Union[Rational, float],
                        s: float) -> float:
    """Evaluate the local Euler factor (1 - lambda_p p^{-s} + p^{w-1-2s})^{-1}.

    Returns a float.
    """
    ps = p ** (-s)
    pws = p ** (float(weight) - 1 - 2 * s)
    denom = 1.0 - float(lambda_p) * ps + pws
    if abs(denom) < 1e-300:
        return float('inf')
    return 1.0 / denom


def hecke_l_function(eigenvalues: Dict[int, Union[Rational, float, None]],
                      weight: Union[Rational, float],
                      s: float,
                      primes: Optional[List[int]] = None) -> float:
    """Evaluate the Hecke L-function as a partial Euler product.

    L^{Hecke}_A(s) = prod_{p in primes} (1 - lambda_p p^{-s} + p^{w-1-2s})^{-1}

    Primes where the eigenvalue is None are skipped (treated as unramified
    with lambda_p = 0, which gives a trivial factor).

    Parameters
    ----------
    eigenvalues : {p: lambda_p} from hecke_eigenvalues_all_primes
    weight : modular weight w
    s : evaluation point
    primes : which primes to include; defaults to all in eigenvalues
    """
    if primes is None:
        primes = sorted(eigenvalues.keys())
    product = 1.0
    for p in primes:
        lp = eigenvalues.get(p)
        if lp is None:
            continue
        factor = hecke_local_factor(lp, p, weight, s)
        if math.isinf(factor):
            return float('inf')
        product *= factor
    return product


def hecke_l_function_from_sequence(S: Dict[int, Rational],
                                    weight: Rational = Rational(2),
                                    s: float = 2.0,
                                    primes: Optional[List[int]] = None,
                                    max_r: Optional[int] = None) -> Dict[str, Any]:
    """Compute the Hecke L-function for a shadow sequence.

    This is the main interface: given a shadow sequence S, compute eigenvalues
    (or best approximations) and evaluate the L-function.

    Returns a dict with eigenvalues, L-function value, and diagnostic info.
    """
    if primes is None:
        primes = PRIMES_100
    if max_r is None:
        max_r = max(S.keys(), default=2)

    eigenvalues = {}
    eigenform_status = {}
    for p in primes:
        result = hecke_eigenvalue_test(S, p, weight, max_r)
        eigenvalues[p] = result['eigenvalue']
        eigenform_status[p] = result['is_eigenform']

    L_val = hecke_l_function(eigenvalues, weight, s, primes)

    # Also compute direct Dirichlet series for comparison
    L_direct = shadow_dirichlet_series_float(S, s, max_r)

    return {
        'eigenvalues': eigenvalues,
        'eigenform_status': eigenform_status,
        'L_euler_product': L_val,
        'L_dirichlet_sum': L_direct,
        'weight': weight,
        's': s,
    }


# =============================================================================
# 4. Satake parameters
# =============================================================================

def satake_parameters(lambda_p: Union[Rational, float, complex],
                       p: int,
                       weight: Union[Rational, float]) -> Tuple[complex, complex]:
    """Compute the Satake parameters alpha_p, beta_p from the Hecke eigenvalue.

    They are roots of X^2 - lambda_p X + p^{w-1} = 0:
        alpha_p = (lambda_p + sqrt(lambda_p^2 - 4 p^{w-1})) / 2
        beta_p  = (lambda_p - sqrt(lambda_p^2 - 4 p^{w-1})) / 2

    Returns (alpha_p, beta_p) as complex numbers.
    """
    lp = complex(lambda_p)
    pw = p ** (float(weight) - 1)
    disc = lp ** 2 - 4 * pw
    sqrt_disc = disc ** 0.5  # complex sqrt
    alpha = (lp + sqrt_disc) / 2
    beta = (lp - sqrt_disc) / 2
    return alpha, beta


def satake_parameters_all_primes(eigenvalues: Dict[int, Union[Rational, float, None]],
                                   weight: Union[Rational, float],
                                   primes: Optional[List[int]] = None) -> Dict[int, Tuple[complex, complex]]:
    """Compute Satake parameters at all primes."""
    if primes is None:
        primes = sorted(eigenvalues.keys())
    result = {}
    for p in primes:
        lp = eigenvalues.get(p)
        if lp is None:
            continue
        result[p] = satake_parameters(lp, p, weight)
    return result


def satake_product_check(alpha: complex, beta: complex,
                          p: int, weight: Union[Rational, float]) -> float:
    """Verify alpha * beta = p^{w-1}."""
    expected = p ** (float(weight) - 1)
    actual = alpha * beta
    return abs(actual - expected)


# =============================================================================
# 5. Ramanujan bound
# =============================================================================

def ramanujan_bound(p: int, weight: Union[Rational, float]) -> float:
    """The Ramanujan bound: 2 p^{(w-1)/2}."""
    return 2.0 * p ** ((float(weight) - 1) / 2.0)


def check_ramanujan_bound(lambda_p: Union[Rational, float, complex],
                            p: int,
                            weight: Union[Rational, float]) -> Dict[str, Any]:
    """Check whether |lambda_p| <= 2 p^{(w-1)/2} (Ramanujan bound).

    Returns:
      'satisfies': bool
      'lambda_p_abs': float
      'bound': float
      'ratio': |lambda_p| / bound (< 1 if satisfied)
    """
    lp_abs = abs(complex(lambda_p))
    bound = ramanujan_bound(p, weight)
    return {
        'satisfies': lp_abs <= bound + 1e-12,  # small tolerance
        'lambda_p_abs': lp_abs,
        'bound': bound,
        'ratio': lp_abs / bound if bound > 0 else float('inf'),
    }


def ramanujan_analysis_all_primes(eigenvalues: Dict[int, Union[Rational, float, None]],
                                    weight: Union[Rational, float],
                                    primes: Optional[List[int]] = None) -> Dict[int, Dict[str, Any]]:
    """Check Ramanujan bound at all primes."""
    if primes is None:
        primes = sorted(eigenvalues.keys())
    results = {}
    for p in primes:
        lp = eigenvalues.get(p)
        if lp is None:
            continue
        results[p] = check_ramanujan_bound(lp, p, weight)
    return results


def is_tempered(eigenvalues: Dict[int, Union[Rational, float, None]],
                 weight: Union[Rational, float],
                 primes: Optional[List[int]] = None) -> bool:
    """Check whether the shadow form is tempered (Ramanujan at all primes)."""
    analysis = ramanujan_analysis_all_primes(eigenvalues, weight, primes)
    return all(v['satisfies'] for v in analysis.values())


# =============================================================================
# 6. Symmetric power L-functions
# =============================================================================

def symmetric_power_local_factor(alpha: complex, beta: complex,
                                   n: int, p: int, s: float) -> complex:
    """Local factor of L(Sym^n A, s) at prime p.

    L_p(Sym^n, s) = prod_{j=0}^{n} (1 - alpha^{n-j} beta^j p^{-s})^{-1}
    """
    ps = p ** (-s)
    product = 1.0 + 0j
    for j in range(n + 1):
        coeff = alpha ** (n - j) * beta ** j
        factor = 1.0 - coeff * ps
        if abs(factor) < 1e-300:
            return complex(float('inf'), 0)
        product *= 1.0 / factor
    return product


def symmetric_power_l_function(satake_params: Dict[int, Tuple[complex, complex]],
                                 n: int,
                                 s: float,
                                 primes: Optional[List[int]] = None) -> complex:
    """Evaluate L(Sym^n A, s) as partial Euler product.

    Parameters
    ----------
    satake_params : {p: (alpha_p, beta_p)}
    n : symmetric power degree (n=1 is the original, n=2 is symmetric square)
    s : evaluation point
    """
    if primes is None:
        primes = sorted(satake_params.keys())
    product = 1.0 + 0j
    for p in primes:
        if p not in satake_params:
            continue
        alpha, beta = satake_params[p]
        factor = symmetric_power_local_factor(alpha, beta, n, p, s)
        product *= factor
    return product


def symmetric_power_suite(S: Dict[int, Rational],
                           weight: Rational = Rational(2),
                           max_n: int = 4,
                           s: float = 3.0,
                           primes: Optional[List[int]] = None,
                           max_r: Optional[int] = None) -> Dict[int, complex]:
    """Compute L(Sym^n A, s) for n = 1, 2, ..., max_n.

    Returns {n: L(Sym^n, s)}.
    """
    if primes is None:
        primes = PRIMES_100
    evs = hecke_eigenvalues_all_primes(S, weight, primes, max_r)
    # Filter to primes where eigenvalue is available
    valid_evs = {p: v for p, v in evs.items() if v is not None}
    sps = satake_parameters_all_primes(valid_evs, weight, list(valid_evs.keys()))

    results = {}
    for n in range(1, max_n + 1):
        results[n] = symmetric_power_l_function(sps, n, s, list(sps.keys()))
    return results


# =============================================================================
# 7. Rankin-Selberg L-function for pairs of families
# =============================================================================

def rankin_selberg_local_factor(alpha_A: complex, beta_A: complex,
                                 alpha_B: complex, beta_B: complex,
                                 p: int, s: float) -> complex:
    """Local factor of L(A x B, s) at prime p.

    L_p(A x B, s) = prod_{i in {0,1}, j in {0,1}}
                       (1 - alpha^{(A,i)} alpha^{(B,j)} p^{-s})^{-1}

    where alpha^{(X,0)} = alpha_X, alpha^{(X,1)} = beta_X.
    """
    ps = p ** (-s)
    product = 1.0 + 0j
    for aA in [alpha_A, beta_A]:
        for aB in [alpha_B, beta_B]:
            factor = 1.0 - aA * aB * ps
            if abs(factor) < 1e-300:
                return complex(float('inf'), 0)
            product *= 1.0 / factor
    return product


def rankin_selberg_l_function(satake_A: Dict[int, Tuple[complex, complex]],
                                satake_B: Dict[int, Tuple[complex, complex]],
                                s: float,
                                primes: Optional[List[int]] = None) -> complex:
    """Evaluate L(A x B, s) as partial Euler product."""
    if primes is None:
        common = sorted(set(satake_A.keys()) & set(satake_B.keys()))
    else:
        common = [p for p in primes if p in satake_A and p in satake_B]
    product = 1.0 + 0j
    for p in common:
        aA, bA = satake_A[p]
        aB, bB = satake_B[p]
        factor = rankin_selberg_local_factor(aA, bA, aB, bB, p, s)
        product *= factor
    return product


def rankin_selberg_pair(S_A: Dict[int, Rational],
                         S_B: Dict[int, Rational],
                         weight_A: Rational = Rational(2),
                         weight_B: Rational = Rational(2),
                         s: float = 3.0,
                         primes: Optional[List[int]] = None,
                         max_r: Optional[int] = None) -> Dict[str, Any]:
    """Compute L(A x B, s) for two shadow sequences.

    Returns Euler product value, pointwise product Dirichlet sum, and Satake data.
    """
    if primes is None:
        primes = PRIMES_100
    ev_A = hecke_eigenvalues_all_primes(S_A, weight_A, primes, max_r)
    ev_B = hecke_eigenvalues_all_primes(S_B, weight_B, primes, max_r)
    valid_A = {p: v for p, v in ev_A.items() if v is not None}
    valid_B = {p: v for p, v in ev_B.items() if v is not None}
    sp_A = satake_parameters_all_primes(valid_A, weight_A)
    sp_B = satake_parameters_all_primes(valid_B, weight_B)

    L_euler = rankin_selberg_l_function(sp_A, sp_B, s, primes)

    # Also compute pointwise product sum for comparison
    if max_r is None:
        max_r = min(max(S_A.keys(), default=2), max(S_B.keys(), default=2))
    RS_prod = rankin_selberg_shadow_product(S_A, S_B, max_r)
    L_pointwise = shadow_dirichlet_series_float(RS_prod, s, max_r)

    return {
        'L_euler': L_euler,
        'L_pointwise': L_pointwise,
        'satake_A': sp_A,
        'satake_B': sp_B,
        'eigenvalues_A': ev_A,
        'eigenvalues_B': ev_B,
    }


# =============================================================================
# 8. Comparison with Riemann zeta
# =============================================================================

def eisenstein_eigenvalue(p: int, t: float) -> complex:
    """Eigenvalue of an Eisenstein series at spectral parameter t.

    For the non-holomorphic Eisenstein series E(s, z) on SL(2,Z),
    the Hecke eigenvalue at prime p is:
        lambda_p = p^{it} + p^{-it} = 2 cos(t log p)

    This is REAL for t real (tempered principal series).
    """
    return p ** (1j * t) + p ** (-1j * t)


def compare_with_eisenstein(eigenvalues: Dict[int, Union[Rational, float, None]],
                              t_candidates: Optional[List[float]] = None,
                              primes: Optional[List[int]] = None) -> Dict[float, float]:
    """Compare shadow Hecke eigenvalues with Eisenstein eigenvalues.

    For each candidate t, compute:
      E(t) = sum_p |lambda_p(shadow) - (p^{it} + p^{-it})|^2

    The minimum over t is the best-fit spectral parameter.

    Parameters
    ----------
    eigenvalues : {p: lambda_p}
    t_candidates : list of spectral parameters to try; defaults to a
                   grid near the first few Riemann zeta zero imaginary parts
    primes : which primes to use
    """
    if primes is None:
        primes = [p for p in sorted(eigenvalues.keys()) if eigenvalues.get(p) is not None]
    if not primes:
        return {}

    # First 10 non-trivial zeta zero imaginary parts (Odlyzko)
    ZETA_ZEROS = [
        14.134725,
        21.022040,
        25.010858,
        30.424876,
        32.935062,
        37.586178,
        40.918719,
        43.327073,
        48.005151,
        49.773832,
    ]

    if t_candidates is None:
        # Grid: some standard values plus zeta zero imaginary parts
        t_candidates = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0] + ZETA_ZEROS

    results = {}
    for t in t_candidates:
        err = 0.0
        count = 0
        for p in primes:
            lp = eigenvalues[p]
            if lp is None:
                continue
            eisen = eisenstein_eigenvalue(p, t)
            diff = complex(lp) - eisen
            err += abs(diff) ** 2
            count += 1
        if count > 0:
            results[t] = err / count  # mean squared error
    return results


def best_fit_spectral_parameter(eigenvalues: Dict[int, Union[Rational, float, None]],
                                  t_range: Tuple[float, float] = (0.0, 60.0),
                                  n_grid: int = 1000,
                                  primes: Optional[List[int]] = None) -> Dict[str, float]:
    """Find the spectral parameter t that best fits the shadow eigenvalues.

    Searches over a fine grid in [t_range[0], t_range[1]].

    Returns {'t_best': float, 'mse': float, 'nearest_zeta_zero': float}.
    """
    ZETA_ZEROS = [
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
        37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    ]

    t_grid = [t_range[0] + (t_range[1] - t_range[0]) * i / n_grid
              for i in range(n_grid + 1)]
    errors = compare_with_eisenstein(eigenvalues, t_grid, primes)

    if not errors:
        return {'t_best': 0.0, 'mse': float('inf'), 'nearest_zeta_zero': 0.0}

    t_best = min(errors, key=errors.get)
    mse = errors[t_best]

    # Find nearest zeta zero
    nearest = min(ZETA_ZEROS, key=lambda z: abs(z - t_best))

    return {
        't_best': t_best,
        'mse': mse,
        'nearest_zeta_zero': nearest,
        'distance_to_zero': abs(t_best - nearest),
    }


# =============================================================================
# 9. Functional equation analysis
# =============================================================================

def completed_l_function_ratio(S: Dict[int, Rational],
                                weight: Rational = Rational(2),
                                s: float = 2.0,
                                primes: Optional[List[int]] = None,
                                max_r: Optional[int] = None) -> Dict[str, float]:
    """Evaluate Lambda(s) / Lambda(w - s) where Lambda = Gamma-factor x L.

    For a weight-w modular form, the completed L-function satisfies:
        Lambda(s) = epsilon * Lambda(w - s)

    where epsilon = +/-1 is the root number.

    We compute the ratio numerically and check if |ratio| ~ 1.
    """
    if primes is None:
        primes = PRIMES_100
    w = float(weight)

    # L(s) and L(w - s) via Euler product
    info_s = hecke_l_function_from_sequence(S, weight, s, primes, max_r)
    info_ws = hecke_l_function_from_sequence(S, weight, w - s, primes, max_r)

    L_s = info_s['L_euler_product']
    L_ws = info_ws['L_euler_product']

    # Gamma factor ratio: Gamma(s) / Gamma(w - s)
    # For weight w, the Gamma factor is (2pi)^{-s} Gamma(s).
    try:
        gamma_s = math.lgamma(s)
        gamma_ws = math.lgamma(w - s)
        log_gamma_ratio = gamma_s - gamma_ws + s * math.log(2 * math.pi) - (w - s) * math.log(2 * math.pi)
        gamma_ratio = math.exp(log_gamma_ratio)
    except (ValueError, OverflowError):
        gamma_ratio = float('nan')

    if abs(L_ws) < 1e-300 or math.isinf(L_s) or math.isinf(L_ws):
        ratio = float('nan')
    else:
        ratio = (L_s / L_ws) * gamma_ratio

    return {
        'L_s': L_s,
        'L_w_minus_s': L_ws,
        'gamma_ratio': gamma_ratio,
        'ratio': ratio,
        'weight': w,
        's': s,
    }


# =============================================================================
# 10. Class-specific Hecke analysis
# =============================================================================

def heisenberg_hecke_analysis(k_val: Union[Rational, int] = 1,
                                weight: Rational = Rational(2),
                                max_r: int = 30) -> Dict[str, Any]:
    """Hecke analysis for Heisenberg.

    Heisenberg has S_2 = k, S_r = 0 for r >= 3 (class G).
    The Hecke operator T_p maps almost everything to zero.

    T_p(S)(r): S(pr) = 0 for pr >= 3 (since S_r = 0 for r >= 3, and pr >= 4
    for r >= 2, p >= 2), EXCEPT T_2(S)(2) = S(4) + 2^{w-1} S(1) = 0 + 0 = 0.
    Wait: S(pr) for r >= 2, p >= 2 gives pr >= 4.  S(4) = 0 (Heisenberg).
    And S(r/p) requires p | r and r/p >= 2.  For r=2, p=2: r/p = 1 < 2, so = 0.
    For r=2p (p >= 2): S(2p / p) = S(2) = k, so T_p(S)(2p) = S(2p^2) + p^{w-1} S(2).
    S(2p^2) = 0 for p >= 2 (since 2p^2 >= 8 > 2).  So T_p(S)(2p) = p^{w-1} * k.
    But S(2p) = 0 for p >= 2.  So T_p(S) != lambda * S in general.

    Conclusion: Heisenberg is NOT a Hecke eigenform for any T_p, because
    T_p creates nonzero entries at r = 2p where S(2p) = 0.
    """
    S = heisenberg_shadow_coefficients(k_val, max_r)
    analysis = hecke_eigenvalue_analysis(S, weight, PRIMES_100[:5], max_r)
    return {
        'family': 'heisenberg',
        'param': k_val,
        'shadow_class': 'G',
        'analysis': analysis,
        'is_eigenform': all(v['is_eigenform'] for v in analysis.values()),
        'note': 'Class G: T_p creates entries at r=2p where S(2p)=0 (not eigenform)',
    }


def virasoro_hecke_analysis(c_val: Union[Rational, int] = 1,
                              weight: Rational = Rational(2),
                              max_r: int = 40) -> Dict[str, Any]:
    """Hecke analysis for Virasoro.

    Virasoro has class M (infinite tower).  The Hecke operator T_p acts
    nontrivially.  The question is whether the resulting sequence is
    proportional to the original.
    """
    S = virasoro_shadow_coefficients(c_val, max_r)
    primes_small = PRIMES_100[:10]  # first 10 primes
    analysis = hecke_eigenvalue_analysis(S, weight, primes_small, max_r)

    # Satake analysis at primes where eigenvalue exists
    satake = {}
    for p, info in analysis.items():
        lp = info.get('eigenvalue')
        if lp is not None:
            satake[p] = satake_parameters(lp, p, weight)

    return {
        'family': 'virasoro',
        'param': c_val,
        'shadow_class': 'M',
        'analysis': analysis,
        'satake': satake,
        'is_eigenform': all(v['is_eigenform'] for v in analysis.values()),
    }


def affine_sl2_hecke_analysis(k_val: Union[Rational, int] = 1,
                                weight: Rational = Rational(2),
                                max_r: int = 30) -> Dict[str, Any]:
    """Hecke analysis for affine sl_2.

    Class L: S_2 = kappa, S_3 = alpha, S_r = 0 for r >= 4.
    Similar to Heisenberg: T_p creates entries outside the support.
    """
    S = affine_sl2_shadow_coefficients(k_val, max_r)
    analysis = hecke_eigenvalue_analysis(S, weight, PRIMES_100[:5], max_r)
    return {
        'family': 'affine_sl2',
        'param': k_val,
        'shadow_class': 'L',
        'analysis': analysis,
        'is_eigenform': all(v['is_eigenform'] for v in analysis.values()),
        'note': 'Class L: tower terminates at arity 3',
    }


# =============================================================================
# 11. Multi-family Rankin-Selberg
# =============================================================================

def standard_family_pairs() -> List[Tuple[str, Any, str, Any]]:
    """Return standard pairs for Rankin-Selberg analysis.

    Each entry: (family_A, param_A, family_B, param_B).
    """
    return [
        ('heisenberg', 1, 'virasoro', 1),
        ('heisenberg', 1, 'virasoro', Rational(1, 2)),
        ('affine_sl2', 1, 'virasoro', 1),
        ('heisenberg', 1, 'affine_sl2', 1),
        ('virasoro', 1, 'virasoro', Rational(1, 2)),
        ('virasoro', Rational(13), 'virasoro', Rational(13)),  # self-dual
        ('lattice', 8, 'virasoro', 1),
        ('betagamma', 1, 'virasoro', 1),
    ]


def rankin_selberg_standard_pairs(weight: Rational = Rational(2),
                                    s: float = 3.0,
                                    max_r: int = 30) -> Dict[str, Dict[str, Any]]:
    """Compute Rankin-Selberg L-functions for all standard family pairs."""
    results = {}
    for (fam_A, par_A, fam_B, par_B) in standard_family_pairs():
        key = f"{fam_A}({par_A}) x {fam_B}({par_B})"
        S_A = shadow_family_coefficients(fam_A, par_A, max_r)
        S_B = shadow_family_coefficients(fam_B, par_B, max_r)
        results[key] = rankin_selberg_pair(S_A, S_B, weight, weight, s, PRIMES_100[:5], max_r)
    return results


# =============================================================================
# 12. Weight determination
# =============================================================================

def determine_shadow_weight(S: Dict[int, Rational],
                              weight_candidates: Optional[List[Rational]] = None,
                              primes: Optional[List[int]] = None,
                              max_r: Optional[int] = None) -> Dict[Rational, int]:
    """Try different weights and count how many primes give eigenforms.

    The "correct" weight is the one that maximises the number of primes
    for which S is a Hecke eigenform.

    Returns {weight: count_of_eigenform_primes}.
    """
    if weight_candidates is None:
        weight_candidates = [Rational(w) for w in range(0, 7)]
    if primes is None:
        primes = PRIMES_100[:10]

    results = {}
    for w in weight_candidates:
        count = 0
        for p in primes:
            test = hecke_eigenvalue_test(S, p, w, max_r)
            if test['is_eigenform']:
                count += 1
        results[w] = count
    return results


# =============================================================================
# 13. Hecke algebra and commutation
# =============================================================================

def hecke_commutation_test(S: Dict[int, Rational],
                             p: int, q: int,
                             weight: Rational = Rational(2),
                             max_r: Optional[int] = None) -> Dict[str, Any]:
    """Test whether T_p T_q = T_q T_p on S.

    The abstract Hecke algebra has T_p T_q = T_q T_p for all p, q coprime.
    This should hold regardless of whether S is an eigenform.

    For p = q, the Hecke relation is:
        T_{p^2} = T_p^2 - p^{w-1} T_1
    where T_1 = identity.
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)

    TpS = shadow_hecke_operator(S, p, weight, max_r)
    TqS = shadow_hecke_operator(S, q, weight, max_r)

    # T_q(T_p(S)) and T_p(T_q(S))
    TqTpS = shadow_hecke_operator(TpS, q, weight, max_r)
    TpTqS = shadow_hecke_operator(TqS, p, weight, max_r)

    # Check difference
    max_diff = Rational(0)
    diffs = {}
    for r in range(2, max_r + 1):
        diff = cancel(TqTpS.get(r, Rational(0)) - TpTqS.get(r, Rational(0)))
        if diff != 0:
            diffs[r] = diff
            if abs(float(diff)) > abs(float(max_diff)):
                max_diff = diff

    return {
        'commutes': len(diffs) == 0,
        'differences': diffs,
        'max_diff': max_diff,
        'p': p,
        'q': q,
    }


# =============================================================================
# 14. Hecke orbit structure for terminating towers
# =============================================================================

def hecke_orbit_terminating(S: Dict[int, Rational],
                              p: int,
                              weight: Rational = Rational(2),
                              max_iter: int = 5,
                              max_r: Optional[int] = None) -> List[Dict[int, Rational]]:
    """Compute the Hecke orbit {S, T_p(S), T_p^2(S), ...} for a terminating tower.

    For class G/L/C towers, T_p spreads the support.  The orbit shows how
    Hecke operators "fill in" the zero entries.

    Returns a list of shadow sequences [S, T_p(S), T_p^2(S), ...].
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)
    orbit = [S]
    current = S
    for _ in range(max_iter):
        current = shadow_hecke_operator(current, p, weight, max_r)
        orbit.append(current)
    return orbit
