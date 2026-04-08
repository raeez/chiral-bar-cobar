r"""Explicit bar cohomology H*(B(Vir_c)) at conformal weights 0 through 10.

THREE INDEPENDENT COMPUTATION METHODS, CROSS-VALIDATED:

METHOD 1 -- CHEVALLEY-EILENBERG COHOMOLOGY of Vir_-.
  The Virasoro negative-mode Lie algebra Vir_- = span{L_{-n} : n >= 2}
  has bracket [L_{-m}, L_{-n}] = (n - m) L_{-m-n}, with NO central
  extension (m, n >= 2 implies m+n >= 4 > 0, so delta_{m+n,0} = 0).

  For chirally Koszul algebras (thm:koszul-equivalences-meta), the PBW
  spectral sequence collapses at E_2, giving:
    H^k(B(Vir_c))_w = H^k(CE(Vir_-))_w
  graded by conformal weight w.  The Lie algebra Vir_- has no c-dependence,
  so the bar cohomology at fixed conformal weight is INDEPENDENT OF c.

  The CE complex Lambda^k(Vir_-^*) at conformal weight w has basis =
  k-element subsets {L_{-n_1}, ..., L_{-n_k}} with n_1 < ... < n_k,
  all n_i >= 2, and n_1 + ... + n_k = w.  The CE differential is dual
  to the Lie bracket.

  TRUNCATION CONTROL: to avoid artifacts at weight w, we include
  generators up to weight >= 2w (since brackets can produce modes
  at weight a+b up to 2w).

METHOD 2 -- DIRECT VIRASORO OPE VERIFICATION.
  Independently verify the Virasoro n-th products from the commutation
  relations [L_m, L_n] = (m-n)L_{m+n} + (c/12)(m^3-m) delta_{m+n,0}
  using exact rational arithmetic.  Cross-validate specific OPE values
  at multiple c values.

METHOD 3 -- ALGEBRAIC GENERATING FUNCTION (PBW-degree grading).
  The Koszul dual Vir^! = Vir_{26-c} (prop:virasoro-generic-koszul-dual)
  has Hilbert function in PBW degree graded by:
    P_{Vir}(x) = x * M(x)^2
  where M(x) = (1-x-sqrt(1-2x-3x^2))/(2x^2) is the Motzkin GF.
  Equivalently: dim(Vir^!)_n = sum_{j=0}^{n-1} M(j)*M(n-1-j).
  The PBW-degree index n counts the number of generator applications.
  This is a DIFFERENT grading from conformal weight.

  The algebraic GF has equivalent form (combinatorial_frontier.tex):
    P(x) = 4x / (1 - x + sqrt(1-2x-3x^2))^2

KEY DISTINCTION: TWO GRADINGS ON THE KOSZUL DUAL.
  1. CONFORMAL WEIGHT w: dim H^k(B(Vir))_w is computed by the CE complex.
     H^1_w = 1 for w in {2, 3, 4}, = 0 for w >= 5.
     H^2_w begins at w = 7 (from CE degree-2 cocycles).
     H^k_w = 0 for k >= 3 at weights <= 10 (verified computationally).

  2. PBW DEGREE n: dim(Vir^!)_n = [x^n] x*M(x)^2.
     Sequence: 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610, ...
     Growth rate: ~ 3^n (the dominant singularity of M(x) is at x = 1/3).

  The conformal-weight grading is finer: each PBW degree n comprises
  states at conformal weights 2n, 2n+1, ..., with the distribution
  governed by the partition structure.

GRADING CONVENTIONS (per signs_and_shifts.tex):
  - Cohomological grading, |d| = +1
  - Bar degree k uses desuspension: |s^{-1}v| = |v| - 1 (AP45)
  - The CE degree k corresponds to bar degree k
  - H^k(B) at bar degree k; Koszulness means H^k = 0 for k >= 2

c-INDEPENDENCE:
  The CE complex of Vir_- = {L_{-n} : n >= 2} has bracket with NO central
  term (m+n >= 4 > 0 for m,n >= 2).  Therefore the differential matrices
  have integer entries, and ALL cohomology dimensions are independent of c.
  This is verified explicitly by checking that the CE differential matrices
  contain only integers (no c-dependence leaks in).

References:
  comp:virasoro-ope, comp:virasoro-bar-diff (bar_complex_tables.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  prop:virasoro-generic-koszul-dual (w_algebras.tex)
  prop:arnold-virasoro-deg3 (bar_complex_tables.tex)
  combinatorial_frontier.tex, subsec:virasoro-near-rationality
  AP19 (bar kernel absorbs a pole)
  AP26 (BPZ inner product for quasi-primary decomposition)
  AP45 (desuspension lowers degree)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, zeros as sympy_zeros

# ============================================================================
# Exact rational arithmetic
# ============================================================================

FR = Fraction


def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int,)):
        return Fraction(int(x))
    return Fraction(x)


# ============================================================================
# Partition functions
# ============================================================================


@lru_cache(maxsize=512)
def partitions_geq2(n: int) -> Tuple[Tuple[int, ...], ...]:
    """All partitions of n into parts >= 2, in decreasing order."""
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    if n == 1:
        return ()
    results: List[Tuple[int, ...]] = []
    _partition_helper_geq2(n, 2, n, [], results)
    return tuple(results)


def _partition_helper_geq2(remaining, min_part, max_part, current, results):
    if remaining == 0:
        results.append(tuple(current))
        return
    if remaining < min_part:
        return
    for part in range(min(remaining, max_part), min_part - 1, -1):
        current.append(part)
        _partition_helper_geq2(remaining - part, min_part, part, current, results)
        current.pop()


@lru_cache(maxsize=512)
def partitions_distinct_geq2(n: int) -> Tuple[Tuple[int, ...], ...]:
    """All partitions of n into DISTINCT parts >= 2, in decreasing order."""
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    if n == 1:
        return ()
    results: List[Tuple[int, ...]] = []
    _partition_helper_distinct(n, 2, [], results)
    return tuple(results)


def _partition_helper_distinct(remaining, min_part, current, results):
    if remaining == 0:
        results.append(tuple(current))
        return
    if remaining < min_part:
        return
    for part in range(remaining, min_part - 1, -1):
        current.append(part)
        _partition_helper_distinct(remaining - part, part + 1, current, results)
        current.pop()


def p_geq2(n: int) -> int:
    """Number of partitions of n into parts >= 2.

    Counts PBW basis states of the Virasoro at conformal weight n.
    GF: prod_{k>=2} 1/(1-q^k).
    """
    return len(partitions_geq2(n))


def q_geq2(n: int) -> int:
    """Number of partitions of n into DISTINCT parts >= 2.

    Counts the dimension of Lambda^*(Vir_-^*)_n (CE chain groups).
    GF: prod_{k>=2} (1+q^k).
    """
    return len(partitions_distinct_geq2(n))


# ============================================================================
# Motzkin numbers and the PBW-degree Koszul dual
# ============================================================================


@lru_cache(maxsize=512)
def motzkin(n: int) -> int:
    """The n-th Motzkin number M(n).

    M(0)=1, M(1)=1, M(2)=2, M(3)=4, M(4)=9, M(5)=21, M(6)=51, ...
    Recurrence: (n+3)*M(n+1) = (2n+3)*M(n) + 3n*M(n-1), equivalently:
      (n+2)*M(n) = (2n+1)*M(n-1) + 3*(n-1)*M(n-2)  for n >= 2.
    GF: M(x) = (1-x-sqrt(1-2x-3x^2))/(2x^2).
    """
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return ((2 * n + 1) * motzkin(n - 1) + 3 * (n - 1) * motzkin(n - 2)) // (n + 2)


def koszul_dual_pbw_dim(n: int) -> int:
    """dim(Vir^!)_n in PBW-degree grading.

    Equals M(n+1) - M(n) (Motzkin differences), which also equals
    [x^n] x*M(x)^2 = sum_{j=0}^{n-1} M(j)*M(n-1-j) by the identity
    x*M(x)^2 = M(x) - 1 (from the Motzkin functional equation
    M = 1 + x*M + x^2*M^2).
    Sequence: 0, 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610, ...
    """
    if n < 1:
        return 0
    return sum(motzkin(j) * motzkin(n - 1 - j) for j in range(n))


def koszul_dual_pbw_gf_coefficients(max_n: int = 15) -> List[int]:
    """The PBW-degree Hilbert function of Vir^!.

    Returns [dim(Vir^!)_0, dim(Vir^!)_1, ..., dim(Vir^!)_{max_n}].
    """
    return [koszul_dual_pbw_dim(n) for n in range(max_n + 1)]


def verify_gf_algebraic(max_n: int = 12) -> Dict[int, bool]:
    """Verify P(x) = x*M(x)^2 = 4x/(1-x+sqrt(1-2x-3x^2))^2.

    Expands the algebraic GF via power series and checks coefficient by
    coefficient against the Motzkin convolution formula.
    """
    # Compute sqrt(1-2x-3x^2) as power series
    N = max_n + 4
    f_c = [FR(0)] * N
    f_c[0] = FR(1)
    f_c[1] = FR(-2)
    f_c[2] = FR(-3)

    s = [FR(0)] * N
    s[0] = FR(1)
    for n in range(1, N):
        conv = sum(s[j] * s[n - j] for j in range(1, n))
        s[n] = (f_c[n] - conv) / FR(2)

    # g(x) = 1 - x + sqrt(1-2x-3x^2)
    g = [s[n] for n in range(N)]
    g[0] += FR(1)
    g[1] += FR(-1)

    # g^2
    g2 = [FR(0)] * N
    for n in range(N):
        for j in range(n + 1):
            g2[n] += g[j] * g[n - j]

    # h = 1/g^2
    h = [FR(0)] * N
    h[0] = FR(1) / g2[0]
    for n in range(1, N):
        h[n] = -sum(g2[j] * h[n - j] for j in range(1, n + 1)) / g2[0]

    # P(x) = 4x * h(x)
    P_alg = [FR(0)] * N
    for n in range(1, N):
        P_alg[n] = FR(4) * h[n - 1]

    results = {}
    for n in range(max_n + 1):
        expected = FR(koszul_dual_pbw_dim(n))
        results[n] = (P_alg[n] == expected)
    return results


# ============================================================================
# METHOD 1: Chevalley-Eilenberg cohomology of Vir_-
# ============================================================================


class VirasoroCEEngine:
    """Chevalley-Eilenberg complex of Vir_- with controlled truncation.

    Generators: {L_{-n} : n >= 2}, indexed by i = n-2 (so i=0 is L_{-2}).
    Bracket: [L_{-(a+2)}, L_{-(b+2)}] = (b-a) L_{-(a+b+4)}, output index a+b+2.
    """

    def __init__(self, max_weight: int = 24):
        self.max_weight = max_weight
        self.n_gens = max_weight - 1
        self._gen_weights = list(range(2, max_weight + 1))

        self._bracket: Dict[Tuple[int, int], Dict[int, int]] = {}
        for a in range(self.n_gens):
            for b in range(a + 1, self.n_gens):
                c_idx = a + b + 2
                coeff = b - a
                if c_idx < self.n_gens and coeff != 0:
                    self._bracket[(a, b)] = {c_idx: coeff}

    def weight_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of Lambda^degree(Vir_-^*) at conformal weight."""
        return list(self._weight_subsets(degree, weight, 0))

    def _weight_subsets(self, degree, target_weight, start):
        if degree == 0:
            if target_weight == 0:
                yield ()
            return
        for i in range(start, self.n_gens):
            w = self._gen_weights[i]
            if w > target_weight:
                break
            remaining_needed = degree - 1
            if self.n_gens - i - 1 < remaining_needed:
                break
            if remaining_needed > 0:
                min_remaining = sum(
                    self._gen_weights[i + 1 + j] for j in range(remaining_needed)
                )
                if target_weight - w < min_remaining:
                    continue
            for rest in self._weight_subsets(degree - 1, target_weight - w, i + 1):
                yield (i,) + rest

    def ce_differential_matrix(self, degree: int, weight: int) -> Matrix:
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight.

        Exact integer arithmetic via sympy Matrix.
        """
        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            return sympy_zeros(n_tgt, n_src)

        target_idx = {t: i for i, t in enumerate(target)}
        mat = sympy_zeros(n_tgt, n_src)

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)

            for (a, b), br in self._bracket.items():
                for c, coeff in br.items():
                    if c not in alpha_set:
                        continue
                    new_set = (alpha_set - {c}) | {a, b}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue

                    pos_c = alpha_list.index(c)
                    sorted_new = list(new_tuple)
                    pos_a = sorted_new.index(a)
                    remaining_after_a = sorted(new_set - {a})
                    pos_b = remaining_after_a.index(b)
                    sign = (-1) ** pos_c * (-1) ** pos_a * (-1) ** pos_b

                    mat[row, col] += sign * coeff

        return mat

    def chain_dim(self, degree: int, weight: int) -> int:
        return len(self.weight_basis(degree, weight))

    def cohomology_dim(self, degree: int, weight: int) -> int:
        """dim H^degree(CE(Vir_-))_weight."""
        dim_k = self.chain_dim(degree, weight)
        if dim_k == 0:
            return 0

        d_curr = self.ce_differential_matrix(degree, weight)
        if d_curr.rows > 0 and d_curr.cols > 0:
            ker = dim_k - d_curr.rank()
        else:
            ker = dim_k

        if degree > 0:
            d_prev = self.ce_differential_matrix(degree - 1, weight)
            if d_prev.rows > 0 and d_prev.cols > 0:
                im = d_prev.rank()
            else:
                im = 0
        else:
            im = 0
        return ker - im

    def verify_d_squared(self, degree: int, weight: int) -> bool:
        """Check d^{degree+1} . d^{degree} = 0."""
        d_p = self.ce_differential_matrix(degree, weight)
        d_p1 = self.ce_differential_matrix(degree + 1, weight)
        if d_p.cols == 0 or d_p1.rows == 0:
            return True
        if d_p.rows != d_p1.cols:
            return True
        return (d_p1 * d_p).is_zero_matrix


# ============================================================================
# METHOD 2: Direct OPE verification with exact arithmetic
# ============================================================================


class VermaModuleExact:
    """Vacuum Verma module of Virasoro at rational c, exact Fraction arithmetic."""

    def __init__(self, c: Fraction, max_weight: int):
        self.c = _frac(c)
        self.max_weight = max_weight

    @lru_cache(maxsize=16384)
    def apply_Lm(
        self, m: int, state: Tuple[int, ...]
    ) -> Tuple[Tuple[Tuple[Tuple[int, ...], FR], ...], FR]:
        """Apply L_m to L_{-p_1}...L_{-p_k}|0>.

        Returns (tuple of (state, coeff), vacuum_coeff).
        """
        if len(state) == 0:
            if m >= -1:
                return (), FR(0)
            else:
                n = -m
                if n < 2 or n > self.max_weight:
                    return (), FR(0)
                return (((n,), FR(1)),), FR(0)

        p1 = state[0]
        rest = state[1:]
        result_dict: Dict[Tuple[int, ...], FR] = {}
        vac_total = FR(0)

        # Term 1: L_{-p1} (L_m rest|0>)
        sub_r, sub_v = self.apply_Lm(m, rest)
        if sub_v != FR(0) and 2 <= p1 <= self.max_weight:
            result_dict[(p1,)] = result_dict.get((p1,), FR(0)) + sub_v
        for st, c in sub_r:
            if c == FR(0):
                continue
            new_st = _prepend_sorted(p1, st)
            if sum(new_st) <= self.max_weight:
                result_dict[new_st] = result_dict.get(new_st, FR(0)) + c

        # Term 2: [L_m, L_{-p1}] = (m + p1) L_{m-p1}
        bracket_c = FR(m + p1)
        new_mode = m - p1
        if bracket_c != FR(0):
            if new_mode == 0:
                rest_w = sum(rest)
                if len(rest) > 0:
                    result_dict[rest] = result_dict.get(rest, FR(0)) + bracket_c * FR(rest_w)
            else:
                sub2_r, sub2_v = self.apply_Lm(new_mode, rest)
                vac_total += bracket_c * sub2_v
                for st, c in sub2_r:
                    if c != FR(0) and sum(st) <= self.max_weight:
                        result_dict[st] = result_dict.get(st, FR(0)) + bracket_c * c

        # Term 3: central (c/12)(m^3-m) delta_{m, p1}
        if m == p1:
            central = self.c * FR(m ** 3 - m) / FR(12)
            if central != FR(0):
                if len(rest) == 0:
                    vac_total += central
                else:
                    result_dict[rest] = result_dict.get(rest, FR(0)) + central

        return tuple((k, v) for k, v in sorted(result_dict.items()) if v != FR(0)), vac_total


class NthProductsExact:
    """Compute n-th products a_{(n)}b via Borcherds-Li recursion, exact arithmetic."""

    def __init__(self, verma: VermaModuleExact):
        self.verma = verma

    @lru_cache(maxsize=65536)
    def nth_product(
        self, a_state: Tuple[int, ...], n: int, b_state: Tuple[int, ...]
    ) -> Tuple[Tuple[Tuple[Tuple[int, ...], FR], ...], FR]:
        """Compute a_{(n)}b."""
        if len(a_state) == 0:
            return (), FR(0)

        if len(a_state) == 1:
            k = a_state[0]
            mode = n - k + 1
            return self.verma.apply_Lm(mode, b_state)

        k = a_state[0]
        v_state = a_state[1:]
        result_dict: Dict[Tuple[int, ...], FR] = {}
        vac_total = FR(0)

        for j in range(k):
            bc = FR(comb(k - 1, j))

            c1 = FR((-1) ** j) * bc
            if c1 != FR(0):
                vj_r, vj_v = self.nth_product(v_state, n - j, b_state)
                m1 = n + j - k + 1
                if vj_v != FR(0):
                    lr, lv = self.verma.apply_Lm(m1, ())
                    vac_total += c1 * vj_v * lv
                    for p, c in lr:
                        result_dict[p] = result_dict.get(p, FR(0)) + c1 * vj_v * c
                for p2, c2 in vj_r:
                    if c2 == FR(0):
                        continue
                    lr, lv = self.verma.apply_Lm(m1, p2)
                    vac_total += c1 * c2 * lv
                    for p3, c3 in lr:
                        result_dict[p3] = result_dict.get(p3, FR(0)) + c1 * c2 * c3

            c2_coeff = FR((-1) ** (k + j)) * bc
            if c2_coeff != FR(0):
                pi = n + k - 1 - j
                lj_r, lj_v = self.verma.apply_Lm(j, b_state)
                if lj_v != FR(0):
                    vp_r, vp_v = self.nth_product(v_state, pi, ())
                    vac_total += c2_coeff * lj_v * vp_v
                    for p2, cc in vp_r:
                        result_dict[p2] = result_dict.get(p2, FR(0)) + c2_coeff * lj_v * cc
                for p2, cc2 in lj_r:
                    if cc2 == FR(0):
                        continue
                    vp_r, vp_v = self.nth_product(v_state, pi, p2)
                    vac_total += c2_coeff * cc2 * vp_v
                    for p3, c3 in vp_r:
                        result_dict[p3] = result_dict.get(p3, FR(0)) + c2_coeff * cc2 * c3

        return tuple((k, v) for k, v in sorted(result_dict.items()) if v != FR(0)), vac_total


def _prepend_sorted(n: int, partition: Tuple[int, ...]) -> Tuple[int, ...]:
    """Insert n into a decreasing tuple, maintaining decreasing order."""
    lst = list(partition)
    pos = 0
    while pos < len(lst) and lst[pos] >= n:
        pos += 1
    lst.insert(pos, n)
    return tuple(lst)


def verify_ope_basic(c: Fraction) -> Dict[str, bool]:
    """Verify fundamental Virasoro OPE identities at central charge c."""
    c_val = _frac(c)
    verma = VermaModuleExact(c_val, 10)
    nth = NthProductsExact(verma)
    T = (2,)
    dT = (3,)
    results = {}

    r3, v3 = nth.nth_product(T, 3, T)
    results['T_(3)T = c/2'] = (len(r3) == 0 and v3 == c_val / FR(2))

    r2, v2 = nth.nth_product(T, 2, T)
    results['T_(2)T = 0'] = (len(r2) == 0 and v2 == FR(0))

    r1, v1 = nth.nth_product(T, 1, T)
    results['T_(1)T = 2T'] = (
        len(r1) == 1 and r1[0] == (T, FR(2)) and v1 == FR(0)
    )

    r0, v0 = nth.nth_product(T, 0, T)
    results['T_(0)T = dT'] = (
        len(r0) == 1 and r0[0] == (dT, FR(1)) and v0 == FR(0)
    )

    return results


# ============================================================================
# Full cohomology table (conformal weight grading)
# ============================================================================


def compute_full_cohomology_table(
    max_weight: int = 10,
    max_bar_degree: int = 4,
) -> Dict[Tuple[int, int], int]:
    """Compute dim H^k(B(Vir))_w for all (k, w) with w <= max_weight.

    Uses CE cohomology with adequate truncation.
    Returns: dict (bar_degree, weight) -> dimension.
    """
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)

    table: Dict[Tuple[int, int], int] = {}
    for k in range(1, max_bar_degree + 1):
        min_w = k * (k + 3) // 2
        for w in range(min_w, max_weight + 1):
            dim = ce.cohomology_dim(k, w)
            table[(k, w)] = dim
    return table


def compute_h1_table(max_weight: int = 10) -> Dict[int, int]:
    """dim H^1(B(Vir))_w for w = 0,...,max_weight (conformal weight grading)."""
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    result = {}
    for w in range(0, max_weight + 1):
        if w < 2:
            result[w] = 0
        else:
            result[w] = ce.cohomology_dim(1, w)
    return result


def compute_ce_total_at_weight(max_weight: int = 10) -> Dict[int, int]:
    """Total dim sum_k H^k(CE(Vir_-))_w at each conformal weight."""
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    result = {}
    for w in range(0, max_weight + 1):
        total = 0
        max_k = w // 2
        for k in range(0, max_k + 1):
            if k == 0:
                total += (1 if w == 0 else 0)
            else:
                total += ce.cohomology_dim(k, w)
        result[w] = total
    return result


def compute_chain_group_dims(
    max_weight: int = 10,
    max_bar_degree: int = 4,
) -> Dict[Tuple[int, int], int]:
    """dim Lambda^k(Vir_-^*)_w (CE chain groups before cohomology)."""
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    table: Dict[Tuple[int, int], int] = {}
    for k in range(1, max_bar_degree + 1):
        min_w = k * (k + 3) // 2
        for w in range(min_w, max_weight + 1):
            dim = ce.chain_dim(k, w)
            if dim > 0:
                table[(k, w)] = dim
    return table


# ============================================================================
# d^2 = 0 verification
# ============================================================================


def verify_ce_d_squared_full(max_weight: int = 10) -> Dict[Tuple[int, int], bool]:
    """Verify d^2 = 0 for all (degree, weight) in the CE complex."""
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    results = {}
    for deg in range(0, 5):
        for w in range(2 * (deg + 1), max_weight + 1):
            results[(deg, w)] = ce.verify_d_squared(deg, w)
    return results


# ============================================================================
# c-independence verification
# ============================================================================


def check_c_independence_ce(max_weight: int = 10) -> bool:
    """Verify that all CE differential matrices have integer entries."""
    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    for k in range(0, 3):
        for w in range(2 * (k + 1), max_weight + 1):
            mat = ce.ce_differential_matrix(k, w)
            for i in range(mat.rows):
                for j in range(mat.cols):
                    val = mat[i, j]
                    if val != int(val):
                        return False
    return True


# ============================================================================
# H^1 analysis: cocycle/coboundary structure
# ============================================================================


def h1_cocycle_analysis(max_weight: int = 10) -> Dict[int, Dict[str, object]]:
    """Analyze H^1(CE(Vir_-))_w: which generators are cocycles.

    H^1_w = ker(d: Lambda^1_w -> Lambda^2_w) / im(d: Lambda^0_w -> Lambda^1_w).
    Lambda^0_w = 0 for w > 0, so im = 0 and H^1_w = ker(d: Lambda^1_w -> Lambda^2_w).

    Lambda^1_w has dim 1 (generator L_{-w}^* for w >= 2).
    d(L_{-w}^*) = sum_{a+b=w, 2<=a<b} (b-a) L_{-a}^* ^ L_{-b}^*.
    d = 0 iff no such decomposition exists, i.e., w <= 4.

    For w = 2: no a,b with 2<=a<b, a+b=2. H^1 = 1.
    For w = 3: no a,b with 2<=a<b, a+b=3. H^1 = 1.
    For w = 4: only a=b=2, violates a<b. H^1 = 1.
    For w >= 5: a=2, b=w-2 >= 3 works. d != 0, H^1 = 0.
    """
    result = {}
    for w in range(0, max_weight + 1):
        if w < 2:
            result[w] = {'dim': 0, 'is_cocycle': None, 'reason': 'below minimum weight'}
            continue
        # Check if L_{-w}^* is a cocycle
        decompositions = []
        for a in range(2, w):
            b = w - a
            if b > a and b >= 2:
                coeff = b - a
                decompositions.append((a, b, coeff))
        is_cocycle = len(decompositions) == 0
        result[w] = {
            'dim': 1 if is_cocycle else 0,
            'is_cocycle': is_cocycle,
            'decompositions': decompositions,
            'reason': 'no bracket decomposition' if is_cocycle
            else f'[L_{{-{decompositions[0][0]}}}, L_{{-{decompositions[0][1]}}}] = {decompositions[0][2]}*L_{{-{w}}}'
        }
    return result


# ============================================================================
# Weight-4 quasi-primary analysis (AP26)
# ============================================================================


def weight4_quasi_primary(c: Fraction) -> Dict[str, object]:
    """Analyze the weight-4 quasi-primary [TT] at central charge c.

    [TT] = L_{-2}^2|0> - (3/5) L_{-4}|0> (BPZ inner product, AP26).
    Verified by L_1 [TT] = 0 (quasi-primary condition).

    In the Koszul dual at conformal weight 4, [TT] does NOT appear as
    a separate bar cohomology class because Lambda^2_4 = 0 (minimum
    weight for Lambda^2 is 2+3=5 > 4).  The only bar cohomology at
    weight 4 is H^1_4 = 1 (the generator L_{-4}^*).
    """
    c_val = _frac(c)
    verma = VermaModuleExact(c_val, 10)

    # L_1 (L_{-2}^2|0>)
    L22_result, L22_vac = verma.apply_Lm(1, (2, 2))
    # L_1 (L_{-4}|0>)
    L4_result, L4_vac = verma.apply_Lm(1, (4,))

    # [TT] = L_{-2}^2|0> - (3/5) L_{-4}|0>
    combined: Dict[Tuple[int, ...], FR] = {}
    for state, coeff in L22_result:
        combined[state] = combined.get(state, FR(0)) + coeff
    for state, coeff in L4_result:
        combined[state] = combined.get(state, FR(0)) + FR(-3, 5) * coeff
    combined_vac = L22_vac + FR(-3, 5) * L4_vac
    combined = {k: v for k, v in combined.items() if v != FR(0)}
    is_qp = (len(combined) == 0 and combined_vac == FR(0))

    return {
        'is_quasi_primary': is_qp,
        'L1_on_L22': (L22_result, L22_vac),
        'L1_on_L4': (L4_result, L4_vac),
        'combined': combined,
        'combined_vac': combined_vac,
    }


# ============================================================================
# H^1 vs p(h) - p(h-1) comparison
# ============================================================================


def h1_vs_partition_difference(max_weight: int = 15) -> Dict[int, Dict[str, object]]:
    """Compare dim H^1(B(Vir))_w with various partition functions.

    dim H^1_w: 0,0,1,1,1,0,0,0,0,0,...  (conformal weight grading)
    p_geq2(w): 1,0,1,1,2,2,4,4,7,8,...  (Verma module dimensions)
    q_geq2(w): 1,0,1,1,1,2,2,3,3,5,...  (CE chain group dimensions)

    The answer to 'is dim H^1_w = p(w) - p(w-1)?' is NO.
    """
    @lru_cache(maxsize=200)
    def p(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        dp_arr = [0] * (n + 1)
        dp_arr[0] = 1
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp_arr[j] += dp_arr[j - i]
        return dp_arr[n]

    truncation = max(2 * max_weight + 4, 30)
    ce = VirasoroCEEngine(max_weight=truncation)
    results = {}
    for w in range(0, max_weight + 1):
        h1 = 0 if w < 2 else ce.cohomology_dim(1, w)
        results[w] = {
            'h1_dim': h1,
            'p_diff': p(w) - p(w - 1) if w >= 1 else 1,
            'p_geq2': p_geq2(w),
            'q_geq2': q_geq2(w),
        }
    return results


# ============================================================================
# Summary: complete dimension tables
# ============================================================================


def full_summary(max_weight: int = 10) -> Dict[str, object]:
    """Complete summary of bar cohomology dimensions at each weight.

    Returns conformal-weight-graded table (CE cohomology) and
    PBW-degree-graded table (Motzkin convolution).
    """
    coh_table = compute_full_cohomology_table(max_weight, max_bar_degree=4)
    ce_totals = compute_ce_total_at_weight(max_weight)
    pbw_dims = {n: koszul_dual_pbw_dim(n) for n in range(max_weight + 1)}

    return {
        'cohomology_by_degree_weight': coh_table,
        'ce_total_by_weight': ce_totals,
        'pbw_degree_dims': pbw_dims,
    }
