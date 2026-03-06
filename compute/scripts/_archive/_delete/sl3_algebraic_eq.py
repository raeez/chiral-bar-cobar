#!/usr/bin/env python3
"""Find algebraic equation for sl_3 bar cohomology GF using discriminant constraint.

Known: H^1=8, H^2=36, H^3=204. GF Q(t) = 1 + 8t + 36t^2 + 204t^3 + H4*t^4 + ...
Radius of convergence = 1/8 (growth rate dim(g)=8).

Ansatz: A(t)*Q^2 + B(t)*Q + C(t) = 0 with C=1, A=t*P(t), B=-1+t*R(t).
Constraint 1: coefficients match through t^3 (3 equations).
Constraint 2: discriminant vanishes at t=1/8 (fixes remaining freedom).
Then t^4 coefficient gives H^4.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, Poly, cancel, together, S)

t, Q, p1 = symbols('t Q p1')

# Known coefficients
h = [1, 8, 36, 204]  # Q = h[0] + h[1]*t + h[2]*t^2 + h[3]*t^3 + ...

# Q^2 coefficients
q2 = [0]*8
for i in range(4):
    for j in range(4):
        if i+j < 8:
            q2[i+j] += h[i]*h[j] if i < len(h) and j < len(h) else 0

print("Q^2 coefficients:")
for i in range(7):
    print(f"  t^{i}: {q2[i]}")

# Ansatz: (p0*t + p1*t^2)*Q^2 + (-1 + r0*t + r1*t^2)*Q + 1 = 0
# From matching t^0: -1 + 1 = 0 OK
# From matching t^1: p0*q2[0] - h[1] + r0*h[0] = 0
#   => p0 + r0 = 8
# From matching t^2: p0*q2[1] + p1*q2[0] - h[2] + r0*h[1] + r1*h[0] = 0
#   => 16*p0 + p1 + 8*r0 + r1 = 36
# From matching t^3: p0*q2[2] + p1*q2[1] - h[3] + r0*h[2] + r1*h[1] = 0
#   => q2[2]*p0 + 16*p1 + 36*r0 + 8*r1 = 204

print(f"\nq2[0]={q2[0]}, q2[1]={q2[1]}, q2[2]={q2[2]}, q2[3]={q2[3]}")

# Solve for p0, r0, r1 in terms of p1 (free parameter)
# Eq1: p0 + r0 = 8
# Eq2: 16*p0 + p1 + 8*r0 + r1 = 36
# Eq3: q2[2]*p0 + 16*p1 + 36*r0 + 8*r1 = 204

from sympy import Matrix, linsolve
p0, r0, r1_sym = symbols('p0 r0 r1')

eqs = [
    p0 + r0 - 8,
    16*p0 + p1 + 8*r0 + r1_sym - 36,
    q2[2]*p0 + 16*p1 + 36*r0 + 8*r1_sym - 204,
]

sol = solve(eqs, [p0, r0, r1_sym])
print(f"\nSolution (parametric in p1):")
for k, v in sol.items():
    print(f"  {k} = {v}")

p0_expr = sol[p0]
r0_expr = sol[r0]
r1_expr = sol[r1_sym]

# Now compute H4 from t^4 coefficient:
# p0*q2[3] + p1*q2[2] - H4 + r0*h[3] + r1*h[2] = 0
# H4 = p0*q2[3] + p1*q2[2] + r0*h[3] + r1*h[2]

H4_expr = p0_expr*q2[3] + p1*q2[2] + r0_expr*h[3] + r1_expr*h[2]
H4_expr = expand(H4_expr)
print(f"\nH4 = {H4_expr}")
print(f"H4 simplified = {simplify(H4_expr)}")

# Now use discriminant constraint: disc(1/8) = 0
# disc = B^2 - 4*A*C where A = (p0+p1*t)*t, B = -1+r0*t+r1*t^2, C = 1
# disc = (-1+r0*t+r1*t^2)^2 - 4*(p0*t+p1*t^2)

# At t=1/8:
t_val = Rational(1, 8)
B_val = -1 + r0_expr*t_val + r1_expr*t_val**2
A_val = p0_expr*t_val + p1*t_val**2
disc_val = expand(B_val**2 - 4*A_val)
print(f"\nDiscriminant at t=1/8 = {simplify(disc_val)}")

# Solve disc(1/8) = 0 for p1
p1_solutions = solve(disc_val, p1)
print(f"\np1 solutions: {p1_solutions}")

for p1_val in p1_solutions:
    p1_float = float(p1_val.evalf())
    p0_val = p0_expr.subs(p1, p1_val)
    r0_val = r0_expr.subs(p1, p1_val)
    r1_val = r1_expr.subs(p1, p1_val)
    H4_val = H4_expr.subs(p1, p1_val)

    print(f"\n--- p1 = {p1_val} (≈{p1_float:.6f}) ---")
    print(f"  p0 = {p0_val}")
    print(f"  r0 = {r0_val}")
    print(f"  r1 = {r1_val}")
    print(f"  H4 = {H4_val} = {float(H4_val.evalf()):.6f}")

    # Check: is H4 a positive integer?
    H4_simplified = simplify(H4_val)
    print(f"  H4 simplified = {H4_simplified}")

    # Also compute the full discriminant polynomial
    p0_n = p0_val
    r0_n = r0_val
    r1_n = r1_val

    A_poly = (p0_n + p1_val*t)*t
    B_poly = -1 + r0_n*t + r1_n*t**2
    disc_poly = expand(B_poly**2 - 4*A_poly)
    disc_factored = factor(disc_poly)
    print(f"  Discriminant = {disc_factored}")

    # Compute Q series from the equation
    # Q = (-B - sqrt(disc)) / (2A) (pick correct branch)
    disc_sqrt = sqrt(disc_poly)
    Q_minus = (-B_poly - disc_sqrt) / (2*A_poly)
    Q_plus = (-B_poly + disc_sqrt) / (2*A_poly)

    Q_m_series = series(Q_minus, t, 0, 8)
    Q_p_series = series(Q_plus, t, 0, 8)

    print(f"\n  Q- series:")
    for n in range(6):
        c = Q_m_series.coeff(t, n)
        print(f"    t^{n}: {simplify(c)}")

    print(f"  Q+ series:")
    for n in range(6):
        c = Q_p_series.coeff(t, n)
        print(f"    t^{n}: {simplify(c)}")

# Also try: discriminant has DOUBLE root at t=1/8 (maximally constrained)
print("\n" + "="*70)
print("ALTERNATIVE: disc has root at t=1/8 AND specific second root")
print("="*70)

# For sl_2: disc = (1-3t)(1+t). Roots: 1/3, -1.
# Pattern: (1 - d*t)(1 + alpha*t) where d = dim g.
# For sl_2: alpha = 1. For sl_3: alpha = ?
# This gives disc = 1 + (alpha-d)*t - d*alpha*t^2

# Our disc from the ansatz has degree 4 in t (from r1^2*t^4 term).
# But maybe with the right p1, it simplifies.

# Let me also try the approach where we match sl_2 first to validate.
print("\n" + "="*70)
print("VALIDATION: sl_2 case")
print("="*70)

h2 = [1, 3, 6, 15, 36, 91, 232]
q2_sl2 = [0]*10
for i in range(len(h2)):
    for j in range(len(h2)):
        if i+j < 10:
            q2_sl2[i+j] += h2[i]*h2[j]

# Same ansatz for sl_2: (p0*t+p1*t^2)*Q^2 + (-1+r0*t+r1*t^2)*Q + 1 = 0
# t^1: p0 + r0 = 3
# t^2: q2_sl2[1]*p0 + p1 + h2[1]*r0 + r1 = 6
# t^3: q2_sl2[2]*p0 + q2_sl2[1]*p1 + h2[2]*r0 + h2[1]*r1 = 15

eqs2 = [
    p0 + r0 - 3,
    q2_sl2[1]*p0 + p1 + h2[1]*r0 + r1_sym - 6,
    q2_sl2[2]*p0 + q2_sl2[1]*p1 + h2[2]*r0 + h2[1]*r1_sym - 15,
]
sol2 = solve(eqs2, [p0, r0, r1_sym])
print(f"\nsl_2 solution (parametric in p1):")
for k, v in sol2.items():
    print(f"  {k} = {v}")

# Discriminant at t=1/3 = 0
t_val2 = Rational(1, 3)
B_val2 = -1 + sol2[r0]*t_val2 + sol2[r1_sym]*t_val2**2
A_val2 = sol2[p0]*t_val2 + p1*t_val2**2
disc_val2 = expand(B_val2**2 - 4*A_val2)
p1_sol2 = solve(disc_val2, p1)
print(f"\nsl_2: p1 solutions from disc(1/3)=0: {p1_sol2}")

for pv in p1_sol2:
    p0v = sol2[p0].subs(p1, pv)
    r0v = sol2[r0].subs(p1, pv)
    r1v = sol2[r1_sym].subs(p1, pv)
    print(f"\n  p1={pv}: p0={p0v}, r0={r0v}, r1={r1v}")

    # Check if this gives t(1+t)Q^2 - (1+t)Q + 1 = 0
    # i.e. A = t(1+t), B = -(1+t), C = 1
    # A = t + t^2 => p0=1, p1=1; B = -1-t => r0=-1... wait
    # Our B = -1 + r0*t + r1*t^2
    # Manuscript: B = -(1+t) = -1-t, so r0 = -1? No, r0 = negative of the coefficient.
    # Actually our B(t) = -1 + r0*t + r1*t^2
    # Manuscript: B(t) = -(1+t) = -1 - t => r0 = -1, r1 = 0
    # Our A(t) = p0*t + p1*t^2
    # Manuscript: A(t) = t(1+t) = t + t^2 => p0=1, p1=1

    print(f"  Expected: p0=1, p1=1, r0=-1, r1=0")
    print(f"  Match: p0={'OK' if p0v==1 else 'FAIL'}, r0={'OK' if r0v==-1 else 'FAIL'}, r1={'OK' if r1v==0 else 'FAIL'}")

    # H4 for sl_2:
    H4_sl2 = p0v*q2_sl2[3] + pv*q2_sl2[2] + r0v*h2[3] + r1v*h2[2]
    print(f"  H4 (sl_2) = {H4_sl2} (expected 36)")

    # Discriminant
    A_p = (p0v + pv*t)*t
    B_p = -1 + r0v*t + r1v*t**2
    disc_p = expand(B_p**2 - 4*A_p)
    print(f"  disc = {factor(disc_p)}")
