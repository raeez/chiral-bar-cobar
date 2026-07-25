r"""Exact non-hook type-A reduction data with typed frontier claims.

The engine computes Young-diagram classes, good-grading BRST combinatorics,
matrix-centralizer generator ledgers, KRW central charges, formal level
reflection, and reachability in the finite reduction graph.  Every strong
generator is even; half-integral conformal weight records the grading, while
parity remains even.

PBW-to-bar collapse, chiral Koszulness, modular quantities, full shadow depth,
categorical transport, DS--bar commutation, transpose-family duality, and
KSDual membership require named packages and return :class:`ClaimPacket`
objects.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_transport_corridor import ReductionGraph
from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    H_HOOK_DS_BAR,
    OpenInvariantError,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    krw_central_charge_data,
    reciprocal_weight_diagnostic_from_partition,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    _partitions_of_n,
    is_hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_partition_sl2_triple,
)


k = Symbol("k")
H_PBW_BAR = (
    "H_PBW^bar: filtered chiral bar comparison, convergence, collapse, "
    "extension control, and twisting compatibility"
)
H_NONHOOK_TRANSPORT = (
    "H_nonhook^transport: realized reduction functors on every graph edge "
    "and compatibility with DS, bar, completion, and Verdier duality"
)
H_FULL_SHADOW = (
    "H_full-shadow: the full Maurer--Cartan coefficient tower across every "
    "generator channel"
)
H_KSDUAL = (
    "H_KSDual: an object-level fixed-point equivalence compatible with "
    "DS/bar and transport"
)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.OPEN, None, hypotheses=tuple(hypotheses))


def _conditional(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.CONDITIONAL, None, hypotheses=tuple(hypotheses))


def is_rectangular(partition: Partition) -> bool:
    """Return whether all rows of the Young diagram have equal length."""

    lam = normalize_partition(partition)
    return len(set(lam)) == 1


def is_even_nilpotent(partition: Partition) -> bool:
    """Return the type-A even-orbit parity criterion."""

    lam = normalize_partition(partition)
    return len({part % 2 for part in lam}) == 1


def partition_orbit_class(partition: Partition) -> str:
    """Classify a partition by hook, transpose, and rectangular combinatorics."""

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    if is_hook_partition(lam):
        return "hook"
    if lam == lam_t and is_rectangular(lam):
        return "self_transpose_rectangular"
    if lam == lam_t:
        return "self_transpose_nonhook"
    return "non_self_transpose_nonhook"


def ds_kd_status(partition: Partition) -> ClaimPacket:
    """Return the typed DS/Koszul comparison obligation."""

    lam = normalize_partition(partition)
    package = H_HOOK_DS_BAR if is_hook_partition(lam) else H_NONHOOK_TRANSPORT
    return _conditional(
        f"DS/Koszul comparison for partition {lam}",
        package,
        H_PBW_BAR,
    )


@dataclass(frozen=True)
class BRSTComplexData:
    """Exact good-grading data and typed PBW/bar consequences."""

    partition: Partition
    N: int
    n_plus_dim: int
    n_plus_grades: Dict[Rational, int]
    n_plus_is_abelian: bool
    g_half_dim: int
    levi_parts: Partition
    levi_dim: int
    is_even: bool
    has_half_integer_grades: bool
    pbw_collapse: ClaimPacket
    is_koszul: ClaimPacket


def brst_complex_analysis(partition: Partition) -> BRSTComplexData:
    """Compute the positive good-grading Lie algebra and its exact dimensions."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    x_diag = [Rational(triple.h[index, index], 2) for index in range(N)]

    grades: Dict[Rational, int] = {}
    positive_roots: List[Tuple[int, int]] = []
    for left in range(N):
        for right in range(N):
            if left == right:
                continue
            grade = x_diag[left] - x_diag[right]
            if grade > 0:
                grades[grade] = grades.get(grade, 0) + 1
                positive_roots.append((left, right))

    positive_set = set(positive_roots)
    nonzero_bracket_exists = any(
        middle == next_left and left != right and (left, right) in positive_set
        for left, middle in positive_roots
        for next_left, right in positive_roots
    )
    central_charge_data = krw_central_charge_data(lam)
    return BRSTComplexData(
        partition=lam,
        N=N,
        n_plus_dim=len(positive_roots),
        n_plus_grades=dict(sorted(grades.items())),
        n_plus_is_abelian=not nonzero_bracket_exists,
        g_half_dim=grades.get(Rational(1, 2), 0),
        levi_parts=transpose_partition(lam),
        levi_dim=central_charge_data.dim_g0,
        is_even=is_even_nilpotent(lam),
        has_half_integer_grades=any(grade.q != 1 for grade in grades),
        pbw_collapse=_conditional(
            f"filtered chiral bar collapse for W(sl_{N},f_{lam})",
            H_PBW_BAR,
        ),
        is_koszul=_conditional(
            f"chiral Koszulness for W(sl_{N},f_{lam})",
            H_PBW_BAR,
            H_HOOK_DS_BAR if is_hook_partition(lam) else H_NONHOOK_TRANSPORT,
        ),
    )


@dataclass(frozen=True)
class ComplementarityData:
    """Exact central scalar arithmetic and typed modular/categorical claims."""

    partition: Partition
    transpose: Partition
    N: int
    is_self_transpose: bool
    orbit_class: str
    formal_reflected_level: object
    c_source: object
    c_transpose_reflected: object
    c_sum: object
    c_sum_k_independent: bool
    formal_central_midpoint: object
    reciprocal_weight_diagnostic_source: Rational
    reciprocal_weight_diagnostic_transpose: Rational
    rho_source: ClaimPacket
    rho_transpose: ClaimPacket
    kappa_source: ClaimPacket
    kappa_transpose: ClaimPacket
    modular_conductor: ClaimPacket
    ds_kd_comparison: ClaimPacket
    source_n_generators: int
    transpose_n_generators: int
    source_n_even: int
    transpose_n_even: int


def complementarity_analysis(partition: Partition, level=k) -> ComplementarityData:
    """Compute formal central reflection data and retain typed derived claims."""

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    level_symbol = sympify(level)
    reflected = hook_dual_level_sl_n(N, level_symbol)
    c_source = krw_central_charge(lam, level_symbol)
    c_transpose = krw_central_charge(lam_t, reflected)
    c_sum = simplify(c_source + c_transpose)
    c_constant = simplify(c_sum.diff(level_symbol)) == 0
    source_generators = w_algebra_generator_data(lam)
    transpose_generators = w_algebra_generator_data(lam_t)
    return ComplementarityData(
        partition=lam,
        transpose=lam_t,
        N=N,
        is_self_transpose=lam == lam_t,
        orbit_class=partition_orbit_class(lam),
        formal_reflected_level=reflected,
        c_source=c_source,
        c_transpose_reflected=c_transpose,
        c_sum=c_sum,
        c_sum_k_independent=c_constant,
        formal_central_midpoint=simplify(c_sum / 2) if lam == lam_t and c_constant else None,
        reciprocal_weight_diagnostic_source=reciprocal_weight_diagnostic_from_partition(lam),
        reciprocal_weight_diagnostic_transpose=reciprocal_weight_diagnostic_from_partition(lam_t),
        rho_source=anomaly_ratio_from_partition(lam),
        rho_transpose=anomaly_ratio_from_partition(lam_t),
        kappa_source=ds_kappa_from_affine(lam, level_symbol),
        kappa_transpose=ds_kappa_from_affine(lam_t, reflected),
        modular_conductor=kappa_complementarity_sum(lam, level_symbol),
        ds_kd_comparison=ds_kd_status(lam),
        source_n_generators=source_generators.f_centralizer_dimension,
        transpose_n_generators=transpose_generators.f_centralizer_dimension,
        source_n_even=source_generators.n_even,
        transpose_n_even=transpose_generators.n_even,
    )


@dataclass(frozen=True)
class ShadowDepthData:
    """Exact generator-line data and an open full-shadow classification."""

    partition: Partition
    N: int
    orbit_class: str
    generator_weights: Tuple[Rational, ...]
    n_even: int
    n_odd: int
    max_weight: Rational
    has_weight_1_generators: bool
    n_weight_1: int
    has_weight_ge_3: bool
    virasoro_line_present: bool
    reciprocal_weight_diagnostic: Rational
    rho: ClaimPacket
    kappa: ClaimPacket
    full_shadow_depth: ClaimPacket

    @property
    def n_bosonic(self) -> int:
        return self.n_even

    @property
    def n_fermionic(self) -> int:
        return self.n_odd


def shadow_depth_analysis(partition: Partition) -> ShadowDepthData:
    """Return finite generator restrictions and the full-shadow obligation."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    generators = w_algebra_generator_data(lam)
    weights = tuple(sorted(Rational(weight) for _, weight, _ in generators.strong_generators))
    weight_one = sum(weight == Rational(1) for weight in weights)
    return ShadowDepthData(
        partition=lam,
        N=N,
        orbit_class=partition_orbit_class(lam),
        generator_weights=weights,
        n_even=generators.n_even,
        n_odd=generators.n_odd,
        max_weight=max(weights),
        has_weight_1_generators=weight_one > 0,
        n_weight_1=weight_one,
        has_weight_ge_3=any(weight >= 3 for weight in weights),
        virasoro_line_present=Rational(2) in weights,
        reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(lam),
        rho=anomaly_ratio_from_partition(lam),
        kappa=ds_kappa_from_affine(lam, k),
        full_shadow_depth=_open(
            f"full shadow depth for W(sl_{N},f_{lam})",
            H_FULL_SHADOW,
        ),
    )


@dataclass(frozen=True)
class TransportAnalysis:
    """Finite graph reachability and typed functorial transport."""

    N: int
    total_partitions: int
    n_hook: int
    n_non_hook: int
    hook_graph_closure_size: int
    graph_reaches_all_partitions: bool
    graph_unreachable: Tuple[Partition, ...]
    partition_data: Dict[Partition, Dict[str, Any]]
    categorical_transport: ClaimPacket


def transport_reachability(N: int) -> TransportAnalysis:
    """Compute reachability in the finite reduction graph from hook vertices."""

    graph = ReductionGraph.build(N)
    hooks = graph.hook_vertices()
    closure = graph.transport_closure(hooks)
    vertices = set(graph.vertices)
    unreachable = tuple(sorted(vertices - closure))

    distances: Dict[Partition, int] = {}
    queue = deque()
    for hook in hooks:
        distances[hook] = 0
        queue.append(hook)
    while queue:
        current = queue.popleft()
        for neighbor in graph.neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    partition_data = {
        lam: {
            "transpose": transpose_partition(lam),
            "orbit_class": partition_orbit_class(lam),
            "is_hook": is_hook_partition(lam),
            "in_graph_closure": lam in closure,
            "graph_distance_from_hooks": distances.get(lam),
            "transport_claim": _conditional(
                f"categorical transport to partition {lam}",
                H_NONHOOK_TRANSPORT,
            ),
        }
        for lam in sorted(vertices)
    }
    return TransportAnalysis(
        N=N,
        total_partitions=len(vertices),
        n_hook=len(hooks),
        n_non_hook=len(vertices) - len(hooks),
        hook_graph_closure_size=len(closure),
        graph_reaches_all_partitions=closure == vertices,
        graph_unreachable=unreachable,
        partition_data=partition_data,
        categorical_transport=_conditional(
            f"functorial propagation across the sl_{N} reduction graph",
            H_NONHOOK_TRANSPORT,
        ),
    )


@dataclass(frozen=True)
class NonHookDualityProfile:
    """Exact non-hook arithmetic and typed object-level comparisons."""

    partition: Partition
    transpose: Partition
    N: int
    orbit_class: str
    is_self_transpose: bool
    is_rectangular: bool
    is_even: bool
    brst: BRSTComplexData
    complementarity: ComplementarityData
    shadow: ShadowDepthData
    graph_reachable_from_hooks: bool
    categorical_transport: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket


def non_hook_duality_profile(partition: Partition, level=k) -> NonHookDualityProfile:
    """Assemble exact data and typed claims for one partition."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    transport = transport_reachability(N)
    comparison_package = H_HOOK_DS_BAR if is_hook_partition(lam) else H_NONHOOK_TRANSPORT
    return NonHookDualityProfile(
        partition=lam,
        transpose=transpose_partition(lam),
        N=N,
        orbit_class=partition_orbit_class(lam),
        is_self_transpose=lam == transpose_partition(lam),
        is_rectangular=is_rectangular(lam),
        is_even=is_even_nilpotent(lam),
        brst=brst_complex_analysis(lam),
        complementarity=complementarity_analysis(lam, level),
        shadow=shadow_depth_analysis(lam),
        graph_reachable_from_hooks=transport.partition_data[lam]["in_graph_closure"],
        categorical_transport=_conditional(
            f"categorical transport from the hook corridor to {lam}",
            comparison_package,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar commutation for partition {lam}",
            comparison_package,
            H_PBW_BAR,
        ),
        koszul_duality=_conditional(
            f"object-level Koszul comparison with transpose {transpose_partition(lam)}",
            comparison_package,
            H_PBW_BAR,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for partition {lam}",
            H_KSDUAL,
        ),
    )


def non_hook_catalog(N: int) -> List[NonHookDualityProfile]:
    """Return profiles for every non-hook partition of ``N``."""

    return [
        non_hook_duality_profile(lam)
        for lam in _partitions_of_n(N)
        if not is_hook_partition(lam)
    ]


def full_catalog(N: int) -> List[NonHookDualityProfile]:
    """Return profiles for every partition of ``N``."""

    return [non_hook_duality_profile(lam) for lam in _partitions_of_n(N)]


def self_transpose_catalog(max_N: int = 8) -> List[NonHookDualityProfile]:
    """Return profiles for all self-transpose diagrams through ``max_N``."""

    return [
        non_hook_duality_profile(lam)
        for N in range(2, max_N + 1)
        for lam in _partitions_of_n(N)
        if lam == transpose_partition(lam)
    ]


def numerical_c_complementarity(partition: Partition, levels=None) -> List[Dict[str, object]]:
    """Evaluate the exact formal central scalar sum at selected levels."""

    if levels is None:
        levels = [Rational(0), Rational(1), Rational(2), Rational(5)]
    data = complementarity_analysis(partition, k)
    return [
        {
            "level": level,
            "reflected_level": data.formal_reflected_level.subs(k, level),
            "c_source": data.c_source.subs(k, level),
            "c_transpose_reflected": data.c_transpose_reflected.subs(k, level),
            "c_sum": data.c_sum.subs(k, level),
        }
        for level in levels
    ]


def numerical_kappa_complementarity(partition: Partition, levels=None) -> ClaimPacket:
    """Return the open numerical modular-comparison packet."""

    lam = normalize_partition(partition)
    return _open(
        f"numerical K^kappa specializations for partition {lam}",
        "numeric values of kappa from direct genus-one calculations",
        H_NONHOOK_TRANSPORT,
    )


def verify_self_transpose_c_complementarity(max_N: int = 8) -> List[Dict[str, Any]]:
    """Verify formal central reflection sums for self-transpose diagrams."""

    results = []
    for profile in self_transpose_catalog(max_N):
        data = profile.complementarity
        results.append({
            "partition": profile.partition,
            "N": profile.N,
            "central_sum": data.c_sum,
            "central_sum_k_independent": data.c_sum_k_independent,
            "formal_central_midpoint": data.formal_central_midpoint,
            "duality_claim": profile.koszul_duality,
        })
    return results


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "BRSTComplexData",
    "ComplementarityData",
    "ShadowDepthData",
    "TransportAnalysis",
    "NonHookDualityProfile",
    "is_rectangular",
    "is_even_nilpotent",
    "partition_orbit_class",
    "ds_kd_status",
    "brst_complex_analysis",
    "complementarity_analysis",
    "shadow_depth_analysis",
    "transport_reachability",
    "non_hook_duality_profile",
    "non_hook_catalog",
    "full_catalog",
    "self_transpose_catalog",
    "numerical_c_complementarity",
    "numerical_kappa_complementarity",
    "verify_self_transpose_c_complementarity",
]
