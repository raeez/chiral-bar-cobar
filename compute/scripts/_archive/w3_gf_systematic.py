#!/usr/bin/env python3
"""Systematic search for algebraic GF of W₃ bar cohomology.

Known: 2, 5, 16, 52 (H^1 through H^4).
Goal: find H^5, H^6, ... by fitting algebraic equations.

Approach: Find all bivariate polynomials Q(x, P) = 0 of bounded
bidegree with exactly the right number of free parameters.
"""
from fractions import Fraction as F
from functools import reduce
from math import lcm, gcd

KNOWN = [0, 2, 5, 16, 52]  # p[0]=0, p[1]=2, ...
N = len(KNOWN) - 1  # = 4 known coefficients

def ps_mult(a, b, n):
    """Multiply power series truncated to n terms."""
    c = [F(0)] * n
    for i in range(min(len(a), n)):
        if a[i] == 0: continue
        for j in range(min(len(b), n - i)):
            if b[j] == 0: continue
            c[i+j] += a[i] * b[j]
    return c

def ps_pow(a, k, n):
    """Power series a^k truncated to n terms."""
    if k == 0:
        r = [F(0)] * n
        r[0] = F(1)
        return r
    if k == 1:
        return list(a[:n]) + [F(0)] * max(0, n - len(a))
    half = ps_pow(a, k // 2, n)
    result = ps_mult(half, half, n)
    if k % 2 == 1:
        result = ps_mult(result, a, n)
    return result

# Precompute P^j for j = 0, 1, 2, 3, 4
NTERMS = 12
p_series = [F(0)] * NTERMS
for i, v in enumerate(KNOWN):
    if i < NTERMS:
        p_series[i] = F(v)

P_POWERS = []
for j in range(5):
    P_POWERS.append(ps_pow(p_series, j, NTERMS))

def search_algebraic(deg_P, deg_x, known=KNOWN):
    """Search for Q(x, P) = 0 of degree deg_P in P and deg_x in x.

    Q(x, P) = Σ_{j=0}^{deg_P} Σ_{i=0}^{deg_x} c_{ij} x^i P^j = 0

    The coefficient of x^k in Q(x, P(x)) gives a linear equation in the c_{ij}.
    """
    n = len(known) - 1  # number of known coefficients (excluding p[0]=0)
    p = [F(v) for v in known]

    # Variables: c_{ij} for i=0..deg_x, j=0..deg_P
    # Total: (deg_x+1)*(deg_P+1) variables
    nvars = (deg_x + 1) * (deg_P + 1)

    def var_idx(i, j):
        return j * (deg_x + 1) + i

    # Precompute P^j series
    nterms = n + 3
    p_ext = list(p) + [F(0)] * max(0, nterms - len(p))
    ppow = [ps_pow(p_ext, j, nterms) for j in range(deg_P + 1)]

    # x^i * P^j at order x^k = ppow[j][k-i] if k-i >= 0
    # Coefficient of x^k in Q(x, P(x)):
    # Σ_{j,i} c_{ij} * ppow[j][k-i]

    # Build equations for k = 0, 1, ..., n+1
    # k=0 always gives c_{00} = 0 (from ppow[0][0]=1, ppow[j][0]=0 for j≥1 since p[0]=0)
    # Actually ppow[0][0]=1 and for j≥1, ppow[j][0] = p[0]^j = 0.
    # So x^0 equation: c_{00}*1 = 0 → c_{00} = 0.

    rows = []
    for k in range(0, n + 2):  # x^0 through x^{n+1}
        row = [F(0)] * nvars
        for j in range(deg_P + 1):
            for i in range(deg_x + 1):
                idx = k - i
                if 0 <= idx < nterms:
                    row[var_idx(i, j)] += ppow[j][idx]
        rows.append(row)

    # Use x^0 through x^n (n+1 equations) to determine the solution space.
    # We need a 1-dimensional null space for a unique prediction.
    # Required: nvars - 1 = n + 1 (including c_{00}=0 constraint)
    # Actually: c_{00}=0 is one of the equations (k=0).
    # So effectively n+1 equations (k=0..n), nvars unknowns.
    # Need rank = nvars - 1 for 1-dim null space.
    # Then k=n+1 equation predicts p_{n+1}.

    # Gaussian elimination on rows[0..n]
    A = [row[:] for row in rows[:n+1]]
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

    if null_dim != 1:
        return None  # not unique

    # Find the free variable
    free_cols = [c for c in range(nvars) if c not in pivot_cols]
    if len(free_cols) != 1:
        return None
    free = free_cols[0]

    # Back-substitute to find solution
    sol = [F(0)] * nvars
    sol[free] = F(1)
    for i in range(rank - 1, -1, -1):
        pc = pivot_cols[i]
        val = F(0)
        for j in range(nvars):
            if j != pc:
                val += A[i][j] * sol[j]
        sol[pc] = -val / A[i][pc]

    # Clear denominators
    denoms = [s.denominator for s in sol if s != 0]
    if denoms:
        common = reduce(lcm, denoms)
        sol = [F(s * common) for s in sol]
    # Also simplify by GCD
    nums = [abs(int(s)) for s in sol if s != 0]
    if nums:
        g = reduce(gcd, nums)
        sol = [F(int(s) // g) for s in sol]

    # Extract coefficients
    c = {}
    for j in range(deg_P + 1):
        for i in range(deg_x + 1):
            v = sol[var_idx(i, j)]
            if v != 0:
                c[(i, j)] = v

    # Check: is the P^{deg_P} coefficient non-trivial?
    has_top = any(c.get((i, deg_P), F(0)) != 0 for i in range(deg_x + 1))
    if not has_top:
        return None  # lower degree in P

    # Now predict p_{n+1} from the x^{n+1} equation
    k = n + 1
    # Coefficient of x^{n+1}: Σ c_{ij} * ppow[j][k-i] = 0
    # ppow[j][k-i] for j>=1 may involve p_{n+1} (unknown).
    # p_{n+1} appears in ppow[1][n+1] = p_{n+1}.
    # ppow[j][n+1] for j≥2: depends on lower p's only (since p[0]=0).
    # Actually ppow[j][n+1] = Σ_{i₁+...+i_j=n+1} p[i₁]...p[i_j]
    # Since p[0]=0, each i_k ≥ 1, so n+1 = i₁+...+i_j with i_k ≥ 1.
    # For j=1: ppow[1][n+1] = p[n+1] (unknown)
    # For j≥2: ppow[j][n+1] = sum over partitions of n+1 into j parts ≥ 1
    #   The only way to get p_{n+1} is if one part equals n+1 and rest are 0,
    #   but parts ≥ 1, so the partition (n+1, 0, ..., 0) is invalid for j≥2.
    #   Wait: for j=2, ppow[2][n+1] = Σ_{a+b=n+1, a≥1, b≥1} p[a]*p[b].
    #   None of these involve p_{n+1} (since both a,b ≥ 1 and a+b=n+1,
    #   the max of a,b is n, not n+1). ✓
    # So p_{n+1} appears ONLY through ppow[1][n+1] = p_{n+1}.
    # Its coefficient in the x^{n+1} equation is: Σ_i c_{i,1} (from j=1 terms
    # where ppow[1][k-i] = p_{n+1} means k-i = n+1 means i=0).
    # So coeff of p_{n+1} = c_{0,1}.

    coeff_pnext = c.get((0, 1), F(0))
    if coeff_pnext == 0:
        return None  # can't determine p_{n+1}

    # Known part of x^{n+1} equation (everything except p_{n+1}):
    known_part = F(0)
    for j in range(deg_P + 1):
        for i in range(deg_x + 1):
            cv = c.get((i, j), F(0))
            if cv == 0:
                continue
            idx = k - i
            if 0 <= idx < nterms:
                if j == 1 and idx == n + 1:
                    continue  # this is the p_{n+1} term
                known_part += cv * ppow[j][idx]

    p_next = -known_part / coeff_pnext

    # Compute discriminant (for degree 2 in P)
    disc_info = None
    if deg_P == 2:
        # A(x) = Σ c_{i,2} x^i, B(x) = Σ c_{i,1} x^i, C(x) = Σ c_{i,0} x^i
        A_poly = [c.get((i, 2), F(0)) for i in range(deg_x + 1)]
        B_poly = [c.get((i, 1), F(0)) for i in range(deg_x + 1)]
        C_poly = [c.get((i, 0), F(0)) for i in range(deg_x + 1)]
        B2 = ps_mult(B_poly, B_poly, 2*deg_x + 2)
        AC = ps_mult(A_poly, C_poly, 2*deg_x + 2)
        disc = [B2[i] - 4*AC[i] if i < len(B2) else F(0) for i in range(2*deg_x + 2)]
        disc_info = {'A': A_poly, 'B': B_poly, 'C': C_poly, 'disc': disc}

    return {
        'deg_P': deg_P, 'deg_x': deg_x,
        'coeffs': c, 'sol': sol,
        'p_next': p_next,
        'disc_info': disc_info,
        'nvars': nvars, 'rank': rank,
    }


def format_bivariate(c, deg_x, deg_P):
    """Format bivariate polynomial."""
    terms = []
    for j in range(deg_P + 1):
        for i in range(deg_x + 1):
            v = c.get((i, j), F(0))
            if v == 0:
                continue
            parts = []
            if v != 1 or (i == 0 and j == 0):
                parts.append(str(v))
            if i > 0:
                parts.append(f"x^{i}" if i > 1 else "x")
            if j > 0:
                parts.append(f"P^{j}" if j > 1 else "P")
            terms.append("·".join(parts) if parts else str(v))
    return " + ".join(terms)


def predict_sequence(result, n_extra=8):
    """Given an algebraic equation, predict many more terms."""
    c = result['coeffs']
    deg_P = result['deg_P']
    deg_x = result['deg_x']

    p = list(KNOWN)
    nterms = N + n_extra + 2
    p_ext = p + [F(0)] * max(0, nterms - len(p))

    for step in range(n_extra):
        k = N + step + 1  # predicting p[k]
        ppow = [ps_pow(p_ext, j, nterms) for j in range(deg_P + 1)]

        coeff_pk = c.get((0, 1), F(0))
        if coeff_pk == 0:
            break

        known_part = F(0)
        for j in range(deg_P + 1):
            for i in range(deg_x + 1):
                cv = c.get((i, j), F(0))
                if cv == 0:
                    continue
                idx = k - i
                if 0 <= idx < nterms:
                    if j == 1 and idx == k:
                        continue
                    known_part += cv * ppow[j][idx]

        pk = -known_part / coeff_pk
        p_ext[k] = pk

    return p_ext[:N + n_extra + 1]


def main():
    print("Systematic algebraic equation search for W₃ bar cohomology")
    print(f"Known: {KNOWN[1:]} (H^1 through H^{N})")
    print()

    results = []

    for deg_P in range(1, 5):
        for deg_x in range(0, 6):
            nvars = (deg_x + 1) * (deg_P + 1)
            # Need nvars - 1 = N + 1 (n+1 equations including x^0)
            # i.e., nvars = N + 2 = 6
            if nvars != N + 2:
                continue

            r = search_algebraic(deg_P, deg_x)
            if r is None:
                continue

            results.append(r)

    # Sort by whether prediction is integer
    results.sort(key=lambda r: (r['p_next'].denominator != 1, r['deg_P'] + r['deg_x']))

    for r in results:
        pn = r['p_next']
        is_int = pn.denominator == 1 and pn > 0
        tag = "*** INTEGER ***" if is_int else ""
        print(f"deg(P)={r['deg_P']}, deg(x)={r['deg_x']}: "
              f"p_{N+1} = {pn} = {float(pn):.4f} {tag}")
        print(f"  Q(x,P) = {format_bivariate(r['coeffs'], r['deg_x'], r['deg_P'])}")

        if r['disc_info']:
            d = r['disc_info']
            print(f"  Δ(x) = {' + '.join(f'{c}x^{i}' for i,c in enumerate(d['disc']) if c!=0)}")

        if is_int:
            seq = predict_sequence(r, 10)
            print(f"  Extended sequence: {[int(s) if s.denominator==1 else float(s) for s in seq[1:]]}")
            # Check growth rate
            ratios = []
            for i in range(2, len(seq)):
                if seq[i-1] != 0 and seq[i] != 0:
                    ratios.append(float(seq[i] / seq[i-1]))
            if ratios:
                print(f"  Ratios: {[f'{r:.3f}' for r in ratios]}")
                print(f"  Apparent growth rate: {ratios[-1]:.4f}")
        print()

    # Also try with relaxed constraint: nvars = N+3 (2-dim null space)
    # and impose growth rate constraint
    print("\n" + "="*60)
    print("Searching with relaxed constraints (2-dim null space + growth rate)...")
    for deg_P in [2]:
        for deg_x in range(1, 6):
            nvars = (deg_x + 1) * (deg_P + 1)
            if nvars != N + 3:  # 7 for W₃
                continue
            search_with_growth_constraint(deg_P, deg_x)


def search_with_growth_constraint(deg_P, deg_x, growth_rate=None):
    """Search with 2-dim null space, adding growth rate constraint."""
    known = KNOWN
    n = len(known) - 1
    p = [F(v) for v in known]
    nvars = (deg_x + 1) * (deg_P + 1)

    def var_idx(i, j):
        return j * (deg_x + 1) + i

    nterms = n + 3
    p_ext = list(p) + [F(0)] * max(0, nterms - len(p))
    ppow = [ps_pow(p_ext, j, nterms) for j in range(deg_P + 1)]

    # Build equations
    rows = []
    for k in range(0, n + 1):
        row = [F(0)] * nvars
        for j in range(deg_P + 1):
            for i in range(deg_x + 1):
                idx = k - i
                if 0 <= idx < nterms:
                    row[var_idx(i, j)] += ppow[j][idx]
        rows.append(row)

    # Try different growth rates
    for gr in [3, 4, 5, 6, 7, 8]:
        # Add constraint: Δ(1/gr) = 0 for quadratic case
        # For deg_P = 2: Δ = B²-4AC where A = Σ c_{i2}x^i, B = Σ c_{i1}x^i, C = Σ c_{i0}x^i
        # Δ(1/gr) = (Σ c_{i1}/gr^i)² - 4(Σ c_{i2}/gr^i)(Σ c_{i0}/gr^i)
        # This is quadratic in the c's, not linear! So it doesn't fit into our linear framework.

        # Instead, try: set the growth rate by requiring p[k]/p[k-1] → gr
        # Or: try a specific discriminant form Δ(x) = (1-gr·x)(1+αx) and solve.

        # Actually let's just try to find the null space of the linear system
        # and parametrize solutions, then pick the one giving integer predictions.
        pass

    # Find 2-dim null space
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
    print(f"\n  deg(P)={deg_P}, deg(x)={deg_x}: nvars={nvars}, rank={rank}, null_dim={null_dim}")

    if null_dim != 2:
        print(f"  Null space dim = {null_dim}, need 2. Skipping.")
        return

    # Find 2 basis vectors for null space
    free_cols = [c for c in range(nvars) if c not in pivot_cols]
    if len(free_cols) != 2:
        return

    basis = []
    for fc_idx in range(2):
        sol = [F(0)] * nvars
        sol[free_cols[fc_idx]] = F(1)
        for i in range(rank - 1, -1, -1):
            pc = pivot_cols[i]
            val = F(0)
            for j in range(nvars):
                if j != pc:
                    val += A[i][j] * sol[j]
            sol[pc] = -val / A[i][pc]
        basis.append(sol)

    # Parametrize: sol = α·basis[0] + β·basis[1]
    # Try rational values of α/β to find integer predictions
    print(f"  Searching for integer predictions over rational α/β...")

    best = None
    for num in range(-20, 21):
        for den in range(1, 21):
            if gcd(abs(num), den) != 1:
                continue
            # sol = basis[0] + (num/den) * basis[1]
            t = F(num, den)
            sol = [basis[0][i] + t * basis[1][i] for i in range(nvars)]

            # Check P^{deg_P} coefficient is nonzero
            has_top = any(sol[var_idx(i, deg_P)] != 0 for i in range(deg_x + 1))
            if not has_top:
                continue

            coeff_b0 = sol[var_idx(0, 1)]
            if coeff_b0 == 0:
                continue

            # Predict p_{n+1}
            c = {}
            for j in range(deg_P + 1):
                for i in range(deg_x + 1):
                    v = sol[var_idx(i, j)]
                    if v != 0:
                        c[(i, j)] = v

            k_pred = n + 1
            known_part = F(0)
            for j in range(deg_P + 1):
                for i in range(deg_x + 1):
                    cv = c.get((i, j), F(0))
                    if cv == 0:
                        continue
                    idx = k_pred - i
                    if 0 <= idx < nterms:
                        if j == 1 and idx == k_pred:
                            continue
                        known_part += cv * ppow[j][idx]

            p5 = -known_part / coeff_b0
            if p5 > 0 and p5.denominator == 1:
                # Also predict p6
                p_ext2 = list(p_ext)
                p_ext2[k_pred] = p5
                ppow2 = [ps_pow(p_ext2, j, nterms) for j in range(deg_P + 1)]
                k6 = k_pred + 1
                kp2 = F(0)
                for j in range(deg_P + 1):
                    for i in range(deg_x + 1):
                        cv = c.get((i, j), F(0))
                        if cv == 0:
                            continue
                        idx = k6 - i
                        if 0 <= idx < nterms:
                            if j == 1 and idx == k6:
                                continue
                            kp2 += cv * ppow2[j][idx]
                p6 = -kp2 / coeff_b0

                both_int = p6 > 0 and p6.denominator == 1
                if both_int:
                    print(f"  α/β={num}/{den}: p₅={int(p5)}, p₆={int(p6)}")
                    if best is None or int(p5) < best[0]:
                        best = (int(p5), int(p6), t, c)

    if best:
        print(f"\n  *** Best integer solution: p₅={best[0]}, p₆={best[1]} ***")


if __name__ == "__main__":
    main()
