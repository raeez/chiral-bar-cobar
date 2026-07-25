r"""Weight bookkeeping for the open N=2 chiral bar spectral sequence.

The n-th product of homogeneous fields has conformal weight
``h(a)+h(b)-n-1``.  This module verifies that bookkeeping from the exact
OPE table.  It does not manufacture the differentials on later pages of a
PBW/Li spectral sequence: those require filtered chain maps and convergence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import sympy as sp

from compute.lib.n2_sca_chiral_bar_engine import GEN_PARITY, GEN_WEIGHT
from compute.lib.n2_superconformal_shadow import n2_nth_product


class OpenWeightGradedBarError(RuntimeError):
    """Raised when OPE weight bookkeeping is promoted to bar cohomology."""


REQUIRED_INPUT = (
    "a filtered completed chiral bar complex, explicit residue differential, "
    "induced higher-page maps, and spectral-sequence convergence"
)


def nth_product_output_weight(a: str, b: str, n: int):
    return sp.simplify(GEN_WEIGHT[a] + GEN_WEIGHT[b] - n - 1)


def mode_1_product(a, b):
    """Exact first product a_(1)b from the standard OPE table."""
    return n2_nth_product(a, b, 1)


def mode_1_product_weight_shift():
    """Weight checks for every nonzero first product."""
    checks = {}
    for a in GEN_WEIGHT:
        for b in GEN_WEIGHT:
            output = mode_1_product(a, b)
            if output:
                checks[(a, b)] = {
                    "expected_output_weight": nth_product_output_weight(a, b, 1),
                    "output": output,
                }
    return checks


@dataclass(frozen=True)
class ChiralBarN2SCA:
    """Typed handle for a proposed filtered N=2 chiral bar complex."""

    central_charge: object = sp.Symbol("c")
    max_weight_half: int = 8

    def status(self) -> Dict[str, object]:
        return {
            "status": "open",
            "central_charge": self.central_charge,
            "max_weight_half": self.max_weight_half,
            "H2": None,
            "quadratic_koszul": None,
            "required_input": REQUIRED_INPUT,
        }

    def h2_at_weight(self, weight_half: int):
        raise OpenWeightGradedBarError(REQUIRED_INPUT)


def analyze_mode1_correction(ce_data: Dict, ce_complex=None) -> Dict:
    """Describe the missing filtered comparison instead of inventing d1."""
    return {
        "status": "open filtered comparison",
        "input_ce_data": ce_data,
        "mode_1_products": mode_1_product_weight_shift(),
        "induced_spectral_sequence_map": None,
        "required_input": REQUIRED_INPUT,
    }


def n2_sca_h2_analysis(max_weight_half: int = 8, c_val=None) -> Dict:
    handle = ChiralBarN2SCA(
        central_charge=sp.Symbol("c") if c_val is None else sp.sympify(c_val),
        max_weight_half=max_weight_half,
    )
    packet = handle.status()
    packet["mode_1_weight_checks"] = mode_1_product_weight_shift()
    return packet


def n2_sca_chiral_bar_h2_at_weight3() -> Dict:
    return {
        "status": "open",
        "conformal_weight": sp.Integer(3),
        "half_weight": 6,
        "H2": None,
        "required_input": REQUIRED_INPUT,
    }
