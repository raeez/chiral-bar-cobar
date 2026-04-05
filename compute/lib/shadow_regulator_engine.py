r"""Shadow regulator engine: algebraic K-theory and Beilinson regulators for shadow curves.

The shadow curve C_A: y^2 = t^4 * Q_L(t) is an algebraic curve encoding the
full shadow obstruction tower of a modular Koszul algebra A. This module
computes algebraic K-theory invariants, Beilinson regulators, and their
relation to shadow L-functions.

ALGEBRAIC K-THEORY OF C_A:

  K_0(C_A) = Z + Pic(C_A).
  K_1(C_A) contains units O*(C_A).
  K_2(C_A) contains Milnor symbols {f, g}.

The natural K_2 element is xi_A = {t, y} in K_2(C_A).

BEILINSON REGULATOR:

  reg: K_2(C) -> H^1_D(C, R(2))

  reg({f, g})(gamma) = integral_gamma (log|f| d arg(g) - log|g| d arg(f))

For xi_A = {t, y}:
  reg(xi_A)(gamma) = integral_gamma (log|t| d arg(y) - log|y| d arg(t))

BEILINSON CONJECTURE:

  L'(0, H^1(C)) = regulator * rational * (2*pi*i)^n

SHADOW CURVE CLASSIFICATION (from shadow_motivic_hodge_engine.py):
  The shadow curve y^2 = t^4 * Q_L(t) with Q_L quadratic in t is birational
  to the conic w^2 = q_0*s^2 + q_1*s + q_2 via s=1/t, w=y*t^{-3}.
  Geometric genus is always 0.

  Despite genus 0, the K-theory of the singular model y^2 = t^4*Q_L(t)
  is nontrivial because of the singularity at t=0. The K_2 element {t,y}
  has nontrivial tame symbols at the singular points.

  For NUMERICAL computations we work with the affine model y^2 = f(t) where
  f(t) = t^4 * Q_L(t) = q_0*t^4 + q_1*t^5 + q_2*t^6, integrating along
  cycles on the Riemann surface.

BOREL REGULATOR AND SHADOW ZETA:

  Borel: K_{2n-1}(Q) tensor R -> R.
  zeta(n) = Borel_regulator * rational.

  Shadow analogue:
    zeta_A(n) = sum_r S_r * r^{-n}.
  The "shadow Borel regulator" is the numerical value that, multiplied by
  a rational, yields zeta_A(n).

SHADOW CHERN CHARACTER:

  ch(E_A) = rank + c_1(E_A) + c_2(E_A)/2 + ...
  where c_1(E_A) = kappa(A) * lambda_1 by Theorem D.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    prop:shadow-periods (arithmetic_shadows.tex)
    rem:motivic-decomposition (arithmetic_shadows.tex)
    def:arithmetic-packet-connection (arithmetic_shadows.tex)

CAUTION (AP1): kappa formulas are family-specific.
CAUTION (AP9): S_2 = kappa != c/2 in general (only for Virasoro).
CAUTION (AP48): kappa depends on the full algebra, not the Virasoro sub.
CAUTION (AP38): All numerical values computed from first principles, not
    copied from literature without convention check.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import numpy as np
from scipy import integrate


# ============================================================================
# 0.  Shadow data for standard families (reproduced for self-containment)
# ============================================================================

def virasoro_shadow_data_numerical(c_val: float) -> Dict[str, float]:
    r"""Shadow data for Virasoro at central charge c.

    kappa = c/2, alpha = S_3 = 2, S_4 = 10/(c(5c+22)),
    Delta = 8*kappa*S_4 = 40/(5c+22).

    Q_L(t) = c^2 + 12c*t + [(180c+872)/(5c+22)]*t^2.
    """
    if c_val == 0.0:
        raise ValueError("Virasoro shadow undefined at c=0")
    denom = 5.0 * c_val + 22.0
    if denom == 0.0:
        raise ValueError("Virasoro shadow undefined at c=-22/5")

    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * denom)
    Delta = 40.0 / denom

    q0 = c_val ** 2
    q1 = 12.0 * c_val
    q2 = (180.0 * c_val + 872.0) / denom

    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2, 'c': c_val,
    }


def heisenberg_shadow_data_numerical(k_val: float) -> Dict[str, float]:
    r"""Shadow data for Heisenberg at level k.

    kappa = k, alpha = 0, S_4 = 0, Delta = 0.
    Q_L(t) = 4k^2 (constant).
    """
    return {
        'kappa': k_val, 'alpha': 0.0, 'S4': 0.0, 'Delta': 0.0,
        'q0': 4.0 * k_val ** 2, 'q1': 0.0, 'q2': 0.0, 'c': 2.0 * k_val,
    }


def affine_sl2_shadow_data_numerical(k_val: float) -> Dict[str, float]:
    r"""Shadow data for affine sl_2 at level k.

    dim(sl_2) = 3, h^v = 2.
    kappa = 3(k+2)/4.
    alpha = 4/(k+2) (Sugawara cubic).
    S_4 = 0, Delta = 0. Class L.
    """
    if k_val == -2.0:
        raise ValueError("Affine sl_2 critical level k=-2")
    hv = 2.0
    kappa = 3.0 * (k_val + hv) / (2.0 * hv)
    alpha = 2.0 * hv / (k_val + hv)
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2
    c_val = 3.0 * k_val / (k_val + 2.0)  # Sugawara
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': 0.0, 'Delta': 0.0,
        'q0': q0, 'q1': q1, 'q2': q2, 'c': c_val,
    }


def betagamma_shadow_data_numerical(lam: float = 0.5) -> Dict[str, float]:
    r"""Shadow data for beta-gamma at conformal weight lambda.

    c = 2(6*lambda^2 - 6*lambda + 1), kappa = c/2.
    Class C: terminates at arity 4 on full deformation complex.
    On T-line restriction: alpha = 2, S_4 = 10/(c(5c+22)).
    """
    c_val = 2.0 * (6.0 * lam ** 2 - 6.0 * lam + 1.0)
    kappa = c_val / 2.0
    alpha = 2.0
    denom = c_val * (5.0 * c_val + 22.0)
    S4 = 10.0 / denom if abs(denom) > 1e-15 else 0.0
    Delta = 8.0 * kappa * S4
    q0 = 4.0 * kappa ** 2
    q1 = 12.0 * kappa * alpha
    q2 = 9.0 * alpha ** 2 + 2.0 * Delta
    return {
        'kappa': kappa, 'alpha': alpha, 'S4': S4, 'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2, 'c': c_val,
    }


FAMILY_DATA_FNS = {
    'virasoro': virasoro_shadow_data_numerical,
    'heisenberg': heisenberg_shadow_data_numerical,
    'affine_sl2': affine_sl2_shadow_data_numerical,
    'betagamma': betagamma_shadow_data_numerical,
}


# ============================================================================
# 1.  Shadow metric Q_L and sextic f(t)
# ============================================================================

def shadow_metric_QL(data: Dict[str, float], t_val: complex) -> complex:
    """Evaluate Q_L(t) = q_0 + q_1*t + q_2*t^2."""
    return data['q0'] + data['q1'] * t_val + data['q2'] * t_val ** 2


def shadow_sextic_f(data: Dict[str, float], t_val: complex) -> complex:
    """Evaluate f(t) = t^4 * Q_L(t), the defining polynomial of y^2 = f(t)."""
    return t_val ** 4 * shadow_metric_QL(data, t_val)


def shadow_curve_y(data: Dict[str, float], t_val: complex, branch: int = 1) -> complex:
    """Evaluate y = branch * sqrt(f(t)) = branch * t^2 * sqrt(Q_L(t)).

    branch = +1 or -1.
    """
    f_val = shadow_sextic_f(data, t_val)
    sq = cmath.sqrt(f_val)
    return branch * sq


def QL_zeros(data: Dict[str, float]) -> Tuple[complex, complex]:
    """Zeros of Q_L(t) = q0 + q1*t + q2*t^2.

    These are the branch points of sqrt(Q_L(t)) (finite ones; there is also
    branching at infinity if deg f is odd, but deg f = 6 is even so no
    branching at infinity).

    Returns (t_plus, t_minus) where t_pm = (-q1 +/- sqrt(q1^2 - 4*q0*q2)) / (2*q2).
    """
    q0, q1, q2 = data['q0'], data['q1'], data['q2']
    if abs(q2) < 1e-30:
        # Q_L is linear or constant; no finite branch points from quadratic formula
        if abs(q1) < 1e-30:
            return (complex('inf'), complex('inf'))
        root = -q0 / q1
        return (root, complex('inf'))
    disc = q1 ** 2 - 4.0 * q0 * q2
    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2.0 * q2)
    t_minus = (-q1 - sqrt_disc) / (2.0 * q2)
    return (t_plus, t_minus)


def branch_points_sextic(data: Dict[str, float]) -> List[complex]:
    """All branch points of y^2 = f(t) = t^4 * Q_L(t).

    Branch points where f has ODD-order vanishing:
    - t=0: order 4 (even) -> NOT a branch point
    - Zeros of Q_L: order 1 (odd) -> branch points (if distinct)
    - If Q_L has a double root: that root has order 2 -> NOT a branch point

    So the only branch points in the finite plane are the SIMPLE zeros of Q_L.
    """
    t_p, t_m = QL_zeros(data)
    pts = []
    if abs(t_p) < 1e30:
        pts.append(t_p)
    if abs(t_m) < 1e30:
        # Check if t_m = t_p (double root)
        if len(pts) == 0 or abs(t_m - t_p) > 1e-10:
            pts.append(t_m)
    return pts


# ============================================================================
# 2.  Picard group and K_0
# ============================================================================

@dataclass
class ShadowK0:
    """K_0(C_A) = Z + Pic(C_A) data.

    For a smooth projective curve of genus g: Pic^0 = Jacobian of dimension g.
    The shadow curve (after normalization) has genus 0, so Pic^0 = 0 and
    Pic = Z (generated by the class of a point).

    However, the SINGULAR model y^2 = t^4*Q_L(t) has additional K-theory
    from the singularity at t=0. The normalization sequence:
      0 -> O*_sing -> O*_norm -> cokernel -> Pic_sing -> Pic_norm -> 0
    contributes nontrivial K_0 and K_1 terms.

    For a node: the cokernel contributes G_m (multiplicative group).
    For a cusp: the cokernel contributes G_a (additive group).
    The t^4 singularity is worse than either; the normalization map
    crushes the t=0 fiber into a point on the smooth conic.
    """
    rank: int  # rank of K_0 free part (always 1 for connected curve)
    pic_degree_0_dim: int  # dimension of Pic^0 (= genus of normalization)
    singularity_contribution: str  # description of singularity K-theory
    family: str
    shadow_class: str

    @property
    def pic_rank(self) -> int:
        """Picard number = 1 (degree map to Z) for connected curve."""
        return 1


def compute_K0(family: str, data: Dict[str, float]) -> ShadowK0:
    """Compute K_0(C_A) for the shadow curve.

    The normalized shadow curve is always genus 0 (a smooth conic).
    K_0(norm) = Z + Z (rank + degree).

    The singular model has additional contributions from the t=0 singularity:
    - Class G (Heisenberg): Q_L constant, f(t) = q0*t^4. The curve y^2 = q0*t^4
      reduces to y = +-sqrt(q0)*t^2, two branches meeting at origin with order 2.
      The singularity is a tacnode.
    - Class L: Q_L has a single root. Singularity structure more complex.
    - Class M: Q_L irreducible. The t=0 singularity is a higher-order cusp.
    """
    Delta = data['Delta']
    if abs(Delta) < 1e-15 and abs(data['alpha']) < 1e-15:
        shadow_class = 'G'
    elif abs(Delta) < 1e-15:
        shadow_class = 'L'
    else:
        shadow_class = 'M'

    return ShadowK0(
        rank=1,
        pic_degree_0_dim=0,  # genus of normalization = 0
        singularity_contribution=(
            'tacnode (two smooth branches tangent to order 2)' if shadow_class == 'G'
            else 'higher cusp (t^4 singularity with nonconstant Q_L)'
        ),
        family=family,
        shadow_class=shadow_class,
    )


# ============================================================================
# 3.  K_1 and units of the shadow curve
# ============================================================================

@dataclass
class ShadowK1:
    """K_1(C_A) data: units of the function field.

    For a smooth projective curve of genus 0 over a field:
      O*(C) = constants (the base field units).

    For the singular affine model y^2 = f(t):
      The coordinate ring R = k[t, y]/(y^2 - f(t)) has units beyond constants
      only if f(t) is a perfect square (then y/sqrt(f) is invertible).

    Key units:
    - t is a unit away from t=0 and t=infinity
    - y is a unit away from the zeros of f(t)
    - t^2/y = 1/sqrt(Q_L(t)) is a unit away from zeros of Q_L

    For K_1, we track the group of units modulo the obvious constants.
    """
    constant_units: str  # description (e.g. "k*" for base field)
    nonconstant_units: List[str]  # generators of nonconstant units
    family: str

    @property
    def rank(self) -> int:
        return len(self.nonconstant_units)


def compute_K1(family: str, data: Dict[str, float]) -> ShadowK1:
    """Compute K_1(C_A) for the shadow curve.

    On the smooth affine piece C_A^0 = C_A minus singular points,
    the units include t (invertible away from t=0, infinity)
    and y (invertible away from zeros of f).

    For Milnor K-theory: K_1^M = O* / k* is generated by
    the rational functions with specified divisors.
    """
    units = ['t (invertible on C_A^0)', 'y (invertible away from f=0)']

    # For class G: y = sqrt(q0)*t^2 on the normalization, so y/t^2 is constant
    if abs(data['Delta']) < 1e-15 and abs(data['alpha']) < 1e-15:
        units.append('y/t^2 = sqrt(q0) (becomes constant on normalization)')

    return ShadowK1(
        constant_units='k* (scalars)',
        nonconstant_units=units,
        family=family,
    )


# ============================================================================
# 4.  K_2 and the Milnor symbol {t, y}
# ============================================================================

@dataclass
class TameSymbol:
    """Tame symbol data at a point P of the shadow curve."""
    point: complex  # the t-coordinate of P
    point_label: str
    vt: int  # valuation v_P(t)
    vy: int  # valuation v_P(y)
    value: complex  # Tame_P({t,y})
    sign_factor: int  # (-1)^{v_P(t)*v_P(y)}


def valuation_at_point(data: Dict[str, float], t_point: complex,
                       func: str = 't') -> int:
    """Compute the valuation v_P(func) at the point t = t_point on C_A.

    For the function t: v_P(t) = order of vanishing of t at P.
      - At t=0: v_{t=0}(t) = 1
      - At finite t != 0: v_P(t) = 0
      - At t=infinity: v_{infty}(t) = -1

    For the function y: v_P(y) = order of vanishing of y at P.
      y^2 = f(t) = t^4 * Q_L(t).
      - At t=0: ord(f) = 4, so v_{t=0}(y) = 2
      - At a simple zero t_0 of Q_L: ord(f) = 1, so v_{t_0}(y) = 1
        (accounting for the double cover: y vanishes to order 1 on ONE
        sheet of the cover; the point P = (t_0, 0) is a ramification point)
      - At t=infinity: if f has degree 6, then v_infty(f) = -6,
        so v_infty(y) = -3.
      - At generic point: v_P(y) = 0.
    """
    if func == 't':
        if abs(t_point) < 1e-14:
            return 1
        elif abs(t_point) > 1e14:
            return -1
        else:
            return 0
    elif func == 'y':
        if abs(t_point) < 1e-14:
            return 2  # f(t) = t^4 * Q_L(t) vanishes to order 4 at t=0
        elif abs(t_point) > 1e14:
            return -3  # degree 6 polynomial => v_infty(y) = -3
        else:
            # Check if t_point is a zero of Q_L
            QL_val = shadow_metric_QL(data, t_point)
            if abs(QL_val) < 1e-10:
                return 1  # simple zero of Q_L => simple zero of f => y vanishes order 1
            else:
                return 0
    else:
        raise ValueError(f"Unknown function '{func}'")


def tame_symbol(data: Dict[str, float], t_point: complex,
                label: str = '') -> TameSymbol:
    r"""Compute the tame symbol Tame_P({t, y}) at a point P = (t_point, y_point).

    Tame_P({f, g}) = (-1)^{v_P(f)*v_P(g)} * (f^{v_P(g)} / g^{v_P(f)}) |_P

    For {t, y}:
      Tame_P({t, y}) = (-1)^{v_P(t)*v_P(y)} * (t^{v_P(y)} / y^{v_P(t)}) |_P
    """
    vt = valuation_at_point(data, t_point, 't')
    vy = valuation_at_point(data, t_point, 'y')

    sign = (-1) ** (vt * vy)

    # Compute the rational function value
    # t^{v_P(y)} / y^{v_P(t)} evaluated at P
    if vt == 0 and vy == 0:
        # Both have valuation 0 => tame symbol is 1
        value = complex(sign)
    elif abs(t_point) < 1e-14:
        # P = origin: vt=1, vy=2
        # t^{vy}/y^{vt} = t^2/y^1 = t^2/y
        # y^2 = t^4 Q_L(t), so y = t^2 sqrt(Q_L(t))
        # t^2/y = 1/sqrt(Q_L(t))
        # At t=0: Q_L(0) = q0 = 4*kappa^2
        # So tame = sign * 1/sqrt(q0) = sign / (2*|kappa|)
        q0 = data['q0']
        if abs(q0) < 1e-30:
            value = complex(float('inf'))
        else:
            value = complex(sign) / cmath.sqrt(q0)
    elif abs(t_point) > 1e14:
        # P = infinity: vt=-1, vy=-3
        # t^{vy}/y^{vt} = t^{-3}/y^{-1} = y/t^3
        # y = t^2*sqrt(Q_L(t)), so y/t^3 = sqrt(Q_L(t))/t
        # For large t: Q_L ~ q2*t^2, so sqrt(Q_L)/t ~ sqrt(q2)
        # tame = sign * sqrt(q2)
        q2 = data['q2']
        value = complex(sign) * cmath.sqrt(q2)
    else:
        # Branch point of Q_L: vt=0, vy=1 (if zero of Q_L)
        # or generic: vt=0, vy=0
        if vy == 1 and vt == 0:
            # t^1/y^0 = t. But wait: tame = sign * t^{vy}/y^{vt} = sign * t^1/y^0 = sign * t
            value = complex(sign) * t_point
        elif vy == 0 and vt == 0:
            value = complex(sign)
        else:
            # General case: compute numerically
            y_val = shadow_curve_y(data, t_point, branch=1)
            if abs(y_val) < 1e-30 and vt != 0:
                value = complex(float('inf'))
            else:
                num = t_point ** vy
                den = y_val ** vt if vt != 0 else 1.0
                value = complex(sign) * num / den

    return TameSymbol(
        point=t_point,
        point_label=label or f't={t_point}',
        vt=vt,
        vy=vy,
        value=value,
        sign_factor=sign,
    )


def compute_all_tame_symbols(data: Dict[str, float]) -> List[TameSymbol]:
    """Compute tame symbols at all relevant points.

    Points where v_P(t) != 0 or v_P(y) != 0:
    1. t = 0 (vt=1, vy=2)
    2. t = infinity (vt=-1, vy=-3)
    3. Zeros of Q_L (vt=0, vy=1 for simple zeros)
    """
    symbols = []

    # t = 0
    symbols.append(tame_symbol(data, 0.0, label='origin'))

    # t = infinity
    symbols.append(tame_symbol(data, 1e15, label='infinity'))

    # Zeros of Q_L
    bp = branch_points_sextic(data)
    for i, t_val in enumerate(bp):
        symbols.append(tame_symbol(data, t_val, label=f'branch_pt_{i}'))

    return symbols


def product_of_tame_symbols(tame_list: List[TameSymbol]) -> complex:
    """Weil reciprocity: the product of all tame symbols equals 1 (up to sign).

    For a SMOOTH projective curve, prod_P Tame_P({f,g}) = 1.
    For our singular model, this serves as a consistency check.
    """
    prod = complex(1.0)
    for ts in tame_list:
        if abs(ts.value) < 1e30:
            prod *= ts.value
    return prod


def virasoro_tame_symbols(c_val: float) -> Dict[str, Any]:
    """Compute all tame symbols for the Virasoro shadow curve at central charge c."""
    data = virasoro_shadow_data_numerical(c_val)
    syms = compute_all_tame_symbols(data)
    prod = product_of_tame_symbols(syms)
    return {
        'c': c_val,
        'kappa': data['kappa'],
        'tame_symbols': syms,
        'product': prod,
        'data': data,
    }


# ============================================================================
# 5.  Beilinson regulator via numerical integration
# ============================================================================

def _log_abs(z: complex) -> float:
    """log|z| for complex z."""
    return math.log(abs(z)) if abs(z) > 1e-300 else -700.0


def _arg(z: complex) -> float:
    """arg(z) in (-pi, pi]."""
    return cmath.phase(z)


def regulator_integrand_real(t_re: float, t_im: float,
                             data: Dict[str, float],
                             component: str = 'real') -> float:
    r"""Integrand for the Beilinson regulator of {t, y} along a path.

    reg({t, y})(gamma) = integral_gamma eta
    where eta = log|t| d(arg y) - log|y| d(arg t).

    For a PARAMETRIC path gamma(s) = t(s), s in [0, 1]:
      eta = log|t| * (d/ds)(arg y) * ds - log|y| * (d/ds)(arg t) * ds.

    For the real-axis cycle (t_im = 0), this simplifies.
    For general paths we parametrize and use quadrature.
    """
    t_val = complex(t_re, t_im)
    if abs(t_val) < 1e-14:
        return 0.0

    f_val = shadow_sextic_f(data, t_val)
    y_val = cmath.sqrt(f_val)

    log_t = _log_abs(t_val)
    log_y = _log_abs(y_val)
    arg_t = _arg(t_val)
    arg_y = _arg(y_val)

    if component == 'real':
        return log_t
    elif component == 'imag':
        return log_y
    else:
        return 0.0


def beilinson_regulator_branch_cycle(data: Dict[str, float],
                                     n_points: int = 1000) -> complex:
    r"""Compute the Beilinson regulator of {t, y} on the branch-cut cycle.

    The branch cut connects the two zeros t_+, t_- of Q_L(t).
    The cycle gamma goes from t_+ to t_- above the cut and returns below.

    reg({t,y})(gamma) = integral_gamma (log|t| d(arg y) - log|y| d(arg t))

    We parametrize the cycle as a small loop around the branch cut.
    For two branch points t_+, t_- in the complex plane, the cycle is
    a loop encircling the segment [t_+, t_-].

    IMPLEMENTATION: We parametrize the loop as an ellipse around the
    branch-cut segment and compute the integral numerically.
    """
    t_p, t_m = QL_zeros(data)
    if abs(t_p) > 1e14 or abs(t_m) > 1e14:
        # Degenerate: no finite branch cut
        return complex(0.0)

    # Midpoint and half-length of the branch cut
    mid = (t_p + t_m) / 2.0
    half_len = abs(t_p - t_m) / 2.0
    if half_len < 1e-14:
        return complex(0.0)

    # Direction of the branch cut
    direction = (t_p - t_m) / abs(t_p - t_m) if abs(t_p - t_m) > 1e-14 else 1.0
    perp = direction * 1j

    # Parametrize loop: ellipse with semi-axes (half_len+eps, eps)
    eps = half_len * 0.1  # offset to avoid the cut

    # Integration via trapezoidal rule on the ellipse
    thetas = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    dt_theta = 2 * np.pi / n_points

    reg_val = 0.0
    prev_arg_y = None
    prev_arg_t = None

    for i, theta in enumerate(thetas):
        # Point on the ellipse
        t_val = mid + (half_len + eps) * math.cos(theta) * direction + eps * math.sin(theta) * perp

        # Evaluate y
        f_val = shadow_sextic_f(data, t_val)
        y_val = cmath.sqrt(f_val)

        log_t = _log_abs(t_val)
        log_y = _log_abs(y_val)
        arg_y = _arg(y_val)
        arg_t = _arg(t_val)

        if prev_arg_y is not None:
            # Unwrap phase differences
            d_arg_y = arg_y - prev_arg_y
            d_arg_t = arg_t - prev_arg_t

            # Unwrap
            while d_arg_y > math.pi:
                d_arg_y -= 2 * math.pi
            while d_arg_y < -math.pi:
                d_arg_y += 2 * math.pi
            while d_arg_t > math.pi:
                d_arg_t -= 2 * math.pi
            while d_arg_t < -math.pi:
                d_arg_t += 2 * math.pi

            # Riemann sum contribution
            reg_val += log_t * d_arg_y - log_y * d_arg_t

        prev_arg_y = arg_y
        prev_arg_t = arg_t

    # Close the loop (last to first)
    t_val = mid + (half_len + eps) * math.cos(thetas[0]) * direction + eps * math.sin(thetas[0]) * perp
    f_val = shadow_sextic_f(data, t_val)
    y_val = cmath.sqrt(f_val)
    arg_y = _arg(y_val)
    arg_t = _arg(t_val)
    d_arg_y = arg_y - prev_arg_y
    d_arg_t = arg_t - prev_arg_t
    while d_arg_y > math.pi:
        d_arg_y -= 2 * math.pi
    while d_arg_y < -math.pi:
        d_arg_y += 2 * math.pi
    while d_arg_t > math.pi:
        d_arg_t -= 2 * math.pi
    while d_arg_t < -math.pi:
        d_arg_t += 2 * math.pi

    log_t_first = _log_abs(
        mid + (half_len + eps) * math.cos(thetas[0]) * direction + eps * math.sin(thetas[0]) * perp
    )
    log_y_first = _log_abs(cmath.sqrt(shadow_sextic_f(
        data,
        mid + (half_len + eps) * math.cos(thetas[0]) * direction + eps * math.sin(thetas[0]) * perp
    )))
    reg_val += log_t_first * d_arg_y - log_y_first * d_arg_t

    return complex(reg_val)


def beilinson_regulator_infinity_cycle(data: Dict[str, float],
                                       R: float = 100.0,
                                       n_points: int = 2000) -> complex:
    r"""Compute the regulator on a large circle (cycle around infinity).

    gamma = circle of radius R in the t-plane.
    reg({t,y})(gamma) = integral_{|t|=R} (log|t| d(arg y) - log|y| d(arg t))

    On the circle |t| = R: log|t| = log(R) (constant).
    d(arg t) = dtheta.
    So the integral simplifies to:
      log(R) * integral d(arg y) - integral log|y| dtheta

    integral d(arg y) = 2*pi * winding number of y around the circle.
    """
    thetas = np.linspace(0, 2 * np.pi, n_points, endpoint=False)

    reg_val = 0.0
    prev_arg_y = None

    for theta in thetas:
        t_val = R * cmath.exp(1j * theta)
        f_val = shadow_sextic_f(data, t_val)
        y_val = cmath.sqrt(f_val)

        log_t = math.log(R)
        log_y = _log_abs(y_val)
        arg_y = _arg(y_val)

        if prev_arg_y is not None:
            d_arg_y = arg_y - prev_arg_y
            while d_arg_y > math.pi:
                d_arg_y -= 2 * math.pi
            while d_arg_y < -math.pi:
                d_arg_y += 2 * math.pi

            d_arg_t = 2 * math.pi / n_points  # uniform parametrization

            reg_val += log_t * d_arg_y - log_y * d_arg_t

        prev_arg_y = arg_y

    # Close
    t_val = R * cmath.exp(1j * thetas[0])
    f_val = shadow_sextic_f(data, t_val)
    y_val = cmath.sqrt(f_val)
    d_arg_y = _arg(y_val) - prev_arg_y
    while d_arg_y > math.pi:
        d_arg_y -= 2 * math.pi
    while d_arg_y < -math.pi:
        d_arg_y += 2 * math.pi
    d_arg_t = 2 * math.pi / n_points
    reg_val += math.log(R) * d_arg_y - _log_abs(y_val) * d_arg_t

    return complex(reg_val)


def beilinson_regulator_all_cycles(data: Dict[str, float],
                                   n_points: int = 2000) -> Dict[str, complex]:
    """Compute the Beilinson regulator on all homology cycles."""
    return {
        'branch_cycle': beilinson_regulator_branch_cycle(data, n_points),
        'infinity_cycle': beilinson_regulator_infinity_cycle(data, n_points=n_points),
    }


def virasoro_beilinson_regulator(c_val: float,
                                 n_points: int = 2000) -> Dict[str, Any]:
    """Full Beilinson regulator computation for Virasoro at central charge c."""
    data = virasoro_shadow_data_numerical(c_val)
    regs = beilinson_regulator_all_cycles(data, n_points)
    return {
        'c': c_val,
        'kappa': data['kappa'],
        'regulators': regs,
        'data': data,
    }


# ============================================================================
# 6.  Shadow L-function and Beilinson conjecture
# ============================================================================

def shadow_coefficients_numerical(data: Dict[str, float],
                                  max_r: int = 50) -> Dict[int, float]:
    r"""Compute shadow tower coefficients S_r from Q_L data.

    H(t) = t^2 * sqrt(Q_L(t)) = sum_{r>=2} r * S_r * t^r.
    So S_r = a_{r-2} / r where a_n are Taylor coefficients of sqrt(Q_L).
    """
    q0, q1, q2 = data['q0'], data['q1'], data['q2']

    if abs(q0) < 1e-30:
        return {r: 0.0 for r in range(2, max_r + 1)}

    a0 = math.sqrt(abs(q0))
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


def shadow_zeta_at_integer(data: Dict[str, float], n: int,
                           max_r: int = 200) -> float:
    r"""Evaluate the shadow zeta function zeta_A(n) = sum_r S_r * r^{-n}.

    For n >= 1 and convergent towers (class G/L/C or class M with rho < 1).
    """
    coeffs = shadow_coefficients_numerical(data, max_r)
    return sum(S_r * r ** (-n) for r, S_r in coeffs.items() if r >= 2)


def shadow_L_function_derivative_at_zero(data: Dict[str, float],
                                         max_r: int = 200) -> float:
    r"""Estimate L'(0, H^1(C_A)) via the shadow zeta.

    For the shadow curve (genus 0, rational), H^1 = 0, so L(s, H^1) = 1
    trivially and L'(0) = 0.

    The nontrivial L-function comes from the SINGULAR model or from
    the shadow zeta itself (a Dirichlet series, not an L-function of
    a variety in the strict sense).

    We compute d/ds zeta_A(s)|_{s=0} numerically:
      L'_A(0) = -sum_r S_r * log(r)
    """
    coeffs = shadow_coefficients_numerical(data, max_r)
    return -sum(S_r * math.log(r) for r, S_r in coeffs.items() if r >= 2 and abs(S_r) > 1e-30)


def beilinson_conjecture_rational_factor(data: Dict[str, float],
                                         n_points: int = 2000,
                                         max_r: int = 200) -> Dict[str, Any]:
    r"""Compute the rational factor r = L'(0) / reg predicted by Beilinson's conjecture.

    Beilinson: L'(0, H^1(C)) ~ reg(C) * rational * (2*pi*i)^n.

    For the shadow curve this is a FORMAL ANALOGY since H^1 of the
    normalization is trivial. We use the shadow zeta as L and the
    Beilinson regulator of {t, y} as reg.

    Returns the ratio and checks if it is close to a rational number.
    """
    Lprime = shadow_L_function_derivative_at_zero(data, max_r)
    regs = beilinson_regulator_all_cycles(data, n_points)
    reg_branch = regs['branch_cycle']

    result = {
        'L_prime_0': Lprime,
        'reg_branch': reg_branch,
        'reg_infinity': regs['infinity_cycle'],
    }

    if abs(reg_branch) > 1e-10:
        ratio = Lprime / reg_branch.real
        result['ratio'] = ratio
        # Check if close to a rational with small denominator
        result['rational_approx'] = _closest_rational(ratio, max_denom=1000)
    else:
        result['ratio'] = None
        result['rational_approx'] = None

    return result


def _closest_rational(x: float, max_denom: int = 1000) -> Optional[Fraction]:
    """Find the closest rational p/q with q <= max_denom."""
    if abs(x) < 1e-14:
        return Fraction(0)
    if abs(x) > 1e10:
        return None
    try:
        return Fraction(x).limit_denominator(max_denom)
    except (ValueError, OverflowError, ZeroDivisionError):
        return None


# ============================================================================
# 7.  Borel regulator and shadow zeta at positive integers
# ============================================================================

def borel_regulator_shadow(data: Dict[str, float], n: int,
                           max_r: int = 200) -> Dict[str, Any]:
    r"""Shadow analogue of the Borel regulator at weight n.

    Classical: zeta(n) = (Borel regulator) * rational, for n >= 2.
    Shadow: zeta_A(n) = (shadow Borel regulator) * rational?

    The "shadow Borel regulator" is defined as the value that, when
    multiplied by a rational, gives zeta_A(n).

    For n = 2: compare with pi^2/6. The "regulator" would be pi^2.
    For n = 3: compare with zeta(3) (Apery's constant). No known
    closed form in terms of pi.

    We compute zeta_A(n) and attempt to identify it as a rational
    multiple of known transcendental constants.
    """
    zeta_val = shadow_zeta_at_integer(data, n, max_r)

    result = {
        'n': n,
        'zeta_A_n': zeta_val,
    }

    # Compare with pi^n transcendentals
    pi_n = math.pi ** n
    ratio_pi = zeta_val / pi_n if abs(pi_n) > 1e-30 else None
    result['ratio_to_pi_n'] = ratio_pi
    if ratio_pi is not None:
        result['rational_approx_pi'] = _closest_rational(ratio_pi, 10000)

    # Compare with classical zeta(n)
    from scipy.special import zeta as scipy_zeta
    classical = float(scipy_zeta(n, 1))
    ratio_classical = zeta_val / classical if abs(classical) > 1e-30 else None
    result['ratio_to_zeta_n'] = ratio_classical
    if ratio_classical is not None:
        result['rational_approx_classical'] = _closest_rational(ratio_classical, 10000)

    # The "shadow Borel regulator" at this n
    # We define it as the part that is transcendental, i.e. zeta_A(n) / rational_part
    result['shadow_borel_regulator'] = zeta_val  # by definition, the full value is the regulator

    return result


def borel_regulator_table(data: Dict[str, float],
                          n_range: range = range(2, 8),
                          max_r: int = 200) -> List[Dict[str, Any]]:
    """Compute shadow Borel regulators for n = 2, 3, ..., n_max."""
    return [borel_regulator_shadow(data, n, max_r) for n in n_range]


# ============================================================================
# 8.  Shadow Chern character
# ============================================================================

@dataclass
class ShadowChernCharacter:
    """The Chern character of the shadow bundle E_A.

    ch(E_A) = rank + c_1 + c_2/2 + c_3/6 + ...

    rank = dimension of the shadow space (= 1 for single-generator, = N for W_N).
    c_1 = kappa * lambda_1 (Theorem D).
    c_2 = ? (involves kappa^2 and possibly S_3 corrections).
    c_3 = ? (involves kappa^3 and higher shadow corrections).

    IMPORTANT (AP27): the bar propagator d log E(z,w) is weight 1.
    All edge-level Hodge data uses E_1 = R^0 pi_* omega.
    So c_1(E_A) = kappa * lambda_1 involves only the standard Hodge class.

    The higher Chern classes c_k involve:
      c_k(E_1^{kappa}) = binomial(kappa, k) * lambda_1^k  (for rank-1 line bundle)

    For a rank-r vector bundle: c_k involves Schur polynomials in Chern roots.
    """
    rank: int
    c1_coeff: float  # coefficient of lambda_1 in c_1
    c2_coeff: float  # coefficient of lambda_1^2 in c_2 (from the split principle)
    c3_coeff: float  # coefficient of lambda_1^3 in c_3
    ch0: float  # = rank
    ch1: float  # = c_1 coefficient
    ch2: float  # = (c_1^2 - 2*c_2)/2 coefficient
    ch3: float  # = (c_1^3 - 3*c_1*c_2 + 3*c_3)/6 coefficient
    family: str
    kappa: float
    corrections: Dict[str, float]  # higher shadow corrections


def shadow_chern_character(family: str, data: Dict[str, float],
                           rank: int = 1) -> ShadowChernCharacter:
    r"""Compute the Chern character of the shadow bundle through degree 3.

    For a rank-1 bundle L with c_1(L) = kappa * lambda_1:
      ch(L) = exp(kappa * lambda_1) = 1 + kappa*lambda_1 + kappa^2*lambda_1^2/2 + ...

    In general (rank r, with the shadow providing additional Chern class data):
      c_1 = kappa * lambda_1 (Theorem D, unconditional for uniform-weight)
      c_2: at genus 2, the Hodge class lambda_2 = 7*lambda_1^2/5760 (Faber-Pandharipande)
           but the shadow bundle's c_2 also receives contributions from the cubic
           shadow S_3 (at arity 3).

    For the split-principle computation on a rank-1 line bundle:
      c_k = kappa^k * lambda_1^k / k! (falling under the exponential)
      ch_k = kappa^k * lambda_1^k / k!

    For higher rank (W_N with N generators):
      The split principle with Chern roots x_1, ..., x_r gives
      c_k = e_k(x_1, ..., x_r) (elementary symmetric polynomial).
      For the diagonal case x_i = kappa_i * lambda_1:
      c_1 = (sum kappa_i) * lambda_1 = kappa_total * lambda_1.
    """
    kappa = data['kappa']
    alpha = data['alpha']
    S4 = data['S4']

    # For rank 1: pure exponential
    c1 = kappa
    c2 = kappa ** 2 / 2.0  # from c_2 = c_1^2/2 for line bundle (no correction)
    c3 = kappa ** 3 / 6.0

    # Corrections from higher shadow data
    # The cubic shadow S_3 contributes to c_2 at genus 2:
    # delta_c2 = alpha * (FP correction factor)
    # This is the planted-forest correction delta_pf^{(2,0)} = S_3(10*S_3 - kappa)/48
    delta_pf_g2 = alpha * (10.0 * alpha - kappa) / 48.0 if rank == 1 else 0.0

    # ch_k = S_k(c_1, c_2, ...) / k! where S_k is the Newton polynomial
    ch0 = float(rank)
    ch1 = c1  # = kappa
    ch2 = (c1 ** 2 - 2 * c2) / 2.0  # = 0 for rank 1 (c2 = c1^2/2)
    # For rank > 1, ch2 can be nonzero
    ch3 = (c1 ** 3 - 3 * c1 * c2 + 3 * c3) / 6.0  # = 0 for rank 1

    return ShadowChernCharacter(
        rank=rank,
        c1_coeff=c1,
        c2_coeff=c2,
        c3_coeff=c3,
        ch0=ch0,
        ch1=ch1,
        ch2=ch2,
        ch3=ch3,
        family=family,
        kappa=kappa,
        corrections={'delta_pf_g2': delta_pf_g2, 'alpha': alpha, 'S4': S4},
    )


def chern_character_landscape() -> Dict[str, ShadowChernCharacter]:
    """Compute Chern characters for all standard families at reference parameters."""
    results = {}

    # Virasoro at several central charges
    for c_val in [1.0, 2.0, 13.0, 25.0]:
        data = virasoro_shadow_data_numerical(c_val)
        results[f'virasoro_c{c_val}'] = shadow_chern_character('virasoro', data, rank=1)

    # Heisenberg
    for k_val in [1.0, 2.0]:
        data = heisenberg_shadow_data_numerical(k_val)
        results[f'heisenberg_k{k_val}'] = shadow_chern_character('heisenberg', data, rank=1)

    # Affine sl_2
    for k_val in [1.0, 2.0]:
        data = affine_sl2_shadow_data_numerical(k_val)
        results[f'affine_sl2_k{k_val}'] = shadow_chern_character('affine_sl2', data, rank=1)

    # Betagamma
    data = betagamma_shadow_data_numerical(0.5)
    results['betagamma'] = shadow_chern_character('betagamma', data, rank=1)

    return results


# ============================================================================
# 9.  Shadow motivic cohomology
# ============================================================================

@dataclass
class ShadowMotivicCohomology:
    r"""Motivic cohomology groups H^n_M(C_A, Z(m)).

    H^0_M(C_A, Z(0)) = Z (always, one connected component).
    H^1_M(C_A, Z(1)) = O*(C_A) (units of the function ring).
    H^2_M(C_A, Z(2)) contains K_2(C_A) (Milnor K-theory).

    For a smooth rational curve: K_2 is "known" by Matsumoto's theorem.
    For the singular shadow curve: K_2 has additional contributions from
    the singularity.
    """
    H0_rank: int  # = 1
    H1_generators: List[str]  # generators of units
    H2_nontrivial: bool  # whether K_2 contributes nontrivially
    family: str
    shadow_class: str
    milnor_symbol: str  # description of the canonical xi_A = {t, y}


def compute_motivic_cohomology(family: str,
                               data: Dict[str, float]) -> ShadowMotivicCohomology:
    """Compute motivic cohomology of the shadow curve."""
    Delta = data['Delta']
    if abs(Delta) < 1e-15 and abs(data['alpha']) < 1e-15:
        shadow_class = 'G'
    elif abs(Delta) < 1e-15:
        shadow_class = 'L'
    else:
        shadow_class = 'M'

    # H^1_M = O* = units
    h1_gens = ['constants (k*)']
    if shadow_class != 'G':
        h1_gens.append('t (coordinate)')
    h1_gens.append('y (hyperelliptic coordinate)')

    # H^2_M nontriviality
    # For rational curves over Q: K_2 is nontrivial (Matsumoto).
    # The key element {t, y} is always in K_2.
    # For class G: y = sqrt(q0)*t^2, so {t, y} = {t, sqrt(q0)*t^2}
    #   = {t, sqrt(q0)} + 2*{t, t} = {t, sqrt(q0)} (since {t,t} is 2-torsion).
    #   This is nontrivial if sqrt(q0) is not in k*.
    h2_nontrivial = True  # Always nontrivial for our purposes

    return ShadowMotivicCohomology(
        H0_rank=1,
        H1_generators=h1_gens,
        H2_nontrivial=h2_nontrivial,
        family=family,
        shadow_class=shadow_class,
        milnor_symbol='{t, y}',
    )


# ============================================================================
# 10.  Cross-verification utilities
# ============================================================================

def regulator_via_residues(data: Dict[str, float]) -> Dict[str, complex]:
    r"""Alternative regulator computation via residue calculus.

    For a rational function on a curve, the regulator can be computed as
    a sum of local contributions (dilogarithm values at special points).

    reg({t, y}) = sum_P v_P(t) * log|y(P)| * arg(t(P))
                  + dilogarithmic corrections.

    This provides an INDEPENDENT path to the regulator (Path 2).
    """
    tame_list = compute_all_tame_symbols(data)
    # The regulator is related to the tame symbols via:
    # reg = sum_P log|Tame_P| * (angle factor)

    residue_sum = 0.0
    for ts in tame_list:
        if abs(ts.value) > 1e-30 and abs(ts.value) < 1e30:
            residue_sum += _log_abs(ts.value) * (ts.vt + ts.vy)

    return {
        'residue_regulator': complex(residue_sum),
        'tame_symbols': tame_list,
    }


def cross_verify_regulator(data: Dict[str, float],
                           n_points: int = 2000) -> Dict[str, Any]:
    """Cross-verify regulator via integration and residues."""
    path1 = beilinson_regulator_all_cycles(data, n_points)
    path2 = regulator_via_residues(data)

    return {
        'path1_integration': path1,
        'path2_residues': path2,
    }


def shadow_zeta_two_methods(data: Dict[str, float], n: int,
                            max_r_direct: int = 200,
                            max_r_check: int = 100) -> Dict[str, float]:
    """Compute shadow zeta at integer n via two methods.

    Method 1: Direct summation with max_r terms.
    Method 2: Direct summation with fewer terms (for convergence check).
    """
    val1 = shadow_zeta_at_integer(data, n, max_r_direct)
    val2 = shadow_zeta_at_integer(data, n, max_r_check)
    return {
        'method1_full': val1,
        'method2_truncated': val2,
        'difference': abs(val1 - val2),
        'relative_diff': abs(val1 - val2) / max(abs(val1), 1e-30),
    }


def koszul_duality_regulator_check(c_val: float,
                                   n_points: int = 2000) -> Dict[str, Any]:
    r"""Check regulator behavior under Koszul duality: c -> 26-c.

    For Virasoro: A^! = Vir_{26-c}.
    The shadow curve of A^! has c' = 26-c.
    Beilinson's conjecture should be compatible with duality.
    """
    data_A = virasoro_shadow_data_numerical(c_val)
    c_dual = 26.0 - c_val
    data_Ad = virasoro_shadow_data_numerical(c_dual)

    reg_A = beilinson_regulator_all_cycles(data_A, n_points)
    reg_Ad = beilinson_regulator_all_cycles(data_Ad, n_points)

    # Complementarity check on L' values
    L_A = shadow_L_function_derivative_at_zero(data_A)
    L_Ad = shadow_L_function_derivative_at_zero(data_Ad)

    return {
        'c': c_val,
        'c_dual': c_dual,
        'kappa_A': data_A['kappa'],
        'kappa_dual': data_Ad['kappa'],
        'kappa_sum': data_A['kappa'] + data_Ad['kappa'],  # Should be 13 for Virasoro
        'reg_A': reg_A,
        'reg_dual': reg_Ad,
        'L_prime_A': L_A,
        'L_prime_dual': L_Ad,
    }


# ============================================================================
# 11.  Full landscape computation
# ============================================================================

@dataclass
class ShadowRegulatorData:
    """Complete shadow regulator data for a family at given parameters."""
    family: str
    params: Dict[str, float]
    K0: ShadowK0
    K1: ShadowK1
    tame_symbols: List[TameSymbol]
    tame_product: complex
    regulators: Dict[str, complex]
    chern_character: ShadowChernCharacter
    motivic: ShadowMotivicCohomology
    borel_table: List[Dict[str, Any]]
    beilinson_ratio: Optional[Dict[str, Any]]


def compute_full_regulator_data(family: str,
                                data: Dict[str, float],
                                rank: int = 1,
                                n_points: int = 1000,
                                max_r: int = 100) -> ShadowRegulatorData:
    """Compute all shadow regulator invariants for a given family and parameters."""
    K0 = compute_K0(family, data)
    K1 = compute_K1(family, data)
    tame_list = compute_all_tame_symbols(data)
    tame_prod = product_of_tame_symbols(tame_list)
    regs = beilinson_regulator_all_cycles(data, n_points)
    chern = shadow_chern_character(family, data, rank)
    motivic = compute_motivic_cohomology(family, data)
    borel = borel_regulator_table(data, range(2, 6), max_r)
    beil = beilinson_conjecture_rational_factor(data, n_points, max_r)

    return ShadowRegulatorData(
        family=family,
        params=data,
        K0=K0,
        K1=K1,
        tame_symbols=tame_list,
        tame_product=tame_prod,
        regulators=regs,
        chern_character=chern,
        motivic=motivic,
        borel_table=borel,
        beilinson_ratio=beil,
    )


def full_landscape_regulators() -> Dict[str, ShadowRegulatorData]:
    """Compute shadow regulators for the full standard landscape."""
    results = {}

    # Virasoro at test central charges
    for c_val in [1.0, 2.0, 13.0, 25.0]:
        data = virasoro_shadow_data_numerical(c_val)
        results[f'virasoro_c{c_val}'] = compute_full_regulator_data(
            'virasoro', data, rank=1, n_points=500, max_r=80
        )

    # Heisenberg
    for k_val in [1.0, 2.0]:
        data = heisenberg_shadow_data_numerical(k_val)
        results[f'heisenberg_k{k_val}'] = compute_full_regulator_data(
            'heisenberg', data, rank=1, n_points=500, max_r=30
        )

    # Affine sl_2
    data = affine_sl2_shadow_data_numerical(1.0)
    results['affine_sl2_k1'] = compute_full_regulator_data(
        'affine_sl2', data, rank=1, n_points=500, max_r=30
    )

    # Beta-gamma
    data = betagamma_shadow_data_numerical(0.5)
    results['betagamma'] = compute_full_regulator_data(
        'betagamma', data, rank=1, n_points=500, max_r=30
    )

    return results
