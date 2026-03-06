#!/usr/bin/env python3
"""Weight-decomposed modular rank computation for sl_3 bar complex at degree 4.

Programme IX computation target: decompose the ~1200-dim chain complex
B^4(sl_3) by h-weight, compute ranks of smaller blocks over F_p.

The sl_3 bar complex at degree n has dim = 8^n (chain group dimension).
At degree 4: 8^4 = 4096 elements. The bar differential d: B^4 -> B^3
is a 512 x 4096 matrix (8^3 x 8^4). Weight decomposition into smaller
blocks makes rank computation feasible.

Key: the bar CHAIN COMPLEX uses the Lie bracket part of the differential
(simple pole residues). The curvature part (double pole) maps to lower
bar degrees. We compute the rank of the bracket-only differential,
decomposed by h-weight.

NOTE: The bracket-only differential d_bracket^2 != 0 in general
(this is proved in the monograph). But rank(d_bracket) still gives
information about the chain-level structure.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from itertools import product
from typing import Dict, List, Tuple

from sympy import Matrix, Rational, zeros, GF


# sl_3 data
DIM_G = 8
GEN_NAMES = ["H1", "H2", "E1", "E2", "E3", "F1", "F2", "F3"]
H1, H2, E1, E2, E3, F1, F2, F3 = range(8)

# Weight of each generator under (H1, H2) action
# H1, H2 have weight (0,0)
# E1 has weight alpha_1 = (2, -1)
# E2 has weight alpha_2 = (-1, 2)
# E3 has weight alpha_1 + alpha_2 = (1, 1)
# F_i have weight -alpha_i
WEIGHTS = {
    H1: (0, 0),
    H2: (0, 0),
    E1: (2, -1),
    E2: (-1, 2),
    E3: (1, 1),
    F1: (-2, 1),
    F2: (1, -2),
    F3: (-1, -1),
}


def weight_of_tensor(indices: Tuple[int, ...]) -> Tuple[int, int]:
    """Weight of a tensor product of generators."""
    w = [0, 0]
    for i in indices:
        wi = WEIGHTS[i]
        w[0] += wi[0]
        w[1] += wi[1]
    return tuple(w)


def sl3_bracket(a: int, b: int) -> Dict[int, Rational]:
    """Structure constants [a, b] = sum_c f^{ab}_c * c.

    Returns dict {generator_index: coefficient}.
    """
    result = {}

    # Cartan matrix
    A = [[2, -1], [-1, 2]]

    # [H_i, E_j] = A_{ij} * E_j
    cartan_gens = [H1, H2]
    pos_gens = [E1, E2]
    neg_gens = [F1, F2]

    for i, hi in enumerate(cartan_gens):
        for j, ej in enumerate(pos_gens):
            if a == hi and b == ej:
                result[ej] = Rational(A[i][j])
                return result
            if a == ej and b == hi:
                result[ej] = Rational(-A[i][j])
                return result

    for i, hi in enumerate(cartan_gens):
        for j, fj in enumerate(neg_gens):
            if a == hi and b == fj:
                result[fj] = Rational(-A[i][j])
                return result
            if a == fj and b == hi:
                result[fj] = Rational(A[i][j])
                return result

    # [H_i, E_3] and [H_i, F_3]
    # E_3 has weight alpha_1 + alpha_2, so [H_i, E_3] = (A[i,0]+A[i,1])*E_3
    for i, hi in enumerate(cartan_gens):
        coeff = A[i][0] + A[i][1]  # = 1 for both i=0,1
        if a == hi and b == E3:
            result[E3] = Rational(coeff)
            return result
        if a == E3 and b == hi:
            result[E3] = Rational(-coeff)
            return result
        if a == hi and b == F3:
            result[F3] = Rational(-coeff)
            return result
        if a == F3 and b == hi:
            result[F3] = Rational(coeff)
            return result

    # [E_i, F_j] = delta_{ij} * H_i (for simple roots i,j in {1,2})
    for i in range(2):
        if a == pos_gens[i] and b == neg_gens[i]:
            result[cartan_gens[i]] = Rational(1)
            return result
        if a == neg_gens[i] and b == pos_gens[i]:
            result[cartan_gens[i]] = Rational(-1)
            return result

    # [E_1, E_2] = E_3
    if a == E1 and b == E2:
        result[E3] = Rational(1)
        return result
    if a == E2 and b == E1:
        result[E3] = Rational(-1)
        return result

    # [F_2, F_1] = F_3
    if a == F2 and b == F1:
        result[F3] = Rational(1)
        return result
    if a == F1 and b == F2:
        result[F3] = Rational(-1)
        return result

    # [E_1, F_3]: [E_1, [F_2, F_1]] = [[E_1,F_2],F_1] + [F_2,[E_1,F_1]]
    # = 0 + [F_2, H_1] = -2*F_2 + F_2... wait, let me use Jacobi
    # [E_1, F_3] = [E_1, [F_2, F_1]]
    # By Jacobi: = [[E_1,F_2], F_1] + [F_2, [E_1, F_1]]
    # [E_1, F_2] = 0 (different simple roots), [E_1, F_1] = H_1
    # = 0 + [F_2, H_1] = -[H_1, F_2] = -(-A[0][1])*F_2 = -1*F_2 = -F_2
    # Wait: [H_1, F_2] = -A[0][1]*F_2 = -(-1)*F_2 = F_2
    # So [F_2, H_1] = -[H_1, F_2] = -F_2
    if a == E1 and b == F3:
        result[F2] = Rational(-1)
        return result
    if a == F3 and b == E1:
        result[F2] = Rational(1)
        return result

    # [E_2, F_3] = [E_2, [F_2, F_1]]
    # = [[E_2,F_2], F_1] + [F_2, [E_2, F_1]]
    # [E_2, F_2] = H_2, [E_2, F_1] = 0
    # = [H_2, F_1] = -(-A[1][0])*F_1... wait
    # [H_2, F_1] = -A[1][0]*F_1 = -(-1)*F_1 = F_1
    if a == E2 and b == F3:
        result[F1] = Rational(1)
        return result
    if a == F3 and b == E2:
        result[F1] = Rational(-1)
        return result

    # [E_3, F_1] = [E_3, F_1] where E_3 = [E_1, E_2]
    # = [[E_1,E_2], F_1] = [E_1, [E_2, F_1]] + [[E_1, F_1], E_2]
    # [E_2, F_1] = 0, [E_1, F_1] = H_1
    # = 0 + [H_1, E_2] = A[0][1]*E_2 = -E_2
    if a == E3 and b == F1:
        result[E2] = Rational(-1)
        return result
    if a == F1 and b == E3:
        result[E2] = Rational(1)
        return result

    # [E_3, F_2] = [[E_1,E_2], F_2] = [E_1, [E_2,F_2]] + [[E_1,F_2], E_2]
    # [E_2, F_2] = H_2, [E_1, F_2] = 0
    # = [E_1, H_2] = -[H_2, E_1] = -A[1][0]*E_1 = E_1
    if a == E3 and b == F2:
        result[E1] = Rational(1)
        return result
    if a == F2 and b == E3:
        result[E1] = Rational(-1)
        return result

    # [E_3, F_3] = [[E_1,E_2], [F_2,F_1]]
    # = [E_1, [E_2, [F_2, F_1]]] - [E_2, [E_1, [F_2, F_1]]]
    # [E_2, F_3] = F_1 (from above), [E_1, F_3] = -F_2 (from above)
    # = [E_1, F_1] - [E_2, (-F_2)] = H_1 + [E_2, F_2] = H_1 + H_2
    if a == E3 and b == F3:
        result[H1] = Rational(1)
        result[H2] = Rational(1)
        return result
    if a == F3 and b == E3:
        result[H1] = Rational(-1)
        result[H2] = Rational(-1)
        return result

    # Serre: [E_1, E_3] = [E_1, [E_1, E_2]] = 0
    # Similarly [E_2, E_3] = 0, [F_1, F_3] = 0, [F_2, F_3] = 0
    # All other brackets are 0
    return result


def build_weight_blocks(degree: int):
    """Build the bar differential matrix decomposed by weight.

    The bar differential d: B^{degree} -> B^{degree-1} acts by
    d([a_1|...|a_n]) = sum_{i<j} (-1)^{...} [a_1|...|[a_i,a_j]|...|a_n]

    For the degree-2 bar differential (simple pole / bracket part):
    d([a|b]) = [a, b]

    For degree n -> n-1, we use the "first pair" convention:
    d([a_1|a_2|...|a_n]) = sum over consecutive pairs (i, i+1):
       (-1)^i [a_1|...|[a_i,a_{i+1}]|...|a_n]
    """
    # Enumerate basis elements by weight
    source_by_weight = defaultdict(list)  # weight -> list of (index_tuple, global_index)
    target_by_weight = defaultdict(list)

    source_bases = list(product(range(DIM_G), repeat=degree))
    target_bases = list(product(range(DIM_G), repeat=degree - 1))

    for idx, basis in enumerate(source_bases):
        w = weight_of_tensor(basis)
        source_by_weight[w].append((basis, idx))

    for idx, basis in enumerate(target_bases):
        w = weight_of_tensor(basis)
        target_by_weight[w].append((basis, idx))

    return source_by_weight, target_by_weight, source_bases, target_bases


def compute_differential_block(
    weight: Tuple[int, int],
    degree: int,
    source_by_weight: dict,
    target_by_weight: dict,
    source_bases: list,
    target_bases: list,
    prime: int = 0,
) -> Tuple[int, int, int]:
    """Compute rank of bar differential restricted to a weight block.

    Returns (source_dim, target_dim, rank).
    """
    sources = source_by_weight.get(weight, [])
    targets = target_by_weight.get(weight, [])

    if not sources or not targets:
        return (len(sources), len(targets), 0)

    # Build local index maps
    target_local = {basis: i for i, (basis, _) in enumerate(targets)}

    n_src = len(sources)
    n_tgt = len(targets)

    # Build matrix
    mat = zeros(n_tgt, n_src)

    for col, (src_basis, _) in enumerate(sources):
        # Apply bar differential: sum over consecutive pairs
        for pos in range(degree - 1):
            a = src_basis[pos]
            b = src_basis[pos + 1]
            bracket = sl3_bracket(a, b)
            sign = (-1) ** pos

            for c, coeff in bracket.items():
                # Build target basis element
                target_elem = src_basis[:pos] + (c,) + src_basis[pos + 2:]
                if target_elem in target_local:
                    row = target_local[target_elem]
                    mat[row, col] += sign * coeff

    if prime > 0:
        # Compute rank over F_p
        mat_mod = mat.applyfunc(lambda x: x % prime)
        return (n_src, n_tgt, mat_mod.rank())
    else:
        return (n_src, n_tgt, mat.rank())


def main():
    print("=" * 70)
    print("sl_3 Bar Complex: Weight-Decomposed Modular Rank Computation")
    print("=" * 70)

    primes = [0, 2, 3, 5, 7]  # 0 = characteristic 0

    for degree in [3, 4]:
        print(f"\n{'=' * 60}")
        print(f"Degree {degree} -> {degree - 1}")
        print(f"Source dim: 8^{degree} = {8**degree}")
        print(f"Target dim: 8^{degree-1} = {8**(degree-1)}")
        print(f"{'=' * 60}")

        source_bw, target_bw, src_bases, tgt_bases = build_weight_blocks(degree)

        # Collect all weights
        all_weights = sorted(set(list(source_bw.keys()) + list(target_bw.keys())))

        total_rank = defaultdict(int)

        for w in all_weights:
            n_src = len(source_bw.get(w, []))
            n_tgt = len(target_bw.get(w, []))
            if n_src == 0 or n_tgt == 0:
                continue

            print(f"\nWeight {w}: source={n_src}, target={n_tgt}", end="")

            for p in primes:
                label = f"char {p}" if p > 0 else "char 0"
                try:
                    _, _, rk = compute_differential_block(
                        w, degree, source_bw, target_bw,
                        src_bases, tgt_bases, prime=p
                    )
                    total_rank[p] += rk
                    print(f"  rk({label})={rk}", end="")
                except Exception as e:
                    print(f"  rk({label})=ERR({e})", end="")

            print()

        print(f"\n--- Totals for d: B^{degree} -> B^{degree-1} ---")
        for p in primes:
            label = f"char {p}" if p > 0 else "char 0"
            print(f"  Total rank ({label}): {total_rank[p]}")

        # Check for modular anomalies
        char0_rank = total_rank[0]
        for p in primes:
            if p > 0 and total_rank[p] != char0_rank:
                print(f"  *** MODULAR ANOMALY at p={p}: "
                      f"rank drops from {char0_rank} to {total_rank[p]} ***")


if __name__ == "__main__":
    main()
