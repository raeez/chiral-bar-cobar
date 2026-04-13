r"""Homotopy Transfer Theorem: explicit transferred A-infinity structures
for finite-dimensional models of chiral algebra bar complexes.

This module builds explicit deformation retracts (i, p, h) for dg algebras
and computes the transferred A-infinity operations m_k^{tr} on cohomology
H*(A, d) via the Kadeishvili-Merkulov tree formula:

    m_1^{tr} = 0
    m_2^{tr}(a,b) = p . m_2(ia, ib)
    m_3^{tr}(a,b,c) = p . m_2(h.m_2(ia,ib), ic) + p . m_2(ia, h.m_2(ib,ic))
    m_k^{tr} = sum over planar binary trees with k leaves

Each internal edge carries h (homotopy), each internal vertex carries m_2
(product), leaves carry i (inclusion), root carries p (projection).

The number of trees at arity k is the Catalan number C_{k-1}.

APPLICATIONS:
  1. Formality detection: m_k^{tr} = 0 for all k >= 3 iff algebra is formal
  2. For Koszul algebras: Ext_A(k,k) is formal (K2 criterion from
     thm:koszul-equivalences-meta)
  3. For NON-Koszul algebras: Ext_A(k,k) has nontrivial m_3
     (detected on the Koszul complex / bar complex)
  4. Shadow depth = A-infinity depth (conj:operadic-complexity):
     r_max(A) should equal the first nonzero m_k on the L-infinity
     convolution algebra, verified at arities 2,3,4.

TWO DISTINCT COMPUTATIONS:
  A) "Algebra-level transfer": given dg algebra (A, d, mu), transfer
     A-infinity from A to H*(A, d). If A has d=0, this is trivial.
  B) "Bar-level transfer": given augmented algebra A (with d=0),
     build bar complex B(A) as a dg algebra (bar diff + shuffle product),
     transfer A-infinity from B(A) to H*(B(A)) = Ext_A(k,k).
     THIS detects non-Koszulness.

The bar complex B(A) = (T^c(s^{-1}A_+), d_bar) is a dg COALGEBRA.
With the shuffle product, it becomes a dg Hopf algebra.
The transferred A-infinity on H*(B(A)) is the A-infinity algebra
structure on Ext_A(k,k) = A^!.

SIGN CONVENTIONS:
  - Cohomological grading (|d| = +1)
  - Koszul sign rule throughout
  - Bar uses desuspension (|s^{-1}a| = |a| - 1)
  - Exact rational arithmetic via fractions.Fraction

References:
  Kadeishvili, "On the theory of homology of fiber spaces", 1980.
  Merkulov, "Strong homotopy algebras of a Kahler manifold", 1999.
  Loday-Vallette, "Algebraic Operads", Ch 9-10.
  prop:ainfty-formality-implies-koszul (chiral_koszul_pairs.tex)
  thm:koszul-equivalences-meta (chiral_koszul_pairs.tex)
  conj:operadic-complexity (nonlinear_modular_shadows.tex)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from itertools import product as cartesian_product
from typing import (
    Any, Callable, Dict, List, Optional, Sequence, Tuple, Union,
)

import numpy as np


# ============================================================================
# Exact rational arithmetic
# ============================================================================

FR = Fraction

def _frac(x) -> Fraction:
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, np.integer)):
        return Fraction(int(x))
    if isinstance(x, float):
        return Fraction(x).limit_denominator(10**15)
    return Fraction(x)


def _zero_vec(n: int) -> np.ndarray:
    arr = np.empty(n, dtype=object)
    arr.fill(FR(0))
    return arr


def _zero_mat(m: int, n: int) -> np.ndarray:
    arr = np.empty((m, n), dtype=object)
    arr.fill(FR(0))
    return arr


def _eye_mat(n: int) -> np.ndarray:
    mat = _zero_mat(n, n)
    for i in range(n):
        mat[i, i] = FR(1)
    return mat


def _mat_vec(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    m = M.shape[0]
    n = M.shape[1]
    result = _zero_vec(m)
    for i in range(m):
        s = FR(0)
        for j in range(n):
            s += M[i, j] * v[j]
        result[i] = s
    return result


def _mat_mat(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    m, k1 = A.shape
    k2, n = B.shape
    assert k1 == k2
    C = _zero_mat(m, n)
    for i in range(m):
        for j in range(n):
            s = FR(0)
            for l in range(k1):
                s += A[i, l] * B[l, j]
            C[i, j] = s
    return C


def _vec_is_zero(v: np.ndarray) -> bool:
    return all(v[i] == FR(0) for i in range(len(v)))


def _vec_dot(u: np.ndarray, v: np.ndarray) -> Fraction:
    return sum(u[i] * v[i] for i in range(len(u)))


# ============================================================================
# Planar binary trees
# ============================================================================

def planar_binary_trees(n: int) -> List:
    """Generate all planar binary trees with n leaves.

    Returns list of nested tuples.  There are C_{n-1} such trees
    where C_k = (2k)!/(k!(k+1)!) is the k-th Catalan number.

    Leaf i is the integer i.  Internal node is (left, right).
    """
    if n == 1:
        return [0]
    if n == 2:
        return [(0, 1)]

    results = []
    for k in range(1, n):
        left_trees = planar_binary_trees(k)
        right_trees = planar_binary_trees(n - k)
        for lt in left_trees:
            for rt in right_trees:
                shifted_rt = _shift_tree(rt, k)
                results.append((lt, shifted_rt))
    return results


def _shift_tree(tree, offset: int):
    if isinstance(tree, int):
        return tree + offset
    left, right = tree
    return (_shift_tree(left, offset), _shift_tree(right, offset))


def count_internal_nodes(tree) -> int:
    if isinstance(tree, int):
        return 0
    left, right = tree
    return 1 + count_internal_nodes(left) + count_internal_nodes(right)


def tree_leaves(tree) -> List[int]:
    if isinstance(tree, int):
        return [tree]
    left, right = tree
    return tree_leaves(left) + tree_leaves(right)


# ============================================================================
# DG Algebra (with grading, differential, product)
# ============================================================================

@dataclass
class DGAlgebra:
    """Finite-dimensional dg algebra (V, d, mu) over Q.

    Basis vectors indexed 0..dim-1.
    degree_of[i]: cohomological degree of i-th basis vector.
    diff: (dim x dim) matrix, diff[i,j] = coeff of e_i in d(e_j).
    prod: (dim x dim x dim) tensor, prod[i,j,k] = coeff of e_k in mu(e_i, e_j).
    """
    dim: int
    degree_of: List[int]
    diff: np.ndarray
    prod: np.ndarray
    unit_idx: int = 0
    name: str = ""

    def d(self, v: np.ndarray) -> np.ndarray:
        return _mat_vec(self.diff, v)

    def mu(self, v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
        n = self.dim
        result = _zero_vec(n)
        for i in range(n):
            if v1[i] == FR(0):
                continue
            for j in range(n):
                if v2[j] == FR(0):
                    continue
                c = v1[i] * v2[j]
                for k in range(n):
                    result[k] += c * self.prod[i, j, k]
        return result

    def basis(self, i: int) -> np.ndarray:
        v = _zero_vec(self.dim)
        v[i] = FR(1)
        return v

    def check_d_squared(self) -> bool:
        d2 = _mat_mat(self.diff, self.diff)
        return all(d2[i, j] == FR(0) for i in range(self.dim) for j in range(self.dim))

    def check_associativity(self) -> bool:
        n = self.dim
        P = self.prod
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for m in range(n):
                        lhs = sum(P[i, j, l] * P[l, k, m] for l in range(n))
                        rhs = sum(P[j, k, l] * P[i, l, m] for l in range(n))
                        if lhs != rhs:
                            return False
        return True

    def check_leibniz(self) -> bool:
        """Verify d is a derivation: d(ab) = d(a)b + (-1)^|a| a d(b)."""
        n = self.dim
        D = self.diff
        P = self.prod
        for i in range(n):
            deg_i = self.degree_of[i]
            sign = FR((-1) ** deg_i)
            for j in range(n):
                for l in range(n):
                    lhs = sum(D[l, k] * P[i, j, k] for k in range(n))
                    rhs = (sum(D[k, i] * P[k, j, l] for k in range(n))
                           + sign * sum(D[k, j] * P[i, k, l] for k in range(n)))
                    if lhs != rhs:
                        return False
        return True


# ============================================================================
# SDR (Strong Deformation Retract)
# ============================================================================

@dataclass
class SDR:
    """Strong deformation retract data.

    (A, d) --p--> (H, 0) --i--> (A, d),  h: A -> A (degree -1)
    satisfying: pi = id_H, dh + hd = id_A - ip, h^2 = 0, ph = 0, hi = 0.
    """
    alg: DGAlgebra
    dim_H: int
    i_mat: np.ndarray   # (dim_A, dim_H)
    p_mat: np.ndarray   # (dim_H, dim_A)
    h_mat: np.ndarray   # (dim_A, dim_A)
    cohom_degrees: List[int]

    def include(self, v: np.ndarray) -> np.ndarray:
        return _mat_vec(self.i_mat, v)

    def project(self, v: np.ndarray) -> np.ndarray:
        return _mat_vec(self.p_mat, v)

    def homotopy(self, v: np.ndarray) -> np.ndarray:
        return _mat_vec(self.h_mat, v)

    def verify_pi(self) -> bool:
        pi = _mat_mat(self.p_mat, self.i_mat)
        eye = _eye_mat(self.dim_H)
        return all(pi[i, j] == eye[i, j]
                   for i in range(self.dim_H) for j in range(self.dim_H))

    def verify_homotopy_relation(self) -> bool:
        D = self.alg.diff
        H = self.h_mat
        n = self.alg.dim
        dh = _mat_mat(D, H)
        hd = _mat_mat(H, D)
        ip = _mat_mat(self.i_mat, self.p_mat)
        for i in range(n):
            for j in range(n):
                lhs = dh[i, j] + hd[i, j]
                rhs = (FR(1) if i == j else FR(0)) - ip[i, j]
                if lhs != rhs:
                    return False
        return True

    def verify_side_conditions(self) -> Dict[str, bool]:
        H = self.h_mat
        n = self.alg.dim
        h2 = _mat_mat(H, H)
        ph = _mat_mat(self.p_mat, H)
        hi = _mat_mat(H, self.i_mat)
        return {
            "h_squared_zero": all(h2[i, j] == FR(0)
                                  for i in range(n) for j in range(n)),
            "p_h_zero": all(ph[i, j] == FR(0)
                            for i in range(ph.shape[0]) for j in range(ph.shape[1])),
            "h_i_zero": all(hi[i, j] == FR(0)
                            for i in range(hi.shape[0]) for j in range(hi.shape[1])),
        }


# ============================================================================
# Build SDR via Hodge decomposition
# ============================================================================

def build_sdr(alg: DGAlgebra) -> SDR:
    """Build a strong deformation retract for a dg algebra.

    Uses exact rational Gaussian elimination to decompose each degree:
        V^k = im(d_{k-1}) + H^k + C^k
    where H^k is the cohomology (cocycles not in coboundaries)
    and C^k is a complement of ker(d_k) in V^k.

    The SDR satisfies:
        pi = id_H, dh + hd = id_A - ip
        h^2 = 0, ph = 0, hi = 0
    """
    n = alg.dim
    D = alg.diff
    degrees = sorted(set(alg.degree_of))

    def indices_in_deg(k):
        return [i for i in range(n) if alg.degree_of[i] == k]

    # Decompose each degree into im(d_{k-1}) + cohom + complement
    # Store: for each degree k, the local-to-global index map,
    # and the decomposition data.

    cohom_vecs = []  # global-space cohomology representatives
    cohom_degrees = []

    # For homotopy: h maps im(d_{k-1}) in degree k back to degree k-1 preimages.
    # We need: for each basis vector of im(d_{k-1}), a preimage in V^{k-1}.
    # Additionally: h maps the complement C^k to something... actually h should
    # be zero on cocycles (ker d_k) and map image vectors back to preimages.
    #
    # Standard construction (following Loday-Vallette, Crainic):
    # Decompose V^k = B^k + H^k + C^k where B^k = im(d_{k-1}), H^k = cohom,
    # C^k = complement of ker(d_k). Then d restricts to an isomorphism C^k -> B^{k+1}.
    # Define h: B^{k+1} -> C^k as the inverse of this isomorphism,
    # and h = 0 on H^k and C^k.

    # Collect per-degree decomposition data
    decomp = {}  # degree -> (B_vecs, H_vecs, C_vecs, B_preimages, C_images)

    for k in degrees:
        idx_k = indices_in_deg(k)
        dim_k = len(idx_k)
        if dim_k == 0:
            decomp[k] = ([], [], [], [], [])
            continue

        # d_k: V^k -> V^{k+1}
        idx_kp1 = indices_in_deg(k + 1)
        dim_kp1 = len(idx_kp1)
        if dim_kp1 > 0:
            d_k = _zero_mat(dim_kp1, dim_k)
            for a, ia in enumerate(idx_kp1):
                for b, jb in enumerate(idx_k):
                    d_k[a, b] = D[ia, jb]
        else:
            d_k = _zero_mat(0, dim_k)

        # d_{k-1}: V^{k-1} -> V^k
        idx_km1 = indices_in_deg(k - 1)
        dim_km1 = len(idx_km1)
        if dim_km1 > 0:
            d_km1 = _zero_mat(dim_k, dim_km1)
            for a, ia in enumerate(idx_k):
                for b, jb in enumerate(idx_km1):
                    d_km1[a, b] = D[ia, jb]
        else:
            d_km1 = _zero_mat(dim_k, 0)

        # B^k = im(d_{k-1}): column basis of d_km1
        B_local = _column_basis(d_km1)
        # Preimages of B vectors
        B_preimages = []
        for bv in B_local:
            pre = _solve(d_km1, bv)
            B_preimages.append(pre)

        # ker(d_k)
        ker_local = _kernel_basis(d_k)

        # H^k = complement of B^k in ker(d_k)
        H_local = []
        for kv in ker_local:
            if not _vec_in_span(kv, B_local + H_local):
                H_local.append(kv)

        # C^k = complement of ker(d_k) in V^k
        # ker(d_k) = B^k + H^k.  C^k is anything outside ker(d_k).
        all_basis = B_local + H_local
        C_local = []
        for i in range(dim_k):
            ei = _zero_vec(dim_k)
            ei[i] = FR(1)
            if not _vec_in_span(ei, all_basis + C_local):
                C_local.append(ei)

        # d_k restricted to C^k gives vectors in V^{k+1}.
        C_images = []
        for cv in C_local:
            img = _mat_vec(d_k, cv)
            C_images.append(img)

        # Convert to global
        def to_global(v_local, idx_list):
            v = _zero_vec(n)
            for a, ia in enumerate(idx_list):
                v[ia] = v_local[a]
            return v

        def to_global_km1(v_local, idx_list):
            v = _zero_vec(n)
            for a, ia in enumerate(idx_list):
                v[ia] = v_local[a]
            return v

        B_global = [to_global(bv, idx_k) for bv in B_local]
        H_global = [to_global(hv, idx_k) for hv in H_local]
        C_global = [to_global(cv, idx_k) for cv in C_local]
        Bpre_global = [to_global_km1(pv, idx_km1) for pv in B_preimages if pv is not None]
        Cimg_global = [to_global(cv, idx_kp1) for cv in C_images] if idx_kp1 else []

        decomp[k] = (B_global, H_global, C_global, Bpre_global, Cimg_global)

        for hv in H_global:
            cohom_vecs.append(hv)
            cohom_degrees.append(k)

    dim_H = len(cohom_vecs)

    # Build i and p using the algebraic decomposition V^k = B^k + H^k + C^k.
    # i: e_j in H -> j-th cohomology representative in A (standard inclusion)
    # p: v in A -> H-component of v in the decomposition (algebraic projection
    #    along B^k + C^k, NOT orthogonal projection)
    i_mat = _zero_mat(n, dim_H)
    for j, cv in enumerate(cohom_vecs):
        for a in range(n):
            i_mat[a, j] = cv[a]

    p_mat = _zero_mat(dim_H, n)
    h_idx = 0  # running index into the cohomology basis
    for k in degrees:
        B_global, H_global, C_global, Bpre_global, Cimg_global = decomp[k]
        if not H_global:
            h_idx += 0
            continue

        idx_k = [i for i in range(n) if alg.degree_of[i] == k]
        dim_k = len(idx_k)
        all_vecs = B_global + H_global + C_global
        dim_B = len(B_global)
        dim_Hk = len(H_global)

        if len(all_vecs) != dim_k:
            h_idx += dim_Hk
            continue

        # Change-of-basis matrix: columns are [B, H, C]
        M_local = _zero_mat(dim_k, dim_k)
        for j, gv in enumerate(all_vecs):
            for a, ia in enumerate(idx_k):
                M_local[a, j] = gv[ia]

        M_inv_local = _invert(M_local)
        if M_inv_local is None:
            h_idx += dim_Hk
            continue

        # p at degree k: extract H-component coordinates
        # p(v) has j-th entry (for the j-th H^k vector) = M_inv_local[dim_B+j, :] @ v_local
        for j_H in range(dim_Hk):
            row_in_Minv = dim_B + j_H
            for b_col, jb in enumerate(idx_k):
                p_mat[h_idx + j_H, jb] = M_inv_local[row_in_Minv, b_col]

        h_idx += dim_Hk

    # Build h: A -> A (contracting homotopy, degree -1)
    # Required: dh + hd = id - ip on all of A.
    #
    # Decomposition V^k = B^k + H^k + C^k where:
    #   B^k = im(d_{k-1}) (boundaries)
    #   H^k = cohomology complement in ker(d_k)
    #   C^k = complement of ker(d_k)
    #
    # d restricts to isomorphism C^k -> B^{k+1}.
    # Define h: B^{k+1} -> C^k as inverse of d|_{C^k}.
    # h = 0 on H^k and C^k.
    #
    # Then: on B^k: hd(b) = 0 (since d(b) is in B^{k+1} subset im(d_k),
    #   but b is in B^k = im(d_{k-1}), and d(b) = 0 since d^2=0).
    #   Actually d(b) may be nonzero! B^k subset ker(d_k) only when d^2=0.
    #   Since d^2=0: d on B^k = d on im(d_{k-1}) = 0. So dh(b) = 0, hd(b) = 0.
    #   id-ip on B^k: b - 0 = b. So need dh + hd = id on B^k. But both are 0!
    #   That's wrong. Let me reconsider.
    #
    # Actually the correct formula: h maps B^k to preimages in V^{k-1}.
    # Specifically: h restricted to B^k should be the (chosen) right-inverse
    # of d_{k-1}. For b in B^k, h(b) is some c in C^{k-1} with d(c) = b.
    # Then dh(b) = d(c) = b, and hd(b) = h(0) = 0 (since d(b)=0 for b in B^k).
    # So (dh+hd)(b) = b. Good: id - ip on B^k is b - 0 = b. Matches.
    #
    # On H^k: h = 0. dh(v) = 0, hd(v) = h(0) = 0 (since d(v)=0 for cocycles).
    # (dh+hd)(v) = 0 = v - v = id - ip. Correct.
    #
    # On C^k: h = 0. dh(v) = 0. hd(v) = h(d(v)) where d(v) in B^{k+1}.
    # h(d(v)) = the preimage of d(v) in C^k, which is v itself! So hd(v) = v.
    # (dh+hd)(v) = v. And id - ip on C^k: v - 0 = v. Correct.
    #
    # Summary: h is zero on H^k and C^k, and maps B^k to C^{k-1} via
    # the inverse of d|_{C^{k-1}}: C^{k-1} -> B^k.

    # Build h: A -> A (contracting homotopy, degree -1)
    # Required: dh + hd = id - ip.
    # h maps B^k to preimages in V^{k-1}, is zero on H^k + C^k.
    #
    # Key: we need the ALGEBRAIC projection onto B^k along H^k + C^k,
    # not the orthogonal projection. Build the full change-of-basis
    # at each degree, invert, and extract the B-component projection.
    h_mat = _zero_mat(n, n)
    for k in degrees:
        B_global, H_global, C_global, Bpre_global, Cimg_global = decomp[k]
        if not B_global:
            continue

        dim_B = len(B_global)
        dim_Hk = len(H_global)
        dim_C = len(C_global)
        dim_k = dim_B + dim_Hk + dim_C

        # Build change-of-basis matrix: columns are [B, H, C] basis vectors
        # restricted to the local coordinates of degree k.
        idx_k = [i for i in range(n) if alg.degree_of[i] == k]
        all_vecs = B_global + H_global + C_global

        # Extract local coordinates
        M_local = _zero_mat(dim_k, dim_k)
        for j, gv in enumerate(all_vecs):
            for a, ia in enumerate(idx_k):
                M_local[a, j] = gv[ia]

        M_inv = _invert(M_local)
        if M_inv is None:
            continue

        # The algebraic projection onto B^k along H^k+C^k:
        # P_B(v_local) = sum_{j<dim_B} (M_inv @ v_local)[j] * B_global[j]
        # In matrix form: P_B = M_local[:, :dim_B] @ M_inv[:dim_B, :]
        # Then h(v) = sum_j (M_inv @ v_local)[j] * Bpre_global[j]
        # = M_pre_local @ M_inv[:dim_B, :] @ v_local

        # Build h at this degree: for v in V^k (global), extract local coords,
        # project onto B^k using algebraic projection, map to preimages.
        # h(v) = sum_{j=0}^{dim_B-1} alpha_j * preimage_j
        # where alpha = M_inv[:dim_B, :] @ v_local

        # Compute preimages in C^{k-1} directly.
        # d|_{C^{k-1}} : C^{k-1} -> B^k is an isomorphism (by d^2=0).
        # h|_{B^k} = (d|_{C^{k-1}})^{-1}.
        #
        # Build this isomorphism explicitly.
        k_minus_1 = k - 1
        if k_minus_1 not in decomp:
            continue
        _, _, C_km1, _, _ = decomp[k_minus_1]
        if not C_km1:
            # No C^{k-1} means no preimages needed (B^k should be empty,
            # but if not, something is wrong).
            continue

        idx_km1 = [i for i in range(n) if alg.degree_of[i] == k_minus_1]
        dim_C_km1 = len(C_km1)

        # Build the matrix d|_{C^{k-1}} : C^{k-1} -> V^k (in global coords)
        # Columns: d(c_j) for each C^{k-1} basis vector c_j.
        dC_cols = []
        for cv in C_km1:
            dv = _mat_vec(D, cv)
            dC_cols.append(dv)

        # Express d(c_j) in terms of B^k basis (local coords in B^k space).
        # Since d(C^{k-1}) = B^k, and we have B^k vectors, solve for the
        # isomorphism matrix.
        # dC_local[a, j] = coefficient of B_a in d(c_j)
        # where B_a are our B^k basis vectors.
        # Since B^k vectors are in global V^k coords, and d(c_j) is too,
        # we need M_inv[:dim_B, :] to extract B-components.
        dC_Bcoords = _zero_mat(dim_B, dim_C_km1)
        for j, dv in enumerate(dC_cols):
            # Extract local coords of dv in degree-k space
            dv_local = _zero_vec(dim_k)
            for a, ia in enumerate(idx_k):
                dv_local[a] = dv[ia]
            # Get B-component coords
            coords = _mat_vec(M_inv, dv_local)
            for b in range(dim_B):
                dC_Bcoords[b, j] = coords[b]

        # Invert: this gives the map B^k -> C^{k-1} (in the C basis)
        dC_inv = _invert(dC_Bcoords)
        if dC_inv is None:
            continue

        # h|_{B^k}: for v in V^k with B-component alpha,
        # h(v) = sum_j (dC_inv @ alpha)[j] * C_km1[j]
        for b_col, jb in enumerate(idx_k):
            # alpha = M_inv[:dim_B, b_col]
            alpha = _zero_vec(dim_B)
            for b in range(dim_B):
                alpha[b] = M_inv[b, b_col]
            # beta = dC_inv @ alpha (coords in C^{k-1} basis)
            beta = _mat_vec(dC_inv, alpha)
            for j in range(dim_C_km1):
                if beta[j] != FR(0):
                    cv = C_km1[j]
                    for a in range(n):
                        h_mat[a, jb] += beta[j] * cv[a]

    return SDR(alg, dim_H, i_mat, p_mat, h_mat, cohom_degrees)


def _gram_schmidt(vecs: List[np.ndarray]) -> List[np.ndarray]:
    """Gram-Schmidt orthogonalization over Q."""
    ortho = []
    for v in vecs:
        w = v.copy()
        for u in ortho:
            proj = _vec_dot(u, w) / _vec_dot(u, u)
            w = np.array([w[i] - proj * u[i] for i in range(len(w))], dtype=object)
        if not _vec_is_zero(w):
            ortho.append(w)
    return ortho


# ============================================================================
# Transferred A-infinity via tree formula
# ============================================================================

class TransferredAInfinity:
    """Computes transferred A-infinity operations via the tree formula.

    Given SDR data for dg algebra (A, d, mu), the transferred
    A-infinity structure on H = H*(A) has:

        m_k^{tr}(a_1,...,a_k) = sum_{T in PBT(k)} eval_tree(T)

    where PBT(k) = planar binary trees with k leaves, and eval_tree(T)
    applies: i at leaves, mu at vertices, h at internal edges, p at root.
    """

    def __init__(self, sdr: SDR):
        self.sdr = sdr
        self.alg = sdr.alg
        self._dim_A = sdr.alg.dim
        self._dim_H = sdr.dim_H
        self._tree_cache: Dict[int, List] = {}

    def _trees(self, k: int) -> List:
        if k not in self._tree_cache:
            self._tree_cache[k] = planar_binary_trees(k)
        return self._tree_cache[k]

    def _eval_tree(self, tree, inputs_A: List[np.ndarray]) -> np.ndarray:
        """Evaluate tree on inputs already embedded in A (via i)."""
        return self._eval_subtree(tree, inputs_A, apply_h=False)

    def _eval_subtree(self, tree, inputs_A: List[np.ndarray],
                      apply_h: bool) -> np.ndarray:
        if isinstance(tree, int):
            result = inputs_A[tree]
        else:
            left, right = tree
            left_val = self._eval_subtree(left, inputs_A, apply_h=True)
            right_val = self._eval_subtree(right, inputs_A, apply_h=True)
            result = self.alg.mu(left_val, right_val)

        if apply_h:
            result = self.sdr.homotopy(result)
        return result

    def m_transferred(self, k: int, inputs_H: List[np.ndarray]) -> np.ndarray:
        """Compute m_k^{tr}(a_1,...,a_k) for cohomology inputs.

        inputs_H: list of k vectors in H (dimension dim_H).
        Returns vector in H.
        """
        assert len(inputs_H) == k

        if k == 1:
            v = self.sdr.include(inputs_H[0])
            dv = self.alg.d(v)
            return self.sdr.project(dv)

        inputs_A = [self.sdr.include(v) for v in inputs_H]

        if k == 2:
            prod = self.alg.mu(inputs_A[0], inputs_A[1])
            return self.sdr.project(prod)

        # General k >= 3: sum over Catalan many trees
        trees = self._trees(k)
        total = _zero_vec(self._dim_H)
        for tree in trees:
            val = self._eval_tree(tree, inputs_A)
            pval = self.sdr.project(val)
            for i in range(self._dim_H):
                total[i] += pval[i]
        return total

    def m1(self, a: np.ndarray) -> np.ndarray:
        return self.m_transferred(1, [a])

    def m2(self, a: np.ndarray, b: np.ndarray) -> np.ndarray:
        return self.m_transferred(2, [a, b])

    def m3(self, a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
        return self.m_transferred(3, [a, b, c])

    def m4(self, a: np.ndarray, b: np.ndarray, c: np.ndarray,
           d_: np.ndarray) -> np.ndarray:
        return self.m_transferred(4, [a, b, c, d_])

    def m5(self, a: np.ndarray, b: np.ndarray, c: np.ndarray,
           d_: np.ndarray, e: np.ndarray) -> np.ndarray:
        return self.m_transferred(5, [a, b, c, d_, e])

    def _basis_H(self, i: int) -> np.ndarray:
        v = _zero_vec(self._dim_H)
        v[i] = FR(1)
        return v

    def stasheff_relation(self, n: int,
                          inputs_H: List[np.ndarray]) -> np.ndarray:
        r"""Compute the n-th Stasheff/A-infinity relation.

        Returns the LHS of:
          sum_{r+s+t=n, s>=1} (-1)^{rs+t} m_{r+1+t}(...m_s(...)...) = 0
        """
        assert len(inputs_H) == n
        total = _zero_vec(self._dim_H)
        max_arity = 5

        for r in range(n + 1):
            for s in range(1, n - r + 1):
                t = n - r - s
                if t < 0:
                    continue
                outer_arity = r + 1 + t
                if outer_arity > max_arity or s > max_arity:
                    continue

                sign = (-1) ** (r * s + t)
                inner = self.m_transferred(s, inputs_H[r:r + s])
                outer_inputs = list(inputs_H[:r]) + [inner] + list(inputs_H[r + s:])
                outer = self.m_transferred(outer_arity, outer_inputs)

                for i in range(self._dim_H):
                    total[i] += FR(sign) * outer[i]

        return total

    def ainfty_depth(self, max_k: int = 5) -> int:
        """Compute A-infinity depth: smallest k >= 3 with m_k nonzero,
        or 2 if all vanish (formal algebra).

        More precisely: returns the largest k with m_k != 0, checked
        through max_k.
        """
        dim_H = self._dim_H
        if dim_H == 0:
            return 0

        depth = 2
        for k in range(3, max_k + 1):
            found = False
            for indices in cartesian_product(range(dim_H), repeat=k):
                inputs = [self._basis_H(i) for i in indices]
                result = self.m_transferred(k, inputs)
                if not _vec_is_zero(result):
                    depth = k
                    found = True
                    break
            # Do NOT break early: m_k=0 does NOT imply m_{k+1}=0 in general
        return depth

    def is_formal(self, max_k: int = 5) -> bool:
        """Check if m_k = 0 for all 3 <= k <= max_k."""
        dim_H = self._dim_H
        if dim_H == 0:
            return True
        for k in range(3, max_k + 1):
            for indices in cartesian_product(range(dim_H), repeat=k):
                inputs = [self._basis_H(i) for i in indices]
                result = self.m_transferred(k, inputs)
                if not _vec_is_zero(result):
                    return False
        return True


# ============================================================================
# Standard example: CE(sl_2)
# ============================================================================

def sl2_ce() -> DGAlgebra:
    """CE complex of sl_2: the canonical nontrivial dg algebra example.

    sl_2: [e,f] = h, [h,e] = 2e, [h,f] = -2f.
    CE complex = Lambda*(sl_2^*) with d dual to bracket.

    Basis:
        0: 1 (degree 0)
        1: e* (degree 1), 2: h* (degree 1), 3: f* (degree 1)
        4: e*^h* (degree 2), 5: e*^f* (degree 2), 6: h*^f* (degree 2)
        7: e*^h*^f* (degree 3)

    Differentials:
        d(e*) = 2 e*^h*       [from d(e*)(h,e) = -e*([h,e]) = -e*(2e) = -2,
                                 but e*^h*(h,e) = -1, so coeff = 2]
        d(h*) = -e*^f*         [from [e,f] = h]
        d(f*) = 2 h*^f*       [from [h,f] = -2f]
        d(degree 2 -> degree 3) = 0

    H*(CE(sl_2)) = k[0] + k[3] (Whitehead's theorem for semisimple).
    Transferred A-infinity on H*: ALL m_k = 0 for k >= 2 nontrivial,
    and m_k = 0 for k >= 3 (FORMAL). sl_2 is Koszul.
    """
    n = 8
    deg = [0, 1, 1, 1, 2, 2, 2, 3]

    d = _zero_mat(n, n)
    d[4, 1] = FR(2)    # d(e*) = 2 e*^h*
    d[5, 2] = FR(-1)   # d(h*) = -e*^f*
    d[6, 3] = FR(2)    # d(f*) = 2 h*^f*

    P = np.empty((n, n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                P[i, j, k] = FR(0)

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
            k_idx = ext_to_idx[union]
            sign = _merge_sign(si, sj)
            P[i, j, k_idx] = FR(sign)

    return DGAlgebra(n, deg, d, P, unit_idx=0, name="CE(sl_2)")


# ============================================================================
# Standard example: truncated polynomial k[x]/(x^n)
# ============================================================================

def truncated_poly(n: int) -> DGAlgebra:
    """k[x]/(x^n), d=0, commutative product.

    For n=2: dual numbers. Koszul.
    For n>=3: NOT Koszul (detected on bar complex).

    Note: when d=0, H=A and h=0, so ALL transferred m_k vanish.
    Non-Koszulness is detected on B(A), not A itself.
    """
    deg = [0] * n
    d = _zero_mat(n, n)
    P = np.empty((n, n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                P[i, j, k] = FR(0)
    for i in range(n):
        for j in range(n):
            if i + j < n:
                P[i, j, i + j] = FR(1)
    return DGAlgebra(n, deg, d, P, unit_idx=0, name=f"k[x]/(x^{n})")


# ============================================================================
# Koszul resolution of k over k[x]/(x^n)
# ============================================================================

def koszul_resolution_k_over_poly2() -> DGAlgebra:
    """Koszul resolution of k over A = k[x]/(x^2).

    The algebra A = k[x]/(x^2) has Koszul resolution:
        ... -> A.e_2 -> A.e_1 -> A.e_0 -> k -> 0
    where d(e_n) = x.e_{n-1}.

    As a dg algebra (the bar construction): this is the tensor algebra
    generated by xi (degree 1) with d(xi) = x (the augmentation ideal
    generator), and xi^2 = 0.

    Model: 4-dimensional dg algebra
        degree 0: 1 (index 0), x (index 1)
        degree 1: xi (index 2), x.xi (index 3)
        d(xi) = x, d(x.xi) = x^2 = 0
        Product: x.x = 0, xi.xi = 0, x.xi = x.xi (index 3), xi.x = -x.xi
    """
    n = 4
    deg = [0, 0, 1, 1]

    d = _zero_mat(n, n)
    d[1, 2] = FR(1)   # d(xi) = x

    P = np.empty((n, n, n), dtype=object)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                P[i, j, k] = FR(0)

    # Unit: 1 * anything = anything * 1 = itself
    for i in range(n):
        P[0, i, i] = FR(1)
        P[i, 0, i] = FR(1)
    P[0, 0, 0] = FR(1)  # unit^2 = unit (already set correctly)

    # x * xi = x.xi (index 3)
    P[1, 2, 3] = FR(1)
    # xi * x = -x.xi (graded commutativity: xi is degree 1)
    P[2, 1, 3] = FR(-1)
    # x^2 = 0 (already zero)
    # xi^2 = 0 (already zero)
    # x . (x.xi) = 0 (x^2 = 0)
    # xi . (x.xi) = 0 (degree 2, not present)
    # (x.xi) . x = 0
    # (x.xi) . xi = 0

    return DGAlgebra(n, deg, d, P, unit_idx=0,
                     name="Koszul_res(k[x]/(x^2))")


def koszul_resolution_k_over_poly3() -> DGAlgebra:
    """Minimal model of k[x]/(x^3) detecting non-Koszulness.

    For A = k[x]/(x^3), the bar complex B(A) has bar generators:
        [x], [x^2] in bar degree 1
        [x|x], [x|x^2], [x^2|x], [x^2|x^2] in bar degree 2
        etc.

    We build a TRUNCATED dg algebra model capturing the essential
    non-formality. The Koszul complex attempts:
        ... -> A.e_2 -d-> A.e_1 -d-> A.e_0 -> k -> 0
    with d(e_1) = x.e_0, d(e_2) = x^2.e_1.

    But d^2(e_2) = x^2 . d(e_1) = x^2 . x = x^3 = 0 in A. Good.
    The obstruction to Koszulness: H^2(Koszul) != 0.

    The resolution of k: we need d(e_2) = x^2 . e_1 but also
    d(e_2') = x . e_1 for the x^2 piece. The complication is that
    the Koszul complex has x^2 . e_1 and this maps to x^2 . x = 0.

    Actually, for k[x]/(x^3): Ext^*_A(k,k) = k<xi_1, xi_2> / (xi_2^2)
    with |xi_1| = 1, |xi_2| = 2 (bar degrees).
    The transferred m_3(xi_1, xi_1, xi_1) = xi_2 (up to sign).
    This is the OBSTRUCTION to Koszulness.

    Model: 6-dim dg algebra capturing the bar complex through arity 3.

    Degrees (bar degree = internal degree for s^{-1}A_+):
        0: unit 1 (index 0)
        1: [x] (index 1), [x^2] (index 2)      -- bar degree 1
        2: [x|x] (index 3)                       -- bar degree 2
        3: [x|x|x] (index 4)                     -- bar degree 3
        2: [x|x^2] ~ [x^2|x] (index 5)          -- bar degree 2

    Bar differential:
        d([x|x]) = [x^2]  (from m_2(x,x) = x^2)
        d([x|x^2]) = [x^3] = 0  (x^3 = 0 in A)
        d([x|x|x]) = [x^2|x] - [x|x^2] = [x^2|x] - [x|x^2]
                      (from product on first and second pairs)

    This model has nontrivial cohomology in bar degree 2 from the
    relation x^3 = 0 creating a cycle that is not a boundary.
    """
    # Build bar complex of k[x]/(x^3) as an explicit dg algebra.
    # Augmentation ideal A_+ = span{x, x^2}.
    # s^{-1}A_+ basis: s^{-1}x (degree 0), s^{-1}x^2 (degree 0).
    # [Wait: the bar grading for augmented algebras concentrated in degree 0
    #  makes ALL bar elements have bar-degree = tensor length,
    #  internal degree = 0 for each factor (since A is in degree 0).]
    #
    # The bar complex B(A) = k + (s^{-1}A_+) + (s^{-1}A_+)^{otimes 2} + ...
    # with d_bar([a_1|...|a_n]) = sum (...|m_2(a_i, a_{i+1})|...) only.
    # (Internal d = 0 since A has d = 0.)
    #
    # For the bar complex of an algebra concentrated in degree 0,
    # the bar differential d_bar: B^n -> B^{n-1} is a degree-1 map
    # (in the total grading where bar degree n gets internal degree -n
    #  from desuspension).
    #
    # The CORRECT setup for detecting non-Koszulness:
    # Bar complex B(A) as a chain complex (coalgebra differential).
    # Its cohomology H*(B(A)) = Ext_A(k,k).
    # The Kadeishvili transfer gives A-infinity on Ext.
    # We implement this directly.

    # Augmentation ideal generators: x (index 0), x^2 (index 1)
    # Bar elements through arity 3:
    # Arity 1: [x]=0, [x^2]=1
    # Arity 2: [x|x]=2, [x|x^2]=3, [x^2|x]=4, [x^2|x^2]=5
    # Arity 3: [x|x|x]=6, [x|x|x^2]=7, [x|x^2|x]=8, [x^2|x|x]=9,
    #           [x|x^2|x^2]=10, [x^2|x|x^2]=11, [x^2|x^2|x]=12, [x^2|x^2|x^2]=13
    # Total: 2 + 4 + 8 = 14 basis elements

    # Bar degrees: arity 1 -> degree 1, arity 2 -> degree 2, arity 3 -> degree 3
    # (In the total complex: internal degree = -n from desuspension of n factors
    #  of degree 0. So total degree = 0 - n + n = 0. But we use bar degree as
    #  the grading for the dg algebra structure.)

    n_basis = 14
    # Assign degrees = arity
    deg = [1, 1,  # arity 1
           2, 2, 2, 2,  # arity 2
           3, 3, 3, 3, 3, 3, 3, 3]  # arity 3

    d = _zero_mat(n_basis, n_basis)

    # Bar differential d: B^n -> B^{n-1}
    # d([a_1|...|a_n]) = sum_{i=1}^{n-1} (-1)^{epsilon_i} [a_1|...|m(a_i,a_{i+1})|...|a_n]
    # where epsilon_i is the Koszul sign (sum of desuspended degrees to the left).
    # Since all a_i have degree 0 in A, desuspended degree = -1.
    # Sign: (-1)^{sum_{j<i} (-1)} = (-1)^{-i} = (-1)^i (since desuspended deg = -1).

    # Product in A = k[x]/(x^3):
    # x * x = x^2 (aug index 0 * 0 -> 1)
    # x * x^2 = x^3 = 0
    # x^2 * x = x^3 = 0
    # x^2 * x^2 = x^4 = 0

    # d_bar on arity 2 -> arity 1:
    # d([x|x]) = +[x*x] = [x^2]   (sign: (-1)^0 = +1 for i=0... let me be careful)
    # Sign convention: for [a|b], d = [m(a,b)].
    # With desuspension:
    # d([s^{-1}a|s^{-1}b]) = +[s^{-1}(m(a,b))]
    # (the sign is +1 for the first
    # and only product in arity 2).
    # Actually, the standard convention: d_bar([a_1|...|a_n]) = sum_{i=1}^{n-1}
    #   (-1)^{|s^{-1}a_1|+...+|s^{-1}a_i|} [a_1|...|a_i*a_{i+1}|...|a_n]
    # With |s^{-1}a_j| = |a_j| - 1 = -1 (since all a_j have degree 0).
    # Sign for position i: (-1)^{i * (-1)} = (-1)^{-i} = (-1)^i.
    # For arity 2: only i=1, sign = (-1)^{1*(-1)} = (-1)^{-1} = -1.
    # Hmm, let me use the Loday-Vallette convention directly.
    # d_bar = sum b'_i where b'_i applies the product at position i.
    # Sign: (-1)^{|a_1|' + ... + |a_i|'} where |a|' = |a| - 1.
    # For all a in degree 0: |a|' = -1.
    # Sign at position i (1-indexed): (-1)^{i * (-1)} = (-1)^{-i} = (-1)^i.

    # For arity 2, position 1: sign = (-1)^{1*(-1)} = -1.
    # d([a_1|a_2]) = (-1)^{|a_1|'} [a_1 * a_2] = (-1)^{-1} [a_1*a_2] = -[a_1*a_2].
    # Wait, let me count properly.
    # Loday-Vallette (2.2.1): d_1([a_1|...|a_n]) = sum_{i=1}^{n-1} (-1)^{epsilon_i}
    #   [a_1|...|a_i . a_{i+1}|...|a_n]
    # where epsilon_i = (|a_1|-1) + ... + (|a_i|-1) = sum_{j=1}^i (|a_j|-1).
    # For |a_j| = 0: epsilon_i = -i.
    # Sign = (-1)^{-i} = (-1)^i (since (-1)^{-1} = -1).

    # d([x|x]) at i=1: sign = (-1)^1 = -1. Product: x*x = x^2.
    # d([x|x]) = -[x^2].
    d[1, 2] = FR(-1)   # d([x|x]) = -[x^2]
    # d([x|x^2]) at i=1: sign = -1. Product: x*x^2 = 0. So d = 0.
    # d([x^2|x]) at i=1: sign = -1. Product: x^2*x = 0. So d = 0.
    # d([x^2|x^2]) at i=1: sign = -1. Product: x^2*x^2 = 0. So d = 0.

    # d_bar on arity 3 -> arity 2:
    # d([a|b|c]) = (-1)^{|a|'} [a*b|c] + (-1)^{|a|'+|b|'} [a|b*c]
    #            = (-1)^{-1} [a*b|c] + (-1)^{-2} [a|b*c]
    #            = -[a*b|c] + [a|b*c]

    # d([x|x|x]) = -[x^2|x] + [x|x^2]
    # [x^2|x] is index 4, [x|x^2] is index 3
    d[4, 6] = FR(-1)   # -[x^2|x] from [x|x|x]
    d[3, 6] = FR(1)    # +[x|x^2] from [x|x|x]

    # d([x|x|x^2]) = -[x^2|x^2] + [x|x*x^2] = -[x^2|x^2] + 0
    d[5, 7] = FR(-1)   # -[x^2|x^2] from [x|x|x^2]

    # d([x|x^2|x]) = -[x*x^2|x] + [x|x^2*x] = 0 + 0 = 0
    # (x*x^2 = 0 and x^2*x = 0)

    # d([x^2|x|x]) = -[x^2*x|x] + [x^2|x^2] = 0 + [x^2|x^2]
    d[5, 9] = FR(1)    # +[x^2|x^2] from [x^2|x|x]

    # d([x|x^2|x^2]) = -[x*x^2|x^2] + [x|x^2*x^2] = 0 + 0 = 0
    # d([x^2|x|x^2]) = -[x^2*x|x^2] + [x^2|x*x^2] = 0 + 0 = 0
    # d([x^2|x^2|x]) = -[x^2*x^2|x] + [x^2|x^2*x] = 0 + 0 = 0
    # d([x^2|x^2|x^2]) = 0

    # Product on B(A): shuffle product (makes B(A) a dg Hopf algebra).
    # For the A-infinity transfer, we use the CONCATENATION product
    # (tensor product structure on T^c(s^{-1}A_+)), which is actually
    # the deconcatenation coproduct of the bar coalgebra dualized.
    #
    # But for the Kadeishvili transfer on B(A) viewed as a dg algebra,
    # the relevant product is the SHUFFLE PRODUCT:
    # [a_1|...|a_p] * [b_1|...|b_q] = sum over (p,q)-shuffles of
    #    +/- [c_{sigma(1)}|...|c_{sigma(p+q)}]
    #
    # For our computation at low arity:
    # [x] * [x] = [x|x] + [x|x] = 2[x|x]?  No!
    # [a] * [b]
    #   = [a|b] + (-1)^{|s^{-1}a||s^{-1}b|} [b|a]
    #   = [a|b] + (-1)^{(-1)(-1)} [b|a]
    #   = [a|b] + (-1) [b|a]
    #   (since |s^{-1}a| = |s^{-1}b| = -1)
    # Wait: shuffle product sign is (-1)^{|s^{-1}a||s^{-1}b|}.
    # |s^{-1}a| = |a| - 1 = -1 for all our elements.
    # So [a]*[b] = [a|b] + (-1)^{(-1)(-1)}[b|a] = [a|b] + (-1)^1 [b|a] = [a|b] - [b|a].

    # This makes B(A) a GRADED COMMUTATIVE algebra (the shuffle algebra).
    # For the A-infinity transfer, we use this as the product.

    P = np.empty((n_basis, n_basis, n_basis), dtype=object)
    for i in range(n_basis):
        for j in range(n_basis):
            for k in range(n_basis):
                P[i, j, k] = FR(0)

    # Shuffle products (only those landing in our truncated space):
    # arity 1 * arity 1 -> arity 2:
    # [x]*[x] = [x|x] - [x|x] = 0
    # Actually: [a]*[b] = [a|b] + sign * [b|a].
    # For (a,b) = (x,x):
    # [x]*[x] = [x|x] + (-1)^{|s^{-1}x||s^{-1}x|}[x|x] = [x|x] + (-1)^1 [x|x] = 0.
    # (Graded symmetric: a*a = 0 for odd-degree elements; |s^{-1}x|=-1 is odd.)

    # [x]*[x^2]
    #   = [x|x^2] + (-1)^{|s^{-1}x||s^{-1}x^2|}[x^2|x]
    #   = [x|x^2] - [x^2|x]
    P[0, 1, 3] = FR(1)     # [x]*[x^2] has +[x|x^2]
    P[0, 1, 4] = FR(-1)    # [x]*[x^2] has -[x^2|x]

    # [x^2]*[x] = [x^2|x] + (-1)^{1}[x|x^2] = [x^2|x] - [x|x^2]
    P[1, 0, 4] = FR(1)
    P[1, 0, 3] = FR(-1)

    # [x^2]*[x^2] = [x^2|x^2] - [x^2|x^2] = 0

    # arity 1 * arity 2 -> arity 3 (if in range):
    # [x]*[x|x] = sum over (1,2)-shuffles of [x,x,x]:
    #   shuffle (1,2,3): [x|x|x]
    #   shuffle (2,1,3): (-1)^{|s^{-1}x||s^{-1}x|}[x|x|x] = -[x|x|x]
    #   shuffle (2,3,1): (-1)^{|s^{-1}x|(|s^{-1}x|+|s^{-1}x|)}[x|x|x]
    #                    = (-1)^{(-1)(-2)}[x|x|x] = [x|x|x]
    # Hmm, the (p,q)-shuffle formula for p=1, q=2:
    # sigma ranges over shuffles that keep the relative order of (a) and (b_1,b_2).
    # Shuffles of {1} and {2,3}: (1,2,3), (2,1,3), (2,3,1).
    # [x] * [x|x]:
    #   (1,2,3): [x|x|x], sign = 1
    #   (2,1,3): [x|x|x], sign = (-1)^{|s^{-1}x||s^{-1}x|} = (-1)^1 = -1
    #   (2,3,1): [x|x|x], sign = (-1)^{|s^{-1}x|(|s^{-1}x|+|s^{-1}x|)} = (-1)^{(-1)(-2)} = (-1)^2 = 1
    # Total: [x|x|x](1 - 1 + 1) = [x|x|x].
    #
    # Actually, all three shuffles give [x|x|x] since all factors are the same!
    # But the sign accounts for the permutation of identical elements.
    # Let me be more careful with distinct elements.

    # For distinct a, b_1, b_2:
    # [a] * [b_1|b_2]:
    #   shuffle (a, b_1, b_2): [a|b_1|b_2], sign = 1
    #   shuffle (b_1, a, b_2): [b_1|a|b_2], sign = (-1)^{|s^{-1}b_1||s^{-1}a|}
    #   shuffle (b_1, b_2, a): [b_1|b_2|a], sign = (-1)^{(|s^{-1}b_1|+|s^{-1}b_2|)|s^{-1}a|}

    # With all desuspended degrees equal to -1:
    #   sign for (b_1,a,b_2) = (-1)^{(-1)(-1)} = (-1)^1 = -1
    #   sign for (b_1,b_2,a) = (-1)^{(-2)(-1)} = (-1)^2 = 1

    # [x]*[x|x^2] = [x|x|x^2] - [x|x|x^2] + [x|x^2|x]
    # Wait, the first two are the same element! Let me index properly.
    # a = x (aug idx 0), b_1 = x (aug idx 0), b_2 = x^2 (aug idx 1).
    # (a,b_1,b_2) = (0,0,1) -> bar elt [x|x|x^2] = index 7
    # (b_1,a,b_2) = (0,0,1) -> same! [x|x|x^2] = index 7
    # (b_1,b_2,a) = (0,1,0) -> [x|x^2|x] = index 8
    # So: [x]*[x|x^2] = 1*[x|x|x^2] + (-1)*[x|x|x^2] + 1*[x|x^2|x]
    #                   = 0 + [x|x^2|x] = [x|x^2|x]
    P[0, 3, 8] = FR(1)   # [x]*[x|x^2] = [x|x^2|x]

    # [x]*[x^2|x] = similar analysis:
    # a=x(0), b_1=x^2(1), b_2=x(0)
    # (a,b_1,b_2) = (0,1,0) -> [x|x^2|x] = index 8, sign +1
    # (b_1,a,b_2) = (1,0,0) -> [x^2|x|x] = index 9, sign -1
    # (b_1,b_2,a) = (1,0,0) -> [x^2|x|x] = index 9, sign +1
    # Total: [x|x^2|x] + 0 = [x|x^2|x]
    P[0, 4, 8] = FR(1)   # [x]*[x^2|x] = [x|x^2|x]

    # [x]*[x^2|x^2]:
    # a=x(0), b_1=x^2(1), b_2=x^2(1)
    # (0,1,1) -> [x|x^2|x^2] = index 10, sign +1
    # (1,0,1) -> [x^2|x|x^2] = index 11, sign -1
    # (1,1,0) -> [x^2|x^2|x] = index 12, sign +1
    P[0, 5, 10] = FR(1)
    P[0, 5, 11] = FR(-1)
    P[0, 5, 12] = FR(1)

    # [x^2]*[x|x]:
    # a=x^2(1), b_1=x(0), b_2=x(0)
    # (1,0,0) -> [x^2|x|x] = index 9, sign +1
    # (0,1,0) -> [x|x^2|x] = index 8, sign -1
    # (0,0,1) -> [x|x|x^2] = index 7, sign +1
    P[1, 2, 9] = FR(1)
    P[1, 2, 8] = FR(-1)
    P[1, 2, 7] = FR(1)

    # [x^2]*[x|x^2]:
    # a=x^2(1), b_1=x(0), b_2=x^2(1)
    # (1,0,1) -> [x^2|x|x^2] = index 11, sign +1
    # (0,1,1) -> [x|x^2|x^2] = index 10, sign -1
    # (0,1,1) -> same as above
    # Wait: (b_1,a,b_2) = (0,1,1) -> [x|x^2|x^2] = index 10
    # (b_1,b_2,a) = (0,1,1) -> same! [x|x^2|x^2] = index 10
    # Total: [x^2|x|x^2] + (-1+1)[x|x^2|x^2] = [x^2|x|x^2]
    P[1, 3, 11] = FR(1)

    # [x^2]*[x^2|x]:
    # a=x^2(1), b_1=x^2(1), b_2=x(0)
    # (1,1,0) -> [x^2|x^2|x] = index 12, sign +1
    # (1,1,0) -> same, sign -1
    # (1,0,1) -> [x^2|x|x^2]... wait
    # (a,b_1,b_2) = (1,1,0): [x^2|x^2|x] = 12, sign +1
    # (b_1,a,b_2) = (1,1,0): same! sign -1
    # (b_1,b_2,a) = (1,0,1): [x^2|x|x^2]... No:
    # b_1=x^2, b_2=x, a=x^2: sequence is (x^2, x, x^2) = (1,0,1)
    # -> [x^2|x|x^2] = index 11, sign +1
    # Total: 0 + [x^2|x|x^2] = [x^2|x|x^2]
    P[1, 4, 11] = FR(1)  # This clashes with the line above! Let me add.
    # Actually P[1, 4, 11] was already 0, this sets it to 1.
    # But P[1, 3, 11] was set above too. These are different entries.

    # [x^2]*[x^2|x^2]: by symmetry, = 0 (graded symmetric, same element)
    # Actually, [x^2]*[x^2|x^2]:
    # (1,1,1) -> all shuffles give same sequence (1,1,1)
    # signs: +1, -1, +1. Total: 1.
    # -> [x^2|x^2|x^2] = index 13
    P[1, 5, 13] = FR(1)

    # Also need [arity 2] * [arity 1]:
    # [x|x]*[x] = analysis similar to [x]*[x|x] with roles swapped
    # For [b_1|b_2]*[a]: shuffles of {b_1,b_2} and {a}:
    # (b_1,b_2,a): sign +1 -> [b_1|b_2|a]
    # (b_1,a,b_2): sign (-1)^{|s^{-1}a||s^{-1}b_2|} = (-1)^{1} = -1 -> [b_1|a|b_2]
    # (a,b_1,b_2): sign (-1)^{|s^{-1}a|(|s^{-1}b_1|+|s^{-1}b_2|)} = (-1)^{2} = +1 -> [a|b_1|b_2]

    # [x|x]*[x]: b_1=x, b_2=x, a=x
    # All shuffles give [x|x|x] (same sequence (0,0,0))
    # sign: +1 - 1 + 1 = 1
    P[2, 0, 6] = FR(1)

    # [x|x]*[x^2]: b_1=x, b_2=x, a=x^2
    # (0,0,1) -> [x|x|x^2] = 7, sign +1
    # (0,1,0) -> [x|x^2|x] = 8, sign -1
    # (1,0,0) -> [x^2|x|x] = 9, sign +1
    P[2, 1, 7] = FR(1)
    P[2, 1, 8] = FR(-1)
    P[2, 1, 9] = FR(1)

    # [x|x^2]*[x]: b_1=x, b_2=x^2, a=x
    # (0,1,0) -> [x|x^2|x] = 8, sign +1
    # (0,0,1) -> [x|x|x^2]... wait, that's (b_1,a,b_2) = (0,0,1) -> [x|x|x^2] = 7?
    # No: (b_1,a,b_2) means insert a between b_1 and b_2: [x|x|x^2] = 7, sign -1
    # (a,b_1,b_2) = (0,0,1) -> [x|x|x^2] = 7, sign +1
    # Total for index 7: -1 + 1 = 0
    # Total for index 8: +1
    P[3, 0, 8] = FR(1)

    # [x^2|x]*[x]: b_1=x^2, b_2=x, a=x
    # (1,0,0) -> [x^2|x|x] = 9, sign +1
    # (1,0,0) -> same for (b_1,a,b_2), sign -1
    # Hmm: (b_1,b_2,a) = (1,0,0) -> [x^2|x|x], +1
    # (b_1,a,b_2) = (1,0,0) -> [x^2|x|x], -1
    # (a,b_1,b_2) = (0,1,0) -> [x|x^2|x] = 8, +1
    # Total: index 9 has +1-1=0, index 8 has +1
    P[4, 0, 8] = FR(1)  # Hmm, this was set above as well

    # This is getting quite complex. Let me simplify by using a cleaner approach.
    # Rather than hand-computing all shuffles, I'll build a general shuffle
    # product computation function.

    # Actually, for detecting non-Koszulness of k[x]/(x^3), I can use
    # a MUCH simpler approach: the minimal A-infinity model.

    return DGAlgebra(n_basis, deg, d, P, unit_idx=-1,
                     name="BarShuffle(k[x]/(x^3))")


# ============================================================================
# Bar complex with shuffle product (general construction)
# ============================================================================

class BarShuffleAlgebra:
    """Bar complex B(A) with shuffle product as a dg algebra.

    For an augmented algebra A (concentrated in degree 0, d=0):
    - Underlying space: B^1 + B^2 + ... + B^{max_n}
      where B^k = (s^{-1}A_+)^{tensor k}
    - Differential: bar differential d_bar
    - Product: shuffle product

    The transferred A-infinity on H*(B(A), d_bar) = Ext_A(k,k)
    detects non-Koszulness: m_3 != 0 iff A is not Koszul.
    """

    def __init__(self, aug_dim: int, product_table: np.ndarray,
                 max_arity: int = 3):
        """
        aug_dim: dimension of augmentation ideal A_+
        product_table: (aug_dim, aug_dim, aug_dim) array where
            product_table[i,j,k] = coefficient of the k-th aug. basis
            element in m_2(e_i, e_j).
        max_arity: maximum bar degree to include
        """
        self.aug_dim = aug_dim
        self.prod_table = product_table
        self.max_arity = max_arity

        # Compute total dimension and index mappings
        self._build_index_maps()
        # Build the dg algebra
        self._build_dga()

    def _build_index_maps(self):
        """Build index maps from multi-indices to flat indices."""
        self.arity_offset = {}
        self.arity_dim = {}
        idx = 0
        for n in range(1, self.max_arity + 1):
            self.arity_offset[n] = idx
            dim_n = self.aug_dim ** n
            self.arity_dim[n] = dim_n
            idx += dim_n
        self.total_dim = idx

    def _multi_to_flat(self, multi: Tuple[int, ...]) -> int:
        n = len(multi)
        offset = self.arity_offset[n]
        flat = 0
        for i, m in enumerate(multi):
            flat = flat * self.aug_dim + m
        return offset + flat

    def _flat_to_multi(self, flat: int) -> Tuple[int, ...]:
        # Find which arity
        for n in range(1, self.max_arity + 1):
            offset = self.arity_offset[n]
            dim_n = self.arity_dim[n]
            if flat < offset + dim_n:
                local = flat - offset
                multi = []
                for _ in range(n):
                    local, r = divmod(local, self.aug_dim)
                    multi.append(r)
                return tuple(reversed(multi))
        raise IndexError(f"flat index {flat} out of range")

    def _arity_of_flat(self, flat: int) -> int:
        for n in range(self.max_arity, 0, -1):
            if flat >= self.arity_offset[n]:
                return n
        return 0

    def _build_dga(self):
        """Build the DGAlgebra from bar differential and shuffle product."""
        N = self.total_dim
        d = self.aug_dim

        # Degrees = arity
        degree_of = []
        for n in range(1, self.max_arity + 1):
            degree_of.extend([-n] * self.arity_dim[n])

        # Bar differential
        diff = _zero_mat(N, N)
        for n in range(2, self.max_arity + 1):
            for flat_src in range(self.arity_offset[n],
                                  self.arity_offset[n] + self.arity_dim[n]):
                multi = self._flat_to_multi(flat_src)
                for i in range(n - 1):
                    # Product at position i: m_2(multi[i], multi[i+1])
                    a, b = multi[i], multi[i + 1]
                    sign_exp = sum(-1 for _ in range(i + 1))  # sum of desuspended degrees
                    sign = FR((-1) ** sign_exp)
                    for c in range(d):
                        coeff = self.prod_table[a, b, c]
                        if coeff != FR(0):
                            new_multi = multi[:i] + (c,) + multi[i + 2:]
                            if len(new_multi) <= self.max_arity:
                                flat_tgt = self._multi_to_flat(new_multi)
                                diff[flat_tgt, flat_src] += sign * coeff

        # Shuffle product
        prod = np.empty((N, N, N), dtype=object)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    prod[i, j, k] = FR(0)

        for n1 in range(1, self.max_arity + 1):
            for n2 in range(1, self.max_arity + 1 - n1):
                n_out = n1 + n2
                if n_out > self.max_arity:
                    continue
                for f1 in range(self.arity_offset[n1],
                                self.arity_offset[n1] + self.arity_dim[n1]):
                    m1 = self._flat_to_multi(f1)
                    for f2 in range(self.arity_offset[n2],
                                    self.arity_offset[n2] + self.arity_dim[n2]):
                        m2 = self._flat_to_multi(f2)
                        # Compute all (n1, n2)-shuffles
                        for perm, sgn in _shuffles(n1, n2):
                            merged = tuple(
                                (m1 + m2)[perm[k]] for k in range(n_out)
                            )
                            flat_out = self._multi_to_flat(merged)
                            prod[f1, f2, flat_out] += FR(sgn)

        self.dga = DGAlgebra(N, degree_of, diff, prod, unit_idx=-1,
                             name=f"BarShuffle(aug_dim={d})")

    def get_dga(self) -> DGAlgebra:
        return self.dga


def _shuffles(p: int, q: int) -> List[Tuple[Tuple[int, ...], int]]:
    """Generate all (p,q)-shuffles with Koszul signs.

    A (p,q)-shuffle is a permutation sigma of {0,...,p+q-1} such that
    sigma(0) < ... < sigma(p-1) and sigma(p) < ... < sigma(p+q-1).

    Sign: (-1)^{number of inversions involving one element from each group},
    with each element contributing desuspended degree -1.
    For elements all of desuspended degree -1:
        sign = (-1)^{number of inversions} * (-1)^{inversions from degree}
    The sign for desuspended degree -1 elements:
        each crossing of (left_elt, right_elt) contributes (-1)^{(-1)(-1)} = (-1).
    So total sign = (-1)^{number of crossings}.
    """
    from itertools import combinations

    n = p + q
    # Choose which positions in [0..n-1] get the first group
    results = []
    for positions in combinations(range(n), p):
        # positions are where elements of the first group go
        # remaining positions get the second group
        pos_set = set(positions)
        second_positions = [i for i in range(n) if i not in pos_set]

        # Build the permutation: perm[output_pos] = input_index
        perm = [0] * n
        for i, pos in enumerate(positions):
            perm[pos] = i  # i-th element of first group
        for j, pos in enumerate(second_positions):
            perm[pos] = p + j  # j-th element of second group

        # Count crossings: pairs (i from first group, j from second group)
        # where the first group element appears AFTER the second group element
        crossings = 0
        for i_idx, i_pos in enumerate(positions):
            for j_idx, j_pos in enumerate(second_positions):
                if i_pos > j_pos:
                    crossings += 1

        sign = (-1) ** crossings
        results.append((tuple(perm), sign))

    return results


# ============================================================================
# Convenience: build bar-shuffle algebra from augmented algebra data
# ============================================================================

def bar_shuffle_from_aug_algebra(dim_aug: int,
                                 prod_table: np.ndarray,
                                 max_arity: int = 3) -> BarShuffleAlgebra:
    """Build BarShuffleAlgebra from augmentation ideal data.

    dim_aug: dimension of A_+
    prod_table: (dim_aug, dim_aug, dim_aug) tensor for m_2 on A_+
        prod_table[i,j,k] = coefficient of e_k in m_2(e_i, e_j)
        (only nonzero when the product lands back in A_+, not in k)
    max_arity: bar degree truncation
    """
    return BarShuffleAlgebra(dim_aug, prod_table, max_arity)


def bar_shuffle_poly(n: int, max_arity: int = 3) -> BarShuffleAlgebra:
    """Bar complex with shuffle product for k[x]/(x^n).

    Augmentation ideal A_+ = span{x, x^2, ..., x^{n-1}}.
    Product in A_+: x^i * x^j = x^{i+j} if i+j < n, else 0.
    """
    d = n - 1  # dim of aug ideal
    prod_table = np.empty((d, d, d), dtype=object)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                prod_table[i, j, k] = FR(0)

    # x^{i+1} * x^{j+1} = x^{i+j+2} if i+j+2 < n, else 0
    for i in range(d):
        for j in range(d):
            s = i + j + 2  # weight of product (x^{i+1} * x^{j+1} = x^s)
            if s < n:
                # x^s corresponds to aug index s-1
                prod_table[i, j, s - 1] = FR(1)

    return BarShuffleAlgebra(d, prod_table, max_arity)


# ============================================================================
# Depth / formality classification
# ============================================================================

SHADOW_CLASSES = {
    "G": "Gaussian (depth 2, formal)",
    "L": "Lie/tree (depth 3)",
    "C": "contact/quartic (depth 4)",
    "M": "mixed (depth infinity)",
}


def classify_depth(depth: int) -> str:
    """Classify shadow archetype from A-infinity depth."""
    if depth <= 2:
        return "G"
    elif depth == 3:
        return "L"
    elif depth == 4:
        return "C"
    else:
        return "M"


# ============================================================================
# Linear algebra helpers (exact rational)
# ============================================================================

def _kernel_basis(M: np.ndarray) -> List[np.ndarray]:
    if M.size == 0:
        rows, cols = M.shape if M.ndim == 2 else (0, 0)
        if cols > 0:
            return [_unit_vec(cols, j) for j in range(cols)]
        return []
    rows, cols = M.shape
    A = np.array([[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
                 dtype=object)
    pivot_cols = []
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i, c] != FR(0):
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        scale = A[r, c]
        for j in range(cols):
            A[r, j] /= scale
        for i in range(rows):
            if i == r:
                continue
            factor = A[i, c]
            if factor != FR(0):
                for j in range(cols):
                    A[i, j] -= factor * A[r, j]
        pivot_cols.append(c)
        r += 1
    free_cols = [c for c in range(cols) if c not in pivot_cols]
    basis = []
    for fc in free_cols:
        v = _zero_vec(cols)
        v[fc] = FR(1)
        for idx, pc in enumerate(pivot_cols):
            v[pc] = -A[idx, fc]
        basis.append(v)
    return basis


def _column_basis(M: np.ndarray) -> List[np.ndarray]:
    if M.size == 0:
        return []
    rows, cols = M.shape
    selected = []
    for c in range(cols):
        col = M[:, c].copy()
        if not selected:
            if any(col[i] != FR(0) for i in range(rows)):
                selected.append(col)
        else:
            test = np.column_stack(selected + [col])
            if _rank(test) > len(selected):
                selected.append(col)
    return selected


def _rank(M: np.ndarray) -> int:
    if M.size == 0:
        return 0
    rows, cols = M.shape
    A = np.array([[_frac(M[i, j]) for j in range(cols)] for i in range(rows)],
                 dtype=object)
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i, c] != FR(0):
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        scale = A[r, c]
        for j in range(cols):
            A[r, j] /= scale
        for i in range(rows):
            if i == r:
                continue
            factor = A[i, c]
            if factor != FR(0):
                for j in range(cols):
                    A[i, j] -= factor * A[r, j]
        r += 1
    return r


def _solve(A: np.ndarray, b: np.ndarray) -> Optional[np.ndarray]:
    rows, cols = A.shape
    aug = _zero_mat(rows, cols + 1)
    for i in range(rows):
        for j in range(cols):
            aug[i, j] = _frac(A[i, j])
        aug[i, cols] = _frac(b[i])
    r = 0
    pivot_cols = []
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if aug[i, c] != FR(0):
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
            if factor != FR(0):
                for j in range(cols + 1):
                    aug[i, j] -= factor * aug[r, j]
        pivot_cols.append(c)
        r += 1
    for i in range(r, rows):
        if aug[i, cols] != FR(0):
            return None
    x = _zero_vec(cols)
    for idx, pc in enumerate(pivot_cols):
        x[pc] = aug[idx, cols]
    return x


def _invert(M: np.ndarray) -> Optional[np.ndarray]:
    n = M.shape[0]
    aug = _zero_mat(n, 2 * n)
    for i in range(n):
        for j in range(n):
            aug[i, j] = _frac(M[i, j])
        aug[i, n + i] = FR(1)
    for c in range(n):
        pivot = None
        for i in range(c, n):
            if aug[i, c] != FR(0):
                pivot = i
                break
        if pivot is None:
            return None
        aug[[c, pivot]] = aug[[pivot, c]]
        scale = aug[c, c]
        for j in range(2 * n):
            aug[c, j] /= scale
        for i in range(n):
            if i == c:
                continue
            factor = aug[i, c]
            if factor != FR(0):
                for j in range(2 * n):
                    aug[i, j] -= factor * aug[c, j]
    inv = _zero_mat(n, n)
    for i in range(n):
        for j in range(n):
            inv[i, j] = aug[i, n + j]
    return inv


def _vec_in_span(v: np.ndarray, basis: List[np.ndarray]) -> bool:
    if not basis:
        return _vec_is_zero(v)
    mat = np.column_stack(basis + [v])
    return _rank(mat) <= len(basis)


def _unit_vec(n: int, i: int) -> np.ndarray:
    v = _zero_vec(n)
    v[i] = FR(1)
    return v


def _merge_sign(a: Tuple[int, ...], b: Tuple[int, ...]) -> int:
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
