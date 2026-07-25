r"""Non-principal line restrictions and typed line-category comparisons.

The finite computational surface consists of KRW central charges, Young
diagrams, strong-generator weights and parity, BP OPE pole orders, and formal
level or quantum-parameter expressions.  These data determine restrictions to
specified generator spans.  The full shadow tower and the category of
topological lines require the comparison packages recorded below.

Categorical outputs carry named packages:

``H_line``
    dualizable boundary condition, completed topological line category, and
    the boundary-to-line comparison;

``H_DS/line``
    a filtered BRST functor on line objects, convergence, and descent to the
    completed category;

``H_hook^{DS/bar}``
    filtered DS/bar comparison, strict completion, and a perfect Verdier
    pairing;

``H_KSDual``
    an object-level fixed-point equivalence compatible with the preceding
    packages.

For Bershadsky--Polyakov, the standard FKR central charge has formal reflected
sum ``50``.  The shifted secondary formula has formal reflected sum ``196``.
The unsigned reciprocal-weight diagnostic is ``17/6``.  The modular quantities
``rho``, ``kappa``, and ``K^kappa`` remain open.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import I, Rational, Symbol, exp, pi, simplify, sympify

from compute.lib.non_principal_w_bar_engine import (
    ClaimPacket,
    ClaimStatus,
    GeneratorSpec,
    OpenInvariantError,
    bershadsky_polyakov_central_charge,
    bershadsky_polyakov_ope_data,
    bershadsky_polyakov_reciprocal_weight_diagnostic,
    bershadsky_polyakov_shifted_central_charge,
    formal_level_reflection,
    type_a_krw_central_charge,
    type_a_strong_generators,
)
from compute.lib.nonprincipal_ds_orbits import (
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
)


k = Symbol("k")
H_LINE = (
    "H_line: dualizable boundary condition, completed topological line "
    "category, and boundary-to-line comparison"
)
H_DS_LINE = (
    "H_DS/line: filtered BRST functor on line objects, convergence, and "
    "descent to the completed category"
)
H_HOOK_DS_BAR = (
    "H_hook^{DS/bar}: filtered DS/bar comparison, strict completion, "
    "and a finite or continuously perfect Verdier pairing"
)
H_KSDUAL = (
    "H_KSDual: object-level fixed-point equivalence compatible with "
    "H_line, H_DS/line, and H_hook^{DS/bar}"
)


def _open(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.OPEN, None, hypotheses=tuple(hypotheses))


def _conditional(statement: str, *hypotheses: str) -> ClaimPacket:
    return ClaimPacket(statement, ClaimStatus.CONDITIONAL, None, hypotheses=tuple(hypotheses))


@dataclass(frozen=True)
class LineRestrictionData:
    """Exact OPE closure data for a specified generator span."""

    name: str
    generators: Tuple[str, ...]
    closure: str
    exact_ope_channels: Tuple[Tuple[str, str, int], ...]
    full_shadow_depth: ClaimPacket


@dataclass(frozen=True)
class GeneratorData:
    """Exact generator ledger with line restrictions and typed full depth."""

    name: str
    generators: Tuple[Tuple[str, object, str], ...]
    num_even: int
    num_odd: int
    reciprocal_weight_diagnostic: Rational
    line_restrictions: Tuple[LineRestrictionData, ...]
    full_shadow_depth: ClaimPacket
    rho: ClaimPacket

    @property
    def num_bosonic(self) -> int:
        return self.num_even

    @property
    def num_fermionic(self) -> int:
        return self.num_odd

    @property
    def anomaly_ratio(self) -> ClaimPacket:
        return self.rho

    @property
    def shadow_depth_T(self) -> ClaimPacket:
        return self.full_shadow_depth

    @property
    def shadow_class_T(self) -> ClaimPacket:
        return self.full_shadow_depth


@dataclass(frozen=True)
class LineOperatorCategoryData:
    """Exact indexing data and typed line-category comparison claims."""

    algebra_name: str
    partition: Tuple[int, ...]
    N: int
    transpose: Tuple[int, ...]
    formal_reflected_level: object
    formal_quantum_parameter: object
    ds_reduction_type: str
    line_category_equivalence: ClaimPacket
    ds_line_functor: ClaimPacket
    ds_bar_commutation: ClaimPacket
    same_family_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def dual_level_formula(self) -> str:
        return f"k' = {self.formal_reflected_level}"

    @property
    def is_self_transpose(self) -> bool:
        """Return the exact Young-diagram fixed-point condition."""

        return self.partition == self.transpose

    @property
    def is_self_dual(self) -> ClaimPacket:
        """Compatibility surface carrying the conditional duality claim."""

        return self.same_family_duality

    @property
    def proof_status(self) -> ClaimStatus:
        return self.line_category_equivalence.status


@dataclass(frozen=True)
class DSLineReductionDiagram:
    """Exact diagram indices and typed comparison arrows."""

    N: int
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    is_self_transpose: bool
    formal_reflected_level: object
    source_algebra: str
    target_algebra: str
    reflected_source_algebra: str
    reflected_target_algebra: str
    algebraic_ds_reduction: ClaimPacket
    source_line_category: ClaimPacket
    target_line_category: ClaimPacket
    ds_line_functor: ClaimPacket
    ds_bar_commutation: ClaimPacket
    diagram_commutes: ClaimPacket


@dataclass(frozen=True)
class OPEChannelData:
    """One primary-source BP OPE pole order and its conditional extraction."""

    source_generator: str
    target_generator: str
    ope_max_pole: int
    channel_type: str
    source: str
    rmatrix_extraction: ClaimPacket

    @property
    def source_gen(self) -> str:
        return self.source_generator

    @property
    def target_gen(self) -> str:
        return self.target_generator

    @property
    def rmatrix_max_pole(self) -> ClaimPacket:
        return self.rmatrix_extraction


RMatrixChannelData = OPEChannelData


@dataclass(frozen=True)
class NonPrincipalLineOperatorEntry:
    """One catalog entry with exact scalar data and typed frontier fields."""

    algebra_name: str
    lie_algebra: str
    N: int
    partition: Tuple[int, ...]
    transpose: Tuple[int, ...]
    nilpotent_type: str
    central_charge: object
    central_scalar_reflection_sum: object
    shifted_secondary_sum: object
    reciprocal_weight_diagnostic: Rational
    rho: ClaimPacket
    kappa: ClaimPacket
    modular_conductor: ClaimPacket
    full_shadow_depth: ClaimPacket
    line_category: LineOperatorCategoryData
    ds_diagram: DSLineReductionDiagram
    ope_channels: Tuple[OPEChannelData, ...]


def bp_central_charge(level=k):
    """Return the standard FKR BP central charge."""

    return bershadsky_polyakov_central_charge(sympify(level))


def bp_shifted_central_charge(level=k):
    """Return the shifted secondary BP comparison scalar."""

    return bershadsky_polyakov_shifted_central_charge(sympify(level))


def principal_w3_central_charge(level=k):
    """Return the principal ``W_3`` central charge in the standard convention."""

    return type_a_krw_central_charge((3,), sympify(level))


def principal_wn_central_charge(N: int, level=k):
    """Return the principal ``W_N`` central charge from KRW."""

    return type_a_krw_central_charge((N,), sympify(level))


def affine_central_charge(N: int, level=k):
    """Return the Sugawara central charge of ``V_k(sl_N)``."""

    return type_a_krw_central_charge((1,) * N, sympify(level))


def virasoro_central_charge(level=k):
    """Return the principal ``sl_2`` Virasoro central charge."""

    return type_a_krw_central_charge((2,), sympify(level))


def ff_dual_level(N: int, level=k):
    """Return the formal reflection ``k -> -k-2N``."""

    return formal_level_reflection(N, sympify(level))


def bp_dual_level(level=k):
    """Return the BP formal reflection ``k -> -k-6``."""

    return ff_dual_level(3, level)


def bp_standard_central_reflection_sum(level=k):
    """Return the standard BP central scalar sum under formal reflection."""

    kk = sympify(level)
    return simplify(bp_central_charge(kk) + bp_central_charge(bp_dual_level(kk)))


def bp_shifted_central_reflection_sum(level=k):
    """Return the shifted secondary BP scalar sum under formal reflection."""

    kk = sympify(level)
    return simplify(bp_shifted_central_charge(kk) + bp_shifted_central_charge(bp_dual_level(kk)))


def principal_wn_central_reflection_sum(N: int, level=k):
    """Return the principal central scalar sum under formal reflection."""

    kk = sympify(level)
    return simplify(
        principal_wn_central_charge(N, kk)
        + principal_wn_central_charge(N, ff_dual_level(N, kk))
    )


def koszul_conductor_bp() -> ClaimPacket:
    """Return the open BP modular-conductor packet."""

    return _open(
        "K_BP^kappa",
        "BP modular characteristics at both formal reflected levels",
        H_HOOK_DS_BAR,
    )


def koszul_conductor_principal_wn(N: int) -> ClaimPacket:
    """Return the open principal modular-conductor packet."""

    return _open(
        f"K^kappa for principal W_{N}",
        "modular characteristics in one convention at both reflected levels",
    )


def bp_anomaly_ratio() -> ClaimPacket:
    return _open(
        "rho_BP",
        "a nonseparating genus-one calculation",
        "identification of the contributing modular channel",
    )


def bp_kappa(level=k) -> ClaimPacket:
    return _open(
        f"kappa_BP({sympify(level)})",
        "a nonseparating genus-one calculation with charged, neutral, improvement, and mixed channels",
    )


def principal_w3_anomaly_ratio() -> ClaimPacket:
    return _open("rho_W3", "a genus-one modular calculation")


def principal_w3_kappa(level=k) -> ClaimPacket:
    return _open(f"kappa_W3({sympify(level)})", "a genus-one modular calculation")


def virasoro_anomaly_ratio() -> ClaimPacket:
    return _open("rho_Vir", "a genus-one modular calculation in the manuscript convention")


def virasoro_kappa(level=k) -> ClaimPacket:
    return _open(f"kappa_Vir({sympify(level)})", "a genus-one modular calculation")


def bp_kappa_complementarity() -> ClaimPacket:
    return koszul_conductor_bp()


def principal_w3_kappa_complementarity() -> ClaimPacket:
    return koszul_conductor_principal_wn(3)


def _restriction_depth(name: str) -> ClaimPacket:
    return _open(
        f"full shadow depth determined from the {name} restriction",
        "the full Maurer--Cartan tower and a reconstruction theorem from the restriction",
    )


def bp_line_restrictions() -> Tuple[LineRestrictionData, ...]:
    """Return exact BP OPE closure data for four natural generator spans."""

    return (
        LineRestrictionData(
            name="Heisenberg J-line",
            generators=("J",),
            closure="The J-J singular OPE closes through the vacuum channel.",
            exact_ope_channels=(("J", "J", 2),),
            full_shadow_depth=_restriction_depth("Heisenberg J-line"),
        ),
        LineRestrictionData(
            name="Virasoro L-line",
            generators=("L",),
            closure="The L-L singular OPE closes through L, its derivative, and the vacuum.",
            exact_ope_channels=(("L", "L", 4),),
            full_shadow_depth=_restriction_depth("Virasoro L-line"),
        ),
        LineRestrictionData(
            name="charged self-lines",
            generators=("G+", "G-"),
            closure="Each charged self-OPE is regular.",
            exact_ope_channels=(("G+", "G+", 0), ("G-", "G-", 0)),
            full_shadow_depth=_restriction_depth("charged self-lines"),
        ),
        LineRestrictionData(
            name="charged pair",
            generators=("G+", "G-"),
            closure="The mixed channel generates J, L, dJ, and :JJ:.",
            exact_ope_channels=(("G+", "G-", 3),),
            full_shadow_depth=_restriction_depth("charged pair"),
        ),
    )


def _generator_data(name: str, partition) -> GeneratorData:
    generators = type_a_strong_generators(partition)
    ledger = tuple(
        (generator.label, generator.conformal_weight, generator.parity)
        for generator in generators
    )
    diagnostic = sum(Rational(1) / Rational(generator.conformal_weight) for generator in generators)
    restrictions = bp_line_restrictions() if normalize_partition(partition) == (2, 1) else ()
    return GeneratorData(
        name=name,
        generators=ledger,
        num_even=len(generators),
        num_odd=0,
        reciprocal_weight_diagnostic=diagnostic,
        line_restrictions=restrictions,
        full_shadow_depth=_open(
            f"full shadow depth of {name}",
            "the full Maurer--Cartan coefficient tower",
        ),
        rho=_open(f"rho of {name}", "a genus-one modular calculation"),
    )


def bp_generator_data() -> GeneratorData:
    return _generator_data("Bershadsky--Polyakov", (2, 1))


def principal_w3_generator_data() -> GeneratorData:
    return _generator_data("principal W_3", (3,))


def virasoro_generator_data() -> GeneratorData:
    return _generator_data("Virasoro", (2,))


def _line_operator_data(partition, algebra_name: str) -> LineOperatorCategoryData:
    lam = normalize_partition(partition)
    N = partition_size(lam)
    lam_t = transpose_partition(lam)
    reflected = ff_dual_level(N, k)
    return LineOperatorCategoryData(
        algebra_name=algebra_name,
        partition=lam,
        N=N,
        transpose=lam_t,
        formal_reflected_level=reflected,
        formal_quantum_parameter=exp(pi * I / (k + N)),
        ds_reduction_type=type_a_orbit_class(lam),
        line_category_equivalence=_conditional(
            f"line-category equivalence for {algebra_name}",
            H_LINE,
        ),
        ds_line_functor=_conditional(
            f"DS functor on line objects for {algebra_name}",
            H_DS_LINE,
        ),
        ds_bar_commutation=_conditional(
            f"DS--bar comparison for {algebra_name}",
            H_HOOK_DS_BAR,
        ),
        same_family_duality=_conditional(
            f"same- or transpose-family duality candidate for {algebra_name}",
            H_HOOK_DS_BAR,
        ),
        ksdual_membership=_conditional(
            f"KSDual membership for {algebra_name}",
            H_KSDUAL,
        ),
    )


def affine_line_operators(N: int, level=k) -> LineOperatorCategoryData:
    return _line_operator_data((1,) * N, f"V_{sympify(level)}(sl_{N})")


def bp_line_operators() -> LineOperatorCategoryData:
    return _line_operator_data((2, 1), "Bershadsky--Polyakov")


def principal_w3_line_operators() -> LineOperatorCategoryData:
    return _line_operator_data((3,), "principal W_3")


def sl4_hook_31_line_operators() -> LineOperatorCategoryData:
    return _line_operator_data((3, 1), "W^k(sl_4,f_(3,1))")


def sl4_hook_211_line_operators() -> LineOperatorCategoryData:
    return _line_operator_data((2, 1, 1), "W^k(sl_4,f_(2,1,1))")


def _proved_elsewhere(statement: str, value=True, *evidence: str) -> ClaimPacket:
    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.PROVED_ELSEWHERE,
        value=value,
        evidence=tuple(evidence),
    )


def ds_line_reduction_diagram(partition, N=None) -> DSLineReductionDiagram:
    """Return exact partition indices and typed arrows for the DS/line square."""

    lam = normalize_partition(partition)
    actual_N = partition_size(lam)
    if N is not None and N != actual_N:
        raise ValueError(f"partition {lam} has size {actual_N}, while N={N}")
    lam_t = transpose_partition(lam)
    reflected = ff_dual_level(actual_N, k)
    return DSLineReductionDiagram(
        N=actual_N,
        partition=lam,
        transpose=lam_t,
        is_self_transpose=lam == lam_t,
        formal_reflected_level=reflected,
        source_algebra=f"V_k(sl_{actual_N})",
        target_algebra=f"W_k(sl_{actual_N},f_{lam})",
        reflected_source_algebra=f"V_({reflected})(sl_{actual_N})",
        reflected_target_algebra=f"W_({reflected})(sl_{actual_N},f_{lam_t})",
        algebraic_ds_reduction=_proved_elsewhere(
            f"quantum DS reduction indexed by {lam}",
            True,
            "Kac--Roan--Wakimoto (2003)",
        ),
        source_line_category=_conditional("source line-category identification", H_LINE),
        target_line_category=_conditional("target line-category identification", H_LINE),
        ds_line_functor=_conditional("DS functor on completed line categories", H_DS_LINE),
        ds_bar_commutation=_conditional("DS--bar comparison in the diagram", H_HOOK_DS_BAR),
        diagram_commutes=_conditional(
            f"commutativity of the DS/line square for {lam}",
            H_LINE,
            H_DS_LINE,
            H_HOOK_DS_BAR,
        ),
    )


def virasoro_shadow_tower(c_val, max_arity=10) -> ClaimPacket:
    """Return the typed open higher-shadow packet for a Virasoro restriction."""

    return _open(
        f"Virasoro-line shadow tower through arity {max_arity} at c={sympify(c_val)}",
        "a derivation of every Maurer--Cartan coefficient in the manuscript normalization",
    )


def bp_shadow_tower_on_tline(max_arity=8) -> ClaimPacket:
    """Return the typed open BP Virasoro-line shadow packet."""

    return virasoro_shadow_tower(bp_central_charge(k), max_arity)


def shadow_depth_classification(c_val) -> ClaimPacket:
    """Return the typed open full-depth classification packet."""

    return _open(
        f"full shadow depth at central charge {sympify(c_val)}",
        "all generator channels and the full Maurer--Cartan tower",
    )


def bp_shadow_depth() -> Dict[str, object]:
    """Return exact BP line restrictions and the open full-depth packet."""

    return {
        "line_restrictions": bp_line_restrictions(),
        "full_shadow_depth": shadow_depth_classification(bp_central_charge(k)),
    }


def bp_ope_channels() -> Tuple[OPEChannelData, ...]:
    """Return the directed singular BP OPE channels in FKR equation (2.1)."""

    source = "Fehily--Kawasetsu--Ridout (2021), Definition 2.1, equation (2.1)"
    channel_specs = (
        ("L", "L", 4),
        ("L", "J", 2),
        ("L", "G+", 2),
        ("L", "G-", 2),
        ("J", "J", 2),
        ("J", "G+", 1),
        ("J", "G-", 1),
        ("G+", "G+", 0),
        ("G-", "G-", 0),
        ("G+", "G-", 3),
    )
    return tuple(
        OPEChannelData(
            source_generator=left,
            target_generator=right,
            ope_max_pole=pole,
            channel_type="even-even",
            source=source,
            rmatrix_extraction=_conditional(
                f"collision-residue extraction from the {left}-{right} OPE channel",
                "H_OPE/r: collision-kernel normalization and residue comparison",
            ),
        )
        for left, right, pole in channel_specs
    )


def bp_rmatrix_channels() -> Tuple[OPEChannelData, ...]:
    """Compatibility API returning exact OPE channels and conditional residues."""

    return bp_ope_channels()


def bp_rmatrix_max_pole() -> ClaimPacket:
    return _conditional(
        "maximum pole order in the BP collision r-matrix",
        "H_OPE/r: collision-kernel normalization and residue comparison",
    )


def principal_w3_rmatrix_max_pole() -> ClaimPacket:
    return _conditional(
        "maximum pole order in the principal W_3 collision r-matrix",
        "the exact W-W OPE and H_OPE/r",
    )


def _catalog_entry(name: str, partition) -> NonPrincipalLineOperatorEntry:
    lam = normalize_partition(partition)
    N = partition_size(lam)
    central_charge = type_a_krw_central_charge(lam, k)
    is_bp = lam == (2, 1)
    standard_sum = (
        bp_standard_central_reflection_sum(k)
        if is_bp
        else simplify(
            central_charge + type_a_krw_central_charge(lam, ff_dual_level(N, k))
        )
    )
    shifted_sum = bp_shifted_central_reflection_sum(k) if is_bp else None
    diagnostic = sum(
        Rational(1) / Rational(generator.conformal_weight)
        for generator in type_a_strong_generators(lam)
    )
    return NonPrincipalLineOperatorEntry(
        algebra_name=name,
        lie_algebra=f"sl_{N}",
        N=N,
        partition=lam,
        transpose=transpose_partition(lam),
        nilpotent_type=type_a_orbit_class(lam),
        central_charge=central_charge,
        central_scalar_reflection_sum=standard_sum,
        shifted_secondary_sum=shifted_sum,
        reciprocal_weight_diagnostic=diagnostic,
        rho=_open(f"rho for {name}", "a genus-one modular calculation"),
        kappa=_open(f"kappa for {name}", "a genus-one modular calculation"),
        modular_conductor=_open(
            f"K^kappa for {name}",
            "modular characteristics at both formal reflected levels",
        ),
        full_shadow_depth=_open(
            f"full shadow depth for {name}",
            "the full Maurer--Cartan tower",
        ),
        line_category=_line_operator_data(lam, name),
        ds_diagram=ds_line_reduction_diagram(lam, N),
        ope_channels=bp_ope_channels() if is_bp else (),
    )


def build_catalog() -> Dict[str, NonPrincipalLineOperatorEntry]:
    """Build the exact scalar and typed categorical catalog through the sl4 hooks."""

    return {
        "Vir": _catalog_entry("Virasoro", (2,)),
        "BP": _catalog_entry("Bershadsky--Polyakov", (2, 1)),
        "W3": _catalog_entry("principal W_3", (3,)),
        "sl4_31": _catalog_entry("W^k(sl_4,f_(3,1))", (3, 1)),
        "sl4_211": _catalog_entry("W^k(sl_4,f_(2,1,1))", (2, 1, 1)),
    }


def bp_numerical_at_level(level_val) -> Dict[str, object]:
    """Evaluate exact BP scalar data and retain typed frontier packets."""

    level = Rational(level_val)
    reflected = bp_dual_level(level)
    return {
        "level": level,
        "formal_reflected_level": reflected,
        "standard_central_charge": bp_central_charge(level),
        "reflected_standard_central_charge": bp_central_charge(reflected),
        "standard_sum": bp_standard_central_reflection_sum(level),
        "shifted_central_charge": bp_shifted_central_charge(level),
        "shifted_sum": bp_shifted_central_reflection_sum(level),
        "reciprocal_weight_diagnostic": bershadsky_polyakov_reciprocal_weight_diagnostic(),
        "rho": bp_anomaly_ratio(),
        "kappa": bp_kappa(level),
        "modular_conductor": koszul_conductor_bp(),
    }


def quantum_parameter_at_level(N, level_val):
    """Return the formal complex value ``exp(pi i/(k+N))`` at one level."""

    import cmath

    level = float(level_val)
    return cmath.exp(cmath.pi * 1j / (level + N))


def _transpose_partition(lam):
    """Compatibility wrapper for exact partition transpose."""

    return transpose_partition(lam)


def _is_hook(lam):
    """Return the exact hook predicate for a normalized partition."""

    normalized = normalize_partition(lam)
    return len(normalized) == 1 or all(part == 1 for part in normalized[1:])


__all__ = [
    "ClaimPacket",
    "ClaimStatus",
    "OpenInvariantError",
    "LineRestrictionData",
    "GeneratorData",
    "LineOperatorCategoryData",
    "DSLineReductionDiagram",
    "OPEChannelData",
    "RMatrixChannelData",
    "NonPrincipalLineOperatorEntry",
    "bp_central_charge",
    "bp_shifted_central_charge",
    "principal_w3_central_charge",
    "principal_wn_central_charge",
    "affine_central_charge",
    "virasoro_central_charge",
    "ff_dual_level",
    "bp_dual_level",
    "bp_standard_central_reflection_sum",
    "bp_shifted_central_reflection_sum",
    "principal_wn_central_reflection_sum",
    "koszul_conductor_bp",
    "koszul_conductor_principal_wn",
    "bp_anomaly_ratio",
    "bp_kappa",
    "principal_w3_anomaly_ratio",
    "principal_w3_kappa",
    "virasoro_anomaly_ratio",
    "virasoro_kappa",
    "bp_kappa_complementarity",
    "principal_w3_kappa_complementarity",
    "bp_line_restrictions",
    "bp_generator_data",
    "principal_w3_generator_data",
    "virasoro_generator_data",
    "affine_line_operators",
    "bp_line_operators",
    "principal_w3_line_operators",
    "sl4_hook_31_line_operators",
    "sl4_hook_211_line_operators",
    "ds_line_reduction_diagram",
    "virasoro_shadow_tower",
    "bp_shadow_tower_on_tline",
    "shadow_depth_classification",
    "bp_shadow_depth",
    "bp_ope_channels",
    "bp_rmatrix_channels",
    "bp_rmatrix_max_pole",
    "principal_w3_rmatrix_max_pole",
    "build_catalog",
    "bp_numerical_at_level",
    "quantum_parameter_at_level",
]
