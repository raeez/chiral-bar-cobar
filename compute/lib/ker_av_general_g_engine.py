"""Kernel of the Reynolds averaging map for general simple Lie algebras.

Proposition prop:ker-av-schur-weyl (standalone/ordered_chiral_homology.tex):
for ANY finite-dimensional representation V of ANY simple Lie algebra g,

  dim ker(av_n | V^{tensor n}) = d^n - binom(n+d-1, d-1)

where d = dim(V).  The formula depends only on d, not on g or the
g-module structure of V.

The proof is elementary: the Reynolds projector av_n projects V^{tensor n}
onto Sym^n(V), whose dimension binom(n+d-1, d-1) depends only on d by
stars-and-bars.  For gl_r with V = C^r, Schur-Weyl duality refines this
to an isotypic decomposition; the kernel is the direct sum of all
non-trivial Sigma_n-isotypic components.

Algebras and their fundamental representation dimensions:
  sl_2:  d = 2  (fundamental C^2)
  sl_3:  d = 3  (fundamental C^3)
  so_5:  d = 5  (vector representation C^5; isomorphic to sp_4)
  G_2:   d = 7  (fundamental, the smallest irreducible)
  sl_N:  d = N  (fundamental C^N)
"""
from __future__ import annotations

from math import comb
from fractions import Fraction
from typing import Dict, List, Tuple


# -- Fundamental representation dimensions --------------------------------
# Each entry: (algebra_name, dim_fund_rep)
# VERIFIED: [DC] direct computation from root system; [LT] Humphreys,
# Introduction to Lie Algebras and Representation Theory.

FUND_REP_DIMS: Dict[str, int] = {
    # sl_N: fundamental = C^N, dim = N
    # VERIFIED: [DC] standard representation; [LT] Humphreys Ch. 1
    "sl_2": 2,
    "sl_3": 3,
    "sl_4": 4,
    "sl_5": 5,
    "sl_6": 6,
    # so_N: vector representation = C^N, dim = N
    # VERIFIED: [DC] defining representation; [LT] Humphreys Ch. 1
    "so_5": 5,   # isomorphic to sp_4 (B_2 = C_2)
    "so_7": 7,
    "so_8": 8,   # triality: three 8-dim fundamentals
    # sp_{2n}: fundamental = C^{2n}, dim = 2n
    # VERIFIED: [DC] symplectic standard; [LT] Humphreys
    "sp_4": 4,   # isomorphic to so_5 as Lie algebra (C_2 = B_2)
    "sp_6": 6,
    # exceptional
    # VERIFIED: [DC] from root system; [LT] Bourbaki Lie IV-VI
    "G_2": 7,    # smallest irreducible of G_2
    "F_4": 26,   # smallest irreducible of F_4
    "E_6": 27,   # smallest irreducible of E_6
    "E_7": 56,   # smallest irreducible of E_7
    "E_8": 248,  # adjoint = smallest = fundamental for E_8
}


# -- Core formula ---------------------------------------------------------

def ker_av_dim(d: int, n: int) -> int:
    """Dimension of ker(av_n) on V^{tensor n} for dim(V) = d.

    ker(av_n) = d^n - binom(n+d-1, d-1).

    VERIFIED: [DC] Reynolds projector image = Sym^n(V), dim = binom(n+d-1, d-1)
    by stars-and-bars; [SY] formula is symmetric-group-theoretic, independent
    of Lie algebra structure.
    """
    if d < 1 or n < 1:
        raise ValueError(f"d and n must be positive, got d={d}, n={n}")
    return d ** n - comb(n + d - 1, d - 1)


def sym_dim(d: int, n: int) -> int:
    """Dimension of Sym^n(V) for dim(V) = d.

    binom(n+d-1, d-1) = binom(n+d-1, n).

    VERIFIED: [DC] stars-and-bars (degree-n monomials in d variables).
    """
    if d < 1 or n < 0:
        raise ValueError(f"d must be positive and n non-negative, got d={d}, n={n}")
    return comb(n + d - 1, d - 1)


def total_dim(d: int, n: int) -> int:
    """Dimension of V^{tensor n} = d^n."""
    return d ** n


def info_ratio(d: int, n: int) -> Fraction:
    """Fraction of V^{tensor n} in the kernel of av_n.

    info_ratio = ker_av_dim / total_dim.
    Measures how much ordered data is lost under averaging.
    """
    t = total_dim(d, n)
    return Fraction(ker_av_dim(d, n), t)


# -- Algebra-specific interface -------------------------------------------

def ker_av_for_algebra(algebra: str, n: int) -> Dict:
    """Compute ker(av_n) data for a named Lie algebra at degree n.

    Returns dict with: algebra, d, n, total, sym, kernel, ratio.
    """
    if algebra not in FUND_REP_DIMS:
        raise KeyError(
            f"Unknown algebra {algebra!r}; known: {sorted(FUND_REP_DIMS)}"
        )
    d = FUND_REP_DIMS[algebra]
    t = total_dim(d, n)
    s = sym_dim(d, n)
    k = ker_av_dim(d, n)
    return {
        "algebra": algebra,
        "d": d,
        "n": n,
        "total": t,
        "sym": s,
        "kernel": k,
        "ratio": Fraction(k, t),
    }


def table_for_algebra(algebra: str, degrees: List[int]) -> List[Dict]:
    """Table of ker(av_n) data across multiple degrees."""
    return [ker_av_for_algebra(algebra, n) for n in degrees]


# -- Cross-algebra comparison at fixed d ----------------------------------

def algebras_with_same_d(d: int) -> List[str]:
    """All algebras in the registry whose fundamental has dimension d.

    Demonstrates that the formula gives identical results for different
    Lie algebras with the same d.
    """
    return [alg for alg, dim in FUND_REP_DIMS.items() if dim == d]


# -- Degree-2 special case: kernel = Alt^2(V) ----------------------------

def ker_av_2_equals_alt2(d: int) -> Tuple[int, int, bool]:
    """Verify that ker(av_2) = dim(Alt^2(V)) = d(d-1)/2.

    At n=2, Sym^2(V) has dimension d(d+1)/2, so
    ker(av_2) = d^2 - d(d+1)/2 = d(d-1)/2 = dim(Alt^2(V)).

    Returns (ker_dim, alt2_dim, match).
    """
    k = ker_av_dim(d, 2)
    alt2 = d * (d - 1) // 2
    return (k, alt2, k == alt2)


# -- Generating function --------------------------------------------------

def generating_function_coeffs(d: int, max_n: int) -> List[int]:
    """Coefficients of the generating function Delta P_d(t).

    Delta P_d(t) = sum_{n >= 0} ker_av_dim(d, n) * t^n
                 = 1/(1 - d*t) - 1/(1-t)^d.

    The first non-trivial coefficient is at n=2.
    Returns [ker(d,0), ker(d,1), ..., ker(d,max_n)].
    ker(d,0) = 0 (1 - 1), ker(d,1) = 0 (d - d).
    """
    return [ker_av_dim(d, n) if n >= 1 else 0 for n in range(max_n + 1)]


# -- Pretty printing ------------------------------------------------------

def print_table(algebras: List[str], degrees: List[int]) -> None:
    """Print a formatted comparison table."""
    header = f"{'Algebra':>10} {'d':>3} |"
    for n in degrees:
        header += f" {'n='+str(n):>10}"
    print(header)
    print("-" * len(header))
    for alg in algebras:
        d = FUND_REP_DIMS[alg]
        row = f"{alg:>10} {d:>3} |"
        for n in degrees:
            k = ker_av_dim(d, n)
            row += f" {k:>10}"
        print(row)


if __name__ == "__main__":
    print("=== Kernel of Reynolds averaging map: general g ===\n")
    algebras = ["sl_2", "sl_3", "sl_4", "sl_5", "so_5", "G_2"]
    degrees = list(range(2, 7))
    print_table(algebras, degrees)

    print("\n=== Algebras with d=5 (should give identical values) ===")
    same_5 = algebras_with_same_d(5)
    print(f"  Algebras with d=5: {same_5}")
    for alg in same_5:
        print(f"  {alg}: ker(av_3) = {ker_av_for_algebra(alg, 3)['kernel']}")

    print("\n=== Degree-2 = Alt^2(V) check ===")
    for d in [2, 3, 5, 7]:
        k, a, ok = ker_av_2_equals_alt2(d)
        print(f"  d={d}: ker(av_2)={k}, dim(Alt^2)={a}, match={ok}")
