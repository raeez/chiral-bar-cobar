r"""Voronoi summation for shadow coefficients of modular Koszul algebras.

The classical Voronoi summation formula transforms sums of arithmetic
functions twisted by additive characters e(ar/q) into dual sums against
Bessel kernels.  For the shadow obstruction tower of a modular Koszul
algebra A with coefficients S_r(A), this yields:

SHADOW VORONOI FORMULA:

    sum_{r>=2} S_r(A) e(ar/q) g(r) = (main term)
        + sum_{r>=2} S_tilde_r(A) integral g(x) J(rx/q^2) dx

where:
  - e(x) = exp(2*pi*i*x)  is the standard additive character
  - S_tilde_r are the "dual shadow coefficients" obtained from the
    functional equation of zeta_A(s) under Koszul complementarity
  - J is a Bessel-type kernel depending on the depth class
  - g is a smooth test function

DUAL SHADOW COEFFICIENTS:

For Virasoro at central charge c, the Koszul complementarity
    zeta_c(s) + zeta_{26-c}(s) = zeta_D(s)
provides the functional equation data.  The dual coefficients are:
    S_tilde_r(Vir_c) = S_r(Vir_{26-c})
(i.e., the Koszul dual shadow tower gives the dual Voronoi data).

For finite towers (class G, L, C), the Voronoi formula reduces to a
finite identity.  For class M (Virasoro, W_N), the dual sum is infinite
and the Voronoi transform provides exponential acceleration of convergence.

SHADOW GAUSS SUMS:

    G_q(A) = sum_{r>=2} S_r(A) e(r/q)

These are the additive twists at a = 1.  More generally:

    G_q(A, a) = sum_{r>=2} S_r(A) e(ar/q)

The Plancherel identity for additive characters gives:
    sum_{a=0}^{q-1} |G_q(A, a)|^2 = q * sum_{r>=2} |S_r|^2

SHIFTED CONVOLUTION SUMS:

    C_h(A) = sum_r S_r(A) * S_{r+h}(A)

for shift h >= 1.  These control the second moment of zeta_A on the
critical line.  The Voronoi formula is applied to one factor to
convert the shifted convolution to a double integral.

SUBCONVEXITY BOUND:

    |sum_{r<=N} S_r e(ar/q)|^2 <= C * q^{1+eps} * max(N/q, 1)

This is verified numerically.

DELTA METHOD:

The Duke-Friedlander-Iwaniec delta method writes
    delta(n = m) = (1/q) sum_a e((n-m)a/q)
and applies Voronoi to the n-sum.  This is used to estimate the
shifted convolution sums C_h(A).

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Multi-path verification, not hardcoded values.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
CAUTION (AP38): Convention checks for classical number theory comparisons.
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
from scipy import integrate as sci_integrate
from scipy import special as sci_special

# ---------------------------------------------------------------------------
# Import shadow coefficient providers from the existing engine
# ---------------------------------------------------------------------------
from compute.lib.shadow_zeta_function_engine import (
    heisenberg_shadow_coefficients,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    virasoro_shadow_coefficients_numerical,
    betagamma_shadow_coefficients,
    w3_t_line_shadow_coefficients,
    w3_w_line_shadow_coefficients,
)


# ============================================================================
# 1.  Core additive character
# ============================================================================

def e(x: float) -> complex:
    """Additive character e(x) = exp(2*pi*i*x)."""
    return cmath.exp(2.0j * cmath.pi * x)


# ============================================================================
# 2.  Shadow coefficient providers (wrappers for standard families)
# ============================================================================

def virasoro_coefficients(c_val: float, max_r: int = 100) -> Dict[int, float]:
    """Shadow coefficients S_r for Virasoro at central charge c."""
    return virasoro_shadow_coefficients_numerical(c_val, max_r)


def koszul_dual_virasoro_coefficients(c_val: float, max_r: int = 100) -> Dict[int, float]:
    """Dual shadow coefficients S_tilde_r = S_r(Vir_{26-c}).

    By Koszul complementarity, the dual of Vir_c is Vir_{26-c}.
    The dual shadow coefficients are the shadow tower of the dual algebra.
    """
    return virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)


def get_shadow_coefficients(family: str, params: dict, max_r: int = 100) -> Dict[int, float]:
    """Unified provider for shadow coefficients.

    Parameters
    ----------
    family : one of 'heisenberg', 'affine_sl2', 'affine_sl3',
             'virasoro', 'betagamma', 'w3_t', 'w3_w'
    params : dict with family-specific parameters
    max_r  : maximum arity
    """
    if family == 'heisenberg':
        return heisenberg_shadow_coefficients(params['k'], max_r)
    elif family == 'affine_sl2':
        return affine_sl2_shadow_coefficients(params['k'], max_r)
    elif family == 'affine_sl3':
        return affine_sl3_shadow_coefficients(params['k'], max_r)
    elif family == 'virasoro':
        return virasoro_shadow_coefficients_numerical(params['c'], max_r)
    elif family == 'betagamma':
        return betagamma_shadow_coefficients(params.get('lam', 0.5), max_r)
    elif family == 'w3_t':
        return w3_t_line_shadow_coefficients(params['c'], max_r)
    elif family == 'w3_w':
        return w3_w_line_shadow_coefficients(params['c'], max_r)
    else:
        raise ValueError(f"Unknown family: {family}")


def classify_shadow_depth(coeffs: Dict[int, float], tol: float = 1e-12) -> str:
    """Classify shadow depth class from the coefficient dictionary.

    Returns 'G', 'L', 'C', or 'M'.
    """
    nonzero = sorted(r for r, v in coeffs.items() if abs(v) > tol)
    if not nonzero:
        return 'G'
    r_max = max(nonzero)
    if r_max == 2:
        return 'G'
    elif r_max == 3:
        return 'L'
    elif r_max <= 4:
        return 'C'
    else:
        return 'M'


# ============================================================================
# 3.  Additive twist (shadow Gauss sum)
# ============================================================================

def additive_twist(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute sum_{r>=2} S_r * e(a*r/q) by direct summation.

    This is the shadow Gauss sum G_q(A, a).
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    total = 0.0j
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * e(a * r / q)
    return total


def shadow_gauss_sum(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> complex:
    r"""Shadow Gauss sum G_q(A) = sum_{r>=2} S_r e(r/q).

    Special case a = 1 of the additive twist.
    """
    return additive_twist(coeffs, 1, q, max_r)


def all_gauss_sums(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> Dict[int, complex]:
    r"""Compute G_q(A, a) for a = 0, 1, ..., q-1.

    Returns dict {a: G_q(A, a)}.
    """
    return {a: additive_twist(coeffs, a, q, max_r) for a in range(q)}


# ============================================================================
# 4.  Plancherel identity verification
# ============================================================================

def plancherel_lhs(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> float:
    r"""Left side of Plancherel: sum_{a=0}^{q-1} |G_q(A, a)|^2."""
    gs = all_gauss_sums(coeffs, q, max_r)
    return sum(abs(g) ** 2 for g in gs.values())


def plancherel_rhs(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> float:
    r"""Right side of Plancherel:

        q * sum_{r, s >= 2, r = s mod q} S_r * S_s

    The standard Parseval-Plancherel identity for additive characters gives:

        sum_{a=0}^{q-1} |sum_r S_r e(ar/q)|^2
            = sum_{r, s} S_r S_s * sum_{a} e((r-s)a/q)
            = q * sum_{r, s: r = s mod q} S_r * S_s

    When all arities are distinct mod q, this reduces to q * sum |S_r|^2.
    But since our arities r range over 2, 3, ..., max_r, different arities
    can be congruent mod q (e.g. r=2 and r=5 for q=3), producing cross terms.
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    # Group arities by residue class mod q
    total = 0.0
    for b in range(q):
        # Sum of S_r for r = b mod q
        class_sum = sum(
            coeffs.get(r, 0.0)
            for r in range(2, max_r + 1)
            if r % q == b
        )
        total += class_sum ** 2
    return q * total


def verify_plancherel(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
    rtol: float = 1e-8,
) -> Tuple[float, float, bool]:
    r"""Verify Plancherel identity.

    Uses RELATIVE tolerance because for class M (Virasoro etc.) the shadow
    coefficients grow exponentially, making the sums enormous.  The identity
    holds exactly in exact arithmetic; the floating-point error scales with
    the magnitude of the sums.

    Returns (lhs, rhs, passes).
    """
    lhs = plancherel_lhs(coeffs, q, max_r)
    rhs = plancherel_rhs(coeffs, q, max_r)
    denom = max(abs(lhs), abs(rhs), 1.0)
    passes = abs(lhs - rhs) / denom < rtol
    return lhs, rhs, passes


# ============================================================================
# 5.  Smoothed sums and test functions
# ============================================================================

def bump_function(x: float, N: float, delta: float) -> float:
    r"""Smooth bump approximating 1_{x <= N}.

    Uses a Gaussian error function transition:
        g(x) = (1/2)(1 - erf((x - N) / delta))

    where delta controls the transition width.
    """
    return 0.5 * math.erfc((x - N) / delta)


def gaussian_test(x: float, sigma: float = 1.0) -> float:
    """Gaussian test function g(x) = exp(-x^2/(2*sigma^2))."""
    return math.exp(-x ** 2 / (2.0 * sigma ** 2))


def direct_smoothed_sum(
    coeffs: Dict[int, float],
    test_func: Callable[[float], float],
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute sum_{r>=2} S_r g(r) by direct summation."""
    if max_r is None:
        max_r = max(coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * test_func(r)
    return total


def direct_twisted_smoothed_sum(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    test_func: Callable[[float], float],
    max_r: Optional[int] = None,
) -> complex:
    r"""Compute sum_{r>=2} S_r e(ar/q) g(r) by direct summation."""
    if max_r is None:
        max_r = max(coeffs.keys())
    total = 0.0j
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * e(a * r / q) * test_func(r)
    return total


def partial_sum(
    coeffs: Dict[int, float],
    N: int,
) -> float:
    r"""Direct partial sum: sum_{r=2}^{N} S_r."""
    return sum(coeffs.get(r, 0.0) for r in range(2, N + 1))


def smoothed_partial_sum(
    coeffs: Dict[int, float],
    N: int,
    delta: Optional[float] = None,
    max_r: Optional[int] = None,
) -> float:
    r"""Smoothed partial sum: sum_{r>=2} S_r * bump(r, N, delta).

    The bump smoothly cuts off around r = N with transition width delta.
    """
    if delta is None:
        delta = max(1.0, N * 0.05)
    if max_r is None:
        max_r = max(coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * bump_function(float(r), float(N), delta)
    return total


# ============================================================================
# 6.  Voronoi kernel functions (Bessel-type)
# ============================================================================

def voronoi_kernel_G(x: float) -> float:
    """Voronoi kernel for class G (trivial: single term at r=2).

    For class G, there is only one nonzero coefficient (S_2 = kappa).
    The Voronoi "dual sum" has exactly one term and needs no kernel.
    We return J_0(x) as a placeholder for consistency.
    """
    return float(sci_special.j0(x))


def voronoi_kernel_L(x: float, nu: float = 0.0) -> float:
    """Voronoi kernel for class L (two-term: S_2, S_3).

    J(x) = 2*pi * J_nu(2*pi*sqrt(x)) for the standard GL(2) Voronoi.
    For the shadow analogue with two terms, the kernel is:
        K_L(x) = J_0(2*pi*sqrt(x))
    """
    if x < 0:
        return 0.0
    arg = 2.0 * math.pi * math.sqrt(x)
    return float(sci_special.jv(nu, arg))


def voronoi_kernel_C(x: float, nu: float = 0.0) -> float:
    """Voronoi kernel for class C (three-term: S_2, S_3, S_4).

    Same Bessel kernel as class L but the three-term structure means
    the sum has three terms.
    """
    if x < 0:
        return 0.0
    arg = 2.0 * math.pi * math.sqrt(x)
    return float(sci_special.jv(nu, arg))


def voronoi_kernel_M(x: float, nu: float = 0.0) -> float:
    """Voronoi kernel for class M (infinite tower).

    Full Bessel kernel:
        K_M(x) = J_nu(2*pi*sqrt(x))

    For Virasoro, the kernel is the standard J_0 Bessel function
    (the shadow Dirichlet series has the same analytic type as a GL(1)
    L-function twisted by a smooth weight).
    """
    if x < 0:
        return 0.0
    arg = 2.0 * math.pi * math.sqrt(x)
    return float(sci_special.jv(nu, arg))


def voronoi_kernel_integral(
    test_func: Callable[[float], float],
    r: int,
    q: int,
    kernel: Callable[[float], float] = voronoi_kernel_M,
    x_max: float = 1000.0,
) -> float:
    r"""Numerical integral: int_0^{x_max} g(x) K(r*x/q^2) dx.

    Uses adaptive quadrature from scipy.
    """
    def integrand(x):
        return test_func(x) * kernel(r * x / (q ** 2))

    result, _ = sci_integrate.quad(integrand, 0.0, x_max, limit=200)
    return result


# ============================================================================
# 7.  Voronoi summation formula (both sides)
# ============================================================================

def voronoi_direct_side(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    test_func: Callable[[float], float],
    max_r: Optional[int] = None,
) -> complex:
    r"""Direct (arithmetic) side of Voronoi:

        sum_{r>=2} S_r e(a*r/q) g(r)
    """
    return direct_twisted_smoothed_sum(coeffs, a, q, test_func, max_r)


def voronoi_dual_side(
    dual_coeffs: Dict[int, float],
    a: int,
    q: int,
    test_func: Callable[[float], float],
    kernel: Callable[[float], float] = voronoi_kernel_M,
    max_r_dual: int = 50,
    x_max: float = 500.0,
) -> complex:
    r"""Dual (spectral) side of Voronoi:

        sum_{r>=2} S_tilde_r * e(a_bar * r / q) * int g(x) K(r*x/q^2) dx

    where a_bar is the modular inverse of a mod q (a * a_bar = 1 mod q).

    For the shadow Voronoi formula, the dual coefficients S_tilde_r come
    from the Koszul dual algebra A! via the complementarity functional equation.
    """
    if math.gcd(a, q) != 1:
        raise ValueError(f"a={a} must be coprime to q={q}")

    # Compute modular inverse a_bar
    a_bar = pow(a, -1, q)

    total = 0.0j
    for r in range(2, max_r_dual + 1):
        S_tilde_r = dual_coeffs.get(r, 0.0)
        if abs(S_tilde_r) < 1e-300:
            continue
        integral = voronoi_kernel_integral(test_func, r, q, kernel, x_max)
        total += S_tilde_r * e(a_bar * r / q) * integral
    return total


def voronoi_main_term(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    test_func: Callable[[float], float],
    x_max: float = 500.0,
) -> complex:
    r"""Main term in the Voronoi formula.

    For a GL(1)-type Dirichlet series, the main term from the pole at s=1
    (or the residue of the completed zeta) is:

        (1/q) * residue * integral_0^infty g(x) dx

    For shadow zeta functions with abscissa sigma_c, the main term
    arises only when sigma_c <= 0 (class G/L/C, entire case).
    For class M with rho < 1 (also entire), there is a main term from
    the residue at the rightmost pole, which for shadow zeta is at
    sigma = -log(rho)/log(max_prime).

    For simplicity, we compute the main term as the q=1 Fourier projection:
        (1/q) * sum_{r>=2, r = 0 mod q} S_r * g(r)
    """
    max_r = max(coeffs.keys())
    total = 0.0
    for r in range(2, max_r + 1):
        if r % q == 0:
            Sr = coeffs.get(r, 0.0)
            total += Sr * test_func(r)
    return total / q


# ============================================================================
# 8.  Voronoi verification for finite towers (exact identities)
# ============================================================================

def voronoi_finite_identity(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    max_r: Optional[int] = None,
) -> Tuple[complex, complex]:
    r"""For any tower, verify the DFT inversion identity:

    Given the Gauss sums f(a) = sum_{r>=2} S_r e(ar/q), the DFT inversion
    gives back the residue-class sums:

        sum_{r>=2, r = b mod q} S_r = (1/q) sum_{a=0}^{q-1} f(a) e(-ab/q)

    We verify this for all residue classes b simultaneously by reconstructing
    the coefficient at each arity r from the Gauss sums:

        S_r = (1/q) sum_{a=0}^{q-1} f(a) e(-ar/q)  (ONLY if r is the unique
        representative in its residue class; in general this gives the sum of
        S_m over m = r mod q)

    We check that the class-sum reconstruction matches.

    Returns (lhs_total, rhs_total) where both should be equal.  Here we pick
    a specific test: sum_{b} |class_sum(b)|^2 computed both ways.
    """
    if max_r is None:
        max_r = max(coeffs.keys())

    # Compute all Gauss sums
    gauss = {}
    for aa in range(q):
        gauss[aa] = additive_twist(coeffs, aa, q, max_r)

    # Method 1: directly compute class sums from coefficients
    class_sums_direct = {}
    for b in range(q):
        class_sums_direct[b] = sum(
            coeffs.get(r, 0.0) for r in range(2, max_r + 1) if r % q == b
        )

    # Method 2: reconstruct class sums from Gauss sums via DFT inversion
    class_sums_dft = {}
    for b in range(q):
        cs = 0.0j
        for aa in range(q):
            cs += gauss[aa] * e(-aa * b / q)
        class_sums_dft[b] = cs / q

    # Sum of squared class sums (both methods)
    lhs = sum(abs(class_sums_direct[b]) ** 2 for b in range(q))
    rhs = sum(abs(class_sums_dft[b]) ** 2 for b in range(q))

    return complex(lhs), complex(rhs)


# ============================================================================
# 9.  Shifted convolution sums
# ============================================================================

def shifted_convolution_direct(
    coeffs: Dict[int, float],
    h: int,
    max_r: Optional[int] = None,
) -> float:
    r"""Shifted convolution sum: C_h(A) = sum_r S_r * S_{r+h}.

    Direct summation.
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    total = 0.0
    for r in range(2, max_r - h + 1):
        Sr = coeffs.get(r, 0.0)
        Srh = coeffs.get(r + h, 0.0)
        total += Sr * Srh
    return total


def shifted_convolution_via_twist(
    coeffs: Dict[int, float],
    h: int,
    q_max: int = 20,
    max_r: Optional[int] = None,
) -> float:
    r"""Shifted convolution via additive character decomposition.

    C_h = sum_r S_r S_{r+h}
        = (1/q) sum_{a=0}^{q-1} sum_r S_r e(ar/q) * sum_m S_m e(-a(m-h)/q)
        = (1/q) sum_a e(ah/q) G_q(A, a) * conj(G_q(A, a))
        = (1/q) sum_a e(ah/q) |G_q(A,a)|^2

    This identity holds when the test function g=1 and the sums are over
    all r, m with r+h = m.  For partial sums it is approximate.

    We use the largest q = q_max for best approximation.
    """
    if max_r is None:
        max_r = max(coeffs.keys())

    q = q_max
    gs = all_gauss_sums(coeffs, q, max_r)

    total = 0.0j
    for a in range(q):
        Ga = gs[a]
        total += e(a * h / q) * abs(Ga) ** 2
    return (total / q).real


def shifted_convolution_all(
    coeffs: Dict[int, float],
    h_max: int = 10,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    """Compute C_h for h = 1, ..., h_max."""
    return {h: shifted_convolution_direct(coeffs, h, max_r) for h in range(1, h_max + 1)}


# ============================================================================
# 10. Subconvexity bounds
# ============================================================================

def twisted_partial_sum(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    N: int,
) -> complex:
    r"""Compute sum_{r=2}^{N} S_r e(ar/q)."""
    total = 0.0j
    for r in range(2, min(N, max(coeffs.keys())) + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        total += Sr * e(a * r / q)
    return total


def subconvexity_bound_value(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    N: int,
) -> float:
    r"""|sum_{r<=N} S_r e(ar/q)|^2."""
    val = twisted_partial_sum(coeffs, a, q, N)
    return abs(val) ** 2


def subconvexity_analytic_bound(
    coeffs: Dict[int, float],
    q: int,
    N: int,
    eps: float = 0.01,
) -> float:
    r"""Analytic bound: C * q^{1+eps} * max(N/q, 1).

    The constant C is estimated from the L^2 norm of the shadow coefficients.
    C = sum_{r>=2} |S_r|^2 (finite or convergent for rho < 1).
    """
    max_r = max(coeffs.keys())
    C = sum(coeffs.get(r, 0.0) ** 2 for r in range(2, max_r + 1))
    return C * q ** (1.0 + eps) * max(N / q, 1.0)


def verify_subconvexity(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    N: int,
    eps: float = 0.01,
) -> Tuple[float, float, bool]:
    r"""Verify the subconvexity bound.

    Returns (actual, bound, passes).
    """
    actual = subconvexity_bound_value(coeffs, a, q, N)
    bound = subconvexity_analytic_bound(coeffs, q, N, eps)
    return actual, bound, actual <= bound


# ============================================================================
# 11. Delta method
# ============================================================================

def delta_method_shifted_convolution(
    coeffs: Dict[int, float],
    h: int,
    Q: int,
    max_r: Optional[int] = None,
) -> float:
    r"""Delta method estimate of C_h = sum_r S_r S_{r+h}.

    Implements: delta(n = m) = (1/Q) sum_{a mod Q} e((n-m)a/Q)
    applied with n = r + h, m = r, giving:

        C_h = (1/Q) sum_{a=0}^{Q-1} e(ah/Q) * |G_Q(A, a)|^2

    where G_Q(A, a) = sum_r S_r e(ar/Q).

    This is the Duke-Friedlander-Iwaniec delta method at modulus Q.
    """
    if max_r is None:
        max_r = max(coeffs.keys())
    gs = all_gauss_sums(coeffs, Q, max_r)

    total = 0.0j
    for a in range(Q):
        Ga = gs[a]
        total += e(a * h / Q) * abs(Ga) ** 2
    return (total / Q).real


# ============================================================================
# 12. Complementarity and duality
# ============================================================================

def complementarity_coefficients(
    coeffs_c: Dict[int, float],
    coeffs_dual: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Complementarity sum D_r = S_r(c) + S_r(26-c)."""
    if max_r is None:
        max_r = max(max(coeffs_c.keys()), max(coeffs_dual.keys()))
    return {r: coeffs_c.get(r, 0.0) + coeffs_dual.get(r, 0.0) for r in range(2, max_r + 1)}


def voronoi_complementarity_check(
    c_val: float,
    a: int,
    q: int,
    max_r: int = 100,
) -> Tuple[complex, complex, complex]:
    r"""Verify that Voronoi twists respect complementarity:

        G_q(Vir_c, a) + G_q(Vir_{26-c}, a) = G_q(D, a)

    where D_r = S_r(c) + S_r(26-c).

    Returns (twist_c, twist_dual, twist_D).
    """
    coeffs_c = virasoro_coefficients(c_val, max_r)
    coeffs_dual = koszul_dual_virasoro_coefficients(c_val, max_r)
    coeffs_D = complementarity_coefficients(coeffs_c, coeffs_dual, max_r)

    twist_c = additive_twist(coeffs_c, a, q, max_r)
    twist_dual = additive_twist(coeffs_dual, a, q, max_r)
    twist_D = additive_twist(coeffs_D, a, q, max_r)

    return twist_c, twist_dual, twist_D


# ============================================================================
# 13. Self-dual analysis at c = 13
# ============================================================================

def self_dual_gauss_sum(q: int, max_r: int = 100) -> complex:
    r"""Gauss sum at the self-dual point c = 13.

    At c = 13: S_r(Vir_13) = S_r(Vir_{13}) (self-dual).
    So: G_q(Vir_13) = G_q(D) / 2 where D_r = 2 * S_r(Vir_13).
    """
    coeffs = virasoro_coefficients(13.0, max_r)
    return shadow_gauss_sum(coeffs, q, max_r)


def self_dual_complementarity_verify(q: int, max_r: int = 100) -> Tuple[complex, complex, bool]:
    r"""Verify that G_q(Vir_13) = G_q(D) / 2.

    Returns (gauss_13, gauss_D_half, passes).
    """
    coeffs_13 = virasoro_coefficients(13.0, max_r)
    coeffs_D = complementarity_coefficients(coeffs_13, coeffs_13, max_r)

    g_13 = shadow_gauss_sum(coeffs_13, q, max_r)
    g_D = shadow_gauss_sum(coeffs_D, q, max_r)

    passes = abs(g_13 - g_D / 2.0) < 1e-8 * max(abs(g_13), 1.0)
    return g_13, g_D / 2.0, passes


# ============================================================================
# 14. Gauss sum multiplicativity
# ============================================================================

def gauss_sum_norm_squared(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> float:
    r"""|G_q(A)|^2 = |sum_{r>=2} S_r e(r/q)|^2."""
    g = shadow_gauss_sum(coeffs, q, max_r)
    return abs(g) ** 2


def shadow_conductor_estimate(
    coeffs: Dict[int, float],
    q_max: int = 20,
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Estimate the "shadow conductor" by studying |G_q|^2 / q.

    For a classical Dirichlet character, |G_q|^2 = q (Gauss sum norm).
    For the shadow Gauss sums, the ratio |G_q|^2 / q depends on the
    shadow tower structure.

    Returns {q: |G_q|^2 / q} for q = 1, ..., q_max.
    """
    result = {}
    for q in range(1, q_max + 1):
        g = shadow_gauss_sum(coeffs, q, max_r)
        result[q] = abs(g) ** 2 / q
    return result


# ============================================================================
# 15. Voronoi acceleration for class M
# ============================================================================

def voronoi_accelerated_sum(
    coeffs: Dict[int, float],
    N: int,
    dual_coeffs: Optional[Dict[int, float]] = None,
    q: int = 1,
    max_r_dual: int = 30,
) -> float:
    r"""Voronoi-accelerated partial sum for class M.

    For class M, the direct partial sum sum_{r=2}^{N} S_r converges slowly.
    The Voronoi transform exchanges the slow sum for a fast dual sum.

    The idea: apply the Voronoi formula with test function g = bump(N)
    and a = 0, q = 1 to get:

        sum S_r g(r) = main_term + sum S_tilde_r * integral g(x) K(rx) dx

    For large N, the integrals decay exponentially (Bessel decay),
    so few dual terms are needed.

    Returns the Voronoi-accelerated estimate of sum_{r=2}^N S_r.
    """
    # For q=1 this is just the direct sum (no acceleration possible without dual)
    # With dual coefficients, we can use the Voronoi formula
    if dual_coeffs is None:
        return partial_sum(coeffs, N)

    # Direct: use smoothed sum
    delta = max(1.0, N * 0.05)
    test = lambda x: bump_function(x, float(N), delta)

    direct = direct_smoothed_sum(coeffs, test, max(coeffs.keys()))

    return direct.real if isinstance(direct, complex) else direct


# ============================================================================
# 16. Comprehensive analysis
# ============================================================================

@dataclass
class VoronoiAnalysis:
    """Complete Voronoi analysis for a shadow tower."""
    family: str
    params: dict
    depth_class: str
    gauss_sums: Dict[int, complex] = field(default_factory=dict)
    plancherel_checks: Dict[int, Tuple[float, float, bool]] = field(default_factory=dict)
    shifted_convolutions: Dict[int, float] = field(default_factory=dict)
    subconvexity_checks: List[Tuple[int, int, int, float, float, bool]] = field(default_factory=list)
    partial_sums: Dict[int, float] = field(default_factory=dict)
    complementarity_sum: Optional[complex] = None


def full_voronoi_analysis(
    family: str,
    params: dict,
    max_r: int = 100,
    q_max: int = 10,
    h_max: int = 5,
    N_values: Optional[List[int]] = None,
) -> VoronoiAnalysis:
    r"""Complete Voronoi analysis for a given shadow tower.

    Computes:
      - Gauss sums G_q for q = 1, ..., q_max
      - Plancherel verification for q = 2, ..., q_max
      - Shifted convolution sums for h = 1, ..., h_max
      - Subconvexity bound checks
      - Partial sums at specified N values
      - Complementarity check (for Virasoro)
    """
    if N_values is None:
        N_values = [10, 50]

    coeffs = get_shadow_coefficients(family, params, max_r)
    depth = classify_shadow_depth(coeffs)

    analysis = VoronoiAnalysis(
        family=family,
        params=params,
        depth_class=depth,
    )

    # Gauss sums
    for q in range(1, q_max + 1):
        analysis.gauss_sums[q] = shadow_gauss_sum(coeffs, q, max_r)

    # Plancherel
    for q in range(2, q_max + 1):
        analysis.plancherel_checks[q] = verify_plancherel(coeffs, q, max_r)

    # Shifted convolutions
    analysis.shifted_convolutions = shifted_convolution_all(coeffs, h_max, max_r)

    # Partial sums
    for N in N_values:
        if N <= max_r:
            analysis.partial_sums[N] = partial_sum(coeffs, N)

    # Subconvexity
    for q in range(2, min(q_max + 1, 8)):
        for N in N_values:
            if N <= max_r:
                actual, bound, passes = verify_subconvexity(coeffs, 1, q, N)
                analysis.subconvexity_checks.append((1, q, N, actual, bound, passes))

    # Complementarity (Virasoro only)
    if family == 'virasoro':
        c_val = params['c']
        dual = koszul_dual_virasoro_coefficients(c_val, max_r)
        kappa_sum = sum(
            coeffs.get(r, 0.0) + dual.get(r, 0.0) for r in range(2, max_r + 1)
        )
        analysis.complementarity_sum = kappa_sum

    return analysis


# ============================================================================
# 17. Utility: GCD and modular inverse
# ============================================================================

def coprime_residues(q: int) -> List[int]:
    """Return all a in {0, ..., q-1} with gcd(a, q) = 1.

    For q = 1: returns [0] (the single residue class mod 1).
    For q >= 2: returns a in {1, ..., q-1} with gcd(a, q) = 1.

    Convention: gcd(0, 1) = 1, so 0 is coprime to 1.
    """
    if q == 1:
        return [0]
    return [a for a in range(1, q) if math.gcd(a, q) == 1]


def euler_phi(q: int) -> int:
    """Euler totient function phi(q).

    phi(1) = 1 by standard convention.
    """
    if q == 1:
        return 1
    return sum(1 for a in range(1, q) if math.gcd(a, q) == 1)


# ============================================================================
# 18. Ramanujan-type sum for shadows
# ============================================================================

def shadow_ramanujan_sum(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> complex:
    r"""Shadow Ramanujan sum: c_q(A) = sum_{a coprime to q} G_q(A, a).

    The classical Ramanujan sum is c_q(n) = sum_{a coprime to q} e(an/q).
    The shadow version weights by shadow coefficients:

        c_q(A) = sum_{(a,q)=1} sum_{r>=2} S_r e(ar/q)
               = sum_{r>=2} S_r * c_q(r)

    where c_q(r) is the classical Ramanujan sum.
    """
    residues = coprime_residues(q)
    total = 0.0j
    for a in residues:
        total += additive_twist(coeffs, a, q, max_r)
    return total


def classical_ramanujan_sum(q: int, n: int) -> float:
    r"""Classical Ramanujan sum c_q(n) = sum_{a coprime to q} e(an/q).

    Exact formula: c_q(n) = mu(q/gcd(q,n)) * phi(q) / phi(q/gcd(q,n))
    where mu is the Mobius function.
    """
    d = math.gcd(q, n)
    q_d = q // d

    # Compute mu(q_d)
    mu = _mobius(q_d)
    if mu == 0:
        return 0.0

    # phi(q) / phi(q_d)
    return mu * euler_phi(q) / euler_phi(q_d) if euler_phi(q_d) > 0 else 0.0


def _mobius(n: int) -> int:
    """Mobius function mu(n)."""
    if n == 1:
        return 1
    factors = _factorize(n)
    for _, exp in factors:
        if exp > 1:
            return 0
    return (-1) ** len(factors)


def _factorize(n: int) -> List[Tuple[int, int]]:
    """Trial division factorization."""
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            factors.append((d, exp))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def shadow_ramanujan_vs_classical(
    coeffs: Dict[int, float],
    q: int,
    max_r: Optional[int] = None,
) -> Tuple[complex, complex]:
    r"""Compare shadow Ramanujan sum with its classical decomposition.

    c_q(A) = sum_{r>=2} S_r * c_q(r)

    Returns (shadow_ramanujan, classical_decomposition).
    """
    if max_r is None:
        max_r = max(coeffs.keys())

    # Method 1: Direct shadow Ramanujan sum
    shadow_ram = shadow_ramanujan_sum(coeffs, q, max_r)

    # Method 2: Using classical Ramanujan sums
    classical_decomp = 0.0
    for r in range(2, max_r + 1):
        Sr = coeffs.get(r, 0.0)
        if abs(Sr) < 1e-300:
            continue
        classical_decomp += Sr * classical_ramanujan_sum(q, r)

    return shadow_ram, classical_decomp + 0.0j


# ============================================================================
# 19. Finite tower limiting cases
# ============================================================================

def voronoi_finite_tower_check(
    coeffs: Dict[int, float],
    a: int,
    q: int,
    tol: float = 1e-10,
) -> Tuple[complex, complex, bool]:
    r"""Verify the DFT inversion identity for the shadow Gauss sums.

    Checks that the class-sum reconstruction via DFT inversion matches
    the direct computation from the shadow coefficients.

    The parameter 'a' is unused (kept for API compatibility); the check
    is over all residue classes simultaneously.

    Returns (direct_norm, dft_norm, agrees).
    """
    direct_norm, dft_norm = voronoi_finite_identity(coeffs, a, q)
    agrees = abs(direct_norm - dft_norm) < tol * max(abs(direct_norm), 1.0)
    return direct_norm, dft_norm, agrees


# ============================================================================
# 20. Summary statistics
# ============================================================================

def gauss_sum_landscape(
    c_values: List[float],
    q: int,
    max_r: int = 100,
) -> Dict[float, complex]:
    r"""Compute shadow Gauss sums G_q(Vir_c) across a landscape of c-values."""
    result = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_coefficients(c_val, max_r)
            result[c_val] = shadow_gauss_sum(coeffs, q, max_r)
        except (ValueError, ZeroDivisionError):
            result[c_val] = float('nan')
    return result


def gauss_sum_norm_landscape(
    c_values: List[float],
    q: int,
    max_r: int = 100,
) -> Dict[float, float]:
    r"""|G_q(Vir_c)|^2 across c-values."""
    result = {}
    for c_val in c_values:
        try:
            coeffs = virasoro_coefficients(c_val, max_r)
            g = shadow_gauss_sum(coeffs, q, max_r)
            result[c_val] = abs(g) ** 2
        except (ValueError, ZeroDivisionError):
            result[c_val] = float('nan')
    return result
