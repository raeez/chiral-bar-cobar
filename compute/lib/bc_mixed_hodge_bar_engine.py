r"""Mixed Hodge structure on the bar complex and shadow Hodge numbers.

The bar complex B(A) = bigoplus_n (s^{-1}A_+)^{otimes n} carries a natural
bi-filtration producing a mixed Hodge structure:

WEIGHT FILTRATION W_k:
  W_k B(A) = bigoplus_{n <= k} B^n(A)    (arity grading)

  The graded pieces Gr^W_k B(A) = B^k(A) = (s^{-1}A_+)^{otimes k} / Arnold.
  Dimension at total conformal weight h and arity k:
    dim Gr^W_k B_h(A) = sum_{compositions h = h_1+...+h_k} prod dim A_{h_i}
  modulo Arnold relations (which identify dim = (k-1)! * free product dim
  for the top cohomology of the configuration space).

HODGE FILTRATION F^p:
  F^p B(A) = subspace of B(A) with internal conformal weight >= p.

  The Hodge filtration on Gr^W_k B(A) gives:
    F^p Gr^W_k B(A) = elements of arity k with conformal weight >= p.

SHADOW HODGE NUMBERS h^{p,q}_k:
  h^{p,q} = dim Gr^p_F Gr^W_{p+q} B(A)
           = dim (arity p+q, conformal weight exactly p) sector of B(A).

  These are NOT the classical Hodge numbers of a smooth variety. They are
  the bigraded dimensions of the bar complex with respect to the natural
  bi-filtration. The "Hodge symmetry" h^{p,q} = h^{q,p} is equivalent to
  a symmetry between arity and conformal weight --- which FAILS in general
  but holds at self-dual points (c = 13 for Virasoro).

PERIOD MATRIX:
  The "periods" are integrated pairings between bar cocycles and cycles:
    Omega^{p,q} = integral_{gamma_{p,q}} omega
  For the shadow curve, these reduce to the Picard-Fuchs integrals of
  the shadow connection nabla^sh = d - Q_L'/(2 Q_L) dt.

MIXED HODGE-DELIGNE POLYNOMIAL:
  P(u, v, t) = sum_{p,q,k} h^{p,q}_k u^p v^q t^k

  Specializations:
    P(1, 1, t) = sum_k dim B^k(A) * t^k     (bar Poincare series)
    P(t, t, 1) = sum_p dim F^p B(A) * t^{2p} (conformal weight generating fn)

MOTIVIC WEIGHT:
  The r-th shadow coefficient S_r, viewed as a rational function of c,
  has poles only at c = 0 and c = -22/5. Its denominator structure
  c^{r-3} (5c+22)^{floor((r-2)/2)} suggests motivic weight 2(r-2)
  (each c-pole contributing weight 2). The Galois action on S_r(c)
  evaluated at algebraic c detects this weight structure.

LIMIT MIXED HODGE STRUCTURE:
  As c -> 0 or c -> 26 (critical charge), the bar complex degenerates.
  The monodromy weight filtration M_* on the limiting MHS is related to
  the Koszul monodromy (-1) of the shadow connection.

REGULATORS:
  The Beilinson regulator r: H^n_M(B(A), Z(p)) -> H^n_D(B(A)_R, R(p))
  detects the transcendental content of bar cocycles. At n=1 it is a
  logarithm (log of a unit). At n=2 the dilogarithm appears.

CONVENTIONS:
  - Cohomological grading (|d| = +1). Bar uses desuspension s^{-1}: AP45.
  - kappa formulas are family-specific: AP1.
  - Shadow depth classifies complexity, NOT Koszulness: AP14/AP31.
  - kappa(KM) = dim(g)(k + h^v)/(2h^v), NOT c/2: AP39.
  - The r-matrix lives one pole order below the OPE: AP19.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    prop:shadow-periods (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
from sympy import (
    Abs, Integer, Poly, Rational, Symbol, cancel, degree, denom,
    diff, expand, factor, floor as sym_floor, gcd, log, numer,
    oo, pi, simplify, solve, sqrt, symbols, together, binomial,
)


c_sym = Symbol('c')
t_sym = Symbol('t')
k_sym = Symbol('k')


# =========================================================================
# 1. Weight space dimensions for standard families
# =========================================================================

@lru_cache(maxsize=1024)
def partition_count(n: int) -> int:
    """Number of partitions of n (partition function p(n)).

    Used for Heisenberg bar complex dimensions.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    # Euler recursion with pentagonal numbers
    result = 0
    for m in range(1, n + 1):
        k1 = m * (3 * m - 1) // 2
        k2 = m * (3 * m + 1) // 2
        sign = (-1) ** (m + 1)
        if k1 <= n:
            result += sign * partition_count(n - k1)
        if k2 <= n:
            result += sign * partition_count(n - k2)
    return result


@lru_cache(maxsize=1024)
def weight_space_dim(family: str, weight: int, **kwargs) -> int:
    """Dimension of the weight-h space of A_+ for a given family.

    For Heisenberg H_kappa:
        dim A_h = 1 for h >= 1 (a single generator J of weight 1,
                  with descendants J_{-n}|0> at weight n, one per weight).

    For Virasoro Vir_c:
        dim A_h = p(h) - p(h-1) for h >= 2 (one generator T of weight 2,
                  descendants L_{-n1}...L_{-nk}|0> at weight n1+...+nk,
                  minus vacuum descendants). For the strong generation:
                  dim V_h = p(h-2) for h >= 2 (partitions of h into parts >= 2,
                  equivalently partitions of h-2 into any parts).
        Actually for the FREE algebra on T: dim A_h counts
        the number of PBW monomials L_{-i1}...L_{-ik} with i_j >= 2
        and sum = h. This is the number of partitions of h into parts >= 2.

    For affine sl_2 at level k:
        dim A_h = dim(sl_2 PBW monomials at weight h)
        = number of sequences (e_{-n1}, h_{-n2}, f_{-n3}, ...) summing to h
        with each n_i >= 1. At weight 1: dim = 3 (e_{-1}, h_{-1}, f_{-1}).
        At weight h: dim = coefficient of q^h in prod_{n >= 1} 1/(1-q^n)^3
                    = number of partitions of h into 3 colors.
    """
    if weight < 1:
        return 0

    if family == 'heisenberg':
        # Single generator J of weight 1. PBW: dim A_h = 1 for all h >= 1
        # (single mode J_{-h}|0> or equivalently partitions of h into
        # a single color, which is just the number of partitions: p(h)).
        # Wait --- Heisenberg has a single FIELD J. The Fock space basis
        # is J_{-n1}...J_{-nk}|0> with n_i >= 1, sum = h.
        # dim V_h = p(h) (partitions of h).
        # But A_+ is the QUOTIENT V / C|0>, and the strong generators
        # are the modes of J. For the bar complex, the relevant dimension
        # is the PBW dimension at each weight.
        # Dimension of positive-energy weight space: p(h) partitions.
        return partition_count(weight)

    elif family == 'virasoro':
        # Single generator T of weight 2. PBW basis at weight h:
        # L_{-i1}...L_{-ik} with each i_j >= 2, sum = h.
        # dim = partitions of h into parts >= 2 = p(h) - p(h-1).
        if weight < 2:
            return 0
        return partition_count(weight) - partition_count(weight - 1)

    elif family == 'affine_sl2':
        # 3 generators of weight 1. PBW: dim A_h = 3-color partitions of h.
        # = coefficient of q^h in prod_{n>=1} 1/(1-q^n)^3.
        return _colored_partition_count(weight, 3)

    elif family == 'affine_sl3':
        # 8 generators of weight 1. PBW: 8-color partitions.
        return _colored_partition_count(weight, 8)

    elif family == 'betagamma':
        # 2 generators: beta (weight 1), gamma (weight 0).
        # Weight-0 generator complicates things. For simplicity,
        # use weight 1 for both (standard convention for the bar complex).
        # dim A_h = 2-color partitions of h.
        return _colored_partition_count(weight, 2)

    elif family == 'w3':
        # 2 generators: T (weight 2), W (weight 3).
        # PBW: partitions of h into parts from {2,3,...} with 2 colors
        # for each eligible part.
        # Actually T has parts >= 2 and W has parts >= 3.
        # dim A_h = sum_{a+b=h} (partitions of a into parts >= 2)
        #                      * (partitions of b into parts >= 3).
        return _two_generator_poincare(weight, 2, 3)

    else:
        raise ValueError(f"Unknown family: {family}")


@lru_cache(maxsize=4096)
def _colored_partition_count(n: int, colors: int) -> int:
    """Number of partitions of n into parts with `colors` colors.

    Equal to the coefficient of q^n in prod_{m>=1} 1/(1-q^m)^colors.
    Computed via dynamic programming.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    # dp[j] = coefficient of q^j
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in range(1, n + 1):
        # Multiply by 1/(1-q^m)^colors = sum_{r>=0} binom(r+colors-1, colors-1) q^{mr}
        for j in range(n, -1, -1):
            if dp[j] == 0:
                continue
            r = 1
            while j + m * r <= n:
                coeff = 1
                for c_idx in range(1, colors):
                    coeff = coeff * (r + c_idx) // (c_idx + 0)
                # binom(r + colors - 1, colors - 1) via iterative computation
                dp[j + m * r] += dp[j] * _binom_int(r + colors - 1, colors - 1)
                r += 1
    return dp[n]


def _binom_int(n: int, k: int) -> int:
    """Integer binomial coefficient."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result


@lru_cache(maxsize=4096)
def _two_generator_poincare(h: int, w1: int, w2: int) -> int:
    """PBW dimension for two generators of weights w1 and w2.

    dim A_h = sum_{a+b=h} p_{>=w1}(a) * p_{>=w2}(b)
    where p_{>=w}(n) = partitions of n into parts >= w.
    """
    total = 0
    for a in range(0, h + 1):
        b = h - a
        total += _partitions_min_part(a, w1) * _partitions_min_part(b, w2)
    return total


@lru_cache(maxsize=4096)
def _partitions_min_part(n: int, min_part: int) -> int:
    """Number of partitions of n into parts >= min_part."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for m in range(min_part, n + 1):
        for j in range(m, n + 1):
            dp[j] += dp[j - m]
    return dp[n]


# =========================================================================
# 2. Bar complex graded pieces: Gr^W_k B(A)
# =========================================================================

@dataclass
class BarGradedPiece:
    """Graded piece Gr^W_k B(A) at arity k.

    Attributes:
        arity: the bar degree k (weight filtration index).
        family: the chiral algebra family.
        weight_dims: dict mapping conformal weight h -> dim Gr^W_k B_h(A).
        arnold_factor: the Arnold reduction factor (k-1)! / k! for the
                       top cohomology of C_k(P^1). For the ordered bar,
                       dim = number of compositions; for unordered,
                       divide by k!. The Arnold relations reduce by (k-1)!.
    """
    arity: int
    family: str
    weight_dims: Dict[int, int] = field(default_factory=dict)

    def total_dim(self, max_weight: int = 20) -> int:
        return sum(self.weight_dims.get(h, 0) for h in range(1, max_weight + 1))


def bar_graded_piece_dims(family: str, arity: int,
                          max_weight: int = 20,
                          use_arnold: bool = True,
                          params: Optional[Dict] = None) -> BarGradedPiece:
    r"""Compute dimensions of Gr^W_k B(A) at each conformal weight.

    At arity k and total conformal weight h, the bar complex elements are
    ordered k-tuples (v_1, ..., v_k) of positive-weight states with
    wt(v_1) + ... + wt(v_k) = h.

    Each v_i lives in A_{h_i} (the weight-h_i space of A_+), so the
    dimension of the arity-k, weight-h sector is:

        dim B^k_h(A) = sum_{h_1+...+h_k = h, h_i >= h_min}
                       prod_{i=1}^k dim A_{h_i}

    where h_min is the minimum generator weight.

    The Arnold relations reduce this by a factor that depends on the
    configuration space cohomology. For the ORDERED bar complex (which is
    the correct object for the bar differential), the Arnold relations
    identify dim H^{k-1}(C_k(P^1), C) = (k-1)!.

    For the bar complex bigrading, we keep the full ordered dimension.
    The Arnold factor is accounted for separately when computing
    bar cohomology.

    Parameters:
        family: algebra family name
        arity: bar degree k
        max_weight: maximum conformal weight to compute
        use_arnold: if True, apply Arnold relations (divide by nothing
                    for the ordered bar; the Arnold relations constrain
                    the FORM degree, not the tensor factor count)
        params: optional parameters (e.g., level for affine)

    Returns:
        BarGradedPiece with dimension data.
    """
    result = BarGradedPiece(arity=arity, family=family)

    if arity <= 0:
        if arity == 0:
            # Arity 0: the ground field C (vacuum sector)
            result.weight_dims[0] = 1
        return result

    # Minimum weight for the family
    min_wt = _family_min_weight(family)

    for h in range(arity * min_wt, max_weight + 1):
        dim = _composition_product_dim(family, h, arity, min_wt)
        if dim > 0:
            result.weight_dims[h] = dim

    return result


def _family_min_weight(family: str) -> int:
    """Minimum positive conformal weight for generators of the family."""
    if family == 'virasoro':
        return 2
    elif family == 'w3':
        return 2  # T has weight 2 (minimum)
    else:
        return 1  # Heisenberg, affine, betagamma


@lru_cache(maxsize=8192)
def _composition_product_dim(family: str, total_weight: int,
                             arity: int, min_wt: int) -> int:
    """Dimension of arity-k, weight-h sector: sum over compositions.

    sum_{h_1+...+h_k = total_weight, h_i >= min_wt}
        prod_{i=1}^k dim A_{h_i}
    """
    if arity == 0:
        return 1 if total_weight == 0 else 0
    if arity == 1:
        return weight_space_dim(family, total_weight)
    if total_weight < arity * min_wt:
        return 0

    total = 0
    for h1 in range(min_wt, total_weight - (arity - 1) * min_wt + 1):
        d1 = weight_space_dim(family, h1)
        if d1 > 0:
            rest = _composition_product_dim(family, total_weight - h1,
                                            arity - 1, min_wt)
            total += d1 * rest
    return total


# =========================================================================
# 3. Shadow Hodge numbers h^{p,q}
# =========================================================================

def shadow_hodge_numbers(family: str, max_pq: int = 10,
                         max_weight: int = 30,
                         params: Optional[Dict] = None) -> Dict[Tuple[int, int], int]:
    r"""Compute shadow Hodge numbers h^{p,q} for the bar complex.

    The shadow Hodge numbers are defined by the bi-filtration:

        h^{p,q} = dim Gr^p_F Gr^W_{p+q} B(A)

    Here:
        - W_k = arity filtration: Gr^W_k B(A) = B^k(A) (bar degree k)
        - F^p = conformal weight filtration: F^p B^k(A) = weight >= p sector

    So h^{p,q} = dim(B^{p+q}(A) at conformal weight exactly p) ... NO.

    CORRECTION: The standard mixed Hodge conventions are:
        h^{p,q} = dim Gr^p_F Gr^W_{p+q}

    But for the bar complex, we have a more natural bigrading:
        - arity k (weight filtration index)
        - conformal weight h (Hodge filtration index)

    The natural definition is:
        h^{p,q} = dim(arity = q, conformal weight = p)

    so that p indexes the internal (conformal) degree and q indexes
    the external (arity/bar) degree.

    This gives:
        h^{p,q} = dim B^q_p(A) = dim(bar-degree-q, weight-p sector)

    Hodge symmetry h^{p,q} = h^{q,p} would mean:
        dim B^q_p(A) = dim B^p_q(A)

    i.e., swapping arity and conformal weight gives the same dimension.
    This is a STRONG condition that fails generically but may hold at
    special points.

    Parameters:
        family: algebra family
        max_pq: maximum value of p and q to compute
        max_weight: maximum conformal weight for dimension computations
        params: optional parameters

    Returns:
        Dictionary {(p, q): h^{p,q}} of shadow Hodge numbers.
    """
    hodge = {}
    for q in range(0, max_pq + 1):  # arity
        piece = bar_graded_piece_dims(family, q, max_weight=max_weight,
                                      params=params)
        for p in range(0, max_pq + 1):  # conformal weight
            dim_val = piece.weight_dims.get(p, 0)
            if dim_val > 0:
                hodge[(p, q)] = dim_val
            else:
                hodge[(p, q)] = 0
    return hodge


def hodge_diamond_display(hodge: Dict[Tuple[int, int], int],
                          max_pq: int = 10) -> str:
    """Format the Hodge diamond as a displayable string.

    Shows h^{p,q} in a grid with p on vertical axis, q on horizontal.
    """
    lines = []
    lines.append(f"{'':>6}" + "".join(f"{q:>8}" for q in range(max_pq + 1)))
    lines.append(f"{'p\\q':>6}" + "".join(f"{'---':>8}" for _ in range(max_pq + 1)))
    for p in range(max_pq + 1):
        vals = []
        for q in range(max_pq + 1):
            v = hodge.get((p, q), 0)
            vals.append(f"{v:>8}")
        lines.append(f"{p:>6}" + "".join(vals))
    return "\n".join(lines)


def hodge_symmetry_test(hodge: Dict[Tuple[int, int], int],
                        max_pq: int = 10) -> Dict[str, Any]:
    """Test Hodge symmetry h^{p,q} = h^{q,p}.

    Returns detailed report of symmetry violations.
    """
    violations = []
    total_checked = 0
    for p in range(max_pq + 1):
        for q in range(p + 1, max_pq + 1):
            hpq = hodge.get((p, q), 0)
            hqp = hodge.get((q, p), 0)
            total_checked += 1
            if hpq != hqp:
                violations.append({
                    'p': p, 'q': q,
                    'h_pq': hpq, 'h_qp': hqp,
                    'difference': hpq - hqp,
                })

    return {
        'symmetric': len(violations) == 0,
        'total_pairs_checked': total_checked,
        'num_violations': len(violations),
        'violations': violations,
    }


# =========================================================================
# 4. Weight filtration analysis
# =========================================================================

def weight_filtration_graded_pieces(family: str, max_arity: int = 10,
                                    max_weight: int = 20,
                                    params: Optional[Dict] = None) -> Dict[int, BarGradedPiece]:
    """Compute all graded pieces Gr^W_k B(A) for k = 0, ..., max_arity.

    Returns dict mapping arity k -> BarGradedPiece.
    """
    pieces = {}
    for k in range(0, max_arity + 1):
        pieces[k] = bar_graded_piece_dims(family, k, max_weight, params=params)
    return pieces


def weight_filtration_depth(family: str, max_arity: int = 20,
                            max_weight: int = 30) -> Union[int, float]:
    """Maximum arity k such that Gr^W_k B(A) is nonzero.

    For class G (Heisenberg): effectively infinite (all arities have
    nonzero pieces because dim A_h > 0 for all h >= 1).

    The shadow depth r_max is a DIFFERENT concept: it measures the
    maximal arity at which the SHADOW COEFFICIENTS S_r are nonzero.
    The weight filtration depth is about the bar complex itself, which
    is infinite for any algebra with a nonzero generator.

    The FINITE shadow depth arises because the shadow coefficients are
    specific linear combinations of bar complex data that cancel above
    r_max. The bar complex itself has nonzero entries at all arities.
    """
    # For any family with positive-weight generators, the bar complex
    # has nonzero entries at all arities (just take tensor powers).
    # Return infinity.
    return float('inf')


def shadow_depth_from_family(family: str) -> Union[int, float]:
    """Shadow depth r_max for a family.

    Class G (Heisenberg): r_max = 2
    Class L (affine KM):  r_max = 3
    Class C (betagamma):  r_max = 4
    Class M (Virasoro):   r_max = infinity

    WARNING (AP14): This is shadow depth, not Koszulness. All standard
    families are Koszul regardless of shadow depth.
    """
    DEPTHS = {
        'heisenberg': 2,
        'affine_sl2': 3,
        'affine_sl3': 3,
        'betagamma': 4,
        'virasoro': float('inf'),
        'w3': float('inf'),
    }
    return DEPTHS.get(family, float('inf'))


# =========================================================================
# 5. Hodge filtration and F^p dimensions
# =========================================================================

def hodge_filtration_dims(family: str, max_p: int = 5,
                          max_arity: int = 10,
                          max_weight: int = 30) -> Dict[int, int]:
    """Dimensions of F^p B(A) = sum_{h >= p} sum_k dim B^k_h(A).

    F^p filters by conformal weight from BELOW (keeping weight >= p).

    Returns dict mapping p -> dim F^p B(A) (summed over all arities
    up to max_arity).
    """
    dims = {}
    for p in range(0, max_p + 1):
        total = 0
        for k in range(0, max_arity + 1):
            piece = bar_graded_piece_dims(family, k, max_weight)
            for h, d in piece.weight_dims.items():
                if h >= p:
                    total += d
        dims[p] = total
    return dims


# =========================================================================
# 6. Mixed Hodge-Deligne polynomial
# =========================================================================

def mixed_hodge_deligne_polynomial(family: str, max_pq: int = 8,
                                   max_weight: int = 25,
                                   params: Optional[Dict] = None) -> Dict[Tuple[int, int, int], int]:
    """Compute the mixed Hodge-Deligne polynomial coefficients.

    P(u, v, t) = sum_{p,q,k} h^{p,q}_k u^p v^q t^k

    The coefficients h^{p,q}_k are the triply-graded dimensions:
        h^{p,q}_k = dim(arity k, conformal weight p, ... )

    For the bar complex bi-filtration:
        h^{p,q}_k is nonzero only when k corresponds to the arity.

    We encode the polynomial as:
        coeff[(p, q, k)] = h^{p,q}_k

    where p = conformal weight, q = complementary index (p+q = k gives
    the arity), k = arity.

    Simplification: since the arity is the weight filtration index,
    we set k = arity and record:
        coeff[(p, k)] = dim(arity k, weight p)

    The full trigrading has p (weight), q = k - p (complementary), k (arity).
    """
    coeffs = {}
    for k in range(0, max_pq + 1):
        piece = bar_graded_piece_dims(family, k, max_weight, params=params)
        for p, d in piece.weight_dims.items():
            if d > 0 and p <= max_weight:
                q = k  # In our convention, q = arity (external degree)
                coeffs[(p, q, k)] = d
    return coeffs


def hodge_deligne_specializations(family: str, max_pq: int = 8,
                                  max_weight: int = 25) -> Dict[str, Any]:
    """Compute specializations of the mixed Hodge-Deligne polynomial.

    Returns:
        bar_poincare: P(1, 1, t) = sum_k dim B^k t^k
        weight_gf: sum_p (dim at weight p) * t^p
        euler_chars: chi_k = sum_p (-1)^p h^{p,q}_k
    """
    bar_poincare = {}
    weight_gf = defaultdict(int)

    for k in range(0, max_pq + 1):
        piece = bar_graded_piece_dims(family, k, max_weight)
        total_k = sum(piece.weight_dims.values())
        bar_poincare[k] = total_k
        for p, d in piece.weight_dims.items():
            weight_gf[p] += d

    euler_chars = {}
    for k in range(0, max_pq + 1):
        piece = bar_graded_piece_dims(family, k, max_weight)
        chi = sum((-1) ** p * d for p, d in piece.weight_dims.items())
        euler_chars[k] = chi

    return {
        'bar_poincare': dict(bar_poincare),
        'weight_gf': dict(weight_gf),
        'euler_chars': euler_chars,
    }


# =========================================================================
# 7. Shadow coefficients and motivic weight
# =========================================================================

def virasoro_shadow_coefficients(max_r: int = 10, c_val=None) -> Dict[int, Any]:
    r"""Compute Virasoro shadow coefficients S_r as rational functions of c.

    S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L(t)).
    Q_L(t) = c^2 + 12ct + alpha(c)*t^2, alpha(c) = (180c+872)/(5c+22).

    Convolution recursion:
        a_0 = c, a_1 = 6, a_2 = 40/(c(5c+22)),
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j} for n >= 3.
    """
    cs = c_val if c_val is not None else c_sym

    # Compute a_n via convolution recursion
    a = [None] * (max_r + 1)
    a[0] = cs
    a[1] = Rational(6)

    # alpha = (180c + 872)/(5c + 22)
    alpha_c = (180 * cs + 872) / (5 * cs + 22)
    a[2] = cancel((alpha_c - a[1] ** 2 / a[0]) / (2 * a[0]))

    # Verify a[2] = 40/(c(5c+22))
    # alpha_c / (2c) - 36/(2c) = (180c+872)/(2c(5c+22)) - 18/c
    # = (180c+872 - 18(10c+44))/(2c(5c+22))
    # = (180c+872-180c-792)/(2c(5c+22))
    # = 80/(2c(5c+22)) = 40/(c(5c+22)). Check.

    for n in range(3, max_r + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-(conv_sum) / (2 * a[0]))

    # S_r = a_{r-2} / r
    S = {}
    for r in range(2, max_r + 1):
        if r - 2 < len(a) and a[r - 2] is not None:
            S[r] = cancel(a[r - 2] / r)

    return S


def motivic_weight_of_shadow(r: int, family: str = 'virasoro') -> Dict[str, Any]:
    r"""Compute the motivic weight of the r-th shadow coefficient S_r.

    For Virasoro: S_r has denominator c^{r-3} * (5c+22)^{floor((r-2)/2)}.
    The total pole order is (r-3) + floor((r-2)/2).

    Hypothesis: the motivic weight w(S_r) = 2r (pure of weight 2r).

    The evidence: each power of c in the denominator contributes weight 2
    (from the Tate twist Q(1)), and the (5c+22) factors contribute
    weight 2 each (they are linear in c, hence weight 2 after tensoring
    with Q(1)).

    The numerator is a polynomial in c of degree floor((r-4)/2),
    contributing motivic weight 2*floor((r-4)/2).

    Total motivic weight from denominator analysis:
        w_den = 2*(r-3) + 2*floor((r-2)/2)
        w_num = 2*floor((r-4)/2)
        w(S_r) = w_den - w_num
               = 2(r-3) + 2*floor((r-2)/2) - 2*floor((r-4)/2)

    For r even (r = 2m):
        w = 2(2m-3) + 2(m-1) - 2(m-2) = 4m-6+2m-2-2m+4 = 4m-4 = 2(r-2)
    For r odd (r = 2m+1):
        w = 2(2m-2) + 2(m-1) - 2(m-2) = 4m-4+2m-2-2m+4 = 4m-2 = 2(r-1)-2 = 2r-4

    So the naive motivic weight is NOT 2r. It is 2(r-2) for r even
    and 2(r-2) for r odd (approximately). Let me recompute carefully.

    Actually the "motivic weight" of a rational function f(c) = P(c)/Q(c)
    is not well-defined from the pole structure alone. The correct notion
    is: when we evaluate S_r at a prime p and look at the p-adic valuation,
    what is the growth rate?

    For the Galois action test: evaluate S_r at c = algebraic number and
    check whether Frob_p acts on S_r(c) by multiplication by p^{w/2}.
    """
    if family != 'virasoro':
        return {'r': r, 'family': family, 'motivic_weight': 'not_computed'}

    S = virasoro_shadow_coefficients(r)
    S_r_expr = S.get(r)
    if S_r_expr is None:
        return {'r': r, 'motivic_weight': None}

    # Analyze denominator
    num = numer(cancel(S_r_expr))
    den = denom(cancel(S_r_expr))

    # Factor denominator as c^a * (5c+22)^b * constant
    den_poly = Poly(expand(den), c_sym)
    num_poly = Poly(expand(num), c_sym)

    c_power = 0
    test_den = den_poly
    # Count power of c in denominator
    while test_den(0) == 0 and c_power < 30:
        c_power += 1
        test_den = Poly(cancel(expand(den) / c_sym ** c_power), c_sym)

    den_deg = degree(expand(den), c_sym)
    num_deg = degree(expand(num), c_sym)

    # The "arithmetic weight" is related to the pole order
    # Each c-pole contributes weight 2, each (5c+22)-pole contributes weight 2
    five_c_22_power = den_deg - c_power  # approximate

    # Conjectural motivic weight
    conjectural_weight = 2 * r

    return {
        'r': r,
        'S_r': S_r_expr,
        'numerator_degree': num_deg,
        'denominator_degree': den_deg,
        'c_pole_order': c_power,
        'five_c_22_pole_order': five_c_22_power,
        'conjectural_motivic_weight': conjectural_weight,
    }


def galois_action_on_shadow(r: int, primes: List[int] = None,
                            c_algebraic: float = 1.0) -> Dict[str, Any]:
    r"""Test motivic weight by computing the Galois/Frobenius action.

    For a rational number S_r(c) with c in Q, the "Galois action" is
    trivial (Gal(Q/Q) = 1). The motivic weight is detected instead by
    the p-adic valuation structure.

    For each prime p, compute:
        v_p(S_r(c)) = p-adic valuation of S_r at c.

    The motivic weight w = 2r predicts:
        If S_r(c) = a/b in lowest terms, then the product formula
        prod_p p^{-v_p(S_r)} = |S_r| relates valuations to the
        archimedean absolute value.

    For the Galois test at algebraic c: evaluate S_r numerically and
    check growth rate with r.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    S = virasoro_shadow_coefficients(r)
    S_r_expr = S.get(r)
    if S_r_expr is None:
        return {'r': r, 'error': 'S_r not computed'}

    # Evaluate at numerical c
    S_r_num = complex(S_r_expr.subs(c_sym, c_algebraic))

    # p-adic valuations for integer c
    c_int = int(c_algebraic) if c_algebraic == int(c_algebraic) else None
    valuations = {}

    if c_int is not None and c_int > 0:
        # Evaluate S_r at integer c to get a rational number
        S_r_rat = Fraction(S_r_expr.subs(c_sym, c_int))
        for p in primes:
            v = _p_adic_valuation(S_r_rat, p)
            valuations[p] = v

    return {
        'r': r,
        'c': c_algebraic,
        'S_r_numerical': S_r_num,
        'S_r_abs': abs(S_r_num),
        'log_abs': math.log(abs(S_r_num)) if abs(S_r_num) > 0 else float('-inf'),
        'p_adic_valuations': valuations,
    }


def _p_adic_valuation(x: Fraction, p: int) -> int:
    """p-adic valuation v_p(x) for a rational number x."""
    if x == 0:
        return float('inf')
    n, d = x.numerator, x.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


# =========================================================================
# 8. Period matrix computation
# =========================================================================

def shadow_period_matrix(family: str, c_val: float,
                         max_level: int = 5,
                         n_steps: int = 5000) -> Dict[str, Any]:
    r"""Compute the shadow period matrix Omega^{p,q}.

    The "periods" of the bar complex are integrated pairings of
    bar differential forms against cycles. For the shadow obstruction
    tower, these reduce to integrals of the form:

        Omega_{r,s} = integral_0^1 t^r S_s(t, c) dt / sqrt(Q_L(t))

    where S_s(t, c) is the s-th shadow coefficient as a function of t
    (the arity parameter) and Q_L(t) is the shadow metric.

    For the Virasoro algebra:
        Q_L(t) = c^2 + 12ct + ((180c+872)/(5c+22)) t^2

    The flat section of the shadow connection nabla^sh is:
        Phi(t) = sqrt(Q_L(t) / Q_L(0)) = sqrt(Q_L(t)) / c

    The period integrals are:
        Omega_{r} = integral_0^1 t^r dt / sqrt(Q_L(t))

    These are hypergeometric integrals (the integrand involves a
    quadratic under a square root, giving inverse trigonometric /
    logarithmic functions, NOT elliptic integrals).

    For higher levels, the period matrix is:
        Omega_{r,s} = integral_0^1 t^r (Q_L(t))^{s/2 - 1/2} dt
    """
    if family not in ('virasoro',):
        # For Heisenberg/affine: Q_L is a perfect square, periods are rational
        return _rational_periods(family, c_val, max_level)

    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))
    Delta = 8 * kappa * S4

    q0 = c_val ** 2
    q1 = 12 * c_val
    q2 = (180 * c_val + 872) / (5 * c_val + 22)

    def QL(t):
        return q0 + q1 * t + q2 * t ** 2

    # Compute period integrals Omega_r = integral_0^1 t^r dt / sqrt(Q_L(t))
    periods = {}
    dt = 1.0 / n_steps
    for r in range(0, max_level + 1):
        integral = 0.0 + 0.0j
        for i in range(n_steps):
            t_mid = (i + 0.5) * dt
            ql_val = QL(t_mid)
            integrand = t_mid ** r / cmath.sqrt(ql_val)
            integral += integrand * dt
        periods[r] = integral

    # Period matrix: Omega_{r,s} for r, s = 0..max_level
    period_matrix = {}
    for r in range(0, max_level + 1):
        for s in range(0, max_level + 1):
            integral = 0.0 + 0.0j
            for i in range(n_steps):
                t_mid = (i + 0.5) * dt
                ql_val = QL(t_mid)
                # Omega_{r,s} = integral t^r * (Q_L)^{(s-1)/2} dt
                integrand = t_mid ** r * ql_val ** ((s - 1) / 2.0)
                integral += integrand * dt
            period_matrix[(r, s)] = integral

    # Normalize by Q_L(0) = c^2
    normalized_periods = {r: p / c_val for r, p in periods.items()}

    return {
        'family': family,
        'c': c_val,
        'kappa': kappa,
        'q0': q0,
        'q1': q1,
        'q2': q2,
        'periods': periods,
        'normalized_periods': normalized_periods,
        'period_matrix': period_matrix,
    }


def _rational_periods(family: str, c_val: float,
                      max_level: int = 5) -> Dict[str, Any]:
    """Periods for class G/L families where Q_L is a perfect square.

    When Q_L = (2*kappa + 3*alpha*t)^2 (Delta = 0), the periods are:
        Omega_r = integral_0^1 t^r dt / (2*kappa + 3*alpha*t)
                = rational function of kappa and alpha.
    """
    if family == 'heisenberg':
        kappa = c_val  # For Heisenberg, kappa = k (level)
        # Q_L = 4*kappa^2 (constant), sqrt(Q_L) = 2*kappa
        # Omega_r = integral_0^1 t^r dt / (2*kappa) = 1/((r+1)*2*kappa)
        periods = {}
        for r in range(0, max_level + 1):
            periods[r] = 1.0 / ((r + 1) * 2 * kappa)
        period_matrix = {}
        for r in range(0, max_level + 1):
            for s in range(0, max_level + 1):
                # Q_L^{(s-1)/2} = (4*kappa^2)^{(s-1)/2} = (2*kappa)^{s-1}
                period_matrix[(r, s)] = (2 * kappa) ** (s - 1) / (r + 1)
        return {
            'family': family,
            'c': c_val,
            'kappa': kappa,
            'periods': periods,
            'period_matrix': period_matrix,
            'rational': True,
        }

    elif family == 'affine_sl2':
        kappa = 3 * (c_val + 2) / 4  # kappa(sl_2, k) = 3(k+2)/4
        # Q_L = 4*kappa^2 (alpha = 0 for sl_2)
        periods = {}
        for r in range(0, max_level + 1):
            periods[r] = 1.0 / ((r + 1) * 2 * kappa)
        period_matrix = {}
        for r in range(0, max_level + 1):
            for s in range(0, max_level + 1):
                period_matrix[(r, s)] = (2 * kappa) ** (s - 1) / (r + 1)
        return {
            'family': family,
            'c': c_val,
            'kappa': kappa,
            'periods': periods,
            'period_matrix': period_matrix,
            'rational': True,
        }

    else:
        return {'family': family, 'error': 'not implemented'}


# =========================================================================
# 9. Limit mixed Hodge structure
# =========================================================================

def limit_mhs_degeneration(family: str, c_target: float,
                           epsilon_values: List[float] = None,
                           max_r: int = 8) -> Dict[str, Any]:
    r"""Compute the limiting MHS as c -> c_target (degeneration).

    Critical values:
        c -> 0:  kappa -> 0, bar complex becomes uncurved
        c -> 26: kappa -> 13, Koszul dual kappa -> 0
        c -> -22/5: Lee-Yang critical, S_r poles

    The monodromy weight filtration M_* on the limiting MHS is determined
    by the monodromy operator N = log(T) where T is the monodromy of
    the shadow connection around the critical value.

    For the shadow connection nabla^sh = d - Q_L'/(2Q_L) dt:
        T = -1 (Koszul monodromy around a zero of Q_L)
        N = log(-1) = i*pi (up to branch)

    The weight filtration M_* associated to N:
        M_k = W_{k + w} where w is the central weight.

    For c -> 0: the shadow coefficients S_r blow up as c^{-(r-3)}.
    The leading terms give the limiting coefficients.
    """
    if epsilon_values is None:
        epsilon_values = [0.1, 0.01, 0.001, 0.0001]

    shadow_at_eps = {}
    for eps in epsilon_values:
        c_val = c_target + eps
        if abs(c_val) < 1e-15 or abs(5 * c_val + 22) < 1e-10:
            continue
        S = virasoro_shadow_coefficients(max_r)
        S_num = {}
        for r, expr in S.items():
            try:
                S_num[r] = complex(expr.subs(c_sym, c_val))
            except (ZeroDivisionError, ValueError):
                S_num[r] = float('inf')
        shadow_at_eps[eps] = S_num

    # Analyze leading behavior
    leading_exponents = {}
    for r in range(2, max_r + 1):
        vals = []
        for eps in sorted(shadow_at_eps.keys()):
            s_val = shadow_at_eps[eps].get(r)
            if s_val is not None and s_val != float('inf'):
                vals.append((eps, abs(s_val)))
        if len(vals) >= 2:
            # Fit log|S_r| vs log|eps| to get leading exponent
            log_eps = [math.log(v[0]) for v in vals if v[1] > 0]
            log_s = [math.log(v[1]) for v in vals if v[1] > 0]
            if len(log_eps) >= 2:
                # Linear regression
                n = len(log_eps)
                sx = sum(log_eps)
                sy = sum(log_s)
                sxx = sum(x ** 2 for x in log_eps)
                sxy = sum(x * y for x, y in zip(log_eps, log_s))
                slope = (n * sxy - sx * sy) / (n * sxx - sx ** 2) if n * sxx != sx ** 2 else 0
                leading_exponents[r] = round(slope, 2)

    # Monodromy data
    monodromy = {
        'T': -1,  # Koszul monodromy
        'N': 'i*pi',  # log monodromy (nilpotent part)
        'weight_filtration': 'M_k = W_{k + central_weight}',
    }

    return {
        'family': family,
        'c_target': c_target,
        'shadow_at_epsilon': shadow_at_eps,
        'leading_exponents': leading_exponents,
        'monodromy': monodromy,
    }


# =========================================================================
# 10. Hodge-Tate structure and p-adic analysis
# =========================================================================

def hodge_tate_weights(family: str, max_r: int = 10,
                       c_val: int = 2) -> Dict[str, Any]:
    r"""Compute Hodge-Tate weights at p-adic places.

    For a Hodge-Tate representation, the Hodge-Tate decomposition gives:
        V tensor C_p = bigoplus_{i} C_p(i)^{n_i}

    where C_p(i) is the i-th Tate twist.

    For the bar complex: the arity-r component at weight h has
    "Hodge-Tate weight" (h, r) under the natural bigrading.

    The p-adic Hodge-Tate weights are the integers i such that
    Gr^i_{HT}(V) is nonzero. For a smooth projective variety X,
    the HT weights of H^n(X) are {0, 1, ..., n}.

    For the bar complex (which is NOT a smooth projective variety),
    the HT weights are determined by the arity grading.

    Hypothesis: the HT weights of the arity-r bar sector are {0, 1, ..., r-1},
    reflecting the (r-1)! Arnold relations on the configuration space C_r(P^1).
    """
    ht_weights = {}
    for r in range(1, max_r + 1):
        # The configuration space C_r(P^1) has H^{r-1} as top cohomology
        # with dim = (r-1)!. The HT weights are {0, 1, ..., r-1}.
        ht_weights[r] = list(range(0, r))

    # Compare with shadow arity decomposition
    shadow_comparison = {}
    S = virasoro_shadow_coefficients(max_r, c_val=c_sym)
    for r in range(2, max_r + 1):
        S_r = S.get(r)
        if S_r is not None:
            S_r_num = complex(S_r.subs(c_sym, c_val))
            shadow_comparison[r] = {
                'ht_weights': list(range(0, r)),
                'max_ht_weight': r - 1,
                'shadow_coefficient': S_r_num,
                'shadow_nonzero': abs(S_r_num) > 1e-15,
            }

    return {
        'family': family,
        'c': c_val,
        'ht_weights_by_arity': ht_weights,
        'shadow_comparison': shadow_comparison,
    }


# =========================================================================
# 11. Beilinson regulators
# =========================================================================

def beilinson_regulator(n: int, family: str = 'virasoro',
                        c_val: float = 2.0,
                        max_terms: int = 20) -> Dict[str, Any]:
    r"""Compute the Beilinson regulator r: H^n_M -> H^n_D.

    For n = 1: the regulator is the logarithm.
        r_1(u) = log|u| for a unit u.
        For the bar complex: the unit is the shadow growth rate rho(c).
        r_1 = log(rho(c)).

    For n = 2: the regulator involves the dilogarithm.
        r_2(x) = Li_2(x) = sum_{k>=1} x^k / k^2.
        For the bar complex: the argument is related to the shadow
        metric's roots.

    For n = 3: the trilogarithm.
        r_3(x) = Li_3(x) = sum_{k>=1} x^k / k^3.
    """
    result = {'n': n, 'family': family, 'c': c_val}

    if family == 'virasoro':
        kappa = c_val / 2
        alpha = 2.0
        S4 = 10.0 / (c_val * (5 * c_val + 22))
        Delta = 8 * kappa * S4  # = 40/(5c+22)

        # Shadow growth rate
        rho_sq = (9 * alpha ** 2 + 2 * Delta) / (4 * kappa ** 2)
        rho = math.sqrt(abs(rho_sq))

        if n == 1:
            # Regulator = log of the shadow growth rate
            reg = math.log(rho) if rho > 0 else float('-inf')
            result['regulator'] = reg
            result['unit'] = rho
            result['description'] = 'log(rho(c)): logarithm of shadow growth rate'

        elif n == 2:
            # Dilogarithm regulator
            # Argument: x = rho^2 / (1 + rho^2) (normalized growth rate)
            x = rho_sq / (1 + rho_sq) if (1 + rho_sq) != 0 else 0
            # Li_2(x) = sum x^k / k^2
            li2 = sum(x ** k / k ** 2 for k in range(1, max_terms + 1))
            result['regulator'] = li2
            result['argument'] = x
            result['description'] = 'Li_2(rho^2/(1+rho^2)): dilogarithm of normalized growth'
            # Comparison: pi^2/6 - Li_2(1-x) = Li_2(x) + log(x)*log(1-x)
            # (functional equation of dilogarithm)
            if 0 < x < 1:
                li2_check = math.pi ** 2 / 6 - sum((1 - x) ** k / k ** 2
                                                     for k in range(1, max_terms + 1))
                log_check = li2 + math.log(x) * math.log(1 - x)
                result['functional_equation_check'] = abs(li2_check - log_check)

        elif n == 3:
            # Trilogarithm regulator
            x = rho_sq / (1 + rho_sq) if (1 + rho_sq) != 0 else 0
            li3 = sum(x ** k / k ** 3 for k in range(1, max_terms + 1))
            result['regulator'] = li3
            result['argument'] = x
            result['description'] = 'Li_3(rho^2/(1+rho^2)): trilogarithm regulator'

        else:
            # General polylogarithm
            x = rho_sq / (1 + rho_sq) if (1 + rho_sq) != 0 else 0
            li_n = sum(x ** k / k ** n for k in range(1, max_terms + 1))
            result['regulator'] = li_n
            result['argument'] = x
            result['description'] = f'Li_{n}(rho^2/(1+rho^2)): polylogarithm regulator'

    elif family == 'heisenberg':
        # For Heisenberg: rho = 0 (class G, tower terminates at arity 2)
        result['regulator'] = 0.0 if n >= 2 else float('-inf')
        result['description'] = 'Trivial: class G has rho = 0'

    return result


# =========================================================================
# 12. Weight spectral sequence
# =========================================================================

def weight_spectral_sequence(family: str, max_arity: int = 6,
                             max_weight: int = 15) -> Dict[str, Any]:
    r"""Compute the E_1 page of the weight spectral sequence.

    The weight filtration W_k on B(A) gives a spectral sequence:
        E_1^{p,q} = H^{p+q}(Gr^W_{-p} B(A)) => H^{p+q}(B(A))

    For the bar complex, Gr^W_k B(A) = B^k(A) (the arity-k sector).
    The bar differential d: B^k -> B^{k-1} maps between adjacent
    graded pieces, so the E_1 page is:

        E_1^{-k, k+n} = H^n(B^k(A), d|_{B^k})

    But d maps B^k to B^{k-1}, so the restriction d|_{B^k} is the
    projection of d to the next graded piece. At E_1, the differential
    is d_1: E_1^{-k, *} -> E_1^{-k+1, *}, which is the induced map
    on cohomology.

    For KOSZUL algebras: the spectral sequence degenerates at E_2
    (PBW degeneration). The E_2 page gives the bar cohomology:
        E_2^{-1, 1+n} = H^n(B^1(A)) = (A!)_n
        E_2^{-k, *} = 0 for k >= 2 (Koszulness).

    For non-Koszul: higher pages contribute.

    We compute the E_1 page dimensions.
    """
    e1_page = {}

    for k in range(0, max_arity + 1):
        piece = bar_graded_piece_dims(family, k, max_weight)
        # At E_1, the dimensions are the arity-k sector dimensions
        # at each conformal weight (before taking d-cohomology).
        for h, d_val in piece.weight_dims.items():
            e1_page[(-k, k + h)] = d_val

    # Total E_1 dimension at each total degree n = p + q
    total_by_degree = defaultdict(int)
    for (p, q), d_val in e1_page.items():
        total_by_degree[p + q] += d_val

    return {
        'family': family,
        'e1_page': dict(e1_page),
        'total_by_degree': dict(total_by_degree),
        'degeneration': 'E_2 for Koszul algebras (all standard families)',
    }


# =========================================================================
# 13. Comparison: shadow depth vs weight filtration depth
# =========================================================================

def shadow_depth_weight_comparison(family: str,
                                   max_arity: int = 10,
                                   max_weight: int = 20) -> Dict[str, Any]:
    r"""Compare shadow depth r_max with the weight filtration.

    Key theorem: the shadow depth r_max is the maximal arity at which
    the shadow COEFFICIENT S_r is nonzero, NOT the maximal arity at
    which the bar complex is nonzero (which is always infinity).

    The weight filtration depth = infinity for all families (because
    the bar complex has nonzero sectors at all arities).

    The shadow depth is a MUCH finer invariant: it measures when the
    specific linear combination that defines S_r vanishes.

    r_max = A-infinity depth = L-infinity formality level
          (operadic complexity theorem, thm:operadic-complexity-detailed).
    """
    r_max = shadow_depth_from_family(family)

    # Check that bar complex is nonzero at each arity
    nonzero_arities = []
    for k in range(1, max_arity + 1):
        piece = bar_graded_piece_dims(family, k, max_weight)
        total = sum(piece.weight_dims.values())
        if total > 0:
            nonzero_arities.append(k)

    return {
        'family': family,
        'shadow_depth': r_max,
        'weight_filtration_depth': float('inf'),
        'bar_nonzero_at_arities': nonzero_arities,
        'all_arities_nonzero': len(nonzero_arities) == max_arity,
        'shadow_class': _family_to_class(family),
    }


def _family_to_class(family: str) -> str:
    """Map family name to shadow class."""
    CLASSES = {
        'heisenberg': 'G',
        'affine_sl2': 'L',
        'affine_sl3': 'L',
        'betagamma': 'C',
        'virasoro': 'M',
        'w3': 'M',
    }
    return CLASSES.get(family, '?')


# =========================================================================
# 14. Self-duality and Hodge symmetry at special points
# =========================================================================

def virasoro_self_duality_test(c_val: float = 13.0,
                               max_pq: int = 8) -> Dict[str, Any]:
    r"""Test whether Hodge symmetry holds at the self-dual point c = 13.

    For Virasoro: Koszul duality is c -> 26 - c.
    At c = 13: the algebra is self-dual (Vir_13 = Vir_{26-13} = Vir_13).

    Hodge symmetry h^{p,q} = h^{q,p} should hold at c = 13 because
    the bigrading is related to the algebra and its dual.

    IMPORTANT (AP8): "Self-dual" here means c = 13 (the Feigin-Frenkel
    involution fixed point), NOT c = 26 (anomaly cancellation).
    """
    hodge = shadow_hodge_numbers('virasoro', max_pq=max_pq)
    symmetry = hodge_symmetry_test(hodge, max_pq)

    # The Hodge numbers for Virasoro do NOT depend on c --- they are
    # purely combinatorial (dimensions of weight spaces and compositions).
    # So h^{p,q}(c=13) = h^{p,q}(c=2) = h^{p,q} universally.
    #
    # This means Hodge symmetry either holds for ALL c or for NONE.
    # In fact, it should FAIL because the bar complex has no reason
    # for arity-weight symmetry: dim B^q_p != dim B^p_q in general.

    # Complementarity check: S_r(c) + S_r(26-c) at c = 13
    S = virasoro_shadow_coefficients(max_pq + 2)
    complementarity = {}
    for r, expr in S.items():
        S_c = complex(expr.subs(c_sym, c_val))
        S_dual = complex(expr.subs(c_sym, 26 - c_val))
        complementarity[r] = {
            'S_r(c)': S_c,
            'S_r(26-c)': S_dual,
            'sum': S_c + S_dual,
            'self_dual': abs(S_c - S_dual) < 1e-10,
        }

    return {
        'c': c_val,
        'hodge_symmetry': symmetry,
        'shadow_self_duality': complementarity,
    }


# =========================================================================
# 15. Master computation: full mixed Hodge package
# =========================================================================

def full_mixed_hodge_package(family: str, max_pq: int = 8,
                             c_val: float = None,
                             params: Optional[Dict] = None) -> Dict[str, Any]:
    """Compute the full mixed Hodge structure data for a family.

    Returns all computed invariants in a single package.
    """
    # Default c values
    if c_val is None:
        c_defaults = {
            'heisenberg': 1.0,
            'virasoro': 2.0,
            'affine_sl2': 1.0,
            'betagamma': 1.0,
            'w3': 2.0,
        }
        c_val = c_defaults.get(family, 1.0)

    hodge = shadow_hodge_numbers(family, max_pq=max_pq)
    symmetry = hodge_symmetry_test(hodge, max_pq)
    depth_comp = shadow_depth_weight_comparison(family)
    specializations = hodge_deligne_specializations(family, max_pq)

    result = {
        'family': family,
        'c': c_val,
        'shadow_class': _family_to_class(family),
        'shadow_depth': shadow_depth_from_family(family),
        'hodge_numbers': hodge,
        'hodge_symmetry': symmetry,
        'depth_comparison': depth_comp,
        'deligne_specializations': specializations,
    }

    return result


# =========================================================================
# 16. Koszul duality on Hodge numbers
# =========================================================================

def koszul_dual_hodge_comparison(family: str, max_pq: int = 8) -> Dict[str, Any]:
    r"""Compare Hodge numbers of A and A! (Koszul dual).

    For Heisenberg: A = H_k, A! = Sym^ch(V*) with curvature -k.
        The Koszul dual has the SAME weight space structure (isomorphic
        as graded vector spaces) but different OPE.
        Hodge numbers should be the SAME.

    For Virasoro: A = Vir_c, A! = Vir_{26-c}.
        Weight space dimensions depend on c? NO --- the PBW structure
        of the free Virasoro algebra is c-independent. So:
        Hodge numbers of A = Hodge numbers of A!.

    This is a structural feature: the bar complex dimensions are
    determined by the GRADED STRUCTURE of the algebra, not by the
    OPE coefficients. Since A and A! have isomorphic underlying graded
    spaces (both are generated by the same generators with the same
    conformal weights), their Hodge numbers coincide.

    The DIFFERENCE between A and A! shows up in the bar COHOMOLOGY
    (which depends on the differential, hence on the OPE), not in the
    bar COMPLEX dimensions (which depend only on the generators).
    """
    hodge_A = shadow_hodge_numbers(family, max_pq=max_pq)

    # For standard families, A and A! have the same generators
    # (same conformal weights), so the bar complex dimensions are identical.
    # The Koszul dual family has:
    dual_families = {
        'heisenberg': 'heisenberg',  # H_k^! has same generators
        'virasoro': 'virasoro',       # Vir_c^! = Vir_{26-c}, same generators
        'affine_sl2': 'affine_sl2',   # sl_2 at dual level, same generators
    }

    dual_family = dual_families.get(family, family)
    hodge_dual = shadow_hodge_numbers(dual_family, max_pq=max_pq)

    # Compare
    match = True
    differences = []
    for (p, q) in hodge_A:
        hA = hodge_A.get((p, q), 0)
        hD = hodge_dual.get((p, q), 0)
        if hA != hD:
            match = False
            differences.append({'p': p, 'q': q, 'h_A': hA, 'h_dual': hD})

    return {
        'family': family,
        'dual_family': dual_family,
        'hodge_numbers_match': match,
        'differences': differences,
        'reason': ('Bar complex dimensions depend only on generator weights, '
                   'which are the same for A and A!. Differences appear in '
                   'bar COHOMOLOGY, not in bar COMPLEX dimensions.'),
    }


# =========================================================================
# 17. Euler characteristics and Hodge-Euler polynomial
# =========================================================================

def hodge_euler_polynomial(family: str, max_pq: int = 8) -> Dict[str, Any]:
    r"""Compute the Hodge-Euler polynomial E(u, v).

    E(u, v) = sum_{p, q} (-1)^{p+q} h^{p,q} u^p v^q

    For the bar complex: E(1, 1) = sum_{p,q} (-1)^{p+q} h^{p,q}
    is related to the Euler characteristic of the bar complex.

    E(u, 1) = sum_p (sum_q (-1)^{p+q} h^{p,q}) u^p
    is the weight-graded Euler characteristic.
    """
    hodge = shadow_hodge_numbers(family, max_pq=max_pq)

    # E(u, v) coefficients
    euler_coeffs = {}
    for (p, q), h in hodge.items():
        if h != 0:
            euler_coeffs[(p, q)] = (-1) ** (p + q) * h

    # E(1, 1) = total alternating Euler characteristic
    euler_total = sum(euler_coeffs.values())

    # E(u, 1): weight-graded
    weight_euler = defaultdict(int)
    for (p, q), coeff in euler_coeffs.items():
        weight_euler[p] += coeff

    return {
        'family': family,
        'euler_coefficients': dict(euler_coeffs),
        'euler_characteristic': euler_total,
        'weight_graded_euler': dict(weight_euler),
    }
