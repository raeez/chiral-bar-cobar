r"""bc_euler_product_shadow_engine.py -- BC-85: Euler product structure of shadow zeta.

For the Riemann zeta: zeta(s) = prod_p (1-p^{-s})^{-1}.  Does the shadow zeta
    zeta_A(s) = sum_{r>=2} S_r(A) * r^{-s}
have an Euler product?  The key test: compute the Dirichlet series coefficients
and check if the associated von Mangoldt function vanishes at non-prime-powers.

MATHEMATICAL FRAMEWORK
======================

1. MULTIPLICATIVE STRUCTURE OF SHADOW COEFFICIENTS
   Test whether S_{mn} = S_m * S_n for gcd(m,n)=1.
   If S is multiplicative: zeta_A(s) = prod_p (sum_{k>=0} S_{p^k} p^{-ks}).
   If NOT multiplicative: no classical Euler product.

2. LOG-DERIVATIVE TEST
   Compute -zeta_A'(s)/zeta_A(s) = sum Lambda_A(n) n^{-s}.
   If Euler product exists: Lambda_A(n) = 0 for n not a prime power.
   Compute Lambda_A(n) via Moebius inversion:
     Lambda_A(n) = sum_{d|n} mu(n/d) * (-S_d * log d)  (formal)
   and also via the recursion from the log-derivative convolution identity.

3. LOCAL FACTORS
   F_p(X) = 1 + sum_{k>=1} S_{p^k} X^k
   Rationality test: is F_p(X) = P_p(X)/Q_p(X)?

4. FACTORIZATION OBSTRUCTION
   E_A(s) = zeta_A(s) / prod_{p<=P} F_p(p^{-s})
   If Euler product holds, E_A -> 0 as P -> infinity.

5. PRIME POWER SHADOW COEFFICIENTS
   Compare S_{p^k} vs (S_p)^k (completely multiplicative test).

6. SHADOW SATAKE PARAMETERS
   If F_p(X) = (1 - alpha_p X)^{-1}(1 - beta_p X)^{-1}, solve for alpha_p, beta_p.

7. RANKIN-SELBERG FROM EULER PRODUCT
   If Euler product exists, L(s, zeta_A x zeta_B) has a local factorization.

CONVENTIONS:
  - Shadow coefficients S_r start at r=2 with S_2 = kappa (the modular characteristic).
  - S_1 := 0 by convention (shadow towers have no arity-1 term).
  - For the Dirichlet series with Euler product, we use
    L_A(s) = 1 + sum_{r>=2} S_r r^{-s}   (constant term 1 for multiplicativity).
  - Cohomological grading (|d| = +1), bar uses desuspension.

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general (AP48 for non-Virasoro).
CAUTION (AP10): Never hardcode wrong expected values in tests.
CAUTION (AP15): E_2* is quasi-modular; do not conflate with holomorphic forms.
CAUTION (AP38): Normalize conventions carefully when comparing literature values.

Manuscript references:
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

from sympy import Rational, cancel

# ---------------------------------------------------------------------------
# 0. Number-theoretic utilities
# ---------------------------------------------------------------------------


def _primes_up_to(N: int) -> List[int]:
    """Sieve of Eratosthenes returning primes <= N."""
    if N < 2:
        return []
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
    return [i for i in range(2, N + 1) if sieve[i]]


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def _is_prime_power(n: int) -> Tuple[bool, int, int]:
    """Return (True, p, k) if n = p^k with k >= 1, else (False, 0, 0)."""
    if n < 2:
        return (False, 0, 0)
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            temp = n
            while temp % d == 0:
                temp //= d
                k += 1
            if temp == 1:
                return (True, d, k)
            else:
                return (False, 0, 0)
        d += 1
    # n is prime
    return (True, n, 1)


def _mobius(n: int) -> int:
    """Moebius function mu(n)."""
    if n == 1:
        return 1
    d = 2
    num_factors = 0
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            temp //= d
            num_factors += 1
            if temp % d == 0:
                return 0  # p^2 divides n
        d += 1
    if temp > 1:
        num_factors += 1
    return (-1) ** num_factors


def _von_mangoldt(n: int) -> float:
    """Classical von Mangoldt function: Lambda(n) = log(p) if n=p^k, else 0."""
    ok, p, k = _is_prime_power(n)
    return math.log(p) if ok else 0.0


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def _divisors(n: int) -> List[int]:
    """All divisors of n, unsorted."""
    divs = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    return sorted(divs)


# ---------------------------------------------------------------------------
# 1. Shadow coefficient providers (exact, Rational)
# ---------------------------------------------------------------------------


def virasoro_shadow_coefficients(c_val: Union[Rational, int, Fraction],
                                  max_r: int = 100) -> Dict[int, Rational]:
    r"""Compute Virasoro shadow coefficients S_2, ..., S_{max_r} at central charge c.

    Uses the convolution recursion from sqrt(Q_L):
        a_0 = c,  a_1 = 6,  a_2 = 40/(c(5c+22))
        a_n = -(1/(2c)) * sum_{j=1}^{n-1} a_j * a_{n-j}   for n >= 3
        S_r = a_{r-2} / r

    Returns dict {r: S_r} with exact Rational values.
    """
    cv = Rational(c_val)
    if cv == 0:
        raise ValueError("Virasoro shadow coefficients undefined at c=0.")

    a = [Rational(0)] * (max_r - 1)
    a[0] = cv
    if max_r > 2:
        a[1] = Rational(6)
    if max_r > 3:
        a[2] = Rational(40) / (cv * (5 * cv + 22))

    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv / (2 * cv))

    result: Dict[int, Rational] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = cancel(a[idx] / r)
    return result


def virasoro_shadow_coefficients_float(c_val: float,
                                        max_r: int = 100) -> Dict[int, float]:
    """Virasoro shadow coefficients via float recursion (faster for large max_r)."""
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    a = [0.0] * (max_r - 1)
    a[0] = c_val
    if max_r > 2:
        a[1] = 6.0
    if max_r > 3:
        a[2] = 40.0 / (c_val * (5.0 * c_val + 22.0))

    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2.0 * c_val)

    result: Dict[int, float] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / float(r)
    return result


def heisenberg_shadow_coefficients(k_val: Union[Rational, int, Fraction],
                                    max_r: int = 100) -> Dict[int, Rational]:
    """Heisenberg: S_2 = k, S_r = 0 for r >= 3 (class G)."""
    kv = Rational(k_val)
    result = {2: kv}
    for r in range(3, max_r + 1):
        result[r] = Rational(0)
    return result


def affine_sl2_shadow_coefficients(k_val: Union[Rational, int, Fraction],
                                    max_r: int = 100) -> Dict[int, Rational]:
    """Affine sl_2: kappa = 3(k+2)/4, S_3 = 4/(k+2), S_r = 0 for r >= 4 (class L)."""
    kv = Rational(k_val)
    kappa = Rational(3) * (kv + 2) / 4
    S3 = Rational(4) / (kv + 2)  # 2*h^v/(k+h^v) with h^v(sl_2)=2
    result = {2: kappa, 3: S3}
    for r in range(4, max_r + 1):
        result[r] = Rational(0)
    return result


def lattice_shadow_coefficients(rank: int,
                                 max_r: int = 100) -> Dict[int, Rational]:
    """Lattice VOA: kappa = rank, S_r = 0 for r >= 3 (class G)."""
    result = {2: Rational(rank)}
    for r in range(3, max_r + 1):
        result[r] = Rational(0)
    return result


# ---------------------------------------------------------------------------
# 2. Multiplicativity tests
# ---------------------------------------------------------------------------


def test_multiplicativity(S: Dict[int, Any],
                           max_r: int = 60) -> Dict[str, Any]:
    r"""Test whether S_{mn} = S_m * S_n for all coprime m, n with mn <= max_r.

    Returns dict with:
      'is_multiplicative': bool
      'failures': list of (m, n, S_{mn}, S_m * S_n)
      'tested_pairs': count of coprime pairs tested
    """
    failures = []
    tested = 0
    for m in range(2, max_r + 1):
        for n in range(m, max_r // m + 1):
            if _gcd(m, n) != 1:
                continue
            mn = m * n
            if mn > max_r:
                continue
            S_mn = S.get(mn, 0)
            S_m = S.get(m, 0)
            S_n = S.get(n, 0)
            product = S_m * S_n
            tested += 1
            # Use float comparison for float dicts, exact for Rational
            if isinstance(S_mn, Rational):
                if cancel(S_mn - product) != 0:
                    failures.append((m, n, S_mn, product))
            else:
                if abs(float(S_mn) - float(product)) > 1e-12 * max(1, abs(float(S_mn)), abs(float(product))):
                    failures.append((m, n, float(S_mn), float(product)))
    return {
        'is_multiplicative': len(failures) == 0,
        'failures': failures,
        'tested_pairs': tested,
    }


def test_complete_multiplicativity(S: Dict[int, Any],
                                    max_r: int = 60) -> Dict[str, Any]:
    r"""Test S_{mn} = S_m * S_n for ALL m, n (not just coprime)."""
    failures = []
    tested = 0
    for m in range(2, max_r + 1):
        for n in range(2, max_r // m + 1):
            mn = m * n
            if mn > max_r:
                continue
            S_mn = S.get(mn, 0)
            S_m = S.get(m, 0)
            S_n = S.get(n, 0)
            product = S_m * S_n
            tested += 1
            if isinstance(S_mn, Rational):
                if cancel(S_mn - product) != 0:
                    failures.append((m, n, S_mn, product))
            else:
                if abs(float(S_mn) - float(product)) > 1e-12 * max(1, abs(float(S_mn)), abs(float(product))):
                    failures.append((m, n, float(S_mn), float(product)))
    return {
        'is_multiplicative': len(failures) == 0,
        'failures': failures,
        'tested_pairs': tested,
    }


def multiplicativity_defect(S: Dict[int, Any],
                             max_r: int = 60) -> Dict[int, float]:
    r"""For each composite n with coprime factorization n = m * k, compute
    the multiplicativity defect delta(n) = S_n - S_m * S_k.

    Returns {n: max |defect| over all coprime factorizations}.
    """
    defects: Dict[int, float] = {}
    for n in range(4, max_r + 1):
        max_def = 0.0
        for m in range(2, n):
            if n % m != 0:
                continue
            k = n // m
            if k < 2 or _gcd(m, k) != 1:
                continue
            S_n = float(S.get(n, 0))
            S_m = float(S.get(m, 0))
            S_k = float(S.get(k, 0))
            d = abs(S_n - S_m * S_k)
            if d > max_def:
                max_def = d
        if max_def > 0:
            defects[n] = max_def
    return defects


# ---------------------------------------------------------------------------
# 3. Shadow von Mangoldt function (Moebius inversion)
# ---------------------------------------------------------------------------


def shadow_von_mangoldt_mobius(S: Dict[int, Any],
                                max_r: Optional[int] = None) -> Dict[int, float]:
    r"""Compute the shadow von Mangoldt function via Moebius inversion.

    Lambda_A(n) = sum_{d|n} mu(n/d) * S_d * log(d)

    This is the formal Moebius inversion of the relation
        S_n * log(n) = sum_{d|n} Lambda_A(d) * 1     (if S multiplicative)

    Actually the correct relation for log derivative of 1 + sum S_r r^{-s} is:
        Lambda_A(n) = sum_{d|n} mu(n/d) * a(d)
    where a(n) = S_n * log(n) - sum_{d|n, d<n} Lambda_A(d) * S_{n/d}.

    For the FORMAL Moebius approach (testing multiplicativity):
    If the Dirichlet series were L_A(s) = prod_p (F_p(p^{-s})) then
        -L_A'/L_A(s) = sum Lambda_A(n) n^{-s}
    and Lambda_A is supported on prime powers.

    We use the RECURSION approach (log-derivative convolution):
        Lambda_A(r) = S_r * log(r) - sum_{d|r, 2<=d<r, r/d>=2} Lambda_A(d) * S_{r/d}

    with the convention L_A(s) = 1 + sum_{r>=2} S_r r^{-s}.
    """
    if max_r is None:
        max_r = max(S.keys())

    Lambda: Dict[int, float] = {}
    for r in range(2, max_r + 1):
        Sr = float(S.get(r, 0))
        val = Sr * math.log(r)
        for d in range(2, r):
            if r % d != 0:
                continue
            q = r // d
            if q < 2:
                continue
            Sq = float(S.get(q, 0))
            val -= Lambda.get(d, 0.0) * Sq
        Lambda[r] = val
    return Lambda


def shadow_von_mangoldt_direct_mobius(S: Dict[int, Any],
                                       max_r: Optional[int] = None) -> Dict[int, float]:
    r"""Compute Lambda_A via DIRECT Moebius inversion formula.

    Lambda_A(n) = sum_{d|n} mu(n/d) * b(d)

    where b(d) = S_d * log(d) for the log derivative of L_A(s) = 1 + sum S_r r^{-s}.

    This is an ALTERNATIVE computation path to shadow_von_mangoldt_mobius.
    The two agree if and only if the computation is correct.

    NOTE: This formula is exact only if S is multiplicative.  For non-multiplicative S,
    the log-derivative recursion (shadow_von_mangoldt_mobius) is the correct definition,
    and this direct formula will differ -- the DIFFERENCE measures the non-multiplicativity.
    """
    if max_r is None:
        max_r = max(S.keys())

    Lambda: Dict[int, float] = {}
    for n in range(2, max_r + 1):
        val = 0.0
        for d in _divisors(n):
            if d < 2:
                continue
            mu_nd = _mobius(n // d)
            if mu_nd == 0:
                continue
            Sd = float(S.get(d, 0))
            val += mu_nd * Sd * math.log(d)
        Lambda[n] = val
    return Lambda


def von_mangoldt_prime_power_support(Lambda: Dict[int, float],
                                      max_r: Optional[int] = None,
                                      tol: float = 1e-10) -> Dict[str, Any]:
    r"""Check whether Lambda_A(n) vanishes at non-prime-power n.

    If the shadow zeta has an Euler product, Lambda_A should be supported
    on prime powers.  Returns diagnostics.
    """
    if max_r is None:
        max_r = max(Lambda.keys())

    non_pp_nonzero = []
    pp_values = []
    for n in range(2, max_r + 1):
        val = Lambda.get(n, 0.0)
        is_pp, p, k = _is_prime_power(n)
        if is_pp:
            pp_values.append((n, p, k, val))
        else:
            if abs(val) > tol:
                non_pp_nonzero.append((n, val))

    return {
        'euler_product_holds': len(non_pp_nonzero) == 0,
        'non_prime_power_violations': non_pp_nonzero,
        'prime_power_values': pp_values,
        'max_non_pp_abs': max((abs(v) for _, v in non_pp_nonzero), default=0.0),
    }


# ---------------------------------------------------------------------------
# 4. Local factors at primes
# ---------------------------------------------------------------------------


def local_factor_coefficients(S: Dict[int, Any],
                               p: int,
                               max_power: int = 10) -> List[float]:
    r"""Extract the local factor coefficients at prime p.

    F_p(X) = 1 + sum_{k>=1} S_{p^k} X^k

    Returns [1, S_p, S_{p^2}, S_{p^3}, ...] as floats.
    """
    coeffs = [1.0]  # constant term 1 for L_A = 1 + sum S_r r^{-s}
    for k in range(1, max_power + 1):
        pk = p ** k
        coeffs.append(float(S.get(pk, 0)))
    return coeffs


def local_factor_evaluate(S: Dict[int, Any],
                            p: int,
                            X: complex,
                            max_power: int = 10) -> complex:
    """Evaluate F_p(X) = 1 + sum_{k>=1} S_{p^k} X^k."""
    coeffs = local_factor_coefficients(S, p, max_power)
    return sum(c * X ** k for k, c in enumerate(coeffs))


def local_factor_rationality_test(S: Dict[int, Any],
                                    p: int,
                                    max_power: int = 10,
                                    max_degree: int = 4) -> Dict[str, Any]:
    r"""Test whether F_p(X) is a rational function P(X)/Q(X).

    Try to fit F_p(X) as a ratio of polynomials of degrees (d1, d2) for
    d1 + d2 <= max_degree.  Uses the Pade approximant approach:

    F_p(X) * Q(X) = P(X)   mod X^{max_power+1}

    For each (d1, d2), solve the linear system and check the residual.
    """
    coeffs = local_factor_coefficients(S, p, max_power)
    n_coeffs = len(coeffs)

    best = {'d1': 0, 'd2': 0, 'residual': float('inf'), 'P': [], 'Q': []}

    for d2 in range(0, max_degree + 1):
        for d1 in range(0, max_degree + 1 - d2):
            # We need n_coeffs > d1 + d2 to have an overdetermined system
            # F * Q = P means:
            # sum_{j=0}^{d2} q_j * coeffs[k-j] = p_k  for k=0,...,d1
            # sum_{j=0}^{d2} q_j * coeffs[k-j] = 0     for k=d1+1,...,n_coeffs-1
            # Normalize: q_0 = 1
            # So we have n_unknown = d1 + 1 + d2 unknowns (p_0,...,p_{d1}, q_1,...,q_{d2})
            # and n_coeffs equations.

            if n_coeffs < d1 + d2 + 1:
                continue

            # Build linear system
            n_eqs = n_coeffs
            n_unk = (d1 + 1) + d2  # p_0...p_{d1}, q_1...q_{d2}

            import numpy as np
            A = np.zeros((n_eqs, n_unk))
            b_vec = np.zeros(n_eqs)

            for k in range(n_eqs):
                # P side: p_k if k <= d1
                if k <= d1:
                    A[k, k] = 1.0

                # Q side: -sum_{j=1}^{d2} q_j * coeffs[k-j]
                for j in range(1, d2 + 1):
                    idx = k - j
                    if 0 <= idx < n_coeffs:
                        A[k, d1 + 1 + (j - 1)] = -coeffs[idx]

                # RHS: coeffs[k] (from q_0 = 1 contribution)
                b_vec[k] = coeffs[k]

            # Solve in least squares
            try:
                sol, residuals, rank, sv = np.linalg.lstsq(A, b_vec, rcond=None)
            except np.linalg.LinAlgError:
                continue

            # Compute residual
            res = np.linalg.norm(A @ sol - b_vec)

            P_coeffs = list(sol[:d1 + 1])
            Q_coeffs = [1.0] + list(sol[d1 + 1:])

            if res < best['residual']:
                best = {
                    'd1': d1, 'd2': d2,
                    'residual': float(res),
                    'P': P_coeffs,
                    'Q': Q_coeffs,
                }

    return best


# ---------------------------------------------------------------------------
# 5. Prime power ratio S_{p^k} / (S_p)^k
# ---------------------------------------------------------------------------


def prime_power_ratio(S: Dict[int, Any],
                       p: int,
                       max_k: int = 10) -> Dict[int, Optional[float]]:
    r"""Compute S_{p^k} / (S_p)^k for k = 1, ..., max_k.

    If S is completely multiplicative: ratio = 1 for all k.
    If merely multiplicative: ratio follows a pattern from Satake parameters.
    """
    Sp = float(S.get(p, 0))
    ratios: Dict[int, Optional[float]] = {}
    for k in range(1, max_k + 1):
        pk = p ** k
        Spk = float(S.get(pk, 0))
        Sp_k = Sp ** k
        if abs(Sp_k) > 1e-100:
            ratios[k] = Spk / Sp_k
        else:
            ratios[k] = None
    return ratios


def prime_power_recursion_check(S: Dict[int, Any],
                                  p: int,
                                  max_k: int = 8) -> Dict[str, Any]:
    r"""Check if S_{p^k} satisfies a degree-2 recursion:
        S_{p^{k+1}} = S_p * S_{p^k} - chi(p) * S_{p^{k-1}}

    For the Hecke eigenform case: chi(p) = p^{w-1} for some weight w.
    We extract chi(p) from the first few values and check consistency.

    Returns: chi_p, residuals, whether recursion holds.
    """
    Sp = float(S.get(p, 0))
    Sp2 = float(S.get(p ** 2, 0))
    Sp3 = float(S.get(p ** 3, 0))

    # From k=1: S_{p^2} = S_p^2 - chi(p) * S_{p^0}
    # S_{p^0} = S_1 = 0 by our convention (shadow starts at r=2)
    # So chi(p) is NOT directly extractable from S_{p^2} = S_p^2 - chi(p) * 0
    # unless we use the convention S_{p^0} = 1 (for L_A = 1 + sum).
    # With S_{p^0} = 1: chi(p) = S_p^2 - S_{p^2}

    S_p0 = 1.0  # convention for L_A = 1 + sum S_r r^{-s}

    if abs(S_p0) < 1e-100:
        return {'chi_p': None, 'recursion_holds': False, 'residuals': {}}

    chi_p = Sp ** 2 - Sp2  # from S_{p^2} = S_p^2 - chi(p) * 1

    # Now check: S_{p^{k+1}} = S_p * S_{p^k} - chi_p * S_{p^{k-1}}
    # for k = 2, 3, ...
    # S values: S_{p^0} = 1, S_{p^1} = S_p, S_{p^2}, S_{p^3}, ...
    pp_vals = [1.0, Sp, Sp2, Sp3]
    for k in range(4, max_k + 1):
        pk = p ** k
        ppv = float(S.get(pk, 0))
        pp_vals.append(ppv)

    residuals: Dict[int, float] = {}
    for k in range(2, len(pp_vals) - 1):
        predicted = Sp * pp_vals[k] - chi_p * pp_vals[k - 1]
        actual = pp_vals[k + 1]
        residuals[k] = abs(predicted - actual)

    holds = all(v < 1e-8 for v in residuals.values()) if residuals else True

    return {
        'chi_p': chi_p,
        'recursion_holds': holds,
        'residuals': residuals,
    }


# ---------------------------------------------------------------------------
# 6. Shadow Satake parameters
# ---------------------------------------------------------------------------


def shadow_satake_parameters(S: Dict[int, Any],
                               p: int) -> Dict[str, Any]:
    r"""Extract Satake parameters alpha_p, beta_p from S_p and S_{p^2}.

    If F_p(X) = (1 - alpha_p X)^{-1} (1 - beta_p X)^{-1}, then:
        S_{p^k} = sum_{j=0}^k alpha_p^j * beta_p^{k-j}
    In particular:
        S_p     = alpha_p + beta_p
        S_{p^2} = alpha_p^2 + alpha_p * beta_p + beta_p^2
                = (alpha_p + beta_p)^2 - alpha_p * beta_p
                = S_p^2 - alpha_p * beta_p

    So: alpha_p * beta_p = S_p^2 - S_{p^2}
    And: alpha_p, beta_p are roots of X^2 - S_p X + (S_p^2 - S_{p^2}) = 0.

    NOTE: We use convention S_{p^0} = 1 (from F_p(0) = 1).
    """
    Sp = float(S.get(p, 0))
    Sp2 = float(S.get(p ** 2, 0))

    # alpha + beta = S_p
    # alpha * beta = S_p^2 - S_{p^2}
    ab = Sp ** 2 - Sp2
    disc = Sp ** 2 - 4 * ab  # = 4 * Sp2 - 3 * Sp^2

    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
        alpha = (Sp + sqrt_disc) / 2.0
        beta = (Sp - sqrt_disc) / 2.0
        on_unit_circle = False  # real => not on unit circle (unless both zero)
    else:
        sqrt_disc = cmath.sqrt(disc)
        alpha = (Sp + sqrt_disc) / 2.0
        beta = (Sp - sqrt_disc) / 2.0
        # On unit circle if |alpha| = |beta| = something specific
        on_unit_circle = abs(abs(alpha) - abs(beta)) < 1e-10

    return {
        'alpha_p': alpha,
        'beta_p': beta,
        'sum_ab': Sp,
        'product_ab': ab,
        'discriminant': disc,
        'abs_alpha': abs(alpha),
        'abs_beta': abs(beta),
        'on_unit_circle': on_unit_circle,
        'ramanujan_bound': abs(alpha) <= p ** 0.5 + 1e-10 and abs(beta) <= p ** 0.5 + 1e-10,
    }


def satake_predicted_coefficients(alpha: complex,
                                    beta: complex,
                                    max_k: int = 10) -> List[complex]:
    r"""From Satake parameters (alpha, beta), predict S_{p^k} for k=0,...,max_k.

    S_{p^k} = sum_{j=0}^k alpha^j beta^{k-j} = (alpha^{k+1} - beta^{k+1})/(alpha - beta)
    if alpha != beta, else S_{p^k} = (k+1) alpha^k.
    """
    if abs(alpha - beta) > 1e-15:
        return [(alpha ** (k + 1) - beta ** (k + 1)) / (alpha - beta)
                for k in range(max_k + 1)]
    else:
        return [(k + 1) * alpha ** k for k in range(max_k + 1)]


# ---------------------------------------------------------------------------
# 7. Partial Euler product and factorization obstruction
# ---------------------------------------------------------------------------


def partial_euler_product(S: Dict[int, Any],
                           s: complex,
                           P_max: int = 50,
                           local_max_power: int = 8) -> complex:
    r"""Compute the partial Euler product prod_{p <= P_max} F_p(p^{-s}).

    F_p(X) = 1 + sum_{k>=1} S_{p^k} X^k,  evaluated at X = p^{-s}.

    If the shadow zeta has a true Euler product, this should converge
    to zeta_A(s) = 1 + sum_{r>=2} S_r r^{-s} as P_max -> infinity.
    """
    primes = _primes_up_to(P_max)
    product = 1.0 + 0.0j
    for p in primes:
        X = p ** (-s)
        Fp = local_factor_evaluate(S, p, X, local_max_power)
        product *= Fp
    return product


def shadow_zeta_direct(S: Dict[int, Any],
                        s: complex,
                        max_r: Optional[int] = None) -> complex:
    r"""Direct evaluation of zeta_A(s) = 1 + sum_{r>=2} S_r r^{-s}."""
    if max_r is None:
        max_r = max(S.keys())
    total = 1.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = S.get(r, 0)
        if Sr == 0:
            continue
        total += float(Sr) * r ** (-s)
    return total


def factorization_obstruction(S: Dict[int, Any],
                                s: complex,
                                P_values: List[int],
                                max_r: Optional[int] = None,
                                local_max_power: int = 8) -> Dict[int, complex]:
    r"""Compute the factorization obstruction E_A(s, P).

    E_A(s, P) = zeta_A(s) / prod_{p<=P} F_p(p^{-s})

    If Euler product holds exactly: E_A -> 1 as P -> infinity.
    Returns {P: E_A(s, P)} for each P in P_values.
    """
    zeta_val = shadow_zeta_direct(S, s, max_r)
    result: Dict[int, complex] = {}
    for P in P_values:
        ep = partial_euler_product(S, s, P, local_max_power)
        if abs(ep) > 1e-100:
            result[P] = zeta_val / ep
        else:
            result[P] = complex('inf')
    return result


# ---------------------------------------------------------------------------
# 8. Rankin-Selberg from Euler product
# ---------------------------------------------------------------------------


def rankin_selberg_from_euler(S_A: Dict[int, Any],
                                S_B: Dict[int, Any],
                                p: int,
                                max_k: int = 5) -> List[complex]:
    r"""Compute the local factor of L(s, zeta_A x zeta_B) at prime p from Satake.

    If alpha_A, beta_A (resp. alpha_B, beta_B) are the Satake parameters,
    the Rankin-Selberg local factor is:
        det(I - M_p X)^{-1}
    where M_p = diag(alpha_A alpha_B, alpha_A beta_B, beta_A alpha_B, beta_A beta_B).

    The coefficients are C_k = Tr(M_p^k) for the symmetric functions.

    Returns the RS local factor coefficients [1, C_1, C_2, ...].
    """
    sat_A = shadow_satake_parameters(S_A, p)
    sat_B = shadow_satake_parameters(S_B, p)

    a_A, b_A = sat_A['alpha_p'], sat_A['beta_p']
    a_B, b_B = sat_B['alpha_p'], sat_B['beta_p']

    eigenvalues = [a_A * a_B, a_A * b_B, b_A * a_B, b_A * b_B]

    # Power sums -> elementary symmetric polynomials -> determinant expansion
    # For a degree-d Euler factor with eigenvalues lambda_1,...,lambda_d:
    # F_p(X) = prod_i (1 - lambda_i X)^{-1}
    # log F_p(X) = sum_{k>=1} (sum_i lambda_i^k) X^k / k
    # F_p(X) = exp(sum_{k>=1} p_k X^k / k) where p_k = sum lambda_i^k

    coeffs = [complex(1)]
    for k in range(1, max_k + 1):
        # Newton's identity: k * e_k = sum_{i=1}^k (-1)^{i-1} p_i * e_{k-i}
        # where p_i = sum lambda_j^i (power sums) and e_k = elementary symmetric.
        # But we want the coefficients of prod (1 - lam_i X)^{-1}, which is
        # 1/det(1 - MX) = sum_k h_k(eigenvalues) X^k
        # where h_k = complete homogeneous symmetric polynomial.
        # Recursion: h_k = sum_{i=1}^k p_i h_{k-i} / k
        pk = sum(lam ** k for lam in eigenvalues)
        hk = sum(pk_j * coeffs[k - j] for j, pk_j in
                 enumerate([sum(lam ** (j + 1) for lam in eigenvalues) for j in range(k)], 1)
                 if k - j >= 0)
        # Simpler: h_k = (1/k) sum_{j=1}^k p_j h_{k-j}
        hk_val = complex(0)
        for j in range(1, k + 1):
            pj = sum(lam ** j for lam in eigenvalues)
            hkj = coeffs[k - j] if k - j >= 0 else 0
            hk_val += pj * hkj
        hk_val /= k
        coeffs.append(hk_val)

    return coeffs


def rankin_selberg_direct(S_A: Dict[int, Any],
                           S_B: Dict[int, Any],
                           s: complex,
                           max_r: Optional[int] = None) -> complex:
    r"""Direct Rankin-Selberg: L(s, A x B) = sum_{r>=2} S_r(A) S_r(B) r^{-s}."""
    if max_r is None:
        max_r = min(max(S_A.keys()), max(S_B.keys()))
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sa = float(S_A.get(r, 0))
        Sb = float(S_B.get(r, 0))
        if Sa == 0 or Sb == 0:
            continue
        total += Sa * Sb * r ** (-s)
    return total


# ---------------------------------------------------------------------------
# 9. Convergence analysis
# ---------------------------------------------------------------------------


def euler_product_convergence_rate(S: Dict[int, Any],
                                     s_values: List[complex],
                                     P_schedule: List[int],
                                     local_max_power: int = 8) -> Dict:
    r"""Measure how fast the partial Euler product converges to zeta_A.

    For each s in s_values and each P in P_schedule, compute
        |zeta_A(s) - prod_{p<=P} F_p(p^{-s})| / |zeta_A(s)|

    Returns nested dict {s: {P: relative_error}}.
    """
    max_r = max(S.keys())
    result: Dict = {}
    for s in s_values:
        zeta_val = shadow_zeta_direct(S, s, max_r)
        if abs(zeta_val) < 1e-100:
            result[s] = {P: float('inf') for P in P_schedule}
            continue
        row: Dict[int, float] = {}
        for P in P_schedule:
            ep = partial_euler_product(S, s, P, local_max_power)
            row[P] = abs(zeta_val - ep) / abs(zeta_val)
        result[s] = row
    return result


# ---------------------------------------------------------------------------
# 10. Cross-verification: Euler product at integers vs direct sum
# ---------------------------------------------------------------------------


def euler_vs_direct_at_integers(S: Dict[int, Any],
                                  s_integers: List[int],
                                  P_max: int = 50) -> Dict[int, Dict[str, float]]:
    r"""Compare partial Euler product with direct sum at integer s values.

    Returns {s: {'direct': val, 'euler': val, 'abs_diff': diff, 'rel_diff': rel}}.
    """
    max_r = max(S.keys())
    result: Dict[int, Dict[str, float]] = {}
    for s in s_integers:
        direct = shadow_zeta_direct(S, s, max_r)
        euler = partial_euler_product(S, s, P_max)
        d = abs(direct - euler)
        rel = d / abs(direct) if abs(direct) > 1e-100 else float('inf')
        result[s] = {
            'direct': float(direct.real),
            'euler': float(euler.real),
            'abs_diff': d,
            'rel_diff': rel,
        }
    return result


# ---------------------------------------------------------------------------
# 11. Comprehensive Euler product analysis
# ---------------------------------------------------------------------------


def full_euler_product_analysis(S: Dict[int, Any],
                                  family_name: str = "unknown",
                                  max_r_mult: int = 60,
                                  max_r_vm: int = 60,
                                  primes_for_satake: Optional[List[int]] = None,
                                  ) -> Dict[str, Any]:
    r"""Run the full Euler product analysis on a shadow coefficient sequence.

    Returns a comprehensive dictionary with all tests:
    1. Multiplicativity test
    2. Complete multiplicativity test
    3. Von Mangoldt prime-power support test
    4. Local factor rationality at small primes
    5. Satake parameters at small primes
    6. Prime power recursion check
    7. Factorization obstruction at s = 2, 3, 4
    """
    if primes_for_satake is None:
        primes_for_satake = [2, 3, 5, 7, 11]

    results: Dict[str, Any] = {'family': family_name}

    # 1. Multiplicativity
    results['multiplicativity'] = test_multiplicativity(S, max_r_mult)

    # 2. Complete multiplicativity
    results['complete_multiplicativity'] = test_complete_multiplicativity(S, max_r_mult)

    # 3. Von Mangoldt
    Lambda = shadow_von_mangoldt_mobius(S, max_r_vm)
    results['von_mangoldt'] = von_mangoldt_prime_power_support(Lambda, max_r_vm)

    # 4. Local factor rationality
    local_rat = {}
    for p in primes_for_satake:
        local_rat[p] = local_factor_rationality_test(S, p, max_power=8, max_degree=3)
    results['local_rationality'] = local_rat

    # 5. Satake parameters
    satake = {}
    for p in primes_for_satake:
        satake[p] = shadow_satake_parameters(S, p)
    results['satake'] = satake

    # 6. Prime power recursion
    pp_rec = {}
    for p in primes_for_satake:
        pp_rec[p] = prime_power_recursion_check(S, p, max_k=6)
    results['prime_power_recursion'] = pp_rec

    # 7. Factorization obstruction
    results['factorization_obstruction'] = factorization_obstruction(
        S, 3.0, [10, 30, 50], local_max_power=6)

    return results
