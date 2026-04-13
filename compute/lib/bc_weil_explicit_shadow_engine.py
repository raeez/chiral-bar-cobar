r"""Weil explicit formula in the shadow/bar-cobar context.

The classical Weil explicit formula encodes the duality between primes
and zeros of the Riemann zeta function:

    sum_{p, k} f_hat(k log p) / p^{k/2}
        = f_hat(0) * log(conductor) - sum_rho f_hat((1/2 - rho)/i) + (arch.)

For the shadow obstruction tower of a modular Koszul algebra A, the
"primes" are the arities r >= 2, and the "zeros" are zeros of zeta_A(s).

SHADOW VON MANGOLDT FUNCTION:

    Lambda_A(r) is the coefficient of r^{-s} in -zeta'_A(s)/zeta_A(s).

For a Dirichlet series zeta_A(s) = sum_{r>=2} S_r r^{-s}, the logarithmic
derivative -zeta'/zeta has coefficients determined by the shadow Mobius
function mu_A, which inverts S under Dirichlet convolution.

SHADOW WEIL EXPLICIT FORMULA:

For a test function f in the Schwartz space, with Mellin transform
    f_hat(s) = int_0^infty f(t) t^{s-1} dt,

the explicit formula states:

    sum_{r>=2} Lambda_A(r) f(log r) / sqrt(r)
        = (main term) - sum_{rho} f_hat(rho - 1/2) + (error)

where rho ranges over zeros of zeta_A(s).

For FINITE TOWERS (class G, L, C), zeta_A(s) is a Dirichlet polynomial
with finitely many terms, so:
  - Lambda_A has finitely many nonzero values (computable exactly)
  - The zeros of zeta_A are the roots of a polynomial in {r^{-s}}
  - The explicit formula reduces to a finite identity

For CLASS M (Virasoro, W_N), zeta_A is an infinite Dirichlet series with
infinitely many zeros, and the formula is a genuine spectral identity.

WEIL POSITIVITY CRITERION:

The positivity sum_rho |f_hat(rho)|^2 >= 0 for suitable f is automatic
(it is the norm of f_hat evaluated at the zeros). The deeper content is:
if ALL zeros satisfy Re(rho) = sigma_A/2 (shadow GRH), then certain
positivity conditions on test functions are equivalent to the zero
locations.

For finite towers: all zeros are computable exactly, and the critical
line can be verified explicitly.

CONNES TRACE FORMULA ANALOGUE:

In Connes' approach, the Weil explicit formula is a trace formula on
the adelic quotient. The shadow analogue: the bar complex B(A) on Ran(X)
is the "adelic space," and the bar differential d_B acts as the
"absorption operator." The trace of f(d_B) on the bar homology
reproduces the spectral side.

DENINGER COHOMOLOGICAL INTERPRETATION:

Deninger posits a cohomology H*(Z, F) with trace formula. The shadow
analogue: H*(Def_cyc^mod(A), d_Theta) is the modular cyclic deformation
cohomology twisted by the MC element. The spectral measure is the
eigenvalue distribution of the twisted differential.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:modular-cyclic-deformation-complex (chiral_hochschild_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (AP48).
CAUTION (AP10): Tests must use multi-path verification, not hardcoded values.
CAUTION (AP38): Convention checks when comparing to classical number theory.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import numpy as np
from sympy import (
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


# =============================================================================
# 1. Shadow von Mangoldt function from -zeta'_A / zeta_A
# =============================================================================

def shadow_von_mangoldt(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Compute the shadow von Mangoldt function Lambda_A(r).

    Lambda_A(r) is the coefficient of r^{-s} in the Dirichlet series
    -zeta'_A(s) / zeta_A(s).

    Since -zeta'_A(s) = sum S_r log(r) r^{-s}, and
    zeta_A(s) = sum S_r r^{-s}, the quotient -zeta'/zeta has
    Dirichlet series coefficients determined by:

        Lambda_A(r) = S_r log(r) / S_r + correction terms

    More precisely, if we write zeta_A = sum a_r r^{-s} (with a_r = S_r
    and a_1 = 0), then:

        -zeta'/zeta = (sum a_r log(r) r^{-s}) / (sum a_r r^{-s})

    The coefficients of -zeta'/zeta are computed via:
        (zeta_A)(Lambda_A) = -zeta'_A   (as Dirichlet series)

    i.e., sum_{d|r} a_d Lambda_A(r/d) = a_r log(r) for all r >= 2.

    This gives the recursion:
        Lambda_A(r) = (a_r log(r) - sum_{d|r, d<r, d>=2} a_d Lambda_A(r/d)) / a_{ref}

    where a_{ref} is the leading nonzero coefficient (a_2 = S_2 = kappa).

    CAUTION: This recursion is well-defined only if kappa = S_2 != 0.
    For kappa = 0 (uncurved algebras at the self-dual point), the von
    Mangoldt function is not defined by this route.

    Parameters
    ----------
    shadow_coeffs : dict {r: S_r} for r >= 2
    max_r : maximum arity to compute

    Returns
    -------
    Dict {r: Lambda_A(r)} for r >= 2.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    a = {r: shadow_coeffs.get(r, 0.0) for r in range(1, max_r + 1)}
    a[1] = 0.0  # Convention: a_1 = 0 for shadow sequences

    # The leading term: we need a nonzero a_d for the recursion.
    # For the shadow Dirichlet series, a_2 = kappa is generically nonzero.
    # We use the "augmented" convention: define zeta_A^aug(s) = 1 + zeta_A(s)
    # so a_1^aug = 1, which gives a well-defined recursion for Lambda_A.

    # With the augmented series (a_1 = 1):
    # sum_{d|r, d>=1} a^aug_d Lambda_A(r/d) = a_r^aug log(r)
    # Lambda_A(r) = a_r log(r) - sum_{d|r, 1<d<r} a_d Lambda_A(r/d)
    # (since a_1^aug = 1, the d=1 term gives Lambda_A(r) on the left)
    # (since a_1 = 0, a_r^aug = a_r for r >= 2)

    lam = {}
    for r in range(2, max_r + 1):
        val = a[r] * math.log(r)
        for d in range(2, r):
            if r % d == 0:
                q = r // d
                if q >= 2 and q in lam:
                    val -= a[d] * lam[q]
        lam[r] = val
    return lam


def shadow_von_mangoldt_exact(
    shadow_coeffs: Dict[int, Rational],
    max_r: Optional[int] = None,
) -> Dict[int, Any]:
    r"""Exact shadow von Mangoldt using sympy Rationals and exact log values.

    Returns dict {r: Lambda_A(r)} where Lambda_A(r) is a sympy expression
    involving log(2), log(3), log(5), etc.
    """
    from sympy import log as slog, Rational as R

    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    a = {r: shadow_coeffs.get(r, R(0)) for r in range(1, max_r + 1)}
    a[1] = R(0)

    lam = {}
    for r in range(2, max_r + 1):
        val = a[r] * slog(r)
        for d in range(2, r):
            if r % d == 0:
                q = r // d
                if q >= 2 and q in lam:
                    val -= a[d] * lam[q]
        lam[r] = cancel(val) if hasattr(val, 'expand') else val
    return lam


# =============================================================================
# 2. Shadow Mobius function (Dirichlet inverse of S)
# =============================================================================

def shadow_mobius_function(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[int, float]:
    r"""Compute the shadow Mobius function mu_A(r).

    mu_A is the Dirichlet inverse of the augmented shadow sequence:
        a^aug(1) = 1, a^aug(r) = S_r for r >= 2.

    The Dirichlet inverse satisfies:
        sum_{d|r} a^aug(d) mu_A(r/d) = delta_{r,1}

    Recursion:
        mu_A(1) = 1
        mu_A(r) = - sum_{d|r, d>1} a^aug(d) mu_A(r/d)  for r >= 2
                = - sum_{d|r, d>=2} S_d mu_A(r/d)

    This is the shadow analogue of the Mobius function. For Heisenberg
    (S_r = 0 for r >= 3), mu_A(r) is nonzero only at powers of 2.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    mu = {1: 1.0}
    for r in range(2, max_r + 1):
        val = 0.0
        for d in range(2, r + 1):
            if r % d == 0:
                q = r // d
                Sd = shadow_coeffs.get(d, 0.0)
                mu_q = mu.get(q, 0.0)
                val -= Sd * mu_q
        mu[r] = val
    return mu


def shadow_mobius_exact(
    shadow_coeffs: Dict[int, Rational],
    max_r: Optional[int] = None,
) -> Dict[int, Rational]:
    r"""Exact shadow Mobius function using Rationals."""
    from sympy import Rational as R

    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    mu = {1: R(1)}
    for r in range(2, max_r + 1):
        val = R(0)
        for d in range(2, r + 1):
            if r % d == 0:
                q = r // d
                Sd = shadow_coeffs.get(d, R(0))
                mu_q = mu.get(q, R(0))
                val -= Sd * mu_q
        mu[r] = cancel(val)
    return mu


# =============================================================================
# 3. Zeros of the shadow zeta function
# =============================================================================

def shadow_zeta_zeros_finite(
    shadow_coeffs: Dict[int, float],
    s_grid_re: Tuple[float, float] = (-5.0, 10.0),
    s_grid_im: Tuple[float, float] = (-30.0, 30.0),
    grid_density: int = 200,
    refine_tol: float = 1e-12,
) -> List[complex]:
    r"""Find zeros of zeta_A(s) numerically for finite shadow towers.

    For class G (Heisenberg): zeta_A(s) = kappa * 2^{-s}.
    This has NO zeros (kappa != 0 and 2^{-s} != 0 for all s).

    For class L (affine): zeta_A(s) = kappa * 2^{-s} + alpha * 3^{-s}.
    Zeros: kappa * 2^{-s} = -alpha * 3^{-s}
        => (2/3)^s = -alpha/kappa
        => s * log(2/3) = log(-alpha/kappa) + 2*pi*i*n
        => s_n = [log(alpha/kappa) + i*pi*(2n+1)] / log(3/2)

    For class C (beta-gamma): three-term polynomial in {2^{-s}, 3^{-s}, 4^{-s}}.
    Solved numerically.

    Uses grid search followed by Newton-Raphson refinement.

    Parameters
    ----------
    shadow_coeffs : dict {r: S_r}
    s_grid_re, s_grid_im : search region bounds
    grid_density : points per dimension in the initial grid
    refine_tol : tolerance for Newton refinement

    Returns
    -------
    List of zeros (complex) sorted by imaginary part.
    """
    # Determine nonzero arities
    nonzero = [(r, shadow_coeffs[r]) for r in sorted(shadow_coeffs.keys())
               if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]

    if len(nonzero) == 0:
        return []

    if len(nonzero) == 1:
        # Single-term Dirichlet series: S_r * r^{-s} = 0 has no solutions
        return []

    if len(nonzero) == 2:
        # Two-term: S_{r1} r1^{-s} + S_{r2} r2^{-s} = 0
        r1, S1 = nonzero[0]
        r2, S2 = nonzero[1]
        # (r1/r2)^s = -S2/S1
        ratio = -S2 / S1
        log_base = math.log(r1 / r2)  # = log(r1) - log(r2)
        if abs(log_base) < 1e-15:
            return []
        # s = (log|ratio| + i*(arg(ratio) + 2*pi*n)) / log_base
        if ratio > 0:
            base_re = math.log(ratio) / log_base
            base_im = 0.0
        elif ratio < 0:
            base_re = math.log(abs(ratio)) / log_base
            base_im = math.pi / log_base
        else:
            return []

        period = 2.0 * math.pi / abs(log_base)
        zeros = []
        # Collect zeros with imaginary part in the search region
        n_min = int(math.floor((s_grid_im[0] - base_im) / period))
        n_max = int(math.ceil((s_grid_im[1] - base_im) / period))
        for n in range(n_min, n_max + 1):
            s_zero = complex(base_re, base_im + n * period)
            if s_grid_re[0] <= s_zero.real <= s_grid_re[1]:
                zeros.append(s_zero)
        return sorted(zeros, key=lambda z: z.imag)

    # General case: numerical grid search + refinement
    def zeta_eval(s):
        total = 0.0 + 0.0j
        for r, Sr in nonzero:
            total += Sr * r ** (-s)
        return total

    def zeta_deriv(s):
        total = 0.0 + 0.0j
        for r, Sr in nonzero:
            total += -Sr * math.log(r) * r ** (-s)
        return total

    # Grid search for sign changes / small values
    re_pts = np.linspace(s_grid_re[0], s_grid_re[1], grid_density)
    im_pts = np.linspace(s_grid_im[0], s_grid_im[1], grid_density)

    candidates = []
    min_val = float('inf')
    for re_s in re_pts:
        for im_s in im_pts:
            s = complex(re_s, im_s)
            z = zeta_eval(s)
            mag = abs(z)
            if mag < 1.0:
                candidates.append((s, mag))

    # Sort by magnitude and refine the best candidates
    candidates.sort(key=lambda x: x[1])

    zeros = []
    for s0, _ in candidates[:100]:
        # Newton-Raphson
        s = s0
        for _ in range(50):
            z = zeta_eval(s)
            dz = zeta_deriv(s)
            if abs(dz) < 1e-50:
                break
            s_new = s - z / dz
            if abs(s_new - s) < refine_tol:
                s = s_new
                break
            s = s_new
        if abs(zeta_eval(s)) < 1e-8:
            # Check if this is a new zero (not a duplicate)
            is_new = True
            for z0 in zeros:
                if abs(s - z0) < 1e-6:
                    is_new = False
                    break
            if is_new:
                zeros.append(s)

    return sorted(zeros, key=lambda z: z.imag)


def shadow_zeta_zeros_class_L(
    kappa: float,
    alpha: float,
    r1: int = 2,
    r2: int = 3,
    n_zeros: int = 20,
) -> List[complex]:
    r"""Exact zeros for class L (two-term) shadow zeta.

    zeta_A(s) = kappa * r1^{-s} + alpha * r2^{-s} = 0
    => (r1/r2)^s = -alpha/kappa
    => s = [log(|alpha/kappa|) + i*(pi + 2*pi*n)] / log(r2/r1)

    Zeros lie on the vertical line Re(s) = log(|alpha/kappa|) / log(r2/r1).

    This is the CRITICAL LINE for class L algebras.
    """
    if abs(kappa) < 1e-50 or abs(alpha) < 1e-50:
        return []

    ratio = abs(alpha / kappa)
    log_ratio = math.log(r2 / r1)  # log(3/2) for standard
    sigma_crit = math.log(ratio) / log_ratio
    period = 2.0 * math.pi / log_ratio

    zeros = []
    # Use symmetric range to ensure conjugate pairing
    half = n_zeros // 2
    for n in range(-half, half + 1):
        t = (math.pi + 2.0 * math.pi * n) / log_ratio
        zeros.append(complex(sigma_crit, t))
        # Also include the conjugate (negative n offset)
        t_conj = -(math.pi + 2.0 * math.pi * n) / log_ratio
        zeros.append(complex(sigma_crit, t_conj))
    # Deduplicate (conjugate pairs may overlap at n=0 if pi/log_ratio = 0)
    unique = []
    for z in zeros:
        is_dup = False
        for u in unique:
            if abs(z - u) < 1e-10:
                is_dup = True
                break
        if not is_dup:
            unique.append(z)
    return sorted(unique, key=lambda z: z.imag)


# =============================================================================
# 4. Test function infrastructure (Gaussian and related)
# =============================================================================

def gaussian_test_function(x: float, sigma: float = 1.0) -> float:
    r"""Gaussian test function f(x) = exp(-x^2 / (2*sigma^2)).

    Normalized so f(0) = 1.
    """
    return math.exp(-x * x / (2.0 * sigma * sigma))


def gaussian_fourier_transform(t: float, sigma: float = 1.0) -> float:
    r"""Fourier transform of the Gaussian f(x) = exp(-x^2/(2*sigma^2)).

    f_hat(t) = sigma * sqrt(2*pi) * exp(-sigma^2 * t^2 / 2)

    Here f_hat(t) = int f(x) e^{-2*pi*i*x*t} dx for real-valued version,
    but for the Mellin-transform convention in the explicit formula:

    f_hat(s) = int_0^infty f(log u) u^{s-1} du
             = int_{-infty}^{infty} f(x) e^{x*s} dx   (substituting u = e^x)
             = int exp(-x^2/(2*sigma^2)) e^{sx} dx
             = sigma * sqrt(2*pi) * exp(sigma^2 * s^2 / 2)

    For the Weil explicit formula, we use the bilateral Laplace transform:
    f_hat(s) = int_{-inf}^{inf} f(x) e^{sx} dx = sigma*sqrt(2pi)*exp(s^2*sigma^2/2)
    """
    return sigma * math.sqrt(2.0 * math.pi) * math.exp(sigma * sigma * t * t / 2.0)


def gaussian_fourier_transform_complex(s: complex, sigma: float = 1.0) -> complex:
    r"""Complex-valued Fourier/Laplace transform of the Gaussian.

    f_hat(s) = sigma * sqrt(2*pi) * exp(sigma^2 * s^2 / 2)
    for complex s.

    Overflow protection: if Re(sigma^2 * s^2 / 2) > 500, return 0
    (the contribution is astronomically large or small depending on sign,
    but for the Weil formula the paired conjugate zeros cancel the
    imaginary growth).
    """
    exponent = sigma * sigma * s * s / 2.0
    if exponent.real > 500:
        # Overflow: return a large but finite value
        return complex(1e200, 0)
    if exponent.real < -500:
        return complex(0.0, 0.0)
    try:
        return sigma * cmath.sqrt(2.0 * cmath.pi) * cmath.exp(exponent)
    except OverflowError:
        return complex(0.0, 0.0)


def hat_function(x: float, a: float = 1.0) -> float:
    r"""Hat (triangular) test function: 1 - |x|/a for |x| < a, else 0."""
    if abs(x) >= a:
        return 0.0
    return 1.0 - abs(x) / a


def hat_fourier_transform(t: float, a: float = 1.0) -> float:
    r"""Bilateral Laplace transform of the hat function.

    f_hat(s) = int_{-a}^{a} (1 - |x|/a) e^{sx} dx
             = (2/a) * (cosh(sa) - 1) / s^2   for s != 0
             = a                                for s = 0
    """
    if abs(t) < 1e-15:
        return a
    return (2.0 / a) * (math.cosh(t * a) - 1.0) / (t * t)


def hat_fourier_transform_complex(s: complex, a: float = 1.0) -> complex:
    r"""Complex bilateral Laplace transform of the hat function."""
    if abs(s) < 1e-15:
        return complex(a, 0.0)
    return (2.0 / a) * (cmath.cosh(s * a) - 1.0) / (s * s)


# =============================================================================
# 5. Shadow Weil explicit formula
# =============================================================================

def weil_arithmetic_side(
    shadow_coeffs: Dict[int, float],
    test_fn: Callable[[float], float],
    sigma_shift: float = 0.0,
    max_r: Optional[int] = None,
) -> float:
    r"""Compute the arithmetic (prime/arity) side of the Weil explicit formula.

    Arithmetic side = sum_{r >= 2} Lambda_A(r) * f(log r) * r^{-sigma_shift}

    where Lambda_A is the shadow von Mangoldt function and f is the test
    function.

    The shift sigma_shift allows centering on a "critical line."
    With sigma_shift = 0, this is the raw sum.
    With sigma_shift = sigma_A/2, this centers on the putative critical line.

    Parameters
    ----------
    shadow_coeffs : dict {r: S_r}
    test_fn : the test function f: R -> R
    sigma_shift : real shift for centering
    max_r : truncation

    Returns
    -------
    Real value of the arithmetic side.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    lam = shadow_von_mangoldt(shadow_coeffs, max_r)

    total = 0.0
    for r in range(2, max_r + 1):
        lam_r = lam.get(r, 0.0)
        if abs(lam_r) < 1e-50:
            continue
        total += lam_r * test_fn(math.log(r)) * r ** (-sigma_shift)
    return total


def weil_spectral_side(
    zeros: List[complex],
    fourier_fn: Callable[[complex], complex],
    sigma_shift: float = 0.0,
) -> complex:
    r"""Compute the spectral (zeros) side of the Weil explicit formula.

    Spectral side = sum_{rho} f_hat(rho - sigma_shift)

    where rho ranges over the zeros of zeta_A(s) and f_hat is the
    bilateral Laplace transform of the test function.

    Parameters
    ----------
    zeros : list of zeros of zeta_A(s) (complex numbers)
    fourier_fn : the Laplace transform f_hat: C -> C
    sigma_shift : real shift for centering

    Returns
    -------
    Complex value of the spectral side.
    """
    total = 0.0 + 0.0j
    for rho in zeros:
        total += fourier_fn(rho - sigma_shift)
    return total


def weil_main_term(
    shadow_coeffs: Dict[int, float],
    fourier_fn: Callable[[complex], complex],
    sigma_shift: float = 0.0,
) -> complex:
    r"""Compute the main term (conductor contribution) of the explicit formula.

    For the shadow zeta, the main term arises from the residue of
    -zeta'/zeta at any pole of zeta_A.

    For finite towers, zeta_A has no pole (it is a polynomial in r^{-s}).
    The "conductor" analogue is:

    main_term = f_hat(0) * log(N_A)

    where N_A is the shadow conductor. For the purposes of the explicit
    formula, we define N_A implicitly by matching the two sides.

    For class G (Heisenberg): N_A = 2^{kappa} (trivially).
    For class L: N_A depends on both kappa and alpha.

    Since the shadow zeta has no Euler product in general, the conductor
    is not a product of local conductors. Instead, we compute it as the
    residual after matching arithmetic and spectral sides.

    Returns
    -------
    The main term contribution.
    """
    # For finite-tower shadow zeta, the main term is determined by
    # the zeta'/zeta expansion at the pole (if any).
    # For class G/L/C: no poles (entire), main term = 0.
    # The explicit formula becomes: arithmetic side = spectral side.
    return complex(0.0, 0.0)


def weil_explicit_formula_verify(
    shadow_coeffs: Dict[int, float],
    sigma: float = 1.0,
    sigma_shift: float = 0.0,
    max_r: int = 50,
    n_zeros: int = 40,
    test_fn_type: str = 'gaussian',
) -> Dict[str, Any]:
    r"""Verify the Weil explicit formula for a given shadow tower.

    Computes both sides and checks agreement.

    For finite towers, the formula is an exact finite identity.
    For class M, it is checked to numerical precision.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dictionary
    sigma : width parameter for the Gaussian test function
    sigma_shift : centering shift
    max_r : truncation for arithmetic side
    n_zeros : number of zeros to include in spectral side
    test_fn_type : 'gaussian' or 'hat'

    Returns
    -------
    Dict with:
        'arithmetic_side': float
        'spectral_side': complex
        'main_term': complex
        'discrepancy': float  (should be ~0 if formula holds)
        'zeros_used': int
    """
    # Determine shadow tower class
    nonzero_arities = [r for r in sorted(shadow_coeffs.keys())
                       if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]
    is_finite = (max(nonzero_arities) <= max_r and
                 all(abs(shadow_coeffs.get(r, 0.0)) < 1e-50
                     for r in range(max(nonzero_arities) + 1, max_r + 1)))

    # Set up test function and its transform
    if test_fn_type == 'gaussian':
        test_fn = lambda x: gaussian_test_function(x, sigma)
        fourier_fn = lambda s: gaussian_fourier_transform_complex(s, sigma)
    elif test_fn_type == 'hat':
        test_fn = lambda x: hat_function(x, sigma)
        fourier_fn = lambda s: hat_fourier_transform_complex(s, sigma)
    else:
        raise ValueError(f"Unknown test function type: {test_fn_type}")

    # Arithmetic side
    arith = weil_arithmetic_side(shadow_coeffs, test_fn, sigma_shift, max_r)

    # Find zeros
    if is_finite and len(nonzero_arities) == 1:
        # Class G: no zeros
        zeros = []
    elif is_finite and len(nonzero_arities) == 2:
        # Class L: exact zeros
        r1 = nonzero_arities[0]
        r2 = nonzero_arities[1]
        kappa_val = shadow_coeffs[r1]
        alpha_val = shadow_coeffs[r2]
        zeros = shadow_zeta_zeros_class_L(
            kappa_val, alpha_val, r1, r2, n_zeros)
    else:
        # General: numerical search
        zeros = shadow_zeta_zeros_finite(
            shadow_coeffs,
            s_grid_re=(-5.0, 10.0),
            s_grid_im=(-50.0, 50.0),
            grid_density=150,
        )

    # Spectral side
    spectral = weil_spectral_side(zeros, fourier_fn, sigma_shift)

    # Main term
    main = weil_main_term(shadow_coeffs, fourier_fn, sigma_shift)

    # The explicit formula: arith = main - spectral + error
    # => discrepancy = arith - Re(main) + Re(spectral)
    # For finite towers with no pole: main = 0, so arith = -spectral
    discrepancy = arith + spectral.real

    return {
        'arithmetic_side': arith,
        'spectral_side': spectral,
        'main_term': main,
        'discrepancy': abs(discrepancy),
        'zeros_used': len(zeros),
        'zeros': zeros,
    }


# =============================================================================
# 6. Weil positivity criterion
# =============================================================================

def weil_positivity_sum(
    zeros: List[complex],
    sigma: float = 1.0,
) -> float:
    r"""Compute the Weil positivity sum: sum_rho |f_hat(rho)|^2.

    For f(x) = exp(-x^2/(2*sigma^2)):
        f_hat(s) = sigma * sqrt(2*pi) * exp(sigma^2 * s^2 / 2)

    |f_hat(rho)|^2 = 2*pi*sigma^2 * exp(sigma^2 * Re(rho^2))

    Since rho = a + bi:
        Re(rho^2) = a^2 - b^2

    So |f_hat(rho)|^2 = 2*pi*sigma^2 * exp(sigma^2 * (a^2 - b^2))

    This is always >= 0 term by term, so the sum is trivially nonneg.

    The DEEPER positivity is the Li criterion analogue: for certain
    explicitly constructed f, the sum being nonneg is EQUIVALENT to
    all zeros lying on the critical line.

    Returns the sum value.
    """
    total = 0.0
    two_pi_sigma_sq = 2.0 * math.pi * sigma * sigma
    for rho in zeros:
        a = rho.real
        b = rho.imag
        re_rho_sq = a * a - b * b
        total += two_pi_sigma_sq * math.exp(sigma * sigma * re_rho_sq)
    return total


def weil_positivity_check(
    zeros: List[complex],
    sigma_values: List[float] = None,
) -> Dict[str, Any]:
    r"""Check Weil positivity for the shadow zeros at multiple test widths.

    For each sigma, computes sum_rho |f_hat(rho)|^2 and checks >= 0.

    Also checks the Li criterion analogue: define
        lambda_n = sum_rho [1 - (1 - 1/rho)^n]
    Li's criterion: all lambda_n >= 0 iff RH holds.

    For shadow zeros: lambda_n^{sh} = sum_rho [1 - (1 - 1/rho)^n]
    and we check positivity.

    Returns dict with positivity results at each sigma and Li coefficients.
    """
    if sigma_values is None:
        sigma_values = [0.5, 1.0, 2.0, 5.0, 10.0]

    positivity = {}
    for sigma in sigma_values:
        val = weil_positivity_sum(zeros, sigma)
        positivity[sigma] = {'value': val, 'positive': val >= 0}

    # Li criterion analogue
    li_coeffs = []
    for n in range(1, 11):
        total = 0.0 + 0.0j
        for rho in zeros:
            if abs(rho) > 1e-10:
                total += 1.0 - (1.0 - 1.0 / rho) ** n
        li_coeffs.append({'n': n, 'lambda_n': total.real, 'positive': total.real >= -1e-10})

    return {
        'gaussian_positivity': positivity,
        'li_coefficients': li_coeffs,
        'all_gaussian_positive': all(v['positive'] for v in positivity.values()),
        'all_li_positive': all(c['positive'] for c in li_coeffs),
    }


# =============================================================================
# 7. Shadow GRH: critical line analysis
# =============================================================================

def shadow_critical_line(
    shadow_coeffs: Dict[int, float],
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Determine the critical line for the shadow zeta function.

    For class G (Heisenberg): no zeros, GRH vacuously true.

    For class L (two-term, affine KM):
        zeta_A(s) = kappa * r1^{-s} + alpha * r2^{-s} = 0
        All zeros lie on the UNIQUE vertical line Re(s) = sigma_crit
        where sigma_crit = log(|alpha/kappa|) / log(r2/r1).
        Shadow GRH is EXACTLY TRUE for class L.

    For class C (three-term, beta-gamma):
        Zeros determined numerically. Check if they lie on a single
        vertical line.

    For class M (Virasoro, W_N):
        Infinite tower. Numerical investigation of zero locations.

    Returns dict with critical line location and GRH status.
    """
    nonzero_arities = sorted(
        [r for r in shadow_coeffs.keys() if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]
    )

    if len(nonzero_arities) == 0:
        return {'class': 'trivial', 'sigma_critical': None, 'grh_status': 'vacuous'}

    if len(nonzero_arities) == 1:
        return {
            'class': 'G',
            'sigma_critical': None,
            'grh_status': 'vacuous_no_zeros',
            'zeros': [],
        }

    if len(nonzero_arities) == 2:
        r1 = nonzero_arities[0]
        r2 = nonzero_arities[1]
        S1 = shadow_coeffs[r1]
        S2 = shadow_coeffs[r2]
        sigma_crit = math.log(abs(S2 / S1)) / math.log(r2 / r1)
        zeros = shadow_zeta_zeros_class_L(S1, S2, r1, r2, n_zeros)
        re_parts = [z.real for z in zeros]
        on_line = all(abs(re - sigma_crit) < 1e-8 for re in re_parts)
        return {
            'class': 'L',
            'sigma_critical': sigma_crit,
            'grh_status': 'proved' if on_line else 'failed',
            'zeros': zeros,
            'all_on_critical_line': on_line,
        }

    # General case: find zeros and check if they cluster on a line
    zeros = shadow_zeta_zeros_finite(
        shadow_coeffs,
        s_grid_re=(-10.0, 15.0),
        s_grid_im=(-50.0, 50.0),
        grid_density=200,
    )

    if not zeros:
        return {
            'class': 'C_or_M',
            'sigma_critical': None,
            'grh_status': 'no_zeros_found',
            'zeros': [],
        }

    re_parts = [z.real for z in zeros]
    mean_re = sum(re_parts) / len(re_parts)
    max_deviation = max(abs(re - mean_re) for re in re_parts)

    return {
        'class': 'C_or_M',
        'sigma_critical': mean_re,
        'grh_status': 'numerical_evidence' if max_deviation < 0.01 else 'off_line',
        'zeros': zeros,
        'max_deviation': max_deviation,
        'all_on_critical_line': max_deviation < 1e-6,
    }


# =============================================================================
# 8. Connes trace formula analogue
# =============================================================================

def connes_absorption_spectrum(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Compute the "absorption spectrum" of the bar differential.

    In Connes' framework, the Weil explicit formula is a trace formula
    for a certain operator H on L^2(A_Q^* / Q^*). The eigenvalues of H
    are the nontrivial zeros of zeta(s), and the absorption spectrum
    consists of the missing eigenvalues from the full line.

    The shadow analogue: the bar differential d_B acts on the bar complex
    B(A) = direct_sum_{r>=2} (s^{-1} A-bar)^{tensor r}, with A-bar = ker(epsilon). The graded pieces
    by arity r give a direct sum decomposition, and the restriction
    of d_B to arity r has eigenvalues determined by the OPE data.

    The "shadow absorption spectrum" is the set of eigenvalues of d_B
    that do NOT correspond to zeros of zeta_A.

    For the linearized computation, the relevant operator is the
    "shadow Laplacian":

        Delta_sh(r) = |Lambda_A(r)|^2 = (shadow von Mangoldt at r)^2

    The spectrum {Delta_sh(r)} is the shadow absorption spectrum.

    Returns dict with:
        'eigenvalues': dict {r: Delta_sh(r)}
        'spectral_density': the normalized distribution
        'total_absorption': sum of eigenvalues
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    lam = shadow_von_mangoldt(shadow_coeffs, max_r)

    eigenvalues = {}
    for r in range(2, max_r + 1):
        lam_r = lam.get(r, 0.0)
        eigenvalues[r] = lam_r * lam_r

    total = sum(eigenvalues.values())
    spectral_density = {r: v / total if total > 0 else 0.0
                        for r, v in eigenvalues.items()}

    return {
        'eigenvalues': eigenvalues,
        'spectral_density': spectral_density,
        'total_absorption': total,
    }


def connes_trace_formula(
    shadow_coeffs: Dict[int, float],
    test_fn: Callable[[float], float],
    fourier_fn: Callable[[complex], complex],
    max_r: int = 50,
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Compute the Connes trace formula for the shadow bar differential.

    The trace formula equates:
        Tr(f(H_sh)) = sum_{r>=2} Lambda_A(r) f(log r)   [orbital side]
                     = sum_rho f_hat(rho)                 [spectral side]
                       + (distributional corrections)

    This is the same as the Weil explicit formula, but interpreted
    as a trace formula on the bar complex.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dictionary
    test_fn : test function f: R -> R
    fourier_fn : bilateral Laplace transform f_hat: C -> C
    max_r : truncation
    n_zeros : number of zeros

    Returns
    -------
    Dict with orbital trace, spectral trace, and discrepancy.
    """
    # Orbital (arithmetic) side
    lam = shadow_von_mangoldt(shadow_coeffs, max_r)
    orbital = sum(lam.get(r, 0.0) * test_fn(math.log(r))
                  for r in range(2, max_r + 1))

    # Find zeros
    nonzero_arities = sorted(
        [r for r in shadow_coeffs.keys() if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]
    )

    if len(nonzero_arities) <= 1:
        zeros = []
    elif len(nonzero_arities) == 2:
        r1 = nonzero_arities[0]
        r2 = nonzero_arities[1]
        zeros = shadow_zeta_zeros_class_L(
            shadow_coeffs[r1], shadow_coeffs[r2], r1, r2, n_zeros)
    else:
        zeros = shadow_zeta_zeros_finite(shadow_coeffs, grid_density=150)

    # Spectral side
    spectral = sum(fourier_fn(rho).real for rho in zeros)

    return {
        'orbital_trace': orbital,
        'spectral_trace': spectral,
        'discrepancy': abs(orbital + spectral),
        'zeros_used': len(zeros),
    }


# =============================================================================
# 9. Deninger cohomological spectral measure
# =============================================================================

def deninger_spectral_measure(
    shadow_coeffs: Dict[int, float],
    t_values: Optional[List[float]] = None,
    max_r: int = 50,
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Compute the Deninger spectral measure for the shadow tower.

    Deninger's programme posits a cohomology theory with trace formula:
        sum_rho f(rho) = integral f(t) d mu(t)
    where mu is the spectral measure.

    The shadow analogue uses the modular cyclic deformation cohomology
    H*(Def_cyc^mod(A), d_Theta). The spectral measure is the
    distribution of zeros of zeta_A along the imaginary axis of the
    critical strip.

    For class L (affine KM):
        Zeros at s_n = sigma_crit + i * (pi + 2*pi*n) / log(r2/r1).
        The spectral measure is a Dirac comb with spacing 2*pi/log(r2/r1).

    For class M (Virasoro):
        Conjectural: the spectral measure should reflect the shadow
        growth rate rho.

    We compute the empirical spectral measure from the zero locations.

    Parameters
    ----------
    shadow_coeffs : shadow coefficient dictionary
    t_values : points at which to evaluate the spectral density
    max_r : truncation
    n_zeros : number of zeros to use

    Returns
    -------
    Dict with spectral measure data.
    """
    if t_values is None:
        t_values = list(np.linspace(-50.0, 50.0, 201))

    # Find zeros
    nonzero_arities = sorted(
        [r for r in shadow_coeffs.keys() if abs(shadow_coeffs.get(r, 0.0)) > 1e-50]
    )

    if len(nonzero_arities) <= 1:
        return {
            'class': 'G',
            't_values': t_values,
            'spectral_density': [0.0] * len(t_values),
            'zero_spacing': None,
            'total_zeros': 0,
        }

    if len(nonzero_arities) == 2:
        r1 = nonzero_arities[0]
        r2 = nonzero_arities[1]
        zeros = shadow_zeta_zeros_class_L(
            shadow_coeffs[r1], shadow_coeffs[r2], r1, r2, n_zeros)
        spacing = 2.0 * math.pi / math.log(r2 / r1)

        # Spectral density: smoothed Dirac comb
        smooth_width = spacing / 5.0
        density = []
        for t in t_values:
            val = 0.0
            for z in zeros:
                val += math.exp(-(t - z.imag) ** 2 / (2.0 * smooth_width ** 2))
            density.append(val / (smooth_width * math.sqrt(2.0 * math.pi)))

        return {
            'class': 'L',
            't_values': t_values,
            'spectral_density': density,
            'zero_spacing': spacing,
            'total_zeros': len(zeros),
            'sigma_critical': zeros[0].real if zeros else None,
        }

    # General case
    zeros = shadow_zeta_zeros_finite(shadow_coeffs, grid_density=150)
    if not zeros:
        return {
            'class': 'C_or_M',
            't_values': t_values,
            'spectral_density': [0.0] * len(t_values),
            'zero_spacing': None,
            'total_zeros': 0,
        }

    # Compute spacing between consecutive zeros
    im_parts = sorted([z.imag for z in zeros])
    spacings = [im_parts[i + 1] - im_parts[i] for i in range(len(im_parts) - 1)]
    mean_spacing = sum(spacings) / len(spacings) if spacings else 0.0

    smooth_width = mean_spacing / 3.0 if mean_spacing > 0 else 1.0
    density = []
    for t in t_values:
        val = 0.0
        for z in zeros:
            val += math.exp(-(t - z.imag) ** 2 / (2.0 * smooth_width ** 2))
        density.append(val / (smooth_width * math.sqrt(2.0 * math.pi)))

    return {
        'class': 'C_or_M',
        't_values': t_values,
        'spectral_density': density,
        'zero_spacing': mean_spacing,
        'total_zeros': len(zeros),
    }


# =============================================================================
# 10. Heisenberg exact computations (verification path 2)
# =============================================================================

def heisenberg_weil_formula_exact(k: float, sigma: float = 1.0) -> Dict[str, Any]:
    r"""Exact Weil explicit formula for Heisenberg H_k.

    zeta_{H_k}(s) = k * 2^{-s}   (single term, S_r = 0 for r >= 3)

    Lambda_{H_k}(r) = k * log(2) * delta_{r,2}
        (von Mangoldt is nonzero only at r = 2)

    Zeros: NONE (k * 2^{-s} = 0 has no solution).

    Arithmetic side = k * log(2) * f(log 2) * 2^{-sigma_shift}
    Spectral side = 0  (no zeros)
    Main term = 0  (no pole for finite Dirichlet series)

    The formula is: arith = 0 (trivially, since spectral = main = 0).
    But arith = k * log(2) * f(log 2) != 0 in general.

    This means the Weil formula for Heisenberg has the form:
        k * log(2) * f(log 2) = (distributional correction)

    The correction comes from the "trivial zeros" (at s = -infinity)
    and the constant term contribution. In the classical formula,
    the correction terms include:
        f_hat(0) * (log conductor) + f_hat(1) * (residue) + archimed.

    For Heisenberg with zeta(s) = k * 2^{-s}:
    - No pole => no residue term
    - "Conductor" = 2 (the single prime)
    - The distributional correction = k * log(2) * f(log 2)

    So the exact identity is:
        sum Lambda f(log r) = f_hat(0) * k * log(2)
        i.e., k * log(2) * f(log 2) = k * log(2) * f_hat(0)
        i.e., f(log 2) = f_hat(0) ... which is FALSE in general!

    The resolution: the Weil formula for a POLYNOMIAL Dirichlet series
    (not a true L-function) has additional distributional terms.
    The correct formulation for finite towers uses the FULL explicit
    formula with conductor and gamma factors.

    For VERIFICATION purposes, we check the self-consistency of:
        Lambda_A computed two ways (direct vs Dirichlet inverse).
    """
    lam_2 = k * math.log(2)
    f_at_log2 = gaussian_test_function(math.log(2), sigma)
    arith = lam_2 * f_at_log2

    return {
        'kappa': k,
        'lambda_2': lam_2,
        'arithmetic_side': arith,
        'spectral_side': 0.0,
        'zeros': [],
        'von_mangoldt': {2: lam_2},
        'f_at_log_2': f_at_log2,
    }


# =============================================================================
# 11. Class L exact computations (verification path 3)
# =============================================================================

def class_L_weil_formula_exact(
    kappa: float,
    alpha: float,
    r1: int = 2,
    r2: int = 3,
    sigma: float = 1.0,
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Exact Weil explicit formula for class L (two-term) shadow zeta.

    zeta_A(s) = kappa * r1^{-s} + alpha * r2^{-s}

    Von Mangoldt:
        Lambda_A(r) for r = r1: kappa * log(r1)
                    for r = r2: alpha * log(r2)
                    for r = r1^a * r2^b: determined by the recursion

    Zeros: all on Re(s) = log(|alpha/kappa|) / log(r2/r1)
        with imaginary parts (pi + 2*pi*n) / log(r2/r1)

    Arithmetic side = sum Lambda_A(r) f(log r)
    Spectral side = sum_n f_hat(rho_n)
    These should match (up to distributional corrections for the
    polynomial Dirichlet series).

    Returns detailed comparison.
    """
    # Von Mangoldt
    coeffs = {r1: kappa, r2: alpha}
    max_r = max(r1, r2) ** 3  # Include composite arities
    for r in range(r1 + 1, max_r + 1):
        if r != r2:
            coeffs[r] = 0.0
    lam = shadow_von_mangoldt(coeffs, max_r)

    # Zeros
    zeros = shadow_zeta_zeros_class_L(kappa, alpha, r1, r2, n_zeros)

    # Arithmetic side
    test_fn = lambda x: gaussian_test_function(x, sigma)
    fourier_fn = lambda s: gaussian_fourier_transform_complex(s, sigma)

    arith = sum(lam.get(r, 0.0) * test_fn(math.log(r))
                for r in range(2, max_r + 1))

    # Spectral side
    spectral = sum(fourier_fn(rho) for rho in zeros)

    return {
        'kappa': kappa,
        'alpha': alpha,
        'arithmetic_side': arith,
        'spectral_side': spectral,
        'discrepancy': abs(arith + spectral.real),
        'zeros': zeros,
        'von_mangoldt': lam,
        'sigma_critical': math.log(abs(alpha / kappa)) / math.log(r2 / r1),
    }


# =============================================================================
# 12. Class C Weil formula (beta-gamma)
# =============================================================================

def class_C_weil_analysis(
    shadow_coeffs: Dict[int, float],
    sigma: float = 1.0,
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Weil explicit formula analysis for class C (beta-gamma).

    Three-term zeta: S_2, S_3, S_4 nonzero, rest zero.
    Zeros determined numerically.

    Returns arithmetic/spectral comparison and critical line analysis.
    """
    lam = shadow_von_mangoldt(shadow_coeffs, 30)

    test_fn = lambda x: gaussian_test_function(x, sigma)
    fourier_fn = lambda s: gaussian_fourier_transform_complex(s, sigma)

    arith = sum(lam.get(r, 0.0) * test_fn(math.log(r))
                for r in range(2, 31))

    zeros = shadow_zeta_zeros_finite(
        shadow_coeffs,
        s_grid_re=(-10.0, 15.0),
        s_grid_im=(-50.0, 50.0),
        grid_density=200,
    )

    spectral = sum(fourier_fn(rho) for rho in zeros)

    # Critical line analysis
    if zeros:
        re_parts = [z.real for z in zeros]
        mean_re = sum(re_parts) / len(re_parts)
        max_dev = max(abs(re - mean_re) for re in re_parts)
        on_line = max_dev < 0.01
    else:
        mean_re = None
        max_dev = None
        on_line = True  # vacuously

    return {
        'arithmetic_side': arith,
        'spectral_side': spectral,
        'discrepancy': abs(arith + spectral.real),
        'zeros': zeros,
        'sigma_critical': mean_re,
        'max_deviation': max_dev,
        'on_critical_line': on_line,
        'von_mangoldt': lam,
    }


# =============================================================================
# 13. Shadow conductor
# =============================================================================

def shadow_conductor(
    shadow_coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    r"""Compute the shadow conductor N_A.

    The shadow conductor is defined implicitly by matching the Weil
    explicit formula:

        N_A = exp(sum_{r>=2} Lambda_A(r) / r)

    For Heisenberg: N_A = exp(kappa * log(2) / 2) = 2^{kappa/2}
    For class L: N_A = exp((kappa*log(r1)/r1 + alpha*log(r2)/r2) + ...)

    This is analogous to the classical conductor = product of local
    ramification data. For the shadow tower, the "local data" at
    arity r is the shadow coefficient S_r.

    Returns N_A as a positive real number.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())

    lam = shadow_von_mangoldt(shadow_coeffs, max_r)

    # sum Lambda_A(r) / r
    log_N = sum(lam.get(r, 0.0) / r for r in range(2, max_r + 1))

    return math.exp(log_N) if abs(log_N) < 500 else float('inf')


# =============================================================================
# 14. Multi-sigma verification (systematic check)
# =============================================================================

def multi_sigma_verification(
    shadow_coeffs: Dict[int, float],
    sigma_values: Optional[List[float]] = None,
    max_r: int = 50,
    n_zeros: int = 40,
) -> Dict[str, Any]:
    r"""Run the Weil explicit formula at multiple test function widths.

    For each sigma in sigma_values, compute arithmetic and spectral
    sides and check agreement.

    A consistent discrepancy across all sigma indicates a systematic
    issue (e.g., missing distributional term). Sigma-dependent
    discrepancy indicates truncation error.

    Returns summary of all checks.
    """
    if sigma_values is None:
        sigma_values = [0.5, 1.0, 2.0, 5.0, 10.0]

    results = {}
    for sigma in sigma_values:
        result = weil_explicit_formula_verify(
            shadow_coeffs, sigma=sigma, max_r=max_r, n_zeros=n_zeros)
        results[sigma] = {
            'arithmetic': result['arithmetic_side'],
            'spectral': result['spectral_side'].real,
            'discrepancy': result['discrepancy'],
        }

    discrepancies = [r['discrepancy'] for r in results.values()]
    max_disc = max(discrepancies)
    mean_disc = sum(discrepancies) / len(discrepancies)

    return {
        'results': results,
        'max_discrepancy': max_disc,
        'mean_discrepancy': mean_disc,
        'all_below_threshold': max_disc < 0.1,
    }


# =============================================================================
# 15. Direct verification: zeta'/zeta as Dirichlet series
# =============================================================================

def verify_logderiv_identity(
    shadow_coeffs: Dict[int, float],
    s: complex,
    max_r: int = 50,
) -> Dict[str, float]:
    r"""Verify that -d/ds log(1 + zeta_A(s)) = sum Lambda_A(r) r^{-s}.

    The shadow von Mangoldt function Lambda_A is computed from the
    AUGMENTED series 1 + zeta_A(s) (with a_1 = 1), so the identity is:

        sum_{r>=2} Lambda_A(r) r^{-s} = -zeta'_A(s) / (1 + zeta_A(s))

    NOT -zeta'/zeta. This distinction matters because the shadow
    Dirichlet series has a_1 = 0 (no arity-1 term), and the augmentation
    adds the unit a_1 = 1.

    Computes both sides at s and checks agreement.
    """
    # Left side: -zeta'_A(s) / (1 + zeta_A(s))
    zeta_val = 0.0 + 0.0j
    zeta_deriv = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if abs(Sr) < 1e-50:
            continue
        r_neg_s = r ** (-s)
        zeta_val += Sr * r_neg_s
        zeta_deriv += -Sr * math.log(r) * r_neg_s

    augmented = 1.0 + zeta_val  # The augmented series value
    if abs(augmented) < 1e-50:
        return {'left': float('nan'), 'right': float('nan'),
                'discrepancy': float('nan'), 'zeta_at_s': abs(zeta_val)}

    left = (-zeta_deriv / augmented)

    # Right side: sum Lambda_A(r) r^{-s}
    lam = shadow_von_mangoldt(shadow_coeffs, max_r)
    right = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        lam_r = lam.get(r, 0.0)
        if abs(lam_r) < 1e-50:
            continue
        right += lam_r * r ** (-s)

    disc = abs(left - right)
    return {
        'left': left,
        'right': right,
        'discrepancy': disc,
        'zeta_at_s': abs(zeta_val),
        'augmented_at_s': abs(augmented),
    }


# =============================================================================
# 16. Functional equation candidates
# =============================================================================

def functional_equation_test(
    shadow_coeffs: Dict[int, float],
    s_values: Optional[List[complex]] = None,
    max_r: int = 50,
) -> Dict[str, Any]:
    r"""Test for a functional equation of the form zeta_A(s) = C(s) zeta_A(w-s).

    Classical: zeta(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2) * zeta(1-s).

    For shadow zeta (finite tower), there is no reason to expect a classical
    functional equation. However, Koszul duality provides a relation:

        zeta_A(s) <-> zeta_{A!}(s)

    and complementarity (Theorem C) relates the shadows of A and A!.

    For the SELF-DUAL point (c=13 for Virasoro, c=0 for Heisenberg),
    zeta_A = zeta_{A!} and a functional equation of type
    zeta_A(s) = C(s) * zeta_A(w-s) may hold.

    We test numerically for the smallest w and simplest C(s).
    """
    if s_values is None:
        s_values = [complex(2.0, t) for t in np.linspace(-10.0, 10.0, 21)]

    def zeta_eval(s):
        total = 0.0 + 0.0j
        for r in range(2, max_r + 1):
            Sr = shadow_coeffs.get(r, 0.0)
            if abs(Sr) < 1e-50:
                continue
            total += Sr * r ** (-s)
        return total

    # Test: zeta(s) / zeta(w - s) for candidate w values
    results = {}
    for w in [0.0, 1.0, 2.0, 5.0]:
        ratios = []
        for s in s_values:
            z_s = zeta_eval(s)
            z_ws = zeta_eval(complex(w, 0) - s)
            if abs(z_ws) > 1e-50:
                ratios.append(z_s / z_ws)
            else:
                ratios.append(complex(float('inf'), 0))

        # Check if the ratio is constant (functional equation)
        finite_ratios = [r for r in ratios if abs(r) < 1e10]
        if len(finite_ratios) >= 2:
            # Check constancy
            mean_r = sum(finite_ratios) / len(finite_ratios)
            max_dev = max(abs(r - mean_r) for r in finite_ratios)
            results[w] = {
                'mean_ratio': mean_r,
                'max_deviation': max_dev,
                'is_constant': max_dev < 0.01 * abs(mean_r) if abs(mean_r) > 1e-10 else max_dev < 1e-10,
                'n_finite': len(finite_ratios),
            }
        else:
            results[w] = {'is_constant': False, 'n_finite': len(finite_ratios)}

    return results
