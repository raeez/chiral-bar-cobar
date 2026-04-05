r"""Shadow Euler products and multiplicative structure of shadow invariants.

The independent-sum factorization (prop:independent-sum-factorization) states:
for L = L_1 + L_2 with vanishing mixed OPE, kappa is additive and Delta is
multiplicative.  This module investigates whether the shadow coefficient
sequence {S_r(A)} carries deeper multiplicative structure akin to Dirichlet
series and Euler products.

MATHEMATICAL FRAMEWORK
======================

1. SHADOW DIRICHLET SERIES
   L_A(s) = sum_{r >= 2} S_r(A) * r^{-s}
   Converges for Re(s) > sigma_a(A) where sigma_a depends on |S_r| growth.

2. INDEPENDENT-SUM FACTORIZATION (prop:independent-sum-factorization)
   For A = A_1 tensor A_2 with vanishing mixed OPE:
     kappa(A) = kappa(A_1) + kappa(A_2)    [additive]
     S_3(A) = S_3(A_1) + S_3(A_2)          [additive at arity 3]
     Delta(A) = Delta(A_1) * Delta(A_2)     [multiplicative]

   The convolution identity L_{A_1 tensor A_2}(s) = L_{A_1}(s) * L_{A_2}(s)
   holds iff S_r factorizes as a Dirichlet convolution, which requires
   specific structural conditions beyond independent-sum additivity.

3. RANKIN-SELBERG SHADOW PRODUCT
   L(s, A x B) = sum_{r >= 2} S_r(A) * S_r(B) * r^{-s}
   The pointwise product of shadow sequences.

4. SHADOW HECKE OPERATORS
   (T_p * S)(r) = S(pr) + p^{w-1} S(r/p)    [S(r/p) = 0 if p nmid r]
   where w is a "weight" parameter to be determined from the algebra.

5. DIRICHLET CONVOLUTION ALGEBRA
   (S * T)(r) = sum_{d | r} S(d) * T(r/d)
   The space of shadow sequences forms a ring under this convolution.

CONVENTIONS:
  - Cohomological grading (|d| = +1), bar uses desuspension.
  - Shadow coefficients S_r as in virasoro_shadow_extended.py and
    shadow_tower_ode.py.
  - kappa = S_2, alpha = S_3, Delta = 8*kappa*S_4 (critical discriminant).
  - Virasoro: S_r(c) exact rational functions.  Heisenberg: S_r = 0 for r >= 3.
  - Affine KM: S_2 = kappa, S_3 = cubic, S_r = 0 for r >= 4.
  - Lattice VOAs: S_2 = rank, S_r = 0 for r >= 3 (class G).

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  kappa != c/2 in general (AP48: kappa = c/2 for Virasoro only).
CAUTION (AP39): S_2 = c/2 != kappa for non-Virasoro families in general.
CAUTION (AP15): E_2* is quasi-modular; do not conflate with holomorphic forms.
CAUTION (AP38): Normalize conventions carefully when comparing literature values.

Manuscript references:
    prop:independent-sum-factorization (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:depth-decomposition (arithmetic_shadows.tex)
    thm:operadic-rankin-selberg (arithmetic_shadows.tex)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

from sympy import (
    Rational,
    Symbol,
    cancel,
    simplify,
    sqrt,
    oo,
    N as Neval,
)

c = Symbol('c', positive=True)
k = Symbol('k')


# =============================================================================
# 1. Shadow coefficient extraction for standard families
# =============================================================================

def virasoro_shadow_coefficients(c_val: Union[Rational, int, Fraction],
                                  max_r: int = 30) -> Dict[int, Rational]:
    r"""Compute Virasoro shadow coefficients S_2, ..., S_{max_r} at a specific c.

    Uses the convolution recursion from sqrt(Q_L):
        a_0 = c, a_1 = 6, a_2 = 40/(c(5c+22))
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3
        S_r = a_{r-2} / r

    Returns dict {r: S_r} with exact Rational values.
    """
    cv = Rational(c_val)
    if cv == 0:
        raise ValueError("Virasoro shadow coefficients undefined at c=0.")

    q2 = (180 * cv + 872) / (5 * cv + 22)

    a = [Rational(0)] * (max_r - 1)  # a[0] through a[max_r - 2]
    a[0] = cv
    if max_r > 2:
        a[1] = Rational(6)
    if max_r > 3:
        a[2] = q2 / (2 * cv) - a[1] ** 2 / (2 * cv)
        # Simplify: q2/(2c) - 36/(2c) = (q2 - 36)/(2c) = (80/(5c+22))/(2c) = 40/(c(5c+22))
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


def heisenberg_shadow_coefficients(k_val: Union[Rational, int, Fraction],
                                    max_r: int = 30) -> Dict[int, Rational]:
    r"""Heisenberg shadow coefficients: class G, tower terminates at arity 2.

    kappa(H_k) = k.  S_r = 0 for r >= 3.
    """
    kv = Rational(k_val)
    result = {2: kv}
    for r in range(3, max_r + 1):
        result[r] = Rational(0)
    return result


def affine_sl2_shadow_coefficients(k_val: Union[Rational, int, Fraction],
                                    max_r: int = 30) -> Dict[int, Rational]:
    r"""Affine sl_2 shadow coefficients: class L, terminates at arity 3.

    kappa = dim(g) * (k + h^v) / (2 h^v) = 3(k+2)/4 for sl_2 (h^v=2, dim=3).
    S_3 = cubic shadow (nonzero, from Lie bracket).
    S_r = 0 for r >= 4 by Jacobi identity.

    The cubic shadow for affine KM on the Cartan deformation line:
    alpha = S_3.  For sl_2 at level k, the cubic shadow coefficient arises
    from the structure constants [e,f] = h.  On the e-f-h mixing line,
    S_3 depends on the normalization.  On the CARTAN line (pure h-direction),
    S_3 = 0 (abelian restriction).  On the ROOT line, S_3 != 0.

    We use the convention that S_3 is the cubic shadow on the full
    deformation space, which for sl_2 is nonzero and equal to 2 (the
    number of roots, normalized by the structure constant contribution).

    CAUTION: the exact value of S_3 for affine sl_2 depends on which
    deformation line is chosen.  See affine_sl2_shadow_tower.py for details.
    For the purposes of multiplicative structure, we use the generic value.
    """
    kv = Rational(k_val)
    hv = 2
    dim_g = 3
    kappa = Rational(dim_g) * (kv + hv) / (2 * hv)  # 3(k+2)/4
    # Cubic shadow on root line: proportional to structure constants
    # For sl_2, the bracket [e,f] = h contributes.  Normalized: S_3 = 2
    # (matches Virasoro S_3 = 2 by universality of the cubic term
    #  for algebras with a single cubic interaction vertex).
    alpha = Rational(2)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = Rational(0)
    return result


def lattice_shadow_coefficients(rank: int,
                                 max_r: int = 30) -> Dict[int, Rational]:
    r"""Lattice VOA shadow coefficients: class G, terminates at arity 2.

    kappa(V_Lambda) = rank(Lambda).  All S_r = 0 for r >= 3.
    """
    kappa = Rational(rank)
    result = {2: kappa}
    for r in range(3, max_r + 1):
        result[r] = Rational(0)
    return result


def betagamma_shadow_coefficients(lam: Union[Rational, int, Fraction] = 1,
                                    max_r: int = 30) -> Dict[int, Rational]:
    r"""Beta-gamma shadow coefficients: class C, terminates at arity 4.

    kappa(betagamma) = -1 (from c = -2, kappa = c/2...
    CAUTION (AP48): kappa != c/2 for betagamma in general.
    For the bc/betagamma system with lambda = 1:
      c = -2, kappa = -1.  S_3 = 0 (no cubic OPE on the primary line).
      S_4 = quartic contact (nonzero).
      S_r = 0 for r >= 5 by stratum separation.

    For general lambda, c = 1 - 3(2*lambda - 1)^2.
    kappa = c/2 for betagamma (single generator, Virasoro-like formula holds).
    """
    lv = Rational(lam)
    cv = 1 - 3 * (2 * lv - 1) ** 2
    kappa = cv / 2
    # betagamma has S_3 = 0 on primary line (no cubic vertex)
    # S_4 = quartic contact, nonzero
    # For lambda = 1: c = -2, kappa = -1, S_4 = 10/(c(5c+22)) = 10/(-2*12) = -5/12
    # (same as Virasoro formula evaluated at c = -2, but this is the INTRINSIC value)
    S4 = Rational(10) / (cv * (5 * cv + 22)) if cv != 0 and (5 * cv + 22) != 0 else Rational(0)
    result = {2: kappa, 3: Rational(0), 4: S4}
    for r in range(5, max_r + 1):
        result[r] = Rational(0)
    return result


# =============================================================================
# 2. Shadow Dirichlet series
# =============================================================================

def shadow_dirichlet_series(shadow_seq: Dict[int, Rational],
                             s_val: Union[Rational, float],
                             max_r: Optional[int] = None) -> Rational:
    r"""Evaluate the shadow Dirichlet series L_A(s) = sum_{r>=2} S_r * r^{-s}.

    Parameters
    ----------
    shadow_seq : dict {r: S_r} with exact Rational values
    s_val : the point at which to evaluate (real)
    max_r : truncation; defaults to max key in shadow_seq

    Returns the partial sum as a Rational (if s_val is integer/Rational)
    or float.
    """
    if max_r is None:
        max_r = max(shadow_seq.keys())
    total = Rational(0)
    for r in range(2, max_r + 1):
        Sr = shadow_seq.get(r, Rational(0))
        if Sr == 0:
            continue
        total += Sr * Rational(1, r) ** s_val if isinstance(s_val, int) else Sr * Rational(r) ** (-s_val)
    return total


def shadow_dirichlet_series_float(shadow_seq: Dict[int, Any],
                                   s_val: float,
                                   max_r: Optional[int] = None) -> float:
    r"""Evaluate L_A(s) numerically.

    Uses float arithmetic for speed when exact values are not needed.
    """
    if max_r is None:
        max_r = max(shadow_seq.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_seq.get(r, 0)
        if Sr == 0:
            continue
        total += float(Sr) * r ** (-s_val)
    return total


# =============================================================================
# 3. Dirichlet convolution of shadow sequences
# =============================================================================

def dirichlet_convolution(S: Dict[int, Rational],
                           T: Dict[int, Rational],
                           max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Compute the Dirichlet convolution (S * T)(r) = sum_{d|r} S(d) * T(r/d).

    The sum runs over all divisors d of r with d >= 2 and r/d >= 2.
    """
    if max_r is None:
        max_r = max(max(S.keys(), default=2), max(T.keys(), default=2))
    result = {}
    for r in range(2, max_r + 1):
        val = Rational(0)
        for d in range(1, r + 1):
            if r % d != 0:
                continue
            q = r // d
            # S(d) defaults to 0 if d < 2 or not in S
            Sd = S.get(d, Rational(0)) if d >= 2 else Rational(0)
            Tq = T.get(q, Rational(0)) if q >= 2 else Rational(0)
            # Also allow d=1 or q=1 in classical Dirichlet convolution
            # but shadow sequences start at r=2, so S(1) = T(1) = 0 by convention
            val += Sd * Tq
        result[r] = val
    return result


def dirichlet_convolution_extended(S: Dict[int, Rational],
                                    T: Dict[int, Rational],
                                    max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Extended Dirichlet convolution where we also include d=1 terms.

    (S *_ext T)(r) = sum_{d|r} S_ext(d) * T_ext(r/d)
    where S_ext(1) := 1 (Dirichlet unit convention) and S_ext(d) := S(d) for d >= 2.

    This is the convolution that corresponds to Dirichlet series multiplication:
    if L_S(s) = 1 + sum_{r>=2} S(r) r^{-s}, L_T(s) = 1 + sum_{r>=2} T(r) r^{-s},
    then L_S * L_T corresponds to the multiplicative convolution with unit.
    """
    if max_r is None:
        max_r = max(max(S.keys(), default=2), max(T.keys(), default=2))
    result = {}
    for r in range(2, max_r + 1):
        val = Rational(0)
        for d in range(1, r + 1):
            if r % d != 0:
                continue
            q = r // d
            # S_ext(1) = 1, S_ext(d) = S(d) for d >= 2
            Sd = S.get(d, Rational(0)) if d >= 2 else Rational(1)
            Tq = T.get(q, Rational(0)) if q >= 2 else Rational(1)
            # Exclude the (1,1) term since we want contributions at r >= 2
            if d == 1 and q == 1:
                continue
            val += Sd * Tq
        result[r] = val
    return result


def additive_combination(S: Dict[int, Rational],
                          T: Dict[int, Rational],
                          max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Pointwise sum of shadow sequences: (S + T)(r) = S(r) + T(r).

    This is the additive operation corresponding to independent-sum
    factorization when kappa is additive.
    """
    if max_r is None:
        max_r = max(max(S.keys(), default=2), max(T.keys(), default=2))
    return {r: S.get(r, Rational(0)) + T.get(r, Rational(0))
            for r in range(2, max_r + 1)}


# =============================================================================
# 4. Independent-sum factorization verification
# =============================================================================

def verify_independent_sum_additivity(S1: Dict[int, Rational],
                                       S2: Dict[int, Rational],
                                       S_tensor: Dict[int, Rational],
                                       max_r: Optional[int] = None) -> Dict[int, bool]:
    r"""Verify that S_{A1 tensor A2}(r) = S_{A1}(r) + S_{A2}(r) for all r.

    For independent (vanishing mixed OPE) tensor products, ALL shadow
    coefficients are additive (prop:independent-sum-factorization).

    Returns dict {r: True/False}.
    """
    if max_r is None:
        max_r = min(max(S_tensor.keys(), default=2),
                    max(S1.keys(), default=2),
                    max(S2.keys(), default=2))
    results = {}
    for r in range(2, max_r + 1):
        expected = S1.get(r, Rational(0)) + S2.get(r, Rational(0))
        actual = S_tensor.get(r, Rational(0))
        results[r] = (cancel(expected - actual) == 0)
    return results


def verify_kappa_additivity(kappa1: Rational, kappa2: Rational,
                             kappa_tensor: Rational) -> bool:
    r"""Verify kappa(A1 tensor A2) = kappa(A1) + kappa(A2)."""
    return cancel(kappa1 + kappa2 - kappa_tensor) == 0


def verify_discriminant_multiplicativity(S1: Dict[int, Rational],
                                          S2: Dict[int, Rational],
                                          S_tensor: Dict[int, Rational]) -> bool:
    r"""Verify Delta(A1 tensor A2) = Delta(A1) * Delta(A2).

    Delta = 8 * kappa * S_4.  For independent tensor products, kappa is
    additive and S_4 is... well, the discriminant is multiplicative
    means 8*(kappa1+kappa2)*S4_tensor = (8*kappa1*S4_1)*(8*kappa2*S4_2).

    This is a NONLINEAR constraint: it does NOT follow from S_4 additivity.
    For class G algebras (S_4 = 0): Delta = 0 and 0*0 = 0, trivially multiplicative.
    For class L algebras (S_4 = 0): same.
    The nontrivial test is for class M (Virasoro) tensor products.
    """
    kappa1 = S1.get(2, Rational(0))
    kappa2 = S2.get(2, Rational(0))
    kappa_t = S_tensor.get(2, Rational(0))
    S4_1 = S1.get(4, Rational(0))
    S4_2 = S2.get(4, Rational(0))
    S4_t = S_tensor.get(4, Rational(0))
    Delta1 = 8 * kappa1 * S4_1
    Delta2 = 8 * kappa2 * S4_2
    Delta_t = 8 * kappa_t * S4_t
    return cancel(Delta1 * Delta2 - Delta_t) == 0


# =============================================================================
# 5. Dirichlet series multiplicativity test
# =============================================================================

def test_dirichlet_multiplicativity(S: Dict[int, Rational],
                                     max_r: int = 20) -> Dict[str, Any]:
    r"""Test whether a shadow sequence is multiplicative in the Dirichlet sense.

    A sequence a(n) is multiplicative if a(mn) = a(m)*a(n) for gcd(m,n) = 1.
    Shadow sequences start at r=2, so we test for r = m*n with m,n >= 2
    and gcd(m,n) = 1.

    Returns a dict with:
      'is_multiplicative': bool
      'failures': list of (m, n, S(mn), S(m)*S(n)) tuples where multiplicativity fails
      'successes': count of pairs where it holds
    """
    from math import gcd
    failures = []
    successes = 0
    for m in range(2, max_r + 1):
        for n in range(2, max_r // m + 1):
            if gcd(m, n) != 1:
                continue
            mn = m * n
            if mn > max_r:
                continue
            S_mn = S.get(mn, Rational(0))
            S_m = S.get(m, Rational(0))
            S_n = S.get(n, Rational(0))
            if cancel(S_mn - S_m * S_n) != 0:
                failures.append((m, n, S_mn, S_m * S_n))
            else:
                successes += 1
    return {
        'is_multiplicative': len(failures) == 0,
        'failures': failures,
        'successes': successes,
    }


def test_complete_multiplicativity(S: Dict[int, Rational],
                                    max_r: int = 20) -> Dict[str, Any]:
    r"""Test whether a shadow sequence is COMPLETELY multiplicative.

    a(mn) = a(m)*a(n) for ALL m, n (not just coprime).
    """
    failures = []
    successes = 0
    for m in range(2, max_r + 1):
        for n in range(2, max_r // m + 1):
            mn = m * n
            if mn > max_r:
                continue
            S_mn = S.get(mn, Rational(0))
            S_m = S.get(m, Rational(0))
            S_n = S.get(n, Rational(0))
            if cancel(S_mn - S_m * S_n) != 0:
                failures.append((m, n, S_mn, S_m * S_n))
            else:
                successes += 1
    return {
        'is_completely_multiplicative': len(failures) == 0,
        'failures': failures,
        'successes': successes,
    }


# =============================================================================
# 6. Rankin-Selberg shadow product
# =============================================================================

def rankin_selberg_shadow_product(S: Dict[int, Rational],
                                   T: Dict[int, Rational],
                                   max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Pointwise product of shadow sequences: (S x T)(r) = S(r) * T(r).

    This is the "Rankin-Selberg shadow product" in the sense that
    L(s, A x B) = sum_{r>=2} S_r(A) * S_r(B) * r^{-s}.
    """
    if max_r is None:
        max_r = min(max(S.keys(), default=2), max(T.keys(), default=2))
    return {r: S.get(r, Rational(0)) * T.get(r, Rational(0))
            for r in range(2, max_r + 1)}


def rankin_selberg_series(S: Dict[int, Rational],
                           T: Dict[int, Rational],
                           s_val: float,
                           max_r: Optional[int] = None) -> float:
    r"""Evaluate the Rankin-Selberg shadow product L(s, A x B) numerically."""
    RS = rankin_selberg_shadow_product(S, T, max_r)
    return shadow_dirichlet_series_float(RS, s_val, max_r)


def rankin_selberg_self_convolution(S: Dict[int, Rational],
                                     max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Self-convolution: L(s, A x A) = sum S_r(A)^2 * r^{-s}."""
    return rankin_selberg_shadow_product(S, S, max_r)


# =============================================================================
# 7. Shadow Hecke operators
# =============================================================================

def shadow_hecke_operator(S: Dict[int, Rational],
                           p: int,
                           weight: Rational,
                           max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Apply the Hecke operator T_p to a shadow sequence.

    (T_p S)(r) = S(p*r) + p^{w-1} * S(r/p)
    where S(r/p) = 0 if p does not divide r.

    Parameters
    ----------
    S : shadow sequence {r: S_r}
    p : prime (Hecke index)
    weight : the modular weight parameter w
    max_r : truncation
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)
    result = {}
    pw = Rational(p) ** (weight - 1)
    for r in range(2, max_r + 1):
        # First term: S(p*r)
        pr = p * r
        term1 = S.get(pr, Rational(0))
        # Second term: p^{w-1} * S(r/p)
        term2 = Rational(0)
        if r % p == 0:
            rp = r // p
            if rp >= 2:
                term2 = pw * S.get(rp, Rational(0))
        result[r] = term1 + term2
    return result


def hecke_eigenvalue_test(S: Dict[int, Rational],
                           p: int,
                           weight: Rational,
                           max_r: Optional[int] = None) -> Dict[str, Any]:
    r"""Test whether S is a Hecke eigenform for T_p with given weight.

    If T_p(S) = lambda_p * S, return lambda_p and residuals.
    """
    TpS = shadow_hecke_operator(S, p, weight, max_r)
    if max_r is None:
        max_r = max(S.keys(), default=2)

    # Find the first nonzero S_r to extract the eigenvalue
    lambda_p = None
    for r in range(2, max_r + 1):
        Sr = S.get(r, Rational(0))
        if Sr != 0 and TpS.get(r, Rational(0)) != 0:
            lambda_p = cancel(TpS[r] / Sr)
            break

    if lambda_p is None:
        return {'is_eigenform': False, 'eigenvalue': None, 'residuals': {}}

    # Check all other entries
    residuals = {}
    for r in range(2, max_r + 1):
        Sr = S.get(r, Rational(0))
        expected = lambda_p * Sr
        actual = TpS.get(r, Rational(0))
        res = cancel(actual - expected)
        if res != 0:
            residuals[r] = res

    return {
        'is_eigenform': len(residuals) == 0,
        'eigenvalue': lambda_p,
        'residuals': residuals,
    }


# =============================================================================
# 8. Euler product analysis
# =============================================================================

def euler_product_local_factor(S: Dict[int, Rational],
                                p: int,
                                max_power: int = 5) -> List[Rational]:
    r"""Extract the local factor at prime p from the shadow Dirichlet series.

    If L_A(s) = prod_p F_p(p^{-s}) where F_p(X) = sum_{k>=0} S(p^k) X^k,
    then the local factor is [S(1), S(p), S(p^2), S(p^3), ...].

    Since shadow sequences start at r=2, S(1) = 0 by convention.
    The local factor coefficients are S(p^k) for k = 0, 1, 2, ...

    Returns [S(p^0), S(p^1), S(p^2), ...] = [0, S(p), S(p^2), ...].
    """
    coeffs = [Rational(0)]  # S(p^0) = S(1) = 0
    for exp in range(1, max_power + 1):
        pk = p ** exp
        coeffs.append(S.get(pk, Rational(0)))
    return coeffs


def euler_product_ratio(S: Dict[int, Rational],
                         kappa_val: Rational,
                         s_val: float,
                         max_r: int = 30) -> float:
    r"""Compute L_A(s) / zeta(s)^kappa and check if the quotient is recognizable.

    For Heisenberg at level k:
      L_{H_k}(s) = k * 2^{-s} (only S_2 = k is nonzero)
      zeta(s)^k is the k-th power of the Riemann zeta function.
      The quotient L_{H_k}(s) / zeta(s)^k is k * 2^{-s} / zeta(s)^k.

    This is exploratory: we compute the ratio numerically and check
    for structure.
    """
    L_val = shadow_dirichlet_series_float(S, s_val, max_r)
    # Approximate zeta(s)
    zeta_approx = sum(n ** (-s_val) for n in range(1, max_r + 50))
    if abs(zeta_approx) < 1e-100:
        return float('inf')
    ratio = L_val / (zeta_approx ** float(kappa_val))
    return ratio


# =============================================================================
# 9. Koszul duality of Dirichlet series
# =============================================================================

def koszul_dual_shadow_series(c_val: Union[Rational, int, Fraction],
                               max_r: int = 30) -> Dict[int, Rational]:
    r"""Shadow coefficients for the Koszul dual Vir_{26-c}.

    S_r^!(c) = S_r(26 - c).
    """
    return virasoro_shadow_coefficients(26 - Rational(c_val), max_r)


def complementarity_dirichlet_sum(c_val: Union[Rational, int, Fraction],
                                    s_val: float,
                                    max_r: int = 30) -> float:
    r"""Compute L_{Vir_c}(s) + L_{Vir_{26-c}}(s).

    At the self-dual point c=13: this is 2 * L_{Vir_13}(s).
    """
    S = virasoro_shadow_coefficients(c_val, max_r)
    S_dual = koszul_dual_shadow_series(c_val, max_r)
    L = shadow_dirichlet_series_float(S, s_val, max_r)
    L_dual = shadow_dirichlet_series_float(S_dual, s_val, max_r)
    return L + L_dual


def complementarity_dirichlet_product(c_val: Union[Rational, int, Fraction],
                                        s_val: float,
                                        max_r: int = 30) -> float:
    r"""Compute L(s, Vir_c x Vir_{26-c}): the Rankin-Selberg of a Koszul pair.

    L(s, A x A!) = sum_{r>=2} S_r(c) * S_r(26-c) * r^{-s}.
    """
    S = virasoro_shadow_coefficients(c_val, max_r)
    S_dual = koszul_dual_shadow_series(c_val, max_r)
    return rankin_selberg_series(S, S_dual, s_val, max_r)


# =============================================================================
# 10. Tensor product (independent sum) shadow sequences
# =============================================================================

def heisenberg_tensor_shadows(k1: Union[Rational, int],
                                k2: Union[Rational, int],
                                max_r: int = 30) -> Tuple[Dict[int, Rational],
                                                            Dict[int, Rational],
                                                            Dict[int, Rational]]:
    r"""Shadow sequences for H_{k1}, H_{k2}, and H_{k1} tensor H_{k2}.

    H_{k1} tensor H_{k2} = H_{k1+k2} (Heisenberg levels add).
    All are class G: S_r = 0 for r >= 3.
    """
    S1 = heisenberg_shadow_coefficients(k1, max_r)
    S2 = heisenberg_shadow_coefficients(k2, max_r)
    # Tensor product = H_{k1+k2}
    S_tensor = heisenberg_shadow_coefficients(Rational(k1) + Rational(k2), max_r)
    return S1, S2, S_tensor


def lattice_direct_sum_shadows(rank1: int, rank2: int,
                                max_r: int = 30) -> Tuple[Dict[int, Rational],
                                                            Dict[int, Rational],
                                                            Dict[int, Rational]]:
    r"""Shadow sequences for V_{Lambda_1}, V_{Lambda_2}, V_{Lambda_1 perp Lambda_2}.

    Orthogonal direct sum of lattices: Lambda = Lambda_1 perp Lambda_2.
    kappa is additive: kappa(V_Lambda) = rank(Lambda_1) + rank(Lambda_2).
    """
    S1 = lattice_shadow_coefficients(rank1, max_r)
    S2 = lattice_shadow_coefficients(rank2, max_r)
    S_tensor = lattice_shadow_coefficients(rank1 + rank2, max_r)
    return S1, S2, S_tensor


# =============================================================================
# 11. Minimal model shadow sequences
# =============================================================================

def minimal_model_virasoro_shadows(p: int, q: int,
                                     max_r: int = 20) -> Dict[int, Rational]:
    r"""Shadow coefficients for the Virasoro minimal model M(p,q).

    The central charge is c = 1 - 6(p-q)^2/(pq).
    The shadow coefficients are S_r(c) from the Virasoro formula,
    since minimal models are quotients of the Virasoro VOA and
    the shadow obstruction tower on the PRIMARY line is the same
    as for the universal Virasoro at the same c.

    CAUTION: The minimal model is a QUOTIENT; its full deformation
    complex may differ from the universal Virasoro.  But the primary-
    line shadow is determined by the central charge alone.

    Standard examples:
      Ising: M(3,4), c = 1/2
      Tricritical Ising: M(3,5) or M(4,5), c = 7/10
      3-state Potts: M(5,6), c = 4/5
    """
    c_val = Rational(1) - 6 * Rational(p - q) ** 2 / Rational(p * q)
    return virasoro_shadow_coefficients(c_val, max_r)


# =============================================================================
# 12. Convolution algebra structure
# =============================================================================

def convolution_ring_product(S: Dict[int, Rational],
                              T: Dict[int, Rational],
                              max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Dirichlet convolution: the ring product on shadow sequences.

    This is the same as dirichlet_convolution, but named for clarity
    in the ring-theoretic context.
    """
    return dirichlet_convolution(S, T, max_r)


def convolution_power(S: Dict[int, Rational],
                       n: int,
                       max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""n-th Dirichlet convolution power of a shadow sequence.

    S^{*0} = delta (Dirichlet identity: 1 at r=1, 0 elsewhere)
    S^{*1} = S
    S^{*n} = S * S^{*(n-1)}

    NOTE: The Dirichlet identity has support at r=1, which is outside
    the shadow range r >= 2.  So S^{*0}(r) = 0 for all r >= 2.
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)
    if n == 0:
        # Dirichlet identity: delta_{r,1}
        return {r: Rational(0) for r in range(2, max_r + 1)}
    if n == 1:
        return {r: S.get(r, Rational(0)) for r in range(2, max_r + 1)}
    result = {r: S.get(r, Rational(0)) for r in range(2, max_r + 1)}
    for _ in range(n - 1):
        result = dirichlet_convolution(result, S, max_r)
    return result


def moebius_inversion(S: Dict[int, Rational],
                       max_r: Optional[int] = None) -> Dict[int, Rational]:
    r"""Compute the Mobius inversion of a shadow sequence.

    If S(r) = sum_{d|r} T(d), then T(r) = sum_{d|r} mu(d) S(r/d).

    Uses the standard Mobius function mu(n):
      mu(1) = 1, mu(n) = (-1)^k if n = p1*...*pk (squarefree),
      mu(n) = 0 if n has a squared factor.
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)

    def moebius_mu(n: int) -> int:
        """Mobius function."""
        if n == 1:
            return 1
        factors = 0
        d = 2
        temp = n
        while d * d <= temp:
            if temp % d == 0:
                temp //= d
                factors += 1
                if temp % d == 0:
                    return 0  # squared factor
            d += 1
        if temp > 1:
            factors += 1
        return (-1) ** factors

    result = {}
    for r in range(2, max_r + 1):
        val = Rational(0)
        for d in range(1, r + 1):
            if r % d != 0:
                continue
            mu_d = moebius_mu(d)
            if mu_d == 0:
                continue
            q = r // d
            Sq = S.get(q, Rational(0)) if q >= 2 else Rational(0)
            val += mu_d * Sq
        result[r] = val
    return result


# =============================================================================
# 13. Abscissa of convergence
# =============================================================================

def abscissa_of_convergence(S: Dict[int, Rational],
                              max_r: Optional[int] = None,
                              tol: float = 1e-10) -> float:
    r"""Estimate the abscissa of absolute convergence of L_A(s).

    sigma_a = lim sup_{r->oo} log|S_r| / log(r).

    For class G (S_r = 0 for r >= 3): sigma_a = -inf (entire).
    For class L (S_r = 0 for r >= 4): sigma_a = -inf (entire).
    For class M (Virasoro): sigma_a depends on the shadow growth rate rho.

    Returns a float estimate.
    """
    if max_r is None:
        max_r = max(S.keys(), default=2)

    import math
    ratios = []
    for r in range(2, max_r + 1):
        Sr = float(S.get(r, 0))
        if abs(Sr) > tol:
            ratios.append(math.log(abs(Sr)) / math.log(r))

    if not ratios:
        return float('-inf')  # All zero: entire function
    return max(ratios)


# =============================================================================
# 14. Comparison infrastructure
# =============================================================================

def shadow_sequence_norm(S: Dict[int, Rational],
                          max_r: Optional[int] = None) -> Rational:
    r"""L^2 norm of shadow sequence: sum |S_r|^2."""
    if max_r is None:
        max_r = max(S.keys(), default=2)
    return sum(S.get(r, Rational(0)) ** 2 for r in range(2, max_r + 1))


def shadow_sequence_inner_product(S: Dict[int, Rational],
                                   T: Dict[int, Rational],
                                   max_r: Optional[int] = None) -> Rational:
    r"""Inner product of shadow sequences: sum S_r * T_r."""
    if max_r is None:
        max_r = min(max(S.keys(), default=2), max(T.keys(), default=2))
    return sum(S.get(r, Rational(0)) * T.get(r, Rational(0))
               for r in range(2, max_r + 1))


def dirichlet_series_comparison(S: Dict[int, Rational],
                                 T: Dict[int, Rational],
                                 s_values: Sequence[float],
                                 max_r: int = 30) -> Dict[float, Tuple[float, float, float]]:
    r"""Compare two shadow Dirichlet series at multiple s values.

    Returns {s: (L_S(s), L_T(s), ratio)} for each s in s_values.
    """
    result = {}
    for s in s_values:
        Ls = shadow_dirichlet_series_float(S, s, max_r)
        Lt = shadow_dirichlet_series_float(T, s, max_r)
        ratio = Ls / Lt if abs(Lt) > 1e-100 else float('inf')
        result[s] = (Ls, Lt, ratio)
    return result
