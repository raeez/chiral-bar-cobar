"""Exact principal W-algebra conductor data for A1-A5 and exceptional types.

This module generalizes the type-A engines
`compute.lib.wn_central_charge_canonical` and
`compute.lib.alpha_n_conductor_engine` to the exceptional simple Lie types
G2, F4, E6, E7, E8 while keeping the repo's live type-A convention:

    c(W^k(g)) = rank(g) - dim(g) * h_dual * (k + h_dual - 1)^2 / (k + h_dual)
    k'        = -k - 2*h_dual

with exact `Fraction` arithmetic throughout.

Naming note:
  - The type-A engine `alpha_n_conductor_engine.py` calls `alpha_N` the
    central-charge complement c(k) + c(k').
  - The same file calls `K_WN` the kappa complementarity
    kappa(k) + kappa(k').

To avoid that ambiguity, this module exports both surfaces explicitly:

    koszul_conductor(type_name, k)
        = c(W^k(g)) + c(W^{k'}(g))

    kappa_complementarity(type_name, k)
        = kappa(W^k(g)) + kappa(W^{k'}(g))
        = varrho(g) * koszul_conductor(type_name, k)

where

    varrho(g) = sum_i 1 / (m_i + 1)

for principal W-algebras with exponents m_i.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, Mapping, Sequence

from compute.lib.wn_central_charge_canonical import c_wn_fl


@dataclass(frozen=True)
class PrincipalWLieData:
    """Minimal simple-Lie data needed for principal W conductor formulas."""

    type_name: str
    family: str
    rank: int
    dim_g: int
    h_dual: int
    exponents: tuple[int, ...]


TYPE_A_DATA: Dict[str, PrincipalWLieData] = {
    "A1": PrincipalWLieData(
        type_name="A1",
        family="A",
        rank=1,
        dim_g=3,
        h_dual=2,
        exponents=(1,),
    ),
    "A2": PrincipalWLieData(
        type_name="A2",
        family="A",
        rank=2,
        dim_g=8,
        h_dual=3,
        exponents=(1, 2),
    ),
    "A3": PrincipalWLieData(
        type_name="A3",
        family="A",
        rank=3,
        dim_g=15,
        h_dual=4,
        exponents=(1, 2, 3),
    ),
    "A4": PrincipalWLieData(
        type_name="A4",
        family="A",
        rank=4,
        dim_g=24,
        h_dual=5,
        exponents=(1, 2, 3, 4),
    ),
    "A5": PrincipalWLieData(
        type_name="A5",
        family="A",
        rank=5,
        dim_g=35,
        h_dual=6,
        exponents=(1, 2, 3, 4, 5),
    ),
}


EXCEPTIONAL_DATA: Dict[str, PrincipalWLieData] = {
    "G2": PrincipalWLieData(
        type_name="G2",
        family="G",
        rank=2,
        dim_g=14,
        h_dual=4,
        exponents=(1, 5),
    ),
    "F4": PrincipalWLieData(
        type_name="F4",
        family="F",
        rank=4,
        dim_g=52,
        h_dual=9,
        exponents=(1, 5, 7, 11),
    ),
    "E6": PrincipalWLieData(
        type_name="E6",
        family="E",
        rank=6,
        dim_g=78,
        h_dual=12,
        exponents=(1, 4, 5, 7, 8, 11),
    ),
    "E7": PrincipalWLieData(
        type_name="E7",
        family="E",
        rank=7,
        dim_g=133,
        h_dual=18,
        exponents=(1, 5, 7, 9, 11, 13, 17),
    ),
    "E8": PrincipalWLieData(
        type_name="E8",
        family="E",
        rank=8,
        dim_g=248,
        h_dual=30,
        exponents=(1, 7, 11, 13, 17, 19, 23, 29),
    ),
}


LIE_DATA: Dict[str, PrincipalWLieData] = {
    **TYPE_A_DATA,
    **EXCEPTIONAL_DATA,
}

TYPE_A_TYPES: tuple[str, ...] = tuple(TYPE_A_DATA)
EXCEPTIONAL_TYPES: tuple[str, ...] = tuple(EXCEPTIONAL_DATA)
ALL_SUPPORTED_TYPES: tuple[str, ...] = TYPE_A_TYPES + EXCEPTIONAL_TYPES

DEFAULT_K_VALUES: tuple[Fraction, ...] = (
    Fraction(-1),
    Fraction(0),
    Fraction(1),
    Fraction(2),
    Fraction(5),
)


def lie_data(type_name: str) -> PrincipalWLieData:
    """Return the stored Lie data for a supported principal W family."""

    try:
        return LIE_DATA[type_name]
    except KeyError as exc:
        supported = ", ".join(ALL_SUPPORTED_TYPES)
        raise KeyError(f"Unsupported type '{type_name}'. Supported: {supported}") from exc


def generator_weights(type_name: str) -> tuple[int, ...]:
    """Principal W generator weights: exponents + 1."""

    data = lie_data(type_name)
    return tuple(exponent + 1 for exponent in data.exponents)


def anomaly_ratio(type_name: str) -> Fraction:
    """varrho(g) = sum_i 1/(m_i + 1) for principal W(g)."""

    return sum(Fraction(1, exponent + 1) for exponent in lie_data(type_name).exponents)


def weyl_rho_squared(type_name: str) -> Fraction:
    """Freudenthal-de Vries value |rho|^2 = dim(g) * h_dual / 12."""

    data = lie_data(type_name)
    return Fraction(data.dim_g * data.h_dual, 12)


def dual_level(type_name: str, k: int | Fraction) -> Fraction:
    """Repo convention for the dual level: k' = -k - 2*h_dual."""

    data = lie_data(type_name)
    return -Fraction(k) - 2 * Fraction(data.h_dual)


def principal_w_central_charge(type_name: str, k: int | Fraction) -> Fraction:
    """Central charge c(W^k(g)) in the repo's canonical convention."""

    data = lie_data(type_name)
    k_fraction = Fraction(k)
    if k_fraction + data.h_dual == 0:
        raise ValueError(
            f"Critical level k = {-data.h_dual} is singular for {type_name}"
        )

    if data.family == "A":
        # A_r = sl_{r+1}, and the canonical type-A module is the source of truth.
        return c_wn_fl(data.rank + 1, k_fraction)

    shift = k_fraction + data.h_dual - 1
    return (
        Fraction(data.rank)
        - Fraction(data.dim_g * data.h_dual) * shift * shift / (k_fraction + data.h_dual)
    )


def principal_w_kappa(type_name: str, k: int | Fraction) -> Fraction:
    """kappa(W^k(g)) = varrho(g) * c(W^k(g))."""

    return anomaly_ratio(type_name) * principal_w_central_charge(type_name, k)


def expected_koszul_conductor(type_name: str) -> Fraction:
    """Closed form for c(k) + c(k') = 2*rank + 4*dim(g)*h_dual."""

    data = lie_data(type_name)
    return Fraction(2 * data.rank + 4 * data.dim_g * data.h_dual)


def koszul_conductor(type_name: str, k: int | Fraction) -> Fraction:
    """Central-charge complement c(W^k(g)) + c(W^{k'}(g))."""

    return principal_w_central_charge(type_name, k) + principal_w_central_charge(
        type_name, dual_level(type_name, k)
    )


def expected_kappa_complementarity(type_name: str) -> Fraction:
    """Closed form for kappa(k) + kappa(k') = varrho(g) * (c(k) + c(k'))."""

    return anomaly_ratio(type_name) * expected_koszul_conductor(type_name)


def kappa_complementarity(type_name: str, k: int | Fraction) -> Fraction:
    """kappa(W^k(g)) + kappa(W^{k'}(g))."""

    return principal_w_kappa(type_name, k) + principal_w_kappa(
        type_name, dual_level(type_name, k)
    )


def verify_k_independence(
    type_name: str,
    k_values: Sequence[int | Fraction] = DEFAULT_K_VALUES,
) -> dict[str, bool]:
    """Check that both complementarity sums are constant across `k_values`."""

    expected_c = expected_koszul_conductor(type_name)
    expected_kappa = expected_kappa_complementarity(type_name)
    checks: dict[str, bool] = {}
    for raw_k in k_values:
        k_value = Fraction(raw_k)
        checks[f"conductor@{k_value}"] = koszul_conductor(type_name, k_value) == expected_c
        checks[f"kappa@{k_value}"] = (
            kappa_complementarity(type_name, k_value) == expected_kappa
        )
    return checks


def export_koszul_conductors(
    type_names: Iterable[str] = ALL_SUPPORTED_TYPES,
) -> dict[str, Fraction]:
    """Export exact central-charge complements for the requested type names."""

    return {type_name: expected_koszul_conductor(type_name) for type_name in type_names}


def export_kappa_complementarities(
    type_names: Iterable[str] = ALL_SUPPORTED_TYPES,
) -> dict[str, Fraction]:
    """Export exact kappa complementarity sums for the requested type names."""

    return {
        type_name: expected_kappa_complementarity(type_name)
        for type_name in type_names
    }


def verify_all(
    type_names: Iterable[str] = ALL_SUPPORTED_TYPES,
    k_values: Sequence[int | Fraction] = DEFAULT_K_VALUES,
) -> dict[str, dict[str, bool]]:
    """Run the narrow consistency checks for each supported type."""

    results: dict[str, dict[str, bool]] = {}
    for type_name in type_names:
        data = lie_data(type_name)
        type_checks = verify_k_independence(type_name, k_values)
        type_checks["freudenthal_de_vries"] = (
            weyl_rho_squared(type_name) == Fraction(data.dim_g * data.h_dual, 12)
        )
        results[type_name] = type_checks
    return results


KOSZUL_CONDUCTORS: Mapping[str, Fraction] = export_koszul_conductors()
KAPPA_COMPLEMENTARITIES: Mapping[str, Fraction] = export_kappa_complementarities()

