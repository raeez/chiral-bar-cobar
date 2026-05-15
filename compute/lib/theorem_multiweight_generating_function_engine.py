r"""Finite-window generating-function diagnostics for the W_3 cross channel.

FINITE-WINDOW DIAGNOSTIC SURFACE
================================

For the W_3 algebra, the cross-channel correction delta_F_g^cross has been
computed at g = 2, 3, 4 (thm:multi-weight-genus-expansion). This module
studies the generating function

    G(t, c) = sum_{g >= 2} delta_F_g(c) * t^{2g}

through the certified finite window g = 2, 3, 4.  No all-genus analytic
claim, convergence-radius theorem, analytic tau-function statement, or
KdV/Gelfand-Dickey hierarchy membership is inferred from these three
coefficients.

(1) RATIO ANALYSIS: compute the two available ratios
    delta_F_3 / delta_F_2 and delta_F_4 / delta_F_3.

(2) SHADOW METRIC CONNECTION: test whether G relates to sqrt(Q_L) where
    Q_L is the canonical Virasoro/T-primary shadow metric.

(3) PADE APPROXIMANT: rational reconstruction of the finite window from
    the three known terms.

(4) NUMERATOR FACTORIZATION: factor P_g(c) over Q to find meaningful roots.

DATA (certified by exhaustive graph sum in theorem_multiweight_structure_engine):

    delta_F_2 = (c + 204) / (16 c)
    delta_F_3 = (5c^3 + 3792c^2 + 1149120c + 217071360) / (138240 c^2)
    delta_F_4 = (287c^4 + 268881c^3 + 115455816c^2
                 + 29725133760c + 5594347866240) / (17418240 c^3)

LOCAL VERIFICATION ROUTES:
    1. Evaluation of closed-form formulas in this module.
    2. Cross-check against theorem_multiweight_structure_engine.
    3. Betti stratum reassembly.
    4. Large-c and small-c consistency checks.
    5. Pade self-consistency on exactly the three input coefficients.

References:
    thm:multi-weight-genus-expansion (higher_genus_modular_koszul.tex)
    theorem_multiweight_structure_engine.py
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, gcd, isqrt, log, sqrt
from typing import Any, Dict, List, Optional, Tuple


GENUS_WINDOW: Tuple[int, ...] = (2, 3, 4)
"""Finite genus window certified by the exhaustive W_3 graph sum."""

HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)
"""The seven slots of the holographic package, kept distinct here."""

MODULAR_KOSZUL_COMPUTE_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)
"""The six projections of the modular Koszul compute package."""

BAR_KOSZUL_OBJECT_ROLES: Dict[str, str] = {
    "A": "input chiral algebra",
    "B(A)": "ordered bar coalgebra T^c(s^{-1}bar A)",
    "A^i": "bar cohomology coalgebra H^*(B(A))",
    "A^!": "Verdier/continuous-linear dual algebra branch",
    "Omega(B(A))": "bar-cobar inversion back to A",
    "Z_ch^der(A)": "derived chiral centre ChirHoch^*(A,A), the bulk slot",
}
"""Firewall preventing bar, dual, inversion, and Hochschild/bulk conflation."""


@dataclass(frozen=True)
class W3ChannelData:
    """Diagonal primary-line data for W_3 before cross-channel graph summation."""

    channel: str
    conformal_weight: int
    kappa: Fraction
    S3: Fraction
    S4: Optional[Fraction]


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


def available_genera() -> Tuple[int, ...]:
    """Return the exact genus window available in this engine."""
    return GENUS_WINDOW


# ============================================================================
# Generating function evaluation
# ============================================================================

def generating_function(c: Fraction, max_g: int = 4) -> Dict[int, Fraction]:
    r"""Compute the finite-window coefficients of G(t, c).

    The certified data are only for g in {2, 3, 4}.  This returns the
    available coefficients {2g: delta_F_g(c)} up to max_g; it does not
    extrapolate the all-genus series.
    """
    result = {}
    for g in GENUS_WINDOW:
        if g <= max_g:
            result[2 * g] = delta_Fg(g, c)
    return result


def generating_function_u(c: Fraction, max_g: int = 4) -> Dict[int, Fraction]:
    r"""Finite-window coefficients in u = t^2.

    Returns {g: delta_F_g(c)} for G(u,c) = sum delta_F_g(c) u^g.
    """
    return {g: delta_Fg(g, c) for g in GENUS_WINDOW if g <= max_g}


def evaluate_generating_function(c: Fraction, t: Fraction,
                                  max_g: int = 4) -> Fraction:
    r"""Evaluate the finite-window truncation sum delta_F_g(c) t^{2g}."""
    return evaluate_generating_function_u(c, t * t, max_g=max_g)


def evaluate_generating_function_u(c: Fraction, u: Fraction,
                                   max_g: int = 4) -> Fraction:
    r"""Evaluate the finite-window truncation G(u,c)=sum delta_F_g(c) u^g."""
    total = Fraction(0)
    for g in GENUS_WINDOW:
        if g <= max_g:
            total += delta_Fg(g, c) * u ** g
    return total


# ============================================================================
# Ratio analysis: delta_F_{g+1} / delta_F_g
# ============================================================================

def genus_ratio(g: int, c: Fraction) -> Fraction:
    r"""Compute the adjacent finite-window quotient delta_F_{g+1}/delta_F_g.

    Only R_2 and R_3 are available.  Interpreting these quotients as a
    convergence radius, Gevrey order, or asymptotic law would require
    all-genus control not supplied by this engine.
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
    for g in GENUS_WINDOW[:-1]:  # g=2->3 and g=3->4
        ratios[g] = genus_ratio(g, c)
    return ratios


def ratio_growth_quotient(c: Fraction) -> Fraction:
    r"""Exact finite-window quotient (delta_F_4/delta_F_3)/(delta_F_3/delta_F_2)."""
    ratios = all_genus_ratios(c)
    return ratios[3] / ratios[2]


def ratio_growth_exponent(c: Fraction) -> Optional[float]:
    r"""Finite-window alpha estimate from R_3/R_2 = (3/2)^alpha.

    R_g = delta_F_{g+1}/delta_F_g. If R_3/R_2 ~ (3/2)^alpha, then
    alpha = log(R_3/R_2) / log(3/2).

    This uses only the certified g = 2, 3, 4 window.  It is not an
    all-genus asymptotic theorem.
    """
    ratios = all_genus_ratios(c)
    R2 = ratios[2]  # delta_F_3 / delta_F_2
    R3 = ratios[3]  # delta_F_4 / delta_F_3
    if R2 <= 0 or R3 <= 0:
        return None
    ratio_of_ratios = float(R3) / float(R2)
    if ratio_of_ratios <= 0:
        return None
    return log(ratio_of_ratios) / log(3 / 2)


def ratio_second_difference(c: Fraction) -> Fraction:
    """R_3/R_2 - 1 in the certified g = 2, 3, 4 window."""
    return ratio_growth_quotient(c) - 1


# ============================================================================
# Pade approximant: [1/1] in t^2
# ============================================================================

def pade_11(c: Fraction) -> Tuple[List[Fraction], List[Fraction]]:
    r"""Finite-window [1/1] Pade approximant in the variable u = t^2.

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

    This is a finite-window diagnostic from the three certified coefficients,
    not a theorem about the all-genus radius of convergence.
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

def virasoro_t_line_shadow_data(c: Fraction) -> Dict[str, Fraction]:
    r"""Canonical Virasoro/T-line shadow constants.

    Source: landscape_census.tex, standard-family constants:
    kappa = c/2, S_3 = 2, S_4 = 10/[c(5c+22)],
    Delta = 8*kappa*S_4 = 40/(5c+22).
    """
    if c == 0 or 5 * c + 22 == 0:
        raise ValueError("Virasoro T-line shadow data is singular at c=0,-22/5")
    kappa = c / 2
    S3 = Fraction(2)
    S4 = Fraction(10) / (c * (5 * c + 22))
    Delta = 8 * kappa * S4
    return {
        "kappa": kappa,
        "S3": S3,
        "S4": S4,
        "Delta": Delta,
    }


def w3_diagonal_channel_data(c: Fraction) -> Dict[str, W3ChannelData]:
    r"""Diagonal T/W primary-line data before cross-channel summation.

    The scalar lane uses kappa_T + kappa_W = 5c/6.  The cross-channel
    correction delta_F_g is not obtained by replacing this diagonal datum
    with another scalar kappa; it is the mixed-channel graph sum.
    """
    t_data = virasoro_t_line_shadow_data(c)
    return {
        "T": W3ChannelData(
            channel="T",
            conformal_weight=2,
            kappa=c / 2,
            S3=t_data["S3"],
            S4=t_data["S4"],
        ),
        "W": W3ChannelData(
            channel="W",
            conformal_weight=3,
            kappa=c / 3,
            S3=Fraction(0),
            S4=None,
        ),
    }


def shadow_metric_Q_virasoro(c: Fraction, t: Fraction) -> Fraction:
    r"""Shadow metric Q_L(t) for Virasoro (T-primary line of W_3).

    Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2

    where for Virasoro:
      kappa = c/2
      S_3 = 2
      alpha = S_3
      S_4 = 10/(c*(5c+22))  (Q^contact)
      Delta = 8*kappa*S_4 = 40/(5c+22)  (critical discriminant)
    """
    data = virasoro_t_line_shadow_data(c)
    kappa = data["kappa"]
    alpha = data["S3"]
    Delta = data["Delta"]

    linear = 2 * kappa + 3 * alpha * t
    return linear ** 2 + 2 * Delta * t ** 2


def shadow_metric_zero_modulus_sq(c: Fraction) -> Fraction:
    r"""Squared modulus of the two complex zeros of Q_L(t) for c > 0."""
    data = virasoro_t_line_shadow_data(c)
    kappa = data["kappa"]
    S3 = data["S3"]
    Delta = data["Delta"]
    return 4 * kappa ** 2 / (9 * S3 ** 2 + 2 * Delta)


def shadow_metric_sqrt_series(c: Fraction, max_order: int = 6
                               ) -> List[Fraction]:
    r"""Taylor coefficients of sqrt(Q_L(t)) for Virasoro.

    The formal branch of sqrt(Q_L) is the Virasoro T-line shadow flat
    section.  The comparison with G(t,c) is a finite-window diagnostic
    only; it is not an analytic identification of the W_3 cross-channel
    series with a tau function or a hierarchy solution.

    Returns coefficients [a_0, a_1, a_2, ...] where
    sqrt(Q_L) = a_0 + a_1*t + a_2*t^2 + ...
    """
    data = virasoro_t_line_shadow_data(c)
    kappa = data["kappa"]
    alpha = data["S3"]
    Delta = data["Delta"]

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

    # Formal branch with leading coefficient 2*kappa (positive for c>0).
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
    if g not in NUMERATOR_COEFFS:
        raise ValueError(f"Data not available for g={g}")
    coeffs = NUMERATOR_COEFFS[g]
    D = DENOMINATOR_CONSTS[g]
    return Fraction(coeffs[0], D)


def small_c_leading(g: int) -> Fraction:
    r"""Leading coefficient of delta_F_g as c -> 0+.

    delta_F_g ~ (constant term of P_g) / D_g * c^{-(g-1)} + ...

    The dominant small-c behavior is c^{-(g-1)}, controlled by the
    max-Betti stratum.
    """
    if g not in NUMERATOR_COEFFS:
        raise ValueError(f"Data not available for g={g}")
    coeffs = NUMERATOR_COEFFS[g]
    D = DENOMINATOR_CONSTS[g]
    return Fraction(coeffs[-1], D)


def kappa_w3(c: Fraction) -> Fraction:
    r"""Modular characteristic kappa(W_3, c).

    The principal W_N convention is kappa(W_N) = c * (H_N - 1).
    For W_3: H_3 = 1 + 1/2 + 1/3 = 11/6, so kappa = c * 5/6.

    This is the diagonal scalar lane kappa_T + kappa_W = c/2 + c/3.
    It is not the Virasoro T-line value c/2 and it is not the
    cross-channel correction delta_F_g.
    """
    return Fraction(5) * c / Fraction(6)


def scalar_lane_decomposition(g: int, c: Fraction) -> Dict[str, Fraction]:
    r"""Separate diagonal scalar and mixed cross-channel genus-g pieces."""
    scalar = scalar_Fg(g, c)
    cross = delta_Fg(g, c)
    return {
        "scalar": scalar,
        "cross": cross,
        "total": scalar + cross,
    }


def scalar_Fg(g: int, c: Fraction) -> Fraction:
    r"""Scalar (single-channel) free energy: kappa * lambda_g^FP.

    This is the uniform-weight contribution that the cross-channel
    correction delta_F_g adds to.
    """
    from .theorem_multiweight_structure_engine import lambda_fp
    kappa = kappa_w3(c)
    return kappa * lambda_fp(g)


def total_Fg(g: int, c: Fraction) -> Fraction:
    r"""Certified finite-window W_3 value: F_g = kappa*lambda_g + delta_F_g."""
    return scalar_Fg(g, c) + delta_Fg(g, c)


def cross_to_scalar_ratio(g: int, c: Fraction) -> Fraction:
    r"""Pointwise finite-window ratio delta_F_g / (kappa * lambda_g).

    Values below or above 1 compare the two terms at the chosen c and g.
    They do not assert all-c dominance.
    """
    s = scalar_Fg(g, c)
    if s == 0:
        raise ValueError("Scalar contribution is zero")
    return delta_Fg(g, c) / s


def cross_exceeds_scalar(g: int, c: Fraction) -> bool:
    r"""Whether delta_F_g^cross exceeds kappa(W_3) lambda_g^FP at this c.

    This is a pointwise finite-window comparison.  It is deliberately not
    stated as a uniform theorem in c: at genus 2 the ratio tends to zero
    as c -> infinity because delta_F_2 has constant leading order while
    the scalar lane grows linearly.
    """
    return cross_to_scalar_ratio(g, c) > 1


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
    if g not in DENOMINATOR_CONSTS:
        raise ValueError(f"Data not available for g={g}")
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
    """Run the finite-window generating function analysis at c = c_val.

    Returns a dictionary with all computed quantities.
    """
    c = Fraction(c_val)
    result: Dict[str, Any] = {'c': c_val, 'genus_window': GENUS_WINDOW}

    # 1. delta_F_g values
    result['delta_F'] = {g: delta_Fg(g, c) for g in GENUS_WINDOW}

    # 2. Ratios
    result['ratios'] = all_genus_ratios(c)
    result['ratio_growth'] = ratio_growth_quotient(c)

    # 3. Scalar comparison
    result['scalar_F'] = {g: scalar_Fg(g, c) for g in GENUS_WINDOW}
    result['cross_to_scalar'] = {g: cross_to_scalar_ratio(g, c) for g in GENUS_WINDOW}
    result['scalar_cross_decomposition'] = {
        g: scalar_lane_decomposition(g, c) for g in GENUS_WINDOW
    }

    # 4. Pade
    result['pade_pole'] = pade_pole(c)
    result['pade_errors'] = pade_reconstruction_error(c)

    # 5. Total free energy
    result['total_F'] = {g: total_Fg(g, c) for g in GENUS_WINDOW}

    return result
