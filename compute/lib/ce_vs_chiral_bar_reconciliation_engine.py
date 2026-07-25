r"""Typed comparison surface for mode CE complexes and ordered chiral bar.

A negative-mode Lie (super)algebra, an Orlik--Solomon vector space, and an
ordered chiral bar complex are three distinct objects.  A PBW filtration may
relate them through a spectral sequence after its filtration, differential,
completion, convergence, and edge morphism have been constructed.  This
module records exact finite inputs and keeps each comparison theorem open.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Dict, Mapping, Tuple

import sympy as sp

from compute.lib.bar_cohomology_n2sca_explicit_engine import (
    SuperCEComplex,
    bracket as n2_bracket,
)
from compute.lib.shadow_tower_extended_families import w3_ope_packet


H_CE = (
    "H_CE: a continuous completed CE complex with fixed super-sign and topology conventions"
)
H_BAR = (
    "H_bar: the ordered Fulton--MacPherson residue complex with its full signed differential"
)
H_PBW = (
    "H_PBW: a complete separated PBW filtration, identified pages, convergence, and edge map"
)
H_OS = (
    "H_OS: an explicit chain map incorporating Arnold forms and their residue differential"
)
H_RES = (
    "H_res: a minimal chiral resolution and a comparison quasi-isomorphism"
)


class OpenCEBarComparisonError(RuntimeError):
    """Signals that finite input data have reached the comparison boundary."""


@dataclass(frozen=True)
class ClaimPacket:
    statement: str
    status: str
    value: object | None = None
    hypotheses: Tuple[str, ...] = ()


@dataclass(frozen=True)
class ComparisonPacket:
    family: str
    exact_inputs: Mapping[str, object]
    ce_cohomology: ClaimPacket
    chiral_bar_cohomology: ClaimPacket
    comparison: ClaimPacket


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, tuple(hypotheses))


def _comparison_error(statement: str) -> OpenCEBarComparisonError:
    return OpenCEBarComparisonError(f"{statement} awaits {H_CE}, {H_BAR}, and {H_PBW}.")


# ---------------------------------------------------------------------------
# Exact Witt negative-mode presentation and chain spaces
# ---------------------------------------------------------------------------


def witt_negative_mode_bracket(m: int, n: int) -> Mapping[int, int]:
    r"""Return ``[L_-m,L_-n]=(n-m)L_-(m+n)`` for ``m,n>=2``."""

    if m < 2 or n < 2:
        raise ValueError("Vacuum-creating Witt modes have indices m,n >= 2.")
    coefficient = n - m
    return {} if coefficient == 0 else {m + n: coefficient}


def witt_ce_chain_dimensions(max_weight: int = 12) -> Mapping[Tuple[int, int], int]:
    """Return exact exterior-chain dimensions for ``span{L_-n:n>=2}``."""

    dimensions: Dict[Tuple[int, int], int] = {(0, 0): 1}

    def choose(target: int, degree: int, start: int, remaining: int) -> int:
        if remaining == 0:
            return int(target == 0)
        total = 0
        for weight in range(start, target + 1):
            total += choose(target - weight, degree + 1, weight + 1, remaining - 1)
        return total

    for weight in range(2, max_weight + 1):
        for degree in range(1, weight // 2 + 1):
            value = choose(weight, 0, 2, degree)
            if value:
                dimensions[(degree, weight)] = value
    return dimensions


def witt_ce_dimensions(max_weight: int = 12):
    """Historical cohomology API; the continuous CE theorem remains open."""

    raise _comparison_error("Witt continuous CE cohomology")


def virasoro_bar_dimensions_known(max_weight: int = 12):
    """Historical bar-dimension API; a residue-bar computation is required."""

    raise _comparison_error("Virasoro ordered bar cohomology")


def reconcile_virasoro(max_weight: int = 12) -> ComparisonPacket:
    """Return exact Witt chain inputs and the typed Virasoro comparison."""

    return ComparisonPacket(
        family="Virasoro",
        exact_inputs={
            "negative_mode_bracket": "[L_-m,L_-n]=(n-m)L_-(m+n)",
            "ce_chain_dimensions": witt_ce_chain_dimensions(max_weight),
            "TT_OPE": "c/2, 2T, dT",
        },
        ce_cohomology=_open("continuous Witt negative-mode CE cohomology", H_CE),
        chiral_bar_cohomology=_open("ordered Virasoro chiral bar cohomology", H_BAR),
        comparison=_open("Virasoro CE-to-bar quasi-isomorphism", H_CE, H_BAR, H_PBW),
    )


# ---------------------------------------------------------------------------
# W_3: the nonlinear WW channel blocks a linear strong-generator CE model
# ---------------------------------------------------------------------------


def w3_negative_mode_bracket(max_weight: int = 8) -> Mapping[str, object]:
    """Return the exact linear ``LL``/``LW`` packet and nonlinear ``WW`` input."""

    generators = []
    linear_brackets: Dict[Tuple[str, str], Mapping[str, int]] = {}
    for weight in range(2, max_weight + 1):
        generators.append(f"L_{-weight}")
        if weight >= 3:
            generators.append(f"W_{-weight}")

    for m in range(2, max_weight + 1):
        for n in range(2, max_weight + 1):
            if m + n <= max_weight and m != n:
                linear_brackets[(f"L_{-m}", f"L_{-n}")] = {
                    f"L_{-(m+n)}": n - m
                }
        for n in range(3, max_weight + 1):
            if m + n <= max_weight:
                coefficient = n - 2 * m
                if coefficient:
                    linear_brackets[(f"L_{-m}", f"W_{-n}")] = {
                        f"W_{-(m+n)}": coefficient
                    }

    c = sp.Symbol("c")
    return {
        "status": "exact linear action plus nonlinear WW channel",
        "generators": tuple(generators),
        "linear_brackets": linear_brackets,
        "WW_OPE": w3_ope_packet(c)["WW"],
        "linear_ce_model": _open(
            "a CE model for the nonlinear W_3 mode algebra",
            H_CE,
            H_PBW,
        ),
    }


def w3_ce_leading_pole(max_weight: int = 6):
    raise _comparison_error("W_3 CE cohomology from its nonlinear mode algebra")


def w3_bar_dimensions_known(max_weight: int = 8):
    raise _comparison_error("W_3 ordered bar cohomology")


def reconcile_w3_at_weight_4(max_weight: int = 6) -> ComparisonPacket:
    """Return the exact W3 OPE input and open weight-four comparison."""

    c = sp.Symbol("c")
    packet = w3_ope_packet(c)
    return ComparisonPacket(
        family="W_3 at conformal weight four",
        exact_inputs={
            "WW_to_Lambda": packet["WW"][1]["Lambda"],
            "WW_to_dLambda": packet["WW"][0]["dLambda"],
            "N_Lambda": c * (5 * c + 22) / 10,
        },
        ce_cohomology=_open("weight-four nonlinear-mode CE cohomology", H_CE),
        chiral_bar_cohomology=_open("weight-four W_3 ordered bar cohomology", H_BAR),
        comparison=_open("weight-four PBW differential and edge map", H_CE, H_BAR, H_PBW),
    )


# ---------------------------------------------------------------------------
# N=2: exact CE chain spaces, open continuous cohomology and bar comparison
# ---------------------------------------------------------------------------


def n2sca_super_ce_chain_table(max_wh: int = 12) -> Mapping[Tuple[int, Fraction], int]:
    """Return exact truncated N=2 CE chain dimensions."""

    ce = SuperCEComplex(max_wh)
    table: Dict[Tuple[int, Fraction], int] = {}
    for weight_half in range(max_wh + 1):
        for degree in range(weight_half + 1):
            dimension = ce.chain_dim(degree, weight_half)
            if dimension:
                table[(degree, Fraction(weight_half, 2))] = dimension
    return table


def n2sca_super_ce_table(max_wh: int = 12):
    raise _comparison_error("N=2 continuous CE cohomology")


def n2sca_h2_classes(max_wh: int = 10) -> ClaimPacket:
    return _open("N=2 continuous CE H^2 classes", H_CE)


def n2sca_subleading_d2_kills_h2(max_wh: int = 10) -> ClaimPacket:
    return _open(
        "N=2 PBW differentials acting on candidate CE H^2 classes",
        H_CE,
        H_BAR,
        H_PBW,
    )


def reconcile_n2(max_wh: int = 10) -> ComparisonPacket:
    """Return exact N=2 mode inputs and the open CE/bar comparison."""

    example = n2_bracket(("G+", Fraction(-3, 2)), ("G-", Fraction(-5, 2)))
    return ComparisonPacket(
        family="N=2 superconformal",
        exact_inputs={
            "sample_G+G-_bracket": example,
            "ce_chain_dimensions": n2sca_super_ce_chain_table(max_wh),
        },
        ce_cohomology=_open("continuous N=2 negative-mode CE cohomology", H_CE),
        chiral_bar_cohomology=_open("ordered N=2 chiral bar cohomology", H_BAR),
        comparison=_open("N=2 CE-to-bar PBW comparison", H_CE, H_BAR, H_PBW),
    )


# ---------------------------------------------------------------------------
# Arnold-form dimensions and comparison frontiers
# ---------------------------------------------------------------------------


def os_dimension(n: int) -> int:
    r"""Return ``dim OS^{n-1}(Conf_n(C))=(n-1)!``."""

    if n < 1:
        raise ValueError("Configuration cardinality n is positive.")
    return factorial(n - 1)


def sl2_ce_vs_bar_with_os(max_weight: int = 8) -> ComparisonPacket:
    """Record exact Arnold top-degree dimensions and the open sl2 comparison."""

    return ComparisonPacket(
        family="affine sl_2",
        exact_inputs={"OS_top_dimensions": {n: os_dimension(n) for n in range(1, 7)}},
        ce_cohomology=_open("continuous affine negative-mode CE cohomology", H_CE),
        chiral_bar_cohomology=_open("ordered affine sl_2 chiral bar cohomology", H_BAR),
        comparison=_open("Arnold-form enhanced CE/bar comparison", H_CE, H_BAR, H_PBW, H_OS),
    )


def poincare_duality_check_virasoro(max_weight: int = 14) -> ClaimPacket:
    return _open("a duality theorem for completed Virasoro bar cohomology", H_BAR)


def poincare_duality_check_sl2(max_weight: int = 6) -> ClaimPacket:
    return _open("a duality theorem for completed affine sl_2 bar cohomology", H_BAR)


def w3_pbw_ss_pages(max_weight: int = 6) -> ClaimPacket:
    return _open("identified W_3 PBW spectral-sequence pages", H_CE, H_BAR, H_PBW)


def minimal_resolution_dimensions_virasoro(max_n: int = 6) -> ClaimPacket:
    return _open("minimal Virasoro chiral-resolution dimensions", H_RES)


def minimal_resolution_dimensions_ce_witt(max_n: int = 6) -> ClaimPacket:
    return _open("minimal continuous Witt CE-resolution dimensions", H_CE, H_RES)


def compare_resolutions_virasoro(max_n: int = 6) -> ClaimPacket:
    return _open("Virasoro chiral/CE resolution comparison", H_CE, H_BAR, H_RES)


def reconciliation_report(max_weight: int = 8) -> Mapping[str, object]:
    """Return the exact-input/open-comparison ledger for the four test families."""

    return {
        "Virasoro": reconcile_virasoro(max_weight),
        "W3": reconcile_w3_at_weight_4(max_weight),
        "N2": reconcile_n2(2 * max_weight),
        "sl2": sl2_ce_vs_bar_with_os(max_weight),
        "status": "finite presentations exact; comparison theorems open",
    }
