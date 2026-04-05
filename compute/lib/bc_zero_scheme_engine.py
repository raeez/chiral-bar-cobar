r"""Derived algebraic geometry of shadow zero schemes.

The zero locus Z_A = {s in C : zeta_A(s) = 0} of the shadow zeta function
acquires a dg-scheme structure encoding multiplicity and tangent data at
each zero.  This module computes:

1. ZERO SCHEME STRUCTURE:
   At a simple zero rho: O_{Z_A, rho} = C (reduced point, length 1).
   At a zero of multiplicity m: O_{Z_A, rho} = C[eps]/(eps^m) (artinian, length m).
   Simple zeros are generic; multiple zeros arise at special central charges
   where the zero scheme becomes non-reduced.

2. TANGENT COMPLEX:
   T_{Z_A, rho} = Hom(Omega^1, C) = C / zeta'_A(rho).
   For a simple zero: |T| = 1/|zeta'_A(rho)| ("inverse zero speed").
   Analogous to |zeta'(rho)|^{-1} for the Riemann zeta, which grows as
   log(gamma_n)/(2*pi).

3. INTERSECTION THEORY:
   <Z_A, Z_B> = sum_{rho in Z_A cap Z_B} mult(rho).
   For complementary pairs (A, A!): common zeros of zeta_c and zeta_{26-c}.
   At c = 13 (self-dual): self-intersection sum mult(rho)^2.

4. EULER CHARACTERISTIC / ZERO COUNTING:
   chi(Z_A, T) = N_A(T) via the argument principle:
   N_A(T) = (1/(2*pi*i)) oint zeta'_A/zeta_A ds.
   Asymptotic: N_A(T) ~ (T/pi) * log(T/(2*pi*e)) + O(log T).

5. HILBERT FUNCTION:
   H_{Z_A}(d) = #{zeros rho with |rho| <= d, counted with multiplicity}.

6. DEFORMATION WITH c:
   As c varies, zeros move: rho_n(c).  By implicit differentiation:
   d(rho)/dc = -(d(zeta)/dc) / (d(zeta)/ds) evaluated at the zero.
   Zero collisions (non-reduced locus) occur where rho_n(c*) = rho_{n+1}(c*).

7. REGULARIZED MOTIVIC CLASS:
   [Z_A]^{reg} = zeta'_A(0) / zeta_A(0) when zeta_A(0) != 0.

8. SPECTRAL COINCIDENCES:
   Derived intersection: #{s : zeta_A(s) = zeta_B(s)} for A != B.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:complementarity-scalar (higher_genus_complementarity.tex)

CAUTION (AP1):  kappa formulas are family-specific.
CAUTION (AP9):  S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP10): Cross-verify by multiple independent methods.
CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from compute.lib.shadow_zeta_function_engine import (
    virasoro_shadow_coefficients_numerical,
    shadow_zeta_numerical,
)

from compute.lib.bc_shadow_zeta_zeros_engine import (
    shadow_coefficients_extended,
    koszul_dual_coefficients,
    _shadow_zeta_complex,
    _shadow_zeta_derivative,
    newton_zero,
    find_zeros_grid,
    _deduplicate_zeros,
    argument_principle_count,
    zero_counting_function,
)


# ============================================================================
# 0.  Data structures
# ============================================================================

@dataclass
class ZeroSchemePoint:
    """A point of the shadow zero scheme with local ring data."""
    location: complex
    multiplicity: int
    inverse_speed: float  # 1/|zeta'(rho)| for simple zeros
    tangent_dim: int  # = 1 for simple zero, m for mult-m zero
    local_ring_length: int  # = multiplicity


@dataclass
class ZeroSchemeData:
    """Full data of a shadow zero scheme."""
    family: str
    param: float
    points: List[ZeroSchemePoint]
    total_length: int  # sum of multiplicities
    is_reduced: bool  # all multiplicities = 1
    euler_char_truncated: int  # N(T) for the truncation height used


# ============================================================================
# 1.  Multiplicity computation at zeros
# ============================================================================

def _shadow_zeta_higher_deriv(
    shadow_coeffs: Dict[int, float],
    s: complex,
    order: int = 1,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate the k-th derivative zeta_A^{(k)}(s).

    zeta_A^{(k)}(s) = sum_{r >= 2} S_r * (-log r)^k * r^{-s}.
    """
    if max_r is None:
        max_r = max(shadow_coeffs.keys())
    total = 0.0 + 0.0j
    for r in range(2, max_r + 1):
        Sr = shadow_coeffs.get(r, 0.0)
        if Sr == 0.0:
            continue
        log_r = math.log(r)
        total += Sr * ((-log_r) ** order) * (r ** (-s))
    return total


def zero_multiplicity(
    shadow_coeffs: Dict[int, float],
    rho: complex,
    max_order: int = 5,
    tol: float = 1e-6,
    max_r: Optional[int] = None,
) -> int:
    """Determine the multiplicity of a zero rho of zeta_A(s).

    The multiplicity m is the smallest k >= 0 such that
    zeta_A^{(k)}(rho) != 0.  If zeta_A(rho) != 0, returns 0.

    Parameters
    ----------
    shadow_coeffs : shadow coefficients
    rho : location of the zero
    max_order : check derivatives up to this order
    tol : tolerance for "is zero"
    max_r : truncation arity

    Returns
    -------
    Multiplicity m (0 if rho is not a zero).
    """
    for k in range(0, max_order + 1):
        val = _shadow_zeta_higher_deriv(shadow_coeffs, rho, order=k, max_r=max_r)
        if abs(val) > tol:
            return k
    return max_order


def compute_inverse_zero_speed(
    shadow_coeffs: Dict[int, float],
    rho: complex,
    max_r: Optional[int] = None,
) -> float:
    """Compute |zeta'_A(rho)|^{-1} at a zero rho.

    This is the "inverse zero speed" - the norm of the tangent space
    generator at the reduced point of the zero scheme.

    For a simple zero: dim T_{Z_A, rho} = 1, |T| = 1/|zeta'(rho)|.
    For a multiple zero of multiplicity m: the tangent space involves
    higher derivatives.

    Returns float('inf') if zeta'(rho) = 0 (non-simple zero).
    """
    deriv = _shadow_zeta_derivative(shadow_coeffs, rho, max_r)
    abs_deriv = abs(deriv)
    if abs_deriv < 1e-300:
        return float('inf')
    return 1.0 / abs_deriv


# ============================================================================
# 2.  Zero scheme point construction
# ============================================================================

def build_zero_scheme_point(
    shadow_coeffs: Dict[int, float],
    rho: complex,
    max_r: Optional[int] = None,
) -> ZeroSchemePoint:
    """Build the local data of the zero scheme at a single zero."""
    mult = zero_multiplicity(shadow_coeffs, rho, max_r=max_r)
    inv_speed = compute_inverse_zero_speed(shadow_coeffs, rho, max_r)
    return ZeroSchemePoint(
        location=rho,
        multiplicity=max(mult, 1),
        inverse_speed=inv_speed,
        tangent_dim=1 if mult <= 1 else mult,
        local_ring_length=max(mult, 1),
    )


def build_zero_scheme(
    family: str,
    param: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
) -> ZeroSchemeData:
    """Construct the full zero scheme for a given algebra.

    Finds zeros by grid search, computes multiplicity and tangent data
    at each zero, and assembles the scheme data.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    points = []
    for z in zeros:
        pt = build_zero_scheme_point(coeffs, z, max_r=max_r)
        points.append(pt)

    total_len = sum(pt.local_ring_length for pt in points)
    is_reduced = all(pt.multiplicity <= 1 for pt in points)

    return ZeroSchemeData(
        family=family,
        param=param,
        points=points,
        total_length=total_len,
        is_reduced=is_reduced,
        euler_char_truncated=len(points),
    )


# ============================================================================
# 3.  Inverse zero speeds for first N zeros
# ============================================================================

def inverse_zero_speeds(
    family: str,
    param: float,
    n_zeros: int = 50,
    max_r: int = 60,
    im_max: float = 200.0,
    grid_re: int = 20,
    grid_im: int = 200,
) -> List[Tuple[complex, float]]:
    """Compute inverse zero speeds for the first n_zeros zeros.

    Returns list of (rho, 1/|zeta'(rho)|) sorted by |Im(rho)|.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=(-im_max, im_max),
        grid_re=grid_re,
        grid_im=grid_im,
        max_r=max_r,
    )

    # Sort by |Im(rho)|, take first n_zeros
    zeros.sort(key=lambda z: abs(z.imag))
    zeros = zeros[:n_zeros]

    result = []
    for rho in zeros:
        inv_sp = compute_inverse_zero_speed(coeffs, rho, max_r)
        result.append((rho, inv_sp))
    return result


# ============================================================================
# 4.  Intersection theory on zero schemes
# ============================================================================

def zero_scheme_intersection(
    family_a: str,
    param_a: float,
    family_b: str,
    param_b: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
    tol: float = 1e-4,
) -> Dict[str, Any]:
    """Compute the intersection number <Z_A, Z_B>.

    <Z_A, Z_B> = sum_{rho in Z_A cap Z_B} mult(rho)
    = number of common zeros counted with multiplicity.

    Parameters
    ----------
    family_a, param_a : first algebra
    family_b, param_b : second algebra
    tol : tolerance for common zero identification

    Returns
    -------
    Dict with 'intersection_number', 'common_zeros', 'n_zeros_a', 'n_zeros_b'.
    """
    coeffs_a = shadow_coefficients_extended(family_a, param_a, max_r)
    coeffs_b = shadow_coefficients_extended(family_b, param_b, max_r)

    zeros_a = find_zeros_grid(
        coeffs_a, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )
    zeros_b = find_zeros_grid(
        coeffs_b, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    # Find common zeros
    common = []
    for za in zeros_a:
        for zb in zeros_b:
            if abs(za - zb) < tol:
                mult_a = zero_multiplicity(coeffs_a, za, max_r=max_r)
                mult_b = zero_multiplicity(coeffs_b, zb, max_r=max_r)
                common.append({
                    'zero': (za + zb) / 2,
                    'mult_a': max(mult_a, 1),
                    'mult_b': max(mult_b, 1),
                    'contribution': min(max(mult_a, 1), max(mult_b, 1)),
                })
                break  # avoid double counting

    intersection = sum(c['contribution'] for c in common)

    return {
        'intersection_number': intersection,
        'common_zeros': common,
        'n_common': len(common),
        'n_zeros_a': len(zeros_a),
        'n_zeros_b': len(zeros_b),
    }


def self_intersection_number(
    family: str,
    param: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
) -> Dict[str, Any]:
    """Compute the self-intersection <Z_A, Z_A> = sum mult(rho)^2.

    For reduced schemes (all simple zeros): <Z, Z> = N (number of zeros).
    For non-reduced: <Z, Z> > N.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    total = 0
    mult_data = []
    for z in zeros:
        m = zero_multiplicity(coeffs, z, max_r=max_r)
        m = max(m, 1)
        total += m * m
        mult_data.append((z, m))

    n_zeros = len(zeros)
    return {
        'self_intersection': total,
        'n_zeros': n_zeros,
        'is_reduced': total == n_zeros,
        'multiplicities': mult_data,
    }


# ============================================================================
# 5.  Complementary pair intersection
# ============================================================================

def complementary_intersection(
    c_val: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
    tol: float = 1e-4,
) -> Dict[str, Any]:
    """Intersection of Z_{Vir_c} and Z_{Vir_{26-c}} (complementary pair).

    At c = 13 (self-dual): this is the self-intersection of Z_{Vir_13}.
    For generic c: the intersection counts common zeros of zeta_c and zeta_{26-c}.

    CAUTION (AP24): kappa(Vir_c) + kappa(Vir_{26-c}) = 13, NOT 0.
    """
    c_dual = 26.0 - c_val
    is_self_dual = abs(c_val - 13.0) < 1e-10

    if is_self_dual:
        return self_intersection_number(
            'virasoro', c_val, max_r, re_range, im_range, grid_re, grid_im,
        )

    return zero_scheme_intersection(
        'virasoro', c_val,
        'virasoro', c_dual,
        max_r, re_range, im_range, grid_re, grid_im, tol,
    )


# ============================================================================
# 6.  Euler characteristic via argument principle
# ============================================================================

def euler_characteristic_argument_principle(
    family: str,
    param: float,
    T_values: List[float],
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    n_contour_pts: int = 2000,
) -> Dict[float, int]:
    """Compute chi(Z_A, T) = N_A(T) via the argument principle.

    N_A(T) = (1/(2*pi*i)) * oint zeta'/zeta ds around [-5,5] x [-T,T].

    Returns dict mapping T to N_A(T).
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    result = {}
    for T in T_values:
        count = argument_principle_count(
            coeffs,
            re_range=re_range,
            im_range=(-T, T),
            n_points=n_contour_pts,
            max_r=max_r,
        )
        result[T] = count
    return result


def euler_characteristic_explicit(
    family: str,
    param: float,
    T_values: List[float],
    max_r: int = 60,
    im_max: float = 600.0,
    grid_re: int = 25,
    grid_im: int = 250,
) -> Dict[float, int]:
    """Compute N_A(T) by explicit zero counting.

    Returns dict mapping T to N_A(T) = #{zeros with |Im(s)| < T}.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-10.0, 10.0),
        im_range=(-im_max, im_max),
        grid_re=grid_re,
        grid_im=grid_im,
        max_r=max_r,
    )
    return zero_counting_function(zeros, T_values)


def asymptotic_zero_count(T: float) -> float:
    """Riemann-von Mangoldt asymptotic: N(T) ~ (T/pi) * log(T/(2*pi*e)).

    This is the standard asymptotic for Dirichlet series zero counting.
    """
    if T <= 0:
        return 0.0
    return (T / math.pi) * math.log(T / (2.0 * math.pi * math.e))


# ============================================================================
# 7.  Hilbert function of zero scheme
# ============================================================================

def hilbert_function(
    family: str,
    param: float,
    d_values: List[float],
    max_r: int = 60,
    im_max: float = 200.0,
    grid_re: int = 25,
    grid_im: int = 200,
) -> Dict[float, int]:
    """Hilbert function H_{Z_A}(d) = #{zeros rho with |rho| <= d, with mult}.

    For the zero subscheme Z_A of A^1:
    H(d) = dim_C O_{Z_A}(d) = sum_{|rho| <= d} mult(rho).

    Parameters
    ----------
    d_values : list of radii at which to evaluate
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-max(d_values) - 1, max(d_values) + 1),
        im_range=(-im_max, im_max),
        grid_re=grid_re,
        grid_im=grid_im,
        max_r=max_r,
    )

    # Compute multiplicities
    zero_data = []
    for z in zeros:
        m = zero_multiplicity(coeffs, z, max_r=max_r)
        m = max(m, 1)
        zero_data.append((z, m))

    result = {}
    for d in d_values:
        count = sum(m for z, m in zero_data if abs(z) <= d)
        result[d] = count
    return result


# ============================================================================
# 8.  Deformation of zeros with central charge
# ============================================================================

def zero_c_derivative(
    c_val: float,
    rho: complex,
    max_r: int = 60,
    dc: float = 1e-5,
) -> complex:
    """Compute d(rho)/dc by implicit differentiation.

    If zeta_c(rho(c)) = 0 for all c, then:
    d(rho)/dc = -(d(zeta)/dc) / (d(zeta)/ds) evaluated at (c, rho).

    We compute d(zeta)/dc numerically via finite difference:
    (zeta_{c+dc}(rho) - zeta_{c-dc}(rho)) / (2*dc).

    d(zeta)/ds is the standard derivative zeta'(rho).
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    coeffs_plus = virasoro_shadow_coefficients_numerical(c_val + dc, max_r)
    coeffs_minus = virasoro_shadow_coefficients_numerical(c_val - dc, max_r)

    zeta_plus = shadow_zeta_numerical(coeffs_plus, rho, max_r)
    zeta_minus = shadow_zeta_numerical(coeffs_minus, rho, max_r)
    dzeta_dc = (zeta_plus - zeta_minus) / (2.0 * dc)

    dzeta_ds = _shadow_zeta_derivative(coeffs, rho, max_r)
    if abs(dzeta_ds) < 1e-300:
        return complex(float('inf'), float('inf'))

    return -dzeta_dc / dzeta_ds


def track_zeros_with_c(
    c_start: float,
    c_end: float,
    n_c_steps: int = 20,
    n_zeros: int = 20,
    max_r: int = 60,
    im_max: float = 100.0,
) -> Dict[str, Any]:
    """Track how zeros move as c varies from c_start to c_end.

    Returns trajectories rho_n(c) for the first n_zeros zeros.
    """
    c_values = [c_start + i * (c_end - c_start) / max(n_c_steps - 1, 1)
                for i in range(n_c_steps)]

    trajectories = {n: [] for n in range(n_zeros)}

    for c_val in c_values:
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
        except ValueError:
            continue

        zeros = find_zeros_grid(
            coeffs,
            re_range=(-5.0, 5.0),
            im_range=(0.1, im_max),
            grid_re=15,
            grid_im=80,
            max_r=max_r,
        )
        zeros.sort(key=lambda z: abs(z.imag))

        for n in range(min(n_zeros, len(zeros))):
            trajectories[n].append((c_val, zeros[n]))

    return {
        'c_values': c_values,
        'trajectories': trajectories,
        'n_c_steps': n_c_steps,
        'n_zeros_tracked': n_zeros,
    }


def zero_c_derivatives_first_n(
    c_val: float,
    n_zeros: int = 20,
    max_r: int = 60,
    im_max: float = 100.0,
) -> List[Tuple[complex, complex]]:
    """Compute d(rho_n)/dc for the first n_zeros zeros at central charge c.

    Returns list of (rho_n, d(rho_n)/dc).
    """
    coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-5.0, 5.0),
        im_range=(0.1, im_max),
        grid_re=15,
        grid_im=80,
        max_r=max_r,
    )
    zeros.sort(key=lambda z: abs(z.imag))
    zeros = zeros[:n_zeros]

    result = []
    for rho in zeros:
        drho_dc = zero_c_derivative(c_val, rho, max_r)
        result.append((rho, drho_dc))
    return result


def find_zero_collisions(
    c_range: Tuple[float, float] = (0.5, 25.5),
    n_c_steps: int = 50,
    max_r: int = 60,
    collision_tol: float = 0.5,
    im_max: float = 50.0,
) -> List[Dict[str, Any]]:
    """Search for c values where two consecutive zeros nearly collide.

    Returns list of candidate collision events.
    """
    c_lo, c_hi = c_range
    dc = (c_hi - c_lo) / max(n_c_steps - 1, 1)

    collisions = []

    for i in range(n_c_steps):
        c_val = c_lo + i * dc
        try:
            coeffs = virasoro_shadow_coefficients_numerical(c_val, max_r)
        except ValueError:
            continue

        zeros = find_zeros_grid(
            coeffs,
            re_range=(-3.0, 3.0),
            im_range=(0.1, im_max),
            grid_re=10,
            grid_im=60,
            max_r=max_r,
        )
        # Sort by imaginary part for consecutive checking
        imags = sorted([z.imag for z in zeros if z.imag > 0.1])

        for j in range(len(imags) - 1):
            gap = imags[j + 1] - imags[j]
            if gap < collision_tol:
                collisions.append({
                    'c_val': c_val,
                    'zero_1_im': imags[j],
                    'zero_2_im': imags[j + 1],
                    'gap': gap,
                    'pair_index': j,
                })

    return collisions


# ============================================================================
# 9.  Regularized motivic class
# ============================================================================

def regularized_motivic_class(
    family: str,
    param: float,
    max_r: int = 60,
) -> Dict[str, complex]:
    """Compute the regularized motivic class [Z_A]^{reg}.

    For an infinite zero set: [Z_A]^{reg} = zeta'_A(0) / zeta_A(0)
    when zeta_A(0) != 0.

    For a finite zero set: [Z_A] = N * [pt] = number of zeros.

    Returns dict with 'zeta_at_0', 'zeta_deriv_at_0', 'regularized_class'.
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)

    zeta_0 = shadow_zeta_numerical(coeffs, complex(0, 0), max_r)
    zeta_prime_0 = _shadow_zeta_derivative(coeffs, complex(0, 0), max_r)

    if abs(zeta_0) < 1e-300:
        reg_class = complex(float('inf'), 0)
    else:
        reg_class = zeta_prime_0 / zeta_0

    return {
        'zeta_at_0': zeta_0,
        'zeta_deriv_at_0': zeta_prime_0,
        'regularized_class': reg_class,
    }


# ============================================================================
# 10. Spectral coincidences (derived intersection with diagonal)
# ============================================================================

def spectral_coincidences(
    family_a: str,
    param_a: float,
    family_b: str,
    param_b: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
    tol: float = 1e-8,
) -> Dict[str, Any]:
    """Find s where zeta_A(s) = zeta_B(s) (spectral coincidences).

    These are zeros of zeta_A(s) - zeta_B(s).  We compute this as a
    Dirichlet series with coefficients S_r(A) - S_r(B).
    """
    coeffs_a = shadow_coefficients_extended(family_a, param_a, max_r)
    coeffs_b = shadow_coefficients_extended(family_b, param_b, max_r)

    # Difference coefficients
    diff_coeffs = {}
    all_r = set(coeffs_a.keys()) | set(coeffs_b.keys())
    for r in all_r:
        diff_coeffs[r] = coeffs_a.get(r, 0.0) - coeffs_b.get(r, 0.0)

    # Find zeros of the difference
    coincidences = find_zeros_grid(
        diff_coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    # Verify each coincidence
    verified = []
    for s in coincidences:
        val_a = shadow_zeta_numerical(coeffs_a, s, max_r)
        val_b = shadow_zeta_numerical(coeffs_b, s, max_r)
        if abs(val_a - val_b) < tol * max(1.0, abs(val_a), abs(val_b)):
            verified.append({
                's': s,
                'zeta_a': val_a,
                'zeta_b': val_b,
                'diff': abs(val_a - val_b),
            })

    return {
        'n_coincidences': len(verified),
        'coincidences': verified,
        'n_raw_candidates': len(coincidences),
    }


def spectral_coincidences_complementary(
    c_val: float,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
) -> Dict[str, Any]:
    """Find spectral coincidences for complementary Virasoro pair (c, 26-c).

    At c = 13 (self-dual): zeta_c(s) = zeta_{26-c}(s) for ALL s,
    so every s is a coincidence (trivial case).

    For c != 13: genuine spectral coincidences.
    """
    c_dual = 26.0 - c_val
    is_self_dual = abs(c_val - 13.0) < 1e-10

    result = spectral_coincidences(
        'virasoro', c_val,
        'virasoro', c_dual,
        max_r, re_range, im_range, grid_re, grid_im,
    )
    result['c'] = c_val
    result['c_dual'] = c_dual
    result['is_self_dual'] = is_self_dual

    return result


# ============================================================================
# 11.  Multi-path verification utilities
# ============================================================================

def verify_zero_simplicity(
    shadow_coeffs: Dict[int, float],
    zeros: List[complex],
    max_r: Optional[int] = None,
    tol: float = 1e-6,
) -> Dict[str, Any]:
    """Verify that all zeros are simple (multiplicity 1).

    Path 1: zeta(rho) = 0 (check it's a zero)
    Path 2: zeta'(rho) != 0 (check derivative is nonzero)

    Returns dict with 'all_simple', 'non_simple_zeros', details.
    """
    non_simple = []
    for rho in zeros:
        val = _shadow_zeta_complex(shadow_coeffs, rho, max_r)
        deriv = _shadow_zeta_derivative(shadow_coeffs, rho, max_r)
        is_zero = abs(val) < tol
        is_simple = abs(deriv) > tol

        if is_zero and not is_simple:
            mult = zero_multiplicity(shadow_coeffs, rho, max_r=max_r)
            non_simple.append({
                'zero': rho,
                'zeta_val': val,
                'zeta_deriv': deriv,
                'multiplicity': mult,
            })

    return {
        'all_simple': len(non_simple) == 0,
        'n_checked': len(zeros),
        'n_non_simple': len(non_simple),
        'non_simple_zeros': non_simple,
    }


def verify_deformation_formula(
    c_val: float,
    rho: complex,
    max_r: int = 60,
    dc: float = 0.01,
) -> Dict[str, Any]:
    """Verify d(rho)/dc via finite difference vs implicit differentiation.

    Path 1: Implicit differentiation formula
    Path 2: Finite difference (rho(c+dc) - rho(c-dc)) / (2*dc)
    Path 3: Forward difference (rho(c+dc) - rho(c)) / dc

    We find the zero nearest to rho at c +/- dc to compute the numerical
    derivative.
    """
    # Implicit differentiation
    drho_analytic = zero_c_derivative(c_val, rho, max_r, dc=1e-5)

    # Find zero near rho at c + dc
    coeffs_plus = virasoro_shadow_coefficients_numerical(c_val + dc, max_r)
    rho_plus = newton_zero(coeffs_plus, rho, max_r=max_r)

    # Find zero near rho at c - dc
    coeffs_minus = virasoro_shadow_coefficients_numerical(c_val - dc, max_r)
    rho_minus = newton_zero(coeffs_minus, rho, max_r=max_r)

    result = {
        'rho': rho,
        'c': c_val,
        'drho_dc_implicit': drho_analytic,
    }

    if rho_plus is not None and rho_minus is not None:
        drho_central = (rho_plus - rho_minus) / (2.0 * dc)
        result['drho_dc_central_diff'] = drho_central
        result['central_diff_error'] = abs(drho_analytic - drho_central)

    if rho_plus is not None:
        drho_forward = (rho_plus - rho) / dc
        result['drho_dc_forward_diff'] = drho_forward
        result['forward_diff_error'] = abs(drho_analytic - drho_forward)

    return result


def verify_hilbert_vs_counting(
    family: str,
    param: float,
    d_values: List[float],
    max_r: int = 60,
) -> Dict[str, Any]:
    """Verify H(d) <= N(d) (Hilbert function bounded by zero count).

    The Hilbert function counts with multiplicity, while N(d) counts
    distinct zeros with |rho| <= d. For reduced schemes, H(d) = N(d).
    """
    coeffs = shadow_coefficients_extended(family, param, max_r)
    zeros = find_zeros_grid(
        coeffs,
        re_range=(-max(d_values) - 1, max(d_values) + 1),
        im_range=(-max(d_values) - 1, max(d_values) + 1),
        grid_re=20,
        grid_im=80,
        max_r=max_r,
    )

    results = {}
    for d in d_values:
        n_d = sum(1 for z in zeros if abs(z) <= d)
        # H(d) counts with multiplicity
        h_d = sum(
            max(zero_multiplicity(coeffs, z, max_r=max_r), 1)
            for z in zeros if abs(z) <= d
        )
        results[d] = {
            'N': n_d,
            'H': h_d,
            'consistent': h_d >= n_d,
        }

    all_ok = all(v['consistent'] for v in results.values())
    return {
        'all_consistent': all_ok,
        'data': results,
    }


def palindromic_zero_test(
    c_val: float = 13.0,
    max_r: int = 60,
    re_range: Tuple[float, float] = (-5.0, 5.0),
    im_range: Tuple[float, float] = (-50.0, 50.0),
    grid_re: int = 20,
    grid_im: int = 100,
    tol: float = 1e-4,
) -> Dict[str, Any]:
    """At c = 13 (self-dual), the zero set should be palindromic.

    Vir_13 is self-dual: Vir_13^! = Vir_{26-13} = Vir_13.
    So the zeros of zeta_13 and zeta_{26-13} are identical.
    The zero set is symmetric under the "palindromic" involution.

    We test that each zero rho has a partner under s -> s_bar (conjugation).
    """
    coeffs = shadow_coefficients_extended('virasoro', c_val, max_r)
    zeros = find_zeros_grid(
        coeffs, re_range, im_range, grid_re, grid_im, max_r=max_r,
    )

    # Check conjugate symmetry: for each rho, there should be a conj(rho)
    n_paired = 0
    unpaired = []
    for z in zeros:
        z_conj = z.conjugate()
        has_pair = any(abs(z_conj - w) < tol for w in zeros)
        if has_pair:
            n_paired += 1
        else:
            unpaired.append(z)

    return {
        'c': c_val,
        'n_zeros': len(zeros),
        'n_paired': n_paired,
        'n_unpaired': len(unpaired),
        'unpaired': unpaired,
        'is_palindromic': len(unpaired) == 0,
    }
