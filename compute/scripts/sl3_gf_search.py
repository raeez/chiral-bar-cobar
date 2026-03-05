#!/usr/bin/env python3
"""Find the algebraic generating function for sl_3 bar cohomology.

Known values: H^1=8, H^2=36, H^3=204.
The generating function P(x) = sum_{n>=1} H^n x^n is algebraic.

For sl_2: P = (1+x-sqrt(1-2x-3x^2))/(2x(1+x)), giving Riordan R(n+3).
The Riordan GF R(x) = sum R(n) x^n satisfies: x(1+x)R^2 - (1+x)R + 1 = 0.

Strategy: find an algebraic equation for the sl_3 GF by fitting to data
and using structural constraints (growth rate 8^n, etc.).
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, cancel, S, Integer, nsimplify,
                   Poly, groebner, Matrix)
from sympy.abc import x

# ============================================================
# Step 1: Verify sl_2 formula and understand the structure
# ============================================================

print("=" * 60)
print("STEP 1: Understanding sl_2 structure")
print("=" * 60)

# Riordan GF: R(x) = (1+x-sqrt(1-2x-3x^2))/(2x(1+x))
# Satisfies: x(1+x)R^2 - (1+x)R + 1 = 0

# The bar cohomology GF: Q(x) = sum_{n>=1} H^n x^n
# where H^n = R(n+3) for sl_2.
# Q(x) = 3x + 6x^2 + 15x^3 + 36x^4 + 91x^5 + ...

# The Riordan sequence R(n) also equals dim of Motzkin paths avoiding
# double rises, or equivalently, the number of non-crossing
# partition pairs on [n].

# For the UNREDUCED Riordan GF R(x), the coefficients are:
# R(0)=1, R(1)=0, R(2)=1, R(3)=1, R(4)=3, R(5)=6, ...

# R satisfies: x(1+x)R^2 - (1+x)R + 1 = 0
# Discriminant: (1+x)^2 - 4x(1+x) = (1+x)(1-3x)

# Let me find what equation Q satisfies.
# Q(x) = (R(x) - 1 - x^2 - x^3) / x^3  (shifting by 3)
# R(x) = 1 + x^2 + x^3 + x^3 * Q(x)

R, Q = symbols('R Q')

# R = 1 + x^2 + x^3*(1 + Q) where Q starts at 3x
# Substitute into x(1+x)R^2 - (1+x)R + 1 = 0:
R_expr = 1 + x**2 + x**3*(1 + Q)

eq = x*(1+x)*R_expr**2 - (1+x)*R_expr + 1
eq_expanded = expand(eq)

# Collect by Q:
q0 = eq_expanded.subs(Q, 0)
q1 = expand(eq_expanded - q0 - x**3*(1+x)*Q*2*(1+x**2+x**3) - x**6*(1+x)*Q**2)

# Actually let me just expand properly
eq_poly = Poly(eq_expanded, Q)
print(f"\nEquation as polynomial in Q:")
print(f"  Degree: {eq_poly.degree()}")
for i, c in enumerate(eq_poly.all_coeffs()):
    print(f"  Q^{eq_poly.degree()-i} coeff: {factor(c)}")

# Get the equation for Q by dividing out common x factors
coeffs = eq_poly.all_coeffs()  # [coeff of Q^2, coeff of Q^1, coeff of Q^0]
print(f"\nCoeff of Q^2: {factor(coeffs[0])}")
print(f"Coeff of Q^1: {factor(coeffs[1])}")
print(f"Coeff of Q^0: {factor(coeffs[2])}")

# The constant term (Q^0) should vanish at x=0 (since Q=0 satisfies
# the equation for the truncated R).
print(f"\nQ^0 term at x=0: {coeffs[2].subs(x, 0)}")

# ============================================================
# Step 2: Try to generalize to sl_3
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: Generalize to sl_3")
print("=" * 60)

# For sl_3, the bar cohomology is: 8, 36, 204, a4, a5, ...
# Growth rate 8^n (= dim(sl_3)^n).

# ANSATZ: The generating function satisfies a quadratic equation
# with discriminant having a root at x = 1/8 (= 1/dim g).

# Following the sl_2 pattern, try:
# There exists a sequence S(n) (generalized Riordan) satisfying
# a quadratic equation, and H^n = S(n + shift) for some shift.

# For sl_2: R satisfies x(1+x)R^2 - (1+x)R + 1 = 0
# Discriminant: (1+x)^2 - 4x(1+x) = (1+x)(1+x-4x) = (1+x)(1-3x)
# Roots at x = -1 and x = 1/3 = 1/dim(g).

# For sl_3, try: a(x)S^2 + b(x)S + c(x) = 0
# with discriminant having root at x = 1/8.

# Most general degree-2 quadratic:
# (a0 + a1*x + a2*x^2)*S^2 + (b0 + b1*x + b2*x^2)*S + (c0 + c1*x + c2*x^2) = 0

# Constraints:
# 1. S(0) should be well-defined (S is a formal power series)
# 2. The discriminant b(x)^2 - 4a(x)c(x) should factor as k*(1-8x)*(...)

# For sl_2, the equation is normalized as A(x)*R^2 + B(x)*R + C = 0:
# x(1+x)*R^2 - (1+x)*R + 1 = 0
# A = x(1+x), B = -(1+x), C = 1.
# Note: A(0) = 0, so at x=0: B(0)*R(0) + C(0) = 0 => -1*R(0) + 1 = 0 => R(0) = 1.

# For sl_3, try: A(x)*S^2 + B(x)*S + C = 0 with A(0)=0, C constant.
# Then S(0) = -C/B(0).

# Generalize: A(x) = x*alpha(x), B(x) = beta(x), C = gamma.
# At x=0: beta(0)*S(0) + gamma = 0 => S(0) = -gamma/beta(0).

# For sl_2: S(0)=R(0)=1, beta(0)=-1, gamma=1 => S(0) = -1/(-1) = 1. ✓

# PARAMETRIC APPROACH:
# A(x) = x*(1 + p*x), B(x) = -(1 + q*x), C = 1.
# Then S(0) = 1 (from -(-1)*1 + 1 = 0 ... wait: B(0)*S(0) + C = -1*1 + 1 = 0. ✓)
# Discriminant: (1+qx)^2 - 4x(1+px) = 1 + 2qx + q^2*x^2 - 4x - 4px^2
#             = 1 + (2q-4)x + (q^2-4p)x^2

# For the discriminant to vanish at x=1/8:
# 1 + (2q-4)/8 + (q^2-4p)/64 = 0
# 64 + 8(2q-4) + (q^2-4p) = 0
# 64 + 16q - 32 + q^2 - 4p = 0
# q^2 + 16q + 32 - 4p = 0
# p = (q^2 + 16q + 32) / 4

# Series expansion: S = 1 + s1*x + s2*x^2 + ...
# From the equation: x(1+px)(1+s1*x+...)^2 - (1+qx)(1+s1*x+...) + 1 = 0

# x^0: -1*1 + 1 = 0. ✓
# x^1: 1 + (-1)*s1 + (-q) = 0 => s1 = 1 - q
# x^2: (1+p) + 2s1 - s2 - q*s1 = 0
#   = 1 + p + 2(1-q) - s2 - q(1-q)
#   = 1 + p + 2 - 2q - s2 - q + q^2
#   = 3 + p - 3q + q^2 - s2
#   => s2 = 3 + p - 3q + q^2

p_sym, q_sym = symbols('p q')

s1 = 1 - q_sym
s2_expr = 3 + p_sym - 3*q_sym + q_sym**2

# Constraint: p = (q^2 + 16q + 32)/4
p_expr = (q_sym**2 + 16*q_sym + 32) / 4

s2_constrained = s2_expr.subs(p_sym, p_expr)
s2_constrained = simplify(s2_constrained)

print(f"s1 = 1 - q = {s1}")
print(f"s2 = {simplify(s2_constrained)}")

# Now: for sl_2, the shift is 3: H^n = S(n+3).
# So S(0)=1, S(1)=s1, S(2)=s2, S(3)=s3 are the "Riordan-like" numbers.
# H^1 = S(shift+1), H^2 = S(shift+2), H^3 = S(shift+3).

# For sl_2: shift=3, H^1 = R(4)=3, H^2 = R(5)=6.
# R(1)=0, so s1=0, which gives q=1. Then p=(1+16+32)/4 = 49/4.
# But for sl_2, p=1 (from A=x(1+x), so p=1). And 49/4 ≠ 1!

# So the parametric form A=x(1+px), B=-(1+qx) doesn't directly give sl_2
# with the discriminant-at-1/d constraint. Let me re-examine.

# For sl_2: disc = (1+x)^2 - 4x(1+x) = (1+x)(1-3x).
# At x=1/3: (1+1/3)(1-1) = 0. ✓ Root at x = 1/dim(g) = 1/3.
# p=1, q=1. Check constraint: p = (q^2+16q+32)/4??? No, that was for dim=8.

# I need to redo with dim = d:
# Disc = (1+qx)^2 - 4x(1+px) = 0 at x=1/d:
# (1+q/d)^2 - 4/d(1+p/d) = 0
# For d=3: (1+q/3)^2 - 4/3(1+p/3) = 0
# With p=q=1: (1+1/3)^2 - 4/3(1+1/3) = 16/9 - 16/9 = 0. ✓

# General: (1+q/d)^2 = (4/d)(1+p/d)
# d(1+q/d)^2 = 4(1+p/d)
# d(1+2q/d+q^2/d^2) = 4+4p/d
# d + 2q + q^2/d = 4 + 4p/d
# d^2 + 2qd + q^2 = 4d + 4p
# p = (d^2 + 2qd + q^2 - 4d) / 4 = ((d+q)^2 - 4d) / 4

print(f"\nGeneral constraint: p = ((d+q)^2 - 4d) / 4")
print(f"For d=3, q=1: p = ((3+1)^2 - 12)/4 = (16-12)/4 = 1. ✓")

# For d=8: p = ((8+q)^2 - 32) / 4 = (q^2+16q+64-32)/4 = (q^2+16q+32)/4

# Now I need to find q for sl_3. The data: H^n for some shift.
# With shift unknown, I have: H^1 = S(shift+1) = 8, etc.

# s1 = 1-q (coefficient of x^1 in S)
# s2 = 3 + p - 3q + q^2 (coefficient of x^2)
# etc.

# For sl_2: s1 = 1-1 = 0 = R(1). H^1 = S(4) = R(4) = 3. Shift = 3.
# The shift depends on d. Maybe shift = d for general Lie algebra?
# sl_2: d=3, shift=3. Let's check: if shift=d=8 for sl_3...

# With shift=8: H^1 = S(9) = 8. Need to compute S(n) for n=0,...,12.
# That's a lot of work. Let me try smaller shifts.

# Actually, for sl_2, the shift is 3 = dim sl_2. Maybe for sl_3,
# shift = 8 = dim sl_3. But then I need S(9)=8, S(10)=36, S(11)=204.
# That would require computing S up to index 11 with one free parameter q.

# Let me try to use the RECURRENCE instead.
# From x(1+px)S^2 - (1+qx)S + 1 = 0, we can derive a recurrence for S(n).

# Alternatively, let me just compute S(n) as a function of q (with p determined)
# and match to the data.

# Let me compute S(n) for general q using the quadratic equation.
# S = [(1+qx) - sqrt(disc)] / [2x(1+px)]
# disc = (1+qx)^2 - 4x(1+px) = 1 + (2q-4)x + (q^2-4p)x^2

# With p = ((d+q)^2 - 4d)/4 for d=8:
d = 8
p_of_q = ((d + q_sym)**2 - 4*d) / 4

disc = 1 + (2*q_sym - 4)*x + (q_sym**2 - 4*p_of_q)*x**2
disc_simplified = simplify(expand(disc))
print(f"\nDiscriminant for d=8: {factor(disc_simplified)}")

# disc = 1 + (2q-4)x + (q^2 - (q^2+16q+32))x^2
#       = 1 + (2q-4)x + (-16q-32)x^2
#       = 1 + (2q-4)x - (16q+32)x^2

# Let me factor: disc = (1-8x)(1 + (2q+4)x/(... )) ?
# At x=1/8: disc(1/8) = 0 by construction.
# disc = -(16q+32)x^2 + (2q-4)x + 1
# = -(16q+32)(x - 1/8)(x - r) for some other root r.

# Product of roots: 1/(-16q-32)) = 1/(8r(-16q-32))... hmm.
# Sum of roots: (2q-4)/(-16q-32)) = -(2q-4)/(16q+32) = -(q-2)/(8q+16) = -(q-2)/(8(q+2))
# Product: 1/(-16q-32) = -1/(16(q+2))
# So 1/8 * r = -1/(16(q+2)) => r = -1/(2(q+2))

# disc = -(16q+32)(x - 1/8)(x + 1/(2(q+2)))
#       = -16(q+2)(x - 1/8)(x + 1/(2(q+2)))
#       = -16(q+2) * x^2 + 16(q+2)(1/8 - 1/(2(q+2)))x + 16(q+2)/(8*2(q+2))
# Hmm, let me just verify with factoring.

# disc = 1 + (2q-4)x - (16q+32)x^2
# = -(16q+32)x^2 + (2q-4)x + 1
# = -(16q+32)[x^2 - (2q-4)/(16q+32) x - 1/(16q+32)]
# = -(16(q+2))[x^2 - (q-2)/(8(q+2)) x - 1/(16(q+2))]

# Roots: x = [(q-2)/(8(q+2)) ± sqrt(...)]/2
# One root is 1/8 by construction.

# Second root: by Vieta, product = -1/(16(q+2)), sum = (q-2)/(8(q+2)).
# 1/8 + r = (q-2)/(8(q+2))
# r = (q-2)/(8(q+2)) - 1/8 = (q-2-q-2)/(8(q+2)) = -4/(8(q+2)) = -1/(2(q+2))

print(f"\nDiscriminant roots: x = 1/8 and x = -1/(2(q+2))")
print(f"For sl_2 (d=3, q=1): second root = -1/(2*3) = -1/6... but sl_2 has root at -1!")
print(f"  So this formula is wrong for sl_2 because sl_2 has d=3, not d=8.")

# For sl_2 with d=3: disc = (1+x)(1-3x) = 1-2x-3x^2.
# p=1, q=1. disc = 1+(2-4)x+(1-4)x^2 = 1-2x-3x^2. ✓
# Roots: 1/3 and -1.
# From formula: second root = -1/(2(1+2)) = -1/6. But actual = -1. WRONG.

# The formula above only works for the SPECIFIC parametrization with
# d appearing. Let me redo for general d.

# disc = 1 + (2q-4)x + (q^2 - 4p)x^2
# p = ((d+q)^2 - 4d)/4
# q^2 - 4p = q^2 - (d+q)^2 + 4d = q^2 - d^2 - 2dq - q^2 + 4d = -d^2 - 2dq + 4d
#           = -d(d + 2q - 4)

# disc = 1 + (2q-4)x - d(d+2q-4)x^2
# Factor: need to verify (1-dx) is a factor.
# disc(1/d) = 1 + (2q-4)/d - d(d+2q-4)/d^2 = 1 + (2q-4)/d - (d+2q-4)/d
#           = 1 + (2q-4-d-2q+4)/d = 1 - d/d = 1-1 = 0. ✓

# Second root: product of roots = 1/(d(d+2q-4)) (from -disc/leading coeff)
# sum of roots = (2q-4)/(d(d+2q-4))

# (1/d) * r = 1/(d(d+2q-4)) => r = 1/(d+2q-4)... wait, product = -const/leading.
# disc = -d(d+2q-4)x^2 + (2q-4)x + 1
# Product of roots = 1/(-d(d+2q-4)) * (-1) = 1/(d(d+2q-4)) [using c/a for quadratic ax^2+bx+c]

# Actually: for ax^2+bx+c=0, product = c/a.
# Here a = -d(d+2q-4), c = 1.
# Product = 1/(-d(d+2q-4)) = -1/(d(d+2q-4))

# (1/d) * r = -1/(d(d+2q-4))
# r = -1/(d+2q-4)

# For d=3, q=1: r = -1/(3+2-4) = -1/1 = -1. ✓✓✓

print(f"\nGeneral second root: r = -1/(d+2q-4)")
print(f"For d=3, q=1: r = -1/(3+2-4) = -1. ✓ (matches sl_2)")

# So disc = -d(d+2q-4) * (x - 1/d) * (x + 1/(d+2q-4))
#          = d(d+2q-4)(1/d - x)(x + 1/(d+2q-4))
#          = (d+2q-4)(1-dx)(1 + x*(d+2q-4)/(d+2q-4))
# Hmm, let me just write:
# disc = (1 - d*x)(1 + (d+2q-4)*x)

# Check: (1-dx)(1+(d+2q-4)x) = 1 + (d+2q-4)x - dx - d(d+2q-4)x^2
#       = 1 + (2q-4)x - d(d+2q-4)x^2
#       = disc. ✓✓✓

print(f"\ndisc = (1-{d}x)(1+(d+2q-4)x) = (1-dx)(1+(d+2q-4)x)")
print(f"For d=3, q=1: (1-3x)(1+(3+2-4)x) = (1-3x)(1+x). ✓")

# Now the GF: S = [(1+qx) - sqrt(disc)] / [2x(1+px)]
# For d=8: S(x; q) depends on the single parameter q.
# S(0) = 1 (verified above).

# I need to compute S(n; q) and find q such that S(n+shift) = H^n for sl_3.

# First, let me find the correct shift.
# For sl_2: S(1)=0 (the first Riordan number is R(1)=0). And shift=3.
# The shift is related to the initial sequence of the S sequence.

# Actually, let me just compute S(n) as a function of q for d=8 and
# see which q gives H^n values matching 8, 36, 204 for some shift.

# S = [(1+qx) - sqrt((1-8x)(1+(4+2q)x))] / [2x(1+px)]
# where p = ((8+q)^2 - 32)/4 = (q^2+16q+32)/4

# Let me compute the first ~15 coefficients of S for various q values.

import numpy as np

def compute_S_coefficients(q_val, d_val=8, N=15):
    """Compute N coefficients of S(x) for given q, d."""
    p_val = ((d_val + q_val)**2 - 4*d_val) / 4

    # Use the recurrence from the quadratic equation:
    # x(1+px)S^2 - (1+qx)S + 1 = 0
    # S = 1 + s1*x + s2*x^2 + ...

    s = [0] * N
    s[0] = 1  # S(0) = 1

    # From the equation, expand order by order:
    # sum_{n>=0} [coeff of x^n in (x(1+px)S^2 - (1+qx)S + 1)] = 0

    # x(1+px)S^2 = x*S^2 + p*x^2*S^2
    # S^2 = sum_{n>=0} (sum_{k=0}^n s[k]*s[n-k]) x^n

    for n in range(1, N):
        # Coefficient of x^n in the equation = 0
        # From x*S^2: coeff of x^{n-1} in S^2 = sum_{k=0}^{n-1} s[k]*s[n-1-k]
        # From p*x^2*S^2: coeff of x^{n-2} in S^2 (if n>=2) = sum_{k=0}^{n-2} s[k]*s[n-2-k]
        # From -(1+qx)S: -s[n] - q*s[n-1] (if n>=1)
        # From +1: delta_{n,0} (already used)

        sq_nm1 = sum(s[k] * s[n-1-k] for k in range(n))
        sq_nm2 = sum(s[k] * s[n-2-k] for k in range(n-1)) if n >= 2 else 0

        # Equation: sq_nm1 + p*sq_nm2 - s[n] - q*s[n-1] = 0
        s[n] = sq_nm1 + p_val * sq_nm2 - q_val * s[n-1]

    return s

print("\n" + "=" * 60)
print("STEP 3: Searching for q parameter")
print("=" * 60)

# For sl_2 (d=3, q=1):
s_sl2 = compute_S_coefficients(1.0, d_val=3, N=12)
print(f"\nsl_2 (d=3, q=1): S = {[int(round(x)) for x in s_sl2]}")
print(f"  S[4:8] = {[int(round(s_sl2[i])) for i in range(4,8)]}")
print(f"  Expected H^1..4 = [3, 6, 15, 36] (= R(4)..R(7))")

# Now scan q for d=8, trying to match H^1=8, H^2=36, H^3=204
# with various shifts.

print(f"\n--- Scanning q for d=8, various shifts ---")

best_results = []

for q_test in np.linspace(-5, 20, 2501):
    s = compute_S_coefficients(q_test, d_val=8, N=20)

    # Try different shifts
    for shift in range(1, 15):
        if shift + 3 >= 20:
            continue
        if abs(s[shift+1]) < 0.01:
            continue
        if abs(s[shift+1] - 8) < 0.5:
            if abs(s[shift+2] - 36) < 1.0:
                if abs(s[shift+3] - 204) < 2.0:
                    a4 = s[shift+4]
                    best_results.append((q_test, shift, s[shift+1], s[shift+2], s[shift+3], a4))

print(f"\nFound {len(best_results)} matches:")
for q_test, shift, h1, h2, h3, a4 in best_results[:20]:
    print(f"  q={q_test:.4f}, shift={shift}: H^1={h1:.1f}, H^2={h2:.1f}, H^3={h3:.1f}, H^4={a4:.1f}")

# Refine the best matches
if best_results:
    from scipy.optimize import minimize_scalar

    for q_test, shift, _, _, _, _ in best_results[:5]:
        def objective(q):
            s = compute_S_coefficients(q, d_val=8, N=20)
            if shift+3 >= 20:
                return 1e10
            return (s[shift+1]-8)**2 + (s[shift+2]-36)**2 + (s[shift+3]-204)**2

        result = minimize_scalar(objective, bounds=(q_test-1, q_test+1), method='bounded')
        q_opt = result.x
        s = compute_S_coefficients(q_opt, d_val=8, N=20)

        print(f"\n  Refined: q={q_opt:.8f}, shift={shift}")
        print(f"    S[0:shift+6] = {[round(s[i],2) for i in range(min(shift+6,20))]}")
        print(f"    H^1={s[shift+1]:.6f}, H^2={s[shift+2]:.6f}, H^3={s[shift+3]:.6f}")
        print(f"    H^4={s[shift+4]:.6f}")

        # Check if q is a nice rational number
        from fractions import Fraction
        q_frac = Fraction(q_opt).limit_denominator(1000)
        print(f"    q ≈ {q_frac} = {float(q_frac):.8f}")
