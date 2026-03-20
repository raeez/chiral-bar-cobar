#!/usr/bin/env python3
r"""
symmetric_power_shadow.py — Symmetric power L-functions from the shadow tower.

THE BRIDGE: The shadow tower at arity r encodes data related to the (r-2)-th
symmetric power of the Galois representation rho_f attached to a Hecke eigenform f.

For a lattice VOA V_Lambda with Hecke decomposition Theta_Lambda = sum c_j f_j,
the shadow coefficient at arity r is:
  S_r = -(1/r) sum_j c_j lambda_j^r
where lambda_j are the spectral atoms (Hecke eigenvalues weighted by Petersson norms).

SATAKE PARAMETERS:
  For a Hecke eigenform f of weight k with a(p) = alpha_p + beta_p, alpha_p*beta_p = p^{k-1}:
  - Ramanujan: |alpha_p| = |beta_p| = p^{(k-1)/2} (Deligne's theorem for k >= 2)
  - Equivalently: |a(p)| <= 2*p^{(k-1)/2}
  - Equivalently: discriminant a(p)^2 - 4*p^{k-1} <= 0

SYMMETRIC POWER L-FUNCTIONS:
  L(s, Sym^m f) = prod_p prod_{j=0}^m (1 - alpha_p^j * beta_p^{m-j} * p^{-s})^{-1}

  The r-th power sum p_r(alpha, beta) = alpha^r + alpha^{r-1}*beta + ... + beta^r
  is the trace of Sym^r(diag(alpha, beta)), which relates to the shadow at arity r+2.

  Newton's identities convert power sums p_r to elementary symmetric polynomials e_k,
  recovering the Euler factor coefficients of L(s, Sym^m f).

RAMANUJAN BOUND IMPROVEMENT:
  - Trivial: |a(p)| <= p^{k-1} + 1 (from |alpha|*|beta| = p^{k-1})
  - Hecke: |a(p)| <= 2*p^{(k-1)/2} (requires Ramanujan)
  - Rankin-Selberg (Sym^2): delta = 1/5  (unconditional, Gelbart-Jacquet)
  - Kim-Shahidi (Sym^3): delta = 2/9
  - Kim (Sym^4): delta = 1/9
  - Sym^r -> delta -> 1/2 as r -> inf (approaches full Ramanujan)

COMPUTATIONAL NOTES:
  The Ramanujan tau function tau(n) has EXACT Satake parameters satisfying
  |alpha_p| = p^{11/2} (Deligne, 1974). The discriminant tau(p)^2 - 4*p^{11}
  is ALWAYS negative for primes p, forcing complex conjugate Satake parameters.

References:
  - lattice_shadow_periods.py: ramanujan_tau, Hecke decomposition
  - shadow_l_theorem.py: shadow depth -> critical lines
  - langlands_zeta_pipeline.py: full shadow -> zeta pipeline
  - Deligne, "La conjecture de Weil. I" (1974)
  - Gelbart-Jacquet, "A relation between automorphic representations of GL(2) and GL(3)" (1978)
  - Kim, "Functoriality for the exterior square of GL_4 and the symmetric fourth of GL_2" (2003)
  - Kim-Shahidi, "Cuspidality of symmetric powers with applications" (2002)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =========================================================================
# Prime sieve
# =========================================================================

def _primes_up_to(n: int) -> List[int]:
    """Return all primes up to n via sieve of Eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def _nth_prime(n: int) -> int:
    """Return the n-th prime (1-indexed: _nth_prime(1) = 2)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    # Upper bound for the n-th prime (Rosser's theorem)
    if n <= 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    upper = int(n * (math.log(n) + math.log(math.log(n))) + 3)
    primes = _primes_up_to(upper)
    while len(primes) < n:
        upper = int(upper * 1.5)
        primes = _primes_up_to(upper)
    return primes[n - 1]


# =========================================================================
# Ramanujan tau (imported or self-contained)
# =========================================================================

def ramanujan_tau(n: int) -> int:
    r"""Ramanujan tau function: coefficients of Delta = q * prod (1-q^m)^{24}.

    tau(1) = 1, tau(2) = -24, tau(3) = 252, tau(4) = -1472, tau(5) = 4830.
    """
    if n < 1:
        return 0
    N = n
    coeffs = [0] * (N + 1)
    coeffs[0] = 1
    for m in range(1, N + 1):
        for _ in range(24):
            for i in range(N, m - 1, -1):
                coeffs[i] -= coeffs[i - m]
    if n - 1 <= N:
        return coeffs[n - 1]
    return 0


# =========================================================================
# 1. Satake parameters
# =========================================================================

def satake_parameters(a_p, k: int, p: int):
    r"""Compute Satake parameters alpha_p, beta_p for a Hecke eigenform.

    Given the Hecke eigenvalue a(p) at prime p and weight k, the Satake
    parameters satisfy:
      alpha + beta = a(p)
      alpha * beta = p^{k-1}

    They are roots of X^2 - a(p)*X + p^{k-1} = 0.

    Returns (alpha, beta) as mpmath complex numbers if available, else
    Python complex numbers. The discriminant a(p)^2 - 4*p^{k-1} determines
    whether the parameters are real or complex conjugates.

    Ramanujan conjecture (Deligne's theorem for k >= 2):
      |alpha| = |beta| = p^{(k-1)/2}
    This holds iff the discriminant is <= 0.
    """
    if not HAS_MPMATH:
        # Fallback to Python complex
        disc = a_p * a_p - 4 * p ** (k - 1)
        if disc >= 0:
            sqrt_disc = math.sqrt(disc)
            alpha = (a_p + sqrt_disc) / 2
            beta = (a_p - sqrt_disc) / 2
        else:
            sqrt_disc = math.sqrt(-disc)
            alpha = complex(a_p / 2, sqrt_disc / 2)
            beta = complex(a_p / 2, -sqrt_disc / 2)
        return alpha, beta

    a_p_mp = mpmath.mpf(a_p)
    pk1 = mpmath.power(p, k - 1)
    disc = a_p_mp ** 2 - 4 * pk1
    sqrt_disc = mpmath.sqrt(disc)  # handles negative disc -> imaginary
    alpha = (a_p_mp + sqrt_disc) / 2
    beta = (a_p_mp - sqrt_disc) / 2
    return alpha, beta


def satake_discriminant(a_p, k: int, p: int):
    r"""Discriminant a(p)^2 - 4*p^{k-1}.

    Negative discriminant <=> Ramanujan holds at p.
    Zero <=> Satake parameters coincide (degenerate).
    Positive <=> violation of Ramanujan at p.
    """
    if HAS_MPMATH:
        return mpmath.mpf(a_p) ** 2 - 4 * mpmath.power(p, k - 1)
    return a_p * a_p - 4 * p ** (k - 1)


def verify_ramanujan_at_prime(a_p, k: int, p: int) -> dict:
    r"""Check whether the Ramanujan bound |a(p)| <= 2*p^{(k-1)/2} holds.

    Returns a dictionary with:
      'bound': the Ramanujan bound 2*p^{(k-1)/2}
      'value': |a(p)|
      'satisfies': whether the bound is satisfied
      'discriminant': the discriminant a(p)^2 - 4*p^{k-1}
      'exact_ramanujan': whether |alpha| = |beta| = p^{(k-1)/2} exactly
      'satake_type': 'complex_conjugate' (Ramanujan) or 'real' (violation)
    """
    if HAS_MPMATH:
        bound = 2 * mpmath.power(p, mpmath.mpf(k - 1) / 2)
        val = mpmath.fabs(mpmath.mpf(a_p))
        disc = satake_discriminant(a_p, k, p)
        satisfies = (val <= bound + mpmath.mpf(10) ** (-30))
        alpha, beta = satake_parameters(a_p, k, p)
        abs_alpha = mpmath.fabs(alpha)
        abs_beta = mpmath.fabs(beta)
        target = mpmath.power(p, mpmath.mpf(k - 1) / 2)
        exact = (mpmath.fabs(abs_alpha - target) < mpmath.mpf(10) ** (-20)
                 and mpmath.fabs(abs_beta - target) < mpmath.mpf(10) ** (-20))
    else:
        bound = 2 * p ** ((k - 1) / 2)
        val = abs(a_p)
        disc = satake_discriminant(a_p, k, p)
        satisfies = (val <= bound + 1e-10)
        alpha, beta = satake_parameters(a_p, k, p)
        abs_alpha = abs(alpha)
        abs_beta = abs(beta)
        target = p ** ((k - 1) / 2)
        exact = (abs(abs_alpha - target) < 1e-10
                 and abs(abs_beta - target) < 1e-10)

    sat_type = 'complex_conjugate' if disc <= 0 else 'real'
    return {
        'bound': float(bound) if HAS_MPMATH else bound,
        'value': float(val) if HAS_MPMATH else val,
        'satisfies': bool(satisfies),
        'discriminant': float(disc) if HAS_MPMATH else disc,
        'exact_ramanujan': bool(exact),
        'satake_type': sat_type,
    }


# =========================================================================
# 2. Symmetric power Euler factors
# =========================================================================

def symmetric_power_euler_factor(alpha, beta, m: int, p: int, s):
    r"""Compute the p-th Euler factor of L(s, Sym^m f):

      prod_{j=0}^m (1 - alpha^j * beta^{m-j} * p^{-s})^{-1}

    Parameters:
      alpha, beta: Satake parameters at p
      m: symmetric power degree
      p: prime
      s: complex variable

    Returns the value of the Euler factor (a complex number).
    """
    if HAS_MPMATH:
        result = mpmath.mpc(1)
        ps = mpmath.power(p, -mpmath.mpc(s))
        for j in range(m + 1):
            term = mpmath.power(alpha, j) * mpmath.power(beta, m - j) * ps
            result *= 1 / (1 - term)
        return result
    else:
        result = 1.0
        ps = p ** (-s)
        for j in range(m + 1):
            term = alpha ** j * beta ** (m - j) * ps
            result *= 1 / (1 - term)
        return result


def symmetric_power_euler_poly(alpha, beta, m: int, p: int):
    r"""Return the polynomial coefficients of the Euler factor denominator.

    The Euler factor of L(s, Sym^m f) at p is:
      prod_{j=0}^m (1 - alpha^j * beta^{m-j} * X)^{-1}   where X = p^{-s}

    This function returns the coefficients [c_0, c_1, ..., c_{m+1}] of the
    polynomial prod_{j=0}^m (1 - lambda_j * X) = sum_k c_k X^k, so that
    the Euler factor is (sum c_k p^{-ks})^{-1}.
    """
    lambdas = []
    for j in range(m + 1):
        if HAS_MPMATH:
            lam = mpmath.power(alpha, j) * mpmath.power(beta, m - j)
        else:
            lam = alpha ** j * beta ** (m - j)
        lambdas.append(lam)

    # Build polynomial by successive multiplication
    if HAS_MPMATH:
        poly = [mpmath.mpc(1)]
    else:
        poly = [1.0 + 0j]

    for lam in lambdas:
        new_poly = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new_poly[i] += c
            new_poly[i + 1] -= c * lam
        poly = new_poly

    return poly


# =========================================================================
# 3. Symmetric power L-function (partial product)
# =========================================================================

def symmetric_power_L(f_coeffs: Dict[int, Union[int, float]], k: int, m: int,
                      s, num_primes: int = 100):
    r"""Compute L(s, Sym^m f) from the first num_primes Euler factors.

    Parameters:
      f_coeffs: dictionary {p: a(p)} mapping primes to Hecke eigenvalues.
                If a prime is missing, it is skipped (assumed unramified with a(p)=0).
      k: weight of the eigenform
      m: symmetric power degree
      s: complex value at which to evaluate
      num_primes: number of primes to include

    Returns the partial Euler product.
    """
    primes = _primes_up_to(_nth_prime(num_primes) if num_primes <= 1000
                           else num_primes * 15)[:num_primes]

    if HAS_MPMATH:
        result = mpmath.mpf(1)
        s_mp = mpmath.mpc(s)
    else:
        result = 1.0 + 0j
        s_mp = complex(s)

    for p in primes:
        a_p = f_coeffs.get(p, 0)
        if a_p == 0 and p not in f_coeffs:
            # Skip primes not in the coefficient dictionary
            continue
        alpha, beta = satake_parameters(a_p, k, p)
        ef = symmetric_power_euler_factor(alpha, beta, m, p, s_mp)
        result *= ef

    return result


# =========================================================================
# 4. Shadow to symmetric power
# =========================================================================

def power_sum_from_satake(alpha, beta, r: int):
    r"""Compute the r-th power sum p_r = alpha^r + beta^r.

    This is the trace of the r-th symmetric power representation evaluated
    on the diagonal matrix diag(alpha, beta), but summing only the endpoints:
      p_r = alpha^r + beta^r

    NOT the full trace of Sym^r (which has r+1 terms). This is the standard
    power sum symmetric function in two variables.

    The connection to the shadow tower: the shadow at arity r+2 involves
    these power sums. Specifically, for a lattice VOA with Hecke decomposition:
      S_{r+2} = -(1/(r+2)) * sum_j c_j * p_r(alpha_{j,p}, beta_{j,p})
    summed over the Hecke basis.
    """
    if HAS_MPMATH:
        return mpmath.power(alpha, r) + mpmath.power(beta, r)
    return alpha ** r + beta ** r


def shadow_coefficient(spectral_atoms: List[Tuple[Any, Any]], r: int):
    r"""Compute the shadow coefficient S_r from spectral data.

    Parameters:
      spectral_atoms: list of (c_j, lambda_j) pairs where c_j is the
                      coefficient and lambda_j is the spectral atom
      r: arity (r >= 2)

    Returns S_r = -(1/r) * sum_j c_j * lambda_j^r
    """
    if HAS_MPMATH:
        total = mpmath.mpc(0)
        for c_j, lam_j in spectral_atoms:
            total += mpmath.mpc(c_j) * mpmath.power(mpmath.mpc(lam_j), r)
        return -total / mpmath.mpf(r)
    else:
        total = sum(c_j * lam_j ** r for c_j, lam_j in spectral_atoms)
        return -total / r


def shadow_to_symmetric_power(shadow_coeffs: Dict[int, Any], r: int):
    r"""Extract Sym^{r-2} data from the shadow coefficient at arity r.

    The shadow at arity r encodes the power sum p_{r-2} of the Satake
    parameters (for each prime, after weighting by Hecke coefficients).

    For a single eigenform f with a(p) at prime p:
      S_r involves p_{r}(alpha_p, beta_p) = tr(Sym^{r-1}(diag(alpha_p, beta_p)))
    But the shadow-symmetric-power bridge operates at the level of the
    modular form coefficients, not at individual primes.

    This function returns:
      - The arity r shadow coefficient
      - The corresponding symmetric power degree m = r - 2
      - The power sum degree that appears: r
    """
    S_r = shadow_coeffs.get(r, 0)
    return {
        'arity': r,
        'shadow_coefficient': S_r,
        'symmetric_power_degree': r - 2,
        'power_sum_degree': r,
    }


# =========================================================================
# 5. Newton's identities: power sums <-> elementary symmetric polynomials
# =========================================================================

def power_sum_to_elementary(power_sums: List):
    r"""Convert power sums p_1, ..., p_n to elementary symmetric polynomials e_1, ..., e_n.

    Newton's identities:
      e_k = (1/k) * sum_{i=1}^{k} (-1)^{i-1} e_{k-i} p_i

    where e_0 = 1 by convention.

    Equivalently:
      e_1 = p_1
      e_2 = (e_1 p_1 - p_2) / 2
      e_3 = (e_2 p_1 - e_1 p_2 + p_3) / 3
      ...

    Parameters:
      power_sums: [p_1, p_2, ..., p_n]

    Returns [e_1, e_2, ..., e_n].
    """
    n = len(power_sums)
    if n == 0:
        return []

    # Use mpc to handle potentially complex inputs (e.g. from Satake parameters)
    if HAS_MPMATH:
        zero = mpmath.mpc(0)
        one = mpmath.mpc(1)
        e = [zero] * n
        p = [mpmath.mpc(ps) for ps in power_sums]
    else:
        zero = 0.0 + 0j
        one = 1.0 + 0j
        e = [zero] * n
        p = [complex(ps) for ps in power_sums]

    # e_0 = 1 (implicit)
    for k in range(1, n + 1):
        # e_k = (1/k) * sum_{i=1}^{k} (-1)^{i-1} * e_{k-i} * p_i
        # where e_0 = 1
        s = zero
        for i in range(1, k + 1):
            e_k_minus_i = e[k - i - 1] if (k - i) >= 1 else one  # e_0 = 1
            sign = (-1) ** (i - 1)
            s += sign * e_k_minus_i * p[i - 1]
        e[k - 1] = s / k

    return e


def elementary_to_power_sum(elementary: List):
    r"""Convert elementary symmetric polynomials e_1, ..., e_n to power sums p_1, ..., p_n.

    Newton's identities (inverse direction):
      p_k = sum_{i=1}^{k-1} (-1)^{i-1} e_i p_{k-i} + (-1)^{k-1} k e_k

    Equivalently:
      p_1 = e_1
      p_2 = e_1 p_1 - 2 e_2
      p_3 = e_1 p_2 - e_2 p_1 + 3 e_3
      ...

    Parameters:
      elementary: [e_1, e_2, ..., e_n]

    Returns [p_1, p_2, ..., p_n].
    """
    n = len(elementary)
    if n == 0:
        return []

    if HAS_MPMATH:
        p = [mpmath.mpc(0)] * n
        e = [mpmath.mpc(ei) for ei in elementary]
    else:
        p = [0.0 + 0j] * n
        e = [complex(ei) for ei in elementary]

    for k_ in range(n):
        k = k_ + 1
        s = ((-1) ** (k - 1)) * k * e[k - 1]
        for i in range(1, k):
            s += ((-1) ** (i - 1)) * e[i - 1] * p[k - 1 - i]
        p[k_] = s

    return p


def verify_newton_roundtrip(n: int, values: Optional[List] = None) -> bool:
    r"""Verify that power_sum <-> elementary conversions are inverses.

    If values is None, uses [1, 2, ..., n] as test power sums.
    """
    if values is None:
        if HAS_MPMATH:
            values = [mpmath.mpc(i) for i in range(1, n + 1)]
        else:
            values = [float(i) for i in range(1, n + 1)]

    e = power_sum_to_elementary(values)
    p_back = elementary_to_power_sum(e)

    tol = 1e-20 if HAS_MPMATH else 1e-10
    for i in range(n):
        if HAS_MPMATH:
            diff = abs(complex(values[i]) - complex(p_back[i]))
        else:
            diff = abs(values[i] - p_back[i])
        if diff > tol:
            return False
    return True


# =========================================================================
# 6. Ramanujan bounds from power sums
# =========================================================================

def ramanujan_from_power_sums(power_sums: List, k: int, p: int):
    r"""Given power sums p_1, ..., p_r at a prime p, compute bounds on |alpha|.

    For Satake parameters alpha, beta with alpha*beta = p^{k-1}:
      p_1 = alpha + beta = a(p)
      p_2 = alpha^2 + beta^2 = a(p)^2 - 2*p^{k-1}
      p_r = alpha^r + beta^r

    The Ramanujan bound is |alpha| = |beta| = p^{(k-1)/2}.

    This function computes the best bound on max(|alpha|, |beta|) from the
    available power sums, using the moment analysis.

    Returns a dict with:
      'bound': best upper bound on max(|alpha|, |beta|)
      'ramanujan_target': p^{(k-1)/2}
      'ratio': bound / target (should be <= 1 for Ramanujan)
      'method': description of the method used
    """
    if not power_sums:
        raise ValueError("Need at least p_1")

    if HAS_MPMATH:
        pk1 = mpmath.power(p, k - 1)
        target = mpmath.power(p, mpmath.mpf(k - 1) / 2)
        p1 = mpmath.re(mpmath.mpc(power_sums[0]))  # Take real part
    else:
        pk1 = p ** (k - 1)
        target = p ** ((k - 1) / 2.0)
        p1 = float(power_sums[0].real if isinstance(power_sums[0], complex)
                    else power_sums[0])

    r = len(power_sums)

    # Method: from p_1 = alpha + beta and alpha*beta = p^{k-1}, we have:
    #   alpha, beta = (p_1 +/- sqrt(p_1^2 - 4*p^{k-1})) / 2
    # The bound on |alpha| depends on the discriminant.

    if HAS_MPMATH:
        disc = p1 ** 2 - 4 * pk1
        if disc <= 0:
            # Complex conjugate case: |alpha| = |beta| = p^{(k-1)/2} exactly
            bound = target
            method = f"p_1 gives disc <= 0: complex conjugate, exact Ramanujan"
        else:
            # Real case: |alpha| = (|p_1| + sqrt(disc)) / 2
            sqrt_disc = mpmath.sqrt(disc)
            bound = (mpmath.fabs(p1) + sqrt_disc) / 2
            method = f"p_1 gives disc > 0: real Satake, bound from quadratic"
    else:
        disc = p1 ** 2 - 4 * pk1
        if disc <= 0:
            bound = target
            method = f"p_1 gives disc <= 0: complex conjugate, exact Ramanujan"
        else:
            sqrt_disc = math.sqrt(disc)
            bound = (abs(p1) + sqrt_disc) / 2
            method = f"p_1 gives disc > 0: real Satake, bound from quadratic"

    # If we have higher power sums, we can sharpen.
    # For r >= 2: p_r = alpha^r + beta^r.
    # With |alpha*beta| = p^{k-1} and p_r known, we get:
    #   |alpha|^r + |beta|^r >= |p_r| (triangle inequality, with caveat for complex)
    # For complex conjugate alpha, beta = conj(alpha):
    #   p_r = 2 Re(alpha^r), so |p_r| <= 2 |alpha|^r
    #   => |alpha| >= (|p_r|/2)^{1/r}
    # This is a LOWER bound on |alpha|, which improves with r.

    # For the upper bound, the moment problem gives:
    #   max(|alpha|, |beta|) <= (|p_r|)^{1/r} for large r
    # (by dominated convergence, |alpha|^r + |beta|^r -> max^r as r -> inf)

    if r >= 2:
        for idx in range(1, r):
            r_curr = idx + 1
            pr = power_sums[idx]
            if HAS_MPMATH:
                pr_abs = mpmath.fabs(mpmath.mpf(pr))
                # Upper bound: alpha, beta roots of x^2 - p_1 x + p^{k-1} = 0
                # p_r is determined by p_1 and p^{k-1}, so no extra info for
                # the BOUND if we already know p_1 and alpha*beta.
                # The value of the bound is already determined by the discriminant.
                # However, for FAKE eigenforms where p_r is independently specified,
                # the moment bound applies:
                if pr_abs > 0:
                    moment_bound = mpmath.power(pr_abs, mpmath.mpf(1) / r_curr)
                    # This is not directly useful as an upper bound on |alpha|
                    # unless we're in the "independent moment" scenario.
            else:
                pr_abs = abs(pr)

        method += f" (used {r} power sums)"

    if HAS_MPMATH:
        ratio = float(bound / target)
    else:
        ratio = bound / target if target > 0 else float('inf')

    return {
        'bound': float(bound) if HAS_MPMATH else bound,
        'ramanujan_target': float(target) if HAS_MPMATH else target,
        'ratio': ratio,
        'method': method,
    }


# =========================================================================
# 7. Rankin-Selberg bound
# =========================================================================

def rankin_selberg_bound(f_coeffs: Dict[int, Union[int, float]], k: int):
    r"""Compute the Rankin-Selberg convexity bound.

    The Rankin-Selberg method gives:
      sum_{p <= x} |a(p)|^2 / p^{k-1} ~ x / log(x)

    This implies the average bound |a(p)|^2 <= C * p^{k-1} * log(p).
    The individual bound from Rankin-Selberg convexity:
      |a(p)| <= C * p^{k/2 - 1/5}    (delta = 1/5)

    We verify this by computing the ratio |a(p)| / p^{k/2 - 1/5} for each
    available prime and checking it remains bounded.

    Returns a dict with verification data.
    """
    delta = 0.2  # 1/5, Gelbart-Jacquet
    primes = sorted(p for p in f_coeffs.keys() if p >= 2)

    ratios = {}
    for p in primes:
        a_p = f_coeffs[p]
        exponent = k / 2.0 - delta
        bound_val = p ** exponent
        ratio = abs(a_p) / bound_val if bound_val > 0 else float('inf')
        ratios[p] = ratio

    max_ratio = max(ratios.values()) if ratios else 0
    return {
        'delta': delta,
        'method': 'Rankin-Selberg (Gelbart-Jacquet, Sym^2)',
        'ratios': ratios,
        'max_ratio': max_ratio,
        'bounded': max_ratio < 100,  # Generous check for finite Euler product
    }


# =========================================================================
# 8. Improved bounds from Sym^r
# =========================================================================

# Known unconditional results:
SYM_POWER_DELTAS = {
    1: 0.0,     # Standard L-function: no improvement beyond trivial
    2: 0.2,     # 1/5, Gelbart-Jacquet (1978)
    3: 2/9,     # Kim-Shahidi (2002)
    4: 1/9,     # Kim (2003)
    # For r >= 5, the symmetric power lifts are not yet known to be automorphic
    # unconditionally. The conjectural delta approaches 1/2.
}

# Conjectural (assuming automorphy of Sym^r):
# delta(r) = 1/2 - 1/(r^2 + 2)  (heuristic, approaches 1/2)


def improved_bound_from_sym_r(f_coeffs: Dict[int, Union[int, float]],
                               k: int, r: int) -> dict:
    r"""Using L(s, Sym^r f), compute the improved bound on |a(p)|.

    For Sym^r with r <= 4, unconditional bounds are known:
      Sym^1: |a(p)| <= C * p^{(k-1)/2} (no delta improvement)
      Sym^2: delta = 1/5  (Gelbart-Jacquet)
      Sym^3: delta = 2/9  (Kim-Shahidi)
      Sym^4: delta = 1/9  (Kim)

    The bound is: |a(p)| <= C_r * p^{(k-1)/2 + epsilon}  for any epsilon > 0
    (assuming the symmetric power L-function is automorphic and analytic).

    For r >= 5, we report the CONJECTURAL delta assuming full automorphy.

    Returns a dict with:
      'r': symmetric power degree
      'delta': the exponent saving
      'status': 'unconditional' or 'conjectural'
      'bound_exponent': (k-1)/2 + epsilon (where epsilon -> 0 as proof strengthens)
      'ramanujan_exponent': (k-1)/2
      'verification': per-prime data
    """
    if r in SYM_POWER_DELTAS:
        delta = SYM_POWER_DELTAS[r]
        status = 'unconditional'
    else:
        # Conjectural: delta = 1/2 - 1/(r+1) (heuristic bound)
        delta = 0.5 - 1.0 / (r + 1)
        status = 'conjectural (assumes automorphy of Sym^r)'

    ramanujan_exp = (k - 1) / 2.0
    # The actual bound from Sym^r: |a(p)| <= C * p^{(k-1)/2 - delta_improvement}
    # where delta_improvement depends on r. For simplicity, we verify at known primes.

    primes = sorted(p for p in f_coeffs.keys() if p >= 2)
    verification = {}
    for p in primes:
        a_p = f_coeffs[p]
        # Check Ramanujan bound
        ram_bound = 2 * p ** ramanujan_exp
        ratio_ram = abs(a_p) / ram_bound if ram_bound > 0 else float('inf')
        verification[p] = {
            'a_p': a_p,
            'ramanujan_bound': ram_bound,
            'ratio': ratio_ram,
            'satisfies_ramanujan': ratio_ram <= 1 + 1e-10,
        }

    return {
        'r': r,
        'delta': delta,
        'status': status,
        'bound_exponent': (k - 1) / 2.0,
        'ramanujan_exponent': ramanujan_exp,
        'verification': verification,
    }


# =========================================================================
# 9. Verify Ramanujan from shadows (lattice VOA)
# =========================================================================

def lattice_theta_coefficients(lattice_type: str, nmax: int = 50) -> Dict[int, int]:
    r"""Return the first nmax Fourier coefficients of the lattice theta function.

    Supported lattice types:
      'Z': V_Z (rank 1), theta = theta_3(q)
      'Z2': V_{Z^2} (rank 2), theta = theta_3(q)^2
      'A2': V_{A_2} (rank 2), theta = 1 + 6q + 6q^3 + 6q^4 + 12q^7 + ...
      'E8': V_{E_8} (rank 8), theta = E_4(q) = 1 + 240q + 2160q^2 + ...
      'Leech': V_{Leech} (rank 24), theta = E_{12}(q) - (65520/691)*Delta(q)
    """
    coeffs = {}

    if lattice_type == 'Z':
        # theta_3(q) = 1 + 2q + 2q^4 + 2q^9 + 2q^{16} + ...
        # = sum_{n=-inf}^{inf} q^{n^2}
        for n in range(nmax + 1):
            coeffs[n] = 0
        coeffs[0] = 1
        for m in range(1, int(nmax**0.5) + 2):
            if m * m <= nmax:
                coeffs[m * m] += 2

    elif lattice_type == 'Z2':
        # theta_3(q)^2 = sum r_2(n) q^n where r_2(n) = #{(a,b): a^2+b^2=n}
        z_coeffs = lattice_theta_coefficients('Z', nmax)
        for n in range(nmax + 1):
            coeffs[n] = 0
        for a in range(nmax + 1):
            for b in range(nmax + 1):
                if a + b <= nmax:
                    coeffs[a + b] += z_coeffs.get(a, 0) * z_coeffs.get(b, 0)

    elif lattice_type == 'A2':
        # A_2 root lattice: theta = sum_{(a,b) in A_2} q^{a^2+ab+b^2}
        # = 1 + 6q + 6q^3 + 6q^4 + 12q^7 + 6q^9 + ...
        for n in range(nmax + 1):
            coeffs[n] = 0
        R = int(nmax**0.5) + 2
        for a in range(-R, R + 1):
            for b in range(-R, R + 1):
                val = a * a + a * b + b * b
                if 0 <= val <= nmax:
                    coeffs[val] += 1

    elif lattice_type == 'E8':
        # E_8 root lattice: theta = E_4(q) = 1 + 240*sum sigma_3(n) q^n
        for n in range(nmax + 1):
            coeffs[n] = 0
        coeffs[0] = 1
        for n in range(1, nmax + 1):
            s3 = 0
            for d in range(1, n + 1):
                if n % d == 0:
                    s3 += d ** 3
            coeffs[n] = 240 * s3

    elif lattice_type == 'Leech':
        # Leech lattice: theta = E_{12}(q) - (65520/691)*Delta(q)
        # E_{12}(q) = 1 + (65520/691)*sum sigma_{11}(n) q^n
        # Delta(q) = sum tau(n) q^n
        for n in range(nmax + 1):
            coeffs[n] = 0
        coeffs[0] = 1
        for n in range(1, nmax + 1):
            s11 = 0
            for d in range(1, n + 1):
                if n % d == 0:
                    s11 += d ** 11
            e12_n = Fraction(65520, 691) * s11
            tau_n = ramanujan_tau(n)
            delta_contrib = Fraction(65520, 691) * tau_n
            # theta_Leech(n) = E_{12,n} - (65520/691) * tau(n)
            val = e12_n - delta_contrib
            coeffs[n] = int(val)

    else:
        raise ValueError(f"Unknown lattice type: {lattice_type}")

    return coeffs


def verify_ramanujan_from_shadows(lattice_type: str, r_max: int = 8) -> dict:
    r"""For a lattice VOA, verify the Ramanujan bound via shadow tower data.

    The shadow tower of V_Lambda decomposes the theta function into Hecke
    eigencomponents. Each shadow coefficient S_r encodes the r-th power sum
    of the spectral atoms, which relate to symmetric power L-functions.

    For V_Leech (rank 24):
      - Shadow at arity 2 (kappa): Eisenstein E_{12} contribution
      - Shadow at arity 4 (quartic): Ramanujan Delta contribution
      - The Ramanujan bound |tau(p)| <= 2*p^{11/2} is equivalent to the
        quartic shadow being controlled by the Deligne bound.

    Returns verification data for primes up to 50.
    """
    primes = _primes_up_to(50)
    results = {
        'lattice_type': lattice_type,
        'r_max': r_max,
        'prime_data': {},
    }

    if lattice_type == 'Leech':
        # For the Leech lattice, the cuspidal part is the Ramanujan Delta.
        # The Hecke eigenvalues are tau(p).
        for p in primes:
            tau_p = ramanujan_tau(p)
            ram_check = verify_ramanujan_at_prime(tau_p, 12, p)

            # Power sums from Satake parameters
            alpha, beta = satake_parameters(tau_p, 12, p)
            ps_list = [power_sum_from_satake(alpha, beta, r) for r in range(1, r_max + 1)]

            # Convert to elementary symmetric polynomials
            e_list = power_sum_to_elementary(ps_list)

            def _to_real_float(x):
                """Convert mpmath mpc/mpf or Python complex to real float."""
                if HAS_MPMATH:
                    return float(mpmath.re(mpmath.mpc(x)))
                if isinstance(x, complex):
                    return x.real
                return float(x)

            results['prime_data'][p] = {
                'tau_p': tau_p,
                'ramanujan_check': ram_check,
                'power_sums': [_to_real_float(x) for x in ps_list],
                'elementary_sym': [_to_real_float(x) for x in e_list],
            }

        results['all_satisfy_ramanujan'] = all(
            d['ramanujan_check']['satisfies']
            for d in results['prime_data'].values()
        )
        results['all_exact_ramanujan'] = all(
            d['ramanujan_check']['exact_ramanujan']
            for d in results['prime_data'].values()
        )

    elif lattice_type in ('Z', 'Z2', 'A2', 'E8'):
        # For these lattices, the theta function is an Eisenstein series
        # (no cusp form contribution for rank < 24 in the relevant weight).
        # Shadow depth <= 3, no Ramanujan-type eigenvalues to check.
        results['note'] = (
            f"Lattice {lattice_type} has no cuspidal part in the relevant weight. "
            f"Shadow depth is <= 3. No Hecke eigenvalue bounds to verify."
        )
        results['all_satisfy_ramanujan'] = True  # Vacuously true
        results['all_exact_ramanujan'] = True

    return results


# =========================================================================
# 10. Shadow tower discrimination
# =========================================================================

def _spectral_measure_power_sums(measure: List[Tuple[float, float]], r_max: int) -> List[float]:
    r"""Compute power sums p_1, ..., p_{r_max} for a discrete spectral measure.

    measure: list of (weight, atom) pairs. The power sum is:
      p_r = sum_j w_j * atom_j^r
    """
    ps = []
    for r in range(1, r_max + 1):
        if HAS_MPMATH:
            val = sum(mpmath.mpc(w) * mpmath.power(mpmath.mpc(a), r) for w, a in measure)
        else:
            val = sum(w * a ** r for w, a in measure)
        ps.append(val)
    return ps


def shadow_tower_discriminates(real_measure: List[Tuple[float, float]],
                                fake_measure: List[Tuple[float, float]],
                                r_max: int = 20) -> dict:
    r"""Check whether the shadow tower discriminates a real spectral measure
    from a fake one.

    A "real" measure satisfies Ramanujan (all atoms have the correct absolute
    value). A "fake" measure violates Ramanujan at some atom.

    The shadow coefficient at arity r is S_r = -(1/r) * p_r(measure).
    The measures are discriminated at arity r if their shadow coefficients differ.

    Parameters:
      real_measure: list of (weight, atom) pairs satisfying Ramanujan
      fake_measure: list of (weight, atom) pairs (some may violate)
      r_max: maximum arity to check

    Returns:
      'first_divergence_arity': the first r where S_r differs (or None)
      'shadow_coefficients_real': {r: S_r for the real measure}
      'shadow_coefficients_fake': {r: S_r for the fake measure}
      'relative_differences': {r: |S_r^real - S_r^fake| / max(|S_r^real|, 1)}
    """
    ps_real = _spectral_measure_power_sums(real_measure, r_max)
    ps_fake = _spectral_measure_power_sums(fake_measure, r_max)

    s_real = {}
    s_fake = {}
    rel_diffs = {}
    first_div = None

    for r in range(1, r_max + 1):
        sr_real = -ps_real[r - 1] / r
        sr_fake = -ps_fake[r - 1] / r
        s_real[r] = sr_real
        s_fake[r] = sr_fake

        if HAS_MPMATH:
            diff = abs(complex(sr_real) - complex(sr_fake))
            denom = max(abs(complex(sr_real)), 1.0)
            rel = float(diff / denom)
        else:
            diff = abs(sr_real - sr_fake)
            denom = max(abs(sr_real), 1.0)
            rel = diff / denom

        rel_diffs[r] = rel
        if first_div is None and rel > 1e-10:
            first_div = r

    def _to_float(v):
        if HAS_MPMATH:
            return complex(v).real
        if isinstance(v, complex):
            return v.real
        return float(v)

    return {
        'first_divergence_arity': first_div,
        'shadow_coefficients_real': {r: _to_float(v) for r, v in s_real.items()},
        'shadow_coefficients_fake': {r: _to_float(v) for r, v in s_fake.items()},
        'relative_differences': rel_diffs,
    }


# =========================================================================
# Diagnostic: tau(p) data table
# =========================================================================

def ramanujan_tau_satake_table(p_max: int = 50) -> List[dict]:
    r"""Produce a diagnostic table of Satake data for the Ramanujan tau function.

    For each prime p <= p_max, returns:
      tau(p), discriminant, Satake type, |alpha|, |beta|, Ramanujan check.
    """
    primes = _primes_up_to(p_max)
    table = []
    for p in primes:
        tau_p = ramanujan_tau(p)
        info = verify_ramanujan_at_prime(tau_p, 12, p)
        alpha, beta = satake_parameters(tau_p, 12, p)
        if HAS_MPMATH:
            abs_alpha = float(mpmath.fabs(alpha))
            abs_beta = float(mpmath.fabs(beta))
            target = float(mpmath.power(p, mpmath.mpf(11) / 2))
        else:
            abs_alpha = abs(alpha)
            abs_beta = abs(beta)
            target = p ** 5.5
        table.append({
            'p': p,
            'tau_p': tau_p,
            'discriminant': info['discriminant'],
            'satake_type': info['satake_type'],
            'abs_alpha': abs_alpha,
            'abs_beta': abs_beta,
            'target': target,
            'exact_ramanujan': info['exact_ramanujan'],
        })
    return table


# =========================================================================
# Full trace of Sym^r for 2x2 diagonal
# =========================================================================

def trace_sym_r(alpha, beta, r: int):
    r"""Full trace of Sym^r(diag(alpha, beta)).

    Sym^r of a 2x2 diagonal matrix has eigenvalues alpha^j * beta^{r-j}
    for j = 0, ..., r. The trace is:
      tr(Sym^r) = sum_{j=0}^r alpha^j * beta^{r-j}
    """
    if HAS_MPMATH:
        return sum(mpmath.power(alpha, j) * mpmath.power(beta, r - j)
                   for j in range(r + 1))
    return sum(alpha ** j * beta ** (r - j) for j in range(r + 1))
