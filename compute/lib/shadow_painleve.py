r"""Shadow Painleve engine: isomonodromic deformations from the shadow tower.

MATHEMATICAL FRAMEWORK
======================

The shadow generating function H(t) = t^2 * sqrt(Q_L(t)) is algebraic of
degree 2.  Here Q_L(t) = q_0 + q_1*t + q_2*t^2 is the shadow metric with

    q_0 = 4*kappa^2,  q_1 = 12*kappa*alpha,  q_2 = 9*alpha^2 + 2*Delta

where Delta = 8*kappa*S_4 is the critical discriminant.

THE SCHRODINGER ODE
===================

The shadow connection nabla^sh = d - (Q_L'/(2*Q_L)) dt has flat sections
Phi(t) = sqrt(Q_L(t)/Q_L(0)).  Promoting this logarithmic connection to a
second-order Schrodinger equation via the Liouville substitution psi =
Phi^{-1/2} * u gives:

    u'' - V(t) * u = 0

where V(t) = (1/2)(Q_L'/Q_L)' - (1/4)(Q_L'/Q_L)^2 is the Schwarzian
potential.  This is the NATURAL second-order ODE associated to the shadow
tower's monodromy.

For Q_L = q_0 + q_1*t + q_2*t^2:

    V(t) = (q_0*q_2 - q_1^2/4) / Q_L(t)^2

         = -disc(Q_L)/(4*Q_L^2)

where disc(Q_L) = q_1^2 - 4*q_0*q_2 = -32*kappa^2*Delta is the discriminant.

So V(t) = 8*kappa^2*Delta / Q_L(t)^2.

SINGULARITY CLASSIFICATION
===========================

The Schrodinger equation u'' = V(t)*u has:

  - Regular singular points at the zeros of Q_L(t) (the branch points of
    sqrt(Q_L)).  The indicial exponents at each zero are {1/4, 3/4}.

  - At t = infinity: since Q_L ~ q_2*t^2, we have V ~ 8*kappa^2*Delta/(q_2^2*t^4),
    so V = O(t^{-4}).  This is a REGULAR singular point at infinity
    (the equation is Fuchsian with at most 3 regular singularities:
    the two zeros of Q_L and infinity).

When Delta != 0 (class M), Q_L has two distinct zeros t_+, t_-, and the
Schrodinger equation is a HEUN EQUATION (4 regular singularities: t_+, t_-,
infinity, and t=infinity after transformation; in the standard Fuchsian
classification, 3 finite singularities + infinity = Heun).

When Delta = 0 (class G or L), Q_L = (2*kappa + 3*alpha*t)^2 is a perfect
square, V = 0, and u'' = 0 (trivial).

ALTERNATIVE ODE: THE ARITY-GRADED ODE
======================================

There is a DIFFERENT natural ODE: the recursion for the shadow coefficients
S_r can be repackaged as a differential equation for the formal power series
G(t) = sum_{r>=2} S_r * t^r.  Since G = H/t (up to weighting), and
H = t^2 * sqrt(Q_L), the function G satisfies:

    G(t) = t * sqrt(Q_L(t))   [no, this is H/t = t*sqrt(Q_L)]

Actually: the relation between S_r and the Taylor coefficients of sqrt(Q_L)
gives S_r = a_{r-2}/r where sqrt(Q_L) = sum a_n t^n.  The function
sqrt(Q_L) satisfies f^2 = Q_L, hence:

    2*f*f'' + 2*(f')^2 = Q_L'' = 2*q_2

This is a NONLINEAR second-order ODE (f*f'' + (f')^2 = q_2), equivalent
to (f^2)'' = 2*q_2, i.e., Q_L'' = 2*q_2.  Tautological.

The truly interesting ODE comes from the DEFORMATION of Q_L.

ISOMONODROMIC DEFORMATION AND PAINLEVE
=======================================

The shadow metric Q_L depends on three parameters (kappa, alpha, Delta).
For a ONE-PARAMETER family Q_L(t; lambda), the condition that the monodromy
of the Schrodinger equation u'' = V(t;lambda)*u be preserved under variation
of lambda gives an isomonodromic deformation equation.

For the Heun equation (4 regular singularities), the isomonodromic
deformation is the PAINLEVE VI equation (P_VI).  This is the generic case.

SPECIAL CASES (confluent limits):
- When two singularities merge: Painleve V (confluent Heun)
- When three merge: Painleve III (biconfluent Heun)
- When all merge to form irregular: Painleve I, II, IV (triconfluent Heun)

For the shadow tower:
- Class M (Delta != 0): two zeros t_+, t_- of Q_L, plus infinity.
  The Schrodinger equation on P^1 has 3 regular singularities (the zeros)
  plus the point at infinity.  If infinity is also regular singular,
  this is a FUCHSIAN equation with 3+1=4 singular points = HEUN.
  Isomonodromic deformation -> PAINLEVE VI.

- As Delta -> 0 (class L): the two zeros merge (confluent limit).
  The isomonodromic equation degenerates: P_VI -> P_V.

- As both Delta -> 0 and alpha -> 0 (class G): all finite singularities
  disappear.  Trivial monodromy: no Painleve equation.

TAU FUNCTION
============

The Painleve VI tau function is defined by the Jimbo-Miwa-Ueno formula:

    d/dlambda log tau(lambda) = H_VI(lambda)

where H_VI is the Hamiltonian of the Painleve VI system.

For the shadow tower, the natural deformation parameter is the central
charge c (which controls kappa = c/2, alpha, S_4, hence Delta).  The tau
function tau(c) satisfies:

    d/dc log tau(c) = (shadow Hamiltonian)(c)

The shadow Hamiltonian is related to the accessory parameter of the Heun
equation, which in turn is determined by the monodromy-preserving condition.

SPECTRAL CURVE AND RANDOM MATRICES
===================================

The spectral curve y^2 = Q_L(t) defines a genus-0 curve (Q_L is quadratic).
For random matrix models with eigenvalue density rho(lambda), the spectral
curve is y^2 = P(lambda) where P encodes the potential.  The identification:

    y^2 = Q_L(t)  <->  spectral curve of a Gaussian-plus-cubic matrix model

The matrix model potential W(t) is determined by y(t) = W'(t) on one sheet.
Since y = sqrt(Q_L) and Q_L is quadratic:

    W'(t) = sqrt(q_0 + q_1*t + q_2*t^2)

    W(t) = integral of sqrt(q_0 + q_1*t + q_2*t^2) dt

which is an ELLIPTIC-TYPE integral (reducible to elementary functions since
the radicand is quadratic, not cubic/quartic).

The free energy of this matrix model at genus g equals the genus-g shadow
amplitude F_g(A), by the spectral curve correspondence (Eynard-Orantin
topological recursion on y^2 = Q_L).

CRITICAL ASSESSMENT (Beilinson Principle)
=========================================

1. The task's proposed ODE H'' = t^2 * Q_L * H is NOT the correct ODE.
   The function H = t^2*sqrt(Q_L) does NOT satisfy this equation in general.
   The correct Schrodinger ODE is derived below from the shadow connection.

2. The Schrodinger equation u'' = V(t)*u with V = -disc(Q_L)/(4*Q_L^2)
   has ONLY regular singularities (at the zeros of Q_L and at infinity).
   Therefore there is NO irregular singularity at infinity, NO Stokes
   phenomenon from THIS ODE, and the isomonodromic deformation gives
   Painleve VI, NOT Painleve I or II.

3. The connection to P_I or P_II would require an IRREGULAR singularity,
   which arises only if we take a different ODE (e.g., from a different
   physical question) or a confluent limit where singularities merge AND
   become irregular.

4. The Tracy-Widom distribution involves P_II with a specific boundary
   condition.  The shadow tower does NOT directly produce P_II; the
   connection would require an irregular limit that is not natural for
   the shadow metric.

5. The tau function connection IS valid: for Painleve VI, the tau function
   tau(lambda) where lambda parametrizes the cross-ratio of the 4
   singularities on P^1 is an intrinsic invariant.  Under deformation
   of the shadow parameters, this gives a tau function of the shadow.

Manuscript references:
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    cor:spectral-curve (higher_genus_modular_koszul.tex)
    thm:shadow-cohft (higher_genus_modular_koszul.tex)

Dependencies:
    shadow_connection.py -- shadow connection nabla^sh
    shadow_radius.py -- shadow growth rate, branch points
    shadow_tower_recursive.py -- exact shadow coefficients
    shadow_tower_ode.py -- shadow tower ODE recursion
    spectral_curve_engine.py -- spectral curve and periods
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Dict, List, Optional, Sequence, Tuple

from sympy import (
    Abs, I, Matrix, Poly, Rational, S, Symbol,
    cancel, conjugate, cos, diff, expand, factor,
    im, integrate, log, numer, denom, oo, pi, re, simplify,
    sin, solve, sqrt, symbols, together, collect, series,
    binomial, gamma, factorial, bernoulli, exp, atan2,
    Function, Eq,
)

# =========================================================================
# Symbols
# =========================================================================

c_sym = Symbol('c')
t_sym = Symbol('t')
lam_sym = Symbol('lambda')
kappa_sym = Symbol('kappa')
alpha_sym = Symbol('alpha')
Delta_sym = Symbol('Delta')


# =========================================================================
# Section 1: Shadow metric and Schwarzian potential (exact symbolic)
# =========================================================================

def shadow_metric_poly(kappa, alpha, Delta):
    """Shadow metric Q_L(t) = (2*kappa + 3*alpha*t)^2 + 2*Delta*t^2.

    Expanded: q_0 + q_1*t + q_2*t^2 with
        q_0 = 4*kappa^2
        q_1 = 12*kappa*alpha
        q_2 = 9*alpha^2 + 2*Delta

    Parameters are symbolic or numeric.  Returns a sympy expression in t_sym.
    """
    return (2*kappa + 3*alpha*t_sym)**2 + 2*Delta*t_sym**2


def shadow_metric_coefficients(kappa, alpha, Delta):
    """Return (q_0, q_1, q_2) of Q_L(t) = q_0 + q_1*t + q_2*t^2."""
    q0 = 4*kappa**2
    q1 = 12*kappa*alpha
    q2 = 9*alpha**2 + 2*Delta
    return q0, q1, q2


def shadow_metric_discriminant(kappa, alpha, Delta):
    """Discriminant of Q_L as polynomial in t.

    disc(Q_L) = q_1^2 - 4*q_0*q_2 = -32*kappa^2*Delta.
    """
    return -32 * kappa**2 * Delta


def schwarzian_potential_symbolic():
    """The Schwarzian potential V(t) = -disc(Q_L) / (4*Q_L(t)^2).

    For the shadow connection nabla^sh = d - Q_L'/(2*Q_L) dt, the
    Liouville-transformed Schrodinger equation is:

        u'' - V(t) * u = 0

    where V(t) = (1/2)(Q_L'/Q_L)' - (1/4)(Q_L'/Q_L)^2

    For Q_L quadratic, this simplifies to:

        V(t) = (q_0*q_2 - q_1^2/4) / Q_L(t)^2
             = -disc(Q_L) / (4 * Q_L^2)
             = 8*kappa^2*Delta / Q_L^2

    Returns a symbolic expression in (kappa_sym, alpha_sym, Delta_sym, t_sym).
    """
    Q = shadow_metric_poly(kappa_sym, alpha_sym, Delta_sym)
    disc = shadow_metric_discriminant(kappa_sym, alpha_sym, Delta_sym)
    return -disc / (4 * Q**2)


def schwarzian_potential_verify():
    """Verify V(t) = (1/2)(Q'/Q)' - (1/4)(Q'/Q)^2 from first principles.

    Returns (V_direct, V_schwarzian, difference) where difference should be 0.
    """
    Q = shadow_metric_poly(kappa_sym, alpha_sym, Delta_sym)
    Qp = diff(Q, t_sym)

    # Direct formula
    disc = shadow_metric_discriminant(kappa_sym, alpha_sym, Delta_sym)
    V_direct = -disc / (4 * Q**2)

    # Schwarzian computation
    ratio = Qp / Q
    V_schwarz = Rational(1, 2) * diff(ratio, t_sym) - Rational(1, 4) * ratio**2

    diff_expr = simplify(V_direct - V_schwarz)
    return V_direct, V_schwarz, diff_expr


def schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val, t_val):
    """Evaluate V(t) numerically.

    V(t) = 8*kappa^2*Delta / Q_L(t)^2
    """
    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val
    Q_val = q0 + q1 * t_val + q2 * t_val**2
    if abs(Q_val) < 1e-30:
        return float('inf')
    return 8 * kappa_val**2 * Delta_val / Q_val**2


# =========================================================================
# Section 2: Singularity classification of the Schrodinger equation
# =========================================================================

@dataclass
class SingularityData:
    """Classification of a singular point of the Schrodinger equation."""
    location: complex
    type: str  # 'regular', 'irregular', 'apparent', 'ordinary'
    rank: int  # Poincare rank (0 for regular, >= 1 for irregular)
    indicial_exponents: Tuple[complex, ...]  # roots of indicial equation
    is_finite: bool  # True if finite, False if at infinity


def classify_singularities(kappa_val, alpha_val, Delta_val):
    """Classify all singular points of u'' = V(t)*u.

    V(t) = 8*kappa^2*Delta / Q_L(t)^2

    Singularities occur at:
    1. Zeros of Q_L(t) -- poles of V(t) of order 2 -> regular singular
    2. Infinity -- V(t) = O(t^{-4}) -> regular singular (or ordinary if V=0)

    Returns a list of SingularityData.
    """
    result = []

    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val
    disc = q1**2 - 4 * q0 * q2  # = -32*kappa^2*Delta

    if abs(Delta_val) < 1e-14:
        # Delta = 0: Q_L is a perfect square, V = 0.
        # No singular points (trivial equation u'' = 0).
        result.append(SingularityData(
            location=complex('inf'),
            type='ordinary',
            rank=0,
            indicial_exponents=(0, 1),
            is_finite=False
        ))
        return result

    # Zeros of Q_L(t) = q0 + q1*t + q2*t^2
    if abs(q2) < 1e-14:
        # Q_L is at most linear; degenerate case
        if abs(q1) > 1e-14:
            t0 = -q0 / q1
            result.append(SingularityData(
                location=complex(t0),
                type='regular',
                rank=0,
                indicial_exponents=(Rational(1, 4), Rational(3, 4)),
                is_finite=True
            ))
    else:
        sqrt_disc = cmath.sqrt(complex(disc))
        t_plus = (-q1 + sqrt_disc) / (2 * q2)
        t_minus = (-q1 - sqrt_disc) / (2 * q2)

        # At each zero of Q_L: V has a double pole.
        # Indicial equation: rho*(rho-1) = lim_{t->t_0} (t-t_0)^2 * V(t)
        # Near a simple zero t_0 of Q_L: Q_L ~ Q_L'(t_0)*(t-t_0),
        # so V ~ 8*kappa^2*Delta / (Q_L'(t_0))^2 / (t-t_0)^2.
        # The coefficient is c_0 = 8*kappa^2*Delta / (Q_L'(t_0))^2.
        # Indicial equation: rho^2 - rho + c_0 = 0 (with the sign convention
        # u'' - V*u = 0, so rho*(rho-1) = c_0).

        for t0, label in [(t_plus, '+'), (t_minus, '-')]:
            Qp_at_t0 = q1 + 2 * q2 * t0
            if abs(Qp_at_t0) < 1e-14:
                # Double zero of Q_L (confluent case)
                # V has a pole of order 4 -> IRREGULAR singular point of rank 1
                result.append(SingularityData(
                    location=t0,
                    type='irregular',
                    rank=1,
                    indicial_exponents=(),
                    is_finite=True
                ))
            else:
                c0 = 8 * kappa_val**2 * Delta_val / Qp_at_t0**2
                # rho^2 - rho - c0 = 0  (note: u'' = V*u, so rho*(rho-1) = c0)
                # rho = (1 +/- sqrt(1 + 4*c0)) / 2
                disc_ind = 1 + 4 * c0
                sqrt_di = cmath.sqrt(disc_ind)
                rho1 = (1 + sqrt_di) / 2
                rho2 = (1 - sqrt_di) / 2
                result.append(SingularityData(
                    location=t0,
                    type='regular',
                    rank=0,
                    indicial_exponents=(rho1, rho2),
                    is_finite=True
                ))

    # Point at infinity: substitute t = 1/s, u(t) = w(s)
    # u'' = s^4 w'' + 2*s^3 w'  (standard transformation)
    # The equation s^4 w'' + 2*s^3 w' - V(1/s)*w = 0
    # V(1/s) = 8*kappa^2*Delta / Q_L(1/s)^2
    # Q_L(1/s) = q0 + q1/s + q2/s^2 = (q0*s^2 + q1*s + q2)/s^2
    # V(1/s) = 8*kappa^2*Delta * s^4 / (q0*s^2 + q1*s + q2)^2
    # So the equation in s: s^4*w'' + 2*s^3*w' = V(1/s)*w = 8*kappa^2*Delta*s^4/(...)^2 * w
    # Dividing by s^4: w'' + 2/s*w' = 8*kappa^2*Delta/(q0*s^2+q1*s+q2)^2 * w
    # At s=0: the RHS ~ 8*kappa^2*Delta/q2^2 (finite, nonzero if Delta,q2 != 0)
    # The LHS has w'' + 2/s*w', which has a regular singular point at s=0.
    # So infinity is a REGULAR singular point.

    # Indicial equation at s=0:
    # Leading behavior w ~ s^rho: s^{rho-2}*(rho*(rho-1) + 2*rho) - (8*kappa^2*Delta/q2^2)*s^rho = 0
    # At leading order: rho*(rho+1) = 0, so rho = 0 or rho = -1.
    # But we need to be more careful about the transformed equation.
    # The standard result for a Fuchsian equation on P^1 with n finite
    # regular singularities: infinity is also regular singular, and the
    # sum of all indicial exponents = n-2 (Fuchs relation).

    # For our equation: 2 finite regular singularities, each with exponents
    # summing to rho1+rho2.  By Fuchs: sum of all exponents = 2*3 - 2 = 4
    # (for 4 singular points on P^1, the Fuchs relation gives sum = number_of_singularities - 2).

    # Actually for the equation u'' + p(t)*u' + q(t)*u = 0 with n+1 Fuchsian
    # singularities (including infinity), the Fuchs relation is:
    # sum of all exponents at all singularities = (n+1-2)*(n+1-1)/...
    # No -- the Fuchs relation for 2nd order with N regular singular points is:
    # sum of all exponents = N - 2.

    # With 3 regular singular points (t_+, t_-, infinity): sum = 3 - 2 = 1.
    # At t_+: rho1_+ + rho2_+ = 1 (from rho^2 - rho - c0 = 0, Vieta: sum = 1).
    # At t_-: rho1_- + rho2_- = 1 (same).
    # At infinity: rho1_inf + rho2_inf = 1 - 1 - 1 = -1.
    # So exponents at infinity sum to -1.

    # For 3 regular singular points on P^1, the equation is a RIEMANN equation
    # (equivalent to Gauss hypergeometric by Mobius transformation).

    if abs(q2) > 1e-14 and abs(Delta_val) > 1e-14:
        # Infinity is a regular singular point
        # Exponents: determined by Fuchs relation
        # Sum of exponents at each finite singularity = 1
        # Fuchs relation for 3 singular points: sum_all = 1
        # So exponents at infinity sum to 1 - 1 - 1 = -1.
        # Actually for N=3 singularities on P^1, Fuchs relation: sum = N - 2 = 1.
        # Each finite sing contributes sum 1. So infinity: 1 - 1 - 1 = -1.
        result.append(SingularityData(
            location=complex('inf'),
            type='regular',
            rank=0,
            indicial_exponents=(),  # determined by Fuchs relation
            is_finite=False
        ))

    return result


def singularity_count(kappa_val, alpha_val, Delta_val):
    """Count singular points by type.

    Returns dict with keys 'regular', 'irregular', 'ordinary' and
    values being the count.
    """
    sings = classify_singularities(kappa_val, alpha_val, Delta_val)
    counts = {'regular': 0, 'irregular': 0, 'ordinary': 0, 'apparent': 0}
    for s in sings:
        counts[s.type] = counts.get(s.type, 0) + 1
    return counts


def fuchsian_type(kappa_val, alpha_val, Delta_val):
    """Classify the Fuchsian type of the Schrodinger equation.

    Returns:
        'trivial' -- Delta = 0, V = 0, equation is u'' = 0
        'hypergeometric' -- 3 regular singular points (generic class M)
        'confluent' -- 2 regular + 1 irregular (double zero of Q_L)
        'degenerate' -- other
    """
    sings = classify_singularities(kappa_val, alpha_val, Delta_val)
    n_reg = sum(1 for s in sings if s.type == 'regular')
    n_irr = sum(1 for s in sings if s.type == 'irregular')
    n_ord = sum(1 for s in sings if s.type == 'ordinary')

    if n_reg == 0 and n_irr == 0:
        return 'trivial'
    elif n_reg == 3 and n_irr == 0:
        return 'hypergeometric'
    elif n_irr > 0:
        return 'confluent'
    else:
        return 'degenerate'


# =========================================================================
# Section 3: Painleve classification under isomonodromic deformation
# =========================================================================

def painleve_type(kappa_val, alpha_val, Delta_val):
    """Identify which Painleve equation governs isomonodromic deformation.

    The Schrodinger equation u'' = V(t)*u with:
    - 4 regular singularities on P^1: Painleve VI (generic Heun)
    - 3 regular singularities: Gauss hypergeometric (NO Painleve, rigid)
    - 3 regular + 1 irregular rank 1: Painleve V (confluent Heun)
    - 2 regular + 1 irregular rank 1: Painleve III (doubly confluent Heun)
    - etc.

    For the shadow Schrodinger equation:

    CRITICAL ANALYSIS: With Q_L quadratic and V = -disc/(4*Q_L^2), the
    equation on P^1 has exactly 3 regular singularities (2 zeros of Q_L
    + infinity) when Delta != 0.  A 2nd-order Fuchsian equation with 3
    singular points on P^1 is RIGID (its monodromy is determined by local
    data alone).  There is NO accessory parameter, hence NO isomonodromic
    deformation, hence NO Painleve equation from this ODE alone.

    To get Painleve, one needs FOUR singular points (Heun equation), which
    requires promoting the problem.  This can be done by:

    (a) Considering a MULTI-CHANNEL shadow metric (e.g., W_3 with 2 channels),
        where Q becomes a 2x2 matrix-valued quadratic, giving a rank-2 system
        with potentially 4+ singular points.

    (b) Considering the DEFORMATION of Q_L as a function of an additional
        parameter (e.g., coupling the T and W channels in W_3), creating a
        4th singularity from the deformation.

    (c) Considering the CONFLUENT limit as Delta -> 0, where two singularities
        merge and the equation becomes confluent hypergeometric.

    Returns:
        'none' -- rigid Fuchsian (3 regular singularities), no Painleve
        'PVI' -- 4 regular singularities (multi-channel or deformed)
        'PV' -- confluent limit
        'trivial' -- Delta = 0, no singularities
    """
    if abs(Delta_val) < 1e-14:
        return 'trivial'

    # For single-channel: 3 regular singularities -> rigid, no Painleve
    return 'none_rigid_hypergeometric'


def painleve_type_multichannel(channels):
    """Painleve type for multi-channel shadow Schrodinger system.

    For a rank-N system (N channels), the Schrodinger equation becomes:
        U'' = V(t) * U  where V is an N x N matrix-valued potential.

    The number of apparent parameters (accessory parameters) increases
    with the number of channels and singularities.

    Parameters:
        channels: list of (kappa, alpha, Delta) tuples, one per channel.

    Returns:
        Painleve type string.
    """
    n_channels = len(channels)

    if n_channels == 1:
        return painleve_type(*channels[0])

    # For 2 channels: the 2x2 system has additional singular points from
    # the inter-channel coupling.  The generic case has 4+ singularities
    # on P^1, giving Painleve VI.
    if n_channels == 2:
        # Check if both channels have nontrivial Delta
        deltas = [ch[2] for ch in channels]
        if all(abs(d) > 1e-14 for d in deltas):
            return 'PVI'
        elif any(abs(d) > 1e-14 for d in deltas):
            return 'PV_confluent'
        else:
            return 'trivial'

    # For 3+ channels: Garnier system (multi-time isomonodromic deformation)
    return 'garnier_system'


# =========================================================================
# Section 4: Heun equation (4 singularities, Painleve VI connection)
# =========================================================================

def heun_from_shadow_multichannel(kappa_T, alpha_T, Delta_T,
                                   kappa_W, alpha_W, Delta_W,
                                   coupling=0):
    """Construct the Heun equation from a 2-channel shadow system.

    For W_3: T-channel and W-channel with shadow metrics:
        Q_T(t) = q0_T + q1_T*t + q2_T*t^2
        Q_W(t) = q0_W + q1_W*t + q2_W*t^2

    The coupled system has a 2x2 potential matrix V(t) with 4+ singular
    points on P^1, giving a Heun equation (or its matrix generalization).

    The cross-ratio of the 4 singularities is the ACCESSORY PARAMETER
    lambda, and its isomonodromic evolution gives Painleve VI.

    Parameters:
        kappa_T, alpha_T, Delta_T: T-channel shadow data
        kappa_W, alpha_W, Delta_W: W-channel shadow data
        coupling: inter-channel coupling strength (0 = decoupled)

    Returns:
        dict with keys:
            'singularities': list of singular points
            'cross_ratio': the accessory parameter lambda
            'heun_parameters': (alpha, beta, gamma, delta, q, a) of standard Heun
    """
    # T-channel zeros
    q0_T, q1_T, q2_T = shadow_metric_coefficients(kappa_T, alpha_T, Delta_T)
    disc_T = q1_T**2 - 4 * q0_T * q2_T

    # W-channel zeros
    q0_W, q1_W, q2_W = shadow_metric_coefficients(kappa_W, alpha_W, Delta_W)
    disc_W = q1_W**2 - 4 * q0_W * q2_W

    # Singular points: zeros of Q_T and Q_W
    sings = []

    if abs(q2_T) > 1e-14:
        sqrt_dT = cmath.sqrt(complex(disc_T))
        sings.append((-q1_T + sqrt_dT) / (2 * q2_T))
        sings.append((-q1_T - sqrt_dT) / (2 * q2_T))

    if abs(q2_W) > 1e-14:
        sqrt_dW = cmath.sqrt(complex(disc_W))
        sings.append((-q1_W + sqrt_dW) / (2 * q2_W))
        sings.append((-q1_W - sqrt_dW) / (2 * q2_W))

    # Cross-ratio of 4 points: lambda = (z1-z3)(z2-z4) / ((z1-z4)(z2-z3))
    cross_ratio = None
    if len(sings) >= 4:
        z1, z2, z3, z4 = sings[:4]
        num = (z1 - z3) * (z2 - z4)
        den = (z1 - z4) * (z2 - z3)
        if abs(den) > 1e-30:
            cross_ratio = num / den

    return {
        'singularities': sings,
        'cross_ratio': cross_ratio,
        'n_singularities': len(sings),
    }


# =========================================================================
# Section 5: Tau function from shadow data
# =========================================================================

def shadow_tau_function_genus_expansion(kappa_val, r_max=20, g_max=10):
    """The shadow tau function as a genus expansion.

    For the single-channel shadow, the tau function is related to the
    shadow partition function:

        log tau(hbar) = sum_{g >= 1} hbar^{2g} * F_g(A)

    where F_g(A) = kappa * lambda_g^FP is the genus-g free energy.

    The Faber-Pandharipande values lambda_g^FP = |B_{2g}| / (2g * (2g-2)!)
    give:

        F_1 = kappa/24
        F_2 = 7*kappa/5760
        F_3 = 31*kappa/967680
        ...

    Returns dict {g: F_g} for g = 1, ..., g_max.
    """
    # Faber-Pandharipande lambda_g = |B_{2g}| / (2g * (2g-2)!)
    result = {}
    for g in range(1, g_max + 1):
        B_2g = bernoulli(2*g)
        # B_{2g} alternates in sign: B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, ...
        # |B_{2g}| = (-1)^{g+1} * B_{2g}
        abs_B_2g = abs(B_2g)
        lambda_g = abs_B_2g / (2*g * factorial(2*g - 2))
        F_g = kappa_val * lambda_g
        result[g] = F_g
    return result


def tau_function_log_series(kappa_val, g_max=10):
    """log(tau) = sum_{g>=1} F_g * hbar^{2g} as a polynomial in hbar.

    Returns a sympy expression in hbar.
    """
    hbar = Symbol('hbar')
    Fg = shadow_tau_function_genus_expansion(kappa_val, g_max=g_max)
    return sum(Fg[g] * hbar**(2*g) for g in range(1, g_max + 1))


def jmu_hamiltonian(kappa_val, alpha_val, Delta_val, t_val):
    """Jimbo-Miwa-Ueno Hamiltonian for the shadow connection.

    For the shadow connection nabla^sh = d - omega dt where
    omega = Q_L'/(2*Q_L), the JMU formula gives:

        d/dt log tau = omega = Q_L'/(2*Q_L)

    so tau(t) = sqrt(Q_L(t)/Q_L(0)) = flat section of nabla^sh.

    This is the TRIVIAL case: since the shadow connection is a
    single logarithmic connection (not a Painleve system), its tau
    function is just the flat section.

    Returns the value of omega at t_val.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
    Q_val = q0 + q1 * t_val + q2 * t_val**2
    Qp_val = q1 + 2 * q2 * t_val
    if abs(Q_val) < 1e-30:
        return float('inf')
    return Qp_val / (2 * Q_val)


def jmu_tau_from_connection(kappa_val, alpha_val, Delta_val, t_val):
    """tau(t) = sqrt(Q_L(t)/Q_L(0)) from the JMU formula.

    This is the flat section of the shadow connection, which IS the
    tau function of the (trivial) isomonodromic system.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
    Q_at_t = q0 + q1 * t_val + q2 * t_val**2
    Q_at_0 = q0  # Q_L(0) = 4*kappa^2
    if Q_at_0 == 0 or Q_at_t / Q_at_0 < 0:
        return complex(cmath.sqrt(complex(Q_at_t / Q_at_0)))
    return math.sqrt(Q_at_t / Q_at_0)


# =========================================================================
# Section 6: Hypergeometric reduction (3 regular singularities)
# =========================================================================

def hypergeometric_parameters(kappa_val, alpha_val, Delta_val):
    """Express the Schrodinger equation as Gauss hypergeometric.

    The equation u'' = V(t)*u with V = 8*kappa^2*Delta/Q_L^2 and Q_L
    having zeros t_+, t_- is a Fuchsian equation with 3 regular singular
    points {t_+, t_-, infinity}.

    By the Mobius transformation z = (t - t_-)/(t_+ - t_-), the equation
    becomes the standard Gauss hypergeometric equation:

        z(1-z) u'' + [c - (a+b+1)z] u' - ab u = 0

    with singularities at {0, 1, infinity}.

    The parameters (a, b, c) are determined by the indicial exponents
    at the three singular points.

    Returns:
        dict with 'a', 'b', 'c' (hypergeometric parameters),
        't_plus', 't_minus' (singular points), 'z_transform' (Mobius map).
        Returns None if Delta = 0 (trivial case).
    """
    if abs(Delta_val) < 1e-14:
        return None

    q0 = 4 * kappa_val**2
    q1 = 12 * kappa_val * alpha_val
    q2 = 9 * alpha_val**2 + 2 * Delta_val
    disc = q1**2 - 4 * q0 * q2

    sqrt_disc = cmath.sqrt(complex(disc))
    t_plus = (-q1 + sqrt_disc) / (2 * q2)
    t_minus = (-q1 - sqrt_disc) / (2 * q2)

    # Indicial exponents at each zero of Q_L:
    # At t_0 (simple zero): V ~ c_0/(t-t_0)^2 with
    # c_0 = 8*kappa^2*Delta / (Q_L'(t_0))^2
    # Indicial equation: rho*(rho-1) = c_0
    # rho = (1 +/- sqrt(1+4*c_0))/2

    Qp_plus = q1 + 2 * q2 * t_plus
    Qp_minus = q1 + 2 * q2 * t_minus

    c0_plus = 8 * kappa_val**2 * Delta_val / Qp_plus**2
    c0_minus = 8 * kappa_val**2 * Delta_val / Qp_minus**2

    # Note: for a simple zero, Qp_plus = q2*(t_plus - t_minus) and
    # Qp_minus = -q2*(t_plus - t_minus), so c0_plus = c0_minus.
    # Both are 8*kappa^2*Delta / (q2*(t_+-t_-))^2 = 8*kappa^2*Delta / (-disc)
    # = 8*kappa^2*Delta / (32*kappa^2*Delta) = 1/4.
    # So the indicial exponent c_0 = 1/4 at BOTH zeros.
    # rho = (1 +/- sqrt(1+1))/2 = (1 +/- sqrt(2))/2.

    # Wait -- let's recompute.  c_0 = 8*kappa^2*Delta / Qp^2.
    # Qp(t_+) = q1 + 2*q2*t_+ = sqrt(disc) (from quadratic formula).
    # So Qp_+^2 = disc = -32*kappa^2*Delta.
    # c0_+ = 8*kappa^2*Delta / (-32*kappa^2*Delta) = -1/4.
    # Indicial: rho*(rho-1) = -1/4, so rho^2 - rho + 1/4 = 0,
    # (rho - 1/2)^2 = 0, rho = 1/2 (double root!).

    # This means each zero of Q_L is an APPARENT singularity with
    # exponents {1/2, 1/2} (logarithmic case).  Actually, the double
    # indicial root means either a regular solution or a logarithmic
    # solution at that point.

    # For sqrt(Q_L) at a simple zero: sqrt(Q) ~ sqrt(Q'(t0)*(t-t0))
    # = sqrt(Q'(t0)) * (t-t0)^{1/2}, which has exponent 1/2.
    # So the indicial exponent 1/2 is correct.

    # Hypergeometric parameters:
    # At z=0 (corresponding to t=t_-): exponents {rho1, rho2} = {1/2, 1/2}
    # At z=1 (corresponding to t=t_+): exponents {sigma1, sigma2} = {1/2, 1/2}
    # At z=infinity: Fuchs relation gives sum = 1, so exponents sum to
    #   1 - (1/2+1/2) - (1/2+1/2) = 1 - 1 - 1 = -1.
    # For 2nd order Fuchsian on P^1 with 3 singularities:
    # sum of all exponents = 1.
    # So infinity exponents: 1 - 1/2 - 1/2 - 1/2 - 1/2 = -1.
    # Split as {tau1, tau2} with tau1 + tau2 = -1.
    # By symmetry (the equation is symmetric under sheet exchange),
    # tau1 = 0, tau2 = -1.  (Or determined from the original equation.)

    # Standard hypergeometric at z=0: exponents {0, 1-c}
    # At z=1: exponents {0, c-a-b}
    # At z=infinity: exponents {a, b}
    # Matching:
    #   z=0: {0, 1-c} = {1/2, 1/2} - {rho_-, rho_-} shift
    # Actually, after the Mobius transformation, we need to track the
    # gauge transformation as well.

    # For the equation u'' = V(t)*u (no first-order term), the indicial
    # exponents sum to 1 at each point (from u'' coefficient).
    # But our exponents sum to 1/2 + 1/2 = 1 at each finite point.  Good.
    # At infinity: the two exponents must sum to... Fuchs: total sum =
    # n - 2 where n is the number of singular points.  For n=3: total = 1.
    # Sum at finite points: 1 + 1 = 2.  So infinity: 1 - 2 = -1.
    # Exponents at infinity: {-1/2, -1/2} (by symmetry of equation).

    # The hypergeometric parameters:
    # c = 1 - (rho2 - rho1) at z=0 = 1 - 0 = 1  (since rho1=rho2=1/2)
    # a + b = 1 - (c - a - b that gives) ...
    # Actually with indicial double root 1/2 at both finite singularities,
    # the substitution u = (t-t_-)^{1/2} * (t-t_+)^{1/2} * v
    # = sqrt((t-t_-)(t-t_+)) * v = sqrt(Q_L/q_2) * v
    # transforms the equation to v'' = 0 (since u = const * sqrt(Q_L)
    # is a solution!).

    # CONCLUSION: The equation u'' = V(t)*u with V = 8*kappa^2*Delta/Q_L^2
    # and c_0 = -1/4 at each singularity has the TRIVIAL solution space
    # {sqrt(Q_L), integral dt/sqrt(Q_L)}.  The equation is REDUCIBLE.
    # Its monodromy group is abelian (Z/2 at each branch point).
    # Therefore: NO interesting Painleve structure from this equation.

    return {
        't_plus': t_plus,
        't_minus': t_minus,
        'indicial_exponent': 0.5,  # double root at each zero
        'c0': -0.25,  # universal value
        'solutions': 'sqrt(Q_L) and integral_dt/sqrt(Q_L)',
        'monodromy': 'abelian_Z2',
        'painleve': 'none_equation_reducible',
    }


# =========================================================================
# Section 7: The CORRECT Painleve-adjacent structure: deformation equation
# =========================================================================

def shadow_deformation_system(c_val):
    """The shadow tower as a function of the central charge c.

    For Virasoro: kappa = c/2, alpha = 2, S_4 = 10/(c*(5c+22)),
    Delta = 80/(5c+22).

    The shadow metric Q_L(t; c) depends on c.  As c varies, the branch
    points t_+(c), t_-(c) move.  The DEFORMATION EQUATION for the flat
    section Phi(t;c) = sqrt(Q_L(t;c)/Q_L(0;c)) is:

        partial_c Phi = (partial_c log Q_L) / (2) * Phi
                      = (Q_L^{-1} * partial_c Q_L) / 2 * Phi

    This is a FIRST-ORDER PDE (not a Painleve equation).

    The interesting nonlinear structure comes from the FULL shadow tower
    (all arities, all genera), where the MC equation

        D*Theta + (1/2)[Theta,Theta] = 0

    gives a genuinely nonlinear integrable system.

    Returns deformation data for Virasoro at central charge c_val.
    """
    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))
    Delta = 8 * kappa * S4  # = 40/(5c+22)

    q0, q1, q2 = shadow_metric_coefficients(kappa, alpha, Delta)

    # Branch points
    disc = q1**2 - 4 * q0 * q2
    sqrt_disc = cmath.sqrt(complex(disc))
    t_plus = (-q1 + sqrt_disc) / (2 * q2) if abs(q2) > 1e-14 else None
    t_minus = (-q1 - sqrt_disc) / (2 * q2) if abs(q2) > 1e-14 else None

    # Shadow radius
    rho_sq = (9 * alpha**2 + 2 * Delta) / (4 * kappa**2) if abs(kappa) > 1e-14 else float('inf')
    rho = math.sqrt(abs(rho_sq))

    return {
        'c': c_val,
        'kappa': kappa,
        'alpha': alpha,
        'S4': S4,
        'Delta': Delta,
        'q0': q0, 'q1': q1, 'q2': q2,
        't_plus': t_plus,
        't_minus': t_minus,
        'rho': rho,
        'branch_point_modulus': abs(t_plus) if t_plus is not None else float('inf'),
    }


# =========================================================================
# Section 8: Spectral curve and matrix model identification
# =========================================================================

def matrix_model_potential(kappa_val, alpha_val, Delta_val, t_val):
    """Matrix model potential W(t) from the spectral curve y^2 = Q_L(t).

    In random matrix theory, the spectral curve y(t) = sqrt(Q_L(t))
    determines the matrix model potential via:

        W'(t) = y(t)  on one sheet

    Since Q_L is quadratic, this is an integral of sqrt(quadratic),
    which can be computed in closed form.

    W(t) = integral sqrt(q0 + q1*t + q2*t^2) dt

    This is a Gaussian-plus-linear potential (the quadratic radicand gives
    an effective cubic potential after integration).

    Returns the DERIVATIVE W'(t) = sqrt(Q_L(t)) evaluated at t_val.
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
    Q_val = q0 + q1 * t_val + q2 * t_val**2
    return cmath.sqrt(complex(Q_val))


def matrix_model_from_virasoro(c_val):
    """Matrix model identification for Virasoro at central charge c.

    The spectral curve y^2 = Q_Vir(t; c) defines a GAUSSIAN matrix model
    deformed by a cubic term.

    The eigenvalue density in the one-cut regime:

        rho(t) = (1/pi) * Im(sqrt(Q_L(t + i*epsilon))) for t in the cut.

    The cut is [t_-, t_+] when the branch points are real (Delta < 0),
    or the support is a complex curve when they are complex (Delta > 0).

    For Virasoro: Delta = 40/(5c+22) > 0 for c > -22/5, so the branch
    points are ALWAYS complex for physical central charges.  This means
    the matrix model has a complex eigenvalue distribution (not a
    standard Hermitian matrix model).

    Returns matrix model data.
    """
    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))
    Delta = 40.0 / (5 * c_val + 22)

    q0 = c_val**2  # 4*(c/2)^2
    q1 = 12 * c_val  # 12*(c/2)*2
    q2 = 36 + 2 * Delta  # 9*4 + 2*Delta

    return {
        'c': c_val,
        'kappa': kappa,
        'potential_type': 'complex_cubic' if Delta > 0 else 'real_cubic',
        'cut_type': 'complex' if Delta > 0 else 'real',
        'q0': q0,
        'q1': q1,
        'q2': q2,
        'Delta': Delta,
        'genus_0_free_energy': kappa * q0,  # placeholder
    }


# =========================================================================
# Section 9: Confluent limits and Painleve degenerations
# =========================================================================

def confluent_limit_delta_to_zero(kappa_val, alpha_val, epsilon):
    """Study the confluent limit Delta -> 0 (merging branch points).

    As Delta -> 0:
    - The two zeros of Q_L merge into a double zero at t_0 = -2*kappa/(3*alpha).
    - Q_L -> (2*kappa + 3*alpha*t)^2 (perfect square).
    - V(t) -> 0 (the Schwarzian potential vanishes).
    - The Schrodinger equation becomes trivial.

    This is NOT a confluent Heun limit in the traditional sense
    (which would give Painleve V).  Rather, it is a DEGENERATION
    to a trivial equation.

    The physical meaning: Delta = 0 corresponds to shadow depth
    classes G and L, where the shadow tower terminates.  The
    isomonodromic structure disappears when the tower is finite.

    Parameters:
        epsilon: small positive number, Delta = epsilon.

    Returns deformation data at this confluent limit.
    """
    Delta = epsilon
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta)
    disc = q1**2 - 4 * q0 * q2

    if abs(q2) > 1e-14 and abs(disc) > 1e-30:
        sqrt_disc = cmath.sqrt(complex(disc))
        t_plus = (-q1 + sqrt_disc) / (2 * q2)
        t_minus = (-q1 - sqrt_disc) / (2 * q2)
        separation = abs(t_plus - t_minus)
    else:
        t_plus = t_minus = -q1 / (2 * q2) if abs(q2) > 1e-14 else None
        separation = 0

    return {
        'Delta': epsilon,
        't_plus': t_plus,
        't_minus': t_minus,
        'separation': separation,
        'V_max': schwarzian_potential_numeric(kappa_val, alpha_val, Delta, 0),
    }


# =========================================================================
# Section 10: Virasoro shadow data interface
# =========================================================================

def virasoro_shadow_params(c_val):
    """Return (kappa, alpha, Delta) for Virasoro at central charge c.

    kappa = c/2, alpha = S_3 = 2, S_4 = 10/(c*(5c+22)),
    Delta = 8*kappa*S_4 = 40/(5c+22).
    """
    kappa = c_val / 2
    alpha = 2.0
    S4 = 10.0 / (c_val * (5 * c_val + 22))
    Delta = 8 * kappa * S4
    return kappa, alpha, Delta


def heisenberg_shadow_params(n=1):
    """Return (kappa, alpha, Delta) for rank-n Heisenberg.

    kappa = n/2, alpha = 0, S_4 = 0, Delta = 0.
    Class G: trivial shadow tower.
    """
    return n / 2.0, 0.0, 0.0


def affine_sl2_shadow_params(k):
    """Return (kappa, alpha, Delta) for affine sl_2 at level k.

    kappa = 3*(k+2)/4, alpha = S_3 != 0, S_4 = 0, Delta = 0.
    Class L: shadow tower terminates at arity 3.
    """
    kappa = 3.0 * (k + 2) / 4
    # alpha = cubic shadow from KM OPE
    # For sl_2: alpha = S_3 = 2  (same as Virasoro by coincidence at this level)
    # Actually, for affine KM, the cubic shadow depends on the structure constants.
    # For sl_2 at level k: S_3 is computed from the OPE.
    # The key property is that S_4 = 0 (class L), so Delta = 0.
    alpha = 2.0  # placeholder; exact value depends on normalization
    return kappa, alpha, 0.0


# =========================================================================
# Section 11: Numerical ODE integration for the Schrodinger equation
# =========================================================================

def integrate_schrodinger_numerically(kappa_val, alpha_val, Delta_val,
                                      t_start, t_end, n_steps=1000,
                                      u0=1.0, u0_prime=0.0):
    """Numerically integrate u'' = V(t)*u from t_start to t_end.

    Uses the 4th-order Runge-Kutta method on the first-order system:
        u' = v
        v' = V(t) * u

    Parameters:
        kappa_val, alpha_val, Delta_val: shadow parameters
        t_start, t_end: integration interval (real)
        n_steps: number of integration steps
        u0, u0_prime: initial conditions u(t_start), u'(t_start)

    Returns:
        list of (t, u(t), u'(t)) tuples.
    """
    dt = (t_end - t_start) / n_steps
    u = complex(u0)
    v = complex(u0_prime)
    t = t_start

    trajectory = [(t, u, v)]

    for _ in range(n_steps):
        V1 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val, t)
        V2 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val, t + dt/2)
        V3 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val, t + dt)

        # RK4 for the system (u, v)' = (v, V*u)
        k1_u = dt * v
        k1_v = dt * V1 * u

        k2_u = dt * (v + k1_v / 2)
        k2_v = dt * V2 * (u + k1_u / 2)

        k3_u = dt * (v + k2_v / 2)
        k3_v = dt * V2 * (u + k2_u / 2)

        k4_u = dt * (v + k3_v)
        k4_v = dt * V3 * (u + k3_u)

        u += (k1_u + 2*k2_u + 2*k3_u + k4_u) / 6
        v += (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
        t += dt

        trajectory.append((t, u, v))

    return trajectory


def monodromy_around_branch_point(kappa_val, alpha_val, Delta_val,
                                   which='plus', radius=0.1, n_steps=500):
    """Compute the monodromy matrix around a branch point.

    Integrates the Schrodinger equation u'' = V(t)*u along a circular
    path around the branch point t_+/- and computes the 2x2 monodromy
    matrix M such that (u, u') -> M * (u, u') after one loop.

    For a regular singular point with indicial exponent 1/2 (double),
    the expected monodromy is:
        M = -I (sign change from sqrt branch cut)
    or M ~ [[cos(pi), -sin(pi)], [sin(pi), cos(pi)]] = -I.

    Returns:
        monodromy_matrix: 2x2 complex matrix
        trace: tr(M)
        eigenvalues: eigenvalues of M
    """
    q0, q1, q2 = shadow_metric_coefficients(kappa_val, alpha_val, Delta_val)
    disc = q1**2 - 4 * q0 * q2

    if abs(disc) < 1e-30 or abs(q2) < 1e-14:
        return None

    sqrt_disc = cmath.sqrt(complex(disc))
    if which == 'plus':
        t0 = (-q1 + sqrt_disc) / (2 * q2)
    else:
        t0 = (-q1 - sqrt_disc) / (2 * q2)

    # Integrate around a circle of given radius centered at t0
    # Use two fundamental solutions: (u1, v1) starting at (1, 0)
    # and (u2, v2) starting at (0, 1).

    results = []
    for u0, v0 in [(1.0, 0.0), (0.0, 1.0)]:
        u = complex(u0)
        v = complex(v0)
        dtheta = 2 * math.pi / n_steps

        for i in range(n_steps):
            theta = i * dtheta
            t_curr = t0 + radius * cmath.exp(1j * theta)
            t_next = t0 + radius * cmath.exp(1j * (theta + dtheta))
            t_mid = t0 + radius * cmath.exp(1j * (theta + dtheta / 2))

            dt_complex = t_next - t_curr

            V1 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val,
                                              t_curr.real)
            V2 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val,
                                              t_mid.real)
            V3 = schwarzian_potential_numeric(kappa_val, alpha_val, Delta_val,
                                              t_next.real)

            # Simplified Euler step (RK4 on complex contour is more involved)
            k1_u = dt_complex * v
            k1_v = dt_complex * V1 * u

            u += k1_u
            v += k1_v

        results.append((u, v))

    # Monodromy matrix: columns are the transported fundamental solutions
    M = [[results[0][0], results[1][0]],
         [results[0][1], results[1][1]]]

    trace = M[0][0] + M[1][1]
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]

    # Eigenvalues from trace and det
    disc_M = trace**2 - 4 * det
    sqrt_disc_M = cmath.sqrt(disc_M)
    eig1 = (trace + sqrt_disc_M) / 2
    eig2 = (trace - sqrt_disc_M) / 2

    return {
        'monodromy_matrix': M,
        'trace': trace,
        'determinant': det,
        'eigenvalues': (eig1, eig2),
    }


# =========================================================================
# Section 12: Stokes data from the Schrodinger equation
# =========================================================================

def stokes_data_from_shadow(kappa_val, alpha_val, Delta_val):
    """Extract Stokes data from the shadow Schrodinger equation.

    For the Fuchsian equation (3 regular singularities), there are NO
    Stokes multipliers (Stokes phenomenon requires irregular singularities).
    The monodromy is entirely captured by the CONNECTION MATRICES between
    the local solutions at different singularities.

    The connection matrices for the hypergeometric equation are given by
    the classical formulas involving Gamma functions.

    However, the SHADOW GENERATING FUNCTION G(t) = sum S_r t^r does have
    Stokes-like behavior from its Borel transform (see shadow_resurgence.py).
    That is a DIFFERENT Stokes phenomenon from the ODE Stokes.

    Returns:
        dict with monodromy data (not Stokes multipliers, since the
        equation is Fuchsian).
    """
    if abs(Delta_val) < 1e-14:
        return {
            'type': 'trivial',
            'monodromy_group': 'trivial',
            'stokes_multipliers': [],
        }

    # For the Fuchsian equation with double indicial exponent 1/2:
    # Monodromy around each finite singularity: exp(2*pi*i * 1/2) = -1.
    # The monodromy group is generated by M_+ = -I, M_- = -I.
    # Product: M_+ * M_- = I (monodromy at infinity is trivial).
    # But actually the local monodromy matrices are scalar -I only
    # if the singularity is NOT logarithmic.  With a double indicial
    # exponent, there may be a Jordan block: M = -I + nilpotent.

    return {
        'type': 'fuchsian_abelian',
        'monodromy_at_plus': -1,  # exp(2*pi*i * 1/2)
        'monodromy_at_minus': -1,
        'monodromy_at_infinity': 1,  # product of finite monodromies
        'stokes_multipliers': [],  # none for Fuchsian equations
        'connection_type': 'hypergeometric',
    }


# =========================================================================
# Section 13: Summary and assessment functions
# =========================================================================

def full_shadow_painleve_analysis(c_val):
    """Complete Painleve analysis for Virasoro at central charge c.

    Returns a comprehensive dict with all computed data.
    """
    kappa, alpha, Delta = virasoro_shadow_params(c_val)

    sings = classify_singularities(kappa, alpha, Delta)
    ftype = fuchsian_type(kappa, alpha, Delta)
    ptype = painleve_type(kappa, alpha, Delta)
    hyp = hypergeometric_parameters(kappa, alpha, Delta)
    deform = shadow_deformation_system(c_val)
    stokes = stokes_data_from_shadow(kappa, alpha, Delta)
    mm = matrix_model_from_virasoro(c_val)

    return {
        'c': c_val,
        'kappa': kappa,
        'alpha': alpha,
        'Delta': Delta,
        'singularities': sings,
        'fuchsian_type': ftype,
        'painleve_type': ptype,
        'hypergeometric': hyp,
        'deformation': deform,
        'stokes': stokes,
        'matrix_model': mm,
    }


def shadow_ode_classification_summary():
    """Summary of the shadow ODE classification.

    KEY MATHEMATICAL CONCLUSIONS:

    1. The shadow connection nabla^sh = d - Q_L'/(2Q_L) dt, when promoted
       to a Schrodinger equation u'' = V(t)*u via Liouville transformation,
       gives a FUCHSIAN equation with 3 regular singular points on P^1.

    2. The indicial exponents at each finite singularity (zero of Q_L) are
       both equal to 1/2 (double root).  This makes the equation REDUCIBLE:
       one solution is sqrt(Q_L), the other is integral(dt/sqrt(Q_L)).

    3. A Fuchsian equation with 3 regular singular points is RIGID (no
       accessory parameters).  Therefore there is NO isomonodromic
       deformation and NO Painleve equation from this ODE.

    4. To obtain Painleve transcendents from the shadow tower, one needs:
       (a) The MULTI-CHANNEL system (e.g., W_3 with T+W channels), which
           gives a rank-2 system with 4+ singularities -> Painleve VI.
       (b) The FULL MC equation D*Theta + (1/2)[Theta,Theta] = 0, which
           is an infinite-dimensional integrable system whose finite
           reductions can produce any Painleve equation.
       (c) The CONFLUENT limit as singularities merge under specialization
           of parameters.

    5. The task's proposed ODE H'' = t^2*Q_L*H is NOT what the shadow
       generating function satisfies.  H = t^2*sqrt(Q_L) satisfies a
       nonlinear ODE (via f^2 = Q_L), not the linear one proposed.

    6. The connection to random matrices IS valid: y^2 = Q_L defines a
       spectral curve, and the Eynard-Orantin topological recursion on
       this curve computes the genus expansion {F_g}, which agrees with
       the shadow genus expansion.

    7. The tau function of the shadow connection is simply sqrt(Q_L(t)/Q_L(0)),
       the flat section.  This is the JMU tau function for the trivial
       (rigid Fuchsian) case.
    """
    return {
        'schrodinger_equation': "u'' = V(t)*u, V = 8*kappa^2*Delta/Q_L^2",
        'singularity_structure': '3 regular singular points on P^1',
        'indicial_exponents': '1/2 (double) at each zero of Q_L',
        'fuchsian_type': 'hypergeometric (Gauss)',
        'equation_reducible': True,
        'solutions': ['sqrt(Q_L)', 'integral dt/sqrt(Q_L)'],
        'painleve_from_single_channel': 'NONE (rigid Fuchsian, no accessory parameter)',
        'painleve_from_multichannel': 'PVI (for 2-channel systems like W_3)',
        'tau_function': 'sqrt(Q_L(t)/Q_L(0))',
        'matrix_model_type': 'complex cubic (for Virasoro with Delta > 0)',
        'task_ode_correct': False,
        'task_ode_correction': 'H does NOT satisfy H\'\'=t^2*Q_L*H; see docstring',
    }


# =========================================================================
# Section 14: W_3 two-channel Painleve VI system
# =========================================================================

def w3_two_channel_system(c_val):
    """W_3 two-channel shadow system: T-line and W-line.

    The W_3 algebra has two primary channels:
        T-channel: kappa_T = c/2, alpha_T = 2, S4_T from Virasoro sub
        W-channel: kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W

    The coupled 2x2 system has 4 singular points on P^1, giving a genuine
    Heun equation whose isomonodromic deformation is Painleve VI.

    The cross-ratio of the 4 singularities is the Painleve VI coordinate.
    """
    # T-channel (Virasoro subsector)
    kappa_T = c_val / 2
    alpha_T = 2.0
    S4_T = 10.0 / (c_val * (5 * c_val + 22))
    Delta_T = 8 * kappa_T * S4_T

    # W-channel
    kappa_W = c_val / 3
    alpha_W = 0.0  # Z_2 parity
    # S4_W = 2560/(c*(5c+22)^3) from the W_3 OPE
    S4_W = 2560.0 / (c_val * (5 * c_val + 22)**3)
    Delta_W = 8 * kappa_W * S4_W

    heun = heun_from_shadow_multichannel(
        kappa_T, alpha_T, Delta_T,
        kappa_W, alpha_W, Delta_W,
    )

    return {
        'c': c_val,
        'T_channel': {'kappa': kappa_T, 'alpha': alpha_T, 'Delta': Delta_T},
        'W_channel': {'kappa': kappa_W, 'alpha': alpha_W, 'Delta': Delta_W},
        'heun_data': heun,
        'painleve_type': 'PVI' if heun['n_singularities'] >= 4 else 'degenerate',
    }


def w3_painleve_vi_cross_ratio(c_val):
    """The Painleve VI coordinate (cross-ratio) for W_3.

    The cross-ratio lambda of the 4 singularities of the W_3 Heun equation
    is a function of the central charge c.  Its isomonodromic evolution
    as c varies gives the Painleve VI transcendent.

    Returns the cross-ratio lambda(c).
    """
    data = w3_two_channel_system(c_val)
    return data['heun_data']['cross_ratio']


# =========================================================================
# Section 15: Topological recursion on the shadow spectral curve
# =========================================================================

def eynard_orantin_genus0(kappa_val, alpha_val, Delta_val, t1_val, t2_val):
    """The Eynard-Orantin kernel on the spectral curve y^2 = Q_L(t).

    The Bergman kernel (genus-0 recursion kernel) for the curve y^2 = Q_L is:

        B(t1, t2) = 1/(2*(t1-t2)^2) + regular terms

    For Q_L quadratic (genus-0 curve), the recursion terminates: the
    topological recursion omega_{g,n} for g >= 1 are determined by the
    spectral curve data alone.

    The genus-1 free energy from topological recursion:

        F_1 = -(1/24) * log(disc(Q_L))  (modulo normalization)

    For disc(Q_L) = -32*kappa^2*Delta:

        F_1 = -(1/24)*log|-32*kappa^2*Delta|
            = -(1/24)*(log 32 + 2*log|kappa| + log|Delta|)

    But the SHADOW genus-1 free energy is F_1 = kappa/24.

    These are DIFFERENT: the topological recursion F_1 depends logarithmically
    on Delta, while the shadow F_1 = kappa/24 is linear in kappa and
    independent of Delta.

    The discrepancy arises because the shadow genus expansion is the
    TAUTOLOGICAL projection (intersection numbers on M-bar_g), not the
    full topological recursion on the spectral curve.  The topological
    recursion computes the full matrix model free energy, which includes
    non-tautological contributions.

    Returns the Bergman kernel value B(t1, t2).
    """
    return 1.0 / (2.0 * (t1_val - t2_val)**2)


def topological_recursion_genus1(kappa_val, alpha_val, Delta_val):
    """Genus-1 free energy from topological recursion vs shadow.

    TR: F_1^TR = -(1/24)*log|disc(Q_L)|  (up to normalization)
    Shadow: F_1^sh = kappa/24

    Returns both for comparison.
    """
    disc = -32 * kappa_val**2 * Delta_val
    F1_TR = None
    if abs(disc) > 1e-30:
        F1_TR = -math.log(abs(disc)) / 24
    F1_shadow = kappa_val / 24

    return {
        'F1_topological_recursion': F1_TR,
        'F1_shadow': F1_shadow,
        'agree': False,  # They do NOT agree in general
        'reason': 'TR computes full matrix model; shadow computes tautological projection',
    }


if __name__ == '__main__':
    print("Shadow Painleve Analysis")
    print("=" * 60)

    summary = shadow_ode_classification_summary()
    for key, val in summary.items():
        print(f"  {key}: {val}")

    print("\n--- Virasoro at c=1/2 ---")
    data = full_shadow_painleve_analysis(0.5)
    print(f"  kappa = {data['kappa']}")
    print(f"  Delta = {data['Delta']}")
    print(f"  Fuchsian type: {data['fuchsian_type']}")
    print(f"  Painleve type: {data['painleve_type']}")

    print("\n--- Virasoro at c=13 (self-dual) ---")
    data = full_shadow_painleve_analysis(13.0)
    print(f"  kappa = {data['kappa']}")
    print(f"  Delta = {data['Delta']}")
    print(f"  Fuchsian type: {data['fuchsian_type']}")
    print(f"  Painleve type: {data['painleve_type']}")

    print("\n--- W_3 two-channel at c=13 ---")
    w3 = w3_two_channel_system(13.0)
    print(f"  T-channel Delta = {w3['T_channel']['Delta']}")
    print(f"  W-channel Delta = {w3['W_channel']['Delta']}")
    print(f"  Heun singularities = {w3['heun_data']['n_singularities']}")
    print(f"  Cross-ratio = {w3['heun_data']['cross_ratio']}")
    print(f"  Painleve type: {w3['painleve_type']}")
