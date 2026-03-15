#!/usr/bin/env python3
"""Analyze the sl3 bar cohomology generating function.

Known: H = [8, 36, 204, ?, ?]
Conjectured recurrence: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
Conjectured GF: Q(x) = 4x(2-13x-2x^2)/((1-8x)(1-3x-x^2))
"""

from sympy import (Rational, symbols, sqrt, solve, simplify, N,
                   series, apart, factor, expand, cancel)

x = symbols('x')

H = [8, 36, 204]

print("=" * 60)
print("sl3 BAR COHOMOLOGY GF ANALYSIS")
print("=" * 60)

# 1. Check conjectured GF
Q_conj = 4*x*(2 - 13*x - 2*x**2) / ((1 - 8*x)*(1 - 3*x - x**2))
Q_series = series(Q_conj, x, 0, n=8)
coeffs = [int(Q_series.coeff(x, i)) for i in range(1, 8)]
print(f"Conjectured GF coefficients: {coeffs}")
print(f"Known values:                {H}")
print(f"Match: {coeffs[:3] == H}")
print(f"Predictions: H4={coeffs[3]}, H5={coeffs[4]}, H6={coeffs[5]}")

# 2. Recurrence
print("\nRecurrence: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3) for n>=4")
denom = expand((1-8*x)*(1-3*x-x**2))
print(f"Denominator: {denom}")

# 3. Partial fractions
pf = apart(Q_conj, x)
print(f"\nPartial fractions: {pf}")

# 4. Growth rate
print("\nPoles of Q(x):")
print(f"  1/8 = 0.125 (growth rate 8 = dim sl3)")
r1 = (-3 + sqrt(13))/(-2)
print(f"  {float(r1):.6f} (growth rate {float(1/r1):.4f})")

# 5. Psi-equation analysis for sl3
# For sl2: x*(1+x)*P^2 - (1+x)*P + 1 = 0, i.e. psi = 1+x
# General: x*psi*P^2 - psi*P + 1 = 0
# Solving for psi coefficients given P = [1, 8, 36, 204, ...]

print("\n" + "=" * 60)
print("PSI-EQUATION: x*psi*P^2 - psi*P + 1 = 0")
print("=" * 60)

P = [1, 8, 36, 204]
max_t = 8
P_ext = P + [0] * (max_t - len(P))
P2 = [0] * max_t
for i in range(max_t):
    for j in range(max_t):
        if i+j < max_t:
            P2[i+j] += P_ext[i] * P_ext[j]
print(f"P^2 coeffs: {P2[:6]}")

# Solve for psi = [psi_0, psi_1, ...] from:
# sum_k psi_k * P2[n-k-1] - sum_k psi_k * P[n-k] + delta_{n,0} = 0
psi = [0] * max_t
# n=0: 0 - psi_0*P[0] + 1 = 0 => psi_0 = 1
psi[0] = 1
for n in range(1, min(len(P)+1, max_t)):
    # sum_k<n psi_k * P2[n-k-1] - sum_k<n psi_k * P[n-k] - psi_n * P[0] = 0
    val = 0
    for k in range(n):
        if n-k-1 >= 0 and n-k-1 < max_t:
            val += psi[k] * P2[n-k-1]
        val -= psi[k] * (P_ext[n-k] if n-k < max_t else 0)
    # val - psi[n]*P[0] = 0
    psi[n] = val  # since P[0] = 1

print(f"psi coefficients: {psi[:6]}")
print(f"psi = {psi[0]} + {psi[1]}*x + {psi[2]}*x^2 + {psi[3]}*x^3 + ...")

for d in range(1, 5):
    terminates = all(psi[k] == 0 for k in range(d+1, min(d+3, max_t)))
    print(f"  Degree {d} polynomial? {terminates} (check psi[{d+1}:]={psi[d+1:d+3]})")

# 6. If psi doesn't terminate, the sl2 form doesn't apply.
# Try: general degree-2 algebraic equation A(x)*P^2 + B(x)*P + C(x) = 0
# with A, B, C polynomials. P has growth rate 8, so discriminant vanishes at x=1/8.

print("\n" + "=" * 60)
print("GENERAL QUADRATIC: A*P^2 + B*P + C = 0")
print("=" * 60)

# Parametrize: A = x*a(x), B = b(x), C = 1 (normalized so C(0)=1, P(0)=1)
# At x=0: B(0)*1 + 1 = 0 => B(0) = -1
# So B = -1 + b1*x + b2*x^2 + ...
# A = a0*x + a1*x^2 + ...

# With A = a0*x, B = -1 + b1*x, C = 1 (4 free params: a0, b1. Total: 2 params)
# Constraint from P1=8:
# n=1: a0*P[0]^2 + (-1)*P[1] + b1*P[0] = 0
# a0*1 - 8 + b1 = 0 => a0 + b1 = 8

# Constraint from P2=36:
# n=2: a0*(2*P[0]*P[1]) + (-1)*P[2] + b1*P[1] = 0
# a0*16 - 36 + 8*b1 = 0 => 16*a0 + 8*b1 = 36

# From n=1: b1 = 8 - a0
# Substituting: 16*a0 + 8*(8-a0) = 36 => 16a0 + 64 - 8a0 = 36 => 8a0 = -28 => a0 = -7/2
# b1 = 8 - (-7/2) = 23/2

a0 = Rational(-7, 2)
b1 = 8 - a0
print(f"A = {a0}*x, B = -1 + {b1}*x")
print(f"Equation: {a0}*x*P^2 + (-1 + {b1}*x)*P + 1 = 0")

# Check P3=204:
# n=3: a0*(2*P0*P2 + P1^2) + (-1)*P3 + b1*P2 = 0
check3 = a0*(2*1*36 + 64) + (-1)*204 + b1*36
print(f"Check n=3: {check3} (should be 0)")

if check3 == 0:
    print("CONSISTENT! The equation holds with known data.")
    # Predict P4:
    # n=4: a0*(2*P0*P3 + 2*P1*P2) + (-1)*P4 + b1*P3 = 0
    # P4 = a0*(2*204 + 2*8*36) + b1*204
    P4_pred = a0*(2*204 + 2*8*36) + b1*204
    print(f"P4 = {P4_pred} = {int(P4_pred)}")

    # Discriminant: B^2 - 4AC = (-1+23/2*x)^2 - 4*(-7/2*x)*1
    # = 1 - 23x + (23/2)^2*x^2 + 14x
    # = 1 - 9x + 529/4*x^2
    A_poly = a0*x
    B_poly = -1 + b1*x
    disc = expand(B_poly**2 - 4*A_poly*1)
    print(f"\nDiscriminant: {disc}")
    print(f"= {factor(disc)}")

    # Growth rate: disc vanishes at x_c where 1/x_c is the growth rate
    disc_roots = solve(disc, x)
    print(f"Discriminant roots: {disc_roots}")
    for r in disc_roots:
        print(f"  x = {r} = {float(r):.6f}, growth rate = {float(1/r):.4f}")

    # P = (-B + sqrt(disc)) / (2A) (taking + branch for P(0)=1)
    P_formula = (-B_poly + sqrt(disc)) / (2*A_poly)
    P_series_check = series(P_formula, x, 0, n=7)
    print(f"\nP(x) from formula: {P_series_check}")
else:
    print(f"NOT consistent. Residual = {check3}")
    # Need higher degree A or B
    print("Trying A = a0*x + a1*x^2, B = -1 + b1*x + b2*x^2, C = 1")

    a0s, a1s, b1s, b2s = symbols('a0 a1 b1 b2')
    # n=1: a0 + b1 = 8
    # n=2: a0*16 + a1 + 8*b1 + b2 = 36 (hmm need to be more careful)
    # Actually let me set up the equations properly.

    A_p = a0s*x + a1s*x**2
    B_p = -1 + b1s*x + b2s*x**2

    # A*P^2 + B*P + C = 0 at each order
    # Use P = 1 + 8x + 36x^2 + 204x^3 + P4*x^4 + ...
    P4s = symbols('P4')
    P_sym = 1 + 8*x + 36*x**2 + 204*x**3 + P4s*x**4

    eq = expand(A_p * P_sym**2 + B_p * P_sym + 1)

    # Extract coefficients
    eqs = []
    for n in range(1, 5):
        c = eq.coeff(x, n)
        c_simplified = simplify(c)
        eqs.append(c_simplified)
        if n <= 3:
            print(f"  x^{n}: {c_simplified} = 0")

    # Solve n=1,2,3 for a0,a1,b1,b2 (4 unknowns, 3 equations -> 1-param family)
    sol = solve(eqs[:3], [a0s, a1s, b1s, b2s], dict=True)
    print(f"\n  Solutions: {sol}")

    if sol:
        for s in sol:
            print(f"\n  Solution: {s}")
            # Use n=4 to get P4
            eq4 = eqs[3].subs(s)
            eq4_simplified = simplify(eq4)
            print(f"  x^4 equation: {eq4_simplified} = 0")
            P4_sol = solve(eq4_simplified, P4s)
            print(f"  P4 = {P4_sol}")
