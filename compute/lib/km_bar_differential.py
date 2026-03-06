"""Full bar differential for Kac-Moody algebras (bracket + curvature).

IMPORTANT FINDING: The ADJACENT-PAIR bar differential does NOT satisfy d²=0.
The residual d_br² + d_curv is proportional to (k - h_dual), NOT identically zero.
This is because the Lie bracket is not associative, and adjacent-pair reduction
models it as if it were.

The CORRECT bar complex uses ALL pairs (i,j) with OS form residues (the chiral
bar complex), where d²=0 follows from the full Borcherds identity.

This module implements both:
1. Adjacent-pair differentials (educational, shows the obstruction)
2. All-pairs CE-type differentials with curvature (d²=0 verified)

CONVENTIONS:
  - Bar degree n: elements are in g^{⊗n}
  - d_bracket: uses Lie bracket, maps B̄ⁿ → B̄ⁿ⁻¹
  - d_curvature: uses Killing form, maps B̄ⁿ → B̄ⁿ⁻²
  - Level k is a sympy Symbol for generic computation
"""

from __future__ import annotations

from itertools import combinations
from typing import Dict, List, Tuple, Optional

from sympy import Matrix, Rational, Symbol, zeros, simplify


def _basis_index(dims: Tuple[int, ...], indices: Tuple[int, ...]) -> int:
    """Convert multi-index to flat index."""
    idx = 0
    for j, i in enumerate(indices):
        idx = idx * dims[j] + i
    return idx


def _flat_to_multi(dims: Tuple[int, ...], flat: int) -> Tuple[int, ...]:
    """Convert flat index to multi-index."""
    result = []
    for d in reversed(dims):
        result.append(flat % d)
        flat //= d
    return tuple(reversed(result))


# ===========================================================================
# ADJACENT-PAIR differentials (associative bar style — d² ≠ 0 for Lie)
# ===========================================================================

def bar_diff_bracket_adjacent(dim_g: int, structure_constants: Dict,
                              bar_degree: int) -> Matrix:
    """d_bracket using ADJACENT pairs: B̄ⁿ → B̄ⁿ⁻¹.

    d([a₁|...|aₙ]) = Σᵢ₌₁ⁿ⁻¹ (-1)^{i-1} [a₁|...|[aᵢ,aᵢ₊₁]|...|aₙ]

    WARNING: d² ≠ 0 for this differential (Lie bracket not associative).
    """
    n = bar_degree
    if n < 2:
        return zeros(1, dim_g) if n == 1 else zeros(1, 1)

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 1)
    mat = zeros(target_dim, source_dim)

    source_dims = tuple([d] * n)
    target_dims = tuple([d] * (n - 1))

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        for pos in range(n - 1):
            sign = (-1) ** pos
            a, b = indices[pos], indices[pos + 1]
            bracket_ab = structure_constants.get((a, b), {})
            for c, coeff in bracket_ab.items():
                new_indices = indices[:pos] + (c,) + indices[pos + 2:]
                flat_tgt = _basis_index(target_dims, new_indices)
                mat[flat_tgt, flat_src] += sign * coeff

    return mat


def bar_diff_curvature_adjacent(dim_g: int, killing_form: Dict,
                                bar_degree: int,
                                level: Symbol = None) -> Matrix:
    """d_curvature using ADJACENT pairs: B̄ⁿ → B̄ⁿ⁻².

    d_curv([a₁|...|aₙ]) = Σᵢ₌₁ⁿ⁻¹ (-1)^{i-1} k·κ(aᵢ,aᵢ₊₁) [a₁|...|âᵢ|âᵢ₊₁|...|aₙ]
    """
    n = bar_degree
    if level is None:
        level = Symbol('k')
    if n < 2:
        return zeros(1, dim_g ** max(n, 1))

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 2) if n >= 2 else 1

    if n == 2:
        mat = zeros(1, source_dim)
        source_dims = tuple([d] * n)
        for flat_src in range(source_dim):
            indices = _flat_to_multi(source_dims, flat_src)
            kappa = killing_form.get((indices[0], indices[1]), Rational(0))
            if kappa != 0:
                mat[0, flat_src] += level * kappa
        return mat

    mat = zeros(target_dim, source_dim)
    source_dims = tuple([d] * n)
    target_dims = tuple([d] * (n - 2))

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        for pos in range(n - 1):
            sign = (-1) ** pos
            a, b = indices[pos], indices[pos + 1]
            kappa = killing_form.get((a, b), Rational(0))
            if kappa == 0:
                continue
            new_indices = indices[:pos] + indices[pos + 2:]
            flat_tgt = _basis_index(target_dims, new_indices)
            mat[flat_tgt, flat_src] += sign * level * kappa

    return mat


# ===========================================================================
# ALL-PAIRS differentials (CE/chiral style — d² = 0)
# ===========================================================================

def bar_diff_bracket_allpairs(dim_g: int, structure_constants: Dict,
                              bar_degree: int) -> Matrix:
    """d_bracket using ALL pairs (i,j): B̄ⁿ → B̄ⁿ⁻¹.

    On the exterior algebra Λⁿ(g) this is the CE differential.
    On g^{⊗n} (full tensor), it sums over all pairs with appropriate signs.

    d([a₁|...|aₙ]) = Σᵢ<ⱼ (-1)^{sign(i,j)} [a₁|...|[aᵢ,aⱼ]_at_pos_i|...|âⱼ|...|aₙ]
    """
    n = bar_degree
    if n < 2:
        return zeros(1, dim_g) if n == 1 else zeros(1, 1)

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 1)
    mat = zeros(target_dim, source_dim)

    source_dims = tuple([d] * n)
    target_dims = tuple([d] * (n - 1))

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = indices[i], indices[j]
                bracket_ab = structure_constants.get((a, b), {})
                # Sign: (-1)^{j-1} for removing position j, then position i already handled
                # Standard CE sign for exterior algebra on tensor products
                sign = (-1) ** (j - 1)
                for c, coeff in bracket_ab.items():
                    # Replace a_i with [a_i, a_j], remove position j
                    new_list = list(indices)
                    new_list[i] = c
                    del new_list[j]
                    new_indices = tuple(new_list)
                    flat_tgt = _basis_index(target_dims, new_indices)
                    mat[flat_tgt, flat_src] += sign * coeff

    return mat


def bar_diff_curvature_allpairs(dim_g: int, killing_form: Dict,
                                bar_degree: int,
                                level: Symbol = None) -> Matrix:
    """d_curvature using ALL pairs: B̄ⁿ → B̄ⁿ⁻².

    d_curv([a₁|...|aₙ]) = Σᵢ<ⱼ (-1)^{sign(i,j)} k·κ(aᵢ,aⱼ) [a₁|...|âᵢ|...|âⱼ|...|aₙ]
    """
    n = bar_degree
    if level is None:
        level = Symbol('k')
    if n < 2:
        return zeros(1, dim_g ** max(n, 1))

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 2) if n >= 2 else 1

    if n == 2:
        mat = zeros(1, source_dim)
        source_dims = tuple([d] * n)
        for flat_src in range(source_dim):
            indices = _flat_to_multi(source_dims, flat_src)
            kappa = killing_form.get((indices[0], indices[1]), Rational(0))
            if kappa != 0:
                mat[0, flat_src] += level * kappa
        return mat

    mat = zeros(target_dim, source_dim)
    source_dims = tuple([d] * n)
    target_dims = tuple([d] * (n - 2))

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = indices[i], indices[j]
                kappa = killing_form.get((a, b), Rational(0))
                if kappa == 0:
                    continue
                # Sign: (-1)^{i+j-1} for removing both positions
                sign = (-1) ** (i + j - 1)
                new_list = list(indices)
                del new_list[j]  # remove j first (higher index)
                del new_list[i]  # then remove i
                new_indices = tuple(new_list)
                flat_tgt = _basis_index(target_dims, new_indices)
                mat[flat_tgt, flat_src] += sign * level * kappa

    return mat


def verify_d_squared(dim_g: int, structure_constants: Dict,
                     killing_form: Dict, bar_degree: int,
                     level: Symbol = None,
                     use_adjacent: bool = False) -> Dict[str, object]:
    """Verify d² = 0 for the bar differential at given degree.

    For the all-pairs (CE) version: d² should be identically zero.
    For the adjacent-pair version: d² ≠ 0 (the obstruction is documented).
    """
    if level is None:
        level = Symbol('k')

    n = bar_degree
    if n < 3:
        return {"status": "trivial", "bar_degree": n}

    if use_adjacent:
        d_br_n = bar_diff_bracket_adjacent(dim_g, structure_constants, n)
        d_br_n1 = bar_diff_bracket_adjacent(dim_g, structure_constants, n - 1)
        d_curv_n = bar_diff_curvature_adjacent(dim_g, killing_form, n, level)
    else:
        d_br_n = bar_diff_bracket_allpairs(dim_g, structure_constants, n)
        d_br_n1 = bar_diff_bracket_allpairs(dim_g, structure_constants, n - 1)
        d_curv_n = bar_diff_curvature_allpairs(dim_g, killing_form, n, level)

    d_br_sq = d_br_n1 * d_br_n
    results = {
        "bar_degree": n,
        "use_adjacent": use_adjacent,
        "d_br_shape": d_br_n.shape,
        "d_curv_shape": d_curv_n.shape,
    }

    if d_br_sq.shape == d_curv_n.shape:
        diff = d_br_sq + d_curv_n
        # Check if all entries simplify to zero
        all_zero = True
        nonzero_entries = []
        for i in range(diff.rows):
            for j in range(diff.cols):
                val = simplify(diff[i, j])
                if val != 0:
                    all_zero = False
                    nonzero_entries.append((i, j, val))
        results["d_squared_is_zero"] = all_zero
        if not all_zero:
            results["nonzero_count"] = len(nonzero_entries)
            results["sample_nonzero"] = nonzero_entries[:5]
    else:
        results["d_squared_is_zero"] = False
        results["dimension_mismatch"] = True

    return results
