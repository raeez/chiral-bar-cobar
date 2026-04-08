r"""Non-principal W-algebra duality beyond hook type.

This engine extends the hook-type corridor (theorem_ds_koszul_hook_engine.py)
to non-hook nilpotent orbits in type A.  The key structural results:

KOSZULNESS (universal):
    W_k(sl_N, f_lambda) is chirally Koszul at generic level k for ALL
    nilpotent orbits lambda of sl_N.  This follows from Arakawa's Kazhdan
    filtration (2005, 2012, 2015): the BRST spectral sequence for the
    Drinfeld-Sokolov reduction collapses at E_2 for ALL nilpotents, not
    just hooks.  The PBW filtration on V_k(sl_N) descends to W_k(sl_N, f)
    via the Kazhdan filtration universally.

    The obstruction beyond hooks is therefore NOT Koszulness.  It is the
    DS-KD INTERTWINING: does DS_{f_{lambda^t}} applied to V_{k'} produce
    the Koszul dual of DS_{f_lambda} applied to V_k?

DS-KD COMMUTATION STATUS:
    - Hook type (all N): PROVED (Fehily 2022, Creutzig-Linshaw-Nakatsuka-Sato 2023)
    - Self-transpose rectangular (e.g. (2,2) in sl_4): PROVED
      (self-duality + c-complementarity c+c' = const)
    - Self-transpose non-rectangular (e.g. (3,2,1) in sl_6): STRONG EVIDENCE
      (c+c' = const, kappa+kappa' = const, but categorical proof OPEN)
    - Non-self-transpose non-hook: OPEN
      (c+c' is k-DEPENDENT for all tested cases)

PARTITION CLASSIFICATION (type A):
    Every partition lambda of N falls into exactly one class:
    (A) Hook: lambda = (N-r, 1^r).  DS-KD PROVED.
    (B) Even rectangular: lambda = (m^s) with ms=N, m=s.  Self-transpose
        iff m=s.  For self-transpose: DS-KD PROVED (by self-duality).
    (C) Non-hook self-transpose: lambda = lambda^t, not hook, not rectangular.
        c+c' = const (verified computationally for N <= 8).  DS-KD CONJECTURAL
        but with strong evidence.
    (D) Non-hook non-self-transpose: lambda != lambda^t, not hook.
        c+c' is k-DEPENDENT.  DS-KD CONJECTURAL.

BRST COMPLEX STRUCTURE:
    For hook type: n_+ is concentrated in a single grade or is abelian.
    For non-hook: n_+ is generically non-abelian with multiple grades.
    This makes the BRST complex more complex but does NOT obstruct PBW
    collapse (Arakawa's theorem is universal).

    The complexity of the BRST complex is measured by:
    - dim(n_+): number of ghost pairs in the BRST complex
    - n_+ grade structure: eigenvalues of ad(x) on n_+
    - n_+ abelianness: whether [n_+, n_+] = 0
    - dim(g_{1/2}): number of fermionic generators of the W-algebra

TRANSPORT FROM HOOKS:
    The reduction graph Gamma_N has vertices = partitions of N and edges =
    proved reduction/inverse-reduction functors.  For N <= 8, the transport
    closure of hooks covers ALL partitions (verified computationally).
    This means every non-hook orbit is reachable from hooks via a sequence
    of proved reduction functors.  However, transport propagation of DS-KD
    commutation requires verifying that each reduction step PRESERVES the
    intertwining -- this is proved for hooks (Fehily) but OPEN for
    non-hook-to-non-hook edges.

References:
    - Arakawa (2005): Representation theory of superconformal algebras...
    - Arakawa (2012): W-algebras at the critical level (Kazhdan filtration)
    - Arakawa (2015): Rationality of W-algebras (associated varieties)
    - Fehily (2022): Inverse Hamiltonian reduction for hook-type
    - Creutzig-Linshaw-Nakatsuka-Sato (2023): Feigin-Semikhatov duality
    - Butson-Nair (2025): Inverse Hamiltonian reduction (geometric, all types)
    - Kac-Roan-Wakimoto (2003): Quantum reduction and DS central charge
    - Manuscript: thm:ds-koszul-obstruction, conj:type-a-transport-to-transpose

Critical pitfalls:
    - c-complementarity (c+c' = const) holds ONLY for self-transpose pairs.
      For non-self-transpose, c+c' is k-dependent.  This is NOT a failure of
      duality; it reflects different anomaly ratios rho(lam) != rho(lam^t).
    - PBW collapse (Koszulness) is UNIVERSAL at generic level.  The obstruction
      to extending DS-KD beyond hooks is the categorical intertwining, not PBW.
    - The reduction graph makes all orbits reachable from hooks, but transport
      propagation requires verifying intertwining at each edge.
    - For non-even nilpotents: half-integer ad(x)-grades produce fermionic
      generators.  The central charge formula is the universal KRW formula.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from sympy import Rational, Symbol, simplify, sympify

from compute.lib.hook_type_w_duality import (
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    krw_central_charge,
    krw_central_charge_data,
    levi_rho_norm_squared,
    rho_shift_norm_squared,
    w_algebra_generator_data,
    weyl_vector_norm_squared_sl_n,
)
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    _partitions_of_n,
    hook_partition,
    is_hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
)
from compute.lib.hook_transport_corridor import ReductionGraph


k_sym = Symbol('k')


# ============================================================================
# 1. Partition classification
# ============================================================================

def is_rectangular(partition: Partition) -> bool:
    """Check if partition is rectangular (all parts equal)."""
    lam = normalize_partition(partition)
    return len(set(lam)) == 1


def is_even_nilpotent(partition: Partition) -> bool:
    """Check if the nilpotent orbit is even.

    A nilpotent in type A with partition (p_1,...,p_r) is even iff all
    parts have the same parity (all odd or all even).  Equivalently,
    all eigenvalues of ad(x) on g are integers.
    """
    lam = normalize_partition(partition)
    parities = set(p % 2 for p in lam)
    return len(parities) <= 1


def partition_orbit_class(partition: Partition) -> str:
    """Classify partition into the four structural classes.

    Returns one of:
        'hook'                     -- class A: (N-r, 1^r)
        'self_transpose_rectangular' -- class B: (m^m), m^2 = N
        'self_transpose_nonhook'   -- class C: lambda = lambda^t, not hook, not rect
        'non_self_transpose_nonhook' -- class D: lambda != lambda^t, not hook
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)

    if is_hook_partition(lam):
        return 'hook'
    if lam == lam_t and is_rectangular(lam):
        return 'self_transpose_rectangular'
    if lam == lam_t:
        return 'self_transpose_nonhook'
    return 'non_self_transpose_nonhook'


def ds_kd_status(partition: Partition) -> str:
    """DS-KD commutation status for this partition.

    Returns:
        'proved_hook'          -- hook type, proved by Fehily-CLNS
        'proved_self_dual_rect' -- self-transpose rectangular, proved by self-duality
        'evidence_self_transpose' -- self-transpose non-hook, c+c' = const (conjectural)
        'open_non_self_transpose' -- non-self-transpose non-hook, c+c' k-dependent (open)
    """
    cls = partition_orbit_class(partition)
    if cls == 'hook':
        return 'proved_hook'
    if cls == 'self_transpose_rectangular':
        return 'proved_self_dual_rect'
    if cls == 'self_transpose_nonhook':
        return 'evidence_self_transpose'
    return 'open_non_self_transpose'


# ============================================================================
# 2. BRST complex structure
# ============================================================================

@dataclass(frozen=True)
class BRSTComplexData:
    """BRST complex structural data for DS reduction at nilpotent f_lambda."""

    partition: Partition
    N: int
    # ad(x) grading on n_+
    n_plus_dim: int
    n_plus_grades: Dict[Rational, int]  # grade -> multiplicity
    n_plus_is_abelian: bool
    # g_{1/2} data (fermionic generators come from here)
    g_half_dim: int
    # Levi data
    levi_parts: Partition  # parts of transpose partition = block sizes of Levi
    levi_dim: int  # dim(g_0) = dim of Levi part of the grading
    # Classification
    is_even: bool
    has_half_integer_grades: bool
    # PBW / Koszulness
    pbw_collapse: bool  # True: Arakawa's Kazhdan filtration gives E2 collapse
    is_koszul: bool  # True at generic level (universal)


def brst_complex_analysis(partition: Partition) -> BRSTComplexData:
    """Analyze the BRST complex for DS reduction at nilpotent f_lambda.

    The BRST complex for the DS reduction of V_k(sl_N) at nilpotent f_lambda
    has ghost pairs indexed by n_+, the positive-grade part of sl_N under
    the ad(x)-grading (x = h/2 from the Jacobson-Morozov triple).

    Arakawa's theorem: the Kazhdan spectral sequence collapses at E_2
    for ALL nilpotent orbits at generic level k.  This gives PBW collapse
    and hence Koszulness for W_k(sl_N, f_lambda) at generic k.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    lam_t = transpose_partition(lam)

    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    x_diag = [Rational(h_diag[i], 2) for i in range(N)]

    # n_+ grade structure
    n_plus_grades: Dict[Rational, int] = {}
    pos_roots: List[Tuple[int, int]] = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ev = x_diag[i] - x_diag[j]
            if ev > 0:
                n_plus_grades[ev] = n_plus_grades.get(ev, 0) + 1
                pos_roots.append((i, j))

    n_dim = sum(n_plus_grades.values())

    # Check if n_+ is abelian: [n_+, n_+] = 0
    # In type A: [E_{ij}, E_{jl}] = E_{il}
    n_abelian = True
    for (i, j1) in pos_roots:
        for (j2, ell) in pos_roots:
            if j1 == j2 and i != ell:
                ev_il = x_diag[i] - x_diag[ell]
                if ev_il > 0:
                    n_abelian = False
                    break
        if not n_abelian:
            break

    # g_{1/2} dimension
    g_half = n_plus_grades.get(Rational(1, 2), 0)

    # Levi data
    cc = krw_central_charge_data(lam)
    levi_dim = cc.dim_g0

    # Even check
    even = is_even_nilpotent(lam)
    has_half = any(g.denominator != 1 for g in n_plus_grades.keys())

    return BRSTComplexData(
        partition=lam,
        N=N,
        n_plus_dim=n_dim,
        n_plus_grades=dict(sorted(n_plus_grades.items())),
        n_plus_is_abelian=n_abelian,
        g_half_dim=g_half,
        levi_parts=lam_t,
        levi_dim=levi_dim,
        is_even=even,
        has_half_integer_grades=has_half,
        pbw_collapse=True,   # Arakawa: universal at generic level
        is_koszul=True,       # Consequence of PBW collapse
    )


# ============================================================================
# 3. c-complementarity and kappa analysis
# ============================================================================

@dataclass(frozen=True)
class ComplementarityData:
    """c-complementarity and kappa data for a partition pair."""

    partition: Partition
    transpose: Partition
    N: int
    is_self_transpose: bool
    orbit_class: str
    ds_kd_status: str
    # Central charge
    c_source: object   # c(k, lambda) symbolic
    c_dual: object     # c(k', lambda^t) symbolic
    c_sum: object      # c + c'
    c_sum_k_independent: bool
    c_sum_value: object  # the constant (if k-independent) or the expression
    # Kappa
    kappa_source: object
    kappa_dual: object
    kappa_sum: object
    kappa_sum_k_independent: bool
    kappa_sum_value: object
    # Anomaly ratios
    rho_source: Rational
    rho_dual: Rational
    rho_match: bool
    # Self-dual point (for self-transpose only)
    self_dual_c: object  # c* = C/2 where C = c+c'
    # Generator data
    source_n_generators: int
    dual_n_generators: int
    source_n_fermionic: int
    dual_n_fermionic: int


def complementarity_analysis(
    partition: Partition, level=Symbol('k')
) -> ComplementarityData:
    """Full complementarity analysis for partition and its transpose."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    kvar = sympify(level)
    kv = hook_dual_level_sl_n(N, kvar)
    self_t = (lam == lam_t)

    cls = partition_orbit_class(lam)
    status = ds_kd_status(lam)

    # Central charge
    c_s = krw_central_charge(lam, kvar)
    c_d = krw_central_charge(lam_t, kv)
    c_sum = simplify(c_s + c_d)
    dc_dk = simplify(c_sum.diff(kvar))
    c_indep = dc_dk == 0
    c_val = c_sum if not c_indep else simplify(c_sum)

    # Kappa
    kappa_s = ds_kappa_from_affine(lam, kvar)
    kappa_d = ds_kappa_from_affine(lam_t, kv)
    kappa_sum = simplify(kappa_s + kappa_d)
    dk_dk = simplify(kappa_sum.diff(kvar))
    k_indep = dk_dk == 0
    k_val = kappa_sum if not k_indep else simplify(kappa_sum)

    # Anomaly ratios
    rho_s = anomaly_ratio_from_partition(lam)
    rho_d = anomaly_ratio_from_partition(lam_t)

    # Self-dual c
    sd_c = None
    if self_t and c_indep:
        sd_c = simplify(c_val / 2)

    # Generator data
    gen_s = w_algebra_generator_data(lam)
    gen_d = w_algebra_generator_data(lam_t)

    return ComplementarityData(
        partition=lam,
        transpose=lam_t,
        N=N,
        is_self_transpose=self_t,
        orbit_class=cls,
        ds_kd_status=status,
        c_source=c_s,
        c_dual=c_d,
        c_sum=c_sum,
        c_sum_k_independent=c_indep,
        c_sum_value=c_val,
        kappa_source=kappa_s,
        kappa_dual=kappa_d,
        kappa_sum=kappa_sum,
        kappa_sum_k_independent=k_indep,
        kappa_sum_value=k_val,
        rho_source=rho_s,
        rho_dual=rho_d,
        rho_match=(rho_s == rho_d),
        self_dual_c=sd_c,
        source_n_generators=len(gen_s.strong_generators),
        dual_n_generators=len(gen_d.strong_generators),
        source_n_fermionic=gen_s.n_fermionic,
        dual_n_fermionic=gen_d.n_fermionic,
    )


# ============================================================================
# 4. Shadow depth analysis for non-hook W-algebras
# ============================================================================

@dataclass(frozen=True)
class ShadowDepthData:
    """Shadow depth classification for W_k(sl_N, f_lambda)."""

    partition: Partition
    N: int
    orbit_class: str
    # Generator content
    generator_weights: Tuple[Rational, ...]
    n_bosonic: int
    n_fermionic: int
    max_bosonic_weight: Rational
    # Anomaly ratio and kappa
    rho: Rational
    kappa_expr: object  # symbolic in k
    # Shadow classification (on the T-line)
    # G = Gaussian (r_max=2), L = Lie (r_max=3), C = contact (r_max=4), M = mixed (r_max=inf)
    shadow_class: str
    shadow_depth_bound: object  # int or 'infinity'
    # Multi-line structure
    has_weight_1_generators: bool
    n_weight_1: int
    has_fermionic_generators: bool
    has_weight_ge_3: bool


def shadow_depth_analysis(partition: Partition) -> ShadowDepthData:
    """Classify the shadow depth of W_k(sl_N, f_lambda).

    The shadow depth classification (G/L/C/M) is determined by the strong
    generator content.  The key discriminant is whether the shadow metric
    Q_L on the T-line (Virasoro direction) has vanishing critical discriminant
    Delta = 8*kappa*S_4.

    For non-hook W-algebras: the generator content is richer (more lines),
    and the shadow structure is generically class M (infinite depth) because
    the Virasoro subalgebra is always present with weight-2 generator.
    """
    lam = normalize_partition(partition)
    N = partition_size(lam)
    cls = partition_orbit_class(lam)

    gen = w_algebra_generator_data(lam)
    weights = tuple(sorted(Rational(w) for (_, w, _) in gen.strong_generators))
    bosonic_weights = [Rational(w) for (_, w, p) in gen.strong_generators if p == 'bosonic']
    fermionic_weights = [Rational(w) for (_, w, p) in gen.strong_generators if p == 'fermionic']

    max_bos = max(bosonic_weights) if bosonic_weights else Rational(0)
    rho = anomaly_ratio_from_partition(lam)
    kappa = ds_kappa_from_affine(lam, k_sym)

    n_w1 = sum(1 for w in bosonic_weights if w == Rational(1))
    has_w1 = n_w1 > 0
    has_ferm = gen.n_fermionic > 0
    has_w3 = any(w >= Rational(3) for w in bosonic_weights)

    # Shadow depth classification on the T-line:
    # - Single weight-1 generator with no higher: class G (Heisenberg-like)
    # - Multiple weight-1 generators only: class L (affine-like)
    # - Weight-2 present (Virasoro direction): class M (infinite depth)
    #   UNLESS it terminates (very special: only for Heisenberg at kappa=0)
    # The presence of a weight-2 generator (the Virasoro) generically forces
    # class M on the T-line.
    if gen.f_centralizer_dimension == 1:
        w = bosonic_weights[0] if bosonic_weights else Rational(0)
        if w == Rational(1):
            shadow_class = 'G'
            depth = 2
        elif w == Rational(2):
            shadow_class = 'M'
            depth = 'infinity'
        else:
            shadow_class = 'M'
            depth = 'infinity'
    elif all(w == Rational(1) for w in bosonic_weights) and not has_ferm:
        shadow_class = 'L'
        depth = 3
    elif max_bos == Rational(2) and not has_w3 and not has_ferm:
        # Only weight 1 and 2 bosonic generators
        if n_w1 == 0:
            shadow_class = 'M'
            depth = 'infinity'
        else:
            # Mixed weight-1 and weight-2: class C or M depending on contact
            shadow_class = 'C'
            depth = 4
    else:
        shadow_class = 'M'
        depth = 'infinity'

    return ShadowDepthData(
        partition=lam,
        N=N,
        orbit_class=cls,
        generator_weights=weights,
        n_bosonic=gen.n_bosonic,
        n_fermionic=gen.n_fermionic,
        max_bosonic_weight=max_bos,
        rho=rho,
        kappa_expr=kappa,
        shadow_class=shadow_class,
        shadow_depth_bound=depth,
        has_weight_1_generators=has_w1,
        n_weight_1=n_w1,
        has_fermionic_generators=has_ferm,
        has_weight_ge_3=has_w3,
    )


# ============================================================================
# 5. Transport graph analysis
# ============================================================================

@dataclass(frozen=True)
class TransportAnalysis:
    """Transport reachability analysis for non-hook partitions."""

    N: int
    total_partitions: int
    n_hook: int
    n_non_hook: int
    hook_closure_size: int
    all_reachable: bool
    unreachable: Tuple[Partition, ...]
    # Per-partition data
    partition_data: Dict[Partition, Dict[str, Any]]


def transport_reachability(N: int) -> TransportAnalysis:
    """Analyze transport reachability from hooks for sl_N.

    Builds the reduction graph and checks whether all partitions of N
    are reachable from the hook vertices via sequences of proved
    reduction/inverse-reduction functors.
    """
    G = ReductionGraph.build(N)
    hooks = G.hook_vertices()
    closure = G.transport_closure(hooks)
    all_parts = set(G.vertices)
    unreachable = sorted(all_parts - closure)

    per_partition: Dict[Partition, Dict[str, Any]] = {}
    for lam in sorted(all_parts):
        lam_t = transpose_partition(lam)
        cls = partition_orbit_class(lam)
        status = ds_kd_status(lam)
        in_closure = lam in closure
        is_hook = is_hook_partition(lam)

        # Shortest path from a hook vertex
        dist = -1
        if in_closure and not is_hook:
            from collections import deque
            visited: Dict[Partition, int] = {}
            queue: deque = deque()
            for h in hooks:
                visited[h] = 0
                queue.append(h)
            while queue:
                current = queue.popleft()
                if current == lam:
                    dist = visited[current]
                    break
                for neighbor in G.neighbors(current):
                    if neighbor not in visited:
                        visited[neighbor] = visited[current] + 1
                        queue.append(neighbor)
        elif is_hook:
            dist = 0

        per_partition[lam] = {
            'partition': lam,
            'transpose': lam_t,
            'is_hook': is_hook,
            'orbit_class': cls,
            'ds_kd_status': status,
            'in_transport_closure': in_closure,
            'distance_from_hooks': dist,
        }

    return TransportAnalysis(
        N=N,
        total_partitions=len(all_parts),
        n_hook=len(hooks),
        n_non_hook=len(all_parts) - len(hooks),
        hook_closure_size=len(closure),
        all_reachable=len(unreachable) == 0,
        unreachable=tuple(unreachable),
        partition_data=per_partition,
    )


# ============================================================================
# 6. Complete non-hook duality profile
# ============================================================================

@dataclass(frozen=True)
class NonHookDualityProfile:
    """Complete duality profile for a non-hook partition."""

    partition: Partition
    transpose: Partition
    N: int
    # Classification
    orbit_class: str
    ds_kd_status: str
    is_self_transpose: bool
    is_even: bool
    is_rectangular: bool
    # BRST
    brst: BRSTComplexData
    # Complementarity
    complementarity: ComplementarityData
    # Shadow
    shadow: ShadowDepthData
    # Transport
    in_transport_closure: bool
    distance_from_hooks: int
    # Verdict
    koszul: bool
    ds_kd_proved: bool
    ds_kd_evidence_level: str  # 'proved', 'strong', 'weak', 'none'


def non_hook_duality_profile(
    partition: Partition, level=Symbol('k')
) -> NonHookDualityProfile:
    """Complete duality analysis for a (possibly non-hook) partition."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)

    cls = partition_orbit_class(lam)
    status = ds_kd_status(lam)
    self_t = (lam == lam_t)
    even = is_even_nilpotent(lam)
    rect = is_rectangular(lam)

    brst = brst_complex_analysis(lam)
    comp = complementarity_analysis(lam, level)
    shadow = shadow_depth_analysis(lam)

    # Transport
    G = ReductionGraph.build(N)
    hooks = G.hook_vertices()
    closure = G.transport_closure(hooks)
    in_closure = lam in closure

    dist = -1
    if in_closure and not is_hook_partition(lam):
        from collections import deque
        visited: Dict[Partition, int] = {}
        queue: deque = deque()
        for h in hooks:
            visited[h] = 0
            queue.append(h)
        while queue:
            current = queue.popleft()
            if current == lam:
                dist = visited[current]
                break
            for neighbor in G.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)
    elif is_hook_partition(lam):
        dist = 0

    # Verdict
    koszul = True  # Arakawa: universal at generic level
    if status == 'proved_hook':
        proved = True
        evidence = 'proved'
    elif status == 'proved_self_dual_rect':
        proved = True
        evidence = 'proved'
    elif status == 'evidence_self_transpose':
        proved = False
        evidence = 'strong'
    else:
        proved = False
        evidence = 'weak' if in_closure else 'none'

    return NonHookDualityProfile(
        partition=lam,
        transpose=lam_t,
        N=N,
        orbit_class=cls,
        ds_kd_status=status,
        is_self_transpose=self_t,
        is_even=even,
        is_rectangular=rect,
        brst=brst,
        complementarity=comp,
        shadow=shadow,
        in_transport_closure=in_closure,
        distance_from_hooks=dist,
        koszul=koszul,
        ds_kd_proved=proved,
        ds_kd_evidence_level=evidence,
    )


# ============================================================================
# 7. Systematic catalog
# ============================================================================

def non_hook_catalog(N: int) -> List[NonHookDualityProfile]:
    """Generate profiles for all non-hook partitions of N."""
    parts = _partitions_of_n(N)
    return [
        non_hook_duality_profile(lam)
        for lam in parts
        if not is_hook_partition(lam)
    ]


def full_catalog(N: int) -> List[NonHookDualityProfile]:
    """Generate profiles for ALL partitions of N."""
    return [non_hook_duality_profile(lam) for lam in _partitions_of_n(N)]


def self_transpose_catalog(max_N: int = 8) -> List[NonHookDualityProfile]:
    """Catalog all self-transpose partitions up to sl_{max_N}."""
    results = []
    for N in range(3, max_N + 1):
        for lam in _partitions_of_n(N):
            if lam == transpose_partition(lam) and not is_hook_partition(lam):
                results.append(non_hook_duality_profile(lam))
    return results


# ============================================================================
# 8. Numerical cross-checks
# ============================================================================

def numerical_c_complementarity(
    partition: Partition, test_levels: Optional[List[int]] = None
) -> Dict[str, Any]:
    """Numerically verify c-complementarity at multiple levels.

    Returns the c+c' values at each test level and whether they are all equal.
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)

    if test_levels is None:
        test_levels = [1, 2, 3, 5, 7, 11, 13, 17]

    values = {}
    for kv in test_levels:
        if kv + N == 0 or (-kv - 2 * N) + N == 0:
            continue
        c_s = krw_central_charge(lam, Rational(kv))
        c_d = krw_central_charge(lam_t, Rational(-kv - 2 * N))
        values[kv] = simplify(c_s + c_d)

    vals_set = set(values.values())
    return {
        'partition': lam,
        'transpose': lam_t,
        'N': N,
        'values': values,
        'all_equal': len(vals_set) <= 1,
        'constant_value': vals_set.pop() if len(vals_set) == 1 else None,
    }


def numerical_kappa_complementarity(
    partition: Partition, test_levels: Optional[List[int]] = None
) -> Dict[str, Any]:
    """Numerically verify kappa-complementarity at multiple levels."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)

    if test_levels is None:
        test_levels = [1, 2, 3, 5, 7, 11, 13, 17]

    values = {}
    for kv in test_levels:
        if kv + N == 0 or (-kv - 2 * N) + N == 0:
            continue
        k_s = ds_kappa_from_affine(lam, Rational(kv))
        k_d = ds_kappa_from_affine(lam_t, Rational(-kv - 2 * N))
        values[kv] = simplify(k_s + k_d)

    vals_set = set(values.values())
    return {
        'partition': lam,
        'transpose': lam_t,
        'N': N,
        'values': values,
        'all_equal': len(vals_set) <= 1,
        'constant_value': vals_set.pop() if len(vals_set) == 1 else None,
    }


# ============================================================================
# 9. The c-complementarity theorem for self-transpose partitions
# ============================================================================

def verify_self_transpose_c_complementarity(max_N: int = 8) -> List[Dict[str, Any]]:
    """Verify that c+c' is k-independent for ALL self-transpose partitions.

    This is a structural theorem: for self-transpose lambda = lambda^t,
    rho(lambda) = rho(lambda^t) (same anomaly ratio on both sides),
    so if c+c' = const then kappa+kappa' = rho*(c+c') = const as well.

    Returns results for each self-transpose partition found.
    """
    results = []
    for N in range(2, max_N + 1):
        for lam in _partitions_of_n(N):
            lam_t = transpose_partition(lam)
            if lam != lam_t:
                continue

            c_s = krw_central_charge(lam, k_sym)
            c_d = krw_central_charge(lam, -k_sym - 2 * N)
            c_sum = simplify(c_s + c_d)
            c_indep = simplify(c_sum.diff(k_sym)) == 0

            rho = anomaly_ratio_from_partition(lam)
            kappa_sum = simplify(rho * c_sum)
            k_indep = simplify(kappa_sum.diff(k_sym)) == 0

            results.append({
                'N': N,
                'partition': lam,
                'is_hook': is_hook_partition(lam),
                'c_sum': c_sum,
                'c_k_independent': c_indep,
                'rho': rho,
                'kappa_sum': kappa_sum,
                'kappa_k_independent': k_indep,
            })
    return results
