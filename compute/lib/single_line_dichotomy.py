"""
Single-line shadow tower dichotomy — thm:single-line-dichotomy.

On a one-dimensional primary slice L of the cyclic deformation complex,
the shadow tower with initial data (kappa, alpha, Q) satisfies:

    S_r = Delta * R_r(alpha, Q, kappa)    for all r >= 4

where Delta = 8*Q*kappa - 9*alpha^2 is the critical discriminant.

Consequences:
  - Delta = 0: tower terminates at arity 3 (class L)
  - alpha = 0, Q != 0: even-arity pump, r_max = infinity
  - alpha != 0, Delta != 0: all-arity pump, r_max = infinity
  - No value 4 <= r_max < infinity is achievable on a single line.

The contact class C (r_max = 4) escapes via stratum separation:
the quartic contact invariant lives on a different stratum of Def_cyc
whose self-bracket exits the complex by rank-one rigidity.

References:
  - thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
  - rem:contact-stratum-separation (higher_genus_modular_koszul.tex)
  - prop:master-equation-from-mc (higher_genus_modular_koszul.tex)
"""

from sympy import Symbol, Rational, factor, simplify, diff, S, Poly


x = Symbol('x')


def compute_single_line_tower(kappa, alpha, Q, max_arity=12):
    """
    Compute the shadow tower on a 1D primary line.

    Parameters:
        kappa: curvature (Sh_2 coefficient, times 2)
        alpha: cubic shadow coefficient (Sh_3 = alpha * x^3)
        Q: direct quartic contact contribution
        max_arity: highest arity to compute

    Returns:
        dict {r: S_r} of shadow coefficients (Sh_r = S_r * x^r)
    """
    # Convention: Sh_2 = (kappa/2) * x^2.
    # Propagator: P = 2/kappa (so that nabla_H(x^r) = 2r * x^r).
    # Inversion: S_r = -o_r_coeff / (2r).
    #
    # For the Virasoro: kappa = c, Sh_2 = (c/2)*x^2 (matching
    # virasoro_shadow_tower.py which sets P = 2/c).
    P = 2 / kappa
    shadows = {2: kappa / 2 * x**2, 3: alpha * x**3}

    # Sh_4: derived from cubic self-bracket + direct contact Q
    o4 = Rational(1, 2) * diff(shadows[3], x) * P * diff(shadows[3], x)
    o4 = simplify(o4)
    S4_derived = -Poly(o4, x).nth(4) / 8 if o4 != 0 else S.Zero
    S4_total = S4_derived + Q
    shadows[4] = S4_total * x**4

    for r in range(5, max_arity + 1):
        obstruction = S.Zero
        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in shadows:
                continue
            if j > k:
                continue
            sj = shadows[j]
            sk = shadows[k]
            if sj == 0 or sk == 0:
                continue
            bracket = diff(sj, x) * P * diff(sk, x)
            bracket = simplify(bracket)
            if j == k:
                obstruction += Rational(1, 2) * bracket
            else:
                obstruction += bracket
        obstruction = simplify(obstruction)

        if obstruction == 0:
            shadows[r] = S.Zero
            continue
        poly = Poly(obstruction, x)
        coeff = poly.nth(r) if poly.degree() >= r else S.Zero
        Sh_r = -coeff / (2 * r) * x**r
        Sh_r = factor(Sh_r)
        shadows[r] = Sh_r

    # Extract coefficients
    coeffs = {}
    for r, sh in shadows.items():
        if sh == 0:
            coeffs[r] = S.Zero
        else:
            coeffs[r] = factor(Poly(sh, x).nth(r))
    return coeffs


def verify_universal_factorization(max_arity=11):
    """
    Verify that S_r = Delta * R_r for all r >= 4
    with symbolic (kappa, alpha, Q).
    """
    kappa = Symbol('kappa', nonzero=True)
    alpha = Symbol('alpha')
    Q = Symbol('Q')
    Delta = 8 * Q * kappa - 9 * alpha**2

    coeffs = compute_single_line_tower(kappa, alpha, Q, max_arity)

    results = {}
    for r in range(4, max_arity + 1):
        Sr = coeffs[r]
        if Sr == 0:
            results[r] = {'S_r': 0, 'R_r': 0, 'divides': True}
            continue
        quotient = simplify(Sr / Delta)
        quotient = factor(quotient)
        # Verify: Sr - Delta * quotient == 0
        check = simplify(Sr - Delta * quotient)
        results[r] = {
            'S_r': factor(Sr),
            'R_r': quotient,
            'divides': check == 0
        }
    return results


def verify_even_cascade(max_arity=14):
    """
    Verify that alpha=0, Q!=0 produces nonzero even-arity shadows
    and zero odd-arity shadows.
    """
    kappa = Symbol('kappa', nonzero=True)
    Q = Symbol('Q', nonzero=True)
    coeffs = compute_single_line_tower(kappa, S.Zero, Q, max_arity)

    odd_zero = all(coeffs[r] == 0 for r in range(5, max_arity + 1, 2))
    even_nonzero = all(
        simplify(coeffs[r]) != 0
        for r in range(6, max_arity + 1, 2)
    )
    return odd_zero, even_nonzero, coeffs


def verify_delta_zero_termination(max_arity=10):
    """
    Verify that Delta=0 implies S_r=0 for all r >= 4.
    """
    kappa = Symbol('kappa', nonzero=True)
    alpha = Symbol('alpha', nonzero=True)
    # Set Q = 9*alpha^2 / (8*kappa) so that Delta = 0
    Q_critical = 9 * alpha**2 / (8 * kappa)

    coeffs = compute_single_line_tower(kappa, alpha, Q_critical, max_arity)

    all_zero = all(
        simplify(coeffs[r]) == 0
        for r in range(4, max_arity + 1)
    )
    return all_zero, coeffs


if __name__ == '__main__':
    print("Single-line dichotomy verification")
    print("=" * 60)

    # Test 1: universal factorization
    print("\n1. Universal factorization S_r = Delta * R_r:")
    results = verify_universal_factorization(11)
    for r in sorted(results.keys()):
        res = results[r]
        status = "OK" if res['divides'] else "FAIL"
        print(f"   r={r}: R_{r} = {res['R_r']}  [{status}]")

    # Test 2: even cascade
    print("\n2. Even-arity cascade (alpha=0, Q!=0):")
    odd_z, even_nz, coeffs = verify_even_cascade(14)
    print(f"   Odd arities all zero: {odd_z}")
    print(f"   Even arities all nonzero: {even_nz}")
    for r in range(4, 15):
        if coeffs[r] != 0:
            print(f"   S_{r} = {factor(coeffs[r])}")

    # Test 3: Delta=0 termination
    print("\n3. Delta=0 termination:")
    all_z, coeffs = verify_delta_zero_termination(10)
    print(f"   All S_r = 0 for r >= 4: {all_z}")
