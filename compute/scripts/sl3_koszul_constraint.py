#!/usr/bin/env python3
"""Use the Koszul functional equation to constrain sl_3 H^4.

For a Koszul algebra: f_{A!}(t) * f_A(-t) = 1.
f_{A!}(t) = Q(t) = 1 + 8t + 36t^2 + 204t^3 + H4*t^4 + ...
f_A(t) = 1/Q(-t) must have NON-NEGATIVE INTEGER coefficients.

This gives: r_4 = 1744 - H4 >= 0, so H4 <= 1744.
Further: r_5 = H5 - 16*H4 + 14624 >= 0, etc.

Also: the phi-ansatz t*phi*Q^2 - phi*Q + 1 = 0 with cubic phi gave H4=1797 > 1744.
So that ansatz is WRONG. Need a better approach.

Strategy: compute the Koszul dual Hilbert series CORRECTLY using OS algebra multiplication.
"""

from sympy import Rational, symbols

# First: verify the Koszul constraint numerically
print("=" * 60)
print("KOSZUL FUNCTIONAL EQUATION CONSTRAINTS")
print("=" * 60)

# Known: Q = 1, 8, 36, 204, H4, H5, ...
q = [1, -8, 36, -204]  # coefficients of Q(-t)

# r_n from R(t) = 1/Q(-t), so R * Q(-t) = 1
# sum_{k=0}^n r_k * q_{n-k}(-1)^{n-k} = delta_{n,0}
# where Q(-t) has coeffs q_n = (-1)^n * H_n

# Actually Q(-t) = 1 - 8t + 36t^2 - 204t^3 + H4*t^4 - ...
# So the coeffs of Q(-t) are: c_0=1, c_1=-8, c_2=36, c_3=-204, c_4=H4
# And R * (Q composed with -t) = 1

# Convolution: sum_{k=0}^n r_k * c_{n-k} = delta_{n0}
c = [1, -8, 36, -204]  # c_n = (-1)^n * H_n

r = [0] * 10
r[0] = 1
for n in range(1, 6):
    s = 0
    for k in range(n):
        if n - k < len(c):
            s += r[k] * c[n - k]
        else:
            break
    r[n] = -s
    print(f"r_{n} = {r[n]}")

print(f"\nAlgebra Hilbert series (first 4 terms): {r[:4]}")
print(f"r_4 = 1744 - H4")
print(f"Constraint: H4 <= 1744")

# For sl_2 verification:
print("\n" + "=" * 60)
print("VERIFICATION: sl_2 algebra Hilbert series")
print("=" * 60)

c2 = [1, -3, 6, -15, 36, -91, 232, -603]
r2 = [0] * 10
r2[0] = 1
for n in range(1, 8):
    s = 0
    for k in range(n):
        if n - k < len(c2):
            s += r2[k] * c2[n - k]
    r2[n] = -s
    print(f"r_{n} = {r2[n]}")

print(f"sl_2 algebra series: {r2[:8]}")
print("All non-negative?", all(x >= 0 for x in r2[:8]))

# Now: what value of H4 makes the sl_3 algebra series "nice"?
print("\n" + "=" * 60)
print("SCANNING H4 VALUES")
print("=" * 60)

# For each candidate H4, compute r_4 and check
# Also need to check that future r_n can be non-negative

# With c = [1, -8, 36, -204, H4, -H5, ...]
# r_4 = 1744 - H4
# r_5 = -8*r_4 + 36*r_3 - 204*r_2 + H4*r_1 - H5
#      = -8*(1744-H4) + 36*140 - 204*28 + 8*H4 - H5
#      = -13952+8H4 + 5040 - 5712 + 8H4 - H5
#      = 16H4 - 14624 - H5
# For r_5 >= 0: H5 <= 16H4 - 14624

# Let me try specific values and see if a pattern emerges.
# The phi-ansatz with different phi forms:

# Approach: compute H4 from different algebraic ansatzes and check Koszul constraint.

# 1. Phi ansatz with DIFFERENT structural forms
# For sl_2: Q satisfies x(1+x)Q^2 - (1+x)Q + 1 = 0
# This has discriminant (1+x)(1-3x). The (1+x) factor = phi(x).
# The disc root at x=-1 and x=1/3.

# For sl_3: if disc = (1+alpha*t)(1-8t), then the equation is:
# t*(1+alpha*t)*Q^2 - (1+alpha*t)*Q + 1 = 0
# But this is the phi ansatz, which gave bad results.

# Alternative: maybe the equation is NOT of the form t*phi*Q^2 - phi*Q + 1 = 0.
# Maybe it's: a(t)*Q^2 + b(t)*Q + c(t) = 0 with a more general structure.

# Let me try: for sl_2, Q = P_sl2 = 1 + x + 3x^2 + ... WAIT
# From the previous script, P_sl2 = (1-sqrt((1-3x)/(1+x)))/(2x) starts with
# 1, 1, 2, 5, 14, 42, ... which are CATALAN numbers!
# No: sl_2 bar cohomology is 1, 3, 6, 15, 36, 91 (Riordan R(n+3)).

# The phi-ansatz Q = (1-sqrt(1-4t/phi))/(2t) for phi=1+t gives:
# Q = 1, 0, 1, 1, 3, 6, 15 which is Riordan starting from R(0).
# The bar cohomology 1, 3, 6, 15, 36, 91 is shifted: it's R(3), R(4), R(5), ...

# So the phi ansatz generates the FULL Riordan sequence, and we want a
# SHIFTED version. The structural equation for the shifted sequence is different!

# For sl_2, let F(t) = sum_{n>=0} R(n+3) t^n = 1 + 3t + 6t^2 + 15t^3 + ...
# From sl3_bar_from_riordan.py, F satisfies:
# x^7(x+1)F^2 + x^3(x+1)(2x^3+2x-1)F + x^3(x^3+x^2+2x+1) = 0
# (after clearing denominators from the substitution R = 1 + x^2 + x^3*F)

# This is much more complex. The shifted GF doesn't satisfy a simple equation.

# KEY INSIGHT: Maybe the sl_3 bar cohomology is NOT a shifted version of a
# Riordan-like sequence. Maybe it satisfies a DIFFERENT algebraic equation
# directly (without being extracted from a larger sequence).

# Let me try a DIRECT fit: Q = 1 + 8t + 36t^2 + 204t^3 + H4 t^4
# satisfies p(t)Q^2 + q(t)Q + r(t) = 0 where p,q,r are polynomials.

# For this to have a solution, we need the polynomial coefficients to
# satisfy linear constraints from matching each power of t.

# With deg(p)=d_p, deg(q)=d_q, deg(r)=d_r, we get constraints up to
# t^(max(d_p+2*deg_Q, d_q+deg_Q, d_r)).

# The number of free parameters = (d_p+1) + (d_q+1) + (d_r+1).
# The number of constraints = number of t-powers we match.

# For the equation to be nontrivial and determine H4, we need enough
# parameters to match through t^3, and then t^4 gives H4.

# Let me try p = t*(p0+p1*t), q = -(1+q1*t+q2*t^2), r = 1.
# This is 4 parameters (p0,p1,q1,q2) and we match t^0 through t^3.

print("\n" + "=" * 60)
print("GENERAL QUADRATIC: t*(p0+p1*t)*Q^2 - (1+q1*t+q2*t^2)*Q + 1 = 0")
print("=" * 60)

# Q = 1 + 8t + 36t^2 + 204t^3 + H4*t^4
# Q^2 = 1 + 16t + 136t^2 + 984t^3 + (2*H4+2*8*204+36^2)t^4 + ...
#      = 1 + 16t + 136t^2 + 984t^3 + (2*H4+3264+1296)t^4 + ...
#      = 1 + 16t + 136t^2 + 984t^3 + (2*H4+4560)t^4 + ...

# t*Q^2 = t + 16t^2 + 136t^3 + 984t^4 + ...
# t^2*Q^2 = t^2 + 16t^3 + 136t^4 + ...

# Equation: t*(p0+p1*t)*Q^2 - (1+q1*t+q2*t^2)*Q + 1 = 0
# = p0*(t*Q^2) + p1*(t^2*Q^2) - Q - q1*(t*Q) - q2*(t^2*Q) + 1

# t*Q = t + 8t^2 + 36t^3 + 204t^4 + ...
# t^2*Q = t^2 + 8t^3 + 36t^4 + ...

# Coefficients:
# t^0: -1 + 1 = 0 ✓
# t^1: p0*1 - 8 - q1*1 = 0 → p0 - q1 = 8
# t^2: p0*16 + p1*1 - 36 - q1*8 - q2*1 = 0 → 16p0 + p1 - 8q1 - q2 = 36
# t^3: p0*136 + p1*16 - 204 - q1*36 - q2*8 = 0 → 136p0 + 16p1 - 36q1 - 8q2 = 204

# 3 equations, 4 unknowns. One free parameter.
# Let q2 be free.

# Eq1: p0 = 8 + q1
# Eq2: 16(8+q1) + p1 - 8q1 - q2 = 36 → 128 + 16q1 + p1 - 8q1 - q2 = 36
#      → p1 + 8q1 - q2 = -92 → p1 = -92 - 8q1 + q2
# Eq3: 136(8+q1) + 16(-92-8q1+q2) - 36q1 - 8q2 = 204
#      → 1088 + 136q1 - 1472 - 128q1 + 16q2 - 36q1 - 8q2 = 204
#      → -384 - 28q1 + 8q2 = 204
#      → -28q1 + 8q2 = 588
#      → -7q1 + 2q2 = 147
#      → q1 = (2q2 - 147)/7

from fractions import Fraction

# For q1 to be rational with denominator dividing 7
# q2 free. Let's parametrize by q2.
# q1 = (2*q2 - 147)/7
# p0 = 8 + q1 = 8 + (2*q2-147)/7 = (56+2*q2-147)/7 = (2*q2-91)/7
# p1 = -92 - 8*(2*q2-147)/7 + q2 = -92 + (-16*q2+1176)/7 + q2
#    = (-644 - 16*q2 + 1176 + 7*q2)/7 = (532 - 9*q2)/7

# t^4 coefficient gives H4:
# p0*984 + p1*136 - H4 - q1*204 - q2*36 = 0
# H4 = p0*984 + p1*136 - q1*204 - q2*36

# Substitute:
# H4 = [(2q2-91)/7]*984 + [(532-9q2)/7]*136 - [(2q2-147)/7]*204 - q2*36
# = [984(2q2-91) + 136(532-9q2) - 204(2q2-147)] / 7 - 36*q2
# Numerator of fraction:
# = 1968q2 - 89544 + 72352 - 1224q2 - 408q2 + 29988
# = (1968-1224-408)q2 + (-89544+72352+29988)
# = 336*q2 + 12796
# H4 = (336*q2 + 12796)/7 - 36*q2
# = 48*q2 + 1828 - 36*q2
# = 12*q2 + 1828

print("H4 = 12*q2 + 1828  (where q2 is a free parameter)")
print()

# Now use discriminant constraint: disc root at t=1/8
# disc = (1+q1*t+q2*t^2)^2 - 4*t*(p0+p1*t)
# Need disc(1/8) = 0

# disc(1/8) = (1 + q1/8 + q2/64)^2 - 4*(p0/8 + p1/64)
# = (1 + q1/8 + q2/64)^2 - p0/2 - p1/16

# Substitute parametric expressions:
# q1 = (2q2-147)/7, p0 = (2q2-91)/7, p1 = (532-9q2)/7

# 1 + q1/8 + q2/64 = 1 + (2q2-147)/56 + q2/64
# = 1 + (2q2-147)/56 + q2/64
# Common denom = 448:
# = 448/448 + 8(2q2-147)/448 + 7q2/448
# = (448 + 16q2 - 1176 + 7q2)/448
# = (23q2 - 728)/448

# p0/2 = (2q2-91)/14
# p1/16 = (532-9q2)/112

# disc(1/8) = [(23q2-728)/448]^2 - (2q2-91)/14 - (532-9q2)/112

# [(23q2-728)/448]^2 = (23q2-728)^2/200704

# (2q2-91)/14 = (2q2-91)*14336/200704 = (2q2-91)*14336/200704
# Actually let me use common denom 200704 = 448^2.
# (2q2-91)/14 = (2q2-91)*14336/200704
# (532-9q2)/112 = (532-9q2)*1792/200704

# disc(1/8) = [(23q2-728)^2 - 14336(2q2-91) - 1792(532-9q2)] / 200704

num = lambda q2v: (23*q2v-728)**2 - 14336*(2*q2v-91) - 1792*(532-9*q2v)

# Expand:
# (23q2-728)^2 = 529*q2^2 - 33488*q2 + 529984
# -14336*(2q2-91) = -28672*q2 + 1304576
# -1792*(532-9q2) = -953344 + 16128*q2

# Sum: 529*q2^2 + (-33488-28672+16128)*q2 + (529984+1304576-953344)
# = 529*q2^2 - 46032*q2 + 881216

# Set = 0:
# 529*q2^2 - 46032*q2 + 881216 = 0

# Discriminant of this quadratic in q2:
D = 46032**2 - 4*529*881216
print(f"Discriminant of q2 equation: {D}")

import math
if D >= 0:
    sqrt_D = math.isqrt(D)
    print(f"sqrt(D) = {sqrt_D}, check: {sqrt_D**2} == {D}? {sqrt_D**2 == D}")
    if sqrt_D**2 == D:
        q2_1 = (46032 + sqrt_D) / (2*529)
        q2_2 = (46032 - sqrt_D) / (2*529)
        print(f"q2 = {q2_1} or {q2_2}")

        for q2v in [q2_1, q2_2]:
            H4v = 12*q2v + 1828
            q1v = (2*q2v - 147)/7
            p0v = (2*q2v - 91)/7
            p1v = (532 - 9*q2v)/7
            print(f"\n  q2={q2v:.6f}: H4={H4v:.6f}")
            print(f"    p0={p0v:.6f}, p1={p1v:.6f}, q1={q1v:.6f}")

            # Check r4 = 1744 - H4
            r4 = 1744 - H4v
            print(f"    r4 (algebra) = {r4:.6f} {'OK' if r4 >= 0 else 'NEGATIVE!'}")

            # Verify: does this equation reproduce the known coefficients?
            # t*(p0+p1*t)*Q^2 - (1+q1*t+q2*t^2)*Q + 1 = 0
            Q_coeffs = [1, 8, 36, 204, H4v]
            Q2_coeffs = [0]*10
            for i in range(5):
                for j in range(5):
                    if i+j < 10:
                        Q2_coeffs[i+j] += Q_coeffs[i]*Q_coeffs[j]

            for n in range(5):
                # Coefficient of t^n in the equation
                val = 0
                # t*(p0+p1*t)*Q^2 part:
                if n >= 1:
                    val += p0v * Q2_coeffs[n-1]
                if n >= 2:
                    val += p1v * Q2_coeffs[n-2]
                # -(1+q1*t+q2*t^2)*Q part:
                val -= Q_coeffs[n]
                if n >= 1:
                    val -= q1v * Q_coeffs[n-1]
                if n >= 2:
                    val -= q2v * Q_coeffs[n-2]
                # +1 part:
                if n == 0:
                    val += 1
                print(f"    eq[t^{n}] = {val:.10f}")
    else:
        print("D is not a perfect square — q2 is irrational")
        sqrt_D_approx = math.sqrt(D)
        q2_1 = (46032 + sqrt_D_approx) / (2*529)
        q2_2 = (46032 - sqrt_D_approx) / (2*529)
        print(f"q2 ≈ {q2_1:.6f} or {q2_2:.6f}")
        for q2v in [q2_1, q2_2]:
            H4v = 12*q2v + 1828
            print(f"  q2={q2v:.6f}: H4={H4v:.6f}, r4={1744-H4v:.6f}")
else:
    print("D < 0 — no real solutions!")

# Also check: is H4 = 1744 special? (gives r4 = 0)
print("\n" + "=" * 60)
print("CHECK H4 = 1744 (gives r4 = 0)")
print("=" * 60)
# q2 = (1744-1828)/12 = -84/12 = -7
q2_check = -7
q1_check = (2*(-7)-147)/7
p0_check = (2*(-7)-91)/7
p1_check = (532-9*(-7))/7
print(f"q2=-7: q1={q1_check}, p0={p0_check}, p1={p1_check}")
print(f"  Equation: t*({p0_check}+{p1_check}*t)*Q^2 - (1+{q1_check}*t+{q2_check}*t^2)*Q + 1 = 0")

# Discriminant: (1+q1*t+q2*t^2)^2 - 4t(p0+p1*t)
from sympy import symbols as sym, expand as exp2, factor as fac2, sqrt as sq2, series as ser2, Rational as Rat

t_sym = sym('t', commutative=True)[0] if isinstance(sym('t'), tuple) else symbols('t')
disc_1744 = (1 + q1_check*t_sym + q2_check*t_sym**2)**2 - 4*t_sym*(p0_check + p1_check*t_sym)
disc_1744_exp = expand(disc_1744)
disc_1744_fac = factor(disc_1744_exp)
print(f"  disc = {disc_1744_fac}")

# Check disc at t=1/8:
disc_at_eighth = disc_1744_exp.subs(t_sym, Rational(1,8))
print(f"  disc(1/8) = {disc_at_eighth}")

# Let me also try: require disc = (1-8t)(1+alpha*t) for some alpha
# This means disc is a degree-2 polynomial in t (NOT degree 4).
# Our disc is: (1+q1*t+q2*t^2)^2 - 4t*(p0+p1*t)
# For this to be degree 2, we need:
#   q2^2 = 0 (coeff of t^4) → q2 = 0
#   2*q1*q2 = 0 (coeff of t^3) → automatically 0
# So we need q2 = 0.

print("\n" + "=" * 60)
print("SPECIAL CASE: q2 = 0 (degree-2 discriminant)")
print("=" * 60)

# With q2 = 0:
# q1 = -147/7 = -21
# p0 = -91/7 = -13
# p1 = 532/7 = 76
# H4 = 12*0 + 1828 = 1828

q2_0 = 0
q1_0 = (2*0-147)/7  # = -21
p0_0 = (2*0-91)/7   # = -13
p1_0 = (532-0)/7    # = 76
H4_0 = 1828
print(f"q2=0: q1={q1_0}, p0={p0_0}, p1={p1_0}, H4={H4_0}")
print(f"  r4 = {1744 - H4_0}")

# disc = (1-21t)^2 - 4t(-13+76t) = 1-42t+441t^2 + 52t - 304t^2
#       = 1 + 10t + 137t^2
disc_q20 = (1 + q1_0*t_sym)**2 - 4*t_sym*(p0_0 + p1_0*t_sym)
print(f"  disc = {expand(disc_q20)}")
print(f"  disc = {factor(disc_q20)}")
print(f"  disc(1/8) = {disc_q20.subs(t_sym, Rational(1,8))}")

# Doesn't factor nicely and disc(1/8) won't be 0.
# The degree-2 disc case doesn't satisfy the radius constraint.

# So we need q2 ≠ 0 and disc(1/8) = 0.
# The answer is H4 ≈ 12*q2 + 1828 with q2 from the quadratic.
# But q2 is irrational → H4 is irrational. Bad.

# CONCLUSION: The 4-parameter ansatz t*(p0+p1*t)*Q^2-(1+q1*t+q2*t^2)*Q+1=0
# with disc(1/8)=0 gives IRRATIONAL H4. This means either:
# (a) the ansatz is too restrictive (need higher degree coefficients), or
# (b) the structural form of the equation is different.

# Let me try a 5-parameter ansatz with one more degree of freedom.
print("\n" + "=" * 60)
print("5-PARAM: t*(p0+p1*t+p2*t^2)*Q^2 - (1+q1*t+q2*t^2)*Q + 1 = 0")
print("=" * 60)

# t^0: -1+1=0 ✓
# t^1: p0-8-q1 = 0 → p0-q1=8
# t^2: 16p0+p1-36-8q1-q2 = 0
# t^3: 136p0+16p1+p2-204-36q1-8q2 = 0
# 3 eqs, 5 unknowns → 2 free (say q2, p2)

# From eq1: p0 = 8+q1
# From eq2: 16(8+q1)+p1-36-8q1-q2=0 → p1=-92-8q1+q2
# From eq3: 136(8+q1)+16(-92-8q1+q2)+p2-204-36q1-8q2=0
#   → 1088+136q1-1472-128q1+16q2+p2-204-36q1-8q2=0
#   → -588-28q1+8q2+p2=0
#   → p2 = 588+28q1-8q2

# Use q1 = (2q2-147)/7 from... wait, that was from the 4-param case.
# Here q1 is still free. Let me keep q1 and q2 as free.

# H4 from t^4:
# p0*q2_4coeff + p1*q2_3coeff + p2*q2_2coeff - H4 - q1*204 - q2*36 = 0
# where q2_ncoeff = coeff of t^n in Q^2
# q2_4 = 2*H4+4560 (has H4 in it!)
# Hmm, this makes the t^4 equation implicit in H4.

# Actually:
# t^4 terms of t*(p0+p1t+p2t^2)*Q^2:
#   p0*[coeff t^3 of Q^2] + p1*[coeff t^2 of Q^2] + p2*[coeff t^1 of Q^2]
# = p0*984 + p1*136 + p2*16

# t^4 terms of -(1+q1t+q2t^2)*Q:
#   -H4 - q1*204 - q2*36

# t^4: p0*984 + p1*136 + p2*16 - H4 - q1*204 - q2*36 = 0
# H4 = 984*p0 + 136*p1 + 16*p2 - 204*q1 - 36*q2

# Substitute: p0=8+q1, p1=-92-8q1+q2, p2=588+28q1-8q2
H4_formula = (984*(8) + 984*symbols('q1') + 136*(-92) - 136*8*symbols('q1') + 136*symbols('q2')
              + 16*588 + 16*28*symbols('q1') - 16*8*symbols('q2')
              - 204*symbols('q1') - 36*symbols('q2'))
H4_formula = expand(H4_formula)
# Let me just compute numerically
def H4_from_q1_q2(q1v, q2v):
    p0v = 8 + q1v
    p1v = -92 - 8*q1v + q2v
    p2v = 588 + 28*q1v - 8*q2v
    return 984*p0v + 136*p1v + 16*p2v - 204*q1v - 36*q2v

# H4 = 984*8 + 984*q1 + 136*(-92) + 136*(-8q1) + 136*q2
#    + 16*588 + 16*28*q1 - 16*8*q2 - 204*q1 - 36*q2
# = 7872 + 984q1 - 12512 - 1088q1 + 136q2
#   + 9408 + 448q1 - 128q2 - 204q1 - 36q2
# = (7872-12512+9408) + (984-1088+448-204)q1 + (136-128-36)q2
# = 4768 + 140*q1 + (-28)*q2
# = 4768 + 140*q1 - 28*q2

print("H4 = 4768 + 140*q1 - 28*q2")

# Now: disc = (1+q1*t+q2*t^2)^2 - 4t*(p0+p1*t+p2*t^2)
# This is degree 4 in t.
# Need disc(1/8) = 0 → one constraint on (q1, q2).
# Need H4 integer + r4 = 1744-H4 ≥ 0 → H4 ≤ 1744.

# For the sl_2 case: Q = 1+3t+6t^2+15t^3+36t^4+91t^5+...
# Equation: t(1+t)Q^2-(1+t)Q+1=0
# In our form: p0=1, p1=1, p2=0, q1=1, q2=0
# Check: p0-q1=0≠8. FAIL!
# The sl_2 equation has B(t) = -(1+t), not -(1+q1t+...). The minus sign!

# Oh wait, the sl_2 equation is: t(1+t)Q^2 - (1+t)Q + 1 = 0
# In our notation: A(t)*Q^2 + B(t)*Q + C(t) = 0
# A = t(1+t), B = -(1+t), C = 1
# So B has a LEADING -1, matching our -(1+q1t+q2t^2).
# With q1=1, q2=0: B = -(1+t). p0=1, p1=1, p2=0.
# Check p0-q1=1-1=0≠8. For sl_2, h1=3, not 8.
# Right — the t^1 equation for sl_2 is p0-3-q1=0 → p0-q1=3.
# With p0=1, q1=1: 1-1=0≠3. FAIL!

# Something is wrong. Let me recheck.
# t(1+t)Q^2 - (1+t)Q + 1 = 0
# Coeff of t^1:
# From t(1+t)Q^2: coeff of t^0 in (1+t)Q^2 = 1*Q^2|_{t^0} = 1
# Wait: t*(1+t)*Q^2 = t*Q^2 + t^2*Q^2.
# Coeff of t^1 in t*Q^2 = Q^2|_{t^0} = 1
# Coeff of t^1 in t^2*Q^2 = 0
# So coeff of t^1 in A*Q^2 = 1.
# Coeff of t^1 in -(1+t)*Q: -(Q|_{t^1}) - (Q|_{t^0}) = -3 - 1 = -4
# Coeff of t^1 in 1: 0
# Total: 1 - 4 = -3 ≠ 0.

# Hmm, that's wrong. Let me re-derive for sl_2.
# The equation is t(1+t)Q^2 - (1+t)Q + 1 = 0 where Q = 1+3t+6t^2+...
# At t=0: 0 - (1)(1) + 1 = 0 ✓

# Hmm, but the sl_2 bar cohomology GF is NOT the Riordan R(x).
# From the phi-ansatz: R(x) = (1-sqrt(1-4x/(1+x)))/(2x) = 1+0x+x^2+x^3+3x^4+...
# That's the Riordan sequence starting from n=0.
# The bar cohomology is 1,3,6,15,36,91,... which is R(3),R(4),R(5),...
# NOT the same as R(0),R(1),R(2),...

# So Q(t) = sum_{n>=0} R(n+3) t^n does NOT satisfy t(1+t)Q^2-(1+t)Q+1=0.
# It satisfies a DIFFERENT equation (the shifted one from sl3_bar_from_riordan.py).

# OK so the phi-ansatz was wrong because it generates R(x), not the shifted Q(t).

# This changes everything. Let me find what equation Q(t) satisfies for sl_2
# and use that as a template for sl_3.

print("\n" + "=" * 60)
print("FINDING THE EQUATION THAT Q(t)=1+3t+6t^2+15t^3+... SATISFIES (sl_2)")
print("=" * 60)

from sympy import symbols, Poly, solve, expand, factor, Rational, sqrt, series

t_s = symbols('t')

# Q satisfies: some algebraic equation with polynomial coefficients.
# Try: a(t)*Q^2 + b(t)*Q + c(t) = 0
# with a, b, c polynomials of minimal degree.

# From the Riordan relation, R satisfies t(1+t)R^2 - (1+t)R + 1 = 0.
# Q(t) = (R(t) - 1 - t^2) / t^3 where R(t) = sum R(n) t^n.
# Wait: R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6,...
# So R(t) = 1 + t^2 + t^3 + 3t^4 + 6t^5 + 15t^6 + ...
# Q(t) = 1 + 3t + 6t^2 + 15t^3 + 36t^4 + ... = sum_{n>=0} R(n+3) t^n
# So R(t) = 1 + t^2 + t^3 * Q(t)

# Substitute into t(1+t)R^2 - (1+t)R + 1 = 0:
Q_s = symbols('Q')
R_sub = 1 + t_s**2 + t_s**3 * Q_s
eq_sl2 = t_s * (1+t_s) * R_sub**2 - (1+t_s) * R_sub + 1
eq_sl2_exp = expand(eq_sl2)

# Collect as polynomial in Q:
eq_poly = Poly(eq_sl2_exp, Q_s)
print(f"Degree in Q: {eq_poly.degree()}")
for i in range(eq_poly.degree()+1):
    coeff = factor(eq_poly.nth(i))
    print(f"  Q^{i}: {coeff}")

# Factor out common t powers
a_sl2 = eq_poly.nth(2)  # coefficient of Q^2
b_sl2 = eq_poly.nth(1)  # coefficient of Q
c_sl2 = eq_poly.nth(0)  # constant

print(f"\nDiscriminant b^2-4ac = {factor(b_sl2**2 - 4*a_sl2*c_sl2)}")

# Q = (-b ± sqrt(disc)) / (2a)
disc_sl2 = b_sl2**2 - 4*a_sl2*c_sl2
Q_sol = (-b_sl2 - sqrt(disc_sl2)) / (2*a_sl2)
Q_sol_series = series(Q_sol, t_s, 0, 8)
print(f"\nQ series (- branch):")
for n in range(7):
    print(f"  t^{n}: {Q_sol_series.coeff(t_s, n)}")

Q_sol2 = (-b_sl2 + sqrt(disc_sl2)) / (2*a_sl2)
Q_sol2_series = series(Q_sol2, t_s, 0, 8)
print(f"Q series (+ branch):")
for n in range(7):
    print(f"  t^{n}: {Q_sol2_series.coeff(t_s, n)}")
