"""Yangian bar cohomology via explicit RTT quadratic algebra.

The RTT Yangian Y(gl_N) has generators T^{(r)}_{ij} (r >= 1, 1 <= i,j <= N)
with relations from the RTT equation.

The relations come in two types:
1. Level-(0,s): [T^{(1)}, T^{(s)}] = linear (quadratic-linear)
   Quadratic part: T^{(1)} x T^{(s)} - T^{(s)} x T^{(1)}

2. Level-(r,s) with r >= 1:
   [T^{(r+1)}, T^{(s)}] - [T^{(r)}, T^{(s+1)}] = T^{(r)}*T^{(s)} - T^{(s)}*T^{(r)}
   This is HOMOGENEOUS quadratic (all terms degree 2).

We compute the Koszul dual A! = T(V*)/(R^perp) and its Hilbert function.
"""

import numpy as np
from itertools import product as cart_product


def gen_index(i, j, r, N):
    """Map generator T^{(r)}_{ij} to a linear index.
    i, j in {0, ..., N-1}, r in {1, ..., L}.
    Index = (r-1)*N^2 + i*N + j.
    """
    return (r - 1) * N * N + i * N + j


def build_rtt_relations(N, L):
    """Build the quadratic relation space R subset V tensor V for Y(gl_N)
    truncated to levels 1,...,L.

    Returns a matrix whose rows span R, in the basis of V tensor V.
    V has dim = N^2 * L.
    """
    d = N * N * L  # dim V
    relations = []

    # Type 1: from RTT at (r=0, s): [T^{(1)}, T^{(s)}] = linear
    # Quadratic part: T^{(1)}_{ij} x T^{(s)}_{kl} - T^{(s)}_{kl} x T^{(1)}_{ij}
    # for each (i,j,k,l) and s = 1,...,L
    for s in range(1, L + 1):
        for i, j, k, l in cart_product(range(N), repeat=4):
            row = np.zeros(d * d)
            a = gen_index(i, j, 1, N)  # T^{(1)}_{ij}
            b = gen_index(k, l, s, N)  # T^{(s)}_{kl}
            row[a * d + b] += 1   # T^{(1)} x T^{(s)}
            row[b * d + a] -= 1   # - T^{(s)} x T^{(1)}
            if np.any(np.abs(row) > 1e-15):
                relations.append(row)

    # Type 2: from RTT at (r, s) with r >= 1:
    # [T^{(r+1)}, T^{(s)}] - [T^{(r)}, T^{(s+1)}]
    #   = T^{(r)}_{kj} T^{(s)}_{il} - T^{(s)}_{kj} T^{(r)}_{il}
    #
    # As a quadratic relation in V x V:
    # T^{(r+1)}_{ij} x T^{(s)}_{kl} - T^{(s)}_{kl} x T^{(r+1)}_{ij}
    # - T^{(r)}_{ij} x T^{(s+1)}_{kl} + T^{(s+1)}_{kl} x T^{(r)}_{ij}
    # - T^{(r)}_{kj} x T^{(s)}_{il} + T^{(s)}_{kj} x T^{(r)}_{il}
    #
    # = 0 (the relation)
    for r in range(1, L):
        for s in range(1, L):
            if r + 1 > L or s + 1 > L:
                continue
            for i, j, k, l in cart_product(range(N), repeat=4):
                row = np.zeros(d * d)

                # [T^{(r+1)}_{ij}, T^{(s)}_{kl}]
                a1 = gen_index(i, j, r + 1, N)
                b1 = gen_index(k, l, s, N)
                row[a1 * d + b1] += 1
                row[b1 * d + a1] -= 1

                # -[T^{(r)}_{ij}, T^{(s+1)}_{kl}]
                a2 = gen_index(i, j, r, N)
                b2 = gen_index(k, l, s + 1, N)
                row[a2 * d + b2] -= 1
                row[b2 * d + a2] += 1

                # -T^{(r)}_{kj} x T^{(s)}_{il}
                c1 = gen_index(k, j, r, N)
                d1 = gen_index(i, l, s, N)
                row[c1 * d + d1] -= 1

                # +T^{(s)}_{kj} x T^{(r)}_{il}
                c2 = gen_index(k, j, s, N)
                d2 = gen_index(i, l, r, N)
                row[c2 * d + d2] += 1

                if np.any(np.abs(row) > 1e-15):
                    relations.append(row)

    if not relations:
        return np.zeros((0, d * d))

    R = np.array(relations, dtype=float)
    return R


def compute_koszul_dual_dims(N, L, max_degree):
    """Compute dim(A!)_n for n = 0, ..., max_degree.

    A! = T(V*)/(R^perp) where R^perp is the annihilator of R in V* x V*.
    """
    d = N * N * L  # dim V
    R = build_rtt_relations(N, L)

    print(f"  N={N}, L={L}: dim V = {d}, num raw relations = {R.shape[0]}")

    # Compute rank of R
    if R.shape[0] > 0:
        rank_R = np.linalg.matrix_rank(R, tol=1e-10)
    else:
        rank_R = 0
    dim_Rperp = d * d - rank_R
    print(f"  rank R = {rank_R}, dim R^perp = {dim_Rperp}")

    # Compute R^perp basis (null space of R^T)
    if R.shape[0] > 0 and rank_R < d * d:
        U, S, Vt = np.linalg.svd(R, full_matrices=True)
        tol = 1e-10 * S[0] if len(S) > 0 else 1e-10
        rank_R = int(np.sum(S > tol))
        # R^perp = rows of Vt from rank_R onwards
        Rperp = Vt[rank_R:]  # (dim_Rperp x d^2)
    elif rank_R == d * d:
        Rperp = np.zeros((0, d * d))
    else:
        Rperp = np.eye(d * d)

    dims = [0] * (max_degree + 1)
    dims[0] = 1
    if max_degree >= 1:
        dims[1] = d

    if max_degree < 2:
        return dims

    # (A!)_2 = V*^{x2} / R^perp
    dims[2] = d * d - Rperp.shape[0]
    print(f"  (A!)_2 = {dims[2]}")

    # For higher degrees, iteratively compute the ideal
    # I_n = sum_{i=0}^{n-2} V^{xi} x R^perp x V^{x(n-2-i)}
    # (A!)_n = d^n - dim(I_n)

    # Track: basis of I_n (as rows of a matrix in R^{d^n})
    # Start with I_2 = R^perp
    prev_ideal_basis = Rperp  # shape (dim_Rperp, d^2)

    for n in range(3, max_degree + 1):
        dim_n = d ** n

        if dim_n > 50000:
            print(f"  Degree {n}: skipping (dim = {dim_n} too large)")
            dims[n] = -1
            break

        # I_n = (I_{n-1} x V) + (V^{x(n-2)} x R^perp)
        # Part 1: I_{n-1} x V (tensor on the right with V*)
        num_prev = prev_ideal_basis.shape[0]
        dim_prev = d ** (n - 1)

        rows1 = []
        for idx in range(num_prev):
            for a in range(d):
                row = np.zeros(dim_n)
                for I in range(dim_prev):
                    val = prev_ideal_basis[idx, I]
                    if abs(val) > 1e-15:
                        row[I * d + a] = val
                rows1.append(row)

        # Part 2: V^{x(n-2)} x R^perp (R^perp in last two positions)
        dim_prefix = d ** (n - 2)
        num_rp = Rperp.shape[0]

        rows2 = []
        for p in range(dim_prefix):
            for r in range(num_rp):
                row = np.zeros(dim_n)
                for q in range(d * d):
                    val = Rperp[r, q]
                    if abs(val) > 1e-15:
                        row[p * d * d + q] = val
                rows2.append(row)

        # Combine
        all_rows = rows1 + rows2
        if all_rows:
            combined = np.array(all_rows, dtype=float)
            rank_In = np.linalg.matrix_rank(combined, tol=1e-10)

            # Get basis for I_n (for next iteration)
            U, S, Vt = np.linalg.svd(combined, full_matrices=False)
            tol_svd = 1e-10 * S[0] if len(S) > 0 else 1e-10
            rank_In = int(np.sum(S > tol_svd))
            prev_ideal_basis = Vt[:rank_In]
        else:
            rank_In = 0
            prev_ideal_basis = np.zeros((0, dim_n))

        dims[n] = dim_n - rank_In
        print(f"  (A!)_{n} = {dims[n]}  [d^{n}={dim_n}, rank I_{n}={rank_In}]")

    return dims


def main():
    print("=" * 60)
    print("YANGIAN BAR COHOMOLOGY: RTT QUADRATIC ALGEBRA")
    print("=" * 60)

    N = 2  # gl_2

    # Test with different truncation levels
    for L in range(1, 5):
        print(f"\n--- Y(gl_{N}) at levels <= {L} ---")
        max_deg = min(4, 3 if L >= 3 else 4)
        dims = compute_koszul_dual_dims(N, L, max_deg)
        print(f"  Result: (A!)_n = {dims}")

    # Also try: only Type 1 relations (just antisymmetric cross-terms)
    print("\n--- Type 1 only (pure antisymmetric) at L=1 ---")
    d = N * N * 1
    R_antisym = []
    for a in range(d):
        for b in range(a + 1, d):
            row = np.zeros(d * d)
            row[a * d + b] = 1
            row[b * d + a] = -1
            R_antisym.append(row)
    R_antisym = np.array(R_antisym)
    rank = np.linalg.matrix_rank(R_antisym)
    print(f"  rank R = {rank}, (A!)_2 = {d*d - (d*d - rank)} = {rank}")

    # Check: what if the relation space is LARGER?
    # The Type 2 RTT relations at (r=1,s=1) give ADDITIONAL relations
    # beyond antisymmetry
    print("\n--- Detailed relation structure ---")
    for L in range(1, 4):
        R = build_rtt_relations(N, L)
        d = N * N * L
        if R.shape[0] > 0:
            rank_R = np.linalg.matrix_rank(R, tol=1e-10)
        else:
            rank_R = 0
        pure_antisym = d * (d - 1) // 2
        print(f"  L={L}: dim V={d}, pure antisym={pure_antisym}, "
              f"total rank R={rank_R}, "
              f"extra relations={rank_R - min(pure_antisym, rank_R)}")

    # Summary check against Master Table
    print("\n--- Comparison with Master Table ---")
    print("  Master Table: H^1=4, H^2=10, H^3=28")
    print("  3^n+1:        H^1=4, H^2=10, H^3=28")


if __name__ == "__main__":
    main()
