"""Averaging kernel dimension and information ratio engine.

Extends averaging_kernel_engine with:
  - sl_4 (d=15) and additional Lie algebras (so_5, g_2, e_8)
  - Cross-algebra comparison tables at fixed arities
  - Information ratio analysis: how much of the ordered bar complex
    is lost under the Sigma_n-coinvariant projection av: B^ord -> B^Sigma
  - Sym/Alt decomposition dimensions for the R-matrix enhanced picture

The averaging map av: g^{E_1} -> g^{mod} projects ordered (E_1) bar
configurations to their symmetric (modular/E_inf) coinvariants.
At arity n on a d-dimensional desuspended generator space V:

  total space     : V^{otimes n},  dim = d^n
  coinvariant dim : Sym^n(V) = binom(d+n-1, n)   [even desuspension]
                    Alt^n(V) = binom(d, n)         [odd desuspension]
  kernel dim      : d^n - coinvariant dim
  information ratio : kernel_dim / d^n
                      (fraction LOST, not fraction surviving)

For the classical r-matrix r(z) = k * Omega / z (AP126: level prefix
mandatory; k=0 -> r=0), the R-matrix provides a Yang-Baxter splitting
of the tensor power into symmetric and alternating components.

The information ratio quantifies the E_1/E_inf gap: how much structure
the ordered bar complex carries beyond its symmetric shadow.

Lie algebra dimensions (adjoint representation):
  sl_N : N^2 - 1
  so_N : N(N-1)/2
  g_2  : 14
  e_8  : 248
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Dict, List, Optional, Tuple


# -- Lie algebra dimension registry ------------------------------------

LIE_ALGEBRA_DIMS: Dict[str, int] = {
    # VERIFIED: [DC] sl_N has dim = N^2 - 1; [LT] Humphreys, Intro to Lie Algebras
    "sl_2": 3,    # 2^2 - 1 = 3
    "sl_3": 8,    # 3^2 - 1 = 8
    "sl_4": 15,   # 4^2 - 1 = 15
    "sl_5": 24,   # 5^2 - 1 = 24
    # VERIFIED: [DC] so_N has dim = N(N-1)/2; [LT] Humphreys
    "so_5": 10,   # 5*4/2 = 10; isomorphic to sp_4
    "so_8": 28,   # 8*7/2 = 28; triality
    # VERIFIED: [DC] exceptional dims from root system; [LT] Bourbaki Lie IV-VI
    "g_2": 14,
    "f_4": 52,
    "e_6": 78,
    "e_7": 133,
    "e_8": 248,   # VERIFIED: [DC] omega_1 = adjoint = 248; [CF] compute/lib/bc_exceptional_categorical_zeta_engine.py
}

# Default parity: all standard chiral algebras from Lie algebras have
# even desuspended degree (the adjoint generators are even).
DEFAULT_PARITY = "even"


# -- Core dimension computations ---------------------------------------

def coinvariant_dim(d: int, n: int, parity: str = "even") -> int:
    """Dimension of the Sigma_n-coinvariant subspace of V^{otimes n}.

    Even parity (symmetric tensors): binom(d + n - 1, n).
    Odd parity (alternating tensors): binom(d, n).

    VERIFIED: [DC] stars-and-bars for Sym; exterior basis count for Alt.
    [SY] Sigma_n-coinvariants on even generators = Sym^n(V).
    """
    if parity == "even":
        return comb(d + n - 1, n)
    elif parity == "odd":
        return comb(d, n)
    else:
        raise ValueError(f"parity must be 'even' or 'odd', got {parity!r}")


def total_dim(d: int, n: int) -> int:
    """Dimension of V^{otimes n} = d^n."""
    return d ** n


def kernel_dim(d: int, n: int, parity: str = "even") -> int:
    """Dimension of ker(av) at arity n.

    kernel = total - coinvariant.
    """
    return total_dim(d, n) - coinvariant_dim(d, n, parity)


def info_ratio(d: int, n: int, parity: str = "even") -> Fraction:
    """Information ratio: fraction of tensor power LOST under averaging.

    info_ratio = kernel_dim / total_dim = 1 - coinvariant_dim / total_dim.

    A ratio of 0 means no information is lost (d=1 or n=1).
    A ratio approaching 1 means almost everything is lost (large n, d >= 2).
    """
    t = total_dim(d, n)
    if t == 0:
        raise ValueError("d and n must be positive")
    return Fraction(kernel_dim(d, n, parity), t)


def surviving_ratio(d: int, n: int, parity: str = "even") -> Fraction:
    """Fraction of the tensor power SURVIVING the averaging map.

    surviving_ratio = 1 - info_ratio = coinvariant_dim / total_dim.
    """
    t = total_dim(d, n)
    if t == 0:
        raise ValueError("d and n must be positive")
    return Fraction(coinvariant_dim(d, n, parity), t)


# -- Sym/Alt decomposition for R-matrix analysis ----------------------

def sym_dim(d: int, n: int) -> int:
    """Dimension of Sym^n(V) for a d-dimensional space V.

    binom(d + n - 1, n).
    """
    return comb(d + n - 1, n)


def alt_dim(d: int, n: int) -> int:
    """Dimension of Alt^n(V) = binom(d, n). Zero for n > d."""
    return comb(d, n)


def sym_alt_ratio(d: int, n: int) -> Fraction:
    """Ratio Sym^n(V) / Alt^n(V).

    Undefined (returns None-like behavior) when Alt^n = 0 (n > d).
    For the R-matrix picture, the symmetric-to-alternating ratio
    measures the asymmetry of the Yang-Baxter decomposition.
    """
    a = alt_dim(d, n)
    if a == 0:
        raise ValueError(f"Alt^{n}(V) = 0 for d={d}, n={n} > d; ratio undefined")
    return Fraction(sym_dim(d, n), a)


def sym_alt_decomposition(d: int, n: int) -> Dict:
    """Full Sym/Alt decomposition data at arity n.

    Returns dict with keys:
      d, n, total_dim, sym_dim, alt_dim, mixed_dim,
      sym_fraction, alt_fraction, mixed_fraction,
      sym_alt_ratio (None if alt_dim = 0).

    The 'mixed' component is whatever is neither fully symmetric
    nor fully alternating in the Sigma_n-isotypic decomposition:
      mixed_dim = d^n - sym_dim - alt_dim  (for n >= 2).
    """
    t = d ** n
    s = sym_dim(d, n)
    a = alt_dim(d, n)
    m = t - s - a if n >= 2 else 0  # at n=1, Sym^1 = V = total

    result: Dict = {
        "d": d,
        "n": n,
        "total_dim": t,
        "sym_dim": s,
        "alt_dim": a,
        "mixed_dim": m,
        "sym_fraction": Fraction(s, t) if t > 0 else Fraction(0),
        "alt_fraction": Fraction(a, t) if t > 0 else Fraction(0),
        "mixed_fraction": Fraction(m, t) if t > 0 else Fraction(0),
    }

    if a > 0:
        result["sym_alt_ratio"] = Fraction(s, a)
    else:
        result["sym_alt_ratio"] = None

    return result


# -- Cross-algebra comparison ------------------------------------------

def averaging_kernel_datum(
    lie_algebra: str,
    arity: int,
    parity: str = "even",
) -> Dict:
    """Full averaging kernel data for a given Lie algebra and arity.

    Returns dict with keys:
      lie_algebra, dim_g, arity, total_dim, coinvariant_dim,
      kernel_dim, info_ratio, surviving_ratio, parity.
    """
    if lie_algebra not in LIE_ALGEBRA_DIMS:
        raise KeyError(
            f"Unknown Lie algebra {lie_algebra!r}; "
            f"known: {sorted(LIE_ALGEBRA_DIMS)}"
        )
    d = LIE_ALGEBRA_DIMS[lie_algebra]
    return {
        "lie_algebra": lie_algebra,
        "dim_g": d,
        "arity": arity,
        "total_dim": total_dim(d, arity),
        "coinvariant_dim": coinvariant_dim(d, arity, parity),
        "kernel_dim": kernel_dim(d, arity, parity),
        "info_ratio": info_ratio(d, arity, parity),
        "surviving_ratio": surviving_ratio(d, arity, parity),
        "parity": parity,
    }


def cross_algebra_table(
    algebras: Optional[List[str]] = None,
    arities: Optional[List[int]] = None,
    parity: str = "even",
) -> List[Dict]:
    """Cross-algebra comparison table.

    Default algebras: sl_2, sl_3, sl_4.
    Default arities: 2, 3, 4, 5.
    """
    if algebras is None:
        algebras = ["sl_2", "sl_3", "sl_4"]
    if arities is None:
        arities = [2, 3, 4, 5]
    rows = []
    for alg in algebras:
        for n in arities:
            rows.append(averaging_kernel_datum(alg, n, parity))
    return rows


def info_ratio_growth_table(
    lie_algebra: str,
    max_arity: int = 10,
    parity: str = "even",
) -> List[Dict]:
    """Information ratio as a function of arity for a single algebra.

    Shows how rapidly the E_1/E_inf gap grows with arity.
    """
    d = LIE_ALGEBRA_DIMS[lie_algebra]
    rows = []
    for n in range(1, max_arity + 1):
        ir = info_ratio(d, n, parity)
        rows.append({
            "lie_algebra": lie_algebra,
            "dim_g": d,
            "arity": n,
            "info_ratio": ir,
            "info_ratio_float": float(ir),
        })
    return rows


# -- Hecke algebra / Schur-Weyl decomposition for fundamental rep ------
#
# For V = C^d (fundamental representation of sl_d), the Schur-Weyl
# decomposition of V^{tensor n} under S_n x GL_d is:
#
#   V^{tensor n} = bigoplus_{lambda |- n, l(lambda) <= d} S_lambda tensor V_lambda
#
# where S_lambda is the Specht module (S_n irrep of shape lambda) and
# V_lambda is the GL_d irrep of highest weight lambda.
#
# At generic q (non-root of unity), the Hecke algebra H_n(q) is
# semisimple and the R-twisted coinvariants are computed by:
#   coinvariant = trivial S_n-isotypic component = single-row lambda = (n)
#   coinvariant space = V_{(n)} = Sym^n(V), dim = binom(d+n-1, n)
#   ker(av_n) = everything else = sum over non-trivial lambda
#
# For V = C^2 (fundamental of sl_2):
#   Partitions with at most 2 parts: lambda = (n-j, j), j = 0, ..., floor(n/2)
#   dim(V_{(n-j,j)}) = n - 2j + 1  (the spin-(n-2j)/2 irrep of SL_2)
#   dim(S_{(n-j,j)}) = binom(n, j) - binom(n, j-1)  for j >= 1, and 1 for j=0
#   coinvariant = lambda = (n, 0): dim(Sym^n(C^2)) = n + 1
#   ker(av_n) = 2^n - (n + 1)


def specht_dim_two_row(n: int, j: int) -> int:
    """Dimension of the Specht module S_{(n-j, j)} for S_n.

    For two-row partitions lambda = (n-j, j) with j >= 0:
      j = 0: dim = 1 (trivial representation)
      j >= 1: dim = binom(n, j) - binom(n, j-1) (ballot numbers)

    VERIFIED: [DC] hook-length formula for two-row partitions;
    [LT] Fulton-Harris Representation Theory, Ch. 4;
    [CF] agrees with Catalan numbers at j = floor(n/2) when n = 2j.
    """
    if j < 0 or j > n // 2:
        return 0
    if j == 0:
        return 1
    return comb(n, j) - comb(n, j - 1)


def gl2_irrep_dim(n: int, j: int) -> int:
    """Dimension of the GL_2 irrep V_{(n-j, j)}.

    For lambda = (n-j, j): this is the SL_2 irrep of spin (n-2j)/2,
    dimension n - 2j + 1.

    VERIFIED: [DC] Weyl dimension formula for GL_2;
    [LC] j=0 gives n+1 = dim Sym^n(C^2).
    """
    if j < 0 or j > n // 2:
        return 0
    return n - 2 * j + 1


def schur_weyl_decomposition_sl2(n: int) -> List[Dict]:
    """Full Schur-Weyl decomposition of (C^2)^{tensor n} under S_n x GL_2.

    Returns a list of dicts, one per partition lambda = (n-j, j):
      j, partition, specht_dim, gl2_dim, product, is_trivial

    VERIFIED: [DC] sum of products = 2^n (total dimension);
    [SY] Schur-Weyl duality is exact at characteristic 0.
    """
    rows = []
    total_check = 0
    for j in range(n // 2 + 1):
        sd = specht_dim_two_row(n, j)
        gd = gl2_irrep_dim(n, j)
        prod = sd * gd
        total_check += prod
        rows.append({
            "j": j,
            "partition": (n - j, j),
            "specht_dim": sd,
            "gl2_dim": gd,
            "product": prod,
            "is_trivial": (j == 0),
        })
    assert total_check == 2 ** n, (
        f"Schur-Weyl total {total_check} != 2^{n} = {2**n}"
    )
    return rows


def hecke_kernel_dim_sl2_fund(n: int) -> int:
    """Dimension of ker(av_n) for V = C^2 (fundamental of sl_2)
    under the Hecke algebra H_n(q) at generic q.

    ker(av_n) = 2^n - dim(Sym^n(C^2)) = 2^n - (n + 1).

    VERIFIED: [DC] Schur-Weyl decomposition, trivial isotypic = Sym^n;
    [DC] explicit Reynolds operator computation at n = 1..6;
    [LT] hook-length formula for dim(S_{(n,0)}) = 1 confirms only
    one copy of the trivial representation.
    """
    return 2 ** n - (n + 1)


def hecke_kernel_decomposition_sl2_fund(n: int) -> List[Dict]:
    """Decomposition of ker(av_n) by S_n-isotypic component.

    Returns a list of non-trivial contributions (j >= 1), each with:
      j, partition, specht_dim, gl2_dim, contribution

    The sum of contributions equals hecke_kernel_dim_sl2_fund(n).
    """
    parts = []
    for j in range(1, n // 2 + 1):
        sd = specht_dim_two_row(n, j)
        gd = gl2_irrep_dim(n, j)
        parts.append({
            "j": j,
            "partition": (n - j, j),
            "specht_dim": sd,
            "gl2_dim": gd,
            "contribution": sd * gd,
        })
    return parts


def hecke_kernel_table_sl2_fund(max_arity: int = 10) -> List[Dict]:
    """Table of Hecke algebra kernel dimensions for V = C^2, arities 1..max_arity.

    Each row has: n, total_dim, coinvariant_dim, kernel_dim, info_ratio.
    """
    rows = []
    for n in range(1, max_arity + 1):
        total = 2 ** n
        coinv = n + 1
        ker = total - coinv
        rows.append({
            "n": n,
            "total_dim": total,
            "coinvariant_dim": coinv,
            "kernel_dim": ker,
            "info_ratio": Fraction(ker, total),
        })
    return rows


# -- Asymptotics -------------------------------------------------------

def asymptotic_surviving_ratio(d: int, n: int) -> float:
    """Stirling approximation to surviving ratio for even parity.

    For large n with d fixed:
      binom(d+n-1, n) / d^n ~ n^{d-1} / ((d-1)! * d^n) * d^n / n^{d-1}
                             ~ 1/((d-1)!) * (1 + (d-1)/n)^n / d^n
                             -> 0 exponentially for d >= 2.

    More precisely: binom(d+n-1,n) ~ n^{d-1}/((d-1)!) for n >> d,
    so surviving ratio ~ n^{d-1}/((d-1)! * d^n) -> 0.
    """
    from math import factorial, log
    if d == 1:
        return 1.0
    # Exact computation for moderate n
    return float(surviving_ratio(d, n))


# -- Pretty printing ---------------------------------------------------

def print_cross_algebra_table(
    algebras: Optional[List[str]] = None,
    arities: Optional[List[int]] = None,
) -> None:
    """Pretty-print the cross-algebra comparison table."""
    rows = cross_algebra_table(algebras, arities)
    print(f"{'algebra':>8}  {'d':>4}  {'n':>3}  {'total':>12}  "
          f"{'coinv':>12}  {'kernel':>12}  {'info_ratio':>16}  {'surv_ratio':>16}")
    print("-" * 96)
    for r in rows:
        print(f"{r['lie_algebra']:>8}  {r['dim_g']:>4}  {r['arity']:>3}  "
              f"{r['total_dim']:>12}  {r['coinvariant_dim']:>12}  "
              f"{r['kernel_dim']:>12}  {str(r['info_ratio']):>16}  "
              f"{str(r['surviving_ratio']):>16}")


def print_sym_alt_table(
    algebras: Optional[List[str]] = None,
    arities: Optional[List[int]] = None,
) -> None:
    """Pretty-print the Sym/Alt decomposition table."""
    if algebras is None:
        algebras = ["sl_2", "sl_3", "sl_4"]
    if arities is None:
        arities = [2, 3, 4, 5]
    print(f"{'algebra':>8}  {'d':>4}  {'n':>3}  {'total':>12}  "
          f"{'sym':>12}  {'alt':>12}  {'mixed':>12}  {'sym/alt':>12}")
    print("-" * 96)
    for alg in algebras:
        d = LIE_ALGEBRA_DIMS[alg]
        for n in arities:
            dec = sym_alt_decomposition(d, n)
            ratio_str = str(dec["sym_alt_ratio"]) if dec["sym_alt_ratio"] is not None else "inf"
            print(f"{alg:>8}  {d:>4}  {n:>3}  {dec['total_dim']:>12}  "
                  f"{dec['sym_dim']:>12}  {dec['alt_dim']:>12}  "
                  f"{dec['mixed_dim']:>12}  {ratio_str:>12}")


# -- main --------------------------------------------------------------

if __name__ == "__main__":
    print("=== Cross-Algebra Averaging Kernel Table ===\n")
    print_cross_algebra_table()
    print()
    print("=== Sym/Alt Decomposition ===\n")
    print_sym_alt_table()
    print()
    print("=== Information Ratio Growth (sl_4, d=15) ===\n")
    for row in info_ratio_growth_table("sl_4", max_arity=8):
        print(f"  n={row['arity']:>2}  info_ratio = {row['info_ratio_float']:.8f}")
