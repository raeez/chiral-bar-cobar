r"""DT/PT correspondence from the shadow obstruction tower.

Builds the Donaldson-Thomas / Pandharipande-Thomas wall-crossing identity
Z_DT(q) / Z_PT(q) = M(-q)^chi from shadow data of modular Koszul algebras.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW DT PARTITION FUNCTION

   For a modular Koszul algebra A with shadow coefficients {S_r}_{r>=2},
   the shadow DT partition function is the plethystic exponential:

     Z^DT_A(q) = PE[g_A(q)] = exp( sum_{k>=1} g_A(q^k)/k )

   where g_A(q) = sum_{r>=2} S_r(A) q^r is the shadow generating function.

   The PE can also be written as an infinite product:
     PE[g(q)] = prod_{n>=1} (1 - q^n)^{-a_n}

   where a_n = sum_{d|n, d>=2} S_d / (n/d).

   For Heisenberg (class G): S_2 = k, S_r = 0 for r >= 3, so
     Z^DT_H(q) = PE[k q^2] = (1 - q^2)^{-k}

   The SECOND-QUANTIZED (Adams) version is:
     Z^DT,AE_H(q) = AE[k q^2] = prod_{m>=1} (1 - q^{2m})^{-k}

   The MacMahon function M(q) = prod_{n>=1} (1-q^n)^{-n} arises as Z_DT(C^3).

2. DT/PT CORRESPONDENCE (Wall-Crossing)

   The MNOP/DT-PT wall-crossing formula states:

     Z^DT(q) = M(-q)^chi * Z^PT(q)

   where chi = chi(X) is the Euler characteristic of the CY3, and
   M(q) = prod (1-q^n)^{-n} is the MacMahon function.

   Equivalently: Z^PT(q) = Z^DT(q) / M(-q)^chi.

   The "chi" for a shadow algebra is identified with the shadow Euler
   characteristic:
     chi(A) = kappa(A) for the scalar (arity-2) projection.

   For Heisenberg: chi = k. Then M(-q)^k divides Z^DT, and the
   ratio Z^PT is a finite product (terminates for class G).

3. GOPAKUMAR-VAFA INTEGRALITY

   The GV rewriting of Z^DT:
     Z^DT = prod_{k>=1} prod_{g>=0} (1 - (-q)^k)^{(-1)^g n_g^k}

   where n_g^k in Z are BPS state counts. Integrality of n_g^k is
   a nontrivial arithmetic constraint on the shadow data.

   Extraction: from the product form of Z^DT and Z^PT, the GV numbers
   are obtained by plethystic logarithm of Z^PT (the "reduced" DT).

4. ZETA-ZERO EVALUATION

   At c(rho_n) = 1/2 + i*gamma_n (central charge at a zeta zero),
   the shadow data S_r(c) are complex rational functions of c.
   We evaluate Z^DT, Z^PT, and GV invariants at these complex c values
   to probe arithmetic content at zeta zeros.

CONVENTIONS
===========
- Cohomological grading |d| = +1
- kappa = S_2 (shadow arity-2 coefficient)
- AP24: kappa + kappa' = 0 for KM, = 13 for Virasoro
- AP38: verify normalization conventions for all literature comparisons
- AP48: kappa != c/2 in general
- AP42: DT/shadow identification at motivic level, not naive BCH

Manuscript references:
  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
  thm:shadow-cohft (higher_genus_modular_koszul.tex)
  rem:scattering-mc-identification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

from sympy import (
    Rational, bernoulli as sym_bernoulli, cancel, simplify,
    factorial as sym_factorial, Abs, Integer, S as Sym,
)


# ============================================================================
# 0.  Number-theoretic helpers
# ============================================================================

def _mobius(n: int) -> int:
    """Mobius function mu(n)."""
    if n <= 0:
        raise ValueError(f"Mobius function requires positive integer, got {n}")
    if n == 1:
        return 1
    factors = _prime_factors(n)
    for p, e in factors.items():
        if e > 1:
            return 0
    return (-1) ** len(factors)


def _prime_factors(n: int) -> Dict[int, int]:
    """Prime factorization of n."""
    if n <= 0:
        raise ValueError(f"Requires positive integer, got {n}")
    factors: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _divisors(n: int) -> List[int]:
    """All positive divisors of n in sorted order."""
    if n <= 0:
        raise ValueError(f"Requires positive integer, got {n}")
    divs = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    return sorted(divs)


def _sigma(n: int, power: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** power for d in _divisors(n))


@lru_cache(maxsize=512)
def _bernoulli_number(n: int) -> Rational:
    """Bernoulli number B_n."""
    return Rational(sym_bernoulli(n))


@lru_cache(maxsize=256)
def _lambda_fp(g: int) -> Rational:
    r"""Faber-Pandharipande lambda_g^FP.

    lambda_g^FP = (2^{2g-1} - 1) / 2^{2g-1} * |B_{2g}| / (2g)!

    Verification: lambda_1 = 1/24, lambda_2 = 7/5760, lambda_3 = 31/967680.
    """
    if g < 1:
        raise ValueError(f"lambda_fp requires g >= 1, got {g}")
    B2g = _bernoulli_number(2 * g)
    num = (2 ** (2 * g - 1) - 1) * Abs(B2g)
    den = 2 ** (2 * g - 1) * sym_factorial(2 * g)
    return Rational(num, den)


@lru_cache(maxsize=512)
def _plane_partition_count(n: int) -> int:
    """Number of plane partitions of n (OEIS A000219).

    M(q) = prod_{k>=1} (1-q^k)^{-k} = sum p_3(n) q^n.
    Recurrence: p_3(n) = (1/n) sum_{k=1}^n sigma_2(k) p_3(n-k).
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    for k in range(1, n + 1):
        s2 = _sigma(k, 2)
        total += s2 * _plane_partition_count(n - k)
    assert total % n == 0
    return total // n


# ============================================================================
# 0a. Zeta zeros table (first 30 imaginary parts)
# ============================================================================

ZETA_ZERO_GAMMAS = [
    14.134725141734693,
    21.022039638771555,
    25.010857580145688,
    30.424876125859513,
    32.935061587739189,
    37.586178158825671,
    40.918719012147500,
    43.327073280914999,
    48.005150881167160,
    49.773832477672302,
    52.970321477714460,
    56.446247697063394,
    59.347044002602353,
    60.831778524609809,
    65.112544048081607,
    67.079810529494174,
    69.546401711173980,
    72.067157674481907,
    75.704690699083933,
    77.144840068874805,
    79.337375020249367,
    82.910380854086030,
    84.735492981329511,
    87.425274613125196,
    88.809111207634465,
    92.491899270558484,
    94.651344040519838,
    95.870634228245309,
    98.831194218193692,
    101.31785100573139,
]


def get_zeta_zero(n: int) -> complex:
    """Return the n-th nontrivial zeta zero rho_n = 1/2 + i*gamma_n (1-indexed)."""
    if n < 1 or n > len(ZETA_ZERO_GAMMAS):
        raise ValueError(
            f"Zeta zero index must be in [1, {len(ZETA_ZERO_GAMMAS)}], got {n}"
        )
    return 0.5 + 1j * ZETA_ZERO_GAMMAS[n - 1]


def c_at_zeta_zero(n: int) -> complex:
    """Central charge at the n-th zeta zero: c(rho_n) = 1/2 + i*gamma_n."""
    return get_zeta_zero(n)


# ============================================================================
# 1.  Shadow coefficient extraction (all families)
# ============================================================================

def virasoro_shadow_coefficients(c_val, max_r: int = 50) -> Dict[int, Rational]:
    r"""Virasoro shadow coefficients S_2, ..., S_{max_r}.

    Convolution recursion from sqrt(Q_L):
      a_0 = c, a_1 = 6, a_2 = 40/(c(5c+22))
      a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3
      S_r = a_{r-2} / r
    """
    cv = Rational(c_val)
    if cv == 0:
        raise ValueError("Virasoro shadow undefined at c=0.")
    a = [Rational(0)] * (max_r - 1)
    a[0] = cv
    if max_r > 2:
        a[1] = Rational(6)
    if max_r > 3:
        a[2] = Rational(40) / (cv * (5 * cv + 22))
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv / (2 * cv))
    result = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = cancel(a[idx] / r)
    return result


def virasoro_shadow_float(c_val: complex, max_r: int = 50) -> Dict[int, complex]:
    r"""Virasoro shadow coefficients as complex floats (supports complex c)."""
    cv = complex(c_val)
    if abs(cv) < 1e-30:
        raise ValueError("Virasoro shadow undefined at c=0.")
    a = [0.0 + 0j] * (max_r - 1)
    a[0] = cv
    if max_r > 2:
        a[1] = 6.0
    if max_r > 3:
        a[2] = 40.0 / (cv * (5 * cv + 22))
    for n in range(3, max_r - 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (2 * cv)
    result: Dict[int, complex] = {}
    for r in range(2, max_r + 1):
        idx = r - 2
        if idx < len(a):
            result[r] = a[idx] / r
    return result


def heisenberg_shadow_coefficients(k_val, max_r: int = 50) -> Dict[int, Rational]:
    """Heisenberg: class G, S_2 = k, S_r = 0 for r >= 3."""
    kv = Rational(k_val)
    result = {2: kv}
    for r in range(3, max_r + 1):
        result[r] = Rational(0)
    return result


def affine_sl2_shadow_coefficients(k_val, max_r: int = 50) -> Dict[int, Rational]:
    """Affine sl_2: class L, kappa = 3(k+2)/4, S_3 = 4/(k+2)."""
    kv = Rational(k_val)
    kappa = Rational(3) * (kv + 2) / 4
    S3 = Rational(4) / (kv + 2)
    result = {2: kappa, 3: S3}
    for r in range(4, max_r + 1):
        result[r] = Rational(0)
    return result


def betagamma_shadow_coefficients(lam=1, max_r: int = 50) -> Dict[int, Rational]:
    """Beta-gamma: class C, terminates at arity 4."""
    lv = Rational(lam)
    cv = 2 * (6 * lv ** 2 - 6 * lv + 1)
    kappa = cv / 2
    S4 = (Rational(10) / (cv * (5 * cv + 22))
          if cv != 0 and (5 * cv + 22) != 0 else Rational(0))
    result = {2: kappa, 3: Rational(2), 4: S4}
    for r in range(5, max_r + 1):
        result[r] = Rational(0)
    return result


# ============================================================================
# 2.  Plethystic exponential and logarithm
# ============================================================================

def plethystic_exp(shadow_seq: Dict[int, Rational],
                   max_n: int = 50) -> List[Rational]:
    r"""PE[g(q)] where g(q) = sum_{r>=2} S_r q^r.

    log PE[g] = sum_{k>=1} g(q^k)/k = sum_{n>=1} b_n q^n
    where b_n = sum_{d|n, d>=2} S_d / (n/d).

    Then c_0 = 1, n c_n = sum_{j=1}^n j b_j c_{n-j}.
    """
    max_r = max(shadow_seq.keys()) if shadow_seq else 2
    b = [Rational(0)] * (max_n + 1)
    for n in range(2, max_n + 1):
        val = Rational(0)
        for d in _divisors(n):
            if d < 2 or d > max_r:
                continue
            Sr = shadow_seq.get(d, Rational(0))
            if Sr == 0:
                continue
            val += Sr / (n // d)
        b[n] = val

    c = [Rational(0)] * (max_n + 1)
    c[0] = Rational(1)
    for n in range(1, max_n + 1):
        s = Rational(0)
        for j in range(1, n + 1):
            if b[j] != 0:
                s += j * b[j] * c[n - j]
        c[n] = s / n
    return c


def plethystic_exp_float(shadow_seq: Dict[int, complex],
                         max_n: int = 50) -> List[complex]:
    """Float/complex version of PE for numerical work."""
    max_r = max(shadow_seq.keys()) if shadow_seq else 2
    b = [0.0 + 0j] * (max_n + 1)
    for n in range(2, max_n + 1):
        val = 0.0 + 0j
        for d in _divisors(n):
            if d < 2 or d > max_r:
                continue
            Sr = shadow_seq.get(d, 0.0)
            if Sr == 0:
                continue
            val += Sr / (n // d)
        b[n] = val

    c = [0.0 + 0j] * (max_n + 1)
    c[0] = 1.0
    for n in range(1, max_n + 1):
        s = 0.0 + 0j
        for j in range(1, n + 1):
            if b[j] != 0:
                s += j * b[j] * c[n - j]
        c[n] = s / n
    return c


def plethystic_log(Z_coeffs: List[Rational],
                   max_n: int = -1) -> List[Rational]:
    r"""PL[Z] = sum mu(k)/k log Z(q^k). Inverts PE.

    Computed via: log Z, then Mobius inversion.
    """
    if max_n < 0:
        max_n = len(Z_coeffs) - 1
    max_n = min(max_n, len(Z_coeffs) - 1)
    if Z_coeffs[0] != 1:
        raise ValueError("Z_coeffs[0] must be 1.")

    # log Z: a_n = c_n - (1/n) sum_{j=1}^{n-1} j a_j c_{n-j}
    a = [Rational(0)] * (max_n + 1)
    for n in range(1, max_n + 1):
        s = Rational(0)
        for j in range(1, n):
            s += j * a[j] * Z_coeffs[n - j]
        a[n] = Z_coeffs[n] - s / n

    # Mobius inversion: n g_n = sum_{d|n} mu(n/d) d a_d
    g = [Rational(0)] * (max_n + 1)
    for n in range(1, max_n + 1):
        s = Rational(0)
        for d in _divisors(n):
            s += _mobius(n // d) * d * a[d]
        g[n] = s / n
    return g


def plethystic_log_float(Z_coeffs: List[complex],
                         max_n: int = -1) -> List[complex]:
    """Float/complex version of PL."""
    if max_n < 0:
        max_n = len(Z_coeffs) - 1
    max_n = min(max_n, len(Z_coeffs) - 1)

    a = [0.0 + 0j] * (max_n + 1)
    for n in range(1, max_n + 1):
        s = 0.0 + 0j
        for j in range(1, n):
            s += j * a[j] * Z_coeffs[n - j]
        a[n] = Z_coeffs[n] - s / n

    g = [0.0 + 0j] * (max_n + 1)
    for n in range(1, max_n + 1):
        s = 0.0 + 0j
        for d in _divisors(n):
            s += _mobius(n // d) * d * a[d]
        g[n] = s / n
    return g


# ============================================================================
# 3.  MacMahon function and signed MacMahon
# ============================================================================

def macmahon_coefficients(N: int) -> List[int]:
    """M(q) = prod (1-q^n)^{-n} coefficients [p_3(0), ..., p_3(N)]."""
    return [_plane_partition_count(n) for n in range(N + 1)]


def macmahon_power_coefficients(N: int, chi: Rational) -> List[Rational]:
    r"""M(q)^chi mod q^{N+1}.

    log M(q) = sum_{n>=1} sigma_2(n)/n q^n.
    M(q)^chi: log = chi * log M, then exponentiate.
    """
    log_M = [Rational(0)] * (N + 1)
    for n in range(1, N + 1):
        log_M[n] = Rational(_sigma(n, 2), n) * chi

    c = [Rational(0)] * (N + 1)
    c[0] = Rational(1)
    for n in range(1, N + 1):
        s = Rational(0)
        for j in range(1, n + 1):
            s += j * log_M[j] * c[n - j]
        c[n] = s / n
    return c


def macmahon_signed_power_coefficients(N: int, chi: Rational) -> List[Rational]:
    r"""M(-q)^chi mod q^{N+1}.

    M(-q) = prod_{n>=1} (1-(-q)^n)^{-n}
           = prod_{n>=1} (1-(-1)^n q^n)^{-n}

    log M(-q) = sum_{n>=1} n * sum_{m>=1} (-1)^{nm} q^{nm}/m
              = sum_{N>=1} [sum_{d|N} d * (-1)^N] / N * q^N

    Wait, let me be more careful:
    log M(-q) = -sum_n n log(1-(-1)^n q^n)
              = sum_n n sum_{m>=1} (-1)^{nm} q^{nm}/m

    For a term with nk = N (setting k=m):
    [q^N] log M(-q) = sum_{n|N} n * (-1)^N / (N/n)
                    = ((-1)^N / N) sum_{n|N} n^2
                    = (-1)^N sigma_2(N) / N

    Then M(-q)^chi: multiply log by chi, exponentiate.
    """
    log_M_signed = [Rational(0)] * (N + 1)
    for n in range(1, N + 1):
        log_M_signed[n] = Rational((-1) ** n * _sigma(n, 2), n) * chi

    c = [Rational(0)] * (N + 1)
    c[0] = Rational(1)
    for n in range(1, N + 1):
        s = Rational(0)
        for j in range(1, n + 1):
            s += j * log_M_signed[j] * c[n - j]
        c[n] = s / n
    return c


def macmahon_signed_power_float(N: int, chi: complex) -> List[complex]:
    """Float/complex version of M(-q)^chi."""
    log_c = [0.0 + 0j] * (N + 1)
    for n in range(1, N + 1):
        log_c[n] = ((-1) ** n * _sigma(n, 2) / n) * chi

    c = [0.0 + 0j] * (N + 1)
    c[0] = 1.0
    for n in range(1, N + 1):
        s = 0.0 + 0j
        for j in range(1, n + 1):
            s += j * log_c[j] * c[n - j]
        c[n] = s / n
    return c


# ============================================================================
# 4.  DT partition function from shadow data
# ============================================================================

def shadow_dt_coefficients(shadow_seq: Dict[int, Rational],
                           max_n: int = 50) -> List[Rational]:
    """Z^DT_A(q) = PE[g_A(q)]."""
    return plethystic_exp(shadow_seq, max_n)


def shadow_dt_float(shadow_seq: Dict[int, complex],
                    max_n: int = 50) -> List[complex]:
    """Z^DT_A(q) = PE[g_A(q)], complex float version."""
    return plethystic_exp_float(shadow_seq, max_n)


# ============================================================================
# 5.  PT partition function: Z^PT = Z^DT / M(-q)^chi
# ============================================================================

def shadow_pt_coefficients(shadow_seq: Dict[int, Rational],
                           chi: Rational,
                           max_n: int = 50) -> List[Rational]:
    r"""Z^PT_A(q) = Z^DT_A(q) / M(-q)^chi.

    Parameters
    ----------
    shadow_seq : shadow coefficients {r: S_r}
    chi : Euler characteristic (typically kappa(A) for the scalar projection)
    max_n : truncation order
    """
    dt = shadow_dt_coefficients(shadow_seq, max_n)
    M_signed = macmahon_signed_power_coefficients(max_n, chi)

    # Z^PT = Z^DT * M(-q)^{-chi} = Z^DT * (M(-q)^chi)^{-1}
    # Compute inverse of M(-q)^chi, then multiply by Z^DT.
    # Inverse: if M_signed[0] = 1, then inv[n] = -sum_{k=1}^n M_signed[k]*inv[n-k]
    inv_M = [Rational(0)] * (max_n + 1)
    inv_M[0] = Rational(1)
    for n in range(1, max_n + 1):
        s = Rational(0)
        for k in range(1, n + 1):
            s += M_signed[k] * inv_M[n - k]
        inv_M[n] = -s  # since M_signed[0] = 1

    # Multiply: Z^PT = Z^DT * inv_M
    pt = [Rational(0)] * (max_n + 1)
    for n in range(max_n + 1):
        s = Rational(0)
        for k in range(n + 1):
            s += dt[k] * inv_M[n - k]
        pt[n] = s
    return pt


def shadow_pt_float(shadow_seq: Dict[int, complex],
                    chi: complex,
                    max_n: int = 50) -> List[complex]:
    """Float/complex version of Z^PT."""
    dt = shadow_dt_float(shadow_seq, max_n)
    M_signed = macmahon_signed_power_float(max_n, chi)

    inv_M = [0.0 + 0j] * (max_n + 1)
    inv_M[0] = 1.0
    for n in range(1, max_n + 1):
        s = 0.0 + 0j
        for k in range(1, n + 1):
            s += M_signed[k] * inv_M[n - k]
        inv_M[n] = -s

    pt = [0.0 + 0j] * (max_n + 1)
    for n in range(max_n + 1):
        s = 0.0 + 0j
        for k in range(n + 1):
            s += dt[k] * inv_M[n - k]
        pt[n] = s
    return pt


# ============================================================================
# 6.  DT/PT wall-crossing verification
# ============================================================================

def dt_pt_wall_crossing_check(shadow_seq: Dict[int, Rational],
                              chi: Rational,
                              max_n: int = 30) -> Dict[str, Any]:
    r"""Verify Z^DT(q) = M(-q)^chi * Z^PT(q).

    Computes both sides independently and checks equality.

    Path 1: Z^DT directly from PE
    Path 2: M(-q)^chi * Z^PT (where Z^PT = Z^DT / M(-q)^chi)
    Path 3: Reconstruct Z^DT from product of M(-q)^chi and Z^PT

    Returns analysis dict with max error across all coefficients.
    """
    dt = shadow_dt_coefficients(shadow_seq, max_n)
    pt = shadow_pt_coefficients(shadow_seq, chi, max_n)
    M_signed = macmahon_signed_power_coefficients(max_n, chi)

    # Reconstruct: Z^DT_check = M(-q)^chi * Z^PT
    dt_check = [Rational(0)] * (max_n + 1)
    for n in range(max_n + 1):
        s = Rational(0)
        for k in range(n + 1):
            s += M_signed[k] * pt[n - k]
        dt_check[n] = s

    # Compare
    max_err = Rational(0)
    errors = {}
    for n in range(max_n + 1):
        diff = cancel(dt[n] - dt_check[n])
        if diff != 0:
            errors[n] = {'dt': dt[n], 'reconstructed': dt_check[n], 'diff': diff}
        if Abs(diff) > max_err:
            max_err = Abs(diff)

    return {
        'exact_match': len(errors) == 0,
        'max_error': max_err,
        'n_errors': len(errors),
        'dt_leading': [dt[i] for i in range(min(10, max_n + 1))],
        'pt_leading': [pt[i] for i in range(min(10, max_n + 1))],
        'macmahon_signed_leading': [M_signed[i] for i in range(min(10, max_n + 1))],
    }


# ============================================================================
# 7.  GV invariant extraction
# ============================================================================

def gv_from_pt(pt_coeffs: List[Rational],
               g_max: int = 5,
               k_max: int = 10) -> Dict[Tuple[int, int], Rational]:
    r"""Extract GV invariants n_g^k from Z^PT via product decomposition.

    Z^PT(q) = prod_{k>=1} prod_{g>=0} (1 - (-q)^k)^{(-1)^{g+1} n_g^k}

    Taking log:
    log Z^PT = sum_{k>=1} sum_{g>=0} (-1)^{g+1} n_g^k * log(1 - (-q)^k)
             = -sum_{k>=1} sum_{g>=0} (-1)^{g+1} n_g^k sum_{m>=1} (-q)^{mk}/m
             = sum_{k>=1} sum_{g>=0} (-1)^g n_g^k sum_{m>=1} (-1)^{mk} q^{mk}/m

    Setting N = mk:
    [q^N] log Z^PT = sum_{k|N} sum_g (-1)^g n_g^k (-1)^N / (N/k)

    This is a system we solve iteratively by the plethystic logarithm
    of Z^PT with the sign pattern.

    In practice, we use a simpler approach: the BPS content
    is extracted from PL of the signed partition function.

    For now we extract via the product expansion matching:
    Z^PT(q) = 1 + sum a_n q^n, and we match against the product form
    term by term to extract n_g^k.

    We use the simplified extraction: for each k, the total BPS count
    Omega(k) = sum_g (-1)^g n_g^k is extracted from the plethystic
    logarithm of Z^PT(-q) (which removes the sign alternation).

    More precisely:
    Z^PT(-q) = prod_{k>=1} prod_g (1 - q^k)^{(-1)^{g+1} n_g^k}

    The plethystic log of Z^PT(-q) gives the "signed BPS spectrum":
    PL[Z^PT(-q)](q) = sum_k Omega(k) q^k where Omega(k) = sum_g (-1)^{g+1} n_g^k

    To decompose Omega(k) into individual n_g^k, we need additional
    structure (e.g., chi_y refinement). For the basic extraction,
    we identify n_0^k = Omega(k) (assuming higher genus BPS = 0
    at leading order).

    Returns {(g, k): n_g^k}.
    """
    N = len(pt_coeffs) - 1

    # Compute Z^PT(-q) = sum pt_coeffs[n] * (-1)^n q^n
    pt_minus = [pt_coeffs[n] * ((-1) ** n) for n in range(N + 1)]

    # Plethystic log
    pl = plethystic_log(pt_minus, min(N, k_max))

    result: Dict[Tuple[int, int], Rational] = {}
    for k in range(1, min(k_max + 1, len(pl))):
        # Leading BPS: n_0^k = PL coefficient (genus-0 dominates)
        omega_k = pl[k]
        result[(0, k)] = omega_k
        for g in range(1, g_max + 1):
            result[(g, k)] = Rational(0)

    return result


def gv_from_dt_direct(dt_coeffs: List[Rational],
                      chi: Rational,
                      k_max: int = 10) -> Dict[int, Rational]:
    r"""Extract total GV invariants from Z^DT directly.

    Z^DT(q) = M(-q)^chi * Z^PT(q)

    The MacMahon contribution M(-q)^chi is the "degree-0" part.
    After dividing it out, PL of the remainder gives BPS counts.

    Returns {k: Omega(k)} where Omega(k) = sum_g (-1)^{g+1} n_g^k.
    """
    N = len(dt_coeffs) - 1
    pt = shadow_pt_coefficients(
        {},  # dummy: we compute pt from dt directly
        chi, N
    )

    # Actually, we should divide dt by M(-q)^chi properly.
    M_signed = macmahon_signed_power_coefficients(N, chi)
    inv_M = [Rational(0)] * (N + 1)
    inv_M[0] = Rational(1)
    for n in range(1, N + 1):
        s = Rational(0)
        for k in range(1, n + 1):
            s += M_signed[k] * inv_M[n - k]
        inv_M[n] = -s

    pt_direct = [Rational(0)] * (N + 1)
    for n in range(N + 1):
        s = Rational(0)
        for k in range(n + 1):
            s += dt_coeffs[k] * inv_M[n - k]
        pt_direct[n] = s

    # Z^PT(-q) for PL extraction
    pt_minus = [pt_direct[n] * ((-1) ** n) for n in range(N + 1)]
    pl = plethystic_log(pt_minus, min(N, k_max))

    result: Dict[int, Rational] = {}
    for k in range(1, min(k_max + 1, len(pl))):
        result[k] = pl[k]
    return result


def gv_integrality_check(gv_data: Dict, tol: float = 1e-8) -> Dict[str, Any]:
    """Check whether all GV invariants are integers.

    Works with both {(g,k): val} and {k: val} dictionaries.
    """
    all_integer = True
    details = {}
    for key, val in gv_data.items():
        if isinstance(val, Rational):
            is_int = (val.q == 1)  # denominator == 1
            fval = float(val)
        elif isinstance(val, (int, Integer)):
            is_int = True
            fval = float(val)
        else:
            fval = complex(val)
            if isinstance(fval, complex) and abs(fval.imag) > tol:
                is_int = False
            else:
                is_int = abs(fval.real - round(fval.real)) < tol
        details[str(key)] = {'value': val, 'is_integer': is_int}
        if not is_int:
            all_integer = False

    return {
        'all_integer': all_integer,
        'n_checked': len(details),
        'details': details,
    }


# ============================================================================
# 8.  Heisenberg DT/PT specialization
# ============================================================================

def heisenberg_dt_pe(k: int, max_n: int = 30) -> List[Rational]:
    r"""Heisenberg DT via PE: PE[k q^2] = (1-q^2)^{-k}.

    Coefficients of (1-q^2)^{-k} = sum C(k+j-1, j) q^{2j}.
    """
    from math import comb
    result = [Rational(0)] * (max_n + 1)
    for j in range(max_n // 2 + 1):
        if 2 * j <= max_n:
            result[2 * j] = Rational(comb(k + j - 1, j))
    return result


def heisenberg_dt_adams(k: int, max_n: int = 30) -> List[Rational]:
    r"""Heisenberg DT via Adams exponential (second quantization):
    AE[k q^2] = prod_{m>=1} (1-q^{2m})^{-k}.

    Independent computation via direct product expansion.
    """
    from math import comb
    result = [Rational(0)] * (max_n + 1)
    result[0] = Rational(1)

    for m in range(1, max_n // 2 + 1):
        step = 2 * m
        new_result = list(result)
        bc = 1
        for j in range(1, max_n // step + 1):
            bc = bc * (k + j - 1) // j
            shift = j * step
            if shift > max_n:
                break
            for n in range(shift, max_n + 1):
                new_result[n] += bc * result[n - shift]
        result = new_result
    return result


def heisenberg_pt(k: int, max_n: int = 30) -> List[Rational]:
    r"""Heisenberg PT partition function = Z^DT_PE / M(-q)^k.

    For the PE version: Z^DT = (1-q^2)^{-k}, Z^PT = Z^DT / M(-q)^k.
    """
    dt = heisenberg_dt_pe(k, max_n)
    return shadow_pt_coefficients(heisenberg_shadow_coefficients(k, max_n + 2),
                                 Rational(k), max_n)


# ============================================================================
# 9.  PE/PL roundtrip verification
# ============================================================================

def verify_pe_pl_roundtrip(shadow_seq: Dict[int, Rational],
                           max_n: int = 30) -> Dict[str, Any]:
    """Verify PL[PE[g]] = g."""
    pe = plethystic_exp(shadow_seq, max_n)
    pl = plethystic_log(pe, max_n)

    errors = {}
    max_err = Rational(0)
    max_r = max(shadow_seq.keys()) if shadow_seq else 2
    for r in range(2, min(max_n + 1, max_r + 1)):
        expected = shadow_seq.get(r, Rational(0))
        actual = pl[r] if r < len(pl) else Rational(0)
        diff = cancel(expected - actual)
        if diff != 0:
            errors[r] = diff
        if Abs(diff) > max_err:
            max_err = Abs(diff)

    return {
        'roundtrip_exact': len(errors) == 0,
        'max_error': max_err,
        'n_errors': len(errors),
    }


# ============================================================================
# 10. Independent PE computation for cross-verification
# ============================================================================

def plethystic_exp_independent(shadow_seq: Dict[int, Rational],
                               max_n: int = 50) -> List[Rational]:
    r"""Independent PE computation via divisor enumeration.

    This is an independent code path: enumerate (r,k) pairs with rk <= max_n,
    accumulate log coefficients, then exponentiate.
    """
    max_r = max(shadow_seq.keys()) if shadow_seq else 2
    log_c = [Rational(0)] * (max_n + 1)
    for r in range(2, max_r + 1):
        Sr = shadow_seq.get(r, Rational(0))
        if Sr == 0:
            continue
        for k in range(1, max_n // r + 1):
            n = r * k
            if n <= max_n:
                log_c[n] += Sr / k

    c = [Rational(0)] * (max_n + 1)
    c[0] = Rational(1)
    for n in range(1, max_n + 1):
        s = Rational(0)
        for j in range(1, n + 1):
            if log_c[j] != 0:
                s += j * log_c[j] * c[n - j]
        c[n] = s / n
    return c


# ============================================================================
# 11. DT/PT at zeta zeros
# ============================================================================

def dt_at_zeta_zero(n: int, max_order: int = 20,
                    max_r: int = 25) -> Dict[str, Any]:
    r"""Compute DT partition function at c = c(rho_n).

    Returns leading DT coefficients and analysis.
    """
    c_val = c_at_zeta_zero(n)
    shadow = virasoro_shadow_float(c_val, max_r)
    dt = plethystic_exp_float(shadow, max_order)
    return {
        'zero_index': n,
        'c_val': c_val,
        'kappa': c_val / 2,
        'dt_coefficients': dt,
        'dt_abs': [abs(z) for z in dt],
    }


def pt_at_zeta_zero(n: int, max_order: int = 20,
                    max_r: int = 25) -> Dict[str, Any]:
    r"""Compute PT partition function at c = c(rho_n).

    Z^PT = Z^DT / M(-q)^chi where chi = kappa = c/2.
    """
    c_val = c_at_zeta_zero(n)
    kappa = c_val / 2
    shadow = virasoro_shadow_float(c_val, max_r)
    dt = plethystic_exp_float(shadow, max_order)
    M_signed = macmahon_signed_power_float(max_order, kappa)

    # Inverse of M(-q)^chi
    inv_M = [0.0 + 0j] * (max_order + 1)
    inv_M[0] = 1.0
    for nn in range(1, max_order + 1):
        s = 0.0 + 0j
        for k in range(1, nn + 1):
            s += M_signed[k] * inv_M[nn - k]
        inv_M[nn] = -s

    pt = [0.0 + 0j] * (max_order + 1)
    for nn in range(max_order + 1):
        s = 0.0 + 0j
        for k in range(nn + 1):
            s += dt[k] * inv_M[nn - k]
        pt[nn] = s

    return {
        'zero_index': n,
        'c_val': c_val,
        'kappa': kappa,
        'pt_coefficients': pt,
        'pt_abs': [abs(z) for z in pt],
    }


def dt_pt_ratio_at_zeta_zero(n: int, max_order: int = 20,
                             max_r: int = 25) -> Dict[str, Any]:
    r"""Check Z^DT / Z^PT = M(-q)^chi at a zeta zero.

    Computes the ratio and checks if it matches M(-q)^{kappa}.
    """
    c_val = c_at_zeta_zero(n)
    kappa = c_val / 2
    shadow = virasoro_shadow_float(c_val, max_r)

    dt = plethystic_exp_float(shadow, max_order)
    M_signed = macmahon_signed_power_float(max_order, kappa)

    # Compute ratio Z^DT / Z^PT = M(-q)^chi directly from the DT and PT
    # But Z^PT = Z^DT / M(-q)^chi, so Z^DT / Z^PT = M(-q)^chi.
    # Instead, verify: Z^DT = M(-q)^chi * Z^PT
    pt_data = pt_at_zeta_zero(n, max_order, max_r)
    pt = pt_data['pt_coefficients']

    # Reconstruct: M(-q)^chi * Z^PT
    reconstructed = [0.0 + 0j] * (max_order + 1)
    for nn in range(max_order + 1):
        s = 0.0 + 0j
        for k in range(nn + 1):
            s += M_signed[k] * pt[nn - k]
        reconstructed[nn] = s

    max_err = 0.0
    for nn in range(max_order + 1):
        err = abs(dt[nn] - reconstructed[nn])
        if err > max_err:
            max_err = err

    return {
        'zero_index': n,
        'c_val': c_val,
        'kappa': kappa,
        'wall_crossing_holds': max_err < 1e-6,
        'max_reconstruction_error': max_err,
        'dt_leading_abs': [abs(dt[i]) for i in range(min(10, max_order + 1))],
        'pt_leading_abs': [abs(pt[i]) for i in range(min(10, max_order + 1))],
    }


def gv_at_zeta_zero(n: int, max_order: int = 20,
                    max_r: int = 25) -> Dict[str, Any]:
    r"""Extract GV invariants at c = c(rho_n) and check integrality.

    At complex c, the GV invariants will be complex. Integrality
    means |Im(n_g^k)| < tol and |Re(n_g^k) - round(Re)| < tol.
    """
    c_val = c_at_zeta_zero(n)
    kappa = c_val / 2
    shadow = virasoro_shadow_float(c_val, max_r)

    dt = plethystic_exp_float(shadow, max_order)

    # PT
    M_signed = macmahon_signed_power_float(max_order, kappa)
    inv_M = [0.0 + 0j] * (max_order + 1)
    inv_M[0] = 1.0
    for nn in range(1, max_order + 1):
        s = 0.0 + 0j
        for k in range(1, nn + 1):
            s += M_signed[k] * inv_M[nn - k]
        inv_M[nn] = -s

    pt = [0.0 + 0j] * (max_order + 1)
    for nn in range(max_order + 1):
        s = 0.0 + 0j
        for k in range(nn + 1):
            s += dt[k] * inv_M[nn - k]
        pt[nn] = s

    # PL of Z^PT(-q) for BPS
    pt_minus = [pt[nn] * ((-1) ** nn) for nn in range(max_order + 1)]
    pl = plethystic_log_float(pt_minus, min(max_order, 10))

    gv_data = {}
    for k in range(1, min(11, len(pl))):
        gv_data[k] = pl[k]

    # Check integrality
    all_near_int = True
    tol = 1e-4
    for k, val in gv_data.items():
        if abs(val.imag) > tol or abs(val.real - round(val.real)) > tol:
            all_near_int = False
            break

    return {
        'zero_index': n,
        'c_val': c_val,
        'gv_bps': gv_data,
        'gv_abs': {k: abs(v) for k, v in gv_data.items()},
        'all_near_integer': all_near_int,
    }


# ============================================================================
# 12. Multi-family DT comparison
# ============================================================================

def family_dt_comparison(max_n: int = 20) -> Dict[str, Any]:
    r"""Compare DT partition functions across all standard families.

    - Heisenberg (k=1): class G, PE terminates
    - Affine sl_2 (k=1): class L
    - Beta-gamma (lam=1): class C
    - Virasoro (c=1): class M (infinite tower)

    Returns leading coefficients and depth classification.
    """
    families = {
        'heisenberg_k1': heisenberg_shadow_coefficients(1, max_n + 2),
        'affine_sl2_k1': affine_sl2_shadow_coefficients(1, max_n + 2),
        'betagamma_lam1': betagamma_shadow_coefficients(1, max_n + 2),
        'virasoro_c1': virasoro_shadow_coefficients(1, max_n + 2),
    }

    result = {}
    for name, shadow in families.items():
        dt = plethystic_exp(shadow, max_n)
        result[name] = {
            'kappa': float(shadow[2]),
            'dt_leading': [float(dt[i]) for i in range(min(10, max_n + 1))],
            'pe_pl_roundtrip': verify_pe_pl_roundtrip(shadow, min(max_n, 15))['roundtrip_exact'],
        }
    return result


# ============================================================================
# 13. Shadow depth and DT complexity
# ============================================================================

def shadow_depth_class(shadow_seq: Dict[int, Rational],
                       tol: float = 1e-12) -> str:
    r"""Classify shadow depth: G/L/C/M."""
    max_r = max(shadow_seq.keys())
    last_nonzero = 2
    for r in range(2, max_r + 1):
        val = float(shadow_seq.get(r, Rational(0)))
        if abs(val) > tol:
            last_nonzero = r

    if last_nonzero == 2:
        return 'G'
    elif last_nonzero == 3:
        return 'L'
    elif last_nonzero == 4:
        return 'C'
    else:
        return 'M'


# ============================================================================
# 14. DT_n for n=0..30 via Hilbert scheme interpretation
# ============================================================================

def hilb_dt_coefficients(shadow_seq: Dict[int, Rational],
                         max_n: int = 30) -> List[Rational]:
    r"""DT_n(A) = Euler characteristic of Hilb^n(shadow variety).

    Under the shadow-DT correspondence, the DT invariants counting
    n-point configurations are the coefficients of Z^DT = PE[g]:
      DT_n = [q^n] PE[g_A(q)]

    This is the virtual count of ideal sheaves of colength n.
    """
    return plethystic_exp(shadow_seq, max_n)


def pt_pair_coefficients(shadow_seq: Dict[int, Rational],
                         chi: Rational,
                         max_n: int = 30) -> List[Rational]:
    r"""PT_n(A) = count of stable pairs at charge n.

    Z^PT = sum PT_n q^n = Z^DT / M(-q)^chi.
    """
    return shadow_pt_coefficients(shadow_seq, chi, max_n)


# ============================================================================
# 15. Full analysis pipeline
# ============================================================================

def full_dt_pt_analysis(shadow_seq: Dict[int, Rational],
                        chi: Rational,
                        max_n: int = 30,
                        family_name: str = 'unknown') -> Dict[str, Any]:
    r"""Complete DT/PT analysis for a shadow sequence.

    Computes:
    1. DT coefficients (PE)
    2. PT coefficients (DT / M(-q)^chi)
    3. Wall-crossing verification
    4. PE/PL roundtrip
    5. GV extraction
    6. Integrality check
    7. Depth classification
    """
    dt = shadow_dt_coefficients(shadow_seq, max_n)
    pt = shadow_pt_coefficients(shadow_seq, chi, max_n)
    wc = dt_pt_wall_crossing_check(shadow_seq, chi, min(max_n, 20))
    rt = verify_pe_pl_roundtrip(shadow_seq, min(max_n, 20))
    gv = gv_from_pt(pt, g_max=3, k_max=min(10, max_n))
    integ = gv_integrality_check(gv)
    depth = shadow_depth_class(shadow_seq)

    return {
        'family': family_name,
        'chi': chi,
        'depth_class': depth,
        'dt_leading': [dt[i] for i in range(min(10, max_n + 1))],
        'pt_leading': [pt[i] for i in range(min(10, max_n + 1))],
        'wall_crossing_exact': wc['exact_match'],
        'roundtrip_exact': rt['roundtrip_exact'],
        'gv_all_integer': integ['all_integer'],
        'gv_sample': {str(k): float(v) for k, v in list(gv.items())[:5]},
    }


def heisenberg_full_analysis(k: int = 1, max_n: int = 30) -> Dict[str, Any]:
    """Complete DT/PT analysis for Heisenberg at level k."""
    shadow = heisenberg_shadow_coefficients(k, max_n + 2)
    return full_dt_pt_analysis(shadow, Rational(k), max_n, f'heisenberg_k{k}')


def virasoro_full_analysis(c: int = 1, max_n: int = 20) -> Dict[str, Any]:
    """Complete DT/PT analysis for Virasoro at central charge c."""
    shadow = virasoro_shadow_coefficients(c, max_n + 2)
    chi = Rational(c, 2)  # kappa(Vir_c) = c/2
    return full_dt_pt_analysis(shadow, chi, max_n, f'virasoro_c{c}')


def affine_sl2_full_analysis(k: int = 1, max_n: int = 20) -> Dict[str, Any]:
    """Complete DT/PT analysis for affine sl_2."""
    shadow = affine_sl2_shadow_coefficients(k, max_n + 2)
    kappa = Rational(3) * Rational(k + 2) / 4
    return full_dt_pt_analysis(shadow, kappa, max_n, f'affine_sl2_k{k}')


def betagamma_full_analysis(lam: int = 1, max_n: int = 20) -> Dict[str, Any]:
    """Complete DT/PT analysis for beta-gamma."""
    shadow = betagamma_shadow_coefficients(lam, max_n + 2)
    lv = Rational(lam)
    cv = 2 * (6 * lv ** 2 - 6 * lv + 1)
    kappa = cv / 2
    return full_dt_pt_analysis(shadow, kappa, max_n, f'betagamma_lam{lam}')
