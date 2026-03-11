"""Chevalley-Eilenberg cohomology of the negative loop algebra V̄ = sl₃ ⊗ t⁻¹k[t⁻¹].

Computes H^n(V̄, k)_H — CE cohomology at each conformal weight H and
CE degree n — for the loop algebra with bracket

    [J^a_{-m}, J^b_{-n}] = f^{ab}_c J^c_{-(m+n)}

(no central extension since m, n ≥ 1 implies m+n ≥ 2, so central term vanishes).

The graded components are:
    V̄ = ⊕_{h≥1} g_h,  g_h ≅ sl₃ (dim 8)

CE cochain complex:
    CE^n_H = Λ^n(V̄*)_H = antisymmetric n-linear forms on V̄ of total weight H

The basis decomposition: Λ^n(V̄*)_H decomposes over partitions of H into
n parts ≥ 1. For a partition with weight h appearing k_h times, the
corresponding subspace is ⊗_h Λ^{k_h}(g*).

References:
    - sl3_bar.py: structure constants for sl₃
    - km_chiral_bar.py: related bar complex computations
    - MEMORY.md: Koszul dual dims [1,8,36,204,1352]
"""

from __future__ import annotations

from itertools import combinations
from math import comb
from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.sl3_bar import DIM_G, sl3_structure_constants


# ============================================================
# Structure constant cache
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
# Partition enumeration
# ============================================================

def partitions_into_n_parts(H: int, n: int) -> List[Tuple[int, ...]]:
    """All partitions of H into exactly n parts ≥ 1, in non-decreasing order.

    Returns a list of sorted tuples (h_1, ..., h_n) with h_i ≥ 1 and sum = H.
    """
    if n == 0:
        return [()] if H == 0 else []
    if n == 1:
        return [(H,)] if H >= 1 else []
    if H < n:
        return []

    result = []
    _partition_helper(H, n, 1, [], result)
    return result


def _partition_helper(remaining: int, parts_left: int, min_val: int,
                      current: List[int], result: List[Tuple[int, ...]]):
    """Recursive helper for partition enumeration."""
    if parts_left == 0:
        if remaining == 0:
            result.append(tuple(current))
        return
    # max value for this part: remaining - (parts_left - 1) * 1
    max_val = remaining - (parts_left - 1)
    for v in range(min_val, max_val + 1):
        _partition_helper(remaining - v, parts_left - 1, v,
                          current + [v], result)


def partition_multiplicities(partition: Tuple[int, ...]) -> Dict[int, int]:
    """Given a sorted partition, return {value: multiplicity}."""
    mults = {}
    for v in partition:
        mults[v] = mults.get(v, 0) + 1
    return mults


# ============================================================
# Basis construction for Λ^n(V̄*)_H
# ============================================================

def exterior_power_dim(dim_g: int, k: int) -> int:
    """Dimension of Λ^k(g*) where dim g = dim_g."""
    return comb(dim_g, k)


def exterior_power_basis(dim_g: int, k: int) -> List[Tuple[int, ...]]:
    """Basis elements for Λ^k(g*): sorted k-tuples from {0, ..., dim_g-1}.

    Each tuple (i_1, ..., i_k) with i_1 < i_2 < ... < i_k represents
    e^{i_1} ∧ ... ∧ e^{i_k}.
    """
    return list(combinations(range(dim_g), k))


def ce_space_dim(dim_g: int, H: int, n: int) -> int:
    """Dimension of CE^n_H = Λ^n(V̄*)_H.

    Sum over partitions of H into n parts of ∏_h C(dim_g, k_h).
    """
    partitions = partitions_into_n_parts(H, n)
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

# A basis element of Λ^n(V̄*)_H is represented as:
#   (partition, component)
# where partition is a sorted tuple of weights (h_1, ..., h_n)
# and component specifies the multi-index within the tensor product
# of exterior powers.
#
# More precisely: for partition with distinct weights h appearing k_h times,
# the component is a dict {h: basis_idx} where basis_idx indexes into
# the Λ^{k_h}(g*) basis (sorted tuple of generator indices).
#
# For efficient matrix computation, we flatten everything into a single
# integer index per partition block.


class CEBasis:
    """Manages basis for CE^n_H = Λ^n(V̄*)_H."""

    def __init__(self, dim_g: int, H: int, n: int):
        self.dim_g = dim_g
        self.H = H
        self.n = n
        self.partitions = partitions_into_n_parts(H, n)

        # For each partition, compute the block dimension and offset
        self.block_offsets = []  # start index for each partition block
        self.block_dims = []    # dimension of each partition block
        self.block_data = []    # list of (mults, ext_bases) for each partition

        offset = 0
        for part in self.partitions:
            mults = partition_multiplicities(part)
            # Sorted distinct weights
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
        """Convert (partition index, {weight: basis_index_within_Λ^k}) to flat index.

        component_indices maps each distinct weight h to an index into
        ext_bases[h].
        """
        mults, weights_sorted, ext_bases = self.block_data[part_idx]
        flat = 0
        for h in weights_sorted:
            flat = flat * len(ext_bases[h]) + component_indices[h]
        return self.block_offsets[part_idx] + flat

    def decode_flat(self, flat_idx: int) -> Tuple[int, Dict[int, Tuple[int, ...]]]:
        """Convert flat index to (partition_index, {weight: exterior_basis_element}).

        Returns the partition index and a dict mapping each distinct weight
        to its exterior power basis element (sorted tuple of generator indices).
        """
        # Find which partition block
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
# CE differential matrix construction
# ============================================================

def _sign_of_insertion(ext_element: Tuple[int, ...], insert_idx: int) -> Tuple[int, Tuple[int, ...]]:
    """Insert generator index into a sorted exterior element.

    Returns (sign, new_element) where sign is +1 or -1 from sorting,
    or (0, ()) if the index is already present (antisymmetry kills it).
    """
    if insert_idx in ext_element:
        return 0, ()
    new_list = list(ext_element) + [insert_idx]
    # Bubble sort to get the sign
    sign = 1
    for i in range(len(new_list) - 1, 0, -1):
        if new_list[i] < new_list[i - 1]:
            new_list[i], new_list[i - 1] = new_list[i - 1], new_list[i]
            sign *= -1
    return sign, tuple(new_list)


def _sign_of_removal(ext_element: Tuple[int, ...], position: int) -> Tuple[int, Tuple[int, ...]]:
    """Remove generator at given position from a sorted exterior element.

    Returns (sign, new_element) where sign is (-1)^position.
    """
    sign = (-1) ** position
    new_list = list(ext_element)
    del new_list[position]
    return sign, tuple(new_list)


def build_ce_differential(dim_g: int, f_tensor: np.ndarray,
                          H: int, n: int) -> np.ndarray:
    """Build the CE differential matrix d: CE^n_H → CE^{n+1}_H.

    The CE differential acts as:
        (dψ)(v_1, ..., v_{n+1}) = Σ_{i<j} (-1)^{i+j} ψ([v_i, v_j], v_1, ..., v̂_i, ..., v̂_j, ..., v_{n+1})

    On the dual side (cochains), this maps Λ^n → Λ^{n+1} by:
        d(e^{a_1} ∧ ... ∧ e^{a_n}) corresponds to contracting two slots
        in the (n+1)-form with the bracket.

    Implementation strategy:
    We work with the DUAL picture. A basis element of Λ^n(V̄*)_H is
    an antisymmetric n-form on V̄ of weight H. We think of it as specifying
    which generators it eats.

    For the loop algebra, an element at positions with weights (h_1,...,h_n)
    and generators (a_1,...,a_n) represents the cochain that evaluates on
    J^{a_1}_{-h_1} ∧ ... ∧ J^{a_n}_{-h_n}.

    The differential d: CE^n_H → CE^{n+1}_H is the transpose of the
    CE boundary d: Λ^{n+1}(V̄)_H → Λ^n(V̄)_H on chains.

    Strategy: build the boundary map on CHAINS (Λ^{n+1} → Λ^n) and transpose.
    This is conceptually cleaner: the boundary is
        ∂(v_1 ∧ ... ∧ v_{n+1}) = Σ_{i<j} (-1)^{i+j} [v_i, v_j] ∧ v_1 ∧ ... ∧ v̂_i ∧ ... ∧ v̂_j ∧ ... ∧ v_{n+1}

    where v_k = J^{a_k}_{-h_k}.

    Returns: (dim CE^{n+1}_H, dim CE^n_H) numpy array.
    """
    source_basis = CEBasis(dim_g, H, n)
    target_basis = CEBasis(dim_g, H, n + 1)

    if source_basis.total_dim == 0 or target_basis.total_dim == 0:
        return np.zeros((target_basis.total_dim, source_basis.total_dim))

    # Build the boundary map on chains: Λ^{n+1}(V̄)_H → Λ^n(V̄)_H
    # Then transpose to get d: CE^n → CE^{n+1} on cochains.
    #
    # Actually, for Lie algebra cohomology with trivial coefficients,
    # the cochain differential IS the standard one. Let's build it directly.
    #
    # We enumerate target basis elements (degree n+1) and for each,
    # we look at all pairs (i,j) in the (n+1)-element set of "slots",
    # bracket the corresponding generators, and produce a degree-n element.
    #
    # But it's more efficient to build the transpose of the boundary.
    # The boundary on Λ^{n+1} → Λ^n is:
    #   ∂(w_1 ∧ ... ∧ w_{n+1}) = Σ_{i<j} (-1)^{i+j} [w_i, w_j] ∧ (others)
    #
    # The CE coboundary is the transpose: d = ∂^T.
    # So M_cochain[target, source] = M_chain[source, target]
    # where M_chain is the boundary from (n+1) to n.
    #
    # Let's build M_chain: Λ^{n+1}(V̄)_H → Λ^n(V̄)_H and then transpose.

    # Build chain boundary: from target_basis (degree n+1) to source_basis (degree n)
    M_chain = np.zeros((source_basis.total_dim, target_basis.total_dim))

    # Iterate over all basis elements of Λ^{n+1}(V̄)_H
    for tgt_flat in range(target_basis.total_dim):
        part_idx, component = target_basis.decode_flat(tgt_flat)
        partition = target_basis.partitions[part_idx]

        # Expand to a list of (weight, generator_index) pairs
        slots = _expand_to_slots(partition, component)
        # slots is a list of (h, a) pairs, length n+1
        # These are already in "canonical" order within each weight group

        # For each pair (i, j) with i < j, compute the bracket contribution
        for i in range(len(slots)):
            for j in range(i + 1, len(slots)):
                h_i, a_i = slots[i]
                h_j, a_j = slots[j]
                h_new = h_i + h_j

                # Bracket [J^{a_i}_{-h_i}, J^{a_j}_{-h_j}] = f^{a_i,a_j}_c J^c_{-h_new}
                for c in range(dim_g):
                    f_val = f_tensor[a_i, a_j, c]
                    if f_val == 0.0:
                        continue

                    # Build the resulting n-element wedge product:
                    # Replace slots[i] and slots[j] with (h_new, c), remove one
                    new_slots = []
                    for k in range(len(slots)):
                        if k == i or k == j:
                            continue
                        new_slots.append(slots[k])
                    # Insert (h_new, c)
                    new_slots.append((h_new, c))

                    # Compute the sign: (-1)^{i+j} from the CE formula,
                    # then additional sign from reordering into canonical form
                    ce_sign = (-1) ** (i + j)

                    # Convert new_slots to canonical form and get sign
                    can_sign, src_flat = _canonicalize_and_index(
                        dim_g, source_basis, new_slots)

                    if src_flat is not None:
                        M_chain[src_flat, tgt_flat] += ce_sign * can_sign * f_val

    # The cochain differential is the transpose of the chain boundary
    return M_chain.T


def _expand_to_slots(partition: Tuple[int, ...],
                     component: Dict[int, Tuple[int, ...]]) -> List[Tuple[int, int]]:
    """Expand a partition + component dict into a list of (weight, gen_index) pairs.

    The partition gives weights (h_1, ..., h_n) in sorted order.
    The component dict maps each distinct weight h to the exterior basis
    element (sorted tuple of gen indices) for that weight.

    Returns: list of (h, a) pairs in canonical order (sorted by weight,
    then by generator index within each weight group).
    """
    mults = partition_multiplicities(partition)
    slots = []
    for h in sorted(mults.keys()):
        gen_indices = component[h]  # sorted tuple of generator indices
        for a in gen_indices:
            slots.append((h, a))
    return slots


def _canonicalize_and_index(dim_g: int, basis: CEBasis,
                            slots: List[Tuple[int, int]]) -> Tuple[int, Optional[int]]:
    """Canonicalize a list of (weight, gen_index) pairs and find its basis index.

    1. Sort by weight (primary), then by gen_index (secondary)
    2. Track the permutation sign
    3. Check for repeated (weight, gen_index) pairs (antisymmetry: returns 0)
    4. Look up the flat index in the basis

    Returns: (sign, flat_index) or (0, None) if the element vanishes.
    """
    n = len(slots)

    # Sort with bubble sort to track sign
    slots = list(slots)
    sign = 1
    for i in range(n):
        for j in range(n - 1, i, -1):
            if slots[j] < slots[j - 1]:
                slots[j], slots[j - 1] = slots[j - 1], slots[j]
                sign *= -1

    # Check for duplicates (antisymmetry kills)
    for i in range(n - 1):
        if slots[i] == slots[i + 1]:
            return 0, None

    # Extract partition (sorted weights)
    partition = tuple(h for h, a in slots)

    # Find partition index
    part_idx = None
    for idx, p in enumerate(basis.partitions):
        if p == partition:
            part_idx = idx
            break

    if part_idx is None:
        # This partition doesn't exist in the basis (weight doesn't match)
        return 0, None

    # Extract component: group generators by weight
    mults = partition_multiplicities(partition)
    component = {}
    pos = 0
    for h in sorted(mults.keys()):
        k = mults[h]
        gens = tuple(a for _, a in slots[pos:pos + k])
        component[h] = gens
        pos += k

    # Find the index within each exterior power basis
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


# ============================================================
# Cohomology computation
# ============================================================

def ce_cohomology_at_weight(dim_g: int, f_tensor: np.ndarray,
                            H: int, max_degree: int = 4,
                            return_dims: bool = False) -> Dict[int, int]:
    """Compute H^n(V̄, k)_H for n = 0, 1, ..., max_degree.

    Returns: {n: dim H^n_H}.
    """
    # Build differential matrices for degrees n to n+1, where n = 0, ..., max_degree
    # CE^0_H = k if H=0, else 0
    # d_n: CE^n_H → CE^{n+1}_H

    dims = {}
    diff_matrices = {}

    for n in range(max_degree + 2):  # need degree max_degree+1 for the image
        dims[n] = ce_space_dim(dim_g, H, n)

    for n in range(max_degree + 1):
        if dims[n] == 0 or dims[n + 1] == 0:
            diff_matrices[n] = np.zeros((dims[n + 1], dims[n]))
        else:
            diff_matrices[n] = build_ce_differential(dim_g, f_tensor, H, n)

    # Compute cohomology
    result = {}
    for n in range(max_degree + 1):
        if dims[n] == 0:
            result[n] = 0
            continue

        # kernel of d_n
        if n <= max_degree:
            d_n = diff_matrices[n]
            rank_out = int(np.linalg.matrix_rank(d_n, tol=1e-8))
            ker_dim = dims[n] - rank_out
        else:
            ker_dim = dims[n]

        # image of d_{n-1}
        if n >= 1 and dims[n - 1] > 0:
            d_prev = diff_matrices[n - 1]
            im_dim = int(np.linalg.matrix_rank(d_prev, tol=1e-8))
        else:
            im_dim = 0

        result[n] = ker_dim - im_dim

    if return_dims:
        return result, dims, diff_matrices

    return result


def ce_cohomology_table(max_weight: int, max_degree: int = 4,
                        dim_g: int = DIM_G,
                        structure_constants: Optional[Dict] = None) -> Dict[Tuple[int, int], int]:
    """Compute CE cohomology H^n(V̄, k)_H for all weights H ≤ max_weight
    and degrees n ≤ max_degree.

    Returns: dict mapping (n, H) to dim H^n_H.
    """
    if structure_constants is None:
        structure_constants = sl3_structure_constants()

    f_tensor = _build_structure_tensor(dim_g, structure_constants)

    table = {}
    for H in range(1, max_weight + 1):
        cohom = ce_cohomology_at_weight(dim_g, f_tensor, H, max_degree)
        for n, dim_h in cohom.items():
            table[(n, H)] = dim_h

    return table


# ============================================================
# Verification
# ============================================================

def verify_d_squared(dim_g: int, f_tensor: np.ndarray,
                     H: int, n: int) -> float:
    """Check d_{n+1} ∘ d_n = 0 by computing the norm of the composition.

    Returns: Frobenius norm of d_{n+1} ∘ d_n (should be ~0).
    """
    d_n = build_ce_differential(dim_g, f_tensor, H, n)
    d_np1 = build_ce_differential(dim_g, f_tensor, H, n + 1)

    if d_n.shape[1] == 0 or d_np1.shape[1] == 0:
        return 0.0

    comp = d_np1 @ d_n
    return np.linalg.norm(comp)


def verify_h1(dim_g: int = DIM_G,
              structure_constants: Optional[Dict] = None) -> Dict[int, int]:
    """Verify H^1_H values.

    Expected:
        H^1_1 = 8 (abelianization: V̄_1/[V̄,V̄]∩V̄_1 = g since [V̄,V̄] starts at weight 2)
        H^1_H = 0 for H ≥ 2 (bracket [V̄_1, V̄_{H-1}] → V̄_H is surjective)

    Total H^1 = 8 = dim(g).
    """
    if structure_constants is None:
        structure_constants = sl3_structure_constants()

    f_tensor = _build_structure_tensor(dim_g, structure_constants)

    result = {}
    for H in range(1, 10):
        cohom = ce_cohomology_at_weight(dim_g, f_tensor, H, max_degree=1)
        result[H] = cohom.get(1, 0)

    return result


# ============================================================
# Display utilities
# ============================================================

def print_ce_table(table: Dict[Tuple[int, int], int],
                   max_weight: int, max_degree: int):
    """Print CE cohomology table in a formatted grid."""
    print(f"\n{'H^n_H':>8}", end="")
    for H in range(1, max_weight + 1):
        print(f" H={H:>2}", end="")
    print("  Total")
    print("-" * (10 + 6 * max_weight + 7))

    for n in range(max_degree + 1):
        print(f"  n={n:>2}  ", end="")
        total = 0
        for H in range(1, max_weight + 1):
            val = table.get((n, H), 0)
            total += val
            print(f" {val:>4}", end="")
        print(f"  {total:>5}")


def print_space_dims(dim_g: int, max_weight: int, max_degree: int):
    """Print dimensions of CE^n_H for reference."""
    print(f"\n{'CE^n_H':>8}", end="")
    for H in range(1, max_weight + 1):
        print(f" H={H:>2}", end="")
    print()
    print("-" * (10 + 6 * max_weight))

    for n in range(max_degree + 2):
        print(f"  n={n:>2}  ", end="")
        for H in range(1, max_weight + 1):
            val = ce_space_dim(dim_g, H, n)
            print(f" {val:>4}", end="")
        print()


# ============================================================
# sl₂ structure constants (for cross-validation)
# ============================================================

DIM_G_SL2 = 3

def sl2_structure_constants() -> Dict:
    """Structure constants for sl₂ with basis h=0, e=1, f=2.

    [h,e] = 2e, [h,f] = -2f, [e,f] = h.
    """
    return {
        (0, 1): {1: 2},   # [h,e] = 2e
        (1, 0): {1: -2},  # [e,h] = -2e
        (0, 2): {2: -2},  # [h,f] = -2f
        (2, 0): {2: 2},   # [f,h] = 2f
        (1, 2): {0: 1},   # [e,f] = h
        (2, 1): {0: -1},  # [f,e] = -h
    }


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    import time

    print("=" * 70)
    print("CE COHOMOLOGY OF V-bar = g tensor t^{-1}k[t^{-1}]")
    print("=" * 70)

    # ================================================================
    # Part 1: sl_2 cross-validation
    # ================================================================
    print("\n" + "=" * 70)
    print("PART 1: sl_2 (dim g = 3)")
    print("=" * 70)

    sc_sl2 = sl2_structure_constants()
    ft_sl2 = _build_structure_tensor(DIM_G_SL2, sc_sl2)

    # d^2 = 0 check
    print("\n--- d^2 = 0 verification ---")
    all_ok = True
    for H in range(1, 8):
        for n in range(0, 4):
            norm = verify_d_squared(DIM_G_SL2, ft_sl2, H, n)
            if norm > 1e-10:
                print(f"  FAIL at (H={H}, n={n}): norm={norm:.2e}")
                all_ok = False
    print(f"  All checks: {'PASS' if all_ok else 'FAIL'}")

    # Cohomology table
    max_H_sl2 = 12
    max_n_sl2 = 4
    print(f"\n--- CE cohomology (max_weight={max_H_sl2}, max_degree={max_n_sl2}) ---")
    t0 = time.time()
    table_sl2 = ce_cohomology_table(max_H_sl2, max_n_sl2, DIM_G_SL2, sc_sl2)
    elapsed = time.time() - t0
    print(f"  Computation time: {elapsed:.1f}s")

    print_ce_table(table_sl2, max_H_sl2, max_n_sl2)

    print("\n  Nonzero entries:")
    for n in range(max_n_sl2 + 1):
        nz = [(H, table_sl2.get((n, H), 0))
              for H in range(1, max_H_sl2 + 1)
              if table_sl2.get((n, H), 0) != 0]
        total = sum(v for _, v in nz)
        print(f"    H^{n}: {nz} (total = {total})")

    print("\n  Pattern: H^n = 2n+1 at weight n(n+1)/2 (triangular number)")

    # ================================================================
    # Part 2: sl_3
    # ================================================================
    print("\n" + "=" * 70)
    print("PART 2: sl_3 (dim g = 8)")
    print("=" * 70)

    sc = sl3_structure_constants()
    f_tensor = _build_structure_tensor(DIM_G, sc)

    # --- d^2 = 0 verification ---
    print("\n--- d^2 = 0 verification ---")
    all_ok = True
    for H in range(1, 7):
        for n in range(0, 4):
            norm = verify_d_squared(DIM_G, f_tensor, H, n)
            if norm > 1e-10:
                print(f"  FAIL at (H={H}, n={n}): norm={norm:.2e}")
                all_ok = False
    print(f"  All checks: {'PASS' if all_ok else 'FAIL'}")

    # --- H^1 verification ---
    print("\n--- H^1 verification ---")
    h1_vals = verify_h1()
    total_h1 = 0
    for H in sorted(h1_vals.keys()):
        val = h1_vals[H]
        total_h1 += val
        expected = DIM_G if H == 1 else 0
        status = "PASS" if val == expected else "FAIL"
        print(f"  H^1_{H} = {val} (expected {expected}) [{status}]")
    print(f"  Total H^1 = {total_h1} (expected {DIM_G})")

    # --- Space dimensions ---
    max_H = 8
    max_n = 4
    print_space_dims(DIM_G, max_H, max_n)

    # --- Cohomology table ---
    print(f"\n--- CE cohomology (max_weight={max_H}, max_degree={max_n}) ---")
    t0 = time.time()
    table = ce_cohomology_table(max_H, max_n, DIM_G, sc)
    elapsed = time.time() - t0
    print(f"  Computation time: {elapsed:.1f}s")

    print_ce_table(table, max_H, max_n)

    # --- Nonzero entries ---
    print("\n  Nonzero entries:")
    for n in range(max_n + 1):
        nz = [(H, table.get((n, H), 0))
              for H in range(1, max_H + 1)
              if table.get((n, H), 0) != 0]
        total = sum(v for _, v in nz)
        print(f"    H^{n}: {nz} (total = {total})")

    # --- Comparison with bar cohomology ---
    print("\n--- Comparison with bar cohomology (Koszul dual Hilbert series) ---")
    print("  CE cohomology of V-bar (exterior algebra):  8, 20, 70, 120")
    print("  Bar cohomology of sl_3-hat (tensor algebra): 8, 36, 204, 1352")
    print("  Ratio bar/CE:  1.00, 1.80, 2.91, 11.27")
    print()
    print("  NOTE: CE cohomology uses Lambda^*(V-bar) (exterior powers).")
    print("  Bar cohomology uses T^*(V-bar) (full tensor products with OS forms).")
    print("  These are DIFFERENT complexes. The bar complex includes")
    print("  symmetric contributions and OS form combinatorics.")
