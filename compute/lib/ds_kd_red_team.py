r"""Adversarial audit of DS--bar/Koszul claims beyond the hook corridor.

This module separates finite computation from homological promotion.  It
computes, exactly:

* type-A partition transpose, orbit and centralizer dimensions;
* the good-grading matrix units in ``n_+`` and their actual brackets;
* strong-generator weights and parity;
* Kac--Roan--Wakimoto central charges and formal level reflection;
* finite Hasse-graph reachability;
* type-B/type-C partition validity and dominance collapse;
* the standard Bershadsky--Polyakov OPE as a normalization control;
* the critical Sugawara denominator and elementary admissible-level
  arithmetic.

The same data leave DS--bar comparison, spectral-sequence degeneration,
Ext obstruction classes, categorical transport, object-level Koszul
duality, modular characteristics, and type-B/type-C orbit duality as typed
proof obligations.  In particular, non-abelian ``n_+`` supplies the
quadratic ghost term in the Chevalley--Eilenberg/BRST differential; a
comparison-map calculation is still required before this structure can be
identified with an obstruction to DS--bar commutation.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import Enum
from math import gcd
from typing import Dict, List, Optional, Tuple

from sympy import Matrix, Rational, Symbol, simplify, sympify

from compute.lib.ds_bar_commutation import (
    bershadsky_polyakov_data,
    ds_bar_commutation_check,
    ds_good_grading_data,
)
from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    ghost_constant,
    hook_dual_level_sl_n,
    krw_central_charge,
    reciprocal_weight_diagnostic_from_partition,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)
from compute.lib.theorem_butson_inverse_reduction_engine import (
    formal_central_scalar_sum,
    type_a_centralizer_dimension,
    type_a_orbit_dimension,
    verify_transport_to_transpose,
)


k = Symbol("k")

KRW_SOURCE = "Kac--Roan--Wakimoto (2003), Theorem 2.1(a), equation (2.6)"
BP_SOURCE = (
    "Fehily--Kawasetsu--Ridout (2021), Definition 2.1, equations (2.1)--(2.2)"
)

H_DS_KD_COMPARISON = (
    "H_DS-KD^comparison: a natural filtered chain map between completed "
    "DS(B(V^k(g))) and B(W^k(g,f)), together with a quasi-isomorphism proof"
)
H_KAZHDAN_FORMALITY = (
    "H_Kazhdan^formality: convergence, page identification, degeneration, "
    "and extension control for the relevant BRST/bar filtrations"
)
H_BAR_BRST_BICOMPLEX = (
    "H_bar-BRST^bicomplex: compatible completed bar and BRST differentials, "
    "including every charged and neutral ghost term"
)
H_EXT_OBSTRUCTION = (
    "H_Ext^obstruction: an identified deformation complex, a constructed "
    "comparison class, and a proof that its vanishing is equivalent to the "
    "DS--bar comparison"
)
H_MODULAR_GENUS_ONE = (
    "H_modular^genus-one: direct genus-one characteristics in one "
    "normalization, including charged ghosts, neutral fields, and the "
    "stress-tensor improvement"
)
H_NONPRINCIPAL_LEVEL = (
    "H_level^nonprincipal: an orbit-sensitive level transform derived from "
    "an object-level comparison, with universal/simple presentations fixed"
)
H_CATEGORICAL_TRANSPORT = (
    "H_transport^categorical: realized inverse-reduction functors on the "
    "finite Hasse path, compatible with DS, bar, completion, and Verdier duality"
)
H_TRANSPOSE_DUALITY = (
    "H_transpose^duality: an object-level equivalence between the source and "
    "transpose reductions at the stated level transform"
)
H_BC_SPECIALNESS = (
    "H_BC^specialness: a primary-source implementation of the Lusztig--"
    "Spaltenstein special-orbit criterion, with type and rank conventions fixed"
)
H_BC_DUALITY = (
    "H_BC^duality: the type-changing Spaltenstein/Barbasch--Vogan map, "
    "including the rank-changing box operation, collapse, and special-piece data"
)
H_CRITICAL_PRESENTATION = (
    "H_critical^presentation: a critical-level DS construction with its "
    "conformal replacement, completion, and bar category specified"
)
H_SIMPLE_QUOTIENT = (
    "H_simple^quotient: the maximal ideal of the affine vacuum algebra and "
    "its BRST image, followed through the completed bar construction"
)


def _open(
    statement: str,
    *hypotheses: str,
    evidence: Tuple[str, ...] = (),
) -> ClaimPacket:
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


class AuditSeverity(str, Enum):
    """Severity of a failed inference on the audited claim surface."""

    CRITICAL = "critical"
    SERIOUS = "serious"
    MODERATE = "moderate"
    MINOR = "minor"


@dataclass(frozen=True)
class AuditFinding:
    """One checkable attack packet with its exact repair obligation."""

    claim_attacked: str
    severity: AuditSeverity
    status: ClaimStatus
    exact_evidence: Tuple[str, ...]
    failure_mode: str
    obligations: Tuple[str, ...]
    claim: ClaimPacket


# -------------------------------------------------------------------------
# Exact BRST bracket audit
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class MatrixUnit:
    """A positive-good-grade matrix unit ``E_row,column``."""

    row: int
    column: int
    grade: Rational


@dataclass(frozen=True)
class BracketWitness:
    """A nonzero matrix-unit bracket inside ``n_+``."""

    left: MatrixUnit
    right: MatrixUnit
    result: Tuple[Tuple[int, int, int], ...]
    result_grade: Rational


@dataclass(frozen=True)
class BRSTBracketAudit:
    """Exact good-grading Lie bracket and typed homological consequences."""

    partition: Partition
    N: int
    grading: Dict[Rational, int]
    positive_matrix_units: Tuple[MatrixUnit, ...]
    n_plus_dim: int
    g_half_dim: int
    n_plus_is_abelian: bool
    bracket_span_dimension: int
    bracket_witnesses: Tuple[BracketWitness, ...]
    quadratic_ghost_term_present: bool
    ghost_constant_value: Rational
    ext_obstruction: ClaimPacket
    ds_bar_obstruction: ClaimPacket


def _positive_matrix_units(partition: Partition) -> Tuple[MatrixUnit, ...]:
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    x_diagonal = tuple(Rational(triple.h[index, index], 2) for index in range(N))
    return tuple(
        MatrixUnit(left, right, x_diagonal[left] - x_diagonal[right])
        for left in range(N)
        for right in range(N)
        if left != right and x_diagonal[left] - x_diagonal[right] > 0
    )


def _matrix_unit_bracket(
    left: MatrixUnit,
    right: MatrixUnit,
) -> Tuple[Tuple[int, int, int], ...]:
    coefficients: Dict[Tuple[int, int], int] = {}
    if left.column == right.row:
        entry = (left.row, right.column)
        coefficients[entry] = coefficients.get(entry, 0) + 1
    if right.column == left.row:
        entry = (right.row, left.column)
        coefficients[entry] = coefficients.get(entry, 0) - 1
    return tuple(
        (row, column, coefficient)
        for (row, column), coefficient in sorted(coefficients.items())
        if coefficient
    )


def _bracket_rank(N: int, witnesses: Tuple[BracketWitness, ...]) -> int:
    if not witnesses:
        return 0
    columns = []
    for witness in witnesses:
        vector = [0] * (N * N)
        for row, column, coefficient in witness.result:
            vector[N * row + column] += coefficient
        columns.append(Matrix(vector))
    return int(Matrix.hstack(*columns).rank())


def ghost_obstruction_analysis(N: int, partition: Partition) -> BRSTBracketAudit:
    r"""Compute the actual brackets in ``n_+``.

    The historical entry-point name is retained for callers.  Its result is
    an audit: the finite bracket and quadratic ghost term are computed,
    while the Ext class and DS--bar obstruction remain open packets.
    """

    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    grading = ds_good_grading_data(lam)
    units = _positive_matrix_units(lam)
    witnesses: List[BracketWitness] = []
    for left_index, left in enumerate(units):
        for right in units[left_index + 1 :]:
            result = _matrix_unit_bracket(left, right)
            if result:
                witnesses.append(
                    BracketWitness(
                        left=left,
                        right=right,
                        result=result,
                        result_grade=left.grade + right.grade,
                    )
                )
    witness_tuple = tuple(witnesses)
    rank = _bracket_rank(N, witness_tuple)
    abelian = rank == 0
    exact_evidence = (
        f"dim n_+={len(units)}",
        f"dim [n_+,n_+]={rank}",
        f"positive grades={dict(grading.n_plus_grades)}",
    )
    return BRSTBracketAudit(
        partition=lam,
        N=N,
        grading=dict(grading.n_plus_grades),
        positive_matrix_units=units,
        n_plus_dim=len(units),
        g_half_dim=grading.g_half_dim,
        n_plus_is_abelian=abelian,
        bracket_span_dimension=rank,
        bracket_witnesses=witness_tuple,
        quadratic_ghost_term_present=not abelian,
        ghost_constant_value=ghost_constant(lam),
        ext_obstruction=_open(
            f"Ext obstruction class for DS--bar comparison at partition {lam}",
            H_EXT_OBSTRUCTION,
            H_BAR_BRST_BICOMPLEX,
            evidence=exact_evidence,
        ),
        ds_bar_obstruction=_open(
            f"failure or vanishing of the DS--bar comparison at partition {lam}",
            H_DS_KD_COMPARISON,
            H_KAZHDAN_FORMALITY,
            evidence=exact_evidence,
        ),
    )


# -------------------------------------------------------------------------
# Standard OPE normalization control
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class BershadskyPolyakovControl:
    """Exact standard BP OPE packet used as the control reduction."""

    level: object
    generators: Tuple[Tuple[str, object, str], ...]
    central_charge: object
    formal_reflected_level: object
    formal_central_sum: object
    pole_orders: Tuple[Tuple[str, str, Tuple[int, ...]], ...]
    jj_pole2: object
    jg_plus_charge: object
    jg_minus_charge: object
    gpgm_pole3: object
    gpgm_pole2_coefficient: object
    gpgm_pole1: object
    ll_pole4: object
    source: str


def bershadsky_polyakov_control(level=k) -> BershadskyPolyakovControl:
    """Return the standard FKR BP OPE and its formal reflected scalar sum."""

    level = sympify(level)
    data = bershadsky_polyakov_data(level)
    pole_orders = tuple(
        (left, right, tuple(term.pole_order for term in terms))
        for left, right, terms in data.ope_data.singular_products
    )
    return BershadskyPolyakovControl(
        level=level,
        generators=data.generators,
        central_charge=data.central_charge,
        formal_reflected_level=data.formal_reflected_level,
        formal_central_sum=data.formal_central_sum,
        pole_orders=pole_orders,
        jj_pole2=data.jj_pole2,
        jg_plus_charge=data.jg_charge,
        jg_minus_charge=data.jg_minus_charge,
        gpgm_pole3=data.gg_pole3,
        gpgm_pole2_coefficient=data.gg_pole2_coeff,
        gpgm_pole1=data.gg_pole1,
        ll_pole4=data.tt_pole4,
        source=data.source,
    )


# -------------------------------------------------------------------------
# Non-hook type-A audit packets
# -------------------------------------------------------------------------


NON_HOOK_TARGETS: List[Tuple[int, Partition, str]] = [
    (4, (2, 2), "sl_4 first non-hook rectangular orbit"),
    (5, (3, 2), "sl_5 first non-even non-hook audit surface"),
    (6, (3, 3), "sl_6 two-row rectangular audit surface"),
    (6, (2, 2, 2), "sl_6 three-row rectangular audit surface"),
    (6, (4, 2), "sl_6 two-row non-hook audit surface"),
    (6, (3, 2, 1), "sl_6 self-transpose staircase audit surface"),
]


@dataclass(frozen=True)
class FormalCentralAudit:
    """Exact reflected KRW central scalar, kept separate from modular data."""

    partition: Partition
    transpose: Partition
    level: object
    formal_reflected_level: object
    source_central_charge: object
    transpose_reflected_central_charge: object
    formal_sum: object
    derivative: Optional[object]
    k_independent: Optional[bool]
    source: str
    modular_interpretation: ClaimPacket


def formal_central_audit(
    N: int,
    partition: Partition,
    level=k,
) -> FormalCentralAudit:
    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    level = sympify(level)
    lam_t = transpose_partition(lam)
    reflected = hook_dual_level_sl_n(N, level)
    source_c = krw_central_charge(lam, level)
    transpose_c = krw_central_charge(lam_t, reflected)
    scalar_sum = formal_central_scalar_sum(lam, level)
    derivative = simplify(scalar_sum.diff(level)) if isinstance(level, Symbol) else None
    constant = derivative == 0 if derivative is not None else None
    return FormalCentralAudit(
        partition=lam,
        transpose=lam_t,
        level=level,
        formal_reflected_level=reflected,
        source_central_charge=source_c,
        transpose_reflected_central_charge=transpose_c,
        formal_sum=scalar_sum,
        derivative=derivative,
        k_independent=constant,
        source=KRW_SOURCE,
        modular_interpretation=_open(
            f"modular interpretation of the reflected central scalar for {lam}",
            H_MODULAR_GENUS_ONE,
            H_NONPRINCIPAL_LEVEL,
            evidence=(KRW_SOURCE, f"formal scalar sum={scalar_sum}"),
        ),
    )


@dataclass(frozen=True)
class NonHookProbe:
    """Exact finite evidence and typed DS/KD obligations for one orbit."""

    N: int
    partition: Partition
    transpose: Partition
    is_self_transpose: bool
    orbit_class: str
    centralizer_dim: int
    orbit_dim: int
    generator_weights: Tuple[object, ...]
    n_generators: int
    n_even: int
    n_odd: int
    ghost_constant: Rational
    n_plus_dim: int
    n_half_dim: int
    nilpotent_plus_is_abelian: bool
    bracket_span_dimension: int
    has_quadratic_ghost: bool
    reciprocal_weight_diagnostic: Rational
    formal_central: FormalCentralAudit
    finite_transport_path: Tuple[Partition, ...]
    finite_graph_reaches_transpose: bool
    rho_source: ClaimPacket
    rho_transpose: ClaimPacket
    kappa_w: ClaimPacket
    kappa_dual_w: ClaimPacket
    modular_conductor: ClaimPacket
    ds_bar_commutation: ClaimPacket
    pbw_collapse: ClaimPacket
    koszul_duality: ClaimPacket
    categorical_transport: ClaimPacket
    transpose_duality: ClaimPacket
    ksdual_membership: ClaimPacket
    findings: Tuple[AuditFinding, ...]

    @property
    def complementarity_sum(self):
        """Compatibility alias for the formal central scalar sum."""

        return self.formal_central.formal_sum

    @property
    def complementarity_is_constant(self) -> Optional[bool]:
        """Compatibility alias for scalar ``k``-independence."""

        return self.formal_central.k_independent


def _probe_findings(
    lam: Partition,
    bracket: BRSTBracketAudit,
    central: FormalCentralAudit,
    graph_reaches_transpose: bool,
) -> Tuple[AuditFinding, ...]:
    findings: List[AuditFinding] = []
    comparison = _open(
        f"DS--bar/Koszul comparison for non-hook partition {lam}",
        H_DS_KD_COMPARISON,
        H_KAZHDAN_FORMALITY,
        H_BAR_BRST_BICOMPLEX,
    )
    findings.append(
        AuditFinding(
            claim_attacked="arbitrary-nilpotent DS--bar/Koszul commutation",
            severity=AuditSeverity.SERIOUS,
            status=ClaimStatus.OPEN,
            exact_evidence=(
                f"dim n_+={bracket.n_plus_dim}",
                f"dim [n_+,n_+]={bracket.bracket_span_dimension}",
                f"finite graph reaches transpose={graph_reaches_transpose}",
            ),
            failure_mode=(
                "The finite orbit and BRST ledgers supply the comparison inputs.  "
                "Completion requires the named chain map and its quasi-isomorphism proof."
            ),
            obligations=comparison.hypotheses,
            claim=comparison,
        )
    )
    if bracket.quadratic_ghost_term_present:
        nonlinear = _open(
            f"compatibility of the quadratic BRST ghost term with chiral bar for {lam}",
            H_BAR_BRST_BICOMPLEX,
            H_DS_KD_COMPARISON,
        )
        findings.append(
            AuditFinding(
                claim_attacked="spectral-sequence collapse from BRST combinatorics",
                severity=AuditSeverity.SERIOUS,
                status=ClaimStatus.OPEN,
                exact_evidence=(
                    f"dim [n_+,n_+]={bracket.bracket_span_dimension}",
                    f"nonzero bracket witnesses={len(bracket.bracket_witnesses)}",
                ),
                failure_mode=(
                    "The quadratic ghost term is present.  Its interaction with "
                    "the bar differential requires a chain-level calculation."
                ),
                obligations=nonlinear.hypotheses,
                claim=nonlinear,
            )
        )
    modular = _open(
        f"kappa complementarity for non-hook partition {lam}",
        H_MODULAR_GENUS_ONE,
        H_NONPRINCIPAL_LEVEL,
    )
    findings.append(
        AuditFinding(
            claim_attacked="non-hook modular kappa arithmetic",
            severity=AuditSeverity.SERIOUS,
            status=ClaimStatus.OPEN,
            exact_evidence=(f"formal KRW central scalar={central.formal_sum}",),
            failure_mode=(
                "The rho and kappa surfaces carry open status.  A direct genus-one "
                "calculation supplies the invariant required for modular arithmetic."
            ),
            obligations=modular.hypotheses,
            claim=modular,
        )
    )
    transport = _conditional(
        f"categorical realization of the finite path from {lam} to {transpose_partition(lam)}",
        H_CATEGORICAL_TRANSPORT,
        H_TRANSPOSE_DUALITY,
    )
    findings.append(
        AuditFinding(
            claim_attacked="promotion of Hasse-graph reachability to duality",
            severity=AuditSeverity.MODERATE,
            status=ClaimStatus.CONDITIONAL,
            exact_evidence=(f"finite graph reaches transpose={graph_reaches_transpose}",),
            failure_mode=(
                "Reachability settles the finite partition combinatorics.  Realized "
                "functors and their bar/DS compatibility constitute the categorical step."
            ),
            obligations=transport.hypotheses,
            claim=transport,
        )
    )
    return tuple(findings)


def probe_non_hook(N: int, partition: Partition, level=k) -> NonHookProbe:
    """Return the complete finite audit and typed frontier for one partition."""

    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    lam_t = transpose_partition(lam)
    generators = w_algebra_generator_data(lam)
    bracket = ghost_obstruction_analysis(N, lam)
    central = formal_central_audit(N, lam, level)
    ds_packet = ds_bar_commutation_check(lam, level)
    transport = verify_transport_to_transpose(lam, level)
    transpose_duality = _conditional(
        f"object-level transpose duality from {lam} to {lam_t}",
        H_TRANSPOSE_DUALITY,
        H_DS_KD_COMPARISON,
        H_NONPRINCIPAL_LEVEL,
        evidence=(f"finite Hasse path={transport.hasse_path_to_transpose}",),
    )
    return NonHookProbe(
        N=N,
        partition=lam,
        transpose=lam_t,
        is_self_transpose=lam == lam_t,
        orbit_class=type_a_orbit_class(lam),
        centralizer_dim=type_a_centralizer_dimension(lam),
        orbit_dim=type_a_orbit_dimension(lam),
        generator_weights=tuple(
            sorted((weight for _, weight, _ in generators.strong_generators), key=sympify)
        ),
        n_generators=generators.f_centralizer_dimension,
        n_even=generators.n_even,
        n_odd=generators.n_odd,
        ghost_constant=bracket.ghost_constant_value,
        n_plus_dim=bracket.n_plus_dim,
        n_half_dim=bracket.g_half_dim,
        nilpotent_plus_is_abelian=bracket.n_plus_is_abelian,
        bracket_span_dimension=bracket.bracket_span_dimension,
        has_quadratic_ghost=bracket.quadratic_ghost_term_present,
        reciprocal_weight_diagnostic=reciprocal_weight_diagnostic_from_partition(lam),
        formal_central=central,
        finite_transport_path=transport.hasse_path_to_transpose,
        finite_graph_reaches_transpose=transport.graph_reaches_transpose,
        rho_source=transport.source_rho,
        rho_transpose=transport.transpose_rho,
        kappa_w=transport.source_kappa,
        kappa_dual_w=transport.transpose_kappa,
        modular_conductor=transport.modular_conductor,
        ds_bar_commutation=ds_packet.ds_bar_commutation,
        pbw_collapse=ds_packet.pbw_collapse,
        koszul_duality=transport.koszul_duality,
        categorical_transport=transport.categorical_transport,
        transpose_duality=transpose_duality,
        ksdual_membership=transport.ksdual_membership,
        findings=_probe_findings(
            lam,
            bracket,
            central,
            transport.graph_reaches_transpose,
        ),
    )


def probe_all_non_hooks() -> Dict[str, NonHookProbe]:
    """Audit every catalogued non-hook partition."""

    return {
        f"sl_{N}_{lam}": probe_non_hook(N, lam)
        for N, lam, _description in NON_HOOK_TARGETS
    }


# -------------------------------------------------------------------------
# Spectral-sequence audit
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class SpectralSequenceAudit:
    """Finite filtration input with every spectral conclusion typed."""

    partition: Partition
    N: int
    brst: BRSTBracketAudit
    strong_generator_count: int
    higher_brst_cohomology: ClaimPacket
    kazhdan_degeneration: ClaimPacket
    cross_differential: ClaimPacket
    ds_bar_comparison: ClaimPacket
    obstruction_class: ClaimPacket
    findings: Tuple[AuditFinding, ...]


def spectral_sequence_probe(N: int, partition: Partition) -> SpectralSequenceAudit:
    """Return exact filtration inputs and named spectral-sequence obligations."""

    lam = normalize_partition(partition)
    bracket = ghost_obstruction_analysis(N, lam)
    generators = w_algebra_generator_data(lam)
    exact_evidence = (
        f"dim n_+={bracket.n_plus_dim}",
        f"dim [n_+,n_+]={bracket.bracket_span_dimension}",
        f"strong-generator count={generators.f_centralizer_dimension}",
    )
    higher = _open(
        f"higher BRST cohomology for W^k(sl_{N},f_{lam})",
        H_KAZHDAN_FORMALITY,
        evidence=exact_evidence,
    )
    degeneration = _open(
        f"Kazhdan/bar spectral-sequence degeneration for partition {lam}",
        H_KAZHDAN_FORMALITY,
        H_BAR_BRST_BICOMPLEX,
        evidence=exact_evidence,
    )
    cross = _open(
        f"completed cross-differential for the bar--BRST bicomplex at {lam}",
        H_BAR_BRST_BICOMPLEX,
        evidence=exact_evidence,
    )
    comparison = _open(
        f"DS--bar comparison quasi-isomorphism for partition {lam}",
        H_DS_KD_COMPARISON,
        H_KAZHDAN_FORMALITY,
        H_BAR_BRST_BICOMPLEX,
        evidence=exact_evidence,
    )
    obstruction = _open(
        f"identified Ext obstruction class for partition {lam}",
        H_EXT_OBSTRUCTION,
        H_DS_KD_COMPARISON,
        evidence=exact_evidence,
    )
    finding = AuditFinding(
        claim_attacked="spectral-sequence collapse and obstruction bidegree",
        severity=AuditSeverity.SERIOUS,
        status=ClaimStatus.OPEN,
        exact_evidence=exact_evidence,
        failure_mode=(
            "Good-grading dimensions and Lie brackets determine the input "
            "differential.  The filtered complexes and comparison map determine "
            "page degeneration, higher cohomology, and any Ext bidegree."
        ),
        obligations=(H_KAZHDAN_FORMALITY, H_BAR_BRST_BICOMPLEX, H_EXT_OBSTRUCTION),
        claim=obstruction,
    )
    return SpectralSequenceAudit(
        partition=lam,
        N=N,
        brst=bracket,
        strong_generator_count=generators.f_centralizer_dimension,
        higher_brst_cohomology=higher,
        kazhdan_degeneration=degeneration,
        cross_differential=cross,
        ds_bar_comparison=comparison,
        obstruction_class=obstruction,
        findings=(finding,),
    )


# -------------------------------------------------------------------------
# Type-B/type-C finite partition audit
# -------------------------------------------------------------------------


def is_valid_type_b_partition(partition: Partition) -> bool:
    """Return the type-B parity condition: even parts have even multiplicity."""

    counts = Counter(normalize_partition(partition))
    return all(part % 2 == 1 or multiplicity % 2 == 0 for part, multiplicity in counts.items())


def is_valid_type_c_partition(partition: Partition) -> bool:
    """Return the type-C parity condition: odd parts have even multiplicity."""

    counts = Counter(normalize_partition(partition))
    return all(part % 2 == 0 or multiplicity % 2 == 0 for part, multiplicity in counts.items())


def is_valid_type_d_partition(partition: Partition) -> bool:
    """Return the type-D parity condition, leaving very-even splitting separate."""

    return is_valid_type_b_partition(partition)


def _all_partitions(n: int) -> List[Partition]:
    if n < 0:
        raise ValueError("partition size must be nonnegative")
    if n == 0:
        return [()]
    result: List[Partition] = []

    def visit(remaining: int, largest: int, prefix: Tuple[int, ...]) -> None:
        if remaining == 0:
            result.append(prefix)
            return
        for part in range(min(remaining, largest), 0, -1):
            visit(remaining - part, part, prefix + (part,))

    visit(n, n, ())
    return result


def _dominates(left: Partition, right: Partition) -> bool:
    """Return ``left >= right`` in dominance order for equal-size partitions."""

    if sum(left) != sum(right):
        return False
    width = max(len(left), len(right))
    left_sum = 0
    right_sum = 0
    for index in range(width):
        left_sum += left[index] if index < len(left) else 0
        right_sum += right[index] if index < len(right) else 0
        if left_sum < right_sum:
            return False
    return True


def _dominance_collapse(partition: Partition, validity) -> Partition:
    lam = normalize_partition(partition)
    candidates = [
        candidate
        for candidate in _all_partitions(sum(lam))
        if validity(candidate) and _dominates(lam, candidate)
    ]
    greatest = [
        candidate
        for candidate in candidates
        if all(_dominates(candidate, competitor) for competitor in candidates)
    ]
    if len(greatest) != 1:
        raise ValueError(f"collapse is not uniquely determined for {lam}: {greatest}")
    return greatest[0]


def b_collapse(partition: Partition) -> Partition:
    """Return the greatest B-valid partition dominated by ``partition``."""

    return _dominance_collapse(partition, is_valid_type_b_partition)


def c_collapse(partition: Partition) -> Partition:
    """Return the greatest C-valid partition dominated by ``partition``."""

    return _dominance_collapse(partition, is_valid_type_c_partition)


def enumerate_type_b_orbits(n: int) -> List[Partition]:
    """Enumerate the type-B_n partition labels of ``2n+1``."""

    return [partition for partition in _all_partitions(2 * n + 1) if is_valid_type_b_partition(partition)]


def enumerate_type_c_orbits(n: int) -> List[Partition]:
    """Enumerate the type-C_n partition labels of ``2n``."""

    return [partition for partition in _all_partitions(2 * n) if is_valid_type_c_partition(partition)]


def is_special_type_b_orbit(partition: Partition) -> ClaimPacket:
    """Return the specialness obligation with type-B conventions exposed."""

    lam = normalize_partition(partition)
    if not is_valid_type_b_partition(lam):
        raise ValueError(f"{lam} does not satisfy the type-B parity condition")
    return _open(
        f"type-B specialness of orbit partition {lam}",
        H_BC_SPECIALNESS,
    )


@dataclass(frozen=True)
class TypeBCDOrbit:
    """Exact orbit-label validity with typed specialness and duality."""

    lie_type: str
    rank: int
    partition: Partition
    is_valid_partition: bool
    specialness: ClaimPacket
    spaltenstein_image: ClaimPacket
    bv_dual: ClaimPacket
    finding: AuditFinding


def _type_bc_orbit_audit(lie_type: str, rank: int, partition: Partition) -> TypeBCDOrbit:
    lam = normalize_partition(partition)
    validity = is_valid_type_b_partition(lam) if lie_type == "B" else is_valid_type_c_partition(lam)
    specialness = _open(
        f"type-{lie_type} specialness of orbit partition {lam}",
        H_BC_SPECIALNESS,
    )
    image = _open(
        f"Spaltenstein image of type-{lie_type} partition {lam}",
        H_BC_SPECIALNESS,
        H_BC_DUALITY,
    )
    dual = _open(
        f"Barbasch--Vogan dual of type-{lie_type} partition {lam}",
        H_BC_DUALITY,
    )
    finding = AuditFinding(
        claim_attacked=f"type-{lie_type} specialness and BV-dual assignment",
        severity=AuditSeverity.SERIOUS,
        status=ClaimStatus.OPEN,
        exact_evidence=(f"partition parity validity={validity}",),
        failure_mode=(
            "Parity validity and same-size dominance collapse settle the finite "
            "partition ledger.  The type-changing duality requires its box "
            "operation and a source-backed special-piece construction."
        ),
        obligations=(H_BC_SPECIALNESS, H_BC_DUALITY),
        claim=dual,
    )
    return TypeBCDOrbit(
        lie_type=lie_type,
        rank=rank,
        partition=lam,
        is_valid_partition=validity,
        specialness=specialness,
        spaltenstein_image=image,
        bv_dual=dual,
        finding=finding,
    )


def analyze_type_b2_orbits() -> Dict[str, TypeBCDOrbit]:
    """Audit every B2 and C2 orbit label without promoting duality claims."""

    result: Dict[str, TypeBCDOrbit] = {}
    for lam in enumerate_type_b_orbits(2):
        result[f"B2_{lam}"] = _type_bc_orbit_audit("B", 2, lam)
    for lam in enumerate_type_c_orbits(2):
        result[f"C2_{lam}"] = _type_bc_orbit_audit("C", 2, lam)
    return result


# -------------------------------------------------------------------------
# Level audit
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class LevelAudit:
    """Exact level arithmetic with presentation-sensitive obligations."""

    partition: Partition
    N: int
    level_type: str
    level_value: object
    formal_reflected_level: object
    formal_reflection_fixed: bool
    affine_sugawara_denominator: object
    affine_sugawara_denominator_vanishes: bool
    basic_admissibility_arithmetic: Optional[bool]
    universal_ds_reduction: ClaimPacket
    conformal_presentation: ClaimPacket
    simple_quotient_null_ideal: ClaimPacket
    pbw_koszulness: ClaimPacket
    ds_bar_comparison: ClaimPacket
    modular_kappa: ClaimPacket
    findings: Tuple[AuditFinding, ...]


def _level_audit(
    N: int,
    partition: Partition,
    level_value,
    level_type: str,
    basic_admissibility_arithmetic: Optional[bool],
) -> LevelAudit:
    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    level_value = sympify(level_value)
    reflected = simplify(-level_value - 2 * N)
    denominator = simplify(level_value + N)
    critical = denominator == 0
    universal = _conditional(
        f"universal DS reduction at level {level_value} for partition {lam}",
        H_CRITICAL_PRESENTATION if critical else H_DS_KD_COMPARISON,
    )
    conformal = _open(
        f"conformal presentation at level {level_value} for partition {lam}",
        H_CRITICAL_PRESENTATION if critical else H_NONPRINCIPAL_LEVEL,
    )
    simple = _open(
        f"BRST image of the simple-quotient null ideal at level {level_value}",
        H_SIMPLE_QUOTIENT,
    )
    pbw = _open(
        f"PBW/bar collapse and Koszulness at level {level_value} for {lam}",
        H_SIMPLE_QUOTIENT,
        H_KAZHDAN_FORMALITY,
    )
    comparison = _open(
        f"DS--bar comparison at level {level_value} for {lam}",
        H_DS_KD_COMPARISON,
        H_CRITICAL_PRESENTATION if critical else H_SIMPLE_QUOTIENT,
    )
    modular = _open(
        f"modular kappa at level {level_value} for {lam}",
        H_MODULAR_GENUS_ONE,
        H_CRITICAL_PRESENTATION if critical else H_SIMPLE_QUOTIENT,
    )
    finding = AuditFinding(
        claim_attacked=f"{level_type} DS/KD verdict",
        severity=AuditSeverity.SERIOUS,
        status=ClaimStatus.OPEN,
        exact_evidence=(
            f"k+N={denominator}",
            f"formal reflection fixed={reflected == level_value}",
            f"basic admissibility arithmetic={basic_admissibility_arithmetic}",
        ),
        failure_mode=(
            "Level arithmetic identifies the Sugawara pole and the formal "
            "reflection.  DS, bar, PBW, simple-quotient, and modular behavior "
            "depend on the selected presentation and comparison package."
        ),
        obligations=tuple(dict.fromkeys(comparison.hypotheses + pbw.hypotheses)),
        claim=comparison,
    )
    return LevelAudit(
        partition=lam,
        N=N,
        level_type=level_type,
        level_value=level_value,
        formal_reflected_level=reflected,
        formal_reflection_fixed=reflected == level_value,
        affine_sugawara_denominator=denominator,
        affine_sugawara_denominator_vanishes=critical,
        basic_admissibility_arithmetic=basic_admissibility_arithmetic,
        universal_ds_reduction=universal,
        conformal_presentation=conformal,
        simple_quotient_null_ideal=simple,
        pbw_koszulness=pbw,
        ds_bar_comparison=comparison,
        modular_kappa=modular,
        findings=(finding,),
    )


def analyze_critical_level(N: int, partition: Partition) -> LevelAudit:
    """Audit the critical value ``k=-N`` for ``sl_N``."""

    return _level_audit(N, partition, -N, "critical", None)


def analyze_admissible_level(
    N: int,
    partition: Partition,
    p: int,
    q: int,
) -> LevelAudit:
    """Audit ``k=-N+p/q`` and record elementary admissibility arithmetic."""

    if q <= 0:
        raise ValueError("q must be positive")
    value = Rational(-N * q + p, q)
    arithmetic = p >= N and gcd(p, q) == 1
    return _level_audit(
        N,
        partition,
        value,
        f"admissible-input (p={p}, q={q})",
        arithmetic,
    )


def analyze_colliding_level(N: int, partition: Partition) -> LevelAudit:
    """Audit the fixed point of ``k -> -k-2N``, namely ``k=-N``."""

    return _level_audit(N, partition, -N, "formal-fixed/critical", None)


# -------------------------------------------------------------------------
# Compatibility arithmetic entry points
# -------------------------------------------------------------------------


def complementarity_sum_non_hook(N: int, partition: Partition):
    """Return the exact formal reflected KRW central scalar sum."""

    return formal_central_audit(N, partition).formal_sum


def complementarity_sum_is_constant(
    N: int,
    partition: Partition,
) -> Tuple[bool, object]:
    """Return exact ``k``-independence and the scalar expression/value."""

    audit = formal_central_audit(N, partition)
    if audit.k_independent:
        return True, simplify(audit.formal_sum.subs(k, 0))
    return False, audit.formal_sum


def kappa_sum_non_hook(N: int, partition: Partition) -> ClaimPacket:
    """Return the unresolved modular-kappa complementarity claim."""

    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    return _open(
        f"kappa(W^k(sl_{N},f_{lam})) + kappa(W^{{-k-2N}}(sl_{N},f_{transpose_partition(lam)}))",
        H_MODULAR_GENUS_ONE,
        H_NONPRINCIPAL_LEVEL,
    )


def kappa_sum_is_constant(N: int, partition: Partition) -> ClaimPacket:
    """Return the unresolved constancy claim without arithmetic on open packets."""

    lam = normalize_partition(partition)
    if partition_size(lam) != N:
        raise ValueError(f"partition {lam} has size {partition_size(lam)}, expected {N}")
    return _open(
        f"k-independence of the non-hook kappa sum for partition {lam}",
        H_MODULAR_GENUS_ONE,
        H_NONPRINCIPAL_LEVEL,
    )


# -------------------------------------------------------------------------
# Complete adversarial report
# -------------------------------------------------------------------------


@dataclass(frozen=True)
class DSKDAuditReport:
    """A checkable report whose conclusions retain their epistemic types."""

    target: str
    partition: Partition
    N: int
    probe: NonHookProbe
    spectral_sequence: SpectralSequenceAudit
    critical_level: LevelAudit
    findings: Tuple[AuditFinding, ...]


def full_red_team_report() -> List[DSKDAuditReport]:
    """Run the complete finite battery and collect typed residual obligations."""

    reports: List[DSKDAuditReport] = []
    for N, lam, description in NON_HOOK_TARGETS:
        probe = probe_non_hook(N, lam)
        spectral = spectral_sequence_probe(N, lam)
        critical = analyze_critical_level(N, lam)
        reports.append(
            DSKDAuditReport(
                target=description,
                partition=lam,
                N=N,
                probe=probe,
                spectral_sequence=spectral,
                critical_level=critical,
                findings=probe.findings + spectral.findings + critical.findings,
            )
        )
    return reports


__all__ = [
    "AuditFinding",
    "AuditSeverity",
    "BP_SOURCE",
    "BRSTBracketAudit",
    "BershadskyPolyakovControl",
    "BracketWitness",
    "DSKDAuditReport",
    "FormalCentralAudit",
    "H_BAR_BRST_BICOMPLEX",
    "H_BC_DUALITY",
    "H_BC_SPECIALNESS",
    "H_CATEGORICAL_TRANSPORT",
    "H_CRITICAL_PRESENTATION",
    "H_DS_KD_COMPARISON",
    "H_EXT_OBSTRUCTION",
    "H_KAZHDAN_FORMALITY",
    "H_MODULAR_GENUS_ONE",
    "H_NONPRINCIPAL_LEVEL",
    "H_SIMPLE_QUOTIENT",
    "H_TRANSPOSE_DUALITY",
    "KRW_SOURCE",
    "LevelAudit",
    "MatrixUnit",
    "NON_HOOK_TARGETS",
    "NonHookProbe",
    "SpectralSequenceAudit",
    "TypeBCDOrbit",
    "analyze_admissible_level",
    "analyze_colliding_level",
    "analyze_critical_level",
    "analyze_type_b2_orbits",
    "b_collapse",
    "bershadsky_polyakov_control",
    "c_collapse",
    "complementarity_sum_is_constant",
    "complementarity_sum_non_hook",
    "enumerate_type_b_orbits",
    "enumerate_type_c_orbits",
    "formal_central_audit",
    "full_red_team_report",
    "ghost_obstruction_analysis",
    "is_special_type_b_orbit",
    "is_valid_type_b_partition",
    "is_valid_type_c_partition",
    "is_valid_type_d_partition",
    "kappa_sum_is_constant",
    "kappa_sum_non_hook",
    "probe_all_non_hooks",
    "probe_non_hook",
    "spectral_sequence_probe",
]
