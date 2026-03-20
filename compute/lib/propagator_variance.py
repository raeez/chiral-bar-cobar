r"""Propagator variance theorem for multi-channel shadow towers.

THEOREM (Propagator Variance = Non-Autonomy).

For a rank-r chiral algebra A with diagonal curvature matrix
kappa = diag(kappa_1,...,kappa_r) and quartic shadow Sh_4, define
the quartic gradient on the diagonal:

    f_i := (d/dx_i)(Sh_4)|_{x_1=...=x_r=x},  coefficient of x^3.

The non-autonomy of the shadow tower on the diagonal at arity 6 is:

    delta = sum_i f_i^2/kappa_i - (sum_i f_i)^2 / (sum_i kappa_i)

This is the PROPAGATOR VARIANCE of the quartic gradient.

PROPERTIES:
  (1) delta >= 0 by Cauchy-Schwarz.
  (2) delta = 0 iff f_i/kappa_i is independent of i
      (curvature-proportionality of the quartic gradient).
  (3) delta is computable from arity 2 (kappa_i) and arity 4 (Sh_4) alone.
  (4) delta controls the ENTIRE infinite non-autonomy correction:
      Q_diag = Q_autonomous + delta^{1/2} * t^4 * R(t).

PROOF:
  The 2D H-Poisson bracket at x_T=x_W=x:
    {Sh_4, Sh_4}_{2D}|_diag = sum_i (1/kappa_i) f_i^2 * x^6
  The 1D effective bracket:
    {S_4^v x^4, S_4^v x^4}_{1D} = (sum f_i)^2 / (sum kappa_i) * x^6
  The difference is delta * x^6.  QED.

The MIXING POLYNOMIAL P(c) for W_3:
  P = 25c^2 + 100c - 428 = 25(c+2)^2 - 528
  P = 0 iff f_T/kappa_T = f_W/kappa_W (enhanced symmetry).

References:
  thm:propagator-variance (new)
  thm:single-line-dichotomy
  thm:shadow-archetype-classification
  thm:virasoro-shadow-generating-function
"""

from __future__ import annotations

from typing import Dict, List, Tuple

from sympy import (
    Matrix, Rational, Symbol, cancel, diff, expand, factor,
    simplify, sqrt, symbols, Poly,
)


c = Symbol('c')


# =========================================================================
# General propagator variance
# =========================================================================

def propagator_variance(kappas: List, f_values: List) -> object:
    r"""Compute the propagator variance.

    delta = sum f_i^2/kappa_i - (sum f_i)^2 / (sum kappa_i)

    Args:
        kappas: list of curvature eigenvalues [kappa_1, ..., kappa_r]
        f_values: list of quartic gradient values [f_1, ..., f_r]

    Returns:
        The propagator variance delta (a sympy expression).
    """
    term1 = sum(f**2 / k for f, k in zip(f_values, kappas))
    term2 = sum(f_values)**2 / sum(kappas)
    return cancel(term1 - term2)


def curvature_proportionality_test(kappas: List, f_values: List) -> object:
    r"""Test whether f_i/kappa_i is independent of i.

    Returns f_i/kappa_i - f_j/kappa_j for the first pair (i,j).
    Zero iff curvature-proportional.
    """
    ratios = [cancel(f / k) for f, k in zip(f_values, kappas)]
    if len(ratios) < 2:
        return Rational(0)
    return cancel(ratios[0] - ratios[1])


def mixing_polynomial(kappas: List, f_values: List) -> object:
    r"""Extract the mixing polynomial P(c).

    P = 0 iff the quartic gradient is curvature-proportional.
    Normalized so that P is a polynomial in c with integer coefficients.
    """
    test = curvature_proportionality_test(kappas, f_values)
    if test == 0:
        return Rational(0)
    # Extract the numerator polynomial
    num = cancel(test)
    from sympy import numer, denom
    return factor(numer(cancel(num)))


# =========================================================================
# W_3 specific
# =========================================================================

def w3_kappas():
    """Curvature eigenvalues for W_3: kappa_T = c/2, kappa_W = c/3."""
    return [c / 2, c / 3]


def w3_quartic_gradients():
    """Quartic gradient f_i = d_i(Sh_4)|_diag for W_3.

    From the Lambda-exchange quartic with alpha = 16/(5c+22):
      Sh_4 = Q₀[x_T^4 + 6α x_T^2 x_W^2 + α² x_W^4]
    where Q₀ = 10/[c(5c+22)], α = 16/(5c+22).

    f_T = (d/dx_T)(Sh_4)|_{x_T=x_W=x} at x^3:
        = 4Q₀ + 12Q₀α = 4Q₀(1 + 3α) = 200(c+14)/[c(5c+22)²]

    f_W = (d/dx_W)(Sh_4)|_{x_T=x_W=x} at x^3:
        = 12Q₀α + 4Q₀α² = 4Q₀α(3 + α) = 640(15c+82)/[c(5c+22)³]
    """
    Q0 = Rational(10) / (c * (5 * c + 22))
    alpha = Rational(16) / (5 * c + 22)

    f_T = 4 * Q0 * (1 + 3 * alpha)
    f_W = 4 * Q0 * alpha * (3 + alpha)

    return [cancel(f_T), cancel(f_W)]


def w3_mixing_polynomial():
    """The mixing polynomial P(c) = 25c² + 100c - 428 for W_3."""
    return 25 * c**2 + 100 * c - 428


def w3_propagator_variance():
    """Propagator variance for W_3."""
    kappas = w3_kappas()
    fs = w3_quartic_gradients()
    return propagator_variance(kappas, fs)


def w3_enhanced_symmetry_loci():
    """Central charges where P = 0 (enhanced symmetry)."""
    from sympy import solve
    P = w3_mixing_polynomial()
    return solve(P, c)


# =========================================================================
# General rank-r algebra
# =========================================================================

def autonomy_criterion(kappas: List, f_values: List) -> bool:
    """Test whether the diagonal is autonomous (delta = 0).

    Returns True iff f_i/kappa_i is independent of i.
    """
    return propagator_variance(kappas, f_values) == 0


def cauchy_schwarz_bound(kappas: List, f_values: List) -> object:
    """The Cauchy-Schwarz ratio: delta * sum(kappa) / sum(f)^2.

    This is >= 0, and equals 0 iff autonomous.
    """
    delta = propagator_variance(kappas, f_values)
    return cancel(delta * sum(kappas) / sum(f_values)**2)
