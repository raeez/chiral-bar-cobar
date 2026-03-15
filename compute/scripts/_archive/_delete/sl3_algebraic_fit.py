#!/usr/bin/env python3
"""Fit an algebraic equation to the sl_3 bar cohomology generating function.

Q(x) = 8x + 36x^2 + 204x^3 + a_4 x^4 + ...

Try: A(x) Q^2 + B(x) Q + C(x) = 0
where A, B, C are polynomials and disc = B^2 - 4AC vanishes at x=1/8.

For sl_2: Q = 3x + 6x^2 + ..., equation is x(1+x)Q^2 - (1+x)Q + x = 0?
Wait, need to first find the sl_2 equation for Q (the SHIFTED sequence).
"""

from sympy import (symbols, solve, expand, factor, simplify, Rational,
                   sqrt, series, Poly, cancel, together, S, nsolve)
import numpy as np
from fractions import Fraction

x = symbols('x')

# ============================================================
# Step 1: Find the equation satisfied by Q_sl2(x) = 3x + 6x^2 + ...
# ============================================================

print("=" * 60)
print("STEP 1: Equation for Q_sl2(x) = 3x + 6x^2 + 15x^3 + ...")
print("=" * 60)

# R(x) = 1 + x^2 + x^3 + x^3*Q(x) + ... wait, Q = sum R(n+3)*x^n starting n=1
# Actually R = sum R(n) x^n, and:
# Q(x) = sum_{n=1}^inf R(n+3) x^n
# R(x) = 1 + 0*x + 1*x^2 + 1*x^3 + R(4)x^4 + ...
#       = 1 + x^2 + x^3*(1 + Q(x)/x) ... no, let me be careful.

# Q(x) = R(4)x + R(5)x^2 + R(6)x^3 + ... = 3x + 6x^2 + 15x^3 + ...
# R(x) = R(0) + R(1)x + R(2)x^2 + R(3)x^3 + x^3*(R(4)x + R(5)x^2 + ...)
#       = 1 + 0*x + x^2 + x^3 + x^3*Q(x)

# R satisfies: x(1+x)R^2 - (1+x)R + 1 = 0
# Substitute R = 1 + x^2 + x^3 + x^3*Q:
# Let me use sympy to do this substitution and get Q's equation.

Q_sym = symbols('Q')
R_sub = 1 + x**2 + x**3 + x**3 * Q_sym
eq_R = x*(1+x)*R_sub**2 - (1+x)*R_sub + 1
eq_R_expanded = expand(eq_R)

# Factor out x powers
poly_Q = Poly(eq_R_expanded, Q_sym)
coeffs_Q = poly_Q.all_coeffs()

print(f"Equation for Q (from R's equation):")
for i, c in enumerate(coeffs_Q):
    power = poly_Q.degree() - i
    c_factored = factor(c)
    print(f"  Q^{power}: {c_factored}")

# Divide out common x factors
# Q^2 coefficient: x^7*(x+1)
# Q^1 coefficient: x^3*(x+1)*(2x^4 + 2x^3 + 2x - 1)
# Q^0 coefficient: x^4*(x^4 + 3x^3 + 3x^2 + 3x + 3)

# Minimum x power: x^3. Divide by x^3:
# x^4*(x+1)*Q^2 + (x+1)*(2x^4+2x^3+2x-1)*Q + x*(x^4+3x^3+3x^2+3x+3) = 0

# Hmm, still has x^4 in Q^2 term. At x=0, only Q^1 survives:
# (0+1)*(0+0+0-1)*Q + 0 = -Q = 0, so Q(0) = 0. ✓

# Let me verify by computing Q from this equation directly.
# The equation x^4(x+1)Q^2 + (x+1)(2x^4+2x^3+2x-1)Q + x(x^4+3x^3+3x^2+3x+3) = 0
# has Q = [-B ± sqrt(B^2-4AC)] / (2A)

# Actually, this is a very high-degree equation. The sl_2 Q satisfies
# a complicated equation because of the shift. That's expected.

# ============================================================
# Step 2: Direct approach - find algebraic equation for Q_sl3
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: Direct algebraic fit for Q_sl3 = 8x + 36x^2 + 204x^3")
print("=" * 60)

# Try: A(x) Q^2 + B(x) Q + C(x) = 0
# with A = a0 + a1*x, B = b0 + b1*x + b2*x^2, C = c1*x + c2*x^2

# Q = 8x + 36x^2 + 204x^3 + a4*x^4 + ...
# Q^2 = 64x^2 + 2*8*36*x^3 + ... = 64x^2 + 576x^3 + ...

h = [0, 8, 36, 204]  # h[n] = coeff of x^n in Q

# Q^2 coefficients:
q2 = [0, 0, 0, 0]  # up to x^3
q2[2] = h[1]**2  # 64
q2[3] = 2*h[1]*h[2]  # 576

# Equation: (a0+a1*x)(64x^2+576x^3+...) + (b0+b1*x+b2*x^2)(8x+36x^2+204x^3+...) + (c1*x+c2*x^2) = 0

# x^0: 0 = 0. ✓
# x^1: 8*b0 + c1 = 0  =>  c1 = -8*b0
# x^2: 64*a0 + 36*b0 + 8*b1 + c2 = 0
# x^3: 576*a0 + 64*a1 + 204*b0 + 36*b1 + 8*b2 = 0

# Unknowns: a0, a1, b0, b1, b2, c2 (c1 determined)
# 3 equations, 6 unknowns. Need 3 more constraints.

# Constraint 4: disc = B^2 - 4AC vanishes at x=1/8
# Constraint 5: growth rate normalization (optional)
# Constraint 6: normalization (e.g., a0 = 1)

# Let me use normalization a0 = 1.
# Then from x^2: 64 + 36*b0 + 8*b1 + c2 = 0 => c2 = -64 - 36*b0 - 8*b1
# From x^3: 576 + 64*a1 + 204*b0 + 36*b1 + 8*b2 = 0

# Still 4 unknowns: a1, b0, b1, b2 with 1 equation + disc constraint.

# disc(x) = (b0+b1*x+b2*x^2)^2 - 4*(1+a1*x)*(c1*x+c2*x^2)
# with c1 = -8*b0, c2 = -64-36*b0-8*b1.

# disc(1/8) = 0 gives another equation.

# ALSO: for the GF to have growth rate 8^n, the radius of convergence = 1/8.
# This means disc has a zero at x=1/8 (and this should be the closest
# singularity to the origin). The disc might also have a double zero there.

# Let me add: disc'(1/8) = 0 (double root) as constraint 5.
# But actually, for sl_2, the disc has SIMPLE zeros at 1/3 and -1.
# So a double root is NOT expected. Let me not assume that.

# Instead, let me try to minimize unknowns. Set b2 = 0 (simplest B).
# Then from x^3: 576 + 64*a1 + 204*b0 + 36*b1 = 0
#   => a1 = -(576 + 204*b0 + 36*b1) / 64

# Now 2 unknowns: b0, b1.
# Plus disc(1/8) = 0.

# c1 = -8*b0
# c2 = -64 - 36*b0 - 8*b1
# a1 = -(576 + 204*b0 + 36*b1)/64

# disc(x) = (b0+b1*x)^2 - 4(1+a1*x)(c1*x+c2*x^2)
# disc(1/8) = (b0+b1/8)^2 - 4(1+a1/8)(c1/8+c2/64)

b0_s, b1_s = symbols('b0 b1')
a1_s = -(576 + 204*b0_s + 36*b1_s) / 64
c1_s = -8*b0_s
c2_s = -64 - 36*b0_s - 8*b1_s

disc_at_18 = (b0_s + b1_s/8)**2 - 4*(1 + a1_s/8)*(c1_s/8 + c2_s/64)
disc_at_18_simplified = simplify(expand(disc_at_18))
print(f"\ndisc(1/8) = {disc_at_18_simplified}")

# This gives one equation in two unknowns (b0, b1).
# Need one more constraint.

# Let me try: the second root of disc should also be a nice number.
# disc(x) = (b0+b1*x)^2 - 4(1+a1*x)(c1*x+c2*x^2)

# This is a polynomial of degree 2 in x (since b2=0 and A is linear):
# disc = b0^2 + 2*b0*b1*x + b1^2*x^2 - 4*(c1*x + c2*x^2 + a1*c1*x^2 + a1*c2*x^3)
# Wait, A*C = (1+a1*x)(c1*x+c2*x^2) = c1*x + c2*x^2 + a1*c1*x^2 + a1*c2*x^3
# This has degree 3! So disc has degree 3 (from the a1*c2*x^3 term)
# unless a1*c2 = 0.

# For disc to be degree 2 (so that we get two branch points and an algebraic
# function of degree 2), we need a1*c2 = 0.

# If c2 = 0: then c2 = -64 - 36*b0 - 8*b1 = 0 => b1 = (-64-36*b0)/8
# If a1 = 0: then 576 + 204*b0 + 36*b1 = 0 => b1 = -(576+204*b0)/36

# Let me try c2 = 0:
print("\n--- Case c2 = 0 ---")
b1_from_c2 = (-64 - 36*b0_s) / 8
a1_from_c2 = -(576 + 204*b0_s + 36*b1_from_c2) / 64
a1_from_c2 = simplify(a1_from_c2)
print(f"b1 = {b1_from_c2}")
print(f"a1 = {a1_from_c2}")

disc_c2 = (b0_s + b1_from_c2*x)**2 - 4*(1+a1_from_c2*x)*(c1_s*x)
disc_c2 = simplify(expand(disc_c2.subs(c1_s, -8*b0_s)))
print(f"disc = {factor(disc_c2)}")

# Now disc(1/8) = 0:
disc_c2_at_18 = disc_c2.subs(x, Rational(1, 8))
disc_c2_at_18 = simplify(disc_c2_at_18)
print(f"disc(1/8) = {disc_c2_at_18}")

# Solve for b0:
b0_sols_c2 = solve(disc_c2_at_18, b0_s)
print(f"b0 solutions: {b0_sols_c2}")

for b0_val in b0_sols_c2:
    b1_val = b1_from_c2.subs(b0_s, b0_val)
    a1_val = a1_from_c2.subs(b0_s, b0_val)
    c1_val = -8*b0_val

    print(f"\n  b0={b0_val}, b1={b1_val}, a1={a1_val}, c1={c1_val}, c2=0")

    # Compute Q(x) = [-B + sqrt(disc)] / (2A)
    A = 1 + a1_val*x
    B = b0_val + b1_val*x
    C = c1_val*x
    disc_full = B**2 - 4*A*C
    print(f"  disc = {factor(disc_full)}")

    # Q = (-B ± sqrt(disc)) / (2A)
    # Need to pick the sign that gives Q(0) = 0.
    # At x=0: Q(0) = (-b0 ± |b0|) / 2
    # For Q(0)=0: need -b0 + |b0| = 0 (if b0>0) => impossible
    #            or -b0 - |b0| = 0 (if b0<0) => 0 OK... wait:
    # (-b0 + b0)/2 = 0 if b0 > 0, using + sign. ✓
    # (-b0 - b0)/2 = -b0 if b0 > 0. Not 0.

    if b0_val > 0:
        Q_expr = (-B + sqrt(disc_full)) / (2*A)
    else:
        Q_expr = (-B - sqrt(disc_full)) / (2*A)

    Q_series = series(Q_expr, x, 0, 6)
    print(f"  Q(x) = {Q_series}")

    # Extract coefficients
    for n in range(1, 6):
        coeff = Q_series.coeff(x, n)
        print(f"    H^{n} = {simplify(coeff)}")

# Now try a1 = 0:
print("\n--- Case a1 = 0 ---")
b1_from_a1 = -(576 + 204*b0_s) / 36
c2_from_a1 = -64 - 36*b0_s - 8*b1_from_a1
c2_from_a1 = simplify(c2_from_a1)
print(f"b1 = {b1_from_a1}")
print(f"c2 = {c2_from_a1}")

disc_a1 = (b0_s + b1_from_a1*x)**2 - 4*(1)*((-8*b0_s)*x + c2_from_a1*x**2)
disc_a1 = simplify(expand(disc_a1))
print(f"disc = {factor(disc_a1)}")

disc_a1_at_18 = disc_a1.subs(x, Rational(1, 8))
disc_a1_at_18 = simplify(disc_a1_at_18)
print(f"disc(1/8) = {disc_a1_at_18}")

b0_sols_a1 = solve(disc_a1_at_18, b0_s)
print(f"b0 solutions: {b0_sols_a1}")

for b0_val in b0_sols_a1:
    b1_val = b1_from_a1.subs(b0_s, b0_val)
    c1_val = -8*b0_val
    c2_val = c2_from_a1.subs(b0_s, b0_val)

    print(f"\n  b0={b0_val}, b1={b1_val}, a1=0, c1={c1_val}, c2={c2_val}")

    A = S(1)
    B = b0_val + b1_val*x
    C = c1_val*x + c2_val*x**2
    disc_full = B**2 - 4*A*C
    print(f"  disc = {factor(disc_full)}")

    if b0_val > 0:
        Q_expr = (-B + sqrt(disc_full)) / 2
    else:
        Q_expr = (-B - sqrt(disc_full)) / 2

    try:
        Q_series = series(Q_expr, x, 0, 8)
        print(f"  Q(x) = {Q_series}")
        for n in range(1, 8):
            coeff = Q_series.coeff(x, n)
            print(f"    H^{n} = {simplify(coeff)}")
    except Exception as e:
        print(f"  Error: {e}")

# ============================================================
# Step 3: Allow b2 nonzero, use the most general degree-2 disc
# ============================================================

print("\n" + "=" * 60)
print("STEP 3: Most general quadratic fit with degree-2 discriminant")
print("=" * 60)

# Equation: Q^2 + B(x)Q + C(x) = 0  (A=1 for simplicity)
# B = b0 + b1*x, C = c1*x + c2*x^2
# disc = B^2 - 4C = b0^2 + (2*b0*b1-4*c1)*x + (b1^2-4*c2)*x^2
# This is degree 2 automatically.

# From Q = 8x + 36x^2 + 204x^3 + ...:
# Q^2 = 64x^2 + 576x^3 + (2*8*204+36^2)x^4 + ...
#      = 64x^2 + 576x^3 + (3264+1296)x^4 + ...
#      = 64x^2 + 576x^3 + 4560x^4 + ...

# x^1: b0*8 + c1 = 0 => c1 = -8*b0
# x^2: 64 + b0*36 + b1*8 + c2 = 0 => c2 = -64-36*b0-8*b1
# x^3: 576 + b0*204 + b1*36 = 0 => b1 = -(576+204*b0)/36 = -(16+17*b0/3)

# b1 is determined! Only b0 is free.

b0_sym = symbols('b0')
b1_val_gen = -(576 + 204*b0_sym) / 36
c1_val_gen = -8*b0_sym
c2_val_gen = -64 - 36*b0_sym - 8*b1_val_gen

b1_val_gen = simplify(b1_val_gen)
c2_val_gen = simplify(c2_val_gen)

print(f"b1 = {b1_val_gen}")
print(f"c1 = {c1_val_gen}")
print(f"c2 = {c2_val_gen}")

# disc = b0^2 + (2*b0*b1 - 4*c1)*x + (b1^2 - 4*c2)*x^2
disc_gen = b0_sym**2 + (2*b0_sym*b1_val_gen - 4*c1_val_gen)*x + (b1_val_gen**2 - 4*c2_val_gen)*x**2
disc_gen = simplify(expand(disc_gen))
print(f"\ndisc = {factor(disc_gen)}")

# disc(1/8) = 0
disc_at_18 = disc_gen.subs(x, Rational(1, 8))
disc_at_18 = simplify(disc_at_18)
print(f"disc(1/8) = {disc_at_18}")

b0_solutions = solve(disc_at_18, b0_sym)
print(f"b0 solutions: {b0_solutions}")

for b0_v in b0_solutions:
    b1_v = b1_val_gen.subs(b0_sym, b0_v)
    c1_v = c1_val_gen.subs(b0_sym, b0_v)
    c2_v = c2_val_gen.subs(b0_sym, b0_v)

    print(f"\n--- b0 = {b0_v} ---")
    print(f"b1 = {b1_v}, c1 = {c1_v}, c2 = {c2_v}")

    disc_full = b0_v**2 + (2*b0_v*b1_v + 4*8*b0_v)*x + (b1_v**2 - 4*c2_v)*x**2
    disc_full = simplify(expand(disc_full))
    disc_factored = factor(disc_full)
    print(f"disc = {disc_factored}")

    B_poly = b0_v + b1_v*x
    C_poly = c1_v*x + c2_v*x**2

    # Q = (-B ± sqrt(disc)) / 2
    # Choose sign for Q(0) = 0: (-b0 ± |b0|)/2 = 0 requires + if b0>0
    if b0_v > 0:
        Q_expr = (-B_poly + sqrt(disc_full)) / 2
    else:
        Q_expr = (-B_poly - sqrt(disc_full)) / 2

    try:
        Q_ser = series(Q_expr, x, 0, 10)
        print(f"Q(x) = {Q_ser}")
        for n in range(1, 10):
            cn = Q_ser.coeff(x, n)
            cn_simplified = simplify(cn)
            print(f"  H^{n} = {cn_simplified}")
    except Exception as e:
        print(f"  Error computing series: {e}")
