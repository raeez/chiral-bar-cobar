r"""Explicit bar complex and bar cohomology of the Virasoro algebra.

Computes the bar cohomology H*(B(Vir_c)) via three methods:

1. CHEVALLEY-EILENBERG COHOMOLOGY of Vir_- = span{L_{-n} : n >= 2}.
   This gives the E_2 page of the PBW spectral sequence.
   For Koszul algebras (which Virasoro is), E_2 = E_infinity = H*(B).
   The bracket: [L_{-m}, L_{-n}] = (n - m)L_{-m-n}, NO central extension
   (since m, n >= 2 implies m+n >= 4 > 0, so delta_{m+n,0} = 0).
   Result: H*(B(Vir_c)) is INDEPENDENT OF c.

2. DIRECT n-th product computation using Virasoro commutation relations.
   The mode formula (L_{-k}|0>)_{(n)} b = L_{n-k+1} b gives explicit
   collision residues.  Cross-validates the CE computation.

3. DIMENSION TABLES for the bar chain complex.

THE VERMA MODULE V_c (vacuum representation):
States are L_{-n_1}...L_{-n_k}|0> with n_1 >= ... >= n_k >= 2, sum = n.
Number of states at weight n: p_{>=2}(n) (partitions into parts >= 2).

THE n-TH PRODUCTS:
For a = L_{-k}|0>: Y(a, z) = sum_m L_m z^{-m-k}.
So a_{(n)} b = L_{n-k+1} b.
[L_m, L_n] = (m-n)L_{m+n} + (c/12)(m^3-m) delta_{m+n,0}.

BAR COHOMOLOGY via CE:
H^k(B(Vir_c)) at conformal weight w equals H^k(CE(Vir_-))_w.
Vir_- has generators {L_{-n} : n >= 2} at weight n.
Bracket: [L_{-m}, L_{-n}] = (n-m)L_{-m-n} (no central term for m,n >= 2).

The CE complex Lambda^k(Vir_-^*) has basis indexed by k-element subsets
of generators {L_{-2}, L_{-3}, L_{-4}, ...}.  The CE differential is
dual to the bracket.

GROUND TRUTH (from the manuscript):
dim V_h = p_{>=2}(h): 1, 1, 2, 2, 4, 4, 7, 8, 12, 14, 21, ...

For the Koszul dual, H^1(B(Vir)) should give dim(A^!)_w.
These are the dimensions of the exterior algebra Lambda(Vir_-^*)
modulo the image of the CE differential.

GRADING:
- Cohomological grading, |d| = +1.
- Bar degree k uses exterior degree k of Lambda^k(Vir_-^*).
- Internal weight w = sum of weights of the chosen generators.

References:
  comp:virasoro-ope, comp:virasoro-bar-diff (bar_complex_tables.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  prop:arnold-virasoro-deg3 (bar_complex_tables.tex)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Optional, Tuple

import numpy as np
from sympy import Matrix, zeros

# ============================================================================
# Exact rational arithmetic helpers
# ============================================================================

FR = Fraction


def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, np.integer)):
        return Fraction(int(x))
    return Fraction(x)


# ============================================================================
# Partitions
# ============================================================================


@lru_cache(maxsize=256)
def partitions_into_parts_geq2(n: int) -> Tuple[Tuple[int, ...], ...]:
    """All partitions of n into parts >= 2, in decreasing order."""
    if n < 0:
        return ()
    if n == 0:
        return ((),)
    if n == 1:
        return ()
    results: List[Tuple[int, ...]] = []
    _partition_helper(n, 2, n, [], results)
    return tuple(results)


def _partition_helper(remaining, min_part, max_part, current, results):
    if remaining == 0:
        results.append(tuple(current))
        return
    if remaining < min_part:
        return
    for part in range(min(remaining, max_part), min_part - 1, -1):
        current.append(part)
        _partition_helper(remaining - part, min_part, part, current, results)
        current.pop()


@lru_cache(maxsize=256)
def num_states_at_weight(n: int) -> int:
    """p_{>=2}(n) = number of partitions of n into parts >= 2."""
    return len(partitions_into_parts_geq2(n))


# ============================================================================
# Virasoro negative Lie algebra Vir_- and its CE complex
# ============================================================================


class VirasoroCE:
    """Chevalley-Eilenberg complex of Vir_- = span{L_{-n} : n >= 2}.

    The Lie algebra Vir_- has bracket:
      [L_{-m}, L_{-n}] = (n - m) L_{-m-n}

    with NO central extension (for m, n >= 2, m+n >= 4 > 0,
    so delta_{m+n,0} = 0).

    The generators have conformal weight: wt(L_{-n}) = n.
    We truncate at a maximal weight.

    The CE complex Lambda^k(Vir_-^*) is graded by conformal weight.
    A basis element at degree k, weight w is a k-element subset
    {L_{-n_1}, ..., L_{-n_k}} with n_1 < n_2 < ... < n_k >= 2
    and n_1 + ... + n_k = w.

    The CE differential d: Lambda^k -> Lambda^{k+1} is:
      d(e^*_{i_1} ^ ... ^ e^*_{i_k}) =
        sum_{a < b} sum_c f^c_{ab} * (-1)^{insertion sign}
          * e^*_{...replace c by a,b...}

    where [e_a, e_b] = sum_c f^c_{ab} e_c defines the structure constants.

    For Vir_-: generators e_n = L_{-(n+2)} for n = 0, 1, 2, ...
    (so that e_n has weight n+2).  Bracket:
      [e_a, e_b] = ((a+2) - (b+2)) e_{a+b+2}
                 = (a - b) e_{a+b+2}

    if a+b+2 < max_generators (i.e., the output stays within truncation).

    Parameters:
        max_weight: maximal conformal weight to include.
    """

    def __init__(self, max_weight: int = 14):
        self.max_weight = max_weight
        # Generators: L_{-2}, L_{-3}, ..., L_{-max_weight}
        # Indexed 0, 1, ..., max_weight-2
        self.n_gens = max_weight - 1  # generators at weights 2, 3, ..., max_weight
        self._gen_weights = list(range(2, max_weight + 1))

        # Build bracket table: [e_a, e_b] for a < b
        # e_a = L_{-(a+2)}, so bracket [L_{-(a+2)}, L_{-(b+2)}]
        # = ((b+2) - (a+2)) L_{-(a+b+4)} = (b - a) L_{-(a+b+4)}
        # In generator indexing: output index = (a+b+4) - 2 = a+b+2
        self._bracket: Dict[Tuple[int, int], Dict[int, int]] = {}
        for a in range(self.n_gens):
            for b in range(a + 1, self.n_gens):
                c = a + b + 2  # output generator index
                coeff = b - a  # (b+2) - (a+2) = b - a
                if c < self.n_gens and coeff != 0:
                    self._bracket[(a, b)] = {c: coeff}

    def weight_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of Lambda^degree(Vir_-^*) at given conformal weight.

        Returns list of sorted tuples of generator indices.
        """
        return list(
            self._weight_subsets(degree, weight, 0)
        )

    def _weight_subsets(self, degree, target_weight, start):
        """Generate degree-subsets of generators with exact total weight."""
        if degree == 0:
            if target_weight == 0:
                yield ()
            return
        for i in range(start, self.n_gens - degree + 1):
            w = self._gen_weights[i]
            if w > target_weight:
                continue
            remaining_gens = self.n_gens - i - 1
            if remaining_gens < degree - 1:
                continue
            # Minimum weight of remaining degree-1 generators
            min_remaining = sum(
                self._gen_weights[i + 1 + j] for j in range(degree - 1)
            ) if degree > 1 else 0
            if target_weight - w < min_remaining:
                continue
            for rest in self._weight_subsets(degree - 1, target_weight - w, i + 1):
                yield (i,) + rest

    def ce_differential(self, degree: int, weight: int) -> Matrix:
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight.

        The CE differential is dual to the Lie bracket:
          d(xi^{i_1} ^ ... ^ xi^{i_k})
            = sum_{a < b} [e_a, e_b]^c * sign * (xi^{i_1} ^ ... replace xi^c by xi^a ^ xi^b ...)

        More precisely: for alpha = {i_1 < ... < i_k},
        for each bracket [e_a, e_b] = f^c_{ab} e_c with c in alpha,
        remove c from alpha, insert a and b, multiply by
        (-1)^{pos of c in alpha} * (-1)^{insertion sign of a,b in new set} * f^c_{ab}.
        """
        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)
        if n_src == 0 or n_tgt == 0:
            return zeros(n_tgt, n_src)

        target_idx = {t: i for i, t in enumerate(target)}
        mat = zeros(n_tgt, n_src)

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)

            for (a, b), br in self._bracket.items():
                for c, coeff in br.items():
                    if c not in alpha_set:
                        continue
                    # Cannot insert a or b if already present
                    # (exterior algebra: no repeats)
                    new_set = (alpha_set - {c}) | {a, b}
                    if len(new_set) != degree + 1:
                        # a or b was already in alpha_set (besides c)
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue

                    # Sign computation
                    # (1) Sign from removing c at position pos_c
                    pos_c = alpha_list.index(c)
                    # (2) Sign from inserting a, b into the sorted new set
                    sorted_new = list(new_tuple)
                    pos_a = sorted_new.index(a)
                    remaining_after_a = sorted(new_set - {a})
                    pos_b = remaining_after_a.index(b)
                    sign = (-1) ** pos_c * (-1) ** pos_a * (-1) ** pos_b

                    mat[row, col] += sign * coeff

        return mat

    def cohomology_dim(self, degree: int, weight: int) -> int:
        """dim H^degree(Vir_-)_weight via CE cohomology."""
        dim_p = len(self.weight_basis(degree, weight))
        if dim_p == 0:
            return 0
        d_curr = self.ce_differential(degree, weight)
        ker = dim_p - (d_curr.rank() if d_curr.rows > 0 else 0)
        if degree > 0:
            d_prev = self.ce_differential(degree - 1, weight)
            im = d_prev.rank() if d_prev.rows > 0 and d_prev.cols > 0 else 0
        else:
            im = 0
        return ker - im

    def verify_d_squared(self, degree: int, weight: int) -> bool:
        """Check d^2 = 0 at given degree and weight."""
        d_p = self.ce_differential(degree, weight)
        d_p1 = self.ce_differential(degree + 1, weight)
        if d_p.cols == 0 or d_p1.rows == 0:
            return True
        if d_p.rows != d_p1.cols:
            return True
        return (d_p1 * d_p).is_zero_matrix

    def chain_group_dim(self, degree: int, weight: int) -> int:
        """dim Lambda^degree(Vir_-^*) at weight."""
        return len(self.weight_basis(degree, weight))


# ============================================================================
# Bar cohomology via CE (the main computation)
# ============================================================================


def virasoro_bar_cohomology_ce(
    max_weight: int = 14, max_degree: int = 6
) -> Dict[int, Dict[int, int]]:
    """Compute H*(B(Vir)) at each (degree, weight) via CE cohomology.

    Since the Virasoro algebra is chirally Koszul (PBW spectral
    sequence collapses at E_2), the CE cohomology of Vir_- equals
    the bar cohomology H*(B(Vir_c)) for all c.

    The result is INDEPENDENT OF c because the CE complex of Vir_-
    has no central extension.

    Returns: dict degree -> (dict weight -> dim).
    """
    ce = VirasoroCE(max_weight)
    result: Dict[int, Dict[int, int]] = {}

    for deg in range(1, max_degree + 1):
        weight_dims: Dict[int, int] = {}
        for w in range(2 * deg, max_weight + 1):
            # Minimum weight at degree k is 2+3+...+(k+1) = k(k+3)/2
            min_w = sum(range(2, deg + 2))
            if w < min_w:
                continue
            dim = ce.cohomology_dim(deg, w)
            if dim > 0:
                weight_dims[w] = dim
        if weight_dims:
            result[deg] = weight_dims

    return result


def virasoro_bar_h1_dims(max_weight: int = 14) -> Dict[int, int]:
    """Dimensions of H^1(B(Vir)) at each conformal weight.

    H^1 = Koszul dual dimensions. These are the dimensions of the
    space Ext^1(k, k) = H^1(Vir_-, k) at each weight.

    For the Virasoro algebra with single generator T (weight 2),
    the bar cohomology H^1 gives the linear dual space of the
    Koszul dual A^! = Ext_A(k, k).
    """
    ce = VirasoroCE(max_weight)
    result = {}
    for w in range(2, max_weight + 1):
        dim = ce.cohomology_dim(1, w)
        result[w] = dim
    return result


def virasoro_bar_total_cohomology(
    max_weight: int = 14, max_degree: int = 6
) -> Dict[int, int]:
    """Total bar cohomology at each degree.

    Returns: dict degree -> sum_w dim H^degree_w.
    """
    full = virasoro_bar_cohomology_ce(max_weight, max_degree)
    return {deg: sum(d.values()) for deg, d in full.items()}


def virasoro_bar_dim_table(max_weight: int = 14) -> Dict[Tuple[int, int], int]:
    """Chain group dimensions: dim B^k_w = dim Lambda^k(Vir_-^*)_w.

    This is the PBW-level (before cohomology) dimension.
    """
    ce = VirasoroCE(max_weight)
    result = {}
    max_k = max_weight // 2
    for k in range(1, max_k + 1):
        for w in range(2 * k, max_weight + 1):
            dim = ce.chain_group_dim(k, w)
            if dim > 0:
                result[(k, w)] = dim
    return result


# ============================================================================
# Virasoro n-th products (for cross-validation and OPE extraction)
# ============================================================================


class VermaModule:
    """Vacuum Verma module of Virasoro at central charge c.

    States: L_{-n_1}...L_{-n_k}|0> with n_i >= 2, decreasing order.
    L_m action via [L_m, L_n] = (m-n)L_{m+n} + (c/12)(m^3-m)delta_{m+n,0}.
    """

    def __init__(self, c: Fraction, max_weight: int):
        self.c = _frac(c)
        self.max_weight = max_weight

    @lru_cache(maxsize=8192)
    def apply_Lm_to_partition(
        self, m: int, partition: Tuple[int, ...]
    ) -> Tuple[Tuple[Tuple[Tuple[int, ...], FR], ...], FR]:
        """Apply L_m to L_{-p_1}...L_{-p_k}|0>.

        Returns (tuple of (partition, coeff), vacuum_coeff).
        """
        if len(partition) == 0:
            if m >= -1:
                return (), FR(0)
            else:
                n = -m
                if n > self.max_weight:
                    return (), FR(0)
                return (((n,), FR(1)),), FR(0)

        n = partition[0]
        rest = partition[1:]

        result_dict: Dict[Tuple[int, ...], FR] = {}
        vac_total = FR(0)

        # Term 1: L_{-n} L_m (rest)
        sub_result, sub_vac = self.apply_Lm_to_partition(m, rest)

        if sub_vac != FR(0) and n >= 2 and n <= self.max_weight:
            key = (n,)
            result_dict[key] = result_dict.get(key, FR(0)) + sub_vac

        for part2, c2 in sub_result:
            if c2 == FR(0):
                continue
            new_part = _prepend_sorted(n, part2)
            new_w = n + sum(part2)
            if new_w <= self.max_weight:
                result_dict[new_part] = result_dict.get(new_part, FR(0)) + c2

        # Term 2: (m+n) L_{m-n} (rest)
        bracket_coeff = FR(m + n)
        new_mode = m - n
        if bracket_coeff != FR(0):
            if new_mode == 0:
                rest_w = sum(rest)
                if len(rest) > 0:
                    val = bracket_coeff * FR(rest_w)
                    result_dict[rest] = result_dict.get(rest, FR(0)) + val
            else:
                sub2_result, sub2_vac = self.apply_Lm_to_partition(new_mode, rest)
                vac_total += bracket_coeff * sub2_vac
                for part2, c2 in sub2_result:
                    scaled = bracket_coeff * c2
                    if scaled != FR(0) and sum(part2) <= self.max_weight:
                        result_dict[part2] = result_dict.get(part2, FR(0)) + scaled

        # Term 3: central term (c/12)(m^3-m) delta_{m,n}
        if m == n:
            central = self.c * FR(m**3 - m) / FR(12)
            if central != FR(0):
                if len(rest) == 0:
                    vac_total += central
                else:
                    result_dict[rest] = result_dict.get(rest, FR(0)) + central

        result_tuples = tuple(
            (k, v) for k, v in sorted(result_dict.items()) if v != FR(0)
        )
        return result_tuples, vac_total


class VirasoroNthProducts:
    """Compute n-th products a_{(n)}b for Verma module states.

    Single-mode: (L_{-k}|0>)_{(n)} b = L_{n-k+1} b.
    Multi-mode: recursive Borcherds-Li formula.
    """

    def __init__(self, verma: VermaModule):
        self.verma = verma

    @lru_cache(maxsize=32768)
    def nth_product(
        self, a_part: Tuple[int, ...], n: int, b_part: Tuple[int, ...]
    ) -> Tuple[Tuple[Tuple[Tuple[int, ...], FR], ...], FR]:
        """Compute a_{(n)}b."""
        if len(a_part) == 0:
            return (), FR(0)

        if len(a_part) == 1:
            k = a_part[0]
            mode = n - k + 1
            return self.verma.apply_Lm_to_partition(mode, b_part)

        # Multi-mode: (L_{-k}v)_{(n)} w via Borcherds-Li
        k = a_part[0]
        v_part = a_part[1:]
        max_j = k  # C(k-1, j) = 0 for j >= k

        result_dict: Dict[Tuple[int, ...], FR] = {}
        vac_total = FR(0)

        for j in range(max_j):
            binom_c = FR(_binom(k - 1, j))

            # First sum: (-1)^j C(k-1,j) L_{n+j-k+1} (v_{(j)} w)
            sign1 = FR((-1)**j)
            coeff1 = sign1 * binom_c
            if coeff1 != FR(0):
                vj_r, vj_v = self.nth_product(v_part, j, b_part)
                mode1 = n + j - k + 1

                if vj_v != FR(0):
                    Lm_r, Lm_v = self.verma.apply_Lm_to_partition(mode1, ())
                    vac_total += coeff1 * vj_v * Lm_v
                    for p, c in Lm_r:
                        result_dict[p] = result_dict.get(p, FR(0)) + coeff1 * vj_v * c

                for p2, c2 in vj_r:
                    if c2 == FR(0):
                        continue
                    Lm_r, Lm_v = self.verma.apply_Lm_to_partition(mode1, p2)
                    vac_total += coeff1 * c2 * Lm_v
                    for p3, c3 in Lm_r:
                        result_dict[p3] = result_dict.get(p3, FR(0)) + coeff1 * c2 * c3

            # Second sum: (-1)^{k+j} C(k-1,j) v_{(n+k-1-j)} (L_j w)
            sign2 = FR((-1)**(k + j))
            coeff2 = sign2 * binom_c
            if coeff2 != FR(0):
                prod_idx = n + k - 1 - j
                Lj_r, Lj_v = self.verma.apply_Lm_to_partition(j, b_part)

                if Lj_v != FR(0):
                    vp_r, vp_v = self.nth_product(v_part, prod_idx, ())
                    vac_total += coeff2 * Lj_v * vp_v
                    for p2, c2 in vp_r:
                        result_dict[p2] = result_dict.get(p2, FR(0)) + coeff2 * Lj_v * c2

                for p2, c2 in Lj_r:
                    if c2 == FR(0):
                        continue
                    vp_r, vp_v = self.nth_product(v_part, prod_idx, p2)
                    vac_total += coeff2 * c2 * vp_v
                    for p3, c3 in vp_r:
                        result_dict[p3] = result_dict.get(p3, FR(0)) + coeff2 * c2 * c3

        result_tuples = tuple(
            (k, v) for k, v in sorted(result_dict.items()) if v != FR(0)
        )
        return result_tuples, vac_total


def _binom(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    from math import comb
    return comb(n, k)


def _prepend_sorted(n: int, partition: Tuple[int, ...]) -> Tuple[int, ...]:
    lst = list(partition)
    pos = 0
    while pos < len(lst) and lst[pos] >= n:
        pos += 1
    lst.insert(pos, n)
    return tuple(lst)


def total_ope_extraction(
    nth_prods: VirasoroNthProducts,
    a_part: Tuple[int, ...],
    b_part: Tuple[int, ...],
) -> Tuple[Dict[Tuple[int, ...], FR], FR]:
    """Compute mu(a, b) = sum_{n >= 0} a_{(n)} b."""
    max_n = sum(a_part) + sum(b_part)
    result_dict: Dict[Tuple[int, ...], FR] = {}
    vac_total = FR(0)

    for n in range(max_n + 1):
        nth_result, nth_vac = nth_prods.nth_product(a_part, n, b_part)
        vac_total += nth_vac
        for part, coeff in nth_result:
            result_dict[part] = result_dict.get(part, FR(0)) + coeff

    return result_dict, vac_total


# ============================================================================
# Verification helpers
# ============================================================================


def verify_low_weight_ope(c: FR) -> Dict[str, bool]:
    """Verify OPE products at low weight."""
    c = _frac(c)
    verma = VermaModule(c, 10)
    nth = VirasoroNthProducts(verma)
    T, dT = (2,), (3,)
    results = {}

    r3, v3 = nth.nth_product(T, 3, T)
    results['T_(3)T = c/2 vac'] = (len(r3) == 0 and v3 == c / FR(2))

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


def verify_ce_d_squared(max_weight: int = 10) -> Dict[Tuple[int, int], bool]:
    """Verify d^2 = 0 for the CE complex of Vir_-."""
    ce = VirasoroCE(max_weight)
    results = {}
    for deg in range(0, 5):
        for w in range(2 * (deg + 1), max_weight + 1):
            ok = ce.verify_d_squared(deg, w)
            results[(deg, w)] = ok
    return results
