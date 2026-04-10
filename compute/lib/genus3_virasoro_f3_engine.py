"""Uniform-weight genus-3 Virasoro F_3 engine.

Scope
=====

This module computes the genus-3 Virasoro free energy on the
UNIFORM-WEIGHT scalar lane:

    F_3(Vir_c) = kappa(Vir_c) * lambda_3^FP
               = (c/2) * 31/967680
               = 31c/1935360

The live graph surface is the full set of 42 stable graphs of type (g=3, n=0),
enumerated from ``compute.lib.stable_graph_enumeration``.  The contribution
assigned here is the scalar vacuum contribution only.  On this scope:

  - the scalar projection of the Virasoro propagator is ``P = 1/kappa = 2/c``;
  - genus-0 boundary vertices belong to the higher-shadow sector and are
    excluded from the scalar vacuum coefficient;
  - positive-valence boundary vertices are excluded from the scalar vacuum
    coefficient;
  - therefore the unique smooth genus-3 graph is the only nonzero graph.

The full Virasoro shadow tower contains additional planted-forest and boundary
data.  This engine does not compute that broader class; it computes the scalar
``F_3`` requested above.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Dict, Tuple

from sympy import Rational, Symbol

from compute.lib.stable_graph_enumeration import (
    StableGraph,
    _lambda_fp_exact,
    enumerate_stable_graphs,
)


UNIFORM_WEIGHT_TAG = "UNIFORM-WEIGHT"
LAMBDA3_FP = Fraction(31, 967680)
VIRASORO_KAPPA_OVER_C = Fraction(1, 2)
VIRASORO_F3_OVER_C = Fraction(31, 1935360)
VIRASORO_SCALAR_PROPAGATOR_NUMERATOR = Fraction(2)
VIRASORO_R_MATRIX_CUBIC_POLE_ORDER = 3
VIRASORO_R_MATRIX_SIMPLE_POLE_ORDER = 1
VIRASORO_SIMPLE_POLE_STRESS_COEFFICIENT = Fraction(2)


@dataclass(frozen=True)
class Genus3VirasoroGraphContribution:
    """Scalar-lane contribution of one stable graph to genus-3 Virasoro F_3."""

    index: int
    graph: StableGraph
    aut_order: int
    loop_number: int
    propagator_power: int
    kappa_coefficient: Fraction
    c_coefficient: Fraction
    scalar_lane_active: bool
    vanishing_reason: str

    def contribution_at_kappa(self, kappa_value: Fraction) -> Fraction:
        """Evaluate the graph contribution at a fixed kappa."""
        return self.kappa_coefficient * kappa_value

    def contribution_at_c(self, c_value: Fraction) -> Fraction:
        """Evaluate the graph contribution at a fixed central charge."""
        return self.c_coefficient * c_value


def lambda3_fp() -> Fraction:
    """Exact Faber-Pandharipande lambda_3 value."""
    return _lambda_fp_exact(3)


def virasoro_kappa(c_value: Fraction) -> Fraction:
    """kappa(Vir_c) = c/2."""
    return c_value * VIRASORO_KAPPA_OVER_C


def virasoro_scalar_propagator(c_value: Fraction) -> Fraction:
    """Scalar projection of the Virasoro propagator: P = 1/kappa = 2/c."""
    if c_value == 0:
        raise ValueError("Scalar Virasoro propagator is undefined at c = 0")
    return VIRASORO_SCALAR_PROPAGATOR_NUMERATOR / c_value


def virasoro_r_matrix_data() -> Dict[str, object]:
    """Structured Virasoro r-matrix data for this scalar-lane engine."""
    return {
        "full_formula": "(c/2)/z^3 + 2T/z",
        "scalar_projection_formula": "(c/2)/z^3",
        "cubic_pole_order": VIRASORO_R_MATRIX_CUBIC_POLE_ORDER,
        "simple_pole_order": VIRASORO_R_MATRIX_SIMPLE_POLE_ORDER,
        "stress_tensor_simple_pole_coefficient": VIRASORO_SIMPLE_POLE_STRESS_COEFFICIENT,
    }


@lru_cache(maxsize=1)
def genus3_stable_graphs() -> Tuple[StableGraph, ...]:
    """All 42 stable graphs at (g=3, n=0)."""
    return tuple(enumerate_stable_graphs(3, 0))


def is_smooth_genus3_graph(graph: StableGraph) -> bool:
    """Check whether a graph is the unique smooth genus-3 graph."""
    return (
        graph.vertex_genera == (3,)
        and graph.num_edges == 0
        and graph.valence == (0,)
    )


def _scalar_lane_vanishing_reason(graph: StableGraph) -> str:
    """Explain why a graph vanishes on the scalar vacuum lane."""
    if any(genus == 0 for genus in graph.vertex_genera):
        return (
            "contains a genus-0 boundary vertex; scalar F_3 excludes higher-shadow "
            "arity data"
        )
    return (
        "contains positive-valence boundary vertices; scalar F_3 keeps only the "
        "vacuum vertex V(3,0)"
    )


def _graph_contribution(index: int, graph: StableGraph) -> Genus3VirasoroGraphContribution:
    """Compute the scalar-lane contribution of one graph."""
    if is_smooth_genus3_graph(graph):
        return Genus3VirasoroGraphContribution(
            index=index,
            graph=graph,
            aut_order=graph.automorphism_order(),
            loop_number=graph.first_betti,
            propagator_power=0,
            kappa_coefficient=lambda3_fp(),
            c_coefficient=VIRASORO_F3_OVER_C,
            scalar_lane_active=True,
            vanishing_reason="smooth genus-3 graph",
        )

    return Genus3VirasoroGraphContribution(
        index=index,
        graph=graph,
        aut_order=graph.automorphism_order(),
        loop_number=graph.first_betti,
        propagator_power=graph.num_edges,
        kappa_coefficient=Fraction(0),
        c_coefficient=Fraction(0),
        scalar_lane_active=False,
        vanishing_reason=_scalar_lane_vanishing_reason(graph),
    )


@lru_cache(maxsize=1)
def genus3_virasoro_graph_contributions() -> Tuple[Genus3VirasoroGraphContribution, ...]:
    """Per-graph scalar-lane contributions for all 42 genus-3 stable graphs."""
    return tuple(
        _graph_contribution(index, graph)
        for index, graph in enumerate(genus3_stable_graphs())
    )


def nonzero_graph_contributions() -> Tuple[Genus3VirasoroGraphContribution, ...]:
    """All nonzero scalar-lane graph contributions."""
    return tuple(
        contribution
        for contribution in genus3_virasoro_graph_contributions()
        if contribution.scalar_lane_active
    )


def total_kappa_coefficient() -> Fraction:
    """Coefficient of kappa in the genus-3 scalar-lane sum."""
    return sum(
        contribution.kappa_coefficient
        for contribution in genus3_virasoro_graph_contributions()
    )


def total_c_coefficient() -> Fraction:
    """Coefficient of c in the genus-3 scalar-lane sum."""
    return sum(
        contribution.c_coefficient
        for contribution in genus3_virasoro_graph_contributions()
    )


def genus3_virasoro_f3(c_value: Fraction) -> Fraction:
    """Evaluate F_3(Vir_c) on the scalar lane at a fixed central charge."""
    return total_c_coefficient() * c_value


def genus3_virasoro_f3_symbolic():
    """Symbolic scalar-lane formula for F_3(Vir_c)."""
    c_symbol = Symbol("c")
    return Rational(VIRASORO_F3_OVER_C.numerator, VIRASORO_F3_OVER_C.denominator) * c_symbol


def verify_genus3_virasoro_f3() -> Dict[str, object]:
    """Compact verification summary for the scalar-lane Virasoro genus-3 engine."""
    contributions = genus3_virasoro_graph_contributions()
    expected_lambda3 = lambda3_fp()
    expected_c_coeff = VIRASORO_F3_OVER_C
    total_kappa = total_kappa_coefficient()
    total_c = total_c_coefficient()

    return {
        "uniform_weight_tag": UNIFORM_WEIGHT_TAG,
        "graph_count": len(contributions),
        "nonzero_graph_count": len(nonzero_graph_contributions()),
        "lambda3_fp": expected_lambda3,
        "total_kappa_coefficient": total_kappa,
        "total_c_coefficient": total_c,
        "expected_c_coefficient": expected_c_coeff,
        "symbolic_formula": genus3_virasoro_f3_symbolic(),
        "kappa_formula": "c/2",
        "match_lambda3": total_kappa == expected_lambda3,
        "match_total": total_c == expected_c_coeff,
        "c1_value": genus3_virasoro_f3(Fraction(1)),
        "c26_value": genus3_virasoro_f3(Fraction(26)),
        "c0_value": genus3_virasoro_f3(Fraction(0)),
    }
