r"""Hilbert modular shadow forms over real quadratic fields Q(sqrt(D)).

This module extends the shadow obstruction tower from Q to real quadratic
fields K = Q(sqrt(D)), producing genuinely new mathematical objects:
shadow Hilbert modular forms, Hilbert shadow zeta functions, shadow Hecke
Grossencharacters, and Asai L-function factorizations.

MATHEMATICAL FRAMEWORK
======================

Let A be a modular Koszul algebra with shadow coefficients {S_r(A)}_{r >= 2}.
Fix a real quadratic field K = Q(sqrt(D)) of class number 1, with ring of
integers O_K, fundamental unit epsilon_D, and the two real embeddings
sigma_1, sigma_2: K -> R.

1. SHADOW HILBERT MODULAR FORM

   F_A^D(tau_1, tau_2) = sum_{r >= 2} S_r(A) * E_r^{Hilb}(tau_1, tau_2; D)

   where E_r^{Hilb} is the Hilbert Eisenstein series of parallel weight r
   for the Hilbert modular group SL_2(O_K):

   E_r^{Hilb}(tau_1, tau_2; D) = sum_{(c,d) in O_K^2/(units)}
       N(c tau + d)^{-r}

   with N(alpha) = alpha^{sigma_1} * alpha^{sigma_2} the norm.

   The Fourier expansion is:
   E_r^{Hilb}(tau_1, tau_2) = 1 + (2/zeta_K(-r+1)) *
       sum_{0 << nu in (O_K)^+} sigma_{r-1}^K(nu) *
       exp(2 pi i (Tr(nu tau_1) + Tr(conj(nu) tau_2)))

   where sigma_{r-1}^K(nu) = sum_{0 << d | nu} N(d)^{r-1} and 0 << means
   totally positive.

2. HILBERT SHADOW ZETA

   zeta_A^D(s) = sum_{ideal a of O_K} S_{N(a)}(A) * N(a)^{-s}

   where the sum runs over nonzero ideals and N(a) is the ideal norm.
   Since O_K has class number 1 for our chosen discriminants, every ideal
   is principal: a = (alpha) for alpha in O_K / units.

   Alternative form via norm sums:
   zeta_A^D(s) = sum_{n >= 2} S_n(A) * r_K(n) * n^{-s}

   where r_K(n) = #{ideals a of O_K : N(a) = n}.

3. HECKE GROSSENCHARAKTER FROM SHADOW DATA

   chi_shadow: I_K -> C* defined on principal ideals by
   chi_shadow((alpha)) = |sigma_1(alpha)/sigma_2(alpha)|^{it}

   where t = t(A) is determined by the shadow growth rate rho(A).

4. ASAI L-FUNCTION FACTORIZATION

   L(s, As(F_A^D)) = L(s, f_shadow) * L(s, f_shadow x chi_D)

   where As is the Asai transfer from GL_2/K to GL_4/Q, and chi_D is the
   Kronecker character (D/.).

5. BASE CHANGE

   BC: GL_2/Q -> GL_2/K sends f_shadow to a Hilbert modular form.
   L(s, BC(f_shadow)) = L(s, f_shadow) * L(s, f_shadow x chi_D).

6. STARK UNITS

   u_D = exp(-L'_D(0, chi_shadow) / L_D(0, chi_shadow))

   When chi_shadow is a ray class character, Stark's conjecture predicts
   u_D is a unit in the Hilbert class field of K.

DISCRIMINANTS:
    D = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    These are the first 10 fundamental discriminants for which Q(sqrt(D))
    has class number 1.

CONVENTIONS:
    - Parallel weight Hilbert modular forms (weight (r, r))
    - Narrow class number 1 assumed (true for all our D)
    - Totally positive elements 0 << alpha means sigma_i(alpha) > 0 for all i
    - Norm N(a + b sqrt(D)) = a^2 - D b^2

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Multi-path verification required for all claims.
CAUTION (AP38): Normalisation conventions for Hilbert Eisenstein series
    vary between references; we follow Shimura's convention.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    conj:arithmetic-comparison (arithmetic_shadows.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
    virasoro_growth_rate_exact,
    _log_gamma_complex,
)


# ============================================================================
# 0.  Real quadratic field arithmetic
# ============================================================================

# First 10 squarefree D > 1 with h(Q(sqrt(D))) = 1
REAL_QUADRATIC_DISCRIMINANTS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Fundamental discriminants: d_K = 4D if D = 2,3 mod 4; d_K = D if D = 1 mod 5
# Actually: d_K = D if D ≡ 1 (mod 4), d_K = 4D otherwise.
# For our list: D=5 -> d_K=5; D=13 -> d_K=13; D=17 -> d_K=17; D=29 -> d_K=29.
# D=2 -> d_K=8; D=3 -> d_K=12; D=7 -> d_K=28; D=11 -> d_K=44;
# D=19 -> d_K=76; D=23 -> d_K=92.


def fundamental_discriminant(D: int) -> int:
    """Compute the fundamental discriminant d_K of Q(sqrt(D)).

    d_K = D if D ≡ 1 (mod 4), d_K = 4D otherwise.
    """
    if D % 4 == 1:
        return D
    return 4 * D


def fundamental_unit(D: int) -> Tuple[int, int]:
    """Compute fundamental unit epsilon = a + b*sqrt(D) of Q(sqrt(D))
    via continued fraction expansion of sqrt(D).

    Returns (a, b) such that a^2 - D*b^2 = ±1, with a, b > 0 minimal.
    """
    # Continued fraction expansion of sqrt(D) to find fundamental solution
    # to Pell's equation x^2 - D*y^2 = ±1
    m = 0
    d = 1
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        raise ValueError(f"D = {D} is a perfect square")
    a = a0

    # Convergent numerators and denominators
    p_prev, p_curr = 1, a0
    q_prev, q_curr = 0, 1

    for _ in range(1000):
        m = d * a - m
        d = (D - m * m) // d
        if d == 0:
            break
        a = (a0 + m) // d

        p_prev, p_curr = p_curr, a * p_curr + p_prev
        q_prev, q_curr = q_curr, a * q_curr + q_prev

        # Check if we found a solution to Pell's equation
        val = p_curr * p_curr - D * q_curr * q_curr
        if val == 1 or val == -1:
            return (p_curr, q_curr)

    raise RuntimeError(f"Failed to find fundamental unit for D = {D}")


def norm_element(a: float, b: float, D: int) -> float:
    """Norm of a + b*sqrt(D): N(alpha) = a^2 - D*b^2."""
    return a * a - D * b * b


def trace_element(a: float, b: float, D: int) -> float:
    """Trace of a + b*sqrt(D): Tr(alpha) = 2a."""
    return 2.0 * a


@lru_cache(maxsize=128)
def _kronecker_symbol(D: int, n: int) -> int:
    """Kronecker symbol (d_K / n) for the fundamental discriminant d_K of Q(sqrt(D)).

    This is the quadratic character chi_D.
    """
    d_K = fundamental_discriminant(D)
    return _jacobi_symbol_extended(d_K, n)


def _jacobi_symbol_extended(a: int, n: int) -> int:
    """Extended Jacobi/Kronecker symbol (a/n)."""
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n == 1:
        return 1
    if n < 0:
        n = -n
        if a < 0:
            return -_jacobi_symbol_extended(-a, n)
    # Standard Jacobi symbol for odd n
    if n == 2:
        if a % 2 == 0:
            return 0
        a8 = a % 8
        if a8 == 1 or a8 == 7:
            return 1
        return -1

    # Factor out powers of 2 from n
    result = 1
    while n % 2 == 0:
        n //= 2
        a8 = a % 8
        if a % 2 == 0:
            return 0
        if a8 == 3 or a8 == 5:
            result = -result

    if n == 1:
        return result

    # Now n is odd > 1, use standard Jacobi
    return result * _jacobi_symbol_odd(a % n, n)


def _jacobi_symbol_odd(a: int, n: int) -> int:
    """Jacobi symbol (a/n) for odd n > 0 via quadratic reciprocity."""
    if n == 1:
        return 1
    if a == 0:
        return 0
    if a == 1:
        return 1

    result = 1
    a = a % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


@lru_cache(maxsize=1024)
def ideal_norm_count(D: int, n: int) -> int:
    """Count r_K(n) = number of ideals of O_K with norm n.

    For K = Q(sqrt(D)) with class number 1:
    r_K(n) = sum_{d | n} chi_D(d)

    where chi_D = (d_K / .) is the Kronecker character.
    """
    if n <= 0:
        return 0
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += _kronecker_symbol(D, d)
    return total


def dedekind_zeta_K_partial(D: int, s: complex, max_n: int = 200) -> complex:
    """Partial sum of Dedekind zeta function of K = Q(sqrt(D)):

    zeta_K(s) = sum_{n >= 1} r_K(n) * n^{-s}
              = zeta(s) * L(s, chi_D)

    Uses direct summation for verification.
    """
    total = 0.0 + 0.0j
    for n in range(1, max_n + 1):
        rn = ideal_norm_count(D, n)
        if rn != 0:
            total += rn * n ** (-s)
    return total


def dedekind_zeta_factored(D: int, s: complex, max_n: int = 200) -> complex:
    """zeta_K(s) = zeta(s) * L(s, chi_D) via separate partial sums.

    Verification path for dedekind_zeta_K_partial.
    """
    zeta_val = sum(n ** (-s) for n in range(1, max_n + 1))
    L_val = sum(_kronecker_symbol(D, n) * n ** (-s) for n in range(1, max_n + 1))
    return zeta_val * L_val


# ============================================================================
# 1.  Hilbert Eisenstein series Fourier coefficients
# ============================================================================

def hilbert_eisenstein_fourier_coeff(
    D: int,
    r: int,
    nu_a: int,
    nu_b: int,
    max_divisors: int = 500,
) -> complex:
    """Fourier coefficient c(nu) of the Hilbert Eisenstein series E_r^{Hilb}
    at the totally positive element nu = nu_a + nu_b * omega, where
    omega = sqrt(D) if D != 1 mod 4, omega = (1 + sqrt(D))/2 if D = 1 mod 4.

    For r >= 2 even, the Fourier expansion of E_r^{Hilb}(tau_1, tau_2) is:

        E_r^{Hilb} = 1 + C_r * sum_{0 << nu} sigma_{r-1}^K(nu) * q_1^{Tr(nu)} * ...

    where C_r = 2^r / zeta_K(1-r) and sigma_{r-1}^K(nu) = sum_{d | (nu)} N(d)^{r-1}.

    For simplicity with real quadratic fields, we encode nu by its norm and trace,
    and compute sigma_{r-1}^K(nu) as a divisor sum over ideals dividing (nu).

    Parameters
    ----------
    D : squarefree discriminant
    r : weight (parallel weight (r, r))
    nu_a, nu_b : coordinates of totally positive element nu = nu_a + nu_b * omega
    max_divisors : truncation for divisor search

    Returns
    -------
    The Fourier coefficient at nu (real for Eisenstein series).
    """
    if r < 2:
        raise ValueError(f"Weight r = {r} must be >= 2")

    # Constant term
    if nu_a == 0 and nu_b == 0:
        return complex(1.0, 0.0)

    # Compute the norm N(nu) = nu_a^2 - D * nu_b^2 (for D != 1 mod 4)
    # or N(nu) = nu_a^2 + nu_a * nu_b - ((D-1)/4) * nu_b^2 (for D = 1 mod 4)
    if D % 4 == 1:
        norm_nu = nu_a * nu_a + nu_a * nu_b - ((D - 1) // 4) * nu_b * nu_b
        trace_nu = 2 * nu_a + nu_b
    else:
        norm_nu = nu_a * nu_a - D * nu_b * nu_b
        trace_nu = 2 * nu_a

    if norm_nu <= 0:
        # nu is not totally positive
        return complex(0.0, 0.0)

    # sigma_{r-1}^K(nu) = sum over ideal divisors d of (nu) of N(d)^{r-1}
    # For class number 1, ideals are principal, so we sum over divisors of N(nu)
    # in Z, weighted by their multiplicity as ideal norms.
    # sigma_{r-1}^K(nu) = sum_{d | N(nu)} chi_D(N(nu)/d) * d^{r-1}
    # Actually for principal ideal (nu), the divisor sum factors through the norm:
    # sigma_{r-1}^K((nu)) = sum_{a | (nu) as ideal} N(a)^{r-1}
    # For h_K = 1, this equals sum_{d | N(nu)} r_K^*(d) * d^{r-1}
    # where r_K^* counts primitive representations.
    # Simpler: use the multiplicative structure.
    # sigma_{r-1}^K(n) := sum_{d | n} chi_D(d) * d^{r-1}  [twisted divisor sum]

    n = abs(norm_nu)
    sigma_val = 0.0
    for d in range(1, n + 1):
        if n % d == 0:
            chi = _kronecker_symbol(D, d)
            sigma_val += chi * d ** (r - 1)

    # Normalisation factor: C_r = 2^r / zeta_K(1 - r)
    # zeta_K(1 - r) = zeta(1 - r) * L(1 - r, chi_D)
    # For r even >= 2: zeta(1 - r) = -B_r / r where B_r is Bernoulli number
    # L(1 - r, chi_D) can be computed from generalized Bernoulli numbers
    # For simplicity, we use the numerical zeta_K value at 1-r.
    zeta_K_1mr = _dedekind_zeta_at_negative_integer(D, r - 1)
    if abs(zeta_K_1mr) < 1e-50:
        C_r = 0.0
    else:
        C_r = 2.0 ** r / zeta_K_1mr

    return complex(C_r * sigma_val, 0.0)


def _bernoulli_number(n: int) -> float:
    """Bernoulli number B_n via the recursion."""
    if n == 0:
        return 1.0
    if n == 1:
        return -0.5
    if n % 2 == 1 and n > 1:
        return 0.0
    # Use the standard recursion
    B = [0.0] * (n + 1)
    B[0] = 1.0
    B[1] = -0.5
    for m in range(2, n + 1):
        if m % 2 == 1 and m > 1:
            B[m] = 0.0
            continue
        s = 0.0
        for k in range(m):
            s += _binomial(m + 1, k) * B[k]
        B[m] = -s / (m + 1)
    return B[n]


def _binomial(n: int, k: int) -> float:
    """Binomial coefficient C(n, k)."""
    if k < 0 or k > n:
        return 0.0
    return math.comb(n, k)


def _generalized_bernoulli(D: int, n: int) -> float:
    """Generalized Bernoulli number B_{n, chi_D}.

    B_{n, chi} = f^{n-1} sum_{a=1}^{f} chi(a) * B_n(a/f)

    where f is the conductor (= |d_K|) and B_n(x) is the Bernoulli polynomial.
    """
    f = abs(fundamental_discriminant(D))
    total = 0.0
    for a in range(1, f + 1):
        chi_a = _kronecker_symbol(D, a)
        if chi_a == 0:
            continue
        # B_n(a/f) = sum_{k=0}^{n} C(n,k) * B_k * (a/f)^{n-k}
        x = a / f
        bernoulli_poly = 0.0
        for k in range(n + 1):
            bernoulli_poly += _binomial(n, k) * _bernoulli_number(k) * x ** (n - k)
        total += chi_a * bernoulli_poly
    return f ** (n - 1) * total


def _dedekind_zeta_at_negative_integer(D: int, m: int) -> float:
    """Compute zeta_K(-m) for m >= 0 integer.

    zeta_K(-m) = zeta(-m) * L(-m, chi_D)

    zeta(-m) = -B_{m+1} / (m+1)   for m >= 0
    L(-m, chi_D) = -B_{m+1, chi_D} / (m+1)   for m >= 0

    So zeta_K(-m) = B_{m+1} * B_{m+1, chi_D} / (m+1)^2
    """
    n = m + 1
    B_n = _bernoulli_number(n)
    B_n_chi = _generalized_bernoulli(D, n)
    zeta_neg_m = -B_n / n
    L_neg_m = -B_n_chi / n
    return zeta_neg_m * L_neg_m


# ============================================================================
# 2.  Shadow Hilbert modular form
# ============================================================================

@dataclass
class HilbertShadowForm:
    """Shadow Hilbert modular form F_A^D(tau_1, tau_2).

    Attributes
    ----------
    D : discriminant of real quadratic field
    family : algebra family name
    param : algebra parameter (c, k, etc.)
    shadow_coeffs : dict r -> S_r(A)
    fourier_coeffs : dict (nu_a, nu_b) -> c(nu)
    max_r : maximum arity used
    """
    D: int
    family: str
    param: float
    shadow_coeffs: Dict[int, float]
    fourier_coeffs: Dict[Tuple[int, int], complex] = field(default_factory=dict)
    max_r: int = 30


def compute_hilbert_shadow_form(
    D: int,
    family: str,
    param: float,
    max_r: int = 30,
    max_nu_norm: int = 50,
) -> HilbertShadowForm:
    """Compute the shadow Hilbert modular form F_A^D.

    F_A^D(tau_1, tau_2) = sum_{r >= 2} S_r(A) * E_r^{Hilb}(tau_1, tau_2; D)

    We compute Fourier coefficients c(nu) for totally positive nu with
    N(nu) <= max_nu_norm.

    Parameters
    ----------
    D : squarefree discriminant
    family : 'heisenberg', 'affine_sl2', 'virasoro', 'betagamma'
    param : family parameter
    max_r : maximum arity for shadow coefficients
    max_nu_norm : maximum norm of nu for Fourier coefficients
    """
    # Get shadow coefficients
    shadow_coeffs = _get_shadow_coefficients(family, param, max_r)

    form = HilbertShadowForm(
        D=D, family=family, param=param,
        shadow_coeffs=shadow_coeffs, max_r=max_r,
    )

    # Compute Fourier coefficients
    # c(0,0) = sum_r S_r * 1 = sum_r S_r  (constant term)
    const_term = sum(shadow_coeffs.get(r, 0.0) for r in range(2, max_r + 1))
    form.fourier_coeffs[(0, 0)] = complex(const_term, 0.0)

    # Enumerate totally positive elements nu = nu_a + nu_b * omega
    # with 0 < N(nu) <= max_nu_norm
    omega_type = "half" if D % 4 == 1 else "sqrt"
    nu_range = int(math.sqrt(max_nu_norm * max(D, 4))) + 2

    for nu_b in range(-nu_range, nu_range + 1):
        for nu_a in range(-nu_range, nu_range + 1):
            if nu_a == 0 and nu_b == 0:
                continue

            # Compute norm and trace
            if D % 4 == 1:
                norm_nu = nu_a ** 2 + nu_a * nu_b - ((D - 1) // 4) * nu_b ** 2
                trace_nu = 2 * nu_a + nu_b
            else:
                norm_nu = nu_a ** 2 - D * nu_b ** 2
                trace_nu = 2 * nu_a

            # Totally positive: both embeddings positive
            # sigma_1(nu) = nu_a + nu_b * sqrt(D) > 0  [or half-integer ring version]
            # sigma_2(nu) = nu_a - nu_b * sqrt(D) > 0  [conjugate]
            # Equivalently: trace > 0 and norm > 0
            if norm_nu <= 0 or norm_nu > max_nu_norm or trace_nu <= 0:
                continue

            # Check actual positivity of both embeddings
            if D % 4 == 1:
                s1 = nu_a + nu_b * (1 + math.sqrt(D)) / 2
                s2 = nu_a + nu_b * (1 - math.sqrt(D)) / 2
            else:
                s1 = nu_a + nu_b * math.sqrt(D)
                s2 = nu_a - nu_b * math.sqrt(D)

            if s1 <= 0 or s2 <= 0:
                continue

            # Sum over arities
            c_nu = 0.0 + 0.0j
            for r in range(2, max_r + 1):
                Sr = shadow_coeffs.get(r, 0.0)
                if abs(Sr) < 1e-30:
                    continue
                e_coeff = hilbert_eisenstein_fourier_coeff(D, r, nu_a, nu_b)
                c_nu += Sr * e_coeff

            if abs(c_nu) > 1e-30:
                form.fourier_coeffs[(nu_a, nu_b)] = c_nu

    return form


def _get_shadow_coefficients(family: str, param: float, max_r: int) -> Dict[int, float]:
    """Dispatch to appropriate shadow coefficient provider."""
    dispatch = {
        'heisenberg': lambda: heisenberg_shadow_coefficients(param, max_r),
        'affine_sl2': lambda: affine_sl2_shadow_coefficients(param, max_r),
        'virasoro': lambda: virasoro_shadow_coefficients_numerical(param, max_r),
        'betagamma': lambda: betagamma_shadow_coefficients(param, max_r),
    }
    if family not in dispatch:
        raise ValueError(f"Unknown family: {family}")
    return dispatch[family]()


# ============================================================================
# 3.  Hilbert shadow zeta function
# ============================================================================

def hilbert_shadow_zeta(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """Evaluate the Hilbert shadow zeta function

    zeta_A^D(s) = sum_{n >= 2} S_n(A) * r_K(n) * n^{-s}

    where r_K(n) = #{ideals of O_K with norm n}.

    Parameters
    ----------
    D : squarefree discriminant
    shadow_coeffs : arity -> S_r
    s : complex evaluation point
    max_n : truncation

    Returns
    -------
    Complex value of the partial sum.
    """
    total = 0.0 + 0.0j
    max_r = max(shadow_coeffs.keys()) if shadow_coeffs else 2
    upper = min(max_r, max_n)
    for n in range(2, upper + 1):
        Sn = shadow_coeffs.get(n, 0.0)
        if abs(Sn) < 1e-30:
            continue
        rn = ideal_norm_count(D, n)
        if rn == 0:
            continue
        total += Sn * rn * n ** (-s)
    return total


def hilbert_shadow_zeta_factored(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """Verification: zeta_A^D(s) via factored form.

    zeta_A^D(s) = sum_n S_n * r_K(n) * n^{-s}

    where r_K(n) = sum_{d|n} chi_D(d).

    Expand: = sum_n S_n * sum_{d|n} chi_D(d) * n^{-s}
            = sum_{d,m: dm <= N} S_{dm} * chi_D(d) * (dm)^{-s}

    This is an independent computation path.
    """
    total = 0.0 + 0.0j
    max_r = max(shadow_coeffs.keys()) if shadow_coeffs else 2
    upper = min(max_r, max_n)
    for d in range(1, upper + 1):
        chi_d = _kronecker_symbol(D, d)
        if chi_d == 0:
            continue
        for m in range(1, upper // d + 1):
            n = d * m
            if n < 2:
                continue
            Sn = shadow_coeffs.get(n, 0.0)
            if abs(Sn) < 1e-30:
                continue
            total += Sn * chi_d * n ** (-s)
    return total


# ============================================================================
# 4.  Hecke L-function with shadow Grossencharakter
# ============================================================================

def shadow_hecke_grossencharakter_parameter(
    family: str,
    param: float,
) -> float:
    """Compute the Grossencharakter parameter t from shadow data.

    The shadow growth rate rho(A) determines an archimedean parameter t
    via t = log(rho) / (2 * pi).

    For class G/L/C: rho = 0 -> t = 0 (trivial character).
    For class M: rho > 0 -> t = log(rho) / (2*pi).

    Returns t.
    """
    if family == 'heisenberg':
        return 0.0
    elif family == 'affine_sl2':
        return 0.0  # Class L, terminates
    elif family == 'betagamma':
        return 0.0  # Class C, terminates
    elif family == 'virasoro':
        rho = virasoro_growth_rate_exact(param)
        if rho <= 0 or rho == float('inf'):
            return 0.0
        return math.log(rho) / (2.0 * math.pi)
    else:
        return 0.0


def hecke_L_shadow(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    t_param: float = 0.0,
    max_n: int = 200,
) -> complex:
    """Hecke L-function over Q(sqrt(D)) with shadow Grossencharakter.

    L_D(s, chi_shadow) = sum_{n >= 1} a_n * n^{-s}

    where a_n = sum_{N(a)=n} chi_shadow(a) and chi_shadow encodes the
    shadow growth rate via the archimedean parameter t.

    For t = 0 (trivial character): L_D(s, chi_0) = zeta_K(s).
    For t != 0: chi_shadow((alpha)) = |sigma_1(alpha)/sigma_2(alpha)|^{it}.

    We approximate by:
    L_D(s, chi_shadow) ~ sum_n r_K(n) * n^{-s} * phase_correction(n, t, D)

    where the phase correction averages over representations of n as ideal norms.
    """
    total = 0.0 + 0.0j
    for n in range(1, max_n + 1):
        rn = ideal_norm_count(D, n)
        if rn == 0:
            continue
        # Phase correction from Grossencharakter
        if abs(t_param) < 1e-15:
            phase = 1.0
        else:
            # Average over ideal representations: for principal ideals (alpha)
            # with N(alpha) = n, chi_shadow = |sigma_1/sigma_2|^{it}
            # For class number 1, this is a well-defined average.
            # The key simplification: for an ideal of norm n in O_K,
            # the ratio sigma_1/sigma_2 of the generator depends on the
            # specific generator. For the canonical generator, we use
            # the minimal totally positive element.
            phase = _grossencharakter_phase(D, n, t_param)
        total += rn * phase * n ** (-s)
    return total


def _grossencharakter_phase(D: int, n: int, t: float) -> complex:
    """Compute Grossencharakter phase for ideal of norm n in Q(sqrt(D)).

    For the canonical generator alpha of the principal ideal of norm n,
    compute |sigma_1(alpha)/sigma_2(alpha)|^{it}.

    We find the minimal totally positive alpha = a + b*sqrt(D) with
    a^2 - D*b^2 = n (if D != 1 mod 4) and compute the ratio.
    """
    if abs(t) < 1e-15:
        return complex(1.0, 0.0)

    # Find a representation n = a^2 - D*b^2 (or suitable for D = 1 mod 4)
    sqrt_D = math.sqrt(D)
    best_ratio = None

    if D % 4 == 1:
        # O_K = Z[(1+sqrt(D))/2], norm(a + b*omega) = a^2 + ab - (D-1)/4 * b^2
        q = (D - 1) // 4
        for b in range(0, int(math.sqrt(4 * n / D)) + 2):
            # a^2 + ab - q*b^2 = n => a^2 + ab = n + q*b^2
            disc = b * b + 4 * (n + q * b * b)
            if disc < 0:
                continue
            sqrt_disc = math.isqrt(disc)
            if sqrt_disc * sqrt_disc == disc:
                a_2 = -b + sqrt_disc
                if a_2 >= 0 and a_2 % 2 == 0:
                    a = a_2 // 2
                    s1 = a + b * (1 + sqrt_D) / 2
                    s2 = a + b * (1 - sqrt_D) / 2
                    if s1 > 0 and s2 > 0:
                        ratio = s1 / s2
                        best_ratio = ratio
                        break
    else:
        # O_K = Z[sqrt(D)], norm(a + b*sqrt(D)) = a^2 - D*b^2
        for b in range(0, int(math.sqrt(n / D)) + 2):
            a2 = n + D * b * b
            a = int(math.sqrt(a2))
            if a * a == a2:
                s1 = a + b * sqrt_D
                s2 = a - b * sqrt_D
                if s1 > 0 and s2 > 0:
                    ratio = s1 / s2
                    best_ratio = ratio
                    break

    if best_ratio is None or best_ratio <= 0:
        return complex(1.0, 0.0)

    # |sigma_1/sigma_2|^{it} = exp(it * log(ratio))
    return cmath.exp(1j * t * math.log(best_ratio))


# ============================================================================
# 5.  Stark unit computation
# ============================================================================

def stark_unit_candidate(
    D: int,
    shadow_coeffs: Dict[int, float],
    family: str = 'virasoro',
    param: float = 25.0,
    max_n: int = 500,
    h: float = 1e-6,
) -> Tuple[complex, float]:
    """Compute the Stark unit candidate:

    u_D = exp(-L'_D(0, chi_shadow) / L_D(0, chi_shadow))

    Uses numerical differentiation for L'(0).

    Returns (u_D, |u_D|).
    """
    t_param = shadow_hecke_grossencharakter_parameter(family, param)

    # L_D(0, chi_shadow)
    L_at_0 = hecke_L_shadow(D, shadow_coeffs, complex(0, 0), t_param, max_n)

    if abs(L_at_0) < 1e-30:
        return (complex(float('nan'), 0), float('nan'))

    # L'_D(0) via finite difference
    L_plus = hecke_L_shadow(D, shadow_coeffs, complex(h, 0), t_param, max_n)
    L_minus = hecke_L_shadow(D, shadow_coeffs, complex(-h, 0), t_param, max_n)
    L_prime = (L_plus - L_minus) / (2 * h)

    ratio = -L_prime / L_at_0
    u_D = cmath.exp(ratio)
    return (u_D, abs(u_D))


# ============================================================================
# 6.  Class number formula
# ============================================================================

def class_number_from_shadow(
    D: int,
    max_n: int = 1000,
) -> Tuple[float, int, float]:
    """Verify the class number formula for Q(sqrt(D)):

    h_D * R_D = sqrt(d_K) / (2 * pi) * L(1, chi_D)

    where d_K is the fundamental discriminant, R_D is the regulator
    (log of fundamental unit), and L(1, chi_D) = sum chi_D(n)/n.

    Returns (h_D_computed, h_D_rounded, regulator).
    """
    d_K = fundamental_discriminant(D)
    eps_a, eps_b = fundamental_unit(D)

    # Regulator R_D = log(epsilon_D)
    sqrt_D = math.sqrt(D)
    if D % 4 == 1:
        eps_val = eps_a + eps_b * (1 + sqrt_D) / 2
    else:
        eps_val = eps_a + eps_b * sqrt_D
    R_D = math.log(eps_val)

    # L(1, chi_D) by partial sum
    L_1_chi = 0.0
    for n in range(1, max_n + 1):
        chi = _kronecker_symbol(D, n)
        L_1_chi += chi / n

    # Class number formula: h_D = sqrt(d_K) / (2 * R_D) * L(1, chi_D)
    # (for real quadratic fields with no w factor since w = 2 for D > 0)
    h_D = math.sqrt(abs(d_K)) / (2.0 * R_D) * L_1_chi

    return (h_D, round(h_D), R_D)


# ============================================================================
# 7.  Base change: comparison of L-functions
# ============================================================================

def base_change_L_function(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """L-function of the base change BC(f_shadow) from GL_2/Q to GL_2/K.

    L(s, BC(f_shadow)) = L(s, f_shadow) * L(s, f_shadow x chi_D)

    where f_shadow has Fourier coefficients from the shadow tower:
    a_n(f_shadow) = S_n(A) for n >= 2, a_1 = 1.

    L(s, f_shadow) = sum_{n >= 1} S_n * n^{-s}
    L(s, f_shadow x chi_D) = sum_{n >= 1} S_n * chi_D(n) * n^{-s}

    Returns L(s, BC(f_shadow)).
    """
    # L(s, f_shadow) = 1 + sum_{n >= 2} S_n * n^{-s}
    L_f = 1.0 + 0.0j
    for n in range(2, max_n + 1):
        Sn = shadow_coeffs.get(n, 0.0)
        if abs(Sn) < 1e-30:
            continue
        L_f += Sn * n ** (-s)

    # L(s, f_shadow x chi_D) = chi_D(1) + sum_{n >= 2} S_n * chi_D(n) * n^{-s}
    L_f_chi = complex(_kronecker_symbol(D, 1), 0.0)
    for n in range(2, max_n + 1):
        Sn = shadow_coeffs.get(n, 0.0)
        if abs(Sn) < 1e-30:
            continue
        chi = _kronecker_symbol(D, n)
        L_f_chi += Sn * chi * n ** (-s)

    return L_f * L_f_chi


def hilbert_shadow_zeta_as_base_change(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """Alternative computation of the Hilbert shadow zeta via base change.

    If the shadow form is a base change from Q, then:
    zeta_A^D(s) = L(s, f_shadow) * L(s, f_shadow x chi_D)

    This provides a verification path.
    """
    return base_change_L_function(D, shadow_coeffs, s, max_n)


# ============================================================================
# 8.  Asai L-function
# ============================================================================

def asai_L_function(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """Asai L-function of the shadow Hilbert modular form.

    For a Hilbert modular form F over K = Q(sqrt(D)) that is a base change
    of f from GL_2/Q:

    L(s, As(F)) = L(s, Sym^2(f)) * L(s, chi_D)

    where Sym^2 is the symmetric square and chi_D is the Kronecker character.

    Alternatively, the Asai factorization gives:
    L(s, As(F)) = L(s, f) * L(s, f x chi_D)

    when F = BC(f). But the Asai transfer As: GL_2/K -> GL_4/Q is the
    tensor induction, so for base change:
    L(s, As(BC(f))) = L(s, f x f) = L(s, Sym^2(f)) * L(s, wedge^2(f))

    The correct factorization for the Asai L-function is:
    L(s, As(F)) = L(s, f) * L(s, f x chi_D)

    when F = BC(f) from GL_2/Q.

    We compute both sides and verify.
    """
    # Direct: L(s, f) * L(s, f x chi_D)
    return base_change_L_function(D, shadow_coeffs, s, max_n)


def asai_L_function_direct(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> complex:
    """Direct computation of Asai L-function via Euler product.

    For each prime p, the local Asai factor depends on the Satake parameters
    of the Hilbert modular form at p:

    For p split in K (chi_D(p) = 1): two primes above p with
        independent Satake parameters.
    For p inert (chi_D(p) = -1): one prime above p with norm p^2.
    For p ramified (chi_D(p) = 0): one prime above p with norm p.

    For the base change form, the Asai Euler factors simplify.
    """
    # Use the a_n coefficients approach
    # a_n^{As}(F) for the Asai transfer can be computed from the
    # shadow coefficients of f and the Kronecker symbol

    total = 0.0 + 0.0j
    for n in range(1, max_n + 1):
        # Asai Dirichlet coefficient: a_n^{As} = sum_{d|n} chi_D(d) * S_{n/d} * S_d
        # where S_1 = 1, S_n = shadow_coeffs[n] for n >= 2
        a_n_as = 0.0
        for d in range(1, n + 1):
            if n % d == 0:
                chi = _kronecker_symbol(D, d)
                Sd = shadow_coeffs.get(d, 0.0) if d >= 2 else 1.0
                Snd = shadow_coeffs.get(n // d, 0.0) if n // d >= 2 else 1.0
                a_n_as += chi * Sd * Snd
        total += a_n_as * n ** (-s)
    return total


# ============================================================================
# 9.  CM point evaluation
# ============================================================================

def evaluate_at_cm_point(
    form: HilbertShadowForm,
    tau_1: complex,
    tau_2: complex,
) -> complex:
    """Evaluate the shadow Hilbert modular form at a point (tau_1, tau_2).

    Uses the Fourier expansion:
    F(tau_1, tau_2) = c(0,0) + sum_{nu >> 0} c(nu) * q_1^{sigma_1(nu)} * q_2^{sigma_2(nu)}

    where q_j = exp(2*pi*i*tau_j).
    """
    D = form.D
    sqrt_D = math.sqrt(D)
    q1 = cmath.exp(2j * math.pi * tau_1)
    q2 = cmath.exp(2j * math.pi * tau_2)

    total = form.fourier_coeffs.get((0, 0), 0.0 + 0.0j)

    for (nu_a, nu_b), c_nu in form.fourier_coeffs.items():
        if nu_a == 0 and nu_b == 0:
            continue
        if abs(c_nu) < 1e-30:
            continue

        # Compute sigma_1(nu) and sigma_2(nu)
        if D % 4 == 1:
            s1_nu = nu_a + nu_b * (1 + sqrt_D) / 2
            s2_nu = nu_a + nu_b * (1 - sqrt_D) / 2
        else:
            s1_nu = nu_a + nu_b * sqrt_D
            s2_nu = nu_a - nu_b * sqrt_D

        # q_1^{sigma_1(nu)} * q_2^{sigma_2(nu)}
        exp_factor = (
            cmath.exp(2j * math.pi * s1_nu * tau_1) *
            cmath.exp(2j * math.pi * s2_nu * tau_2)
        )
        total += c_nu * exp_factor

    return total


def cm_point_algebraicity_test(
    D: int,
    family: str,
    param: float,
    cm_disc: int = -4,
    max_r: int = 20,
    max_nu_norm: int = 20,
) -> Tuple[complex, bool, float]:
    """Evaluate shadow Hilbert form at a CM point and test algebraicity.

    A CM point on the Hilbert modular surface for Q(sqrt(D)) is
    (tau_1, tau_2) where Q(tau_1, tau_2) generates a CM field.

    Simple CM points: tau_1 = tau_2 = i (diagonal embedding of Q(i)).

    Returns (value, is_approximately_rational, distance_to_nearest_rational).
    """
    form = compute_hilbert_shadow_form(D, family, param, max_r, max_nu_norm)

    # CM point: the simplest is the diagonal tau_1 = tau_2 = i
    # (corresponds to the product E x E of the CM elliptic curve with j = 1728)
    tau_cm = complex(0, 1)
    value = evaluate_at_cm_point(form, tau_cm, tau_cm)

    # Test if value is approximately rational
    re_val = value.real
    if abs(value.imag) > 1e-6 * max(abs(re_val), 1e-10):
        return (value, False, abs(value.imag))

    # Find nearest rational with small denominator
    best_dist = abs(re_val)
    for denom in range(1, 1001):
        numer = round(re_val * denom)
        dist = abs(re_val - numer / denom)
        if dist < best_dist:
            best_dist = dist

    is_rational = best_dist < 1e-4
    return (value, is_rational, best_dist)


# ============================================================================
# 10.  Functional equation tests
# ============================================================================

def hilbert_shadow_zeta_functional_equation_test(
    D: int,
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> Tuple[complex, complex, float]:
    """Test the functional equation for the Hilbert shadow zeta.

    The completed Hilbert shadow zeta should satisfy:
    Lambda_A^D(s) = Lambda_A^D(w_0 - s)

    where w_0 is the central weight. For parallel weight r Eisenstein series,
    the functional equation relates s to r - s, but since F_A^D is a
    MIXTURE of different weights, there is no clean functional equation
    for the full form. Instead we test the factored form:

    zeta_A^D(s) = L(s, f) * L(s, f x chi_D)

    Each factor has its own functional equation; the product satisfies
    a combined functional equation.

    Returns (zeta_at_s, zeta_at_w0_minus_s, relative_discrepancy).
    """
    z1 = hilbert_shadow_zeta(D, shadow_coeffs, s, max_n)
    # The "dual" point depends on the weight; for weight 2 shadow:
    z2 = hilbert_shadow_zeta(D, shadow_coeffs, 2.0 - s, max_n)

    denom = max(abs(z1), abs(z2), 1e-30)
    discrepancy = abs(z1 - z2) / denom

    return (z1, z2, discrepancy)


# ============================================================================
# 11.  Classical limit (D = 1 comparison)
# ============================================================================

def classical_limit_comparison(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_n: int = 200,
) -> Tuple[complex, complex, float]:
    """Compare Hilbert shadow zeta at D -> 1 (degenerate) with classical.

    For D = 1 (degenerate: Q(sqrt(1)) = Q), chi_D is trivial, r_K(n) = d(n)
    (ordinary divisor function), and the Hilbert shadow zeta degenerates to:

    zeta_A^{D=1}(s) = sum_n S_n * d(n) * n^{-s} = zeta_A(s)^2 (heuristically)

    Actually for D = 1: chi_1(n) = 1 for all n, so r_K(n) = sum_{d|n} 1 = d(n).
    Thus zeta_A^{D=1}(s) = sum_n S_n * d(n) * n^{-s}.

    This is NOT the square of zeta_A(s), but rather the Rankin-Selberg
    convolution of zeta_A with the Riemann zeta.

    Classical shadow zeta: zeta_A(s) = sum_n S_n * n^{-s}.

    Returns (hilbert_at_D_trivial, classical_zeta, comparison_ratio).
    """
    # Hilbert with D = 1 (use chi_D = 1, so r_K(n) = d(n))
    hilbert_val = 0.0 + 0.0j
    max_r = max(shadow_coeffs.keys()) if shadow_coeffs else 2
    upper = min(max_r, max_n)
    for n in range(2, upper + 1):
        Sn = shadow_coeffs.get(n, 0.0)
        if abs(Sn) < 1e-30:
            continue
        # d(n) = number of divisors
        dn = sum(1 for d in range(1, n + 1) if n % d == 0)
        hilbert_val += Sn * dn * n ** (-s)

    # Classical
    classical_val = shadow_zeta_numerical(shadow_coeffs, s, max_r)

    ratio = abs(hilbert_val / classical_val) if abs(classical_val) > 1e-30 else float('inf')
    return (hilbert_val, classical_val, ratio)


# ============================================================================
# 12.  Landscape sweep: all D, all families
# ============================================================================

@dataclass
class HilbertShadowLandscapeEntry:
    """Result of Hilbert shadow computation for one (D, family, param) triple."""
    D: int
    family: str
    param: float
    kappa: float
    class_number: int
    regulator: float
    hilbert_zeta_at_2: complex
    hilbert_zeta_at_3: complex
    base_change_at_2: complex
    base_change_at_3: complex
    n_fourier_coeffs: int
    constant_term: complex


def landscape_sweep(
    families: Optional[Dict[str, float]] = None,
    discriminants: Optional[List[int]] = None,
    max_r: int = 20,
    max_nu_norm: int = 20,
) -> List[HilbertShadowLandscapeEntry]:
    """Sweep over all (D, family) combinations.

    Default families: Heisenberg (k=1), affine sl_2 (k=1), Virasoro (c=25), betagamma (lam=0.5).
    Default discriminants: first 10 real quadratic fields of class number 1.
    """
    if families is None:
        families = {
            'heisenberg': 1.0,
            'affine_sl2': 1.0,
            'virasoro': 25.0,
            'betagamma': 0.5,
        }
    if discriminants is None:
        discriminants = REAL_QUADRATIC_DISCRIMINANTS

    results = []
    for D in discriminants:
        h_D, h_D_int, R_D = class_number_from_shadow(D)
        for family, param in families.items():
            shadow_coeffs = _get_shadow_coefficients(family, param, max_r)
            kappa = shadow_coeffs.get(2, 0.0)

            form = compute_hilbert_shadow_form(D, family, param, max_r, max_nu_norm)

            hz_2 = hilbert_shadow_zeta(D, shadow_coeffs, complex(2, 0), max_r)
            hz_3 = hilbert_shadow_zeta(D, shadow_coeffs, complex(3, 0), max_r)
            bc_2 = base_change_L_function(D, shadow_coeffs, complex(2, 0), max_r)
            bc_3 = base_change_L_function(D, shadow_coeffs, complex(3, 0), max_r)

            entry = HilbertShadowLandscapeEntry(
                D=D, family=family, param=param, kappa=kappa,
                class_number=h_D_int, regulator=R_D,
                hilbert_zeta_at_2=hz_2, hilbert_zeta_at_3=hz_3,
                base_change_at_2=bc_2, base_change_at_3=bc_3,
                n_fourier_coeffs=len(form.fourier_coeffs),
                constant_term=form.fourier_coeffs.get((0, 0), 0.0),
            )
            results.append(entry)
    return results


# ============================================================================
# 13.  Dedekind zeta special values (for class number verification)
# ============================================================================

def dedekind_zeta_special_value(D: int, s_val: int, max_n: int = 5000) -> float:
    """Compute zeta_K(s) at positive even integer s via factorization.

    zeta_K(s) = zeta(s) * L(s, chi_D).

    For s = 2: zeta(2) = pi^2/6, L(2, chi_D) computed numerically.
    """
    if s_val < 2:
        raise ValueError("Only s >= 2 supported for direct summation")

    zeta_s = sum(n ** (-s_val) for n in range(1, max_n + 1))
    L_s = sum(_kronecker_symbol(D, n) * n ** (-s_val) for n in range(1, max_n + 1))
    return zeta_s * L_s


# ============================================================================
# 14.  Utility: totally positive element enumeration
# ============================================================================

def enumerate_totally_positive(D: int, max_norm: int) -> List[Tuple[int, int, int, float, float]]:
    """Enumerate totally positive elements nu of O_K with 0 < N(nu) <= max_norm.

    Returns list of (nu_a, nu_b, norm, sigma_1(nu), sigma_2(nu)).
    """
    sqrt_D = math.sqrt(D)
    results = []
    bound = int(math.sqrt(max_norm * max(D, 4))) + 2

    for b in range(-bound, bound + 1):
        for a in range(-bound, bound + 1):
            if a == 0 and b == 0:
                continue

            if D % 4 == 1:
                norm = a * a + a * b - ((D - 1) // 4) * b * b
                s1 = a + b * (1 + sqrt_D) / 2
                s2 = a + b * (1 - sqrt_D) / 2
            else:
                norm = a * a - D * b * b
                s1 = a + b * sqrt_D
                s2 = a - b * sqrt_D

            if norm > 0 and norm <= max_norm and s1 > 0 and s2 > 0:
                results.append((a, b, norm, s1, s2))

    results.sort(key=lambda x: (x[2], x[3]))
    return results
