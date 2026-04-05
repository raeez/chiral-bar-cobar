r"""Shadow zeta functions and analytic continuation for modular Koszul algebras.

For a modular Koszul algebra A with shadow coefficients S_r(A) (arity-r
projections of the universal MC element Theta_A), define the SHADOW ZETA
FUNCTION:

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s}

This is a Dirichlet series whose analytic properties encode the complexity
of the shadow obstruction tower.  The abscissa of convergence sigma_c(A)
classifies the tower's growth:

    Class G (Heisenberg):    sigma_c = -infinity  (finite sum, entire)
    Class L (affine KM):     sigma_c = -infinity  (finite sum, entire)
    Class C (beta-gamma):    sigma_c = -infinity  (finite sum, entire)
    Class M (Virasoro, W_N): sigma_c > 0          (from S_r ~ rho^r r^{-5/2})

For class M algebras the abscissa is:
    sigma_c = log(rho) / log(e) = log(rho)     [NOT log(rho)/log(r)]

Actually sigma_c = lim sup (log|S_r|) / log(r).  Since |S_r| ~ C rho^r r^{-5/2},
    log|S_r| ~ r log(rho) - (5/2) log(r) + const
    log|S_r| / log(r) ~ r log(rho) / log(r) -> +infinity if rho > 1.

So for rho > 1: sigma_c = +infinity (diverges for all s).
For rho < 1: sigma_c = -infinity (converges for all s, entire!).
For rho = 1 (critical): sigma_c = 5/2 (borderline, from r^{-5/2} decay).

COMPLETED SHADOW ZETA:

    Lambda_A(s) = Gamma(s/2) * pi^{-s/2} * zeta_A(s)

This is the analogue of the Riemann xi function, with the gamma factor
absorbing the analytic structure at s = 0.

TWISTED SHADOW ZETA:

    zeta_A(s, chi) = sum_{r >= 2} S_r(A) * chi(r) * r^{-s}

for a Dirichlet character chi.  This probes the arithmetic structure of
the shadow tower modulo the conductor of chi.

MELLIN TRANSFORM RELATION:

    zeta_A(s) = (1/Gamma(s)) * integral_0^infty H_A(e^{-t}) * t^{s-1} dt

where H_A(x) = sum_{r >= 2} S_r * x^r is the shadow generating function.
This integral converges for Re(s) > sigma_c and provides the analytic
continuation.

EULER PRODUCT:  For MULTIPLICATIVE shadow sequences (S_{mn} = S_m * S_n
for coprime m, n), the zeta function has an Euler product factorization.
Standard shadow towers are NOT multiplicative in general (the recursion
is quadratic, not multiplicative).  However, the Heisenberg tower is
trivially multiplicative (only one nonzero term).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    cor:shadow-extraction (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction as F
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from sympy import (
    Abs,
    Rational,
    Symbol,
    cancel,
    gamma as sym_gamma,
    log as sym_log,
    oo,
    pi as sym_pi,
    simplify,
    sqrt,
    zoo,
)

c = Symbol('c')


# ============================================================================
# 1.  Shadow coefficient providers for each family
# ============================================================================

def heisenberg_shadow_coefficients(k_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for Heisenberg H_k.

    S_2 = k (the level = the modular characteristic kappa).
    S_r = 0 for all r >= 3 (class G, Gaussian archetype).

    Ground truth: shadow_tower_atlas.py, prop:heisenberg-shadow-termination.
    """
    result = {2: float(k_val)}
    for r in range(3, max_r + 1):
        result[r] = 0.0
    return result


def affine_sl2_shadow_coefficients(k_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_2).

    kappa = dim(sl_2) * (k + h^v) / (2 * h^v) = 3(k+2)/4.
    S_3 = cubic shadow (from Lie bracket/Sugawara); level-dependent.

    For the primary (Sugawara/stress-tensor) line:
        S_3 = alpha, where alpha depends on normalization.
        In the Sugawara normalization: alpha = 2*h^v/(k + h^v) = 4/(k+2).

    S_r = 0 for r >= 4 (class L, tower terminates by Jacobi identity).

    CAUTION: The cubic shadow normalization varies across modules.
    We use the Sugawara-line convention from linf_bracket_engine.py:
        alpha = 2*h^v/(k + h^v) for sl_2, h^v = 2.
    At level k=1: alpha = 4/3.
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def affine_sl3_shadow_coefficients(k_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_3).

    kappa = dim(sl_3) * (k + h^v) / (2 * h^v) = 8*(k+3)/6 = 4(k+3)/3.
    S_3 = cubic shadow from Lie bracket.

    For sl_3: dim(g) = 8, h^v = 3.
    Sugawara cubic: alpha = 2*h^v/(k + h^v) = 6/(k+3).

    S_r = 0 for r >= 4 (class L, Jacobi identity).
    """
    h_dual = 3.0
    dim_g = 8.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {2: kappa, 3: alpha}
    for r in range(4, max_r + 1):
        result[r] = 0.0
    return result


def virasoro_shadow_coefficients_numerical(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c via convolution recursion.

    Uses H(t) = t^2 * sqrt(Q_L(t)) where Q_L(t) = c^2 + 12c*t + alpha(c)*t^2
    with alpha(c) = (180c + 872)/(5c + 22).

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).

    Ground truth: virasoro_shadow_extended.py, shadow_tower_ode.py.
    """
    if c_val == 0.0 or 5.0 * c_val + 22.0 == 0.0:
        raise ValueError(f"Virasoro shadow undefined at c={c_val} (pole of Q_L)")

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    # Taylor coefficients of sqrt(Q_L(t))
    a0 = math.sqrt(abs(q0))
    if c_val < 0:
        a0 = -a0  # sqrt(c^2) = |c|; for c < 0, a0 = -c > 0... but we need a0 = c for the convolution
        # Actually sqrt(c^2) = |c|, and the generating function uses the POSITIVE square root.
        # For c > 0: a0 = c. For c < 0: a0 = |c| = -c, and the recursion gives S_r with the
        # correct sign structure. We use a0 = |c| always.
        a0 = abs(c_val)

    a = [a0]
    if max_r >= 3:
        a1 = q1 / (2.0 * a0)
        a.append(a1)
    if max_r >= 4:
        a2 = (q2 - a[1] ** 2) / (2.0 * a0)
        a.append(a2)
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)
    return result


def betagamma_shadow_coefficients(lam_val: float = 0.5, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for beta-gamma at weight lambda.

    The beta-gamma system at weight lambda has:
        c = 2(6*lambda^2 - 6*lambda + 1)
        kappa = c/2 = 6*lambda^2 - 6*lambda + 1
        On the T-line: S_3 = 2, S_4 = 10/(c(5c+22))
        Tower terminates at arity 4 (class C) on the FULL deformation complex.

    For the 1D T-line restriction, we use the Virasoro shadow data at central
    charge c(lambda). The GLOBAL termination at arity 4 comes from stratum
    separation (thm:betagamma-rank-one-rigidity), so on the 1D T-line the tower
    continues to infinity. However, the global shadow depth is r_max = 4.

    For the shadow zeta, we use the GLOBAL shadow:
        S_2 = kappa, S_3 = 2, S_4 = 10/(c(5c+22)), S_r = 0 for r >= 5.
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0

    result = {2: kappa, 3: 2.0}
    if c_val != 0.0 and 5.0 * c_val + 22.0 != 0.0:
        result[4] = 10.0 / (c_val * (5.0 * c_val + 22.0))
    else:
        result[4] = 0.0

    for r in range(5, max_r + 1):
        result[r] = 0.0
    return result


def w3_t_line_shadow_coefficients(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for W_3 along the T-line (Virasoro restriction).

    On the T-line, the W_3 shadow tower is identical to Virasoro.
    kappa_T = c/2, S_3 = 2, S_4 = 10/(c(5c+22)).
    """
    return virasoro_shadow_coefficients_numerical(c_val, max_r)


def w3_w_line_shadow_coefficients(c_val: float, max_r: int = 30) -> Dict[int, float]:
    """Shadow coefficients for W_3 along the W-line.

    kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W = 2560/(c(5c+22)^3).
    Odd arities vanish.

    Q_W(w) = 4*(c/3)^2 + 16*(c/3)*S4_W * w^2.
    """
    kappa_W = c_val / 3.0
    S4_W = 2560.0 / (c_val * (5.0 * c_val + 22.0) ** 3)

    q0 = 4.0 * kappa_W ** 2
    q1 = 0.0  # alpha = 0
    q2 = 16.0 * kappa_W * S4_W

    a0 = math.sqrt(abs(q0))
    if a0 == 0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    a = [a0]
    if max_r >= 3:
        a1 = q1 / (2.0 * a0)  # = 0
        a.append(a1)
    if max_r >= 4:
        a2 = (q2 - a[1] ** 2) / (2.0 * a0)
        a.append(a2)
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {}
    for n in range(len(a)):
        r = n + 2
        result[r] = a[n] / float(r)
    return result


# ============================================================================
# 2.  Shadow zeta function: direct summation
# ============================================================================

def shadow_zeta_numerical(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate zeta_A(s) = sum_{r >= 2} S_r * r^{-s} by direct summation.

    Parameters
    ----------
    shadow_coeffs : dict mapping arity r to shadow coefficient S_r
    s : complex number at which to evaluate
    max_r : truncation arity (default: max key in shadow_coeffs)

    Returns
    -------
    Complex value of the partial sum.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        total += Sr * r ** (-s)
    return total


def shadow_zeta_at_integers(
    shadow_coeffs: Dict[int, float],
    s_values: List[int],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Evaluate zeta_A(s) at integer values of s.

    For real s and real S_r, the result is real.
    """
    result = {}
    for s in s_values:
        val = shadow_zeta_numerical(shadow_coeffs, complex(s, 0), max_r)
        result[s] = val.real
    return result


# ============================================================================
# 3.  Completed shadow zeta: Lambda_A(s) = Gamma(s/2) * pi^{-s/2} * zeta_A(s)
# ============================================================================

def completed_shadow_zeta_numerical(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate Lambda_A(s) = Gamma(s/2) * pi^{-s/2} * zeta_A(s).

    The gamma factor regularizes the behaviour near s = 0.
    """
    zeta_val = shadow_zeta_numerical(shadow_coeffs, s, max_r)
    gamma_val = cmath.exp(math.lgamma(s.real / 2.0))  # Real gamma for real s
    if s.imag != 0:
        # For complex s, use the log-gamma relation
        # Gamma(s/2) via Stirling or scipy if available; fallback to real approx
        try:
            from scipy.special import gamma as scipy_gamma
            gamma_val = scipy_gamma(s / 2.0)
        except ImportError:
            # Use the reflection formula or real part approximation
            gamma_val = cmath.exp(_log_gamma_complex(s / 2.0))
    pi_factor = math.pi ** (-s.real / 2.0)
    if s.imag != 0:
        pi_factor = cmath.exp(-s / 2.0 * cmath.log(math.pi))
    return gamma_val * pi_factor * zeta_val


def _log_gamma_complex(z: complex) -> complex:
    """Stirling approximation for log(Gamma(z)) for Re(z) > 0."""
    # Stirling: log(Gamma(z)) ~ z*log(z) - z - log(z)/2 + log(2*pi)/2
    if z.real > 0:
        return z * cmath.log(z) - z - cmath.log(z) / 2 + cmath.log(2 * math.pi) / 2
    # For Re(z) <= 0, use reflection: Gamma(z)*Gamma(1-z) = pi/sin(pi*z)
    # log Gamma(z) = log(pi) - log(sin(pi*z)) - log(Gamma(1-z))
    return (cmath.log(math.pi) - cmath.log(cmath.sin(math.pi * z))
            - _log_gamma_complex(1.0 - z))


# ============================================================================
# 4.  Abscissa of convergence
# ============================================================================

def abscissa_of_convergence(
    shadow_coeffs: Dict[int, float],
    min_r: int = 5,
) -> float:
    """Estimate sigma_c = lim sup (log|S_r|) / log(r).

    For finite towers (class G, L, C): returns -infinity (all S_r = 0 for large r).
    For class M: sigma_c depends on the growth rate rho.
        If rho < 1: sigma_c = -infinity (series entire).
        If rho = 1: sigma_c = 5/2 (from r^{-5/2} decay).
        If rho > 1: sigma_c = +infinity (series diverges for all s).

    Returns
    -------
    Estimated abscissa.  Returns -1e10 for -infinity, 1e10 for +infinity.
    """
    max_r = max(shadow_coeffs.keys())

    # Check if tower is finite (all S_r = 0 beyond some point)
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r
    if last_nonzero < max_r - 5:
        return -1e10  # Finite tower => entire function

    # Compute lim sup of log|S_r| / log(r) for large r
    ratios = []
    for r in range(max(min_r, 5), max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-300:
            ratios.append(math.log(abs(Sr)) / math.log(r))

    if not ratios:
        return -1e10

    # The lim sup: take the maximum of the last few values
    # (for oscillating sequences, this is approximate)
    return max(ratios[-min(10, len(ratios)):])


def abscissa_from_growth_rate(rho: float) -> float:
    """Exact abscissa of convergence from the shadow growth rate rho.

    For |S_r| ~ C * rho^r * r^{-5/2}:
        rho < 1: sigma_c = -infinity (entire)
        rho = 1: sigma_c = 5/2
        rho > 1: sigma_c = +infinity

    This is the EXACT result, not an estimate from finite data.
    """
    if rho < 1.0 - 1e-12:
        return float('-inf')
    elif abs(rho - 1.0) < 1e-12:
        return 2.5  # 5/2
    else:
        return float('inf')


# ============================================================================
# 5.  Shadow growth rate computation
# ============================================================================

def shadow_growth_rate_from_coeffs(
    shadow_coeffs: Dict[int, float],
    min_r: int = 10,
) -> float:
    """Estimate rho from |S_{r+1}/S_r| for large r.

    For class M: converges to rho as r -> infinity.
    For finite towers: returns 0.0.
    """
    max_r = max(shadow_coeffs.keys())

    # Check for finite tower
    last_nonzero = 2
    for r in range(2, max_r + 1):
        if abs(shadow_coeffs.get(r, 0.0)) > 1e-50:
            last_nonzero = r
    if last_nonzero < max_r - 5:
        return 0.0

    # Compute consecutive ratios
    ratios = []
    for r in range(max(min_r, 5), max_r):
        Sr = shadow_coeffs.get(r, 0.0)
        Sr1 = shadow_coeffs.get(r + 1, 0.0)
        if abs(Sr) > 1e-200 and abs(Sr1) > 1e-200:
            ratios.append(abs(Sr1 / Sr))

    if not ratios:
        return 0.0
    return ratios[-1]


def virasoro_growth_rate_exact(c_val: float) -> float:
    """Exact shadow growth rate for Virasoro at central charge c.

    rho(Vir_c) = sqrt((180c + 872) / ((5c + 22) * c^2)).
    """
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return float('inf')
    return math.sqrt(numer / denom)


# ============================================================================
# 6.  Mellin transform path (verification path 2)
# ============================================================================

def shadow_generating_function_numerical(
    shadow_coeffs: Dict[int, float],
    x: float,
) -> float:
    """Evaluate H_A(x) = sum_{r >= 2} S_r * x^r.

    This is the shadow generating function at the point x.
    """
    max_r = max(shadow_coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        total += Sr * x ** r
    return total


def mellin_transform_zeta(
    shadow_coeffs: Dict[int, float],
    s: float,
    n_points: int = 2000,
    t_max: float = 30.0,
) -> float:
    """Compute zeta_A(s) via the Mellin transform:

        zeta_A(s) = (1/Gamma(s)) * integral_0^infty H_A(e^{-t}) * t^{s-1} dt

    Uses numerical quadrature (trapezoidal rule on a log-transformed grid).

    This provides an INDEPENDENT verification of the direct summation.
    Only valid for real s > sigma_c.
    """
    if s <= 0:
        return float('nan')

    # Gamma(s) for real s > 0
    gamma_s = math.gamma(s)

    # Numerical integration: transform t = e^u, dt = e^u du
    # integral = int_{-inf}^{ln(t_max)} H(e^{-e^u}) * e^{u(s-1)} * e^u du
    #          = int H(e^{-e^u}) * e^{u*s} du
    # But simpler: direct trapezoidal on [eps, t_max]
    dt = t_max / n_points
    integral = 0.0
    for i in range(1, n_points):
        t = i * dt
        x = math.exp(-t)
        if x < 1e-300:
            break
        H_val = shadow_generating_function_numerical(shadow_coeffs, x)
        integral += H_val * t ** (s - 1) * dt

    return integral / gamma_s


# ============================================================================
# 7.  Twisted shadow zeta (Dirichlet characters)
# ============================================================================

def dirichlet_character_mod4(n: int) -> int:
    """The nontrivial Dirichlet character mod 4: chi_4(n).

    chi_4(1) = 1, chi_4(3) = -1, chi_4(0) = chi_4(2) = 0.
    This is the Legendre symbol (-4/n), the character of Q(i).
    """
    n_mod = n % 4
    if n_mod == 1:
        return 1
    elif n_mod == 3:
        return -1
    else:
        return 0


def dirichlet_character_mod8_1(n: int) -> int:
    """The character chi_8^{(1)}(n) = (8/n): odd part mod 8.

    chi(1) = 1, chi(3) = -1, chi(5) = -1, chi(7) = 1, chi(even) = 0.
    """
    if n % 2 == 0:
        return 0
    n_mod = n % 8
    if n_mod in (1, 7):
        return 1
    elif n_mod in (3, 5):
        return -1
    return 0


def dirichlet_character_mod8_2(n: int) -> int:
    """The character chi_8^{(2)}(n) = (-8/n).

    chi(1) = 1, chi(3) = 1, chi(5) = -1, chi(7) = -1, chi(even) = 0.
    """
    if n % 2 == 0:
        return 0
    n_mod = n % 8
    if n_mod in (1, 3):
        return 1
    elif n_mod in (5, 7):
        return -1
    return 0


def twisted_shadow_zeta_numerical(
    shadow_coeffs: Dict[int, float],
    s: complex,
    character_fn: Callable[[int], int],
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate zeta_A(s, chi) = sum_{r >= 2} S_r * chi(r) * r^{-s}.

    Parameters
    ----------
    shadow_coeffs : arity -> S_r
    s : complex evaluation point
    character_fn : Dirichlet character r -> chi(r)
    max_r : truncation
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        chi_r = character_fn(r)
        if Sr == 0.0 or chi_r == 0:
            continue
        total += Sr * chi_r * r ** (-s)
    return total


# ============================================================================
# 8.  Euler product analysis
# ============================================================================

def check_multiplicativity(
    shadow_coeffs: Dict[int, float],
    max_r: int = 20,
    tol: float = 1e-8,
) -> Tuple[bool, List[Tuple[int, int, float]]]:
    """Check if the shadow sequence is multiplicative: S_{mn} = S_m * S_n for gcd(m,n)=1.

    Returns (is_multiplicative, list_of_violations) where violations
    are triples (m, n, |S_{mn} - S_m * S_n|).

    Standard shadow towers are NOT multiplicative in general.
    """
    violations = []
    for m in range(2, max_r + 1):
        for n in range(m, max_r // m + 1):
            if m * n > max_r:
                break
            if math.gcd(m, n) != 1:
                continue
            Sm = shadow_coeffs.get(m, 0.0)
            Sn = shadow_coeffs.get(n, 0.0)
            Smn = shadow_coeffs.get(m * n, 0.0)
            error = abs(Smn - Sm * Sn)
            if error > tol:
                violations.append((m, n, error))

    return (len(violations) == 0, violations)


def formal_euler_product_coefficients(
    shadow_coeffs: Dict[int, float],
    primes: Optional[List[int]] = None,
    max_r: int = 20,
) -> Dict[int, List[float]]:
    """Extract formal Euler factor coefficients at each prime p.

    For a Dirichlet series sum a_n n^{-s}, the Euler factor at p is
    sum_{k >= 0} a_{p^k} p^{-ks}. Here a_r = S_r.

    Returns dict mapping prime p to [S_{p^0}, S_{p^1}, S_{p^2}, ...].
    Note: S_1 = 0 (tower starts at r=2), and p^0 = 1 is not in the sum.
    """
    if primes is None:
        primes = [2, 3, 5, 7, 11, 13]

    result = {}
    for p in primes:
        coeffs = []
        pk = 1
        while pk <= max_r:
            coeffs.append(shadow_coeffs.get(pk, 0.0))
            pk *= p
        result[p] = coeffs
    return result


# ============================================================================
# 9.  Special values and residue computations
# ============================================================================

def shadow_zeta_special_values(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    """Compute special values of the shadow zeta function.

    Returns dict with:
        'zeta(0)' = sum S_r (formal, may diverge)
        'zeta(1)' = sum S_r / r
        'zeta(2)' = sum S_r / r^2
        'zeta(-1)' = sum S_r * r (formal)
        'zeta_prime(0)' = -sum S_r * log(r)
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    z0 = sum(shadow_coeffs.get(r, 0.0) for r in range(2, max_r + 1))
    z1 = sum(shadow_coeffs.get(r, 0.0) / r for r in range(2, max_r + 1))
    z2 = sum(shadow_coeffs.get(r, 0.0) / r ** 2 for r in range(2, max_r + 1))
    zm1 = sum(shadow_coeffs.get(r, 0.0) * r for r in range(2, max_r + 1))
    zp0 = -sum(
        shadow_coeffs.get(r, 0.0) * math.log(r)
        for r in range(2, max_r + 1)
        if shadow_coeffs.get(r, 0.0) != 0.0
    )

    return {
        'zeta(0)': z0,
        'zeta(1)': z1,
        'zeta(2)': z2,
        'zeta(-1)': zm1,
        'zeta_prime(0)': zp0,
    }


# ============================================================================
# 10. Heisenberg closed-form analysis
# ============================================================================

def heisenberg_zeta_exact(k_val: float, s: complex) -> complex:
    """Exact shadow zeta for Heisenberg: zeta_{H_k}(s) = k * 2^{-s}.

    This is a single-term Dirichlet series (class G).
    """
    return k_val * 2.0 ** (-s)


def heisenberg_completed_zeta(k_val: float, s: complex) -> complex:
    """Completed Heisenberg shadow zeta: Gamma(s/2) * pi^{-s/2} * k * 2^{-s}.

    = k * Gamma(s/2) * (2*pi)^{-s/2} * sqrt(2)^s * 2^{-s}
    Actually: k * Gamma(s/2) * pi^{-s/2} * 2^{-s}.
    """
    try:
        gamma_val = math.gamma(s.real / 2.0) if s.imag == 0 else cmath.exp(_log_gamma_complex(s / 2.0))
    except (ValueError, OverflowError):
        return complex(float('nan'), 0)
    pi_factor = math.pi ** (-s.real / 2.0) if s.imag == 0 else cmath.exp(-s / 2.0 * cmath.log(math.pi))
    return k_val * gamma_val * pi_factor * 2.0 ** (-s)


# ============================================================================
# 11. Functional equation analysis
# ============================================================================

def functional_equation_test(
    shadow_coeffs: Dict[int, float],
    s_values: List[complex],
    target_weight: float = 1.0,
    max_r: Optional[int] = None,
) -> List[Tuple[complex, complex, complex]]:
    """Test for a functional equation of the form Lambda(s) = Lambda(w - s)
    for various candidate weights w.

    Returns list of (s, Lambda(s), Lambda(w-s)) for comparison.
    """
    results = []
    for s in s_values:
        Ls = completed_shadow_zeta_numerical(shadow_coeffs, s, max_r)
        Lws = completed_shadow_zeta_numerical(shadow_coeffs, complex(target_weight, 0) - s, max_r)
        results.append((s, Ls, Lws))
    return results


# ============================================================================
# 12. Cross-family comparison
# ============================================================================

@dataclass
class ShadowZetaData:
    """Complete shadow zeta data for a modular Koszul algebra."""
    name: str
    shadow_class: str  # G, L, C, M
    shadow_coeffs: Dict[int, float]
    kappa: float
    growth_rate: float
    abscissa: float
    special_values: Dict[str, float]
    is_multiplicative: bool

    def zeta(self, s: complex) -> complex:
        return shadow_zeta_numerical(self.shadow_coeffs, s)


def compute_shadow_zeta_data(
    name: str,
    shadow_class: str,
    shadow_coeffs: Dict[int, float],
) -> ShadowZetaData:
    """Compute full shadow zeta data for a given algebra."""
    kappa = shadow_coeffs.get(2, 0.0)
    rho = shadow_growth_rate_from_coeffs(shadow_coeffs)
    sigma = abscissa_of_convergence(shadow_coeffs)
    specials = shadow_zeta_special_values(shadow_coeffs)
    is_mult, _ = check_multiplicativity(shadow_coeffs)

    return ShadowZetaData(
        name=name,
        shadow_class=shadow_class,
        shadow_coeffs=shadow_coeffs,
        kappa=kappa,
        growth_rate=rho,
        abscissa=sigma,
        special_values=specials,
        is_multiplicative=is_mult,
    )


# ============================================================================
# 13. Full landscape computation
# ============================================================================

def compute_full_landscape(max_r: int = 30) -> Dict[str, ShadowZetaData]:
    """Compute shadow zeta data for the full standard landscape.

    Returns dict mapping algebra name to ShadowZetaData.
    """
    landscape = {}

    # Heisenberg at k=1
    coeffs = heisenberg_shadow_coefficients(1.0, max_r)
    landscape['Heis_k=1'] = compute_shadow_zeta_data('Heis_k=1', 'G', coeffs)

    # Heisenberg at k=2
    coeffs = heisenberg_shadow_coefficients(2.0, max_r)
    landscape['Heis_k=2'] = compute_shadow_zeta_data('Heis_k=2', 'G', coeffs)

    # Affine sl_2 at k=1
    coeffs = affine_sl2_shadow_coefficients(1.0, max_r)
    landscape['aff_sl2_k=1'] = compute_shadow_zeta_data('aff_sl2_k=1', 'L', coeffs)

    # Affine sl_3 at k=1
    coeffs = affine_sl3_shadow_coefficients(1.0, max_r)
    landscape['aff_sl3_k=1'] = compute_shadow_zeta_data('aff_sl3_k=1', 'L', coeffs)

    # Beta-gamma at lambda=1/2 (symplectic bosons, c=-1)
    coeffs = betagamma_shadow_coefficients(0.5, max_r)
    landscape['bg_lam=1/2'] = compute_shadow_zeta_data('bg_lam=1/2', 'C', coeffs)

    # Beta-gamma at lambda=1 (c=2)
    coeffs = betagamma_shadow_coefficients(1.0, max_r)
    landscape['bg_lam=1'] = compute_shadow_zeta_data('bg_lam=1', 'C', coeffs)

    # Virasoro at c=1
    coeffs = virasoro_shadow_coefficients_numerical(1.0, max_r)
    landscape['Vir_c=1'] = compute_shadow_zeta_data('Vir_c=1', 'M', coeffs)

    # Virasoro at c=13 (self-dual)
    coeffs = virasoro_shadow_coefficients_numerical(13.0, max_r)
    landscape['Vir_c=13'] = compute_shadow_zeta_data('Vir_c=13', 'M', coeffs)

    # Virasoro at c=26
    coeffs = virasoro_shadow_coefficients_numerical(26.0, max_r)
    landscape['Vir_c=26'] = compute_shadow_zeta_data('Vir_c=26', 'M', coeffs)

    # W_3 T-line at c=50
    coeffs = w3_t_line_shadow_coefficients(50.0, max_r)
    landscape['W3_T_c=50'] = compute_shadow_zeta_data('W3_T_c=50', 'M', coeffs)

    # W_3 W-line at c=50
    coeffs = w3_w_line_shadow_coefficients(50.0, max_r)
    landscape['W3_W_c=50'] = compute_shadow_zeta_data('W3_W_c=50', 'M', coeffs)

    return landscape


# ============================================================================
# 14. Virasoro shadow zeta closed-form ingredients
# ============================================================================

def virasoro_zeta_from_ode(c_val: float, s: float, max_r: int = 100) -> float:
    """Compute Virasoro shadow zeta using extended tower from ODE.

    The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) satisfies
    the algebraic equation H^2 = t^4 * Q_L(t), giving all S_r from the
    convolution recursion to arbitrary arity.
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    return shadow_zeta_numerical(coeffs, complex(s, 0), max_r).real


def virasoro_zeta_values_table(
    c_values: List[float],
    s_values: List[float],
    max_r: int = 50,
) -> Dict[Tuple[float, float], float]:
    """Compute a table of zeta_{Vir_c}(s) for given c and s values."""
    table = {}
    for c_val in c_values:
        coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
        for s in s_values:
            table[(c_val, s)] = shadow_zeta_numerical(coeffs, complex(s, 0), max_r).real
    return table


# ============================================================================
# 15. Koszul duality relation for shadow zeta
# ============================================================================

def virasoro_koszul_dual_zeta_relation(
    c_val: float,
    s: float,
    max_r: int = 50,
) -> Dict[str, float]:
    """Compute zeta_{Vir_c}(s) and zeta_{Vir_{26-c}}(s) and their sum/difference.

    Koszul duality: Vir_c^! = Vir_{26-c}.
    The shadow zeta of the dual algebra is obtained by c -> 26 - c.
    """
    c_dual = 26.0 - c_val
    coeffs_A = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_dual = virasoro_shadow_coefficients_numerical(c_dual, max_r)

    zeta_A = shadow_zeta_numerical(coeffs_A, complex(s, 0), max_r).real
    zeta_dual = shadow_zeta_numerical(coeffs_dual, complex(s, 0), max_r).real

    return {
        'c': c_val,
        'c_dual': c_dual,
        'zeta_A': zeta_A,
        'zeta_dual': zeta_dual,
        'sum': zeta_A + zeta_dual,
        'difference': zeta_A - zeta_dual,
    }


# ============================================================================
# 16. Affine KM exact closed forms
# ============================================================================

def affine_sl2_zeta_exact(k_val: float, s: complex) -> complex:
    """Exact shadow zeta for affine sl_2:

    zeta_{sl_2,k}(s) = kappa * 2^{-s} + alpha * 3^{-s}

    where kappa = 3(k+2)/4, alpha = 4/(k+2).
    Only two nonzero terms (class L, tower terminates at arity 3).
    """
    kappa = 3.0 * (k_val + 2.0) / 4.0
    alpha = 4.0 / (k_val + 2.0)
    return kappa * 2.0 ** (-s) + alpha * 3.0 ** (-s)


def affine_sl3_zeta_exact(k_val: float, s: complex) -> complex:
    """Exact shadow zeta for affine sl_3:

    zeta_{sl_3,k}(s) = kappa * 2^{-s} + alpha * 3^{-s}

    where kappa = 4(k+3)/3, alpha = 6/(k+3).
    """
    kappa = 4.0 * (k_val + 3.0) / 3.0
    alpha = 6.0 / (k_val + 3.0)
    return kappa * 2.0 ** (-s) + alpha * 3.0 ** (-s)


# ============================================================================
# 17. Beta-gamma exact closed form
# ============================================================================

def betagamma_zeta_exact(lam_val: float, s: complex) -> complex:
    """Exact shadow zeta for beta-gamma at weight lambda.

    zeta_{bg}(s) = kappa * 2^{-s} + 2 * 3^{-s} + S_4 * 4^{-s}

    where kappa = 6*lambda^2 - 6*lambda + 1 and
    S_4 = 10/(c*(5c+22)) with c = 2(6*lambda^2 - 6*lambda + 1).

    Three nonzero terms (class C, tower terminates at arity 4).
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0
    S3 = 2.0
    if c_val != 0.0 and 5.0 * c_val + 22.0 != 0.0:
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    else:
        S4 = 0.0
    return kappa * 2.0 ** (-s) + S3 * 3.0 ** (-s) + S4 * 4.0 ** (-s)


# ============================================================================
# 18. Convergence analysis
# ============================================================================

def convergence_domain_analysis(
    shadow_coeffs: Dict[int, float],
    s_range: Tuple[float, float] = (-5.0, 15.0),
    n_points: int = 100,
) -> List[Tuple[float, float, bool]]:
    """Analyze the convergence domain of zeta_A(s) on the real line.

    For each s in [s_range[0], s_range[1]], compute partial sums at
    increasing truncation and check if they stabilize.

    Returns list of (s, value_at_max_truncation, converged_flag).
    """
    max_r = max(shadow_coeffs.keys())
    ds = (s_range[1] - s_range[0]) / n_points
    results = []

    for i in range(n_points + 1):
        s = s_range[0] + i * ds
        # Compute partial sums at multiple truncations
        vals = []
        for trunc in [max_r // 4, max_r // 2, 3 * max_r // 4, max_r]:
            if trunc < 2:
                trunc = 2
            val = shadow_zeta_numerical(shadow_coeffs, complex(s, 0), trunc)
            vals.append(val.real)

        # Check convergence: last two partial sums should agree
        if len(vals) >= 2 and vals[-1] != 0:
            rel_diff = abs(vals[-1] - vals[-2]) / (abs(vals[-1]) + 1e-300)
            converged = rel_diff < 1e-4
        else:
            converged = True  # Zero series

        results.append((s, vals[-1], converged))

    return results
