"""Non-principal DS reduction seed data.

This module adds the next scaffold layer above orbit combinatorics:
  - the proved sl_3 subregular (Bershadsky-Polyakov) seed invariants;
  - the good-grading and generator-presentation data for that seed case;
  - hook-pair seed records for the first genuinely non-self-dual type-A case.

Scope discipline:
  - principal finite-type PBW statements remain in the principal modules;
  - non-principal results here are tagged as proved/evidence/programme.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.bv_duality import first_nonselfdual_type_a_hook_pair
from compute.lib.nonprincipal_ds_orbits import (
    STATUS_HOOK_EVIDENCE,
    STATUS_PROVED_SUBREGULAR_SL3,
    STATUS_PROGRAMME,
    TRACK_FRONTIER_NONPRINCIPAL,
    Partition,
    nonprincipal_hook_case,
)


@dataclass(frozen=True)
class NonprincipalDSSeed:
    """Frontier seed record for non-principal DS orbit reductions."""

    lie_type: str
    rank: int
    partition: Partition
    dual_partition: Partition
    level_shift: object
    central_charge: object
    complementarity_sum: object
    track: str
    status: str


GeneratorPresentation = Tuple[Tuple[str, object, str], ...]


def bp_dual_level(level=Symbol("k")):
    """Dual level for the sl_3 subregular/Bershadsky-Polyakov seed case."""
    k = sympify(level)
    return -k - 6


def bp_residual_sl2_level(level=Symbol("k")):
    """Residual affine sl_2 level in the subregular sl_3 reduction."""
    k = sympify(level)
    return k + Rational(1, 2)


def bp_residual_sl2_dual_relation(level=Symbol("k")):
    """Residual-level relation induced by the ambient duality k -> -k-6."""
    k = sympify(level)
    lhs = bp_residual_sl2_level(bp_dual_level(k))
    rhs = -bp_residual_sl2_level(k) - 5
    return simplify(lhs - rhs)


def bp_central_charge(level=Symbol("k")):
    """Bershadsky-Polyakov central charge from the sl_3 subregular proposition."""
    k = sympify(level)
    if k + 3 == 0:
        raise ValueError("Bershadsky-Polyakov central charge undefined at k = -3")
    return 2 - 3 * (2 * k + 3) ** 2 / (k + 3)


def bp_complementarity_sum(level=Symbol("k")):
    """Complementarity sum c(k) + c(k') for k' = -k-6."""
    k = sympify(level)
    kp = bp_dual_level(k)
    return simplify(bp_central_charge(k) + bp_central_charge(kp))


def bp_complementarity_constant():
    """Constant value of c(k)+c(k') for the current BP formula bundle."""
    k = Symbol("k")
    return simplify(bp_complementarity_sum(k))


def bp_curvature_proxy(level=Symbol("k")):
    """Curvature proxy used in the manuscript consistency check."""
    k = sympify(level)
    return Rational(1, 2) * (k + Rational(1, 2))


def bp_curvature_dual_relation(level=Symbol("k")):
    """Check m_0(k') = -m_0(k) - 5/2 for the proxy curvature."""
    k = sympify(level)
    lhs = bp_curvature_proxy(bp_dual_level(k))
    rhs = -bp_curvature_proxy(k) - Rational(5, 2)
    return simplify(lhs - rhs)


def sl3_subregular_good_grading_multiplicities() -> Dict[int, int]:
    """ad(h)-grading multiplicities for the minimal sl_3 sl_2-triple."""
    return {-2: 1, -1: 2, 0: 2, 1: 2, 2: 1}


def bp_current_presentation() -> GeneratorPresentation:
    """Current-algebra presentation used in the DS hierarchy computation."""
    return (
        ("J1", 1, "bosonic"),
        ("J2", 1, "bosonic"),
        ("J3", 1, "bosonic"),
        ("G+", Rational(3, 2), "fermionic"),
        ("G-", Rational(3, 2), "fermionic"),
    )


def bp_strong_presentation() -> GeneratorPresentation:
    """Strong generating set used in the manuscript's BP algebra example."""
    return (
        ("J", 1, "bosonic"),
        ("G+", Rational(3, 2), "fermionic"),
        ("G-", Rational(3, 2), "fermionic"),
        ("T", 2, "bosonic"),
    )


def sl3_subregular_bp_seed(level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for the proved sl_3 subregular case."""
    k = sympify(level)
    return NonprincipalDSSeed(
        lie_type="A",
        rank=2,
        partition=(2, 1),
        dual_partition=(2, 1),
        level_shift=bp_dual_level(k),
        central_charge=bp_central_charge(k),
        complementarity_sum=bp_complementarity_constant(),
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=STATUS_PROVED_SUBREGULAR_SL3,
    )


def first_nonselfdual_hook_seed(level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for the first non-self-dual type-A hook pair (A3)."""
    n, r, pair = first_nonselfdual_type_a_hook_pair()
    hook_case = nonprincipal_hook_case(n, r, level=level)
    status = (
        STATUS_HOOK_EVIDENCE
        if hook_case.status == STATUS_HOOK_EVIDENCE
        else STATUS_PROGRAMME
    )
    return NonprincipalDSSeed(
        lie_type=pair.source_type,
        rank=pair.source_rank,
        partition=pair.source_orbit,
        dual_partition=pair.target_orbit,
        level_shift=hook_case.level_shift,
        central_charge=Symbol("unknown_nonprincipal_hook_c"),
        complementarity_sum=Symbol("unknown_nonprincipal_hook_sum"),
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=status,
    )


def verify_nonprincipal_ds_reduction_seed(level=Symbol("k")) -> Dict[str, bool]:
    """Sanity checks for the DS reduction seed layer."""
    k = sympify(level)
    results: Dict[str, bool] = {}

    bp = sl3_subregular_bp_seed(k)
    results["sl3 subregular partition self-dual"] = (bp.partition == bp.dual_partition == (2, 1))
    results["sl3 subregular shift is involutive"] = (simplify(bp_dual_level(bp.level_shift) - k) == 0)
    results["sl3 subregular c+c' is k-independent"] = (
        simplify(bp_complementarity_sum(k) - bp_complementarity_constant()) == 0
    )
    results["sl3 subregular c+c' (current formula bundle) = 76"] = (
        simplify(bp.complementarity_sum - 76) == 0
    )
    results["sl3 subregular residual sl2 dual relation"] = (
        bp_residual_sl2_dual_relation(k) == 0
    )
    results["sl3 subregular curvature proxy dual relation"] = (
        bp_curvature_dual_relation(k) == 0
    )
    results["sl3 subregular status tag"] = (bp.status == STATUS_PROVED_SUBREGULAR_SL3)
    results["sl3 subregular frontier track"] = (bp.track == TRACK_FRONTIER_NONPRINCIPAL)
    grading = sl3_subregular_good_grading_multiplicities()
    results["sl3 subregular good grading sums to dim sl3"] = (sum(grading.values()) == 8)
    results["sl3 subregular good grading symmetric"] = all(
        grading[d] == grading[-d] for d in grading if -d in grading
    )
    results["sl3 subregular current presentation weights"] = (
        tuple(weight for _, weight, _ in bp_current_presentation())
        == (1, 1, 1, Rational(3, 2), Rational(3, 2))
    )
    results["sl3 subregular strong presentation weights"] = (
        tuple(weight for _, weight, _ in bp_strong_presentation())
        == (1, Rational(3, 2), Rational(3, 2), 2)
    )

    hook = first_nonselfdual_hook_seed(k)
    results["first non-self-dual hook partition"] = (
        hook.partition == (3, 1) and hook.dual_partition == (2, 1, 1)
    )
    results["first non-self-dual hook status/evidence"] = (hook.status == STATUS_HOOK_EVIDENCE)
    results["first non-self-dual hook frontier track"] = (hook.track == TRACK_FRONTIER_NONPRINCIPAL)

    return results
