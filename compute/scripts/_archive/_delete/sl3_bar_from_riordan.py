#!/usr/bin/env python3
"""Derive the algebraic equation for the bar cohomology GF.

For sl_2: R(x) satisfies x(1+x)R^2 - (1+x)R + 1 = 0 (Riordan).
The bar cohomology GF is F(t) = 1 + 3t + 6t^2 + 15t^3 + ...
with F(t) = sum_{n>=0} R(n+3) t^n.

Step 1: Derive the algebraic equation for F from R's equation.
Step 2: Find the analogous equation for sl_3.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, collect, Poly, cancel, together,
                   Matrix, Symbol, groebner)

x, t, F, R = symbols('x t F R')

# =============================================================
# Step 1: Derive equation for F(t) = sum R(n+3) t^n for sl_2
# =============================================================
print("=" * 70)
print("STEP 1: Derive equation for F(t) from Riordan equation")
print("=" * 70)

# R(x) = 1 + 0*x + x^2 + x^3*F(x)
# where F(x) = 1 + 3x + 6x^2 + 15x^3 + ...
# (since R(3)=1, R(4)=3, R(5)=6, ...)

# Substituting R = 1 + x^2 + x^3*F into x(1+x)R^2 - (1+x)R + 1 = 0:
R_expr = 1 + x**2 + x**3 * F
eq = x*(1+x)*R_expr**2 - (1+x)*R_expr + 1
eq_expanded = expand(eq)

# Collect powers of x and F:
# This gives an equation in x and F. We want to eliminate x
# by noting that F = F(x) (a function of x).
# But actually, since F(x) = sum R(n+3) x^n, the equation should
# hold identically for the specific F(x) that satisfies it.

# Let me expand and collect in terms of F:
eq_poly = Poly(eq_expanded, F)
print(f"\nEquation as polynomial in F:")
print(f"  Degree in F: {eq_poly.degree()}")
for power in range(eq_poly.degree() + 1):
    coeff = eq_poly.nth(power)
    coeff_factored = factor(coeff)
    print(f"  F^{power}: {coeff_factored}")

# So the equation is: a(x)*F^2 + b(x)*F + c(x) = 0
# where a, b, c are polynomials in x.
a_coeff = eq_poly.nth(2)
b_coeff = eq_poly.nth(1)
c_coeff = eq_poly.nth(0)

print(f"\na(x) = {factor(a_coeff)}")
print(f"b(x) = {factor(b_coeff)}")
print(f"c(x) = {factor(c_coeff)}")

# Discriminant:
disc = b_coeff**2 - 4*a_coeff*c_coeff
disc_factored = factor(disc)
print(f"\nDiscriminant = {disc_factored}")

# Solution:
F_sol = (-b_coeff - sqrt(disc)) / (2*a_coeff)  # pick correct branch
F_series = series(F_sol, x, 0, 8)
print(f"\nF(x) series (- branch):")
for n in range(8):
    c = F_series.coeff(x, n)
    print(f"  x^{n}: {c}")

# Check + branch too
F_sol_plus = (-b_coeff + sqrt(disc)) / (2*a_coeff)
F_series_plus = series(F_sol_plus, x, 0, 8)
print(f"\nF(x) series (+ branch):")
for n in range(8):
    c = F_series_plus.coeff(x, n)
    print(f"  x^{n}: {c}")

# =============================================================
# Step 2: Generalize to sl_3
# =============================================================
print("\n" + "=" * 70)
print("STEP 2: Generalize to sl_3")
print("=" * 70)

# For sl_2, the Riordan equation is: x(1+x)R^2 - (1+x)R + 1 = 0
# This can be written as: x(1+p*x)R^2 - (1+p*x)R + 1 = 0 with p=1
# Or more generally: x*A(x)*R^2 - A(x)*R + 1 = 0 with A(x) = 1+x.
# Equivalently: R = A/(x*A*R + ... hmm.

# The key: the discriminant of x(1+x)R^2-(1+x)R+1=0 is
# (1+x)^2 - 4x(1+x) = (1+x)(1-3x), with roots x=-1 and x=1/3=1/dim(sl_2).

# For sl_3 (d=8), we want discriminant root at x=1/8.
# General form: the equation for R should give growth rate d^n for R(n).

# INSIGHT: For sl_2, the equation factors as:
# x(1+x)R^2 - (1+x)R + 1 = 0
# disc = (1+x)(1-3x) = (1+x)(1-d*x) with d=3.
# The "-1" root of (1+x) and the "1/d" root.

# For sl_3, try: the equation for R is
# x*B(x)*R^2 - B(x)*R + 1 = 0
# where B(x) = 1 + p*x (linear) and disc = B(x)^2 - 4*x*B(x) = B(x)(B(x)-4x)
# = B(x)(1 + (p-4)*x)
# disc root at x=1/d: B(1/d)(1+(p-4)/d) = 0, OR 1+(p-4)/d=0 => p = 4-d.

# For sl_2: p = 4-3 = 1, B(x) = 1+x. disc = (1+x)(1-3x). ✓!

# For sl_3: p = 4-8 = -4, B(x) = 1-4x.
# Equation: x(1-4x)R^2 - (1-4x)R + 1 = 0
# disc = (1-4x)(1-8x). Roots: x=1/4 and x=1/8.
# Radius of convergence = min(1/4, 1/8) = 1/8. ✓

print("Ansatz: x*B(x)*R^2 - B(x)*R + 1 = 0 with B(x) = 1+(4-d)*x")
print(f"  sl_2 (d=3): B(x) = 1+x, disc = (1+x)(1-3x)")
print(f"  sl_3 (d=8): B(x) = 1-4x, disc = (1-4x)(1-8x)")

# Compute R(x) for the sl_3 ansatz:
# x(1-4x)R^2 - (1-4x)R + 1 = 0
# R = [(1-4x) ± sqrt((1-4x)(1-8x))] / (2x(1-4x))
#   = [1 ± sqrt((1-8x)/(1-4x))] / (2x)  ... hmm, need to simplify.

# R = [(1-4x) - sqrt((1-4x)(1-8x))] / (2x(1-4x))
#   = [1 - sqrt((1-8x)/(1-4x))] / (2x)

# Actually: disc = (1-4x)^2 - 4x(1-4x) = (1-4x)(1-4x-4x) = (1-4x)(1-8x)
# R = [(1-4x) ± sqrt((1-4x)(1-8x))] / (2x(1-4x))

disc_sl3 = (1 - 4*x)*(1 - 8*x)
R_sl3_minus = ((1-4*x) - sqrt(disc_sl3)) / (2*x*(1-4*x))
R_sl3_plus = ((1-4*x) + sqrt(disc_sl3)) / (2*x*(1-4*x))

print("\n--- R(x) for sl_3 ansatz ---")
R_m_series = series(R_sl3_minus, x, 0, 10)
R_p_series = series(R_sl3_plus, x, 0, 10)

print("R- series:")
for n in range(10):
    c = R_m_series.coeff(x, n)
    print(f"  R({n}) = {c}")

print("\nR+ series:")
for n in range(8):
    c = R_p_series.coeff(x, n)
    print(f"  R({n}) = {c}")

# Extract bar cohomology: H^n = R(n+3) (if R starts at n=0)
# Or: the bar cohomology GF is F(t) = sum_{n>=0} R(n+k) t^n for some shift k.
# For sl_2: R(0)=1,R(1)=0,R(2)=1,R(3)=1,R(4)=3,R(5)=6,...
# H^1=3=R(4), H^2=6=R(5). Shift = 3.

# For sl_3: need to check what shift gives H^1=8.

print("\n--- Finding the correct shift for sl_3 ---")
R_coeffs = []
for n in range(10):
    R_coeffs.append(R_m_series.coeff(x, n))
print(f"R(0..9) = {R_coeffs}")

# Find shift k such that R(k+1) = 8 (= dim sl_3)
for k in range(9):
    if k+1 < len(R_coeffs) and R_coeffs[k+1] == 8:
        print(f"  R({k+1}) = 8 => shift = {k}")
        print(f"  Then H^1 = R({k+1}) = {R_coeffs[k+1]}")
        if k+2 < len(R_coeffs):
            print(f"  H^2 = R({k+2}) = {R_coeffs[k+2]}")
        if k+3 < len(R_coeffs):
            print(f"  H^3 = R({k+3}) = {R_coeffs[k+3]}")
        if k+4 < len(R_coeffs):
            print(f"  H^4 = R({k+4}) = {R_coeffs[k+4]}")

# =============================================================
# Also try a more general equation: x*(1+p*x+q*x^2)*R^2 - (1+p*x+q*x^2)*R + 1 = 0
# =============================================================
print("\n" + "=" * 70)
print("MORE GENERAL: x*B(x)*R^2 - B(x)*R + 1 = 0 with B quadratic")
print("=" * 70)

# B(x) = 1 + p*x + q*x^2
# disc = B(x)^2 - 4*x*B(x) = B(x)(B(x)-4x) = B(x)(1+(p-4)*x+q*x^2)
# Need disc root at x=1/d. So either B(1/d)=0 or 1+(p-4)/d+q/d^2=0.

# For the SIMPLEST case (B linear, already done above), B(1/d) ≠ 0 and 1+(p-4)/d = 0.
# For the quadratic case, we have more freedom.

# Let's try to FIT: require R(1)=0, R(2)=h2_raw, etc., by choosing p,q.
# But first let me see if the linear ansatz (q=0) gives the right answer for sl_3.

# For the linear ansatz sl_3:
print("\n--- Check linear ansatz sl_3: R(n+?) matches H^n = 8,36,204 ---")
# From the R- series computed above, check if consecutive R values match.
for start in range(10):
    match = True
    if start + 1 >= len(R_coeffs) or R_coeffs[start + 1] != 8:
        match = False
    if match and (start + 2 >= len(R_coeffs) or R_coeffs[start + 2] != 36):
        match = False
    if match and (start + 3 >= len(R_coeffs) or R_coeffs[start + 3] != 204):
        match = False
    if match:
        print(f"  MATCH at shift {start}: R({start+1})=8, R({start+2})=36, R({start+3})=204")
        if start + 4 < len(R_coeffs):
            print(f"  => H^4 = R({start+4}) = {R_coeffs[start+4]}")

# If no match, the linear ansatz is wrong. Try quadratic B.

# Let me try the parametric family:
# x*B*R^2 - B*R + 1 = 0 with B = 1+p*x
# and fit p to match the first 3 bar cohomology values.

print("\n--- Parametric search for sl_3 ---")
# R = [B - sqrt(B^2-4xB)] / (2xB) = [1 - sqrt(1-4x/B)] / (2x)
# R(x) = [1 - sqrt(1 - 4x/(1+px))] / (2x)

p_sym = Symbol('p')
R_param = (1 - sqrt(1 - 4*x/(1+p_sym*x))) / (2*x)

# Expand to get coefficients as functions of p:
R_param_series = series(R_param, x, 0, 10)
print("R(x) parametric series:")
for n in range(8):
    cn = R_param_series.coeff(x, n)
    cn_simplified = simplify(cn)
    print(f"  R({n}) = {cn_simplified}")

# For sl_2: need some R(k)=3, R(k+1)=6, R(k+2)=15 with p=1.
# Check:
print("\n--- Check sl_2 (p=1) ---")
for n in range(8):
    cn = R_param_series.coeff(x, n).subs(p_sym, 1)
    print(f"  R({n}) = {cn}")

# For sl_3: need R(k)=8, R(k+1)=36, R(k+2)=204.
# Try different p values and find which gives consecutive 8, 36, 204.
print("\n--- Search for p giving 8, 36, 204 ---")

# First, get the parametric R coefficients as functions of p
R_coeffs_p = []
for n in range(10):
    cn = simplify(R_param_series.coeff(x, n))
    R_coeffs_p.append(cn)

# The sequence R(0)=1, R(1)=1 always (from the series expansion).
# Actually R(0) might depend on p. Let me check.
print(f"R(0) = {R_coeffs_p[0]}")
print(f"R(1) = {R_coeffs_p[1]}")
print(f"R(2) = {R_coeffs_p[2]}")
print(f"R(3) = {R_coeffs_p[3]}")
print(f"R(4) = {R_coeffs_p[4]}")

# If R(1)=1 always, then we need R(k)=8 for some k>1.
# Let me solve R(k) = 8 for p.
for k in range(2, 8):
    eq = R_coeffs_p[k] - 8
    sols = solve(eq, p_sym)
    if sols:
        for s in sols:
            s_float = float(s.evalf())
            if abs(s_float) < 100:
                # Check R(k+1) and R(k+2)
                r_next = R_coeffs_p[k+1].subs(p_sym, s) if k+1 < len(R_coeffs_p) else None
                r_next2 = R_coeffs_p[k+2].subs(p_sym, s) if k+2 < len(R_coeffs_p) else None
                print(f"  R({k})=8 => p={s} (≈{s_float:.4f})")
                if r_next is not None:
                    print(f"    R({k+1}) = {simplify(r_next)}")
                if r_next2 is not None:
                    print(f"    R({k+2}) = {simplify(r_next2)}")
                if r_next == 36:
                    print(f"    *** R({k+1})=36 MATCH! ***")
                    if r_next2 == 204:
                        print(f"    *** R({k+2})=204 MATCH! ***")
                        if k+3 < len(R_coeffs_p):
                            h4 = simplify(R_coeffs_p[k+3].subs(p_sym, s))
                            print(f"    => H^4 = R({k+3}) = {h4}")
                        if k+4 < len(R_coeffs_p):
                            h5 = simplify(R_coeffs_p[k+4].subs(p_sym, s))
                            print(f"    => H^5 = R({k+4}) = {h5}")
