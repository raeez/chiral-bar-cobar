#!/usr/bin/env python3
"""Compute bar cohomology of Virasoro and W_3 algebras via mode algebra.

Strategy:
  1. Represent the Virasoro (or W_3) vacuum module truncated at weight max_h
  2. Precompute mode matrices L_n: V_h -> V_{h-n} (and W_n for W_3)
  3. Build zeroth product operators a_(0): V_{h_b} -> V_{h_a+h_b-1}
  4. Assemble bar differential d: B^{n+1}_w -> B^n_w with OS form factors
  5. Compute cohomology = ker(d_out)/im(d_in) at each (n, w)
  6. Sum over w to get total dim H^n

Validates against known Virasoro values (Motzkin differences):
  1, 2, 5, 12, 30, 76, 196, 512, ...

Then computes W_3 bar cohomology (known: 2, 5, 16, 52).

Author: Raeez Lorgat
"""

import numpy as np
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
import sys
import time


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
    if weight < 0:
        return [()]  if weight == 0 else []
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
    # Split weight into L-part and W-part
    for w_part in range(0, weight + 1):
        l_part = weight - w_part
        for l_partition in partitions_geq(l_part, 2):
            for w_partition in partitions_geq(w_part, 3):
                basis.append((l_partition, w_partition))
    # Remove the vacuum (0, 0) if weight > 0, keep if weight == 0
    if weight == 0:
        return [((), ())]
    return [(l, w) for l, w in basis if l or w]


# ============================================================================
# Virasoro mode algebra (numerical, float64)
# ============================================================================

class VirasoroFock:
    """Truncated Virasoro vacuum module with numerical mode matrices.

    Stores PBW bases at each weight and precomputes L_n matrices.
    """

    def __init__(self, c, max_weight):
        self.c = float(c)
        self.max_h = max_weight

        # PBW bases at each weight
        self.basis = {}
        self.basis_index = {}  # partition -> (weight, index)
        for h in range(0, max_weight + 1):
            if h == 0:
                b = [()]
            elif h == 1:
                b = []
            else:
                b = vir_pbw_basis(h)
            self.basis[h] = b
            for i, part in enumerate(b):
                self.basis_index[part] = (h, i)

        self.dim = {h: len(b) for h, b in self.basis.items()}

        # Cache for L_n matrices
        self._L_cache = {}

    def L_matrix(self, n, h_source):
        """Matrix of L_n: V_{h_source} -> V_{h_source - n}.

        Returns numpy array of shape (dim_target, dim_source), or None if
        target weight is out of range.
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
        mat = np.zeros((dim_t, dim_s))

        tgt_index = {p: i for i, p in enumerate(tgt_basis)}

        for col, partition in enumerate(src_basis):
            # Compute L_n applied to this PBW state
            result = self._L_on_pbw(n, partition)
            for part, coeff in result.items():
                if part in tgt_index:
                    mat[tgt_index[part], col] += coeff

        self._L_cache[key] = mat
        return mat

    def _L_on_pbw(self, n, partition):
        """Apply L_n to PBW state. Returns dict {partition: float_coeff}."""
        if not partition:
            # L_n |0> = 0 for n >= -1
            if n >= -1:
                return {}
            else:
                return {(-n,): 1.0}

        if n <= -2:
            return self._insert_mode(-n, partition)

        # Annihilation: commute L_n through from left
        m1 = partition[0]
        rest = partition[1:]
        result = {}

        # [L_n, L_{-m1}] = (n+m1) L_{n-m1}
        comm = n + m1
        new_n = n - m1  # mode index of commutator result

        if comm != 0:
            if new_n <= -2:
                inner = self._insert_mode(-new_n, rest)
            else:
                inner = self._L_on_pbw(new_n, rest)
            for p, c in inner.items():
                result[p] = result.get(p, 0.0) + comm * c

        # Central term: (c/12) n(n^2-1) delta_{n, m1}
        if n == m1 and n >= 2:
            central = self.c / 12.0 * n * (n * n - 1)
            if abs(central) > 1e-15:
                rest_key = rest if rest else ()
                result[rest_key] = result.get(rest_key, 0.0) + central

        # Pass-through: L_{-m1} (L_n on rest)
        inner = self._L_on_pbw(n, rest)
        for p, c in inner.items():
            new_p = self._prepend(m1, p)
            result[new_p] = result.get(new_p, 0.0) + c

        return {k: v for k, v in result.items() if abs(v) > 1e-15}

    def _insert_mode(self, m, partition):
        """Insert L_{-m} before L_{-p1}...L_{-pk}|0>, reorder to PBW."""
        if not partition:
            return {(m,): 1.0}

        p1 = partition[0]
        if m >= p1:
            return {(m,) + partition: 1.0}

        rest = partition[1:]
        result = {}

        # L_{-m} L_{-p1} = L_{-p1} L_{-m} + (p1-m) L_{-(m+p1)}
        # Term 1: push L_{-m} past L_{-p1}
        inner1 = self._insert_mode(m, rest)
        for p, c in inner1.items():
            new_p = (p1,) + p
            result[new_p] = result.get(new_p, 0.0) + c

        # Term 2: commutator (p1-m) L_{-(m+p1)}
        inner2 = self._insert_mode(m + p1, rest)
        coeff = float(p1 - m)
        for p, c in inner2.items():
            result[p] = result.get(p, 0.0) + coeff * c

        return {k: v for k, v in result.items() if abs(v) > 1e-15}

    def _prepend(self, m, partition):
        """Prepend m to partition (assumes m >= partition[0])."""
        if not partition or m >= partition[0]:
            return (m,) + partition
        # Need to insert properly
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

    Uses the recursive formula:
    - T_(0) = L_{-1}
    - (L_{-m} v)_(0) = sum_j f(j) [L_{-m-j} v_(j) + (-1)^m v_(1-m-j) L_{j-1}]

    where f(j) = (-1)^j C(1-m, j) and v_(j) is the j-th product mode.
    """

    def __init__(self, fock):
        self.fock = fock
        self._cache = {}  # (a_partition, h_b) -> matrix
        self._product_cache = {}  # (partition, j, h) -> matrix

    def zeroth_product_matrix(self, a_partition, h_b):
        """Matrix of a_(0): V_{h_b} -> V_{h_a+h_b-1}.

        Returns numpy matrix or None if out of range.
        """
        h_a = sum(a_partition)
        h_target = h_a + h_b - 1

        if h_target < 0 or h_target > self.fock.max_h:
            return None
        if h_b not in self.fock.dim or self.fock.dim.get(h_b, 0) == 0:
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
            # Vacuum: zero zeroth product
            return None

        if len(a_partition) == 1:
            m = a_partition[0]
            if m == 2:
                # T_(0) = L_{-1}
                return self.fock.L_matrix(-1, h_b)
            else:
                # Single mode L_{-m}|0> for m >= 3: zeroth product = 0
                return None

        # Multi-mode: use (L_{-m1} v)_(0) = sum_j [terms]
        m1 = a_partition[0]
        v_partition = a_partition[1:]
        h_v = sum(v_partition)
        h_a = sum(a_partition)
        h_target = h_a + h_b - 1

        dim_s = self.fock.dim.get(h_b, 0)
        dim_t = self.fock.dim.get(h_target, 0)
        if dim_s == 0 or dim_t == 0:
            return None

        result = np.zeros((dim_t, dim_s))

        max_j = h_b + h_v + 5

        for j in range(max_j):
            binom_coeff = self._binom(1 - m1, j) * ((-1) ** j)
            if abs(binom_coeff) < 1e-15 and j > h_b + 3:
                continue

            # Term 1: L_{-m1-j} (v_(j) |b>)
            # v_(j): V_{h_b} -> V_{h_v + h_b - j - 1}
            h_mid1 = h_v + h_b - j - 1
            v_j_mat = self._jth_product_matrix(v_partition, j, h_b)
            if v_j_mat is not None and h_mid1 >= 0:
                # L_{-m1-j}: V_{h_mid1} -> V_{h_mid1 + m1 + j} = V_{h_target}
                L_mat = self.fock.L_matrix(-m1 - j, h_mid1)
                if L_mat is not None:
                    result += binom_coeff * (L_mat @ v_j_mat)

            # Term 2: (-1)^m1 * v_(1-m1-j) (L_{j-1} |b>)
            # L_{j-1}: V_{h_b} -> V_{h_b - j + 1}
            h_mid2 = h_b - j + 1
            L_jm1 = self.fock.L_matrix(j - 1, h_b)
            if L_jm1 is not None and h_mid2 >= 0:
                k2 = 1 - m1 - j
                v_k2_mat = self._jth_product_matrix(v_partition, k2, h_mid2)
                if v_k2_mat is not None:
                    result += binom_coeff * ((-1) ** m1) * (v_k2_mat @ L_jm1)

        if np.max(np.abs(result)) < 1e-12:
            return None
        return result

    def _jth_product_matrix(self, v_partition, j, h_target_input):
        """Matrix of v_(j): V_{h_target_input} -> V_{h_v + h_target_input - j - 1}.

        For single mode L_{-p}|0>:
          v_(j) = (1/(p-2)!) * (-1)^{p-2} * falling(j, p-2) * L_{j-p+1}

        For vacuum: v_(j) = delta_{j,-1} * id
        """
        key = (v_partition, j, h_target_input)
        if key in self._product_cache:
            return self._product_cache[key]

        mat = self._compute_jth_product(v_partition, j, h_target_input)
        self._product_cache[key] = mat
        return mat

    def _compute_jth_product(self, v_partition, j, h_source):
        """Compute matrix of v_(j): V_{h_source} -> V_{...}."""
        h_v = sum(v_partition) if v_partition else 0
        h_target = h_v + h_source - j - 1

        if h_target < 0 or h_target > self.fock.max_h:
            return None
        if self.fock.dim.get(h_source, 0) == 0:
            return None
        if self.fock.dim.get(h_target, 0) == 0:
            return None

        if not v_partition:
            # Vacuum: v_(j) = delta_{j,-1} * id
            if j == -1 and h_source == h_target:
                return np.eye(self.fock.dim[h_source])
            return None

        if len(v_partition) == 1:
            p = v_partition[0]
            k = p - 2  # number of derivatives

            # v_(j) = ((-1)^k / k!) * j*(j-1)*...*(j-k+1) * L_{j-p+1}
            falling = 1.0
            for i in range(k):
                falling *= (j - i)

            factorial_k = 1
            for i in range(2, k + 1):
                factorial_k *= i

            coeff = ((-1) ** k) * falling / factorial_k
            if abs(coeff) < 1e-15:
                return None

            mode = j - p + 1  # L_{j-p+1}
            L_mat = self.fock.L_matrix(mode, h_source)
            if L_mat is None:
                return None
            return coeff * L_mat

        # Multi-mode: recursive via Borcherds
        m1 = v_partition[0]
        w_partition = v_partition[1:]
        h_w = sum(w_partition) if w_partition else 0

        dim_s = self.fock.dim.get(h_source, 0)
        dim_t = self.fock.dim.get(h_target, 0)
        if dim_s == 0 or dim_t == 0:
            return None

        result = np.zeros((dim_t, dim_s))
        max_i = h_source + h_w + 5

        for i in range(max_i):
            bc = self._binom(1 - m1, i) * ((-1) ** i)
            if abs(bc) < 1e-15 and i > h_source + 3:
                continue

            # Term 1: L_{-m1-i} (w_(j+i) target)
            h_mid1 = h_w + h_source - (j + i) - 1
            w_ji = self._jth_product_matrix(w_partition, j + i, h_source)
            if w_ji is not None and 0 <= h_mid1 <= self.fock.max_h:
                L_mat = self.fock.L_matrix(-m1 - i, h_mid1)
                if L_mat is not None:
                    result += bc * (L_mat @ w_ji)

            # Term 2: (-1)^m1 * w_(1-m1+j-i) (L_{i-1} target)
            h_mid2 = h_source - i + 1
            L_im1 = self.fock.L_matrix(i - 1, h_source)
            if L_im1 is not None and 0 <= h_mid2 <= self.fock.max_h:
                k2 = 1 - m1 + j - i
                w_k2 = self._jth_product_matrix(w_partition, k2, h_mid2)
                if w_k2 is not None:
                    result += bc * ((-1) ** m1) * (w_k2 @ L_im1)

        if np.max(np.abs(result)) < 1e-12:
            return None
        return result

    def _binom(self, n, k):
        """Generalized binomial coefficient C(n, k) for real n, int k >= 0."""
        if k < 0:
            return 0.0
        result = 1.0
        for i in range(k):
            result *= (n - i) / (i + 1)
        return result


# ============================================================================
# OS form residues
# ============================================================================

# Form residue tables for the bar complex.
# OS^{n-1}(C_n) has dim (n-1)!
# The residue R_{ij}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1}) is a linear map.

# For n=3: OS^2(C_3) has basis {w1=eta12^eta13, w2=eta12^eta23}, dim=2.
# Residues:
#   R_12(w1)=+1, R_12(w2)=+1
#   R_13(w1)=+1, R_13(w2)=0
#   R_23(w1)=0,  R_23(w2)=-1

OS2_RESIDUES = {
    # (form_idx, (i,j)): coefficient
    (0, (1, 2)): 1.0,
    (0, (1, 3)): 1.0,
    (0, (2, 3)): 0.0,
    (1, (1, 2)): 1.0,
    (1, (1, 3)): 0.0,
    (1, (2, 3)): -1.0,
}

# After collision (i,j), the ordering of the result in degree n-1:
# (1,2): merged -> pos 1, remaining -> pos 2 (for 3-pt)
# (1,3): merged -> pos 1, remaining=z2 -> pos 2
# (2,3): remaining=z1 -> pos 1, merged -> pos 2

def collision_result_3pt(i, j, a1, a2, a3):
    """After collision (i,j) in a 3-point bar element [a1|a2|a3],
    return (contracted_pair, remaining, order).

    contracted_pair = (a_i, a_j) to apply zeroth product
    remaining = the spectator
    order: 'merged_first' or 'remaining_first' in the degree-2 result
    """
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
        """Enumerate basis of the tensor part of B^n at total conformal weight total_h.

        Each element is a tuple (a1, a2, ..., an) of PBW partitions with
        sum(a_i weights) = total_h.
        """
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
        """Matrix of d: B^2_w -> B^1_w.

        d([a|b]) = a_(0) b.
        Shifted weight w: h_a + h_b - 2 = w, so total_h = w + 2.
        Target: B^1_w = V_{w+1}.
        """
        total_h = w + 2
        src_basis = self.bar_tensor_basis(2, total_h)
        tgt_h = w + 1
        tgt_basis = self.fock.basis.get(tgt_h, [])

        if not src_basis or not tgt_basis:
            return np.zeros((len(tgt_basis), len(src_basis))), src_basis, tgt_basis

        dim_t = len(tgt_basis)
        dim_s = len(src_basis)
        mat = np.zeros((dim_t, dim_s))

        tgt_idx = {p: i for i, p in enumerate(tgt_basis)}

        for col, (a, b) in enumerate(src_basis):
            h_b = sum(b)
            zp_mat = self.zp.zeroth_product_matrix(a, h_b)
            if zp_mat is None:
                continue

            # b is a PBW state in V_{h_b}: find its index
            b_idx = None
            for ii, bp in enumerate(self.fock.basis[h_b]):
                if bp == b:
                    b_idx = ii
                    break
            if b_idx is None:
                continue

            # a_(0)b is the b_idx-th column of zp_mat
            result_vec = zp_mat[:, b_idx]

            # Map to target basis
            for row in range(dim_t):
                mat[row, col] += result_vec[row]

        return mat, src_basis, tgt_basis

    def differential_3to2(self, w):
        """Matrix of d: B^3_w -> B^2_w.

        B^3_w includes OS^2 factor (dim 2).
        Source basis: tensor_basis_3 x {0, 1} (form index).
        Target basis: tensor_basis_2 (OS^1 is 1-dim).

        d([a1|a2|a3] x omega_k) = sum_{i<j} R_{ij}(omega_k) * [contracted | remaining]
        """
        total_h_src = w + 3
        total_h_tgt = w + 2

        tensor3 = self.bar_tensor_basis(3, total_h_src)
        tensor2 = self.bar_tensor_basis(2, total_h_tgt)

        if not tensor3 or not tensor2:
            n_s = len(tensor3) * 2
            n_t = len(tensor2)
            return np.zeros((n_t, n_s)), tensor3, tensor2

        # Source: each tensor3 element x 2 OS forms = len(tensor3) * 2
        # Target: tensor2 elements
        dim_s = len(tensor3) * 2
        dim_t = len(tensor2)
        mat = np.zeros((dim_t, dim_s))

        tgt_idx = {elem: i for i, elem in enumerate(tensor2)}

        for t_idx, (a1, a2, a3) in enumerate(tensor3):
            for form_idx in range(2):
                col = t_idx * 2 + form_idx

                for (i, j) in [(1, 2), (1, 3), (2, 3)]:
                    residue = OS2_RESIDUES.get((form_idx, (i, j)), 0.0)
                    if abs(residue) < 1e-15:
                        continue

                    (ai, aj), remaining, order = collision_result_3pt(
                        i, j, a1, a2, a3)

                    # Compute ai_(0) aj
                    h_aj = sum(aj)
                    zp_mat = self.zp.zeroth_product_matrix(ai, h_aj)
                    if zp_mat is None:
                        continue

                    aj_idx = None
                    for ii, bp in enumerate(self.fock.basis[h_aj]):
                        if bp == aj:
                            aj_idx = ii
                            break
                    if aj_idx is None:
                        continue

                    contracted_vec = zp_mat[:, aj_idx]
                    h_contracted = sum(ai) + h_aj - 1

                    # Build degree-2 elements from contracted + remaining
                    for c_idx in range(len(contracted_vec)):
                        if abs(contracted_vec[c_idx]) < 1e-15:
                            continue

                        contracted_part = self.fock.basis[h_contracted][c_idx]

                        if order == 'merged_first':
                            deg2_elem = (contracted_part, remaining)
                        else:
                            deg2_elem = (remaining, contracted_part)

                        if deg2_elem in tgt_idx:
                            row = tgt_idx[deg2_elem]
                            mat[row, col] += residue * contracted_vec[c_idx]

        return mat, tensor3, tensor2

    def compute_H1(self, max_w):
        """Compute dim H^1 = sum_w dim H^1_w.

        H^1_w = B^1_w / im(d: B^2_w -> B^1_w)
        """
        total = 0
        for w in range(1, max_w + 1):
            tgt_h = w + 1
            dim_B1 = self.fock.dim.get(tgt_h, 0)
            if dim_B1 == 0:
                continue

            mat, _, _ = self.differential_2to1(w)
            if mat.size == 0:
                total += dim_B1
                continue

            rank = np.linalg.matrix_rank(mat, tol=1e-8)
            total += dim_B1 - rank

        return total

    def compute_Hn(self, n, max_w):
        """Compute dim H^n = sum_w dim H^n_w for n >= 1.

        H^n_w = ker(d_out: B^n_w -> B^{n-1}_w) / im(d_in: B^{n+1}_w -> B^n_w)
        """
        if n < 1:
            return 0

        total = 0
        for w in range(n, max_w + 1):
            dim_Hn_w = self._Hn_at_w(n, w)
            total += dim_Hn_w
        return total

    def _Hn_at_w(self, n, w):
        """Compute dim H^n_w = dim ker(d_out) - dim im(d_in)."""
        # d_out: B^n_w -> B^{n-1}_w
        # d_in:  B^{n+1}_w -> B^n_w

        total_h_n = w + n  # conformal weight at degree n

        # dim B^n_w (including OS forms for n >= 3)
        if n == 1:
            dim_Bn = self.fock.dim.get(w + 1, 0)
            os_factor = 1
        elif n == 2:
            tensor2 = self.bar_tensor_basis(2, w + 2)
            dim_Bn = len(tensor2)
            os_factor = 1  # OS^1 is 1-dim
        elif n == 3:
            tensor3 = self.bar_tensor_basis(3, w + 3)
            dim_Bn = len(tensor3) * 2  # OS^2 has dim 2
            os_factor = 2
        else:
            # For n >= 4, need to implement OS^{n-1}
            # For now, skip
            return 0

        if dim_Bn == 0:
            return 0

        # d_out: B^n_w -> B^{n-1}_w
        if n == 1:
            # d: B^1 -> B^0 = 0 (no bar degree 0 in augmentation)
            ker_dim = dim_Bn
        elif n == 2:
            mat_out, _, _ = self.differential_2to1(w)
            if mat_out.size == 0:
                ker_dim = dim_Bn
            else:
                ker_dim = dim_Bn - np.linalg.matrix_rank(mat_out, tol=1e-8)
        elif n == 3:
            mat_out, _, _ = self.differential_3to2(w)
            if mat_out.size == 0:
                ker_dim = dim_Bn
            else:
                ker_dim = dim_Bn - np.linalg.matrix_rank(mat_out, tol=1e-8)
        else:
            ker_dim = dim_Bn

        # d_in: B^{n+1}_w -> B^n_w
        if n + 1 == 2:
            mat_in, _, _ = self.differential_2to1(w)
            im_dim = np.linalg.matrix_rank(mat_in, tol=1e-8) if mat_in.size > 0 else 0
        elif n + 1 == 3:
            mat_in, _, _ = self.differential_3to2(w)
            im_dim = np.linalg.matrix_rank(mat_in, tol=1e-8) if mat_in.size > 0 else 0
        else:
            im_dim = 0

        h_n = ker_dim - im_dim
        return max(h_n, 0)

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
# Main: validation and computation
# ============================================================================

def motzkin_differences(max_n):
    """Motzkin differences M(n+1) - M(n) for n = 1, 2, ...

    Ground truth for Virasoro bar cohomology.
    """
    # Motzkin numbers: M(0)=1, M(1)=1, M(2)=2, M(3)=4, M(4)=9, ...
    N = max_n + 5
    M = [0] * N
    M[0] = 1
    M[1] = 1
    for i in range(2, N):
        M[i] = M[i-1] + sum(M[k] * M[i-2-k] for k in range(i-1))

    return {n: M[n+1] - M[n] for n in range(1, max_n + 1)}


def validate_virasoro():
    """Validate the computation against known Virasoro bar cohomology."""
    print("=" * 70)
    print("VIRASORO BAR COHOMOLOGY VALIDATION")
    print("=" * 70)

    expected = motzkin_differences(8)
    print(f"\nExpected (Motzkin differences): {[expected[n] for n in range(1, 9)]}")

    # First test: c = 7
    print("\n--- c = 7, max_weight = 25 ---")
    bc = BarCohomology(c=7, max_weight=25)

    # Compute H^1 first as a basic check
    print("\nComputing bar cohomology:")
    results = bc.compute_all(max_n=3, max_w=20)

    print(f"\nValidation:")
    for n in sorted(results.keys()):
        exp = expected.get(n, "?")
        ok = results[n] == exp
        print(f"  H^{n}: computed={results[n]}, expected={exp}  {'OK' if ok else 'MISMATCH'}")

    return results


def validate_zeroth_product():
    """Validate zeroth product computation with known values."""
    print("=" * 70)
    print("ZEROTH PRODUCT VALIDATION")
    print("=" * 70)

    c_val = 7.0
    fock = VirasoroFock(c_val, 20)
    zp = ZerothProductEngine(fock)

    # T_(0) T = L_{-1} T = partial T = L_{-3}|0>
    # In PBW at weight 3: [(3,)]
    mat = zp.zeroth_product_matrix((2,), 2)
    print(f"\nT_(0) acting on V_2 -> V_3:")
    if mat is not None:
        print(f"  Matrix shape: {mat.shape}")
        print(f"  Matrix:\n{mat}")
        # T is the only basis at weight 2, mapped to L_{-3}|0> at weight 3
        # But weight 3 basis is [(3,)] only
        expected = np.array([[1.0]])  # L_{-1} L_{-2}|0> = L_{-3}|0>
        ok = np.allclose(mat, expected)
        print(f"  Expected: {expected.flatten()} -> {'OK' if ok else 'MISMATCH'}")

    # :TT:_(0) T = (2+c) L_{-5} + 6 L_{-3}L_{-2}
    # Weight 4 basis: [(4,), (2,2)]
    # Weight 5 basis: [(5,), (3,2)]
    mat_tt = zp.zeroth_product_matrix((2, 2), 2)
    print(f"\n:TT:_(0) acting on V_2 -> V_5:")
    if mat_tt is not None:
        print(f"  Matrix shape: {mat_tt.shape}")
        print(f"  Matrix:\n{mat_tt}")
        # Expect: (2+c)*e_{(5,)} + 6*e_{(3,2)}
        expected_5 = 2 + c_val  # coefficient of L_{-5}|0>
        expected_32 = 6.0       # coefficient of L_{-3}L_{-2}|0>
        print(f"  Expected: [{expected_5}, {expected_32}]^T")
        ok = (abs(mat_tt[0, 0] - expected_5) < 1e-10 and
              abs(mat_tt[1, 0] - expected_32) < 1e-10)
        print(f"  -> {'OK' if ok else 'MISMATCH'}")
    else:
        print("  (None returned)")

    # (partial T)_(0) = 0 (derivative has zero zeroth product)
    mat_dt = zp.zeroth_product_matrix((3,), 2)
    print(f"\n(partial T)_(0) acting on V_2:")
    print(f"  {mat_dt}  (expected: None)")
    ok = mat_dt is None
    print(f"  -> {'OK' if ok else 'MISMATCH'}")

    # L_{-4}|0>_(0) = 0
    mat_4 = zp.zeroth_product_matrix((4,), 2)
    print(f"\nL_{{-4}}|0>_(0) acting on V_2:")
    print(f"  {mat_4}  (expected: None)")


def main():
    print("Bar Cohomology Computation")
    print("=" * 70)

    # Step 1: Validate zeroth products
    validate_zeroth_product()

    # Step 2: Validate Virasoro bar cohomology
    print()
    validate_virasoro()


if __name__ == "__main__":
    main()
