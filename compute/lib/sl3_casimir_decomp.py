"""Casimir decomposition of sl₃^{⊗n} — PBW spectral sequence data.

Decomposes tensor powers of the adjoint representation of sl₃ into
Casimir eigenspaces (irreducible representations under the diagonal
adjoint action). This is the representation-theoretic input for the
PBW spectral sequence analysis of chiral bar cohomology.

Key outputs:
1. Casimir eigenspace multiplicities for g^{⊗n}, n = 2, 3, 4
2. CE bracket rank within each eigenspace
3. Verification against representation-theoretic predictions

The quadratic Casimir C₂ = Σ_{a,b} κ^{ab} ad(eₐ) ∘ ad(e_b) acts on
g^{⊗n} via the diagonal adjoint action. Eigenvalues identify irreps:

    C₂(V(λ₁,λ₂)) = (2/3)(λ₁² + λ₂² + λ₁λ₂) + 2(λ₁ + λ₂)

To avoid rationals, we compute 3C₂ which has integer eigenvalues:

    3C₂(V(λ₁,λ₂)) = 2(λ₁² + λ₂² + λ₁λ₂) + 6(λ₁ + λ₂)

Common eigenvalues of 3C₂:
    V(0,0):  0  (trivial, dim 1)
    V(1,0):  8  (fundamental, dim 3)
    V(0,1):  8  (antifundamental, dim 3)
    V(1,1): 18  (adjoint, dim 8)
    V(2,0): 20  (dim 6)
    V(0,2): 20  (dim 6)
    V(2,1): 32  (dim 15)
    V(1,2): 32  (dim 15)
    V(3,0): 36  (dim 10)
    V(0,3): 36  (dim 10)
    V(2,2): 48  (dim 27)
    V(3,1): 50  (dim 24)
    V(1,3): 50  (dim 24)
    V(4,0): 56  (dim 15)
    V(0,4): 56  (dim 15)
    V(4,1): 72  (dim 35)
    V(1,4): 72  (dim 35)
    V(3,3): 90  (dim 64)

References:
  - Thm thm:pbw-genus1-km (higher_genus.tex)
  - genus1_pbw_sl2.py (sl₂ analog)
"""

from __future__ import annotations

from typing import Dict, List, Tuple

import numpy as np

from compute.lib.sl3_bar import (
    DIM_G,
    sl3_structure_constants,
    sl3_killing_form,
)
from compute.lib.km_chiral_bar import ce_bracket_differential_numpy


# ============================================================
# sl₃ inverse Killing form
# ============================================================

def sl3_inverse_killing_form() -> Dict[Tuple[int, int], float]:
    """Inverse Killing form κ^{ab} for sl₃.

    The Killing form κ has Cartan block A = [[2,-1],[-1,2]] and
    root-coroot pairs κ(Eᵢ,Fᵢ) = 1. The inverse:

    Cartan block: A⁻¹ = (1/3)[[2,1],[1,2]]
    Root-coroot: κ⁻¹(Eᵢ,Fᵢ) = κ⁻¹(Fᵢ,Eᵢ) = 1
    """
    H1, H2, E1, E2, E3, F1, F2, F3 = range(8)
    inv_kf = {}
    # Cartan block: A⁻¹ = (1/3)[[2,1],[1,2]]
    inv_kf[(H1, H1)] = 2.0 / 3.0
    inv_kf[(H1, H2)] = 1.0 / 3.0
    inv_kf[(H2, H1)] = 1.0 / 3.0
    inv_kf[(H2, H2)] = 2.0 / 3.0
    # Root-coroot pairs
    inv_kf[(E1, F1)] = 1.0
    inv_kf[(F1, E1)] = 1.0
    inv_kf[(E2, F2)] = 1.0
    inv_kf[(F2, E2)] = 1.0
    inv_kf[(E3, F3)] = 1.0
    inv_kf[(F3, E3)] = 1.0
    return inv_kf


# ============================================================
# Tensor index encoding/decoding
# ============================================================

def _decode(index: int, power: int, d: int = DIM_G) -> List[int]:
    """Decode flat index into tensor-factor indices (base d)."""
    digits = [0] * power
    value = index
    for pos in range(power - 1, -1, -1):
        digits[pos] = value % d
        value //= d
    return digits


def _encode(factors: List[int], d: int = DIM_G) -> int:
    """Encode tensor-factor indices into flat index (base d)."""
    index = 0
    for v in factors:
        index = index * d + v
    return index


# ============================================================
# Bracket lookup (float)
# ============================================================

_BRACKET_CACHE: Dict[Tuple[int, int], Dict[int, float]] = {}


def _get_bracket() -> Dict[Tuple[int, int], Dict[int, float]]:
    """Get sl₃ bracket as float dict (cached)."""
    global _BRACKET_CACHE
    if not _BRACKET_CACHE:
        sc = sl3_structure_constants()
        _BRACKET_CACHE = {
            (a, b): {c: float(v) for c, v in targets.items()}
            for (a, b), targets in sc.items()
        }
    return _BRACKET_CACHE


# ============================================================
# Casimir matrix construction
# ============================================================

def build_casimir(power: int) -> np.ndarray:
    """Build 3C₂ (scaled quadratic Casimir) on sl₃^{⊗power}.

    Returns integer-valued matrix (as float64) of shape (d^n, d^n).
    The factor of 3 clears the Cartan denominators, giving integer
    eigenvalues: 3C₂(V(λ₁,λ₂)) = 2(λ₁²+λ₂²+λ₁λ₂) + 6(λ₁+λ₂).
    """
    d = DIM_G
    dim = d ** power
    bracket = _get_bracket()
    inv_kf = sl3_inverse_killing_form()

    # Scale by 3 to get integer eigenvalues
    scaled_inv_kf = {k: 3.0 * v for k, v in inv_kf.items()}

    C = np.zeros((dim, dim), dtype=np.float64)

    for src in range(dim):
        factors_src = _decode(src, power, d)

        for (a, b), kappa in scaled_inv_kf.items():
            # Compute ad(b)(e_src) → sparse vector
            ad_b: Dict[int, float] = {}
            for slot in range(power):
                br = bracket.get((b, factors_src[slot]))
                if br is None:
                    continue
                for c, coeff in br.items():
                    new_factors = list(factors_src)
                    new_factors[slot] = c
                    idx = _encode(new_factors, d)
                    ad_b[idx] = ad_b.get(idx, 0.0) + coeff

            # Compute ad(a)(ad_b_result) → accumulate into C
            for idx1, coeff1 in ad_b.items():
                factors1 = _decode(idx1, power, d)
                for slot in range(power):
                    br = bracket.get((a, factors1[slot]))
                    if br is None:
                        continue
                    for c, coeff2 in br.items():
                        new_factors = list(factors1)
                        new_factors[slot] = c
                        idx2 = _encode(new_factors, d)
                        C[idx2, src] += kappa * coeff1 * coeff2

    return C


# ============================================================
# Eigenspace decomposition
# ============================================================

def casimir_eigenspace_decomposition(power: int) -> Dict[int, int]:
    """Decompose sl₃^{⊗power} into 3C₂ eigenspaces.

    Returns: {eigenvalue: multiplicity} where eigenvalues are integers
    (eigenvalues of 3C₂, not C₂).

    Note: the Casimir matrix is NOT symmetric in the Chevalley basis
    (the Killing form is indefinite). We use general eigenvalue
    decomposition and verify all eigenvalues are real integers.
    """
    C = build_casimir(power)
    eigenvalues = np.linalg.eigvals(C)

    # Verify all eigenvalues are real
    max_imag = np.max(np.abs(eigenvalues.imag))
    if max_imag > 0.01:
        raise ArithmeticError(
            f"Casimir has non-real eigenvalues: max imag {max_imag:.6f}"
        )

    real_evs = eigenvalues.real

    # Round to nearest integer
    rounded = np.round(real_evs).astype(int)

    # Verify rounding is accurate
    max_err = np.max(np.abs(real_evs - rounded))
    if max_err > 0.1:
        raise ArithmeticError(
            f"Casimir eigenvalues not close to integers: max error {max_err:.6f}"
        )

    # Count multiplicities
    unique, counts = np.unique(rounded, return_counts=True)
    return {int(ev): int(ct) for ev, ct in zip(unique, counts)}


def casimir_nullity(power: int, eigenvalue: int) -> int:
    """Compute nullity of (3C₂ - eigenvalue·I) on sl₃^{⊗power}.

    More memory-efficient than full decomposition for checking a
    single eigenvalue.
    """
    C = build_casimir(power)
    d = DIM_G
    dim = d ** power
    shifted = C - eigenvalue * np.eye(dim)
    rank = int(np.linalg.matrix_rank(shifted, tol=0.5))
    return dim - rank


# ============================================================
# Expected decompositions from representation theory
# ============================================================

def sl3_irrep_dim(lam1: int, lam2: int) -> int:
    """Dimension of V(λ₁ω₁ + λ₂ω₂) for sl₃."""
    return (lam1 + 1) * (lam2 + 1) * (lam1 + lam2 + 2) // 2


def sl3_casimir_eigenvalue(lam1: int, lam2: int) -> int:
    """Eigenvalue of 3C₂ on V(λ₁ω₁ + λ₂ω₂).

    3C₂ = 2(λ₁² + λ₂² + λ₁λ₂) + 6(λ₁ + λ₂)
    """
    return 2 * (lam1**2 + lam2**2 + lam1 * lam2) + 6 * (lam1 + lam2)


def expected_adj_tensor2() -> Dict[int, int]:
    """Expected decomposition of adj⊗adj for sl₃.

    8⊗8 = 1 + 8 + 8 + 10 + 10* + 27
    """
    decomp = {}
    # V(0,0): dim 1, eigenvalue 0
    decomp[0] = decomp.get(0, 0) + 1
    # V(1,1): dim 8 × 2 copies, eigenvalue 18
    decomp[18] = decomp.get(18, 0) + 16
    # V(3,0): dim 10, eigenvalue 36
    decomp[36] = decomp.get(36, 0) + 10
    # V(0,3): dim 10, eigenvalue 36
    decomp[36] = decomp.get(36, 0) + 10
    # V(2,2): dim 27, eigenvalue 48
    decomp[48] = decomp.get(48, 0) + 27
    return decomp


def expected_adj_tensor3() -> Dict[int, int]:
    """Expected decomposition of adj⊗adj⊗adj for sl₃.

    Computed by iterating: (8⊗8)⊗8 using Littlewood-Richardson.
    8³ = 512. Decomposition (eigenvalue → total multiplicity):

    This is computed and verified by the code itself.
    """
    # We don't hardcode this — let the computation discover it.
    # The verification is that eigenvalues are valid and dims sum to 512.
    return None


# ============================================================
# CE bracket rank within eigenspaces
# ============================================================

def ce_bracket_differential(power: int) -> np.ndarray:
    """CE bracket differential d: g^{⊗n} → g^{⊗(n-1)} for sl₃.

    Delegates to ce_bracket_differential_numpy from km_chiral_bar.py,
    which uses ALL pairs (i,j) with sign (-1)^{j-1}, replaces position i
    with [a_i, a_j], and removes position j. Satisfies d² = 0.
    """
    sc = _get_bracket()
    return ce_bracket_differential_numpy(DIM_G, sc, power)


def bracket_rank_by_eigenspace(power: int) -> Dict[int, Dict]:
    """Rank of CE bracket d₁: g^{⊗n} → g^{⊗(n-1)} within Casimir eigenspaces.

    For each eigenvalue λ of 3C₂ on g^{⊗n}:
    - Compute the eigenspace E_λ ⊂ g^{⊗n}
    - Restrict d₁ to E_λ → g^{⊗(n-1)}
    - Report: dim(E_λ), rank(d₁|_{E_λ}), dim(ker d₁ ∩ E_λ)

    Uses the fact that d₁ is equivariant: C₂(tgt) ∘ d₁ = d₁ ∘ C₂(src),
    so d₁ maps E_λ(src) → E_λ(tgt).
    """
    d = DIM_G
    src_dim = d ** power
    tgt_dim = d ** (power - 1)

    # Build Casimir on source
    C_src = build_casimir(power)

    # Eigendecomposition (general, not assuming symmetry)
    eigenvalues_src, eigenvectors_src = np.linalg.eig(C_src)
    # Sort by real eigenvalue
    order = np.argsort(eigenvalues_src.real)
    eigenvalues_src = eigenvalues_src.real[order]
    eigenvectors_src = eigenvectors_src[:, order].real
    ev_rounded = np.round(eigenvalues_src).astype(int)

    # Build bracket differential
    D = ce_bracket_differential(power)

    results = {}
    unique_evs = sorted(set(ev_rounded))

    for ev in unique_evs:
        mask = (ev_rounded == ev)
        dim_eigenspace = int(np.sum(mask))
        # Eigenvectors for this eigenspace (columns)
        V_lambda = eigenvectors_src[:, mask]
        # Restrict bracket to eigenspace: D @ V_lambda
        restricted = D @ V_lambda
        rank = int(np.linalg.matrix_rank(restricted, tol=1e-8))
        ker_dim = dim_eigenspace - rank

        results[int(ev)] = {
            "dim": dim_eigenspace,
            "rank": rank,
            "ker_dim": ker_dim,
        }

    return results


# ============================================================
# Verify d² = 0 for CE bracket
# ============================================================

def verify_ce_d_squared(power: int) -> float:
    """Verify d² = 0 for CE bracket on g^{⊗n} (should be < 1e-10)."""
    D_n = ce_bracket_differential(power)
    D_nm1 = ce_bracket_differential(power - 1)
    d_sq = D_nm1 @ D_n
    return float(np.max(np.abs(d_sq)))


# ============================================================
# Koszul dual dimensions from Koszul relation
# ============================================================

def koszul_dual_dims_from_bar_cohomology(
    bar_dims: List[int],
) -> List[int]:
    """Compute dual-branch dims from bar-dual dims via H_A(t)·H_{A!}(-t) = 1.

    Given H^n = bar_dims[n] interpreted as dim(A^i)_n, computes
    b_n = dim(A^!)_n after finite-dimensional duality.
    bar_dims[0] should be 1 (= H⁰).
    """
    N = len(bar_dims)
    a = bar_dims  # a[n] = H^n
    # H_A(t) · H_{A!}(-t) = 1
    # Σ_n (Σ_{k=0}^n a_k · c_{n-k}) t^n = 1
    # where c_m = (-1)^m · b_m
    c = [0] * N
    c[0] = 1  # b_0 = 1
    for n in range(1, N):
        c[n] = -sum(a[k] * c[n - k] for k in range(1, n + 1))
    # b_n = (-1)^n · c_n
    b = [(-1)**n * c[n] for n in range(N)]
    return b


# ============================================================
# Main computation
# ============================================================

def run_decomposition(max_power: int = 4) -> Dict:
    """Run full Casimir decomposition analysis for sl₃^{⊗n}.

    Returns comprehensive results including eigenspaces, bracket ranks,
    and Koszul dual analysis.
    """
    results = {}

    # Koszul dual dimensions (assuming known/conjectured bar cohomology)
    bar_dims = [1, 8, 36, 204, 1352, 9892, 76084, 598592]
    kd = koszul_dual_dims_from_bar_cohomology(bar_dims)
    results["koszul_dual_dims"] = {
        "bar_cohomology": bar_dims,
        "koszul_dual": kd,
        "note": "(A^!)_n computed from H_A(t)·H_{A!}(-t) = 1",
    }

    for n in range(2, max_power + 1):
        dim_n = DIM_G ** n
        print(f"\n--- sl₃^{{⊗{n}}} (dim {dim_n}) ---")

        # Casimir eigenspace decomposition
        print(f"  Building 3C₂ on g^{{⊗{n}}}...")
        decomp = casimir_eigenspace_decomposition(n)
        total_dim = sum(decomp.values())
        print(f"  Eigenspaces: {decomp}")
        print(f"  Total dim: {total_dim} (expected {dim_n})")
        assert total_dim == dim_n, f"Dimension mismatch: {total_dim} ≠ {dim_n}"

        # Verify against expected decomposition (n=2)
        if n == 2:
            expected = expected_adj_tensor2()
            match = (decomp == expected)
            print(f"  Matches rep theory: {match}")
            if not match:
                print(f"    Expected: {expected}")
                results[f"n={n}_match"] = False
            else:
                results[f"n={n}_match"] = True

        # CE bracket rank analysis
        print(f"  Computing CE bracket d: g^{{⊗{n}}} → g^{{⊗{n-1}}}...")
        bracket_data = bracket_rank_by_eigenspace(n)
        total_rank = sum(v["rank"] for v in bracket_data.values())
        total_ker = sum(v["ker_dim"] for v in bracket_data.values())
        print(f"  Total rank(d): {total_rank}")
        print(f"  Total dim(ker d): {total_ker}")

        for ev in sorted(bracket_data.keys()):
            info = bracket_data[ev]
            print(f"    3C₂={ev}: dim={info['dim']}, "
                  f"rank={info['rank']}, ker={info['ker_dim']}")

        # Verify d² = 0
        if n >= 3:
            d_sq_norm = verify_ce_d_squared(n)
            print(f"  ||d²||: {d_sq_norm:.2e} ({'✓' if d_sq_norm < 1e-10 else '✗'})")
            results[f"n={n}_d_sq"] = d_sq_norm

        results[f"n={n}"] = {
            "dim": dim_n,
            "eigenspaces": decomp,
            "bracket_by_eigenspace": bracket_data,
            "total_rank": total_rank,
            "total_ker": total_ker,
        }

    return results


if __name__ == "__main__":
    print("=" * 70)
    print("CASIMIR DECOMPOSITION OF sl₃^{⊗n}")
    print("=" * 70)
    results = run_decomposition(4)

    print("\n" + "=" * 70)
    print("KOSZUL DUAL DIMENSIONS")
    print("=" * 70)
    kd = results["koszul_dual_dims"]
    print(f"  Bar cohomology H^n: {kd['bar_cohomology']}")
    print(f"  Koszul dual (A^!)_n: {kd['koszul_dual']}")
    print(f"  Classical Λ^n(g*):   {[1, 8, 28, 56, 70, 56, 28, 8]}")
