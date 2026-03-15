#!/usr/bin/env python3
"""Compute bar cohomology via the Koszul functional equation.

For a Koszul algebra A with Koszul dual A!:
    f_A(t) * f_{A!}(-t) = 1

where f_A(t) = 1 + sum dim(A_n) t^n, f_{A!}(t) = 1 + sum dim(A!_n) t^n.

The bar cohomology dimensions are H^n = dim(A!_n).

Strategy:
1. For sl_2: known H^n = R(n+3) (Riordan). Compute f_A from inversion.
2. Identify the pattern in f_A.
3. Generalize to sl_3 and predict H^4.
"""

from sympy import Rational, sqrt, symbols, series, S

x = symbols('x')

def invert_series(coeffs):
    """Compute 1/f(t) given coefficients of f(t)."""
    n = len(coeffs)
    g = coeffs
    a = [Rational(0)] * n
    a[0] = Rational(1, g[0])
    for i in range(1, n):
        s = sum(g[k] * a[i-k] for k in range(1, i+1))
        a[i] = -s * a[0]
    return a

# =============================================================
# sl_2: bar cohomology = Riordan numbers R(n+3)
# =============================================================
print("=" * 70)
print("sl_2 (d=3): H^n = R(n+3) = 3, 6, 15, 36, 91, 232, 603, ...")
print("=" * 70)

# f_{A!}(t) = 1 + 3t + 6t^2 + 15t^3 + 36t^4 + 91t^5 + ...
h_sl2 = [1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298]

# f_A(t) = 1/f_{A!}(-t)
# f_{A!}(-t) coefficients: (-1)^n * h_n
h_neg = [(-1)**n * h_sl2[n] for n in range(len(h_sl2))]
a_sl2 = invert_series(h_neg)
# a_n here are coefficients of 1/f_{A!}(-t), so f_A(t) = sum a_n t^n
print("\nf_A(t) = 1/f_{A!}(-t) for sl_2:")
for n in range(min(11, len(a_sl2))):
    print(f"  dim(A_{n}) = {a_sl2[n]}")

# Check: these should be positive and meaningful
print("\nf_A coefficients:", [int(a_sl2[n]) for n in range(11)])

# What is this sequence? 1, 3, 3, 6, 9, 18, 33, 63, 120, 231, ...
# Let me check OEIS-like patterns
print("\nRatios a_{n+1}/a_n:")
for n in range(9):
    if a_sl2[n] != 0:
        print(f"  a_{n+1}/a_{n} = {float(a_sl2[n+1]/a_sl2[n]):.4f}")

# Check: does f_A satisfy a nice algebraic equation?
# f_{A!} satisfies the Riordan-shifted equation.
# Since H(t) = f_{A!}(t) = 1 + 3t + 6t^2 + ..., let's find its algebraic equation.

# The generating function for H^n = R(n+3) where R satisfies x(1+x)R^2-(1+x)R+1=0.
# Let me derive the equation for Q(t) = sum R(n+3) t^n.
# R(x) = sum_{n>=0} R(n) x^n satisfies x(1+x)R^2 - (1+x)R + 1 = 0.
# So R(x) = (1+x-sqrt((1+x)(1-3x)))/(2x(1+x)).
#
# Now Q(t) = sum_{n>=0} R(n+3) t^n = ?
# Q(t) = (R(t/1) - R(0) - R(1)t/1 - R(2)(t/1)^2) / (t/1)^3 ... shifted by 3.
# Actually Q(t) = sum_{n>=0} R(n+3) t^n. This is not simply R(t) shifted.

# Better approach: find the algebraic equation for Q(t) = 1+3t+6t^2+15t^3+...
# by elimination from R's equation.

# Let me try: does Q satisfy a quadratic equation aQ^2 + bQ + c = 0
# with a,b,c low-degree polynomials?

# Fit Q to a quadratic with a = a0+a1*t+a2*t^2, b = b0+b1*t, c = c0+c1*t+c2*t^2
# Q = 1+3t+6t^2+15t^3+36t^4+91t^5+...

# If Q satisfies a*Q^2 + b*Q + c = 0, expand to order t^5 and solve for coefficients.
# Too many unknowns. Let me try the simplest: a=polynomial deg 1, b=deg 1, c=deg 0.

# a(t)*Q^2 + b(t)*Q + c = 0
# (a0+a1*t)*Q^2 + (b0+b1*t)*Q + c0 = 0
# 4 unknowns (a0,a1,b0,b1,c0 with one scaling freedom = 4 effective).
# Use Q values at t^0,...,t^3 to get 4 equations.

# t^0: a0*1 + b0*1 + c0 = 0
# t^1: a0*6 + a1*1 + b0*3 + b1*1 = 0  (coeff of t in a*Q^2+b*Q)
# ...

# Actually, let me use sympy to find the minimal polynomial.
from sympy import Poly, groebner

# Better: just check if Q satisfies known quadratic equations.
# For the Riordan numbers (full sequence), R satisfies x(1+x)R^2-(1+x)R+1=0.
# Let me derive what Q = sum R(n+3)t^n satisfies.

# From R(x) = 1/x^3 * (integral terms), it's complex. Let me just fit.

print("\n--- Finding algebraic equation for Q(t) = f_{A!}(t) ---")
# Try: alpha*t*Q^2 + beta*Q + gamma = 0 (simplest form)
# t^0: beta + gamma = 0 => gamma = -beta. WLOG beta=1, gamma=-1.
# So: alpha*t*Q^2 + Q - 1 = 0.
# t^1: alpha*1 + 3 = 0 => alpha = -3.
# Check t^2: -3*(2*3) + 6 = -18+6 = -12 ≠ 0. FAIL.

# Try: (a0+a1*t)*Q^2 + (b0+b1*t)*Q + (c0+c1*t) = 0
# 6 unknowns, 1 scaling = 5 effective. Use 5 equations from t^0,...,t^4.

# Q^2 = (1+3t+6t^2+15t^3+36t^4+...)^2
# = 1 + 6t + 21t^2 + 72t^3 + 222t^4 + ...

Q_coeffs = h_sl2[:8]
Q2_coeffs = [0]*8
for i in range(8):
    for j in range(8-i):
        Q2_coeffs[i+j] += Q_coeffs[i] * Q_coeffs[j]

print(f"Q coefficients: {Q_coeffs}")
print(f"Q^2 coefficients: {Q2_coeffs}")

# Equation: (a0+a1*t)*Q^2 + (b0+b1*t)*Q + (c0+c1*t) = 0
# Coefficient of t^n:
# sum_{k=0}^{n} a_k * Q2_{n-k} + sum_{k=0}^{n} b_k * Q_{n-k} + c_n = 0
# where a_k=0 for k>=2, b_k=0 for k>=2, c_k=0 for k>=2.

from sympy import Matrix, symbols as syms

a0, a1, b0, b1, c0, c1 = syms('a0 a1 b0 b1 c0 c1')

eqs = []
for n in range(6):
    eq = 0
    # a*Q^2 contribution
    if n < len(Q2_coeffs):
        eq += a0 * Q2_coeffs[n]
    if n >= 1 and n-1 < len(Q2_coeffs):
        eq += a1 * Q2_coeffs[n-1]
    # b*Q contribution
    if n < len(Q_coeffs):
        eq += b0 * Q_coeffs[n]
    if n >= 1 and n-1 < len(Q_coeffs):
        eq += b1 * Q_coeffs[n-1]
    # c contribution
    if n == 0:
        eq += c0
    if n == 1:
        eq += c1
    eqs.append(eq)

print("\nEquations for algebraic relation:")
for i, eq in enumerate(eqs):
    print(f"  t^{i}: {eq} = 0")

# Solve (set a0=1 for normalization):
from sympy import solve
sol = solve(eqs[:6], [a1, b0, b1, c0, c1], dict=True)
print(f"\nSolutions (with a0 free):")
for s in sol:
    print(f"  {s}")

# Substitute a0 = 1:
if sol:
    s = sol[0]
    for var in [a1, b0, b1, c0, c1]:
        val = s.get(var, var).subs(a0, 1)
        print(f"  {var} = {val}")

    # The equation is: (1+a1_val*t)*Q^2 + (b0_val+b1_val*t)*Q + (c0_val+c1_val*t) = 0
    a1_v = s[a1].subs(a0, 1)
    b0_v = s[b0].subs(a0, 1)
    b1_v = s[b1].subs(a0, 1)
    c0_v = s[c0].subs(a0, 1)
    c1_v = s[c1].subs(a0, 1)

    print(f"\nAlgebraic equation: (1+{a1_v}*t)*Q^2 + ({b0_v}+{b1_v}*t)*Q + ({c0_v}+{c1_v}*t) = 0")

    # Discriminant
    a_poly = 1 + a1_v*x
    b_poly = b0_v + b1_v*x
    c_poly = c0_v + c1_v*x
    disc = b_poly**2 - 4*a_poly*c_poly
    disc_expanded = disc.expand()
    print(f"Discriminant: {disc_expanded}")
    from sympy import factor as fac
    print(f"Factored: {fac(disc_expanded)}")

# =============================================================
# Now do the same for sl_3
# =============================================================
print("\n" + "=" * 70)
print("sl_3 (d=8): H^n = 8, 36, 204, ?, ...")
print("=" * 70)

# f_{A!}(t) = 1 + 8t + 36t^2 + 204t^3 + h4*t^4 + ...
# f_A(t) = 1/f_{A!}(-t)

h3 = [1, 8, 36, 204]
h3_neg = [(-1)**n * h3[n] for n in range(len(h3))]
a3 = invert_series(h3_neg)
print("\nKnown f_A coefficients for sl_3:")
for n in range(4):
    print(f"  dim(A_{n}) = {a3[n]}")

# f_A(t) = 1 + 8t + 28t^2 + 140t^3 + ...
# Check: 28 = C(8,2) = 8*7/2. 140 = ?

print(f"\nPattern check: a_1={a3[1]}, a_2={a3[2]}")
print(f"  C(8,2) = {8*7//2} {'✓' if a3[2]==28 else '✗'}")
print(f"  a_3 = {a3[3]}")
print(f"  C(8,3) = {8*7*6//6}")

# For sl_2: a_n sequence is 1, 3, 3, 6, 9, 18, 33, 63, 120, 231, ...
# These are signed Motzkin numbers! M(n) = 1,1,2,4,9,21,51,127,...
# a_n(sl_2) = Motzkin(n-1) + Motzkin(n)? Let's check.
motzkin = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]
print("\nMotzkin numbers:", motzkin)
print("sl_2 A-coefficients:", [int(a_sl2[n]) for n in range(10)])
print("M(n)+M(n-1):", [motzkin[0]] + [motzkin[n]+motzkin[n-1] for n in range(1,10)])
# Hmm: 1+1=2≠3. Not this.

# Let me check: for sl_2, does A(t) satisfy a nice equation?
print("\n--- Checking A(t) algebraic equation for sl_2 ---")
# A = 1/(1-3t+6t^2-15t^3+...) = 1/f_{A!}(-t)
# f_{A!}(t) satisfies: a(t)*Q^2 + b(t)*Q + c(t) = 0
# If A = 1/Q(-t), then Q(-t) = 1/A.
# Substitute Q = 1/A, t -> -t in the equation:
# a(-t)/A^2 + b(-t)/A + c(-t) = 0
# Multiply by A^2: a(-t) + b(-t)*A + c(-t)*A^2 = 0
# So A satisfies: c(-t)*A^2 + b(-t)*A + a(-t) = 0

# =============================================================
# Generalize: try to find the algebraic equation for f_{A!}(t) of sl_3
# =============================================================
print("\n" + "=" * 70)
print("GENERALIZATION: algebraic equation for f_{A!}(t)")
print("=" * 70)

# For sl_2: Q = f_{A!} satisfies the equation we found above.
# Key observation: the discriminant factors as (1-d*t)(1+alpha*t) for some alpha.
# For sl_2 (d=3): disc should have root at 1/3.

# For sl_3 (d=8): disc should have root at 1/8.

# Let's try the ANSATZ: Q satisfies
# t*Q^2 + (b0 + b1*t)*Q + (c0 + c1*t) = 0
# with discriminant (b0+b1*t)^2 - 4*t*(c0+c1*t) having root at t=1/d.

# Using Q(0)=1: b0 + c0 = 0. (Since t*Q^2 vanishes at t=0.)
# So c0 = -b0. WLOG b0 = -1: b0=-1, c0=1.

# t*Q^2 + (-1+b1*t)*Q + (1+c1*t) = 0

# At t^1: 1 + (-1)*h1 + b1*1 + c1 = 0
# 1 - h1 + b1 + c1 = 0 => b1 + c1 = h1 - 1 = d - 1

# Discriminant: (-1+b1*t)^2 - 4*t*(1+c1*t) = 1-2*b1*t+b1^2*t^2 - 4*t - 4*c1*t^2
# = 1 - (2*b1+4)*t + (b1^2-4*c1)*t^2

# Root at t=1/d: 1 - (2*b1+4)/d + (b1^2-4*c1)/d^2 = 0

# Two equations: b1+c1 = d-1 and d^2 - d(2*b1+4) + b1^2-4*c1 = 0
# From first: c1 = d-1-b1.
# Substitute: d^2 - 2*d*b1 - 4*d + b1^2 - 4*(d-1-b1) = 0
# d^2 - 2*d*b1 - 4*d + b1^2 - 4*d + 4 + 4*b1 = 0
# b1^2 + (4-2*d)*b1 + (d^2-8*d+4) = 0
# b1 = [(2*d-4) ± sqrt((2*d-4)^2 - 4*(d^2-8*d+4))]/2
# disc_b1 = 4*d^2-16*d+16 - 4*d^2+32*d-16 = 16*d
# b1 = [(2*d-4) ± 4*sqrt(d)]/2 = (d-2) ± 2*sqrt(d)

print("ANSATZ: t*Q^2 + (-1+b1*t)*Q + (1+c1*t) = 0")
print("with b1 + c1 = d-1 and disc root at t=1/d")

for d_val in [3, 8]:
    from sympy import sqrt as ssqrt
    b1_plus = (d_val - 2) + 2*ssqrt(d_val)
    b1_minus = (d_val - 2) - 2*ssqrt(d_val)
    print(f"\nd={d_val}:")
    print(f"  b1 = (d-2) ± 2*sqrt(d) = {d_val-2} ± {2*ssqrt(d_val)}")
    print(f"  b1+ = {b1_plus.simplify()} = {float(b1_plus):.4f}")
    print(f"  b1- = {b1_minus.simplify()} = {float(b1_minus):.4f}")

    for b1_val in [b1_plus, b1_minus]:
        c1_val = d_val - 1 - b1_val
        print(f"\n  b1={float(b1_val):.4f}, c1={float(c1_val):.4f}")

        # Compute Q series from the quadratic:
        # t*Q^2 + (-1+b1*t)*Q + (1+c1*t) = 0
        # Q = [1-b1*t ± sqrt(disc)] / (2t)
        # disc = (1-b1*t)^2 - 4*t*(1+c1*t)
        disc_eq = (1-b1_val*x)**2 - 4*x*(1+c1_val*x)
        disc_eq = disc_eq.expand()

        Q_plus = ((1-b1_val*x) + sqrt(disc_eq)) / (2*x)
        Q_minus = ((1-b1_val*x) - sqrt(disc_eq)) / (2*x)

        try:
            Q_p_series = series(Q_plus, x, 0, 6)
            Q_m_series = series(Q_minus, x, 0, 6)

            q_p = [Q_p_series.coeff(x, n) for n in range(6)]
            q_m = [Q_m_series.coeff(x, n) for n in range(6)]

            # Check which matches known values
            if d_val == 3:
                expected = [1, 3, 6, 15, 36]
            else:
                expected = [1, 8, 36, 204, None]

            match_p = all(q_p[n] == expected[n] for n in range(min(len(expected), 4)) if expected[n] is not None)
            match_m = all(q_m[n] == expected[n] for n in range(min(len(expected), 4)) if expected[n] is not None)

            if match_p or True:  # Print all for debugging
                print(f"    Q+ series: {[float(c) if c!=0 else 0 for c in q_p[:5]]}")
            if match_m or True:
                print(f"    Q- series: {[float(c) if c!=0 else 0 for c in q_m[:5]]}")

            if match_p:
                print(f"    *** Q+ MATCHES! ***")
                if d_val == 8 and len(q_p) > 4:
                    print(f"    PREDICTION: H^4(sl_3) = {q_p[4]}")
            if match_m:
                print(f"    *** Q- MATCHES! ***")
                if d_val == 8 and len(q_m) > 4:
                    print(f"    PREDICTION: H^4(sl_3) = {q_m[4]}")
        except Exception as e:
            print(f"    Error: {e}")

# =============================================================
# Also try more general ansatz
# =============================================================
print("\n" + "=" * 70)
print("MORE GENERAL ANSATZ")
print("=" * 70)

# Try: (1+a*t)*Q^2 + (b0+b1*t)*Q + (c0+c1*t) = 0
# 5 unknowns (a, b0, b1, c0, c1) with 1 scaling = 4 effective.
# + constraint: disc root at 1/d.

# Use Q(0)=1: c0 = -(1+0)*1 - b0*1 = -1-b0. Or: (1)*1 + b0*1 + c0 = 0 (t^0 term is 0).
# Wait: at t=0: (1)*Q(0)^2 + b0*Q(0) + c0 = 0 => 1+b0+c0=0 => c0=-1-b0.

# WLOG set b0=-1: c0=0. Then:
# (1+a*t)*Q^2 + (-1+b1*t)*Q + c1*t = 0
# t^0: 1-1+0=0 ✓
# t^1: a + 6 + (-1)*h1 + b1 + c1 = 0
#       (where h1=3 for sl_2 or h1=8 for sl_3)
# Wait let me be more careful.

# Q^2 = 1 + 2h1*t + (h1^2+2h2)*t^2 + ...
# (1+a*t)*Q^2: at t^1 = a + 2*h1
# (-1+b1*t)*Q: at t^1 = -h1 + b1
# c1*t: at t^1 = c1
# Total: a + 2*h1 - h1 + b1 + c1 = a + h1 + b1 + c1 = 0
# So a + b1 + c1 = -h1

# For sl_2 (h1=3): a + b1 + c1 = -3
# For sl_3 (h1=8): a + b1 + c1 = -8

# At t^2:
# (1+a*t)*Q^2 at t^2: h1^2+2*h2 + a*2*h1
# (-1+b1*t)*Q at t^2: -h2 + b1*h1
# c1*t at t^2: 0
# Total: h1^2+2*h2+2*a*h1-h2+b1*h1 = h1^2+h2+2*a*h1+b1*h1 = 0
# h1^2+h2+(2*a+b1)*h1 = 0 => 2*a+b1 = -(h1^2+h2)/h1 = -(h1+h2/h1)

# For sl_2: 2a+b1 = -(9+6)/3 = -5
# Combined with a+b1+c1=-3: from 2a+b1=-5 => b1=-5-2a.
# a+(-5-2a)+c1=-3 => -a-5+c1=-3 => c1=a+2.

# Discriminant:
# disc = (-1+b1*t)^2 - 4*(1+a*t)*c1*t
# = 1-2*b1*t+b1^2*t^2 - 4*c1*t - 4*a*c1*t^2
# = 1 - (2*b1+4*c1)*t + (b1^2-4*a*c1)*t^2

# Root at t=1/d: 1 - (2*b1+4*c1)/d + (b1^2-4*a*c1)/d^2 = 0

# For sl_2 (d=3): with b1=-5-2a, c1=a+2:
# 2*b1+4*c1 = 2*(-5-2a)+4*(a+2) = -10-4a+4a+8 = -2
# b1^2-4*a*c1 = (-5-2a)^2 - 4*a*(a+2) = 25+20a+4a^2-4a^2-8a = 25+12a
# disc root at 1/3: 1 - (-2)/3 + (25+12a)/9 = 0
# 1 + 2/3 + (25+12a)/9 = 0
# 9/9 + 6/9 + (25+12a)/9 = 0
# 9+6+25+12a = 0 => 40+12a=0 => a=-10/3

# b1 = -5-2*(-10/3) = -5+20/3 = 5/3
# c1 = -10/3+2 = -4/3
# disc = 1-(-2)*t+(25+12*(-10/3))*t^2 = 1+2t+(25-40)*t^2 = 1+2t-15t^2... hmm
# Let me check: disc should be (1-3t)(1+something*t).
# 1+2t-15t^2 = -(15t^2-2t-1) = -(5t+1)(3t-1) = (1-3t)(1+5t). Wait:
# -(15t^2-2t-1): 15t^2-2t-1 = (5t+1)(3t-1). So -1*(5t+1)(3t-1) = (1-3t)(5t+1).
# Hmm: (1-3t)(5t+1) = 5t+1-15t^2-3t = 1+2t-15t^2. ✓!

# But we need disc = (1-3t)(1+alpha*t) with integer alpha.
# disc = (1-3t)(1+5t). So alpha=5. Hmm.

# Now check: does the equation give the right Q?
# (1-10t/3)*Q^2 + (-1+5t/3)*Q + (-4t/3) = 0
# Multiply by -3: (-3+10t)*Q^2 + (3-5t)*Q + 4t = 0
# Or: (10t-3)*Q^2 + (3-5t)*Q + 4t = 0

# Check Q=1+3t+6t^2+15t^3+36t^4+91t^5:
print("\n--- Verifying sl_2 equation ---")
for a_val_num, a_val_den in [(-10, 3)]:
    a_v = Rational(a_val_num, a_val_den)
    b1_v = -5 - 2*a_v
    c1_v = a_v + 2
    print(f"a={a_v}, b1={b1_v}, c1={c1_v}")
    # Equation: (1+a*t)*Q^2 + (-1+b1*t)*Q + c1*t = 0
    # Let me verify with known Q coefficients
    for n_max in range(6):
        # Compute coeff of t^n_max in (1+a*t)*Q^2+(-1+b1*t)*Q+c1*t
        val = 0
        for k in range(n_max+1):
            if k == 0:
                val += 1 * Q2_coeffs[n_max]
            if k == 1 and n_max >= 1:
                val += a_v * Q2_coeffs[n_max-1]
            if k == 0:
                val += (-1) * Q_coeffs[n_max]
            if k == 1 and n_max >= 1:
                val += b1_v * Q_coeffs[n_max-1]
            # c1*t: only at n_max=1
        if n_max == 1:
            val += c1_v
        # Hmm this is getting messy. Let me just compute directly.
        pass

# Let me just do it properly with sympy
t = x
Q_poly = sum(h_sl2[n]*t**n for n in range(8))
a_v = Rational(-10, 3)
b1_v = Rational(5, 3)
c1_v = Rational(-4, 3)
eq_check = (1 + a_v*t)*Q_poly**2 + (-1 + b1_v*t)*Q_poly + c1_v*t
eq_expanded = eq_check.expand()
print("Checking equation coefficients:")
for n in range(7):
    print(f"  t^{n}: {eq_expanded.coeff(t, n)}")

# =============================================================
# Apply to sl_3
# =============================================================
print("\n" + "=" * 70)
print("APPLYING TO sl_3 (d=8)")
print("=" * 70)

# For sl_3: h1=8, h2=36, h3=204, d=8
# a + b1 + c1 = -8
# 2a + b1 = -(h1 + h2/h1) = -(8+36/8) = -(8+9/2) = -25/2
# b1 = -25/2 - 2a
# c1 = -8 - a - b1 = -8 - a + 25/2 + 2a = a + 9/2

# Disc root at t=1/8:
# 2*b1+4*c1 = 2*(-25/2-2a)+4*(a+9/2) = -25-4a+4a+18 = -7
# b1^2-4*a*c1 = (-25/2-2a)^2 - 4*a*(a+9/2) = 625/4+50a+4a^2 - 4a^2-18a = 625/4+32a
# Root at 1/8: 1-(-7)/8+(625/4+32a)/64 = 0
# 1+7/8+(625/4+32a)/64 = 0
# 64/64+56/64+(625/4+32a)/64 = 0
# Wait: (625/4+32a)/64 = 625/256+32a/64 = 625/256+a/2
# 1+7/8+625/256+a/2 = 0
# 256/256+224/256+625/256+128a/256 = 0
# (256+224+625+128a)/256 = 0
# 1105+128a = 0
# a = -1105/128

a_sl3 = Rational(-1105, 128)
b1_sl3 = Rational(-25, 2) - 2*a_sl3
c1_sl3 = a_sl3 + Rational(9, 2)

print(f"a = {a_sl3}")
print(f"b1 = {b1_sl3}")
print(f"c1 = {c1_sl3}")

# Equation: (1+a*t)*Q^2 + (-1+b1*t)*Q + c1*t = 0
# disc = 1 - (-7)*t + (625/4+32*a)*t^2 = 1+7t+(625/4+32*(-1105/128))*t^2
disc_const = Rational(625,4) + 32*a_sl3
print(f"disc = 1 + 7t + {disc_const}*t^2")

# = 1 + 7t + (625/4 - 35360/128)*t^2
# 625/4 = 20000/128. 32*(-1105/128) = -35360/128.
# disc_const = (20000-35360)/128 = -15360/128 = -120

disc_const_val = disc_const
print(f"disc constant term of t^2: {disc_const_val}")
print(f"disc = 1 + 7t - 120*t^2 = (1-8t)(1+15t)? Let's check:")
print(f"  (1-8t)(1+15t) = {((1-8*t)*(1+15*t)).expand()}")

disc_sl3 = 1 + 7*t - 120*t**2
disc_factored = (1 - 8*t)*(1 + 15*t)
print(f"  disc = {disc_sl3} = {disc_factored.expand()} {'✓' if disc_sl3 == disc_factored.expand() else '✗'}")

# Great! disc = (1-8t)(1+15t). Root at t=1/8 ✓.
# Now compute Q from the equation:

print("\n--- Computing Q (= f_{A!}) for sl_3 ---")
# (1+a*t)*Q^2 + (-1+b1*t)*Q + c1*t = 0
# Q = (1-b1*t - sqrt(disc_full)) / (2*(1+a*t))
# where disc_full = (-1+b1*t)^2 - 4*(1+a*t)*(c1*t)
#                 = 1-2*b1*t+b1^2*t^2 - 4*c1*t-4*a*c1*t^2
# We already know disc = 1+7t-120t^2 (factoring out common factors)

# Actually disc_full = (-1+b1*t)^2 - 4*(1+a*t)*(c1*t)
disc_full = (-1+b1_sl3*t)**2 - 4*(1+a_sl3*t)*(c1_sl3*t)
disc_full_exp = disc_full.expand()
print(f"disc_full = {disc_full_exp}")

# Q = [1-b1*t ± sqrt(disc_full)] / (2*(1+a*t))
# Pick the branch where Q(0) = 1.
# At t=0: Q = [1 ± 1]/2. Pick +: Q=(1+1)/2=1. ✓

Q_sl3 = (1 - b1_sl3*t + sqrt(disc_full_exp)) / (2*(1+a_sl3*t))
Q_sl3_series = series(Q_sl3, t, 0, 8)
print(f"\nQ series for sl_3:")
for n in range(8):
    c = Q_sl3_series.coeff(t, n)
    c_simplified = c.simplify()
    print(f"  H^{n} = {c_simplified}")

# Verify against known values
print("\nVerification:")
print(f"  H^0 = 1 ✓" if Q_sl3_series.coeff(t, 0) == 1 else "  H^0 FAIL")
print(f"  H^1 = 8 {'✓' if Q_sl3_series.coeff(t, 1) == 8 else '✗'}")
print(f"  H^2 = 36 {'✓' if Q_sl3_series.coeff(t, 2) == 36 else '✗'}")
print(f"  H^3 = 204 {'✓' if Q_sl3_series.coeff(t, 3) == 204 else '✗'}")

h4_predicted = Q_sl3_series.coeff(t, 4)
print(f"\n*** PREDICTION: H^4(sl_3) = {h4_predicted.simplify()} ***")
h5_predicted = Q_sl3_series.coeff(t, 5)
print(f"*** PREDICTION: H^5(sl_3) = {h5_predicted.simplify()} ***")

# Also verify the t^3 coefficient of the equation
print("\n--- Verify equation at t^3 ---")
Q_test = 1 + 8*t + 36*t**2 + 204*t**3
eq_val = (1+a_sl3*t)*Q_test**2 + (-1+b1_sl3*t)*Q_test + c1_sl3*t
eq_expanded = eq_val.expand()
for n in range(5):
    print(f"  t^{n}: {eq_expanded.coeff(t, n)}")
