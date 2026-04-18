"""Audit helpers for the toroidal formal-disk DIM surface in Vol I.

This module is intentionally narrow.  It records the parameter-level facts
that survive first-principles audit for the Ding-Iohara-Miki structure
function in the formal-disk setting:

1. the standard DIM convention q_1 = q, q_2 = t^{-1}, q_3 = t/q;
2. the cyclic parameter action often attached to the Miki automorphism;
3. the degeneration at t = q, where q_3 = 1 and the scalar structure
   function collapses to 1;
4. the rational/additive classical limit, which yields the usual three-factor
   toroidal/affine-Yangian structure function.

It does NOT implement a full 2 x 2 FRT/RTT matrix presentation for
U_{q,t}(ddot sl_2).  The local audited surface here is the current-exchange
kernel encoded by the DIM structure function.
"""

from __future__ import annotations

from dataclasses import dataclass

from sympy import Expr, exp, factor, limit, simplify, sympify


@dataclass(frozen=True)
class DIMParameters:
    """Two-parameter DIM convention with q_1 q_2 q_3 = 1."""

    q: Expr
    t: Expr
    q1: Expr
    q2: Expr
    q3: Expr


def dim_parameters(q, t) -> DIMParameters:
    """Return the standard DIM parameter triple.

    Convention used elsewhere in the programme:
      q_1 = q, q_2 = t^{-1}, q_3 = t/q.
    """

    q = sympify(q)
    t = sympify(t)
    return DIMParameters(q=q, t=t, q1=q, q2=1 / t, q3=t / q)


def structure_function(x, *, q=None, t=None, q1=None, q2=None, q3=None) -> Expr:
    """Scalar DIM structure function G(x).

    G(x) = prod_i (1 - q_i x) / (1 - x/q_i), with q_1 q_2 q_3 = 1.
    """

    x = sympify(x)
    if q1 is None or q2 is None or q3 is None:
        if q is None or t is None:
            raise ValueError("Provide either (q, t) or (q1, q2, q3).")
        params = dim_parameters(q, t)
        q1, q2, q3 = params.q1, params.q2, params.q3
    else:
        q1 = sympify(q1)
        q2 = sympify(q2)
        q3 = sympify(q3)

    numer = (1 - q1 * x) * (1 - q2 * x) * (1 - q3 * x)
    denom = (1 - x / q1) * (1 - x / q2) * (1 - x / q3)
    return simplify(numer / denom)


def current_exchange_factor(z, w, q, t) -> Expr:
    """Current-level DIM exchange factor for E(z) E(w)."""

    z = sympify(z)
    w = sympify(w)
    return structure_function(w / z, q=q, t=t)


def miki_parameter_cycle(params: DIMParameters) -> DIMParameters:
    """Cyclic permutation of the DIM triple.

    At the level of q_i this is:
      (q_1, q_2, q_3) -> (q_2, q_3, q_1).

    Re-expressed in (q, t) coordinates:
      q' = q_2 = 1/t,
      t' = 1/q_2' = 1/q_3 = q/t.
    """

    q_new = simplify(params.q2)
    t_new = simplify(1 / params.q3)
    cycled = dim_parameters(q_new, t_new)
    if simplify(cycled.q1 - params.q2) != 0:
        raise ValueError("DIM cycle did not send q1 to q2.")
    if simplify(cycled.q2 - params.q3) != 0:
        raise ValueError("DIM cycle did not send q2 to q3.")
    if simplify(cycled.q3 - params.q1) != 0:
        raise ValueError("DIM cycle did not send q3 to q1.")
    return cycled


def miki_orbit(q, t, length: int = 3) -> list[DIMParameters]:
    """Successive cyclic DIM parameter states."""

    orbit = [dim_parameters(q, t)]
    for _ in range(length):
        orbit.append(miki_parameter_cycle(orbit[-1]))
    return orbit


def t_equals_q_degeneracy(q, x) -> Expr:
    """Specialize G(x) at t = q.

    In the standard DIM convention t = q gives q_1 = q, q_2 = q^{-1},
    q_3 = 1, hence G(x) = 1.
    """

    q = sympify(q)
    x = sympify(x)
    return simplify(structure_function(x, q=q, t=q))


def classical_limit_factor(u, h_plus, h_minus, eps) -> Expr:
    """Single-factor additive limit.

    limit_{eps -> 0} (1 - exp(eps (u + h_plus))) / (1 - exp(eps (u - h_minus))).
    """

    u = sympify(u)
    h_plus = sympify(h_plus)
    h_minus = sympify(h_minus)
    eps = sympify(eps)
    factor_expr = (1 - exp(eps * (u + h_plus))) / (1 - exp(eps * (u - h_minus)))
    return simplify(limit(factor_expr, eps, 0))


def classical_limit_structure_function(u, h1, h2):
    """Additive/rational limit of the DIM structure function.

    Write q_i = exp(eps * h_i), x = exp(eps * u), h_3 = -h_1 - h_2.  Then

      lim_{eps -> 0} G(exp(eps u))
        = prod_i (u + h_i) / (u - h_i).
    """

    u = sympify(u)
    h1 = sympify(h1)
    h2 = sympify(h2)
    h3 = simplify(-h1 - h2)
    return simplify(((u + h1) * (u + h2) * (u + h3)) / ((u - h1) * (u - h2) * (u - h3)))


def classical_limit_from_multiplicative(u, h1, h2, eps):
    """Compute the multiplicative-to-additive limit directly."""

    u = sympify(u)
    h1 = sympify(h1)
    h2 = sympify(h2)
    eps = sympify(eps)
    h3 = simplify(-h1 - h2)
    x = exp(eps * u)
    g = structure_function(
        x,
        q1=exp(eps * h1),
        q2=exp(eps * h2),
        q3=exp(eps * h3),
    )
    return simplify(limit(g, eps, 0))


def classical_limit_denominator(u, h1, h2):
    """Denominator of the rational toroidal limit."""

    return factor(classical_limit_structure_function(u, h1, h2).as_numer_denom()[1])
