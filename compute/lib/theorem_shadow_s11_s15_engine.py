r"""Shadow obstruction tower: S_11 through S_15 and asymptotic growth rate.

CLOSED-FORM RESULTS (Virasoro):

    S_11(c) = -15360(91125c^3 + 990225c^2 + 3500190c + 3988097)
              / [11 c^8 (5c+22)^4]

    S_12(c) = 2560(4100625c^4 + 59413500c^3 + 315017100c^2
              + 717857460c + 583976486) / [3 c^9 (5c+22)^5]

    S_13(c) = -552960(455625c^4 + 6196500c^3 + 30285900c^2
              + 61608540c + 41821334) / [13 c^10 (5c+22)^5]

    S_14(c) = 61440(61509375c^5 + 1045659375c^4 + 6814327500c^3
              + 20792882250c^2 + 28229400450c + 11646558206)
              / [7 c^11 (5c+22)^6]

    S_15(c) = -49152(61509375c^5 + 977315625c^4 + 5793727500c^3
              + 15153459750c^2 + 14607504450c - 433898894)
              / [c^12 (5c+22)^6]

    S_15 is the FIRST shadow coefficient whose numerator has a positive
    real zero: c_0 ~ 0.02883.  For c < c_0, S_15 has sign +1 instead of
    the generic (-1)^15 = -1.

ASYMPTOTIC GROWTH RATE (thm:shadow-growth-rate):

    S_r(c) ~ C(c) * rho(c)^r * r^{-5/2} * cos(r*theta(c) + phi(c))

    where:
        rho(c) = sqrt((180c+872) / (c^2(5c+22)))  = 1/|t_*|
        theta(c) = pi - |arg(t_*)|
        t_* = nearest zero of Q_L(t) = c^2 + 12ct + [(180c+872)/(5c+22)]t^2

    GROWTH CLASS: Gevrey-0 (sub-factorial).
        |S_r| / r! -> 0 as r -> infinity.
        No factorial growth.  The series is NOT Gevrey-1.

    PROOF (Darboux transfer theorem):
        The generating function H(t) = t^2 sqrt(Q_L(t)) has algebraic
        branch points at the zeros of Q_L(t).  By the Darboux transfer
        theorem for algebraic singularities:
            [t^n] sqrt(1 - t/t_*) ~ -1/(2 sqrt(pi)) * t_*^{-n} * n^{-3/2}
        The Taylor coefficient a_n of f = sqrt(Q_L) therefore satisfies
            a_n ~ C * |t_*|^{-n} * n^{-3/2}  (with oscillatory correction
            from the complex conjugate branch point).
        Since S_r = a_{r-2}/r, we obtain
            S_r ~ C' * rho^r * r^{-5/2}
        where the -5/2 exponent is -3/2 (from the square-root singularity)
        minus 1 (from the division by r).

    CONVERGENCE RADIUS:
        The shadow Taylor series sum S_r t^r converges for |t| < 1/rho(c).
        rho(c) = 1  iff  5c^3 + 22c^2 - 180c - 872 = 0
                     iff  c = c* ~ 6.12537.
        For c > c*: rho < 1, shadow expansion CONVERGES.
        For c < c*: rho > 1, shadow expansion DIVERGES geometrically.

    BOREL SUMMABILITY:
        The geometric divergence (Gevrey-0) is milder than the factorial
        divergence (Gevrey-1) of the string genus expansion.  The shadow
        series is Borel summable along all non-Stokes directions.
        The Stokes directions are determined by the argument of the
        branch points of Q_L.

    CRITICAL CENTRAL CHARGE:
        c* = unique positive real root of 5c^3 + 22c^2 - 180c - 872 = 0
        c* ~ 6.12536830
        At c = c*: rho = 1 (marginal convergence, logarithmic corrections).
        At c = 1:  rho ~ 6.24 (strong divergence).
        At c = 13: rho ~ 0.467 (strong convergence).
        At c = 26: rho ~ 0.232 (very strong convergence).

    OSCILLATORY STRUCTURE:
        The branch points of Q_L(t) are complex conjugates (since
        disc(Q_L) = -320c^2/(5c+22) < 0 for c > 0).  The oscillatory
        factor cos(r*theta + phi) has beat period
            T = pi / (pi - |arg(t_*)|).
        This controls the phase slip: the (-1)^r sign pattern breaks
        at r_slip ~ T + 4.

References:
    thm:shadow-growth-rate (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-denominator (theorem_shadow_s9_s10_engine.py, proved)
    thm:shadow-double-convergence (higher_genus_modular_koszul.tex)
    rem:shadow-borel-summability (higher_genus_modular_koszul.tex)
    prop:universal-instanton-action (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple, Union

from sympy import (
    Poly,
    Rational,
    Symbol,
    cancel,
    denom,
    expand,
    factor,
    limit,
    numer,
    oo,
    simplify,
    solve,
    sqrt,
)

c = Symbol('c')
k = Symbol('k')


# =========================================================================
# 1. Core: inherited from S9/S10 engine
# =========================================================================

def virasoro_shadow_metric():
    """Q_L(t) = c^2 + 12c t + [(180c+872)/(5c+22)] t^2."""
    q0 = c**2
    q1 = 12 * c
    q2 = (180 * c + 872) / (5 * c + 22)
    return q0, q1, q2


# =========================================================================
# 2. Convolution recursion (primary computation path)
# =========================================================================

def convolution_coefficients(max_n: int = 28) -> list:
    r"""Taylor coefficients a_n of f(t) = sqrt(Q_L(t)).

    f^2 = Q_L implies:
        a_0 = c, a_1 = 6,
        a_2 = (q2 - a_1^2) / (2c),
        a_n = -(1/(2c)) sum_{j=1}^{n-1} a_j a_{n-j}  for n >= 3.
    """
    q0, q1, q2 = virasoro_shadow_metric()
    a = [None] * (max_n + 1)
    a[0] = c
    if max_n >= 1:
        a[1] = cancel(q1 / (2 * c))  # = 6
    if max_n >= 2:
        a[2] = cancel((q2 - a[1]**2) / (2 * c))
    for n in range(3, max_n + 1):
        conv_sum = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = cancel(-conv_sum / (2 * c))
    return a


def shadow_coefficients_convolution(max_r: int = 30) -> Dict[int, Any]:
    """S_r via convolution: S_r = a_{r-2}/r."""
    a = convolution_coefficients(max_n=max_r - 2)
    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = factor(cancel(a[n] / r))
    return result


# =========================================================================
# 3. Master equation recursion (independent verification path)
# =========================================================================

def shadow_coefficients_master_eq(max_r: int = 30) -> Dict[int, Any]:
    r"""S_r via the projected MC equation.

    For r >= 5:
        S_r = -(1/(rc)) sum_{3<=j<=k, j+k=r+2} eps(j,k) j k S_j S_k
    where eps = 1 if j < k, 1/2 if j = k.
    """
    tower = {}
    tower[2] = c / 2
    tower[3] = Rational(2)
    tower[4] = Rational(10) / (c * (5 * c + 22))

    for r in range(5, max_r + 1):
        total = Rational(0)
        for j in range(3, r + 1):
            k_val = r + 2 - j
            if k_val < j or k_val < 3:
                continue
            if j not in tower or k_val not in tower:
                continue
            contrib = j * k_val * tower[j] * tower[k_val]
            if j == k_val:
                contrib = contrib / 2
            total += contrib
        tower[r] = cancel(-total / (r * c))

    return tower


# =========================================================================
# 4. ODE 3-term recurrence (third independent path)
# =========================================================================

def shadow_coefficients_ode(max_r: int = 30) -> Dict[int, Any]:
    r"""S_r via 2 Q_L f' = Q_L' f.

    Three-term linear recurrence:
        2 q0 (n+1) a_{n+1} = q1 (1-2n) a_n + 2 q2 (2-n) a_{n-1}.
    """
    q0, q1, q2 = virasoro_shadow_metric()
    max_n = max_r - 2
    a = [None] * (max_n + 2)
    a[0] = c
    a[1] = cancel(q1 * a[0] / (2 * q0))

    for n in range(1, max_n + 1):
        rhs = q1 * (1 - 2 * n) * a[n]
        rhs += 2 * q2 * (2 - n) * a[n - 1]
        a[n + 1] = cancel(rhs / (2 * q0 * (n + 1)))

    result = {}
    for r in range(2, max_r + 1):
        n = r - 2
        if n <= len(a) - 1 and a[n] is not None:
            result[r] = factor(cancel(a[n] / r))
    return result


# =========================================================================
# 5. Explicit closed-form formulas S_2 through S_15
# =========================================================================

def S_explicit(r: int):
    """Explicit closed-form S_r for Virasoro, r = 2, ..., 15."""
    if r == 2:
        return c / 2
    if r == 3:
        return Rational(2)
    if r == 4:
        return Rational(10) / (c * (5 * c + 22))
    if r == 5:
        return Rational(-48) / (c**2 * (5 * c + 22))
    if r == 6:
        return (Rational(80) * (45 * c + 193)
                / (3 * c**3 * (5 * c + 22)**2))
    if r == 7:
        return (Rational(-2880) * (15 * c + 61)
                / (7 * c**4 * (5 * c + 22)**2))
    if r == 8:
        return (Rational(80) * (2025 * c**2 + 16470 * c + 33314)
                / (c**5 * (5 * c + 22)**3))
    if r == 9:
        return (Rational(-1280) * (2025 * c**2 + 15570 * c + 29554)
                / (3 * c**6 * (5 * c + 22)**3))
    if r == 10:
        return (Rational(256) * (91125 * c**3 + 1050975 * c**2
                                 + 3989790 * c + 4969967)
                / (c**7 * (5 * c + 22)**4))
    if r == 11:
        return (Rational(-15360)
                * (91125 * c**3 + 990225 * c**2
                   + 3500190 * c + 3988097)
                / (11 * c**8 * (5 * c + 22)**4))
    if r == 12:
        return (Rational(2560)
                * (4100625 * c**4 + 59413500 * c**3
                   + 315017100 * c**2 + 717857460 * c
                   + 583976486)
                / (3 * c**9 * (5 * c + 22)**5))
    if r == 13:
        return (Rational(-552960)
                * (455625 * c**4 + 6196500 * c**3
                   + 30285900 * c**2 + 61608540 * c
                   + 41821334)
                / (13 * c**10 * (5 * c + 22)**5))
    if r == 14:
        return (Rational(61440)
                * (61509375 * c**5 + 1045659375 * c**4
                   + 6814327500 * c**3 + 20792882250 * c**2
                   + 28229400450 * c + 11646558206)
                / (7 * c**11 * (5 * c + 22)**6))
    if r == 15:
        return (Rational(-49152)
                * (61509375 * c**5 + 977315625 * c**4
                   + 5793727500 * c**3 + 15153459750 * c**2
                   + 14607504450 * c - 433898894)
                / (c**12 * (5 * c + 22)**6))
    raise ValueError(f"Explicit formula not implemented for r={r}")


# =========================================================================
# 6. Simplified explicit formulas using direct numerator polynomials
# =========================================================================

def S_explicit_factored(r: int):
    """Explicit S_r in fully factored form (numerator as polynomial)."""
    if r < 2 or r > 15:
        raise ValueError(f"r={r} out of range [2, 15]")
    coeffs = shadow_coefficients_convolution(max_r=r)
    return coeffs[r]


# =========================================================================
# 7. Growth rate: rho(c) = sqrt(q2/q0)
# =========================================================================

def shadow_growth_rate_squared():
    """rho^2 = q2/q0 = (180c+872)/[c^2(5c+22)]."""
    q0, _, q2 = virasoro_shadow_metric()
    return cancel(q2 / q0)


def growth_rate_numerical(c_val: float) -> float:
    """Numerical growth rate rho at a given c."""
    rho2 = (180 * c_val + 872) / (c_val**2 * (5 * c_val + 22))
    return math.sqrt(rho2)


# =========================================================================
# 8. Branch points and convergence radius
# =========================================================================

def branch_points(c_val: float) -> Tuple[complex, complex]:
    """Zeros of Q_L(t) at numerical c.  Always a conjugate pair for c > 0."""
    q0 = c_val**2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872) / (5.0 * c_val + 22)
    disc = q1**2 - 4 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2 * q2)
    t_minus = (-q1 - sqrt_disc) / (2 * q2)
    return t_plus, t_minus


def convergence_radius(c_val: float) -> float:
    """Convergence radius R = |t_*| of the shadow Taylor series.

    The shadow series sum S_r t^r converges for |t| < R.
    """
    t_plus, t_minus = branch_points(c_val)
    return min(abs(t_plus), abs(t_minus))


def convergence_radius_symbolic():
    """Symbolic convergence radius: R = sqrt(q0/q2) = c * sqrt((5c+22)/(180c+872))."""
    q0, _, q2 = virasoro_shadow_metric()
    return sqrt(q0 / q2)


# =========================================================================
# 9. Critical central charge
# =========================================================================

def critical_central_charge_polynomial():
    """5c^3 + 22c^2 - 180c - 872 = 0 defines rho(c) = 1."""
    return 5 * c**3 + 22 * c**2 - 180 * c - 872


def critical_central_charge_numerical() -> float:
    """c* ~ 6.12537: the unique positive root of rho(c) = 1."""
    roots = solve(critical_central_charge_polynomial(), c)
    for r in roots:
        rv = complex(r)
        if abs(rv.imag) < 1e-10 and rv.real > 0:
            return float(rv.real)
    raise RuntimeError("No positive root found")


# =========================================================================
# 10. Asymptotic analysis
# =========================================================================

def darboux_exponent() -> Rational:
    """The power-law exponent in S_r ~ C * rho^r * r^alpha.

    alpha = -5/2: composed of -3/2 (Darboux for sqrt singularity)
    and -1 (from S_r = a_{r-2}/r).
    """
    return Rational(-5, 2)


def asymptotic_parameters(c_val: float) -> Dict[str, float]:
    """Full asymptotic parameters at a given c.

    Returns rho, theta (branch point argument), beat_period, alpha.
    """
    t_plus, _ = branch_points(c_val)
    rho = 1.0 / abs(t_plus)
    theta_bp = cmath.phase(t_plus)
    beat = math.pi / abs(math.pi - abs(theta_bp))
    return {
        'rho': rho,
        'theta_deg': math.degrees(theta_bp),
        'beat_period': beat,
        'alpha': -2.5,
        'convergence_radius': abs(t_plus),
    }


def root_test(c_val: Union[int, Fraction], max_r: int = 15
              ) -> List[Tuple[int, float]]:
    """Root test: |S_r|^{1/r} should converge to rho."""
    cf = Fraction(c_val) if isinstance(c_val, int) else c_val
    a = _convolution_numerical(cf, max_r - 2)
    results = []
    for r in range(4, max_r + 1):
        n = r - 2
        Sr = a[n] / r
        val = abs(float(Sr))
        if val > 0:
            root = val ** (1.0 / r)
            results.append((r, root))
    return results


def ratio_test(c_val: Union[int, Fraction], max_r: int = 15
               ) -> List[Tuple[int, float, float]]:
    """Ratio test: |S_{r+1}/S_r| vs predicted rho.

    Returns [(r, ratio, rho)].
    """
    cf = Fraction(c_val) if isinstance(c_val, int) else c_val
    a = _convolution_numerical(cf, max_r - 2)
    rho = growth_rate_numerical(float(cf))
    results = []
    for r in range(4, max_r):
        n = r - 2
        n1 = r - 1
        Sr = abs(float(a[n] / r))
        Sr1 = abs(float(a[n1] / (r + 1)))
        if Sr > 0:
            ratio = Sr1 / Sr
            results.append((r, ratio, rho))
    return results


def gevrey_test(c_val: Union[int, Fraction], max_r: int = 15
                ) -> List[Tuple[int, float]]:
    """Test |S_r|/r! -> 0 (Gevrey-0 = sub-factorial growth).

    Returns [(r, |S_r|/r!)].
    """
    cf = Fraction(c_val) if isinstance(c_val, int) else c_val
    a = _convolution_numerical(cf, max_r - 2)
    results = []
    for r in range(4, max_r + 1):
        n = r - 2
        Sr = abs(float(a[n] / r))
        if Sr > 0:
            ratio = Sr / math.factorial(r)
            results.append((r, ratio))
    return results


# =========================================================================
# 11. Exact Fraction evaluation
# =========================================================================

def _convolution_numerical(c_frac: Fraction, max_n: int) -> list:
    """Convolution coefficients a_n at exact rational c."""
    q0 = c_frac**2
    q1 = 12 * c_frac
    q2 = Fraction(180 * c_frac + 872, 5 * c_frac + 22)
    a = [None] * (max_n + 1)
    a[0] = c_frac
    if max_n >= 1:
        a[1] = q1 / (2 * c_frac)
    if max_n >= 2:
        a[2] = (q2 - a[1]**2) / (2 * c_frac)
    for n in range(3, max_n + 1):
        s = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -s / (2 * c_frac)
    return a


def virasoro_S_fraction(r: int, c_val: Union[int, Fraction]) -> Fraction:
    """Evaluate S_r(Vir) at an exact rational c value."""
    c_f = Fraction(c_val) if isinstance(c_val, int) else c_val
    if c_f == 0:
        raise ValueError("c=0 is a pole of S_r for r >= 4")
    if 5 * c_f + 22 == 0:
        raise ValueError("c=-22/5 is a pole of S_r for r >= 4")
    a = _convolution_numerical(c_f, r - 2)
    return a[r - 2] / r


# =========================================================================
# 12. Structural theorems verification for S_11-S_15
# =========================================================================

def denominator_exponents(r: int) -> Tuple[int, int]:
    """Predicted denominator exponents: (pow_c, pow_5c22).

    denom(S_r) = rho(r) * c^{r-3} * (5c+22)^{floor((r-2)/2)}.
    """
    return (r - 3, (r - 2) // 2)


def verify_denominator_theorem(max_r: int = 15) -> List[Tuple[int, bool]]:
    """Verify denominator theorem for S_11 through S_max_r."""
    coeffs = shadow_coefficients_convolution(max_r)
    results = []
    for r in range(11, max_r + 1):
        Sr = cancel(coeffs[r])
        d = denom(Sr)
        d_poly = Poly(d, c)

        pow_c = 0
        rem = d_poly
        while rem.eval(0) == 0:
            pow_c += 1
            rem = Poly(cancel(rem.as_expr() / c), c)

        pow_5c22 = 0
        while rem.eval(Rational(-22, 5)) == 0:
            pow_5c22 += 1
            rem = Poly(cancel(rem.as_expr() / (5 * c + 22)), c)

        pred_c, pred_5c22 = denominator_exponents(r)
        results.append((r, pow_c == pred_c and pow_5c22 == pred_5c22))
    return results


def verify_numerator_degree(max_r: int = 15) -> List[Tuple[int, int, int, bool]]:
    """Verify deg_c(numer(S_r)) = floor((r-4)/2) for S_11-S_max_r."""
    coeffs = shadow_coefficients_convolution(max_r)
    results = []
    for r in range(11, max_r + 1):
        Sr = cancel(coeffs[r])
        n = numer(Sr)
        n_poly = Poly(n, c)
        d = n_poly.total_degree()
        pred = (r - 4) // 2
        results.append((r, d, pred, d == pred))
    return results


# =========================================================================
# 13. Koszul duality at c=13
# =========================================================================

def duality_ratio_at_c13(max_r: int = 15) -> Dict[int, Any]:
    """Verify S_r(c)/S_r(26-c) = 1 at c=13."""
    coeffs = shadow_coefficients_convolution(max_r)
    results = {}
    for r in range(4, max_r + 1):
        Sr = coeffs[r]
        Sr_dual = Sr.subs(c, 26 - c)
        ratio = cancel(Sr / Sr_dual)
        ratio_at_13 = cancel(ratio.subs(c, 13))
        results[r] = ratio_at_13
    return results


# =========================================================================
# 14. S_15 numerator zero analysis
# =========================================================================

def s15_positive_zero() -> float:
    """The unique positive real zero of the S_15 numerator.

    61509375c^5 + 977315625c^4 + 5793727500c^3
    + 15153459750c^2 + 14607504450c - 433898894 = 0
    has a unique positive root c_0 ~ 0.02883.
    """
    poly = (61509375 * c**5 + 977315625 * c**4
            + 5793727500 * c**3 + 15153459750 * c**2
            + 14607504450 * c - 433898894)
    roots = solve(poly, c)
    for r in roots:
        rv = complex(r)
        if abs(rv.imag) < 1e-10 and rv.real > 0:
            return float(rv.real)
    raise RuntimeError("No positive root found")


# =========================================================================
# 15. Affine sl_2 specialization
# =========================================================================

def affine_sl2_central_charge():
    """c(sl_2, k) = 3k/(k+2)."""
    return 3 * k / (k + 2)


def affine_sl2_shadow_coefficient(r: int):
    """S_r for affine sl_2 via Sugawara substitution c = 3k/(k+2)."""
    coeffs = shadow_coefficients_convolution(max_r=r)
    return factor(cancel(coeffs[r].subs(c, 3 * k / (k + 2))))


# =========================================================================
# 16. Cross-engine consistency
# =========================================================================

def verify_cross_engine_s9_s10(max_r: int = 15) -> List[Tuple[int, bool]]:
    """Verify our S_2-S_10 agree with the S9/S10 engine."""
    from compute.lib.theorem_shadow_s9_s10_engine import (
        shadow_coefficients_convolution as s910_conv,
    )
    ours = shadow_coefficients_convolution(max_r)
    theirs = s910_conv(max_r=min(max_r, 10))
    results = []
    for r in range(2, min(max_r, 10) + 1):
        diff = simplify(ours[r] - theirs[r])
        results.append((r, diff == 0))
    return results


# =========================================================================
# 17. Large-c asymptotics of S_r
# =========================================================================

def large_c_leading_order(r: int):
    """Leading behavior of S_r as c -> infinity.

    S_r ~ const / c^{r-3-floor((r-4)/2)} as c -> infinity.
    The exponent is r - 3 - floor((r-4)/2) = ceil((r-2)/2).
    """
    coeffs = shadow_coefficients_convolution(max_r=r)
    Sr = coeffs[r]
    return limit(Sr * c**((r - 2 + 1) // 2), c, oo)


# =========================================================================
# 18. Summary data table
# =========================================================================

def shadow_tower_table(max_r: int = 15) -> Dict[int, Dict[str, Any]]:
    """Complete data for S_2 through S_max_r.

    Returns {r: {formula, numer_deg, denom_pow_c, denom_pow_5c22,
                  lead_sign, sign_pred, ...}}.
    """
    coeffs = shadow_coefficients_convolution(max_r)
    results = {}
    for r in range(4, max_r + 1):
        Sr = cancel(coeffs[r])
        d = denom(Sr)
        d_poly = Poly(d, c)

        pow_c = 0
        rem = d_poly
        while rem.eval(0) == 0:
            pow_c += 1
            rem = Poly(cancel(rem.as_expr() / c), c)

        pow_5c22 = 0
        while rem.eval(Rational(-22, 5)) == 0:
            pow_5c22 += 1
            rem = Poly(cancel(rem.as_expr() / (5 * c + 22)), c)

        n = numer(Sr)
        n_poly = Poly(n, c)

        results[r] = {
            'pow_c': pow_c,
            'pow_5c22': pow_5c22,
            'numer_deg': n_poly.total_degree(),
            'lead_sign': 1 if float(n_poly.LC()) > 0 else -1,
            'pred_pow_c': r - 3,
            'pred_pow_5c22': (r - 2) // 2,
            'pred_numer_deg': (r - 4) // 2,
            'pred_lead_sign': (-1)**r,
        }
    return results
