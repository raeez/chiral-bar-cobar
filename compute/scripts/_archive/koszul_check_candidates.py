#!/usr/bin/env python3
"""Check OEIS candidate sequences against the Koszul constraint.

For a Koszul pair: f_A(t) * f_{A!}(-t) = 1
This means r_n = sum_{k=0}^{n-1} (-1)^{n-k+1} r_k H_{n-k}
where H_n = bar cohomology dims and r_n = algebra Hilbert series dims.
ALL r_n must be non-negative.
"""

def check_koszul(name, H_seq):
    """Check Koszul constraint: compute algebra series r_n and verify non-negativity."""
    N = len(H_seq)
    r = [0] * N
    r[0] = 1  # H_0 = 1 always

    print(f"\n{'='*50}")
    print(f"{name}")
    print(f"H = {H_seq[:10]}{'...' if N > 10 else ''}")
    print(f"{'='*50}")

    all_positive = True
    for n in range(1, N):
        total = 0
        for k in range(n):
            sign = (-1) ** (n - k + 1)
            total += sign * r[k] * H_seq[n - k]
        r[n] = total
        status = "✓" if total >= 0 else "✗ NEGATIVE"
        if total < 0:
            all_positive = False
        if n <= 15 or total < 0:
            print(f"  r_{n} = {total} {status}")

    print(f"\nAll r_n >= 0 through degree {N-1}: {all_positive}")
    return r, all_positive


# Known sl_2 bar cohomology (Riordan numbers R(n+2))
sl2_H = [1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298, 30537, 83097]

# A030112: 8 glass plates
A030112 = [1, 8, 36, 204, 1086, 5916, 31998, 173502, 940005, 5094220,
           27604798, 149590922, 810627389, 4392774126, 23804329059]

# A290357: 8th Euler transform (offset: first term is for n=0 or n=1?)
# Terms: 1, 1, 8, 36, 204, 1002, 5244, 26328, 133476, 667335
# The sequence starts 1, 1, 8, 36, 204 — the first '1' might be for n=0
# Our H starts: H_0=1, so we need H_1=8. Let's try both offsets.
A290357_v1 = [1, 8, 36, 204, 1002, 5244, 26328, 133476, 667335]  # skip first 1
A290357_v2 = [1, 1, 8, 36, 204, 1002, 5244, 26328, 133476, 667335]  # include both 1s

print("VALIDATION: sl_2")
r_sl2, ok_sl2 = check_koszul("sl_2 bar cohomology (Riordan)", sl2_H)

print("\n" + "#"*60)
print("CANDIDATE TESTING: sl_3")
print("#"*60)

r_A030112, ok_A030112 = check_koszul("A030112 (8 glass plates)", A030112)
r_A290357_v1, ok_v1 = check_koszul("A290357 v1 (skip leading 1)", A290357_v1)
r_A290357_v2, ok_v2 = check_koszul("A290357 v2 (include leading 1)", A290357_v2)

# Now try a broader search: what value of H_4 makes r_4,...,r_10 all non-negative?
print("\n" + "#"*60)
print("EXHAUSTIVE SEARCH for H_4")
print("#"*60)

H_known = [1, 8, 36, 204]  # H_0, H_1, H_2, H_3

# For each candidate H_4, compute r_4 and check non-negativity
# r_4 = 1744 - H_4, so H_4 <= 1744.
# We need r_4 >= 0: H_4 <= 1744.
# We also need r_5 >= 0, which depends on H_5.
# Without knowing H_5, we can't constrain further from r_5 alone.

# But we can compute which H_4 values are consistent with the growth rate.
# If the sequence grows like C * alpha^n, then H_4 / H_3 should be between
# H_3/H_2 and something reasonable.

# Ratios: H_2/H_1 = 36/8 = 4.5, H_3/H_2 = 204/36 = 5.667
# The growth rate alpha satisfies: successive ratios converge to alpha.
# For sl_2: ratios 2, 2.5, 2.4, 2.53, 2.55 → converges to 2+2√2 ≈ 4.828

# For sl_3: ratios 8, 4.5, 5.667 → the growth rate could be anywhere.
# If ratios increase: H_4/204 > 5.667 → H_4 > 1156
# If ratios stay around 5.5-6: H_4 ≈ 1100-1200

print(f"\nKoszul upper bound: H_4 <= 1744")
print(f"Growth consistency (H_4/H_3 > H_2/H_1=4.5): H_4 > {int(204*4.5)} = 918")
print(f"Growth consistency (H_4/H_3 ≈ H_3/H_2=5.667): H_4 ≈ {int(204*5.667)}")

# Let's also check: for the sl_2 case, what is the relationship between
# the successive ratios H_{n+1}/H_n and the actual growth rate?
print("\nsl_2 ratios and growth rate (α = 2+2√2 ≈ 4.828):")
for i in range(1, len(sl2_H)-1):
    ratio = sl2_H[i+1] / sl2_H[i]
    print(f"  H_{i+1}/H_{i} = {sl2_H[i+1]}/{sl2_H[i]} = {ratio:.4f}")

# For the three candidates, print the ratios
print("\nA030112 ratios:")
for i in range(len(A030112)-1):
    ratio = A030112[i+1] / A030112[i]
    print(f"  a_{i+1}/a_{i} = {A030112[i+1]}/{A030112[i]} = {ratio:.4f}")

print("\nA290357 ratios:")
for i in range(len(A290357_v1)-1):
    ratio = A290357_v1[i+1] / A290357_v1[i]
    print(f"  a_{i+1}/a_{i} = {A290357_v1[i+1]}/{A290357_v1[i]} = {ratio:.4f}")

# Verify: for sl_2, the growth rate is 2+2*sqrt(2)
import math
alpha_sl2 = 2 + 2*math.sqrt(2)
print(f"\nsl_2 theoretical growth rate: {alpha_sl2:.6f}")
print(f"  Last computed ratio: {sl2_H[-1]/sl2_H[-2]:.6f}")

# For A030112, the growth rate is w(8) = 1/(2*cos(8*pi/17))
alpha_A030112 = 1 / (2 * math.cos(8 * math.pi / 17))
print(f"\nA030112 theoretical growth rate: {alpha_A030112:.6f}")
print(f"  Last computed ratio: {A030112[-1]/A030112[-2]:.6f}")
