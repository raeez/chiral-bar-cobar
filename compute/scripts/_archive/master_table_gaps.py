#!/usr/bin/env python3
"""Attack remaining Master Table gaps via recurrence analysis.

Gaps: sl₃ deg 4-5, W₃ deg 5, Y(sl₂) deg 4-5.

For each algebra with enough data points, try:
1. Constant-coefficient recurrences of various orders
2. Polynomial-coefficient (D-finite) recurrences
3. Growth rate analysis
"""

from sympy import Rational, symbols, sqrt, solve, simplify, factor, Matrix
from math import factorial

# Known bar cohomology data
data = {
    'Heisenberg': [1, 1, 1, 2, 3, 5, 7, 11],  # p(n-2) for n>=2, 1 at n=1
    'free_fermion': [1, 1, 2, 3, 5, 7, 11],    # p(n-1)
    'bc_ghosts': [2, 4, 10, 24, 58, 140],       # 2^n - n + 1
    'sl2': [1, 3, 6, 15, 36, 91, 232, 603],     # Riordan R(n+3)
    'Virasoro': [1, 2, 5, 13, 35, 96, 267],     # Motzkin diffs M(n+1)-M(n)
    'sl3': [8, 36, 204],                         # ONLY 3 KNOWN
    'W3': [2, 5, 16, 52],                        # 4 KNOWN
    'Y_sl2': [4, 10, 28],                        # 3 KNOWN
}

def find_const_recurrence(name, vals, max_order=None):
    """Try to find constant-coefficient recurrence."""
    if max_order is None:
        max_order = len(vals) // 2

    print(f"\n{'='*50}")
    print(f"{name}: {vals}")
    print(f"{'='*50}")

    for k in range(2, max_order + 1):
        # c₁*a(n-1) + ... + c_k*a(n-k) = a(n)
        # Need at least k+1 data points (k for equations + 1 for verification)
        if len(vals) < k + 1:
            continue

        rows = []
        rhs = []
        for n in range(k, len(vals)):
            row = [vals[n-j] for j in range(1, k+1)]
            rows.append(row)
            rhs.append(vals[n])

        M = Matrix(rows)
        r = Matrix(rhs)

        if M.rows < M.cols:
            continue

        # Use least squares if overdetermined
        try:
            if M.rows == M.cols:
                sol = M.solve(r)
            else:
                # Check if system is consistent
                augmented = M.row_join(r)
                rref, pivots = augmented.rref()
                # Check if last column is a pivot
                if M.cols in pivots:
                    print(f"  Order {k}: inconsistent")
                    continue
                sol = M[:M.cols, :].solve(r[:M.cols, :])
                # Verify remaining rows
                residual = M * sol - r
                if any(residual[i] != 0 for i in range(M.rows)):
                    print(f"  Order {k}: inconsistent (residual check)")
                    continue
        except Exception:
            print(f"  Order {k}: solve failed")
            continue

        # Verify
        ok = True
        for n in range(k, len(vals)):
            pred = sum(sol[j] * vals[n-j-1] for j in range(k))
            if pred != vals[n]:
                ok = False
                break

        if ok:
            coeffs = [sol[j] for j in range(k)]
            print(f"  Order {k}: EXACT recurrence found!")
            print(f"    a(n) = {' + '.join(f'{c}*a(n-{j+1})' for j, c in enumerate(coeffs))}")

            # Predict next values
            extended = list(vals)
            for _ in range(5):
                next_val = sum(coeffs[j] * extended[-(j+1)] for j in range(k))
                extended.append(next_val)
            print(f"    Predictions: {extended[len(vals):]}")

            # Characteristic polynomial
            t = symbols('t')
            char_poly = t**k - sum(coeffs[j] * t**(k-1-j) for j in range(k))
            print(f"    Char poly: {char_poly}")
            roots = solve(char_poly, t)
            print(f"    Roots: {roots}")
            for root in roots:
                try:
                    print(f"      {root} ≈ {float(root):.6f}")
                except (TypeError, ValueError):
                    print(f"      {root} (complex)")
            print(f"    Factored: {factor(char_poly)}")

            # Growth rate
            max_root = max(abs(float(root)) for root in roots if root.is_real)
            print(f"    Growth rate: {max_root:.6f}")

            return coeffs, extended
        else:
            print(f"  Order {k}: no constant recurrence")

    return None, None

def find_dfinite_recurrence(name, vals, order=1, deg=1):
    """Try D-finite recurrence: sum_{j=0}^{order} p_j(n) * a(n-j) = 0
    where p_j are polynomials of degree <= deg."""
    print(f"\n  D-finite (order {order}, poly degree {deg}):")

    # p_j(n) = sum_{i=0}^{deg} c_{j,i} * n^i
    # Total unknowns: (order+1) * (deg+1)
    n_unknowns = (order + 1) * (deg + 1)

    if len(vals) < n_unknowns + 1:
        print(f"    Not enough data ({len(vals)} < {n_unknowns+1})")
        return None

    # Build system: for each valid n, sum_{j=0}^{order} p_j(n) * a(n-j) = 0
    c = symbols(f'c0:{(order+1)*(deg+1)}')

    rows = []
    for n in range(order, len(vals)):
        row = []
        for j in range(order + 1):
            for i in range(deg + 1):
                # coefficient of c_{j*(deg+1)+i}: n^i * a(n-j)
                val = n**i * vals[n - j]
                row.append(val)
        rows.append(row)

    M = Matrix(rows)
    # We want M * c = 0 (nontrivial). Find null space.
    null = M.nullspace()
    if null:
        print(f"    Null space dimension: {len(null)}")
        for ns in null:
            # Display the recurrence
            terms = []
            for j in range(order + 1):
                poly_terms = []
                for i in range(deg + 1):
                    coeff = ns[j * (deg + 1) + i]
                    if coeff != 0:
                        if i == 0:
                            poly_terms.append(f"{coeff}")
                        else:
                            poly_terms.append(f"{coeff}*n^{i}")
                if poly_terms:
                    p = " + ".join(poly_terms)
                    terms.append(f"({p})*a(n-{j})")
            print(f"    Recurrence: {' + '.join(terms)} = 0")

            # Predict
            extended = list(vals)
            for step in range(5):
                n = len(extended)
                # sum_{j=0}^{order} p_j(n)*a(n-j) = 0
                # => p_0(n)*a(n) = -sum_{j=1}^{order} p_j(n)*a(n-j)
                p0 = sum(ns[i] * n**i for i in range(deg + 1))
                if p0 == 0:
                    print(f"    Cannot predict (p₀(n)=0 at n={n})")
                    break
                rhs = 0
                for j in range(1, order + 1):
                    pj = sum(ns[j*(deg+1) + i] * n**i for i in range(deg + 1))
                    rhs -= pj * extended[n - j]
                next_val = Rational(rhs, p0)
                if next_val.denominator != 1:
                    print(f"    Non-integer at n={n}: {next_val}")
                    break
                extended.append(int(next_val))
            if len(extended) > len(vals):
                print(f"    Predictions: {extended[len(vals):]}")
            return ns
    else:
        print(f"    No D-finite recurrence found")
    return None

# Main analysis
results = {}

for name, vals in data.items():
    coeffs, extended = find_const_recurrence(name, vals)
    if coeffs is not None:
        results[name] = extended

# For algebras without constant recurrences, try D-finite
print("\n" + "=" * 60)
print("D-FINITE RECURRENCE SEARCH")
print("=" * 60)

for name in ['sl2', 'Virasoro', 'W3']:
    vals = data[name]
    for order in range(1, 3):
        for deg in range(1, 3):
            find_dfinite_recurrence(name, vals, order, deg)

# Special analysis for W₃
print("\n" + "=" * 60)
print("W₃ DEEP ANALYSIS")
print("=" * 60)

w3 = [2, 5, 16, 52]
print(f"W₃: {w3}")
print(f"Ratios: {[w3[i+1]/w3[i] for i in range(len(w3)-1)]}")
print(f"Differences: {[w3[i+1]-w3[i] for i in range(len(w3)-1)]}")
print(f"Second differences: {[w3[i+2]-2*w3[i+1]+w3[i] for i in range(len(w3)-2)]}")

# W₃ has central charge c = 2 - 24(k+2)²/(k+3) via DS reduction of sl₃
# The W₃ algebra has 2 generators: T (weight 2) and W (weight 3)
# dim W₃ at weight n: partition function of 2 generators of weights 2 and 3
# p_{2,3}(n) = number of partitions of n into parts 2 and 3

# H₁ = 2 (generators T, W)
# H₂ = 5
# H₃ = 16
# H₄ = 52

# Growth rate: 52/16 ≈ 3.25, 16/5 = 3.2, 5/2 = 2.5
# Approaching something around 3-4?

# The W₃ algebra is a quotient of the universal enveloping of the Zamolodchikov algebra.
# Its bar cohomology should be related to the minimal resolution of W₃.

# Try: does W₃ satisfy a(n) ~ C * 3^n for some correction?
# 2, 5, 16, 52: 2*3=6≠5, 5*3=15≠16, 16*3=48≠52
# Close to 3^n but with corrections.

# Try: a(n) = A*α^n + B*β^n fit
# 4 data points, 4 unknowns (A, α, B, β) — nonlinear.
# Try rational GF: a(n) = c₁a(n-1) + c₂a(n-2) (order 2)
# c₁*2+c₂*? = 5 — need 3 points for order 2.
# c₁*2 + c₂*1 = 5 (using H₀=1)
# Wait, we don't have H₀. Let me use H₁=2, H₂=5, H₃=16, H₄=52.

# Order 2: c₁*H(n-1) + c₂*H(n-2) = H(n)
# n=3: c₁*5 + c₂*2 = 16
# n=4: c₁*16 + c₂*5 = 52
M_w3 = Matrix([[5, 2], [16, 5]])
r_w3 = Matrix([16, 52])
try:
    sol_w3 = M_w3.solve(r_w3)
    print(f"\nOrder-2 recurrence: c₁={sol_w3[0]}, c₂={sol_w3[1]}")
    # Predict H₅
    H5_pred = sol_w3[0]*52 + sol_w3[1]*16
    print(f"H₅ prediction: {H5_pred}")

    # Characteristic polynomial
    t = symbols('t')
    cp = t**2 - sol_w3[0]*t - sol_w3[1]
    print(f"Char poly: {cp} = {factor(cp)}")
    roots = solve(cp, t)
    print(f"Roots: {roots}")
    for r in roots:
        try:
            print(f"  {r} ≈ {float(r):.6f}")
        except:
            pass
except Exception as e:
    print(f"Order-2 failed: {e}")

# Also try with H₀ = 1 prepended
print("\nWith H₀=1 prepended:")
w3_ext = [1] + w3
for k in range(2, 4):
    if len(w3_ext) < k + 2:
        continue
    rows = []
    rhs = []
    for n in range(k, len(w3_ext)):
        row = [w3_ext[n-j] for j in range(1, k+1)]
        rows.append(row)
        rhs.append(w3_ext[n])
    M = Matrix(rows)
    r = Matrix(rhs)
    try:
        if M.rows > M.cols:
            # Overdetermined, check consistency
            sol = M[:M.cols,:].solve(r[:M.cols,:])
            check = M * sol - r
            if all(check[i] == 0 for i in range(M.rows)):
                print(f"  Order {k}: {sol.T} (consistent)")
            else:
                print(f"  Order {k}: inconsistent")
        else:
            sol = M.solve(r)
            print(f"  Order {k}: {sol.T}")
    except Exception as e:
        print(f"  Order {k}: {e}")

# Y(sl₂) analysis
print("\n" + "=" * 60)
print("Y(sl₂) ANALYSIS")
print("=" * 60)

y_sl2 = [4, 10, 28]
print(f"Y(sl₂): {y_sl2}")
print(f"Ratios: {[y_sl2[i+1]/y_sl2[i] for i in range(len(y_sl2)-1)]}")

# Conjectured: 3^n + 1
print(f"3^n+1: {[3**n+1 for n in range(1,6)]}")
# 4, 10, 28, 82, 244

# Order-2 with H₀=1:
y_ext = [1] + y_sl2
M_y = Matrix([[y_ext[1], y_ext[0]], [y_ext[2], y_ext[1]]])
r_y = Matrix([y_ext[2], y_ext[3]])
try:
    sol_y = M_y.solve(r_y)
    print(f"Order-2: c₁={sol_y[0]}, c₂={sol_y[1]}")
    # Predict
    ext = list(y_ext)
    for _ in range(3):
        ext.append(sol_y[0]*ext[-1] + sol_y[1]*ext[-2])
    print(f"Extended: {ext}")

    t = symbols('t')
    cp = t**2 - sol_y[0]*t - sol_y[1]
    print(f"Char poly: {factor(cp)}")
    roots = solve(cp, t)
    for r in roots:
        print(f"  Root: {r} ≈ {float(r):.4f}")
except Exception as e:
    print(f"Order-2: {e}")

# Summary
print("\n" + "=" * 60)
print("MASTER TABLE GAP PREDICTIONS")
print("=" * 60)

print("""
| Algebra | Known | H₄ | H₅ | Method | Confidence |
|---------|-------|-----|-----|--------|------------|
| sl₃     | [8,36,204] | 1352† | 9892† | Rational GF (1-8x)(1-3x-x²) | LOW |
| W₃      | [2,5,16,52] | TBD | TBD | Order-2 recurrence | MEDIUM |
| Y(sl₂)  | [4,10,28] | 82 | 244 | 3^n+1 conjecture | LOW |

† = from conjectured recurrence a(n)=11a(n-1)-23a(n-2)-8a(n-3)
""")
