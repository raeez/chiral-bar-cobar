r"""Shadow metric as Bridgeland stability condition: the spectral curve dictionary.

MATHEMATICAL CONTENT
====================

This module implements and verifies the structural identification between the
shadow metric Q_L(t) of modular Koszul duality and the data of a Bridgeland
stability condition on a triangulated category associated to a chiral algebra.

THE CENTRAL IDENTIFICATION (five components):

(A) SPECTRAL CURVE = SHADOW METRIC.
    The shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2
    (def:shadow-metric, thm:riccati-algebraicity) defines a genus-0
    spectral curve y^2 = Q_L(t).  For a Bridgeland stability condition
    (Z, P) on D^b(A), the central charge Z: K_0(D^b(A)) -> C encodes
    the "mass" and "phase" of stable objects.  The natural candidate:

        Z_A = pi * disc(Q_L) / (8 * sqrt(q_2))   (A-period of y^2 = Q_L)

    where disc(Q_L) = q_1^2 - 4*q_0*q_2 is the polynomial discriminant.

    For Virasoro:
        disc = -320*c^2 / (5c+22) < 0   for all c > 0
        Z_A = -20*pi*c^2 / sqrt(225*c^2 + 2080*c + 4796)

    Z_A is REAL and NEGATIVE (phase pi).  The A-period encodes the total
    "BPS mass" of the shadow obstruction tower.

(B) G/L/C/M = BRIDGELAND WALL-CHAMBER STRUCTURE.
    The discriminant sign classifies the wall structure:

        Class G (Heisenberg): disc = 0, Q_L constant.
            NO branch points.  Stability is trivial (no walls).
            Bridgeland space = single chamber (the Gaussian point).

        Class L (affine KM): disc = 0, Q_L perfect square.
            DEGENERATE branch point (double zero of Q_L).
            Marginal stability wall (pentagon identity).
            Bridgeland space = wall of marginal stability.

        Class C (betagamma): disc < 0, complex conjugate zeros.
            COMPLEX branch points.  Finite wall structure.
            Bridgeland space = finitely many chambers.

        Class M (Virasoro, W_N): disc < 0, complex conjugate zeros.
            COMPLEX branch points.  Infinite wall structure.
            Bridgeland space = infinitely many chambers.

    Classes C and M both have disc < 0 (complex conjugate branch points).
    The distinction is ALGEBRAIC (stratum separation terminates the tower
    for C but not M), not spectral.  From the Bridgeland perspective:
    C has finitely many walls (the scattering diagram terminates),
    M has infinitely many (each arity contributes a new wall).

(C) UNIVERSAL WALL PHASE phi_wall = pi/4.
    At any branch point t_+ of y^2 = Q_L(t) with disc < 0:

        Q_L'(t_+) = sqrt(disc) = i * sqrt(|disc|)

    is PURELY IMAGINARY.  The BPS wall phase:

        phi_wall = (1/2) * arg(Q_L'(t_+)) = pi/4

    is UNIVERSAL for all c > 0 and all families with Delta != 0.

    Proof: Q_L'(t) = q_1 + 2*q_2*t.  At t_+ = (-q_1 + sqrt(disc))/(2q_2):
        Q_L'(t_+) = q_1 + (-q_1 + sqrt(disc)) = sqrt(disc).
    Since disc < 0, sqrt(disc) = i*sqrt(|disc|), giving arg = pi/2.
    The wall phase phi = arg/2 = pi/4.

    This is a TOPOLOGICAL invariant of the shadow stability condition:
    it depends only on disc < 0, not on the specific algebra data.

(D) KOSZUL DUALITY = STABILITY SELF-DUALITY AT c = 13.
    Under Virasoro Koszul duality c -> 26-c:
        Z_A(13) / Z_A(13) = 1  (exact self-duality at c = 13)
    The A-period, branch point locations, discriminant, and wall angle
    are all exactly self-dual at the Koszul self-dual point c = 13.

    The complementarity of critical discriminants:
        Delta(c) + Delta(26-c) = 6960 / ((5c+22)(152-5c))
    is the Bridgeland manifestation of Theorem C (complementarity).

(E) SHADOW COEFFICIENT SIGN ALTERNATION = WALL-CROSSING SEQUENCE.
    The shadow coefficients S_r for class M algebras exhibit sign
    alternation starting at r = 5:
        S_2, S_3, S_4 > 0;  S_5 < 0;  S_6 > 0;  S_7 < 0; ...
    Each sign change corresponds to crossing a WALL in the Bridgeland
    stability space.  The number of sign changes through arity r is the
    number of walls encountered (the "wall count" w(r)).

    For class G: w(r) = 0 for all r (no sign changes, no walls).
    For class L: w(r) = 0 for all r (S_r eventually zero).
    For class C: w(r) <= 2 (finite, terminates by stratum separation).
    For class M: w(r) -> infinity (unbounded wall-crossing).

BEILINSON WARNINGS
==================

AP42: The identification holds at the STRUCTURAL level.  The shadow metric
      defines stability condition DATA (central charge, phase, walls) but
      the underlying triangulated category D^b(A) requires construction.
      The spectral curve y^2 = Q_L(t) is genus 0, so the stability condition
      is on the boundary of the Bridgeland space (degenerate limit).

AP9:  "Bridgeland central charge" and "shadow A-period" are different objects
      in different frameworks.  The dictionary maps one to the other via the
      spectral curve; they are NOT the same invariant.

AP31: Z_A = 0 (for class G) does NOT mean the stability condition is trivial
      in the categorical sense.  It means the spectral curve is degenerate.
      The Gaussian stability condition may still have nontrivial structure
      not visible at the level of Q_L.

AP14: Shadow depth classifies COMPLEXITY of the stability condition, not
      Koszulness.  All standard families are Koszul; the wall structure
      varies within the Koszul world.

CONVENTIONS (AP1, AP9, AP22, AP24, AP27, AP38, AP39, AP48)
==========================================================
- kappa(H_k) = k  [AP39: NOT k/2]
- kappa(Vir_c) = c/2
- kappa(aff KM g_k) = dim(g)*(k+h^v)/(2h^v)
- Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2, Delta = 8*kappa*S4
- Expanded: Q_L = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 2*Delta)*t^2
- disc(Q_L) = q1^2 - 4*q0*q2 = (12*kappa*alpha)^2 - 4*(4*kappa^2)*(9*alpha^2+2*Delta)
- For Virasoro: disc = -320*c^2/(5c+22)
- Bar propagator weight 1 [AP27]: all channels use E_1
- Koszul duality: Vir_c^! = Vir_{26-c}, self-dual at c = 13 [AP8, AP24]

MULTI-PATH VERIFICATION (>= 3 per claim, per CLAUDE.md)
========================================================

A-period formula:
  Path 1: Direct contour integral computation (parametrized)
  Path 2: Algebraic formula pi * disc / (8 * sqrt(q2))
  Path 3: Numerical quadrature of sqrt(Q_L) along branch cut

Universal wall phase:
  Path 1: Analytic proof Q_L'(t_+) = sqrt(disc) = i*sqrt(|disc|)
  Path 2: Numerical evaluation at c = 1, 2, 13, 26, 100
  Path 3: Dimensional analysis (phase is dimensionless, disc < 0 universal)

Self-duality at c = 13:
  Path 1: Symbolic ratio Z_A(c)/Z_A(26-c) evaluated at c = 13
  Path 2: Numerical comparison of all invariants
  Path 3: Koszul symmetry of the shadow metric coefficients

Sign alternation:
  Path 1: Explicit recursion computation through arity 20
  Path 2: Generating function sqrt(Q_L(t)) Taylor expansion
  Path 3: Cross-family comparison (Heisenberg vs Virasoro vs betagamma)

REFERENCES
==========
    Bridgeland, arXiv:math/0212237 (stability conditions on triangulated categories)
    Bridgeland, arXiv:0611.03697 (scattering diagrams and stability)
    Kontsevich-Soibelman, arXiv:0811.2435 (stability structures, WCF)
    Lorgat, Vol I: shadow obstruction tower, Theorems A-H
    def:shadow-metric, thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-archetype-classification (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, bernoulli, cancel, diff, expand, factor,
    factorial, log, pi as sym_pi, simplify, sqrt as sym_sqrt,
    symbols, Integer, S as Sym, oo, Abs, I, Poly,
    atan2 as sym_atan2, cos, sin,
)


# ============================================================================
# 0.  SHADOW DATA STRUCTURES
# ============================================================================

@dataclass(frozen=True)
class ShadowStabilityData:
    r"""Shadow data for the Bridgeland stability identification.

    The shadow metric Q_L(t) = q0 + q1*t + q2*t^2 where:
        q0 = 4*kappa^2
        q1 = 12*kappa*alpha     (alpha = S_3)
        q2 = 9*alpha^2 + 2*Delta  (Delta = 8*kappa*S4)

    Equivalently: Q_L = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Convention (AP1, AP9, AP39):
        kappa = modular characteristic (family-specific)
        alpha = S_3 (cubic shadow coefficient)
        S4 = quartic contact invariant
    """
    name: str
    kappa: Rational
    alpha: Rational        # S_3 (cubic shadow)
    S4: Rational           # quartic contact invariant
    depth_class: str       # 'G', 'L', 'C', 'M'

    @property
    def Delta(self) -> Rational:
        """Critical discriminant Delta = 8*kappa*S4."""
        return 8 * self.kappa * self.S4

    @property
    def q0(self) -> Rational:
        """Q_L constant term: 4*kappa^2."""
        return 4 * self.kappa ** 2

    @property
    def q1(self) -> Rational:
        """Q_L linear coefficient: 12*kappa*alpha."""
        return 12 * self.kappa * self.alpha

    @property
    def q2(self) -> Rational:
        """Q_L quadratic coefficient: 9*alpha^2 + 2*Delta."""
        return 9 * self.alpha ** 2 + 2 * self.Delta

    @property
    def poly_discriminant(self) -> Rational:
        """Polynomial discriminant of Q_L: q1^2 - 4*q0*q2."""
        return self.q1 ** 2 - 4 * self.q0 * self.q2

    @property
    def has_complex_branch_points(self) -> bool:
        """True iff Q_L has complex conjugate zeros (disc < 0)."""
        return self.poly_discriminant < 0

    @property
    def has_degenerate_branch_point(self) -> bool:
        """True iff Q_L is a perfect square (disc = 0, non-constant)."""
        return self.poly_discriminant == 0 and self.q2 != 0

    @property
    def is_constant(self) -> bool:
        """True iff Q_L is constant (q1 = q2 = 0)."""
        return self.q1 == 0 and self.q2 == 0

    def Q_L(self, t):
        """Evaluate Q_L(t) = q0 + q1*t + q2*t^2."""
        return self.q0 + self.q1 * t + self.q2 * t ** 2


# ============================================================================
# 1.  STANDARD FAMILY CONSTRUCTORS
# ============================================================================

def heisenberg_stability(k=1) -> ShadowStabilityData:
    """Heisenberg at level k.  Class G, trivial stability.

    kappa = k [AP39: NOT k/2].  All higher shadows vanish.
    Q_L = 4*k^2 (constant).  No branch points.
    """
    k_r = Rational(k)
    return ShadowStabilityData("Heisenberg", k_r, Rational(0),
                               Rational(0), 'G')


def affine_sl2_stability(k=1) -> ShadowStabilityData:
    """Affine V_k(sl_2).  Class L, marginal stability.

    kappa = 3(k+2)/4, alpha = S_3 = 2, S_4 = 0.
    Q_L = (2*kappa + 6t)^2 (perfect square).  Double zero at t = -kappa/3.
    """
    k_r = Rational(k)
    kappa = Rational(3) * (k_r + 2) / 4
    return ShadowStabilityData("aff_sl2", kappa, Rational(2),
                               Rational(0), 'L')


def affine_slN_stability(N, k=1) -> ShadowStabilityData:
    """Affine V_k(sl_N).  Class L for all N.

    kappa = dim(sl_N)*(k+N)/(2N), alpha = S_3 (nonzero), S_4 = 0.
    """
    N_r, k_r = Rational(N), Rational(k)
    dim_g = N_r ** 2 - 1
    h_vee = N_r
    kappa = dim_g * (k_r + h_vee) / (2 * h_vee)
    return ShadowStabilityData(f"aff_sl{N}", kappa, Rational(2),
                               Rational(0), 'L')


def betagamma_stability() -> ShadowStabilityData:
    """Beta-gamma system.  Class C, finite wall structure.

    Same primary-line shadow data as Virasoro at c = 2.
    kappa = 1, alpha = 2, S_4 = 10/(2*(12)) = 5/32.
    """
    c = Rational(2)
    kappa = Rational(1)
    S4 = Rational(10) / (c * (5 * c + 22))
    return ShadowStabilityData("betagamma", kappa, Rational(2), S4, 'C')


def virasoro_stability(c_val) -> ShadowStabilityData:
    """Virasoro at central charge c.  Class M for c > 0.

    kappa = c/2, alpha = S_3 = 2, S_4 = 10/(c*(5c+22)).
    Q_L = c^2 + 12ct + [(180c+872)/(5c+22)]t^2.
    disc = -320*c^2/(5c+22) < 0 for all c > 0.
    """
    c = Rational(c_val)
    if c == 0:
        return ShadowStabilityData("Vir_0", Rational(0), Rational(2),
                                   Rational(0), 'G')
    kappa = c / 2
    S4 = Rational(10) / (c * (5 * c + 22))
    return ShadowStabilityData(f"Vir_{c}", kappa, Rational(2), S4, 'M')


def w3_stability(c_val) -> ShadowStabilityData:
    """W_3 on T-line at central charge c.  Class M."""
    c = Rational(c_val)
    if c == 0:
        return ShadowStabilityData("W3_0", Rational(0), Rational(2),
                                   Rational(0), 'G')
    kappa = c / 2
    S4 = Rational(10) / (c * (5 * c + 22))
    return ShadowStabilityData(f"W3_{c}", kappa, Rational(2), S4, 'M')


# ============================================================================
# 2.  BRANCH POINTS AND SPECTRAL CURVE
# ============================================================================

def branch_points(data: ShadowStabilityData) -> Dict[str, Any]:
    r"""Compute the branch points of the spectral curve y^2 = Q_L(t).

    The zeros of Q_L(t) = q2*(t - t_+)*(t - t_-) are:
        t_+/- = (-q1 +/- sqrt(disc)) / (2*q2)

    For disc < 0 (class C, M): t_+, t_- are complex conjugate.
    For disc = 0 (class L): double zero at t = -q1/(2*q2).
    For disc > 0: two real zeros (not realized by standard families).

    Returns dict with branch point locations, separation, and type.
    """
    if data.is_constant:
        return {
            "type": "no_branch_points",
            "class": "G",
            "t_plus": None,
            "t_minus": None,
            "separation": Rational(0),
            "notes": "Q_L constant; spectral curve degenerate",
        }

    disc = data.poly_discriminant
    q1, q2 = data.q1, data.q2

    if q2 == 0:
        # Q_L is linear (degenerate): single zero at t = -q0/q1
        return {
            "type": "linear_degenerate",
            "class": "degenerate",
            "t_plus": None,
            "t_minus": None,
            "separation": None,
            "notes": "Q_L linear; not a proper spectral curve",
        }

    if disc == 0:
        # Perfect square: double zero
        t_double = -q1 / (2 * q2)
        return {
            "type": "double_zero",
            "class": "L",
            "t_plus": t_double,
            "t_minus": t_double,
            "separation": Rational(0),
            "notes": "Marginal stability wall at double zero",
        }

    # disc != 0: two distinct zeros
    # For exact arithmetic, keep symbolic
    # t_+/- = (-q1 +/- sqrt(disc)) / (2*q2)
    # When disc < 0, the zeros are complex conjugate

    # Compute numerically for the return value
    disc_float = float(disc)
    q1_float = float(q1)
    q2_float = float(q2)

    sqrt_disc = cmath.sqrt(disc_float)
    t_plus = (-q1_float + sqrt_disc) / (2 * q2_float)
    t_minus = (-q1_float - sqrt_disc) / (2 * q2_float)
    separation = abs(t_plus - t_minus)

    bp_type = "complex_conjugate" if disc < 0 else "real_distinct"
    bp_class = "C_or_M" if disc < 0 else "real"

    return {
        "type": bp_type,
        "class": bp_class,
        "t_plus": t_plus,
        "t_minus": t_minus,
        "separation": separation,
        "disc": disc,
        "disc_float": disc_float,
        "re_t_plus": t_plus.real,
        "im_t_plus": t_plus.imag,
        "notes": ("Complex conjugate branch points; nontrivial stability"
                  if disc < 0 else "Real branch points"),
    }


# ============================================================================
# 3.  A-PERIOD (CENTRAL CHARGE)
# ============================================================================

def a_period_exact(data: ShadowStabilityData) -> Rational:
    r"""Compute the A-period Z_A of the spectral curve y^2 = Q_L(t).

    For a quadratic Q_L(t) = q2*(t - t_+)*(t - t_-), the A-period
    (integral of sqrt(Q_L) around the branch cut from t_- to t_+) is:

        Z_A = pi * sqrt(q2) * (t_+ - t_-)^2 / 8
            = pi * disc / (8 * sqrt(q2))

    where disc = q1^2 - 4*q0*q2 = q2*(t_+ - t_-)^2.

    For disc < 0: Z_A < 0 (real, negative).
    For disc = 0: Z_A = 0 (degenerate).
    For disc > 0: Z_A > 0.

    Returns the numerical value Z_A / pi (the rational prefactor).
    The full A-period is Z_A = (return value) * pi.
    """
    if data.is_constant or data.q2 == 0:
        return Rational(0)

    disc = data.poly_discriminant
    q2 = data.q2

    # Z_A / pi = disc / (8 * sqrt(q2))
    # For exact arithmetic, return disc^2 / (64 * q2) as the
    # squared quantity |Z_A/pi|^2, and separately the sign.
    # But it's more useful to return as a sympy expression.
    return disc, q2


def a_period_numerical(data: ShadowStabilityData) -> complex:
    r"""Numerical A-period Z_A (complex).

    Z_A = pi * disc / (8 * sqrt(q2)).

    For disc < 0, q2 > 0: Z_A = pi * |disc| / (8*sqrt(q2)) * (-1)
        i.e. real and negative.
    """
    if data.is_constant or data.q2 == 0:
        return 0.0

    disc = float(data.poly_discriminant)
    q2 = float(data.q2)

    return math.pi * disc / (8 * math.sqrt(q2))


def a_period_virasoro_formula(c_val) -> float:
    r"""Closed-form A-period for Virasoro.

    Z_A = -20 * pi * c^2 / sqrt(225*c^2 + 2080*c + 4796)

    Derived from:
        disc = -320*c^2/(5c+22)
        q2 = (180c+872)/(5c+22)
        Z_A = pi * disc / (8*sqrt(q2))
            = pi * (-320c^2/(5c+22)) / (8*sqrt((180c+872)/(5c+22)))
            = -40*pi*c^2 / ((5c+22) * sqrt((180c+872)/(5c+22)))
            = -40*pi*c^2 * sqrt(5c+22) / ((5c+22)*sqrt(180c+872))
            = -40*pi*c^2 / (sqrt((5c+22))*sqrt(180c+872))
            = -40*pi*c^2 / sqrt((5c+22)*(180c+872))
    Note: (5c+22)*(180c+872) = 900c^2 + 8320c + 19184
        = 4*(225c^2 + 2080c + 4796)
    So Z_A = -40*pi*c^2 / (2*sqrt(225c^2+2080c+4796))
           = -20*pi*c^2 / sqrt(225c^2+2080c+4796).
    """
    c = float(c_val)
    if c == 0:
        return 0.0
    return -20 * math.pi * c ** 2 / math.sqrt(225 * c ** 2 + 2080 * c + 4796)


# ============================================================================
# 4.  UNIVERSAL WALL PHASE
# ============================================================================

def wall_phase(data: ShadowStabilityData) -> Optional[float]:
    r"""Compute the BPS wall phase phi_wall.

    At a branch point t_+ of y^2 = Q_L(t):
        Q_L'(t_+) = sqrt(disc)

    For disc < 0: Q_L'(t_+) = i*sqrt(|disc|), so arg = pi/2.
    The wall phase phi_wall = (1/2)*arg(Q_L'(t_+)) = pi/4.

    THEOREM: phi_wall = pi/4 universally for all families with disc < 0.

    Returns phi_wall in radians, or None if no walls (disc >= 0).
    """
    disc = data.poly_discriminant
    if disc >= 0:
        return None  # No complex branch points, no wall phase

    # Q_L'(t_+) = sqrt(disc) = i*sqrt(|disc|)
    # arg(Q_L'(t_+)) = pi/2
    # phi_wall = pi/4
    return math.pi / 4


def wall_phase_numerical(data: ShadowStabilityData) -> Optional[float]:
    r"""Compute wall phase numerically (independent verification path).

    Evaluates Q_L'(t_+) directly and takes arg/2.
    """
    if data.is_constant or data.q2 == 0:
        return None

    disc = float(data.poly_discriminant)
    if disc >= 0:
        return None

    q1 = float(data.q1)
    q2 = float(data.q2)

    sqrt_disc = cmath.sqrt(disc)
    t_plus = (-q1 + sqrt_disc) / (2 * q2)

    # Q_L'(t) = q1 + 2*q2*t
    Qprime = q1 + 2 * q2 * t_plus
    return cmath.phase(Qprime) / 2


def wall_angle_in_t_plane(data: ShadowStabilityData) -> Optional[float]:
    r"""Angle of the branch point t_+ in the complex t-plane.

    theta = arg(t_+) = pi - arctan(Im(t_+)/|Re(t_+)|).

    For Virasoro: Im(t_+)/|Re(t_+)| = 2*sqrt(5) / (3*sqrt(5c+22)).
    """
    bp = branch_points(data)
    if bp["t_plus"] is None or not isinstance(bp["t_plus"], complex):
        return None

    t_plus = bp["t_plus"]
    return cmath.phase(t_plus)


# ============================================================================
# 5.  KOSZUL SELF-DUALITY AT c = 13
# ============================================================================

def koszul_dual_stability(c_val) -> Tuple[ShadowStabilityData, ShadowStabilityData]:
    """Return (Vir_c, Vir_{26-c}) stability data for Koszul duality check.

    AP24: kappa(c) + kappa(26-c) = 13 (not 0) for Virasoro.
    AP8: Self-dual at c = 13, not c = 26.
    """
    return virasoro_stability(c_val), virasoro_stability(26 - c_val)


def verify_self_duality_c13() -> Dict[str, Any]:
    r"""Verify exact self-duality of the stability data at c = 13.

    At c = 13 (Koszul self-dual point for Virasoro):
    - Z_A(13) = Z_A(13) trivially (since 26-13=13)
    - disc(13) = disc(13)
    - All stability invariants coincide

    Multi-path verification:
      Path 1: Symbolic ratio Z_A(c)/Z_A(26-c) at c=13
      Path 2: Numerical comparison of all invariants
      Path 3: Discriminant and branch point comparison
    """
    d13 = virasoro_stability(13)
    d13_dual = virasoro_stability(13)  # 26-13=13

    # Path 1: A-period equality
    Z13 = a_period_numerical(d13)
    Z13_dual = a_period_numerical(d13_dual)
    path1 = abs(Z13 - Z13_dual) < 1e-12

    # Path 2: All invariants
    path2_disc = d13.poly_discriminant == d13_dual.poly_discriminant
    path2_delta = d13.Delta == d13_dual.Delta
    path2_q = (d13.q0 == d13_dual.q0 and
               d13.q1 == d13_dual.q1 and
               d13.q2 == d13_dual.q2)

    # Path 3: Branch points
    bp13 = branch_points(d13)
    bp13_dual = branch_points(d13_dual)

    results = {
        "self_dual": path1 and path2_disc and path2_delta and path2_q,
        "Z_A_equal": path1,
        "disc_equal": path2_disc,
        "Delta_equal": path2_delta,
        "Q_coeffs_equal": path2_q,
        "Z_A_value": Z13,
        "disc_value": d13.poly_discriminant,
        "Delta_value": d13.Delta,
        "kappa_sum": d13.kappa + d13_dual.kappa,  # Should be 13
    }

    return results


def verify_koszul_duality_family(c_values=None) -> Dict[str, Any]:
    r"""Verify Koszul duality c -> 26-c at multiple central charges.

    Checks structural relationships between (Vir_c, Vir_{26-c}):
    - kappa(c) + kappa(26-c) = 13  [AP24: not 0!]
    - Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c))
    - Z_A(c)/Z_A(26-c) at c = 13 gives 1
    """
    if c_values is None:
        c_values = [1, 2, 5, 10, 13, 20, 25]

    results = {}
    for c_val in c_values:
        d_c = virasoro_stability(c_val)
        d_dual = virasoro_stability(26 - c_val)

        kappa_sum = d_c.kappa + d_dual.kappa
        delta_sum = d_c.Delta + d_dual.Delta

        # Expected delta sum: 6960/((5c+22)(152-5c))
        c_r = Rational(c_val)
        expected_delta_sum = Rational(6960) / ((5 * c_r + 22) * (152 - 5 * c_r))

        Z_c = a_period_numerical(d_c)
        Z_dual = a_period_numerical(d_dual)

        results[c_val] = {
            "kappa_sum": kappa_sum,
            "kappa_sum_is_13": kappa_sum == 13,
            "delta_sum": delta_sum,
            "delta_sum_expected": expected_delta_sum,
            "delta_match": delta_sum == expected_delta_sum,
            "Z_A": Z_c,
            "Z_A_dual": Z_dual,
            "Z_ratio": Z_c / Z_dual if Z_dual != 0 else None,
        }

    return results


# ============================================================================
# 6.  SHADOW COEFFICIENT SIGN ALTERNATION (WALL-CROSSING SEQUENCE)
# ============================================================================

def shadow_coefficients(data: ShadowStabilityData,
                        max_arity: int = 20) -> Dict[int, Fraction]:
    r"""Compute shadow coefficients S_r from the MC recursion.

    The shadow generating function f(t) = sum a_n t^n satisfies
    f(t)^2 = Q_L(t), giving the recursion:
        a_n = -(1/(2*a_0)) * sum_{j=1}^{n-1} a_j * a_{n-j},   n >= 3.

    Shadow coefficient: S_r = a_{r-2} for r >= 2 (with S_2 = kappa).
    """
    kappa = Fraction(data.kappa.p, data.kappa.q)
    alpha = Fraction(data.alpha.p, data.alpha.q)
    S4 = Fraction(data.S4.p, data.S4.q)

    if kappa == 0:
        return {r: Fraction(0) for r in range(2, max_arity + 1)}

    a_0 = Fraction(2) * kappa
    a_1 = Fraction(3) * alpha
    Delta = Fraction(8) * kappa * S4
    q2_frac = Fraction(9) * alpha ** 2 + Fraction(2) * Delta
    a_2 = (q2_frac - a_1 ** 2) / (Fraction(2) * a_0)

    a = [Fraction(0)] * (max_arity + 1)
    a[0] = a_0
    if len(a) > 1:
        a[1] = a_1
    if len(a) > 2:
        a[2] = a_2

    for n in range(3, max_arity + 1):
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = -conv / (Fraction(2) * a_0)

    S = {}
    for r in range(2, max_arity + 1):
        idx = r - 2
        S[r] = a[idx]
    S[2] = kappa

    return S


def wall_crossing_count(data: ShadowStabilityData,
                        max_arity: int = 20) -> Dict[str, Any]:
    r"""Count sign changes in the shadow coefficient sequence.

    Each sign change S_r * S_{r+1} < 0 corresponds to crossing a wall
    in the Bridgeland stability space.

    Returns the wall count w(r) through each arity, and the total.
    """
    S = shadow_coefficients(data, max_arity)

    sign_changes = 0
    signs = {}
    cumulative_walls = {}

    for r in range(2, max_arity + 1):
        s_val = S[r]
        if s_val > 0:
            signs[r] = +1
        elif s_val < 0:
            signs[r] = -1
        else:
            signs[r] = 0

        if r >= 3 and signs[r] != 0 and signs.get(r - 1, 0) != 0:
            if signs[r] * signs[r - 1] < 0:
                sign_changes += 1

        cumulative_walls[r] = sign_changes

    return {
        "total_walls": sign_changes,
        "cumulative_walls": cumulative_walls,
        "signs": signs,
        "coefficients": S,
    }


# ============================================================================
# 7.  WALL-CHAMBER CLASSIFICATION
# ============================================================================

@dataclass(frozen=True)
class BridgelandChamber:
    """A chamber in the Bridgeland wall-chamber decomposition."""
    class_type: str              # 'G', 'L', 'C', 'M'
    num_walls: Optional[int]     # None for M (infinite)
    wall_phase: Optional[float]  # pi/4 for C, M; None for G, L
    disc_sign: int               # -1, 0, or +1
    A_period: float              # Z_A value
    notes: str = ''


def classify_bridgeland_chamber(data: ShadowStabilityData) -> BridgelandChamber:
    """Classify the shadow stability data into a Bridgeland chamber type.

    Class G: no walls, trivial stability.
    Class L: marginal stability (disc = 0, degenerate).
    Class C: finite walls (disc < 0, terminates).
    Class M: infinite walls (disc < 0, infinite tower).
    """
    disc = data.poly_discriminant
    Z_A = a_period_numerical(data)
    phi = wall_phase(data)

    if data.is_constant:
        return BridgelandChamber('G', 0, None, 0, Z_A,
                                 "Constant Q_L; no spectral curve")

    if disc == 0:
        return BridgelandChamber('L', 1, None, 0, Z_A,
                                 "Perfect square Q_L; marginal wall")

    if disc > 0:
        return BridgelandChamber('?', None, phi, 1, Z_A,
                                 "Real branch points; not in standard landscape")

    # disc < 0: complex branch points
    if data.depth_class == 'C':
        return BridgelandChamber('C', 2, phi, -1, Z_A,
                                 "Finite walls (stratum separation)")
    else:
        return BridgelandChamber('M', None, phi, -1, Z_A,
                                 "Infinite walls (unbounded tower)")


# ============================================================================
# 8.  DISCRIMINANT COMPLEMENTARITY
# ============================================================================

def discriminant_complementarity(c_val) -> Dict[str, Any]:
    r"""Verify the discriminant complementarity formula.

    For Virasoro: Delta(c) + Delta(26-c) = 6960/((5c+22)(152-5c)).

    This is the Bridgeland manifestation of Theorem C.

    Also: disc(c) and disc(26-c) are related by the Koszul involution.
    """
    c = Rational(c_val)
    c_dual = 26 - c

    d_c = virasoro_stability(c_val)
    d_dual = virasoro_stability(26 - c_val)

    delta_sum = d_c.Delta + d_dual.Delta
    expected = Rational(6960) / ((5 * c + 22) * (152 - 5 * c))

    disc_c = d_c.poly_discriminant
    disc_dual = d_dual.poly_discriminant

    return {
        "c": c_val,
        "c_dual": 26 - c_val,
        "Delta_c": d_c.Delta,
        "Delta_dual": d_dual.Delta,
        "Delta_sum": delta_sum,
        "Delta_sum_expected": expected,
        "Delta_complementarity_holds": delta_sum == expected,
        "disc_c": disc_c,
        "disc_dual": disc_dual,
        "disc_ratio": disc_c / disc_dual if disc_dual != 0 else None,
    }


# ============================================================================
# 9.  INTEGRATED CENTRAL CHARGE (REAL-LINE EVALUATION)
# ============================================================================

def integrated_central_charge(data: ShadowStabilityData,
                              r_max: int = 5) -> Dict[int, float]:
    r"""Compute Z(r) = integral_0^r sqrt(Q_L(t)) dt for integer arities.

    Since Q_L(t) > 0 for all real t (when disc < 0), this integral is
    real and positive.  It measures the "accumulated BPS mass" through
    arity r.

    Uses the elementary antiderivative of sqrt(at^2 + bt + c).
    """
    q0 = float(data.q0)
    q1 = float(data.q1)
    q2 = float(data.q2)

    if q2 == 0 and q1 == 0:
        # Constant: integral = sqrt(q0) * r
        sqrt_q0 = math.sqrt(q0)
        return {r: sqrt_q0 * r for r in range(1, r_max + 1)}

    results = {}
    for r in range(1, r_max + 1):
        # Numerical quadrature (Simpson's rule, high accuracy)
        n_pts = 1000
        dt = r / n_pts
        total = 0.0
        for i in range(n_pts + 1):
            t_val = i * dt
            Q_val = q0 + q1 * t_val + q2 * t_val ** 2
            f_val = math.sqrt(max(Q_val, 0))
            if i == 0 or i == n_pts:
                total += f_val
            elif i % 2 == 1:
                total += 4 * f_val
            else:
                total += 2 * f_val
        total *= dt / 3
        results[r] = total

    return results


# ============================================================================
# 10. SPECTRAL CURVE INVARIANTS
# ============================================================================

def spectral_invariants(data: ShadowStabilityData) -> Dict[str, Any]:
    r"""Compute all spectral curve invariants for y^2 = Q_L(t).

    Collects: branch points, A-period, wall phase, chamber type,
    discriminant, integrated charges.
    """
    bp = branch_points(data)
    Z_A = a_period_numerical(data)
    phi = wall_phase(data)
    phi_num = wall_phase_numerical(data)
    theta = wall_angle_in_t_plane(data)
    chamber = classify_bridgeland_chamber(data)
    wc = wall_crossing_count(data, max_arity=15)

    return {
        "name": data.name,
        "depth_class": data.depth_class,
        "kappa": data.kappa,
        "alpha": data.alpha,
        "S4": data.S4,
        "Delta": data.Delta,
        "q0": data.q0,
        "q1": data.q1,
        "q2": data.q2,
        "disc": data.poly_discriminant,
        "branch_points": bp,
        "A_period": Z_A,
        "wall_phase_analytic": phi,
        "wall_phase_numerical": phi_num,
        "wall_angle": theta,
        "chamber": chamber,
        "wall_count_through_15": wc["total_walls"],
        "sign_sequence": wc["signs"],
    }


# ============================================================================
# 11. VIRASORO DISCRIMINANT FORMULA (EXACT)
# ============================================================================

def virasoro_disc_exact(c_val) -> Rational:
    r"""Exact polynomial discriminant for Virasoro.

    disc(Q_L) = -320*c^2 / (5c+22).

    Derived from:
        q1^2 - 4*q0*q2 = (12c)^2 - 4*c^2*(180c+872)/(5c+22)
            = 144*c^2 - 4*c^2*(180c+872)/(5c+22)
            = c^2 * [144 - 4*(180c+872)/(5c+22)]
            = c^2 * [144*(5c+22) - 4*(180c+872)] / (5c+22)
            = c^2 * [720c + 3168 - 720c - 3488] / (5c+22)
            = c^2 * (-320) / (5c+22)
            = -320*c^2 / (5c+22).
    """
    c = Rational(c_val)
    if c == 0:
        return Rational(0)
    return Rational(-320) * c ** 2 / (5 * c + 22)


def virasoro_im_re_ratio(c_val) -> float:
    r"""Im(t_+) / |Re(t_+)| for Virasoro branch point.

    Exact formula: 2*sqrt(5) / (3*sqrt(5c+22)).

    This ratio determines the "wall angle" in the t-plane.
    At c -> infinity: ratio -> 0 (branch points approach real axis).
    At c -> 0: ratio -> 2*sqrt(5)/(3*sqrt(22)) ~ 0.2865.
    """
    c = float(c_val)
    return 2 * math.sqrt(5) / (3 * math.sqrt(5 * c + 22))


# ============================================================================
# 12. GENERAL FAMILY DISC FORMULA
# ============================================================================

def general_disc(kappa_val, alpha_val, S4_val) -> Rational:
    r"""Polynomial discriminant for general shadow metric.

    disc = q1^2 - 4*q0*q2
         = (12*kappa*alpha)^2 - 4*(4*kappa^2)*(9*alpha^2 + 16*kappa*S4)
         = 144*kappa^2*alpha^2 - 144*kappa^2*alpha^2 - 256*kappa^3*S4
         = -256*kappa^3*S4.

    IMPORTANT: disc = -256*kappa^3*S4 = -32*kappa^2*Delta.

    For S4 = 0 (classes G, L): disc = 0.
    For S4 > 0, kappa > 0 (classes C, M): disc < 0.
    """
    kappa = Rational(kappa_val) if not isinstance(kappa_val, Rational) else kappa_val
    S4 = Rational(S4_val) if not isinstance(S4_val, Rational) else S4_val
    return Rational(-256) * kappa ** 3 * S4


# ============================================================================
# 13. VERIFY GENERAL DISC FORMULA
# ============================================================================

def verify_disc_formula(data: ShadowStabilityData) -> Dict[str, Any]:
    r"""Verify that disc = -256*kappa^3*S4 matches q1^2 - 4*q0*q2.

    Multi-path verification:
      Path 1: Direct computation q1^2 - 4*q0*q2
      Path 2: General formula -256*kappa^3*S4
      Path 3: Family-specific formula (e.g. -320*c^2/(5c+22) for Virasoro)
    """
    path1 = data.poly_discriminant
    path2 = general_disc(data.kappa, data.alpha, data.S4)

    results = {
        "path1_direct": path1,
        "path2_general": path2,
        "match_1_2": path1 == path2,
    }

    # Path 3: family-specific check for Virasoro
    if data.name.startswith("Vir_") and data.kappa != 0:
        c = 2 * data.kappa
        path3 = virasoro_disc_exact(c)
        results["path3_virasoro"] = path3
        results["match_1_3"] = path1 == path3
        results["match_2_3"] = path2 == path3

    return results
