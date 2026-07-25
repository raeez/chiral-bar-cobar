r"""Finite generator screen for the N=2 chiral bar problem.

The module certifies the OPE table and enumerates ordered words in the four
strong generators.  These finite data form an input to a completed
Fulton--MacPherson bar complex.  Cohomology, spectral-sequence collapse, and
quadratic Koszul recognition remain open until the residue maps, descendants,
completion, and convergence theorem are supplied.
"""

from __future__ import annotations

from itertools import product
from math import factorial
from typing import Dict, List, Tuple

import sympy as sp

from compute.lib.n2_superconformal_shadow import n2_nth_products


c = sp.Symbol("c")

GENERATORS = ("T", "J", "G+", "G-")
GEN_WEIGHT = {
    "T": sp.Integer(2),
    "J": sp.Integer(1),
    "G+": sp.Rational(3, 2),
    "G-": sp.Rational(3, 2),
}
GEN_PARITY = {"T": 0, "J": 0, "G+": 1, "G-": 1}


class OpenN2BarCohomologyError(RuntimeError):
    """Raised when the finite generator screen is promoted to cohomology."""


REQUIRED_INPUT = (
    "the completed Fulton--MacPherson residue complex with descendants, "
    "orientation signs, singular-vector quotient, and convergence proof"
)


def n2_ope_data():
    """OPE n-th products, using ``1`` for the vacuum state."""
    converted = {}
    for pair, degrees in n2_nth_products().items():
        converted[pair] = {
            degree: {
                ("1" if state == "vac" else state): coefficient
                for state, coefficient in outputs.items()
            }
            for degree, outputs in degrees.items()
        }
    return converted


def max_pole_order(a: str, b: str) -> int:
    degrees = n2_ope_data().get((a, b), {})
    return max(degrees, default=-1) + 1


def bar_basis_at_weight(n: int, h_total) -> List[Tuple[str, ...]]:
    r"""Ordered generator words of length n and total conformal weight h.

    This is a finite screen.  Descendants and configuration-space forms are
    separate tensor factors in the full bar complex.
    """
    if n < 0:
        raise ValueError("word length must be nonnegative")
    target = sp.Rational(h_total)
    return [
        word
        for word in product(GENERATORS, repeat=n)
        if sum((GEN_WEIGHT[item] for item in word), sp.Rational(0)) == target
    ]


def bar_dim_at_weight(n: int, h_total) -> int:
    """Dimension of the ordered generator-word screen."""
    return len(bar_basis_at_weight(n, h_total))


def ordered_screen_with_os_dimension(n: int, h_total):
    """Record the Orlik--Solomon top-degree dimension separately."""
    word_dimension = bar_dim_at_weight(n, h_total)
    os_top_dimension = factorial(n - 1) if n >= 1 else 1
    return {
        "word_dimension": word_dimension,
        "os_top_dimension": os_top_dimension,
        "tensor_product_upper_bound": word_dimension * os_top_dimension,
        "status": "finite generator/OS screen",
    }


def chiral_bar_status_packet():
    return {
        "status": "open",
        "H2": None,
        "quadratic_koszul": None,
        "required_input": REQUIRED_INPUT,
        "certified_inputs": (
            "standard N=2 OPE table",
            "generator weights and parities",
            "ordered generator-word enumeration",
            "Orlik--Solomon top-degree dimensions",
        ),
    }


def _open():
    raise OpenN2BarCohomologyError(REQUIRED_INPUT)


def ce_differential_matrix(h_total, c_val=None):
    return _open()


def ce_h2_at_weight(h_total, c_val=None):
    return _open()


def chiral_bar_differential_data(h_total, c_val=None):
    return {
        "status": "input packet",
        "weight": sp.Rational(h_total),
        "ope": n2_ope_data(),
        "differential": None,
        "required_input": REQUIRED_INPUT,
    }


def chiral_bar_h2_numerical(c_val: float, max_weight: int = 6) -> Dict:
    return _open()


def _compute_h2_at_weight_simplified(h_total, c_val: float) -> Dict:
    return _open()


def n2_sca_koszulness_analysis(c_val: float = 1.0) -> Dict:
    packet = chiral_bar_status_packet()
    packet.update(
        central_charge=sp.Rational(c_val),
        finite_screens={
            str(weight): {
                degree: bar_dim_at_weight(degree, weight)
                for degree in (1, 2, 3)
            }
            for weight in (
                sp.Integer(1),
                sp.Rational(3, 2),
                sp.Integer(2),
                sp.Rational(5, 2),
                sp.Integer(3),
            )
        },
    )
    return packet


def koszulness_evidence_summary() -> Dict:
    return {
        "status": "open",
        "proved_inputs": [
            "universal OPE presentation",
            "Li/PBW associated-graded generator packet",
            "finite ordered-word screens",
        ],
        "remaining_obligations": [
            "construct the signed residue differential",
            "include descendants and quotient singular vectors",
            "compute the d1 and higher spectral-sequence maps",
            "prove completion and convergence",
        ],
        "quadratic_koszul": None,
    }
