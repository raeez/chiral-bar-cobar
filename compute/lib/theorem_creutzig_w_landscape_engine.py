r"""Exact W-algebra arithmetic with typed geometric comparison claims.

The computational lane contains partition transposition, candidate hook
corridors, represented generator-weight ledgers, and source-backed
central-charge formulas.
The geometric lane contains ``rho``, ``kappa``, the modular conductor, full
shadow class and depth, DS--bar transport, object-level Koszul duality, and
KSDual membership.  Every object in the geometric lane is a
:class:`ClaimPacket` whose hypotheses name the missing comparison theorem.

The distinction is structural.  A reciprocal-weight sum is an arithmetic
diagnostic.  Its promotion to ``rho`` requires a genus-one modular trace
calculation.  Rationality and ``C_2``-cofiniteness control the representation
category; chiral Koszulness additionally requires a completed bar comparison.
Likewise, a braided equivalence of module categories reaches the chiral bar
construction only through a named functorial comparison.

The type-A central charges are evaluated by the Kac--Roan--Wakimoto formula
through :mod:`compute.lib.hook_type_w_duality`.  The theorem labelled
``thm:w-algebra-koszul-main`` is conditional on its filtered DS/bar, continuous
Verdier, and genus-one trace package.

Manuscript references:
    thm:w-algebra-koszul-main (w_algebras.tex): principal DS Koszul duality
    conj:w-orbit-duality (w_algebras.tex): general nilpotent Koszul duality
    thm:hook-transport-corridor (w_algebras.tex): hook-type transport
    prop:sl3-nilpotent-shadow-data (w_algebras.tex): sl_3 nilpotent shadows
    prop:sl4-hook-shadow-data (w_algebras.tex): sl_4 hook shadows
    thm:ds-shadow-functor-arity2 (w_algebras.tex): DS shadow commutation
    tab:master-invariants (landscape_census.tex): master invariant table
    tab:shadow-tower-census (landscape_census.tex): shadow tower census
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

from sympy import (
    Float,
    Integer,
    Rational,
    Symbol,
    diff,
    simplify,
    sympify,
)

from compute.lib.hook_type_w_duality import (
    H_HOOK_DS_BAR,
    anomaly_ratio_from_partition,
    ds_kappa_from_affine,
    hook_dual_level_sl_n,
    kappa_complementarity_sum,
    krw_central_charge,
    reciprocal_weight_diagnostic_from_partition,
)
from compute.lib.non_principal_w_bar_engine import ClaimPacket, ClaimStatus
from compute.lib.nonprincipal_ds_orbits import (
    Partition,
    hook_partition,
    normalize_partition,
    partition_size,
    transpose_partition,
)


k_sym = Symbol('k')

MINIMAL_SO_SOURCE = (
    "Creutzig--Fasquel--Kovalchuk--Linshaw--Nakatsuka (2025), "
    "Theorem 1.1 and Corollary 1.2"
)
TYPE_A_STAGES_SOURCE = (
    "Creutzig--Fasquel--Linshaw--Nakatsuka (2025), Conjecture A; "
    "Theorem A (= Theorems 4.1, 4.6, 4.8); Theorem B (= Theorem 2.2)"
)
KL_SOURCE = (
    "Creutzig--Dhillon--Nakatsuka (2026), "
    "Theorem 1.1 (= Theorem 5.2)"
)


def _exact_expression(value: object, parameter: str) -> object:
    """Return an exact SymPy expression and reject inexact input data."""

    if isinstance(value, float):
        raise TypeError(f"{parameter} must be exact; received Python float {value!r}")
    expression = sympify(value)
    if expression.has(Float):
        raise TypeError(f"{parameter} must be exact; received inexact expression {value!r}")
    return expression


def _exact_integer(value: object, parameter: str, minimum: int) -> int:
    """Return an exact integer in the stated domain."""

    if isinstance(value, bool) or not isinstance(value, (int, Integer)):
        raise TypeError(f"{parameter} must be an exact integer, received {value!r}")
    integer = int(value)
    if integer < minimum:
        raise ValueError(f"{parameter} must be at least {minimum}, received {integer}")
    return integer


def _proved_elsewhere_claim(
    statement: str,
    value: object,
    *evidence: str,
) -> ClaimPacket:
    """Return a source-backed claim whose value lies in the cited theorem."""

    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.PROVED_ELSEWHERE,
        value=value,
        evidence=tuple(evidence),
    )


def _has_precise_result_reference(reference: Optional[str]) -> bool:
    """Recognize an author--year reference carrying a numbered result."""

    if not reference or not any(str(year) in reference for year in range(1900, 2101)):
        return False
    return any(
        marker in reference
        for marker in ("Theorem ", "Proposition ", "Corollary ", "Lemma ")
    )


def _is_simple_simply_laced_type(lie_type: str, rank: int) -> bool:
    """Recognize the ADE source notation accepted by the KL constructor."""

    family = lie_type.strip().upper()
    if family == "SL":
        return rank >= 2
    if family == "A":
        return rank >= 1
    if family == "D":
        return rank >= 4
    if family == "E":
        return rank in {6, 7, 8}
    return False


def _open_claim(statement: str, *hypotheses: str) -> ClaimPacket:
    """Return an unresolved claim with its construction obligations."""
    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.OPEN,
        value=None,
        hypotheses=tuple(hypotheses),
    )


def _conditional_claim(
    statement: str,
    *hypotheses: str,
    evidence: Tuple[str, ...] = (),
) -> ClaimPacket:
    """Return a conditional claim without supplying a numerical value."""
    return ClaimPacket(
        statement=statement,
        status=ClaimStatus.CONDITIONAL,
        value=None,
        evidence=evidence,
        hypotheses=tuple(hypotheses),
    )


# ============================================================================
# 1.  Data structures
# ============================================================================

@dataclass(frozen=True)
class MinimalWAlgebraData:
    """Arithmetic data and typed claims for ``W^k(so_N,f_min)``."""

    lie_type: str           # "so_N"
    N: int                  # orthogonal dimension, N >= 7
    level: object           # typically k = -1
    central_charge: object  # c(k)
    reciprocal_weight_diagnostic: Rational
    anomaly_ratio: ClaimPacket
    kappa: ClaimPacket
    modular_conductor: ClaimPacket
    n_generators: int       # number of strong generators
    generator_weights: Tuple[object, ...]  # conformal weights
    generator_parities: Tuple[str, ...]    # every represented generator is even
    shadow_class: ClaimPacket
    shadow_depth: ClaimPacket
    orbifold_realization_at_minus_1: ClaimPacket
    strong_rationality_at_minus_1: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket
    koszul_status: ClaimPacket

    @property
    def is_rational_at_minus_1(self) -> Optional[bool]:
        """Resolve rationality only where strong rationality is source-backed."""

        value = self.strong_rationality_at_minus_1.value
        return True if value is True else None

    @property
    def is_c2_cofinite(self) -> Optional[bool]:
        """Resolve ``C_2``-cofiniteness through the same source-backed claim."""

        value = self.strong_rationality_at_minus_1.value
        return True if value is True else None


@dataclass(frozen=True)
class HookSuccessiveReductionData:
    """Hook arithmetic, a candidate corridor, and typed comparison claims."""

    N: int
    partition: Partition
    transpose: Partition
    candidate_partition_corridor: Tuple[Partition, ...]
    n_candidate_steps: int
    reduction_by_stages: ClaimPacket
    koszul_by_transport: ClaimPacket
    c_complementarity: object   # c(k) + c(k') at dual level
    reciprocal_weight_diagnostic: Rational
    anomaly_ratio: ClaimPacket
    kappa_source: ClaimPacket
    kappa_dual: ClaimPacket
    modular_conductor: ClaimPacket
    shadow_class: ClaimPacket
    shadow_depth: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket

    @property
    def kappa_sum(self) -> ClaimPacket:
        """Compatibility name for the typed modular conductor."""

        return self.modular_conductor


@dataclass(frozen=True)
class BuildingBlockBCDData:
    """Arithmetic data and typed claims for principal BCD W-algebras."""

    lie_type: str       # "B_n", "C_n", "D_n"
    rank: int           # n
    dim_g: int          # dimension of g
    h_dual: int         # dual Coxeter number
    n_generators: int   # number of strong generators = rank
    generator_weights: Tuple[int, ...]  # conformal weights (exponents + 1)
    central_charge: ClaimPacket
    reciprocal_weight_diagnostic: Rational
    anomaly_ratio: ClaimPacket
    kappa: ClaimPacket
    modular_conductor: ClaimPacket
    langlands_dual_type: str
    langlands_dual_level: ClaimPacket
    c_complementarity: ClaimPacket
    shadow_class: ClaimPacket
    shadow_depth: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket
    koszul_status: ClaimPacket


@dataclass(frozen=True)
class ConformalExtensionData:
    """A conformal-extension presentation and its bar-transport claim."""

    source_algebra: str     # e.g. "V_k(sl_3)"
    extension_type: str     # "simple current", "coset", "orbifold"
    w_algebra: str          # e.g. "W^k(sl_3)"
    level: object
    source_presentation: Optional[str]
    source_reference: Optional[str]
    koszul_inherited: ClaimPacket

    @property
    def koszul_status(self) -> ClaimPacket:
        """Compatibility name for the inheritance claim."""

        return self.koszul_inherited


@dataclass(frozen=True)
class KLCategoryEquivalenceData:
    """Level data and a typed MC3 transport claim."""

    source_algebra: str
    source_level: object
    target_algebra: str
    target_level: object
    equivalence_type: str   # "conformal_embedding", "ds_reduction", "coset"
    level_regime: str
    nilpotent_orbit: Optional[str]
    source_reference: Optional[str]
    braided_equivalence: ClaimPacket
    mc3_consequence: ClaimPacket


@dataclass(frozen=True)
class CreutzigLandscapeEntry:
    """One arithmetic profile with every geometric lift typed."""

    family_name: str
    lie_type: str
    central_charge: object
    reciprocal_weight_diagnostic: Rational
    kappa: ClaimPacket
    anomaly_ratio: ClaimPacket
    modular_conductor: ClaimPacket
    c_complementarity: object
    shadow_class: ClaimPacket
    shadow_depth: ClaimPacket
    ds_bar_commutation: ClaimPacket
    koszul_duality: ClaimPacket
    ksdual_membership: ClaimPacket
    koszul_status: ClaimPacket
    source_paper: str
    notes: str


# ============================================================================
# 2.  Lie algebra data for types B, C, D
# ============================================================================

def _so_dim(N: int) -> int:
    """Dimension of so_N = N(N-1)/2."""
    return N * (N - 1) // 2


def _sp_dim(n: int) -> int:
    """Dimension of sp_{2n} = n(2n+1)."""
    return n * (2 * n + 1)


def _lie_data_type_b(n: int) -> Dict[str, Any]:
    """Lie algebra data for B_n = so_{2n+1}, n >= 2.

    Exponents: 1, 3, 5, ..., 2n-1.
    h^v = 2n - 1.
    dim = n(2n+1).
    """
    if n < 2:
        raise ValueError(f"B_n requires n >= 2, got n={n}")
    N = 2 * n + 1
    return {
        'type': f'B_{n}',
        'lie_algebra': f'so_{N}',
        'rank': n,
        'dim': _so_dim(N),
        'h_dual': 2 * n - 1,
        'exponents': tuple(2 * i + 1 for i in range(n)),
        'generator_weights': tuple(2 * i + 2 for i in range(n)),
    }


def _lie_data_type_c(n: int) -> Dict[str, Any]:
    """Lie algebra data for C_n = sp_{2n}, n >= 2.

    Exponents: 1, 3, 5, ..., 2n-1.
    h^v = n + 1.
    dim = n(2n+1).
    """
    if n < 2:
        raise ValueError(f"C_n requires n >= 2, got n={n}")
    return {
        'type': f'C_{n}',
        'lie_algebra': f'sp_{2*n}',
        'rank': n,
        'dim': _sp_dim(n),
        'h_dual': n + 1,
        'exponents': tuple(2 * i + 1 for i in range(n)),
        'generator_weights': tuple(2 * i + 2 for i in range(n)),
    }


def _lie_data_type_d(n: int) -> Dict[str, Any]:
    """Lie algebra data for D_n = so_{2n}, n >= 3.

    Exponents: 1, 3, 5, ..., 2n-3, n-1.
    h^v = 2n - 2.
    dim = n(2n-1).
    """
    if n < 3:
        raise ValueError(f"D_n requires n >= 3, got n={n}")
    N = 2 * n
    exps = list(2 * i + 1 for i in range(n - 1))
    exps.append(n - 1)
    exps.sort()
    return {
        'type': f'D_{n}',
        'lie_algebra': f'so_{N}',
        'rank': n,
        'dim': _so_dim(N),
        'h_dual': 2 * n - 2,
        'exponents': tuple(exps),
        'generator_weights': tuple(e + 1 for e in exps),
    }


def _lie_data(lie_type: str, rank: int) -> Dict[str, Any]:
    """Dispatch to the appropriate Lie algebra data."""
    if lie_type.startswith('B'):
        return _lie_data_type_b(rank)
    elif lie_type.startswith('C'):
        return _lie_data_type_c(rank)
    elif lie_type.startswith('D'):
        return _lie_data_type_d(rank)
    else:
        raise ValueError(f"Unsupported lie_type: {lie_type}")


# ============================================================================
# 3.  Minimal W-algebras of so_N (Arakawa-Moreau conjecture)
# ============================================================================

def _minimal_so_generator_data(N: int) -> Tuple[
    int, Tuple[object, ...], Tuple[str, ...]
]:
    """Return the source-backed generator ledger for minimal ``so_N``.

    Put ``r=N-4``.  The even orbifold presentation has
    ``3 + r(r-1)/2`` weight-one generators, ``2r`` weight-``3/2``
    generators, and one Virasoro generator of weight two.  Every generator
    lies in the even subalgebra.
    """
    N = _exact_integer(N, "N", 7)

    r = N - 4
    n_weight_one = 3 + r * (r - 1) // 2
    n_weight_three_halves = 2 * r
    weights = (
        (Rational(1),) * n_weight_one
        + (Rational(3, 2),) * n_weight_three_halves
        + (Rational(2),)
    )
    parities = ("even",) * len(weights)
    return len(weights), weights, parities


def _minimal_so_reciprocal_weight_diagnostic(N: int) -> Rational:
    """Return the reciprocal-weight sum of the source-backed even ledger."""

    _, weights, _ = _minimal_so_generator_data(N)
    return sum(Rational(1) / weight for weight in weights)


def _minimal_so_central_charge(N: int, level=k_sym) -> object:
    r"""Return the minimal-W central charge in the source convention.

    Kac--Wakimoto's minimal-W formula, quoted as (M2) in the proof of
    Creutzig et al. (2025), gives

    ``k dim(so_N)/(k+N-2) - 6k + N - 6``.
    """

    _minimal_so_generator_data(N)
    k = _exact_expression(level, "level")
    return simplify(k * _so_dim(N) / (k + N - 2) - 6 * k + N - 6)


def minimal_w_so_data(N: int, level=k_sym) -> MinimalWAlgebraData:
    """Return arithmetic data and comparison obligations for minimal ``so_N``.

    The orbifold realization holds for every integer ``N >= 7``.  At level
    minus one, strong rationality is proved for even ``N >= 8``.  The odd
    family retains its source-visible strong-rationality obligation.
    """
    n_gen, weights, parities = _minimal_so_generator_data(N)
    diagnostic = _minimal_so_reciprocal_weight_diagnostic(N)
    c = _minimal_so_central_charge(N, level)
    k_val = _exact_expression(level, "level")
    if k_val == Rational(-1) and N % 2 == 0:
        strong_rationality = _proved_elsewhere_claim(
            f"strong rationality of W^{{-1}}(so_{N},f_min)",
            True,
            MINIMAL_SO_SOURCE,
        )
    else:
        strong_rationality = ClaimPacket(
            statement=f"strong rationality of W^{k_val}(so_{N},f_min)",
            status=ClaimStatus.OPEN,
            value=None,
            evidence=(
                f"{MINIMAL_SO_SOURCE}: orbifold realization for every N >= 7",
            ),
            hypotheses=(
                "a strong-rationality theorem for the supplied parity and level",
            ),
        )
    orbifold_realization = _proved_elsewhere_claim(
        f"orbifold realization of W^{{-1}}(so_{N},f_min)",
        True,
        (
            "Creutzig--Fasquel--Kovalchuk--Linshaw--Nakatsuka (2025), "
            "Theorem 1.1"
        ),
    )
    rho = _open_claim(
        f"rho of W^{k_val}(so_{N},f_min)",
        "a nonseparating genus-one calculation in the chosen normalization",
        "a comparison between the modular trace and the represented generator ledger",
    )
    kappa = _conditional_claim(
        f"kappa of W^{k_val}(so_{N},f_min)",
        "the genus-one trace comparison defining rho",
        "normalization compatibility with the central-charge lane",
    )
    modular_conductor = _open_claim(
        f"K^kappa of W^{k_val}(so_{N},f_min)",
        "modular characteristics for a specified Verdier comparison pair",
        "a common genus-one normalization at both levels",
    )
    ds_bar = _conditional_claim(
        f"DS--bar comparison for W^{k_val}(so_{N},f_min)",
        "a filtered BRST/bar comparison with strict completion",
        "a finite or continuously perfect Verdier pairing",
    )
    koszul = _conditional_claim(
        f"chiral Koszulness of W^{k_val}(so_{N},f_min)",
        "a bar-Ext versus ordinary-Ext comparison with completion control",
        "diagonal concentration of the completed chiral bar spectral sequence",
        evidence=(
            f"{MINIMAL_SO_SOURCE}: orbifold realization for every N >= 7; "
            "strong rationality for even N at level -1",
        ),
    )

    return MinimalWAlgebraData(
        lie_type=f"so_{N}",
        N=N,
        level=k_val,
        central_charge=c,
        reciprocal_weight_diagnostic=diagnostic,
        anomaly_ratio=rho,
        kappa=kappa,
        modular_conductor=modular_conductor,
        n_generators=n_gen,
        generator_weights=weights,
        generator_parities=parities,
        shadow_class=_open_claim(
            f"full shadow class of W^{k_val}(so_{N},f_min)",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        shadow_depth=_open_claim(
            f"full shadow depth of W^{k_val}(so_{N},f_min)",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        orbifold_realization_at_minus_1=orbifold_realization,
        strong_rationality_at_minus_1=strong_rationality,
        ds_bar_commutation=ds_bar,
        koszul_duality=_conditional_claim(
            f"object-level Koszul comparison for W^{k_val}(so_{N},f_min)",
            *ds_bar.hypotheses,
            "identification of the Verdier companion",
        ),
        ksdual_membership=_open_claim(
            f"KSDual membership of W^{k_val}(so_{N},f_min)",
            "an object-level fixed-point equivalence in the completed Verdier--Koszul ambient",
        ),
        koszul_status=koszul,
    )


def minimal_so_at_minus_1(N: int) -> MinimalWAlgebraData:
    """Specialization to level k = -1 (the Arakawa-Moreau case)."""
    return minimal_w_so_data(N, level=Rational(-1))


# ============================================================================
# 4.  Hook-type successive reductions [2403.08212]
# ============================================================================

def _hook_candidate_partition_corridor(N: int, r: int) -> Tuple[Partition, ...]:
    """Combinatorial corridor from ``[N]`` to ``[N-r,1^r]``.

    The tuple records partition incidence only:
        [N] -> [N-1, 1] -> [N-2, 1^2] -> ... -> [N-r, 1^r]

    A reduction functor between adjacent entries is a separate theorem.
    """
    chain = []
    for i in range(r + 1):
        parts = [N - i] + [1] * i
        chain.append(normalize_partition(parts))
    return tuple(chain)


def hook_successive_reduction_data(
    N: int, r: int, level=k_sym
) -> HookSuccessiveReductionData:
    """Return a hook profile and its reduction-by-stages obligation.

    The partition chain and KRW central-charge arithmetic are exact.  Transport
    of chiral bar Koszulness through the inverse reductions requires the
    filtered DS/bar comparison package and is returned as a conditional packet.
    """
    N = _exact_integer(N, "N", 2)
    r = _exact_integer(r, "r", 0)
    if r < 0 or r >= N - 1:
        raise ValueError(f"Hook requires 0 <= r < N-1, got r={r}, N={N}")

    lam = hook_partition(N, r)
    lam_t = transpose_partition(lam)
    corridor = _hook_candidate_partition_corridor(N, r)
    k = _exact_expression(level, "level")
    kv = hook_dual_level_sl_n(N, k)

    # Central charge complementarity
    c_source = krw_central_charge(lam, k)
    c_dual = krw_central_charge(lam_t, kv)
    c_comp = simplify(c_source + c_dual)

    diagnostic = reciprocal_weight_diagnostic_from_partition(lam)
    rho = anomaly_ratio_from_partition(lam)
    kap_source = ds_kappa_from_affine(lam, k)
    kap_dual = ds_kappa_from_affine(lam_t, kv)
    kap_sum = kappa_complementarity_sum(lam, k)
    reduction_by_stages = ClaimPacket(
        statement=f"reduction by stages along the corridor ending at {lam}",
        status=ClaimStatus.OPEN,
        value=None,
        evidence=(
            f"{TYPE_A_STAGES_SOURCE}: general reduction by stages is Conjecture A; "
            "Theorem A proves three specified low-rank reductions",
        ),
        hypotheses=(
            "Conjecture A for the supplied target and its specified sequence of hook reductions",
        ),
    )
    ds_bar = _conditional_claim(
        f"DS--bar commutation along the hook chain ending at {lam}",
        "a reduction-by-stages theorem for the supplied corridor",
        H_HOOK_DS_BAR,
        evidence=(TYPE_A_STAGES_SOURCE,),
    )
    koszul_transport = _conditional_claim(
        f"transport of chiral bar Koszulness along the hook chain ending at {lam}",
        "a reduction-by-stages theorem for the supplied corridor",
        H_HOOK_DS_BAR,
        "preservation of the completed chiral bar filtration at every inverse reduction",
        evidence=(
            TYPE_A_STAGES_SOURCE,
            "thm:w-algebra-koszul-main at the principal endpoint",
        ),
    )
    koszul_duality = _conditional_claim(
        f"object-level Koszul comparison for the transpose pair {lam}, {lam_t}",
        H_HOOK_DS_BAR,
    )
    ksdual_membership = _open_claim(
        f"KSDual membership for the hook partition {lam}",
        "an object-level fixed-point equivalence compatible with DS/bar transport",
    )
    shadow = _open_claim(
        f"full shadow class for the hook partition {lam}",
        "all generator channels in the Maurer--Cartan tower and collision normalization",
    )
    shadow_depth = _open_claim(
        f"full shadow depth for the hook partition {lam}",
        "all generator channels in the Maurer--Cartan tower and collision normalization",
    )

    return HookSuccessiveReductionData(
        N=N,
        partition=lam,
        transpose=lam_t,
        candidate_partition_corridor=corridor,
        n_candidate_steps=r,
        reduction_by_stages=reduction_by_stages,
        koszul_by_transport=koszul_transport,
        c_complementarity=c_comp,
        reciprocal_weight_diagnostic=diagnostic,
        anomaly_ratio=rho,
        kappa_source=kap_source,
        kappa_dual=kap_dual,
        modular_conductor=kap_sum,
        shadow_class=shadow,
        shadow_depth=shadow_depth,
        ds_bar_commutation=ds_bar,
        koszul_duality=koszul_duality,
        ksdual_membership=ksdual_membership,
    )


# ============================================================================
# 5.  Building blocks for types B, C, D [2409.03465]
# ============================================================================

def _bcd_reciprocal_weight_diagnostic(generator_weights: Tuple[int, ...]) -> Rational:
    """Return the reciprocal sum of the represented principal generator weights."""

    return sum(Rational(1, h) for h in generator_weights)


def _langlands_dual_bcd_type(lie_type: str) -> str:
    """Return the Langlands-dual classical type."""

    family = lie_type[0]
    if family == "B":
        return "C"
    if family == "C":
        return "B"
    if family == "D":
        return "D"
    raise ValueError(f"Unsupported lie_type: {lie_type}")


def d3_a3_incomplete_ansatz_discrepancy(level=k_sym) -> object:
    r"""Return the ``D_3=A_3`` discrepancy detecting the incomplete ansatz.

    The rank-minus-pole expression gives ``3-60/(k+4)``.  KRW (2003),
    Theorem 2.1(a), equation (2.6), applied to principal ``sl_4`` gives the
    source-backed value.  Their difference is ``60k+120``.
    """

    k = _exact_expression(level, "level")
    incomplete_rank_pole_expression = 3 - Rational(60) / (k + 4)
    exact_a3 = krw_central_charge((4,), k)
    return simplify(incomplete_rank_pole_expression - exact_a3)


def building_block_bcd_data(
    lie_type: str, rank: int, level=k_sym
) -> BuildingBlockBCDData:
    """Return represented BCD generator arithmetic and source obligations."""

    rank = _exact_integer(rank, "rank", 0)
    data = _lie_data(lie_type, rank)
    gen_weights = data['generator_weights']
    diagnostic = _bcd_reciprocal_weight_diagnostic(gen_weights)
    k = _exact_expression(level, "level")
    h_dual = data['h_dual']
    dual_family = _langlands_dual_bcd_type(data['type'])
    dual_type = f"{dual_family}_{rank}"
    package = (
        "H_principal^{DS/bar}: filtered DS/bar comparison, strict completion, "
        "and a finite or continuously perfect Verdier pairing"
    )
    rho = _open_claim(
        f"rho of principal {data['type']}",
        "a nonseparating genus-one calculation",
        "a theorem identifying rho with the reciprocal-weight diagnostic",
    )
    kappa = _conditional_claim(
        f"kappa of principal {data['type']}",
        "the genus-one trace comparison defining rho",
        "normalization compatibility with the central-charge lane",
    )
    ds_bar = _conditional_claim(
        f"DS--bar comparison for principal {data['type']}",
        package,
    )
    central_charge = ClaimPacket(
        statement=f"principal central charge of {data['type']} at level {k}",
        status=ClaimStatus.OPEN,
        value=None,
        evidence=(
            "the D_3=A_3 oracle gives discrepancy 60*k+120 for the incomplete rank-minus-pole expression",
        ),
        hypotheses=(
            "the complete Kac--Roan--Wakimoto formula in one fixed non-simply-laced convention",
            "an explicit good grading and invariant-form normalization",
        ),
    )
    dual_level = _open_claim(
        f"Langlands-dual level from {data['type']} to {dual_type}",
        "a fixed-convention Feigin--Frenkel level relation for the Langlands-dual pair",
    )
    c_comp = _open_claim(
        f"reflected central-charge sum for principal {data['type']} and {dual_type}",
        "resolved source and target central-charge packets in one convention",
        "a resolved Langlands-dual level packet",
    )

    return BuildingBlockBCDData(
        lie_type=data['type'],
        rank=rank,
        dim_g=data['dim'],
        h_dual=h_dual,
        n_generators=len(gen_weights),
        generator_weights=gen_weights,
        central_charge=central_charge,
        reciprocal_weight_diagnostic=diagnostic,
        anomaly_ratio=rho,
        kappa=kappa,
        modular_conductor=_open_claim(
            f"K^kappa of principal {data['type']}",
            "modular characteristics in a common convention at both reflected levels",
            package,
        ),
        langlands_dual_type=dual_type,
        langlands_dual_level=dual_level,
        c_complementarity=c_comp,
        shadow_class=_open_claim(
            f"full shadow class of principal {data['type']}",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        shadow_depth=_open_claim(
            f"full shadow depth of principal {data['type']}",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        ds_bar_commutation=ds_bar,
        koszul_duality=_conditional_claim(
            f"object-level Koszul comparison for principal {data['type']}",
            package,
            "the hypotheses of thm:w-algebra-koszul-main",
        ),
        ksdual_membership=_open_claim(
            f"KSDual membership of principal {data['type']}",
            "an object-level fixed-point equivalence in the completed Verdier--Koszul ambient",
        ),
        koszul_status=_conditional_claim(
            f"chiral Koszulness of principal {data['type']}",
            package,
            "the PBW, Verdier, and genus-one trace hypotheses of thm:w-algebra-koszul-main",
            evidence=("chapters/examples/w_algebras.tex:413-440",),
        ),
    )


# ============================================================================
# 6.  Conformal extension Koszulness [2508.18889]
# ============================================================================

def conformal_extension_koszulness(
    source_type: str,
    source_rank: int,
    source_level: object,
    extension_type: str = "simple_current",
    *,
    source_presentation: Optional[str] = None,
    source_reference: Optional[str] = None,
) -> ConformalExtensionData:
    """Return the completed-bar obligation for a cited presentation.

    A source presentation and an author--year--result reference place the
    extension in a checkable theorem domain.  An arbitrary algebra label
    carries an open presentation packet.
    """

    source_rank = _exact_integer(source_rank, "source_rank", 1)
    k = _exact_expression(source_level, "source_level")
    source_backed = bool(source_presentation) and _has_precise_result_reference(
        source_reference
    )
    if source_backed:
        inheritance = _conditional_claim(
            f"chiral Koszulness transported through the {extension_type} extension",
            "chiral Koszulness of the augmented source algebra",
            f"compatibility of the {extension_type} presentation with the completed chiral bar filtration",
            "convergence and diagonal concentration for the extension spectral sequence",
            evidence=(source_presentation, source_reference),
        )
    else:
        inheritance = _open_claim(
            f"chiral Koszulness transported through the {extension_type} presentation",
            "a source-backed presentation with author, year, and numbered theorem",
            "a functorial completed-bar comparison for the stated extension type",
            "chiral Koszulness of the augmented source algebra",
        )
    return ConformalExtensionData(
        source_algebra=f"V_{k}({source_type}_{source_rank})",
        extension_type=extension_type,
        w_algebra=f"W^{k}({source_type}_{source_rank})",
        level=k,
        source_presentation=source_presentation,
        source_reference=source_reference,
        koszul_inherited=inheritance,
    )


# ============================================================================
# 7.  KL-category equivalence and MC3 [2603.04667]
# ============================================================================

def kl_category_equivalence(
    source_type: str,
    source_rank: int,
    source_level: object,
    target_type: str,
    target_rank: int,
    target_level: object,
    equivalence_type: str = "ds_reduction",
    *,
    nilpotent_orbit: Optional[str] = None,
    source_reference: Optional[str] = None,
) -> KLCategoryEquivalenceData:
    """Return the source theorem and the distinct MC3 transport packet."""

    source_rank = _exact_integer(source_rank, "source_rank", 1)
    target_rank = _exact_integer(target_rank, "target_rank", 1)
    k = _exact_expression(source_level, "source_level")
    kp = _exact_expression(target_level, "target_level")
    if k.is_rational is True and kp.is_rational is True:
        level_regime = "rational"
    elif k.is_rational is False or kp.is_rational is False:
        level_regime = "irrational"
    else:
        level_regime = "symbolic"
    theorem_domain_hypotheses = (
        "a simple simply-laced source Lie algebra",
        "an exact irrational source level",
        "quantum Drinfeld--Sokolov reduction for a specified nilpotent orbit",
        "the W-algebra target for the same Lie algebra and level",
        "Creutzig--Dhillon--Nakatsuka (2026), Theorem 1.1 (= Theorem 5.2)",
    )
    in_theorem_domain = (
        equivalence_type == "ds_reduction"
        and _is_simple_simply_laced_type(source_type, source_rank)
        and k.is_rational is False
        and simplify(kp - k) == 0
        and target_type == "W"
        and target_rank == source_rank
        and bool(nilpotent_orbit)
        and source_reference == KL_SOURCE
    )
    if in_theorem_domain:
        braided_equivalence = _proved_elsewhere_claim(
            "braided tensor equivalence induced by quantum DS reduction",
            True,
            KL_SOURCE,
        )
        mc3 = _conditional_claim(
            "MC3 transport from the KL category to the W-algebra module category",
            "the source-backed braided equivalence packet",
            "preservation of compact objects and thick closure by the DS functor",
            evidence=(KL_SOURCE,),
        )
    else:
        extra_hypotheses = ()
        if source_type.strip().upper() in {"B", "C"}:
            extra_hypotheses = (
                "a theorem with the Langlands-dual target and its fixed-convention dual level",
            )
        braided_equivalence = _open_claim(
            "braided tensor equivalence for the supplied algebra-level pair",
            *theorem_domain_hypotheses,
            *extra_hypotheses,
        )
        mc3 = _open_claim(
            f"MC3 transport for the {equivalence_type} presentation",
            "a resolved source-backed braided-equivalence packet",
            "preservation of compact generators and thick closure",
        )

    return KLCategoryEquivalenceData(
        source_algebra=f"{source_type}_{source_rank}",
        source_level=k,
        target_algebra=f"{target_type}_{target_rank}",
        target_level=kp,
        equivalence_type=equivalence_type,
        level_regime=level_regime,
        nilpotent_orbit=nilpotent_orbit,
        source_reference=source_reference,
        braided_equivalence=braided_equivalence,
        mc3_consequence=mc3,
    )


# ============================================================================
# 8.  Landscape catalog assembly
# ============================================================================

def _type_a_principal_entry(N: int, level=k_sym) -> CreutzigLandscapeEntry:
    """Landscape entry for W_N = W^k(sl_N, f_prin)."""
    lam = normalize_partition([N])
    k = _exact_expression(level, "level")
    kv = hook_dual_level_sl_n(N, k)
    c = krw_central_charge(lam, k)
    diagnostic = reciprocal_weight_diagnostic_from_partition(lam)
    rho = anomaly_ratio_from_partition(lam)
    kap = ds_kappa_from_affine(lam, k)
    conductor = kappa_complementarity_sum(lam, k)
    c_dual = krw_central_charge(lam, kv)
    c_comp = simplify(c + c_dual)
    ds_bar = _conditional_claim(
        f"DS--bar comparison for the principal W_{N} algebra",
        H_HOOK_DS_BAR,
        "the filtered DS/bar hypotheses of thm:w-algebra-koszul-main",
    )
    return CreutzigLandscapeEntry(
        family_name=f"W_{N}",
        lie_type=f"A_{N-1}",
        central_charge=c,
        reciprocal_weight_diagnostic=diagnostic,
        kappa=kap,
        anomaly_ratio=rho,
        modular_conductor=conductor,
        c_complementarity=c_comp,
        shadow_class=_open_claim(
            f"full shadow class of the principal W_{N} algebra",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        shadow_depth=_open_claim(
            f"full shadow depth of the principal W_{N} algebra",
            "the complete Maurer--Cartan tower with collision normalization",
        ),
        ds_bar_commutation=ds_bar,
        koszul_duality=_conditional_claim(
            f"object-level Koszul comparison for the principal W_{N} algebra",
            H_HOOK_DS_BAR,
            "continuous Verdier duality and the genus-one trace hypotheses of thm:w-algebra-koszul-main",
            evidence=("chapters/examples/w_algebras.tex:426-440",),
        ),
        ksdual_membership=_open_claim(
            f"KSDual membership of the principal W_{N} algebra",
            "an object-level fixed-point equivalence in the completed Verdier--Koszul ambient",
        ),
        koszul_status=_conditional_claim(
            f"principal W_{N} chiral Koszulness",
            H_HOOK_DS_BAR,
            "the filtered DS/bar, Verdier, and genus-one trace hypotheses of thm:w-algebra-koszul-main",
            evidence=("chapters/examples/w_algebras.tex:428",),
        ),
        source_paper=(
            "Kac--Roan--Wakimoto (2003), Theorem 2.1(a), equation (2.6); "
            "thm:w-algebra-koszul-main"
        ),
        notes=f"Principal W-algebra of sl_{N}",
    )


def _hook_entry(N: int, r: int, level=k_sym) -> CreutzigLandscapeEntry:
    """Landscape entry for hook-type W^k(sl_N, f_{[N-r,1^r]})."""
    data = hook_successive_reduction_data(N, r, level)
    return CreutzigLandscapeEntry(
        family_name=f"W(sl_{N}, [{N-r},1^{r}])",
        lie_type=f"A_{N-1}",
        central_charge=krw_central_charge(data.partition, level),
        reciprocal_weight_diagnostic=data.reciprocal_weight_diagnostic,
        kappa=data.kappa_source,
        anomaly_ratio=data.anomaly_ratio,
        modular_conductor=data.modular_conductor,
        c_complementarity=data.c_complementarity,
        shadow_class=data.shadow_class,
        shadow_depth=data.shadow_depth,
        ds_bar_commutation=data.ds_bar_commutation,
        koszul_duality=data.koszul_duality,
        ksdual_membership=data.ksdual_membership,
        koszul_status=data.koszul_by_transport,
        source_paper=f"{TYPE_A_STAGES_SOURCE}; thm:hook-transport-corridor",
        notes=(
            f"Hook type, {data.n_candidate_steps} candidate partition incidences "
            "from the principal partition"
        ),
    )


def _minimal_so_entry(N: int) -> CreutzigLandscapeEntry:
    """Landscape entry for W^{-1}(so_N, f_min)."""
    data = minimal_so_at_minus_1(N)
    return CreutzigLandscapeEntry(
        family_name=f"W^{{-1}}(so_{N}, f_min)",
        lie_type=f"B_{(N-1)//2}",
        central_charge=data.central_charge,
        reciprocal_weight_diagnostic=data.reciprocal_weight_diagnostic,
        kappa=data.kappa,
        anomaly_ratio=data.anomaly_ratio,
        modular_conductor=data.modular_conductor,
        c_complementarity="N/A (specialized level)",
        shadow_class=data.shadow_class,
        shadow_depth=data.shadow_depth,
        ds_bar_commutation=data.ds_bar_commutation,
        koszul_duality=data.koszul_duality,
        ksdual_membership=data.ksdual_membership,
        koszul_status=data.koszul_status,
        source_paper=MINIMAL_SO_SOURCE,
        notes=(
            "Orbifold realization at k=-1; strong rationality is source-backed "
            "for even N and remains an explicit obligation for odd N"
        ),
    )


def _bcd_entry(lie_type: str, rank: int, level=k_sym) -> CreutzigLandscapeEntry:
    """Landscape entry for principal W^k(g) of type B/C/D."""
    data = building_block_bcd_data(lie_type, rank, level)
    return CreutzigLandscapeEntry(
        family_name=f"W({data.lie_type})",
        lie_type=data.lie_type,
        central_charge=data.central_charge,
        reciprocal_weight_diagnostic=data.reciprocal_weight_diagnostic,
        kappa=data.kappa,
        anomaly_ratio=data.anomaly_ratio,
        modular_conductor=data.modular_conductor,
        c_complementarity=data.c_complementarity,
        shadow_class=data.shadow_class,
        shadow_depth=data.shadow_depth,
        ds_bar_commutation=data.ds_bar_commutation,
        koszul_duality=data.koszul_duality,
        ksdual_membership=data.ksdual_membership,
        koszul_status=data.koszul_status,
        source_paper=(
            "Creutzig--Kovalchuk--Linshaw (2025), Theorems 6.3 and 7.2; "
            "thm:w-algebra-koszul-main"
        ),
        notes=f"Principal W-algebra of {data.lie_type}",
    )


def creutzig_landscape_catalog(level=k_sym) -> List[CreutzigLandscapeEntry]:
    """Return the configured 27-row finite landscape truncation.

    Returns a list of CreutzigLandscapeEntry objects covering:
    1. Type A principal: W_2 through W_6
    2. Hook-type: all hooks in sl_3 through sl_6
    3. Minimal so_N: so_7, so_9, so_11
    4. Types B, C, D principal: B_2..B_4, C_2..C_4, D_3..D_5
    """
    level = _exact_expression(level, "level")
    entries = []

    # Type A principal
    for N in range(2, 7):
        entries.append(_type_a_principal_entry(N, level))

    # Hook-type in sl_3 through sl_6
    for N in range(3, 7):
        for r in range(1, N - 1):
            entries.append(_hook_entry(N, r, level))

    # Minimal so_N at level -1
    for N in [7, 9, 11]:
        entries.append(_minimal_so_entry(N))

    # Types B, C, D
    for n in range(2, 5):
        entries.append(_bcd_entry('B', n, level))
        entries.append(_bcd_entry('C', n, level))
    for n in range(3, 6):
        entries.append(_bcd_entry('D', n, level))

    return entries


# ============================================================================
# 9.  Cross-checks and consistency
# ============================================================================

def verify_type_a_kappa_consistency(N: int, level=k_sym) -> ClaimPacket:
    """Return the open comparison between ``kappa`` and a weight diagnostic.

    The reciprocal-weight sum ``H_N-1`` is exact generator arithmetic.  Its
    identification with the genus-one anomaly ratio is an open comparison;
    consequently this routine preserves the packets supplied by the canonical
    hook engine and performs no symbolic arithmetic on them.
    """
    N = _exact_integer(N, "N", 2)
    lam = normalize_partition([N])
    k = _exact_expression(level, "level")
    kap = ds_kappa_from_affine(lam, k)
    rho = anomaly_ratio_from_partition(lam)
    harmonic_tail = sum(Rational(1, j) for j in range(2, N + 1))
    hypotheses = tuple(dict.fromkeys(
        (*kap.hypotheses, *rho.hypotheses, "identification of rho with the reciprocal-weight diagnostic")
    ))
    return ClaimPacket(
        statement=f"kappa(W_{N}) = c(W_{N}) times the diagnostic {harmonic_tail}",
        status=ClaimStatus.OPEN,
        value=None,
        evidence=(f"exact principal generator diagnostic H_{N}-1={harmonic_tail}",),
        hypotheses=hypotheses,
    )


def verify_c_complementarity_k_independent(
    partition: Partition, level=k_sym
) -> bool:
    """Test level-independence of the exact type-A central-charge sum."""
    lam = normalize_partition(partition)
    lam_t = transpose_partition(lam)
    N = partition_size(lam)
    k = _exact_expression(level, "level")
    kv = hook_dual_level_sl_n(N, k)
    c_sum = simplify(krw_central_charge(lam, k) + krw_central_charge(lam_t, kv))
    return all(simplify(diff(c_sum, parameter)) == 0 for parameter in k.free_symbols)


def verify_bcd_c_complementarity(
    lie_type: str, rank: int, level=k_sym
) -> ClaimPacket:
    """Return the open fixed-convention BCD complementarity packet."""

    return building_block_bcd_data(lie_type, rank, level).c_complementarity


def verify_hook_koszulness_chain(N: int) -> Dict[Partition, ClaimPacket]:
    """Return conditional endpoint and hook-transport packets."""
    N = _exact_integer(N, "N", 2)
    results = {}
    for r in range(N):
        lam = hook_partition(N, r)
        if r == N - 1:
            results[lam] = _conditional_claim(
                f"affine endpoint Koszulness for sl_{N}",
                "the completed chiral PBW/bar comparison",
                evidence=("affine PBW arithmetic",),
            )
        elif r == 0:
            results[lam] = _conditional_claim(
                f"principal W_{N} chiral Koszulness",
                H_HOOK_DS_BAR,
                "the filtered DS/bar, Verdier, and genus-one trace hypotheses of thm:w-algebra-koszul-main",
                evidence=("chapters/examples/w_algebras.tex:428",),
            )
        else:
            data = hook_successive_reduction_data(N, r)
            results[lam] = data.koszul_by_transport
    return results


def bar_cobar_kl_commutation_check(
    lie_type: str, rank: int, source_level: object, target_level: object
) -> ClaimPacket:
    """Return the open arity-two KL/bar comparison obligation.

    The KL equivalence lives in module categories.  The chiral bar construction
    lives on augmented algebra objects.  A comparison therefore consists of a
    functor on augmented algebras, its compatibility with completed bar
    filtrations, and a genus-one trace comparison.  The packet records this
    additional structure.
    """
    source = _exact_expression(source_level, "source_level")
    target = _exact_expression(target_level, "target_level")
    return _open_claim(
        f"arity-two KL/bar comparison for {lie_type}_{rank} at levels "
        f"{source} and {target}",
        "resolved modular-characteristic packets at both levels",
        "a theorem comparing the KL functor with the completed chiral bar construction",
    )


# ============================================================================
# 10.  Summary statistics
# ============================================================================

def landscape_summary() -> Dict[str, Any]:
    """Summary statistics for the configured finite truncation."""
    catalog = creutzig_landscape_catalog()
    n_total = len(catalog)
    n_proved = sum(
        1
        for e in catalog
        if e.koszul_status.status in {ClaimStatus.PROVED_HERE, ClaimStatus.PROVED_ELSEWHERE}
        and e.koszul_status.value is True
    )
    n_class_m = sum(1 for e in catalog if e.shadow_class.value == "M")
    n_class_l = sum(1 for e in catalog if e.shadow_class.value == "L")
    n_class_c = sum(1 for e in catalog if e.shadow_class.value == "C")
    families = set(e.lie_type for e in catalog)
    kappa_statuses = Counter(e.kappa.status.value for e in catalog)
    rho_statuses = Counter(e.anomaly_ratio.status.value for e in catalog)
    conductor_statuses = Counter(e.modular_conductor.status.value for e in catalog)
    ds_bar_statuses = Counter(e.ds_bar_commutation.status.value for e in catalog)
    duality_statuses = Counter(e.koszul_duality.status.value for e in catalog)
    ksdual_statuses = Counter(e.ksdual_membership.status.value for e in catalog)
    koszul_statuses = Counter(e.koszul_status.status.value for e in catalog)

    return {
        'n_configured_rows': n_total,
        'n_proved_koszul': n_proved,
        'n_class_M': n_class_m,
        'n_class_L': n_class_l,
        'n_class_C': n_class_c,
        'n_resolved_kappa': sum(e.kappa.resolved for e in catalog),
        'n_resolved_rho': sum(e.anomaly_ratio.resolved for e in catalog),
        'n_resolved_modular_conductor': sum(e.modular_conductor.resolved for e in catalog),
        'n_resolved_full_shadow_class': sum(e.shadow_class.resolved for e in catalog),
        'n_resolved_full_shadow_depth': sum(e.shadow_depth.resolved for e in catalog),
        'kappa_status_counts': dict(sorted(kappa_statuses.items())),
        'rho_status_counts': dict(sorted(rho_statuses.items())),
        'modular_conductor_status_counts': dict(sorted(conductor_statuses.items())),
        'ds_bar_status_counts': dict(sorted(ds_bar_statuses.items())),
        'koszul_duality_status_counts': dict(sorted(duality_statuses.items())),
        'ksdual_status_counts': dict(sorted(ksdual_statuses.items())),
        'koszul_status_counts': dict(sorted(koszul_statuses.items())),
        'lie_types_covered': sorted(families),
        'configured_bounds': {
            'type_A_principal_N': (2, 6),
            'type_A_hook_N': (3, 6),
            'minimal_so_N': (7, 9, 11),
            'B_rank': (2, 4),
            'C_rank': (2, 4),
            'D_rank': (3, 5),
        },
        'isomorphism_aliases': {
            'B_2': 'C_2',
            'D_3': 'A_3',
        },
        'new_families_from_creutzig': [
            'minimal so_N at level -1',
            'hook-type successive reductions (type A)',
            'principal W(B_n), W(C_n), W(D_n)',
            'conformal extensions',
        ],
    }
