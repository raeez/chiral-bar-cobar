"""Niemeier lattice VOA depth engine for the BB3 rank-24 arithmetic claim.

Scope lock:
    This module verifies the specific BB3 depth formula

        d(V_Lambda) = 3 + dim S_{r/2}(SL_2(Z))

    for even unimodular lattices of rank r, and applies it to the 24 Niemeier
    lattices at rank 24. In this convention, every Niemeier lattice has depth 4.

    The module is intentionally narrow. It does not replace the separate class-G
    shadow-tower calculations elsewhere in the repo; it isolates the rank-24
    arithmetic depth statement requested for the compute layer.

Verification paths implemented here:
    1. Standard dimension formula for S_k(SL_2(Z)).
    2. Ring-theoretic count from M_* = C[E_4, E_6] and S_k = Delta * M_{k-12}.
    3. Explicit Delta = eta^24 q-expansion plus the level-1 Sturm bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb
from typing import Dict, Iterable, Tuple


E12_Q1_COEFFICIENT = Fraction(65520, 691)


@dataclass(frozen=True)
class RootComponent:
    """A simply-laced root-system factor in a Niemeier root lattice."""

    family: str
    rank: int


@dataclass(frozen=True)
class NiemeierLattice:
    """One of the 24 positive-definite even unimodular lattices of rank 24."""

    label: str
    root_system: str
    components: Tuple[RootComponent, ...]

    @property
    def rank(self) -> int:
        return 24

    @property
    def root_count(self) -> int:
        return sum(root_count(component.family, component.rank) for component in self.components)

    @property
    def has_roots(self) -> bool:
        return self.root_count > 0


@dataclass(frozen=True)
class Weight12CuspVerification:
    """Independent checks that dim S_12(SL_2(Z)) = 1."""

    dimension_formula_value: int
    ring_theory_value: int
    sturm_bound: int
    delta_generator: str
    delta_qexp_prefix: Tuple[int, ...]
    delta_vanishing_order: int
    unique_by_sturm: bool
    verification_paths: Tuple[str, ...]

    @property
    def is_verified(self) -> bool:
        return (
            self.dimension_formula_value == 1
            and self.ring_theory_value == 1
            and self.sturm_bound == 1
            and self.delta_vanishing_order == 1
            and self.delta_qexp_prefix[:3] == (1, -24, 252)
            and self.unique_by_sturm
        )


@dataclass(frozen=True)
class NiemeierDepthRecord:
    """Arithmetic depth data for one Niemeier lattice in the BB3 convention."""

    label: str
    root_system: str
    rank: int
    half_rank_weight: int
    dim_s_half_rank: int
    depth: int
    cusp_generator: str
    cusp_coefficient: Fraction
    root_count: int
    theta_q1_coefficient: int
    mechanism_kind: str
    mechanism_summary: str
    verification_paths: Tuple[str, ...]


def _repeat_component(family: str, rank: int, multiplicity: int) -> Tuple[RootComponent, ...]:
    return tuple(RootComponent(family, rank) for _ in range(multiplicity))


NIEMEIER_LATTICES: Tuple[NiemeierLattice, ...] = (
    NiemeierLattice("D24", "D24", (RootComponent("D", 24),)),
    NiemeierLattice("D16+E8", "D16+E8", (RootComponent("D", 16), RootComponent("E", 8))),
    NiemeierLattice("E8^3", "E8^3", _repeat_component("E", 8, 3)),
    NiemeierLattice("A24", "A24", (RootComponent("A", 24),)),
    NiemeierLattice("D12^2", "D12^2", _repeat_component("D", 12, 2)),
    NiemeierLattice("A17+E7", "A17+E7", (RootComponent("A", 17), RootComponent("E", 7))),
    NiemeierLattice(
        "D10+E7^2",
        "D10+E7^2",
        (RootComponent("D", 10), RootComponent("E", 7), RootComponent("E", 7)),
    ),
    NiemeierLattice("A15+D9", "A15+D9", (RootComponent("A", 15), RootComponent("D", 9))),
    NiemeierLattice("D8^3", "D8^3", _repeat_component("D", 8, 3)),
    NiemeierLattice("A12^2", "A12^2", _repeat_component("A", 12, 2)),
    NiemeierLattice(
        "A11+D7+E6",
        "A11+D7+E6",
        (RootComponent("A", 11), RootComponent("D", 7), RootComponent("E", 6)),
    ),
    NiemeierLattice("E6^4", "E6^4", _repeat_component("E", 6, 4)),
    NiemeierLattice("A9^2+D6", "A9^2+D6", (RootComponent("A", 9), RootComponent("A", 9), RootComponent("D", 6))),
    NiemeierLattice("D6^4", "D6^4", _repeat_component("D", 6, 4)),
    NiemeierLattice("A8^3", "A8^3", _repeat_component("A", 8, 3)),
    NiemeierLattice(
        "A7^2+D5^2",
        "A7^2+D5^2",
        (RootComponent("A", 7), RootComponent("A", 7), RootComponent("D", 5), RootComponent("D", 5)),
    ),
    NiemeierLattice("A6^4", "A6^4", _repeat_component("A", 6, 4)),
    NiemeierLattice(
        "A5^4+D4",
        "A5^4+D4",
        _repeat_component("A", 5, 4) + (RootComponent("D", 4),),
    ),
    NiemeierLattice("D4^6", "D4^6", _repeat_component("D", 4, 6)),
    NiemeierLattice("A4^6", "A4^6", _repeat_component("A", 4, 6)),
    NiemeierLattice("A3^8", "A3^8", _repeat_component("A", 3, 8)),
    NiemeierLattice("A2^12", "A2^12", _repeat_component("A", 2, 12)),
    NiemeierLattice("A1^24", "A1^24", _repeat_component("A", 1, 24)),
    NiemeierLattice("Leech", "Leech", ()),
)
assert len(NIEMEIER_LATTICES) == 24

NIEMEIER_BY_LABEL: Dict[str, NiemeierLattice] = {
    lattice.label: lattice for lattice in NIEMEIER_LATTICES
}


def root_count(family: str, rank: int) -> int:
    """Return the number of roots in a simple ADE root system."""
    if family == "A":
        return rank * (rank + 1)
    if family == "D":
        return 2 * rank * (rank - 1)
    if family == "E":
        exceptional = {6: 72, 7: 126, 8: 240}
        if rank in exceptional:
            return exceptional[rank]
    raise ValueError(f"unsupported root system {family}{rank}")


def dim_cusp_forms_formula(weight: int) -> int:
    """Return dim S_weight(SL_2(Z)) from the standard full-level formula."""
    if weight < 2 or weight % 2 != 0:
        return 0
    if weight < 12:
        return 0
    if weight % 12 == 2:
        return weight // 12 - 1
    return weight // 12


def modular_form_monomial_basis(weight: int) -> Tuple[Tuple[int, int], ...]:
    """List the E4^a E6^b monomials of total weight ``weight``."""
    if weight < 0 or weight % 2 != 0:
        return ()
    basis = []
    for exponent_e6 in range(weight // 6 + 1):
        remaining = weight - 6 * exponent_e6
        if remaining % 4 == 0:
            basis.append((remaining // 4, exponent_e6))
    return tuple(basis)


def dim_modular_forms_via_ring(weight: int) -> int:
    """Return dim M_weight(SL_2(Z)) from M_* = C[E4, E6]."""
    if weight < 0 or weight % 2 != 0:
        return 0
    if weight == 0:
        return 1
    return len(modular_form_monomial_basis(weight))


def dim_cusp_forms_via_ring(weight: int) -> int:
    """Return dim S_weight(SL_2(Z)) using S_k = Delta * M_{k-12}."""
    if weight < 12 or weight % 2 != 0:
        return 0
    return dim_modular_forms_via_ring(weight - 12)


def sturm_bound_level_one(weight: int) -> int:
    """Return the level-1 Sturm bound for holomorphic modular forms of weight k."""
    if weight < 0 or weight % 2 != 0:
        raise ValueError("weight must be a nonnegative even integer")
    return weight // 12


def _convolve_truncated(left: Iterable[int], right: Iterable[int], max_power: int) -> Tuple[int, ...]:
    left_tuple = tuple(left)
    right_tuple = tuple(right)
    output = [0] * (max_power + 1)
    for left_power, left_coeff in enumerate(left_tuple):
        if left_coeff == 0:
            continue
        for right_power, right_coeff in enumerate(right_tuple):
            if right_coeff == 0:
                continue
            total_power = left_power + right_power
            if total_power > max_power:
                break
            output[total_power] += left_coeff * right_coeff
    return tuple(output)


@lru_cache(maxsize=None)
def eta24_product_coefficients(max_power: int) -> Tuple[int, ...]:
    """Return coefficients of prod_{n>=1} (1 - q^n)^24 through q^max_power."""
    if max_power < 0:
        raise ValueError("max_power must be nonnegative")
    coefficients = (1,) + (0,) * max_power
    for n in range(1, max_power + 1):
        factor = [0] * (max_power + 1)
        max_j = min(24, max_power // n)
        for j in range(max_j + 1):
            factor[j * n] = comb(24, j) * ((-1) ** j)
        coefficients = _convolve_truncated(coefficients, factor, max_power)
    return coefficients


@lru_cache(maxsize=None)
def ramanujan_delta_qexp(max_exponent: int) -> Dict[int, int]:
    """Return the q-expansion coefficients of Delta = eta^24 through q^max_exponent."""
    if max_exponent < 1:
        raise ValueError("max_exponent must be at least 1")
    eta24 = eta24_product_coefficients(max_exponent - 1)
    return {exponent: eta24[exponent - 1] for exponent in range(1, max_exponent + 1)}


def ramanujan_tau(n: int) -> int:
    """Return tau(n), the q^n coefficient of Delta = eta^24."""
    return ramanujan_delta_qexp(n)[n]


def niemeier_cusp_coefficient(root_count_value: int) -> Fraction:
    """Return the coefficient c_Delta in Theta_Lambda = E_12 + c_Delta Delta."""
    return Fraction(691 * root_count_value - 65520, 691)


def verify_weight_12_cusp_dimension() -> Weight12CuspVerification:
    """Verify dim S_12 = 1 by three independent full-level arguments."""
    delta_prefix = ramanujan_delta_qexp(6)
    delta_vanishing_order = next(
        exponent for exponent, coefficient in delta_prefix.items() if coefficient != 0
    )
    sturm_bound = sturm_bound_level_one(12)
    unique_by_sturm = sturm_bound == 1 and delta_prefix[1] == 1 and delta_vanishing_order == 1
    return Weight12CuspVerification(
        dimension_formula_value=dim_cusp_forms_formula(12),
        ring_theory_value=dim_cusp_forms_via_ring(12),
        sturm_bound=sturm_bound,
        delta_generator="Ramanujan Delta = eta^24",
        delta_qexp_prefix=tuple(delta_prefix[index] for index in range(1, 7)),
        delta_vanishing_order=delta_vanishing_order,
        unique_by_sturm=unique_by_sturm,
        verification_paths=(
            "dimension formula",
            "ring identity S_12 = Delta * M_0 with M_* = C[E4,E6]",
            "Sturm bound plus explicit Delta = eta^24 q-expansion",
        ),
    )


def depth_from_even_unimodular_rank(rank: int) -> int:
    """Return d(V_Lambda) = 3 + dim S_{rank/2} for even unimodular rank ``rank``."""
    if rank <= 0 or rank % 8 != 0:
        raise ValueError("rank must be a positive multiple of 8")
    return 3 + dim_cusp_forms_formula(rank // 2)


def niemeier_depth_record(label: str) -> NiemeierDepthRecord:
    """Return the BB3 depth data for one Niemeier lattice."""
    if label not in NIEMEIER_BY_LABEL:
        raise ValueError(f"unknown Niemeier lattice label: {label}")
    lattice = NIEMEIER_BY_LABEL[label]
    weight12 = verify_weight_12_cusp_dimension()
    if not weight12.is_verified:
        raise RuntimeError("weight-12 cusp-space verification failed")
    cusp_coefficient = niemeier_cusp_coefficient(lattice.root_count)
    if lattice.has_roots:
        mechanism_kind = "root_system_plus_cusp"
        mechanism_summary = (
            "The theta q^1 coefficient is the root count, but the extra depth still "
            "comes from the unique weight-12 cusp generator Delta."
        )
    else:
        mechanism_kind = "pure_cusp_only"
        mechanism_summary = (
            "The q^1 coefficient vanishes because there are no roots, so the depth-4 "
            "contribution is carried purely by the cusp-form sector."
        )
    return NiemeierDepthRecord(
        label=lattice.label,
        root_system=lattice.root_system,
        rank=lattice.rank,
        half_rank_weight=lattice.rank // 2,
        dim_s_half_rank=weight12.dimension_formula_value,
        depth=depth_from_even_unimodular_rank(lattice.rank),
        cusp_generator=weight12.delta_generator,
        cusp_coefficient=cusp_coefficient,
        root_count=lattice.root_count,
        theta_q1_coefficient=lattice.root_count,
        mechanism_kind=mechanism_kind,
        mechanism_summary=mechanism_summary,
        verification_paths=weight12.verification_paths,
    )


def all_niemeier_depth_records() -> Dict[str, NiemeierDepthRecord]:
    """Return BB3 depth data for all 24 Niemeier lattices."""
    return {lattice.label: niemeier_depth_record(lattice.label) for lattice in NIEMEIER_LATTICES}


__all__ = [
    "E12_Q1_COEFFICIENT",
    "NIEMEIER_BY_LABEL",
    "NIEMEIER_LATTICES",
    "NiemeierDepthRecord",
    "NiemeierLattice",
    "RootComponent",
    "Weight12CuspVerification",
    "all_niemeier_depth_records",
    "depth_from_even_unimodular_rank",
    "dim_cusp_forms_formula",
    "dim_cusp_forms_via_ring",
    "dim_modular_forms_via_ring",
    "eta24_product_coefficients",
    "modular_form_monomial_basis",
    "niemeier_cusp_coefficient",
    "niemeier_depth_record",
    "ramanujan_delta_qexp",
    "ramanujan_tau",
    "root_count",
    "sturm_bound_level_one",
    "verify_weight_12_cusp_dimension",
]
