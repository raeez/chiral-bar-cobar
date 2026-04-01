r"""Supplementary computations for the spectral curve investigation.

1. Numerical verification of shadow coefficients from sqrt(Q_L) expansion.
2. The c-direction Gauss-Manin connection and its monodromy.
3. The TWO-PARAMETER Gauss-Manin: nabla_{(t,c)} on the (t,c)-base.
4. Numerical EO vs shadow at specific c values.
5. The surface S and its arithmetic.
"""

import sys
import os
sys.path.insert(0, os.path.expanduser('~/chiral-bar-cobar'))

from sympy import (
    Symbol, Rational, sqrt, simplify, cancel, expand, factor,
    diff, integrate, log, pi, I, oo, Abs, N,
    series, collect, Poly, solve, degree, fraction,
    numer, denom, together, apart, limit,
    binomial, factorial, bernoulli, zeta,
    Matrix, eye, zeros as sym_zeros,
)

c = Symbol('c', positive=True)  # Use positive assumption for sqrt(c^2) = c
t = Symbol('t')

def virasoro_QL():
    alpha_c = (180*c + 872) / (5*c + 22)
    return c**2 + 12*c*t + alpha_c * t**2

def virasoro_alpha(c_sym=c):
    return (180*c_sym + 872) / (5*c_sym + 22)

def virasoro_shadow_data():
    kappa = c / 2
    alpha = Rational(2)
    S4 = Rational(10) / (c * (5*c + 22))
    Delta = 8*kappa*S4
    return kappa, alpha, S4, cancel(Delta)


print("=" * 80)
print("SUPPLEMENT 1: SHADOW COEFFICIENT VERIFICATION (c > 0)")
print("=" * 80)
print()

QL = virasoro_QL()
# With c positive, sqrt(c^2) = c
sqrt_QL_series = series(sqrt(QL), t, 0, n=10)

print("Shadow coefficients S_r from sqrt(Q_L) expansion (c > 0):")
shadow_coefficients = {}
for k in range(10):
    coeff_k = sqrt_QL_series.coeff(t, k)
    coeff_k_simplified = cancel(coeff_k)
    S_val = cancel(coeff_k_simplified / (k+2))
    shadow_coefficients[k+2] = S_val
    print(f"  S_{k+2} = {S_val}")

print()

# Verify against known values
kappa, alpha_val, S4, Delta = virasoro_shadow_data()
print("Verification:")
print(f"  S_2 = kappa = c/2: {cancel(shadow_coefficients[2] - kappa) == 0}")
print(f"  S_3 = 2: {cancel(shadow_coefficients[3] - 2) == 0}")
print(f"  S_4 = 10/(c(5c+22)): {cancel(shadow_coefficients[4] - S4) == 0}")
print()

# Compute S_5 from the recursion and verify
# S_5 = -P/(2*5) * [c_{3,4} * 3*4 * S_3 * S_4] = -(2/c)/(10) * 12 * 2 * S_4
#      = -24*S_4/(5c) = -24*10/(5c*c*(5c+22)) = -240/(5c^2(5c+22)) = -48/(c^2(5c+22))
S5_from_recursion = cancel(-Rational(48) / (c**2 * (5*c + 22)))
print(f"  S_5 from recursion: {S5_from_recursion}")
print(f"  S_5 from series:    {shadow_coefficients[5]}")
print(f"  Match: {cancel(shadow_coefficients[5] - S5_from_recursion) == 0}")
print()


print("=" * 80)
print("SUPPLEMENT 2: c-DIRECTION GAUSS-MANIN CONNECTION")
print("=" * 80)
print()

# Consider the sqrt local system in the c-direction.
# Fix t = t_0 and look at f(c) = sqrt(Q_L(t_0; c)) as a function of c.
# Q_L(t_0; c) = c^2 + 12c*t_0 + alpha(c)*t_0^2
# This is a RATIONAL function of c (not polynomial, due to alpha(c)).
#
# The "c-connection" for this sqrt local system is:
# nabla^c = d/dc - (dQ_L/dc) / (2*Q_L)
# with flat sections sqrt(Q_L(t_0; c) / Q_L(t_0; c_0)).

dQL_dc = diff(QL, c)
omega_c = cancel(dQL_dc / (2*QL))
print(f"c-direction connection form:")
print(f"  omega_c = (dQ_L/dc) / (2Q_L)")
print(f"  dQ_L/dc = {cancel(dQL_dc)}")
print()

# The c-connection has singularities where Q_L = 0 in c.
# For fixed t, Q_L(t;c) = 0 defines a curve in the (c,t)-plane.
# We already know: (5c+22)*Q_L = 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2
# Setting t=0: Q_L(0;c) = c^2 = 0 => c = 0 (double root).
# For general t: the zeros of Q_L in c are roots of a cubic.

# The discriminant of the cubic (5c+22)Q_L in c:
# Need to use unsimplified form to avoid rational expressions in c
P_expr = expand(5*c**3 + (60*t+22)*c**2 + (180*t**2+264*t)*c + 872*t**2)
P_c = Poly(P_expr, c)
print(f"P(c) := (5c+22)*Q_L(t;c) as polynomial in c:")
print(f"  Degree: {P_c.degree()}")
print(f"  Coefficients: {P_c.all_coeffs()}")
print()

# For the cubic 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2:
# At t=0: 5c^3 + 22c^2 = c^2(5c+22), roots c=0 (double), c=-22/5.
# This confirms: at t=0, Q_L vanishes at c=0 (where kappa=0).

print("Zeros of P(c) at t=0: c=0 (double), c=-22/5 (simple)")
print()

# The TWO-PARAMETER connection on the (t,c)-plane:
# nabla = d - omega_t dt - omega_c dc
# where omega_t = Q_L'_t/(2Q_L), omega_c = (dQ_L/dc)/(2Q_L).
# This is the FULL Gauss-Manin connection of the rank-1 sqrt local system
# on the base (t,c) minus the discriminant locus {Q_L = 0}.
#
# FLATNESS: nabla^2 = 0 iff d(omega_t dt + omega_c dc) = 0, which holds
# automatically since omega_t dt + omega_c dc = d(log sqrt(Q_L)).

omega_t = cancel(diff(QL, t) / (2*QL))
print(f"t-direction: omega_t = Q_L'/2Q_L")
print(f"c-direction: omega_c = (dQ_L/dc)/(2Q_L)")
print(f"Both are components of d(log sqrt(Q_L)), hence the 2-form is closed.")
print(f"The connection is FLAT on the complement of {{Q_L = 0}} in the (t,c)-plane.")
print()

# The discriminant locus {Q_L = 0} in the (t,c)-plane:
# (5c+22)*Q_L = 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2 = 0
# This is a degree-3 curve in c and degree-2 curve in t.
# Union with the pole: c = -22/5.
# Total discriminant divisor D = {(5c+22)*Q_L = 0} union {5c+22 = 0}.

print("Discriminant locus in the (t,c)-plane:")
print("  D = {P(c,t) = 0} union {c = -22/5}")
print("  where P(c,t) = 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2")
print()


print("=" * 80)
print("SUPPLEMENT 3: MONODROMY OF THE c-FAMILY")
print("=" * 80)
print()

# The period omega(c) = pi * sqrt((5c+22)/(45c+218)) has monodromy
# around the branch points c = -22/5 and c = -218/45.
#
# Around c = -22/5: (5c+22) has a simple zero.
# omega ~ pi * sqrt((5c+22)/something) ~ sqrt(5c+22) -> 0.
# Monodromy: analytic continuation around c = -22/5 sends sqrt(5c+22) -> -sqrt(5c+22).
# So omega -> -omega. Monodromy = -1.
#
# Around c = -218/45: (45c+218) has a simple zero.
# omega ~ pi * sqrt(something/(45c+218)) ~ 1/sqrt(45c+218) -> infinity.
# Monodromy: sqrt(45c+218) -> -sqrt(45c+218), so 1/sqrt -> -1/sqrt.
# Again omega -> -omega. Monodromy = -1.
#
# COMBINED monodromy (loop around both branch points = loop around infinity):
# (-1)*(-1) = +1. So the monodromy at infinity is trivial.
# This means: the period omega(c) is a SINGLE-VALUED function
# on C \ {-22/5, -218/45}, i.e., on the complement of two points.

print("Monodromy of the c-period omega(c):")
print(f"  Around c = -22/5 (Lee-Yang): M = -1 (square root branch)")
print(f"  Around c = -218/45:          M = -1 (square root branch)")
print(f"  Around infinity:              M = (-1)(-1) = +1 (trivial)")
print()
print(f"The period omega(c) has Z/2 monodromy around each finite singularity")
print(f"and trivial monodromy at infinity.")
print()

# KOSZUL DUALITY and the c-monodromy:
# The involution c -> 26-c maps:
#   -22/5 -> 26+22/5 = 152/5
#   -218/45 -> 26+218/45 = 1388/45
# So the Koszul dual singularities are at c = 152/5 and c = 1388/45.
# These are the SECOND set of singular fibers (for the dual algebra).

print("Koszul dual singularities:")
print(f"  -22/5 <-> 152/5 = {Rational(152,5)} = {float(Rational(152,5))}")
print(f"  -218/45 <-> 1388/45 = {Rational(1388,45)} = {float(Rational(1388,45)):.4f}")
print()

# The FULL monodromy representation of the PAIR (A, A!) has singularities at
# c in {-22/5, -218/45, 152/5, 1388/45, 0, 26}.
# (Adding c=0 for the cusp and c=26 = Koszul dual of cusp.)

# Complementarity of discriminants:
# Delta(c) + Delta(26-c) = 40/(5c+22) + 40/(152-5c) = 40*174/[(5c+22)(152-5c)]
#                        = 6960/[(5c+22)(152-5c)]
Delta_c = Rational(40) / (5*c + 22)
Delta_dual = Rational(40) / (152 - 5*c)
Delta_sum = cancel(Delta_c + Delta_dual)
print(f"Discriminant complementarity:")
print(f"  Delta(c) + Delta(26-c) = {Delta_sum}")
print(f"  = 6960/[(5c+22)(152-5c)]: {cancel(Delta_sum - 6960/((5*c+22)*(152-5*c))) == 0}")
print()


print("=" * 80)
print("SUPPLEMENT 4: THE SURFACE S AND ITS ARITHMETIC STRUCTURE")
print("=" * 80)
print()

# The surface S: {(c,t,y) : y^2 = Q_L(t;c)}.
# In cleared form: {(c,t,y) : (5c+22)y^2 = P(c,t)}.
# P = 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2.
#
# This is a surface of BIDEGREE (3,2) in (c,t) with a y^2 factor.
# The projection to the c-line gives a family of conics (genus 0).
# The projection to the t-line gives a family of cubics (genus 1 generically!).
#
# WAIT: the projection pi_t: S -> P^1_t is given by:
# For fixed t, P(c,t) is a CUBIC in c. So y^2 = P(c,t)/(5c+22) is a
# rational function of c. The curve {y^2 = rational function of c}
# can have genus > 0!
#
# Let's analyze: for fixed t != 0, P(c,t) = 5c^3 + ... is a cubic,
# and (5c+22) is linear. So (5c+22)y^2 = P gives:
# y^2 = P/(5c+22) = [5c^3 + ...] / (5c+22)
# = 5c^3/(5c+22) + ... (degree 2 in c after polynomial long division)
# Actually: P/(5c+22) = c^2 + 12ct + alpha(c)t^2 is degree 2 in c
# (since alpha(c) is a rational function). So the fiber over fixed t is:
# y^2 = c^2 + 12ct + alpha(c)t^2
# which is a rational function of c of degree 2 in the numerator (after clearing denom).
# This is a genus-0 curve in c.
#
# More precisely: clear denominators: (5c+22)y^2 = P(c,t).
# This is a degree-3 equation in c (for fixed t,y). The projection
# (c,t,y) -> (t,y) is a 3-fold cover, generically.
# The projection (c,t,y) -> c is a conic (degree 2 in t for fixed c,y).
# The projection (c,t,y) -> t gives a cubic in c (for fixed t,y).
#
# The GENUS of S as an abstract surface:
# S is defined by (5c+22)y^2 = P(c,t) in weighted projective space.
# This is a K3 surface if the bidegree is right, or rational otherwise.
# Let's check: in P^1_c x P^1_t x P^1_y, the equation is
# (5c+22)y^2 = P(c,t) which is degree (1+2, 2, 0) + (0, 0, 2) = bidegree.
# Hmm, this doesn't fit the standard framework easily.
#
# For the purposes of this investigation, the key point is that S
# is a rational surface (since each fiber is genus 0).

print("The surface S = {(c,t,y) : y^2 = Q_L(t;c)} is a RATIONAL SURFACE")
print("(each fiber over c is a genus-0 curve).")
print()

# THE DISCRIMINANT LOCUS:
# D = {(c,t) : Q_L(t;c) = 0} in the (c,t)-plane.
# This is the curve P(c,t) = 0 (for c != -22/5).
# For fixed c > 0, this gives the branch points t_+/-(c) (complex conjugate).
# As c varies, the branch points trace out a curve in the c-plane.

# Let's compute the branch point locus more explicitly.
# Q_L = 0 iff c^2 + 12ct + alpha(c)t^2 = 0
# Treating this as quadratic in t: alpha*t^2 + 12c*t + c^2 = 0
# t = [-12c +/- sqrt(144c^2 - 4*alpha*c^2)] / (2*alpha)
#   = [-12c +/- c*sqrt(144 - 4*alpha)] / (2*alpha)
#   = c * [-12 +/- sqrt(144 - 4*alpha)] / (2*alpha)
# = c * [-12 +/- sqrt(-320/(5c+22))] / [2*(180c+872)/(5c+22)]
# = c * (5c+22) * [-12 +/- i*sqrt(320/(5c+22))] / [2*(180c+872)]

# As c -> 0: t ~ 0 (both branch points collide at the origin).
# As c -> infinity: alpha ~ 36, so
# t ~ c * [-12 +/- sqrt(144-144)] / 72 ... wait, 4*alpha -> 4*36 = 144
# so sqrt(144-4*alpha) -> 0 as c -> infinity!
# This means: the branch points collide also at c = infinity!

# The separation: |t_+ - t_-|^2 = c^2 * (-320/(5c+22)) / alpha^2
#                               = -320c^2 / [(5c+22)*alpha^2]
# For large c: alpha ~ 36, so |t_+-t_-|^2 ~ -320c^2/(5c*36^2) ~ -320/(5*36^2) * c
# Wait, this is negative, meaning the branch points are complex conjugate (as expected).
# |t_+-t_-|^2 = 320c^2/(5c+22)/alpha^2 -> 320c^2/(5c*1296) ~ c/20.25
# So the branch points SPREAD as c grows. The separation grows like sqrt(c).

# Actually let me recompute: alpha = (180c+872)/(5c+22) -> 36 as c -> infty.
# 144 - 4*alpha -> 144 - 4*36 = 0 from below (4*alpha > 144 for large c).
# 4*alpha = 4(180c+872)/(5c+22) = (720c+3488)/(5c+22)
# 144 - 4*alpha = [144(5c+22) - 720c - 3488]/(5c+22) = [720c+3168-720c-3488]/(5c+22)
#               = -320/(5c+22)
# So 144-4*alpha = -320/(5c+22), confirming the discriminant formula.

# The branch points in the c-plane (for the FAMILY):
# As c ranges over C, the two branch points t_+(c), t_-(c) trace
# two curves in the (c,t)-plane. These curves are the solutions of
# Q_L(t;c) = 0. Since Q_L is quadratic in t, these are TWO branches
# of the discriminant curve D.
#
# D: alpha(c)*t^2 + 12c*t + c^2 = 0
# This is a conic in the (c,t)-plane (after clearing the c-dependent
# coefficient alpha(c)).

# In homogeneous form: (180c+872)t^2/(5c+22) + 12ct + c^2 = 0
# Multiply by (5c+22): (180c+872)t^2 + 12c(5c+22)t + c^2(5c+22) = 0
# = (180c+872)t^2 + (60c^2+264c)t + (5c^3+22c^2) = 0
# Factor out common factors: check gcd.
# At t=0: 5c^3+22c^2 = c^2(5c+22) = 0, so c=0 or c=-22/5.
# At c=0: 872t^2 = 0, so t=0.
# So D passes through (c,t) = (0,0) with multiplicity 2.

print("Discriminant curve D = {Q_L(t;c) = 0} in the (c,t)-plane:")
print("  Equation: (180c+872)t^2 + (60c^2+264c)t + (5c^3+22c^2) = 0")
print("  Passes through (0,0) with multiplicity 2 (cusp/node).")
print()

# Check the singularity type at (0,0):
# Substitute c = epsilon*u, t = epsilon*v:
# (180*eps*u + 872)*(eps*v)^2 + (60*eps^2*u^2+264*eps*u)*(eps*v) + (5*eps^3*u^3+22*eps^2*u^2) = 0
# Leading order in epsilon:
# 872*eps^2*v^2 + 264*eps^2*u*v + 22*eps^2*u^2 + O(eps^3) = 0
# Divide by eps^2: 872v^2 + 264uv + 22u^2 = 0
# = 2(436v^2 + 132uv + 11u^2)
# Discriminant: 132^2 - 4*436*11 = 17424 - 19184 = -1760 < 0
# So the tangent cone is an irreducible conic (no real tangent lines).
# The singularity at (0,0) is an ISOLATED POINT of the real discriminant curve,
# but over C it is a NODE (two complex conjugate branches).

print("Singularity at (0,0):")
print("  Tangent cone: 872v^2 + 264uv + 22u^2 = 0")
print("  Discriminant of tangent cone: 264^2 - 4*872*22 = 69696 - 76736 = -7040 < 0")

# Wait, let me recompute: the quadratic form is 2(436v^2 + 132uv + 11u^2)
# Disc = 132^2 - 4*436*11 = 17424 - 19184 = -1760 < 0
# Over C, two complex conjugate tangent directions.
# This is a NODE of the (complex) discriminant curve.
print("  = -1760 < 0: complex conjugate tangent directions.")
print("  This is a NODE of the complex discriminant curve D.")
print()


print("=" * 80)
print("SUPPLEMENT 5: NUMERICAL EO vs SHADOW AT SPECIFIC c VALUES")
print("=" * 80)
print()

# Use the topological recursion engine for numerical comparison.
# The key test: does the EO recursion on y^2 = Q_L(t;c) at specific c
# values reproduce the shadow tower coefficients?

from fractions import Fraction

# Compute shadow coefficients S_r at c = 10 from the closed form.
c_val = 10
kappa_val = c_val / 2  # = 5
alpha_val = 2
S4_val = 10 / (c_val * (5*c_val + 22))  # = 10/(10*72) = 10/720 = 1/72
Delta_val = 8 * kappa_val * S4_val  # = 8*5/72 = 40/72 = 5/9

print(f"c = {c_val}:")
print(f"  kappa = {kappa_val}")
print(f"  alpha = S_3 = {alpha_val}")
print(f"  S_4 = {S4_val}")
print(f"  Delta = {Delta_val}")
print()

# Q_L(t) = 100 + 120t + (180*10+872)/(5*10+22) * t^2
#         = 100 + 120t + 2672/72 * t^2
#         = 100 + 120t + 334/9 * t^2
q0 = c_val**2  # 100
q1 = 12*c_val  # 120
alpha_c_val = (180*c_val + 872) / (5*c_val + 22)  # 2672/72 = 334/9
q2 = alpha_c_val

print(f"  Q_L(t) = {q0} + {q1}t + {q2:.6f}t^2")
print(f"  alpha(10) = {alpha_c_val:.6f} = 334/9")
print()

# Branch points: t_pm = (-120 +/- sqrt(120^2 - 4*100*334/9)) / (2*334/9)
# = (-120 +/- sqrt(14400 - 133600/9)) / (668/9)
# = (-120 +/- sqrt((129600 - 133600)/9)) / (668/9)
# = (-120 +/- sqrt(-4000/9)) / (668/9)
# = (-120 +/- i*sqrt(4000)/3) / (668/9)
# = (-120 +/- i*20*sqrt(10)/3) / (668/9)
# = 9*(-120 +/- i*20*sqrt(10)/3) / 668
# = (-1080 +/- i*60*sqrt(10)) / 668
# = (-270 +/- i*15*sqrt(10)) / 167

import cmath
import math

disc_num = q1**2 - 4*q0*q2
print(f"  disc_t = {disc_num:.6f}")
t_p = (-q1 + cmath.sqrt(disc_num)) / (2*q2)
t_m = (-q1 - cmath.sqrt(disc_num)) / (2*q2)
print(f"  t_+ = {t_p}")
print(f"  t_- = {t_m}")
print(f"  |t_+| = {abs(t_p):.6f}")
print(f"  R = |t_+| = {abs(t_p):.6f}")
print()

# Shadow coefficients from Taylor expansion at c=10:
S_vals = {}
QL_at_10 = q0 + q1*t + q2*t**2
sqrt_QL_at_10_series = series(sqrt(Symbol('t')**0 * q0 + q1*Symbol('t') + q2*Symbol('t')**2), Symbol('t'), 0, n=10)
# Actually let me just use the exact sympy formula
t_sym = Symbol('t')
QL_num = q0 + q1*t_sym + q2*t_sym**2
sqrt_series = series(sqrt(QL_num), t_sym, 0, n=10)
print("Shadow coefficients at c=10:")
for k in range(10):
    coeff = sqrt_series.coeff(t_sym, k)
    S_r = coeff / (k+2)
    S_vals[k+2] = float(S_r)
    print(f"  S_{k+2} = {float(S_r):.10f}")
print()

# Now compare with the recursion formula.
# S_5 = -(P/10) * c_{3,4} * 12 * S_3 * S_4 = -(2/kappa)/(10) * 12 * 2 * S_4
#      = -48*S_4/(10*kappa) ... wait, P = 1/kappa = 2/c.
P_val = 1 / kappa_val
S5_rec = -P_val / 10 * 12 * alpha_val * S4_val
print(f"S_5 from recursion: {S5_rec:.10f}")
print(f"S_5 from series:    {S_vals[5]:.10f}")
print(f"Match: {abs(S5_rec - S_vals[5]) < 1e-12}")
print()


print("=" * 80)
print("SUPPLEMENT 6: THE GAUSS-MANIN OF THE FULL (c,t)-FAMILY")
print("=" * 80)
print()

# The two-parameter Gauss-Manin connection nabla_{(c,t)} on the
# rank-1 local system L = <sqrt(Q_L(t;c))> over the base
# B = {(c,t) : Q_L(t;c) != 0 and c != -22/5}
# is given by:
#
# nabla = d - d(log sqrt(Q_L)) = d - dQ_L/(2Q_L)
#
# In coordinates: nabla = d - omega_t dt - omega_c dc
# where omega_t = (dQ_L/dt)/(2Q_L), omega_c = (dQ_L/dc)/(2Q_L).
#
# The connection 1-form is omega = d(log sqrt(Q_L)) = (1/2) d(log Q_L).
# This is an EXACT 1-form, so the connection is automatically FLAT.
# The monodromy around each component of the discriminant D is -1
# (the universal monodromy of a square root around a simple zero).
#
# KEY OBSERVATION: the connection omega = (1/2) d log Q_L is
# INDEPENDENT of the parametrization. It depends only on Q_L
# as a function on the (c,t)-plane. The shadow connection
# nabla^sh is the RESTRICTION of this 2D connection to the t-axis
# (c fixed). The "c-connection" is the restriction to the c-axis
# (t fixed).
#
# The period omega(c) = integral of omega_t dt around a cycle
# encircling the branch cut is a HORIZONTAL section of the c-connection:
# nabla^c(omega) = 0. This is the CLASSICAL Gauss-Manin.

print("The two-parameter Gauss-Manin connection:")
print("  omega = (1/2) d log Q_L = dQ_L / (2Q_L)")
print("  = omega_t dt + omega_c dc")
print()
print("  omega_t = partial_t Q_L / (2Q_L)  [the shadow connection]")
print("  omega_c = partial_c Q_L / (2Q_L)  [the c-variation]")
print()
print("  This is FLAT (omega = d(log sqrt(Q_L)) is exact).")
print("  Monodromy = -1 around each component of D = {Q_L = 0}.")
print()
print("  The shadow connection nabla^sh is the RESTRICTION to the t-direction.")
print("  The period omega(c) is a horizontal section of the c-direction restriction.")
print()

# CURVATURE of the (c,t)-connection:
# F = d omega = d[(1/2) d log Q_L] = (1/2) d^2 log Q_L = 0 (d^2 = 0).
# The connection is flat. No curvature. QED.

# But the INDUCED connection on the period bundle (the Gauss-Manin
# in the classical sense) can have nontrivial curvature if the
# family has non-trivial monodromy in the base directions.
# For our rank-1 case: the monodromy is Z/2, so the induced connection
# on the line bundle of periods has curvature = (1/2) * [singular 2-form].
# But on the complement of D, the curvature is 0 (flat connection).


print("=" * 80)
print("SUPPLEMENT 7: COMPARISON WITH THE SHADOW CONNECTION ON M-bar_g")
print("=" * 80)
print()

# The shadow connection nabla^sh = d - Q'/(2Q) dt is a connection on a
# line bundle over the arity parameter t.
#
# The MODULAR shadow connection nabla^mod is a connection on a line bundle
# over M-bar_g (the moduli space of curves). The latter has curvature
# kappa * omega_g (the modular characteristic times the Hodge class).
#
# These are DIFFERENT objects:
# 1. nabla^sh lives on the SHADOW LINE (the 1D deformation space of
#    the chiral algebra), with parameter t = arity coordinate.
# 2. nabla^mod lives on M-bar_g, with curvature kappa * omega_g.
#
# The CONNECTION between them: the shadow tower IS the Taylor expansion
# (in t) of the parallel transport of nabla^sh. The genus-g contribution
# F_g = kappa * lambda_g^FP is the trace of nabla^mod over M-bar_g.
# The shadow connection encodes how the modular characteristic varies
# with the arity parameter, while the modular connection encodes how
# the obstruction class varies over moduli space.
#
# The Picard-Fuchs equation 2Q f'' + Q' f' - Q'' f = 0 governs
# sections of nabla^sh. The TAUTOLOGICAL RELATIONS on M-bar_g
# govern sections of nabla^mod. The shadow tower INTERTWINES them:
# the MC equation projects the tautological relations to the shadow line.

print("Two connections, two geometries:")
print()
print("  nabla^sh (shadow connection):")
print("    Base: the shadow line L (1-dimensional, parameter t)")
print("    Curvature: 0 (flat)")
print("    Monodromy: -1 around each zero of Q_L")
print("    PF equation: 2Q f'' + Q' f' - Q'' f = 0")
print()
print("  nabla^mod (modular connection on M-bar_g):")
print("    Base: M-bar_g (moduli of curves)")
print("    Curvature: kappa * omega_g (Hodge class)")
print("    PF equation: tautological relations")
print()
print("  The shadow tower intertwines them: the MC equation projects")
print("  the tautological relations on M-bar_g to the PF equation on L.")


print()
print("=" * 80)
print("SUPPLEMENT 8: THE 45c+218 FACTOR AND ITS MEANING")
print("=" * 80)
print()

# The period omega(c) = pi*sqrt((5c+22)/(45c+218)) has a NEW singularity
# at c = -218/45 that does NOT appear in the shadow connection itself.
# Where does 45c+218 come from?
#
# From the computation: alpha(c) = (180c+872)/(5c+22) = 4(45c+218)/(5c+22).
# So the period squared is (5c+22)/alpha = (5c+22)^2 / [4(45c+218)] * 4/(5c+22)
# Wait: period^2 = (2pi)^2 / alpha = (2pi)^2 * (5c+22) / (180c+872)
#                = (2pi)^2 * (5c+22) / [4*(45c+218)]
#                = pi^2 * (5c+22) / (45c+218).
# Yes: the factor 45c+218 comes from the t^2 coefficient of Q_L.
#
# 45c+218 = 0 iff c = -218/45 approx -4.844.
# At this c value: alpha(c) = 4*(45c+218)/(5c+22) = 0.
# So alpha(-218/45) = 0! The t^2 coefficient of Q_L vanishes!
#
# When alpha = 0: Q_L(t) = c^2 + 12ct (linear in t!).
# The spectral curve y^2 = c^2 + 12ct degenerates to a SINGLE branch point
# at t = -c/12 (where Q_L = 0). The curve is no longer a quadratic
# double cover; it becomes a FOLD: y^2 = 12c(t + c/12).

# Check: alpha(-218/45) = (180*(-218/45)+872)/(5*(-218/45)+22)
#       = (-180*218/45 + 872) / (-218/9 + 22)
#       = (-872 + 872) / (-218/9 + 198/9)
#       = 0 / (-20/9) = 0. Yes!

c_val_218 = Rational(-218, 45)
alpha_at_218 = cancel(virasoro_alpha(c).subs(c, c_val_218))
print(f"alpha(-218/45) = {alpha_at_218}")
print(f"At c = -218/45: Q_L(t) = c^2 + 12ct (linear in t, alpha = 0)")
print(f"The spectral curve degenerates to y^2 = 12c(t + c/12)")
print(f"  = a single fold point, genus dropping to 'sub-genus-0'.")
print()

# This means: c = -218/45 is where the QUADRATIC structure of Q_L
# degenerates. The shadow metric ceases to be a non-degenerate
# quadratic form in t. The shadow tower, which depends on Q_L
# being degree 2 in t, BREAKS DOWN at this c value.
#
# Recall: Q_L(t) = (2kappa + 3*alpha*t)^2 + 2*Delta*t^2
# At alpha = 0: Q_L = 4kappa^2 + 2*Delta*t^2 = c^2 + 16*kappa*S_4*t^2.
# Wait, if alpha = 0, then S_3 = 0. For Virasoro, S_3 = 2 for all c.
# Contradiction? Let me check.
#
# For Virasoro: S_3 = alpha = 2, independent of c.
# But alpha(c) = (180c+872)/(5c+22) is the t^2 COEFFICIENT of Q_L,
# which is 9*S_3^2 + 16*kappa*S_4 = 9*4 + 16*(c/2)*10/(c(5c+22))
# = 36 + 80/(5c+22) = (180c+792+80)/(5c+22) = (180c+872)/(5c+22).
#
# So alpha(c) = 36 + 80/(5c+22), and alpha = 0 requires:
# 36 + 80/(5c+22) = 0 => 80/(5c+22) = -36 => 5c+22 = -80/36 = -20/9
# => 5c = -22 - 20/9 = -198/9 - 20/9 = -218/9 => c = -218/45.
#
# At c = -218/45: S_3 = 2 (still!), kappa = c/2 = -109/45.
# S_4 = 10/(c*(5c+22)) = 10/((-218/45)*(-20/9)) = 10*(45*9)/(218*20)
#      = 4050/4360 = 405/436 = 45/48.444... hmm.
# Let me compute: 5c+22 = 5*(-218/45)+22 = -218/9+22 = (-218+198)/9 = -20/9.
# S_4 = 10/((-218/45)*(-20/9)) = 10*45*9/(218*20) = 4050/4360 = 405/436.
# Delta = 8*kappa*S_4 = 8*(-109/45)*(405/436)
#       = 8*(-109)*405/(45*436) = 8*(-109)*9/436 = -72*109/436
#       = -7848/436 = -18. Hmm.

c218 = Rational(-218, 45)
kappa_218 = c218/2
S4_218 = cancel(Rational(10) / (c218*(5*c218+22)))
Delta_218 = cancel(8*kappa_218*S4_218)
print(f"At c = -218/45:")
print(f"  kappa = {kappa_218} = {float(kappa_218):.4f}")
print(f"  S_3 = 2 (universal for Virasoro)")
print(f"  S_4 = {S4_218} = {float(S4_218):.4f}")
print(f"  Delta = {Delta_218} = {float(Delta_218):.4f}")
print(f"  alpha(c) = 9*S_3^2 + 16*kappa*S_4 = 36 + 2*Delta = {36 + 2*float(Delta_218):.4f}")
alpha_check = cancel(36 + 2*Delta_218)
print(f"  Check: 36 + 2*Delta = {alpha_check}")
print()

# So alpha(c) = 36 + 2*Delta, and alpha = 0 iff Delta = -18.
# At c = -218/45: Delta = -18, confirming alpha = 0.
# This is a NEGATIVE discriminant! For negative Delta, the branch points
# are REAL (not complex conjugate). And alpha = 0 means the branch points
# are at t = 0 and t = infinity (one of them).
#
# Actually at alpha = 0: Q_L = c^2 + 12ct = c(c + 12t).
# Zero at t = -c/12 = -(-218/45)/12 = 218/(45*12) = 218/540 = 109/270.
# The other "zero" is at t = infinity (since Q_L is now degree 1 in t).

print(f"Physical interpretation of c = -218/45:")
print(f"  This is where the shadow metric Q_L LOSES its quadratic term in t.")
print(f"  The spectral curve degenerates: one branch point escapes to infinity.")
print(f"  The period diverges (integral to infinity).")
print(f"  Delta = -18 < 0: the shadow metric has REAL zeros (not complex conjugate).")
print(f"  This is a phase transition in the shadow tower structure.")
print()

print("45c+218 in Koszul dual notation:")
print(f"  For Vir_c: 45c+218 = 0 at c = -218/45")
print(f"  For Vir_{{26-c}}: 45(26-c)+218 = 1388-45c = 0 at c = 1388/45")
print(f"  So {Rational(-218,45)} and {Rational(1388,45)} are Koszul dual.")
print(f"  Sum: -218/45 + 1388/45 = {Rational(-218+1388,45)} = 26. Correct (Koszul sum).")
print()
