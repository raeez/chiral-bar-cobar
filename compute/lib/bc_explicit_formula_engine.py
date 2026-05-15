r"""Bar-cobar explicit formula engine for scalar shadow Dirichlet data.

This module computes scalar invariants of a shadow tower
``{S_r(A)}_{r >= 2}``.  It does not construct the bar coalgebra, the
Verdier/Koszul dual, the chiral derived centre, or a holographic package.

CLASSICAL ANALOGY
=================

In analytic number theory, the Chebyshev function psi(x) = sum_{n<=x} Lambda(n)
where Lambda(n) is the von Mangoldt function, defined by

    -zeta'(s)/zeta(s) = sum_{n=1}^{infty} Lambda(n) * n^{-s}.

The explicit formula (von Mangoldt) states:

    psi(x) = x - sum_{rho} x^rho / rho - log(2*pi) - (1/2)*log(1 - x^{-2})

where rho runs over the nontrivial zeros of zeta(s).

SHADOW ANALOGUE
===============

For a shadow tower with bare shadow Dirichlet series

    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s},

the logarithmic-derivative arithmetic is attached to the normalized
shadow L-function

    L_A(s) = 1 + zeta_A(s).

Define the shadow von Mangoldt function Lambda_A(r) by

    -L_A'(s) / L_A(s) = sum_{r >= 2} Lambda_A(r) * r^{-s}.

The coefficient recursion is the Dirichlet-algebra identity
``(Lambda_A * L_A)(r) = S_r log(r)`` with ``L_A(1)=1``:

    Lambda_A(r) = S_r * log(r) - sum_{d | r, 2 <= d < r} Lambda_A(d) * S_{r/d}

This is the shadow von Mangoldt recursion.

SHADOW COUNTING FUNCTIONS
=========================

1. psi_A(x) = sum_{r <= x} Lambda_A(r)    (shadow Chebyshev function)
2. pi_A(x) = #{r <= x : S_r(A) != 0}     (shadow prime counting function)

For class G (Heisenberg): pi_A(x) = 1 for x >= 2 (only r=2 contributes).
For class L (affine KM):  pi_A(x) = 2 for x >= 3.
For class C (beta-gamma): pi_A(x) = 3 for x >= 4.
For class M (Virasoro):   pi_A(x) ~ x (all arities contribute).

EXPLICIT FORMULA (SHADOW ANALOGUE)
===================================

The zero-sum routines are finite-window diagnostics for the normalized
L-function convention

    psi_A(x) = (principal term) - sum_{rho_sh} x^{rho_sh} / rho_sh
               + (lower order),

where rho_sh runs over zeros of L_A(s), not the bare zeta_A(s).

For finite towers, L_A is a finite Dirichlet polynomial.  It has no
general Riemann-style Euler product; zeros can occur in vertical
periodic families even in one-prime examples.  For class M, all
statements here are truncated scalar computations unless an external
analytic continuation theorem is supplied.

SHADOW CHEBYSHEV BIAS
=====================

The bias sum B_A(x) = sum_{r <= x} S_r(A) measures whether the shadow
tower is net positive or negative.  For Virasoro, the asymptotic sign
pattern S_r ~ rho^r r^{-5/2} cos(r*theta + phi) creates systematic
oscillations.

WEIL EXPLICIT FORMULA (SHADOW TRACE FORMULA)
=============================================

For a test function h with sufficient decay:

    sum_r Lambda_A(r) h(r) = (principal term) + sum_{rho_sh} hat{h}(rho_sh)

where hat{h} is the Fourier/Mellin transform of h evaluated at zeros.

CRAMER MODEL
=============

A finite-window variance model where the observed S_r are compared with
the Darboux asymptotics of the shadow quadratic form Q_L.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)

Normalization firewalls:
    * A, B(A), A^i=H^*(B(A)), A^!, and Z_ch^der(A) are distinct objects.
    * A^! is the Verdier/continuous-linear dual branch under finite-type
      or completed hypotheses.
    * Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
    * Z_ch^der(A) = ChirHoch^*(A,A) is the Hochschild/bulk object.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)
"""Seven entries of the holographic package."""


MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_br,T_br)",
    "R4_mod(L)",
)
"""Six primary projections of the modular Koszul compute package."""


TYPED_FIREWALL_OBJECTS: Tuple[str, ...] = (
    "A",
    "B(A)",
    "A^i",
    "A^!",
    "Omega(B(A))",
    "Z_ch^der(A)",
)


def bar_koszul_firewall_summary() -> Dict[str, str]:
    """Typed roles for the objects kept separate by this compute surface."""
    return {
        "A": "input chiral algebra",
        "B(A)": "ordered bar coalgebra before cohomology",
        "A^i": "bar cohomology coalgebra H^*(B(A))",
        "A^!": (
            "Verdier/continuous-linear dual branch under finite-type or "
            "completed hypotheses"
        ),
        "Omega(B(A))": "bar-cobar inversion recovering A",
        "Z_ch^der(A)": "ChirHoch^*(A,A), the Hochschild/derived-centre bulk",
    }


def kernel_normalization_constants(
    c: complex = 26,
    k: complex = 1,
    h_vee: complex = 2,
) -> Dict[str, Dict[str, Any]]:
    """Canonical collision and KZ normalizations used as firewalls."""
    return {
        "heisenberg_collision": {
            "formula": "k/z",
            "coefficient": k,
        },
        "affine_raw_collision": {
            "formula": "k*Omega_tr/z",
            "coefficient": k,
        },
        "affine_kz_coefficient": {
            "formula": "Omega/((k+h^vee)z)",
            "coefficient": 1 / (k + h_vee),
        },
        "virasoro_collision": {
            "formula": "(c/2)/z^3 + 2T/z",
            "central_coefficient": c / 2,
            "stress_coefficient": 2,
        },
    }


EXPLICIT_FORMULA_DIAGNOSTIC_SCOPE: Dict[str, Any] = {
    "surface": "scalar_shadow_dirichlet_projection",
    "zero_sum_is_certifying": False,
    "constructs_chiral_mc_theorem": False,
    "constructs_full_theta_A": False,
    "imports_riemann_selberg_arithmetic": False,
    "proves_analytic_continuation": False,
    "proves_functional_equation": False,
}
"""Scope flags shared by finite-window zero-sum and Weil diagnostics."""


def explicit_formula_diagnostic_scope() -> Dict[str, Any]:
    """Return the non-certifying scope of the scalar zero-sum diagnostics."""
    return dict(EXPLICIT_FORMULA_DIAGNOSTIC_SCOPE)


# ============================================================================
# 1.  Shadow coefficient providers (thin wrappers for self-containment)
# ============================================================================

def heisenberg_shadow_coefficients_exact(
    k_val: Union[int, Fraction],
    max_r: int = 50,
) -> Dict[int, Fraction]:
    """Exact Heisenberg coefficients: S_2=k and S_r=0 for r>=3."""
    k_frac = Fraction(k_val)
    result = {r: Fraction(0) for r in range(2, max_r + 1)}
    result[2] = k_frac
    return result


def affine_sl2_shadow_coefficients_exact(
    k_val: Union[int, Fraction],
    max_r: int = 50,
) -> Dict[int, Fraction]:
    r"""Exact affine sl_2 coefficients on the class-L line.

    The local canonical source is ``landscape_census.tex``:
    ``kappa(V_k(g)) = dim(g)(k+h^\vee)/(2h^\vee)``.  For ``sl_2``,
    ``dim(g)=3`` and ``h^\vee=2``, hence ``S_2=3(k+2)/4`` and
    ``S_3=4/(k+2)``.
    """
    k_frac = Fraction(k_val)
    if k_frac == -2:
        raise ValueError("affine sl_2 class-L coefficient S_3 has a pole at k=-2")
    result = {r: Fraction(0) for r in range(2, max_r + 1)}
    result[2] = Fraction(3) * (k_frac + 2) / 4
    result[3] = Fraction(4) / (k_frac + 2)
    return result


def virasoro_initial_shadow_coefficients_exact(
    c_val: Union[int, Fraction],
) -> Dict[str, Fraction]:
    r"""Exact Virasoro initial coefficients from the canonical census.

    On the non-singular surface ``c(5c+22) != 0``:
    ``S_2=c/2``, ``S_3=2``, ``S_4=10/(c(5c+22))``,
    ``S_5=-48/(c^2(5c+22))``, and
    ``Delta=8*kappa*S_4=40/(5c+22)``.
    """
    c_frac = Fraction(c_val)
    if c_frac == 0 or 5 * c_frac + 22 == 0:
        raise ValueError(f"Virasoro shadow undefined at c={c_frac}")
    return {
        "S2": c_frac / 2,
        "S3": Fraction(2),
        "S4": Fraction(10, 1) / (c_frac * (5 * c_frac + 22)),
        "S5": Fraction(-48, 1) / (c_frac * c_frac * (5 * c_frac + 22)),
        "Delta": Fraction(40, 1) / (5 * c_frac + 22),
    }


def heisenberg_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Heisenberg H_k.  Class G: only S_2 = k."""
    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = float(k_val)
    return result


def affine_sl2_shadow_coefficients(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for affine V_k(sl_2).  Class L: S_2, S_3 nonzero."""
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = kappa
    result[3] = alpha
    return result


def betagamma_shadow_coefficients(lam_val: float = 0.5, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for beta-gamma.  Class C: S_2, S_3, S_4 nonzero.

    For the global shadow (stratum separation terminates at arity 4):
    S_2 = kappa, S_3 = alpha (from Virasoro sub), S_4 = quartic contact.
    On the T-line: S_3 != 0 generically.
    """
    c_val = 2.0 * (6.0 * lam_val ** 2 - 6.0 * lam_val + 1.0)
    kappa = c_val / 2.0
    # Use Virasoro-line data for the T-line restriction
    if abs(c_val) < 1e-15 or abs(5.0 * c_val + 22.0) < 1e-15:
        S4 = 0.0
    else:
        S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    result = {r: 0.0 for r in range(2, max_r + 1)}
    result[2] = kappa
    result[3] = 2.0  # universal gravitational cubic on the Virasoro/T-line
    result[4] = S4
    return result


def virasoro_shadow_coefficients(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Shadow coefficients for Virasoro Vir_c via convolution recursion.

    H(t) = t^2 * sqrt(Q_L(t)), Q_L(t) = c^2 + 12c*t + alpha(c)*t^2,
    alpha(c) = (180c + 872) / (5c + 22).

    S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).
    """
    if abs(c_val) < 1e-15 or abs(5.0 * c_val + 22.0) < 1e-15:
        raise ValueError(f"Virasoro shadow undefined at c={c_val}")

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / (5.0 * c_val + 22.0)

    # Algebraic branch fixed by the canonical initial condition S_2=c/2.
    a0 = c_val
    a = [a0]

    if max_r >= 3:
        a.append(q1 / (2.0 * a0))
    if max_r >= 4:
        a.append((q2 - a[1] ** 2) / (2.0 * a0))
    for n in range(3, max_r - 2 + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a.append(-conv / (2.0 * a0))

    result = {r: 0.0 for r in range(2, max_r + 1)}
    for n in range(len(a)):
        r = n + 2
        if r <= max_r:
            result[r] = a[n] / float(r)
    return result


def virasoro_growth_rate(c_val: float) -> float:
    """Exact shadow growth rate for Virasoro: rho = sqrt((180c+872)/((5c+22)*c^2))."""
    numer = 180.0 * c_val + 872.0
    denom = (5.0 * c_val + 22.0) * c_val ** 2
    if denom <= 0:
        return float('inf')
    return math.sqrt(numer / denom)


# ============================================================================
# 2.  Shadow von Mangoldt function
# ============================================================================

def shadow_von_mangoldt(shadow_coeffs: Dict[int, float],
                        max_r: Optional[int] = None) -> Dict[int, float]:
    r"""Compute the shadow von Mangoldt function Lambda_A(r).

    Define ``L_A(s) = 1 + sum_{r>=2} S_r r^{-s}``.
    Then -L_A'/L_A = sum_{r>=2} Lambda_A(r) r^{-s} where

        Lambda_A(r) = S_r * log(r) - sum_{d | r, 2 <= d < r, r/d >= 2} Lambda_A(d) * S_{r/d}

    This is the Dirichlet-series inversion for the normalized
    log derivative.

    Returns dict {r: Lambda_A(r)} for r = 2, ..., max_r.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    Lambda = {}
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        # Main term: S_r * log(r)
        val = Sr * math.log(r)
        # Subtract contributions from proper divisors
        for d in range(2, r):
            if r % d != 0:
                continue
            q = r // d
            if q < 2:
                continue
            Sq = shadow_coeffs.get(q, 0.0)
            val -= Lambda.get(d, 0.0) * Sq
        Lambda[r] = val
    return Lambda


def shadow_von_mangoldt_from_log_derivative(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Compute Lambda_A(r) by the Dirichlet-inverse log-derivative formula.

    Let ``a_1=1`` and ``a_r=S_r`` for ``r>=2``.  If
    ``b_r=S_r log(r)`` and ``a^{-1}`` is the Dirichlet inverse of ``a``, then

        Lambda_A = b * a^{-1}.

    This is the coefficient form of ``-L_A'/L_A`` and gives an alternative
    implementation to the forward recursion in :func:`shadow_von_mangoldt`.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    a = {1: 1.0}
    for r in range(2, max_r + 1):
        a[r] = shadow_coeffs.get(r, 0.0)

    a_inv = {1: 1.0}
    for n in range(2, max_r + 1):
        total = 0.0
        for d in range(2, n + 1):
            if n % d == 0:
                total += a.get(d, 0.0) * a_inv.get(n // d, 0.0)
        a_inv[n] = -total

    Lambda = {}
    for n in range(2, max_r + 1):
        val = 0.0
        for d in range(2, n + 1):
            if n % d != 0:
                continue
            Sd = shadow_coeffs.get(d, 0.0)
            if abs(Sd) < 1e-300:
                continue
            val += Sd * math.log(d) * a_inv.get(n // d, 0.0)
        Lambda[n] = val
    return Lambda


# ============================================================================
# 3.  Shadow Chebyshev counting function psi_A(x)
# ============================================================================

def shadow_chebyshev_psi(shadow_coeffs: Dict[int, float],
                         x: float,
                         max_r: Optional[int] = None) -> float:
    r"""Shadow Chebyshev function psi_A(x) = sum_{r <= x} Lambda_A(r).

    Verification path 1: direct summation from definition.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    return sum(Lambda.get(r, 0.0) for r in range(2, int(x) + 1) if r <= max_r)


def shadow_chebyshev_psi_table(shadow_coeffs: Dict[int, float],
                               x_values: List[float],
                               max_r: Optional[int] = None) -> Dict[float, float]:
    """Compute psi_A(x) for a list of x values."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    result = {}
    for x in x_values:
        result[x] = sum(Lambda.get(r, 0.0) for r in range(2, int(x) + 1) if r <= max_r)
    return result


# ============================================================================
# 4.  Shadow prime counting function pi_A(x)
# ============================================================================

def shadow_prime_counting(shadow_coeffs: Dict[int, float],
                          x: float,
                          threshold: float = 1e-15) -> int:
    r"""Shadow prime counting function pi_A(x) = #{r <= x : S_r(A) != 0}.

    Counts arities at which the shadow is nonvanishing.

    Class G (Heisenberg): pi_A(x) = 1 for x >= 2.
    Class L (affine KM):  pi_A(x) = 2 for x >= 3.
    Class C (beta-gamma): pi_A(x) depends on line.
    Class M (Virasoro):   pi_A(x) = x - 1 for x >= 2 (all arities).
    """
    count = 0
    for r in range(2, int(x) + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > threshold:
            count += 1
    return count


def shadow_prime_counting_table(shadow_coeffs: Dict[int, float],
                                x_values: List[float],
                                threshold: float = 1e-15) -> Dict[float, int]:
    """Compute pi_A(x) for a list of x values."""
    return {x: shadow_prime_counting(shadow_coeffs, x, threshold) for x in x_values}


def shadow_active_arities(shadow_coeffs: Dict[int, float],
                          max_r: Optional[int] = None,
                          threshold: float = 1e-15) -> List[int]:
    """Return the list of arities r where S_r != 0 (the shadow 'primes')."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    return [r for r in range(2, max_r + 1)
            if abs(shadow_coeffs.get(r, 0.0)) > threshold]


# ============================================================================
# 5.  Shadow zeta zeros (for finite towers: exact; for class M: numerical)
# ============================================================================

def shadow_zeta_value(shadow_coeffs: Dict[int, float],
                      s: complex,
                      max_r: Optional[int] = None) -> complex:
    """Evaluate the bare shadow zeta_A(s) = sum_{r >= 2} S_r r^{-s}."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * r ** (-s)
    return total


def shadow_zeta_derivative(shadow_coeffs: Dict[int, float],
                           s: complex,
                           max_r: Optional[int] = None) -> complex:
    """Evaluate the bare derivative zeta_A'(s)."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += -Sr * math.log(r) * r ** (-s)
    return total


def shadow_l_function_value(shadow_coeffs: Dict[int, float],
                            s: complex,
                            max_r: Optional[int] = None) -> complex:
    """Evaluate L_A(s) = 1 + zeta_A(s)."""
    return 1.0 + shadow_zeta_value(shadow_coeffs, s, max_r)


def shadow_l_function_derivative(shadow_coeffs: Dict[int, float],
                                 s: complex,
                                 max_r: Optional[int] = None) -> complex:
    """Evaluate L_A'(s); the constant term has derivative zero."""
    return shadow_zeta_derivative(shadow_coeffs, s, max_r)


def shadow_log_derivative(shadow_coeffs: Dict[int, float],
                          s: complex,
                          max_r: Optional[int] = None) -> complex:
    """Evaluate -L_A'(s)/L_A(s) = sum Lambda_A(r) r^{-s}."""
    l_val = shadow_l_function_value(shadow_coeffs, s, max_r)
    l_prime = shadow_l_function_derivative(shadow_coeffs, s, max_r)
    if abs(l_val) < 1e-300:
        return complex(float('nan'), float('nan'))
    return -l_prime / l_val


def find_shadow_zeros_on_line(shadow_coeffs: Dict[int, float],
                              sigma: float,
                              t_range: Tuple[float, float] = (0.1, 100.0),
                              n_points: int = 5000,
                              max_r: Optional[int] = None) -> List[complex]:
    r"""Find approximate zeros of L_A(sigma + it) by sign-change detection.

    Scans the line Re(s) = sigma for zeros of the normalized shadow
    L-function by detecting sign changes in the real and imaginary parts.

    Returns list of approximate zeros sigma + i*t.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    t_lo, t_hi = t_range
    dt = (t_hi - t_lo) / n_points

    zeros = []
    prev_val = shadow_l_function_value(shadow_coeffs, complex(sigma, t_lo), max_r)
    for i in range(1, n_points + 1):
        t = t_lo + i * dt
        val = shadow_l_function_value(shadow_coeffs, complex(sigma, t), max_r)
        # Detect zero: both real and imaginary parts near zero,
        # or sign change in real part with small imaginary part
        if (prev_val.real * val.real < 0 and
                abs(val.imag) < abs(val.real) + abs(prev_val.real)):
            # Refine by bisection
            t_a, t_b = t - dt, t
            for _ in range(30):
                t_mid = (t_a + t_b) / 2
                v_mid = shadow_l_function_value(shadow_coeffs, complex(sigma, t_mid), max_r)
                if v_mid.real * shadow_l_function_value(
                        shadow_coeffs, complex(sigma, t_a), max_r).real < 0:
                    t_b = t_mid
                else:
                    t_a = t_mid
            zeros.append(complex(sigma, (t_a + t_b) / 2))
        prev_val = val
    return zeros


def find_shadow_zeros_general(shadow_coeffs: Dict[int, float],
                              sigma_range: Tuple[float, float] = (-1.0, 5.0),
                              t_range: Tuple[float, float] = (0.1, 50.0),
                              n_sigma: int = 20,
                              n_t: int = 2000,
                              max_r: Optional[int] = None) -> List[complex]:
    """Find zeros of L_A in a rectangular region of the complex plane.

    Uses grid search followed by Newton refinement.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    zeros = []
    d_sigma = (sigma_range[1] - sigma_range[0]) / n_sigma
    d_t = (t_range[1] - t_range[0]) / n_t

    for i in range(n_sigma + 1):
        sigma = sigma_range[0] + i * d_sigma
        new_zeros = find_shadow_zeros_on_line(
            shadow_coeffs, sigma, t_range, n_t, max_r)
        zeros.extend(new_zeros)

    # Deduplicate (merge zeros within tolerance)
    unique = []
    for z in sorted(zeros, key=lambda w: (w.real, w.imag)):
        if not any(abs(z - u) < 0.1 for u in unique):
            unique.append(z)
    return unique


def refine_zero_newton(shadow_coeffs: Dict[int, float],
                       s0: complex,
                       max_iter: int = 50,
                       tol: float = 1e-12,
                       max_r: Optional[int] = None) -> complex:
    """Refine a zero of L_A by Newton's method: s_{n+1} = s_n - L/L'."""
    s = s0
    for _ in range(max_iter):
        z = shadow_l_function_value(shadow_coeffs, s, max_r)
        zp = shadow_l_function_derivative(shadow_coeffs, s, max_r)
        if abs(zp) < 1e-300:
            break
        ds = z / zp
        s = s - ds
        if abs(ds) < tol:
            break
    return s


# ============================================================================
# 6.  Explicit formula: psi_A(x) from zeros
# ============================================================================

def explicit_formula_from_zeros(
    shadow_coeffs: Dict[int, float],
    x: float,
    zeros: List[complex],
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Compute a finite-window zero-sum diagnostic for psi_A(x).

    The intended normalized convention is

        psi_A(x) = (principal term) - sum_{rho} x^{rho} / rho
                   + (lower order),

    where rho runs over zeros of L_A(s)=1+zeta_A(s).  This routine is a
    residual-fit diagnostic.  It does not prove analytic continuation,
    a functional equation, or any chiral Maurer--Cartan theorem.

    Returns dict with:
        'psi_direct': direct computation of psi_A(x)
        'zero_sum': paired sum x^rho/rho over supplied zeros
        'signed_zero_term': the term -sum x^rho/rho in the displayed formula
        'main_term': residual fitted after seeing psi_direct and zero_sum
        'error': residual-fit closure error
        'zero_contributions': list of individual x^rho / rho terms
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    # Direct computation (path 1)
    psi_direct = shadow_chebyshev_psi(shadow_coeffs, x, max_r)

    # Zero sum (path 2)
    zero_contributions = []
    zero_sum = 0.0 + 0.0j
    for rho in zeros:
        if abs(rho) < 1e-15:
            continue
        term = x ** rho / rho
        zero_contributions.append((rho, term))
        zero_sum += term
    # Include conjugate zeros (zeros come in conjugate pairs for real coefficients)
    conj_sum = 0.0
    for rho, term in zero_contributions:
        if rho.imag > 0.01:
            # The pair (rho, conj(rho)) contributes x^rho/rho + x^{conj(rho)}/conj(rho)
            # = 2 * Re(x^rho / rho)
            conj_sum += 2.0 * (x ** rho / rho).real
        elif abs(rho.imag) <= 0.01:
            # Real zero
            conj_sum += (x ** rho / rho).real

    main_term = psi_direct + conj_sum
    signed_zero_term = -conj_sum
    reconstruction = main_term + signed_zero_term

    error = abs(psi_direct - reconstruction)

    result = {
        'psi_direct': psi_direct,
        'zero_sum': conj_sum,
        'signed_zero_term': signed_zero_term,
        'main_term': main_term,
        'residual_principal_term': main_term,
        'reconstruction': reconstruction,
        'error': error,
        'zero_contributions': zero_contributions,
        'main_term_is_residual_fit': True,
        'certifies_explicit_formula': False,
    }
    result.update(explicit_formula_diagnostic_scope())
    return result


def explicit_formula_error(
    shadow_coeffs: Dict[int, float],
    x_values: List[float],
    zeros: List[complex],
    max_r: Optional[int] = None,
) -> Dict[float, float]:
    """Compute the zero-only residual ``|psi_direct + sum x^rho/rho|``.

    No principal term is supplied, so these values are finite-window
    diagnostics rather than explicit-formula errors in the analytic sense.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    errors = {}
    for x in x_values:
        psi_direct = sum(Lambda.get(r, 0.0) for r in range(2, int(x) + 1) if r <= max_r)
        # Zeros contribution (using conjugate pairs)
        zero_sum = 0.0
        for rho in zeros:
            if abs(rho) < 1e-15:
                continue
            if rho.imag > 0.01:
                zero_sum += 2.0 * (x ** rho / rho).real
            elif abs(rho.imag) <= 0.01:
                zero_sum += (x ** rho / rho).real
        errors[x] = abs(psi_direct + zero_sum)
    return errors


# ============================================================================
# 7.  Inverse Mellin verification path
# ============================================================================

def psi_from_inverse_mellin(shadow_coeffs: Dict[int, float],
                            x: float,
                            sigma: float = 3.0,
                            T: float = 100.0,
                            n_points: int = 5000,
                            max_r: Optional[int] = None) -> float:
    r"""Compute psi_A(x) via the inverse Mellin transform of -L_A'/L_A.

    psi_A(x) = (1/2pi i) * integral_{sigma - iT}^{sigma + iT}
                              [-L_A'(s)/L_A(s)] * x^s / s ds

    Verification path 2: independent of the recursive von Mangoldt computation.

    Uses trapezoidal quadrature on the vertical line Re(s) = sigma.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    dt = 2 * T / n_points
    integral = 0.0 + 0.0j

    for i in range(n_points + 1):
        t = -T + i * dt
        s = complex(sigma, t)
        # -L'/L
        log_deriv = shadow_log_derivative(shadow_coeffs, s, max_r)
        if math.isnan(log_deriv.real) or math.isnan(log_deriv.imag):
            continue
        # x^s / s
        if abs(s) < 1e-15:
            continue
        integrand = log_deriv * x ** s / s
        # Trapezoidal weight
        w = dt if 0 < i < n_points else dt / 2
        integral += integrand * w

    # Factor: 1/(2*pi*i)
    result = integral / (2.0 * math.pi * 1j)
    return result.real


# ============================================================================
# 8.  Shadow Chebyshev bias
# ============================================================================

def shadow_bias_sum(shadow_coeffs: Dict[int, float],
                    x: float,
                    max_r: Optional[int] = None) -> float:
    r"""Shadow Chebyshev bias: B_A(x) = sum_{r <= x} S_r(A).

    Measures whether the shadow tower is net positive or negative up to arity x.

    For Virasoro: the asymptotic sign pattern is S_r ~ rho^r r^{-5/2} cos(r*theta + phi),
    so the bias oscillates with period 2*pi/theta.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    return sum(shadow_coeffs.get(r, 0.0) for r in range(2, min(int(x) + 1, max_r + 1)))


def shadow_bias_table(shadow_coeffs: Dict[int, float],
                      x_values: List[float],
                      max_r: Optional[int] = None) -> Dict[float, float]:
    """Compute B_A(x) for a list of x values."""
    return {x: shadow_bias_sum(shadow_coeffs, x, max_r) for x in x_values}


def shadow_sign_changes(shadow_coeffs: Dict[int, float],
                        max_r: Optional[int] = None,
                        threshold: float = 1e-15) -> List[int]:
    """Find arities at which S_r changes sign.

    Returns list of arities r where S_r * S_{r-1} < 0.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    changes = []
    prev_sign = 0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < threshold:
            continue
        curr_sign = 1 if Sr > 0 else -1
        if prev_sign != 0 and curr_sign != prev_sign:
            changes.append(r)
        prev_sign = curr_sign
    return changes


def shadow_bias_positive_density(shadow_coeffs: Dict[int, float],
                                 max_r: Optional[int] = None,
                                 threshold: float = 1e-15) -> float:
    """Fraction of arities r in [2, max_r] where S_r > 0.

    For a balanced tower with cos(r*theta) oscillation: density ~ 1/2.
    For Heisenberg (S_2 = k > 0 only): density = 1/(max_r - 1).
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    positive = 0
    total = 0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > threshold:
            total += 1
            if Sr > 0:
                positive += 1
    if total == 0:
        return 0.0
    return positive / total


# ============================================================================
# 9.  Shadow Chebyshev slope estimator
# ============================================================================

def shadow_pnt_constant(shadow_coeffs: Dict[int, float],
                        max_r: Optional[int] = None) -> float:
    r"""Estimate the finite-window Chebyshev slope psi_A(max_r)/max_r.

    For finite towers this returns 0 because psi_A is eventually constant.
    For dense class-M truncations this returns only the observed terminal
    slope; it is not an asymptotic prime-number-theorem constant without
    an analytic continuation and pole theorem for L_A.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)

    # Check if tower is finite
    active = [r for r in range(2, max_r + 1)
              if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]
    if len(active) < max_r * 0.5:
        return 0.0  # Finite tower

    # For dense towers, report the observed terminal ratio psi(x)/x.
    psi_val = sum(Lambda.get(r, 0.0) for r in range(2, max_r + 1))
    if max_r > 2:
        return psi_val / max_r
    return 0.0


def shadow_pnt_ratio_table(shadow_coeffs: Dict[int, float],
                           x_values: List[float],
                           max_r: Optional[int] = None) -> Dict[float, float]:
    """Compute finite-window ratios psi_A(x) / x for a list of x values."""
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    result = {}
    for x in x_values:
        psi_val = sum(Lambda.get(r, 0.0) for r in range(2, int(x) + 1) if r <= max_r)
        result[x] = psi_val / x if x > 0 else 0.0
    return result


# ============================================================================
# 10. Weil explicit formula (shadow trace formula)
# ============================================================================

def weil_explicit_formula(
    shadow_coeffs: Dict[int, float],
    test_fn: Callable[[float], float],
    zeros: List[complex],
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Finite-window shadow Weil diagnostic.

    For a test function h:

        sum_{r >= 2} Lambda_A(r) h(r) = (principal) + sum_{rho} hat_h(rho)

    where hat_h(rho) = sum_{r >= 2} h(r) r^{-rho} (the Mellin-type transform).

    The principal term is the residual after the supplied zeros of L_A are
    paired with the arithmetic side.  Thus the returned equality is a
    finite-window decomposition, not a trace formula theorem.

    Returns dict with:
        'sum_side': sum Lambda_A(r) h(r)
        'spectral_side': sum_rho hat_h(rho)
        'principal': estimated principal term
        'error': |sum_side - (principal + spectral_side)|
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)

    # Arithmetic side: sum Lambda_A(r) h(r)
    sum_side = 0.0
    for r in range(2, max_r + 1):
        sum_side += Lambda.get(r, 0.0) * test_fn(float(r))

    # Spectral side: sum_rho hat_h(rho)
    spectral_sum = 0.0
    for rho in zeros:
        if abs(rho) < 1e-15:
            continue
        # hat_h(rho) = sum_r h(r) r^{-rho}
        hat_h = 0.0 + 0.0j
        for r in range(2, max_r + 1):
            hat_h += test_fn(float(r)) * r ** (-rho)
        if rho.imag > 0.01:
            spectral_sum += 2.0 * hat_h.real
        elif abs(rho.imag) <= 0.01:
            spectral_sum += hat_h.real

    principal = sum_side - spectral_sum
    error = abs(sum_side - (principal + spectral_sum))

    result = {
        'sum_side': sum_side,
        'spectral_side': spectral_sum,
        'principal': principal,
        'principal_is_residual_fit': True,
        'error': error,
        'certifies_weil_formula': False,
    }
    result.update(explicit_formula_diagnostic_scope())
    return result


# ============================================================================
# 11. Cramer model: shadow variance
# ============================================================================

def shadow_variance_from_quadratic(kappa: float, alpha: float, S4: float) -> float:
    r"""Variance parameter from the shadow quadratic form Q_L.

    Q_L(t) = (2*kappa)^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S4)*t^2

    The variance of S_r (in the Cramer model) is related to the spread
    of the quadratic form.  For the single-line shadow:

        Var(S_r) ~ (rho^{2r}) * r^{-5} * (1/2)

    The Cramer constant sigma^2 is:
        sigma^2 = lim_{r -> inf} r^5 * |S_r|^2 / rho^{2r}

    From the asymptotic expansion S_r ~ C * rho^r * r^{-5/2} * cos(r*theta + phi):
        sigma^2 = C^2 / 2  (average of cos^2)

    The amplitude C depends on the residue of sqrt(Q_L) at the branch point.
    For Virasoro: C = |c| * sqrt(2 / (pi * |t_0|)) where t_0 is the branch point.
    """
    # Critical discriminant
    Delta = 8.0 * kappa * S4

    # Branch point modulus = 2|kappa| / sqrt(9*alpha^2 + 2*Delta)
    denom = 9.0 * alpha ** 2 + 2.0 * Delta
    if denom <= 0 or abs(kappa) < 1e-15:
        return 0.0

    t0_mod = 2.0 * abs(kappa) / math.sqrt(denom)

    # Amplitude from the Darboux theorem for algebraic singularities:
    # sqrt(Q_L) ~ A * (1 - t/t_0)^{1/2} near t_0
    # The coefficient of t^n in the Taylor expansion of (1-t/t_0)^{1/2}
    # decays as (1/t_0^n) * n^{-3/2} / Gamma(-1/2)
    # But S_r = a_{r-2}/r where a_n are Taylor coefficients of sqrt(Q_L),
    # so S_r ~ A * (1/t_0)^{r-2} * (r-2)^{-3/2} / (Gamma(-1/2) * r)
    # ~ A * rho^r * r^{-5/2} / Gamma(-1/2)  where rho = 1/t_0

    # The constant C^2 / 2:
    # C = A * t_0^2 / |Gamma(-1/2)| = A * t_0^2 * sqrt(pi) / 2
    # where A = sqrt(Q_L(0)) * sqrt(2 / (pi * t_0_mod)) or similar

    # Direct: sigma^2 from the Gaussian average over the oscillation
    rho = 1.0 / t0_mod if t0_mod > 0 else 0.0
    if rho <= 0:
        return 0.0

    # C from the generating function residue:
    # sqrt(Q_L) ~ sqrt(-q2) * sqrt(t_0 - t) * sqrt(t_0_conj - t) near t_0
    # The leading singularity has coefficient related to sqrt(-q2 * (t_0_conj - t_0))
    q2 = 9.0 * alpha ** 2 + 16.0 * kappa * S4
    if q2 == 0:
        return 0.0

    # Residue calculation: near t = t_0 (branch point), sqrt(Q_L(t)) has
    # a square-root singularity.  Darboux's theorem gives:
    # a_n ~ [coefficient] * rho^n * n^{-3/2} / Gamma(-1/2)
    # = [coefficient] * rho^n * n^{-3/2} * (-2/sqrt(pi))
    # So C = |coefficient| * 2 / sqrt(pi)
    # sigma^2 = C^2 / 2

    # For a practical estimate, compute from the explicit coefficients
    return rho ** 2  # First approximation: sigma^2 ~ rho^2


def cramer_variance_from_coefficients(shadow_coeffs: Dict[int, float],
                                      min_r: int = 10,
                                      max_r: Optional[int] = None) -> float:
    r"""Estimate the Cramer constant sigma^2 from explicit shadow coefficients.

    sigma^2 = lim_{r -> inf} r^5 * |S_r|^2 / rho^{2r}

    Uses the ratio test on the last few terms.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    # Estimate rho
    ratios = []
    for r in range(max(min_r, 5), max_r):
        Sr = shadow_coeffs.get(r, 0.0)
        Sr1 = shadow_coeffs.get(r + 1, 0.0)
        if abs(Sr) > 1e-200 and abs(Sr1) > 1e-200:
            ratios.append(abs(Sr1 / Sr))
    if not ratios:
        return 0.0
    rho = ratios[-1]
    if rho < 1e-15:
        return 0.0

    # Compute r^5 * |S_r|^2 / rho^{2r} for the last few terms
    estimates = []
    for r in range(max(min_r, 10), max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) > 1e-200:
            val = r ** 5 * Sr ** 2 / rho ** (2 * r)
            estimates.append(val)

    if not estimates:
        return 0.0
    # Return the average of the last few
    return sum(estimates[-5:]) / len(estimates[-5:])


def cramer_predicted_psi(x: float, C_pnt: float) -> float:
    """Cramer model prediction: psi_A(x) ~ C * x."""
    return C_pnt * x


# ============================================================================
# 12. Parseval identity: shadow primes vs zeros
# ============================================================================

def parseval_identity_check(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    sigma: float = 3.0,
    max_r: Optional[int] = None,
) -> Dict[str, float]:
    r"""Check a finite-window Parseval identity for the bare shadow zeta.

    For the shadow zeta function, the Parseval relation on the line Re(s)=sigma:

        sum_{r >= 2} |S_r|^2 * r^{-2*sigma}
            = (1/2pi) * integral |zeta_A(sigma + it)|^2 dt

    Also records the squared normalized log-derivative coefficient sum
    ``sum |Lambda_A(r)|^2 r^{-2*sigma}``.

    Returns:
        'coefficient_sum': sum |S_r|^2 r^{-2 sigma}
        'von_mangoldt_sum': sum |Lambda_A(r)|^2 r^{-2 sigma}
        'zeta_L2_estimate': numerical estimate of (1/2pi) int |zeta|^2 dt
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)

    coeff_sum = sum(shadow_coeffs.get(r, 0.0) ** 2 * r ** (-2 * sigma)
                    for r in range(2, max_r + 1))
    vm_sum = sum(Lambda.get(r, 0.0) ** 2 * r ** (-2 * sigma)
                 for r in range(2, max_r + 1))

    # Numerical L^2 integral estimate
    T = 50.0
    n_pts = 2000
    dt = 2 * T / n_pts
    L2_integral = 0.0
    for i in range(n_pts + 1):
        t = -T + i * dt
        z = shadow_zeta_value(shadow_coeffs, complex(sigma, t), max_r)
        w = dt if 0 < i < n_pts else dt / 2
        L2_integral += abs(z) ** 2 * w
    L2_estimate = L2_integral / (2 * math.pi)

    return {
        'coefficient_sum': coeff_sum,
        'von_mangoldt_sum': vm_sum,
        'zeta_L2_estimate': L2_estimate,
    }


# ============================================================================
# 13. Heisenberg exact formulas (complete verification benchmark)
# ============================================================================

def heisenberg_von_mangoldt_exact(k_val: float, r: int) -> float:
    r"""Exact shadow von Mangoldt for Heisenberg.

    The normalized shadow L-function is L_A(s) = 1 + k * 2^{-s}.  Hence

        -L_A'/L_A = k * log(2) * 2^{-s} / (1 + k * 2^{-s}).

    Expanding as a geometric series (for |k * 2^{-s}| < 1, i.e., Re(s) > log(k)/log(2)):
        -L'/L = k * log(2) * 2^{-s} * sum_{n=0}^inf (-k)^n * 2^{-ns}
              = sum_{n=1}^inf (-1)^{n+1} * k^n * log(2) * 2^{-ns}

    So Lambda(2^n) = (-1)^{n+1} * k^n * log(2) for n >= 1,
    and Lambda(r) = 0 if r is not a power of 2.

    The same coefficients follow from the recursion with L_A(1)=1:
    Lambda(2) = S_2 * log(2) = k * log(2).
    Lambda(4) = S_4 * log(4) - Lambda(2) * S_2 = 0 - k * log(2) * k = -k^2 * log(2).
    Lambda(8) = S_8 * log(8) - Lambda(2)*S_4 - Lambda(4)*S_2
              = 0 - 0 - (-k^2 log(2)) * k = k^3 * log(2).

    So Lambda(2^n) = (-1)^{n+1} * k^n * log(2), confirming the geometric series.

    At non-powers-of-2: Lambda(r) = 0.
    """
    if r < 2:
        return 0.0
    # Check if r is a power of 2
    n = 0
    temp = r
    while temp > 1:
        if temp % 2 != 0:
            return 0.0
        temp //= 2
        n += 1
    # r = 2^n
    return (-1.0) ** (n + 1) * k_val ** n * math.log(2.0)


def heisenberg_psi_exact(k_val: float, x: float) -> float:
    r"""Exact psi_{H_k}(x) = sum_{2^n <= x} (-1)^{n+1} k^n log(2).

    = log(2) * sum_{n=1}^{floor(log2(x))} (-k)^{n-1} * k
    = k * log(2) * sum_{n=0}^{N-1} (-k)^n     where N = floor(log2(x))
    = k * log(2) * (1 - (-k)^N) / (1 + k)     for k != -1
    """
    if x < 2:
        return 0.0
    N = int(math.log2(x))
    if N < 1:
        return 0.0
    total = 0.0
    for n in range(1, N + 1):
        total += (-1.0) ** (n + 1) * k_val ** n * math.log(2.0)
    return total


def heisenberg_bias_exact(k_val: float, x: float) -> float:
    """Exact bias B_{H_k}(x) = k if x >= 2, else 0."""
    if x >= 2:
        return k_val
    return 0.0


# ============================================================================
# 14. Affine sl_2 exact formulas
# ============================================================================

def affine_sl2_von_mangoldt_exact(k_val: float, r: int) -> float:
    r"""Exact shadow von Mangoldt for affine sl_2.

    L_A(s) = 1 + kappa * 2^{-s} + alpha * 3^{-s}.

    From the recursion:
        Lambda(2) = S_2 * log(2) = kappa * log(2)
        Lambda(3) = S_3 * log(3) = alpha * log(3)
        Lambda(4) = S_4 * log(4) - Lambda(2)*S_2 = 0 - kappa^2 * log(2)
                  = -kappa^2 * log(2)
        Lambda(5) = 0 (S_5 = 0, no proper divisors d with S_{5/d} != 0)
        Lambda(6) = S_6 * log(6) - Lambda(2)*S_3 - Lambda(3)*S_2
                  = 0 - kappa*alpha*log(2) - kappa*alpha*log(3)
                  = -kappa*alpha*(log(2) + log(3)) = -kappa*alpha*log(6)
    """
    h_dual = 2.0
    dim_g = 3.0
    kappa = dim_g * (k_val + h_dual) / (2.0 * h_dual)
    alpha = 2.0 * h_dual / (k_val + h_dual)
    coeffs = affine_sl2_shadow_coefficients(k_val, max(r, 10))
    Lambda = shadow_von_mangoldt(coeffs, max(r, 10))
    return Lambda.get(r, 0.0)


# ============================================================================
# 15. Full landscape explicit formula data
# ============================================================================

@dataclass
class ExplicitFormulaData:
    """Scalar explicit-formula diagnostics for one shadow tower."""
    name: str
    shadow_class: str
    shadow_coeffs: Dict[int, float]
    von_mangoldt: Dict[int, float]
    psi_table: Dict[float, float]
    pi_table: Dict[float, int]
    bias_table: Dict[float, float]
    active_arities: List[int]
    pnt_constant: float
    sign_changes: List[int]
    positive_density: float


def compute_explicit_formula_data(
    name: str,
    shadow_class: str,
    shadow_coeffs: Dict[int, float],
    x_values: Optional[List[float]] = None,
) -> ExplicitFormulaData:
    """Compute scalar explicit-formula diagnostics for one shadow tower."""
    max_r = max(shadow_coeffs.keys())
    if x_values is None:
        x_values = [float(x) for x in range(2, min(max_r + 1, 52))]

    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    psi = shadow_chebyshev_psi_table(shadow_coeffs, x_values, max_r)
    pi_tbl = shadow_prime_counting_table(shadow_coeffs, x_values)
    bias = shadow_bias_table(shadow_coeffs, x_values, max_r)
    active = shadow_active_arities(shadow_coeffs, max_r)
    C_pnt = shadow_pnt_constant(shadow_coeffs, max_r)
    sc = shadow_sign_changes(shadow_coeffs, max_r)
    pd = shadow_bias_positive_density(shadow_coeffs, max_r)

    return ExplicitFormulaData(
        name=name,
        shadow_class=shadow_class,
        shadow_coeffs=shadow_coeffs,
        von_mangoldt=Lambda,
        psi_table=psi,
        pi_table=pi_tbl,
        bias_table=bias,
        active_arities=active,
        pnt_constant=C_pnt,
        sign_changes=sc,
        positive_density=pd,
    )


def compute_full_landscape_data(max_r: int = 30) -> Dict[str, ExplicitFormulaData]:
    """Compute explicit formula data for the standard landscape."""
    landscape = {}

    # Heisenberg k=1
    coeffs = heisenberg_shadow_coefficients(1.0, max_r)
    landscape['Heis_k=1'] = compute_explicit_formula_data('Heis_k=1', 'G', coeffs)

    # Heisenberg k=2
    coeffs = heisenberg_shadow_coefficients(2.0, max_r)
    landscape['Heis_k=2'] = compute_explicit_formula_data('Heis_k=2', 'G', coeffs)

    # Affine sl_2 at k=1
    coeffs = affine_sl2_shadow_coefficients(1.0, max_r)
    landscape['aff_sl2_k=1'] = compute_explicit_formula_data('aff_sl2_k=1', 'L', coeffs)

    # Beta-gamma at lambda=1
    coeffs = betagamma_shadow_coefficients(1.0, max_r)
    landscape['bg_lam=1'] = compute_explicit_formula_data('bg_lam=1', 'C', coeffs)

    # Virasoro c=1
    coeffs = virasoro_shadow_coefficients(1.0, max_r)
    landscape['Vir_c=1'] = compute_explicit_formula_data('Vir_c=1', 'M', coeffs)

    # Virasoro c=13 (self-dual)
    coeffs = virasoro_shadow_coefficients(13.0, max_r)
    landscape['Vir_c=13'] = compute_explicit_formula_data('Vir_c=13', 'M', coeffs)

    # Virasoro c=26
    coeffs = virasoro_shadow_coefficients(26.0, max_r)
    landscape['Vir_c=26'] = compute_explicit_formula_data('Vir_c=26', 'M', coeffs)

    return landscape


# ============================================================================
# 16. Consistency verification: three-path cross-check
# ============================================================================

def verify_von_mangoldt_consistency(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    r"""Verify shadow von Mangoldt coefficients by two coefficient paths.

    Path 1: Forward recursion from ``(Lambda_A * L_A)(r)=S_r log(r)``.
    Path 2: Dirichlet-inverse formula ``Lambda_A=(S log)*L_A^{-1}``.
    The convolution identity is checked separately against the path-1 output.

    Returns absolute and relative errors for the convolution and path checks.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    Lambda = shadow_von_mangoldt(shadow_coeffs, max_r)
    Lambda_inverse = shadow_von_mangoldt_from_log_derivative(shadow_coeffs, max_r)

    path_error = 0.0
    path_relative_error = 0.0
    for r in range(2, max_r + 1):
        diff = abs(Lambda.get(r, 0.0) - Lambda_inverse.get(r, 0.0))
        scale = max(1.0, abs(Lambda.get(r, 0.0)), abs(Lambda_inverse.get(r, 0.0)))
        path_error = max(path_error, diff)
        path_relative_error = max(path_relative_error, diff / scale)

    # Verify that the convolution identity holds for the forward recursion.
    max_error = 0.0
    max_relative_error = 0.0
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        lhs = Sr * math.log(r)
        # rhs = Lambda(r) + sum_{d | r, 2 <= d < r, r/d >= 2} Lambda(d) * S_{r/d}
        rhs = Lambda.get(r, 0.0)
        for d in range(2, r):
            if r % d != 0:
                continue
            q = r // d
            if q < 2:
                continue
            rhs += Lambda.get(d, 0.0) * shadow_coeffs.get(q, 0.0)
        error = abs(lhs - rhs)
        scale = max(1.0, abs(lhs), abs(rhs))
        max_error = max(max_error, error)
        max_relative_error = max(max_relative_error, error / scale)

    return {
        'max_error': max_error,
        'max_relative_error': max_relative_error,
        'path_error': path_error,
        'path_relative_error': path_relative_error,
        'path1_path2_agreement': path_relative_error < tol,
        'is_consistent': max_relative_error < tol and path_relative_error < tol,
    }


def verify_psi_two_paths(
    shadow_coeffs: Dict[int, float],
    x: float,
    sigma: float = 5.0,
    max_r: Optional[int] = None,
    tol: float = 0.5,
) -> Dict[str, Any]:
    r"""Compare psi_A(x) from direct summation vs inverse Mellin.

    Path 1: Direct sum of Lambda_A(r).
    Path 2: Inverse Mellin integral of -L_A'/L_A.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    psi_direct = shadow_chebyshev_psi(shadow_coeffs, x, max_r)
    psi_mellin = psi_from_inverse_mellin(shadow_coeffs, x, sigma=sigma,
                                          T=80.0, n_points=4000, max_r=max_r)
    error = abs(psi_direct - psi_mellin)
    return {
        'psi_direct': psi_direct,
        'psi_mellin': psi_mellin,
        'error': error,
        'is_consistent': error < tol,
    }
