#!/usr/bin/env python3
"""Search for H^4 of sl_3 bar cohomology using multiple constraints.

Known: H^1=8, H^2=36, H^3=204
Constraints:
1. H^4 positive integer, H^4 <= 1744 (Koszul functional equation)
2. Growth rate ~ 8^n (so H^4 ~ 204*8/? ~ 1000-1700)
3. The GF P(t) = 1+8t+36t^2+204t^3+H4*t^4+... should be algebraic
4. The algebra GF f_A(t) = 1/P(-t) should have non-negative integer coefficients

Strategy: For each candidate H4, check if the continued Koszul inversion
gives non-negative integers through several terms (assuming some algebraic
structure for P).
"""

import sys
from fractions import Fraction

# Known bar cohomology (Koszul dual Hilbert series)
h = [1, 8, 36, 204]  # H^0, H^1, H^2, H^3

# Algebra Hilbert series: f_A(t) = 1/P(-t) where P(t) = sum h_n t^n
# Compute algebra coefficients as functions of H4
# P(-t) = 1 - 8t + 36t^2 - 204t^3 + H4*t^4 - ...
# f_A = 1/P(-t) = sum r_n t^n

# Recursion: r_n = -sum_{k=0}^{n-1} r_k * c_{n-k}
# where c_n = (-1)^n * h_n (coefficients of P(-t))

c = [Fraction(1), Fraction(-8), Fraction(36), Fraction(-204)]

r = [Fraction(0)] * 10
r[0] = Fraction(1)
for n in range(1, 4):
    s = Fraction(0)
    for k in range(n):
        s += r[k] * c[n-k]
    r[n] = -s

print("Algebra series (first 4 terms, exact):")
for n in range(4):
    print(f"  r_{n} = {r[n]}")

# r_4 = 1744 - H4 (from the convolution)
print(f"\nr_4 = 1744 - H4")

# For H4 in a range, check if r_5, r_6, ... can all be non-negative integers.
# r_5 = f(H4, H5): r_5 = H5 - 16*H4 + 14624
# For r_5 >= 0: H5 >= 16*H4 - 14624

# But we don't know H5. What we CAN check: for a given H4, does there EXIST
# a valid sequence H5, H6, ... such that all r_n >= 0?

# A stronger constraint: the GF P(t) is algebraic of degree 2.
# If P satisfies a(t)*P^2 + b(t)*P + c(t) = 0 with polynomial coefficients,
# then once we fix a,b,c (from fitting 4+ data points), ALL subsequent H_n
# are determined.

# With 4 data points (H0=1, H1=8, H2=36, H3=204), we can fit a quadratic
# equation with certain polynomial degrees and then check if H4, H5, ... are
# non-negative integers with valid Koszul inversions.

# For the GENERAL quadratic: a(t)*P^2 + b(t)*P + c(t) = 0
# Normalize: c(t) = 1, b(0) = -1 (from P(0)=1).
# With various degrees for a and b:

from sympy import symbols, Rational, sqrt, series, solve, expand, factor, simplify

t = symbols('t')

# Try: a = alpha*t, b = -1 + beta*t, c = 1.
# 2 unknowns (alpha, beta). 3 constraints (t^1, t^2, t^3).
# Over-determined! Let me check.
# t^1: alpha + beta = 8  (1 equation)
# t^2: 16*alpha + 8*beta = 36  (use Q^2 coeff of t^1 = 16, Q coeff of t^1 = 8)
# Wait, let me redo this carefully.

# P = 1 + 8t + 36t^2 + 204t^3 + H4 t^4 + ...
# P^2 = 1 + 16t + 136t^2 + 984t^3 + ...

# a(t)*P^2 + b(t)*P + 1 = 0
# With a = alpha*t, b = -1+beta*t:

# t^0: -1 + 1 = 0 OK
# t^1: alpha*1 - 8 + beta*1 = 0 => alpha + beta = 8
# t^2: alpha*16 - 36 + beta*8 = 0 => 16*alpha + 8*beta = 36
# t^3: alpha*136 - 204 + beta*36 = 0 => 136*alpha + 36*beta = 204

# From t^1: beta = 8 - alpha
# t^2: 16*alpha + 8*(8-alpha) = 36 => 8*alpha + 64 = 36 => 8*alpha = -28 => alpha = -7/2
# t^3: 136*(-7/2) + 36*(8+7/2) = -476 + 36*23/2 = -476 + 414 = -62 ≠ 204

# INCONSISTENT with 2 unknowns and 3 equations. Need more parameters.

# a = alpha*t + gamma*t^2, b = -1 + beta*t, c = 1.
# 3 unknowns. 3 equations.
# t^1: alpha + beta = 8
# t^2: 16*alpha + gamma + 8*beta = 36
# t^3: 136*alpha + 16*gamma + 36*beta = 204

# From t^1: beta = 8 - alpha
# t^2: 16*alpha + gamma + 8*(8-alpha) = 36 => 8*alpha + gamma = -28 => gamma = -28-8*alpha
# t^3: 136*alpha + 16*(-28-8*alpha) + 36*(8-alpha) = 204
#   => 136*alpha - 448 - 128*alpha + 288 - 36*alpha = 204
#   => -28*alpha - 160 = 204 => alpha = -364/28 = -13

alpha_val = Rational(-13)
beta_val = 8 - alpha_val  # = 21
gamma_val = -28 - 8*alpha_val  # = -28+104 = 76

print(f"\n=== Ansatz: ({alpha_val}*t + {gamma_val}*t^2)*P^2 + (-1+{beta_val}*t)*P + 1 = 0 ===")

# Predict H4:
# t^4: alpha*P2[3] + gamma*P2[2] - H4 + beta*204 = 0
# P2[3] = 984, P2[2] = 136
H4_pred = alpha_val*984 + gamma_val*136 - beta_val*204
# Wait: t^4 of a*P^2 + b*P + 1:
# From a*P^2: alpha*(P^2 coeff of t^3) + gamma*(P^2 coeff of t^2)
# = alpha*984 + gamma*136
# From b*P: -H4 + beta*(P coeff of t^3) = -H4 + beta*204
# From c: 0
# Total: alpha*984 + gamma*136 - H4 + beta*204 = 0

H4_pred = alpha_val*984 + gamma_val*136 + beta_val*204
print(f"H4 = {alpha_val}*984 + {gamma_val}*136 + {beta_val}*204 = {H4_pred}")

# Check Koszul: r4 = 1744 - H4
r4_val = 1744 - H4_pred
print(f"r4 (algebra coeff) = {r4_val}")

# Compute more H values from the equation
# H_n = alpha*(P^2)_{n-1} + gamma*(P^2)_{n-2} + beta*H_{n-1}
h_extended = list(h) + [H4_pred]
h2 = [0]*20  # P^2 coefficients
for i in range(len(h_extended)):
    for j in range(len(h_extended)):
        if i+j < 20:
            h2[i+j] += h_extended[i]*h_extended[j]

for n in range(5, 12):
    # Need P^2 coefficients, which depend on previous H values
    # Recompute P^2 up to degree n-1
    h2_n_minus_1 = sum(h_extended[i]*h_extended[n-1-i] for i in range(min(n, len(h_extended))) if n-1-i >= 0 and n-1-i < len(h_extended))
    h2_n_minus_2 = sum(h_extended[i]*h_extended[n-2-i] for i in range(min(n-1, len(h_extended))) if n-2-i >= 0 and n-2-i < len(h_extended))

    h_n = alpha_val * h2_n_minus_1 + gamma_val * h2_n_minus_2 + beta_val * h_extended[n-1]
    h_extended.append(h_n)
    print(f"H_{n} = {h_n}")

# Compute algebra series
print(f"\nAlgebra Hilbert series:")
c_ext = [(-1)**n * h_extended[n] for n in range(len(h_extended))]
r_ext = [Fraction(0)] * len(h_extended)
r_ext[0] = Fraction(1)
for n in range(1, len(h_extended)):
    s = Fraction(0)
    for k in range(n):
        if n-k < len(c_ext):
            s += r_ext[k] * c_ext[n-k]
    r_ext[n] = -s
    if n <= 10:
        print(f"  r_{n} = {r_ext[n]}")

# Check all non-negative?
all_nonneg = all(r_ext[n] >= 0 for n in range(len(r_ext)))
print(f"\nAll algebra coefficients non-negative? {all_nonneg}")
if not all_nonneg:
    for n in range(len(r_ext)):
        if r_ext[n] < 0:
            print(f"  NEGATIVE at n={n}: r_{n} = {r_ext[n]}")
            break

# Check discriminant
a_poly = alpha_val*t + gamma_val*t**2
b_poly = -1 + beta_val*t
disc = b_poly**2 - 4*a_poly
disc_exp = expand(disc)
disc_fac = factor(disc_exp)
print(f"\nDiscriminant = {disc_fac}")

# Roots of discriminant
from sympy import Poly as SPoly
disc_roots = solve(disc_exp, t)
print(f"Discriminant roots: {disc_roots}")
for r in disc_roots:
    print(f"  root = {r}, 1/root = {simplify(1/r)}, float ≈ {float(r.evalf()):.6f}")

# Series expansion of P from the equation
P_formula = (-b_poly - sqrt(disc_exp)) / (2*a_poly)
P_series = series(P_formula, t, 0, 12)
print(f"\nP series (- branch):")
for n in range(10):
    cn = P_series.coeff(t, n)
    print(f"  t^{n}: {cn}")

P_formula2 = (-b_poly + sqrt(disc_exp)) / (2*a_poly)
P_series2 = series(P_formula2, t, 0, 12)
print(f"\nP series (+ branch):")
for n in range(10):
    cn = P_series2.coeff(t, n)
    print(f"  t^{n}: {cn}")

# Now try for sl_2 to validate
print("\n" + "="*60)
print("VALIDATION: sl_2")
print("="*60)

# sl_2: H = 1, 3, 6, 15, 36, 91, ...
# Same ansatz: (a1*t+a2*t^2)*P^2 + (-1+b1*t)*P + 1 = 0
# t^1: a1+b1=3, t^2: 6a1+a2+3b1=6, t^3: 30a1+6a2+6b1=15
# From t^1: b1=3-a1
# t^2: 6a1+a2+3(3-a1)=6 => 3a1+a2=-3 => a2=-3-3a1
# t^3: 30a1+6(-3-3a1)+6(3-a1) = 15 => 30a1-18-18a1+18-6a1=15 => 6a1=15 => a1=5/2

a1_sl2 = Rational(5,2)
b1_sl2 = 3 - a1_sl2  # = 1/2
a2_sl2 = -3 - 3*a1_sl2  # = -21/2

print(f"sl_2: a1={a1_sl2}, a2={a2_sl2}, b1={b1_sl2}")

# Predict H4 for sl_2
h_sl2 = [1, 3, 6, 15]
h2_sl2 = [0]*10
for i in range(4):
    for j in range(4):
        if i+j < 10:
            h2_sl2[i+j] += h_sl2[i]*h_sl2[j]

H4_sl2 = a1_sl2*h2_sl2[3] + a2_sl2*h2_sl2[2] + b1_sl2*h_sl2[3]
print(f"H4 (sl_2) = {H4_sl2} (expected 36)")

# The sl_2 equation gives H4 = 36 if the ansatz works
if H4_sl2 == 36:
    print("MATCH! sl_2 ansatz gives correct H4.")
else:
    print(f"MISMATCH: got {H4_sl2}, expected 36")

    # The "correct" sl_2 equation is t(1+t)P^2 - (1+t)P + 1 = 0
    # = (t+t^2)P^2 + (-1-t)P + 1 = 0
    # So a1=1, a2=1, b1=-1.
    # Check: t^1: 1+(-1)=0 ≠ 3. WRONG!
    # The sl_2 P(t) = 1+3t+6t^2+15t^3+... is NOT the Riordan R(x).
    # R(x) = 1+0x+x^2+x^3+3x^4+6x^5+... is the Riordan GF.
    # P(t) = sum_{n>=0} R(n+3) t^n is the SHIFTED version.
    # P does NOT satisfy the Riordan equation directly.
    print("\nNote: P(t) is the SHIFTED Riordan GF, not R(x) itself.")
    print("The Riordan equation t(1+t)R^2-(1+t)R+1=0 applies to R, not P.")

# For sl_2, the correct H4 in our shifted GF is 36 = R(7).
# Our ansatz with a1=5/2 gives:
h2_sl2_3 = 2*1*15 + 2*3*6  # = 30+36 = 66
h2_sl2_2 = 2*1*6 + 3*3     # = 12+9 = 21
H4_check = Rational(5,2)*66 + Rational(-21,2)*21 + Rational(1,2)*15
print(f"H4 check = (5/2)*66 + (-21/2)*21 + (1/2)*15 = {H4_check}")

# Let me also try the FACTORED form for sl_3
# For sl_2, the equation t(1+t)R^2-(1+t)R+1=0 has disc = (1+t)(1-3t).
# Root at 1/3 = 1/d.
# For the shifted P: different equation, but disc should still have root at 1/d.

# For sl_3: disc of our ansatz = (-1+21t)^2 - 4(-13t+76t^2)
# = 1-42t+441t^2+52t-304t^2 = 1+10t+137t^2
# Wait, that's not right. Let me compute.
# Actually disc = b^2 - 4ac = (-1+21t)^2 - 4*(-13t+76t^2)*1
# = 1-42t+441t^2 + 52t - 304t^2
# = 1 + 10t + 137t^2

print("\n" + "="*60)
print("CHECKING DISCRIMINANT ROOT AT 1/8")
print("="*60)
disc_val = 1 + 10*Rational(1,8) + 137*Rational(1,64)
print(f"disc(1/8) = 1 + 10/8 + 137/64 = {disc_val}")
print(f"          = {float(disc_val)}")

# disc(1/8) = 1 + 5/4 + 137/64 = 64/64 + 80/64 + 137/64 = 281/64 ≠ 0.
# The discriminant does NOT vanish at 1/8!
# So the radius of convergence is determined by the disc roots, not 1/8.

# Maybe this ansatz gives a DIFFERENT radius of convergence.
# If growth rate is indeed 8^n, disc must have a root at 1/8.
# This ansatz DOESN'T, so either:
# (a) the growth rate isn't 8^n for this equation, or
# (b) the ansatz needs more terms.

# Let's check: what is the actual radius?
# disc = 137t^2 + 10t + 1
# Roots: t = (-10 ± sqrt(100-548))/274 = (-10 ± sqrt(-448))/274
# Complex! So the discriminant has NO real roots.
# This means P(t) = (-b-sqrt(disc))/(2a) is defined for all real t.
# The singularity of P comes from a(t) = 0, i.e., t(-13+76t)=0 -> t=0 or t=13/76.
# t=13/76 ≈ 0.171. And 1/8 = 0.125.
# Since 13/76 > 1/8, the radius from a(t)=0 is 13/76, not 1/8.

print(f"\na(t)=0 roots: t=0, t=13/76 ≈ {13/76:.4f}")
print(f"1/8 = {1/8:.4f}")
print(f"Radius of convergence = 13/76 (from pole of P)")
print(f"Growth rate ≈ 76/13 ≈ {76/13:.2f} (NOT 8!)")
print(f"\nThis means H_n grows like (76/13)^n ≈ 5.85^n, not 8^n.")
print("So this equation gives the WRONG growth rate.")

# Need growth rate 8^n => radius = 1/8.
# This requires either disc root or a(t) root at 1/8.
# With a = alpha*t+gamma*t^2: a(1/8) = alpha/8 + gamma/64 = -13/8 + 76/64 = -13/8 + 19/16
# = -26/16 + 19/16 = -7/16 ≠ 0.

# If we REQUIRE a(1/8)=0: alpha/8 + gamma/64 = 0 => gamma = -8*alpha.
# With this constraint: gamma = -8*alpha.
# Then from the equations:
# gamma = -28-8*alpha and gamma = -8*alpha => -28-8*alpha = -8*alpha => -28 = 0. CONTRADICTION!

# So with this 3-param ansatz, we CANNOT have a(1/8)=0 and match the data.
# We need more parameters.

print("\n" + "="*60)
print("4-PARAM ANSATZ: (a1*t+a2*t^2)*P^2 + (-1+b1*t+b2*t^2)*P + 1 = 0")
print("="*60)

# 4 unknowns (a1,a2,b1,b2), 3 equations from matching t^1,t^2,t^3.
# 1 free parameter. Use the extra freedom to impose radius = 1/8.

# Equations:
# t^1: a1+b1 = 8
# t^2: 16*a1+a2+8*b1+b2 = 36
# t^3: 136*a1+16*a2+36*b1+8*b2 = 204

# Free param: let b2 be free.
# a1+b1=8 => b1=8-a1
# 16a1+a2+8(8-a1)+b2=36 => 8a1+a2+b2=-28 => a2=-28-8a1-b2
# 136a1+16(-28-8a1-b2)+36(8-a1)+8b2 = 204
# => 136a1-448-128a1-16b2+288-36a1+8b2 = 204
# => -28a1-8b2-160 = 204 => -28a1-8b2 = 364 => 7a1+2b2=-91 => a1=(-91-2b2)/7

# H4 = a1*(P^2)_3 + a2*(P^2)_2 + b1*H3 + b2*H2
# = a1*984 + a2*136 + b1*204 + b2*36

# Substitute:
# a1 = (-91-2b2)/7
# b1 = 8-a1 = 8+(91+2b2)/7 = (56+91+2b2)/7 = (147+2b2)/7
# a2 = -28-8a1-b2 = -28-8(-91-2b2)/7-b2 = -28+(728+16b2)/7-b2
#    = (-196+728+16b2-7b2)/7 = (532+9b2)/7

# H4 = [(-91-2b2)/7]*984 + [(532+9b2)/7]*136 + [(147+2b2)/7]*204 + b2*36
# = [984(-91-2b2) + 136(532+9b2) + 204(147+2b2)] / 7 + 36*b2
# Numerator: -89544-1968b2 + 72352+1224b2 + 29988+408b2
# = (-89544+72352+29988) + (-1968+1224+408)b2
# = 12796 + (-336)b2
# H4 = (12796-336b2)/7 + 36b2 = 12796/7 - 336b2/7 + 36b2
# = 12796/7 + (-336+252)b2/7 = 12796/7 - 84b2/7
# = (12796 - 84*b2)/7

# For H4 to be integer: 12796-84b2 ≡ 0 (mod 7)
# 12796 mod 7: 12796/7 = 1828 exact! So 12796 = 7*1828.
# 84 mod 7 = 0. So 12796-84b2 is always divisible by 7!
# H4 = 1828 - 12*b2

print("H4 = 1828 - 12*b2  (b2 is free parameter)")

# Now require disc root at t=1/8 OR a(t) root at t=1/8.

# Discriminant: d(t) = (-1+b1*t+b2*t^2)^2 - 4*(a1*t+a2*t^2)
# Require d(1/8) = 0 for disc root:
# d(1/8) = (-1+b1/8+b2/64)^2 - 4*(a1/8+a2/64)

# Substitute parametric expressions in b2:
# b1 = (147+2*b2)/7, a1 = (-91-2*b2)/7, a2 = (532+9*b2)/7

# -1+b1/8+b2/64 = -1 + (147+2b2)/(7*8) + b2/64
# = -1 + (147+2b2)/56 + b2/64
# Common denom = 448:
# = (-448 + 8(147+2b2) + 7b2)/448
# = (-448 + 1176 + 16b2 + 7b2)/448
# = (728 + 23b2)/448

# a1/8+a2/64 = (-91-2b2)/(7*8) + (532+9b2)/(7*64)
# = (-91-2b2)/56 + (532+9b2)/448
# = (8(-91-2b2) + 532+9b2)/448
# = (-728-16b2+532+9b2)/448
# = (-196-7b2)/448

# d(1/8) = [(728+23b2)/448]^2 - 4*(-196-7b2)/448
# = (728+23b2)^2/448^2 + 4*(196+7b2)/448
# = [(728+23b2)^2 + 4*448*(196+7b2)] / 448^2

# Numerator: (728+23b2)^2 + 1792*(196+7b2)
# = 529984 + 33488b2 + 529b2^2 + 351232 + 12544b2
# = 529b2^2 + 46032b2 + 881216

# Set = 0:
# 529b2^2 + 46032b2 + 881216 = 0
# Discriminant: 46032^2 - 4*529*881216

D_b2 = 46032**2 - 4*529*881216
print(f"\nDiscriminant of b2 equation: {D_b2}")

import math
if D_b2 >= 0:
    sd = math.isqrt(D_b2)
    print(f"sqrt(D) ≈ {math.sqrt(D_b2):.4f}, isqrt = {sd}, check: {sd*sd == D_b2}")
    if sd*sd != D_b2:
        print("Not a perfect square — b2 is irrational from disc constraint alone.")

# Also try: a(1/8) = 0
# a1/8 + a2/64 = 0 => a2 = -8*a1
# But a2 = (532+9b2)/7 and a1 = (-91-2b2)/7
# a2 = -8*a1 => (532+9b2)/7 = -8*(-91-2b2)/7 = (728+16b2)/7
# => 532+9b2 = 728+16b2 => -7b2 = 196 => b2 = -28

b2_pole = -28
H4_pole = 1828 - 12*b2_pole
print(f"\n=== If a(1/8)=0: b2 = {b2_pole}, H4 = {H4_pole} ===")

# Check parameters
a1_p = (-91-2*b2_pole)/7
b1_p = (147+2*b2_pole)/7
a2_p = (532+9*b2_pole)/7

print(f"a1={Rational(-91-2*b2_pole,7)}, a2={Rational(532+9*b2_pole,7)}, b1={Rational(147+2*b2_pole,7)}, b2={b2_pole}")

# Verify a(1/8)=0
a_at_eighth = a1_p/8 + a2_p/64
print(f"a(1/8) = {a_at_eighth}")

# Algebra coefficient r4
r4_pole = 1744 - H4_pole
print(f"r4 = {r4_pole}")
if r4_pole >= 0:
    print("r4 >= 0: OK")
else:
    print("r4 < 0: VIOLATES KOSZUL CONSTRAINT")

# Compute full series
h_ext = [1, 8, 36, 204, H4_pole]
h2_ext = [0]*20
for i in range(5):
    for j in range(5):
        if i+j < 20:
            h2_ext[i+j] += h_ext[i]*h_ext[j]

for n in range(5, 12):
    h2_n1 = sum(h_ext[i]*h_ext[n-1-i] for i in range(len(h_ext)) if 0 <= n-1-i < len(h_ext))
    h2_n2 = sum(h_ext[i]*h_ext[n-2-i] for i in range(len(h_ext)) if 0 <= n-2-i < len(h_ext))
    h_n = Rational(a1_p)*h2_n1 + Rational(a2_p)*h2_n2 + Rational(b1_p)*h_ext[n-1] + Rational(b2_pole)*h_ext[n-2]
    h_ext.append(int(h_n))
    print(f"  H_{n} = {int(h_n)}")

# Check algebra series
print(f"\nAlgebra Hilbert series:")
c_ext2 = [(-1)**n * h_ext[n] for n in range(len(h_ext))]
r_ext2 = [0] * len(h_ext)
r_ext2[0] = 1
for n in range(1, min(12, len(h_ext))):
    s = 0
    for k in range(n):
        if n-k < len(c_ext2):
            s += r_ext2[k] * c_ext2[n-k]
    r_ext2[n] = -s
    print(f"  r_{n} = {r_ext2[n]}")

all_nn = all(r_ext2[n] >= 0 for n in range(min(12, len(h_ext))))
print(f"\nAll non-negative? {all_nn}")

# Growth rate check
print(f"\nGrowth rates H_n/H_{{n-1}}:")
for n in range(1, min(10, len(h_ext))):
    if h_ext[n-1] != 0:
        print(f"  H_{n}/H_{n-1} = {h_ext[n]}/{h_ext[n-1]} = {h_ext[n]/h_ext[n-1]:.4f}")

# Discriminant and its factorization
a_poly2 = Rational(a1_p)*t + Rational(a2_p)*t**2
b_poly2 = -1 + Rational(b1_p)*t + Rational(b2_pole)*t**2
disc2 = expand(b_poly2**2 - 4*a_poly2)
print(f"\nDiscriminant = {factor(disc2)}")
disc_roots2 = solve(disc2, t)
print(f"Disc roots: {disc_roots2}")
for r in disc_roots2:
    print(f"  root = {r} ≈ {float(r.evalf()):.6f}")
