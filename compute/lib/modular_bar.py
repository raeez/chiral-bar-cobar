"""Low-genus modular-bar combinatorics.

This module collects the smallest explicit combinatorial structures used in the
three-preprint chain-level rewrite:

- Mok's codimension formula for planted-forest strata,
- the seven planted-forest boundary types of FM_3,
- the four primitive quartic channels,
- the low-order archetype classifier.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


@dataclass(frozen=True)
class PlantedForestType:
    """Minimal planted-forest data for low-genus bookkeeping.

    Parameters
    ----------
    name:
        Human-readable identifier of the boundary type.
    grid_depths:
        The tuple (w_i) in Mok's codimension formula.
    tree_vertex_counts:
        The tuple (|V(T_{v_j})|) for the rooted planted trees.
    """

    name: str
    grid_depths: Tuple[int, ...]
    tree_vertex_counts: Tuple[int, ...]

    @property
    def codimension(self) -> int:
        return mok_codimension(self.grid_depths, self.tree_vertex_counts)


def mok_codimension(grid_depths: Iterable[int], tree_vertex_counts: Iterable[int]) -> int:
    """Compute Mok's codimension formula.

    codim W_nu = sum_i w_i + sum_j (|V(T_{v_j})| - 1).
    """
    return sum(int(w) for w in grid_depths) + sum(int(v) - 1 for v in tree_vertex_counts)


def fm3_planted_forest_types() -> List[PlantedForestType]:
    """Return the seven boundary types of FM_3 in Mok's language.

    For the smallest explicit model it suffices to encode the codimension data:
    - pair and triple collisions: codimension 1,
    - nested collisions: codimension 2.
    """
    return [
        PlantedForestType("12", (), (2,)),
        PlantedForestType("23", (), (2,)),
        PlantedForestType("13", (), (2,)),
        PlantedForestType("123", (), (2,)),
        PlantedForestType("12<123", (), (3,)),
        PlantedForestType("23<123", (), (3,)),
        PlantedForestType("13<123", (), (3,)),
    ]


def quartic_channels() -> Tuple[str, str, str, str]:
    """The four primitive quartic channels.

    One local contact channel and three one-edge separating channels.
    """
    return ("contact", "12|34", "13|24", "14|23")


def genus_two_shells() -> Tuple[str, str, str]:
    """The three primitive genus-two shells in the log-FM chart.

    They are the first place where the modular theory sees all three kinds of
    geometry at once: iterated loop gluing, mixed separating/non-separating
    gluing, and planted-forest corrections.
    """
    return ("loop-loop", "sep-loop", "planted-forest")


def genus_two_profile(family: str) -> Tuple[str, ...]:
    """Return the surviving genus-two shells for a standard family."""
    family = family.lower()
    if family in {"heisenberg", "free"}:
        return ("loop-loop",)
    if family in {"affine", "affine sl2", "affine sl_2", "current"}:
        return ("loop-loop", "sep-loop")
    if family in {"virasoro", "w_n", "w3", "w_3", "principal w_n"}:
        return genus_two_shells()
    raise KeyError(f"unknown family: {family}")


def shadow_archetype(cubic_nonzero: bool, contact_quartic_nonzero: bool) -> str:
    """Classify the low-order nonlinear behaviour.

    Returns one of:
    - Gaussian
    - Lie/tree
    - Contact/quartic
    - Mixed modular
    """
    if not cubic_nonzero and not contact_quartic_nonzero:
        return "Gaussian"
    if cubic_nonzero and not contact_quartic_nonzero:
        return "Lie/tree"
    if not cubic_nonzero and contact_quartic_nonzero:
        return "Contact/quartic"
    return "Mixed modular"


def standard_family_profiles() -> Dict[str, str]:
    """Return the low-order archetype of the standard families."""
    return {
        "Heisenberg": shadow_archetype(False, False),
        "Free": shadow_archetype(False, False),
        "Affine": shadow_archetype(True, False),
        "beta-gamma": shadow_archetype(False, True),
        "Virasoro": shadow_archetype(True, True),
        "W_N": shadow_archetype(True, True),
    }
