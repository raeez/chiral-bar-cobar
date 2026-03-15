"""Barbasch-Vogan duality scaffold for nilpotent orbits.

Current scope:
  - exact type-A implementation via partition transpose;
  - hook-family utilities for the non-principal DS frontier;
  - first non-self-dual hook pair locator (type A).

This module is orbit-combinatorial only: it does not implement BRST/DS
cohomology, OPE data, or level corrections beyond the existing ansatz layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    hook_partition,
    normalize_partition,
    transpose_partition,
)


@dataclass(frozen=True)
class BVDualOrbit:
    """Small record for a Barbasch-Vogan dual orbit pair."""

    source_type: str
    source_rank: int
    source_orbit: Partition
    target_type: str
    target_rank: int
    target_orbit: Partition
    is_self_dual: bool
    status: str


STATUS_EXACT_TYPE_A = "exact_type_a_transpose"
STATUS_HOOK_FRONTIER = "hook_frontier_seed"


def type_a_bv_dual(partition: Iterable[int]) -> Partition:
    """BV dual in type A via partition transpose."""
    return transpose_partition(partition)


def is_type_a_self_dual_orbit(partition: Iterable[int]) -> bool:
    """Check whether a type-A orbit is self-BV-dual."""
    lam = normalize_partition(partition)
    return type_a_bv_dual(lam) == lam


def type_a_bv_pair(n: int, partition: Iterable[int]) -> BVDualOrbit:
    """Build a BV dual pair record in type A_{n-1}."""
    lam = normalize_partition(partition)
    if sum(lam) != n:
        raise ValueError("partition size must equal n")
    dual = type_a_bv_dual(lam)
    return BVDualOrbit(
        source_type="A",
        source_rank=n - 1,
        source_orbit=lam,
        target_type="A",
        target_rank=n - 1,
        target_orbit=dual,
        is_self_dual=(lam == dual),
        status=STATUS_EXACT_TYPE_A,
    )


def type_a_hook_bv_pair(n: int, r: int) -> BVDualOrbit:
    """BV pair for the hook orbit (n-r,1^r) in type A."""
    if not (1 <= r <= n - 2):
        raise ValueError("non-principal hook requires 1 <= r <= n-2")
    hook = hook_partition(n, r)
    dual = type_a_bv_dual(hook)
    return BVDualOrbit(
        source_type="A",
        source_rank=n - 1,
        source_orbit=hook,
        target_type="A",
        target_rank=n - 1,
        target_orbit=dual,
        is_self_dual=(hook == dual),
        status=STATUS_HOOK_FRONTIER,
    )


def first_nonselfdual_type_a_hook_pair(max_n: int = 12) -> Tuple[int, int, BVDualOrbit]:
    """Find the first non-self-dual non-principal hook pair in type A."""
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            if r > n - 2:
                continue
            pair = type_a_hook_bv_pair(n, r)
            if not pair.is_self_dual:
                return n, r, pair
    raise ValueError("no non-self-dual hook pair found up to max_n")


def verify_bv_duality_scaffold(max_n: int = 9) -> Dict[str, bool]:
    """Sanity checks for the type-A BV duality scaffold."""
    results: Dict[str, bool] = {}

    for n in range(3, max_n + 1):
        # Subregular orbit (n-1,1)
        sub = (n - 1, 1)
        sub_pair = type_a_bv_pair(n, sub)
        expected_sub_dual = hook_partition(n, n - 2)
        results[f"A{n-1} subregular dual hook formula"] = (
            sub_pair.target_orbit == expected_sub_dual
        )

        for r in range(1, n - 1):
            if r > n - 2:
                continue
            pair = type_a_hook_bv_pair(n, r)
            expected = hook_partition(n, n - r - 1)
            back = type_a_bv_dual(pair.target_orbit)
            results[f"A{n-1} hook r={r} transpose formula"] = (
                pair.target_orbit == expected
            )
            results[f"A{n-1} hook r={r} involution"] = (back == pair.source_orbit)

    first_n, first_r, first_pair = first_nonselfdual_type_a_hook_pair(max_n=max_n)
    results["first non-self-dual hook is A3 r=1"] = (
        first_n == 4
        and first_r == 1
        and first_pair.source_orbit == (3, 1)
        and first_pair.target_orbit == (2, 1, 1)
    )

    return results
