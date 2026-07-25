"""Exact type-A DS arithmetic and typed arbitrary-nilpotent obligations.

The module computes partition, centralizer, ghost, generator, and KRW
central-charge data.  Modular characteristics and every passage from those
scalars to DS--bar commutation, PBW collapse, shadow depth, or transport are
represented by ``ClaimPacket`` objects.

Six audit lanes:
  (a) exact partition and KRW data with typed DS--bar status;
  (b) formal reflected central scalars with typed modular conductors;
  (c) affine Slodowy geometry with typed PBW/Koszul promotion;
  (d) exact BRST dimensions with a typed mixed-commutator claim;
  (e) generator-weight pole bounds with typed spectral conclusions;
  (f) finite graph edges with typed categorical transport.

Mathematical framework:
  The conjecture (conj:ds-kd-arbitrary-nilpotent) asserts that for any
  simple g and any nilpotent f in g, the DS reduction functor DS_f
  commutes with bar-cobar duality:

    DS_f(B(V_k(g))) ~ B(W_k(g, f))

  at generic level k. The hook-type corridor in type A is conditional on
  its named DS/bar and completion package. The question is whether non-hook
  nilpotents (e.g., (2,2) in sl_4, (3,2) in sl_5, (2,2,1) in sl_5)
  also satisfy commutation.

  The computational strategy tests generator matching and central-charge
  threading for nilpotents in sl_N (N = 3..7).  Modular compatibility and
  PBW--Slodowy promotion remain typed comparison problems.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    H_HOOK_DS_BAR,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    ghost_constant,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    krw_central_charge_data,
    w_algebra_generator_data,
)
from compute.lib.nonprincipal_ds_orbits import (
    _partitions_of_n,
    centralizer_dimension_sl_n,
    is_hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)
from compute.lib.hook_transport_corridor import ReductionGraph
from compute.lib.ds_kd_red_team import (
    H_BAR_BRST_BICOMPLEX,
    H_CATEGORICAL_TRANSPORT,
    H_DS_KD_COMPARISON,
    H_EXT_OBSTRUCTION,
    H_KAZHDAN_FORMALITY,
    H_MODULAR_GENUS_ONE,
    H_NONPRINCIPAL_LEVEL,
)

Partition = Tuple[int, ...]
k = Symbol('k')


def _open(statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()) -> ClaimPacket:
    """Create an unresolved claim with its promotion obligations."""

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
    """Create a conditional comparison with no scalar value."""

    return ClaimPacket(
        statement,
        ClaimStatus.CONDITIONAL,
        None,
        evidence=evidence,
        hypotheses=tuple(dict.fromkeys(hypotheses)),
    )


# ===================================================================
# (a) DS-bar commutation: three-criterion check for ANY partition
# ===================================================================

@dataclass(frozen=True)
class DSBarCommutationResult:
    """Exact arithmetic and typed DS--bar claims for one orbit."""

    N: int
    partition: Partition
    transpose: Partition
    orbit_class: str
    is_hook: bool
    # Criterion (i): kappa compatibility
    ghost_constant_value: object
    anomaly_ratio: ClaimPacket
    kappa_formula: ClaimPacket
    kappa_compatibility: ClaimPacket
    # Criterion (ii): generator matching
    n_generators: int
    centralizer_dim: int
    generators_match: bool
    # Criterion (iii): central charge threading
    central_charge: object
    c_leading: object
    c_quadratic: object
    krw_formula_consistent: bool
    # Categorical claim
    ds_bar_commutation: ClaimPacket


def ds_bar_commutation_any_partition(
    partition: Partition, level=Symbol('k')
) -> DSBarCommutationResult:
    """Return exact scalar checks and the typed DS--bar obligation.

    The generator/centralizer equality and KRW formula evaluation are exact.
    Modular compatibility and DS--bar commutation retain their independent
    genus-one and chain-level packages.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    lam_t = transpose_partition(lam)
    orbit_cls = type_a_orbit_class(lam)
    hook = is_hook_partition(lam)
    lev = sympify(level)

    # The modular lane remains typed.
    C_lam = ghost_constant(lam)
    kappa_w = ds_kappa_from_affine(lam, lev)
    rho = anomaly_ratio_from_partition(lam)
    kappa_compatibility = _open(
        f"genus-one kappa compatibility for W(sl_{N}, f_{lam})",
        H_MODULAR_GENUS_ONE,
        H_DS_KD_COMPARISON,
        evidence=(f"exact KRW central charge {krw_central_charge(lam, lev)}",),
    )

    # (ii) Generators
    gen_data = w_algebra_generator_data(lam)
    n_gens = gen_data.f_centralizer_dimension
    cent_dim = centralizer_dimension_sl_n(lam)
    # f-centralizer dimension should equal g^f = centralizer of f in g
    # For sl_N: dim(g^f) = sum_i (lambda^t_i)^2 - 1
    gens_ok = (n_gens == cent_dim)

    # (iii) Central charge: verify krw_central_charge_data.central_charge matches
    cc_data = krw_central_charge_data(lam)
    c_formula = krw_central_charge(lam, lev)
    c_from_data = cc_data.central_charge.subs(Symbol('k'), lev)
    c_ok = simplify(c_formula - c_from_data) == 0

    if hook:
        commutation = _conditional(
            f"DS--bar commutation for the hook orbit {lam} in sl_{N}",
            H_HOOK_DS_BAR,
            "the hypotheses of the hook transport corridor at the selected level",
            evidence=(
                f"generator-centralizer equality {n_gens}={cent_dim}",
                f"exact KRW threading check {c_ok}",
            ),
        )
    else:
        commutation = _open(
            f"DS--bar commutation for the non-hook orbit {lam} in sl_{N}",
            H_DS_KD_COMPARISON,
            H_BAR_BRST_BICOMPLEX,
            H_KAZHDAN_FORMALITY,
            evidence=(
                f"generator-centralizer equality {n_gens}={cent_dim}",
                f"exact KRW threading check {c_ok}",
            ),
        )

    return DSBarCommutationResult(
        N=N,
        partition=lam,
        transpose=lam_t,
        orbit_class=orbit_cls,
        is_hook=hook,
        ghost_constant_value=C_lam,
        anomaly_ratio=rho,
        kappa_formula=kappa_w,
        kappa_compatibility=kappa_compatibility,
        n_generators=n_gens,
        centralizer_dim=cent_dim,
        generators_match=gens_ok,
        central_charge=c_formula,
        c_leading=cc_data.leading_term,
        c_quadratic=cc_data.quadratic_coeff,
        krw_formula_consistent=c_ok,
        ds_bar_commutation=commutation,
    )


def verify_all_partitions_sl_n(N: int) -> Dict[Partition, DSBarCommutationResult]:
    """Return exact checks and typed DS--bar claims for every partition."""
    results = {}
    for lam in _partitions_of_n(N):
        if lam == (1,) * N:
            # Skip the trivial partition (= affine algebra itself)
            continue
        results[lam] = ds_bar_commutation_any_partition(lam)
    return results


# ===================================================================
# (b) Central charge complementarity for all dual pairs
# ===================================================================

@dataclass(frozen=True)
class ComplementarityResult:
    """Central charge and kappa complementarity for a dual pair."""

    partition: Partition
    transpose: Partition
    N: int
    # Kappa sum: kappa(W_k(f)) + kappa(W_{k^v}(f^t))
    source_kappa: ClaimPacket
    dual_kappa: ClaimPacket
    kappa_sum: ClaimPacket
    kappa_sum_k_independent: ClaimPacket
    # c sum: c(W_k(f)) + c(W_{k^v}(f^t))
    c_sum: object
    c_sum_k_independent: bool
    # Ghost constants
    ghost_sum: object  # C_lambda + C_{lambda^t}


def complementarity_check(
    partition: Partition, level=Symbol('k')
) -> ComplementarityResult:
    """Check central charge and kappa complementarity for lambda <-> lambda^t."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    lam_t = transpose_partition(lam)
    lev = sympify(level)
    kv = hook_dual_level_sl_n(N, lev)

    # Kappa and its conductor remain on the typed modular lane.
    kappa_source = ds_kappa_from_affine(lam, lev)
    kappa_dual = ds_kappa_from_affine(lam_t, kv)
    kappa_sum = kappa_complementarity_sum(lam, lev)
    kappa_k_indep = _open(
        f"level-independence of the modular conductor for {lam} and {lam_t}",
        *kappa_sum.hypotheses,
        "a represented trace calculation proving constancy in the level parameter",
    )

    # c
    c_source = krw_central_charge(lam, lev)
    c_dual = krw_central_charge(lam_t, kv)
    c_sum = simplify(c_source + c_dual)
    c_k_indep = simplify(c_sum.diff(lev)) == 0

    # Ghost
    C_lam = ghost_constant(lam)
    C_lam_t = ghost_constant(lam_t)

    return ComplementarityResult(
        partition=lam,
        transpose=lam_t,
        N=N,
        source_kappa=kappa_source,
        dual_kappa=kappa_dual,
        kappa_sum=kappa_sum,
        kappa_sum_k_independent=kappa_k_indep,
        c_sum=c_sum,
        c_sum_k_independent=c_k_indep,
        ghost_sum=C_lam + C_lam_t,
    )


def complementarity_all_partitions_sl_n(
    N: int,
) -> Dict[Partition, ComplementarityResult]:
    """Check complementarity for all partitions of N."""
    results = {}
    seen = set()
    for lam in _partitions_of_n(N):
        if lam == (1,) * N:
            continue
        lam_t = transpose_partition(lam)
        pair = (min(lam, lam_t), max(lam, lam_t))
        if pair in seen:
            continue
        seen.add(pair)
        results[lam] = complementarity_check(lam)
    return results


# ===================================================================
# (c) Affine Slodowy input and typed PBW/Koszul promotion
# ===================================================================

@dataclass(frozen=True)
class PBWKoszulnessResult:
    """Exact Slodowy data and typed PBW/Koszul claims."""

    partition: Partition
    N: int
    orbit_class: str
    # Slodowy slice data
    slice_dim: int  # dim(S_f) = dim(g^f)
    # Li filtration: gr_Li W ~ C[J S_f]
    # S_f = f + g^e is an affine space of dimension dim(g^e) = dim(g^f)
    # (since dim(g^e) = dim(g^f) for sl_N)
    # So C[J S_f] ~ Sym_partial(V) with V = (g^e)^*
    # => PBW-Slodowy collapse applies => W is completed Koszul
    pbw_generators_dim: int  # = dim(g^e) = dim(g^f)
    # The PBW-Slodowy theorem applies if:
    # (1) filtration is exhaustive, separated, multiplicative
    # (2) finite-dim per weight, filtration bounded below
    # (3) gr_F A ~ Sym_partial(V)
    # All three hold for universal W-algebras at generic level.
    slodowy_slice_affine: bool
    pbw_collapse_applies: ClaimPacket
    is_chirally_koszul: ClaimPacket


def pbw_koszulness_check(partition: Partition) -> PBWKoszulnessResult:
    """Return exact Slodowy geometry and typed PBW/Koszul claims.

    The key fact: for ANY nilpotent f in sl_N, the Slodowy slice
    S_f = f + g^e is an affine space. The arc space J(S_f) = J(A^d)
    for d = dim(g^e), so C[J(S_f)] ~ Sym_partial((g^e)^*).

    The affine-space identity supplies the associated-graded target.  A
    source-backed Li theorem in the selected presentation, convergence of the
    filtered chiral bar complex, and extension control supply the promotion.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    orbit_cls = type_a_orbit_class(lam)

    # dim(g^f) = dim(g^e) = centralizer dimension
    cent_dim = centralizer_dimension_sl_n(lam)

    # Slodowy slice is ALWAYS affine for sl_N
    # S_f = f + g^e ~ A^{cent_dim}
    slice_affine = True

    pbw_applies = _conditional(
        f"PBW--Slodowy collapse for W(sl_{N}, f_{lam})",
        "the Li associated-graded identification in the selected level convention",
        "a complete separated multiplicative filtration with finite weight pieces",
        "convergence of the filtered chiral bar spectral sequence",
        evidence=(f"exact affine Slodowy-slice dimension {cent_dim}",),
    )
    is_koszul = _conditional(
        f"completed chiral Koszulness of W(sl_{N}, f_{lam})",
        *pbw_applies.hypotheses,
        "the PBW--Slodowy collapse theorem in the completed chiral category",
    )

    return PBWKoszulnessResult(
        partition=lam,
        N=N,
        orbit_class=orbit_cls,
        slice_dim=cent_dim,
        pbw_generators_dim=cent_dim,
        slodowy_slice_affine=slice_affine,
        pbw_collapse_applies=pbw_applies,
        is_chirally_koszul=is_koszul,
    )


# ===================================================================
# (d) BV/BRST: Q_DS and d_bar commutation
# ===================================================================

@dataclass(frozen=True)
class BRSTBarCommutationResult:
    """BRST-bar commutation data for DS reduction."""

    partition: Partition
    N: int
    # BRST complex dimensions
    ghost_plus_dim: int   # dim(n_+) = number of positive-grade directions
    ghost_half_dim: int   # dim(g_{1/2}) = fermionic ghost sector
    ghost_int_dim: int    # dim(g_{j>0, j integer}) = bosonic constraint sector
    # The BRST charge Q_DS has ghost number +1 and is nilpotent (Q^2 = 0)
    # The bar differential d_bar has bar degree +1 and d_bar^2 = 0
    # The key claim: [Q_DS, d_bar] = 0 (they commute as differations)
    # This follows from:
    # (1) Q_DS acts on the BRST complex, d_bar on the bar complex
    # (2) They act on different tensor factors
    # (3) DS is a BRST cohomology operation; bar is a deformation-theoretic
    #     operation. Both are MC elements in their respective convolution
    #     algebras, and the convolution algebras are INDEPENDENT.
    brst_bar_commutation: ClaimPacket
    # Consequence: the DS-bar spectral sequence has
    # E_0 = B(V_k(g)) tensor ghost complex
    # d_0 = d_bar (bar differential)
    # d_1 = Q_DS (BRST charge)
    # E_1 = H_bar(V_k(g)) tensor ghost complex
    # E_2 = H_DS(H_bar(V_k(g)))
    # vs the other order:
    # E_0' = B(V_k(g)) tensor ghost complex
    # d_0' = Q_DS
    # d_1' = d_bar
    # E_1' = B(DS(V_k(g))) = B(W_k(g,f))
    # The conjecture: E_2 = E_1' (the two spectral sequences agree at E_2)
    spectral_sequence_realization: ClaimPacket


def brst_bar_commutation_check(partition: Partition) -> BRSTBarCommutationResult:
    """Check BRST-bar commutation structure for a DS reduction."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]

    # Count positive-grade directions
    ghost_plus = 0
    ghost_half = 0
    ghost_int = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            eigenval = Rational(h_diag[i] - h_diag[j], 2)
            if eigenval > 0:
                ghost_plus += 1
                if eigenval == Rational(1, 2):
                    ghost_half += 1
                elif eigenval.is_integer:
                    ghost_int += 1

    commutation = _open(
        f"commutation of the BRST and chiral-bar differentials for {lam}",
        "a common completed complex carrying both differentials",
        "an explicit mixed-commutator calculation including collision residues",
        "compatible signs, filtrations, and continuity",
        evidence=(
            f"exact positive ghost dimension {ghost_plus}",
            f"exact half-integral ghost dimension {ghost_half}",
        ),
    )
    ss_realization = _open(
        f"DS--bar double spectral sequence for {lam}",
        *commutation.hypotheses,
        "boundedness or completeness sufficient for convergence",
    )

    return BRSTBarCommutationResult(
        partition=lam,
        N=N,
        ghost_plus_dim=ghost_plus,
        ghost_half_dim=ghost_half,
        ghost_int_dim=ghost_int,
        brst_bar_commutation=commutation,
        spectral_sequence_realization=ss_realization,
    )


# ===================================================================
# (e) Spectral sequence degeneration for non-hook types
# ===================================================================

@dataclass(frozen=True)
class SpectralSequenceResult:
    """Exact generator-weight bound and typed spectral conclusions."""

    partition: Partition
    N: int
    orbit_class: str
    is_hook: bool
    e1_degeneration_at_generic: ClaimPacket
    bar_cohomology_concentrated: ClaimPacket
    generator_weight_pole_bound: int
    shadow_depth_class: ClaimPacket


def spectral_sequence_check(partition: Partition) -> SpectralSequenceResult:
    """Return the spectral obligations and a generator-weight locality bound."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    orbit_cls = type_a_orbit_class(lam)
    hook = is_hook_partition(lam)

    e1_ok = _open(
        f"E1 degeneration of the DS--bar spectral sequence for {lam}",
        H_DS_KD_COMPARISON,
        H_BAR_BRST_BICOMPLEX,
        H_KAZHDAN_FORMALITY,
    )
    bar_conc = _open(
        f"bar-cohomology concentration for W(sl_{N}, f_{lam})",
        *e1_ok.hypotheses,
        H_KAZHDAN_FORMALITY,
    )

    # Locality gives a candidate bound from the two largest weights.  The
    # actual singular packet requires OPE coefficients.
    gen_data = w_algebra_generator_data(lam)
    weights = sorted([w for (_, w, _) in gen_data.strong_generators], reverse=True)
    if len(weights) >= 2:
        max_pole = int(weights[0] + weights[1])
    elif len(weights) == 1:
        max_pole = int(2 * weights[0])
    else:
        max_pole = 2

    depth_class = _open(
        f"full shadow-depth class of W(sl_{N}, f_{lam})",
        "the complete Maurer--Cartan tower with collision normalization",
        "a termination or nontermination argument beyond the generator-weight pole bound",
        evidence=(f"exact generator-weight pole bound {max_pole}",),
    )

    return SpectralSequenceResult(
        partition=lam,
        N=N,
        orbit_class=orbit_cls,
        is_hook=hook,
        e1_degeneration_at_generic=e1_ok,
        bar_cohomology_concentrated=bar_conc,
        generator_weight_pole_bound=max_pole,
        shadow_depth_class=depth_class,
    )


# ===================================================================
# (f) Edge-compatibility and transport-closure
# ===================================================================

@dataclass(frozen=True)
class EdgeCompatibilityResult:
    """Exact edge arithmetic and typed transport claims."""

    source: Partition
    target: Partition
    N: int
    source_class: str
    target_class: str
    # An edge (lambda -> mu) is "compatible" with DS-bar commutation if:
    # (1) Both source and target pass the three-criterion check
    # (2) The kappa difference kappa(W(f_lambda)) - kappa(W(f_mu)) equals
    #     the ghost constant difference C_mu - C_lambda
    # (3) The central charge transformation is consistent
    source_commutation: ClaimPacket
    target_commutation: ClaimPacket
    kappa_difference: ClaimPacket
    central_charge_difference: object
    edge_transport: ClaimPacket


def edge_compatibility_check(
    source: Partition, target: Partition, level=Symbol('k')
) -> EdgeCompatibilityResult:
    """Check edge-compatibility for one reduction graph edge."""
    src = normalize_partition(source)
    tgt = normalize_partition(target)
    N_src = partition_size(src)
    N_tgt = partition_size(tgt)
    if N_src != N_tgt:
        raise ValueError("Source and target must be partitions of the same N")
    N = N_src
    lev = sympify(level)

    src_cls = type_a_orbit_class(src)
    tgt_cls = type_a_orbit_class(tgt)

    # Source and target DS--bar comparisons remain typed.
    src_check = ds_bar_commutation_any_partition(src, lev)
    tgt_check = ds_bar_commutation_any_partition(tgt, lev)
    src_claim = src_check.ds_bar_commutation
    tgt_claim = tgt_check.ds_bar_commutation

    kappa_src = ds_kappa_from_affine(src, lev)
    kappa_tgt = ds_kappa_from_affine(tgt, lev)
    kappa_diff = _open(
        f"modular-characteristic difference along {src}->{tgt}",
        *kappa_src.hypotheses,
        *kappa_tgt.hypotheses,
        "a common represented genus-one trace normalization",
    )

    # Central charge transformation
    c_src = krw_central_charge(src, lev)
    c_tgt = krw_central_charge(tgt, lev)
    c_diff = simplify(c_src - c_tgt)
    edge_claim = _open(
        f"DS transport realization along the dominance edge {src}->{tgt}",
        H_CATEGORICAL_TRANSPORT,
        H_DS_KD_COMPARISON,
        evidence=(f"exact KRW central-charge difference {c_diff}",),
    )

    return EdgeCompatibilityResult(
        source=src,
        target=tgt,
        N=N,
        source_class=src_cls,
        target_class=tgt_cls,
        source_commutation=src_claim,
        target_commutation=tgt_claim,
        kappa_difference=kappa_diff,
        central_charge_difference=c_diff,
        edge_transport=edge_claim,
    )


def all_edges_compatible_sl_n(N: int) -> Dict[Tuple[Partition, Partition], EdgeCompatibilityResult]:
    """Check edge-compatibility for all edges of the reduction graph Gamma_N."""
    G = ReductionGraph.build(N)
    results = {}
    seen = set()
    for src, tgt in G.edges:
        pair = (min(src, tgt), max(src, tgt))
        if pair in seen:
            continue
        seen.add(pair)
        results[(src, tgt)] = edge_compatibility_check(src, tgt)
    return results


# ===================================================================
# Non-hook specific checks
# ===================================================================

def non_hook_partitions_sl_n(N: int) -> List[Partition]:
    """Return all non-hook, non-trivial partitions of N."""
    return [
        lam for lam in _partitions_of_n(N)
        if not is_hook_partition(lam) and lam != (1,) * N
    ]


@dataclass(frozen=True)
class NonHookDefenseResult:
    """Complete defense data for a non-hook partition."""

    partition: Partition
    N: int
    orbit_class: str
    # Three-criterion check
    commutation: DSBarCommutationResult
    # Complementarity
    complementarity: ComplementarityResult
    # PBW Koszulness
    pbw: PBWKoszulnessResult
    # BRST-bar
    brst: BRSTBarCommutationResult
    # Spectral sequence
    spectral: SpectralSequenceResult
    theorem_status: ClaimPacket


def non_hook_defense(partition: Partition) -> NonHookDefenseResult:
    """Complete defense evidence for one non-hook partition."""
    lam = normalize_partition(partition)
    N = partition_size(lam)
    orbit_cls = type_a_orbit_class(lam)

    comm = ds_bar_commutation_any_partition(lam)
    comp = complementarity_check(lam)
    pbw = pbw_koszulness_check(lam)
    brst = brst_bar_commutation_check(lam)
    spec = spectral_sequence_check(lam)

    theorem_status = _open(
        f"arbitrary-nilpotent DS--Koszul theorem for {lam} in sl_{N}",
        *comm.ds_bar_commutation.hypotheses,
        *comp.kappa_sum.hypotheses,
        *pbw.is_chirally_koszul.hypotheses,
        *brst.brst_bar_commutation.hypotheses,
        *spec.e1_degeneration_at_generic.hypotheses,
    )

    return NonHookDefenseResult(
        partition=lam,
        N=N,
        orbit_class=orbit_cls,
        commutation=comm,
        complementarity=comp,
        pbw=pbw,
        brst=brst,
        spectral=spec,
        theorem_status=theorem_status,
    )


def full_non_hook_defense_sl_n(N: int) -> Dict[Partition, NonHookDefenseResult]:
    """Complete defense for all non-hook partitions of N."""
    results = {}
    for lam in non_hook_partitions_sl_n(N):
        results[lam] = non_hook_defense(lam)
    return results


# ===================================================================
# Summary and strength assessment
# ===================================================================

@dataclass(frozen=True)
class DefenseStrength:
    """Status ledger for one arbitrary-nilpotent comparison."""

    partition: Partition
    generator_match_computed: bool
    krw_formula_computed: bool
    kappa_status: ClaimStatus
    complementarity_status: ClaimStatus
    pbw_status: ClaimStatus
    brst_status: ClaimStatus
    spectral_status: ClaimStatus
    overall: ClaimPacket


def assess_defense_strength(partition: Partition) -> DefenseStrength:
    """Return exact checks and statuses without aggregating them to truth."""
    lam = normalize_partition(partition)
    defense = non_hook_defense(lam) if not is_hook_partition(lam) else None
    comm = defense.commutation if defense else ds_bar_commutation_any_partition(lam)
    comp = defense.complementarity if defense else complementarity_check(lam)
    pbw = defense.pbw if defense else pbw_koszulness_check(lam)
    brst = defense.brst if defense else brst_bar_commutation_check(lam)
    spectral = defense.spectral if defense else spectral_sequence_check(lam)
    overall = defense.theorem_status if defense else comm.ds_bar_commutation

    return DefenseStrength(
        partition=lam,
        generator_match_computed=comm.generators_match,
        krw_formula_computed=comm.krw_formula_consistent,
        kappa_status=comm.kappa_compatibility.status,
        complementarity_status=comp.kappa_sum.status,
        pbw_status=pbw.is_chirally_koszul.status,
        brst_status=brst.brst_bar_commutation.status,
        spectral_status=spectral.e1_degeneration_at_generic.status,
        overall=overall,
    )


def defense_summary(max_N: int = 7) -> List[dict]:
    """Summary table of defense strength for all non-hook partitions up to sl_{max_N}."""
    rows = []
    for N in range(4, max_N + 1):
        for lam in non_hook_partitions_sl_n(N):
            defense = non_hook_defense(lam)
            strength = assess_defense_strength(lam)
            rows.append({
                'N': N,
                'partition': lam,
                'orbit_class': type_a_orbit_class(lam),
                'generator_match_computed': defense.commutation.generators_match,
                'krw_formula_computed': defense.commutation.krw_formula_consistent,
                'ds_bar_status': defense.commutation.ds_bar_commutation.status,
                'conductor_status': defense.complementarity.kappa_sum.status,
                'pbw_status': defense.pbw.is_chirally_koszul.status,
                'overall_status': strength.overall.status,
                'overall_hypotheses': strength.overall.hypotheses,
            })
    return rows


# ===================================================================
# Ghost constant identities and structural results
# ===================================================================

def ghost_constant_symmetry_check(N: int) -> Dict[Partition, bool]:
    """Verify transpose symmetry and nonnegativity of the finite ghost ledger."""
    results = {}
    for lam in _partitions_of_n(N):
        if lam == (1,) * N:
            continue
        lam_t = transpose_partition(lam)
        C1 = ghost_constant(lam)
        C2 = ghost_constant(lam_t)
        # C_lambda + C_{lambda^t} should be a positive rational
        results[lam] = (C1 + C2 > 0 and C1 >= 0 and C2 >= 0)
    return results


def ghost_constant_ordering_check(N: int) -> List[Tuple[Partition, Rational]]:
    """List ghost constants for all partitions of N, sorted by value.

    The ghost constant increases with orbit dimension:
    larger orbits have larger ghost constants.
    """
    data = []
    for lam in _partitions_of_n(N):
        if lam == (1,) * N:
            data.append((lam, Rational(0)))
        else:
            data.append((lam, ghost_constant(lam)))
    return sorted(data, key=lambda x: x[1])


def verify_ghost_orbit_monotonicity(N: int) -> bool:
    """Verify that ghost constant is monotone with respect to orbit closure.

    In type A, the partial order on orbits corresponds to the dominance
    order on partitions. Ghost constant should respect this: if
    lambda >= mu in dominance order, then C_lambda >= C_mu.
    """
    data = ghost_constant_ordering_check(N)
    partitions = _partitions_of_n(N)

    for lam in partitions:
        for mu in partitions:
            # Check dominance: lam >= mu iff sum_{i<=k} lam_i >= sum_{i<=k} mu_i for all k
            lam_n = normalize_partition(lam)
            mu_n = normalize_partition(mu)
            max_len = max(len(lam_n), len(mu_n))
            lam_padded = lam_n + (0,) * (max_len - len(lam_n))
            mu_padded = mu_n + (0,) * (max_len - len(mu_n))

            # Check lam dominates mu
            dominates = True
            for i in range(max_len):
                if sum(lam_padded[:i+1]) < sum(mu_padded[:i+1]):
                    dominates = False
                    break

            if dominates:
                C_lam = ghost_constant(lam) if lam != (1,) * N else Rational(0)
                C_mu = ghost_constant(mu) if mu != (1,) * N else Rational(0)
                if C_lam < C_mu:
                    return False
    return True
