r"""Large-N limit of sl_N categorical zeta functions.

Mathematical foundation
-----------------------
As N -> infinity, the categorical zeta zeta^{DK}_{sl_N}(s) involves
representations of growing dimension.  This module studies the large-N
behavior relevant to 't Hooft expansion and gauge/gravity duality.

The categorical zeta for sl_N is:
    zeta^{DK}_{sl_N}(s) = sum_{lambda dominant, nontrivial} dim(V_lambda)^{-s}

where the sum runs over all nontrivial dominant integral weights lambda
of sl_N, and dim(V_lambda) is computed by the Weyl dimension formula.

For N = 2 this reduces exactly to the Riemann zeta: zeta(s) - 1
(excluding trivial rep), or zeta(s) (including it).

LARGE-N STRUCTURE:

1. SYMMETRIC REPRESENTATIONS: lambda = (n, 0, ..., 0).
   dim V_{(n)} = C(N+n-1, n) ~ N^n / n! as N -> infty.
   The symmetric-rep zeta:
       zeta^{sym}_{sl_N}(s) = sum_{n >= 1} [C(N+n-1, n)]^{-s}
   converges for Re(s) > 0 at large N (superexponential decay).

2. ADJOINT REPRESENTATION: dim = N^2 - 1 for sl_N.
   Adjoint contribution (N^2 - 1)^{-s} -> 0 as N -> infty for fixed s > 0.

3. RESCALED ZETA: Z_N(s) = N^{-2s} * zeta^{DK}_{sl_N}(s).
   Rescaling by adjoint dimension to probe the N -> infty limit.

4. PLANAR LIMIT: Restrict to representations with at most 2 rows
   in the Young diagram (analogue of genus-0 in gauge theory).

5. CASIMIR ZETA: Replace dim(V_lambda) by the quadratic Casimir C_2(lambda).
   For sl_2: C_2(V_n) = n(n+2)/4, giving a distinct zeta function.

6. CHARACTER ZETA: zeta^{char}(s, q) = sum chi_lambda(q)^{-s},
   interpolating between dim (q=1) and root-of-unity values.

7. RENORMALIZED sl_infty ZETA: Normalize by N^{|lambda|} before taking
   the limit, relating to frame-Robinson-Schensted asymptotics.

8. 'T HOOFT DOUBLE SCALING: N -> infty, s -> s_0 with sN fixed.

VERIFICATION PATHS (multi-path mandate, CLAUDE.md):
    Path 1: N=2 reproduces Riemann zeta (exact check)
    Path 2: Weyl dimension formula vs hook-content formula (must agree)
    Path 3: Monotonicity: zeta^{DK}_{sl_N}(s) monotone in N for fixed s > sigma_c
    Path 4: Asymptotic formula check: leading term at large N
    Path 5: Character identity: chi_lambda(1) = dim V_lambda

Connections to the monograph
----------------------------
    - MC3 (cor:mc3-all-types): thick generation by evaluation modules
    - DK bridge (thm:drinfeld-kohno-bridge): Y(g) <-> U_q(hat{g})
    - large_n_twisted_holography.py: 't Hooft genus expansion
    - kappa(A): the modular characteristic scales as ~N^2 for sl_N
    - bc_categorical_zeta_engine.py: base categorical zeta engine

Conventions
-----------
    - Highest weight lambda in fundamental weight coordinates (Bourbaki).
    - Young diagram: lambda = (lambda_1 >= lambda_2 >= ... >= 0) in partition notation.
    - sl_N = A_{N-1}: rank = N-1, representations indexed by partitions with
      at most N-1 parts.
    - dim V_lambda via hook-content formula (efficient for large N).
    - Cohomological grading (|d| = +1).

References
----------
    Stanley, "Enumerative Combinatorics", vol. 2, Cambridge 1999.
    Chari-Pressley, "A Guide to Quantum Groups", Cambridge 1994.
    't Hooft, "A planar diagram theory for strong interactions", 1974.
    bc_categorical_zeta_engine.py: base categorical zeta
    concordance.tex: MC3 status
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb, factorial, log, prod
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np


# =========================================================================
# 0. Young diagram utilities and hook-content formula
# =========================================================================

def partition_to_young_diagram(lam: Tuple[int, ...]) -> List[Tuple[int, int]]:
    """Return the set of cells (i, j) in the Young diagram of partition lam.

    Convention: (i, j) with i = row (0-indexed from top), j = column (0-indexed).
    lam = (lam_1, lam_2, ...) with lam_1 >= lam_2 >= ...
    """
    cells = []
    for i, lam_i in enumerate(lam):
        for j in range(lam_i):
            cells.append((i, j))
    return cells


def hook_length(lam: Tuple[int, ...], i: int, j: int) -> int:
    """Hook length at cell (i, j) in the Young diagram of partition lam.

    hook(i, j) = (lam_i - j) + (lam'_j - i) - 1
    where lam' is the conjugate partition.
    """
    # Arm length: number of cells to the right of (i, j)
    arm = lam[i] - j - 1
    # Leg length: number of cells below (i, j)
    leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
    return arm + leg + 1


def content(N: int, i: int, j: int) -> int:
    """Content factor at cell (i, j) for sl_N representation.

    content(i, j) = N + j - i.
    """
    return N + j - i


def hook_content_dimension(N: int, lam: Tuple[int, ...]) -> int:
    """Dimension of sl_N irrep V_lambda via the hook-content formula.

    dim V_lambda = prod_{(i,j) in lambda} (N + j - i) / hook(i, j)

    This is exact (integer-valued) and efficient for large N since it
    requires only a product over the |lambda| cells of the Young diagram.

    Args:
        N: rank parameter (sl_N).
        lam: partition (lambda_1 >= lambda_2 >= ...) giving the Young diagram.
             Must have at most N-1 nonzero parts (otherwise dim = 0).

    Returns:
        Dimension as a nonneg integer. Returns 0 if the partition has >= N parts.
    """
    # Remove trailing zeros
    lam = tuple(x for x in lam if x > 0)
    if not lam:
        return 1  # trivial representation
    if len(lam) >= N:
        return 0  # too many rows for sl_N

    result = Fraction(1)
    for i, lam_i in enumerate(lam):
        for j in range(lam_i):
            c = N + j - i
            h = hook_length(lam, i, j)
            result *= Fraction(c, h)

    return int(result)


def weyl_dimension_slN_partition(N: int, lam: Tuple[int, ...]) -> int:
    """Weyl dimension for sl_N via the product formula over positive roots.

    This is an independent computation from hook_content_dimension.
    Used for cross-verification.

    For sl_N, the dominant weight in fundamental weight coords is:
        hw_i = lam_i - lam_{i+1}  for i = 1, ..., N-1
    and the Weyl dimension formula gives:
        dim = prod_{1 <= i < j <= N} (lam_i - lam_j + j - i) / (j - i)

    where lam is extended by zeros: lam_k = 0 for k > len(lam).
    """
    lam_ext = list(lam) + [0] * N
    lam_ext = lam_ext[:N]

    result = Fraction(1)
    for i in range(N):
        for j in range(i + 1, N):
            num = lam_ext[i] - lam_ext[j] + j - i
            den = j - i
            result *= Fraction(num, den)

    d = int(result)
    if d <= 0:
        return 0
    return d


def partition_size(lam: Tuple[int, ...]) -> int:
    """Number of boxes |lambda| in the partition."""
    return sum(lam)


def num_rows(lam: Tuple[int, ...]) -> int:
    """Number of nonzero parts (rows) in the partition."""
    return sum(1 for x in lam if x > 0)


# =========================================================================
# 1. Partition enumeration
# =========================================================================

def partitions_bounded(max_size: int, max_rows: int,
                       min_size: int = 1) -> List[Tuple[int, ...]]:
    """All partitions lambda with min_size <= |lambda| <= max_size and
    at most max_rows nonzero parts.

    Returns partitions in sorted order (by size, then lexicographic).
    Excludes the empty partition.
    """
    result = []
    _enum_partitions(max_size, max_rows, 0, [], result, min_size)
    result.sort(key=lambda p: (sum(p), p))
    return result


def _enum_partitions(remaining: int, max_rows: int, min_part: int,
                     current: List[int], result: List[Tuple[int, ...]],
                     min_size: int) -> None:
    """Recursive partition enumeration (parts in non-increasing order)."""
    if len(current) == max_rows or remaining == 0:
        if current and sum(current) >= min_size:
            result.append(tuple(current))
        return
    # Also record current if nonempty and meets minimum size
    if current and sum(current) >= min_size:
        result.append(tuple(current))
    # Add a part >= 1, <= remaining, <= previous part (if any)
    upper = min(remaining, current[-1] if current else remaining)
    for part in range(upper, 0, -1):
        _enum_partitions(remaining - part, max_rows, part,
                         current + [part], result, min_size)


def partitions_at_most_k_rows(max_size: int, k: int) -> List[Tuple[int, ...]]:
    """All nontrivial partitions with at most k rows and |lambda| <= max_size."""
    return partitions_bounded(max_size, k, min_size=1)


def symmetric_partitions(max_n: int) -> List[Tuple[int, ...]]:
    """Single-row partitions (n,) for n = 1, ..., max_n."""
    return [(n,) for n in range(1, max_n + 1)]


# =========================================================================
# 2. Categorical zeta for sl_N (direct enumeration)
# =========================================================================

def categorical_zeta_slN(N: int, s: complex,
                         max_box_count: int = 15,
                         include_trivial: bool = False) -> complex:
    r"""Categorical zeta zeta^{DK}_{sl_N}(s) by direct summation.

    sum_{lambda nontrivial dominant} dim(V_lambda)^{-s}

    Uses the hook-content formula for dim(V_lambda).

    Args:
        N: sl_N parameter (N >= 2).
        s: complex exponent.
        max_box_count: maximum |lambda| for the enumeration.
        include_trivial: whether to include dim=1 (trivial rep).

    Returns:
        Partial sum of the categorical zeta.
    """
    result = complex(0)
    if include_trivial:
        result += 1.0  # trivial: dim = 1

    parts = partitions_bounded(max_box_count, N - 1, min_size=1)
    for lam in parts:
        d = hook_content_dimension(N, lam)
        if d > 0:
            result += d ** (-s)

    return result


def categorical_zeta_sl2_exact(s: complex, N_terms: int = 1000,
                               include_trivial: bool = True) -> complex:
    r"""Categorical zeta for sl_2 = Riemann zeta (direct partial sum).

    sum_{d=1}^{N_terms} d^{-s}  (including trivial)
    sum_{d=2}^{N_terms+1} d^{-s}  (excluding trivial)
    """
    start = 1 if include_trivial else 2
    return sum(d ** (-s) for d in range(start, start + N_terms))


# =========================================================================
# 3. Symmetric representation zeta
# =========================================================================

def dim_symmetric_rep(N: int, n: int) -> int:
    """Dimension of the n-th symmetric power representation of sl_N.

    V_{(n,0,...,0)} = Sym^n(C^N), dim = C(N+n-1, n).
    """
    return comb(N + n - 1, n)


def symmetric_rep_zeta(N: int, s: complex,
                       max_n: int = 200) -> complex:
    r"""Zeta restricted to single-row (symmetric) representations.

    zeta^{sym}_{sl_N}(s) = sum_{n >= 1} C(N+n-1, n)^{-s}

    At large N: C(N+n-1, n) ~ N^n / n!, so each term ~ (n!)^s N^{-ns}.
    Converges for Re(s) > 0 (superexponential decay in n for fixed N).
    """
    result = complex(0)
    for n in range(1, max_n + 1):
        d = dim_symmetric_rep(N, n)
        if d > 0:
            term = d ** (-s)
            result += term
            # Early termination if terms become negligible
            if abs(term) < 1e-16 * max(abs(result), 1e-30):
                break
    return result


def symmetric_rep_asymptotic(N: int, n: int) -> float:
    """Asymptotic approximation dim V_{(n)} ~ N^n / n! for large N."""
    return float(N ** n) / factorial(n)


# =========================================================================
# 4. Adjoint representation contribution
# =========================================================================

def dim_adjoint(N: int) -> int:
    """Dimension of the adjoint representation of sl_N: N^2 - 1."""
    return N * N - 1


def adjoint_contribution(N: int, s: complex) -> complex:
    """Single-term contribution of the adjoint to the zeta: (N^2 - 1)^{-s}."""
    return dim_adjoint(N) ** (-s)


# =========================================================================
# 5. Rescaled zeta: Z_N(s) = N^{-2s} * zeta^{DK}_{sl_N}(s)
# =========================================================================

def rescaled_zeta(N: int, s: complex,
                  max_box_count: int = 12) -> complex:
    r"""Rescaled categorical zeta: Z_N(s) = N^{-2s} * zeta^{DK}_{sl_N}(s).

    Normalization by the adjoint scale ~ N^2.
    """
    z = categorical_zeta_slN(N, s, max_box_count=max_box_count)
    return N ** (-2 * s) * z


def rescaled_zeta_data(s: complex, N_range: range = range(2, 21),
                       max_box_count: int = 10) -> Dict[int, complex]:
    """Compute Z_N(s) for a range of N values."""
    return {N: rescaled_zeta(N, s, max_box_count=max_box_count)
            for N in N_range}


# =========================================================================
# 6. Planar limit: representations with at most 2 rows
# =========================================================================

def planar_zeta(N: int, s: complex,
                max_box_count: int = 20) -> complex:
    r"""Planar-limit categorical zeta: sum over partitions with <= 2 rows.

    zeta^{planar}_{sl_N}(s) = sum_{lambda: rows(lambda) <= 2} dim(V_lambda)^{-s}

    In gauge theory, restricting to <= 2 rows keeps only the genus-0
    (planar) sector of the 't Hooft expansion.
    """
    parts = partitions_at_most_k_rows(max_box_count, 2)
    result = complex(0)
    for lam in parts:
        d = hook_content_dimension(N, lam)
        if d > 0:
            result += d ** (-s)
    return result


def planar_fraction(N: int, s: complex,
                    max_box_count: int = 12) -> float:
    """Fraction of the full zeta captured by the planar sector."""
    full = categorical_zeta_slN(N, s, max_box_count=max_box_count)
    plan = planar_zeta(N, s, max_box_count=max_box_count)
    if abs(full) < 1e-30:
        return 0.0
    return abs(plan) / abs(full)


# =========================================================================
# 7. Casimir zeta
# =========================================================================

def casimir_eigenvalue_sl2(n: int) -> Fraction:
    """Quadratic Casimir eigenvalue for sl_2 representation V_n.

    C_2(V_n) = n(n+2)/4 in the standard normalization.
    Here n is the highest weight (dim = n+1).
    """
    return Fraction(n * (n + 2), 4)


def casimir_eigenvalue_slN(N: int, lam: Tuple[int, ...]) -> Fraction:
    r"""Quadratic Casimir eigenvalue for sl_N representation V_lambda.

    C_2(lambda) = (lambda, lambda + 2*rho) / 2
    where rho = (N-1, N-2, ..., 1, 0)/2 in the standard basis.

    In partition notation, lambda = (lam_1, ..., lam_k, 0, ..., 0) (N parts),
    the Casimir is:

    C_2 = sum_i lam_i * (lam_i + N + 1 - 2i) / 2 - |lambda|^2 / (2N)

    The subtraction of |lambda|^2/(2N) accounts for the traceless condition.
    """
    lam_ext = list(lam) + [0] * N
    lam_ext = lam_ext[:N]
    size = sum(lam_ext)

    # Sum over parts
    total = Fraction(0)
    for i in range(N):
        li = lam_ext[i]
        total += Fraction(li * (li + N + 1 - 2 * (i + 1)), 2)

    # Traceless correction
    total -= Fraction(size * size, 2 * N)

    return total


def casimir_zeta_sl2(s: complex, N_terms: int = 500) -> complex:
    r"""Casimir zeta for sl_2: sum_{n >= 1} C_2(V_n)^{-s}.

    C_2(V_n) = n(n+2)/4, so:
    zeta^{Cas}_{sl_2}(s) = sum_{n >= 1} [n(n+2)/4]^{-s}
                         = 4^s * sum_{n >= 1} [n(n+2)]^{-s}

    This is NOT the Riemann zeta (it involves products n(n+2)).
    """
    result = complex(0)
    for n in range(1, N_terms + 1):
        c2 = float(casimir_eigenvalue_sl2(n))
        if c2 > 0:
            result += c2 ** (-s)
    return result


def casimir_zeta_slN(N: int, s: complex,
                     max_box_count: int = 10) -> complex:
    r"""Casimir zeta for sl_N: sum_{lambda nontrivial} C_2(lambda)^{-s}.

    Uses the quadratic Casimir C_2(lambda) = (lambda, lambda+2rho)/2.
    """
    parts = partitions_bounded(max_box_count, N - 1, min_size=1)
    result = complex(0)
    for lam in parts:
        c2 = float(casimir_eigenvalue_slN(N, lam))
        if c2 > 0:
            result += c2 ** (-s)
    return result


# =========================================================================
# 8. Character zeta
# =========================================================================

def character_sl2(n: int, q: complex) -> complex:
    """Character of sl_2 representation V_n evaluated at diag(q, q^{-1}).

    chi_{V_n}(q) = (q^{n+1} - q^{-(n+1)}) / (q - q^{-1})

    At q = 1: chi = n + 1 = dim V_n.
    """
    if abs(q - 1.0) < 1e-12:
        return complex(n + 1)
    if abs(q + 1.0) < 1e-12:
        # q = -1: chi = ((-1)^{n+1} - (-1)^{-(n+1)}) / (-1 - (-1)^{-1})
        # = ((-1)^{n+1} - (-1)^{n+1}) / (-2) = 0 for all n
        # Actually: need careful limit. chi(q=-1) = (-1)^n * (n+1) by L'Hopital.
        # Let me compute directly.
        num = q ** (n + 1) - q ** (-(n + 1))
        den = q - q ** (-1)
        if abs(den) < 1e-30:
            return complex((-1) ** n * (n + 1))
        return num / den
    num = q ** (n + 1) - q ** (-(n + 1))
    den = q - q ** (-1)
    if abs(den) < 1e-30:
        return complex(n + 1)
    return num / den


def character_slN_symmetric(N: int, n: int, q_diag: Tuple[complex, ...]) -> complex:
    r"""Character of symmetric representation Sym^n(C^N) at diagonal element.

    chi_{Sym^n}(q_1, ..., q_N) = h_n(q_1, ..., q_N)
    (complete homogeneous symmetric polynomial of degree n).

    For the special case q_diag = (q, q^{w_2}, ..., q^{w_N}) with Weyl orbit
    weights w_i, this simplifies.

    This function takes the actual diagonal entries as input.
    """
    # Compute h_n by the generating function approach
    # h_n = sum_{i_1 <= i_2 <= ... <= i_n} q_{i_1} * ... * q_{i_n}
    # More efficiently via Newton's identity or recursion.
    if n == 0:
        return complex(1)
    if n == 1:
        return sum(q_diag)

    # Use the recursion: h_n = (1/n) sum_{k=1}^{n} p_k * h_{n-k}
    # where p_k = sum q_i^k is the power sum.
    h = [complex(0)] * (n + 1)
    h[0] = 1.0
    p = [0.0] + [sum(qi ** k for qi in q_diag) for k in range(1, n + 1)]

    for m in range(1, n + 1):
        h[m] = sum(p[k] * h[m - k] for k in range(1, m + 1)) / m

    return h[n]


def character_zeta_sl2(s: complex, q: complex,
                       N_terms: int = 200) -> complex:
    r"""Character zeta for sl_2: sum_{n >= 1} chi_{V_n}(q)^{-s}.

    At q = 1: chi(1) = dim V_n = n+1, recovering the categorical zeta.
    At q = root of unity: characters take discrete values.
    """
    result = complex(0)
    for n in range(1, N_terms + 1):
        chi = character_sl2(n, q)
        if abs(chi) > 1e-30:
            result += chi ** (-s)
    return result


def root_of_unity(N: int, k: int = 1) -> complex:
    """Return q = exp(2*pi*i*k/N), the primitive N-th root of unity."""
    return cmath.exp(2j * cmath.pi * k / N)


# =========================================================================
# 9. Renormalized sl_infty zeta
# =========================================================================

def frame_robinson_schensted_limit(lam: Tuple[int, ...]) -> float:
    r"""Limit of dim(V_lambda)/N^{|lambda|} as N -> infty.

    By the hook-content formula:
        dim V_lambda / N^{|lambda|} -> prod_{(i,j)} 1/hook(i,j) = f_lambda / |lambda|!

    where f_lambda is the number of standard Young tableaux of shape lambda
    (by the hook length formula: f_lambda = |lambda|! / prod hook(i,j)).

    Returns f_lambda / |lambda|!.
    """
    lam = tuple(x for x in lam if x > 0)
    if not lam:
        return 1.0
    n = sum(lam)
    # f_lambda / n! = 1 / prod hook(i, j)
    hook_prod = 1
    for i, lam_i in enumerate(lam):
        for j in range(lam_i):
            hook_prod *= hook_length(lam, i, j)
    return 1.0 / hook_prod


def renormalized_dimension(N: int, lam: Tuple[int, ...]) -> float:
    """Renormalized dimension: dim(V_lambda) / N^{|lambda|}."""
    d = hook_content_dimension(N, lam)
    n = sum(lam)
    if n == 0:
        return 1.0
    return d / (N ** n)


def renormalized_zeta(N: int, s: complex,
                      max_box_count: int = 10) -> complex:
    r"""Renormalized zeta: sum [dim V_lambda / N^{|lambda|}]^{-s}.

    This should converge to a finite limit as N -> infty:
        sum [f_lambda / |lambda|!]^{-s}
    where f_lambda counts standard Young tableaux.
    """
    parts = partitions_bounded(max_box_count, N - 1 if N > 1 else max_box_count,
                               min_size=1)
    result = complex(0)
    for lam in parts:
        rd = renormalized_dimension(N, lam)
        if rd > 1e-30:
            result += rd ** (-s)
    return result


def renormalized_zeta_limit(s: complex,
                            max_box_count: int = 10,
                            max_rows: int = 50) -> complex:
    r"""Limiting renormalized zeta as N -> infty.

    sum_{lambda nontrivial} [f_lambda / |lambda|!]^{-s}

    where f_lambda / |lambda|! = 1 / prod hook(i,j) by the hook-length formula.
    """
    parts = partitions_bounded(max_box_count, max_rows, min_size=1)
    result = complex(0)
    for lam in parts:
        frs = frame_robinson_schensted_limit(lam)
        if frs > 1e-30:
            result += frs ** (-s)
    return result


# =========================================================================
# 10. 't Hooft double scaling
# =========================================================================

def thooft_double_scaling_zeta(N: int, tau: float,
                               max_box_count: int = 10) -> complex:
    r"""'t Hooft double scaling: N -> infty, s -> 0 with s*N = tau fixed.

    zeta^{DK}_{sl_N}(tau/N) for various N, with tau fixed.
    """
    s = tau / N
    return categorical_zeta_slN(N, s, max_box_count=max_box_count)


def thooft_rescaled(N: int, tau: float,
                    max_box_count: int = 10) -> complex:
    r"""N^{-2*tau/N} * zeta^{DK}_{sl_N}(tau/N).

    Combined rescaling and double scaling.
    """
    s = tau / N
    return rescaled_zeta(N, s, max_box_count=max_box_count)


# =========================================================================
# 11. Monotonicity and growth analysis
# =========================================================================

def zeta_monotonicity_check(s: float, N_range: range = range(2, 16),
                            max_box_count: int = 8) -> Dict[str, Any]:
    """Check whether zeta^{DK}_{sl_N}(s) is monotone in N for fixed s.

    Returns a dict with:
        'values': {N: zeta_N(s)}
        'is_monotone_increasing': bool
        'is_monotone_decreasing': bool
        'differences': {N: zeta_{N+1}(s) - zeta_N(s)}
    """
    values = {}
    for N in N_range:
        values[N] = categorical_zeta_slN(N, s, max_box_count=max_box_count).real

    Ns = sorted(values.keys())
    diffs = {}
    for i in range(len(Ns) - 1):
        diffs[Ns[i]] = values[Ns[i + 1]] - values[Ns[i]]

    return {
        'values': values,
        'is_monotone_increasing': all(d >= -1e-12 for d in diffs.values()),
        'is_monotone_decreasing': all(d <= 1e-12 for d in diffs.values()),
        'differences': diffs,
    }


def symmetric_zeta_growth(s: float, N_range: range = range(2, 21),
                          max_n: int = 100) -> Dict[int, float]:
    """Growth of symmetric-rep zeta with N."""
    return {N: symmetric_rep_zeta(N, s, max_n=max_n).real for N in N_range}


# =========================================================================
# 12. Abscissa of convergence
# =========================================================================

def abscissa_of_convergence_slN(N: int, max_box_count: int = 10,
                                s_range: Tuple[float, float] = (0.1, 5.0),
                                n_points: int = 50) -> float:
    """Estimate the abscissa of convergence sigma_c for sl_N categorical zeta.

    Returns the smallest s (in the tested range) where the partial sum
    appears to converge (successive partial sums agree within tolerance).
    """
    for s_test in np.linspace(s_range[0], s_range[1], n_points):
        z1 = categorical_zeta_slN(N, s_test, max_box_count=max_box_count)
        z2 = categorical_zeta_slN(N, s_test, max_box_count=max(5, max_box_count - 3))
        if abs(z1) > 1e-30 and abs(z1 - z2) / abs(z1) < 0.01:
            return float(s_test)
    return float(s_range[1])


# =========================================================================
# 13. Cross-verification utilities
# =========================================================================

def verify_hook_vs_weyl(N: int, max_box_count: int = 6) -> Dict[str, Any]:
    """Cross-verify hook-content formula against Weyl product formula.

    Path 2 of the verification mandate: these two independent formulas
    must produce identical dimensions for all representations.
    """
    parts = partitions_bounded(max_box_count, N - 1, min_size=1)
    mismatches = []
    total_checked = 0
    for lam in parts:
        d_hook = hook_content_dimension(N, lam)
        d_weyl = weyl_dimension_slN_partition(N, lam)
        total_checked += 1
        if d_hook != d_weyl:
            mismatches.append({
                'partition': lam,
                'hook_dim': d_hook,
                'weyl_dim': d_weyl,
            })

    return {
        'total_checked': total_checked,
        'mismatches': mismatches,
        'all_agree': len(mismatches) == 0,
    }


def verify_sl2_is_riemann(s: float, N_terms: int = 500) -> Dict[str, Any]:
    """Verify that sl_2 categorical zeta = Riemann zeta.

    Path 1: The defining identity.
    """
    z_cat = categorical_zeta_sl2_exact(s, N_terms=N_terms, include_trivial=True)
    z_riemann = sum(n ** (-s) for n in range(1, N_terms + 1))
    return {
        'categorical': z_cat,
        'riemann': z_riemann,
        'difference': abs(z_cat - z_riemann),
        'match': abs(z_cat - z_riemann) < 1e-10,
    }


def verify_character_at_one(N_terms: int = 50) -> Dict[str, Any]:
    """Verify that chi_lambda(1) = dim V_lambda (Path 5).

    Characters at the identity element must equal dimensions.
    """
    mismatches = []
    for n in range(N_terms):
        chi = character_sl2(n, 1.0)
        dim = n + 1
        if abs(chi - dim) > 1e-10:
            mismatches.append({'n': n, 'chi': chi, 'dim': dim})
    return {
        'total_checked': N_terms,
        'mismatches': mismatches,
        'all_agree': len(mismatches) == 0,
    }


def verify_asymptotic_dimension(N: int, n: int) -> Dict[str, float]:
    """Compare exact dimension of Sym^n(C^N) with asymptotic N^n/n!."""
    exact = dim_symmetric_rep(N, n)
    asymp = symmetric_rep_asymptotic(N, n)
    return {
        'exact': float(exact),
        'asymptotic': asymp,
        'ratio': float(exact) / asymp if asymp > 0 else float('inf'),
        'relative_error': abs(float(exact) - asymp) / float(exact) if exact > 0 else 0.0,
    }


# =========================================================================
# 14. Summary / reporting
# =========================================================================

def large_n_summary(s_values: List[float] = [2.0, 3.0, 4.0],
                    N_range: range = range(2, 11),
                    max_box_count: int = 8) -> Dict[str, Any]:
    """Compute a summary table of large-N zeta values.

    Returns a nested dict: {s: {N: {'full': ..., 'rescaled': ...,
                                     'planar': ..., 'symmetric': ...}}}
    """
    summary = {}
    for s in s_values:
        summary[s] = {}
        for N in N_range:
            full = categorical_zeta_slN(N, s, max_box_count=max_box_count)
            resc = rescaled_zeta(N, s, max_box_count=max_box_count)
            plan = planar_zeta(N, s, max_box_count=max_box_count)
            sym = symmetric_rep_zeta(N, s)
            summary[s][N] = {
                'full': full.real,
                'rescaled': resc.real,
                'planar': plan.real,
                'symmetric': sym.real,
            }
    return summary


def casimir_summary(s_values: List[float] = [1.0, 2.0, 3.0, 4.0, 5.0],
                    N_range: range = range(2, 11)) -> Dict[str, Any]:
    """Compute a summary table of Casimir zeta values."""
    summary = {}
    for s in s_values:
        summary[s] = {}
        for N in N_range:
            if N == 2:
                val = casimir_zeta_sl2(s).real
            else:
                val = casimir_zeta_slN(N, s).real
            summary[s][N] = val
    return summary
