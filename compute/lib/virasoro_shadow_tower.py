"""
Virasoro shadow obstruction tower - explicit computation through arity 10.

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
    Sh_7 = S7 x^7              (septic, computed here)
    Sh_8 = S8 x^8              (octic, computed here)
    Sh_9 = S9 x^9              (nonic, computed here)
    Sh_10 = S10 x^10           (decic, computed here)
    ...

The single-generator propagator is P = 2/c (inverse Hessian of κ = c/2).
The H-Poisson bracket is {f, g}_H = (∂f/∂x) · P · (∂g/∂x).
The master equation gives Sh_r = -∇_H^{-1}(o^(r)).

Equivalently, the weighted generating function

    H(t) = sum_{r >= 2} r S_r t^r = t^2 sqrt(Q_L(t))

is controlled by the quadratic shadow metric

    Q_L(t) = c^2 + 12 c t + (36 + 80/(5 c + 22)) t^2.

Writing sqrt(Q_L(t)) = sum_{n >= 0} a_n t^n gives the exact convolution
recursion

    a_0 = c,  a_1 = 6,  a_2 = 40/[c(5c+22)],
    a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3,

with S_r = a_{r-2}/r.

References:
    - thm:w-virasoro-quintic-forced (w_algebras.tex)
    - cor:virasoro-quintic-shadow-explicit (w_algebras.tex)
    - thm:shadow-formality-identification (higher_genus_modular_koszul.tex)
"""

from sympy import Symbol, Rational, cancel, simplify, factor, oo, S


c = Symbol('c')
x = Symbol('x')

# Propagator: P = 2/c (inverse of Hessian H = c/2)
P = Rational(2, 1) / c


def shadow_metric_coefficients():
    """Return q_0, q_1, q_2 for Q_L(t) = q_0 + q_1 t + q_2 t^2."""
    q0 = c**2
    q1 = 12 * c
    q2 = Rational(36) + Rational(80, 1) / (5 * c + 22)
    return q0, q1, q2


def sqrt_ql_coefficients(max_n=8):
    """Taylor coefficients a_n of sqrt(Q_L(t)) from f^2 = Q_L.

    If sqrt(Q_L(t)) = sum_{n >= 0} a_n t^n, then
        a_0 = c,
        a_1 = 6,
        a_2 = 40/[c(5c+22)],
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}   for n >= 3.
    """
    q0, q1, q2 = shadow_metric_coefficients()
    coeffs = [None] * (max_n + 1)
    coeffs[0] = c

    if max_n >= 1:
        coeffs[1] = cancel(q1 / (2 * coeffs[0]))

    if max_n >= 2:
        coeffs[2] = cancel((q2 - coeffs[1]**2) / (2 * coeffs[0]))

    for n in range(3, max_n + 1):
        conv_sum = sum(coeffs[j] * coeffs[n - j] for j in range(1, n))
        coeffs[n] = cancel(-conv_sum / (2 * coeffs[0]))

    return coeffs


def shadow_coefficients_from_ql(max_arity=10):
    """Exact shadow coefficients from the direct Q_L convolution recursion."""
    ql_coeffs = sqrt_ql_coefficients(max_arity - 2)
    coeffs = {}
    for r in range(2, max_arity + 1):
        coeffs[r] = factor(cancel(ql_coeffs[r - 2] / r))
    return coeffs


EXACT_SHADOW_COEFFICIENTS = {
    2: c / 2,
    3: Rational(2, 1),
    4: Rational(10, 1) / (c * (5 * c + 22)),
    5: Rational(-48, 1) / (c**2 * (5 * c + 22)),
    6: Rational(80, 1) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2),
    7: Rational(-2880, 1) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2),
    8: Rational(80, 1) * (2025 * c**2 + 16470 * c + 33314) / (c**5 * (5 * c + 22)**3),
    9: Rational(-1280, 1) * (2025 * c**2 + 15570 * c + 29554) / (3 * c**6 * (5 * c + 22)**3),
    10: Rational(256, 1) * (
        91125 * c**3 + 1050975 * c**2 + 3989790 * c + 4969967
    ) / (c**7 * (5 * c + 22)**4),
}


def exact_shadow_coefficients(max_arity=10):
    """Return the recorded exact S_r(c) formulas through arity 10."""
    upper = min(max_arity, max(EXACT_SHADOW_COEFFICIENTS))
    return {r: EXACT_SHADOW_COEFFICIENTS[r] for r in range(2, upper + 1)}


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


def verify_known_values(max_arity=10):
    """Verify the exact S_r(c) formulas against both recursion surfaces."""
    upper = min(max_arity, max(EXACT_SHADOW_COEFFICIENTS))
    coeffs = shadow_coefficients(upper)
    ql_coeffs = shadow_coefficients_from_ql(upper)
    expected = exact_shadow_coefficients(upper)

    for r in range(2, upper + 1):
        diff_master = simplify(coeffs[r] - expected[r])
        assert diff_master == 0, (
            f"Sh_{r} wrong from master equation: {coeffs[r]}, "
            f"expected {expected[r]}, diff={diff_master}"
        )

        diff_ql = simplify(ql_coeffs[r] - expected[r])
        assert diff_ql == 0, (
            f"Sh_{r} wrong from Q_L recursion: {ql_coeffs[r]}, "
            f"expected {expected[r]}, diff={diff_ql}"
        )

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
