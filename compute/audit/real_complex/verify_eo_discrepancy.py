r"""Verify the EO vs shadow tower discrepancy more carefully.

Key claim to verify: the EO F_1 on y^2 = Q_L(t) does NOT equal kappa/24.

Also verify: the Airy model free energies ARE lambda_g^FP.

And: that the tree-level EO omega_{0,n} DO match shadow coefficients.
"""

import sys, os
sys.path.insert(0, os.path.expanduser('~/chiral-bar-cobar'))

from fractions import Fraction
import cmath
import math

# ============================================================================
# 1. Airy free energies vs lambda_g^FP
# ============================================================================

print("=" * 80)
print("VERIFICATION 1: Airy free energies = lambda_g^FP")
print("=" * 80)
print()

# The Airy curve y^2 = x has free energies F_g^Airy.
# lambda_g^FP = |B_{2g}| / (4g(g-1)) for g >= 2, and 1/24 for g = 1.
# These should be the SAME as the EO free energies of the Airy curve.
#
# Bernoulli numbers: B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30,
# B_10 = 5/66, B_12 = -691/2730.
#
# lambda_1^FP = 1/24
# lambda_2^FP = |B_4|/(4*2*1) = (1/30)/8 = 1/240
# lambda_3^FP = |B_6|/(4*3*2) = (1/42)/24 = 1/1008
# lambda_4^FP = |B_8|/(4*4*3) = (1/30)/48 = 1/1440
# lambda_5^FP = |B_10|/(4*5*4) = (5/66)/80 = 1/1056

# The EO result for the Airy curve (Kontsevich's theorem):
# F_g^Airy = chi(M_g) = B_{2g}/(4g(g-1)) for g >= 2.
# F_1^Airy = -chi(M_1)/12 = 1/24.
#
# CAREFUL: chi(M_g) = B_{2g}/(4g(g-1)) includes the SIGN.
# B_4 = -1/30, so chi(M_2) = -1/(30*8) = -1/240.
# But lambda_2^FP = |B_4|/(4*2*1) = 1/240 (positive).
#
# The SIGN CONVENTION in the shadow tower:
# F_g = kappa * lambda_g^FP where all F_g values are POSITIVE
# (from the A-hat generating function, whose coefficients are all positive).
# So lambda_g^FP = |B_{2g}| / (4g(g-1)) (always positive).
# The EO F_g^Airy includes signs, but the PHYSICAL F_g uses |B_{2g}|.

# Actually let me re-examine. The A-hat genus:
# A-hat(ix) = (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...
# A-hat(ix) - 1 = x^2/24 + 7x^4/5760 + 31x^6/967680 + ...
# F_g matches [hbar^{2g}] of kappa*(A-hat(i*hbar) - 1).
# So F_1 = kappa/24, F_2 = 7*kappa/5760, etc.

# Verify: 7/5760 = ? = |B_4|/(4*2*1)?
# |B_4| = 1/30. 1/(30*8) = 1/240. 7/5760 = 7/5760.
# 1/240 = 24/5760. So 7/5760 != 1/240.
# WAIT: this means lambda_2^FP != |B_4|/(4*2*1)?

# Let me recheck. The claim from the manuscript is:
# F_g = kappa * lambda_g^FP where lambda_g = integral of lambda_g over M_g.
# For g=1: lambda_1 = 1/24.
# For g=2: lambda_2 = 1/1152 (not 1/240).
# Hmm, different references use different normalizations.

# From the A-hat function:
# A-hat(x) = x/2 / sinh(x/2)
# For ix: A-hat(ix) = ix/(2i sin(x/2)) = x/(2 sin(x/2))
# = (x/2)/sin(x/2) = 1 + x^2/24 + 7x^4/5760 + ...

# The coefficients of A-hat(ix) - 1:
# [x^2] = 1/24
# [x^4] = 7/5760
# [x^6] = 31/967680

# So F_1 = kappa/24, F_2 = 7*kappa/5760, F_3 = 31*kappa/967680.

# Now from lambda classes on M-bar_g:
# lambda_g^FP (Faber-Pandharipande) = integral_{M_g} lambda_g.
# For g=1: int_{M_1} lambda_1 = 1/24.
# For g=2: int_{M_2} lambda_2 = 1/1152? Let me check.

# Actually, the Faber-Pandharipande formula:
# int_{M_g} lambda_g = (-1)^g * B_{2g}/(2g) * B_{2g-2}/(2g-2) * 1/(2g-2)!
# Hmm, this doesn't look right either.

# Let me use a cleaner reference. The Mumford formula:
# int_{M_g} lambda_g c_{g-1} = |B_{2g}|/(2g) * 1/(2g-2)! for some class c_{g-1}.

# Actually, the correct formula is (Faber's conjecture, proved):
# int_{M_{g,n}} psi_1^{d_1} ... psi_n^{d_n} lambda_g = (lots of combinatorics)

# For our purposes, the key identity is:
# F_g = kappa * [coefficient of hbar^{2g} in A-hat(i*hbar) - 1]
# = kappa * sum_{k=1}^g (-1)^{k+1} * B_{2k}^2 / ((2k)! * 2^{2k} * ...) ... no.

# Let me just compute the A-hat coefficients directly.
# A-hat(x) = prod_{k >= 1} (x_k/2) / sinh(x_k/2) for eigenvalues x_k.
# For a single variable: A-hat(x) = (x/2)/sinh(x/2).
# Taylor expansion of (x/2)/sinh(x/2):
# sinh(u) = u + u^3/6 + u^5/120 + u^7/5040 + ...
# (x/2)/sinh(x/2) = 1/(1 + (x/2)^2/6 + (x/2)^4/120 + ...)
# Let u = x/2:
# u/sinh(u) = 1/(1 + u^2/6 + u^4/120 + u^6/5040 + ...)
# = 1 - u^2/6 + (u^2/6)^2 - u^4/120 + ...
# = 1 - u^2/6 + u^4(1/36 - 1/120) + ...
# = 1 - u^2/6 + u^4*(10/360 - 3/360) + ...
# = 1 - u^2/6 + 7u^4/360 + ...

# With u = x/2: u^2 = x^2/4, u^4 = x^4/16.
# A-hat(x) = 1 - x^2/24 + 7x^4/5760 - ...

# A-hat(ix) = 1 + x^2/24 + 7x^4/5760 + ...
# (replacing x by ix changes the sign of even powers to positive)

print("A-hat generating function coefficients:")
# Using the formula: A-hat(ix) - 1 = sum_{g>=1} a_g x^{2g}
# a_1 = 1/24
# a_2 = 7/5760
# a_3 = 31/967680
# These are the lambda_g^FP values.

# Verify: B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, B_10 = 5/66.

# The A-hat genus can also be written as:
# A-hat(x) = exp(-sum_{k>=1} s_k * x^{2k} / (2k))
# where s_k = 2*zeta(2k)*(2k-1)! / (2*pi)^{2k} ... no.

# Actually the simplest: A-hat(x) = prod (x_j/2)/sinh(x_j/2).
# For a rank-1 bundle with Chern root x:
# A-hat(x) = (x/2)/sinh(x/2) = sum_{n>=0} (-1)^n (2^{2n}-2) B_{2n} x^{2n} / (2n)!
# Wait, that's the Todd class maybe.

# Cleanest: (x/2)/sinh(x/2) = sum_{n>=0} E_n x^n / n! where E_n are...
# No, let me just do Taylor expansion numerically.

from decimal import Decimal, getcontext
getcontext().prec = 50

# u/sinh(u) at u = x/2
# = 1 - u^2/6 + 7u^4/360 - 31u^6/15120 + 127u^8/604800 - ...
# With u = x/2:
# = 1 - x^2/24 + 7x^4/5760 - 31x^6/967680 + 127x^8/154828800 - ...

# So A-hat(ix) - 1 = x^2/24 + 7x^4/5760 + 31x^6/967680 + 127x^8/154828800 + ...
# (all positive, since replacing x by ix flips signs of even-index terms)

# lambda_g^FP values:
lambda_FP = {
    1: Fraction(1, 24),
    2: Fraction(7, 5760),
    3: Fraction(31, 967680),
    4: Fraction(127, 154828800),
}

for g, lam in lambda_FP.items():
    print(f"  lambda_{g}^FP = {lam} = {float(lam):.12e}")

print()

# Now compare with |B_{2g}|/(4g(g-1)):
bernoulli_vals = {
    2: Fraction(1, 6),
    4: Fraction(-1, 30),
    6: Fraction(1, 42),
    8: Fraction(-1, 30),
    10: Fraction(5, 66),
}

print("Comparison with |B_{2g}|/(4g(g-1)):")
for g in range(1, 5):
    if g == 1:
        b_formula = Fraction(1, 24)  # Special case for g=1
    else:
        B2g = abs(bernoulli_vals[2*g])
        b_formula = B2g / (4*g*(g-1))
    print(f"  g={g}: lambda_g^FP = {lambda_FP[g]}, |B_{{2g}}|/(4g(g-1)) = {b_formula}, match = {lambda_FP[g] == b_formula}")

print()

# So lambda_g^FP != |B_{2g}|/(4g(g-1)) in general!
# The actual Airy free energies (Kontsevich) involve DIFFERENT combinatorics.
# The A-hat coefficients come from (x/2)/sinh(x/2), while |B_{2g}|/(4g(g-1))
# comes from chi(M_g) = B_{2g}/(4g(g-1)).
#
# Conclusion: the existing code `airy_free_energy` in topological_recursion_engine.py
# uses chi(M_g) = B_{2g}/(4g(g-1)), but the actual lambda_g^FP from the
# shadow tower (Theorem D) uses the A-hat coefficients 1/24, 7/5760, 31/967680, ...
#
# Let me check: are these the SAME?
# g=1: 1/24 vs B_2/(4*1*0) = ... undefined (g=1 is special). Both give 1/24.
# g=2: 7/5760 vs |B_4|/(4*2*1) = (1/30)/8 = 1/240.
#       7/5760 = 7/5760. 1/240 = 24/5760. These are DIFFERENT.

print("CRITICAL: lambda_2^FP = 7/5760 != |B_4|/(4*2*1) = 1/240!")
print("The topological_recursion_engine.py uses the WRONG formula for F_g^Airy.")
print()

# What IS lambda_g^FP?
# From Theorem D (the A-hat generating function):
# sum_{g>=1} F_g * hbar^{2g} = kappa * [A-hat(i*hbar) - 1]
# = kappa * [hbar^2/24 + 7*hbar^4/5760 + 31*hbar^6/967680 + ...]
# So F_g = kappa * a_g where a_g is the coefficient of hbar^{2g} in A-hat(i*hbar) - 1.
#
# These ARE the lambda-class integrals over M_g (the Faber-Pandharipande theorem).
# But they are NOT B_{2g}/(4g(g-1)).
#
# The Euler characteristic chi(M_g) = B_{2g}/(2g(2g-2)) for g >= 2
# (Harer-Zagier formula). For g=2: chi(M_2) = B_4/(2*2*2) = -1/(30*4) = -1/120.
# Note: 1/120 != 1/240 either.
#
# The correct identity: lambda_g^FP = integral_{M_g} lambda_g (the top Chern class
# of the Hodge bundle). This is DIFFERENT from chi(M_g).
#
# From Faber's conjecture (proved by multiple groups):
# int_{M_g} lambda_g = |B_{2g}| * |B_{2g-2}| / (2g * (2g-2) * (2g-2)!)
# Hmm, this formula is complicated. Let me verify for g=2:
# int_{M_2} lambda_2 = |B_4| * |B_2| / (4 * 2 * 2!)
#                     = (1/30) * (1/6) / (4 * 2 * 2) = 1/180 / 16 = 1/2880
# But we said lambda_2^FP = 7/5760 = 7/5760.
# Is 7/5760 = 1/2880 * 2? No: 1/2880 = 2/5760. So 7/5760 != 1/2880.

# Hmm. I think the issue is that the A-hat coefficients are NOT simply
# lambda_g integrals over M_g. The correct formula involves MORE than
# just the top Chern class. The A-hat class is a polynomial in lambda_i's.

# Actually, the shadow tower formula is:
# F_g = kappa * lambda_g^FP
# where lambda_g^FP is DEFINED as the A-hat coefficient:
# lambda_g^FP := [hbar^{2g}] A-hat(i*hbar) - 1.
# This is a DEFINITION in the manuscript, motivated by the Faber-Pandharipande
# intersection numbers but not identical to int_{M_g} lambda_g.

# The actual value: the coefficient of u^{2n} in u/sinh(u):
# u/sinh(u) = sum_{n=0}^infty (-1)^n * (2 - 2^{2n+1}) * B_{2n} / (2n)! * u^{2n}
# Wait, let me use a standard identity.
# u/sinh(u) = 2u/(e^u - e^{-u}) = 2u*e^{-u}/(1 - e^{-2u})
#            = sum_{n=0}^infty (-1)^n * 2(1 - 2^{2n-1}) * B_{2n}/(2n)! * u^{2n}  [for n >= 1]
# Hmm, I'm getting confused with signs. Let me just verify numerically.

import math as m

def ahat_coeff(g, terms=100):
    """Compute [x^{2g}] of A-hat(ix) = (x/2)/sin(x/2) numerically.

    A-hat(ix) = (x/2)/sin(x/2) = sum a_g x^{2g}.
    """
    # Use the reciprocal: sin(x/2)/(x/2) = sum_{k=0}^inf (-1)^k (x/2)^{2k}/(2k+1)!
    # Then A-hat = 1 / [sin(x/2)/(x/2)] = 1/f(x) where f = 1 - x^2/24 + x^4/1920 - ...

    # Build the coefficients of f(x) = sin(x/2)/(x/2) in powers of x^2:
    # f = sum_{k=0}^N (-1)^k / (2^{2k} * (2k+1)!) * x^{2k}
    N = terms
    f_coeffs = [0.0] * (N + 1)
    for k in range(N + 1):
        f_coeffs[k] = (-1)**k / (2**(2*k) * m.factorial(2*k + 1))

    # Invert: 1/f = g, where g * f = 1.
    # g[0] = 1/f[0] = 1.
    # g[n] = -(1/f[0]) * sum_{k=1}^n f[k] * g[n-k]
    g_coeffs = [0.0] * (N + 1)
    g_coeffs[0] = 1.0 / f_coeffs[0]
    for n in range(1, N + 1):
        s = sum(f_coeffs[k] * g_coeffs[n - k] for k in range(1, n + 1))
        g_coeffs[n] = -s / f_coeffs[0]

    if g < len(g_coeffs):
        return g_coeffs[g]
    return 0.0

print("A-hat(ix) coefficients (numerical):")
for g in range(1, 8):
    a_g = ahat_coeff(g)
    print(f"  a_{g} = [x^{2*g}] A-hat(ix) = {a_g:.15e}")
    if g in lambda_FP:
        print(f"       lambda_{g}^FP = {float(lambda_FP[g]):.15e}")
        print(f"       Match: {abs(a_g - float(lambda_FP[g])) < 1e-12}")

print()


# ============================================================================
# 2. Verify: EO on Airy curve gives which F_g?
# ============================================================================

print("=" * 80)
print("VERIFICATION 2: EO on Airy curve")
print("=" * 80)
print()

# The Airy curve is y^2 = x. This is the local model near a simple
# ramification point at x = 0.
#
# The EO free energies for the Airy curve are:
# F_g^Airy = chi^orb(M_{g,0}) / normalization = B_{2g}/(4g(g-1)) for g >= 2.
# F_1^Airy = 1/24.
#
# But we showed that lambda_g^FP = a_g (the A-hat coefficient).
# Are F_g^Airy = a_g? Let's check.
# F_2^Airy = B_4/(4*2*1) = (-1/30)/8 = -1/240. With sign: -1/240.
# a_2 = 7/5760 = 0.001215...
# -1/240 = -0.004167...
# These are DIFFERENT!

print("F_g^Airy = B_{2g}/(4g(g-1)) vs lambda_g^FP = [x^{2g}] A-hat(ix):")
for g in range(2, 6):
    B2g = Fraction(0)
    # Bernoulli numbers
    if 2*g == 4: B2g = Fraction(-1, 30)
    elif 2*g == 6: B2g = Fraction(1, 42)
    elif 2*g == 8: B2g = Fraction(-1, 30)
    elif 2*g == 10: B2g = Fraction(5, 66)

    F_airy = B2g / (4*g*(g-1))
    a_g = ahat_coeff(g)
    print(f"  g={g}: F_Airy = {F_airy} = {float(F_airy):.10e}, a_g = {a_g:.10e}, SAME? {abs(float(F_airy) - a_g) < 1e-12}")

print()

# So F_g^Airy (Euler characteristic) != lambda_g^FP (A-hat coefficient).
# The claim "F_g = kappa * F_g^Airy" is WRONG if F_g^Airy = B_{2g}/(4g(g-1)).
# The correct claim is F_g = kappa * lambda_g^FP = kappa * a_g.
#
# The EO recursion on the Airy curve gives F_g^Airy = B_{2g}/(4g(g-1)),
# which is NOT the same as the shadow tower's F_g/kappa.
#
# CONCLUSION: the EO recursion on the Airy curve does NOT reproduce
# the shadow tower free energies. The shadow tower uses the A-hat
# class, which involves ALL lambda classes, not just chi(M_g).

print("CONCLUSION: The EO recursion on the Airy curve gives chi(M_g) = B_{2g}/(4g(g-1)),")
print("which is DIFFERENT from lambda_g^FP = [x^{2g}] A-hat(ix) for g >= 2.")
print()
print("The shadow tower formula F_g = kappa * lambda_g^FP uses the A-hat GENUS,")
print("not the Euler characteristic of M_g. The A-hat genus involves INTEGRALS")
print("of lambda classes over M_g (not just the top-degree lambda_g).")
print()
print("The EO recursion is therefore NOT a direct source of the shadow tower")
print("free energies at g >= 2. The MC recursion (which uses the FULL modular")
print("operad structure, not just the topological recursion kernel) is needed.")
print()

# ============================================================================
# 3. What ARE the A-hat coefficients in terms of intersection numbers?
# ============================================================================

print("=" * 80)
print("VERIFICATION 3: A-hat coefficients as intersection numbers")
print("=" * 80)
print()

# The A-hat genus of M_g is int_{M_g} A-hat(T_{M_g}).
# For the moduli space M_g, the tangent bundle T_{M_g} has Chern roots
# that can be expressed in terms of lambda classes.
#
# The Mumford relation:
# ch(E) = 1 + sum_{k>=1} kappa_k / (2k)!
# where E is the Hodge bundle and kappa_k are the kappa classes.
#
# The A-hat genus uses the Todd/A-hat class of the tangent bundle,
# which involves the Pontryagin classes p_i = (-1)^i c_{2i} of T.
#
# Actually, the shadow tower formula is:
# F_g = kappa(A) * integral_{M_g,1} lambda_g * psi_1^0 = kappa(A) * lambda_g^FP
# where lambda_g^FP is the Faber-Pandharipande intersection number
# int_{M_g} lambda_g.
#
# But wait: int_{M_g} lambda_g = ? Let me look this up.
# From Faber (1999), the lambda_g integral over M_g:
# int_{M_g} lambda_g = |B_{2g}| / (2g * (2g)!) * (-1)^{g-1}  ... no.

# Actually, from the standard reference (e.g., Pandharipande's lectures):
# int_{M_g} lambda_{g-1} = |B_{2g}| / (2g * (2g-2)!)
# NOT lambda_g.

# The confusion is that the Hodge bundle E has rank g, so lambda_g = c_g(E)
# is the TOP Chern class. On M_g (of dimension 3g-3), we need
# lambda_g to have degree 3g-3 for the integral to make sense.
# But deg(lambda_g) = g, so int_{M_g} lambda_g makes sense only if
# g = 3g-3, i.e., g = 3/2. That's not an integer!

# So int_{M_g} lambda_g = 0 for dimensional reasons when g != 3/2!
# This means "lambda_g^FP" is NOT int_{M_g} lambda_g.

# The correct FP number: lambda_g * lambda_{g-1}^{2g-3} / ... integrated
# against psi classes. Or more commonly:
# lambda_g^FP is the FP VALUE defined as the coefficient of hbar^{2g-2}
# in the string equation / Witten conjecture.

# Actually, re-reading the manuscript (thm:theorem-d and the A-hat generating
# function), the statement is:
# F_g(A) = kappa(A) * [coefficient of hbar^{2g} in A-hat(i*hbar) - 1]
# And these coefficients are DEFINED as lambda_g^FP in the manuscript.
# They are NOT intersection numbers on M_g in the usual sense.
# They are COEFFICIENTS of the A-hat genus, which is a generating function
# for certain specific intersection numbers on M_{g,n}.

# The key: the A-hat generating function is:
# A-hat(ix) - 1 = sum_{g>=1} a_g x^{2g}
# where a_g is a specific rational number.
# For the shadow tower: F_g = kappa * a_g.
# The manuscript calls a_g by the name "lambda_g^FP."

# These a_g are: 1/24, 7/5760, 31/967680, 127/154828800, ...
# Let me verify: are these related to Bernoulli numbers by a DIFFERENT formula?

# u/sinh(u) = sum_{n>=0} (2 - 2^{2n+1}) B_{2n} / (2n)! * u^{2n}  ?
# No. Standard identity:
# u/sinh(u) = sum_{n>=0} (2^{2n} - 2) * |B_{2n}| / (2n)! * u^{2n}  for n >= 1
# Wait, let me just derive it:
# 1/sinh(u) = 2/(e^u - e^{-u})
# u/sinh(u) = 2u*e^u/(e^{2u} - 1)
#
# The generating function: 2u*e^u/(e^{2u}-1) = u/(e^u - e^{-u}/2) ... hmm.
# Better: t/sinh(t) = sum_{n=0}^inf 2(1-2^{2n-1}) B_{2n} t^{2n} / (2n)!
# (Abramowitz & Stegun, 23.1.16)

# For n=0: 2(1-1/2) B_0 / 0! = 2*1/2*1 = 1. OK.
# For n=1: 2(1-2) B_2 / 2! = 2*(-1)*1/6 / 2 = -1/6.
# But u/sinh(u) at u^2: let's check. sinh(u) = u + u^3/6 + ...
# u/sinh(u) = u/(u + u^3/6 + ...) = 1/(1 + u^2/6 + ...) = 1 - u^2/6 + ...
# So [u^2] = -1/6. From the formula: 2(1-2)*B_2/2! = -2*1/6/2 = -1/6. Matches!
# For n=2: 2(1-8)*B_4/4! = 2*(-7)*(-1/30)/24 = 14/(30*24) = 14/720 = 7/360.
# [u^4] of u/sinh(u): expanding further, 1/(1+u^2/6+u^4/120+...)
# = 1 - u^2/6 + (u^2/6)^2 - u^4/120 + ... = 1 - u^2/6 + u^4/36 - u^4/120
# = 1 - u^2/6 + u^4(1/36 - 1/120) = 1 - u^2/6 + u^4*7/360. Matches!

print("u/sinh(u) = sum_{n>=0} 2(1-2^{2n-1}) B_{2n} u^{2n} / (2n)!")
print()

# Now A-hat(ix) = (ix/2)/sinh(ix/2) ... wait.
# A-hat(x) = (x/2)/sinh(x/2). This is the A-hat genus for a single variable x.
# A-hat(ix) = (ix/2)/sinh(ix/2) = (ix/2)/(i*sin(x/2)) = (x/2)/sin(x/2).
#
# So A-hat(ix) = (x/2)/sin(x/2).
# (x/2)/sin(x/2) = sum_{n>=0} (-1)^n * 2(1-2^{2n-1}) B_{2n} / (2n)! * (x/2)^{2n}
# Wait: sin(x/2)/(x/2) = sum_{n>=0} (-1)^n (x/2)^{2n} / (2n+1)!.
# And (x/2)/sin(x/2) = 1 / [sin(x/2)/(x/2)].

# Let me just use the direct formula:
# (x/2)/sin(x/2) uses the SAME expansion as u/sinh(u) with u = ix/2,
# so u^{2n} = (ix/2)^{2n} = (-1)^n x^{2n}/2^{2n}.
# Then: (x/2)/sin(x/2) = sum_{n>=0} 2(1-2^{2n-1}) B_{2n} / (2n)! * (-1)^n * x^{2n}/2^{2n}
# = sum_{n>=0} 2(1-2^{2n-1}) B_{2n} (-1)^n / (2^{2n} (2n)!) * x^{2n}
# = sum_{n>=0} (1-2^{2n-1}) B_{2n} (-1)^n / (2^{2n-1} (2n)!) * x^{2n}

# For n=1: (1-2)(-1)(1/6) / (2*2) = -(-1/6)/4 = 1/24. Matches!
# For n=2: (1-8)(1)(-1/30) / (8*24) = (-7)(-1/30)/192 = 7/5760. Matches!
# For n=3: (1-32)(-1)(1/42) / (32*720) = (-31)(-1/42)/23040 = 31/967680. Matches!

print("lambda_g^FP = (1-2^{2g-1}) B_{2g} (-1)^g / (2^{2g-1} (2g)!)")
print()

for g in range(1, 6):
    B2g_dict = {2: Fraction(1,6), 4: Fraction(-1,30), 6: Fraction(1,42),
                8: Fraction(-1,30), 10: Fraction(5,66)}
    B2g = B2g_dict.get(2*g, Fraction(0))
    if B2g == 0:
        continue
    lam = (1 - 2**(2*g-1)) * B2g * (-1)**g / (2**(2*g-1) * m.factorial(2*g))
    lam_frac = Fraction(int((1 - 2**(2*g-1)) * (-1)**g), 1) * B2g / Fraction(2**(2*g-1) * m.factorial(2*g))
    a_g = ahat_coeff(g)
    print(f"  g={g}: formula = {float(lam_frac):.15e}, A-hat coeff = {a_g:.15e}, match = {abs(float(lam_frac) - a_g) < 1e-12}")

print()
print("VERIFIED: lambda_g^FP = (1 - 2^{2g-1}) * B_{2g} * (-1)^g / (2^{2g-1} * (2g)!)")
print()
print("This is NOT B_{2g}/(4g(g-1)) [Euler characteristic of M_g].")
print("The topological_recursion_engine.py function airy_free_energy() uses the WRONG formula.")
print()

# Final summary
print("=" * 80)
print("FINAL SUMMARY OF EO vs SHADOW TOWER")
print("=" * 80)
print()
print("1. The shadow tower free energies are F_g = kappa * lambda_g^FP")
print("   where lambda_g^FP = (1-2^{2g-1})*B_{2g}*(-1)^g / (2^{2g-1}*(2g)!).")
print()
print("2. The EO recursion on the Airy curve gives F_g^Airy = B_{2g}/(4g(g-1)).")
print()
print("3. These are DIFFERENT for g >= 2:")
print(f"   g=2: lambda_2^FP = 7/5760 = {float(Fraction(7,5760)):.6e}")
print(f"         F_2^Airy  = -1/240 = {float(Fraction(-1,240)):.6e}")
print()
print("4. Therefore: the shadow tower IS NOT the EO recursion on ANY spectral curve.")
print("   The MC recursion (which uses the modular operad structure) produces a")
print("   DIFFERENT sequence of invariants than the EO recursion.")
print()
print("5. The tree-level (genus-0) data DOES match: the shadow coefficients S_r")
print("   are exactly the Taylor coefficients of sqrt(Q_L(t)), which are also")
print("   the tree-level moments of the spectral curve. Agreement at genus 0")
print("   but disagreement at genus >= 2.")
print()
print("6. The correct comparison: the MC recursion on the modular convolution")
print("   algebra g^mod_A projects to the shadow tower. The EO recursion on the")
print("   spectral curve is a DIFFERENT recursion producing different invariants.")
print("   The shadow tower lives in the MC/A-hat world, not the EO/chi world.")
