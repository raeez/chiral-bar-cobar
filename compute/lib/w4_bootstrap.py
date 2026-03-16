"""W₄ OPE bootstrap: construct W₃, W₄ primaries directly in the free-boson Fock space.

Instead of relying on the (buggy) quantum Miura expansion, we:
1. Enumerate weight-h free-boson monomials
2. Build the L₁ constraint matrix (Virasoro lowering)
3. Find its kernel (= Virasoro primary subspace)
4. Determine W₃ as the unique primary satisfying the W₃ algebra OPE

This is path (B) from mc4_bpz_frontier.md.

The free-boson Fock space for sl₄ uses 3 independent bosons φ₀, φ₁, φ₂
(indices 0, 1, 2) with propagator <dφᵢ(z) dφⱼ(w)> = -δᵢⱼ/(z-w)².

The stress tensor T = -(1/2)Σ(dφₐ)² + Qₐ·d²φₐ where Q = α₀·ρ is the
background charge vector.

A weight-h free-boson monomial is a product Π d^{mₖ}φ_{iₖ} with
Σ mₖ = h (total derivative order = conformal weight).

The L₁ operator acts on monomials via the Virasoro algebra:
L₁·(d^m φᵢ) = m·d^{m-1}φᵢ  (lowers derivative by 1)
plus commutator terms from normal ordering with T.
"""

from __future__ import annotations

from itertools import product as iterproduct
from typing import Dict, List, Tuple

import numpy as np

from compute.lib.w4_ope_miura import (
    Field, Monomial, simplify_field, field_weight,
    _bpz_inner_product, compute_ope, evaluate_field_as_number,
    add_fields, scale_field, sort_monomial,
)


# ═══════════════════════════════════════════════════════════════
# Monomial enumeration
# ═══════════════════════════════════════════════════════════════

def enumerate_monomials(weight: int, n_bosons: int = 3) -> List[Monomial]:
    """Enumerate all normal-ordered free-boson monomials of given weight.

    A monomial is a tuple ((i₁,m₁), (i₂,m₂), ...) with:
    - iₖ ∈ {0, 1, ..., n_bosons-1} (boson index)
    - mₖ ≥ 1 (derivative order; bare φ doesn't appear in vertex algebras)
    - Σ mₖ = weight
    - Sorted: (i₁,m₁) ≤ (i₂,m₂) ≤ ... (normal ordering)

    Returns list of Monomial tuples.
    """
    results = []
    _enum_helper(weight, n_bosons, [], 0, 0, results)
    return results


def _enum_helper(target: int, n_bosons: int, current: list,
                  min_boson: int, min_deriv: int, results: list):
    """Recursively enumerate monomials."""
    if target == 0:
        results.append(tuple(current))
        return
    if target < 0:
        return

    # Add one more operator (i, m) with m ≥ 1 and m ≤ target
    for m in range(max(1, min_deriv), target + 1):
        for i in range(min_boson if m > min_deriv else min_boson, n_bosons):
            current.append((i, m))
            # Next operator must be ≥ (i, m) in lex order
            _enum_helper(target - m, n_bosons, current, i, m, results)
            current.pop()
            # After same m, next boson must be > i
        min_boson = 0  # reset for next m value


def monomial_to_field(mon: Monomial, coeff: float = 1.0) -> Field:
    """Convert a monomial to a single-term field."""
    return [(coeff, mon)]


# ═══════════════════════════════════════════════════════════════
# L₁ action (Virasoro lowering operator)
# ═══════════════════════════════════════════════════════════════

def l1_action_on_monomial(mon: Monomial, T: Field) -> Field:
    """Compute L₁ acting on a normal-ordered monomial.

    L₁ = ∮ dz/(2πi) z² T(z) · (monomial at w)

    For T = -(1/2)Σ(dφₐ)² + Qₐ·d²φₐ, the L₁ action is:

    L₁·(d^{m₁}φ_{i₁} ··· d^{mₖ}φ_{iₖ}) =
      Σⱼ mⱼ · (d^{m₁}φ_{i₁} ··· d^{mⱼ-1}φ_{iⱼ} ··· d^{mₖ}φ_{iₖ})  [from kinetic term]
      + ... [background charge corrections]

    More precisely: L₁ acts via the contour integral of z²T(z) around
    the monomial. Using the T OPE with each operator in the monomial:

    T(z)·d^m φᵢ(w) ~ -(m·d^{m-1}φᵢ(w))/(z-w)³ + (m·d^m φᵢ(w))/(z-w)²
                       + (d^{m+1}φᵢ(w))/(z-w)   [from kinetic part]
                       + Qᵢ·(...) [from background charge part]

    Actually, the simplest approach: L₁ is the MODE of T, so
    L₁·A = Res_{z→w} (z-w)² T(z) A(w), which is the pole-1 coefficient
    of T(z)·A(w) multiplied by... no, L_n = ∮ z^{n+1} T(z) dz/(2πi).

    L₁·A(w) = pole-2 coefficient of (z-w)·T(z)·A(w)... this is getting
    complicated. Let me use the OPE engine directly.
    """
    # L₁·A = coefficient of (z-w)^{-2} in (z-w)·T(z)·A(w)
    # = coefficient of (z-w)^{-1} in T(z)·A(w) ... no.
    # L_n = ∮ dz/(2πi) z^{n+1} T(z), so for a field at w:
    # L_n A(w) = Res_{z→w} (z-w)^{n+1} T(z) A(w)
    # = coefficient of (z-w)^{-(n+2)} in T(z)A(w) ... no.
    # L_n A(w) = Res_{z=w} (z-w)^{n+1} T(z) A(w) dz
    # The OPE T(z)A(w) = Σ_k C_k(w)/(z-w)^k
    # Res_{z=w} (z-w)^{n+1} Σ_k C_k/(z-w)^k = C_{n+2}
    # So L_n A = C_{n+2} = (pole n+2 coefficient of T×A OPE)

    # L₁ A = pole 3 coefficient of T(z)·A(w)
    A_field = monomial_to_field(mon)
    ope = compute_ope(T, A_field, max_pole=3)
    return ope.get(3, [])


def build_l1_matrix(monomials: List[Monomial], T: Field) -> np.ndarray:
    """Build the matrix of L₁ action on the monomial basis.

    Returns matrix M where M[i,j] = coefficient of monomial[i] in L₁·monomial[j].
    """
    n = len(monomials)
    mon_to_idx = {m: i for i, m in enumerate(monomials)}

    # We need L₁ to map weight-h monomials to weight-(h-1) monomials.
    # So the target monomials are at weight h-1.
    h = sum(m for _, m in monomials[0])  # all monomials have same weight
    target_monomials = enumerate_monomials(h - 1)
    target_to_idx = {m: i for i, m in enumerate(target_monomials)}

    n_target = len(target_monomials)
    M = np.zeros((n_target, n))

    for j, mon in enumerate(monomials):
        l1_result = l1_action_on_monomial(mon, T)
        l1_result = simplify_field(l1_result)
        for coeff, res_mon in l1_result:
            res_mon = sort_monomial(res_mon)
            if res_mon in target_to_idx:
                M[target_to_idx[res_mon], j] += coeff

    return M, target_monomials


def find_primary_space(weight: int, T: Field, n_bosons: int = 3) -> Tuple[List[Monomial], np.ndarray]:
    """Find the Virasoro primary subspace at given weight.

    Returns (monomials, basis) where basis[i] are the coefficients
    of the i-th primary vector in the monomial basis.
    """
    monomials = enumerate_monomials(weight, n_bosons)
    print(f"Weight {weight}: {len(monomials)} monomials")

    M, _ = build_l1_matrix(monomials, T)
    print(f"L₁ matrix: {M.shape[0]} × {M.shape[1]}")

    # Primary space = kernel of L₁ (and higher L_n, but L₁ suffices for primaries)
    U, S, Vt = np.linalg.svd(M, full_matrices=True)

    # Kernel = rows of Vt corresponding to zero singular values
    tol = 1e-10 * S[0] if len(S) > 0 else 1e-10
    kernel_dim = np.sum(S < tol)
    kernel_basis = Vt[-kernel_dim:]  # last kernel_dim rows of Vt

    print(f"Singular values: min={S[-1]:.2e}, threshold={tol:.2e}")
    print(f"Primary space dimension: {kernel_dim}")

    return monomials, kernel_basis


if __name__ == "__main__":
    from compute.lib.w4_ope_miura import W4MiuraOPE

    ope = W4MiuraOPE.from_t(1.0, verbose=False)
    T = ope.T
    c = ope.c_actual

    print(f"c = {c}")
    print(f"\n--- Weight 3 primary space ---")
    mons3, basis3 = find_primary_space(3, T)

    print(f"\n--- Weight 4 primary space ---")
    mons4, basis4 = find_primary_space(4, T)
