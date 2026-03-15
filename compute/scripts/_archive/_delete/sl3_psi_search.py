#!/usr/bin/env python3
"""Systematic search for sl_3 bar cohomology equation.

For sl_2: P = 1 + 0*x + 1*x^2 + x^3*G where G = bar cohomology GF.
P satisfies x*psi*P^2 - psi*P + 1 = 0 with psi = 1+x (polynomial deg 1).
Growth rate = 3 = dim(sl_2), from disc root at x=1/3.

For sl_3: P = 1 + c_1*x + ... + c_{s-1}*x^{s-1} + x^s * G
where G = 1 + 8x + 36x^2 + 204x^3 + H_4*x^4 + ...
and s = shift (unknown).

Strategy: for each shift s and pre-bar coefficients c_1,...,c_{s-1}:
1. Compute psi = 1/(P - x*P^2)
2. Check if psi terminates (polynomial)
3. If so, impose growth rate = 8 to determine H_4
"""

from sympy import Rational, symbols, sqrt, series, solve, simplify, N

# Bar cohomology data
H = [1, 8, 36, 204]  # H_0, H_1, H_2, H_3

def compute_P_coeffs(s, pre_bar_coeffs, H_data, max_terms=20):
    """Construct P coefficients: P_0=1, P_1=c_1,..., P_{s-1}=c_{s-1},
    then P_{s+n} = H_n."""
    P = [Rational(0)] * max_terms
    P[0] = Rational(1)
    for i, c in enumerate(pre_bar_coeffs):
        P[i+1] = Rational(c)
    for n, h in enumerate(H_data):
        if s + n < max_terms:
            P[s + n] = Rational(h)
    return P

def compute_P_squared(P, max_terms):
    """Compute P^2 coefficients."""
    P2 = [Rational(0)] * max_terms
    for i in range(max_terms):
        for j in range(max_terms):
            if i + j < max_terms:
                P2[i+j] += P[i] * P[j]
    return P2

def compute_psi(P, max_terms):
    """Compute psi = 1/(P - x*P^2) as power series."""
    P2 = compute_P_squared(P, max_terms)

    # Q = P - x*P^2
    Q = [Rational(0)] * max_terms
    for n in range(max_terms):
        Q[n] = P[n] - (P2[n-1] if n >= 1 else 0)

    # psi = 1/Q
    if Q[0] == 0:
        return None

    psi = [Rational(0)] * max_terms
    psi[0] = Rational(1) / Q[0]
    for n in range(1, max_terms):
        s = sum(psi[k] * Q[n-k] for k in range(n) if n-k < max_terms)
        psi[n] = -s / Q[0]

    return psi

def check_polynomial_psi(psi, max_terms, tol_degree=None):
    """Check if psi appears to be a polynomial (coefficients become 0)."""
    # Find the last nonzero coefficient
    last_nonzero = -1
    for n in range(max_terms):
        if psi[n] != 0:
            last_nonzero = n

    if tol_degree is not None:
        # Check if all coefficients after tol_degree are 0
        for n in range(tol_degree + 1, max_terms):
            if psi[n] != 0:
                return False, last_nonzero
        return True, tol_degree

    return last_nonzero, last_nonzero

# ================================================================
# VALIDATION: sl_2
# ================================================================
print("=" * 60)
print("sl_2 VALIDATION")
print("=" * 60)

H_sl2 = [1, 1, 3, 6, 15, 36, 91, 232, 603, 1585]
# Wait: for sl_2, H_n = R(n+3). H_0 = R(3) = 1, H_1 = R(4) = 3.
# But in MEMORY.md: "sl₂ | Riordan R(n+3)"
# So H_1 = 3 (=dim sl_2). But R(4) = 3. ✓

# The shift s=3, pre-bar = [0, 1] (P_1=0, P_2=1)
P_sl2 = compute_P_coeffs(3, [0, 1], H_sl2, max_terms=15)
print(f"P coefficients: {[int(p) for p in P_sl2[:12]]}")

psi_sl2 = compute_psi(P_sl2, 15)
print(f"psi coefficients: {[float(p) for p in psi_sl2[:8]]}")
print(f"Expected: 1, 1, 0, 0, 0, ...")

# Check: psi = 1+x?
is_poly = all(psi_sl2[n] == 0 for n in range(2, 12))
print(f"psi = 1+x (polynomial degree 1): {is_poly}")

# ================================================================
# sl_3: SYSTEMATIC SEARCH
# ================================================================
print("\n" + "=" * 60)
print("sl_3: SYSTEMATIC SEARCH")
print("=" * 60)

H_sl3 = [1, 8, 36, 204]

# Try different shifts s and pre-bar coefficients
# For s=3: P = 1 + c1*x + c2*x^2 + x^3*(1+8x+36x^2+204x^3+...)

print("\n--- Shift s=3, c1=0 ---")
# Try c2 as parameter
from sympy import Symbol
c2 = Symbol('c2')

# Manual computation with symbolic c2
# P = 1, 0, c2, 1, 8, 36, 204, ...
P_sym = [Rational(1), Rational(0), c2, Rational(1), Rational(8),
         Rational(36), Rational(204)]
max_t = len(P_sym)

# P^2
P2_sym = [Rational(0)] * max_t
for i in range(max_t):
    for j in range(max_t):
        if i+j < max_t:
            P2_sym[i+j] += P_sym[i] * P_sym[j]

# Q = P - xP^2
Q_sym = [Rational(0)] * max_t
for n in range(max_t):
    Q_sym[n] = P_sym[n] - (P2_sym[n-1] if n >= 1 else 0)

print("Q = P - x*P^2:")
for n in range(max_t):
    print(f"  Q_{n} = {simplify(Q_sym[n])}")

# psi from Q
psi_sym = [Rational(0)] * max_t
psi_sym[0] = Rational(1)
for n in range(1, max_t):
    s = sum(psi_sym[k] * Q_sym[n-k] for k in range(n) if n-k < max_t)
    psi_sym[n] = simplify(-s)

print("\npsi coefficients:")
for n in range(max_t):
    print(f"  psi_{n} = {simplify(psi_sym[n])}")

# For psi to be degree d, need psi_{d+1} = psi_{d+2} = ... = 0
# Check: psi_3 always 0?
print(f"\npsi_3 = {simplify(psi_sym[3])}")
print(f"psi_4 = {simplify(psi_sym[4])}")
print(f"psi_5 = {simplify(psi_sym[5])}")

# Solve for c2 such that psi terminates
# If psi has degree 2: need psi_3 = psi_4 = 0
if simplify(psi_sym[3]) == 0:
    print("\npsi_3 = 0 always! Checking if psi can be degree 2...")
    c2_solutions = solve(psi_sym[4], c2)
    print(f"  psi_4 = 0 requires c2 = {c2_solutions}")
    for c2_val in c2_solutions:
        print(f"  c2 = {c2_val} ≈ {float(c2_val):.6f}")
        psi_at = [simplify(p.subs(c2, c2_val)) for p in psi_sym]
        print(f"    psi = {[float(p) for p in psi_at[:6]]}")

# Now try: for psi degree 2, what growth rate results?
# disc = psi(psi - 4x), roots of psi - 4x = 0
# psi = 1 + x + (1-c2)*x^2
# psi - 4x = 1 + (1-4)*x + (1-c2)*x^2 = (1-c2)*x^2 - 3x + 1
print("\n--- Degree-2 psi analysis ---")
print("psi = 1 + x + (1-c2)*x^2")
print("psi - 4x = (1-c2)*x^2 - 3x + 1")
print()
print("For growth rate 8: psi(1/8) - 4/8 = 0")
print("  psi(1/8) = 1 + 1/8 + (1-c2)/64 = 1/2")
print("  1.125 + (1-c2)/64 = 0.5")
print("  (1-c2)/64 = -0.625")
print("  1-c2 = -40")
print("  c2 = 41")

c2_growth = 41
print(f"\nc2 = {c2_growth}")
psi_val = [1, 1, 1 - c2_growth]
print(f"psi = 1 + x - {c2_growth-1}x^2 = {psi_val}")

# Check psi_4 with c2=41
psi4_at_41 = simplify(psi_sym[4].subs(c2, c2_growth))
print(f"psi_4 at c2={c2_growth}: {psi4_at_41}")
if psi4_at_41 != 0:
    print("  psi is NOT degree 2 at c2=41!")
    print("  Need c2 satisfying BOTH growth rate AND polynomial psi.")

    # The polynomial condition: c2^2 + c2 - 7 = 0 (from psi_4 = 0)
    # The growth condition: c2 = 41
    # These are INCOMPATIBLE.
    print("\n  Polynomial psi (deg 2) requires c2 = (-1±√29)/2 ≈ 2.19 or -3.19")
    print("  Growth rate 8 requires c2 = 41")
    print("  INCOMPATIBLE for s=3, c1=0, degree-2 psi.")

# Let's try higher degree psi
print("\n--- What if psi has degree 3? ---")
# psi_3 = 0 always, so psi is degree <= 2 unless we change approach.
# Maybe s=3, c1≠0?

print("\n--- Shift s=3, c1 as parameter ---")
c1 = Symbol('c1')

P_sym2 = [Rational(1), c1, c2, Rational(1), Rational(8),
          Rational(36), Rational(204)]
max_t2 = len(P_sym2)

P2_sym2 = [Rational(0)] * max_t2
for i in range(max_t2):
    for j in range(max_t2):
        if i+j < max_t2:
            P2_sym2[i+j] += P_sym2[i] * P_sym2[j]

Q_sym2 = [Rational(0)] * max_t2
for n in range(max_t2):
    Q_sym2[n] = P_sym2[n] - (P2_sym2[n-1] if n >= 1 else 0)

psi_sym2 = [Rational(0)] * max_t2
psi_sym2[0] = Rational(1)
for n in range(1, max_t2):
    s = sum(psi_sym2[k] * Q_sym2[n-k] for k in range(n) if n-k < max_t2)
    psi_sym2[n] = simplify(-s)

print("\npsi coefficients (with c1, c2):")
for n in range(min(5, max_t2)):
    print(f"  psi_{n} = {simplify(psi_sym2[n])}")

# For psi degree 1 (like sl_2): psi_2 = psi_3 = 0
print("\nFor psi degree 1: psi_2 = 0 and psi_3 = 0")
sol_deg1 = solve([psi_sym2[2], psi_sym2[3]], [c1, c2])
print(f"  Solutions: {sol_deg1}")

if sol_deg1:
    for sol in sol_deg1 if isinstance(sol_deg1, list) else [sol_deg1]:
        if isinstance(sol, dict):
            c1v, c2v = sol[c1], sol[c2]
        else:
            c1v, c2v = sol
        print(f"\n  c1 = {c1v}, c2 = {c2v}")
        psi_vals = [simplify(p.subs(c1, c1v).subs(c2, c2v)) for p in psi_sym2]
        print(f"  psi = {[float(p) if p.is_number else p for p in psi_vals[:6]]}")

        # Check growth rate
        psi_poly_val = psi_vals[0] + psi_vals[1] / 8
        print(f"  psi(1/8) = {float(psi_poly_val):.6f}")
        print(f"  psi(1/8) - 1/2 = {float(psi_poly_val - Rational(1,2)):.6f}")

        # Growth rate from disc = psi(psi-4x)
        # psi - 4x = psi_0 + (psi_1-4)x = 1 + (psi_1-4)x
        # Root: x = 1/(4-psi_1)
        psi_1_val = psi_vals[1]
        if psi_1_val != 4:
            root = 1 / (4 - psi_1_val)
            print(f"  psi-4x root: x = 1/(4-{psi_1_val}) = {float(root):.6f}")
            print(f"  Growth rate = {float(1/root):.6f}")
            print(f"  dim(sl_3) = 8. Match: {abs(float(1/root) - 8) < 0.001}")

# For psi degree 2: psi_3 = 0
print("\nFor psi degree 2: psi_3 = 0")
sol_deg2_eq = psi_sym2[3]
print(f"  psi_3 = {simplify(sol_deg2_eq)}")

# This gives one equation in two unknowns (c1, c2).
# Add growth rate constraint: psi(1/8) = 1/2
# psi(1/8) = 1 + psi_1/8 + psi_2/64 = 1/2
psi_at_8th = psi_sym2[0] + psi_sym2[1]*Rational(1,8) + psi_sym2[2]*Rational(1,64)
growth_eq = psi_at_8th - Rational(1, 2)
print(f"  Growth constraint: {simplify(growth_eq)} = 0")

sol_deg2 = solve([sol_deg2_eq, growth_eq], [c1, c2])
print(f"  Solutions: {sol_deg2}")

if sol_deg2:
    for sol in sol_deg2 if isinstance(sol_deg2, list) else [sol_deg2]:
        if isinstance(sol, dict):
            c1v, c2v = sol[c1], sol[c2]
        else:
            c1v, c2v = sol
        c1v = simplify(c1v)
        c2v = simplify(c2v)
        print(f"\n  c1 = {c1v}, c2 = {c2v}")

        # Check if c1, c2 are rational
        is_rational = c1v.is_rational and c2v.is_rational if hasattr(c1v, 'is_rational') else False
        print(f"  Rational? {is_rational}")
        if c1v.is_number:
            print(f"  c1 ≈ {float(c1v):.6f}, c2 ≈ {float(c2v):.6f}")

        psi_vals = [simplify(p.subs(c1, c1v).subs(c2, c2v)) for p in psi_sym2]
        print(f"  psi coeffs: {[float(p) if p.is_number else p for p in psi_vals[:6]]}")

        # Verify psi terminates
        for n in range(3, min(6, max_t2)):
            val = simplify(psi_sym2[n].subs(c1, c1v).subs(c2, c2v))
            print(f"    psi_{n} = {val}")
