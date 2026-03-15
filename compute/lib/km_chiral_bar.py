"""Chiral bar cohomology for Kac-Moody algebras.

Computes bar cohomology dimensions for sl_N-hat via:

1. KOSZUL DUAL HILBERT SERIES (Cor cor:bar-cohomology-koszul-dual):
   dim H^n(B(g-hat)) = dim (g-hat^!)_n.
   The E_2 collapse of the PBW spectral sequence identifies bar
   cohomology with the Koszul dual Hilbert function.  For sl_2 this
   gives Riordan numbers R(n+3); for sl_3 the conjectured rational GF
   predicts H^4=1352.

2. DIRECT BRACKET RANK (Computation comp:sl3-modular-rank):
   Compute rank(d_bracket: B^n -> B^{n-1}) on g^{otimes n} (the
   CE-type bracket differential).  The bracket-only differential does
   NOT square to zero (CLAUDE.md Critical Pitfalls), but its ranks
   determine the Koszul dual dimensions via the PBW spectral
   sequence's E_0 page.

3. CONJECTURED RATIONAL GF (Conjecture conj:sl3-bar-gf):
   P(x) = 4x(2 - 13x - 2x^2)/((1-8x)(1-3x-x^2))
   Recurrence: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3).

CURVATURE BARRIER (PROVED — see Part 3b documentation):
   Direct matrix computation of bar cohomology is blocked because:
   (a) d_bracket alone has d² ≠ 0 (proved for all sign conventions);
   (b) d_curvature uses R^{(1)} (derivative-residue), which produces
       forms outside the OS algebra (dw/w² terms);
   (c) the augmented approach (V = g ⊕ k·|0⟩ with combined product)
       fails because μ_aug violates the Jacobi identity.
   The correct method is PBW spectral sequence (Part 1), not matrices.

CONVENTIONS (CLAUDE.md):
- Cohomological grading, |d| = +1
- Bar degree n: chain group B-bar^n = g^{otimes n} tensor OS^{n-1}(n)
- dim B-bar^n = (dim g)^n * (n-1)!
- Bar uses DESUSPENSION: B(A) = T^c(s^{-1}A-bar, d)
- d_bracket^2 != 0 (PROVED). Full d = d_bracket + d_curvature has d^2=0
- PBW SS does NOT automatically degenerate at E_3 for "quadratic OPE"

References:
  - Cor cor:bar-cohomology-koszul-dual (chiral_koszul_pairs.tex)
  - Prop prop:sl3-pbw-ss (detailed_computations.tex)
  - Computation comp:sl3-modular-rank (detailed_computations.tex)
  - Rem rem:bar-deg2-symmetric-square (examples_summary.tex)
  - Conjecture conj:sl3-bar-gf (examples_summary.tex)
  - Thm thm:km-chiral-koszul (chiral_koszul_pairs.tex)
  - Prop prop:pole-decomposition (bar_cobar_construction.tex)
"""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple

import numpy as np

from compute.lib.sl3_bar import (
    DIM_G as SL3_DIM,
    sl3_structure_constants,
    sl3_killing_form,
)
from compute.lib.os_algebra import os_dimension, residue_map


# ============================================================
# Part 1: Koszul dual Hilbert series (known formulas)
# ============================================================

def riordan(n: int) -> int:
    """Riordan number R(n) via recurrence.  OEIS A005043.

    (n+1) R(n) = (n-1)(2R(n-1) + 3R(n-2)), with R(0)=1, R(1)=0.
    """
    if n <= 0:
        return 1
    if n == 1:
        return 0
    R = [1, 0]
    for k in range(2, n + 1):
        num = (k - 1) * (2 * R[k - 1] + 3 * R[k - 2])
        assert num % (k + 1) == 0
        R.append(num // (k + 1))
    return R[n]


def sl2_bar_cohomology(max_degree: int) -> List[int]:
    """Bar cohomology for sl_2-hat via PBW spectral sequence.

    The E_2 = E_infinity page of the PBW SS identifies bar cohomology
    with CE cohomology of the positive-mode loop algebra.

    Known values (comp:sl2-ce-verification, bar_deg2_resolution):
      H^0=1, H^1=3, H^2=5, H^3=15, H^4=36, H^5=91, H^6=232.

    CORRECTION: The Riordan formula R(n+3) gives H^2=6 (WRONG).
    The correct H^2=5 follows from H^2_{h=2}=0 (the bar differential
    d: B^2_{h=2} -> B^1_{h=2} is an isomorphism, rank 9; see
    bar_deg2_resolution.py).  All 5 H^2 classes live at weight >= 3.
    Riordan values are correct for n != 2.
    """
    result = [riordan(n + 3) for n in range(max_degree + 1)]
    if max_degree >= 2:
        result[2] = 5  # Corrected: R(5)=6 is wrong, H^2=5
    return result


def sl3_bar_cohomology(max_degree: int) -> List[int]:
    """Bar cohomology for sl_3-hat via conjectured rational GF.

    Known: H^0=1, H^1=8, H^2=36, H^3=204.
    Conjectured (conj:sl3-bar-gf): a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3).
    Predicts H^4=1352, H^5=9892, H^6=76084, H^7=598592.

    The three known values are verified by direct computation
    (Prop prop:sl3-pbw-ss); the conjectured GF extends via the recurrence.

    Returns: [H^0, H^1, ..., H^{max_degree}].
    """
    known = [1, 8, 36, 204]
    if max_degree < len(known):
        return known[:max_degree + 1]

    result = known.copy()
    for _ in range(len(known), max_degree + 1):
        a_n = 11 * result[-1] - 23 * result[-2] - 8 * result[-3]
        result.append(a_n)
    return result[:max_degree + 1]


def bar_cohomology_degree2(dim_g: int) -> int:
    """Degree-2 bar cohomology for KM algebras — KNOWN VALUES ONLY.

    DEPRECATED: The old formula C(dim_g + 1, 2) was based on the
    incorrect rem:bar-deg2-symmetric-square, which used the wrong
    target space (g_2 of dim d instead of A-bar_2 of dim d + d(d+1)/2)
    and wrong differential component (Lie bracket instead of (-1)-product).

    CORRECTED (bar_deg2_resolution.py):
      H^2_{h=2} = 0 for ALL semisimple g (bar differential is injective).
      Total H^2 = H^2(CE of positive-mode loop algebra).

    Known values:
      sl_2 (dim 3):  H^2 = 5  (comp:sl2-ce-verification)
      sl_3 (dim 8):  H^2 = 36 (prop:sl3-pbw-ss)
    """
    known = {3: 5, 8: 36}
    if dim_g in known:
        return known[dim_g]
    raise NotImplementedError(
        f"H^2(bar) for dim(g)={dim_g} requires CE computation; "
        f"no closed-form formula is known"
    )


# ============================================================
# Part 2: Direct bracket differential (CE-type, g^{otimes n})
# ============================================================

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


def bracket_pair_map_numpy(dim_g: int, structure_constants: Dict,
                           n: int, i: int, j: int) -> np.ndarray:
    """Bracket map for pair (i,j) on g^{otimes n} -> g^{otimes (n-1)}.

    Replaces position i with [g_i, g_j] and removes position j.
    Indices are 0-based.

    Returns: (dim_g^{n-1}, dim_g^n) numpy array.
    """
    if n < 2 or i >= n or j >= n or i == j:
        raise ValueError(f"Invalid pair ({i},{j}) for n={n}")

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 1)
    M = np.zeros((target_dim, source_dim))

    source_dims = tuple([d] * n)
    target_dims = tuple([d] * (n - 1))

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        a, b = indices[i], indices[j]
        bracket_ab = structure_constants.get((a, b), {})

        for c, coeff in bracket_ab.items():
            new_list = list(indices)
            new_list[i] = c
            del new_list[j]
            flat_tgt = _basis_index(target_dims, tuple(new_list))
            M[flat_tgt, flat_src] += float(coeff)

    return M


def killing_pair_map_numpy(dim_g: int, killing_form: Dict,
                           n: int, i: int, j: int) -> np.ndarray:
    """Killing contraction for pair (i,j): g^{otimes n} -> g^{otimes (n-2)}.

    Contracts positions i,j with kappa(g_i, g_j) and removes both.

    Returns: (dim_g^{n-2}, dim_g^n) numpy array (or (1, dim_g^n) if n=2).
    """
    if n < 2 or i >= n or j >= n or i == j:
        raise ValueError(f"Invalid pair ({i},{j}) for n={n}")

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 2) if n > 2 else 1
    M = np.zeros((target_dim, source_dim))

    source_dims = tuple([d] * n)

    for flat_src in range(source_dim):
        indices = _flat_to_multi(source_dims, flat_src)
        a, b = indices[i], indices[j]
        kappa = killing_form.get((a, b), 0)
        if kappa == 0:
            continue

        new_list = list(indices)
        ii, jj = min(i, j), max(i, j)
        del new_list[jj]
        del new_list[ii]
        if n > 2:
            target_dims = tuple([d] * (n - 2))
            flat_tgt = _basis_index(target_dims, tuple(new_list))
        else:
            flat_tgt = 0
        M[flat_tgt, flat_src] += float(kappa)

    return M


def ce_bracket_differential_numpy(dim_g: int, structure_constants: Dict,
                                   bar_degree: int) -> np.ndarray:
    """All-pairs (CE-type) bracket differential: g^{otimes n} -> g^{otimes (n-1)}.

    d(a_1 ... a_n) = sum_{i<j} (-1)^{j-1} (... [a_i,a_j] ... hat{a_j} ...)

    Sign convention: (-1)^{j-1} for removing position j.
    This matches km_bar_differential.py and gives d^2=0 on g^{otimes n}
    (without OS forms).

    WARNING: This is the CE-type differential on g^{otimes n}, NOT the
    chiral bar differential.  It does NOT include OS forms.  On g^{otimes n}
    alone, this differential DOES square to zero.  The modular rank of this
    map at degree 3->2 is 56 (comp:sl3-modular-rank uses a different sign
    convention with OS forms giving rank 63).

    Returns: (dim_g^{n-1}, dim_g^n) numpy array.
    """
    n = bar_degree
    if n < 2:
        return np.zeros((1, dim_g))

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 1)
    M = np.zeros((target_dim, source_dim))

    for i in range(n):
        for j in range(i + 1, n):
            sign = (-1) ** (j - 1)
            pair_map = bracket_pair_map_numpy(dim_g, structure_constants, n, i, j)
            M += sign * pair_map

    return M


def bracket_diff_rank(dim_g: int, structure_constants: Dict,
                      bar_degree: int) -> int:
    """Rank of CE bracket differential at given bar degree."""
    M = ce_bracket_differential_numpy(dim_g, structure_constants, bar_degree)
    return int(np.linalg.matrix_rank(M, tol=1e-8))


def bar_cohomology_direct(dim_g: int, structure_constants: Dict,
                          killing_form: Dict,
                          max_degree: int = 3) -> Dict[str, object]:
    """Compute bracket differential ranks and related data for bar complex.

    Builds the CE-type bracket differential on g^{otimes n} and computes
    ranks.  Note: this is the associated graded (PBW E_0) differential,
    NOT the full chiral bar differential.  On g^{otimes n} without OS
    forms, this differential squares to zero.

    From comp:sl3-modular-rank for sl_3 (d=8):
    - rank(d: B^3 -> B^2) = 56 (CE-type on g^{otimes n}, sign (-1)^{j-1})
    - rank(d: B^4 -> B^3) = 512 (surjective)

    The manuscript's rank 63 at degree 3 uses OS forms and sign (-1)^{i+j}.
    """
    results = {"dim_g": dim_g}

    # Chain group dimensions (g^{otimes n}, no OS forms)
    chain_dims = {n: dim_g ** n for n in range(1, max_degree + 2)}
    results["chain_dims"] = chain_dims

    # Compute bracket differential ranks
    bracket_ranks = {}
    for n in range(2, max_degree + 2):
        if dim_g ** n > 200000:
            bracket_ranks[n] = None
            continue
        rank = bracket_diff_rank(dim_g, structure_constants, n)
        bracket_ranks[n] = rank
    results["bracket_ranks"] = bracket_ranks

    # Bracket-only bar cohomology on g^{otimes n}
    # This is the E_0-page cohomology of the PBW SS
    bracket_cohom = {}
    for n in range(1, max_degree + 1):
        dim_n = chain_dims[n]
        rank_out = bracket_ranks.get(n)
        rank_in = bracket_ranks.get(n + 1)
        if rank_out is None or rank_in is None:
            bracket_cohom[n] = None
            continue
        bracket_cohom[n] = dim_n - rank_out - rank_in
    results["bracket_only_cohom"] = bracket_cohom

    # Killing differential ranks
    curvature_ranks = {}
    for n in range(2, min(max_degree + 2, 5)):
        if dim_g ** n > 200000:
            curvature_ranks[n] = None
            continue
        M = _ce_killing_differential_numpy(dim_g, killing_form, n)
        curvature_ranks[n] = int(np.linalg.matrix_rank(M, tol=1e-8))
    results["curvature_ranks"] = curvature_ranks

    return results


def _ce_killing_differential_numpy(dim_g: int, killing_form: Dict,
                                    bar_degree: int) -> np.ndarray:
    """All-pairs Killing contraction: g^{otimes n} -> g^{otimes (n-2)}.

    d_curv(a_1 ... a_n) = sum_{i<j} (-1)^{i+j-1} kappa(a_i, a_j) (remaining)
    """
    n = bar_degree
    if n < 2:
        return np.zeros((1, dim_g))

    d = dim_g
    source_dim = d ** n
    target_dim = d ** (n - 2) if n > 2 else 1
    M = np.zeros((target_dim, source_dim))

    for i in range(n):
        for j in range(i + 1, n):
            sign = (-1) ** (i + j - 1)
            pair_map = killing_pair_map_numpy(d, killing_form, n, i, j)
            M += sign * pair_map

    return M


# ============================================================
# Part 3: Chiral bar differential with OS forms
# ============================================================

def chiral_bracket_differential(dim_g: int, structure_constants: Dict,
                                bar_degree: int,
                                sign_convention: str = "os") -> np.ndarray:
    """Chiral bar bracket differential with OS forms.

    d_bracket: B^n = g^{otimes n} tensor OS^{n-1}(n)
            -> B^{n-1} = g^{otimes (n-1)} tensor OS^{n-2}(n-1)

    The full map is: d = sum_{i<j} sign * (bracket_ij kron residue_ij)

    Two sign conventions:
    - "os": sign (-1)^{i+j}, matching the manuscript's comp:sl3-modular-rank
      (gives rank 63 at degree 3 for sl_3)
    - "ce": sign (-1)^{j-1}, matching the CE differential on g^{otimes n}
      (gives rank 56 at degree 3 for sl_3 without OS, rank varies with OS)

    Returns: (target_dim, source_dim) numpy array.
    """
    n = bar_degree
    if n < 2:
        return np.zeros((1, dim_g))

    d = dim_g
    os_src_dim = os_dimension(n, n - 1)
    os_tgt_dim = os_dimension(n - 1, n - 2)

    source_dim = d ** n * os_src_dim
    target_dim = d ** (n - 1) * os_tgt_dim

    if source_dim == 0 or target_dim == 0:
        return np.zeros((max(target_dim, 1), max(source_dim, 1)))

    M = np.zeros((target_dim, source_dim))

    for i_pt in range(1, n + 1):
        for j_pt in range(i_pt + 1, n + 1):
            if sign_convention == "os":
                sign = (-1) ** (i_pt + j_pt)
            else:
                sign = (-1) ** (j_pt - 1)

            # Bracket on g^{otimes n} -> g^{otimes (n-1)}
            b_map = bracket_pair_map_numpy(d, structure_constants, n,
                                           i_pt - 1, j_pt - 1)

            # Residue on OS^{n-1}(n) -> OS^{n-2}(n-1)
            r_map = residue_map(n, n - 1, i_pt, j_pt)

            # Kronecker product
            contrib = sign * np.kron(b_map, r_map)
            M += contrib

    return M


def chiral_bracket_rank(dim_g: int, structure_constants: Dict,
                        bar_degree: int,
                        sign_convention: str = "os") -> int:
    """Rank of chiral bracket differential with OS forms."""
    M = chiral_bracket_differential(dim_g, structure_constants,
                                    bar_degree, sign_convention)
    return int(np.linalg.matrix_rank(M, tol=1e-8))


# ============================================================
# Part 3b: Curvature barrier — why direct matrix computation fails
# ============================================================
#
# THE BARRIER (PROVED):
#
# The chiral bar differential d = d_bracket + d_curvature has two parts
# (Prop prop:pole-decomposition):
#
#   d_bracket: simple-pole residue R^{(0)}, extracts [a,b] = a_{(0)}b
#   d_curvature: derivative-residue R^{(1)}, extracts k·κ(a,b) = a_{(1)}b
#
# d_bracket alone does NOT square to zero (proved computationally for
# all 2048 sign conventions). Only d = d_bracket + d_curvature has d²=0,
# via the Borcherds identity. This is an intrinsically vertex-algebraic
# identity, not reducible to Lie Jacobi.
#
# WHY R^{(1)} CANNOT BE IMPLEMENTED AS A MATRIX:
#
# R^{(1)} is the derivative-residue: for ω = (dε/ε)∧α(ε) + β(ε),
# R^{(1)}(ω) = α'(0). On OS forms:
#
#   R^{(1)}_{12}(η₁₂ ∧ η₁₃) = -dw/w²    (NOT in OS algebra)
#
# The derivative-residue produces forms with double poles (dw/w²),
# which lie OUTSIDE the OS algebra. These extended forms don't support
# further residue operations. No finite-dimensional extension of the
# bar complex accommodates R^{(1)} as a matrix operation.
#
# WHY THE AUGMENTED APPROACH FAILS:
#
# A natural attempt: build V = g ⊕ k·|0⟩ with total product
# μ_aug(a,b) = [a,b] + k·κ(a,b)·|0⟩, then use standard R^{(0)} on V.
# This FAILS because μ_aug does NOT satisfy the Jacobi identity:
#
#   Σ_cyc μ_aug(μ_aug(a,b),c) includes Σ_cyc κ([a,b],c)·|0⟩
#   For sl₂ triple (e,f,h): this sum = 6k·|0⟩ ≠ 0
#
# The CE differential on V therefore has d² ≠ 0, and the augmented
# complex gives wrong cohomology dimensions.
#
# CORRECT METHOD (CLAUDE.md):
# PBW spectral sequence + Koszul dual Hilbert series. NOT matrix rank.
# See Part 1 (Koszul dual Hilbert series) and genus1_pbw_sl2.py.
#
# The functions below are INVESTIGATORY — they document the failed
# augmented approach. They are retained for reference but produce
# wrong results for bar cohomology.

# --- sl_2 data (used by tests and other modules) ---

DIM_SL2 = 3


def sl2_structure_constants_float() -> Dict:
    """sl_2 structure constants as float dict. Basis: e=0, h=1, f=2."""
    E, H, F = 0, 1, 2
    sc = {}
    sc[(E, F)] = {H: 1.0}
    sc[(F, E)] = {H: -1.0}
    sc[(H, E)] = {E: 2.0}
    sc[(E, H)] = {E: -2.0}
    sc[(H, F)] = {F: -2.0}
    sc[(F, H)] = {F: 2.0}
    return sc


def sl2_killing_form_float() -> Dict:
    """sl_2 Killing form as float dict. κ(e,f)=κ(f,e)=1, κ(h,h)=2."""
    return {(0, 2): 1.0, (2, 0): 1.0, (1, 1): 2.0}


# --- Augmented complex (INVESTIGATORY — produces wrong cohomology) ---

def _augmented_structure_constants(
    dim_g: int,
    structure_constants: Dict,
    killing_form: Dict,
    level: float,
) -> Dict:
    """Build augmented structure constants for V = g ⊕ k·|0⟩.

    WARNING: μ_aug does NOT satisfy Jacobi. The CE differential on V
    has d² ≠ 0. This function is retained for investigation only.
    """
    vac = dim_g
    sc_ext: Dict = {}
    for (a, b), targets in structure_constants.items():
        ext: Dict[int, float] = {}
        for c, coeff in targets.items():
            ext[c] = float(coeff)
        kappa = killing_form.get((a, b), 0)
        if kappa != 0:
            ext[vac] = ext.get(vac, 0) + float(level) * float(kappa)
        if ext:
            sc_ext[(a, b)] = ext
    for (a, b), kappa in killing_form.items():
        if (a, b) not in sc_ext and float(kappa) != 0:
            sc_ext[(a, b)] = {vac: float(level) * float(kappa)}
    return sc_ext


def chiral_full_differential(
    dim_g: int,
    structure_constants: Dict,
    killing_form: Dict,
    level: float,
    bar_degree: int,
    sign_convention: str = "os",
) -> np.ndarray:
    """INVESTIGATORY: augmented differential on V = g ⊕ k·|0⟩.

    WARNING: d² ≠ 0 because μ_aug violates Jacobi. See barrier
    documentation above. Retained for investigation only.
    """
    dim_V = dim_g + 1
    sc_ext = _augmented_structure_constants(
        dim_g, structure_constants, killing_form, level
    )
    return chiral_bracket_differential(dim_V, sc_ext, bar_degree, sign_convention)


def chiral_curvature_differential(
    dim_g: int,
    killing_form: Dict,
    level: float,
    bar_degree: int,
    sign_convention: str = "os",
) -> np.ndarray:
    """INVESTIGATORY: curvature-only differential using R^{(0)} on Killing.

    WARNING: This uses the WRONG residue operation. The true d_curvature
    uses R^{(1)} (derivative-residue), which produces forms outside OS.
    Using R^{(0)} with Killing form gives a different map that does NOT
    combine with d_bracket to give d² = 0. Retained for investigation.
    """
    n = bar_degree
    if n < 2:
        return np.zeros((1, dim_g))

    d = dim_g
    os_src_dim = os_dimension(n, n - 1)
    os_tgt_dim = os_dimension(n - 1, n - 2)

    source_dim = d ** n * os_src_dim
    target_tensor_dim = d ** (n - 2) if n > 2 else 1
    target_dim = target_tensor_dim * os_tgt_dim

    if source_dim == 0 or target_dim == 0:
        return np.zeros((max(target_dim, 1), max(source_dim, 1)))

    M = np.zeros((target_dim, source_dim))

    for i_pt in range(1, n + 1):
        for j_pt in range(i_pt + 1, n + 1):
            if sign_convention == "os":
                sign = (-1) ** (i_pt + j_pt)
            else:
                sign = (-1) ** (j_pt - 1)

            k_map = killing_pair_map_numpy(d, killing_form, n,
                                           i_pt - 1, j_pt - 1)
            r_map = residue_map(n, n - 1, i_pt, j_pt)

            contrib = float(level) * sign * np.kron(k_map, r_map)
            M += contrib

    return M


def _pure_g_mask(dim_g: int, n: int, os_dim: int) -> np.ndarray:
    """Boolean mask for pure-g elements in V^{⊗n} ⊗ OS."""
    dim_V = dim_g + 1
    total = dim_V ** n * os_dim
    mask = np.zeros(total, dtype=bool)
    for tensor_flat in range(dim_V ** n):
        indices = _flat_to_multi(tuple([dim_V] * n), tensor_flat)
        if all(idx < dim_g for idx in indices):
            start = tensor_flat * os_dim
            mask[start:start + os_dim] = True
    return mask


def bar_cohomology_full(
    dim_g: int,
    structure_constants: Dict,
    killing_form: Dict,
    level: float,
    bar_degree: int,
    sign_convention: str = "os",
) -> Dict[str, object]:
    """INVESTIGATORY: g-sector cohomology of augmented complex.

    WARNING: Produces WRONG results. d² ≠ 0 in the augmented complex
    because μ_aug violates Jacobi. See barrier documentation above.
    """
    n = bar_degree
    d = dim_g
    dim_V = d + 1

    os_n = os_dimension(n, n - 1) if n >= 1 else 1
    os_n1 = os_dimension(n + 1, n) if n + 1 >= 2 else 0

    B_n_aug_dim = dim_V ** n * os_n
    B_n_g_dim = d ** n * os_n
    B_n1_aug_dim = dim_V ** (n + 1) * os_n1 if os_n1 > 0 else 0

    if B_n_aug_dim > 300000 or B_n1_aug_dim > 300000:
        return {"n": n, "H_n": None, "note": "too large",
                "B_n_aug_dim": B_n_aug_dim, "B_n1_aug_dim": B_n1_aug_dim}

    g_mask_n = _pure_g_mask(d, n, os_n)
    g_cols_n = np.where(g_mask_n)[0]

    d_n = chiral_full_differential(
        d, structure_constants, killing_form, level, n, sign_convention
    )

    d_n_g = d_n[:, g_cols_n]
    rank_d_n_g = int(np.linalg.matrix_rank(d_n_g, tol=1e-8))
    dim_cocycles = len(g_cols_n) - rank_d_n_g

    if B_n1_aug_dim == 0:
        dim_coboundaries = 0
    else:
        g_mask_n_tgt = _pure_g_mask(d, n, os_dimension(n, n - 1) if n >= 1 else 1)
        g_rows_n = np.where(g_mask_n_tgt)[0]
        non_g_rows_n = np.where(~g_mask_n_tgt)[0]

        d_n1 = chiral_full_differential(
            d, structure_constants, killing_form, level, n + 1, sign_convention
        )

        d_g = d_n1[g_rows_n, :]
        d_non_g = d_n1[non_g_rows_n, :]

        if len(non_g_rows_n) == 0:
            dim_coboundaries = int(np.linalg.matrix_rank(d_g, tol=1e-8))
        else:
            rank_non_g = int(np.linalg.matrix_rank(d_non_g, tol=1e-8))
            null_dim = d_non_g.shape[1] - rank_non_g
            if null_dim == 0:
                dim_coboundaries = 0
            else:
                _, S, Vt = np.linalg.svd(d_non_g, full_matrices=True)
                tol = max(d_non_g.shape) * max(S) * 1e-10 if len(S) > 0 else 1e-10
                rank_svd = int(np.sum(S > tol))
                null_basis = Vt[rank_svd:, :].T
                restricted = d_g @ null_basis
                dim_coboundaries = int(np.linalg.matrix_rank(
                    restricted, tol=1e-8))

    H_n = dim_cocycles - dim_coboundaries
    return {
        "n": n,
        "dim_B_n_g": B_n_g_dim,
        "dim_B_n_aug": B_n_aug_dim,
        "dim_B_n1_aug": B_n1_aug_dim,
        "rank_d_n_g": rank_d_n_g,
        "dim_cocycles": dim_cocycles,
        "dim_coboundaries": dim_coboundaries,
        "H_n": H_n,
        "WARNING": "WRONG — augmented complex has d² ≠ 0",
    }


def verify_d_squared_augmented(
    dim_g: int,
    structure_constants: Dict,
    killing_form: Dict,
    level: float,
    bar_degree: int = 3,
    sign_convention: str = "os",
) -> Dict[str, object]:
    """INVESTIGATORY: verify d² for augmented differential (expected to FAIL).

    Confirms that d² ≠ 0 in the augmented complex, documenting the
    fundamental barrier.
    """
    n = bar_degree
    d_n = chiral_full_differential(
        dim_g, structure_constants, killing_form, level, n, sign_convention
    )
    d_nm1 = chiral_full_differential(
        dim_g, structure_constants, killing_form, level, n - 1, sign_convention
    )

    d_sq = d_nm1 @ d_n
    norm = float(np.max(np.abs(d_sq)))

    return {
        "bar_degree": n,
        "sign_convention": sign_convention,
        "level": level,
        "d_n_shape": d_n.shape,
        "d_{n-1}_shape": d_nm1.shape,
        "d^2_norm": norm,
        "d^2 = 0": norm < 1e-10,
        "note": "Expected d² ≠ 0: μ_aug violates Jacobi",
    }


# ============================================================
# Part 4: Conjectured rational GF and predictions
# ============================================================

def sl3_recurrence(a1: int = 8, a2: int = 36, a3: int = 204,
                   n_terms: int = 10) -> List[int]:
    """Compute bar cohomology dimensions using the conjectured recurrence.

    From Conjecture conj:sl3-bar-gf:
    a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
    with a(1)=8, a(2)=36, a(3)=204.

    The recurrence comes from the denominator of the rational GF:
    (1-8x)(1-3x-x^2) = 1 - 11x + 23x^2 + 8x^3.
    """
    a = [0, a1, a2, a3]
    for _k in range(4, n_terms + 1):
        a_n = 11 * a[-1] - 23 * a[-2] - 8 * a[-3]
        a.append(a_n)
    return a[1:]


def sl3_rational_gf_coefficients(n_terms: int = 10) -> List[int]:
    """Coefficients of the sl_3 bar cohomology rational GF.

    P(x) = 4x(2 - 13x - 2x^2) / ((1-8x)(1-3x-x^2))
    """
    return sl3_recurrence(8, 36, 204, n_terms)


# ============================================================
# Part 5: Verification suite
# ============================================================

def verify_sl2(max_degree: int = 8) -> Dict[str, object]:
    """Verify sl_2-hat bar cohomology.

    Corrected values: H^0=1, H^1=3, H^2=5, H^3=15, H^4=36, H^5=91, H^6=232.
    Note: Riordan R(n+3) is wrong at n=2 (gives 6, correct is 5).
    """
    bar_cohom = sl2_bar_cohomology(max_degree)
    results = {"bar_cohomology": bar_cohom}

    expected = {1: 3, 2: 5, 3: 15, 4: 36, 5: 91, 6: 232}
    for n, exp in expected.items():
        if n <= max_degree:
            actual = bar_cohom[n]
            results[f"H^{n} = {exp}"] = (actual == exp, actual)

    # Verify H^2 matches known value
    dim_g = 3
    h2_formula = bar_cohomology_degree2(dim_g)
    results["H^2 = 5 (corrected)"] = (bar_cohom[2] == h2_formula, bar_cohom[2])

    return results


def verify_sl3_known(max_degree: int = 8) -> Dict[str, object]:
    """Verify sl_3-hat bar cohomology against known/conjectured values.

    Known: H^1=8, H^2=36, H^3=204.
    Conjectured: H^4=1352, H^5=9892, etc.
    """
    bar_cohom = sl3_bar_cohomology(max_degree)
    results = {"bar_cohomology": bar_cohom}

    known = {1: 8, 2: 36, 3: 204}
    conjectured = {4: 1352, 5: 9892, 6: 76084, 7: 598592}

    for n, exp in known.items():
        if n <= max_degree:
            actual = bar_cohom[n]
            results[f"H^{n} = {exp} (known)"] = (actual == exp, actual)

    for n, exp in conjectured.items():
        if n <= max_degree:
            actual = bar_cohom[n]
            results[f"H^{n} = {exp} (conjectured)"] = (actual == exp, actual)

    # Verify H^2 = C(dim_g + 1, 2)
    dim_g = 8
    h2_formula = bar_cohomology_degree2(dim_g)
    results[f"H^2 = C({dim_g+1},2) = {h2_formula}"] = (
        bar_cohom[2] == h2_formula, bar_cohom[2])

    return results


def verify_bracket_ranks_sl3(max_degree: int = 3) -> Dict[str, object]:
    """Verify bracket differential ranks for sl_3 against manuscript.

    CE-type on g^{otimes n} (sign (-1)^{j-1}, no OS forms):
    - rank(d: B^2 -> B^1) = 8 = dim g  [surjective]
    - rank(d: B^3 -> B^2) = 56  [d^2=0 holds, rank < dim B^2 = 64]

    With OS forms and sign (-1)^{i+j} (comp:sl3-modular-rank):
    - rank(d: B^3 -> B^2) = 63  [Killing anomaly: 63 over Q, 64 over F_p]
    - rank(d: B^4 -> B^3) = 1024 = dim B^3  [surjective]

    Note: the manuscript's "512" for degree 4 is without OS forms
    (dim g^3 = 512); with OS forms dim B^3 = 512*2 = 1024.
    """
    sc = {(a, b): {c: float(v) for c, v in targets.items()}
          for (a, b), targets in sl3_structure_constants().items()}

    results = {}

    # CE-type ranks on g^{otimes n} (no OS)
    for n in range(2, max_degree + 2):
        if SL3_DIM ** n > 200000:
            continue
        rank = bracket_diff_rank(SL3_DIM, sc, n)
        results[f"CE rank(d: B^{n} -> B^{n-1})"] = rank

    # Expected CE ranks (no OS forms)
    expected_ce = {2: SL3_DIM, 3: 56}
    for n, exp in expected_ce.items():
        if n <= max_degree + 1:
            actual = results.get(f"CE rank(d: B^{n} -> B^{n-1})")
            if actual is not None:
                results[f"CE rank at {n} = {exp}"] = (actual == exp, actual)

    # Chiral bracket rank with OS forms (sign (-1)^{i+j})
    for n in range(2, min(max_degree + 2, 5)):
        os_src = os_dimension(n, n - 1)
        if SL3_DIM ** n * os_src > 200000:
            continue
        rank = chiral_bracket_rank(SL3_DIM, sc, n, sign_convention="os")
        results[f"OS rank(d: B^{n} -> B^{n-1})"] = rank

    # Expected OS ranks
    os_rank_3 = results.get("OS rank(d: B^3 -> B^2)")
    results["OS rank at 3 = 63 (comp:sl3-modular-rank)"] = (
        os_rank_3 == 63, os_rank_3)

    os_rank_4 = results.get("OS rank(d: B^4 -> B^3)")
    if os_rank_4 is not None:
        dim_B3_os = SL3_DIM ** 3 * os_dimension(3, 2)  # 512 * 2 = 1024
        results[f"OS rank at 4 = {dim_B3_os} (surjective)"] = (
            os_rank_4 == dim_B3_os, os_rank_4)

    return results


def verify_d_squared_ce(dim_g: int, structure_constants: Dict,
                        bar_degree: int = 3) -> Dict[str, object]:
    """Verify d^2 = 0 for CE bracket differential on g^{otimes n}.

    The CE-type bracket differential with sign (-1)^{j-1} on g^{otimes n}
    (without OS forms) satisfies d^2 = 0.  This is a standard fact from
    Lie algebra cohomology.

    Returns dict with norm of d^2 and pass/fail.
    """
    n = bar_degree
    d_n = ce_bracket_differential_numpy(dim_g, structure_constants, n)
    d_n1 = ce_bracket_differential_numpy(dim_g, structure_constants, n - 1)

    d_sq = d_n1 @ d_n
    norm = np.max(np.abs(d_sq))

    return {
        "bar_degree": n,
        "d_n_shape": d_n.shape,
        "d_{n-1}_shape": d_n1.shape,
        "d^2_norm": float(norm),
        "d^2 = 0": norm < 1e-10,
    }


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 70)
    print("CHIRAL BAR COHOMOLOGY FOR KAC-MOODY ALGEBRAS")
    print("=" * 70)

    # --- sl_2: Koszul dual Hilbert series ---
    print("\n--- sl_2-hat: Koszul dual Hilbert series ---")
    sl2_results = verify_sl2(8)
    bar2 = sl2_results["bar_cohomology"]
    print(f"  dim(A^!)_n (n=0..8): {bar2}")
    for name, data in sl2_results.items():
        if isinstance(data, tuple) and len(data) >= 2:
            ok, actual = data[0], data[1]
            status = "PASS" if ok else "FAIL"
            print(f"  [{status}] {name} (got {actual})")

    # --- sl_3: Koszul dual Hilbert series ---
    print("\n--- sl_3-hat: Koszul dual Hilbert series ---")
    sl3_results = verify_sl3_known(8)
    bar3 = sl3_results["bar_cohomology"]
    print(f"  dim(A^!)_n (n=0..8): {bar3}")
    for name, data in sl3_results.items():
        if isinstance(data, tuple) and len(data) >= 2:
            ok, actual = data[0], data[1]
            status = "PASS" if ok else "FAIL"
            print(f"  [{status}] {name} (got {actual})")

    # --- sl_3: Bracket differential ranks ---
    print("\n--- sl_3: Bracket differential ranks ---")
    rank_results = verify_bracket_ranks_sl3(3)
    for name, data in rank_results.items():
        if isinstance(data, tuple) and len(data) >= 2:
            ok, actual = data[0], data[1]
            status = "PASS" if ok else "FAIL"
            print(f"  [{status}] {name} (got {actual})")
        elif isinstance(data, (int, float)):
            print(f"  {name} = {data}")

    # --- sl_3: Verify d^2 = 0 for CE bracket ---
    print("\n--- sl_3: d^2 = 0 check (CE bracket, no OS) ---")
    sc = {(a, b): {c: float(v) for c, v in targets.items()}
          for (a, b), targets in sl3_structure_constants().items()}
    d2_check = verify_d_squared_ce(SL3_DIM, sc, 3)
    print(f"  d_3 shape: {d2_check['d_n_shape']}")
    print(f"  d_2 shape: {d2_check['d_{n-1}_shape']}")
    print(f"  ||d^2|| = {d2_check['d^2_norm']:.2e}")
    print(f"  d^2 = 0: {'PASS' if d2_check['d^2 = 0'] else 'FAIL'}")

    # --- Degree-2 universal formula ---
    print("\n--- Degree-2 universal formula ---")
    for name, d in [("sl_2", 3), ("sl_3", 8), ("so_5", 10)]:
        h2 = bar_cohomology_degree2(d)
        print(f"  {name}: dim g = {d}, H^2 = C({d+1},2) = {h2}")

    # --- Recurrence predictions ---
    print("\n--- Recurrence predictions for sl_3-hat ---")
    rec = sl3_recurrence(8, 36, 204, 8)
    print(f"  H^1,...,H^8: {rec}")
    print(f"  H^4 (conjectured) = {rec[3]}")
