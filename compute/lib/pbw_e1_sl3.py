"""PBW spectral sequence E₁ page for sl₃-hat bar cohomology.

Computes dim E₁^{p,0}_H = dim(S^p(V̄)_H)^g for the PBW spectral sequence
of the KM algebra sl₃-hat at generic level.

Mathematical setup:
  V̄ = ⊕_{h≥1} g_h where g_h ≅ sl₃ (adjoint rep at each mode).
  S^p(V̄)_H = elements of symmetric-algebra degree p at conformal weight H.
  The g = sl₃ zero-mode action is diagonal; invariants = ker of all ad(J^a_0).

  E₁^{p,q} = H^q(g; S^p(V̄)) = H^q(g;k) ⊗ (S^p(V̄))^g
  (since g is semisimple, H^q(g; V_λ) = 0 for non-trivial finite-dim V_λ).

  For total degree n = p+q ≤ 7 (< dim sl₃ = 8), only q=0 contributes.
  MC1 (chiral Koszulness) gives E₂ = E_∞, so:
  H^n = Σ_H E₂^{n,0}_H = Σ_H ker(d₁)/im(d₁) at each weight H.

Key optimization: the invariant dimension of
  (S^{m₁}(g) ⊗ S^{m₂}(g) ⊗ ... ⊗ S^{m_k}(g))^g
depends only on the PARTITION TYPE (m₁,...,m_k), not on the specific weights.

Two computation methods:
  1. Direct (Kronecker product): exact, for types with total dim ≤ ~10000.
  2. Weyl integration: numerical (rounds to integer), scales to any dimension.

References:
  - prop:sl3-pbw-ss (detailed_computations.tex)
  - thm:pbw-koszulness-criterion (higher_genus.tex)
  - sl3_casimir_decomp.py (Casimir decomposition data)
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations_with_replacement
from math import prod
from typing import Dict, List, Tuple

import numpy as np

from compute.lib.sl3_bar import DIM_G, sl3_structure_constants


# ============================================================
# Weyl integration for SU(3) — the scalable method
# ============================================================

def _adjoint_eigenvalues_su3(theta1: float, theta2: float) -> np.ndarray:
    """Eigenvalues of the adjoint representation on the SU(3) maximal torus.

    The torus element is diag(e^{iθ₁}, e^{iθ₂}, e^{-i(θ₁+θ₂)}).
    Adjoint eigenvalues = e^{iα(θ)} for roots α, plus 1,1 for Cartan.

    Returns array of 8 complex eigenvalues.
    """
    t1, t2, t3 = theta1, theta2, -(theta1 + theta2)
    roots = [t1 - t2, t2 - t1,   # ±α₁
             t2 - t3, t3 - t2,   # ±α₂
             t1 - t3, t3 - t1]   # ±(α₁+α₂)
    eigenvalues = np.array([np.exp(1j * r) for r in roots] + [1.0, 1.0],
                           dtype=np.complex128)
    return eigenvalues


def _weyl_density_su3(theta1: float, theta2: float) -> float:
    """Squared Weyl denominator |Δ(θ)|² for SU(3).

    |Δ|² = ∏_{α>0} |e^{iα(θ)} - 1|² = ∏_{α>0} (2 - 2cos(α(θ)))
    Positive roots: θ₁-θ₂, θ₁+2θ₂, 2θ₁+θ₂
    """
    t1, t2, t3 = theta1, theta2, -(theta1 + theta2)
    pos_roots = [t1 - t2, t2 - t3, t1 - t3]
    density = 1.0
    for alpha in pos_roots:
        density *= (2.0 - 2.0 * np.cos(alpha))
    return density


def _sym_power_character(eigenvalues: np.ndarray, degree: int) -> complex:
    """Character of the m-th symmetric power: χ_{S^m(V)}(g).

    Uses the Newton identity / recursion:
      χ_{S^m}(g) = (1/m) Σ_{k=1}^{m} p_k × χ_{S^{m-k}}(g)
    where p_k = Σ_i λ_i^k (power sum symmetric function).
    """
    if degree == 0:
        return 1.0 + 0j
    # Precompute power sums
    power_sums = np.array([np.sum(eigenvalues ** k) for k in range(1, degree + 1)],
                          dtype=np.complex128)
    # Newton recursion
    chi = np.zeros(degree + 1, dtype=np.complex128)
    chi[0] = 1.0
    for m in range(1, degree + 1):
        chi[m] = sum(power_sums[k - 1] * chi[m - k] for k in range(1, m + 1)) / m
    return chi[degree]


def invariant_dim_weyl(partition_type: Tuple[int, ...],
                       n_grid: int = 200) -> int:
    """Compute dim(S^{m₁}(g) ⊗ ... ⊗ S^{m_k}(g))^g via Weyl integration.

    Uses the formula:
      dim(M)^G = (1/(2π)^r × |W|) ∫_T χ_M(t) |Δ(t)|² dt

    For SU(3): r=2, |W|=6, T = (θ₁,θ₂) ∈ [0,2π)².

    The character of the tensor product = product of individual characters.
    """
    dtheta = (2 * np.pi / n_grid)
    theta_vals = np.linspace(0, 2 * np.pi, n_grid, endpoint=False)

    integral = 0.0
    for i in range(n_grid):
        for j in range(n_grid):
            t1, t2 = theta_vals[i], theta_vals[j]
            eigs = _adjoint_eigenvalues_su3(t1, t2)
            density = _weyl_density_su3(t1, t2)

            # Product of symmetric power characters
            chi_product = 1.0 + 0j
            for m in partition_type:
                chi_product *= _sym_power_character(eigs, m)

            integral += (chi_product * density).real

    # Normalization: (dθ₁ dθ₂) / ((2π)² × |W|)
    result = integral * dtheta ** 2 / (4 * np.pi ** 2 * 6)
    return int(round(result))


# ============================================================
# Direct computation (Kronecker product) — exact, for small types
# ============================================================

def _build_adjoint_matrices() -> np.ndarray:
    """Build 8 adjoint matrices ad(e_i) for sl₃, shape (8, 8, 8).

    ad_mats[i, j, k] = coefficient of e_j in [e_i, e_k].
    """
    sc = sl3_structure_constants()
    ad = np.zeros((DIM_G, DIM_G, DIM_G), dtype=np.float64)
    for (i, k), products in sc.items():
        for j, coeff in products.items():
            ad[i, j, k] = float(coeff)
    return ad


_AD_MATS = None


def ad_matrices() -> np.ndarray:
    global _AD_MATS
    if _AD_MATS is None:
        _AD_MATS = _build_adjoint_matrices()
    return _AD_MATS


def sym_power_basis(dim: int, degree: int) -> List[Tuple[int, ...]]:
    """Sorted basis monomials for S^degree(k^dim)."""
    return list(combinations_with_replacement(range(dim), degree))


def _sym_power_action_matrices(degree: int) -> List[np.ndarray]:
    """Build adjoint action matrices on S^degree(g) for each generator.

    Returns list of 8 matrices, each of size (dim S^m(g)) × (dim S^m(g)).
    """
    ad = ad_matrices()
    basis = sym_power_basis(DIM_G, degree)
    dim = len(basis)
    idx_map = {b: i for i, b in enumerate(basis)}

    mats = []
    for a in range(DIM_G):
        mat = np.zeros((dim, dim), dtype=np.float64)
        for col, monomial in enumerate(basis):
            for pos in range(degree):
                color = monomial[pos]
                for j in range(DIM_G):
                    coeff = ad[a, j, color]
                    if coeff == 0:
                        continue
                    new_mon = list(monomial)
                    new_mon[pos] = j
                    new_mon_sorted = tuple(sorted(new_mon))
                    row = idx_map.get(new_mon_sorted)
                    if row is not None:
                        mat[row, col] += coeff
        mats.append(mat)
    return mats


# Cache for factor action matrices
_FACTOR_CACHE: Dict[int, List[np.ndarray]] = {}


def _get_factor_matrices(degree: int) -> List[np.ndarray]:
    """Cached action matrices for S^degree(g)."""
    if degree not in _FACTOR_CACHE:
        _FACTOR_CACHE[degree] = _sym_power_action_matrices(degree)
    return _FACTOR_CACHE[degree]


def invariant_dim_direct(partition_type: Tuple[int, ...]) -> int:
    """Dimension of (S^{m₁}(g) ⊗ ... ⊗ S^{m_k}(g))^g via direct computation.

    Uses Kronecker products. Memory-safe for total dim ≤ ~10000.
    """
    k = len(partition_type)
    if k == 0:
        return 1

    # Get action matrices for each factor
    all_factor_mats = [_get_factor_matrices(m) for m in partition_type]
    factor_dims = [len(sym_power_basis(DIM_G, m)) for m in partition_type]
    total_dim = prod(factor_dims)

    if total_dim > 2000:
        raise MemoryError(
            f"Total dim {total_dim} too large for direct method "
            f"(stack would be {8*total_dim**2*8/1e9:.1f} GB). "
            f"Use invariant_dim_weyl instead."
        )

    # Build stacked action matrix
    stack = np.zeros((DIM_G * total_dim, total_dim), dtype=np.float64)

    for a in range(DIM_G):
        action_a = np.zeros((total_dim, total_dim), dtype=np.float64)
        for f_idx in range(k):
            term = np.array([[1.0]])
            for g_idx in range(k):
                if g_idx == f_idx:
                    term = np.kron(term, all_factor_mats[g_idx][a])
                else:
                    term = np.kron(term, np.eye(factor_dims[g_idx]))
            action_a += term
        stack[a * total_dim: (a + 1) * total_dim, :] = action_a

    rank = np.linalg.matrix_rank(stack, tol=1e-8)
    return total_dim - rank


# ============================================================
# Unified interface
# ============================================================

_INVARIANT_DIM_CACHE: Dict[Tuple[int, ...], int] = {}
# Memory for direct method scales as O(8 * total_dim^2 * 8 bytes).
# At total_dim = 1500 that is ~280 MB, which is acceptable.
# S^6(sl_3) has dim 1716, so m <= 5 uses direct; m >= 6 uses Weyl.
_DIRECT_THRESHOLD = 1500


def invariant_dim_partition_type(partition_type: Tuple[int, ...]) -> int:
    """Dimension of (S^{m₁}(g) ⊗ ... ⊗ S^{m_k}(g))^g for g = sl₃.

    Automatically chooses direct (exact) or Weyl (numerical) method.
    """
    if not partition_type:
        return 1

    factor_dims = [len(sym_power_basis(DIM_G, m)) for m in partition_type]
    total_dim = prod(factor_dims)

    if total_dim <= _DIRECT_THRESHOLD:
        result = invariant_dim_direct(partition_type)
    else:
        # Use Weyl with high precision grid
        result = invariant_dim_weyl(partition_type, n_grid=300)

    return result


def invariant_dim_cached(ptype: Tuple[int, ...]) -> int:
    """Cached version of invariant_dim_partition_type."""
    if ptype not in _INVARIANT_DIM_CACHE:
        _INVARIANT_DIM_CACHE[ptype] = invariant_dim_partition_type(ptype)
    return _INVARIANT_DIM_CACHE[ptype]


# ============================================================
# Partition enumeration
# ============================================================

def partitions_of(n: int, num_parts: int, min_part: int = 1) -> List[Tuple[int, ...]]:
    """All partitions of n into exactly num_parts parts, each ≥ min_part.

    Returns sorted tuples (h₁, h₂, ...) with h₁ ≤ h₂ ≤ ...
    """
    if num_parts == 0:
        return [()] if n == 0 else []
    if num_parts == 1:
        return [(n,)] if n >= min_part else []
    result = []
    for first in range(min_part, n // num_parts + 1):
        for rest in partitions_of(n - first, num_parts - 1, first):
            result.append((first,) + rest)
    return result


def partition_type(partition: Tuple[int, ...]) -> Tuple[int, ...]:
    """Extract the multiplicity type from a partition.

    Example: (1, 1, 2, 3) → (2, 1, 1) — two 1's, one 2, one 3.
    Returns sorted descending.
    """
    counts = Counter(partition)
    return tuple(sorted(counts.values(), reverse=True))


def count_partitions_by_type(
    weight: int, num_parts: int
) -> Dict[Tuple[int, ...], int]:
    """Count partitions of `weight` into `num_parts` parts (≥1), grouped by type."""
    result: Dict[Tuple[int, ...], int] = {}
    for p in partitions_of(weight, num_parts):
        t = partition_type(p)
        result[t] = result.get(t, 0) + 1
    return result


def all_partition_types(pbw_degree: int) -> List[Tuple[int, ...]]:
    """All partition types (multiplicity signatures) at a given PBW degree.

    Example: pbw_degree=4 → [(4,), (3,1), (2,2), (2,1,1), (1,1,1,1)].
    """
    def int_partitions(n, max_part=None):
        if max_part is None:
            max_part = n
        if n == 0:
            yield ()
            return
        for p in range(min(n, max_part), 0, -1):
            for rest in int_partitions(n - p, p):
                yield (p,) + rest
    return list(int_partitions(pbw_degree))


# ============================================================
# E₁ page dimensions
# ============================================================

def e1_dim(pbw_degree: int, weight: int) -> int:
    """Dimension of E₁^{pbw_degree, 0} at conformal weight H.

    This is dim(S^p(V̄)_H)^g where p = pbw_degree, H = weight.
    """
    type_counts = count_partitions_by_type(weight, pbw_degree)
    total = 0
    for ptype, count in type_counts.items():
        inv_dim = invariant_dim_cached(ptype)
        total += count * inv_dim
    return total


def e1_dims_table(
    max_pbw: int, max_weight: int
) -> Dict[Tuple[int, int], int]:
    """Compute E₁^{p,0}_H for p = 1..max_pbw, H = p..max_weight."""
    result = {}
    for p in range(1, max_pbw + 1):
        for H in range(p, max_weight + 1):
            d = e1_dim(p, H)
            result[(p, H)] = d
    return result


def e1_total_through_weight(pbw_degree: int, max_weight: int) -> int:
    """Total dimension of E₁^{p,0} = Σ_H E₁^{p,0}_H through max_weight."""
    return sum(e1_dim(pbw_degree, H) for H in range(pbw_degree, max_weight + 1))


def invariant_dims_all_types(pbw_degree: int) -> Dict[Tuple[int, ...], int]:
    """Compute invariant dimensions for all partition types at a given PBW degree."""
    types = all_partition_types(pbw_degree)
    return {t: invariant_dim_cached(t) for t in types}


# ============================================================
# Cross-validation
# ============================================================

def verify_basic_facts() -> Dict[str, bool]:
    """Verify known invariant dimensions."""
    results = {}

    # S^m(g)^g = number of monomials C₂^a C₃^b with 2a+3b = m
    chevalley = {1: 0, 2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 1, 8: 2, 9: 2}
    for m, expected in chevalley.items():
        actual = invariant_dim_cached((m,))
        results[f"S^{m}(g)^g = {expected}"] = (actual == expected)

    # (g⊗g)^g = 1 (Killing form)
    actual = invariant_dim_cached((1, 1))
    results["(g⊗g)^g = 1"] = (actual == 1)

    # (g⊗g⊗g)^g = 2 (from Casimir data)
    actual = invariant_dim_cached((1, 1, 1))
    results["(g^⊗3)^g = 2"] = (actual == 2)

    # (g^⊗4)^g = 8 (from Casimir data)
    actual = invariant_dim_cached((1, 1, 1, 1))
    results["(g^⊗4)^g = 8"] = (actual == 8)

    # E₁^{1,0}_H = 0 for all H (g^g = 0 for simple g)
    for H in range(1, 5):
        d = e1_dim(1, H)
        results[f"E1^(1,0)_{H} = 0"] = (d == 0)

    # E₁^{2,0}_2 = 1 (Casimir at weight 2)
    results["E1^(2,0)_2 = 1"] = (e1_dim(2, 2) == 1)

    return results


def cross_validate_with_spectral_sequence(
    min_weight: int = 1,
    max_weight: int = 8,
) -> Dict[str, bool]:
    """Verify sum over PBW degrees matches adjoint_invariant_dim.

    At each weight H: Σ_p E₁^{p,0}_H should equal the total invariant dim
    in the weight-H space of S*(V̄).
    """
    from compute.lib.spectral_sequence import adjoint_invariant_dim
    from compute.lib.sl3_bar import sl3_structure_constants

    sc = sl3_structure_constants()
    # Convert to the format expected by adjoint_invariant_dim
    sc_int = {}
    for (a, b), prods in sc.items():
        sc_int[(a, b)] = {k: v for k, v in prods.items()}

    results = {}
    for H in range(min_weight, max_weight + 1):
        expected = adjoint_invariant_dim(DIM_G, sc_int, H)
        # Sum over PBW degrees 1 to H
        actual = sum(e1_dim(p, H) for p in range(1, H + 1))
        results[f"H={H}: Σ_p E1^(p,0) = {expected}"] = (actual == expected)

    return results


# ============================================================
# Summary output
# ============================================================

def print_e1_summary(max_pbw: int = 5, max_weight: int = 15) -> None:
    """Print summary of E₁ page dimensions."""
    print(f"\nE₁^{{p,0}}_H dimensions for sl₃-hat PBW spectral sequence")
    print(f"{'p\\H':>6}", end="")
    for H in range(1, max_weight + 1):
        print(f"{H:>5}", end="")
    print("  | total")
    print("-" * (6 + 5 * max_weight + 10))

    for p in range(1, max_pbw + 1):
        print(f"{p:>6}", end="")
        total = 0
        for H in range(1, max_weight + 1):
            if H < p:
                print(f"{'':>5}", end="")
            else:
                d = e1_dim(p, H)
                total += d
                print(f"{d:>5}", end="")
        print(f"  | {total}")

    print("\nInvariant dims by partition type:")
    for p in range(1, max_pbw + 1):
        types = invariant_dims_all_types(p)
        print(f"  p={p}: {dict(types)}")


if __name__ == "__main__":
    print("=== Basic verification ===")
    for k, v in verify_basic_facts().items():
        print(f"  {'OK' if v else 'FAIL'}: {k}")
    print()
    print_e1_summary(max_pbw=4, max_weight=12)
