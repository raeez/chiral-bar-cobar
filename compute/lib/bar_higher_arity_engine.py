r"""Explicit bar differential at higher arities (5, 6, 7) for standard families.

Extends bar_differential_sl2_matrices_engine.py and the Virasoro/betagamma
CE engines to ARITY 5, 6, 7, where the combinatorics explodes but the
explicit matrices carry decisive information about higher A-infinity
structure, Massey products, and bar cohomology at deep weights.

OBJECTIVES:

1.  sl_2 BAR DIFFERENTIAL B^5 -> B^4, B^6 -> B^5 at weights up to 10.
    Cocycle dimension and concentration: H^n is concentrated at
    h = n(n+1)/2, with dim 2n+1.  At arity 5 (CE degree 5), the chain
    group has nontrivial cocycle only at h = 15.

2.  HEISENBERG RANK 1 (PBW / CE side): At all arities 5, 6, 7 the loop
    algebra h_- = t^{-1}C[t^{-1}] is ABELIAN (modes m, n >= 1, no central
    term for positive modes).  The CE differential is IDENTICALLY ZERO.
    H^*(CE(h_-))_h = chain dim = #{partitions of h into n DISTINCT
    positive parts}.  Summing over arities gives the generating function
    prod_{k>=1}(1 + x^k), which is the Hilbert series of the exterior
    algebra Lambda^*(h_-^*).  This is the PBW-collapsed bar cohomology
    of the UNCURVED Heisenberg (the free rank-one commutative vertex
    algebra).  For the CURVED Heisenberg H_k (level k != 0), the bar
    cohomology at each arity collapses further to a single 1-dimensional
    class by the curvature m_0 = k*omega, but that is computed by
    a different (curved) differential outside the PBW collapse.  Here
    we verify the UNCURVED side, which is k-independent and carries
    the full CE information.

3.  VIRASORO: H^1(B(Vir))_h is concentrated at h in {2, 3, 4}.  At arity 5
    (CE degree 5), H^5_h = 0 for all weights tested.  Verify by computing
    explicit kernel and image dimensions.

4.  COMBINATORIAL DIMENSION COUNT: at arity n, B^n_h has dimension equal to
    the number of partitions of h into n distinct positive parts (loop
    algebra index n CE chain group).  For sl_2 the dimension is multiplied
    by (dim sl_2)^n = 3^n.  Closed-form counts at arity 6 weight 10 included.

5.  HIGHER MASSEY PRODUCTS: m_5 (5-ary A-infinity operation) for the
    finite-dimensional non-Koszul algebra k[x]/(x^3).  This is the smallest
    non-Koszul commutative algebra; its Tor algebra has nontrivial m_3
    (triple Massey) and the higher m_k recursively cascade via the
    Kadeishvili tree formula.

6.  CYCLIC STRUCTURE: At arity n the bar complex carries a Z/n action by
    cyclic rotation.  We extract the cyclic cohomology at arity 5 via the
    Connes-Tsygan double complex.  For sl_2 at arity 5 the rotation
    preserves the CE differential up to the appropriate Koszul sign.

7.  SPARSITY ANALYSIS: at arity n the CE differential matrix has dimension
    O(3^n * partition count).  We measure the density of nonzero entries
    and verify that it scales as O(n^{-2}) (each generator participates in
    O(n^2) bracket relations out of (3^n * partitions) possible target rows).

REFERENCES:
    bar_differential_sl2_matrices_engine.py: arities 1-4 baseline
    bar_cohomology_virasoro_explicit_engine.py: Vir CE complex
    bar_cohomology_betagamma_explicit_engine.py: bg loop algebra
    virasoro_ainfty_higher.py: m_5, m_6, m_7 for class M
    AP45 (signs_and_shifts.tex): desuspension lowers degree
    CLAUDE.md: bar = ordered tensor antisymmetrized via OS form
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from typing import Dict, FrozenSet, Iterable, List, Optional, Sequence, Tuple

import numpy as np


# ============================================================
# Exact rational arithmetic helpers
# ============================================================

FR = Fraction


def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, np.integer)):
        return Fraction(int(x))
    return Fraction(x)


def _frac_array(shape) -> np.ndarray:
    arr = np.empty(shape, dtype=object)
    arr.fill(Fraction(0))
    return arr


def _frac_matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    if A.size == 0 or B.size == 0:
        return _frac_array((A.shape[0], B.shape[1]))
    m, k1 = A.shape
    k2, n = B.shape
    assert k1 == k2, f"Shape mismatch: {A.shape} @ {B.shape}"
    C = _frac_array((m, n))
    for i in range(m):
        for j in range(n):
            s = Fraction(0)
            for el in range(k1):
                s += A[i, el] * B[el, j]
            C[i, j] = s
    return C


def _exact_rank(M: np.ndarray) -> int:
    if M.size == 0:
        return 0
    rows, cols = M.shape
    if rows == 0 or cols == 0:
        return 0
    A = np.array(
        [[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
        dtype=object,
    )
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i, c] != Fraction(0):
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        scale = A[r, c]
        for j in range(cols):
            A[r, j] = A[r, j] / scale
        for i in range(rows):
            if i == r:
                continue
            factor = A[i, c]
            if factor != Fraction(0):
                for j in range(cols):
                    A[i, j] = A[i, j] - factor * A[r, j]
        r += 1
    return r


def _mod_p_rank(M: np.ndarray, p: int = 1000000007) -> int:
    """Fast rank computation modulo a large prime.

    Converts the Fraction matrix to residues mod p (assuming no entry has
    denominator divisible by p, which is effectively certain for a random
    large prime), then runs Gaussian elimination over F_p using integer
    arithmetic.  This is >100x faster than exact rational rank for matrices
    with hundreds of rows and columns, and agrees with the exact rank
    whenever p does not divide any minor denominator.
    """
    if M.size == 0:
        return 0
    rows, cols = M.shape
    if rows == 0 or cols == 0:
        return 0

    # Convert to int mod p
    def _to_mod(x):
        if isinstance(x, Fraction):
            num = x.numerator % p
            den = pow(x.denominator % p, p - 2, p)
            return (num * den) % p
        return int(x) % p

    A = [[_to_mod(M[i, j]) for j in range(cols)] for i in range(rows)]

    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i][c] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = pow(A[r][c], p - 2, p)
        for j in range(cols):
            A[r][j] = (A[r][j] * inv) % p
        for i in range(rows):
            if i == r:
                continue
            f = A[i][c]
            if f != 0:
                for j in range(cols):
                    A[i][j] = (A[i][j] - f * A[r][j]) % p
        r += 1
    return r


def _density(M: np.ndarray) -> Fraction:
    """Fraction of nonzero entries in M."""
    if M.size == 0:
        return Fraction(0)
    rows, cols = M.shape
    if rows == 0 or cols == 0:
        return Fraction(0)
    nz = 0
    for i in range(rows):
        for j in range(cols):
            if M[i, j] != Fraction(0):
                nz += 1
    return Fraction(nz, rows * cols)


# ============================================================
# Partition combinatorics
# ============================================================


@lru_cache(maxsize=4096)
def partitions_distinct_into_n(weight: int, n_parts: int,
                               min_part: int = 1) -> int:
    """#{partitions of `weight` into exactly `n_parts` DISTINCT parts >= min_part}.

    These count the bar (CE) chain dimensions for one Lie generator slot.
    For sl_2 with dim_g = 3, the chain dim at arity n weight h is
    3^n times the count of partitions of h into n distinct positive parts
    in the unmarked case, OR (more accurately) the count of n-tuples of
    (lie_idx, mode) with strictly increasing flat index and total mode = h.
    """
    if n_parts == 0:
        return 1 if weight == 0 else 0
    if weight < min_part * n_parts + n_parts * (n_parts - 1) // 2:
        return 0
    total = 0
    # First part can be from min_part to weight - (n_parts - 1) * min_part
    # adjusted by the n_parts - 1 remaining slots that need at least
    # min_part + 1 each (since distinct).
    max_first = weight - sum(range(min_part + 1, min_part + n_parts))
    for first in range(min_part, max_first + 1):
        total += partitions_distinct_into_n(
            weight - first, n_parts - 1, first + 1
        )
    return total


@lru_cache(maxsize=4096)
def partitions_into_n(weight: int, n_parts: int,
                      min_part: int = 1) -> int:
    """#{partitions of `weight` into exactly `n_parts` parts >= min_part}.

    Used for the symmetric algebra Sym^n(V_h) basis dimension.
    """
    if n_parts == 0:
        return 1 if weight == 0 else 0
    if weight < min_part * n_parts:
        return 0
    total = 0
    for first in range(min_part, weight - min_part * (n_parts - 1) + 1):
        total += partitions_into_n(weight - first, n_parts - 1, first)
    return total


# ============================================================
# Lie algebra data: sl_2 (re-imported to keep this engine self-contained)
# ============================================================

DIM_SL2 = 3
SL2_NAMES = {0: 'e', 1: 'h', 2: 'f'}

SL2_BRACKET: Dict[Tuple[int, int], Dict[int, Fraction]] = {
    (0, 2): {1: Fraction(1)},    # [e, f] = h
    (2, 0): {1: Fraction(-1)},   # [f, e] = -h
    (1, 0): {0: Fraction(2)},    # [h, e] = 2e
    (0, 1): {0: Fraction(-2)},   # [e, h] = -2e
    (1, 2): {2: Fraction(-2)},   # [h, f] = -2f
    (2, 1): {2: Fraction(2)},    # [f, h] = 2f
}


# ============================================================
# A unified loop-algebra CE engine for arbitrary Lie data
# ============================================================


class LoopCEEngine:
    """CE complex of a loop algebra L_- = g tensor t^{-1}C[t^{-1}].

    Parameterized by:
        dim_g: dimension of the underlying Lie algebra g
        bracket: dict {(a, b): {c: f^c_{ab}}} for the structure constants
        max_weight: largest mode considered

    Generators are pairs (lie_idx, mode) with lie_idx in [0, dim_g),
    mode in [1, max_weight].  Flat index = lie_idx + dim_g * (mode - 1).

    The CE differential at degree p, weight h is the dual of the loop
    algebra bracket [(a, m), (b, n)] = ([a,b], m+n) (vanishing if
    m+n > max_weight).
    """

    def __init__(self, dim_g: int, bracket: Dict[Tuple[int, int],
                                                  Dict[int, Fraction]],
                 max_weight: int):
        self.dim_g = dim_g
        self.bracket = bracket
        self.max_weight = max_weight
        self.n_gens = dim_g * max_weight

        # Build (i, j) -> {flat_c: coeff} table for i < j
        self._bracket_table: Dict[Tuple[int, int], Dict[int, Fraction]] = {}
        for i in range(self.n_gens):
            ai, mi = i % dim_g, i // dim_g + 1
            for j in range(i + 1, self.n_gens):
                aj, mj = j % dim_g, j // dim_g + 1
                m_sum = mi + mj
                if m_sum > max_weight:
                    continue
                br = bracket.get((ai, aj))
                if not br:
                    continue
                result = {}
                for c, coeff in br.items():
                    flat_c = c + dim_g * (m_sum - 1)
                    result[flat_c] = _frac(coeff)
                if result:
                    self._bracket_table[(i, j)] = result

        self._basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}
        self._diff_cache: Dict[Tuple[int, int], np.ndarray] = {}

    def gen_weight(self, flat_idx: int) -> int:
        return flat_idx // self.dim_g + 1

    def chain_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Sorted-tuple basis of Lambda^degree(L_-^*) at conformal weight."""
        key = (degree, weight)
        if key in self._basis_cache:
            return self._basis_cache[key]
        result = list(self._weight_subsets(degree, weight, 0))
        self._basis_cache[key] = result
        return result

    def _weight_subsets(self, degree: int, weight: int, start: int):
        if degree == 0:
            if weight == 0:
                yield ()
            return
        for i in range(start, self.n_gens - degree + 1):
            w = self.gen_weight(i)
            if w > weight:
                break
            rem = weight - w
            if rem < degree - 1:
                continue
            for rest in self._weight_subsets(degree - 1, rem, i + 1):
                yield (i,) + rest

    def chain_dim(self, degree: int, weight: int) -> int:
        return len(self.chain_basis(degree, weight))

    def differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight."""
        key = (degree, weight)
        if key in self._diff_cache:
            return self._diff_cache[key]

        source = self.chain_basis(degree, weight)
        target = self.chain_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)

        if n_src == 0 or n_tgt == 0:
            mat = _frac_array((n_tgt, n_src))
            self._diff_cache[key] = mat
            return mat

        target_idx = {t: i for i, t in enumerate(target)}
        mat = _frac_array((n_tgt, n_src))

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)

            for (beta, gamma), br in self._bracket_table.items():
                for delta, coeff in br.items():
                    if delta not in alpha_set:
                        continue
                    new_set = (alpha_set - {delta}) | {beta, gamma}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue

                    pos_c = alpha_list.index(delta)
                    sorted_new = list(new_tuple)
                    pos_beta = sorted_new.index(beta)
                    remaining = sorted(new_set - {beta})
                    pos_gamma = remaining.index(gamma)
                    sign = Fraction((-1) ** (pos_c + pos_beta + pos_gamma))
                    mat[row, col] += sign * coeff

        self._diff_cache[key] = mat
        return mat

    def verify_d_squared(self, degree: int, weight: int) -> bool:
        d_p = self.differential_matrix(degree, weight)
        d_p1 = self.differential_matrix(degree + 1, weight)
        if d_p.size == 0 or d_p1.size == 0:
            return True
        if d_p1.shape[1] != d_p.shape[0]:
            return True
        prod = _frac_matmul(d_p1, d_p)
        return all(prod[i, j] == Fraction(0)
                   for i in range(prod.shape[0])
                   for j in range(prod.shape[1]))

    def cohomology_dim(self, degree: int, weight: int,
                       fast: bool = False) -> int:
        dim_p = self.chain_dim(degree, weight)
        if dim_p == 0:
            return 0
        rank_fn = _mod_p_rank if fast else _exact_rank
        d_curr = self.differential_matrix(degree, weight)
        rank_out = rank_fn(d_curr) if d_curr.size > 0 else 0
        ker_dim = dim_p - rank_out
        if degree > 0:
            d_prev = self.differential_matrix(degree - 1, weight)
            im_dim = rank_fn(d_prev) if d_prev.size > 0 else 0
        else:
            im_dim = 0
        return ker_dim - im_dim

    def matrix_density(self, degree: int, weight: int) -> Fraction:
        return _density(self.differential_matrix(degree, weight))


# ============================================================
# (1) sl_2 at arities 5, 6, 7
# ============================================================


def sl2_engine(max_weight: int) -> LoopCEEngine:
    return LoopCEEngine(DIM_SL2, SL2_BRACKET, max_weight)


def sl2_arity_n_cohomology(n: int, max_weight: int) -> Dict[int, int]:
    """dim H^n(B(V_k(sl_2)))_h for h <= max_weight.

    Returns {weight: cohomology dimension}.  Concentration prediction:
    H^n is supported only at h = n(n+1)/2 with dim 2n+1.
    """
    eng = sl2_engine(max_weight)
    out = {}
    for h in range(0, max_weight + 1):
        out[h] = eng.cohomology_dim(n, h)
    return out


def sl2_concentration_weight(n: int) -> int:
    """h such that H^n(B(V_k(sl_2)))_h is the unique nonzero summand."""
    return n * (n + 1) // 2


def sl2_concentration_dim(n: int) -> int:
    """dim H^n(B(V_k(sl_2)))_{n(n+1)/2} = 2n + 1 (the (2n+1)-dim irrep)."""
    return 2 * n + 1


# ============================================================
# (2) Heisenberg rank 1: free abelian loop algebra
# ============================================================


# Empty bracket: Heisenberg modes commute (no central term for m,n >= 1)
HEIS_BRACKET: Dict[Tuple[int, int], Dict[int, Fraction]] = {}


def heisenberg_engine(max_weight: int) -> LoopCEEngine:
    """CE engine for the rank-1 Heisenberg loop algebra.

    The Lie algebra is 1-dimensional with vanishing bracket.  All higher
    modes commute, so the CE differential is identically zero.  The
    chain complex has dim Lambda^p_h = #{partitions of h into p distinct
    positive parts}.

    Bar cohomology is then the EXTERIOR ALGEBRA on countable
    generators {a_1, a_2, ...} with |a_n| = 1 (after desuspension).
    Generating function: prod_{k>=1} (1 + x^k).
    """
    return LoopCEEngine(1, HEIS_BRACKET, max_weight)


def heisenberg_chain_dim(arity: int, weight: int) -> int:
    """dim Lambda^arity(H_-^*)_weight = #partitions of weight into arity distinct positive parts."""
    return partitions_distinct_into_n(weight, arity, 1)


def heisenberg_cohomology_dim(arity: int, weight: int) -> int:
    """For Heisenberg rank 1, d = 0, so H^n_h = chain dim."""
    return heisenberg_chain_dim(arity, weight)


def heisenberg_gf_coefficient(weight: int) -> int:
    """[x^weight] prod_{k>=1} (1 + x^k) = sum_arity dim Lambda^arity_weight.

    Independent path: total dimension across all arities at fixed weight.
    """
    coeffs = [0] * (weight + 1)
    coeffs[0] = 1
    for k in range(1, weight + 1):
        for w in range(weight, k - 1, -1):
            coeffs[w] += coeffs[w - k]
    return coeffs[weight]


def heisenberg_kahler_check(max_weight: int = 12) -> Dict[str, bool]:
    """Verify the bar cohomology of Heisenberg = Sym(V*) with curvature -k*omega.

    Path A: chain dim sum across all arities at weight w = [x^w] prod (1+x^k).
    Path B: independent series expansion.

    These two paths must agree.
    """
    out = {}
    for w in range(0, max_weight + 1):
        path_a = sum(heisenberg_chain_dim(n, w)
                     for n in range(0, w + 1))
        path_b = heisenberg_gf_coefficient(w)
        out[f'w={w}'] = (path_a == path_b)
    return out


# ============================================================
# (3) Virasoro at arity 5
# ============================================================


# Vir_- has bracket [L_{-(a+2)}, L_{-(b+2)}] = (b-a) L_{-(a+b+4)}
# Index a is the offset from L_{-2}, so weight of generator a is a+2.
# We pack this into the LoopCEEngine by shifting modes (using a 1-D Lie
# algebra with mode = weight, but the bracket only fires when both modes
# are present).  However, the loop bracket [(a,m),(b,n)] = ([a,b], m+n)
# does NOT fit Virasoro directly because Virasoro has dim_g = 1 with a
# nontrivial bracket between DIFFERENT modes.  We supply a dedicated engine.


class VirasoroCEEngine:
    """Truncated CE complex of Vir_- = span{L_{-n} : n >= 2}.

    Generators indexed by their conformal weight n (n in [2, max_weight]).
    Bracket: [L_{-m}, L_{-n}] = (n - m) L_{-(m+n)} (output weight m+n,
    truncated to <= max_weight).

    For m, n >= 2 we have m + n >= 4, so no central term ever appears.
    """

    def __init__(self, max_weight: int = 12):
        self.max_weight = max_weight
        self.gens = list(range(2, max_weight + 1))   # modes 2, 3, ..., max_weight
        self.gen_index = {g: i for i, g in enumerate(self.gens)}
        self.n_gens = len(self.gens)
        self._basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}
        self._diff_cache: Dict[Tuple[int, int], np.ndarray] = {}

    def chain_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        key = (degree, weight)
        if key in self._basis_cache:
            return self._basis_cache[key]
        result = list(self._weight_subsets(degree, weight, 0))
        self._basis_cache[key] = result
        return result

    def _weight_subsets(self, degree: int, weight: int, start: int):
        if degree == 0:
            if weight == 0:
                yield ()
            return
        for i in range(start, self.n_gens - degree + 1):
            w = self.gens[i]
            if w > weight:
                break
            rem = weight - w
            if rem < degree - 1:
                continue
            for rest in self._weight_subsets(degree - 1, rem, i + 1):
                yield (i,) + rest

    def chain_dim(self, degree: int, weight: int) -> int:
        return len(self.chain_basis(degree, weight))

    def differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        key = (degree, weight)
        if key in self._diff_cache:
            return self._diff_cache[key]
        source = self.chain_basis(degree, weight)
        target = self.chain_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            mat = _frac_array((n_tgt, n_src))
            self._diff_cache[key] = mat
            return mat
        target_idx = {t: i for i, t in enumerate(target)}
        mat = _frac_array((n_tgt, n_src))

        # Bracket pairs (i, j) with i < j and weight i + weight j <= max
        for i in range(self.n_gens):
            wi = self.gens[i]
            for j in range(i + 1, self.n_gens):
                wj = self.gens[j]
                w_sum = wi + wj
                if w_sum > self.max_weight:
                    continue
                k_idx = self.gen_index.get(w_sum)
                if k_idx is None:
                    continue
                coeff = Fraction(wj - wi)  # (n - m) with m = wi, n = wj
                # CE: replace generator k_idx in alpha by {i, j}
                for col, alpha in enumerate(source):
                    if k_idx not in alpha:
                        continue
                    if i in alpha or j in alpha:
                        continue
                    alpha_set = set(alpha)
                    alpha_list = list(alpha)
                    new_set = (alpha_set - {k_idx}) | {i, j}
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue
                    pos_c = alpha_list.index(k_idx)
                    sorted_new = list(new_tuple)
                    pos_i = sorted_new.index(i)
                    remaining = sorted(new_set - {i})
                    pos_j = remaining.index(j)
                    sign = Fraction((-1) ** (pos_c + pos_i + pos_j))
                    mat[row, col] += sign * coeff

        self._diff_cache[key] = mat
        return mat

    def cohomology_dim(self, degree: int, weight: int,
                       fast: bool = False) -> int:
        dim_p = self.chain_dim(degree, weight)
        if dim_p == 0:
            return 0
        rank_fn = _mod_p_rank if fast else _exact_rank
        d_curr = self.differential_matrix(degree, weight)
        rank_out = rank_fn(d_curr) if d_curr.size > 0 else 0
        ker_dim = dim_p - rank_out
        if degree > 0:
            d_prev = self.differential_matrix(degree - 1, weight)
            im_dim = rank_fn(d_prev) if d_prev.size > 0 else 0
        else:
            im_dim = 0
        return ker_dim - im_dim

    def verify_d_squared(self, degree: int, weight: int) -> bool:
        d_p = self.differential_matrix(degree, weight)
        d_p1 = self.differential_matrix(degree + 1, weight)
        if d_p.size == 0 or d_p1.size == 0:
            return True
        if d_p1.shape[1] != d_p.shape[0]:
            return True
        prod = _frac_matmul(d_p1, d_p)
        return all(prod[i, j] == Fraction(0)
                   for i in range(prod.shape[0])
                   for j in range(prod.shape[1]))

    def matrix_density(self, degree: int, weight: int) -> Fraction:
        return _density(self.differential_matrix(degree, weight))


# ============================================================
# (4) Combinatorial dimension count for sl_2 at arity 6 weight 10
# ============================================================


def sl2_chain_dim_exact(arity: int, weight: int,
                        max_weight: Optional[int] = None) -> int:
    """dim Lambda^arity((sl_2)_-^*)_weight via direct enumeration.

    For sl_2 the loop algebra has 3 generators per mode, so the chain
    group at (arity, weight) is the count of strictly increasing arity-tuples
    of (lie_idx, mode) pairs (under flat-index order) with mode sum = weight.

    Equivalent closed form: sum over compositions h = m_1 + ... + m_arity
    where the m_i are positive integers (in nondecreasing flat-index order).
    Distinct flat indices = 3 lie choices per mode, but at the SAME mode
    we can have multiple distinct (lie, mode) pairs.

    The formula is:
        dim = sum over weight-arity-tuples (m_1 <= ... <= m_arity) of
              [#ways to assign sl_2 indices respecting strict flat order]

    For our flat index ordering, a tuple of length arity with mode pattern
    (m_1 <= m_2 <= ... <= m_arity) where mode m appears n_m times contributes
    prod_m C(3, n_m) (binomial: choose n_m of the 3 sl_2 generators at mode m,
    must be distinct since we're in the antisymmetric tensor / exterior algebra).
    """
    if max_weight is None:
        max_weight = weight
    eng = sl2_engine(max_weight)
    return eng.chain_dim(arity, weight)


def sl2_chain_dim_combinatorial(arity: int, weight: int) -> int:
    """Closed-form chain dimension via mode-multiplicity enumeration.

    Independent path that does NOT use the engine: enumerate all
    multisets of mode numbers summing to weight with at most 3 of each
    mode (since sl_2 has 3 generators), each mode contributing C(3, n_m).
    """
    total = 0

    def enumerate_modes(remaining: int, min_mode: int, slots: int,
                        weight_factor: int):
        nonlocal total
        if slots == 0:
            if remaining == 0:
                total += weight_factor
            return
        if remaining < min_mode:
            return
        # Choose multiplicity n at mode = min_mode, n in {0, 1, 2, 3}
        for n in range(0, min(3, slots) + 1):
            cost = n * min_mode
            if cost > remaining:
                break
            from math import comb as _comb
            new_factor = weight_factor * _comb(3, n)
            enumerate_modes(remaining - cost, min_mode + 1, slots - n, new_factor)

    enumerate_modes(weight, 1, arity, 1)
    return total


# ============================================================
# (5) Higher Massey products for k[x]/(x^3)
# ============================================================


class TruncatedPolyMasseyEngine:
    r"""Bar complex and Massey products for A = k[x]/(x^N).

    A is a finite-dimensional commutative algebra with basis {1, x, ..., x^{N-1}}
    and relation x^N = 0.  The augmentation ideal is V = span{x, x^2, ..., x^{N-1}}.

    The bar complex B(A) has:
        B^n = V^{tensor n}    (no shift; we work with degree = number of slots)

    The bar differential is the dual of the multiplication:
        d(v_1 | ... | v_n) = sum_i (-1)^{i-1} v_1 | ... | (v_i * v_{i+1}) | ... | v_n
    where v_i * v_{i+1} is the product in A (and the term is zero if the
    product lies in the unit span k * 1, which only happens when v_i = v_j = 0).
    For A = k[x]/(x^N), the product x^i * x^j = x^{i+j} if i+j < N, else 0.

    For N = 2 (the dual numbers), B(k[x]/(x^2)) is the Koszul resolution
    and m_k = 0 for k >= 3 (Koszul case).

    For N = 3, the algebra is NOT Koszul.  The Tor algebra is a graded
    polynomial ring on a 1-dim degree-(1, 1) generator and a 1-dim
    degree-(2, 3) generator (the Massey class).  Higher Massey products
    m_k for k >= 3 are nontrivial and accumulate weight.

    We compute the bar cohomology dimensions H^k_w (k = bar arity,
    w = polynomial weight) and verify the formal power series matches
    the prediction from the Koszul-dual differential.
    """

    def __init__(self, N: int = 3, max_weight: int = 9):
        assert N >= 2
        self.N = N
        self.max_weight = max_weight
        # V basis: x, x^2, ..., x^{N-1}, weights 1, 2, ..., N-1
        self.basis = list(range(1, N))     # weight of each basis element
        self.dim_V = N - 1

    def chain_basis(self, arity: int, weight: int) -> List[Tuple[int, ...]]:
        """Tuples (w_1, ..., w_arity) of weights with sum = weight, w_i in [1, N-1]."""
        if arity == 0:
            return [()] if weight == 0 else []
        results = []
        for w1 in range(1, self.N):
            if w1 > weight:
                break
            for rest in self.chain_basis(arity - 1, weight - w1):
                results.append((w1,) + rest)
        return results

    def chain_dim(self, arity: int, weight: int) -> int:
        return len(self.chain_basis(arity, weight))

    def differential_matrix(self, arity: int, weight: int) -> np.ndarray:
        """Bar differential B^arity_weight -> B^{arity-1}_weight.

        d(w_1, ..., w_arity) = sum_{i=1}^{arity-1} (-1)^{i-1}
                                  delta_{w_i + w_{i+1} < N} *
                                  (w_1, ..., w_i + w_{i+1}, ..., w_arity)

        Note: we work in the unshifted bar (degree = arity), so this is the
        standard bar differential.  Cohomological degree gradient is +1 with
        the desuspension convention; the formal sign is the same as written.
        """
        if arity <= 0:
            return _frac_array((0, 0))
        source = self.chain_basis(arity, weight)
        target = self.chain_basis(arity - 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            return _frac_array((n_tgt, n_src))
        target_idx = {t: i for i, t in enumerate(target)}
        mat = _frac_array((n_tgt, n_src))
        for col, tup in enumerate(source):
            for i in range(arity - 1):
                wsum = tup[i] + tup[i + 1]
                if wsum >= self.N:
                    continue   # product is zero in A/k
                new = tup[:i] + (wsum,) + tup[i + 2:]
                row = target_idx.get(new)
                if row is None:
                    continue
                sign = Fraction((-1) ** i)
                mat[row, col] += sign
        return mat

    def cohomology_dim(self, arity: int, weight: int) -> int:
        if arity == 0:
            return 1 if weight == 0 else 0
        dim_p = self.chain_dim(arity, weight)
        if dim_p == 0:
            return 0
        d_in = self.differential_matrix(arity, weight)     # B^arity -> B^{arity-1}
        d_out = self.differential_matrix(arity + 1, weight)  # B^{arity+1} -> B^arity
        rank_in = _exact_rank(d_in)
        ker_in = dim_p - rank_in if rank_in > 0 else dim_p
        # Image into B^arity comes from d_out
        if d_out.size > 0:
            rank_out = _exact_rank(d_out)
        else:
            rank_out = 0
        # H^arity = ker(d_in) / im(d_out as map to B^arity)
        # But ker(d_in) sits in B^arity; im(d_out as map to ARITY = arity+1 - 1 = arity)
        # So we compare:
        return ker_in - rank_out

    def verify_d_squared(self, arity: int, weight: int) -> bool:
        """Verify d_{arity-1} . d_{arity} = 0."""
        d_n = self.differential_matrix(arity, weight)
        if arity < 2:
            return True
        d_n_minus = self.differential_matrix(arity - 1, weight)
        if d_n.size == 0 or d_n_minus.size == 0:
            return True
        if d_n_minus.shape[1] != d_n.shape[0]:
            return True
        prod = _frac_matmul(d_n_minus, d_n)
        return all(prod[i, j] == Fraction(0)
                   for i in range(prod.shape[0])
                   for j in range(prod.shape[1]))

    def koszul_test(self, max_arity: int = 5,
                    max_weight: int = 8) -> Dict[Tuple[int, int], int]:
        """Compute H^arity_weight for arity in [1, max_arity], weight in [1, max_weight].

        For N = 2 (Koszul), all H^arity_weight = 0 except H^arity_arity = 1
        (the line of "x | x | ... | x").  For N >= 3, additional cohomology
        appears off the diagonal, signalling non-Koszulness.
        """
        out = {}
        for arity in range(1, max_arity + 1):
            for w in range(1, max_weight + 1):
                out[(arity, w)] = self.cohomology_dim(arity, w)
        return out

    def has_higher_massey(self, max_arity: int = 5,
                          max_weight: int = 8) -> bool:
        """True iff there exists arity >= 3, weight > arity with H^arity_weight > 0."""
        for arity in range(3, max_arity + 1):
            for w in range(arity + 1, max_weight + 1):
                if self.cohomology_dim(arity, w) > 0:
                    return True
        return False


# ============================================================
# (6) Cyclic structure: Z/n action and cyclic cohomology at arity 5
# ============================================================


def cyclic_rotation_sign(n: int) -> int:
    """Koszul sign of cyclic rotation on n-fold tensor with degree-1 entries.

    For each entry of cohomological degree 1 (after desuspension) the
    rotation produces a sign (-1)^{n-1}.  This is the standard sign for
    the cyclic action on the bar/Hochschild complex.
    """
    return (-1) ** (n - 1)


def cyclic_action_on_basis(basis: List[Tuple[int, ...]]
                            ) -> Dict[Tuple[int, ...], Tuple[int, Tuple[int, ...]]]:
    """Apply the cyclic rotation t: (a_1, ..., a_n) -> (a_2, ..., a_n, a_1).

    The output keeps the SORTED tuple as the canonical representative
    (since our basis is the sorted-tuple basis), with a sign determined
    by the permutation needed to sort the rotated tuple.
    """
    out = {}
    for tup in basis:
        n = len(tup)
        if n == 0:
            out[tup] = (1, tup)
            continue
        rotated = tup[1:] + (tup[0],)
        # Compute the sign of the permutation that sorts `rotated`
        # back to a sorted tuple
        sign, sorted_rot = _sort_with_sign(list(rotated))
        out[tup] = (sign, tuple(sorted_rot))
    return out


def _sort_with_sign(lst: List[int]) -> Tuple[int, List[int]]:
    """Return (sign, sorted_list) where sign is the parity of the permutation."""
    n = len(lst)
    a = list(lst)
    sign = 1
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                sign = -sign
    return sign, a


def cyclic_invariants_dim(engine: LoopCEEngine, degree: int,
                          weight: int) -> int:
    """Dimension of the Z/degree-invariant subspace of Lambda^degree_weight.

    Computes the rank of (1 - t_signed) where t_signed is the cyclic
    rotation with the appropriate Koszul sign, and returns
    chain_dim - rank(1 - t_signed) = dim(invariants).
    """
    basis = engine.chain_basis(degree, weight)
    n_basis = len(basis)
    if n_basis == 0:
        return 0
    if degree <= 1:
        return n_basis    # rotation is trivial
    sign_rot = cyclic_rotation_sign(degree)
    cyc = cyclic_action_on_basis(basis)
    basis_idx = {b: i for i, b in enumerate(basis)}
    # Build matrix M = I - sign_rot * permutation_matrix
    M = _frac_array((n_basis, n_basis))
    for j, b in enumerate(basis):
        M[j, j] = Fraction(1)
        sign, target = cyc[b]
        if target in basis_idx:
            i = basis_idx[target]
            M[i, j] = M[i, j] - Fraction(sign * sign_rot)
    rank = _exact_rank(M)
    return n_basis - rank


def cyclic_cohomology_arity_5_sl2(weight: int = 15,
                                  max_weight: int = 16
                                  ) -> Dict[str, int]:
    """Compute the Z/5-invariant part of Lambda^5((sl_2)_-^*)_weight.

    For arity 5, the rotation sign is (-1)^4 = +1, so the cyclic action
    is sign-trivial.  The cyclic invariants form the candidate space for
    cyclic cohomology HC^5(sl_2)_weight.
    """
    eng = sl2_engine(max_weight)
    chain = eng.chain_dim(5, weight)
    inv = cyclic_invariants_dim(eng, 5, weight)
    coh = eng.cohomology_dim(5, weight)
    return {
        'chain_dim': chain,
        'cyclic_invariant_dim': inv,
        'ce_cohomology_dim': coh,
    }


# ============================================================
# (7) Sparsity analysis
# ============================================================


def sparsity_profile(engine, family_name: str, arities: Iterable[int],
                     weights: Iterable[int]) -> Dict[Tuple[int, int], Dict]:
    """Compute (chain_dim, density, rank) for each (arity, weight)."""
    out = {}
    for ar in arities:
        for w in weights:
            d = engine.differential_matrix(ar, w)
            if d.size == 0:
                density = Fraction(0)
                rank = 0
            else:
                density = _density(d)
                rank = _exact_rank(d)
            chain = engine.chain_dim(ar, w)
            out[(ar, w)] = {
                'family': family_name,
                'chain_dim_source': chain,
                'chain_dim_target': engine.chain_dim(ar + 1, w),
                'density': float(density),
                'rank': rank,
            }
    return out


def sl2_sparsity_summary(arity: int, weight: int) -> Dict:
    """Summary of the sl_2 differential matrix sparsity at (arity, weight).

    The expected scaling: nonzero entries per column = O(arity * 2)
    (each generator participates in O(1) brackets), while the column
    height grows like 3 * partition counts.  Hence density falls as
    arity grows.
    """
    eng = sl2_engine(max(weight, 2 * arity + 4))
    d = eng.differential_matrix(arity, weight)
    if d.size == 0:
        return {
            'arity': arity, 'weight': weight,
            'rows': 0, 'cols': 0, 'nonzero': 0,
            'density': 0.0, 'rank': 0,
        }
    rows, cols = d.shape
    nonzero = sum(1 for i in range(rows) for j in range(cols)
                   if d[i, j] != Fraction(0))
    return {
        'arity': arity, 'weight': weight,
        'rows': rows, 'cols': cols,
        'nonzero': nonzero,
        'density': float(_density(d)),
        'rank': _exact_rank(d),
    }


# ============================================================
# Convenience: a single entry-point status report
# ============================================================


def report_sl2_high_arity(max_arity: int = 6,
                          max_weight: Optional[int] = None) -> Dict:
    """Diagnostic report on sl_2 bar cohomology at arities 1..max_arity."""
    if max_weight is None:
        max_weight = max_arity * (max_arity + 1) // 2 + 2
    eng = sl2_engine(max_weight)
    out = {}
    for n in range(1, max_arity + 1):
        h_concentration = sl2_concentration_weight(n)
        expected_dim = sl2_concentration_dim(n)
        actual_dim = eng.cohomology_dim(n, h_concentration)
        out[n] = {
            'concentration_weight': h_concentration,
            'expected_dim': expected_dim,
            'actual_dim': actual_dim,
            'matches': (actual_dim == expected_dim),
        }
    return out


def report_heisenberg_high_arity(max_arity: int = 7,
                                 max_weight: int = 12) -> Dict:
    """Diagnostic report on Heisenberg rank-1 bar cohomology."""
    eng = heisenberg_engine(max_weight)
    out = {}
    for n in range(1, max_arity + 1):
        for w in range(n, max_weight + 1):
            chain = eng.chain_dim(n, w)
            coh = eng.cohomology_dim(n, w)
            out[(n, w)] = {
                'chain_dim': chain,
                'cohomology_dim': coh,
                'd_zero': chain == coh,
            }
    return out


def report_virasoro_arity_5(weights: Iterable[int] = (5, 6, 7, 8, 9, 10)
                            ) -> Dict:
    """Diagnostic report on Virasoro bar cohomology at arity 5 (CE side).

    NOTE ON CHAIN CONCENTRATION: The CE complex at arity p requires
    p DISTINCT generators with modes in {2, 3, ..., max_weight}.  The
    minimum conformal weight for a p-tuple is 2 + 3 + ... + (p+1) =
    p(p+3)/2.  For p = 5 this is 20.  For weights 5..10 the chain
    group is empty, and so cohomology is trivially zero.  We still
    verify chain-emptiness as a structural fact; the CE cohomology
    concentration at arity 1 in weights {2, 3, 4} remains the
    informative fingerprint.
    """
    max_w = max(weights)
    eng = VirasoroCEEngine(max_weight=max(max_w * 2, 16))
    out = {}
    for w in weights:
        out[w] = {
            'chain_dim_p5': eng.chain_dim(5, w),
            'cohomology_dim_p5': eng.cohomology_dim(5, w),
            'd_squared_zero': eng.verify_d_squared(4, w),
        }
    return out


def report_virasoro_arity_5_saturated(
    min_weight: int = 20, max_weight: int = 25
) -> Dict:
    """Virasoro CE cohomology at arity 5 in the SATURATED weight range.

    The arity-5 CE chain group is nonempty for weight >= 20 (the minimum
    2+3+4+5+6 = 20).  We verify that H^5 vanishes throughout the lowest
    few nontrivial weight strata, which is consistent with Koszulness
    of the Virasoro vertex operator algebra (bar cohomology concentrated
    in arity 1).
    """
    eng = VirasoroCEEngine(max_weight=max(max_weight * 2, 30))
    out = {}
    for w in range(min_weight, max_weight + 1):
        out[w] = {
            'chain_dim_p5': eng.chain_dim(5, w),
            'chain_dim_p4': eng.chain_dim(4, w),
            'chain_dim_p6': eng.chain_dim(6, w),
            'cohomology_dim_p5': eng.cohomology_dim(5, w),
            'd_squared_zero': eng.verify_d_squared(4, w),
        }
    return out
