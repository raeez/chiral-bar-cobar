r"""Typed chiral-Hochschild audit surface.

The executable layer in this module has two parts.

* Exact input arithmetic: strong-generator weights, parities, type-A Lie
  dimensions, Sugawara central charges, and elementary OPE constraints.
* Epistemic transport: a family support datum ``H_H(A; S)`` or a named
  bounded-to-chart comparison carries a bounded calculation to the completed
  curve-level chiral Hochschild complex.

The default family constructors supply the first part.  They leave chart-level
Betti numbers, Hilbert polynomials, dual-centre identifications, outer-
derivation quotients, Gerstenhaber classes, and spectral-sequence collapse as
open obligations.  This separation implements the theorem in
``chapters/theory/chiral_hochschild_koszul.tex``:

    H_H(A; S)  ==>  Supp ChirHoch^bullet(A) subset S.

Bakalov--De Sole--Kac provide two bounded benchmarks used here:

* rank-one even superboson: dimensions ``(2, 1, 0, ...)``;
* Virasoro: one-dimensional groups in degrees ``{0, 2, 3}``.

Each chart-level use of these benchmarks names a bounded-to-chart
quasi-isomorphism.  Affine, beta-gamma, bc, free-fermion, lattice, and
principal-W rows require their own family data.

Object firewall:

* ``B(A)`` is the ordered bar coalgebra;
* ``A^i = H^*(B(A))`` is its bar-cohomology coalgebra;
* ``A^!`` is a Verdier or continuous-linear dual branch under its own
  hypotheses;
* ``Omega(B(A)) -> A`` is bar--cobar reconstruction;
* ``Z_ch^der(A) = RHom_{A^e}(A,A)`` is the chiral Hochschild cochain object.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Mapping, Optional, Tuple

from sympy import Rational, Symbol, simplify, sympify


HOLOGRAPHIC_PACKAGE_ENTRIES: Tuple[str, ...] = (
    "A",
    "A^i",
    "A^!",
    "C",
    "r(z)",
    "Theta_A",
    "nabla^hol",
)

MODULAR_KOSZUL_PRIMARY_PROJECTIONS: Tuple[str, ...] = (
    "Fact_X(L)",
    "barB_X(L)",
    "Theta_L",
    "L_L",
    "(V_L^br, T_L^br)",
    "R_4^mod(L)",
)

THEOREM_H_REQUIRED_COMPONENTS: Tuple[str, ...] = (
    "complete_chart_complex_Q_A",
    "quasi_isomorphism_gamma_A_to_completed_chiral_cochains",
    "support_model_K_A_S",
    "inclusion_i_A",
    "projection_p_A",
    "contracting_homotopy_h_A",
    "incidence_and_bar_face_compatibility",
    "averaging_and_Mittag_Leffler_comparison",
)

BOUNDED_TO_CHART_OBLIGATION = (
    "construct a chain map from the bounded vertex cochain complex to the "
    "completed curve-level chart complex and prove that it is a quasi-isomorphism"
)


class OpenChirHochComputation(RuntimeError):
    """Raised when a numerical chart invariant is requested from open data."""


def holographic_package_entries() -> Tuple[str, ...]:
    return HOLOGRAPHIC_PACKAGE_ENTRIES


def modular_koszul_primary_projections() -> Tuple[str, ...]:
    return MODULAR_KOSZUL_PRIMARY_PROJECTIONS


def bar_koszul_derived_center_firewall() -> Dict[str, str]:
    """Return the distinct mathematical roles of the five constructions."""

    return {
        "A": "input chiral algebra",
        "B(A)": "ordered bar coalgebra before cohomology",
        "A^i": "bar-cohomology coalgebra H^*(B(A))",
        "A^!": (
            "Verdier/continuous-linear dual branch of A^i under finite-type "
            "or completed hypotheses"
        ),
        "Omega(B(A))": "bar--cobar reconstruction of A",
        "Z_ch^der(A)": "RHom_{A^e}(A,A), the chiral Hochschild cochain object",
        "two-sided bar": "cofibrant replacement of the diagonal A-bimodule",
    }


@dataclass(frozen=True)
class ChiralAlgebraData:
    """Exact family-level input data used before any cohomology transport."""

    name: str
    regime: str
    n_generators: int
    gen_weights: Tuple[Any, ...]
    lie_type: Optional[str] = None
    lie_rank: Optional[int] = None
    lie_dim: Optional[int] = None
    level: Any = None
    central_charge: Any = None
    parity: Tuple[int, ...] = ()
    ope_summary: Mapping[str, Any] = field(default_factory=dict)

    def is_km(self) -> bool:
        return self.lie_type is not None and self.lie_rank is not None

    def is_free_field(self) -> bool:
        return self.name in {
            "heisenberg",
            "betagamma",
            "bc_ghosts",
            "free_fermion",
        }

    def is_w_algebra(self) -> bool:
        return self.regime == "w_algebra"

    def dual_coxeter(self) -> Optional[int]:
        if self.lie_type == "A" and self.lie_rank is not None:
            return self.lie_rank + 1
        return None

    def is_critical_level(self) -> bool:
        h_dual = self.dual_coxeter()
        if h_dual is None:
            return False
        try:
            return simplify(self.level + h_dual) == 0
        except TypeError:
            return False


def heisenberg_data(k: Any = None) -> ChiralAlgebraData:
    level = Symbol("k") if k is None else sympify(k)
    return ChiralAlgebraData(
        name="heisenberg",
        regime="quadratic-presentation",
        n_generators=1,
        gen_weights=(1,),
        level=level,
        central_charge=1,
        parity=(0,),
        ope_summary={"alpha_alpha_double_pole": level},
    )


def affine_slN_data(N: int, k: Any = None) -> ChiralAlgebraData:
    if not isinstance(N, int) or N < 2:
        raise ValueError("N must be an integer at least 2")
    level = Symbol("k") if k is None else sympify(k)
    if k is not None and simplify(level + N) == 0:
        central_charge = None
    else:
        central_charge = simplify((N * N - 1) * level / (level + N))
    return ChiralAlgebraData(
        name=f"affine_sl{N}",
        regime="quadratic-presentation",
        n_generators=N * N - 1,
        gen_weights=(1,) * (N * N - 1),
        lie_type="A",
        lie_rank=N - 1,
        lie_dim=N * N - 1,
        level=level,
        central_charge=central_charge,
        parity=(0,) * (N * N - 1),
        ope_summary={
            "simple_pole": "[x,y]",
            "double_pole": "kappa(x,y)",
        },
    )


def affine_sl2_data(k: Any = None) -> ChiralAlgebraData:
    return affine_slN_data(2, k)


def affine_sl3_data(k: Any = None) -> ChiralAlgebraData:
    return affine_slN_data(3, k)


def betagamma_data() -> ChiralAlgebraData:
    return ChiralAlgebraData(
        name="betagamma",
        regime="quadratic-presentation",
        n_generators=2,
        gen_weights=(1, 0),
        central_charge=2,
        parity=(0, 0),
        ope_summary={"beta_gamma_simple_pole": 1},
    )


def bc_ghosts_data() -> ChiralAlgebraData:
    return ChiralAlgebraData(
        name="bc_ghosts",
        regime="quadratic-presentation",
        n_generators=2,
        gen_weights=(2, -1),
        central_charge=-26,
        parity=(1, 1),
        ope_summary={"b_c_simple_pole": 1},
    )


def free_fermion_data() -> ChiralAlgebraData:
    return ChiralAlgebraData(
        name="free_fermion",
        regime="quadratic-presentation",
        n_generators=1,
        gen_weights=(Rational(1, 2),),
        central_charge=Rational(1, 2),
        parity=(1,),
        ope_summary={"psi_psi_simple_pole": 1},
    )


def virasoro_data(c: Any = None) -> ChiralAlgebraData:
    central_charge = Symbol("c") if c is None else sympify(c)
    return ChiralAlgebraData(
        name="virasoro",
        regime="w_algebra",
        n_generators=1,
        gen_weights=(2,),
        central_charge=central_charge,
        parity=(0,),
        ope_summary={
            "TT_pole_4": central_charge / 2,
            "TT_pole_2": "2T",
            "TT_pole_1": "dT",
        },
    )


def wN_data(N: int, c: Any = None) -> ChiralAlgebraData:
    if not isinstance(N, int) or N < 2:
        raise ValueError("N must be an integer at least 2")
    central_charge = Symbol("c") if c is None else sympify(c)
    return ChiralAlgebraData(
        name=f"w{N}",
        regime="w_algebra",
        n_generators=N - 1,
        gen_weights=tuple(range(2, N + 1)),
        lie_type="A",
        lie_rank=N - 1,
        central_charge=central_charge,
        parity=(0,) * (N - 1),
        ope_summary={"principal_W_generating_weights": tuple(range(2, N + 1))},
    )


def w3_data(c: Any = None) -> ChiralAlgebraData:
    return wN_data(3, c)


@dataclass(frozen=True)
class FamilySupportDatum:
    r"""A typed instance of the hypothesis package ``H_H(A; S)``."""

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
    status: str = "assumed-H_H"

    def __post_init__(self) -> None:
        normalized = tuple(sorted(set(self.support)))
        if normalized != self.support:
            raise ValueError("support must be a strictly increasing tuple")
        if self.model_dimensions is not None:
            extra = set(self.model_dimensions) - set(self.support)
            if extra:
                raise ValueError("model dimensions must be supported on S")
        if any(value == "" for value in self.named_components.values()):
            raise ValueError("every component of H_H(A;S) must be named")

    @property
    def named_components(self) -> Dict[str, str]:
        return {
            "complete_chart_complex_Q_A": self.complete_chart_complex,
            "quasi_isomorphism_gamma_A_to_completed_chiral_cochains": (
                self.chart_comparison_map
            ),
            "support_model_K_A_S": self.support_model,
            "inclusion_i_A": self.inclusion,
            "projection_p_A": self.projection,
            "contracting_homotopy_h_A": self.contracting_homotopy,
            "incidence_and_bar_face_compatibility": (
                self.incidence_and_bar_face_compatibility
            ),
            "averaging_and_Mittag_Leffler_comparison": (
                self.completion_and_averaging_map
            ),
        }


@dataclass(frozen=True)
class BoundedCohomologyBenchmark:
    family: str
    complex_name: str
    support: Tuple[int, ...]
    dimensions: Mapping[int, int]
    source: str
    status: str = "proved-bounded-complex"

    @property
    def vector(self) -> Tuple[int, ...]:
        if not self.support:
            return ()
        return tuple(self.dimensions.get(n, 0) for n in range(max(self.support) + 1))

    def dimension(self, degree: int) -> int:
        return self.dimensions.get(degree, 0)

    def prefix(self, max_degree: int) -> Tuple[int, ...]:
        if max_degree < 0:
            return ()
        return tuple(self.dimension(n) for n in range(max_degree + 1))


@dataclass(frozen=True)
class BoundedToChartComparison:
    family: str
    map_name: str
    source_complex: str
    target_complex: str
    quasi_isomorphism_status: str = "open"

    @property
    def supplies_transport(self) -> bool:
        return self.quasi_isomorphism_status in {"assumed", "proved-elsewhere"}


@dataclass(frozen=True)
class KoszulDualityDatum:
    """Named perfect-pairing input for a chart/dual-chart comparison."""

    family: str
    dual_family: str
    pairing_map: str
    cohomological_shift: int
    perfectness_status: str = "assumed"

    @property
    def supplies_pairing(self) -> bool:
        return self.perfectness_status in {"assumed", "proved-elsewhere"}


def bounded_cohomology_benchmark(
    data: ChiralAlgebraData,
) -> Optional[BoundedCohomologyBenchmark]:
    """Return precisely the two BDSK bounded calculations used here."""

    if data.name == "heisenberg":
        return BoundedCohomologyBenchmark(
            family=data.name,
            complex_name="C^bullet_ch,b(B_h,B_h)",
            support=(0, 1),
            dimensions={0: 2, 1: 1},
            source="Bakalov--De Sole--Kac (2021), Theorem 7.4",
        )
    if data.name == "virasoro":
        return BoundedCohomologyBenchmark(
            family=data.name,
            complex_name="C^bullet_ch,b(Vir_c,Vir_c)",
            support=(0, 2, 3),
            dimensions={0: 1, 2: 1, 3: 1},
            source="Bakalov--De Sole--Kac (2021), Theorem 7.2",
        )
    return None


@dataclass(frozen=True)
class DerivationAnalysis:
    family: str
    total_derivations: Optional[int]
    inner_derivations: Optional[int]
    outer_derivations: Optional[int]
    known_inner_zero_mode_dimension: Optional[int]
    candidate_derivations: Mapping[str, str]
    exact_ope_constraints: Mapping[str, Any]
    parameter_tangents: Mapping[str, str]
    status: str
    resolution_obligation: str

    @property
    def dim_chirhoch1(self) -> Optional[int]:
        return self.outer_derivations

    @property
    def derivation_types(self) -> Mapping[str, str]:
        return self.candidate_derivations

    @property
    def obstruction_to_extension(self) -> Mapping[str, Optional[bool]]:
        return {name: None for name in self.candidate_derivations}


def derivation_analysis(data: ChiralAlgebraData) -> DerivationAnalysis:
    """Return exact candidate tests and the open full quotient."""

    common_obligation = (
        "construct the completed chiral derivation complex, solve its cocycle "
        "equations in every conformal-weight window, compute all inner "
        "coderivations, and pass through the chart comparison"
    )
    if data.is_km():
        dim_g = data.lie_dim
        return DerivationAnalysis(
            family=data.name,
            total_derivations=None,
            inner_derivations=None,
            outer_derivations=None,
            known_inner_zero_mode_dimension=dim_g,
            candidate_derivations={
                "adjoint_zero_modes": (
                    "x_(0) acts by [x,-] and spans a known inner subspace"
                ),
                "level_motion": "motion of the OPE bilinear form",
            },
            exact_ope_constraints={
                "adjoint_zero_mode_dimension": dim_g,
                "zero_mode_action": "(J^a)_(0) J^b = f^{ab}_c J^c",
            },
            parameter_tangents={"level": "formal OPE-family direction"},
            status="open-complete-chiral-derivation-quotient",
            resolution_obligation=common_obligation,
        )
    if data.name == "heisenberg":
        return DerivationAnalysis(
            family=data.name,
            total_derivations=None,
            inner_derivations=None,
            outer_derivations=None,
            known_inner_zero_mode_dimension=0,
            candidate_derivations={
                "shift": "D(alpha)=1 satisfies the generator-level OPE equation",
                "rescaling": "D(alpha)=a alpha requires D(k)=2ak",
            },
            exact_ope_constraints={
                "fixed_fibre_rescaling": "2ak=0",
                "shift_singular_part": 0,
            },
            parameter_tangents={"level": "formal OPE-family direction"},
            status="open-bounded-to-chart-derivation-transport",
            resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
        )
    if data.name == "virasoro":
        return DerivationAnalysis(
            family=data.name,
            total_derivations=None,
            inner_derivations=None,
            outer_derivations=None,
            known_inner_zero_mode_dimension=None,
            candidate_derivations={"weight_preserving": "D(T)=aT"},
            exact_ope_constraints={"central_charge_motion": "D(c)=2ac"},
            parameter_tangents={"central_charge": "formal OPE-family direction"},
            status="open-complete-chiral-derivation-quotient",
            resolution_obligation=common_obligation,
        )
    if data.name.startswith("w"):
        return DerivationAnalysis(
            family=data.name,
            total_derivations=None,
            inner_derivations=None,
            outer_derivations=None,
            known_inner_zero_mode_dimension=None,
            candidate_derivations={
                "generator_weight_preserving_maps": (
                    "finite low-weight ansatz before the full Borcherds system"
                )
            },
            exact_ope_constraints={
                "strong_generator_weights": data.gen_weights,
                "central_charge": data.central_charge,
            },
            parameter_tangents={"central_charge": "formal OPE-family direction"},
            status="open-family-specific-linearized-Borcherds-system",
            resolution_obligation=common_obligation,
        )
    return DerivationAnalysis(
        family=data.name,
        total_derivations=None,
        inner_derivations=None,
        outer_derivations=None,
        known_inner_zero_mode_dimension=None,
        candidate_derivations={
            "charge_or_weight_motion": "generator-level OPE-compatible ansatz"
        },
        exact_ope_constraints=dict(data.ope_summary),
        parameter_tangents={"family_parameter": "formal OPE-family direction"},
        status="open-family-specific-chiral-derivation-complex",
        resolution_obligation=common_obligation,
    )


@dataclass(frozen=True)
class HochschildPolynomial:
    p0: Optional[int]
    p1: Optional[int]
    p2: Optional[int]
    status: str
    support: Optional[Tuple[int, ...]]
    resolution_obligation: str

    @property
    def coefficients(self) -> List[Optional[int]]:
        return [self.p0, self.p1, self.p2]

    @property
    def total_dimension(self) -> Optional[int]:
        if any(value is None for value in self.coefficients):
            return None
        return int(sum(self.coefficients))

    @property
    def euler_characteristic(self) -> Optional[int]:
        if any(value is None for value in self.coefficients):
            return None
        return int(self.p0 - self.p1 + self.p2)

    @property
    def is_palindromic(self) -> Optional[bool]:
        if self.p0 is None or self.p2 is None:
            return None
        return self.p0 == self.p2

    def evaluate(self, value: Any) -> Any:
        if any(coefficient is None for coefficient in self.coefficients):
            raise OpenChirHochComputation(self.resolution_obligation)
        return self.p0 + self.p1 * value + self.p2 * value * value

    def symbolic(self) -> Any:
        return self.evaluate(Symbol("t"))


@dataclass(frozen=True)
class WAlgebraHochschild:
    family: str
    gen_degrees: Tuple[int, ...]
    bounded_benchmark: Optional[BoundedCohomologyBenchmark]
    chart_support: Optional[Tuple[int, ...]]
    chart_dimensions: Optional[Mapping[int, int]]
    status: str
    resolution_obligation: str

    @property
    def amplitude(self) -> Optional[Tuple[int, int]]:
        if self.chart_support:
            return min(self.chart_support), max(self.chart_support)
        return None

    def dim_n(self, n: int) -> Optional[int]:
        if self.chart_dimensions is None:
            return None
        return self.chart_dimensions.get(n, 0)

    def poincare_series(self, max_n: int) -> List[Optional[int]]:
        return [self.dim_n(n) for n in range(max_n + 1)]

    @property
    def total_dim(self) -> Optional[int]:
        if self.chart_dimensions is None:
            return None
        return sum(self.chart_dimensions.values())

    @property
    def bounded_by_theorem_h(self) -> Optional[bool]:
        return None if self.chart_support is None else True


@dataclass(frozen=True)
class DeformationObstruction:
    deformation_name: str
    cohomological_degree: Optional[int]
    obstruction_class: Optional[str]
    is_unobstructed: Optional[bool]
    status: str
    reason: str


@dataclass(frozen=True)
class KoszulDualityRelation:
    family_A: str
    family_A_dual: str
    betti_A: Optional[List[int]]
    betti_A_dual: Optional[List[int]]
    relation_satisfied: Optional[bool]
    status: str
    resolution_obligation: str


@dataclass(frozen=True)
class ChirHochResult:
    data: ChiralAlgebraData
    dim_H0: Optional[int]
    dim_H1: Optional[int]
    dim_H2: Optional[int]
    support: Optional[Tuple[int, ...]]
    dimensions: Optional[Mapping[int, int]]
    polynomial: Optional[HochschildPolynomial]
    w_hochschild: Optional[WAlgebraHochschild]
    derivation_info: DerivationAnalysis
    obstructions: Tuple[DeformationObstruction, ...]
    all_unobstructed: Optional[bool]
    bounded_benchmark: Optional[BoundedCohomologyBenchmark]
    status: str
    hypothesis_package: Tuple[str, ...]
    resolution_obligation: str

    @property
    def poincare_polynomial(self) -> Optional[List[int]]:
        if self.dimensions is None:
            return None
        if set(self.dimensions).issubset({0, 1, 2}):
            return [self.dimensions.get(n, 0) for n in range(3)]
        return None


def _transported_dimensions(
    data: ChiralAlgebraData,
    comparison: Optional[BoundedToChartComparison],
) -> Tuple[Optional[Tuple[int, ...]], Optional[Mapping[int, int]], str]:
    benchmark = bounded_cohomology_benchmark(data)
    if benchmark is None or comparison is None:
        return None, None, "open-family-support-datum"
    if comparison.family != data.name:
        raise ValueError("comparison family differs from the chiral algebra family")
    if comparison.source_complex != benchmark.complex_name:
        raise ValueError("comparison source differs from the bounded benchmark complex")
    if comparison.supplies_transport:
        return (
            benchmark.support,
            dict(benchmark.dimensions),
            f"conditional-{comparison.quasi_isomorphism_status}-bounded-to-chart",
        )
    return None, None, "open-bounded-to-chart-comparison"


def compute_chirhoch(
    data: ChiralAlgebraData,
    *,
    family_datum: Optional[FamilySupportDatum] = None,
    bounded_to_chart: Optional[BoundedToChartComparison] = None,
) -> ChirHochResult:
    """Return a status-typed chart result from explicit comparison data."""

    benchmark = bounded_cohomology_benchmark(data)
    dimensions: Optional[Mapping[int, int]] = None
    support: Optional[Tuple[int, ...]] = None
    status = "open-family-support-datum"

    if family_datum is not None:
        if family_datum.family != data.name:
            raise ValueError("H_H family differs from the chiral algebra family")
        support = family_datum.support
        dimensions = (
            None
            if family_datum.model_dimensions is None
            else dict(family_datum.model_dimensions)
        )
        status = f"conditional-{family_datum.status}"
    else:
        support, dimensions, status = _transported_dimensions(
            data, bounded_to_chart
        )

    dim_H0 = None if dimensions is None else dimensions.get(0, 0)
    dim_H1 = None if dimensions is None else dimensions.get(1, 0)
    dim_H2 = None if dimensions is None else dimensions.get(2, 0)

    polynomial = None
    if data.regime == "quadratic-presentation":
        polynomial = HochschildPolynomial(
            p0=dim_H0,
            p1=dim_H1,
            p2=dim_H2,
            status=status,
            support=support,
            resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
        )

    w_packet = None
    if data.regime == "w_algebra":
        w_packet = WAlgebraHochschild(
            family=data.name,
            gen_degrees=tuple(int(weight) for weight in data.gen_weights),
            bounded_benchmark=benchmark,
            chart_support=support,
            chart_dimensions=dimensions,
            status=status,
            resolution_obligation=BOUNDED_TO_CHART_OBLIGATION,
        )

    return ChirHochResult(
        data=data,
        dim_H0=dim_H0,
        dim_H1=dim_H1,
        dim_H2=dim_H2,
        support=support,
        dimensions=dimensions,
        polynomial=polynomial,
        w_hochschild=w_packet,
        derivation_info=derivation_analysis(data),
        obstructions=tuple(deformation_obstruction_analysis(data)),
        all_unobstructed=None,
        bounded_benchmark=benchmark,
        status=status,
        hypothesis_package=THEOREM_H_REQUIRED_COMPONENTS,
        resolution_obligation=(
            "supply H_H(A;S) or " + BOUNDED_TO_CHART_OBLIGATION
        ),
    )


def center_dimension(
    data: ChiralAlgebraData,
    *,
    family_datum: Optional[FamilySupportDatum] = None,
    bounded_to_chart: Optional[BoundedToChartComparison] = None,
) -> Optional[int]:
    """Return the chart degree-zero dimension when a comparison supplies it."""

    return compute_chirhoch(
        data,
        family_datum=family_datum,
        bounded_to_chart=bounded_to_chart,
    ).dim_H0


def center_dimension_koszul_dual(
    data: ChiralAlgebraData,
    *,
    duality_datum: Optional[KoszulDualityDatum] = None,
    family_datum: Optional[FamilySupportDatum] = None,
    bounded_to_chart: Optional[BoundedToChartComparison] = None,
) -> Optional[int]:
    """Return the degree-two chart value after support and pairing data."""

    if duality_datum is None or not duality_datum.supplies_pairing:
        return None
    if duality_datum.family != data.name:
        raise ValueError("duality family differs from the chiral algebra family")
    result = compute_chirhoch(
        data,
        family_datum=family_datum,
        bounded_to_chart=bounded_to_chart,
    )
    return result.dim_H2


def compute_hochschild_polynomial(
    data: ChiralAlgebraData,
    *,
    family_datum: Optional[FamilySupportDatum] = None,
    bounded_to_chart: Optional[BoundedToChartComparison] = None,
) -> HochschildPolynomial:
    result = compute_chirhoch(
        data,
        family_datum=family_datum,
        bounded_to_chart=bounded_to_chart,
    )
    if result.polynomial is None:
        return HochschildPolynomial(
            p0=result.dim_H0,
            p1=result.dim_H1,
            p2=result.dim_H2,
            status=result.status,
            support=result.support,
            resolution_obligation=result.resolution_obligation,
        )
    return result.polynomial


def compute_w_algebra_hochschild(
    data: ChiralAlgebraData,
    *,
    family_datum: Optional[FamilySupportDatum] = None,
    bounded_to_chart: Optional[BoundedToChartComparison] = None,
) -> WAlgebraHochschild:
    if data.regime != "w_algebra":
        raise ValueError("the input belongs to a different presentation regime")
    packet = compute_chirhoch(
        data,
        family_datum=family_datum,
        bounded_to_chart=bounded_to_chart,
    ).w_hochschild
    assert packet is not None
    return packet


def deformation_obstruction_analysis(
    data: ChiralAlgebraData,
) -> List[DeformationObstruction]:
    parameter = "level" if data.is_km() or data.name == "heisenberg" else "central_charge"
    if data.name in {"betagamma", "bc_ghosts", "free_fermion"}:
        parameter = "presentation_parameter"
    return [
        DeformationObstruction(
            deformation_name=f"{parameter}_motion",
            cohomological_degree=None,
            obstruction_class=None,
            is_unobstructed=True,
            status="computed-formal-OPE-family",
            reason="the displayed OPE coefficients form an exact parameter family",
        ),
        DeformationObstruction(
            deformation_name="chart_Gerstenhaber_class",
            cohomological_degree=None,
            obstruction_class=None,
            is_unobstructed=None,
            status="open-chain-level-placement",
            reason=(
                "a formal parameter family acquires a chiral Hochschild degree "
                "only through an explicit cochain representative and comparison"
            ),
        ),
    ]


def all_deformations_unobstructed(data: ChiralAlgebraData) -> Optional[bool]:
    derivation_analysis(data)
    return None


def koszul_duality_check(
    data_A: ChiralAlgebraData,
    data_A_dual: ChiralAlgebraData,
) -> KoszulDualityRelation:
    return KoszulDualityRelation(
        family_A=data_A.name,
        family_A_dual=data_A_dual.name,
        betti_A=None,
        betti_A_dual=None,
        relation_satisfied=None,
        status="open-perfect-pairing-and-chart-comparison",
        resolution_obligation=(
            "construct the Koszul-dual chart, prove the completed perfect pairing, "
            "and identify both family support models"
        ),
    )


def ff_involution_on_hochschild(data: ChiralAlgebraData) -> Dict[str, Any]:
    """Return exact parameter involutions and the open cohomology transport."""

    if data.is_km():
        h_dual = data.dual_coxeter()
        dual_level = simplify(-data.level - 2 * h_dual)
        return {
            "ff_applicable": True,
            "h_dual": h_dual,
            "dual_level": dual_level,
            "parameter_involution_check": (
                simplify(-dual_level - 2 * h_dual - data.level) == 0
            ),
            "dimensions_match": None,
            "status": "open-bar-duality-and-chart-comparison",
        }
    if data.name == "virasoro":
        return {
            "ff_applicable": False,
            "dual_central_charge_candidate": simplify(26 - data.central_charge),
            "dimensions_match": None,
            "status": "open-Virasoro-duality-comparison",
        }
    if data.name in {"betagamma", "bc_ghosts"}:
        companion = "bc_ghosts" if data.name == "betagamma" else "betagamma"
        return {
            "ff_applicable": False,
            "koszul_dual_candidate": companion,
            "dimensions_match": None,
            "status": "open-free-field-bar-comparison",
        }
    return {
        "ff_applicable": False,
        "dimensions_match": None,
        "status": "outside-parameter-involution-table",
    }


def verify_additivity_under_tensor(
    data_A: ChiralAlgebraData,
    data_B: ChiralAlgebraData,
) -> Dict[str, Any]:
    return {
        "applicable": None,
        "families": (data_A.name, data_B.name),
        "P_A": None,
        "P_B": None,
        "P_product_full": None,
        "status": "open-Kunneth-map-for-completed-chiral-chart-complexes",
    }


def verify_euler_char_additivity(
    data_A: ChiralAlgebraData,
    data_B: ChiralAlgebraData,
) -> Dict[str, Any]:
    return {
        "families": (data_A.name, data_B.name),
        "matches": None,
        "status": "open-after-family-support-and-Kunneth-data",
    }


def _ope_derivation_check_heisenberg() -> Dict[str, Any]:
    a, k = Symbol("a"), Symbol("k")
    return {
        "family": "heisenberg",
        "ope": "alpha(z)alpha(w) ~ k/(z-w)^2",
        "rescaling_constraint": simplify(2 * a * k),
        "shift_singular_part": 0,
        "shift_is_generator_level_ope_compatible": True,
        "chart_outer_quotient_dim": None,
        "status": "open-bounded-to-chart-transport",
    }


def _ope_derivation_check_virasoro() -> Dict[str, Any]:
    return {
        "family": "virasoro",
        "weight_2_space_dim": 1,
        "state_space_basis_weight_2": ("T",),
        "weight_preserving_ansatz": "D(T)=aT",
        "ope_constraint": "D(c)=2ac",
        "chart_outer_quotient_dim": None,
        "bounded_support": (0, 2, 3),
        "status": "open-bounded-to-chart-transport",
    }


def _ope_derivation_check_w3() -> Dict[str, Any]:
    return {
        "family": "w3",
        "weight_2_space_dim": 1,
        "weight_3_space_dim": 2,
        "state_space_basis_weight_2": ("T",),
        "state_space_basis_weight_3": ("dT", "W"),
        "weight_preserving_ansatz": "D(T)=aT, D(W)=gW+d(dT)",
        "chart_outer_quotient_dim": None,
        "status": "open-full-linearized-W3-Borcherds-system",
    }


def compute_all_standard_families() -> Dict[str, ChirHochResult]:
    families = {
        "heisenberg": heisenberg_data(),
        "affine_sl2": affine_sl2_data(),
        "affine_sl3": affine_sl3_data(),
        "affine_sl4": affine_slN_data(4),
        "betagamma": betagamma_data(),
        "bc_ghosts": bc_ghosts_data(),
        "free_fermion": free_fermion_data(),
        "virasoro": virasoro_data(),
        "w3": w3_data(),
        "w4": wN_data(4),
    }
    return {name: compute_chirhoch(data) for name, data in families.items()}


def verify_theorem_h_complete(data: ChiralAlgebraData) -> Dict[str, Any]:
    result = compute_chirhoch(data)
    return {
        "family": data.name,
        "passed": None,
        "support": result.support,
        "dimensions": result.dimensions,
        "bounded_benchmark": result.bounded_benchmark,
        "status": result.status,
        "hypothesis_package": result.hypothesis_package,
        "resolution_obligation": result.resolution_obligation,
    }


def verify_universal_polynomial() -> Dict[str, Any]:
    return {
        "all_passed": None,
        "families": {
            name: {"polynomial": None, "status": result.status}
            for name, result in compute_all_standard_families().items()
        },
        "status": "family support models determine Hilbert series individually",
    }


def verify_km_h1_equals_dim_g() -> Dict[str, Any]:
    families: Dict[str, Dict[str, Any]] = {}
    for N in (2, 3, 4, 5, 6, 10):
        data = affine_slN_data(N)
        analysis = derivation_analysis(data)
        families[f"sl{N}"] = {
            "dim_g": data.lie_dim,
            "known_inner_zero_mode_dimension": (
                analysis.known_inner_zero_mode_dimension
            ),
            "dim_H1": None,
            "status": analysis.status,
        }
    return {
        "all_passed": None,
        "families": families,
        "claim": (
            "dim(sl_N) computes a known inner zero-mode subspace; the complete "
            "chart outer quotient remains open"
        ),
    }


def hochschild_spectral_sequence_E2(
    data: ChiralAlgebraData,
    max_p: int = 10,
    max_q: int = 4,
) -> Dict[str, Any]:
    return {
        "family": data.name,
        "shape": (max_p + 1, max_q + 1),
        "E2_page": None,
        "collapse": None,
        "status": "open-filtered-chart-complex-and-differentials",
    }


def _ce_cohomology_sl2_adjoint() -> Dict[int, int]:
    """The finite-dimensional Whitehead calculation, kept type-separated."""

    return {0: 0, 1: 0, 2: 0}


def _lie_dim(lie_type: str, rank: int) -> int:
    family = lie_type.upper()
    if family == "A":
        return (rank + 1) ** 2 - 1
    if family in {"B", "C"}:
        return rank * (2 * rank + 1)
    if family == "D":
        return rank * (2 * rank - 1)
    if family == "G" and rank == 2:
        return 14
    if family == "F" and rank == 4:
        return 52
    if family == "E" and rank in {6, 7, 8}:
        return {6: 78, 7: 133, 8: 248}[rank]
    raise ValueError(f"unknown Lie type {lie_type}_{rank}")


def whitehead_lemma_check(lie_type: str, rank: int) -> Dict[str, Any]:
    return {
        "lie_type": f"{lie_type}_{rank}",
        "dim_g": _lie_dim(lie_type, rank),
        "H1_g_g": 0,
        "H2_g_g": 0,
        "chiral_H1": None,
        "status": (
            "proved finite-dimensional Chevalley--Eilenberg calculation; "
            "chiral transport open"
        ),
    }


def summary_table() -> List[Dict[str, Any]]:
    return [
        {
            "family": name,
            "regime": result.data.regime,
            "n_gen": result.data.n_generators,
            "dim_H0": result.dim_H0,
            "dim_H1": result.dim_H1,
            "dim_H2": result.dim_H2,
            "support": result.support,
            "status": result.status,
        }
        for name, result in compute_all_standard_families().items()
    ]
