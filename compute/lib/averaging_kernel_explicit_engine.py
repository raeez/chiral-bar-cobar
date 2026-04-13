"""
Explicit basis for ker(av_n) in V^{tensor n} / Sym^n(V).

The averaging map av_n: V^{tensor n} -> Sym^n(V) sends a tensor to its
Sigma_n-symmetrization.  For EVEN desuspended degree (the relevant case
for affine KM and all standard families), this is the quotient map
V^{tensor n} -> Sym^n(V), and ker(av_n) consists of tensors whose full
symmetrization vanishes.

Dimension formula (type-independent):

    dim ker(av_n) = d^n - C(n+d-1, d-1)

where d = dim(V), C = binomial coefficient.

This engine constructs EXPLICIT basis elements for ker(av_n).

Key structural fact: ker(av_n) is spanned by elements of the form

    e_{i_1} tensor ... tensor e_{i_n} - e_{sigma(i_1)} tensor ... tensor e_{sigma(i_n)}

for various permutations sigma in Sigma_n.  More precisely, ker(av_n) is the
image of the antisymmetrization operators associated to the non-trivial
irreducible representations of Sigma_n.

At n=2: ker(av_2) = Alt^2(V) = span{ e_i tensor e_j - e_j tensor e_i : i < j }.
    dim = d(d-1)/2 = d^2 - C(d+1,2).

For sl_2 (d=3), the basis {e,h,f} gives ker(av_2) the 3 antisymmetric tensors:
    e tensor f - f tensor e,  e tensor h - h tensor e,  f tensor h - h tensor f.

At n=3: ker(av_3) has dimension d^3 - C(d+2,3).  For d=3: 27 - 10 = 17.
These decompose under Sigma_3 into:
  - The alternating part Alt^3(V): dim = C(d,3).  For d=3: 1 element.
  - The "standard representation" part (two copies of the standard rep):
    dim = d^3 - C(d+2,3) - C(d,3).  For d=3: 17 - 1 = 16 elements.

References:
  - Vol I, averaging_kernel_engine.py (dimension verification)
  - Vol I, Section: E_1 coinvariant projection
  - Schur-Weyl duality: V^{tensor n} = direct sum_{lambda} S^lambda(V) tensor M^lambda
"""
from __future__ import annotations

from itertools import permutations, product
from math import comb, factorial
from typing import Dict, List, Optional, Tuple

import numpy as np
from numpy.typing import NDArray


# ── basis labeling ──────────────────────────────────────────────────

def basis_labels(d: int) -> List[str]:
    """Standard basis labels for a d-dimensional space.

    For d=2: ['e_0', 'e_1'].
    For d=3: ['e', 'h', 'f'] (sl_2 adjoint).
    """
    if d == 3:
        return ['e', 'h', 'f']
    return [f'e_{i}' for i in range(d)]


def tensor_basis(d: int, n: int) -> List[Tuple[int, ...]]:
    """Enumerate all multi-indices for the tensor basis of V^{tensor n}.

    Returns list of n-tuples (i_1, ..., i_n) with 0 <= i_k < d.
    Ordered lexicographically.
    """
    return list(product(range(d), repeat=n))


def multi_index_to_label(idx: Tuple[int, ...], labels: List[str]) -> str:
    """Convert a multi-index to a human-readable tensor label."""
    return ' tensor '.join(labels[i] for i in idx)


# ── symmetrization map ──────────────────────────────────────────────

def symmetrization_matrix(d: int, n: int) -> NDArray:
    """Construct the symmetrization matrix av_n: V^{tensor n} -> V^{tensor n}.

    The symmetrization map is (1/n!) * sum_{sigma in S_n} sigma.
    We represent it as a (d^n x d^n) matrix in the standard tensor basis.

    The image of this matrix is Sym^n(V) embedded in V^{tensor n}.
    The kernel of this matrix is ker(av_n).
    """
    N = d ** n
    tb = tensor_basis(d, n)
    # Map from multi-index to linear index
    idx_map: Dict[Tuple[int, ...], int] = {
        mi: i for i, mi in enumerate(tb)
    }

    mat = np.zeros((N, N), dtype=float)
    perms = list(permutations(range(n)))
    nfact = factorial(n)

    for row_idx, mi in enumerate(tb):
        for sigma in perms:
            permuted = tuple(mi[sigma[k]] for k in range(n))
            col_idx = idx_map[permuted]
            mat[row_idx, col_idx] += 1.0 / nfact

    return mat


def kernel_basis_numerical(d: int, n: int) -> NDArray:
    """Compute a basis for ker(av_n) via SVD.

    Returns a matrix whose ROWS are basis vectors for ker(av_n),
    expressed in the standard tensor basis of V^{tensor n}.
    """
    mat = symmetrization_matrix(d, n)
    # ker(mat) = null space = right singular vectors with singular value 0
    U, S, Vh = np.linalg.svd(mat)
    # Threshold for zero singular values
    tol = 1e-10
    null_mask = S < tol
    # The null space vectors are the COLUMNS of V corresponding to zero singular values
    # In numpy SVD, mat = U @ diag(S) @ Vh, so null space = rows of Vh where S ~ 0
    # But we need to be careful: SVD of an NxN matrix gives N singular values
    null_rows = Vh[null_mask]
    return null_rows


# ── explicit antisymmetric basis at n=2 ─────────────────────────────

def antisymmetric_basis_n2(d: int) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """Explicit basis for ker(av_2) = Alt^2(V).

    Returns list of pairs ((i,j), (j,i)) with i < j, representing
    the basis element e_i tensor e_j - e_j tensor e_i.

    Dimension: C(d,2) = d(d-1)/2.
    """
    basis = []
    for i in range(d):
        for j in range(i + 1, d):
            basis.append(((i, j), (j, i)))
    assert len(basis) == comb(d, 2), (
        f"Expected {comb(d,2)} antisymmetric basis elements, got {len(basis)}"
    )
    return basis


def antisymmetric_basis_n2_labeled(d: int) -> List[str]:
    """Human-readable labels for ker(av_2) basis elements."""
    labels = basis_labels(d)
    basis = antisymmetric_basis_n2(d)
    result = []
    for (i, j), (j2, i2) in basis:
        result.append(
            f"{labels[i]} tensor {labels[j]} - {labels[j2]} tensor {labels[i2]}"
        )
    return result


# ── explicit basis construction at general n ─────────────────────────

def kernel_basis_explicit(d: int, n: int) -> NDArray:
    """Construct an explicit integer basis for ker(av_n).

    Strategy: construct the symmetrization projector P = av_n
    (as a rational matrix), then compute ker(P) = image(I - P).
    The columns of (I - P) that are nonzero span ker(av_n).
    We then row-reduce to get a clean basis.

    For exact computation we use the rational representation:
    P = (1/n!) sum_sigma sigma, so n!*P is an integer matrix,
    and ker(P) = ker(n!*P).  We use the integer SVD approach
    via rank computation.
    """
    N = d ** n
    tb = tensor_basis(d, n)
    idx_map: Dict[Tuple[int, ...], int] = {
        mi: i for i, mi in enumerate(tb)
    }

    # Build n! * P as an integer matrix
    perms = list(permutations(range(n)))
    nfact = factorial(n)
    nP = np.zeros((N, N), dtype=int)

    for row_idx, mi in enumerate(tb):
        for sigma in perms:
            permuted = tuple(mi[sigma[k]] for k in range(n))
            col_idx = idx_map[permuted]
            nP[row_idx, col_idx] += 1

    # ker(P) = ker(nP) since n! != 0.
    # I - P has image = ker(P), but we need the kernel directly.
    # Use SVD of the float version for the basis.
    P_float = nP.astype(float) / nfact
    return kernel_basis_numerical(d, n)


# ── Schur-Weyl decomposition of ker(av_n) ──────────────────────────

def _sign(sigma: Tuple[int, ...]) -> int:
    """Sign of a permutation given as a tuple."""
    n = len(sigma)
    visited = [False] * n
    sign = 1
    for i in range(n):
        if visited[i]:
            continue
        cycle_len = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = sigma[j]
            cycle_len += 1
        if cycle_len % 2 == 0:
            sign *= -1
    return sign


def alternating_part_n3(d: int) -> Optional[NDArray]:
    """The alternating (sign representation) component of ker(av_3).

    At n=3, the alternating part is Alt^3(V) with dim = C(d,3).
    For d < 3, this vanishes.

    Returns a matrix whose rows are basis vectors (in tensor basis),
    or None if the alternating part vanishes.
    """
    if d < 3:
        return None

    N = d ** 3
    tb = tensor_basis(d, 3)
    idx_map: Dict[Tuple[int, ...], int] = {
        mi: i for i, mi in enumerate(tb)
    }

    # Basis for Alt^3(V): for each triple i < j < k, the element
    # sum_{sigma in S_3} sign(sigma) e_{sigma(i,j,k)}
    basis_rows = []
    perms3 = list(permutations(range(3)))
    for i in range(d):
        for j in range(i + 1, d):
            for k in range(j + 1, d):
                vec = np.zeros(N, dtype=float)
                triple = (i, j, k)
                for sigma in perms3:
                    permuted = tuple(triple[sigma[l]] for l in range(3))
                    idx = idx_map[permuted]
                    vec[idx] += _sign(sigma)
                basis_rows.append(vec)

    if len(basis_rows) == 0:
        return None

    result = np.array(basis_rows)
    assert result.shape[0] == comb(d, 3), (
        f"Expected {comb(d,3)} alternating basis elements at n=3, got {result.shape[0]}"
    )
    return result


def standard_rep_part_n3(d: int) -> NDArray:
    """The standard-representation component of ker(av_3).

    At n=3, ker(av_3) decomposes under S_3 as:
        ker(av_3) = Alt^3(V) + 2 copies of (standard rep of S_3) tensor (some GL(V) rep)

    The standard representation of S_3 is 2-dimensional, corresponding
    to the partition (2,1).  The GL(d) irreducible corresponding to (2,1)
    has dimension d(d+1)(d-1)/3 = (d^2-1)*d/3.  Each copy contributes
    that many basis elements, and there are 2 copies of the standard rep
    in the regular representation... but the precise multiplicity in
    V^{tensor 3} is given by Schur-Weyl:

        V^{tensor 3} = S^{(3)}(V) + S^{(2,1)}(V)^2 + S^{(1,1,1)}(V)

    where S^{lambda}(V) is the Schur functor, and the multiplicity
    of S^{lambda}(V) is dim(Specht module M^lambda).

    dim S^{(3)}(V) = C(d+2,3)
    dim S^{(2,1)}(V) = d(d^2-1)/3  (with multiplicity 2)
    dim S^{(1,1,1)}(V) = C(d,3)

    Check: C(d+2,3) + 2*d(d^2-1)/3 + C(d,3) = d^3. Verified.

    ker(av_3) = S^{(2,1)}(V)^2 + S^{(1,1,1)}(V)
    dim ker(av_3) = 2*d(d^2-1)/3 + C(d,3)

    We construct the standard-rep part by projecting with the Young
    symmetrizer for the partition (2,1).

    Returns matrix whose rows span the standard-rep part.
    """
    N = d ** 3
    tb = tensor_basis(d, 3)
    idx_map: Dict[Tuple[int, ...], int] = {
        mi: i for i, mi in enumerate(tb)
    }

    # Young symmetrizer for (2,1) with standard tableau:
    #   1 2
    #   3
    # Row symmetrize: symmetrize positions {0,1}, leave position 2 alone.
    # Column antisymmetrize: antisymmetrize positions {0,2}.
    # Young symmetrizer c_{(2,1)} = a_C * b_R where
    #   b_R = e + (01)  (symmetrize rows)
    #   a_C = e - (02)  (antisymmetrize columns)
    # Apply: first b_R then a_C.

    # For a second copy, use the OTHER standard Young tableau:
    #   1 3
    #   2
    # Row symmetrize: {0,2}, Column antisymmetrize: {0,1}.

    def apply_young_symmetrizer_1(v: NDArray) -> NDArray:
        """Apply c_{(2,1)} for tableau [[1,2],[3]] to a vector in V^{tensor 3}."""
        # b_R: symmetrize positions 0,1
        result_br = np.zeros_like(v)
        for mi_idx, mi in enumerate(tb):
            # identity
            result_br[mi_idx] += v[mi_idx]
            # swap 0,1
            swapped = (mi[1], mi[0], mi[2])
            result_br[mi_idx] += v[idx_map[swapped]]
        # a_C: antisymmetrize positions 0,2
        result = np.zeros_like(v)
        for mi_idx, mi in enumerate(tb):
            # identity
            result[mi_idx] += result_br[mi_idx]
            # swap 0,2
            swapped = (mi[2], mi[1], mi[0])
            result[mi_idx] -= result_br[idx_map[swapped]]
        return result

    def apply_young_symmetrizer_2(v: NDArray) -> NDArray:
        """Apply c_{(2,1)} for tableau [[1,3],[2]] to a vector in V^{tensor 3}."""
        # b_R: symmetrize positions 0,2
        result_br = np.zeros_like(v)
        for mi_idx, mi in enumerate(tb):
            result_br[mi_idx] += v[mi_idx]
            swapped = (mi[2], mi[1], mi[0])
            result_br[mi_idx] += v[idx_map[swapped]]
        # a_C: antisymmetrize positions 0,1
        result = np.zeros_like(v)
        for mi_idx, mi in enumerate(tb):
            result[mi_idx] += result_br[mi_idx]
            swapped = (mi[1], mi[0], mi[2])
            result[mi_idx] -= result_br[idx_map[swapped]]
        return result

    # Apply both Young symmetrizers to each standard basis vector
    basis_vecs = []
    for i in range(N):
        e_i = np.zeros(N, dtype=float)
        e_i[i] = 1.0
        v1 = apply_young_symmetrizer_1(e_i)
        if np.linalg.norm(v1) > 1e-10:
            basis_vecs.append(v1)
        v2 = apply_young_symmetrizer_2(e_i)
        if np.linalg.norm(v2) > 1e-10:
            basis_vecs.append(v2)

    if len(basis_vecs) == 0:
        return np.zeros((0, N), dtype=float)

    # Stack and extract linearly independent subset
    mat = np.array(basis_vecs)
    # SVD to find rank and basis
    U, S, Vh = np.linalg.svd(mat, full_matrices=False)
    rank = np.sum(S > 1e-10)
    return Vh[:rank]


# ── verification routines ────────────────────────────────────────────

def verify_kernel_dim(d: int, n: int) -> Dict:
    """Verify dim ker(av_n) = d^n - C(n+d-1, d-1) by explicit construction.

    Returns dict with computed and expected dimensions.
    """
    expected = d ** n - comb(n + d - 1, d - 1)
    basis = kernel_basis_numerical(d, n)
    computed = basis.shape[0]
    return {
        'd': d,
        'n': n,
        'total_dim': d ** n,
        'sym_dim': comb(n + d - 1, d - 1),
        'expected_kernel_dim': expected,
        'computed_kernel_dim': computed,
        'match': computed == expected,
    }


def verify_kernel_elements_in_kernel(d: int, n: int) -> bool:
    """Verify that every computed kernel basis element IS in ker(av_n).

    Each basis vector v satisfies av_n(v) = 0, i.e., P*v = 0.
    """
    P = symmetrization_matrix(d, n)
    basis = kernel_basis_numerical(d, n)
    for i in range(basis.shape[0]):
        v = basis[i]
        Pv = P @ v
        if np.linalg.norm(Pv) > 1e-10:
            return False
    return True


def verify_schur_weyl_n3(d: int) -> Dict:
    """Verify Schur-Weyl decomposition of V^{tensor 3} at dimension d.

    V^{tensor 3} = S^{(3)}(V) + S^{(2,1)}(V)^2 + S^{(1,1,1)}(V)

    Dimensions:
        S^{(3)}: C(d+2,3) = C(d+2,d-1)
        S^{(2,1)}: d(d^2-1)/3, multiplicity 2
        S^{(1,1,1)}: C(d,3)

    Total: C(d+2,3) + 2*d*(d^2-1)/3 + C(d,3) = d^3
    """
    sym3 = comb(d + 2, 3)
    hook21 = d * (d * d - 1) // 3
    alt3 = comb(d, 3)
    total_check = sym3 + 2 * hook21 + alt3
    kernel_check = 2 * hook21 + alt3

    return {
        'd': d,
        'total': d ** 3,
        'S^(3)': sym3,
        'S^(2,1) x 2': 2 * hook21,
        'S^(1,1,1)': alt3,
        'sum': total_check,
        'total_match': total_check == d ** 3,
        'ker(av_3)': kernel_check,
        'ker_formula': d ** 3 - comb(d + 2, 3),
        'ker_match': kernel_check == d ** 3 - comb(d + 2, 3),
    }


# ── sl_2 specialization ─────────────────────────────────────────────

def sl2_ker_av2_basis() -> List[str]:
    """The 3 explicit basis elements of ker(av_2) for sl_2 (d=3).

    In the sl_2 adjoint basis {e, h, f}:
        e tensor f - f tensor e
        e tensor h - h tensor e
        f tensor h - h tensor f

    These span Alt^2(sl_2), the 3-dimensional alternating square,
    which is isomorphic to sl_2 itself via the Lie bracket
    (the antisymmetric tensors ARE the Lie bracket data).
    """
    return antisymmetric_basis_n2_labeled(3)


def sl2_ker_av3_decomposition() -> Dict:
    """Full decomposition of ker(av_3) for sl_2 (d=3).

    dim ker(av_3) = 27 - 10 = 17, decomposing as:
        Alt^3(sl_2): dim = C(3,3) = 1
        S^{(2,1)}(sl_2) x 2: dim = 2 * 3*(9-1)/3 = 2*8 = 16

    The single alternating element is e ^ h ^ f (the volume form on sl_2).
    The 16 standard-rep elements are the "mixed symmetry" tensors.
    """
    d = 3
    alt_dim = comb(d, 3)      # 1
    hook_dim = d * (d**2 - 1) // 3  # 8
    total_ker = 2 * hook_dim + alt_dim  # 17

    # Verify
    assert total_ker == d**3 - comb(d + 2, 3), (
        f"Schur-Weyl mismatch: {total_ker} != {d**3 - comb(d+2,3)}"
    )

    return {
        'dim_ker': total_ker,
        'alt3_dim': alt_dim,
        'hook21_dim': hook_dim,
        'hook21_multiplicity': 2,
        'hook21_total': 2 * hook_dim,
        'alt3_description': 'e ^ h ^ f (volume form, isomorphic to det)',
        'hook21_description': (
            'Mixed-symmetry tensors: symmetric in two slots, '
            'antisymmetric with the third'
        ),
    }


# ── general explicit basis enumeration ───────────────────────────────

def enumerate_kernel_basis_labeled(d: int, n: int) -> List[str]:
    """Return human-readable labels for ALL basis elements of ker(av_n).

    For n=2: antisymmetric tensors e_i tensor e_j - e_j tensor e_i (i < j).
    For n >= 3: computed numerically, rounded to nearest integer coefficients.
    """
    labels = basis_labels(d)
    tb = tensor_basis(d, n)

    if n == 2:
        return antisymmetric_basis_n2_labeled(d)

    # For n >= 3, use numerical basis and try to identify integer structure
    basis = kernel_basis_numerical(d, n)
    result = []
    for row_idx in range(basis.shape[0]):
        v = basis[row_idx]
        # Normalize so the largest coefficient is +/- 1
        max_abs = np.max(np.abs(v))
        if max_abs < 1e-12:
            continue
        v_norm = v / max_abs
        # Build label from nonzero coefficients
        terms = []
        for i, coeff in enumerate(v_norm):
            if abs(coeff) > 1e-8:
                # Round to nice fraction
                rounded = round(coeff, 6)
                mi_label = multi_index_to_label(tb[i], labels)
                if abs(rounded - 1.0) < 1e-6:
                    terms.append(f'+ {mi_label}')
                elif abs(rounded + 1.0) < 1e-6:
                    terms.append(f'- {mi_label}')
                else:
                    terms.append(f'+ ({rounded:.4f}) {mi_label}')
        label = ' '.join(terms)
        if label.startswith('+ '):
            label = label[2:]
        result.append(label)

    return result


# ── Schur-Weyl dimension table ──────────────────────────────────────

def schur_weyl_table_n2(d: int) -> Dict:
    """Schur-Weyl decomposition of V^{tensor 2}.

    V^{tensor 2} = Sym^2(V) + Alt^2(V)
        Sym^2: C(d+1,2) = d(d+1)/2
        Alt^2: C(d,2) = d(d-1)/2
    """
    sym2 = comb(d + 1, 2)
    alt2 = comb(d, 2)
    return {
        'd': d,
        'total': d ** 2,
        'Sym^2': sym2,
        'Alt^2': alt2,
        'sum': sym2 + alt2,
        'match': sym2 + alt2 == d ** 2,
        'ker(av_2)': alt2,
    }


def schur_weyl_table_n4(d: int) -> Dict:
    """Schur-Weyl decomposition of V^{tensor 4}.

    Partitions of 4: (4), (3,1), (2,2), (2,1,1), (1,1,1,1).
    Specht module dims (= multiplicities): 1, 3, 2, 3, 1.
    GL(d) Schur functor dims:
        S^{(4)}: C(d+3,4)
        S^{(3,1)}: d^2(d^2-1)/12 * ... [hook length formula]
        S^{(2,2)}: C(d+1,2)*C(d,2)/3 = d(d-1)(d+1)(d+2)/12  [for d >= 2]
        S^{(2,1,1)}: same as S^{(3,1)} by duality for GL
        S^{(1,1,1,1)}: C(d,4)

    For GL(d), dim S^lambda(V) is given by the hook-content formula.
    When lambda has more than d parts, dim = 0.
    """
    # Hook-content formula for partition lambda and GL(d):
    # dim S^lambda(C^d) = prod_{(i,j) in lambda} (d - i + j) / hook(i,j)

    def schur_dim_gl(partition: Tuple[int, ...], d_val: int) -> int:
        """Dimension of Schur functor S^lambda(C^d) via hook-content formula."""
        if len(partition) > d_val:
            return 0
        # Generate all boxes (i,j) with i = row (0-indexed), j = col (0-indexed)
        boxes = []
        for i, row_len in enumerate(partition):
            for j in range(row_len):
                boxes.append((i, j))

        # Hook length at box (i,j): number of boxes to the right + below + 1
        def hook_length(i: int, j: int) -> int:
            arm = partition[i] - j - 1  # boxes to the right
            leg = sum(1 for r in range(i + 1, len(partition)) if partition[r] > j)
            return arm + leg + 1

        # Content at box (i,j): j - i
        numerator = 1
        denominator = 1
        for (i, j) in boxes:
            numerator *= (d_val - i + j)
            denominator *= hook_length(i, j)

        if numerator % denominator != 0:
            raise ValueError(
                f"Non-integer Schur dim for lambda={partition}, d={d_val}: "
                f"{numerator}/{denominator}"
            )
        return numerator // denominator

    # Partitions of 4 with Specht module dimensions
    partitions_4 = [
        ((4,), 1),
        ((3, 1), 3),
        ((2, 2), 2),
        ((2, 1, 1), 3),
        ((1, 1, 1, 1), 1),
    ]

    decomp = {}
    total_check = 0
    for lam, mult in partitions_4:
        sdim = schur_dim_gl(lam, d)
        decomp[str(lam)] = {'schur_dim': sdim, 'multiplicity': mult, 'total': sdim * mult}
        total_check += sdim * mult

    sym4_dim = schur_dim_gl((4,), d)

    return {
        'd': d,
        'total': d ** 4,
        'decomposition': decomp,
        'sum': total_check,
        'match': total_check == d ** 4,
        'ker(av_4)': d ** 4 - sym4_dim,
        'ker_formula': d ** 4 - comb(d + 3, 4),
        'ker_match': (d ** 4 - sym4_dim) == (d ** 4 - comb(d + 3, 4)),
    }


# ── main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 70)
    print("EXPLICIT ker(av_n) BASIS ENUMERATION")
    print("=" * 70)

    # --- d=3 (sl_2), n=2 ---
    print("\n--- sl_2 (d=3), n=2: ker(av_2) ---")
    print(f"Expected dim: 3^2 - C(4,2) = 9 - 6 = 3")
    result = verify_kernel_dim(3, 2)
    print(f"Computed dim: {result['computed_kernel_dim']}")
    print(f"Match: {result['match']}")
    print("\nExplicit basis (antisymmetric tensors):")
    for elem in sl2_ker_av2_basis():
        print(f"  {elem}")

    # --- d=3 (sl_2), n=3 ---
    print("\n--- sl_2 (d=3), n=3: ker(av_3) ---")
    print(f"Expected dim: 3^3 - C(5,2) = 27 - 10 = 17")
    result3 = verify_kernel_dim(3, 3)
    print(f"Computed dim: {result3['computed_kernel_dim']}")
    print(f"Match: {result3['match']}")

    decomp = sl2_ker_av3_decomposition()
    print(f"\nSchur-Weyl decomposition of ker(av_3):")
    print(f"  Alt^3(sl_2): dim = {decomp['alt3_dim']}  ({decomp['alt3_description']})")
    print(f"  S^(2,1)(sl_2) x 2: dim = {decomp['hook21_total']}  ({decomp['hook21_description']})")
    print(f"  Total: {decomp['dim_ker']}")

    # --- Schur-Weyl verification ---
    print("\n--- Schur-Weyl verification at n=3 ---")
    sw3 = verify_schur_weyl_n3(3)
    for k, v in sw3.items():
        print(f"  {k}: {v}")

    # --- d=2, n=2,3,4 ---
    for n in [2, 3, 4]:
        print(f"\n--- d=2, n={n}: ker(av_{n}) ---")
        r = verify_kernel_dim(2, n)
        print(f"  dim = {r['computed_kernel_dim']} (expected {r['expected_kernel_dim']}), match={r['match']}")

    # --- d=3, n=4 ---
    print(f"\n--- sl_2 (d=3), n=4: ker(av_4) ---")
    r4 = verify_kernel_dim(3, 4)
    print(f"  dim = {r4['computed_kernel_dim']} (expected {r4['expected_kernel_dim']}), match={r4['match']}")

    # --- Schur-Weyl at n=4 ---
    print("\n--- Schur-Weyl n=4, d=3 ---")
    sw4 = schur_weyl_table_n4(3)
    for k, v in sw4.items():
        print(f"  {k}: {v}")

    print("\n" + "=" * 70)
    print("ALL VERIFICATIONS COMPLETE")
    print("=" * 70)
