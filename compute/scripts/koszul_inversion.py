#!/usr/bin/env python3
"""Find algebraic equation for bar cohomology GFs.

sl₂ bar cohomology = Riordan R(n+3): H₀=1, H₁=3, H₂=6, H₃=15, H₄=36, H₅=91, ...
sl₃ bar cohomology: H₀=1, H₁=8, H₂=36, H₃=204, H₄=?

Strategy: find the algebraic equation for sl₂, then apply same structure to sl₃.
"""

from sympy import Rational, symbols, sqrt, solve, simplify, series, factor, expand

x = symbols('x')

# CORRECT DATA (H₀=1 = ground field, then bar cohomology)
sl2 = [1, 3, 6, 15, 36, 91, 232, 603]   # R(3) through R(10)
sl3 = [1, 8, 36, 204]

def convolution(a, b, N):
    """Compute (a*b)[n] for n=0,...,N-1."""
    result = [0]*N
    for i in range(min(len(a), N)):
        for j in range(min(len(b), N)):
            if i+j < N:
                result[i+j] += a[i]*b[j]
    return result

def check_equation(name, P, A_coeffs, B_coeffs, C_coeffs, max_check):
    """Check A(x)*P² + B(x)*P + C(x) = 0 coefficient by coefficient."""
    N = max_check + 1
    P2 = convolution(P, P, N)
    residuals = []
    for n in range(N):
        val = 0
        for k, a in enumerate(A_coeffs):
            if n-k >= 0 and n-k < N:
                val += a * P2[n-k]
        for k, b in enumerate(B_coeffs):
            if n-k >= 0 and n-k < len(P):
                val += b * P[n-k]
        for k, c in enumerate(C_coeffs):
            if n == k:
                val += c
        residuals.append(val)
    print(f"{name}: residuals = {residuals}")
    return residuals

print("=" * 60)
print("PART 1: Verify Riordan equation for sl₂")
print("=" * 60)

# Riordan numbers R(n) satisfy the recurrence:
# (n+1)*R(n+1) = (n-1)*R(n) + 3*(n-1)*R(n-1) + (n-2)*(... )
# But the GF is more useful. The Riordan GF r(x) = sum R(n) x^n satisfies:
# r(x) = (1+x-sqrt(1-2x-3x²)) / (2x(1+x))
# Or equivalently: x(1+x)r² - (1+x)r + 1 = 0 (after clearing denominators)
# i.e. A = x(1+x) = x+x², B = -(1+x) = -1-x, C = 1

# But our P(x) = sum H_n x^n where H_n = R(n+3).
# So P(x) = r(x)/x³ * (stuff)... let me just check directly.

# First verify on the raw Riordan numbers
riordan = [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603]
print("Raw Riordan r(x): x(1+x)r² - (1+x)r + 1 = 0")
check_equation("Riordan", riordan, [0, 1, 1], [-1, -1], [1], 8)

# Now: P(x) = sum_{n>=0} R(n+3) x^n
# If r(x) = sum R(n) x^n, then P(x) = (r(x) - R(0) - R(1)x - R(2)x²) / x³
# = (r(x) - 1 - 0 - x²) / x³
# So r(x) = 1 + x² + x³ P(x)

# Substitute into x(1+x)r² - (1+x)r + 1 = 0:
# Let R = 1 + x² + x³P
# x(1+x)(1+x²+x³P)² - (1+x)(1+x²+x³P) + 1 = 0

# Expand (1+x²+x³P)²:
# = 1 + 2x² + 2x³P + x⁴ + 2x⁵P + x⁶P²

# x(1+x)*[1 + 2x² + 2x³P + x⁴ + 2x⁵P + x⁶P²]
# = (x+x²)(1 + 2x² + 2x³P + x⁴ + 2x⁵P + x⁶P²)
# = x + x² + 2x³ + 2x⁴ + 2x⁴P + 2x⁵P + x⁵ + x⁶ + 2x⁶P + 2x⁷P + x⁷P² + x⁸P²

# -(1+x)(1+x²+x³P) = -1-x-x²-x³-x³P-x⁴P

# +1

# Collecting constant and low-order terms:
# x⁰: -1+1 = 0 ✓
# x¹: x - x = 0 ✓
# x²: x² - x² = 0 ✓
# x³: 2x³ - x³ - x³P = x³(2-1) - x³P = x³ - x³P = x³(1-P)
# For this to be 0: coefficient of P at x⁰ must be 1, i.e. P(0) = 1. ✓

# This is getting complicated. Let me just numerically find the equation.

print("\n" + "=" * 60)
print("PART 2: Systematic search for algebraic equation of P")
print("=" * 60)

# Try: (a₁x + a₂x²)P² + (-1 + b₁x + b₂x²)P + (1 + c₁x + c₂x²) = 0
# or with more structure: (a₁x + a₂x² + a₃x³)P² + (-1 + b₁x + b₂x² + b₃x³)P + 1 = 0

# At x⁰: -P₀ + 1 = 0 ✓ (P₀=1)
# So C = 1 works. Try A = sum a_k x^k (k>=1), B = -1 + sum b_k x^k (k>=1), C = 1.

P2_sl2 = convolution(sl2, sl2, 12)

# For degree d polynomials A, B (starting from x¹ and x⁰):
# Unknowns: a₁,...,a_d, b₁,...,b_d (2d total)
# Equations from x¹,...,x^{2d} ideally. With 8 data points, we can go up to d=3 or so.

for d in range(1, 5):
    print(f"\n--- Degree {d} ---")
    syms_a = symbols(f'a1:{d+1}')
    syms_b = symbols(f'b1:{d+1}')
    all_syms = list(syms_a) + list(syms_b)

    eqs = []
    for n in range(1, 2*d + 1):
        if n >= len(sl2):
            break
        val = -sl2[n]  # from B₀*P[n] = -P[n]
        for k in range(1, d+1):
            # a_k * P²[n-k]
            if n-k >= 0 and n-k < len(P2_sl2):
                val += syms_a[k-1] * P2_sl2[n-k]
            # b_k * P[n-k]
            if n-k >= 0 and n-k < len(sl2):
                val += syms_b[k-1] * sl2[n-k]
        eqs.append(val)

    if len(eqs) < len(all_syms):
        print(f"  Underdetermined: {len(eqs)} eqs, {len(all_syms)} unknowns")
        continue

    sol = solve(eqs[:len(all_syms)], all_syms, dict=True)
    if not sol:
        print("  No solution")
        continue

    s = sol[0]
    print(f"  Solution: {s}")

    # Check remaining equations
    ok = True
    for n in range(len(all_syms) + 1, len(sl2)):
        val = -sl2[n]
        for k in range(1, d+1):
            if n-k >= 0 and n-k < len(P2_sl2):
                val += s[syms_a[k-1]] * P2_sl2[n-k]
            if n-k >= 0 and n-k < len(sl2):
                val += s[syms_b[k-1]] * sl2[n-k]
        if val != 0:
            ok = False
            print(f"  Check x^{n}: {val} (FAIL)")
        else:
            print(f"  Check x^{n}: 0 ✓")

    if ok:
        print(f"  *** EXACT EQUATION FOUND ***")
        A_str = " + ".join(f"{s[syms_a[k]]}*x^{k+1}" for k in range(d))
        B_str = "-1 + " + " + ".join(f"{s[syms_b[k]]}*x^{k+1}" for k in range(d))
        print(f"  A(x) = {A_str}")
        print(f"  B(x) = {B_str}")
        print(f"  C = 1")

        # Now apply to sl₃
        print(f"\n  === Applying degree-{d} structure to sl₃ ===")
        P2_sl3 = convolution(sl3, sl3, 10)

        # Same structure, solve with sl₃ data
        syms_a3 = symbols(f'a1:{d+1}')
        syms_b3 = symbols(f'b1:{d+1}')
        all_syms3 = list(syms_a3) + list(syms_b3)

        eqs3 = []
        for n in range(1, len(sl3)):  # only 3 equations (n=1,2,3)
            val = -sl3[n]
            for k in range(1, d+1):
                if n-k >= 0 and n-k < len(P2_sl3):
                    val += syms_a3[k-1] * P2_sl3[n-k]
                if n-k >= 0 and n-k < len(sl3):
                    val += syms_b3[k-1] * sl3[n-k]
            eqs3.append(val)

        if len(eqs3) < len(all_syms3):
            # Underdetermined — parametric solution
            free = all_syms3[len(eqs3):]
            solve_for = all_syms3[:len(eqs3)]
            sol3 = solve(eqs3, solve_for, dict=True)
            if sol3:
                s3 = sol3[0]
                print(f"  sl₃ parametric solution (free: {free}):")
                for v in solve_for:
                    print(f"    {v} = {s3[v]}")

                # P₄ prediction
                P4_sym = symbols('P4')
                n = 4
                val4 = -P4_sym
                for k in range(1, d+1):
                    ak = s3.get(syms_a3[k-1], syms_a3[k-1])
                    bk = s3.get(syms_b3[k-1], syms_b3[k-1])
                    # P²[4-k] needs P₄ in general
                    # P²[n-k] = sum_{i+j=n-k} P_i*P_j
                    # For k=1: P²[3] = 2*P₀P₃ + 2*P₁P₂ = 2*204+2*8*36=408+576=984... wait
                    # Actually P²[3] = sum P_i P_j with i+j=3
                    # = P₀P₃+P₁P₂+P₂P₁+P₃P₀ = 2*1*204+2*8*36 = 408+576 = 984
                    # Hmm but for n-k=3 when k=1: we need P²[3]
                    # P²[3] involves only P₀,...,P₃ which we know
                    idx = n - k
                    if idx >= 0 and idx < len(P2_sl3):
                        val4 += ak * P2_sl3[idx]
                    elif idx >= 0:
                        # Need to compute P²[idx] which may involve P₄
                        # P²[4] = 2*P₀*P₄ + 2*P₁*P₃ + P₂² = 2P₄ + 2*8*204 + 36² = 2P₄+3264+1296
                        if idx == 4:
                            val4 += ak * (2*P4_sym + 2*sl3[1]*sl3[3] + sl3[2]**2)
                        elif idx == 3:
                            val4 += ak * P2_sl3[3]
                    # B part
                    pidx = n - k
                    if pidx >= 0 and pidx < len(sl3):
                        val4 += bk * sl3[pidx]
                    elif pidx == 4:
                        val4 += bk * P4_sym

                P4_sol = solve(val4, P4_sym)
                if P4_sol:
                    P4_expr = P4_sol[0]
                    print(f"\n  P₄ = {simplify(P4_expr)}")

                    # Try to constrain free parameters using growth rate = 8
                    # Discriminant vanishes at x=1/8
                    A_sl3 = sum(s3.get(syms_a3[k], syms_a3[k])*x**(k+1) for k in range(d))
                    B_sl3 = -1 + sum(s3.get(syms_b3[k], syms_b3[k])*x**(k+1) for k in range(d))
                    disc = expand(B_sl3**2 - 4*A_sl3)
                    disc_at_8 = disc.subs(x, Rational(1, 8))
                    print(f"\n  disc(1/8) = {disc_at_8}")

                    if len(free) == 1:
                        b2_vals = solve(disc_at_8, free[0])
                        print(f"  {free[0]} from growth rate 8: {b2_vals}")
                        for bv in b2_vals:
                            P4_num = P4_expr.subs(free[0], bv)
                            print(f"    => P₄ = {simplify(P4_num)} = {float(P4_num):.1f}")
                    elif len(free) == 2:
                        print(f"  2 free params — need another constraint")
                        # Try: disc has a double root (algebraic curve is smooth)
                        # Or: require disc to factor over Q
                        # Or: require second growth rate to match dual
        break  # only process the first matching degree

print("\n" + "=" * 60)
print("PART 3: Alternative — use Riordan recurrence directly")
print("=" * 60)

# The Riordan numbers satisfy: a(n) = a(n-1) + sum_{k=2}^{n-1} a(k)*a(n+1-k)
# More precisely: for the shifted sequence P_n = R(n+3):
# From OEIS A005043: a(n) = ((n-1)*(2*a(n-1) + 3*a(n-2)))/(n+1)
# Let me verify this:
print("Riordan recurrence: P(n) = ((n+2)*(2*P(n-1) + 3*P(n-2)))/(n+4)")
for n in range(2, 8):
    pred = ((n+2) * (2*sl2[n-1] + 3*sl2[n-2])) // (n+4)
    actual = sl2[n]
    check = (n+2) * (2*sl2[n-1] + 3*sl2[n-2])
    print(f"  P({n}): pred={pred}, actual={actual}, num={check}, div by {n+4}={check/(n+4)}")

# The Riordan recurrence is: (n+1)*a(n+1) = (n-1)*(2*a(n)+3*a(n-1)) for n >= 1
# For our shifted P_n = R(n+3) = a(n+3):
# (n+4)*P_{n+1} = (n+2)*(2*P_n + 3*P_{n-1})
print("\nVerified recurrence: (n+4)*P(n+1) = (n+2)*(2*P(n) + 3*P(n-1))")

# This means sl₂ GF is D-FINITE (satisfies a linear ODE), not just algebraic.
# The algebraic equation is degree 2 but with the specific GF:
# P(x) = (r(x) - 1 - x²) / x³ where r solves x(1+x)r² - (1+x)r + 1 = 0

# For sl₃: does P also satisfy a similar D-finite recurrence?
# The conjectured recurrence was: a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
# This is a CONSTANT-coefficient recurrence (rational GF, not algebraic).

# Key difference:
# - sl₂: D-finite recurrence (polynomial coefficients) → algebraic GF
# - sl₃ (conjectured): constant-coeff recurrence → rational GF

# If sl₃ GF is RATIONAL, it's determined by finitely many initial values + the recurrence.
# The recurrence a(n) = 11a(n-1) - 23a(n-2) - 8a(n-3) needs 3 initial values.
# With [8, 36, 204], it predicts:
print("\n" + "=" * 60)
print("PART 4: sl₃ rational GF from recurrence")
print("=" * 60)

# a(n) = 11*a(n-1) - 23*a(n-2) - 8*a(n-3)
sl3_ext = list(sl3[1:])  # [8, 36, 204]
for n in range(3, 8):
    next_val = 11*sl3_ext[n-1] - 23*sl3_ext[n-2] - 8*sl3_ext[n-3]
    sl3_ext.append(next_val)
print(f"Recurrence 11a(n-1)-23a(n-2)-8a(n-3): {sl3_ext}")
print(f"P₄ = {sl3_ext[3]}")

# Characteristic polynomial: t³ - 11t² + 23t + 8 = 0
t = symbols('t')
char_poly = t**3 - 11*t**2 + 23*t + 8
roots = solve(char_poly, t)
print(f"\nCharacteristic roots: {roots}")
for r in roots:
    print(f"  {r} ≈ {float(r):.6f}")

print(f"\nFactored: {factor(char_poly)}")

# GF: P(x) = N(x) / (1 - 11x + 23x² + 8x³) for some numerator N(x)
# With P₁=8, P₂=36, P₃=204:
# (1 - 11x + 23x² + 8x³) * P(x) = N(x) (polynomial of degree <= 2)
# N₀ = P₁ = 8 (wait, need to be careful about indexing)

# Actually P(x) = sum_{n>=1} H_n x^{n-1} = 8 + 36x + 204x² + ...
# or P(x) = sum_{n>=0} H_{n+1} x^n = 8 + 36x + 204x² + ...
# Let Q(x) = P(x) = 8 + 36x + 204x² + H₄x³ + ...

# (1-11x+23x²+8x³)*Q(x) should be a polynomial of degree ≤ 2
# Coeff of x^n for n >= 3: Q_n - 11*Q_{n-1} + 23*Q_{n-2} + 8*Q_{n-3} = 0
# which is the recurrence. ✓

# So N(x) = (1-11x+23x²+8x³)*(8+36x+204x²) truncated to degree ≤ 2
Q_trunc = [8, 36, 204]
denom_coeffs = [1, -11, 23, 8]
N = [0, 0, 0]
for i in range(3):
    for j in range(3):
        if i+j < 3:
            N[i+j] += denom_coeffs[i] * Q_trunc[j]

print(f"\nNumerator N(x) = {N[0]} + {N[1]}*x + {N[2]}*x²")
print(f"GF = ({N[0]} + {N[1]}*x + {N[2]}*x²) / (1 - 11x + 23x² + 8x³)")

# Verify
Q_gf = (N[0] + N[1]*x + N[2]*x**2) / (1 - 11*x + 23*x**2 + 8*x**3)
Q_series = series(Q_gf, x, 0, n=8)
print(f"\nGF series: {Q_series}")

# Compare with manuscript's conjectured GF: 4x(2-13x-2x²)/((1-8x)(1-3x-x²))
# = 4x(2-13x-2x²)/(1-11x+23x²+8x³) ... wait, the denom matches!
# (1-8x)(1-3x-x²) = 1 - 3x - x² - 8x + 24x² + 8x³ = 1 - 11x + 23x² + 8x³ ✓

print(f"\nDenominator factored: {factor(1 - 11*x + 23*x**2 + 8*x**3)}")

# But the manuscript GF has a factor of x in the numerator, meaning P(0)=0.
# Our Q(x) = 8 + 36x + ... has Q(0)=8 ≠ 0.
# The manuscript GF: 4x(2-13x-2x²)/(denom) = (8x-52x²-8x³)/(denom)
# At x=0: 0. So the manuscript GF gives the bar cohomology as:
# H₁x + H₂x² + H₃x³ + ... = sum H_n x^n (n>=1)
# Let me check: series of 4x(2-13x-2x²)/denom

Q_manuscript = 4*x*(2 - 13*x - 2*x**2) / ((1-8*x)*(1-3*x-x**2))
Q_ms_series = series(Q_manuscript, x, 0, n=8)
print(f"\nManuscript GF: {Q_ms_series}")

# My GF: N(x)/denom
Q_my = (N[0] + N[1]*x + N[2]*x**2) / (1 - 11*x + 23*x**2 + 8*x**3)
Q_my_series = series(Q_my, x, 0, n=8)
print(f"My GF:         {Q_my_series}")

# Now check: does the recurrence actually work?
# We need to verify that the recurrence IS consistent.
# The key question: is 11a(n-1)-23a(n-2)-8a(n-3) the RIGHT recurrence?
# It's consistent with [8, 36, 204] by construction (3 initial values, 3 roots).
# But any degree-3 recurrence with 3 initial values is consistent!
# The question is whether the bar cohomology ACTUALLY satisfies this recurrence.

# Better approach: check if the denominator (1-8x)(1-3x-x²) is forced.
# Growth rate analysis: the dominant root of t³-11t²+23t+8 determines growth.
print(f"\nChar poly roots (growth rates):")
for r in roots:
    print(f"  {float(r):.6f}")

print("\n" + "=" * 60)
print("PART 5: sl₂ — what recurrence does Riordan satisfy?")
print("=" * 60)

# For sl₂: H = [1, 3, 6, 15, 36, 91, 232, 603]
# Riordan recurrence: (n+4)*H(n+1) = (n+2)*(2*H(n)+3*H(n-1))
# This is NOT constant-coefficient. Can we find a constant-coeff one?

# Test linear recurrence of order k:
for k in range(2, 5):
    print(f"\nOrder-{k} constant recurrence for sl₂?")
    # c₁*H(n-1) + ... + c_k*H(n-k) = H(n) for all valid n
    from sympy import Matrix
    rows = []
    rhs = []
    for n in range(k, len(sl2)):
        row = [sl2[n-j] for j in range(1, k+1)]
        rows.append(row)
        rhs.append(sl2[n])

    M = Matrix(rows)
    r = Matrix(rhs)
    if M.rows >= M.cols:
        # Overdetermined — check if consistent
        sol = M.solve(r)
        print(f"  Solution: {sol.T}")
        # Verify
        for n in range(k, len(sl2)):
            pred = sum(sol[j]*sl2[n-j-1] for j in range(k))
            if pred != sl2[n]:
                print(f"  FAIL at n={n}: pred={pred}, actual={sl2[n]}")
                break
        else:
            print(f"  All checks pass!")

# The point: if sl₂ has NO constant-coeff recurrence, then assuming sl₃ does is a CONJECTURE.
# The manuscript's rational GF for sl₃ is thus conjectural.

print("\n" + "=" * 60)
print("PART 6: Alternative approach — PBW spectral sequence")
print("=" * 60)

# For KM(g), the bar complex has a filtration by conformal weight.
# The E₁ page involves Ext groups of the Lie algebra g.
# E₁^{p,q} = H^p(g, Sym^q(g)) (roughly)
# For sl₃: we need Lie algebra cohomology with values in symmetric powers.

# H^n(sl₃, k) = exterior algebra on generators in degrees 3 and 5.
# So H^*(sl₃, k) has dims [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, ...] (degrees 0,3,5,8)

# More relevant: H^n(sl₃, sl₃) and H^n(sl₃, Sym²(sl₃))

# For the PBW approach, the E₂ page of the spectral sequence gives:
# dim H^n(bar) = sum_p dim E₂^{p,n-p}

# This requires computing H^p(sl₃, Sym^q(sl₃)) for various p,q.
# For Koszul algebras, E₂ = E_∞, so this gives the exact answer.

# KEY RESULT from Lie algebra cohomology:
# H^*(g, V) where V is a finite-dim g-module can be computed from
# the Chevalley-Eilenberg complex: C^n = Hom(∧^n g, V)

# For sl₃ (dim 8):
# C^n(sl₃, Sym^q(sl₃)) = ∧^n(sl₃*) ⊗ Sym^q(sl₃)
# dim C^n = C(8,n) * C(q+7, q) ... this gets large fast.

# Instead, use the Weyl character formula approach:
# H^p(g, V) = sum_w (-1)^{l(w)} mult(V, w·0 - 0) for simple g
# where w ranges over the Weyl group.

# For sl₃, Weyl group = S₃ (order 6).
# H^p(sl₃, V) is nonzero only when V contains certain weights.

# The bar cohomology generating function as a character:
# sum_n dim H^n * t^n = prod_{positive roots} (1 + t^{2h_α - 1}) / (1 - t^{2h_α})
# For sl₃: positive roots have heights 1, 1, 2 (two simple + one sum)
# Hmm, this is getting complicated.

# Let me try a more direct approach: compute sl₃ bar cohomology
# using the representation-theoretic decomposition.

print("For sl₃ bar cohomology via PBW spectral sequence:")
print("  E₁ page: CE cohomology of sl₃ with coefficients")
print("  Need H^p(sl₃, Sym^q(sl₃)) for all p, q with p+q ≤ 4")
print("")
print("  Relevant representation theory:")
print("  sl₃ adjoint = V(1,1) (dim 8)")
print("  Sym²(adj) = V(2,2) ⊕ V(0,3) ⊕ V(3,0) ⊕ V(1,1) ⊕ V(0,0)")
print("    dims: 27 + 10 + 10 + 8 + 1 = ... wait, need to compute")

# Actually: Sym²(V(1,1)) decomposes as:
# (1,1)⊗(1,1) = Sym²⊕∧²
# (1,1)⊗(1,1) = V(2,2) + V(3,0) + V(0,3) + V(1,1) + V(0,0) (sym part)
#              + V(2,2) + V(1,1) (alt part)? No...

# SL₃ tensor product: V(1,1)⊗V(1,1)
# By highest weight theory: 8⊗8 = 64
# Decomposition: adjoint⊗adjoint for sl₃
# = V(2,2) ⊕ V(3,0) ⊕ V(0,3) ⊕ 2·V(1,1) ⊕ V(0,0)
# dims: 27 + 10 + 10 + 2*8 + 1 = 64 ✓

# Symmetric part: V(2,2) ⊕ V(3,0) ⊕ V(0,3) ⊕ V(1,1) ⊕ V(0,0)
# = 27 + 10 + 10 + 8 + 1 = 56? But dim Sym²(8) = 36.
# Hmm, 36 = C(8+1,2) = 36. Let me recount.
# V(2,2)=27, V(0,0)=1, and we need 36-28=8 more...
# Actually I think: Sym²(V(1,1)) = V(2,2) ⊕ V(0,0) (dims 27+1=28)... no, that's only 28.
# Wait: dim V(2,2) for sl₃:
# V(a,b) has dim = (a+1)(b+1)(a+b+2)/2
# V(2,2): (3)(3)(6)/2 = 27
# V(3,0): (4)(1)(5)/2 = 10
# V(0,3): (1)(4)(5)/2 = 10

# Full tensor product: 8⊗8 = 27 + 10 + 10 + 8 + 8 + 1 = 64
# Sym²: 27 + 10 + 1 = ... no. Need to be more careful.

# For sl₃ (type A₂), the adjoint is V(1,1) with dim 8.
# V(1,1) ⊗ V(1,1) = V(2,2) ⊕ V(3,0) ⊕ V(0,3) ⊕ V(1,1) ⊕ V(1,1) ⊕ V(0,0)
# Wait, that gives 27+10+10+8+8+1 = 64 but some of these go to Sym and some to Alt.

# The symmetric square Sym²(V) picks up irreps that appear with even parity
# under the swap. For self-dual V = V(1,1):
# Sym² picks up V(2,2), V(1,1), V(0,0) ... no, I need to actually compute this.

# Let me just note the dim and move on.
print(f"\n  dim Sym²(sl₃) = C(8+1,2) = {8*9//2}")
print(f"  dim ∧²(sl₃) = C(8,2) = {8*7//2}")

# H⁴(bar) via spectral sequence:
# The bar complex at degree n involves modes at conformal weights w = 1,...,n
# E₂^{p,q} = H^p(g, V_q) where V_q captures weight-q contribution
# Total H^n(bar) = sum_{p+q=n} E₂^{p,q}

# This is the right approach but requires extensive representation theory.
# Let me try something simpler: just verify the conjectured value 1352 against
# the PBW structure.

# For sl₃ at degree 4: the chain group B̄⁴ has dim = 8⁴ * 3! = 4096 * 6 = 24576
# The bar differential d: B̄⁴ → B̄³ and d: B̄⁵ → B̄⁴ determine H⁴.
# H⁴ = dim ker(d₄) - dim im(d₅)
# where d₄: B̄⁴ → B̄³ has size 24576 × (8³ * 2) = 24576 × 1024
# This is... actually computable? Let me check sizes.

print(f"\n  Chain group dims for sl₃:")
for n in range(1, 7):
    from math import factorial
    dim_chains = 8**n * factorial(n-1)
    print(f"    B̄^{n} = 8^{n} * {n-1}! = {dim_chains}")

print("\nDirect matrix computation for H⁴ would require:")
print("  d₄: 24576 × 1024 matrix (rank computation)")
print("  d₅: 122880 × 24576 matrix (rank computation)")
print("  Even sparse, this is feasible with numpy.")

# But the issue remains: what IS the bar differential?
# From the previous session, we established that the FULL bar complex
# involves all conformal weights, not just the Lie algebra generators.
# So B̄^n ≠ g^⊗n ⊗ OS^{n-1}.

# HOWEVER: if we restrict to conformal weight n (each generator at weight 1),
# then the only contribution at weight n is exactly g^⊗n ⊗ OS^{n-1}.
# Higher weights involve modes J^a_{-k} with k > 1.

# At weight w, the contribution to B̄^n is:
# span{J^{a₁}_{-k₁} ⊗ ... ⊗ J^{aₙ}_{-kₙ} : k₁+...+kₙ=w} ⊗ OS^{n-1}

# For the MINIMUM weight sector (w=n, all k_i=1):
# B̄^n_min = g^⊗n ⊗ OS^{n-1}, dim = d^n * (n-1)!

# The key claim from the manuscript: the spectral sequence on weight
# collapses at E₂, and E₂ = H_CE(g, coefficients).

# So H^n(bar) = sum_{w>=n} h^n_w where h^n_w is the cohomology at weight w.

# At minimum weight (w=n): h^n_n = H^n of the CE-like complex on g^⊗n ⊗ OS^{n-1}
# where the differential is the residue of the simple pole of the OPE.

# For n=1: h^1_1 = dim g = 8 (no differential). ✓
# For n=2: h^2_2 = dim ker(d₂) on g⊗g ⊗ OS¹(C₂) = g⊗g (OS¹(C₂) = span{η₁₂})
# d₂ maps (a⊗b)⊗η₁₂ → [a,b] via the Lie bracket (simple pole residue)
# ker d₂ = {a⊗b : [a,b]=0 in sl₃} ... this is NOT zero!
# dim(g⊗g) = 64, rank([,]) = dim[g,g] = dim(g) = 8 (sl₃ is simple, [g,g]=g)
# So h^2_2 = 64 - 8 = 56... but H₂ = 36. That's wrong.

# Hmm. Unless d₂ maps to something other than g.
# Or: maybe the bar differential goes B̄¹ → B̄², not B̄² → B̄¹.
# In the COHOMOLOGICAL convention (|d|=+1): d: B̄^n → B̄^{n+1}
# So d₁: B̄¹ → B̄² (adds a factor), not contracts.

# Then H¹ = ker(d₁: B̄¹→B̄²) / im(d₀: B̄⁰→B̄¹)
# B̄⁰ = ground field (dim 1), d₀ = 0 (or augmentation), so H¹ = ker(d₁).
# For H¹ = 8 = dim(g), we need ker(d₁) = g, i.e. d₁ = 0.

# And H² = ker(d₂: B̄²→B̄³) / im(d₁: B̄¹→B̄²)
# If d₁ = 0, then H² = ker(d₂).
# dim B̄² = 64 (at min weight), H₂ = 36, so rank(d₂) should be 64-36 = 28.
# But... where does d₂ map TO? B̄³ = g⊗g⊗g ⊗ OS²(C₃), dim = 512*2 = 1024.
# rank(d₂) ≤ min(64, 1024) = 64, and 28 ≤ 64. Plausible.

# But this is ONLY the minimum weight sector. Higher weights contribute more.
# From H₂ = 36 = dim Sym²(g), maybe the minimum-weight cohomology is Sym²(g)?
# Indeed, h^2_2 = Sym²(g) = 36 would mean the antisymmetric part is killed.
# d₂(a⊗b⊗η₁₂) = something in B̄³, and ker(d₂) = {symmetric tensors}
# if d₂ acts as antisymmetrization or commutator.

# Actually: if d₂(a⊗b⊗η₁₂) involves [a,b], then d₂ kills Sym²(g) iff
# it factors through ∧²(g). Let's check:
# [a,b] = -[b,a], so the bracket is antisymmetric.
# If d₂(a⊗b) = [a,b] ⊗ (...) + (...), then yes, Sym²(g) ⊂ ker(d₂).
# And im(d₂) has dim = dim(∧²g) - dim(ker([,] on ∧²g))
# = 28 - dim{a∧b : [a,b]=0}

# For sl₃: dim ∧²(sl₃) = 28
# The bracket [,]: ∧²(sl₃) → sl₃ is surjective (sl₃ is perfect)
# So ker([,] on ∧²) = 28 - 8 = 20
# And rank(d₂ on ∧²) = 8

# If only ∧² contributes to d₂ and ker includes all of Sym²:
# ker(d₂) ⊇ Sym²(g) (dim 36) + ker([,]∩∧²) (dim 20) = dim 56
# But B̄² = 64 and d₂ has rank 8, so ker(d₂) = 64-8 = 56.
# H² at min weight = 56, but we need H² = 36.

# So either: (1) there are higher-weight contributions to H² with negative signs (impossible for dims)
# (2) im(d₁) is nonzero, contributing 56-36=20 to the quotient
# (3) my analysis of the differential is wrong

# If d₁: B̄¹ → B̄² has image of dim 20, then H² = 56/20 = ... no, 56-20 = 36. Yes!
# That works if d₁ has rank 20 and maps into ker(d₂).

# But d₁ maps FROM B̄¹ = g (dim 8). So rank(d₁) ≤ 8.
# 20 > 8, contradiction.

# So this approach has an error. The bar complex structure is more subtle.
# Perhaps the OS factor changes the analysis, or the differential includes
# more than just the Lie bracket.

print("\nConclusion: direct computation of H⁴ requires understanding")
print("the full bar differential including all conformal weights.")
print("The conjectured value H₄ = 1352 from the rational GF remains unverified.")
print("But the rational GF structure (if correct) is FULLY DETERMINED")
print("by the 3 known values [8, 36, 204] and the denominator (1-8x)(1-3x-x²).")

print("\n" + "=" * 60)
print("PART 7: What determines the denominator?")
print("=" * 60)

# The conjectured denominator (1-8x)(1-3x-x²) has roots:
# x = 1/8 (growth rate 8 = dim sl₃)
# and roots of 1-3x-x² = 0: x = (-3±sqrt(13))/(-2) = (3∓sqrt(13))/2
r1 = (3 - sqrt(13))/2
r2 = (3 + sqrt(13))/2
print(f"Denominator roots:")
print(f"  1/8 = 0.125 (growth rate 8)")
print(f"  (3-sqrt(13))/2 = {float(r1):.6f} (growth rate {float(1/r1):.4f})")
print(f"  (3+sqrt(13))/2 = {float(r2):.6f} (growth rate {float(1/r2):.4f})")

# For sl₂: Riordan has growth rate 3 = dim(sl₂). The GF is ALGEBRAIC (not rational).
# For sl₃: if GF is rational with growth rate 8 = dim(sl₃), the dominant pole is 1/8.

# The question is: what determines the other factor (1-3x-x²)?
# In Koszul duality: the dual's growth rate should appear.
# sl₃^! = ??? The Koszul dual of affine sl₃ at level k.

# For KM at level k: the bar cohomology might depend on k!
# At level k, the OPE has both simple pole ([,]) and double pole (k*Killing).
# The double pole contributes to d through the Poincaré residue as well.

# If the growth rate 8 comes from (dim g)^n = 8^n chain groups,
# then the other factor (3+sqrt(13))/2 ≈ 3.303 might relate to
# h^∨(sl₃) = 3 (dual Coxeter number).

# (3+sqrt(13))/2 ≈ 3.303... not exactly 3.
# But 1-3x-x² evaluated at specific points:
# If x = 1/3: 1-1-1/9 = -1/9 ≠ 0
# The factor 1-3x-x² doesn't have root 1/3.

# Connection to Coxeter: 2h(sl₃) = 6 (Coxeter number h=3, dual Coxeter h^∨=3)
# The periodicity of KM bar cohomology for sl₂ is period 4 = 2h^∨(sl₂).
# For sl₃, periodicity is NOT 2h^∨=6 (verified in the manuscript).

# What if the second factor comes from the Killing form eigenvalue structure?
# For sl₃: Killing eigenvalues on the adjoint are 6 (= 2*h^∨ = 2*3).
# Casimir eigenvalue on adjoint: C₂(adj) = 2h^∨ = 6.
# On Sym²(adj): varies by irrep component.

# I think the key insight might be:
# For a rational GF, the denominator factors correspond to
# the spectrum of the "bar transfer matrix" T acting on the chain groups.
# T has eigenvalues that are the reciprocals of the denominator roots.
# Eigenvalue 8: from the "free" growth (dim g)
# Eigenvalue (3+sqrt(13))/2 ≈ 3.303: from the "Koszul dual" contribution

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"sl₃ conjectured rational GF: {N[0]}+{N[1]}x+{N[2]}x² over (1-11x+23x²+8x³)")
print(f"= {Q_ms_series}")
print(f"\nPredicted values:")
for i, c in enumerate(sl3_ext):
    status = "KNOWN" if i < 3 else "PREDICTED"
    print(f"  H_{i+1} = {c}  [{status}]")

print(f"\nThe conjectured GF is FULLY DETERMINED by [8, 36, 204]")
print(f"and the assumption of a degree-3 constant-coefficient recurrence")
print(f"with denominator (1-8x)(1-3x-x²).")
print(f"\nThe denominator choice (1-8x)(1-3x-x²) is the conjecture.")
print(f"Factor 1-8x comes from growth rate dim(sl₃)=8.")
print(f"Factor 1-3x-x² is not yet derived from first principles.")
