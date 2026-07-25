r"""Exact scalar arithmetic and open derived-centre operations.

The chiral derived centre is the completed cochain object

    Z_ch^der(A) = RHom_{A^e}(A,A).

Strong-generator arithmetic, modular scalars, and finite combinatorics can be
computed before a chain model for this object is available.  Products,
Gerstenhaber brackets, BV operators, annulus maps, open/closed Maurer--Cartan
elements, Morita maps, and HKR comparisons require explicit chain maps.

This module evaluates the former and returns typed open obligations for the
latter.  The bounded BDSK calculations are recorded separately from the
curve-level chart:

* rank-one even superboson: dimensions ``(2,1,0,...)``;
* Virasoro: support ``{0,2,3}`` with one-dimensional groups.

A bounded-to-chart quasi-isomorphism is the transport datum in both cases.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb
from typing import Any, Dict, List, Mapping, Optional, Tuple


FAMILIES = ("Heisenberg", "Affine_sl2", "Virasoro", "W3")

CHAIN_MODEL_OBLIGATION = (
    "construct the completed curve-level chiral Hochschild cochain complex, "
    "its differential, and the named chain map realizing this operation"
)

BOUNDED_TO_CHART_OBLIGATION = (
    "construct the bounded-to-chart chain map and prove that it is a "
    "quasi-isomorphism after completion and averaging"
)


def kappa(family: str, **params: Any) -> Fraction:
    """Return the repository's exact family-specific scalar formula."""

    if family == "Heisenberg":
        return Fraction(params.get("k", 1))
    if family == "Affine_sl2":
        level = Fraction(params.get("k", 1))
        return Fraction(3) * (level + 2) / 4
    if family == "Virasoro":
        return Fraction(params.get("c", 26)) / 2
    if family == "W3":
        return Fraction(5) * Fraction(params.get("c", 2)) / 6
    raise ValueError(f"unknown family: {family}")


def generator_weights(family: str) -> List[int]:
    if family == "Heisenberg":
        return [1]
    if family == "Affine_sl2":
        return [1, 1, 1]
    if family == "Virasoro":
        return [2]
    if family == "W3":
        return [2, 3]
    raise ValueError(f"unknown family: {family}")


def num_generators(family: str) -> int:
    return len(generator_weights(family))


def _partition_count(weights: List[int], target: int) -> int:
    """Count unordered partitions with parts drawn from a labelled list."""

    if target < 0:
        return 0
    values = [0] * (target + 1)
    values[0] = 1
    for weight in weights:
        if weight <= 0:
            continue
        for total in range(weight, target + 1):
            values[total] += values[total - weight]
    return values[target]


def _composition_count(n_vars: int, total: int) -> int:
    if total < 0:
        return 0
    if n_vars <= 0:
        return int(total == 0)
    return comb(total + n_vars - 1, n_vars - 1)


class HochschildCocycleEnumerator:
    """Count a finite strong-generator ansatz before imposing a differential.

    The result is a combinatorial candidate-space count.  It is distinct from
    the dimension of a chiral cochain space and from its cohomology.
    """

    def __init__(self, family: str, weight_bound: int = 8):
        if weight_bound < 0:
            raise ValueError("weight_bound must be nonnegative")
        self.family = family
        self.weight_bound = weight_bound
        self.weights = generator_weights(family)

    def _weight_tuples(self, length: int) -> List[Tuple[int, ...]]:
        if length < 0:
            return []
        return list(product(self.weights, repeat=length))

    def candidate_dimension(self, arity: int, weight_shift: int) -> int:
        if arity < 1 or weight_shift < 0:
            return 0
        count = 0
        for inputs in self._weight_tuples(arity):
            input_weight = sum(inputs)
            for output_weight in self.weights:
                lambda_degree = input_weight - output_weight - weight_shift
                if 0 <= lambda_degree <= self.weight_bound:
                    count += _composition_count(arity - 1, lambda_degree)
        return count

    def cochain_dimension(self, degree: int, weight: int) -> int:
        """Compatibility name for the generator-ansatz count."""

        return self.candidate_dimension(degree + 1, weight)

    def total_cochain_dimension(self, degree: int) -> int:
        return sum(
            self.cochain_dimension(degree, weight)
            for weight in range(self.weight_bound + 1)
        )


@dataclass(frozen=True)
class BoundedBenchmark:
    family: str
    support: Tuple[int, ...]
    dimensions: Mapping[int, int]
    source: str

    @property
    def vector(self) -> Tuple[int, ...]:
        return tuple(self.dimensions.get(n, 0) for n in range(max(self.support) + 1))

    def dimension(self, degree: int) -> int:
        return self.dimensions.get(degree, 0)

    def prefix(self, max_degree: int) -> Tuple[int, ...]:
        if max_degree < 0:
            return ()
        return tuple(self.dimension(n) for n in range(max_degree + 1))


def heisenberg_bounded_benchmark() -> BoundedBenchmark:
    return BoundedBenchmark(
        family="rank-one even superboson",
        support=(0, 1),
        dimensions={0: 2, 1: 1},
        source="Bakalov--De Sole--Kac (2021), Theorem 7.4",
    )


def virasoro_bounded_benchmark() -> BoundedBenchmark:
    return BoundedBenchmark(
        family="Virasoro",
        support=(0, 2, 3),
        dimensions={0: 1, 2: 1, 3: 1},
        source="Bakalov--De Sole--Kac (2021), Theorem 7.2",
    )


@dataclass(frozen=True)
class ChartCohomologyStatus:
    family: str
    bounded_benchmark: Optional[BoundedBenchmark]
    chart_support: Optional[Tuple[int, ...]]
    chart_dimensions: Optional[Mapping[int, int]]
    conformal_weight_dimensions: Optional[Mapping[Any, int]]
    status: str
    resolution_obligation: str


def heisenberg_hh_cocycles(
    k: Fraction = Fraction(1), max_weight: int = 4
) -> ChartCohomologyStatus:
    """Return the bounded benchmark and the open weight-graded chart status."""

    Fraction(k)
    if max_weight < 0:
        raise ValueError("max_weight must be nonnegative")
    return ChartCohomologyStatus(
        family="Heisenberg",
        bounded_benchmark=heisenberg_bounded_benchmark(),
        chart_support=None,
        chart_dimensions=None,
        conformal_weight_dimensions=None,
        status="open-bounded-to-chart-comparison",
        resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
    )


def affine_sl2_hh_dimensions(k: int) -> ChartCohomologyStatus:
    if k == -2:
        raise ValueError("the critical level has a separate Feigin--Frenkel centre theory")
    return ChartCohomologyStatus(
        family="Affine_sl2",
        bounded_benchmark=None,
        chart_support=None,
        chart_dimensions=None,
        conformal_weight_dimensions=None,
        status="open-affine-bounded-complex-and-chart-comparison",
        resolution_obligation=CHAIN_MODEL_OBLIGATION,
    )


def affine_sl2_hh_at_levels() -> Dict[int, ChartCohomologyStatus]:
    return {level: affine_sl2_hh_dimensions(level) for level in (1, 2, 3)}


def virasoro_hh2_weight_graded(
    c: Fraction = Fraction(26), max_weight: int = 8
) -> ChartCohomologyStatus:
    """Record BDSK cohomological support and the open conformal-weight split."""

    Fraction(c)
    if max_weight < 0:
        raise ValueError("max_weight must be nonnegative")
    return ChartCohomologyStatus(
        family="Virasoro",
        bounded_benchmark=virasoro_bounded_benchmark(),
        chart_support=None,
        chart_dimensions=None,
        conformal_weight_dimensions=None,
        status="open-bounded-to-chart-and-weight-grading-comparison",
        resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
    )


@dataclass(frozen=True)
class OpenChainOperation:
    operation: str
    source: str
    target: str
    value: None
    status: str
    resolution_obligation: str


def _open_operation(operation: str, source: str, target: str) -> OpenChainOperation:
    return OpenChainOperation(
        operation=operation,
        source=source,
        target=target,
        value=None,
        status="open-explicit-chain-map",
        resolution_obligation=CHAIN_MODEL_OBLIGATION,
    )


class DerivedCenterStructureMaps:
    """Status surface for cup, Gerstenhaber, and BV operations."""

    def __init__(self, family: str, **params: Any):
        self.family = family
        self.params = params
        self.scalar_kappa = kappa(family, **params)

    def product(self, f_name: str, g_name: str) -> OpenChainOperation:
        return _open_operation(
            f"cup({f_name},{g_name})",
            "C_ch(A,A) tensor C_ch(A,A)",
            "C_ch(A,A)",
        )

    def gerstenhaber_bracket(
        self, f_name: str, g_name: str
    ) -> OpenChainOperation:
        return _open_operation(
            f"Gerstenhaber({f_name},{g_name})",
            "C_ch(A,A) tensor C_ch(A,A)",
            "C_ch(A,A)[-1]",
        )

    def bv_operator(self, f_name: str) -> OpenChainOperation:
        return _open_operation(
            f"BV({f_name})", "C_ch(A,A)", "C_ch(A,A)[-1]"
        )

    def verify_bv_relation(self, f_name: str, g_name: str) -> Dict[str, Any]:
        return {
            "inputs": (f_name, g_name),
            "match": None,
            "status": "open-until-cup-bracket-and-BV-chain-maps-exist",
            "resolution_obligation": CHAIN_MODEL_OBLIGATION,
        }


class AnnulusTrace:
    """Status surface for the annulus trace and scalar comparison."""

    def __init__(self, family: str, **params: Any):
        self.family = family
        self.params = params
        self.scalar_kappa = kappa(family, **params)

    def trace_on_identity(self) -> OpenChainOperation:
        return _open_operation("annulus_trace(1)", "HH_ch,0(A)", "H*(M_1,1)")

    def trace_on_hh1(self) -> OpenChainOperation:
        return _open_operation("annulus_trace(H1)", "HH_ch,1(A)", "H*(M_1,1)")

    def trace_on_hh2(self) -> OpenChainOperation:
        return _open_operation("annulus_trace(H2)", "HH_ch,2(A)", "H*(M_1,1)")

    def verify_modularity(self) -> Dict[str, Any]:
        return {
            "family": self.family,
            "scalar_kappa": self.scalar_kappa,
            "trace_equals_kappa": None,
            "scalar_diagnostic": verify_complementarity(
                self.family, **self.params
            ),
            "status": "open-annulus-chain-map-and-normalization",
        }


class OpenClosedMCElement:
    """Status surface for the open/closed Maurer--Cartan element."""

    def __init__(self, family: str, **params: Any):
        self.family = family
        self.params = params
        self.scalar_kappa = kappa(family, **params)

    def theta_oc(self, g: int, n: int) -> OpenChainOperation:
        if g < 0 or n < 0:
            raise ValueError("genus and arity must be nonnegative")
        return _open_operation(
            f"Theta_oc[{g},{n}]",
            "open/closed deformation complex",
            f"genus-{g}, arity-{n} summand",
        )

    def verify_mc_equation(self, g: int, n: int) -> Dict[str, Any]:
        return {
            "genus": g,
            "arity": n,
            "MC_value": None,
            "MC_satisfied": None,
            "status": "open-open/closed-chain-element-and-bracket",
            "resolution_obligation": CHAIN_MODEL_OBLIGATION,
        }


class DeformationQuantization:
    """Auxiliary Weyl arithmetic and an open derived-centre comparison."""

    def __init__(self, family: str, **params: Any):
        self.family = family
        self.params = params
        self.scalar_kappa = kappa(family, **params)

    def classical_poisson_bracket(
        self, f_name: str, g_name: str
    ) -> OpenChainOperation:
        return _open_operation(
            f"classical_bracket({f_name},{g_name})",
            "classical derived-centre model",
            "classical derived-centre model",
        )

    def quantum_commutator(
        self, f_name: str, g_name: str
    ) -> OpenChainOperation:
        return _open_operation(
            f"quantum_commutator({f_name},{g_name})",
            "quantized derived-centre model",
            "quantized derived-centre model",
        )

    def weyl_algebra_dimension(self, weight: int) -> int:
        """Return the exact PBW count for an auxiliary rank-one Weyl algebra."""

        if self.family != "Heisenberg":
            raise ValueError("this auxiliary count is implemented for rank one")
        return 0 if weight < 0 else weight + 1

    def verify_quantization(self) -> Dict[str, Any]:
        return {
            "family": self.family,
            "comparison": None,
            "status": "open-quantization-map-to-derived-centre",
            "resolution_obligation": CHAIN_MODEL_OBLIGATION,
        }


class BulkBoundaryMaps:
    """Status surface for restriction and annulus maps."""

    def __init__(self, family: str, **params: Any):
        self.family = family
        self.params = params
        self.scalar_kappa = kappa(family, **params)

    def restriction(self, bulk_element: str) -> OpenChainOperation:
        return _open_operation(
            f"restriction({bulk_element})",
            "physical bulk observables",
            "chiral Hochschild cochains",
        )

    def annulus_map(self, boundary_element: str) -> OpenChainOperation:
        return _open_operation(
            f"annulus({boundary_element})",
            "chiral Hochschild chains",
            "derived chiral centre",
        )

    def composition_a_r(self, element: str) -> OpenChainOperation:
        return _open_operation(
            f"annulus_after_restriction({element})",
            "physical bulk observables",
            "derived chiral centre",
        )

    def verify_composition(self) -> Dict[str, Any]:
        return {
            "composition_equals_kappa_identity": None,
            "status": "open-OCA-and-annulus-chain-maps",
            "resolution_obligation": CHAIN_MODEL_OBLIGATION,
        }


def morita_invariance_check(family: str, n: int, **params: Any) -> Dict[str, Any]:
    if n < 1:
        raise ValueError("matrix size must be positive")
    kappa(family, **params)
    return {
        "family": family,
        "n": n,
        "HH_A": None,
        "HH_Mat_n_A": None,
        "morita_invariant": None,
        "status": "open-chiral-Morita-object-and-comparison-functor",
        "resolution_obligation": CHAIN_MODEL_OBLIGATION,
    }


def chiral_hkr_dimension(
    family: str, degree: int, max_weight: int = 6
) -> Optional[int]:
    generator_weights(family)
    degree, max_weight
    return None


def verify_kappa_additivity(
    families: List[Tuple[str, Dict[str, Any]]]
) -> Dict[str, Any]:
    values = [kappa(family, **params) for family, params in families]
    return {
        "families": [family for family, _ in families],
        "kappas": values,
        "sum": sum(values, Fraction(0)),
        "status": "exact scalar arithmetic; categorical additivity requires its trace datum",
    }


def verify_complementarity(family: str, **params: Any) -> Dict[str, Any]:
    """Evaluate exact scalar involution identities, separately from duality."""

    scalar = kappa(family, **params)
    if family == "Heisenberg":
        level = Fraction(params.get("k", 1))
        companion_parameter = -level
        companion_scalar = companion_parameter
        expected_sum = Fraction(0)
    elif family == "Affine_sl2":
        level = Fraction(params.get("k", 1))
        companion_parameter = -level - 4
        companion_scalar = Fraction(3) * (companion_parameter + 2) / 4
        expected_sum = Fraction(0)
    elif family == "Virasoro":
        charge = Fraction(params.get("c", 26))
        companion_parameter = 26 - charge
        companion_scalar = companion_parameter / 2
        expected_sum = Fraction(13)
    else:
        return {
            "family": family,
            "scalar_identity": None,
            "chiral_duality": None,
            "status": "open-companion-parameter-formula",
        }
    total = scalar + companion_scalar
    return {
        "family": family,
        "kappa_A": scalar,
        "companion_parameter": companion_parameter,
        "kappa_A_dual": companion_scalar,
        "sum": total,
        "expected_sum": expected_sum,
        "scalar_identity": total == expected_sum,
        "match": total == expected_sum,
        "chiral_duality": None,
        "status": "exact scalar identity; bar-duality comparison open",
    }


def full_derived_center_package(family: str, **params: Any) -> Dict[str, Any]:
    """Return exact input arithmetic and every remaining chain obligation."""

    scalar = kappa(family, **params)
    benchmark: Optional[BoundedBenchmark]
    if family == "Heisenberg":
        benchmark = heisenberg_bounded_benchmark()
    elif family == "Virasoro":
        benchmark = virasoro_bounded_benchmark()
    else:
        benchmark = None
    return {
        "family": family,
        "params": params,
        "kappa": scalar,
        "generator_weights": generator_weights(family),
        "num_generators": num_generators(family),
        "bounded_benchmark": benchmark,
        "HH_dimensions": None,
        "HH_support": None,
        "cup_product": None,
        "Gerstenhaber_bracket": None,
        "BV_operator": None,
        "annulus_trace_identity": None,
        "open_closed_MC": None,
        "morita_invariant_n2": None,
        "calabi_yau": None,
        "euler_characteristic": None,
        "status": "open-family-support-and-chain-map-package",
        "resolution_obligation": CHAIN_MODEL_OBLIGATION,
    }
