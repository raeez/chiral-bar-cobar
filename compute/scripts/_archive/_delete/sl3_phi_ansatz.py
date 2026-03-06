#!/usr/bin/env python3
"""Find sl_3 bar cohomology GF using the structural ansatz from sl_2.

For sl_2: t*phi(t)*Q^2 - phi(t)*Q + 1 = 0, phi(t) = 1+t.
This gives Q = [1 - sqrt(1 - 4t/phi(t))] / (2t).

For sl_3: same structural form with phi(t) = 1 + a*t + b*t^2 + ...
Fit a, b, ... to match Q = 1 + 8t + 36t^2 + 204t^3 + ...

The discriminant is phi(t)*(phi(t)-4t), with roots determined by phi.
Radius of convergence = smallest positive root of phi(t)-4t = 0.
For growth rate 8: need phi(1/8) - 4/8 = 0, i.e. phi(1/8) = 1/2.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, S, collect)

t = symbols('t')
a, b, c_coeff = symbols('a b c')

# ================================================================
# VALIDATION: sl_2
# ================================================================
print("=" * 60)
print("VALIDATION: sl_2")
print("=" * 60)

phi_sl2 = 1 + t
g_sl2 = 1 - 4*t / phi_sl2
Q_sl2 = (1 - sqrt(g_sl2)) / (2*t)
Q_sl2_series = series(Q_sl2, t, 0, 8)
print("sl_2 Q series:")
for n in range(7):
    print(f"  t^{n}: {Q_sl2_series.coeff(t, n)}")
print("Expected: 1, 3, 6, 15, 36, 91, 232")

# ================================================================
# sl_3: phi(t) = 1 + a*t
# ================================================================
print("\n" + "=" * 60)
print("sl_3: phi = 1 + a*t (linear)")
print("=" * 60)

phi = 1 + a*t
g = 1 - 4*t / phi
Q_param = (1 - sqrt(g)) / (2*t)
Q_series = series(Q_param, t, 0, 6)

coeffs = {}
for n in range(5):
    cn = simplify(Q_series.coeff(t, n))
    coeffs[n] = cn
    print(f"  t^{n}: {cn}")

# Match t^0 = 1: always true (since g starts as 1-4t+...)
# Match t^1 = 8:
eq1 = coeffs[1] - 8
a_sol_linear = solve(eq1, a)
print(f"\nFrom Q[1]=8: a = {a_sol_linear}")

for a_val in a_sol_linear:
    print(f"\n  a = {a_val}:")
    for n in range(5):
        cn = coeffs[n].subs(a, a_val)
        print(f"    Q[{n}] = {simplify(cn)}")
    # Check phi(1/8)-1/2=0: need smallest positive root of phi-4t
    psi = (1 + a_val*t - 4*t)
    roots = solve(psi, t)
    print(f"    phi-4t roots: {roots}")

# ================================================================
# sl_3: phi(t) = 1 + a*t + b*t^2 (quadratic)
# ================================================================
print("\n" + "=" * 60)
print("sl_3: phi = 1 + a*t + b*t^2 (quadratic)")
print("=" * 60)

phi2 = 1 + a*t + b*t**2
g2 = 1 - 4*t / phi2
Q2 = (1 - sqrt(g2)) / (2*t)
Q2_series = series(Q2, t, 0, 6)

coeffs2 = {}
for n in range(5):
    cn = simplify(Q2_series.coeff(t, n))
    coeffs2[n] = cn
    # Print only if small
    if n <= 1:
        print(f"  t^{n}: {cn}")

# Match Q[1] = 8 and Q[2] = 36
eq_q1 = coeffs2[1] - 8
eq_q2 = coeffs2[2] - 36

print(f"\n  Q[1] - 8 = {simplify(eq_q1)}")
print(f"  Q[2] - 36 = {simplify(eq_q2)}")

sol_ab = solve([eq_q1, eq_q2], [a, b])
print(f"\n  Solutions (a, b): {sol_ab}")

for sol in sol_ab if isinstance(sol_ab, list) else [sol_ab]:
    if isinstance(sol, dict):
        a_val, b_val = sol[a], sol[b]
    else:
        a_val, b_val = sol

    print(f"\n  a={a_val}, b={b_val}:")

    # Check Q[3]
    q3 = coeffs2[3].subs(a, a_val).subs(b, b_val)
    q3_simplified = simplify(q3)
    print(f"    Q[3] = {q3_simplified} (expected 204)")

    if q3_simplified == 204:
        print("    *** Q[3] MATCHES! ***")
        q4 = coeffs2[4].subs(a, a_val).subs(b, b_val)
        q4_simplified = simplify(q4)
        print(f"    Q[4] = {q4_simplified}  <-- THIS IS H^4")

        # Compute more terms
        Q_long = series(Q2.subs(a, a_val).subs(b, b_val), t, 0, 10)
        print("\n    Full series:")
        for n in range(10):
            cn = simplify(Q_long.coeff(t, n))
            print(f"      Q[{n}] = {cn}")

        # Discriminant
        phi_val = phi2.subs(a, a_val).subs(b, b_val)
        disc = phi_val * (phi_val - 4*t)
        print(f"\n    phi(t) = {phi_val}")
        print(f"    disc = phi*(phi-4t) = {factor(disc)}")

        # Roots of phi-4t
        psi = expand(phi_val - 4*t)
        roots = solve(psi, t)
        print(f"    Roots of phi-4t: {roots}")
        for r in roots:
            print(f"      1/r = {simplify(1/r)}")

# ================================================================
# sl_3: phi(t) = 1 + a*t + b*t^2 + c*t^3 (cubic) — if quadratic fails
# ================================================================
# Only run if quadratic didn't give a match

print("\n" + "=" * 60)
print("sl_3: phi = 1 + a*t + b*t^2 + c*t^3 (cubic, fit 3 coeffs)")
print("=" * 60)

phi3 = 1 + a*t + b*t**2 + c_coeff*t**3
g3 = 1 - 4*t / phi3
Q3 = (1 - sqrt(g3)) / (2*t)
Q3_series = series(Q3, t, 0, 6)

coeffs3 = {}
for n in range(5):
    cn = Q3_series.coeff(t, n)
    coeffs3[n] = cn

# Match Q[1]=8, Q[2]=36, Q[3]=204
eq3_1 = simplify(coeffs3[1] - 8)
eq3_2 = simplify(coeffs3[2] - 36)
eq3_3 = simplify(coeffs3[3] - 204)

print(f"  Solving Q[1]=8, Q[2]=36, Q[3]=204 for (a,b,c)...")
sol3 = solve([eq3_1, eq3_2, eq3_3], [a, b, c_coeff])
print(f"  Solutions: {sol3}")

for sol in sol3 if isinstance(sol3, list) else [sol3]:
    if isinstance(sol, dict):
        a_v, b_v, c_v = sol[a], sol[b], sol[c_coeff]
    else:
        a_v, b_v, c_v = sol

    print(f"\n  a={a_v}, b={b_v}, c={c_v}:")
    phi_val = phi3.subs(a, a_v).subs(b, b_v).subs(c_coeff, c_v)
    print(f"    phi(t) = {phi_val}")

    Q_check = (1 - sqrt(1 - 4*t/phi_val)) / (2*t)
    Q_check_series = series(Q_check, t, 0, 10)
    print("    Series:")
    for n in range(8):
        cn = simplify(Q_check_series.coeff(t, n))
        print(f"      Q[{n}] = {cn}")

    # Discriminant and radius
    psi = expand(phi_val - 4*t)
    roots = solve(psi, t)
    print(f"    Roots of phi-4t: {roots}")
    for r in roots:
        rv = simplify(r)
        print(f"      root = {rv}, 1/root = {simplify(1/rv)}")
