"""
Virasoro shadow Postnikov tower — explicit computation through arity 7.

Computes the shadow obstruction tower Sh_r(Vir_c) on the single-generator primary line
using the all-arity master equation:
    ∇_H(Sh_r) + o^(r) = 0
where the obstruction class o^(r) is the H-Poisson bracket of lower shadows
composed through single-edge sewing.

The Virasoro shadow data:
    Sh_2 = (c/2) x^2           (curvature κ)
    Sh_3 = 2 x^3               (gravitational cubic C)
    Sh_4 = Q0 x^4              (contact quartic Q, Q0 = 10/[c(5c+22)])
    Sh_5 = S5 x^5              (quintic, computed here)
    Sh_6 = S6 x^6              (sextic, computed here)
    ...

The single-generator propagator is P = 2/c (inverse Hessian of κ = c/2).
The H-Poisson bracket is {f, g}_H = (∂f/∂x) · P · (∂g/∂x).
The master equation gives Sh_r = -∇_H^{-1}(o^(r)).

References:
    - thm:w-virasoro-quintic-forced (w_algebras.tex)
    - cor:virasoro-quintic-shadow-explicit (w_algebras.tex)
    - thm:shadow-formality-identification (higher_genus_modular_koszul.tex)
"""

from sympy import Symbol, Rational, simplify, factor, oo, S


c = Symbol('c')
x = Symbol('x')

# Propagator: P = 2/c (inverse of Hessian H = c/2)
P = Rational(2, 1) / c


def h_poisson_bracket(f, g):
    """Compute the H-Poisson bracket {f, g}_H = (df/dx) * P * (dg/dx)."""
    from sympy import diff
    return diff(f, x) * P * diff(g, x)


def invert_nabla_H(f_xn, n):
    """
    Solve ∇_H(Sh) = -f for Sh = S * x^n on the primary line.
    ∇_H(f) = {κ, f}_H where κ = (c/2)x² and {f,g}_H = (df/dx)(2/c)(dg/dx).
    For f = S x^n: ∇_H(S x^n) = 2n S x^n.
    Hence ∇_H^{-1}(α x^n) = α/(2n) * x^n.
    """
    from sympy import Poly
    poly = Poly(f_xn, x)
    coeff_xn = poly.nth(n)
    return coeff_xn / (2 * n) * x**n


def compute_shadow_tower(max_arity=7):
    """
    Compute the Virasoro shadow obstruction tower through the given arity.

    Returns dict {r: Sh_r} where Sh_r is a symbolic expression in c, x.
    """
    shadows = {}

    # Arity 2: κ = c/2 * x^2
    shadows[2] = (c / 2) * x**2

    # Arity 3: gravitational cubic C = 2x^3
    # This is the Sugawara normal-ordering contribution
    shadows[3] = 2 * x**3

    # Arity 4: quartic contact Q = Q0 * x^4
    Q0 = Rational(10, 1) / (c * (5*c + 22))
    shadows[4] = Q0 * x**4

    # Higher arities: use the master equation recursively
    for r in range(5, max_arity + 1):
        # Compute obstruction o^(r) as sum of H-Poisson brackets
        # of lower shadows that compose to give arity r
        obstruction = S.Zero

        # All pairs (j, k) with j + k = r + 1, j >= 2, k >= 2
        # (since the bracket of Sh_j and Sh_k has arity j + k - 1
        #  due to the single-edge contraction removing one leg)
        # Actually: {Sh_j, Sh_k}_H has degree j + k - 2 in x
        # We need contributions summing to degree r in x
        # From the sewing: {Sh_j, Sh_k}_H removes 2 legs and adds none,
        # so the x-degree is j + k - 2. We need j + k - 2 = r,
        # i.e., j + k = r + 2. But that's the arity of the graph.
        #
        # Actually, the correct formula from the quintic proof:
        # o^(r) = sum over pairs with j + k = r + 2 of {Sh_j, Sh_k}
        # But we need to be more careful.
        #
        # From thm:w-virasoro-quintic-forced:
        # o^(5) = {C, Q}_H where C = Sh_3, Q = Sh_4
        # C has degree 3, Q degree 4, {C, Q} has degree 3+4-2 = 5. ✓
        #
        # General rule: {Sh_j, Sh_k}_H has x-degree j + k - 2.
        # We need x-degree r, so j + k = r + 2.

        for j in range(2, r + 1):
            k = r + 2 - j
            if k < 2 or k not in shadows:
                continue
            if j > k:
                continue  # avoid double counting, add factor 2 for j != k

            bracket = h_poisson_bracket(shadows[j], shadows[k])
            bracket = simplify(bracket)

            if j == k:
                obstruction += Rational(1, 2) * bracket  # ½[Θ^(j), Θ^(j)]
            else:
                obstruction += bracket  # ½ · 2 = 1 for ordered pairs

        obstruction = simplify(obstruction)

        # Solve: ∇_H(Sh_r) + o^(r) = 0 => Sh_r = -∇_H^{-1}(o^(r))
        # ∇_H(f) = {κ, f}_H, for f = S x^r: ∇_H(S x^r) = 2r S x^r
        # Hence ∇_H^{-1}(α x^r) = α/(2r) x^r
        from sympy import Poly
        poly = Poly(obstruction, x)
        coeff = poly.nth(r)
        Sh_r = -coeff / (2 * r) * x**r
        Sh_r = factor(Sh_r)

        shadows[r] = Sh_r

    return shadows


def shadow_coefficients(max_arity=7):
    """Extract the rational coefficient S_r in Sh_r = S_r * x^r."""
    shadows = compute_shadow_tower(max_arity)
    coeffs = {}
    for r, sh in shadows.items():
        from sympy import Poly
        poly = Poly(sh, x)
        coeffs[r] = factor(poly.nth(r))
    return coeffs


def verify_known_values():
    """Verify the shadow obstruction tower against known results."""
    coeffs = shadow_coefficients(7)

    # Sh_2 coefficient = c/2
    assert simplify(coeffs[2] - c/2) == 0, f"Sh_2 wrong: {coeffs[2]}"

    # Sh_3 coefficient = 2
    assert simplify(coeffs[3] - 2) == 0, f"Sh_3 wrong: {coeffs[3]}"

    # Sh_4 coefficient = 10/[c(5c+22)]
    expected_Q0 = Rational(10, 1) / (c * (5*c + 22))
    assert simplify(coeffs[4] - expected_Q0) == 0, f"Sh_4 wrong: {coeffs[4]}"

    # Sh_5 coefficient = -48/[c^2(5c+22)]
    # From: o^(5) = 480/[c^2(5c+22)] * x^5, then Sh_5 = -o^(5)/(2*5)
    expected_S5 = Rational(-48, 1) / (c**2 * (5*c + 22))
    diff = simplify(coeffs[5] - expected_S5)
    assert diff == 0, f"Sh_5 wrong: {coeffs[5]}, expected {expected_S5}, diff={diff}"

    return coeffs


if __name__ == '__main__':
    print("Virasoro shadow obstruction tower computation")
    print("=" * 50)

    coeffs = verify_known_values()
    print("Verification of known values: PASSED")
    print()

    for r in sorted(coeffs.keys()):
        print(f"  Sh_{r}(Vir_c) = ({coeffs[r]}) * x^{r}")
    print()

    # Print the complementarity potential
    print("Complementarity potential S_Vir(x):")
    from sympy import factorial
    for r in sorted(coeffs.keys()):
        coeff_in_S = coeffs[r] / factorial(r)
        coeff_in_S = factor(coeff_in_S)
        print(f"  + (1/{r}!) * ({coeffs[r]}) * x^{r}")
        print(f"    = ({coeff_in_S}) * x^{r}")
