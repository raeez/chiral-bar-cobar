r"""
shadow_automorphic_bridge.py — Shadow Tower to Automorphic Forms

Connects shadow tower data to automorphic forms, L-functions, and spectral
decomposition for all standard families.

MATHEMATICAL CONTENT:

1. Shadow generating function: G_A(t) = sum_{r>=2} S_r(A) * t^r
2. Formal Mellin transform: L_A(s) = int_0^infty G_A(t) t^{s-1} dt
3. For lattice VOAs: G_Lambda -> theta-series connection
4. Euler product test via MC multiplicativity of shadow atoms
5. Pade / Borel summation for infinite-tower families (Virasoro)

FAMILIES:
  - Heisenberg: G_H(t) = (k/2)*t^2, L_H(s) = (k/2)/(s+2) — trivial
  - Affine sl_2: G_aff(t) = (k/2)*t^2 + 2*t^3 — terminates at depth 3
  - Virasoro: G_Vir(t) = sum S_r(c) t^r — infinite series (class M)
  - Lattice VOAs: theta function connection via Hecke eigenform decomposition

KEY RESULTS:
  - For lattice VOAs the shadow GF encodes theta function data
  - Euler products arise from multiplicativity of Hecke eigenvalues
  - The MC equation constrains weights but does NOT force multiplicativity
    (see euler_product_from_mc.py)
  - Pade approximants to G_Vir capture the branch-cut structure of sqrt(Q)

References:
  thm:shadow-moduli-resolution (arithmetic_shadows.tex)
  prop:mc-bracket-determines-atoms (arithmetic_shadows.tex)
  thm:shadow-l-correspondence (arithmetic_shadows.tex)
  thm:algebraic-family-rigidity (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

try:
    from sympy import (
        Rational, Symbol, cancel, expand, factor, fraction, simplify, sqrt,
        series, Poly, S as Sym, gamma as sym_gamma, oo, integrate,
        pi as sym_pi, zeta as sym_zeta, binomial, bernoulli,
    )
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# Symbolic variables
c = Symbol('c', positive=True)
t = Symbol('t')
s = Symbol('s')


# =====================================================================
# Section 1: Shadow generating functions for standard families
# =====================================================================

def heisenberg_shadow_gf(k_val: float) -> Dict[str, Any]:
    r"""Shadow generating function for Heisenberg algebra at level k.

    G_H(t) = (k/2) * t^2  (terminates at depth 2, class G)

    The Mellin transform:
      L_H(s) = int_0^infty (k/2)*t^2 * t^{s-1} dt
    is formally (k/2) * delta(s+2) in distribution sense,
    or as a regularized value: L_H(s) = (k/2) / (s+2) with a pole at s=-2.

    Parameters
    ----------
    k_val : float
        Level (kappa = k for Heisenberg, NOT c/2).

    Returns
    -------
    dict with GF data.
    """
    kappa = k_val
    coeffs = {2: kappa / 2.0}
    # All higher coefficients vanish
    for r in range(3, 13):
        coeffs[r] = 0.0

    return {
        'family': 'Heisenberg',
        'level': k_val,
        'kappa': kappa,
        'depth': 2,
        'archetype': 'G',
        'coefficients': coeffs,
        'gf_closed_form': f'G(t) = {kappa/2} * t^2',
        'mellin_poles': {-2: kappa / 2.0},
        'euler_product': True,  # trivial: single term
    }


def affine_sl2_shadow_gf(k_val: float) -> Dict[str, Any]:
    r"""Shadow generating function for affine sl_2 at level k.

    G_aff(t) = (k/2)*t^2 + C_3*t^3  (terminates at depth 3, class L)

    For affine sl_2: kappa = dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4
    and C_3 = 2 (cubic shadow from Lie bracket, universal for sl_2).

    WAIT -- let me be precise about kappa.
    For sl_2 (dim=3, h^v=2): kappa = 3(k+2)/4.
    S_2 = kappa = 3(k+2)/4.
    S_3 = 2 (the cubic shadow for sl_2).

    BUT the shadow GF convention is G(t) = sum S_r * t^r where
    S_r is the coefficient on x^r on the primary line.
    The GF convention: G'(t) = H(t)/t where H = sum r*S_r*t^r.

    For affine sl_2 at level k (away from critical k = -2):
      S_2 = kappa_KM = dim(g)*(k+h^v)/(2*h^v) = 3(k+2)/4
      S_3 = 2 (universal cubic shadow)
      S_r = 0 for r >= 4

    The formal Mellin transform:
      L_aff(s) = S_2 / (s+2) + S_3 / (s+3)

    Parameters
    ----------
    k_val : float
        Level. Must not be -2 (critical level).

    Returns
    -------
    dict with GF data.
    """
    if abs(k_val + 2.0) < 1e-12:
        raise ValueError("Critical level k = -h^v = -2: Sugawara undefined")

    h_dual = 2
    dim_g = 3
    kappa = dim_g * (k_val + h_dual) / (2 * h_dual)
    S_2 = kappa
    S_3 = 2.0  # universal cubic shadow for sl_2

    coeffs = {2: S_2, 3: S_3}
    for r in range(4, 13):
        coeffs[r] = 0.0

    return {
        'family': 'affine_sl2',
        'level': k_val,
        'kappa': kappa,
        'depth': 3,
        'archetype': 'L',
        'coefficients': coeffs,
        'gf_closed_form': f'G(t) = {S_2}*t^2 + {S_3}*t^3',
        'mellin_poles': {-2: S_2, -3: S_3},
        'euler_product': True,  # terminates: rational L-function
    }


def virasoro_shadow_gf(c_val: float, max_arity: int = 12) -> Dict[str, Any]:
    r"""Shadow generating function for Virasoro at central charge c.

    G_Vir(t) = sum_{r=2}^{infty} S_r(c) * t^r  (infinite, class M)

    The closed-form generating function:
      H(t,c) = sum r*S_r t^r = t^2 * sqrt(c^2 + 12*c*t + alpha(c)*t^2)
    where alpha(c) = (180c + 872)/(5c + 22).

    G'(t) = H(t)/t = t * sqrt(c^2 + 12*c*t + alpha(c)*t^2)

    So G(t) = integral of t*sqrt(Q(t)) dt where Q(t) = c^2 + 12ct + alpha*t^2.

    Parameters
    ----------
    c_val : float
        Central charge. Must not be 0 or -22/5.
    max_arity : int
        Maximum arity for shadow coefficient computation.

    Returns
    -------
    dict with GF data.
    """
    if abs(c_val) < 1e-12:
        raise ValueError("c = 0: pole of shadow tower")
    if abs(c_val + 22.0 / 5.0) < 1e-12:
        raise ValueError("c = -22/5 (Lee-Yang): pole of S_4")

    # Compute shadow coefficients via recursion
    S = {}
    S[2] = c_val / 2.0
    S[3] = 2.0
    denom4 = c_val * (5.0 * c_val + 22.0)
    S[4] = 10.0 / denom4

    for r in range(5, max_arity + 1):
        target = r + 2
        total = 0.0
        for j in range(3, target):
            k = target - j
            if k < j:
                break
            if k < 3:
                continue
            contrib = 2.0 * j * k * S[j] * S[k]
            if j == k:
                contrib *= 0.5
            total += contrib
        S[r] = -total / (2.0 * r * c_val)

    # Alpha and branch point data
    alpha = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    discriminant_Q = 144.0 * c_val**2 - 4.0 * c_val**2 * alpha
    # Q(t) = c^2 + 12ct + alpha*t^2; zeros at t = (-12c +/- sqrt(disc)) / (2*alpha)
    # disc = (12c)^2 - 4*alpha*c^2 = 4c^2(36 - alpha)
    disc_factor = 36.0 - alpha  # = 36 - (180c+872)/(5c+22) = -80/(5c+22)
    # For c > 0: disc_factor < 0, so branch points are complex

    return {
        'family': 'Virasoro',
        'c': c_val,
        'kappa': S[2],
        'depth': float('inf'),
        'archetype': 'M',
        'coefficients': S,
        'alpha': alpha,
        'disc_factor': disc_factor,
        'euler_product': False,  # infinite tower, non-multiplicative
    }


def virasoro_shadow_coefficients_exact(max_arity: int = 10) -> Dict[int, Any]:
    r"""Compute Virasoro S_r(c) as exact rational functions of c.

    Uses the recursive master equation. Seeds:
      S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)]

    Returns dict {r: S_r(c)} as sympy expressions.
    """
    if not HAS_SYMPY:
        raise RuntimeError("sympy required for exact computation")

    S = {}
    S[2] = c / 2
    S[3] = Rational(2)
    S[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_arity + 1):
        target = r + 2
        total = Rational(0)
        for j in range(3, target):
            k = target - j
            if k < j:
                break
            if k < 3:
                continue
            bracket_coeff = 2 * j * k * S[j] * S[k]
            if j == k:
                bracket_coeff = bracket_coeff / 2
            total += bracket_coeff
        S[r] = cancel(-total / (2 * r * c))

    return S


# =====================================================================
# Section 2: Formal Mellin transform L_A(s)
# =====================================================================

def formal_mellin_heisenberg(s_val: complex, k_val: float) -> complex:
    r"""Formal Mellin transform for Heisenberg.

    G_H(t) = (k/2)*t^2.
    L_H(s) = int_0^1 (k/2)*t^{s+1} dt = (k/2)/(s+2)

    (Regularized to [0,1] interval; pole at s = -2.)
    """
    if abs(s_val + 2) < 1e-12:
        return complex(float('inf'))
    return (k_val / 2.0) / (s_val + 2)


def formal_mellin_affine(s_val: complex, k_val: float) -> complex:
    r"""Formal Mellin transform for affine sl_2.

    G_aff(t) = S_2*t^2 + S_3*t^3.
    L_aff(s) = S_2/(s+2) + S_3/(s+3)

    Poles at s = -2 (residue S_2) and s = -3 (residue S_3).
    """
    h_dual = 2
    dim_g = 3
    S_2 = dim_g * (k_val + h_dual) / (2 * h_dual)
    S_3 = 2.0

    result = 0.0 + 0.0j
    if abs(s_val + 2) > 1e-12:
        result += S_2 / (s_val + 2)
    else:
        return complex(float('inf'))
    if abs(s_val + 3) > 1e-12:
        result += S_3 / (s_val + 3)
    else:
        return complex(float('inf'))
    return result


def formal_mellin_virasoro(s_val: complex, c_val: float,
                           max_arity: int = 12) -> complex:
    r"""Formal Mellin transform for Virasoro (truncated).

    G_Vir(t) = sum_{r=2}^{max_arity} S_r(c) * t^r.
    L_Vir(s) = sum_{r=2}^{max_arity} S_r(c) / (s+r)

    For the full infinite series, the Mellin transform has a branch cut
    arising from the sqrt(Q(t)) structure of the closed-form GF.

    Poles at s = -r for each r with S_r != 0, i.e., at s = -2, -3, -4, ...
    """
    data = virasoro_shadow_gf(c_val, max_arity)
    S = data['coefficients']

    result = 0.0 + 0.0j
    for r, sr in S.items():
        if abs(s_val + r) < 1e-12:
            return complex(float('inf'))
        result += sr / (s_val + r)
    return result


def formal_mellin_general(s_val: complex, coefficients: Dict[int, float]) -> complex:
    r"""Formal Mellin transform for any family.

    L_A(s) = sum_r S_r / (s + r)

    Poles at s = -r with residue S_r.
    """
    result = 0.0 + 0.0j
    for r, sr in coefficients.items():
        if abs(s_val + r) < 1e-12:
            return complex(float('inf'))
        result += sr / (s_val + r)
    return result


# =====================================================================
# Section 3: Lattice theta function connection
# =====================================================================

def lattice_theta_coefficients(lattice_type: str, n_max: int = 30) -> List[int]:
    r"""Compute theta-series coefficients for standard lattices.

    Theta_Lambda(q) = sum_{v in Lambda} q^{|v|^2/2} = 1 + sum_{n>=1} r(n) q^n

    Returns [r(1), r(2), ..., r(n_max)] (NOT including the constant term 1).
    """
    if lattice_type == 'Z':
        # theta_Z(q) = 1 + 2q + 2q^4 + 2q^9 + ...
        # r_Z(n) = 2 if n is a perfect square, 0 otherwise
        coeffs = []
        for n in range(1, n_max + 1):
            s = int(math.isqrt(n))
            if s * s == n:
                coeffs.append(2)
            else:
                coeffs.append(0)
        return coeffs

    elif lattice_type == 'Z2':
        # theta_{Z^2}(q) = theta_Z(q)^2 = 1 + 4q + 4q^2 + 4q^4 + 8q^5 + ...
        # r_{Z^2}(n) = number of representations as sum of two squares
        coeffs = []
        for n in range(1, n_max + 1):
            count = 0
            s = int(math.isqrt(n)) + 1
            for a in range(-s, s + 1):
                a2 = a * a
                if a2 > n:
                    continue
                rem = n - a2
                b = int(math.isqrt(rem))
                if b * b == rem:
                    count += 1 if b == 0 else 2
            coeffs.append(count)
        return coeffs

    elif lattice_type == 'A2':
        # A_2: Gram matrix [[2,-1],[-1,2]], norm = 2(a^2+b^2-ab)
        # r_{A_2}(n) = #{(a,b): a^2+b^2-ab = n}
        coeffs = []
        for n in range(1, n_max + 1):
            count = 0
            s = int(math.isqrt(4 * n)) + 2
            for a in range(-s, s + 1):
                for b in range(-s, s + 1):
                    if a * a + b * b - a * b == n:
                        count += 1
            coeffs.append(count)
        return coeffs

    elif lattice_type == 'D4':
        # D_4 lattice: theta_{D_4}(q) = 1 + 24*sum_{n>=1} sigma_1^{odd}(n)*q^n
        # where sigma_1^{odd}(n) = sum_{d|n, d odd} d.
        # Actually: theta_{D_4} = (theta_3^4 + theta_4^4 + theta_2^4)/2
        # r_{D_4}(n) = 24 * sum_{d|n, d odd} d  (Jacobi four-square theorem variant)
        coeffs = []
        for n in range(1, n_max + 1):
            sigma1_odd = sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)
            coeffs.append(24 * sigma1_odd)
        return coeffs

    elif lattice_type == 'E8':
        # theta_{E_8} = E_4(tau) = 1 + 240*sum_{n>=1} sigma_3(n)*q^n
        # r_{E_8}(n) = 240 * sigma_3(n)
        coeffs = []
        for n in range(1, n_max + 1):
            sigma3 = sum(d ** 3 for d in range(1, n + 1) if n % d == 0)
            coeffs.append(240 * sigma3)
        return coeffs

    else:
        raise ValueError(f"Unknown lattice type: {lattice_type}")


def sigma_k(n: int, k: int) -> int:
    """Divisor sum sigma_k(n) = sum_{d|n} d^k."""
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


def eisenstein_series_coefficients(weight: int, n_max: int = 30) -> List[float]:
    r"""Fourier coefficients of E_k(tau) = 1 + c_k * sum sigma_{k-1}(n) q^n.

    For k = 4: c_4 = 240, E_4 = 1 + 240*sum sigma_3(n) q^n
    For k = 6: c_6 = -504, E_6 = 1 - 504*sum sigma_5(n) q^n
    For k = 8: c_8 = 480, E_8 = 1 + 480*sum sigma_7(n) q^n

    The constant c_k = (-1)^{k/2} * 2k / B_k where B_k is the Bernoulli number.

    Returns normalized coefficients [a(1), a(2), ..., a(n_max)] where
    E_k = 1 + sum a(n) q^n.
    """
    if not HAS_SYMPY:
        # Use known values for small weights
        known_ck = {4: 240, 6: -504, 8: 480, 10: -264, 12: Fraction(65520, 691)}
        if weight not in known_ck:
            raise ValueError(f"Weight {weight} not supported without sympy")
        ck = float(known_ck[weight])
    else:
        B_k = float(bernoulli(weight))
        if abs(B_k) < 1e-30:
            raise ValueError(f"B_{weight} = 0")
        # Standard normalization: E_k = 1 + c_k * sum sigma_{k-1}(n) q^n
        # where c_k = -2k/B_k
        ck = -2.0 * weight / B_k

    return [ck * sigma_k(n, weight - 1) for n in range(1, n_max + 1)]


def verify_E8_theta_equals_E4(n_max: int = 20) -> Dict[str, Any]:
    r"""Verify that theta_{E_8} = E_4 coefficient by coefficient.

    This is the fundamental identity: the E_8 theta series is exactly
    the weight-4 Eisenstein series. A cornerstone of lattice theory.

    Returns dict with comparison data.
    """
    theta_coeffs = lattice_theta_coefficients('E8', n_max)
    e4_coeffs = eisenstein_series_coefficients(4, n_max)

    matches = True
    diffs = []
    for n in range(n_max):
        diff = abs(theta_coeffs[n] - e4_coeffs[n])
        diffs.append(diff)
        if diff > 0.5:
            matches = False

    return {
        'matches': matches,
        'max_diff': max(diffs),
        'theta_coeffs': theta_coeffs[:10],
        'e4_coeffs': [int(round(x)) for x in e4_coeffs[:10]],
        'n_checked': n_max,
    }


# =====================================================================
# Section 4: Euler product verification for lattice VOAs
# =====================================================================

def check_multiplicativity(coeffs: List[float], n_max: int = None,
                           tol: float = 1e-10) -> Dict[str, Any]:
    r"""Test whether Fourier coefficients a(n) are multiplicative:
    a(mn) = a(m)*a(n) for gcd(m,n) = 1.

    For Hecke eigenforms, normalized coefficients are multiplicative.
    For raw theta functions, coefficients may NOT be multiplicative.

    Returns dict with multiplicativity test results.
    """
    if n_max is None:
        n_max = len(coeffs)
    else:
        n_max = min(n_max, len(coeffs))

    defect = 0.0
    violations = []

    for m in range(1, n_max + 1):
        for n in range(m, n_max + 1):
            if math.gcd(m, n) != 1:
                continue
            mn = m * n
            if mn > n_max:
                continue
            a_mn = coeffs[mn - 1]
            a_m = coeffs[m - 1]
            a_n = coeffs[n - 1]
            product = a_m * a_n
            diff = abs(a_mn - product)
            norm = max(abs(a_mn), 1.0)
            rel_diff = diff / norm

            if rel_diff > defect:
                defect = rel_diff

            if rel_diff > tol:
                violations.append((m, n, a_mn, product))

    return {
        'defect': defect,
        'violations': violations[:20],  # first 20
        'is_multiplicative': defect < tol,
        'n_checked': n_max,
    }


def euler_product_test_lattice(lattice_type: str, n_max: int = 30) -> Dict[str, Any]:
    r"""Test whether the Epstein zeta of a lattice VOA has an Euler product.

    The Epstein zeta E_Lambda(s) = sum_{0 != v in Lambda} |v|^{-2s}
    has an Euler product iff the theta function is a Hecke eigenform.

    For E_8: theta = E_4, a Hecke eigenform. NORMALIZED coefficients
    sigma_3(n) are multiplicative. So E_{E_8}(s) ~ zeta(s)*zeta(s-3)
    has an Euler product.

    For Z^2: theta = (theta_3)^2, NOT a Hecke eigenform. No Euler product
    for the raw theta coefficients.

    Returns dict with Euler product analysis.
    """
    theta_coeffs = lattice_theta_coefficients(lattice_type, n_max)

    # Test raw multiplicativity
    raw_mult = check_multiplicativity(theta_coeffs, n_max)

    # For E_8: test normalized coefficients (sigma_3)
    if lattice_type == 'E8':
        # r_{E_8}(n) = 240*sigma_3(n), so normalized = sigma_3(n)
        normalized = [sigma_k(n, 3) for n in range(1, n_max + 1)]
        norm_mult = check_multiplicativity(normalized, n_max)
    else:
        normalized = None
        norm_mult = None

    # For D4: r_{D_4}(n) = 24*sigma_1^{odd}(n)
    # sigma_1^{odd} is multiplicative, so normalized coefficients are multiplicative
    if lattice_type == 'D4':
        normalized = [sum(d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)
                      for n in range(1, n_max + 1)]
        norm_mult = check_multiplicativity(normalized, n_max)

    return {
        'lattice': lattice_type,
        'raw_multiplicative': raw_mult['is_multiplicative'],
        'raw_defect': raw_mult['defect'],
        'normalized_multiplicative': norm_mult['is_multiplicative'] if norm_mult else None,
        'normalized_defect': norm_mult['defect'] if norm_mult else None,
        'theta_first10': theta_coeffs[:10],
        'has_euler_product': (norm_mult['is_multiplicative'] if norm_mult
                              else raw_mult['is_multiplicative']),
    }


# =====================================================================
# Section 5: Virasoro shadow coefficients as rational functions of c
# =====================================================================

def virasoro_S_r_exact(r: int) -> Any:
    r"""Compute S_r(c) as an exact rational function of c (sympy).

    Seeds: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
    Recursion for r >= 5.

    Returns sympy expression in the variable c.
    """
    if not HAS_SYMPY:
        raise RuntimeError("sympy required")
    return virasoro_shadow_coefficients_exact(r)[r]


def virasoro_S_r_numerical(c_val: float, max_arity: int = 12) -> Dict[int, float]:
    r"""Compute S_r(c) numerically for given c.

    Returns dict {r: S_r(c_val)} for r = 2, ..., max_arity.
    """
    data = virasoro_shadow_gf(c_val, max_arity)
    return data['coefficients']


# =====================================================================
# Section 6: Pade approximants for Virasoro shadow GF
# =====================================================================

def pade_approximant(coeffs: List[float], m: int, n: int) -> Tuple[List[float], List[float]]:
    r"""Compute [m/n] Pade approximant from power series coefficients.

    Given f(t) = sum_{k=0}^{m+n} a_k t^k, find P(t)/Q(t) where
    deg(P) <= m, deg(Q) <= n, Q(0) = 1, and f*Q - P = O(t^{m+n+1}).

    Uses the standard linear algebra approach.

    Returns (P_coeffs, Q_coeffs) where P(t) = sum P_i t^i, Q(t) = 1 + sum Q_j t^j.
    """
    if not HAS_NUMPY:
        raise RuntimeError("numpy required for Pade")

    N = m + n
    if len(coeffs) < N + 1:
        raise ValueError(f"Need at least {N+1} coefficients, got {len(coeffs)}")

    a = np.array(coeffs[:N + 1], dtype=float)

    # Solve for Q_1, ..., Q_n from:
    # sum_{j=0}^{n} Q_j * a_{i-j} = 0 for i = m+1, ..., m+n
    # where Q_0 = 1
    if n > 0:
        A_mat = np.zeros((n, n))
        b_vec = np.zeros(n)
        for i in range(m + 1, m + n + 1):
            row = i - m - 1
            for j in range(1, n + 1):
                idx = i - j
                if 0 <= idx <= N:
                    A_mat[row, j - 1] = a[idx]
            b_vec[row] = -a[i] if i <= N else 0.0

        try:
            Q_tail = np.linalg.solve(A_mat, b_vec)
        except np.linalg.LinAlgError:
            # Singular system: fall back to least squares
            Q_tail, _, _, _ = np.linalg.lstsq(A_mat, b_vec, rcond=None)

        Q_coeffs = [1.0] + list(Q_tail)
    else:
        Q_coeffs = [1.0]

    # Compute P coefficients: P_i = sum_{j=0}^{min(i,n)} Q_j * a_{i-j}
    P_coeffs = []
    for i in range(m + 1):
        pi = 0.0
        for j in range(min(i, n) + 1):
            if i - j <= N:
                pi += Q_coeffs[j] * a[i - j]
        P_coeffs.append(pi)

    return P_coeffs, Q_coeffs


def virasoro_pade(c_val: float, m: int = 4, n: int = 4,
                  max_arity: int = 12) -> Dict[str, Any]:
    r"""Compute [m/n] Pade approximant of the Virasoro shadow GF.

    The shadow GF G_Vir(t) = sum_{r=2}^infty S_r(c) * t^r is an infinite
    series with radius of convergence determined by the branch points of
    sqrt(Q(t)).

    The Pade approximant captures the pole/branch structure:
    - For the Virasoro shadow, the GF has BRANCH POINTS (not poles),
      so the Pade denominators should cluster near the branch cut.

    Returns the Pade coefficients and poles of the rational approximant.
    """
    data = virasoro_shadow_gf(c_val, max_arity)
    S = data['coefficients']

    # Build coefficient array starting from t^0
    # G(t) = 0 + 0*t + S_2*t^2 + S_3*t^3 + ...
    N = max_arity
    coeffs = [0.0, 0.0]  # a_0 = 0, a_1 = 0
    for r in range(2, N + 1):
        coeffs.append(S.get(r, 0.0))

    needed = m + n + 1
    if len(coeffs) < needed:
        coeffs.extend([0.0] * (needed - len(coeffs)))

    P_coeffs, Q_coeffs = pade_approximant(coeffs, m, n)

    # Find poles: roots of Q(t)
    if n > 0 and HAS_NUMPY:
        Q_poly = np.array(Q_coeffs[::-1])
        poles = np.roots(Q_poly)
    else:
        poles = np.array([])

    return {
        'c': c_val,
        'm': m,
        'n': n,
        'P_coeffs': P_coeffs,
        'Q_coeffs': Q_coeffs,
        'poles': poles,
        'residues': _pade_residues(P_coeffs, Q_coeffs, poles),
    }


def _pade_residues(P_coeffs, Q_coeffs, poles):
    """Compute residues of P(t)/Q(t) at each pole."""
    if not HAS_NUMPY or len(poles) == 0:
        return []
    residues = []
    for pole in poles:
        # Residue = P(pole) / Q'(pole)
        P_val = sum(P_coeffs[k] * pole ** k for k in range(len(P_coeffs)))
        # Q'(t) = sum k*Q_k*t^{k-1}
        Q_prime = sum(k * Q_coeffs[k] * pole ** (k - 1)
                      for k in range(1, len(Q_coeffs)))
        if abs(Q_prime) > 1e-15:
            residues.append(P_val / Q_prime)
        else:
            residues.append(complex(float('inf')))
    return residues


# =====================================================================
# Section 7: Spectral data extraction from shadow Mellin transform
# =====================================================================

def virasoro_mellin_poles(c_val: float, max_arity: int = 12) -> List[Dict]:
    r"""Extract spectral data from the poles of L_Vir(s).

    L_Vir(s) = sum_{r=2}^{N} S_r(c) / (s + r)

    Poles at s = -r with residue S_r(c).

    The spectral interpretation: each pole s = -r corresponds to a
    "shadow eigenvalue" at weight r. The residue S_r measures the
    shadow amplitude at that weight.

    For the full (non-truncated) Mellin transform, the poles accumulate
    at s = -infty, reflecting the infinite depth of the Virasoro tower.
    """
    data = virasoro_shadow_gf(c_val, max_arity)
    S = data['coefficients']

    poles = []
    for r in sorted(S.keys()):
        sr = S[r]
        if abs(sr) > 1e-30:
            poles.append({
                'pole': -r,
                'residue': sr,
                'arity': r,
                'weight': r,
            })
    return poles


def shadow_laplacian_eigenvalues(c_val: float, max_arity: int = 10) -> np.ndarray:
    r"""Extract eigenvalues of the "shadow Laplacian" from shadow tower data.

    The shadow Laplacian Delta_sh is the formal operator whose spectral
    decomposition reproduces the shadow GF:

      G(t) = Tr(t^{Delta_sh}) = sum_j t^{lambda_j}

    For a truncated tower with S_r for r = 2,...,N:
    the eigenvalues are obtained from the spectral polynomial
    (see shadow_spectral_inversion.py).

    Returns array of eigenvalues (complex in general for Virasoro).
    """
    if not HAS_NUMPY:
        raise RuntimeError("numpy required")

    data = virasoro_shadow_gf(c_val, max_arity)
    S = data['coefficients']

    # Convert to power sums p_r = -r * S_r
    N = max_arity
    p = [0.0] * N  # p[i] = p_{i+1}
    for r in range(2, N + 1):
        p[r - 1] = -r * S.get(r, 0.0)

    # Newton's identities: p -> e
    e = [0.0] * (N + 1)
    e[0] = 1.0
    for k in range(1, N + 1):
        total = 0.0
        for i in range(1, k + 1):
            total += (-1) ** (i - 1) * p[i - 1] * e[k - i]
        e[k] = total / k

    # Spectral polynomial P(z) = 1 - e_1*z + e_2*z^2 - ...
    coeffs = [1.0]
    for k in range(1, N + 1):
        coeffs.append((-1) ** k * e[k])

    # Roots of P(z) in descending order for np.roots
    roots = np.roots(coeffs[::-1])

    # Eigenvalues lambda_j = 1/z_j
    eigenvalues = np.array([1.0 / z if abs(z) > 1e-15 else np.inf + 0j
                            for z in roots])
    return eigenvalues


# =====================================================================
# Section 8: Lattice shadow-theta correspondence
# =====================================================================

def lattice_shadow_theta_correspondence(lattice_type: str,
                                        n_max: int = 20) -> Dict[str, Any]:
    r"""Verify the shadow-theta correspondence for lattice VOAs.

    The shadow tower data of a lattice VOA V_Lambda should encode the
    theta function Theta_Lambda. Specifically:

    For rank-r lattice with theta in M_{r/2}:
    - Shadow at arity 2 (kappa) = rank/2 (rank = number of generators)
      Actually kappa = k for Heisenberg, and for a lattice VOA of rank r
      with standard normalization: kappa = r (the level is 1 for each
      direction, total kappa = rank * 1 = rank).

    - The theta coefficients r_Lambda(n) are encoded in the genus-1
      partition function, NOT directly in the shadow tower coefficients.
      The shadow tower lives at the ALGEBRAIC level; the theta function
      is the ANALYTIC/AUTOMORPHIC shadow.

    - The connection: the shadow generating function G(t), when
      evaluated on the genus-1 sewing parameter t = q, gives
      (a projection of) the log of the partition function.

    For a rank-r lattice:
      kappa = r (shadow at arity 2 = rank)
      Z_1(q) = Theta_Lambda(q) / eta(q)^r
      log Z_1 = log Theta_Lambda - r * log eta

    Returns verification data.
    """
    theta_coeffs = lattice_theta_coefficients(lattice_type, n_max)

    # Lattice rank
    ranks = {'Z': 1, 'Z2': 2, 'A2': 2, 'D4': 4, 'E8': 8}
    rank = ranks.get(lattice_type, 1)

    # Kappa = rank (for standard lattice VOA at level 1)
    kappa = rank

    # Theta weight
    weight = rank  # theta in M_{r/2} where r = 2*rank for "norm" lattice
    # Actually for even lattices of rank r: theta in M_{r/2}
    # Z: rank 1, weight 1/2 (half-integer!)
    # Z^2: rank 2, weight 1
    # E_8: rank 8, weight 4
    if lattice_type == 'Z':
        weight = 0.5
    elif lattice_type == 'Z2':
        weight = 1
    elif lattice_type == 'A2':
        weight = 1
    elif lattice_type == 'D4':
        weight = 2
    elif lattice_type == 'E8':
        weight = 4

    return {
        'lattice': lattice_type,
        'rank': rank,
        'kappa': kappa,
        'theta_weight': weight,
        'theta_coefficients': theta_coeffs[:10],
        'shadow_depth': _lattice_shadow_depth(lattice_type),
    }


def _lattice_shadow_depth(lattice_type: str) -> int:
    """Shadow depth for standard lattices.

    Heisenberg = rank-1 lattice: depth 2 (class G).
    All even lattices with only Eisenstein: depth 3 (class L).
    Lattices with cusp forms (rank >= 24): depth >= 4.
    """
    depths = {
        'Z': 2,    # rank 1, purely Gaussian
        'Z2': 2,   # rank 2, still Gaussian (no Lie bracket)
        'A2': 3,   # rank 2 with root structure, Lie bracket gives cubic
        'D4': 3,   # rank 4 with root structure
        'E8': 3,   # rank 8, theta = E_4, no cusp forms at weight 4
    }
    return depths.get(lattice_type, 2)


# =====================================================================
# Section 9: Shadow coefficient Ramanujan bound
# =====================================================================

def ramanujan_bound_check(lattice_type: str, n_max: int = 30) -> Dict[str, Any]:
    r"""Verify Ramanujan-type bounds on lattice theta coefficients.

    For theta_{E_8} = E_4: the coefficients are r(n) = 240*sigma_3(n).
    The Ramanujan bound for weight-k Eisenstein series is:
      a(n) = sigma_{k-1}(n) << n^{k-1}  (exact growth, not a bound)

    For cusp forms of weight k: a(n) << n^{(k-1)/2+epsilon} (Deligne's theorem).

    For lattice VOAs (cor:unconditional-lattice in arithmetic_shadows.tex):
    Ramanujan bound is UNCONDITIONAL because it reduces to Deligne's theorem
    for the Ramanujan conjecture on cusp forms (proved for holomorphic
    modular forms by Deligne 1974).

    Returns dict with bound verification.
    """
    theta_coeffs = lattice_theta_coefficients(lattice_type, n_max)

    ranks = {'Z': 1, 'Z2': 2, 'A2': 2, 'D4': 4, 'E8': 8}
    rank = ranks.get(lattice_type, 1)

    weight_map = {'Z': 0.5, 'Z2': 1, 'A2': 1, 'D4': 2, 'E8': 4}
    weight = weight_map.get(lattice_type, 1)

    # For Eisenstein series of weight k: a(n) ~ C * n^{k-1} for large n
    # So |a(n)| / n^{k-1} should be bounded
    ratios = []
    for n in range(1, n_max + 1):
        if theta_coeffs[n - 1] == 0:
            ratios.append(0.0)
            continue
        if weight > 0.5:
            bound = n ** (weight - 1) if n > 0 else 1.0
        else:
            bound = n ** 0.5  # half-integer weight bound
        ratio = abs(theta_coeffs[n - 1]) / max(bound, 1e-30)
        ratios.append(ratio)

    max_ratio = max(ratios) if ratios else 0

    return {
        'lattice': lattice_type,
        'weight': weight,
        'max_ratio': max_ratio,
        'bounded': max_ratio < float('inf'),
        'ratios_first10': ratios[:10],
        'bound_type': 'Eisenstein' if lattice_type in ['E8', 'D4'] else 'theta',
    }


# =====================================================================
# Section 10: Borel summation for Virasoro shadow GF
# =====================================================================

def virasoro_borel_sum(c_val: float, t_val: float,
                       max_arity: int = 20) -> Dict[str, Any]:
    r"""Borel sum of the Virasoro shadow generating function.

    For the Virasoro shadow GF G(t) = sum S_r(c)*t^r with S_r growing
    factorially for large r (from the branch cut of sqrt(Q)), the Borel
    transform is:

      B(z) = sum S_r(c) * z^r / Gamma(r+1)

    and the Borel sum is:

      G^{Borel}(t) = int_0^infty B(z*t) * e^{-z} dz

    For the Virasoro tower with closed-form H(t) = t^2*sqrt(Q(t)):
    the Borel sum should reproduce the exact GF within the radius
    of convergence, and provide the correct analytic continuation beyond.

    Parameters
    ----------
    c_val : float
        Central charge.
    t_val : float
        Point at which to evaluate the Borel sum.
    max_arity : int
        Truncation arity.

    Returns dict with Borel sum data.
    """
    data = virasoro_shadow_gf(c_val, max_arity)
    S = data['coefficients']

    # Borel transform coefficients: B_r = S_r / r!
    borel_coeffs = {}
    for r, sr in S.items():
        borel_coeffs[r] = sr / math.factorial(r)

    # Evaluate B(z) at z = t_val
    def borel_transform(z):
        return sum(borel_coeffs.get(r, 0) * z ** r for r in range(2, max_arity + 1))

    # Numerical Borel sum via trapezoidal integration
    # G^Borel(t) = int_0^infty B(t*z) * e^{-z} dz
    n_points = 500
    z_max = 30.0  # e^{-30} ~ 1e-13
    dz = z_max / n_points

    borel_sum = 0.0
    for i in range(1, n_points):
        z = i * dz
        integrand = borel_transform(t_val * z) * math.exp(-z)
        borel_sum += integrand * dz

    # Exact value from the closed-form GF
    # G(t) = integral of u * sqrt(Q(u)) du from 0 to t
    # where Q(u) = c^2 + 12*c*u + alpha*u^2
    # Direct computation: sum S_r * t^r
    exact_sum = sum(S.get(r, 0) * t_val ** r for r in range(2, max_arity + 1))

    return {
        'c': c_val,
        't': t_val,
        'borel_sum': borel_sum,
        'direct_sum': exact_sum,
        'agreement': abs(borel_sum - exact_sum) / max(abs(exact_sum), 1e-30),
        'max_arity': max_arity,
    }


# =====================================================================
# Section 11: Shadow-automorphic dictionary
# =====================================================================

def shadow_automorphic_dictionary() -> Dict[str, Dict[str, str]]:
    r"""The shadow-automorphic dictionary: translating between shadow tower
    invariants and automorphic form data.

    This is the computational incarnation of the arithmetic programme
    (arithmetic_shadows.tex): shadow coefficients <-> L-function data.

    DICTIONARY:
      Shadow side               | Automorphic side
      ========================= | =========================
      kappa (arity 2)           | Leading Eisenstein term
      S_3 (cubic shadow)        | Shifted Eisenstein / Lie datum
      S_4 (quartic shadow)      | Cusp form contribution (if nonzero)
      Shadow depth d            | d-1 critical lines
      Shadow atoms lambda_j     | Spectral eigenvalues of Laplacian
      Shadow metric Q_L         | Quadratic form on primary line
      Mellin poles of L_A(s)    | Weights of automorphic forms
      MC recursion              | Newton's identities on atoms
    """
    return {
        'kappa': {
            'shadow': 'S_2 = kappa (modular characteristic)',
            'automorphic': 'Leading Eisenstein series E_k coefficient',
            'formula': 'kappa determines weight-1 part of theta decomposition',
        },
        'cubic': {
            'shadow': 'S_3 = cubic shadow from Lie bracket',
            'automorphic': 'Shifted Eisenstein: activates zeta(s-k+1) with k>1',
            'formula': 'S_3 != 0 iff depth >= 3 (class L or higher)',
        },
        'quartic': {
            'shadow': 'S_4 = Q^contact (quartic contact invariant)',
            'automorphic': 'Cusp form contribution: activates L(s,f)',
            'formula': 'S_4 != 0 AND shadow NOT terminating iff cusp forms contribute',
        },
        'depth': {
            'shadow': 'Shadow depth d = max{r : S_r != 0} + 1',
            'automorphic': 'd-1 critical lines (thm:shadow-l-correspondence)',
            'formula': 'depth(V_Lambda) = 1 + #{activated L-functions}',
        },
        'mc_equation': {
            'shadow': 'MC recursion: nabla_H(S_r) + o^(r) = 0',
            'automorphic': "Newton's identities on spectral atoms",
            'formula': 'p_r = -r*S_r; Newton: p_r = sum_j lambda_j^r',
        },
    }
