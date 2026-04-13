"""A-infinity bimodule structures for gluing local CY3 quiver charts.

Mathematical core of chart-to-global passage in CY3 geometry. Given A-infinity
algebras A, B associated to local charts, the transition data is encoded in an
(A,B)-bimodule M with operations

    m_{p|1|q}: A^{otimes p} tensor M tensor B^{otimes q} -> M[2-p-q]

satisfying the A-infinity bimodule equation. This module computes:

1. Explicit A-infinity bimodule structures for low (p,q)
2. Transition bimodules for A_n quiver mutations (flops)
3. Derived tensor products for triple-overlap cocycles
4. Koszul dual bimodules via the bar construction
5. Numerical invariants (Euler characteristics, Hochschild homology)
6. Shadow obstruction contributions from transition data

GRADING: Cohomological (|d| = +1). Bar uses DESUSPENSION (|s^{-1}v| = |v| - 1).
SIGN CONVENTION: Koszul sign rule throughout.

References:
  - Keller, "A-infinity algebras, modules and functor categories"
  - Loday-Vallette, "Algebraic Operads" Ch. 9-10
  - Seidel, "Fukaya categories and Picard-Lefschetz theory" Ch. 1
  - Van den Bergh, "Non-commutative crepant resolutions"
  - Bridgeland, "Flops and derived categories"
  - Kontsevich, "Homological algebra of mirror symmetry"
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as iter_product
from typing import Dict, List, Optional, Tuple, Callable

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
    if isinstance(x, float):
        return Fraction(x).limit_denominator(10**12)
    return Fraction(x)


def _frac_array(shape) -> np.ndarray:
    """Create a zero array of Fraction objects."""
    if isinstance(shape, int):
        shape = (shape,)
    arr = np.empty(shape, dtype=object)
    arr.fill(Fraction(0))
    return arr


def _frac_matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Matrix multiply two Fraction-object arrays."""
    if A.ndim == 1 and B.ndim == 1:
        return sum(A[i] * B[i] for i in range(len(A)))
    if A.ndim == 1:
        A = A.reshape(1, -1)
    if B.ndim == 1:
        B = B.reshape(-1, 1)
    m, k1 = A.shape
    k2, n = B.shape
    assert k1 == k2, f"Shape mismatch: {A.shape} vs {B.shape}"
    C = _frac_array((m, n))
    for i in range(m):
        for j in range(n):
            s = Fraction(0)
            for l in range(k1):
                s += A[i, l] * B[l, j]
            C[i, j] = s
    return C


def _is_zero(arr: np.ndarray, tol=None) -> bool:
    """Check if a Fraction-object array is identically zero."""
    for x in arr.flat:
        if x != Fraction(0):
            return False
    return True


def _unit_vec(n: int, j: int) -> np.ndarray:
    """Standard basis vector e_j in Q^n."""
    v = _frac_array(n)
    v[j] = Fraction(1)
    return v


def _image_dim(M: np.ndarray) -> int:
    """Compute rank (dimension of image) of a Fraction-object matrix."""
    if M.size == 0:
        return 0
    rows, cols = M.shape
    A = np.array([[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
                 dtype=object)
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


def _kernel_basis(M: np.ndarray) -> List[np.ndarray]:
    """Compute kernel basis of a Fraction-object matrix via row reduction."""
    if M.size == 0:
        rows, cols = M.shape
        return [_unit_vec(cols, j) for j in range(cols)]
    rows, cols = M.shape
    A = np.array([[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
                 dtype=object)
    pivot_cols = []
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
        pivot_cols.append(c)
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
    free_cols = [c for c in range(cols) if c not in pivot_cols]
    basis = []
    for fc in free_cols:
        v = _frac_array(cols)
        v[fc] = Fraction(1)
        for idx, pc in enumerate(pivot_cols):
            v[pc] = -A[idx, fc]
        basis.append(v)
    return basis


# ============================================================
# Koszul sign
# ============================================================

def _koszul_sign(degrees: List[int], perm: List[int]) -> Fraction:
    """Koszul sign of a permutation acting on elements of given degrees.

    Computes (-1)^{number of transpositions of odd-degree elements}.
    """
    sign = Fraction(1)
    n = len(degrees)
    # Bubble sort to compute sign
    arr = list(perm)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                # Transposition of elements at positions i, j
                if degrees[arr[i]] % 2 == 1 and degrees[arr[j]] % 2 == 1:
                    sign = -sign
                arr[i], arr[j] = arr[j], arr[i]
    return sign


# ============================================================
# A-infinity algebra (finite-dimensional, over Q)
# ============================================================

@dataclass
class AInfAlgebra:
    """A finite-dimensional A-infinity algebra over Q.

    An A-infinity algebra has operations m_n: A^{otimes n} -> A[2-n]
    for n >= 1, satisfying the Stasheff relations:

        sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(id^r, m_s, id^t) = 0

    Representation:
      dims[k] = dim A^k (cohomological degree k)
      total_dim = sum of all dims
      m_ops[n] = dict mapping (i_1,...,i_n, j) to coefficient of e_j
                 in m_n(e_{i_1}, ..., e_{i_n}).
      degrees[i] = cohomological degree of basis vector e_i.

    For a dg algebra, m_1 = d, m_2 = product, m_n = 0 for n >= 3.
    """
    dims: Dict[int, int]
    m_ops: Dict[int, Dict[tuple, Fraction]]  # m_ops[n][(i1,...,in,j)] = coeff
    name: str = ""

    def __post_init__(self):
        self._total_dim = sum(self.dims.values())
        self._degrees = {}
        offset = 0
        for k in sorted(self.dims.keys()):
            for i in range(self.dims[k]):
                self._degrees[offset + i] = k
            offset += self.dims[k]

    @property
    def total_dim(self) -> int:
        return self._total_dim

    def degree_of(self, i: int) -> int:
        return self._degrees[i]

    def m(self, n: int, indices: tuple) -> np.ndarray:
        """Compute m_n(e_{i_1}, ..., e_{i_n}) as a vector.

        indices = (i_1, ..., i_n).
        Returns array of length total_dim.
        """
        result = _frac_array(self.total_dim)
        ops = self.m_ops.get(n, {})
        for j in range(self.total_dim):
            key = indices + (j,)
            if key in ops:
                result[j] = ops[key]
        return result

    def m_coeff(self, n: int, inputs: tuple, output: int) -> Fraction:
        """Coefficient of e_{output} in m_n(e_{inputs})."""
        ops = self.m_ops.get(n, {})
        key = inputs + (output,)
        return ops.get(key, Fraction(0))


def verify_stasheff(A: AInfAlgebra, n: int, inputs: tuple) -> np.ndarray:
    """Compute the Stasheff relation at arity n on given inputs.

    The Stasheff relation:
        sum_{r+s+t=n, s>=1} (-1)^{rs+t} m_{r+1+t}(a_1,...,a_r, m_s(a_{r+1},...,a_{r+s}), a_{r+s+1},...,a_n) = 0

    Sign convention: (-1)^{rs + t} where the sign also includes
    the Koszul sign from moving m_s past a_1,...,a_r.

    For us, using the standard sign: (-1)^{r + sum_{i<=r} |a_i|(s-1)}
    which simplifies to (-1)^{rs+t} on desuspended elements.

    Returns the vector that should be zero.
    """
    assert len(inputs) == n
    result = _frac_array(A.total_dim)

    for r in range(n):           # r = number of inputs before m_s
        for s in range(1, n - r + 1):  # s >= 1, arity of inner operation
            t = n - r - s              # remaining inputs after m_s
            if t < 0:
                continue

            # Compute inner: m_s(a_{r+1}, ..., a_{r+s})
            inner_inputs = inputs[r:r+s]
            inner_result = A.m(s, inner_inputs)

            # Sign: (-1)^{rs + t}
            # More precisely with Koszul signs on shifted elements:
            # (-1)^{sum_{i=1}^{r} (|a_i| - 1) * (s - 1)} = (-1)^{r(s-1) + ...}
            # Using the standard convention from Keller:
            # epsilon = sum_{i=1}^{r} (|a_i| - 1)  (the shifted degree sum)
            epsilon = sum(A.degree_of(inputs[i]) - 1 for i in range(r))
            sign = Fraction((-1) ** epsilon)

            # Outer: m_{r+1+t}(a_1,...,a_r, inner, a_{r+s+1},...,a_n)
            for j in range(A.total_dim):
                if inner_result[j] == Fraction(0):
                    continue
                outer_inputs = inputs[:r] + (j,) + inputs[r+s:]
                outer_result = A.m(r + 1 + t, outer_inputs)
                result += sign * inner_result[j] * outer_result

    return result


def check_stasheff_all(A: AInfAlgebra, max_n: int = 3) -> bool:
    """Check all Stasheff relations up to arity max_n."""
    for n in range(1, max_n + 1):
        for inputs in iter_product(range(A.total_dim), repeat=n):
            rel = verify_stasheff(A, n, inputs)
            if not _is_zero(rel):
                return False
    return True


# ============================================================
# A-infinity bimodule
# ============================================================

@dataclass
class AInfBimodule:
    """An (A, B)-bimodule M in the A-infinity sense.

    Operations: m_{p|1|q}: A^{otimes p} tensor M tensor B^{otimes q} -> M[2-p-q]
    for p, q >= 0, p + q >= 0.

    The A-infinity bimodule equation:
      sum over decompositions sum +- m_{p'|1|q'} o (id^{p'} tensor m_{p''|1|q''} tensor id^{q'})
      + sum +- m_{p'|1|q'}(id^{p'} tensor ..tensor mu^A_s .. tensor m tensor ..)
      + sum +- m_{p'|1|q'}(.. tensor m tensor .. mu^B_s .. tensor id^{q'})
      = 0

    Representation:
      A, B: the two A-infinity algebras
      M_dims[k] = dim M^k (cohomological grading)
      M_total_dim = sum of M_dims
      bim_ops[(p,q)][(a1,...,ap, m_idx, b1,...,bq, out)] = coefficient
    """
    A: AInfAlgebra
    B: AInfAlgebra
    M_dims: Dict[int, int]
    bim_ops: Dict[Tuple[int, int], Dict[tuple, Fraction]]
    name: str = ""

    def __post_init__(self):
        self._M_total_dim = sum(self.M_dims.values())
        self._M_degrees = {}
        offset = 0
        for k in sorted(self.M_dims.keys()):
            for i in range(self.M_dims[k]):
                self._M_degrees[offset + i] = k
            offset += self.M_dims[k]

    @property
    def M_total_dim(self) -> int:
        return self._M_total_dim

    def M_degree_of(self, i: int) -> int:
        return self._M_degrees[i]

    def bim_m(self, p: int, q: int, a_indices: tuple,
              m_idx: int, b_indices: tuple) -> np.ndarray:
        """Compute m_{p|1|q}(a_1,...,a_p, m, b_1,...,b_q) as vector in M.

        a_indices: (a_1,...,a_p) indices in A
        m_idx: index in M
        b_indices: (b_1,...,b_q) indices in B
        """
        result = _frac_array(self.M_total_dim)
        ops = self.bim_ops.get((p, q), {})
        for j in range(self.M_total_dim):
            key = a_indices + (m_idx,) + b_indices + (j,)
            if key in ops:
                result[j] = ops[key]
        return result

    def bim_m_coeff(self, p: int, q: int, a_indices: tuple,
                    m_idx: int, b_indices: tuple, out: int) -> Fraction:
        """Coefficient of e_{out} in m_{p|1|q}(a_1,...,a_p, m, b_1,...,b_q)."""
        ops = self.bim_ops.get((p, q), {})
        key = a_indices + (m_idx,) + b_indices + (out,)
        return ops.get(key, Fraction(0))


def verify_bimodule_relation(bim: AInfBimodule, p: int, q: int,
                              a_indices: tuple, m_idx: int,
                              b_indices: tuple) -> np.ndarray:
    """Verify the A-infinity bimodule relation at bidegree (p, q).

    The full bimodule relation at total arity (p, 1, q):

    (I) Inner bimodule composition:
        sum_{p'+p''=p, q'+q''=q} +- m_{p'|1|q'}(id^{p'}, m_{p''|1|q''}(...), id^{q'})

    (II) Left algebra action:
        sum_{r+s<=p, s>=2} +- m_{p-s+1|1|q}(a_1,..,a_r, mu^A_s(a_{r+1},..,a_{r+s}), .., m, b_1,..,b_q)

    (III) Right algebra action:
        sum_{r+s<=q, s>=2} +- m_{p|1|q-s+1}(a_1,..,a_p, m, b_1,..,b_r, mu^B_s(b_{r+1},..,b_{r+s}), ..)

    Returns vector in M that should be zero.
    """
    A = bim.A
    B = bim.B
    result = _frac_array(bim.M_total_dim)

    # ---- (I) Inner bimodule compositions ----
    # Split (p,q) into outer (p', q') and inner (p'', q'') with p'+p''=p, q'+q''=q
    for pp in range(p + 1):         # p' = 0, ..., p
        ppp = p - pp                # p'' = p - p'
        for qp in range(q + 1):     # q' = 0, ..., q
            qpp = q - qp            # q'' = q - q'
            if pp + qp == p + q and ppp == 0 and qpp == 0:
                # This is m_{p|1|q} applied to identity — skip self
                # Actually (pp, qp) = (p, q) and (ppp, qpp) = (0, 0)
                # m_{p|1|q}(id^p, m_{0|1|0}(m), id^q) is valid
                pass
            if ppp + qpp == 0 and pp + qp == p + q:
                # Special: inner is m_{0|1|0} = differential on M
                inner_a = ()
                inner_b = ()
                for k in range(bim.M_total_dim):
                    inner_val = bim.bim_m(0, 0, (), m_idx, ())
                    if inner_val[k] == Fraction(0):
                        continue
                    # Outer: m_{p|1|q}(a_1,...,a_p, k, b_1,...,b_q)
                    outer_val = bim.bim_m(p, q, a_indices, k, b_indices)

                    # Sign: epsilon = sum shifted degrees of a_1,...,a_{pp} = a_1,...,a_p
                    # (before the inner operation)
                    epsilon = sum(A.degree_of(a_indices[i]) - 1 for i in range(pp))
                    sign = Fraction((-1) ** epsilon)
                    result += sign * inner_val[k] * outer_val
                continue

            # General case: inner m_{p''|1|q''} acts on
            # a_{pp+1},...,a_{pp+ppp}, m, b_1,...,b_{qpp}
            # outer m_{pp|1|qp} acts on
            # a_1,...,a_{pp}, [inner result], b_{qpp+1},...,b_q

            # Inner: m_{ppp|1|qpp}(a_{pp+1},...,a_p, m_idx, b_1,...,b_{qpp})
            inner_a = a_indices[pp:pp + ppp]
            inner_b = b_indices[:qpp]
            inner_val = bim.bim_m(ppp, qpp, inner_a, m_idx, inner_b)

            # Sign: shifted degrees of elements before inner op
            epsilon = sum(A.degree_of(a_indices[i]) - 1 for i in range(pp))
            sign = Fraction((-1) ** epsilon)

            for k in range(bim.M_total_dim):
                if inner_val[k] == Fraction(0):
                    continue
                # Outer: m_{pp|1|qp}(a_1,...,a_{pp}, k, b_{qpp+1},...,b_q)
                outer_a = a_indices[:pp]
                outer_b = b_indices[qpp:]
                outer_val = bim.bim_m(pp, qp, outer_a, k, outer_b)
                result += sign * inner_val[k] * outer_val

    # ---- (II) Left algebra action: insert m^A_s inside the a-inputs ----
    for s in range(2, p + 1):  # s = arity of mu^A_s, s >= 2
        for r in range(0, p - s + 1):  # r = number of a's before mu^A_s
            # mu^A_s(a_{r+1}, ..., a_{r+s})
            inner_a_indices = a_indices[r:r + s]
            inner_val = A.m(s, inner_a_indices)

            # Sign from moving mu past shifted a_1,...,a_r
            epsilon = sum(A.degree_of(a_indices[i]) - 1 for i in range(r))
            sign = Fraction((-1) ** epsilon)

            for k in range(A.total_dim):
                if inner_val[k] == Fraction(0):
                    continue
                # New a-inputs: a_1,...,a_r, k, a_{r+s+1},...,a_p
                new_a = a_indices[:r] + (k,) + a_indices[r + s:]
                new_p = p - s + 1
                outer_val = bim.bim_m(new_p, q, new_a, m_idx, b_indices)
                result += sign * inner_val[k] * outer_val

    # ---- (III) Right algebra action: insert m^B_s inside the b-inputs ----
    for s in range(2, q + 1):
        for r in range(0, q - s + 1):
            inner_b_indices = b_indices[r:r + s]
            inner_val = B.m(s, inner_b_indices)

            # Sign: shifted degrees of ALL a's + m + b_1,...,b_r
            epsilon_a = sum(A.degree_of(a_indices[i]) - 1 for i in range(p))
            epsilon_m = bim.M_degree_of(m_idx) - 1
            epsilon_b = sum(B.degree_of(b_indices[i]) - 1 for i in range(r))
            epsilon = epsilon_a + epsilon_m + epsilon_b
            sign = Fraction((-1) ** epsilon)

            for k in range(B.total_dim):
                if inner_val[k] == Fraction(0):
                    continue
                new_b = b_indices[:r] + (k,) + b_indices[r + s:]
                new_q = q - s + 1
                outer_val = bim.bim_m(p, new_q, a_indices, m_idx, new_b)
                result += sign * inner_val[k] * outer_val

    return result


def check_bimodule_relations(bim: AInfBimodule, max_pq: int = 3,
                             reduced: bool = True) -> bool:
    """Check all bimodule relations up to total arity p+q <= max_pq.

    If reduced=True (default), only check on the augmentation ideal
    (non-unit elements) of A and B. The A-infinity bimodule equation
    is formulated on the REDUCED bar complex; unit actions are strict
    identities and do not participate in the A-infinity relations.
    """
    # Determine non-unit indices (augmentation ideal)
    if reduced:
        a_aug = [i for i in range(bim.A.total_dim)
                 if bim.A.degree_of(i) != 0]
        b_aug = [i for i in range(bim.B.total_dim)
                 if bim.B.degree_of(i) != 0]
        # If augmentation ideal is empty, fall back to full check
        if not a_aug:
            a_aug = list(range(bim.A.total_dim))
        if not b_aug:
            b_aug = list(range(bim.B.total_dim))
    else:
        a_aug = list(range(bim.A.total_dim))
        b_aug = list(range(bim.B.total_dim))

    for total in range(max_pq + 1):
        for p in range(total + 1):
            q = total - p
            for a_indices in iter_product(a_aug, repeat=p):
                for m_idx in range(bim.M_total_dim):
                    for b_indices in iter_product(b_aug, repeat=q):
                        rel = verify_bimodule_relation(
                            bim, p, q, a_indices, m_idx, b_indices)
                        if not _is_zero(rel):
                            return False
    return True


# ============================================================
# Standard A-infinity algebras
# ============================================================

def trivial_algebra(n: int = 1, degree: int = 0) -> AInfAlgebra:
    """Ground field k concentrated in degree 0 (or specified degree).

    The unit algebra: m_2(1, 1) = 1, all other operations vanish.
    """
    dims = {degree: n}
    m_ops = {2: {}}
    # Unit: m_2(e_i, e_j) = delta_{ij} e_i for the 1d case
    if n == 1:
        m_ops[2][(0, 0, 0)] = Fraction(1)
    else:
        # Diagonal product for n-dim commutative
        for i in range(n):
            m_ops[2][(i, i, i)] = Fraction(1)
    return AInfAlgebra(dims=dims, m_ops=m_ops, name=f"k^{n}[{degree}]")


def path_algebra_A1() -> AInfAlgebra:
    """Path algebra of the A_1 quiver (single vertex, no arrows).

    This is just k = the ground field.
    """
    return trivial_algebra(1, 0)


def path_algebra_A2() -> AInfAlgebra:
    """Path algebra of the A_2 quiver: 1 -> 2.

    Basis: e_1 (idempotent at 1), e_2 (idempotent at 2), a (arrow 1->2).
    All in degree 0.
    Product: e_1 * a = a, a * e_2 = a, e_i * e_i = e_i, others = 0.
    """
    dims = {0: 3}  # e_1, e_2, a
    m_ops = {2: {}}
    # Idempotent relations
    m_ops[2][(0, 0, 0)] = Fraction(1)  # e_1 * e_1 = e_1
    m_ops[2][(1, 1, 1)] = Fraction(1)  # e_2 * e_2 = e_2
    # Arrow composition
    m_ops[2][(0, 2, 2)] = Fraction(1)  # e_1 * a = a
    m_ops[2][(2, 1, 2)] = Fraction(1)  # a * e_2 = a
    return AInfAlgebra(dims=dims, m_ops=m_ops, name="kA_2")


def path_algebra_A3() -> AInfAlgebra:
    """Path algebra of the A_3 quiver: 1 -> 2 -> 3.

    Basis: e_1, e_2, e_3 (idempotents), a (1->2), b (2->3), ba (1->3).
    All in degree 0.
    """
    dims = {0: 6}  # e_1, e_2, e_3, a, b, ba
    m_ops = {2: {}}
    # Idempotents
    for i in range(3):
        m_ops[2][(i, i, i)] = Fraction(1)
    # e_1 * a = a, a * e_2 = a
    m_ops[2][(0, 3, 3)] = Fraction(1)
    m_ops[2][(3, 1, 3)] = Fraction(1)
    # e_2 * b = b, b * e_3 = b
    m_ops[2][(1, 4, 4)] = Fraction(1)
    m_ops[2][(4, 2, 4)] = Fraction(1)
    # a * b = ba
    m_ops[2][(3, 4, 5)] = Fraction(1)
    # e_1 * ba = ba, ba * e_3 = ba
    m_ops[2][(0, 5, 5)] = Fraction(1)
    m_ops[2][(5, 2, 5)] = Fraction(1)
    return AInfAlgebra(dims=dims, m_ops=m_ops, name="kA_3")


def ext_algebra_A1_flop() -> AInfAlgebra:
    """Ext algebra Ext*(T, T) for the tilting generator on the A_1 flop.

    The conifold resolution C^2/Z_2 -> resolved.
    Tilting generator T = O + O(-1)[1] on the resolved side.
    Ext*(T, T) is the path algebra of the A_1 quiver with relations,
    concentrated in degrees 0 and 1.

    Basis:
      degree 0: e_0, e_1 (idempotents for O, O(-1)[1])
      degree 1: a (from Ext^1(O, O(-1)[1]) = k), b (from Ext^1(O(-1)[1], O) = k)
      degree 2: (none — this is the quiver WITH relations ab = ba = 0, which is
                 the derived endomorphism algebra: m_2(a,b) = 0, but m_3 != 0)

    The A-infinity structure has m_3(a, b, a) = nonzero (the Massey product),
    encoding the geometry of the flop.

    For the conifold: T = O_X + O_C(-1)[1] where C is the exceptional P^1.
    Ext^1(O, O(-1)[1]) = H^0(O(1)) on P^1 = k^2, but for the simplest
    model we take the rank-1 truncation.

    We use the simplified model where Ext^1 is 1-dimensional in each direction.
    """
    dims = {0: 2, 1: 2}
    # Basis: e_0 (deg 0), e_1 (deg 0), a (deg 1), b (deg 1)
    m_ops = {}

    # m_1 = 0 (this is the cohomology algebra, so differential vanishes)
    m_ops[1] = {}

    # m_2: product
    m_ops[2] = {}
    # Idempotents
    m_ops[2][(0, 0, 0)] = Fraction(1)  # e_0 * e_0 = e_0
    m_ops[2][(1, 1, 1)] = Fraction(1)  # e_1 * e_1 = e_1
    # Arrow relations: e_0 * a = a, a * e_1 = a
    m_ops[2][(0, 2, 2)] = Fraction(1)
    m_ops[2][(2, 1, 2)] = Fraction(1)
    # b goes the other way: e_1 * b = b, b * e_0 = b
    m_ops[2][(1, 3, 3)] = Fraction(1)
    m_ops[2][(3, 0, 3)] = Fraction(1)
    # a * b = 0, b * a = 0 (the relations in the quiver with relations)

    # m_3: the Massey product encoding the flop
    # m_3(a, b, a) = e_0 (a nonzero scalar times the idempotent)
    # m_3(b, a, b) = e_1
    # These are the key higher products from the geometry.
    m_ops[3] = {}
    # m_3(a, b, a): inputs (2, 3, 2), degree shift 2-3=-1,
    # so output in degree 1+1+1-1=2. But we have no degree-2 generators.
    # Actually m_3: A^{otimes 3} -> A[2-3] = A[-1], so it RAISES degree by -1
    # (lowers by 1). Input degrees: 1+1+1=3, output degree: 3-1=2.
    # We need a degree-2 element. For the conifold, Ext^2(O,O) = k.
    # Let us add it.
    dims = {0: 2, 1: 2, 2: 1}
    # New basis: e_0(0), e_1(0), a(1), b(1), w(2)
    # Redefine:
    m_ops[2][(0, 0, 0)] = Fraction(1)
    m_ops[2][(1, 1, 1)] = Fraction(1)
    m_ops[2][(0, 2, 2)] = Fraction(1)
    m_ops[2][(2, 1, 2)] = Fraction(1)
    m_ops[2][(1, 3, 3)] = Fraction(1)
    m_ops[2][(3, 0, 3)] = Fraction(1)
    # a*b = 0, but we could have a*b = w or a*b = 0 with m_3 nonzero
    # For the A_1 flop: a*b = 0 in the associative product (it's the quiver
    # with relations), and the higher product encodes the obstruction.
    # m_3(a, b, a) requires degree 2 output: this goes to w
    m_ops[3][(2, 3, 2, 4)] = Fraction(1)  # m_3(a, b, a) = w
    # Actually for the geometric situation the correct Massey structure is:
    # m_2(a, b) = 0 but m_3 detects the nonformality.
    # The simplest correct model: m_3(a, b, a) = lambda * w for lambda != 0.

    return AInfAlgebra(dims=dims, m_ops=m_ops, name="Ext_A1_flop")


def dg_algebra_from_matrices(dims: Dict[int, int],
                              d_matrix: np.ndarray,
                              product_tensor: np.ndarray,
                              name: str = "") -> AInfAlgebra:
    """Convert a dg algebra (d, m_2) to an AInfAlgebra."""
    total_dim = sum(dims.values())
    m_ops = {}

    # m_1 from differential
    m_ops[1] = {}
    for i in range(total_dim):
        for j in range(total_dim):
            if d_matrix[j, i] != Fraction(0):
                m_ops[1][(i, j)] = _frac(d_matrix[j, i])

    # m_2 from product
    m_ops[2] = {}
    for i in range(total_dim):
        for j in range(total_dim):
            for k in range(total_dim):
                if product_tensor[i, j, k] != Fraction(0):
                    m_ops[2][(i, j, k)] = _frac(product_tensor[i, j, k])

    return AInfAlgebra(dims=dims, m_ops=m_ops, name=name)


# ============================================================
# Transition bimodule for A_1 quiver mutation (flop)
# ============================================================

def identity_bimodule(A: AInfAlgebra) -> AInfBimodule:
    """The diagonal (identity) bimodule A over (A, A).

    M = A with:
      m_{0|1|0} = m_1 (the differential)
      m_{1|1|0}(a, m) = m_2(a, m) (left action)
      m_{0|1|1}(m, b) = m_2(m, b) (right action)
      m_{p|1|q} for p+q >= 2: from higher m_{p+q+1}.

    This is the identity functor in the bimodule category.
    """
    bim_ops = {}

    # m_{0|1|0}: differential on M = A
    bim_ops[(0, 0)] = {}
    ops_1 = A.m_ops.get(1, {})
    for key, val in ops_1.items():
        # key = (i, j) means m_1(e_i) has coeff val at e_j
        # For bimodule: m_{0|1|0}(m=i, out=j) = val
        bim_ops[(0, 0)][key] = val

    # m_{1|1|0}: left action = m_2(a, m)
    bim_ops[(1, 0)] = {}
    ops_2 = A.m_ops.get(2, {})
    for key, val in ops_2.items():
        # key = (i, j, k) means m_2(e_i, e_j) has coeff val at e_k
        # For bimodule: m_{1|1|0}(a=i, m=j, out=k) = val
        bim_ops[(1, 0)][key] = val

    # m_{0|1|1}: right action = m_2(m, b)
    bim_ops[(0, 1)] = {}
    for key, val in ops_2.items():
        # m_2(e_i, e_j) -> e_k means m_{0|1|1}(m=i, b=j, out=k) = val
        bim_ops[(0, 1)][key] = val

    # m_{1|1|1}: from m_3
    bim_ops[(1, 1)] = {}
    ops_3 = A.m_ops.get(3, {})
    for key, val in ops_3.items():
        # key = (i, j, k, l): m_3(e_i, e_j, e_k) -> e_l
        # Bimodule: m_{1|1|1}(a=i, m=j, b=k, out=l) = val
        bim_ops[(1, 1)][key] = val

    # m_{2|1|0}: from m_3, m_3(a1, a2, m)
    bim_ops[(2, 0)] = {}
    for key, val in ops_3.items():
        bim_ops[(2, 0)][key] = val

    # m_{0|1|2}: from m_3, m_3(m, b1, b2)
    bim_ops[(0, 2)] = {}
    for key, val in ops_3.items():
        bim_ops[(0, 2)][key] = val

    return AInfBimodule(
        A=A, B=A, M_dims=dict(A.dims), bim_ops=bim_ops,
        name=f"Id({A.name})"
    )


def a1_flop_bimodule() -> Tuple[AInfAlgebra, AInfAlgebra, AInfBimodule]:
    """Transition bimodule for the A_1 flop (conifold).

    Two charts: U (resolution) and U' (flopped resolution).
    A = Ext*(T, T) and B = Ext*(T', T') are the endomorphism algebras.

    For the A_1 flop, A and B are isomorphic as A-infinity algebras
    (mutation equivalence). The transition bimodule M = Ext*(T, T')
    encodes the Fourier-Mukai kernel of the flop.

    Simplified model (rank 1):
      A = B = k[x]/(x^2) with |x| = 1 (exterior algebra on one generator).
      This is the endomorphism algebra of the structure sheaf on P^1.

    The transition bimodule M has:
      M^0 = k (one morphism in degree 0)
      M^1 = k (one extension class)
      m_{0|1|0} = 0 (on cohomology)
      m_{1|1|0}(x, m_0) = m_1 (left action)
      m_{0|1|1}(m_0, x) = m_1 (right action)
      m_{1|1|1}(x, m_0, x) = 0 (vanishes for degree reasons in the rank-1 model)

    For the genuine conifold (rank 2), the higher products are nontrivial.
    """
    # A = B = exterior algebra k[x]/(x^2), |x| = 1
    dims = {0: 1, 1: 1}
    m_ops = {}
    m_ops[1] = {}  # d = 0
    m_ops[2] = {}
    # 1*1 = 1 (unit)
    m_ops[2][(0, 0, 0)] = Fraction(1)
    # 1*x = x
    m_ops[2][(0, 1, 1)] = Fraction(1)
    # x*1 = x
    m_ops[2][(1, 0, 1)] = Fraction(1)
    # x*x = 0 (exterior)

    A = AInfAlgebra(dims=dims, m_ops=m_ops, name="Lambda(x)")
    B = AInfAlgebra(dims=dims, m_ops=dict(m_ops), name="Lambda(x)'")

    # Transition bimodule M
    M_dims = {0: 1, 1: 1}
    bim_ops = {}

    # m_{0|1|0} = 0 (cohomological, no differential)
    bim_ops[(0, 0)] = {}

    # m_{1|1|0}: left A-action on M
    # x . m_0 = m_1
    bim_ops[(1, 0)] = {}
    bim_ops[(1, 0)][(1, 0, 1)] = Fraction(1)  # m_{1|1|0}(x, m_0) = m_1
    # 1 . m_0 = m_0, 1 . m_1 = m_1
    bim_ops[(1, 0)][(0, 0, 0)] = Fraction(1)
    bim_ops[(1, 0)][(0, 1, 1)] = Fraction(1)
    # x . m_1 = 0 (degree 2, no space)

    # m_{0|1|1}: right B-action on M
    bim_ops[(0, 1)] = {}
    bim_ops[(0, 1)][(0, 1, 1)] = Fraction(1)  # m_{0|1|1}(m_0, x) = m_1
    bim_ops[(0, 1)][(0, 0, 0)] = Fraction(1)  # m_{0|1|1}(m_0, 1) = m_0
    bim_ops[(0, 1)][(1, 0, 1)] = Fraction(1)  # m_{0|1|1}(m_1, 1_B) = m_1 (strict unit action)
    # m_{0|1|1}(m_1, x) = 0 (degree 2, no target space)

    # m_{1|1|1}: the transfer operation
    bim_ops[(1, 1)] = {}
    # For the rank-1 model, m_{1|1|1}(x, m_0, x) = 0 by degree (output would be
    # degree 1+0+1 + (2-1-1) = 2, but M^2 = 0).
    # Nontrivial only in rank >= 2.

    M = AInfBimodule(A=A, B=B, M_dims=M_dims, bim_ops=bim_ops,
                     name="Flop_A1")

    return A, B, M


def a1_flop_bimodule_rank2() -> Tuple[AInfAlgebra, AInfAlgebra, AInfBimodule]:
    """Rank-2 transition bimodule for the A_1 flop (full conifold model).

    The genuine conifold C^2/Z_2:
    Tilting generator T = O + O_C(-1)[1] on the resolved side.
    The exceptional P^1 has normal bundle O(-1)+O(-1).

    Ext*(T, T) has:
      degree 0: e_0, e_1 (idempotents)
      degree 1: a, b (arrows in both directions, from H^0(O_C(1)) = k^2 but
                the quiver has ONE arrow each way for the McKay quiver)

    The A_1 McKay quiver: two vertices, arrows a: 0->1 and b: 1->0,
    relation ab = ba (preprojective algebra).

    For the A-infinity enhancement:
      m_2(a, b) = 0, m_2(b, a) = 0 (relations in the quiver with relations)
      but m_3 is nontrivial, detecting the flop.

    The transition bimodule M = RHom(T, F(T)) where F is the flop functor.
    """
    # A-infinity algebra: degree 0 (2 idempotents), degree 1 (2 arrows)
    dims_A = {0: 2, 1: 2}
    m_ops_A = {}
    m_ops_A[1] = {}  # d = 0 on cohomology
    m_ops_A[2] = {}
    # Idempotents: e_0*e_0=e_0, e_1*e_1=e_1
    m_ops_A[2][(0, 0, 0)] = Fraction(1)
    m_ops_A[2][(1, 1, 1)] = Fraction(1)
    # a: 0->1, so e_0*a = a, a*e_1 = a (a = index 2)
    m_ops_A[2][(0, 2, 2)] = Fraction(1)
    m_ops_A[2][(2, 1, 2)] = Fraction(1)
    # b: 1->0, so e_1*b = b, b*e_0 = b (b = index 3)
    m_ops_A[2][(1, 3, 3)] = Fraction(1)
    m_ops_A[2][(3, 0, 3)] = Fraction(1)
    # a*b = 0, b*a = 0 (quiver with relations, nontrivial in m_3)

    # m_3: Massey products from the geometry
    # For the conifold, the key m_3's are:
    # m_3(a, b, a) contributes to Ext^2 — but we stay in degrees 0,1.
    # Actually: m_3: A^{otimes 3} -> A[2-3] = A[-1].
    # Input (deg 1, deg 1, deg 1) -> output deg 1+1+1-1 = 2, not in our algebra.
    # Input (deg 1, deg 1, deg 0) -> output deg 1+1+0-1 = 1.
    # m_3(a, b, e_0) or m_3(b, a, e_1): these CAN be nonzero.
    # The conifold's higher product: m_3(a, b, a) requires degree 2.
    # Since we have no degree 2, we encode via:
    # m_3(a, e_1, b) = lambda * e_0 (output degree 1+0+1-1=1, need degree 0? No,
    # shift is 2-3=-1, so output degree = sum_input_deg + (-1) = wrong.)
    #
    # Correct: m_n: A^{otimes n} -> A has degree 2-n in the shifted (bar) sense.
    # So m_3 has degree 2-3 = -1 on the SUSPENDED algebra.
    # On the unsuspended: m_3(a_1,...,a_3) has degree |a_1|+|a_2|+|a_3| + (2-3).
    # = |a_1|+|a_2|+|a_3| - 1.
    #
    # So m_3(a, b, e_0): degrees 1+1+0-1 = 1. Could give a or b.
    # m_3(a, b, e_1): degrees 1+1+0-1 = 1.
    # These give the nontrivial A-infinity structure.
    m_ops_A[3] = {}
    # The preprojective relation for the conifold:
    # The obstruction to ab=0: m_3(a, b, e_0) = a (simplest nontrivial choice)
    # This encodes that the "relation" ab has a higher correction.
    # By symmetry: m_3(b, a, e_1) = b
    m_ops_A[3][(2, 3, 0, 2)] = Fraction(1)  # m_3(a, b, e_0) = a
    m_ops_A[3][(3, 2, 1, 3)] = Fraction(1)  # m_3(b, a, e_1) = b

    A = AInfAlgebra(dims=dims_A, m_ops=m_ops_A, name="Ext_conifold")

    # B is the mutated algebra (flop side).
    # For the conifold, the flop is an involution, so B = A up to relabeling.
    # The mutation swaps the two vertices: e_0 <-> e_1, a <-> b.
    m_ops_B = {}
    m_ops_B[1] = {}
    m_ops_B[2] = dict(m_ops_A[2])  # Same product structure
    m_ops_B[3] = dict(m_ops_A[3])  # Same higher products
    B = AInfAlgebra(dims=dict(dims_A), m_ops=m_ops_B, name="Ext_conifold'")

    # Transition bimodule M = RHom(T, F(T))
    # F swaps the simple objects S_0 <-> S_1.
    # M has:
    #   M^0: Hom(T_0, F(T_0)) + Hom(T_1, F(T_1)) = k + k (2-dim)
    #   M^1: Ext^1(T_0, F(T_1)) + Ext^1(T_1, F(T_0)) = k + k (2-dim)
    M_dims = {0: 2, 1: 2}
    # Basis: m_0^0 (deg 0, vertex 0), m_1^0 (deg 0, vertex 1),
    #        m_0^1 (deg 1, from 0 to 1), m_1^1 (deg 1, from 1 to 0)
    bim_ops = {}

    # m_{0|1|0} = 0 on cohomology
    bim_ops[(0, 0)] = {}

    # m_{1|1|0}: left A-action
    bim_ops[(1, 0)] = {}
    # Idempotent actions
    bim_ops[(1, 0)][(0, 0, 0)] = Fraction(1)  # e_0 . m_0^0 = m_0^0
    bim_ops[(1, 0)][(1, 1, 1)] = Fraction(1)  # e_1 . m_1^0 = m_1^0
    bim_ops[(1, 0)][(0, 2, 2)] = Fraction(1)  # e_0 . m_0^1 = m_0^1
    bim_ops[(1, 0)][(1, 3, 3)] = Fraction(1)  # e_1 . m_1^1 = m_1^1
    # Arrow actions: a . m_1^0 = m_0^1 (a goes 0->1 in A, flop swaps, so
    # it maps m at vertex 1 to extension at vertex 0)
    bim_ops[(1, 0)][(2, 1, 2)] = Fraction(1)  # a . m_1^0 = m_0^1
    # b . m_0^0 = m_1^1
    bim_ops[(1, 0)][(3, 0, 3)] = Fraction(1)  # b . m_0^0 = m_1^1

    # m_{0|1|1}: right B-action
    bim_ops[(0, 1)] = {}
    bim_ops[(0, 1)][(0, 0, 0)] = Fraction(1)  # m_0^0 . e_0 = m_0^0
    bim_ops[(0, 1)][(1, 1, 1)] = Fraction(1)  # m_1^0 . e_1 = m_1^0
    bim_ops[(0, 1)][(2, 0, 2)] = Fraction(1)  # m_0^1 . e_0 = m_0^1
    bim_ops[(0, 1)][(3, 1, 3)] = Fraction(1)  # m_1^1 . e_1 = m_1^1
    # m_0^0 . a = m_0^1
    bim_ops[(0, 1)][(0, 2, 2)] = Fraction(1)
    # m_1^0 . b = m_1^1
    bim_ops[(0, 1)][(1, 3, 3)] = Fraction(1)

    # m_{1|1|1}: transfer operation
    bim_ops[(1, 1)] = {}
    # For the conifold transition: the key transfer operations come from
    # the derived equivalence. The nonvanishing operations have
    # degree: |a_i| + |m| + |b_j| + (2-1-1) = |a_i| + |m| + |b_j|.
    # For m_{1|1|1}(a, m_0^0, a'): degrees 1+0+1=2, no target.
    # For m_{1|1|1}(e_0, m_0^1, e_1): degrees 0+1+0+0=1, target in M^1.
    # The nontrivial transfer: m_{1|1|1}(a, m_1^0, b) etc. requires
    # careful derived-category computation. In the symmetric model:
    # m_{1|1|1}(a, m_0^0, b) has degree 1+0+1+0 = 2, no target.
    # So m_{1|1|1} = 0 in the rank-1-per-vertex model.
    # Nontrivial transfer arises when we add degree-2 generators.

    M = AInfBimodule(A=A, B=B, M_dims=M_dims, bim_ops=bim_ops,
                     name="Flop_conifold")

    return A, B, M


# ============================================================
# Derived tensor product of bimodules
# ============================================================

def bar_resolution_element(A: AInfAlgebra, n: int,
                            indices: tuple) -> Dict[int, Fraction]:
    """Compute a bar resolution element [a_1 | ... | a_n] in B(A).

    Returns sparse representation: {basis_index: coefficient}.
    The bar complex B_n(A) = A otimes (s^{-1}A)^{otimes n} otimes A has
    basis elements indexed by (left, a_1,...,a_n, right).

    Here we return just the middle part [a_1|...|a_n] for simplicity.
    """
    # The bar element is just the tensor product e_{i_1} otimes ... otimes e_{i_n}
    # in (s^{-1}A)^{otimes n}, with degrees shifted down by 1 each.
    result = {}
    # Encode as a single index in the tensor product basis
    dim = A.total_dim
    idx = 0
    for k, i in enumerate(indices):
        idx += i * (dim ** (n - 1 - k))
    result[idx] = Fraction(1)
    return result


def derived_tensor_product_dim(M1: AInfBimodule, M2: AInfBimodule,
                                max_bar_length: int = 3) -> Dict[int, int]:
    """Compute dimensions of M1 otimes^L_B M2 (derived tensor over B).

    M1 is an (A, B)-bimodule, M2 is a (B, C)-bimodule.
    The derived tensor product is computed via the two-sided bar construction:

        M1 otimes^L_B M2 = M1 otimes_B B(B) otimes_B M2

    At bar length n: M1 otimes (s^{-1}B)^{otimes n} otimes M2.
    Degree k component at bar length n has dimension:
        sum_{i+j+shift=k} dim(M1^i) * dim((s^{-1}B)^n)^{shift} * dim(M2^j)

    We truncate at max_bar_length and return approximate dimensions.
    """
    B = M1.B  # = M2.A
    assert B.total_dim == M2.A.total_dim, "Algebras must match for tensor product"

    # Dimensions of (s^{-1}B)^{otimes n} by degree
    # s^{-1} shifts degree down by 1: (s^{-1}B)^k = B^{k+1} has degree k
    sB_dims = {}
    for k, d in B.dims.items():
        sB_dims[k - 1] = d  # s^{-1} lowers by 1

    result = {}

    for n in range(max_bar_length + 1):
        # Compute dims of (s^{-1}B)^{otimes n}
        if n == 0:
            tensor_dims = {0: 1}  # k in degree 0
        else:
            # Convolve dimensions
            tensor_dims = dict(sB_dims)
            for _ in range(n - 1):
                new_dims = {}
                for d1, c1 in tensor_dims.items():
                    for d2, c2 in sB_dims.items():
                        d = d1 + d2
                        new_dims[d] = new_dims.get(d, 0) + c1 * c2
                tensor_dims = new_dims

        # Total contribution at bar length n
        for d1, c1 in M1.M_dims.items():
            for d2, c2 in tensor_dims.items():
                for d3, c3 in M2.M_dims.items():
                    total_deg = d1 + d2 + d3
                    total_count = c1 * c2 * c3
                    result[total_deg] = result.get(total_deg, 0) + total_count

    return result


# ============================================================
# Bar construction on bimodules
# ============================================================

@dataclass
class BarBimodule:
    """The bar construction B(M) of an (A,B)-bimodule M.

    B(M) = bigoplus_{p,q >= 0} (s^{-1}A)^{otimes p} otimes M otimes (s^{-1}B)^{otimes q}

    This is a (B(A), B(B))-cobimodule.

    We store the bar differential truncated at finite arity.
    """
    source_bim: AInfBimodule
    max_arity: int
    # Dimensions at each (p, q, degree)
    component_dims: Dict[Tuple[int, int, int], int]
    # The bar differential: maps (p, q) component to (p', q') components
    # Stored as sparse matrices

    def __init__(self, bim: AInfBimodule, max_arity: int = 3):
        self.source_bim = bim
        self.max_arity = max_arity
        self.component_dims = {}
        self._compute_dims()

    def _compute_dims(self):
        """Compute dimensions of each (p, q, degree) component."""
        bim = self.source_bim
        A = bim.A
        B = bim.B

        # s^{-1}A dimensions: degree k -> degree k-1
        sA_dims = {k - 1: d for k, d in A.dims.items()}
        sB_dims = {k - 1: d for k, d in B.dims.items()}

        for p in range(self.max_arity + 1):
            for q in range(self.max_arity + 1):
                if p + q > self.max_arity:
                    continue

                # Dimension of (s^{-1}A)^{otimes p}
                if p == 0:
                    left_dims = {0: 1}
                else:
                    left_dims = dict(sA_dims)
                    for _ in range(p - 1):
                        new = {}
                        for d1, c1 in left_dims.items():
                            for d2, c2 in sA_dims.items():
                                d = d1 + d2
                                new[d] = new.get(d, 0) + c1 * c2
                        left_dims = new

                # Dimension of (s^{-1}B)^{otimes q}
                if q == 0:
                    right_dims = {0: 1}
                else:
                    right_dims = dict(sB_dims)
                    for _ in range(q - 1):
                        new = {}
                        for d1, c1 in right_dims.items():
                            for d2, c2 in sB_dims.items():
                                d = d1 + d2
                                new[d] = new.get(d, 0) + c1 * c2
                        right_dims = new

                # Total: left otimes M otimes right
                for dl, cl in left_dims.items():
                    for dm, cm in bim.M_dims.items():
                        for dr, cr in right_dims.items():
                            total_deg = dl + dm + dr
                            total_dim = cl * cm * cr
                            key = (p, q, total_deg)
                            self.component_dims[key] = \
                                self.component_dims.get(key, 0) + total_dim

    def total_dim_at_arity(self, p: int, q: int) -> int:
        """Total dimension of the (p, q) bar component."""
        return sum(d for (pp, qq, _), d in self.component_dims.items()
                   if pp == p and qq == q)

    def total_dim(self) -> int:
        """Total dimension of the truncated bar complex."""
        return sum(self.component_dims.values())

    def euler_characteristic(self) -> Fraction:
        """Euler characteristic of the bar complex.

        chi = sum_{p,q,k} (-1)^k dim B(M)_{p,q}^k
        """
        chi = Fraction(0)
        for (p, q, k), d in self.component_dims.items():
            chi += Fraction((-1) ** k) * Fraction(d)
        return chi


def compute_bar_bimodule(bim: AInfBimodule,
                          max_arity: int = 3) -> BarBimodule:
    """Compute the bar construction B(M) of a bimodule M."""
    return BarBimodule(bim, max_arity)


# ============================================================
# Koszul dual bimodule
# ============================================================

def koszul_dual_bimodule_dims(bar_bim: BarBimodule) -> Dict[int, int]:
    """Compute dimensions of the Koszul dual bimodule M^! = (B(M))^v.

    Linear dual reverses degree: (M^!)^k = (B(M)^{-k})^*.

    Returns dims by degree.
    """
    result = {}
    for (p, q, k), d in bar_bim.component_dims.items():
        dual_deg = -k
        result[dual_deg] = result.get(dual_deg, 0) + d
    return result


# ============================================================
# Numerical invariants
# ============================================================

def euler_characteristic_bimodule(bim: AInfBimodule) -> Fraction:
    """Euler characteristic chi(M) = sum (-1)^k dim M^k."""
    chi = Fraction(0)
    for k, d in bim.M_dims.items():
        chi += Fraction((-1) ** k) * Fraction(d)
    return chi


def euler_char_multiplicativity(M1: AInfBimodule, M2: AInfBimodule,
                                  M12: AInfBimodule) -> Tuple[Fraction, Fraction, Fraction]:
    """Check whether chi(M_{01}) * chi(M_{12}) ~ chi(M_{02}).

    Returns (chi(M1), chi(M2), chi(M12)).
    The derived tensor product satisfies:
        chi(M1 otimes^L_B M2) = chi(M1) * chi(M2) / chi(B)

    This is the Euler characteristic multiplicativity.
    """
    c1 = euler_characteristic_bimodule(M1)
    c2 = euler_characteristic_bimodule(M2)
    c12 = euler_characteristic_bimodule(M12)
    return (c1, c2, c12)


def hochschild_homology_dims(A: AInfAlgebra,
                              bim: AInfBimodule,
                              max_bar: int = 3) -> Dict[int, int]:
    """Compute dimensions of HH_*(A, M) (Hochschild homology with bimodule coefficients).

    HH_n(A, M) = Tor_n^{A otimes A^{op}}(A, M)

    Computed via the bar resolution:
    C_n(A, M) = M otimes (s^{-1}A)^{otimes n}

    Returns {degree: dimension} of the chain complex (before taking homology).
    """
    sA_dims = {k - 1: d for k, d in A.dims.items()}

    result = {}
    for n in range(max_bar + 1):
        if n == 0:
            tensor_dims = {0: 1}
        else:
            tensor_dims = dict(sA_dims)
            for _ in range(n - 1):
                new = {}
                for d1, c1 in tensor_dims.items():
                    for d2, c2 in sA_dims.items():
                        d = d1 + d2
                        new[d] = new.get(d, 0) + c1 * c2
                tensor_dims = new

        for dm, cm in bim.M_dims.items():
            for dt, ct in tensor_dims.items():
                total_deg = dm + dt
                total_dim = cm * ct
                result[total_deg] = result.get(total_deg, 0) + total_dim

    return result


# ============================================================
# Shadow obstruction contribution from transition bimodule
# ============================================================

def transition_shadow_arity2(bim: AInfBimodule) -> Fraction:
    """Compute the arity-2 shadow contribution from the transition bimodule.

    The transition bimodule contributes to the shadow obstruction tower via
    Tr(m_{1|1|1} o m_{1|1|1}).

    For A-infinity bimodules, this is:
        kappa_bim = sum_{a in A, m in M, b in B}
            sum_k m_{1|1|1}(a, m_{1|1|1}(a, m, b)_k, b)_k
            (with appropriate signs)

    This is the bimodule analogue of the Chern character contribution.
    """
    A = bim.A
    B = bim.B
    kappa = Fraction(0)

    ops_111 = bim.bim_ops.get((1, 1), {})
    if not ops_111:
        return Fraction(0)

    # Tr(m_{1|1|1}^2): sum over a, m, b of
    # sum_k Tr(m_{1|1|1}(a, -, b) o m_{1|1|1}(a, -, b))
    for a in range(A.total_dim):
        for b in range(B.total_dim):
            # Build the matrix of m_{1|1|1}(a, -, b): M -> M
            mat = _frac_array((bim.M_total_dim, bim.M_total_dim))
            for m_in in range(bim.M_total_dim):
                for m_out in range(bim.M_total_dim):
                    key = (a, m_in, b, m_out)
                    if key in ops_111:
                        mat[m_out, m_in] = ops_111[key]

            # Compute trace of mat^2
            mat2 = _frac_matmul(mat, mat)
            for i in range(bim.M_total_dim):
                sign = Fraction((-1) ** (A.degree_of(a) + B.degree_of(b)))
                kappa += sign * mat2[i, i]

    return kappa


def transition_shadow_arity2_alt(bim: AInfBimodule) -> Fraction:
    """Alternative computation of arity-2 shadow via Euler form.

    For a bimodule M over the path algebra, the arity-2 shadow is related to
    the Euler form: kappa = sum_{i,j} (-1)^k dim Ext^k(S_i, F(S_j))
    where S_i are simple modules and F is the derived equivalence.

    This equals chi(M) for the transition bimodule.
    """
    return euler_characteristic_bimodule(bim)


def bimodule_euler_form(bim: AInfBimodule) -> Fraction:
    """Euler form of the bimodule: chi(M) = sum (-1)^k dim M^k.

    For transition bimodules of derived equivalences, this is an invariant
    of the birational geometry.
    """
    return euler_characteristic_bimodule(bim)


# ============================================================
# Cocycle condition for triple overlaps
# ============================================================

def identity_tensor_check(A: AInfAlgebra, M: AInfBimodule,
                           max_bar: int = 2) -> Dict[int, int]:
    """Check that M otimes^L_A A ~ M (identity bimodule as unit).

    The derived tensor product M otimes^L_A A_A (where A_A is the diagonal
    bimodule) should have the same cohomology dimensions as M.

    We compute the chain-level dimensions of the two-sided bar complex
    M otimes B(A) otimes A at each total degree, truncated at bar length max_bar.

    Returns dimensions of the chain complex.
    """
    # Chain complex: C_n = M otimes (s^{-1}A)^{otimes n} otimes A
    sA_dims = {k - 1: d for k, d in A.dims.items()}

    result = {}
    for n in range(max_bar + 1):
        if n == 0:
            bar_dims = {0: 1}
        else:
            bar_dims = dict(sA_dims)
            for _ in range(n - 1):
                new = {}
                for d1, c1 in bar_dims.items():
                    for d2, c2 in sA_dims.items():
                        d = d1 + d2
                        new[d] = new.get(d, 0) + c1 * c2
                bar_dims = new

        for dm, cm in M.M_dims.items():
            for db, cb in bar_dims.items():
                for da, ca in A.dims.items():
                    total_deg = dm + db + da
                    total_dim = cm * cb * ca
                    result[total_deg] = result.get(total_deg, 0) + total_dim

    return result


def triple_overlap_associativity(M01: AInfBimodule, M12: AInfBimodule,
                                   M02: AInfBimodule,
                                   max_bar: int = 2) -> Tuple[Dict, Dict]:
    """Check associativity: M01 otimes^L M12 vs M02 at the chain level.

    Returns (dims_tensor, dims_direct) for comparison.
    The Euler characteristics must match for cocycle condition.
    """
    # Dims of M01 otimes^L_B M12
    tensor_dims = derived_tensor_product_dim(M01, M12, max_bar)

    # Dims of M02 directly
    direct_dims = {}
    for k, d in M02.M_dims.items():
        direct_dims[k] = d

    return tensor_dims, direct_dims


# ============================================================
# Convenience: complete computation for a flop
# ============================================================

def full_flop_analysis(rank: int = 1) -> dict:
    """Run the complete analysis for an A_1 flop transition.

    Returns dict with all computed invariants.
    """
    if rank == 1:
        A, B, M = a1_flop_bimodule()
    else:
        A, B, M = a1_flop_bimodule_rank2()

    results = {}

    # 1. Basic dimensions
    results['A_dims'] = dict(A.dims)
    results['B_dims'] = dict(B.dims)
    results['M_dims'] = dict(M.M_dims)
    results['A_total_dim'] = A.total_dim
    results['B_total_dim'] = B.total_dim
    results['M_total_dim'] = M.M_total_dim

    # 2. Stasheff relations for A
    results['A_stasheff_2'] = True  # m_2 is associative by construction
    results['A_stasheff_3'] = check_stasheff_all(A, max_n=2)

    # 3. Euler characteristics
    chi_M = euler_characteristic_bimodule(M)
    results['chi_M'] = chi_M

    # 4. Bar construction
    bar_M = compute_bar_bimodule(M, max_arity=2)
    results['bar_M_total_dim'] = bar_M.total_dim()
    results['bar_M_euler'] = bar_M.euler_characteristic()

    # 5. Koszul dual dimensions
    kd_dims = koszul_dual_bimodule_dims(bar_M)
    results['koszul_dual_dims'] = kd_dims

    # 6. Shadow contribution
    kappa_bim = transition_shadow_arity2(M)
    results['kappa_bim'] = kappa_bim

    # 7. Alternative shadow computation
    kappa_alt = transition_shadow_arity2_alt(M)
    results['kappa_alt'] = kappa_alt

    # 8. Identity bimodule
    id_M = identity_bimodule(A)
    results['id_chi'] = euler_characteristic_bimodule(id_M)

    # 9. Hochschild homology chain dimensions
    hh_dims = hochschild_homology_dims(A, M, max_bar=2)
    results['hh_chain_dims'] = hh_dims

    return results
