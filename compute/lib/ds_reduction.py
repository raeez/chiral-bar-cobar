"""Chain-level seed scaffold for non-principal Drinfeld-Sokolov reduction.

Current scope is intentionally narrow: the sl_3 subregular orbit seed used by
the non-principal frontier. This module does not compute BRST cohomology; it
records the structural inputs needed to launch that computation cleanly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import Rational, Symbol, sympify

from compute.lib.nonprincipal_ds_orbits import (
    TRACK_FRONTIER_NONPRINCIPAL,
    subregular_partition,
    type_a_orbit_class,
)
from compute.lib.nonprincipal_ds_reduction import bp_dual_level


@dataclass(frozen=True)
class Sl2TripleSeed:
    """Symbolic sl_2-triple data inside a Lie algebra."""

    e: str
    h: str
    f: str


@dataclass(frozen=True)
class DSGhostWeight:
    """BRST ghost conformal-weight data for one graded root direction."""

    root_label: str
    ad_h_grade: Rational
    b_weight: Rational
    c_weight: Rational


@dataclass(frozen=True)
class DSReductionSeed:
    """Frontier DS reduction seed record."""

    lie_type: str
    rank: int
    partition: Tuple[int, ...]
    sl2_triple: Sl2TripleSeed
    positive_grades: Tuple[DSGhostWeight, ...]
    dual_level: object
    expected_target: str
    track: str
    status: str


STATUS_DS_SEED = "nonprincipal_ds_seed"


def brst_ghost_weights(ad_h_grade) -> Tuple[Rational, Rational]:
    """Ghost conformal weights from DS grading."""
    grade = sympify(ad_h_grade)
    return (Rational(1) + grade / 2, -grade / 2)


def sl3_subregular_sl2_triple() -> Sl2TripleSeed:
    """Standard symbolic triple for the sl_3 subregular seed."""
    return Sl2TripleSeed(e="E12", h="H1", f="F12")


def sl3_subregular_positive_grades() -> Dict[str, Rational]:
    """Positive ad(h)-grades used by the subregular DS seed."""
    # For h = H1: alpha1 has grade 2, alpha1+alpha2 has grade 1.
    return {
        "alpha1": Rational(2),
        "alpha1+alpha2": Rational(1),
    }


def sl3_subregular_ghost_profile() -> Tuple[DSGhostWeight, ...]:
    """Ghost profile for the positive-graded root directions."""
    profile = []
    for root, grade in sl3_subregular_positive_grades().items():
        b_weight, c_weight = brst_ghost_weights(grade)
        profile.append(
            DSGhostWeight(
                root_label=root,
                ad_h_grade=grade,
                b_weight=b_weight,
                c_weight=c_weight,
            )
        )
    return tuple(profile)


def sl3_subregular_ds_seed(level=Symbol("k")) -> DSReductionSeed:
    """Seed DS record for the non-principal sl_3 subregular case."""
    k = sympify(level)
    return DSReductionSeed(
        lie_type="A",
        rank=2,
        partition=subregular_partition(3),
        sl2_triple=sl3_subregular_sl2_triple(),
        positive_grades=sl3_subregular_ghost_profile(),
        dual_level=bp_dual_level(k),
        expected_target="affine_sl2_seed",
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=STATUS_DS_SEED,
    )


def verify_ds_reduction_seed(level=Symbol("k")) -> Dict[str, bool]:
    """Consistency checks for the DS seed scaffold."""
    k = sympify(level)
    seed = sl3_subregular_ds_seed(k)
    results: Dict[str, bool] = {}

    results["seed orbit is subregular"] = (type_a_orbit_class(seed.partition) == "subregular")
    results["seed sl2 triple labels"] = (
        seed.sl2_triple.e == "E12"
        and seed.sl2_triple.h == "H1"
        and seed.sl2_triple.f == "F12"
    )
    results["seed dual level formula"] = (seed.dual_level == -k - 6)
    results["seed has positive grades only"] = all(item.ad_h_grade > 0 for item in seed.positive_grades)
    results["ghost weight balance b+c=1"] = all(
        (item.b_weight + item.c_weight) == 1 for item in seed.positive_grades
    )
    results["ghost profile roots expected"] = (
        {item.root_label for item in seed.positive_grades} == {"alpha1", "alpha1+alpha2"}
    )
    results["seed frontier track"] = (seed.track == TRACK_FRONTIER_NONPRINCIPAL)
    results["seed status tag"] = (seed.status == STATUS_DS_SEED)

    return results
