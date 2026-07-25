r"""Exact W3 PBW/OPE inputs and the open bar-cohomology calculation."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Mapping, Tuple

import sympy as sp

from compute.lib.w3_bar import w3_central_charge
from compute.lib.w3_bar_extended import (
    ClaimPacket,
    H_BAR,
    W3VacuumModule,
    dim_vbar,
    dim_vbar_gf,
    ordered_top_form_chain_dim,
    verify_mu_generators,
)


class OpenW3BarCohomologyError(RuntimeError):
    """Signals that PBW/OPE data have reached the cohomology boundary."""


def _open(statement: str) -> ClaimPacket:
    return ClaimPacket(statement, "open", None, (H_BAR,))


def _cohomology_error(statement: str):
    return OpenW3BarCohomologyError(f"{statement} awaits {H_BAR}.")


def w3_bar_dims(max_n: int = 20) -> List[int]:
    raise _cohomology_error("W3 bar-cohomology dimensions")


def virasoro_bar_dims(max_n: int = 20) -> List[int]:
    raise _cohomology_error("Virasoro bar-cohomology dimensions")


def w3_gf_from_formula(max_n: int = 20) -> List[int]:
    raise _cohomology_error("The proposed W3 bar generating function")


def _motzkin_numbers(N: int) -> List[int]:
    """Return the combinatorial Motzkin sequence, with no bar interpretation."""

    values = [0] * N
    if N:
        values[0] = 1
    if N > 1:
        values[1] = 1
    for n in range(2, N):
        values[n] = values[n - 1] + sum(values[k] * values[n - 2 - k] for k in range(n - 1))
    return values


def w3_vacuum_dims(max_h: int = 20) -> Dict[int, int]:
    return dim_vbar_gf(max_h)


def bar_chain_dim(bar_degree: int, weight: int) -> int:
    """Return the raw arity/top-Arnold-form chain count."""

    return ordered_top_form_chain_dim(bar_degree, weight)


def verify_ope_data(c_val=7) -> Dict[str, bool]:
    return verify_mu_generators(c_val, verbose=False)


def verify_curvature_complementarity() -> Mapping[str, object]:
    k = sp.Symbol("k")
    return {
        "formal_reflected_central_sum": sp.simplify(w3_central_charge(k) + w3_central_charge(-k - 6)),
        "leading_norm_ratio": sp.Rational(2, 3),
        "bar_curvature": _open("W3 bar curvature"),
        "modular_conductor": ClaimPacket("W3 modular conductor", "open", None, ("H_W3^mod", H_BAR)),
    }


class W3BarCohomologyEngine:
    """Ledger of exact finite inputs and open W3 bar outputs."""

    def __init__(self, max_n: int = 8, max_h: int = 20, c_val=7):
        self.max_n = max_n
        self.max_h = max_h
        self.c_val = c_val
        self.vacuum_dimensions = w3_vacuum_dims(max_h)
        self.raw_chain_dimensions = {
            (arity, weight): value
            for arity in range(1, max_n + 1)
            for weight in range(max_h + 1)
            if (value := bar_chain_dim(arity, weight))
        }
        self.ope_checks = verify_ope_data(c_val)
        self.bar_differential = _open("W3 ordered bar differential")
        self.cohomology = _open("W3 ordered bar cohomology")
        self.koszulness = ClaimPacket("W3 chiral Koszulness", "open", None, (H_BAR, "H_W3^PBW"))

    def summary(self) -> Mapping[str, object]:
        return {
            "vacuum_dimensions": self.vacuum_dimensions,
            "raw_chain_dimensions": self.raw_chain_dimensions,
            "ope_checks": self.ope_checks,
            "bar_differential": self.bar_differential,
            "cohomology": self.cohomology,
            "koszulness": self.koszulness,
        }
