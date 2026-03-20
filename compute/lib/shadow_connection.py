r"""The shadow connection: logarithmic connection of the shadow metric.

THEOREM (Shadow connection).
Let A be a chirally Koszul algebra and L a primary line with
shadow metric Q_L(t) (Definition def:shadow-metric).

(i)   Q_L defines a logarithmic connection ∇^sh = d - Q'/(2Q) dt
      on the trivial line bundle O_L over L \ {Q = 0}.

(ii)  Regular singular points at the zeros of Q with residue 1/2.
      Monodromy: exp(2πi · 1/2) = -1 (the Koszul sign).

(iii) Parallel transport: Φ(t) = √(Q(t)/Q(0)). Shadow GF = t²√Q.

(iv)  Koszul duality transforms Q(t,c) → Q(t,26-c).
      Dual Lee-Yang points: -22/5 + 152/5 = 26.
      Self-dual at c = 13.

(v)   Complementarity sum: Δ(c) + Δ(26-c) = 6960/[(5c+22)(152-5c)].
      Constant numerator.

(vi)  Multi-channel curvature = propagator variance δ_mix.

(vii) Monodromy factors through Z/2: sheet exchange = Koszul sign.

References:
  thm:shadow-connection (new)
  def:shadow-metric
  thm:riccati-algebraicity
  thm:propagator-variance
"""

from __future__ import annotations

from sympy import (
    I, Rational, Symbol, cancel, diff, exp, factor, log,
    numer, denom, pi, simplify, sqrt, symbols,
)

c = Symbol('c')
t = Symbol('t')


# =========================================================================
# Shadow metric and connection form
# =========================================================================

def shadow_metric(kappa, alpha, S4):
    """The shadow metric Q_L(t) = (2κ)² + 4κα·t + (α² + 16κ²S₄)·t²."""
    return (2*kappa)**2 + 4*kappa*alpha*t + (alpha**2 + 16*kappa**2*S4)*t**2


def critical_discriminant(kappa, S4):
    """Δ = 8κS₄."""
    return 8*kappa*S4


def connection_form(Q):
    """The logarithmic connection 1-form ω = Q'/(2Q) dt."""
    Q_prime = diff(Q, t)
    return cancel(Q_prime / (2*Q))


def parallel_transport(Q, kappa):
    """Parallel transport Φ(t) = √(Q(t)/Q(0)) = √Q/(2κ)."""
    Q0 = Q.subs(t, 0)
    return sqrt(Q / Q0)


# =========================================================================
# Virasoro specialization
# =========================================================================

def virasoro_shadow_metric():
    """Q_Vir(t) = c² + 12ct + α(c)t² where α = (180c+872)/(5c+22)."""
    alpha_c = (180*c + 872) / (5*c + 22)
    return c**2 + 12*c*t + alpha_c*t**2


def virasoro_connection_form():
    """Connection 1-form for Virasoro."""
    Q = virasoro_shadow_metric()
    return connection_form(Q)


def virasoro_discriminant():
    """Critical discriminant Δ = 40/(5c+22)."""
    return Rational(40) / (5*c + 22)


# =========================================================================
# Koszul duality
# =========================================================================

def koszul_dual_metric(Q_expr):
    """Apply Koszul duality c → 26-c to the shadow metric."""
    return Q_expr.subs(c, 26 - c)


def complementarity_sum_discriminant():
    """Δ(c) + Δ(26-c) = 6960/[(5c+22)(152-5c)]."""
    Delta = virasoro_discriminant()
    Delta_dual = Delta.subs(c, 26 - c)
    return cancel(Delta + Delta_dual)


def dual_lee_yang_points():
    """The Koszul-dual Lee-Yang points: -22/5 and 152/5."""
    return (Rational(-22, 5), Rational(152, 5))


# =========================================================================
# Residues and monodromy
# =========================================================================

def connection_residue_at_zero(Q):
    """Residue of ω = Q'/(2Q) at a simple zero of Q.

    At a simple zero t₀: Q(t) ≈ Q'(t₀)(t-t₀), so
    ω ≈ 1/(2(t-t₀)), giving residue 1/2.
    """
    return Rational(1, 2)


def monodromy_at_zero():
    """Monodromy around a zero of Q: exp(2πi · residue) = exp(πi) = -1.

    This is the KOSZUL SIGN.
    """
    return -1


# =========================================================================
# Multi-channel curvature
# =========================================================================

def multi_channel_curvature(kappas, f_values):
    """The curvature of the shadow connection on the multi-channel space.

    This equals the propagator variance δ_mix.
    """
    from .propagator_variance import propagator_variance
    return propagator_variance(kappas, f_values)


# =========================================================================
# Complementarity analysis
# =========================================================================

def complementarity_sum_metric():
    """Q(t,c) + Q(t,26-c)."""
    Q = virasoro_shadow_metric()
    Q_dual = koszul_dual_metric(Q)
    return cancel(Q + Q_dual)


def complementarity_product_metric():
    """Q(t,c) · Q(t,26-c) — the shadow norm."""
    Q = virasoro_shadow_metric()
    Q_dual = koszul_dual_metric(Q)
    return cancel(Q * Q_dual)


def self_dual_metric():
    """Q(t, 13) — the shadow metric at the self-dual point."""
    Q = virasoro_shadow_metric()
    return Q.subs(c, 13)
