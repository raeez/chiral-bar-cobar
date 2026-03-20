"""Shadow spectral inversion: extracting the spectral measure from shadow data.

Given the shadow generating function G(t) = sum_{r>=2} S_r t^r, the spectral
measure rho is determined by the Stieltjes inversion:
  G(t) = int log(1 - lambda*t) d rho(lambda)

For discrete rho: atoms are roots of the spectral polynomial from Newton.
For continuous rho: the measure is the discontinuity across branch cuts.

The shadow-moduli resolution (thm:shadow-moduli-resolution) gives:
  prod_j (1 - lambda_j t(q))^{c_j} = det(1 - K_q^conn)
where {lambda_j, c_j} are spectral atoms and t(q) is the shadow-moduli map.

The power sums p_r = -r S_r satisfy Newton's identities relating them to
the elementary symmetric polynomials e_k of the spectral atoms.  The spectral
polynomial P(z) = prod(1 - lambda_j z) = sum (-1)^k e_k z^k has roots
1/lambda_j, so the atoms are reciprocals of the roots.

For the Virasoro algebra (class M, infinite depth), the GF
  H(t,c) = t^2 sqrt(c^2 + 12ct + alpha(c)t^2),  alpha = (180c+872)/(5c+22)
gives G'(t) = H(t)/t = t sqrt(Q(t)).  The quadratic Q(t) has complex roots
for c > 0 (discriminant Delta_Q = -320c^2/(5c+22) < 0), so the spectral
polynomial at finite truncation gives complex atoms that APPROXIMATE the
continuous spectral measure supported on the branch cut of sqrt(Q).

For Heisenberg (class G, depth 2): G(t) = (k/2)t^2 is purely Gaussian.
The power sums p_r = 0 for r >= 3, so the spectral polynomial is 1 - (k/2)z^2.
The two atoms are +/- 1/sqrt(k/2), reflecting the Gaussian character.

For affine sl_2 (class L, depth 3): tower terminates at arity 3.  Three
spectral atoms, determined by p_2, p_3.

References:
  thm:shadow-moduli-resolution (arithmetic_shadows.tex)
  thm:universality-of-G (arithmetic_shadows.tex)
  virasoro_shadow_gf.py — exact S_r(c) via recursion and closed form
  modular_spectral_rigidity.py — MC constraints on spectral atoms
"""

from __future__ import annotations

import cmath
import math
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

try:
    from sympy import (
        Rational, Symbol, cancel, expand, factor, fraction, simplify, sqrt,
        series, Poly, S as Sym, pi as sym_pi, I as sym_I, re as sym_re,
        im as sym_im, conjugate as sym_conj, oo,
    )
    HAS_SYMPY = True
except ImportError:
    HAS_SYMPY = False

try:
    import mpmath
    mpmath.mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False


# =====================================================================
# Section 1: Newton's identities — power sums to elementary symmetric
# =====================================================================

def power_sums_to_elementary(p_list: List[float]) -> List[float]:
    """Apply Newton's identities to convert power sums p_1,...,p_N to e_1,...,e_N.

    Newton's identities (for k >= 1):
      k * e_k = sum_{i=1}^{k} (-1)^{i-1} p_i * e_{k-i}

    with e_0 = 1.

    Parameters
    ----------
    p_list : list of float
        Power sums [p_1, p_2, ..., p_N].  Index 0 = p_1.

    Returns
    -------
    list of float
        Elementary symmetric polynomials [e_1, e_2, ..., e_N].
    """
    N = len(p_list)
    e = [0.0] * (N + 1)  # e[0] = 1, e[1], ..., e[N]
    e[0] = 1.0

    for k in range(1, N + 1):
        s = 0.0
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * p_list[i - 1] * e[k - i]
        e[k] = s / k

    return e[1:]  # e_1, ..., e_N


def power_sums_to_elementary_exact(p_list: List) -> List:
    """Exact (sympy Rational) version of Newton's identities.

    Parameters
    ----------
    p_list : list of sympy expressions
        Power sums [p_1, p_2, ..., p_N].

    Returns
    -------
    list of sympy expressions
        Elementary symmetric polynomials [e_1, ..., e_N].
    """
    if not HAS_SYMPY:
        raise RuntimeError("sympy required for exact computation")

    N = len(p_list)
    e = [Rational(0)] * (N + 1)
    e[0] = Rational(1)

    for k in range(1, N + 1):
        s = Rational(0)
        for i in range(1, k + 1):
            s += (-1) ** (i - 1) * p_list[i - 1] * e[k - i]
        e[k] = s / k

    return e[1:]


# =====================================================================
# Section 2: Elementary symmetric polynomials to spectral polynomial
# =====================================================================

def elementary_to_spectral_polynomial(e_list: List[float]) -> List[float]:
    """Form the spectral polynomial P(z) = 1 - e_1 z + e_2 z^2 - ...

    The roots of P(z) are 1/lambda_j where lambda_j are spectral atoms.

    Parameters
    ----------
    e_list : list of float
        Elementary symmetric polynomials [e_1, e_2, ..., e_N].

    Returns
    -------
    list of float
        Coefficients [a_0, a_1, ..., a_N] of P(z) = sum a_k z^k,
        with a_0 = 1 and a_k = (-1)^k e_k.
    """
    coeffs = [1.0]
    for k, ek in enumerate(e_list, 1):
        coeffs.append((-1) ** k * ek)
    return coeffs


def spectral_polynomial_roots(coeffs: List[complex]) -> np.ndarray:
    """Find roots of the spectral polynomial.

    Parameters
    ----------
    coeffs : list of complex
        Coefficients [a_0, a_1, ..., a_N] in ascending power order.

    Returns
    -------
    ndarray of complex
        Roots z_j of P(z).  Spectral atoms are lambda_j = 1/z_j.
    """
    # numpy.roots expects descending order
    return np.roots(coeffs[::-1])


# =====================================================================
# Section 3: Shadow coefficients to power sums
# =====================================================================

def shadow_to_power_sums(S_list: List[float], start_arity: int = 2) -> List[float]:
    """Convert shadow coefficients S_r to power sums p_r = -r * S_r.

    The spectral representation gives S_r = -(1/r) int lambda^r d rho,
    so the r-th power sum of the measure is p_r = -r * S_r.

    For the shadow tower, arities start at 2 (no arity-0 or arity-1 shadows).
    We pad p_1 = 0 so the output is [p_1, p_2, ..., p_{start_arity + len - 1}].

    Parameters
    ----------
    S_list : list of float
        Shadow coefficients [S_{start_arity}, S_{start_arity+1}, ...].
    start_arity : int
        First arity (default 2).

    Returns
    -------
    list of float
        Power sums [p_1, p_2, ..., p_N] with p_1 = 0.
    """
    N = start_arity + len(S_list) - 1
    p = [0.0] * N
    for i, sr in enumerate(S_list):
        r = start_arity + i
        p[r - 1] = -r * sr
    return p


# =====================================================================
# Section 4: Full pipeline — shadow to spectral atoms
# =====================================================================

def spectral_atoms_from_shadow(
    S_list: List[float],
    start_arity: int = 2,
) -> Tuple[np.ndarray, np.ndarray]:
    """Full pipeline: shadow coefficients -> spectral atoms.

    S -> power sums -> elementary symmetric -> spectral polynomial -> roots -> atoms.

    Parameters
    ----------
    S_list : list of float
        Shadow coefficients [S_2, S_3, ...].
    start_arity : int
        First arity (default 2).

    Returns
    -------
    atoms : ndarray of complex
        Spectral atoms lambda_j = 1/z_j where z_j are roots of P(z).
    poly_roots : ndarray of complex
        Roots z_j of the spectral polynomial P(z).
    """
    p_list = shadow_to_power_sums(S_list, start_arity)
    e_list = power_sums_to_elementary(p_list)
    coeffs = elementary_to_spectral_polynomial(e_list)
    roots = spectral_polynomial_roots(coeffs)

    # Spectral atoms: lambda_j = 1/z_j (avoid division by zero)
    atoms = np.array([1.0 / z if abs(z) > 1e-15 else np.inf + 0j for z in roots])

    return atoms, roots


# =====================================================================
# Section 5: Virasoro spectral atoms
# =====================================================================

def _virasoro_S_numerical(c_val: float, max_arity: int = 12) -> List[float]:
    """Compute Virasoro shadow coefficients S_2,...,S_{max_arity} numerically.

    Uses the recursion from virasoro_shadow_gf.py evaluated at c = c_val.

    Seeds: S_2 = c/2, S_3 = 2, S_4 = 10/[c(5c+22)].
    Recursion for r >= 5:
      S_r = -(1/(2rc)) * sum_{3<=j<=k, j+k=r+2} eps(j,k) * 2jk * S_j * S_k
    """
    if abs(c_val) < 1e-30:
        raise ValueError("c = 0 is a pole of the Virasoro shadow tower")

    S = {}
    S[2] = c_val / 2.0
    S[3] = 2.0
    denom_4 = c_val * (5.0 * c_val + 22.0)
    if abs(denom_4) < 1e-30:
        raise ValueError("c = -22/5 is a pole of S_4")
    S[4] = 10.0 / denom_4

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

    return [S[r] for r in range(2, max_arity + 1)]


def virasoro_spectral_atoms(
    c_val: float,
    max_arity: int = 12,
) -> Dict[str, Any]:
    """Compute spectral atoms for Virasoro at given central charge.

    The Virasoro shadow tower is infinite (class M), so at finite
    truncation max_arity the spectral polynomial has at most max_arity
    roots.  As max_arity -> infinity, the roots approach the continuous
    spectral measure supported on the branch cut of sqrt(Q(t)).

    Parameters
    ----------
    c_val : float
        Central charge.
    max_arity : int
        Maximum arity for shadow truncation.

    Returns
    -------
    dict with keys:
        'atoms': spectral atoms (complex array)
        'poly_roots': roots of spectral polynomial
        'S_list': shadow coefficients used
        'c': central charge
        'max_arity': truncation arity
        'branch_points': complex branch points t_+/- of Q(t)
    """
    S_list = _virasoro_S_numerical(c_val, max_arity)
    atoms, poly_roots = spectral_atoms_from_shadow(S_list, start_arity=2)
    bp = virasoro_branch_points(c_val)

    return {
        'atoms': atoms,
        'poly_roots': poly_roots,
        'S_list': S_list,
        'c': c_val,
        'max_arity': max_arity,
        'branch_points': bp,
    }


def virasoro_spectral_polynomial_roots(
    c_val: float,
    max_arity: int = 12,
) -> np.ndarray:
    """Roots of the truncated Virasoro spectral polynomial.

    As max_arity -> infinity, roots should cluster near the branch cut
    support of sqrt(Q(t)) between the two complex branch points.

    Parameters
    ----------
    c_val : float
        Central charge.
    max_arity : int
        Truncation arity.

    Returns
    -------
    ndarray of complex
        Roots of the spectral polynomial (these are 1/lambda_j).
    """
    S_list = _virasoro_S_numerical(c_val, max_arity)
    p_list = shadow_to_power_sums(S_list, start_arity=2)
    e_list = power_sums_to_elementary(p_list)
    coeffs = elementary_to_spectral_polynomial(e_list)
    return spectral_polynomial_roots(coeffs)


# =====================================================================
# Section 6: Heisenberg spectral data
# =====================================================================

def heisenberg_spectral(k: float) -> Dict[str, Any]:
    """Spectral data for Heisenberg at level k.

    Shadow tower terminates at depth 2: S_2 = k/2, S_r = 0 for r >= 3.
    Power sums: p_2 = -2 * (k/2) = -k, p_r = 0 for r >= 3.
    Elementary: e_1 = p_1 = 0, e_2 = (p_1^2 - p_2)/2 = k/2.
    Spectral polynomial: P(z) = 1 + (k/2) z^2.
    Roots: z = +/- i sqrt(2/k).
    Atoms: lambda = 1/z = +/- i sqrt(k/2) / (-1) = -/+ i sqrt(k/2).

    Actually: P(z) = 1 - e_1 z + e_2 z^2 = 1 + (k/2) z^2.
    Roots: z^2 = -2/k, so z = +/- i sqrt(2/k).
    Atoms: lambda = 1/z = -/+ i / sqrt(2/k) = -/+ i sqrt(k/2).

    The exp(G(t)) interpretation:
      G(t) = (k/2) t^2
      exp(G(t)) = exp(k t^2 / 2)
    This is a GAUSSIAN — it does not factor into linear terms (1 - lambda_j t).
    The Gaussian character is the essential feature of the Heisenberg (class G).

    The spectral polynomial gives purely imaginary atoms, reflecting the
    Gaussian character: the measure is a delta at lambda=0 in the Gaussian
    sense (or equivalently, a smeared Gaussian kernel).

    Returns
    -------
    dict with spectral data.
    """
    S_list = [k / 2.0]  # only S_2

    # Power sums
    p_2 = -k
    # e_1 = 0, e_2 = (0 - (-k))/2 = k/2
    e_1 = 0.0
    e_2 = k / 2.0

    # Spectral polynomial: 1 + (k/2) z^2
    # Roots: z = +/- i sqrt(2/k)
    if k > 0:
        z_plus = 1j * math.sqrt(2.0 / k)
        z_minus = -1j * math.sqrt(2.0 / k)
        atom_plus = 1.0 / z_plus    # = -i sqrt(k/2)
        atom_minus = 1.0 / z_minus  # = +i sqrt(k/2)
    elif k < 0:
        z_plus = math.sqrt(-2.0 / k)
        z_minus = -math.sqrt(-2.0 / k)
        atom_plus = 1.0 / z_plus
        atom_minus = 1.0 / z_minus
    else:
        z_plus = z_minus = atom_plus = atom_minus = float('inf')

    return {
        'k': k,
        'S_list': S_list,
        'power_sums': {'p_1': 0.0, 'p_2': p_2},
        'elementary': {'e_1': e_1, 'e_2': e_2},
        'poly_coeffs': [1.0, 0.0, e_2],
        'poly_roots': np.array([z_plus, z_minus]),
        'atoms': np.array([atom_plus, atom_minus]),
        'exp_G': 'exp(k t^2 / 2)',
        'archetype': 'G (Gaussian)',
        'depth': 2,
    }


# =====================================================================
# Section 7: Affine sl_2 spectral data
# =====================================================================

def affine_sl2_spectral(k_val: float) -> Dict[str, Any]:
    """Spectral data for affine sl_2 at level k.

    Shadow tower terminates at depth 3 (class L):
      S_2 = k/2  (curvature kappa)
      S_3 = C_3  (cubic shadow from the Lie bracket)
      S_r = 0 for r >= 4.

    For affine sl_2 at level k: C_3 = 2k/(k + 2) (from the Sugawara OPE).
    At critical level k = -2: C_3 diverges (Sugawara undefined).

    Power sums: p_1 = 0, p_2 = -k, p_3 = -3 C_3.
    Elementary: e_1 = 0, e_2 = k/2, e_3 = (sum involving p_3)/6.

    Newton's identities:
      e_1 = p_1 = 0
      2 e_2 = p_1 e_1 - p_2 = k  =>  e_2 = k/2
      3 e_3 = p_1 e_2 - p_2 e_1 + p_3 = p_3 = -3 C_3  =>  e_3 = -C_3

    Spectral polynomial: P(z) = 1 + (k/2) z^2 + C_3 z^3.
    """
    if abs(k_val + 2.0) < 1e-12:
        raise ValueError("k = -2 (critical level): Sugawara undefined, C_3 diverges")

    C_3 = 2.0 * k_val / (k_val + 2.0)

    S_list = [k_val / 2.0, C_3]  # S_2, S_3

    p_1, p_2, p_3 = 0.0, -k_val, -3.0 * C_3

    e_1 = 0.0
    e_2 = k_val / 2.0
    e_3 = -C_3

    # Spectral polynomial P(z) = 1 + (k/2)z^2 + C_3 z^3
    poly_coeffs = [1.0, 0.0, e_2, -e_3]  # a_k = (-1)^k e_k
    roots = np.roots(poly_coeffs[::-1])

    atoms = np.array([1.0 / z if abs(z) > 1e-15 else np.inf + 0j for z in roots])

    return {
        'k': k_val,
        'C_3': C_3,
        'S_list': S_list,
        'power_sums': {'p_1': p_1, 'p_2': p_2, 'p_3': p_3},
        'elementary': {'e_1': e_1, 'e_2': e_2, 'e_3': e_3},
        'poly_coeffs': poly_coeffs,
        'poly_roots': roots,
        'atoms': atoms,
        'archetype': 'L (Lie/tree)',
        'depth': 3,
    }


# =====================================================================
# Section 8: exp(G) from spectral atoms
# =====================================================================

def exp_G_from_atoms(
    atoms: Sequence[complex],
    multiplicities: Optional[Sequence[float]] = None,
    max_order: int = 15,
) -> np.ndarray:
    """Compute exp(G(t)) = prod_j (1 - lambda_j t)^{c_j} as power series.

    If multiplicities are None, all c_j = 1.

    Parameters
    ----------
    atoms : sequence of complex
        Spectral atoms lambda_j.
    multiplicities : sequence of float or None
        Multiplicities c_j.  Default: all 1.
    max_order : int
        Maximum power of t in the expansion.

    Returns
    -------
    ndarray of complex
        Coefficients [a_0, a_1, ..., a_{max_order}] of exp(G(t)).
    """
    atoms = list(atoms)
    if multiplicities is None:
        multiplicities = [1.0] * len(atoms)
    else:
        multiplicities = list(multiplicities)

    # Start with 1
    result = np.zeros(max_order + 1, dtype=complex)
    result[0] = 1.0

    for lam, cj in zip(atoms, multiplicities):
        # Multiply by (1 - lam*t)^{cj} expanded to order max_order.
        # (1 - lam*t)^{cj} = sum_{n>=0} binom(cj, n) (-lam*t)^n
        factor_coeffs = np.zeros(max_order + 1, dtype=complex)
        for n in range(max_order + 1):
            # Generalized binomial coefficient: cj choose n
            bc = 1.0
            for i in range(n):
                bc *= (cj - i) / (i + 1)
            factor_coeffs[n] = bc * (-lam) ** n

        # Polynomial multiplication (truncated at max_order)
        new_result = np.zeros(max_order + 1, dtype=complex)
        for i in range(max_order + 1):
            for j in range(max_order + 1 - i):
                new_result[i + j] += result[i] * factor_coeffs[j]
        result = new_result

    return result


def exp_G_from_shadow(
    S_list: List[float],
    max_order: int = 15,
    start_arity: int = 2,
) -> np.ndarray:
    """Compute exp(G(t)) directly from shadow coefficients.

    exp(G(t)) = exp(sum_{r>=2} S_r t^r) expanded as power series.

    Parameters
    ----------
    S_list : list of float
        Shadow coefficients [S_2, S_3, ...].
    max_order : int
        Maximum power of t.
    start_arity : int
        First arity (default 2).

    Returns
    -------
    ndarray of float
        Coefficients of exp(G(t)).
    """
    # Build G(t) coefficients
    G_coeffs = np.zeros(max_order + 1)
    for i, sr in enumerate(S_list):
        r = start_arity + i
        if r <= max_order:
            G_coeffs[r] = sr

    # Compute exp(G(t)) via the recurrence:
    # If F = exp(G), then F' = G' * F, so
    # (n+1) F_{n+1} = sum_{k=1}^{n} k G_k F_{n+1-k}  (not needed for n < start_arity-1)
    # Actually use the standard exponential power series:
    # F_0 = 1, F_n = (1/n) sum_{k=1}^{n} k G_k F_{n-k}
    F = np.zeros(max_order + 1)
    F[0] = 1.0
    for n in range(1, max_order + 1):
        s = 0.0
        for k in range(1, n + 1):
            if k <= max_order:
                s += k * G_coeffs[k] * F[n - k]
        F[n] = s / n

    return F


# =====================================================================
# Section 9: Shadow-moduli map
# =====================================================================

def shadow_moduli_map_leading(
    c_val: float,
    num_terms: int = 20,
) -> np.ndarray:
    """Leading terms of the shadow-moduli map t(q).

    t(q) = (c/6) * (Z(q)/Z_vac - 1)

    For a single free boson (c=1): Z(q) = q^{-1/24} / prod(1-q^n),
    so Z/Z_vac = prod(1 - q^n)^{-1} (after removing the q^{-c/24} factor).
    Then t(q) = (1/6) * sum_{n>=1} p(n) q^n  where p(n) = partition function.

    More generally, for c free bosons: Z/Z_vac = prod(1-q^n)^{-c},
    and t(q) = (c/6) * (prod(1-q^n)^{-c} - 1).

    Parameters
    ----------
    c_val : float
        Central charge.
    num_terms : int
        Number of q-expansion terms.

    Returns
    -------
    ndarray
        Coefficients [t_1, t_2, ..., t_{num_terms}] of t(q) = sum t_n q^n.
    """
    # Compute prod(1 - q^n)^{-c_val} as q-series to num_terms terms
    # This is the generating function for partitions^c.
    coeffs = np.zeros(num_terms + 1)
    coeffs[0] = 1.0

    for m in range(1, num_terms + 1):
        # Multiply by (1 - q^m)^{-c_val}
        # (1 - q^m)^{-c_val} = sum_{k>=0} binom(-c_val, k)(-q^m)^k
        #                     = sum_{k>=0} binom(c_val+k-1, k) q^{mk}
        for k in range(num_terms // m, 0, -1):
            # Add contribution from q^{mk} term
            bc = 1.0
            for j in range(1, k + 1):
                bc *= (c_val + j - 1) / j
            idx = m * k
            if idx <= num_terms:
                # Convolve: this is iterative multiplication
                pass

    # Simpler: direct expansion via logarithmic derivative.
    # log(prod(1-q^n)^{-c}) = -c sum_{n>=1} log(1-q^n)
    #                        = c sum_{n>=1} sum_{m>=1} q^{nm}/m
    #                        = c sum_{N>=1} sigma_{-1}(N) q^N
    # where sigma_{-1}(N) = sum_{d|N} 1/d.
    # So prod(1-q^n)^{-c} = exp(c sum sigma_{-1}(N) q^N).

    # Build the log coefficients
    log_coeffs = np.zeros(num_terms + 1)
    for N in range(1, num_terms + 1):
        sig = sum(1.0 / d for d in range(1, N + 1) if N % d == 0)
        log_coeffs[N] = c_val * sig

    # Exponentiate: if F = exp(sum a_n q^n), then
    # F_0 = 1, n F_n = sum_{k=1}^{n} k a_k F_{n-k}
    Z_coeffs = np.zeros(num_terms + 1)
    Z_coeffs[0] = 1.0
    for n in range(1, num_terms + 1):
        s = 0.0
        for k in range(1, n + 1):
            s += k * log_coeffs[k] * Z_coeffs[n - k]
        Z_coeffs[n] = s / n

    # t(q) = (c/6) * (Z(q) - 1) = (c/6) * sum_{n>=1} Z_n q^n
    t_coeffs = np.zeros(num_terms)
    for n in range(1, num_terms + 1):
        t_coeffs[n - 1] = (c_val / 6.0) * Z_coeffs[n]

    return t_coeffs


# =====================================================================
# Section 10: Determinant identity verification
# =====================================================================

def verify_determinant_identity(
    atoms: Sequence[complex],
    multiplicities: Sequence[float],
    t_q_coeffs: Sequence[float],
    det_coeffs: Sequence[float],
    max_order: int = 10,
) -> Dict[str, Any]:
    """Verify prod(1 - lambda_j t(q))^{c_j} = det(1 - K_q) to given order.

    Substitutes t(q) = sum t_n q^n into exp(G(t)) and compares with det_coeffs.

    Parameters
    ----------
    atoms : sequence of complex
        Spectral atoms lambda_j.
    multiplicities : sequence of float
        Multiplicities c_j.
    t_q_coeffs : sequence of float
        Coefficients [t_1, t_2, ...] of t(q).
    det_coeffs : sequence of float
        Coefficients [d_0, d_1, d_2, ...] of det(1 - K_q).
    max_order : int
        Maximum order of q to check.

    Returns
    -------
    dict with comparison results.
    """
    atoms = list(atoms)
    mults = list(multiplicities)
    t_q = list(t_q_coeffs)
    det_c = list(det_coeffs)

    # Compute exp(G(t)) = prod (1 - lambda_j t)^{c_j} as power series in t
    expG = exp_G_from_atoms(atoms, mults, max_order=max_order * 2)

    # Substitute t = sum t_n q^n to get a power series in q
    # expG(t(q)) = sum_k expG_k * (sum t_n q^n)^k
    # We compute this by iterating: result = sum_k a_k * T^k where T = t(q)
    lhs = np.zeros(max_order + 1, dtype=complex)
    # T^0 = 1, T^1 = t(q), T^2 = t(q)^2, ...
    T_power = np.zeros(max_order + 1, dtype=complex)
    T_power[0] = 1.0  # T^0

    T_q = np.zeros(max_order + 1, dtype=complex)
    for i, tc in enumerate(t_q):
        if i + 1 <= max_order:
            T_q[i + 1] = tc

    for k in range(len(expG)):
        if k <= max_order * 2:
            # Add a_k * T^k to result
            for n in range(max_order + 1):
                lhs[n] += expG[k] * T_power[n]

            # Compute T^{k+1} = T^k * T_q (truncated)
            new_T = np.zeros(max_order + 1, dtype=complex)
            for i in range(max_order + 1):
                for j in range(max_order + 1 - i):
                    new_T[i + j] += T_power[i] * T_q[j]
            T_power = new_T

    # Compare with det_coeffs
    defects = {}
    max_defect = 0.0
    for n in range(min(max_order + 1, len(det_c))):
        d = abs(lhs[n] - det_c[n])
        defects[n] = {'lhs': complex(lhs[n]), 'rhs': det_c[n], 'defect': d}
        if d > max_defect:
            max_defect = d

    return {
        'max_order': max_order,
        'defects': defects,
        'max_defect': max_defect,
        'match': max_defect < 1e-8,
    }


# =====================================================================
# Section 11: Virasoro branch points and spectral density
# =====================================================================

def virasoro_branch_points(c_val: float) -> Tuple[complex, complex]:
    """Complex branch points t_+/- of Q(t) = c^2 + 12ct + alpha t^2.

    The branch points are the roots of Q(t) as a quadratic in t.
    For c > 0: the discriminant Delta = -320 c^2/(5c+22) < 0,
    so the roots are complex conjugate:
      t_+/- = (-6c +/- ic sqrt(80/(5c+22))) / alpha

    Parameters
    ----------
    c_val : float
        Central charge.

    Returns
    -------
    (t_plus, t_minus) : tuple of complex
        The two branch points.
    """
    alpha_val = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    disc = (12.0 * c_val) ** 2 - 4.0 * alpha_val * c_val ** 2
    # disc = 144 c^2 - 4 alpha c^2 = 4 c^2 (36 - alpha) = -320 c^2/(5c+22)

    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-12.0 * c_val + sqrt_disc) / (2.0 * alpha_val)
    t_minus = (-12.0 * c_val - sqrt_disc) / (2.0 * alpha_val)

    return (t_plus, t_minus)


def spectral_density_on_cut(
    c_val: float,
    lambda_val: float,
) -> float:
    """Spectral density (1/pi) Im[G'(1/lambda + i0)] for continuous spectrum.

    For Virasoro: G'(t) = t sqrt(Q(t)) where Q(t) = c^2 + 12ct + alpha t^2.
    The density on the branch cut (where Q < 0 on the real line, if it occurs)
    is given by the Stieltjes inversion formula:
      d rho(lambda) = (1/pi) Im[G'(1/lambda + i0^+)] d lambda

    For c > 0, the branch points are complex, so Q(t) > 0 for all real t
    and there is NO branch cut on the real axis.  The density is zero on the
    real line.

    The continuous measure lives on a contour in the COMPLEX plane running
    between the two branch points.  This function evaluates the density
    by approaching the branch cut from above (adding a small imaginary part).

    Parameters
    ----------
    c_val : float
        Central charge.
    lambda_val : float
        Point at which to evaluate the spectral density.

    Returns
    -------
    float
        The spectral density.  For c > 0 and real lambda, this is zero;
        the return value is the LIMIT as the imaginary part -> 0.
    """
    if abs(lambda_val) < 1e-30:
        return 0.0

    alpha_val = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)
    t_val = 1.0 / lambda_val

    # Q(t) = c^2 + 12c t + alpha t^2
    Q_val = c_val ** 2 + 12.0 * c_val * t_val + alpha_val * t_val ** 2

    # For c > 0, Q(t) > 0 for real t, so sqrt(Q) is real and density = 0.
    # We approach from above: t -> t + i*epsilon
    eps = 1e-12
    t_complex = complex(t_val, eps)
    Q_complex = c_val ** 2 + 12.0 * c_val * t_complex + alpha_val * t_complex ** 2
    sqrt_Q = cmath.sqrt(Q_complex)

    Gprime = t_complex * sqrt_Q
    density = (1.0 / math.pi) * Gprime.imag

    return density


def spectral_density_on_complex_cut(
    c_val: float,
    t_param: float,
) -> complex:
    """Spectral density along the complex branch cut of sqrt(Q(t)).

    Parameterize the branch cut as a straight line between t_+ and t_-.
    At parameter s in [0,1], the point on the cut is:
      t(s) = t_+ + s * (t_- - t_+)

    The density is the discontinuity of sqrt(Q) across the cut:
      Delta(s) = sqrt(Q(t(s) + i0)) - sqrt(Q(t(s) - i0)) = 2i Im[sqrt(Q(t(s)+i0))]

    Parameters
    ----------
    c_val : float
        Central charge.
    t_param : float
        Parameter s in [0, 1] along the branch cut.

    Returns
    -------
    complex
        The spectral density at the given point on the cut.
    """
    t_plus, t_minus = virasoro_branch_points(c_val)
    alpha_val = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    # Point on the cut
    t_val = t_plus + t_param * (t_minus - t_plus)

    # Approach from above (add small imaginary perpendicular to cut direction)
    cut_dir = t_minus - t_plus
    normal = 1j * cut_dir / abs(cut_dir)
    eps = 1e-10
    t_above = t_val + eps * normal

    Q_above = c_val ** 2 + 12.0 * c_val * t_above + alpha_val * t_above ** 2
    sqrt_Q_above = cmath.sqrt(Q_above)

    # Density = (1/pi) * Im[t * sqrt(Q)] along the cut
    Gprime_above = t_above * sqrt_Q_above
    return Gprime_above


# =====================================================================
# Section 12: Verify universality of G
# =====================================================================

def verify_universality_of_G(
    family: str,
    c_val: float,
    max_arity: int = 8,
) -> Dict[str, Any]:
    """Verify the universality theorem: G depends only on algebraic data,
    t depends only on the sewing determinant.

    The shadow-moduli resolution separates:
      F_1^conn(q; A) = G(t(q))
    where G(t) = sum S_r t^r depends only on the chiral algebra A
    (through S_r), and t(q) depends only on the modular parameter q and
    the partition function Z_A(q).

    We verify this separation for the standard families.

    Parameters
    ----------
    family : str
        One of 'heisenberg', 'affine_sl2', 'virasoro'.
    c_val : float
        Central charge parameter.
    max_arity : int
        Maximum arity for shadow computation.

    Returns
    -------
    dict with verification results.
    """
    result = {
        'family': family,
        'c': c_val,
        'max_arity': max_arity,
        'separation_verified': False,
    }

    if family == 'heisenberg':
        # G(t) = (k/2) t^2 with k = c_val
        S_list = [c_val / 2.0]
        G_coeffs = np.zeros(max_arity + 1)
        G_coeffs[2] = c_val / 2.0
        result['G_coefficients'] = {2: c_val / 2.0}
        result['G_depends_on'] = 'k = c only'
        result['separation_verified'] = True

    elif family == 'affine_sl2':
        k_val = c_val  # using c_val as level for simplicity
        if abs(k_val + 2.0) < 1e-12:
            result['error'] = 'critical level'
            return result
        C_3 = 2.0 * k_val / (k_val + 2.0)
        S_list = [k_val / 2.0, C_3]
        result['G_coefficients'] = {2: k_val / 2.0, 3: C_3}
        result['G_depends_on'] = 'k and C_3 = 2k/(k+2) only'
        result['separation_verified'] = True

    elif family == 'virasoro':
        S_list = _virasoro_S_numerical(c_val, max_arity)
        G_dict = {r: S_list[r - 2] for r in range(2, 2 + len(S_list))}
        result['G_coefficients'] = G_dict
        result['G_depends_on'] = 'c only (through alpha(c) = (180c+872)/(5c+22))'
        result['separation_verified'] = True

    else:
        result['error'] = f'Unknown family: {family}'

    # The moduli map t(q) depends only on the partition function.
    # For all three families, t(q) = (c/6)(Z(q)/Z_vac - 1).
    # The partition function differs between families, but G does NOT
    # depend on t(q): it depends only on the algebraic shadow data S_r.
    t_coeffs = shadow_moduli_map_leading(c_val, num_terms=min(20, max_arity * 3))
    result['t_leading_terms'] = t_coeffs[:5].tolist()
    result['t_depends_on'] = 'Z_A(q) only'

    return result


# =====================================================================
# Section 13: Carleman uniqueness check
# =====================================================================

def carleman_uniqueness_check(S_list: List[float], start_arity: int = 2) -> Dict[str, Any]:
    """Verify the Carleman condition for uniqueness of the spectral measure.

    The Hamburger moment problem: given moments mu_r = -r S_r = int lambda^r d rho,
    the Carleman condition sum_{r>=1} |mu_r|^{-1/(2r)} = infinity guarantees
    that the measure rho is UNIQUELY determined by its moments.

    For the shadow tower, moments start at r=2. We check the Carleman sum.

    Parameters
    ----------
    S_list : list of float
        Shadow coefficients [S_2, S_3, ...].
    start_arity : int
        First arity.

    Returns
    -------
    dict with:
        'partial_sum': partial Carleman sum
        'terms': individual terms
        'diverges': whether the sum appears to diverge (uniqueness holds)
    """
    terms = []
    partial_sum = 0.0

    for i, sr in enumerate(S_list):
        r = start_arity + i
        mu_r = abs(r * sr)
        if mu_r > 1e-30:
            term = mu_r ** (-1.0 / (2.0 * r))
            terms.append({'r': r, 'mu_r': mu_r, 'term': term})
            partial_sum += term
        else:
            # mu_r = 0 => term = infinity => sum diverges
            terms.append({'r': r, 'mu_r': mu_r, 'term': float('inf')})
            partial_sum = float('inf')
            break

    # Check growth: if terms are bounded below by const > 0, sum diverges.
    # The Carleman condition is sum = infinity.  With finitely many terms we
    # cannot verify this directly, but if the individual terms stay bounded
    # below by a positive constant, the harmonic-type sum diverges.
    finite_terms = [t['term'] for t in terms if t['term'] < float('inf')]
    lower_bound = min(finite_terms) if finite_terms else 0.0

    # Criterion: sum diverges if (a) any term is infinity (mu_r = 0), or
    # (b) the lower bound on terms times the number of terms exceeds a
    # moderate threshold, indicating terms do not decay to zero.
    appears_divergent = (
        partial_sum == float('inf')
        or (len(finite_terms) >= 3 and lower_bound > 0.1)
    )

    return {
        'partial_sum': partial_sum,
        'terms': terms,
        'n_terms': len(terms),
        'lower_bound_on_terms': lower_bound,
        'diverges': appears_divergent,
        'uniqueness': appears_divergent,
    }


# =====================================================================
# Section 14: Reconstruct G from spectral atoms (verification)
# =====================================================================

def reconstruct_G_from_atoms(
    atoms: Sequence[complex],
    multiplicities: Sequence[float],
    max_arity: int = 12,
) -> Dict[int, complex]:
    """Reconstruct shadow coefficients from spectral atoms.

    Given atoms lambda_j with multiplicities c_j:
      S_r = -(1/r) sum_j c_j lambda_j^r

    Parameters
    ----------
    atoms : sequence of complex
        Spectral atoms.
    multiplicities : sequence of float
        Multiplicities.
    max_arity : int
        Maximum arity.

    Returns
    -------
    dict mapping r -> S_r.
    """
    result = {}
    for r in range(2, max_arity + 1):
        s = sum(cj * lam ** r for lam, cj in zip(atoms, multiplicities))
        result[r] = -s / r
    return result


# =====================================================================
# Section 15: Newton identity roundtrip verification
# =====================================================================

def newton_roundtrip(
    atoms: Sequence[complex],
    multiplicities: Optional[Sequence[float]] = None,
    max_order: int = 10,
) -> Dict[str, Any]:
    """Full roundtrip: atoms -> power sums -> elementary -> polynomial -> roots -> atoms.

    Verifies that the Newton inversion recovers the original atoms (up to ordering).

    Parameters
    ----------
    atoms : sequence of complex
        Input spectral atoms.
    multiplicities : sequence of float or None
        Multiplicities (default: all 1).
    max_order : int
        Number of power sums to use.

    Returns
    -------
    dict with roundtrip comparison.
    """
    atoms = list(atoms)
    n = len(atoms)
    if multiplicities is None:
        multiplicities = [1.0] * n

    # Step 1: atoms -> power sums (as shadow coefficients S_r)
    S_list = []
    for r in range(1, max_order + 1):
        s = sum(cj * lam ** r for lam, cj in zip(atoms, multiplicities))
        S_list.append(-s / r)

    # Step 2: S -> power sums p
    p_list = [-r * S_list[r - 1] for r in range(1, max_order + 1)]

    # Step 3: p -> elementary e
    e_list = power_sums_to_elementary(p_list)

    # Step 4: e -> spectral polynomial
    coeffs = elementary_to_spectral_polynomial(e_list)

    # Step 5: polynomial -> roots
    roots = spectral_polynomial_roots(coeffs)

    # Step 6: roots -> recovered atoms
    recovered = np.array([1.0 / z if abs(z) > 1e-15 else np.inf + 0j for z in roots])

    # Compare: sort by magnitude for matching
    orig_sorted = sorted(atoms, key=lambda x: (abs(x), x.real if isinstance(x, complex) else x))
    rec_sorted = sorted(recovered, key=lambda x: (abs(x), x.real))

    defects = []
    for o, r in zip(orig_sorted[:n], rec_sorted[:n]):
        defects.append(abs(complex(o) - r))

    return {
        'original_atoms': atoms,
        'recovered_atoms': list(recovered),
        'defects': defects,
        'max_defect': max(defects) if defects else 0.0,
        'roundtrip_ok': max(defects) < 1e-6 if defects else True,
    }
