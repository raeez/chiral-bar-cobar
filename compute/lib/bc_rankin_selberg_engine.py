r"""bc_rankin_selberg_engine.py -- Rankin-Selberg convolution for shadow zeta functions.

BC-73: For two modular Koszul algebras A, B with shadow zeta functions
    zeta_A(s) = sum_{r >= 2} S_r(A) * r^{-s},
    zeta_B(s) = sum_{r >= 2} S_r(B) * r^{-s},
define the RANKIN-SELBERG CONVOLUTION:

    L(s, zeta_A x zeta_B) = sum_{r >= 2} S_r(A) * S_r(B) * r^{-s}

This is the Dirichlet series of POINTWISE PRODUCTS of shadow coefficients.
In classical number theory, L(s, f x g) controls the inner product of
automorphic forms and governs non-vanishing on Re(s) = 1.

COMPUTATIONS:

1. Self-convolution L(s, zeta_A x zeta_A) = sum S_r(A)^2 r^{-s}.
   Petersson norm: L(1, zeta_A x zeta_A) = sum S_r^2 / r.
   Zeros vs zeros of zeta_A (should NOT coincide in general).

2. Complementarity convolution L(s, zeta_A x zeta_{A!}).
   For Virasoro: A! = Vir_{26-c}, so L(s, zeta_c x zeta_{26-c}).
   At self-dual c=13: equals self-convolution.

3. Cross-family convolution: e.g. L(s, zeta_Vir x zeta_{sl_2}).
   For class L x class M: result is class L (finite Dirichlet polynomial).
   For class G x class M: single-term polynomial.

4. Shadow Petersson inner product: <zeta_A, zeta_B>_RS = L(1, zeta_A x zeta_B).
   Inner product matrix for standard families.

5. Symmetric square: L(s, Sym^2 zeta_A) via Dirichlet convolution of
   multiplicative structure.  Coefficients: C_r(Sym^2) = sum_{d|r} S_d * S_{r/d}
   (over divisors, but shadow towers are NOT multiplicative in general --
   this is the FORMAL symmetric square, distinct from the literal Sym^2
   L-function of a modular form).

6. Exterior square: L(s, wedge^2 zeta_A), the antisymmetric part.

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general.
CAUTION (AP10): Never hardcode wrong expected values in tests.
CAUTION (AP24): kappa + kappa' = 0 for KM, = 13 for Virasoro.
CAUTION (AP39): kappa != c/2 for non-Virasoro families.
CAUTION (AP48): kappa depends on the full algebra, not just the Virasoro sub.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    def:shadow-algebra (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:operadic-rankin-selberg (arithmetic_shadows.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple

from compute.lib.shadow_zeta_function_engine import (
    virasoro_shadow_coefficients_numerical,
    affine_sl2_shadow_coefficients,
    affine_sl3_shadow_coefficients,
    heisenberg_shadow_coefficients,
    betagamma_shadow_coefficients,
    shadow_zeta_numerical,
    shadow_growth_rate_from_coeffs,
    abscissa_of_convergence,
    virasoro_growth_rate_exact,
)


# ============================================================================
# 1.  Shadow coefficient providers
# ============================================================================

def get_virasoro_coeffs(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Virasoro shadow coefficients at central charge c."""
    return virasoro_shadow_coefficients_numerical(c_val, max_r)


def get_koszul_dual_virasoro_coeffs(c_val: float, max_r: int = 50) -> Dict[int, float]:
    """Koszul dual Virasoro: Vir_{26-c} shadow coefficients.

    The Koszul duality c -> 26 - c is the Feigin-Frenkel-type involution
    for Virasoro.  NOT anti-symmetric: kappa(c) + kappa(26-c) = 13 (AP24).
    """
    return virasoro_shadow_coefficients_numerical(26.0 - c_val, max_r)


def get_heisenberg_coeffs(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Heisenberg shadow coefficients at level k."""
    return heisenberg_shadow_coefficients(k_val, max_r)


def get_affine_sl2_coeffs(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Affine sl_2 shadow coefficients at level k."""
    return affine_sl2_shadow_coefficients(k_val, max_r)


def get_affine_sl3_coeffs(k_val: float, max_r: int = 50) -> Dict[int, float]:
    """Affine sl_3 shadow coefficients at level k."""
    return affine_sl3_shadow_coefficients(k_val, max_r)


def get_betagamma_coeffs(lam_val: float = 0.5, max_r: int = 50) -> Dict[int, float]:
    """Beta-gamma shadow coefficients at weight lambda."""
    return betagamma_shadow_coefficients(lam_val, max_r)


# ============================================================================
# 2.  Rankin-Selberg convolution: L(s, zeta_A x zeta_B)
# ============================================================================

def rankin_selberg_coefficients(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
) -> Dict[int, float]:
    """Pointwise product coefficients: RS_r = S_r(A) * S_r(B).

    These are the Dirichlet coefficients of L(s, zeta_A x zeta_B).
    """
    min_r = max(min(coeffs_A.keys()), min(coeffs_B.keys()))
    max_r = min(max(coeffs_A.keys()), max(coeffs_B.keys()))
    result = {}
    for r in range(min_r, max_r + 1):
        sa = coeffs_A.get(r, 0.0)
        sb = coeffs_B.get(r, 0.0)
        result[r] = sa * sb
    return result


def rankin_selberg_L(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Evaluate L(s, zeta_A x zeta_B) = sum_{r >= 2} S_r(A) * S_r(B) * r^{-s}.

    Direct summation of the pointwise product Dirichlet series.
    """
    rs_coeffs = rankin_selberg_coefficients(coeffs_A, coeffs_B)
    if max_r is not None:
        rs_coeffs = {r: v for r, v in rs_coeffs.items() if r <= max_r}
    return shadow_zeta_numerical(rs_coeffs, s, max_r=max(rs_coeffs.keys()) if rs_coeffs else 2)


def self_convolution_L(
    coeffs: Dict[int, float],
    s: complex,
    max_r: Optional[int] = None,
) -> complex:
    """Self-convolution: L(s, zeta_A x zeta_A) = sum S_r^2 * r^{-s}."""
    return rankin_selberg_L(coeffs, coeffs, s, max_r)


def complementarity_convolution_L(
    c_val: float,
    s: complex,
    max_r: int = 50,
) -> complex:
    """Complementarity convolution for Virasoro: L(s, zeta_c x zeta_{26-c}).

    At c = 13 (self-dual point): equals self-convolution L(s, zeta_13 x zeta_13).
    """
    coeffs_A = get_virasoro_coeffs(c_val, max_r)
    coeffs_B = get_koszul_dual_virasoro_coeffs(c_val, max_r)
    return rankin_selberg_L(coeffs_A, coeffs_B, s)


# ============================================================================
# 3.  Petersson norm and shadow inner product
# ============================================================================

def petersson_norm(
    coeffs: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    """Petersson norm of shadow: ||zeta_A||^2 = L(1, zeta_A x zeta_A) = sum S_r^2 / r.

    This is the shadow analogue of the Petersson norm of a modular form.
    Convergence: for class G/L/C (finite tower), this is a finite sum.
    For class M: converges because S_r ~ rho^r r^{-5/2}, so S_r^2 ~ rho^{2r} r^{-5}
    and rho < 1 for generic Virasoro.
    """
    val = self_convolution_L(coeffs, complex(1.0, 0.0), max_r)
    return val.real


def shadow_inner_product(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    max_r: Optional[int] = None,
) -> float:
    """Shadow inner product: <zeta_A, zeta_B>_RS = L(1, zeta_A x zeta_B) = sum S_r(A)*S_r(B)/r.

    This is REAL for real shadow coefficients.
    """
    val = rankin_selberg_L(coeffs_A, coeffs_B, complex(1.0, 0.0), max_r)
    return val.real


def petersson_inner_product_matrix(
    families: Dict[str, Dict[int, float]],
) -> Dict[Tuple[str, str], float]:
    """Compute the shadow Petersson inner product matrix for a collection of families.

    Returns dict mapping (name_A, name_B) -> <zeta_A, zeta_B>_RS.
    The matrix is symmetric: <A, B> = <B, A>.
    """
    names = sorted(families.keys())
    result = {}
    for i, name_a in enumerate(names):
        for j, name_b in enumerate(names):
            if j < i:
                result[(name_a, name_b)] = result[(name_b, name_a)]
            else:
                val = shadow_inner_product(families[name_a], families[name_b])
                result[(name_a, name_b)] = val
    return result


# ============================================================================
# 4.  Abscissa of convergence for the Rankin-Selberg convolution
# ============================================================================

def rs_abscissa(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
) -> float:
    """Estimate abscissa of convergence for L(s, zeta_A x zeta_B).

    Since RS_r = S_r(A) * S_r(B), the growth is bounded by:
        |RS_r| <= |S_r(A)| * |S_r(B)|

    For class M x class M: |S_r|^2 ~ rho^{2r} r^{-5}, still exponentially
    decaying for rho < 1, so sigma_c = -infinity (entire).

    For class G/L/C x anything: finite tower, so entire.
    """
    rs_coeffs = rankin_selberg_coefficients(coeffs_A, coeffs_B)
    return abscissa_of_convergence(rs_coeffs)


def rs_growth_rate(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
) -> float:
    """Growth rate of the RS convolution coefficients.

    For A, B both class M with rates rho_A, rho_B:
        RS growth rate = rho_A * rho_B.
    """
    rs_coeffs = rankin_selberg_coefficients(coeffs_A, coeffs_B)
    return shadow_growth_rate_from_coeffs(rs_coeffs)


# ============================================================================
# 5.  Zero finding for the Rankin-Selberg L-function
# ============================================================================

def _sign_changes_on_line(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    sigma: float,
    t_min: float,
    t_max: float,
    n_points: int = 2000,
) -> List[float]:
    """Find approximate imaginary parts of zeros on Re(s) = sigma.

    Scans |L(sigma + i*t)| for local minima that are close to zero.
    A sign change in BOTH real and imaginary parts simultaneously
    (i.e., |L| passes through or near zero) indicates a genuine zero.

    Returns list of approximate t-values where zeros occur.
    """
    dt = (t_max - t_min) / n_points
    candidates = []

    vals = []
    for k in range(n_points + 1):
        t = t_min + k * dt
        val = rankin_selberg_L(coeffs_A, coeffs_B, complex(sigma, t))
        vals.append((t, val))

    # Find local minima of |L(s)|
    for k in range(1, len(vals) - 1):
        t_prev, v_prev = vals[k - 1]
        t_curr, v_curr = vals[k]
        t_next, v_next = vals[k + 1]
        abs_prev = abs(v_prev)
        abs_curr = abs(v_curr)
        abs_next = abs(v_next)
        # Local minimum of |L|
        if abs_curr <= abs_prev and abs_curr <= abs_next and abs_curr < 1e-3:
            # Refine by golden-section search on |L|
            t_lo, t_hi = t_prev, t_next
            for _ in range(50):
                if t_hi - t_lo < 1e-12:
                    break
                t_m1 = t_lo + 0.382 * (t_hi - t_lo)
                t_m2 = t_lo + 0.618 * (t_hi - t_lo)
                v1 = abs(rankin_selberg_L(coeffs_A, coeffs_B, complex(sigma, t_m1)))
                v2 = abs(rankin_selberg_L(coeffs_A, coeffs_B, complex(sigma, t_m2)))
                if v1 < v2:
                    t_hi = t_m2
                else:
                    t_lo = t_m1
            t_zero = (t_lo + t_hi) / 2.0
            v_zero = abs(rankin_selberg_L(coeffs_A, coeffs_B, complex(sigma, t_zero)))
            if v_zero < 1e-4:
                candidates.append(t_zero)

    return candidates


def find_rs_zeros(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    sigma: float = 0.5,
    t_max: float = 100.0,
    n_points: int = 5000,
    max_zeros: int = 50,
) -> List[complex]:
    """Find zeros of L(s, zeta_A x zeta_B) on the line Re(s) = sigma.

    Uses sign-change detection followed by bisection refinement.
    Returns up to max_zeros zeros as complex numbers sigma + i*t.
    """
    candidates = _sign_changes_on_line(
        coeffs_A, coeffs_B, sigma, 0.1, t_max, n_points
    )
    zeros = [complex(sigma, t) for t in candidates[:max_zeros]]
    return zeros


def find_self_convolution_zeros(
    coeffs: Dict[int, float],
    sigma: float = 0.5,
    t_max: float = 100.0,
    max_zeros: int = 50,
) -> List[complex]:
    """Find zeros of the self-convolution L(s, zeta_A x zeta_A)."""
    return find_rs_zeros(coeffs, coeffs, sigma, t_max, max_zeros=max_zeros)


# ============================================================================
# 6.  Symmetric square and exterior square (formal)
# ============================================================================

def _divisors(n: int) -> List[int]:
    """All positive divisors of n."""
    divs = []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            divs.append(d)
            if d != n // d:
                divs.append(n // d)
    return sorted(divs)


def symmetric_square_coefficients(
    coeffs: Dict[int, float],
    max_r: int = 30,
) -> Dict[int, float]:
    """Formal symmetric square coefficients via Dirichlet convolution.

    C_r(Sym^2) = sum_{d | r, d >= 2, r/d >= 2} S_d * S_{r/d}

    WARNING: This is the FORMAL Dirichlet convolution of the shadow sequence
    with itself.  It is NOT the same as the Sym^2 L-function of a modular
    form (which uses Satake parameters).  Shadow towers are not multiplicative
    in general, so this is a DIFFERENT operation.

    The sum restricts to d >= 2 and r/d >= 2 because S_r is defined only for r >= 2.
    """
    result = {}
    for r in range(4, max_r + 1):  # minimum: d=2, r/d=2 => r=4
        total = 0.0
        for d in _divisors(r):
            if d >= 2 and r // d >= 2:
                sd = coeffs.get(d, 0.0)
                srd = coeffs.get(r // d, 0.0)
                total += sd * srd
        result[r] = total
    return result


def symmetric_square_L(
    coeffs: Dict[int, float],
    s: complex,
    max_r: int = 30,
) -> complex:
    """Evaluate L(s, Sym^2 zeta_A) = sum C_r(Sym^2) * r^{-s}."""
    sym2_coeffs = symmetric_square_coefficients(coeffs, max_r)
    if not sym2_coeffs:
        return 0.0 + 0.0j
    total = 0.0 + 0.0j
    for r, c_r in sym2_coeffs.items():
        if c_r != 0.0:
            total += c_r * r ** (-s)
    return total


def exterior_square_coefficients(
    coeffs: Dict[int, float],
    max_r: int = 30,
) -> Dict[int, float]:
    r"""Formal exterior square coefficients via antisymmetrized Dirichlet convolution.

    C_r(\wedge^2) = sum_{d | r, 2 <= d < r/d} S_d * S_{r/d} * (-1)^{...}

    More precisely, the exterior square uses the antisymmetric part:
    for each divisor pair (d, r/d) with d < r/d and both >= 2:
        add S_d * S_{r/d}
    for d = r/d (perfect square):
        subtract S_d^2 / 2  (antisymmetric: zero contribution for exact square)

    Actually, the standard decomposition is:
        Sym^2: include diagonal (d = r/d) and symmetrize
        wedge^2: exclude diagonal (d = r/d)

    So: C_r(wedge^2) = sum_{d | r, 2 <= d < r/d} S_d * S_{r/d}
    and: C_r(Sym^2) = sum_{d | r, 2 <= d <= r/d} S_d * S_{r/d} * (1 if d < r/d else 1)
                     = C_r(wedge^2) + sum_{d^2 = r, d >= 2} S_d^2

    The full Dirichlet convolution = Sym^2 + wedge^2:
        (S * S)_r = sum_{d | r, d >= 2, r/d >= 2} S_d * S_{r/d}
                  = 2 * C_r(wedge^2) + diagonal
    """
    result = {}
    for r in range(4, max_r + 1):
        total = 0.0
        for d in _divisors(r):
            e = r // d
            if d >= 2 and e >= 2 and d < e:
                total += coeffs.get(d, 0.0) * coeffs.get(e, 0.0)
        result[r] = total
    return result


def exterior_square_L(
    coeffs: Dict[int, float],
    s: complex,
    max_r: int = 30,
) -> complex:
    r"""Evaluate L(s, \wedge^2 zeta_A) = sum C_r(\wedge^2) * r^{-s}."""
    ext2_coeffs = exterior_square_coefficients(coeffs, max_r)
    if not ext2_coeffs:
        return 0.0 + 0.0j
    total = 0.0 + 0.0j
    for r, c_r in ext2_coeffs.items():
        if c_r != 0.0:
            total += c_r * r ** (-s)
    return total


# ============================================================================
# 7.  Cross-family convolutions
# ============================================================================

def cross_family_rs_L(
    family_A: str,
    param_A: float,
    family_B: str,
    param_B: float,
    s: complex,
    max_r: int = 50,
) -> complex:
    """Compute L(s, zeta_A x zeta_B) for named families.

    Families: 'virasoro', 'heisenberg', 'affine_sl2', 'affine_sl3', 'betagamma'.
    param is the family parameter (c for Virasoro, k for Heisenberg/affine, lambda for bg).
    """
    providers = {
        'virasoro': get_virasoro_coeffs,
        'heisenberg': get_heisenberg_coeffs,
        'affine_sl2': get_affine_sl2_coeffs,
        'affine_sl3': get_affine_sl3_coeffs,
        'betagamma': get_betagamma_coeffs,
    }
    coeffs_A = providers[family_A](param_A, max_r)
    coeffs_B = providers[family_B](param_B, max_r)
    return rankin_selberg_L(coeffs_A, coeffs_B, s)


def class_of_rs_convolution(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
) -> str:
    """Determine the shadow depth class of the RS convolution.

    Class G x anything = class G (if one factor terminates at arity 2)
    Class L x anything with class <= L = class L
    Class C x anything with class <= C = class C
    Class M x class M = class M

    The RS convolution of two finite towers is finite: the product
    terminates wherever either factor terminates.
    """
    def _class_of(coeffs: Dict[int, float]) -> str:
        max_nonzero = 2
        for r in sorted(coeffs.keys()):
            if abs(coeffs.get(r, 0.0)) > 1e-50:
                max_nonzero = r
        if max_nonzero <= 2:
            return 'G'
        elif max_nonzero <= 3:
            return 'L'
        elif max_nonzero <= 4:
            return 'C'
        else:
            return 'M'

    class_a = _class_of(coeffs_A)
    class_b = _class_of(coeffs_B)

    # The RS product S_r(A) * S_r(B) vanishes wherever either factor vanishes.
    # So the product terminates at the MINIMUM of the two termination arities.
    order = {'G': 0, 'L': 1, 'C': 2, 'M': 3}
    min_class = min(class_a, class_b, key=lambda c: order[c])
    return min_class


# ============================================================================
# 8.  Convexity bounds
# ============================================================================

def convexity_bound_rs(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    sigma: float,
    t: float,
) -> float:
    """Estimate a convexity bound for |L(sigma + it, zeta_A x zeta_B)|.

    For a Dirichlet series with exponentially decaying coefficients (rho < 1),
    the function is entire and the standard Phragmen-Lindelof convexity bound
    gives polynomial growth in the t-aspect.

    For finite towers (class G/L/C): the sum is a Dirichlet polynomial of
    bounded degree, so |L(sigma+it)| = O(1) as t -> infinity (bounded!).

    For class M x class M: |L(sigma + it)| = O(|t|^{alpha}) where alpha
    depends on sigma and the growth rate.

    This returns a heuristic upper bound (not rigorous).
    """
    rs_coeffs = rankin_selberg_coefficients(coeffs_A, coeffs_B)
    max_r = max(rs_coeffs.keys())

    # Trivial bound: |L(sigma+it)| <= sum |RS_r| * r^{-sigma}
    trivial = sum(abs(v) * r ** (-sigma) for r, v in rs_coeffs.items() if v != 0.0)
    return trivial


def verify_convexity(
    coeffs_A: Dict[int, float],
    coeffs_B: Dict[int, float],
    sigma: float = 0.5,
    t_values: Optional[List[float]] = None,
) -> List[Tuple[float, float, float]]:
    """Verify convexity bound at several t-values.

    Returns list of (t, |L(sigma+it)|, bound) triples.
    """
    if t_values is None:
        t_values = [1.0, 5.0, 10.0, 20.0, 50.0]
    results = []
    bound = convexity_bound_rs(coeffs_A, coeffs_B, sigma, 0.0)
    for t in t_values:
        val = abs(rankin_selberg_L(coeffs_A, coeffs_B, complex(sigma, t)))
        results.append((t, val, bound))
    return results


# ============================================================================
# 9.  Petersson norm vs shadow radius relation
# ============================================================================

def shadow_radius(coeffs: Dict[int, float]) -> float:
    """Estimate the shadow radius rho from consecutive coefficient ratios.

    For class M: rho = lim |S_{r+1}/S_r| as r -> infinity.
    For finite towers: rho = 0.
    """
    return shadow_growth_rate_from_coeffs(coeffs)


def petersson_norm_vs_radius(
    c_values: List[float],
    max_r: int = 50,
) -> List[Tuple[float, float, float]]:
    """Compare Petersson norm with shadow radius squared for Virasoro.

    Returns list of (c, ||zeta||^2, rho^2) triples.

    The Petersson norm sum S_r^2 / r is controlled by rho^2:
        ||zeta||^2 ~ C * sum rho^{2r} r^{-6} (since S_r^2 ~ rho^{2r} r^{-5}
        and we divide by r).
    """
    results = []
    for c_val in c_values:
        try:
            coeffs = get_virasoro_coeffs(c_val, max_r)
            pn = petersson_norm(coeffs)
            rho = virasoro_growth_rate_exact(c_val)
            results.append((c_val, pn, rho ** 2))
        except (ValueError, ZeroDivisionError):
            continue
    return results


# ============================================================================
# 10.  Utility: standard family collection for inner product matrices
# ============================================================================

def standard_family_collection(max_r: int = 50) -> Dict[str, Dict[int, float]]:
    """Build a standard collection of shadow coefficient dictionaries.

    Includes: Heisenberg (k=1), affine sl_2 (k=1,2), affine sl_3 (k=1),
    beta-gamma (lambda=0.5), Virasoro at c = 1,2,...,25, W_3 at c=-2
    (via the T-line/Virasoro restriction).
    """
    collection = {}
    collection['Heis_1'] = get_heisenberg_coeffs(1.0, max_r)
    collection['sl2_k1'] = get_affine_sl2_coeffs(1.0, max_r)
    collection['sl2_k2'] = get_affine_sl2_coeffs(2.0, max_r)
    collection['sl3_k1'] = get_affine_sl3_coeffs(1.0, max_r)
    collection['bg_half'] = get_betagamma_coeffs(0.5, max_r)
    for c_val in range(1, 26):
        collection[f'Vir_{c_val}'] = get_virasoro_coeffs(float(c_val), max_r)
    # W_3 at c = -2 along the T-line (Virasoro restriction, NOT the full W_3)
    # NOTE: c = -2 is too close to the pole at 5c+22 = 0 => c = -4.4, so -2 is fine
    collection['W3_T_cm2'] = get_virasoro_coeffs(-2.0, max_r)
    return collection


def virasoro_complementarity_scan(
    c_values: List[float],
    s: complex = complex(1.0, 0.0),
    max_r: int = 50,
) -> List[Tuple[float, complex, complex, complex]]:
    """Scan complementarity convolution across c-values.

    Returns list of (c, L(s, zeta_c x zeta_{26-c}), L(s, zeta_c x zeta_c),
                      L(s, zeta_{26-c} x zeta_{26-c})).
    """
    results = []
    for c_val in c_values:
        try:
            coeffs_A = get_virasoro_coeffs(c_val, max_r)
            coeffs_B = get_koszul_dual_virasoro_coeffs(c_val, max_r)
            L_cross = rankin_selberg_L(coeffs_A, coeffs_B, s)
            L_self_A = self_convolution_L(coeffs_A, s)
            L_self_B = self_convolution_L(coeffs_B, s)
            results.append((c_val, L_cross, L_self_A, L_self_B))
        except (ValueError, ZeroDivisionError):
            continue
    return results
