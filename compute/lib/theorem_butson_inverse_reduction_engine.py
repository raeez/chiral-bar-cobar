r"""Exact type-A orbit arithmetic with typed inverse-reduction claims.

For partitions of ``N`` this engine computes the dominance order, Hasse
covers, positive-coroot steps, centralizer and orbit dimensions, exact strong
generator ledgers, Kac--Roan--Wakimoto central charges, formal level
reflection, and finite graph reachability.

Butson--Nair (2025), Theorem 1.1 and Corollary 6.9, prove generic-level
inverse Hamiltonian reduction for affine ``gl_N`` W-algebras along their
positive-coroot corridor.  Applying that theorem to the ``sl_N`` conventions
used here, identifying the localized auxiliary free fields, and transporting
bar, PBW, modular, Koszul, or duality structures require explicit hypothesis
packages.  Those surfaces return :class:`ClaimPacket` objects.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    OpenInvariantError,
    WAlgebraGeneratorData,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
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
    type_a_orbit_class,
)


k = Symbol("k")
BUTSON_NAIR_AFFINE_SOURCE = (
    "Butson--Nair (2025), Theorem 1.1 and Corollary 6.9, arXiv:2508.18248"
)
BUTSON_NAIR_FINITE_SOURCE = (
    "Butson--Nair (2025), Theorem 1.1, arXiv:2503.19882"
)
BUTSON_CY3_SOURCE = "Butson (2023), arXiv:2312.03648"

H_BN_IHR = (
    "H_BN-IHR: identify the Hasse cover with the positive-coroot datum of "
    "Butson--Nair and carry Corollary 6.9 from gl_N to the chosen sl_N normalization"
)
H_BN_AUX = (
    "H_BN-aux: identify the localized chiral differential-operator algebra, "
    "its free-field factors, and the level convention for this cover"
)
H_BN_BAR = (
    "H_BN-bar: a filtered chain-level comparison between inverse reduction, "
    "the completed chiral bar complex, and the auxiliary free fields"
)
H_PBW_BAR = (
    "H_PBW-bar: convergence and extension control for the PBW-to-chiral-bar "
    "spectral sequence with compatible twisting morphism"
)
H_MODULAR = (
    "H_BN-modular: genus-one characteristics in a common normalization and "
    "additivity across the inverse-reduction free-field factor"
)
H_TRANSPORT = (
    "H_BN-transport: realized functors on the chosen edge chain, together "
    "with composition, completion, and Verdier compatibility"
)
H_KOSZUL = (
    "H_BN-Koszul: PBW/bar collapse plus a perfect twisting comparison for "
    "the source, target, and auxiliary factor"
)
H_DUALITY = (
    "H_transpose-duality: an object-level Koszul equivalence with the "
    "transpose partition at formal reflected level"
)
H_KSDUAL = (
    "H_KSDual: a fixed-point equivalence compatible with inverse reduction, "
    "DS/bar comparison, and transpose duality"
)
H_CY3 = (
    "H_CY3-VA: the proposed CY3 divisor identification, free generation, "
    "genus-one characteristic, and bar comparison"
)


def _open(statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()) -> ClaimPacket:
    return ClaimPacket(
        statement,
        ClaimStatus.OPEN,
        None,
        evidence=evidence,
        hypotheses=tuple(hypotheses),
    )


def _conditional(
    statement: str,
    *hypotheses: str,
    evidence: Tuple[str, ...] = (),
) -> ClaimPacket:
    return ClaimPacket(
        statement,
        ClaimStatus.CONDITIONAL,
        None,
        evidence=evidence,
        hypotheses=tuple(hypotheses),
    )


def _proved_elsewhere(statement: str, value, *evidence: str) -> ClaimPacket:
    return ClaimPacket(
        statement,
        ClaimStatus.PROVED_ELSEWHERE,
        value,
        evidence=tuple(evidence),
    )


@lru_cache(maxsize=None)
def _partitions(n: int) -> Tuple[Partition, ...]:
    return tuple(normalize_partition(partition) for partition in _partitions_of_n(n))


def dominance_order(lam: Partition, mu: Partition) -> bool:
    r"""Return the type-A dominance relation ``lam >= mu``."""

    lam = normalize_partition(lam)
    mu = normalize_partition(mu)
    if partition_size(lam) != partition_size(mu):
        raise ValueError("partitions must have the same size")
    width = max(len(lam), len(mu))
    lam_padded = lam + (0,) * (width - len(lam))
    mu_padded = mu + (0,) * (width - len(mu))
    return all(
        sum(lam_padded[: index + 1]) >= sum(mu_padded[: index + 1])
        for index in range(width)
    )


def is_covering_relation(lam: Partition, mu: Partition) -> bool:
    r"""Return whether ``lam`` covers ``mu`` in dominance order."""

    lam = normalize_partition(lam)
    mu = normalize_partition(mu)
    if partition_size(lam) != partition_size(mu):
        raise ValueError("partitions must have the same size")
    if lam == mu or not dominance_order(lam, mu):
        return False
    return all(
        nu in (lam, mu)
        or not (dominance_order(lam, nu) and dominance_order(nu, mu))
        for nu in _partitions(partition_size(lam))
    )


@lru_cache(maxsize=None)
def _orbit_hasse_edges(n: int) -> Tuple[Tuple[Partition, Partition], ...]:
    return tuple(
        (lam, mu)
        for lam in _partitions(n)
        for mu in _partitions(n)
        if lam != mu and is_covering_relation(lam, mu)
    )


def orbit_hasse_diagram(n: int) -> Dict[Partition, List[Partition]]:
    r"""Return the finite Hasse diagram of type-A nilpotent orbits."""

    diagram = {partition: [] for partition in _partitions(n)}
    for lam, mu in _orbit_hasse_edges(n):
        diagram[lam].append(mu)
    return diagram


def orbit_hasse_edges(n: int) -> List[Tuple[Partition, Partition]]:
    r"""Return every oriented Hasse edge ``lam > mu``."""

    return list(_orbit_hasse_edges(n))


def partition_root_step(target: Partition, source: Partition) -> Tuple[int, ...]:
    r"""Return the padded row-vector difference ``target-source``."""

    target = normalize_partition(target)
    source = normalize_partition(source)
    if partition_size(target) != partition_size(source):
        raise ValueError("partitions must have the same size")
    width = max(len(target), len(source))
    target_padded = target + (0,) * (width - len(target))
    source_padded = source + (0,) * (width - len(source))
    return tuple(left - right for left, right in zip(target_padded, source_padded))


def is_positive_coroot_step(target: Partition, source: Partition) -> bool:
    r"""Return whether ``target-source`` is a positive type-A coroot."""

    nonzero = [entry for entry in partition_root_step(target, source) if entry]
    return nonzero == [1, -1]


def type_a_centralizer_dimension(partition: Partition) -> int:
    r"""Return ``dim sl_N^f = sum_j (lambda_j^t)^2 - 1``."""

    transpose = transpose_partition(normalize_partition(partition))
    return sum(column * column for column in transpose) - 1


def type_a_orbit_dimension(partition: Partition) -> int:
    r"""Return the dimension of the nilpotent ``SL_N`` orbit."""

    lam = normalize_partition(partition)
    n = partition_size(lam)
    return n * n - 1 - type_a_centralizer_dimension(lam)


@dataclass(frozen=True)
class InverseReductionEdge:
    r"""Exact Hasse-cover data and typed inverse-reduction obligations."""

    n: int
    source: Partition
    target: Partition
    root_step: Tuple[int, ...]
    is_positive_coroot_step: bool
    source_centralizer_dim: int
    target_centralizer_dim: int
    source_orbit_dim: int
    target_orbit_dim: int
    centralizer_dimension_drop: int
    orbit_dimension_jump: int
    half_orbit_dimension_jump: int
    source_generators: WAlgebraGeneratorData
    target_generators: WAlgebraGeneratorData
    is_hook_edge: bool
    inverse_reduction: ClaimPacket
    auxiliary_free_fields: ClaimPacket
    bar_compatibility: ClaimPacket


def inverse_reduction_edge(
    n: int,
    source: Partition,
    target: Partition,
) -> InverseReductionEdge:
    r"""Return exact data for the Hasse cover ``target > source``."""

    source = normalize_partition(source)
    target = normalize_partition(target)
    if partition_size(source) != n or partition_size(target) != n:
        raise ValueError(f"partitions must have size {n}")
    if not is_covering_relation(target, source):
        raise ValueError("target must cover source in dominance order")

    root_step = partition_root_step(target, source)
    positive_coroot = is_positive_coroot_step(target, source)
    source_generators = w_algebra_generator_data(source)
    target_generators = w_algebra_generator_data(target)
    source_centralizer = type_a_centralizer_dimension(source)
    target_centralizer = type_a_centralizer_dimension(target)
    if source_generators.f_centralizer_dimension != source_centralizer:
        raise ArithmeticError("source centralizer formulas disagree")
    if target_generators.f_centralizer_dimension != target_centralizer:
        raise ArithmeticError("target centralizer formulas disagree")

    source_orbit = type_a_orbit_dimension(source)
    target_orbit = type_a_orbit_dimension(target)
    centralizer_drop = source_centralizer - target_centralizer
    orbit_jump = target_orbit - source_orbit
    if centralizer_drop != orbit_jump or orbit_jump % 2:
        raise ArithmeticError("orbit and centralizer dimension formulas disagree")

    evidence = (BUTSON_NAIR_AFFINE_SOURCE, BUTSON_NAIR_FINITE_SOURCE)
    return InverseReductionEdge(
        n=n,
        source=source,
        target=target,
        root_step=root_step,
        is_positive_coroot_step=positive_coroot,
        source_centralizer_dim=source_centralizer,
        target_centralizer_dim=target_centralizer,
        source_orbit_dim=source_orbit,
        target_orbit_dim=target_orbit,
        centralizer_dimension_drop=centralizer_drop,
        orbit_dimension_jump=orbit_jump,
        half_orbit_dimension_jump=orbit_jump // 2,
        source_generators=source_generators,
        target_generators=target_generators,
        is_hook_edge=is_hook_partition(source) and is_hook_partition(target),
        inverse_reduction=_conditional(
            f"generic-level affine inverse reduction {source}->{target} in the sl_{n} convention",
            H_BN_IHR,
            evidence=evidence,
        ),
        auxiliary_free_fields=_conditional(
            f"localized auxiliary free-field identification for {source}->{target}",
            H_BN_IHR,
            H_BN_AUX,
            evidence=evidence,
        ),
        bar_compatibility=_conditional(
            f"bar compatibility of inverse reduction {source}->{target}",
            H_BN_IHR,
            H_BN_AUX,
            H_BN_BAR,
            evidence=(BUTSON_NAIR_AFFINE_SOURCE,),
        ),
    )


def all_inverse_reduction_edges(n: int) -> List[InverseReductionEdge]:
    r"""Return typed inverse-reduction records for every Hasse cover."""

    return [
        inverse_reduction_edge(n, source=mu, target=lam)
        for lam, mu in _orbit_hasse_edges(n)
    ]


@dataclass(frozen=True)
class KappaEdgeData:
    r"""Exact central data and typed modular fields on one Hasse edge."""

    edge: InverseReductionEdge
    level: object
    source_central_charge: object
    target_central_charge: object
    formal_central_difference: object
    source_reciprocal_weight_diagnostic: Rational
    target_reciprocal_weight_diagnostic: Rational
    source_rho: ClaimPacket
    target_rho: ClaimPacket
    source_kappa: ClaimPacket
    target_kappa: ClaimPacket
    kappa_deficit: ClaimPacket
    modular_additivity: ClaimPacket


def kappa_along_edge(
    edge: InverseReductionEdge,
    level=k,
) -> KappaEdgeData:
    r"""Return exact central arithmetic and the modular edge obligation."""

    level = sympify(level)
    source_c = krw_central_charge(edge.source, level)
    target_c = krw_central_charge(edge.target, level)
    return KappaEdgeData(
        edge=edge,
        level=level,
        source_central_charge=source_c,
        target_central_charge=target_c,
        formal_central_difference=simplify(source_c - target_c),
        source_reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(
            edge.source
        ),
        target_reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(
            edge.target
        ),
        source_rho=anomaly_ratio_from_partition(edge.source),
        target_rho=anomaly_ratio_from_partition(edge.target),
        source_kappa=ds_kappa_from_affine(edge.source, level),
        target_kappa=ds_kappa_from_affine(edge.target, level),
        kappa_deficit=_open(
            f"kappa deficit across inverse-reduction edge {edge.source}->{edge.target}",
            H_MODULAR,
            H_BN_AUX,
        ),
        modular_additivity=_conditional(
            f"modular additivity across inverse-reduction edge {edge.source}->{edge.target}",
            H_BN_IHR,
            H_BN_AUX,
            H_MODULAR,
            evidence=(BUTSON_NAIR_AFFINE_SOURCE,),
        ),
    )


def _hasse_adjacency(n: int) -> Dict[Partition, Set[Partition]]:
    adjacency = {partition: set() for partition in _partitions(n)}
    for lam, mu in _orbit_hasse_edges(n):
        adjacency[lam].add(mu)
        adjacency[mu].add(lam)
    return adjacency


def _shortest_hasse_path(
    n: int,
    source: Partition,
    target: Partition,
) -> Tuple[Partition, ...]:
    source = normalize_partition(source)
    target = normalize_partition(target)
    if source == target:
        return (source,)
    adjacency = _hasse_adjacency(n)
    queue = deque([source])
    previous: Dict[Partition, Optional[Partition]] = {source: None}
    while queue:
        current = queue.popleft()
        for neighbor in sorted(adjacency[current]):
            if neighbor in previous:
                continue
            previous[neighbor] = current
            if neighbor == target:
                path = [target]
                while previous[path[-1]] is not None:
                    path.append(previous[path[-1]])
                return tuple(reversed(path))
            queue.append(neighbor)
    return ()


@dataclass(frozen=True)
class TransposeVerificationData:
    r"""Exact transpose arithmetic and typed object-level comparisons."""

    partition: Partition
    transpose: Partition
    n: int
    orbit_class: str
    is_self_transpose: bool
    source_generators: WAlgebraGeneratorData
    transpose_generators: WAlgebraGeneratorData
    source_n_generators: int
    transpose_n_generators: int
    generator_count_match: bool
    formal_reflected_level: object
    source_central_charge: object
    transpose_reflected_central_charge: object
    formal_central_sum: object
    formal_central_sum_k_independent: Optional[bool]
    source_reciprocal_weight_diagnostic: Rational
    transpose_reciprocal_weight_diagnostic: Rational
    source_rho: ClaimPacket
    transpose_rho: ClaimPacket
    source_kappa: ClaimPacket
    transpose_kappa: ClaimPacket
    modular_conductor: ClaimPacket
    hasse_path_to_transpose: Tuple[Partition, ...]
    graph_reaches_transpose: bool
    categorical_transport: ClaimPacket
    bar_compatibility: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def source_c(self):
        return self.source_central_charge

    @property
    def dual_c(self):
        return self.transpose_reflected_central_charge

    @property
    def c_sum(self):
        return self.formal_central_sum

    @property
    def c_sum_is_constant(self):
        return self.formal_central_sum_k_independent


def verify_transport_to_transpose(
    partition: Partition,
    level=k,
) -> TransposeVerificationData:
    r"""Compute transpose arithmetic and retain typed transport claims."""

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    n = partition_size(lam)
    level = sympify(level)
    reflected = hook_dual_level_sl_n(n, level)
    source_generators = w_algebra_generator_data(lam)
    transpose_generators = w_algebra_generator_data(lam_t)
    source_c = krw_central_charge(lam, level)
    transpose_c = krw_central_charge(lam_t, reflected)
    central_sum = simplify(source_c + transpose_c)
    central_constant = (
        simplify(central_sum.diff(level)) == 0 if isinstance(level, Symbol) else None
    )
    path = _shortest_hasse_path(n, lam, lam_t)
    return TransposeVerificationData(
        partition=lam,
        transpose=lam_t,
        n=n,
        orbit_class=type_a_orbit_class(lam),
        is_self_transpose=lam == lam_t,
        source_generators=source_generators,
        transpose_generators=transpose_generators,
        source_n_generators=source_generators.f_centralizer_dimension,
        transpose_n_generators=transpose_generators.f_centralizer_dimension,
        generator_count_match=(
            source_generators.f_centralizer_dimension
            == transpose_generators.f_centralizer_dimension
        ),
        formal_reflected_level=reflected,
        source_central_charge=source_c,
        transpose_reflected_central_charge=transpose_c,
        formal_central_sum=central_sum,
        formal_central_sum_k_independent=central_constant,
        source_reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(lam),
        transpose_reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(
            lam_t
        ),
        source_rho=anomaly_ratio_from_partition(lam),
        transpose_rho=anomaly_ratio_from_partition(lam_t),
        source_kappa=ds_kappa_from_affine(lam, level),
        transpose_kappa=ds_kappa_from_affine(lam_t, reflected),
        modular_conductor=kappa_complementarity_sum(lam, level),
        hasse_path_to_transpose=path,
        graph_reaches_transpose=bool(path),
        categorical_transport=_conditional(
            f"categorical transport from {lam} to transpose {lam_t}",
            H_BN_IHR,
            H_TRANSPORT,
            evidence=(BUTSON_NAIR_AFFINE_SOURCE,),
        ),
        bar_compatibility=_conditional(
            f"bar compatibility along a Hasse path from {lam} to {lam_t}",
            H_BN_BAR,
            H_TRANSPORT,
        ),
        koszul_duality=_conditional(
            f"object-level Koszul duality between {lam} and {lam_t}",
            H_KOSZUL,
            H_DUALITY,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for partition {lam}",
            H_KSDUAL,
        ),
    )


def verify_all_partitions_transport(
    n: int,
    level=k,
) -> Dict[Partition, TransposeVerificationData]:
    r"""Return typed transpose profiles for every partition of ``n``."""

    return {
        partition: verify_transport_to_transpose(partition, level)
        for partition in _partitions(n)
    }


@dataclass(frozen=True)
class KoszulnessData:
    r"""Exact Slodowy/generator data and typed bar/Koszul obligations."""

    partition: Partition
    n: int
    orbit_class: str
    slodowy_slice_dimension: int
    slodowy_slice_is_affine_space: bool
    arc_space_is_affine: bool
    generator_weights: Tuple[Rational, ...]
    n_generators: int
    n_even: int
    n_odd: int
    inverse_reduction: ClaimPacket
    pbw_collapse: ClaimPacket
    bar_comparison: ClaimPacket
    koszulness: ClaimPacket
    full_shadow_depth: ClaimPacket

    @property
    def arc_space_affine(self) -> bool:
        return self.arc_space_is_affine


def koszulness_certificate(partition: Partition) -> KoszulnessData:
    r"""Return exact finite data and the generic-level Koszul obligations."""

    lam = normalize_partition(partition)
    n = partition_size(lam)
    generators = w_algebra_generator_data(lam)
    weights = tuple(
        sorted(Rational(weight) for _, weight, _ in generators.strong_generators)
    )
    return KoszulnessData(
        partition=lam,
        n=n,
        orbit_class=type_a_orbit_class(lam),
        slodowy_slice_dimension=type_a_centralizer_dimension(lam),
        slodowy_slice_is_affine_space=True,
        arc_space_is_affine=True,
        generator_weights=weights,
        n_generators=generators.f_centralizer_dimension,
        n_even=generators.n_even,
        n_odd=generators.n_odd,
        inverse_reduction=_conditional(
            f"generic-level inverse-reduction placement for partition {lam}",
            H_BN_IHR,
            evidence=(BUTSON_NAIR_AFFINE_SOURCE,),
        ),
        pbw_collapse=_conditional(
            f"PBW-to-bar collapse for W(sl_{n},f_{lam})",
            H_PBW_BAR,
        ),
        bar_comparison=_conditional(
            f"inverse-reduction/bar comparison for W(sl_{n},f_{lam})",
            H_BN_BAR,
            H_PBW_BAR,
        ),
        koszulness=_conditional(
            f"chiral Koszulness for W(sl_{n},f_{lam}) at generic level",
            H_KOSZUL,
            H_PBW_BAR,
        ),
        full_shadow_depth=_open(
            f"full shadow depth for W(sl_{n},f_{lam})",
            "the complete Maurer--Cartan coefficient tower across every generator channel",
        ),
    )


@dataclass(frozen=True)
class TransportGraph:
    r"""Finite Hasse reachability and typed categorical transport."""

    n: int
    partitions: Tuple[Partition, ...]
    edges: Tuple[InverseReductionEdge, ...]
    hasse_diagram: Dict[Partition, Tuple[Partition, ...]]
    hook_partitions: Tuple[Partition, ...]
    reachable_from_hooks: FrozenSet[Partition]
    combinatorial_full_reachability: bool
    inverse_reduction_surface: ClaimPacket
    categorical_transport: ClaimPacket

    @property
    def full_reachability(self) -> bool:
        return self.combinatorial_full_reachability


def build_transport_graph(n: int) -> TransportGraph:
    r"""Build the undirected finite Hasse graph and typed transport surface."""

    partitions = _partitions(n)
    edges = tuple(all_inverse_reduction_edges(n))
    adjacency = _hasse_adjacency(n)
    hooks = tuple(partition for partition in partitions if is_hook_partition(partition))
    reachable: Set[Partition] = set(hooks)
    queue = deque(hooks)
    while queue:
        current = queue.popleft()
        for neighbor in adjacency[current]:
            if neighbor in reachable:
                continue
            reachable.add(neighbor)
            queue.append(neighbor)
    full = reachable == set(partitions)
    return TransportGraph(
        n=n,
        partitions=partitions,
        edges=edges,
        hasse_diagram={
            partition: tuple(sorted(covers))
            for partition, covers in orbit_hasse_diagram(n).items()
        },
        hook_partitions=hooks,
        reachable_from_hooks=frozenset(reachable),
        combinatorial_full_reachability=full,
        inverse_reduction_surface=_conditional(
            f"generic-level inverse reduction on every sl_{n} Hasse edge",
            H_BN_IHR,
            H_BN_AUX,
            evidence=(BUTSON_NAIR_AFFINE_SOURCE,),
        ),
        categorical_transport=_conditional(
            f"categorical transport across the sl_{n} Hasse graph",
            H_BN_IHR,
            H_TRANSPORT,
        ),
    )


def formal_central_scalar_sum(partition: Partition, level=k):
    r"""Return ``c_lambda(k)+c_lambda^t(-k-2N)`` as exact arithmetic."""

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    n = partition_size(lam)
    level = sympify(level)
    reflected = hook_dual_level_sl_n(n, level)
    return simplify(
        krw_central_charge(lam, level)
        + krw_central_charge(lam_t, reflected)
    )


def central_charge_conductor(partition: Partition, level=k):
    r"""Compatibility name for the exact formal central scalar sum."""

    return formal_central_scalar_sum(partition, level)


def central_charge_conductor_catalog(
    max_n: int = 6,
    level=k,
) -> Dict[Partition, object]:
    r"""Return formal central scalar sums through ``sl_max_n``."""

    return {
        partition: formal_central_scalar_sum(partition, level)
        for n in range(3, max_n + 1)
        for partition in _partitions(n)
    }


def anomaly_ratio_catalog(max_n: int = 6) -> Dict[Partition, ClaimPacket]:
    r"""Return open ``rho`` packets for each nontrivial partition."""

    return {
        partition: anomaly_ratio_from_partition(partition)
        for n in range(2, max_n + 1)
        for partition in _partitions(n)
        if partition != (1,) * n
    }


def anomaly_ratio_transpose_relation(partition: Partition) -> Dict[str, object]:
    r"""Separate exact reciprocal diagnostics from open modular data."""

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    return {
        "partition": lam,
        "transpose": lam_t,
        "source_reciprocal_weight_diagnostic": reciprocal_weight_diagnostic_from_partition(
            lam
        ),
        "transpose_reciprocal_weight_diagnostic": reciprocal_weight_diagnostic_from_partition(
            lam_t
        ),
        "source_rho": anomaly_ratio_from_partition(lam),
        "transpose_rho": anomaly_ratio_from_partition(lam_t),
        "rho_comparison": _open(
            f"genus-one rho comparison for transpose pair {lam}, {lam_t}",
            H_MODULAR,
        ),
        "modular_conductor": kappa_complementarity_sum(lam, k),
    }


@dataclass(frozen=True)
class CY3VertexAlgebraCandidate:
    r"""A CY3 divisor construction with typed identification claims."""

    description: str
    parameters: Dict[str, object]
    proposed_identification: str
    construction: ClaimPacket
    identification: ClaimPacket
    free_generation: ClaimPacket
    modular_characteristic: ClaimPacket
    koszulness: ClaimPacket

    @property
    def conjectural_identification(self) -> str:
        return self.proposed_identification


def _cy3_candidate(
    description: str,
    parameters: Dict[str, object],
    proposed_identification: str,
) -> CY3VertexAlgebraCandidate:
    return CY3VertexAlgebraCandidate(
        description=description,
        parameters=parameters,
        proposed_identification=proposed_identification,
        construction=_proved_elsewhere(
            f"CY3 divisor vertex algebra construction for {description}",
            True,
            BUTSON_CY3_SOURCE,
        ),
        identification=_open(
            f"identification with {proposed_identification}",
            H_CY3,
            evidence=(BUTSON_CY3_SOURCE,),
        ),
        free_generation=_open(
            f"free strong generation for {proposed_identification}",
            H_CY3,
        ),
        modular_characteristic=_open(
            f"genus-one modular characteristic for {proposed_identification}",
            H_CY3,
        ),
        koszulness=_conditional(
            f"chiral Koszulness for {proposed_identification}",
            H_CY3,
            H_PBW_BAR,
            H_KOSZUL,
        ),
    )


def cy3_candidate_catalog() -> List[CY3VertexAlgebraCandidate]:
    r"""Return typed CY3 divisor candidates from Butson's programme."""

    return [
        _cy3_candidate(
            "resolved-conifold divisor",
            {"m": 2, "n": 0, "f": "principal"},
            "W^kappa(gl_2,f_principal) / Virasoro corridor",
        ),
        _cy3_candidate(
            "gl_{1|1} divisor",
            {"m": 1, "n": 1, "f": "principal"},
            "W^kappa(gl_{1|1}) / bc corridor",
        ),
        _cy3_candidate(
            "gl_{2|1} minimal divisor",
            {"m": 2, "n": 1, "f": "minimal"},
            "W^kappa(gl_{2|1},f_minimal)",
        ),
        _cy3_candidate(
            "genus-zero class-S divisor",
            {"m": 2, "punctures": 3},
            "V^S_{GL_2;f_1,f_2,f_3}",
        ),
    ]


@dataclass(frozen=True)
class ButsonAnalysisSummary:
    r"""Exact finite census and typed theorem-level consequences."""

    n: int
    total_partitions: int
    total_edges: int
    hook_edges: int
    non_hook_edges: int
    combinatorial_full_reachability: bool
    all_edges_are_positive_coroot_steps: bool
    self_transpose_central_sums_constant: bool
    inverse_reduction_surface: ClaimPacket
    bar_compatibility: ClaimPacket
    pbw_collapse: ClaimPacket
    koszulness: ClaimPacket
    categorical_transport: ClaimPacket
    transpose_duality: ClaimPacket

    @property
    def full_reachability(self) -> bool:
        return self.combinatorial_full_reachability

    @property
    def c_conductor_constant_self_transpose(self) -> bool:
        return self.self_transpose_central_sums_constant


def butson_analysis(n: int, level=k) -> ButsonAnalysisSummary:
    r"""Return the exact Hasse census and typed Butson programme surface."""

    graph = build_transport_graph(n)
    self_transpose = [
        partition
        for partition in graph.partitions
        if partition == transpose_partition(partition)
    ]
    central_constant = all(
        simplify(formal_central_scalar_sum(partition, k).diff(k)) == 0
        for partition in self_transpose
    )
    hook_edges = sum(edge.is_hook_edge for edge in graph.edges)
    return ButsonAnalysisSummary(
        n=n,
        total_partitions=len(graph.partitions),
        total_edges=len(graph.edges),
        hook_edges=hook_edges,
        non_hook_edges=len(graph.edges) - hook_edges,
        combinatorial_full_reachability=graph.combinatorial_full_reachability,
        all_edges_are_positive_coroot_steps=all(
            edge.is_positive_coroot_step for edge in graph.edges
        ),
        self_transpose_central_sums_constant=central_constant,
        inverse_reduction_surface=graph.inverse_reduction_surface,
        bar_compatibility=_conditional(
            f"bar compatibility across the sl_{n} inverse-reduction surface",
            H_BN_BAR,
            H_TRANSPORT,
        ),
        pbw_collapse=_conditional(
            f"PBW-to-bar collapse across all sl_{n} orbit strata",
            H_PBW_BAR,
        ),
        koszulness=_conditional(
            f"generic-level chiral Koszulness across all sl_{n} orbit strata",
            H_PBW_BAR,
            H_KOSZUL,
        ),
        categorical_transport=graph.categorical_transport,
        transpose_duality=_conditional(
            f"transpose-family Koszul duality for sl_{n}",
            H_TRANSPORT,
            H_DUALITY,
        ),
    )


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "InverseReductionEdge",
    "KappaEdgeData",
    "TransposeVerificationData",
    "KoszulnessData",
    "TransportGraph",
    "CY3VertexAlgebraCandidate",
    "ButsonAnalysisSummary",
    "dominance_order",
    "is_covering_relation",
    "orbit_hasse_diagram",
    "orbit_hasse_edges",
    "partition_root_step",
    "is_positive_coroot_step",
    "type_a_centralizer_dimension",
    "type_a_orbit_dimension",
    "inverse_reduction_edge",
    "all_inverse_reduction_edges",
    "kappa_along_edge",
    "verify_transport_to_transpose",
    "verify_all_partitions_transport",
    "koszulness_certificate",
    "build_transport_graph",
    "formal_central_scalar_sum",
    "central_charge_conductor",
    "central_charge_conductor_catalog",
    "anomaly_ratio_catalog",
    "anomaly_ratio_transpose_relation",
    "cy3_candidate_catalog",
    "butson_analysis",
]
