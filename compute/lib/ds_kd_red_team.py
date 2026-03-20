"""RED TEAM: DS-KD commutation obstruction analysis.

Attack on conj:ds-kd-arbitrary-nilpotent: does bar-cobar/Koszul duality
COMMUTE with Drinfeld-Sokolov reduction for arbitrary nilpotent orbits?

The hook-type corridor in type A is PROVED (thm:hook-transport-corridor).
This module probes where the commutation FAILS or could fail, outside the
proved corridor.

ATTACK AXES:

A. Non-hook nilpotents in type A:
   - sl_4, partition (2,2): the FIRST non-hook case (rectangular)
   - sl_5, partition (3,2): another non-hook
   - sl_6, partitions (3,3) and (2,2,2): multiple non-hooks
   Key probe: does the kappa compatibility still hold? Does the ghost
   constant formula still give a consistent complementarity sum?

B. Derived functor obstruction:
   DS = H^0(BRST) is a derived functor. Bar is also derived. Their
   composition need not commute: there is a spectral sequence
       E_2^{p,q} = H^p_bar(H^q_DS(-)) => H^{p+q}(bar . DS)
   vs the alternate order
       E_2^{p,q} = H^p_DS(H^q_bar(-)) => H^{p+q}(DS . bar)
   If the DS spectral sequence has nonvanishing higher pages, the two
   compositions diverge. The BRST differential d_DS and bar differential
   d_bar satisfy d_DS^2 = 0 and d_bar^2 = 0 separately, but the
   CROSS-DIFFERENTIAL d_DS . d_bar + d_bar . d_DS need not vanish.
   When it does vanish, the bicomplexes give the same total cohomology.
   When it does NOT, the obstruction lives in Ext.

C. Non-special orbits in types B, C, D:
   In type A all orbits are special. In types B, C, D there exist
   non-special orbits. The BV duality is only defined on special orbits.
   For non-special orbits, the Spaltenstein map d: O -> O^sp is a many-to-one
   collapse. The KD dual W-algebra target is AMBIGUOUS: different non-special
   orbits collapse to the same special orbit under d, so the inverse image
   is not unique.

D. Level-dependent failures:
   - At critical level k = -h^v: Sugawara is undefined, DS might be degenerate
   - At admissible levels: null vectors in V_k(g) may force null vectors
     in W_k(g,f) that obstruct Koszulness
   - Level shifts: the hook-type proof uses k -> -k-2N; for non-hook
     non-principal, the correct level shift k -> k'(k,f) is UNKNOWN

E. Quadratic ghost obstruction:
   For non-hook nilpotents, the positive-grade nilpotent n_+ may be
   NON-ABELIAN. When [n_+, n_+] != 0, the BRST differential has a
   QUADRATIC ghost term (b-c-c type). This quadratic term is the primary
   structural obstruction to DS-bar commutation: it means the DS complex
   is not a simple Koszul complex but a genuinely nonlinear BRST resolution.

References:
  - conj:ds-kd-arbitrary-nilpotent (w_algebras_deep.tex ~l.1584)
  - thm:hook-transport-corridor (subregular_hook_frontier.tex ~l.226)
  - prop:ds-bar-hook-commutation (subregular_hook_frontier.tex ~l.359)
  - conj:w-orbit-duality (w_algebras.tex ~l.373)
  - rem:bv-orbit-identification (w_algebras_deep.tex ~l.1600)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from sympy import (
    Rational, Symbol, cancel, expand, factor, simplify, sqrt, sympify,
    Matrix, zeros
)

from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    normalize_partition,
    partition_size,
    transpose_partition,
    hook_partition,
    centralizer_dimension_sl_n,
    orbit_dimension_sl_n,
    type_a_bv_dual,
    type_a_orbit_class,
    type_a_partition_sl2_triple,
    ad_h_grade_multiplicities_sl_n,
)
from compute.lib.hook_type_w_duality import (
    ghost_constant,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    krw_central_charge,
    krw_central_charge_data,
    w_algebra_generator_data,
    complementarity_constant,
)
from compute.lib.ds_bar_commutation import (
    dim_sl_n,
    affine_kappa_sl_n,
    affine_central_charge_sl_n,
    ds_nilpotent_plus_dim,
    ds_nilpotent_half_dim,
)


k = Symbol('k')


# =========================================================================
# A. Non-hook nilpotent data
# =========================================================================

# Catalog of non-hook partitions for the red team attack
NON_HOOK_TARGETS: List[Tuple[int, Partition, str]] = [
    (4, (2, 2), "sl_4 even: FIRST non-hook, self-transpose"),
    (5, (3, 2), "sl_5 non-hook: not self-transpose"),
    (6, (3, 3), "sl_6 rectangular: self-transpose"),
    (6, (2, 2, 2), "sl_6 three-row: self-transpose"),
    (6, (4, 2), "sl_6 non-hook two-row: not self-transpose"),
    (6, (3, 2, 1), "sl_6 staircase: non-hook non-rectangular"),
]


@dataclass(frozen=True)
class NonHookProbe:
    """Red-team probe for a non-hook nilpotent orbit."""

    N: int
    partition: Partition
    transpose: Partition
    is_self_transpose: bool
    orbit_class: str
    # DS data
    centralizer_dim: int
    orbit_dim: int
    ghost_constant: Rational
    n_plus_dim: int
    n_half_dim: int
    # Kappa data
    kappa_w: object  # kappa(W_k(sl_N, f_lambda))
    kappa_dual_w: object  # kappa(W_{k'}(sl_N, f_{lambda^t}))
    complementarity_sum: object  # kappa + kappa_dual (should be constant in k)
    complementarity_is_constant: bool
    # BRST structure
    nilpotent_plus_is_abelian: bool
    has_quadratic_ghost: bool
    # Diagnosis
    diagnosis: str


def probe_non_hook(N: int, partition: Partition, level=Symbol('k')) -> NonHookProbe:
    """Full probe of a non-hook nilpotent orbit in sl_N."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    is_self_t = (lam == lam_t)

    # Basic orbit data
    cent_dim = centralizer_dimension_sl_n(lam)
    orb_dim = orbit_dimension_sl_n(lam)
    C_lam = ghost_constant(lam)
    n_plus = ds_nilpotent_plus_dim(lam)
    n_half = ds_nilpotent_half_dim(lam)
    orb_class = type_a_orbit_class(lam)

    # Kappa for W_k(sl_N, f_lambda)
    kappa_w = ds_kappa_from_affine(lam, level)

    # Kappa for the putative dual: W_{-k-2N}(sl_N, f_{lambda^t})
    kv = hook_dual_level_sl_n(N, level)
    kappa_dual_w = ds_kappa_from_affine(lam_t, kv)

    # Complementarity sum
    comp_sum = simplify(kappa_w + kappa_dual_w)
    # Check if the sum is constant in k (no k-dependence)
    comp_is_const = (simplify(comp_sum.diff(sympify(level))) == 0
                     if hasattr(comp_sum, 'diff') else True)

    # BRST structure: is n_+ abelian?
    # For hook partitions (m, 1^r), n_+ is abelian.
    # For non-hook partitions, n_+ may be non-abelian.
    # Check: if the sl_2-grading has positive-grade pieces g_j with j >= 2,
    # then [g_1, g_1] can land in g_2, making n_+ non-abelian.
    triple = type_a_partition_sl2_triple(lam)
    h_diag = [triple.h[i, i] for i in range(N)]
    grading = ad_h_grade_multiplicities_sl_n(triple.h)

    # n_+ is abelian iff there are no positive grades j, k with j+k
    # also a positive grade. This means [g_j, g_k] cannot land in n_+.
    positive_grades = {g: m for g, m in grading.items() if g > 0}
    max_positive_grade = max(positive_grades.keys()) if positive_grades else 0
    pos_grade_set = set(positive_grades.keys())

    # Check for commutator landings within n_+
    has_internal_bracket = False
    for j in pos_grade_set:
        for l in pos_grade_set:
            if (j + l) in pos_grade_set:
                has_internal_bracket = True
                break
        if has_internal_bracket:
            break

    n_plus_abelian = not has_internal_bracket

    # Quadratic ghost term present iff n_+ non-abelian
    has_quad_ghost = not n_plus_abelian

    # Diagnosis
    if n_plus_abelian:
        if len(pos_grade_set) == 1:
            diagnosis = (f"n_+ abelian (single grade {max_positive_grade}): "
                         f"DS is Koszul-type, bar commutation plausible")
        else:
            diagnosis = (f"n_+ abelian (grades {sorted(pos_grade_set)}, no internal brackets): "
                         f"DS is Koszul-type, bar commutation plausible")
    else:
        diagnosis = (f"n_+ NON-ABELIAN (grades {sorted(pos_grade_set)}, "
                     f"internal brackets present): "
                     f"BRST has quadratic ghost term, bar commutation OBSTRUCTED")

    return NonHookProbe(
        N=N,
        partition=lam,
        transpose=lam_t,
        is_self_transpose=is_self_t,
        orbit_class=orb_class,
        centralizer_dim=cent_dim,
        orbit_dim=orb_dim,
        ghost_constant=C_lam,
        n_plus_dim=n_plus,
        n_half_dim=n_half,
        kappa_w=kappa_w,
        kappa_dual_w=kappa_dual_w,
        complementarity_sum=comp_sum,
        complementarity_is_constant=comp_is_const,
        nilpotent_plus_is_abelian=n_plus_abelian,
        has_quadratic_ghost=has_quad_ghost,
        diagnosis=diagnosis,
    )


def probe_all_non_hooks() -> Dict[str, NonHookProbe]:
    """Probe all non-hook targets."""
    results = {}
    for N, lam, desc in NON_HOOK_TARGETS:
        key = f"sl_{N}_{lam}"
        results[key] = probe_non_hook(N, lam)
    return results


# =========================================================================
# B. Derived-functor obstruction: spectral sequence analysis
# =========================================================================

@dataclass(frozen=True)
class SpectralSequenceObstruction:
    """Obstruction data from the DS-bar spectral sequence."""

    partition: Partition
    N: int
    # DS spectral sequence data
    # E_2^{0,0} = H^0_DS(H^0_bar(-)) -- the "commuting" term
    # E_2^{p,q} with (p,q) != (0,0) -- the obstruction terms
    ds_complex_dim: int  # dim of the BRST complex
    bar_complex_dim: int  # dim of the bar complex (in low degrees)
    # Key obstruction: does H^1_DS survive?
    # If W_k(g,f) has H^1(BRST) != 0 (which happens at special levels),
    # the DS reduction is not exact and the spectral sequence has higher terms
    h1_ds_survives_at_generic_level: bool
    # Obstruction class location
    obstruction_bidegree: Optional[Tuple[int, int]]
    obstruction_description: str


def spectral_sequence_probe(N: int, partition: Partition) -> SpectralSequenceObstruction:
    """Analyze the DS-bar spectral sequence obstruction.

    The key mathematical fact: DS reduction is EXACT at generic level
    (the BRST spectral sequence degenerates at E_1 by the Kazhdan
    filtration argument), so at generic k the two compositions agree.

    The obstruction appears at SPECIAL levels:
    - Critical: k = -h^v (DS is undefined)
    - Admissible: k = -h^v + p/q with p, q coprime, q >= h^v
      At admissible levels, DS may have higher BRST cohomology.
    - Boundary of admissibility: where the Kazhdan filtration fails
    """
    lam = normalize_partition(partition)

    # DS complex dimension = dim(n_+) (fermionic ghosts)
    # + dim(n_-) (anti-ghosts) in the full BRST complex
    n_plus = ds_nilpotent_plus_dim(lam)

    # Bar complex: at generic level, H^1(B(W)) = generators of W
    cent_dim = centralizer_dimension_sl_n(lam)

    # At generic level, DS is exact: E_1 degenerates, no obstruction
    h1_survives_generic = False

    # The obstruction is concentrated at special levels
    # For non-hook partitions, the BRST differential has a quadratic ghost
    # term that makes the spectral sequence DIFFERENT from the hook case.
    # Even at generic level, the bicomplexity of bar + BRST introduces
    # potential cross-term contributions.
    triple = type_a_partition_sl2_triple(lam)
    grading = ad_h_grade_multiplicities_sl_n(triple.h)
    positive_grades = {g: m for g, m in grading.items() if g > 0}
    max_pos = max(positive_grades.keys()) if positive_grades else 0
    pos_set = set(positive_grades.keys())

    # n_+ is abelian iff no two positive grades sum to another positive grade
    has_bracket = any((j + l) in pos_set for j in pos_set for l in pos_set)

    if not has_bracket:
        # Abelian n_+: DS is Koszul-type, spectral sequence collapses
        obstr_bideg = None
        obstr_desc = (f"n_+ abelian (positive grades {sorted(pos_set)}), "
                      f"spectral sequence collapses at E_1")
    elif len(pos_set) == 2:
        # Two positive grades with internal bracket: E_2 obstruction
        obstr_bideg = (1, 1)
        obstr_desc = (f"n_+ non-abelian (grades {sorted(pos_set)}, "
                      f"internal brackets): "
                      f"quadratic ghost gives E_2 obstruction at bidegree (1,1). "
                      f"The cross-differential d_bar . d_DS may be nonzero.")
    else:
        # Multiple interacting grades: higher obstruction
        obstr_bideg = (2, 1)
        obstr_desc = (f"n_+ deeply non-abelian (grades {sorted(pos_set)}): "
                      f"multiple ghost interactions, higher-order obstruction.")

    return SpectralSequenceObstruction(
        partition=lam,
        N=N,
        ds_complex_dim=2 * n_plus,  # ghosts + anti-ghosts
        bar_complex_dim=cent_dim,
        h1_ds_survives_at_generic_level=h1_survives_generic,
        obstruction_bidegree=obstr_bideg,
        obstruction_description=obstr_desc,
    )


# =========================================================================
# C. Non-special orbits in types B, C, D
# =========================================================================

@dataclass(frozen=True)
class TypeBCDOrbit:
    """Orbit data in type B, C, or D."""

    lie_type: str
    rank: int
    partition: Partition
    is_valid_bc_partition: bool
    is_special: bool
    spaltenstein_image: Optional[Partition]
    orbit_dim: Optional[int]
    centralizer_dim: Optional[int]
    bv_dual_exists: bool
    diagnosis: str


def is_valid_type_b_partition(partition: Partition) -> bool:
    """Check if partition is a valid type B_n orbit label.

    In type B_n = so_{2n+1}, nilpotent orbits correspond to partitions
    of 2n+1 where EVEN parts occur with EVEN multiplicity.
    """
    lam = normalize_partition(partition)
    from collections import Counter
    counts = Counter(lam)
    for part, mult in counts.items():
        if part % 2 == 0 and mult % 2 != 0:
            return False
    return True


def is_valid_type_c_partition(partition: Partition) -> bool:
    """Check if partition is a valid type C_n orbit label.

    In type C_n = sp_{2n}, nilpotent orbits correspond to partitions
    of 2n where ODD parts occur with EVEN multiplicity.
    """
    lam = normalize_partition(partition)
    from collections import Counter
    counts = Counter(lam)
    for part, mult in counts.items():
        if part % 2 == 1 and mult % 2 != 0:
            return False
    return True


def is_valid_type_d_partition(partition: Partition) -> bool:
    """Check if partition is a valid type D_n orbit label.

    In type D_n = so_{2n}, nilpotent orbits correspond to partitions
    of 2n where EVEN parts occur with EVEN multiplicity.
    (Note: very even partitions give TWO orbits, but we ignore that here.)
    """
    lam = normalize_partition(partition)
    from collections import Counter
    counts = Counter(lam)
    for part, mult in counts.items():
        if part % 2 == 0 and mult % 2 != 0:
            return False
    return True


def is_special_type_b_orbit(partition: Partition) -> bool:
    """Check if a type B_n orbit is special.

    A type-B orbit (partition of 2n+1 with even parts even mult) is
    SPECIAL iff in the sequence of parts, there is no "gap" where an
    even part appears between two distinct odd parts.

    Explicit criterion (Collingwood-McGovern, Thm 6.3.7):
    A B-partition lambda is special iff for every even part p of lambda,
    the multiplicity of p equals the multiplicity of p in the
    B-collapse of the transpose of lambda.

    For small ranks we can verify directly against the known classification.

    B_2 = so_5 orbits and specialness:
      (5)           -> regular, SPECIAL
      (3,1,1)       -> subregular, SPECIAL
      (2,2,1)       -> minimal non-zero, NON-SPECIAL
      (1,1,1,1,1)   -> zero, SPECIAL

    B_3 = so_7 orbits and specialness:
      (7)           -> SPECIAL (regular)
      (5,1,1)       -> SPECIAL
      (3,3,1)       -> SPECIAL
      (3,2,2)       -> NON-SPECIAL
      (3,1,1,1,1)   -> SPECIAL
      (2,2,2,1)     -> NON-SPECIAL
      (1,1,1,1,1,1,1) -> SPECIAL (zero)
    """
    lam = normalize_partition(partition)

    # Direct method: compute the Barbasch-Vogan/Spaltenstein double dual
    # and check if it gives back the original.
    # d_BV(lambda) = B-collapse of transpose(lambda)
    # lambda is special iff d_BV(d_BV^{-1}) = lambda, which for type B
    # is equivalent to: B-collapse(transpose(C-collapse(transpose(lambda)))) = lambda
    #
    # But we need to be careful: transpose of a B-partition lands in
    # a different type. For B <-> C duality:
    # transpose of a B-partition gives a C-partition (possibly after collapse).

    # Direct check for type B: a B-partition is special iff each even row
    # appears with even multiplicity (which is already required for B-validity)
    # AND additionally, when we look at the sequence of multiplicities,
    # the pattern matches the Spaltenstein criterion.

    # Simplest correct approach: use the round-trip criterion.
    # Step 1: transpose lambda, get a partition (possibly not C-valid)
    # Step 2: C-collapse to get a valid C-partition mu
    # Step 3: transpose mu, get a partition (possibly not B-valid)
    # Step 4: B-collapse to get a valid B-partition nu
    # lambda is special iff nu == lambda

    lam_t = transpose_partition(lam)
    mu = c_collapse(lam_t)       # Valid C-partition
    mu_t = transpose_partition(mu)
    nu = b_collapse(mu_t)        # Valid B-partition
    return normalize_partition(nu) == lam


def b_collapse(partition: Partition) -> Partition:
    """B-collapse: largest type-B partition dominated by input.

    Type B_n: partitions of 2n+1 with even parts having even multiplicity.

    Algorithm (Collingwood-McGovern, Nilpotent Orbits, Thm 6.3.3):
    Given a partition mu, produce the B-collapse mu_B by iterating:
      1. Find the largest even part p with odd multiplicity.
      2. Find the largest i such that mu_i = p. Set mu_i = p-1.
      3. Find the smallest j > i such that mu_j < mu_{j-1} (or j = end).
         Set mu_j = mu_j + 1. (This redistributes the lost 1.)
      4. Re-sort into nonincreasing order and repeat.

    Terminates because each step strictly decreases in dominance order.
    """
    lam = list(normalize_partition(partition))
    n = len(lam)
    max_iters = sum(lam) * 10  # Safety bound
    iters = 0
    while iters < max_iters:
        iters += 1
        from collections import Counter
        counts = Counter(lam)
        # Find largest even part with odd multiplicity
        violating = None
        for part in sorted(counts.keys(), reverse=True):
            if part > 0 and part % 2 == 0 and counts[part] % 2 != 0:
                violating = part
                break
        if violating is None:
            break  # Already a valid B-partition

        # Find the LAST occurrence of this part
        last_idx = len(lam) - 1 - lam[::-1].index(violating)
        lam[last_idx] -= 1

        # Find the first position after last_idx where we can add 1
        # i.e., smallest j > last_idx such that lam[j] < lam[j-1]
        # or j = len(lam) (append a new part)
        placed = False
        for j in range(last_idx + 1, len(lam)):
            if lam[j] < lam[j - 1]:
                lam[j] += 1
                placed = True
                break
        if not placed:
            lam.append(1)

        lam = sorted([x for x in lam if x > 0], reverse=True)
    return tuple(lam) if lam else (0,)


def c_collapse(partition: Partition) -> Partition:
    """C-collapse: largest type-C partition dominated by input.

    Type C_n: partitions of 2n with odd parts having even multiplicity.

    Same algorithm as B-collapse but targeting odd parts instead of even.
    """
    lam = list(normalize_partition(partition))
    max_iters = sum(lam) * 10
    iters = 0
    while iters < max_iters:
        iters += 1
        from collections import Counter
        counts = Counter(lam)
        violating = None
        for part in sorted(counts.keys(), reverse=True):
            if part > 0 and part % 2 == 1 and counts[part] % 2 != 0:
                violating = part
                break
        if violating is None:
            break

        last_idx = len(lam) - 1 - lam[::-1].index(violating)
        lam[last_idx] -= 1

        placed = False
        for j in range(last_idx + 1, len(lam)):
            if lam[j] < lam[j - 1]:
                lam[j] += 1
                placed = True
                break
        if not placed:
            lam.append(1)

        lam = sorted([x for x in lam if x > 0], reverse=True)
    return tuple(lam) if lam else (0,)


def enumerate_type_b_orbits(n: int) -> List[Partition]:
    """All nilpotent orbits in B_n = so_{2n+1}.

    These are partitions of 2n+1 with even parts having even multiplicity.
    """
    target = 2 * n + 1
    return [p for p in _all_partitions(target) if is_valid_type_b_partition(p)]


def enumerate_type_c_orbits(n: int) -> List[Partition]:
    """All nilpotent orbits in C_n = sp_{2n}.

    These are partitions of 2n with odd parts having even multiplicity.
    """
    target = 2 * n
    return [p for p in _all_partitions(target) if is_valid_type_c_partition(p)]


def _all_partitions(n: int) -> List[Partition]:
    """All partitions of n (for small n only)."""
    if n == 0:
        return [()]
    result = []
    _partition_helper(n, n, [], result)
    return result


def _partition_helper(n: int, max_part: int, current: list, result: list):
    if n == 0:
        result.append(tuple(current))
        return
    for p in range(min(n, max_part), 0, -1):
        _partition_helper(n - p, p, current + [p], result)


def analyze_type_b2_orbits() -> Dict[str, TypeBCDOrbit]:
    """Full orbit analysis for B_2 = so_5 = sp_4 (= C_2).

    B_2 orbits (partitions of 5, even parts even mult):
      (5)       = regular
      (3,1,1)   = subregular
      (2,2,1)   = minimal (NON-SPECIAL in type B)
      (1,1,1,1,1) = zero

    C_2 orbits (partitions of 4, odd parts even mult):
      (4)       = regular
      (2,2)     = subregular (also the minimal non-zero)
      (2,1,1)   = NON-VALID for C_2 (odd part 1 has mult 2... wait, (2,1,1): 1 appears twice = even, valid)
      Actually: partitions of 4 with odd-mult-even:
      (4): no odd parts -> valid
      (3,1): odd parts 3 (mult 1) and 1 (mult 1) -> both odd mult -> INVALID
      (2,2): no odd parts -> valid
      (2,1,1): odd part 1, mult 2 (even) -> valid
      (1,1,1,1): odd part 1, mult 4 (even) -> valid

    So C_2 orbits: (4), (2,2), (2,1,1), (1,1,1,1).

    KEY FINDING: B_2 = C_2 as Lie algebras (so_5 = sp_4), but the orbit
    parametrizations are DIFFERENT. The BV duality map between B_2 and C_2
    orbits is:
      B_2 (5) <-> C_2 (4)      [regular <-> regular]
      B_2 (3,1,1) <-> C_2 (2,2)  [subregular <-> subregular]
      B_2 (2,2,1) <-> ???        [NON-SPECIAL, BV dual problematic]
      B_2 (1,1,1,1,1) <-> C_2 (1,1,1,1)  [zero <-> zero]
    """
    results = {}

    b2_orbits = enumerate_type_b_orbits(2)
    for lam in b2_orbits:
        is_spec = is_special_type_b_orbit(lam)
        spalt = b_collapse(transpose_partition(lam)) if is_spec else None
        results[f"B2_{lam}"] = TypeBCDOrbit(
            lie_type="B",
            rank=2,
            partition=lam,
            is_valid_bc_partition=True,
            is_special=is_spec,
            spaltenstein_image=spalt,
            orbit_dim=None,  # Would need so_5 orbit dim formula
            centralizer_dim=None,
            bv_dual_exists=is_spec,
            diagnosis=("SPECIAL: BV dual exists" if is_spec
                       else "NON-SPECIAL: BV dual AMBIGUOUS, DS-KD target unclear"),
        )

    c2_orbits = enumerate_type_c_orbits(2)
    for lam in c2_orbits:
        results[f"C2_{lam}"] = TypeBCDOrbit(
            lie_type="C",
            rank=2,
            partition=lam,
            is_valid_bc_partition=True,
            is_special=True,  # All C_2 orbits are special (small rank)
            spaltenstein_image=c_collapse(transpose_partition(lam)),
            orbit_dim=None,
            centralizer_dim=None,
            bv_dual_exists=True,
            diagnosis="C_2 orbit, all special at this rank",
        )

    return results


# =========================================================================
# D. Level-dependent failure analysis
# =========================================================================

@dataclass(frozen=True)
class LevelDependentFailure:
    """Analysis of DS-KD commutation failure at special levels."""

    partition: Partition
    N: int
    level_type: str
    level_value: object
    # At this level, what happens?
    ds_is_defined: bool
    w_algebra_has_null_vectors: bool
    pbw_koszulness_holds: bool
    kappa_defined: bool
    # Diagnosis
    failure_mode: str


def analyze_critical_level(N: int, partition: Partition) -> LevelDependentFailure:
    """Analyze DS-KD at the critical level k = -h^v = -N for sl_N."""
    lam = normalize_partition(partition)
    kc = -N  # critical level for sl_N

    return LevelDependentFailure(
        partition=lam,
        N=N,
        level_type="critical",
        level_value=kc,
        ds_is_defined=False,  # Sugawara undefined at critical level
        w_algebra_has_null_vectors=True,  # V_{-h^v}(g) is the vacuum module
        pbw_koszulness_holds=False,  # PBW fails at critical level
        kappa_defined=False,  # kappa diverges at k = -h^v
        failure_mode=(
            "FATAL: Sugawara construction undefined at k = -h^v. "
            "DS reduction produces the Feigin-Frenkel center z(g), "
            "not a W-algebra in the usual sense. Bar-cobar/KD is "
            "undefined in the standard framework. The critical-level "
            "W-algebra is a commutative algebra (the center), which is "
            "trivially Koszul but in a degenerate sense."
        ),
    )


def analyze_admissible_level(
    N: int, partition: Partition, p: int, q: int
) -> LevelDependentFailure:
    """Analyze DS-KD at an admissible level k = -N + p/q.

    Admissible levels for sl_N: k + N = p/q with p >= N, q >= 1,
    gcd(p,q) = 1 (boundary admissible levels in the KW sense).

    At admissible levels, V_k(g) has a maximal proper submodule and
    the simple quotient L_k(g) is a VOA with finitely many simple
    modules in category O. The W-algebra W_k(g,f) = DS(L_k(g)) may
    differ from DS(V_k(g)).
    """
    lam = normalize_partition(partition)
    k_val = Rational(-N * q + p, q)  # k = -N + p/q

    # At admissible levels, V_k has null vectors that may propagate to W_k
    # The simple quotient L_k has DIFFERENT bar complex from V_k
    return LevelDependentFailure(
        partition=lam,
        N=N,
        level_type=f"admissible (p={p}, q={q})",
        level_value=k_val,
        ds_is_defined=True,
        w_algebra_has_null_vectors=True,  # Always at admissible levels
        pbw_koszulness_holds=False,  # PBW applies to V_k, not L_k
        kappa_defined=True,
        failure_mode=(
            f"CONDITIONAL: DS(V_k) vs DS(L_k) discrepancy. "
            f"The universal algebra V_k is Koszul (prop:pbw-universality) "
            f"but the simple quotient L_k may fail Koszulness. "
            f"Bar-cobar applied to L_k sees the null vector ideal. "
            f"For non-hook partition {lam}, the null vector structure "
            f"of W_k(sl_{N}, f) at admissible k = {k_val} is UNKNOWN. "
            f"This is a genuine attack vector: the hook-type proof uses "
            f"GENERIC level and does not address simple quotients."
        ),
    )


def analyze_colliding_level(N: int, partition: Partition) -> LevelDependentFailure:
    """Analyze DS-KD at the colliding level k' = k, i.e. 2k + 2N = 0.

    At k = -N, which is the critical level, the dual level k' = -k-2N = k.
    This is the self-dual point, but it coincides with the critical level.
    """
    lam = normalize_partition(partition)
    k_self_dual = -N  # k such that -k-2N = k, i.e. 2k = -2N

    return LevelDependentFailure(
        partition=lam,
        N=N,
        level_type="self-dual/critical collision",
        level_value=k_self_dual,
        ds_is_defined=False,
        w_algebra_has_null_vectors=True,
        pbw_koszulness_holds=False,
        kappa_defined=False,
        failure_mode=(
            f"DEGENERATE: The self-dual level k = -N coincides with "
            f"the critical level. Both bar-cobar and DS are degenerate. "
            f"No KD statement is possible at this level."
        ),
    )


# =========================================================================
# E. Quadratic ghost obstruction: the n_+ abelianity criterion
# =========================================================================

@dataclass(frozen=True)
class GhostObstructionData:
    """Detailed analysis of the quadratic ghost obstruction."""

    partition: Partition
    N: int
    # ad(h) grading data
    grading: Dict[int, int]
    positive_grades: Dict[int, int]
    max_positive_grade: int
    # n_+ structure
    n_plus_dim: int
    n_plus_is_abelian: bool
    # If non-abelian: identify the commutator [g_j, g_k] landing in g_{j+k}
    commutator_landings: List[Tuple[int, int, int]]  # (j, k, j+k)
    # Ghost complex structure
    ghost_central_charge: Rational
    # BRST differential order: 1 (linear) if abelian, 2+ if non-abelian
    brst_differential_order: int
    # Ext obstruction
    ext_group_dimension: Optional[int]
    ext_description: str


def ghost_obstruction_analysis(N: int, partition: Partition) -> GhostObstructionData:
    """Detailed ghost obstruction analysis for DS-bar commutation.

    The KEY obstruction to DS-bar commutation for non-hook nilpotents
    is the non-abelianity of n_+.

    When n_+ is abelian (all hook partitions and some non-hooks like
    the even orbit (2,2) in sl_4), the BRST differential is LINEAR
    in the ghost fields: d_BRST(x) = sum_alpha [J_alpha, x] * c^alpha.
    This is a Koszul-type resolution, and bar commutes with it.

    When n_+ is non-abelian, the BRST differential has a QUADRATIC
    ghost term: d_BRST includes terms of the form
      c^alpha * c^beta * b_gamma  (ghost number +1)
    arising from [n_alpha, n_beta] = n_gamma in n_+.
    This quadratic term means the BRST complex is NOT a simple
    Koszul complex, and bar-cobar commutation requires checking
    the anticommutativity of the two differentials.

    The obstruction class lives in
      Ext^1_{BRST}(H^*(bar), H^*(bar))
    which measures the failure of the natural comparison map
      bar(DS(-)) -> DS(bar(-))
    to be a quasi-isomorphism.
    """
    lam = normalize_partition(partition)
    triple = type_a_partition_sl2_triple(lam)
    grading = ad_h_grade_multiplicities_sl_n(triple.h)
    positive = {g: m for g, m in grading.items() if g > 0}
    max_pos = max(positive.keys()) if positive else 0

    n_plus = ds_nilpotent_plus_dim(lam)

    # n_+ is abelian iff there are no positive grades j, k with j+k
    # also a positive grade (i.e., [g_j, g_k] cannot land in n_+).
    pos_grade_set = set(positive.keys())
    has_internal_bracket = False
    for j in pos_grade_set:
        for l in pos_grade_set:
            if (j + l) in pos_grade_set:
                has_internal_bracket = True
                break
        if has_internal_bracket:
            break
    n_abelian = not has_internal_bracket

    # Identify commutator landings
    comm_landings = []
    if not n_abelian:
        for j in positive:
            for l in positive:
                if j + l in pos_grade_set:
                    comm_landings.append((j, l, j + l))

    # Ghost central charge
    C_lam = ghost_constant(lam)

    # BRST order
    brst_order = 1 if n_abelian else (2 if max_pos <= 2 else max_pos)

    # Ext obstruction estimate
    if n_abelian:
        ext_dim = 0
        ext_desc = "n_+ abelian: Ext^1 = 0, no obstruction"
    else:
        # The obstruction Ext^1 has dimension >= number of commutator relations
        # in n_+, which is dim([n_+, n_+])
        comm_dim = sum(grading.get(j + l, 0) for j, l, jl in comm_landings
                       if jl > 0) if comm_landings else 0
        # But this double-counts, so divide by 2
        ext_dim_est = max(1, comm_dim // 2)
        ext_dim = ext_dim_est
        ext_desc = (
            f"n_+ non-abelian: Ext^1 >= {ext_dim_est} from "
            f"{len(comm_landings)} commutator landings. "
            f"The bar differential and BRST differential "
            f"generate a bicomplex with potential cross-terms "
            f"at BRST order {brst_order}. "
            f"This is the PRIMARY obstruction to DS-bar commutation "
            f"for partition {lam} in sl_{N}."
        )

    return GhostObstructionData(
        partition=lam,
        N=N,
        grading=dict(grading),
        positive_grades=positive,
        max_positive_grade=max_pos,
        n_plus_dim=n_plus,
        n_plus_is_abelian=n_abelian,
        commutator_landings=comm_landings,
        ghost_central_charge=C_lam,
        brst_differential_order=brst_order,
        ext_group_dimension=ext_dim,
        ext_description=ext_desc,
    )


# =========================================================================
# F. Kappa compatibility and complementarity sum for non-hook orbits
# =========================================================================

def complementarity_sum_non_hook(N: int, partition: Partition) -> object:
    """Compute c(k) + c(k') for a non-hook W-algebra.

    For the hook-type corridor, c(k) + c(k') is a constant independent
    of k (the Koszul conductor). If this fails for non-hook orbits,
    the entire duality ansatz k' = -k-2N is WRONG for these orbits.
    """
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    level = Symbol('k')
    kv = hook_dual_level_sl_n(N, level)

    c_direct = krw_central_charge(lam, level)
    c_dual = krw_central_charge(lam_t, kv)

    return simplify(c_direct + c_dual)


def complementarity_sum_is_constant(N: int, partition: Partition) -> Tuple[bool, object]:
    """Check if c(k) + c(k') is constant (independent of k).

    Returns (is_constant, value_or_expression).
    """
    cs = complementarity_sum_non_hook(N, partition)
    level = Symbol('k')
    deriv = simplify(cs.diff(level))
    if deriv == 0:
        # It's constant -- evaluate at k=0
        val = cs.subs(level, 0)
        return True, simplify(val)
    else:
        return False, cs


def kappa_sum_non_hook(N: int, partition: Partition) -> object:
    """Compute kappa(W_k(f)) + kappa(W_{k'}(f^t)) for non-hook orbits."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    level = Symbol('k')
    kv = hook_dual_level_sl_n(N, level)

    kappa_direct = ds_kappa_from_affine(lam, level)
    kappa_dual = ds_kappa_from_affine(lam_t, kv)

    return simplify(kappa_direct + kappa_dual)


def kappa_sum_is_constant(N: int, partition: Partition) -> Tuple[bool, object]:
    """Check if kappa sum is constant."""
    ks = kappa_sum_non_hook(N, partition)
    level = Symbol('k')
    deriv = simplify(ks.diff(level))
    if deriv == 0:
        val = ks.subs(level, 0)
        return True, simplify(val)
    else:
        return False, ks


# =========================================================================
# G. Complete red-team report
# =========================================================================

@dataclass(frozen=True)
class RedTeamVerdict:
    """Summary verdict from the red-team attack."""

    target: str
    partition: Partition
    N: int
    # Checks
    kappa_constant: bool
    complementarity_constant: bool
    n_plus_abelian: bool
    spectral_sequence_collapses: bool
    # Overall
    ds_kd_plausible: bool
    obstruction_severity: str  # "none", "mild", "severe", "fatal"
    summary: str


def full_red_team_report() -> List[RedTeamVerdict]:
    """Run the complete red-team attack battery."""
    verdicts = []

    for N, lam, desc in NON_HOOK_TARGETS:
        probe = probe_non_hook(N, lam)
        ss = spectral_sequence_probe(N, lam)
        ghost = ghost_obstruction_analysis(N, lam)
        kappa_const, kappa_val = kappa_sum_is_constant(N, lam)
        comp_const, comp_val = complementarity_sum_is_constant(N, lam)

        # Determine severity
        # NOTE: complementarity sum c(k)+c(k') being k-dependent is NOT
        # necessarily fatal. The existing hook test test_31_211_k_dependent
        # shows that even for the PROVED hook pair (3,1)/(2,1,1) in sl_4,
        # c(k)+c(k') is k-dependent! The hook proof works via kappa
        # compatibility + generator matching + Sugawara threading, not
        # via central-charge constancy.
        #
        # However, if KAPPA sum is k-dependent, that IS fatal.
        if not kappa_const:
            severity = "fatal"
            plausible = False
            summary = (f"FATAL: kappa sum is k-dependent for {lam}. "
                       f"The ghost constant formula fails.")
        elif ghost.n_plus_is_abelian and kappa_const:
            severity = "none"
            plausible = True
            comp_note = (" Complementarity sum is k-dependent (as for some hooks)."
                         if not comp_const else "")
            summary = (f"CLEAN: n_+ abelian, kappa constant. "
                       f"DS-KD should commute for {lam} as for hooks.{comp_note}")
        elif not ghost.n_plus_is_abelian and kappa_const:
            severity = "mild"
            plausible = True  # Plausible but not proved
            comp_note = (" Complementarity k-dependent." if not comp_const
                         else " Complementarity constant.")
            summary = (f"MILD: n_+ non-abelian (BRST order {ghost.brst_differential_order}), "
                       f"kappa constant.{comp_note} "
                       f"DS-KD plausible via spectral sequence argument, "
                       f"but quadratic ghost term requires verification. "
                       f"Ext obstruction dim >= {ghost.ext_group_dimension}.")
        else:
            severity = "severe"
            plausible = False
            summary = f"SEVERE: multiple obstructions for {lam}."

        verdicts.append(RedTeamVerdict(
            target=desc,
            partition=lam,
            N=N,
            kappa_constant=kappa_const,
            complementarity_constant=comp_const,
            n_plus_abelian=ghost.n_plus_is_abelian,
            spectral_sequence_collapses=(ss.obstruction_bidegree is None),
            ds_kd_plausible=plausible,
            obstruction_severity=severity,
            summary=summary,
        ))

    return verdicts
