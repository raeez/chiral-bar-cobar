#!/usr/bin/env python3
"""Find algebraic generating function for W₃ bar cohomology.

Known terms: dim H^n(B(W₃)) = 2, 5, 16, 52, ...
Strategy: Fit P(x) = 2x + 5x² + 16x³ + 52x⁴ + ... to algebraic equations
of increasing degree/complexity, find which ones are consistent and predict
the next terms.

For sl₂: P satisfies quadratic x(1+x)P² - (1+x)P + 1 = 0 (Riordan GF).
For Vir: P satisfies x²Q² - (1-x)Q + 1 = 0 (Motzkin GF).
Both have discriminant Δ(x) = 1-2x-3x² = (1-3x)(1+x).

For W₃: expect algebraic, sharing discriminant with sl₃.
Growth rate should be 8^n (dim sl₃ = 8).
"""
from fractions import Fraction as F
from itertools import product as iprod

# Known W₃ bar cohomology dimensions
W3_KNOWN = [2, 5, 16, 52]  # H^1, H^2, H^3, H^4

# Also useful: sl₃ first values
SL3_KNOWN = [8, 36, 204]  # H^1, H^2, H^3

def power_series_mult(a, b, nterms):
    """Multiply two power series (lists of coefficients) through nterms."""
    c = [F(0)] * nterms
    for i in range(min(len(a), nterms)):
        if a[i] == 0:
            continue
        for j in range(min(len(b), nterms - i)):
            c[i+j] += a[i] * b[j]
    return c

def try_quadratic_fit(known, label=""):
    """Try to fit P(x) = Σ a_n x^n to A(x)P² + B(x)P + C(x) = 0.

    P starts at x^1: P = p₁x + p₂x² + ...
    """
    n = len(known)
    p = [F(0)] + [F(k) for k in known]  # p[0]=0, p[1]=known[0], etc.

    # P² through x^{2n}
    nterms = 2*n + 2
    p_ext = p + [F(0)] * (nterms - len(p))
    p2 = power_series_mult(p_ext, p_ext, nterms)

    print(f"\n{'='*60}")
    print(f"Quadratic fit for {label}")
    print(f"Known: {known}")
    print(f"P = {' + '.join(f'{p[i]}x^{i}' for i in range(1, len(p)) if p[i]!=0)}")
    print(f"P² = {' + '.join(f'{p2[i]}x^{i}' for i in range(nterms) if p2[i]!=0)}")

    # Try: A(x) = Σ a_i x^i (deg dA), B(x) = Σ b_i x^i (deg dB), C(x) = Σ c_i x^i (deg dC)
    # Equation: A·P² + B·P + C = 0
    # At x=0: C(0) = 0 (since P(0)=0)

    for dA, dB, dC in [(0,1,1), (1,1,1), (0,1,2), (1,1,2), (0,2,1),
                        (1,2,1), (2,1,1), (1,2,2), (2,2,1), (2,1,2),
                        (0,0,1), (1,0,1), (0,2,2), (2,2,2)]:
        # Number of unknowns
        nA = dA + 1
        nB = dB + 1
        nC = dC + 1  # but c_0 = 0, so nC-1 free
        nunknowns = nA + nB + (nC - 1)

        # Number of equations: matching coefficients x^1 through x^{n+1}
        neqs = n + 1  # we have n known coefficients, want to predict n+1

        if nunknowns < neqs - 1:
            continue  # not enough unknowns
        if nunknowns > neqs + 2:
            continue  # too many unknowns, underdetermined

        # Build the system: for each power x^k (k=1,...,n+1),
        # sum over (a_i * p2[k-i]) + (b_i * p[k-i]) + c_k = 0
        # where a_i, b_i, c_j are the coefficients of A, B, C.

        # Variables: a_0,...,a_{dA}, b_0,...,b_{dB}, c_1,...,c_{dC}
        # (c_0=0 is enforced)

        rows = []
        for k in range(1, n + 2):  # x^1 through x^{n+1}
            row = []
            # A coefficients
            for i in range(nA):
                if k - i >= 0 and k - i < nterms:
                    row.append(p2[k-i])
                else:
                    row.append(F(0))
            # B coefficients
            for i in range(nB):
                if k - i >= 0 and k - i < len(p_ext):
                    row.append(p_ext[k-i])
                else:
                    row.append(F(0))
            # C coefficients (c_1,...,c_{dC})
            for j in range(1, nC):
                row.append(F(1) if k == j else F(0))
            rows.append(row)

        # Solve the homogeneous system rows · x = 0
        # with nunknowns variables
        # If we can solve for x^{n+1} coefficient in terms of the rest,
        # that gives us the prediction.

        # Actually, let's use the first n equations to find the null space,
        # then use the (n+1)-th equation to predict the next term.

        # First: check if the first n equations are consistent with a
        # 1-dimensional null space (after removing scaling)
        sol = solve_homogeneous(rows[:n], nunknowns)
        if sol is None:
            continue

        # Check if solution is non-trivial and has non-zero A coefficient
        a_coeffs = sol[:nA]
        if all(c == 0 for c in a_coeffs):
            continue  # degenerate (no quadratic term)

        b_coeffs = sol[nA:nA+nB]
        c_coeffs = [F(0)] + list(sol[nA+nB:])

        # Verify on known terms
        ok = True
        for k in range(1, n + 1):
            val = F(0)
            for i in range(nA):
                if k-i >= 0 and k-i < nterms:
                    val += a_coeffs[i] * p2[k-i]
            for i in range(nB):
                if k-i >= 0 and k-i < len(p_ext):
                    val += b_coeffs[i] * p_ext[k-i]
            if k < len(c_coeffs):
                val += c_coeffs[k]
            if val != 0:
                ok = False
                break

        if not ok:
            continue

        # Now predict x^{n+1}: the equation at order x^{n+1} involves p_{n+1} (unknown)
        # A(x)P² + B(x)P + C(x) at order x^{n+1}:
        # Σ_i a_i p2[n+1-i] + Σ_i b_i p[n+1-i] + c_{n+1} = 0
        # p2[k] = Σ_{i+j=k} p_i * p_j. Since p_0=0, the terms with p_{n+1}
        # in p2[n+1] are p_0*p_{n+1} + p_{n+1}*p_0 = 0. So p2[n+1] depends
        # only on p_1,...,p_n. Therefore p_{n+1} appears ONLY in B(x)*P at
        # order n+1, via the term b_0 * p_{n+1}.

        # So: a_0*p2[n+1] + ... + b_0*p_{n+1} + ... + c_{n+1} = 0
        # Collecting known terms:
        k = n + 1
        known_part = F(0)
        for i in range(nA):
            idx = k - i
            if 0 <= idx < nterms:
                known_part += a_coeffs[i] * p2[idx]
        for i in range(nB):
            idx = k - i
            if idx > 0 and idx <= n and 0 <= idx < len(p_ext):
                known_part += b_coeffs[i] * p_ext[idx]
        if k < len(c_coeffs):
            known_part += c_coeffs[k]

        # The unknown p_{n+1} contributes b_0 * p_{n+1}
        if b_coeffs[0] == 0:
            continue  # can't solve for p_{n+1}

        p_next = -known_part / b_coeffs[0]

        # Compute discriminant
        disc_coeffs = compute_discriminant(a_coeffs, b_coeffs, c_coeffs, nterms)

        print(f"\n  deg(A,B,C) = ({dA},{dB},{dC})")
        print(f"  A(x) = {format_poly(a_coeffs)}")
        print(f"  B(x) = {format_poly(b_coeffs)}")
        print(f"  C(x) = {format_poly(c_coeffs)}")
        print(f"  Predicted p_{n+1} = {p_next} = {float(p_next):.4f}")
        print(f"  Discriminant B²-4AC = {format_poly(disc_coeffs[:8])}")

        # Check: is discriminant consistent with growth rate 8?
        # Radius of convergence = smallest positive root of discriminant
        # For growth 8^n, need root at x=1/8
        disc_at_eighth = sum(c * F(1,8)**i for i, c in enumerate(disc_coeffs[:8]))
        print(f"  Δ(1/8) = {disc_at_eighth} = {float(disc_at_eighth):.6f}")

        # Also check if p_next is a positive integer
        if p_next > 0 and p_next.denominator == 1:
            print(f"  *** INTEGER PREDICTION: H^{n+1} = {p_next} ***")


def solve_homogeneous(rows, nvars):
    """Find a non-trivial solution to the homogeneous system rows·x = 0.
    Returns None if no 1-dim null space found."""
    if not rows:
        return None

    m = len(rows)
    n = nvars

    # Augmented matrix (just the coefficient matrix for homogeneous)
    A = [[F(0)] * n for _ in range(m)]
    for i, row in enumerate(rows):
        for j in range(min(len(row), n)):
            A[i][j] = row[j]

    # Gaussian elimination
    pivot_cols = []
    r = 0
    for col in range(n):
        pivot = None
        for row in range(r, m):
            if A[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        pv = A[r][col]
        for row in range(m):
            if row != r and A[row][col] != 0:
                factor = A[row][col] / pv
                for c2 in range(n):
                    A[row][c2] -= factor * A[r][c2]
        pivot_cols.append(col)
        r += 1

    rank = r
    if rank >= n:
        return None  # only trivial solution
    if rank < n - 1:
        return None  # more than 1-dim null space (underdetermined)

    # rank = n-1: 1-dim null space
    # Find the free variable
    free_cols = [c for c in range(n) if c not in pivot_cols]
    if len(free_cols) != 1:
        return None

    free = free_cols[0]
    sol = [F(0)] * n
    sol[free] = F(1)

    for i in range(rank - 1, -1, -1):
        pc = pivot_cols[i]
        val = F(0)
        for j in range(n):
            if j != pc:
                val += A[i][j] * sol[j]
        sol[pc] = -val / A[i][pc]

    # Clear denominators
    denoms = [s.denominator for s in sol if s != 0]
    if denoms:
        from math import lcm
        from functools import reduce
        common = reduce(lcm, denoms)
        sol = [s * common for s in sol]

    return sol


def compute_discriminant(a_coeffs, b_coeffs, c_coeffs, nterms):
    """Compute B² - 4AC as polynomial coefficients."""
    b2 = power_series_mult(b_coeffs, b_coeffs, nterms)
    ac = power_series_mult(a_coeffs, c_coeffs, nterms)
    disc = [F(0)] * nterms
    for i in range(nterms):
        b2i = b2[i] if i < len(b2) else F(0)
        aci = ac[i] if i < len(ac) else F(0)
        disc[i] = b2i - 4 * aci
    return disc


def format_poly(coeffs):
    """Format polynomial from coefficient list."""
    terms = []
    for i, c in enumerate(coeffs):
        if c == 0:
            continue
        if i == 0:
            terms.append(str(c))
        elif i == 1:
            terms.append(f"{c}x")
        else:
            terms.append(f"{c}x^{i}")
    return " + ".join(terms) if terms else "0"


def extended_search(known, label, max_total_deg=4):
    """More systematic search over polynomial degrees."""
    n = len(known)
    p = [F(0)] + [F(k) for k in known]
    nterms = 2*n + 4
    p_ext = p + [F(0)] * (nterms - len(p))
    p2 = power_series_mult(p_ext, p_ext, nterms)

    print(f"\n{'='*60}")
    print(f"Extended algebraic search for {label}")
    print(f"Known: {known}")

    results = []

    for dA in range(max_total_deg + 1):
        for dB in range(max_total_deg + 1):
            for dC in range(max_total_deg + 1):
                nA = dA + 1
                nB = dB + 1
                nC = dC  # c_0 = 0, so free coeffs are c_1,...,c_{dC}
                nunknowns = nA + nB + nC

                # Need exactly n equations to have 1-dim null space
                # (n unknowns - 1 = n equations for 1-dim kernel)
                # We have n+1 equations available (x^1 through x^{n+1})
                # Use first n to determine, n+1 to predict

                if nunknowns < 2:
                    continue
                if nunknowns - 1 > n:
                    continue  # not enough equations
                if nunknowns - 1 < n:
                    continue  # overdetermined

                # So nunknowns = n + 1

                # Build system: x^1 through x^n
                rows = []
                for k in range(1, n + 1):
                    row = []
                    for i in range(nA):
                        idx = k - i
                        row.append(p2[idx] if 0 <= idx < nterms else F(0))
                    for i in range(nB):
                        idx = k - i
                        row.append(p_ext[idx] if 0 <= idx < nterms else F(0))
                    for j in range(1, dC + 1):
                        row.append(F(1) if k == j else F(0))
                    rows.append(row)

                sol = solve_homogeneous(rows, nunknowns)
                if sol is None:
                    continue

                a_c = sol[:nA]
                b_c = sol[nA:nA+nB]
                c_c = [F(0)] + list(sol[nA+nB:])

                if all(c == 0 for c in a_c):
                    continue

                if b_c[0] == 0:
                    continue

                # Predict p_{n+1}
                k = n + 1
                known_part = F(0)
                for i in range(nA):
                    idx = k - i
                    if 0 <= idx < nterms:
                        known_part += a_c[i] * p2[idx]
                for i in range(nB):
                    idx = k - i
                    if 1 <= idx <= n and 0 <= idx < len(p_ext):
                        known_part += b_c[i] * p_ext[idx]
                if k < len(c_c):
                    known_part += c_c[k]

                p_next = -known_part / b_c[0]

                disc = compute_discriminant(a_c, b_c, c_c, nterms)
                disc_at_eighth = sum(c * F(1,8)**i for i, c in enumerate(disc[:max(len(a_c)+len(b_c), len(c_c))*2+2]))

                is_int = p_next > 0 and p_next.denominator == 1

                results.append({
                    'dA': dA, 'dB': dB, 'dC': dC,
                    'A': a_c, 'B': b_c, 'C': c_c,
                    'p_next': p_next,
                    'disc': disc,
                    'disc_1_8': disc_at_eighth,
                    'is_int': is_int,
                })

    # Print results, prioritizing integer predictions
    results.sort(key=lambda r: (not r['is_int'], r['dA']+r['dB']+r['dC']))

    for r in results:
        tag = "*** INTEGER ***" if r['is_int'] else ""
        print(f"\n  deg(A,B,C)=({r['dA']},{r['dB']},{r['dC']}) {tag}")
        print(f"  A = {format_poly(r['A'])}")
        print(f"  B = {format_poly(r['B'])}")
        print(f"  C = {format_poly(r['C'])}")
        print(f"  p_{n+1} = {r['p_next']} = {float(r['p_next']):.4f}")
        print(f"  Δ(1/8) = {float(r['disc_1_8']):.6f}")

    return results


def functional_equation_search(known, label):
    """Try P = x * F(P) type functional equations.

    P = x * (a + bP + cP² + dP³ + ...)
    Coefficients extracted from known terms.
    """
    n = len(known)
    p = [F(0)] + [F(k) for k in known]
    nterms = 2*n + 4
    p_ext = p + [F(0)] * (nterms - len(p))

    print(f"\n{'='*60}")
    print(f"Functional equation search for {label}")
    print(f"P = x·F(P) where F(t) = a₀ + a₁t + a₂t² + ...")

    # P = x * F(P) means p_1 = a_0 (coefficient of x)
    # p_2 = a_1 * p_1 (coefficient of x²: from x * a_1 * P at x^2 = a_1 * p_1 * x² → p_2 = a_1 * p_1)
    # Actually more carefully:
    # P = x * (a_0 + a_1 P + a_2 P² + a_3 P³ + ...)
    # Coefficient of x^1: p_1 = a_0
    # Coefficient of x^2: p_2 = a_1 * p_1
    # Coefficient of x^3: p_3 = a_1 * p_2 + a_2 * p_1²
    # Coefficient of x^4: p_4 = a_1 * p_3 + 2 * a_2 * p_1 * p_2 + a_3 * p_1³
    # Coefficient of x^5: p_5 = a_1 * p_4 + a_2 * (2*p_1*p_3 + p_2²) + 3*a_3*p_1²*p_2 + a_4*p_1⁴

    p1, p2, p3, p4 = [F(k) for k in known]

    # a_0 = p_1 = 2
    a0 = p1
    # a_1 * p_1 = p_2 → a_1 = p_2/p_1 = 5/2
    a1 = p2 / p1
    # a_1 * p_2 + a_2 * p_1² = p_3 → a_2 = (p_3 - a_1*p_2)/p_1²
    a2 = (p3 - a1 * p2) / (p1**2)
    # a_1 * p_3 + 2*a_2*p_1*p_2 + a_3*p_1³ = p_4
    a3 = (p4 - a1*p3 - 2*a2*p1*p2) / (p1**3)

    print(f"  a₀ = {a0}")
    print(f"  a₁ = {a1} = {float(a1):.6f}")
    print(f"  a₂ = {a2} = {float(a2):.6f}")
    print(f"  a₃ = {a3} = {float(a3):.6f}")

    # Predict p_5 = a_1*p_4 + a_2*(2*p_1*p_3 + p_2²) + 3*a_3*p_1²*p_2 + a_4*p_1⁴
    # But we don't know a_4. We need more structure.

    # Try: F is a polynomial of degree d
    for d in range(1, 4):
        print(f"\n  --- F polynomial of degree {d} ---")
        if d == 1:
            # P = x(a_0 + a_1 P) → P(1 - a_1 x) = a_0 x → P = a_0 x / (1 - a_1 x)
            # This gives p_n = a_0 * a_1^{n-1}
            # Check: p_1=2=a_0, p_2=5=2*a_1 → a_1=5/2, p_3=2*(5/2)²=25/2≠16. FAIL
            print(f"  P = {a0}x / (1 - {a1}x) → p_3 = {a0 * a1**2} (need 16): FAIL")

        elif d == 2:
            # P = x(a_0 + a_1 P + a_2 P²)
            # This is a quadratic: a_2 x P² + (a_1 x - 1)P + a_0 x = 0
            # P = (1 - a_1 x ± √((1-a_1 x)² - 4a_0 a_2 x²)) / (2a_2 x)
            print(f"  a₀={a0}, a₁={a1}, a₂={a2}")
            print(f"  Quadratic: {a2}x P² + ({a1}x - 1)P + {a0}x = 0")

            # Discriminant: (1-a_1 x)² - 4 a_0 a_2 x²
            # = 1 - 2a_1 x + a_1² x² - 4a_0 a_2 x²
            # = 1 - 2a_1 x + (a_1² - 4a_0 a_2) x²
            d0 = F(1)
            d1 = -2*a1
            d2_coeff = a1**2 - 4*a0*a2
            print(f"  Δ(x) = {d0} + {d1}x + {d2_coeff}x²")
            print(f"  Δ(x) = 1 - {2*a1}x + {d2_coeff}x²")

            # Roots of Δ: x = (2a₁ ± √(4a₁²-4d2))/2d2 = (a₁ ± √(a₁²-d2))/d2
            # d2 = a₁² - 4a₀a₂
            inner = 4*a1**2 - 4*d2_coeff
            print(f"  4a₁² - 4(a₁²-4a₀a₂) = {inner} = 16a₀a₂ = {16*a0*a2}")

            # Check: does F(t) = a₀+a₁t+a₂t² predict p₄?
            p4_pred = a1*p3 + 2*a2*p1*p2
            # Wait, this doesn't include higher terms from P². Let me redo.
            # From P = x(a₀+a₁P+a₂P²):
            # p₄ = a₁p₃ + a₂(2p₁p₂) ... no, we need P² at x³:
            # P² = Σ (Σ_{i+j=k} p_i p_j) x^k
            # P²[x³] = 2p₁p₂ = 2·2·5 = 20
            # So x·a₂·P² at x⁴ = a₂·P²[x³] = a₂·20
            # x·a₁·P at x⁴ = a₁·p₃ = (5/2)·16 = 40
            # x·a₀ at x⁴ = 0 (only contributes at x¹)
            # So p₄ = a₁·p₃ + a₂·(2p₁p₂) = 40 + a₂·20
            # We know p₄=52, so: 52 = 40 + 20a₂ → a₂ = 12/20 = 3/5
            a2_from_p4 = (p4 - a1*p3) / (2*p1*p2)
            print(f"  a₂ from p₃: {a2}")
            print(f"  a₂ from p₄: {a2_from_p4}")
            print(f"  Consistent: {a2 == a2_from_p4}")

            if a2 != a2_from_p4:
                print(f"  INCONSISTENT: degree-2 F doesn't fit all 4 terms")
                # The extra constraint from p₄ is not satisfied
                # This means F is NOT degree 2
            else:
                # Predict p₅
                # P²[x⁴] = 2p₁p₃ + p₂² = 2·2·16 + 25 = 89
                p5 = a1*p4 + a2*(2*p1*p3 + p2**2)
                print(f"  Predicted p₅ = {p5} = {float(p5):.4f}")

        elif d == 3:
            # P = x(a₀ + a₁P + a₂P² + a₃P³)
            # 4 unknowns, 4 equations → unique
            print(f"  a₀={a0}, a₁={a1}, a₂={a2}, a₃={a3}")

            # Check internal consistency
            # p₁ = a₀ = 2 ✓
            # p₂ = a₁p₁ = 5/2·2 = 5 ✓
            # From P = x·F(P): [x^k] P = [x^{k-1}] F(P).
            # F(P) = a₀ + a₁P + a₂P² + a₃P³
            # [x^{k-1}] F(P) = a₁·p_{k-1} + a₂·[x^{k-1}]P² + a₃·[x^{k-1}]P³
            # (a₀ only contributes to [x⁰])

            # P³ coefficients
            p2_series = power_series_mult(p_ext, p_ext, nterms)
            p3_series = power_series_mult(p2_series, p_ext, nterms)

            # Verify p₄ = a₁p₃ + a₂·p2[3] + a₃·p3[3]
            # p2[3] = 2p₁p₂ = 20
            # p3[3] = p₁³ = 8 (only way to get x³ from P³ with P starting at x)
            # P³[x³] = (p₁x + ...)³ at x³ = p₁³ = 8
            p4_check = a1*p3 + a2*p2_series[3] + a3*p3_series[3]
            print(f"  p₄ check: {p4_check} (should be {p4}): {'✓' if p4_check == p4 else '✗'}")

            # Predict p₅
            # p₅ = a₁p₄ + a₂·p2[4] + a₃·p3[4]
            # p2[4] = 2p₁p₃ + p₂² = 64 + 25 = 89
            # p3[4] = 3·p₁²·p₂ = 3·4·5 = 60
            p5 = a1*p4 + a2*p2_series[4] + a3*p3_series[4]
            print(f"  P²[x⁴] = {p2_series[4]}")
            print(f"  P³[x⁴] = {p3_series[4]}")
            print(f"  Predicted p₅ = {p5} = {float(p5):.4f}")

            if p5.denominator == 1 and p5 > 0:
                print(f"  *** INTEGER PREDICTION: H^5 = {p5} ***")

            # Predict more
            # p₆ = a₁p₅ + a₂·p2[5] + a₃·p3[5]
            p_ext2 = list(p_ext)
            p_ext2[5] = p5
            p2_s2 = power_series_mult(p_ext2, p_ext2, nterms)
            p3_s2 = power_series_mult(p2_s2, p_ext2, nterms)
            p6 = a1*p5 + a2*p2_s2[5] + a3*p3_s2[5]
            print(f"  Predicted p₆ = {p6} = {float(p6):.4f}")

            if p6.denominator == 1 and p6 > 0:
                print(f"  *** INTEGER PREDICTION: H^6 = {p6} ***")

            # Continue
            p_ext3 = list(p_ext2)
            p_ext3[6] = p6
            p2_s3 = power_series_mult(p_ext3, p_ext3, nterms)
            p3_s3 = power_series_mult(p2_s3, p_ext3, nterms)
            p7 = a1*p6 + a2*p2_s3[6] + a3*p3_s3[6]
            print(f"  Predicted p₇ = {p7} = {float(p7):.4f}")

            p_ext4 = list(p_ext3)
            p_ext4[7] = p7
            p2_s4 = power_series_mult(p_ext4, p_ext4, nterms)
            p3_s4 = power_series_mult(p2_s4, p_ext4, nterms)
            p8 = a1*p7 + a2*p2_s4[7] + a3*p3_s4[7]
            print(f"  Predicted p₈ = {p8} = {float(p8):.4f}")

            print(f"\n  Sequence: {known + [int(p5) if p5.denominator==1 else float(p5), int(p6) if p6.denominator==1 else float(p6), int(p7) if p7.denominator==1 else float(p7), int(p8) if p8.denominator==1 else float(p8)]}")

            # Analyze the cubic F(t) = a₀ + a₁t + a₂t² + a₃t³
            # The algebraic equation is: t = x·F(t), i.e., t - x(a₀+a₁t+a₂t²+a₃t³) = 0
            # This is degree 3 in t (for each x), making P algebraic of degree 3.
            # Growth rate determined by the smallest positive singularity.
            # Singularity at x where the cubic has a double root:
            # t - x·F(t) = 0 and 1 - x·F'(t) = 0
            # From second: x = 1/F'(t)
            # Sub into first: t = F(t)/F'(t)
            # i.e., t·F'(t) = F(t) → a₀ = 0 ... no that's wrong.
            # t·F'(t) - F(t) = t(a₁+2a₂t+3a₃t²) - (a₀+a₁t+a₂t²+a₃t³) = 0
            # = -a₀ + a₂t² + 2a₃t³ = 0
            # So: 2a₃t³ + a₂t² - a₀ = 0

            print(f"\n  Singularity equation: {2*a3}t³ + {a2}t² - {a0} = 0")
            # For each root t₀, x₀ = 1/F'(t₀) = 1/(a₁+2a₂t₀+3a₃t₀²)
            # Growth rate = 1/x₀


def verify_sl2():
    """Verify the method on sl₂ (Riordan numbers)."""
    sl2 = [3, 6, 15, 36, 91]  # R(4),...,R(8)
    print("\n" + "="*60)
    print("VERIFICATION: sl₂ (should recover Riordan GF)")

    p = [F(0)] + [F(k) for k in sl2]

    # Known: P = x(a₀+a₁P+a₂P²) with a₀=3, a₁=2, a₂=0 (since Riordan satisfies P=x(3+2P)/(1+P)?)
    # Actually: x(1+x)P² - (1+x)P + 1 = 0 (as derived above for R(x))
    # For the SHIFTED series P(x) = Σ R(n+3) x^n = 3x + 6x² + 15x³ + ...:
    # we need to derive the equation for this shifted series.

    # Let's use the functional equation approach
    p1, p2, p3, p4, p5 = [F(k) for k in sl2]
    a0 = p1  # = 3
    a1 = p2/p1  # = 2
    a2_from_p3 = (p3 - a1*p2)/(p1**2)  # = (15-12)/9 = 1/3
    a2_from_p4_check = (p4 - a1*p3)/(2*p1*p2)  # = (36-30)/36 = 1/6
    print(f"  a₀={a0}, a₁={a1}")
    print(f"  a₂ from p₃: {a2_from_p3}")
    print(f"  a₂ from p₄: {a2_from_p4_check}")
    print(f"  Consistent: {a2_from_p3 == a2_from_p4_check}")
    # Not consistent! So sl₂ also needs degree 3 in F.

    a2 = a2_from_p3  # = 1/3
    a3 = (p4 - a1*p3 - a2*(2*p1*p2)) / (p1**3)
    print(f"  a₃ from p₄: {a3}")

    # Predict p₅
    nterms = 14
    p_ext = p + [F(0)] * (nterms - len(p))
    p2s = power_series_mult(p_ext, p_ext, nterms)
    p3s = power_series_mult(p2s, p_ext, nterms)
    p5_pred = a1*p4 + a2*p2s[4] + a3*p3s[4]
    print(f"  P²[x⁴] = {p2s[4]}, P³[x⁴] = {p3s[4]}")
    print(f"  Predicted p₅ = {p5_pred} (actual: {p5})")
    print(f"  Match: {p5_pred == p5}")


if __name__ == "__main__":
    # First verify on sl₂
    verify_sl2()

    # Then try W₃
    functional_equation_search(W3_KNOWN, "W₃")

    # Also try sl₃
    functional_equation_search(SL3_KNOWN, "sl₃")

    # Try the quadratic algebraic fit approach
    extended_search(W3_KNOWN, "W₃", max_total_deg=3)
