#!/usr/bin/env python3
"""
Compute bar cohomology dimensions for chiral algebras.

For V^k(g) at generic level, the bar cohomology H^n = dim (A^!)_n
where A^! is the chiral Koszul dual. The generating function for
sl_2 is the Riordan number GF: P(x) = (1-sqrt((1-3x)/(1+x)))/(2x).

We hypothesize that for sl_N with d = dim(g) = N^2-1, the GF is:
  P_d(x) = (1 - sqrt((1-dx)/(1+x))) / (2x)

and that H^n = P_d coefficient at index n+d (shift by d = dim g).

For W_3, Yangian, etc., we use direct algebraic computation of the
quadratic Koszul dual dimensions.
"""

from fractions import Fraction
import sys


def sqrt_series(f_coeffs, num_terms):
    """
    Compute the power series sqrt(f) where f = sum f_coeffs[k] x^k.
    Returns list of coefficients of sqrt(f) up to x^{num_terms-1}.
    Uses exact rational arithmetic.
    """
    g = [Fraction(0)] * num_terms
    if not f_coeffs or f_coeffs[0] == 0:
        raise ValueError("f(0) must be nonzero for sqrt")

    g[0] = Fraction(1)  # sqrt(f(0)) = 1 when f(0) = 1

    for n in range(1, num_terms):
        # g(x)^2 = f(x)
        # 2*g[0]*g[n] + sum_{k=1}^{n-1} g[k]*g[n-k] = f[n]
        s = sum(g[k] * g[n-k] for k in range(1, n))
        f_n = f_coeffs[n] if n < len(f_coeffs) else Fraction(0)
        g[n] = (f_n - s) / (2 * g[0])

    return g


def product_series(a, b, num_terms):
    """Multiply two power series (as coefficient lists)."""
    c = [Fraction(0)] * num_terms
    for i in range(min(len(a), num_terms)):
        for j in range(min(len(b), num_terms - i)):
            c[i+j] += a[i] * b[j]
    return c


def quotient_series(f_coeffs, num_terms):
    """
    Compute (1-dx)/(1+x) as a series.
    f_coeffs = coefficients of (1-dx)/(1+x).
    But it's easier to compute directly.
    """
    pass


def compute_Pd(d, num_terms):
    """
    Compute the generating function P_d(x) = (1-sqrt((1-dx)/(1+x)))/(2x)
    as a power series up to x^{num_terms-1}.

    Returns list of Fraction coefficients.
    """
    d = Fraction(d)

    # Step 1: Compute f(x) = (1-dx)/(1+x) as a series
    # (1-dx) * (1+x)^{-1} = (1-dx) * sum_{k>=0} (-x)^k
    f = [Fraction(0)] * (num_terms + 2)
    for k in range(num_terms + 2):
        # coefficient of x^k in (1-dx)*(1-x+x^2-...) = (-1)^k - d*(-1)^{k-1}
        f[k] = Fraction((-1)**k)
        if k >= 1:
            f[k] += -d * Fraction((-1)**(k-1))
        # = (-1)^k + d*(-1)^k = (-1)^k * (1+d) for k >= 1
        # Wait: (-1)^k - d*(-1)^{k-1} = (-1)^k + d*(-1)^k = (-1)^k (1+d) for k >= 1
        # And for k=0: f[0] = 1

    # Verify: f[0] = 1, f[1] = -1 - d*1 = -(1+d), f[2] = 1 + d*(-1) = 1+d, ...
    # Actually let me recompute more carefully.
    # (1-dx) * 1/(1+x) = (1-dx) * sum_{k>=0} (-1)^k x^k
    # Coeff of x^n: (-1)^n + (-d)*(-1)^{n-1} [for n >= 1]
    #             = (-1)^n + d*(-1)^n = (-1)^n (1+d) [for n >= 1]
    # Coeff of x^0: 1
    f = [Fraction(0)] * (num_terms + 2)
    f[0] = Fraction(1)
    for k in range(1, num_terms + 2):
        f[k] = Fraction((-1)**k) * (1 + d)

    # Step 2: Compute sqrt(f)
    g = sqrt_series(f, num_terms + 2)

    # Step 3: P_d(x) = (1 - g(x)) / (2x)
    # Coefficient of x^n in P_d = -(g_{n+1}) / 2
    P = [Fraction(0)] * num_terms
    for n in range(num_terms):
        P[n] = -g[n+1] / 2

    return P


def verify_riordan(num_terms=15):
    """Verify that P_3(x) gives the Riordan numbers for sl_2."""
    P = compute_Pd(3, num_terms)
    print("P_3(x) coefficients (should be Riordan numbers):")

    # Known Riordan numbers: 1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298
    riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298]

    for n in range(min(len(P), len(riordan))):
        match = "OK" if P[n] == Fraction(riordan[n]) else "MISMATCH"
        print(f"  P[{n}] = {P[n]} (expected R({n}) = {riordan[n]}) {match}")

    # Bar cohomology: H^n = P[n + dim(sl_2)] = P[n+3]
    print("\nBar cohomology for sl_2 (H^n = R(n+3)):")
    for n in range(1, min(11, num_terms - 3)):
        print(f"  H^{n} = {P[n+3]}")


def compute_sl3(num_terms=20):
    """Compute bar cohomology for sl_3 using the generating function."""
    d = 8  # dim sl_3
    P = compute_Pd(d, num_terms)

    print(f"\nP_8(x) coefficients (conjectured GF for sl_3):")
    for n in range(min(15, num_terms)):
        print(f"  P[{n}] = {P[n]}")

    # Bar cohomology: H^n = P[n + dim(sl_3)] = P[n+8]
    print(f"\nConjectured bar cohomology for sl_3 (H^n = P[n+{d}]):")
    for n in range(1, min(11, num_terms - d)):
        val = P[n + d]
        print(f"  H^{n} = {val}")

    # Check against known values: 8, 36, 204
    print(f"\nVerification: H^1={P[d+1]}, H^2={P[d+2]}, H^3={P[d+3]}")
    print(f"Expected:     H^1=8, H^2=36, H^3=204")


def compute_general(name, d, num_terms=25, known=None):
    """Compute bar cohomology for a general Lie algebra."""
    P = compute_Pd(d, num_terms)

    print(f"\n{'='*60}")
    print(f"Bar cohomology for {name} (dim g = {d})")
    print(f"GF: P_d(x) = (1 - sqrt((1-{d}x)/(1+x))) / (2x)")
    print(f"H^n = P[n + {d}]")
    print(f"{'='*60}")

    values = []
    for n in range(1, min(13, num_terms - d)):
        val = P[n + d]
        marker = ""
        if known and n <= len(known):
            if val == Fraction(known[n-1]):
                marker = " [VERIFIED]"
            else:
                marker = f" [EXPECTED {known[n-1]}]"
        print(f"  H^{n} = {val}{marker}")
        values.append(int(val))

    return values


def compute_virasoro_check(num_terms=20):
    """
    Check Virasoro bar cohomology.
    Known: M(n+1)-M(n) where M = Motzkin numbers.
    Motzkin: 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, ...
    Differences: 0, 1, 2, 5, 12, 30, 76, 196, 512, 1353, 3610
    """
    motzkin = [1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511]
    diffs = [motzkin[n+1] - motzkin[n] for n in range(len(motzkin)-1)]
    print(f"\nVirasoro bar cohomology (Motzkin differences):")
    for n, v in enumerate(diffs):
        print(f"  H^{n+1} = {v}")

    # Check: Virasoro has 1 generator at weight 2, so it's NOT an
    # affine Kac-Moody algebra. The P_d formula doesn't apply directly.
    # The GF is P_Vir(x) = 4x / (1-x+sqrt(1-2x-3x^2))^2
    # from the manuscript.


def compute_bc_check():
    """
    Check bc ghost bar cohomology.
    Known: 2^n - n + 1
    """
    print(f"\nbc ghost bar cohomology (2^n - n + 1):")
    for n in range(1, 13):
        print(f"  H^{n} = {2**n - n + 1}")


def compute_betagamma_check():
    """
    Check beta-gamma bar cohomology.
    Known: [x^n] sqrt((1+x)/(1-3x)), with recurrence n*a(n) = 2n*a(n-1) + 3(n-2)*a(n-2)
    """
    a = [Fraction(1), Fraction(2)]  # a(0)=1, a(1)=2
    for n in range(2, 15):
        val = (2*n*a[n-1] + 3*(n-2)*a[n-2]) / n
        a.append(val)
    print(f"\nbeta-gamma bar cohomology:")
    for n in range(1, len(a)):
        print(f"  H^{n} = {a[n]}")


def compute_yangian_sl2():
    """
    Compute Yangian Y(sl_2) bar cohomology.

    The Yangian in the RTT presentation is a quadratic algebra with
    4 generators T_{ij}^{(0)} at level 0 and the RTT relation.

    For sl_2: V = C^2, generators are 4 matrix entries T_{ij}.
    The RTT relation R(u-v) T_1(u) T_2(v) = T_2(v) T_1(u) R(u-v)
    with R(u) = 1 - hbar*P/u gives quadratic relations.

    At level 0: the 4 generators T_{ij}^{(0)} with RTT relation
    give a quadratic algebra. The number of independent quadratic
    relations determines H^2.

    Known: H^1 = 4, H^2 = 10, H^3 = 28.

    The Yangian is Koszul (PBW basis), so A^! has Hilbert series
    satisfying H_A(t) * H_{A^!}(-t) = 1.

    H_A(t) = 1/(1-t)^4 (PBW = polynomial algebra on 4 generators at level 0)
    H_{A^!}(t) = 1/H_A(-t) = 1/(1+t)^4 = sum C(n+3,3)(-t)^n... wait

    1/(1+t)^4 = sum_{n>=0} C(n+3,n) (-1)^n t^n = 1 - 4t + 10t^2 - 20t^3 + ...
    But this gives alternating signs and |coeff| = C(n+3,3).

    H_{A^!}(-t) = 1/H_A(t), so H_{A^!}(t) = 1/(1-t)^4... that's the same as H_A.
    Hmm, that means A^! = A (self-dual)?

    Actually, for the Yangian, H_A(t) is NOT 1/(1-t)^4 because of the
    multi-level structure. Let me think more carefully.

    The Yangian has generators at each level r >= 0: T_{ij}^{(r)}.
    With the level grading, the Hilbert series is:
    H(t,q) = prod_{r>=0} 1/(1-q^r t)^4

    For the bar cohomology at bar degree n (summing over levels):
    we need to track the full bigraded structure.

    For a truncation to level 0 only (q=0): just 4 generators,
    6 RTT relations => A = quadratic algebra with dim A_n = C(n+3,3).
    A^! has dim (A^!)_n = C(n+3,3) as well (since Sym^! = Wedge,
    but with the non-commutative twist from the RTT relation).

    Actually wait. For the level-0 truncation:
    4 generators, 6 independent quadratic relations.
    The quadratic algebra A has H_A(t) = 1/(1-4t+6t^2-...) or something.

    For a quadratic algebra with V = C^4 (4 generators) and
    R = 6-dimensional relation space in V tensor V (dim 16):
    A^! has (A^!)_1 = 4, (A^!)_2 = dim(V*⊗V*)/R^perp = dim R = 6... no.

    (A^!)_2 = dim(R^perp) = 16 - 6 = 10. So H^2 = 10. ✓!

    For H^3: need to compute dim(A^!)_3.
    """
    print(f"\n{'='*60}")
    print("Yangian Y(sl_2) bar cohomology (RTT, level-0 truncation)")
    print(f"{'='*60}")

    # Generators: T_{11}, T_{12}, T_{21}, T_{22} (4 generators)
    # Relations: RTT gives 6 independent quadratic relations
    # among the 16-dimensional V⊗V.

    # For the Koszul dual: H^1 = 4, H^2 = 10 (= 16-6)
    # For H^3: we need dim(A^!)_3

    # The Koszul dual A^! = T(V*)/(R^perp) where R^perp is 10-dimensional.
    # dim(A^!)_3 = dim V*^{⊗3} - dim of degree-3 relations generated by R^perp
    # = 64 - dim(generated ideal at degree 3)

    # Generated ideal at degree 3: R^perp ⊗ V* + V* ⊗ R^perp
    # (two copies, overlapping)
    # dim(R^perp ⊗ V*) = 10 * 4 = 40
    # dim(V* ⊗ R^perp) = 4 * 10 = 40
    # dim(R^perp ⊗ V* + V* ⊗ R^perp) = 40 + 40 - dim(intersection)

    # The intersection: elements in V*^3 that can be written as both
    # r ⊗ v and v' ⊗ r' with r, r' in R^perp.

    # For the Koszul complex: dim(A^!)_3 = 64 - (80 - dim_intersection)

    # For a Koszul algebra with the RTT data, the Hilbert series satisfies:
    # H_A(t) * H_{A^!}(-t) = 1
    # H_A(t) = 1 + 4t + 10t^2 + 20t^3 + 35t^4 + ... = C(n+3,3) = 1/(1-t)^4
    # Wait, this is the FREE algebra on 4 generators, not the quotient by 6 relations.

    # Actually for the Yangian at level 0: the PBW basis gives
    # ordered monomials in 4 variables. The Hilbert series is
    # H_A(t) = 1/(1-t)^4 = sum C(n+3,n) t^n.

    # If A is Koszul with H_A(t) = 1/(1-t)^4, then:
    # H_{A^!}(-t) = (1-t)^4
    # H_{A^!}(t) = (1+t)^4 = 1 + 4t + 6t^2 + 4t^3 + t^4

    # So (A^!)_n = C(4,n): 1, 4, 6, 4, 1, 0, 0, ...
    # But the table says H^1=4, H^2=10, H^3=28!

    # So H_A(t) ≠ 1/(1-t)^4. The Yangian has more structure.

    # Let me try: for the CHIRAL Yangian, the bar cohomology involves
    # the OS algebra factors, just like for affine algebras.
    # With 4 generators and the OS factor (n-1)!:
    # The "chiral" Hilbert series would be different.

    # For the ordinary Yangian (non-chiral), with H_A(t) = 1/(1-t)^4:
    # A^! = Wedge(C^4), dim (A^!)_n = C(4,n).

    # For the chiral version: multiplied by (n-1)! from OS algebra.
    # But that gives H^1 = 4*1=4, H^2 = 6*1=6, not 10.

    # Actually, looking at the table values 4, 10, 28:
    # 4 = C(4,1)
    # 10 = C(5,2)
    # 28 = C(8,2) or C(7,3)? C(8,2)=28. ✓
    # Actually C(n+3,2) for n=1,2,3: C(4,2)=6, C(5,2)=10, C(6,2)=15.
    # H^2=10=C(5,2). H^3=28≠C(6,2)=15.

    # Let me check: 28 = C(8,2)=28 or 4*7=28. Hmm.
    # Catalan-like: C(4) = 14, C(5) = 42. Not matching.
    # Motzkin: M(5) = 21, M(6) = 51. Not matching.

    # Let me try: if H_{A^!}(t) satisfies a quadratic equation
    # similar to P_d for affine algebras, with d=4 (the number of generators):
    # P_4(x) = (1-sqrt((1-4x)/(1+x)))/(2x)

    d = 4
    P = compute_Pd(d, 20)
    print(f"\nUsing P_4(x) = (1-sqrt((1-4x)/(1+x)))/(2x):")
    print(f"H^n = P[n+4]:")
    for n in range(1, 10):
        if n + d < len(P):
            print(f"  H^{n} = {P[n+d]}")

    print(f"\nKnown: H^1=4, H^2=10, H^3=28")


def compute_W3():
    """
    Compute W_3 bar cohomology.

    W_3 has 2 generators: T (weight 2) and W (weight 3).
    Known: H^1 = 2, H^2 = 5, H^3 = 16, H^4 = 52.

    For the chiral bar complex, the generators are at different
    conformal weights, so the P_d formula (which assumes all generators
    at weight 1) doesn't directly apply.

    However, W_3 is the DS reduction of sl_3. The manuscript states
    that P_{sl_N} and P_{W(sl_N)} share the same discriminant.

    For sl_2: disc = (1-3x)(1+x). Vir GF: 4x/(1-x+sqrt(1-2x-3x^2))^2
    For sl_3: disc = (1-8x)(1+x). W_3 GF should involve sqrt((1-8x)(1+x)).

    The pattern from sl_2 -> Vir:
    P_Vir(x) = 4x / (1-x+sqrt((1-3x)(1+x)))^2

    For sl_3 -> W_3, by analogy:
    P_{W_3}(x) = ??? involving sqrt((1-8x)(1+x))
    """
    print(f"\n{'='*60}")
    print("W_3 bar cohomology")
    print(f"{'='*60}")

    # Known values
    print("Known: H^1 = 2, H^2 = 5, H^3 = 16, H^4 = 52")

    # Try the Motzkin-difference analogy:
    # For Virasoro: H^n = M(n+1) - M(n) where M = Motzkin
    # Motzkin GF: M(x) = (1-x-sqrt(1-2x-3x^2))/(2x^2)
    # For W_3: replace discriminant 1-2x-3x^2 with 1-7x-8x^2 = (1-8x)(1+x)

    # Generalized "Motzkin" with discriminant D(x) = 1 - (d-1)x - dx^2:
    # M_d(x) = (1-x-sqrt(D(x)))/(2x^2) where D = 1-(d-1)x-dx^2

    # For d=3: D=1-2x-3x^2 ✓
    # For d=8: D=1-7x-8x^2

    # Let's compute M_8 and check if M_8(n+1)-M_8(n) gives the W_3 sequence
    d = 8
    num_terms = 20

    # D(x) = 1 - (d-1)x - d*x^2
    D_coeffs = [Fraction(1), Fraction(-(d-1)), Fraction(-d)] + [Fraction(0)] * (num_terms + 5)

    sqrtD = sqrt_series(D_coeffs, num_terms + 5)

    # M_d(x) = (1 - x - sqrt(D)) / (2x^2)
    # Numerator: 1 - x - sqrt(D)
    # = 1 - x - (1 + sqrtD[1]*x + sqrtD[2]*x^2 + ...)
    # = -x - sqrtD[1]*x - sqrtD[2]*x^2 - sqrtD[3]*x^3 - ...
    # = (-1-sqrtD[1])x - sqrtD[2]*x^2 - sqrtD[3]*x^3 - ...
    # Dividing by 2x^2:
    # M_d = (-1-sqrtD[1])/(2x) + sum_{n>=0} (-sqrtD[n+2])/2 * x^n

    # But M_d should be a proper power series (no 1/x term).
    # Check: 1 - sqrtD[1] should be 0?
    # sqrtD[0] = 1, and we need 1 - 0 - 1 = 0 for the constant term.
    # The x^1 term in 1-x-sqrtD: -1 - sqrtD[1].
    # sqrtD[1] = -(d-1)/2 (from the sqrt expansion).
    # So -1 - sqrtD[1] = -1 + (d-1)/2 = (d-3)/2.
    # For d=3: (3-3)/2 = 0. Good, no 1/x term.
    # For d=8: (8-3)/2 = 5/2. This gives a 1/x pole!

    # So the M_d formula doesn't directly work for d != 3.
    # The W-algebra bar cohomology GF has a different form.

    print("\nThe direct M_d(x) analogy doesn't work for d=8 (pole at x=0).")
    print("Need a different approach for W_3.")

    # Instead, let's try to find a GF that:
    # 1. Is algebraic with discriminant (1-8x)(1+x)
    # 2. Gives H^1=2, H^2=5, H^3=16, H^4=52

    # Try: P(x) satisfies a*x*P^2 + b*P + c = 0 with discriminant (1-8x)(1+x)
    # b^2 - 4ac*x = alpha*(1-8x)(1+x)

    # Let P = sum p_n x^n with p_0 = 0 (since H^0 = 1 but we start from n=1).
    # Wait, actually for W_3, the table says H^1=2 (2 generators T,W).

    # Let me just try to find the recurrence for the sequence 2, 5, 16, 52, ...
    vals = [2, 5, 16, 52]
    print(f"\nLooking for patterns in: {vals}")
    print(f"Ratios: {[Fraction(vals[i+1], vals[i]) for i in range(len(vals)-1)]}")
    print(f"Second ratios: {[Fraction(vals[i+2]*vals[i], vals[i+1]**2) for i in range(len(vals)-2)]}")

    # Check if vals satisfy n*a(n) = alpha*a(n-1) + beta*a(n-2):
    # 2*5 = 10, a*2 + b*? (no a(-1))
    # 3*16 = 48, a*5 + b*2
    # 4*52 = 208, a*16 + b*5
    # From last two: 48 = 5a + 2b, 208 = 16a + 5b
    # 5*48 = 240 = 25a + 10b, 2*208 = 416 = 32a + 10b
    # 416-240 = 176 = 7a, a = 176/7 ≈ 25.1 (not integer)

    # Try a(n) = alpha*a(n-1) + beta*a(n-2):
    # 16 = 5*alpha + 2*beta
    # 52 = 16*alpha + 5*beta
    # 5*16 = 80 = 25alpha + 10beta
    # 2*52 = 104 = 32alpha + 10beta
    # 104-80 = 24 = 7alpha => alpha = 24/7. Not integer.

    # OEIS lookup for 2, 5, 16, 52:
    # Could be related to A001700 (3^n*(n+1)/2-n) or A006318 (large Schroeder)?
    # Large Schroeder: 1, 2, 6, 22, 90, ... No.
    # Little Schroeder: 1, 1, 2, 6, 22, 90, ... No.
    # A000670 (ordered Bell): 1, 1, 3, 13, 75, ... No.

    # Let me check: 2, 5, 16, 52, ?
    # 52/16 = 3.25, 16/5 = 3.2, 5/2 = 2.5
    # Approaching some growth rate?

    # Try the functional equation approach with 2 generators:
    # For 2 generators (like the free field case), the bar cohomology
    # might follow a pattern related to the beta-gamma GF sqrt((1+x)/(1-3x))
    # but adapted for the W_3 OPE structure.

    print("\nTrying direct computation from W_3 quadratic data...")
    print("(W_3 has 2 generators, so need to work out relations)")

    # For now, just extend what we can using the recurrence if we find one.
    # Let's try OEIS-style search with 2, 5, 16, 52:
    # Checking (2n+1)!! / something... or Catalan variants
    # 2, 5, 16, 52, 170? (52*3.27 ≈ 170)

    # Actually, let me check the generating function for the W_3 augmentation ideal.
    # W_3 has 2 generators at weights 2 and 3.
    # Augmentation ideal dims: weight 2: 1 (T), weight 3: 1 (W),
    # weight 4: 2 (partialT, :TT: minus central), weight 5: 3, etc.
    # These are given by the character of W_3.

    # For the bar complex at degree n, the dimensions involve
    # weighted tensor products. The bar cohomology is NOT just
    # from the generators but includes all descendants.

    # Given the complexity, let me just flag these as requiring
    # separate investigation and focus on what we CAN compute.


def main():
    print("=" * 60)
    print("Chiral bar cohomology computation")
    print("=" * 60)

    # Verify sl_2
    print("\n--- Verification: sl_2 ---")
    verify_riordan()

    # sl_3
    compute_general("sl_3", d=8, num_terms=25, known=[8, 36, 204])

    # sl_4
    compute_general("sl_4", d=15, num_terms=30)

    # so_5 (B_2, dim=10)
    compute_general("so_5 (B_2)", d=10, num_terms=25)

    # G_2 (dim=14)
    compute_general("G_2", d=14, num_terms=30)

    # Yangian
    compute_yangian_sl2()

    # W_3
    compute_W3()

    # bc and beta-gamma (already have formulas)
    compute_bc_check()
    compute_betagamma_check()


if __name__ == "__main__":
    main()
