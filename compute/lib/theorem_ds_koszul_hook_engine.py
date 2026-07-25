r"""Exact hook-corridor arithmetic with typed DS--Koszul obligations.

For a hook partition ``lambda=(N-r,1^r)``, this module computes its transpose,
good-grading dimensions, generator ledger, formal level reflection
``k'=-k-2N``, and Kac--Roan--Wakimoto central charges.  These are the scalar
and combinatorial lanes.

The PBW collapse, completed chiral Koszulness, genus-one anomaly ratio,
modular characteristic, modular conductor, reduction-by-stages comparison,
transport to ``lambda^t``, full shadow class, and DS--Koszul diagram are typed
``ClaimPacket`` surfaces.  Each packet names the source-domain, filtration,
completion, Verdier, or trace hypothesis required for promotion.

The standard Bershadsky--Polyakov/FKR central charge satisfies
``c(k)+c(-k-6)=50``.  The shifted secondary central-charge lane satisfies the
corresponding identity with value ``196``.  The reciprocal-weight diagnostic
``17/6`` belongs to neither anomaly-ratio realization nor modular conductor.

Dominance-graph distance is exact combinatorics.  Since transposition sends
the principal partition ``(N)`` to ``(1^N)``, a principal same-orbit
Feigin--Frenkel statement supplies no automatic seed for transport from
``lambda`` to ``lambda^t``.  Reduction by stages and its compatibility with
completed chiral bar duality remain explicit construction obligations.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Rational,
    Symbol,
    cancel,
    expand,
    factor,
    simplify,
    sympify,
)

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    H_HOOK_DS_BAR,
    WAlgebraCentralCharge,
    WAlgebraGeneratorData,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    ghost_constant,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    krw_central_charge_data,
    levi_rho_norm_squared,
    rho_shift_norm_squared,
    w_algebra_generator_data,
    weyl_vector_norm_squared_sl_n,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    hook_partition,
    is_hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_partition_sl2_triple,
)
from compute.lib.hook_transport_corridor import ReductionGraph


k_sym = Symbol('k')


def _open(statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()) -> ClaimPacket:
    """Return an open claim with explicit construction obligations."""

    return ClaimPacket(
        statement,
        ClaimStatus.OPEN,
        None,
        evidence=evidence,
        hypotheses=tuple(dict.fromkeys(hypotheses)),
    )


def _conditional(
    statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()
) -> ClaimPacket:
    """Return a conditional comparison with no scalar payload."""

    return ClaimPacket(
        statement,
        ClaimStatus.CONDITIONAL,
        None,
        evidence=evidence,
        hypotheses=tuple(dict.fromkeys(hypotheses)),
    )


# ============================================================================
# 1.  Core data structures
# ============================================================================

@dataclass(frozen=True)
class DSKDCommutationResult:
    """Exact corridor data and typed DS--Koszul claims."""

    lie_algebra: str
    N: int
    partition: Partition
    transpose: Partition
    is_hook: bool
    # Method 1: PBW filtration
    pbw_source_koszul: ClaimPacket
    pbw_dual_koszul: ClaimPacket
    pbw_n_plus_dim: int
    pbw_e2_collapse: ClaimPacket
    # Method 2: Fehily-CLNS
    affine_kappa_sum_zero: bool
    affine_kd: ClaimPacket
    c_sum_k_independent: bool      # c(W_k(f_lam)) + c(W_{k'}(f_{lam^t})) = const
    c_sum_value: object            # the constant value
    clns_diagram_commutes: ClaimPacket
    # Method 3: Transport
    principal_ds_kd: ClaimPacket
    hook_spine_count: int
    transport_path_available: bool
    transport_propagation: ClaimPacket
    # Method 4: Shadow tower
    source_shadow_class: ClaimPacket
    dual_shadow_class: ClaimPacket
    shadow_structurally_compatible: ClaimPacket
    self_transpose_kappa_sum: ClaimPacket
    # Overall
    overall_verdict: ClaimPacket
    ds_kd_commutes: ClaimPacket


@dataclass(frozen=True)
class PBWFiltrationData:
    """PBW filtration / spectral sequence data for the BRST complex."""

    partition: Partition
    N: int
    n_plus_dim: int
    n_plus_is_abelian: bool
    n_plus_grade_structure: Dict[Rational, int]
    ghost_pairs: int
    g_half_dim: int
    e2_collapse: ClaimPacket
    w_is_koszul: ClaimPacket


@dataclass(frozen=True)
class FehilyCLNSDualityData:
    """Fehily-CLNS commutative diagram verification."""

    partition: Partition
    transpose: Partition
    N: int
    # Affine KD (left side of diagram)
    affine_kappa_source: object
    affine_kappa_dual: object
    affine_kappa_sum: object
    affine_kappa_sum_zero: bool
    affine_kd: ClaimPacket
    # W-algebra c-complementarity (right side of diagram)
    source_c: object
    dual_c: object
    c_sum: object
    c_sum_k_independent: bool
    c_sum_value: object
    # Anomaly ratios
    source_rho: ClaimPacket
    dual_rho: ClaimPacket
    rho_match: ClaimPacket
    fehily_embedding: ClaimPacket
    clns_edge_comparison: ClaimPacket
    genra_juillard_reduction_by_stages: ClaimPacket
    # Diagram conclusion
    diagram_commutes: ClaimPacket


@dataclass(frozen=True)
class TransportPropagationData:
    """Transport propagation from principal nilpotent."""

    partition: Partition
    N: int
    principal_partition: Partition
    principal_ds_kd: ClaimPacket
    hook_spine_count: int
    path_available: bool
    reduction_by_stages: ClaimPacket
    propagation: ClaimPacket


@dataclass(frozen=True)
class ShadowTowerComparisonData:
    """Shadow tower structural comparison."""

    partition: Partition
    transpose: Partition
    N: int
    source_kappa: ClaimPacket
    dual_kappa: ClaimPacket
    source_rho: ClaimPacket
    dual_rho: ClaimPacket
    source_shadow_class: ClaimPacket
    dual_shadow_class: ClaimPacket
    # The represented conductor and its level dependence remain typed.
    is_self_transpose: bool
    kappa_sum: ClaimPacket
    kappa_sum_k_independent: ClaimPacket
    structurally_compatible: ClaimPacket


# ============================================================================
# 2.  Method 1: PBW filtration and BRST spectral sequence
# ============================================================================

def _n_plus_dimension(partition: Partition) -> int:
    """Dimension of n_+ for the nilpotent grading of g = sl_N."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = Rational(h_diag[i] - h_diag[j], 2)
            if eigenval > 0:
                count += 1
    return count


def _n_plus_grade_structure(partition: Partition) -> Dict[Rational, int]:
    """Grade structure of n_+ under ad(x) = (1/2)*ad(h)."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    grades: Dict[Rational, int] = {}
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = Rational(h_diag[i] - h_diag[j], 2)
            if eigenval > 0:
                grades[eigenval] = grades.get(eigenval, 0) + 1
    return grades


def _n_plus_is_abelian(partition: Partition) -> bool:
    """Check whether n_+ is abelian for the given nilpotent grading.

    n_+ is abelian iff [n_+, n_+] = 0.  In type A, [E_{ij}, E_{jl}] = E_{il},
    so n_+ is non-abelian iff there exist (i,j) and (j,l) in n_+ with i != l
    and (i,l) also in n_+.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]

    pos_roots = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = Rational(h_diag[i] - h_diag[j], 2)
            if eigenval > 0:
                pos_roots.append((i, j))

    for (i, j) in pos_roots:
        for (j2, l) in pos_roots:
            if j == j2 and i != l:
                eigenval_il = Rational(h_diag[i] - h_diag[l], 2)
                if eigenval_il > 0:
                    return False
    return True


def _g_half_dimension(partition: Partition) -> int:
    """Dimension of g_{1/2} for the nilpotent grading."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = Rational(h_diag[i] - h_diag[j], 2)
            if eigenval == Rational(1, 2):
                count += 1
    return count


def pbw_filtration_analysis(partition: Partition) -> PBWFiltrationData:
    """Method 1: PBW filtration analysis via BRST spectral sequence.

    The BRST spectral sequence for DS reduction at nilpotent f_lambda:
    - V_k(sl_N) is Koszul by prop:pbw-universality.
    - For hook-type: the good grading (Elashvili-Kac) gives a Kazhdan
      filtration.  The associated graded of d_BRST is the CE differential.
      For hook type, g_0 is a Levi subalgebra (reductive), so the Kazhdan
      spectral sequence collapses at E_2.
    - Conclusion: W_k(sl_N, f_lam) is Koszul for all hook partitions.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)

    n_dim = _n_plus_dimension(lam)
    n_abelian = _n_plus_is_abelian(lam)
    n_grades = _n_plus_grade_structure(lam)
    g_half = _g_half_dimension(lam)

    e2_collapse = _conditional(
        f"E2 collapse of the hook BRST spectral sequence for {lam}",
        "a source-backed good-grading and associated-graded BRST theorem",
        "boundedness and convergence of the completed Kazhdan filtration",
        evidence=(
            f"exact n_plus dimension {n_dim}",
            f"exact g_half dimension {g_half}",
        ),
    )
    w_koszul = _conditional(
        f"completed chiral Koszulness of W(sl_{N}, f_{lam})",
        *e2_collapse.hypotheses,
        "the PBW--Slodowy collapse theorem in the completed chiral category",
    )

    return PBWFiltrationData(
        partition=lam,
        N=N,
        n_plus_dim=n_dim,
        n_plus_is_abelian=n_abelian,
        n_plus_grade_structure=n_grades,
        ghost_pairs=n_dim,
        g_half_dim=g_half,
        e2_collapse=e2_collapse,
        w_is_koszul=w_koszul,
    )


# ============================================================================
# 3.  Method 2: Fehily-CLNS commutative diagram
# ============================================================================

def fehily_clns_duality(
    partition: Partition, level=Symbol('k')
) -> FehilyCLNSDualityData:
    """Method 2: Verify the Fehily-CLNS commutative diagram.

    The diagram:
        V_k(sl_N) --DS(f_lam)--> W_k(f_lam)
             |                         |
            KD                        KD
             |                         |
        V_{k'}(sl_N) --DS(f_{lam^t})--> W_{k'}(f_{lam^t})

    Left vertical: V_k^! = V_{k'} where k' = -k - 2N.
    Verified by: kappa(V_k) + kappa(V_{k'}) = 0.

    Right vertical (the CLAIM): W_k(f_lam)^! = W_{k'}(f_{lam^t}).
    Necessary condition: c(W_k(f_lam)) + c(W_{k'}(f_{lam^t})) is k-independent.
    (The c-sum is the 'Koszul constant' for the pair.)

    NOTE: for non-self-transpose pairs, the kappa sum is k-DEPENDENT
    because the anomaly ratios differ.  This is expected and correct.
    The c-sum being k-independent is the correct test.
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    kvar = sympify(level)
    kv = hook_dual_level_sl_n(N, kvar)

    # Affine KD: kappa(V_k(sl_N)) + kappa(V_{k'}(sl_N)) = 0
    # kappa(V_k) = dim(g)*(k+N)/(2N)
    dim_g = N * N - 1
    affine_kappa_s = Rational(dim_g, 2 * N) * (kvar + N)
    affine_kappa_d = Rational(dim_g, 2 * N) * (kv + N)
    affine_kappa_sum = simplify(affine_kappa_s + affine_kappa_d)
    affine_ok = simplify(affine_kappa_sum) == 0
    affine_kd = _conditional(
        f"affine chiral Koszul duality at reflected levels for sl_{N}",
        "the affine chiral-Koszul theorem in the selected level and completion convention",
        "continuous Verdier duality for the affine presentation",
        evidence=(f"exact affine kappa sum {affine_kappa_sum}",),
    )

    # W-algebra c-complementarity
    source_c = krw_central_charge(lam, kvar)
    dual_c = krw_central_charge(lam_t, kv)
    c_sum = simplify(source_c + dual_c)
    dc_dk = simplify(c_sum.diff(kvar))
    c_sum_const = dc_dk == 0

    # Evaluate c_sum constant value (substitute k=0 or similar)
    if c_sum_const:
        c_sum_val = simplify(c_sum)
    else:
        c_sum_val = c_sum

    # Anomaly ratios
    rho_s = anomaly_ratio_from_partition(lam)
    rho_d = anomaly_ratio_from_partition(lam_t)
    rho_match = _open(
        f"equality of the represented anomaly ratios for {lam} and {lam_t}",
        *rho_s.hypotheses,
        *rho_d.hypotheses,
        "a common genus-one trace channel for both reductions",
        evidence=(f"partition self-transpose flag {lam == lam_t}",),
    )

    fehily = _conditional(
        f"Fehily inverse-reduction input for the hook orbit {lam}",
        "a precise Fehily embedding or inverse-reduction theorem whose source domain contains this orbit and level",
        "conversion from the source normalization to the present KRW convention",
    )
    clns = _conditional(
        f"CLNS hook-edge comparison input for {lam}->{lam_t}",
        "a precise CLNS theorem whose source domain contains this edge and level",
        "conversion from the source category and level convention to the present one",
    )
    genra_juillard = _conditional(
        f"Genra--Juillard reduction-by-stages input for {lam}->{lam_t}",
        "a precise reduction-by-stages theorem whose source domain contains the selected hook corridor",
        "compatibility of the source functors with the present completions",
    )
    diagram_ok = _conditional(
        f"completed hook-corridor DS--Koszul square for {lam}->{lam_t}",
        *affine_kd.hypotheses,
        *fehily.hypotheses,
        *clns.hypotheses,
        *genra_juillard.hypotheses,
        H_HOOK_DS_BAR,
        "compatibility of every source-domain map with completed chiral Koszul duality",
        evidence=(
            f"exact affine reflected sum {affine_kappa_sum}",
            f"exact standard-KRW central sum {c_sum}",
        ),
    )

    return FehilyCLNSDualityData(
        partition=lam,
        transpose=lam_t,
        N=N,
        affine_kappa_source=affine_kappa_s,
        affine_kappa_dual=affine_kappa_d,
        affine_kappa_sum=affine_kappa_sum,
        affine_kappa_sum_zero=affine_ok,
        affine_kd=affine_kd,
        source_c=source_c,
        dual_c=dual_c,
        c_sum=c_sum,
        c_sum_k_independent=c_sum_const,
        c_sum_value=c_sum_val,
        source_rho=rho_s,
        dual_rho=rho_d,
        rho_match=rho_match,
        fehily_embedding=fehily,
        clns_edge_comparison=clns,
        genra_juillard_reduction_by_stages=genra_juillard,
        diagram_commutes=diagram_ok,
    )


# ============================================================================
# 4.  Method 3: Transport propagation from principal nilpotent
# ============================================================================

def _hook_spine_count(partition: Partition) -> int:
    """Return ``len(lambda)-1`` along the formal hook spine."""
    lam = normalize_partition(partition)
    if not is_hook_partition(lam):
        raise ValueError(f"hook-spine count requires a hook partition, got {lam}")
    return len(lam) - 1


def transport_propagation_analysis(
    partition: Partition, level=Symbol('k')
) -> TransportPropagationData:
    """Return exact graph distance and typed reduction-by-stages claims."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    principal = (N,)

    spine_count = _hook_spine_count(lam)
    path_available = ReductionGraph.build(N).path_exists(lam, principal)
    principal_claim = _conditional(
        f"principal same-orbit Feigin--Frenkel comparison in sl_{N}",
        "the principal Feigin--Frenkel duality theorem in the present completed chiral category",
        "the Verdier and genus-one hypotheses of the principal reconstruction package",
        evidence=(
            f"partition transpose sends {principal} to {transpose_partition(principal)}",
        ),
    )
    reduction = _conditional(
        f"reduction by stages from {principal} to the hook orbit {lam}",
        "a precise inverse-reduction theorem whose source domain contains this hook corridor",
        "compatibility of inverse reduction with the selected level reflection",
        evidence=(
            f"exact hook-spine count {spine_count}",
            f"dominance-graph path availability {path_available}",
        ),
    )
    propagation = _open(
        f"transport of DS--Koszul duality from {principal} to {lam}",
        *principal_claim.hypotheses,
        *reduction.hypotheses,
        "a bridge from the principal same-orbit comparison to the transpose-orbit target",
        "functorial compatibility with completed chiral bar and Verdier duality",
    )

    return TransportPropagationData(
        partition=lam,
        N=N,
        principal_partition=principal,
        principal_ds_kd=principal_claim,
        hook_spine_count=spine_count,
        path_available=path_available,
        reduction_by_stages=reduction,
        propagation=propagation,
    )


# ============================================================================
# 5.  Method 4: Shadow tower comparison
# ============================================================================

def _shadow_depth_class(partition: Partition) -> ClaimPacket:
    """Return the open full-shadow-class claim with weight evidence."""
    lam = normalize_partition(partition)
    gen_data = w_algebra_generator_data(lam)
    weights = [w for (_, w, _) in gen_data.strong_generators]
    max_weight = max(weights) if weights else 0

    if gen_data.f_centralizer_dimension == 1:
        w = weights[0]
        if w == Rational(1):
            candidate = "G"
        else:
            candidate = "M"
    elif gen_data.n_fermionic > 0:
        candidate = "M"
    elif all(w == Rational(1) for w in weights):
        candidate = "L"
    elif max_weight >= Rational(3):
        candidate = "M"
    else:
        candidate = "M"
    return _open(
        f"full shadow class of W(sl_{partition_size(lam)}, f_{lam})",
        "the complete Maurer--Cartan tower with collision normalization",
        "a termination or nontermination theorem beyond generator weights",
        evidence=(f"generator-weight candidate {candidate}",),
    )


def shadow_tower_comparison(
    partition: Partition, level=Symbol('k')
) -> ShadowTowerComparisonData:
    """Return typed modular and full-shadow comparison obligations."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    kvar = sympify(level)
    kv = hook_dual_level_sl_n(N, kvar)
    is_self_t = (lam == lam_t)

    source_kappa = ds_kappa_from_affine(lam, kvar)
    dual_kappa = ds_kappa_from_affine(lam_t, kv)
    source_rho = anomaly_ratio_from_partition(lam)
    dual_rho = anomaly_ratio_from_partition(lam_t)

    kappa_sum = kappa_complementarity_sum(lam, kvar)
    kappa_k_indep = _open(
        f"level-independence of the represented modular conductor for {lam},{lam_t}",
        *kappa_sum.hypotheses,
        "a proof that the represented genus-one trace sum is constant in the level parameter",
    )

    source_class = _shadow_depth_class(lam)
    dual_class = _shadow_depth_class(lam_t)

    compatible = _open(
        f"shadow-tower compatibility for the hook pair {lam},{lam_t}",
        *source_class.hypotheses,
        *dual_class.hypotheses,
        *kappa_sum.hypotheses,
        "an arity-by-arity comparison of the two completed Maurer--Cartan towers",
    )

    return ShadowTowerComparisonData(
        partition=lam,
        transpose=lam_t,
        N=N,
        source_kappa=source_kappa,
        dual_kappa=dual_kappa,
        source_rho=source_rho,
        dual_rho=dual_rho,
        source_shadow_class=source_class,
        dual_shadow_class=dual_class,
        is_self_transpose=is_self_t,
        kappa_sum=kappa_sum,
        kappa_sum_k_independent=kappa_k_indep,
        structurally_compatible=compatible,
    )


# ============================================================================
# 6.  Master verification: all four methods
# ============================================================================

def verify_ds_kd_hook(
    partition: Partition, level=Symbol('k')
) -> DSKDCommutationResult:
    """Assemble the exact corridor ledger and conditional theorem packet."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    kvar = sympify(level)
    kv = hook_dual_level_sl_n(N, kvar)
    is_hook = is_hook_partition(lam)
    if not is_hook:
        raise ValueError(f"hook DS--Koszul ledger requires a hook partition, got {lam}")

    # Method 1: PBW for both sides
    pbw_source = pbw_filtration_analysis(lam)
    pbw_dual = pbw_filtration_analysis(lam_t)

    # Method 2: CLNS diagram
    clns = fehily_clns_duality(lam, kvar)

    # Method 3: Transport
    transport = transport_propagation_analysis(lam, kvar)

    # Method 4: Shadow
    shadow = shadow_tower_comparison(lam, kvar)

    overall = _open(
        f"agreement of the four hook-corridor comparison methods for {lam}",
        *pbw_source.w_is_koszul.hypotheses,
        *pbw_dual.w_is_koszul.hypotheses,
        *clns.diagram_commutes.hypotheses,
        *transport.propagation.hypotheses,
        *shadow.structurally_compatible.hypotheses,
    )
    ds_kd = _conditional(
        f"DS reduction commutes with completed chiral Koszul duality for {lam}",
        *overall.hypotheses,
        H_HOOK_DS_BAR,
    )

    return DSKDCommutationResult(
        lie_algebra=f"sl_{N}",
        N=N,
        partition=lam,
        transpose=lam_t,
        is_hook=is_hook,
        # Method 1
        pbw_source_koszul=pbw_source.w_is_koszul,
        pbw_dual_koszul=pbw_dual.w_is_koszul,
        pbw_n_plus_dim=pbw_source.n_plus_dim,
        pbw_e2_collapse=pbw_source.e2_collapse,
        # Method 2
        affine_kappa_sum_zero=clns.affine_kappa_sum_zero,
        affine_kd=clns.affine_kd,
        c_sum_k_independent=clns.c_sum_k_independent,
        c_sum_value=clns.c_sum_value,
        clns_diagram_commutes=clns.diagram_commutes,
        # Method 3
        principal_ds_kd=transport.principal_ds_kd,
        hook_spine_count=transport.hook_spine_count,
        transport_path_available=transport.path_available,
        transport_propagation=transport.propagation,
        # Method 4
        source_shadow_class=shadow.source_shadow_class,
        dual_shadow_class=shadow.dual_shadow_class,
        shadow_structurally_compatible=shadow.structurally_compatible,
        self_transpose_kappa_sum=shadow.kappa_sum,
        # Overall
        overall_verdict=overall,
        ds_kd_commutes=ds_kd,
    )


# ============================================================================
# 7.  Catalog: run all hook partitions for sl_N, N = 3..max_N
# ============================================================================

def hook_ds_kd_catalog(max_N: int = 6) -> List[Dict[str, Any]]:
    """Run DS-KD commutation verification for all hook partitions up to sl_N."""
    results = []
    for N in range(3, max_N + 1):
        for r in range(1, N):
            lam = hook_partition(N, r)
            if lam == (N,):
                continue
            result = verify_ds_kd_hook(lam)
            results.append({
                "N": N,
                "partition": lam,
                "transpose": result.transpose,
                "is_hook": result.is_hook,
                "pbw_source_koszul": result.pbw_source_koszul,
                "pbw_dual_koszul": result.pbw_dual_koszul,
                "clns_holds": result.clns_diagram_commutes,
                "transport_status": result.transport_propagation.status,
                "shadow_compatible": result.shadow_structurally_compatible,
                "overall_status": result.overall_verdict.status,
                "ds_kd_status": result.ds_kd_commutes.status,
                "ds_kd_hypotheses": result.ds_kd_commutes.hypotheses,
            })
    return results


# ============================================================================
# 8.  Numerical cross-checks at specific levels
# ============================================================================

def numerical_c_complementarity(
    partition: Partition, k_values: Optional[List[Fraction]] = None
) -> List[Dict[str, Any]]:
    """Numerical verification of c-complementarity at specific k values.

    c(W_k(f_lam)) + c(W_{k'}(f_{lam^t})) should be k-independent.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 7, 10, 50, 100]]

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)

    results = []
    for kv_num in k_values:
        kv_dual = Fraction(-1) * kv_num - 2 * N

        if kv_num + N == 0 or kv_dual + N == 0:
            continue

        from compute.lib.ds_nonprincipal_shadows import _krw_central_charge as _krw_c_frac
        source_c = _krw_c_frac(lam, kv_num)
        dual_c = _krw_c_frac(lam_t, kv_dual)

        results.append({
            "k": kv_num,
            "k_dual": kv_dual,
            "source_c": source_c,
            "dual_c": dual_c,
            "c_sum": source_c + dual_c,
        })

    return results


def numerical_affine_kappa_check(
    N: int, k_values: Optional[List[Fraction]] = None
) -> List[Dict[str, Any]]:
    """Numerical verification of affine kappa anti-symmetry.

    kappa(V_k(sl_N)) + kappa(V_{k'}(sl_N)) should be 0.
    This is the LEFT side of the commutative diagram.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 7, 10, 50, 100]]

    dim_g = Fraction(N * N - 1)
    h_v = Fraction(N)

    results = []
    for kv_num in k_values:
        kv_dual = Fraction(-1) * kv_num - 2 * N

        if kv_num + h_v == 0 or kv_dual + h_v == 0:
            continue

        kappa_s = dim_g * (kv_num + h_v) / (2 * h_v)
        kappa_d = dim_g * (kv_dual + h_v) / (2 * h_v)

        results.append({
            "k": kv_num,
            "k_dual": kv_dual,
            "kappa_source": kappa_s,
            "kappa_dual": kappa_d,
            "kappa_sum": kappa_s + kappa_d,
            "is_zero": kappa_s + kappa_d == 0,
        })

    return results


def numerical_self_transpose_kappa(
    partition: Partition, k_values: Optional[List[Fraction]] = None
) -> List[Dict[str, Any]]:
    """Numerical kappa sum for self-transpose partitions.

    For self-transpose lambda = lambda^t: the kappa sum
    kappa(W_k(f_lam)) + kappa(W_{k'}(f_lam)) is k-independent.
    """
    if k_values is None:
        k_values = [Fraction(n) for n in [1, 2, 3, 5, 7, 10, 50, 100]]

    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)

    if lam != lam_t:
        return [{"error": "not self-transpose"}]

    results = []
    for kv_num in k_values:
        kv_dual = Fraction(-1) * kv_num - 2 * N

        if kv_num + N == 0 or kv_dual + N == 0:
            continue

        from compute.lib.ds_nonprincipal_shadows import _krw_central_charge as _krw_c_frac
        c_s = _krw_c_frac(lam, kv_num)
        c_d = _krw_c_frac(lam, kv_dual)

        level_source = Rational(kv_num.numerator, kv_num.denominator)
        level_dual = Rational(kv_dual.numerator, kv_dual.denominator)
        rho = anomaly_ratio_from_partition(lam)
        kappa_s = ds_kappa_from_affine(lam, level_source)
        kappa_d = ds_kappa_from_affine(lam, level_dual)
        conductor = kappa_complementarity_sum(lam, level_source)

        results.append({
            "k": kv_num,
            "source_c": c_s,
            "dual_c": c_d,
            "rho": rho,
            "kappa_source": kappa_s,
            "kappa_dual": kappa_d,
            "kappa_sum": conductor,
        })

    return results


# ============================================================================
# 9.  BRST spectral sequence page analysis
# ============================================================================

def brst_spectral_sequence_page(partition: Partition) -> Dict[str, Any]:
    """Return a page candidate and the typed BRST-collapse claim."""
    lam = normalize_partition(partition)
    N = partition_size(lam)

    n_dim = _n_plus_dimension(lam)
    grades = _n_plus_grade_structure(lam)
    max_grade = max(grades.keys()) if grades else 0

    g0_reductive = is_hook_partition(lam) or lam == (N,)

    if lam == (N,):
        page = 2
        reason = "principal CE page candidate"
    elif is_hook_partition(lam):
        n_abelian = _n_plus_is_abelian(lam)
        if n_abelian:
            reason = "abelian-n_plus page candidate"
            page = 1
        else:
            reason = "Kazhdan page candidate"
            page = 2
    else:
        page = int(2 * max_grade)
        reason = f"grade-bound candidate from max ad-grade {max_grade}"

    collapse = _conditional(
        f"BRST spectral-sequence collapse for {lam}",
        "a source-backed associated-graded BRST theorem in this good-grading convention",
        "boundedness and convergence of the completed filtration",
        evidence=(f"candidate page {page}", f"exact max ad-grade {max_grade}"),
    )
    return {
        "partition": lam,
        "candidate_collapse_page": page,
        "candidate_reason": reason,
        "collapse": collapse,
        "n_plus_dim": n_dim,
        "max_ad_grade": max_grade,
        "g_0_reductive": g0_reductive,
    }


# ============================================================================
# 10.  Generator matching under Koszul duality
# ============================================================================

def generator_matching_under_kd(partition: Partition) -> Dict[str, Any]:
    """Compare generator content of W(f_lam) and W(f_{lam^t}).

    For self-transpose: same generator content.
    For non-self-transpose: different generator content (expected).
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)

    source_gens = w_algebra_generator_data(lam)
    dual_gens = w_algebra_generator_data(lam_t)

    source_weights = sorted([w for (_, w, _) in source_gens.strong_generators])
    dual_weights = sorted([w for (_, w, _) in dual_gens.strong_generators])

    is_self_t = (lam == lam_t)
    if is_self_t:
        weights_match = source_weights == dual_weights
    else:
        weights_match = None  # Not expected to match

    return {
        "partition": lam,
        "transpose": lam_t,
        "is_self_transpose": is_self_t,
        "source_n_generators": source_gens.f_centralizer_dimension,
        "dual_n_generators": dual_gens.f_centralizer_dimension,
        "source_weights": source_weights,
        "dual_weights": dual_weights,
        "source_n_bosonic": source_gens.n_bosonic,
        "source_n_fermionic": source_gens.n_fermionic,
        "dual_n_bosonic": dual_gens.n_bosonic,
        "dual_n_fermionic": dual_gens.n_fermionic,
        "weights_match": weights_match,
    }


# ============================================================================
# 11.  c-sum compatibility constant
# ============================================================================

def ds_kd_compatibility_constant(partition: Partition) -> Dict[str, Any]:
    """Compute the c-sum Koszul duality constant for a hook pair.

    c(W_k(f_lam)) + c(W_{k'}(f_{lam^t})) = C_KD (k-independent).
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    kvar = Symbol('k')
    kv = hook_dual_level_sl_n(N, kvar)

    source_c = krw_central_charge(lam, kvar)
    dual_c = krw_central_charge(lam_t, kv)
    c_sum = simplify(source_c + dual_c)
    dc_dk = simplify(c_sum.diff(kvar))
    is_constant = dc_dk == 0

    return {
        "partition": lam,
        "transpose": lam_t,
        "N": N,
        "c_sum_expression": c_sum,
        "c_sum_is_constant": is_constant,
        "c_sum_value": simplify(c_sum) if is_constant else c_sum,
    }


# ============================================================================
# 12.  Anomaly ratio duality analysis
# ============================================================================

def anomaly_ratio_duality(partition: Partition) -> Dict[str, Any]:
    """Anomaly ratio data for a hook duality pair."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)

    rho_source = anomaly_ratio_from_partition(lam)
    rho_dual = anomaly_ratio_from_partition(lam_t)

    c_data_source = krw_central_charge_data(lam)
    c_data_dual = krw_central_charge_data(lam_t)

    # For the c-sum to be k-independent, we need:
    # A_s + A_d - B_s/(k+N) - B_d/(-k-N) = const
    # => A_s + A_d - B_s/(k+N) + B_d/(k+N) = const
    # => B_d = B_s (the quadratic coefficients must match)
    B_s = c_data_source.quadratic_coeff
    B_d = c_data_dual.quadratic_coeff
    quadratic_match = (B_s == B_d)

    return {
        "partition": lam,
        "transpose": lam_t,
        "rho_source": rho_source,
        "rho_dual": rho_dual,
        "rho_equal": _open(
            f"equality of represented anomaly ratios for {lam},{lam_t}",
            *rho_source.hypotheses,
            *rho_dual.hypotheses,
            "a common genus-one trace channel for the pair",
        ),
        "quadratic_coeff_source": B_s,
        "quadratic_coeff_dual": B_d,
        "quadratic_match": quadratic_match,
    }


# ============================================================================
# 13.  Self-dual hook analysis
# ============================================================================

def self_dual_hook_analysis(N: int) -> List[Dict[str, Any]]:
    """Analyze self-dual (self-transpose) hook partitions for sl_N.

    Self-transpose hook (N-r, 1^r) requires N = 2r+1 (odd N only).
    """
    results = []
    for r in range(1, N):
        lam = hook_partition(N, r)
        lam_t = transpose_partition(lam)
        if lam == lam_t:
            results.append({
                "N": N,
                "partition": lam,
                "r": r,
                "is_self_transpose": True,
                "rho": anomaly_ratio_from_partition(lam),
            })
    return results
