"""Normalization bridge for non-principal DS central-charge conventions.

The current BP seed implementation carries two distinct convention layers:

  - raw formula bundle (as currently encoded): c(k) + c(k') = 196;
  - chapter proposition normalization target: c(k) + c(k') = 22.

This module makes that discrepancy explicit and computable, rather than
silently baking one convention into frontier checks.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.nonprincipal_ds_reduction import (
    bp_central_charge,
    bp_complementarity_constant,
    bp_dual_level,
)


@dataclass(frozen=True)
class CentralChargeConvention:
    """Affine central-charge convention c -> a*c + b."""

    name: str
    scale: object
    shift: object

    def apply(self, c_expr):
        c = sympify(c_expr)
        return simplify(self.scale * c + self.shift)


RAW_BP_CONVENTION = CentralChargeConvention(
    name="bp_raw_formula_bundle",
    scale=Rational(1),
    shift=Rational(0),
)

CHAPTER_BP_SUM_CONVENTION = CentralChargeConvention(
    name="bp_chapter_sum22_shift_only_bridge",
    scale=Rational(1),
    shift=Rational(-87),
)


def bp_dual_sum_under_convention(
    convention: CentralChargeConvention,
    level=Symbol("k"),
):
    """Compute c_conv(k) + c_conv(k') under a chosen convention."""
    k = sympify(level)
    kp = bp_dual_level(k)
    c_k = convention.apply(bp_central_charge(k))
    c_kp = convention.apply(bp_central_charge(kp))
    return simplify(c_k + c_kp)


def shift_to_target_dual_sum(raw_sum, target_sum):
    """Affine shift delta with scale=1 so that (c+delta)+(c'+delta)=target."""
    raw = sympify(raw_sum)
    target = sympify(target_sum)
    return simplify((target - raw) / 2)


def bp_shift_to_target_sum(target_sum=22):
    """Shift required to move the current raw BP sum to `target_sum`."""
    return shift_to_target_dual_sum(bp_complementarity_constant(), target_sum)


def bp_shifted_convention_for_target(target_sum=22) -> CentralChargeConvention:
    """Convenience constructor for a shift-only target-sum convention."""
    return CentralChargeConvention(
        name=f"bp_shifted_to_sum_{target_sum}",
        scale=Rational(1),
        shift=bp_shift_to_target_sum(target_sum),
    )


def verify_nonprincipal_ds_normalization(level=Symbol("k")) -> Dict[str, bool]:
    """Checks for raw and bridged BP normalization layers."""
    k = sympify(level)
    results: Dict[str, bool] = {}

    raw_sum = bp_dual_sum_under_convention(RAW_BP_CONVENTION, k)
    results["raw BP convention gives sum 196"] = (simplify(raw_sum - 196) == 0)

    shift = bp_shift_to_target_sum(22)
    results["required shift to target 22 is -87"] = (simplify(shift + 87) == 0)

    chapter_conv = bp_shifted_convention_for_target(22)
    chapter_sum = bp_dual_sum_under_convention(chapter_conv, k)
    results["shifted BP convention gives sum 22"] = (simplify(chapter_sum - 22) == 0)

    # Check equivalence to the explicit bridge constant.
    explicit_sum = bp_dual_sum_under_convention(CHAPTER_BP_SUM_CONVENTION, k)
    results["explicit chapter bridge matches computed shift"] = (
        simplify(explicit_sum - chapter_sum) == 0
    )

    return results
