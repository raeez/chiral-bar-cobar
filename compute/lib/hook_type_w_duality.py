r"""Exact hook-type ``W``-algebra data and typed comparison obligations.

This module is the compatibility surface for hook-type reductions in type A.
The canonical computations live in :mod:`non_principal_w_bar_engine`:

* Young-diagram transpose and orbit labels;
* ``sl_2``-centralizer generator weights, with every generator even;
* Kac--Roan--Wakimoto central charges in the standard level convention;
* the formal involution ``k -> -k-2N``.

Transpose is a theorem of partition combinatorics.  Its interpretation as a
Koszul target is conditional on ``H_hook^{DS/bar}``, a filtered BRST/bar
comparison together with strict completion and a perfect Verdier pairing.
The modular characteristic ``kappa``, its coefficient ``rho``, the modular
conductor, bar cohomology, same-family duality, and KSDual membership carry
typed open or conditional packets.

For Bershadsky--Polyakov, the exact scalar ledger remains convention-separated:
the standard FKR central charge has reflected sum ``50``; the shifted secondary
formula has reflected sum ``196``; the unsigned reciprocal-weight diagnostic is
``17/6``.  Modular promotion requires the genus-one and comparison packages
recorded by the typed claim surfaces.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import Rational, Symbol, cancel, simplify, sympify

from compute.lib.non_principal_w_bar_engine import (
    ClaimPacket,
    ClaimStatus,
    GeneratorSpec,
    OpenInvariantError,
    formal_level_reflection,
    type_a_krw_central_charge,
    type_a_krw_central_charge_data,
    type_a_strong_generators,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    ad_h_grade_multiplicities_sl_n,
    homogeneous_f_centralizer_basis_sl_n,
    hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)


k = Symbol("k")
H_HOOK_DS_BAR = (
    "H_hook^{DS/bar}: filtered BRST/bar comparison, strict completion, "
    "and a finite or continuously perfect Verdier pairing"
)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.OPEN, None, hypotheses=tuple(hypotheses))


def _conditional(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.CONDITIONAL, None, hypotheses=tuple(hypotheses))


@dataclass(frozen=True)
class WAlgebraGeneratorData:
    """Exact strong-generator and centralizer data for one type-A reduction."""

    lie_algebra: str
    rank: int
    partition: Partition
    transpose_partition: Partition
    orbit_class: str
    f_centralizer_dimension: int
    f_centralizer_grades: Dict[int, int]
    full_grading: Dict[int, int]
    strong_generators: Tuple[Tuple[str, object, str], ...]
    n_even: int
    n_odd: int

    @property
    def n_bosonic(self) -> int:
        """Compatibility alias for the even-generator count."""

        return self.n_even

    @property
    def n_fermionic(self) -> int:
        """Compatibility alias for the odd-generator count."""

        return self.n_odd


@dataclass(frozen=True)
class WAlgebraCentralCharge:
    """Exact KRW central-charge data with the source formula exposed."""

    partition: Partition
    N: int
    dim_g0: int
    dim_g_half: int
    rho_squared: object
    rho_L_squared: object
    x_diagonal: Tuple[object, ...]
    x_norm_squared: object
    positive_root_grades: Tuple[object, ...]
    charged_ghost_term: object
    central_charge: object
    source: str
    leading_term: object
    quadratic_coeff: object


@dataclass(frozen=True)
class HookDualityData:
    """Exact hook-pair arithmetic and typed categorical comparisons."""

    source_partition: Partition
    target_partition: Partition
    transpose_relation: bool
    source_generators: WAlgebraGeneratorData
    target_generators: WAlgebraGeneratorData
    source_central_charge: WAlgebraCentralCharge
    target_central_charge: WAlgebraCentralCharge
    formal_reflected_level: object
    formal_central_charge_sum: object
    source_kappa: ClaimPacket
    target_kappa: ClaimPacket
    kappa_sum: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def dual_level(self):
        """Compatibility alias for the formal reflected level."""

        return self.formal_reflected_level

    @property
    def c_sum(self):
        """Compatibility alias for the formal central-charge sum."""

        return self.formal_central_charge_sum


def weyl_vector_sl_n(N: int) -> Tuple[Rational, ...]:
    """Return the Weyl vector of ``sl_N`` in trace-form coordinates."""

    if N < 1:
        raise ValueError("N must be a positive integer")
    return tuple(Rational(N - 1 - 2 * index, 2) for index in range(N))


def weyl_vector_norm_squared_sl_n(N: int) -> Rational:
    """Return ``(rho|rho)=N(N^2-1)/12`` for ``sl_N``."""

    return Rational(N * (N * N - 1), 12)


def levi_rho_from_partition(partition: Partition) -> Tuple[Rational, ...]:
    """Return Weyl-vector coordinates for the grade-zero Levi factors."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    x_values = [Rational(triple.h[index, index], 2) for index in range(N)]
    multiplicities = Counter(x_values)
    coordinates = []
    for eigenvalue in sorted(multiplicities, reverse=True):
        coordinates.extend(weyl_vector_sl_n(multiplicities[eigenvalue]))
    return tuple(coordinates)


def levi_rho_norm_squared(partition: Partition) -> Rational:
    """Return the trace-form norm of the grade-zero Levi Weyl vector."""

    coordinates = levi_rho_from_partition(partition)
    return sum(value * value for value in coordinates)


def rho_shift_norm_squared(partition: Partition) -> Rational:
    """Return the exact difference ``(rho|rho)-(rho_0|rho_0)``."""

    N = partition_size(normalize_partition(partition))
    return weyl_vector_norm_squared_sl_n(N) - levi_rho_norm_squared(partition)


def w_algebra_generator_data(partition: Partition) -> WAlgebraGeneratorData:
    """Return exact centralizer grades, weights, and even parity."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    centralizer = homogeneous_f_centralizer_basis_sl_n(triple.f, triple.h)
    centralizer_grades = {grade: len(basis) for grade, basis in centralizer.items()}
    generators = type_a_strong_generators(lam)
    strong_generators = tuple(
        (generator.label, generator.conformal_weight, generator.parity)
        for generator in generators
    )
    return WAlgebraGeneratorData(
        lie_algebra=f"sl_{N}",
        rank=N - 1,
        partition=lam,
        transpose_partition=transpose_partition(lam),
        orbit_class=type_a_orbit_class(lam),
        f_centralizer_dimension=len(generators),
        f_centralizer_grades=centralizer_grades,
        full_grading=ad_h_grade_multiplicities_sl_n(triple.h),
        strong_generators=strong_generators,
        n_even=len(generators),
        n_odd=0,
    )


def krw_central_charge_data(partition: Partition) -> WAlgebraCentralCharge:
    """Return KRW (2003), Theorem 2.1(a), equation (2.6), data."""

    lam = normalize_partition(partition)
    N = partition_size(lam)
    canonical = type_a_krw_central_charge_data(lam, k)
    triple = type_a_partition_sl2_triple(lam)
    h_diagonal = [triple.h[index, index] for index in range(N)]
    dim_g0 = (N - 1) + sum(
        h_diagonal[left] == h_diagonal[right]
        for left in range(N)
        for right in range(N)
        if left != right
    )
    rho_squared = weyl_vector_norm_squared_sl_n(N)
    rho_L_squared = levi_rho_norm_squared(lam)
    return WAlgebraCentralCharge(
        partition=lam,
        N=N,
        dim_g0=dim_g0,
        dim_g_half=canonical.dim_g_half,
        rho_squared=rho_squared,
        rho_L_squared=rho_L_squared,
        x_diagonal=canonical.x_diagonal,
        x_norm_squared=canonical.x_norm_squared,
        positive_root_grades=canonical.positive_root_grades,
        charged_ghost_term=canonical.charged_ghost_term,
        central_charge=canonical.central_charge,
        source=canonical.source,
        leading_term=dim_g0 - Rational(canonical.dim_g_half, 2),
        quadratic_coeff=12 * (rho_squared - rho_L_squared),
    )


def _krw_per_root_pair(x_diag, N, level):
    """Evaluate the KRW formula from a good-grading diagonal."""

    kk = sympify(level)
    x_values = tuple(sympify(value) for value in x_diag)
    positive_grades = tuple(
        x_values[left] - x_values[right]
        for left in range(N)
        for right in range(N)
        if x_values[left] - x_values[right] > 0
    )
    x_norm = sum(value * value for value in x_values)
    dim_half = sum(grade == Rational(1, 2) for grade in positive_grades)
    ghost_term = sum(12 * grade**2 - 12 * grade + 2 for grade in positive_grades)
    return cancel(
        kk * (N * N - 1) / (kk + N)
        - 12 * kk * x_norm
        - ghost_term
        - Rational(dim_half, 2)
    )


def krw_central_charge(partition: Partition, level=k):
    """Return the exact standard-convention KRW central charge."""

    return type_a_krw_central_charge(partition, level)


def ghost_constant(partition: Partition) -> Rational:
    """Return ``sum_{j>0} j dim(g_j)`` for the good grading."""

    lam = normalize_partition(partition)
    triple = type_a_partition_sl2_triple(lam)
    N = partition_size(lam)
    x_diagonal = [Rational(triple.h[index, index], 2) for index in range(N)]
    return sum(
        x_diagonal[left] - x_diagonal[right]
        for left in range(N)
        for right in range(N)
        if x_diagonal[left] - x_diagonal[right] > 0
    )


def ghost_constant_hook(N: int, r: int) -> Rational:
    """Return the exact good-grading ghost sum for ``(N-r,1^r)``."""

    return ghost_constant(hook_partition(N, r))


def transpose_ghost_sum(partition: Partition) -> Rational:
    """Return the exact ghost sum of a partition and its transpose."""

    lam = normalize_partition(partition)
    return ghost_constant(lam) + ghost_constant(transpose_partition(lam))


def complementarity_constant(partition: Partition) -> Rational:
    """Compatibility alias for the signed transpose ghost sum."""

    return -transpose_ghost_sum(partition)


def reciprocal_weight_diagnostic_from_partition(partition: Partition) -> Rational:
    """Return the unsigned reciprocal sum of exact even-generator weights."""

    generators = type_a_strong_generators(normalize_partition(partition))
    return sum(Rational(1) / Rational(generator.conformal_weight) for generator in generators)


def anomaly_ratio_from_partition(partition: Partition) -> ClaimPacket:
    """Return the typed open ``rho`` packet for one partition."""

    lam = normalize_partition(partition)
    return _open(
        f"rho for W(sl_{partition_size(lam)}, f_{lam})",
        "a nonseparating genus-one calculation",
        "a theorem identifying rho with a specified modular channel",
    )


def ds_kappa_from_affine(partition: Partition, level=k) -> ClaimPacket:
    """Return the typed conditional DS/modular comparison packet."""

    lam = normalize_partition(partition)
    return _conditional(
        f"kappa of W^{sympify(level)}(sl_{partition_size(lam)}, f_{lam}) via DS",
        H_HOOK_DS_BAR,
        "a direct genus-one calculation on the reduced algebra",
    )


def kappa_complementarity_sum(partition: Partition, level=k) -> ClaimPacket:
    """Return the typed open modular-conductor packet."""

    lam = normalize_partition(partition)
    return _open(
        f"K^kappa for the transpose corridor of {lam}",
        "modular characteristics in a common convention at both formal reflected levels",
        H_HOOK_DS_BAR,
    )


def hook_dual_level_sl4(level=k):
    """Return the formal level reflection ``k -> -k-8``."""

    return formal_level_reflection(4, level)


def hook_dual_level_sl_n(N: int, level=k):
    """Return the formal level reflection ``k -> -k-2N``."""

    return formal_level_reflection(N, level)


def sl4_hook_211_generators() -> WAlgebraGeneratorData:
    return w_algebra_generator_data((2, 1, 1))


def sl4_hook_31_generators() -> WAlgebraGeneratorData:
    return w_algebra_generator_data((3, 1))


def sl4_22_generators() -> WAlgebraGeneratorData:
    return w_algebra_generator_data((2, 2))


def sl4_principal_generators() -> WAlgebraGeneratorData:
    return w_algebra_generator_data((4,))


def c_sl4_211(level=k):
    return krw_central_charge((2, 1, 1), level)


def c_sl4_31(level=k):
    return krw_central_charge((3, 1), level)


def c_sl4_22(level=k):
    return krw_central_charge((2, 2), level)


def c_sl4_principal(level=k):
    return krw_central_charge((4,), level)


def kappa_sl4_211(level=k) -> ClaimPacket:
    return ds_kappa_from_affine((2, 1, 1), level)


def kappa_sl4_31(level=k) -> ClaimPacket:
    return ds_kappa_from_affine((3, 1), level)


def kappa_sl4_22(level=k) -> ClaimPacket:
    return ds_kappa_from_affine((2, 2), level)


def kappa_sl4_principal(level=k) -> ClaimPacket:
    return ds_kappa_from_affine((4,), level)


def kappa_anti_symmetry_31_211(level=k) -> ClaimPacket:
    return kappa_complementarity_sum((3, 1), level)


def kappa_anti_symmetry_22(level=k) -> ClaimPacket:
    return kappa_complementarity_sum((2, 2), level)


def c_complementarity_22(level=k):
    """Return the formal central-charge sum for the self-transpose diagram."""

    kk = sympify(level)
    return simplify(c_sl4_22(kk) + c_sl4_22(hook_dual_level_sl4(kk)))


def c_complementarity_31_211(level=k):
    """Return the formal central-charge sum for the sl4 transpose pair."""

    kk = sympify(level)
    reflected = hook_dual_level_sl4(kk)
    return simplify(c_sl4_31(kk) + c_sl4_211(reflected))


def sl4_hook_duality_data(level=k) -> HookDualityData:
    """Return exact sl4 hook arithmetic and conditional comparison packets."""

    kk = sympify(level)
    reflected = hook_dual_level_sl4(kk)
    source = (3, 1)
    target = (2, 1, 1)
    return HookDualityData(
        source_partition=source,
        target_partition=target,
        transpose_relation=transpose_partition(source) == target,
        source_generators=w_algebra_generator_data(source),
        target_generators=w_algebra_generator_data(target),
        source_central_charge=krw_central_charge_data(source),
        target_central_charge=krw_central_charge_data(target),
        formal_reflected_level=reflected,
        formal_central_charge_sum=simplify(
            krw_central_charge(source, kk) + krw_central_charge(target, reflected)
        ),
        source_kappa=ds_kappa_from_affine(source, kk),
        target_kappa=ds_kappa_from_affine(target, reflected),
        kappa_sum=kappa_complementarity_sum(source, kk),
        ds_bar_commutation=_conditional("DS--bar commutation for the sl4 hook pair", H_HOOK_DS_BAR),
        koszul_duality=_conditional(
            "object-level Koszul comparison for the sl4 transpose pair",
            H_HOOK_DS_BAR,
        ),
        ksdual_membership=_open(
            "KSDual membership for the sl4 hook pair",
            "an object-level fixed-point equivalence",
        ),
    )


def bar_degree_one_generator_count(partition: Partition) -> int:
    """Return the number of cogenerators in bar filtration degree one."""

    return w_algebra_generator_data(partition).f_centralizer_dimension


def bar_cohomology_h0(partition: Partition) -> ClaimPacket:
    """Return the conditional connected-bar ``H^0`` packet."""

    lam = normalize_partition(partition)
    return _conditional(
        f"H^0 of the completed chiral bar complex for partition {lam}",
        "connected augmentation and convergence of the completed bar filtration",
    )


def bar_cohomology_h1_generators(partition: Partition) -> ClaimPacket:
    """Return the conditional comparison from degree-one cogenerators to ``H^1``."""

    lam = normalize_partition(partition)
    return _conditional(
        f"H^1 of the completed chiral bar complex for partition {lam}",
        "collapse of the degree-one edge map",
        H_HOOK_DS_BAR,
    )


def bar_cohomology_h2_estimate(partition: Partition) -> ClaimPacket:
    """Return the open arity-two bar-cohomology obligation."""

    lam = normalize_partition(partition)
    return _open(
        f"H^2 of the completed chiral bar complex for partition {lam}",
        "the full OPE differential with collision terms",
        "convergence and extension control",
    )


def hook_kappa_anti_symmetry_sl_n(N: int, r: int, level=k) -> ClaimPacket:
    """Return the open modular comparison packet for one hook transpose orbit."""

    return kappa_complementarity_sum(hook_partition(N, r), level)


def hook_kappa_anti_symmetry_catalog(max_N: int = 6, level=k) -> Dict[str, ClaimPacket]:
    """Return typed modular obligations for all hook partitions through ``sl_max_N``."""

    results: Dict[str, ClaimPacket] = {}
    for N in range(3, max_N + 1):
        for r in range(1, N - 1):
            lam = hook_partition(N, r)
            results[f"sl_{N}:{lam}->{transpose_partition(lam)}"] = (
                hook_kappa_anti_symmetry_sl_n(N, r, level)
            )
    return results


def verify_hook_type_w_duality() -> Dict[str, object]:
    """Return an exact arithmetic audit and typed categorical obligations."""

    source = (3, 1)
    target = (2, 1, 1)
    data = sl4_hook_duality_data(k)
    return {
        "transpose_relation": transpose_partition(source) == target,
        "transpose_involution": transpose_partition(target) == source,
        "source_generator_count": data.source_generators.f_centralizer_dimension == 5,
        "target_generator_count": data.target_generators.f_centralizer_dimension == 9,
        "all_source_generators_even": data.source_generators.n_odd == 0,
        "all_target_generators_even": data.target_generators.n_odd == 0,
        "central_charge_source_matches_krw": simplify(
            data.source_central_charge.central_charge - krw_central_charge(source)
        ) == 0,
        "central_charge_target_matches_krw": simplify(
            data.target_central_charge.central_charge - krw_central_charge(target)
        ) == 0,
        "formal_reflection_is_involutive": simplify(
            hook_dual_level_sl4(data.formal_reflected_level) - k
        ) == 0,
        "ds_bar_commutation": data.ds_bar_commutation,
        "koszul_duality": data.koszul_duality,
        "ksdual_membership": data.ksdual_membership,
        "modular_conductor": data.kappa_sum,
    }


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "WAlgebraGeneratorData",
    "WAlgebraCentralCharge",
    "HookDualityData",
    "weyl_vector_sl_n",
    "weyl_vector_norm_squared_sl_n",
    "levi_rho_from_partition",
    "levi_rho_norm_squared",
    "rho_shift_norm_squared",
    "w_algebra_generator_data",
    "krw_central_charge_data",
    "krw_central_charge",
    "ghost_constant",
    "ghost_constant_hook",
    "transpose_ghost_sum",
    "complementarity_constant",
    "reciprocal_weight_diagnostic_from_partition",
    "anomaly_ratio_from_partition",
    "ds_kappa_from_affine",
    "kappa_complementarity_sum",
    "hook_dual_level_sl4",
    "hook_dual_level_sl_n",
    "sl4_hook_211_generators",
    "sl4_hook_31_generators",
    "sl4_22_generators",
    "sl4_principal_generators",
    "c_sl4_211",
    "c_sl4_31",
    "c_sl4_22",
    "c_sl4_principal",
    "kappa_sl4_211",
    "kappa_sl4_31",
    "kappa_sl4_22",
    "kappa_sl4_principal",
    "kappa_anti_symmetry_31_211",
    "kappa_anti_symmetry_22",
    "c_complementarity_22",
    "c_complementarity_31_211",
    "sl4_hook_duality_data",
    "bar_degree_one_generator_count",
    "bar_cohomology_h0",
    "bar_cohomology_h1_generators",
    "bar_cohomology_h2_estimate",
    "hook_kappa_anti_symmetry_sl_n",
    "hook_kappa_anti_symmetry_catalog",
    "verify_hook_type_w_duality",
]
