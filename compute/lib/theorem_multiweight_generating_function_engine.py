r"""Generating function analysis of the multi-weight cross-channel correction.

GENERATING FUNCTION ANALYSIS (new result)
==========================================

For the W_3 algebra, the cross-channel correction delta_F_g^cross has been
computed at g = 2, 3, 4 (thm:multi-weight-genus-expansion). This module
studies the generating function

    G(t, c) = sum_{g >= 2} delta_F_g(c) * t^{2g}

at specific values of c, seeking structural patterns:

(1) RATIO ANALYSIS: compute delta_F_{g+1} / delta_F_g and test for
    convergence to a radius of convergence or factorial/polynomial growth.

(2) SHADOW METRIC CONNECTION: test whether G relates to sqrt(Q_L) where
    Q_L is the shadow metric on the T-primary line.

(3) PADE APPROXIMANT: rational reconstruction of G from the 3 known terms.

(4) NUMERATOR FACTORIZATION: factor P_g(c) over Q to find meaningful roots.

DATA (PROVED by exhaustive graph sum, from theorem_multiweight_structure_engine):

    delta_F_2 = (c + 204) / (16 c)
    delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
    delta_F_4 = (287c^4 + 268881c^3 + 115455816c^2
                 + 29725133760c + 5594347866240) / (17418240 c^3)

MULTI-PATH VERIFICATION:
    Path 1: Evaluation of closed-form formulas (this module)
    Path 2: Cross-check against theorem_multiweight_structure_engine
    Path 3: Betti stratum reassembly
    Path 4: Asymptotic consistency checks (large c, small c)
    Path 5: Pade self-consistency (reconstruct input from approximant)

References:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    theorem_multiweight_structure_engine.py
    AP27 (bar propagator weight universality)
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import factorial, gcd, isqrt, log, sqrt
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# Core data: closed-form delta_F_g for W_3
# ============================================================================

# Numerator P_g(c) coefficients, highest power first
# delta_F_g = P_g(c) / (D_g * c^{g-1})
NUMERATOR_COEFFS: Dict[int, List[int]] = {
    2: [1, 204],
    3: [5, 3792, 1149120, 217071360],
    4: [287, 268881, 115455816, 29725133760, 5594347866240],
}

DENOMINATOR_CONSTS: Dict[int, int] = {
    2: 16,
    3: 138240,
    4: 17418240,
}


def delta_Fg(g: int, c: Fraction) -> Fraction:
    r"""Exact delta_F_g^cross(W_3, c) from closed-form formula.

    delta_F_g = P_g(c) / (D_g * c^{g-1})
    """
    if g not in NUMERATOR_COEFFS:
        raise ValueError(f"delta_F_g not available for g={g}; need g in {{2,3,4}}")
    if c == 0:
        raise ValueError("c must be nonzero")
    coeffs = NUMERATOR_COEFFS[g]
    D = DENOMINATOR_CONSTS[g]
    deg = len(coeffs) - 1
    P = sum(Fraction(coeffs[k]) * c ** (deg - k) for k in range(len(coeffs)))
    return P / (Fraction(D) * c ** (g - 1))


# ============================================================================
# Generating function evaluation
# ============================================================================

def generating_function(c: Fraction, max_g: int = 4) -> Dict[int, Fraction]:
    r"""Compute G(t, c) coefficients: G = sum_{g>=2} delta_F_g * t^{2g}.

    Returns dict {2g: delta_F_g(c)} for g = 2, ..., max_g.
    """
    result = {}
    for g in range(2, max_g + 1):
        if g in NUMERATOR_COEFFS:
            result[2 * g] = delta_Fg(g, c)
    return result


def evaluate_generating_function(c: Fraction, t: Fraction,
                                  max_g: int = 4) -> Fraction:
    r"""Evaluate G(t, c) = sum_{g>=2} delta_F_g(c) * t^{2g} at given t, c."""
    total = Fraction(0)
    for g in range(2, max_g + 1):
        if g in NUMERATOR_COEFFS:
            total += delta_Fg(g, c) * t ** (2 * g)
    return total


# ============================================================================
# Ratio analysis: delta_F_{g+1} / delta_F_g
# ============================================================================

def genus_ratio(g: int, c: Fraction) -> Fraction:
    r"""Compute delta_F_{g+1}(c) / delta_F_g(c).

    If the generating function has radius of convergence R, the ratios
    should converge to 1/R^2 as g -> infinity (for power series in t^2).

    If the ratios grow like g^alpha, the series has zero radius (Gevrey).
    """
    if g + 1 not in NUMERATOR_COEFFS:
        raise ValueError(f"Need g+1={g+1} data")
    dF_g = delta_Fg(g, c)
    dF_gp1 = delta_Fg(g + 1, c)
    if dF_g == 0:
        raise ValueError(f"delta_F_{g}(c={c}) = 0, ratio undefined")
    return dF_gp1 / dF_g


def all_genus_ratios(c: Fraction) -> Dict[int, Fraction]:
    """Compute all available ratios delta_F_{g+1}/delta_F_g."""
    ratios = {}
    for g in range(2, 4):  # g=2->3 and g=3->4
        ratios[g] = genus_ratio(g, c)
    return ratios


def ratio_growth_exponent(c: Fraction) -> Optional[Fraction]:
    r"""If R_{g+1}/R_g ~ g^alpha, estimate alpha from two data points.

    R_g = delta_F_{g+1}/delta_F_g. If R_3/R_2 ~ (3/2)^alpha, then
    alpha = log(R_3/R_2) / log(3/2).

    Returns None if data is insufficient or the ratio analysis is
    not meaningful (e.g., ratios decrease).
    """
    ratios = all_genus_ratios(c)
    R2 = ratios[2]  # delta_F_3 / delta_F_2
    R3 = ratios[3]  # delta_F_4 / delta_F_3
    if R2 <= 0 or R3 <= 0:
        return None
    # alpha = log(R3/R2) / log(3/2)
    ratio_of_ratios = float(R3) / float(R2)
    if ratio_of_ratios <= 0:
        return None
    alpha_float = log(ratio_of_ratios) / log(3 / 2)
    # Return as fraction approximation
    return Fraction(R3, R2)  # Return the ratio itself; exponent is float


def ratio_second_difference(c: Fraction) -> Fraction:
    """R_3/R_2 - 1: fractional growth of the ratio.

    If this is approximately constant across different c values,
    it suggests the radius of convergence is independent of c.
    """
    ratios = all_genus_ratios(c)
    return ratios[3] / ratios[2] - 1


# ============================================================================
# Pade approximant: [1/1] in t^2
# ============================================================================

def pade_11(c: Fraction) -> Tuple[List[Fraction], List[Fraction]]:
    r"""[1/1] Pade approximant of G(t,c) in the variable u = t^2.

    G(u) = a_2 u^2 + a_3 u^3 + a_4 u^4 + ...

    We seek P(u)/Q(u) = (p0 + p1*u) / (1 + q1*u) matching the first 3
    coefficients (in u^2, u^3, u^4).

    Formally, write H(u) = G(u)/u^2 = a_2 + a_3*u + a_4*u^2 + ...
    Then [1/1] Pade of H in u: (p0 + p1*u)/(1 + q1*u).

    Matching:
      H(0) = a_2  =>  p0 = a_2
      H'(0) = a_3  =>  p1 + p0*(-q1) = a_3  =>  p1 = a_3 + a_2*q1
      (1/2)H''(0) = a_4  =>  ...

    From the Pade equations:
      q1 = -a_4 / a_3   (if a_3 != 0)
      p0 = a_2
      p1 = a_3 - a_2 * a_4 / a_3 = (a_3^2 - a_2*a_4) / a_3

    Returns (numerator_coeffs [p0, p1], denominator_coeffs [1, q1])
    """
    a2 = delta_Fg(2, c)
    a3 = delta_Fg(3, c)
    a4 = delta_Fg(4, c)

    if a3 == 0:
        raise ValueError("a_3 = 0, Pade [1/1] undefined")

    q1 = -a4 / a3
    p0 = a2
    p1 = (a3 * a3 - a2 * a4) / a3

    return ([p0, p1], [Fraction(1), q1])


def pade_evaluate(c: Fraction, u: Fraction) -> Fraction:
    """Evaluate the [1/1] Pade approximant at u = t^2.

    Returns P(u)/Q(u) * u^2.
    """
    num_c, den_c = pade_11(c)
    P = num_c[0] + num_c[1] * u
    Q = den_c[0] + den_c[1] * u
    if Q == 0:
        raise ValueError("Pade denominator vanishes")
    return P / Q * u * u


def pade_pole(c: Fraction) -> Fraction:
    """Location of the Pade pole: u_pole = -1/q1 = a_3/a_4.

    This estimates the radius of convergence of G(u) in the u = t^2 variable.
    The radius of convergence in t is sqrt(u_pole).
    """
    _, den_c = pade_11(c)
    q1 = den_c[1]
    if q1 == 0:
        raise ValueError("q1 = 0, no finite pole")
    return -Fraction(1) / q1


def pade_reconstruction_error(c: Fraction) -> Dict[int, Fraction]:
    """Verify Pade [1/1] reproduces input coefficients exactly.

    The [1/1] Pade has 3 free parameters (p0, p1, q1) and 3 input
    coefficients (a_2, a_3, a_4), so the reconstruction should be exact.
    """
    a2 = delta_Fg(2, c)
    a3 = delta_Fg(3, c)
    a4 = delta_Fg(4, c)

    num_c, den_c = pade_11(c)
    p0, p1 = num_c
    q1 = den_c[1]

    # Reconstruct: H(u) = (p0 + p1*u)/(1 + q1*u) = a2 + a3*u + a4*u^2 + ...
    # Taylor expand: H = p0 + (p1 - p0*q1)*u + (p0*q1^2 - p1*q1)*u^2 + ...
    rec_a2 = p0
    rec_a3 = p1 - p0 * q1
    rec_a4 = p0 * q1 ** 2 - p1 * q1

    return {
        2: a2 - rec_a2,
        3: a3 - rec_a3,
        4: a4 - rec_a4,
    }


# ============================================================================
# Shadow metric connection
# ============================================================================

def shadow_metric_Q_virasoro(c: Fraction, t: Fraction) -> Fraction:
    r"""Shadow metric Q_L(t) for Virasoro (T-primary line of W_3).

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    where for Virasoro:
      kappa = c/2
      S_3 = -6/(c*(5c+22))  (cubic shadow coefficient)
      alpha = S_3
      S_4 = 10/(c^2*(5c+22))  (Q^contact)
      Delta = 8*kappa*S_4 = 40/(c*(5c+22))  (critical discriminant)
    """
    kappa = c / 2
    S3 = Fraction(-6) / (c * (5 * c + 22))
    S4 = Fraction(10) / (c ** 2 * (5 * c + 22))
    Delta = 8 * kappa * S4  # = 40 / (c * (5c+22))
    alpha = S3

    linear = 2 * kappa + 3 * alpha * t
    return linear ** 2 + 2 * Delta * t ** 2


def shadow_metric_sqrt_series(c: Fraction, max_order: int = 6
                               ) -> List[Fraction]:
    r"""Taylor coefficients of sqrt(Q_L(t)) for Virasoro.

    sqrt(Q_L) is the flat section of the shadow connection.
    Compare with the generating function G(t,c) to test whether
    G = f(sqrt(Q_L)) for some simple f.

    Returns coefficients [a_0, a_1, a_2, ...] where
    sqrt(Q_L) = a_0 + a_1*t + a_2*t^2 + ...
    """
    kappa = c / 2
    S3 = Fraction(-6) / (c * (5 * c + 22))
    S4 = Fraction(10) / (c ** 2 * (5 * c + 22))
    Delta = 8 * kappa * S4
    alpha = S3

    # Q_L(t) = (2kappa)^2 + 12*kappa*alpha*t + (9*alpha^2 + 2*Delta)*t^2
    # = A + B*t + C*t^2  where A=(2kappa)^2, B=12*kappa*alpha, C=9*alpha^2+2*Delta
    A = (2 * kappa) ** 2
    B = 12 * kappa * alpha
    C = 9 * alpha ** 2 + 2 * Delta

    # sqrt(A + B*t + C*t^2) = sqrt(A) * sqrt(1 + (B/A)*t + (C/A)*t^2)
    # Taylor expand sqrt(1 + x) where x = (B/A)*t + (C/A)*t^2
    # sqrt(1+x) = 1 + x/2 - x^2/8 + x^3/16 - ...

    if A == 0:
        return [Fraction(0)] * max_order

    sqrtA = kappa  # sqrt(4*kappa^2) = 2*|kappa| but we track sign; for c>0, kappa>0
    # Actually sqrt(A) = 2*kappa for c>0
    sqrtA_val = 2 * kappa

    b = B / A  # = 12*kappa*alpha / (4*kappa^2) = 3*alpha/kappa
    cc = C / A  # = (9*alpha^2 + 2*Delta) / (4*kappa^2)

    # Compute coefficients of sqrt(1 + b*t + cc*t^2) via recursive formula
    # Let f(t) = sqrt(1 + b*t + cc*t^2), f(0) = 1
    # 2*f*f' = b + 2*cc*t  =>  f' = (b + 2*cc*t) / (2*f)
    # Taylor: f_0 = 1, and for n >= 1:
    #   f_n from the identity (1 + b*t + cc*t^2) * (sum f_n t^n)^2 = sum (coeff of t^n)

    # Simpler: just compute by expanding (1+x)^{1/2} with x = bt + cc*t^2
    # Coefficients of x^k at order t^n, then sum with binomial(1/2, k)

    coeffs = [Fraction(0)] * max_order

    # x = b*t + cc*t^2, so x^k has terms at t^{k}, t^{k+1}, ..., t^{2k}
    # x^k = sum_{j=0}^{k} C(k,j) * b^{k-j} * cc^j * t^{k+j}

    # binomial(1/2, k) = (1/2)(1/2 - 1)...(1/2 - k + 1) / k!
    def binom_half(k: int) -> Fraction:
        if k == 0:
            return Fraction(1)
        num = Fraction(1)
        for i in range(k):
            num *= (Fraction(1, 2) - i)
        return num / Fraction(factorial(k))

    for n in range(max_order):
        total = Fraction(0)
        for k in range(n + 1):
            bk = binom_half(k)
            # coefficient of t^n in x^k
            # x^k = (b*t + cc*t^2)^k = sum_{j=0}^{k} C(k,j) b^{k-j} cc^j t^{k+j}
            # need k + j = n, so j = n - k
            j = n - k
            if j < 0 or j > k:
                continue
            comb = Fraction(factorial(k), factorial(j) * factorial(k - j))
            term = bk * comb * b ** (k - j) * cc ** j
            total += term
        coeffs[n] = total

    # Multiply by sqrt(A) = 2*kappa
    return [sqrtA_val * c_n for c_n in coeffs]


# ============================================================================
# Numerator factorization
# ============================================================================

def numerator_polynomial(g: int) -> List[int]:
    """Return P_g(c) coefficients [highest, ..., lowest power]."""
    if g not in NUMERATOR_COEFFS:
        raise ValueError(f"Data not available for g={g}")
    return list(NUMERATOR_COEFFS[g])


def numerator_roots_float(g: int) -> List[complex]:
    """Approximate roots of P_g(c) as complex numbers.

    Uses numpy if available, otherwise companion matrix via pure Python
    for low-degree polynomials.
    """
    coeffs = numerator_polynomial(g)
    deg = len(coeffs) - 1

    if deg == 1:
        # Linear: a*c + b = 0 => c = -b/a
        return [complex(-coeffs[1] / coeffs[0])]

    # For higher degree, use the companion matrix eigenvalue approach
    # or direct formulas
    if deg == 2:
        a, b, c_coeff = coeffs
        disc = b * b - 4 * a * c_coeff
        if disc >= 0:
            sq = sqrt(disc)
            return [complex((-b + sq) / (2 * a)), complex((-b - sq) / (2 * a))]
        else:
            sq = sqrt(-disc)
            return [
                complex(-b / (2 * a), sq / (2 * a)),
                complex(-b / (2 * a), -sq / (2 * a)),
            ]

    if deg == 3:
        # Use numpy-free cubic via Cardano, or just evaluate numerically
        # For robustness, use iterative root finding
        return _find_roots_numerically(coeffs)

    if deg == 4:
        return _find_roots_numerically(coeffs)

    return _find_roots_numerically(coeffs)


def _find_roots_numerically(coeffs: List[int], tol: float = 1e-12,
                             max_iter: int = 1000) -> List[complex]:
    """Find roots of polynomial with integer coefficients via Durand-Kerner.

    P(x) = coeffs[0]*x^n + coeffs[1]*x^{n-1} + ... + coeffs[n]
    """
    n = len(coeffs) - 1
    if n == 0:
        return []

    # Normalize
    lead = float(coeffs[0])
    a = [c / lead for c in coeffs]

    # Initial guesses on a circle of radius |a_n/a_0|^{1/n}
    R = abs(a[-1]) ** (1.0 / n) if abs(a[-1]) > 0 else 1.0
    import cmath
    roots = [R * cmath.exp(2j * cmath.pi * k / n + 0.4j) for k in range(n)]

    for _ in range(max_iter):
        max_change = 0.0
        for i in range(n):
            # Evaluate polynomial at roots[i]
            val = complex(1.0)
            for k in range(n + 1):
                if k == 0:
                    val = complex(a[0])
                else:
                    val = val * roots[i] + a[k]
            # Denominator: product of (roots[i] - roots[j]) for j != i
            denom = complex(1.0)
            for j in range(n):
                if j != i:
                    diff = roots[i] - roots[j]
                    if abs(diff) < 1e-30:
                        diff = complex(1e-15, 1e-15)
                    denom *= diff
            correction = val / denom
            roots[i] -= correction
            max_change = max(max_change, abs(correction))
        if max_change < tol:
            break

    # Sort: real roots first (by real part), then complex pairs
    real_roots = []
    complex_roots = []
    for r in roots:
        if abs(r.imag) < 1e-8:
            real_roots.append(complex(r.real, 0))
        else:
            complex_roots.append(r)

    real_roots.sort(key=lambda z: z.real)
    complex_roots.sort(key=lambda z: (z.real, abs(z.imag)))

    return real_roots + complex_roots


def numerator_rational_roots(g: int) -> List[Fraction]:
    """Find exact rational roots of P_g(c) via rational root theorem.

    If P_g = a_0 c^n + ... + a_n, rational roots are p/q where
    p | a_n and q | a_0.
    """
    coeffs = numerator_polynomial(g)
    a0 = abs(coeffs[0])
    an = abs(coeffs[-1])

    # Divisors of a number (for small numbers; use prime factorization for large)
    def divisors(n: int) -> List[int]:
        if n == 0:
            return [0]
        divs = []
        for d in range(1, isqrt(n) + 1):
            if n % d == 0:
                divs.append(d)
                if d != n // d:
                    divs.append(n // d)
        return sorted(divs)

    candidates = set()
    for p in divisors(an):
        for q in divisors(a0):
            if q == 0:
                continue
            candidates.add(Fraction(p, q))
            candidates.add(Fraction(-p, q))

    roots = []
    for r in sorted(candidates, key=lambda x: abs(x)):
        val = sum(
            Fraction(coeffs[k]) * r ** (len(coeffs) - 1 - k)
            for k in range(len(coeffs))
        )
        if val == 0:
            roots.append(r)

    return roots


def numerator_gcd_content(g: int) -> int:
    """GCD of all numerator coefficients (the content of P_g)."""
    coeffs = numerator_polynomial(g)
    result = abs(coeffs[0])
    for c in coeffs[1:]:
        result = gcd(result, abs(c))
    return result


# ============================================================================
# Large-c and small-c asymptotics
# ============================================================================

def large_c_leading(g: int) -> Fraction:
    r"""Leading coefficient of delta_F_g as c -> infinity.

    delta_F_g ~ (leading coeff of P_g) / D_g * c^{deg(P_g) - (g-1)}
    For g = 2: delta_F_2 ~ 1/16 (constant)
    For g >= 3: delta_F_g ~ (P_g leading) / D_g * c (linear in c)
    """
    coeffs = NUMERATOR_COEFFS[g]
    D = DENOMINATOR_CONSTS[g]
    return Fraction(coeffs[0], D)


def small_c_leading(g: int) -> Fraction:
    r"""Leading coefficient of delta_F_g as c -> 0+.

    delta_F_g ~ (constant term of P_g) / D_g * c^{-(g-1)} + ...

    The dominant small-c behavior is c^{-(g-1)}, controlled by the
    max-Betti stratum.
    """
    coeffs = NUMERATOR_COEFFS[g]
    D = DENOMINATOR_CONSTS[g]
    return Fraction(coeffs[-1], D)


def kappa_w3(c: Fraction) -> Fraction:
    r"""Modular characteristic kappa(W_3, c).

    kappa(W_3) = c * (5c + 22) / (5 * 6 * 2) = c * (5c + 22) / 60

    DERIVATION: For W_N at level k, the central charge is
    c = (N-1)(1 - N(N+1)/(k+N)). For W_3: c = 2(1 - 12/(k+3)).
    kappa = dim(g) * (k + h^v) / (2 * h^v) with dim(sl_3)=8, h^v=3.
    But for W-algebras, kappa = c * (H_N - 1) where H_N = harmonic number.
    For W_3: H_3 = 1 + 1/2 + 1/3 = 11/6, so kappa = c * 5/6.

    AP39 WARNING: kappa != c/2 for W-algebras. kappa(W_3) = 5c/6.
    """
    return Fraction(5) * c / Fraction(6)


def scalar_Fg(g: int, c: Fraction) -> Fraction:
    r"""Scalar (single-channel) free energy: kappa * lambda_g^FP.

    This is the uniform-weight contribution that the cross-channel
    correction delta_F_g adds to.
    """
    from .theorem_multiweight_structure_engine import lambda_fp
    kappa = kappa_w3(c)
    return kappa * lambda_fp(g)


def total_Fg(g: int, c: Fraction) -> Fraction:
    r"""Total genus-g free energy: F_g = kappa * lambda_g + delta_F_g."""
    return scalar_Fg(g, c) + delta_Fg(g, c)


def cross_to_scalar_ratio(g: int, c: Fraction) -> Fraction:
    r"""Ratio delta_F_g / (kappa * lambda_g): how large the correction is.

    If this ratio is << 1, the scalar approximation is good.
    If this ratio is >> 1, the cross-channel dominates.
    """
    s = scalar_Fg(g, c)
    if s == 0:
        raise ValueError("Scalar contribution is zero")
    return delta_Fg(g, c) / s


# ============================================================================
# Denominator structure analysis
# ============================================================================

def denominator_factored(g: int) -> Dict[str, Any]:
    """Analyze the denominator D_g * c^{g-1}.

    Test whether D_g relates to known combinatorial quantities:
    - (2g)! or (2g-2)!
    - Products of factorials from graph automorphisms
    - Powers of 2 from Z_2 channel parity
    """
    D = DENOMINATOR_CONSTS[g]

    # Prime factorization
    factors: Dict[int, int] = {}
    n = D
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    # Check divisibility by standard quantities
    facts = {
        f'{2*g}!': factorial(2 * g),
        f'{2*g-2}!': factorial(2 * g - 2),
        f'{2*g-1}!': factorial(2 * g - 1),
    }
    divisibility = {}
    for name, val in facts.items():
        if D % val == 0:
            divisibility[name] = D // val
        elif val % D == 0:
            divisibility[name] = Fraction(1, val // D)

    return {
        'D_g': D,
        'prime_factors': factors,
        'divisibility': divisibility,
        'g': g,
    }


# ============================================================================
# Full analysis at a given c value
# ============================================================================

def full_analysis(c_val: int) -> Dict[str, Any]:
    """Run the complete generating function analysis at c = c_val.

    Returns a dictionary with all computed quantities.
    """
    c = Fraction(c_val)
    result: Dict[str, Any] = {'c': c_val}

    # 1. delta_F_g values
    result['delta_F'] = {g: delta_Fg(g, c) for g in [2, 3, 4]}

    # 2. Ratios
    result['ratios'] = all_genus_ratios(c)
    result['ratio_growth'] = result['ratios'][3] / result['ratios'][2]

    # 3. Scalar comparison
    result['scalar_F'] = {g: scalar_Fg(g, c) for g in [2, 3, 4]}
    result['cross_to_scalar'] = {g: cross_to_scalar_ratio(g, c) for g in [2, 3, 4]}

    # 4. Pade
    result['pade_pole'] = pade_pole(c)
    result['pade_errors'] = pade_reconstruction_error(c)

    # 5. Total free energy
    result['total_F'] = {g: total_Fg(g, c) for g in [2, 3, 4]}

    return result
