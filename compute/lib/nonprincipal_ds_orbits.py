"""Non-principal DS orbit scaffold for type-A hook/subregular families.

This module is intentionally separated from the principal finite-type PBW
modules. It records only the orbit-combinatorial data needed to launch the
non-principal W frontier:

  - hook and subregular partitions in type A;
  - Barbasch-Vogan duality as partition transpose (type A);
  - orbit/centralizer dimension identities for sl_n nilpotent orbits;
  - a frontier case catalog with explicit status tags.

No OPE or bar differential is implemented here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from sympy import Symbol, sympify

Partition = Tuple[int, ...]

TRACK_CORE_PRINCIPAL = "core_principal_finite_type_pbw"
TRACK_FRONTIER_NONPRINCIPAL = "frontier_nonprincipal_ds_orbit"

STATUS_PROVED_SUBREGULAR_SL3 = "proved_subregular_sl3"
STATUS_HOOK_EVIDENCE = "hook_spectrum_evidence"
STATUS_PROGRAMME = "programme"


@dataclass(frozen=True)
class OrbitDualityCase:
    """Small record used by non-principal DS orbit frontier checks."""

    lie_type: str
    rank: int
    partition: Partition
    dual_partition: Partition
    family: str
    level_shift: object
    track: str
    status: str


def normalize_partition(parts: Iterable[int]) -> Partition:
    """Normalize an integer partition to nonincreasing order."""
    cleaned = []
    for part in parts:
        value = int(part)
        if value <= 0:
            raise ValueError("partition parts must be positive integers")
        cleaned.append(value)
    if not cleaned:
        raise ValueError("partition must be nonempty")
    return tuple(sorted(cleaned, reverse=True))


def partition_size(partition: Iterable[int]) -> int:
    """Total size n of the partition of n."""
    return sum(normalize_partition(partition))


def transpose_partition(partition: Iterable[int]) -> Partition:
    """Ferrers transpose of a partition."""
    lam = normalize_partition(partition)
    height = lam[0]
    return tuple(sum(1 for part in lam if part >= col) for col in range(1, height + 1))


def is_hook_partition(partition: Iterable[int]) -> bool:
    """Return True iff the partition is of hook type (n-r,1^r)."""
    lam = normalize_partition(partition)
    return sum(1 for part in lam if part > 1) <= 1


def hook_partition(n: int, r: int) -> Partition:
    """Hook partition (n-r, 1^r) of n.

    The endpoints are included:
      r = 0   -> principal partition (n)
      r = n-1 -> trivial partition (1^n)
    """
    if n < 1:
        raise ValueError("n must be positive")
    if not (0 <= r <= n - 1):
        raise ValueError("r must satisfy 0 <= r <= n-1")
    return (n - r,) + (1,) * r


def subregular_partition(n: int) -> Partition:
    """Subregular partition in type A_{n-1}: (n-1, 1)."""
    if n < 3:
        raise ValueError("subregular partition requires n >= 3")
    return (n - 1, 1)


def type_a_bv_dual(partition: Iterable[int]) -> Partition:
    """Barbasch-Vogan dual in type A (partition transpose)."""
    return transpose_partition(partition)


def hook_dual_partition(n: int, r: int) -> Partition:
    """Dual of a hook partition in type A."""
    return type_a_bv_dual(hook_partition(n, r))


def type_a_orbit_class(partition: Iterable[int]) -> str:
    """Classify a type-A nilpotent orbit partition."""
    lam = normalize_partition(partition)
    n = sum(lam)
    if lam == (n,):
        return "principal"
    if lam == (1,) * n:
        return "trivial"
    if n >= 3 and lam == (n - 1, 1):
        return "subregular"
    if is_hook_partition(lam):
        return "hook_nonprincipal"
    return "general_nonprincipal"


def centralizer_dimension_sl_n(partition: Iterable[int]) -> int:
    """Dimension of the nilpotent centralizer in sl_n."""
    dual = transpose_partition(partition)
    # gl_n centralizer dimension is sum_i (dual_i)^2; subtract scalar center for sl_n.
    return sum(part * part for part in dual) - 1


def orbit_dimension_sl_n(partition: Iterable[int]) -> int:
    """Dimension of the nilpotent orbit in sl_n."""
    n = partition_size(partition)
    dual = transpose_partition(partition)
    # Dimension agrees with gl_n: n^2 - sum_i (dual_i)^2.
    return n * n - sum(part * part for part in dual)


def principal_ff_level_shift_type_a(n: int, level=Symbol("k")):
    """Principal Feigin-Frenkel involution k -> -k - 2n for sl_n."""
    if n < 2:
        raise ValueError("type A rank requires n >= 2")
    k = sympify(level)
    return -k - 2 * n


def nonprincipal_hook_level_shift_ansatz_type_a(n: int, level=Symbol("k")):
    """Current hook/subregular ansatz for the non-principal level shift.

    This intentionally reuses the principal Feigin-Frenkel involution as a
    starting scaffold, while the full non-principal correction remains open.
    """
    return principal_ff_level_shift_type_a(n, level=level)


def nonprincipal_hook_case(n: int, r: int, level=Symbol("k")) -> OrbitDualityCase:
    """Build a single non-principal hook/subregular frontier case."""
    if not (1 <= r <= n - 2):
        raise ValueError("non-principal hook requires 1 <= r <= n-2")

    partition = hook_partition(n, r)
    dual = hook_dual_partition(n, r)
    family = "subregular" if r == 1 else "hook"

    if n == 3 and r == 1:
        status = STATUS_PROVED_SUBREGULAR_SL3
    elif n <= 6:
        status = STATUS_HOOK_EVIDENCE
    else:
        status = STATUS_PROGRAMME

    return OrbitDualityCase(
        lie_type="A",
        rank=n - 1,
        partition=partition,
        dual_partition=dual,
        family=family,
        level_shift=nonprincipal_hook_level_shift_ansatz_type_a(n, level=level),
        track=TRACK_FRONTIER_NONPRINCIPAL,
        status=status,
    )


def nonprincipal_hook_cases(max_n: int = 6, level=Symbol("k")) -> Tuple[OrbitDualityCase, ...]:
    """Enumerate hook/subregular non-principal seed cases in type A."""
    if max_n < 3:
        return ()
    cases = []
    for n in range(3, max_n + 1):
        for r in range(1, n - 1):
            cases.append(nonprincipal_hook_case(n, r, level=level))
    return tuple(cases)


def verify_nonprincipal_ds_orbit_scaffold(max_n: int = 8) -> Dict[str, bool]:
    """Sanity checks for the hook/subregular non-principal DS scaffold."""
    results: Dict[str, bool] = {}

    for n in range(3, max_n + 1):
        sub = subregular_partition(n)
        sub_dual = type_a_bv_dual(sub)
        expected_sub_dual = hook_partition(n, n - 2)
        results[f"A{n-1} subregular classification"] = type_a_orbit_class(sub) == "subregular"
        results[f"A{n-1} subregular dual formula"] = sub_dual == expected_sub_dual

        # sl_n identity: orbit + centralizer = dim(sl_n) = n^2 - 1
        orbit_dim = orbit_dimension_sl_n(sub)
        centralizer_dim = centralizer_dimension_sl_n(sub)
        results[f"A{n-1} subregular dimension identity"] = orbit_dim + centralizer_dim == n * n - 1

        for r in range(1, n - 1):
            hook = hook_partition(n, r)
            dual = hook_dual_partition(n, r)
            expected = hook_partition(n, n - r - 1)
            cls = type_a_orbit_class(hook)
            case = nonprincipal_hook_case(n, r)

            results[f"A{n-1} hook r={r} is hook"] = is_hook_partition(hook)
            results[f"A{n-1} hook r={r} dual formula"] = dual == expected
            results[f"A{n-1} hook r={r} non-principal class"] = cls in {
                "subregular",
                "hook_nonprincipal",
            }
            results[f"A{n-1} hook r={r} frontier track"] = (
                case.track == TRACK_FRONTIER_NONPRINCIPAL
            )

    cases = nonprincipal_hook_cases(max_n=max_n)
    results["frontier catalog excludes principal"] = all(
        type_a_orbit_class(case.partition) != "principal" for case in cases
    )
    results["frontier catalog excludes trivial"] = all(
        type_a_orbit_class(case.partition) != "trivial" for case in cases
    )

    return results
