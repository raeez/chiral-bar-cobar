r"""Family-indexed computation surface for Theorem H.

Theorem H concerns the completed curve-level complex

    C_ch^bullet(A,A) = RHom_{A^e}(A,A).

A datum ``H_H(A;S)`` consists of a complete chart model, a model supported
in ``S``, and a strong deformation retract between them.  It gives the
support inclusion ``Supp ChirHoch^bullet(A) subset S``.  The support set is
part of the family datum.

Two bounded vertex-complex calculations enter as independent benchmarks:

* the even superboson attached to an ``r``-dimensional space has
  ``dim H_b^n = C(r,n) + C(r,n+1)``;
* Virasoro has one-dimensional bounded cohomology in degrees ``0,2,3``.

Bakalov--De Sole--Kac prove these statements in Theorems 7.4 and 7.2.
A named bounded-to-chart quasi-isomorphism transports either benchmark to
the completed curve chart.  Their Conjecture 7.5 supplies the affine upper
bound ``C(dim(g),n) + C(dim(g),n+1)``.  Principal W, beta-gamma, bc,
lattice, and further family rows await their own ``H_H(A;S)`` data.

A perfect degree-``d`` pairing is recorded separately.  It governs a
duality comparison after both chart complexes have been constructed.

Compatibility functions retain the historical public names.  Functions
whose names refer to chart cohomology return ``None`` until explicit chart
transport data are supplied.  Bounded values are available through the
``bounded_*`` functions and the ambient-typed records below.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import reduce
from math import comb, gcd
from types import MappingProxyType
from typing import Any, Dict, List, Mapping, Optional, Tuple


THEOREM_H_REQUIRED_COMPONENTS: Tuple[str, ...] = (
    "complete_chart_complex_Q_A",
    "chart_quasi_isomorphism_gamma_A",
    "support_model_K_A_S",
    "strong_deformation_retract_i_p_h",
    "incidence_and_bar_face_compatibility",
    "averaging_and_Mittag_Leffler_comparison",
)

THEOREM_H_HYPOTHESES = THEOREM_H_REQUIRED_COMPONENTS
THEOREM_H_DEFECT_COMPLEX = "D_H(A;S)"
THEOREM_H_PACKAGE_CONDITIONAL = "family-indexed-H_H(A;S)"

BOUNDED_TO_CHART_OBLIGATION = (
    "construct the bounded-to-chart chain map and prove that it is a "
    "quasi-isomorphism on the completed curve-level cochain complex"
)

FAMILY_SUPPORT_OBLIGATION = (
    "construct the complete family datum H_H(A;S), including its strong "
    "deformation retract and completion comparison"
)

PERFECT_PAIRING_OBLIGATION = (
    "construct the degree-d chain pairing and prove its perfectness on both "
    "completed chart complexes"
)


class CohomologyAmbient(str, Enum):
    """The cochain complex whose cohomology a numerical profile describes."""

    BOUNDED_VERTEX = "bounded_vertex_complex"
    COMPLETED_CURVE_CHART = "completed_curve_chart"


@dataclass(frozen=True)
class CohomologyProfile:
    """A cohomology profile with an explicit ambient complex and status."""

    family: str
    ambient: CohomologyAmbient
    complex_name: str
    support: Optional[Tuple[int, ...]]
    dimensions: Optional[Mapping[int, int]]
    status: str
    source: str
    resolution_obligation: str = ""

    def __post_init__(self) -> None:
        if self.support is not None:
            normalized = tuple(sorted(set(self.support)))
            if normalized != self.support or any(n < 0 for n in self.support):
                raise ValueError("support must be a strictly increasing tuple of nonnegative degrees")
        if self.dimensions is not None:
            if any(n < 0 or value < 0 for n, value in self.dimensions.items()):
                raise ValueError("cohomology dimensions use nonnegative degrees and values")
            visible_support = tuple(sorted(n for n, value in self.dimensions.items() if value))
            if self.support is None or visible_support != self.support:
                raise ValueError("support must equal the degrees carrying positive dimension")

    def dimension(self, degree: int) -> Optional[int]:
        """Return an exact dimension when the ambient profile determines it."""

        if degree < 0:
            return 0
        if self.dimensions is not None:
            return self.dimensions.get(degree, 0)
        if self.support is not None and degree not in self.support:
            return 0
        return None

    def prefix(self, max_degree: int) -> Optional[Tuple[Optional[int], ...]]:
        if max_degree < 0:
            return ()
        values = tuple(self.dimension(n) for n in range(max_degree + 1))
        if all(value is None for value in values):
            return None
        return values

    @property
    def vector(self) -> Optional[Tuple[int, ...]]:
        if self.dimensions is None or self.support is None:
            return None
        if not self.support:
            return ()
        return tuple(self.dimensions.get(n, 0) for n in range(max(self.support) + 1))

    @property
    def total_dimension(self) -> Optional[int]:
        if self.dimensions is None:
            return None
        return sum(self.dimensions.values())

    @property
    def euler_characteristic(self) -> Optional[int]:
        if self.dimensions is None:
            return None
        return sum((-1) ** n * value for n, value in self.dimensions.items())


@dataclass(frozen=True)
class BoundedToChartComparison:
    """A named cochain map from a bounded complex to a completed chart."""

    family: str
    map_name: str
    source_complex: str
    target_complex: str
    quasi_isomorphism_status: str = "open"

    def __post_init__(self) -> None:
        if any(value == "" for value in (
            self.family, self.map_name, self.source_complex, self.target_complex
        )):
            raise ValueError("a comparison names its family, map, source, and target")
        allowed = {"open", "assumed", "proved-elsewhere"}
        if self.quasi_isomorphism_status not in allowed:
            raise ValueError(f"comparison status belongs to {sorted(allowed)}")

    @property
    def supplies_transport(self) -> bool:
        return self.quasi_isomorphism_status in {"assumed", "proved-elsewhere"}


@dataclass(frozen=True)
class FamilySupportDatum:
    r"""A typed instance of ``H_H(A;S)`` for one completed curve chart."""

    family: str
    support: Tuple[int, ...]
    complete_chart_complex: str
    chart_comparison_map: str
    support_model: str
    inclusion: str
    projection: str
    contracting_homotopy: str
    incidence_and_bar_face_compatibility: str
    completion_and_averaging_map: str
    model_dimensions: Optional[Mapping[int, int]] = None
    status: str = "assumed"

    def __post_init__(self) -> None:
        normalized = tuple(sorted(set(self.support)))
        if normalized != self.support or any(n < 0 for n in self.support):
            raise ValueError("support must be a strictly increasing tuple of nonnegative degrees")
        names = (
            self.family,
            self.complete_chart_complex,
            self.chart_comparison_map,
            self.support_model,
            self.inclusion,
            self.projection,
            self.contracting_homotopy,
            self.incidence_and_bar_face_compatibility,
            self.completion_and_averaging_map,
        )
        if any(value == "" for value in names):
            raise ValueError("every component of H_H(A;S) carries a name")
        if self.status not in {"open", "assumed", "proved-elsewhere"}:
            raise ValueError("H_H status is open, assumed, or proved-elsewhere")
        if self.model_dimensions is not None:
            visible = tuple(sorted(n for n, value in self.model_dimensions.items() if value))
            if visible != self.support:
                raise ValueError("model dimensions must realize the declared support")

    @property
    def supplies_chart_model(self) -> bool:
        return self.status in {"assumed", "proved-elsewhere"}


@dataclass(frozen=True)
class PerfectDegreePairing:
    """A pairing datum, logically separate from support and chart transport."""

    family: str
    dual_family: str
    pairing_map: str
    cohomological_degree: int
    perfectness_status: str = "open"

    def __post_init__(self) -> None:
        if any(value == "" for value in (self.family, self.dual_family, self.pairing_map)):
            raise ValueError("a perfect-pairing datum names both families and its chain map")
        allowed = {"open", "assumed", "proved-elsewhere"}
        if self.perfectness_status not in allowed:
            raise ValueError(f"pairing status belongs to {sorted(allowed)}")

    @property
    def supplies_pairing(self) -> bool:
        return self.perfectness_status in {"assumed", "proved-elsewhere"}


@dataclass(frozen=True)
class AffineExteriorBound:
    """The BDSK Conjecture 7.5 exterior-power bound in a named ambient."""

    family: str
    lie_dimension: int
    ambient: CohomologyAmbient
    status: str
    source: str
    comparison_map: Optional[str] = None

    def upper_bound(self, degree: int) -> int:
        return exterior_two_term_dimension(self.lie_dimension, degree)

    def prefix(self, max_degree: int) -> Tuple[int, ...]:
        if max_degree < 0:
            return ()
        return tuple(self.upper_bound(n) for n in range(max_degree + 1))


@dataclass(frozen=True)
class FamilyCohomologyRecord:
    """The bounded, chart, comparison, and pairing data for one family."""

    key: str
    family: str
    presentation: str
    bounded: CohomologyProfile
    chart: CohomologyProfile
    bounded_affine_bound: Optional[AffineExteriorBound]
    chart_affine_bound: Optional[AffineExteriorBound]
    comparison: Optional[BoundedToChartComparison]
    family_support: Optional[FamilySupportDatum]
    perfect_pairing: Optional[PerfectDegreePairing]
    generator_weights: Tuple[int, ...]
    metadata: Mapping[str, Any]

    @property
    def regime(self) -> str:
        return "family_indexed_support"

    @property
    def poincare(self) -> Optional[List[int]]:
        vector = self.chart.vector
        return None if vector is None else list(vector)

    def __getitem__(self, key: str) -> Any:
        """Read-only migration path for historical dictionary importers."""

        migration = {
            "regime": self.regime,
            "status": self.chart.status,
            "poincare": self.poincare,
            "bounded_profile": self.bounded,
            "chart_profile": self.chart,
            "generator_weights": self.generator_weights,
        }
        if key in migration:
            return migration[key]
        raise KeyError(key)

    def get(self, key: str, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default


def exterior_two_term_dimension(vector_space_dimension: int, degree: int) -> int:
    r"""Return ``dim Lambda^n(V) + dim Lambda^(n+1)(V)`` exactly."""

    if not isinstance(vector_space_dimension, int) or vector_space_dimension < 0:
        raise ValueError("vector-space dimension must be a nonnegative integer")
    if not isinstance(degree, int):
        raise TypeError("cohomological degree must be an integer")
    if degree < 0:
        return 0
    first = comb(vector_space_dimension, degree) if degree <= vector_space_dimension else 0
    second = (
        comb(vector_space_dimension, degree + 1)
        if degree + 1 <= vector_space_dimension
        else 0
    )
    return first + second


def superboson_bounded_dimension(rank: int, degree: int) -> int:
    r"""BDSK Theorem 7.4: ``dim S^n(Pi h)^* + dim S^(n+1)(Pi h)^*``."""

    return exterior_two_term_dimension(rank, degree)


def virasoro_bounded_dimension(degree: int) -> int:
    """BDSK Theorem 7.2 in the bounded Virasoro complex."""

    return int(degree in {0, 2, 3})


def affine_bounded_upper_bound(lie_dimension: int, degree: int) -> int:
    """The numerical right side of BDSK Conjecture 7.5."""

    return exterior_two_term_dimension(lie_dimension, degree)


def _open_profile(
    family: str,
    ambient: CohomologyAmbient,
    complex_name: str,
    status: str,
    source: str,
    obligation: str,
) -> CohomologyProfile:
    return CohomologyProfile(
        family=family,
        ambient=ambient,
        complex_name=complex_name,
        support=None,
        dimensions=None,
        status=status,
        source=source,
        resolution_obligation=obligation,
    )


def superboson_bounded_profile(rank: int = 1) -> CohomologyProfile:
    if not isinstance(rank, int) or rank < 0:
        raise ValueError("superboson rank must be a nonnegative integer")
    dimensions = {
        degree: superboson_bounded_dimension(rank, degree)
        for degree in range(rank + 1)
    }
    dimensions = {degree: value for degree, value in dimensions.items() if value}
    support = tuple(dimensions)
    return CohomologyProfile(
        family=f"even superboson of rank {rank}",
        ambient=CohomologyAmbient.BOUNDED_VERTEX,
        complex_name=f"C^bullet_ch,b(B_h{rank},B_h{rank})",
        support=support,
        dimensions=dimensions,
        status="proved-bounded-BDSK-Theorem-7.4",
        source="Bakalov--De Sole--Kac (2021), Theorem 7.4",
    )


def virasoro_bounded_profile() -> CohomologyProfile:
    dimensions = {0: 1, 2: 1, 3: 1}
    return CohomologyProfile(
        family="Virasoro Vir_c",
        ambient=CohomologyAmbient.BOUNDED_VERTEX,
        complex_name="C^bullet_ch,b(Vir_c,Vir_c)",
        support=(0, 2, 3),
        dimensions=dimensions,
        status="proved-bounded-BDSK-Theorem-7.2",
        source="Bakalov--De Sole--Kac (2021), Theorem 7.2",
    )


def _normalize_family(family: str) -> str:
    return family.lower().replace("-", "_").replace(" ", "_")


def _family_base(
    family: str,
    *,
    rank: Optional[int] = None,
    N: Optional[int] = None,
) -> Tuple[str, str, str, CohomologyProfile, Optional[AffineExteriorBound], Tuple[int, ...], Dict[str, Any]]:
    normalized = _normalize_family(family)

    if normalized in {"heisenberg", "heis", "superboson", "even_superboson"}:
        resolved_rank = 1 if rank is None else rank
        bounded = superboson_bounded_profile(resolved_rank)
        return (
            f"superboson_rank_{resolved_rank}",
            bounded.family,
            "bounded even superboson / Heisenberg presentation",
            bounded,
            None,
            (1,) * resolved_rank,
            {"rank": resolved_rank, "family_parameter": "Heisenberg level recorded separately"},
        )

    if normalized in {"virasoro", "vir", "vir_c", "w2", "w_2"}:
        bounded = virasoro_bounded_profile()
        return (
            "virasoro",
            bounded.family,
            "bounded Virasoro vertex complex",
            bounded,
            None,
            (2,),
            {"central_charge": "fixed-fibre parameter"},
        )

    affine_N: Optional[int] = None
    if normalized in {"affine", "affine_km", "affine_sln"}:
        affine_N = N
    elif normalized.startswith("affine_sl") and normalized[9:].isdigit():
        affine_N = int(normalized[9:])
    if affine_N is not None:
        if affine_N < 2:
            raise ValueError("affine sl_N requires N at least 2")
        lie_dimension = affine_N * affine_N - 1
        family_name = f"affine V_k(sl_{affine_N})"
        bounded = _open_profile(
            family_name,
            CohomologyAmbient.BOUNDED_VERTEX,
            f"C^bullet_ch,b(V_k(sl_{affine_N}),V_k(sl_{affine_N}))",
            "conjectural-BDSK-Conjecture-7.5-bound",
            "Bakalov--De Sole--Kac (2021), Conjecture 7.5",
            "construct the bounded affine complex and establish the conjectural exterior bound",
        )
        bound = AffineExteriorBound(
            family=family_name,
            lie_dimension=lie_dimension,
            ambient=CohomologyAmbient.BOUNDED_VERTEX,
            status="conjectural-BDSK-Conjecture-7.5-bound",
            source="Bakalov--De Sole--Kac (2021), Conjecture 7.5",
        )
        return (
            f"affine_sl{affine_N}",
            family_name,
            "bounded affine vertex complex",
            bounded,
            bound,
            (1,) * lie_dimension,
            {
                "N": affine_N,
                "lie_dimension": lie_dimension,
                "known_inner_zero_mode_dimension": lie_dimension,
            },
        )

    w_N: Optional[int] = None
    if normalized in {"w", "wn", "w_n", "w_algebra"}:
        w_N = N
    elif normalized.startswith("w") and normalized[1:].isdigit():
        w_N = int(normalized[1:])
    if w_N is not None:
        if w_N < 2:
            raise ValueError("principal W_N requires N at least 2")
        if w_N == 2:
            return _family_base("virasoro")
        family_name = f"principal W_{w_N}"
        bounded = _open_profile(
            family_name,
            CohomologyAmbient.BOUNDED_VERTEX,
            f"C^bullet_ch,b(W_{w_N},W_{w_N})",
            "open-family-specific-bounded-complex",
            "family-specific construction",
            FAMILY_SUPPORT_OBLIGATION,
        )
        return (
            f"w{w_N}",
            family_name,
            "principal W-algebra vertex complex",
            bounded,
            None,
            tuple(range(2, w_N + 1)),
            {"N": w_N},
        )

    if normalized in {"betagamma", "beta_gamma", "free_betagamma"}:
        key, family_name, weights = "betagamma", "free beta-gamma", (1, 0)
    elif normalized in {"bc", "bc_ghosts", "free_fermion", "free_fermion_bc"}:
        key, family_name, weights = "bc_ghosts", "free fermion bc", (2, -1)
    elif normalized in {"lattice", "lattice_rank_r", "lattice_va"}:
        resolved_rank = 1 if rank is None else rank
        if not isinstance(resolved_rank, int) or resolved_rank < 1:
            raise ValueError("lattice rank must be a positive integer")
        key, family_name, weights = (
            f"lattice_rank_{resolved_rank}",
            f"lattice vertex algebra of rank {resolved_rank}",
            (1,) * resolved_rank,
        )
    else:
        raise KeyError(f"unknown Theorem-H family: {family}")

    bounded = _open_profile(
        family_name,
        CohomologyAmbient.BOUNDED_VERTEX,
        f"C^bullet_ch,b({key},{key})",
        "open-family-specific-bounded-complex",
        "family-specific construction",
        FAMILY_SUPPORT_OBLIGATION,
    )
    return key, family_name, "family-specific vertex complex", bounded, None, weights, {}


def _chart_from_data(
    key: str,
    family_name: str,
    bounded: CohomologyProfile,
    comparison: Optional[BoundedToChartComparison],
    family_datum: Optional[FamilySupportDatum],
) -> CohomologyProfile:
    default_complex = f"C^bullet_ch({key},{key})^completed"

    if family_datum is not None:
        if family_datum.family != key:
            raise ValueError("H_H family differs from the requested family")
        if family_datum.supplies_chart_model:
            return CohomologyProfile(
                family=family_name,
                ambient=CohomologyAmbient.COMPLETED_CURVE_CHART,
                complex_name=family_datum.complete_chart_complex,
                support=family_datum.support,
                dimensions=family_datum.model_dimensions,
                status=f"conditional-{family_datum.status}-H_H(A;S)",
                source=family_datum.support_model,
                resolution_obligation=(
                    "compute dimensions inside the supplied support model"
                    if family_datum.model_dimensions is None
                    else ""
                ),
            )
        return _open_profile(
            family_name,
            CohomologyAmbient.COMPLETED_CURVE_CHART,
            family_datum.complete_chart_complex,
            "open-family-support-datum",
            family_datum.support_model,
            FAMILY_SUPPORT_OBLIGATION,
        )

    if comparison is not None:
        if comparison.family != key:
            raise ValueError("comparison family differs from the requested family")
        if comparison.source_complex != bounded.complex_name:
            raise ValueError("comparison source differs from the bounded complex")
        if comparison.supplies_transport and bounded.dimensions is not None:
            return CohomologyProfile(
                family=family_name,
                ambient=CohomologyAmbient.COMPLETED_CURVE_CHART,
                complex_name=comparison.target_complex,
                support=bounded.support,
                dimensions=dict(bounded.dimensions),
                status=(
                    f"conditional-{comparison.quasi_isomorphism_status}-"
                    "bounded-to-chart"
                ),
                source=comparison.map_name,
            )
        return _open_profile(
            family_name,
            CohomologyAmbient.COMPLETED_CURVE_CHART,
            comparison.target_complex,
            "open-bounded-to-chart-comparison",
            comparison.map_name,
            BOUNDED_TO_CHART_OBLIGATION,
        )

    return _open_profile(
        family_name,
        CohomologyAmbient.COMPLETED_CURVE_CHART,
        default_complex,
        "open-family-support-datum",
        "family support datum H_H(A;S)",
        FAMILY_SUPPORT_OBLIGATION,
    )


def cohomology_record(
    family: str,
    *,
    rank: Optional[int] = None,
    N: Optional[int] = None,
    comparison: Optional[BoundedToChartComparison] = None,
    family_datum: Optional[FamilySupportDatum] = None,
    perfect_pairing: Optional[PerfectDegreePairing] = None,
) -> FamilyCohomologyRecord:
    """Return one ambient-typed Theorem-H family record."""

    key, family_name, presentation, bounded, affine_bound, weights, metadata = _family_base(
        family, rank=rank, N=N
    )
    if perfect_pairing is not None and perfect_pairing.family != key:
        raise ValueError("pairing family differs from the requested family")
    chart = _chart_from_data(key, family_name, bounded, comparison, family_datum)

    chart_affine_bound = None
    if affine_bound is not None and comparison is not None and comparison.supplies_transport:
        if comparison.family != key or comparison.source_complex != bounded.complex_name:
            raise ValueError("affine comparison differs from the bounded family data")
        chart_affine_bound = AffineExteriorBound(
            family=family_name,
            lie_dimension=affine_bound.lie_dimension,
            ambient=CohomologyAmbient.COMPLETED_CURVE_CHART,
            status=(
                "conjectural-BDSK-Conjecture-7.5-bound-transported-by-"
                f"{comparison.quasi_isomorphism_status}"
            ),
            source=affine_bound.source,
            comparison_map=comparison.map_name,
        )

    return FamilyCohomologyRecord(
        key=key,
        family=family_name,
        presentation=presentation,
        bounded=bounded,
        chart=chart,
        bounded_affine_bound=affine_bound,
        chart_affine_bound=chart_affine_bound,
        comparison=comparison,
        family_support=family_datum,
        perfect_pairing=perfect_pairing,
        generator_weights=weights,
        metadata=MappingProxyType(dict(metadata)),
    )


def _standard_family_data() -> Dict[str, FamilyCohomologyRecord]:
    return {
        "heisenberg": cohomology_record("heisenberg"),
        "virasoro": cohomology_record("virasoro"),
        "affine_sl2": cohomology_record("affine_sl2"),
        "affine_sl3": cohomology_record("affine_sl3"),
        "betagamma": cohomology_record("betagamma"),
        "bc_ghosts": cohomology_record("bc_ghosts"),
        "free_fermion": cohomology_record("free_fermion"),
        "w3": cohomology_record("w3"),
        "w4": cohomology_record("w4"),
        "w5": cohomology_record("w5"),
        "lattice": cohomology_record("lattice", rank=1),
    }


FAMILY_DATA: Mapping[str, FamilyCohomologyRecord] = MappingProxyType(
    _standard_family_data()
)
THEOREM_H_STATUS = FAMILY_DATA


def theorem_h_scope_record(
    family: Optional[str] = None,
    applies: Optional[bool] = None,
    reason: Optional[str] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    """Return the family-indexed statement and the status of supplied data."""

    record = None if family is None else cohomology_record(family, **kwargs)
    return {
        "claim": "H_H(A;S) implies Supp ChirHoch(A) subset S",
        "type_signature": {
            "quadrant": "Open-Chain",
            "presentation": "completed curve-level chiral Hochschild cochains",
            "level": 3,
            "hypothesis_package": "family support datum H_H(A;S)",
        },
        "family": family,
        "chart_ambient": CohomologyAmbient.COMPLETED_CURVE_CHART.value,
        "applies": None if record is None else record.chart.support is not None,
        "status": "open-explicit-family-support-datum" if record is None else record.chart.status,
        "support": None if record is None else record.chart.support,
        "dimensions": None if record is None else record.chart.dimensions,
        "support_determined": False if record is None else record.chart.support is not None,
        "defect_complex": (
            THEOREM_H_DEFECT_COMPLEX
            if record is None or record.chart.support is None
            else None
        ),
        "hypotheses": THEOREM_H_REQUIRED_COMPONENTS,
        "reason": reason,
        "legacy_applies_argument": applies,
    }


def bounded_betti(family: str, degree: int, **kwargs: Any) -> Optional[int]:
    return cohomology_record(family, **kwargs).bounded.dimension(degree)


def bounded_poincare(family: str, **kwargs: Any) -> Optional[List[int]]:
    vector = cohomology_record(family, **kwargs).bounded.vector
    return None if vector is None else list(vector)


def hochschild_betti(family: str, degree: int, **kwargs: Any) -> Optional[int]:
    """Compatibility API for completed chart cohomology."""

    return cohomology_record(family, **kwargs).chart.dimension(degree)


def hochschild_poincare(
    family: str, max_n: int = 10, **kwargs: Any
) -> Optional[List[int]]:
    """Compatibility API for the completed chart vector."""

    del max_n
    vector = cohomology_record(family, **kwargs).chart.vector
    return None if vector is None else list(vector)


def hochschild_total_dim(family: str, **kwargs: Any) -> Optional[int]:
    return cohomology_record(family, **kwargs).chart.total_dimension


def hochschild_euler_char(family: str, **kwargs: Any) -> Optional[int]:
    return cohomology_record(family, **kwargs).chart.euler_characteristic


def quadratic_poincare_polynomial(
    center_dim: int, hoch1_dim: int, dual_center_dim: int
) -> List[int]:
    """A raw three-coefficient constructor, independent of any family claim."""

    return [center_dim, hoch1_dim, dual_center_dim]


def quadratic_hochschild_betti(family: str, degree: int, **kwargs: Any) -> Optional[int]:
    return hochschild_betti(family, degree, **kwargs)


def quadratic_euler_char(family: str, **kwargs: Any) -> Optional[int]:
    return hochschild_euler_char(family, **kwargs)


def quadratic_total_dim(family: str, **kwargs: Any) -> Optional[int]:
    return hochschild_total_dim(family, **kwargs)


def generator_count(family: str, **kwargs: Any) -> int:
    return len(cohomology_record(family, **kwargs).generator_weights)


def w_algebra_gen_degrees(lie_type: str, rank: int) -> List[int]:
    if lie_type == "A" and rank >= 1:
        return list(range(2, rank + 2))
    raise ValueError("the implemented principal family is type A with positive rank")


def w_algebra_hochschild_dim(gen_degrees: List[int], degree: int) -> Optional[int]:
    """Historical chart API; generator weights alone determine metadata."""

    tuple(gen_degrees), degree
    return None


def w_algebra_poincare_series(
    gen_degrees: List[int], max_n: int
) -> Optional[List[int]]:
    tuple(gen_degrees), max_n
    return None


def w_algebra_quasi_period(gen_degrees: List[int]) -> Optional[int]:
    tuple(gen_degrees)
    return None


def w_algebra_growth_rate(gen_degrees: List[int]) -> Optional[float]:
    tuple(gen_degrees)
    return None


def virasoro_hochschild_dims(
    max_n: int = 20, **kwargs: Any
) -> Optional[List[Optional[int]]]:
    profile = cohomology_record("virasoro", **kwargs).chart
    prefix = profile.prefix(max_n)
    return None if prefix is None else list(prefix)


def w3_hochschild_dims(
    max_n: int = 30, **kwargs: Any
) -> Optional[List[Optional[int]]]:
    profile = cohomology_record("w3", **kwargs).chart
    prefix = profile.prefix(max_n)
    return None if prefix is None else list(prefix)


def virasoro_periodicity_check(max_n: int = 20, **kwargs: Any) -> Dict[str, Any]:
    dims = virasoro_hochschild_dims(max_n, **kwargs)
    return {
        "ambient": CohomologyAmbient.COMPLETED_CURVE_CHART.value,
        "dimensions": dims,
        "status": cohomology_record("virasoro", **kwargs).chart.status,
        "periodicity_claim": None,
    }


def w3_quasi_periodicity_check(max_n: int = 60, **kwargs: Any) -> Dict[str, Any]:
    dims = w3_hochschild_dims(max_n, **kwargs)
    return {
        "ambient": CohomologyAmbient.COMPLETED_CURVE_CHART.value,
        "dimensions": dims,
        "status": cohomology_record("w3", **kwargs).chart.status,
        "quasi_periodicity_claim": None,
    }


def affine_slN_data(N: int, **kwargs: Any) -> FamilyCohomologyRecord:
    return cohomology_record("affine_slN", N=N, **kwargs)


def wN_data(N: int, **kwargs: Any) -> FamilyCohomologyRecord:
    return cohomology_record("wN", N=N, **kwargs)


def lattice_data(rank: int, **kwargs: Any) -> FamilyCohomologyRecord:
    return cohomology_record("lattice", rank=rank, **kwargs)


def verify_concentration(family: str, **kwargs: Any) -> Dict[str, Any]:
    record = cohomology_record(family, **kwargs)
    return {
        "family": record.family,
        "ambient": record.chart.ambient.value,
        "support": record.chart.support,
        "support_determined": record.chart.support is not None,
        "passed": None,
        "status": record.chart.status,
    }


def verify_palindromicity(
    family: str,
    *,
    perfect_pairing: Optional[PerfectDegreePairing] = None,
    dual_chart_dimensions: Optional[Mapping[int, int]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    record = cohomology_record(family, perfect_pairing=perfect_pairing, **kwargs)
    vector = record.chart.vector
    supplies_pairing = perfect_pairing is not None and perfect_pairing.supplies_pairing
    passed = None
    checks: Dict[int, bool] = {}
    if vector is not None and supplies_pairing:
        dual_dimensions = dual_chart_dimensions
        if dual_dimensions is None and perfect_pairing.dual_family == record.key:
            dual_dimensions = record.chart.dimensions
        if dual_dimensions is not None:
            degree = perfect_pairing.cohomological_degree
            relevant = set(record.chart.dimensions or ())
            relevant.update(degree - n for n in dual_dimensions)
            checks = {
                n: (record.chart.dimension(n) == dual_dimensions.get(degree - n, 0))
                for n in sorted(relevant)
            }
            passed = all(checks.values())
    return {
        "family": record.family,
        "polynomial": None if vector is None else list(vector),
        "passed": passed,
        "degree_reflection_checks": checks,
        "pairing_status": None if perfect_pairing is None else perfect_pairing.perfectness_status,
        "resolution_obligation": PERFECT_PAIRING_OBLIGATION if passed is None else "",
    }


def verify_koszul_duality_hochschild(
    family: str,
    *,
    perfect_pairing: Optional[PerfectDegreePairing] = None,
    dual_chart_dimensions: Optional[Mapping[int, int]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    result = verify_palindromicity(
        family,
        perfect_pairing=perfect_pairing,
        dual_chart_dimensions=dual_chart_dimensions,
        **kwargs,
    )
    return {
        "family": result["family"],
        "passed": result["passed"],
        "degree_reflection_checks": result["degree_reflection_checks"],
        "pairing": perfect_pairing,
        "resolution_obligation": result["resolution_obligation"],
    }


def verify_theorem_h(family: str, **kwargs: Any) -> Dict[str, Any]:
    record = cohomology_record(family, **kwargs)
    chart_data_supplied = record.chart.support is not None
    return {
        "family": record.family,
        "regime": record.regime,
        "passed": True if chart_data_supplied else None,
        "bounded": record.bounded,
        "chart": record.chart,
        "theorem_h_scope": theorem_h_scope_record(family, **kwargs),
    }


def verify_theorem_h_all_families() -> Dict[str, Dict[str, Any]]:
    return {family: verify_theorem_h(family) for family in FAMILY_DATA}


def koszul_dual_polynomial(
    family: str, *, perfect_pairing: Optional[PerfectDegreePairing] = None, **kwargs: Any
) -> Optional[List[int]]:
    record = cohomology_record(family, perfect_pairing=perfect_pairing, **kwargs)
    if perfect_pairing is None or not perfect_pairing.supplies_pairing:
        return None
    if record.chart.dimensions is None or perfect_pairing.cohomological_degree < 0:
        return None
    degree = perfect_pairing.cohomological_degree
    if any(n > degree for n in record.chart.dimensions):
        return None
    return [record.chart.dimensions.get(degree - n, 0) for n in range(degree + 1)]


def hochschild_spectral_sequence(
    family: str, max_p: int = 6, max_q: int = 4, **kwargs: Any
) -> Optional[List[List[int]]]:
    """Historical API; an explicit filtered complex determines this page."""

    cohomology_record(family, **kwargs), max_p, max_q
    return None


def exterior_algebra_verification(
    family: str = "heisenberg", **kwargs: Any
) -> Dict[str, Any]:
    record = cohomology_record(family, **kwargs)
    rank = record.metadata.get("rank")
    if rank is None or record.bounded.dimensions is None:
        return {"family": record.family, "passed": None, "status": record.bounded.status}
    expected = {
        n: exterior_two_term_dimension(int(rank), n)
        for n in range(int(rank) + 1)
    }
    expected = {n: value for n, value in expected.items() if value}
    return {
        "family": record.family,
        "ambient": record.bounded.ambient.value,
        "dimensions": dict(record.bounded.dimensions),
        "expected_from_exterior_powers": expected,
        "passed": dict(record.bounded.dimensions) == expected,
    }


def non_koszul_failure_example() -> Dict[str, Any]:
    """Historical name for an open family-support record."""

    return {
        "family": "admissible affine quotient",
        "chart_dimensions": None,
        "status": "open-family-specific-H_H(A;S)",
        "resolution_obligation": FAMILY_SUPPORT_OBLIGATION,
    }


def bar_complex_betti_abelian(rank: int = 1, max_n: int = 6) -> Dict[str, Any]:
    """Compute the abelian CE dimensions and the BDSK bounded profile."""

    if not isinstance(rank, int) or rank < 0:
        raise ValueError("abelian rank must be a nonnegative integer")
    ce_dimensions = {n: comb(rank, n) for n in range(rank + 1)}
    bounded = superboson_bounded_profile(rank)
    return {
        "rank": rank,
        "ce_dimensions": ce_dimensions,
        "ce_cohomology": dict(ce_dimensions),
        "bounded_vertex_prefix": bounded.prefix(max_n),
        "bounded_vertex_profile": bounded,
        "chart_dimensions": None,
        "chart_status": "open-bounded-to-chart-comparison",
    }


def bar_complex_betti_sl2(max_tensor_degree: int = 4) -> Dict[str, Any]:
    """Record exact CE cohomology and the conjectural affine bound."""

    del max_tensor_degree
    record = affine_slN_data(2)
    assert record.bounded_affine_bound is not None
    return {
        "ce_dimensions": {0: 1, 1: 3, 2: 3, 3: 1},
        "ce_cohomology": {0: 1, 1: 0, 2: 0, 3: 1},
        "whitehead_lemmas": {1: 0, 2: 0},
        "bounded_affine_upper_bound": record.bounded_affine_bound.prefix(4),
        "bounded_status": record.bounded_affine_bound.status,
        "chart_dimensions": None,
        "chart_status": record.chart.status,
    }


def polynomial_growth_verification(
    family: str, max_n: int = 30, **kwargs: Any
) -> Dict[str, Any]:
    record = cohomology_record(family, **kwargs)
    prefix = record.bounded.prefix(max_n)
    return {
        "family": record.family,
        "ambient": record.bounded.ambient.value,
        "dimensions": prefix,
        "verified": record.bounded.dimensions is not None,
        "status": record.bounded.status,
    }


def euler_characteristic_derived(
    family: str, max_n: int = 40, **kwargs: Any
) -> Dict[str, Any]:
    del max_n
    record = cohomology_record(family, **kwargs)
    return {
        "family": record.family,
        "ambient": record.chart.ambient.value,
        "chi": record.chart.euler_characteristic,
        "verified": record.chart.euler_characteristic is not None,
        "status": record.chart.status,
    }


def palindromicity_derived(
    family: str,
    *,
    perfect_pairing: Optional[PerfectDegreePairing] = None,
    dual_chart_dimensions: Optional[Mapping[int, int]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    return verify_palindromicity(
        family,
        perfect_pairing=perfect_pairing,
        dual_chart_dimensions=dual_chart_dimensions,
        **kwargs,
    )


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


def lcm_list(values: List[int]) -> int:
    return reduce(_lcm, values)
