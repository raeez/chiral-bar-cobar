#!/usr/bin/env python3
"""Parametric search: assume W₃ GF is degree-2 algebraic with specific discriminant.

For sl₂: P satisfies x(1+x)P²-(1+x)P+1=0, Δ=(1-3x)(1+x), P(0)=1.
But W₃ P(0)=0, so the form must differ.

Strategy: parametrize by discriminant Δ(x)=(1-rx)(1+sx) and find the
unique quadratic A(x)P²+B(x)P+C(x)=0 matching the 4 known terms
with that discriminant. Check if predictions are integers.
"""
from fractions import Fraction as F
from functools import reduce
from math import gcd

KNOWN = [0, 2, 5, 16, 52]  # p[0]=0, p[1]=2, ...

def ps_mult(a, b, n):
    c = [F(0)] * n
    for i in range(min(len(a), n)):
        if a[i] == 0: continue
        for j in range(min(len(b), n - i)):
            if b[j] == 0: continue
            c[i+j] += a[i] * b[j]
    return c

def ps_pow(a, k, n):
    if k == 0:
        r = [F(0)] * n; r[0] = F(1); return r
    if k == 1:
        return list(a[:n]) + [F(0)] * max(0, n - len(a))
    h = ps_pow(a, k//2, n)
    r = ps_mult(h, h, n)
    if k % 2: r = ps_mult(r, a, n)
    return r


def try_quadratic_with_disc(r, s, known=KNOWN):
    """Try A(x)P² + B(x)P + C(x) = 0 with discriminant Δ = (1-rx)(1+sx).

    B² - 4AC = f(x)² · (1-rx)(1+sx) for some polynomial f(x).

    With P(0)=0, B(0)≠0 (otherwise degenerate).
    Try A, B, C with increasing degrees.
    """
    n = len(known) - 1
    p = [F(v) for v in known]
    nterms = n + 4
    p_ext = p + [F(0)] * (nterms - len(p))
    p2 = ps_mult(p_ext, p_ext, nterms)

    # P = (−B ± √(B²−4AC))/(2A)
    # For P(0) = 0: −B(0) ± √(Δ·f(0)²) = 0 at x=0 (after multiplying by 2A)
    # Actually 2A(0)P(0) + B(0) = ±f(0)√Δ(0) → B(0) = ±f(0)·1 = ±f(0)
    # So P = (−B + f√Δ)/(2A) or P = (−B − f√Δ)/(2A)
    # At x=0: P = (−B(0) + f(0))/(2A(0)) = 0 if B(0) = f(0)
    # Or: P = (−B(0) − f(0))/(2A(0)) = 0 if B(0) = −f(0)

    # Try simplest case: f = constant (f(x) = f₀)
    # Then Δ_eff = f₀² · Δ(x) = f₀²(1−rx)(1+sx) = f₀²(1+(s−r)x−rsx²)
    # B² − 4AC = f₀²(1+(s−r)x−rsx²)

    # Try: A = a₀ + a₁x + a₂x², B = b₀ + b₁x, C = c₀ + c₁x + c₂x²
    # P(0)=0 → C(0) = 0 (from the equation at x=0: A(0)·0 + B(0)·0 + C(0) = 0)
    # So c₀ = 0: C = c₁x + c₂x²

    # The equation A·P² + B·P + C = 0 at x^k gives linear constraint on params.
    # Discriminant constraint: B² − 4AC = f₀²·Δ(x)

    # B² = b₀² + 2b₀b₁x + b₁²x²
    # 4AC = 4(a₀+a₁x+a₂x²)(c₁x+c₂x²) = 4(a₀c₁x + (a₀c₂+a₁c₁)x² + (a₁c₂+a₂c₁)x³ + a₂c₂x⁴)
    # B²−4AC at each power of x:
    # x⁰: b₀² = f₀²
    # x¹: 2b₀b₁ − 4a₀c₁ = f₀²(s−r)
    # x²: b₁² − 4(a₀c₂+a₁c₁) = −f₀²rs
    # x³: −4(a₁c₂+a₂c₁) = 0
    # x⁴: −4a₂c₂ = 0

    # From x⁰: f₀ = ±b₀. Set f₀ = b₀ (positive branch).
    # From x³: a₁c₂ + a₂c₁ = 0
    # From x⁴: a₂c₂ = 0

    # Case: a₂=0 (A is linear), c₂ arbitrary:
    # x³: a₁c₂ = 0. Sub-case a₁=0 → A=a₀ (constant), or c₂=0 → C=c₁x.

    # Sub-case A=a₀, C=c₁x: simplest.
    # x¹: 2b₀b₁ − 4a₀c₁ = b₀²(s−r)
    # x²: b₁² = −b₀²rs  → b₁² = −b₀²rs
    # For b₁ real: rs ≤ 0. Since r > 0 (growth rate), need s ≤ 0.
    # But s > 0 was our assumption (Δ has roots at 1/r and −1/s).
    # With s > 0: b₁² < 0 impossible! So this sub-case fails.

    # Unless s < 0: Δ = (1−rx)(1−|s|x) with both roots positive.
    # Or we allow complex: b₁ = ib₀√(rs). But we want rational coeffs.

    # Sub-case A=a₀, C=c₁x+c₂x²:
    # x³: 0 (since a₁=a₂=0)
    # x²: b₁² − 4a₀c₂ = −b₀²rs
    # x¹: 2b₀b₁ − 4a₀c₁ = b₀²(s−r)
    # Plus: matching the 4 known terms.

    # Params: a₀, b₀, b₁, c₁, c₂. 5 unknowns.
    # Discriminant constraints: 2 equations (x¹, x²). Known term matching: 4 equations (x¹-x⁴).
    # But x¹ matching and discriminant x¹ are DIFFERENT equations.

    # Matching: a₀·P²[k] + B·P[k] + C[k] = 0 for each x^k.
    # x¹: a₀·0 + b₀·2 + c₁ = 0 → c₁ = −2b₀
    # x²: a₀·4 + b₀·5 + b₁·2 + c₂ = 0 → c₂ = −4a₀−5b₀−2b₁
    # x³: a₀·20 + b₀·16 + b₁·5 = 0 → 20a₀+16b₀+5b₁=0
    # x⁴: a₀·89 + b₀·52 + b₁·16 = 0 → 89a₀+52b₀+16b₁=0

    # From x³: a₀ = −(16b₀+5b₁)/20
    # x⁴: 89·(−(16b₀+5b₁)/20)+52b₀+16b₁=0
    # (−1424b₀−445b₁)/20+52b₀+16b₁=0
    # −1424b₀−445b₁+1040b₀+320b₁=0
    # −384b₀−125b₁=0
    # b₁ = −384b₀/125

    r_val = F(r) if isinstance(r, (int, F)) else r
    s_val = F(s) if isinstance(s, (int, F)) else s

    # Set b₀ = 125 (to clear denominators)
    b0 = F(125)
    b1 = F(-384)
    a0 = -(16*b0 + 5*b1) / 20  # = -(2000-1920)/20 = -80/20 = -4
    c1 = -2*b0  # = -250
    c2 = -4*a0 - 5*b0 - 2*b1  # = 16-625+768 = 159

    # Check discriminant constraints:
    # x¹: 2b₀b₁ − 4a₀c₁ = b₀²(s−r)
    lhs1 = 2*b0*b1 - 4*a0*c1
    rhs1 = b0**2 * (s_val - r_val)
    # x²: b₁² − 4a₀c₂ = −b₀²rs
    lhs2 = b1**2 - 4*a0*c2
    rhs2 = -b0**2 * r_val * s_val

    # From lhs1 = rhs1: s−r = lhs1/b₀²
    s_minus_r = lhs1 / b0**2
    # From lhs2 = rhs2: rs = −lhs2/b₀²
    rs_val = -lhs2 / b0**2

    # So r and s are roots of t² − (s−r+2r)t + rs = t² − (s+r)t + rs = 0
    # Wait: s+r = s−r + 2r. But we only know s−r and rs.
    # Actually: (s−r)² = (s+r)² − 4rs → (s+r)² = (s−r)² + 4rs
    sum_rs_sq = s_minus_r**2 + 4*rs_val
    # s+r = ±√(sum_rs_sq)

    # The discriminant is Δ(x) = 1+(s−r)x−rs·x² = 1+αx+βx²
    alpha = s_minus_r
    beta = -rs_val

    # Roots of Δ: x = (−α±√(α²+4β))/(2β) = (−(s−r)±√((s−r)²+4rs))/(-2rs)
    #           = (−(s−r)±(s+r))/(-2rs)
    # Root 1: (−(s−r)+(s+r))/(-2rs) = 2r/(-2rs) = −1/s
    # Root 2: (−(s−r)−(s+r))/(-2rs) = −2s/(-2rs) = 1/r
    # Exactly as expected: Δ has roots at 1/r and −1/s.

    # Radius of convergence = min positive root = 1/r.
    # Growth rate = r.

    # The actual growth rate from our coefficients:
    actual_r = F(1) / (alpha + F(1))  # wrong formula
    # Actually, 1/r is the positive root of Δ, which is 1/r from the formula above.
    # But we computed α=s−r and β=−rs, so Δ = 1+αx+βx².
    # Positive root: 1/r. So r = ...
    # From the derivation: r and s satisfy: s−r = α, rs = −β.
    # So r is a root of: t² − (sum)·t + product = 0 where sum = s+r, product = rs = −β.
    # And s−r = α → s = r+α → product: r(r+α) = −β → r²+αr+β = 0.
    # r = (−α±√(α²−4β))/2

    disc_r = alpha**2 - 4*beta

    # Print results
    print(f"\nWith A={a0}, B={b0}+{b1}x, C={c1}x+{c2}x²:")
    print(f"  Discriminant: Δ = 1 + {alpha}x + {beta}x² = {b0**2}(1 + {alpha}x + {beta}x²)")
    print(f"  s−r = {alpha} = {float(alpha):.6f}")
    print(f"  rs = {-beta} = {float(-beta):.6f}")
    print(f"  Disc of r-equation: {disc_r} = {float(disc_r):.6f}")

    if disc_r >= 0:
        import math
        sqrt_disc = math.sqrt(float(disc_r))
        r1 = float(-alpha + sqrt_disc) / 2
        r2 = float(-alpha - sqrt_disc) / 2
        print(f"  Possible growth rates: {r1:.6f}, {r2:.6f}")
        print(f"  Radius of convergence: {1/r1:.6f}, {1/r2:.6f}")

    # Now predict p₅
    k = 5
    # a₀·P²[5] + b₀·p[5] + b₁·p[4] = 0
    # p₅ = −(a₀·P²[5] + b₁·p[4]) / b₀
    # P²[5] = 2p₁p₄+2p₂p₃ = 2·2·52+2·5·16 = 208+160 = 368
    P2_5 = F(2)*F(2)*F(52) + F(2)*F(5)*F(16)
    p5 = -(a0*P2_5 + b1*KNOWN[4]) / b0
    print(f"  P²[5] = {P2_5}")
    print(f"  Predicted p₅ = {p5} = {float(p5):.6f}")
    print(f"  Integer: {p5.denominator == 1}")

    if p5.denominator == 1 and p5 > 0:
        # Continue predicting
        p_ext = list(KNOWN) + [int(p5)]
        p_ext2 = [F(v) for v in p_ext] + [F(0)] * 10
        for step in range(6, 12):
            pp = ps_mult(p_ext2, p_ext2, step+2)
            pk = -(a0*pp[step] + b1*p_ext2[step-1]) / b0
            p_ext2[step] = pk
            is_int = pk.denominator == 1 and pk > 0
            print(f"  p_{step} = {pk} = {float(pk):.4f} {'✓' if is_int else '✗'}")
            if not is_int:
                break

    return p5


def search_over_disc_params():
    """Try different discriminant forms."""
    print("="*60)
    print("Searching over discriminant parameters")
    print("Δ(x) = 1 + αx + βx² with α = s-r, β = -rs")
    print("="*60)

    # The matching equations fix: a₀=-4, b₀=125, b₁=-384, c₁=-250, c₂=159
    # The discriminant is FORCED by the matching to be:
    # B²-4AC = (125-384x)² - 4(-4)(−250x+159x²)
    #        = 15625 - 96000x + 147456x² + 16(-250x+159x²)
    #        = 15625 - 96000x + 147456x² - 4000x + 2544x²
    #        = 15625 - 100000x + 150000x²

    b0, b1, a0, c1, c2 = F(125), F(-384), F(-4), F(-250), F(159)
    B2 = [b0**2, 2*b0*b1, b1**2]  # b₀² + 2b₀b₁x + b₁²x²
    AC = [F(0), a0*c1, a0*c2]  # a₀c₁x + a₀c₂x²
    disc = [B2[i] - 4*AC[i] if i < len(B2) else F(0) for i in range(3)]

    print(f"\nForced discriminant from matching:")
    print(f"  A = {a0}")
    print(f"  B = {b0} + {b1}x")
    print(f"  C = {c1}x + {c2}x²")
    print(f"  B² = {B2}")
    print(f"  4AC = {[4*v for v in AC]}")
    print(f"  Δ = {disc[0]} + {disc[1]}x + {disc[2]}x²")

    # Factor disc
    d0, d1, d2 = disc
    print(f"  = {d0} + {d1}x + {d2}x²")

    # Roots: x = (-d1 ± √(d1²-4d0d2))/(2d2)
    inner = d1**2 - 4*d0*d2
    print(f"  Inner discriminant: {inner} = {float(inner):.4f}")

    import math
    if float(inner) >= 0:
        sqrt_inner = F(int(math.isqrt(int(inner)))) if inner >= 0 and math.isqrt(int(inner))**2 == int(inner) else None
        if sqrt_inner is not None:
            print(f"  √(inner) = {sqrt_inner} (exact)")
            root1 = (-d1 + sqrt_inner) / (2*d2)
            root2 = (-d1 - sqrt_inner) / (2*d2)
            print(f"  Roots: {root1} = {float(root1):.6f}, {root2} = {float(root2):.6f}")
            print(f"  Growth rate: {F(1)/root1} = {float(F(1)/root1):.6f} and {F(1)/root2} = {float(F(1)/root2):.6f}")
            print(f"  Factored: Δ = {d2}(x-{root1})(x-{root2})")
        else:
            sqrt_f = math.sqrt(float(inner))
            root1 = float(-d1 + sqrt_f) / float(2*d2)
            root2 = float(-d1 - sqrt_f) / float(2*d2)
            print(f"  √(inner) ≈ {sqrt_f:.6f} (irrational)")
            print(f"  Roots ≈ {root1:.6f}, {root2:.6f}")
            print(f"  Growth rate ≈ {1/root1:.6f}, {1/root2:.6f}")

    # Scale to make it nicer
    # 15625 = 5⁶ = 125², -100000 = -10⁵ = -4·25000, 150000 = 15·10⁴
    # GCD(15625, 100000, 150000) = 625
    g = gcd(gcd(int(d0), abs(int(d1))), int(d2))
    print(f"\n  GCD of coefficients: {g}")
    print(f"  Δ/{g} = {d0//g} + {d1//g}x + {d2//g}x²")

    # p₅ prediction
    P2_5 = F(368)
    p5 = -(a0*P2_5 + b1*KNOWN[4]) / b0
    print(f"\n  p₅ = {p5} = {float(p5):.6f}")

    # Now try with A(x) linear (not constant)
    print("\n" + "="*60)
    print("Trying A(x) = a₀ + a₁x:")
    print("="*60)

    # Matching equations with A = a₀+a₁x, B = b₀+b₁x, C = c₁x+c₂x²:
    # x¹: b₀·2+c₁ = 0  →  c₁ = -2b₀
    # x²: a₀·4+b₀·5+b₁·2+c₂ = 0  →  c₂ = -4a₀-5b₀-2b₁
    # x³: a₀·20+a₁·4+b₀·16+b₁·5 = 0
    # x⁴: a₀·89+a₁·20+b₀·52+b₁·16 = 0

    # 2 equations in 4 unknowns (a₀,a₁,b₀,b₁): 2-dim family.
    # Add discriminant constraint Δ(1/r) = 0 for specific r: 1 more equation.
    # Still 1-dim family. Need another constraint.

    # Try: Δ(x) = (1-rx)(1+sx) with RATIONAL r,s.
    # B²-4AC must have the form f(x)²·(1-rx)(1+sx).
    # B²-4AC is a polynomial (degree ≤ 4 if A is linear, B linear, C quadratic).
    # Actually deg(B²)=2, deg(4AC) ≤ 1+2=3.
    # So B²-4AC has degree ≤ 3.
    # For it to factor as f(x)²·(1-rx)(1+sx), we need:
    # If f is constant: deg=2 (the simplest case)
    # If f is linear: deg=4 (but our poly is deg ≤ 3), so f must be constant.
    # So f = f₀, and Δ is degree ≤ 3. But (1-rx)(1+sx) is degree 2.
    # So B²-4AC has degree ≤ 3, and its first two roots are at 1/r and -1/s.
    # The degree-3 term must be zero for it to be degree 2 (or it factors differently).

    # Let's just compute B²-4AC for the 2-parameter family.
    # With b₀=1 (normalization):
    # c₁ = -2, c₂ = -4a₀-5-2b₁
    # From x³: 20a₀+4a₁+16+5b₁=0 → a₁ = -(20a₀+16+5b₁)/4
    # From x⁴: 89a₀+20a₁+52+16b₁=0 → substituting a₁:
    #   89a₀+20·(-(20a₀+16+5b₁)/4)+52+16b₁=0
    #   89a₀-100a₀-80-25b₁+52+16b₁=0
    #   -11a₀-28-9b₁=0 → a₀=-(28+9b₁)/11

    # So the free parameter is b₁. Let's parametrize.
    print("\nFree parameter: b₁ (with b₀=1)")
    print("a₀ = -(28+9b₁)/11")
    print("a₁ = -(20a₀+16+5b₁)/4")
    print("c₁ = -2, c₂ = -4a₀-5-2b₁")

    # Discriminant: B²-4AC
    # B = 1+b₁x, A = a₀+a₁x, C = -2x+c₂x²
    # B² = 1+2b₁x+b₁²x²
    # 4AC = 4(a₀+a₁x)(-2x+c₂x²)
    #      = 4(-2a₀x+a₀c₂x²-2a₁x²+a₁c₂x³)
    #      = -8a₀x+(4a₀c₂-8a₁)x²+4a₁c₂x³
    # B²-4AC = 1+(2b₁+8a₀)x+(b₁²-4a₀c₂+8a₁)x²-4a₁c₂x³

    for b1_num in range(-30, 31):
        b1_val = F(b1_num, 10)  # try b₁ in steps of 0.1

        a0_val = -(F(28) + 9*b1_val) / 11
        a1_val = -(20*a0_val + 16 + 5*b1_val) / 4
        c2_val = -4*a0_val - 5 - 2*b1_val
        c1_val = F(-2)

        # Discriminant
        d0 = F(1)
        d1 = 2*b1_val + 8*a0_val
        d2 = b1_val**2 - 4*a0_val*c2_val + 8*a1_val
        d3 = -4*a1_val*c2_val

        # For Δ to be degree 2, need d3=0
        if d3 != 0:
            continue

        # d3 = -4a₁c₂ = 0 requires a₁=0 or c₂=0
        # a₁ = -(20a₀+16+5b₁)/4
        # c₂ = -4a₀-5-2b₁

        # If a₁=0: 20a₀+16+5b₁=0 → a₀=-(16+5b₁)/20
        # Combined with a₀=-(28+9b₁)/11:
        # -(16+5b₁)/20 = -(28+9b₁)/11
        # (16+5b₁)/20 = (28+9b₁)/11
        # 11(16+5b₁) = 20(28+9b₁)
        # 176+55b₁ = 560+180b₁
        # -384 = 125b₁ → b₁ = -384/125

        # If c₂=0: -4a₀-5-2b₁=0 → a₀=-(5+2b₁)/4
        # Combined with a₀=-(28+9b₁)/11:
        # -(5+2b₁)/4 = -(28+9b₁)/11
        # (5+2b₁)/4 = (28+9b₁)/11
        # 55+22b₁ = 112+36b₁
        # -57 = 14b₁ → b₁ = -57/14

    # Case a₁=0 (A is constant):
    print("\n--- Case a₁=0 (A constant) ---")
    b1_exact = F(-384, 125)
    a0_exact = -(F(28) + 9*b1_exact) / 11
    a1_exact = F(0)
    c1_exact = F(-2)
    c2_exact = -4*a0_exact - 5 - 2*b1_exact

    d0 = F(1)
    d1 = 2*b1_exact + 8*a0_exact
    d2 = b1_exact**2 - 4*a0_exact*c2_exact

    print(f"b₁ = {b1_exact}, a₀ = {a0_exact}, c₂ = {c2_exact}")
    print(f"Δ = {d0} + {d1}x + {d2}x²")

    # Factor
    inner = d1**2 - 4*d0*d2
    print(f"Inner disc = {inner}")

    # Predict p₅ (same as before since a₁=0 just means same a₀)
    P2_5 = F(368)
    p5 = -(a0_exact*P2_5 + b1_exact*KNOWN[4]) / F(1)  # b₀=1
    print(f"p₅ = {p5} = {float(p5):.6f}")

    # Case c₂=0 (C is linear):
    print("\n--- Case c₂=0 (C linear) ---")
    b1_exact2 = F(-57, 14)
    a0_exact2 = -(F(28) + 9*b1_exact2) / 11
    a1_exact2 = -(20*a0_exact2 + 16 + 5*b1_exact2) / 4
    c2_exact2 = F(0)

    d0 = F(1)
    d1 = 2*b1_exact2 + 8*a0_exact2
    d2 = b1_exact2**2 + 8*a1_exact2

    print(f"b₁ = {b1_exact2}, a₀ = {a0_exact2}, a₁ = {a1_exact2}")
    print(f"Δ = {d0} + {d1}x + {d2}x²")

    inner = d1**2 - 4*d0*d2
    print(f"Inner disc = {inner}")

    # Factor Δ
    if inner >= 0:
        import math
        si = int(inner * 1)  # it's a Fraction
        # Check if perfect square
        isq = math.isqrt(si.numerator) if hasattr(si, 'numerator') else math.isqrt(int(inner))
        si_num = inner.numerator
        si_den = inner.denominator
        sqrt_num = math.isqrt(si_num)
        sqrt_den = math.isqrt(si_den)
        if sqrt_num**2 == si_num and sqrt_den**2 == si_den:
            sqrt_inner = F(sqrt_num, sqrt_den)
            root1 = (-d1 + sqrt_inner) / (2*d2)
            root2 = (-d1 - sqrt_inner) / (2*d2)
            print(f"Δ roots: {root1} = {float(root1):.6f}, {root2} = {float(root2):.6f}")
            print(f"Growth rate: {float(F(1)/root1):.6f} and {float(F(1)/root2):.6f}")
        else:
            sf = math.sqrt(float(inner))
            r1 = float(-d1 + sf) / float(2*d2)
            r2 = float(-d1 - sf) / float(2*d2)
            print(f"Δ roots ≈ {r1:.6f}, {r2:.6f}")
            print(f"Growth rate ≈ {1/r1:.6f}, {1/r2:.6f}")

    # Predict p₅
    p5_2 = -(a0_exact2*P2_5 + a1_exact2*F(89) + b1_exact2*KNOWN[4]) / F(1)
    print(f"p₅ = {p5_2} = {float(p5_2):.6f}")

    # Now try: ASSUME specific growth rates and solve
    print("\n" + "="*60)
    print("Assuming specific growth rates (positive root of Δ at 1/r)")
    print("="*60)

    # For the c₂=0 case, Δ = 1 + d₁x + d₂x² has root at 1/r:
    # 1 + d₁/r + d₂/r² = 0 → r² + d₁r + d₂ = 0
    # For the a₁=0 case, same.

    # In the general 2-parameter family (b₁ free), we need
    # Δ(1/r) = 0 as an additional constraint.
    # This gives a unique b₁ for each r.

    for r_try in [F(3), F(4), F(5), F(6), F(7), F(8),
                  F(7,2), F(9,2), F(11,2), F(13,2),
                  F(10,3), F(13,3), F(16,3)]:

        # a₀ = -(28+9b₁)/11
        # a₁ = -(20a₀+16+5b₁)/4
        # c₂ = -4a₀-5-2b₁

        # Δ = 1 + (2b₁+8a₀)x + (b₁²-4a₀c₂+8a₁)x² + (-4a₁c₂)x³
        # Δ(1/r) = 0 (constraint #1)
        # For Δ to be exactly degree 2: d₃ = -4a₁c₂ = 0 (constraint #2, optional)

        # Without d₃=0 constraint: Δ is degree 3.
        # Δ(x) = 1+d₁x+d₂x²+d₃x³ with root at 1/r:
        # 1 + d₁/r + d₂/r² + d₃/r³ = 0

        # Express all in terms of b₁:
        # a₀ = -(28+9b)/11  where b = b₁
        # a₁ = -(20a₀+16+5b)/4 = -(20·(-(28+9b)/11)+16+5b)/4
        #     = -((-560-180b)/11+16+5b)/4
        #     = -((-560-180b+176+55b)/11)/4
        #     = -((-384-125b)/11)/4
        #     = (384+125b)/44
        # c₂ = -4·(-(28+9b)/11)-5-2b = (112+36b)/11-5-2b = (112+36b-55-22b)/11 = (57+14b)/11

        # d₁ = 2b+8·(-(28+9b)/11) = 2b+(-224-72b)/11 = (22b-224-72b)/11 = (-50b-224)/11
        # d₂ = b²-4a₀c₂+8a₁
        #     = b²-4·(-(28+9b)/11)·(57+14b)/11+8·(384+125b)/44
        #     = b²+4(28+9b)(57+14b)/121+(384+125b)·2/11
        #     = b²+(4(1596+392b+513b+126b²))/121+(768+250b)/11
        #     = b²+(4(1596+905b+126b²))/121+(768+250b)/11
        #     = b²+(6384+3620b+504b²)/121+(768+250b)/11

        # This is getting unwieldy. Let me just use the parametric formula numerically.
        b = F(0)  # placeholder
        # Use sympy-like approach: express d₁, d₂, d₃ as functions of b₁ and solve

        # Let me just try specific b₁ values and check
        pass

    # Better approach: directly solve for b₁ from Δ(1/r) = 0
    # for specific rational r values
    for r_num, r_den in [(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
                          (7,2),(9,2),(11,2),(13,2),(15,2),
                          (10,3),(13,3),(16,3),(17,3),(19,3),
                          (5,2),(3,2),(4,3),(7,3),(8,3)]:
        r = F(r_num, r_den)

        # Δ(1/r) = 1 + d₁/r + d₂/r² + d₃/r³ = 0
        # where d₁, d₂, d₃ are polynomial functions of b₁.
        # d₁ = (-50b-224)/11
        # d₂ = b²+(6384+3620b+504b²)/121+(768+250b)/11
        # d₃ = -4a₁c₂ = -4·(384+125b)/44·(57+14b)/11 = -(384+125b)(57+14b)/121

        # Let me compute d₂ more carefully:
        # d₂ = b₁² - 4a₀c₂ + 8a₁
        # = b₁² + 4(28+9b₁)(57+14b₁)/(11²) + 8(384+125b₁)/44
        # = b₁² + 4(1596+392b₁+513b₁+126b₁²)/121 + (384+125b₁)·2/11
        # = b₁² + (6384+3620b₁+504b₁²)/121 + (768+250b₁)/11

        # Convert all to denominator 121:
        # = 121b₁²/121 + (6384+3620b₁+504b₁²)/121 + (768+250b₁)·11/121
        # = (121b₁² + 6384+3620b₁+504b₁² + 8448+2750b₁)/121
        # = (625b₁² + 6370b₁ + 14832)/121

        b_sym = None  # will solve numerically
        # Δ(1/r) = 1 + (-50b-224)/(11r) + (625b²+6370b+14832)/(121r²) + (stuff)/r³ = 0

        # d₃ = -(384+125b)(57+14b)/121 = -(21888+5376b+7125b+1750b²)/121
        #     = -(1750b²+12501b+21888)/121

        # So Δ(1/r) = 1 + (-50b-224)/(11r) + (625b²+6370b+14832)/(121r²) - (1750b²+12501b+21888)/(121r³) = 0

        # Multiply by 121r³:
        # 121r³ + (-50b-224)·11r² + (625b²+6370b+14832)r - (1750b²+12501b+21888) = 0

        # Collect terms in b:
        # constant: 121r³ - 224·11r² + 14832r - 21888
        # b: -50·11r² + 6370r - 12501
        # b²: 625r - 1750

        const = 121*r**3 - 2464*r**2 + 14832*r - 21888
        lin = -550*r**2 + 6370*r - 12501
        quad = 625*r - 1750

        if quad == 0:
            if lin == 0:
                continue
            b_sol = [-const/lin]
        else:
            disc_b = lin**2 - 4*quad*const
            if disc_b < 0:
                continue
            # Check if perfect square
            dn = disc_b.numerator
            dd = disc_b.denominator
            import math
            sn = math.isqrt(abs(dn))
            sd = math.isqrt(dd)
            if sn*sn == dn and sd*sd == dd:
                sqrt_db = F(sn, sd)
                b_sol = [(-lin+sqrt_db)/(2*quad), (-lin-sqrt_db)/(2*quad)]
            else:
                sf = math.sqrt(float(disc_b))
                b_sol = [F(0)]  # placeholder, skip non-rational
                continue

        for b_val in b_sol:
            a0_v = -(F(28)+9*b_val)/11
            a1_v = (384+125*b_val)/44
            c1_v = F(-2)
            c2_v = (57+14*b_val)/11

            # Predict p₅
            P2_5 = F(368)
            # d(a₀+a₁x)P²+(1+b₁x)P+(-2x+c₂x²) = 0
            # at x⁵: a₀·P²[5]+a₁·P²[4]+p₅+b_val·52 = 0
            # Wait, the equation is for b₀=1.
            # (a₀+a₁x)(P²) + (1+b_val·x)P + (-2x+c₂x²) = 0
            # Coeff of x⁵:
            # a₀·P²[5] + a₁·P²[4] + 1·p₅ + b_val·p₄ + 0 = 0
            # (c₂ only contributes at x² and x³ from c₂x²·P^0 terms... wait C=c₁x+c₂x²)
            # C contributes to x^k only at k=1 (c₁) and k=2 (c₂). For k=5: nothing from C.

            p5_v = -(a0_v*P2_5 + a1_v*F(89) + b_val*F(52))
            is_int = p5_v.denominator == 1 and p5_v > 0

            if is_int:
                d1_v = (-50*b_val-224)/11
                d2_v = (625*b_val**2+6370*b_val+14832)/121
                d3_v = -(1750*b_val**2+12501*b_val+21888)/121

                print(f"\nr = {r} = {float(r):.4f}, b₁ = {b_val} = {float(b_val):.4f}")
                print(f"  a₀={float(a0_v):.6f}, a₁={float(a1_v):.6f}, c₂={float(c2_v):.6f}")
                print(f"  *** p₅ = {int(p5_v)} ***")
                print(f"  Δ = 1 + {float(d1_v):.6f}x + {float(d2_v):.6f}x² + {float(d3_v):.6f}x³")

                # Check Δ is degree 2 (d₃ ≈ 0)?
                if abs(float(d3_v)) < 0.001:
                    print(f"  Δ is degree 2! (d₃ ≈ 0)")

                # Extend the sequence
                p_ext = [F(0), F(2), F(5), F(16), F(52), p5_v] + [F(0)]*10
                all_int = True
                for step in range(6, 12):
                    pp = ps_mult(p_ext[:step+1], p_ext[:step+1], step+2)
                    # Coeff of x^step: a₀·pp[step]+a₁·pp[step-1]+p_ext[step]+b_val·p_ext[step-1]=0
                    pk = -(a0_v*pp[step] + a1_v*pp[step-1] + b_val*p_ext[step-1])
                    p_ext[step] = pk
                    is_int_k = pk.denominator == 1 and pk > 0
                    print(f"  p_{step} = {pk} = {float(pk):.4f} {'✓' if is_int_k else '✗'}")
                    if not is_int_k:
                        all_int = False
                        break
                if all_int:
                    print(f"  *** ALL INTEGER through p_11! ***")
                    print(f"  Sequence: {[int(p_ext[i]) for i in range(1, 12)]}")


if __name__ == "__main__":
    search_over_disc_params()
