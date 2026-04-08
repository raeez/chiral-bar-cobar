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
from functools import lru_cache
from typing import Dict, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.bv_duality import first_nonselfdual_type_a_hook_pair
from compute.lib.nonprincipal_ds_orbits import (
    STATUS_HOOK_EVIDENCE,
    STATUS_PROVED_SUBREGULAR_SL3,
    STATUS_PROGRAMME,
    TRACK_FRONTIER_NONPRINCIPAL,
    Partition,
    hook_partition,
    hook_orbit_pair_profile,
    nonprincipal_general_cases,
    nonprincipal_hook_cases,
    nonprincipal_hook_case,
    nonprincipal_two_row_cases,
    nonprincipal_type_a_case,
    type_a_general_nonprincipal_partitions,
    two_row_nonhook_partition,
    type_a_orbit_class,
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
    """Bershadsky-Polyakov central charge from the sl_3 subregular proposition.

    c(k) = 2 - 24(k+1)^2/(k+3), K_BP = 196.
    BP formula: c = 2 - 24(k+1)^2/(k+3), K=196 (FKR 2020, verified k=-3/2 -> c=-2)
    """
    k = sympify(level)
    if k + 3 == 0:
        raise ValueError("Bershadsky-Polyakov central charge undefined at k = -3")
    return 2 - 24 * (k + 1) ** 2 / (k + 3)


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


def hook_constraint_count_ansatz_type_a(n: int, r: int) -> int:
    """Current hook/subregular DS constraint-count ansatz in type A.

    This is a frontier-level sizing rule for truncated BRST sectors; it is not
    a proved formula for the full non-principal DS complex.
    """
    nonprincipal_hook_case(n, r)
    if n == 3 and r == 1:
        # Match the proved sl_3 subregular seed, which constrains two
        # positive-grade directions (E12 and E13) at the DS-input level.
        return 2
    return hook_orbit_pair_profile(n, r).source_positive_simple_root_count


def hook_pair_constraint_counts_ansatz_type_a(n: int, r: int) -> Tuple[int, int]:
    """Constraint-count ansatz for a hook pair and its transpose-dual orbit."""
    if n == 3 and r == 1:
        return 2, 2
    profile = hook_orbit_pair_profile(n, r)
    return (
        profile.source_positive_simple_root_count,
        profile.target_positive_simple_root_count,
    )


def verify_hook_constraint_count_ansatz(max_n: int = 10) -> Dict[str, bool]:
    """Sanity checks for the hook constraint-count ansatz."""
    results: Dict[str, bool] = {}
    results["ansatz A2 subregular count is 2"] = (
        hook_constraint_count_ansatz_type_a(3, 1) == 2
    )
    results["ansatz first non-self-dual A3 count is 2"] = (
        hook_constraint_count_ansatz_type_a(4, 1) == 2
    )

    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            source, target = hook_pair_constraint_counts_ansatz_type_a(n, r)
            dual_r = n - r - 1
            key = f"A{n-1} hook r={r}"
            results[f"{key} source count positive"] = source >= 1
            results[f"{key} target count positive"] = target >= 1
            if not (n == 3 and r == 1):
                profile = hook_orbit_pair_profile(n, r)
                results[f"{key} source count matches orbit profile"] = (
                    source == profile.source_positive_simple_root_count
                )
                results[f"{key} target count matches orbit profile"] = (
                    target == profile.target_positive_simple_root_count
                )
            dual_source, dual_target = hook_pair_constraint_counts_ansatz_type_a(n, dual_r)
            results[f"{key} dual swap symmetry"] = (
                source == dual_target and target == dual_source
            )
    return results


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


def nonprincipal_type_a_seed(partition: Partition, level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for one non-principal type-A orbit-duality case."""
    orbit_case = nonprincipal_type_a_case(partition, level=level)
    if orbit_case.partition == (2, 1):
        return sl3_subregular_bp_seed(level)

    status = (
        STATUS_HOOK_EVIDENCE
        if orbit_case.status == STATUS_HOOK_EVIDENCE
        else STATUS_PROGRAMME
    )
    family_tag = orbit_case.family
    return NonprincipalDSSeed(
        lie_type=orbit_case.lie_type,
        rank=orbit_case.rank,
        partition=orbit_case.partition,
        dual_partition=orbit_case.dual_partition,
        level_shift=orbit_case.level_shift,
        central_charge=Symbol(f"unknown_nonprincipal_{family_tag}_c"),
        complementarity_sum=Symbol(f"unknown_nonprincipal_{family_tag}_sum"),
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=status,
    )


def nonprincipal_hook_seed(n: int, r: int, level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for one type-A non-principal hook/subregular case.

    For `A_2` subregular (`n=3, r=1`) this returns the proved
    Bershadsky-Polyakov seed. Higher-rank hook/subregular cases remain frontier
    placeholders with explicit unknown central-charge data.
    """
    return _nonprincipal_hook_seed_cached(n, r, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_hook_seed_cached(n: int, r: int, level) -> NonprincipalDSSeed:
    """Cached hook/subregular seed record keyed by normalized level."""
    return nonprincipal_type_a_seed(hook_partition(n, r), level=level)


def nonprincipal_two_row_seed(n: int, s: int, level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for one type-A non-hook two-row orbit case."""
    return _nonprincipal_two_row_seed_cached(n, s, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_two_row_seed_cached(n: int, s: int, level) -> NonprincipalDSSeed:
    """Cached two-row seed record keyed by normalized level."""
    partition = two_row_nonhook_partition(n, s)
    return nonprincipal_type_a_seed(partition, level=level)


def nonprincipal_general_seed(partition: Partition, level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for one general type-A non-principal orbit case."""
    normalized_partition = tuple(partition)
    return _nonprincipal_general_seed_cached(normalized_partition, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_general_seed_cached(partition: Partition, level) -> NonprincipalDSSeed:
    """Cached general non-principal seed record keyed by partition and level."""
    if type_a_orbit_class(partition) != "general_nonprincipal":
        raise ValueError("general non-principal seed requires a general_nonprincipal partition")
    return nonprincipal_type_a_seed(partition, level=level)


def first_nonselfdual_hook_seed(level=Symbol("k")) -> NonprincipalDSSeed:
    """Seed record for the first non-self-dual type-A hook pair (A3)."""
    return _first_nonselfdual_hook_seed_cached(sympify(level))


@lru_cache(maxsize=64)
def _first_nonselfdual_hook_seed_cached(level) -> NonprincipalDSSeed:
    """Cached first non-self-dual hook seed keyed by normalized level."""
    n, r, _ = first_nonselfdual_type_a_hook_pair()
    return nonprincipal_hook_seed(n, r, level=level)


def nonprincipal_hook_seed_catalog(max_n: int = 6, level=Symbol("k")) -> Tuple[NonprincipalDSSeed, ...]:
    """Enumerate non-principal hook/subregular seed records in type A."""
    return _nonprincipal_hook_seed_catalog_cached(max_n, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_hook_seed_catalog_cached(
    max_n: int,
    level,
) -> Tuple[NonprincipalDSSeed, ...]:
    """Cached hook/subregular seed catalog keyed by normalized level."""
    return tuple(
        nonprincipal_hook_seed(n, r, level=level)
        for n in range(3, max_n + 1)
        for r in range(1, n - 1)
    )


def nonprincipal_two_row_seed_catalog(
    max_n: int = 8,
    level=Symbol("k"),
) -> Tuple[NonprincipalDSSeed, ...]:
    """Enumerate non-principal type-A two-row seed records."""
    return _nonprincipal_two_row_seed_catalog_cached(max_n, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_two_row_seed_catalog_cached(
    max_n: int,
    level,
) -> Tuple[NonprincipalDSSeed, ...]:
    """Cached two-row seed catalog keyed by normalized level."""
    return tuple(
        nonprincipal_two_row_seed(n, s, level=level)
        for n in range(4, max_n + 1)
        for s in range(2, (n // 2) + 1)
        if type_a_orbit_class(two_row_nonhook_partition(n, s)) == "two_row_nonhook"
    )


def nonprincipal_general_seed_catalog(
    max_n: int = 8,
    level=Symbol("k"),
) -> Tuple[NonprincipalDSSeed, ...]:
    """Enumerate general type-A non-principal seed records."""
    return _nonprincipal_general_seed_catalog_cached(max_n, sympify(level))


@lru_cache(maxsize=64)
def _nonprincipal_general_seed_catalog_cached(
    max_n: int,
    level,
) -> Tuple[NonprincipalDSSeed, ...]:
    """Cached general non-principal seed catalog keyed by normalized level."""
    return tuple(
        nonprincipal_general_seed(partition, level=level)
        for n in range(3, max_n + 1)
        for partition in type_a_general_nonprincipal_partitions(n)
    )


def verify_nonprincipal_hook_seed_catalog(max_n: int = 8, level=Symbol("k")) -> Dict[str, bool]:
    """Sanity checks for the hook/subregular seed catalog."""
    return dict(_verify_nonprincipal_hook_seed_catalog_items(max_n, sympify(level)))


@lru_cache(maxsize=64)
def _verify_nonprincipal_hook_seed_catalog_items(
    max_n: int,
    level,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for hook/subregular seed catalog verification."""
    results: Dict[str, bool] = {}
    seeds = nonprincipal_hook_seed_catalog(max_n=max_n, level=level)
    orbit_cases = nonprincipal_hook_cases(max_n=max_n, level=level)

    results["hook seed catalog is nonempty"] = bool(seeds)
    results["hook seed catalog matches orbit catalog size"] = (len(seeds) == len(orbit_cases))
    results["hook seed catalog stays on non-principal track"] = all(
        seed.track == TRACK_FRONTIER_NONPRINCIPAL for seed in seeds
    )
    results["hook seed catalog excludes principal/trivial"] = all(
        type_a_orbit_class(seed.partition) not in {"principal", "trivial"} for seed in seeds
    )
    results["hook constraint-count ansatz checks"] = all(
        verify_hook_constraint_count_ansatz(max_n=max_n).values()
    )

    for seed, orbit_case in zip(seeds, orbit_cases):
        n = sum(seed.partition)
        if n == 3 and seed.partition == (2, 1):
            results["A2 subregular keeps proved status"] = (
                seed.status == STATUS_PROVED_SUBREGULAR_SL3
            )
            continue

        key = f"A{n-1} partition {seed.partition}"
        expected_status = (
            STATUS_HOOK_EVIDENCE
            if orbit_case.status == STATUS_HOOK_EVIDENCE
            else STATUS_PROGRAMME
        )
        results[f"{key} status propagates"] = (seed.status == expected_status)
        results[f"{key} dual partition propagates"] = (seed.dual_partition == orbit_case.dual_partition)
        results[f"{key} level shift propagates"] = (simplify(seed.level_shift - orbit_case.level_shift) == 0)

    first = first_nonselfdual_hook_seed(level=level)
    results["first non-self-dual hook remains A3"] = (
        first.partition == (3, 1) and first.dual_partition == (2, 1, 1)
    )

    return tuple(results.items())


def verify_nonprincipal_two_row_seed_catalog(
    max_n: int = 8,
    level=Symbol("k"),
) -> Dict[str, bool]:
    """Sanity checks for the non-hook two-row seed catalog."""
    return dict(_verify_nonprincipal_two_row_seed_catalog_items(max_n, sympify(level)))


@lru_cache(maxsize=64)
def _verify_nonprincipal_two_row_seed_catalog_items(
    max_n: int,
    level,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for two-row seed catalog verification."""
    results: Dict[str, bool] = {}
    seeds = nonprincipal_two_row_seed_catalog(max_n=max_n, level=level)
    orbit_cases = nonprincipal_two_row_cases(max_n=max_n, level=level)

    results["two-row seed catalog is nonempty"] = bool(seeds)
    results["two-row seed catalog matches orbit catalog size"] = (len(seeds) == len(orbit_cases))
    results["two-row seed catalog stays on non-principal track"] = all(
        seed.track == TRACK_FRONTIER_NONPRINCIPAL for seed in seeds
    )
    results["two-row seed catalog excludes principal/trivial"] = all(
        type_a_orbit_class(seed.partition) not in {"principal", "trivial"} for seed in seeds
    )
    results["two-row seed catalog is non-hook"] = all(
        type_a_orbit_class(seed.partition) == "two_row_nonhook" for seed in seeds
    )

    for seed, orbit_case in zip(seeds, orbit_cases):
        n = sum(seed.partition)
        key = f"A{n-1} two-row {seed.partition}"
        expected_status = (
            STATUS_HOOK_EVIDENCE
            if orbit_case.status == STATUS_HOOK_EVIDENCE
            else STATUS_PROGRAMME
        )
        results[f"{key} status propagates"] = (seed.status == expected_status)
        results[f"{key} dual partition propagates"] = (seed.dual_partition == orbit_case.dual_partition)
        results[f"{key} level shift propagates"] = (simplify(seed.level_shift - orbit_case.level_shift) == 0)

    return tuple(results.items())


def verify_nonprincipal_general_seed_catalog(
    max_n: int = 8,
    level=Symbol("k"),
) -> Dict[str, bool]:
    """Sanity checks for the general non-principal seed catalog."""
    return dict(_verify_nonprincipal_general_seed_catalog_items(max_n, sympify(level)))


@lru_cache(maxsize=64)
def _verify_nonprincipal_general_seed_catalog_items(
    max_n: int,
    level,
) -> Tuple[Tuple[str, bool], ...]:
    """Cached immutable items for general non-principal seed catalog verification."""
    results: Dict[str, bool] = {}
    seeds = nonprincipal_general_seed_catalog(max_n=max_n, level=level)
    orbit_cases = nonprincipal_general_cases(max_n=max_n, level=level)

    results["general seed catalog is nonempty"] = bool(seeds)
    results["general seed catalog matches orbit catalog size"] = (len(seeds) == len(orbit_cases))
    results["general seed catalog stays on non-principal track"] = all(
        seed.track == TRACK_FRONTIER_NONPRINCIPAL for seed in seeds
    )
    results["general seed catalog excludes principal/trivial"] = all(
        type_a_orbit_class(seed.partition) not in {"principal", "trivial"} for seed in seeds
    )
    results["general seed catalog stays off hook/two-row families"] = all(
        type_a_orbit_class(seed.partition) == "general_nonprincipal" for seed in seeds
    )

    for seed, orbit_case in zip(seeds, orbit_cases):
        n = sum(seed.partition)
        key = f"A{n-1} general {seed.partition}"
        expected_status = (
            STATUS_HOOK_EVIDENCE
            if orbit_case.status == STATUS_HOOK_EVIDENCE
            else STATUS_PROGRAMME
        )
        results[f"{key} status propagates"] = (seed.status == expected_status)
        results[f"{key} dual partition propagates"] = (seed.dual_partition == orbit_case.dual_partition)
        results[f"{key} level shift propagates"] = (simplify(seed.level_shift - orbit_case.level_shift) == 0)

    return tuple(results.items())


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
    results["sl3 subregular c+c' (current formula bundle) = 196"] = (
        simplify(bp.complementarity_sum - 196) == 0
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
    results["hook seed catalog checks"] = all(
        verify_nonprincipal_hook_seed_catalog(max_n=8, level=k).values()
    )
    results["two-row seed catalog checks"] = all(
        verify_nonprincipal_two_row_seed_catalog(max_n=8, level=k).values()
    )
    results["general nonprincipal seed catalog checks"] = all(
        verify_nonprincipal_general_seed_catalog(max_n=7, level=k).values()
    )
    results["hook constraint-count ansatz checks"] = all(
        verify_hook_constraint_count_ansatz(max_n=8).values()
    )

    return results
