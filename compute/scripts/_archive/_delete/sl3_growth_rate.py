#!/usr/bin/env python3
"""Determine sl_3 H_4 using the correct structural ansatz and growth rate constraint.

CORRECT equation for Riordan numbers (sl_2 bar cohomology):
  x*psi(x)*P^2 - psi(x)*P + 1 = 0  where psi(x) = 1+x

Key: psi = 1/(P - x*P^2)  [derived from the equation]

For sl_2: psi = 1+x, disc roots at x=1/3 (growth rate 3 = dim sl_2)
For sl_3: psi = 1 - 7x + 29x^2 - 131x^3 + psi_4*x^4 + ...

Growth rate constraint: disc(1/8) = 0, where disc = psi*(psi-4x).
This gives psi(1/8) = 1/2 (since psi-4x vanishing at 1/8 with psi positive).

With psi = polynomial of degree d:
  psi(1/8) = 1/2 determines one coefficient.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, S, Poly, nroots, N as Neval)

x = symbols('x')

# ================================================================
# VALIDATION: sl_2
# ================================================================
print("=" * 60)
print("sl_2 VALIDATION: psi = 1+x")
print("=" * 60)

psi_sl2 = 1 + x
disc_sl2 = psi_sl2 * (psi_sl2 - 4*x)  # = (1+x)(1-3x)
P_sl2 = (psi_sl2 - sqrt(disc_sl2)) / (2*x*psi_sl2)
P_sl2_series = series(P_sl2, x, 0, 15)

print("P(x) series (Riordan numbers):")
riordan = []
for n in range(12):
    cn = P_sl2_series.coeff(x, n)
    riordan.append(int(cn))
    print(f"  R({n}) = {cn}")

print(f"\nExpected: 1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585")
print(f"Match: {riordan == [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585]}")

# Bar cohomology H_n = R(n+2) for n >= 1, H_0 = 1
print("\nBar cohomology (H_n = R(n+2)):")
for n in range(10):
    if n == 0:
        print(f"  H_0 = 1")
    else:
        print(f"  H_{n} = R({n+2}) = {riordan[n+2] if n+2 < len(riordan) else '?'}")

# Disc roots
print(f"\nDisc = (1+x)(1-3x)")
print(f"Roots: x = -1, x = 1/3")
print(f"Growth rate = 1/(1/3) = 3 = dim(sl_2) ✓")

# ================================================================
# sl_3: compute psi coefficients from known bar cohomology
# ================================================================
print("\n" + "=" * 60)
print("sl_3: COMPUTING psi FROM KNOWN DATA")
print("=" * 60)

# Known: H_0=1, H_1=8, H_2=36, H_3=204
# The GF P(x) counts bar cohomology shifted:
# P = R_0 + R_1*x + R_2*x^2 + ... where H_n = R_{n+?}
#
# Actually, for sl_2: P(x) = Riordan GF = sum R(n) x^n
# and H_n(bar cohomology) = R(n+2) for n >= 1.
#
# What's the offset for sl_3? If the pattern is H_n = P_{n+s} for some shift s,
# we need to figure out s.
#
# For sl_2: P starts 1, 0, 1, 1, 3, 6, 15, 36, ...
# H: 1, 3, 6, 15, 36, 91, ...
# So H_n = P_{n+2} for n >= 1. And H_0 = 1.
#
# Why the shift? Because the bar complex at degree 0 is trivial (the unit),
# and degrees 1 and 2 correspond to the generators and their first compositions.
#
# For sl_3, the shift might be different. But let me first compute psi
# assuming the GF P satisfies x*psi*P^2 - psi*P + 1 = 0 and
# psi = 1/(P - x*P^2).
#
# From P = 1 + c_1*x + c_2*x^2 + c_3*x^3 + ...
# we need to determine what c_n are.
#
# For sl_2: c_0=1, c_1=0, c_2=1, c_3=1, c_4=3, c_5=6, ...
# Bar cohomology H_n = c_{n+2}.
#
# For sl_3: we know H_1=8, H_2=36, H_3=204.
# If H_n = c_{n+2} (same shift as sl_2):
#   c_0 = 1, c_1 = ?, c_2 = 8, c_3 = 36, c_4 = 204, c_5 = H_4
#
# But what is c_1? For sl_2 it was 0. Let's see if c_1 = 0 also for sl_3.

# Actually, let me first try WITHOUT a shift: P = sum H_n x^n directly.
# P = 1 + 8x + 36x^2 + 204x^3 + H_4 x^4 + ...
# Then psi = 1/(P - x*P^2)

# Compute P - x*P^2 through degree 3
a = [1, 8, 36, 204]  # P coefficients (H values)

# P^2 coefficients
p2 = [0] * (2*len(a))
for i in range(len(a)):
    for j in range(len(a)):
        if i+j < len(p2):
            p2[i+j] += a[i] * a[j]

print("P^2 coefficients:")
for n in range(5):
    print(f"  (P^2)_{n} = {p2[n]}")

# x*P^2 coefficients (shift by 1)
xp2 = [0] + p2

# P - x*P^2
diff = [0] * 5
for n in range(min(5, len(a))):
    diff[n] = a[n] - (xp2[n] if n < len(xp2) else 0)

print("\nP - x*P^2 coefficients (= 1/psi):")
for n in range(4):
    print(f"  (P-xP^2)_{n} = {diff[n]}")

# psi = 1/(P-xP^2), computed as formal power series inversion
# Let q = P-xP^2 = q_0 + q_1*x + q_2*x^2 + ...
q = diff[:4]
print(f"\nq = {q}")

# psi = 1/q: psi_n = (-1/q_0) * sum_{k=0}^{n-1} psi_k * q_{n-k}
psi_coeffs = [0] * 4
psi_coeffs[0] = Rational(1, q[0])
for n in range(1, 4):
    s = sum(psi_coeffs[k] * q[n-k] for k in range(n) if n-k < len(q))
    psi_coeffs[n] = -s / q[0]

print("\npsi coefficients:")
for n in range(4):
    print(f"  psi_{n} = {psi_coeffs[n]}")

print(f"\npsi(x) = {psi_coeffs[0]} + {psi_coeffs[1]}*x + {psi_coeffs[2]}*x^2 + {psi_coeffs[3]}*x^3 + ...")

# ================================================================
# Growth rate constraint: psi(1/8) = 1/2
# ================================================================
print("\n" + "=" * 60)
print("GROWTH RATE CONSTRAINT: psi(1/d) = 1/2 where d = dim(g) = 8")
print("=" * 60)

# psi(1/8) through degree 3:
psi_at_eighth = sum(psi_coeffs[n] * Rational(1, 8)**n for n in range(4))
print(f"psi(1/8) through degree 3 = {psi_at_eighth} = {float(psi_at_eighth):.6f}")
print(f"Target: 1/2 = 0.5")
print(f"Deficit: {Rational(1,2) - psi_at_eighth}")

# If psi is degree 4: psi_4/8^4 must make up the deficit
deficit = Rational(1, 2) - psi_at_eighth
psi_4_needed = deficit * 8**4
print(f"\nFor degree-4 psi: psi_4 = {psi_4_needed}")

# psi_4 = 1797 - H_4 (from the series inversion)
# Actually let's verify this relation
print("\nRelation: psi_4 = psi_4_from_eq - H_4")
print("where psi_4_from_eq depends on the series coefficients")

# More precisely:
# psi_4 is determined by: psi_0 * (H_4 - P^2[3]) + psi_1 * q_3 + ... + psi_3 * q_1 + psi_4 * q_0 = 0
# Actually psi * q = 1, so sum_{k=0}^{4} psi_k * q_{4-k} = 0
# q_4 = H_4 - (xP^2)_4 = H_4 - P^2[3]
# P^2[3] = sum_{i+j=3} a_i*a_j = 2*1*204 + 2*8*36 = 408 + 576 = 984
# So q_4 = H_4 - 984

q_4_as_H4 = symbols('H4') - 984
constraint = sum(psi_coeffs[k] * ([1, 7, 20, 68][4-k] if 4-k < 4 else q_4_as_H4)
                 for k in range(5) if 4-k >= 0)
# This needs fixing -- let me recompute
# q = [1, 7, 20, 68, H4-984, ...]

H4 = symbols('H4')
q_sym = [1, 7, 20, 68, H4 - 984]
psi_4 = symbols('psi4')

# psi * q = 1 at degree 4:
# sum_{k=0}^{4} psi_k * q_{4-k} = 0
eq_deg4 = sum(psi_coeffs[k] * q_sym[4-k] for k in range(4)) + psi_4 * q_sym[0]
print(f"\nDegree-4 equation: {expand(eq_deg4)} = 0")
psi_4_sol = solve(eq_deg4, psi_4)[0]
print(f"psi_4 = {psi_4_sol}")

# Now: growth constraint psi_4 = psi_4_needed = {psi_4_needed}
# So: psi_4_sol(H4) = psi_4_needed
H4_sol = solve(psi_4_sol - psi_4_needed, H4)
print(f"\nGrowth rate = 8 constraint: H_4 = {H4_sol}")

if H4_sol:
    H4_val = H4_sol[0]
    psi_4_val = int(psi_4_sol.subs(H4, H4_val))
    print(f"  H_4 = {H4_val}")
    print(f"  psi_4 = {psi_4_val}")

    # Verify
    psi_full = [int(c) for c in psi_coeffs] + [psi_4_val]
    print(f"\n  psi = {psi_full}")

    # Check psi(1/8)
    psi_check = sum(Rational(c) * Rational(1,8)**n for n, c in enumerate(psi_full))
    print(f"  psi(1/8) = {psi_check} (should be 1/2)")

    # Now compute FULL series with this psi
    print("\n" + "=" * 60)
    print(f"FULL SERIES with H_4 = {H4_val}")
    print("=" * 60)

    psi_poly = sum(Rational(c) * x**n for n, c in enumerate(psi_full))
    disc = psi_poly * (psi_poly - 4*x)
    P_full = (psi_poly - sqrt(disc)) / (2*x*psi_poly)
    P_series = series(P_full, x, 0, 18)

    print("P(x) series:")
    all_positive_int = True
    for n in range(16):
        cn = P_series.coeff(x, n)
        cn_simplified = simplify(cn)
        is_int = cn_simplified == int(cn_simplified) if cn_simplified.is_number else False
        is_pos = cn_simplified > 0 if cn_simplified.is_number else False
        status = ""
        if cn_simplified.is_number:
            if not is_int:
                status = " ✗ NOT INTEGER"
                all_positive_int = False
            elif not is_pos:
                status = " ✗ NON-POSITIVE"
                all_positive_int = False
            else:
                status = " ✓"
        print(f"  P_{n} = {cn_simplified}{status}")

    print(f"\nAll positive integers: {all_positive_int}")

    # Disc roots
    disc_roots = nroots(Poly(expand(disc), x))
    print("\nDiscriminant roots:")
    for r in disc_roots:
        r_val = complex(r.evalf())
        print(f"  x = {r_val:.8f}, |x| = {abs(r_val):.8f}, 1/|x| = {1/abs(r_val):.4f}")

    # Growth rate check
    print(f"\nSmallest |root| ≈ {min(abs(complex(r.evalf())) for r in disc_roots):.8f}")
    print(f"Growth rate ≈ {1/min(abs(complex(r.evalf())) for r in disc_roots):.4f}")

    # Also try: what if psi has degree 5?
    print("\n" + "=" * 60)
    print("WHAT IF psi HAS DEGREE 5?")
    print("=" * 60)

    # With degree 5, we have an extra parameter psi_5.
    # The growth constraint gives: psi(1/8) = 1/2.
    # With 5 known psi coefficients (through degree 4), psi_5 is then:
    # sum_{n=0}^{5} psi_n/8^n = 1/2
    # We already have sum_{n=0}^{4} psi_n/8^n = 1/2 for degree 4.
    # So psi_5/8^5 = 0, meaning psi_5 = 0.
    # This means degree 4 IS the right truncation if we want growth rate 8!
    print("If psi(1/8) = 1/2 holds exactly at degree 4,")
    print("then adding psi_5*x^5 requires psi_5/8^5 = 0, so psi_5 = 0.")
    print("This means degree 4 is the natural truncation point.")
    print("(Unless the growth rate constraint is slightly different.)")

# ================================================================
# Also try: NO shift (P = bar cohomology GF directly)
# ================================================================
print("\n" + "=" * 60)
print("ALTERNATIVE: With shift (like sl_2)")
print("=" * 60)
print("For sl_2: P = R_0 + R_1*x + R_2*x^2 + ... = 1 + 0x + x^2 + x^3 + ...")
print("Bar cohomology: H_n = P_{n+2} for n >= 1, H_0 = 1")
print()
print("For sl_3: if same shift applies,")
print("  P = 1 + c_1*x + 8*x^2 + 36*x^3 + 204*x^4 + H_4*x^5 + ...")
print("  with c_1 unknown (might be 0 like sl_2)")
print()
print("Let me compute psi for c_1 = 0:")

a_shifted = [1, 0, 8, 36, 204]
p2_s = [0] * 10
for i in range(len(a_shifted)):
    for j in range(len(a_shifted)):
        if i+j < len(p2_s):
            p2_s[i+j] += a_shifted[i] * a_shifted[j]

q_s = [a_shifted[n] - (p2_s[n-1] if n >= 1 else 0) for n in range(5)]
print(f"  q (= P-xP^2): {q_s}")

# psi = 1/q
psi_s = [Rational(0)] * 5
psi_s[0] = Rational(1, q_s[0])
for n in range(1, 5):
    s = sum(psi_s[k] * q_s[n-k] for k in range(n) if n-k < len(q_s))
    psi_s[n] = -s / q_s[0]

print(f"  psi coefficients: {[float(c) for c in psi_s]}")

psi_at_eighth_s = sum(psi_s[n] * Rational(1,8)**n for n in range(5))
print(f"  psi(1/8) through degree 4 = {float(psi_at_eighth_s):.6f}")
print(f"  Target: 1/2")
