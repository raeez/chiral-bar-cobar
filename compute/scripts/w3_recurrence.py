#!/usr/bin/env python3
"""Search for P-recursive recurrences matching W₃ bar cohomology.

For algebraic GFs, the coefficients satisfy:
Σ_{j=0}^{d} p_j(n) · a(n-j) = 0
where p_j are polynomials in n.

With 4 terms, try all such recurrences and predict more terms.
Also verify on known sequences (sl₂/Riordan, Virasoro/Motzkin).
"""
from fractions import Fraction as F

# Known sequences
SL2 = [3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298]  # R(n+3)
VIR = [1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610]  # M(n+1)-M(n)
W3 = [2, 5, 16, 52]
BG = [2, 4, 10, 26, 70, 192, 534, 1500, 4246, 12092]  # β-gamma
SL3 = [8, 36, 204]


def find_recurrence(seq, label, max_order=3, max_poly_deg=2, verbose=True):
    """Find P-recursive recurrence for seq.

    Try: Σ_{j=0}^{order} (Σ_{k=0}^{deg} c_{jk} n^k) · a(n-j) = 0
    where a(n) = seq[n-1] (1-indexed).

    Parameters: order = recurrence depth, deg = polynomial degree.
    Total unknowns = (order+1) * (deg+1).
    """
    N = len(seq)
    a = {i+1: F(seq[i]) for i in range(N)}  # 1-indexed

    if verbose:
        print(f"\n{'='*60}")
        print(f"Recurrence search for {label}: {seq[:min(6,N)]}")

    results = []

    for order in range(1, max_order + 1):
        for deg in range(0, max_poly_deg + 1):
            nvars = (order + 1) * (deg + 1)

            # Build equations: for n = order+1, order+2, ..., N
            # (need a(n), a(n-1), ..., a(n-order) to all be defined)
            neqs = N - order
            if neqs < 1 or neqs > nvars + 2:
                continue

            rows = []
            for n in range(order + 1, N + 1):
                row = []
                for j in range(order + 1):
                    for k in range(deg + 1):
                        row.append(F(n)**k * a[n - j])
                rows.append(row)

            # Find null space
            sol = solve_homogeneous_exact(rows, nvars)
            if sol is None:
                continue

            # Check for trivial solution
            if all(s == 0 for s in sol):
                continue

            # Extract polynomial coefficients
            polys = []
            for j in range(order + 1):
                p = [sol[j * (deg + 1) + k] for k in range(deg + 1)]
                polys.append(p)

            # Verify on all known terms
            ok = True
            for n in range(order + 1, N + 1):
                val = F(0)
                for j in range(order + 1):
                    for k in range(deg + 1):
                        val += polys[j][k] * F(n)**k * a[n - j]
                if val != 0:
                    ok = False
                    break

            if not ok:
                continue

            # Predict next terms
            predicted = list(seq)
            all_int = True
            for step in range(10):
                n = N + step + 1
                # Σ_{j=0}^{order} p_j(n) · a(n-j) = 0
                # p_0(n) · a(n) = -Σ_{j=1}^{order} p_j(n) · a(n-j)
                coeff_an = sum(polys[0][k] * F(n)**k for k in range(deg + 1))
                if coeff_an == 0:
                    break
                rhs = F(0)
                for j in range(1, order + 1):
                    idx = n - j
                    if idx < 1 or idx > len(predicted):
                        break
                    a_val = F(predicted[idx - 1])
                    for k in range(deg + 1):
                        rhs -= polys[j][k] * F(n)**k * a_val
                else:
                    a_n = rhs / coeff_an
                    if a_n.denominator != 1 or a_n <= 0:
                        all_int = False
                    predicted.append(a_n if a_n.denominator == 1 else float(a_n))
                    continue
                break

            if verbose:
                tag = "*** ALL INT ***" if all_int and len(predicted) > N + 2 else ""
                print(f"\n  order={order}, poly_deg={deg}: {tag}")
                for j, p in enumerate(polys):
                    ps = " + ".join(f"{p[k]}·n^{k}" if k > 0 else str(p[k])
                                    for k in range(len(p)) if p[k] != 0)
                    print(f"    p_{j}(n) = {ps or '0'}")
                if len(predicted) > N:
                    extra = predicted[N:]
                    print(f"    Predicted: {[int(x) if isinstance(x, F) and x.denominator==1 else x for x in extra[:6]]}")
                    if all_int and len(extra) >= 3:
                        # Check growth rate
                        vals = [float(predicted[i]) for i in range(max(1, N-1), min(N+5, len(predicted)))]
                        ratios = [vals[i]/vals[i-1] for i in range(1, len(vals)) if vals[i-1] != 0]
                        print(f"    Ratios: {[f'{r:.4f}' for r in ratios]}")

            if all_int and len(predicted) > N + 2:
                results.append({
                    'order': order, 'deg': deg,
                    'polys': polys,
                    'predicted': predicted,
                })

    return results


def solve_homogeneous_exact(rows, nvars):
    """Find non-trivial solution with 1-dim null space."""
    if not rows:
        return None
    m = len(rows)
    n = nvars

    A = [[F(0)] * n for _ in range(m)]
    for i, row in enumerate(rows):
        for j in range(min(len(row), n)):
            A[i][j] = row[j]

    pivot_cols = []
    r = 0
    for col in range(n):
        piv = None
        for row in range(r, m):
            if A[row][col] != 0:
                piv = row
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][col]
        for row in range(m):
            if row != r and A[row][col] != 0:
                fac = A[row][col] / pv
                for c2 in range(n):
                    A[row][c2] -= fac * A[r][c2]
        pivot_cols.append(col)
        r += 1

    rank = r
    if rank != n - 1:
        return None

    free_cols = [c for c in range(n) if c not in pivot_cols]
    if len(free_cols) != 1:
        return None
    free = free_cols[0]

    sol = [F(0)] * n
    sol[free] = F(1)
    for i in range(rank - 1, -1, -1):
        pc = pivot_cols[i]
        val = sum(A[i][j] * sol[j] for j in range(n) if j != pc)
        sol[pc] = -val / A[i][pc]

    # Clear denominators
    from math import lcm as mlcm
    from functools import reduce
    denoms = [s.denominator for s in sol if s != 0]
    if denoms:
        common = reduce(mlcm, denoms)
        sol = [F(int(s * common)) for s in sol]
    from math import gcd as mgcd
    nums = [abs(int(s)) for s in sol if s != 0]
    if nums:
        g = reduce(mgcd, nums)
        if g > 0:
            sol = [F(int(s) // g) for s in sol]

    return sol


def search_higher_order(seq, label, max_order=4, max_deg=3):
    """Search recurrences allowing higher order and polynomial degree.
    Accept multi-dim null space and try all basis combinations."""
    N = len(seq)
    a = {i+1: F(seq[i]) for i in range(N)}

    print(f"\n{'='*60}")
    print(f"Extended recurrence search for {label}: {seq}")

    for order in range(1, max_order + 1):
        for deg in range(0, max_deg + 1):
            nvars = (order + 1) * (deg + 1)
            neqs = N - order

            if neqs < 1 or nvars < 2:
                continue
            if neqs >= nvars:
                continue  # overdetermined, handled by find_recurrence

            # Build system
            rows = []
            for n in range(order + 1, N + 1):
                row = []
                for j in range(order + 1):
                    for k in range(deg + 1):
                        row.append(F(n)**k * a[n - j])
                rows.append(row)

            # Gaussian elimination
            A = [row[:] for row in rows]
            m = len(A)
            pivot_cols = []
            r = 0
            for col in range(nvars):
                piv = None
                for row in range(r, m):
                    if A[row][col] != 0:
                        piv = row
                        break
                if piv is None:
                    continue
                A[r], A[piv] = A[piv], A[r]
                pv = A[r][col]
                for row in range(m):
                    if row != r and A[row][col] != 0:
                        fac = A[row][col] / pv
                        for c2 in range(nvars):
                            A[row][c2] -= fac * A[r][c2]
                pivot_cols.append(col)
                r += 1

            rank = r
            null_dim = nvars - rank
            if null_dim < 1 or null_dim > 3:
                continue

            # Find basis vectors for null space
            free_cols = [c for c in range(nvars) if c not in pivot_cols]
            basis = []
            for fc in free_cols:
                sol = [F(0)] * nvars
                sol[fc] = F(1)
                for i in range(rank - 1, -1, -1):
                    pc = pivot_cols[i]
                    val = sum(A[i][j] * sol[j] for j in range(nvars) if j != pc)
                    sol[pc] = -val / A[i][pc]
                basis.append(sol)

            # For 1-dim: direct
            if null_dim == 1:
                sol = basis[0]
                polys = []
                for j in range(order + 1):
                    p = [sol[j * (deg + 1) + k] for k in range(deg + 1)]
                    polys.append(p)

                result = try_predict(polys, seq, order, deg)
                if result is not None:
                    print(f"  order={order}, deg={deg}, null_dim=1: {result}")

            # For 2-dim: search over combinations
            elif null_dim == 2:
                found_any = False
                for num in range(-10, 11):
                    for den in range(1, 11):
                        from math import gcd
                        if gcd(abs(num), den) != 1:
                            continue
                        t = F(num, den)
                        sol = [basis[0][i] + t * basis[1][i] for i in range(nvars)]
                        polys = []
                        for j in range(order + 1):
                            p = [sol[j * (deg + 1) + k] for k in range(deg + 1)]
                            polys.append(p)

                        result = try_predict(polys, seq, order, deg)
                        if result is not None and result.get('all_int'):
                            if not found_any:
                                print(f"  order={order}, deg={deg}, null_dim=2:")
                                found_any = True
                            print(f"    t={t}: pred={result['predicted'][N:N+6]}")


def try_predict(polys, seq, order, deg):
    """Try to predict next terms from recurrence polys."""
    N = len(seq)
    predicted = list(seq)
    all_int = True

    for step in range(8):
        n = N + step + 1
        coeff_an = sum(polys[0][k] * F(n)**k for k in range(deg + 1))
        if coeff_an == 0:
            break
        rhs = F(0)
        for j in range(1, order + 1):
            idx = n - j
            if idx < 1 or idx > len(predicted):
                break
            a_val = F(predicted[idx - 1]) if isinstance(predicted[idx - 1], int) else predicted[idx - 1]
            if not isinstance(a_val, F):
                a_val = F(a_val)
            for k in range(deg + 1):
                rhs -= polys[j][k] * F(n)**k * a_val
        else:
            a_n = rhs / coeff_an
            if a_n.denominator != 1 or a_n <= 0:
                all_int = False
                predicted.append(float(a_n))
            else:
                predicted.append(int(a_n))
            continue
        break

    if len(predicted) <= N:
        return None

    return {'predicted': predicted, 'all_int': all_int, 'order': order, 'deg': deg}


if __name__ == "__main__":
    # Verify on known sequences
    print("VERIFICATION ON KNOWN SEQUENCES:")
    find_recurrence(SL2, "sl₂ (Riordan)")
    find_recurrence(VIR, "Virasoro (Motzkin diff)")
    find_recurrence(BG, "β-gamma")

    # Search for W₃
    print("\n\nW₃ SEARCH:")
    find_recurrence(W3, "W₃", max_order=3, max_poly_deg=2)

    # Extended search with multi-dim null space
    search_higher_order(W3, "W₃ (extended)")

    # Also try sl₃
    print("\n\nsl₃ SEARCH:")
    find_recurrence(SL3, "sl₃", max_order=2, max_poly_deg=1)
    search_higher_order(SL3, "sl₃ (extended)")
