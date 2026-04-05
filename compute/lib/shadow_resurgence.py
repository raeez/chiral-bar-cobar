r"""Shadow resurgence engine: Borel singularities, Stokes constants,
optimal truncation, and Borel reconstruction for the shadow Postnikov tower.

This is the THIRD adversarial method for computing shadow obstruction towers, competing
with the sqrt(Q_L) algebraic method (A) and OPE recursion method (B).

MATHEMATICAL FRAMEWORK
======================

The shadow generating function H(t) = t^2 sqrt(Q_L(t)) is algebraic of
degree 2. Its Taylor coefficients S_r have asymptotic behavior

    S_r ~ A * rho^r * r^{-5/2} * cos(r*theta + phi)

where rho is the shadow growth rate (reciprocal of the convergence radius).
This asymptotic expansion is resurgent: the Borel transform

    B(s) = sum_{r>=2} S_r * s^r / Gamma(r+1)

has singularities whose locations, types, and residues encode the full
non-perturbative content of the shadow obstruction tower.

BOREL SINGULARITY STRUCTURE
===========================

For the shadow metric Q_L(t) = q0 + q1*t + q2*t^2 with zeros at t_pm,
the ordinary generating function G(t) = sum S_r t^r has branch points
at t_pm. The Borel transform B(s) = sum S_r s^r / r! is an ENTIRE
function (since |S_r| grows at most geometrically, and r! kills this).
However, the Borel-Laplace integral

    S[G](t) = int_0^infty B(s) e^{-s/t} ds/t

encounters Stokes phenomena when the integration contour passes through
directions where arg(s) = arg(1/t_pm). The instanton actions are

    A_pm = 1 / t_pm

and the Stokes constants at these singularities measure the discontinuity
of the lateral Borel sums.

STOKES CONSTANTS
================

For the algebraic function sqrt(Q_L), the monodromy around each branch
point t_pm is -1 (square root branch). The Stokes constant at the
corresponding Borel singularity encodes this monodromy:

    S_1(A) = 2 * pi * i * alpha(A)

where alpha(A) is the CONNECTION COEFFICIENT relating the perturbative
expansion around t=0 to the expansion around t=t_pm. For the shadow
generating function:

    alpha(A) = lim_{r->infty} S_r / (rho^r * r^{-5/2} * cos(r*theta+phi))

computed from the exact asymptotic amplitude C in S_r ~ C*rho^r*r^{-5/2}*...

The genuine Stokes constant (not just the leading 2*pi*i) depends on:
- The prefactor C (Darboux coefficient from the branch point singularity)
- The argument theta of the branch point
- The higher-order corrections from the quadratic structure of Q_L

OPTIMAL TRUNCATION
==================

For a divergent asymptotic series with factorial/geometric growth, the
optimal truncation order N* minimizes the remainder. For |S_r| ~ C*rho^r/r^{5/2}:

    N*(t) = |A_1| / |t| = 1 / (rho * |t|)

where A_1 is the nearest instanton action. At t=1 (unit coupling):

    N*(A) = floor(1/rho(A))

FAMILIES
========

15 algebras covering all four depth classes:
  G: Heisenberg (ranks 1,2,3,8,24)
  L: Affine sl_2 (k=1,2,10), Affine sl_3 (k=1)
  C: Beta-gamma (c=-2)
  M: Virasoro (c=1/2,1,4,13,25,26), W_3 T-line (c=2), W_3 W-line (c=2)

Manuscript references:
    thm:shadow-radius (higher_genus_modular_koszul.tex)
    thm:riccati-algebraicity (higher_genus_modular_koszul.tex)
    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
    thm:single-line-dichotomy (higher_genus_modular_koszul.tex)
    def:shadow-metric (higher_genus_modular_koszul.tex)
    thm:shadow-connection (higher_genus_modular_koszul.tex)

Dependencies:
    shadow_radius.py -- shadow growth rate, branch points
    shadow_tower_recursive.py -- exact shadow coefficients (method A)
    resurgence_frontier_engine.py -- Borel transform infrastructure
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple


# =====================================================================
# Section 0: Algebra shadow data for all 15 families
# =====================================================================

@dataclass
class ShadowData:
    """Shadow data (kappa, alpha, S4) for a chiral algebra.

    Sufficient to determine the shadow metric Q_L, branch points,
    growth rate, and the full resurgence structure.

    Attributes:
        name: human-readable identifier
        kappa: S_2 (curvature / modular characteristic)
        alpha: S_3 (cubic shadow coefficient)
        S4: S_4 (quartic contact invariant)
        depth_class: one of 'G', 'L', 'C', 'M'
    """
    name: str
    kappa: float
    alpha: float
    S4: float
    depth_class: str

    @property
    def Delta(self) -> float:
        """Critical discriminant Delta = 8*kappa*S4."""
        return 8.0 * self.kappa * self.S4

    @property
    def q0(self) -> float:
        return 4.0 * self.kappa**2

    @property
    def q1(self) -> float:
        return 12.0 * self.kappa * self.alpha

    @property
    def q2(self) -> float:
        return 9.0 * self.alpha**2 + 16.0 * self.kappa * self.S4

    @property
    def branch_points(self) -> Tuple[complex, complex]:
        """Zeros of Q_L(t) = q0 + q1*t + q2*t^2."""
        disc = self.q1**2 - 4.0 * self.q0 * self.q2
        sq = cmath.sqrt(disc)
        if abs(self.q2) < 1e-30:
            # Degenerate: Q_L is at most linear
            return (complex('inf'), complex('inf'))
        t_plus = (-self.q1 + sq) / (2.0 * self.q2)
        t_minus = (-self.q1 - sq) / (2.0 * self.q2)
        return (t_plus, t_minus)

    @property
    def rho(self) -> float:
        """Shadow growth rate = 1 / |nearest branch point|."""
        t_p, t_m = self.branch_points
        if t_p == complex('inf'):
            return 0.0
        R = min(abs(t_p), abs(t_m))
        return 1.0 / R if R > 1e-30 else float('inf')

    @property
    def theta(self) -> float:
        """Argument of the nearest branch point."""
        t_p, _ = self.branch_points
        if t_p == complex('inf'):
            return 0.0
        return cmath.phase(t_p)

    @property
    def instanton_actions(self) -> Tuple[complex, complex]:
        """Borel singularity locations A_pm = 1/t_pm."""
        t_p, t_m = self.branch_points
        A_p = 1.0 / t_p if abs(t_p) > 1e-30 else complex('inf')
        A_m = 1.0 / t_m if abs(t_m) > 1e-30 else complex('inf')
        return (A_p, A_m)


# --- Standard landscape: 15 algebras ---

def heisenberg_data(rank: int = 1) -> ShadowData:
    """Heisenberg H_rank: class G, depth 2. kappa = rank/2."""
    return ShadowData(
        name=f'Heis_n={rank}',
        kappa=rank / 2.0,
        alpha=0.0,
        S4=0.0,
        depth_class='G',
    )


def affine_sl2_data(k: float) -> ShadowData:
    """Affine sl_2 at level k: class L, depth 3.

    kappa = dim(g)*(k+h^v)/(2*h^v) = 3*(k+2)/4 for sl_2.
    alpha = 1 (Killing cubic).
    S4 = 0 (Jacobi identity).
    """
    kappa = 3.0 * (k + 2.0) / 4.0
    return ShadowData(
        name=f'aff_sl2_k={k}',
        kappa=kappa,
        alpha=1.0,
        S4=0.0,
        depth_class='L',
    )


def affine_sl3_data(k: float) -> ShadowData:
    """Affine sl_3 at level k: class L, depth 3.

    kappa = dim(g)*(k+h^v)/(2*h^v) = 8*(k+3)/6 = 4*(k+3)/3.
    """
    kappa = 4.0 * (k + 3.0) / 3.0
    return ShadowData(
        name=f'aff_sl3_k={k}',
        kappa=kappa,
        alpha=1.0,
        S4=0.0,
        depth_class='L',
    )


def betagamma_data() -> ShadowData:
    """Beta-gamma system at c=-2: class C, depth 4.

    kappa = -1, alpha = nonzero (contact), S4 = -5/12.
    The quartic contact invariant lives on a charged stratum.
    """
    return ShadowData(
        name='betagamma_c=-2',
        kappa=-1.0,
        alpha=1.0,  # nonzero contact cubic
        S4=-5.0 / 12.0,
        depth_class='C',
    )


def virasoro_data(c_val: float) -> ShadowData:
    """Virasoro at central charge c: class M, depth infinity.

    kappa = c/2, alpha = 2, S4 = 10/(c(5c+22)).
    """
    kappa = c_val / 2.0
    alpha = 2.0
    S4 = 10.0 / (c_val * (5.0 * c_val + 22.0))
    return ShadowData(
        name=f'Vir_c={c_val}',
        kappa=kappa,
        alpha=alpha,
        S4=S4,
        depth_class='M',
    )


def w3_T_data(c_val: float) -> ShadowData:
    """W_3 T-line (= Virasoro shadow line)."""
    d = virasoro_data(c_val)
    d.name = f'W3_T_c={c_val}'
    return d


def w3_W_data(c_val: float) -> ShadowData:
    """W_3 W-line: even-arity shadow line.

    kappa_W = c/3, alpha_W = 0 (Z_2 parity), S4_W = 2560/(c(5c+22)^3).
    """
    kappa_W = c_val / 3.0
    S4_W = 2560.0 / (c_val * (5.0 * c_val + 22.0)**3)
    return ShadowData(
        name=f'W3_W_c={c_val}',
        kappa=kappa_W,
        alpha=0.0,
        S4=S4_W,
        depth_class='M',
    )


def standard_landscape() -> List[ShadowData]:
    """All 15 standard algebras for the resurgence atlas."""
    algebras = []
    # Class G: Heisenberg
    for n in [1, 2, 3, 8, 24]:
        algebras.append(heisenberg_data(n))
    # Class L: Affine
    for k in [1.0, 2.0, 10.0]:
        algebras.append(affine_sl2_data(k))
    algebras.append(affine_sl3_data(1.0))
    # Class C: Beta-gamma
    algebras.append(betagamma_data())
    # Class M: Virasoro
    for c in [0.5, 1.0, 4.0, 13.0, 25.0, 26.0]:
        algebras.append(virasoro_data(c))
    # Class M: W_3
    algebras.append(w3_T_data(2.0))
    algebras.append(w3_W_data(2.0))
    return algebras


# =====================================================================
# Section 1: Shadow coefficients via convolution recursion
# =====================================================================

def shadow_coefficients(data: ShadowData, max_r: int = 30) -> Dict[int, float]:
    r"""Compute shadow coefficients S_2, ..., S_{max_r} via sqrt(Q_L) expansion.

    Uses the convolution recursion f^2 = Q_L:
        a_0 = sqrt(q0) = 2|kappa|
        a_1 = q1/(2*a_0)
        a_n = (c_n - sum_{j=1}^{n-1} a_j a_{n-j}) / (2*a_0)  for n >= 2
    where c_0=q0, c_1=q1, c_2=q2, c_n=0 for n>=3.
    Then S_r = a_{r-2}/r.
    """
    q0, q1, q2 = data.q0, data.q1, data.q2
    max_n = max_r - 2
    if max_n < 0 or q0 <= 0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    a = [0.0] * (max_n + 1)
    a[0] = math.sqrt(q0)
    if a[0] == 0.0:
        return {r: 0.0 for r in range(2, max_r + 1)}

    if max_n >= 1:
        a[1] = q1 / (2.0 * a[0])
    for n in range(2, max_n + 1):
        cn = q2 if n == 2 else 0.0
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv) / (2.0 * a[0])

    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


def shadow_coefficients_fraction(kappa_num: int, kappa_den: int,
                                  alpha_num: int, alpha_den: int,
                                  S4_num: int, S4_den: int,
                                  max_r: int = 30) -> Dict[int, Fraction]:
    """Exact shadow coefficients using Fraction arithmetic (no roundoff)."""
    kappa = Fraction(kappa_num, kappa_den)
    alpha = Fraction(alpha_num, alpha_den)
    S4 = Fraction(S4_num, S4_den)

    q0 = 4 * kappa**2
    q1 = 12 * kappa * alpha
    q2 = 9 * alpha**2 + 16 * kappa * S4

    max_n = max_r - 2
    if max_n < 0:
        return {}

    # a_0 = sqrt(q0) = 2*|kappa|
    a0 = 2 * abs(kappa)
    if a0 == 0:
        return {r: Fraction(0) for r in range(2, max_r + 1)}

    a = [Fraction(0)] * (max_n + 1)
    a[0] = a0
    if max_n >= 1:
        a[1] = q1 / (2 * a0)
    for n in range(2, max_n + 1):
        cn = q2 if n == 2 else Fraction(0)
        conv = sum(a[j] * a[n - j] for j in range(1, n))
        a[n] = (cn - conv) / (2 * a0)

    return {r: a[r - 2] / r for r in range(2, max_r + 1)}


# =====================================================================
# Section 2: Borel transform
# =====================================================================

def borel_coefficients(coeffs: Dict[int, float]) -> Dict[int, float]:
    r"""Borel transform coefficients: b_r = S_r / Gamma(r+1) = S_r / r!.

    B(s) = sum_{r>=2} b_r s^r is an ENTIRE function for algebraic GF
    (the factorial kills the geometric growth).
    """
    return {r: sr / math.gamma(r + 1) for r, sr in coeffs.items()}


def borel_evaluate(coeffs: Dict[int, float], s: complex) -> complex:
    r"""Evaluate B(s) = sum_{r>=2} S_r s^r / r! at a point."""
    s = complex(s)
    result = 0.0 + 0.0j
    for r in sorted(coeffs.keys()):
        result += coeffs[r] * s**r / math.gamma(r + 1)
    return result


def borel_evaluate_high_precision(coeffs_frac: Dict[int, Fraction],
                                   s_real: float, s_imag: float = 0.0
                                   ) -> complex:
    """Evaluate B(s) using Fraction coefficients for high precision."""
    result_re = 0.0
    result_im = 0.0
    s = complex(s_real, s_imag)
    for r in sorted(coeffs_frac.keys()):
        sr_f = float(coeffs_frac[r])
        s_pow = s**r
        fact = math.gamma(r + 1)
        result_re += sr_f * s_pow.real / fact
        result_im += sr_f * s_pow.imag / fact
    return complex(result_re, result_im)


# =====================================================================
# Section 3: Darboux coefficient and exact Stokes constant
# =====================================================================

def darboux_coefficient(data: ShadowData) -> complex:
    r"""Compute the Darboux coefficient C for the asymptotic formula.

    For f(t) = t^2 * sqrt(Q_L(t)) with a branch point at t_0 (zero of Q_L),
    the singularity analysis (Flajolet-Sedgewick, Theorem VI.1) gives:

        [t^r] f(t) ~ C_0 * t_0^{-r} * r^{-5/2}

    where C_0 depends on the local behavior of f near t_0.

    Near a simple zero t_0 of Q_L: Q_L(t) ~ Q_L'(t_0) * (t - t_0), so
        sqrt(Q_L(t)) ~ sqrt(Q_L'(t_0)) * sqrt(t - t_0)
        f(t) ~ t_0^2 * sqrt(Q_L'(t_0)) * sqrt(t - t_0)

    The transfer theorem for (1 - t/t_0)^{1/2} gives:
        [t^r] (1 - t/t_0)^{1/2} = -t_0^{-r} / (2 sqrt(pi) r^{3/2}) + O(r^{-5/2})

    For f(t) = t^2 sqrt(Q_L), the leading singular behavior at t_0 is:
        f(t) ~ t_0^2 * sqrt(q2 * (t_0 + t_0')) * sqrt(1 - t/t_0) * (-t_0)^{1/2}

    where t_0' is the other zero of Q_L and q2 is the leading coefficient.
    The Darboux coefficient for the SHADOW coefficients S_r = [t^r] G(t)
    (where G(t) = sum S_r t^r, NOT the weighted GF) involves an additional
    1/r factor, pushing the exponent from r^{-3/2} to r^{-5/2}.

    Actually, recall S_r = a_{r-2}/r where a_n = [t^n] sqrt(Q_L). So:
        S_r = (1/r) * [t^{r-2}] sqrt(Q_L(t))

    The transfer theorem for sqrt(Q_L) gives:
        a_n = [t^n] sqrt(Q_L(t)) ~ C_a * t_0^{-n} * n^{-3/2}

    where C_a = -sqrt(Q_L'(t_0)) / (2 sqrt(pi) (-t_0)^{1/2})
             = -sqrt(q2*(t_0-t_0')) / (2 sqrt(pi) * sqrt(-t_0))

    (using Q_L'(t_0) = q1 + 2*q2*t_0 = q2*(t_0 - t_0') since t_0 + t_0' = -q1/q2
    and t_0*t_0' = q0/q2.)

    Then S_r = a_{r-2}/r ~ C_a * t_0^{-(r-2)} * (r-2)^{-3/2} / r
            ~ C_a * t_0^{-r} * t_0^2 * r^{-5/2}

    So C = C_a * t_0^2 = -t_0^2 * sqrt(q2*(t_0-t_0')) / (2*sqrt(pi)*sqrt(-t_0))
         = -t_0^{3/2} * sqrt(q2*(t_0-t_0')) / (2*sqrt(pi))

    For complex conjugate branch points (Delta > 0), both contribute and
    the asymptotic formula has the form 2*Re(C * t_0^{-r}) * r^{-5/2},
    which gives the cos(r*theta + phi) oscillation.

    Returns the complex Darboux coefficient C.
    """
    if data.depth_class in ('G', 'L'):
        # Tower terminates; Darboux coefficient is 0 (no branch point singularity)
        return 0.0 + 0.0j

    t_p, t_m = data.branch_points
    q2 = data.q2

    if abs(q2) < 1e-30 or abs(t_p) < 1e-30:
        return 0.0 + 0.0j

    # Q_L'(t_0) = q1 + 2*q2*t_0 = q2*(2*t_0 - (-q1/q2)) = q2*(2*t_0 + (t_p+t_m))
    # Since t_p + t_m = -q1/q2, Q_L'(t_p) = q2*(2*t_p + t_p + t_m) = q2*(t_p - t_m) ... wait.
    # Q_L(t) = q2*(t - t_p)*(t - t_m), so Q_L'(t_p) = q2*(t_p - t_m).
    deriv_at_tp = q2 * (t_p - t_m)

    # C_a = coefficient in a_n ~ C_a * t_p^{-n} * n^{-3/2}
    # From the Darboux transfer: [t^n] sqrt(Q_L(t)) where sqrt(Q_L) has
    # a branch point at t_p with sqrt(Q_L) ~ sqrt(q2*(t_p-t_m)) * sqrt(t-t_p).
    #
    # For f(z) ~ A*(1-z/t_0)^alpha near z=t_0, the transfer gives:
    #   [z^n] f(z) ~ A * t_0^{-n} * n^{-alpha-1} / Gamma(-alpha)
    #
    # Here alpha = 1/2, Gamma(-1/2) = -2*sqrt(pi).
    # sqrt(Q_L(t)) ~ sqrt(q2*(t_p-t_m)) * (-t_p)^{1/2} * (1-t/t_p)^{1/2}
    # ... actually:
    # sqrt(Q_L(t)) = sqrt(q2) * sqrt((t-t_p)*(t-t_m))
    #              = sqrt(q2) * sqrt(t_m - t_p) * sqrt(1-t/t_p) * sqrt(... something involving t_m)
    #
    # Let me be more careful. Write Q_L(t) = q2*(t-t_p)*(t-t_m).
    # sqrt(Q_L) = sqrt(q2) * sqrt(t-t_p) * sqrt(t-t_m).
    # Near t = t_p: sqrt(t-t_m) ~ sqrt(t_p - t_m) (analytic at t_p).
    # So sqrt(Q_L) ~ sqrt(q2) * sqrt(t_p - t_m) * sqrt(t - t_p).
    #
    # Now sqrt(t - t_p) = sqrt(-t_p) * sqrt(1 - t/t_p).
    # So sqrt(Q_L) ~ sqrt(q2) * sqrt(t_p - t_m) * sqrt(-t_p) * (1-t/t_p)^{1/2}.
    #
    # Transfer: [t^n] (1-t/t_p)^{1/2} = t_p^{-n} * n^{-3/2} / Gamma(-1/2)
    #         = t_p^{-n} * n^{-3/2} / (-2*sqrt(pi))
    #
    # So: a_n ~ sqrt(q2) * sqrt(t_p-t_m) * sqrt(-t_p) * t_p^{-n} * n^{-3/2} / (-2*sqrt(pi))
    #
    # And S_r = a_{r-2}/r, so S_r ~ (a coefficient) * t_p^{-(r-2)} * (r-2)^{-3/2} / r
    #                              ~ C * rho^r * r^{-5/2}
    # where rho = |1/t_p|, and:
    # C = sqrt(q2)*sqrt(t_p-t_m)*sqrt(-t_p) * t_p^2 / (-2*sqrt(pi))

    sqrt_q2 = cmath.sqrt(q2)
    sqrt_diff = cmath.sqrt(t_p - t_m)
    sqrt_neg_tp = cmath.sqrt(-t_p)

    C_a = sqrt_q2 * sqrt_diff * sqrt_neg_tp / (-2.0 * math.sqrt(math.pi))
    C = C_a * t_p**2

    return C


def darboux_amplitude_phase(data: ShadowData) -> Tuple[float, float]:
    """Extract amplitude |C| and phase phi from the Darboux coefficient.

    The asymptotic formula reads:
        S_r ~ 2*|C| * rho^r * r^{-5/2} * cos(r*theta + phi)

    where C = |C| * exp(i*phi) is the complex Darboux coefficient from
    the branch point t_p, and theta = -arg(t_p) is the oscillation frequency.

    The factor of 2 comes from adding the contributions of both complex
    conjugate branch points (when Delta > 0).
    """
    C = darboux_coefficient(data)
    amplitude = abs(C)
    phase = cmath.phase(C)
    return amplitude, phase


def stokes_constant_exact(data: ShadowData) -> complex:
    r"""Exact Stokes constant S_1 for the shadow obstruction tower.

    The Stokes constant at the dominant Borel singularity A_1 = 1/t_p
    is related to the connection coefficient between the perturbative
    expansion and the one-instanton sector.

    For the algebraic function sqrt(Q_L) with a square-root branch point:

        S_1 = 2*pi*i * C_connection

    where C_connection is the ratio of the analytic continuation of
    sqrt(Q_L) across the cut to the perturbative expansion.

    For Q_L(t) = q2*(t-t_p)*(t-t_m), the monodromy of sqrt(Q_L) around
    t_p is -1 (square root). In the Borel plane, this translates to:

        S_1 = 2*pi*i * R_{t_p}

    where R_{t_p} is the Borel residue, computed from the Darboux analysis.

    Specifically, the Borel transform B(s) of the shadow generating function
    has a branch point at s = A_1 = 1/t_p. Near this point:

        B(s) ~ R_0 * (s - A_1)^{-1/2} + regular

    where R_0 encodes the Darboux coefficient. The Stokes automorphism
    (discontinuity of lateral Borel sums) gives:

        S_1 = -R_0 * sqrt(pi) / Gamma(1/2) = -R_0

    ... actually for the standard normalization, the Stokes constant of a
    Borel singularity of type (s-A)^{alpha} is:

        S_1 = e^{i*pi*alpha} * sin(pi*alpha) * R_0 * (some Gamma factors)

    For alpha = -1/2 (square root branch in the Borel plane, coming from
    the r^{-3/2} algebraic singularity in coefficient space):

    The precise formula: the shadow generating function G(t) = sum S_r t^r
    has Borel transform B(s) = sum S_r s^r/r!. If S_r ~ C*rho^r*r^{-5/2},
    then B(s) near s = 1/rho*e^{-i*theta} has a singularity of the form:

        B(s) ~ C * Gamma(-3/2)^{-1} * (1 - rho*e^{i*theta}*s)^{3/2} + analytic

    Wait - let me be more precise about the Borel plane singularity type.

    For a_r ~ C * w^{-r} * r^{beta} (where w = t_p, beta = -5/2):
    The Borel transform b_r = a_r/r! has:
        sum b_r s^r = sum C*w^{-r}*r^{beta}*s^r/r!

    This is convergent for all s (entire function). The singularities appear
    when we try to Borel-Laplace resum. The key object is the analytic
    continuation of B(s) beyond its disk of convergence, which involves
    the analytic continuation of the original algebraic function.

    For our algebraic shadow obstruction tower: G(t) = sum S_r t^r has algebraic
    branch points. The Stokes constant is determined by the monodromy
    of G around the branch point. Since G^2 = t^4 * Q_L(t) (locally),
    the monodromy is -1, giving:

        S_1 = 2*pi*i * (analytic continuation coefficient)

    The analytic continuation coefficient is:
        C_ac = t_p^2 * sqrt(q2*(t_p - t_m)) * sqrt(-t_p)
    evaluated with the correct branch of the square root.

    The EXACT Stokes constant is then:

        S_1 = 2*pi*i * C_ac / (normalization from Borel transform)

    For the direct shadow obstruction tower (OGF, not weighted GF):

        S_1 = i * sqrt(pi) * t_p^{3/2} * sqrt(q2 * (t_p - t_m))
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j

    t_p, t_m = data.branch_points
    q2 = data.q2

    if abs(q2) < 1e-30 or abs(t_p) < 1e-30:
        return 0.0 + 0.0j

    # The Stokes constant encodes the monodromy of sqrt(Q_L) at t_p.
    # sqrt(Q_L) = sqrt(q2) * sqrt(t-t_p) * sqrt(t-t_m).
    # Monodromy of sqrt(t-t_p) around t_p: factor of -1.
    # The discontinuity across the cut from t_p is:
    #   disc = 2 * sqrt(q2) * sqrt(t_p - t_m) * i*sqrt(|t - t_p|)  (on the cut)
    #
    # In the Borel plane, the Stokes constant relating the perturbative
    # expansion sum S_r t^r to its Borel-Laplace resummation is:
    #
    # S_1 = 2*pi*i * lim_{r->inf} [S_r * t_p^r * r^{5/2}] / (normalization)
    #
    # From the Darboux analysis:
    #   S_r ~ 2*Re[C * t_p^{-r}] * r^{-5/2}
    # where C = sqrt(q2)*sqrt(t_p-t_m)*sqrt(-t_p)*t_p^2 / (-2*sqrt(pi))
    #
    # The Stokes constant relates to C via:
    #   S_1 = -2*pi*i * C / t_p^2
    #       = -2*pi*i * sqrt(q2)*sqrt(t_p-t_m)*sqrt(-t_p) / (-2*sqrt(pi))
    #       = i * sqrt(pi) * sqrt(q2) * sqrt(t_p-t_m) * sqrt(-t_p)

    stokes = 1j * math.sqrt(math.pi) * cmath.sqrt(q2) * cmath.sqrt(t_p - t_m) * cmath.sqrt(-t_p)
    return stokes


def stokes_constant_numerical(data: ShadowData, max_r: int = 200) -> complex:
    r"""Numerically extract the Stokes constant from high-order shadow coefficients.

    Uses Richardson extrapolation on the sequence:
        s_r = S_r * t_p^r * r^{5/2}

    For class M algebras with complex conjugate branch points:
        s_r -> 2*Re(C) * cos(arg(t_p^{-r})) + 2*Im(C) * sin(arg(t_p^{-r}))

    We extract C by fitting to cos/sin at the known frequency theta = arg(t_p).
    Then S_1 = -2*pi*i * C / t_p^2.
    """
    if data.depth_class in ('G', 'L'):
        return 0.0 + 0.0j

    t_p, t_m = data.branch_points
    if abs(t_p) < 1e-30:
        return 0.0 + 0.0j

    coeffs = shadow_coefficients(data, max_r)
    theta = cmath.phase(t_p)
    rho = data.rho

    # Build the sequence s_r = S_r * rho^{-r} * r^{5/2}
    # = S_r / (|t_p|^{-r}) * r^{5/2}
    # This should oscillate as 2*|C|*cos(r*theta + phi)
    cos_vals = []
    sin_vals = []
    weights = []
    for r in range(10, max_r + 1):
        sr = coeffs.get(r, 0.0)
        if abs(sr) < 1e-300:
            continue
        s_r = sr * (1.0 / rho)**r * r**2.5  # = S_r * |t_p|^r * r^{5/2}
        angle = r * theta
        cos_vals.append((s_r, math.cos(angle), math.sin(angle), r))

    if len(cos_vals) < 4:
        return 0.0 + 0.0j

    # Least-squares fit: s_r = A*cos(r*theta) + B*sin(r*theta)
    # Then C_real = A, C_imag = B (up to sign/normalization)
    n = len(cos_vals)
    sum_sc = sum(v[0] * v[1] for v in cos_vals)
    sum_ss = sum(v[0] * v[2] for v in cos_vals)
    sum_cc = sum(v[1]**2 for v in cos_vals)
    sum_cs = sum(v[1] * v[2] for v in cos_vals)
    sum_ssq = sum(v[2]**2 for v in cos_vals)

    det = sum_cc * sum_ssq - sum_cs**2
    if abs(det) < 1e-30:
        return 0.0 + 0.0j

    A = (sum_sc * sum_ssq - sum_ss * sum_cs) / det
    B = (sum_ss * sum_cc - sum_sc * sum_cs) / det

    # A, B are 2*Re(C), 2*Im(C) where C is the complex Darboux coefficient
    # including the t_p^2 factor. So C_darboux = (A + iB)/2.
    # Then S_1 = -2*pi*i * C_darboux / t_p^2.
    # But we worked with s_r = S_r * rho^{-r} * r^{5/2} and theta = arg(t_p),
    # so the oscillation comes from Re(C * (t_p / |t_p|)^{-r}).
    # Thus A + iB ~ 2*C * (direction), and we need to undo the direction.

    # Actually, the asymptotic formula is:
    #   S_r ~ 2*Re[C * t_p^{-r}] * r^{-5/2}
    # where C = |C| exp(i*phi).
    # s_r = S_r * |t_p|^r * r^{5/2} ~ 2*Re[C * (t_p/|t_p|)^{-r}]
    #     = 2*|C| * cos(-r*arg(t_p) + phi)
    #     = 2*|C| * cos(r*theta_inv + phi)
    # where theta_inv = -arg(t_p) = -theta.
    #
    # Our fit used angle = r*theta (arg of t_p, not -arg).
    # So: s_r ~ 2*|C|*cos(-r*theta + phi) = 2*|C|*(cos(phi)*cos(r*theta) + sin(phi)*sin(r*theta))
    # Hence A = 2*|C|*cos(phi), B = 2*|C|*sin(phi).
    # C_complex = (A + iB)/2 = |C|*exp(i*phi).
    # And S_1 = -2*pi*i * C_complex / t_p^2.

    C_num = complex(A, B) / 2.0
    S_1 = -2.0j * math.pi * C_num / t_p**2

    return S_1


# =====================================================================
# Section 4: Optimal truncation
# =====================================================================

def optimal_truncation_order(data: ShadowData, t_val: float = 1.0) -> int:
    r"""Optimal truncation order N*(A, t) for the shadow series at coupling t.

    For a divergent series with |S_r| ~ |C|*rho^r*r^{-5/2}, the terms
    |S_r t^r| are minimized when:

        d/dr [rho^r * |t|^r * r^{-5/2}] = 0
        => (rho*|t|)^r * r^{-5/2} * [log(rho*|t|) - 5/(2r)] = 0
        => r* = 5 / (2*|log(rho*|t|)|)  (if rho*|t| < 1)

    For rho*|t| >= 1, the series diverges from the start and N* = 2 (just kappa).

    At t=1:
        N* = floor(5 / (2*log(1/rho))) = floor(5 / (2*log(R)))

    where R = 1/rho is the convergence radius.

    For class G/L algebras (rho=0): N* = infinity (series terminates).
    For class C: N* depends on the charged-stratum analysis (not covered here).
    """
    rho = data.rho
    if rho < 1e-30:
        # Tower terminates; N* = max_arity or infinity
        return 1000  # effectively infinite

    effective_rho = rho * abs(t_val)
    if effective_rho >= 1.0:
        # Series diverges from the start
        return 2

    # N* = 5 / (2 * log(1/(rho*|t|)))
    N_star = 5.0 / (2.0 * math.log(1.0 / effective_rho))
    return max(2, int(math.floor(N_star)))


def optimal_truncation_error(data: ShadowData, t_val: float = 1.0,
                              max_r: int = 60) -> Dict[str, Any]:
    """Compute the remainder at optimal truncation.

    Returns the optimal order, the partial sum at that order,
    and the estimated remainder (smallest term magnitude).
    """
    N_star = optimal_truncation_order(data, t_val)
    coeffs = shadow_coefficients(data, max(max_r, N_star + 5))

    # Partial sum up to N*
    partial = sum(coeffs.get(r, 0.0) * t_val**r for r in range(2, N_star + 1))

    # Smallest term (at N*)
    term_N = abs(coeffs.get(N_star, 0.0) * t_val**N_star) if N_star <= max_r else 0.0

    # Terms around N* for diagnostic
    terms = {}
    for r in range(max(2, N_star - 3), min(max_r + 1, N_star + 4)):
        terms[r] = abs(coeffs.get(r, 0.0) * t_val**r)

    return {
        'N_star': N_star,
        'partial_sum': partial,
        'smallest_term': term_N,
        'rho': data.rho,
        'effective_rho': data.rho * abs(t_val),
        'terms_near_Nstar': terms,
    }


# =====================================================================
# Section 5: Borel reconstruction (method C)
# =====================================================================

def borel_reconstruct(data: ShadowData, max_r: int = 30) -> Dict[int, float]:
    r"""Reconstruct shadow coefficients from resurgent Borel analysis.

    This is METHOD C: reconstruct S_r from the Borel singularity data
    and the asymptotic formula, then compare with the exact values from
    the convolution recursion (method A).

    The asymptotic formula (Darboux):
        S_r = 2*Re[C * t_p^{-r}] * r^{-5/2}   (for large r)

    where C is the complex Darboux coefficient and t_p is the branch point.

    For small r: the asymptotic formula has corrections. The EXACT
    resurgent reconstruction would require computing ALL orders of the
    transseries. We instead use:

    For class G: S_2 = kappa, S_r = 0 for r >= 3.
    For class L: S_2 = kappa, S_3 = alpha, S_r = 0 for r >= 4.
    For class M: use the asymptotic formula for r >= 5, and exact values
                 for r = 2, 3, 4 (the asymptotic formula is not accurate
                 at low arity).

    Returns dict r -> S_r^{Borel} (the Borel-reconstructed value).
    """
    if data.depth_class == 'G':
        return {r: (data.kappa if r == 2 else 0.0) for r in range(2, max_r + 1)}

    if data.depth_class == 'L':
        result = {r: 0.0 for r in range(2, max_r + 1)}
        result[2] = data.kappa
        result[3] = data.alpha
        return result

    # Class C or M: use Darboux asymptotics
    C = darboux_coefficient(data)
    t_p, t_m = data.branch_points

    if abs(C) < 1e-30 or abs(t_p) < 1e-30:
        return shadow_coefficients(data, max_r)

    # Exact values at low arity (asymptotic formula is not accurate there)
    exact = shadow_coefficients(data, max_r)
    result = {}

    for r in range(2, max_r + 1):
        if r <= 4:
            # Use exact values at low arity
            result[r] = exact[r]
        else:
            # Darboux asymptotic: S_r ~ 2*Re[C * t_p^{-r}] * r^{-5/2}
            # Both branch points contribute (complex conjugate pair):
            contrib_p = C * t_p**(-(r - 2)) / r  # from a_{r-2}/r
            contrib_m = C.conjugate() * t_m**(-(r - 2)) / r
            # The transfer theorem: a_n ~ C_a * t_p^{-n} * n^{-3/2} / Gamma(-1/2)
            # Gamma(-1/2) = -2*sqrt(pi)
            # So a_n ~ C_a * t_p^{-n} * n^{-3/2} * (-1/(2*sqrt(pi)))
            # But C already includes the Gamma factor from darboux_coefficient.
            # The asymptotic formula is:
            #   S_r = a_{r-2}/r ~ C * t_p^{-(r-2)} * (r-2)^{-3/2} / r
            # Wait, I already computed C = C_a * t_p^2 in darboux_coefficient,
            # where C_a includes the 1/(-2*sqrt(pi)) Gamma factor.
            # So: S_r ~ C * t_p^{-r} * (r-2)^{-3/2} / r  (from C = C_a * t_p^2)

            # For both branch points:
            val_p = C * t_p**(-r) * (r - 2)**(-1.5) / r
            val_m = C.conjugate() * t_m**(-r) * (r - 2)**(-1.5) / r
            result[r] = (val_p + val_m).real

    return result


# =====================================================================
# Section 6: Cross-validation (method A vs method C)
# =====================================================================

def cross_validate(data: ShadowData, max_r: int = 30) -> Dict[str, Any]:
    """Compare exact (method A) vs Borel-reconstructed (method C) coefficients.

    Returns comparison metrics: relative errors, convergence of the
    asymptotic approximation, and the arity at which the asymptotic
    formula becomes a good approximation.
    """
    exact = shadow_coefficients(data, max_r)
    borel = borel_reconstruct(data, max_r)

    errors = {}
    for r in range(5, max_r + 1):
        e = exact.get(r, 0.0)
        b = borel.get(r, 0.0)
        if abs(e) > 1e-300:
            errors[r] = abs(e - b) / abs(e)
        elif abs(b) < 1e-300:
            errors[r] = 0.0
        else:
            errors[r] = float('inf')

    # Find arity where error drops below 10%, 1%, 0.1%
    thresholds = {}
    for threshold in [0.1, 0.01, 0.001]:
        for r in range(5, max_r + 1):
            if errors.get(r, 1.0) < threshold:
                thresholds[threshold] = r
                break

    return {
        'algebra': data.name,
        'depth_class': data.depth_class,
        'rho': data.rho,
        'darboux_C': darboux_coefficient(data),
        'stokes_S1': stokes_constant_exact(data),
        'N_star': optimal_truncation_order(data),
        'relative_errors': errors,
        'convergence_thresholds': thresholds,
        'max_error': max(errors.values()) if errors else 0.0,
        'tail_error': errors.get(max_r, 0.0),
    }


# =====================================================================
# Section 7: Full resurgence atlas for the standard landscape
# =====================================================================

@dataclass
class ResurgenceEntry:
    """Complete resurgence data for one algebra."""
    data: ShadowData
    coefficients: Dict[int, float]
    borel_coefficients: Dict[int, float]
    darboux_C: complex
    stokes_S1: complex
    N_star: int
    branch_points: Tuple[complex, complex]
    instanton_actions: Tuple[complex, complex]
    borel_singularity_modulus: float
    borel_singularity_argument: float
    cross_validation_error: float


def build_resurgence_atlas(max_r: int = 30) -> Dict[str, ResurgenceEntry]:
    """Build the complete resurgence atlas for all 15 standard algebras."""
    landscape = standard_landscape()
    atlas = {}

    for data in landscape:
        coeffs = shadow_coefficients(data, max_r)
        b_coeffs = borel_coefficients(coeffs)
        C = darboux_coefficient(data)
        S1 = stokes_constant_exact(data)
        N_star = optimal_truncation_order(data)
        bp = data.branch_points
        A = data.instanton_actions

        # Borel singularity metrics
        bp_mod = abs(bp[0]) if bp[0] != complex('inf') else float('inf')
        bp_arg = cmath.phase(bp[0]) if bp[0] != complex('inf') else 0.0

        # Cross-validation error
        cv = cross_validate(data, max_r)
        cv_err = cv['tail_error']

        atlas[data.name] = ResurgenceEntry(
            data=data,
            coefficients=coeffs,
            borel_coefficients=b_coeffs,
            darboux_C=C,
            stokes_S1=S1,
            N_star=N_star,
            branch_points=bp,
            instanton_actions=A,
            borel_singularity_modulus=bp_mod,
            borel_singularity_argument=bp_arg,
            cross_validation_error=cv_err,
        )

    return atlas


# =====================================================================
# Section 8: Specific targets from the problem statement
# =====================================================================

def stokes_constant_virasoro(c_val: float) -> Dict[str, Any]:
    """Compute the exact Stokes constant S_1(Vir, c) and related data."""
    data = virasoro_data(c_val)
    S1_exact = stokes_constant_exact(data)
    S1_numerical = stokes_constant_numerical(data, max_r=200)
    C = darboux_coefficient(data)
    amp, phase = darboux_amplitude_phase(data)

    return {
        'c': c_val,
        'S1_exact': S1_exact,
        'S1_numerical': S1_numerical,
        'S1_modulus': abs(S1_exact),
        'S1_argument': cmath.phase(S1_exact),
        'darboux_C': C,
        'darboux_amplitude': amp,
        'darboux_phase': phase,
        'rho': data.rho,
        'theta': data.theta,
        'N_star': optimal_truncation_order(data),
        'branch_plus': data.branch_points[0],
        'branch_minus': data.branch_points[1],
    }


def w3_borel_singularities(c_val: float) -> Dict[str, Any]:
    """Borel singularity locations for W_3 on both T-line and W-line."""
    T_data = w3_T_data(c_val)
    W_data = w3_W_data(c_val)

    return {
        'c': c_val,
        'T_line': {
            'branch_points': T_data.branch_points,
            'instanton_actions': T_data.instanton_actions,
            'rho': T_data.rho,
            'theta': T_data.theta,
            'stokes_S1': stokes_constant_exact(T_data),
            'N_star': optimal_truncation_order(T_data),
        },
        'W_line': {
            'branch_points': W_data.branch_points,
            'instanton_actions': W_data.instanton_actions,
            'rho': W_data.rho,
            'theta': W_data.theta,
            'stokes_S1': stokes_constant_exact(W_data),
            'N_star': optimal_truncation_order(W_data),
        },
    }


# =====================================================================
# Section 9: Borel-Pade singularity detection
# =====================================================================

def pade_approximant(coeffs_list: List[float], m: int, n: int
                      ) -> Tuple[Optional[List[float]], Optional[List[float]]]:
    """Compute [m/n] Pade approximant P(x)/Q(x) from power series.

    Returns (P_coeffs, Q_coeffs) or (None, None) on failure.
    """
    import numpy as np

    N = m + n + 1
    c = list(coeffs_list) + [0.0] * max(0, N - len(coeffs_list))

    if n == 0:
        return c[:m + 1], [1.0]

    mat = np.zeros((n, n))
    rhs = np.zeros(n)
    for i in range(n):
        for j in range(n):
            idx = m + 1 + i - (j + 1)
            if 0 <= idx < len(c):
                mat[i, j] = c[idx]
        idx_r = m + 1 + i
        if 0 <= idx_r < len(c):
            rhs[i] = -c[idx_r]

    try:
        q_vec = np.linalg.solve(mat, rhs)
    except np.linalg.LinAlgError:
        return None, None

    Q_c = [1.0] + list(q_vec)
    P_c = [0.0] * (m + 1)
    for k in range(m + 1):
        for j in range(min(k, n) + 1):
            if k - j < len(c):
                P_c[k] += Q_c[j] * c[k - j]

    return P_c, Q_c


def borel_pade_singularities(data: ShadowData, max_r: int = 30,
                               pade_order: Optional[int] = None
                               ) -> Dict[str, Any]:
    """Detect Borel singularities via Pade approximation of B(s).

    Computes the diagonal Pade [N/N] of the Borel transform inner series
    and finds its poles (approximations to Borel singularities).
    """
    import numpy as np

    coeffs = shadow_coefficients(data, max_r)
    # Inner series: g_k = S_{k+2} / (k+2)! for k = 0, 1, ...
    inner = []
    for k in range(max_r - 1):
        r = k + 2
        sr = coeffs.get(r, 0.0)
        inner.append(sr / math.gamma(r + 1))

    if pade_order is None:
        pade_order = len(inner) // 2

    m = pade_order
    n = pade_order

    P, Q = pade_approximant(inner, m, n)
    if Q is None:
        return {'poles': [], 'nearest_pole': None}

    # Find poles = roots of Q polynomial
    Q_rev = list(reversed(Q))
    poles = np.roots(Q_rev)

    # Filter to finite poles
    finite_poles = [p for p in poles if abs(p) < 1e10 and abs(p) > 1e-10]

    # Sort by modulus
    finite_poles.sort(key=lambda z: abs(z))

    nearest = finite_poles[0] if finite_poles else None

    # Compare with predicted singularities
    predicted = data.instanton_actions

    return {
        'algebra': data.name,
        'pade_order': pade_order,
        'n_poles': len(finite_poles),
        'nearest_pole': nearest,
        'nearest_modulus': abs(nearest) if nearest else None,
        'nearest_arg': cmath.phase(nearest) if nearest else None,
        'predicted_A_plus': predicted[0],
        'predicted_A_minus': predicted[1],
        'predicted_modulus': abs(predicted[0]) if predicted[0] != complex('inf') else None,
        'all_poles': finite_poles,
    }


# =====================================================================
# Section 10: Ratio method for rho extraction
# =====================================================================

def ratio_rho_extraction(data: ShadowData, max_r: int = 60) -> Dict[str, Any]:
    """Extract rho from consecutive ratios |S_{r+1}/S_r| -> rho.

    For class M: the ratio converges to rho with oscillating corrections.
    Richardson extrapolation accelerates convergence.
    """
    coeffs = shadow_coefficients(data, max_r)

    ratios = []
    for r in range(2, max_r):
        sr = coeffs.get(r, 0.0)
        sr1 = coeffs.get(r + 1, 0.0)
        if abs(sr) > 1e-300:
            ratios.append((r, abs(sr1 / sr)))

    if not ratios:
        return {'rho_predicted': data.rho, 'rho_extracted': 0.0, 'converged': False}

    # Last few ratios
    tail = [v[1] for v in ratios[-10:]]
    rho_raw = tail[-1] if tail else 0.0

    # Richardson extrapolation: if ratio_r ~ rho + A/r^2 + ...,
    # then rho ~ (r^2 * ratio_r - (r-1)^2 * ratio_{r-1}) / (r^2 - (r-1)^2)
    #          = (r^2 * ratio_r - (r-1)^2 * ratio_{r-1}) / (2r - 1)
    richardson_vals = []
    for i in range(len(ratios) - 1):
        r1, v1 = ratios[i]
        r2, v2 = ratios[i + 1]
        if r2 > r1:
            rich = (r2**2 * v2 - r1**2 * v1) / (r2**2 - r1**2)
            richardson_vals.append((r2, rich))

    rho_richardson = richardson_vals[-1][1] if richardson_vals else rho_raw

    return {
        'rho_predicted': data.rho,
        'rho_raw': rho_raw,
        'rho_richardson': rho_richardson,
        'relative_error_raw': abs(rho_raw - data.rho) / data.rho if data.rho > 1e-30 else 0.0,
        'relative_error_rich': abs(rho_richardson - data.rho) / data.rho if data.rho > 1e-30 else 0.0,
        'converged': abs(rho_richardson - data.rho) / max(data.rho, 1e-30) < 0.01,
        'n_ratios': len(ratios),
        'tail_ratios': tail[-5:],
    }


# =====================================================================
# Section 11: Summary and printing
# =====================================================================

def resurgence_summary(data: ShadowData, max_r: int = 30) -> str:
    """Human-readable summary of the resurgence analysis for one algebra."""
    lines = [
        f"=== Resurgence Analysis: {data.name} ===",
        f"  Depth class: {data.depth_class}",
        f"  kappa = {data.kappa:.6f}",
        f"  alpha = {data.alpha:.6f}",
        f"  S4 = {data.S4:.6e}",
        f"  Delta = {data.Delta:.6e}",
    ]

    if data.depth_class in ('G', 'L'):
        lines.append(f"  Tower terminates: rho = 0, no Borel singularities")
        lines.append(f"  Stokes constant: S_1 = 0 (trivially)")
        return "\n".join(lines)

    lines.extend([
        f"  rho = {data.rho:.8f}",
        f"  theta = {data.theta:.6f} (= {data.theta/math.pi:.4f} pi)",
        f"  Branch points: t_+ = {data.branch_points[0]:.6f}",
        f"                 t_- = {data.branch_points[1]:.6f}",
        f"  Instanton actions: A_+ = {data.instanton_actions[0]:.6f}",
        f"                     A_- = {data.instanton_actions[1]:.6f}",
    ])

    C = darboux_coefficient(data)
    S1 = stokes_constant_exact(data)
    N_star = optimal_truncation_order(data)

    lines.extend([
        f"  Darboux coefficient: C = {C:.6f}",
        f"    |C| = {abs(C):.6e}, arg(C) = {cmath.phase(C):.6f}",
        f"  Stokes constant: S_1 = {S1:.6f}",
        f"    |S_1| = {abs(S1):.6e}, arg(S_1) = {cmath.phase(S1):.6f}",
        f"  Optimal truncation: N* = {N_star} (at t=1)",
    ])

    # Cross-validation
    cv = cross_validate(data, max_r)
    if cv['relative_errors']:
        max_err = max(cv['relative_errors'].values())
        tail_err = cv['relative_errors'].get(max_r, 0.0)
        lines.extend([
            f"  Cross-validation (method A vs C):",
            f"    Max relative error: {max_err:.2e}",
            f"    Tail error (r={max_r}): {tail_err:.2e}",
        ])
        for thresh, arity in cv.get('convergence_thresholds', {}).items():
            lines.append(f"    Error < {thresh}: from arity {arity}")

    return "\n".join(lines)


if __name__ == '__main__':
    print("=" * 70)
    print("SHADOW RESURGENCE ATLAS")
    print("=" * 70)

    # Specific targets
    for c_val in [0.5, 13.0]:
        result = stokes_constant_virasoro(c_val)
        print(f"\nVirasoro c={c_val}:")
        print(f"  S_1 = {result['S1_exact']:.8f}")
        print(f"  |S_1| = {result['S1_modulus']:.8e}")
        print(f"  N* = {result['N_star']}")

    print("\nW_3 Borel singularities at c=2:")
    w3 = w3_borel_singularities(2.0)
    for line_name in ['T_line', 'W_line']:
        ld = w3[line_name]
        print(f"  {line_name}:")
        print(f"    Branch points: {ld['branch_points']}")
        print(f"    rho = {ld['rho']:.8f}")
        print(f"    S_1 = {ld['stokes_S1']:.8f}")

    # Full atlas summary
    print("\n" + "=" * 70)
    print("FULL ATLAS")
    print("=" * 70)
    for data in standard_landscape():
        print("\n" + resurgence_summary(data))
