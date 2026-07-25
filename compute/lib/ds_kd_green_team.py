"""Exact strategy data and typed DS--Koszul research obligations.

Five candidate strategies organize the obligations in arbitrary-nilpotent
DS--Koszul comparison.

Strategy A — Induction on orbit closure order
  Nilpotent orbits form a poset under closure.  Principal (maximal) is
  principal and hook orbits provide conditional seeds.  The closure order
  supplies candidate paths; a reduction-by-stages functor must realize them.

  Key data: each cover O' < O supplies exact orbit, centralizer, generator,
  and KRW central-charge ledgers.  A reduction-by-stages theorem supplies
  the categorical transport.

Strategy B — BFN / Coulomb branch isomorphism
  A candidate framed quiver supplies finite rank data.  A sourced BFN--
  Slodowy identification and a chiral uplift are separate proof obligations.

  Key test: sl_3 subregular W-algebra matches Coulomb branch of a
  specific (framed) quiver.

Strategy C — Derived DS = homotopy DS (formality route)
  Replace classical BRST DS with the full derived/homotopy DS functor.
  Since bar is also derived, one seeks a natural interchange morphism and a
  comparison from derived DS to classical DS.  Both constructions require
  explicit completion and formality hypotheses.

Strategy D — Shadow-level commutation
  Instead of chain-level commutation, prove DS and bar commute at the
  shadow level.  At each arity r, DS(Θ_A^{≤r}) = Θ_{DS(A)}^{≤r}.
  At arity 2, the exact KRW and ghost ledgers furnish evidence for a typed
  genus-one trace comparison.
  Arity 3 and every induction step require explicit comparison cocycles in
  the relative deformation complex.

Strategy E — Type-by-type exhaustion at small rank
  Enumerate finite orbit and scalar ledgers at small rank and attach the
  unresolved comparison package to every orbit.

Mathematical context:
  ``conj:ds-kd-arbitrary-nilpotent`` is conjectural.  The hook corridor is
  conditional on its filtered DS/bar, completion, and Verdier package.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Set, Tuple

from sympy import Rational as SRational

from compute.lib.hook_type_w_duality import (
    ClaimPacket,
    ClaimStatus,
    H_HOOK_DS_BAR,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    ghost_constant,
    krw_central_charge,
)
from compute.lib.ds_bar_commutation import affine_kappa_sl_n
from compute.lib.ds_kd_red_team import (
    H_BAR_BRST_BICOMPLEX,
    H_BC_DUALITY,
    H_CATEGORICAL_TRANSPORT,
    H_DS_KD_COMPARISON,
    H_EXT_OBSTRUCTION,
    H_KAZHDAN_FORMALITY,
    H_MODULAR_GENUS_ONE,
    H_TRANSPOSE_DUALITY,
    enumerate_type_b_orbits,
    enumerate_type_c_orbits,
)

# Re-use existing infrastructure
from compute.lib.w_algebra_transport_propagation import (
    Partition,
    partitions,
    transpose,
    is_hook,
    hook_partitions,
    centralizer_dimension,
    nilpotent_orbit_dimension,
    generator_weights,
    dominance_order_covers,
    graph_is_connected,
)


def _open(statement: str, *hypotheses: str, evidence: Tuple[str, ...] = ()) -> ClaimPacket:
    """Return an open strategy claim with its construction obligations."""

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


def _ds_bar_claim(n: int, lam: Partition) -> ClaimPacket:
    """Typed DS--bar status for a type-A orbit."""

    if is_hook(lam):
        return _conditional(
            f"DS--bar commutation for the hook orbit {lam} in sl_{n}",
            H_HOOK_DS_BAR,
            "the hypotheses of the hook transport corridor at the selected level",
        )
    return _open(
        f"DS--bar commutation for the non-hook orbit {lam} in sl_{n}",
        H_DS_KD_COMPARISON,
        H_BAR_BRST_BICOMPLEX,
        H_KAZHDAN_FORMALITY,
    )


# =====================================================================
# STRATEGY A: Induction on orbit closure
# =====================================================================

def closure_poset_covers(n: int) -> List[Tuple[Partition, Partition]]:
    """Covering relations in the closure partial order on nilpotent orbits.

    For type A (sl_N), the closure order on nilpotent orbits coincides
    with the dominance order on partitions:
      O_lambda >= O_mu  iff  lambda >= mu in dominance order.

    Returns pairs (lambda, mu) where O_lambda covers O_mu.
    """
    return dominance_order_covers(n)


def closure_poset_layers(n: int) -> List[List[Partition]]:
    """Stratify partitions into layers by position in the closure poset.

    Layer 0 = maximal orbit (principal partition (n)).
    Layer 1 = orbits covered only by layer-0 elements.
    ...
    Last layer = minimal orbit (trivial partition (1^n)).

    This is the BFS-layer decomposition from the top.
    """
    pars = partitions(n)
    covers = closure_poset_covers(n)

    # Build downward adjacency
    children: Dict[Partition, Set[Partition]] = defaultdict(set)
    parents: Dict[Partition, Set[Partition]] = defaultdict(set)
    for lam, mu in covers:
        children[lam].add(mu)
        parents[mu].add(lam)

    # Top element is (n)
    top = tuple([n])
    layers: List[List[Partition]] = []
    assigned: Set[Partition] = set()
    current_layer = [top]
    assigned.add(top)
    layers.append(current_layer)

    while len(assigned) < len(pars):
        next_layer = []
        for lam in current_layer:
            for mu in children.get(lam, set()):
                if mu not in assigned:
                    # Check all parents are already assigned
                    if all(p in assigned for p in parents.get(mu, set())):
                        next_layer.append(mu)
                        assigned.add(mu)
        if not next_layer:
            # Assign remaining (shouldn't happen for connected posets)
            for p in pars:
                if p not in assigned:
                    next_layer.append(p)
                    assigned.add(p)
        layers.append(sorted(next_layer, reverse=True))
        current_layer = next_layer

    return layers


@dataclass(frozen=True)
class InductionStep:
    """Data for one induction step along the closure order."""
    parent: Partition
    child: Partition
    parent_orbit_dim: int
    child_orbit_dim: int
    parent_centralizer_dim: int
    child_centralizer_dim: int
    parent_gen_weights: Tuple[Fraction, ...]
    child_gen_weights: Tuple[Fraction, ...]
    parent_is_hook: bool
    child_is_hook: bool
    codimension: int
    central_charge_difference: object


def compute_induction_steps(n: int, k: Fraction = Fraction(7)) -> List[InductionStep]:
    """Compute finite cover data and exact KRW central-charge differences."""
    covers = closure_poset_covers(n)
    steps = []
    level = SRational(k.numerator, k.denominator)
    for lam, mu in covers:
        c_lam = krw_central_charge(lam, level)
        c_mu = krw_central_charge(mu, level)
        steps.append(InductionStep(
            parent=lam,
            child=mu,
            parent_orbit_dim=nilpotent_orbit_dimension(lam),
            child_orbit_dim=nilpotent_orbit_dimension(mu),
            parent_centralizer_dim=centralizer_dimension(lam),
            child_centralizer_dim=centralizer_dimension(mu),
            parent_gen_weights=tuple(generator_weights(lam)),
            child_gen_weights=tuple(generator_weights(mu)),
            parent_is_hook=is_hook(lam),
            child_is_hook=is_hook(mu),
            codimension=nilpotent_orbit_dimension(lam) - nilpotent_orbit_dimension(mu),
            central_charge_difference=c_lam - c_mu,
        ))
    return steps


def induction_feasibility_score(n: int) -> Dict[str, object]:
    """Score the feasibility of Strategy A for sl_N.

    Checks:
    1. Every cover step is reachable from the distinguished hook seed set.
    2. The codimension of each step is bounded (small = easier).
    3. The generator spectrum change is controlled.
    """
    layers = closure_poset_layers(n)
    steps = compute_induction_steps(n)
    covers = closure_poset_covers(n)

    # Build parent map
    parent_map: Dict[Partition, Set[Partition]] = defaultdict(set)
    for lam, mu in covers:
        parent_map[mu].add(lam)

    # Candidate seeds: principal, zero, and hooks.
    reached: Set[Partition] = set()
    reached.add(tuple([n]))
    reached.add(tuple([1] * n))
    for h in hook_partitions(n):
        reached.add(h)

    # Finite reachability closure; this constructs no categorical functor.
    changed = True
    induction_rounds = 0
    while changed:
        changed = False
        induction_rounds += 1
        for lam in partitions(n):
            if lam in reached:
                continue
            pars = parent_map.get(lam, set())
            if pars and all(p in reached for p in pars):
                reached.add(lam)
                changed = True

    all_pars = set(partitions(n))
    remaining = all_pars - reached
    max_codim = max((s.codimension for s in steps), default=0)
    non_hook_steps = [s for s in steps if not s.parent_is_hook or not s.child_is_hook]

    return {
        'n': n,
        'total_orbits': len(all_pars),
        'hook_seed_count': len(reached & set(hook_partitions(n))),
        'candidate_reached_count': len(reached),
        'remaining': len(remaining),
        'remaining_orbits': sorted(remaining, reverse=True),
        'induction_rounds': induction_rounds,
        'max_codimension': max_codim,
        'non_hook_steps': len(non_hook_steps),
        'candidate_closure_covers_all': len(remaining) == 0,
        'transport_realization': _open(
            f"closure-order transport realizes DS--bar commutation in sl_{n}",
            H_CATEGORICAL_TRANSPORT,
            H_DS_KD_COMPARISON,
        ),
        'feasibility': 'high' if len(remaining) == 0 else (
            'medium' if len(remaining) <= 2 else 'low'
        ),
    }


# =====================================================================
# STRATEGY B: BFN / Coulomb branch
# =====================================================================

@dataclass(frozen=True)
class QuiverData:
    """Candidate framed-quiver ledger and typed BFN identification."""

    candidate_gauge_ranks: Tuple[int, ...]
    candidate_framing_ranks: Tuple[int, ...]
    lie_type: str
    nilpotent_partition: Partition
    slodowy_dimension: int
    orbit_dimension: int
    gauge_rank_sum: int
    bfn_slodowy_identification: ClaimPacket


def bfn_quiver_for_type_a(lam: Partition) -> QuiverData:
    """Compute a candidate type-A framed-quiver rank ledger.

    For sl_N with partition lambda = (p_1, ..., p_r), the Coulomb branch
    of the associated quiver gauge theory is isomorphic to the Slodowy
    slice S_lambda.

    The quiver is a framed linear A_{N-1} quiver with gauge ranks
    determined by the partition:
      v_i = sum_{j > i} lambda^t_j  (gauge rank at node i)
      w_i = lambda^t_i - lambda^t_{i+1}  (framing rank at node i)

    The rank transform is exact partition arithmetic.  Its interpretation as
    a BFN Coulomb branch realizing the Slodowy slice is a typed obligation.
    """
    N = sum(lam)
    lam_t = transpose(lam)

    # Pad transpose to length N
    lam_t_padded = list(lam_t) + [0] * (N - len(lam_t))

    # Gauge ranks: v_i = sum_{j > i} lambda^t_j
    gauge = []
    for i in range(len(lam_t_padded)):
        gauge.append(sum(lam_t_padded[j] for j in range(i + 1, len(lam_t_padded))))

    # Framing ranks: w_i = lambda^t_i - lambda^t_{i+1}
    framing = []
    for i in range(len(lam_t_padded)):
        next_val = lam_t_padded[i + 1] if i + 1 < len(lam_t_padded) else 0
        framing.append(lam_t_padded[i] - next_val)

    # Trim trailing zeros
    while gauge and gauge[-1] == 0:
        gauge.pop()
    while framing and framing[-1] == 0:
        framing.pop()

    slodowy_dim = centralizer_dimension(lam)
    orbit_dim = nilpotent_orbit_dimension(lam)
    identification = _open(
        f"BFN Coulomb branch of the candidate quiver realizes S_{lam}",
        "a primary-source BFN/quiver-Slodowy theorem for this rank convention",
        "a Poisson identification with the selected Slodowy slice",
        "a chiral quantization compatible with the W-algebra presentation",
        evidence=(
            f"candidate gauge ranks {tuple(gauge)}",
            f"candidate framing ranks {tuple(framing)}",
            f"exact Slodowy dimension {slodowy_dim}",
        ),
    )

    return QuiverData(
        candidate_gauge_ranks=tuple(gauge),
        candidate_framing_ranks=tuple(framing),
        lie_type='A',
        nilpotent_partition=lam,
        slodowy_dimension=slodowy_dim,
        orbit_dimension=orbit_dim,
        gauge_rank_sum=sum(gauge),
        bfn_slodowy_identification=identification,
    )


def bfn_coulomb_matches_slodowy(lam: Partition) -> ClaimPacket:
    """Return the BFN--Slodowy identification obligation.

    The historical boolean entry point now propagates the typed geometric
    claim instead of comparing a target dimension with itself.
    """

    return bfn_quiver_for_type_a(lam).bfn_slodowy_identification


def bfn_strategy_assessment(n: int) -> Dict[str, object]:
    """Assess BFN strategy for sl_N.

    For each partition:
    1. Build the BFN quiver
    2. Check Coulomb = Slodowy dimension
    3. Check whether the quiver has a known bar-cobar interpretation
    """
    pars = partitions(n)
    results = {}
    identifications = []

    for lam in pars:
        quiver = bfn_quiver_for_type_a(lam)
        identification = bfn_coulomb_matches_slodowy(lam)
        identifications.append(identification)

        label = ''.join(str(p) for p in lam)
        results[f'({label})'] = {
            'candidate_gauge_ranks': quiver.candidate_gauge_ranks,
            'candidate_framing_ranks': quiver.candidate_framing_ranks,
            'gauge_rank_sum': quiver.gauge_rank_sum,
            'slodowy_dim': quiver.slodowy_dimension,
            'orbit_dim': quiver.orbit_dimension,
            'bfn_slodowy_identification': identification,
        }

    return {
        'n': n,
        'partition_ledgers_complete': len(results) == len(pars),
        'bfn_slodowy_identifications': tuple(identifications),
        'quiver_data': results,
        'bottleneck': 'BFN--Slodowy identification and its chiral quantization',
    }


# =====================================================================
# STRATEGY C: Derived DS = homotopy DS (formality route)
# =====================================================================

@dataclass(frozen=True)
class FormalityData:
    """Data relevant to the derived DS ≃ classical DS formality question."""
    partition: Partition
    lie_algebra: str
    rank: int
    is_even_nilpotent: bool
    slodowy_is_affine: bool
    li_filtration_status: ClaimPacket
    formality_realization: ClaimPacket
    remaining_obligation: str


def is_even_nilpotent(lam: Partition) -> bool:
    """A nilpotent in sl_N is even iff all parts of lambda have the same parity.

    Equivalently, the ad(x) eigenvalues are all integers (no half-integers).
    """
    parities = set(p % 2 for p in lam)
    return len(parities) == 1


def slodowy_slice_is_affine(lam: Partition) -> bool:
    """The Slodowy slice S_f = f + g^e is always affine (as a variety).

    This is true for all nilpotents in all types.
    """
    return True


def li_filtration_status(lam: Partition) -> ClaimPacket:
    """Return the source-sensitive Li associated-graded obligation."""
    return _open(
        f"Li associated graded of W(sl_{sum(lam)}, f_{lam}) equals the Slodowy arc algebra",
        "a precise primary-source theorem in the selected nilpotent and level convention",
        "compatibility with the completed filtration used by the chiral bar complex",
    )


def formality_assessment(n: int) -> List[FormalityData]:
    """Record affine Slodowy input and the independent formality claim."""
    results = []
    for lam in partitions(n):
        is_even = is_even_nilpotent(lam)
        li_status = li_filtration_status(lam)

        results.append(FormalityData(
            partition=lam,
            lie_algebra=f'sl_{n}',
            rank=n - 1,
            is_even_nilpotent=is_even,
            slodowy_is_affine=slodowy_slice_is_affine(lam),
            li_filtration_status=li_status,
            formality_realization=_open(
                f"derived DS agrees with classical DS for the orbit {lam} in sl_{n}",
                *li_status.hypotheses,
                "formality of the completed BRST complex",
                H_BAR_BRST_BICOMPLEX,
                H_DS_KD_COMPARISON,
            ),
            remaining_obligation=(
                "construct the completed BRST formality quasi-isomorphism and its "
                "bar-compatible interchange map"
            ),
        ))
    return results


def derived_ds_strategy_score(n: int) -> Dict[str, object]:
    """Collect exact affine inputs and the derived-DS/bar obligation."""
    assessments = formality_assessment(n)
    all_even = all(a.is_even_nilpotent for a in assessments)
    affine_inputs = all(a.slodowy_is_affine for a in assessments)

    return {
        'n': n,
        'all_slodowy_slices_affine': affine_inputs,
        'derived_ds_bar_comparison': _open(
            f"derived-DS/bar comparison for all type-A orbits in sl_{n}",
            H_DS_KD_COMPARISON,
            H_BAR_BRST_BICOMPLEX,
            H_KAZHDAN_FORMALITY,
        ),
        'all_even': all_even,
        'num_orbits': len(assessments),
        'affine_slodowy_count': sum(1 for a in assessments if a.slodowy_is_affine),
        'num_even': sum(1 for a in assessments if a.is_even_nilpotent),
        'bottleneck': 'Derived DS ≃ classical DS (formality of BRST complex)',
    }


# =====================================================================
# STRATEGY D: Shadow-level commutation
# =====================================================================

def generator_weight_shadow_depth_candidate(lam: Partition) -> int:
    """Return the generator-weight depth candidate used for triage.

    Shadow depth classification:
    - G (r_max=2): free/Heisenberg-type
    - L (r_max=3): Lie-type (affine, principal W with rank 1)
    - C (r_max=4): contact-type (beta-gamma, some non-principal)
    - M (r_max=inf): mixed (Virasoro, W_N with N >= 3)

    For W-algebras: the principal W_N has r_max = inf for N >= 3.
    For subregular: depends on the OPE structure.
    For non-principal general: heuristic based on generator degrees.
    This arithmetic classifies a candidate from generator weights.  It carries
    no assertion about termination of the full Maurer--Cartan tower.
    """
    N = sum(lam)
    num_gens = centralizer_dimension(lam)
    max_gen_weight = max(generator_weights(lam)) if generator_weights(lam) else Fraction(1)

    if num_gens == 1:
        # Single generator -> Heisenberg type (if h=1) or Virasoro type (if h=2)
        if max_gen_weight == 1:
            return 2  # G
        elif max_gen_weight == 2:
            return float('inf')  # M (Virasoro-like)
        else:
            return float('inf')  # M
    elif lam == tuple([N]):
        # Principal
        if N == 2:
            return float('inf')  # Virasoro
        return float('inf')  # W_N, M class
    elif is_hook(lam) and lam != tuple([N]):
        # Non-principal hook
        gen_ws = sorted(generator_weights(lam))
        max_w = max(gen_ws)
        if max_w <= 2:
            return 2  # L-like
        elif max_w <= 3:
            return 4  # C-like
        else:
            return float('inf')  # M
    else:
        # General non-hook: heuristic
        gen_ws = sorted(generator_weights(lam))
        max_w = max(gen_ws) if gen_ws else 1
        if max_w >= 3:
            return float('inf')
        return 4


def shadow_depth_estimate(lam: Partition) -> ClaimPacket:
    """Return the open full-shadow-depth claim for one orbit."""

    candidate = generator_weight_shadow_depth_candidate(lam)
    return _open(
        f"full shadow depth of W(sl_{sum(lam)}, f_{lam})",
        "the complete Maurer--Cartan tower with collision normalization",
        "a termination or nontermination theorem beyond generator weights",
        evidence=(f"generator-weight candidate {candidate}",),
    )


def shadow_kappa_ds_commutation(N: int, lam: Partition,
                                 k: Fraction = Fraction(7)) -> Dict[str, object]:
    """Return exact arity-two evidence and the typed comparison claim.

    The affine class-L characteristic, KRW central charge, and DS ghost
    constant are exact convention-fixed scalars.  The reduced modular
    characteristic and its comparison with the affine class remain typed.
    """
    level = SRational(k.numerator, k.denominator)
    kappa_affine = affine_kappa_sl_n(N, level)
    rho = anomaly_ratio_from_partition(tuple(lam))
    c_val = krw_central_charge(tuple(lam), level)
    kappa_w = ds_kappa_from_affine(tuple(lam), level)
    C_ghost = ghost_constant(tuple(lam))

    comparison = _open(
        f"arity-two DS--bar shadow comparison for {lam} in sl_{N}",
        H_MODULAR_GENUS_ONE,
        H_DS_KD_COMPARISON,
        evidence=(
            f"exact affine kappa {kappa_affine}",
            f"exact KRW central charge {c_val}",
            f"exact DS ghost constant {C_ghost}",
        ),
    )

    return {
        'partition': lam,
        'kappa_affine': kappa_affine,
        'ghost_constant': C_ghost,
        'anomaly_ratio': rho,
        'central_charge': c_val,
        'kappa_w': kappa_w,
        'commutation_arity2': comparison,
    }


def shadow_commutation_induction_data(n: int) -> Dict[str, object]:
    """Collect exact depth candidates and typed shadow comparisons."""
    pars = partitions(n)
    results = {}

    for lam in pars:
        depth_candidate = generator_weight_shadow_depth_candidate(lam)
        depth_claim = shadow_depth_estimate(lam)
        arity2 = shadow_kappa_ds_commutation(n, lam)

        label = ''.join(str(p) for p in lam)
        results[label] = {
            'shadow_depth_candidate': depth_candidate,
            'shadow_depth_realization': depth_claim,
            'arity2': arity2['commutation_arity2'],
            'arity3': _open(
                f"arity-three DS--bar shadow comparison for {lam}",
                "an explicit cubic comparison cocycle and gauge homotopy",
            ),
            'arity4': _open(
                f"arity-four DS--bar shadow comparison for {lam}",
                "the quartic resonance and boundary-collision calculation",
            ),
            'full_tower': _open(
                f"all-arity DS--bar shadow comparison for {lam}",
                "compatible comparison maps at every arity",
                "convergence in the completed Maurer--Cartan filtration",
            ),
        }

    finite_depth = sum(
        1
        for lam in pars
        if generator_weight_shadow_depth_candidate(lam) < float('inf')
    )

    return {
        'n': n,
        'total_orbits': len(pars),
        'finite_depth_candidate_count': finite_depth,
        'infinite_depth_candidate_count': len(pars) - finite_depth,
        'orbit_data': results,
        'candidate_feasibility': 'high' if finite_depth == len(pars) else 'medium',
        'bottleneck': 'Infinite shadow obstruction tower requires all-arity induction',
    }


# =====================================================================
# STRATEGY E: Type-by-type exhaustion at small rank
# =====================================================================

@dataclass(frozen=True)
class OrbitRecord:
    """One nilpotent orbit with its DS-bar commutation data."""
    lie_type: str
    rank: int
    label: str  # partition for type A, or B/C/G label
    orbit_dim: int
    centralizer_dim: int
    num_generators: int
    is_even: bool
    is_hook: bool
    transpose_label: str
    orbit_duality: ClaimPacket
    ds_bar_status: ClaimPacket


def type_a_orbit_census(n: int) -> List[OrbitRecord]:
    """Complete orbit census for sl_N."""
    results = []
    for lam in partitions(n):
        lam_t = transpose(lam)
        hook = is_hook(lam)

        status = _ds_bar_claim(n, lam)

        label = ','.join(str(p) for p in lam)
        dual_label = ','.join(str(p) for p in lam_t)
        gen_ws = generator_weights(lam)

        results.append(OrbitRecord(
            lie_type='A',
            rank=n - 1,
            label=f'({label})',
            orbit_dim=nilpotent_orbit_dimension(lam),
            centralizer_dim=centralizer_dimension(lam),
            num_generators=len(gen_ws),
            is_even=is_even_nilpotent(lam),
            is_hook=hook,
            transpose_label=f'({dual_label})',
            orbit_duality=_open(
                f"object-level duality sends the orbit {lam} to {lam_t} in sl_{n}",
                H_TRANSPOSE_DUALITY,
                H_DS_KD_COMPARISON,
            ),
            ds_bar_status=status,
        ))
    return results


def _type_b_orbit_dimension(lam: Partition) -> int:
    """Return the type-B orbit dimension from the orthogonal centralizer formula."""

    size = sum(lam)
    transpose_lam = transpose(lam)
    odd_rows = sum(part % 2 for part in lam)
    centralizer_dim = (sum(column * column for column in transpose_lam) - odd_rows) // 2
    return size * (size - 1) // 2 - centralizer_dim


def _type_c_orbit_dimension(lam: Partition) -> int:
    """Return the type-C orbit dimension from the symplectic centralizer formula."""

    size = sum(lam)
    transpose_lam = transpose(lam)
    odd_rows = sum(part % 2 for part in lam)
    centralizer_dim = (sum(column * column for column in transpose_lam) + odd_rows) // 2
    rank = size // 2
    return rank * (2 * rank + 1) - centralizer_dim


def type_bcd_orbit_data() -> Dict[str, List[Dict[str, object]]]:
    """Exact small-rank B/C partition ledgers and typed DS/bar claims.

    Type B uses even parts of even multiplicity; type C uses odd parts of
    even multiplicity.  The orbit dimensions below follow the standard
    classical centralizer formulas.  Object-level DS/bar and orbit duality
    remain typed obligations.
    """
    data = {}

    # B_2 = so_5 ≅ sp_4 = C_2
    # Partitions of 5 with odd parts having even multiplicity (type B_2):
    # (5), (3,1,1), (2,2,1), (1,1,1,1,1)  -- plus we need to filter
    # Actually for so_5: partitions of 5 with even parts having even mult
    # Type B orbits correspond to partitions of 2n+1 = 5 such that
    # EVEN parts occur with even multiplicity.
    # Partitions of 5: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1^5)
    # Even parts with even mult:
    #   (5): no even parts -> OK
    #   (4,1): 4 appears once (odd mult) -> NO
    #   (3,2): 2 appears once -> NO
    #   (3,1,1): no even parts -> OK
    #   (2,2,1): 2 appears twice -> OK
    #   (2,1,1,1): 2 appears once -> NO
    #   (1^5): no even parts -> OK
    # So B_2 orbits: (5), (3,1,1), (2,2,1), (1^5) = 4 orbits
    b2_names = {
        (5,): 'principal',
        (3, 1, 1): 'subregular',
        (2, 2, 1): 'minimal',
        (1, 1, 1, 1, 1): 'zero',
    }
    data['B_2'] = [
        {
            'partition': lam,
            'orbit': b2_names[lam],
            'dim': _type_b_orbit_dimension(lam),
            'ds_status': 'distinguished' if lam in ((5,), (1, 1, 1, 1, 1)) else 'open',
        }
        for lam in enumerate_type_b_orbits(2)
    ]

    # C_2 = sp_4 ≅ so_5
    # Partitions of 4 with ODD parts having even multiplicity (type C_2):
    # Partitions of 2n=4: (4), (3,1), (2,2), (2,1,1), (1^4)
    # Odd parts with even mult:
    #   (4): no odd parts -> OK
    #   (3,1): 3 appears once, 1 appears once -> NO
    #   (2,2): no odd parts -> OK
    #   (2,1,1): 1 appears twice -> OK
    #   (1^4): 1 appears 4 times -> OK
    # C_2 orbits: (4), (2,2), (2,1,1), (1^4) = 4 orbits
    c2_names = {
        (4,): 'principal',
        (2, 2): 'subregular',
        (2, 1, 1): 'minimal',
        (1, 1, 1, 1): 'zero',
    }
    data['C_2'] = [
        {
            'partition': lam,
            'orbit': c2_names[lam],
            'dim': _type_c_orbit_dimension(lam),
            'ds_status': 'distinguished' if lam in ((4,), (1, 1, 1, 1)) else 'open',
        }
        for lam in enumerate_type_c_orbits(2)
    ]

    # G_2: 5 nilpotent orbits
    # Principal (G_2), subregular (A_1 + tilde{A}_1), short root (tilde{A}_1),
    # long root (A_1), zero
    data['G_2'] = [
        {'partition': None, 'orbit': 'G_2 (principal)', 'dim': 12, 'ds_status': 'distinguished'},
        {'partition': None, 'orbit': 'A_1 + tilde{A}_1 (subregular)', 'dim': 10, 'ds_status': 'open'},
        {'partition': None, 'orbit': 'tilde{A}_1 (short root)', 'dim': 8, 'ds_status': 'open'},
        {'partition': None, 'orbit': 'A_1 (long root)', 'dim': 6, 'ds_status': 'open'},
        {'partition': None, 'orbit': '0 (zero)', 'dim': 0, 'ds_status': 'distinguished'},
    ]

    # B_3 = so_7: partitions of 7 with even parts of even multiplicity
    # Partitions of 7: (7), (5,1,1), (3,3,1), (3,2,2), (3,1,1,1,1),
    #                  (2,2,2,1), (2,2,1,1,1), (1^7)
    # Filter: even parts must appear with even mult
    #   (7): OK
    #   (5,1,1): OK (no even parts)
    #   (3,3,1): OK
    #   (3,2,2): 2 appears twice -> OK
    #   (3,1,1,1,1): OK
    #   (2,2,2,1): 2 appears 3 times -> NO
    #   (2,2,1,1,1): 2 appears twice -> OK
    #   (1^7): OK
    # Full list of partitions of 7:
    # (7), (6,1), (5,2), (5,1,1), (4,3), (4,2,1), (4,1,1,1),
    # (3,3,1), (3,2,2), (3,2,1,1), (3,1^4), (2,2,2,1), (2,2,1,1,1),
    # (2,1^5), (1^7)
    # Filter for B_3 (even parts even mult):
    b3_valid = enumerate_type_b_orbits(3)

    data['B_3'] = [
        {
            'partition': lam,
            'orbit': 'principal' if lam == (7,) else (
                'zero' if lam == (1,) * 7 else 'other'
            ),
            'dim': _type_b_orbit_dimension(lam),
            'ds_status': 'distinguished' if lam in ((7,), tuple([1]*7)) else 'open',
        }
        for lam in b3_valid
    ]

    for family, rows in data.items():
        for row in rows:
            raw_status = row.pop('ds_status')
            if raw_status == 'distinguished':
                packet = _conditional(
                    f"DS--bar commutation for {family} orbit {row['orbit']}",
                    H_DS_KD_COMPARISON,
                    "the principal or zero-orbit specialization in a fixed convention",
                )
            else:
                packet = _open(
                    f"DS--bar commutation for {family} orbit {row['orbit']}",
                    H_DS_KD_COMPARISON,
                    H_BC_DUALITY,
                )
            row['ds_bar_status'] = packet

    return data


def transpose_for_bcd(lam: Partition, N: int) -> Partition:
    """Transpose partition (same as type A transpose)."""
    return transpose(lam)


def type_e_exhaustion_assessment() -> Dict[str, object]:
    """Return finite orbit-count ledgers and the size of the open middle lane.

    Type E_6: 21 nilpotent orbits
    Type E_7: 45 nilpotent orbits
    Type E_8: 70 nilpotent orbits
    Type F_4: 16 nilpotent orbits
    Type G_2: 5 nilpotent orbits

    The two distinguished endpoints are bookkeeping seeds; their DS/bar
    realization retains the comparison hypotheses recorded above.
    """
    return {
        'G_2': {'total': 5, 'distinguished_endpoints': 2, 'open_middle': 3},
        'B_2': {'total': 4, 'distinguished_endpoints': 2, 'open_middle': 2},
        'C_2': {'total': 4, 'distinguished_endpoints': 2, 'open_middle': 2},
        'B_3': {'total': 7, 'distinguished_endpoints': 2, 'open_middle': 5},
        'C_3': {'total': 8, 'distinguished_endpoints': 2, 'open_middle': 6},
        'F_4': {'total': 16, 'distinguished_endpoints': 2, 'open_middle': 14},
        'E_6': {'total': 21, 'distinguished_endpoints': 2, 'open_middle': 19},
        'E_7': {'total': 45, 'distinguished_endpoints': 2, 'open_middle': 43},
        'E_8': {'total': 70, 'distinguished_endpoints': 2, 'open_middle': 68},
    }


# =====================================================================
# OVERALL STRATEGY SCORING
# =====================================================================

@dataclass
class StrategyRating:
    """Editorial triage score; these integers carry no theorem status."""
    name: str
    code: str  # A, B, C, D, E
    feasibility: int  # 1-10
    completeness: int  # 1-10
    novelty: int  # 1-10
    bottleneck: str
    pros: List[str]
    cons: List[str]


def rate_all_strategies() -> List[StrategyRating]:
    """Return explicit editorial priority scores for five research routes."""
    return [
        StrategyRating(
            name='Induction on orbit closure',
            code='A',
            feasibility=7,
            completeness=8,
            novelty=6,
            bottleneck='Induction step: DS-bar for O implies DS-bar for O\' in closure. '
                       'The relative reduction step involves a sub-ghost system that must be '
                       'controlled.',
            pros=[
                'Natural mathematical structure (poset induction)',
                'Starts from distinguished principal and hook audit surfaces',
                'In type A, the finite dominance graph is connected',
                'Each induction step is a relative statement, potentially simpler',
            ],
            cons=[
                'Relative DS step not obviously simpler than the full problem',
                'For non-type-A: the closure order and BV duality are more complex',
                'Induction base in BCD/exceptional types is just principal + zero',
            ],
        ),
        StrategyRating(
            name='BFN Coulomb branch',
            code='B',
            feasibility=5,
            completeness=9,
            novelty=9,
            bottleneck='Need bar-cobar theory for BFN Coulomb branch algebras. '
                       'The BFN construction is Poisson-algebraic; extending to the '
                       'chiral/vertex algebra level is non-trivial.',
            pros=[
                'BFN supplies an independent Poisson-geometric comparison route',
                'Quiver rank data are finite and explicit',
                'A chiral BFN/bar theorem would construct the required comparison map',
                'Quiver varieties organize uniform families across Lie types',
            ],
            cons=[
                'BFN construction gives the ASSOCIATED GRADED, not the vertex algebra',
                'Chiral uplift from BFN is not yet proved in general',
                'Requires substantial new machinery (quiver W-algebras)',
                'May trade one hard problem for another equally hard one',
            ],
        ),
        StrategyRating(
            name='Derived DS = homotopy DS (formality)',
            code='C',
            feasibility=8,
            completeness=9,
            novelty=8,
            bottleneck='Formality of the BRST complex: is derived DS ≃ classical DS? '
                       'The required statement concerns the completed BRST complex and '
                       'its interchange morphism with chiral bar.',
            pros=[
                'Derived categories provide the natural ambient comparison',
                'Affine Slodowy slices furnish a tractable associated-graded input',
                'A source-backed Li theorem would identify the PBW page',
                'The route isolates one chain-level interchange construction',
                'Connects directly to the three-pillar architecture (Pillar A: Ch_inf)',
            ],
            cons=[
                'Need formality of the BRST complex specifically, not just the W-algebra',
                'The BRST complex has ghosts: formality of currents+ghosts is stronger',
                'For non-generic levels: formality can fail (admissible)',
                'Does not directly produce the dual orbit identification',
            ],
        ),
        StrategyRating(
            name='Shadow-level commutation',
            code='D',
            feasibility=7,
            completeness=6,
            novelty=7,
            bottleneck='Infinite shadow obstruction tower for M-class algebras (Virasoro, W_N). '
                       'Arity two requires the genus-one trace comparison; arities three and four '
                       'require explicit cocycles. Full depth needs an all-arity argument.',
            pros=[
                'Exact KRW and ghost ledgers constrain arity two',
                'Cubic and quartic channels can be attacked independently',
                'Generator weights give finite triage bounds in many examples',
                'Directly uses the manuscript\'s shadow obstruction tower machinery',
            ],
            cons=[
                'Does not handle the full chain-level commutation',
                'Principal W-algebras have infinite shadow depth (M class)',
                'Quartic and higher arity steps require new resonance computations',
                'Shadow-level commutation may be weaker than chain-level',
            ],
        ),
        StrategyRating(
            name='Type-by-type exhaustion (small rank)',
            code='E',
            feasibility=9,
            completeness=3,
            novelty=3,
            bottleneck='Only proves the result for finitely many cases. Does not '
                       'establish the general conjecture. Useful for building evidence '
                       'and testing strategies, not for a proof.',
            pros=[
                'Immediately actionable: enumerate and check',
                'Covers all small cases that might reveal obstructions',
                'Computational verification is definitive for each case',
                'Useful benchmark: any strategy must pass these checks',
            ],
            cons=[
                'Finite exhaustion cannot prove an infinite conjecture',
                'Rapidly growing orbit counts: E_8 has 70 orbits',
                'BCD and exceptional types need separate orbit parameterizations',
                'Proves evidence, not a theorem',
            ],
        ),
    ]


def recommended_strategy() -> str:
    """Return a composite audit programme with its proof obligations exposed."""
    return (
        "COMPOSITE AUDIT PROGRAMME: C + A + E, tested through D\n"
        "\n"
        "Step 1 (C): Construct the derived-DS/chiral-bar interchange morphism.\n"
        "Step 2 (C): Prove completed BRST formality from a sourced Li/PBW theorem.\n"
        "Step 3 (A): Realize every chosen closure edge by reduction in stages.\n"
        "Step 4 (E): Maintain exact finite partition, orbit, and KRW ledgers.\n"
        "Step 5 (D): Compute the genus-one, cubic, and quartic comparison classes.\n"
        "\n"
        "Open packages: H_DS-KD^comparison, H_bar-BRST^bicomplex, "
        "H_Kazhdan^formality, H_transport^categorical, H_modular^genus-one.\n"
    )


# =====================================================================
# DIAGNOSTIC RUNNER
# =====================================================================

def run_diagnostics() -> Dict[str, object]:
    """Return exact strategy diagnostics and typed theorem obligations."""
    results: Dict[str, object] = {}

    # Strategy A: closure induction
    for n in [3, 4, 5]:
        score = induction_feasibility_score(n)
        results[f"A: sl_{n} candidate closure covers all orbits"] = score[
            'candidate_closure_covers_all'
        ]
        results[f"A: sl_{n} transport realization"] = score['transport_realization']
        results[f"A: sl_{n} graph connected"] = graph_is_connected(n)

    # Strategy B: exact candidate ranks plus typed BFN identification
    for n in [3, 4, 5]:
        for lam in partitions(n):
            label = ''.join(str(p) for p in lam)
            results[f"B: BFN--Slodowy identification sl_{n} ({label})"] = (
                bfn_coulomb_matches_slodowy(lam)
            )

    # Strategy C: derived DS formality
    for n in [3, 4, 5]:
        score = derived_ds_strategy_score(n)
        results[f"C: sl_{n} affine Slodowy inputs"] = score['all_slodowy_slices_affine']
        results[f"C: sl_{n} derived DS/bar comparison"] = score[
            'derived_ds_bar_comparison'
        ]

    # Strategy D: shadow kappa commutation
    for n in [3, 4]:
        for lam in partitions(n):
            label = ''.join(str(p) for p in lam)
            check = shadow_kappa_ds_commutation(n, lam)
            results[f"D: kappa DS-bar comparison sl_{n} ({label})"] = check[
                'commutation_arity2'
            ]

    # Strategy E: orbit census
    for n in [2, 3, 4, 5]:
        census = type_a_orbit_census(n)
        results[f"E: sl_{n} orbit statuses are typed"] = all(
            isinstance(record.ds_bar_status, ClaimPacket) and record.ds_bar_status.hypotheses
            for record in census
        )

    # Strategy ratings
    ratings = rate_all_strategies()
    for r in ratings:
        results[f"Rating: Strategy {r.code} feasibility >= 5"] = r.feasibility >= 5

    return results
