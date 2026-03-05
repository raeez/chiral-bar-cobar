"""Bar complex of a chiral algebra as an explicit chain complex.

For a chiral algebra A with OPE data, the bar complex is:
  B-bar(A) = (T^c(s^{-1}A-bar), d_bar)

where A-bar = A / C*vacuum (remove vacuum), and d_bar is determined by:
  - Simple pole residues -> Lie bracket component
  - Double pole residues -> curvature m_0

Bar degree n: B-bar^n = (s^{-1}A-bar)^{tensor n} / Arnold relations.

Arnold relations on FM_{n+1}(P^1):
  eta_{ij} wedge eta_{jk} + eta_{jk} wedge eta_{ki} + eta_{ki} wedge eta_{ij} = 0
reduce the dimension.  On C_n(P^1), dim H^{n-1}(C_n, C) = (n-1)! for the
top-degree cohomology relevant to bar degree n-1.

GRADING: Cohomological, |d| = +1.  Bar differential has bar-degree -1
(it maps B-bar^n -> B-bar^{n-1}).  In the internal (conformal weight) grading,
d has degree +1.

This module computes bar complexes for algebras specified by:
1. A list of generators with their conformal weights
2. An OPE table: for each pair (a, b), the singular terms
   a(z)b(w) ~ sum_k c_{ab}^k / (z-w)^k
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, zeros, eye, Symbol

from .utils import GradedVectorSpace, ChainComplex, partition_number


# ---------------------------------------------------------------------------
# OPE Algebra
# ---------------------------------------------------------------------------

@dataclass
class Generator:
    """A generator of a chiral algebra."""
    name: str
    weight: int  # conformal weight
    index: int   # position in the basis


@dataclass
class OPEAlgebra:
    """A chiral algebra specified by generators and OPE coefficients.

    ope_table[(a, b)] = {pole_order: {output_name: coefficient}}

    Example for sl_2 at level k:
      ope_table[("e", "f")] = {
          2: {"1": k},           # double pole: k * 1/(z-w)^2
          1: {"h": Rational(1)}, # simple pole: h(w)/(z-w)
      }
      ope_table[("h", "h")] = {
          2: {"1": 2*k},         # double pole: 2k/(z-w)^2
      }
      ope_table[("h", "e")] = {
          1: {"e": Rational(2)}, # simple pole: 2*e(w)/(z-w)
      }
    """
    generators: List[Generator]
    ope_table: Dict[Tuple[str, str], Dict[int, Dict[str, Rational]]]
    name: str = ""
    level: Optional[Symbol] = None  # symbolic level parameter

    @property
    def gen_names(self) -> List[str]:
        return [g.name for g in self.generators]

    @property
    def dim(self) -> int:
        return len(self.generators)

    def simple_pole(self, a: str, b: str) -> Dict[str, Rational]:
        """Extract simple pole coefficient: a(z)b(w) ~ ... + c/(z-w)."""
        entry = self.ope_table.get((a, b), {})
        return entry.get(1, {})

    def double_pole(self, a: str, b: str) -> Dict[str, Rational]:
        """Extract double pole coefficient: a(z)b(w) ~ ... + c/(z-w)^2."""
        entry = self.ope_table.get((a, b), {})
        return entry.get(2, {})


# ---------------------------------------------------------------------------
# Standard algebras
# ---------------------------------------------------------------------------

def heisenberg_algebra(kappa=None) -> OPEAlgebra:
    """Heisenberg algebra H_kappa with one generator J of weight 1.

    OPE: J(z)J(w) ~ kappa/(z-w)^2.  No simple pole.
    """
    if kappa is None:
        kappa = Symbol("kappa")

    return OPEAlgebra(
        generators=[Generator("J", weight=1, index=0)],
        ope_table={
            ("J", "J"): {2: {"1": kappa}},  # double pole only
        },
        name=f"H_{kappa}",
        level=kappa,
    )


def sl2_algebra(k=None) -> OPEAlgebra:
    """Affine sl_2 at level k.

    Generators: e, h, f (weights all 1 for the current generators).
    OPE:
      e(z)f(w) ~ k/(z-w)^2 + h(w)/(z-w)
      h(z)h(w) ~ 2k/(z-w)^2
      h(z)e(w) ~ 2*e(w)/(z-w)
      h(z)f(w) ~ -2*f(w)/(z-w)
      (and antisymmetric: f(z)e(w) ~ k/(z-w)^2 - h(w)/(z-w), etc.)
    """
    if k is None:
        k = Symbol("k")

    return OPEAlgebra(
        generators=[
            Generator("e", weight=1, index=0),
            Generator("h", weight=1, index=1),
            Generator("f", weight=1, index=2),
        ],
        ope_table={
            ("e", "f"): {2: {"1": k}, 1: {"h": Rational(1)}},
            ("f", "e"): {2: {"1": k}, 1: {"h": Rational(-1)}},
            ("h", "h"): {2: {"1": 2 * k}},
            ("h", "e"): {1: {"e": Rational(2)}},
            ("e", "h"): {1: {"e": Rational(-2)}},
            ("h", "f"): {1: {"f": Rational(-2)}},
            ("f", "h"): {1: {"f": Rational(2)}},
        },
        name=f"sl2_{k}",
        level=k,
    )


def virasoro_algebra(c=None) -> OPEAlgebra:
    """Virasoro algebra Vir_c with one generator T of weight 2.

    OPE: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + dT(w)/(z-w)

    For bar complex purposes, the (z-w)^4 term is higher-order and
    only the poles of order <= 2 enter the bar differential directly.
    The (z-w)^2 term gives curvature, the (z-w)^1 term gives bracket.
    """
    if c is None:
        c = Symbol("c")

    return OPEAlgebra(
        generators=[Generator("T", weight=2, index=0)],
        ope_table={
            ("T", "T"): {
                2: {"T": Rational(2)},      # 2T(w)/(z-w)^2
                1: {"dT": Rational(1)},     # dT(w)/(z-w)  (derivative)
            },
        },
        name=f"Vir_{c}",
        level=c,
    )


def free_fermion_algebra() -> OPEAlgebra:
    """Free fermion (bc ghost system) with generators b (weight 2), c (weight -1).

    Actually for the free fermion algebra with one generator psi of weight 1/2,
    OPE: psi(z)psi(w) ~ 1/(z-w).

    But for Koszul duality purposes, we use the standard presentation.
    The free fermion F has: F^! = beta-gamma (VF014).
    """
    return OPEAlgebra(
        generators=[Generator("psi", weight=1, index=0)],
        ope_table={
            ("psi", "psi"): {1: {"1": Rational(1)}},  # simple pole only
        },
        name="F",
    )


# ---------------------------------------------------------------------------
# Bar complex computation
# ---------------------------------------------------------------------------

def arnold_dimension(n: int) -> int:
    """Dimension of the bar-relevant part of OS algebra at n points.

    For n generators in bar degree n-1, the relevant space is
    H^{n-1}(C_n(C), C) which has dimension (n-1)!.

    But for bar degree d with d+1 points on P^1, we need:
    dim H^0(FM_{d+1}(P^1), Omega^d_log) which by Arnold = d!

    Actually, the correct count for the bar complex on P^1:
    At bar degree d, we have d+1 points, and the log forms give
    dim = d! (from the OS algebra).

    For the BAR complex specifically (not the full tensor power):
    dim B-bar^d = dim(A-bar)^d * d! / d! = ... no, that's wrong.

    Let me be more careful. The bar complex is:
    B-bar^d = (s^{-1}A-bar)^{otimes d} tensored with the
    d-th component of the bar cooperad.

    For the associative bar complex (no Arnold): dim = dim(A-bar)^d.
    For the commutative bar complex: reduced, so dim is smaller.
    For the chiral bar complex on P^1: Arnold relations reduce it.

    The key formula: for generators of a LIE-type algebra (like KM),
    the bar degree d component has basis indexed by
    {(a_1, ..., a_d) : generators} with the relations from Arnold.

    For the LIE operad bar (Chevalley-Eilenberg complex):
    dim = C(n, d) where n = dim(g) ... this is Lambda^d(g).

    For the COM operad bar (Harrison complex):
    dim = partition-related.

    For the CHIRAL bar on P^1:
    This is more subtle because the chiral operad combines
    Lie and Com aspects.

    SAFE APPROACH: Compute case-by-case using known values,
    then verify against the Master Table.
    """
    # (n-1)! for OS algebra top degree
    from math import factorial
    if n < 1:
        return 0
    return factorial(n - 1)


def bar_dim_heisenberg(degree: int) -> int:
    """Bar complex dimension for Heisenberg (rank 1) at given bar degree.

    PROVED (rem:bar-dims-partitions, free_fields.tex):
      dim B-bar^1(H) = 1
      dim B-bar^n(H) = p(n-2) for n >= 2
    giving 1, 1, 1, 2, 3, 5, 7, 11, ...
    """
    if degree < 1:
        return 0
    if degree == 1:
        return 1
    return partition_number(degree - 2)


def bar_dim_free_fermion(degree: int) -> int:
    """Bar complex dimension for free fermion at given bar degree.

    From manuscript Table: 1, 1, 2, 3, 5 = p(0), p(1), p(2), p(3), p(4).
    So dim B-bar^d(F) = p(d-1) where p is the partition function.
    """
    if degree < 1:
        return 0
    return partition_number(degree - 1)


def bar_dim_sl2(degree: int) -> Optional[int]:
    """Bar COHOMOLOGY dimension for sl2-hat at given bar degree.

    dim H^n(B-bar(sl2)) = R(n+3) where R = Riordan numbers (OEIS A005043).
    Recurrence: R(n) = ((n-1)*(2*R(n-1) + 3*R(n-2))) / (n+1), R(0)=1, R(1)=0.
    Values: 3, 6, 15, 36, 91, 232, 603, 1585, ...
    Chain group dim = 3^n * (n-1)! (much larger).
    """
    if degree < 1:
        return None
    n = degree + 4  # need R(degree+3), so compute up to index degree+3
    R = [0] * n
    R[0] = 1
    R[1] = 0
    for i in range(2, n):
        R[i] = ((i - 1) * (2 * R[i-1] + 3 * R[i-2])) // (i + 1)
    return R[degree + 3]


def bar_dim_virasoro(degree: int) -> Optional[int]:
    """Bar COHOMOLOGY dimension for Virasoro at given bar degree.

    dim H^n(B-bar(Vir_c)) = M(n+1) - M(n) where M = Motzkin numbers.
    This is OEIS A002026 (first differences of Motzkin numbers).
    Values: 1, 2, 5, 12, 30, 76, 196, 512, 1353, ...
    """
    # First differences of Motzkin numbers
    # Compute enough Motzkin numbers
    if degree < 1:
        return None
    n = degree + 2  # need M(degree+1) and M(degree)
    M = [0] * n
    M[0] = 1
    if n > 1:
        M[1] = 1
    for i in range(2, n):
        M[i] = M[i-1] + sum(M[k] * M[i-2-k] for k in range(i-1))
    return M[degree + 1] - M[degree]


def bar_dim_w3(degree: int) -> Optional[int]:
    """Bar complex dimension for W_3 at given bar degree.

    From manuscript Table: 2, 5, 16, 52.
    Growth is exponential.
    """
    known = {1: 2, 2: 5, 3: 16, 4: 52}
    return known.get(degree)


def bar_dim_sl3(degree: int) -> Optional[int]:
    """Bar COHOMOLOGY dimension for sl3-hat at given bar degree.

    From the Master Table (examples_summary.tex): 8, 36, 204.
    These are dim H^n(B-bar), NOT chain group dims.
    Chain group dim = dim(g)^n * (n-1)! = 8^n * (n-1)! (proved).
    """
    known = {1: 8, 2: 36, 3: 204}
    return known.get(degree)


# ---------------------------------------------------------------------------
# KM bar complex: Chevalley-Eilenberg interpretation
# ---------------------------------------------------------------------------

def km_chain_space_dim(dim_g: int, degree: int) -> int:
    """Total dimension of the bar chain space B-bar^d for a KM algebra.

    B-bar^d = g^{tensor d} tensor Omega^{d-1}(Conf_d)
    dim = dim(g)^d * (d-1)!

    This is the CHAIN SPACE dimension, not cohomology.
    The Master Table reports BAR COHOMOLOGY dims (much smaller):
      sl2 chain: 3, 9, 54, 486       cohomology: 3, 6, 15, 36, 91
      sl3 chain: 8, 64, 1024, 24576  cohomology: 8, 36, 204
    """
    from math import factorial
    if degree < 1:
        return 0
    return dim_g ** degree * factorial(degree - 1)


# ---------------------------------------------------------------------------
# Registry of known bar COHOMOLOGY dimensions (from Master Table)
# ---------------------------------------------------------------------------
# NOTE: The Master Table (examples_summary.tex, Table 2) reports
# BAR COHOMOLOGY dim H^n(B-bar(A)), NOT chain group dimensions.
# For KM algebras, chain group dim B-bar^n = dim(g)^n * (n-1)!
# (proved in rem:bar-dims-level-independent), which is much larger.

KNOWN_BAR_DIMS = {
    # === PROVED by formula (rem:bar-dims-partitions, free_fields.tex) ===
    "Heisenberg": {1: 1, 2: 1, 3: 1, 4: 2, 5: 3, 6: 5, 7: 7, 8: 11},
    "free_fermion": {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 7, 7: 11, 8: 15},
    # === From summary table ===
    "bc": {1: 2, 2: 3, 3: 6, 4: 13, 5: 28, 6: 59, 7: 122, 8: 249},  # 2^n - n + 1
    "beta_gamma": {1: 2, 2: 4, 3: 10, 4: 26, 5: 70, 6: 192, 7: 534, 8: 1500},  # [x^n]sqrt((1+x)/(1-3x))
    # === KM BAR COHOMOLOGY dims (from summary table) ===
    "sl2": {1: 3, 2: 6, 3: 15, 4: 36, 5: 91, 6: 232, 7: 603},
    "sl3": {1: 8, 2: 36, 3: 204},
    # === Non-KM: from summary table ===
    "Virasoro": {1: 1, 2: 2, 3: 5, 4: 12, 5: 30, 6: 76, 7: 196, 8: 512},
    "W3": {1: 2, 2: 5, 3: 16, 4: 52},
    "Yangian_sl2": {1: 4, 2: 10, 3: 28},
}

# KM chain group dimensions (PROVED, rem:bar-dims-level-independent):
# dim B-bar^n = dim(g)^n * (n-1)!
# These are much larger than the cohomology dims above.
KNOWN_CHAIN_GROUP_DIMS = {
    "sl2": {1: 3, 2: 9, 3: 54, 4: 486, 5: 5832},
    "sl3": {1: 8, 2: 64, 3: 1024, 4: 24576},
    "G2": {1: 14, 2: 196, 3: 5488},
    "B2": {1: 10, 2: 100, 3: 2000},
}


def verify_bar_dim(algebra: str, degree: int, computed: int) -> Tuple[bool, str]:
    """Verify a computed bar dimension against ground truth.

    Returns (matches, message).
    """
    known = KNOWN_BAR_DIMS.get(algebra, {})
    expected = known.get(degree)
    if expected is None:
        return True, f"No ground truth for {algebra} bar dim at degree {degree}"
    if computed == expected:
        return True, f"VERIFIED: dim B-bar^{degree}({algebra}) = {computed} matches Master Table"
    return False, (
        f"MISMATCH: computed dim B-bar^{degree}({algebra}) = {computed}, "
        f"but Master Table says {expected}"
    )
