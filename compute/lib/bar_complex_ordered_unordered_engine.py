r"""Ordered (E_1) vs unordered bar complex: explicit chain-level comparison.

MATHEMATICAL FRAMEWORK:

The bar complex of a chiral algebra A has two variants:

1. ORDERED BAR COMPLEX B^{ord}(A):
   B^{ord,n} = (s^{-1}A_bar)^{\otimes n}
   This is the Hochschild-type complex: full tensor products, no quotienting
   by the symmetric group action. The differential uses the ORDERED
   positions of tensor factors. The E_1 page of the PBW spectral sequence
   computes Hochschild homology of the enveloping algebra.

2. UNORDERED BAR COMPLEX B^{un}(A):
   B^{un,n} = \Lambda^n(s^{-1}A_bar)   (for bosonic generators)
   This is the Chevalley-Eilenberg complex: exterior powers, with the
   antisymmetric tensor structure. The differential is the CE differential
   dual to the Lie bracket. This is what the PBW-collapsed bar complex
   computes for Koszul algebras.

KEY DISTINCTION (AP37): The ordered bar is a TENSOR construction (Hochschild),
the unordered bar is an EXTERIOR construction (Chevalley-Eilenberg). In char 0,
the antisymmetrization map pi: B^{ord} -> B^{un} is a quasi-isomorphism
(Loday-Quillen-Tsygan / HKR theorem). But as chain complexes they are DIFFERENT:
- B^{ord,n} has dimension dim(V)^n (full tensor power)
- B^{un,n} has dimension C(dim(V), n) (binomial coefficient)

For affine KM at level k, with Lie algebra g of dimension d:
  The loop algebra g_- = g \otimes t^{-1}C[t^{-1}] has infinitely many
  generators (a, m) for a in g, m >= 1. At conformal weight h:
  - Ordered: tensor products of generators with total weight h
  - Unordered: exterior products (subsets) of generators with total weight h

THE S_n ACTION on B^{ord,n}:
  The symmetric group S_n acts on (s^{-1}V)^{\otimes n} by permuting
  tensor factors with Koszul signs. For degree-p elements in s^{-1}V
  (where p = original_degree - 1 by desuspension), swapping adjacent
  factors of degrees p_i and p_{i+1} gives sign (-1)^{p_i * p_{i+1}}.

  For weight-1 generators (e.g., sl_2 currents): s^{-1}v has degree 0,
  so all permutations act WITHOUT signs. The S_n-irrep decomposition of
  V^{\otimes n} is the Schur decomposition.

  For weight-2 generators (e.g., Virasoro T): s^{-1}T has degree 1,
  so transpositions act with sign (-1)^{1*1} = -1. The S_n action on
  (s^{-1}V)^{\otimes n} is the SIGN representation tensored with the
  natural permutation action.

SWISS-CHEESE STRUCTURE:
  The ordered bar carries BOTH:
  (a) C-direction factorization (the bar differential d_bar)
  (b) R-direction ordering (the deconcatenation coproduct Delta)
  The unordered bar keeps only (a). The coproduct on the unordered bar
  is cocommutative (since we quotient by S_n). The ORDERED coproduct
  Delta: B^{ord,n} -> sum_{p+q=n} B^{ord,p} \otimes B^{ord,q}
  is NOT cocommutative -- it distinguishes "first p" from "last q".

DK BRIDGE (MC3) IMPLICATION:
  The Yangian/quantum group structure comes from the ORDERED bar complex.
  The R-matrix R(z) lives in End(V \otimes V), acting on B^{ord,2}.
  The Yang-Baxter equation is a relation in B^{ord,3}.
  The unordered bar sees only the COMMUTATIVE part: the classical r-matrix
  r(z) in S^2(V) (symmetric part of V \otimes V, after accounting for
  desuspension signs). The full quantum R-matrix R = 1 + r/z + ... has
  non-symmetric corrections that live in the ordered-but-not-unordered part.

References:
  bar_complex.py: OPE algebra infrastructure
  bar_cohomology_sl2_explicit_engine.py: CE (unordered) computation for sl_2
  bar_cohomology_virasoro_explicit_engine.py: CE computation for Virasoro
  AP37: Lie homology (exterior) != Hochschild homology (tensor)
  AP45: desuspension lowers degree: |s^{-1}v| = |v| - 1
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product as iproduct
from math import factorial, comb
from typing import Dict, List, Optional, Tuple

import numpy as np


# ============================================================
# Exact rational arithmetic helpers
# ============================================================

def _frac(x) -> Fraction:
    """Coerce to Fraction."""
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, np.integer)):
        return Fraction(int(x))
    return Fraction(x)


def _frac_array(shape) -> np.ndarray:
    """Create a zero array of Fraction objects."""
    arr = np.empty(shape, dtype=object)
    arr.fill(Fraction(0))
    return arr


# ============================================================
# Generator and algebra data
# ============================================================

class LoopGenerator:
    """A generator (a, n) of g_- with Lie index a and mode n >= 1."""
    __slots__ = ('lie_idx', 'mode', 'flat_idx', 'desuspended_degree')

    def __init__(self, lie_idx: int, mode: int, flat_idx: int,
                 conformal_weight: int = 1):
        self.lie_idx = lie_idx
        self.mode = mode  # conformal weight of this generator
        self.flat_idx = flat_idx
        # Desuspension: |s^{-1}v| = |v| - 1 (AP45)
        # For weight-1 generators: desuspended degree = 0
        # For weight-2 generators: desuspended degree = 1
        self.desuspended_degree = conformal_weight - 1

    def __repr__(self):
        return f"g({self.lie_idx},{self.mode})#{self.flat_idx}"


# ============================================================
# sl_2 data
# ============================================================

DIM_SL2 = 3

# [e,f] = h, [h,e] = 2e, [h,f] = -2f
SL2_BRACKET: Dict[Tuple[int, int], Dict[int, Fraction]] = {
    (0, 2): {1: Fraction(1)},    # [e, f] = h
    (2, 0): {1: Fraction(-1)},   # [f, e] = -h
    (1, 0): {0: Fraction(2)},    # [h, e] = 2e
    (0, 1): {0: Fraction(-2)},   # [e, h] = -2e
    (1, 2): {2: Fraction(-2)},   # [h, f] = -2f
    (2, 1): {2: Fraction(2)},    # [f, h] = 2f
}


# ============================================================
# Virasoro data: Vir_- = {L_{-n} : n >= 2}
# ============================================================

def vir_bracket(m: int, n: int) -> Fraction:
    """[L_{-m}, L_{-n}] = (n - m) L_{-(m+n)}.

    For m, n >= 2. No central extension since m+n >= 4 > 0.
    Returns the coefficient of L_{-(m+n)}.
    """
    return Fraction(n - m)


# ============================================================
# Ordered bar complex engine
# ============================================================

class OrderedUnorderedBarEngine:
    """Engine comparing ordered and unordered bar complexes.

    For a loop algebra g_- with bracket data, computes:
    1. Ordered bar: full tensor products at each (bar_degree, weight)
    2. Unordered bar: exterior products (subsets) at each (bar_degree, weight)
    3. S_n action on the ordered bar and irrep decomposition
    4. Antisymmetrization map and quasi-isomorphism verification
    5. Differentials on both complexes and cohomology comparison
    """

    def __init__(self, algebra_type: str = 'sl2', max_weight: int = 8):
        """Initialize the engine.

        Args:
            algebra_type: 'sl2' or 'virasoro'
            max_weight: maximum conformal weight to include
        """
        self.algebra_type = algebra_type
        self.max_weight = max_weight

        if algebra_type == 'sl2':
            self._init_sl2()
        elif algebra_type == 'virasoro':
            self._init_virasoro()
        else:
            raise ValueError(f"Unknown algebra type: {algebra_type}")

        # Build bracket table for all pairs
        self._build_bracket_table()

        # Caches
        self._ordered_basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}
        self._unordered_basis_cache: Dict[Tuple[int, int], List[Tuple[int, ...]]] = {}

    def _init_sl2(self):
        """Initialize sl_2 loop algebra generators."""
        self.dim_g = DIM_SL2
        self.gen_conf_weight = 1  # all generators have conformal weight 1
        self.generators: List[LoopGenerator] = []
        idx = 0
        for n in range(1, self.max_weight + 1):
            for a in range(self.dim_g):
                self.generators.append(
                    LoopGenerator(a, n, idx, conformal_weight=1))
                idx += 1
        self.n_gens = len(self.generators)
        self._lie_bracket = SL2_BRACKET

    def _init_virasoro(self):
        """Initialize Virasoro negative-mode algebra generators."""
        self.dim_g = 1  # single generator T per mode
        self.gen_conf_weight = 2  # T has conformal weight 2
        self.generators: List[LoopGenerator] = []
        idx = 0
        # L_{-n} for n >= 2, with conformal weight n
        for n in range(2, self.max_weight + 1):
            self.generators.append(
                LoopGenerator(0, n, idx, conformal_weight=2))
            idx += 1
        self.n_gens = len(self.generators)

    def _build_bracket_table(self):
        """Build bracket lookup for pairs of generator flat indices."""
        self._bracket_table: Dict[Tuple[int, int], Dict[int, Fraction]] = {}

        if self.algebra_type == 'sl2':
            for i in range(self.n_gens):
                gi = self.generators[i]
                for j in range(self.n_gens):
                    if i == j:
                        continue
                    gj = self.generators[j]
                    m_sum = gi.mode + gj.mode
                    if m_sum > self.max_weight:
                        continue
                    br = self._lie_bracket.get((gi.lie_idx, gj.lie_idx))
                    if br:
                        result = {}
                        for c, coeff in br.items():
                            flat_c = c + self.dim_g * (m_sum - 1)
                            if flat_c < self.n_gens:
                                result[flat_c] = _frac(coeff)
                        if result:
                            self._bracket_table[(i, j)] = result

        elif self.algebra_type == 'virasoro':
            for i in range(self.n_gens):
                gi = self.generators[i]
                mi = gi.mode  # L_{-mi}
                for j in range(self.n_gens):
                    if i == j:
                        continue
                    gj = self.generators[j]
                    mj = gj.mode  # L_{-mj}
                    m_sum = mi + mj
                    if m_sum > self.max_weight or m_sum < 2:
                        continue
                    coeff = vir_bracket(mi, mj)
                    if coeff != Fraction(0):
                        # Output: L_{-(mi+mj)}, flat index = m_sum - 2
                        flat_c = m_sum - 2
                        if flat_c < self.n_gens:
                            self._bracket_table[(i, j)] = {flat_c: coeff}

    # ============================================================
    # Basis enumeration
    # ============================================================

    def gen_weight(self, idx: int) -> int:
        """Conformal weight of generator at flat index idx."""
        return self.generators[idx].mode

    def ordered_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of B^{ord,degree}_weight = ordered degree-tuples of generators.

        Returns list of tuples (i_1, ..., i_degree) of generator flat indices
        (with repetitions allowed for Hochschild, but NOT for the bar complex
        of a Lie algebra -- the ordered bar is Lambda^n for the CE complex).

        CORRECTION: For the ORDERED bar complex of a chiral algebra on P^1,
        the relevant object is the TENSOR power, not the exterior power.
        The Arnold relations reduce the full tensor power, but at the E_1
        level (before Arnold), we have full tensor products.

        For comparison purposes, we compute the FULL ordered tensor product
        (sequences with repetition) and the EXTERIOR/SUBSET version separately.
        The actual chiral bar complex lies between these two via Arnold relations.

        Here we compute: ordered sequences (i_1, ..., i_degree) with
        i_1, ..., i_degree distinct (exterior part of tensor), and
        total weight = sum of generator weights.
        """
        key = (degree, weight)
        if key in self._ordered_basis_cache:
            return self._ordered_basis_cache[key]

        result = []
        self._enum_ordered(degree, weight, 0, [], result)
        self._ordered_basis_cache[key] = result
        return result

    def _enum_ordered(self, remaining: int, remaining_weight: int,
                      min_idx: int, current: list, result: list):
        """Enumerate ordered sequences of distinct generators with given weight.

        For the ordered bar, we use PERMUTATIONS of subsets (ordered tuples
        of distinct elements). This gives degree! * C(N, degree) basis elements
        at maximum, filtered by weight.
        """
        if remaining == 0:
            if remaining_weight == 0:
                result.append(tuple(current))
            return
        if remaining_weight <= 0 and remaining > 0:
            return

        # For ordered: we pick from ALL generators, but each generator
        # can appear at most once (exterior). The ordering matters.
        # We enumerate subsets first, then permutations.
        # Actually, let's enumerate all ordered tuples of distinct elements directly.
        used = set(current)
        for i in range(self.n_gens):
            if i in used:
                continue
            w = self.gen_weight(i)
            if w > remaining_weight:
                continue
            current.append(i)
            self._enum_ordered(remaining - 1, remaining_weight - w,
                               min_idx, current, result)
            current.pop()

    def unordered_basis(self, degree: int, weight: int) -> List[Tuple[int, ...]]:
        """Basis of B^{un,degree}_weight = unordered degree-subsets of generators.

        Returns sorted list of degree-element subsets (as sorted tuples)
        of generator flat indices with total weight = weight.
        """
        key = (degree, weight)
        if key in self._unordered_basis_cache:
            return self._unordered_basis_cache[key]

        result = []
        self._enum_unordered(degree, weight, 0, [], result)
        self._unordered_basis_cache[key] = result
        return result

    def _enum_unordered(self, remaining: int, remaining_weight: int,
                        start: int, current: list, result: list):
        """Enumerate sorted subsets of generators with given total weight."""
        if remaining == 0:
            if remaining_weight == 0:
                result.append(tuple(current))
            return
        if remaining_weight <= 0 and remaining > 0:
            return

        for i in range(start, self.n_gens):
            w = self.gen_weight(i)
            if w > remaining_weight:
                continue
            current.append(i)
            self._enum_unordered(remaining - 1, remaining_weight - w,
                                 i + 1, current, result)
            current.pop()

    # ============================================================
    # Dimension computation
    # ============================================================

    def ordered_dim(self, degree: int, weight: int) -> int:
        """Dimension of ordered bar at (degree, weight)."""
        return len(self.ordered_basis(degree, weight))

    def unordered_dim(self, degree: int, weight: int) -> int:
        """Dimension of unordered bar at (degree, weight)."""
        return len(self.unordered_basis(degree, weight))

    def dimension_table(self, max_degree: int, max_wt: int
                        ) -> Dict[Tuple[int, int], Tuple[int, int]]:
        """Table of (ordered_dim, unordered_dim) at each (degree, weight)."""
        table = {}
        for n in range(1, max_degree + 1):
            for h in range(n, max_wt + 1):
                d_ord = self.ordered_dim(n, h)
                d_un = self.unordered_dim(n, h)
                if d_ord > 0 or d_un > 0:
                    table[(n, h)] = (d_ord, d_un)
        return table

    # ============================================================
    # S_n action on ordered bar
    # ============================================================

    def koszul_sign(self, perm: Tuple[int, ...],
                    degrees: List[int]) -> Fraction:
        """Koszul sign of permutation acting on elements of given degrees.

        For sigma in S_n acting on v_1 tensor ... tensor v_n,
        the sign is (-1)^{sum of |v_i|*|v_j| for (i,j) inverted by sigma}.

        An inversion is a pair (i, j) with i < j but sigma(i) > sigma(j).
        For the desuspended bar complex, |s^{-1}v| = |v| - 1.
        """
        sign = Fraction(1)
        n = len(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    # Inversion: elements at positions i and j are swapped
                    sign *= Fraction(-1) ** (degrees[perm[i]] * degrees[perm[j]])
        return sign

    def sn_action_matrix(self, degree: int, weight: int, sigma: Tuple[int, ...]
                         ) -> np.ndarray:
        """Matrix of sigma in S_degree acting on B^{ord,degree}_weight.

        sigma is given as a tuple (sigma(0), sigma(1), ..., sigma(degree-1)).
        The action permutes tensor factors with Koszul signs.
        """
        basis = self.ordered_basis(degree, weight)
        n = len(basis)
        if n == 0:
            return _frac_array((0, 0))

        # Build index lookup
        basis_idx = {b: i for i, b in enumerate(basis)}
        mat = _frac_array((n, n))

        for col, b in enumerate(basis):
            # Apply sigma: permute the tuple entries
            new_tuple = tuple(b[sigma[i]] for i in range(degree))

            # Koszul sign: depends on desuspended degrees of the generators
            degs = [self.generators[b[k]].desuspended_degree for k in range(degree)]
            sign = self.koszul_sign(sigma, degs)

            row = basis_idx.get(new_tuple)
            if row is not None:
                mat[row, col] += sign

        return mat

    def sn_character(self, degree: int, weight: int) -> Dict[Tuple[int, ...], Fraction]:
        """Character of S_degree on B^{ord,degree}_weight.

        Returns {cycle_type: trace} where cycle_type is a sorted partition.
        For full irrep decomposition we compute traces of class representatives.
        """
        if degree > 5:
            return {}  # too expensive

        from itertools import permutations as iterperms

        basis = self.ordered_basis(degree, weight)
        n = len(basis)
        if n == 0:
            return {}

        # Group permutations by cycle type
        cycle_types: Dict[Tuple[int, ...], List[Tuple[int, ...]]] = {}
        for perm in iterperms(range(degree)):
            ct = self._cycle_type(perm)
            if ct not in cycle_types:
                cycle_types[ct] = []
            cycle_types[ct].append(perm)

        result = {}
        for ct, perms in cycle_types.items():
            # Pick one representative and compute trace
            sigma = perms[0]
            mat = self.sn_action_matrix(degree, weight, sigma)
            tr = sum(mat[i, i] for i in range(n))
            result[ct] = _frac(tr)

        return result

    @staticmethod
    def _cycle_type(perm: Tuple[int, ...]) -> Tuple[int, ...]:
        """Cycle type of a permutation, as a sorted partition."""
        n = len(perm)
        visited = [False] * n
        cycles = []
        for i in range(n):
            if visited[i]:
                continue
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
                length += 1
            cycles.append(length)
        return tuple(sorted(cycles, reverse=True))

    def sn_irrep_decomposition(self, degree: int, weight: int
                               ) -> Dict[Tuple[int, ...], int]:
        """Decompose the S_n representation on B^{ord,n}_weight into irreps.

        Uses character inner products. Returns {partition: multiplicity}.
        Only implemented for degree <= 4 (we hardcode character tables).
        """
        char = self.sn_character(degree, weight)
        if not char:
            return {}

        if degree == 1:
            # S_1 is trivial
            total = char.get((1,), Fraction(0))
            if total != Fraction(0):
                return {(1,): int(total)}
            return {}

        elif degree == 2:
            # S_2: trivial (2) and sign (1,1)
            # Class (2): identity -> trace = dim
            # Class (1,1): transposition -> trace
            tr_id = char.get((2,), Fraction(0))  # cycle type (2) = identity? No!
            # Cycle type of identity (0,1) -> (1,1)
            # Cycle type of (1,0) -> (2)
            tr_id = char.get((1, 1), Fraction(0))  # identity has cycle type (1,1)
            tr_swap = char.get((2,), Fraction(0))  # transposition has cycle type (2)

            # Trivial: chi = 1, 1
            # Sign: chi = 1, -1
            mult_triv = (tr_id + tr_swap) / Fraction(2)
            mult_sign = (tr_id - tr_swap) / Fraction(2)
            result = {}
            if mult_triv != Fraction(0):
                result[(2,)] = int(mult_triv)
            if mult_sign != Fraction(0):
                result[(1, 1)] = int(mult_sign)
            return result

        elif degree == 3:
            # S_3 character table:
            # Class sizes: (1^3):1, (2,1):3, (3):2
            # Trivial (3):     1, 1, 1
            # Sign (1^3):      1, -1, 1
            # Standard (2,1):  2, 0, -1
            tr_111 = char.get((1, 1, 1), Fraction(0))  # identity
            tr_21 = char.get((2, 1), Fraction(0))       # transposition
            tr_3 = char.get((3,), Fraction(0))           # 3-cycle

            order = Fraction(6)
            mult_triv = (tr_111 + Fraction(3) * tr_21 + Fraction(2) * tr_3) / order
            mult_sign = (tr_111 - Fraction(3) * tr_21 + Fraction(2) * tr_3) / order
            mult_std = (Fraction(2) * tr_111 - Fraction(2) * tr_3) / order

            result = {}
            if mult_triv != Fraction(0):
                result[(3,)] = int(mult_triv)
            if mult_sign != Fraction(0):
                result[(1, 1, 1)] = int(mult_sign)
            if mult_std != Fraction(0):
                result[(2, 1)] = int(mult_std)
            return result

        elif degree == 4:
            # S_4 character table:
            # Classes: (1^4):1, (2,1^2):6, (2^2):3, (3,1):8, (4):6
            # Partitions: (4), (3,1), (2,2), (2,1,1), (1,1,1,1)
            # Characters (rows = irreps, cols = classes):
            #   (4):       1,  1,  1,  1,  1
            #   (3,1):     3,  1, -1,  0, -1
            #   (2,2):     2,  0,  2, -1,  0
            #   (2,1,1):   3, -1, -1,  0,  1
            #   (1^4):     1, -1,  1,  1, -1

            tr_1111 = char.get((1, 1, 1, 1), Fraction(0))
            tr_211 = char.get((2, 1, 1), Fraction(0))
            tr_22 = char.get((2, 2), Fraction(0))
            tr_31 = char.get((3, 1), Fraction(0))
            tr_4 = char.get((4,), Fraction(0))

            class_sizes = [Fraction(1), Fraction(6), Fraction(3),
                           Fraction(8), Fraction(6)]
            traces = [tr_1111, tr_211, tr_22, tr_31, tr_4]
            order = Fraction(24)

            # Character table rows
            chi_table = [
                [1, 1, 1, 1, 1],        # (4) = trivial
                [3, 1, -1, 0, -1],       # (3,1) = standard
                [2, 0, 2, -1, 0],        # (2,2)
                [3, -1, -1, 0, 1],       # (2,1,1)
                [1, -1, 1, 1, -1],       # (1^4) = sign
            ]
            partitions = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]

            result = {}
            for row_idx, part in enumerate(partitions):
                mult = Fraction(0)
                for col_idx in range(5):
                    mult += class_sizes[col_idx] * Fraction(chi_table[row_idx][col_idx]) * traces[col_idx]
                mult /= order
                if mult != Fraction(0):
                    result[part] = int(mult)
            return result

        return {}

    # ============================================================
    # Antisymmetrization map
    # ============================================================

    def antisymmetrization_matrix(self, degree: int, weight: int) -> np.ndarray:
        """Matrix of the antisymmetrization map pi: B^{ord} -> B^{un}.

        pi(v_1 tensor ... tensor v_n) = (1/n!) sum_{sigma in S_n} sgn(sigma) * v_{sigma(1)} tensor ... tensor v_{sigma(n)}

        where sgn includes the Koszul sign.

        The matrix has rows indexed by unordered basis, columns by ordered basis.
        """
        ord_basis = self.ordered_basis(degree, weight)
        un_basis = self.unordered_basis(degree, weight)
        n_ord = len(ord_basis)
        n_un = len(un_basis)

        if n_ord == 0 or n_un == 0:
            return _frac_array((max(n_un, 0), max(n_ord, 0)))

        un_idx = {b: i for i, b in enumerate(un_basis)}
        mat = _frac_array((n_un, n_ord))

        for col, b_ord in enumerate(ord_basis):
            # The ordered tuple b_ord = (i_1, ..., i_n) maps to
            # the sorted version (unordered) with a sign.
            sorted_b = tuple(sorted(b_ord))
            row = un_idx.get(sorted_b)
            if row is None:
                continue  # should not happen if basis is consistent

            # Compute the sign: the Koszul sign of the sorting permutation
            # Find permutation that sorts b_ord
            indexed = list(enumerate(b_ord))
            indexed_sorted = sorted(indexed, key=lambda x: x[1])
            # The permutation sigma satisfies b_ord[sigma[i]] = sorted_b[i]
            # We need the sign of this permutation, weighted by degrees
            perm = [x[0] for x in indexed_sorted]
            degs = [self.generators[b_ord[k]].desuspended_degree
                    for k in range(degree)]

            # Count inversions with Koszul signs
            sign = Fraction(1)
            for i in range(degree):
                for j in range(i + 1, degree):
                    if perm[i] > perm[j]:
                        sign *= Fraction(-1) ** (degs[perm[i]] * degs[perm[j]])

            mat[row, col] += sign / Fraction(factorial(degree))

        return mat

    # ============================================================
    # CE differential (unordered)
    # ============================================================

    def ce_differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        """CE differential d: Lambda^degree -> Lambda^{degree+1} at given weight.

        This is the differential on the UNORDERED bar complex.
        Returns matrix with Fraction entries.
        """
        source = self.unordered_basis(degree, weight)
        target = self.unordered_basis(degree + 1, weight)
        n_src, n_tgt = len(source), len(target)

        if n_src == 0 or n_tgt == 0:
            return _frac_array((max(n_tgt, 0), max(n_src, 0)))

        target_idx = {t: i for i, t in enumerate(target)}
        mat = _frac_array((n_tgt, n_src))

        for col, alpha in enumerate(source):
            alpha_set = set(alpha)
            alpha_list = list(alpha)

            # CE differential: for each pair (beta, gamma) with
            # [beta, gamma] having component along some c in alpha,
            # contribute sign * coeff * (alpha with c replaced by {beta, gamma})
            for c_pos, c in enumerate(alpha_list):
                # Which pairs (beta, gamma) bracket to c?
                for (beta, gamma), br in self._bracket_table.items():
                    if c not in br:
                        continue
                    if beta in alpha_set and beta != c:
                        continue
                    if gamma in alpha_set and gamma != c:
                        continue
                    if beta == gamma:
                        continue

                    coeff = br[c]
                    new_set = (alpha_set - {c}) | {beta, gamma}
                    if len(new_set) != degree + 1:
                        continue
                    new_tuple = tuple(sorted(new_set))
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue

                    # Sign computation for CE differential:
                    # d(x^{i_1} ^ ... ^ x^{i_p})(v_0, ..., v_p) =
                    #   sum_{a<b} (-1)^{a+b} x^{...}([v_a, v_b], v_0, ..., hat_a, ..., hat_b, ...)
                    # In dual terms: inserting beta, gamma at the position of c.
                    sorted_new = list(new_tuple)
                    pos_beta = sorted_new.index(beta)
                    remaining_after_beta = [x for x in sorted_new if x != beta]
                    pos_gamma = remaining_after_beta.index(gamma)
                    sign = Fraction((-1) ** (c_pos + pos_beta + pos_gamma))

                    mat[row, col] += sign * coeff

        return mat

    # ============================================================
    # Hochschild differential (ordered)
    # ============================================================

    def hochschild_differential_matrix(self, degree: int, weight: int) -> np.ndarray:
        """Differential d: B^{ord,degree} -> B^{ord,degree-1} at given weight.

        For the ordered bar, the differential is:
        d(a_1 | ... | a_n) = sum_{i=1}^{n-1} +/- a_1 | ... | [a_i, a_{i+1}] | ... | a_n

        where the sign involves Koszul signs from desuspension.
        The bracket [a_i, a_{i+1}] uses the loop algebra bracket.

        This maps bar degree n to bar degree n-1 (bar-degree -1 differential).
        In our convention, this raises cohomological degree by 1.
        """
        source = self.ordered_basis(degree, weight)
        target = self.ordered_basis(degree - 1, weight)
        n_src = len(source)
        n_tgt = len(target)

        if n_src == 0 or n_tgt == 0:
            return _frac_array((max(n_tgt, 0), max(n_src, 0)))

        target_idx = {t: i for i, t in enumerate(target)}
        mat = _frac_array((n_tgt, n_src))

        for col, b in enumerate(source):
            b_list = list(b)
            for i in range(degree - 1):
                # Bracket [b[i], b[i+1]]
                pair = (b[i], b[i + 1])
                br = self._bracket_table.get(pair, {})
                for c, coeff in br.items():
                    # Replace positions i, i+1 with c
                    new_list = b_list[:i] + [c] + b_list[i + 2:]
                    new_tuple = tuple(new_list)
                    # Check all entries are distinct
                    if len(set(new_tuple)) != len(new_tuple):
                        continue
                    row = target_idx.get(new_tuple)
                    if row is None:
                        continue

                    # Koszul sign: (-1)^{sum of desuspended degrees of b[0],...,b[i-1]}
                    degs = [self.generators[b_list[k]].desuspended_degree
                            for k in range(i)]
                    sign = Fraction((-1) ** sum(degs))

                    mat[row, col] += sign * coeff

        return mat

    # ============================================================
    # Cohomology computation
    # ============================================================

    @staticmethod
    def _exact_rank(M: np.ndarray) -> int:
        """Exact rank of a Fraction-valued matrix via Gaussian elimination."""
        if M.size == 0:
            return 0
        rows, cols = M.shape
        if rows == 0 or cols == 0:
            return 0
        A = np.array([[_frac(M[i, j]) for j in range(cols)]
                       for i in range(rows)], dtype=object)
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

    def unordered_cohomology_dim(self, degree: int, weight: int) -> int:
        """dim H^degree(B^{un})_weight via ker/im."""
        # d_{degree-1}: Lambda^{degree-1} -> Lambda^{degree}
        # d_{degree}: Lambda^{degree} -> Lambda^{degree+1}
        # H^degree = ker(d_degree) / im(d_{degree-1})

        dim_space = self.unordered_dim(degree, weight)
        if dim_space == 0:
            return 0

        # Image of d_{degree-1}
        d_prev = self.ce_differential_matrix(degree - 1, weight)
        rank_prev = self._exact_rank(d_prev) if d_prev.size > 0 else 0

        # Kernel of d_degree
        d_curr = self.ce_differential_matrix(degree, weight)
        rank_curr = self._exact_rank(d_curr) if d_curr.size > 0 else 0
        ker_dim = dim_space - rank_curr

        return ker_dim - rank_prev

    def unordered_d_squared_zero(self, degree: int, weight: int) -> bool:
        """Verify d^2 = 0 on the unordered (CE) complex."""
        d1 = self.ce_differential_matrix(degree, weight)
        d2 = self.ce_differential_matrix(degree + 1, weight)

        if d1.size == 0 or d2.size == 0:
            return True

        # d2 @ d1 should be zero
        rows2, cols2 = d2.shape
        rows1, cols1 = d1.shape
        if cols2 != rows1:
            # Dimension mismatch means the spaces don't connect
            return cols2 == 0 or rows1 == 0

        product = _frac_array((rows2, cols1))
        for i in range(rows2):
            for j in range(cols1):
                s = Fraction(0)
                for k in range(cols2):
                    s += d2[i, k] * d1[k, j]
                product[i, j] = s

        return all(product[i, j] == Fraction(0)
                   for i in range(rows2) for j in range(cols1))

    # ============================================================
    # Comparison: ordered vs unordered dimensions
    # ============================================================

    def comparison_summary(self, max_degree: int = 4, max_wt: int = 6
                           ) -> Dict[Tuple[int, int], Dict[str, int]]:
        """Summary comparing ordered vs unordered at each (degree, weight).

        Returns dict mapping (n, h) -> {
            'ordered': dim B^{ord,n}_h,
            'unordered': dim B^{un,n}_h,
            'ratio': ordered / unordered (as integer if exact),
        }
        """
        result = {}
        for n in range(1, max_degree + 1):
            for h in range(1, max_wt + 1):
                d_ord = self.ordered_dim(n, h)
                d_un = self.unordered_dim(n, h)
                if d_ord > 0 or d_un > 0:
                    entry = {'ordered': d_ord, 'unordered': d_un}
                    if d_un > 0:
                        entry['ratio'] = d_ord // d_un
                    result[(n, h)] = entry
        return result

    # ============================================================
    # Swiss-cheese: ordered coproduct
    # ============================================================

    def ordered_deconcatenation_coproduct(self, degree: int, weight: int
                                          ) -> Dict[Tuple[int, int], List[Tuple[Tuple[int, ...], Tuple[int, ...]]]]:
        """Deconcatenation coproduct on B^{ord,degree}_weight.

        Delta(a_1 | ... | a_n) = sum_{p=0}^{n} (a_1 | ... | a_p) tensor (a_{p+1} | ... | a_n)

        Returns dict mapping (p, q) -> list of (left_part, right_part) pairs.
        This is NOT cocommutative: Delta != tau o Delta.
        """
        basis = self.ordered_basis(degree, weight)
        result: Dict[Tuple[int, int], List] = {}

        for b in basis:
            for p in range(degree + 1):
                q = degree - p
                left = b[:p]
                right = b[p:]
                key = (p, q)
                if key not in result:
                    result[key] = []
                result[key].append((left, right))

        return result

    def coproduct_is_cocommutative(self, degree: int, weight: int) -> bool:
        """Check whether the deconcatenation coproduct is cocommutative.

        It should NOT be for degree >= 2 with dim > 1.
        Cocommutativity: Delta = tau_{12} o Delta (swap tensor factors).
        """
        basis = self.ordered_basis(degree, weight)
        if len(basis) <= 1:
            return True

        # For each basis element, check if Delta = tau o Delta
        for b in basis:
            for p in range(1, degree):
                q = degree - p
                left = b[:p]
                right = b[p:]
                # Swapped version: we need right | left to equal left | right
                # in the OTHER summand. But for non-cocommutative, there exists
                # a splitting where left != right (as tensor factors in different spaces).
                # The point is that deconcatenation distinguishes order.
                if left != right and p != q:
                    return False
                if p == q and left != right:
                    return False
        return True

    # ============================================================
    # Ordered first-disagrees analysis
    # ============================================================

    def first_disagreement_degree(self, max_wt: int = 8) -> Optional[Tuple[int, int]]:
        """Find the first (degree, weight) where ordered != unordered dims.

        For degree 1: always equal (both = number of generators at that weight).
        For degree >= 2: ordered = n! * unordered when all gens are distinct.
        """
        for n in range(1, max_wt + 1):
            for h in range(n, max_wt + 1):
                d_ord = self.ordered_dim(n, h)
                d_un = self.unordered_dim(n, h)
                if d_ord > 0 and d_un > 0 and d_ord != d_un:
                    return (n, h)
        return None

    # ============================================================
    # Alternating part extraction
    # ============================================================

    def alternating_part_dim(self, degree: int, weight: int) -> int:
        """Dimension of the alternating (sign) isotypic component of B^{ord,n}_h.

        The alternating part of (s^{-1}V)^{tensor n} under S_n is Lambda^n(s^{-1}V).
        For desuspended degree 0 (weight-1 generators), the sign representation
        acts as the usual sign: the alternating part = antisymmetric tensors.
        For desuspended degree 1 (weight-2 generators), the Koszul sign
        CANCELS the usual sign: alternating = SYMMETRIC tensors.

        This should equal the unordered dimension (since the unordered bar
        IS the alternating part in the appropriate sense).
        """
        decomp = self.sn_irrep_decomposition(degree, weight)
        # The sign representation corresponds to partition (1,...,1)
        sign_part = tuple([1] * degree)
        return decomp.get(sign_part, 0)

    def trivial_part_dim(self, degree: int, weight: int) -> int:
        """Dimension of the trivial isotypic component of B^{ord,n}_h."""
        decomp = self.sn_irrep_decomposition(degree, weight)
        # The trivial representation corresponds to partition (n,)
        return decomp.get((degree,), 0)
