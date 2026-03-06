#!/usr/bin/env python3
"""Find the algebraic generating function for sl_3 bar cohomology.

Known: P(x) = 8x + 36x^2 + 204x^3 + a_4 x^4 + ...
From the manuscript: P is algebraic, growth rate 8^n, radius of convergence 1/8.

For sl_2: P satisfies x(1+x)P^2 - (1+x)P + 1 = 0
         discriminant: (1+x)^2 - 4x(1+x) = (1+x)(1-3x) = 1-2x-3x^2

Strategy: fit P_{sl3} to a quadratic equation a(x)P^2 + b(x)P + c(x) = 0
where a,b,c are polynomials with discriminant having root at x=1/8.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, resultant, Poly, simplify, QQ, ZZ,
                   cancel, collect, together)
from sympy import S as SS

x = symbols('x')

# First verify sl_2
print("=== Verifying sl_2 ===")
Delta2 = 1 - 2*x - 3*x**2
P_sl2 = (1 + x - sqrt(Delta2)) / (2*x*(1+x))
coeffs_sl2 = [P_sl2.series(x, 0, n+1).coeff(x, n) for n in range(1, 11)]
print(f"sl_2 coefficients: {coeffs_sl2}")
print(f"Expected Riordan: [3, 6, 15, 36, 91, 232, 603, ...]")

# Now for sl_3, try ansatz:
# P = (f(x) - sqrt(Delta_3(x))) / g(x)
# where Delta_3 = 1 - a*x - b*x^2 has root at x=1/8

# If Delta_3(1/8) = 0: 1 - a/8 - b/64 = 0 => b = 64 - 8a
# Also need growth rate 8^n, so radius of convergence = 1/8 => smallest positive root of Delta at 1/8

# Discriminant must also have a negative root for the generating function to be well-defined on (0, 1/8).

# For sl_2: Delta = 1-2x-3x^2 = (1-3x)(1+x), roots 1/3 and -1.
# Radius = 1/3 = 1/dim(g).

# For sl_3: radius = 1/8 = 1/dim(g).
# Delta_3 = (1-8x)(1+alpha*x) = 1 + (alpha-8)x - 8*alpha*x^2
# So a = 8-alpha, b = 8*alpha, and b = 64-8a => 8*alpha = 64-8(8-alpha) = 64-64+8alpha = 8alpha. ✓ (always satisfied)

# The ansatz for P:
# For sl_2: P = (1+x-sqrt(Delta))/(2x(1+x))
#   = (1+x-sqrt((1-3x)(1+x)))/(2x(1+x))
# The denominator 2x(1+x) uses the negative root -1 of the discriminant.

# For sl_3, try: P = (f(x) - sqrt((1-8x)(1+alpha*x))) / (something)

# General quadratic: A(x)*P^2 + B(x)*P + C(x) = 0
# => P = (-B ± sqrt(B^2 - 4AC)) / (2A)
# Discriminant = B^2 - 4AC must factor as proportional to (1-8x)(1+alpha*x)

# Let's parametrize by alpha and fit to the known coefficients.
# Try A = x*(1+alpha*x), B = -(1+beta*x), C = 1
# (generalization of sl_2 where A=x(1+x), B=-(1+x), C=1, i.e. alpha=beta=1)

print("\n=== Fitting sl_3 ===")

# Ansatz: x*(1+alpha*x)*P^2 - (1+beta*x)*P + 1 = 0
# Coefficients of P = sum a_n x^n with a_1=8, a_2=36, a_3=204

alpha, beta = symbols('alpha beta')

# P = a1*x + a2*x^2 + a3*x^3 + ...
a1, a2, a3 = 8, 36, 204

# Substitute and collect powers of x:
# x*(1+alpha*x)*(a1*x + a2*x^2 + ...)^2 - (1+beta*x)*(a1*x + a2*x^2 + ...) + 1 = 0

# x^0: +1 = 0? No! The equation has constant term 1, which is nonzero.
# Wait, for sl_2: x(1+x)P^2 - (1+x)P + 1 = 0
# P = 1 + 2x + 5x^2 + 15x^3 + ... (if we include constant term?)
# Actually let me recheck. P_sl2 = (1+x-sqrt(1-2x-3x^2))/(2x(1+x))
# At x=0: numerator = 1+0-1 = 0, denominator = 0. L'Hopital.

# Let me compute P_sl2 series:
print("P_sl2 series:")
P_sl2_series = series(P_sl2, x, 0, 8)
print(f"  {P_sl2_series}")

# So P_sl2 starts at x^0 with coefficient 1!
# P_sl2 = 1 + x + 3x^2 + ... WAIT no, the bar cohomology starts at degree 1.
# H^0 = 1 (vacuum), H^1 = 3, H^2 = 6, ...
# So P(x) = 1 + 3x + 6x^2 + 15x^3 + 36x^4 + 91x^5 + ...
# But the manuscript defines P(x) = sum_{n>=1} dim H^n * x^n
# Let me re-read...

# Actually from the manuscript eq:gf-sl2-riordan:
# P(x) = (1+x-sqrt(1-2x-3x^2)) / (2x(1+x))
# This should give the generating function starting from n=1.

# Let me compute:
print("\nComputing P_sl2 = (1+x-sqrt(1-2x-3x^2))/(2x(1+x)) as series:")
num = 1 + x - sqrt(1 - 2*x - 3*x**2)
den = 2*x*(1+x)
# Direct series expansion
num_series = series(num, x, 0, 10)
print(f"  Numerator series: {num_series}")

# Numerator: 1+x - sqrt(1-2x-3x^2)
# sqrt(1-2x-3x^2) = 1 - x - 2x^2 - 2x^3 - 5x^4 - 14x^5 - ...
# 1+x - (1-x-2x^2-...) = 2x + 2x^2 + 2x^3 + 5x^4 + ...
# Divide by 2x(1+x) = 2x + 2x^2:
# P = (2x + 2x^2 + 2x^3 + ...)/(2x + 2x^2)
# P = 1 + 0*x + ...? Let me just compute.

# Use sympy to get the correct expansion
P_formal = num / den
# Can't directly series divide, let me use a different approach
# P satisfies x(1+x)P^2 - (1+x)P + 1 = 0
# So P = [(1+x) - sqrt((1+x)^2 - 4x(1+x))] / (2x(1+x))
#       = [(1+x) - sqrt((1+x)(1-3x))] / (2x(1+x))
#       = [1 - sqrt((1-3x)/(1+x))] / (2x)

# Let h = sqrt((1-3x)/(1+x))
# h = 1 - 2x - x^2/2 - 3x^3/2 - ... (need to compute)
# P = (1-h)/(2x)

h = sqrt((1-3*x)/(1+x))
P_alt = (1 - h) / (2*x)
P_alt_series = series(P_alt, x, 0, 8)
print(f"\n  P_sl2 = (1-sqrt((1-3x)/(1+x)))/(2x) = {P_alt_series}")

# OK so P_sl2 starts with constant term 1, giving H^0=1, H^1=?, etc.
# But the manuscript says P = sum_{n>=1} H^n * x^n
# So maybe the manuscript's P is x*P_alt? Or the indexing is different?

# Let me just extract coefficients from P_alt
for n in range(8):
    c = P_alt_series.coeff(x, n)
    print(f"  x^{n}: {c}")

# Now for sl_3, let me try P = (1 - sqrt((1-8x)/(1+alpha*x))) / (2x)
# and fit alpha to the known values.
print("\n=== Trying P_sl3 = (1 - sqrt((1-8x)/(1+alpha*x))) / (2x) ===")

for n in range(8):
    c = P_alt_series.coeff(x, n)
    if n == 0:
        print(f"  sl_2: x^0 = {c} (this is R(3) = 1)")
    else:
        print(f"  sl_2: x^{n} = {c} (R({n+3}))")

# For sl_3:
alpha_val = symbols('alpha_val', positive=True)
P_sl3_try = (1 - sqrt((1 - 8*x) / (1 + alpha_val*x))) / (2*x)
P_sl3_series = series(P_sl3_try, x, 0, 6)

# Extract coefficients
c0 = P_sl3_series.coeff(x, 0)
c1 = P_sl3_series.coeff(x, 1)
c2 = P_sl3_series.coeff(x, 2)
c3 = P_sl3_series.coeff(x, 3)

print(f"\n  Coefficient of x^0: {simplify(c0)}")
print(f"  Coefficient of x^1: {simplify(c1)}")
print(f"  Coefficient of x^2: {simplify(c2)}")
print(f"  Coefficient of x^3: {simplify(c3)}")

# The manuscript says: H^1 = 8, H^2 = 36, H^3 = 204
# These correspond to n=1, 2, 3 in the bar degree.
# If P_sl3 starts at x^0 with H^0=1, then:
# x^0 coeff = 1 (vacuum) -- probably not counted in the manuscript's table
# x^1 coeff = H^1 = 8
# x^2 coeff = H^2 = 36
# x^3 coeff = H^3 = 204

# For sl_2: x^0=1, x^1=1, x^2=3, x^3=6
# But expected H^1=3, H^2=6, H^3=15 (Riordan R(4)=3, R(5)=6, R(6)=15)
# So x^0=1, x^1=1, x^2=3 DON'T match H^1=3, H^2=6

# There's an indexing mismatch. Let me recheck the manuscript formula.

print("\n=== Checking manuscript formula directly ===")
# eq:gf-sl2-riordan:
# P_{sl_2}(x) = (1 + x - sqrt(1-2x-3x^2)) / (2x(1+x))
# = sum_{n>=1} dim H^n * x^n

# Let me compute this directly, handling the singularity at x=0
# Numerator at x=0: 1+0-1=0, denominator at x=0: 0. Use L'Hopital or series.

# sqrt(1-2x-3x^2) = 1 + (-2-6x)/(2*1) * x + ... no, let me just use sympy
s = sqrt(1 - 2*x - 3*x**2)
s_series = series(s, x, 0, 10)
print(f"sqrt(1-2x-3x^2) = {s_series}")

num_series = series(1 + x - s, x, 0, 10)
print(f"1 + x - sqrt(...) = {num_series}")

# Now divide by 2x(1+x) = 2x + 2x^2
# P = (num_series) / (2x(1+x))
# num starts at x^1 (since 1+x - sqrt at x=0 is 0)
# So P starts at x^0

# Manual: num = 2x + 4x^2 + 10x^3 + ...?? Let me read off
for n in range(10):
    print(f"  num coeff x^{n}: {num_series.coeff(x, n)}")
