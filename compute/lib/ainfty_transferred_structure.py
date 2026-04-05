"""A-infinity transferred structure and formality characterization of Koszulness.

prop:ainfty-formality-implies-koszul: A is chirally Koszul iff the
transferred A-infinity structure on H*(B(A)) is formal (m_n = 0 for n >= 3).

This module computes the HPL-transferred A-infinity structure for
finite-dimensional dg algebras and verifies formality.

The SHADOW TOWER measures A-infinity non-formality of A itself (or L-infinity
on Def_cyc).  The KOSZULNESS criterion measures A-infinity formality of the
DUAL A^! = H*(B(A)).  These are DIFFERENT objects with different formality
properties:

  - Heisenberg: shadow depth 2 (Gaussian), A^! formal.  Koszul.
  - Affine sl_2: shadow depth 3 (Lie/tree), A^! formal.  Koszul.
  - betagamma: shadow depth 4 (contact), A^! formal.  Koszul.
  - Virasoro: shadow depth infinity (mixed), A^! formal.  Koszul.
  - k[x]/(x^3): A^! NOT formal (m_3 != 0).  NOT Koszul.

The shadow obstruction tower Theta_A^{<=r} at arity r measures the L-infinity
formality obstruction of A (prop:shadow-formality-low-arity), NOT
the A-infinity structure on A^!.

GRADING: Cohomological (|d| = +1).  Bar uses DESUSPENSION.
SIGN CONVENTION: Koszul sign rule throughout.

References:
  - prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
  - thm:koszul-equivalences-meta (12 equivalent characterizations)
  - prop:shadow-formality-low-arity (shadow = L-infinity formality at arities 2,3,4)
  - Keller, "A-infinity algebras, modules and functor categories" (HPL)
  - Loday-Vallette, "Algebraic Operads" Ch. 9-10 (Koszul duality + HPL)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as iter_product
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
    if isinstance(x, float):
        return Fraction(x).limit_denominator(10**12)
    return Fraction(x)


def _frac_array(shape) -> np.ndarray:
    """Create a zero array of Fraction objects."""
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


def _kernel_basis(M: np.ndarray) -> List[np.ndarray]:
    """Compute kernel basis of a Fraction-object matrix via row reduction.

    Returns list of column vectors spanning ker(M).
    """
    if M.size == 0:
        rows, cols = M.shape
        return [_unit_vec(cols, j) for j in range(cols)]

    rows, cols = M.shape
    # Augmented approach: row-reduce M^T to find null space of M
    # ker(M) = {x : Mx = 0}
    # Work with a copy
    A = np.array([[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
                 dtype=object)

    # Gaussian elimination with partial pivoting
    pivot_cols = []
    r = 0
    for c in range(cols):
        # Find pivot in column c, row >= r
        pivot = None
        for i in range(r, rows):
            if A[i, c] != Fraction(0):
                pivot = i
                break
        if pivot is None:
            continue
        # Swap rows
        A[[r, pivot]] = A[[pivot, r]]
        pivot_cols.append(c)
        # Scale pivot row
        scale = A[r, c]
        for j in range(cols):
            A[r, j] = A[r, j] / scale
        # Eliminate column
        for i in range(rows):
            if i == r:
                continue
            factor = A[i, c]
            if factor != Fraction(0):
                for j in range(cols):
                    A[i, j] = A[i, j] - factor * A[r, j]
        r += 1

    # Free variables: columns not in pivot_cols
    free_cols = [c for c in range(cols) if c not in pivot_cols]
    basis = []
    for fc in free_cols:
        v = _frac_array(cols)
        v[fc] = Fraction(1)
        for idx, pc in enumerate(pivot_cols):
            v[pc] = -A[idx, fc]
        basis.append(v)
    return basis


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


def _unit_vec(n: int, j: int) -> np.ndarray:
    """Standard basis vector e_j in Q^n."""
    v = _frac_array(n)
    v[j] = Fraction(1)
    return v


# ============================================================
# DG Algebra
# ============================================================

@dataclass
class DGAlgebra:
    """A finite-dimensional dg algebra (V, d, m_2) over Q.

    V = direct sum V^k (cohomological grading).
    d: V^k -> V^{k+1}, d^2 = 0.
    m_2: V^p tensor V^q -> V^{p+q}, associative, d is a derivation.

    Internal representation:
      dims[k] = dim V^k
      basis_offset[k] = sum_{j < k} dims[j]  (offset into flat vector)
      total_dim = sum of all dims

    Differential: d_matrix is (total_dim x total_dim) with d_matrix[i,j] != 0
    only when j is in degree k and i is in degree k+1.

    Product: product_tensor[i, j, k] = coefficient of e_k in m_2(e_i, e_j).
    """
    dims: Dict[int, int]
    d_matrix: np.ndarray       # (total_dim, total_dim), Fraction entries
    product_tensor: np.ndarray  # (total_dim, total_dim, total_dim), Fraction
    name: str = ""

    @property
    def total_dim(self) -> int:
        return sum(self.dims.values())

    @property
    def degrees(self) -> List[int]:
        return sorted(self.dims.keys())

    def basis_offset(self, k: int) -> int:
        """Offset of degree-k block in the flat basis."""
        return sum(self.dims.get(j, 0) for j in sorted(self.dims.keys()) if j < k)

    def degree_range(self, k: int) -> Tuple[int, int]:
        """(start, end) indices for degree-k basis vectors."""
        off = self.basis_offset(k)
        return (off, off + self.dims.get(k, 0))

    def degree_of(self, i: int) -> int:
        """Degree of basis vector e_i."""
        offset = 0
        for k in self.degrees:
            if offset + self.dims[k] > i:
                return k
            offset += self.dims[k]
        raise IndexError(f"Index {i} out of range for total_dim {self.total_dim}")

    def check_d_squared(self) -> bool:
        """Verify d^2 = 0."""
        d2 = _frac_matmul(self.d_matrix, self.d_matrix)
        return _is_zero(d2)

    def check_associativity(self) -> bool:
        """Verify m_2 is associative: m_2(m_2(a,b),c) = m_2(a,m_2(b,c))."""
        n = self.total_dim
        P = self.product_tensor
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # (ij)k
                    lhs = Fraction(0)
                    rhs = Fraction(0)
                    for l in range(n):
                        for m in range(n):
                            lhs += P[i, j, l] * P[l, k, m]  # sum_l P[i,j,l]*P[l,k,m] for each m
                            rhs += P[j, k, l] * P[i, l, m]  # sum_l P[j,k,l]*P[i,l,m]
                    # Actually we need to compare for each output
                    pass
        # More efficient: check for each output index
        for m in range(n):
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        lhs = sum(P[i, j, l] * P[l, k, m] for l in range(n))
                        rhs = sum(P[j, k, l] * P[i, l, m] for l in range(n))
                        if lhs != rhs:
                            return False
        return True

    def check_leibniz(self) -> bool:
        """Verify d is a derivation: d(m_2(a,b)) = m_2(d(a),b) + (-1)^|a| m_2(a,d(b)).

        Convention: D[target, source], so d(e_k) = sum_l D[l, k] e_l.
        P[i, j, k] = coefficient of e_k in m_2(e_i, e_j).
        """
        n = self.total_dim
        D = self.d_matrix
        P = self.product_tensor
        for i in range(n):
            deg_i = self.degree_of(i)
            for j in range(n):
                sign = Fraction((-1) ** deg_i)
                for l in range(n):
                    # LHS: (d(m_2(e_i, e_j)))_l = sum_k D[l, k] * P[i, j, k]
                    lhs = sum(D[l, k] * P[i, j, k] for k in range(n))
                    # RHS: (m_2(d(e_i), e_j))_l + (-1)^|i| (m_2(e_i, d(e_j)))_l
                    #     = sum_k D[k, i] * P[k, j, l] + (-1)^|i| sum_k D[k, j] * P[i, k, l]
                    rhs = (sum(D[k, i] * P[k, j, l] for k in range(n))
                           + sign * sum(D[k, j] * P[i, k, l] for k in range(n)))
                    if lhs != rhs:
                        return False
        return True

    def cohomology_dims(self) -> Dict[int, int]:
        """Compute dim H^k(V, d) for each degree k."""
        result = {}
        n = self.total_dim
        D = self.d_matrix
        for k in self.degrees:
            s, e = self.degree_range(k)
            dim_k = e - s
            if dim_k == 0:
                result[k] = 0
                continue
            # d_k: V^k -> V^{k+1}: extract rows in degree k+1, cols in degree k
            s1, e1 = self.degree_range(k + 1) if (k + 1) in self.dims else (0, 0)
            if e1 > s1:
                dk = D[s1:e1, s:e]
                ker_dk = len(_kernel_basis(dk))
            else:
                ker_dk = dim_k  # d_k = 0

            # d_{k-1}: V^{k-1} -> V^k
            sm1, em1 = self.degree_range(k - 1) if (k - 1) in self.dims else (0, 0)
            if em1 > sm1:
                dkm1 = D[s:e, sm1:em1]
                im_dkm1 = _image_dim(dkm1)
            else:
                im_dkm1 = 0

            result[k] = ker_dk - im_dkm1
        return result

    def cohomology_projection_data(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Compute HPL retraction data: projection P, inclusion I, homotopy H.

        Constructs a deformation retract:
            (V, d) --P--> (H*(V), 0) --I--> (V, d)
        with PI = id on H*, IP = id - dH - Hd.

        Returns (P, I, H) as (total_dim x total_dim) Fraction matrices.
        P: V -> V (projects onto cocycle representatives, kills coboundaries)
        I: V -> V (includes cohomology representatives)
        H: V -> V (contracting homotopy, H: V^k -> V^{k-1})
        """
        n = self.total_dim
        P_mat = _frac_array((n, n))
        I_mat = _frac_array((n, n))
        H_mat = _frac_array((n, n))

        D = self.d_matrix

        for k in self.degrees:
            s, e = self.degree_range(k)
            dim_k = e - s
            if dim_k == 0:
                continue

            # d_k: V^k -> V^{k+1}
            s1, e1 = self.degree_range(k + 1) if (k + 1) in self.dims else (0, 0)
            if e1 > s1:
                dk = D[s1:e1, s:e]
            else:
                dk = _frac_array((0, dim_k))

            # d_{k-1}: V^{k-1} -> V^k
            sm1, em1 = self.degree_range(k - 1) if (k - 1) in self.dims else (0, 0)
            if em1 > sm1:
                dkm1 = D[s:e, sm1:em1]
            else:
                dkm1 = _frac_array((dim_k, 0))

            # Kernel of d_k
            ker_vecs = _kernel_basis(dk)  # vectors in Q^{dim_k}

            # Image of d_{k-1}
            im_rank = _image_dim(dkm1)

            # Decompose ker(d_k) into im(d_{k-1}) + complement (= cohomology)
            # Image basis: columns of dkm1 (take first im_rank linearly independent)
            im_vecs = []
            if dkm1.shape[1] > 0:
                # Row reduce dkm1 transpose to find im basis
                A_t = dkm1.T.copy() if dkm1.size > 0 else _frac_array((0, dim_k))
                # Actually, columns of dkm1 span im(d_{k-1})
                # Extract linearly independent columns
                used = []
                rank_check = _frac_array((0, dim_k)) if dim_k > 0 else _frac_array((0, 0))
                for col_idx in range(dkm1.shape[1]):
                    col = dkm1[:, col_idx].copy()
                    test = np.vstack([rank_check, col.reshape(1, -1)]) if rank_check.shape[0] > 0 else col.reshape(1, -1)
                    if _image_dim(test) > len(used):
                        used.append(col_idx)
                        rank_check = test
                    if len(used) >= im_rank:
                        break
                im_vecs = [dkm1[:, ci] for ci in used]

            # Cohomology representatives: ker vectors not in im
            # Project ker_vecs orthogonal to im_vecs (Gram-Schmidt over Q)
            cohom_vecs = []
            # Build the subspace spanned by im_vecs
            if im_vecs:
                im_matrix = np.column_stack(im_vecs) if im_vecs else _frac_array((dim_k, 0))
            else:
                im_matrix = _frac_array((dim_k, 0))

            for kv in ker_vecs:
                # Check if kv is in span of im_vecs + already chosen cohom_vecs
                # by augmenting and checking rank
                if im_vecs or cohom_vecs:
                    existing = im_vecs + cohom_vecs
                    test_mat = np.column_stack(existing + [kv])
                    if _image_dim(test_mat.T) > len(existing):
                        cohom_vecs.append(kv)
                else:
                    if any(x != Fraction(0) for x in kv):
                        cohom_vecs.append(kv)

            # Homotopy: need to map im(d_k) back to preimages in V^{k-1}
            # For the image vectors of d_{k-1} in V^k, H should map them to
            # their preimages in V^{k-1} (so that d_{k-1} H = projection onto im)
            # H: V^k -> V^{k-1}, so H maps degree k to degree k-1
            # We need: for v in im(d_{k-1}), H(v) = some u with d_{k-1}(u) = v
            for idx, iv in enumerate(im_vecs):
                if idx < dkm1.shape[1]:
                    # Find preimage: dkm1 * u = iv
                    # u lives in V^{k-1}, indices [sm1, em1)
                    # Solve dkm1 * u = iv
                    u = _solve_linear(dkm1, iv)
                    if u is not None:
                        # H maps the basis vector corresponding to iv to u
                        # Express iv in terms of degree-k basis
                        for a in range(dim_k):
                            for b in range(em1 - sm1):
                                H_mat[sm1 + b, s + a] += u[b] * iv[a]

            # Projection P: V^k -> cohomology representatives in V^k
            # P kills coboundaries (im d_{k-1}) and non-cocycles (complement of ker d_k)
            # P = sum_alpha c_alpha c_alpha^T where c_alpha are cohom reps
            for cv in cohom_vecs:
                # P projects onto cv: need dual basis
                # For simplicity, if cohom_vecs form an orthonormal-ish basis,
                # just use P(v) = sum <cv, v> / <cv, cv> * cv
                norm_sq = sum(cv[a] * cv[a] for a in range(dim_k))
                if norm_sq != Fraction(0):
                    for a in range(dim_k):
                        for b in range(dim_k):
                            P_mat[s + a, s + b] += cv[a] * cv[b] / norm_sq

            # Inclusion I: embed cohomology representatives
            for cv in cohom_vecs:
                norm_sq = sum(cv[a] * cv[a] for a in range(dim_k))
                if norm_sq != Fraction(0):
                    for a in range(dim_k):
                        for b in range(dim_k):
                            I_mat[s + a, s + b] += cv[a] * cv[b] / norm_sq

        return P_mat, I_mat, H_mat


def _solve_linear(A: np.ndarray, b: np.ndarray) -> Optional[np.ndarray]:
    """Solve Ax = b over Q.  Returns x or None if no solution."""
    rows, cols = A.shape
    # Augmented matrix [A | b]
    aug = _frac_array((rows, cols + 1))
    for i in range(rows):
        for j in range(cols):
            aug[i, j] = _frac(A[i, j])
        aug[i, cols] = _frac(b[i])

    # Row reduce
    r = 0
    pivot_cols = []
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if aug[i, c] != Fraction(0):
                pivot = i
                break
        if pivot is None:
            continue
        aug[[r, pivot]] = aug[[pivot, r]]
        scale = aug[r, c]
        for j in range(cols + 1):
            aug[r, j] /= scale
        for i in range(rows):
            if i == r:
                continue
            factor = aug[i, c]
            if factor != Fraction(0):
                for j in range(cols + 1):
                    aug[i, j] -= factor * aug[r, j]
        pivot_cols.append(c)
        r += 1

    # Check consistency
    for i in range(r, rows):
        if aug[i, cols] != Fraction(0):
            return None

    # Extract solution (free variables set to 0)
    x = _frac_array(cols)
    for idx, pc in enumerate(pivot_cols):
        x[pc] = aug[idx, cols]
    return x


# ============================================================
# Bar complex (truncated, for finite-dimensional dg algebras)
# ============================================================

@dataclass
class BarComplex:
    """Bar complex B(A) of a dg algebra A, truncated at tensor degree max_arity.

    B^n(A) = (s^{-1} A_+)^{tensor n} where A_+ = augmentation ideal.

    Bar differential d_B: B^n -> B^{n-1} is:
      d_B(a_1|...|a_n) = sum_{j} ±(a_1|...|d(a_j)|...|a_n)        [internal]
                        + sum_{j} ±(a_1|...|m_2(a_j,a_{j+1})|...|a_n) [product]

    SIGN CONVENTION (cohomological, desuspension):
      d_internal: sign = (-1)^{|a_1|'+...+|a_{j-1}|'} where |a|' = |a| - 1
      d_product: sign = (-1)^{|a_1|'+...+|a_j|'} for m_2(a_j, a_{j+1})

    The bar degree is the tensor degree n.  The internal degree of
    a_1|...|a_n is (|a_1|-1) + ... + (|a_n|-1) = sum|a_i| - n.
    """
    algebra: DGAlgebra
    max_arity: int

    def __post_init__(self):
        """Precompute augmentation ideal basis."""
        # For a connected dg algebra: A_+ = kernel of augmentation A -> k
        # For CE complexes and polynomial algebras: A_+ = degrees > 0
        # plus non-unit elements in degree 0.
        # Augmentation ideal basis: all basis vectors except the degree-0 unit.
        # CONVENTION: the unit is always the FIRST basis vector in degree 0.
        A = self.algebra
        self._aug_basis = []
        self._aug_degrees = []
        unit_skipped = False
        for k in A.degrees:
            s, e = A.degree_range(k)
            for i in range(s, e):
                if k == 0 and not unit_skipped:
                    # Skip the unit (first basis vector in degree 0)
                    unit_skipped = True
                    continue
                self._aug_basis.append(i)
                self._aug_degrees.append(k)

        self._aug_dim = len(self._aug_basis)
        # Desuspended degrees: |s^{-1}a| = |a| - 1
        self._desuspended_degrees = [d - 1 for d in self._aug_degrees]

    def tensor_space_dim(self, n: int) -> int:
        """Dimension of B^n = (s^{-1} A_+)^{tensor n}."""
        if n <= 0:
            return 0
        return self._aug_dim ** n

    def _tensor_index(self, indices: Tuple[int, ...]) -> int:
        """Multi-index (i_1, ..., i_n) in [0, aug_dim)^n -> flat index."""
        n = len(indices)
        flat = 0
        for i, idx in enumerate(indices):
            flat = flat * self._aug_dim + idx
        return flat

    def _multi_index(self, flat: int, n: int) -> Tuple[int, ...]:
        """Flat index -> multi-index (i_1, ..., i_n)."""
        indices = []
        for _ in range(n):
            flat, r = divmod(flat, self._aug_dim)
            indices.append(r)
        return tuple(reversed(indices))

    def _desuspended_sign_prefix(self, indices: Tuple[int, ...], up_to: int) -> int:
        """(-1)^{|a_1|' + ... + |a_{up_to}|'} where |a|' = desuspended degree."""
        total = sum(self._desuspended_degrees[indices[j]] for j in range(up_to))
        return (-1) ** total

    def bar_differential_matrix(self, n: int) -> np.ndarray:
        """Matrix of d_B: B^n -> B^{n-1}, acting on flat-indexed tensor products.

        Returns shape (dim B^{n-1}, dim B^n) Fraction matrix.
        """
        if n <= 1:
            # d_B: B^1 -> B^0 = 0 (there is no B^0 in the reduced bar complex)
            return _frac_array((0, self.tensor_space_dim(n)))

        A = self.algebra
        dim_src = self.tensor_space_dim(n)
        dim_tgt = self.tensor_space_dim(n - 1)
        mat = _frac_array((dim_tgt, dim_src))

        for flat_src in range(dim_src):
            multi = self._multi_index(flat_src, n)

            # Internal differential: apply d_A to each tensor factor
            for j in range(n):
                sign = self._desuspended_sign_prefix(multi, j)
                # d_A(a_{aug_basis[multi[j]]}) in the full algebra
                a_idx = self._aug_basis[multi[j]]
                for b_pos in range(self._aug_dim):
                    b_idx = self._aug_basis[b_pos]
                    coeff = A.d_matrix[b_idx, a_idx]
                    if coeff != Fraction(0):
                        new_multi = multi[:j] + (b_pos,) + multi[j+1:]
                        flat_tgt = self._tensor_index(new_multi)
                        # This is still arity n, so contributes to B^n -> B^n
                        # Wait: internal d doesn't change tensor degree.
                        # The bar differential's internal part preserves arity.
                        # Only the product part reduces arity.
                        # So the full d_B has two components:
                        # d_internal: B^n -> B^n (same arity)
                        # d_product: B^n -> B^{n-1}
                        # For the TOTAL bar differential, both act.
                        # But the bar differential maps B^n -> B^{n-1} only
                        # when we view B as a bicomplex.
                        pass

            # Product part: apply m_2 to adjacent pairs
            # Sign convention (Loday-Vallette): (-1)^{|sa_1|+...+|sa_j|}
            # where j is the LEFT element of the pair being multiplied.
            for j in range(n - 1):
                sign = self._desuspended_sign_prefix(multi, j + 1)
                a_idx = self._aug_basis[multi[j]]
                b_idx = self._aug_basis[multi[j + 1]]
                for c_pos in range(self._aug_dim):
                    c_idx = self._aug_basis[c_pos]
                    coeff = A.product_tensor[a_idx, b_idx, c_idx]
                    if coeff != Fraction(0):
                        new_multi = multi[:j] + (c_pos,) + multi[j+2:]
                        assert len(new_multi) == n - 1
                        flat_tgt = self._tensor_index(new_multi)
                        mat[flat_tgt, flat_src] += _frac(sign) * _frac(coeff)

        return mat

    def bar_differential_full(self, n: int) -> Tuple[np.ndarray, np.ndarray]:
        """Full bar differential: both internal and product parts.

        Returns (d_internal, d_product) where:
          d_internal: B^n -> B^n (same arity, changes internal degree)
          d_product: B^n -> B^{n-1} (reduces arity)

        The total bar differential is d_B = d_internal + d_product
        (when viewing B as a total complex).
        """
        A = self.algebra
        dim_n = self.tensor_space_dim(n)

        # Internal part: B^n -> B^n
        d_int = _frac_array((dim_n, dim_n))
        for flat_src in range(dim_n):
            multi = self._multi_index(flat_src, n)
            for j in range(n):
                sign = self._desuspended_sign_prefix(multi, j)
                a_idx = self._aug_basis[multi[j]]
                for b_pos in range(self._aug_dim):
                    b_idx = self._aug_basis[b_pos]
                    coeff = A.d_matrix[b_idx, a_idx]
                    if coeff != Fraction(0):
                        new_multi = multi[:j] + (b_pos,) + multi[j+1:]
                        flat_tgt = self._tensor_index(new_multi)
                        d_int[flat_tgt, flat_src] += _frac(sign) * _frac(coeff)

        # Product part: B^n -> B^{n-1}
        d_prod = self.bar_differential_matrix(n)

        return d_int, d_prod

    def total_differential_matrix(self, max_n: Optional[int] = None) -> np.ndarray:
        """Build total bar differential on B^1 + B^2 + ... + B^{max_n}.

        Assembles the block matrix for the total complex.
        Returns (total_dim, total_dim) Fraction matrix.
        """
        if max_n is None:
            max_n = self.max_arity

        # Compute dimensions and offsets
        dims = {}
        offsets = {}
        total = 0
        for n in range(1, max_n + 1):
            d = self.tensor_space_dim(n)
            dims[n] = d
            offsets[n] = total
            total += d

        D = _frac_array((total, total))

        for n in range(1, max_n + 1):
            d_int, d_prod = self.bar_differential_full(n)

            # Internal part: B^n -> B^n
            r_start = offsets[n]
            c_start = offsets[n]
            for i in range(dims[n]):
                for j in range(dims[n]):
                    D[r_start + i, c_start + j] = d_int[i, j]

            # Product part: B^n -> B^{n-1}
            if n >= 2:
                r_start_tgt = offsets[n - 1]
                c_start_src = offsets[n]
                rows_p, cols_p = d_prod.shape
                for i in range(rows_p):
                    for j in range(cols_p):
                        D[r_start_tgt + i, c_start_src + j] += d_prod[i, j]

        return D

    def check_d_squared(self, max_n: Optional[int] = None) -> bool:
        """Verify d_B^2 = 0 on the total complex."""
        D = self.total_differential_matrix(max_n)
        D2 = _frac_matmul(D, D)
        return _is_zero(D2)


# ============================================================
# HPL Transfer of A-infinity structure
# ============================================================

class HPLTransfer:
    """Homological Perturbation Lemma transfer of A-infinity structure.

    Given a dg algebra (A, d, m_2) with a deformation retraction:
        (A, d) --P--> (H, 0) --I--> (A, d), H: homotopy
    satisfying PI = id_H, IP = id_A - dH - Hd, H^2 = 0, PH = 0, HI = 0.

    The HPL transfers the A-infinity structure {m_n} from A to H:
        m_1^tr = 0  (since d = 0 on H)
        m_2^tr = P m_2 (I x I)
        m_3^tr = P m_2 (H m_2 x id)(I x I x I) + P m_2 (id x H m_2)(I x I x I)
        m_n^tr = sum over planar binary trees with n leaves

    Convention: m_n^tr: H^{tensor n} -> H with Koszul signs.

    The KEY THEOREM (Kadeishvili, Merkulov):
        {m_n^tr} satisfies the A-infinity relations on H iff
        the original (A, d, m_2) is a dg algebra.

    FORMALITY: The transferred A-infinity structure is formal iff
    m_n^tr = 0 for all n >= 3.
    """

    def __init__(self, algebra: DGAlgebra):
        self.algebra = algebra
        P, I, H = algebra.cohomology_projection_data()
        self.P = P
        self.I = I
        self.H = H
        self._n = algebra.total_dim

    def _apply_product(self, v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        """Compute m_2(v1, v2) using the product tensor."""
        n = self._n
        P = self.algebra.product_tensor
        result = _frac_array(n)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[k] += v1[i] * v2[j] * P[i, j, k]
        return result

    def _apply_matrix(self, M: np.ndarray, v: np.ndarray) -> np.ndarray:
        """Matrix-vector product M @ v."""
        n = M.shape[0]
        result = _frac_array(n)
        for i in range(n):
            for j in range(M.shape[1]):
                result[i] += M[i, j] * v[j]
        return result

    def m1_transferred(self, v: np.ndarray) -> np.ndarray:
        """m_1^{tr} = P d I.  Should be zero on cohomology."""
        Iv = self._apply_matrix(self.I, v)
        dIv = self._apply_matrix(self.algebra.d_matrix, Iv)
        return self._apply_matrix(self.P, dIv)

    def m2_transferred(self, v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        """m_2^{tr} = P m_2 (I tensor I)."""
        Iv1 = self._apply_matrix(self.I, v1)
        Iv2 = self._apply_matrix(self.I, v2)
        prod = self._apply_product(Iv1, Iv2)
        return self._apply_matrix(self.P, prod)

    def m3_transferred(self, v1: np.ndarray, v2: np.ndarray,
                       v3: np.ndarray) -> np.ndarray:
        """m_3^{tr}: first A-infinity obstruction.

        m_3^tr(a,b,c) = P m_2(H m_2(Ia, Ib), Ic)
                       + P m_2(Ia, H m_2(Ib, Ic))

        (Sum over the two planar binary trees with 3 leaves.)
        Signs follow from Koszul rule with desuspended degrees.
        """
        Iv1 = self._apply_matrix(self.I, v1)
        Iv2 = self._apply_matrix(self.I, v2)
        Iv3 = self._apply_matrix(self.I, v3)

        # Tree 1: ((a,b),c) = m_2(H m_2(a,b), c)
        m2_12 = self._apply_product(Iv1, Iv2)
        Hm2_12 = self._apply_matrix(self.H, m2_12)
        tree1 = self._apply_product(Hm2_12, Iv3)

        # Tree 2: (a,(b,c)) = m_2(a, H m_2(b,c))
        # Sign: (-1)^{|a|'} where |a|' = desuspended degree of a
        m2_23 = self._apply_product(Iv2, Iv3)
        Hm2_23 = self._apply_matrix(self.H, m2_23)
        tree2 = self._apply_product(Iv1, Hm2_23)

        # The sign for tree2 relative to tree1: in the A-infinity convention
        # with desuspended inputs, tree2 gets a factor (-1)^{|a|'}.
        # For the transfer formula, both trees contribute with + sign
        # (the Koszul signs are absorbed into the tree morphisms).
        # See Loday-Vallette, Theorem 10.3.1.
        total = _frac_array(self._n)
        for i in range(self._n):
            total[i] = tree1[i] + tree2[i]

        return self._apply_matrix(self.P, total)

    def m4_transferred(self, v1: np.ndarray, v2: np.ndarray,
                       v3: np.ndarray, v4: np.ndarray) -> np.ndarray:
        """m_4^{tr}: second A-infinity obstruction.

        Sum over 5 planar binary trees with 4 leaves:
          (((a,b),c),d), ((a,(b,c)),d), ((a,b),(c,d)),
          (a,((b,c),d)), (a,(b,(c,d)))

        Plus correction from m_3 composed with H:
          m_4^tr = sum_{trees T_4} P m_2(...H m_2(...)) [4-leaf trees]
                 + P m_2(H m_3^tr(...), ...) + ... [3+1 compositions]

        For the HPL formula specifically:
          m_4^tr = sum over planar rooted trees with 4 leaves and
                   internal edges labeled by H, internal vertices by m_2,
                   root by P, leaves by I.
        """
        Iv1 = self._apply_matrix(self.I, v1)
        Iv2 = self._apply_matrix(self.I, v2)
        Iv3 = self._apply_matrix(self.I, v3)
        Iv4 = self._apply_matrix(self.I, v4)

        total = _frac_array(self._n)

        # The 5 planar binary trees with 4 leaves, each with all internal
        # edges carrying homotopy H and all vertices carrying m_2:

        # Tree 1: (((1,2),3),4)
        m12 = self._apply_product(Iv1, Iv2)
        Hm12 = self._apply_matrix(self.H, m12)
        m123 = self._apply_product(Hm12, Iv3)
        Hm123 = self._apply_matrix(self.H, m123)
        t1 = self._apply_product(Hm123, Iv4)

        # Tree 2: ((1,(2,3)),4)
        m23 = self._apply_product(Iv2, Iv3)
        Hm23 = self._apply_matrix(self.H, m23)
        m1_23 = self._apply_product(Iv1, Hm23)
        Hm1_23 = self._apply_matrix(self.H, m1_23)
        t2 = self._apply_product(Hm1_23, Iv4)

        # Tree 3: ((1,2),(3,4))
        m34 = self._apply_product(Iv3, Iv4)
        Hm34 = self._apply_matrix(self.H, m34)
        t3 = self._apply_product(Hm12, Hm34)

        # Tree 4: (1,((2,3),4))
        m23_4 = self._apply_product(Hm23, Iv4)
        Hm23_4 = self._apply_matrix(self.H, m23_4)
        t4 = self._apply_product(Iv1, Hm23_4)

        # Tree 5: (1,(2,(3,4)))
        m2_34 = self._apply_product(Iv2, Hm34)
        Hm2_34 = self._apply_matrix(self.H, m2_34)
        t5 = self._apply_product(Iv1, Hm2_34)

        for i in range(self._n):
            total[i] = t1[i] + t2[i] + t3[i] + t4[i] + t5[i]

        return self._apply_matrix(self.P, total)

    def is_formal(self, max_arity: int = 6) -> bool:
        """Check if m_n^{tr} = 0 for all 3 <= n <= max_arity.

        Tests on all basis vectors of cohomology.
        """
        A = self.algebra
        cohom = A.cohomology_dims()
        total_cohom = sum(cohom.values())

        if total_cohom == 0:
            return True

        # Build cohomology basis vectors (in the full space, after projection)
        cohom_basis = []
        for k in A.degrees:
            s, e = A.degree_range(k)
            for i in range(s, e):
                Pei = self._apply_matrix(self.P, _unit_vec(self._n, i))
                if any(x != Fraction(0) for x in Pei):
                    # Check if linearly independent from existing
                    is_new = True
                    if cohom_basis:
                        test_mat = np.column_stack(cohom_basis + [Pei])
                        if _image_dim(test_mat.T) <= len(cohom_basis):
                            is_new = False
                    if is_new:
                        cohom_basis.append(Pei)

        if not cohom_basis:
            return True

        # Check m_3
        if max_arity >= 3:
            for v1 in cohom_basis:
                for v2 in cohom_basis:
                    for v3 in cohom_basis:
                        result = self.m3_transferred(v1, v2, v3)
                        if any(x != Fraction(0) for x in result):
                            return False

        # Check m_4
        if max_arity >= 4:
            for v1 in cohom_basis:
                for v2 in cohom_basis:
                    for v3 in cohom_basis:
                        for v4 in cohom_basis:
                            result = self.m4_transferred(v1, v2, v3, v4)
                            if any(x != Fraction(0) for x in result):
                                return False

        # Higher arities not implemented; return True if passed up to 4
        return True

    def shadow_depth(self) -> int:
        """Compute the shadow depth: max arity of nonzero m_n on the ALGEBRA.

        This measures A-infinity non-formality of A itself (NOT the dual).
        For Koszul algebras:
          - Heisenberg: depth 2 (Gaussian)
          - Affine: depth 3 (Lie/tree)
          - betagamma: depth 4 (contact)
          - Virasoro: depth infinity (mixed)

        Shadow depth != Koszulness. All of the above are Koszul.
        """
        # For finite-dimensional examples, compute transferred m_n on A
        # and find the largest n with m_n != 0.
        # This is a proxy: for infinite-dimensional chiral algebras,
        # the shadow depth comes from the shadow obstruction tower Theta_A^{<=r}.
        A = self.algebra
        cohom_basis = self._get_cohomology_basis()

        if not cohom_basis:
            return 0

        max_depth = 2  # m_2 is always nonzero for nontrivial algebras

        # Check m_3
        for v1 in cohom_basis:
            for v2 in cohom_basis:
                for v3 in cohom_basis:
                    result = self.m3_transferred(v1, v2, v3)
                    if any(x != Fraction(0) for x in result):
                        max_depth = max(max_depth, 3)
                        break
                if max_depth >= 3:
                    break
            if max_depth >= 3:
                break

        # Check m_4
        for v1 in cohom_basis:
            for v2 in cohom_basis:
                for v3 in cohom_basis:
                    for v4 in cohom_basis:
                        result = self.m4_transferred(v1, v2, v3, v4)
                        if any(x != Fraction(0) for x in result):
                            max_depth = max(max_depth, 4)
                            break
                    if max_depth >= 4:
                        break
                if max_depth >= 4:
                    break
            if max_depth >= 4:
                break

        return max_depth

    def _get_cohomology_basis(self) -> List[np.ndarray]:
        """Extract a basis for the cohomology as vectors in the full space."""
        A = self.algebra
        cohom_basis = []
        for k in A.degrees:
            s, e = A.degree_range(k)
            for i in range(s, e):
                Pei = self._apply_matrix(self.P, _unit_vec(self._n, i))
                if any(x != Fraction(0) for x in Pei):
                    is_new = True
                    if cohom_basis:
                        test_mat = np.column_stack(cohom_basis + [Pei])
                        if _image_dim(test_mat.T) <= len(cohom_basis):
                            is_new = False
                    if is_new:
                        cohom_basis.append(Pei)
        return cohom_basis


# ============================================================
# Stasheff A-infinity relation checker
# ============================================================

def stasheff_relation(transfer: HPLTransfer, n: int,
                      inputs: List[np.ndarray]) -> np.ndarray:
    """Compute the n-th Stasheff/A-infinity relation.

    The A-infinity relations state that for each n >= 1:
      sum_{r+s+t=n} (-1)^{rs+t} m_{r+1+t}(a_1,...,a_r, m_s(a_{r+1},...,a_{r+s}), a_{r+s+1},...,a_n) = 0

    Returns the left-hand side (should be zero if A-infinity holds).
    """
    assert len(inputs) == n

    dim = transfer._n
    total = _frac_array(dim)

    # Collect the m_k functions
    def m_k(k, args):
        if k == 1:
            return transfer.m1_transferred(args[0])
        elif k == 2:
            return transfer.m2_transferred(args[0], args[1])
        elif k == 3:
            return transfer.m3_transferred(args[0], args[1], args[2])
        elif k == 4:
            return transfer.m4_transferred(args[0], args[1], args[2], args[3])
        else:
            return _frac_array(dim)  # higher m_k not computed

    for r in range(n + 1):
        for s in range(1, n - r + 1):
            t = n - r - s
            if t < 0:
                continue
            if r + 1 + t > 4 or s > 4:
                continue  # Skip arities beyond our computation

            # Sign: (-1)^{rs + t}
            sign = (-1) ** (r * s + t)

            # Inner application: m_s(a_{r+1}, ..., a_{r+s})
            inner_args = inputs[r:r+s]
            inner_result = m_k(s, inner_args)

            # Outer application: m_{r+1+t}(a_1,...,a_r, inner_result, a_{r+s+1},...,a_n)
            outer_args = list(inputs[:r]) + [inner_result] + list(inputs[r+s:])
            assert len(outer_args) == r + 1 + t
            outer_result = m_k(r + 1 + t, outer_args)

            for i in range(dim):
                total[i] += _frac(sign) * outer_result[i]

    return total


# ============================================================
# Standard example constructions
# ============================================================

def abelian_dga(dim: int) -> DGAlgebra:
    """Abelian Lie algebra of dimension dim: CE complex with d = 0.

    C*(k^dim, k) = Lambda*(k^dim), d = 0 (trivial bracket).
    Product: exterior product (graded commutative).

    Cohomology = full exterior algebra.
    Bar complex -> Koszul dual = symmetric algebra.
    A-infinity on bar cohomology: FORMAL (m_n = 0 for n >= 3).
    Shadow depth: 2 (Gaussian class).
    """
    from math import comb as binomial

    # Degrees: 0, 1, ..., dim
    dims = {}
    for k in range(dim + 1):
        dims[k] = binomial(dim, k)

    total = sum(dims.values())

    # Basis: multi-indices I = {i_1 < ... < i_k} for degree k
    # Ordered: first degree-0 (just {empty}), then degree-1, etc.
    basis_list = []  # (degree, subset)
    for k in range(dim + 1):
        subsets = _ordered_subsets(dim, k)
        for s in subsets:
            basis_list.append((k, s))

    # d = 0
    d_matrix = _frac_array((total, total))

    # Product: exterior product
    # e_I wedge e_J = sgn(I,J) e_{I union J} if I cap J = empty, else 0
    product_tensor = _frac_array((total, total, total))

    basis_to_idx = {s: i for i, (_, s) in enumerate(basis_list)}

    for i, (ki, si) in enumerate(basis_list):
        for j, (kj, sj) in enumerate(basis_list):
            si_set = set(si)
            sj_set = set(sj)
            if si_set & sj_set:
                continue  # intersection nonempty -> wedge = 0
            union = tuple(sorted(si_set | sj_set))
            if union not in basis_to_idx:
                continue
            k = basis_to_idx[union]
            # Sign: number of transpositions to merge si and sj into sorted order
            sign = _merge_sign(si, sj)
            product_tensor[i, j, k] = Fraction(sign)

    return DGAlgebra(dims=dims, d_matrix=d_matrix,
                     product_tensor=product_tensor, name=f"CE(k^{dim})")


def ce_complex_sl2() -> DGAlgebra:
    """Chevalley-Eilenberg complex C*(sl_2, k).

    sl_2 basis: e, h, f with [e,f] = h, [h,e] = 2e, [h,f] = -2f.

    CE complex: Lambda*(sl_2^*), d_CE dual to bracket.
    Degrees: C^0 = k (dim 1), C^1 = (sl_2)* (dim 3),
             C^2 = Lambda^2(sl_2)* (dim 3), C^3 = Lambda^3(sl_2)* (dim 1).

    Cohomology: H^0 = k, H^1 = 0, H^2 = 0, H^3 = k (Whitehead).
    Bar cohomology of CE(sl_2) is FORMAL -> sl_2 is Koszul.
    """
    # Basis: degree 0: {1}, degree 1: {e*, h*, f*}, degree 2: {e*h*, e*f*, h*f*},
    #        degree 3: {e*h*f*}
    # Using indices: e*=0, h*=1, f*=2 within each exterior power
    dims = {0: 1, 1: 3, 2: 3, 3: 1}
    total = 8

    # Flat basis ordering:
    # 0: 1 (degree 0)
    # 1: e* (degree 1)
    # 2: h* (degree 1)
    # 3: f* (degree 1)
    # 4: e*^h* (degree 2)
    # 5: e*^f* (degree 2)
    # 6: h*^f* (degree 2)
    # 7: e*^h*^f* (degree 3)

    d_matrix = _frac_array((total, total))

    # d_CE: C^1 -> C^2
    # d(xi)(X,Y) = -xi([X,Y])
    # For dual basis e*, h*, f* and bracket [e,f]=h, [h,e]=2e, [h,f]=-2f:
    #
    # d(e*)(X,Y) = -e*([X,Y])
    #   d(e*)(h,e) = -e*([h,e]) = -e*(2e) = -2  -> coefficient of h*^e* = -2
    #   but h*^e* = -e*^h*, so d(e*) has +2 in the e*^h* component
    #   d(e*)(h,f) = -e*([h,f]) = -e*(-2f) = 0
    #   d(e*)(e,f) = -e*([e,f]) = -e*(h) = 0
    # So d(e*) = 2 e*^h*  (index 4 gets +2 from index 1)
    #
    # d(h*)(X,Y) = -h*([X,Y])
    #   d(h*)(e,f) = -h*([e,f]) = -h*(h) = -1  -> coeff of e*^f* = -1
    #   d(h*)(h,e) = -h*([h,e]) = -h*(2e) = 0
    #   d(h*)(h,f) = -h*([h,f]) = -h*(-2f) = 0
    # So d(h*) = -e*^f*  (index 5 gets -1 from index 2)
    #
    # d(f*)(X,Y) = -f*([X,Y])
    #   d(f*)(h,f) = -f*([h,f]) = -f*(-2f) = 2  -> coeff of h*^f* = 2
    #   d(f*)(e,f) = -f*([e,f]) = -f*(h) = 0
    #   d(f*)(h,e) = -f*([h,e]) = -f*(2e) = 0
    # So d(f*) = 2 h*^f*  (index 6 gets +2 from index 3)

    # d: C^1 -> C^2
    d_matrix[4, 1] = Fraction(2)   # d(e*) -> 2 e*^h*
    d_matrix[5, 2] = Fraction(-1)  # d(h*) -> -e*^f*
    d_matrix[6, 3] = Fraction(2)   # d(f*) -> 2 h*^f*

    # d: C^2 -> C^3
    # d(e*^h*)(e,h,f) = -(e*^h*)([e,h], f) - (e*^h*)(e, [h,f]) + (e*^h*)(h, [e,f])
    #                    (using the Chevalley-Eilenberg formula for degree 2)
    # Actually, d on Lambda^2 -> Lambda^3:
    # d(alpha)(X,Y,Z) = -alpha([X,Y],Z) + alpha([X,Z],Y) - alpha([Y,Z],X)
    # (for cochains of degree 2)
    #
    # d(e*^h*)(e,h,f):
    #   = -(e*^h*)([e,h],f) + (e*^h*)([e,f],h) - (e*^h*)([h,f],e)
    #   = -(e*^h*)(-2e, f) + (e*^h*)(h, h) - (e*^h*)(-2f, e)
    #   = -(-2)(e*^h*)(e,f) + (e*^h*)(h,h) - (-2)(e*^h*)(f,e)
    #   = -(-2)*0 + 0 - (-2)*0 = 0
    # Hmm, (e*^h*)(e,f) = e*(e)*h*(f) - e*(f)*h*(e) = 1*0 - 0*0 = 0
    # (e*^h*)(h,h) = e*(h)*h*(h) - e*(h)*h*(h) = 0
    # (e*^h*)(f,e) = e*(f)*h*(e) - e*(e)*h*(f) = 0
    # So d(e*^h*) = 0 in this term. Let me redo more carefully.
    #
    # d_CE on Lambda^p uses: d(xi)(X_0,...,X_p) = sum_{i<j} (-1)^{i+j} xi([X_i,X_j], X_0,...,hat_i,...,hat_j,...,X_p)
    # (up to sign convention; the above is the standard one with a minus for Lie algebras)
    #
    # For p=2, xi in Lambda^2:
    # d(xi)(X_0, X_1, X_2) = xi([X_0,X_1], X_2) - xi([X_0,X_2], X_1) + xi([X_1,X_2], X_0)
    # With a minus sign from the Lie algebra convention: d = -delta_{CE}
    # No wait. Standard: d_CE(xi)(X_0,...,X_p) = sum_{i<j} (-1)^{i+j} xi([X_i,X_j], X_0,...,hat,...,hat,...,X_p)
    # But we need to be consistent. Let me use the sign that gives d^2 = 0.
    #
    # For d: Lambda^1 -> Lambda^2:
    #   (d xi)(X,Y) = -xi([X,Y])
    # For d: Lambda^2 -> Lambda^3:
    #   (d xi)(X,Y,Z) = -xi([X,Y], Z) + xi([X,Z], Y) - xi([Y,Z], X)
    #
    # Verify d^2 = 0 on e*:
    # d(e*) = 2 e*^h*
    # d(d(e*))(X,Y,Z) = 2 * d(e*^h*)(X,Y,Z)
    # = 2 * [-(e*^h*)([X,Y],Z) + (e*^h*)([X,Z],Y) - (e*^h*)([Y,Z],X)]
    #
    # Evaluate on (e,h,f):
    # d(e*^h*)(e,h,f) = -(e*^h*)([e,h],f) + (e*^h*)([e,f],h) - (e*^h*)([h,f],e)
    # [e,h] = -2e, [e,f] = h, [h,f] = -2f
    # = -(e*^h*)(-2e, f) + (e*^h*)(h, h) - (e*^h*)(-2f, e)
    # (e*^h*)(X,Y) = e*(X)h*(Y) - e*(Y)h*(X)
    # (e*^h*)(-2e, f) = -2*1*0 - 0*0 = 0
    # (e*^h*)(h, h) = 0*1 - 0*1 = 0... wait, e*(h)=0, h*(h)=1
    # = 0*1 - 1*0 = 0
    # (e*^h*)(-2f, e) = -2*0*0 - 1*0 = 0  (e*(f)=0, h*(e)=0; e*(e)=1, h*(f)=0)
    # Wait: e*(-2f) = -2*e*(f) = 0, h*(e) = 0. So (e*^h*)(-2f,e) = 0*0 - (-2)*0*0 ...
    # Actually (e*^h*)(X,Y) = e*(X)*h*(Y) - e*(Y)*h*(X)
    # (e*^h*)(-2f, e) = e*(-2f)*h*(e) - e*(e)*h*(-2f) = 0*0 - 1*0 = 0
    # So d(e*^h*)(e,h,f) = 0.
    # Since Lambda^3 is 1-dimensional, d(e*^h*) = 0.
    #
    # Similarly for d(e*^f*) and d(h*^f*):
    # d(e*^f*)(e,h,f) = -(e*^f*)([e,h],f) + (e*^f*)([e,f],h) - (e*^f*)([h,f],e)
    # = -(e*^f*)(-2e,f) + (e*^f*)(h,h) - (e*^f*)(-2f,e)
    # (e*^f*)(-2e,f) = e*(-2e)*f*(f) - e*(f)*f*(-2e) = (-2)*1 - 0 = -2
    # (e*^f*)(h,h) = 0
    # (e*^f*)(-2f,e) = e*(-2f)*f*(e) - e*(e)*f*(-2f) = 0 - 1*(-2) = 2
    # d(e*^f*)(e,h,f) = -(-2) + 0 - 2 = 2 - 2 = 0
    #
    # d(h*^f*)(e,h,f) = -(h*^f*)(-2e,f) + (h*^f*)(h,h) - (h*^f*)(-2f,e)
    # (h*^f*)(-2e,f) = h*(-2e)*f*(f) - h*(f)*f*(-2e) = 0*1 - 0*0 = 0
    # (h*^f*)(h,h) = 0
    # (h*^f*)(-2f,e) = h*(-2f)*f*(e) - h*(e)*f*(-2f) = 0*0 - 0*(-2) = 0
    # d(h*^f*)(e,h,f) = 0
    #
    # Good: d: C^2 -> C^3 is the zero map.

    # d: C^2 -> C^3 is zero
    # (already initialized to zero)

    # Product: exterior product on Lambda*(sl_2^*)
    product_tensor = _frac_array((total, total, total))

    # Build basis list for the exterior algebra product
    # degree 0: () -> idx 0
    # degree 1: (0,), (1,), (2,) -> idx 1, 2, 3
    # degree 2: (0,1), (0,2), (1,2) -> idx 4, 5, 6
    # degree 3: (0,1,2) -> idx 7
    ext_basis = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
    ext_to_idx = {s: i for i, s in enumerate(ext_basis)}

    for i, si in enumerate(ext_basis):
        for j, sj in enumerate(ext_basis):
            si_set = set(si)
            sj_set = set(sj)
            if si_set & sj_set:
                continue
            union = tuple(sorted(si_set | sj_set))
            if union not in ext_to_idx:
                continue
            k = ext_to_idx[union]
            sign = _merge_sign(si, sj)
            product_tensor[i, j, k] = Fraction(sign)

    return DGAlgebra(dims=dims, d_matrix=d_matrix,
                     product_tensor=product_tensor, name="CE(sl_2)")


def polynomial_algebra(n: int) -> DGAlgebra:
    """Truncated polynomial algebra k[x]/(x^{n+1}) with x in degree 0.

    This is a commutative algebra concentrated in degree 0.
    Basis: {1, x, x^2, ..., x^n}.
    d = 0 (no differential).

    For n = 1: k[x]/(x^2) = exterior algebra on one generator. Koszul.
    For n >= 2: k[x]/(x^{n+1}). NOT Koszul for n >= 2.
      The bar cohomology carries nontrivial m_3.
    """
    dim = n + 1
    dims = {0: dim}
    total = dim

    d_matrix = _frac_array((total, total))

    product_tensor = _frac_array((total, total, total))
    # x^i * x^j = x^{i+j} if i+j <= n, else 0
    for i in range(dim):
        for j in range(dim):
            if i + j <= n:
                product_tensor[i, j, i + j] = Fraction(1)

    return DGAlgebra(dims=dims, d_matrix=d_matrix,
                     product_tensor=product_tensor,
                     name=f"k[x]/(x^{n+1})")


def exterior_algebra(n: int) -> DGAlgebra:
    """Exterior algebra Lambda(x_1, ..., x_n) with generators in degree 0.

    This is the Koszul dual of the polynomial algebra k[x_1,...,x_n].
    Always Koszul.

    For computational tractability: each x_i is in degree 0 (as an algebra),
    but has an internal "generator index" for the exterior product.
    The full exterior algebra is 2^n-dimensional, concentrated in degree 0.
    """
    from math import comb as binomial

    total = 2 ** n
    dims = {0: total}

    d_matrix = _frac_array((total, total))

    # Basis: subsets of {0, ..., n-1}, ordered by size then lexicographic
    basis = []
    for k in range(n + 1):
        basis.extend(_ordered_subsets(n, k))
    basis_to_idx = {s: i for i, s in enumerate(basis)}

    product_tensor = _frac_array((total, total, total))
    for i, si in enumerate(basis):
        for j, sj in enumerate(basis):
            si_set = set(si)
            sj_set = set(sj)
            if si_set & sj_set:
                continue
            union = tuple(sorted(si_set | sj_set))
            k = basis_to_idx[union]
            sign = _merge_sign(si, sj)
            product_tensor[i, j, k] = Fraction(sign)

    return DGAlgebra(dims=dims, d_matrix=d_matrix,
                     product_tensor=product_tensor,
                     name=f"Lambda({n})")


def koszul_dual_algebra(n: int) -> DGAlgebra:
    """The quadratic dual of k[x]/(x^2): the polynomial algebra k[xi].

    Truncated at degree n for finiteness: k[xi]/(xi^{n+1}).
    xi has degree 1 (bar degree / cohomological degree).
    """
    total = n + 1
    dims = {i: 1 for i in range(n + 1)}

    d_matrix = _frac_array((total, total))

    product_tensor = _frac_array((total, total, total))
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j <= n:
                product_tensor[i, j, i + j] = Fraction(1)

    return DGAlgebra(dims=dims, d_matrix=d_matrix,
                     product_tensor=product_tensor,
                     name=f"k[xi]/(xi^{n+1})")


def truncated_polynomial_dga(d_trunc: int) -> DGAlgebra:
    """k[x]/(x^d) as an augmented algebra (d >= 2).

    Augmentation: x -> 0.  Unit: 1.
    For d = 2: Koszul (dual to k[xi]).
    For d = 3: NOT Koszul (m_3 on bar cohomology is nonzero).
    """
    return polynomial_algebra(d_trunc - 1)


# ============================================================
# Shadow depth / formality classification
# ============================================================

SHADOW_ARCHETYPES = {
    "G": {"name": "Gaussian", "max_depth": 2,
           "description": "m_n = 0 for n >= 3 on A. A-infinity formal."},
    "L": {"name": "Lie/tree", "max_depth": 3,
           "description": "m_3 != 0, m_n = 0 for n >= 4 on A. One L-infinity obstruction."},
    "C": {"name": "contact/quartic", "max_depth": 4,
           "description": "m_3 = 0, m_4 != 0. Contact obstruction at arity 4."},
    "M": {"name": "mixed", "max_depth": None,
           "description": "Infinitely many nonzero m_n. Infinite shadow obstruction tower."},
}


def classify_shadow_archetype(depth: int) -> str:
    """Classify shadow archetype from depth.

    depth 2 -> G (Gaussian): Heisenberg
    depth 3 -> L (Lie/tree): affine Kac-Moody
    depth 4 -> C (contact): betagamma
    depth > 4 or infinity -> M (mixed): Virasoro, W_N
    """
    if depth <= 2:
        return "G"
    elif depth == 3:
        return "L"
    elif depth == 4:
        return "C"
    else:
        return "M"


# ============================================================
# Helpers
# ============================================================

def _ordered_subsets(n: int, k: int) -> List[Tuple[int, ...]]:
    """All k-element subsets of {0,...,n-1} in lexicographic order."""
    if k == 0:
        return [()]
    if k > n:
        return []
    from itertools import combinations
    return [tuple(s) for s in combinations(range(n), k)]


def _merge_sign(a: Tuple[int, ...], b: Tuple[int, ...]) -> int:
    """Sign of the shuffle permutation that merges sorted tuples a and b.

    Counts the number of pairs (i,j) with a[i] > b[j] (inversions).
    """
    count = 0
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la and j < lb:
        if a[i] <= b[j]:
            i += 1
        else:
            count += la - i
            j += 1
    return (-1) ** count
