#!/usr/bin/env python3
"""Compute sl_3 bar cohomology at minimum conformal weight via direct linear algebra.

The chiral bar complex at minimum conformal weight:
  B_bar^n = g^{otimes n} otimes OS^{n-1}(C_n)
  dim B_bar^n = (dim g)^n * (n-1)!

Differential d: B_bar^n -> B_bar^{n-1} is the Lie bracket contraction with OS residue.

Uses weight decomposition under sl_3 to break into independent blocks.
"""

import numpy as np
from itertools import product as iproduct, combinations
from collections import defaultdict
import time

# ================================================================
# sl_3 structure constants
# ================================================================
# Basis: 0=H1, 1=H2, 2=E1, 3=E2, 4=E3, 5=F1, 6=F2, 7=F3
# where E3=[E1,E2], F3=[F2,F1]

DIM = 8
NAMES = ['H1', 'H2', 'E1', 'E2', 'E3', 'F1', 'F2', 'F3']

# Weights under (H1, H2) eigenvalues
WEIGHTS = {
    0: (0, 0),    # H1
    1: (0, 0),    # H2
    2: (2, -1),   # E1
    3: (-1, 2),   # E2
    4: (1, 1),    # E3 = [E1,E2]
    5: (-2, 1),   # F1
    6: (1, -2),   # F2
    7: (-1, -1),  # F3 = [F2,F1]
}

# Build structure constants: [a, b] = sum_c f[a,b,c] * basis[c]
# Define only the "upper triangle" then antisymmetrize
f = np.zeros((DIM, DIM, DIM), dtype=np.float64)

# Cartan matrix for A2
A = np.array([[2, -1], [-1, 2]])

# [Hi, Ej] = A_{ij} Ej  (i in {0,1}, j in {0,1} mapping to E_{j+1} = basis[2+j])
for i in range(2):
    for j in range(2):
        f[i][2+j][2+j] = A[i][j]

# [Hi, E3] : weight of E3 = alpha1+alpha2, so [H1,E3] = (A_{11}+A_{12})E3 = 1*E3
# [H2,E3] = (A_{21}+A_{22})E3 = 1*E3
f[0][4][4] = 1
f[1][4][4] = 1

# [Hi, Fj] = -A_{ij} Fj
for i in range(2):
    for j in range(2):
        f[i][5+j][5+j] = -A[i][j]

# [Hi, F3] = -(A_{i1}+A_{i2})*F3
f[0][7][7] = -1
f[1][7][7] = -1

# [Ei, Fi] = Hi
f[2][5][0] = 1    # [E1, F1] = H1
f[3][6][1] = 1    # [E2, F2] = H2

# [E1, E2] = E3
f[2][3][4] = 1

# [F2, F1] = F3
f[6][5][7] = 1

# [E3, F1] = -E2 (computed: [[E1,E2],F1] = [E1,[E2,F1]] + [[E1,F1],E2] = 0 + [H1,E2] = -E2)
f[4][5][3] = -1

# [E3, F2] = E1 (computed: [[E1,E2],F2] = [E1,[E2,F2]] + [[E1,F2],E2] = [E1,H2] + 0 = -(-1)E1 = E1)
# Wait: [E1, H2] = -[H2, E1] = -A_{21}*E1 = -(-1)*E1 = E1. So [E3,F2] = E1. Correct.
f[4][6][2] = 1

# [E3, F3] = H1 + H2
f[4][7][0] = 1
f[4][7][1] = 1

# [E1, F3] = -F2 (computed above)
f[2][7][6] = -1

# [E2, F3] = F1
f[3][7][5] = 1

# [F1, E3] should come from antisymmetry, but let's also set cross brackets
# that don't follow from the above

# Now enforce antisymmetry: f[b][a][c] = -f[a][b][c]
for a in range(DIM):
    for b in range(a+1, DIM):
        for c in range(DIM):
            if f[a][b][c] != 0 and f[b][a][c] != 0:
                # Both set; they should be negatives
                if abs(f[a][b][c] + f[b][a][c]) > 1e-10:
                    print(f"CONFLICT: f[{NAMES[a]}][{NAMES[b]}][{NAMES[c]}] = {f[a][b][c]}, "
                          f"f[{NAMES[b]}][{NAMES[a]}][{NAMES[c]}] = {f[b][a][c]}")
            elif f[a][b][c] != 0:
                f[b][a][c] = -f[a][b][c]
            elif f[b][a][c] != 0:
                f[a][b][c] = -f[b][a][c]

# Check antisymmetry
print("Checking antisymmetry...")
ok = True
for a in range(DIM):
    for b in range(DIM):
        for c in range(DIM):
            if abs(f[a][b][c] + f[b][a][c]) > 1e-10:
                print(f"  FAIL: [{NAMES[a]},{NAMES[b]}] -> {NAMES[c]}: "
                      f"{f[a][b][c]} vs {f[b][a][c]}")
                ok = False
if ok:
    print("  Antisymmetry: PASS")

# Print all nonzero brackets
print("\nNonzero brackets:")
for a in range(DIM):
    for b in range(a+1, DIM):
        terms = []
        for c in range(DIM):
            if abs(f[a][b][c]) > 1e-10:
                coeff = f[a][b][c]
                terms.append(f"{coeff:+.0f}*{NAMES[c]}")
        if terms:
            print(f"  [{NAMES[a]}, {NAMES[b]}] = {' '.join(terms)}")

# Verify Jacobi identity
print("\nVerifying Jacobi identity...")
jacobi_ok = True
for a in range(DIM):
    for b in range(DIM):
        for c in range(DIM):
            # [a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0
            jac = np.zeros(DIM)
            for d in range(DIM):
                jac += f[b][c][d] * f[a][d]  # [a, [b,c]]
                jac += f[c][a][d] * f[b][d]  # [b, [c,a]]
                jac += f[a][b][d] * f[c][d]  # [c, [a,b]]
            if np.max(np.abs(jac)) > 1e-10:
                if jacobi_ok:
                    print(f"  FAIL: ({NAMES[a]}, {NAMES[b]}, {NAMES[c]}): {jac}")
                jacobi_ok = False
print(f"  Jacobi identity: {'PASS' if jacobi_ok else 'FAIL'}")


# ================================================================
# Orlik-Solomon algebra
# ================================================================

def os_basis(n):
    """NBC basis for OS^{n-1}(C_n). Returns list of tuples of edges."""
    if n <= 1:
        return [()]

    edges = [(i, j) for i in range(n) for j in range(i+1, n)]

    # Broken circuits: for triangle (i,j,k) with i<j<k,
    # circuit {(i,j),(i,k),(j,k)}, max in lex = (j,k), BC = {(i,j),(i,k)}
    broken_circuits = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                broken_circuits.append(frozenset({(i,j), (i,k)}))

    basis = []
    for subset in combinations(edges, n-1):
        subset_set = frozenset(subset)
        if not any(bc.issubset(subset_set) for bc in broken_circuits):
            basis.append(tuple(sorted(subset)))
    return basis


# OS residue: extract omega_{ij} from a form in OS^{n-1}(C_n),
# returning a form in OS^{n-2}(C_{n-1}).
#
# The residue map works as follows:
# 1. If omega_{ij} is not in the form, result is 0
# 2. Pull omega_{ij} to the front (with sign), remove it
# 3. Relabel: merge positions i,j -> min(i,j), remove max(i,j), shift down
# 4. Express result in NBC basis of C_{n-1}

def _relabel_edge(e, i, j):
    """Relabel an edge after merging positions i and j.
    Position max(i,j) is removed; both i,j map to min(i,j);
    positions > max(i,j) shift down by 1."""
    hi = max(i, j)
    lo = min(i, j)
    a, b = e
    # Map positions
    def remap(p):
        if p == i or p == j:
            return lo
        elif p > hi:
            return p - 1
        else:
            return p
    a2, b2 = remap(a), remap(b)
    if a2 == b2:
        return None  # degenerate
    return (min(a2, b2), max(a2, b2))


def _sort_with_sign(edges):
    """Sort a list of edges and return (sorted_tuple, sign)."""
    arr = list(edges)
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return tuple(arr), (-1)**swaps


def _express_in_nbc(form_edges, n, basis, depth=0):
    """Express a form (given as sorted tuple of edges) in the NBC basis.
    Returns dict {index: coefficient}."""
    if depth > 20:
        return {}

    if form_edges in basis:
        return {basis.index(form_edges): 1.0}

    # Check for repeated edges (= 0)
    if len(set(form_edges)) < len(form_edges):
        return {}

    # Find a broken circuit
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                bc = ((i,j), (i,k))
                if bc[0] in form_edges and bc[1] in form_edges:
                    # Arnold: omega_{ij} ^ omega_{ik} = omega_{ij} ^ omega_{jk} - omega_{ik} ^ omega_{jk}
                    # where (j,k) is the missing edge

                    pos_ij = form_edges.index(bc[0])
                    pos_ik = form_edges.index(bc[1])
                    missing = (j, k)

                    # Term 1: replace omega_{ik} with omega_{jk}
                    new1 = list(form_edges)
                    new1[pos_ik] = missing
                    s1, sign1 = _sort_with_sign(new1)

                    # Term 2: replace omega_{ij} with omega_{jk}, negate
                    new2 = list(form_edges)
                    new2[pos_ij] = missing
                    s2, sign2 = _sort_with_sign(new2)

                    result = {}
                    c1 = _express_in_nbc(s1, n, basis, depth+1)
                    for idx, v in c1.items():
                        result[idx] = result.get(idx, 0) + sign1 * v
                    c2 = _express_in_nbc(s2, n, basis, depth+1)
                    for idx, v in c2.items():
                        result[idx] = result.get(idx, 0) - sign2 * v

                    return {k: v for k, v in result.items() if abs(v) > 1e-10}

    return {}


def compute_residue_matrices(n):
    """Precompute all residue matrices Res_{D_{ij}}: OS^{n-1}(C_n) -> OS^{n-2}(C_{n-1})."""
    basis_n = os_basis(n)
    basis_nm1 = os_basis(n - 1)

    matrices = {}
    for i in range(n):
        for j in range(i+1, n):
            M = np.zeros((len(basis_nm1), len(basis_n)), dtype=np.float64)
            target_edge = (i, j)

            for col, form in enumerate(basis_n):
                if target_edge not in form:
                    continue

                pos = form.index(target_edge)
                sign = (-1) ** pos  # sign from pulling omega_{ij} to front

                # Remaining edges
                remaining = list(form[:pos]) + list(form[pos+1:])

                # Relabel
                relabeled = []
                ok = True
                for e in remaining:
                    e2 = _relabel_edge(e, i, j)
                    if e2 is None:
                        ok = False
                        break
                    relabeled.append(e2)

                if not ok:
                    continue

                sorted_rel, sort_sign = _sort_with_sign(relabeled)

                # Express in NBC basis
                coeffs = _express_in_nbc(sorted_rel, n - 1, basis_nm1)
                for row, v in coeffs.items():
                    M[row, col] += sign * sort_sign * v

            matrices[(i, j)] = M

    return matrices


# ================================================================
# Verify OS dimensions
# ================================================================
print("\nOS algebra dimensions:")
for n in range(1, 7):
    basis = os_basis(n)
    from math import factorial
    expected = factorial(n - 1)
    print(f"  OS^{n-1}(C_{n}): dim = {len(basis)}, expected = {expected}")
    assert len(basis) == expected


# ================================================================
# Weight decomposition
# ================================================================

def weight_decomposition(n):
    """Decompose g^{otimes n} by weight."""
    decomp = defaultdict(list)
    for indices in iproduct(range(DIM), repeat=n):
        w = tuple(sum(WEIGHTS[idx][k] for idx in indices) for k in range(2))
        decomp[w].append(indices)
    return decomp


# ================================================================
# Bar differential for one weight block
# ================================================================

def bar_differential_block(n, weight, decomp_n, decomp_nm1, res_matrices):
    """Compute d: B_bar^n_w -> B_bar^{n-1}_w.

    Returns matrix M (rows = target, cols = source).
    """
    os_n = os_basis(n)
    os_nm1 = os_basis(n - 1)

    tuples_n = decomp_n.get(weight, [])
    tuples_nm1 = decomp_nm1.get(weight, [])

    dim_out = len(tuples_nm1) * len(os_nm1)
    dim_in = len(tuples_n) * len(os_n)

    if dim_out == 0 or dim_in == 0:
        return np.zeros((max(dim_out, 1), max(dim_in, 1)))

    # Index maps for target tuples
    tuple_to_idx = {}
    for idx, t in enumerate(tuples_nm1):
        tuple_to_idx[t] = idx

    M = np.zeros((dim_out, dim_in), dtype=np.float64)

    for col_t, lie_tuple in enumerate(tuples_n):
        for i in range(n):
            for j in range(i+1, n):
                a_i = lie_tuple[i]
                a_j = lie_tuple[j]

                # Residue matrix for this pair
                res_mat = res_matrices[(i, j)]

                # [a_i, a_j] = sum_c f[a_i, a_j, c] * basis[c]
                for c in range(DIM):
                    coeff = f[a_i][a_j][c]
                    if abs(coeff) < 1e-10:
                        continue

                    # New tuple: replace position j with c, remove position i
                    new_list = list(lie_tuple)
                    new_list[j] = c
                    new_tuple = tuple(new_list[:i] + new_list[i+1:])

                    if new_tuple not in tuple_to_idx:
                        continue

                    row_t = tuple_to_idx[new_tuple]

                    # Sign: (-1)^i for removing position i
                    # (This is the Koszul sign in the bar complex)
                    sign = (-1) ** i

                    # Combine Lie algebra and form contributions
                    for col_f in range(len(os_n)):
                        for row_f in range(len(os_nm1)):
                            if abs(res_mat[row_f, col_f]) < 1e-10:
                                continue
                            col = col_t * len(os_n) + col_f
                            row = row_t * len(os_nm1) + row_f
                            M[row, col] += sign * coeff * res_mat[row_f, col_f]

    return M


# ================================================================
# Main computation
# ================================================================

def compute_bar_cohomology(max_degree=3):
    """Compute bar cohomology H^n for n = 1,...,max_degree."""

    print("\n" + "=" * 60)
    print("sl_3 BAR COHOMOLOGY COMPUTATION")
    print("=" * 60)

    # Precompute weight decompositions
    decomps = {}
    for n in range(1, max_degree + 2):
        t0 = time.time()
        decomps[n] = weight_decomposition(n)
        t1 = time.time()
        total = sum(len(v) for v in decomps[n].values())
        nw = len(decomps[n])
        print(f"  g^{n}: {nw} weights, {total} tuples, {t1-t0:.2f}s")

    # Precompute OS residue matrices
    print("Precomputing OS residue matrices...")
    res_mats = {}
    for n in range(2, max_degree + 2):
        res_mats[n] = compute_residue_matrices(n)

    # Collect all weights
    all_weights = set()
    for n in range(1, max_degree + 2):
        all_weights.update(decomps[n].keys())
    print(f"Total distinct weights: {len(all_weights)}")

    results = {}

    for deg in range(1, max_degree + 1):
        print(f"\n--- Degree {deg} ---")
        t_start = time.time()

        os_dim = len(os_basis(deg))
        total_ker = 0
        total_im = 0
        total_chain = 0

        for w in sorted(all_weights):
            n_tuples = len(decomps[deg].get(w, []))
            if n_tuples == 0:
                continue

            chain_dim = n_tuples * os_dim
            total_chain += chain_dim

            # d_deg: B^deg_w -> B^{deg-1}_w
            if deg >= 2:
                M_out = bar_differential_block(deg, w, decomps[deg], decomps[deg-1],
                                                res_mats[deg])
                rank_out = np.linalg.matrix_rank(M_out, tol=1e-8)
                ker_dim = chain_dim - rank_out
            else:
                # d_1 maps to B^0 = C (vacuum).
                # At min weight, d_1 = 0 (no OPE at weight 1 gives vacuum)
                ker_dim = chain_dim

            # d_{deg+1}: B^{deg+1}_w -> B^{deg}_w
            if deg + 1 in decomps and deg + 1 in res_mats:
                n_tuples_p1 = len(decomps[deg+1].get(w, []))
                if n_tuples_p1 > 0:
                    M_in = bar_differential_block(deg+1, w, decomps[deg+1], decomps[deg],
                                                  res_mats[deg+1])
                    rank_in = np.linalg.matrix_rank(M_in, tol=1e-8)
                else:
                    rank_in = 0
            else:
                rank_in = 0

            total_ker += ker_dim
            total_im += rank_in

        H_n = total_ker - total_im
        t_end = time.time()
        results[deg] = H_n

        print(f"  Chain dim: {total_chain}, ker(d): {total_ker}, "
              f"im(d+1): {total_im}, H^{deg} = {H_n}  ({t_end-t_start:.1f}s)")

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    expected = {1: 8, 2: 36, 3: 204}
    for deg, val in results.items():
        exp = expected.get(deg, '?')
        match = "OK" if val == exp else ("NEW" if exp == '?' else "MISMATCH")
        print(f"  H^{deg} = {val}  (expected: {exp}) {match}")

    return results


results = compute_bar_cohomology(max_degree=3)
