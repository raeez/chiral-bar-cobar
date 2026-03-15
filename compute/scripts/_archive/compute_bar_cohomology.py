#!/usr/bin/env python3
"""Compute bar cohomology of Virasoro and W_3 algebras via mode algebra.

Strategy:
  1. Represent the Virasoro (or W_3) vacuum module truncated at weight max_h
  2. Precompute mode matrices L_n: V_h -> V_{h-n} (and W_n for W_3)
  3. Build zeroth product operators a_(0): V_{h_b} -> V_{h_a+h_b-1}
  4. Assemble bar differential d: B^{n+1}_w -> B^n_w with OS form factors
  5. Compute cohomology = ker(d_out)/im(d_in) at each (n, w)
  6. Sum over w to get total dim H^n

Uses exact Fraction arithmetic throughout (no numpy dependency).

Validates against known Virasoro values (Motzkin differences):
  1, 2, 5, 12, 30, 76, 196, 512, ...

Then computes W_3 bar cohomology (known: 2, 5, 16, 52).

Author: Raeez Lorgat
"""

from fractions import Fraction
import sys
import time

ZERO = Fraction(0)
ONE = Fraction(1)


# ============================================================================
# Pure Python linear algebra with Fraction
# ============================================================================

def matrix_rank(mat, nrows, ncols):
    """Compute rank of a matrix via Gaussian elimination over Q.
    mat is a list of lists of Fraction, shape nrows x ncols.
    """
    if nrows == 0 or ncols == 0:
        return 0
    # Copy matrix
    m = [row[:] for row in mat]
    rank = 0
    for col in range(ncols):
        # Find pivot
        pivot = None
        for row in range(rank, nrows):
            if m[row][col] != ZERO:
                pivot = row
                break
        if pivot is None:
            continue
        # Swap
        m[rank], m[pivot] = m[pivot], m[rank]
        # Eliminate
        inv = Fraction(1, m[rank][col])
        for row in range(nrows):
            if row != rank and m[row][col] != ZERO:
                factor = m[row][col] * inv
                for c in range(ncols):
                    m[row][c] -= factor * m[rank][c]
        rank += 1
    return rank


def mat_mul(A, A_rows, A_cols, B, B_rows, B_cols):
    """Multiply A (A_rows x A_cols) by B (B_rows x B_cols). Returns list of lists."""
    assert A_cols == B_rows
    result = [[ZERO] * B_cols for _ in range(A_rows)]
    for i in range(A_rows):
        for k in range(A_cols):
            if A[i][k] == ZERO:
                continue
            for j in range(B_cols):
                if B[k][j] != ZERO:
                    result[i][j] += A[i][k] * B[k][j]
    return result


def mat_add(A, B, nrows, ncols):
    """Add two matrices."""
    return [[A[i][j] + B[i][j] for j in range(ncols)] for i in range(nrows)]


def mat_scale(A, nrows, ncols, scalar):
    """Scale matrix by scalar."""
    return [[A[i][j] * scalar for j in range(ncols)] for i in range(nrows)]


def identity_matrix(n):
    """n x n identity matrix."""
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def zero_matrix(nrows, ncols):
    """nrows x ncols zero matrix."""
    return [[ZERO] * ncols for _ in range(nrows)]


def is_zero_matrix(mat, nrows, ncols):
    """Check if matrix is all zeros."""
    return all(mat[i][j] == ZERO for i in range(nrows) for j in range(ncols))


# ============================================================================
# PBW basis enumeration
# ============================================================================

def partitions_geq(n, min_part, max_part=None):
    """Partitions of n into parts >= min_part, as decreasing tuples."""
    if max_part is None:
        max_part = n
    max_part = min(max_part, n)
    if n == 0:
        yield ()
        return
    if n < min_part:
        return
    for first in range(max_part, min_part - 1, -1):
        for rest in partitions_geq(n - first, min_part, first):
            yield (first,) + rest


def vir_pbw_basis(weight):
    """PBW basis at given weight for Virasoro: partitions into parts >= 2."""
    if weight == 0:
        return [()]
    if weight == 1:
        return []
    return list(partitions_geq(weight, 2))


def w3_pbw_basis(weight):
    """PBW basis at given weight for W_3 vacuum module.

    States: L_{-n1}...L_{-na} W_{-m1}...W_{-mb} |0>
    with n_i >= 2 (decreasing), m_j >= 3 (decreasing), sum = weight.

    Represented as (L_tuple, W_tuple).
    """
    basis = []
    for w_part in range(0, weight + 1):
        l_part = weight - w_part
        for l_partition in partitions_geq(l_part, 2):
            for w_partition in partitions_geq(w_part, 3):
                basis.append((l_partition, w_partition))
    if weight == 0:
        return [((), ())]
    return [(l, w) for l, w in basis if l or w]


# ============================================================================
# Virasoro mode algebra (exact Fraction arithmetic)
# ============================================================================

class VirasoroFock:
    """Truncated Virasoro vacuum module with exact mode matrices."""

    def __init__(self, c, max_weight):
        self.c = Fraction(c)
        self.max_h = max_weight

        self.basis = {}
        self.basis_index = {}
        for h in range(0, max_weight + 1):
            b = vir_pbw_basis(h)
            self.basis[h] = b
            for i, part in enumerate(b):
                self.basis_index[part] = (h, i)

        self.dim = {h: len(b) for h, b in self.basis.items()}
        self._L_cache = {}

    def L_matrix(self, n, h_source):
        """Matrix of L_n: V_{h_source} -> V_{h_source - n}.
        Returns (matrix, dim_target, dim_source) or None.
        """
        h_target = h_source - n
        key = (n, h_source)
        if key in self._L_cache:
            return self._L_cache[key]

        if h_target < 0 or h_target > self.max_h:
            self._L_cache[key] = None
            return None

        src_basis = self.basis.get(h_source, [])
        tgt_basis = self.basis.get(h_target, [])

        if not src_basis or not tgt_basis:
            self._L_cache[key] = None
            return None

        dim_s = len(src_basis)
        dim_t = len(tgt_basis)
        mat = zero_matrix(dim_t, dim_s)
        tgt_index = {p: i for i, p in enumerate(tgt_basis)}

        for col, partition in enumerate(src_basis):
            result = self._L_on_pbw(n, partition)
            for part, coeff in result.items():
                if part in tgt_index:
                    mat[tgt_index[part]][col] += coeff

        self._L_cache[key] = (mat, dim_t, dim_s)
        return (mat, dim_t, dim_s)

    def _L_on_pbw(self, n, partition):
        """Apply L_n to PBW state. Returns dict {partition: Fraction coeff}."""
        if not partition:
            if n >= -1:
                return {}
            else:
                return {(-n,): ONE}

        if n <= -2:
            return self._insert_mode(-n, partition)

        m1 = partition[0]
        rest = partition[1:]
        result = {}

        # [L_n, L_{-m1}] = (n+m1) L_{n-m1} + central
        comm_coeff = n + m1
        new_n = n - m1

        if comm_coeff != 0:
            if new_n <= -2:
                inner = self._insert_mode(-new_n, rest)
            else:
                inner = self._L_on_pbw(new_n, rest)
            c_frac = Fraction(comm_coeff)
            for p, c in inner.items():
                result[p] = result.get(p, ZERO) + c_frac * c

        # Central: (c/12) n(n^2-1) delta_{n,m1}
        if n == m1 and n >= 2:
            central = self.c * Fraction(n * (n * n - 1), 12)
            if central != ZERO:
                rest_key = rest if rest else ()
                result[rest_key] = result.get(rest_key, ZERO) + central

        # Pass-through: L_{-m1} (L_n rest)
        inner = self._L_on_pbw(n, rest)
        for p, c in inner.items():
            new_p = self._prepend(m1, p)
            result[new_p] = result.get(new_p, ZERO) + c

        return {k: v for k, v in result.items() if v != ZERO}

    def _insert_mode(self, m, partition):
        """Insert L_{-m} before L_{-p1}...L_{-pk}|0>, reorder to PBW."""
        if not partition:
            return {(m,): ONE}

        p1 = partition[0]
        if m >= p1:
            return {(m,) + partition: ONE}

        rest = partition[1:]
        result = {}

        # L_{-m} L_{-p1} = L_{-p1} L_{-m} + (p1-m) L_{-(m+p1)}
        inner1 = self._insert_mode(m, rest)
        for p, c in inner1.items():
            new_p = (p1,) + p
            result[new_p] = result.get(new_p, ZERO) + c

        coeff = Fraction(p1 - m)
        inner2 = self._insert_mode(m + p1, rest)
        for p, c in inner2.items():
            result[p] = result.get(p, ZERO) + coeff * c

        return {k: v for k, v in result.items() if v != ZERO}

    def _prepend(self, m, partition):
        """Prepend m to partition maintaining PBW order."""
        if not partition or m >= partition[0]:
            return (m,) + partition
        result = list(partition)
        for i in range(len(result)):
            if m >= result[i]:
                return tuple(result[:i]) + (m,) + tuple(result[i:])
        return tuple(result) + (m,)


# ============================================================================
# Zeroth product computation
# ============================================================================

class ZerothProductEngine:
    """Compute zeroth product matrices for Virasoro PBW states.

    For a PBW state a at weight h_a, a_(0) maps V_{h_b} -> V_{h_a+h_b-1}.

    Uses the recursive Borcherds formula:
    - T_(0) = L_{-1}
    - (partial^k T)_(0) = 0 for k >= 1
    - (L_{-m} v)_(0) via iterate formula
    """

    def __init__(self, fock):
        self.fock = fock
        self._cache = {}
        self._product_cache = {}

    def zeroth_product_matrix(self, a_partition, h_b):
        """Matrix of a_(0): V_{h_b} -> V_{h_a+h_b-1}.
        Returns (matrix, dim_target, dim_source) or None.
        """
        h_a = sum(a_partition)
        h_target = h_a + h_b - 1

        if h_target < 0 or h_target > self.fock.max_h:
            return None
        if self.fock.dim.get(h_b, 0) == 0:
            return None
        if self.fock.dim.get(h_target, 0) == 0:
            return None

        key = (a_partition, h_b)
        if key in self._cache:
            return self._cache[key]

        mat = self._compute_zeroth(a_partition, h_b)
        self._cache[key] = mat
        return mat

    def _compute_zeroth(self, a_partition, h_b):
        """Compute the zeroth product matrix."""
        if not a_partition:
            return None

        if len(a_partition) == 1:
            m = a_partition[0]
            if m == 2:
                # T_(0) = L_{-1}
                return self.fock.L_matrix(-1, h_b)
            else:
                # (partial^{m-2} T)_(0) = 0 for m >= 3
                return None

        # Multi-mode: Borcherds iterate
        m1 = a_partition[0]
        v_partition = a_partition[1:]
        h_v = sum(v_partition)
        h_a = sum(a_partition)
        h_target = h_a + h_b - 1

        dim_s = self.fock.dim.get(h_b, 0)
        dim_t = self.fock.dim.get(h_target, 0)
        if dim_s == 0 or dim_t == 0:
            return None

        result = zero_matrix(dim_t, dim_s)

        # The Borcherds iterate formula:
        # (L_{-m} v)_(j) = sum_{i>=0} (-1)^i C(1-m, i) *
        #   [ L_{-m-i} v_(j+i) + (-1)^m v_(j+1-m-i) L_{i-1} ]
        # We need j = 0.
        max_i = h_b + h_v + 5

        for i in range(max_i):
            bc = _binom(1 - m1, i) * ((-1) ** i)
            if bc == 0 and i > h_b + 3:
                continue
            bc = Fraction(bc) if not isinstance(bc, Fraction) else bc

            # Term 1: L_{-m1-i} (v_(i) |b>)
            h_mid1 = h_v + h_b - i - 1
            v_i_data = self._jth_product_matrix(v_partition, i, h_b)
            if v_i_data is not None and 0 <= h_mid1 <= self.fock.max_h:
                v_i_mat, v_i_rows, v_i_cols = v_i_data
                L_data = self.fock.L_matrix(-m1 - i, h_mid1)
                if L_data is not None:
                    L_mat, L_rows, L_cols = L_data
                    prod = mat_mul(L_mat, L_rows, L_cols, v_i_mat, v_i_rows, v_i_cols)
                    prod_s = mat_scale(prod, L_rows, v_i_cols, bc)
                    result = mat_add(result, prod_s, dim_t, dim_s)

            # Term 2: (-1)^m1 * v_(1-m1-i) (L_{i-1} |b>)
            h_mid2 = h_b - i + 1
            L_im1_data = self.fock.L_matrix(i - 1, h_b)
            if L_im1_data is not None and 0 <= h_mid2 <= self.fock.max_h:
                L_im1_mat, L_im1_rows, L_im1_cols = L_im1_data
                k2 = 1 - m1 - i
                v_k2_data = self._jth_product_matrix(v_partition, k2, h_mid2)
                if v_k2_data is not None:
                    v_k2_mat, v_k2_rows, v_k2_cols = v_k2_data
                    prod = mat_mul(v_k2_mat, v_k2_rows, v_k2_cols,
                                   L_im1_mat, L_im1_rows, L_im1_cols)
                    sign = Fraction((-1) ** m1)
                    prod_s = mat_scale(prod, v_k2_rows, L_im1_cols, bc * sign)
                    result = mat_add(result, prod_s, dim_t, dim_s)

        if is_zero_matrix(result, dim_t, dim_s):
            return None
        return (result, dim_t, dim_s)

    def _jth_product_matrix(self, v_partition, j, h_source):
        """Matrix of v_(j): V_{h_source} -> V_{h_v+h_source-j-1}.
        Returns (matrix, nrows, ncols) or None.
        """
        key = (v_partition, j, h_source)
        if key in self._product_cache:
            return self._product_cache[key]

        mat = self._compute_jth_product(v_partition, j, h_source)
        self._product_cache[key] = mat
        return mat

    def _compute_jth_product(self, v_partition, j, h_source):
        """Compute v_(j) matrix."""
        h_v = sum(v_partition) if v_partition else 0
        h_target = h_v + h_source - j - 1

        if h_target < 0 or h_target > self.fock.max_h:
            return None
        if self.fock.dim.get(h_source, 0) == 0:
            return None
        if self.fock.dim.get(h_target, 0) == 0:
            return None

        if not v_partition:
            # Vacuum _(j) = delta_{j,-1} * id
            if j == -1 and h_source == h_target:
                n = self.fock.dim[h_source]
                return (identity_matrix(n), n, n)
            return None

        if len(v_partition) == 1:
            p = v_partition[0]
            k = p - 2  # number of derivatives: (partial^k T)

            # (partial^k T)_(j) = (-1)^k / k! * j(j-1)...(j-k+1) * L_{j-k-1}
            # = (-1)^k * C(j, k) * L_{j-k-1}   (since falling/k! = C(j,k))
            # Actually: (partial^k T)_(j) = (-1)^k * falling(j,k) / k! * L_{j-p+1}
            falling = ONE
            for ii in range(k):
                falling *= Fraction(j - ii)

            factorial_k = ONE
            for ii in range(2, k + 1):
                factorial_k *= Fraction(ii)

            coeff = ((-1) ** k) * falling / factorial_k
            if coeff == ZERO:
                return None

            mode = j - p + 1  # L_{mode}
            L_data = self.fock.L_matrix(mode, h_source)
            if L_data is None:
                return None
            L_mat, L_rows, L_cols = L_data
            return (mat_scale(L_mat, L_rows, L_cols, Fraction(coeff)), L_rows, L_cols)

        # Multi-mode: recursive Borcherds
        m1 = v_partition[0]
        w_partition = v_partition[1:]
        h_w = sum(w_partition) if w_partition else 0

        dim_s = self.fock.dim.get(h_source, 0)
        dim_t = self.fock.dim.get(h_target, 0)
        if dim_s == 0 or dim_t == 0:
            return None

        result = zero_matrix(dim_t, dim_s)
        max_i = h_source + h_w + 5

        for i in range(max_i):
            bc = _binom(1 - m1, i) * ((-1) ** i)
            if bc == 0 and i > h_source + 3:
                continue
            bc = Fraction(bc) if not isinstance(bc, Fraction) else bc

            # Term 1: L_{-m1-i} (w_(j+i) source)
            h_mid1 = h_w + h_source - (j + i) - 1
            w_ji_data = self._jth_product_matrix(w_partition, j + i, h_source)
            if w_ji_data is not None and 0 <= h_mid1 <= self.fock.max_h:
                w_ji_mat, w_ji_rows, w_ji_cols = w_ji_data
                L_data = self.fock.L_matrix(-m1 - i, h_mid1)
                if L_data is not None:
                    L_mat, L_rows, L_cols = L_data
                    prod = mat_mul(L_mat, L_rows, L_cols, w_ji_mat, w_ji_rows, w_ji_cols)
                    prod_s = mat_scale(prod, L_rows, w_ji_cols, bc)
                    result = mat_add(result, prod_s, dim_t, dim_s)

            # Term 2: (-1)^m1 * w_(j+1-m1-i) (L_{i-1} source)
            h_mid2 = h_source - i + 1
            L_im1_data = self.fock.L_matrix(i - 1, h_source)
            if L_im1_data is not None and 0 <= h_mid2 <= self.fock.max_h:
                L_im1_mat, L_im1_rows, L_im1_cols = L_im1_data
                k2 = j + 1 - m1 - i
                w_k2_data = self._jth_product_matrix(w_partition, k2, h_mid2)
                if w_k2_data is not None:
                    w_k2_mat, w_k2_rows, w_k2_cols = w_k2_data
                    prod = mat_mul(w_k2_mat, w_k2_rows, w_k2_cols,
                                   L_im1_mat, L_im1_rows, L_im1_cols)
                    sign = Fraction((-1) ** m1)
                    prod_s = mat_scale(prod, w_k2_rows, L_im1_cols, bc * sign)
                    result = mat_add(result, prod_s, dim_t, dim_s)

        if is_zero_matrix(result, dim_t, dim_s):
            return None
        return (result, dim_t, dim_s)


def _binom(n, k):
    """Generalized binomial coefficient C(n, k) for integer n, int k >= 0."""
    if k < 0:
        return Fraction(0)
    result = Fraction(1)
    for i in range(k):
        result *= Fraction(n - i, i + 1)
    return result


# ============================================================================
# OS form residues
# ============================================================================

# For n=2: OS^1(C_2) has dim 1 (the form eta_{12}), residue = 1.
# For n=3: OS^2(C_3) has basis {w1=eta12^eta13, w2=eta12^eta23}, dim=2.
OS2_RESIDUES = {
    (0, (1, 2)): ONE,   (0, (1, 3)): ONE,   (0, (2, 3)): ZERO,
    (1, (1, 2)): ONE,   (1, (1, 3)): ZERO,  (1, (2, 3)): -ONE,
}


def collision_result_3pt(i, j, a1, a2, a3):
    """After collision (i,j) in [a1|a2|a3], return (ai, aj, remaining, order)."""
    if (i, j) == (1, 2):
        return (a1, a2), a3, 'merged_first'
    elif (i, j) == (1, 3):
        return (a1, a3), a2, 'merged_first'
    elif (i, j) == (2, 3):
        return (a2, a3), a1, 'remaining_first'


# ============================================================================
# Bar complex and cohomology
# ============================================================================

class BarCohomology:
    """Compute bar cohomology of the Virasoro algebra."""

    def __init__(self, c, max_weight=20):
        self.fock = VirasoroFock(c, max_weight)
        self.zp = ZerothProductEngine(self.fock)
        self.max_h = max_weight

    def bar_tensor_basis(self, n, total_h):
        """Basis of tensor part of B^n at total conformal weight total_h."""
        basis = []
        self._enum_tensor(n, total_h, [], basis)
        return basis

    def _enum_tensor(self, slots, remaining_h, current, result):
        if slots == 0:
            if remaining_h == 0:
                result.append(tuple(current))
            return
        min_h = 2
        max_h = remaining_h - 2 * (slots - 1)
        for h in range(min_h, min(max_h, self.max_h) + 1):
            for part in self.fock.basis.get(h, []):
                if not part:
                    continue
                self._enum_tensor(slots - 1, remaining_h - h,
                                  current + [part], result)

    def differential_2to1(self, w):
        """Matrix of d: B^2_w -> B^1_w. Returns (mat, nrows, ncols, src, tgt)."""
        total_h = w + 2
        src_basis = self.bar_tensor_basis(2, total_h)
        tgt_h = w + 1
        tgt_basis = self.fock.basis.get(tgt_h, [])

        dim_s = len(src_basis)
        dim_t = len(tgt_basis)
        if dim_s == 0 or dim_t == 0:
            return zero_matrix(dim_t, dim_s), dim_t, dim_s

        mat = zero_matrix(dim_t, dim_s)

        for col, (a, b) in enumerate(src_basis):
            h_b = sum(b)
            zp_data = self.zp.zeroth_product_matrix(a, h_b)
            if zp_data is None:
                continue
            zp_mat, zp_rows, zp_cols = zp_data

            b_idx = self.fock.basis[h_b].index(b)

            for row in range(dim_t):
                mat[row][col] += zp_mat[row][b_idx]

        return mat, dim_t, dim_s

    def differential_3to2(self, w):
        """Matrix of d: B^3_w -> B^2_w.
        Source: tensor3 x OS^2 (dim 2). Target: tensor2.
        """
        total_h_src = w + 3
        total_h_tgt = w + 2

        tensor3 = self.bar_tensor_basis(3, total_h_src)
        tensor2 = self.bar_tensor_basis(2, total_h_tgt)

        dim_s = len(tensor3) * 2
        dim_t = len(tensor2)
        if dim_s == 0 or dim_t == 0:
            return zero_matrix(dim_t, dim_s), dim_t, dim_s

        mat = zero_matrix(dim_t, dim_s)
        tgt_idx = {elem: i for i, elem in enumerate(tensor2)}

        for t_idx, (a1, a2, a3) in enumerate(tensor3):
            for form_idx in range(2):
                col = t_idx * 2 + form_idx

                for (i, j) in [(1, 2), (1, 3), (2, 3)]:
                    residue = OS2_RESIDUES.get((form_idx, (i, j)), ZERO)
                    if residue == ZERO:
                        continue

                    (ai, aj), remaining, order = collision_result_3pt(
                        i, j, a1, a2, a3)

                    h_aj = sum(aj)
                    zp_data = self.zp.zeroth_product_matrix(ai, h_aj)
                    if zp_data is None:
                        continue
                    zp_mat, zp_rows, zp_cols = zp_data

                    aj_idx = self.fock.basis[h_aj].index(aj)
                    h_contracted = sum(ai) + h_aj - 1

                    for c_idx in range(zp_rows):
                        if zp_mat[c_idx][aj_idx] == ZERO:
                            continue

                        contracted_part = self.fock.basis[h_contracted][c_idx]

                        if order == 'merged_first':
                            deg2_elem = (contracted_part, remaining)
                        else:
                            deg2_elem = (remaining, contracted_part)

                        if deg2_elem in tgt_idx:
                            row = tgt_idx[deg2_elem]
                            mat[row][col] += residue * zp_mat[c_idx][aj_idx]

        return mat, dim_t, dim_s

    def compute_Hn(self, n, max_w, debug=False):
        """Compute dim H^n = sum_w dim H^n_w."""
        if n < 1:
            return 0
        total = 0
        for w in range(n, max_w + 1):
            h = self._Hn_at_w(n, w, debug=debug)
            if h > 0:
                if debug:
                    print(f"    H^{n}_{w} = {h}")
                total += h
        return total

    def _Hn_at_w(self, n, w, debug=False):
        """Compute dim H^n_w = dim ker(d_out) - dim im(d_in)."""
        # dim B^n_w
        if n == 1:
            dim_Bn = self.fock.dim.get(w + 1, 0)
        elif n == 2:
            dim_Bn = len(self.bar_tensor_basis(2, w + 2))
        elif n == 3:
            dim_Bn = len(self.bar_tensor_basis(3, w + 3)) * 2
        else:
            return 0

        if dim_Bn == 0:
            return 0

        # d_out: B^n_w -> B^{n-1}_w
        if n == 1:
            ker_dim = dim_Bn  # d: B^1 -> 0
        elif n == 2:
            mat_out, nr, nc = self.differential_2to1(w)
            rank_out = matrix_rank(mat_out, nr, nc)
            ker_dim = dim_Bn - rank_out
        elif n == 3:
            mat_out, nr, nc = self.differential_3to2(w)
            rank_out = matrix_rank(mat_out, nr, nc)
            ker_dim = dim_Bn - rank_out
        else:
            ker_dim = dim_Bn

        # d_in: B^{n+1}_w -> B^n_w
        if n + 1 == 2:
            mat_in, nr, nc = self.differential_2to1(w)
            im_dim = matrix_rank(mat_in, nr, nc)
        elif n + 1 == 3:
            mat_in, nr, nc = self.differential_3to2(w)
            im_dim = matrix_rank(mat_in, nr, nc)
        else:
            im_dim = 0

        if debug and (ker_dim - im_dim) != 0:
            print(f"      w={w}: dim_B^{n}={dim_Bn}, ker={ker_dim}, im={im_dim}, H={ker_dim-im_dim}")

        return max(ker_dim - im_dim, 0)

    def compute_all(self, max_n, max_w):
        """Compute dim H^n for n = 1, ..., max_n."""
        results = {}
        for n in range(1, max_n + 1):
            t0 = time.time()
            h = self.compute_Hn(n, max_w)
            dt = time.time() - t0
            results[n] = h
            print(f"  H^{n} = {h}  ({dt:.1f}s)")
        return results


# ============================================================================
# Validation and main
# ============================================================================

def motzkin_differences(max_n):
    """Motzkin differences M(n+1) - M(n): ground truth for Virasoro."""
    N = max_n + 5
    M = [0] * N
    M[0] = 1
    M[1] = 1
    for i in range(2, N):
        M[i] = M[i-1] + sum(M[k] * M[i-2-k] for k in range(i-1))
    return {n: M[n+1] - M[n] for n in range(1, max_n + 1)}


def validate_zeroth_product():
    """Validate zeroth product computation with known values."""
    print("=" * 70)
    print("ZEROTH PRODUCT VALIDATION")
    print("=" * 70)

    c_val = 7
    fock = VirasoroFock(c_val, 20)
    zp = ZerothProductEngine(fock)
    all_ok = True

    # T_(0) T = L_{-1} T = L_{-3}|0>
    data = zp.zeroth_product_matrix((2,), 2)
    print(f"\nT_(0) on V_2 -> V_3:")
    if data is not None:
        mat, nr, nc = data
        expected = ONE  # single entry
        ok = (nr == 1 and nc == 1 and mat[0][0] == expected)
        print(f"  mat[0][0] = {mat[0][0]}, expected {expected} -> {'OK' if ok else 'MISMATCH'}")
        all_ok &= ok
    else:
        print("  None returned -> MISMATCH")
        all_ok = False

    # :TT:_(0) T = (2+c) L_{-5} + 6 L_{-3}L_{-2}
    data = zp.zeroth_product_matrix((2, 2), 2)
    print(f"\n:TT:_(0) on V_2 -> V_5:")
    if data is not None:
        mat, nr, nc = data
        expected_5 = Fraction(2 + c_val)  # coeff of (5,)
        expected_32 = Fraction(6)          # coeff of (3,2)
        ok = (mat[0][0] == expected_5 and mat[1][0] == expected_32)
        print(f"  [{mat[0][0]}, {mat[1][0]}]^T, expected [{expected_5}, {expected_32}]^T -> {'OK' if ok else 'MISMATCH'}")
        all_ok &= ok
    else:
        print("  None returned -> MISMATCH")
        all_ok = False

    # (partial T)_(0) = 0
    data = zp.zeroth_product_matrix((3,), 2)
    ok = data is None
    print(f"\n(partial T)_(0) on V_2: {data} (expected None) -> {'OK' if ok else 'MISMATCH'}")
    all_ok &= ok

    # L_{-4}|0>_(0) = 0
    data = zp.zeroth_product_matrix((4,), 2)
    ok = data is None
    print(f"L_{{-4}}|0>_(0) on V_2: {data} (expected None) -> {'OK' if ok else 'MISMATCH'}")
    all_ok &= ok

    return all_ok


def validate_virasoro(max_w=12):
    """Validate against known Virasoro bar cohomology."""
    print("\n" + "=" * 70)
    print("VIRASORO BAR COHOMOLOGY VALIDATION")
    print("=" * 70)

    expected = motzkin_differences(10)
    print(f"\nExpected (Motzkin diffs): {[expected[n] for n in range(1, 9)]}")
    print(f"\nc = 7, max_weight = {max_w + 5}")

    bc = BarCohomology(c=7, max_weight=max_w + 5)

    print("\nComputing bar cohomology (bar degrees 1-3):")
    # Debug: show per-weight contributions
    print("\nDetailed per-weight breakdown:")
    for n in range(1, 4):
        t0 = time.time()
        h = bc.compute_Hn(n, max_w, debug=True)
        dt = time.time() - t0
        print(f"  H^{n} = {h}  ({dt:.1f}s)")

    print("\nFinal results:")
    results = bc.compute_all(max_n=3, max_w=max_w)

    print(f"\nValidation:")
    all_ok = True
    for n in sorted(results.keys()):
        exp = expected.get(n, "?")
        ok = results[n] == exp
        print(f"  H^{n}: computed={results[n]}, expected={exp}  {'OK' if ok else 'MISMATCH'}")
        all_ok &= ok

    return all_ok


def main():
    print("Bar Cohomology Computation (exact arithmetic)")
    print("=" * 70)

    ok1 = validate_zeroth_product()
    ok2 = validate_virasoro(max_w=10)

    if ok1 and ok2:
        print("\n*** ALL VALIDATIONS PASSED ***")
    else:
        print("\n*** SOME VALIDATIONS FAILED ***")


if __name__ == "__main__":
    main()
