r"""Exact sphere correlators of the Virasoro stress tensor.

Let

    G_n(z_1, ..., z_n) = <T(z_1) ... T(z_n)>_{P^1}

in the vacuum sector of ``Vir_c``.  The singular part of the stress-tensor
operator product expansion gives the sphere Ward recursion

    G_n(z, Z) = sum_i [
        (c/2) (z-z_i)^(-4) G_{n-2}(Z \ {z_i})
        + 2 (z-z_i)^(-2) G_{n-1}(Z)
        + (z-z_i)^(-1) partial_{z_i} G_{n-1}(Z)
    ],

with ``G_0 = 1`` and ``G_1 = 0``.  The three summands are retained
separately as the central, stress-exchange, and derivative contributions.

The connected correlator is the cumulant

    G_n^conn = sum_{pi in Pi_n} (-1)^(|pi|-1) (|pi|-1)!
               product_{B in pi} G_|B|(z_B).

An independent cycle expansion supplies an exact oracle.  For ``n >= 3``,

    G_n^conn = c sum_C product_{(i,j) in E(C)} (z_i-z_j)^(-2),

where ``C`` runs over unoriented Hamiltonian cycles on the labelled points;
the two-point term is ``c/(2 z_12^4)``.  This follows directly from Wick
contraction of ``T = (1/2):J^2:`` for a free boson and polynomiality in the
number of bosons.

These functions produce rational functions on configuration space.  A
scalar ``S_r`` arises after supplying the ordered residue complex
``H_res(Vir_c; X)``, an Arnold class, a residue projection, and its
normalization.  The two current weight-six formulas therefore remain
attached to the formal relation and weighted-Riccati extractions.  A
level-six radical/decoupling map supplies the additional singular-vector
interpretation of the formal relation coefficient.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations
from math import factorial
from typing import Iterable, Sequence

import sympy as sp


MAX_ARITY = 6
CENTRAL_CHARGE = sp.Symbol("c")
RESIDUE_PROJECTION_REQUIREMENT = (
    "Supply H_res(Vir_c; X), an ordered Arnold class, a residue projection, "
    "and its normalization before assigning a scalar S_r to G_r^conn."
)
WEIGHT_SIX_SCOPE = (
    "G_6^conn retains its configuration-space variables. C_6^rel and "
    "R_6^Ricc arise from distinct formal extractions; H_res and the "
    "ordered residue map determine their comparison, while a level-six "
    "radical/decoupling map supplies singular-vector meaning."
)


class ResidueProjectionRequired(RuntimeError):
    """Raised when a scalar is requested from a coordinate correlator."""


@dataclass(frozen=True)
class WardRecursionTerms:
    """The three singular contributions in one stress-tensor insertion."""

    central: sp.Expr
    stress_exchange: sp.Expr
    derivative: sp.Expr

    @property
    def total(self) -> sp.Expr:
        """Their exact sum."""

        return sp.Add(self.central, self.stress_exchange, self.derivative)


def _validated_points(points: Iterable[sp.Symbol]) -> tuple[sp.Symbol, ...]:
    result = tuple(sp.sympify(point) for point in points)
    if len(result) > MAX_ARITY:
        raise ValueError(f"implemented arity is at most {MAX_ARITY}")
    if any(not isinstance(point, sp.Symbol) for point in result):
        raise TypeError("Ward differentiation requires independent symbols")
    if len(set(result)) != len(result):
        raise ValueError("configuration-space symbols are pairwise distinct")
    return result


@lru_cache(maxsize=None)
def _set_partitions(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Set partitions of ``range(n)``, each block ordered increasingly."""

    if n == 0:
        return ((),)

    result: list[tuple[tuple[int, ...], ...]] = []
    for partition in _set_partitions(n - 1):
        result.append(partition + ((n - 1,),))
        for block_index in range(len(partition)):
            extended = list(partition)
            extended[block_index] = extended[block_index] + (n - 1,)
            result.append(tuple(extended))
    return tuple(result)


@lru_cache(maxsize=None)
def _ward_correlator(
    points: tuple[sp.Symbol, ...],
    central_charge: sp.Expr,
) -> sp.Expr:
    n = len(points)
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return sp.Integer(0)

    inserted = points[0]
    remaining = points[1:]
    previous = _ward_correlator(remaining, central_charge)
    central_terms: list[sp.Expr] = []
    stress_terms: list[sp.Expr] = []
    derivative_terms: list[sp.Expr] = []

    for index, point in enumerate(remaining):
        omitted = remaining[:index] + remaining[index + 1 :]
        separation = inserted - point
        central_terms.append(
            central_charge
            * sp.Rational(1, 2)
            * _ward_correlator(omitted, central_charge)
            / separation**4
        )
        stress_terms.append(2 * previous / separation**2)
        derivative_terms.append(sp.diff(previous, point) / separation)

    return sp.Add(*central_terms, *stress_terms, *derivative_terms)


def ward_recursion_terms(
    points: Sequence[sp.Symbol],
    central_charge: object = CENTRAL_CHARGE,
) -> WardRecursionTerms:
    """Return the central, stress-exchange, and derivative contributions.

    ``points[0]`` is the inserted stress tensor.  The result sums to
    :func:`virasoro_ward_correlator` on the same ordered symbols.
    """

    symbols = _validated_points(points)
    if len(symbols) < 2:
        raise ValueError("one Ward insertion requires at least two points")

    c = sp.sympify(central_charge)
    inserted = symbols[0]
    remaining = symbols[1:]
    previous = _ward_correlator(remaining, c)
    central_terms: list[sp.Expr] = []
    stress_terms: list[sp.Expr] = []
    derivative_terms: list[sp.Expr] = []

    for index, point in enumerate(remaining):
        omitted = remaining[:index] + remaining[index + 1 :]
        separation = inserted - point
        central_terms.append(
            c
            * sp.Rational(1, 2)
            * _ward_correlator(omitted, c)
            / separation**4
        )
        stress_terms.append(2 * previous / separation**2)
        derivative_terms.append(sp.diff(previous, point) / separation)

    return WardRecursionTerms(
        central=sp.Add(*central_terms),
        stress_exchange=sp.Add(*stress_terms),
        derivative=sp.Add(*derivative_terms),
    )


def virasoro_ward_correlator(
    points: Sequence[sp.Symbol],
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    """Return the exact vacuum sphere correlator ``G_n`` for ``n <= 6``."""

    symbols = _validated_points(points)
    return _ward_correlator(symbols, sp.sympify(central_charge))


@lru_cache(maxsize=None)
def _connected_correlator(
    points: tuple[sp.Symbol, ...],
    central_charge: sp.Expr,
) -> sp.Expr:
    n = len(points)
    if n == 0:
        return sp.Integer(0)

    terms: list[sp.Expr] = []
    for partition in _set_partitions(n):
        product = sp.Integer(1)
        for block in partition:
            block_points = tuple(points[index] for index in block)
            product *= _ward_correlator(block_points, central_charge)
        if product != 0:
            block_count = len(partition)
            mobius = (-1) ** (block_count - 1) * factorial(block_count - 1)
            terms.append(mobius * product)
    return sp.Add(*terms)


def virasoro_connected_correlator(
    points: Sequence[sp.Symbol],
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    """Return ``G_n^conn`` by Möbius inversion on set partitions."""

    symbols = _validated_points(points)
    return _connected_correlator(symbols, sp.sympify(central_charge))


def cycle_connected_correlator(
    points: Sequence[sp.Symbol],
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    """Return the connected correlator from unoriented cycle graphs."""

    symbols = _validated_points(points)
    c = sp.sympify(central_charge)
    n = len(symbols)
    if n < 2:
        return sp.Integer(0)
    if n == 2:
        return c * sp.Rational(1, 2) / (symbols[0] - symbols[1]) ** 4

    terms: list[sp.Expr] = []
    for tail in permutations(range(1, n)):
        if tail[0] > tail[-1]:
            continue
        cycle = (0,) + tail
        product = c
        for index in range(n):
            source = symbols[cycle[index]]
            target = symbols[cycle[(index + 1) % n]]
            product /= (source - target) ** 2
        terms.append(product)
    return sp.Add(*terms)


def cycle_expansion_correlator(
    points: Sequence[sp.Symbol],
    central_charge: object = CENTRAL_CHARGE,
) -> sp.Expr:
    """Return the full correlator by assembling connected cycle graphs."""

    symbols = _validated_points(points)
    c = sp.sympify(central_charge)
    if len(symbols) == 0:
        return sp.Integer(1)

    terms: list[sp.Expr] = []
    for partition in _set_partitions(len(symbols)):
        product = sp.Integer(1)
        for block in partition:
            block_points = tuple(symbols[index] for index in block)
            product *= cycle_connected_correlator(block_points, c)
        if product != 0:
            terms.append(product)
    return sp.Add(*terms)


@lru_cache(maxsize=None)
def standard_points(n: int) -> tuple[sp.Symbol, ...]:
    """Canonical coordinate symbols used by the exact evaluators."""

    if not 0 <= n <= MAX_ARITY:
        raise ValueError(f"implemented arity is between 0 and {MAX_ARITY}")
    return tuple(sp.symbols(f"z0:{n}"))


def _exact_value(
    expression: sp.Expr,
    points: tuple[sp.Symbol, ...],
    coordinates: Sequence[object],
    central_charge: object,
) -> sp.Expr:
    values = tuple(sp.sympify(value) for value in coordinates)
    if len(values) != len(points):
        raise ValueError("the number of coordinates equals the arity")
    if len(set(values)) != len(values):
        raise ValueError("configuration-space coordinates are pairwise distinct")
    substitutions = dict(zip(points, values))
    substitutions[CENTRAL_CHARGE] = sp.sympify(central_charge)
    return sp.cancel(expression.subs(substitutions))


def evaluate_ward_correlator(
    coordinates: Sequence[object],
    central_charge: object,
) -> sp.Expr:
    """Evaluate ``G_n`` exactly at pairwise-distinct coordinates."""

    points = standard_points(len(coordinates))
    expression = virasoro_ward_correlator(points, CENTRAL_CHARGE)
    return _exact_value(expression, points, coordinates, central_charge)


def evaluate_connected_correlator(
    coordinates: Sequence[object],
    central_charge: object,
) -> sp.Expr:
    """Evaluate the Möbius-inverted connected correlator exactly."""

    points = standard_points(len(coordinates))
    expression = virasoro_connected_correlator(points, CENTRAL_CHARGE)
    return _exact_value(expression, points, coordinates, central_charge)


def evaluate_cycle_expansion(
    coordinates: Sequence[object],
    central_charge: object,
) -> sp.Expr:
    """Evaluate the independent cycle expansion exactly."""

    points = standard_points(len(coordinates))
    expression = cycle_expansion_correlator(points, CENTRAL_CHARGE)
    return _exact_value(expression, points, coordinates, central_charge)


def require_residue_projection(arity: int) -> None:
    """State the extra datum required for a scalar ``S_arity``."""

    weight_six_scope = f" {WEIGHT_SIX_SCOPE}" if arity == 6 else ""
    raise ResidueProjectionRequired(
        f"S_{arity}: {RESIDUE_PROJECTION_REQUIREMENT}{weight_six_scope}"
    )
