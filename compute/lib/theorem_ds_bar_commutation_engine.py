r"""DS-bar commutation engine: chain-level comparison of B(DS(-)) vs DS(B(-)).

MATHEMATICAL CONTENT
====================

THE BOTTLENECK FOR DIRECTION 4: does the bar functor commute with
Drinfeld-Sokolov reduction at the chain level?

Two paths from V_k(g) to a cochain complex:

  Path A (bar-then-DS):  V_k(g)  -->  B(V_k(g))  -->  DS(B(V_k(g)))
  Path B (DS-then-bar):  V_k(g)  -->  W_k(g)     -->  B(W_k(g))

If B and DS commute (up to quasi-isomorphism), then the Koszul duality
theory for V_k(g) descends to W_k(g), proving bar-cobar duality for
ALL W-algebras obtainable by DS reduction.

GENUS-0 ANALYSIS
================

At genus 0, both the bar differential d_bar and the BRST differential
d_BRST are chain maps on graded complexes.  The question is whether the
PBW filtration on B(V_k(g)) is compatible with the BRST grading.

For sl_2 -> Vir_c (principal DS reduction, c(k) = 1 - 6(k+1)^2/(k+2)):
  - V_k(sl_2) has 3 generators {e, h, f} at conformal weight 1.
  - Vir_c has 1 generator {T} at conformal weight 2.
  - The BRST complex has generators {J^a, b^alpha, c_alpha} where
    alpha runs over positive roots (just alpha_1 for sl_2).

The bar complex B(V_k(sl_2)) is graded by:
  (1) Bar degree n (number of tensor factors)
  (2) Conformal weight h (sum of mode numbers)

The CE complex Lambda^p(g_-^*) computes the bar cohomology by PBW
collapse (Koszulness).  The BRST reduction acts on each weight space.

CHAIN-LEVEL COMPARISON STRATEGY
================================

We compare the two paths by computing:

1. H*(B(V_k(sl_2))) at each (bar degree, conformal weight):
   Known from bar_differential_sl2_matrices_engine.py.
   Result: H^n concentrated at weight n(n+1)/2, dim H^n = 2n+1.

2. H*(B(Vir_c)) at each (bar degree, conformal weight):
   Known from bar_cohomology_virasoro_explicit_engine.py.
   Result: H^1 at weights {2,3,4}, H^2 starting at weight 7.

3. The BRST reduction of H*(B(V_k(sl_2))):
   DS acts on each H^n(B(sl_2)) = (2n+1)-dimensional sl_2-module.
   The BRST cohomology H*(BRST, H^n(B)) extracts the highest-weight
   vector, which has dimension 1 for each irreducible module.

4. Comparison: does dim H^p(BRST, H^n(B(sl_2)))_h match dim H^q(B(Vir))_h
   under appropriate degree/weight shifts?

KEY INSIGHT: DS-BAR COMMUTATION AT THE COHOMOLOGY LEVEL
========================================================

For sl_2 -> Vir, the bar cohomology H^n(B(V_k(sl_2))) is the
(2n+1)-dimensional irreducible sl_2-module V_{2n}.  The DS functor
extracts the top component (highest weight vector), giving:

  DS(H^n(B(sl_2))) = 1-dimensional, at conformal weight n(n+1)/2 + n
                    = n(n+3)/2 (shifted by the BRST ghost number).

Wait: the DS reduction CHANGES the conformal weight.  The Sugawara
formula T_Sug = (1/(2(k+2))) sum J^a J_a gives the Virasoro generator.
The DS reduction maps weight-h states of sl_2 to weight-h' states of Vir
with h' = h (the conformal weight is preserved by the DS functor when
measured in the BRST-reduced grading).

Actually, the DS functor for sl_2 -> Vir takes V_k(sl_2) generators at
weight 1 and produces Vir generator T at weight 2.  The weight shift is:
  T = (1/(2(k+2)))(J^e J^f + J^f J^e + (1/2) J^h J^h)
which is a QUADRATIC expression in the weight-1 generators.

So the DS functor does NOT simply pass through the bar complex.  It
changes the ALGEBRAIC STRUCTURE.  The commutation question is whether
the homological algebra (bar cohomology dimensions, Euler characteristics)
is preserved.

EULER CHARACTERISTIC COMPARISON
================================

The decisive first test: compare Euler characteristics at each conformal
weight.

For V_k(sl_2):
  chi_h(B(sl_2)) = sum_n (-1)^n dim(Lambda^n(g_-^*)_h)

For Vir_c:
  chi_h(B(Vir)) = sum_n (-1)^n dim(Lambda^n(Vir_-^*)_h)

The DS reduction relates these via:
  chi_h(B(Vir)) should equal the DS-reduced Euler characteristic of B(sl_2).

This is a weaker statement than chain-level commutation but provides
the first computational evidence.

FILTRATION COMPATIBILITY
========================

The PBW filtration on V_k(sl_2) induces a filtration on B(V_k(sl_2)).
The BRST differential d_BRST respects this filtration iff DS commutes
with bar at the filtered level.

For the PBW spectral sequence:
  E_1 page of B(V_k(sl_2)) = Lambda^*(g_-^*)  (CE complex)
  E_1 page of B(Vir_c) = Lambda^*(Vir_-^*)    (CE complex)

The DS reduction on E_1 pages is:
  DS(Lambda^p(g_-^*)) contains Lambda^q(Vir_-^*) as the BRST cohomology.

If the spectral sequence is compatible, then:
  E_2(B(sl_2)) --(DS)--> E_2(B(Vir))
which would prove DS-bar commutation at the E_2 level.

EXPLICIT COMPUTATION FOR sl_2 -> Vir
======================================

We compute at each conformal weight h = 0, 1, ..., max_weight:

1. dim Lambda^p(sl_2_-^*)_h for p = 0, 1, 2, ...
2. dim Lambda^p(Vir_-^*)_h for p = 0, 1, 2, ...
3. The sl_2 representation content of Lambda^p(sl_2_-^*)_h
4. The BRST reduction of (3) = extraction of trivial subrepresentations
5. Comparison of (4) with (2)

For (3): at weight h, the sl_2 representation decomposes into irreducibles.
The DS functor extracts the n_+-BRST cohomology, which for finite-dim
sl_2-modules is the space of highest-weight vectors.

WEIGHT SHIFT IN DS REDUCTION
=============================

Under the DS reduction sl_2 -> Vir, the conformal weight is shifted:
  h_Vir = h_sl2 - h_BRST
where h_BRST accounts for the ghost contribution.

For the principal embedding sl_2 -> sl_2 (trivially the identity),
the BRST complex has:
  - Matter sector: V_k(sl_2) with L_0 eigenvalue h
  - Ghost sector: bc system for the positive root alpha
    b has weight 1 (since the root has grade 1 in the Dynkin grading)
    c has weight 0

The BRST differential has ghost number +1.  The DS-reduced conformal
weight equals the original weight (the ghost contribution cancels in
the trace for the modified L_0).

Actually, for sl_2 -> Vir (principal DS), the modified stress tensor is:
  T_DS = T_Sug + (1/2) partial J^h = T_Sug + (1/2) partial h(z)
which shifts the conformal weights of generators:
  e: weight 1 -> weight 0 (shifted by -1 from the h-eigenvalue +2)
  h: weight 1 -> weight 1 (shifted by 0)
  f: weight 1 -> weight 2 (shifted by +1 from the h-eigenvalue -2)

In the DS reduction, e and b form a contractible pair, c is absorbed,
and T = the Sugawara-modified generator is the only surviving generator.
T has conformal weight 2 under the modified L_0.

So the DS weight shift is:
  For a state of sl_2-weight h and h-eigenvalue m:
    h_DS = h - m/2   (shifted by the Cartan eigenvalue divided by 2)

For bar complex elements: at bar degree p with generators at modes
(n_1, ..., n_p), the total conformal weight is n_1 + ... + n_p.
Each generator carries an sl_2 index a_i, and the total h-eigenvalue
is sum of the h-eigenvalues of the a_i.

This makes the weight comparison tractable: we just need to track
the h-eigenvalue decomposition at each weight.

References:
    bar_differential_sl2_matrices_engine.py: sl_2 bar complex matrices
    bar_cohomology_virasoro_explicit_engine.py: Virasoro bar cohomology
    ds_shadow_cascade_engine.py: DS shadow cascade data
    theorem_butson_inverse_reduction_engine.py: Butson inverse reduction
    theorem_transport_transpose_sl4_engine.py: sl_4 duality data
    thm:ds-koszul-obstruction (manuscript): DS introduces higher SC ops
    AP19: bar kernel absorbs a pole (d log absorption)
    AP14: Koszulness != formality (DS introduces SC non-formality)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from typing import Dict, List, Optional, Tuple

import numpy as np


# ============================================================================
# Exact arithmetic helpers (self-contained to avoid import cycles)
# ============================================================================

FR = Fraction


def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    return Fraction(int(x)) if isinstance(x, (int, np.integer)) else Fraction(x)


def _frac_array(shape) -> np.ndarray:
    arr = np.empty(shape, dtype=object)
    arr.fill(Fraction(0))
    return arr


def _frac_matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    if A.size == 0 or B.size == 0:
        return _frac_array((A.shape[0], B.shape[1]))
    m, k1 = A.shape
    k2, n = B.shape
    assert k1 == k2
    C = _frac_array((m, n))
    for i in range(m):
        for j in range(n):
            s = Fraction(0)
            for el in range(k1):
                s += A[i, el] * B[el, j]
            C[i, j] = s
    return C


def _kernel_dim(M: np.ndarray) -> int:
    """Dimension of kernel of a Fraction matrix via row echelon."""
    if M.size == 0:
        return M.shape[1] if len(M.shape) == 2 else 0
    rows, cols = M.shape
    if rows == 0:
        return cols
    if cols == 0:
        return 0
    A = M.copy()
    pivot_cols = []
    row = 0
    for col in range(cols):
        found = None
        for r in range(row, rows):
            if A[r, col] != Fraction(0):
                found = r
                break
        if found is None:
            continue
        if found != row:
            A[[row, found]] = A[[found, row]]
        pivot = A[row, col]
        for r in range(row + 1, rows):
            if A[r, col] != Fraction(0):
                factor = A[r, col] / pivot
                for c2 in range(col, cols):
                    A[r, c2] -= factor * A[row, c2]
        pivot_cols.append(col)
        row += 1
    return cols - len(pivot_cols)


def _rank(M: np.ndarray) -> int:
    """Rank of a Fraction matrix."""
    if M.size == 0:
        return 0
    return M.shape[1] - _kernel_dim(M)


def _image_dim(M: np.ndarray) -> int:
    """Dimension of image = rank."""
    return _rank(M)


# ============================================================================
# sl_2 Lie algebra data
# ============================================================================

DIM_SL2 = 3
SL2_NAMES = {0: 'e', 1: 'h', 2: 'f'}

# H-eigenvalues: e has eigenvalue +2, h has 0, f has -2
SL2_H_EIGENVALUE = {0: 2, 1: 0, 2: -2}

# Structure constants: [e_a, e_b] = sum_c f^c_{ab} e_c
SL2_BRACKET: Dict[Tuple[int, int], Dict[int, Fraction]] = {
    (0, 2): {1: Fraction(1)},    # [e, f] = h
    (2, 0): {1: Fraction(-1)},   # [f, e] = -h
    (1, 0): {0: Fraction(2)},    # [h, e] = 2e
    (0, 1): {0: Fraction(-2)},   # [e, h] = -2e
    (1, 2): {2: Fraction(-2)},   # [h, f] = -2f
    (2, 1): {2: Fraction(2)},    # [f, h] = 2f
}


# ============================================================================
# Central charge formulas
# ============================================================================

def c_sl2(k: Fraction) -> Fraction:
    r"""Central charge of V_k(sl_2) = 3k/(k+2)."""
    if k + 2 == 0:
        raise ValueError("Critical level k = -2")
    return Fraction(3) * k / (k + 2)


def c_vir_from_sl2(k: Fraction) -> Fraction:
    r"""Central charge of Vir = DS(V_k(sl_2)).

    c = 1 - 6(k+1)^2/(k+2)
      = 1 - 6(k^2 + 2k + 1)/(k+2)

    Equivalently: c = 13 - 6(k+2) - 6/(k+2)
    (from the Fateev-Lukyanov formula with N=2, matching c_WN in
    ds_shadow_cascade_engine.py).
    """
    if k + 2 == 0:
        raise ValueError("Critical level k = -2")
    return Fraction(1) - Fraction(6) * (k + 1)**2 / (k + 2)


def kappa_sl2(k: Fraction) -> Fraction:
    r"""Modular characteristic kappa(sl_2, k) = dim(sl_2)(k+h^v)/(2h^v) = 3(k+2)/4."""
    return Fraction(3) * (k + 2) / Fraction(4)


def kappa_vir(k: Fraction) -> Fraction:
    r"""Modular characteristic kappa(Vir_c) = c/2 where c = c_vir_from_sl2(k)."""
    return c_vir_from_sl2(k) / Fraction(2)


# ============================================================================
# Loop algebra CE complex for sl_2 (bar cohomology computation)
# ============================================================================

class SL2BarCohomology:
    """Chevalley-Eilenberg cohomology of sl_2_- computing H*(B(V_k(sl_2))).

    The loop algebra sl_2_- = sl_2 tensor t^{-1}C[t^{-1}] has generators
    (a, m) for a in {e, h, f}, m >= 1.  The CE complex Lambda^p(sl_2_-^*)
    at conformal weight h computes bar cohomology at bar degree p.

    Each generator (a, m) carries:
      - Conformal weight m
      - h-eigenvalue: SL2_H_EIGENVALUE[a] (i.e. e->+2, h->0, f->-2)
    """

    def __init__(self, max_weight: int = 8):
        self.max_weight = max_weight
        self.dim_g = DIM_SL2
        self.n_gens = DIM_SL2 * max_weight

        # Generator list: (lie_idx, mode, flat_idx, h_eigenvalue)
        self.generators: List[Tuple[int, int, int, int]] = []
        idx = 0
        for m in range(1, max_weight + 1):
            for a in range(DIM_SL2):
                self.generators.append((a, m, idx, SL2_H_EIGENVALUE[a]))
                idx += 1

        # Bracket table for flat indices
        self._bracket_table: Dict[Tuple[int, int], Dict[int, Fraction]] = {}
        for i in range(self.n_gens):
            ai, mi, _, _ = self.generators[i]
            for j in range(i + 1, self.n_gens):
                aj, mj, _, _ = self.generators[j]
                m_sum = mi + mj
                if m_sum > max_weight:
                    continue
                br = SL2_BRACKET.get((ai, aj))
                if br:
                    result = {}
                    for c, coeff in br.items():
                        flat_c = c + DIM_SL2 * (m_sum - 1)
                        result[flat_c] = _frac(coeff)
                    if result:
                        self._bracket_table[(i, j)] = result

        self._basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}
        self._diff_cache: Dict[Tuple[int, int], np.ndarray] = {}

    def weight_of(self, flat_idx: int) -> int:
        return self.generators[flat_idx][1]

    def h_eigenvalue_of(self, flat_idx: int) -> int:
        return self.generators[flat_idx][3]

    def name_of(self, flat_idx: int) -> str:
        a, m, _, _ = self.generators[flat_idx]
        return f"{SL2_NAMES[a]}_{m}"

    def weight_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of Lambda^degree(sl_2_-^*)_weight."""
        key = (degree, weight)
        if key in self._basis_cache:
            return self._basis_cache[key]
        result = list(self._weight_subsets(degree, weight, 0))
        self._basis_cache[key] = result
        return result

    def _weight_subsets(self, degree: int, weight: int,
                        start: int) -> List[Tuple[int, ...]]:
        if degree == 0:
            return [()] if weight == 0 else []
        if degree < 0 or weight < degree:
            return []
        results = []
        for i in range(start, self.n_gens - degree + 1):
            w = self.generators[i][1]
            if w > weight:
                continue
            for rest in self._weight_subsets(degree - 1, weight - w, i + 1):
                results.append((i,) + rest)
        return results

    def chain_dim(self, degree: int, weight: int) -> int:
        return len(self.weight_basis(degree, weight))

    def h_eigenvalue_decomposition(self, degree: int, weight: int) -> Dict[int, int]:
        """Decompose Lambda^degree_weight by total h-eigenvalue.

        Returns {m: count} where m is the total h-eigenvalue and count
        is the number of basis elements with that eigenvalue.
        """
        decomp: Dict[int, int] = {}
        for alpha in self.weight_basis(degree, weight):
            m_total = sum(self.h_eigenvalue_of(i) for i in alpha)
            decomp[m_total] = decomp.get(m_total, 0) + 1
        return decomp

    def differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight."""
        key = (degree, weight)
        if key in self._diff_cache:
            return self._diff_cache[key]

        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
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
        """Check d^2 = 0 at (degree, weight)."""
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

    def cohomology_dim(self, degree: int, weight: int) -> int:
        """dim H^degree(Lambda^*(sl_2_-^*))_weight = dim H^degree(B(V_k(sl_2)))_weight."""
        d_in = self.differential_matrix(degree - 1, weight) if degree >= 1 else _frac_array((0, 0))
        d_out = self.differential_matrix(degree, weight)

        ker = _kernel_dim(d_out) if d_out.size > 0 else self.chain_dim(degree, weight)
        img = _image_dim(d_in) if d_in.size > 0 else 0

        return ker - img

    def euler_char(self, weight: int, max_degree: int = 0) -> Fraction:
        """Euler characteristic at given weight: sum (-1)^p dim Lambda^p_weight."""
        if max_degree == 0:
            max_degree = weight  # Can't have more exterior factors than weight
        chi = Fraction(0)
        for p in range(max_degree + 1):
            d = self.chain_dim(p, weight)
            if d > 0:
                chi += Fraction((-1)**p) * d
        return chi

    def sl2_representation_at_bar_degree(self, bar_degree: int) -> Dict:
        """Decompose H^n(B(sl_2)) into sl_2 irreducibles.

        For V_k(sl_2), the bar cohomology H^n is concentrated at weight
        n(n+1)/2 and forms the (2n+1)-dimensional irreducible V_{2n}.

        Returns the representation data including highest weight, dimension,
        and weight decomposition.
        """
        n = bar_degree
        conc_weight = n * (n + 1) // 2
        dim_expected = 2 * n + 1

        actual_dim = self.cohomology_dim(n, conc_weight)

        return {
            'bar_degree': n,
            'concentrated_weight': conc_weight,
            'expected_dim': dim_expected,
            'actual_dim': actual_dim,
            'matches': actual_dim == dim_expected,
            'highest_weight': 2 * n,
            'is_irreducible': actual_dim == dim_expected,
        }


# ============================================================================
# Virasoro bar cohomology (CE complex of Vir_-)
# ============================================================================

class VirasoroBarCohomology:
    """CE cohomology of Vir_- = {L_{-n} : n >= 2} computing H*(B(Vir_c)).

    Generators: L_{-n} for n >= 2, indexed by i = n - 2.
    Bracket: [L_{-m}, L_{-n}] = (n - m) L_{-(m+n)}.
    NO central extension for m, n >= 2 (m + n >= 4 > 0).
    """

    def __init__(self, max_weight: int = 10):
        self.max_weight = max_weight
        self.n_gens = max_weight - 1 if max_weight >= 2 else 0

        # Generator i has conformal weight i + 2
        self._bracket_table: Dict[Tuple[int, int], Dict[int, Fraction]] = {}
        for i in range(self.n_gens):
            mi = i + 2
            for j in range(i + 1, self.n_gens):
                mj = j + 2
                m_sum = mi + mj
                if m_sum > max_weight:
                    continue
                # [L_{-mi}, L_{-mj}] = (mj - mi) L_{-(mi+mj)}
                coeff = Fraction(mj - mi)
                if coeff != 0:
                    target_idx = m_sum - 2
                    if 0 <= target_idx < self.n_gens:
                        self._bracket_table[(i, j)] = {target_idx: coeff}

        self._basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}
        self._diff_cache: Dict[Tuple[int, int], np.ndarray] = {}

    def weight_of(self, idx: int) -> int:
        return idx + 2

    def weight_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        key = (degree, weight)
        if key in self._basis_cache:
            return self._basis_cache[key]
        result = list(self._weight_subsets(degree, weight, 0))
        self._basis_cache[key] = result
        return result

    def _weight_subsets(self, degree: int, weight: int,
                        start: int) -> List[Tuple[int, ...]]:
        if degree == 0:
            return [()] if weight == 0 else []
        if degree < 0 or weight < 2 * degree:
            return []
        results = []
        for i in range(start, self.n_gens - degree + 1):
            w = i + 2
            if w > weight:
                continue
            for rest in self._weight_subsets(degree - 1, weight - w, i + 1):
                results.append((i,) + rest)
        return results

    def chain_dim(self, degree: int, weight: int) -> int:
        return len(self.weight_basis(degree, weight))

    def differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        """CE differential d: Lambda^degree_weight -> Lambda^{degree+1}_weight."""
        key = (degree, weight)
        if key in self._diff_cache:
            return self._diff_cache[key]

        source = self.weight_basis(degree, weight)
        target = self.weight_basis(degree + 1, weight)
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

    def cohomology_dim(self, degree: int, weight: int) -> int:
        d_in = self.differential_matrix(degree - 1, weight) if degree >= 1 else _frac_array((0, 0))
        d_out = self.differential_matrix(degree, weight)
        ker = _kernel_dim(d_out) if d_out.size > 0 else self.chain_dim(degree, weight)
        img = _image_dim(d_in) if d_in.size > 0 else 0
        return ker - img

    def euler_char(self, weight: int) -> Fraction:
        chi = Fraction(0)
        max_deg = weight // 2
        for p in range(max_deg + 1):
            d = self.chain_dim(p, weight)
            if d > 0:
                chi += Fraction((-1)**p) * d
        return chi


# ============================================================================
# DS-modified weight and the BRST reduction on the bar complex
# ============================================================================

def ds_weight_shift(sl2_weight: int, h_eigenvalue: int) -> int:
    r"""DS-modified conformal weight.

    Under principal DS reduction sl_2 -> Vir, the modified L_0 is:
      L_0^{DS} = L_0^{Sug} + (1/2) partial J^h
    which shifts conformal weights by half the h-eigenvalue:
      h_{DS} = h - m/2  where m = h-eigenvalue of the state.

    For the bar complex: a p-form in Lambda^p(sl_2_-^*) at conformal
    weight w and total h-eigenvalue m has DS-modified weight w.

    IMPORTANT: in the CE complex, the total conformal weight is the SUM
    of mode numbers, and the h-eigenvalue is the SUM of h-eigenvalues
    of the exterior factors.  The DS-modified weight is:
      w_{DS} = sum(modes) - (1/2) * sum(h-eigenvalues)
    which may be a HALF-INTEGER.

    Actually, for the principal embedding x_0 = (1/2)h with sl_2
    triple {e, h, f}, the BRST grading has:
      grade(e) = +1, grade(h) = 0, grade(f) = -1
    The DS-modified conformal weight is:
      h_{DS} = h_orig + grade_shift
    where the grade shift depends on the nilpotent grading.

    For generators at mode m: e_m has h_{DS} = m - 1, h_m has h_{DS} = m,
    f_m has h_{DS} = m + 1.  So f_{m=1} has h_{DS} = 2 (the Virasoro
    generator T = f_1 + lower-order terms at grade -1).
    """
    # For the principal nilpotent (grade: e -> +1, h -> 0, f -> -1):
    # DS weight = original weight + grade, where grade = -h_eigenvalue/2
    # e has h_eig = +2, grade = -1, so e_m -> weight m-1
    # h has h_eig = 0, grade = 0, so h_m -> weight m
    # f has h_eig = -2, grade = +1, so f_m -> weight m+1
    return sl2_weight - h_eigenvalue // 2


def ds_weight_of_generator(lie_idx: int, mode: int) -> int:
    """DS-modified conformal weight of generator (a, m) of sl_2_-."""
    return mode - SL2_H_EIGENVALUE[lie_idx] // 2


class DSBarComparison:
    """Compare bar cohomology through the two DS paths.

    Path A: V_k(sl_2) -> B(V_k(sl_2)) -> BRST-reduce -> DS(B(V_k(sl_2)))
    Path B: V_k(sl_2) -> Vir_c -> B(Vir_c)

    The comparison is at the level of:
    1. Chain group dimensions (after DS weight shift)
    2. Euler characteristics
    3. Cohomology dimensions
    4. sl_2 representation content and BRST extraction
    """

    def __init__(self, max_weight: int = 8):
        self.max_weight = max_weight
        self.sl2_bar = SL2BarCohomology(max_weight=max_weight)
        self.vir_bar = VirasoroBarCohomology(max_weight=max_weight + 2)

    # ----------------------------------------------------------------
    # DS-modified chain group decomposition for sl_2 bar complex
    # ----------------------------------------------------------------

    def sl2_ds_modified_chain_dims(self, degree: int, weight: int) -> Dict[int, int]:
        """Decompose Lambda^degree(sl_2_-^*)_weight by DS-modified weight.

        Each basis element (a_{i_1}, m_1) ^ ... ^ (a_{i_p}, m_p) with
        sum(m_j) = weight gets DS-modified weight:
          w_DS = sum(m_j - SL2_H_EIGENVALUE[a_{i_j}] / 2)
               = weight - (1/2) * sum(h-eigenvalues)

        Since h-eigenvalues are even ({+2, 0, -2}), w_DS is always an integer.
        Returns {w_DS: count}.
        """
        decomp: Dict[int, int] = {}
        for alpha in self.sl2_bar.weight_basis(degree, weight):
            h_sum = sum(SL2_H_EIGENVALUE[self.sl2_bar.generators[i][0]] for i in alpha)
            w_ds = weight - h_sum // 2
            decomp[w_ds] = decomp.get(w_ds, 0) + 1
        return decomp

    def sl2_ds_modified_euler_char(self, ds_weight: int) -> Fraction:
        """Euler characteristic of the sl_2 bar complex at DS-modified weight.

        chi_{DS}(w) = sum over (degree p, original weight h) of
          (-1)^p * #{basis elements in Lambda^p_h with DS weight = w}
        """
        chi = Fraction(0)
        for orig_weight in range(self.max_weight + 1):
            for p in range(orig_weight + 1):
                decomp = self.sl2_ds_modified_chain_dims(p, orig_weight)
                if ds_weight in decomp:
                    chi += Fraction((-1)**p) * decomp[ds_weight]
        return chi

    # ----------------------------------------------------------------
    # Full comparison tables
    # ----------------------------------------------------------------

    def euler_char_comparison(self, max_ds_weight: int = 0) -> Dict[int, Dict]:
        """Compare Euler characteristics at each DS weight.

        At each DS-modified weight w:
          chi_A(w) = Euler char of DS-modified sl_2 bar complex
          chi_B(w) = Euler char of Virasoro bar complex at weight w

        For DS-bar commutation, we need chi_A = chi_B at all weights.

        IMPORTANT SUBTLETY: the DS reduction introduces a bc ghost system
        that contributes to the Euler characteristic.  The full comparison
        requires accounting for the ghost sector.

        At the E_2 page level (after PBW collapse):
          Path A: H*(B(sl_2)) -> DS -> result
          Path B: H*(B(Vir)) directly

        The comparison at the Euler characteristic level should hold
        WITHOUT ghost correction because both sides use the modified L_0
        grading.  The ghost contribution cancels in the Euler characteristic
        by standard BRST arguments.
        """
        if max_ds_weight == 0:
            max_ds_weight = self.max_weight + 2

        results = {}
        for w in range(max_ds_weight + 1):
            chi_sl2_ds = self.sl2_ds_modified_euler_char(w)
            chi_vir = self.vir_bar.euler_char(w)
            results[w] = {
                'ds_weight': w,
                'chi_sl2_ds_modified': chi_sl2_ds,
                'chi_virasoro': chi_vir,
                'match': chi_sl2_ds == chi_vir,
            }
        return results

    def chain_dim_comparison(self, max_weight: int = 0) -> Dict[int, Dict]:
        """Compare chain dimensions at each DS weight.

        For each DS-modified weight w and each degree p, compare:
          dim_A = number of sl_2 bar chains at DS weight w, CE degree p
          dim_B = dim Lambda^p(Vir_-)_w

        This is a finer comparison than Euler characteristics.
        """
        if max_weight == 0:
            max_weight = self.max_weight

        results = {}
        for w in range(max_weight + 1):
            degree_data = {}
            for p in range(w + 1):
                # Path B: Virasoro chain dim
                vir_dim = self.vir_bar.chain_dim(p, w)

                # Path A: sl_2 chains at DS weight w, degree p
                sl2_ds_dim = 0
                for orig_w in range(self.max_weight + 1):
                    decomp = self.sl2_ds_modified_chain_dims(p, orig_w)
                    sl2_ds_dim += decomp.get(w, 0)

                if vir_dim > 0 or sl2_ds_dim > 0:
                    degree_data[p] = {
                        'sl2_ds_dim': sl2_ds_dim,
                        'vir_dim': vir_dim,
                        'match': sl2_ds_dim == vir_dim,
                    }

            results[w] = degree_data
        return results

    def cohomology_comparison(self, max_weight: int = 0) -> Dict[int, Dict]:
        """Compare bar cohomology dimensions through both paths.

        Path A: H^n(B(sl_2)) = V_{2n} (irreducible sl_2-module).
                DS extracts the highest-weight vector: dim = 1 at each n.
                The DS-modified weight of the HWV at bar degree n:
                  H^n is concentrated at original weight n(n+1)/2.
                  The HWV has h-eigenvalue 2n (highest weight of V_{2n}).
                  DS weight = n(n+1)/2 - n = n(n-1)/2.

                Wait: the HWV is e_{m_1} ^ ... ^ e_{m_n} for some modes.
                But actually the HWV is the element with maximal h-eigenvalue
                in the cohomology H^n. For the (2n+1)-dim irrep V_{2n},
                the HWV has h-eigenvalue 2n and the LWV has h-eigenvalue -2n.

                DS reduction extracts the n_+-BRST cohomology.  For sl_2,
                n_+ = span{e}, and the BRST cohomology of a finite-dim
                sl_2-module V is:
                  H^0(BRST, V) = V^{n_+} / n_+(V) = highest weight space
                  H^p(BRST, V) = 0 for p > 0 (V irreducible)

                So DS(H^n(B(sl_2))) = 1-dimensional at each n, located at
                the DS-modified weight of the highest-weight vector.

                For V_{2n} at conformal weight n(n+1)/2:
                  The HWV has all generators being f-type (h-eig = -2 each).
                  Actually, the HWV has h-eigenvalue +2n (HIGHEST weight).
                  The generators producing H^n at weight n(n+1)/2 must have
                  modes summing to n(n+1)/2 and h-eigenvalues summing to 2n.
                  This means mostly e-type generators (h-eig = +2 each).
                  If all n generators are e-type: h-eigenvalue = 2n, weight = sum(modes).
                  The triangular weight n(n+1)/2 = 1+2+...+n, so the modes are 1,2,...,n.

                  The HWV is e_1 ^ e_2 ^ ... ^ e_n, with:
                    h-eigenvalue = 2n
                    conformal weight = 1+2+...+n = n(n+1)/2
                    DS weight = n(n+1)/2 - 2n/2 = n(n+1)/2 - n = n(n-1)/2

        Path B: H^p(B(Vir))_w for the Virasoro bar complex.
                At bar degree 1: H^1_2 = H^1_3 = H^1_4 = 1 (three generators).
                But wait: Vir has ONE generator T at weight 2.  The bar cohomology
                H^1(B(Vir)) should be 1-dimensional at weight 2.

                Actually, the Koszul dual Vir^! has generators at PBW degree 1
                corresponding to the modes L_{-n} for n >= 2.  These are at
                conformal weights 2, 3, 4, 5, ...

                For a chirally Koszul algebra, H^1(B) = the generators of A^!.
                Vir^! = Vir_{26-c} has strong generators T^! at weight 2
                (and its modes).  But in the CE cohomology:
                H^1(CE(Vir_-))_w = number of generators at weight w MINUS
                relations.

                Let me compute this directly from the engine.

        This method computes the actual cohomology and compares.
        """
        if max_weight == 0:
            max_weight = self.max_weight

        comparison = {}
        for w in range(max_weight + 1):
            sl2_data = {}
            vir_data = {}

            for p in range(w + 1):
                h_sl2 = self.sl2_bar.cohomology_dim(p, w)
                if h_sl2 > 0:
                    sl2_data[p] = h_sl2

                h_vir = self.vir_bar.cohomology_dim(p, w)
                if h_vir > 0:
                    vir_data[p] = h_vir

            # For the DS path: we need to compute DS(H^p(B(sl_2))) at DS weight w
            ds_cohomology: Dict[int, int] = {}
            for p in range(w + 1):
                # H^p(B(sl_2)) is concentrated at original weight p(p+1)/2
                orig_w = p * (p + 1) // 2
                if orig_w > self.max_weight:
                    continue
                dim_hp = self.sl2_bar.cohomology_dim(p, orig_w)
                if dim_hp == 0:
                    continue

                # The BRST reduction of V_{2p} gives 1-dim at DS weight p(p-1)/2
                ds_w = p * (p - 1) // 2
                if ds_w == w:
                    ds_cohomology[p] = 1  # HWV extraction

            comparison[w] = {
                'weight': w,
                'sl2_cohomology': sl2_data,
                'vir_cohomology': vir_data,
                'ds_reduced_sl2': ds_cohomology,
            }

        return comparison

    # ----------------------------------------------------------------
    # h-eigenvalue analysis: what the DS functor sees
    # ----------------------------------------------------------------

    def sl2_h_eigenvalue_profile(self, weight: int) -> Dict[int, Dict[int, int]]:
        """Full h-eigenvalue decomposition at each CE degree for given weight.

        Returns {degree: {h_eigenvalue: count}}.
        """
        profile = {}
        for p in range(weight + 1):
            decomp = self.sl2_bar.h_eigenvalue_decomposition(p, weight)
            if decomp:
                profile[p] = decomp
        return profile

    # ----------------------------------------------------------------
    # BRST reduction on CE chain groups
    # ----------------------------------------------------------------

    def brst_invariant_count(self, degree: int, weight: int) -> Dict[int, int]:
        """Count BRST-invariant (h-eigenvalue = 0) states at (degree, weight).

        In the DS reduction, the BRST cohomology of a finite-dimensional
        sl_2-module extracts the subspace annihilated by the raising
        operator e.  For the CE chain group Lambda^p(sl_2_-^*)_h, this
        is the subspace with h-eigenvalue = 0 (the e-fixed points in
        the h=0 weight space), modulo the image of e.

        For a COARSER analysis: the h-eigenvalue = 0 subspace gives an
        UPPER BOUND on the BRST cohomology.

        Returns {ds_weight: count_of_h_eigenvalue_0_states}.
        """
        result: Dict[int, int] = {}
        for alpha in self.sl2_bar.weight_basis(degree, weight):
            h_sum = sum(SL2_H_EIGENVALUE[self.sl2_bar.generators[i][0]] for i in alpha)
            if h_sum == 0:
                ds_w = weight  # DS weight = original weight when h_eig = 0
                result[ds_w] = result.get(ds_w, 0) + 1
        return result

    # ----------------------------------------------------------------
    # Filtration compatibility analysis
    # ----------------------------------------------------------------

    def pbw_filtration_compatibility(self, max_weight: int = 0) -> Dict:
        """Analyze PBW filtration compatibility with DS reduction.

        The PBW filtration on V_k(sl_2) induces a filtration on B(V_k(sl_2)).
        If this filtration is compatible with the BRST differential, then
        the associated spectral sequence of the double complex
        (bar differential x BRST differential) converges to the bar
        cohomology of the DS output.

        The PBW spectral sequence for V_k(sl_2):
          E_1 = Lambda^*(sl_2_-^*) -> E_2 = H*(CE(sl_2_-)) = H*(B)

        The BRST spectral sequence for the DS reduction:
          E_1 = H*(BRST, Lambda^*(sl_2_-^*)) -> E_2 = H*(BRST, H*(CE))

        For the two to give the same answer as B(Vir_c), we need
        the double complex spectral sequence to collapse.

        This method checks whether the BRST-reduced E_1 page dimensions
        match the Virasoro CE chain dimensions (which would mean the
        spectral sequences are compatible at E_1).
        """
        if max_weight == 0:
            max_weight = self.max_weight

        results = {}
        for w in range(max_weight + 1):
            w_data = {}
            for p in range(w + 1):
                # sl_2 CE chain group at degree p, weight w
                sl2_dim = self.sl2_bar.chain_dim(p, w)
                # h-eigenvalue = 0 subspace (upper bound on BRST cohomology)
                h0_count = self.brst_invariant_count(p, w)
                # Virasoro chain group at degree p, DS weight
                # For h_eigenvalue = 0: DS weight = original weight
                vir_dim = self.vir_bar.chain_dim(p, w)

                h0_at_w = h0_count.get(w, 0)
                if sl2_dim > 0 or vir_dim > 0:
                    w_data[p] = {
                        'sl2_total': sl2_dim,
                        'sl2_h0': h0_at_w,
                        'vir': vir_dim,
                    }

            if w_data:
                results[w] = w_data

        return results


# ============================================================================
# Genus-0 DS-bar commutation evidence at the Koszul dual level
# ============================================================================

def koszul_dual_comparison() -> Dict:
    """Compare Koszul duals through the two paths.

    Path A: V_k(sl_2)^! = V_{-k-4}(sl_2) (affine Koszul dual, by
            Feigin-Frenkel involution k -> -k-2h^v = -k-4).
            Then DS(V_{-k-4}(sl_2)) = Vir_{c(-k-4)}.

    Path B: DS(V_k(sl_2)) = Vir_c.
            Vir_c^! = Vir_{26-c} (Virasoro Koszul dual).

    For DS-bar commutation at the Koszul dual level, we need:
      c(-k-4) = 26 - c(k)

    Verification: c(k) = 1 - 6(k+1)^2/(k+2).
    c(-k-4) = 1 - 6(-k-3)^2/(-k-2) = 1 + 6(k+3)^2/(k+2).
    [Sign: (-k-3)^2/(-(k+2)) = -(k+3)^2/(k+2), so the minus from
    the outer -6 gives +6(k+3)^2/(k+2).]

    26 - c(k) = 25 + 6(k+1)^2/(k+2).

    Difference: c(-k-4) - (26-c(k))
      = [1 + 6(k+3)^2/(k+2)] - [25 + 6(k+1)^2/(k+2)]
      = -24 + 6[(k+3)^2 - (k+1)^2]/(k+2)
      = -24 + 6 * 4(k+2) / (k+2)     [since (k+3)^2-(k+1)^2 = 4(k+2)]
      = -24 + 24 = 0.

    RESULT: c(-k-4) = 26-c(k) holds IDENTICALLY for all k != -2.
    DS commutes with Koszul duality at the central charge level UNIVERSALLY.
    This is a consequence of the Fateev-Lukyanov complementarity
    c(k) + c(-k-2N) = const, which for N=2 gives c(k) + c(-k-4) = 26.
    """
    test_levels = [Fraction(p) for p in [1, 2, 3, 5, 10, -3, -1]]
    results = {}
    for k in test_levels:
        try:
            c_k = c_vir_from_sl2(k)
            k_dual = -k - 4
            c_k_dual = c_vir_from_sl2(k_dual)
            c_koszul = 26 - c_k
            delta = c_k_dual - c_koszul
            results[k] = {
                'k': k,
                'c(k)': c_k,
                'k_FF_dual': k_dual,
                'c(k_FF_dual)': c_k_dual,
                '26_minus_c(k)': c_koszul,
                'delta': delta,
                'commutes_at_koszul_level': delta == 0,
            }
        except (ValueError, ZeroDivisionError):
            results[k] = {'k': k, 'error': 'singular'}
    return results


# ============================================================================
# Kappa commutation analysis
# ============================================================================

def kappa_commutation_comparison() -> Dict:
    """Compare kappa through the two DS paths.

    Path A: kappa(V_k(sl_2)) = 3(k+2)/4.
            kappa(V_{-k-4}(sl_2)) = 3(-k-4+2)/4 = 3(-k-2)/4 = -3(k+2)/4.
            So kappa + kappa' = 0 for affine sl_2 (AP24: true for KM).

    Path B: kappa(Vir_c) = c/2.
            kappa(Vir_{26-c}) = (26-c)/2.
            kappa + kappa' = 13 (AP24: true for Virasoro).

    The kappa complementarity sum CHANGES under DS:
      sl_2: kappa + kappa' = 0
      Vir:  kappa + kappa' = 13

    This is consistent with the Koszul dual mismatch found above.
    The difference 13 - 0 = 13 is the ghost sector contribution.
    """
    test_levels = [Fraction(p) for p in [1, 2, 3, 5, 10]]
    results = {}
    for k in test_levels:
        try:
            kap_sl2 = kappa_sl2(k)
            kap_sl2_dual = kappa_sl2(-k - 4)
            kap_vir = kappa_vir(k)
            kap_vir_dual = Fraction(26 - c_vir_from_sl2(k)) / 2

            results[k] = {
                'k': k,
                'kappa_sl2': kap_sl2,
                'kappa_sl2_dual': kap_sl2_dual,
                'kappa_sl2_sum': kap_sl2 + kap_sl2_dual,
                'kappa_vir': kap_vir,
                'kappa_vir_dual': kap_vir_dual,
                'kappa_vir_sum': kap_vir + kap_vir_dual,
                'complementarity_shift': (kap_vir + kap_vir_dual) - (kap_sl2 + kap_sl2_dual),
            }
        except (ValueError, ZeroDivisionError):
            results[k] = {'k': k, 'error': 'singular'}
    return results


# ============================================================================
# Explicit chain-level BRST double complex for the bar complex
# ============================================================================

class BRSTBarDoubleComplex:
    """The double complex (d_CE, d_BRST) for DS reduction of B(V_k(sl_2)).

    This is the chain-level engine for the DS-bar commutation question.

    The double complex has:
    - Horizontal differential: d_CE (bar/Chevalley-Eilenberg differential)
    - Vertical differential: d_BRST (DS/BRST differential)

    The total complex computes H*(BRST, B(V_k(sl_2))).

    If DS and bar commute, then H*(BRST, B(V_k(sl_2))) should be
    quasi-isomorphic to B(Vir_c) = B(DS(V_k(sl_2))).

    BRST DIFFERENTIAL FOR sl_2 -> Vir:
    The BRST differential acts on sl_2-modules by:
      d_BRST = c * e  (contraction with the nilpotent e)
    where c is a ghost with ghost number +1 and e is the raising operator.

    For CE chain groups Lambda^p(sl_2_-^*)_h:
    d_BRST(omega)(v_1, ..., v_p) = omega(e . v_1, v_2, ..., v_p) + ...
    i.e., it is the Lie algebra action of e on the exterior powers.

    The BRST cohomology of Lambda^p(sl_2_-^*)_h decomposes by the
    sl_2 representation theory of the chain group.  Each irreducible
    V_j contributes:
      H^0(BRST, V_j) = 1 if j = 0 (trivial), else = 0
    for finite-dimensional representations.

    Wait: for the DS reduction, the BRST complex is:
    ... -> V tensor Lambda^1(n_+^*) -> V tensor Lambda^0(n_+^*) -> 0
    with d = e.c (the action of e contracted with ghost c).

    For sl_2 with n_+ = Ce: Lambda^0(n_+^*) = C, Lambda^1(n_+^*) = C,
    and the BRST complex is:
      V -> V
    where the map is the action of e.  The BRST cohomology is:
      H^0 = V/eV = lowest weight space
      H^1 = ker(e) / image = 0 for irreducible V (since e is injective
            from V_{m-2} to V_m on irreducible V_j for m < j)

    Actually: e: V_j -> V_j maps the weight-m space to weight-(m+2) space.
    For the standard sl_2 representation V_j (dim j+1, weights -j, -j+2, ..., j):
      ker(e) = weight-j space (top weight), dim = 1
      im(e) = weights -j+2, ..., j (everything except the lowest weight)
      H^0(BRST) = ker(e on weight j space) = 1-dim (for e acting on V)

    No wait, the DS BRST cohomology for principal sl_2 reduction is:
      H^0(n_+, V) = V / n_+ V = V^{lowest weight component}

    For irreducible V_j: this is 1-dimensional (the lowest weight vector).
    The lowest weight vector has h-eigenvalue = -j.
    Its DS-modified weight = orig_weight + j/2 (since h-eig = -j gives
    grade shift +j/2).

    So for H^n(B(sl_2)) = V_{2n} at original weight n(n+1)/2:
      The LWV has h-eigenvalue = -2n.
      DS weight = n(n+1)/2 + n = n(n+3)/2.

    Cross-check for n=1: DS weight = 1*4/2 = 2.
    This should correspond to L_{-2} in the Virasoro, i.e. the generator T.
    Indeed, H^1(B(Vir))_2 = 1. MATCH.

    For n=2: DS weight = 2*5/2 = 5.
    H^2(B(sl_2)) = V_4 at weight 3.  LWV has h-eig = -4, DS wt = 3+2 = 5.
    Check: H^2(B(Vir))_5 should be 0 (weight 5 for CE degree 2 requires
    two distinct generators summing to 5, e.g. L_{-2} ^ L_{-3}, but this
    is at CE degree 2, not cohomology degree 2).
    Actually dim Lambda^2(Vir_-)_5 = 1 (just L_{-2} ^ L_{-3}).
    And dim Lambda^1(Vir_-)_5 = 1 (just L_{-5}).
    The CE differential d: Lambda^1_5 -> Lambda^2_5 maps
      d(L_{-5}^*) = ? We need the bracket: [L_{-2}, L_{-3}] = L_{-5}.
      So d(L_{-5}^*)(L_{-2}, L_{-3}) = L_{-5}^*([L_{-2}, L_{-3}]) = 1.
      So d is the 1x1 matrix [1], which has trivial kernel.
      H^1(CE)_5 = ker(d) at degree 1 = 0.
      But also: d: Lambda^0_5 -> Lambda^1_5 is 0 (since Lambda^0_5 = 0).
      So H^1_5 = dim ker(d^1_5) - dim im(d^0_5) = 0 - 0 = 0.
      And H^2_5 = dim ker(d^2_5) - dim im(d^1_5).
      d^2_5: Lambda^2_5 -> Lambda^3_5. Lambda^3_5 requires weight 5 from
      3 distinct generators >= 2, which is impossible (2+2+... but need distinct).
      Min weight for 3 generators: 2+3+4 = 9 > 5. So Lambda^3_5 = 0.
      ker(d^2_5) = Lambda^2_5 = 1-dimensional.
      im(d^1_5) = rank of d^1_5 = 1 (the 1x1 matrix [1] has rank 1).
      H^2_5 = 1 - 1 = 0.

    So H^2(B(Vir))_5 = 0.  But DS(H^2(B(sl_2))) predicts a 1-dim
    contribution at DS weight 5.

    MISMATCH AT BAR DEGREE 2, DS WEIGHT 5.

    This means DS-bar commutation FAILS at the naive cohomology level
    for bar degree >= 2.  The obstruction is:
      H^2(B(sl_2)) = V_4 (5-dimensional) with LWV at DS weight 5
      H^2(B(Vir))_5 = 0

    The DS reduction DESTROYS the bar degree 2 cohomology that sl_2 has.
    The Virasoro bar complex has NO degree-2 cohomology at weight 5.
    The DS-reduced sl_2 bar cohomology DOES (one class from the LWV of V_4).

    RESOLUTION: the commutation is NOT at the level of individual
    bar degrees.  The DS reduction REDISTRIBUTES cohomology across bar
    degrees.  The correct comparison is via the TOTAL cohomology:
      H*(BRST, H*(B(sl_2))) vs H*(B(Vir))
    where we take the TOTAL cohomology, not degree-by-degree.

    The Euler characteristic comparison IS valid and should hold.
    """

    def __init__(self, max_weight: int = 8):
        self.max_weight = max_weight
        self.sl2 = SL2BarCohomology(max_weight=max_weight)
        self.vir = VirasoroBarCohomology(max_weight=max_weight + 4)

    def ds_reduced_bar_cohomology(self) -> Dict[int, Dict]:
        """Compute DS reduction of H*(B(sl_2)) at each DS weight.

        H^n(B(sl_2)) = V_{2n} at original weight n(n+1)/2.
        DS reduction extracts LWV (h-eig = -2n) at DS weight n(n+3)/2.

        Returns {ds_weight: {bar_degree: dim}}.
        """
        result: Dict[int, Dict] = {}
        max_n = self.max_weight  # bar degree
        for n in range(1, max_n + 1):
            orig_w = n * (n + 1) // 2
            if orig_w > self.max_weight:
                break
            dim_hn = self.sl2.cohomology_dim(n, orig_w)
            if dim_hn == 0:
                continue
            # DS weight of LWV
            ds_w = n * (n + 3) // 2
            if ds_w not in result:
                result[ds_w] = {}
            result[ds_w][n] = 1  # 1-dim from LWV extraction
        return result

    def vir_bar_cohomology_table(self, max_weight: int = 0) -> Dict[int, Dict[int, int]]:
        """Complete Virasoro bar cohomology at each (weight, degree)."""
        if max_weight == 0:
            max_weight = self.max_weight + 4
        result: Dict[int, Dict[int, int]] = {}
        for w in range(max_weight + 1):
            for p in range(w // 2 + 1):
                dim_hp = self.vir.cohomology_dim(p, w)
                if dim_hp > 0:
                    if w not in result:
                        result[w] = {}
                    result[w][p] = dim_hp
        return result

    def full_comparison(self) -> Dict:
        """Full comparison of DS-reduced bar vs Virasoro bar cohomology.

        Returns detailed analysis including:
        - Where the two paths agree
        - Where they disagree
        - The structural obstruction
        """
        ds_reduced = self.ds_reduced_bar_cohomology()
        vir_table = self.vir_bar_cohomology_table()

        all_weights = sorted(set(list(ds_reduced.keys()) + list(vir_table.keys())))

        comparison = {}
        for w in all_weights:
            ds_data = ds_reduced.get(w, {})
            vir_data = vir_table.get(w, {})

            # Total dimension at this weight
            ds_total = sum(ds_data.values())
            vir_total = sum(vir_data.values())

            comparison[w] = {
                'ds_weight': w,
                'ds_reduced_cohomology': dict(ds_data),
                'vir_cohomology': dict(vir_data),
                'ds_total_dim': ds_total,
                'vir_total_dim': vir_total,
                'match_total': ds_total == vir_total,
                'match_graded': ds_data == vir_data,
            }

        return comparison

    def euler_char_total_comparison(self, max_weight: int = 0) -> Dict:
        """Compare total Euler characteristics through both paths.

        The generating function comparison:
          sum_w chi(DS(B(sl_2)))_w * q^w  vs  sum_w chi(B(Vir))_w * q^w

        If these agree as formal power series, DS-bar commutation holds
        at the Euler characteristic level (i.e. in the Grothendieck group).
        """
        if max_weight == 0:
            max_weight = self.max_weight + 4

        comparison = DSBarComparison(max_weight=self.max_weight)
        result = {}
        for w in range(max_weight + 1):
            chi_vir = self.vir.euler_char(w)
            chi_sl2_ds = comparison.sl2_ds_modified_euler_char(w)
            result[w] = {
                'weight': w,
                'chi_sl2_ds': chi_sl2_ds,
                'chi_vir': chi_vir,
                'match': chi_sl2_ds == chi_vir,
            }
        return result


# ============================================================================
# Genus-1 kappa comparison
# ============================================================================

def genus1_kappa_comparison() -> Dict:
    """Compare genus-1 obstruction through the two paths.

    For DS-bar commutation at genus 1:
      Path A: kappa(V_k(sl_2)) goes through DS to kappa(Vir_c)
      Path B: kappa(Vir_c) computed directly

    At genus 1: obs_1 = kappa * lambda_1.
    kappa(sl_2) = 3(k+2)/4.
    kappa(Vir_c) = c/2 = [1 - 6(k+1)^2/(k+2)] / 2.

    The DS ghost sector contributes kappa_ghost.
    kappa_ghost = c_ghost / 2.
    c_ghost = c(sl_2) - c(Vir) = 3k/(k+2) - 1 + 6(k+1)^2/(k+2)
            = [3k + 6(k+1)^2 - (k+2)] / (k+2)
            = [3k + 6k^2 + 12k + 6 - k - 2] / (k+2)
            = [6k^2 + 14k + 4] / (k+2)
            = 2(3k^2 + 7k + 2) / (k+2)
            = 2(3k+1)(k+2) / (k+2)
            = 2(3k+1)

    So c_ghost = 2(3k+1), kappa_ghost = 3k+1.
    kappa(sl_2) = 3(k+2)/4.
    kappa(Vir) = c(Vir)/2.
    kappa_ghost = (3k+1).

    Check: kappa(Vir) + kappa_ghost = c(Vir)/2 + (3k+1)
         = [1 - 6(k+1)^2/(k+2)] / 2 + 3k + 1
         = 1/2 - 3(k+1)^2/(k+2) + 3k + 1
         = 3k + 3/2 - 3(k^2+2k+1)/(k+2)
         = 3k + 3/2 - (3k^2+6k+3)/(k+2)
         = [3k(k+2) + 3(k+2)/2 - 3k^2 - 6k - 3] / (k+2)
         = [3k^2 + 6k + 3k/2 + 3 - 3k^2 - 6k - 3] / (k+2)

    This is getting complicated. Let me just compute numerically.
    """
    results = {}
    test_levels = [Fraction(p) for p in [1, 2, 3, 5, 10, 20, 100]]
    for k in test_levels:
        try:
            c_aff = c_sl2(k)
            c_v = c_vir_from_sl2(k)
            c_gh = c_aff - c_v

            kap_aff = kappa_sl2(k)
            kap_v = kappa_vir(k)
            kap_gh = c_gh / 2

            # Test: does kappa(sl_2) = kappa(Vir) + kappa_ghost?
            rhs = kap_v + kap_gh
            diff = kap_aff - rhs

            results[k] = {
                'k': k,
                'c_sl2': c_aff,
                'c_vir': c_v,
                'c_ghost': c_gh,
                'kappa_sl2': kap_aff,
                'kappa_vir': kap_v,
                'kappa_ghost': kap_gh,
                'kappa_sum': rhs,
                'additivity_diff': diff,
                'kappa_additive': diff == 0,
            }
        except (ValueError, ZeroDivisionError):
            results[k] = {'k': k, 'error': 'singular'}
    return results


# ============================================================================
# Ghost sector Hilbert series (for full double complex)
# ============================================================================

def ghost_euler_char(weight: int) -> Fraction:
    """Euler characteristic of the bc ghost system at conformal weight.

    For sl_2 -> Vir (principal DS), the ghost system has one bc pair
    with b at weight 1 and c at weight 0.

    The ghost Fock space at weight h has dimension counting the number
    of monomials in {b_{-n} : n >= 1} and {c_{-n} : n >= 1} with
    total weight h and definite ghost number.

    Actually: the bc ghost for the DS reduction of sl_2 has:
      b at conformal weight 1 (positive root has grade 1)
      c at conformal weight 0

    The ghost partition function is:
      prod_{n>=1} (1 + q^n)^2 / prod_{n>=1} (1 - q^n)^0
    Wait: bc ghosts are fermionic, so:
      Z_ghost(q) = prod_{n>=0} (1 + q^n) * prod_{n>=1} (1 + q^n)
                 = (1+1) * prod_{n>=1} (1 + q^n)^2

    For the Euler characteristic (with ghost number grading):
      chi_ghost(q) = prod_{n>=0} (1 - q^n) * prod_{n>=1} (1 - q^n)
    No, the Euler characteristic with respect to ghost number is:
      chi(q) = Tr((-1)^{ghost number} q^{L_0})

    For one bc pair with b weight 1, c weight 0:
      chi(q) = prod_{n>=1} (1 - q^n) * (1 - q^{n-1})
    Hmm, this is getting into conformal field theory specifics.

    For the purposes of this engine, we compute the ghost contribution
    to the Euler characteristic as a correction factor.

    The key fact: for principal DS sl_2 -> Vir with one bc pair,
    the ghost sector Euler characteristic is:
      chi_ghost(q) = (1-1) * prod_{n>=1}(1-q^n)(1-q^n) = 0

    Wait: c_0 has weight 0 and the c zero mode c_0 gives (1 + q^0) = 2
    in the partition function but (1 - q^0) = 0 in the Euler characteristic.
    So the ghost Euler characteristic is IDENTICALLY ZERO (the c_0 zero
    mode kills it).

    This is the standard result: the BRST reduction selects a specific
    ghost number, and the Euler characteristic over all ghost numbers
    vanishes due to the zero mode.

    For the DS-bar comparison: we must fix the ghost number (to 0) and
    then compare.  The ghost-number-0 sector gives the physical states.
    """
    # Ghost contribution at fixed ghost number 0
    # For one bc pair, ghost number 0 means equal b and c occupation
    # This is computed by taking the constant term in the ghost number
    # expansion of the partition function.
    #
    # For simplicity at this stage, return the partition function
    # coefficient of the ghost-number-0 sector.
    if weight == 0:
        return Fraction(1)
    if weight == 1:
        return Fraction(1)  # b_{-1} c_0 at ghost number 0

    # For higher weights: count states with equal b and c occupation
    # at the given conformal weight.
    # This is the coefficient of z^0 q^weight in
    # prod_{n>=0} (1 + z q^n) * prod_{n>=1} (1 + z^{-1} q^n)
    # where z tracks ghost number.

    # For practical computation, enumerate the states.
    count = Fraction(0)
    max_mode = weight + 1
    # b modes: b_{-1}, b_{-2}, ..., b_{-max_mode} at weights 1, 2, ...
    # c modes: c_0, c_{-1}, c_{-2}, ... at weights 0, 1, 2, ...
    # Ghost number: each b contributes +1, each c contributes -1.
    # Ghost number 0 means #b = #c.

    # Enumerate subsets of b modes and c modes with equal cardinality
    # and total weight = weight.
    b_modes = list(range(1, weight + 1))  # b_{-n} has weight n
    c_modes = list(range(0, weight + 1))  # c_{-n} has weight n

    for nb in range(min(len(b_modes), weight) + 1):
        for b_subset in combinations(b_modes, nb):
            b_weight = sum(b_subset)
            if b_weight > weight:
                continue
            c_weight_needed = weight - b_weight
            # Need nc = nb c-modes with total weight = c_weight_needed
            for c_subset in combinations(c_modes, nb):
                if sum(c_subset) == c_weight_needed:
                    count += 1

    return count


# ============================================================================
# Master comparison function
# ============================================================================

def ds_bar_commutation_evidence(max_weight: int = 6) -> Dict:
    """Compute all evidence for DS-bar commutation at sl_2 -> Vir.

    Returns a comprehensive analysis including:
    1. Central charge and kappa comparison
    2. Euler characteristic comparison
    3. Chain-level dimension comparison
    4. Cohomology comparison (bar-degree by bar-degree)
    5. Koszul dual comparison
    6. Filtration compatibility analysis
    7. Double complex structure

    The key question: does B(DS(-)) agree with DS(B(-)) up to
    quasi-isomorphism?
    """
    result = {}

    # 1. Central charge / kappa
    result['kappa'] = genus1_kappa_comparison()

    # 2. Koszul dual comparison
    result['koszul_dual'] = koszul_dual_comparison()

    # 3. Kappa commutation
    result['kappa_commutation'] = kappa_commutation_comparison()

    # 4. Euler characteristic comparison
    comp = DSBarComparison(max_weight=max_weight)
    result['euler_chars'] = comp.euler_char_comparison(max_ds_weight=max_weight + 2)

    # 5. Chain dimension comparison
    result['chain_dims'] = comp.chain_dim_comparison(max_weight=max_weight)

    # 6. Double complex comparison
    dc = BRSTBarDoubleComplex(max_weight=max_weight)
    result['cohomology'] = dc.full_comparison()

    # 7. Filtration analysis
    result['filtration'] = comp.pbw_filtration_compatibility(max_weight=max_weight)

    return result


# ============================================================================
# Verification constants
# ============================================================================

# Known bar cohomology of V_k(sl_2):
# H^n concentrated at weight n(n+1)/2, dim H^n = 2n+1
SL2_BAR_COHOMOLOGY = {
    1: {'weight': 1, 'dim': 3},     # H^1 at weight 1
    2: {'weight': 3, 'dim': 5},     # H^2 at weight 3 (corrected from Riordan)
    3: {'weight': 6, 'dim': 7},     # H^3 at weight 6
    4: {'weight': 10, 'dim': 9},    # H^4 at weight 10
}

# Known bar cohomology of Vir_c:
# H^1 at weights 2, 3, 4 (the three generator modes L_{-2}, L_{-3}, L_{-4})
VIRASORO_BAR_H1 = {2: 1, 3: 1, 4: 1}

# DS weight mapping for LWV extraction:
# H^n(B(sl_2)) -> DS weight n(n+3)/2
DS_WEIGHT_MAP = {
    1: 2,    # n=1: DS weight = 1*4/2 = 2
    2: 5,    # n=2: DS weight = 2*5/2 = 5
    3: 9,    # n=3: DS weight = 3*6/2 = 9
}

# Central charge at specific levels
CENTRAL_CHARGE_VALUES = {
    Fraction(1): {'c_sl2': Fraction(1), 'c_vir': Fraction(-7)},
    Fraction(2): {'c_sl2': Fraction(3, 2), 'c_vir': Fraction(-25, 2)},
    Fraction(-3): {'c_sl2': Fraction(9), 'c_vir': Fraction(25)},
}
