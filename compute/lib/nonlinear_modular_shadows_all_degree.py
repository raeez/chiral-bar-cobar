"""Finite-degree checks for the nonlinear modular shadow master equation.

The theorem surface in ``appendices/nonlinear_modular_shadows.tex`` is
formal: the master equation lives in the completed degree filtration, and
the degree-r component is obtained by collecting the ordered bracket pairs
whose single-edge contraction has output degree r.

This module keeps that bookkeeping explicit.  It is intentionally small:
it does not import the manuscript and it does not use the existing
Virasoro shadow-tower engines.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from sympy import Rational, Symbol, cancel, simplify


c = Symbol("c")


@dataclass(frozen=True)
class PairCoefficient:
    """One unordered degree-r bracket contribution."""

    p: int
    q: int
    ordered_count: int
    coefficient: Rational

    @property
    def pair(self) -> tuple[int, int]:
        return (self.p, self.q)


def bracket_output_degree(p: int, q: int) -> int:
    """Degree of a single-edge contraction of p- and q-linear tensors."""
    if p < 2 or q < 2:
        raise ValueError("shadow tensors start in degree 2")
    return p + q - 2


def ordered_degree_pairs(r: int) -> list[tuple[int, int]]:
    """Ordered pairs contributing to the degree-r part of {S,S}.

    The degree-r projection can only see pairs (p,q) with p+q-2=r.
    We include the linear pair (2,r) and its reverse; lower nonlinear
    obstruction pairs are extracted separately.
    """
    if r < 3:
        raise ValueError("the shadow master equation starts at degree 3")
    pairs: list[tuple[int, int]] = []
    for p in range(2, r + 1):
        q = r + 2 - p
        if 2 <= q <= r:
            pairs.append((p, q))
    return pairs


def unordered_half_bracket_coefficients(r: int) -> list[PairCoefficient]:
    """Collect ordered degree-r terms in one half of the bracket.

    The equation {S,S}=0 is equivalent to (1/2){S,S}=0.  After this
    harmless division by two, a non-diagonal unordered pair has coefficient
    1 because its two orderings both appear, while a diagonal pair has
    coefficient 1/2.
    """
    counts: dict[tuple[int, int], int] = {}
    for p, q in ordered_degree_pairs(r):
        key = (p, q) if p <= q else (q, p)
        counts[key] = counts.get(key, 0) + 1

    return [
        PairCoefficient(
            p=pair[0],
            q=pair[1],
            ordered_count=count,
            coefficient=Rational(count, 2),
        )
        for pair, count in sorted(counts.items())
    ]


def linear_pair_coefficient(r: int) -> PairCoefficient:
    """The coefficient of {Sh_2, Sh_r} after collecting ordered pairs."""
    for item in unordered_half_bracket_coefficients(r):
        if item.p == 2 and item.q == r:
            return item
    raise AssertionError(f"degree {r} has no linear pair")


def obstruction_pair_coefficients(r: int) -> list[PairCoefficient]:
    """The nonlinear obstruction pairs for degree r."""
    return [
        item
        for item in unordered_half_bracket_coefficients(r)
        if item.p >= 3
    ]


def obstruction_is_future_free(r: int) -> bool:
    """True iff every obstruction pair uses shadows already below degree r."""
    return all(item.p < r and item.q < r for item in obstruction_pair_coefficients(r))


def scalar_sewing_coefficient(
    p: int,
    q: int,
    s_p: Any,
    s_q: Any,
    propagator: Any,
) -> Any:
    """Coefficient of {S_p x^p, S_q x^q}_H on a one-dimensional slice."""
    return cancel(p * q * propagator * s_p * s_q)


def scalar_obstruction_coefficient(
    r: int,
    shadows: Mapping[int, Any],
    propagator: Any,
) -> Any:
    """Coefficient of the degree-r obstruction on a scalar slice."""
    total = Rational(0)
    for item in obstruction_pair_coefficients(r):
        total += item.coefficient * scalar_sewing_coefficient(
            item.p,
            item.q,
            shadows[item.p],
            shadows[item.q],
            propagator,
        )
    return cancel(total)


def scalar_master_residual(
    r: int,
    shadows: Mapping[int, Any],
    propagator: Any,
    linear_eigenvalue: Any | None = None,
) -> Any:
    """Residual of the scalar propagation equation at degree r.

    In the Virasoro one-primary propagation gauge used by the local compute
    layer, ``nabla_H`` acts on the unknown degree-r scalar by multiplication
    by ``2r``.  The cubic and quartic shadows are seed data; the recurrence
    begins at degree 5.
    """
    if linear_eigenvalue is None:
        linear_eigenvalue = 2 * r
    return simplify(
        linear_eigenvalue * shadows[r]
        + scalar_obstruction_coefficient(r, shadows, propagator)
    )


def solve_scalar_tower_from_seeds(
    *,
    s2: Any,
    s3: Any,
    s4: Any,
    propagator: Any,
    max_r: int,
) -> dict[int, Any]:
    """Solve the scalar master recurrence from seed shadows through max_r."""
    if max_r < 4:
        raise ValueError("need max_r >= 4 to include the quartic seed")
    shadows: dict[int, Any] = {2: s2, 3: s3, 4: s4}
    for r in range(5, max_r + 1):
        obstruction = scalar_obstruction_coefficient(r, shadows, propagator)
        shadows[r] = cancel(-obstruction / (2 * r))
    return shadows


def virasoro_master_tower(max_r: int = 16) -> dict[int, Any]:
    """Virasoro scalar tower from the all-degree master recurrence."""
    return solve_scalar_tower_from_seeds(
        s2=c / 2,
        s3=Rational(2),
        s4=Rational(10) / (c * (5 * c + 22)),
        propagator=Rational(2) / c,
        max_r=max_r,
    )


def virasoro_generating_function_tower(max_r: int = 16) -> dict[int, Any]:
    """Virasoro scalar tower from the independent square-root identity.

    Let H(t)=sum_{r>=2} h_r t^r with h_r=r S_r.  The shadow metric identity

        H(t)^2 = t^4 (c^2 + 12 c t + ((180c+872)/(5c+22)) t^2)

    determines every h_r by coefficient comparison.  This route does not
    use the master-equation obstruction pairs.
    """
    if max_r < 4:
        raise ValueError("need max_r >= 4")

    q2 = (180 * c + 872) / (5 * c + 22)
    h: dict[int, Any] = {
        2: c,
        3: Rational(6),
    }
    h[4] = cancel((q2 - h[3] ** 2) / (2 * h[2]))

    for n in range(7, max_r + 3):
        r = n - 2
        if r > max_r:
            break
        convolution = Rational(0)
        for i in range(3, n - 2):
            j = n - i
            if i in h and j in h:
                convolution += h[i] * h[j]
        h[r] = cancel(-convolution / (2 * h[2]))

    return {r: cancel(h[r] / r) for r in range(2, max_r + 1)}

