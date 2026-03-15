r"""E₁ page of the bar spectral sequence for sl₃[t] = sl₃ \otimes \C[t].

Extends the sl₂ current algebra E₁ computation to sl₃, with direct
verification of the Loday-Quillen-Tsygan (LQT) prediction.

The E₁ page for the Strategy IV spectral sequence (comp:current-algebra-E1,
comp:current-algebra-E1-all-types in yangians.tex) computes
  dim E_1^{0,p}(g[t])
where p is the "loop degree" defined by deg_loop(xi_{i,n}) = 2e_i + 1 + 2n
for the LQT generators (exponents e_i, loop level n >= 0).

KEY DISTINCTION: The cohomology H*(g[t], k) computed here is the
CONTINUOUS Chevalley-Eilenberg cohomology, where cochains on the
pro-finite-dimensional algebra g[t] = lim g[t]/(t^N) are required to
factor through finite-dimensional quotients.  This is NOT the algebraic
CE cohomology (which equals H*(g) by retraction t -> 0).

At each polynomial weight H (= total t-degree), the continuous CE complex
is finite-dimensional and can be computed directly.  The generators of g[t]
at t-degree n (n >= 0) contribute dim(g) generators at each level.

The complex:
  - g[t]_H = {sum of products X_{a_i} * t^{n_i} with sum(n_i) = H, each n_i >= 0}
  - CE^p_H = Lambda^p((g[t]_H)*) = antisymmetric p-forms on g[t] at weight H
  - Decomposition: CE^p_H = direct-sum over partitions (n_1,...,n_p) of H
    into p parts >= 0, of tensor products of exterior powers Lambda^{k_n}(g*)

The CE differential d: CE^p_H -> CE^{p+1}_H acts by:
  (df)(v_1,...,v_{p+1}) = sum_{i<j} (-1)^{i+j} f([v_i,v_j], v_1,...,hat{v}_i,...,hat{v}_j,...,v_{p+1})

Since [X*t^a, Y*t^b] = [X,Y]*t^{a+b}, the differential preserves
polynomial weight H.

For sl_3 (exponents 1, 2), LQT predicts:
  dim E_1^{0,p}: 1, 0, 0, 1, 0, 2, 0, 2, 2, 2, ...

This module provides:
  1. Direct computation of continuous CE cohomology at each weight H
  2. Verification of d^2 = 0
  3. Accumulation by loop degree p = CE_degree + 2*poly_weight
     (the grading from the Strategy IV spectral sequence, where each
     generator X*t^n has loop degree 1+2n, so a CE p-form on generators
     with t-degrees n_1,...,n_p has loop degree p + 2*(n_1+...+n_p))
  4. Comparison with LQT predictions
  5. Cross-validation with sl_2 and with ce_cohomology_loop.py

Relationship to existing modules:
  - ce_cohomology_loop.py: CE cohomology of V-bar = g tensor t^{-1}k[t^{-1}].
    This is the NEGATIVE loop algebra. The computations are isomorphic
    (replace t by t^{-1}, reverse grading) but differ in:
      * ce_cohomology_loop.py uses partitions of H into parts >= 1
      * This module uses partitions of H into parts >= 0
    At q=0, this module includes the zero-mode g_0 = g (contributions
    from the finite-dimensional algebra), while ce_cohomology_loop.py
    does not (V-bar starts at weight 1).
  - lqt_e1_growth.py: LQT predictions via subset-sum counting
  - pbw_e1_sl3.py: PBW E_1 page via invariant dimensions

References:
  - comp:current-algebra-E1, comp:current-algebra-E1-all-types (yangians.tex)
  - Feigin-Tsygan (LQT theorem for current algebras)
  - genus1_pbw_sl2.py (sl_2 analog)
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.sl3_bar import DIM_G, sl3_structure_constants
from compute.lib.ce_cohomology_loop import (
    sl2_structure_constants,
    DIM_G_SL2,
)


# ============================================================
# Structure constant tensor
# ============================================================

def _build_structure_tensor(dim_g: int, structure_constants: Dict) -> np.ndarray:
    """Build dense structure constant tensor f^{ab}_c.

    Returns: (dim_g, dim_g, dim_g) array where T[a,b,c] = f^{ab}_c.
    """
    T = np.zeros((dim_g, dim_g, dim_g))
    for (a, b), outputs in structure_constants.items():
        for c, coeff in outputs.items():
            T[a, b, c] += float(coeff)
    return T


# ============================================================
# Partition enumeration (parts >= 0)
# ============================================================

def partitions_into_n_parts_geq0(H: int, n: int) -> List[Tuple[int, ...]]:
    """All partitions of H into exactly n parts >= 0, in non-decreasing order.

    Unlike ce_cohomology_loop.py which uses parts >= 1, this allows parts = 0
    (the zero-mode g_0 of the current algebra).
    """
    if n == 0:
        return [()] if H == 0 else []
    if H < 0:
        return []
    result = []
    _partition_helper_geq0(H, n, 0, [], result)
    return result


def _partition_helper_geq0(remaining: int, parts_left: int, min_val: int,
                            current: List[int], result: List[Tuple[int, ...]]):
    """Recursive helper for partition enumeration (parts >= 0)."""
    if parts_left == 0:
        if remaining == 0:
            result.append(tuple(current))
        return
    max_val = remaining
    for v in range(min_val, max_val + 1):
        _partition_helper_geq0(remaining - v, parts_left - 1, v,
                                current + [v], result)


def partition_multiplicities(partition: Tuple[int, ...]) -> Dict[int, int]:
    """Given a sorted partition, return {value: multiplicity}."""
    mults = {}
    for v in partition:
        mults[v] = mults.get(v, 0) + 1
    return mults


# ============================================================
# Basis construction for CE^p_H
# ============================================================

def exterior_power_dim(dim_g: int, k: int) -> int:
    """Dimension of Lambda^k(g*) where dim g = dim_g."""
    return comb(dim_g, k)


def exterior_power_basis(dim_g: int, k: int) -> List[Tuple[int, ...]]:
    """Basis elements for Lambda^k(g*): sorted k-tuples from {0,...,dim_g-1}."""
    return list(combinations(range(dim_g), k))


def ce_space_dim(dim_g: int, H: int, n: int) -> int:
    """Dimension of CE^n_H (continuous cochains at weight H, CE degree n).

    Sum over partitions of H into n parts >= 0, product of C(dim_g, k_h)
    for each weight h appearing k_h times.
    """
    partitions = partitions_into_n_parts_geq0(H, n)
    total = 0
    for part in partitions:
        mults = partition_multiplicities(part)
        prod = 1
        for h, k in mults.items():
            prod *= exterior_power_dim(dim_g, k)
        total += prod
    return total


# ============================================================
# Basis element representation
# ============================================================

class CEBasis:
    """Manages basis for CE^n_H (continuous cochains at weight H, degree n)."""

    def __init__(self, dim_g: int, H: int, n: int):
        self.dim_g = dim_g
        self.H = H
        self.n = n
        self.partitions = partitions_into_n_parts_geq0(H, n)

        self.block_offsets = []
        self.block_dims = []
        self.block_data = []

        offset = 0
        for part in self.partitions:
            mults = partition_multiplicities(part)
            weights_sorted = sorted(mults.keys())
            ext_bases = {}
            block_dim = 1
            for h in weights_sorted:
                k = mults[h]
                basis = exterior_power_basis(dim_g, k)
                ext_bases[h] = basis
                block_dim *= len(basis)

            self.block_offsets.append(offset)
            self.block_dims.append(block_dim)
            self.block_data.append((mults, weights_sorted, ext_bases))
            offset += block_dim

        self.total_dim = offset

    def flat_index(self, part_idx: int, component_indices: Dict[int, int]) -> int:
        """Convert (partition index, {weight: basis_index_within_Lambda^k}) to flat index."""
        mults, weights_sorted, ext_bases = self.block_data[part_idx]
        flat = 0
        for h in weights_sorted:
            flat = flat * len(ext_bases[h]) + component_indices[h]
        return self.block_offsets[part_idx] + flat

    def decode_flat(self, flat_idx: int) -> Tuple[int, Dict[int, Tuple[int, ...]]]:
        """Convert flat index to (partition_index, {weight: exterior_basis_element})."""
        part_idx = 0
        for i, (off, dim) in enumerate(zip(self.block_offsets, self.block_dims)):
            if flat_idx < off + dim:
                part_idx = i
                break
        else:
            part_idx = len(self.partitions) - 1

        local = flat_idx - self.block_offsets[part_idx]
        mults, weights_sorted, ext_bases = self.block_data[part_idx]

        result = {}
        for h in reversed(weights_sorted):
            basis = ext_bases[h]
            result[h] = basis[local % len(basis)]
            local //= len(basis)

        return part_idx, result


# ============================================================
# CE differential matrix
# ============================================================

def _expand_to_slots(partition: Tuple[int, ...],
                     component: Dict[int, Tuple[int, ...]]) -> List[Tuple[int, int]]:
    """Expand partition + component dict into list of (weight, gen_index) pairs."""
    mults = partition_multiplicities(partition)
    slots = []
    for h in sorted(mults.keys()):
        gen_indices = component[h]
        for a in gen_indices:
            slots.append((h, a))
    return slots


def _canonicalize_and_index(dim_g: int, basis: CEBasis,
                            slots: List[Tuple[int, int]]) -> Tuple[int, Optional[int]]:
    """Canonicalize (weight, gen_index) pairs and find basis index.

    Returns: (sign, flat_index) or (0, None) if the element vanishes.
    """
    n = len(slots)
    slots = list(slots)
    sign = 1
    for i in range(n):
        for j in range(n - 1, i, -1):
            if slots[j] < slots[j - 1]:
                slots[j], slots[j - 1] = slots[j - 1], slots[j]
                sign *= -1

    for i in range(n - 1):
        if slots[i] == slots[i + 1]:
            return 0, None

    partition = tuple(h for h, a in slots)

    part_idx = None
    for idx, p in enumerate(basis.partitions):
        if p == partition:
            part_idx = idx
            break

    if part_idx is None:
        return 0, None

    mults = partition_multiplicities(partition)
    component = {}
    pos = 0
    for h in sorted(mults.keys()):
        k = mults[h]
        gens = tuple(a for _, a in slots[pos:pos + k])
        component[h] = gens
        pos += k

    mults_data, weights_sorted, ext_bases = basis.block_data[part_idx]
    component_indices = {}
    for h in weights_sorted:
        gens = component[h]
        try:
            idx = ext_bases[h].index(gens)
        except ValueError:
            return 0, None
        component_indices[h] = idx

    flat = basis.flat_index(part_idx, component_indices)
    return sign, flat


def build_ce_differential(dim_g: int, f_tensor: np.ndarray,
                          H: int, n: int) -> np.ndarray:
    """Build CE differential d: CE^n_H -> CE^{n+1}_H.

    For the current algebra g[t], the bracket [X*t^a, Y*t^b] = [X,Y]*t^{a+b}
    preserves the total weight H.

    Strategy: build the boundary on chains (Lambda^{n+1} -> Lambda^n)
    and transpose.

    Returns: (dim CE^{n+1}_H, dim CE^n_H) numpy array.
    """
    source_basis = CEBasis(dim_g, H, n)
    target_basis = CEBasis(dim_g, H, n + 1)

    if source_basis.total_dim == 0 or target_basis.total_dim == 0:
        return np.zeros((target_basis.total_dim, source_basis.total_dim))

    M_chain = np.zeros((source_basis.total_dim, target_basis.total_dim))

    for tgt_flat in range(target_basis.total_dim):
        part_idx, component = target_basis.decode_flat(tgt_flat)
        partition = target_basis.partitions[part_idx]
        slots = _expand_to_slots(partition, component)

        for i in range(len(slots)):
            for j in range(i + 1, len(slots)):
                h_i, a_i = slots[i]
                h_j, a_j = slots[j]
                h_new = h_i + h_j

                for c in range(dim_g):
                    f_val = f_tensor[a_i, a_j, c]
                    if f_val == 0.0:
                        continue

                    new_slots = []
                    for k in range(len(slots)):
                        if k == i or k == j:
                            continue
                        new_slots.append(slots[k])
                    new_slots.append((h_new, c))

                    ce_sign = (-1) ** (i + j)
                    can_sign, src_flat = _canonicalize_and_index(
                        dim_g, source_basis, new_slots)

                    if src_flat is not None:
                        M_chain[src_flat, tgt_flat] += ce_sign * can_sign * f_val

    return M_chain.T


# ============================================================
# d^2 = 0 verification
# ============================================================

def verify_d_squared(dim_g: int, f_tensor: np.ndarray,
                     H: int, n: int) -> float:
    """Check d_{n+1} . d_n = 0.  Returns Frobenius norm (should be near 0)."""
    d_n = build_ce_differential(dim_g, f_tensor, H, n)
    d_np1 = build_ce_differential(dim_g, f_tensor, H, n + 1)

    if d_n.shape[1] == 0 or d_np1.shape[0] == 0:
        return 0.0

    comp = d_np1 @ d_n
    return float(np.linalg.norm(comp))


# ============================================================
# Cohomology computation
# ============================================================

def ce_cohomology_at_weight(dim_g: int, f_tensor: np.ndarray,
                            H: int, max_degree: int = 8) -> Dict[int, int]:
    """Compute H^n(g[t], k)_H for n = 0, ..., max_degree.

    Returns: {n: dim H^n_H}.
    """
    dims = {}
    diff_matrices = {}

    for n in range(max_degree + 2):
        dims[n] = ce_space_dim(dim_g, H, n)

    for n in range(max_degree + 1):
        if dims[n] == 0 or dims[n + 1] == 0:
            diff_matrices[n] = np.zeros((dims[n + 1], dims[n]))
        else:
            diff_matrices[n] = build_ce_differential(dim_g, f_tensor, H, n)

    result = {}
    for n in range(max_degree + 1):
        if dims[n] == 0:
            result[n] = 0
            continue

        if n <= max_degree and dims[n + 1] > 0:
            d_n = diff_matrices[n]
            rank_out = int(np.linalg.matrix_rank(d_n, tol=1e-8))
            ker_dim = dims[n] - rank_out
        else:
            ker_dim = dims[n]

        if n >= 1 and dims[n - 1] > 0:
            d_prev = diff_matrices[n - 1]
            im_dim = int(np.linalg.matrix_rank(d_prev, tol=1e-8))
        else:
            im_dim = 0

        result[n] = ker_dim - im_dim

    return result


def ce_cohomology_table(dim_g: int, f_tensor: np.ndarray,
                        max_weight: int, max_degree: int) -> Dict[Tuple[int, int], int]:
    """Compute H^n(g[t], k)_H for H = 0,...,max_weight, n = 0,...,max_degree.

    Returns: dict mapping (n, H) to dim H^n_H (nonzero entries only).
    """
    table = {}
    for H in range(max_weight + 1):
        cohom = ce_cohomology_at_weight(dim_g, f_tensor, H, max_degree)
        for n, dim_val in cohom.items():
            if dim_val != 0:
                table[(n, H)] = dim_val
    return table


# ============================================================
# E₁ page by loop degree
# ============================================================

def e1_by_loop_degree(dim_g: int, f_tensor: np.ndarray,
                      max_weight: int, max_loop_deg: int,
                      max_ce_deg: int = None) -> Dict[int, int]:
    """Compute dim E_1^{0,p} by accumulating H^n_H at loop degree p = n + 2H.

    The loop degree grading: a CE n-form on generators at t-degrees
    (h_1,...,h_n) has loop degree n + 2*(h_1+...+h_n) = n + 2H.

    Returns: {loop_degree: total_dim}.
    """
    if max_ce_deg is None:
        max_ce_deg = max_loop_deg

    result = {p: 0 for p in range(max_loop_deg + 1)}

    for H in range(max_weight + 1):
        max_n = min(max_ce_deg, max_loop_deg - 2 * H)
        if max_n < 0:
            continue
        cohom = ce_cohomology_at_weight(dim_g, f_tensor, H, max_degree=max_n)
        for n, dim_val in cohom.items():
            p = n + 2 * H
            if p <= max_loop_deg and dim_val != 0:
                result[p] += dim_val

    return result


# ============================================================
# LQT predictions
# ============================================================

def lqt_prediction(exponents: List[int], max_loop_deg: int) -> List[int]:
    """LQT prediction: dim E_1^{0,p} = number of subsets of
    {2e_i + 1 + 2n : i, n >= 0} summing to p.
    """
    gens = []
    for e in exponents:
        n = 0
        while 2 * e + 1 + 2 * n <= max_loop_deg:
            gens.append(2 * e + 1 + 2 * n)
            n += 1

    dp = [0] * (max_loop_deg + 1)
    dp[0] = 1
    for g_deg in gens:
        for s in range(max_loop_deg, g_deg - 1, -1):
            dp[s] += dp[s - g_deg]
    return dp


def lqt_prediction_sl2(max_loop_deg: int) -> List[int]:
    """LQT prediction for sl_2[t]: exponents = [1]."""
    return lqt_prediction([1], max_loop_deg)


def lqt_prediction_sl3(max_loop_deg: int) -> List[int]:
    """LQT prediction for sl_3[t]: exponents = [1, 2]."""
    return lqt_prediction([1, 2], max_loop_deg)


# ============================================================
# Convenience wrappers
# ============================================================

def sl2_e1_direct(max_weight: int, max_loop_deg: int) -> Dict[int, int]:
    """E₁ for sl₂[t] via direct CE cohomology."""
    sc = sl2_structure_constants()
    ft = _build_structure_tensor(DIM_G_SL2, sc)
    return e1_by_loop_degree(DIM_G_SL2, ft, max_weight, max_loop_deg)


def sl3_e1_direct(max_weight: int, max_loop_deg: int) -> Dict[int, int]:
    """E₁ for sl₃[t] via direct CE cohomology."""
    sc = sl3_structure_constants()
    ft = _build_structure_tensor(DIM_G, sc)
    return e1_by_loop_degree(DIM_G, ft, max_weight, max_loop_deg)


def sl2_cohomology_table(max_weight: int, max_degree: int) -> Dict[Tuple[int, int], int]:
    """Full (CE degree, weight) table for sl₂[t]."""
    sc = sl2_structure_constants()
    ft = _build_structure_tensor(DIM_G_SL2, sc)
    return ce_cohomology_table(DIM_G_SL2, ft, max_weight, max_degree)


def sl3_cohomology_table(max_weight: int, max_degree: int) -> Dict[Tuple[int, int], int]:
    """Full (CE degree, weight) table for sl₃[t]."""
    sc = sl3_structure_constants()
    ft = _build_structure_tensor(DIM_G, sc)
    return ce_cohomology_table(DIM_G, ft, max_weight, max_degree)


# ============================================================
# Comparison utilities
# ============================================================

def compare_with_lqt(dim_g: int, f_tensor: np.ndarray,
                     max_weight: int, max_loop_deg: int,
                     lqt_dims: List[int]) -> Dict[str, object]:
    """Compare direct computation with LQT prediction."""
    direct = e1_by_loop_degree(dim_g, f_tensor, max_weight, max_loop_deg)

    matches = {}
    mismatches = {}
    for p in range(max_loop_deg + 1):
        d = direct.get(p, 0)
        lqt = lqt_dims[p] if p < len(lqt_dims) else 0
        if d == lqt:
            matches[p] = d
        else:
            mismatches[p] = {"direct": d, "lqt": lqt}

    return {
        "direct": direct,
        "lqt": {p: lqt_dims[p] for p in range(min(max_loop_deg + 1, len(lqt_dims)))},
        "matches": matches,
        "mismatches": mismatches,
        "all_match": len(mismatches) == 0,
    }


def growth_rate_comparison(max_loop_deg: int = 20) -> Dict[str, object]:
    """Compare LQT growth rates for sl₂ vs sl₃.

    sl₂: dim H^p ~ exp(pi*sqrt(p/12))  (rank 1)
    sl₃: dim H^p ~ exp(pi*sqrt(p/6))   (rank 2)
    """
    sl2_lqt = lqt_prediction_sl2(max_loop_deg)
    sl3_lqt = lqt_prediction_sl3(max_loop_deg)

    return {
        "sl2": sl2_lqt,
        "sl3": sl3_lqt,
        "ratio_nonzero": {
            p: sl3_lqt[p] / sl2_lqt[p]
            for p in range(max_loop_deg + 1)
            if sl2_lqt[p] > 0 and sl3_lqt[p] > 0
        },
        "first_departure": next(
            (p for p in range(max_loop_deg + 1)
             if sl2_lqt[p] != sl3_lqt[p]),
            None
        ),
    }


# ============================================================
# Cross-validation with ce_cohomology_loop.py
# ============================================================

def cross_validate_with_loop_module(dim_g: int, structure_constants: Dict,
                                     max_weight: int,
                                     max_degree: int) -> Dict[str, object]:
    """Cross-validate H^n_H(g[t]) with H^n_H(V-bar) from ce_cohomology_loop.py.

    For H >= 1, the CE cohomology of g[t] at weight H should equal the
    CE cohomology of V-bar = g tensor t^{-1}k[t^{-1}] at weight H
    (the partitions differ only at weight 0: g[t] includes the zero-mode,
    V-bar does not).
    """
    from compute.lib.ce_cohomology_loop import (
        ce_cohomology_table as loop_table,
    )

    f_tensor = _build_structure_tensor(dim_g, structure_constants)
    current_table = ce_cohomology_table(dim_g, f_tensor, max_weight, max_degree)
    vbar_table = loop_table(max_weight, max_degree, dim_g, structure_constants)

    matches = {}
    mismatches = {}
    for H in range(1, max_weight + 1):
        for n in range(max_degree + 1):
            current_val = current_table.get((n, H), 0)
            vbar_val = vbar_table.get((n, H), 0)
            key = (n, H)
            if current_val == vbar_val:
                if current_val != 0:
                    matches[key] = current_val
            else:
                mismatches[key] = {"current": current_val, "vbar": vbar_val}

    return {
        "matches": matches,
        "mismatches": mismatches,
        "all_match": len(mismatches) == 0,
    }


# ============================================================
# Print utilities
# ============================================================

def print_cohomology_table(table: Dict[Tuple[int, int], int],
                           max_weight: int, max_degree: int,
                           title: str = "H^n_H"):
    """Print cohomology table in a formatted grid."""
    print(f"\n{title:>8}", end="")
    for H in range(max_weight + 1):
        print(f" H={H:>2}", end="")
    print("  Total")
    print("-" * (10 + 6 * (max_weight + 1) + 7))

    for n in range(max_degree + 1):
        print(f"  n={n:>2}  ", end="")
        total = 0
        for H in range(max_weight + 1):
            val = table.get((n, H), 0)
            total += val
            print(f" {val:>4}", end="")
        print(f"  {total:>5}")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    import time

    print("=" * 70)
    print("E₁ PAGE: CURRENT ALGEBRA g[t] — STRATEGY IV SPECTRAL SEQUENCE")
    print("=" * 70)

    # Part 1: sl₂ cross-validation
    print("\n" + "=" * 70)
    print("PART 1: sl₂[t]")
    print("=" * 70)

    sc_sl2 = sl2_structure_constants()
    ft_sl2 = _build_structure_tensor(DIM_G_SL2, sc_sl2)

    print("\n--- d^2 = 0 verification ---")
    all_ok = True
    for H in range(6):
        for n in range(4):
            norm = verify_d_squared(DIM_G_SL2, ft_sl2, H, n)
            if norm > 1e-10:
                print(f"  FAIL at (H={H}, n={n}): norm={norm:.2e}")
                all_ok = False
    print(f"  All checks: {'PASS' if all_ok else 'FAIL'}")

    max_H_sl2 = 6
    max_n_sl2 = 4
    table_sl2 = ce_cohomology_table(DIM_G_SL2, ft_sl2, max_H_sl2, max_n_sl2)
    print_cohomology_table(table_sl2, max_H_sl2, max_n_sl2, "sl₂[t]")

    print(f"\n--- E₁ by loop degree ---")
    max_loop_sl2 = 9
    t0 = time.time()
    direct_sl2 = e1_by_loop_degree(DIM_G_SL2, ft_sl2, max_H_sl2, max_loop_sl2)
    elapsed = time.time() - t0
    direct_list = [direct_sl2.get(p, 0) for p in range(max_loop_sl2 + 1)]
    lqt_sl2 = lqt_prediction_sl2(max_loop_sl2)
    print(f"  Time: {elapsed:.1f}s")
    print(f"  Direct: {direct_list}")
    print(f"  LQT:    {lqt_sl2}")
    print(f"  Match:  {direct_list == lqt_sl2}")

    # Cross-validation with loop module
    print("\n--- Cross-validation with ce_cohomology_loop.py ---")
    xval = cross_validate_with_loop_module(DIM_G_SL2, sc_sl2, 4, 4)
    print(f"  All match at H >= 1: {xval['all_match']}")
    if xval['mismatches']:
        print(f"  Mismatches: {xval['mismatches']}")

    # Part 2: sl₃
    print("\n" + "=" * 70)
    print("PART 2: sl₃[t]")
    print("=" * 70)

    sc_sl3 = sl3_structure_constants()
    ft_sl3 = _build_structure_tensor(DIM_G, sc_sl3)

    print("\n--- d^2 = 0 verification ---")
    all_ok = True
    for H in range(5):
        for n in range(5):
            norm = verify_d_squared(DIM_G, ft_sl3, H, n)
            if norm > 1e-10:
                print(f"  FAIL at (H={H}, n={n}): norm={norm:.2e}")
                all_ok = False
    print(f"  All checks: {'PASS' if all_ok else 'FAIL'}")

    max_H_sl3 = 4
    max_n_sl3 = 6
    t0 = time.time()
    table_sl3 = ce_cohomology_table(DIM_G, ft_sl3, max_H_sl3, max_n_sl3)
    elapsed = time.time() - t0
    print(f"  Computation time: {elapsed:.1f}s")
    print_cohomology_table(table_sl3, max_H_sl3, max_n_sl3, "sl₃[t]")

    print(f"\n--- E₁ by loop degree ---")
    max_loop_sl3 = 9
    direct_sl3 = e1_by_loop_degree(DIM_G, ft_sl3, max_H_sl3, max_loop_sl3)
    direct_list = [direct_sl3.get(p, 0) for p in range(max_loop_sl3 + 1)]
    lqt_sl3 = lqt_prediction_sl3(max_loop_sl3)
    print(f"  Direct: {direct_list}")
    print(f"  LQT:    {lqt_sl3}")
    print(f"  Match:  {direct_list == lqt_sl3}")

    # Part 3: growth comparison
    print("\n" + "=" * 70)
    print("PART 3: Growth rate comparison (LQT)")
    print("=" * 70)

    growth = growth_rate_comparison(20)
    print(f"\n  sl₂ LQT: {growth['sl2']}")
    print(f"  sl₃ LQT: {growth['sl3']}")
    print(f"  First departure: p = {growth['first_departure']}")
    for p, r in sorted(growth['ratio_nonzero'].items()):
        print(f"    p={p:>2}: ratio = {r:.2f}")
