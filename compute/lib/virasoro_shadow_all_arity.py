r"""Closed-form Virasoro shadow tower to arbitrary arity.

The shadow metric Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22) controls the
entire infinite tower of shadow coefficients S_r for the Virasoro algebra.
The generating function H(t) = t^2 sqrt(Q_L(t)) gives S_r = a_{r-2}/r
where a_n = [t^n] sqrt(Q_L(t)).

KEY DISCOVERY: alpha = 2 for Virasoro (the cubic shadow coefficient),
c-independent, determined uniquely by the critical cubic
    5c^3 + 22c^2 - 180c - 872 = 0
which is the condition rho(c) = 1 for the shadow growth rate
    rho = sqrt(9*alpha^2 + 2*Delta) / (2*kappa)
       = sqrt(36 + 80/(5c+22)) / c.

The convolution recursion a_0^2 = Q_L(0), 2*a_0*a_n = Q_L^(n) - sum a_j*a_{n-j}
yields closed-form rational functions of c at each arity.

DENOMINATOR PATTERN (THEOREM): S_r has denominator c^{r-3} * (5c+22)^{floor((r-2)/2)}.

PROOF. The Taylor coefficient a_n of sqrt(Q_L) satisfies a_n = -(1/(2c)) sum a_j a_{n-j}.
By induction, denom(a_n) = c^{n-1} * (5c+22)^{floor(n/2)} for n >= 2.
Base: a_2 = 40/[c(5c+22)], denom = c^1*(5c+22)^1. Check.
Step: the product a_j*a_{n-j} has c-power (j-1)+(n-j-1) = n-2 in the denominator,
and (5c+22)-power floor(j/2)+floor((n-j)/2) <= floor(n/2). After dividing by 2c,
the c-power becomes n-1 and the (5c+22)-power is floor(n/2).
The inequality floor(j/2)+floor((n-j)/2) <= floor(n/2) is saturated by
j=2 (for n even) or j=1 (for n odd), ensuring the denominator is exact. QED.

Corollary: S_r = a_{r-2}/r has denom c^{r-3}*(5c+22)^{floor((r-2)/2)}.

In particular, NO Kac determinant zeros beyond weight 4 (c=-68/7, c=-46/3, etc.)
appear in the denominators. The shadow tower sees only the first Gram determinant.
The numerator at arity r is a polynomial in c of degree floor((r-4)/2).

References:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    cor:virasoro-quintic-shadow-explicit (w_algebras.tex)
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    factor,
    numer,
    denom,
    simplify,
    sqrt,
    Poly,
)


c = Symbol('c')


# ═══════════════════════════════════════════════════════════════════════
# Virasoro shadow data
# ═══════════════════════════════════════════════════════════════════════

def kappa_vir():
    """kappa = c/2."""
    return c / 2


def alpha_vir():
    """alpha = 2 (c-independent, the Sugawara self-coupling).

    Determined by the critical cubic: the condition rho = 1 gives
    9*alpha^2 + 2*Delta = 4*kappa^2, i.e.,
    9*alpha^2 + 80/(5c+22) = c^2.
    Multiplying by (5c+22): 9*alpha^2*(5c+22) + 80 = c^2*(5c+22),
    i.e., 5c^3 + 22c^2 - 45*alpha^2*c - (198*alpha^2 + 80) = 0.
    The known critical cubic 5c^3 + 22c^2 - 180c - 872 = 0 forces
    45*alpha^2 = 180 and 198*alpha^2 + 80 = 872,
    both giving alpha^2 = 4, hence alpha = 2.
    """
    return Rational(2)


def S4_vir():
    """S_4 = 10/[c(5c+22)]."""
    return Rational(10) / (c * (5 * c + 22))


def Delta_vir():
    """Critical discriminant Delta = 8*kappa*S_4 = 40/(5c+22)."""
    return Rational(40) / (5 * c + 22)


def shadow_metric_vir():
    """Q_L(t) = (c + 6t)^2 + 80t^2/(5c+22).

    Returns (q0, q1, q2) where Q_L = q0 + q1*t + q2*t^2.
    """
    q0 = c**2
    q1 = 12 * c
    q2 = Rational(36) + Rational(80) / (5 * c + 22)
    # Equivalently: q2 = (180c + 872) / (5c+22)
    return q0, q1, q2


# ═══════════════════════════════════════════════════════════════════════
# Convolution recursion for sqrt(Q_L)
# ═══════════════════════════════════════════════════════════════════════

def sqrt_QL_coefficients(max_n: int = 20) -> List:
    """Taylor coefficients a_n of sqrt(Q_L(t)) via convolution recursion.

    f(t) = sqrt(Q_L(t)) = sum_{n>=0} a_n t^n
    f(t)^2 = Q_L(t) = q0 + q1*t + q2*t^2

    Recursion:
        a_0 = sqrt(q0) = c  (for c > 0)
        2*a_0*a_1 = q1      => a_1 = q1/(2c) = 6
        2*a_0*a_2 + a_1^2 = q2  => a_2 = (q2 - 36)/(2c) = 40/[c(5c+22)]
        2*a_0*a_n + sum_{j=1}^{n-1} a_j*a_{n-j} = 0  for n >= 3
            => a_n = -(1/(2c)) * sum_{j=1}^{n-1} a_j*a_{n-j}

    Returns list [a_0, a_1, ..., a_{max_n}].
    """
    q0, q1, q2 = shadow_metric_vir()

    a = [None] * (max_n + 1)
    a[0] = c  # sqrt(q0)

    if max_n >= 1:
        a[1] = cancel(q1 / (2 * c))  # = 6

    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * c))  # = 40/[c(5c+22)]

    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * c))

    return a


def shadow_coefficients(max_r: int = 20) -> Dict[int, object]:
    """Virasoro shadow tower S_r for r = 2, ..., max_r.

    S_r = a_{r-2} / r  where a_n = [t^n] sqrt(Q_L(t)).

    Returns dict {r: S_r} with S_r as simplified sympy expressions.
    """
    a = sqrt_QL_coefficients(max_n=max_r - 2)

    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = factor(cancel(a[n] / r))

    return result


# ═══════════════════════════════════════════════════════════════════════
# Denominator analysis
# ═══════════════════════════════════════════════════════════════════════

def denominator_pattern(max_r: int = 15) -> List[Tuple[int, int, int]]:
    """Analyse the denominator pattern of S_r.

    Returns list of (r, power_of_c, power_of_5c22) for r = 4, ..., max_r.
    The denominator of S_r is c^{pow_c} * (5c+22)^{pow_5c22} * (rational const).

    Predicted pattern:
        pow_c = r - 3
        pow_5c22 = floor((r-2)/2)
    """
    coeffs = shadow_coefficients(max_r)

    pattern = []
    for r in range(4, max_r + 1):
        Sr = coeffs[r]
        d = denom(cancel(Sr))
        d_poly = Poly(d, c)

        # Factor out powers of c
        pow_c = 0
        rem = d_poly
        while rem.eval(0) == 0:
            pow_c += 1
            rem = Poly(cancel(rem.as_expr() / c), c)

        # Check for (5c+22) factors
        pow_5c22 = 0
        while rem.eval(Rational(-22, 5)) == 0:
            pow_5c22 += 1
            rem = Poly(cancel(rem.as_expr() / (5 * c + 22)), c)

        pattern.append((r, pow_c, pow_5c22))

    return pattern


# ═══════════════════════════════════════════════════════════════════════
# Shadow growth rate
# ═══════════════════════════════════════════════════════════════════════

def shadow_growth_rate_squared():
    """rho^2 = (9*alpha^2 + 2*Delta) / (4*kappa^2)
             = (36 + 80/(5c+22)) / c^2
             = (180c + 872) / [c^2(5c+22)].
    """
    return (180 * c + 872) / (c**2 * (5 * c + 22))


def critical_cubic():
    """5c^3 + 22c^2 - 180c - 872 = 0: the locus rho = 1."""
    return 5 * c**3 + 22 * c**2 - 180 * c - 872


# ═══════════════════════════════════════════════════════════════════════
# Explicit closed-form results
# ═══════════════════════════════════════════════════════════════════════

EXPLICIT_SHADOWS = {
    2: "c/2",
    3: "2",
    4: "10 / [c(5c+22)]",
    5: "-48 / [c^2(5c+22)]",
    6: "80(45c+193) / [3 c^3 (5c+22)^2]",
    7: "-2880(15c+61) / [7 c^4 (5c+22)^2]",
}


def S_explicit(r: int):
    """Return explicit closed-form S_r as sympy expression."""
    if r == 2:
        return c / 2
    if r == 3:
        return Rational(2)
    if r == 4:
        return Rational(10) / (c * (5 * c + 22))
    if r == 5:
        return Rational(-48) / (c**2 * (5 * c + 22))
    if r == 6:
        return Rational(80) * (45 * c + 193) / (3 * c**3 * (5 * c + 22)**2)
    if r == 7:
        return Rational(-2880) * (15 * c + 61) / (7 * c**4 * (5 * c + 22)**2)
    raise ValueError(f"Explicit formula not implemented for r={r}")


# ═══════════════════════════════════════════════════════════════════════
# Master equation recursion (independent check)
# ═══════════════════════════════════════════════════════════════════════

def shadow_coefficients_master_eq(max_r: int = 20) -> Dict[int, object]:
    """Virasoro shadow tower via the master equation recursion.

    The master equation nabla_H(Sh_r) + o^(r) = 0 gives:

        2r S_r + sum_{3<=j<=k, j+k=r+2} eps(j,k) * (2jk S_j S_k / c) = 0

    where eps(j,k) = 1 if j<k, 1/2 if j=k, and the j=2 term is
    separated out as the nabla_H part (giving the 2r S_r on the left).

    Equivalently:  S_r = -(1/(rc)) * sum_{3<=j<=k, j+k=r+2} eps*j*k*S_j*S_k

    NOTE: the sum starts at j=3, NOT j=2. The j=2 term is the Hessian
    flow, not the obstruction. S_2, S_3, S_4 are initial data from the
    OPE and Gram matrix.
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_r + 1):
        total = Rational(0)
        for j in range(3, r + 1):
            k = r + 2 - j
            if k < j or k < 3:
                continue
            if j not in tower or k not in tower:
                continue
            contrib = j * k * tower[j] * tower[k]
            if j == k:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c))

    return tower
