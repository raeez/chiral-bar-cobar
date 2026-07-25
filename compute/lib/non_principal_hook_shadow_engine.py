r"""Exact hook-family arithmetic with typed shadow and transport claims.

For ``W^k(sl_N,f_(N-m,1^m))`` this engine computes the hook partition,
transpose, strong-generator weights, even parity, KRW central charge, formal
level reflection, reciprocal-weight diagnostic, and formal central scalar sum.
For the Bershadsky--Polyakov hook it also exposes the primary-source OPE pole
orders, the standard reflected sum ``50``, and the shifted secondary sum
``196``.

The modular characteristic, ``rho``, modular conductor, higher shadow
coefficients, full shadow depth, DS cascade, collision extraction, categorical
transport, bar comparison, duality, and KSDual membership return open or
conditional :class:`ClaimPacket` objects with named packages.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify

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
    reciprocal_weight_diagnostic_from_partition,
    w_algebra_generator_data,
)
from compute.lib.non_principal_w_bar_engine import (
    bershadsky_polyakov_ope_data,
    bershadsky_polyakov_shifted_central_charge,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    hook_partition,
    normalize_partition,
    transpose_partition,
    type_a_orbit_class,
)


k = Symbol("k")
H_HOOK_SHADOW = (
    "H_hook-shadow: every generator channel in the Maurer--Cartan tower, "
    "collision normalization, convergence, and reconstruction from restrictions"
)
H_DS_CASCADE = (
    "H_DS-cascade: filtered DS comparison for every shadow coefficient and "
    "strict compatibility with completion"
)
H_HOOK_TRANSPORT = (
    "H_hook-transport: realized inverse-reduction functors and compatibility "
    "with DS, bar, completion, and Verdier duality"
)
H_KSDUAL = (
    "H_KSDual: object-level fixed-point equivalence compatible with the hook "
    "transport and DS/bar packages"
)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.OPEN, None, hypotheses=tuple(hypotheses))


def _conditional(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.CONDITIONAL, None, hypotheses=tuple(hypotheses))


def _virasoro_shadow_coefficients(c_val, max_arity: int = 10) -> ClaimPacket:
    """Return the open higher-shadow packet for a Virasoro restriction."""

    return _open(
        f"Virasoro-restriction shadow coefficients through arity {max_arity} at c={sympify(c_val)}",
        H_HOOK_SHADOW,
    )


@dataclass(frozen=True)
class HookShadowProfile:
    """Exact hook data with typed modular and full-shadow fields."""

    N: int
    m: int
    partition: Partition
    transpose: Partition
    is_self_transpose: bool
    orbit_class: str
    generator_weights: Tuple[Rational, ...]
    num_generators: int
    num_even: int
    num_odd: int
    weight_one_count: int
    max_weight: Rational
    central_charge: object
    formal_reflected_level: object
    formal_central_sum: object
    formal_central_sum_k_independent: bool
    shifted_secondary_sum: object
    reciprocal_weight_diagnostic: Rational
    exact_ope_pole_orders: Tuple[Tuple[str, str, int], ...]
    rho: ClaimPacket
    kappa: ClaimPacket
    modular_conductor: ClaimPacket
    ope_completion: ClaimPacket
    full_shadow_depth: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def num_bosonic(self) -> int:
        return self.num_even

    @property
    def num_fermionic(self) -> int:
        return self.num_odd

    @property
    def anomaly_ratio(self) -> ClaimPacket:
        return self.rho


@dataclass(frozen=True)
class HookShadowMetric:
    """Typed higher-shadow metric obligations for one exact hook profile."""

    profile: HookShadowProfile
    quadratic_coefficient: ClaimPacket
    quartic_coefficient: ClaimPacket
    discriminant: ClaimPacket
    growth_rate: ClaimPacket


@dataclass(frozen=True)
class DSCascadeResult:
    """Exact source/target indices and a conditional DS shadow cascade."""

    source_partition: Partition
    target_partition: Partition
    source_central_charge: object
    target_central_charge: object
    cascade: ClaimPacket
    depth_comparison: ClaimPacket
    ds_bar_commutation: ClaimPacket


@dataclass(frozen=True)
class TransportToTransposeEvidence:
    """Exact transpose arithmetic and typed categorical transport."""

    N: int
    m: int
    partition: Partition
    transpose: Partition
    transpose_involution: bool
    formal_reflected_level: object
    formal_central_sum: object
    formal_central_sum_k_independent: bool
    source_diagnostic: Rational
    target_diagnostic: Rational
    source_kappa: ClaimPacket
    target_kappa: ClaimPacket
    modular_conductor: ClaimPacket
    transport: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket


def _bp_ope_poles() -> Tuple[Tuple[str, str, int], ...]:
    ope = bershadsky_polyakov_ope_data(k)
    return tuple(
        (left, right, max((term.pole_order for term in terms), default=0))
        for left, right, terms in ope.singular_products
    )


def hook_shadow_profile(N: int, m: int, max_arity: int = 8) -> HookShadowProfile:
    """Return exact hook arithmetic and typed frontier claims."""

    if not 0 <= m <= N - 2:
        raise ValueError(f"m must satisfy 0 <= m <= N-2={N-2}, got m={m}")
    lam = hook_partition(N, m)
    lam_t = transpose_partition(lam)
    generators = w_algebra_generator_data(lam)
    weights = tuple(sorted(Rational(weight) for _, weight, _ in generators.strong_generators))
    central_charge = krw_central_charge(lam, k)
    reflected = hook_dual_level_sl_n(N, k)
    reflected_central_charge = krw_central_charge(lam_t, reflected)
    central_sum = simplify(central_charge + reflected_central_charge)
    central_constant = simplify(central_sum.diff(k)) == 0
    is_bp = lam == (2, 1) and N == 3
    shifted_sum = None
    if is_bp:
        shifted_sum = simplify(
            bershadsky_polyakov_shifted_central_charge(k)
            + bershadsky_polyakov_shifted_central_charge(reflected)
        )
    return HookShadowProfile(
        N=N,
        m=m,
        partition=lam,
        transpose=lam_t,
        is_self_transpose=lam == lam_t,
        orbit_class=type_a_orbit_class(lam),
        generator_weights=weights,
        num_generators=generators.f_centralizer_dimension,
        num_even=generators.n_even,
        num_odd=generators.n_odd,
        weight_one_count=sum(weight == Rational(1) for weight in weights),
        max_weight=max(weights),
        central_charge=central_charge,
        formal_reflected_level=reflected,
        formal_central_sum=central_sum,
        formal_central_sum_k_independent=central_constant,
        shifted_secondary_sum=shifted_sum,
        reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(lam),
        exact_ope_pole_orders=_bp_ope_poles() if is_bp else (),
        rho=anomaly_ratio_from_partition(lam),
        kappa=ds_kappa_from_affine(lam, k),
        modular_conductor=kappa_complementarity_sum(lam, k),
        ope_completion=_open(
            f"complete OPE coefficients for hook partition {lam}",
            "primary-source formulas or a direct BRST OPE computation",
        ) if not is_bp else ClaimPacket(
            statement="primary BP singular OPE surface",
            status=ClaimStatus.PROVED_ELSEWHERE,
            value=bershadsky_polyakov_ope_data(k),
            evidence=("Fehily--Kawasetsu--Ridout (2021), equation (2.1)",),
        ),
        full_shadow_depth=_open(
            f"full shadow depth for hook partition {lam}",
            H_HOOK_SHADOW,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar commutation for hook partition {lam}",
            H_HOOK_DS_BAR,
        ),
        koszul_duality=_conditional(
            f"object-level Koszul comparison with transpose {lam_t}",
            H_HOOK_TRANSPORT,
            H_HOOK_DS_BAR,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for hook partition {lam}",
            H_KSDUAL,
        ),
    )


def hook_shadow_metric(N: int, m: int) -> HookShadowMetric:
    """Return typed higher-shadow metric obligations."""

    profile = hook_shadow_profile(N, m)
    return HookShadowMetric(
        profile=profile,
        quadratic_coefficient=_open("quadratic shadow coefficient", H_HOOK_SHADOW),
        quartic_coefficient=_open("quartic shadow coefficient", H_HOOK_SHADOW),
        discriminant=_open("shadow discriminant", H_HOOK_SHADOW),
        growth_rate=_open("shadow growth rate", H_HOOK_SHADOW),
    )


def hook_shadow_metric_numerical(N: int, m: int, level_val) -> Dict[str, object]:
    """Return exact central specialization and typed metric fields."""

    metric = hook_shadow_metric(N, m)
    return {
        "partition": metric.profile.partition,
        "level": Rational(level_val),
        "central_charge": simplify(metric.profile.central_charge.subs(k, level_val)),
        "quadratic_coefficient": metric.quadratic_coefficient,
        "quartic_coefficient": metric.quartic_coefficient,
        "discriminant": metric.discriminant,
        "growth_rate": metric.growth_rate,
    }


def ds_cascade_check(N: int, m: int, max_arity: int = 6) -> DSCascadeResult:
    """Return exact hook indices and the conditional DS shadow cascade."""

    source = hook_shadow_profile(N, m, max_arity)
    target_m = min(m + 1, N - 2)
    target = hook_shadow_profile(N, target_m, max_arity)
    return DSCascadeResult(
        source_partition=source.partition,
        target_partition=target.partition,
        source_central_charge=source.central_charge,
        target_central_charge=target.central_charge,
        cascade=_conditional(
            f"DS shadow cascade from {source.partition} to {target.partition}",
            H_DS_CASCADE,
        ),
        depth_comparison=_open(
            f"full shadow-depth comparison from {source.partition} to {target.partition}",
            H_HOOK_SHADOW,
            H_DS_CASCADE,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar comparison along {source.partition}->{target.partition}",
            H_HOOK_DS_BAR,
        ),
    )


def ds_cascade_numerical(N: int, m: int, level_val, max_arity: int = 6) -> Dict[str, object]:
    """Return exact central specializations and typed cascade claims."""

    cascade = ds_cascade_check(N, m, max_arity)
    return {
        "source_partition": cascade.source_partition,
        "target_partition": cascade.target_partition,
        "source_central_charge": simplify(cascade.source_central_charge.subs(k, level_val)),
        "target_central_charge": simplify(cascade.target_central_charge.subs(k, level_val)),
        "cascade": cascade.cascade,
        "depth_comparison": cascade.depth_comparison,
    }


def transport_to_transpose_check(
    N: int,
    m: int,
    level=k,
    test_levels=None,
) -> TransportToTransposeEvidence:
    """Return exact transpose/scalar data and typed transport comparisons."""

    profile = hook_shadow_profile(N, m)
    level_symbol = sympify(level)
    reflected = hook_dual_level_sl_n(N, level_symbol)
    c_source = krw_central_charge(profile.partition, level_symbol)
    c_target = krw_central_charge(profile.transpose, reflected)
    central_sum = simplify(c_source + c_target)
    return TransportToTransposeEvidence(
        N=N,
        m=m,
        partition=profile.partition,
        transpose=profile.transpose,
        transpose_involution=transpose_partition(profile.transpose) == profile.partition,
        formal_reflected_level=reflected,
        formal_central_sum=central_sum,
        formal_central_sum_k_independent=simplify(central_sum.diff(level_symbol)) == 0,
        source_diagnostic=reciprocal_weight_diagnostic_from_partition(profile.partition),
        target_diagnostic=reciprocal_weight_diagnostic_from_partition(profile.transpose),
        source_kappa=ds_kappa_from_affine(profile.partition, level_symbol),
        target_kappa=ds_kappa_from_affine(profile.transpose, reflected),
        modular_conductor=kappa_complementarity_sum(profile.partition, level_symbol),
        transport=_conditional(
            f"categorical transport from {profile.partition} to {profile.transpose}",
            H_HOOK_TRANSPORT,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar comparison for {profile.partition}",
            H_HOOK_DS_BAR,
        ),
        koszul_duality=_conditional(
            f"object-level Koszul comparison for {profile.partition}",
            H_HOOK_TRANSPORT,
            H_HOOK_DS_BAR,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for {profile.partition}",
            H_KSDUAL,
        ),
    )


def hook_kappa_multi_path(N: int, m: int, test_levels=None) -> ClaimPacket:
    """Return the open independent modular-verification obligation."""

    lam = hook_partition(N, m)
    return _open(
        f"independent verification of kappa for hook partition {lam}",
        "a genus-one calculation",
        "a categorical comparison theorem",
        "an independent specialization or literature value",
    )


def hook_shadow_tower_landscape(N: int, level_val, max_arity: int = 6) -> List[Dict[str, object]]:
    """Return exact central specializations and typed shadow packets for all hooks."""

    return [
        {
            "partition": profile.partition,
            "m": m,
            "central_charge": simplify(profile.central_charge.subs(k, level_val)),
            "reciprocal_weight_diagnostic": profile.reciprocal_weight_diagnostic,
            "rho": profile.rho,
            "kappa": profile.kappa,
            "shadow_tower": _virasoro_shadow_coefficients(profile.central_charge, max_arity),
            "full_shadow_depth": profile.full_shadow_depth,
        }
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m, max_arity),)
    ]


def hook_shadow_depth_table(max_N: int = 8) -> List[Dict[str, object]]:
    """Return exact hook ledgers and open full-depth fields through ``max_N``."""

    return [
        {
            "N": N,
            "m": m,
            "partition": profile.partition,
            "transpose": profile.transpose,
            "is_self_transpose": profile.is_self_transpose,
            "central_charge": profile.central_charge,
            "num_generators": profile.num_generators,
            "num_even": profile.num_even,
            "num_odd": profile.num_odd,
            "rho": profile.rho,
            "kappa": profile.kappa,
            "full_shadow_depth": profile.full_shadow_depth,
        }
        for N in range(3, max_N + 1)
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m),)
    ]


def hook_generator_spectrum(N: int, m: int) -> Dict[str, object]:
    """Return exact even-generator weights and the open ``rho`` field."""

    profile = hook_shadow_profile(N, m)
    weight_distribution: Dict[Rational, Dict[str, int]] = {}
    contributions = []
    for index, weight in enumerate(profile.generator_weights, start=1):
        weight_distribution.setdefault(weight, {"even": 0, "odd": 0})["even"] += 1
        contributions.append((f"generator_{index}", Rational(1) / weight))
    return {
        "partition": profile.partition,
        "N": N,
        "m": m,
        "total_generators": profile.num_generators,
        "n_even": profile.num_even,
        "n_odd": profile.num_odd,
        "weight_distribution": weight_distribution,
        "reciprocal_weight_contributions": tuple(contributions),
        "reciprocal_weight_diagnostic": profile.reciprocal_weight_diagnostic,
        "rho": profile.rho,
        "generator_weights": profile.generator_weights,
    }


def principal_limit_check(N: int) -> Dict[str, object]:
    """Return exact principal-hook arithmetic and typed derived fields."""

    profile = hook_shadow_profile(N, 0)
    return {
        "N": N,
        "partition": profile.partition,
        "is_principal": profile.partition == (N,),
        "central_charge_matches_krw": simplify(
            profile.central_charge - krw_central_charge((N,), k)
        ) == 0,
        "num_generators": profile.num_generators,
        "expected_generators": N - 1,
        "generators_match": profile.num_generators == N - 1,
        "rho": profile.rho,
        "kappa": profile.kappa,
        "full_shadow_depth": profile.full_shadow_depth,
    }


def subregular_hook_check(N: int) -> Dict[str, object]:
    """Return exact data for the subregular hook ``(N-1,1)``."""

    profile = hook_shadow_profile(N, 1)
    return {
        "N": N,
        "partition": profile.partition,
        "is_subregular": profile.partition == (N - 1, 1),
        "transpose": profile.transpose,
        "num_generators": profile.num_generators,
        "rho": profile.rho,
        "full_shadow_depth": profile.full_shadow_depth,
    }


def minimal_hook_check(N: int) -> Dict[str, object]:
    """Return exact data for the minimal hook ``(2,1^(N-2))``."""

    profile = hook_shadow_profile(N, N - 2)
    return {
        "N": N,
        "m": N - 2,
        "partition": profile.partition,
        "is_minimal": profile.partition == (2,) + (1,) * (N - 2),
        "transpose": profile.transpose,
        "transpose_is_subregular": profile.transpose == (N - 1, 1),
        "num_generators": profile.num_generators,
        "rho": profile.rho,
        "full_shadow_depth": profile.full_shadow_depth,
    }


def hook_landscape(N: int, max_arity: int = 6) -> Dict[str, object]:
    """Return exact hook profiles, transpose orbits, and typed transport claims."""

    profiles = [hook_shadow_profile(N, m, max_arity) for m in range(N - 1)]
    seen = set()
    transpose_orbits = []
    for profile in profiles:
        if profile.partition in seen:
            continue
        seen.add(profile.partition)
        seen.add(profile.transpose)
        transpose_orbits.append({
            "type": "self-transpose" if profile.partition == profile.transpose else "transpose-pair",
            "partition": profile.partition,
            "transpose": profile.transpose,
            "duality": profile.koszul_duality,
        })
    return {
        "N": N,
        "num_hooks": N - 1,
        "profiles": profiles,
        "transpose_orbits": transpose_orbits,
        "transport_evidence": [transport_to_transpose_check(N, m) for m in range(N - 1)],
    }


def hook_anomaly_ratio_table(max_N: int = 8) -> List[Dict[str, object]]:
    """Compatibility table separating diagnostics from open ``rho`` packets."""

    return [
        {
            "N": N,
            "m": m,
            "partition": profile.partition,
            "reciprocal_weight_diagnostic": profile.reciprocal_weight_diagnostic,
            "rho": profile.rho,
            "num_generators": profile.num_generators,
            "num_even": profile.num_even,
            "num_odd": profile.num_odd,
        }
        for N in range(3, max_N + 1)
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m),)
    ]


def hook_complementarity_constants(max_N: int = 8) -> List[Dict[str, object]]:
    """Return typed modular-conductor obligations for every hook."""

    return [
        {
            "N": N,
            "m": m,
            "partition": profile.partition,
            "transpose": profile.transpose,
            "modular_conductor": profile.modular_conductor,
        }
        for N in range(3, max_N + 1)
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m),)
    ]


def hook_c_conductor_table(max_N: int = 8) -> List[Dict[str, object]]:
    """Return exact formal central scalar sums for every hook."""

    return [
        {
            "N": N,
            "m": m,
            "partition": profile.partition,
            "transpose": profile.transpose,
            "central_sum": profile.formal_central_sum,
            "central_sum_k_independent": profile.formal_central_sum_k_independent,
        }
        for N in range(3, max_N + 1)
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m),)
    ]


def hook_quintic_shadow(N: int, m: int) -> Dict[str, object]:
    """Return the typed quintic-shadow obligation for one hook."""

    profile = hook_shadow_profile(N, m)
    return {
        "partition": profile.partition,
        "quintic_shadow": _open(
            f"quintic shadow coefficient for {profile.partition}",
            H_HOOK_SHADOW,
        ),
    }


def hook_shadow_growth_landscape(N: int, level_val) -> List[Dict[str, object]]:
    """Return exact central specializations and open growth-rate fields."""

    return [
        {
            "partition": profile.partition,
            "m": m,
            "central_charge": simplify(profile.central_charge.subs(k, level_val)),
            "growth_rate": _open(
                f"shadow growth rate for {profile.partition} at level {level_val}",
                H_HOOK_SHADOW,
            ),
        }
        for m in range(N - 1)
        for profile in (hook_shadow_profile(N, m),)
    ]


def hook_cross_family_consistency(N: int) -> Dict[str, object]:
    """Return exact family checks and typed modular/shadow obligations."""

    profiles = [hook_shadow_profile(N, m) for m in range(N - 1)]
    return {
        "N": N,
        "all_generators_even": all(profile.num_odd == 0 for profile in profiles),
        "all_transposes_involutive": all(
            transpose_partition(profile.transpose) == profile.partition for profile in profiles
        ),
        "principal_limit": principal_limit_check(N),
        "modular_claims": tuple(profile.modular_conductor for profile in profiles),
        "full_shadow_claims": tuple(profile.full_shadow_depth for profile in profiles),
        "transport_claims": tuple(profile.koszul_duality for profile in profiles),
    }


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "HookShadowProfile",
    "HookShadowMetric",
    "DSCascadeResult",
    "TransportToTransposeEvidence",
    "hook_shadow_profile",
    "hook_shadow_metric",
    "hook_shadow_metric_numerical",
    "ds_cascade_check",
    "ds_cascade_numerical",
    "transport_to_transpose_check",
    "hook_kappa_multi_path",
    "hook_shadow_tower_landscape",
    "hook_shadow_depth_table",
    "hook_generator_spectrum",
    "principal_limit_check",
    "subregular_hook_check",
    "minimal_hook_check",
    "hook_landscape",
    "hook_anomaly_ratio_table",
    "hook_complementarity_constants",
    "hook_c_conductor_table",
    "hook_quintic_shadow",
    "hook_shadow_growth_landscape",
    "hook_cross_family_consistency",
]
