#!/usr/bin/env python3
"""
Verify the Koszul dual Hilbert function dim(A!)_w for chiral algebras.

The table in examples_summary.tex reports dim(A!)_w at each conformal weight w.
This script tests whether these match:
  (A) The exterior algebra Λ(V*) dimensions (naive PBW SS E1 page)
  (B) The Lie algebra homology H_*(g⊗t^{-1}C[t^{-1}], C) at weight w
  (C) Something else (the actual chiral bar complex)

Known values:
  Heisenberg: 1, 1, 1, 2, 3, 5, 7, 11  (= p(w-2) for w≥2)
  sl₂:        3, 6, 15, 36, 91, 232     (= Riordan R(w+3))
  sl₃:        8, 36, 204, 1352†         (conjectured GF)
"""

import numpy as np
from itertools import combinations, product as iterproduct
from collections import defaultdict
from math import comb
from functools import lru_cache


# ============================================================
# Part 1: Exterior algebra dimensions Π(1+q^m)^d
# ============================================================

def exterior_algebra_dims(d, max_w):
    """
    Compute dim Λ(V*)_w for V = C^d at each mode level m≥1.
    This is [q^w] in Π_{m≥1} (1+q^m)^d.
    """
    # Use polynomial multiplication
    # Start with 1
    coeffs = [0] * (max_w + 1)
    coeffs[0] = 1

    for m in range(1, max_w + 1):
        # Multiply by (1 + q^m)^d
        # (1+q^m)^d = Σ_k C(d,k) q^{mk}
        new_coeffs = [0] * (max_w + 1)
        for k in range(min(d, max_w // m) + 1):
            c = comb(d, k)
            for j in range(max_w + 1 - m * k):
                new_coeffs[j + m * k] += coeffs[j] * c
        coeffs = new_coeffs

    return coeffs


# ============================================================
# Part 2: Lie algebra homology of g⊗t^{-1}C[t^{-1}]
# ============================================================

def sl2_structure_constants():
    """
    sl₂ basis: e=0, h=1, f=2
    [e,f] = h, [h,e] = 2e, [h,f] = -2f
    Returns f[a][b][c] = structure constant [e_a, e_b] = Σ f[a][b][c] e_c
    """
    d = 3
    f = [[[0]*d for _ in range(d)] for _ in range(d)]
    # [e,f] = h
    f[0][2][1] = 1
    f[2][0][1] = -1
    # [h,e] = 2e
    f[1][0][0] = 2
    f[0][1][0] = -2
    # [h,f] = -2f
    f[1][2][2] = -2
    f[2][1][2] = 2
    return f


def sl3_structure_constants():
    """
    sl₃ basis (8-dim): e1,e2,e3,f1,f2,f3,h1,h2
    Standard Chevalley basis for sl₃.
    Returns f[a][b][c] for [e_a, e_b] = Σ f[a][b][c] e_c
    """
    d = 8
    # Indices: e1=0, e2=1, e3=2, f1=3, f2=4, f3=5, h1=6, h2=7
    # e3 = [e1, e2], f3 = [f2, f1]
    # Cartan matrix: A = [[2,-1],[-1,2]]
    f = [[[0]*d for _ in range(d)] for _ in range(d)]

    def set_bracket(a, b, pairs):
        """Set [e_a, e_b] = Σ coeff * e_c and [e_b, e_a] = -Σ coeff * e_c"""
        for c, coeff in pairs:
            f[a][b][c] = coeff
            f[b][a][c] = -coeff

    # [h1, e1] = 2e1
    set_bracket(6, 0, [(0, 2)])
    # [h1, e2] = -e2
    set_bracket(6, 1, [(1, -1)])
    # [h1, e3] = e3  (since e3 = [e1,e2], ad(h1)e3 = (2-1)e3 = e3)
    set_bracket(6, 2, [(2, 1)])
    # [h1, f1] = -2f1
    set_bracket(6, 3, [(3, -2)])
    # [h1, f2] = f2
    set_bracket(6, 4, [(4, 1)])
    # [h1, f3] = -f3
    set_bracket(6, 5, [(5, -1)])
    # [h2, e1] = -e1
    set_bracket(7, 0, [(0, -1)])
    # [h2, e2] = 2e2
    set_bracket(7, 1, [(1, 2)])
    # [h2, e3] = e3
    set_bracket(7, 2, [(2, 1)])
    # [h2, f1] = f1
    set_bracket(7, 3, [(3, 1)])
    # [h2, f2] = -2f2
    set_bracket(7, 4, [(4, -2)])
    # [h2, f3] = -f3
    set_bracket(7, 5, [(5, -1)])
    # [e1, f1] = h1
    set_bracket(0, 3, [(6, 1)])
    # [e2, f2] = h2
    set_bracket(1, 4, [(7, 1)])
    # [e1, e2] = e3
    set_bracket(0, 1, [(2, 1)])
    # [f2, f1] = f3  (note sign: [f1,f2] = -f3)
    set_bracket(4, 3, [(5, 1)])
    # [e3, f1] = -e2  (ad(f1)e3 = ad(f1)[e1,e2] = [h1,e2] = -e2... wait)
    # Actually: [e3, f1] = [[e1,e2], f1] = [e1,[e2,f1]] + [[e1,f1],e2]
    # [e2,f1] = 0 (different simple roots), [e1,f1] = h1
    # So [e3,f1] = 0 + [h1, e2] = -e2
    set_bracket(2, 3, [(1, -1)])
    # [e3, f2] = e1  (similarly)
    # [[e1,e2], f2] = [e1,[e2,f2]] + [[e1,f2],e2]
    # [e2,f2] = h2, [e1,f2] = 0
    # = [e1, h2] + 0 = -[h2, e1] = -(-e1) = e1
    set_bracket(2, 4, [(0, 1)])
    # [e3, f3] = h1 + h2
    # [[e1,e2], [f2,f1]] = ... use Jacobi identity
    # [e3, f3] = [e3, [f2,f1]] = [[e3,f2], f1] + [f2, [e3,f1]]
    # = [e1, f1] + [f2, -e2] = h1 + (-[f2,e2]) = h1 + [e2,f2] = h1 + h2
    set_bracket(2, 5, [(6, 1), (7, 1)])
    # [e1, f3] = -f2
    # [e1, [f2,f1]] = [[e1,f2],f1] + [f2,[e1,f1]]
    # = 0 + [f2, h1] = -[h1, f2] = -(f2) = -f2... wait
    # [h1, f2] = f2, so [f2, h1] = -f2
    # So [e1, f3] = -f2
    # Hmm wait: [h1, f2] = f2 from above. So [f2, h1] = -[h1, f2] = -f2.
    # [e1, f3] = 0 + [f2, h1] = -f2
    set_bracket(0, 5, [(4, -1)])
    # [e2, f3] = f1
    # [e2, [f2,f1]] = [[e2,f2],f1] + [f2,[e2,f1]]
    # = [h2, f1] + 0 = f1
    set_bracket(1, 5, [(3, 1)])
    # [h1, h2] = 0 (Cartan subalgebra is abelian)
    # Already zero by initialization

    return f


def lie_algebra_homology_weight(struct_const, dim_g, weight):
    """
    Compute Lie algebra homology H_*(g⊗t^{-1}C[t^{-1}], C) at conformal weight w.

    The current algebra L = g⊗t^{-1}C[t^{-1}] has basis {e_a ⊗ t^{-m} : a=0,...,d-1, m≥1}
    with bracket [e_a⊗t^{-m}, e_b⊗t^{-n}] = [e_a,e_b]⊗t^{-(m+n)} = Σ_c f[a][b][c] e_c⊗t^{-(m+n)}.

    The CE chain complex at weight w:
    ... → Λ^k(L)_w → Λ^{k-1}(L)_w → ...

    where Λ^k(L)_w consists of k-vectors with total conformal weight w.

    Returns dict: degree -> dim H_k
    """
    d = dim_g
    w = weight

    # Step 1: Enumerate basis elements of L at weight ≤ w
    # Each basis element is (a, m) where a ∈ {0,...,d-1}, m ∈ {1,...,w}
    # We use a total ordering: (a, m) < (b, n) iff (m, a) < (n, b)
    basis = []
    for m in range(1, w + 1):
        for a in range(d):
            basis.append((a, m))

    # Map each basis element to an index
    basis_idx = {b: i for i, b in enumerate(basis)}
    N = len(basis)  # Total number of basis elements at weight ≤ w

    # Step 2: For each degree k, enumerate basis of Λ^k(L)_w
    # A basis element of Λ^k is a sorted k-tuple of distinct basis indices
    # with total weight = w

    def weight_of_subset(subset):
        return sum(basis[i][1] for i in subset)

    # Precompute: for each k, list all k-subsets of {0,...,N-1} with weight w
    chain_bases = {}  # k -> list of sorted tuples
    for k in range(1, w + 1):  # k can be at most w (since each element has weight ≥ 1)
        if k > N:
            break
        chains = []
        for combo in combinations(range(N), k):
            if weight_of_subset(combo) == w:
                chains.append(combo)
        if chains:
            chain_bases[k] = chains

    if not chain_bases:
        return {}

    # Step 3: Compute the CE boundary map ∂: Λ^k → Λ^{k-1}
    # ∂(v_{i1} ∧ ... ∧ v_{ik}) = Σ_{p<q} (-1)^{p+q} [v_{ip}, v_{iq}] ∧ v_{i1} ∧ ... ∧ v̂_{ip} ∧ ... ∧ v̂_{iq} ∧ ...

    def bracket(i, j):
        """Compute [basis[i], basis[j]] as a dict: basis_index -> coefficient"""
        a, m = basis[i]
        b, n = basis[j]
        result = {}
        wt = m + n
        if wt > w:  # weight exceeds our range, won't contribute
            return result
        for c in range(d):
            coeff = struct_const[a][b][c]
            if coeff != 0:
                key = (c, wt)
                if key in basis_idx:
                    result[basis_idx[key]] = coeff
        return result

    def boundary_matrix(k):
        """Compute the matrix of ∂: Λ^k → Λ^{k-1} at weight w."""
        if k not in chain_bases or (k-1) not in chain_bases:
            return None

        source = chain_bases[k]
        target = chain_bases[k-1]
        target_idx = {t: i for i, t in enumerate(target)}

        mat = np.zeros((len(target), len(source)), dtype=np.float64)

        for col, combo in enumerate(source):
            combo_list = list(combo)
            for p in range(len(combo_list)):
                for q in range(p+1, len(combo_list)):
                    # Compute [v_{ip}, v_{iq}]
                    br = bracket(combo_list[p], combo_list[q])
                    if not br:
                        continue

                    # The remaining elements (excluding p and q)
                    remaining = [combo_list[r] for r in range(len(combo_list)) if r != p and r != q]

                    sign = (-1) ** (p + q)

                    for idx_c, coeff in br.items():
                        # Insert idx_c into remaining (sorted)
                        new_combo = sorted(remaining + [idx_c])
                        new_combo_tuple = tuple(new_combo)

                        # Check if idx_c is already in remaining (would give 0 in exterior algebra)
                        if idx_c in remaining:
                            continue

                        if new_combo_tuple in target_idx:
                            # Determine sign from sorting
                            # The element is: [v_p, v_q] ∧ v_0 ∧ ... ∧ v̂_p ∧ ... ∧ v̂_q ∧ ...
                            # = sign * v_{sorted} where we need to count transpositions
                            # to insert idx_c into the sorted remaining list
                            pos = new_combo.index(idx_c)
                            sort_sign = (-1) ** pos

                            row = target_idx[new_combo_tuple]
                            mat[row, col] += sign * sort_sign * coeff

        return mat

    # Step 4: Compute homology dimensions
    results = {}
    max_k = max(chain_bases.keys()) if chain_bases else 0

    for k in range(1, max_k + 1):
        dim_k = len(chain_bases.get(k, []))

        # Compute rank of ∂_k: Λ^k → Λ^{k-1}
        mat_k = boundary_matrix(k)
        rank_k = int(np.linalg.matrix_rank(mat_k)) if mat_k is not None else 0

        # Compute rank of ∂_{k+1}: Λ^{k+1} → Λ^k
        mat_k1 = boundary_matrix(k+1)
        rank_k1 = int(np.linalg.matrix_rank(mat_k1)) if mat_k1 is not None else 0

        h_k = dim_k - rank_k - rank_k1
        if h_k > 0:
            results[k] = h_k

    return results


def heisenberg_structure_constants():
    """Heisenberg: 1 generator, abelian current algebra."""
    return [[[0]]]


# ============================================================
# Part 3: Main comparison
# ============================================================

def main():
    print("=" * 70)
    print("Koszul dual Hilbert function verification")
    print("=" * 70)

    # Known table values
    table = {
        'Heisenberg': [1, 1, 1, 2, 3, 5, 7, 11],
        'sl2': [3, 6, 15, 36, 91, 232],
        'sl3': [8, 36, 204, 1352],  # 1352 is conjectured
    }

    max_w = 8

    # --- Exterior algebra dimensions ---
    print("\n--- Exterior algebra Π(1+q^m)^d ---")
    for name, d in [('Heisenberg', 1), ('sl2', 3), ('sl3', 8)]:
        ext_dims = exterior_algebra_dims(d, max_w)
        print(f"{name} (d={d}): {ext_dims[1:max_w+1]}")
        print(f"  Table:       {table[name]}")
        match = all(ext_dims[w+1] == table[name][w] for w in range(min(len(table[name]), max_w)))
        print(f"  Match: {match}")

    # --- Lie algebra homology ---
    print("\n--- Lie algebra homology H_*(g⊗t^{-1}C[t^{-1}], C)_w ---")

    # Heisenberg (d=1, abelian)
    print("\nHeisenberg (d=1, abelian current algebra):")
    heis_sc = heisenberg_structure_constants()
    for w in range(1, 7):
        hom = lie_algebra_homology_weight(heis_sc, 1, w)
        total = sum(hom.values())
        tab_val = table['Heisenberg'][w-1] if w <= len(table['Heisenberg']) else '?'
        ext_val = exterior_algebra_dims(1, w)[w]
        print(f"  w={w}: H_* = {dict(hom)}, total = {total}, "
              f"ext = {ext_val}, table = {tab_val}")

    # sl₂ (d=3)
    print("\nsl₂ (d=3):")
    sl2_sc = sl2_structure_constants()
    for w in range(1, 6):
        hom = lie_algebra_homology_weight(sl2_sc, 3, w)
        total = sum(hom.values())
        tab_val = table['sl2'][w-1] if w <= len(table['sl2']) else '?'
        ext_val = exterior_algebra_dims(3, w)[w]
        print(f"  w={w}: H_* = {dict(hom)}, total = {total}, "
              f"ext = {ext_val}, table = {tab_val}")

    # sl₃ (d=8) - only small weights due to combinatorial explosion
    print("\nsl₃ (d=8):")
    sl3_sc = sl3_structure_constants()

    # First verify structure constants
    print("  Verifying sl₃ Jacobi identity...")
    d = 8
    ok = True
    for a in range(d):
        for b in range(d):
            for c in range(d):
                # [a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0
                for e in range(d):
                    val = 0
                    for f in range(d):
                        val += sl3_sc[a][f][e] * sl3_sc[b][c][f]  # [a,[b,c]]
                        val += sl3_sc[b][f][e] * sl3_sc[c][a][f]  # [b,[c,a]]
                        val += sl3_sc[c][f][e] * sl3_sc[a][b][f]  # [c,[a,b]]
                    if abs(val) > 1e-10:
                        print(f"  Jacobi FAILED at ({a},{b},{c},{e}): {val}")
                        ok = False
    print(f"  Jacobi identity: {'PASSED' if ok else 'FAILED'}")

    for w in range(1, 4):  # Only up to w=3 due to size
        hom = lie_algebra_homology_weight(sl3_sc, 8, w)
        total = sum(hom.values())
        tab_val = table['sl3'][w-1] if w <= len(table['sl3']) else '?'
        ext_val = exterior_algebra_dims(8, w)[w]
        print(f"  w={w}: H_* = {dict(hom)}, total = {total}, "
              f"ext = {ext_val}, table = {tab_val}")

    # --- Summary ---
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print("If exterior dims ≠ table vals: the PBW SS E₁=Λ(V*) doesn't collapse")
    print("If Lie algebra homology ≠ table vals: the chiral bar ≠ algebraic bar")
    print("In that case, the table computes the CHIRAL bar complex cohomology")
    print("which involves OS forms on configuration spaces.")


if __name__ == '__main__':
    main()
