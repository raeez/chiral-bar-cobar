#!/usr/bin/env python3
"""Extended computation for sl_3 bar cohomology via cubic phi-ansatz.

Equation: t * phi(t) * P^2 - P + 1 = 0
sl_2: phi = 1+t, gives Riordan numbers (PROVED)
sl_3: phi = 1-7t+29t^2-131t^3, gives 1, 8, 36, 204, 1797, ...

Compute extended series, growth rate, discriminant analysis,
and full Koszul check.
"""

from sympy import (symbols, sqrt, series, Rational, solve, expand,
                   factor, simplify, S, Abs, re, im, N, Poly, roots,
                   nroots, cos, pi)

t = symbols('t')

# ================================================================
# sl_2 validation
# ================================================================
print("=" * 60)
print("sl_2: phi = 1+t")
print("=" * 60)

phi_sl2 = 1 + t
disc_sl2 = 1 - 4*t*phi_sl2
P_sl2 = (1 - sqrt(disc_sl2)) / (2*t*phi_sl2)
P_sl2_series = series(P_sl2, t, 0, 16)

print("Bar cohomology H_n (sl_2):")
sl2_H = []
for n in range(15):
    cn = P_sl2_series.coeff(t, n)
    sl2_H.append(int(cn))
    if n <= 12:
        print(f"  H_{n} = {cn}")

# Discriminant roots
disc_roots_sl2 = solve(disc_sl2, t)
print(f"\nDiscriminant roots: {disc_roots_sl2}")
for r in disc_roots_sl2:
    print(f"  t = {r} ≈ {float(r.evalf()):.6f}, 1/|t| = {float(abs(1/r.evalf())):.6f}")

# Growth rate
print(f"\nGrowth rate = 1/|smallest root| = {float(abs(1/disc_roots_sl2[1].evalf())):.6f}")
print(f"dim(sl_2) = 3")
print(f"Ratio growth/dim = {float(abs(1/disc_roots_sl2[1].evalf()))/3:.6f}")

# Koszul check
print("\nKoszul algebra series r_n:")
r_sl2 = [0] * 15
r_sl2[0] = 1
for n in range(1, 15):
    total = 0
    for k in range(n):
        total += ((-1)**(n-k+1)) * r_sl2[k] * sl2_H[n-k]
    r_sl2[n] = total
    status = "✓" if total >= 0 else "✗ NEG"
    print(f"  r_{n} = {total} {status}")

# ================================================================
# sl_3: cubic phi
# ================================================================
print("\n" + "=" * 60)
print("sl_3: phi = 1 - 7t + 29t^2 - 131t^3")
print("=" * 60)

phi_sl3 = 1 - 7*t + 29*t**2 - 131*t**3
disc_sl3 = expand(1 - 4*t*phi_sl3)
print(f"Discriminant: {disc_sl3}")

P_sl3 = (1 - sqrt(1 - 4*t*phi_sl3)) / (2*t*phi_sl3)
P_sl3_series = series(P_sl3, t, 0, 20)

print("\nBar cohomology H_n (sl_3, cubic phi):")
sl3_H = []
for n in range(18):
    cn = P_sl3_series.coeff(t, n)
    sl3_H.append(int(cn))
    print(f"  H_{n} = {cn}")

# Discriminant roots
print(f"\nDiscriminant: {disc_sl3}")
disc_poly = Poly(disc_sl3, t)
disc_roots_sl3 = nroots(disc_poly)
print("Discriminant roots (numerical):")
for r in disc_roots_sl3:
    r_eval = complex(r.evalf())
    print(f"  t = {r_eval:.6f}, |t| = {abs(r_eval):.6f}, 1/|t| = {1/abs(r_eval):.6f}")

# Smallest |root|
min_abs = min(abs(complex(r.evalf())) for r in disc_roots_sl3)
print(f"\nSmallest |root| = {min_abs:.6f}")
print(f"Growth rate = 1/smallest|root| = {1/min_abs:.6f}")
print(f"dim(sl_3) = 8")
print(f"Ratio growth/dim = {1/min_abs/8:.6f}")

# Check ratios
print("\nSuccessive ratios H_{n+1}/H_n:")
for i in range(1, min(16, len(sl3_H)-1)):
    if sl3_H[i] != 0:
        ratio = sl3_H[i+1] / sl3_H[i]
        print(f"  H_{i+1}/H_{i} = {sl3_H[i+1]}/{sl3_H[i]} = {ratio:.6f}")

# Koszul check
print("\nKoszul algebra series r_n:")
r_sl3 = [0] * len(sl3_H)
r_sl3[0] = 1
for n in range(1, len(sl3_H)):
    total = 0
    for k in range(n):
        total += ((-1)**(n-k+1)) * r_sl3[k] * sl3_H[n-k]
    r_sl3[n] = total
    status = "✓" if total >= 0 else "✗ NEG"
    print(f"  r_{n} = {total} {status}")

# ================================================================
# phi roots (where denominator vanishes)
# ================================================================
print("\n" + "=" * 60)
print("phi(t) roots (poles of P)")
print("=" * 60)

phi_roots = nroots(Poly(phi_sl3, t))
print("Roots of phi(t) = 1 - 7t + 29t^2 - 131t^3:")
for r in phi_roots:
    r_eval = complex(r.evalf())
    print(f"  t = {r_eval:.6f}, |t| = {abs(r_eval):.6f}")

# ================================================================
# Compare growth rates
# ================================================================
print("\n" + "=" * 60)
print("GROWTH RATE COMPARISON")
print("=" * 60)

import math

alpha_sl2 = 2 + 2*math.sqrt(2)
print(f"sl_2: growth rate = 2+2√2 = {alpha_sl2:.6f}")
print(f"  dim(sl_2) = 3, ratio = {alpha_sl2/3:.4f}")

alpha_sl3 = 1/min_abs
print(f"sl_3 (cubic phi): growth rate = {alpha_sl3:.6f}")
print(f"  dim(sl_3) = 8, ratio = {alpha_sl3/8:.4f}")

alpha_A030112 = 1 / (2 * math.cos(8 * math.pi / 17))
print(f"A030112 (glass plates): growth rate = {alpha_A030112:.6f}")
print(f"  dim(sl_3) = 8, ratio = {alpha_A030112/8:.4f}")

print(f"\nsl_2 ratio (growth/dim) = {alpha_sl2/3:.4f}")
print(f"sl_3 cubic phi ratio = {alpha_sl3/8:.4f}")
print(f"A030112 ratio = {alpha_A030112/8:.4f}")
print(f"\nConsistency check: sl_2 ratio > 1 means growth > dim.")
print(f"If pattern holds, sl_3 should also have growth > dim = 8.")
print(f"Cubic phi growth = {alpha_sl3:.2f}: {'CONSISTENT (>8)' if alpha_sl3 > 8 else 'INCONSISTENT (<8)'}")
print(f"A030112 growth = {alpha_A030112:.2f}: {'CONSISTENT (>8)' if alpha_A030112 > 8 else 'INCONSISTENT (<8)'}")
